"""
Pre-open pipeline orchestrator.

Runs (in order):
- ingest_docs (optional)
- llm_extract (optional)
- ingest_prices
- build_features
- run_model
- paper_trade
"""

from __future__ import annotations

import argparse
import datetime as dt
import os
import subprocess
import sys
import time
from pathlib import Path
from typing import List, Tuple


def parse_args() -> argparse.Namespace:
    today = dt.date.today().isoformat()
    parser = argparse.ArgumentParser(description="Run the pre-open pipeline in sequence.")
    parser.add_argument("--date", default=today, help="Target date YYYY-MM-DD (default: today).")
    parser.add_argument("--cutoff", default="08:15", help="Cutoff local time for docs (HH:MM).")
    parser.add_argument("--tz", default="America/New_York", help="Timezone for doc cutoff.")
    parser.add_argument("--url", action="append", default=[], help="URL to ingest (repeatable).")
    parser.add_argument(
        "--urls-file",
        default=os.getenv("DOC_URLS_FILE"),
        help="File with one URL per line for ingest_docs (or set DOC_URLS_FILE).",
    )
    parser.add_argument("--max-docs", type=int, default=50, help="Max docs to ingest.")
    parser.add_argument("--skip-news", action="store_true", help="Skip ingest_docs and llm_extract.")
    parser.add_argument("--dry-run", action="store_true", help="Pass dry-run to supported steps.")
    parser.add_argument("--continue-on-error", action="store_true", help="Continue running steps after failures.")
    return parser.parse_args()


def run_step(name: str, cmd: List[str]) -> Tuple[bool, float, str]:
    started = time.time()
    try:
        subprocess.run(cmd, check=True)
        return True, time.time() - started, ""
    except subprocess.CalledProcessError as exc:
        return False, time.time() - started, f"{exc}"


def market_is_open(date_str: str, calendar: str = "XNYS") -> bool:
    """Return True if the market is scheduled to be open on the given date.

    Uses exchange-calendars when available (covers weekends + US holidays).
    Falls back to weekday-only if the dependency isn't installed.

    calendar: default XNYS (NYSE). For NASDAQ use XNAS.
    """

    try:
        import exchange_calendars as xcals  # type: ignore

        cal = xcals.get_calendar(calendar)
        # is_session accepts YYYY-MM-DD
        return bool(cal.is_session(date_str))
    except Exception:
        # Conservative fallback: weekdays only.
        d = dt.date.fromisoformat(date_str)
        return d.weekday() < 5


def main() -> None:
    args = parse_args()
    if os.getenv("SKIP_NEWS") == "1":
        args.skip_news = True

    # Skip on non-trading days (weekends/holidays) so cron can run daily safely.
    if not market_is_open(args.date):
        print(f"[preopen_run] Market closed on {args.date}; skipping.")
        return

    py = sys.executable
    base = Path(__file__).resolve().parents[1]
    steps: List[Tuple[str, List[str]]] = []

    if not args.skip_news:
        if args.urls_file or args.url:
            cmd = [
                py,
                str(base / "execution" / "ingest_docs.py"),
                "--date",
                args.date,
                "--cutoff",
                args.cutoff,
                "--tz",
                args.tz,
                "--max-docs",
                str(args.max_docs),
            ]
            if args.urls_file:
                cmd += ["--urls-file", args.urls_file]
            for u in args.url:
                cmd += ["--url", u]
            steps.append(("ingest_docs", cmd))
        steps.append(("llm_extract", [py, str(base / "execution" / "llm_extract.py")]))

    prices_cmd = [py, str(base / "execution" / "ingest_prices.py"), "--date", args.date]
    if args.dry_run:
        prices_cmd.append("--dry-run")
    steps.append(("ingest_prices", prices_cmd))

    features_cmd = [py, str(base / "execution" / "build_features.py"), "--end-date", args.date]
    if args.dry_run:
        features_cmd.append("--dry-run")
    steps.append(("build_features", features_cmd))

    model_cmd = [py, str(base / "execution" / "run_model.py"), "--score-date", args.date]
    if args.dry_run:
        model_cmd.append("--dry-run")
    steps.append(("run_model", model_cmd))

    trade_cmd = [py, str(base / "execution" / "paper_trade.py"), "--date", args.date]
    if args.dry_run:
        trade_cmd.append("--dry-run")
    steps.append(("paper_trade", trade_cmd))

    results = []
    for name, cmd in steps:
        ok, elapsed, err = run_step(name, cmd)
        results.append((name, ok, elapsed, err))
        if not ok and not args.continue_on_error:
            break

    print("[preopen_run] Summary:")
    for name, ok, elapsed, err in results:
        status = "ok" if ok else "error"
        print(f"- {name}: {status} ({elapsed:.1f}s)")
        if err:
            print(f"  {err}")

    failures = [r for r in results if not r[1]]
    if failures:
        raise SystemExit(1)


if __name__ == "__main__":
    main()
