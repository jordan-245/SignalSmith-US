"""Signal Foundry — Telegram Summary Formatter.

Formats a concise Telegram-ready summary from a Signal Foundry report.
Includes top 5 picks with probabilities and trade plans.

Usage (standalone):
  python -m execution.foundry.foundry_telegram --market US --date 2026-02-07

Usage (import):
  from execution.foundry.foundry_telegram import format_telegram_summary, send_foundry_summary
  msg = format_telegram_summary(market="US", as_of_str="2026-02-07")
  send_foundry_summary(market="US", as_of_str="2026-02-07")

Uses the telegram_fmt.py patterns from execution/telegram_fmt.py for sending.
"""

from __future__ import annotations

import argparse
import datetime as dt
import html
import os
import sys
from pathlib import Path
from typing import Any, Dict, List, Optional, Tuple

REPO = Path(__file__).resolve().parents[2]
sys.path.insert(0, str(REPO / "execution"))

from foundry.foundry_report import (
    DEFAULT_PORTFOLIO,
    DEFAULT_RISK_PER_TRADE_PCT,
    _compute_atr,
    _detect_regime,
    _generate_trade_plans,
    _load_catalyst_data,
    load_predictions,
    load_prices,
    load_universe,
)

try:
    from telegram_fmt import send_telegram, get_default_chat_id
except ImportError:
    send_telegram = None  # type: ignore
    get_default_chat_id = None  # type: ignore

TOP_TELEGRAM = 5


def _esc(text: str) -> str:
    """Escape HTML entities for Telegram HTML parse mode."""
    return html.escape(str(text))


def format_telegram_summary(
    market: str = "US",
    as_of_str: Optional[str] = None,
    run_id: Optional[str] = None,
    top_n: int = TOP_TELEGRAM,
    portfolio: float = DEFAULT_PORTFOLIO,
    risk_pct: float = DEFAULT_RISK_PER_TRADE_PCT,
) -> str:
    """Generate a concise Telegram message from foundry data.

    Returns HTML-formatted string ready for Telegram's HTML parse mode.
    """
    as_of = dt.date.fromisoformat(as_of_str) if as_of_str else dt.date.today()

    preds = load_predictions(market, as_of, run_id)
    prices = load_prices(market, as_of, run_id)
    universe = load_universe(market)

    if preds.empty:
        return (
            f"<b>Signal Foundry — {_esc(market)} — {as_of.isoformat()}</b>\n\n"
            "⚠️ No predictions available for this date."
        )

    # Sort by ensemble
    if "p_up_ens" in preds.columns:
        preds = preds.sort_values("p_up_ens", ascending=False)

    top = preds.head(top_n)
    top_tickers = top["ticker"].tolist()

    # Regime
    regime = _detect_regime(prices, market)

    # Trade plans
    trade_plans = _generate_trade_plans(top, prices, portfolio, risk_pct)
    plan_map = {tp["ticker"]: tp for tp in trade_plans}

    # Build message
    lines: List[str] = []

    # Header
    lines.append(f"<b>📊 Signal Foundry — {_esc(market)}</b>")
    lines.append(f"📅 {as_of.isoformat()}")
    lines.append(f"🌡️ {_esc(regime.get('current', 'Unknown'))}")
    lines.append("")

    # Top picks
    lines.append(f"<b>🏆 Top {top_n} Picks</b>")
    lines.append("")

    for rank, (_, row) in enumerate(top.iterrows(), 1):
        ticker = str(row["ticker"])
        px = float(row.get("px", 0))
        p1d = float(row.get("p_up_1d", 0)) * 100
        p5d = float(row.get("p_up_5d", 0)) * 100
        p20d = float(row.get("p_up_20d", 0)) * 100
        p_ens = float(row.get("p_up_ens", 0)) * 100

        # Conviction emoji
        if p_ens > 60:
            conv = "🟢"
        elif p_ens > 52:
            conv = "🟡"
        else:
            conv = "⚪"

        lines.append(f"{conv} <b>{rank}. {_esc(ticker)}</b> — ${px:.2f}")
        lines.append(f"   P(↑): 1D {p1d:.0f}% | 5D {p5d:.0f}% | 20D {p20d:.0f}%")

        plan = plan_map.get(ticker)
        if plan:
            lines.append(
                f"   📋 Entry ${plan['entry']:.2f} → Stop ${plan['stop']:.2f} → Target ${plan['target']:.2f}"
            )
            lines.append(
                f"   📦 {plan['shares']} shares (${plan['position_value']:,.0f} | {plan['pct_of_portfolio']:.0f}% port)"
            )
        lines.append("")

    # Footer
    predicted = preds["ticker"].nunique()
    lines.append(f"📊 Universe: {predicted}/{len(universe)} tickers predicted")
    lines.append(f"💼 Portfolio: ${portfolio:,.0f} | Risk/trade: {risk_pct}%")
    lines.append("")
    lines.append(f"<i>Generated {dt.datetime.now(dt.timezone.utc).strftime('%H:%M UTC')}</i>")

    return "\n".join(lines)


def send_foundry_summary(
    market: str = "US",
    as_of_str: Optional[str] = None,
    run_id: Optional[str] = None,
    top_n: int = TOP_TELEGRAM,
    portfolio: float = DEFAULT_PORTFOLIO,
    risk_pct: float = DEFAULT_RISK_PER_TRADE_PCT,
    chat_id: Optional[str] = None,
) -> str:
    """Generate and send the Telegram summary. Returns the message text."""
    msg = format_telegram_summary(
        market=market,
        as_of_str=as_of_str,
        run_id=run_id,
        top_n=top_n,
        portfolio=portfolio,
        risk_pct=risk_pct,
    )

    if send_telegram is not None:
        send_telegram(msg, chat_id=chat_id, warn_if_missing=True)
        print(f"[foundry_telegram] Sent {market} summary to Telegram")
    else:
        print("[foundry_telegram] telegram_fmt not available; message not sent")
        print(msg)

    return msg


def main() -> None:
    parser = argparse.ArgumentParser(description="Signal Foundry Telegram Summary")
    parser.add_argument("--market", choices=["US", "ASX"], default="US")
    parser.add_argument("--date", default=None, help="YYYY-MM-DD")
    parser.add_argument("--run-id", default=None)
    parser.add_argument("--top-n", type=int, default=TOP_TELEGRAM)
    parser.add_argument("--portfolio", type=float, default=DEFAULT_PORTFOLIO)
    parser.add_argument("--risk-pct", type=float, default=DEFAULT_RISK_PER_TRADE_PCT)
    parser.add_argument("--send", action="store_true", help="Actually send via Telegram")
    parser.add_argument("--chat-id", default=None)
    args = parser.parse_args()

    if args.send:
        msg = send_foundry_summary(
            market=args.market,
            as_of_str=args.date,
            run_id=args.run_id,
            top_n=args.top_n,
            portfolio=args.portfolio,
            risk_pct=args.risk_pct,
            chat_id=args.chat_id,
        )
    else:
        msg = format_telegram_summary(
            market=args.market,
            as_of_str=args.date,
            run_id=args.run_id,
            top_n=args.top_n,
            portfolio=args.portfolio,
            risk_pct=args.risk_pct,
        )
        print(msg)


if __name__ == "__main__":
    main()
