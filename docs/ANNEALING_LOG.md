# SignalSmith — Self-Annealing Log

Purpose: capture failures, root causes, fixes, and validations (per AGENTS.md).

Rules:
- Append-only.
- Each incident: **Symptom**, **Root cause**, **Fix**, **Validation**, **Follow-ups**.

---

## 2026-02-04 — Incident A1: preopen_run hangs after completion
- **Symptom:** `preopen_run.py` completes main work (prices upserted 100% coverage) but does not exit; process can hang ~1 minute and may require kill.
- **Root cause (suspected):** lingering non-daemon thread / hung IO / background task not terminating cleanly.
- **Fix (pending):** add explicit shutdown/exit path in `preopen_run.py` and/or ensure any background work is daemonized/joined.
- **Validation (pending):** run `./.venv/bin/python execution/preopen_run.py --dry-run` and confirm it exits reliably.
- **Follow-ups:** instrument with timestamps around each stage; add a max-runtime watchdog to prevent future flaps.

---

## 2026-02-05T20:09:15+00:00
- Context: RSS ingest hung on IPv6 SYN-SENT connect; no output for ~1m+
- Change: requests.get timeout now uses (connect, read) tuple: (min(5,t), t) in execution/ingest_rss.py
- Validation: reran ingest_rss (max-items 80) -> exit code 0

---

## 2026-02-07T01:10:47+00:00 — Incident A2: ingest_docs crashes when Supabase env missing
- **Symptom:** `execution/ingest_rss.py` discovers URLs but `execution/ingest_docs.py` aborts with `RuntimeError: SUPABASE_URL not set`.
- **Root cause:** repo has no `.env` in this runtime, so Supabase credentials are unavailable; `ingest_docs.py` attempted remote dedupe/insert anyway.
- **Fix:** added a `supabase_enabled()` guard and a local JSONL fallback writer (`data/ingest_docs/<date>/<run_id>.jsonl`) so the job completes without Supabase.
- **Validation:** ran `./.venv/bin/python -u execution/ingest_rss.py --max-items 3` → wrote local JSONL + exited cleanly.
- **Follow-ups:** restore Supabase env in cron/runtime (so remote storage + dedupe works again); consider making missing Supabase a hard alert in ops status.

---

## 2026-02-07T01:31:13+00:00 — Incident A3: approval timeout sweep fails when Supabase env missing
- **Symptom:** `execution/approval_timeout.py` crashed with `RuntimeError: SUPABASE_URL not set`.
- **Root cause:** Supabase credentials are not present in this runtime (no `.env`, and cron environment didn’t provide `SUPABASE_URL` / `SUPABASE_SERVICE_ROLE`).
- **Fix:** added `supabase_enabled()` guard so the sweep skips cleanly when Supabase isn’t configured (noise-control; avoids cron flaps).
- **Validation:** ran `./.venv/bin/python execution/approval_timeout.py --timeout-minutes 15 --notify-telegram` → prints skip message, exits 0.
- **Follow-ups:** restore Supabase env in cron/runtime so the sweep can actually enforce timeouts.
