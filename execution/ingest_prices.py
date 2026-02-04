"""
Daily OHLCV ingest for universe tickers + SPY benchmark.
- Fetches prices from Yahoo Finance
- Upserts into Supabase tables: instruments, universe_versions, prices_daily, benchmark_prices_daily
- Logs to pipeline_runs (stage=market_data)
"""

from __future__ import annotations

import argparse
import datetime as dt
import os
import sys
from pathlib import Path
from typing import Dict, List, Tuple

import pandas as pd
import requests
import yfinance as yf
from dotenv import load_dotenv

DEFAULT_TICKERS_FILE = Path(__file__).with_name("sp500_tickers.txt")
BENCHMARK = "SPY"


def load_env() -> None:
    env_path = Path(__file__).resolve().parents[1] / ".env"
    if env_path.exists():
        load_dotenv(env_path)


def parse_args() -> argparse.Namespace:
    today = dt.date.today().isoformat()
    parser = argparse.ArgumentParser(description="Ingest OHLCV into Supabase (single date or range).")
    parser.add_argument("--date", default=today, help="Target date YYYY-MM-DD (default: today).")
    parser.add_argument("--start-date", default=None, help="Optional start date for range ingest (YYYY-MM-DD).")
    parser.add_argument("--end-date", default=None, help="Optional end date for range ingest (YYYY-MM-DD, exclusive).")
    parser.add_argument("--ticker", action="append", default=[], help="Additional ticker (repeatable).")
    parser.add_argument(
        "--tickers-file",
        default=os.getenv("UNIVERSE_TICKERS_FILE") or str(DEFAULT_TICKERS_FILE),
        help="Path to ticker list (one per line). Defaults to bundled S&P 500 list.",
    )
    parser.add_argument("--universe-version", default=None, help="Optional universe version_id (default: sp500-<date>).")
    parser.add_argument("--source", default="yfinance", help="Data source label to store (default: yfinance).")
    parser.add_argument("--chunk-size", type=int, default=500, help="Upsert batch size.")
    parser.add_argument("--dry-run", action="store_true", help="Fetch and report without writing to Supabase.")
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


def load_tickers(path: str, extras: List[str]) -> List[str]:
    tickers: List[str] = []
    try:
        with open(path, "r", encoding="utf-8") as f:
            tickers.extend([line.strip().upper() for line in f if line.strip()])
    except FileNotFoundError:
        print(f"[tickers] file not found at {path}; continuing with provided tickers only.")
    tickers.extend([t.upper() for t in extras if t])
    uniq: List[str] = []
    seen = set()
    for t in tickers:
        if t and t not in seen:
            uniq.append(t)
            seen.add(t)
    return [t for t in uniq if t != BENCHMARK]


def fetch_prices_range(tickers: List[str], start_date: dt.date, end_date: dt.date) -> Tuple[List[Dict], List[Dict], List[str]]:
    """Fetch OHLCV for tickers over [start_date, end_date).

    Note: Yahoo Finance uses hyphenated class share tickers (e.g. BRK-B, BF-B)
    while many universes use dot notation (BRK.B, BF.B). We normalize *only for
    download*, then map back to the original ticker symbols for storage.
    """

    def to_yahoo_symbol(t: str) -> str:
        # Most common mapping: dot-class → hyphen-class.
        # Keep canonical storage tickers untouched elsewhere.
        return t.replace(".", "-")

    tickers = [t.upper() for t in tickers]
    canonical = sorted(set(tickers))
    canon_to_yf = {t: to_yahoo_symbol(t) for t in canonical}

    all_yf = sorted(set([canon_to_yf[t] for t in canonical] + [BENCHMARK]))
    yf_to_canon = {v: k for k, v in canon_to_yf.items()}

    data = yf.download(
        tickers=all_yf,
        start=start_date.isoformat(),
        end=end_date.isoformat(),
        progress=False,
        auto_adjust=False,
        interval="1d",
        group_by="column",
    )
    if data.empty:
        raise RuntimeError(f"No price data returned for {start_date} -> {end_date}.")

    if isinstance(data.columns, pd.MultiIndex):
        fields = {}
        for field in ["Open", "High", "Low", "Close", "Adj Close", "Volume"]:
            if field in data.columns.get_level_values(0):
                fields[field] = data[field]
            else:
                fields[field] = None
    else:
        fields = {field: data[[field]] if field in data.columns else None for field in ["Open", "High", "Low", "Close", "Adj Close", "Volume"]}

    records: List[Dict] = []
    benchmark_rows: List[Dict] = []
    tickers_with_data: set[str] = set()  # canonical tickers

    def get_val(field: str, ts: pd.Timestamp, ticker: str) -> float | None:
        df = fields.get(field)
        if df is None or ticker not in df.columns:
            return None
        try:
            val = df.loc[ts, ticker]
        except Exception:
            return None
        try:
            val = float(val)
        except Exception:
            return None
        if pd.isna(val):
            return None
        return val

    for ts in data.index:
        date_str = pd.to_datetime(ts).date().isoformat()
        for ticker in canonical + [BENCHMARK]:
            yf_ticker = BENCHMARK if ticker == BENCHMARK else canon_to_yf.get(ticker, ticker)
            row = {
                "date": date_str,
                "ticker": ticker if ticker != BENCHMARK else BENCHMARK,
                "open": get_val("Open", ts, yf_ticker),
                "high": get_val("High", ts, yf_ticker),
                "low": get_val("Low", ts, yf_ticker),
                "close": get_val("Close", ts, yf_ticker),
                "adj_close": get_val("Adj Close", ts, yf_ticker) or get_val("Close", ts, yf_ticker),
                "volume": get_val("Volume", ts, yf_ticker),
            }
            if all(val is None for val in [row["open"], row["high"], row["low"], row["close"], row["adj_close"], row["volume"]]):
                continue
            if ticker == BENCHMARK:
                benchmark_rows.append(
                    {
                        "date": row["date"],
                        "symbol": BENCHMARK,
                        "open": row["open"],
                        "high": row["high"],
                        "low": row["low"],
                        "close": row["close"],
                        "adj_close": row["adj_close"],
                        "volume": row["volume"],
                    }
                )
            else:
                records.append(row)
                tickers_with_data.add(ticker)

    missing = sorted(set(canonical) - tickers_with_data)
    return records, benchmark_rows, missing


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


def upsert_universe(version_id: str, as_of_date: dt.date, members: List[str], notes: str | None, chunk_size: int) -> None:
    payload = {
        "version_id": version_id,
        "as_of_date": as_of_date.isoformat(),
        "members_json": members,
        "notes": notes,
    }
    upsert_rows("universe_versions", [payload], ["version_id"], chunk_size)


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
        base = supabase_base()
        url = f"{base}/rest/v1/pipeline_runs"
        payload = {
            "run_id": run_id,
            "tag": "ingest_prices",
            "stage": "market_data",
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
        headers = supabase_headers()
        headers["Prefer"] = "return=minimal"
        resp = requests.post(url, headers=headers, json=payload, timeout=15)
        if resp.status_code >= 300:
            print(f"[pipeline_runs] insert failed: {resp.status_code} {resp.text}")
    except Exception as exc:  # pragma: no cover - logging should not break ingest
        print(f"[pipeline_runs] log error: {exc}")


def main() -> None:
    load_env()
    args = parse_args()
    if args.start_date and args.end_date:
        start_date = dt.date.fromisoformat(args.start_date)
        end_date = dt.date.fromisoformat(args.end_date)
    else:
        target_date = dt.date.fromisoformat(args.date)
        start_date = target_date
        end_date = target_date + dt.timedelta(days=1)

    started_at = dt.datetime.now(dt.timezone.utc)
    run_id = started_at.strftime("%Y%m%d%H%M%S")
    stats = {
        "tickers_requested": 0,
        "prices_upserted": 0,
        "benchmark_upserted": 0,
        "missing": [],
    }
    warnings: List[str] = []

    tickers = load_tickers(args.tickers_file, args.ticker)
    stats["tickers_requested"] = len(tickers)
    if not tickers:
        warnings.append("No tickers provided; nothing to ingest.")
        log_pipeline_run(run_id, start_date.isoformat(), "noop", stats, warnings, started_at, dt.datetime.now(dt.timezone.utc))
        print("[done] No tickers to ingest.")
        return

    try:
        records, bench_rows, missing = fetch_prices_range(tickers, start_date, end_date)
    except Exception as exc:
        warnings.append(str(exc))
        log_pipeline_run(run_id, start_date.isoformat(), "error", stats, warnings, started_at, dt.datetime.now(dt.timezone.utc))
        raise

    stats["missing"] = missing
    tickers_with_data = len({row["ticker"] for row in records})
    coverage = (tickers_with_data / len(tickers)) * 100 if tickers else 0
    if coverage < 97:
        warnings.append(f"Coverage low: {coverage:.1f}% ({tickers_with_data}/{len(tickers)})")

    if not records and not bench_rows:
        warnings.append("No price rows fetched; likely holiday or bad date.")
        log_pipeline_run(run_id, start_date.isoformat(), "noop", stats, warnings, started_at, dt.datetime.now(dt.timezone.utc))
        print("[done] No price data fetched.")
        return

    version_id = args.universe_version or f"sp500-{start_date.isoformat()}"
    try:
        if not args.dry_run:
            upsert_rows("instruments", [{"ticker": t, "active_flag": True} for t in tickers + [BENCHMARK]], ["ticker"], args.chunk_size)
            upsert_universe(version_id, start_date, tickers, notes=None, chunk_size=args.chunk_size)
    except Exception as exc:
        warnings.append(f"instrument/universe upsert failed: {exc}")
        log_pipeline_run(run_id, start_date.isoformat(), "error", stats, warnings, started_at, dt.datetime.now(dt.timezone.utc))
        raise

    try:
        if not args.dry_run:
            price_rows = [{**r, "source": args.source} for r in records]
            upsert_rows("prices_daily", price_rows, ["date", "ticker"], args.chunk_size)
            stats["prices_upserted"] = len(price_rows)
            if bench_rows:
                bench_payload = [{**r, "source": args.source} for r in bench_rows]
                upsert_rows("benchmark_prices_daily", bench_payload, ["date", "symbol"], args.chunk_size)
                stats["benchmark_upserted"] = len(bench_payload)
    except Exception as exc:
        warnings.append(f"price upsert failed: {exc}")
        log_pipeline_run(run_id, start_date.isoformat(), "error", stats, warnings, started_at, dt.datetime.now(dt.timezone.utc))
        raise

    status = "success" if not warnings else "warn"
    ended_at = dt.datetime.now(dt.timezone.utc)
    if not args.dry_run:
        log_pipeline_run(run_id, start_date.isoformat(), status, stats, warnings, started_at, ended_at)

    print(f"[done] Upserted {stats['prices_upserted']} rows ({coverage:.1f}% coverage), missing tickers: {len(missing)}")
    if warnings:
        for w in warnings:
            print(f"[warn] {w}")


if __name__ == "__main__":
    try:
        main()
    except Exception as exc:
        print(f"[fatal] ingest_prices failed: {exc}")
        sys.exit(1)
