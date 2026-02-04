"""
Baseline daily loop: Universe -> Prices -> Features -> Labels -> Model -> Predictions -> Paper trades -> Report.
No news/filings/LLM; uses Yahoo Finance for prices and a simple logistic regression baseline.
Outputs: top 10 predictions, paper portfolio positions, equity curve row, and a markdown report.
"""

from __future__ import annotations

import argparse
import datetime as dt
import sys
import time
from dataclasses import dataclass
import json
import os
import requests
from textwrap import shorten
from pathlib import Path
from typing import List, Tuple

import numpy as np
import pandas as pd

try:
    import yfinance as yf
except ImportError as exc:  # pragma: no cover - dependency guard
    raise SystemExit("Missing dependency: pip install yfinance pandas numpy scikit-learn requests") from exc

try:
    from sklearn.linear_model import LogisticRegression
    from sklearn.model_selection import train_test_split
    from sklearn.metrics import roc_auc_score
except ImportError as exc:  # pragma: no cover - dependency guard
    raise SystemExit("Missing dependency: pip install scikit-learn") from exc


DEFAULT_UNIVERSE: List[str] = [
    "AAPL",
    "MSFT",
    "GOOGL",
    "AMZN",
    "META",
    "NVDA",
    "JPM",
    "V",
    "XOM",
    "PG",
    "SPY",  # benchmark
]

DEFAULT_CASH = 5_000.0
TOP_N = 10
HORIZON_DAYS = 5


@dataclass
class PipelineArtifacts:
    close: pd.DataFrame
    features: pd.DataFrame
    labels: pd.DataFrame
    predictions: pd.DataFrame
    positions: pd.DataFrame
    equity_row: pd.Series
    report_path: Path
    run_id: str
    tag: str | None
    missing_tickers: List[str]


def fetch_prices(tickers: List[str], start: str, end: str, retries: int = 3, backoff: float = 2.0) -> Tuple[pd.DataFrame, List[str]]:
    last_exc: Exception | None = None
    data = pd.DataFrame()
    for attempt in range(1, retries + 1):
        try:
            data = yf.download(
                tickers=tickers,
                start=start,
                end=end,
                progress=False,
                auto_adjust=True,
                interval="1d",
                group_by="column",
            )
            if not data.empty:
                break
        except Exception as exc:  # pragma: no cover - best-effort fetch retry
            last_exc = exc
        time.sleep(backoff * attempt)

    if data.empty:
        raise RuntimeError(f"No price data returned from Yahoo Finance after {retries} attempts. Last error: {last_exc}")

    if isinstance(data.columns, pd.MultiIndex):
        # Expect level 0 to be price field, level 1 to be ticker
        if "Close" in data.columns.get_level_values(0):
            close = data["Close"]
        elif "Adj Close" in data.columns.get_level_values(0):
            close = data["Adj Close"]
        else:
            raise RuntimeError("No Close/Adj Close data returned from Yahoo Finance.")
    else:
        if "Close" not in data.columns:
            raise RuntimeError("No Close column returned from Yahoo Finance.")
        close = data[["Close"]]
        close.columns = tickers[:1]

    close = close.dropna(how="all").sort_index()
    # Drop tickers that fully failed; keep SPY mandatory
    close = close.loc[:, close.notna().any()]
    missing = sorted(set(tickers) - set(close.columns))
    if "SPY" not in close.columns:
        raise RuntimeError("Benchmark SPY data missing; cannot continue baseline.")
    if len(missing) == len(tickers):
        raise RuntimeError("No tickers returned any price data.")
    return close, missing


def build_features(close: pd.DataFrame) -> pd.DataFrame:
    returns_1d = close.pct_change(1)
    returns_5d = close.pct_change(5)
    returns_20d = close.pct_change(20)
    vol_20d = close.pct_change().rolling(20).std()
    ma10 = close.rolling(10).mean()
    ma50 = close.rolling(50).mean()
    price_vs_ma20 = close / close.rolling(20).mean()

    stacked = []
    for ticker in close.columns:
        df = pd.DataFrame(
            {
                "date": close.index,
                "ticker": ticker,
                "close": close[ticker],
                "ret_1d": returns_1d[ticker],
                "ret_5d": returns_5d[ticker],
                "ret_20d": returns_20d[ticker],
                "vol_20d": vol_20d[ticker],
                "ma10_over_ma50": ma10[ticker] / ma50[ticker],
                "price_vs_ma20": price_vs_ma20[ticker],
            }
        )
        stacked.append(df)
    features = pd.concat(stacked, ignore_index=True)
    return features


def build_labels(close: pd.DataFrame, horizon: int = HORIZON_DAYS) -> pd.DataFrame:
    spy = close["SPY"]
    spy_fwd = spy.pct_change(horizon).shift(-horizon)
    labels = []
    for ticker in close.columns:
        if ticker == "SPY":
            continue
        fwd_ret = close[ticker].pct_change(horizon).shift(-horizon)
        excess = fwd_ret - spy_fwd
        labels.append(
            pd.DataFrame(
                {
                    "date": close.index,
                    "ticker": ticker,
                    f"excess_ret_{horizon}d": excess,
                    f"label_{horizon}d": (excess > 0).astype(float),
                }
            )
        )
    label_df = pd.concat(labels, ignore_index=True)
    return label_df


def train_and_score(
    features: pd.DataFrame, labels: pd.DataFrame, horizon: int = HORIZON_DAYS
) -> Tuple[pd.DataFrame, float]:
    df = (
        features.merge(labels, on=["date", "ticker"], how="inner")
        .dropna(subset=["ret_20d", f"label_{horizon}d"])
        .copy()
    )
    feature_cols = ["ret_1d", "ret_5d", "ret_20d", "vol_20d", "ma10_over_ma50", "price_vs_ma20"]
    df = df.dropna(subset=feature_cols)
    if df.empty:
        raise RuntimeError("No training rows after cleaning features/labels.")

    X = df[feature_cols]
    y = df[f"label_{horizon}d"]
    X_train, X_val, y_train, y_val = train_test_split(X, y, test_size=0.2, shuffle=False)

    model = LogisticRegression(max_iter=200, n_jobs=None)
    model.fit(X_train, y_train)

    val_probs = model.predict_proba(X_val)[:, 1]
    auc = roc_auc_score(y_val, val_probs) if len(np.unique(y_val)) > 1 else np.nan

    latest_date = features["date"].max()
    live = features[(features["date"] == latest_date) & (features["ticker"] != "SPY")].dropna(subset=feature_cols)
    live_probs = model.predict_proba(live[feature_cols])[:, 1]
    predictions = live[["date", "ticker"]].copy()
    predictions["score"] = live_probs
    predictions = predictions.sort_values("score", ascending=False).reset_index(drop=True)
    predictions["rank"] = predictions["score"].rank(ascending=False, method="first").astype(int)
    predictions["val_auc"] = auc
    return predictions, auc


def paper_trade(predictions: pd.DataFrame, close: pd.DataFrame, cash: float = DEFAULT_CASH) -> Tuple[pd.DataFrame, pd.Series]:
    as_of = predictions["date"].iloc[0]
    prices_row = close.loc[as_of]
    top = predictions.head(TOP_N)
    positions = []
    alloc = cash / TOP_N
    for _, row in top.iterrows():
        ticker = row["ticker"]
        price = prices_row[ticker]
        if pd.isna(price) or price <= 0:
            continue
        shares = np.floor(alloc / price)
        cost = shares * price
        positions.append({"ticker": ticker, "shares": shares, "price": price, "cost": cost})

    positions_df = pd.DataFrame(positions)
    spent = positions_df["cost"].sum() if not positions_df.empty else 0.0
    cash_left = cash - spent
    equity = spent + cash_left
    equity_row = pd.Series(
        {
            "date": as_of,
            "cash_start": cash,
            "cash_end": cash_left,
            "invested": spent,
            "equity": equity,
        }
    )
    return positions_df, equity_row


def write_report(artifacts: PipelineArtifacts, out_dir: Path) -> Path:
    out_dir.mkdir(parents=True, exist_ok=True)
    date_str = artifacts.predictions["date"].iloc[0].strftime("%Y-%m-%d")
    report_path = out_dir / f"baseline_report_{date_str}.md"

    top10 = artifacts.predictions.head(TOP_N)[["rank", "ticker", "score"]]
    positions_md = artifacts.positions.to_markdown(index=False) if not artifacts.positions.empty else "_No positions_"
    equity_md = artifacts.equity_row.to_frame().T.to_markdown(index=False)

    report = [
        "# Baseline Daily Report",
        f"Date: {date_str}",
        "",
        "## Top 10 Predictions",
        top10.to_markdown(index=False),
        "",
        "## Paper Portfolio Positions",
        positions_md,
        "",
        "## Equity Curve Row",
        equity_md,
        "",
        "## Notes",
        f"- Validation AUC (last split): {artifacts.predictions['val_auc'].iloc[0]:.3f}" if not np.isnan(artifacts.predictions['val_auc'].iloc[0]) else "- Validation AUC: N/A",
        "- Baseline loop only (prices/features/labels/model/paper).",
    ]
    report_path.write_text("\n".join(report), encoding="utf-8")
    return report_path


def write_run_log(artifacts: PipelineArtifacts, out_dir: Path) -> Path:
    runs_dir = out_dir / "runs"
    runs_dir.mkdir(parents=True, exist_ok=True)
    date_ts = artifacts.predictions["date"].iloc[0]
    date_str = date_ts.strftime("%Y-%m-%d")
    log_path = runs_dir / f"{date_str}__{artifacts.run_id}.json"
    top = artifacts.predictions.head(TOP_N)[["ticker", "score"]]
    payload = {
        "run_id": artifacts.run_id,
        "tag": artifacts.tag,
        "date": date_str,
        "val_auc": artifacts.predictions["val_auc"].iloc[0],
        "top": top.to_dict(orient="records"),
        "positions": artifacts.positions.to_dict(orient="records"),
        "equity": {k: float(v) if isinstance(v, (np.floating, float)) else v for k, v in artifacts.equity_row.to_dict().items()},
        "report_path": str(artifacts.report_path),
        "missing_tickers": artifacts.missing_tickers,
    }
    log_path.write_text(json.dumps(payload, indent=2, default=str), encoding="utf-8")
    return log_path


def send_telegram_message(text: str) -> None:
    # Nicely formatted Telegram HTML message
    from telegram_fmt import send_telegram as _send

    _send(text)


def push_supabase(payload: dict) -> None:
    supabase_url = os.getenv("SUPABASE_URL")
    supabase_key = os.getenv("SUPABASE_SERVICE_ROLE")
    if not supabase_url or not supabase_key:
        print("[supabase] Skipped: SUPABASE_URL or SUPABASE_SERVICE_ROLE not set.")
        return
    table = os.getenv("SUPABASE_PIPELINE_TABLE", "pipeline_runs")
    url = f"{supabase_url.rstrip('/')}/rest/v1/{table}"
    headers = {
        "apikey": supabase_key,
        "Authorization": f"Bearer {supabase_key}",
        "Content-Type": "application/json",
        "Prefer": "return=minimal",
    }
    try:
        resp = requests.post(url, headers=headers, json=payload, timeout=10)
    except Exception as exc:  # pragma: no cover
        print(f"[supabase] insert error: {exc}")
        return
    if resp.status_code >= 300:
        print(f"[supabase] insert failed: {resp.status_code} {resp.text}")
        if any(marker in resp.text for marker in ["column", "schema cache", "missing", "unknown"]):
            legacy_payload = {
                k: v
                for k, v in payload.items()
                if k
                not in {
                    "stage",
                    "status",
                    "started_at",
                    "ended_at",
                    "stats_json",
                    "warnings_json",
                }
            }
            resp2 = requests.post(url, headers=headers, json=legacy_payload, timeout=10)
            if resp2.status_code >= 300:
                print(f"[supabase] legacy insert failed: {resp2.status_code} {resp2.text}")
            else:
                print("[supabase] legacy insert ok (schema fallback).")
    else:
        print(f"[supabase] insert ok: {resp.status_code}")


def run_pipeline(start: str, end: str, cash: float, universe: List[str], run_id: str | None = None, tag: str | None = None) -> PipelineArtifacts:
    started_at = dt.datetime.now(dt.timezone.utc)
    run_id = run_id or started_at.strftime("%Y%m%d%H%M%S")
    close, missing = fetch_prices(universe, start=start, end=end)
    features = build_features(close)
    labels = build_labels(close, horizon=HORIZON_DAYS)
    predictions, auc = train_and_score(features, labels, horizon=HORIZON_DAYS)
    positions, equity_row = paper_trade(predictions, close, cash=cash)
    output_dir = Path(__file__).resolve().parents[1] / "output" / "baseline"
    artifacts = PipelineArtifacts(
        close=close,
        features=features,
        labels=labels,
        predictions=predictions,
        positions=positions,
        equity_row=equity_row,
        report_path=Path(),
        run_id=run_id,
        tag=tag,
        missing_tickers=missing,
    )
    report_path = write_report(artifacts, output_dir)
    artifacts.report_path = report_path
    log_path = write_run_log(artifacts, output_dir)
    log_data = json.loads(log_path.read_text())
    log_data.update(
        {
            "stage": "baseline",
            "status": "success",
            "started_at": started_at.isoformat(),
            "ended_at": dt.datetime.now(dt.timezone.utc).isoformat(),
            "stats_json": {"val_auc": log_data.get("val_auc"), "missing_tickers": log_data.get("missing_tickers")},
            "warnings_json": [],
        }
    )
    push_supabase(log_data)
    # Optional Telegram ping
    top_tickers = ", ".join([t["ticker"] for t in json.loads(log_path.read_text()).get("top", [])[:5]])
    val_auc = artifacts.predictions["val_auc"].iloc[0]
    msg = shorten(f"Baseline run {run_id} ({artifacts.predictions['date'].iloc[0].date()}): AUC={val_auc:.3f}, Top={top_tickers}", width=300, placeholder="…")
    send_telegram_message(msg)
    return PipelineArtifacts(
        close=close,
        features=features,
        labels=labels,
        predictions=predictions,
        positions=positions,
        equity_row=equity_row,
        report_path=report_path,
        run_id=run_id,
        tag=tag,
        missing_tickers=missing,
    )


def parse_args() -> argparse.Namespace:
    today = dt.date.today()
    default_start = (today - dt.timedelta(days=365)).isoformat()
    default_end = today.isoformat()
    parser = argparse.ArgumentParser(description="Run baseline daily loop (prices -> features -> labels -> model -> paper).")
    parser.add_argument("--start", default=default_start, help="Start date (YYYY-MM-DD)")
    parser.add_argument("--end", default=default_end, help="End date (YYYY-MM-DD)")
    parser.add_argument("--cash", type=float, default=DEFAULT_CASH, help="Starting cash for paper portfolio")
    parser.add_argument("--universe", nargs="*", default=DEFAULT_UNIVERSE, help="Universe tickers (include SPY for benchmark)")
    return parser.parse_args()


def main() -> None:
    args = parse_args()
    if "SPY" not in args.universe:
        print("For baseline, SPY benchmark is required; adding SPY.")
        args.universe.append("SPY")

    artifacts = run_pipeline(start=args.start, end=args.end, cash=args.cash, universe=args.universe)
    print(f"Report written to: {artifacts.report_path}")
    print("Top 5 predictions:")
    print(artifacts.predictions.head().to_string(index=False))
    print("Positions:")
    print(artifacts.positions.head().to_string(index=False) if not artifacts.positions.empty else "No positions generated.")
    print("Equity row:")
    print(artifacts.equity_row.to_string())


if __name__ == "__main__":
    main()
