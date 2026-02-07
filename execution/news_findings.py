"""News watch: scan recent ingested docs and send a human-friendly Telegram update *only if* something looks noteworthy.

Deterministic (no LLM calls): uses existing docs_text/docs_raw and (optionally) docs_extracted.

Heuristics:
- Summarize counts and top tickers mentioned.
- Flag potential negative catalysts via keyword hits.

Exit behavior:
- If nothing noteworthy: print HEARTBEAT_OK (so cron stays quiet).
- If noteworthy: send Telegram message (HTML formatted via telegram_fmt) and print HEARTBEAT_OK.

"""

from __future__ import annotations

import argparse
import datetime as dt
import os
import re
from pathlib import Path
from typing import Dict, List, Tuple

import requests
from dotenv import load_dotenv

from telegram_fmt import send_telegram


NEG_PATTERNS: List[Tuple[str, str]] = [
    (r"sec investigation", "SEC investigation"),
    (r"restatement", "Restatement"),
    (r"guidance cut|cuts guidance|lower(?:ed)? guidance", "Guidance cut"),
    (r"miss(?:es|ed)? estimates|miss(?:es|ed)? expectations", "Earnings miss"),
    (r"downgrade(?:d)?", "Downgrade"),
    (r"secondary offering|dilution|dilutive", "Dilution/secondary"),
    (r"layoffs?|job cuts", "Layoffs"),
]

POS_PATTERNS: List[Tuple[str, str]] = [
    (r"beats estimates|beat estimates|tops estimates", "Beats"),
    (r"raises guidance|guidance raised|raise guidance", "Guidance raised"),
    (r"upgrade(?:d)?|price target raised", "Upgrade"),
]

TICKER_RE = re.compile(r"\b[A-Z]{1,5}\b")
TICKER_STOP = {"THE", "AND", "FOR", "WITH", "FROM", "THIS", "THAT", "CEO", "CFO", "SEC", "USA", "ETF"}


def load_env() -> None:
    env_path = Path(__file__).resolve().parents[1] / ".env"
    if env_path.exists():
        load_dotenv(env_path)


def supabase_base() -> str:
    base = os.getenv("SUPABASE_URL", "")
    if not base:
        raise RuntimeError("SUPABASE_URL not set")
    return base.rstrip("/")


def supabase_headers() -> Dict[str, str]:
    key = os.getenv("SUPABASE_SERVICE_ROLE", "")
    if not key:
        raise RuntimeError("SUPABASE_SERVICE_ROLE not set")
    return {
        "apikey": key,
        "Authorization": f"Bearer {key}",
        "Content-Type": "application/json",
    }


def parse_args() -> argparse.Namespace:
    p = argparse.ArgumentParser(description="Scan recent docs and send notable findings.")
    p.add_argument("--lookback-min", type=int, default=60, help="How far back to scan (minutes).")
    p.add_argument("--limit", type=int, default=80, help="Max docs to inspect.")
    p.add_argument("--min-docs", type=int, default=8, help="Minimum doc count before sending a routine summary.")
    p.add_argument("--force", action="store_true", help="Always send a summary, even if nothing noteworthy.")
    return p.parse_args()


def fetch_recent_docs(since_iso: str, limit: int) -> List[dict]:
    # Pull cleaned text joined with docs_raw metadata.
    base = supabase_base()
    url = f"{base}/rest/v1/docs_text"
    select = "doc_id,cleaned_text,docs_raw!inner(url,source,published_at,observed_at,content_hash)"
    params = [
        ("select", select),
        ("docs_raw.observed_at", f"gte.{since_iso}"),
        ("order", "docs_raw(observed_at).desc"),
        ("limit", str(limit)),
    ]
    r = requests.get(url, headers=supabase_headers(), params=params, timeout=20)
    if r.status_code >= 300:
        raise RuntimeError(f"docs_text fetch failed: {r.status_code} {r.text}")
    return r.json() or []


def extract_tickers(text: str) -> List[str]:
    if not text:
        return []
    # Fast heuristic: look for $TICKER first.
    ticks = set(re.findall(r"\$([A-Z]{1,5})\b", text.upper()))
    # Then plain tickers (very noisy; kept conservative)
    for m in TICKER_RE.findall(text.upper()[:4000]):
        if m in TICKER_STOP:
            continue
        if 1 <= len(m) <= 5:
            ticks.add(m)
    # keep somewhat sane
    out = sorted(ticks)
    return out[:12]


def keyword_hits(text: str) -> Tuple[List[str], List[str]]:
    t = (text or "").lower()
    neg = [label for pat, label in NEG_PATTERNS if re.search(pat, t)]
    pos = [label for pat, label in POS_PATTERNS if re.search(pat, t)]
    return neg, pos


def shorten_url(url: str, max_len: int = 70) -> str:
    if not url:
        return ""
    if len(url) <= max_len:
        return url
    return url[: max_len - 1] + "…"


def _load_alert_sources() -> set[str]:
    """Return the allowlist of docs_raw.source hostnames permitted to trigger Telegram alerts.

    If the file doesn't exist, we default to "alert on anything" (backwards compatible).
    """

    fpath = Path(__file__).resolve().parents[1] / "directives" / "news_alert_sources.txt"
    if not fpath.exists():
        return set()
    out: set[str] = set()
    for line in fpath.read_text(encoding="utf-8").splitlines():
        s = line.strip()
        if not s or s.startswith("#"):
            continue
        if "#" in s:
            s = s.split("#", 1)[0].strip()
        if s:
            out.add(s.lower())
    return out


def main() -> None:
    load_env()
    args = parse_args()

    now = dt.datetime.now(dt.timezone.utc)
    since = now - dt.timedelta(minutes=args.lookback_min)
    since_iso = since.isoformat()

    rows = fetch_recent_docs(since_iso, args.limit)
    if not rows:
        print("HEARTBEAT_OK")
        return

    # Tiering: we ingest everything, but we only *alert* on high-signal sources.
    alert_sources = _load_alert_sources()
    # Empty allowlist = backwards compatible behavior (alert on anything).
    if alert_sources:
        alert_rows = [
            r
            for r in rows
            if ((r.get("docs_raw") or {}).get("source") or "").lower() in alert_sources
        ]
    else:
        alert_rows = rows

    ticker_counts: Dict[str, int] = {}
    neg_hits: List[Tuple[str, str]] = []  # (ticker-ish, label)
    pos_hits: List[Tuple[str, str]] = []

    for r in alert_rows:
        text = (r.get("cleaned_text") or "")
        tickers = extract_tickers(text)
        for t in tickers:
            ticker_counts[t] = ticker_counts.get(t, 0) + 1

        neg, pos = keyword_hits(text)
        if neg:
            t0 = tickers[0] if tickers else "(no ticker)"
            for lbl in neg[:3]:
                neg_hits.append((t0, lbl))
        if pos:
            t0 = tickers[0] if tickers else "(no ticker)"
            for lbl in pos[:2]:
                pos_hits.append((t0, lbl))

    top_tickers = sorted(ticker_counts.items(), key=lambda kv: (-kv[1], kv[0]))[:8]

    # Notify when something looks materially actionable *from Tier A sources*.
    noteworthy = bool(neg_hits) or (len(alert_rows) >= args.min_docs)
    if not (noteworthy or args.force):
        print("HEARTBEAT_OK")
        return

    header = f"News — last {args.lookback_min}m"
    lines = [header]

    if alert_sources:
        lines.append(f"- Tier A sources scanned: {len(alert_rows)}/{len(rows)} docs")

    # Keep it short.
    if top_tickers:
        lines.append("- Mentions: " + ", ".join([f"{t} ({c})" for t, c in top_tickers[:3]]))

    if neg_hits:
        seen = set()
        uniq = []
        for t, lbl in neg_hits:
            key = (t, lbl)
            if key in seen:
                continue
            seen.add(key)
            uniq.append((t, lbl))
        lines.append("- Flags: " + "; ".join([f"{t}: {lbl}" for t, lbl in uniq[:5]]))

    send_telegram("\n".join(lines))
    print("HEARTBEAT_OK")


if __name__ == "__main__":
    main()
