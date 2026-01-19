"""
Deduplicate prices_daily on (date, ticker) by keeping the latest ingested_at row.
This rewrites the affected date range to remove duplicates server-side via REST.
"""

from __future__ import annotations

import argparse
import datetime as dt
import os
import sys
from pathlib import Path
from typing import Dict, Iterable, List

import requests
from dotenv import load_dotenv


def load_env() -> None:
    env_path = Path(__file__).resolve().parents[1] / ".env"
    if env_path.exists():
        load_dotenv(env_path)


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description="Remove duplicate prices_daily rows (date, ticker).")
    parser.add_argument("--start-date", default=None, help="Optional start date YYYY-MM-DD for cleanup scope.")
    parser.add_argument("--end-date", default=None, help="Optional end date YYYY-MM-DD for cleanup scope.")
    parser.add_argument("--page-size", type=int, default=5000, help="REST page size for fetch.")
    parser.add_argument("--chunk-days", type=int, default=30, help="Days per delete/insert chunk.")
    parser.add_argument("--batch-size", type=int, default=1000, help="Insert batch size.")
    parser.add_argument("--dry-run", action="store_true", help="Report duplicates without rewriting.")
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


def iter_date_chunks(start_date: dt.date, end_date: dt.date, chunk_days: int) -> Iterable[tuple[dt.date, dt.date]]:
    cursor = start_date
    while cursor <= end_date:
        chunk_end = min(cursor + dt.timedelta(days=chunk_days - 1), end_date)
        yield cursor, chunk_end
        cursor = chunk_end + dt.timedelta(days=1)


def fetch_prices(start_date: str | None, end_date: str | None, page_size: int) -> List[Dict]:
    base = supabase_base()
    url = f"{base}/rest/v1/prices_daily"
    rows: List[Dict] = []
    offset = 0
    while True:
        headers = supabase_headers()
        headers["Range-Unit"] = "items"
        headers["Range"] = f"{offset}-{offset + page_size - 1}"
        params: List[tuple[str, str]] = [
            ("select", "date,ticker,open,high,low,close,adj_close,volume,source,ingested_at"),
            ("order", "date.asc,ticker.asc,ingested_at.desc"),
        ]
        if start_date:
            params.append(("date", f"gte.{start_date}"))
        if end_date:
            params.append(("date", f"lte.{end_date}"))
        resp = requests.get(url, headers=headers, params=params, timeout=30)
        if resp.status_code >= 300:
            raise RuntimeError(f"prices_daily fetch failed: {resp.status_code} {resp.text}")
        batch = resp.json()
        rows.extend(batch)
        if len(batch) < page_size:
            break
        offset += page_size
    return rows


def delete_range(start_date: dt.date, end_date: dt.date) -> None:
    base = supabase_base()
    url = f"{base}/rest/v1/prices_daily"
    params = [
        ("date", f"gte.{start_date.isoformat()}"),
        ("date", f"lte.{end_date.isoformat()}"),
    ]
    headers = supabase_headers()
    resp = requests.delete(url, headers=headers, params=params, timeout=60)
    if resp.status_code >= 300:
        raise RuntimeError(f"prices_daily delete failed: {resp.status_code} {resp.text}")


def insert_rows(rows: List[Dict], batch_size: int) -> None:
    if not rows:
        return
    base = supabase_base()
    url = f"{base}/rest/v1/prices_daily"
    headers = supabase_headers()
    headers["Prefer"] = "return=minimal"
    for i in range(0, len(rows), batch_size):
        chunk = rows[i : i + batch_size]
        resp = requests.post(url, headers=headers, json=chunk, timeout=60)
        if resp.status_code >= 300:
            raise RuntimeError(f"prices_daily insert failed: {resp.status_code} {resp.text}")


def main() -> None:
    load_env()
    args = parse_args()
    rows = fetch_prices(args.start_date, args.end_date, args.page_size)
    if not rows:
        print("[done] No rows returned; nothing to clean.")
        return

    canonical: Dict[tuple[str, str], Dict] = {}
    duplicates = 0
    by_date: Dict[str, List[Dict]] = {}
    for row in rows:
        key = (row["date"], row["ticker"])
        if key in canonical:
            duplicates += 1
            continue
        canonical[key] = row
        by_date.setdefault(row["date"], []).append(row)

    min_date = dt.date.fromisoformat(min(by_date))
    max_date = dt.date.fromisoformat(max(by_date))
    print(f"[scan] rows={len(rows)} unique={len(canonical)} duplicates={duplicates}")
    if duplicates == 0:
        print("[done] No duplicates detected.")
        return

    if args.dry_run:
        print("[dry-run] Skipping delete/reinsert.")
        return

    total_inserted = 0
    for chunk_start, chunk_end in iter_date_chunks(min_date, max_date, args.chunk_days):
        delete_range(chunk_start, chunk_end)
        rows_to_insert: List[Dict] = []
        cursor = chunk_start
        while cursor <= chunk_end:
            rows_to_insert.extend(by_date.get(cursor.isoformat(), []))
            cursor += dt.timedelta(days=1)
        insert_rows(rows_to_insert, args.batch_size)
        total_inserted += len(rows_to_insert)
        print(f"[chunk] {chunk_start} -> {chunk_end}: inserted {len(rows_to_insert)} rows")

    print(f"[done] reinserted={total_inserted} duplicates_removed={duplicates}")


if __name__ == "__main__":
    try:
        main()
    except Exception as exc:
        print(f"[fatal] cleanup_prices_duplicates failed: {exc}")
        sys.exit(1)
