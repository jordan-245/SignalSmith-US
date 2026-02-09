"""Signal Foundry — deterministic pipeline steps.

All heavy lifting lives here. The conductor (foundry_run.py) calls these
functions in sequence.  Each step reads inputs, writes parquet, returns
a DataFrame or diagnostics dict.

Parquet layout (PRD §10):
    data/foundry/prices/market={US|ASX}/date=YYYY-MM-DD/part.parquet
    data/foundry/features/market={US|ASX}/feature_set=v1/date=YYYY-MM-DD/part.parquet
    data/foundry/labels/market={US|ASX}/horizon={1d|5d|20d}/date=YYYY-MM-DD/part.parquet
"""

from __future__ import annotations

import datetime as dt
import functools
import logging
import time as _time
import warnings
from pathlib import Path
from typing import Dict, List, Optional, Tuple

import numpy as np
import pandas as pd
import yfinance as yf

try:
    import yaml  # type: ignore
except ImportError:
    yaml = None  # type: ignore

try:
    import exchange_calendars as ec  # type: ignore
except ImportError:
    ec = None  # type: ignore

from sklearn.metrics import brier_score_loss

# Import the canonical model stack and FEATURE_COLS from foundry_models.
# Try relative import first (when used as execution.foundry.foundry_steps),
# then bare import (when run from the foundry directory).
try:
    from execution.foundry.foundry_models import (
        FEATURE_COLS as _MODEL_FEATURE_COLS,
        train_model_stack as _train_model_stack,
    )
except ImportError:
    try:
        from foundry_models import (
            FEATURE_COLS as _MODEL_FEATURE_COLS,
            train_model_stack as _train_model_stack,
        )
    except ImportError:
        _MODEL_FEATURE_COLS = None
        _train_model_stack = None

log = logging.getLogger("foundry")

REPO = Path(__file__).resolve().parents[2]

# ── Market → exchange calendar mapping ──────────────────────────────
MARKET_CALENDAR = {
    "US": "XNYS",   # NYSE
    "ASX": "XASX",  # ASX
}

MARKET_BENCHMARK = {
    "US": "SPY",
    "ASX": "^AXJO",
}


# ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
# Helpers
# ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

def _retry(max_attempts: int = 3, base_delay: float = 2.0):
    """Decorator: retry with exponential backoff."""
    def decorator(fn):
        @functools.wraps(fn)
        def wrapper(*args, **kwargs):
            last_exc: Optional[Exception] = None
            for attempt in range(1, max_attempts + 1):
                try:
                    return fn(*args, **kwargs)
                except Exception as exc:
                    last_exc = exc
                    if attempt < max_attempts:
                        delay = base_delay * (2 ** (attempt - 1))
                        log.warning(
                            "Retry %d/%d for %s after error: %s (backoff %.1fs)",
                            attempt, max_attempts, fn.__name__, exc, delay,
                        )
                        _time.sleep(delay)
            raise last_exc  # type: ignore[misc]
        return wrapper
    return decorator


def _parquet_dir(kind: str, market: str, sub: str) -> Path:
    """Build the canonical parquet directory path."""
    return REPO / "data" / "foundry" / kind / f"market={market}" / sub


def _ensure_dir(p: Path) -> Path:
    p.mkdir(parents=True, exist_ok=True)
    return p


def get_calendar(market: str):
    """Return the exchange_calendars calendar for *market*."""
    if ec is None:
        raise RuntimeError("exchange-calendars is required")
    return ec.get_calendar(MARKET_CALENDAR[market])


def latest_session(market: str, on_or_before: dt.date) -> dt.date:
    """Return the most recent valid trading session ≤ *on_or_before*."""
    cal = get_calendar(market)
    ts = pd.Timestamp(on_or_before)
    sessions = cal.sessions[cal.sessions <= ts]
    if sessions.empty:
        raise ValueError(f"No sessions found on or before {on_or_before} for {market}")
    return sessions[-1].date()


def is_session(market: str, d: dt.date) -> bool:
    cal = get_calendar(market)
    return cal.is_session(pd.Timestamp(d))


# ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
# Universe loading
# ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

def load_universe(market: str) -> List[str]:
    """Read directives/foundry/universe_{market}.txt → de-duped ticker list."""
    fname = "universe_us.txt" if market == "US" else "universe_asx.txt"
    f = REPO / "directives" / "foundry" / fname
    if not f.exists():
        log.warning("Universe file not found: %s", f)
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


def load_quality_gates() -> dict:
    p = REPO / "directives" / "foundry" / "quality_gates.yaml"
    if not p.exists():
        return {}
    if yaml is None:
        log.warning("PyYAML not installed — quality gates will be empty")
        return {}
    return yaml.safe_load(p.read_text(encoding="utf-8")) or {}


# ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
# Step 1 — Price ingestion
# ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

def ingest_prices(
    tickers: List[str],
    market: str,
    as_of: dt.date,
    years: int = 5,
) -> pd.DataFrame:
    """Download OHLCV via yfinance and write date-partitioned parquet.

    Also fetches the market benchmark (SPY / ^AXJO) so that relative-
    strength features can be computed downstream.

    Returns a single long DataFrame with columns:
        date, ticker, open, high, low, close, volume
    """
    # Add benchmark if not already present
    bench = MARKET_BENCHMARK.get(market, "SPY")
    all_tickers = list(dict.fromkeys(tickers + [bench]))  # preserve order, de-dup

    start = (as_of - dt.timedelta(days=int(years * 365.25 + 60))).isoformat()
    end = (as_of + dt.timedelta(days=1)).isoformat()

    all_rows: List[pd.DataFrame] = []
    chunk_size = 40
    failed: List[str] = []

    @_retry(max_attempts=3, base_delay=2.0)
    def _download_chunk(tickers_chunk: List[str]) -> pd.DataFrame:
        raw = yf.download(
            tickers_chunk,
            start=start,
            end=end,
            interval="1d",
            auto_adjust=False,
            progress=False,
            group_by="column",
        )
        if raw is None or raw.empty:
            raise ValueError(f"Empty result for {tickers_chunk[:3]}...")
        return raw

    for i in range(0, len(all_tickers), chunk_size):
        chunk = all_tickers[i : i + chunk_size]
        try:
            raw = _download_chunk(chunk)
        except Exception as exc:
            log.warning("yfinance download failed for chunk %s: %s", chunk[:3], exc)
            failed.extend(chunk)
            continue

        all_rows.extend(_parse_yf_frame(raw, chunk))

    if failed:
        log.warning("Failed to fetch %d tickers: %s", len(failed), failed[:10])

    if not all_rows:
        log.error("No price data obtained at all — aborting")
        return pd.DataFrame()

    prices = pd.concat(all_rows, ignore_index=True)

    # ── Stale price detection ──
    try:
        expected_session = latest_session(market, as_of)
        stale_tickers: List[str] = []
        for t, g in prices.groupby("ticker"):
            ticker_latest = g["date"].max().date()
            if ticker_latest < expected_session:
                stale_tickers.append(str(t))
        if stale_tickers:
            log.warning(
                "Stale prices for %d/%d tickers (latest < %s): %s",
                len(stale_tickers),
                prices["ticker"].nunique(),
                expected_session,
                stale_tickers[:10],
            )
            if len(stale_tickers) == prices["ticker"].nunique():
                raise RuntimeError(
                    f"ALL {len(stale_tickers)} tickers have stale prices "
                    f"(latest < {expected_session})"
                )
    except RuntimeError:
        raise
    except Exception as exc:
        log.warning("Stale price check skipped: %s", exc)
    prices = prices.dropna(subset=["date", "ticker", "close"])
    prices = prices.sort_values(["ticker", "date"]).reset_index(drop=True)

    # ── Write date-partitioned parquet ──
    for d, grp in prices.groupby(prices["date"].dt.date):
        out_dir = _ensure_dir(_parquet_dir("prices", market, f"date={d.isoformat()}"))
        grp.to_parquet(out_dir / "part.parquet", index=False)

    log.info(
        "Prices ingested: %d tickers, %d rows, date range %s → %s",
        prices["ticker"].nunique(),
        len(prices),
        prices["date"].min().date(),
        prices["date"].max().date(),
    )
    return prices


def _parse_yf_frame(raw: pd.DataFrame, chunk: List[str]) -> List[pd.DataFrame]:
    """Normalise yfinance output (MultiIndex or flat) into per-ticker frames."""
    frames: List[pd.DataFrame] = []

    if isinstance(raw.columns, pd.MultiIndex):
        fields = set(raw.columns.get_level_values(0))
        px_field = "Adj Close" if "Adj Close" in fields else "Close"
        for t in chunk:
            try:
                s = raw[px_field][t].dropna()
            except KeyError:
                continue
            if s.empty:
                continue
            valid_idx = s.index  # dates where close is not NaN
            g = pd.DataFrame({"date": pd.to_datetime(valid_idx), "ticker": t.upper()})
            g["close"] = pd.to_numeric(s.values, errors="coerce")
            for col, src in [("high", "High"), ("low", "Low"), ("open", "Open"), ("volume", "Volume")]:
                try:
                    vals = raw[src][t].reindex(valid_idx)
                    g[col] = pd.to_numeric(vals.values, errors="coerce")
                except KeyError:
                    g[col] = np.nan
            frames.append(g)
    else:
        # Single-ticker download
        px_field = "Adj Close" if "Adj Close" in raw.columns else "Close"
        g = raw.reset_index().rename(columns={"Date": "date"})
        t = chunk[0].upper() if chunk else "UNKNOWN"
        g["ticker"] = t
        g["close"] = pd.to_numeric(g[px_field], errors="coerce")
        for col, src in [("high", "High"), ("low", "Low"), ("open", "Open"), ("volume", "Volume")]:
            if src in g.columns:
                g[col] = pd.to_numeric(g[src], errors="coerce")
            else:
                g[col] = np.nan
        frames.append(g[["date", "ticker", "open", "high", "low", "close", "volume"]])

    return frames


# ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
# Step 2 — Feature engineering
# ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

def build_features(
    prices: pd.DataFrame,
    market: str,
    feature_set: str,
    as_of: dt.date,
) -> pd.DataFrame:
    """Compute market features and write parquet.

    Features (v1):
      - ret_1d, ret_5d, ret_20d  (percentage returns)
      - vol_20d                  (20-day rolling std of daily returns)
      - ma_ratio_20_50           (SMA20 / SMA50)
      - ma_ratio_50_200          (SMA50 / SMA200)
      - px_gt_sma200             (price > SMA200, binary)
      - sma50_gt_sma200          (SMA50 > SMA200, binary)
      - rel_strength_20d         (ticker 20d return − benchmark 20d return)
    """
    if prices.empty:
        log.warning("build_features: empty prices — returning empty DataFrame")
        return pd.DataFrame()

    bench = MARKET_BENCHMARK.get(market, "SPY")
    bench_px = prices.loc[prices["ticker"] == bench, ["date", "close"]].copy()
    bench_px = bench_px.sort_values("date").rename(columns={"close": "bench_close"})
    if bench_px.empty:
        log.warning("Benchmark %s not found in price data — relative strength will be NaN", bench)

    # Pre-compute benchmark 20d return for merge
    bench_px["bench_ret_20d"] = bench_px["bench_close"].pct_change(20)

    frames: List[pd.DataFrame] = []
    missing_tickers: List[str] = []

    def _compute_rsi(series: pd.Series, window: int = 14) -> pd.Series:
        """Compute RSI (Relative Strength Index) for a price series."""
        delta = series.diff()
        gain = (delta.where(delta > 0, 0)).rolling(window).mean()
        loss = (-delta.where(delta < 0, 0)).rolling(window).mean()
        rs = gain / (loss + 1e-10)
        return 100 - (100 / (1 + rs))

    for t, g in prices.groupby("ticker"):
        if t == bench:
            continue  # skip benchmark from features output (it's only for RS)
        g = g.sort_values("date").copy()
        s = g["close"].astype(float)
        v = g["volume"].astype(float)
        if len(s) < 30:
            missing_tickers.append(str(t))
            continue

        rets = s.pct_change()
        sma20 = s.rolling(20).mean()
        vol_20d = rets.rolling(20).std()

        feat = pd.DataFrame({
            "date": g["date"].values,
            "ticker": str(t),
            "close": s.values,
            "ret_1d": rets.values,
            "ret_5d": (s / s.shift(5) - 1.0).values,
            "ret_20d": (s / s.shift(20) - 1.0).values,
            "vol_20d": vol_20d.values,
            "sma20": sma20.values,
            "sma50": s.rolling(50).mean().values,
            "sma200": s.rolling(200).mean().values,
        })
        eps = 1e-10
        feat["ma_ratio_20_50"] = feat["sma20"] / (feat["sma50"] + eps)
        feat["ma_ratio_50_200"] = feat["sma50"] / (feat["sma200"] + eps)
        feat["px_gt_sma200"] = (feat["close"] > feat["sma200"]).astype(float)
        feat["sma50_gt_sma200"] = (feat["sma50"] > feat["sma200"]).astype(float)

        # ── Volume features (v2) ──
        vol_ma_20 = v.rolling(20).mean()
        feat["vol_ratio_20d"] = (v / (vol_ma_20 + 1e-10)).values
        feat["dollar_volume_20d"] = np.log1p((s * v).rolling(20).mean()).values
        feat["volume_trend_5d"] = (v.rolling(5).mean() / (vol_ma_20 + 1e-10)).values

        # ── Volatility-adjusted returns (Sharpe-like, v2) ──
        feat["sharpe_5d"] = feat["ret_5d"] / (feat["vol_20d"] + 1e-8)
        feat["sharpe_20d"] = feat["ret_20d"] / (feat["vol_20d"] + 1e-8)

        # ── Mean reversion features (v2) ──
        feat["rsi_14"] = _compute_rsi(s, 14).values
        feat["z_score_20d"] = ((s.values - sma20.values)
                               / (sma20.values * vol_20d.values * np.sqrt(20) + 1e-8))

        # ── Mean reversion explicit signals (v3) ──
        # RSI oversold indicator: 1.0 when RSI < 30, 0.0 when RSI > 70, linear between
        rsi_vals = feat["rsi_14"].values
        feat["rsi_14_oversold"] = np.clip((70.0 - rsi_vals) / 40.0, 0.0, 1.0)
        # Mean-reversion signal: negative past returns → positive signal (inverted)
        feat["mean_revert_5d"] = -feat["ret_5d"].values
        feat["mean_revert_20d"] = -feat["ret_20d"].values

        frames.append(feat)

    if missing_tickers:
        log.warning(
            "build_features: %d tickers skipped (too few rows): %s",
            len(missing_tickers),
            missing_tickers[:10],
        )

    if not frames:
        log.warning("build_features: no features produced")
        return pd.DataFrame()

    feats = pd.concat(frames, ignore_index=True)
    feats["date"] = pd.to_datetime(feats["date"])

    # Merge benchmark relative strength
    if not bench_px.empty:
        feats = feats.merge(bench_px[["date", "bench_ret_20d"]], on="date", how="left")
        feats["rel_strength_20d"] = feats["ret_20d"] - feats["bench_ret_20d"]
    else:
        feats["bench_ret_20d"] = np.nan
        feats["rel_strength_20d"] = np.nan

    # ── Cross-sectional rank features (v2) ──
    # Within each date, rank tickers by momentum / vol / relative strength
    feats["rank_ret_20d"] = feats.groupby("date")["ret_20d"].rank(pct=True)
    feats["rank_vol_20d"] = feats.groupby("date")["vol_20d"].rank(pct=True)
    # NOTE: rank_rel_strength removed — perfectly correlated (r=1.0) with rank_ret_20d

    # Drop helper columns not needed as features, keep sma20/50/200 for debugging
    # but only expose the final feature columns for modeling
    # Note: we keep NaN rows — only drop rows where ALL feature cols are NaN
    core_cols = [
        "date", "ticker", "close",
        # Original features
        "ret_1d", "ret_5d", "ret_20d", "vol_20d",
        "ma_ratio_20_50", "ma_ratio_50_200",
        "px_gt_sma200", "sma50_gt_sma200",
        "rel_strength_20d",
        # Volume features (v2)
        "vol_ratio_20d", "dollar_volume_20d", "volume_trend_5d",
        # Volatility-adjusted returns (v2)
        "sharpe_5d", "sharpe_20d",
        # Mean reversion features (v2)
        "rsi_14", "z_score_20d",
        # Cross-sectional rank features (v2)
        "rank_ret_20d", "rank_vol_20d",
        # Mean-reversion explicit signals (v3)
        "rsi_14_oversold", "mean_revert_5d", "mean_revert_20d",
    ]
    feats = feats[core_cols].copy()

    # Drop rows with ANY missing feature — partial NaN rows must not pass to models
    feature_cols = FEATURE_COLS  # defined below
    feats = feats.dropna(subset=feature_cols, how="any")

    # Write parquet
    out_dir = _ensure_dir(_parquet_dir("features", market, f"feature_set={feature_set}/date={as_of.isoformat()}"))
    feats.to_parquet(out_dir / "part.parquet", index=False)

    log.info(
        "Features built: %d tickers, %d rows, %d with all features present",
        feats["ticker"].nunique(),
        len(feats),
        feats[feature_cols].dropna().shape[0],
    )
    return feats


# The set of numeric features used by models — single source of truth
# is foundry_models.FEATURE_COLS.  Fallback defined here only if import failed.
if _MODEL_FEATURE_COLS is not None:
    FEATURE_COLS = _MODEL_FEATURE_COLS
else:
    FEATURE_COLS = [
        "ret_1d",
        "ret_5d",
        "ret_20d",
        "vol_20d",
        "ma_ratio_20_50",
        "ma_ratio_50_200",
        "px_gt_sma200",
        "sma50_gt_sma200",
        "rel_strength_20d",
        "vol_ratio_20d",
        "dollar_volume_20d",
        "volume_trend_5d",
        "sharpe_5d",
        "sharpe_20d",
        "rsi_14",
        "z_score_20d",
        "rank_ret_20d",
        "rank_vol_20d",
        "rsi_14_oversold",
        "mean_revert_5d",
        "mean_revert_20d",
    ]
    log.warning("Could not import FEATURE_COLS from foundry_models; using local fallback")


# ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
# Step 3 — Label generation
# ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

def build_labels(
    prices: pd.DataFrame,
    market: str,
    as_of: dt.date,
) -> pd.DataFrame:
    """Compute forward-return labels and write parquet per horizon.

    Layout:
        data/foundry/labels/market=US/horizon=1d/date=YYYY-MM-DD/part.parquet
        data/foundry/labels/market=US/horizon=5d/date=YYYY-MM-DD/part.parquet
        data/foundry/labels/market=US/horizon=20d/date=YYYY-MM-DD/part.parquet
    """
    if prices.empty:
        log.warning("build_labels: empty prices — returning empty DataFrame")
        return pd.DataFrame()

    bench = MARKET_BENCHMARK.get(market, "SPY")
    frames: List[pd.DataFrame] = []

    for t, g in prices.groupby("ticker"):
        if t == bench:
            continue
        g = g.sort_values("date").copy()
        s = g["close"].astype(float)
        if len(s) < 5:
            continue
        lbl = pd.DataFrame({
            "date": g["date"].values,
            "ticker": str(t),
            "ret_fwd_1d": (s.shift(-1) / s - 1.0).values,
            "ret_fwd_5d": (s.shift(-5) / s - 1.0).values,
            "ret_fwd_20d": (s.shift(-20) / s - 1.0).values,
        })
        lbl["y_up_1d"] = (lbl["ret_fwd_1d"] > 0).astype(int)
        lbl["y_up_5d"] = (lbl["ret_fwd_5d"] > 0).astype(int)
        lbl["y_up_20d"] = (lbl["ret_fwd_20d"] > 0).astype(int)
        frames.append(lbl)

    if not frames:
        log.warning("build_labels: no labels produced")
        return pd.DataFrame()

    labels = pd.concat(frames, ignore_index=True)
    labels["date"] = pd.to_datetime(labels["date"])

    # Write per-horizon parquet as per PRD layout
    for horizon in ["1d", "5d", "20d"]:
        col_ret = f"ret_fwd_{horizon}"
        col_y = f"y_up_{horizon}"
        hor_df = labels[["date", "ticker", col_ret, col_y]].dropna(subset=[col_ret])
        out_dir = _ensure_dir(_parquet_dir("labels", market, f"horizon={horizon}/date={as_of.isoformat()}"))
        hor_df.to_parquet(out_dir / "part.parquet", index=False)

    # Also return the wide DataFrame (all horizons) for downstream use
    log.info("Labels built: %d tickers, %d rows", labels["ticker"].nunique(), len(labels))
    return labels


# ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
# Step 4 — Predict & Calibrate
# ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

def predict_and_calibrate(
    feats: pd.DataFrame,
    labels: pd.DataFrame,
    market: str,
    as_of: dt.date,
    run_id: str,
) -> Tuple[pd.DataFrame, Dict]:
    """Train ensemble (LR + LightGBM), calibrate, predict on as_of cross-section.

    Uses ``train_model_stack()`` from ``foundry_models`` for each horizon to
    get the full ensemble + calibrator.

    Returns (predictions_df, diagnostics_dict).
    diagnostics includes ``val_auc`` and ``calibration_error`` keys for
    ``check_quality_gates_extended()``.
    """
    if _train_model_stack is None:
        return pd.DataFrame(), {"ok": False, "reason": "foundry_models not importable"}

    if feats.empty or labels.empty:
        return pd.DataFrame(), {"ok": False, "reason": "missing feats/labels"}

    # Merge on date + ticker
    df = feats.merge(labels, on=["date", "ticker"], how="inner")
    df = df.dropna(subset=FEATURE_COLS)  # need all features for modelling

    # Train on data strictly before as_of
    train = df[df["date"].dt.date < as_of].copy()

    # Identify the latest date ≤ as_of for the test cross-section
    candidates = df[df["date"].dt.date <= as_of]["date"]
    if candidates.empty:
        return pd.DataFrame(), {"ok": False, "reason": "no data on/before as_of"}
    last_dt = candidates.max()
    test = df[df["date"] == last_dt].copy()

    diag: Dict = {
        "train_rows": int(len(train)),
        "test_rows": int(len(test)),
        "as_of": as_of.isoformat(),
        "asof_effective": last_dt.date().isoformat() if not pd.isna(last_dt) else None,
    }

    if len(train) < 2000 or len(test) < 10:
        diag["ok"] = False
        diag["reason"] = f"insufficient rows (train={len(train)}, test={len(test)})"
        return pd.DataFrame(), diag

    # ── Split train into base (for model) + calib (for calibration) ──
    dates = sorted(train["date"].dt.date.unique())
    calib_start = dates[-126] if len(dates) > 146 else dates[int(len(dates) * 0.8)]
    base = train[train["date"].dt.date < calib_start]
    calib = train[train["date"].dt.date >= calib_start]

    if len(base) < 1000 or len(calib) < 500:
        diag["ok"] = False
        diag["reason"] = "insufficient base/calib split"
        return pd.DataFrame(), diag

    preds_out = test[["date", "ticker", "close"]].copy()
    calib_stats: Dict = {}
    # Aggregate val_auc and calibration_error across horizons (use 5d as primary)
    auc_by_hz: Dict = {}
    ece_by_hz: Dict = {}

    for horizon, ycol in [("1d", "y_up_1d"), ("5d", "y_up_5d"), ("20d", "y_up_20d")]:
        X_base = base[FEATURE_COLS]
        y_base = base[ycol]
        X_calib = calib[FEATURE_COLS]
        y_calib = calib[ycol]
        X_test = test[FEATURE_COLS]

        try:
            ens, cal, stack_diag = _train_model_stack(
                X_base, y_base, X_calib, y_calib,
            )
        except Exception as exc:
            log.warning("Model stack training failed for %s: %s", horizon, exc)
            preds_out[f"p_up_{horizon}"] = np.nan
            continue

        # Predict on test set: raw ensemble → calibrated
        raw_test = ens.predict_proba(X_test)
        preds_out[f"p_up_{horizon}"] = cal.transform(raw_test)

        calib_stats[horizon] = {
            "brier_uncal": round(stack_diag["brier_uncal"], 4),
            "brier_cal": round(stack_diag["brier_cal"], 4),
            "val_auc": stack_diag.get("val_auc"),
            "calibration_error": stack_diag.get("calibration_error"),
            "calib_cut": str(calib_start),
            "tree_backend": stack_diag.get("tree_backend"),
        }
        if stack_diag.get("val_auc") is not None:
            auc_by_hz[horizon] = stack_diag["val_auc"]
        if stack_diag.get("calibration_error") is not None:
            ece_by_hz[horizon] = stack_diag["calibration_error"]

    # Ensemble: mean of calibrated probabilities across horizons
    prob_cols = [c for c in preds_out.columns if c.startswith("p_up_")]
    preds_out["p_up_ens"] = preds_out[prob_cols].mean(axis=1)
    preds_out = preds_out.sort_values("p_up_ens", ascending=False)

    # Write parquet
    out_dir = _ensure_dir(_parquet_dir("predictions", market, f"run_id={run_id}"))
    preds_out.to_parquet(out_dir / "part.parquet", index=False)

    diag["ok"] = True
    diag["calibration"] = calib_stats
    diag["tickers_predicted"] = int(preds_out["ticker"].nunique())
    # Use 5d horizon as primary for quality gate metrics, fallback to any available
    diag["val_auc"] = auc_by_hz.get("5d", auc_by_hz.get("20d", auc_by_hz.get("1d")))
    diag["calibration_error"] = ece_by_hz.get("5d", ece_by_hz.get("20d", ece_by_hz.get("1d")))

    log.info("Predictions: %d tickers, ensemble range [%.2f, %.2f]",
             diag["tickers_predicted"],
             preds_out["p_up_ens"].min(),
             preds_out["p_up_ens"].max())
    return preds_out, diag


# ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
# Step 5 — Quality gates
# ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

def quality_gate_check(
    gates: dict,
    market: str,
    diagnostics: Dict,
) -> Dict:
    """Evaluate quality gates from YAML config against diagnostics."""
    res: Dict = {"ok": True, "reasons": []}

    if not diagnostics.get("ok"):
        res["ok"] = False
        res["reasons"].append(diagnostics.get("reason", "upstream failure"))
        return res

    universe = load_universe(market)
    predicted = int(diagnostics.get("tickers_predicted", 0))
    total = len(universe)

    # Coverage gate
    cov_min = float(((gates.get("coverage") or {}).get("min_ok_ticker_frac") or 0.0))
    frac = (predicted / total) if total else 0.0
    if cov_min and frac < cov_min:
        res["ok"] = False
        res["reasons"].append(f"coverage {frac:.1%} < {cov_min:.0%}")

    # Training rows gate (total pooled)
    min_train = int(((gates.get("training") or {}).get("min_training_rows") or 0))
    train_rows = int(diagnostics.get("train_rows", 0))
    if min_train and train_rows < min_train:
        res["ok"] = False
        res["reasons"].append(f"train_rows {train_rows} < min {min_train}")

    # Minimum tickers gate
    min_tickers = int(((gates.get("coverage") or {}).get("min_tickers") or 0))
    if min_tickers and predicted < min_tickers:
        res["ok"] = False
        res["reasons"].append(f"predicted {predicted} < min_tickers {min_tickers}")

    # Calibration gate
    max_brier = float(((gates.get("calibration") or {}).get("max_brier") or 1.0))
    try:
        b = diagnostics.get("calibration", {}).get("5d", {}).get("brier_uncal")
        if b is not None and float(b) > max_brier:
            res["ok"] = False
            res["reasons"].append(f"brier_5d {float(b):.3f} > {max_brier:.3f}")
    except Exception:
        pass

    return res


# ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
# Backward-compatible aliases
# ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

def write_prices_parquet(
    tickers: List[str],
    market: str,
    as_of: dt.date,
    years: int = 5,
    run_id: str = "",
) -> pd.DataFrame:
    """Backward-compatible wrapper for ingest_prices().

    The old interface accepted a run_id parameter but the new
    ingest_prices() writes date-partitioned parquet instead.
    """
    return ingest_prices(tickers, market=market, as_of=as_of, years=years)
