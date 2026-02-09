# Signal Foundry — Cron Schedule

## Overview

The Signal Foundry pipeline runs on a fixed schedule for each market, aligned with exchange open/close times. All schedules use `exchange-calendars` to skip weekends and holidays automatically.

## Schedule

### US Market (NYSE: XNYS)

| Run | Time | Timezone | Cron Expression | Description |
|-----|------|----------|-----------------|-------------|
| Pre-open | 08:15 | America/New_York (ET) | `15 8 * * 1-5` | Morning predictions before market open (9:30 ET) |
| Post-close | 16:45 | America/New_York (ET) | `45 16 * * 1-5` | Full pipeline after close (16:00 ET) |

### ASX Market (ASX: XASX)

| Run | Time | Timezone | Cron Expression | Description |
|-----|------|----------|-----------------|-------------|
| Pre-open | 09:30 | Australia/Sydney (AEST/AEDT) | `30 9 * * 1-5` | Morning predictions before market open (10:00 AEST) |
| Post-close | 16:30 | Australia/Sydney (AEST/AEDT) | `30 16 * * 1-5` | Full pipeline after close (16:00 AEST) |

## Cron Commands

```bash
# US Pre-open (08:15 ET = 13:15 UTC during EST, 12:15 UTC during EDT)
# Using TZ= prefix for timezone-aware cron
TZ=America/New_York
15 8 * * 1-5  /srv/signalsmith/SignalSmith-US/.venv/bin/python -u /srv/signalsmith/SignalSmith-US/execution/foundry/foundry_run.py --market US --mode pre --feature-set v1

# US Post-close (16:45 ET)
TZ=America/New_York
45 16 * * 1-5  /srv/signalsmith/SignalSmith-US/.venv/bin/python -u /srv/signalsmith/SignalSmith-US/execution/foundry/foundry_run.py --market US --mode post --feature-set v1

# ASX Pre-open (09:30 AEST)
TZ=Australia/Sydney
30 9 * * 1-5  /srv/signalsmith/SignalSmith-US/.venv/bin/python -u /srv/signalsmith/SignalSmith-US/execution/foundry/foundry_run.py --market ASX --mode pre --feature-set v1

# ASX Post-close (16:30 AEST)
TZ=Australia/Sydney
30 16 * * 1-5  /srv/signalsmith/SignalSmith-US/.venv/bin/python -u /srv/signalsmith/SignalSmith-US/execution/foundry/foundry_run.py --market ASX --mode post --feature-set v1
```

## Notes

### Timezone Handling
- US schedule uses `America/New_York` which automatically handles EST/EDT transitions.
- ASX schedule uses `Australia/Sydney` which handles AEST/AEDT transitions.
- The orchestrator checks `exchange-calendars` at runtime, so cron firing on a holiday will be handled gracefully (logged as `skipped`).

### Holiday Handling
- Cron fires Mon–Fri regardless of holidays.
- The orchestrator's `is_trading_day()` check handles:
  - Market holidays (e.g., Independence Day, ANZAC Day)
  - Early close days
  - Unexpected exchange closures
- When a holiday is detected, the run is logged as `skipped` in Supabase and a brief Telegram notification is sent.

### DST Transitions
- **US**: EDT (UTC-4) from March–November; EST (UTC-5) from November–March.
- **ASX**: AEDT (UTC+11) from October–April; AEST (UTC+10) from April–October.
- Using `TZ=` in cron ensures correct local time regardless of DST.

### Server Timezone
- Server runs on `Australia/Brisbane` (UTC+10, no DST).
- If using system cron without TZ= prefix, convert times manually:
  - US pre-open 08:15 ET = 23:15 AEST (EST) or 22:15 AEST (EDT)
  - US post-close 16:45 ET = 07:45+1 AEST (EST) or 06:45+1 AEST (EDT)
  - ASX times are straightforward (same timezone family).

### OpenClaw Integration
- These cron jobs can be managed via OpenClaw's scheduler once available.
- For now, manual crontab or systemd timers are recommended.
- The orchestrator is designed to be called by any scheduler — it's a standalone CLI.

## Monitoring
- Each run logs to Supabase `pipeline_runs` with stage, status, and timing.
- Telegram notifications sent on completion, skip, or error.
- Check recent runs: query `pipeline_runs` where `stage LIKE 'foundry_%'` ordered by `created_at DESC`.
