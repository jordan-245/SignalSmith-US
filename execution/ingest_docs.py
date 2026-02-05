"""
Doc ingestion + cleaning.
- Fetches URLs
- Enforces cutoff (published_at or observed_at <= cutoff)
- Hash-dedupes against docs_raw.content_hash
- Stores raw + cleaned text in Supabase tables: docs_raw, docs_text
"""

from __future__ import annotations

import argparse
import datetime as dt
import hashlib
import json
import os
import time
from email.utils import parsedate_to_datetime
from pathlib import Path
from typing import Dict, List, Tuple
from urllib.parse import urlparse

import requests
from bs4 import BeautifulSoup
from dotenv import load_dotenv
from zoneinfo import ZoneInfo

# User-Agent must be explicit enough for SEC Fair Access guidance.
# Keep it stable and identifiable.
USER_AGENT = "SignalSmith/0.1 (doc-ingest; +https://srv1281557.hstgr.cloud; research bot)"
META_PUBLISHED_KEYS = [
    "article:published_time",
    "article:modified_time",
    "og:published_time",
    "og:updated_time",
    "publication_date",
    "publish-date",
    "pubdate",
    "date",
    "dc.date",
    "dc.date.issued",
]


def parse_args() -> argparse.Namespace:
    today = dt.date.today().isoformat()
    parser = argparse.ArgumentParser(description="Ingest documents and store raw/cleaned text in Supabase.")
    parser.add_argument("--url", action="append", default=[], help="URL to ingest (repeatable).")
    parser.add_argument("--urls-file", help="File with one URL per line.")
    parser.add_argument("--date", default=today, help="Date for cutoff (YYYY-MM-DD).")
    parser.add_argument("--cutoff", default="08:15", help="Cutoff local time (HH:MM).")
    parser.add_argument("--tz", default="America/New_York", help="Timezone for cutoff.")
    parser.add_argument("--max-docs", type=int, default=50, help="Max docs to ingest.")
    parser.add_argument("--timeout", type=int, default=15, help="HTTP timeout seconds.")
    return parser.parse_args()


def load_env() -> None:
    env_path = Path(__file__).resolve().parents[1] / ".env"
    if env_path.exists():
        load_dotenv(env_path)


def build_cutoff(date_str: str, time_str: str, tz_name: str) -> dt.datetime:
    date_part = dt.date.fromisoformat(date_str)
    hour, minute = map(int, time_str.split(":"))
    tz = ZoneInfo(tz_name)
    return dt.datetime.combine(date_part, dt.time(hour=hour, minute=minute, tzinfo=tz))


def gather_urls(args: argparse.Namespace) -> List[str]:
    urls = list(args.url)
    if args.urls_file:
        with open(args.urls_file, "r", encoding="utf-8") as f:
            urls.extend([line.strip() for line in f if line.strip()])
    # de-dupe while preserving order
    seen = set()
    uniq = []
    for u in urls:
        if u not in seen:
            uniq.append(u)
            seen.add(u)
    return uniq[: args.max_docs]


# Conservative per-host throttling to stay scraper-friendly (esp. SEC).
# Single-process, so a simple in-memory timestamp map is enough.
_LAST_REQ_AT: Dict[str, float] = {}


def _min_interval_for_host(host: str) -> float:
    host = (host or "").lower()
    if host.endswith("sec.gov"):
        return 0.75  # ~1.3 rps; stay well under SEC guidance + reduce blocking risk
    return 0.0


def _throttle(url: str) -> None:
    host = urlparse(url).netloc.lower()
    interval = _min_interval_for_host(host)
    if interval <= 0:
        return
    now = time.time()
    last = _LAST_REQ_AT.get(host, 0.0)
    sleep_for = interval - (now - last)
    if sleep_for > 0:
        time.sleep(sleep_for)
    _LAST_REQ_AT[host] = time.time()


def fetch_url_with_retry(url: str, timeout: int, retries: int = 2, backoff: float = 2.0) -> Tuple[bytes, Dict[str, str]]:
    headers = {"User-Agent": USER_AGENT}
    last_exc: Exception | None = None
    for attempt in range(1, retries + 2):
        try:
            _throttle(url)
            resp = requests.get(url, headers=headers, timeout=timeout)
            if resp.status_code in (429,) or resp.status_code >= 500:
                raise requests.HTTPError(f"{resp.status_code} {resp.text}", response=resp)
            resp.raise_for_status()
            ctype = resp.headers.get("Content-Type", "").lower()
            if ctype and not any(t in ctype for t in ["text", "html", "json"]):
                raise ValueError(f"Non-text content type: {ctype}")
            robots = resp.headers.get("X-Robots-Tag", "")
            if robots and any(token in robots.lower() for token in ["noindex", "nofollow"]):
                raise PermissionError(f"Robots policy: {robots}")
            return resp.content, resp.headers
        except Exception as exc:
            last_exc = exc
            if attempt > retries:
                break
            time.sleep(backoff * attempt)
    if last_exc:
        raise last_exc
    raise RuntimeError("Unknown fetch error")


def try_parse_datetime(value: str) -> dt.datetime | None:
    if not value:
        return None
    value = value.strip()
    try:
        clean = value.replace("Z", "+00:00") if value.endswith("Z") else value
        dt_parsed = dt.datetime.fromisoformat(clean)
        if dt_parsed.tzinfo is None:
            dt_parsed = dt_parsed.replace(tzinfo=dt.timezone.utc)
        return dt_parsed
    except Exception:
        pass
    try:
        dt_parsed = parsedate_to_datetime(value)
        if dt_parsed.tzinfo is None:
            dt_parsed = dt_parsed.replace(tzinfo=dt.timezone.utc)
        return dt_parsed
    except Exception:
        return None


def detect_published_at(headers: Dict[str, str], observed_at: dt.datetime, content: bytes | None = None) -> dt.datetime:
    last_mod = headers.get("Last-Modified") or headers.get("last-modified")
    if last_mod:
        parsed = try_parse_datetime(last_mod)
        if parsed:
            return parsed

    if content:
        soup = BeautifulSoup(content, "html.parser")
        for key in META_PUBLISHED_KEYS:
            meta = soup.find("meta", attrs={"property": key}) or soup.find("meta", attrs={"name": key})
            if meta and meta.get("content"):
                parsed = try_parse_datetime(meta["content"])
                if parsed:
                    return parsed
        time_tag = soup.find("time", attrs={"datetime": True})
        if time_tag and time_tag.get("datetime"):
            parsed = try_parse_datetime(time_tag["datetime"])
            if parsed:
                return parsed

    return observed_at


def clean_html(content: bytes) -> str:
    """Extract readable text from HTML.

    Prefers readability-lxml (main-article extraction). Falls back to a simple
    BeautifulSoup text dump.
    """

    # 1) Try readability for higher-signal extraction.
    try:
        from readability import Document  # type: ignore

        # readability expects text input
        doc = Document(content.decode("utf-8", errors="ignore"))
        html = doc.summary(html_partial=True)
        soup = BeautifulSoup(html, "html.parser")
    except Exception:
        # 2) Fallback: full-page text.
        soup = BeautifulSoup(content, "html.parser")

    for script in soup(["script", "style", "noscript"]):
        script.decompose()
    text = soup.get_text(separator="\n")
    lines = [line.strip() for line in text.splitlines()]
    return "\n".join([l for l in lines if l])


def hash_bytes(content: bytes) -> str:
    return hashlib.sha256(content).hexdigest()


def supabase_headers() -> Dict[str, str]:
    supabase_key = os.getenv("SUPABASE_SERVICE_ROLE", "")
    return {
        "apikey": supabase_key,
        "Authorization": f"Bearer {supabase_key}",
        "Content-Type": "application/json",
    }


def supabase_base() -> str:
    base = os.getenv("SUPABASE_URL", "")
    if not base:
        raise RuntimeError("SUPABASE_URL not set")
    return base.rstrip("/")


def fetch_existing_hashes(hashes: List[str]) -> List[str]:
    if not hashes:
        return []
    base = supabase_base()
    url = f"{base}/rest/v1/docs_raw"
    # Build in.(...) list
    in_list = ",".join(hashes)
    params = {"select": "content_hash", "content_hash": f"in.({in_list})"}
    resp = requests.get(url, headers=supabase_headers(), params=params, timeout=10)
    resp.raise_for_status()
    rows = resp.json()
    return [row["content_hash"] for row in rows]


def insert_docs_raw(rows: List[Dict]) -> List[Dict]:
    if not rows:
        return []
    base = supabase_base()
    url = f"{base}/rest/v1/docs_raw"
    headers = supabase_headers()
    headers["Prefer"] = "return=representation"
    resp = requests.post(url, headers=headers, json=rows, timeout=15)
    if resp.status_code >= 300:
        raise RuntimeError(f"docs_raw insert failed: {resp.status_code} {resp.text}")
    return resp.json()


def insert_docs_text(rows: List[Dict]) -> None:
    if not rows:
        return
    base = supabase_base()
    url = f"{base}/rest/v1/docs_text"
    headers = supabase_headers()
    headers["Prefer"] = "return=minimal"
    resp = requests.post(url, headers=headers, json=rows, timeout=15)
    if resp.status_code >= 300:
        raise RuntimeError(f"docs_text insert failed: {resp.status_code} {resp.text}")


def push_pipeline_run(
    run_id: str,
    date_str: str,
    stage: str,
    status: str,
    started_at: dt.datetime,
    ended_at: dt.datetime,
    stats: Dict,
    warnings: List[str],
) -> None:
    supabase_url = os.getenv("SUPABASE_URL")
    supabase_key = os.getenv("SUPABASE_SERVICE_ROLE")
    if not supabase_url or not supabase_key:
        print("[pipeline_run] skipped: missing SUPABASE_URL or SUPABASE_SERVICE_ROLE")
        return
    table = os.getenv("SUPABASE_PIPELINE_TABLE", "pipeline_runs")
    url = f"{supabase_url.rstrip('/')}/rest/v1/{table}"
    payload = {
        "run_id": run_id,
        "tag": "ingest_docs",
        "stage": stage,
        "status": status,
        "date": date_str,
        "started_at": started_at.isoformat(),
        "ended_at": ended_at.isoformat(),
        "stats_json": stats,
        "warnings_json": warnings,
        "val_auc": None,
        "top": None,
        "positions": None,
        "equity": None,
        "report_path": None,
        "missing_tickers": stats.get("errors", []),
    }
    legacy_payload = {
        "run_id": run_id,
        "tag": "ingest_docs",
        "date": date_str,
        "val_auc": None,
        "top": stats,
        "positions": None,
        "equity": None,
        "report_path": None,
        "missing_tickers": stats.get("errors", []),
    }
    headers = {
        "apikey": supabase_key,
        "Authorization": f"Bearer {supabase_key}",
        "Content-Type": "application/json",
        "Prefer": "return=minimal",
    }
    try:
        resp = requests.post(url, headers=headers, json=payload, timeout=10)
        if resp.status_code >= 300:
            print(f"[pipeline_run] insert failed: {resp.status_code} {resp.text}")
            # fallback for older schema without stage/status/timestamps
            if any(marker in resp.text for marker in ["column", "schema cache", "missing", "unknown"]):
                resp2 = requests.post(url, headers=headers, json=legacy_payload, timeout=10)
                if resp2.status_code >= 300:
                    print(f"[pipeline_run] legacy insert failed: {resp2.status_code} {resp2.text}")
                else:
                    print("[pipeline_run] legacy insert ok (schema fallback).")
    except Exception as exc:
        print(f"[pipeline_run] insert error: {exc}")


def main() -> None:
    load_env()
    started_at = dt.datetime.now(dt.timezone.utc)
    run_id = started_at.strftime("%Y%m%d%H%M%S")
    stats = {
        "fetched": 0,
        "skipped_fetch": 0,
        "skipped_cutoff": 0,
        "skipped_content_type": 0,
        "skipped_robots": 0,
        "dedupe_batch": 0,
        "dedupe_remote": 0,
        "inserted": 0,
        "errors": [],
    }
    warnings: List[str] = []
    finished = False

    def finish(status: str) -> None:
        nonlocal finished
        ended_at = dt.datetime.now(dt.timezone.utc)
        push_pipeline_run(
            run_id=run_id,
            date_str=args.date,
            stage="document_ingest",
            status=status,
            started_at=started_at,
            ended_at=ended_at,
            stats=stats,
            warnings=warnings,
        )
        finished = True

    args = parse_args()
    cutoff = build_cutoff(args.date, args.cutoff, args.tz)
    urls = gather_urls(args)
    if not urls:
        warnings.append("No URLs provided.")
        finish("noop")
        return

    try:
        candidates = []
        for url in urls:
            try:
                content, headers = fetch_url_with_retry(url, timeout=args.timeout)
            except Exception as exc:
                print(f"[skip] {url} fetch error: {exc}")
                if isinstance(exc, PermissionError):
                    stats["skipped_robots"] += 1
                elif "Non-text content type" in str(exc):
                    stats["skipped_content_type"] += 1
                else:
                    stats["skipped_fetch"] += 1
                stats["errors"].append({"url": url, "reason": str(exc)})
                continue
            stats["fetched"] += 1
            observed_at = dt.datetime.now(dt.timezone.utc)
            published_at = detect_published_at(headers, observed_at, content)
            if published_at > cutoff.astimezone(published_at.tzinfo or dt.timezone.utc):
                print(f"[skip] {url} published_at {published_at} after cutoff {cutoff}")
                stats["skipped_cutoff"] += 1
                continue
            content_hash = hash_bytes(content)
            candidates.append(
                {
                    "url": url,
                    "source": urlparse(url).netloc,
                    "published_at": published_at.isoformat(),
                    "observed_at": observed_at.isoformat(),
                    "content_type": headers.get("Content-Type"),
                    "content_hash": content_hash,
                    "raw_content": content.decode("utf-8", errors="replace"),
                    "status": "ingested",
                    "cleaned_text": clean_html(content),
                }
            )

        # De-dupe within batch
        unique = {}
        for row in candidates:
            if row["content_hash"] not in unique:
                unique[row["content_hash"]] = row
            else:
                stats["dedupe_batch"] += 1
        rows = list(unique.values())

        if not rows:
            print("[done] No docs after fetch/cutoff/dedupe.")
            finish("noop")
            return

        # Check existing in Supabase
        try:
            existing = set(fetch_existing_hashes([r["content_hash"] for r in rows]))
        except Exception as exc:
            warnings.append(f"Failed to check existing hashes: {exc}")
            finish("error")
            raise

        new_rows = [r for r in rows if r["content_hash"] not in existing]
        stats["dedupe_remote"] = len(rows) - len(new_rows)
        if not new_rows:
            print("[done] All docs already ingested (hash match).")
            finish("noop")
            return

        try:
            inserted_raw = insert_docs_raw(
                [
                    {
                        "url": r["url"],
                        "source": r["source"],
                        "published_at": r["published_at"],
                        "observed_at": r["observed_at"],
                        "content_type": r["content_type"],
                        "content_hash": r["content_hash"],
                        "raw_content": r["raw_content"],
                        "status": r["status"],
                    }
                    for r in new_rows
                ]
            )
        except Exception as exc:
            warnings.append(str(exc))
            finish("error")
            raise

        try:
            insert_docs_text(
                [
                    {
                        "doc_id": raw["doc_id"],
                        "cleaned_text": unique[raw["content_hash"]]["cleaned_text"],
                        "language": None,
                        "text_hash": hash_bytes(unique[raw["content_hash"]]["cleaned_text"].encode("utf-8")),
                        "status": "cleaned",
                    }
                    for raw in inserted_raw
                ]
            )
        except Exception as exc:
            warnings.append(str(exc))
            finish("error")
            raise

        stats["inserted"] = len(inserted_raw)
        print(f"[done] Inserted {len(inserted_raw)} docs.")
        finish("success")
    except Exception as exc:
        warnings.append(str(exc))
        if not finished:
            try:
                finish("error")
            except Exception as push_exc:
                print(f"[pipeline_run] log failed: {push_exc}")
        raise


if __name__ == "__main__":
    try:
        main()
    except Exception as exc:
        print(f"[fatal] ingest_docs failed: {exc}")
        raise
