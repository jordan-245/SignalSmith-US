#!/usr/bin/env python3
"""Signal Foundry — Model Hyperparameter Optimization

Runs systematic search over LightGBM params, ensemble weights,
LR regularization, calibration window, regime-aware modeling, and L1 reg.
"""

from __future__ import annotations

import datetime as dt
import glob
import json
import logging
import sys
import time
import warnings
from itertools import product
from pathlib import Path
from typing import Any, Dict, List, Optional, Tuple

import numpy as np
import pandas as pd
from sklearn.metrics import brier_score_loss, roc_auc_score

REPO = Path(__file__).resolve().parents[2]
sys.path.insert(0, str(REPO / "execution"))
sys.path.insert(0, str(REPO / "execution" / "foundry"))

from foundry_models import (
    FEATURE_COLS, BaselineLogistic, CalibrationWrapper,
    EnsembleModel, RegimeClassifier, TreeModel, train_model_stack,
)

try:
    import lightgbm as lgb
    _HAS_LGB = True
except ImportError:
    _HAS_LGB = False

logging.basicConfig(level=logging.INFO, format="%(asctime)s [%(name)s] %(message)s")
logger = logging.getLogger("foundry.optimize")
warnings.filterwarnings("ignore")


def load_all_prices() -> pd.DataFrame:
    price_files = sorted(glob.glob(str(REPO / "data/foundry/prices/market=US/date=*/part.parquet")))
    if not price_files:
        raise RuntimeError("No price data found")
    logger.info("Loading %d price files...", len(price_files))
    prices = pd.concat([pd.read_parquet(f) for f in price_files], ignore_index=True)
    prices["date"] = pd.to_datetime(prices["date"])
    prices = prices.drop_duplicates(subset=["date", "ticker"]).sort_values(["ticker", "date"]).reset_index(drop=True)
    logger.info("Prices: %d rows, %d tickers", len(prices), prices["ticker"].nunique())
    return prices


def _compute_rsi(series: pd.Series, window: int = 14) -> pd.Series:
    delta = series.diff()
    gain = (delta.where(delta > 0, 0)).rolling(window).mean()
    loss = (-delta.where(delta < 0, 0)).rolling(window).mean()
    rs = gain / (loss + 1e-10)
    return 100 - (100 / (1 + rs))


def build_features_local(prices: pd.DataFrame) -> pd.DataFrame:
    bench_px = prices.loc[prices["ticker"] == "SPY", ["date", "close"]].copy()
    bench_px = bench_px.sort_values("date").rename(columns={"close": "bench_close"})
    bench_px["bench_ret_20d"] = bench_px["bench_close"].pct_change(20)
    frames = []
    for t, g in prices.groupby("ticker"):
        if t == "SPY":
            continue
        g = g.sort_values("date").copy()
        s = g["close"].astype(float)
        v = g["volume"].astype(float) if "volume" in g.columns else pd.Series(np.nan, index=g.index)
        if len(s) < 250:
            continue
        rets = s.pct_change()
        sma20 = s.rolling(20).mean()
        vol_20d = rets.rolling(20).std()
        sma50 = s.rolling(50).mean()
        sma200 = s.rolling(200).mean()
        eps = 1e-10
        vol_ma_20 = v.rolling(20).mean()
        feat = pd.DataFrame({
            "date": g["date"].values, "ticker": str(t), "close": s.values,
            "ret_1d": rets.values,
            "ret_5d": (s / s.shift(5) - 1).values,
            "ret_20d": (s / s.shift(20) - 1).values,
            "vol_20d": vol_20d.values,
            "ma_ratio_20_50": (sma20 / (sma50 + eps)).values,
            "ma_ratio_50_200": (sma50 / (sma200 + eps)).values,
            "px_gt_sma200": (s > sma200).astype(float).values,
            "sma50_gt_sma200": (sma50 > sma200).astype(float).values,
            # Volume features (v2)
            "vol_ratio_20d": (v / (vol_ma_20 + eps)).values,
            "dollar_volume_20d": (s * v).rolling(20).mean().values,
            "volume_trend_5d": (v.rolling(5).mean() / (vol_ma_20 + eps)).values,
            # Sharpe-like (v2)
            "sharpe_5d": ((s / s.shift(5) - 1) / (vol_20d + 1e-8)).values,
            "sharpe_20d": ((s / s.shift(20) - 1) / (vol_20d + 1e-8)).values,
            # Mean reversion (v2)
            "rsi_14": _compute_rsi(s, 14).values,
            "z_score_20d": ((s.values - sma20.values) / (vol_20d.values * np.sqrt(20) + 1e-8)),
        })
        # Mean-reversion explicit signals (v3)
        rsi_vals = feat["rsi_14"].values
        feat["rsi_14_oversold"] = np.clip((70.0 - rsi_vals) / 40.0, 0.0, 1.0)
        feat["mean_revert_5d"] = -feat["ret_5d"].values
        feat["mean_revert_20d"] = -feat["ret_20d"].values
        frames.append(feat)
    feats = pd.concat(frames, ignore_index=True)
    feats["date"] = pd.to_datetime(feats["date"])
    feats = feats.merge(bench_px[["date", "bench_ret_20d"]], on="date", how="left")
    feats["rel_strength_20d"] = feats["ret_20d"] - feats["bench_ret_20d"]
    # Cross-sectional ranks (v2)
    feats["rank_ret_20d"] = feats.groupby("date")["ret_20d"].rank(pct=True)
    feats["rank_vol_20d"] = feats.groupby("date")["vol_20d"].rank(pct=True)
    feats = feats[["date", "ticker", "close"] + FEATURE_COLS].copy()
    feats = feats.dropna(subset=FEATURE_COLS, how="any")
    logger.info("Features: %d rows, %d tickers", len(feats), feats["ticker"].nunique())
    return feats


def build_labels_local(prices: pd.DataFrame) -> pd.DataFrame:
    frames = []
    for t, g in prices.groupby("ticker"):
        if t == "SPY":
            continue
        g = g.sort_values("date").copy()
        s = g["close"].astype(float)
        if len(s) < 30:
            continue
        lbl = pd.DataFrame({
            "date": g["date"].values, "ticker": str(t),
            "ret_fwd_5d": (s.shift(-5) / s - 1).values,
        })
        lbl["y_up_5d"] = (lbl["ret_fwd_5d"] > 0).astype(int)
        frames.append(lbl)
    labels = pd.concat(frames, ignore_index=True)
    labels["date"] = pd.to_datetime(labels["date"])
    logger.info("Labels: %d rows", len(labels))
    return labels


def prepare_dataset(prices: pd.DataFrame) -> pd.DataFrame:
    feats = build_features_local(prices)
    labels = build_labels_local(prices)
    df = feats.merge(labels, on=["date", "ticker"], how="inner")
    df = df.dropna(subset=FEATURE_COLS + ["y_up_5d"])
    df = df.sort_values("date").reset_index(drop=True)
    logger.info("Dataset: %d rows, %d tickers, %s→%s",
                len(df), df["ticker"].nunique(),
                df["date"].min().date(), df["date"].max().date())
    return df


def ts_cv_splits(df, n_splits=3, calib_size=63):
    dates = sorted(df["date"].dt.date.unique())
    n = len(dates)
    test_size = max(21, n // (n_splits + 2))
    splits = []
    for i in range(n_splits):
        te = n - (n_splits - 1 - i) * test_size
        ts = te - test_size
        ce = ts
        cs = max(0, ce - calib_size)
        tre = cs
        if tre < 100:
            continue
        train = df[df["date"].dt.date.isin(set(dates[:tre]))]
        calib = df[df["date"].dt.date.isin(set(dates[cs:ce]))]
        test = df[df["date"].dt.date.isin(set(dates[ts:te]))]
        if len(train) > 1000 and len(calib) > 200 and len(test) > 100:
            splits.append((train, calib, test))
            logger.info("  Split %d: train=%d calib=%d test=%d", i, len(train), len(calib), len(test))
    return splits


def compute_ece(y, p, n_bins=10):
    edges = np.linspace(0, 1, n_bins + 1)
    ece = 0.0
    n = len(y)
    if n == 0:
        return 0.0
    for i in range(n_bins):
        mask = (p >= edges[i]) & (p < edges[i + 1])
        if mask.sum() > 0:
            ece += abs(y[mask].mean() - p[mask].mean()) * mask.sum() / n
    return ece


def eval_config(splits, horizon="5d", lr_C=1.0, tree_params=None,
                lr_w=0.4, tree_w=0.6, opt_weights=False, reg_alpha=None):
    ycol = f"y_up_{horizon}"
    tp = tree_params or {}
    aucs, briers_u, briers_c, eces, weights = [], [], [], [], []

    for train, calib, test in splits:
        Xtr, ytr = train[FEATURE_COLS], train[ycol]
        Xca, yca = calib[FEATURE_COLS], calib[ycol]
        Xte, yte = test[FEATURE_COLS], test[ycol]

        lr = BaselineLogistic(C=lr_C)
        tree = TreeModel(**tp) if tp else TreeModel()
        lr.fit(Xtr, ytr)
        tree.fit(Xtr, ytr, eval_set=(Xca, yca))

        # If reg_alpha specified, retrain tree with it via direct LGB
        if reg_alpha is not None and _HAS_LGB and reg_alpha > 0:
            tree_model = lgb.LGBMClassifier(
                objective="binary",
                n_estimators=tp.get("n_estimators", 300),
                max_depth=tp.get("max_depth", 5),
                learning_rate=tp.get("learning_rate", 0.05),
                subsample=tp.get("subsample", 0.8),
                min_child_samples=tp.get("min_child_samples", 50),
                reg_lambda=tp.get("reg_lambda", 1.0),
                reg_alpha=reg_alpha,
                colsample_bytree=tp.get("colsample_bytree", 0.7),
                random_state=42, verbosity=-1, n_jobs=-1,
            )
            tree_model.fit(Xtr, ytr, eval_set=[(Xca, yca)],
                          callbacks=[lgb.early_stopping(50, verbose=False)])
            tree.model = tree_model
            tree._fitted = True

        lr_cp = lr.predict_proba(Xca)
        tr_cp = tree.predict_proba(Xca)

        lw, tw = lr_w, tree_w
        if opt_weights:
            best_a, best_ww = 0, (0.4, 0.6)
            for wl in np.arange(0, 1.05, 0.1):
                wt = 1.0 - wl
                try:
                    a = roc_auc_score(yca, wl * lr_cp + wt * tr_cp)
                    if a > best_a:
                        best_a, best_ww = a, (round(wl, 1), round(wt, 1))
                except ValueError:
                    pass
            lw, tw = best_ww
            weights.append(best_ww)

        ens = EnsembleModel(models=[lr, tree], weights={lr.name: lw, tree.name: tw})
        ens._fitted = True

        raw_ca = ens.predict_proba(Xca)
        cal = CalibrationWrapper(method="isotonic")
        cal.fit(raw_ca, yca.values)

        raw_te = ens.predict_proba(Xte)
        cal_te = cal.transform(raw_te)
        ya = yte.values.astype(float)

        try:
            aucs.append(roc_auc_score(ya, cal_te))
        except ValueError:
            pass
        briers_u.append(brier_score_loss(ya, raw_te))
        briers_c.append(brier_score_loss(ya, cal_te))
        eces.append(compute_ece(ya, cal_te))

    res = {
        "auc_mean": float(np.mean(aucs)) if aucs else None,
        "auc_std": float(np.std(aucs)) if aucs else None,
        "brier_uncal": float(np.mean(briers_u)) if briers_u else None,
        "brier_cal": float(np.mean(briers_c)) if briers_c else None,
        "ece": float(np.mean(eces)) if eces else None,
        "n_folds": len(aucs),
    }
    if opt_weights and weights:
        res["weights"] = weights
        res["avg_lr_w"] = float(np.mean([w[0] for w in weights]))
        res["avg_tree_w"] = float(np.mean([w[1] for w in weights]))
    return res


def eval_regime(splits, horizon="5d"):
    ycol = f"y_up_{horizon}"
    rc = RegimeClassifier()
    aucs, briers, eces = [], [], []

    for train, calib, test in splits:
        tr_r = rc.classify_dataframe(train.copy())
        ca_r = rc.classify_dataframe(calib.copy())
        te_r = rc.classify_dataframe(test.copy())
        preds, ys = [], []
        for regime in ["low", "medium", "high"]:
            tr_s = tr_r[tr_r["regime"] == regime]
            ca_s = ca_r[ca_r["regime"] == regime]
            te_s = te_r[te_r["regime"] == regime]
            if len(tr_s) < 500 or len(ca_s) < 100:
                tr_s, ca_s = tr_r, ca_r
            if len(te_s) == 0:
                continue
            try:
                ens, cal, _ = train_model_stack(
                    tr_s[FEATURE_COLS], tr_s[ycol],
                    ca_s[FEATURE_COLS], ca_s[ycol])
                raw = ens.predict_proba(te_s[FEATURE_COLS])
                preds.extend(cal.transform(raw).tolist())
                ys.extend(te_s[ycol].values.tolist())
            except Exception:
                pass
        if len(preds) > 10:
            ya, pa = np.array(ys, float), np.array(preds, float)
            try:
                aucs.append(roc_auc_score(ya, pa))
            except ValueError:
                pass
            briers.append(brier_score_loss(ya, pa))
            eces.append(compute_ece(ya, pa))

    return {
        "auc_mean": float(np.mean(aucs)) if aucs else None,
        "auc_std": float(np.std(aucs)) if aucs else None,
        "brier_cal": float(np.mean(briers)) if briers else None,
        "ece": float(np.mean(eces)) if eces else None,
        "n_folds": len(aucs),
    }


def run_optimization():
    t0 = time.time()
    logger.info("=" * 60)
    logger.info("SIGNAL FOUNDRY — MODEL OPTIMIZATION")
    logger.info("=" * 60)

    prices = load_all_prices()
    df = prepare_dataset(prices)
    splits = ts_cv_splits(df, n_splits=3, calib_size=63)
    logger.info("Created %d CV splits", len(splits))
    if len(splits) < 2:
        logger.error("Need ≥2 splits"); return

    R: Dict[str, Any] = {}

    # ── BASELINE ──
    logger.info("\n>>> BASELINE")
    bl_tp = dict(max_depth=5, n_estimators=300, learning_rate=0.05,
                 min_child_samples=50, reg_lambda=1.0, colsample_bytree=0.7)
    bl = eval_config(splits, tree_params=bl_tp, lr_w=0.4, tree_w=0.6)
    R["baseline"] = bl
    logger.info("AUC=%.4f ±%.4f  Brier=%.4f  ECE=%.4f",
                bl["auc_mean"] or 0, bl["auc_std"] or 0,
                bl["brier_cal"] or 0, bl["ece"] or 0)

    # ── STEP 1: LGBM Grid Search ──
    logger.info("\n>>> STEP 1: LightGBM Grid Search (81 combos)")
    grid = list(product([0.01, 0.05, 0.1], [3, 5, 7], [100, 300, 500], [30, 50, 100]))
    best_auc, best_tp = 0.0, {}
    lgbm_all = []
    for idx, (lr_v, md, ne, mcs) in enumerate(grid):
        tp = dict(learning_rate=lr_v, max_depth=md, n_estimators=ne,
                  min_child_samples=mcs, reg_lambda=1.0, colsample_bytree=0.7)
        r = eval_config(splits, tree_params=tp, lr_w=0.4, tree_w=0.6)
        a = r["auc_mean"] or 0
        lgbm_all.append({"p": tp, **r})
        if a > best_auc:
            best_auc, best_tp = a, tp.copy()
        if (idx + 1) % 20 == 0:
            logger.info("  [%d/81] best so far: %.4f", idx + 1, best_auc)

    lgbm_all.sort(key=lambda x: x.get("auc_mean") or 0, reverse=True)
    logger.info("Top 5:")
    for i, r in enumerate(lgbm_all[:5]):
        p = r["p"]
        logger.info("  %d. AUC=%.4f | lr=%.2f md=%d ne=%d mcs=%d",
                     i+1, r["auc_mean"], p["learning_rate"], p["max_depth"],
                     p["n_estimators"], p["min_child_samples"])
    R["lgbm_grid"] = {"best": best_tp, "best_auc": best_auc,
                       "top5": lgbm_all[:5]}

    # ── STEP 2: Ensemble Weights ──
    logger.info("\n>>> STEP 2: Ensemble Weight Optimization")
    ew = eval_config(splits, tree_params=best_tp, opt_weights=True)
    olw = ew.get("avg_lr_w", 0.4)
    otw = ew.get("avg_tree_w", 0.6)
    logger.info("AUC=%.4f  Optimal weights: LR=%.1f Tree=%.1f",
                ew["auc_mean"] or 0, olw, otw)
    R["ensemble_weights"] = ew

    # ── STEP 3: LR C ──
    logger.info("\n>>> STEP 3: LR Regularization (C)")
    best_c, best_c_auc = 1.0, 0.0
    lr_res = {}
    for c in [0.01, 0.1, 0.5, 1.0, 5.0, 10.0]:
        r = eval_config(splits, lr_C=c, tree_params=best_tp, lr_w=olw, tree_w=otw)
        lr_res[str(c)] = r
        a = r["auc_mean"] or 0
        logger.info("  C=%.2f: AUC=%.4f  Brier=%.4f  ECE=%.4f",
                     c, a, r["brier_cal"] or 0, r["ece"] or 0)
        if a > best_c_auc:
            best_c_auc, best_c = a, c
    logger.info("Best C=%.2f (AUC=%.4f)", best_c, best_c_auc)
    R["lr_C"] = {"best_C": best_c, "all": lr_res}

    # ── STEP 4: Calibration Window ──
    logger.info("\n>>> STEP 4: Calibration Window")
    cw_res = {}
    for cdays, lab in [(63, "3mo"), (126, "6mo"), (252, "1yr")]:
        cs = ts_cv_splits(df, n_splits=3, calib_size=cdays)
        if not cs:
            continue
        r = eval_config(cs, lr_C=best_c, tree_params=best_tp, lr_w=olw, tree_w=otw)
        cw_res[lab] = r
        logger.info("  %s: AUC=%.4f  Brier=%.4f  ECE=%.4f",
                     lab, r["auc_mean"] or 0, r["brier_cal"] or 0, r["ece"] or 0)
    R["calib_window"] = cw_res

    # ── STEP 5: Regime-Aware ──
    logger.info("\n>>> STEP 5: Regime-Aware Modeling")
    rg = eval_regime(splits)
    logger.info("AUC=%.4f ±%.4f  Brier=%.4f  ECE=%.4f",
                rg["auc_mean"] or 0, rg["auc_std"] or 0,
                rg["brier_cal"] or 0, rg["ece"] or 0)
    R["regime_aware"] = rg

    # ── STEP 6: L1 Reg ──
    logger.info("\n>>> STEP 6: L1 Regularization (reg_alpha)")
    best_alpha, best_alpha_auc = 0.0, 0.0
    l1_res = {}
    for alpha in [0.0, 0.01, 0.1, 0.5, 1.0, 2.0]:
        r = eval_config(splits, lr_C=best_c, tree_params=best_tp,
                        lr_w=olw, tree_w=otw, reg_alpha=alpha)
        l1_res[str(alpha)] = r
        a = r["auc_mean"] or 0
        logger.info("  alpha=%.2f: AUC=%.4f  Brier=%.4f  ECE=%.4f",
                     alpha, a, r["brier_cal"] or 0, r["ece"] or 0)
        if a > best_alpha_auc:
            best_alpha_auc, best_alpha = a, alpha
    logger.info("Best reg_alpha=%.2f (AUC=%.4f)", best_alpha, best_alpha_auc)
    R["l1_reg"] = {"best_alpha": best_alpha, "all": l1_res}

    # ── FINAL: Combined best config ──
    logger.info("\n>>> FINAL: Evaluating combined best config")
    final_tp = best_tp.copy()
    # Add reg_alpha to final config evaluation
    final = eval_config(splits, lr_C=best_c, tree_params=final_tp,
                        lr_w=olw, tree_w=otw, reg_alpha=best_alpha)
    R["final_optimized"] = final
    logger.info("FINAL: AUC=%.4f ±%.4f  Brier=%.4f  ECE=%.4f",
                final["auc_mean"] or 0, final["auc_std"] or 0,
                final["brier_cal"] or 0, final["ece"] or 0)

    elapsed = time.time() - t0
    R["elapsed_s"] = round(elapsed, 1)

    # ── Save results ──
    out_dir = REPO / "data" / "foundry" / "optimization"
    out_dir.mkdir(parents=True, exist_ok=True)
    out_path = out_dir / "optimization_results.json"
    with open(out_path, "w") as f:
        json.dump(R, f, indent=2, default=str)
    logger.info("\nResults saved to %s", out_path)

    # ── Generate Report ──
    generate_report(R, bl, final, best_tp, best_c, olw, otw, best_alpha, elapsed)

    return R


def generate_report(R, baseline, final, best_tp, best_c, olw, otw, best_alpha, elapsed):
    """Generate markdown optimization report."""
    bl = baseline
    fn = final

    def fmt(v, d=4):
        return f"{v:.{d}f}" if v is not None else "N/A"

    def delta(new, old):
        if new is None or old is None:
            return "N/A"
        d = new - old
        sign = "+" if d >= 0 else ""
        return f"{sign}{d:.4f}"

    lines = [
        "# Signal Foundry — Model Optimization Report",
        f"**Date:** {dt.datetime.now().strftime('%Y-%m-%d %H:%M')}",
        f"**Duration:** {elapsed:.0f}s",
        "",
        "## Summary",
        "",
        "| Metric | Baseline | Optimized | Delta |",
        "|--------|----------|-----------|-------|",
        f"| AUC (mean) | {fmt(bl['auc_mean'])} | {fmt(fn['auc_mean'])} | {delta(fn['auc_mean'], bl['auc_mean'])} |",
        f"| AUC (std) | {fmt(bl['auc_std'])} | {fmt(fn['auc_std'])} | {delta(fn['auc_std'], bl['auc_std'])} |",
        f"| Brier (cal) | {fmt(bl['brier_cal'])} | {fmt(fn['brier_cal'])} | {delta(fn['brier_cal'], bl['brier_cal'])} |",
        f"| ECE | {fmt(bl['ece'])} | {fmt(fn['ece'])} | {delta(fn['ece'], bl['ece'])} |",
        "",
        "## Best Hyperparameters Found",
        "",
        "### LightGBM",
        f"- `learning_rate`: {best_tp.get('learning_rate', 0.05)}",
        f"- `max_depth`: {best_tp.get('max_depth', 5)}",
        f"- `n_estimators`: {best_tp.get('n_estimators', 300)}",
        f"- `min_child_samples`: {best_tp.get('min_child_samples', 50)}",
        f"- `reg_lambda`: {best_tp.get('reg_lambda', 1.0)}",
        f"- `colsample_bytree`: {best_tp.get('colsample_bytree', 0.7)}",
        f"- `reg_alpha` (L1): {best_alpha}",
        "",
        "### Logistic Regression",
        f"- `C`: {best_c}",
        "",
        "### Ensemble Weights",
        f"- LR weight: {olw:.1f}",
        f"- Tree weight: {otw:.1f}",
        "",
    ]

    # LightGBM top 5
    top5 = R.get("lgbm_grid", {}).get("top5", [])
    if top5:
        lines.extend([
            "## LightGBM Grid Search — Top 5",
            "",
            "| Rank | LR | Depth | Trees | MinChild | AUC | Brier | ECE |",
            "|------|----|-------|-------|----------|-----|-------|-----|",
        ])
        for i, r in enumerate(top5):
            p = r["p"]
            lines.append(
                f"| {i+1} | {p['learning_rate']} | {p['max_depth']} | "
                f"{p['n_estimators']} | {p['min_child_samples']} | "
                f"{fmt(r.get('auc_mean'))} | {fmt(r.get('brier_cal'))} | "
                f"{fmt(r.get('ece'))} |"
            )
        lines.append("")

    # Ensemble weights
    ew = R.get("ensemble_weights", {})
    if "weights" in ew:
        lines.extend([
            "## Ensemble Weight Search",
            f"- Per-fold optimal: {ew['weights']}",
            f"- Average: LR={ew.get('avg_lr_w', 0.4):.1f}, Tree={ew.get('avg_tree_w', 0.6):.1f}",
            f"- AUC with optimized weights: {fmt(ew.get('auc_mean'))}",
            "",
        ])

    # LR C
    lr_data = R.get("lr_C", {})
    lr_all = lr_data.get("all", {})
    if lr_all:
        lines.extend([
            "## LR Regularization (C)",
            "",
            "| C | AUC | Brier | ECE |",
            "|---|-----|-------|-----|",
        ])
        for c, r in sorted(lr_all.items(), key=lambda x: float(x[0])):
            lines.append(f"| {c} | {fmt(r.get('auc_mean'))} | {fmt(r.get('brier_cal'))} | {fmt(r.get('ece'))} |")
        lines.extend(["", f"**Best C:** {lr_data.get('best_C', 1.0)}", ""])

    # Calibration window
    cw = R.get("calib_window", {})
    if cw:
        lines.extend([
            "## Calibration Window",
            "",
            "| Window | AUC | Brier | ECE |",
            "|--------|-----|-------|-----|",
        ])
        for lab, r in cw.items():
            lines.append(f"| {lab} | {fmt(r.get('auc_mean'))} | {fmt(r.get('brier_cal'))} | {fmt(r.get('ece'))} |")
        lines.append("")

    # Regime-aware
    rg = R.get("regime_aware", {})
    if rg:
        lines.extend([
            "## Regime-Aware Modeling",
            f"- AUC: {fmt(rg.get('auc_mean'))} (±{fmt(rg.get('auc_std'))})",
            f"- Brier: {fmt(rg.get('brier_cal'))}",
            f"- ECE: {fmt(rg.get('ece'))}",
            f"- vs Baseline AUC: {delta(rg.get('auc_mean'), bl['auc_mean'])}",
            "",
        ])

    # L1 reg
    l1 = R.get("l1_reg", {})
    l1_all = l1.get("all", {})
    if l1_all:
        lines.extend([
            "## L1 Regularization (reg_alpha)",
            "",
            "| reg_alpha | AUC | Brier | ECE |",
            "|-----------|-----|-------|-----|",
        ])
        for a, r in sorted(l1_all.items(), key=lambda x: float(x[0])):
            lines.append(f"| {a} | {fmt(r.get('auc_mean'))} | {fmt(r.get('brier_cal'))} | {fmt(r.get('ece'))} |")
        lines.extend(["", f"**Best reg_alpha:** {l1.get('best_alpha', 0)}", ""])

    # Recommended config
    lines.extend([
        "## Recommended Production Config",
        "",
        "```python",
        "# foundry_models.py — TreeModel defaults",
        f"max_depth={best_tp.get('max_depth', 5)},",
        f"n_estimators={best_tp.get('n_estimators', 300)},",
        f"learning_rate={best_tp.get('learning_rate', 0.05)},",
        f"min_child_samples={best_tp.get('min_child_samples', 50)},",
        f"reg_lambda={best_tp.get('reg_lambda', 1.0)},",
        f"reg_alpha={best_alpha},",
        f"colsample_bytree={best_tp.get('colsample_bytree', 0.7)},",
        "",
        f"# BaselineLogistic",
        f"C={best_c},",
        "",
        f"# EnsembleModel weights",
        f"lr_weight={olw:.1f},",
        f"tree_weight={otw:.1f},",
        "```",
        "",
    ])

    report_text = "\n".join(lines)
    report_path = REPO / "data" / "foundry" / "optimization" / "optimization_report.md"
    report_path.parent.mkdir(parents=True, exist_ok=True)
    report_path.write_text(report_text, encoding="utf-8")
    logger.info("Report saved to %s", report_path)

    # Also print to stdout
    print("\n" + report_text)


if __name__ == "__main__":
    run_optimization()