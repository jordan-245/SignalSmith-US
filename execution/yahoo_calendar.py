"""Yahoo Finance calendar fetcher (events-of-day).

Pulls daily event calendars from Yahoo Finance and produces a compact summary
focused on potential catalysts:
- Earnings
- Economic events
- Stock splits
- IPO pricing

Why: identify catalysts to inform swing hypotheses and daily trading focus.

Implementation notes:
- Uses the finance.yahoo.com pages that embed `root.App.main = ...` JSON.
- Avoids browser automation.
- Output is written to output/yahoo_calendar/<YYYY-MM-DD>.json for inspection.

Usage:
  ./.venv/bin/python execution/yahoo_calendar.py --day 2026-02-04

"""

from __future__ import annotations

import argparse
import datetime as dt
import json
import os
import re
from pathlib import Path
from typing import Any, Dict, List, Tuple

import requests

BASE = "https://finance.yahoo.com/calendar"
UA = "signalsmith-yahoo-calendar/0.1"


def parse_args() -> argparse.Namespace:
    today = dt.date.today().isoformat()
    p = argparse.ArgumentParser(description="Fetch Yahoo Finance calendar events for a day")
    p.add_argument("--day", default=today, help="YYYY-MM-DD")
    p.add_argument("--max", type=int, default=20, help="Max items per category to include in summary")
    p.add_argument("--out", default=None, help="Optional output path (default: output/yahoo_calendar/<day>.json)")
    return p.parse_args()


def fetch_root_app_main(url: str, retries: int = 2, backoff_s: float = 2.0) -> Dict[str, Any]:
    """Fetch Yahoo page and extract embedded `root.App.main` JSON.

    Yahoo often embeds a huge JSON blob in a script tag. The exact formatting
    varies, so we locate the marker and slice to the first terminating `;\n`.
    """

    last_exc: Exception | None = None
    for attempt in range(1, retries + 2):
        try:
            r = requests.get(url, headers={"User-Agent": UA}, timeout=30)
            if r.status_code in (429, 500, 502, 503, 504):
                raise requests.HTTPError(f"{r.status_code} transient", response=r)
            r.raise_for_status()
            text = r.text

            marker = "root.App.main ="
            i = text.find(marker)
            if i == -1:
                raise RuntimeError(f"root.App.main marker not found (len={len(text)})")

            # Start after marker
            j = i + len(marker)
            # Skip whitespace
            while j < len(text) and text[j] in " \t":
                j += 1

            # Find the end of the JSON assignment.
            end = text.find(";\n", j)
            if end == -1:
                end = text.find(";</script>", j)
            if end == -1:
                # last resort: try a regex across a smaller window
                m = re.search(r"root\.App\.main\s*=\s*(\{.*?\})\s*;", text[j:], re.S)
                if not m:
                    raise RuntimeError("root.App.main JSON terminator not found")
                payload = m.group(1)
            else:
                payload = text[j:end].strip()

            return json.loads(payload)
        except Exception as exc:
            last_exc = exc
            if attempt > retries:
                break
            import time

            time.sleep(backoff_s * attempt)

    raise RuntimeError(f"Failed to fetch/parse root.App.main for {url}: {last_exc}")


def get_store(app: Dict[str, Any]) -> Dict[str, Any]:
    return app.get("context", {}).get("dispatcher", {}).get("stores", {})


def calendar_rows_for(path: str, day: str, offset: int = 0, size: int = 100) -> Tuple[List[Dict[str, Any]], int]:
    url = f"{BASE}/{path}?day={day}&offset={offset}&size={size}"
    app = fetch_root_app_main(url)
    stores = get_store(app)
    total = int(stores.get("ScreenerCriteriaStore", {}).get("meta", {}).get("total", 0) or 0)
    rows = stores.get("ScreenerResultsStore", {}).get("results", {}).get("rows", []) or []
    return rows, total


def fetch_all(path: str, day: str, step: int = 100, cap: int = 500) -> List[Dict[str, Any]]:
    out: List[Dict[str, Any]] = []
    offset = 0
    total_seen = None
    while True:
        rows, total = calendar_rows_for(path, day, offset=offset, size=step)
        if total_seen is None:
            total_seen = total
        out.extend(rows)
        offset += step
        if offset >= total or offset >= cap or not rows:
            break
    return out


def summarize_earnings(rows: List[Dict[str, Any]], max_items: int) -> List[str]:
    lines: List[str] = []
    for r in rows[:max_items]:
        ticker = r.get("ticker") or r.get("symbol") or "?"
        name = r.get("companyshortname") or r.get("shortName") or ""
        when = r.get("startdatetimetype") or r.get("startDateTimeType") or ""
        eps_est = r.get("epsestimate")
        lines.append(f"- {ticker} {f'({name})' if name else ''} {when} eps_est={eps_est}")
    return lines


def summarize_splits(rows: List[Dict[str, Any]], max_items: int) -> List[str]:
    lines: List[str] = []
    for r in rows[:max_items]:
        ticker = r.get("symbol") or r.get("ticker") or "?"
        ratio = r.get("splitRatio") or r.get("splitratio") or ""
        name = r.get("shortName") or r.get("companyName") or ""
        lines.append(f"- {ticker} {f'({name})' if name else ''} split={ratio}")
    return lines


def summarize_ipo(rows: List[Dict[str, Any]], max_items: int) -> List[str]:
    lines: List[str] = []
    for r in rows[:max_items]:
        symbol = r.get("symbol") or "?"
        name = r.get("companyName") or r.get("shortName") or ""
        price = r.get("priceRange") or r.get("price") or ""
        lines.append(f"- {symbol} {f'({name})' if name else ''} price={price}")
    return lines


def summarize_econ(rows: List[Dict[str, Any]], max_items: int) -> List[str]:
    lines: List[str] = []
    for r in rows[:max_items]:
        event = r.get("event") or r.get("eventName") or r.get("name") or "?"
        country = r.get("country") or r.get("countryCode") or ""
        time_ = r.get("time") or r.get("startDateTime") or ""
        impact = r.get("impact") or r.get("importance") or ""
        lines.append(f"- {time_} {country} {event} impact={impact}")
    return lines


def main() -> None:
    args = parse_args()
    day = args.day

    data: Dict[str, Any] = {"day": day, "fetched_at": dt.datetime.now(dt.timezone.utc).isoformat(), "categories": {}}

    cats = {
        "earnings": "earnings",
        "economic": "economic",
        "splits": "splits",
        "ipo": "ipo",
    }

    for k, path in cats.items():
        try:
            rows = fetch_all(path, day)
            data["categories"][k] = {"count": len(rows), "rows": rows}
        except Exception as exc:
            data["categories"][k] = {"count": 0, "rows": [], "error": str(exc)}

    # Write artifact
    out_path = Path(args.out) if args.out else (Path(__file__).resolve().parents[1] / "output" / "yahoo_calendar" / f"{day}.json")
    out_path.parent.mkdir(parents=True, exist_ok=True)
    out_path.write_text(json.dumps(data, indent=2) + "\n", encoding="utf-8")

    # Print compact summary (for cron/Telegram)
    econ = data["categories"].get("economic", {})
    earnings = data["categories"].get("earnings", {})
    splits = data["categories"].get("splits", {})
    ipo = data["categories"].get("ipo", {})

    print(f"[yahoo_calendar] {day} summary")
    print(f"- economic events: {econ.get('count', 0)}")
    print(f"- earnings: {earnings.get('count', 0)}")
    print(f"- splits: {splits.get('count', 0)}")
    print(f"- ipo pricing: {ipo.get('count', 0)}")

    if earnings.get("rows"):
        print("\nEarnings (top):")
        for line in summarize_earnings(earnings["rows"], args.max):
            print(line)

    if econ.get("rows"):
        print("\nEconomic (top):")
        for line in summarize_econ(econ["rows"], args.max):
            print(line)

    if splits.get("rows"):
        print("\nSplits (top):")
        for line in summarize_splits(splits["rows"], args.max):
            print(line)

    if ipo.get("rows"):
        print("\nIPOs (top):")
        for line in summarize_ipo(ipo["rows"], args.max):
            print(line)


if __name__ == "__main__":
    main()
