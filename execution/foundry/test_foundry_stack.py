"""End-to-end smoke test for foundry models + backtest on synthetic data.

Run with:
  source .venv/bin/activate
  python -u execution/foundry/test_foundry_stack.py
"""

from __future__ import annotations

import datetime as dt
import sys
from pathlib import Path

import numpy as np
import pandas as pd

# Ensure sibling imports work
sys.path.insert(0, str(Path(__file__).resolve().parent))

from foundry_models import (
    FEATURE_COLS,
    BaselineLogistic,
    CalibrationWrapper,
    EnsembleModel,
    RegimeClassifier,
    TreeModel,
    train_model_stack,
)
from foundry_backtest import (
    compute_metrics,
    quality_gate_check_backtest,
    run_backtest_pipeline,
    save_backtest_results,
    validate_no_lookahead,
    walk_forward_backtest,
)

np.random.seed(42)

REPO = Path(__file__).resolve().parents[2]


def generate_synthetic_data(
    n_tickers: int = 5,
    n_days: int = 1200,   # ~4.8 years
    start_date: str = "2020-01-02",
) -> tuple[pd.DataFrame, pd.DataFrame]:
    """Create synthetic features and labels for testing."""
    dates = pd.bdate_range(start_date, periods=n_days, freq="B")
    tickers = [f"SYN{i:02d}" for i in range(n_tickers)]

    rows_feat = []
    rows_label = []

    for t in tickers:
        # Simulate random walk price
        px = 100.0 * np.exp(np.cumsum(np.random.normal(0.0003, 0.015, n_days)))
        vol = np.random.uniform(1e6, 1e8, n_days)  # synthetic volume
        rets = np.diff(np.log(px), prepend=np.log(px[0]))
        vol_20 = pd.Series(rets).rolling(20).std().values
        vol_ma_20 = pd.Series(vol).rolling(20).mean().values

        for i in range(250, n_days):  # skip first 250 for warm-up
            ret_1d = rets[i]
            ret_5d = np.sum(rets[max(i - 4, 0) : i + 1])
            ret_20d = np.sum(rets[max(i - 19, 0) : i + 1])
            sma50 = np.mean(px[max(i - 49, 0) : i + 1])
            sma200 = np.mean(px[max(i - 199, 0) : i + 1])

            sma20 = np.mean(px[max(i - 19, 0) : i + 1])
            v20 = vol_20[i] if not np.isnan(vol_20[i]) else 0.015
            vm20 = vol_ma_20[i] if not np.isnan(vol_ma_20[i]) else 1e7

            # RSI approximation
            rsi = 50.0 + np.random.normal(0, 15)
            rsi = max(0, min(100, rsi))

            rows_feat.append({
                "date": dates[i],
                "ticker": t,
                # Original features
                "ret_1d": ret_1d,
                "ret_5d": ret_5d,
                "ret_20d": ret_20d,
                "vol_20d": v20,
                "ma_ratio_20_50": sma20 / sma50 if sma50 != 0 else 1.0,
                "ma_ratio_50_200": sma50 / sma200 if sma200 != 0 else 1.0,
                "px_gt_sma200": float(px[i] > sma200),
                "sma50_gt_sma200": float(sma50 > sma200),
                "rel_strength_20d": ret_20d + np.random.normal(0, 0.005),
                # Volume features (v2)
                "vol_ratio_20d": vol[i] / (vm20 + 1e-10),
                "dollar_volume_20d": np.mean(px[max(i-19,0):i+1] * vol[max(i-19,0):i+1]),
                "volume_trend_5d": np.mean(vol[max(i-4,0):i+1]) / (vm20 + 1e-10),
                # Volatility-adjusted returns (v2)
                "sharpe_5d": ret_5d / (v20 + 1e-8),
                "sharpe_20d": ret_20d / (v20 + 1e-8),
                # Mean reversion features (v2)
                "rsi_14": rsi,
                "z_score_20d": (px[i] - sma20) / (v20 * np.sqrt(20) + 1e-8),
                # Cross-sectional ranks are filled per-date below
                "px": px[i],
                "sma50": sma50,
                "sma200": sma200,
            })

            # Forward-looking labels (would come from build_labels in production)
            if i + 20 < n_days:
                rows_label.append({
                    "date": dates[i],
                    "ticker": t,
                    "y_up_1d": int(px[i + 1] > px[i]) if i + 1 < n_days else 0,
                    "y_up_5d": int(px[min(i + 5, n_days - 1)] > px[i]),
                    "y_up_20d": int(px[min(i + 20, n_days - 1)] > px[i]),
                    "ret_fwd_1d": (px[i + 1] / px[i] - 1) if i + 1 < n_days else 0.0,
                    "ret_fwd_5d": (px[min(i + 5, n_days - 1)] / px[i] - 1),
                    "ret_fwd_20d": (px[min(i + 20, n_days - 1)] / px[i] - 1),
                })

    features = pd.DataFrame(rows_feat)
    # Add cross-sectional rank features (v2)
    features["rank_ret_20d"] = features.groupby("date")["ret_20d"].rank(pct=True)
    features["rank_vol_20d"] = features.groupby("date")["vol_20d"].rank(pct=True)

    # Mean-reversion explicit signals (v3)
    features["rsi_14_oversold"] = np.clip((70.0 - features["rsi_14"].values) / 40.0, 0.0, 1.0)
    features["mean_revert_5d"] = -features["ret_5d"].values
    features["mean_revert_20d"] = -features["ret_20d"].values

    labels = pd.DataFrame(rows_label)
    return features, labels


def test_individual_models():
    """Test each model class individually."""
    print("=" * 60)
    print("TEST: Individual models")
    print("=" * 60)

    features, labels = generate_synthetic_data(n_tickers=3, n_days=800)
    df = features.merge(labels, on=["date", "ticker"], how="inner")

    X = df[FEATURE_COLS]
    y = df["y_up_5d"]

    # Split
    split = int(len(X) * 0.7)
    X_train, X_test = X.iloc[:split], X.iloc[split:]
    y_train, y_test = y.iloc[:split], y.iloc[split:]

    # Logistic
    lr = BaselineLogistic()
    lr.fit(X_train, y_train)
    p_lr = lr.predict_proba(X_test)
    assert p_lr.shape == (len(X_test),), f"LR shape mismatch: {p_lr.shape}"
    assert 0 <= p_lr.min() and p_lr.max() <= 1, "LR probs out of [0,1]"
    print(f"  ✓ BaselineLogistic: mean_prob={p_lr.mean():.4f}")

    # Tree
    tree = TreeModel()
    tree.fit(X_train, y_train)
    p_tree = tree.predict_proba(X_test)
    assert p_tree.shape == (len(X_test),)
    assert 0 <= p_tree.min() and p_tree.max() <= 1
    print(f"  ✓ TreeModel ({tree.name}): mean_prob={p_tree.mean():.4f}")

    # Ensemble
    ens = EnsembleModel(models=[lr, tree], weights={"logistic": 0.4, tree.name: 0.6})
    ens._fitted = True
    p_ens = ens.predict_proba(X_test)
    assert p_ens.shape == (len(X_test),)
    expected_manual = 0.4 * p_lr + 0.6 * p_tree
    np.testing.assert_allclose(p_ens, expected_manual, atol=1e-10)
    print(f"  ✓ EnsembleModel: mean_prob={p_ens.mean():.4f}  (weights verified)")

    # Calibration
    cal_iso = CalibrationWrapper(method="isotonic")
    cal_iso.fit(p_ens[:200], y_test.values[:200])
    p_cal = cal_iso.transform(p_ens[200:])
    assert 0 <= p_cal.min() and p_cal.max() <= 1
    print(f"  ✓ CalibrationWrapper (isotonic): mean_cal={p_cal.mean():.4f}")

    cal_platt = CalibrationWrapper(method="platt")
    cal_platt.fit(p_ens[:200], y_test.values[:200])
    p_platt = cal_platt.transform(p_ens[200:])
    assert 0 <= p_platt.min() and p_platt.max() <= 1
    print(f"  ✓ CalibrationWrapper (platt): mean_cal={p_platt.mean():.4f}")

    print()


def test_regime_classifier():
    """Test regime classification."""
    print("=" * 60)
    print("TEST: Regime classifier")
    print("=" * 60)

    features, _ = generate_synthetic_data(n_tickers=3, n_days=800)

    rc = RegimeClassifier()
    df_regime = rc.classify_dataframe(features)

    assert "regime" in df_regime.columns
    regimes = df_regime["regime"].value_counts()
    print(f"  Regime distribution:\n{regimes.to_string()}")
    assert set(regimes.index).issubset({"low", "medium", "high"})
    print("  ✓ RegimeClassifier works")
    print()


def test_train_model_stack():
    """Test the convenience function."""
    print("=" * 60)
    print("TEST: train_model_stack")
    print("=" * 60)

    features, labels = generate_synthetic_data(n_tickers=3, n_days=800)
    df = features.merge(labels, on=["date", "ticker"], how="inner")

    X = df[FEATURE_COLS]
    y = df["y_up_5d"]

    # Split into train, calib, test
    n = len(X)
    X_train, X_calib, X_test = X.iloc[:int(n*0.6)], X.iloc[int(n*0.6):int(n*0.8)], X.iloc[int(n*0.8):]
    y_train, y_calib, y_test = y.iloc[:int(n*0.6)], y.iloc[int(n*0.6):int(n*0.8)], y.iloc[int(n*0.8):]

    ens, cal, diag = train_model_stack(X_train, y_train, X_calib, y_calib)
    p = ens.predict_proba(X_test)
    p_cal = cal.transform(p)

    print(f"  Diagnostics: {diag}")
    print(f"  Raw probs: mean={p.mean():.4f} std={p.std():.4f}")
    print(f"  Cal probs: mean={p_cal.mean():.4f} std={p_cal.std():.4f}")
    assert diag["brier_cal"] <= diag["brier_uncal"] + 0.05  # calibration shouldn't make things much worse
    print("  ✓ train_model_stack works")
    print()


def test_walk_forward_backtest():
    """Test walk-forward backtest on synthetic data."""
    print("=" * 60)
    print("TEST: Walk-forward backtest")
    print("=" * 60)

    features, labels = generate_synthetic_data(n_tickers=5, n_days=1200)
    df = features.merge(labels, on=["date", "ticker"], how="inner")

    results = walk_forward_backtest(
        df,
        horizon="5d",
        train_window_days=500,
        calib_window_days=100,
        step_days=30,
        min_train_rows=200,
    )

    assert not results.empty, "Walk-forward produced no results"
    assert set(results.columns) == {"date", "ticker", "y_true", "p_raw", "p_cal", "fold"}
    print(f"  Folds: {results['fold'].nunique()}")
    print(f"  Total rows: {len(results)}")
    print(f"  Date range: {results['date'].min().date()} → {results['date'].max().date()}")

    # Metrics
    metrics = compute_metrics(results)
    assert metrics["ok"], f"Metrics failed: {metrics}"
    print(f"  AUC-ROC: {metrics['auc_roc']:.4f}")
    print(f"  Brier (raw): {metrics['brier_raw']:.4f}")
    print(f"  Brier (cal): {metrics['brier_cal']:.4f}")
    print(f"  Hit rate: {metrics['hit_rate']:.4f} (baseline={metrics['baseline_rate']:.4f})")
    print(f"  Cal slope: {metrics['calibration_slope']:.4f}")

    # Quality gate check
    gate = quality_gate_check_backtest(metrics)
    print(f"  Quality gate: {'PASS' if gate['ok'] else 'FAIL'}")
    if not gate["ok"]:
        print(f"    Reasons: {gate['reasons']}")

    # Lookahead check
    la = validate_no_lookahead(results, "5d")
    print(f"  Lookahead check: {'OK' if la['ok'] else 'ISSUES: ' + str(la['issues'])}")

    print("  ✓ Walk-forward backtest works")
    print()
    return results, metrics


def test_save_backtest():
    """Test saving backtest results to parquet."""
    print("=" * 60)
    print("TEST: Save backtest results")
    print("=" * 60)

    features, labels = generate_synthetic_data(n_tickers=3, n_days=800)
    df = features.merge(labels, on=["date", "ticker"], how="inner")

    results = walk_forward_backtest(
        df,
        horizon="5d",
        train_window_days=400,
        calib_window_days=80,
        step_days=30,
        min_train_rows=100,
    )
    metrics = compute_metrics(results)

    out_dir = save_backtest_results(results, metrics, "US", "test_run_001", "5d")
    assert out_dir.exists()
    preds_file = out_dir / "predictions_5d.parquet"
    metrics_file = out_dir / "metrics_5d.parquet"
    assert preds_file.exists(), f"Missing {preds_file}"
    assert metrics_file.exists(), f"Missing {metrics_file}"

    # Read back and verify
    preds_back = pd.read_parquet(preds_file)
    assert len(preds_back) == len(results)
    print(f"  Saved {len(preds_back)} rows to {preds_file}")

    metrics_back = pd.read_parquet(metrics_file)
    print(f"  Saved metrics to {metrics_file}")
    print(f"  Columns: {list(metrics_back.columns)}")

    print("  ✓ Save works")
    print()


def test_full_pipeline():
    """Test the full backtest pipeline entry point."""
    print("=" * 60)
    print("TEST: Full backtest pipeline (run_backtest_pipeline)")
    print("=" * 60)

    features, labels = generate_synthetic_data(n_tickers=5, n_days=1200)

    summary = run_backtest_pipeline(
        features=features,
        labels=labels,
        market="US",
        run_id="test_pipeline_001",
        horizons=["5d"],
        train_window_days=500,
        calib_window_days=100,
        step_days=30,
        min_train_rows=200,
    )

    assert "horizons" in summary
    assert "5d" in summary["horizons"]

    hz = summary["horizons"]["5d"]
    print(f"  5d horizon:")
    print(f"    Folds: {hz['n_folds']}")
    print(f"    Rows: {hz['n_rows']}")
    print(f"    AUC: {hz['metrics'].get('auc_roc', 'N/A')}")
    print(f"    Gate: {'PASS' if hz['gate']['ok'] else 'FAIL: ' + str(hz['gate']['reasons'])}")
    if hz.get("regime_metrics"):
        for regime, rm in hz["regime_metrics"].items():
            if rm.get("ok"):
                print(f"    Regime {regime}: AUC={rm.get('auc_roc', 'N/A'):.4f}, n={rm.get('n_rows')}")
            else:
                print(f"    Regime {regime}: {rm.get('reason', 'no data')}")

    print(f"  Overall: {'PASS' if summary['ok'] else 'FAIL'}")
    print("  ✓ Full pipeline works")
    print()


def main():
    print("\n🔬 Signal Foundry — Model & Backtest Stack Tests\n")

    test_individual_models()
    test_regime_classifier()
    test_train_model_stack()
    test_walk_forward_backtest()
    test_save_backtest()
    test_full_pipeline()

    print("=" * 60)
    print("✅ ALL TESTS PASSED")
    print("=" * 60)


if __name__ == "__main__":
    main()
