"""RSS feed ingestion.

Discovers article URLs from RSS/Atom feeds and hands them to ingest_docs.py for
fetch+clean+Supabase storage.

Design goals:
- Free sources: RSS/Atom
- Safe-ish: rate limiting is handled in ingest_docs; RSS stage just discovers URLs
- Idempotent-ish: ingest_docs content-hash dedupe prevents duplicate storage

Typical usage:
  python execution/ingest_rss.py --feeds-file directives/rss_sources.txt --date 2026-02-04 --cutoff 08:15 --tz America/New_York

Ad-hoc:
  python execution/ingest_rss.py --feed https://example.com/rss.xml
"""

from __future__ import annotations

import argparse
import datetime as dt
import os
import subprocess
import sys
import tempfile
from pathlib import Path
from typing import List
from urllib.parse import urlparse

import feedparser
import requests

from journal import journal_run, journal_watch


def parse_args() -> argparse.Namespace:
    today = dt.date.today().isoformat()
    p = argparse.ArgumentParser(description="Discover RSS/Atom URLs and pass them to ingest_docs.py")
    p.add_argument("--feed", action="append", default=[], help="RSS/Atom feed URL (repeatable)")
    p.add_argument("--feeds-file", default=str(Path(__file__).resolve().parents[1] / "directives" / "rss_sources.txt"))
    p.add_argument("--date", default=today, help="Date for cutoff (YYYY-MM-DD)")
    p.add_argument("--cutoff", default="08:15", help="Cutoff local time (HH:MM)")
    p.add_argument("--tz", default="America/New_York", help="Timezone for cutoff")
    p.add_argument("--max-items", type=int, default=50, help="Max discovered items to attempt")
    p.add_argument("--timeout", type=int, default=15, help="Feed fetch timeout seconds")
    return p.parse_args()


def load_feeds(args: argparse.Namespace) -> List[str]:
    feeds = list(args.feed)
    fpath = Path(args.feeds_file)
    if fpath.exists():
        for line in fpath.read_text(encoding="utf-8").splitlines():
            s = line.strip()
            if not s or s.startswith("#"):
                continue
            # Allow inline comments after a URL.
            if "#" in s:
                s = s.split("#", 1)[0].strip()
            if s:
                feeds.append(s)
    # de-dupe
    uniq: List[str] = []
    seen = set()
    for u in feeds:
        if u not in seen:
            uniq.append(u)
            seen.add(u)
    return uniq


def discover_urls(feed_url: str, timeout: int) -> List[str]:
    """Fetch + parse an RSS/Atom feed with a real timeout.

    feedparser's built-in URL fetching can hang depending on the environment;
    we fetch with requests (timeout) then parse the content.

    Includes light retries for flaky endpoints (e.g., Nasdaq).
    """

    def _timeout_for(url: str) -> int:
        host = urlparse(url).netloc.lower()
        if host.endswith("nasdaq.com"):
            return max(timeout, 30)
        if host.endswith("sec.gov"):
            return max(timeout, 30)
        return timeout

    ua = {"User-Agent": "SignalSmith/0.1 (rss-discovery; +https://srv1281557.hstgr.cloud; research bot)"}

    last_exc: Exception | None = None
    for attempt in range(1, 3 + 1):
        try:
            t = _timeout_for(feed_url)
            resp = requests.get(feed_url, headers=ua, timeout=t)
            resp.raise_for_status()
            parsed = feedparser.parse(resp.content)

            urls: List[str] = []
            for e in parsed.entries or []:
                link = getattr(e, "link", None) or None
                if not link:
                    continue
                if link not in urls:
                    urls.append(link)
            return urls
        except Exception as exc:
            last_exc = exc
            # simple backoff
            if attempt < 3:
                import time

                time.sleep(1.5 * attempt)

    raise last_exc or RuntimeError("Failed to fetch feed")


def main() -> None:
    args = parse_args()
    feeds = load_feeds(args)
    if not feeds:
        print("[rss] No feeds configured.")
        return

    urls: List[str] = []
    feed_failures = 0
    for f in feeds:
        try:
            for u in discover_urls(f, args.timeout):
                if u not in urls:
                    urls.append(u)
        except Exception as exc:
            feed_failures += 1
            print(f"[rss] feed failed: {f} ({exc})")

    if not urls:
        journal_run("ingest_rss", "ok", f"feeds={len(feeds)} urls=0 failures={feed_failures}")
        if feed_failures:
            journal_watch(f"ingest_rss feed failures={feed_failures}")
        print("[rss] No URLs discovered.")
        return

    urls = urls[: args.max_items]
    with tempfile.NamedTemporaryFile("w", delete=False, encoding="utf-8") as tf:
        for u in urls:
            tf.write(u + "\n")
        tmp_path = tf.name

    # Hand off to ingest_docs for actual fetching/cleaning/storage.
    repo = Path(__file__).resolve().parents[1]
    python_bin = os.getenv("PYTHON") or sys.executable
    cmd = [
        python_bin,
        str(repo / "execution" / "ingest_docs.py"),
        "--urls-file",
        tmp_path,
        "--date",
        args.date,
        "--cutoff",
        args.cutoff,
        "--tz",
        args.tz,
        "--max-docs",
        str(args.max_items),
    ]
    print(f"[rss] Discovered {len(urls)} URL(s); invoking ingest_docs.py")
    rc = subprocess.run(cmd, check=False).returncode
    journal_run("ingest_rss", "ok" if rc == 0 else "warn", f"feeds={len(feeds)} urls={len(urls)} failures={feed_failures} rc={rc}")
    if feed_failures or rc != 0:
        journal_watch(f"ingest_rss had issues: feed_failures={feed_failures} rc={rc}")


if __name__ == "__main__":
    main()
