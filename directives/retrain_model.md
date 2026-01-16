---
layer: directive
tags: [layer/directive]
---

# retrain_model

## Purpose
Retrain models after feature/schema changes or drift.

## Inputs
- Rebuilt `features_daily`, `labels`
- Updated feature_set_version + model configs
- Universe alignment

## Outputs
- New `model_runs` with metrics/artifacts
- Comparison vs prior runs
- Run log for model_retrain

## Tools/Scripts (links to execution scripts)
- [[20_EXECUTION/retrain_model]]

## Edge cases
- Feature schema changes needing backfill
- Overfit on small data; compare to baselines
- Regressions; block promotion if below threshold

## Run steps
1. Load rebuilt features/labels with versions.
2. Train primary + baseline; walk-forward eval.
3. Compare to production; decide promotion.
4. Persist artifacts/metrics; log decisions/warnings.

## Learnings / Updates
- 
