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
    """
    if ind.empty:
        return []
    spy = ind[ind["ticker"] == "SPY"]
    spy_ret20 = float(spy.iloc[0]["ret20"]) if not spy.empty and "ret20" in spy.columns else 0.0

    leaders = []
    for etf in sector_etfs:
        row = ind[ind["ticker"] == etf]
        if row.empty:
            continue
        r20 = float(row.iloc[0].get("ret20") or 0.0)
        leaders.append((etf, r20 - spy_ret20))

    leaders.sort(key=lambda x: x[1], reverse=True)
    return leaders
