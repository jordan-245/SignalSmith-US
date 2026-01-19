---
layer: directive
tags: [layer/directive]
---

# run_model

## Purpose
Train and score the daily ranking model using the latest features, producing predictions and explanations before market open.

## Inputs
- `features_daily` (with feature_set_version)
- `labels` for training windows
- Model configs (LightGBM/XGBoost primary, logistic regression baseline)
- Universe version and run parameters (train window, horizons)

## Outputs
- `model_runs` record with metrics and artifact reference
- `predictions` rows with scores, ranks, explanation_json
- `pipeline_runs` entry for stage=model_runner

## Tools/Scripts (links to execution scripts)
- [[20_EXECUTION/run_model]]

## Edge cases
- Stale or incomplete features; halt scoring if coverage below threshold
- Small training window causing overfit/underfit; fall back to baseline
- Feature drift/regime shifts; log warnings for monitoring

## Run steps
1. Select training slice (rolling 3-5y) and validation slice (next period).
2. Train primary model; evaluate; train baseline for comparison.
3. Persist metrics/artifacts with feature_set_version and universe version.
4. Score current date for universe; produce ranks and explanations.
5. Write `predictions` and log run stats; mark warnings if metrics degrade.

## Learnings / Updates
- 
