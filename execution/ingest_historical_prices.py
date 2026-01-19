"""
Historical OHLCV backfill for universe tickers + SPY benchmark.
- Fetches prices from Yahoo Finance in date chunks
- Upserts into Supabase tables: instruments, universe_versions, prices_daily, benchmark_prices_daily
- Logs to pipeline_runs (stage=market_data_backfill)
"""

from __future__ import annotations

import argparse
import datetime as dt
import sys
from pathlib import Path
from typing import Dict, Iterable, List

import requests

CURRENT_DIR = Path(__file__).resolve().parent
if str(CURRENT_DIR) not in sys.path:
    sys.path.append(str(CURRENT_DIR))

import ingest_prices  # noqa: E402


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description="Backfill historical OHLCV into Supabase.")
    parser.add_argument("--start-date", required=True, help="Start date YYYY-MM-DD (inclusive).")
    parser.add_argument("--end-date", required=True, help="End date YYYY-MM-DD (inclusive).")
    parser.add_argument("--chunk-days", type=int, default=90, help="Days per fetch chunk.")
    parser.add_argument("--tickers-per-batch", type=int, default=0, help="Optional ticker batch size (0 = all).")
    parser.add_argument("--ticker", action="append", default=[], help="Additional ticker (repeatable).")
    parser.add_argument(
        "--tickers-file",
        default=str(ingest_prices.DEFAULT_TICKERS_FILE),
        help="Path to ticker list (one per line). Defaults to bundled S&P 500 list.",
    )
    parser.add_argument("--universe-version", default=None, help="Optional universe version_id (default: sp500-<start-date>).")
    parser.add_argument("--source", default="yfinance", help="Data source label to store (default: yfinance).")
    parser.add_argument("--chunk-size", type=int, default=500, help="Upsert batch size.")
    parser.add_argument("--dry-run", action="store_true", help="Fetch and report without writing to Supabase.")
    return parser.parse_args()


def iter_date_chunks(start_date: dt.date, end_exclusive: dt.date, chunk_days: int) -> Iterable[tuple[dt.date, dt.date]]:
    cursor = start_date
    while cursor < end_exclusive:
        chunk_end = min(cursor + dt.timedelta(days=chunk_days), end_exclusive)
        yield cursor, chunk_end
        cursor = chunk_end


def chunked(seq: List[str], size: int) -> Iterable[List[str]]:
    if size <= 0:
        yield seq
        return
    for i in range(0, len(seq), size):
        yield seq[i : i + size]


def log_pipeline_run(
    run_id: str,
    date_str: str,
    status: str,
    stats: Dict,
    warnings: List[str],
    started_at: dt.datetime,
    ended_at: dt.datetime,
) -> None:
    try:
        base = ingest_prices.supabase_base()
        url = f"{base}/rest/v1/pipeline_runs"
        payload = {
            "run_id": run_id,
            "tag": "ingest_historical_prices",
            "stage": "market_data_backfill",
            "status": status,
            "date": date_str,
            "started_at": started_at.isoformat(),
            "ended_at": ended_at.isoformat(),
            "stats_json": stats,
            "warnings_json": warnings,
            "val_auc": None,
            "top": None,
            "positions": None,
            "equity": None,
            "report_path": None,
            "missing_tickers": stats.get("missing", []),
        }
        headers = ingest_prices.supabase_headers()
        headers["Prefer"] = "return=minimal"
        resp = requests.post(url, headers=headers, json=payload, timeout=20)
        if resp.status_code >= 300:
            print(f"[pipeline_runs] insert failed: {resp.status_code} {resp.text}")
    except Exception as exc:  # pragma: no cover
        print(f"[pipeline_runs] log error: {exc}")


def main() -> None:
    ingest_prices.load_env()
    args = parse_args()
    start_date = dt.date.fromisoformat(args.start_date)
    end_date_inclusive = dt.date.fromisoformat(args.end_date)
    end_exclusive = end_date_inclusive + dt.timedelta(days=1)

    started_at = dt.datetime.now(dt.timezone.utc)
    run_id = started_at.strftime("%Y%m%d%H%M%S")
    stats = {
        "tickers_requested": 0,
        "price_rows_upserted": 0,
        "benchmark_rows_upserted": 0,
        "chunks": 0,
        "missing": [],
    }
    warnings: List[str] = []

    tickers = ingest_prices.load_tickers(args.tickers_file, args.ticker)
    stats["tickers_requested"] = len(tickers)
    if not tickers:
        warnings.append("No tickers provided; nothing to ingest.")
        log_pipeline_run(run_id, start_date.isoformat(), "noop", stats, warnings, started_at, dt.datetime.now(dt.timezone.utc))
        print("[done] No tickers to ingest.")
        return

    version_id = args.universe_version or f"sp500-{start_date.isoformat()}"
    try:
        if not args.dry_run:
            ingest_prices.upsert_rows(
                "instruments",
                [{"ticker": t, "active_flag": True} for t in tickers + [ingest_prices.BENCHMARK]],
                ["ticker"],
                args.chunk_size,
            )
            ingest_prices.upsert_universe(version_id, start_date, tickers, notes=None, chunk_size=args.chunk_size)
    except Exception as exc:
        warnings.append(f"instrument/universe upsert failed: {exc}")
        log_pipeline_run(run_id, start_date.isoformat(), "error", stats, warnings, started_at, dt.datetime.now(dt.timezone.utc))
        raise

    missing_set: set[str] = set()
    try:
        for chunk_start, chunk_end in iter_date_chunks(start_date, end_exclusive, args.chunk_days):
            stats["chunks"] += 1
            for batch_index, batch in enumerate(chunked(tickers, args.tickers_per_batch)):
                records, bench_rows, missing = ingest_prices.fetch_prices_range(batch, chunk_start, chunk_end)
                if missing:
                    missing_set.update(missing)
                if batch_index > 0:
                    bench_rows = []
                if not records and not bench_rows:
                    warnings.append(f"No price data for chunk {chunk_start} -> {chunk_end}.")
                    continue
                if not args.dry_run:
                    price_rows = [{**r, "source": args.source} for r in records]
                    ingest_prices.upsert_rows("prices_daily", price_rows, ["date", "ticker"], args.chunk_size)
                    stats["price_rows_upserted"] += len(price_rows)
                    if bench_rows:
                        bench_payload = [{**r, "source": args.source} for r in bench_rows]
                        ingest_prices.upsert_rows(
                            "benchmark_prices_daily",
                            bench_payload,
                            ["date", "symbol"],
                            args.chunk_size,
                        )
                        stats["benchmark_rows_upserted"] += len(bench_payload)
    except Exception as exc:
        warnings.append(str(exc))
        log_pipeline_run(run_id, start_date.isoformat(), "error", stats, warnings, started_at, dt.datetime.now(dt.timezone.utc))
        raise

    stats["missing"] = sorted(missing_set)
    status = "success" if not warnings else "warn"
    ended_at = dt.datetime.now(dt.timezone.utc)
    if not args.dry_run:
        log_pipeline_run(run_id, start_date.isoformat(), status, stats, warnings, started_at, ended_at)

    print(
        f"[done] chunks={stats['chunks']} prices={stats['price_rows_upserted']} "
        f"benchmarks={stats['benchmark_rows_upserted']} missing_tickers={len(stats['missing'])}"
    )
    if warnings:
        for w in warnings:
            print(f"[warn] {w}")


if __name__ == "__main__":
    try:
        main()
    except Exception as exc:
        print(f"[fatal] ingest_historical_prices failed: {exc}")
        sys.exit(1)
