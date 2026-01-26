"""
P&L view for the latest (or specified) baseline run.
- Loads positions from output/baseline/runs/*.json
- Fetches latest prices via yfinance
- Computes position and portfolio P&L since entry
"""

from __future__ import annotations

import argparse
import datetime as dt
import json
from pathlib import Path
from typing import Dict, List, Tuple

import numpy as np
import pandas as pd
import yfinance as yf

DEFAULT_RUNS_DIR = Path(__file__).resolve().parents[1] / "output" / "baseline" / "runs"


def parse_args() -> argparse.Namespace:
    today = dt.date.today().isoformat()
    parser = argparse.ArgumentParser(description="Show P&L view for a baseline run.")
    parser.add_argument("--run-file", default=None, help="Path to a run JSON file (default: latest).")
    parser.add_argument(
        "--runs-dir",
        default=str(DEFAULT_RUNS_DIR),
        help="Directory containing run JSON files (default: output/baseline/runs).",
    )
    parser.add_argument("--as-of-date", default=today, help="Price as-of date YYYY-MM-DD (default: today).")
    parser.add_argument(
        "--output",
        default=None,
        help="Optional output markdown path (default: output/baseline/pnl/pnl_<run>__<asof>.md).",
    )
    return parser.parse_args()


def latest_run_file(runs_dir: Path) -> Path:
    run_files = sorted(runs_dir.glob("*.json"), key=lambda p: p.stat().st_mtime, reverse=True)
    if not run_files:
        raise FileNotFoundError(f"No run logs found in {runs_dir}")
    return run_files[0]


def load_run(path: Path) -> Dict:
    data = json.loads(path.read_text(encoding="utf-8"))
    if not data.get("positions"):
        raise RuntimeError(f"No positions found in run log: {path}")
    return data


def extract_close(data: pd.DataFrame) -> pd.DataFrame | pd.Series:
    if data.empty:
        raise RuntimeError("No price data returned from Yahoo Finance.")
    if isinstance(data.columns, pd.MultiIndex):
        if "Close" in data.columns.get_level_values(0):
            return data["Close"]
        if "Adj Close" in data.columns.get_level_values(0):
            return data["Adj Close"]
        raise RuntimeError("No Close/Adj Close data returned from Yahoo Finance.")
    if "Close" in data.columns:
        return data["Close"]
    if "Adj Close" in data.columns:
        return data["Adj Close"]
    raise RuntimeError("No Close/Adj Close data returned from Yahoo Finance.")


def fetch_last_prices(tickers: List[str], start: str, end: str) -> Tuple[Dict[str, float], Dict[str, str]]:
    data = yf.download(
        tickers=tickers,
        start=start,
        end=end,
        progress=False,
        auto_adjust=True,
        interval="1d",
        group_by="column",
    )
    close = extract_close(data)
    prices: Dict[str, float] = {}
    price_dates: Dict[str, str] = {}
    if isinstance(close, pd.Series):
        series = close.dropna()
        if not series.empty:
            prices[tickers[0]] = float(series.iloc[-1])
            price_dates[tickers[0]] = pd.to_datetime(series.index[-1]).date().isoformat()
        return prices, price_dates

    for ticker in tickers:
        if ticker not in close.columns:
            continue
        series = close[ticker].dropna()
        if series.empty:
            continue
        prices[ticker] = float(series.iloc[-1])
        price_dates[ticker] = pd.to_datetime(series.index[-1]).date().isoformat()
    return prices, price_dates


def build_positions_view(positions: List[Dict], prices: Dict[str, float], price_dates: Dict[str, str]) -> pd.DataFrame:
    df = pd.DataFrame(positions)
    if df.empty:
        raise RuntimeError("No positions to compute P&L.")
    if "shares" not in df.columns or "price" not in df.columns:
        raise RuntimeError("Positions missing required fields: shares, price.")

    df = df[df["shares"] > 0].copy()
    df["entry_price"] = df["price"].astype(float)
    df["entry_value"] = df["shares"].astype(float) * df["entry_price"]
    df["last_price"] = df["ticker"].map(prices)
    df["price_date"] = df["ticker"].map(price_dates)
    df["market_value"] = df["shares"].astype(float) * df["last_price"].astype(float)
    df["pnl"] = df["market_value"] - df["entry_value"]
    df["pnl_pct"] = df["pnl"] / df["entry_value"]
    df = df.sort_values("pnl", ascending=False)
    return df


def format_positions_view(df: pd.DataFrame) -> pd.DataFrame:
    display = df[
        [
            "ticker",
            "shares",
            "entry_price",
            "entry_value",
            "last_price",
            "price_date",
            "market_value",
            "pnl",
            "pnl_pct",
        ]
    ].copy()
    display["entry_price"] = display["entry_price"].round(2)
    display["entry_value"] = display["entry_value"].round(2)
    display["last_price"] = display["last_price"].round(2)
    display["market_value"] = display["market_value"].round(2)
    display["pnl"] = display["pnl"].round(2)
    display["pnl_pct"] = (display["pnl_pct"] * 100).round(2)
    display = display.fillna("NA")
    return display


def main() -> None:
    args = parse_args()
    runs_dir = Path(args.runs_dir)
    run_path = Path(args.run_file) if args.run_file else latest_run_file(runs_dir)
    run = load_run(run_path)

    run_date = run.get("date")
    if not run_date:
        raise RuntimeError(f"Run log missing date: {run_path}")
    entry_date = dt.date.fromisoformat(run_date)
    as_of = dt.date.fromisoformat(args.as_of_date)
    if as_of < entry_date:
        raise RuntimeError("as-of-date must be on or after the run date.")
    end_date = (as_of + dt.timedelta(days=1)).isoformat()

    positions = run.get("positions", [])
    tickers = [p.get("ticker") for p in positions if p.get("ticker")]
    if not tickers:
        raise RuntimeError(f"No tickers in positions for run: {run_path}")

    prices, price_dates = fetch_last_prices(sorted(set(tickers)), entry_date.isoformat(), end_date)
    missing = sorted(set(tickers) - set(prices.keys()))
    positions_view = build_positions_view(positions, prices, price_dates)

    cash_start = float(run.get("equity", {}).get("cash_start", 0.0))
    cash_end = float(run.get("equity", {}).get("cash_end", 0.0))
    invested = float(positions_view["entry_value"].sum())
    market_value = float(positions_view["market_value"].sum())
    equity_now = market_value + cash_end
    pnl_total = equity_now - cash_start
    pnl_pct = (pnl_total / cash_start) if cash_start else np.nan

    summary = pd.DataFrame(
        [
            {
                "run_date": run_date,
                "as_of": as_of.isoformat(),
                "cash_start": round(cash_start, 2),
                "cash_end": round(cash_end, 2),
                "invested": round(invested, 2),
                "market_value": round(market_value, 2),
                "equity": round(equity_now, 2),
                "pnl": round(pnl_total, 2),
                "pnl_pct": round(pnl_pct * 100, 2) if not np.isnan(pnl_pct) else np.nan,
            }
        ]
    )

    display_positions = format_positions_view(positions_view)

    if args.output:
        report_path = Path(args.output)
    else:
        report_path = Path(__file__).resolve().parents[1] / "output" / "baseline" / "pnl"
        report_path = report_path / f"pnl_{run_date}__{as_of.isoformat()}.md"

    report_path.parent.mkdir(parents=True, exist_ok=True)
    lines = [
        "# P&L View",
        f"Run date: {run_date}",
        f"As of: {as_of.isoformat()}",
        "",
        "## Portfolio Summary",
        summary.to_markdown(index=False),
        "",
        "## Position P&L",
        display_positions.to_markdown(index=False),
    ]
    if missing:
        lines.extend(["", "## Notes", f"- Missing latest price for: {', '.join(missing)}"])
    report_path.write_text("\n".join(lines), encoding="utf-8")

    print("Portfolio Summary:")
    print(summary.to_string(index=False))
    print("\nPosition P&L:")
    print(display_positions.to_string(index=False))
    print(f"\nReport: {report_path}")


if __name__ == "__main__":
    main()
