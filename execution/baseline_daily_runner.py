"""
Daily scheduler wrapper for the baseline loop.
Computes a rolling start date, keeps SPY for benchmarking, and runs the baseline pipeline once.
"""

from __future__ import annotations

import argparse
import datetime as dt
from typing import List
from pathlib import Path
from dotenv import load_dotenv

from pathlib import Path
import sys

CURRENT_DIR = Path(__file__).resolve().parent
if str(CURRENT_DIR) not in sys.path:
    sys.path.append(str(CURRENT_DIR))

import baseline_pipeline  # noqa: E402


def parse_args() -> argparse.Namespace:
    today = dt.date.today()
    parser = argparse.ArgumentParser(description="Run the baseline pipeline for today's date with a rolling window.")
    parser.add_argument("--lookback-days", type=int, default=365, help="Days back from today for start date.")
    parser.add_argument("--cash", type=float, default=baseline_pipeline.DEFAULT_CASH, help="Starting cash.")
    parser.add_argument(
        "--universe",
        nargs="*",
        default=baseline_pipeline.DEFAULT_UNIVERSE,
        help="Universe tickers (SPY required; added automatically if missing).",
    )
    parser.add_argument(
        "--end-date",
        default=today.isoformat(),
        help="End date YYYY-MM-DD (default: today; useful for backfills or replays).",
    )
    parser.add_argument("--run-id", default=None, help="Optional run identifier for logging.")
    parser.add_argument("--tag", default=None, help="Optional tag for logging (e.g., env/deployment).")
    return parser.parse_args()


def main() -> None:
    env_path = Path(__file__).resolve().parents[1] / ".env"
    if env_path.exists():
        load_dotenv(env_path)
    args = parse_args()
    end_date = dt.date.fromisoformat(args.end_date)
    start_date = (end_date - dt.timedelta(days=args.lookback_days)).isoformat()
    end_str = end_date.isoformat()

    universe: List[str] = list(args.universe)
    if "SPY" not in universe:
        universe.append("SPY")

    try:
        artifacts = baseline_pipeline.run_pipeline(
            start=start_date,
            end=end_str,
            cash=args.cash,
            universe=universe,
            run_id=args.run_id,
            tag=args.tag,
        )
    except RuntimeError as exc:
        print(f"[baseline_daily_runner] Failed: {exc}. Try increasing --lookback-days (>=120).")
        raise SystemExit(1)
    print(f"[baseline_daily_runner] Completed run for end={end_str}")
    print(f"Report: {artifacts.report_path}")
    print("Top 5 predictions:")
    print(artifacts.predictions.head().to_string(index=False))


if __name__ == "__main__":
    main()
