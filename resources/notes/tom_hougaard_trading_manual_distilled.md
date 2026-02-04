# Tom Hougaard — *The First Trading Manual* (Distilled Notes)

Source PDF: `resources/Tom_Hougaard_The_Trading_Manual_Singles.pdf`

Purpose: extract **implementable** rules/ideas we can encode into SignalSmith (paper-only) without turning this into discretionary “vibes trading”.

## Core principles worth encoding

### 1) Always define risk *before* the trade
Hougaard’s framing is simple: you should be able to answer these before entering:
1. Proposed entry price
2. Proposed stop-loss
3. Risk per point/share
4. Account size
5. % of account risked

**SignalSmith mapping:**
- We already have deterministic entries.
- We should explicitly calculate (and log) per-trade risk and max loss.
- Our current schema doesn’t store native stop orders; we can still enforce *stop logic* as a rule:
  - **initial stop level** stored in `paper_orders.rules_json` (or `paper_positions` if we add a json column later)
  - **stop breach → exit next session** (paper simulation)

### 2) Structure / routine matters
The manual emphasizes a daily routine and a playbook approach.

**SignalSmith mapping:**
- Keep the system procedural:
  - pre-open scan (targets)
  - post-close scan (validation + catalyst research)
  - consistent logging + Telegram summaries

### 3) Demo accounts only for mechanics
Demo accounts are for learning platform mechanics, stop-loss placement, and practicing a technique; beyond that they can create a false sense of confidence.

**SignalSmith mapping:**
- Paper trading is our “mechanical demo”, but we should treat it like real:
  - small caps on new features
  - explicit risk caps
  - audit trail and performance tracking

### 4) Adding to winners can improve expectancy (context-dependent)
There’s discussion that adding to a position at defined profit milestones can materially improve risk/reward (example: doubling after a move, moving stop to entry).

**SignalSmith mapping (later iteration):**
- Add-on rule candidate:
  - If position up > X ATR and trend intact, allow one add-on tranche
  - Move “risk” to breakeven equivalent in simulation
- Not implementing yet until we add stop/risk metadata.

## What we will implement next (suggested)
1) **Risk metadata** in swing book:
   - compute ATR(14) from daily highs/lows
   - initial stop = entry - k*ATR (e.g. k=2)
   - time stop = exit after N sessions if no progress
2) **Position sizing by risk** (instead of equal-weight):
   - size so $risk per name = 0.5%–1.0% equity (configurable)
3) **Log “trade prep”** fields into Telegram summary:
   - entry proxy, stop level, risk dollars, risk %

## Notes / caveats
- The book is discretionary; SignalSmith is automated. We only import rules that are:
  - objective
  - testable
  - bounded by strict risk caps
- Earnings direction prediction remains out of scope; we use **post-event confirmation** and strict sizing.
