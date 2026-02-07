"""Signal Foundry conductor (MVP, US only).

Runs a deterministic daily pipeline and writes:
- parquet feature store under data/foundry/
- markdown report under docs/foundry/

MVP scope:
- Market: US
- Universe: S&P500 tickers from directives/foundry/universe_us.txt
- Data: daily OHLCV from yfinance
- Models: logistic regression + random forest (scikit-learn)
- Horizons: 1d / 5d / 20d direction probabilities
- Evaluation: simple walk-forward for last N days + brier score

Usage:
  ./.venv/bin/python -u execution/foundry/foundry_run.py --market US --mode post --as-of 2026-02-07

"""

from __future__ import annotations

import argparse
import datetime as dt
import json
from pathlib import Path

from foundry_steps import (
    build_features,
    build_labels,
    load_quality_gates,
    load_universe,
    predict_and_calibrate,
    quality_gate_check,
    render_report,
    write_prices_parquet,
)


REPO = Path(__file__).resolve().parents[2]


def parse_args() -> argparse.Namespace:
    p = argparse.ArgumentParser()
    p.add_argument("--market", choices=["US", "ASX"], default="US")
    p.add_argument("--mode", choices=["pre", "post"], default="post")
    p.add_argument("--as-of", default=dt.date.today().isoformat())
    p.add_argument("--feature-set", default="v1")
    p.add_argument("--years", type=int, default=5, help="Price history window")
    p.add_argument("--limit", type=int, default=0, help="Optional ticker limit for faster local testing")
    return p.parse_args()


def main() -> None:
    args = parse_args()
    as_of = dt.date.fromisoformat(args.as_of)
    run_id = dt.datetime.now(dt.timezone.utc).strftime("%Y%m%d%H%M%S")

    if args.market != "US":
        raise SystemExit("ASX MVP not implemented yet")

    tickers = load_universe("US")
    if args.limit and args.limit > 0:
        tickers = tickers[: args.limit]

    prices = write_prices_parquet(tickers, market="US", as_of=as_of, years=args.years, run_id=run_id)
    feats = build_features(prices, market="US", feature_set=args.feature_set, as_of=as_of)
    labels = build_labels(prices, market="US", as_of=as_of)

    preds, diagnostics = predict_and_calibrate(feats, labels, market="US", as_of=as_of, run_id=run_id)

    gates = load_quality_gates()
    gate_res = quality_gate_check(gates, feats, labels, diagnostics)

    report_md = render_report(market="US", as_of=as_of, run_id=run_id, preds=preds, diagnostics=diagnostics, gate_res=gate_res)

    # Promote latest only if gates pass
    if gate_res.get("ok"):
        latest = REPO / "docs" / "foundry" / "US" / "latest.md"
        latest.write_text(report_md, encoding="utf-8")

    out = {
        "ok": bool(gate_res.get("ok")),
        "market": "US",
        "as_of": as_of.isoformat(),
        "run_id": run_id,
        "gate": gate_res,
    }
    print(json.dumps(out, indent=2))


if __name__ == "__main__":
    main()
