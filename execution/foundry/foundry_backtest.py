"""Signal Foundry — Walk-Forward Backtesting

Implements:
  - walk_forward_backtest(): train-on-trailing-window, score-next-period, roll forward
  - compute_metrics(): AUC, precision-recall, calibration, hit-rate vs baseline
  - quality_gate_check_backtest(): enforce thresholds from quality_gates.yaml
  - No lookahead: strict date-based train/test splits

All results saved as parquet under data/foundry/backtests/.
"""

from __future__ import annotations

import datetime as dt
import logging
from pathlib import Path
from typing import Any, Dict, List, Optional, Tuple

import numpy as np
import pandas as pd

try:
    import yaml
except ImportError:
    yaml = None

from sklearn.metrics import (
    auc,
    brier_score_loss,
    precision_recall_curve,
    roc_auc_score,
)

# Try package-qualified imports first, then bare imports (for direct execution).
try:
    from execution.foundry.foundry_models import (
        FEATURE_COLS,
        BaselineLogistic,
        CalibrationWrapper,
        EnsembleModel,
        RegimeClassifier,
        TreeModel,
        train_model_stack,
    )
except ImportError:
    from foundry_models import (
        FEATURE_COLS,
        BaselineLogistic,
        CalibrationWrapper,
        EnsembleModel,
        RegimeClassifier,
        TreeModel,
        train_model_stack,
    )

# Import load_quality_gates from foundry_steps (single source of truth)
try:
    from execution.foundry.foundry_steps import load_quality_gates as _load_quality_gates_steps
except ImportError:
    try:
        from foundry_steps import load_quality_gates as _load_quality_gates_steps
    except ImportError:
        _load_quality_gates_steps = None

logger = logging.getLogger("foundry.backtest")

REPO = Path(__file__).resolve().parents[2]


# ────────────────────────────────────────────────────────────────────
# Walk-Forward Backtesting
# ────────────────────────────────────────────────────────────────────
def walk_forward_backtest(
    df: pd.DataFrame,
    horizon: str = "5d",
    train_window_days: int = 756,       # ~3 years
    calib_window_days: int = 126,       # ~6 months
    step_days: int = 21,                # roll forward 1 month
    min_train_rows: int = 500,
    feature_cols: Optional[List[str]] = None,
    lr_weight: float = 0.4,
    tree_weight: float = 0.6,
    calib_method: str = "isotonic",
) -> pd.DataFrame:
    """Walk-forward backtest over the merged features+labels dataframe.

    Parameters
    ----------
    df : DataFrame
        Must contain columns: date, ticker, all feature_cols, y_up_{horizon}.
    horizon : str
        Label horizon suffix, e.g. "1d", "5d", "20d".
    train_window_days : int
        Number of calendar days for the training window.
    calib_window_days : int
        Calendar days reserved at the end of training window for calibration.
    step_days : int
        Calendar days to roll forward each iteration.
    min_train_rows : int
        Minimum training rows required (skip fold otherwise).
    feature_cols : list
        Feature columns to use.
    lr_weight, tree_weight : float
        Ensemble weights.
    calib_method : str
        "isotonic" or "platt".

    Returns
    -------
    DataFrame with columns: date, ticker, y_true, p_raw, p_cal, fold
    """
    feature_cols = feature_cols or FEATURE_COLS
    ycol = f"y_up_{horizon}"

    if ycol not in df.columns:
        raise ValueError(f"Label column {ycol} not found in DataFrame")

    # Ensure date is datetime
    df = df.copy()
    df["date"] = pd.to_datetime(df["date"])

    # Get sorted unique dates
    all_dates = sorted(df["date"].dt.date.unique())
    if len(all_dates) < 100:
        logger.warning("Very few dates (%d) for walk-forward", len(all_dates))

    # Determine test date boundaries
    # Start testing after we have enough history for training + calibration
    min_history_days = train_window_days + calib_window_days
    first_possible_test = all_dates[0] + dt.timedelta(days=min_history_days)

    # Build test periods
    results_list = []
    fold = 0

    test_start = first_possible_test
    last_date = all_dates[-1]

    while test_start <= last_date:
        test_end = test_start + dt.timedelta(days=step_days)

        # Strict temporal splits (NO LOOKAHEAD)
        # Train: [test_start - train_window - calib_window, test_start - calib_window)
        # Calib: [test_start - calib_window, test_start)
        # Test:  [test_start, test_end)
        train_end_date = test_start
        calib_start_date = test_start - dt.timedelta(days=calib_window_days)
        train_start_date = calib_start_date - dt.timedelta(days=train_window_days)

        train_mask = (df["date"].dt.date >= train_start_date) & (df["date"].dt.date < calib_start_date)
        calib_mask = (df["date"].dt.date >= calib_start_date) & (df["date"].dt.date < train_end_date)
        test_mask = (df["date"].dt.date >= test_start) & (df["date"].dt.date < test_end)

        train_df = df.loc[train_mask].dropna(subset=feature_cols + [ycol])
        calib_df = df.loc[calib_mask].dropna(subset=feature_cols + [ycol])
        test_df = df.loc[test_mask].dropna(subset=feature_cols + [ycol])

        # Skip if insufficient data
        if len(train_df) < min_train_rows:
            logger.debug(
                "Fold %d: skip — only %d train rows (need %d)",
                fold, len(train_df), min_train_rows,
            )
            test_start = test_start + dt.timedelta(days=step_days)
            fold += 1
            continue

        if len(calib_df) < 50:
            logger.debug("Fold %d: skip — only %d calib rows", fold, len(calib_df))
            test_start = test_start + dt.timedelta(days=step_days)
            fold += 1
            continue

        if len(test_df) == 0:
            test_start = test_start + dt.timedelta(days=step_days)
            fold += 1
            continue

        X_train = train_df[feature_cols]
        y_train = train_df[ycol]
        X_calib = calib_df[feature_cols]
        y_calib = calib_df[ycol]
        X_test = test_df[feature_cols]
        y_test = test_df[ycol]

        try:
            ens, cal, _ = train_model_stack(
                X_train, y_train,
                X_calib, y_calib,
                lr_weight=lr_weight,
                tree_weight=tree_weight,
                calib_method=calib_method,
            )

            p_raw = ens.predict_proba(X_test)
            p_cal = cal.transform(p_raw)
        except Exception as exc:
            logger.warning("Fold %d: model failure — %s", fold, exc)
            test_start = test_start + dt.timedelta(days=step_days)
            fold += 1
            continue

        fold_result = pd.DataFrame({
            "date": test_df["date"].values,
            "ticker": test_df["ticker"].values,
            "y_true": y_test.values,
            "p_raw": p_raw,
            "p_cal": p_cal,
            "fold": fold,
        })
        results_list.append(fold_result)

        test_start = test_start + dt.timedelta(days=step_days)
        fold += 1

    if not results_list:
        logger.warning("Walk-forward produced zero folds")
        return pd.DataFrame(columns=["date", "ticker", "y_true", "p_raw", "p_cal", "fold"])

    results = pd.concat(results_list, ignore_index=True)
    logger.info(
        "Walk-forward complete: %d folds, %d rows, dates %s → %s",
        results["fold"].nunique(),
        len(results),
        results["date"].min().date(),
        results["date"].max().date(),
    )
    return results


# ────────────────────────────────────────────────────────────────────
# Metrics Computation
# ────────────────────────────────────────────────────────────────────
def compute_metrics(results: pd.DataFrame) -> Dict[str, Any]:
    """Compute aggregate backtest metrics from walk-forward results.

    Returns dict with: auc_roc, auc_pr, brier_raw, brier_cal, hit_rate,
    baseline_rate, hit_rate_lift, calibration_slope, calibration_intercept, n_rows, n_folds.
    """
    if results.empty:
        return {"ok": False, "reason": "no results"}

    y = results["y_true"].values.astype(float)
    p_raw = results["p_raw"].values.astype(float)
    p_cal = results["p_cal"].values.astype(float)

    metrics: Dict[str, Any] = {"ok": True, "n_rows": len(results), "n_folds": int(results["fold"].nunique())}

    # Baseline rate (fraction of positives)
    baseline_rate = float(y.mean())
    metrics["baseline_rate"] = baseline_rate

    # AUC-ROC
    try:
        metrics["auc_roc"] = float(roc_auc_score(y, p_cal))
    except ValueError:
        metrics["auc_roc"] = None

    # Precision-Recall AUC
    try:
        prec, rec, _ = precision_recall_curve(y, p_cal)
        metrics["auc_pr"] = float(auc(rec, prec))
    except (ValueError, IndexError):
        metrics["auc_pr"] = None

    # Brier scores
    metrics["brier_raw"] = float(brier_score_loss(y, p_raw))
    metrics["brier_cal"] = float(brier_score_loss(y, p_cal))

    # Hit rate: predict up if p_cal > 0.5, compare to y_true
    pred_up = (p_cal > 0.5).astype(float)
    metrics["hit_rate"] = float((pred_up == y).mean())
    metrics["hit_rate_lift"] = metrics["hit_rate"] - max(baseline_rate, 1.0 - baseline_rate)

    # Calibration: bin predictions and compare to actual rate
    try:
        cal_stats = _calibration_curve_stats(y, p_cal, n_bins=10)
        metrics["calibration_slope"] = cal_stats["slope"]
        metrics["calibration_intercept"] = cal_stats["intercept"]
        metrics["calibration_bins"] = cal_stats["bins"]
    except Exception:
        metrics["calibration_slope"] = None
        metrics["calibration_intercept"] = None

    return metrics


def _calibration_curve_stats(y_true: np.ndarray, y_prob: np.ndarray, n_bins: int = 10) -> Dict:
    """Compute calibration curve and fit a linear regression to get slope/intercept."""
    from sklearn.calibration import calibration_curve as _cc

    fraction_of_positives, mean_predicted_value = _cc(y_true, y_prob, n_bins=n_bins, strategy="uniform")

    # Fit slope and intercept: actual = slope * predicted + intercept
    # Perfect calibration: slope=1, intercept=0
    if len(fraction_of_positives) >= 2:
        coeffs = np.polyfit(mean_predicted_value, fraction_of_positives, 1)
        slope, intercept = float(coeffs[0]), float(coeffs[1])
    else:
        slope, intercept = 1.0, 0.0

    bins = [
        {"predicted": float(p), "actual": float(a)}
        for p, a in zip(mean_predicted_value, fraction_of_positives)
    ]

    return {"slope": slope, "intercept": intercept, "bins": bins}


def compute_per_regime_metrics(results: pd.DataFrame, regimes: pd.Series) -> Dict[str, Dict]:
    """Compute metrics split by volatility regime."""
    results = results.copy()
    results["regime"] = regimes.values if len(regimes) == len(results) else "unknown"

    per_regime = {}
    for regime, grp in results.groupby("regime"):
        if len(grp) < 20:
            per_regime[str(regime)] = {"ok": False, "reason": "insufficient rows", "n_rows": len(grp)}
            continue
        per_regime[str(regime)] = compute_metrics(grp)

    return per_regime


# ────────────────────────────────────────────────────────────────────
# Quality Gate Check (Backtest-specific)
# ────────────────────────────────────────────────────────────────────
def load_quality_gates() -> Dict:
    """Load quality gates from YAML config.

    Delegates to foundry_steps.load_quality_gates() when available.
    """
    if _load_quality_gates_steps is not None:
        return _load_quality_gates_steps()
    # Fallback if foundry_steps import failed
    p = REPO / "directives" / "foundry" / "quality_gates.yaml"
    if not p.exists():
        return {}
    if yaml is None:
        return {}
    return yaml.safe_load(p.read_text(encoding="utf-8")) or {}


def quality_gate_check_backtest(metrics: Dict, gates: Optional[Dict] = None) -> Dict:
    """Validate backtest metrics against quality gates.

    Returns dict with 'ok' (bool) and 'reasons' (list of failures).
    """
    if gates is None:
        gates = load_quality_gates()

    result = {"ok": True, "reasons": [], "metrics_summary": {}}

    if not metrics.get("ok", False):
        result["ok"] = False
        result["reasons"].append(f"metrics computation failed: {metrics.get('reason', 'unknown')}")
        return result

    # 1. Minimum training rows (total across all folds)
    min_rows = int((gates.get("training") or {}).get("min_rows_per_ticker", 350))
    # We check total rows as a proxy
    if metrics.get("n_rows", 0) < min_rows:
        result["ok"] = False
        result["reasons"].append(
            f"backtest rows ({metrics['n_rows']}) < minimum ({min_rows})"
        )

    # 2. AUC must exceed baseline (0.5) + margin
    auc_val = metrics.get("auc_roc")
    min_auc = float((gates.get("model") or {}).get("min_auc", 0.52))
    if auc_val is not None and auc_val < min_auc:
        result["ok"] = False
        result["reasons"].append(f"AUC {auc_val:.4f} < minimum {min_auc:.4f}")

    # 3. Calibration: slope within [0.7, 1.3] per FOUNDRY_PLAN
    cal_slope = metrics.get("calibration_slope")
    if cal_slope is not None:
        if cal_slope < 0.7 or cal_slope > 1.3:
            result["ok"] = False
            result["reasons"].append(
                f"calibration slope {cal_slope:.3f} outside [0.7, 1.3]"
            )

    # 4. Brier score (calibrated) under threshold
    max_brier = float((gates.get("calibration") or {}).get("max_brier", 0.30))
    brier_cal = metrics.get("brier_cal")
    if brier_cal is not None and brier_cal > max_brier:
        result["ok"] = False
        result["reasons"].append(f"Brier (cal) {brier_cal:.4f} > max {max_brier:.4f}")

    # 5. Hit rate lift: should be positive (better than naive baseline)
    hit_lift = metrics.get("hit_rate_lift")
    if hit_lift is not None and hit_lift < -0.02:
        result["ok"] = False
        result["reasons"].append(f"hit rate lift {hit_lift:.4f} is negative")

    # Summary
    result["metrics_summary"] = {
        "auc_roc": metrics.get("auc_roc"),
        "brier_cal": metrics.get("brier_cal"),
        "hit_rate": metrics.get("hit_rate"),
        "hit_rate_lift": metrics.get("hit_rate_lift"),
        "calibration_slope": metrics.get("calibration_slope"),
        "n_folds": metrics.get("n_folds"),
        "n_rows": metrics.get("n_rows"),
    }

    return result


# ────────────────────────────────────────────────────────────────────
# No-Lookahead Validation
# ────────────────────────────────────────────────────────────────────
def validate_no_lookahead(df: pd.DataFrame, horizon: str = "5d") -> Dict:
    """Verify that walk-forward folds have no temporal overlap (no lookahead).

    For each fold, the max date of any prior fold's test set must be strictly
    less than the min date of the current fold's test set.

    Returns {"ok": bool, "issues": list} with actual validation.
    """
    issues: List[str] = []

    if "fold" not in df.columns or df.empty:
        return {"ok": True, "issues": []}

    df = df.copy()
    df["date"] = pd.to_datetime(df["date"])

    # Build per-fold date ranges
    fold_ids = sorted(df["fold"].unique())
    fold_ranges: Dict[int, Tuple[pd.Timestamp, pd.Timestamp]] = {}
    for fid in fold_ids:
        grp = df[df["fold"] == fid]
        fold_ranges[fid] = (grp["date"].min(), grp["date"].max())

    # Check sequential ordering: max(prior fold) < min(current fold)
    for i in range(1, len(fold_ids)):
        curr_id = fold_ids[i]
        curr_min = fold_ranges[curr_id][0]

        for j in range(i):
            prev_id = fold_ids[j]
            prev_max = fold_ranges[prev_id][1]

            if prev_max >= curr_min:
                issues.append(
                    f"Fold {prev_id} test max date ({prev_max.date()}) "
                    f">= fold {curr_id} test min date ({curr_min.date()}) — "
                    f"possible lookahead"
                )

    return {"ok": len(issues) == 0, "issues": issues}


# ────────────────────────────────────────────────────────────────────
# Save Results
# ────────────────────────────────────────────────────────────────────
def save_backtest_results(
    results: pd.DataFrame,
    metrics: Dict,
    market: str,
    run_id: str,
    horizon: str,
) -> Path:
    """Save backtest predictions and metrics as parquet."""
    out_dir = REPO / "data" / "foundry" / "backtests" / f"market={market}" / f"run_id={run_id}"
    out_dir.mkdir(parents=True, exist_ok=True)

    # Save prediction-level results
    results_path = out_dir / f"predictions_{horizon}.parquet"
    results.to_parquet(results_path, index=False)

    # Save metrics as a single-row parquet
    metrics_flat = {}
    for k, v in metrics.items():
        if isinstance(v, (int, float, str, bool, type(None))):
            metrics_flat[k] = v
        elif isinstance(v, list):
            metrics_flat[k] = str(v)
        elif isinstance(v, dict):
            for kk, vv in v.items():
                metrics_flat[f"{k}_{kk}"] = str(vv) if isinstance(vv, (dict, list)) else vv

    metrics_df = pd.DataFrame([metrics_flat])
    metrics_df["horizon"] = horizon
    metrics_df["market"] = market
    metrics_df["run_id"] = run_id
    metrics_path = out_dir / f"metrics_{horizon}.parquet"
    metrics_df.to_parquet(metrics_path, index=False)

    logger.info("Saved backtest results to %s", out_dir)
    return out_dir


# ────────────────────────────────────────────────────────────────────
# Full Backtest Pipeline (entry point)
# ────────────────────────────────────────────────────────────────────
def run_backtest_pipeline(
    features: pd.DataFrame,
    labels: pd.DataFrame,
    market: str = "US",
    run_id: str = "",
    horizons: Optional[List[str]] = None,
    train_window_days: int = 756,
    calib_window_days: int = 126,
    step_days: int = 21,
    min_train_rows: int = 500,
) -> Dict[str, Any]:
    """Run full backtest pipeline for one or more horizons.

    Returns a summary dict with per-horizon metrics and quality gate results.
    """
    if horizons is None:
        horizons = ["1d", "5d", "20d"]

    # Merge features and labels
    df = features.merge(labels, on=["date", "ticker"], how="inner")

    if df.empty:
        return {"ok": False, "reason": "empty merged dataset"}

    # Add regime labels
    regime_clf = RegimeClassifier()
    df = regime_clf.classify_dataframe(df)

    summary: Dict[str, Any] = {"ok": True, "horizons": {}}
    gates = load_quality_gates()

    for hz in horizons:
        ycol = f"y_up_{hz}"
        if ycol not in df.columns:
            summary["horizons"][hz] = {"ok": False, "reason": f"missing column {ycol}"}
            continue

        logger.info("Running walk-forward backtest for horizon=%s ...", hz)

        results = walk_forward_backtest(
            df,
            horizon=hz,
            train_window_days=train_window_days,
            calib_window_days=calib_window_days,
            step_days=step_days,
            min_train_rows=min_train_rows,
        )

        if results.empty:
            summary["horizons"][hz] = {"ok": False, "reason": "no walk-forward results"}
            continue

        # Compute aggregate metrics
        metrics = compute_metrics(results)

        # Compute per-regime metrics
        # Align regimes with results by joining on date+ticker
        results_with_regime = results.merge(
            df[["date", "ticker", "regime"]].drop_duplicates(),
            on=["date", "ticker"],
            how="left",
        )
        regime_metrics = {}
        if "regime" in results_with_regime.columns:
            regime_metrics = compute_per_regime_metrics(
                results_with_regime.drop(columns=["regime"], errors="ignore"),
                results_with_regime["regime"],
            )

        # Quality gate check
        gate_result = quality_gate_check_backtest(metrics, gates)

        # Save results
        if run_id:
            save_backtest_results(results, metrics, market, run_id, hz)

        # Lookahead validation
        lookahead_check = validate_no_lookahead(results, hz)

        summary["horizons"][hz] = {
            "metrics": metrics,
            "gate": gate_result,
            "regime_metrics": regime_metrics,
            "lookahead_check": lookahead_check,
            "n_folds": int(results["fold"].nunique()),
            "n_rows": len(results),
        }

        if not gate_result["ok"]:
            summary["ok"] = False

    return summary
