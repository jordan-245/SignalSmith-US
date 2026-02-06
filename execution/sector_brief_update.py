"""Sector brief (deterministic): tag recent docs to sectors + write summary.

Goal:
- Maintain awareness of what is happening across sectors without constant chatter.

Inputs:
- Recent ingested docs (docs_raw + docs_text) from Supabase
- Cached ticker->sector mapping via execution/yf_meta.py
- Sector radar snapshot from output/sector_radar.json (optional)

Outputs:
- output/sector_brief.json
- docs/SECTOR_NOTES.md (append-only, 1 per day)
- Optional: Telegram alert only when triggers fire

No LLM.
"""

from __future__ import annotations

import argparse
import datetime as dt
import json
import os
import re
from collections import Counter, defaultdict
from pathlib import Path
from typing import Any, Dict, List, Optional, Tuple

import pandas as pd
import requests
from dotenv import load_dotenv

REPO = Path(__file__).resolve().parents[1]
OUT_JSON = REPO / "output" / "sector_brief.json"
OUT_MD = REPO / "docs" / "SECTOR_NOTES.md"
SECTOR_RADAR_PATH = REPO / "output" / "sector_radar.json"
TICKERS_FILE = REPO / "execution" / "sp500_tickers.txt"

# Trigger thresholds (tweakable)
TRIGGER_ABS_RET1 = float(os.getenv("SECTOR_BRIEF_TRIGGER_ABS_RET1", "0.015"))  # 1.5%
TRIGGER_DOC_SPIKE_MULT = float(os.getenv("SECTOR_BRIEF_TRIGGER_DOC_SPIKE_MULT", "2.5"))


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


def load_universe() -> set[str]:
    ticks: List[str] = []
    if TICKERS_FILE.exists():
        ticks = [t.strip().upper() for t in TICKERS_FILE.read_text(encoding="utf-8").splitlines() if t.strip()]
    # Add common ETF proxies we use elsewhere
    ticks += [
        "SPY","QQQ","IWM","TLT","HYG","GLD","SLV","USO","UNG",
        "XLC","XLY","XLP","XLE","XLF","XLV","XLI","XLB","XLRE","XLK","XLU",
    ]
    return set([t for t in ticks if re.fullmatch(r"[A-Z.]{1,6}", t)])


def fetch_recent_docs(since_utc: dt.datetime, limit: int = 400) -> List[Dict[str, Any]]:
    base = sb_base()
    url = f"{base}/rest/v1/docs_text"
    # Join docs_raw for metadata
    select = "doc_id,cleaned_text,docs_raw!inner(url,source,published_at)"
    params = [
        ("select", select),
        ("docs_raw.published_at", f"gte.{since_utc.isoformat()}"),
        # Ordering on joined fields is picky in PostgREST; use observed_at as stable proxy.
        ("order", "created_at.desc"),
        ("limit", str(limit)),
    ]
    r = requests.get(url, headers=sb_headers(), params=params, timeout=30)
    if r.status_code >= 300:
        raise RuntimeError(f"docs_text fetch failed: {r.status_code} {r.text}")
    return r.json() or []


def extract_tickers(text: str, universe: set[str]) -> List[str]:
    """Extract likely tickers from text.

    We intentionally avoid 1-letter false positives (A/I/C/D/F/etc) by only
    accepting 1-letter tickers when they appear as $X.
    """

    if not text:
        return []

    out: List[str] = []
    seen = set()

    # Exchange: TICKER patterns (high-signal). Allow 1-6.
    for m in re.findall(r"\b(?:NYSE|NASDAQ|AMEX|TSX|TSXV|ASX)\s*[:\/]\s*([A-Z]{1,6})\b", text):
        t = m
        if t in universe and t not in seen:
            out.append(t)
            seen.add(t)

    # $TICKER is high-signal. Allow 1-6.
    for m in re.findall(r"\$([A-Z]{1,6})", text):
        t = m
        if t in universe and t not in seen:
            out.append(t)
            seen.add(t)

    # Bare tickers: require 2-6 letters to reduce false positives.
    for m in re.findall(r"\b([A-Z]{2,6})\b", text):
        t = m
        if t in universe and t not in seen:
            out.append(t)
            seen.add(t)

    return out


def sector_for_ticker(t: str) -> str:
    try:
        from yf_meta import get_meta

        meta = get_meta(t) or {}
        s = meta.get("sector")
        if s:
            return str(s)
    except Exception:
        pass
    return "Unknown"


def load_sector_radar() -> Optional[dict]:
    if not SECTOR_RADAR_PATH.exists():
        return None
    try:
        return json.loads(SECTOR_RADAR_PATH.read_text(encoding="utf-8"))
    except Exception:
        return None


def append_once(day: dt.date, md: str) -> None:
    OUT_MD.parent.mkdir(parents=True, exist_ok=True)
    if not OUT_MD.exists():
        OUT_MD.write_text("# SignalSmith — Sector Notes (append-only)\n\n---\n", encoding="utf-8")

    header = f"## {day.isoformat()}"
    existing = OUT_MD.read_text(encoding="utf-8")
    if header in existing:
        print("HEARTBEAT_OK")
        return

    with OUT_MD.open("a", encoding="utf-8") as fp:
        fp.write("\n" + header + "\n" + md.strip() + "\n")


def main() -> None:
    load_env()

    ap = argparse.ArgumentParser()
    ap.add_argument("--day", default=dt.date.today().isoformat())
    ap.add_argument("--lookback-hours", type=float, default=24.0)
    ap.add_argument("--notify", action="store_true", help="Send Telegram only if triggers fire")
    args = ap.parse_args()

    day = dt.date.fromisoformat(args.day)
    if not market_is_open(day.isoformat()):
        print("HEARTBEAT_OK")
        return

    now = dt.datetime.now(dt.timezone.utc)
    since = now - dt.timedelta(hours=float(args.lookback_hours))

    universe = load_universe()
    docs = fetch_recent_docs(since)

    # Tag docs to sectors by mentioned tickers
    sector_docs: Dict[str, List[Dict[str, Any]]] = defaultdict(list)
    sector_ticker_counts: Dict[str, Counter] = defaultdict(Counter)

    for d in docs:
        txt = (d.get("cleaned_text") or "")[:8000]
        tickers = extract_tickers(txt, universe)
        if not tickers:
            continue

        # Assign doc to all sectors mentioned (via tickers)
        sectors = sorted(set([sector_for_ticker(t) for t in tickers]))
        meta = d.get("docs_raw") or {}
        item = {
            "doc_id": d.get("doc_id"),
            "published_at": meta.get("published_at"),
            "source": meta.get("source"),
            "url": meta.get("url"),
            "tickers": tickers[:15],
            "snippet": re.sub(r"\s+", " ", txt.strip())[:220],
        }
        for s in sectors:
            sector_docs[s].append(item)
        for t in tickers:
            sector_ticker_counts[sector_for_ticker(t)][t] += 1

    # Build summary
    radar = load_sector_radar() or {}
    sectors_radar = radar.get("sectors") or []

    leaders = sectors_radar[:3] if len(sectors_radar) >= 3 else sectors_radar
    laggards = list(reversed(sectors_radar[-3:])) if len(sectors_radar) >= 3 else []

    summary = {
        "generated_at_utc": now.replace(microsecond=0).isoformat().replace("+00:00", "Z"),
        "lookback_hours": float(args.lookback_hours),
        "leaders": leaders,
        "laggards": laggards,
        "sectors": [],
    }

    # Determine triggers
    triggers: List[str] = []
    for x in sectors_radar:
        try:
            if abs(float(x.get("ret1") or 0.0)) >= TRIGGER_ABS_RET1:
                triggers.append(f"{x.get('symbol')} ret1={float(x.get('ret1')):+.1%}")
        except Exception:
            pass

    # sector doc counts
    doc_counts = {s: len(v) for s, v in sector_docs.items()}

    # baseline: median sector doc count
    baseline = 0.0
    if doc_counts:
        baseline = float(pd.Series(list(doc_counts.values())).median())
    for s, n in sorted(doc_counts.items(), key=lambda kv: kv[1], reverse=True):
        if baseline > 0 and n >= TRIGGER_DOC_SPIKE_MULT * baseline and n >= 8:
            triggers.append(f"news spike in {s}: {n} docs (median~{baseline:.0f})")

    # Build per-sector blocks
    for s in sorted(sector_docs.keys(), key=lambda x: len(sector_docs[x]), reverse=True):
        top_ticks = sector_ticker_counts[s].most_common(8)
        summary["sectors"].append(
            {
                "sector": s,
                "doc_count": len(sector_docs[s]),
                "top_tickers": [{"ticker": t, "mentions": c} for t, c in top_ticks],
                "docs": sector_docs[s][:8],
            }
        )

    OUT_JSON.parent.mkdir(parents=True, exist_ok=True)
    OUT_JSON.write_text(json.dumps(summary, indent=2, default=str) + "\n", encoding="utf-8")

    # Markdown note
    md_lines: List[str] = []
    md_lines.append(f"- Generated: {summary['generated_at_utc']}")
    if leaders:
        md_lines.append("- Sector leaders (rs20 vs SPY): " + ", ".join([f"{x.get('symbol')} ({float(x.get('rs20') or 0):+.1%})" for x in leaders]))
    if laggards:
        md_lines.append("- Sector laggards (rs20 vs SPY): " + ", ".join([f"{x.get('symbol')} ({float(x.get('rs20') or 0):+.1%})" for x in laggards]))

    if triggers:
        md_lines.append("- Triggers: " + "; ".join(triggers))

    # Top sectors by doc volume
    if summary["sectors"]:
        md_lines.append("\n### Sector news volume (last 24h)")
        for blk in summary["sectors"][:8]:
            s = blk["sector"]
            md_lines.append(f"- {s}: {blk['doc_count']} docs")
            if blk.get("top_tickers"):
                md_lines.append("  - tickers: " + ", ".join([f"{x['ticker']}({x['mentions']})" for x in blk["top_tickers"][:6]]))

    append_once(day, "\n".join(md_lines))

    if args.notify and triggers:
        send_telegram(
            "Sector Brief triggers — {day}\n\n".format(day=day.isoformat())
            + "- "
            + "\n- ".join(triggers[:10])
        )

    print("HEARTBEAT_OK")


if __name__ == "__main__":
    main()
