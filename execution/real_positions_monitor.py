"""Monitor real (non-bot) positions: news + technicals + fundamentals.

Uses deterministic heuristics and sends Telegram updates.

Inputs:
- directives/real_positions.json
- Supabase docs tables for news (best-effort)
- yfinance for prices + basic fundamentals

Commands:
  ./.venv/bin/python -u execution/real_positions_monitor.py --mode digest --when premarket
  ./.venv/bin/python -u execution/real_positions_monitor.py --mode digest --when postclose
  ./.venv/bin/python -u execution/real_positions_monitor.py --mode alerts

Exit:
- prints HEARTBEAT_OK when nothing to do
"""

from __future__ import annotations

import argparse
import datetime as dt
import json
import os
import re
from pathlib import Path
from typing import Dict, List, Optional, Tuple

import numpy as np
import pandas as pd
import requests
import yfinance as yf
from dotenv import load_dotenv

from telegram_fmt import send_telegram


STATE_DIR = Path(__file__).resolve().parents[1] / "output" / "state"

NEG_KWS = [
    "offering",
    "dilution",
    "warrant",
    "restatement",
    "sec investigation",
    "subpoena",
    "going concern",
    "bankruptcy",
    "chapter 11",
    "delist",
    "halt",
    "ransomware",
    "data breach",
    "cyber incident",
]

POS_KWS = [
    "contract award",
    "definitive agreement",
    "strategic alternatives",
    "beats estimates",
    "raises guidance",
    "upgrade",
]


def load_env() -> None:
    env_path = Path(__file__).resolve().parents[1] / ".env"
    if env_path.exists():
        load_dotenv(env_path)


def load_config() -> dict:
    cfg_path = Path(__file__).resolve().parents[1] / "directives" / "real_positions.json"
    return json.loads(cfg_path.read_text(encoding="utf-8"))


def supabase_enabled() -> bool:
    return bool(os.getenv("SUPABASE_URL")) and bool(os.getenv("SUPABASE_SERVICE_ROLE"))


def supabase_base() -> str:
    base = os.getenv("SUPABASE_URL", "")
    if not base:
        raise RuntimeError("SUPABASE_URL not set")
    return base.rstrip("/")


def supabase_headers() -> Dict[str, str]:
    key = os.getenv("SUPABASE_SERVICE_ROLE", "")
    if not key:
        raise RuntimeError("SUPABASE_SERVICE_ROLE not set")
    return {"apikey": key, "Authorization": f"Bearer {key}", "Content-Type": "application/json"}


def fetch_news_mentions(tickers: List[str], lookback_hours: int = 24, limit: int = 200) -> Dict[str, List[dict]]:
    """Best-effort: pull recent docs_text rows and bucket by ticker mention."""
    out: Dict[str, List[dict]] = {t: [] for t in tickers}
    if not tickers or not supabase_enabled():
        return out

    since = (dt.datetime.now(dt.timezone.utc) - dt.timedelta(hours=lookback_hours)).isoformat()
    base = supabase_base()
    url = f"{base}/rest/v1/docs_text"
    select = "doc_id,cleaned_text,docs_raw!inner(url,source,published_at,observed_at)"
    params = [
        ("select", select),
        ("docs_raw.observed_at", f"gte.{since}"),
        ("order", "docs_raw(observed_at).desc"),
        ("limit", str(limit)),
    ]
    r = requests.get(url, headers=supabase_headers(), params=params, timeout=25)
    if r.status_code >= 300:
        return out

    rows = r.json() or []
    texts_u = [(row.get("cleaned_text") or "")[:3500].upper() for row in rows]

    def mentioned(txt: str, t: str) -> bool:
        tu = t.upper()
        return (f"${tu}" in txt) or (f" {tu} " in txt) or (f"({tu})" in txt)

    for row, txtu in zip(rows, texts_u):
        for t in tickers:
            if mentioned(txtu, t):
                out[t].append(row)

    return out


def tech_stats(ticker: str, days: int = 260) -> Optional[dict]:
    """Compute lightweight daily technicals from yfinance."""
    try:
        end = dt.datetime.now(dt.timezone.utc)
        start = end - dt.timedelta(days=days * 2)
        bars = yf.download(
            ticker,
            start=start.date().isoformat(),
            end=(end.date() + dt.timedelta(days=1)).isoformat(),
            interval="1d",
            auto_adjust=False,
            progress=False,
        )
        if bars is None or bars.empty:
            return None

        s = bars["Adj Close"].dropna() if "Adj Close" in bars.columns else bars["Close"].dropna()
        if len(s) < 60:
            return None

        rets = s.pct_change()
        sma20 = s.rolling(20).mean().iloc[-1]
        sma50 = s.rolling(50).mean().iloc[-1]
        sma200 = s.rolling(200).mean().iloc[-1] if len(s) >= 200 else np.nan
        r20 = s.iloc[-1] / s.shift(20).iloc[-1] - 1.0
        r60 = s.iloc[-1] / s.shift(60).iloc[-1] - 1.0
        vol20 = rets.rolling(20).std().iloc[-1]

        # RSI14
        delta = s.diff()
        gain = delta.clip(lower=0).rolling(14).mean()
        loss = (-delta.clip(upper=0)).rolling(14).mean()
        rs = gain / loss.replace(0, np.nan)
        rsi14 = (100 - (100 / (1 + rs))).iloc[-1]

        # ATR14
        high = bars["High"].astype(float)
        low = bars["Low"].astype(float)
        prev = s.shift(1)
        tr = pd.concat([(high - low).abs(), (high - prev).abs(), (low - prev).abs()], axis=1).max(axis=1)
        atr14 = tr.rolling(14).mean().iloc[-1]

        v = bars["Volume"].astype(float) if "Volume" in bars.columns else None
        vol_ratio = None
        if v is not None and not v.dropna().empty:
            v20 = v.rolling(20).mean().iloc[-1]
            v60 = v.rolling(60).mean().iloc[-1]
            if pd.notna(v20) and pd.notna(v60) and v60 != 0:
                vol_ratio = float(v20 / v60)

        px = float(s.iloc[-1])
        trend = "up" if (px > sma50 and (pd.isna(sma200) or sma50 > sma200)) else "down"

        return {
            "px": px,
            "sma20": float(sma20),
            "sma50": float(sma50),
            "sma200": float(sma200) if pd.notna(sma200) else None,
            "ret20": float(r20),
            "ret60": float(r60),
            "vol20": float(vol20) if pd.notna(vol20) else None,
            "rsi14": float(rsi14) if pd.notna(rsi14) else None,
            "atr14": float(atr14) if pd.notna(atr14) else None,
            "vol_ratio": vol_ratio,
            "trend": trend,
        }
    except Exception:
        return None


def fundamentals(ticker: str) -> dict:
    """Best-effort fundamentals via yfinance."""
    out = {}
    try:
        info = yf.Ticker(ticker).info or {}
        keep = [
            "marketCap",
            "sector",
            "industry",
            "trailingPE",
            "forwardPE",
            "priceToBook",
            "profitMargins",
            "beta",
            "dividendYield",
            "shortPercentOfFloat",
            "fiftyTwoWeekLow",
            "fiftyTwoWeekHigh",
        ]
        for k in keep:
            if k in info:
                out[k] = info.get(k)
    except Exception:
        pass
    return out


def news_flags(text: str) -> Tuple[List[str], List[str]]:
    t = (text or "").lower()
    neg = [kw for kw in NEG_KWS if kw in t]
    pos = [kw for kw in POS_KWS if kw in t]
    # de-dupe
    neg = list(dict.fromkeys(neg))
    pos = list(dict.fromkeys(pos))
    return neg[:6], pos[:6]


def _state_path(name: str) -> Path:
    STATE_DIR.mkdir(parents=True, exist_ok=True)
    return STATE_DIR / name


def maybe_alert_move(ticker: str, pct_move: float, msg: str) -> bool:
    """Dedup alerts per ticker per UTC date."""
    key = f"realpos_alert_{ticker}_{dt.datetime.now(dt.timezone.utc).date().isoformat()}.json"
    p = _state_path(key)
    if p.exists():
        return False
    p.write_text(json.dumps({"ticker": ticker, "ts": dt.datetime.now(dt.timezone.utc).isoformat(), "pct_move": pct_move, "msg": msg}), encoding="utf-8")
    send_telegram(msg)
    return True


def digest(when: str) -> None:
    cfg = load_config()
    poss = cfg.get("positions") or []
    tickers = [p["ticker"] for p in poss]

    news = fetch_news_mentions(tickers, lookback_hours=36, limit=250)

    lines = [f"Real positions — {when}", ""]

    for p in poss:
        t = p["ticker"]
        qty = float(p.get("qty") or 0)
        cost = float(p.get("avg_cost") or 0)

        ts = tech_stats(t)
        px = ts["px"] if ts else None
        pl = None
        pl_pct = None
        if px is not None and cost > 0:
            pl = (px - cost) * qty
            pl_pct = (px / cost) - 1.0

        lines.append(f"{t} · qty={qty:g} · cost={cost:.2f}" + (f" · px={px:.2f}" if px is not None else ""))
        if pl is not None and pl_pct is not None:
            lines.append(f"- P/L: {pl:+.2f} ({pl_pct:+.1%})")

        if ts:
            sma200 = ts.get("sma200")
            sma200_str = f"{sma200:.2f}" if isinstance(sma200, (int, float)) and sma200 is not None else "n/a"
            lines.append(
                f"- Tech: trend={ts['trend']} · RSI14={ts.get('rsi14'):.1f} · 20d={ts['ret20']:+.1%} · SMA50={ts['sma50']:.2f} · SMA200={sma200_str} · ATR14={ts.get('atr14'):.2f}"
            )

        fnd = fundamentals(t)
        if fnd:
            sec = fnd.get("sector")
            mcap = fnd.get("marketCap")
            pe = fnd.get("trailingPE")
            lines.append(f"- Fund: sector={sec or 'n/a'} · mcap={mcap or 'n/a'} · PE={pe or 'n/a'}")

        # News
        nrows = news.get(t) or []
        if nrows:
            blob = "\n".join((r.get("cleaned_text") or "")[:1500] for r in nrows[:3])
            neg, pos = news_flags(blob)
            if neg:
                lines.append(f"- News flags: {', '.join(neg)}")
            if pos:
                lines.append(f"- News +: {', '.join(pos)}")
            # show 1-2 links
            links = []
            for r in nrows[:2]:
                md = r.get("docs_raw") or {}
                u = md.get("url")
                if u:
                    links.append(u)
            if links:
                lines.append("- Links: " + " | ".join(links))
        else:
            lines.append("- News: (no recent mentions)")

        lines.append("")

    send_telegram("\n".join(lines).strip())
    print("HEARTBEAT_OK")


def alerts() -> None:
    cfg = load_config()
    poss = cfg.get("positions") or []
    tickers = [p["ticker"] for p in poss]

    pct_thr = float((cfg.get("alerts") or {}).get("pct_move") or 0.05)
    vol_thr = float((cfg.get("alerts") or {}).get("volume_spike_ratio") or 2.0)

    # Price/volume alert checks (yfinance)
    sent = 0
    for p in poss:
        t = p["ticker"]
        ts = tech_stats(t)
        if not ts:
            continue

        # approximate daily move vs SMA20 as proxy if we don't have prev close reliably
        # better: compute last two closes from yfinance quickly
        try:
            bars = yf.download(t, period="7d", interval="1d", auto_adjust=False, progress=False)
            s = bars["Adj Close"].dropna() if (bars is not None and not bars.empty and "Adj Close" in bars.columns) else bars["Close"].dropna()
            if len(s) >= 2:
                pct = float(s.iloc[-1] / s.iloc[-2] - 1.0)
                if abs(pct) >= pct_thr:
                    msg = f"Real position alert: {t} moved {pct:+.1%} (threshold {pct_thr:.0%}). px={float(s.iloc[-1]):.2f}"
                    if maybe_alert_move(t, pct, msg):
                        sent += 1
                        continue
        except Exception:
            pass

        vr = ts.get("vol_ratio")
        if vr is not None and vr >= vol_thr:
            msg = f"Real position alert: {t} volume spike (20d/60d={vr:.2f}x, threshold {vol_thr:.2f}x)."
            if maybe_alert_move(t, 0.0, msg):
                sent += 1

    if sent == 0:
        print("HEARTBEAT_OK")
    else:
        print("HEARTBEAT_OK")


def main() -> None:
    load_env()
    p = argparse.ArgumentParser()
    p.add_argument("--mode", choices=["digest", "alerts"], default="digest")
    p.add_argument("--when", choices=["premarket", "postclose"], default="premarket")
    args = p.parse_args()

    if args.mode == "digest":
        digest(args.when)
    else:
        alerts()


if __name__ == "__main__":
    main()
