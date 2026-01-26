"""
Paper trading using model predictions and daily prices.
- Loads predictions from Supabase for a given date
- Enforces min-hold for positions
- Uses a VWAP proxy from OHLC for fills
- Writes paper orders, fills, positions, and equity curve
- Logs results to pipeline_runs (stage=paper_broker)
"""

from __future__ import annotations

import argparse
import datetime as dt
import math
import os
import sys
from pathlib import Path
from typing import Dict, List, Optional, Tuple

import pandas as pd
import requests
from dotenv import load_dotenv

DEFAULT_CASH = 5_000.0
DEFAULT_TOP_N = 10
DEFAULT_HORIZON = 5
DEFAULT_FEES_BPS = 2
DEFAULT_SLIPPAGE_BPS = 5
DEFAULT_MIN_HOLD_DAYS = 5
DEFAULT_PORTFOLIO_ID = "default"
DEFAULT_PORTFOLIO_NAME = "Default"
VWAP_METHOD = "ohlc_avg"


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
    parser.add_argument("--cash", type=float, default=DEFAULT_CASH, help="Starting cash (first run only).")
    parser.add_argument("--fees-bps", type=float, default=DEFAULT_FEES_BPS, help="Fee bps applied to notional.")
    parser.add_argument("--slippage-bps", type=float, default=DEFAULT_SLIPPAGE_BPS, help="Slippage bps applied to notional.")
    parser.add_argument("--min-hold-days", type=int, default=DEFAULT_MIN_HOLD_DAYS, help="Min hold in business days.")
    parser.add_argument("--portfolio-id", default=DEFAULT_PORTFOLIO_ID, help="Paper portfolio id.")
    parser.add_argument("--portfolio-name", default=DEFAULT_PORTFOLIO_NAME, help="Paper portfolio name (on create).")
    parser.add_argument("--chunk-size", type=int, default=500, help="Upsert batch size.")
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


def fetch_prices(date_str: str, tickers: List[str]) -> Dict[str, Dict[str, float | None]]:
    if not tickers:
        return {}
    base = supabase_base()
    url = f"{base}/rest/v1/prices_daily"
    in_list = ",".join(tickers)
    params = {
        "select": "ticker,open,high,low,close,adj_close,volume",
        "date": f"eq.{date_str}",
        "ticker": f"in.({in_list})",
    }
    resp = requests.get(url, headers=supabase_headers(), params=params, timeout=20)
    if resp.status_code >= 300:
        raise RuntimeError(f"prices_daily fetch failed: {resp.status_code} {resp.text}")
    rows = resp.json()
    price_map: Dict[str, Dict[str, float | None]] = {}

    def to_float(value: object) -> float | None:
        if value is None:
            return None
        try:
            val = float(value)
        except Exception:
            return None
        return None if pd.isna(val) else val

    for row in rows:
        price_map[row["ticker"]] = {
            "open": to_float(row.get("open")),
            "high": to_float(row.get("high")),
            "low": to_float(row.get("low")),
            "close": to_float(row.get("close")),
            "adj_close": to_float(row.get("adj_close")),
            "volume": to_float(row.get("volume")),
        }
    return price_map


def vwap_proxy(price_row: Dict[str, float | None]) -> Optional[float]:
    vals = [price_row.get("open"), price_row.get("high"), price_row.get("low"), price_row.get("close")]
    clean = [v for v in vals if v is not None]
    if clean:
        return float(sum(clean) / len(clean))
    return close_price(price_row)


def close_price(price_row: Dict[str, float | None]) -> Optional[float]:
    for key in ("adj_close", "close"):
        val = price_row.get(key)
        if val is not None:
            return float(val)
    return None


def fetch_portfolio(portfolio_id: str) -> Optional[Dict]:
    base = supabase_base()
    url = f"{base}/rest/v1/paper_portfolio"
    params = {
        "select": "portfolio_id,name,starting_cash,rules_json,created_at",
        "portfolio_id": f"eq.{portfolio_id}",
        "limit": 1,
    }
    resp = requests.get(url, headers=supabase_headers(), params=params, timeout=15)
    if resp.status_code >= 300:
        raise RuntimeError(f"paper_portfolio fetch failed: {resp.status_code} {resp.text}")
    rows = resp.json()
    return rows[0] if rows else None


def create_portfolio(portfolio_id: str, name: str, starting_cash: float, rules: Dict) -> Dict:
    base = supabase_base()
    url = f"{base}/rest/v1/paper_portfolio"
    headers = supabase_headers()
    headers["Prefer"] = "return=representation"
    payload = {
        "portfolio_id": portfolio_id,
        "name": name,
        "starting_cash": starting_cash,
        "rules_json": rules,
    }
    resp = requests.post(url, headers=headers, json=payload, timeout=15)
    if resp.status_code >= 300:
        raise RuntimeError(f"paper_portfolio insert failed: {resp.status_code} {resp.text}")
    return resp.json()[0]


def ensure_portfolio(args: argparse.Namespace) -> Dict:
    portfolio = fetch_portfolio(args.portfolio_id)
    if portfolio:
        return portfolio
    rules = {
        "top_n": args.top_n,
        "min_hold_days": args.min_hold_days,
        "fees_bps": args.fees_bps,
        "slippage_bps": args.slippage_bps,
        "horizon_days": args.horizon_days,
        "vwap_method": VWAP_METHOD,
    }
    return create_portfolio(args.portfolio_id, args.portfolio_name, args.cash, rules)


def fetch_latest_equity(portfolio_id: str, before_date: str) -> Optional[Dict]:
    base = supabase_base()
    url = f"{base}/rest/v1/paper_equity_curve"
    params = {
        "select": "date,equity,cash,drawdown,turnover",
        "portfolio_id": f"eq.{portfolio_id}",
        "date": f"lt.{before_date}",
        "order": "date.desc",
        "limit": 1,
    }
    resp = requests.get(url, headers=supabase_headers(), params=params, timeout=15)
    if resp.status_code >= 300:
        raise RuntimeError(f"paper_equity_curve fetch failed: {resp.status_code} {resp.text}")
    rows = resp.json()
    return rows[0] if rows else None


def fetch_max_equity(portfolio_id: str, on_or_before_date: str) -> Optional[float]:
    base = supabase_base()
    url = f"{base}/rest/v1/paper_equity_curve"
    params = {
        "select": "equity",
        "portfolio_id": f"eq.{portfolio_id}",
        "date": f"lte.{on_or_before_date}",
        "order": "equity.desc",
        "limit": 1,
    }
    resp = requests.get(url, headers=supabase_headers(), params=params, timeout=15)
    if resp.status_code >= 300:
        raise RuntimeError(f"paper_equity_curve fetch failed: {resp.status_code} {resp.text}")
    rows = resp.json()
    if not rows:
        return None
    equity = rows[0].get("equity")
    return float(equity) if equity is not None else None


def fetch_latest_positions_date(portfolio_id: str, before_date: str) -> Optional[str]:
    base = supabase_base()
    url = f"{base}/rest/v1/paper_positions"
    params = {
        "select": "date",
        "portfolio_id": f"eq.{portfolio_id}",
        "date": f"lt.{before_date}",
        "order": "date.desc",
        "limit": 1,
    }
    resp = requests.get(url, headers=supabase_headers(), params=params, timeout=15)
    if resp.status_code >= 300:
        raise RuntimeError(f"paper_positions fetch failed: {resp.status_code} {resp.text}")
    rows = resp.json()
    return rows[0]["date"] if rows else None


def fetch_positions(portfolio_id: str, date_str: str) -> List[Dict]:
    base = supabase_base()
    url = f"{base}/rest/v1/paper_positions"
    params = {
        "select": "date,portfolio_id,ticker,qty,avg_cost,market_value,entry_date,eligible_sell_date",
        "portfolio_id": f"eq.{portfolio_id}",
        "date": f"eq.{date_str}",
        "order": "ticker.asc",
    }
    resp = requests.get(url, headers=supabase_headers(), params=params, timeout=15)
    if resp.status_code >= 300:
        raise RuntimeError(f"paper_positions fetch failed: {resp.status_code} {resp.text}")
    return resp.json()


def upsert_rows(table: str, rows: List[Dict], conflict_cols: List[str], chunk_size: int) -> None:
    if not rows:
        return
    base = supabase_base()
    url = f"{base}/rest/v1/{table}"
    headers = supabase_headers()
    headers["Prefer"] = "resolution=merge-duplicates"
    for i in range(0, len(rows), chunk_size):
        chunk = rows[i : i + chunk_size]
        params = {"on_conflict": ",".join(conflict_cols)}
        resp = requests.post(url, headers=headers, params=params, json=chunk, timeout=30)
        if resp.status_code >= 300:
            raise RuntimeError(f"{table} upsert failed: {resp.status_code} {resp.text}")


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


def parse_iso_date(value: Optional[str]) -> Optional[dt.date]:
    if not value:
        return None
    return dt.date.fromisoformat(value)


def eligible_to_sell(position: Dict, trade_date: dt.date, min_hold_days: int) -> bool:
    eligible = parse_iso_date(position.get("eligible_sell_date"))
    if eligible:
        return eligible <= trade_date
    entry_date = parse_iso_date(position.get("entry_date"))
    if not entry_date:
        return True
    eligible = (pd.Timestamp(entry_date) + pd.tseries.offsets.BDay(min_hold_days)).date()
    return eligible <= trade_date


def main() -> None:
    load_env()
    args = parse_args()
    trade_date = dt.date.fromisoformat(args.date)

    started_at = dt.datetime.now(dt.timezone.utc)
    run_id = started_at.strftime("%Y%m%d%H%M%S")
    stats = {
        "model_run_id": None,
        "portfolio_id": args.portfolio_id,
        "orders": 0,
        "fills": 0,
        "positions": 0,
        "missing": [],
    }
    warnings: List[str] = []

    try:
        portfolio = ensure_portfolio(args)
        model_run_id = args.model_run_id or fetch_latest_model_run(args.horizon_days)
        stats["model_run_id"] = model_run_id
        preds = fetch_predictions(model_run_id, args.date, args.horizon_days, args.top_n)
    except Exception as exc:
        warnings.append(str(exc))
        log_pipeline_run(run_id, args.date, "error", stats, warnings, started_at, dt.datetime.now(dt.timezone.utc), [], {})
        raise

    if not preds:
        warnings.append("No predictions found for date.")
        log_pipeline_run(run_id, args.date, "noop", stats, warnings, started_at, dt.datetime.now(dt.timezone.utc), [], {})
        print("[done] No predictions found.")
        return

    latest_positions_date = fetch_latest_positions_date(args.portfolio_id, args.date)
    existing_positions = fetch_positions(args.portfolio_id, latest_positions_date) if latest_positions_date else []
    top_tickers = [p["ticker"] for p in preds]
    position_tickers = [p["ticker"] for p in existing_positions]
    price_tickers = sorted(set(top_tickers + position_tickers))

    try:
        price_map = fetch_prices(args.date, price_tickers)
    except Exception as exc:
        warnings.append(str(exc))
        log_pipeline_run(run_id, args.date, "error", stats, warnings, started_at, dt.datetime.now(dt.timezone.utc), [], {})
        raise

    missing_prices = sorted(set(price_tickers) - set(price_map.keys()))
    if missing_prices:
        warnings.append(f"Missing prices for: {', '.join(missing_prices)}")
        stats["missing"] = missing_prices

    prior_equity = fetch_latest_equity(args.portfolio_id, args.date)
    cash_start = float(prior_equity.get("cash")) if prior_equity and prior_equity.get("cash") is not None else float(portfolio.get("starting_cash") or args.cash)
    cash = cash_start

    orders: List[Dict] = []
    fills: List[Dict] = []
    traded_notional = 0.0

    kept_positions: Dict[str, Dict] = {}
    top_set = set(top_tickers)

    for pos in existing_positions:
        ticker = pos["ticker"]
        qty = float(pos.get("qty") or 0.0)
        if qty <= 0:
            continue
        eligible = eligible_to_sell(pos, trade_date, args.min_hold_days)
        if eligible and ticker not in top_set:
            price_row = price_map.get(ticker)
            if not price_row:
                warnings.append(f"Missing price for sell: {ticker}")
                kept_positions[ticker] = pos
                continue
            vwap = vwap_proxy(price_row)
            if vwap is None:
                warnings.append(f"No VWAP proxy for sell: {ticker}")
                kept_positions[ticker] = pos
                continue
            fill_price = vwap * (1 - args.slippage_bps / 10_000.0)
            notional = fill_price * qty
            fees = notional * (args.fees_bps / 10_000.0)
            proceeds = notional - fees
            cash += proceeds
            traded_notional += abs(notional)

            order_id = f"{run_id}-SELL-{ticker}"
            orders.append(
                {
                    "order_id": order_id,
                    "date": args.date,
                    "ticker": ticker,
                    "side": "sell",
                    "target_weight": 0.0,
                    "qty_estimate": qty,
                    "status": "filled",
                }
            )
            fills.append(
                {
                    "fill_id": f"{order_id}-FILL",
                    "order_id": order_id,
                    "fill_price": round(fill_price, 6),
                    "fill_method": VWAP_METHOD,
                    "slippage_bps": args.slippage_bps,
                    "fees": round(fees, 6),
                    "filled_at": dt.datetime.now(dt.timezone.utc).isoformat(),
                }
            )
        else:
            kept_positions[ticker] = pos

    new_targets = [t for t in top_tickers if t not in kept_positions]
    if new_targets:
        alloc = cash / len(new_targets)
        for ticker in new_targets:
            price_row = price_map.get(ticker)
            if not price_row:
                warnings.append(f"Missing price for buy: {ticker}")
                continue
            vwap = vwap_proxy(price_row)
            if vwap is None:
                warnings.append(f"No VWAP proxy for buy: {ticker}")
                continue
            fill_price = vwap * (1 + args.slippage_bps / 10_000.0)
            cost_per_share = fill_price * (1 + args.fees_bps / 10_000.0)
            shares = math.floor(alloc / cost_per_share) if cost_per_share > 0 else 0
            if shares <= 0:
                warnings.append(f"Insufficient cash to buy {ticker} at {fill_price:.2f}.")
                continue
            total_notional = fill_price * shares
            fees = total_notional * (args.fees_bps / 10_000.0)
            total_cost = total_notional + fees
            if total_cost > cash:
                shares = math.floor(cash / cost_per_share) if cost_per_share > 0 else 0
                if shares <= 0:
                    warnings.append(f"Insufficient cash to buy {ticker} after adjustments.")
                    continue
                total_notional = fill_price * shares
                fees = total_notional * (args.fees_bps / 10_000.0)
                total_cost = total_notional + fees
            cash -= total_cost
            traded_notional += abs(total_notional)

            order_id = f"{run_id}-BUY-{ticker}"
            orders.append(
                {
                    "order_id": order_id,
                    "date": args.date,
                    "ticker": ticker,
                    "side": "buy",
                    "target_weight": round(1.0 / args.top_n, 6) if args.top_n else None,
                    "qty_estimate": shares,
                    "status": "filled",
                }
            )
            fills.append(
                {
                    "fill_id": f"{order_id}-FILL",
                    "order_id": order_id,
                    "fill_price": round(fill_price, 6),
                    "fill_method": VWAP_METHOD,
                    "slippage_bps": args.slippage_bps,
                    "fees": round(fees, 6),
                    "filled_at": dt.datetime.now(dt.timezone.utc).isoformat(),
                }
            )

            entry_date = trade_date
            eligible_sell_date = (pd.Timestamp(trade_date) + pd.tseries.offsets.BDay(args.min_hold_days)).date()
            kept_positions[ticker] = {
                "ticker": ticker,
                "qty": shares,
                "avg_cost": fill_price,
                "entry_date": entry_date.isoformat(),
                "eligible_sell_date": eligible_sell_date.isoformat(),
            }

    positions_out: List[Dict] = []
    for ticker, pos in sorted(kept_positions.items()):
        qty = float(pos.get("qty") or 0.0)
        if qty <= 0:
            continue
        price_row = price_map.get(ticker)
        mark_price = close_price(price_row) if price_row else None
        if mark_price is None:
            mark_price = float(pos.get("avg_cost") or 0.0)
            warnings.append(f"Missing close for {ticker}; using avg_cost for market_value.")
        market_value = mark_price * qty
        positions_out.append(
            {
                "date": args.date,
                "portfolio_id": args.portfolio_id,
                "ticker": ticker,
                "qty": round(qty, 6),
                "avg_cost": round(float(pos.get("avg_cost") or 0.0), 6),
                "market_value": round(market_value, 6),
                "entry_date": pos.get("entry_date"),
                "eligible_sell_date": pos.get("eligible_sell_date"),
            }
        )

    invested = sum(p["market_value"] for p in positions_out)
    equity = invested + cash
    prev_max_equity = fetch_max_equity(args.portfolio_id, args.date)
    max_equity = equity if prev_max_equity is None else max(prev_max_equity, equity)
    drawdown = (equity / max_equity - 1) if max_equity else 0.0
    turnover = (traded_notional / equity) if equity else 0.0

    equity_row = {
        "date": args.date,
        "portfolio_id": args.portfolio_id,
        "equity": round(equity, 6),
        "cash": round(cash, 6),
        "drawdown": round(drawdown, 6),
        "turnover": round(turnover, 6),
    }

    stats.update({"orders": len(orders), "fills": len(fills), "positions": len(positions_out)})
    status = "success"
    if warnings:
        status = "warn"

    ended_at = dt.datetime.now(dt.timezone.utc)
    if not args.dry_run:
        try:
            upsert_rows("paper_orders", orders, ["order_id"], args.chunk_size)
            upsert_rows("paper_fills", fills, ["fill_id"], args.chunk_size)
            upsert_rows("paper_positions", positions_out, ["date", "portfolio_id", "ticker"], args.chunk_size)
            upsert_rows("paper_equity_curve", [equity_row], ["date", "portfolio_id"], args.chunk_size)
        except Exception as exc:
            warnings.append(str(exc))
            log_pipeline_run(run_id, args.date, "error", stats, warnings, started_at, ended_at, positions_out, equity_row)
            raise

    log_pipeline_run(run_id, args.date, status, stats, warnings, started_at, ended_at, positions_out, equity_row)

    print(f"[done] positions={len(positions_out)} cash_end={cash:.2f} equity={equity:.2f}")
    if warnings:
        for w in warnings:
            print(f"[warn] {w}")


if __name__ == "__main__":
    try:
        main()
    except Exception as exc:
        print(f"[fatal] paper_trade failed: {exc}")
        sys.exit(1)
