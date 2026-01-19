---
layer: directive
tags: [layer/directive]
---

# evaluate_model

## Purpose
Assess model performance across regimes and windows to detect drift and validate improvements before promotion.

## Inputs
- `model_runs` artifacts and metrics
- Holdout or walk-forward slices (labels + features)
- Benchmark comparisons (SPY excess return)

## Outputs
- Evaluation report (metrics per period, confusion stats, calibration)
- Drift indicators (prediction/feature distribution shifts)
- Promotion decision notes; `pipeline_runs` entry for stage=model_eval

## Tools/Scripts (links to execution scripts)
- [[20_EXECUTION/evaluate_model]]

## Edge cases
- Data leakage; ensure splits respect time
- Unbalanced classes; track precision/recall, not just accuracy
- Regime shifts causing metric instability; flag for retrain or feature review

## Run steps
1. Load candidate and baseline model outputs over evaluation windows.
2. Compute metrics per year/regime; include uplift vs baseline.
3. Check prediction/feature distribution shifts.
4. Summarize promotion recommendation and risks.
5. Log results and update monitoring dashboards.

## Learnings / Updates
- 
