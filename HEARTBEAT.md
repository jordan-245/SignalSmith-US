# SignalSmith Heartbeat

Goal: continuous monitoring with minimal noise.

Checklist:
- Scan for new documents and announcements (news, filings, press releases).
- If new docs exist, run `execution/ingest_docs.py` then `execution/llm_extract.py`.
- If market open is within 2 hours (ET), verify pre-open pipeline readiness.
- Review last run logs for errors or data gaps.
- If a failure is detected, start the self-annealing loop:
  - Diagnose root cause.
  - Propose deterministic fix.
  - Implement fix in execution scripts and add tests.
  - Update the relevant directive with approval.
  - Re-run the failed stage in isolation and validate outputs.

Output policy:
- If nothing requires attention, respond with `HEARTBEAT_OK`.
- Otherwise send a brief alert summary (Telegram) with next steps.

---

## Signal Foundry Pipeline

### Checks

1. **Latest Foundry Run Freshness**
   - Look at `data/foundry/predictions/market=US/` for the newest `run_id=*` directory.
   - Extract the date from the run_id (format: `YYYYMMDDHHmmss`).
   - If today is a weekday (Mon–Fri) and the latest prediction data is **> 2 trading days old**, raise an alert:
     `⚠️ Foundry predictions stale — last run: <date>, now: <today>`
   - If no prediction directories exist, alert:
     `⚠️ No Foundry prediction data found`

2. **Disk Usage**
   - Check total size of `data/foundry/` (use `du -sh data/foundry/`).
   - If usage exceeds **500 MB**, alert:
     `⚠️ Foundry data exceeds 500MB — currently <size>. Run foundry_cleanup.py`

3. **Quality Gate Warnings**
   - Read `docs/foundry/US/latest.md`.
   - Scan for lines containing `⚠️` or `WARN` or `FAIL` in the quality gates section.
   - If any quality gate warnings are present, include them in the heartbeat output:
     `⚠️ Quality gate warnings in latest report: <warnings>`

4. **Pipeline Error Logs**
   - If the latest run appears to have errored (no report generated, or `data/foundry/run_log.jsonl` last entry has `"status": "error"`), check `/var/log/foundry/*.log` for recent errors.
   - Summarise any errors found:
     `❌ Foundry pipeline errors detected — check /var/log/foundry/`

5. **Local Run Log**
   - Check `data/foundry/run_log.jsonl` for the most recent entry.
   - If the last entry status is `error`, include it in the alert.

### Actions
- If all checks pass: include `Foundry: OK` in the heartbeat.
- If any check fails: include the specific alerts and suggest next steps (re-run pipeline, run cleanup, investigate logs).
