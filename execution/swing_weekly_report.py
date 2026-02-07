"""Weekly Swing Book health + performance report (deterministic).

Goal: observability without changing trading logic.

Reads Supabase:
- paper_equity_curve
- paper_positions
- paper_orders

Produces a Telegram message with:
- last 5 trading days equity change
- worst day, best day
- current drawdown
- current exposure (invested vs cash)
- turnover proxy (order count)
- any pauses triggered (from output/state/trading_pause.json)

Usage:
  ./.venv/bin/python -u execution/swing_weekly_report.py --lookback-sessions 5

"""

from __future__ import annotations

import argparse
import datetime as dt
import json
import os
from pathlib import Path
from typing import Dict, List, Tuple

import pandas as pd
import requests
from dotenv import load_dotenv

from telegram_fmt import send_telegram

REPO = Path(__file__).resolve().parents[1]
DEFAULT_PORTFOLIO_ID = os.getenv("SWING_PORTFOLIO_ID", "swing")


def load_env() -> None:
    env_path = REPO / ".env"
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
    return {"apikey": key, "Authorization": f"Bearer {key}", "Content-Type": "application/json"}


def fetch_equity_curve(portfolio_id: str, limit: int = 30) -> List[Dict]:
    base = supabase_base()
    url = f"{base}/rest/v1/paper_equity_curve"
    params = [
        ("select", "date,equity,cash,drawdown"),
        ("portfolio_id", f"eq.{portfolio_id}"),
        ("order", "date.desc"),
        ("limit", str(limit)),
    ]
    r = requests.get(url, headers=supabase_headers(), params=params, timeout=25)
    if r.status_code >= 300:
        raise RuntimeError(f"paper_equity_curve fetch failed: {r.status_code} {r.text}")
    return r.json() or []


def fetch_positions_latest(portfolio_id: str) -> List[Dict]:
    base = supabase_base()
    url = f"{base}/rest/v1/paper_positions"
    # get latest date for portfolio
    p1 = [
        ("select", "date"),
        ("portfolio_id", f"eq.{portfolio_id}"),
        ("order", "date.desc"),
        ("limit", "1"),
    ]
    r1 = requests.get(url, headers=supabase_headers(), params=p1, timeout=25)
    if r1.status_code >= 300 or not (r1.json() or []):
        return []
    last_date = (r1.json() or [])[0]["date"]

    p2 = [
        ("select", "ticker,qty,market_value,avg_cost"),
        ("portfolio_id", f"eq.{portfolio_id}"),
        ("date", f"eq.{last_date}"),
        ("order", "market_value.desc"),
    ]
    r2 = requests.get(url, headers=supabase_headers(), params=p2, timeout=25)
    if r2.status_code >= 300:
        return []
    rows = r2.json() or []
    # keep only open positions
    out = [x for x in rows if float(x.get("qty") or 0) > 0]
    return out


def fetch_orders(portfolio_id: str, since_date: str) -> List[Dict]:
    # NOTE: paper_orders currently has no portfolio_id, so we approximate by date filter only.
    base = supabase_base()
    url = f"{base}/rest/v1/paper_orders"
    params = [
        ("select", "date,ticker,side,order_id"),
        ("date", f"gte.{since_date}"),
        ("order", "date.desc"),
        ("limit", "2000"),
    ]
    r = requests.get(url, headers=supabase_headers(), params=params, timeout=25)
    if r.status_code >= 300:
        return []
    return r.json() or []


def read_pause_state() -> Dict:
    p = REPO / "output" / "state" / "trading_pause.json"
    if not p.exists():
        return {}
    try:
        return json.loads(p.read_text(encoding="utf-8"))
    except Exception:
        return {}


def compute_session_returns(curve_rows: List[Dict]) -> pd.DataFrame:
    if not curve_rows:
        return pd.DataFrame()
    df = pd.DataFrame(curve_rows)
    df["date"] = pd.to_datetime(df["date"])
    df = df.sort_values("date")
    df["equity"] = pd.to_numeric(df["equity"], errors="coerce")
    df["cash"] = pd.to_numeric(df.get("cash"), errors="coerce")
    df["drawdown"] = pd.to_numeric(df.get("drawdown"), errors="coerce")
    df["ret"] = df["equity"].pct_change()
    return df


def main() -> None:
    load_env()
    ap = argparse.ArgumentParser()
    ap.add_argument("--lookback-sessions", type=int, default=5)
    ap.add_argument("--portfolio-id", default=DEFAULT_PORTFOLIO_ID)
    args = ap.parse_args()

    curve = fetch_equity_curve(args.portfolio_id, limit=max(15, args.lookback_sessions + 10))
    df = compute_session_returns(curve)
    if df.empty or df["equity"].dropna().empty:
        print("HEARTBEAT_OK")
        return

    # last N sessions
    tail = df.dropna(subset=["equity"]).tail(args.lookback_sessions)
    if tail.empty:
        print("HEARTBEAT_OK")
        return

    start_eq = float(tail["equity"].iloc[0])
    end_eq = float(tail["equity"].iloc[-1])
    chg = (end_eq / start_eq - 1.0) if start_eq else 0.0

    # daily best/worst
    rets = tail["ret"].dropna()
    worst = rets.min() if not rets.empty else None
    best = rets.max() if not rets.empty else None

    dd_now = float(df["drawdown"].dropna().iloc[-1]) if not df["drawdown"].dropna().empty else None
    cash_now = float(df["cash"].dropna().iloc[-1]) if not df["cash"].dropna().empty else None

    positions = fetch_positions_latest(args.portfolio_id)
    invested = float(sum(float(p.get("market_value") or 0.0) for p in positions))

    # orders since first day in tail
    since_date = tail["date"].iloc[0].date().isoformat()
    orders = fetch_orders(args.portfolio_id, since_date)
    order_count = len(orders)

    pause = read_pause_state()
    paused = bool(pause.get("paused"))
    pause_kind = pause.get("kind")
    pause_detail = pause.get("detail")

    lines = [f"Swing weekly check — last {args.lookback_sessions} sessions", ""]
    lines.append(f"- Equity: {start_eq:,.2f} → {end_eq:,.2f} ({chg:+.1%})")
    if worst is not None and best is not None:
        lines.append(f"- Best day: {float(best):+.1%} · Worst day: {float(worst):+.1%}")
    if dd_now is not None:
        lines.append(f"- Drawdown now: {dd_now:+.1%}")
    if cash_now is not None:
        gross = invested + cash_now
        exp = invested / gross if gross else 0.0
        lines.append(f"- Exposure: invested={invested:,.2f} · cash={cash_now:,.2f} · invested%={exp:.0%}")
    lines.append(f"- Orders (since {since_date}): {order_count}")

    if positions:
        top = ", ".join([f"{p.get('ticker')}({float(p.get('market_value') or 0):,.0f})" for p in positions[:6]])
        lines.append(f"- Positions: {len(positions)} · top: {top}")

    if paused:
        lines.append("")
        lines.append(f"- PAUSED: {pause_kind or 'unknown'}")
        if pause_detail:
            lines.append(f"  - {pause_detail}")

    send_telegram("\n".join(lines))
    print("HEARTBEAT_OK")


if __name__ == "__main__":
    main()
