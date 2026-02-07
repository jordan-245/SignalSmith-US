"""Swing Book risk-parameter grid backtest (deterministic, daily-bars).

Purpose:
- Compare "amounts" (risk per trade, daily loss limit, max drawdown brake, ATR stop multiple)
  under a simplified but faithful version of the swing_book rules.

Notes:
- Uses Supabase prices_daily (adj_close/close/high/low/open/volume).
- Uses daily bars only (no intraday VWAP).
- This is for *relative* comparison of risk knobs, not perfect replication of live fills.

Output:
- Writes markdown summary to docs/SWING_RISK_GRID.md
- Writes CSV results to output/backtests/swing_risk_grid_<date>.csv

Usage:
  ./.venv/bin/python -u execution/swing_backtest_risk_grid.py --years 2

"""

from __future__ import annotations

import argparse
import datetime as dt
import itertools
import math
import os
from dataclasses import dataclass
from pathlib import Path
from typing import Dict, List, Optional, Tuple

import numpy as np
import pandas as pd
import requests
from dotenv import load_dotenv


REPO = Path(__file__).resolve().parents[1]

DEFAULT_PORTFOLIO_EQUITY = float(os.getenv("SWING_BACKTEST_EQUITY", "5000"))
MAX_POSITIONS = 10
MIN_HOLD_DAYS = 5
TIME_STOP_DAYS = 10
TIME_STOP_PROGRESS_ATR = 0.5

FEES_BPS = 2
SLIPPAGE_BPS = 5

ATR_DAYS = 14

# Candidate filters (mirrors swing_book roughly)
RSI_MIN = 45
RSI_MAX = 78
ADX_MIN = 18
MAX_DIST_SMA200 = 0.35

# Regime throttles (same intent as swing_book defaults)
RISK_OFF_ENTRY_MULT = float(os.getenv("SWING_RISK_OFF_ENTRY_MULT", "0.40"))
RISK_OFF_MAX_POSITIONS_MULT = float(os.getenv("SWING_RISK_OFF_MAX_POSITIONS_MULT", "0.50"))


def load_env() -> None:
    env_path = REPO / ".env"
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
    return {"apikey": key, "Authorization": f"Bearer {key}", "Content-Type": "application/json"}


def load_universe() -> List[str]:
    # SP500 + key proxies. (Same file as swing_book)
    tickers_file = REPO / "execution" / "sp500_tickers.txt"
    tickers: List[str] = []
    if tickers_file.exists():
        for line in tickers_file.read_text(encoding="utf-8").splitlines():
            s = line.strip().upper()
            if s:
                tickers.append(s)

    proxies = [
        "SPY",
        "IWM",
        "VOO",
        "IVV",
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
        "XLK",
        "XLF",
        "XLV",
        "XLI",
        "XLY",
        "XLP",
        "XLU",
        "XLB",
        "XLRE",
        "XLC",
    ]

    out: List[str] = []
    seen = set()
    for t in tickers + proxies:
        if t and t not in seen:
            out.append(t)
            seen.add(t)
    return out


def _fetch_yfinance_prices(ticker: str, start: dt.date, end: dt.date) -> pd.DataFrame:
    """Fallback for ETFs/proxies not present in Supabase prices_daily."""
    try:
        import yfinance as yf  # type: ignore

        bars = yf.download(
            ticker,
            start=start.isoformat(),
            end=(end + dt.timedelta(days=1)).isoformat(),
            interval="1d",
            auto_adjust=False,
            progress=False,
        )
        if bars is None or bars.empty:
            return pd.DataFrame()
        # yfinance may return MultiIndex columns; flatten to single-series per field.
        if isinstance(bars.columns, pd.MultiIndex):
            def _col(name: str):
                # common shapes: ("Close", "SPY") or ("Price", "Close") depending on version
                for key in [(name, ticker), ("Price", name), (name, "")]:
                    if key in bars.columns:
                        return bars[key]
                # try first level match
                for c in bars.columns:
                    if len(c) >= 1 and c[0] == name:
                        return bars[c]
                return None

            close = _col("Close")
            high = _col("High")
            low = _col("Low")
            open_ = _col("Open")
            vol = _col("Volume")
            adj = _col("Adj Close")
            df = pd.DataFrame({
                "date": bars.index,
                "ticker": ticker,
                "close": close,
                "high": high,
                "low": low,
                "open": open_,
                "volume": vol,
                "adj_close": adj,
            })
        else:
            df = bars.reset_index().rename(columns={"Date": "date"})
            df["ticker"] = ticker
            df["close"] = df.get("Close")
            df["high"] = df.get("High")
            df["low"] = df.get("Low")
            df["open"] = df.get("Open")
            df["volume"] = df.get("Volume")
            df["adj_close"] = df.get("Adj Close")

        # Normalize dtypes
        df["date"] = pd.to_datetime(df["date"])
        for c in ["adj_close", "close", "high", "low", "open", "volume"]:
            df[c] = pd.to_numeric(df.get(c), errors="coerce")
        df["px"] = df["adj_close"].where(df["adj_close"].notna(), df["close"])
        keep = ["date", "ticker", "adj_close", "close", "high", "low", "open", "volume", "px"]
        return df[keep].dropna(subset=["px"])
    except Exception:
        return pd.DataFrame()


def fetch_prices(tickers: List[str], start: dt.date, end: dt.date) -> pd.DataFrame:
    base = supabase_base()
    url = f"{base}/rest/v1/prices_daily"
    cols = "date,ticker,adj_close,close,high,low,open,volume"

    all_rows: List[Dict] = []

    def chunks(xs: List[str], n: int = 200) -> List[List[str]]:
        return [xs[i : i + n] for i in range(0, len(xs), n)]

    for part in chunks(tickers, 200):
        in_list = ",".join(part)
        params = [
            ("select", cols),
            ("date", f"gte.{start.isoformat()}"),
            ("date", f"lte.{end.isoformat()}"),
            ("ticker", f"in.({in_list})"),
            ("order", "date.asc"),
        ]
        r = requests.get(url, headers=supabase_headers(), params=params, timeout=60)
        if r.status_code >= 300:
            raise RuntimeError(f"prices_daily fetch failed: {r.status_code} {r.text}")
        all_rows.extend(r.json() or [])

    if not all_rows:
        return pd.DataFrame()

    df = pd.DataFrame(all_rows)
    df["date"] = pd.to_datetime(df["date"])
    for c in ["adj_close", "close", "high", "low", "open", "volume"]:
        if c in df.columns:
            df[c] = pd.to_numeric(df[c], errors="coerce")
    df["px"] = df["adj_close"].where(df["adj_close"].notna(), df["close"])
    df = df.dropna(subset=["px"])

    # Ensure key regime proxies exist even if Supabase doesn't store ETFs.
    needed = ["SPY", "IWM"]
    present = set(df["ticker"].astype(str).unique()) if not df.empty else set()
    for t in needed:
        if t not in present:
            yfd = _fetch_yfinance_prices(t, start, end)
            if not yfd.empty:
                df = pd.concat([df, yfd], ignore_index=True)

    return df


def compute_indicators_all(df: pd.DataFrame) -> pd.DataFrame:
    # returns a long DF indexed by (date,ticker) with needed fields
    if df.empty:
        return df

    df = df.sort_values(["ticker", "date"]).copy()

    out = []
    for t, g in df.groupby("ticker", sort=False):
        g = g.sort_values("date").set_index("date")
        s = g["px"].astype(float)
        high = g["high"].astype(float)
        low = g["low"].astype(float)
        rets = s.pct_change()

        sma50 = s.rolling(50).mean()
        sma200 = s.rolling(200).mean()
        ret20 = s / s.shift(20) - 1.0
        ret60 = s / s.shift(60) - 1.0
        vol20 = rets.rolling(20).std()

        # RSI14
        delta = s.diff()
        gain = delta.clip(lower=0).rolling(14).mean()
        loss = (-delta.clip(upper=0)).rolling(14).mean()
        rs = gain / loss.replace(0, np.nan)
        rsi14 = 100 - (100 / (1 + rs))

        # ATR14
        prev_close = s.shift(1)
        tr = pd.concat([(high - low).abs(), (high - prev_close).abs(), (low - prev_close).abs()], axis=1).max(axis=1)
        atr14 = tr.rolling(ATR_DAYS).mean()

        # ADX14
        up_move = high.diff()
        down_move = -low.diff()
        plus_dm = up_move.where((up_move > down_move) & (up_move > 0), 0.0)
        minus_dm = down_move.where((down_move > up_move) & (down_move > 0), 0.0)
        tr14 = tr.rolling(14).sum()
        plus_di = 100 * (plus_dm.rolling(14).sum() / tr14.replace(0, np.nan))
        minus_di = 100 * (minus_dm.rolling(14).sum() / tr14.replace(0, np.nan))
        dx = (100 * (plus_di - minus_di).abs() / (plus_di + minus_di).replace(0, np.nan))
        adx14 = dx.rolling(14).mean()

        dist_sma200 = (s / sma200 - 1.0)

        o = pd.DataFrame(
            {
                "ticker": t,
                "close": s,
                "high": high,
                "low": low,
                "sma50": sma50,
                "sma200": sma200,
                "ret20": ret20,
                "ret60": ret60,
                "vol20": vol20,
                "rsi14": rsi14,
                "atr14": atr14,
                "adx14": adx14,
                "dist_sma200": dist_sma200,
            }
        )
        out.append(o.reset_index())

    ind = pd.concat(out, ignore_index=True)
    ind = ind.dropna(subset=["close", "sma50", "sma200", "ret20", "vol20"])  # need warmup
    ind["date"] = pd.to_datetime(ind["date"])
    return ind


@dataclass
class Position:
    qty: float
    entry_px: float
    entry_date: pd.Timestamp
    eligible_date: pd.Timestamp
    scaled_out: bool = False
    hi: float = 0.0


@dataclass
class Params:
    risk_per_trade: float
    daily_loss_limit: float
    max_drawdown: float
    atr_mult: float


def backtest(ind: pd.DataFrame, params: Params) -> Dict[str, float]:
    # Prepare date index from SPY (must exist)
    spy = ind[ind["ticker"] == "SPY"].sort_values("date")
    if spy.empty:
        raise RuntimeError("SPY not found in indicators")
    dates = spy["date"].unique()

    cash = DEFAULT_PORTFOLIO_EQUITY
    positions: Dict[str, Position] = {}
    equity_curve: List[float] = []
    peak = DEFAULT_PORTFOLIO_EQUITY
    paused = False

    # helper map for faster row access
    ind_key = {(row.ticker, row.date): row for row in ind.itertuples(index=False)}

    def equity(date: pd.Timestamp) -> float:
        total = cash
        for t, p in positions.items():
            row = ind_key.get((t, date))
            px = float(row.close) if row is not None else p.entry_px
            total += px * p.qty
        return float(total)

    def regime_label(date: pd.Timestamp) -> str:
        r = ind_key.get(("SPY", date))
        if r is None:
            return "unknown"
        return "risk-on" if float(r.close) > float(r.sma200) else "risk-off"

    def candidates_for(date: pd.Timestamp) -> List[str]:
        # rank by risk-adjusted momentum
        rows = [r for (t, d), r in ind_key.items() if d == date]
        if not rows:
            return []
        df = pd.DataFrame([{
            "ticker": r.ticker,
            "close": float(r.close),
            "sma50": float(r.sma50),
            "sma200": float(r.sma200),
            "ret20": float(r.ret20),
            "vol20": float(r.vol20),
            "rsi14": float(r.rsi14) if not pd.isna(r.rsi14) else np.nan,
            "adx14": float(r.adx14) if not pd.isna(r.adx14) else np.nan,
            "dist_sma200": float(r.dist_sma200) if not pd.isna(r.dist_sma200) else np.nan,
            "atr14": float(r.atr14) if not pd.isna(r.atr14) else np.nan,
        } for r in rows])

        # filters
        df = df[(df["close"] > df["sma50"]) & (df["sma50"] > df["sma200"])]
        df = df[(df["dist_sma200"].isna()) | (df["dist_sma200"] <= MAX_DIST_SMA200)]
        df = df[(df["rsi14"].isna()) | ((df["rsi14"] >= RSI_MIN) & (df["rsi14"] <= RSI_MAX))]
        df = df[(df["adx14"].isna()) | (df["adx14"] >= ADX_MIN)]
        df = df.replace([np.inf, -np.inf], np.nan).dropna(subset=["ret20", "vol20"])
        df["score"] = df["ret20"] / df["vol20"].replace(0, np.nan)
        df = df.dropna(subset=["score"]).sort_values("score", ascending=False)
        return df["ticker"].tolist()

    # main loop
    for i, d in enumerate(dates):
        date = pd.Timestamp(d)

        # mark-to-market equity
        eq = equity(date)
        equity_curve.append(eq)
        peak = max(peak, eq)
        dd = eq / peak - 1.0

        # daily return (vs prior day)
        daily_ret = None
        if i > 0:
            daily_ret = eq / equity_curve[i - 1] - 1.0

        # risk brakes
        if dd <= -abs(params.max_drawdown):
            paused = True
        if daily_ret is not None and daily_ret <= -abs(params.daily_loss_limit):
            paused = True

        reg = regime_label(date)
        entry_mult = 1.0 if reg == "risk-on" else RISK_OFF_ENTRY_MULT
        max_pos = MAX_POSITIONS if reg == "risk-on" else max(1, int(round(MAX_POSITIONS * RISK_OFF_MAX_POSITIONS_MULT)))

        # update highs
        for t, p in positions.items():
            row = ind_key.get((t, date))
            if row is None:
                continue
            px = float(row.close)
            p.hi = max(p.hi, px)

        # exits
        exits: List[str] = []
        for t, p in list(positions.items()):
            row = ind_key.get((t, date))
            if row is None:
                continue
            px = float(row.close)
            atr = float(row.atr14) if not pd.isna(row.atr14) else None
            if atr is None or atr <= 0:
                continue

            hard_stop = p.entry_px - params.atr_mult * atr
            if px <= hard_stop:
                exits.append(t)
                continue

            # trailing stop activates after +1 ATR progress
            if p.hi >= p.entry_px + 1.0 * atr:
                trail = p.hi - params.atr_mult * atr
                if px <= trail:
                    exits.append(t)
                    continue

            # time stop (eligible only)
            if date >= p.eligible_date:
                held_days = np.busday_count(p.entry_date.date(), date.date())
                if held_days >= TIME_STOP_DAYS:
                    if px < p.entry_px + TIME_STOP_PROGRESS_ATR * atr:
                        exits.append(t)
                        continue

        for t in exits:
            row = ind_key.get((t, date))
            px = float(row.close) if row is not None else positions[t].entry_px
            qty = positions[t].qty
            fill = px * (1 - SLIPPAGE_BPS / 10_000.0)
            notional = fill * qty
            fees = notional * (FEES_BPS / 10_000.0)
            cash += notional - fees
            positions.pop(t, None)

        # partial take-profit (eligible only)
        for t, p in list(positions.items()):
            if p.scaled_out:
                continue
            if date < p.eligible_date:
                continue
            row = ind_key.get((t, date))
            if row is None:
                continue
            px = float(row.close)
            atr = float(row.atr14) if not pd.isna(row.atr14) else None
            if atr is None or atr <= 0:
                continue
            if px >= p.entry_px + 2.0 * atr and p.qty >= 2:
                sell_qty = math.floor(p.qty / 2.0)
                if sell_qty >= 1:
                    fill = px * (1 - SLIPPAGE_BPS / 10_000.0)
                    notional = fill * sell_qty
                    fees = notional * (FEES_BPS / 10_000.0)
                    cash += notional - fees
                    p.qty -= sell_qty
                    p.scaled_out = True

        # entries (skip if paused)
        if paused:
            continue

        ranked = candidates_for(date)
        targets = ranked[:max_pos]

        # rotate out if eligible and not target or below sma50
        for t, p in list(positions.items()):
            if date < p.eligible_date:
                continue
            row = ind_key.get((t, date))
            if row is None:
                continue
            px = float(row.close)
            below = px < float(row.sma50)
            if (t not in targets) or below:
                fill = px * (1 - SLIPPAGE_BPS / 10_000.0)
                notional = fill * p.qty
                fees = notional * (FEES_BPS / 10_000.0)
                cash += notional - fees
                positions.pop(t, None)

        # fill open slots
        slots = max_pos - len(positions)
        if slots <= 0:
            continue

        eq_now = equity(date)
        max_notional = 0.10 * eq_now

        for t in targets:
            if slots <= 0:
                break
            if t in positions:
                continue
            row = ind_key.get((t, date))
            if row is None:
                continue
            px = float(row.close)
            atr = float(row.atr14) if not pd.isna(row.atr14) else None
            if atr is None or atr <= 0:
                continue

            stop = px - params.atr_mult * atr
            risk_per_share = max(0.01, px - stop)

            risk_budget = (params.risk_per_trade * entry_mult) * eq_now
            shares_risk = math.floor(risk_budget / risk_per_share)

            cost_per_share = px * (1 + FEES_BPS / 10_000.0) * (1 + SLIPPAGE_BPS / 10_000.0)
            shares_cash = math.floor(cash / cost_per_share)
            shares_cap = math.floor(max_notional / cost_per_share)
            shares = int(max(0, min(shares_risk, shares_cash, shares_cap)))
            if shares <= 0:
                continue

            fill = px * (1 + SLIPPAGE_BPS / 10_000.0)
            notional = fill * shares
            fees = notional * (FEES_BPS / 10_000.0)
            total = notional + fees
            if total > cash:
                continue

            cash -= total
            entry_date = date
            eligible = entry_date + pd.tseries.offsets.BDay(MIN_HOLD_DAYS)
            positions[t] = Position(qty=float(shares), entry_px=float(fill), entry_date=entry_date, eligible_date=pd.Timestamp(eligible.date()), scaled_out=False, hi=float(fill))
            slots -= 1

    # results
    eqs = np.array(equity_curve, dtype=float)
    if len(eqs) < 5:
        raise RuntimeError("not enough history")

    total_ret = eqs[-1] / eqs[0] - 1.0
    dd_series = eqs / np.maximum.accumulate(eqs) - 1.0
    max_dd = float(dd_series.min())

    # annualized approx
    years = len(eqs) / 252.0
    cagr = float((eqs[-1] / eqs[0]) ** (1.0 / max(1e-9, years)) - 1.0)

    daily_rets = eqs[1:] / eqs[:-1] - 1.0
    vol = float(np.std(daily_rets) * math.sqrt(252.0)) if len(daily_rets) > 10 else 0.0
    sharpe = float((np.mean(daily_rets) * 252.0) / (np.std(daily_rets) * math.sqrt(252.0))) if np.std(daily_rets) > 0 else 0.0

    worst_week = float(pd.Series(daily_rets).rolling(5).sum().min()) if len(daily_rets) >= 5 else float(np.min(daily_rets))

    return {
        "total_return": float(total_ret),
        "cagr": float(cagr),
        "max_drawdown": float(max_dd),
        "vol": float(vol),
        "sharpe": float(sharpe),
        "worst_5d": float(worst_week),
    }


def parse_args() -> argparse.Namespace:
    p = argparse.ArgumentParser()
    p.add_argument("--years", type=int, default=2)
    p.add_argument("--end", default="", help="YYYY-MM-DD (default: latest in Supabase)")
    p.add_argument("--out-md", default=str(REPO / "docs" / "SWING_RISK_GRID.md"))
    return p.parse_args()


def main() -> None:
    load_env()
    args = parse_args()

    uni = load_universe()

    # Determine end date: use today (UTC) unless explicit.
    if args.end:
        end = dt.date.fromisoformat(args.end)
    else:
        end = dt.datetime.now(dt.timezone.utc).date()

    start = end - dt.timedelta(days=int(args.years * 365.25 + 30))

    print(f"[backtest] fetching prices {start}..{end} for {len(uni)} tickers")
    px = fetch_prices(uni, start, end)
    if px.empty:
        raise RuntimeError("No prices fetched")

    ind = compute_indicators_all(px)

    # Grid (balanced-focused)
    risk_per_trade = [0.01, 0.015, 0.02, 0.025]
    daily_loss = [0.025, 0.035, 0.05]
    max_dd = [0.08, 0.10, 0.12, 0.15]
    atr_mult = [1.8, 2.0, 2.5]

    rows = []
    combos = list(itertools.product(risk_per_trade, daily_loss, max_dd, atr_mult))
    print(f"[backtest] running grid: {len(combos)} combos")

    for r, dl, mdd, am in combos:
        p = Params(risk_per_trade=r, daily_loss_limit=dl, max_drawdown=mdd, atr_mult=am)
        try:
            res = backtest(ind, p)
            rows.append({
                "risk_per_trade": r,
                "daily_loss_limit": dl,
                "max_drawdown_brake": mdd,
                "atr_mult": am,
                **res,
            })
        except Exception as exc:
            rows.append({
                "risk_per_trade": r,
                "daily_loss_limit": dl,
                "max_drawdown_brake": mdd,
                "atr_mult": am,
                "error": str(exc)[:160],
            })

    df = pd.DataFrame(rows)

    out_dir = REPO / "output" / "backtests"
    out_dir.mkdir(parents=True, exist_ok=True)
    stamp = dt.datetime.now(dt.timezone.utc).strftime("%Y%m%d%H%M%S")
    csv_path = out_dir / f"swing_risk_grid_{stamp}.csv"
    df.to_csv(csv_path, index=False)

    # Score: balanced = prioritize max_dd then cagr
    ok = df[df.get("error").isna()] if "error" in df.columns else df
    ok = ok.copy()
    for c in ["cagr", "max_drawdown", "worst_5d", "sharpe"]:
        if c in ok.columns:
            ok[c] = pd.to_numeric(ok[c], errors="coerce")
    ok = ok.dropna(subset=["cagr", "max_drawdown"]) if ("cagr" in ok.columns and "max_drawdown" in ok.columns) else ok

    best = pd.DataFrame()
    if not ok.empty and all(c in ok.columns for c in ["cagr", "max_drawdown", "worst_5d"]):
        ok["score"] = (ok["cagr"] * 1.0) + (ok["max_drawdown"] * 2.5) + (ok["worst_5d"] * 0.5)
        best = ok.sort_values("score", ascending=False).head(15)

    md_lines = []
    md_lines.append(f"# Swing risk grid backtest")
    md_lines.append("")
    md_lines.append(f"- Window: ~{args.years}y ending {end.isoformat()}")
    md_lines.append(f"- Universe: SP500 + proxies ({len(uni)} tickers)")
    md_lines.append(f"- Note: daily-bar approximation; relative comparison only")
    md_lines.append(f"- Results CSV: `{csv_path.relative_to(REPO)}`")
    md_lines.append("")

    md_lines.append("## Top parameter sets (balanced score)")
    md_lines.append("")
    if best.empty:
        md_lines.append("No successful runs.")
    else:
        md_lines.append("| risk/trade | daily loss | max DD brake | ATR mult | CAGR | Max DD | Worst 5d | Sharpe |")
        md_lines.append("|---:|---:|---:|---:|---:|---:|---:|---:|")
        for _, row in best.iterrows():
            md_lines.append(
                "| {r:.2%} | {dl:.2%} | {mdd:.0%} | {am:.1f} | {cagr:+.1%} | {mddv:+.1%} | {w:+.1%} | {sh:.2f} |".format(
                    r=float(row["risk_per_trade"]),
                    dl=float(row["daily_loss_limit"]),
                    mdd=float(row["max_drawdown_brake"]),
                    am=float(row["atr_mult"]),
                    cagr=float(row["cagr"]),
                    mddv=float(row["max_drawdown"]),
                    w=float(row.get("worst_5d") or 0.0),
                    sh=float(row.get("sharpe") or 0.0),
                )
            )

    out_md = Path(args.out_md)
    out_md.write_text("\n".join(md_lines) + "\n", encoding="utf-8")

    print(f"[ok] wrote {out_md}")


if __name__ == "__main__":
    main()
