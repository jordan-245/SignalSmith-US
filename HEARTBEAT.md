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
