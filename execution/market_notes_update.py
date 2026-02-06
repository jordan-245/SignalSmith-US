"""Append a daily market/regime note (deterministic, append-only).

Purpose:
- Maintain a lightweight, continuous log of the market backdrop that the swing
  system is operating within.

Writes:
- docs/MARKET_NOTES.md (append-only)

No LLMs.
"""

from __future__ import annotations

import argparse
import datetime as dt
import os
from pathlib import Path
from typing import Any, Dict, List, Optional, Tuple

import io
import numpy as np
import pandas as pd
import requests
import yfinance as yf
from contextlib import redirect_stderr, redirect_stdout
from dotenv import load_dotenv

REPO = Path(__file__).resolve().parents[1]
OUT_PATH = REPO / "docs" / "MARKET_NOTES.md"

SYMS = [
    "SPY",  # broad
    "QQQ",  # growth/tech proxy
    "IWM",  # small caps proxy
    "TLT",  # duration
    "HYG",  # credit-ish
    "GLD",  # gold
    "USO",  # oil
]


def load_env() -> None:
    env_path = REPO / ".env"
    if env_path.exists():
        load_dotenv(env_path)


def sb_base() -> str:
    base = os.getenv("SUPABASE_URL", "").rstrip("/")
    if not base:
        raise RuntimeError("SUPABASE_URL not set")
    return base


def sb_headers() -> Dict[str, str]:
    key = os.getenv("SUPABASE_SERVICE_ROLE", "")
    if not key:
        raise RuntimeError("SUPABASE_SERVICE_ROLE not set")
    return {"apikey": key, "Authorization": f"Bearer {key}"}


def market_is_open(date_str: str) -> bool:
    try:
        import exchange_calendars as xcals  # type: ignore

        cal = xcals.get_calendar("XNYS")
        return bool(cal.is_session(date_str))
    except Exception:
        d = dt.date.fromisoformat(date_str)
        return d.weekday() < 5


def fetch_prices_supabase(tickers: List[str], end_date: dt.date, lookback_bdays: int = 260) -> pd.DataFrame:
    start_date = (pd.Timestamp(end_date) - pd.tseries.offsets.BDay(lookback_bdays)).date()
    url = f"{sb_base()}/rest/v1/prices_daily"
    cols = "date,ticker,adj_close,close"

    in_list = ",".join([t.upper() for t in tickers])
    params = [
        ("select", cols),
        ("date", f"gte.{start_date.isoformat()}"),
        ("date", f"lte.{end_date.isoformat()}"),
        ("ticker", f"in.({in_list})"),
        ("order", "date.asc"),
    ]
    r = requests.get(url, headers=sb_headers(), params=params, timeout=30)
    if r.status_code >= 300:
        return pd.DataFrame()
    rows = r.json() or []
    if not rows:
        return pd.DataFrame()

    df = pd.DataFrame(rows)
    df["date"] = pd.to_datetime(df["date"])
    df["px"] = df["adj_close"].astype(float).where(df["adj_close"].notna(), df["close"].astype(float))
    return df[["date", "ticker", "px"]]


def fetch_prices_yfinance(tickers: List[str], end_date: dt.date, lookback_days: int = 420) -> pd.DataFrame:
    start = (end_date - dt.timedelta(days=lookback_days)).isoformat()
    end = (end_date + dt.timedelta(days=1)).isoformat()

    frames: List[pd.DataFrame] = []
    for t in tickers:
        try:
            with redirect_stdout(io.StringIO()), redirect_stderr(io.StringIO()):
                bars = yf.download(t, start=start, end=end, interval="1d", progress=False, auto_adjust=False)
            if bars is None or bars.empty:
                continue

            def pick(col: str):
                if isinstance(bars.columns, pd.MultiIndex):
                    if (col, t) in bars.columns:
                        return bars[(col, t)]
                    # sometimes ticker is upper
                    if (col, t.upper()) in bars.columns:
                        return bars[(col, t.upper())]
                    # fallback: first column under that level
                    if col in bars.columns.get_level_values(0):
                        return bars[col].iloc[:, 0]
                    return None
                else:
                    return bars[col] if col in bars.columns else None

            s = pick("Adj Close")
            if s is None:
                s = pick("Close")
            if s is None:
                continue
            s = pd.Series(s).dropna()
            if s.empty:
                continue

            df = pd.DataFrame({"date": pd.to_datetime(s.index), "ticker": t.upper(), "px": s.astype(float).values})
            frames.append(df)
        except Exception:
            continue

    if not frames:
        return pd.DataFrame()
    out = pd.concat(frames, ignore_index=True)
    out = out.sort_values(["ticker", "date"])
    return out


def compute_snapshot(df: pd.DataFrame) -> Dict[str, Dict[str, float]]:
    """Return per-symbol snapshot: close, sma50, sma200, ret20, vol20."""
    out: Dict[str, Dict[str, float]] = {}
    if df.empty:
        return out

    for t, g in df.sort_values(["ticker", "date"]).groupby("ticker"):
        s = g.set_index("date")["px"].astype(float).dropna()
        if len(s) < 220:
            continue
        rets = s.pct_change()
        snap = {
            "close": float(s.iloc[-1]),
            "sma50": float(s.rolling(50).mean().iloc[-1]),
            "sma200": float(s.rolling(200).mean().iloc[-1]),
            "ret20": float(s.iloc[-1] / s.shift(20).iloc[-1] - 1.0),
            "vol20": float(rets.rolling(20).std().iloc[-1]),
        }
        out[str(t).upper()] = snap
    return out


def regime_label(spy: Dict[str, float]) -> str:
    try:
        return "risk-on" if spy["close"] > spy["sma200"] else "risk-off"
    except Exception:
        return "unknown"


def pct(x: Optional[float]) -> str:
    if x is None or (isinstance(x, float) and np.isnan(x)):
        return ""
    return f"{x:+.1%}"


def f2(x: Optional[float]) -> str:
    if x is None or (isinstance(x, float) and np.isnan(x)):
        return ""
    return f"{x:.2f}"


def append_note(day: dt.date, snaps: Dict[str, Dict[str, float]]) -> None:
    OUT_PATH.parent.mkdir(parents=True, exist_ok=True)
    if not OUT_PATH.exists():
        OUT_PATH.write_text("# SignalSmith — Market Notes (append-only)\n\n---\n", encoding="utf-8")

    header = f"## {day.isoformat()}"
    existing = OUT_PATH.read_text(encoding="utf-8")
    if header in existing:
        print("HEARTBEAT_OK")
        return

    now_utc = dt.datetime.now(dt.timezone.utc).replace(microsecond=0)
    try:
        from zoneinfo import ZoneInfo

        aest = ZoneInfo("Australia/Brisbane")
        now_aest = now_utc.astimezone(aest)
        ts_aest = now_aest.isoformat()
    except Exception:
        ts_aest = ""

    spy = snaps.get("SPY") or {}
    qqq = snaps.get("QQQ") or {}
    iwm = snaps.get("IWM") or {}
    tlt = snaps.get("TLT") or {}
    hyg = snaps.get("HYG") or {}
    gld = snaps.get("GLD") or {}
    uso = snaps.get("USO") or {}

    reg = regime_label(spy)

    lines: List[str] = []
    lines.append("\n" + header)
    lines.append(f"- Generated: {now_utc.isoformat().replace('+00:00','Z')}" + (f" | AEST: {ts_aest}" if ts_aest else ""))
    lines.append(f"- Regime: **{reg}** (SPY close {f2(spy.get('close'))} vs SMA200 {f2(spy.get('sma200'))})")
    lines.append("")

    def row(sym: str, snap: Dict[str, float]) -> str:
        if not snap:
            return f"- {sym}: (missing)"
        trend = "above" if snap["close"] > snap["sma200"] else "below"
        return (
            f"- {sym}: 20d {pct(snap.get('ret20'))} | vol20 {pct(snap.get('vol20'))} | close {trend} SMA200"
        )

    lines.append("### Snapshot")
    lines.append(row("SPY", spy))
    lines.append(row("QQQ", qqq))
    lines.append(row("IWM", iwm))
    lines.append(row("TLT", tlt))
    lines.append(row("HYG", hyg))
    lines.append(row("GLD", gld))
    lines.append(row("USO", uso))

    # Simple implications
    lines.append("\n### Implications")
    if reg == "risk-off":
        lines.append("- Prefer liquidity + tighter entry standards; avoid chasing high beta.")
        lines.append("- Treat rallies as sellable until breadth/leadership improves.")
    elif reg == "risk-on":
        lines.append("- Momentum/trend setups have higher hit-rate; allow fuller sizing within risk caps.")
        lines.append("- Still enforce ATR risk sizing; avoid overextension entries.")
    else:
        lines.append("- Regime unclear; keep exposure modest and prioritize clear trend + liquidity.")

    blob = "\n".join(lines) + "\n"
    with OUT_PATH.open("a", encoding="utf-8") as fp:
        fp.write(blob)

    print(f"[ok] appended market note for {day.isoformat()}")


def main() -> None:
    load_env()
    ap = argparse.ArgumentParser()
    ap.add_argument("--day", default=dt.date.today().isoformat(), help="YYYY-MM-DD (market session date)")
    args = ap.parse_args()

    day = dt.date.fromisoformat(args.day)
    if not market_is_open(day.isoformat()):
        print("HEARTBEAT_OK")
        return

    df = fetch_prices_supabase(SYMS, day, lookback_bdays=260)
    snaps = compute_snapshot(df)

    # Fallback: if Supabase doesn’t have these tickers yet, pull from yfinance.
    if not snaps:
        df2 = fetch_prices_yfinance(SYMS, day)
        snaps = compute_snapshot(df2)

    append_note(day, snaps)


if __name__ == "__main__":
    main()
