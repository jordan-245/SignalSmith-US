---
layer: directive
tags: [layer/directive]
---

# ingest_prices

## Purpose
Daily OHLCV for S&P 500 + SPY before features/modeling.

## Inputs
- Active universe version
- Vendor creds (env), target date, cutoff (08:15 ET)

## Outputs
- `prices_daily`, `benchmark_prices_daily`
- Run log entry for market_data stage

## Tools/Scripts (links to execution scripts)
- [[20_EXECUTION/ingest_prices]]

## Edge cases
- Vendor gaps/late data; warn if >3% missing
- Holidays/early closes
- Stale/misdated rows from timezone issues

## Run steps
1. Load active universe.
2. Pull OHLCV for tickers + SPY with retry.
3. Validate coverage/freshness; warn on gaps.
4. Upsert price tables; log run stats.

## Learnings / Updates
- 
