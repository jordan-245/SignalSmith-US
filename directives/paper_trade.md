---
layer: directive
tags: [layer/directive]
---

# paper_trade

## Purpose
Generate daily paper trades from model predictions using VWAP fills, enforce 5-day minimum hold, and track portfolio performance.

## Inputs
- `predictions` (Top 10)
- `prices_daily`/VWAP or proxy
- Portfolio config (starting_cash=$5k, equal weight, fees/slippage)
- Existing positions and eligible_sell_date

## Outputs
- `paper_orders`, `paper_fills`, `paper_positions`, `paper_equity_curve`
- Portfolio metrics and warnings
- `pipeline_runs` entry for stage=paper_broker

## Tools/Scripts (links to execution scripts)
- [[20_EXECUTION/paper_trade]]

## Edge cases
- No trading day (holiday) or missing prices/VWAP proxy
- Positions not yet sell-eligible (min-hold constraint)
- Cash shortfalls; adjust orders to respect capital and costs
- Rounding/lot size issues; log adjustments

## Run steps
1. Load predictions and current positions; filter sell-eligible holdings.
2. Keep non-eligible holdings; queue sells for eligible holdings not in Top 10.
3. Allocate remaining weight to Top 10; generate buy/sell orders with fees/slippage.
4. Apply VWAP or proxy fills; update positions, equity, and drawdown metrics.
5. Persist orders/fills/positions/equity; log run stats and warnings.

## Learnings / Updates
- 
