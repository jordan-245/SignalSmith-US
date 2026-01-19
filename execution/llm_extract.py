"""
Stub LLM extraction: reads cleaned docs from Supabase, applies cutoff and budget, and writes docs_extracted rows.
Replace the extraction stub with a real Gemini call; caching by content_hash is enforced via Supabase check.
"""

from __future__ import annotations

import argparse
import datetime as dt
import json
import os
import re
from pathlib import Path
from typing import Dict, List, Set

import requests
from dotenv import load_dotenv

DEFAULT_SCHEMA_VERSION = "v0"
DEFAULT_BUDGET = 5.0  # dollars/day
TOKENS_PER_CHAR = 0.25
COST_PER_TOKEN = 0.000002  # stub cost
DEFAULT_TICKERS_FILE = Path(__file__).with_name("sp500_tickers.txt")
TICKER_STOPWORDS = {"USA", "CEO", "CFO", "EPS", "EBITDA", "FY", "Q1", "Q2", "Q3", "Q4", "SEC"}
SOURCE_TICKER_MAP = {
    "apple.com": "AAPL",
    "www.apple.com": "AAPL",
    "nvidianews.nvidia.com": "NVDA",
    "nvidia.com": "NVDA",
    "press.aboutamazon.com": "AMZN",
    "ir.aboutamazon.com": "AMZN",
    "about.netflix.com": "NFLX",
    "investor.microsoft.com": "MSFT",
    "news.microsoft.com": "MSFT",
}


def load_env() -> None:
    env_path = Path(__file__).resolve().parents[1] / ".env"
    if env_path.exists():
        load_dotenv(env_path)


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description="Stub LLM extraction for cleaned docs in Supabase.")
    parser.add_argument("--max-docs", type=int, default=20, help="Max docs to process.")
    parser.add_argument("--budget", type=float, default=DEFAULT_BUDGET, help="Daily budget in dollars.")
    parser.add_argument("--schema-version", default=DEFAULT_SCHEMA_VERSION, help="Schema version tag.")
    parser.add_argument(
        "--tickers-file",
        default=os.getenv("UNIVERSE_TICKERS_FILE") or str(DEFAULT_TICKERS_FILE),
        help="Optional file with one allowed ticker per line for relevance filtering.",
    )
    parser.add_argument(
        "--min-tickers",
        type=int,
        default=1,
        help="Minimum ticker hits required to spend budget on a doc (after allowlist filtering).",
    )
    return parser.parse_args()


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


def fetch_candidates(limit: int) -> List[Dict]:
    base = supabase_base()
    url = f"{base}/rest/v1/docs_text"
    params = {
        "select": "doc_id,cleaned_text,text_hash,docs_raw!inner(content_hash,published_at,source)",
        "order": "created_at.desc",
        "limit": limit,
    }
    resp = requests.get(url, headers=supabase_headers(), params=params, timeout=15)
    resp.raise_for_status()
    return resp.json()


def existing_extractions(content_hashes: Set[str]) -> Set[str]:
    if not content_hashes:
        return set()
    base = supabase_base()
    url = f"{base}/rest/v1/docs_raw"
    params = {"select": "content_hash,docs_extracted(doc_id)", "content_hash": f"in.({','.join(content_hashes)})"}
    resp = requests.get(url, headers=supabase_headers(), params=params, timeout=15)
    resp.raise_for_status()
    rows = resp.json()
    seen = set()
    for row in rows:
        if row.get("docs_extracted"):
            seen.add(row["content_hash"])
    return seen


def load_ticker_allowlist(path: str | None) -> Set[str]:
    if not path:
        return set()
    try:
        with open(path, "r", encoding="utf-8") as f:
            return {line.strip().upper() for line in f if line.strip()}
    except FileNotFoundError:
        print(f"[tickers] allowlist not found at {path}; continuing without allowlist.")
        return set()


def extract_candidate_tickers(text: str, allowlist: Set[str]) -> List[str]:
    if not text:
        return []
    matches = re.findall(r"\b[A-Z]{1,5}\b", text)
    tickers: List[str] = []
    for m in matches:
        if allowlist and m not in allowlist:
            continue
        if not allowlist and m in TICKER_STOPWORDS:
            continue
        if m not in tickers:
            tickers.append(m)
    return tickers


def infer_ticker_from_source(source: str | None, allowlist: Set[str]) -> List[str]:
    if not source:
        return []
    ticker = SOURCE_TICKER_MAP.get(source) or SOURCE_TICKER_MAP.get(source.replace("www.", "", 1))
    if ticker and (not allowlist or ticker in allowlist):
        return [ticker]
    return []


def stub_extract(text: str, tickers: List[str]) -> Dict:
    # Replace with actual Gemini call; this is a placeholder deterministic payload.
    return {
        "doc_type": "other",
        "event_types": [],
        "tone_score": 0.0,
        "uncertainty_score": 0.0,
        "numeric_claims": [],
        "tickers_mentioned": [{"ticker": t, "confidence": 0.6} for t in tickers],
        "summary_bullets": [],
    }


def insert_docs_extracted(rows: List[Dict]) -> None:
    if not rows:
        return
    base = supabase_base()
    url = f"{base}/rest/v1/docs_extracted"
    headers = supabase_headers()
    headers["Prefer"] = "return=minimal"
    resp = requests.post(url, headers=headers, json=rows, timeout=15)
    if resp.status_code >= 300:
        raise RuntimeError(f"docs_extracted insert failed: {resp.status_code} {resp.text}")


def main() -> None:
    load_env()
    args = parse_args()
    allowlist = load_ticker_allowlist(args.tickers_file)

    candidates = fetch_candidates(limit=args.max_docs)
    if not candidates:
        print("[done] No cleaned docs to process.")
        return

    # Deduplicate by content_hash and skip already extracted
    content_hashes = {c["docs_raw"]["content_hash"] for c in candidates}
    already = existing_extractions(content_hashes)
    queue = [c for c in candidates if c["docs_raw"]["content_hash"] not in already]

    budget_used = 0.0
    to_insert = []
    for c in queue:
        text = c.get("cleaned_text") or ""
        source = c.get("docs_raw", {}).get("source")
        tickers = extract_candidate_tickers(text, allowlist)
        if not tickers:
            tickers = infer_ticker_from_source(source, allowlist)
        if len(tickers) < args.min_tickers:
            print(f"[skip] {c.get('doc_id')} skipped: insufficient ticker hits (found {len(tickers)}).")
            continue
        tokens_in = int(len(text) * TOKENS_PER_CHAR)
        cost = tokens_in * COST_PER_TOKEN
        if budget_used + cost > args.budget:
            print(f"[budget] stop: would exceed budget (${args.budget}).")
            break
        payload = stub_extract(text, tickers)
        to_insert.append(
            {
                "doc_id": c["doc_id"],
                "schema_version": args.schema_version,
                "extracted_json": payload,
                "confidence": None,
                "status": "success",
                "error_msg": None,
                "tokens_in": tokens_in,
                "tokens_out": 0,
                "cost_estimate": cost,
            }
        )
        budget_used += cost

    if not to_insert:
        print("[done] Nothing to insert (budget or duplicates).")
        return

    try:
        insert_docs_extracted(to_insert)
    except Exception as exc:
        raise SystemExit(str(exc))

    print(f"[done] Inserted {len(to_insert)} extractions; budget used ~${budget_used:.4f}.")


if __name__ == "__main__":
    main()
