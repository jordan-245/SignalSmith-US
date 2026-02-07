"""Idea candidates digest (deterministic).

Goal: surface *new* small-cap catalysts without requiring a predefined ticker list.

Approach:
- Scan recently ingested docs (docs_text joined with docs_raw)
- Apply strict catalyst keyword heuristics (positive + negative)
- Extract likely tickers (very heuristic) and rank candidates
- Send a short Telegram digest (quiet if nothing meaningful)

This is designed to be used on a schedule (premarket + post-close).

Usage:
  ./.venv/bin/python execution/idea_candidates_digest.py --lookback-min 720

Exit behavior:
- If nothing to report: prints HEARTBEAT_OK
- If digest sent: prints HEARTBEAT_OK

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


# Keep patterns fairly strict to avoid turning the digest into a general news summary.
PATTERNS: List[Tuple[str, int, str]] = [
    # Trading / listing / structure
    (r"trading halt|halted trading|resumption of trading|resumes trading", 45, "Halt/Resumption"),
    (r"nasdaq (?:has )?notified|listing determination|hearing panel", 35, "Listing notice"),
    (r"regain compliance|regained compliance|minimum bid", 30, "Compliance regained"),
    (r"reverse stock split|reverse split", 30, "Reverse split"),
    (r"uplisting|up-listing|transfer to nasdaq|list on nasdaq", 28, "Uplisting"),

    # Capital markets / dilution risk
    (r"registered direct offering|public offering|underwritten offering", 45, "Offering"),
    (r"at-the-market|\batm program\b", 40, "ATM"),
    (r"private placement", 35, "Private placement"),
    (r"warrant\b|pre-funded warrant", 25, "Warrants"),

    # M&A / strategic
    (r"strategic alternatives|exploring strategic alternatives", 45, "Strategic alternatives"),
    (r"acquisition|to acquire|merger agreement|definitive agreement", 35, "M&A"),
    (r"spin-off|spinoff", 25, "Spin-off"),

    # Earnings / guidance
    (r"preliminary results|unaudited results", 25, "Prelim results"),
    (r"guidance", 18, "Guidance"),

    # Distress / legal
    (r"going concern", 45, "Going concern"),
    (r"chapter 11|bankruptcy", 60, "Bankruptcy"),
    (r"subpoena|sec investigation|doj investigation|grand jury", 55, "Investigation"),
    (r"restatement", 55, "Restatement"),

    # Cyber catalysts
    (r"ransomware|data breach|unauthorized access|cyber incident", 40, "Cyber incident"),
    (r"zero-day|0-day|known exploited vulnerability|kev", 30, "Exploit/KEV"),

    # Product / contract (keep lighter)
    (r"contract award|task order|sole-source|multi-year contract", 28, "Contract award"),
    (r"patent granted|fda clearance|fda approval", 22, "Regulatory milestone"),
]

TICKER_RE = re.compile(r"\b[A-Z]{1,5}\b")
TICKER_STOP = {
    "THE",
    "AND",
    "FOR",
    "WITH",
    "FROM",
    "THIS",
    "THAT",
    "CEO",
    "CFO",
    "SEC",
    "USA",
    "ETF",
    "NASDAQ",
    "NYSE",
}


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
    p = argparse.ArgumentParser(description="Send an idea candidates digest from recently ingested docs")
    p.add_argument("--lookback-min", type=int, default=720, help="How far back to scan (minutes)")
    p.add_argument("--limit", type=int, default=200, help="Max docs to inspect")
    p.add_argument("--top", type=int, default=10, help="Max candidates to include")
    p.add_argument("--min-score", type=int, default=45, help="Minimum score to include")
    p.add_argument("--force", action="store_true", help="Send even if no candidates meet thresholds")
    p.add_argument(
        "--title",
        default="Idea candidates",
        help="Telegram title prefix (e.g., 'Premarket ideas' / 'Post-close ideas')",
    )
    return p.parse_args()


def fetch_recent_docs(since_iso: str, limit: int) -> List[dict]:
    base = supabase_base()
    url = f"{base}/rest/v1/docs_text"
    select = "doc_id,cleaned_text,docs_raw!inner(url,source,published_at,observed_at,content_hash)"
    params = [
        ("select", select),
        ("docs_raw.observed_at", f"gte.{since_iso}"),
        ("order", "docs_raw(observed_at).desc"),
        ("limit", str(limit)),
    ]
    r = requests.get(url, headers=supabase_headers(), params=params, timeout=25)
    if r.status_code >= 300:
        raise RuntimeError(f"docs_text fetch failed: {r.status_code} {r.text}")
    return r.json() or []


def extract_tickers(text: str) -> List[str]:
    if not text:
        return []
    ticks = set(re.findall(r"\$([A-Z]{1,5})\b", text.upper()))
    # Plain tickers are noisy; keep conservative slice.
    for m in TICKER_RE.findall(text.upper()[:2500]):
        if m in TICKER_STOP:
            continue
        if 1 <= len(m) <= 5:
            ticks.add(m)
    return sorted(ticks)[:8]


def score_text(text: str) -> Tuple[int, List[str]]:
    t = (text or "").lower()
    s = 0
    labels: List[str] = []
    for pat, pts, label in PATTERNS:
        if re.search(pat, t):
            s += pts
            labels.append(label)
    # de-dupe labels
    out: List[str] = []
    seen = set()
    for l in labels:
        if l in seen:
            continue
        seen.add(l)
        out.append(l)
    return s, out[:4]


def shorten_url(url: str, max_len: int = 60) -> str:
    if not url:
        return ""
    return url if len(url) <= max_len else url[: max_len - 1] + "…"


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

    candidates: List[dict] = []
    for r in rows:
        text = r.get("cleaned_text") or ""
        md = r.get("docs_raw") or {}
        s, labels = score_text(text)
        if s <= 0:
            continue
        ticks = extract_tickers(text)
        candidates.append(
            {
                "score": s,
                "labels": labels,
                "tickers": ticks,
                "source": (md.get("source") or ""),
                "url": (md.get("url") or ""),
                "observed_at": (md.get("observed_at") or ""),
            }
        )

    # Rank and filter
    candidates.sort(key=lambda x: (-x["score"], x.get("source") or "", x.get("url") or ""))
    picked = [c for c in candidates if c["score"] >= args.min_score][: args.top]

    if not picked and not args.force:
        print("HEARTBEAT_OK")
        return

    title = f"{args.title} — last {args.lookback_min}m"
    lines = [title]

    if picked:
        for c in picked:
            t0 = c["tickers"][0] if c["tickers"] else "(no ticker)"
            lbl = ", ".join(c["labels"]) if c["labels"] else "Signal"
            lines.append(f"- {t0} | {lbl} | s={c['score']} | {shorten_url(c['url'])}")
    else:
        lines.append("- No candidates met the threshold.")

    send_telegram("\n".join(lines))
    print("HEARTBEAT_OK")


if __name__ == "__main__":
    main()
