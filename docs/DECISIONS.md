# SignalSmith — Decisions Log

Purpose: keep durable, human-readable decisions so the system compounds.

Rules:
- Append-only.
- Date-stamped.
- Each entry: **Decision**, **Why**, **Impact**, **Next**.

---

## 2026-02-04

### D1 — Notifications as an exception dashboard (Mode 3)
- **Decision:** Do all background work, but only notify on important items (errors, trades, red flags, and meaningful news spikes).
- **Why:** Keep Telegram readable while still staying "alive".
- **Impact:** Cron/system messages should mostly collapse to `HEARTBEAT_OK`; formatted bot messages carry the actual signal.
- **Next:** Tighten remaining jobs that still emit verbose cron summaries.

### D2 — Add risk metadata + time-stops to swing book
- **Decision:** Encode ATR stops, risk-based sizing metadata, and time-stop exits in `swing_book.py` and persist in `rules_json`.
- **Why:** Turn discretionary risk doctrine into testable automation.
- **Impact:** Orders/positions include entry/stop/ATR/risk parameters; dead-money exits are enforced.
- **Next:** Add optional “add to winners” tranche behind strict conditions.

---
