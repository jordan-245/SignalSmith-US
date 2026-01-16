---
layer: directive
tags: [layer/directive]
---

# build_features

## Purpose
Assemble market + doc signals into daily features keyed by (date, ticker).

## Inputs
- `prices_daily`, `benchmark_prices_daily`
- `docs_extracted` + metadata <= cutoff
- Feature config + universe version

## Outputs
- `features_daily` with `features_json`, feature_set_version
- Coverage metrics and run log

## Tools/Scripts (links to execution scripts)
- [[20_EXECUTION/build_features]]

## Edge cases
- Missing prices/docs; fill/null and flag gaps
- Cutoff alignment to avoid lookahead
- Schema changes may need backfill

## Run steps
1. Load price + doc signals per windows.
2. Compute market features and doc aggregates.
3. Assemble `features_json`, set feature_set_version, align to universe.
4. Write `features_daily`; log coverage/warnings.

## Learnings / Updates
- 
