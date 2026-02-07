"""Swing-book autonomous paper trading.

This runs a simple, deterministic swing strategy over:
- S&P 500 universe (from execution/sp500_tickers.txt)
- plus a small set of commodity proxies / related ETFs

Workflow (daily):
1) Determine market regime summary (very lightweight).
2) Build candidate set.
3) Compute technical filters from Supabase daily prices.
4) Select up to MAX_POSITIONS targets.
5) Paper trade into targets using first-hour VWAP fills (yfinance 1h) with daily fallback.
6) Notify Telegram with a compact summary.

This is intentionally simple; we can iterate.

Safety: paper-only.
"""

from __future__ import annotations

import datetime as dt
import io
import math
import os
import time
from contextlib import redirect_stderr, redirect_stdout
from pathlib import Path
from typing import Dict, List, Optional, Tuple

import numpy as np
import pandas as pd
import requests
import yfinance as yf
from dotenv import load_dotenv

from journal import journal_run, journal_watch

DEFAULT_PORTFOLIO_ID = "swing"
DEFAULT_PORTFOLIO_NAME = "Swing Book"
DEFAULT_CASH = 5_000.0
MAX_POSITIONS = 10
MIN_HOLD_DAYS = 5  # business days

# Avoid opening new positions into earnings events.
EARNINGS_AVOID_DAYS = 3  # trading sessions ahead (inclusive)

# Post-earnings catalyst allocation (paper-only)
CATALYST_MAX_EQUITY_PER_NAME = 0.02
CATALYST_MAX_EQUITY_TOTAL = 0.10
CATALYST_NEWS_LOOKBACK_DAYS = 3

FEES_BPS = 2
SLIPPAGE_BPS = 5

# Risk model (ATR-based stops + risk-based sizing)
ATR_DAYS = 14
ATR_STOP_MULT = 2.0

# Risk per position (equity-at-risk at stop).
# Defaults tuned from robust (gap-aware) risk grid backtest v2.
RISK_PER_TRADE_BASE_PCT = float(os.getenv("SWING_RISK_PER_TRADE_BASE_PCT", "0.015"))
RISK_PER_TRADE_MIN_PCT = float(os.getenv("SWING_RISK_PER_TRADE_MIN_PCT", "0.01"))
RISK_PER_TRADE_MAX_PCT = float(os.getenv("SWING_RISK_PER_TRADE_MAX_PCT", "0.03"))

MAX_EQUITY_PER_NAME = 0.10  # hard cap on notional exposure per name

# Portfolio-level risk controls
MAX_GROSS_EXPOSURE_PCT = float(os.getenv("SWING_MAX_GROSS_EXPOSURE_PCT", "0.95"))
MAX_SECTOR_EXPOSURE_PCT = float(os.getenv("SWING_MAX_SECTOR_EXPOSURE_PCT", "0.30"))
MAX_DRAWDOWN_PCT = float(os.getenv("SWING_MAX_DRAWDOWN_PCT", "0.12"))
DAILY_LOSS_LIMIT_PCT = float(os.getenv("SWING_DAILY_LOSS_LIMIT_PCT", "0.025"))

# Regime-aware throttles
RISK_OFF_ENTRY_MULT = float(os.getenv("SWING_RISK_OFF_ENTRY_MULT", "0.40"))
RISK_OFF_MAX_POSITIONS_MULT = float(os.getenv("SWING_RISK_OFF_MAX_POSITIONS_MULT", "0.50"))
RISK_ON_ENTRY_MULT = float(os.getenv("SWING_RISK_ON_ENTRY_MULT", "1.00"))

# Time stop: exit if a position hasn't made meaningful progress after N business days.
TIME_STOP_DAYS = int(os.getenv("SWING_TIME_STOP_DAYS", "10"))
TIME_STOP_PROGRESS_ATR = float(os.getenv("SWING_TIME_STOP_PROGRESS_ATR", "0.5"))

# Commodity proxies / related ETFs (starter set; editable)
PROXIES = [
    # Broad market + small-cap proxy (regime)
    "SPY",
    "IWM",
    "VOO",
    "IVV",
    # Macro / commodities
    "GLD",
    "SLV",
    "GDX",
    "GDXJ",
    "USO",
    "UNG",
    "XLE",
    "OIH",
    "DBC",
    "DBA",
]

# Sector ETF mapping for rotation context (Yahoo/yfinance sector strings).
SECTOR_ETF = {
    "Technology": "XLK",
    "Financial Services": "XLF",
    "Financial": "XLF",
    "Healthcare": "XLV",
    "Health Care": "XLV",
    "Energy": "XLE",
    "Industrials": "XLI",
    "Consumer Cyclical": "XLY",
    "Consumer Defensive": "XLP",
    "Consumer Staples": "XLP",
    "Utilities": "XLU",
    "Basic Materials": "XLB",
    "Real Estate": "XLRE",
    "Communication Services": "XLC",
}

SECTOR_ETFS = sorted(set(SECTOR_ETF.values()))

# Fundamental/liquidity guardrails.
# NOTE: We’re now targeting “smallish” names too, so keep these as *guardrails*, not hard large-cap gates.
MIN_MARKET_CAP = float(os.getenv("SWING_MIN_MARKET_CAP", "0"))  # default: no hard cap
MIN_AVG_VOLUME = float(os.getenv("SWING_MIN_AVG_VOLUME", "0"))  # default: no hard cap
MIN_AVG_DOLLAR_VOL = float(os.getenv("SWING_MIN_AVG_DOLLAR_VOL", "20000000"))  # $20M/day default

# Simple idempotency + non-overlap guardrails
STATE_DIR = Path(__file__).resolve().parents[1] / "output" / "state"
LOCK_PATH = Path(os.getenv("SWING_BOOK_LOCK_PATH", "/tmp/signalsmith_swing_book.lock"))
LOCK_STALE_SECONDS = int(os.getenv("SWING_BOOK_LOCK_STALE_SECONDS", "7200"))


def load_env() -> None:
    env_path = Path(__file__).resolve().parents[1] / ".env"
    if env_path.exists():
        load_dotenv(env_path)


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


def send_telegram(text: str) -> None:
    from telegram_fmt import send_telegram as _send

    _send(text, timeout=15)


def load_universe() -> List[str]:
    tickers_file = Path(__file__).with_name("sp500_tickers.txt")
    tickers: List[str] = []
    if tickers_file.exists():
        for line in tickers_file.read_text(encoding="utf-8").splitlines():
            s = line.strip().upper()
            if s:
                tickers.append(s)
    # De-dupe and add proxies
    out: List[str] = []
    seen = set()
    for t in tickers + [p.upper() for p in PROXIES]:
        if t and t not in seen:
            out.append(t)
            seen.add(t)
    return out


def fetch_prices_window(tickers: List[str], end_date: dt.date, lookback_days: int = 260) -> pd.DataFrame:
    """Fetch daily close series from Supabase for [end-lookback, end]."""
    start_date = (pd.Timestamp(end_date) - pd.tseries.offsets.BDay(lookback_days)).date()
    base = supabase_base()
    url = f"{base}/rest/v1/prices_daily"

    # PostgREST in.(...) lists can get large; chunk tickers.
    cols = "date,ticker,adj_close,close,high,low,open,volume"
    all_rows: List[Dict] = []

    def chunks(xs: List[str], n: int) -> List[List[str]]:
        return [xs[i : i + n] for i in range(0, len(xs), n)]

    for part in chunks(tickers, 200):
        in_list = ",".join(part)
        params = {
            "select": cols,
            "date": f"gte.{start_date.isoformat()}",
            "date": f"lte.{end_date.isoformat()}",
            "ticker": f"in.({in_list})",
            "order": "date.asc",
        }
        # NOTE: duplicate keys in dict overwrite; use list of tuples instead.
        params_list = [
            ("select", cols),
            ("date", f"gte.{start_date.isoformat()}"),
            ("date", f"lte.{end_date.isoformat()}"),
            ("ticker", f"in.({in_list})"),
            ("order", "date.asc"),
        ]
        resp = requests.get(url, headers=supabase_headers(), params=params_list, timeout=30)
        if resp.status_code >= 300:
            raise RuntimeError(f"prices_daily fetch failed: {resp.status_code} {resp.text}")
        all_rows.extend(resp.json())

    if not all_rows:
        return pd.DataFrame()

    df = pd.DataFrame(all_rows)
    df["date"] = pd.to_datetime(df["date"])
    # Prefer adj_close then close.
    df["px"] = df["adj_close"].astype(float).where(df["adj_close"].notna(), df["close"].astype(float))
    return df


def compute_indicators(df: pd.DataFrame) -> pd.DataFrame:
    """Compute per-ticker indicators from daily OHLCV.

    Keep this lightweight: only indicators we will actually use.
    """
    if df.empty:
        return df

    out_rows: List[Dict] = []
    for ticker, g in df.sort_values(["ticker", "date"]).groupby("ticker"):
        g = g.set_index("date").sort_index()
        s = g["px"].astype(float).dropna()
        if len(s) < 220:
            continue

        high = g["high"].astype(float).reindex(s.index)
        low = g["low"].astype(float).reindex(s.index)
        vol = g.get("volume")
        if vol is not None:
            vol = vol.astype(float).reindex(s.index)

        rets = s.pct_change()
        sma50 = s.rolling(50).mean()
        sma200 = s.rolling(200).mean()
        ret20 = (s / s.shift(20) - 1.0)
        ret60 = (s / s.shift(60) - 1.0)
        vol20 = rets.rolling(20).std()

        # RSI14
        delta = s.diff()
        gain = delta.clip(lower=0).rolling(14).mean()
        loss = (-delta.clip(upper=0)).rolling(14).mean()
        rs = gain / loss.replace(0, np.nan)
        rsi14 = 100 - (100 / (1 + rs))

        # ATR14
        prev_close = s.shift(1)
        tr = pd.concat(
            [
                (high - low).abs(),
                (high - prev_close).abs(),
                (low - prev_close).abs(),
            ],
            axis=1,
        ).max(axis=1)
        atr14 = tr.rolling(ATR_DAYS).mean()

        # ADX(14) (trend strength)
        up_move = high.diff()
        down_move = -low.diff()
        plus_dm = up_move.where((up_move > down_move) & (up_move > 0), 0.0)
        minus_dm = down_move.where((down_move > up_move) & (down_move > 0), 0.0)
        tr14 = tr.rolling(14).sum()
        plus_di = 100 * (plus_dm.rolling(14).sum() / tr14.replace(0, np.nan))
        minus_di = 100 * (minus_dm.rolling(14).sum() / tr14.replace(0, np.nan))
        dx = (100 * (plus_di - minus_di).abs() / (plus_di + minus_di).replace(0, np.nan))
        adx14 = dx.rolling(14).mean()

        # Volume confirmation: 20d vs 60d average volume + dollar volume snapshot
        vol_ratio = None
        avg_vol20 = None
        avg_dollar_vol20 = None
        if vol is not None:
            v20 = vol.rolling(20).mean()
            v60 = vol.rolling(60).mean()
            vr = v20 / v60.replace(0, np.nan)
            vol_ratio = float(vr.iloc[-1]) if not pd.isna(vr.iloc[-1]) else None
            avg_vol20 = float(v20.iloc[-1]) if not pd.isna(v20.iloc[-1]) else None
            if avg_vol20 is not None:
                avg_dollar_vol20 = float(avg_vol20 * float(s.iloc[-1]))

        # Overextension: distance from SMA200
        dist_sma200 = float(s.iloc[-1] / sma200.iloc[-1] - 1.0) if not pd.isna(sma200.iloc[-1]) else None

        # 52w high proximity
        hi_52w = s.rolling(252).max()
        near_52w = float(s.iloc[-1] / hi_52w.iloc[-1]) if not pd.isna(hi_52w.iloc[-1]) else None

        last_dt = s.index[-1]
        out_rows.append(
            {
                "ticker": ticker,
                "date": last_dt,
                "close": float(s.iloc[-1]),
                "sma50": float(sma50.iloc[-1]),
                "sma200": float(sma200.iloc[-1]),
                "ret20": float(ret20.iloc[-1]),
                "ret60": float(ret60.iloc[-1]) if not pd.isna(ret60.iloc[-1]) else None,
                "vol20": float(vol20.iloc[-1]) if not pd.isna(vol20.iloc[-1]) else None,
                "rsi14": float(rsi14.iloc[-1]) if not pd.isna(rsi14.iloc[-1]) else None,
                "atr14": float(atr14.iloc[-1]) if not pd.isna(atr14.iloc[-1]) else None,
                "adx14": float(adx14.iloc[-1]) if not pd.isna(adx14.iloc[-1]) else None,
                "vol_ratio": vol_ratio,
                "avg_vol20": avg_vol20,
                "avg_dollar_vol20": avg_dollar_vol20,
                "dist_sma200": dist_sma200,
                "near_52w": near_52w,
            }
        )

    return pd.DataFrame(out_rows)


def rank_candidates(ind: pd.DataFrame) -> pd.DataFrame:
    if ind.empty:
        return ind
    df = ind.copy()

    # Trend filter: close > sma50 > sma200
    df = df[(df["close"] > df["sma50"]) & (df["sma50"] > df["sma200"])]

    # Avoid extreme overextension (helps reduce buying blow-off tops)
    if "dist_sma200" in df.columns:
        df = df[(df["dist_sma200"].isna()) | (df["dist_sma200"] <= 0.35)]

    # RSI filter: avoid overbought extremes
    df = df[(df["rsi14"].isna()) | ((df["rsi14"] >= 45) & (df["rsi14"] <= 78))]

    # ADX filter (prefer trending names)
    if "adx14" in df.columns:
        df = df[(df["adx14"].isna()) | (df["adx14"] >= 18)]

    # Base score: momentum / vol (risk-adjusted)
    df["score"] = df["ret20"] / (df["vol20"].replace(0, np.nan))

    # Boost: near highs + volume confirmation (small weights)
    if "near_52w" in df.columns:
        df["score"] = df["score"] + 0.25 * (df["near_52w"].fillna(0.0) - 0.9)
    if "vol_ratio" in df.columns:
        df["score"] = df["score"] + 0.10 * (df["vol_ratio"].fillna(1.0) - 1.0)

    df = df.replace([np.inf, -np.inf], np.nan).dropna(subset=["score"])
    df = df.sort_values("score", ascending=False)
    return df


def _get_xnys_calendar():
    try:
        import exchange_calendars as xcals  # type: ignore

        return xcals.get_calendar("XNYS")
    except Exception:
        return None


def market_is_open(date_str: str, calendar: str = "XNYS") -> bool:
    """True if the exchange calendar has a session on date_str."""
    try:
        import exchange_calendars as xcals  # type: ignore

        cal = xcals.get_calendar(calendar)
        return bool(cal.is_session(date_str))
    except Exception:
        d = dt.date.fromisoformat(date_str)
        return d.weekday() < 5


def next_trading_sessions(date_str: str, sessions_ahead: int) -> List[str]:
    """Return a list of session dates (YYYY-MM-DD) starting at date_str (inclusive)."""
    cal = _get_xnys_calendar()
    if cal is None:
        # Weekday fallback (no holiday awareness)
        d0 = dt.date.fromisoformat(date_str)
        out: List[str] = []
        d = d0
        while len(out) < max(1, sessions_ahead + 1):
            if d.weekday() < 5:
                out.append(d.isoformat())
            d += dt.timedelta(days=1)
        return out

    start = pd.Timestamp(date_str)
    # Pull enough calendar days to cover N sessions
    end = start + pd.Timedelta(days=20)
    sessions = cal.sessions_in_range(start, end)
    out = [s.date().isoformat() for s in sessions[: max(1, sessions_ahead + 1)]]
    return out


def next_earnings_date(ticker: str) -> Optional[dt.date]:
    """Best-effort next earnings date from yfinance.

    Suppresses yfinance stdout/stderr to avoid log spam.
    """

    try:
        with redirect_stdout(io.StringIO()), redirect_stderr(io.StringIO()):
            cal = yf.Ticker(ticker).calendar
        if cal is None or getattr(cal, "empty", False):
            return None
        if "Earnings Date" in cal.index:
            val = cal.loc["Earnings Date"].iloc[0]
        else:
            val = cal.iloc[0, 0]
        ts = pd.to_datetime(val)
        if pd.isna(ts):
            return None
        return ts.date()
    except Exception:
        return None


def filter_earnings_avoid(candidates: List[str], trade_date: dt.date, sessions_ahead: int) -> Tuple[List[str], List[str]]:
    """Remove tickers with earnings within next sessions_ahead sessions (inclusive)."""
    if not candidates or sessions_ahead <= 0:
        return candidates, []

    window = set(next_trading_sessions(trade_date.isoformat(), sessions_ahead))
    kept: List[str] = []
    avoided: List[str] = []
    cache: Dict[str, Optional[dt.date]] = {}

    for t in candidates:
        if t not in cache:
            cache[t] = next_earnings_date(t)
        ed = cache[t]
        if ed is not None and ed.isoformat() in window:
            avoided.append(t)
        else:
            kept.append(t)

    return kept, avoided


def first_hour_vwap_yf_1h(ticker: str, date_str: str, tz: str = "America/New_York") -> Optional[float]:
    d0 = dt.date.fromisoformat(date_str)
    d1 = d0 + dt.timedelta(days=1)
    try:
        # yfinance can be noisy on missing intraday; suppress its stdout/stderr.
        with redirect_stdout(io.StringIO()), redirect_stderr(io.StringIO()):
            bars = yf.download(
                tickers=ticker,
                start=d0.isoformat(),
                end=d1.isoformat(),
                interval="1h",
                progress=False,
                auto_adjust=False,
                prepost=False,
            )
    except Exception:
        return None

    if bars is None or bars.empty:
        return None

    idx = bars.index
    try:
        if getattr(idx, "tz", None) is None:
            idx = idx.tz_localize("UTC")
        idx_local = idx.tz_convert(tz)
    except Exception:
        return None

    bars = bars.copy()
    bars.index = idx_local
    day = bars[bars.index.date == d0]
    if day.empty:
        return None

    open_bar = day[(day.index.hour == 9) & (day.index.minute == 30)]
    if open_bar.empty:
        open_bar = day.iloc[:1]

    try:
        tp = (open_bar["High"].astype(float) + open_bar["Low"].astype(float) + open_bar["Close"].astype(float)) / 3.0
        v = open_bar["Volume"].astype(float)
        v_sum = float(v.sum())
        if v_sum <= 0:
            return None
        return float((tp * v).sum() / v_sum)
    except Exception:
        return None


def ensure_portfolio(portfolio_id: str, name: str, starting_cash: float) -> None:
    base = supabase_base()
    url = f"{base}/rest/v1/paper_portfolio"
    params = [("select", "portfolio_id"), ("portfolio_id", f"eq.{portfolio_id}"), ("limit", "1")]
    resp = requests.get(url, headers=supabase_headers(), params=params, timeout=15)
    if resp.status_code >= 300:
        raise RuntimeError(f"paper_portfolio fetch failed: {resp.status_code} {resp.text}")
    if resp.json():
        return

    headers = supabase_headers()
    headers["Prefer"] = "return=minimal"
    payload = {
        "portfolio_id": portfolio_id,
        "name": name,
        "starting_cash": starting_cash,
        "rules_json": {
            "max_positions": MAX_POSITIONS,
            "min_hold_days": MIN_HOLD_DAYS,
            "fees_bps": FEES_BPS,
            "slippage_bps": SLIPPAGE_BPS,
            "vwap_method": "first_hour_vwap_1h_yfinance",
        },
    }
    resp2 = requests.post(url, headers=headers, json=payload, timeout=15)
    if resp2.status_code >= 300:
        raise RuntimeError(f"paper_portfolio insert failed: {resp2.status_code} {resp2.text}")


def fetch_latest_positions(portfolio_id: str, before_date: str) -> Tuple[str | None, List[Dict]]:
    base = supabase_base()
    url = f"{base}/rest/v1/paper_positions"
    params = [("select", "date"), ("portfolio_id", f"eq.{portfolio_id}"), ("date", f"lt.{before_date}"), ("order", "date.desc"), ("limit", "1")]
    resp = requests.get(url, headers=supabase_headers(), params=params, timeout=15)
    if resp.status_code >= 300:
        raise RuntimeError(f"paper_positions latest date failed: {resp.status_code} {resp.text}")
    rows = resp.json()
    if not rows:
        return None, []
    last_date = rows[0]["date"]

    params2 = [
        ("select", "date,portfolio_id,ticker,qty,avg_cost,market_value,entry_date,eligible_sell_date,rules_json"),
        ("portfolio_id", f"eq.{portfolio_id}"),
        ("date", f"eq.{last_date}"),
        ("order", "ticker.asc"),
    ]
    resp2 = requests.get(url, headers=supabase_headers(), params=params2, timeout=15)
    if resp2.status_code >= 300:
        raise RuntimeError(f"paper_positions fetch failed: {resp2.status_code} {resp2.text}")
    return last_date, resp2.json()


def eligible_to_sell(pos: Dict, trade_date: dt.date) -> bool:
    eligible = pos.get("eligible_sell_date")
    if eligible:
        return dt.date.fromisoformat(eligible) <= trade_date
    entry = pos.get("entry_date")
    if not entry:
        return True
    eligible2 = (pd.Timestamp(dt.date.fromisoformat(entry)) + pd.tseries.offsets.BDay(MIN_HOLD_DAYS)).date()
    return eligible2 <= trade_date


def fetch_existing_order_ids(trade_date: dt.date, ticker: str, side: str) -> List[str]:
    """Best-effort de-dupe guard.

    paper_orders table does not currently have portfolio_id, so we can only
    de-dupe by date+ticker+side.
    """

    base = supabase_base()
    url = f"{base}/rest/v1/paper_orders"
    params = [
        ("select", "order_id"),
        ("date", f"eq.{trade_date.isoformat()}"),
        ("ticker", f"eq.{ticker}"),
        ("side", f"eq.{side}"),
        ("limit", "5"),
    ]
    try:
        resp = requests.get(url, headers=supabase_headers(), params=params, timeout=15)
        if resp.status_code >= 300:
            return []
        rows = resp.json() or []
        return [r.get("order_id") for r in rows if r.get("order_id")]
    except Exception:
        return []


def upsert(table: str, rows: List[Dict], conflict_cols: List[str]) -> None:
    """Upsert rows into Supabase.

    Backward compatible: if optional metadata columns (e.g. rules_json) are not
    deployed yet, retry once after stripping them.
    """
    if not rows:
        return
    base = supabase_base()
    url = f"{base}/rest/v1/{table}"
    headers = supabase_headers()
    headers["Prefer"] = "resolution=merge-duplicates"
    params = {"on_conflict": ",".join(conflict_cols)}

    def post(payload: List[Dict]) -> requests.Response:
        return requests.post(url, headers=headers, params=params, json=payload, timeout=30)

    resp = post(rows)
    if resp.status_code < 300:
        return

    text = resp.text or ""
    if "rules_json" in text and any(k in text.lower() for k in ["column", "schema cache", "unknown"]):
        stripped = [{k: v for k, v in r.items() if k != "rules_json"} for r in rows]
        resp2 = post(stripped)
        if resp2.status_code < 300:
            return
        raise RuntimeError(f"{table} upsert failed (retry): {resp2.status_code} {resp2.text}")

    raise RuntimeError(f"{table} upsert failed: {resp.status_code} {resp.text}")


def fetch_recent_docs_recent(limit: int = 400, lookback_days: int = 3) -> List[Dict]:
    """Fetch recent cleaned docs (joined to docs_raw) for batch catalyst scoring."""
    base = supabase_base()
    url = f"{base}/rest/v1/docs_text"
    since = (dt.datetime.now(dt.timezone.utc) - dt.timedelta(days=lookback_days)).isoformat()
    select = "doc_id,cleaned_text,docs_raw!inner(url,source,published_at,observed_at)"
    params = [
        ("select", select),
        ("docs_raw.observed_at", f"gte.{since}"),
        ("order", "docs_raw(observed_at).desc"),
        ("limit", str(limit)),
    ]
    r = requests.get(url, headers=supabase_headers(), params=params, timeout=25)
    if r.status_code >= 300:
        return []
    return r.json() or []


def fetch_recent_docs_for_ticker(ticker: str, since_date: dt.date, limit: int = 5) -> List[Dict]:
    """Fetch recent cleaned docs that mention ticker (best-effort, simple text match)."""
    base = supabase_base()
    url = f"{base}/rest/v1/docs_text"

    # Join docs_raw for metadata.
    select = "doc_id,cleaned_text,docs_raw!inner(url,source,published_at)"
    like1 = f"%${ticker}%"
    like2 = f"% {ticker} %"
    like3 = f"%({ticker})%"

    params = [
        ("select", select),
        ("docs_raw.published_at", f"gte.{since_date.isoformat()}"),
        ("order", "docs_raw.published_at.desc"),
        ("limit", str(limit)),
        # OR filter for mentions
        ("or", f"(cleaned_text.ilike.{like1},cleaned_text.ilike.{like2},cleaned_text.ilike.{like3})"),
    ]

    resp = requests.get(url, headers=supabase_headers(), params=params, timeout=20)
    if resp.status_code >= 300:
        return []
    return resp.json() or []


def research_likely_good(ticker: str, trade_date: dt.date) -> Tuple[bool, str]:
    """Deterministic heuristic to decide if post-event news flow looks positive.

    We intentionally avoid "predicting earnings". This is a post-event filter using
    our ingested news text from docs_text.
    """

    since = trade_date - dt.timedelta(days=CATALYST_NEWS_LOOKBACK_DAYS)
    docs = fetch_recent_docs_for_ticker(ticker, since, limit=6)
    if not docs:
        return False, "no recent docs"

    text = "\n".join((d.get("cleaned_text") or "")[:4000] for d in docs).lower()

    pos_words = [
        "beats", "beat estimates", "tops estimates", "raises guidance", "raise guidance", "guidance raised",
        "strong demand", "record", "outperform", "upgrade", "price target raised",
    ]
    neg_words = [
        "misses", "missed estimates", "cuts guidance", "cut guidance", "guidance cut",
        "weak demand", "downgrade", "price target cut", "restatement", "sec investigation",
        "secondary offering", "dilution",
    ]

    pos = sum(text.count(w) for w in pos_words)
    neg = sum(text.count(w) for w in neg_words)

    if neg > 0:
        return False, f"negative flags (neg={neg})"
    if pos >= 2:
        return True, f"positive news keywords (pos={pos})"
    return False, f"insufficient positive signal (pos={pos}, neg={neg})"


def market_note(ind: pd.DataFrame) -> Tuple[str, str]:
    """Return (regime_label, detail) from a broad US index proxy.

    Prefers Supabase prices; falls back to yfinance if proxies are missing.

    Regime logic (simple + robust):
    - risk-on when SPY (or VOO/IVV) is above SMA200
    - "smallcaps-leading" when IWM 60d return > SPY 60d return (if available)
    """

    def from_row(sym: str, row: pd.Series, smallcaps: str | None = None) -> Tuple[str, str]:
        r20 = float(row.get("ret20") or 0.0)
        r60 = float(row.get("ret60") or 0.0)
        vol = float(row.get("vol20") or 0.0)
        sma200 = float(row.get("sma200") or 0.0)
        close = float(row.get("close") or 0.0)
        risk_on = bool(close > sma200) if sma200 else False
        label = "risk-on" if risk_on else "risk-off"

        extra = ""
        if smallcaps:
            extra = f" · {smallcaps}"

        detail = f"{sym} 20d={r20:+.1%} · 60d={r60:+.1%} · vol20={vol:.2%} · close>{'SMA200' if risk_on else 'SMA200? no'}{extra}"
        return label, detail

    # Small-cap relative strength (best-effort)
    smallcaps_note = None
    try:
        spy = ind[ind["ticker"] == "SPY"]
        iwm = ind[ind["ticker"] == "IWM"]
        if not spy.empty and not iwm.empty:
            spy60 = float(spy.iloc[0].get("ret60") or 0.0)
            iwm60 = float(iwm.iloc[0].get("ret60") or 0.0)
            smallcaps_note = ("smallcaps-leading" if iwm60 > spy60 else "smallcaps-lagging") + f" (IWM60-SPY60={iwm60 - spy60:+.1%})"
    except Exception:
        smallcaps_note = None

    for sym in ("SPY", "VOO", "IVV"):
        df = ind[ind["ticker"] == sym]
        if not df.empty:
            return from_row(sym, df.iloc[0], smallcaps=smallcaps_note)

    # Fallback: yfinance
    try:
        d0 = pd.Timestamp(ind["date"].max()).date() if (ind is not None and not ind.empty) else None
        # If we can't infer date, just bail.
        if d0 is None:
            return "unknown", "missing index proxy"

        start = (d0 - dt.timedelta(days=400)).isoformat()
        end = (d0 + dt.timedelta(days=1)).isoformat()
        for sym in ("SPY", "VOO", "IVV"):
            with redirect_stdout(io.StringIO()), redirect_stderr(io.StringIO()):
                bars = yf.download(sym, start=start, end=end, interval="1d", progress=False, auto_adjust=False)
            if bars is None or bars.empty:
                continue
            s = bars["Adj Close"].dropna() if "Adj Close" in bars.columns else bars["Close"].dropna()
            if len(s) < 220:
                continue
            rets = s.pct_change()
            sma200 = s.rolling(200).mean().iloc[-1]
            r20 = (s.iloc[-1] / s.shift(20).iloc[-1] - 1.0)
            r60 = (s.iloc[-1] / s.shift(60).iloc[-1] - 1.0) if len(s) >= 61 else 0.0
            vol20 = rets.rolling(20).std().iloc[-1]
            row = pd.Series({"close": float(s.iloc[-1]), "sma200": float(sma200), "ret20": float(r20), "ret60": float(r60), "vol20": float(vol20)})
            return from_row(sym, row)
    except Exception:
        pass

    return "unknown", "missing index proxy"


def _acquire_lock() -> None:
    """Best-effort non-overlap lock.

    Prevents accidental double-runs (and duplicate Telegram) if timers overlap or
    are manually re-triggered.
    """

    try:
        if LOCK_PATH.exists():
            age = time.time() - LOCK_PATH.stat().st_mtime
            if age > LOCK_STALE_SECONDS:
                # stale lock: remove
                LOCK_PATH.unlink(missing_ok=True)
        # atomic create
        fd = os.open(str(LOCK_PATH), os.O_CREAT | os.O_EXCL | os.O_WRONLY)
        with os.fdopen(fd, "w", encoding="utf-8") as fp:
            fp.write(f"pid={os.getpid()} ts={dt.datetime.now(dt.timezone.utc).isoformat()}\n")
    except FileExistsError:
        raise RuntimeError(f"swing_book lock is held: {LOCK_PATH}")


def _release_lock() -> None:
    try:
        LOCK_PATH.unlink(missing_ok=True)
    except Exception:
        pass


def _state_marker(trade_date: dt.date, mode: str) -> Path:
    STATE_DIR.mkdir(parents=True, exist_ok=True)
    return STATE_DIR / f"swing_book_{trade_date.isoformat()}_{mode}.done"


def _validate_invariants(trade_date: dt.date, held_before: Dict[str, Dict], exits: List[Tuple[str, str]]) -> None:
    """Hard safety checks. If violated, raise so the scheduler flags the run."""

    # Invariant: no rotate/time exits before eligible sell date.
    bad: List[str] = []
    for t, reason in exits:
        if reason in ("rotate", "time"):
            p = held_before.get(t) or {}
            if not eligible_to_sell(p, trade_date):
                bad.append(f"{t}:{reason} (ineligible)")
    if bad:
        raise RuntimeError("Invariant violated: attempted early exit(s): " + ", ".join(bad))

    # Invariant: at most 1 order per ticker+side+date (paper_orders has no portfolio_id)
    # If violated, treat as duplication bug.
    try:
        base = supabase_base()
        url = f"{base}/rest/v1/paper_orders"
        params = [
            ("select", "ticker,side,order_id"),
            ("date", f"eq.{trade_date.isoformat()}"),
            ("limit", "2000"),
        ]
        resp = requests.get(url, headers=supabase_headers(), params=params, timeout=20)
        if resp.status_code < 300:
            rows = resp.json() or []
            counts: Dict[Tuple[str, str], List[str]] = {}
            for r in rows:
                k = (str(r.get("ticker") or ""), str(r.get("side") or ""))
                oid = str(r.get("order_id") or "")
                if k[0] and k[1] and oid:
                    counts.setdefault(k, []).append(oid)
            dup = {k: v for k, v in counts.items() if len(v) > 1}
            if dup:
                sample = "; ".join([f"{k[0]} {k[1]} x{len(v)}" for k, v in list(dup.items())[:8]])
                raise RuntimeError("Invariant violated: duplicate orders detected: " + sample)
    except RuntimeError:
        raise
    except Exception:
        # Don’t fail the whole run on an inability to validate.
        pass


def _fetch_equity_curve(portfolio_id: str, limit: int = 90) -> List[Dict]:
    base = supabase_base()
    url = f"{base}/rest/v1/paper_equity_curve"
    params = [
        ("select", "date,equity,cash,drawdown"),
        ("portfolio_id", f"eq.{portfolio_id}"),
        ("order", "date.desc"),
        ("limit", str(limit)),
    ]
    r = requests.get(url, headers=supabase_headers(), params=params, timeout=20)
    if r.status_code >= 300:
        return []
    return r.json() or []


def _compute_drawdown_from_curve(curve_rows: List[Dict], current_equity: float) -> float:
    """Compute drawdown vs peak equity in provided history (including current)."""
    peak = 0.0
    for row in reversed(curve_rows or []):
        try:
            eq = float(row.get("equity") or 0.0)
        except Exception:
            eq = 0.0
        peak = max(peak, eq)
    peak = max(peak, float(current_equity))
    if peak <= 0:
        return 0.0
    return float((current_equity / peak) - 1.0)


def run(trade_date: dt.date, mode: str = "pre") -> None:
    # Skip weekends/holidays so the cron schedule is safe.
    if not market_is_open(trade_date.isoformat()):
        send_telegram(f"[swing] {trade_date.isoformat()} market closed; skipping.")
        return

    # If trading is paused, exit quietly.
    try:
        from safety_controller import get as safety_get

        st = safety_get() or {}
        if st.get("paused"):
            return
    except Exception:
        pass

    # Idempotency: if this mode already completed today, exit quietly.
    marker = _state_marker(trade_date, mode)
    if marker.exists():
        # quiet: prevents duplicate swing messages/orders
        return

    _acquire_lock()
    import atexit

    atexit.register(_release_lock)

    ensure_portfolio(DEFAULT_PORTFOLIO_ID, DEFAULT_PORTFOLIO_NAME, DEFAULT_CASH)

    universe = load_universe()

    # Include sector ETFs so we can compute rotation/leadership context.
    px = fetch_prices_window(universe + SECTOR_ETFS, trade_date, lookback_days=260)
    ind = compute_indicators(px)

    ranked = rank_candidates(ind)

    regime_label, regime_detail = market_note(ind)

    leaders: List[Tuple[str, float]] = []
    leaders_str = "(n/a)"
    leaders_map: Dict[str, float] = {}
    try:
        from sector_regime import sector_leaders

        leaders = sector_leaders(ind, SECTOR_ETFS)[:5]
        leaders_str = ", ".join([f"{etf}({rs:+.1%})" for etf, rs in leaders[:3]]) if leaders else "(n/a)"
        leaders_map = {etf: rs for etf, rs in leaders}
    except Exception:
        pass

    # Enrich top candidates with sector + basic fundamentals via yfinance (best-effort, cached).
    try:
        from yf_meta import get_meta

        cand = ranked.head(200).copy()
        sectors = []
        mcaps = []
        avgs = []
        sector_etfs = []
        sector_rs = []
        for t in cand["ticker"].tolist():
            meta = get_meta(t) or {}
            sector = meta.get("sector")
            mcap = meta.get("market_cap")
            avg_vol = meta.get("three_month_average_volume") or meta.get("ten_day_average_volume")
            etf = SECTOR_ETF.get(str(sector), None) if sector else None
            rs = float(leaders_map.get(etf, 0.0)) if etf else 0.0
            sectors.append(sector)
            mcaps.append(mcap)
            avgs.append(avg_vol)
            sector_etfs.append(etf)
            sector_rs.append(rs)

        cand["sector"] = sectors
        cand["market_cap"] = mcaps
        cand["avg_volume"] = avgs
        cand["sector_etf"] = sector_etfs
        cand["sector_rs"] = sector_rs

        # Fundamental guardrails
        cand = cand[(cand["market_cap"].isna()) | (cand["market_cap"].astype(float) >= MIN_MARKET_CAP)]
        cand = cand[(cand["avg_volume"].isna()) | (cand["avg_volume"].astype(float) >= MIN_AVG_VOLUME)]

        # Liquidity guardrail: average dollar volume (from Supabase OHLCV) must be reasonable.
        # This helps avoid microstructure traps where spreads/impact dominate.
        if "avg_dollar_vol20" in cand.columns:
            cand = cand[(cand["avg_dollar_vol20"].isna()) | (cand["avg_dollar_vol20"].astype(float) >= MIN_AVG_DOLLAR_VOL)]

        # Catalyst scoring (batch): boost/penalize based on recent docs mentioning the ticker.
        docs = fetch_recent_docs_recent(limit=400, lookback_days=3)
        texts_u = [(d.get("cleaned_text") or "")[:3500].upper() for d in (docs or [])]

        cat_scores: Dict[str, float] = {}
        if texts_u:
            POS = [
                "CONTRACT AWARD",
                "DEFINITIVE AGREEMENT",
                "STRATEGIC ALTERNATIVES",
                "UPGRADE",
                "PRICE TARGET RAISED",
                "RAISES GUIDANCE",
                "BEATS ESTIMATES",
            ]
            NEG = [
                "REGISTERED DIRECT",
                "PUBLIC OFFERING",
                "AT-THE-MARKET",
                "ATM PROGRAM",
                "PRIVATE PLACEMENT",
                "WARRANT",
                "DILUTION",
                "RESTATEMENT",
                "SEC INVESTIGATION",
                "GOING CONCERN",
                "CHAPTER 11",
                "BANKRUPTCY",
                "DELIST",
            ]

            def mentioned(txt: str, t: str) -> bool:
                return (f"${t}" in txt) or (f" {t} " in txt) or (f"({t})" in txt)

            for t in cand["ticker"].tolist():
                rel = [txt for txt in texts_u if mentioned(txt, t)]
                if not rel:
                    cat_scores[t] = 0.0
                    continue
                # Count keywords only within docs that mention the ticker.
                blob_u = "\n".join(rel)
                pos = sum(blob_u.count(w) for w in POS)
                neg = sum(blob_u.count(w) for w in NEG)
                # Lightweight score: mostly penalize dilution/distress.
                cat_scores[t] = float(0.20 * pos - 0.35 * neg)

        cand["catalyst_score"] = [cat_scores.get(t, 0.0) for t in cand["ticker"].tolist()]

        # Sector leadership boost (small) + catalyst score
        cand["score"] = cand["score"] + 0.20 * cand["sector_rs"].fillna(0.0) + cand["catalyst_score"].fillna(0.0)

        ranked = cand.sort_values("score", ascending=False)
    except Exception:
        pass

    if ranked.empty:
        send_telegram(f"[swing] {trade_date.isoformat()} no candidates. {regime_detail}")
        return

    # Regime-aware throttles
    entry_mult = RISK_ON_ENTRY_MULT if regime_label == "risk-on" else RISK_OFF_ENTRY_MULT if regime_label == "risk-off" else 1.0
    max_positions_eff = int(max(1, round(MAX_POSITIONS * (1.0 if regime_label == "risk-on" else RISK_OFF_MAX_POSITIONS_MULT if regime_label == "risk-off" else 1.0))))

    # Earnings avoid rule: do not open new positions into earnings within the next N sessions.
    pre_targets = ranked.head(80)["ticker"].tolist()  # limit API calls
    filtered, avoided = filter_earnings_avoid(pre_targets, trade_date, EARNINGS_AVOID_DAYS)
    targets = filtered[:max_positions_eff]

    # Portfolio state
    _, positions = fetch_latest_positions(DEFAULT_PORTFOLIO_ID, trade_date.isoformat())
    held = {p["ticker"]: p for p in positions if float(p.get("qty") or 0) > 0}

    def stop_level(ticker: str, avg_cost: float) -> Optional[float]:
        row = ind[ind["ticker"] == ticker]
        if row.empty:
            return None
        atr = row.iloc[0].get("atr14")
        if atr is None or pd.isna(atr):
            return None
        return float(avg_cost) - ATR_STOP_MULT * float(atr)

    # Decide exits:
    # - Hard stop-loss breach exits immediately (even if not yet eligible to sell)
    # - Trailing stop (uses high-watermark since entry) exits immediately if hit
    # - Partial profit-taking (once eligible): scale out at +2 ATR from entry
    # - Time stop: if held long enough with insufficient progress, exit once eligible
    # - Otherwise, if eligible and (no longer in targets OR close below SMA50)

    held_before_exits = dict(held)
    exits: List[Tuple[str, str]] = []  # (ticker, reason) full exit
    partial_sells: List[Tuple[str, float, str]] = []  # (ticker, qty, reason)

    # Build high-watermarks from Supabase price window (cheap) for held names.
    px_map: Dict[str, pd.DataFrame] = {}
    if not px.empty:
        for t, g in px.groupby("ticker"):
            px_map[str(t)] = g.sort_values("date")

    def high_since_entry(ticker: str, entry_iso: str) -> Optional[float]:
        try:
            ed = pd.to_datetime(entry_iso)
        except Exception:
            return None
        g = px_map.get(ticker)
        if g is None or g.empty:
            return None
        g2 = g[g["date"] >= ed]
        if g2.empty:
            return None
        try:
            return float(g2["px"].astype(float).max())
        except Exception:
            return None

    for t, p in list(held.items()):
        row = ind[ind["ticker"] == t]
        close_px = float(row.iloc[0]["close"]) if not row.empty else None

        qty = float(p.get("qty") or 0.0)
        if qty <= 0:
            continue

        avg_cost = float(p.get("avg_cost") or 0.0)
        atr_now = None
        if not row.empty:
            v = row.iloc[0].get("atr14")
            if v is not None and not pd.isna(v):
                atr_now = float(v)

        # Hard stop
        st = stop_level(t, avg_cost)
        if close_px is not None and st is not None and close_px <= st:
            exits.append((t, "stop"))
            continue

        # Trailing stop (only if we have ATR + entry date)
        entry_iso = str(p.get("entry_date") or "")
        if close_px is not None and atr_now is not None and entry_iso:
            hi = high_since_entry(t, entry_iso)
            if hi is not None:
                trail = float(hi) - ATR_STOP_MULT * float(atr_now)
                # Only activate trailing after some progress (avoids immediate whipsaw)
                if float(hi) >= (avg_cost + 1.0 * float(atr_now)) and close_px <= trail:
                    exits.append((t, "trail"))
                    continue

        # From here: only eligible-to-sell logic
        if not eligible_to_sell(p, trade_date):
            continue

        # Partial profit-taking: scale out 50% at +2 ATR from entry
        if close_px is not None and atr_now is not None and qty >= 2:
            tp_level = avg_cost + 2.0 * float(atr_now)
            already_scaled = False
            try:
                rj = p.get("rules_json") or {}
                already_scaled = bool((rj.get("scaled_out") is True) or (rj.get("take_profit_2atr") is True))
            except Exception:
                already_scaled = False

            if (not already_scaled) and close_px >= tp_level:
                partial_qty = math.floor(qty / 2.0)
                if partial_qty >= 1:
                    partial_sells.append((t, float(partial_qty), "take_profit"))

        # Time stop: after TIME_STOP_DAYS business days, if no meaningful progress, exit.
        try:
            entry_date = dt.date.fromisoformat(entry_iso) if entry_iso else None
        except Exception:
            entry_date = None
        if entry_date is not None:
            held_days = int(np.busday_count(entry_date.isoformat(), trade_date.isoformat()))
            if held_days >= TIME_STOP_DAYS and close_px is not None and atr_now is not None:
                thresh = avg_cost + TIME_STOP_PROGRESS_ATR * float(atr_now)
                if close_px < thresh:
                    exits.append((t, "time"))
                    continue

        below = False
        if close_px is not None and not row.empty:
            below = close_px < float(row.iloc[0]["sma50"])
        if (t not in targets) or below:
            exits.append((t, "rotate"))

    # Decide entries: targets not held
    entries = [t for t in targets if t not in held]

    # Cash: use latest equity curve if exists
    base = supabase_base()
    eq_url = f"{base}/rest/v1/paper_equity_curve"
    eq_params = [("select", "cash"), ("portfolio_id", f"eq.{DEFAULT_PORTFOLIO_ID}"), ("date", f"lt.{trade_date.isoformat()}"), ("order", "date.desc"), ("limit", "1")]
    eq_resp = requests.get(eq_url, headers=supabase_headers(), params=eq_params, timeout=15)
    cash = DEFAULT_CASH
    if eq_resp.status_code < 300 and eq_resp.json():
        c = eq_resp.json()[0].get("cash")
        if c is not None:
            cash = float(c)

    orders: List[Dict] = []
    fills: List[Dict] = []

    run_id = dt.datetime.now(dt.timezone.utc).strftime("%Y%m%d%H%M%S")

    def daily_proxy(ticker: str) -> Optional[float]:
        r = ind[ind["ticker"] == ticker]
        if r.empty:
            return None
        # ohlc proxy not available here; use close as conservative
        return float(r.iloc[0]["close"])

    # Partial sells (take-profit scaling)
    for t, qty_part, reason in partial_sells:
        if fetch_existing_order_ids(trade_date, t, "sell"):
            # If something already sold today, don't double-sell.
            continue
        if t not in held:
            continue
        qty = float(qty_part)
        if qty <= 0 or qty >= float(held[t].get("qty") or 0.0):
            continue
        vwap = first_hour_vwap_yf_1h(t, trade_date.isoformat()) or daily_proxy(t)
        if vwap is None:
            continue
        fill_price = vwap * (1 - SLIPPAGE_BPS / 10_000.0)
        notional = fill_price * qty
        fees = notional * (FEES_BPS / 10_000.0)
        cash += notional - fees

        row = ind[ind["ticker"] == t]
        bench_px = float(row.iloc[0]["close"]) if not row.empty else fill_price
        impl_shortfall_per_share = (bench_px - fill_price)

        order_id = f"{run_id}-SELL-PART-{t}"
        orders.append({
            "order_id": order_id,
            "date": trade_date.isoformat(),
            "ticker": t,
            "side": "sell",
            "target_weight": 0.0,
            "qty_estimate": qty,
            "status": "filled",
            "rules_json": {
                "benchmark_price": round(bench_px, 6),
                "benchmark_method": "last_close_available",
                "fill_price": round(fill_price, 6),
                "implementation_shortfall_per_share": round(impl_shortfall_per_share, 6),
                "implementation_shortfall_dollars": round(impl_shortfall_per_share * qty, 2),
                "source": f"partial_{reason}",
            },
        })
        fills.append({"fill_id": f"{order_id}-FILL", "order_id": order_id, "fill_price": round(fill_price, 6), "fill_method": "first_hour_vwap_1h_yfinance", "slippage_bps": SLIPPAGE_BPS, "fees": round(fees, 6), "filled_at": dt.datetime.now(dt.timezone.utc).isoformat()})

        # Reduce held qty and mark scaled_out in rules_json (persisted later in positions_out)
        held_qty = float(held[t].get("qty") or 0.0)
        held[t]["qty"] = max(0.0, held_qty - qty)
        try:
            rj = held[t].get("rules_json") or {}
            rj["scaled_out"] = True
            rj["take_profit_2atr"] = True
            held[t]["rules_json"] = rj
        except Exception:
            pass

    # Full sells
    for t, reason in exits:
        # De-dupe: if we already placed a sell for this ticker today, skip.
        if fetch_existing_order_ids(trade_date, t, "sell"):
            continue

        qty = float(held[t].get("qty") or 0.0)
        if qty <= 0:
            continue
        vwap = first_hour_vwap_yf_1h(t, trade_date.isoformat()) or daily_proxy(t)
        if vwap is None:
            continue
        fill_price = vwap * (1 - SLIPPAGE_BPS / 10_000.0)
        notional = fill_price * qty
        fees = notional * (FEES_BPS / 10_000.0)
        cash += notional - fees

        # Implementation Shortfall benchmark (decision price): latest available close.
        row = ind[ind["ticker"] == t]
        bench_px = float(row.iloc[0]["close"]) if not row.empty else fill_price
        impl_shortfall_per_share = (bench_px - fill_price)  # sell sign=-1 => -1*(fill-bench) = bench-fill

        order_id = f"{run_id}-SELL-{t}"
        orders.append({
            "order_id": order_id,
            "date": trade_date.isoformat(),
            "ticker": t,
            "side": "sell",
            "target_weight": 0.0,
            "qty_estimate": qty,
            "status": "filled",
            "rules_json": {
                "benchmark_price": round(bench_px, 6),
                "benchmark_method": "last_close_available",
                "fill_price": round(fill_price, 6),
                "implementation_shortfall_per_share": round(impl_shortfall_per_share, 6),
                "implementation_shortfall_dollars": round(impl_shortfall_per_share * qty, 2),
                "source": f"exit_{reason}",
            },
        })
        fills.append({"fill_id": f"{order_id}-FILL", "order_id": order_id, "fill_price": round(fill_price, 6), "fill_method": "first_hour_vwap_1h_yfinance", "slippage_bps": SLIPPAGE_BPS, "fees": round(fees, 6), "filled_at": dt.datetime.now(dt.timezone.utc).isoformat()})
        held.pop(t, None)

    # Buys (two-stage):
    # 1) Post-close catalyst adds (only in mode=post)
    # 2) Regular target buys (equal-ish allocation)

    # Best-effort sector exposure tracking (for diversification constraints)
    _meta_cache: Dict[str, Dict] = {}

    def sector_etf_for(ticker: str) -> Optional[str]:
        try:
            from yf_meta import get_meta

            if ticker not in _meta_cache:
                _meta_cache[ticker] = get_meta(ticker) or {}
            sector = _meta_cache[ticker].get("sector")
            if not sector:
                return None
            return SECTOR_ETF.get(str(sector))
        except Exception:
            return None

    def held_exposures(equity_now: float) -> Tuple[float, Dict[str, float]]:
        """Return (gross_exposure_pct, sector_exposure_pct_by_etf)."""
        gross = 0.0
        sec: Dict[str, float] = {}
        for t, p in held.items():
            qty = float(p.get("qty") or 0.0)
            if qty <= 0:
                continue
            px_close = daily_proxy(t) or float(p.get("avg_cost") or 0.0)
            mv = px_close * qty
            gross += mv
            etf = sector_etf_for(t)
            if etf:
                sec[etf] = sec.get(etf, 0.0) + mv
        if equity_now <= 0:
            return 0.0, {}
        return gross / equity_now, {k: v / equity_now for k, v in sec.items()}

    def estimate_equity_now() -> float:
        total = cash
        for t, p in held.items():
            qty = float(p.get("qty") or 0.0)
            if qty <= 0:
                continue
            px_close = daily_proxy(t) or float(p.get("avg_cost") or 0.0)
            total += px_close * qty
        return float(total)

    catalyst_buys: List[str] = []
    catalyst_reasons: Dict[str, str] = {}

    if mode == "post":
        # Candidates for catalyst research: from our ranked list (already trend-filtered)
        # limited to reduce Yahoo calls.
        post_cands = ranked.head(40)["ticker"].tolist()
        for t in post_cands:
            if t in held:
                continue
            ed = next_earnings_date(t)
            if ed is None:
                continue
            if ed.isoformat() != trade_date.isoformat():
                continue
            ok, why = research_likely_good(t, trade_date)
            if ok:
                catalyst_buys.append(t)
                catalyst_reasons[t] = why

    # Execute catalyst buys with strict caps + same ATR risk sizing.
    equity_now = estimate_equity_now()
    catalyst_budget_total = CATALYST_MAX_EQUITY_TOTAL * equity_now
    catalyst_budget_name = CATALYST_MAX_EQUITY_PER_NAME * equity_now

    max_notional = MAX_EQUITY_PER_NAME * equity_now

    def risk_pct_for_trade(source: str, rank_idx: int, rank_total: int, fill_price: float, atr: float) -> float:
        """Adjust risk-per-trade based on confidence + risk.

        Also applies regime-based throttling (entry_mult): in risk-off, new entries are sized down.

        - catalyst trades start more conservative.
        - top-ranked names can get a small bump.
        - very high ATR% names get reduced risk.
        """
        pct = float(RISK_PER_TRADE_BASE_PCT)
        if source == "catalyst":
            pct = min(pct, 0.03)

        # confidence proxy: position in ranked list
        if rank_total > 0:
            frac = rank_idx / max(1, rank_total - 1)
            if frac <= 0.15:
                pct += 0.01
            elif frac >= 0.70:
                pct -= 0.02

        # risk proxy: ATR stop distance as % of price
        atr_pct = (ATR_STOP_MULT * atr) / max(0.01, fill_price)
        if atr_pct >= 0.12:
            pct -= 0.02
        elif atr_pct >= 0.08:
            pct -= 0.01

        pct = float(min(RISK_PER_TRADE_MAX_PCT, max(RISK_PER_TRADE_MIN_PCT, pct)))
        # Regime throttle
        pct = pct * float(entry_mult)
        # Keep within min/max even after throttle
        return float(min(RISK_PER_TRADE_MAX_PCT, max(0.0, pct)))

    slots = max_positions_eff - len(held)
    catalyst_buys = catalyst_buys[: max(0, slots)]

    catalyst_allocated = 0.0
    for t in catalyst_buys:
        if slots <= 0:
            break
        if catalyst_allocated >= catalyst_budget_total:
            break

        row = ind[ind["ticker"] == t]
        if row.empty or row.iloc[0].get("atr14") is None or pd.isna(row.iloc[0].get("atr14")):
            continue
        atr = float(row.iloc[0]["atr14"])

        vwap = first_hour_vwap_yf_1h(t, trade_date.isoformat()) or daily_proxy(t)
        if vwap is None:
            continue
        fill_price = vwap * (1 + SLIPPAGE_BPS / 10_000.0)

        st = fill_price - ATR_STOP_MULT * atr
        risk_per_share = max(0.01, fill_price - st)

        # Caps: catalyst bucket caps, plus global max/name notional.
        dollars_cap = min(
            catalyst_budget_name,
            catalyst_budget_total - catalyst_allocated,
            max_notional,
            cash,
        )
        if dollars_cap <= 25:
            continue

        cost_per_share = fill_price * (1 + FEES_BPS / 10_000.0)

        risk_pct = risk_pct_for_trade("catalyst", catalyst_buys.index(t), max(1, len(catalyst_buys)), fill_price, atr)
        risk_budget = risk_pct * equity_now

        shares_risk = math.floor(risk_budget / risk_per_share)
        shares_cap = math.floor(dollars_cap / cost_per_share)

        shares = int(max(0, min(shares_risk, shares_cap)))
        if shares <= 0:
            continue

        # Portfolio constraints: gross exposure + sector exposure
        proposed_mv = float(fill_price * shares)
        gross_pct, sector_pct = held_exposures(equity_now)
        if (gross_pct + (proposed_mv / max(1.0, equity_now))) > MAX_GROSS_EXPOSURE_PCT:
            continue
        etf = sector_etf_for(t)
        if etf:
            if (sector_pct.get(etf, 0.0) + (proposed_mv / max(1.0, equity_now))) > MAX_SECTOR_EXPOSURE_PCT:
                continue

        total_notional = proposed_mv
        fees = total_notional * (FEES_BPS / 10_000.0)
        total_cost = total_notional + fees
        if total_cost > cash:
            continue

        cash -= total_cost
        catalyst_allocated += total_cost
        slots -= 1

        order_id = f"{run_id}-CATALYST-BUY-{t}"
        orders.append({"order_id": order_id, "date": trade_date.isoformat(), "ticker": t, "side": "buy", "target_weight": 0.0, "qty_estimate": shares, "status": "filled"})
        fills.append({"fill_id": f"{order_id}-FILL", "order_id": order_id, "fill_price": round(fill_price, 6), "fill_method": "first_hour_vwap_1h_yfinance", "slippage_bps": SLIPPAGE_BPS, "fees": round(fees, 6), "filled_at": dt.datetime.now(dt.timezone.utc).isoformat()})

        eligible_sell_date = (pd.Timestamp(trade_date) + pd.tseries.offsets.BDay(MIN_HOLD_DAYS)).date()
        held[t] = {
            "ticker": t,
            "qty": shares,
            "avg_cost": fill_price,
            "entry_date": trade_date.isoformat(),
            "eligible_sell_date": eligible_sell_date.isoformat(),
            "rules_json": {"scaled_out": False, "take_profit_2atr": False},
        }

    # Regular buys (from targets not held), sized by risk using ATR stop.
    buys = entries[: max(0, slots)]
    if buys:
        equity_now = estimate_equity_now()
        max_notional = MAX_EQUITY_PER_NAME * equity_now

        for i, t in enumerate(buys):
            row = ind[ind["ticker"] == t]
            if row.empty or row.iloc[0].get("atr14") is None or pd.isna(row.iloc[0].get("atr14")):
                continue
            atr = float(row.iloc[0]["atr14"])

            vwap = first_hour_vwap_yf_1h(t, trade_date.isoformat()) or daily_proxy(t)
            if vwap is None:
                continue
            fill_price = vwap * (1 + SLIPPAGE_BPS / 10_000.0)

            st = fill_price - ATR_STOP_MULT * atr
            risk_per_share = max(0.01, fill_price - st)

            risk_pct = risk_pct_for_trade("regular", i, max(1, len(buys)), fill_price, atr)
            risk_budget = risk_pct * equity_now

            # Implementation Shortfall benchmark (decision price): latest available close in indicators.
            bench_px = float(row.iloc[0]["close"]) if not row.empty else fill_price

            # Shares by risk
            shares_risk = math.floor(risk_budget / risk_per_share)

            # Shares by notional cap and available cash
            cost_per_share = fill_price * (1 + FEES_BPS / 10_000.0)
            shares_cap = math.floor(max_notional / cost_per_share)
            shares_cash = math.floor(cash / cost_per_share)

            shares = int(max(0, min(shares_risk, shares_cap, shares_cash)))
            if shares <= 0:
                continue

            # Portfolio constraints: gross exposure + sector exposure
            proposed_mv = float(fill_price * shares)
            gross_pct, sector_pct = held_exposures(equity_now)
            if (gross_pct + (proposed_mv / max(1.0, equity_now))) > MAX_GROSS_EXPOSURE_PCT:
                continue
            etf = sector_etf_for(t)
            if etf:
                if (sector_pct.get(etf, 0.0) + (proposed_mv / max(1.0, equity_now))) > MAX_SECTOR_EXPOSURE_PCT:
                    continue

            total_notional = proposed_mv
            fees = total_notional * (FEES_BPS / 10_000.0)
            total_cost = total_notional + fees
            if total_cost > cash:
                continue
            cash -= total_cost

            order_id = f"{run_id}-BUY-{t}"
            impl_shortfall_per_share = (fill_price - bench_px)  # buy sign=+1
            orders.append({
                "order_id": order_id,
                "date": trade_date.isoformat(),
                "ticker": t,
                "side": "buy",
                "target_weight": 0.0,
                "qty_estimate": shares,
                "status": "filled",
                "rules_json": {
                    "benchmark_price": round(bench_px, 6),
                    "benchmark_method": "last_close_available",
                    "entry_price": round(fill_price, 6),
                    "implementation_shortfall_per_share": round(impl_shortfall_per_share, 6),
                    "implementation_shortfall_dollars": round(impl_shortfall_per_share * shares, 2),
                    "atr14": round(atr, 6),
                    "stop_price": round(st, 6),
                    "risk_per_share": round(risk_per_share, 6),
                    "risk_budget": round(risk_budget, 2),
                    "risk_pct": round(risk_pct, 4),
                    "time_stop_days": TIME_STOP_DAYS,
                    "time_stop_progress_atr": TIME_STOP_PROGRESS_ATR,
                    "source": "regular",
                },
            })
            fills.append({"fill_id": f"{order_id}-FILL", "order_id": order_id, "fill_price": round(fill_price, 6), "fill_method": "first_hour_vwap_1h_yfinance", "slippage_bps": SLIPPAGE_BPS, "fees": round(fees, 6), "filled_at": dt.datetime.now(dt.timezone.utc).isoformat()})

            eligible_sell_date = (pd.Timestamp(trade_date) + pd.tseries.offsets.BDay(MIN_HOLD_DAYS)).date()
            held[t] = {
                "ticker": t,
                "qty": shares,
                "avg_cost": fill_price,
                "entry_date": trade_date.isoformat(),
                "eligible_sell_date": eligible_sell_date.isoformat(),
                "rules_json": {"scaled_out": False, "take_profit_2atr": False},
            }

    # Mark positions using latest close
    positions_out: List[Dict] = []
    for t, p in sorted(held.items()):
        qty = float(p.get("qty") or 0.0)
        if qty <= 0:
            continue
        px_close = daily_proxy(t) or float(p.get("avg_cost") or 0.0)
        row = ind[ind["ticker"] == t]
        atr_now = None
        if not row.empty:
            v = row.iloc[0].get("atr14")
            if v is not None and not pd.isna(v):
                atr_now = float(v)
        avg_cost = float(p.get("avg_cost") or 0.0)
        st_indic = stop_level(t, avg_cost)
        prev_rj = {}
        try:
            prev_rj = p.get("rules_json") or {}
        except Exception:
            prev_rj = {}

        positions_out.append({
            "date": trade_date.isoformat(),
            "portfolio_id": DEFAULT_PORTFOLIO_ID,
            "ticker": t,
            "qty": round(qty, 6),
            "avg_cost": round(avg_cost, 6),
            "market_value": round(px_close * qty, 6),
            "entry_date": p.get("entry_date"),
            "eligible_sell_date": p.get("eligible_sell_date"),
            "rules_json": {
                **(prev_rj if isinstance(prev_rj, dict) else {}),
                "atr14_now": round(atr_now, 6) if atr_now is not None else None,
                "stop_price_indicative": round(st_indic, 6) if st_indic is not None else None,
                "time_stop_days": TIME_STOP_DAYS,
                "time_stop_progress_atr": TIME_STOP_PROGRESS_ATR,
            },
        })

    invested = float(sum(r["market_value"] for r in positions_out))
    equity = invested + cash

    # Drawdown + daily loss brake (risk engine)
    curve = _fetch_equity_curve(DEFAULT_PORTFOLIO_ID, limit=120)
    # Daily P&L proxy: compare to last equity row (if present)
    prev_equity = None
    if curve:
        try:
            prev_equity = float(curve[0].get("equity") or 0.0)
        except Exception:
            prev_equity = None

    dd = _compute_drawdown_from_curve(curve, equity)
    daily_ret = None
    if prev_equity and prev_equity > 0:
        daily_ret = (equity / prev_equity) - 1.0

    equity_row = {
        "date": trade_date.isoformat(),
        "portfolio_id": DEFAULT_PORTFOLIO_ID,
        "equity": round(equity, 6),
        "cash": round(cash, 6),
        "drawdown": round(dd, 6),
        "turnover": 0.0,
        "rules_json": {
            "max_drawdown_pct": MAX_DRAWDOWN_PCT,
            "daily_loss_limit_pct": DAILY_LOSS_LIMIT_PCT,
            "daily_ret": round(daily_ret, 6) if daily_ret is not None else None,
        },
    }

    # Invariants (fail hard so the scheduler notices)
    try:
        _validate_invariants(trade_date, held_before_exits, exits)
    except Exception as e:
        # Trading-impacting: pause further swing runs until human review.
        try:
            from safety_controller import pause as safety_pause

            safety_pause(
                kind="swing_invariant",
                detail=str(e),
                run_context={"date": trade_date.isoformat(), "mode": mode, "exits": exits},
            )
        except Exception:
            pass
        raise

    # Persist
    if orders:
        upsert("paper_orders", orders, ["order_id"])
    if fills:
        upsert("paper_fills", fills, ["fill_id"])
    upsert("paper_positions", positions_out, ["date", "portfolio_id", "ticker"])
    upsert("paper_equity_curve", [equity_row], ["date", "portfolio_id"])

    # Risk brakes: if we breach drawdown or daily loss limits, pause *new entries* until review.
    # (We already executed this run; this prevents subsequent runs from adding risk.)
    try:
        breach = False
        reason = []
        if dd <= -abs(MAX_DRAWDOWN_PCT):
            breach = True
            reason.append(f"drawdown {dd:.1%} <= -{abs(MAX_DRAWDOWN_PCT):.0%}")
        if daily_ret is not None and daily_ret <= -abs(DAILY_LOSS_LIMIT_PCT):
            breach = True
            reason.append(f"day {daily_ret:.1%} <= -{abs(DAILY_LOSS_LIMIT_PCT):.0%}")
        if breach:
            from safety_controller import pause as safety_pause

            safety_pause(
                kind="risk_brake",
                detail="; ".join(reason),
                run_context={"date": trade_date.isoformat(), "mode": mode, "equity": equity, "drawdown": dd, "daily_ret": daily_ret},
            )
            send_telegram(f"[swing] RISK BRAKE engaged: {'; '.join(reason)}. Trading paused.")
    except Exception:
        pass

    # Friendlier Telegram summary (first line becomes bold via telegram_fmt)
    summary_lines = [
        f"Swing — {trade_date.isoformat()}",
        "",
        f"- Regime: {regime_label} ({regime_detail})",
        f"- Sector leaders: {leaders_str}",
        "",
    ]
    top_targets = targets[:10]
    targets_line = ", ".join(top_targets[:5])
    if len(top_targets) > 5:
        targets_line += ", " + ", ".join(top_targets[5:])
    summary_lines.append(f"- Targets: {targets_line}")

    # Compact risk/regime status line (so we can see throttles + constraints at a glance)
    try:
        gross_pct, sector_pct = held_exposures(equity)
        top_sector = None
        if sector_pct:
            top_sector = max(sector_pct.items(), key=lambda kv: kv[1])
        top_sector_str = f"{top_sector[0]} {top_sector[1]:.0%}" if top_sector else "(n/a)"
        dd_pct = dd  # already negative or 0
        throttle_str = "risk-off" if regime_label == "risk-off" else "risk-on" if regime_label == "risk-on" else "unknown"
        applied_entry_mult = entry_mult
        applied_max_pos = max_positions_eff
        summary_lines.append(
            f"- Risk status: gross={gross_pct:.0%}/{MAX_GROSS_EXPOSURE_PCT:.0%} · top-sector={top_sector_str}/{MAX_SECTOR_EXPOSURE_PCT:.0%} · dd={dd_pct:.1%}/{-abs(MAX_DRAWDOWN_PCT):.0%} · day={daily_ret:.1%} (limit -{abs(DAILY_LOSS_LIMIT_PCT):.0%})" if daily_ret is not None else
            f"- Risk status: gross={gross_pct:.0%}/{MAX_GROSS_EXPOSURE_PCT:.0%} · top-sector={top_sector_str}/{MAX_SECTOR_EXPOSURE_PCT:.0%} · dd={dd_pct:.1%}/{-abs(MAX_DRAWDOWN_PCT):.0%}"
        )
        summary_lines.append(
            f"- Regime throttle: {throttle_str} · entry_mult={applied_entry_mult:.2f} · max_positions={applied_max_pos}/{MAX_POSITIONS}"
        )
    except Exception:
        pass

    summary_lines.append(
        f"- Risk model: ATR{ATR_DAYS} stop={ATR_STOP_MULT:.1f}x · risk/trade={RISK_PER_TRADE_BASE_PCT:.1%} (adj {RISK_PER_TRADE_MIN_PCT:.0%}-{RISK_PER_TRADE_MAX_PCT:.0%}) · max/name={MAX_EQUITY_PER_NAME:.0%} · time-stop={TIME_STOP_DAYS}bd/{TIME_STOP_PROGRESS_ATR:.1f}ATR"
    )
    summary_lines.append("")

    # Show indicative stop levels for first few positions (computed from avg_cost and current ATR).
    stops_preview = []
    for t, p in list(sorted(held.items()))[:5]:
        avg_cost = float(p.get("avg_cost") or 0.0)
        st = stop_level(t, avg_cost)
        if st is not None:
            stops_preview.append(f"{t}@{st:.2f}")
    # Stops are useful but noisy; show only when there were buys/sells.
    if stops_preview and (len(buys) > 0 or len(exits) > 0):
        summary_lines.append("- Stops: " + ", ".join(stops_preview))
    if avoided:
        summary_lines.append(
            f"- Earnings-avoided (next {EARNINGS_AVOID_DAYS} sessions): {', '.join(avoided[:10])}{'…' if len(avoided) > 10 else ''}"
        )
    cat_filled = len([o for o in orders if str(o.get("order_id", "")).find("-CATALYST-BUY-") != -1])
    if cat_filled:
        # show up to 5 catalyst reasons
        shown = []
        for t in list(catalyst_reasons.keys())[:5]:
            shown.append(f"{t} ({catalyst_reasons[t]})")
        summary_lines.append(
            f"- Catalyst buys: {cat_filled} (cap {CATALYST_MAX_EQUITY_TOTAL:.0%} total, {CATALYST_MAX_EQUITY_PER_NAME:.0%}/name)"
        )
        if shown:
            summary_lines.append("- Catalyst notes: " + "; ".join(shown))

    summary_lines.append("")
    sell_stop = sum(1 for _, r in exits if r == "stop")
    sell_time = sum(1 for _, r in exits if r == "time")
    sell_rotate = sum(1 for _, r in exits if r == "rotate")
    summary_lines.append(
        f"- Trades: sells={len(exits)} (stop={sell_stop}, time={sell_time}, rotate={sell_rotate}) · buys={len(buys)} · positions={len(positions_out)}"
    )
    summary_lines.append(f"- Equity: ${equity:,.2f} · Cash: ${cash:,.2f}")
    # Mark this mode as completed for the day (prevents duplicate messages/orders).
    marker.write_text(dt.datetime.now(dt.timezone.utc).isoformat() + "\n", encoding="utf-8")

    # Release lock before messaging (so transient Telegram issues don’t cause reruns).
    _release_lock()

    # Best-effort message
    try:
        send_telegram("\n".join(summary_lines))
    except Exception:
        pass


def main() -> None:
    import argparse

    load_env()

    p = argparse.ArgumentParser(description="Swing book paper trading")
    p.add_argument("--day", default=dt.date.today().isoformat(), help="YYYY-MM-DD")
    p.add_argument("--mode", choices=["pre", "post"], default="pre", help="Run mode: pre-open scan or post-close scan")
    args = p.parse_args()

    trade_date = dt.date.fromisoformat(args.day)
    run(trade_date, mode=args.mode)


if __name__ == "__main__":
    main()
