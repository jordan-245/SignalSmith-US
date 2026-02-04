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
from contextlib import redirect_stderr, redirect_stdout
from pathlib import Path
from typing import Dict, List, Optional, Tuple

import numpy as np
import pandas as pd
import requests
import yfinance as yf
from dotenv import load_dotenv

DEFAULT_PORTFOLIO_ID = "swing"
DEFAULT_PORTFOLIO_NAME = "Swing Book"
DEFAULT_CASH = 5_000.0
MAX_POSITIONS = 10
MIN_HOLD_DAYS = 5  # business days

# Avoid opening new positions into earnings events.
EARNINGS_AVOID_DAYS = 3  # trading sessions ahead (inclusive)

FEES_BPS = 2
SLIPPAGE_BPS = 5

# Commodity proxies / related ETFs (starter set; editable)
PROXIES = [
    "SPY",
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
    bot_token = os.getenv("TELEGRAM_BOT_TOKEN", "")
    chat_id = os.getenv("TELEGRAM_CHAT_ID", "")
    if not bot_token or not chat_id:
        return
    url = f"https://api.telegram.org/bot{bot_token}/sendMessage"
    try:
        requests.post(url, json={"chat_id": chat_id, "text": text}, timeout=15)
    except Exception:
        pass


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
    """Compute basic indicators per ticker (SMA50, SMA200, ret20, vol20, RSI14-ish)."""
    if df.empty:
        return df
    out_rows: List[Dict] = []
    for ticker, g in df.sort_values(["ticker", "date"]).groupby("ticker"):
        s = g.set_index("date")["px"].astype(float).dropna()
        if len(s) < 220:
            continue
        rets = s.pct_change()
        sma50 = s.rolling(50).mean()
        sma200 = s.rolling(200).mean()
        ret20 = (s / s.shift(20) - 1.0)
        vol20 = rets.rolling(20).std()

        # RSI14 (simple): average gains / losses
        delta = s.diff()
        gain = delta.clip(lower=0).rolling(14).mean()
        loss = (-delta.clip(upper=0)).rolling(14).mean()
        rs = gain / loss.replace(0, np.nan)
        rsi14 = 100 - (100 / (1 + rs))

        last_dt = s.index[-1]
        out_rows.append(
            {
                "ticker": ticker,
                "date": last_dt,
                "close": float(s.iloc[-1]),
                "sma50": float(sma50.iloc[-1]),
                "sma200": float(sma200.iloc[-1]),
                "ret20": float(ret20.iloc[-1]),
                "vol20": float(vol20.iloc[-1]) if not pd.isna(vol20.iloc[-1]) else None,
                "rsi14": float(rsi14.iloc[-1]) if not pd.isna(rsi14.iloc[-1]) else None,
            }
        )
    return pd.DataFrame(out_rows)


def rank_candidates(ind: pd.DataFrame) -> pd.DataFrame:
    if ind.empty:
        return ind
    df = ind.copy()
    # Trend filter: close > sma50 > sma200
    df = df[(df["close"] > df["sma50"]) & (df["sma50"] > df["sma200"])]
    # RSI filter: avoid overbought extremes
    df = df[(df["rsi14"].isna()) | ((df["rsi14"] >= 45) & (df["rsi14"] <= 72))]
    # Score: momentum / vol
    df["score"] = df["ret20"] / (df["vol20"].replace(0, np.nan))
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
        ("select", "date,portfolio_id,ticker,qty,avg_cost,market_value,entry_date,eligible_sell_date"),
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


def upsert(table: str, rows: List[Dict], conflict_cols: List[str]) -> None:
    if not rows:
        return
    base = supabase_base()
    url = f"{base}/rest/v1/{table}"
    headers = supabase_headers()
    headers["Prefer"] = "resolution=merge-duplicates"
    params = {"on_conflict": ",".join(conflict_cols)}
    resp = requests.post(url, headers=headers, params=params, json=rows, timeout=30)
    if resp.status_code >= 300:
        raise RuntimeError(f"{table} upsert failed: {resp.status_code} {resp.text}")


def market_note(ind: pd.DataFrame) -> str:
    """Very lightweight regime note from SPY / proxies."""
    spy = ind[ind["ticker"] == "SPY"]
    if spy.empty:
        return "Regime: unknown (missing SPY)."
    r20 = float(spy.iloc[0]["ret20"])
    vol = float(spy.iloc[0]["vol20"] or 0.0)
    trend = "up" if (spy.iloc[0]["close"] > spy.iloc[0]["sma50"] > spy.iloc[0]["sma200"]) else "not-up"
    return f"Regime: SPY 20d={r20:+.1%}, vol20={vol:.2%}, trend={trend}."


def run(trade_date: dt.date) -> None:
    # Skip weekends/holidays so the cron schedule is safe.
    if not market_is_open(trade_date.isoformat()):
        send_telegram(f"[swing] {trade_date.isoformat()} market closed; skipping.")
        return

    ensure_portfolio(DEFAULT_PORTFOLIO_ID, DEFAULT_PORTFOLIO_NAME, DEFAULT_CASH)

    universe = load_universe()
    px = fetch_prices_window(universe, trade_date, lookback_days=260)
    ind = compute_indicators(px)
    ranked = rank_candidates(ind)

    note = market_note(ind)

    if ranked.empty:
        send_telegram(f"[swing] {trade_date.isoformat()} no candidates. {note}")
        return

    # Earnings avoid rule: do not open new positions into earnings within the next N sessions.
    pre_targets = ranked.head(80)["ticker"].tolist()  # limit API calls
    filtered, avoided = filter_earnings_avoid(pre_targets, trade_date, EARNINGS_AVOID_DAYS)
    targets = filtered[:MAX_POSITIONS]

    # Portfolio state
    _, positions = fetch_latest_positions(DEFAULT_PORTFOLIO_ID, trade_date.isoformat())
    held = {p["ticker"]: p for p in positions if float(p.get("qty") or 0) > 0}

    # Decide exits: if eligible and no longer in targets OR close below SMA50
    exits: List[str] = []
    for t, p in held.items():
        if not eligible_to_sell(p, trade_date):
            continue
        row = ind[ind["ticker"] == t]
        below = False
        if not row.empty:
            below = float(row.iloc[0]["close"]) < float(row.iloc[0]["sma50"])
        if (t not in targets) or below:
            exits.append(t)

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

    # Sells
    for t in exits:
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

        order_id = f"{run_id}-SELL-{t}"
        orders.append({"order_id": order_id, "date": trade_date.isoformat(), "ticker": t, "side": "sell", "target_weight": 0.0, "qty_estimate": qty, "status": "filled"})
        fills.append({"fill_id": f"{order_id}-FILL", "order_id": order_id, "fill_price": round(fill_price, 6), "fill_method": "first_hour_vwap_1h_yfinance", "slippage_bps": SLIPPAGE_BPS, "fees": round(fees, 6), "filled_at": dt.datetime.now(dt.timezone.utc).isoformat()})
        held.pop(t, None)

    # Buys
    slots = MAX_POSITIONS - len(held)
    buys = entries[: max(0, slots)]
    if buys:
        alloc = cash / len(buys)
        for t in buys:
            vwap = first_hour_vwap_yf_1h(t, trade_date.isoformat()) or daily_proxy(t)
            if vwap is None:
                continue
            fill_price = vwap * (1 + SLIPPAGE_BPS / 10_000.0)
            cost_per_share = fill_price * (1 + FEES_BPS / 10_000.0)
            shares = math.floor(alloc / cost_per_share) if cost_per_share > 0 else 0
            if shares <= 0:
                continue
            total_notional = fill_price * shares
            fees = total_notional * (FEES_BPS / 10_000.0)
            total_cost = total_notional + fees
            if total_cost > cash:
                continue
            cash -= total_cost

            order_id = f"{run_id}-BUY-{t}"
            orders.append({"order_id": order_id, "date": trade_date.isoformat(), "ticker": t, "side": "buy", "target_weight": round(1.0 / MAX_POSITIONS, 6), "qty_estimate": shares, "status": "filled"})
            fills.append({"fill_id": f"{order_id}-FILL", "order_id": order_id, "fill_price": round(fill_price, 6), "fill_method": "first_hour_vwap_1h_yfinance", "slippage_bps": SLIPPAGE_BPS, "fees": round(fees, 6), "filled_at": dt.datetime.now(dt.timezone.utc).isoformat()})

            eligible_sell_date = (pd.Timestamp(trade_date) + pd.tseries.offsets.BDay(MIN_HOLD_DAYS)).date()
            held[t] = {"ticker": t, "qty": shares, "avg_cost": fill_price, "entry_date": trade_date.isoformat(), "eligible_sell_date": eligible_sell_date.isoformat()}

    # Mark positions using latest close
    positions_out: List[Dict] = []
    for t, p in sorted(held.items()):
        qty = float(p.get("qty") or 0.0)
        if qty <= 0:
            continue
        px_close = daily_proxy(t) or float(p.get("avg_cost") or 0.0)
        positions_out.append({
            "date": trade_date.isoformat(),
            "portfolio_id": DEFAULT_PORTFOLIO_ID,
            "ticker": t,
            "qty": round(qty, 6),
            "avg_cost": round(float(p.get("avg_cost") or 0.0), 6),
            "market_value": round(px_close * qty, 6),
            "entry_date": p.get("entry_date"),
            "eligible_sell_date": p.get("eligible_sell_date"),
        })

    invested = float(sum(r["market_value"] for r in positions_out))
    equity = invested + cash

    equity_row = {"date": trade_date.isoformat(), "portfolio_id": DEFAULT_PORTFOLIO_ID, "equity": round(equity, 6), "cash": round(cash, 6), "drawdown": 0.0, "turnover": 0.0}

    # Persist
    if orders:
        upsert("paper_orders", orders, ["order_id"])
    if fills:
        upsert("paper_fills", fills, ["fill_id"])
    upsert("paper_positions", positions_out, ["date", "portfolio_id", "ticker"])
    upsert("paper_equity_curve", [equity_row], ["date", "portfolio_id"])

    summary_lines = [
        f"[swing] {trade_date.isoformat()} executed.",
        note,
        f"Targets: {', '.join(targets[:10])}",
    ]
    if avoided:
        summary_lines.append(f"Earnings-avoided (next {EARNINGS_AVOID_DAYS} sessions): {', '.join(avoided[:10])}{'…' if len(avoided) > 10 else ''}")
    summary_lines.append(
        f"Trades: sells={len(exits)} buys={len(buys)} positions={len(positions_out)} equity=${equity:,.2f} cash=${cash:,.2f}"
    )
    send_telegram("\n".join(summary_lines))


def main() -> None:
    load_env()
    trade_date = dt.date.today()
    run(trade_date)


if __name__ == "__main__":
    main()
