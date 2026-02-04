# Catalyst Research (Yahoo Calendar) — SOP

Goal: use day-of events (Yahoo calendar) to trigger **structured, bounded** research and (optionally) small paper allocations.

## Principles
- **Do not predict earnings.**
- Pre-earnings: avoid rule stays on.
- Post-earnings: only allocate if evidence suggests news is good **and** price action confirms.
- Always cap risk and exposure.

## Current implementation (v0)
Implemented in `execution/swing_book.py`:
- **Pre-open:** earnings avoid window (next N sessions)
- **Post-close:** for names with earnings “today”:
  - pull recent `docs_text` mentioning ticker
  - block if negative flags; allow if positive keywords
  - allocate with caps: 2% equity/name, 10% total

## Next iteration (recommended)
Replace/augment keyword heuristic with:
1) price reaction checks (gap, volume, close strength)
2) explicit stop/risk metadata (ATR-based)
3) record catalysts + reasons into a dedicated table (optional)
