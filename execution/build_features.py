"""
Market-only feature builder.
- Loads prices from Supabase (prices_daily + benchmark_prices_daily)
- Computes baseline market features (returns, vol, trend, price/MA)
- Writes features_daily and labels tables
- Logs to pipeline_runs (stage=feature_builder)
"""

from __future__ import annotations

import argparse
import datetime as dt
import os
import sys
from pathlib import Path
from typing import Dict, Iterable, List, Sequence, Tuple

import pandas as pd
import requests
from dotenv import load_dotenv

BENCHMARK = "SPY"
FEATURE_SET_VERSION = "v1"


def load_env() -> None:
    env_path = Path(__file__).resolve().parents[1] / ".env"
    if env_path.exists():
        load_dotenv(env_path)


def parse_args() -> argparse.Namespace:
    today = dt.date.today()
    default_start = (today - dt.timedelta(days=400)).isoformat()
    parser = argparse.ArgumentParser(description="Build market-only features and labels from Supabase price tables.")
    parser.add_argument("--start-date", default=default_start, help="Start date YYYY-MM-DD for feature window.")
    parser.add_argument("--end-date", default=today.isoformat(), help="End date YYYY-MM-DD (default: today).")
    parser.add_argument("--feature-set-version", default=FEATURE_SET_VERSION, help="Feature set version tag.")
    parser.add_argument("--horizon-days", type=int, default=5, help="Label horizon (trading days).")
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


def fetch_rows(
    table: str,
    start_date: str,
    end_date: str,
    select_cols: Sequence[str],
    extra_filters: Sequence[Tuple[str, str]] = (),
    order_by: str | None = None,
    page_size: int = 1000,
) -> List[Dict]:
    base = supabase_base()
    url = f"{base}/rest/v1/{table}"
    rows: List[Dict] = []
    offset = 0
    while True:
        headers = supabase_headers()
        headers["Range-Unit"] = "items"
        headers["Range"] = f"{offset}-{offset + page_size - 1}"
        params: List[Tuple[str, str]] = [("select", ",".join(select_cols)), ("date", f"gte.{start_date}"), ("date", f"lte.{end_date}")]
        if order_by:
            params.append(("order", order_by))
        params.extend(extra_filters)
        resp = requests.get(url, headers=headers, params=params, timeout=30)
        if resp.status_code >= 300:
            raise RuntimeError(f"{table} fetch failed: {resp.status_code} {resp.text}")
        batch = resp.json()
        rows.extend(batch)
        if len(batch) < page_size:
            break
        offset += page_size
    return rows


def upsert_chunked(table: str, rows: List[Dict], conflict_cols: List[str], chunk_size: int) -> None:
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
) -> None:
    try:
        base = supabase_base()
        url = f"{base}/rest/v1/pipeline_runs"
        payload = {
            "run_id": run_id,
            "tag": "build_features",
            "stage": "feature_builder",
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
    except Exception as exc:  # pragma: no cover
        print(f"[pipeline_runs] log error: {exc}")


def pivot_prices(rows: List[Dict], value_field: str, ticker_field: str = "ticker") -> pd.DataFrame:
    if not rows:
        return pd.DataFrame()
    df = pd.DataFrame(rows)
    df["date"] = pd.to_datetime(df["date"])
    df[value_field] = pd.to_numeric(df[value_field], errors="coerce")
    return df.pivot(index="date", columns=ticker_field, values=value_field).sort_index()


def compute_features(close: pd.DataFrame) -> pd.DataFrame:
    returns_1d = close.pct_change(1, fill_method=None)
    returns_5d = close.pct_change(5, fill_method=None)
    returns_20d = close.pct_change(20, fill_method=None)
    vol_20d = close.pct_change(fill_method=None).rolling(20).std()
    ma10 = close.rolling(10).mean()
    ma50 = close.rolling(50).mean()
    price_vs_ma20 = close / close.rolling(20).mean()

    stacked = []
    for ticker in close.columns:
        if ticker == BENCHMARK:
            continue
        df = pd.DataFrame(
            {
                "date": close.index,
                "ticker": ticker,
                "ret_1d": returns_1d[ticker],
                "ret_5d": returns_5d[ticker],
                "ret_20d": returns_20d[ticker],
                "vol_20d": vol_20d[ticker],
                "ma10_over_ma50": ma10[ticker] / ma50[ticker],
                "price_vs_ma20": price_vs_ma20[ticker],
            }
        )
        stacked.append(df)
    if not stacked:
        return pd.DataFrame()
    features = pd.concat(stacked, ignore_index=True)
    feature_cols = ["ret_1d", "ret_5d", "ret_20d", "vol_20d", "ma10_over_ma50", "price_vs_ma20"]
    return features.dropna(subset=feature_cols)


def compute_labels(close: pd.DataFrame, benchmark: pd.Series, horizon: int) -> pd.DataFrame:
    labels = []
    bench_fwd = benchmark.pct_change(horizon, fill_method=None).shift(-horizon)
    for ticker in close.columns:
        if ticker == BENCHMARK:
            continue
        fwd_ret = close[ticker].pct_change(horizon, fill_method=None).shift(-horizon)
        excess = fwd_ret - bench_fwd
        df = pd.DataFrame(
            {
                "date": close.index,
                "ticker": ticker,
                "horizon_days": horizon,
                "excess_return": excess,
                "y_class": (excess > 0).astype(float),
            }
        )
        labels.append(df)
    if not labels:
        return pd.DataFrame()
    return pd.concat(labels, ignore_index=True).dropna(subset=["excess_return", "y_class"])


def main() -> None:
    load_env()
    args = parse_args()
    start_date = dt.date.fromisoformat(args.start_date)
    end_date = dt.date.fromisoformat(args.end_date)
    started_at = dt.datetime.now(dt.timezone.utc)
    run_id = started_at.strftime("%Y%m%d%H%M%S")
    stats = {
        "feature_rows": 0,
        "label_rows": 0,
        "tickers": 0,
        "dates": 0,
        "missing": [],
    }
    warnings: List[str] = []

    try:
        price_rows = fetch_rows(
            "prices_daily",
            start_date=start_date.isoformat(),
            end_date=end_date.isoformat(),
            select_cols=["date", "ticker", "adj_close", "close"],
            order_by="date.asc,ticker.asc",
        )
        bench_rows = fetch_rows(
            "benchmark_prices_daily",
            start_date=start_date.isoformat(),
            end_date=end_date.isoformat(),
            select_cols=["date", "symbol", "adj_close", "close"],
            extra_filters=[("symbol", f"eq.{BENCHMARK}")],
            order_by="date.asc,symbol.asc",
        )
    except Exception as exc:
        warnings.append(str(exc))
        log_pipeline_run(run_id, end_date.isoformat(), "error", stats, warnings, started_at, dt.datetime.now(dt.timezone.utc))
        raise

    if not price_rows or not bench_rows:
        warnings.append("No price data found for requested window.")
        log_pipeline_run(run_id, end_date.isoformat(), "noop", stats, warnings, started_at, dt.datetime.now(dt.timezone.utc))
        print("[done] No price data to build features.")
        return

    price_df = pd.DataFrame(price_rows)
    dupes = price_df.duplicated(subset=["date", "ticker"])
    if dupes.any():
        warnings.append(f"prices_daily had {int(dupes.sum())} duplicate date/ticker rows; keeping last.")
        price_df = price_df.drop_duplicates(subset=["date", "ticker"], keep="last")
    price_df["price"] = pd.to_numeric(price_df["adj_close"], errors="coerce").fillna(pd.to_numeric(price_df["close"], errors="coerce"))
    close = price_df.pivot(index="date", columns="ticker", values="price")
    close.index = pd.to_datetime(close.index)
    close = close.sort_index()

    bench_df = pd.DataFrame(bench_rows)
    bench_dupes = bench_df.duplicated(subset=["date", "symbol"])
    if bench_dupes.any():
        warnings.append(f"benchmark_prices_daily had {int(bench_dupes.sum())} duplicate date/symbol rows; keeping last.")
        bench_df = bench_df.drop_duplicates(subset=["date", "symbol"], keep="last")
    bench_df["price"] = pd.to_numeric(bench_df["adj_close"], errors="coerce").fillna(pd.to_numeric(bench_df["close"], errors="coerce"))
    bench_close = bench_df.pivot(index="date", columns="symbol", values="price")
    bench_close.index = pd.to_datetime(bench_close.index)
    bench_close = bench_close.sort_index()

    stats["tickers"] = len([t for t in close.columns if t != BENCHMARK])
    stats["dates"] = close.shape[0]
    if BENCHMARK not in bench_close.columns:
        warnings.append("Benchmark SPY not found in benchmark_prices_daily.")
        log_pipeline_run(run_id, end_date.isoformat(), "error", stats, warnings, started_at, dt.datetime.now(dt.timezone.utc))
        raise SystemExit("Benchmark SPY missing.")

    features = compute_features(close)
    labels = compute_labels(close, bench_close[BENCHMARK], args.horizon_days)
    stats["feature_rows"] = len(features)
    stats["label_rows"] = len(labels)

    if features.empty:
        warnings.append("No feature rows after computation (check coverage).")
        log_pipeline_run(run_id, end_date.isoformat(), "error", stats, warnings, started_at, dt.datetime.now(dt.timezone.utc))
        raise SystemExit("No features computed.")

    feature_records = []
    feature_cols = ["ret_1d", "ret_5d", "ret_20d", "vol_20d", "ma10_over_ma50", "price_vs_ma20"]
    for _, row in features.iterrows():
        feature_records.append(
            {
                "date": pd.to_datetime(row["date"]).date().isoformat(),
                "ticker": row["ticker"],
                "feature_set_version": args.feature_set_version,
                "features_json": {col: None if pd.isna(row[col]) else float(row[col]) for col in feature_cols},
            }
        )

    label_records = []
    for _, row in labels.iterrows():
        label_records.append(
            {
                "date": pd.to_datetime(row["date"]).date().isoformat(),
                "ticker": row["ticker"],
                "horizon_days": int(row["horizon_days"]),
                "excess_return": float(row["excess_return"]),
                "y_class": float(row["y_class"]),
            }
        )

    try:
        if not args.dry_run:
            upsert_chunked("features_daily", feature_records, ["date", "ticker", "feature_set_version"], args.chunk_size)
            upsert_chunked("labels", label_records, ["date", "ticker", "horizon_days"], args.chunk_size)
    except Exception as exc:
        warnings.append(f"feature/label upsert failed: {exc}")
        log_pipeline_run(run_id, end_date.isoformat(), "error", stats, warnings, started_at, dt.datetime.now(dt.timezone.utc))
        raise

    status = "success" if not warnings else "warn"
    ended_at = dt.datetime.now(dt.timezone.utc)
    if not args.dry_run:
        log_pipeline_run(run_id, end_date.isoformat(), status, stats, warnings, started_at, ended_at)

    print(f"[done] features={stats['feature_rows']} labels={stats['label_rows']} tickers={stats['tickers']} dates={stats['dates']}")
    if warnings:
        for w in warnings:
            print(f"[warn] {w}")


if __name__ == "__main__":
    try:
        main()
    except Exception as exc:
        print(f"[fatal] build_features failed: {exc}")
        sys.exit(1)
