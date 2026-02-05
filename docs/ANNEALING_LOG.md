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
