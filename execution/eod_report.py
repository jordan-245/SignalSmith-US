"""
End-of-day report for paper portfolio stored in Supabase.
Fetches latest equity + positions and prints a summary.
"""

from __future__ import annotations

import argparse
import datetime as dt
import os
from pathlib import Path
from typing import Dict, List

import requests
from dotenv import load_dotenv

DEFAULT_PORTFOLIO_ID = "default"


def parse_args() -> argparse.Namespace:
    today = dt.date.today().isoformat()
    parser = argparse.ArgumentParser(description="Generate EOD report from Supabase paper trading tables.")
    parser.add_argument("--date", default=today, help="Report date YYYY-MM-DD (default: today).")
    parser.add_argument("--portfolio-id", default=DEFAULT_PORTFOLIO_ID, help="Paper portfolio id.")
    parser.add_argument("--positions-limit", type=int, default=20, help="Max positions to include.")
    parser.add_argument("--output", default=None, help="Optional markdown output path.")
    parser.add_argument("--notify-telegram", action="store_true", help="Send Telegram summary.")
    return parser.parse_args()


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


def fetch_equity(date_str: str, portfolio_id: str) -> Dict | None:
    base = supabase_base()
    url = f"{base}/rest/v1/paper_equity_curve"
    params = {
        "select": "date,portfolio_id,equity,cash,drawdown,turnover",
        "date": f"eq.{date_str}",
        "portfolio_id": f"eq.{portfolio_id}",
        "limit": 1,
    }
    resp = requests.get(url, headers=supabase_headers(), params=params, timeout=15)
    if resp.status_code >= 300:
        raise RuntimeError(f"paper_equity_curve fetch failed: {resp.status_code} {resp.text}")
    rows = resp.json()
    if rows:
        return rows[0]
    params = {
        "select": "date,portfolio_id,equity,cash,drawdown,turnover",
        "portfolio_id": f"eq.{portfolio_id}",
        "order": "date.desc",
        "limit": 1,
    }
    resp = requests.get(url, headers=supabase_headers(), params=params, timeout=15)
    if resp.status_code >= 300:
        raise RuntimeError(f"paper_equity_curve fetch failed: {resp.status_code} {resp.text}")
    rows = resp.json()
    return rows[0] if rows else None


def fetch_positions(date_str: str, portfolio_id: str, limit: int) -> List[Dict]:
    base = supabase_base()
    url = f"{base}/rest/v1/paper_positions"
    params = {
        "select": "ticker,qty,avg_cost,market_value,entry_date,eligible_sell_date",
        "date": f"eq.{date_str}",
        "portfolio_id": f"eq.{portfolio_id}",
        "order": "market_value.desc",
        "limit": limit,
    }
    resp = requests.get(url, headers=supabase_headers(), params=params, timeout=15)
    if resp.status_code >= 300:
        raise RuntimeError(f"paper_positions fetch failed: {resp.status_code} {resp.text}")
    return resp.json()


def send_telegram(text: str) -> None:
    bot_token = os.getenv("TELEGRAM_BOT_TOKEN", "")
    chat_id = os.getenv("TELEGRAM_CHAT_ID", "")
    if not bot_token or not chat_id:
        return
    url = f"https://api.telegram.org/bot{bot_token}/sendMessage"
    try:
        resp = requests.post(url, json={"chat_id": chat_id, "text": text}, timeout=10)
        if resp.status_code >= 300:
            print(f"[telegram] send failed: {resp.status_code} {resp.text}")
    except Exception as exc:
        print(f"[telegram] send error: {exc}")


def format_summary(date_str: str, equity_row: Dict | None, positions: List[Dict]) -> str:
    if not equity_row:
        return f"[eod_report] No equity data found for {date_str}."
    equity = equity_row.get("equity")
    cash = equity_row.get("cash")
    drawdown = equity_row.get("drawdown")
    turnover = equity_row.get("turnover")
    lines = [
        f"EOD Report ({equity_row.get('date', date_str)})",
        f"Equity: {equity}",
        f"Cash: {cash}",
        f"Drawdown: {drawdown}",
        f"Turnover: {turnover}",
    ]
    if positions:
        lines.append("Top Positions:")
        for row in positions[:5]:
            lines.append(f"- {row.get('ticker')} | qty {row.get('qty')} | mv {row.get('market_value')}")
    return "\n".join(lines)


def write_markdown(path: Path, equity_row: Dict | None, positions: List[Dict]) -> None:
    if not equity_row:
        content = "# EOD Report\n\nNo equity data found.\n"
        path.write_text(content, encoding="utf-8")
        return
    date_str = equity_row.get("date", "")
    lines = [
        f"# EOD Report ({date_str})",
        "",
        f"- Equity: {equity_row.get('equity')}",
        f"- Cash: {equity_row.get('cash')}",
        f"- Drawdown: {equity_row.get('drawdown')}",
        f"- Turnover: {equity_row.get('turnover')}",
        "",
        "| Ticker | Qty | Avg Cost | Market Value | Entry Date | Eligible Sell |",
        "| --- | --- | --- | --- | --- | --- |",
    ]
    for row in positions:
        lines.append(
            "| {ticker} | {qty} | {avg_cost} | {market_value} | {entry_date} | {eligible_sell_date} |".format(
                ticker=row.get("ticker"),
                qty=row.get("qty"),
                avg_cost=row.get("avg_cost"),
                market_value=row.get("market_value"),
                entry_date=row.get("entry_date"),
                eligible_sell_date=row.get("eligible_sell_date"),
            )
        )
    path.write_text("\n".join(lines) + "\n", encoding="utf-8")


def main() -> None:
    load_env()
    args = parse_args()
    equity_row = fetch_equity(args.date, args.portfolio_id)
    if equity_row is None:
        print(f"[eod_report] No equity data found for portfolio={args.portfolio_id}.")
        return
    positions = fetch_positions(equity_row.get("date", args.date), args.portfolio_id, args.positions_limit)
    summary = format_summary(args.date, equity_row, positions)
    print(summary)
    if args.output:
        write_markdown(Path(args.output), equity_row, positions)
    if args.notify_telegram:
        send_telegram(summary)


if __name__ == "__main__":
    main()
