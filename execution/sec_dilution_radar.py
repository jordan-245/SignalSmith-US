"""SEC dilution radar (deterministic).

Prioritizes recently ingested SEC filings that often imply dilution/financing:
S-1, S-3, 424B5, 424B3, FWP.

It relies on already-ingested docs_raw/docs_text.

Usage:
  python execution/sec_dilution_radar.py --lookback-min 1440 --limit 120 --top 12
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


OFFER_FORMS = {
    "S-1",
    "S-1/A",
    "S-3",
    "S-3/A",
    "424B5",
    "424B3",
    "FWP",
}
FORM_PRIORITY = {
    "S-1": 100,
    "S-1/A": 90,
    "S-3": 95,
    "S-3/A": 85,
    "424B5": 92,
    "FWP": 90,
    "424B3": 80,
}

KEYWORDS: List[Tuple[re.Pattern, int, str]] = [
    (re.compile(r"at\-the\-market|\bATM\b", re.I), 18, "ATM program"),
    (re.compile(r"registered direct", re.I), 22, "Registered direct"),
    (re.compile(r"underwritten public offering", re.I), 22, "Underwritten offering"),
    (re.compile(r"prospectus supplement", re.I), 10, "Prospectus supplement"),
    (re.compile(r"warrants?", re.I), 8, "Warrants"),
    (re.compile(r"PIPE\b|private investment in public equity", re.I), 18, "PIPE"),
    (re.compile(r"dilut", re.I), 6, "Dilution language"),
    (re.compile(r"common stock|ordinary shares", re.I), 3, "Equity issuance"),
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
    p = argparse.ArgumentParser(description="Rank recent SEC filings for dilution/financing risk")
    p.add_argument("--lookback-min", type=int, default=1440)
    p.add_argument("--limit", type=int, default=200)
    p.add_argument("--top", type=int, default=12)
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
    out: Dict[str, str] = {}
    for row in r.json() or []:
        out[row["doc_id"]] = row.get("cleaned_text") or ""
    return out


def normalize_form(s: str) -> Optional[str]:
    if not s:
        return None
    s = s.strip().upper()
    s = s.replace("FORM ", "")
    s = re.sub(r"\s+", " ", s)
    return s


def parse_company_and_form(html: str) -> Tuple[Optional[str], Optional[str]]:
    soup = BeautifulSoup(html or "", "html.parser")
    company = None
    span = soup.find("span", {"class": "companyName"})
    if span:
        company = span.get_text(" ", strip=True)
        company = company.split("(Filer)")[0].strip() if "(Filer)" in company else company

    form = None
    text = soup.get_text("\n")
    for line in text.splitlines():
        line = line.strip()
        if line.lower().startswith("form ") and len(line) <= 24:
            form = normalize_form(line)
            break
    return company, form


def score(form: Optional[str], cleaned_text: str) -> Tuple[int, List[str]]:
    s = 0
    reasons: List[str] = []
    if form:
        s += FORM_PRIORITY.get(form, 0)

    txt = cleaned_text or ""
    for pat, bonus, label in KEYWORDS:
        if pat.search(txt):
            s += bonus
            reasons.append(label)

    # de-dupe reasons
    out: List[str] = []
    seen = set()
    for r in reasons:
        if r not in seen:
            out.append(r)
            seen.add(r)
    return s, out[:4]


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

    ranked = []
    for r in rows:
        company, form = parse_company_and_form(r.get("raw_content") or "")
        if not form or form not in OFFER_FORMS:
            continue
        s, reasons = score(form, cleaned.get(r["doc_id"], ""))
        ranked.append(
            {
                "score": s,
                "company": company or "(unknown)",
                "form": form,
                "reasons": reasons,
                "url": r.get("url") or "",
                "observed_at": r.get("observed_at") or "",
            }
        )

    if not ranked:
        print(f"Dilution radar: no {', '.join(sorted(OFFER_FORMS))} filings found in last {args.lookback_min}m.")
        return

    ranked.sort(key=lambda x: (-x["score"], x["observed_at"]))
    top = ranked[: args.top]

    lines: List[str] = []
    lines.append(f"Dilution radar (last {args.lookback_min}m) — top {len(top)}")
    for x in top:
        why = ", ".join(x["reasons"]) if x["reasons"] else ""
        lines.append(f"- {x['company']} — {x['form']}{(' — ' + why) if why else ''}\n  {x['url']}")

    print("\n".join(lines))


if __name__ == "__main__":
    main()
