"""Sector radar (deterministic).

Computes a lightweight, always-on sector view using US sector ETFs.

Outputs:
- output/sector_radar.json

Designed to be cheap + robust:
- Uses yfinance daily bars as the primary source.
- No LLM.

If you later want CA/AU: add region-specific ETF sets.
"""

from __future__ import annotations

import datetime as dt
import io
import json
from contextlib import redirect_stderr, redirect_stdout
from pathlib import Path
from typing import Dict, List

import numpy as np
import pandas as pd
import yfinance as yf

REPO = Path(__file__).resolve().parents[1]
OUT = REPO / "output" / "sector_radar.json"

SECTOR_ETFS = {
    "Communication Services": "XLC",
    "Consumer Discretionary": "XLY",
    "Consumer Staples": "XLP",
    "Energy": "XLE",
    "Financials": "XLF",
    "Health Care": "XLV",
    "Industrials": "XLI",
    "Materials": "XLB",
    "Real Estate": "XLRE",
    "Technology": "XLK",
    "Utilities": "XLU",
}

CROSS = {
    "Broad": "SPY",
    "Growth": "QQQ",
    "Small Caps": "IWM",
    "Long Rates": "TLT",
    "Credit": "HYG",
    "Gold": "GLD",
    "Oil": "USO",
}


def _download(sym: str, start: str, end: str) -> pd.Series:
    with redirect_stdout(io.StringIO()), redirect_stderr(io.StringIO()):
        bars = yf.download(sym, start=start, end=end, interval="1d", progress=False, auto_adjust=False)
    if bars is None or bars.empty:
        return pd.Series(dtype=float)

    # handle multiindex columns
    if isinstance(bars.columns, pd.MultiIndex):
        if ("Adj Close", sym) in bars.columns:
            s = bars[("Adj Close", sym)]
        elif ("Close", sym) in bars.columns:
            s = bars[("Close", sym)]
        else:
            s = bars.iloc[:, 0]
    else:
        s = bars["Adj Close"] if "Adj Close" in bars.columns else bars["Close"]

    s = pd.Series(s).dropna().astype(float)
    return s


def _snap(s: pd.Series) -> Dict[str, float]:
    if len(s) < 220:
        return {}
    rets = s.pct_change()
    return {
        "close": float(s.iloc[-1]),
        "ret1": float(s.iloc[-1] / s.shift(1).iloc[-1] - 1.0),
        "ret5": float(s.iloc[-1] / s.shift(5).iloc[-1] - 1.0),
        "ret20": float(s.iloc[-1] / s.shift(20).iloc[-1] - 1.0),
        "vol20": float(rets.rolling(20).std().iloc[-1]),
        "sma50": float(s.rolling(50).mean().iloc[-1]),
        "sma200": float(s.rolling(200).mean().iloc[-1]),
    }


def main() -> None:
    day = dt.date.today()
    start = (day - dt.timedelta(days=420)).isoformat()
    end = (day + dt.timedelta(days=1)).isoformat()

    # Download SPY once (benchmark)
    spy = _download("SPY", start, end)
    spy_snap = _snap(spy)

    payload = {
        "generated_at_utc": dt.datetime.now(dt.timezone.utc).replace(microsecond=0).isoformat().replace("+00:00", "Z"),
        "benchmark": {"symbol": "SPY", **spy_snap},
        "sectors": [],
        "cross": [],
    }

    # sectors
    for name, sym in SECTOR_ETFS.items():
        s = _download(sym, start, end)
        snap = _snap(s)
        if not snap:
            continue
        # relative strength vs SPY
        rs5 = (snap["ret5"] - spy_snap.get("ret5", 0.0)) if spy_snap else snap["ret5"]
        rs20 = (snap["ret20"] - spy_snap.get("ret20", 0.0)) if spy_snap else snap["ret20"]
        trend = "above" if snap["close"] > snap["sma200"] else "below"
        payload["sectors"].append(
            {
                "sector": name,
                "symbol": sym,
                **snap,
                "rs5": float(rs5),
                "rs20": float(rs20),
                "trend": trend,
            }
        )

    # cross assets
    for name, sym in CROSS.items():
        s = _download(sym, start, end)
        snap = _snap(s)
        if not snap:
            continue
        trend = "above" if snap["close"] > snap["sma200"] else "below"
        payload["cross"].append({"name": name, "symbol": sym, **snap, "trend": trend})

    # sort sectors by rs20
    payload["sectors"] = sorted(payload["sectors"], key=lambda x: x.get("rs20", -9e9), reverse=True)

    OUT.parent.mkdir(parents=True, exist_ok=True)
    OUT.write_text(json.dumps(payload, indent=2) + "\n", encoding="utf-8")
    print(f"[ok] wrote {OUT}")


if __name__ == "__main__":
    main()
