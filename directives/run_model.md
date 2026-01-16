---
layer: directive
tags: [layer/directive]
---

# run_model

## Purpose
Train/score the daily ranking model to produce pre-open predictions + explanations.

## Inputs
- `features_daily` + feature_set_version
- `labels` and model configs
- Universe version, train window, horizons

## Outputs
- `model_runs` with metrics/artifact ref
- `predictions` with scores/ranks/explanations
- Run log entry for model_runner

## Tools/Scripts (links to execution scripts)
- [[20_EXECUTION/run_model]]

## Edge cases
- Stale/incomplete features; halt scoring if low coverage
- Short training windows; compare against baseline
- Drift/regime shifts; log warnings

## Run steps
1. Pick train/validation slices.
2. Train primary + baseline; compare metrics.
3. Persist artifacts/metrics with versions.
4. Score current date; produce ranks/explanations.
5. Write `predictions`; log stats/warnings.

## Learnings / Updates
- 
