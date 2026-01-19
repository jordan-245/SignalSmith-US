---
layer: directive
tags: [layer/directive]
---

# retrain_model

## Purpose
Re-train models after feature set/schema changes or significant performance drift, producing refreshed artifacts and metrics.

## Inputs
- `features_daily` (possibly rebuilt)
- `labels` for historical windows
- Updated feature_set_version and model configs
- Universe version alignment

## Outputs
- New `model_runs` with metrics and artifact references
- Comparison report vs prior model runs
- `pipeline_runs` entry for stage=model_retrain

## Tools/Scripts (links to execution scripts)
- [[20_EXECUTION/retrain_model]]

## Edge cases
- Feature schema changes requiring backfill alignment
- Overfitting on small datasets; use baselines and cross-period checks
- Metric regressions; block promotion if below thresholds

## Run steps
1. Load rebuilt features/labels aligned to universe/version.
2. Train primary + baseline models; run walk-forward evaluation.
3. Compare metrics to previous production model; decide promotion.
4. Persist artifacts and metrics with clear versioning.
5. Log retrain run with decisions and warnings.

## Learnings / Updates
- 
