"""Append-only journaling for compounding context.

This module writes *small* durable breadcrumbs to docs/*.md so that even routine
scheduled runs contribute context (without spamming Telegram).

- journal_run(): append to docs/RUN_LOG.md
- journal_watch(): update/append lightweight watch items in docs/OPS_STATUS.md (append-only section)

Intentionally minimal + dependency-free.
"""

from __future__ import annotations

import datetime as dt
from pathlib import Path
from typing import Optional

REPO_ROOT = Path(__file__).resolve().parents[1]
RUN_LOG = REPO_ROOT / "docs" / "RUN_LOG.md"
OPS_STATUS = REPO_ROOT / "docs" / "OPS_STATUS.md"


def _utc_now() -> str:
    return dt.datetime.now(dt.timezone.utc).replace(microsecond=0).isoformat()


def journal_run(job: str, status: str, metrics: str = "") -> None:
    """Append a single compact line to RUN_LOG.md."""
    RUN_LOG.parent.mkdir(parents=True, exist_ok=True)
    ts = _utc_now()
    line = f"- {ts} | {job} | {status}" + (f" | {metrics.strip()}" if metrics.strip() else "") + "\n"
    if not RUN_LOG.exists():
        RUN_LOG.write_text("# SignalSmith — Run Log\n\n---\n", encoding="utf-8")
    with RUN_LOG.open("a", encoding="utf-8") as f:
        f.write(line)


def journal_watch(item: str) -> None:
    """Append a watch item with timestamp to OPS_STATUS.md."""
    OPS_STATUS.parent.mkdir(parents=True, exist_ok=True)
    ts = _utc_now()
    entry = f"- {ts} {item.strip()}\n"

    if not OPS_STATUS.exists():
        OPS_STATUS.write_text("# SignalSmith — Ops Status\n\n## Watch items\n", encoding="utf-8")

    with OPS_STATUS.open("a", encoding="utf-8") as f:
        f.write(entry)
