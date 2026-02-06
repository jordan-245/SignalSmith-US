"""Send + log a simple premarket review (deterministic).

Goal: once before the US trading day, provide a short "what to watch" note so
Jordan knows what matters today.

Outputs:
- Appends to docs/PREMARKET_REVIEW.md (append-only; one per date)
- Sends a concise Telegram note (same content)

No LLM.
"""

from __future__ import annotations

import argparse
import datetime as dt
import os
import re
from pathlib import Path
from typing import Any, Dict, List, Optional

import pandas as pd
import requests
from dotenv import load_dotenv

REPO = Path(__file__).resolve().parents[1]
OUT_PATH = REPO / "docs" / "PREMARKET_REVIEW.md"
MARKET_NOTES = REPO / "docs" / "MARKET_NOTES.md"
LEAD_PIPELINE = REPO / "docs" / "LEAD_PIPELINE.md"


def load_env() -> None:
    p = REPO / ".env"
    if p.exists():
        load_dotenv(p)


def sb_base() -> str:
    base = os.getenv("SUPABASE_URL", "").rstrip("/")
    if not base:
        raise RuntimeError("SUPABASE_URL not set")
    return base


def sb_headers() -> Dict[str, str]:
    key = os.getenv("SUPABASE_SERVICE_ROLE", "")
    if not key:
        raise RuntimeError("SUPABASE_SERVICE_ROLE not set")
    return {"apikey": key, "Authorization": f"Bearer {key}"}


def send_telegram(text: str) -> None:
    from telegram_fmt import send_telegram as _send

    _send(text, timeout=15)


def market_is_open(date_str: str) -> bool:
    try:
        import exchange_calendars as xcals  # type: ignore

        cal = xcals.get_calendar("XNYS")
        return bool(cal.is_session(date_str))
    except Exception:
        d = dt.date.fromisoformat(date_str)
        return d.weekday() < 5


def parse_lead_pipeline(md: str) -> Dict[str, int]:
    out = {"TODO": 0, "IN_PROGRESS": 0, "READY": 0, "ARCHIVED": 0}
    cur = None
    for line in (md or "").splitlines():
        m = re.match(r"^##\s+(TODO|IN_PROGRESS|READY|ARCHIVED)\s*$", line.strip())
        if m:
            cur = m.group(1)
            continue
        if cur and line.startswith("- "):
            out[cur] += 1
    return out


def last_market_note() -> str:
    if not MARKET_NOTES.exists():
        return "(no market notes yet)"
    txt = MARKET_NOTES.read_text(encoding="utf-8")
    # grab last section starting with "## YYYY-"
    parts = re.split(r"\n(?=##\s+\d{4}-\d{2}-\d{2})", txt)
    parts = [p.strip() for p in parts if p.strip().startswith("## ")]
    if not parts:
        return "(no market notes entries yet)"
    return parts[-1]


def latest_positions(portfolio_id: str = "swing") -> List[Dict[str, Any]]:
    base = sb_base()
    url = f"{base}/rest/v1/paper_positions"

    # find latest date
    r = requests.get(
        url,
        headers=sb_headers(),
        params=[("select", "date"), ("portfolio_id", f"eq.{portfolio_id}"), ("order", "date.desc"), ("limit", "1")],
        timeout=20,
    )
    if r.status_code >= 300:
        return []
    rows = r.json() or []
    if not rows:
        return []
    last_date = rows[0]["date"]

    r2 = requests.get(
        url,
        headers=sb_headers(),
        params=[
            ("select", "ticker,qty,market_value,entry_date,eligible_sell_date"),
            ("portfolio_id", f"eq.{portfolio_id}"),
            ("date", f"eq.{last_date}"),
            ("order", "market_value.desc"),
        ],
        timeout=20,
    )
    if r2.status_code >= 300:
        return []
    return r2.json() or []


def format_positions(pos: List[Dict[str, Any]], maxn: int = 10) -> str:
    if not pos:
        return "(none)"
    ticks = [p.get("ticker") for p in pos if float(p.get("qty") or 0) > 0]
    ticks = [t for t in ticks if t]
    return ", ".join(ticks[:maxn]) + ("…" if len(ticks) > maxn else "")


def append_once(day: dt.date, text: str) -> None:
    OUT_PATH.parent.mkdir(parents=True, exist_ok=True)
    if not OUT_PATH.exists():
        OUT_PATH.write_text("# SignalSmith — Premarket Review (append-only)\n\n---\n", encoding="utf-8")

    header = f"## {day.isoformat()}"
    existing = OUT_PATH.read_text(encoding="utf-8")
    if header in existing:
        print("HEARTBEAT_OK")
        return

    blob = f"\n{header}\n" + text.strip() + "\n"
    with OUT_PATH.open("a", encoding="utf-8") as fp:
        fp.write(blob)


def main() -> None:
    load_env()

    ap = argparse.ArgumentParser()
    ap.add_argument("--day", default=dt.date.today().isoformat())
    args = ap.parse_args()
    day = dt.date.fromisoformat(args.day)

    if not market_is_open(day.isoformat()):
        print("HEARTBEAT_OK")
        return

    pos = latest_positions("swing")
    pos_line = format_positions(pos)

    lp_md = LEAD_PIPELINE.read_text(encoding="utf-8") if LEAD_PIPELINE.exists() else ""
    lp = parse_lead_pipeline(lp_md)

    note = last_market_note()

    # Short message (Telegram-friendly)
    now_utc = dt.datetime.now(dt.timezone.utc).replace(microsecond=0).isoformat().replace("+00:00", "Z")
    lines: List[str] = []
    lines.append(f"Premarket — {day.isoformat()}")
    lines.append("")
    lines.append(f"- Swing positions: {pos_line}")
    lines.append(f"- Lead pipeline: TODO {lp['TODO']} | INPROG {lp['IN_PROGRESS']} | READY {lp['READY']} | ARCH {lp['ARCHIVED']}")
    lines.append("")
    lines.append("- Backdrop (latest market note):")
    # keep only a few lines
    note_lines = [l for l in note.splitlines() if l.strip()][:8]
    for l in note_lines:
        lines.append(f"  {l}")

    text = "\n".join(lines)

    # Append to notes and send
    append_once(day, f"- Generated: {now_utc}\n\n" + "\n".join([f"- {l[2:]}" if l.startswith("- ") else l for l in lines[2:]]))
    send_telegram(text)


if __name__ == "__main__":
    main()
