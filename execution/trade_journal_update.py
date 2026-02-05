"""Append a daily trade journal entry from paper trading tables (deterministic).

Reads paper_orders + paper_fills (+ optional paper_equity_curve) for a given date
and appends a compact markdown section to docs/TRADE_JOURNAL.md.

This is designed for continuity: you can review later and reconstruct what
happened without digging through raw tables.

Usage:
  python execution/trade_journal_update.py --date 2026-02-05 --portfolio-id default

Notes:
- We intentionally keep this non-LLM and best-effort.
- Duplicate prevention: if the date+portfolio header already exists, we skip.
"""

from __future__ import annotations

import argparse
import datetime as dt
import os
from pathlib import Path
from typing import Any, Dict, List, Optional

import requests
from dotenv import load_dotenv

REPO_ROOT = Path(__file__).resolve().parents[1]
JOURNAL_PATH = REPO_ROOT / "docs" / "TRADE_JOURNAL.md"


def load_env() -> None:
    env_path = REPO_ROOT / ".env"
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


def parse_args() -> argparse.Namespace:
    today = dt.date.today().isoformat()
    p = argparse.ArgumentParser(description="Append trade journal entry")
    p.add_argument("--date", default=today, help="YYYY-MM-DD")
    p.add_argument("--portfolio-id", default="default")
    p.add_argument("--dry-run", action="store_true")
    return p.parse_args()


def fetch_orders(date: str) -> List[dict]:
    base = supabase_base()
    url = f"{base}/rest/v1/paper_orders"
    params = [
        ("select", "order_id,date,ticker,side,target_weight,qty_estimate,status"),
        ("date", f"eq.{date}"),
        ("order", "ticker.asc"),
    ]
    r = requests.get(url, headers=supabase_headers(), params=params, timeout=20)
    if r.status_code >= 300:
        raise RuntimeError(f"paper_orders fetch failed: {r.status_code} {r.text}")
    return r.json() or []


def fetch_fills(order_ids: List[str]) -> List[dict]:
    if not order_ids:
        return []
    base = supabase_base()
    url = f"{base}/rest/v1/paper_fills"
    in_list = ",".join(order_ids)
    params = [
        ("select", "fill_id,order_id,fill_price,fill_method,slippage_bps,fees,filled_at"),
        ("order_id", f"in.({in_list})"),
        ("order", "filled_at.asc"),
    ]
    r = requests.get(url, headers=supabase_headers(), params=params, timeout=20)
    if r.status_code >= 300:
        raise RuntimeError(f"paper_fills fetch failed: {r.status_code} {r.text}")
    return r.json() or []


def fetch_equity(date: str, portfolio_id: str) -> Optional[dict]:
    base = supabase_base()
    url = f"{base}/rest/v1/paper_equity_curve"
    params = [
        ("select", "date,portfolio_id,equity,cash,drawdown,turnover"),
        ("date", f"eq.{date}"),
        ("portfolio_id", f"eq.{portfolio_id}"),
        ("limit", "1"),
    ]
    r = requests.get(url, headers=supabase_headers(), params=params, timeout=20)
    if r.status_code >= 300:
        return None
    rows = r.json() or []
    return rows[0] if rows else None


def fmt_money(x: Any) -> str:
    try:
        v = float(x)
    except Exception:
        return ""
    return f"${v:,.2f}"


def fmt_pct(x: Any) -> str:
    try:
        v = float(x)
    except Exception:
        return ""
    return f"{v:.2f}%"


def append_entry(date: str, portfolio_id: str, equity_row: Optional[dict], orders: List[dict], fills: List[dict], dry_run: bool) -> None:
    JOURNAL_PATH.parent.mkdir(parents=True, exist_ok=True)
    if not JOURNAL_PATH.exists():
        JOURNAL_PATH.write_text("# SignalSmith — Trade Journal (append-only)\n\n---\n", encoding="utf-8")

    header = f"## {date} — portfolio={portfolio_id}"
    existing = JOURNAL_PATH.read_text(encoding="utf-8")
    if header in existing:
        print(f"[skip] journal already has entry for {date} portfolio={portfolio_id}")
        return

    lines: List[str] = []
    lines.append("\n" + header)

    if equity_row:
        lines.append(
            f"- Equity: {fmt_money(equity_row.get('equity'))} | Cash: {fmt_money(equity_row.get('cash'))} | "
            f"Drawdown: {fmt_pct((equity_row.get('drawdown') or 0) * 100)} | Turnover: {fmt_pct((equity_row.get('turnover') or 0) * 100)}"
        )

    lines.append(f"- Orders: {len(orders)} | Fills: {len(fills)}")

    if orders:
        lines.append("\n### Orders")
        for o in orders:
            tw = o.get("target_weight")
            tw_s = f"{float(tw)*100:.2f}%" if tw is not None else ""
            qe = o.get("qty_estimate")
            qe_s = f"~{float(qe):.2f}" if qe is not None else ""
            lines.append(f"- {o.get('ticker')} {o.get('side')} {qe_s} @ target {tw_s} ({o.get('status')})")

    if fills:
        lines.append("\n### Fills")
        # map order_id -> order
        omap = {o.get("order_id"): o for o in orders}
        for f in fills:
            o = omap.get(f.get("order_id")) or {}
            lines.append(
                "- {ticker} {side} fill={fill} | slip={slip}bps | fees={fees} | method={meth}".format(
                    ticker=o.get("ticker") or "?",
                    side=o.get("side") or "?",
                    fill=(f"{float(f.get('fill_price')):.4f}" if f.get("fill_price") is not None else ""),
                    slip=(f"{float(f.get('slippage_bps')):.1f}" if f.get("slippage_bps") is not None else ""),
                    fees=(fmt_money(f.get("fees")) or ""),
                    meth=f.get("fill_method") or "",
                )
            )

    blob = "\n".join(lines) + "\n"
    if dry_run:
        print(blob)
        return

    with JOURNAL_PATH.open("a", encoding="utf-8") as fp:
        fp.write(blob)

    print(f"[ok] appended journal entry for {date} portfolio={portfolio_id}")


def main() -> None:
    load_env()
    args = parse_args()

    orders = fetch_orders(args.date)
    fills = fetch_fills([o["order_id"] for o in orders if o.get("order_id")])
    equity_row = fetch_equity(args.date, args.portfolio_id)

    # Quiet mode: if nothing happened and we have no equity row, do nothing.
    if not orders and not fills and not equity_row:
        print("HEARTBEAT_OK")
        return

    append_entry(args.date, args.portfolio_id, equity_row, orders, fills, args.dry_run)


if __name__ == "__main__":
    main()
