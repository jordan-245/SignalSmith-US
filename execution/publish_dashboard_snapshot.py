"""Publish a public-safe dashboard snapshot (deterministic).

Goal: create a *publicly shareable* snapshot without exposing secrets.

Writes:
- <OUT_DIR>/dashboard.json
- <OUT_DIR>/index.html

Snapshot includes:
- latest equity/cash for swing portfolio
- current positions
- lead pipeline (from docs/LEAD_PIPELINE.md)
- next scheduled run times (UTC + AEST)

NOTE: Uses SUPABASE_SERVICE_ROLE locally to generate the snapshot, but outputs contain no keys.
"""

from __future__ import annotations

import datetime as dt
import html
import json
import os
import re
from pathlib import Path
from typing import Any, Dict, List, Optional, Tuple

import requests
from dotenv import load_dotenv

REPO = Path(__file__).resolve().parents[1]
OUT_DIR = Path(os.getenv("DASHBOARD_OUT_DIR", str(Path("/var/www/signalsmith"))))
LEAD_PIPELINE = REPO / "docs" / "LEAD_PIPELINE.md"


def load_env() -> None:
    env_path = REPO / ".env"
    if env_path.exists():
        load_dotenv(env_path)


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


def sb_get(table: str, params: List[Tuple[str, str]], timeout: int = 30) -> List[Dict[str, Any]]:
    url = f"{sb_base()}/rest/v1/{table}"
    r = requests.get(url, headers=sb_headers(), params=params, timeout=timeout)
    r.raise_for_status()
    return r.json() or []


def latest_equity(portfolio_id: str) -> Optional[Dict[str, Any]]:
    rows = sb_get(
        "paper_equity_curve",
        [("select", "date,equity,cash,drawdown,turnover"), ("portfolio_id", f"eq.{portfolio_id}"), ("order", "date.desc"), ("limit", "1")],
    )
    return rows[0] if rows else None


def latest_positions(portfolio_id: str) -> List[Dict[str, Any]]:
    rows = sb_get(
        "paper_positions",
        [("select", "date"), ("portfolio_id", f"eq.{portfolio_id}"), ("order", "date.desc"), ("limit", "1")],
    )
    if not rows:
        return []
    last_date = rows[0]["date"]
    pos = sb_get(
        "paper_positions",
        [
            ("select", "ticker,qty,avg_cost,market_value,entry_date,eligible_sell_date"),
            ("portfolio_id", f"eq.{portfolio_id}"),
            ("date", f"eq.{last_date}"),
            ("order", "market_value.desc"),
        ],
    )
    return pos


def parse_kanban(md: str) -> Dict[str, list[dict]]:
    cols = {"TODO": [], "IN_PROGRESS": [], "READY": [], "ARCHIVED": []}
    cur: str | None = None
    card: dict | None = None

    for line in (md or "").splitlines():
        m = re.match(r"^##\s+(TODO|IN_PROGRESS|READY|ARCHIVED)\s*$", line.strip())
        if m:
            if card and cur:
                cols[cur].append(card)
            cur = m.group(1)
            card = None
            continue
        if not cur:
            continue
        if line.startswith("- "):
            if card:
                cols[cur].append(card)
            card = {"title": line[2:].strip(), "bullets": []}
            continue
        if line.strip().startswith("-") and card is not None:
            card["bullets"].append(line.strip().lstrip("-").strip())

    if card and cur:
        cols[cur].append(card)
    return cols


def next_runs_hint(now_utc: dt.datetime) -> Dict[str, str]:
    try:
        from zoneinfo import ZoneInfo

        aest = ZoneInfo("Australia/Brisbane")
    except Exception:
        aest = None

    def to_utc_z(t: dt.datetime) -> str:
        return t.astimezone(dt.timezone.utc).replace(microsecond=0).isoformat().replace("+00:00", "Z")

    def to_aest(t: dt.datetime) -> str:
        if not aest:
            return ""
        return t.astimezone(aest).replace(microsecond=0).isoformat()

    def next_at_minute(minute: int) -> dt.datetime:
        t = now_utc.astimezone(dt.timezone.utc).replace(second=0, microsecond=0)
        cand = t.replace(minute=minute)
        if cand <= t:
            cand = cand + dt.timedelta(hours=1)
            cand = cand.replace(minute=minute)
        return cand

    def next_half_hour() -> dt.datetime:
        t = now_utc.astimezone(dt.timezone.utc).replace(second=0, microsecond=0)
        m = 30 if t.minute < 30 else 0
        cand = t.replace(minute=m)
        if cand <= t:
            cand = cand + dt.timedelta(minutes=30)
        return cand

    rss_next = next_at_minute(5)
    appr_next = next_half_hour()

    return {
        "rss_ingest_next_aest": to_aest(rss_next),
        "rss_ingest_next_utc": to_utc_z(rss_next),
        "approval_sweep_next_aest": to_aest(appr_next),
        "approval_sweep_next_utc": to_utc_z(appr_next),
        "swing_preopen_time": "08:30 America/New_York",
        "swing_postclose_time": "16:45 America/New_York",
    }


def render_html() -> str:
    # The live UI is served from /var/www/signalsmith/index.html
    # This script still writes index.html for completeness, but the system now uses the file already deployed.
    return (OUT_DIR / "index.html").read_text(encoding="utf-8") if (OUT_DIR / "index.html").exists() else ""


def main() -> None:
    load_env()
    OUT_DIR.mkdir(parents=True, exist_ok=True)

    now = dt.datetime.now(dt.timezone.utc)

    try:
        from zoneinfo import ZoneInfo

        aest = ZoneInfo("Australia/Brisbane")
    except Exception:
        aest = None

    now_aest = now.astimezone(aest) if aest else now

    pipeline_md = LEAD_PIPELINE.read_text(encoding="utf-8") if LEAD_PIPELINE.exists() else ""
    lead_pipeline = parse_kanban(pipeline_md)

    eq = latest_equity("swing")
    # Optional: sector radar (precomputed)
    sector_path = REPO / "output" / "sector_radar.json"
    sector_radar = None
    if sector_path.exists():
        try:
            sector_radar = json.loads(sector_path.read_text(encoding="utf-8"))
        except Exception:
            sector_radar = None

    payload: Dict[str, Any] = {
        "generated_at_utc": now.replace(microsecond=0).isoformat().replace("+00:00", "Z"),
        "generated_at_aest": now_aest.replace(microsecond=0).isoformat(),
        "equity": eq,
        "positions": latest_positions("swing"),
        "next_runs": next_runs_hint(now),
        "lead_pipeline": lead_pipeline,
        "sector_radar": sector_radar,
        "equity_summary": {
            "start_equity": None,
            "current_equity": (eq or {}).get("equity"),
            "max_drawdown": 0.0,
        },
    }

    (OUT_DIR / "dashboard.json").write_text(json.dumps(payload, indent=2, default=str) + "\n", encoding="utf-8")

    # index.html is managed as a static asset in OUT_DIR.
    # Keep it as-is (don’t rewrite) to allow manual styling without touching python.

    print(f"[ok] wrote {OUT_DIR/'dashboard.json'}")


if __name__ == "__main__":
    main()
