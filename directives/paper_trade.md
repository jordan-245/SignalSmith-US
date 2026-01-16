---
layer: directive
tags: [layer/directive]
---

# paper_trade

## Purpose
Turn predictions into paper trades with VWAP fills and 5-day min-hold.

## Inputs
- Top 10 `predictions`
- `prices_daily`/VWAP proxy
- Portfolio config + positions

## Outputs
- `paper_orders`, `paper_fills`, `paper_positions`, `paper_equity_curve`
- Portfolio metrics + run log

## Tools/Scripts (links to execution scripts)
- [[20_EXECUTION/paper_trade]]

## Edge cases
- Holiday/missing prices/VWAP proxy
- Not sell-eligible (min-hold)
- Cash/rounding issues; adjust and log

## Run steps
1. Load predictions + positions; split sell-eligible.
2. Keep non-eligible; queue sells for eligible not in Top 10.
3. Allocate to Top 10; generate orders with fees/slippage.
4. Apply VWAP/proxy fills; update positions/equity; log stats.

## Learnings / Updates
- 
