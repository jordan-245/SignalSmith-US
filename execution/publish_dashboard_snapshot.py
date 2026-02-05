"""Publish a public-safe dashboard snapshot (deterministic).

Goal: create a *publicly shareable* snapshot without exposing secrets.

Writes:
- docs/public/dashboard.json
- docs/public/index.html

Snapshot includes:
- latest equity/cash for swing portfolio
- current positions
- top leads (from docs/LEAD_BOOK.md)
- next scheduled run times (best-effort: parse from docs/RUN_LOG.md cadence + known cron schedule text)

Intended hosting:
- GitHub Pages from /docs/public (or /docs)

Usage:
  python execution/publish_dashboard_snapshot.py

NOTE: Uses SUPABASE_SERVICE_ROLE locally to generate the snapshot, but outputs contain no keys.
"""

from __future__ import annotations

import datetime as dt
import json
import os
import re
from pathlib import Path
from typing import Any, Dict, List, Optional, Tuple

import requests
from dotenv import load_dotenv

REPO = Path(__file__).resolve().parents[1]
OUT_DIR = REPO / "docs"
LEAD_BOOK = REPO / "docs" / "LEAD_BOOK.md"
RUN_LOG = REPO / "docs" / "RUN_LOG.md"


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


def parse_leads(md: str) -> List[Dict[str, str]]:
    leads: List[Dict[str, str]] = []
    cur: Dict[str, str] = {}
    for line in md.splitlines():
        if line.startswith("### "):
            if cur:
                leads.append(cur)
            cur = {"title": line.replace("### ", "").strip()}
        elif line.startswith("- ") and cur is not None:
            cur.setdefault("bullets", "")
            cur["bullets"] += line[2:].strip() + "\n"
    if cur:
        leads.append(cur)
    return leads[:10]


def next_runs_hint(now_utc: dt.datetime) -> Dict[str, str]:
    # Hard-coded from our cron schedule:
    # - RSS ingest at minute 5 UTC
    # - approval sweep every 30m
    # - swing pre 08:30 ET; post 16:45 ET
    def next_at_minute(minute: int) -> dt.datetime:
        t = now_utc.replace(second=0, microsecond=0)
        cand = t.replace(minute=minute)
        if cand <= t:
            cand = cand + dt.timedelta(hours=1)
            cand = cand.replace(minute=minute)
        return cand

    def next_half_hour() -> dt.datetime:
        t = now_utc.replace(second=0, microsecond=0)
        m = 30 if t.minute < 30 else 0
        cand = t.replace(minute=m)
        if cand <= t:
            cand = cand + dt.timedelta(minutes=30)
        return cand

    return {
        "rss_ingest_next_utc": next_at_minute(5).isoformat().replace("+00:00", "Z"),
        "approval_sweep_next_utc": next_half_hour().isoformat().replace("+00:00", "Z"),
        "swing_preopen_time": "08:30 America/New_York",
        "swing_postclose_time": "16:45 America/New_York",
    }


def render_html(payload: Dict[str, Any]) -> str:
    # Minimal self-contained HTML.
    js = json.dumps(payload, indent=2)
    return f"""<!doctype html>
<html>
<head>
  <meta charset=\"utf-8\"/>
  <meta name=\"viewport\" content=\"width=device-width, initial-scale=1\"/>
  <title>SignalSmith Dashboard</title>
  <style>
    body {{ font-family: ui-sans-serif, system-ui, -apple-system, Segoe UI, Roboto, Arial; margin: 24px; max-width: 980px; }}
    h1 {{ margin: 0 0 6px 0; }}
    .muted {{ color: #666; }}
    .card {{ border: 1px solid #ddd; border-radius: 10px; padding: 14px 16px; margin: 14px 0; }}
    code, pre {{ background: #f6f6f6; padding: 2px 6px; border-radius: 6px; }}
    table {{ border-collapse: collapse; width: 100%; }}
    th, td {{ border-bottom: 1px solid #eee; text-align: left; padding: 6px 8px; font-size: 14px; }}
  </style>
</head>
<body>
  <h1>SignalSmith — Public Dashboard</h1>
  <div class=\"muted\">Updated (UTC): {payload.get('generated_at_utc','')}</div>

  <div class=\"card\">
    <h2>Next runs</h2>
    <pre>{json.dumps(payload.get('next_runs',{}), indent=2)}</pre>
  </div>

  <div class=\"card\">
    <h2>Equity (swing)</h2>
    <pre>{json.dumps(payload.get('equity',{}), indent=2)}</pre>
  </div>

  <div class=\"card\">
    <h2>Positions (swing)</h2>
    <table>
      <thead><tr><th>Ticker</th><th>Qty</th><th>Avg cost</th><th>Market value</th><th>Entry date</th></tr></thead>
      <tbody>
        {''.join([f"<tr><td>{p.get('ticker','')}</td><td>{p.get('qty','')}</td><td>{p.get('avg_cost','')}</td><td>{p.get('market_value','')}</td><td>{p.get('entry_date','')}</td></tr>" for p in payload.get('positions',[])])}
      </tbody>
    </table>
  </div>

  <div class=\"card\">
    <h2>Leads</h2>
    {''.join([f"<h3>{l.get('title','')}</h3><pre>{(l.get('bullets') or '').strip()}</pre>" for l in payload.get('leads',[])])}
  </div>

  <div class=\"card\">
    <h2>Raw snapshot</h2>
    <details><summary>dashboard.json</summary><pre>{js}</pre></details>
  </div>
</body>
</html>"""


def main() -> None:
    load_env()
    OUT_DIR.mkdir(parents=True, exist_ok=True)

    now = dt.datetime.now(dt.timezone.utc)

    payload: Dict[str, Any] = {
        "generated_at_utc": now.replace(microsecond=0).isoformat().replace("+00:00", "Z"),
        "equity": latest_equity("swing"),
        "positions": latest_positions("swing"),
        "leads": parse_leads(LEAD_BOOK.read_text(encoding="utf-8")) if LEAD_BOOK.exists() else [],
        "next_runs": next_runs_hint(now),
    }

    (OUT_DIR / "dashboard.json").write_text(json.dumps(payload, indent=2, default=str) + "\n", encoding="utf-8")
    (OUT_DIR / "index.html").write_text(render_html(payload), encoding="utf-8")

    print(f"[ok] wrote {OUT_DIR/'index.html'} and dashboard.json")


if __name__ == "__main__":
    main()
