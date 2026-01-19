---
layer: directive
tags: [layer/directive]
---

# build_features

## Purpose
Aggregate market and document-derived signals into daily features keyed by (date, ticker) for modeling.

## Inputs
- `prices_daily`, `benchmark_prices_daily`
- `docs_extracted` (with sentiment/events) and document metadata <= cutoff
- Feature config (windows, aggregations, feature_set_version)
- Universe version for alignment

## Outputs
- `features_daily` rows with `features_json` and `feature_set_version`
- Coverage metrics and warnings
- `pipeline_runs` entry for stage=feature_builder

## Tools/Scripts (links to execution scripts)
- [[20_EXECUTION/build_features]]

## Edge cases
- Missing price data or sparse docs; fill with nulls and flag coverage gaps
- Timezone/cutoff alignment mistakes leading to lookahead; enforce `published_at <= cutoff`
- Schema changes requiring backfill

## Run steps
1. Load price and doc signals within configured windows.
2. Compute market features (returns, volatility, trend, volume, beta proxy).
3. Compute doc features (counts, sentiment/uncertainty aggregates, event flags, novelty where available).
4. Assemble `features_json`, enforce feature_set_version, and align to universe.
5. Write to `features_daily`; log coverage and warnings.

## Learnings / Updates
- 
