"""
Market-only model runner.
- Loads features + labels from Supabase
- Trains logistic regression baseline
- Scores latest date, writes model_runs and predictions
- Logs to pipeline_runs (stage=model_runner)
"""

from __future__ import annotations

import argparse
import datetime as dt
import os
import sys
from pathlib import Path
from typing import Dict, List, Sequence, Tuple

import numpy as np
import pandas as pd
import requests
from dotenv import load_dotenv
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import roc_auc_score
from sklearn.model_selection import train_test_split

FEATURE_COLS = ["ret_1d", "ret_5d", "ret_20d", "vol_20d", "ma10_over_ma50", "price_vs_ma20"]
DEFAULT_FEATURE_SET = "v1"
TOP_N = 10


def load_env() -> None:
    env_path = Path(__file__).resolve().parents[1] / ".env"
    if env_path.exists():
        load_dotenv(env_path)


def parse_args() -> argparse.Namespace:
    today = dt.date.today()
    parser = argparse.ArgumentParser(description="Train + score logistic regression baseline using Supabase features.")
    parser.add_argument("--feature-set-version", default=DEFAULT_FEATURE_SET, help="Feature set version to use.")
    parser.add_argument("--horizon-days", type=int, default=5, help="Label horizon (trading days).")
    parser.add_argument("--train-window-days", type=int, default=365, help="Training window length.")
    parser.add_argument("--score-date", default=today.isoformat(), help="Date to score YYYY-MM-DD (default: today).")
    parser.add_argument("--top-n", type=int, default=TOP_N, help="Top N predictions to keep.")
    parser.add_argument("--chunk-size", type=int, default=500, help="Upsert batch size.")
    parser.add_argument("--dry-run", action="store_true", help="Run without writing to Supabase.")
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
            "tag": "run_model",
            "stage": "model_runner",
            "status": status,
            "date": date_str,
            "started_at": started_at.isoformat(),
            "ended_at": ended_at.isoformat(),
            "stats_json": stats,
            "warnings_json": warnings,
            "val_auc": stats.get("val_auc"),
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


def load_features(feature_set: str, start_date: str, end_date: str) -> pd.DataFrame:
    rows = fetch_rows(
        "features_daily",
        start_date=start_date,
        end_date=end_date,
        select_cols=["date", "ticker", "feature_set_version", "features_json"],
        extra_filters=[("feature_set_version", f"eq.{feature_set}")],
    )
    if not rows:
        return pd.DataFrame()
    records = []
    for row in rows:
        feats = row.get("features_json") or {}
        feats["date"] = row["date"]
        feats["ticker"] = row["ticker"]
        records.append(feats)
    df = pd.DataFrame(records)
    df["date"] = pd.to_datetime(df["date"])
    return df


def load_labels(horizon: int, start_date: str, end_date: str) -> pd.DataFrame:
    rows = fetch_rows(
        "labels",
        start_date=start_date,
        end_date=end_date,
        select_cols=["date", "ticker", "horizon_days", "excess_return", "y_class"],
        extra_filters=[("horizon_days", f"eq.{horizon}")],
    )
    if not rows:
        return pd.DataFrame()
    df = pd.DataFrame(rows)
    df["date"] = pd.to_datetime(df["date"])
    return df


def train_model(train_df: pd.DataFrame, horizon: int) -> Tuple[LogisticRegression, float]:
    df = train_df.dropna(subset=FEATURE_COLS + ["y_class"])
    if df.empty:
        raise RuntimeError("No training rows after dropping NaNs.")
    X = df[FEATURE_COLS]
    y = df["y_class"]
    X_train, X_val, y_train, y_val = train_test_split(X, y, test_size=0.2, shuffle=False)
    model = LogisticRegression(max_iter=200, n_jobs=None)
    model.fit(X_train, y_train)
    val_auc = float("nan")
    if len(np.unique(y_val)) > 1:
        val_probs = model.predict_proba(X_val)[:, 1]
        val_auc = float(roc_auc_score(y_val, val_probs))
    return model, val_auc


def score_latest(model: LogisticRegression, features: pd.DataFrame, score_date: dt.date, top_n: int) -> pd.DataFrame:
    latest = features[features["date"].dt.date == score_date]
    latest = latest.dropna(subset=FEATURE_COLS)
    if latest.empty:
        return pd.DataFrame()
    probs = model.predict_proba(latest[FEATURE_COLS])[:, 1]
    preds = latest[["date", "ticker"]].copy()
    preds["score"] = probs
    preds = preds.sort_values("score", ascending=False).drop_duplicates(subset=["ticker"], keep="first").reset_index(drop=True)
    preds["rank"] = preds["score"].rank(ascending=False, method="first").astype(int)
    return preds.head(top_n)


def main() -> None:
    load_env()
    args = parse_args()
    score_date = dt.date.fromisoformat(args.score_date)
    train_start = score_date - dt.timedelta(days=args.train_window_days)

    started_at = dt.datetime.now(dt.timezone.utc)
    run_id = started_at.strftime("%Y%m%d%H%M%S")
    stats = {"training_rows": 0, "val_auc": None, "predictions": 0, "missing": []}
    warnings: List[str] = []

    try:
        features = load_features(args.feature_set_version, train_start.isoformat(), score_date.isoformat())
        labels = load_labels(args.horizon_days, train_start.isoformat(), score_date.isoformat())
    except Exception as exc:
        warnings.append(str(exc))
        log_pipeline_run(run_id, score_date.isoformat(), "error", stats, warnings, started_at, dt.datetime.now(dt.timezone.utc))
        raise

    if features.empty or labels.empty:
        warnings.append("Features or labels missing for requested window.")
        log_pipeline_run(run_id, score_date.isoformat(), "error", stats, warnings, started_at, dt.datetime.now(dt.timezone.utc))
        raise SystemExit("No training data.")

    train_df = features.merge(labels, on=["date", "ticker"], how="inner")
    stats["training_rows"] = len(train_df)
    if train_df.empty:
        warnings.append("No overlapping features/labels to train on.")
        log_pipeline_run(run_id, score_date.isoformat(), "error", stats, warnings, started_at, dt.datetime.now(dt.timezone.utc))
        raise SystemExit("Empty training merge.")

    try:
        model, val_auc = train_model(train_df, args.horizon_days)
    except Exception as exc:
        warnings.append(str(exc))
        log_pipeline_run(run_id, score_date.isoformat(), "error", stats, warnings, started_at, dt.datetime.now(dt.timezone.utc))
        raise

    stats["val_auc"] = val_auc
    preds = score_latest(model, features, score_date, args.top_n)
    stats["predictions"] = len(preds)
    if preds.empty:
        warnings.append("No predictions generated for score_date (coverage gap).")

    model_run_id = run_id
    model_run_row = {
        "model_run_id": model_run_id,
        "train_start": train_start.isoformat(),
        "train_end": score_date.isoformat(),
        "horizon_days": args.horizon_days,
        "feature_set_version": args.feature_set_version,
        "metrics_json": {"val_auc": val_auc, "training_rows": stats["training_rows"]},
        "artifact_ref": None,
    }

    prediction_rows = []
    for _, row in preds.iterrows():
        prediction_rows.append(
            {
                "model_run_id": model_run_id,
                "date": pd.to_datetime(row["date"]).date().isoformat(),
                "ticker": row["ticker"],
                "horizon_days": args.horizon_days,
                "score": float(row["score"]),
                "rank": int(row["rank"]),
                "explanation_json": {},
            }
        )

    try:
        if not args.dry_run:
            upsert_chunked("model_runs", [model_run_row], ["model_run_id"], args.chunk_size)
            upsert_chunked("predictions", prediction_rows, ["model_run_id", "date", "ticker", "horizon_days"], args.chunk_size)
    except Exception as exc:
        warnings.append(f"model/prediction upsert failed: {exc}")
        log_pipeline_run(run_id, score_date.isoformat(), "error", stats, warnings, started_at, dt.datetime.now(dt.timezone.utc))
        raise

    status = "success" if not warnings else "warn"
    ended_at = dt.datetime.now(dt.timezone.utc)
    if not args.dry_run:
        log_pipeline_run(run_id, score_date.isoformat(), status, stats, warnings, started_at, ended_at)

    print(f"[done] training_rows={stats['training_rows']} val_auc={val_auc:.3f}" if isinstance(val_auc, float) else f"[done] training_rows={stats['training_rows']}")
    if not preds.empty:
        print("Top predictions:")
        print(preds[["ticker", "score", "rank"]].to_string(index=False))
    if warnings:
        for w in warnings:
            print(f"[warn] {w}")


if __name__ == "__main__":
    try:
        main()
    except Exception as exc:
        print(f"[fatal] run_model failed: {exc}")
        sys.exit(1)
