"""SEC EDGAR digest (deterministic).

Fetches recent SEC filing index pages already ingested into Supabase (docs_raw)
(and optional cleaned_text from docs_text) and produces a short, human-friendly
summary list.

Usage:
  python execution/sec_digest.py --lookback-min 240 --limit 25

Output:
  Prints markdown-ish lines suitable for pasting into Telegram.

Notes:
- This does NOT scrape new SEC pages; it relies on already-ingested docs_raw.
- It uses conservative parsing (companyName span + 'Form X' line + 'Items' lines).
"""

from __future__ import annotations

import argparse
import datetime as dt
import os
import re
from typing import Dict, List, Optional, Tuple

import requests
from bs4 import BeautifulSoup
from dotenv import load_dotenv


FORM_PRIORITY = {
    # offerings / dilution
    "S-1": 100,
    "S-3": 95,
    "424B5": 92,
    "FWP": 90,
    "424B3": 80,
    # material events
    "8-K": 70,
    "8-K/A": 65,
    # governance/ownership
    "SC 13D": 60,
    "SC 13G": 40,
    "DEF 14A": 40,
    # periodics
    "10-Q": 35,
    "10-K": 35,
}

ITEM_BONUS: List[Tuple[re.Pattern, int, str]] = [
    (re.compile(r"Item\s+1\.01", re.I), 25, "Material agreement"),
    (re.compile(r"Item\s+2\.02", re.I), 12, "Results/earnings"),
    (re.compile(r"Item\s+1\.02", re.I), 10, "Agreement termination"),
    (re.compile(r"Item\s+3\.03", re.I), 10, "Security holder rights"),
    (re.compile(r"Item\s+5\.02", re.I), 8, "Mgmt/board change"),
    (re.compile(r"Item\s+5\.07", re.I), 6, "Vote results"),
    (re.compile(r"Item\s+8\.01", re.I), 6, "Other events"),
]


def load_env() -> None:
    env_path = os.path.join(os.path.dirname(__file__), "..", ".env")
    if os.path.exists(env_path):
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
    return {"apikey": key, "Authorization": f"Bearer {key}"}


def parse_args() -> argparse.Namespace:
    p = argparse.ArgumentParser(description="Build a quick digest of recently ingested SEC filing index pages")
    p.add_argument("--lookback-min", type=int, default=240)
    p.add_argument("--limit", type=int, default=40)
    p.add_argument("--top", type=int, default=10)
    return p.parse_args()


def fetch_recent_sec_rows(since_iso: str, limit: int) -> List[dict]:
    base = supabase_base()
    url = f"{base}/rest/v1/docs_raw"
    params = [
        ("select", "doc_id,url,observed_at,raw_content"),
        ("source", "eq.www.sec.gov"),
        ("observed_at", f"gte.{since_iso}"),
        ("order", "observed_at.desc"),
        ("limit", str(limit)),
    ]
    r = requests.get(url, headers=supabase_headers(), params=params, timeout=30)
    r.raise_for_status()
    return r.json() or []


def fetch_cleaned_text(doc_ids: List[str]) -> Dict[str, str]:
    if not doc_ids:
        return {}
    base = supabase_base()
    url = f"{base}/rest/v1/docs_text"
    in_list = ",".join(doc_ids)
    params = [("select", "doc_id,cleaned_text"), ("doc_id", f"in.({in_list})")]
    r = requests.get(url, headers=supabase_headers(), params=params, timeout=30)
    r.raise_for_status()
    out = {}
    for row in r.json() or []:
        out[row["doc_id"]] = row.get("cleaned_text") or ""
    return out


def normalize_form(s: str) -> Optional[str]:
    if not s:
        return None
    s = s.strip().upper()
    # common variants
    s = s.replace("FORM ", "")
    s = re.sub(r"\s+", " ", s)
    # keep canonical like 8-K/A
    return s


def parse_company_and_form(html: str) -> Tuple[Optional[str], Optional[str]]:
    soup = BeautifulSoup(html or "", "html.parser")

    company = None
    span = soup.find("span", {"class": "companyName"})
    if span:
        # e.g. "SILGAN HOLDINGS INC (Filer) CIK : 0000849869 ..."
        company = span.get_text(" ", strip=True)
        # trim after (Filer) if present
        company = company.split("(Filer)")[0].strip() if "(Filer)" in company else company

    # Find a line like "Form 8-K"
    text = soup.get_text("\n")
    form = None
    for line in text.splitlines():
        line = line.strip()
        if not line:
            continue
        if line.lower().startswith("form ") and len(line) <= 20:
            form = normalize_form(line)
            break

    return company, form


def parse_items(cleaned_text: str) -> List[str]:
    if not cleaned_text:
        return []
    items: List[str] = []
    for line in cleaned_text.splitlines():
        line = line.strip()
        if line.lower().startswith("item "):
            # keep short
            items.append(re.sub(r"\s+", " ", line))
    # de-dupe preserving order
    out: List[str] = []
    seen = set()
    for it in items:
        if it not in seen:
            out.append(it)
            seen.add(it)
    return out[:6]


def score(form: Optional[str], items: List[str]) -> Tuple[int, List[str]]:
    s = 0
    reasons: List[str] = []
    if form:
        s += FORM_PRIORITY.get(form, 5)
        if form in ("S-1", "S-3", "424B5", "FWP", "424B3"):
            reasons.append("Financing/offerings")
        elif form.startswith("8-K"):
            reasons.append("Material event")
    blob = "\n".join(items)
    for pat, bonus, label in ITEM_BONUS:
        if pat.search(blob):
            s += bonus
            reasons.append(label)
    # de-dupe reasons
    reasons2: List[str] = []
    seen = set()
    for r in reasons:
        if r not in seen:
            reasons2.append(r)
            seen.add(r)
    return s, reasons2[:3]


def main() -> None:
    load_env()
    args = parse_args()

    now = dt.datetime.now(dt.timezone.utc)
    since = (now - dt.timedelta(minutes=args.lookback_min)).replace(microsecond=0)
    since_iso = since.isoformat().replace("+00:00", "Z")

    rows = fetch_recent_sec_rows(since_iso, args.limit)
    if not rows:
        print("No recent SEC filings ingested.")
        return

    cleaned = fetch_cleaned_text([r["doc_id"] for r in rows])

    parsed = []
    for r in rows:
        company, form = parse_company_and_form(r.get("raw_content") or "")
        items = parse_items(cleaned.get(r["doc_id"], ""))
        s, reasons = score(form, items)
        parsed.append(
            {
                "score": s,
                "company": company or "(unknown)",
                "form": form or "(unknown)",
                "items": items,
                "reasons": reasons,
                "url": r.get("url") or "",
                "observed_at": r.get("observed_at") or "",
            }
        )

    parsed.sort(key=lambda x: (-x["score"], x["observed_at"]))

    top = parsed[: args.top]
    lines = []
    lines.append(f"SEC filings (last {args.lookback_min}m) — top {len(top)}")
    for x in top:
        items = "; ".join(x["items"][:3]) if x["items"] else "(no item breakdown)"
        why = ", ".join(x["reasons"]) if x["reasons"] else ""
        lines.append(f"- {x['company']} — {x['form']}{(' — ' + why) if why else ''}\n  {items}\n  {x['url']}")

    print("\n".join(lines))


if __name__ == "__main__":
    main()
