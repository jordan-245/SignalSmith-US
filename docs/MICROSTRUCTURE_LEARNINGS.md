# Microstructure learnings → SignalSmith system changes

Source: `resources/notes/The Professional Trader’s Microstructure Manual A Practical Framework for Execution and Portfolio Management.md`

## Principles to apply (in plain English)
- **Execution is part of the edge**: selection alpha can be erased by bad fills.
- **Liquidity is a service**: taking liquidity costs spread/impact; providing liquidity can earn premium but risks non-execution.
- **Adverse selection is real**: if you get filled instantly in a thin name, assume the other side may know more.
- **Implementation Shortfall** should be the core execution metric.

## Concrete changes we should implement (deterministic)
1) **Journal execution quality** per trade:
   - decision time price (benchmark)
   - fill price
   - implementation shortfall = sign * (fill - benchmark)
   - realized slippage vs spread proxy

2) **Order-type policy in swing_book**
   - prefer **limit/"offer liquidity"** when spreads are wide (microcaps / premarket / illiquid)
   - use **market/VWAP** only when speed is worth the cost (breakouts, news urgency)

3) **Liquidity filters**
   - incorporate **dollar volume** guardrail (price * avg volume)
   - downsize or skip when liquidity is insufficient

4) **Post-fill logic**
   - treat "too easy" fills in thin names as a risk flag (adverse selection)

## What’s already done
- Trade journal exists: `docs/TRADE_JOURNAL.md` + `execution/trade_journal_update.py`.
- Swing sizing updated to risk-at-stop model with baseline 5% equity-at-risk.

## Next steps (needs your approval before trading changes)
- Add decision-price benchmark capture in swing_book (e.g., close or VWAP proxy) to compute implementation shortfall.
- Add dollar-volume based position cap and/or skip logic.
