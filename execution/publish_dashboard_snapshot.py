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
import html
import json
import os
import re
from pathlib import Path
from typing import Any, Dict, List, Optional, Tuple

import requests
from dotenv import load_dotenv

REPO = Path(__file__).resolve().parents[1]
OUT_DIR = Path(os.getenv("DASHBOARD_OUT_DIR", str(REPO / "docs")))
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
    """Best-effort next-run times.

    We present next-run timestamps in both UTC and AEST for convenience.
    """

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

    # Hard-coded from our cron schedule:
    # - RSS ingest at minute 5 UTC
    # - approval sweep every 30m
    # - swing pre 08:30 ET; post 16:45 ET
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


def render_html(payload: Dict[str, Any]) -> str:
    # Self-contained HTML snapshot with lightweight styling.
    js = json.dumps(payload, indent=2, ensure_ascii=True)
    positions = payload.get("positions") or []
    leads = payload.get("leads") or []

    def esc(value: Any) -> str:
        return html.escape("" if value is None else str(value))

    def render_kv(data: Dict[str, Any]) -> str:
        if not data:
            return '<div class="empty">No data available.</div>'
        rows = "".join(
            [f"<div class=\"kv-row\"><span>{esc(k)}</span><span>{esc(v)}</span></div>" for k, v in data.items()]
        )
        return f"<div class=\"kv\">{rows}</div>"

    def render_bullets(text: str) -> str:
        lines = [line.strip() for line in (text or "").splitlines() if line.strip()]
        if not lines:
            return '<div class="empty">No notes.</div>'
        items = "".join([f"<li>{esc(line)}</li>" for line in lines])
        return f"<ul class=\"bullets\">{items}</ul>"

    def render_positions(rows: List[Dict[str, Any]]) -> str:
        if not rows:
            return '<tr><td class="empty-cell" colspan="5">No positions.</td></tr>'
        return "".join(
            [
                "<tr>"
                f"<td>{esc(p.get('ticker',''))}</td>"
                f"<td>{esc(p.get('qty',''))}</td>"
                f"<td>{esc(p.get('avg_cost',''))}</td>"
                f"<td>{esc(p.get('market_value',''))}</td>"
                f"<td>{esc(p.get('entry_date',''))}</td>"
                "</tr>"
                for p in rows
            ]
        )

    def render_leads(rows: List[Dict[str, Any]]) -> str:
        if not rows:
            return '<div class="empty">No leads.</div>'
        cards = []
        for lead in rows:
            title = lead.get("title") or "Lead template"
            cards.append(
                "<article class=\"lead-card\">"
                f"<h3>{esc(title)}</h3>"
                f"{render_bullets(lead.get('bullets',''))}"
                "</article>"
            )
        return "".join(cards)

    return f"""<!doctype html>
<html lang="en">
<head>
  <meta charset="utf-8"/>
  <meta name="viewport" content="width=device-width, initial-scale=1"/>
  <title>SignalSmith Dashboard</title>
  <style>
    @import url('https://fonts.googleapis.com/css2?family=Fraunces:wght@600;700&family=Space+Grotesk:wght@400;500;600&display=swap');
    :root {{
      --bg: #f6f1ea;
      --bg-2: #eef3ee;
      --ink: #161616;
      --muted: #5f646b;
      --card: #ffffff;
      --stroke: #e5ddd2;
      --accent: #0f6b5c;
      --accent-2: #d59553;
      --shadow: 0 18px 40px rgba(20, 24, 28, 0.12);
    }}
    * {{ box-sizing: border-box; }}
    body {{
      margin: 0;
      color: var(--ink);
      font-family: 'Space Grotesk', 'Segoe UI', system-ui, sans-serif;
      background:
        radial-gradient(1200px circle at 10% 0%, #fff4e2 0, var(--bg) 45%, var(--bg-2) 100%),
        repeating-linear-gradient(135deg, rgba(15, 107, 92, 0.03), rgba(15, 107, 92, 0.03) 2px, transparent 2px, transparent 6px);
      min-height: 100vh;
    }}
    main {{ max-width: 1120px; margin: 0 auto; padding: 36px 24px 64px; }}
    .hero {{ display: flex; justify-content: space-between; align-items: flex-end; gap: 24px; flex-wrap: wrap; }}
    .eyebrow {{ text-transform: uppercase; letter-spacing: 0.28em; font-size: 12px; color: var(--muted); }}
    h1 {{ font-family: 'Fraunces', serif; font-size: 40px; margin: 8px 0 6px; }}
    .subtitle {{ color: var(--muted); margin: 0; font-size: 15px; }}
    .pill {{
      background: var(--card);
      border: 1px solid var(--stroke);
      border-radius: 999px;
      padding: 10px 16px;
      display: inline-flex;
      flex-direction: column;
      gap: 2px;
      box-shadow: var(--shadow);
    }}
    .pill-label {{ font-size: 11px; letter-spacing: 0.16em; text-transform: uppercase; color: var(--muted); }}
    .pill-value {{ font-size: 14px; font-weight: 600; color: var(--ink); }}
    .divider {{ height: 1px; background: var(--stroke); margin: 20px 0 24px; }}
    .grid {{ display: grid; gap: 18px; }}
    .grid.two {{ grid-template-columns: repeat(auto-fit, minmax(280px, 1fr)); }}
    .panel {{
      background: var(--card);
      border: 1px solid var(--stroke);
      border-radius: 18px;
      padding: 18px 20px;
      box-shadow: var(--shadow);
      position: relative;
      overflow: hidden;
      animation: fade-up 0.6s ease both;
      animation-delay: var(--delay, 0ms);
    }}
    .panel::after {{
      content: "";
      position: absolute;
      top: 0;
      left: 0;
      width: 100%;
      height: 4px;
      background: linear-gradient(90deg, var(--accent), var(--accent-2));
      opacity: 0.8;
    }}
    .panel-header {{ display: flex; align-items: center; justify-content: space-between; gap: 12px; margin-bottom: 12px; }}
    h2 {{ margin: 0; font-size: 18px; }}
    h3 {{ margin: 0 0 10px 0; font-size: 16px; }}
    .tag {{ background: #f1ede7; color: var(--muted); border-radius: 999px; padding: 4px 10px; font-size: 12px; font-weight: 600; }}
    .kv {{ display: grid; gap: 8px; }}
    .kv-row {{
      display: flex;
      justify-content: space-between;
      gap: 12px;
      padding: 8px 10px;
      border-radius: 10px;
      background: #faf6f0;
      border: 1px solid #efe6db;
      font-size: 13px;
    }}
    .kv-row span:first-child {{ color: var(--muted); font-weight: 600; }}
    .kv-row span:last-child {{ text-align: right; font-weight: 600; }}
    .table-wrap {{ overflow-x: auto; }}
    table {{ width: 100%; border-collapse: collapse; font-size: 14px; }}
    th {{
      text-align: left;
      font-size: 11px;
      letter-spacing: 0.14em;
      text-transform: uppercase;
      color: var(--muted);
      padding: 8px 10px;
      border-bottom: 1px solid var(--stroke);
    }}
    td {{ padding: 10px; border-bottom: 1px solid #f0e6db; }}
    tr:nth-child(even) td {{ background: #fbf8f3; }}
    .empty {{ border: 1px dashed #e6dbcf; border-radius: 12px; padding: 12px; color: var(--muted); background: #faf6f0; font-size: 13px; }}
    .empty-cell {{ text-align: center; color: var(--muted); padding: 16px; }}
    .leads-grid {{ display: grid; gap: 14px; grid-template-columns: repeat(auto-fit, minmax(240px, 1fr)); }}
    .lead-card {{
      border: 1px solid #eadfd2;
      border-radius: 14px;
      padding: 14px;
      background: linear-gradient(140deg, #fff8ef, #fefcf9);
      box-shadow: 0 12px 24px rgba(22, 25, 28, 0.08);
    }}
    .bullets {{ margin: 0; padding-left: 18px; color: var(--muted); }}
    .bullets li {{ margin-bottom: 6px; }}
    .code-block {{ margin-top: 10px; }}
    details summary {{ cursor: pointer; font-weight: 600; color: var(--accent); }}
    pre {{
      margin: 12px 0 0;
      padding: 12px;
      border-radius: 12px;
      background: #f7f2eb;
      border: 1px solid #e6dbcf;
      overflow: auto;
      font-size: 12px;
      font-family: ui-monospace, SFMono-Regular, Menlo, Consolas, "Liberation Mono", monospace;
    }}
    @keyframes fade-up {{ from {{ opacity: 0; transform: translateY(8px); }} to {{ opacity: 1; transform: translateY(0); }} }}
    @media (max-width: 720px) {{
      h1 {{ font-size: 30px; }}
      .pill {{ width: 100%; }}
    }}
    @media (prefers-reduced-motion: reduce) {{
      .panel {{ animation: none; }}
    }}
  </style>
</head>
<body>
  <main>
    <header class="hero">
      <div>
        <div class="eyebrow">SignalSmith</div>
        <h1>Public Dashboard</h1>
        <p class="subtitle">Execution, portfolio, and pipeline snapshot.</p>
        <p class="subtitle">Chat: message me on Telegram (this page is static).</p>
      </div>
      <div class="pill">
        <span class="pill-label">Updated (AEST)</span>
        <span class="pill-value">{esc(payload.get('generated_at_aest',''))}</span>
        <div class="muted" style="margin-top:6px; font-size:12px;">UTC: {esc(payload.get('generated_at_utc',''))}</div>
      </div>
    </header>

    <div class="divider"></div>

    <section class="grid two">
      <article class="panel" style="--delay: 60ms;">
        <div class="panel-header">
          <h2>Next runs</h2>
        </div>
        {render_kv(payload.get('next_runs', {}))}
      </article>

      <article class="panel" style="--delay: 120ms;">
        <div class="panel-header">
          <h2>Equity (swing)</h2>
        </div>
        {render_kv(payload.get('equity') or {})}
      </article>
    </section>

    <section class="panel" style="--delay: 180ms;">
      <div class="panel-header">
        <h2>Positions (swing)</h2>
        <span class="tag">{len(positions)} open</span>
      </div>
      <div class="table-wrap">
        <table>
          <thead>
            <tr>
              <th>Ticker</th>
              <th>Qty</th>
              <th>Avg cost</th>
              <th>Market value</th>
              <th>Entry date</th>
            </tr>
          </thead>
          <tbody>
            {render_positions(positions)}
          </tbody>
        </table>
      </div>
    </section>

    <section class="panel" style="--delay: 240ms;">
      <div class="panel-header">
        <h2>Leads</h2>
        <span class="tag">{len(leads)} items</span>
      </div>
      <div class="leads-grid">
        {render_leads(leads)}
      </div>
    </section>

    <section class="panel" style="--delay: 300ms;">
      <div class="panel-header">
        <h2>Raw snapshot</h2>
        <span class="tag">dashboard.json</span>
      </div>
      <details class="code-block">
        <summary>View JSON</summary>
        <pre>{js}</pre>
      </details>
    </section>
  </main>
</body>
</html>"""


def main() -> None:
    load_env()
    OUT_DIR.mkdir(parents=True, exist_ok=True)

    now = dt.datetime.now(dt.timezone.utc)

    # Show times in AEST/AEDT (Australia/Brisbane) for Jordan.
    try:
        from zoneinfo import ZoneInfo

        aest = ZoneInfo("Australia/Brisbane")
    except Exception:
        aest = None

    now_aest = now.astimezone(aest) if aest else now

    payload: Dict[str, Any] = {
        "generated_at_utc": now.replace(microsecond=0).isoformat().replace("+00:00", "Z"),
        "generated_at_aest": now_aest.replace(microsecond=0).isoformat(),
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
