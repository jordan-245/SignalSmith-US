"""
Paper trading using model predictions and daily prices.
- Loads predictions from Supabase for a given date
- Allocates equal weight across Top N picks
- Computes positions and equity snapshot
- Logs results to pipeline_runs (stage=paper_broker)
"""

from __future__ import annotations

import argparse
import datetime as dt
import math
import os
import sys
from pathlib import Path
from typing import Dict, List

import pandas as pd
import requests
from dotenv import load_dotenv

DEFAULT_CASH = 5_000.0
DEFAULT_TOP_N = 10
DEFAULT_HORIZON = 5
DEFAULT_FEES_BPS = 2
DEFAULT_SLIPPAGE_BPS = 5
DEFAULT_MIN_HOLD_DAYS = 5


def load_env() -> None:
    env_path = Path(__file__).resolve().parents[1] / ".env"
    if env_path.exists():
        load_dotenv(env_path)


def parse_args() -> argparse.Namespace:
    today = dt.date.today().isoformat()
    parser = argparse.ArgumentParser(description="Paper trade Top N predictions for a given date.")
    parser.add_argument("--date", default=today, help="Trade date YYYY-MM-DD (default: today).")
    parser.add_argument("--model-run-id", default=None, help="Optional model_run_id (defaults to latest).")
    parser.add_argument("--horizon-days", type=int, default=DEFAULT_HORIZON, help="Prediction horizon filter.")
    parser.add_argument("--top-n", type=int, default=DEFAULT_TOP_N, help="Number of positions.")
    parser.add_argument("--cash", type=float, default=DEFAULT_CASH, help="Starting cash.")
    parser.add_argument("--fees-bps", type=float, default=DEFAULT_FEES_BPS, help="Fee bps applied to notional.")
    parser.add_argument("--slippage-bps", type=float, default=DEFAULT_SLIPPAGE_BPS, help="Slippage bps applied to notional.")
    parser.add_argument("--min-hold-days", type=int, default=DEFAULT_MIN_HOLD_DAYS, help="Min hold in business days.")
    parser.add_argument("--dry-run", action="store_true", help="Compute without writing to Supabase.")
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


def fetch_latest_model_run(horizon_days: int) -> str:
    base = supabase_base()
    url = f"{base}/rest/v1/model_runs"
    params = {
        "select": "model_run_id,created_at",
        "horizon_days": f"eq.{horizon_days}",
        "order": "created_at.desc",
        "limit": 1,
    }
    resp = requests.get(url, headers=supabase_headers(), params=params, timeout=15)
    if resp.status_code >= 300:
        raise RuntimeError(f"model_runs fetch failed: {resp.status_code} {resp.text}")
    rows = resp.json()
    if not rows:
        raise RuntimeError("No model_runs found for horizon.")
    return rows[0]["model_run_id"]


def fetch_predictions(model_run_id: str, date_str: str, horizon_days: int, top_n: int) -> List[Dict]:
    base = supabase_base()
    url = f"{base}/rest/v1/predictions"
    params = {
        "select": "ticker,score,rank",
        "model_run_id": f"eq.{model_run_id}",
        "date": f"eq.{date_str}",
        "horizon_days": f"eq.{horizon_days}",
        "order": "score.desc",
        "limit": top_n,
    }
    resp = requests.get(url, headers=supabase_headers(), params=params, timeout=15)
    if resp.status_code >= 300:
        raise RuntimeError(f"predictions fetch failed: {resp.status_code} {resp.text}")
    return resp.json()


def fetch_prices(date_str: str, tickers: List[str]) -> Dict[str, float]:
    if not tickers:
        return {}
    base = supabase_base()
    url = f"{base}/rest/v1/prices_daily"
    in_list = ",".join(tickers)
    params = {
        "select": "ticker,adj_close,close",
        "date": f"eq.{date_str}",
        "ticker": f"in.({in_list})",
    }
    resp = requests.get(url, headers=supabase_headers(), params=params, timeout=20)
    if resp.status_code >= 300:
        raise RuntimeError(f"prices_daily fetch failed: {resp.status_code} {resp.text}")
    rows = resp.json()
    prices: Dict[str, float] = {}
    for row in rows:
        price = row.get("adj_close") or row.get("close")
        if price is not None:
            prices[row["ticker"]] = float(price)
    return prices


def log_pipeline_run(
    run_id: str,
    date_str: str,
    status: str,
    stats: Dict,
    warnings: List[str],
    started_at: dt.datetime,
    ended_at: dt.datetime,
    positions: List[Dict],
    equity: Dict,
) -> None:
    try:
        base = supabase_base()
        url = f"{base}/rest/v1/pipeline_runs"
        payload = {
            "run_id": run_id,
            "tag": "paper_trade",
            "stage": "paper_broker",
            "status": status,
            "date": date_str,
            "started_at": started_at.isoformat(),
            "ended_at": ended_at.isoformat(),
            "stats_json": stats,
            "warnings_json": warnings,
            "val_auc": None,
            "top": None,
            "positions": positions,
            "equity": equity,
            "report_path": None,
            "missing_tickers": stats.get("missing", []),
        }
        headers = supabase_headers()
        headers["Prefer"] = "return=minimal"
        resp = requests.post(url, headers=headers, json=payload, timeout=15)
        if resp.status_code >= 300:
            print(f"[pipeline_runs] insert failed: {resp.status_code} {resp.text}")
    except Exception as exc:  # pragma: no cover
        print(f"[pipeline_runs] log error: {exc}")


def main() -> None:
    load_env()
    args = parse_args()
    date_str = args.date

    started_at = dt.datetime.now(dt.timezone.utc)
    run_id = started_at.strftime("%Y%m%d%H%M%S")
    stats = {"model_run_id": None, "positions": 0, "missing": []}
    warnings: List[str] = []

    try:
        model_run_id = args.model_run_id or fetch_latest_model_run(args.horizon_days)
        stats["model_run_id"] = model_run_id
        preds = fetch_predictions(model_run_id, date_str, args.horizon_days, args.top_n)
    except Exception as exc:
        warnings.append(str(exc))
        log_pipeline_run(run_id, date_str, "error", stats, warnings, started_at, dt.datetime.now(dt.timezone.utc), [], {})
        raise

    if not preds:
        warnings.append("No predictions found for date.")
        log_pipeline_run(run_id, date_str, "noop", stats, warnings, started_at, dt.datetime.now(dt.timezone.utc), [], {})
        print("[done] No predictions found.")
        return

    tickers = [p["ticker"] for p in preds]
    try:
        prices = fetch_prices(date_str, tickers)
    except Exception as exc:
        warnings.append(str(exc))
        log_pipeline_run(run_id, date_str, "error", stats, warnings, started_at, dt.datetime.now(dt.timezone.utc), [], {})
        raise

    alloc = args.cash / args.top_n if args.top_n else 0.0
    cost_mult = 1 + (args.fees_bps + args.slippage_bps) / 10_000.0
    positions: List[Dict] = []
    invested = 0.0
    missing: List[str] = []
    eligible_sell_date = (pd.Timestamp(date_str) + pd.tseries.offsets.BDay(args.min_hold_days)).date().isoformat()

    for p in preds:
        ticker = p["ticker"]
        price = prices.get(ticker)
        if price is None or price <= 0:
            missing.append(ticker)
            continue
        shares = math.floor(alloc / (price * cost_mult))
        if shares <= 0:
            warnings.append(f"Insufficient cash to buy {ticker} at {price:.2f}.")
            continue
        cost = shares * price * cost_mult
        invested += cost
        positions.append(
            {
                "ticker": ticker,
                "shares": shares,
                "price": price,
                "cost": round(cost, 2),
                "entry_date": date_str,
                "eligible_sell_date": eligible_sell_date,
                "fees_bps": args.fees_bps,
                "slippage_bps": args.slippage_bps,
            }
        )

    stats["positions"] = len(positions)
    stats["missing"] = missing
    cash_left = max(args.cash - invested, 0.0)
    equity = {
        "date": date_str,
        "cash_start": args.cash,
        "cash_end": round(cash_left, 2),
        "invested": round(invested, 2),
        "equity": round(invested + cash_left, 2),
    }

    status = "success"
    if warnings or missing:
        status = "warn"
    ended_at = dt.datetime.now(dt.timezone.utc)
    if not args.dry_run:
        log_pipeline_run(run_id, date_str, status, stats, warnings, started_at, ended_at, positions, equity)

    print(f"[done] positions={len(positions)} cash_left={cash_left:.2f}")
    if missing:
        print(f"[warn] missing prices for: {', '.join(missing)}")
    for w in warnings:
        print(f"[warn] {w}")


if __name__ == "__main__":
    try:
        main()
    except Exception as exc:
        print(f"[fatal] paper_trade failed: {exc}")
        sys.exit(1)
