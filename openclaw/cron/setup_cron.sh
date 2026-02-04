#!/usr/bin/env bash
set -euo pipefail

# Adds SignalSmith cron jobs to OpenClaw.
# NOTE: Re-running this script will create duplicates. Use `openclaw cron list`
# and remove existing jobs if needed before re-running.

DELIVER_ARGS=(--deliver --channel telegram)
if [[ -n "${TELEGRAM_TO:-}" ]]; then
  DELIVER_ARGS+=(--to "$TELEGRAM_TO")
fi

# Pre-open full run (ET) - handles DST automatically.
openclaw cron add \
  --name "SignalSmith pre-open run" \
  --cron "45 8 * * 1-5" \
  --tz "America/New_York" \
  --session isolated \
  --message "Run pre-open pipeline: python execution/preopen_run.py. Skip if market closed." \
  "${DELIVER_ARGS[@]}"

# Post-close report (ET).
openclaw cron add \
  --name "SignalSmith post-close report" \
  --cron "30 16 * * 1-5" \
  --tz "America/New_York" \
  --session isolated \
  --message "Run EOD report: python execution/eod_report.py --notify-telegram." \
  "${DELIVER_ARGS[@]}"

# Approval timeout sweep (UTC).
openclaw cron add \
  --name "SignalSmith approval timeout sweep" \
  --cron "*/5 * * * *" \
  --tz "UTC" \
  --session isolated \
  --message "Run approval timeout sweep: execution/approval_timeout.py --timeout-minutes 15 --notify-telegram"

# Optional after-hours digest (ET). Enable with ENABLE_AFTER_HOURS=1.
if [[ "${ENABLE_AFTER_HOURS:-0}" == "1" ]]; then
  openclaw cron add \
    --name "SignalSmith after-hours digest" \
    --cron "30 19 * * 1-5" \
    --tz "America/New_York" \
    --session isolated \
    --message "Run after-hours digest: notable news + late filings + price moves." \
    "${DELIVER_ARGS[@]}"
fi

# Optional weekly maintenance (AEST). Enable with ENABLE_WEEKLY_MAINTENANCE=1.
if [[ "${ENABLE_WEEKLY_MAINTENANCE:-0}" == "1" ]]; then
  openclaw cron add \
    --name "SignalSmith weekly maintenance" \
    --cron "0 10 * * 6" \
    --tz "Australia/Brisbane" \
    --session isolated \
    --message "Run weekly maintenance: data cleanup, backfill gaps, model eval." \
    "${DELIVER_ARGS[@]}"
fi
