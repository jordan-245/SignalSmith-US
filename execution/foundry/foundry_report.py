"""Signal Foundry — Daily Report Generator.

Generates a comprehensive daily report per market (US / ASX) containing:
  - Top rankings table with probabilities (P(up) 1D/5D/20D), expected return, downside tail risk
  - Catalyst map (placeholder; pulls from Supabase docs_extracted if available)
  - Regime summary (current regime label + recent history)
  - Trade plans per top ticker: entry, invalidation (stop), position sizing
  - Calibration summary: AUC, calibration error, hit rate
  - Model consensus: individual model scores + ensemble

Outputs:
  - Markdown report  -> output/foundry/reports/{market}/YYYY-MM-DD.md
  - HTML report      -> output/foundry/reports/{market}/YYYY-MM-DD.html

Usage:
  python -m execution.foundry.foundry_report --market US --date 2026-02-07
  python -m execution.foundry.foundry_report --market ASX --date 2026-02-07

Can also be imported:
  from execution.foundry.foundry_report import generate_report
  md, html_str = generate_report(market="US", as_of_str="2026-02-07")
"""

from __future__ import annotations

import argparse
import datetime as dt
import html as html_module
import json
import logging
import math
import os
import sys
from pathlib import Path
from typing import Any, Dict, List, Optional, Tuple

import numpy as np
import pandas as pd

try:
    from jinja2 import Template
except ImportError:
    Template = None  # type: ignore

logger = logging.getLogger("foundry.report")

# Import shared utilities from foundry_steps / foundry_models to avoid duplication.
# Try package-qualified imports first, then bare imports (for direct execution).
try:
    from execution.foundry.foundry_steps import load_universe
except ImportError:
    try:
        from foundry_steps import load_universe
    except ImportError:
        load_universe = None  # type: ignore  — defined below as fallback

try:
    from execution.foundry.foundry_models import (
        FEATURE_COLS as _FEATURE_COLS,
        EnsembleModel,
        CalibrationWrapper,
        train_model_stack,
    )
except ImportError:
    try:
        from foundry_models import (
            FEATURE_COLS as _FEATURE_COLS,
            EnsembleModel,
            CalibrationWrapper,
            train_model_stack,
        )
    except ImportError:
        _FEATURE_COLS = None
        EnsembleModel = None  # type: ignore
        CalibrationWrapper = None  # type: ignore
        train_model_stack = None  # type: ignore

# ---------------------------------------------------------------------------
# Paths
# ---------------------------------------------------------------------------
REPO = Path(__file__).resolve().parents[2]
DATA = REPO / "data" / "foundry"
OUTPUT = REPO / "output" / "foundry" / "reports"
DIRECTIVES = REPO / "directives" / "foundry"

# ---------------------------------------------------------------------------
# Portfolio defaults
# ---------------------------------------------------------------------------
DEFAULT_PORTFOLIO = 5000.0
DEFAULT_RISK_PER_TRADE_PCT = 2.0
TOP_N = 20
ATR_PERIOD = 14


# ===================================================================
# Data loaders
# ===================================================================

# load_universe is imported from foundry_steps above.
# Fallback definition only if the import failed.
if load_universe is None:
    def load_universe(market: str) -> List[str]:
        """Load ticker universe from directives file (fallback)."""
        fname = "universe_us.txt" if market == "US" else "universe_asx.txt"
        f = DIRECTIVES / fname
        if not f.exists():
            return []
        out: List[str] = []
        seen: set = set()
        for line in f.read_text(encoding="utf-8").splitlines():
            s = line.strip()
            if not s or s.startswith("#"):
                continue
            t = s.upper()
            if t not in seen:
                out.append(t)
                seen.add(t)
        return out


def _find_latest_run(market: str, kind: str = "predictions") -> Optional[Path]:
    """Find the most recent run_id parquet for a given kind/market."""
    base = DATA / kind / f"market={market}"
    if not base.exists():
        return None
    runs = sorted(base.glob("run_id=*"), key=lambda p: p.name, reverse=True)
    for r in runs:
        pq = r / "part.parquet"
        if pq.exists():
            return pq
    return None


def load_predictions(market: str, as_of: dt.date, run_id: Optional[str] = None) -> pd.DataFrame:
    if run_id:
        pq = DATA / "predictions" / f"market={market}" / f"run_id={run_id}" / "part.parquet"
        if pq.exists():
            return pd.read_parquet(pq)
    pq = _find_latest_run(market, "predictions")
    return pd.read_parquet(pq) if pq else pd.DataFrame()


def load_prices(market: str, as_of: dt.date, run_id: Optional[str] = None) -> pd.DataFrame:
    """Load price data from date-partitioned parquet (date=YYYY-MM-DD)."""
    base = DATA / "prices" / f"market={market}"
    if not base.exists():
        return pd.DataFrame()

    # Try exact date first
    pq = base / f"date={as_of.isoformat()}" / "part.parquet"
    if pq.exists():
        return pd.read_parquet(pq)

    # Fall back to reading all date partitions and concatenating
    date_dirs = sorted(base.glob("date=*"), reverse=True)
    frames: List[pd.DataFrame] = []
    for d in date_dirs:
        pq2 = d / "part.parquet"
        if pq2.exists():
            frames.append(pd.read_parquet(pq2))
    if frames:
        df = pd.concat(frames, ignore_index=True)
        # Standardize column name to "close"
        if "px" in df.columns and "close" not in df.columns:
            df = df.rename(columns={"px": "close"})
        return df
    return pd.DataFrame()


def load_features(market: str, as_of: dt.date, feature_set: str = "v1") -> pd.DataFrame:
    pq = DATA / "features" / f"market={market}" / f"feature_set={feature_set}" / f"date={as_of.isoformat()}" / "part.parquet"
    if pq.exists():
        return pd.read_parquet(pq)
    base = DATA / "features" / f"market={market}" / f"feature_set={feature_set}"
    if not base.exists():
        return pd.DataFrame()
    dates = sorted(base.glob("date=*"), reverse=True)
    for d in dates:
        pq2 = d / "part.parquet"
        if pq2.exists():
            return pd.read_parquet(pq2)
    return pd.DataFrame()


def load_labels(market: str, as_of: dt.date) -> pd.DataFrame:
    pq = DATA / "labels" / f"market={market}" / f"date={as_of.isoformat()}" / "part.parquet"
    if pq.exists():
        return pd.read_parquet(pq)
    base = DATA / "labels" / f"market={market}"
    if not base.exists():
        return pd.DataFrame()
    dates = sorted(base.glob("date=*"), reverse=True)
    for d in dates:
        pq2 = d / "part.parquet"
        if pq2.exists():
            return pd.read_parquet(pq2)
    return pd.DataFrame()


def load_backtests(market: str, run_id: Optional[str] = None) -> pd.DataFrame:
    if run_id:
        pq = DATA / "backtests" / f"market={market}" / f"run_id={run_id}" / "part.parquet"
        if pq.exists():
            return pd.read_parquet(pq)
    pq = _find_latest_run(market, "backtests")
    return pd.read_parquet(pq) if pq else pd.DataFrame()


# ===================================================================
# Catalyst map (Supabase integration)
# ===================================================================

def _load_catalyst_data(tickers: List[str]) -> Dict[str, List[Dict]]:
    """Pull catalyst/news data from Supabase docs_extracted if available."""
    catalysts: Dict[str, List[Dict]] = {}
    try:
        import requests as _requests
        url = os.getenv("SUPABASE_URL", "")
        key = os.getenv("SUPABASE_SERVICE_ROLE", "")
        if not url or not key:
            return catalysts
        headers = {
            "apikey": key,
            "Authorization": f"Bearer {key}",
            "Content-Type": "application/json",
        }
        resp = _requests.get(
            f"{url}/rest/v1/docs_extracted",
            params={
                "select": "ticker,headline,source,extracted_at,sentiment",
                "order": "extracted_at.desc",
                "limit": "100",
            },
            headers=headers,
            timeout=10,
        )
        if resp.status_code == 200:
            for row in resp.json():
                t = (row.get("ticker") or "").upper()
                if t in tickers:
                    catalysts.setdefault(t, []).append({
                        "headline": row.get("headline", ""),
                        "source": row.get("source", ""),
                        "date": row.get("extracted_at", ""),
                        "sentiment": row.get("sentiment", ""),
                    })
    except Exception:
        pass
    return catalysts


# ===================================================================
# Regime detection (simplified)
# ===================================================================

def _detect_regime(prices: pd.DataFrame, market: str) -> Dict[str, Any]:
    """Simple regime classification based on benchmark behavior."""
    benchmark = "SPY" if market == "US" else "STW.AX"

    if prices.empty or "ticker" not in prices.columns:
        return {"current": "Unknown", "history": []}

    bm = prices[prices["ticker"] == benchmark].sort_values("date")
    if bm.empty:
        # Fallback to cross-sectional median
        last_dates = prices.groupby("date")["px"].median().reset_index()
        bm = last_dates.sort_values("date")
    else:
        bm = bm[["date", "px"]].copy()

    if len(bm) < 50:
        return {"current": "Unknown", "history": []}

    bm = bm.tail(200).copy()
    bm["ret_20d"] = bm["px"].pct_change(20)
    bm["vol_20d"] = bm["px"].pct_change().rolling(20).std()
    bm = bm.dropna()

    if bm.empty:
        return {"current": "Unknown", "history": []}

    def _classify(ret: float, vol: float) -> str:
        if ret > 0.02 and vol < 0.02:
            return "Risk-On (Low Vol)"
        elif ret > 0.02:
            return "Risk-On (High Vol)"
        elif ret < -0.02 and vol > 0.02:
            return "Risk-Off (High Vol)"
        elif ret < -0.02:
            return "Risk-Off (Low Vol)"
        return "Transitional"

    latest = bm.iloc[-1]
    ret = float(latest["ret_20d"])
    vol = float(latest["vol_20d"])
    raw_label = _classify(ret, vol)

    icon_map = {
        "Risk-On (Low Vol)": "🟢",
        "Risk-On (High Vol)": "🟡",
        "Risk-Off (High Vol)": "🔴",
        "Risk-Off (Low Vol)": "🟠",
        "Transitional": "⚪",
    }
    current = f"{icon_map.get(raw_label, '⚪')} {raw_label}"

    # Recent history (4-week steps)
    history: List[Dict] = []
    step = 20
    for i in range(min(5, len(bm) // step)):
        idx = -(i * step + 1) if i > 0 else -1
        if abs(idx) >= len(bm):
            break
        row = bm.iloc[idx]
        r = float(row["ret_20d"])
        v = float(row["vol_20d"])
        date_val = str(row["date"])[:10] if "date" in row.index else ""
        history.append({"date": date_val, "regime": _classify(r, v)})
    history.reverse()

    return {"current": current, "history": history}


# ===================================================================
# Trade plan generation
# ===================================================================

def _compute_atr(ticker_prices: pd.DataFrame, period: int = ATR_PERIOD) -> float:
    """Compute Average True Range."""
    if ticker_prices.empty or len(ticker_prices) < period + 1:
        return 0.0
    df = ticker_prices.sort_values("date").tail(period + 1).copy()
    df["prev_close"] = df["px"].shift(1)
    high = df["high"] if "high" in df.columns else df["px"]
    low = df["low"] if "low" in df.columns else df["px"]
    df["tr"] = np.maximum(
        high - low,
        np.maximum(abs(high - df["prev_close"]), abs(low - df["prev_close"])),
    )
    atr = df["tr"].dropna().mean()
    return float(atr) if not math.isnan(atr) else 0.0


def _generate_trade_plans(
    top_preds: pd.DataFrame,
    prices: pd.DataFrame,
    portfolio: float = DEFAULT_PORTFOLIO,
    risk_pct: float = DEFAULT_RISK_PER_TRADE_PCT,
) -> List[Dict[str, Any]]:
    """Generate trade plans for top-ranked tickers."""
    plans: List[Dict[str, Any]] = []
    risk_amount = portfolio * (risk_pct / 100.0)

    for _, row in top_preds.iterrows():
        ticker = row["ticker"]
        px = float(row.get("px", 0))
        if px <= 0:
            continue

        tp = prices[prices["ticker"] == ticker].copy() if not prices.empty else pd.DataFrame()
        atr = _compute_atr(tp, ATR_PERIOD) if not tp.empty else px * 0.02

        entry = round(px, 2)
        stop_distance = max(atr * 2.0, px * 0.005) if atr > 0 else px * 0.04
        stop = round(entry - stop_distance, 2)
        shares = max(int(risk_amount / stop_distance), 1) if stop_distance > 0 else 1
        position_value = round(shares * entry, 2)
        pct_of_portfolio = round(100.0 * position_value / portfolio, 1) if portfolio > 0 else 0.0
        target = round(entry + stop_distance * 3.0, 2)
        p_ens = float(row.get("p_up_ens", 0.5))

        # Downside tail risk: 5th percentile daily return
        tail_risk = 0.0
        if not tp.empty and "px" in tp.columns and len(tp) > 20:
            rets = tp["px"].pct_change().dropna()
            if len(rets) > 20:
                tail_risk = float(rets.quantile(0.05))

        plans.append({
            "ticker": ticker,
            "entry": entry,
            "stop": stop,
            "target": target,
            "stop_distance": round(stop_distance, 2),
            "shares": shares,
            "position_value": position_value,
            "pct_of_portfolio": pct_of_portfolio,
            "risk_amount": round(shares * stop_distance, 2),
            "rr_ratio": "3:1",
            "p_up_ens": p_ens,
            "atr": round(atr, 2),
            "tail_risk_5pct": round(tail_risk * 100, 2),
        })

    return plans


# ===================================================================
# Calibration & Model Consensus
# ===================================================================

def _detect_feature_cols(df: pd.DataFrame) -> List[str]:
    """Auto-detect available feature columns from a merged dataframe."""
    # Candidate columns in priority order
    candidates = [
        "ret_1d", "ret_5d", "ret_20d", "vol_20d",
        "px_gt_sma200", "sma50_gt_sma200",
        "ma_ratio_20_50", "ma_ratio_50_200", "rel_strength_20d",
    ]
    return [c for c in candidates if c in df.columns]


def _compute_calibration_summary(
    features: pd.DataFrame,
    labels: pd.DataFrame,
    as_of: dt.date,
) -> Dict[str, Any]:
    """Compute calibration metrics using the unified model stack from foundry_models."""
    summary: Dict[str, Any] = {}

    if features.empty or labels.empty:
        return {"available": False, "reason": "no features/labels data"}

    df = features.merge(labels, on=["date", "ticker"], how="inner")
    df = df[df["date"].dt.date < as_of].copy()

    if len(df) < 100:
        return {"available": False, "reason": "insufficient data"}

    feature_cols = _FEATURE_COLS if _FEATURE_COLS is not None else _detect_feature_cols(df)
    if len(feature_cols) < 3:
        return {"available": False, "reason": f"too few feature cols ({len(feature_cols)})"}

    dates = sorted(df["date"].unique())
    eval_start = dates[-120] if len(dates) > 140 else dates[int(len(dates) * 0.7)]
    # Split into train (base), calibration, and eval
    calib_start = dates[-60] if len(dates) > 80 else dates[int(len(dates) * 0.8)]
    train_df = df[df["date"] < eval_start]
    calib_df = df[(df["date"] >= eval_start) & (df["date"] < calib_start)]
    eval_df = df[df["date"] >= calib_start]

    # Fallback: if calib_df is too small, split train into base+calib
    if len(calib_df) < 50:
        calib_start = eval_start
        eval_start = dates[int(len(dates) * 0.6)] if len(dates) > 100 else dates[int(len(dates) * 0.5)]
        train_df = df[df["date"] < eval_start]
        calib_df = df[(df["date"] >= eval_start) & (df["date"] < calib_start)]
        eval_df = df[df["date"] >= calib_start]

    from sklearn.metrics import roc_auc_score, brier_score_loss

    # Drop NaN in feature columns to avoid sklearn errors
    all_cols = [c for c in feature_cols if c in train_df.columns]
    label_cols = [c for c in ["y_up_1d", "y_up_5d", "y_up_20d"] if c in train_df.columns]
    train_df = train_df.dropna(subset=all_cols)
    calib_df = calib_df.dropna(subset=all_cols)
    eval_df = eval_df.dropna(subset=all_cols)

    if len(train_df) < 500 or len(eval_df) < 50:
        return {"available": False, "reason": "insufficient rows after NaN drop"}

    # If calibration set is too small, use part of training set
    if len(calib_df) < 50:
        n_calib = max(int(len(train_df) * 0.2), 100)
        calib_df = train_df.tail(n_calib)
        train_df = train_df.iloc[:-n_calib]

    horizons: Dict[str, Dict] = {}
    for horizon, ycol in [("1d", "y_up_1d"), ("5d", "y_up_5d"), ("20d", "y_up_20d")]:
        if ycol not in df.columns:
            continue
        try:
            X_train = train_df[feature_cols]
            y_train = train_df[ycol]
            X_calib = calib_df[feature_cols]
            y_calib = calib_df[ycol]
            X_eval = eval_df[feature_cols]
            y_eval = eval_df[ycol]

            if train_model_stack is not None:
                ens, cal, stack_diag = train_model_stack(
                    X_train, y_train, X_calib, y_calib,
                )
                raw_eval = ens.predict_proba(X_eval)
                ens_prob = cal.transform(raw_eval)
            else:
                # Fallback: basic LR if foundry_models unavailable
                logger.warning("train_model_stack unavailable, falling back to standalone LR")
                from sklearn.linear_model import LogisticRegression
                lr = LogisticRegression(max_iter=200)
                lr.fit(X_train, y_train)
                ens_prob = lr.predict_proba(X_eval)[:, 1]

            auc_val = float(roc_auc_score(y_eval, ens_prob))
            brier = float(brier_score_loss(y_eval, ens_prob))
            hit_rate = float(((ens_prob > 0.5).astype(int) == y_eval.values).mean() * 100)

            # Expected Calibration Error
            n_bins = 10
            bin_edges = np.linspace(0, 1, n_bins + 1)
            ece = 0.0
            for i in range(n_bins):
                mask = (ens_prob >= bin_edges[i]) & (ens_prob < bin_edges[i + 1])
                if mask.sum() > 0:
                    bin_acc = float(y_eval.values[mask].mean())
                    bin_conf = float(ens_prob[mask].mean())
                    ece += abs(bin_acc - bin_conf) * mask.sum() / len(y_eval)

            horizons[horizon] = {
                "auc": round(auc_val, 4),
                "brier": round(brier, 4),
                "hit_rate": round(hit_rate, 1),
                "ece": round(ece, 4),
                "eval_rows": int(len(eval_df)),
            }
        except Exception as e:
            logger.warning("Calibration summary failed for horizon %s: %s", horizon, e)
            horizons[horizon] = {"error": str(e)}

    summary["available"] = True
    summary["horizons"] = horizons
    summary["eval_window"] = f"{str(eval_start)[:10]} to {str(dates[-1])[:10]}"
    return summary


def _compute_model_consensus(
    preds: pd.DataFrame,
    features: pd.DataFrame,
    labels: pd.DataFrame,
    top_tickers: List[str],
    as_of: dt.date,
) -> List[Dict[str, Any]]:
    """Per-ticker model consensus using the unified EnsembleModel from foundry_models.

    Shows individual sub-model scores (LR, LightGBM/GBT) + calibrated ensemble.
    """
    if features.empty or labels.empty or preds.empty:
        return []

    df = features.merge(labels, on=["date", "ticker"], how="inner")
    train = df[df["date"].dt.date < as_of].copy()

    feature_cols = _FEATURE_COLS if _FEATURE_COLS is not None else _detect_feature_cols(df)
    if len(feature_cols) < 3 or len(train) < 500:
        return []

    # Drop NaN rows
    ycol = "y_up_5d"
    if ycol not in train.columns:
        return []
    train = train.dropna(subset=feature_cols + [ycol])

    last_dt = preds["date"].max()
    test = df[df["date"] == last_dt].copy()
    if test.empty:
        return []

    consensus: List[Dict[str, Any]] = []
    try:
        # Split train into base + calib for the unified model stack
        n_calib = max(int(len(train) * 0.15), 200)
        base_df = train.iloc[:-n_calib]
        calib_df = train.iloc[-n_calib:]

        X_train = base_df[feature_cols]
        y_train = base_df[ycol]
        X_calib = calib_df[feature_cols]
        y_calib = calib_df[ycol]

        if train_model_stack is not None:
            ens, cal, _ = train_model_stack(X_train, y_train, X_calib, y_calib)
        else:
            logger.warning("train_model_stack unavailable for model consensus")
            return []

        test_subset = test[test["ticker"].isin(top_tickers)].dropna(subset=feature_cols)
        if test_subset.empty:
            return []

        X_test = test_subset[feature_cols]

        # Get individual sub-model scores
        lr_probs = ens.models[0].predict_proba(X_test)  # BaselineLogistic
        tree_probs = ens.models[1].predict_proba(X_test)  # TreeModel
        raw_ens = ens.predict_proba(X_test)
        cal_ens = cal.transform(raw_ens)

        tree_name = ens.models[1].name  # "lgbm" or "gbt_sklearn"

        for i, (_, row) in enumerate(test_subset.iterrows()):
            consensus.append({
                "ticker": row["ticker"],
                "lr_score": round(float(lr_probs[i]) * 100, 1),
                "tree_score": round(float(tree_probs[i]) * 100, 1),
                "ensemble": round(float(cal_ens[i]) * 100, 1),
                "tree_name": tree_name,
            })
    except Exception as exc:
        logger.warning("Model consensus computation failed: %s", exc)

    return consensus


# ===================================================================
# Report rendering — Markdown
# ===================================================================

def _render_markdown(
    market: str,
    as_of: dt.date,
    preds: pd.DataFrame,
    prices: pd.DataFrame,
    regime: Dict[str, Any],
    catalysts: Dict[str, List[Dict]],
    trade_plans: List[Dict[str, Any]],
    calibration: Dict[str, Any],
    model_consensus: List[Dict[str, Any]],
    universe_size: int,
) -> str:
    """Render the complete Markdown report."""
    L: List[str] = []

    # --- Header ---
    L.append(f"# Signal Foundry — {market} Daily Report")
    L.append("")
    L.append(f"**Date:** {as_of.isoformat()}  ")
    L.append(f"**Market:** {market}  ")
    L.append(f"**Universe:** {universe_size} tickers  ")
    L.append(f"**Generated:** {dt.datetime.now(dt.timezone.utc).strftime('%Y-%m-%d %H:%M UTC')}  ")
    L.append("")
    L.append("---")
    L.append("")

    # --- Regime Summary ---
    L.append("## Regime Summary")
    L.append("")
    L.append(f"**Current Regime:** {regime.get('current', 'Unknown')}")
    L.append("")
    history = regime.get("history", [])
    if history:
        L.append("**Recent Regime History:**")
        L.append("")
        L.append("| Date | Regime |")
        L.append("|------|--------|")
        for h in history:
            L.append(f"| {h['date']} | {h['regime']} |")
        L.append("")
    L.append("---")
    L.append("")

    # --- Top Rankings ---
    L.append("## Top Rankings")
    L.append("")

    if preds.empty:
        L.append("*No predictions available for this date.*")
    else:
        top = preds.head(TOP_N).copy()
        L.append(f"Top {len(top)} tickers ranked by ensemble P(up).")
        L.append("")
        L.append("| # | Ticker | Price | P(up 1D) | P(up 5D) | P(up 20D) | Ensemble | Tail Risk 5% |")
        L.append("|---|--------|-------|----------|----------|-----------|----------|-------------|")

        tail_map = {tp["ticker"]: tp.get("tail_risk_5pct", 0) for tp in trade_plans}
        for rank, (_, row) in enumerate(top.iterrows(), 1):
            ticker = row["ticker"]
            px = f"${float(row.get('px', 0)):.2f}"
            p1 = f"{float(row.get('p_up_1d', 0)) * 100:.1f}%"
            p5 = f"{float(row.get('p_up_5d', 0)) * 100:.1f}%"
            p20 = f"{float(row.get('p_up_20d', 0)) * 100:.1f}%"
            ens = f"{float(row.get('p_up_ens', 0)) * 100:.1f}%"
            tail = tail_map.get(ticker, 0)
            t_str = f"{tail:.1f}%" if tail != 0 else "—"
            L.append(f"| {rank} | **{ticker}** | {px} | {p1} | {p5} | {p20} | {ens} | {t_str} |")
        L.append("")

    L.append("---")
    L.append("")

    # --- Catalyst Map ---
    L.append("## Catalyst Map")
    L.append("")
    if catalysts:
        for ticker, events in catalysts.items():
            L.append(f"### {ticker}")
            for ev in events[:3]:
                sent = ev.get("sentiment", "")
                icon = "🟢" if sent == "positive" else ("🔴" if sent == "negative" else "⚪")
                L.append(f"- {icon} **{ev.get('headline', 'N/A')}** ({ev.get('source', '')} — {ev.get('date', '')[:10]})")
            L.append("")
    else:
        L.append("*No catalyst data available.* Catalyst data will be populated from")
        L.append("`docs_extracted` in Supabase when news integration is active.")
        L.append("")

    L.append("---")
    L.append("")

    # --- Trade Plans ---
    L.append("## Trade Plans")
    L.append("")
    L.append(f"Portfolio: **${DEFAULT_PORTFOLIO:,.0f}** | Risk per trade: **{DEFAULT_RISK_PER_TRADE_PCT}%** (${DEFAULT_PORTFOLIO * DEFAULT_RISK_PER_TRADE_PCT / 100:,.0f})")
    L.append("")

    if trade_plans:
        L.append("| Ticker | Entry | Stop | Target | R:R | Shares | Position | % Port |")
        L.append("|--------|-------|------|--------|-----|--------|----------|--------|")
        for tp in trade_plans[:TOP_N]:
            L.append(
                f"| **{tp['ticker']}** "
                f"| ${tp['entry']:.2f} "
                f"| ${tp['stop']:.2f} "
                f"| ${tp['target']:.2f} "
                f"| {tp['rr_ratio']} "
                f"| {tp['shares']} "
                f"| ${tp['position_value']:,.0f} "
                f"| {tp['pct_of_portfolio']:.0f}% |"
            )
        L.append("")

        L.append("### Detailed Plans (Top 5)")
        L.append("")
        for tp in trade_plans[:5]:
            p_ens = tp.get("p_up_ens", 0.5)
            conviction = "High" if p_ens > 0.6 else ("Medium" if p_ens > 0.52 else "Low")
            L.append(f"#### {tp['ticker']}")
            L.append(f"- **Conviction:** {conviction} (P(up) = {p_ens * 100:.1f}%)")
            L.append(f"- **Entry:** ${tp['entry']:.2f} (market / limit at open)")
            L.append(f"- **Stop (Invalidation):** ${tp['stop']:.2f} (2x ATR = ${tp['stop_distance']:.2f} below entry)")
            L.append(f"- **Target:** ${tp['target']:.2f} (3:1 R:R)")
            L.append(f"- **Position:** {tp['shares']} shares = ${tp['position_value']:,.0f} ({tp['pct_of_portfolio']:.0f}% of portfolio)")
            L.append(f"- **Risk:** ${tp['risk_amount']:,.0f} ({DEFAULT_RISK_PER_TRADE_PCT}% of ${DEFAULT_PORTFOLIO:,.0f})")
            L.append(f"- **ATR({ATR_PERIOD}):** ${tp['atr']:.2f}")
            tail = tp.get("tail_risk_5pct", 0)
            if tail != 0:
                L.append(f"- **Downside Tail Risk (5th pctile):** {tail:.1f}% daily")
            L.append("")
    else:
        L.append("*No trade plans generated.*")
        L.append("")

    L.append("---")
    L.append("")

    # --- Calibration Summary ---
    L.append("## Calibration Summary")
    L.append("")
    if calibration.get("available"):
        L.append(f"Evaluation window: {calibration.get('eval_window', 'N/A')}")
        L.append("")
        L.append("| Horizon | AUC | Brier Score | Hit Rate | ECE |")
        L.append("|---------|-----|-------------|----------|-----|")
        for h in ["1d", "5d", "20d"]:
            hdata = calibration.get("horizons", {}).get(h, {})
            if "error" in hdata:
                L.append(f"| {h} | — | — | — | Error: {hdata['error'][:40]} |")
            elif hdata:
                L.append(
                    f"| {h} "
                    f"| {hdata.get('auc', '—')} "
                    f"| {hdata.get('brier', '—')} "
                    f"| {hdata.get('hit_rate', '—')}% "
                    f"| {hdata.get('ece', '—')} |"
                )
        L.append("")
        ev_rows = 0
        for h in calibration.get("horizons", {}).values():
            ev_rows = h.get("eval_rows", 0)
            break
        if ev_rows:
            L.append(f"Evaluation rows: {ev_rows:,}")
            L.append("")
    else:
        reason = calibration.get("reason", "No calibration data available")
        L.append(f"*{reason}*")
        L.append("")

    L.append("---")
    L.append("")

    # --- Model Consensus ---
    L.append("## Model Consensus (5D Horizon)")
    L.append("")
    if model_consensus:
        tree_label = model_consensus[0].get("tree_name", "LightGBM").upper()
        L.append(f"| Ticker | LogReg | {tree_label} | Ensemble (cal) |")
        L.append("|--------|--------|-------------|----------------|")
        for mc in model_consensus:
            L.append(
                f"| **{mc['ticker']}** "
                f"| {mc['lr_score']:.1f}% "
                f"| {mc.get('tree_score', mc.get('rf_score', 0)):.1f}% "
                f"| {mc['ensemble']:.1f}% |"
            )
        L.append("")
    else:
        L.append("*Model consensus data not available.*")
        L.append("")

    L.append("---")
    L.append("")
    L.append(f"*Report generated by Signal Foundry v0.1 — {market} pipeline*")
    L.append("")

    return "\n".join(L)


# ===================================================================
# Report rendering — HTML
# ===================================================================

_HTML_TEMPLATE = """<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>Signal Foundry — {{ market }} — {{ date }}</title>
<style>
  :root { --bg: #0d1117; --fg: #c9d1d9; --accent: #58a6ff; --border: #30363d; --green: #3fb950; --red: #f85149; --yellow: #d29922; }
  * { box-sizing: border-box; margin: 0; padding: 0; }
  body { font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Helvetica, Arial, sans-serif; background: var(--bg); color: var(--fg); line-height: 1.6; padding: 2rem; max-width: 1100px; margin: 0 auto; }
  h1 { color: var(--accent); border-bottom: 1px solid var(--border); padding-bottom: 0.5rem; margin-bottom: 1rem; font-size: 1.8rem; }
  h2 { color: var(--accent); margin-top: 2rem; margin-bottom: 0.5rem; font-size: 1.3rem; border-bottom: 1px solid var(--border); padding-bottom: 0.3rem; }
  h3 { color: var(--fg); margin-top: 1rem; }
  h4 { color: var(--fg); margin-top: 0.8rem; }
  p, li { margin-bottom: 0.4rem; }
  strong { color: #e6edf3; }
  hr { border: none; border-top: 1px solid var(--border); margin: 1.5rem 0; }
  table { border-collapse: collapse; width: 100%; margin: 1rem 0; font-size: 0.9rem; }
  th { background: #161b22; color: var(--accent); text-align: left; padding: 0.5rem 0.8rem; border: 1px solid var(--border); white-space: nowrap; }
  td { padding: 0.4rem 0.8rem; border: 1px solid var(--border); }
  tr:nth-child(even) { background: #161b22; }
  tr:hover { background: #1c2128; }
  code { background: #161b22; padding: 0.1rem 0.3rem; border-radius: 3px; font-size: 0.85em; }
  ul { padding-left: 1.5rem; }
  .meta { color: #8b949e; font-size: 0.9rem; margin-bottom: 1rem; }
</style>
</head>
<body>
{{ content }}
</body>
</html>"""


def _md_to_html(md_text: str, market: str, as_of: dt.date) -> str:
    """Convert markdown report to HTML using a simple parser + Jinja2 template."""
    import re

    lines = md_text.split("\n")
    html_parts: List[str] = []
    in_table = False
    in_list = False

    for line in lines:
        stripped = line.strip()

        # Horizontal rule
        if stripped == "---":
            if in_table:
                html_parts.append("</table>")
                in_table = False
            if in_list:
                html_parts.append("</ul>")
                in_list = False
            html_parts.append("<hr>")
            continue

        # Headers
        if stripped.startswith("#### "):
            if in_list:
                html_parts.append("</ul>")
                in_list = False
            html_parts.append(f"<h4>{_inline_md(stripped[5:])}</h4>")
            continue
        if stripped.startswith("### "):
            if in_list:
                html_parts.append("</ul>")
                in_list = False
            html_parts.append(f"<h3>{_inline_md(stripped[4:])}</h3>")
            continue
        if stripped.startswith("## "):
            if in_list:
                html_parts.append("</ul>")
                in_list = False
            html_parts.append(f"<h2>{_inline_md(stripped[3:])}</h2>")
            continue
        if stripped.startswith("# "):
            html_parts.append(f"<h1>{_inline_md(stripped[2:])}</h1>")
            continue

        # Table rows
        if stripped.startswith("|"):
            # Skip alignment rows
            if re.match(r"^\|[\s\-:|]+\|$", stripped):
                continue
            if not in_table:
                html_parts.append("<table>")
                in_table = True
                # Header row
                cells = [c.strip() for c in stripped.strip("|").split("|")]
                html_parts.append("<tr>" + "".join(f"<th>{_inline_md(c)}</th>" for c in cells) + "</tr>")
            else:
                cells = [c.strip() for c in stripped.strip("|").split("|")]
                html_parts.append("<tr>" + "".join(f"<td>{_inline_md(c)}</td>" for c in cells) + "</tr>")
            continue
        else:
            if in_table:
                html_parts.append("</table>")
                in_table = False

        # List items
        if stripped.startswith("- "):
            if not in_list:
                html_parts.append("<ul>")
                in_list = True
            html_parts.append(f"<li>{_inline_md(stripped[2:])}</li>")
            continue
        else:
            if in_list:
                html_parts.append("</ul>")
                in_list = False

        # Empty lines
        if not stripped:
            continue

        # Italic line
        if stripped.startswith("*") and stripped.endswith("*") and not stripped.startswith("**"):
            html_parts.append(f"<p><em>{_inline_md(stripped[1:-1])}</em></p>")
            continue

        # Normal paragraph
        html_parts.append(f"<p>{_inline_md(stripped)}</p>")

    if in_table:
        html_parts.append("</table>")
    if in_list:
        html_parts.append("</ul>")

    content = "\n".join(html_parts)

    if Template is not None:
        tpl = Template(_HTML_TEMPLATE)
        return tpl.render(market=market, date=as_of.isoformat(), content=content)
    else:
        return _HTML_TEMPLATE.replace("{{ market }}", market).replace("{{ date }}", as_of.isoformat()).replace("{{ content }}", content)


def _inline_md(text: str) -> str:
    """Convert inline markdown (bold, code, italic) to HTML."""
    import re
    # Escape HTML entities first but preserve our markdown
    text = text.replace("&", "&amp;").replace("<", "&lt;").replace(">", "&gt;")
    # Bold
    text = re.sub(r"\*\*(.+?)\*\*", r"<strong>\1</strong>", text)
    # Code
    text = re.sub(r"`(.+?)`", r"<code>\1</code>", text)
    # Italic
    text = re.sub(r"\*(.+?)\*", r"<em>\1</em>", text)
    return text


# ===================================================================
# Main entry point
# ===================================================================

def generate_report(
    market: str = "US",
    as_of_str: Optional[str] = None,
    run_id: Optional[str] = None,
    portfolio: float = DEFAULT_PORTFOLIO,
    risk_pct: float = DEFAULT_RISK_PER_TRADE_PCT,
    top_n: int = TOP_N,
) -> Tuple[str, str]:
    """Generate the daily report for a market.

    Returns (markdown_str, html_str).
    """
    as_of = dt.date.fromisoformat(as_of_str) if as_of_str else dt.date.today()

    print(f"[foundry_report] Generating {market} report for {as_of.isoformat()} ...")

    # Load data
    preds = load_predictions(market, as_of, run_id)
    prices = load_prices(market, as_of, run_id)
    features = load_features(market, as_of)
    labels = load_labels(market, as_of)
    universe = load_universe(market)

    if preds.empty:
        print(f"[foundry_report] WARNING: No predictions found for {market}")

    # Standardize column names to "close" everywhere, then alias "px" for report rendering
    if not preds.empty:
        if "px" in preds.columns and "close" not in preds.columns:
            preds = preds.rename(columns={"px": "close"})
        if "close" in preds.columns and "px" not in preds.columns:
            preds["px"] = preds["close"]
    if not prices.empty:
        if "px" in prices.columns and "close" not in prices.columns:
            prices = prices.rename(columns={"px": "close"})
        if "close" in prices.columns and "px" not in prices.columns:
            prices["px"] = prices["close"]

    # Ensure predictions sorted by ensemble
    if not preds.empty and "p_up_ens" in preds.columns:
        preds = preds.sort_values("p_up_ens", ascending=False)

    # Components
    print("[foundry_report]   regime ...")
    regime = _detect_regime(prices, market)

    print("[foundry_report]   catalysts ...")
    top_tickers = preds["ticker"].head(top_n).tolist() if not preds.empty else []
    catalysts = _load_catalyst_data(top_tickers)

    print("[foundry_report]   trade plans ...")
    trade_plans = _generate_trade_plans(preds.head(top_n), prices, portfolio, risk_pct) if not preds.empty else []

    print("[foundry_report]   calibration ...")
    calibration = _compute_calibration_summary(features, labels, as_of)

    print("[foundry_report]   model consensus ...")
    model_consensus = _compute_model_consensus(preds, features, labels, top_tickers[:10], as_of)

    # Render
    print("[foundry_report]   rendering markdown ...")
    md = _render_markdown(
        market=market,
        as_of=as_of,
        preds=preds,
        prices=prices,
        regime=regime,
        catalysts=catalysts,
        trade_plans=trade_plans,
        calibration=calibration,
        model_consensus=model_consensus,
        universe_size=len(universe),
    )

    print("[foundry_report]   rendering HTML ...")
    html_str = _md_to_html(md, market, as_of)

    # Save
    md_dir = OUTPUT / market
    md_dir.mkdir(parents=True, exist_ok=True)
    md_path = md_dir / f"{as_of.isoformat()}.md"
    html_path = md_dir / f"{as_of.isoformat()}.html"

    md_path.write_text(md, encoding="utf-8")
    html_path.write_text(html_str, encoding="utf-8")

    # Also save as latest
    (md_dir / "latest.md").write_text(md, encoding="utf-8")
    (md_dir / "latest.html").write_text(html_str, encoding="utf-8")

    print(f"[foundry_report] Saved: {md_path}")
    print(f"[foundry_report] Saved: {html_path}")

    return md, html_str


def main() -> None:
    parser = argparse.ArgumentParser(description="Signal Foundry Report Generator")
    parser.add_argument("--market", choices=["US", "ASX"], default="US")
    parser.add_argument("--date", default=None, help="YYYY-MM-DD (default: today)")
    parser.add_argument("--run-id", default=None)
    parser.add_argument("--portfolio", type=float, default=DEFAULT_PORTFOLIO)
    parser.add_argument("--risk-pct", type=float, default=DEFAULT_RISK_PER_TRADE_PCT)
    parser.add_argument("--top-n", type=int, default=TOP_N)
    args = parser.parse_args()

    md, html_str = generate_report(
        market=args.market,
        as_of_str=args.date,
        run_id=args.run_id,
        portfolio=args.portfolio,
        risk_pct=args.risk_pct,
        top_n=args.top_n,
    )

    print(f"\n[foundry_report] Done. Report length: {len(md)} chars MD, {len(html_str)} chars HTML")


if __name__ == "__main__":
    main()