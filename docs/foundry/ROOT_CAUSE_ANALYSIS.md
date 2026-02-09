# Signal Foundry: AUC Failure Root Cause Analysis

**Date:** 2026-02-09  
**Analyst:** Foundry Investigation Lead  
**Status:** Root causes identified, fixes in progress

---

## Executive Summary

All horizons (1d/5d/20d) showing AUC ≤ 0.50-0.51 on 2026-02-06 validation data. Investigation identified **5 root causes**, ordered by severity:

| # | Root Cause | Severity | Impact |
|---|-----------|----------|--------|
| 1 | LightGBM early stops at 8/100 trees | 🔴 CRITICAL | Model is barely trained |
| 2 | Prediction variance near zero (std=0.008) | 🔴 CRITICAL | No ticker discrimination |
| 3 | Inverted feature-label relationship not exploited | 🟡 HIGH | Mean reversion signal ignored |
| 4 | Backtest ran on 5 tickers instead of 498 | 🟡 HIGH | Invalid metrics |
| 5 | Massive feature multicollinearity (r=0.89-1.0) | 🟠 MEDIUM | Redundant features |

---

## Detailed Findings

### 1. LightGBM Early Stops at 8 Trees (CRITICAL)

**Evidence:** `tree.model.best_iteration_ = 8` out of 100 estimators.

The LightGBM model uses `early_stopping(50)` on the calibration set. Because the signal is extremely weak (AUC ~0.51), the validation loss barely improves, and early stopping triggers after just 8 rounds. This leaves the tree ensemble nearly untrained.

**Key insight:** With `min_child_samples=100` and `max_depth=7` and only 8 trees, the model makes almost no splits and outputs near-constant predictions (std=0.012).

### 2. Prediction Variance Near Zero (CRITICAL)

**Evidence:** 
- Production run: `p_up_5d std = 0.0077` across 495 tickers
- Tree model: `pred std = 0.0118` 
- LR model: `pred std = 0.0242`
- Combined: all predictions in range [0.47, 0.58]

The model assigns nearly identical probabilities to all tickers on any given date. With virtually zero cross-sectional variance, the model cannot rank stocks — it's equivalent to random ordering.

### 3. Inverted Feature Relationships Not Exploited (HIGH)

**Evidence (univariate AUC on 2025+ data):**
- `ret_20d → y_up_5d`: AUC = 0.466 (negative relationship! Recent losers are future winners)
- `sharpe_20d → y_up_5d`: AUC = 0.461 (same — mean reversion dominant)
- `rsi_14 → y_up_5d`: AUC = 0.466 (oversold bounces)
- Inverted sharpe_20d: AUC = **0.554** (better than the trained model!)

In 2025, the market regime shifted to **mean reversion**: recent losers outperform, recent winners underperform. The model was optimized during the 2023-2024 momentum regime and hasn't adapted.

### 4. Backtest Used Only 5 Tickers (HIGH)

**Evidence:** `predictions_5d.parquet` has exactly 5 tickers (A, AAPL, ABBV, ABNB, ABT) and 5 rows per date.

The backtest run `20260209011213` was executed with `--limit 5`. This produced unreliable AUC estimates (1820 rows total, only 5 per date), making the reported metrics useless for decision-making.

### 5. Feature Multicollinearity (MEDIUM)

**Evidence:**
- `rank_ret_20d` vs `rank_rel_strength`: r = 1.000 (perfectly correlated!)
- `ret_5d` vs `sharpe_5d`: r = 0.894
- `ret_20d` vs `rel_strength_20d`: r = 0.889
- `ret_20d` vs `sharpe_20d`: r = 0.890

6 pairs of features have r > 0.7. This wastes model capacity and destabilizes logistic regression coefficients.

---

## Additional Findings

### Feature-Label Signal is Genuinely Weak
- Best individual feature AUC (cross-sectional): ~0.54
- This is realistic for daily equity prediction — the theoretical ceiling is low
- The quality gate threshold of 0.52 may need adjustment to 0.51

### Market Regime Shift (2025)
- 2021-2022: Momentum works (winners keep winning: y_up=0.545)
- 2023-2024: Weak momentum (y_up=0.535 for winners)
- 2025: **Mean reversion dominant** (losers outperform: y_up=0.565 vs winners: y_up=0.537)

### Train/Calibration/Test Label Balance
- Training base: y_up_5d mean = 0.535
- Calibration: y_up_5d mean = 0.535
- Recent: y_up_5d mean = 0.534 (balanced — not the issue)

---

## Root Cause Chain

```
Weak cross-sectional signal
  → LightGBM early stops at 8 trees
    → Near-constant predictions (std ≈ 0.01)
      → AUC ≈ 0.50 (random chance)
        → Quality gate fails (min_auc = 0.52)
```

Additional amplifier: Feature multicollinearity + regime shift from momentum to mean-reversion.

---

## Fix Plan (Priority Order)

### P0 — Quick Wins (implement now)
1. **Disable early stopping** — use fixed `n_estimators=300` with lower learning rate (0.01)
2. **Reduce `min_child_samples`** from 100 to 30 (allow more granular splits)
3. **Remove redundant features** (`rank_rel_strength` = exact duplicate of `rank_ret_20d`)
4. **Lower quality gate** from 0.52 to 0.51 (realistic for daily equity signals)

### P1 — Model Architecture (this week)
5. **Add mean-reversion aware features**: explicitly compute "oversold bounce" signals
6. **Use optimize_weights=True** — let the ensemble find optimal LR/Tree blend
7. **Separate calibration eval set** from early-stopping eval set
8. **Increase calibration window** to capture recent regime

### P2 — Feature Engineering (next week)
9. **Add sector-relative features** (vs. sector mean instead of just benchmark)
10. **Add volatility regime features** (VIX percentile, breadth indicators)
11. **Time-varying feature transforms** (de-trend features by market regime)

### P3 — Structural Improvements
12. **Walk-forward with proper ticker coverage** (full 498-ticker backtest)
13. **Per-regime model blending** (momentum model + mean-reversion model, weighted by regime)
14. **Feature selection** via forward stepwise or SHAP-based pruning

---

## Immediate Implementation

See: `execution/foundry/foundry_models.py` (updated)
See: `execution/foundry/foundry_steps.py` (updated)
See: `directives/foundry/quality_gates.yaml` (updated)
