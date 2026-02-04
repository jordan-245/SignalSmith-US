"""Daily event brief (Yahoo calendar-inspired).

Yahoo Finance calendar pages are increasingly JS/API-driven and can be hard to
scrape reliably without a browser/crumb.

This script provides a practical replacement using *free Yahoo data*:
- Pulls calendar *counts* from the AU Yahoo calendar landing page (server-rendered).
- Flags likely catalysts (earnings) for a focused ticker set by querying the
  per-ticker Yahoo calendar via yfinance.

Focused ticker set (v0):
- Current swing book holdings (latest paper_positions for portfolio_id=swing)
- Current model book holdings (portfolio_id=default)
- Commodity proxies used by swing book

Output:
- Prints a concise brief (for OpenClaw cron + Telegram delivery)

"""

from __future__ import annotations

import argparse
import datetime as dt
import io
import os
import re
from contextlib import redirect_stderr, redirect_stdout
from pathlib import Path
from typing import Dict, List, Optional, Set

import pandas as pd
import requests
import yfinance as yf
from dotenv import load_dotenv

UA = "signalsmith-day-brief/0.1"
AU_CAL = "https://au.finance.yahoo.com/calendar?day={day}"

PROXIES = ["SPY", "GLD", "SLV", "GDX", "GDXJ", "USO", "UNG", "XLE", "OIH", "DBC", "DBA"]


def parse_args() -> argparse.Namespace:
    today = dt.date.today().isoformat()
    p = argparse.ArgumentParser(description="Daily event brief")
    p.add_argument("--day", default=today, help="YYYY-MM-DD")
    p.add_argument("--max", type=int, default=25, help="Max tickers to check for earnings")
    p.add_argument("--portfolio", action="append", default=["default", "swing"], help="paper portfolio_id to include")
    return p.parse_args()


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


def fetch_latest_positions(portfolio_id: str, before_date: str) -> List[str]:
    base = supabase_base()
    url = f"{base}/rest/v1/paper_positions"

    # Find most recent date
    params1 = [("select", "date"), ("portfolio_id", f"eq.{portfolio_id}"), ("date", f"lt.{before_date}"), ("order", "date.desc"), ("limit", "1")]
    r1 = requests.get(url, headers=supabase_headers(), params=params1, timeout=15)
    if r1.status_code >= 300:
        return []
    rows = r1.json()
    if not rows:
        return []
    last_date = rows[0]["date"]

    params2 = [
        ("select", "ticker,qty"),
        ("portfolio_id", f"eq.{portfolio_id}"),
        ("date", f"eq.{last_date}"),
        ("order", "ticker.asc"),
    ]
    r2 = requests.get(url, headers=supabase_headers(), params=params2, timeout=15)
    if r2.status_code >= 300:
        return []
    tickers = []
    for row in r2.json():
        try:
            if float(row.get("qty") or 0) > 0:
                tickers.append(row["ticker"])
        except Exception:
            continue
    return tickers


def yahoo_calendar_counts(day: str) -> Dict[str, int]:
    url = AU_CAL.format(day=day)
    r = requests.get(url, headers={"User-Agent": UA}, timeout=30)
    r.raise_for_status()
    html = r.text

    def find(label: str) -> int:
        # Matches like: "[4 Earnings]" or "4 Earnings"
        m = re.search(rf"(\d+)\s+{re.escape(label)}", html, re.I)
        return int(m.group(1)) if m else 0

    return {
        "economic": find("Economic events"),
        "earnings": find("Earnings"),
        "splits": find("Stock splits"),
        "ipo": find("IPO pricing"),
    }


def next_earnings_date(ticker: str) -> Optional[dt.date]:
    """Best-effort next earnings date from yfinance.

    yfinance can be noisy on missing fundamentals; suppress stdout/stderr.
    """

    try:
        with redirect_stdout(io.StringIO()), redirect_stderr(io.StringIO()):
            cal = yf.Ticker(ticker).calendar
        if cal is None or getattr(cal, "empty", False):
            return None
        if "Earnings Date" in cal.index:
            val = cal.loc["Earnings Date"].iloc[0]
        else:
            val = cal.iloc[0, 0]
        ts = pd.to_datetime(val)
        if pd.isna(ts):
            return None
        return ts.date()
    except Exception:
        return None


def main() -> None:
    load_env()
    args = parse_args()
    day = args.day

    # Build focused ticker set
    tickers: Set[str] = set(PROXIES)
    for pid in args.portfolio:
        for t in fetch_latest_positions(pid, day):
            tickers.add(t)

    tickers_list = sorted(tickers)

    # Limit to avoid hammering Yahoo
    tickers_list = tickers_list[: args.max]

    counts = {}
    try:
        counts = yahoo_calendar_counts(day)
    except Exception as exc:
        counts = {"error": 1}
        print(f"[warn] yahoo calendar counts fetch failed: {exc}")

    earnings_today: List[str] = []
    for t in tickers_list:
        ed = next_earnings_date(t)
        if ed and ed.isoformat() == day:
            earnings_today.append(t)

    print(f"[day_brief] {day}")
    if "error" not in counts:
        print(f"Yahoo calendar counts: earnings={counts['earnings']} economic={counts['economic']} splits={counts['splits']} ipo={counts['ipo']}")
    else:
        print("Yahoo calendar counts: unavailable")

    if earnings_today:
        print("Earnings today (focused set): " + ", ".join(sorted(earnings_today)))
    else:
        print("Earnings today (focused set): none detected")

    print("Focused tickers checked: " + ", ".join(tickers_list))


if __name__ == "__main__":
    main()
