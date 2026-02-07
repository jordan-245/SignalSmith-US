from __future__ import annotations

import datetime as dt
import json
import math
from dataclasses import dataclass
from pathlib import Path
from typing import Dict, List, Tuple

import numpy as np
import pandas as pd
import yfinance as yf
# yaml is optional; fall back to json-like parsing if missing.
try:
    import yaml  # type: ignore
except Exception:  # pragma: no cover
    yaml = None
from sklearn.ensemble import RandomForestClassifier
from sklearn.isotonic import IsotonicRegression
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import brier_score_loss


REPO = Path(__file__).resolve().parents[2]


def load_universe(market: str) -> List[str]:
    f = REPO / "directives" / "foundry" / ("universe_us.txt" if market == "US" else "universe_asx.txt")
    out: List[str] = []
    for line in f.read_text(encoding="utf-8").splitlines():
        s = line.strip()
        if not s or s.startswith("#"):
            continue
        out.append(s.upper())
    # de-dupe
    uniq = []
    seen = set()
    for t in out:
        if t not in seen:
            uniq.append(t)
            seen.add(t)
    return uniq


def load_quality_gates() -> dict:
    p = REPO / "directives" / "foundry" / "quality_gates.yaml"
    if not p.exists():
        return {}
    if yaml is None:
        # Minimal fallback: treat as empty gates if PyYAML isn't installed.
        return {}
    return yaml.safe_load(p.read_text(encoding="utf-8")) or {}


def _parquet_path(kind: str, market: str, sub: str) -> Path:
    return REPO / "data" / "foundry" / kind / f"market={market}" / sub


def write_prices_parquet(tickers: List[str], market: str, as_of: dt.date, years: int, run_id: str) -> pd.DataFrame:
    start = (as_of - dt.timedelta(days=int(years * 365.25 + 30))).isoformat()
    end = (as_of + dt.timedelta(days=1)).isoformat()

    # yfinance batching is best-effort; for robustness, fetch in chunks
    all_rows = []
    chunk = 50
    for i in range(0, len(tickers), chunk):
        part = tickers[i : i + chunk]
        df = yf.download(part, start=start, end=end, interval="1d", auto_adjust=False, progress=False, group_by="column")
        if df is None or df.empty:
            continue

        # Normalize: handle MultiIndex
        if isinstance(df.columns, pd.MultiIndex):
            # columns level0: Price fields
            fields = set(df.columns.get_level_values(0))
            # prefer Adj Close else Close
            px_field = "Adj Close" if "Adj Close" in fields else "Close"
            px = df[px_field]
            high = df["High"] if "High" in fields else None
            low = df["Low"] if "Low" in fields else None
            open_ = df["Open"] if "Open" in fields else None
            vol = df["Volume"] if "Volume" in fields else None

            for t in px.columns:
                s = px[t].dropna()
                if s.empty:
                    continue
                g = pd.DataFrame({
                    "date": pd.to_datetime(s.index),
                    "ticker": str(t).upper(),
                    "px": pd.to_numeric(s.values, errors="coerce"),
                })
                if high is not None and t in high.columns:
                    g["high"] = pd.to_numeric(high[t].values, errors="coerce")
                if low is not None and t in low.columns:
                    g["low"] = pd.to_numeric(low[t].values, errors="coerce")
                if open_ is not None and t in open_.columns:
                    g["open"] = pd.to_numeric(open_[t].values, errors="coerce")
                if vol is not None and t in vol.columns:
                    g["volume"] = pd.to_numeric(vol[t].values, errors="coerce")
                all_rows.append(g)
        else:
            # single ticker case
            px_field = "Adj Close" if "Adj Close" in df.columns else "Close"
            g = df.reset_index().rename(columns={"Date": "date"})
            g["ticker"] = part[0].upper() if part else "UNKNOWN"
            g["px"] = pd.to_numeric(g[px_field], errors="coerce")
            for col in ["High", "Low", "Open", "Volume"]:
                if col in g.columns:
                    g[col.lower()] = pd.to_numeric(g[col], errors="coerce")
            all_rows.append(g[["date", "ticker", "px", "high", "low", "open", "volume"]])

    if not all_rows:
        return pd.DataFrame()

    prices = pd.concat(all_rows, ignore_index=True)
    prices = prices.dropna(subset=["date", "ticker", "px"]).sort_values(["ticker", "date"])

    out_dir = _parquet_path("prices", market, f"run_id={run_id}")
    out_dir.mkdir(parents=True, exist_ok=True)
    out_path = out_dir / "part.parquet"
    prices.to_parquet(out_path, index=False)

    return prices


def build_features(prices: pd.DataFrame, market: str, feature_set: str, as_of: dt.date) -> pd.DataFrame:
    if prices.empty:
        return pd.DataFrame()

    out = []
    for t, g in prices.groupby("ticker"):
        g = g.sort_values("date")
        s = g["px"].astype(float)
        rets = s.pct_change()
        feat = pd.DataFrame({
            "date": g["date"].values,
            "ticker": t,
            "ret_1d": rets,
            "ret_5d": s / s.shift(5) - 1.0,
            "ret_20d": s / s.shift(20) - 1.0,
            "vol_20d": rets.rolling(20).std(),
            "sma50": s.rolling(50).mean(),
            "sma200": s.rolling(200).mean(),
            "px": s.values,
        })
        feat["px_gt_sma200"] = (feat["px"] > feat["sma200"]).astype(float)
        feat["sma50_gt_sma200"] = (feat["sma50"] > feat["sma200"]).astype(float)
        out.append(feat)

    feats = pd.concat(out, ignore_index=True)
    feats["date"] = pd.to_datetime(feats["date"])
    feats = feats.dropna()

    out_dir = _parquet_path("features", market, f"feature_set={feature_set}/date={as_of.isoformat()}")
    out_dir.mkdir(parents=True, exist_ok=True)
    feats.to_parquet(out_dir / "part.parquet", index=False)
    return feats


def build_labels(prices: pd.DataFrame, market: str, as_of: dt.date) -> pd.DataFrame:
    if prices.empty:
        return pd.DataFrame()

    out = []
    for t, g in prices.groupby("ticker"):
        g = g.sort_values("date")
        s = g["px"].astype(float)
        lbl = pd.DataFrame({
            "date": g["date"].values,
            "ticker": t,
            "y_up_1d": (s.shift(-1) / s - 1.0 > 0).astype(int),
            "y_up_5d": (s.shift(-5) / s - 1.0 > 0).astype(int),
            "y_up_20d": (s.shift(-20) / s - 1.0 > 0).astype(int),
            "ret_fwd_1d": (s.shift(-1) / s - 1.0),
            "ret_fwd_5d": (s.shift(-5) / s - 1.0),
            "ret_fwd_20d": (s.shift(-20) / s - 1.0),
        })
        out.append(lbl)

    labels = pd.concat(out, ignore_index=True)
    labels["date"] = pd.to_datetime(labels["date"])
    labels = labels.dropna()

    out_dir = _parquet_path("labels", market, f"date={as_of.isoformat()}")
    out_dir.mkdir(parents=True, exist_ok=True)
    labels.to_parquet(out_dir / "part.parquet", index=False)
    return labels


def _train_models(X: pd.DataFrame, y: pd.Series) -> Dict[str, object]:
    # Logistic regression baseline
    lr = LogisticRegression(max_iter=200)
    lr.fit(X, y)

    rf = RandomForestClassifier(
        n_estimators=300,
        max_depth=6,
        random_state=42,
        n_jobs=-1,
    )
    rf.fit(X, y)
    return {"lr": lr, "rf": rf}


def predict_and_calibrate(feats: pd.DataFrame, labels: pd.DataFrame, market: str, as_of: dt.date, run_id: str) -> Tuple[pd.DataFrame, Dict]:
    if feats.empty or labels.empty:
        return pd.DataFrame(), {"ok": False, "reason": "missing feats/labels"}

    df = feats.merge(labels, on=["date", "ticker"], how="inner")

    # Use a cross-sectional model trained on all tickers pooled.
    # Train on data strictly before as_of.
    train = df[df["date"].dt.date < as_of].copy()

    # If as_of isn't a trading day for many tickers, use the latest available date <= as_of.
    last_dt = df[df["date"].dt.date <= as_of]["date"].max()
    if pd.isna(last_dt):
        return pd.DataFrame(), {"ok": False, "reason": "no data on/before as_of"}
    asof_dt = pd.to_datetime(last_dt)
    test = df[df["date"] == asof_dt].copy()

    feature_cols = [
        "ret_1d",
        "ret_5d",
        "ret_20d",
        "vol_20d",
        "px_gt_sma200",
        "sma50_gt_sma200",
    ]

    # Diagnostics
    diag: Dict[str, object] = {
        "train_rows": int(len(train)),
        "test_rows": int(len(test)),
        "as_of": as_of.isoformat(),
        "asof_effective": asof_dt.date().isoformat(),
    }

    # If too little data, bail.
    if len(train) < 5000 or len(test) < 50:
        diag["ok"] = False
        diag["reason"] = "insufficient rows"
        return pd.DataFrame(), diag

    X_train = train[feature_cols]
    models = {
        "1d": _train_models(X_train, train["y_up_1d"]),
        "5d": _train_models(X_train, train["y_up_5d"]),
        "20d": _train_models(X_train, train["y_up_20d"]),
    }

    preds_out = test[["date", "ticker", "px"]].copy()

    # Calibrate: use a held-out tail window (last ~120 sessions) as calibration set.
    # Simple approach: take last 120 unique dates in train.
    dates = sorted(set(train["date"].dt.date.tolist()))
    calib_cut = dates[-120] if len(dates) > 140 else dates[int(len(dates) * 0.8)]
    calib = train[train["date"].dt.date >= calib_cut].copy()
    base_train = train[train["date"].dt.date < calib_cut].copy()

    calib_stats = {}

    for horizon, ycol in [("1d", "y_up_1d"), ("5d", "y_up_5d"), ("20d", "y_up_20d")]:
        Xb = base_train[feature_cols]
        yb = base_train[ycol]
        Xc = calib[feature_cols]
        yc = calib[ycol]
        Xt = test[feature_cols]

        # Use LR as the base prob model, then fit isotonic calibration on held-out tail.
        lr = LogisticRegression(max_iter=200)
        lr.fit(Xb, yb)

        base_prob_c = lr.predict_proba(Xc)[:, 1]
        brier = float(brier_score_loss(yc, base_prob_c))

        # Isotonic calibration maps uncalibrated probs -> calibrated probs
        iso = IsotonicRegression(out_of_bounds="clip")
        iso.fit(base_prob_c, yc)

        base_prob_t = lr.predict_proba(Xt)[:, 1]
        prob = iso.predict(base_prob_t)

        preds_out[f"p_up_{horizon}"] = prob
        calib_stats[horizon] = {"brier_uncal": brier, "calib_cut": str(calib_cut)}

    # Simple ensemble: average calibrated probs
    preds_out["p_up_ens"] = preds_out[["p_up_1d", "p_up_5d", "p_up_20d"]].mean(axis=1)

    # Rank
    preds_out = preds_out.sort_values("p_up_ens", ascending=False)

    out_dir = _parquet_path("predictions", market, f"run_id={run_id}")
    out_dir.mkdir(parents=True, exist_ok=True)
    preds_out.to_parquet(out_dir / "part.parquet", index=False)

    diag["ok"] = True
    diag["calibration"] = calib_stats

    # overall coverage
    diag["tickers_predicted"] = int(preds_out["ticker"].nunique())
    diag["asof_effective"] = asof_dt.date().isoformat()

    return preds_out, diag


def quality_gate_check(gates: dict, feats: pd.DataFrame, labels: pd.DataFrame, diagnostics: Dict) -> Dict:
    res = {"ok": True, "reasons": []}

    # Coverage gate: fraction of tickers with rows at as_of in predictions
    cov_min = float((((gates or {}).get("coverage") or {}).get("min_ok_ticker_frac") or 0.0))
    universe = load_universe("US")
    predicted = int(diagnostics.get("tickers_predicted") or 0)
    frac = (predicted / len(universe)) if universe else 0.0
    if cov_min and frac < cov_min:
        res["ok"] = False
        res["reasons"].append(f"coverage {frac:.1%} < {cov_min:.0%}")

    # Training rows
    min_rows = int((((gates or {}).get("training") or {}).get("min_rows_per_ticker") or 0))
    train_rows = int(diagnostics.get("train_rows") or 0)
    # pooled rows proxy: require overall enough
    if min_rows and train_rows < (min_rows * 200):
        res["ok"] = False
        res["reasons"].append(f"train_rows {train_rows} too low")

    # Calibration gate (use 5d brier_uncal as a rough sanity check)
    max_brier = float((((gates or {}).get("calibration") or {}).get("max_brier") or 1.0))
    try:
        b = diagnostics.get("calibration", {}).get("5d", {}).get("brier_uncal")
        if b is not None and float(b) > max_brier:
            res["ok"] = False
            res["reasons"].append(f"brier {float(b):.3f} > {max_brier:.3f}")
    except Exception:
        pass

    return res


def render_report(market: str, as_of: dt.date, run_id: str, preds: pd.DataFrame, diagnostics: Dict, gate_res: Dict) -> str:
    top = preds.head(20).copy() if preds is not None and not preds.empty else pd.DataFrame()

    lines = []
    lines.append(f"# Signal Foundry — {market} — {as_of.isoformat()}")
    lines.append("")
    lines.append(f"Run id: `{run_id}`")
    lines.append(f"Quality gates: **{'PASS' if gate_res.get('ok') else 'FAIL'}**")
    if not gate_res.get("ok"):
        lines.append("- Reasons: " + "; ".join(gate_res.get("reasons") or []))
    lines.append("")

    lines.append("## Coverage")
    lines.append(f"- Predicted tickers: {diagnostics.get('tickers_predicted')} / {len(load_universe('US'))}")
    lines.append(f"- Train rows: {diagnostics.get('train_rows')} · Test rows: {diagnostics.get('test_rows')}")
    lines.append("")

    if top.empty:
        lines.append("## Top candidates")
        lines.append("(no predictions)")
        return "\n".join(lines) + "\n"

    show = top[["ticker", "p_up_1d", "p_up_5d", "p_up_20d", "p_up_ens"]].copy()
    for c in ["p_up_1d", "p_up_5d", "p_up_20d", "p_up_ens"]:
        show[c] = (show[c].astype(float) * 100).round(1)

    lines.append("## Top candidates")
    lines.append(show.to_markdown(index=False))
    lines.append("")

    lines.append("## Calibration (uncalibrated Brier, lower is better)")
    cal = diagnostics.get("calibration") or {}
    for h in ["1d", "5d", "20d"]:
        b = cal.get(h, {}).get("brier_uncal")
        if b is not None:
            lines.append(f"- {h}: {float(b):.3f}")
    lines.append("")

    return "\n".join(lines) + "\n"
