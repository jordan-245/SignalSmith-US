---
layer: directive
tags: [layer/directive]
---

# ingest_prices

## Purpose
Pull daily OHLCV for S&P 500 tickers and SPY and persist before feature building, modeling, and reporting.

## Inputs
- Active universe version (tickers, as_of_date)
- Data vendor credentials (env)
- Target date (default: today) and cutoff time (08:15 ET)

## Outputs
- `prices_daily` rows for universe tickers
- `benchmark_prices_daily` row for SPY
- `pipeline_runs` entry for stage=market_data

## Tools/Scripts (links to execution scripts)
- [[20_EXECUTION/ingest_prices]]

## Edge cases
- Missing/late vendor data or partial coverage (>3% missing triggers warning)
- Market holidays or early closes
- Stale quotes or timezones causing misdated rows

## Run steps
1. Load active universe version for target date.
2. Pull OHLCV for tickers + SPY; retry on transient vendor errors.
3. Validate row counts and freshness; flag gaps and mark warnings.
4. Upsert into `prices_daily` and `benchmark_prices_daily`.
5. Log `pipeline_runs` with stats and warnings.

## Learnings / Updates
- 
