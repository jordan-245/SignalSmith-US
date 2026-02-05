"""Sector regime helpers for swing_book.

Computes sector ETF leadership vs SPY over short lookbacks.
"""

from __future__ import annotations

import datetime as dt
from typing import Dict, List, Tuple

import pandas as pd


def sector_leaders(ind: pd.DataFrame, sector_etfs: List[str]) -> List[Tuple[str, float]]:
    """Return list of (etf, rs_score) sorted desc.

    rs_score = sector_ret20 - spy_ret20 (best-effort).

    Prefers Supabase-derived indicators; falls back to yfinance if sector ETFs
    are missing.
    """
    if ind is None:
        ind = pd.DataFrame()

    spy = ind[ind["ticker"] == "SPY"] if not ind.empty else pd.DataFrame()
    spy_ret20 = float(spy.iloc[0]["ret20"]) if not spy.empty and "ret20" in spy.columns else None

    leaders = []
    for etf in sector_etfs:
        row = ind[ind["ticker"] == etf] if not ind.empty else pd.DataFrame()
        if not row.empty:
            r20 = float(row.iloc[0].get("ret20") or 0.0)
            leaders.append((etf, r20 - (spy_ret20 or 0.0)))

    # If we got nothing, fall back to yfinance for SPY + sector ETFs.
    if leaders:
        leaders.sort(key=lambda x: x[1], reverse=True)
        return leaders

    try:
        import datetime as dt
        import io
        from contextlib import redirect_stderr, redirect_stdout
        import yfinance as yf

        # infer a date if possible
        d0 = pd.Timestamp(ind["date"].max()).date() if (ind is not None and not ind.empty and "date" in ind.columns) else None
        if d0 is None:
            d0 = dt.date.today()
        start = (d0 - dt.timedelta(days=400)).isoformat()
        end = (d0 + dt.timedelta(days=1)).isoformat()

        def ret20(sym: str) -> float | None:
            with redirect_stdout(io.StringIO()), redirect_stderr(io.StringIO()):
                bars = yf.download(sym, start=start, end=end, interval="1d", progress=False, auto_adjust=False)
            if bars is None or bars.empty:
                return None
            s = bars["Adj Close"].dropna() if "Adj Close" in bars.columns else bars["Close"].dropna()
            if len(s) < 40:
                return None
            return float(s.iloc[-1] / s.shift(20).iloc[-1] - 1.0)

        spy_r20 = ret20("SPY") or 0.0
        out = []
        for etf in sector_etfs:
            r20v = ret20(etf)
            if r20v is None:
                continue
            out.append((etf, float(r20v - spy_r20)))
        out.sort(key=lambda x: x[1], reverse=True)
        return out
    except Exception:
        return []
