---
layer: directive
tags: [layer/directive]
---

# ingest_historical_prices

## Purpose
Backfill historical OHLCV for S&P 500 + SPY for rebuilds/retraining.

## Inputs
- Universe by date/version
- Date range
- Vendor creds/rate limits

## Outputs
- Backfilled `prices_daily` + `benchmark_prices_daily`
- Backfill run log

## Tools/Scripts (links to execution scripts)
- [[20_EXECUTION/ingest_historical_prices]]

## Edge cases
- Corporate actions/ticker changes; reconcile
- Vendor gaps; retry or mark missing
- Large windows; chunk/backoff

## Run steps
1. Resolve universe across range.
2. Chunk to respect limits.
3. Pull OHLCV; validate coverage.
4. Upsert price tables; log stats/gaps.

## Learnings / Updates
- 
