---
layer: directive
tags: [layer/directive]
---

# ingest_historical_prices

## Purpose
Backfill historical OHLCV for S&P 500 tickers and SPY to support feature/label rebuilding and model retraining.

## Inputs
- Universe membership by date/version
- Date range to backfill
- Data vendor credentials and rate limits

## Outputs
- `prices_daily` and `benchmark_prices_daily` rows across the requested window
- Backfill log entries in `pipeline_runs`

## Tools/Scripts (links to execution scripts)
- [[20_EXECUTION/ingest_historical_prices]]

## Edge cases
- Corporate actions or ticker changes; reconcile to instrument table
- Vendor gaps; retry or mark missing with warnings
- Large windows hitting rate limits; chunk and backoff

## Run steps
1. Resolve universe membership across the target range.
2. Chunk date ranges to stay within vendor limits.
3. Pull OHLCV for tickers + SPY; validate coverage.
4. Upsert into price tables with idempotent semantics.
5. Log backfill stats and any gaps for follow-up.

## Learnings / Updates
- Backfills over ~1y for ~500 tickers can take >10 minutes; use chunking to avoid timeouts.
- Recommended flags: `--chunk-days 120 --tickers-per-batch 200` (observed ~12–13 min, 4 chunks).
- Yahoo Finance may fail for tickers with dots or recent symbol changes (e.g., `BRK.B`, `BF.B`, `IPG`, `WBA`, `FI`, `K`). Expect “possibly delisted / no timezone” errors; capture in warnings and proceed.
