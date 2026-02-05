"""Extract key dilution terms from recent SEC offering filings (deterministic).

Given recent SEC filing index pages already ingested (docs_raw), locate the
primary filing document link (S-1/S-1A/S-3/S-3A/424B*/FWP) and scrape a few
high-signal terms:
- estimated offering size / aggregate price
- share counts (if present)
- structure hints (ATM / underwritten / registered direct / PIPE / warrants)
- 'use of proceeds' presence

Usage:
  python execution/sec_dilution_terms.py --lookback-min 1440 --top 10

Output:
  Prints short bullets.
"""

from __future__ import annotations

import argparse
import datetime as dt
import os
import re
import time
from typing import Dict, List, Optional, Tuple

import requests
from bs4 import BeautifulSoup
from dotenv import load_dotenv

UA = "SignalSmith/0.1 (sec-terms; +https://srv1281557.hstgr.cloud; research bot)"

OFFER_FORMS = {"S-1", "S-1/A", "S-3", "S-3/A", "424B5", "424B3", "FWP"}

STRUCT_PATTERNS: List[Tuple[re.Pattern, str]] = [
    (re.compile(r"at\-the\-market|\bATM\b", re.I), "ATM"),
    (re.compile(r"underwritten public offering", re.I), "Underwritten"),
    (re.compile(r"registered direct", re.I), "Registered Direct"),
    (re.compile(r"PIPE\b|private investment in public equity", re.I), "PIPE"),
    (re.compile(r"warrants?", re.I), "Warrants"),
    (re.compile(r"selling stockholders?|resale", re.I), "Resale/Selling SH"),
]

MONEY_RE = re.compile(r"\$\s?([0-9]{1,3}(?:,[0-9]{3})*(?:\.[0-9]+)?)(?:\s?(million|billion))?", re.I)
# Some filings say "up to $X" / "aggregate offering price" / "maximum aggregate"
MONEY_CTX_RE = re.compile(
    r"(?:(?:up to|maximum|aggregate|total)\s+)?(?:aggregate\s+offering\s+price|aggregate\s+price|offering\s+price|gross\s+proceeds|maximum\s+aggregate\s+offering\s+price)[^\$]{0,80}(\$\s?[0-9][0-9,]*(?:\.[0-9]+)?(?:\s?(?:million|billion))?)",
    re.I,
)

# Shares — common patterns
SHARES_RE = re.compile(r"([0-9]{1,3}(?:,[0-9]{3})+)\s+(?:shares?)\s+of\s+(?:common stock|ordinary shares)", re.I)
SHARES_CTX_RE = re.compile(
    r"(?:up to|maximum of|a total of|totaling)?\s*([0-9]{1,3}(?:,[0-9]{3})+)\s+(?:shares?)\b",
    re.I,
)

_LAST_SEC_REQ = 0.0


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
    p = argparse.ArgumentParser(description="Extract dilution terms from SEC offering filings")
    p.add_argument("--lookback-min", type=int, default=1440)
    p.add_argument("--limit", type=int, default=600)
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
        if line.lower().startswith("form ") and len(line) <= 28:
            form = normalize_form(line)
            break
    return company, form


def find_primary_doc_url(index_url: str, index_html: str, target_form: str) -> Optional[str]:
    soup = BeautifulSoup(index_html or "", "html.parser")

    # SEC index uses table.tableFile (document list)
    table = soup.find("table", {"class": "tableFile"})
    if not table:
        return None

    # Current SEC layout columns: Seq | Description | Document | Type | Size
    best = None
    for tr in table.find_all("tr"):
        tds = tr.find_all("td")
        if len(tds) < 4:
            continue
        doc_cell = tds[2]
        type_cell = tds[3]
        doc_link = doc_cell.find("a")
        if not doc_link or not doc_link.get("href"):
            continue
        doc_href = doc_link["href"].strip()
        ftype = type_cell.get_text(" ", strip=True).upper()

        # Prefer the row whose Type matches the filing form.
        if ftype == target_form.upper():
            best = doc_href
            break

    # fallback: first HTML-ish document in the list that is not the -index page
    if not best:
        for tr in table.find_all("tr"):
            tds = tr.find_all("td")
            if len(tds) < 3:
                continue
            doc_cell = tds[2]
            a = doc_cell.find("a")
            if not a or not a.get("href"):
                continue
            href = a["href"].strip()
            if href.endswith("-index.htm"):
                continue
            if any(href.lower().endswith(ext) for ext in (".htm", ".html", ".txt")):
                best = href
                break

    if not best:
        return None

    # make absolute
    if best.startswith("http"):
        return best
    # index_url is like https://www.sec.gov/Archives/edgar/data/.../....-index.htm
    # relative href is like /Archives/edgar/data/.../filename.htm
    if best.startswith("/"):
        return "https://www.sec.gov" + best

    # otherwise relative to directory
    base_dir = index_url.rsplit("/", 1)[0]
    return base_dir + "/" + best


def sec_get(url: str, timeout: int = 30) -> str:
    global _LAST_SEC_REQ
    # throttle
    now = time.time()
    sleep_for = 0.8 - (now - _LAST_SEC_REQ)
    if sleep_for > 0:
        time.sleep(sleep_for)
    _LAST_SEC_REQ = time.time()

    # Prefer non-iXBRL doc URL when present.
    if url.startswith("https://www.sec.gov/ix?doc="):
        url = "https://www.sec.gov" + url.split("doc=", 1)[1]

    r = requests.get(url, headers={"User-Agent": UA}, timeout=timeout)
    r.raise_for_status()
    return r.text


def extract_terms(text: str) -> Dict[str, object]:
    t = " ".join((text or "").split())
    out: Dict[str, object] = {}

    # structure tags
    tags = []
    for pat, label in STRUCT_PATTERNS:
        if pat.search(t):
            tags.append(label)
    out["tags"] = tags

    # money amounts: prefer context-matched amounts first (more likely to be the actual offering size)
    def _money_to_float(val: str) -> float:
        s = val.strip().lower().replace("$", "").replace(",", "")
        mult = 1.0
        if "billion" in s:
            mult = 1e9
            s = s.replace("billion", "")
        elif "million" in s:
            mult = 1e6
            s = s.replace("million", "")
        try:
            return float(s.strip()) * mult
        except Exception:
            return 0.0

    m_raw: List[str] = []
    seen = set()
    for mm in MONEY_CTX_RE.finditer(t[:250000]):
        val = re.sub(r"\s+", " ", mm.group(1)).strip()
        if val in seen:
            continue
        seen.add(val)
        m_raw.append(val)
        if len(m_raw) >= 8:
            break

    # fallback: capture a few raw $ amounts
    if len(m_raw) < 4:
        for mm in MONEY_RE.finditer(t[:250000]):
            num = mm.group(1)
            scale = (mm.group(2) or "").lower()
            val = "$" + num + (" " + scale if scale else "")
            if val in seen:
                continue
            seen.add(val)
            m_raw.append(val)
            if len(m_raw) >= 12:
                break

    # Filter out tiny values (par value / exercise prices) and keep the largest few
    m_scored = [(v, _money_to_float(v)) for v in m_raw]
    m_scored = [(v, x) for v, x in m_scored if x >= 1_000_000]
    m_scored.sort(key=lambda vx: -vx[1])
    m = [v for v, _ in m_scored[:3]]

    out["money"] = m

    # shares: prefer specific "shares of common stock" patterns; fallback to contextual shares counts
    shares: List[str] = []
    seen2 = set()
    for sm in SHARES_RE.finditer(t[:250000]):
        val = sm.group(1)
        if val in seen2:
            continue
        seen2.add(val)
        shares.append(val)
        if len(shares) >= 3:
            break

    if not shares:
        for sm in SHARES_CTX_RE.finditer(t[:120000]):
            val = sm.group(1)
            if val in seen2:
                continue
            # avoid obvious non-share counts (years, etc.) by requiring comma formatting
            if "," not in val:
                continue
            seen2.add(val)
            shares.append(val)
            if len(shares) >= 2:
                break

    out["shares"] = shares

    out["use_of_proceeds"] = bool(re.search(r"use of proceeds", t, re.I))
    return out


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

    candidates = []
    for r in rows:
        company, form = parse_company_and_form(r.get("raw_content") or "")
        if not form or form not in OFFER_FORMS:
            continue
        candidates.append({
            "company": company or "(unknown)",
            "form": form,
            "url": r.get("url") or "",
            "doc_id": r["doc_id"],
            "index_html": r.get("raw_content") or "",
            "observed_at": r.get("observed_at") or "",
            "cleaned_index": cleaned.get(r["doc_id"], ""),
        })

    if not candidates:
        print("No offering-form filings found in lookback window.")
        return

    # Prefer most recent; user wants quick terms, not exhaustive.
    candidates.sort(key=lambda x: x["observed_at"], reverse=True)
    candidates = candidates[: args.top]

    lines: List[str] = []
    lines.append(f"Dilution terms (last {args.lookback_min}m) — {len(candidates)} filing(s)")

    for c in candidates:
        primary = find_primary_doc_url(c["url"], c["index_html"], c["form"]) or ""
        terms: Dict[str, object] = {}
        err = None
        if primary:
            try:
                doc_html = sec_get(primary, timeout=40)
                doc_text = BeautifulSoup(doc_html, "html.parser").get_text(" ")
                terms = extract_terms(doc_text)
            except Exception as exc:
                err = str(exc)

        tags = ", ".join(terms.get("tags", []) or [])
        money = ", ".join((terms.get("money") or [])[:2])
        shares = ", ".join((terms.get("shares") or [])[:2])
        uop = terms.get("use_of_proceeds")

        bits = []
        if tags:
            bits.append(tags)
        if money:
            bits.append(f"$ sizes: {money}")
        if shares:
            bits.append(f"shares: {shares}")
        if uop:
            bits.append("has Use of Proceeds")

        summary = " | ".join(bits) if bits else "(terms not found yet)"
        if err:
            summary = summary + f" | fetch err: {err[:120]}"

        lines.append(f"- {c['company']} — {c['form']}\n  {summary}\n  index: {c['url']}\n  doc: {primary or '(not found)'}")

    print("\n".join(lines))


if __name__ == "__main__":
    main()
