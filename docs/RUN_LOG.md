# SignalSmith — Run Log (append-only)

Purpose: durable, compact record of scheduled runs (including successful ones) so the system compounds.

Format:
- Timestamp (UTC)
- Job
- Status
- Key metrics

---
- 2026-02-04T13:49:51+00:00 | ingest_rss | ok | feeds=10 urls=1 failures=0 rc=0
