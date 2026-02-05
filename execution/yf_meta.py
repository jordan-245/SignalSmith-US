"""yfinance metadata helpers (sector + basic fundamentals).

We keep this light and best-effort.
- Uses yfinance.Ticker(...).fast_info / info.
- Caches results to avoid repeated calls.
"""

from __future__ import annotations

import io
import json
from contextlib import redirect_stderr, redirect_stdout
from pathlib import Path
from typing import Any, Dict, Optional

import yfinance as yf

CACHE_PATH = Path(__file__).resolve().parents[1] / "output" / "cache" / "yfinance_meta.json"


def _load_cache() -> Dict[str, Dict[str, Any]]:
    try:
        if CACHE_PATH.exists():
            return json.loads(CACHE_PATH.read_text(encoding="utf-8"))
    except Exception:
        return {}
    return {}


def _save_cache(cache: Dict[str, Dict[str, Any]]) -> None:
    CACHE_PATH.parent.mkdir(parents=True, exist_ok=True)
    CACHE_PATH.write_text(json.dumps(cache, indent=2, sort_keys=True, default=str) + "\n", encoding="utf-8")


def get_meta(ticker: str) -> Dict[str, Any]:
    """Fetch best-effort fundamentals + classification from Yahoo via yfinance.

    Intended for *snapshotting* leads (not deep accounting).
    Adds (when available): trailing/forward PE, PS, PB, EV/EBITDA, sharesOut, float.
    """
    t = (ticker or "").upper().strip()
    if not t:
        return {}

    cache = _load_cache()
    if t in cache:
        return cache[t]

    meta: Dict[str, Any] = {}
    try:
        with redirect_stdout(io.StringIO()), redirect_stderr(io.StringIO()):
            yt = yf.Ticker(t)
            # fast_info is faster/less brittle; info can be slow
            fi = getattr(yt, "fast_info", None)
            if fi:
                meta["market_cap"] = fi.get("market_cap") or fi.get("marketCap")
                meta["last_price"] = fi.get("last_price")
                meta["ten_day_average_volume"] = fi.get("ten_day_average_volume")
                meta["three_month_average_volume"] = fi.get("three_month_average_volume")
            # sector usually lives in .info
            try:
                info = yt.info or {}
                if isinstance(info, dict):
                    meta["sector"] = info.get("sector")
                    meta["industry"] = info.get("industry")

                    # valuation / fundamentals (best-effort)
                    meta["trailing_pe"] = info.get("trailingPE")
                    meta["forward_pe"] = info.get("forwardPE")
                    meta["price_to_sales_ttm"] = info.get("priceToSalesTrailing12Months")
                    meta["price_to_book"] = info.get("priceToBook")
                    meta["enterprise_value"] = info.get("enterpriseValue")
                    meta["ev_to_ebitda"] = info.get("enterpriseToEbitda")
                    meta["shares_outstanding"] = info.get("sharesOutstanding")
                    meta["float_shares"] = info.get("floatShares")
                    meta["short_ratio"] = info.get("shortRatio")
            except Exception:
                pass
    except Exception:
        meta = {}

    cache[t] = meta
    _save_cache(cache)
    return meta


def get_sector(ticker: str) -> Optional[str]:
    return (get_meta(ticker).get("sector") or None)
