---
layer: directive
tags: [layer/directive]
---

# evaluate_model

## Purpose
Assess model performance across regimes/windows before promotion.

## Inputs
- `model_runs` artifacts/metrics
- Walk-forward slices (features + labels)
- Benchmark (SPY excess return)

## Outputs
- Evaluation report with metrics per period
- Drift indicators and promotion notes
- Run log for model_eval

## Tools/Scripts (links to execution scripts)
- [[20_EXECUTION/evaluate_model]]

## Edge cases
- Time-based splits to avoid leakage
- Unbalanced classes; monitor precision/recall
- Regime shifts; flag for retrain/feature review

## Run steps
1. Load candidate + baseline outputs.
2. Compute metrics per period; compare uplift vs baseline.
3. Check prediction/feature shifts.
4. Summarize promotion recommendation + risks; log results.

## Learnings / Updates
- 
