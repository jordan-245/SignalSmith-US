"""SignalSmith local dashboard (read-only).

Run (on VPS):
  cd /srv/signalsmith/SignalSmith-US
  source .venv/bin/activate
  streamlit run ui/dashboard.py --server.address 127.0.0.1 --server.port 8501

Access (from laptop):
  ssh -L 8501:127.0.0.1:8501 root@<VPS_IP>
  open http://localhost:8501

Security:
- Binds to 127.0.0.1 only.
- Uses Supabase service role from .env / system env.

"""

from __future__ import annotations

import datetime as dt
import os
from pathlib import Path
from typing import Any, Dict, List, Optional, Tuple

import pandas as pd
import plotly.express as px
import plotly.graph_objects as go
import requests
import streamlit as st
from dotenv import load_dotenv

REPO = Path(__file__).resolve().parents[1]


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


def sb_get(table: str, params: List[Tuple[str, str]], timeout: int = 20) -> List[Dict[str, Any]]:
    url = f"{sb_base()}/rest/v1/{table}"
    r = requests.get(url, headers=sb_headers(), params=params, timeout=timeout)
    r.raise_for_status()
    return r.json() or []


@st.cache_data(ttl=30)
@st.cache_data(ttl=30)
def latest_equity(portfolio_id: str) -> Optional[Dict[str, Any]]:
    rows = sb_get(
        "paper_equity_curve",
        [
            ("select", "date,equity,cash"),
            ("portfolio_id", f"eq.{portfolio_id}"),
            ("order", "date.desc"),
            ("limit", "1"),
        ],
    )
    return rows[0] if rows else None


@st.cache_data(ttl=60)
def equity_curve(portfolio_id: str, days: int) -> pd.DataFrame:
    start = (dt.date.today() - dt.timedelta(days=days)).isoformat()
    rows = sb_get(
        "paper_equity_curve",
        [
            ("select", "date,equity,cash"),
            ("portfolio_id", f"eq.{portfolio_id}"),
            ("date", f"gte.{start}"),
            ("order", "date.asc"),
        ],
    )
    if not rows:
        return pd.DataFrame(columns=["date", "equity", "cash"])
    df = pd.DataFrame(rows)
    df["date"] = pd.to_datetime(df["date"])
    df["equity"] = pd.to_numeric(df["equity"], errors="coerce")
    df["cash"] = pd.to_numeric(df["cash"], errors="coerce")
    return df


@st.cache_data(ttl=30)
def latest_positions(portfolio_id: str) -> pd.DataFrame:
    # Find last date
    rows = sb_get(
        "paper_positions",
        [
            ("select", "date"),
            ("portfolio_id", f"eq.{portfolio_id}"),
            ("order", "date.desc"),
            ("limit", "1"),
        ],
    )
    if not rows:
        return pd.DataFrame()
    last_date = rows[0]["date"]

    pos = sb_get(
        "paper_positions",
        [
            ("select", "date,ticker,qty,avg_cost,market_value,entry_date,eligible_sell_date"),
            ("portfolio_id", f"eq.{portfolio_id}"),
            ("date", f"eq.{last_date}"),
            ("order", "market_value.desc"),
        ],
    )
    df = pd.DataFrame(pos)
    if df.empty:
        return df
    for c in ["qty", "avg_cost", "market_value"]:
        df[c] = pd.to_numeric(df[c], errors="coerce")
    return df


@st.cache_data(ttl=30)
def recent_orders(portfolio_id: str, limit: int = 200) -> pd.DataFrame:
    rows = sb_get(
        "paper_orders",
        [
            ("select", "order_id,date,ticker,side,qty_estimate,status"),
            ("order", "date.desc"),
            ("limit", str(limit)),
        ],
    )
    df = pd.DataFrame(rows)
    if df.empty:
        return df
    df["date"] = pd.to_datetime(df["date"], errors="coerce")
    if portfolio_id:
        # table doesn’t store portfolio_id; filter by our convention in order_id prefix where possible
        # (keeps UI useful without schema changes).
        if portfolio_id == "swing":
            df = df[df["order_id"].str.contains("-BUY-| -SELL-|CATALYST", regex=True) | (df["order_id"].str.contains("SWING", case=False, na=False))]
    return df


@st.cache_data(ttl=30)
def recent_fills(limit: int = 200) -> pd.DataFrame:
    rows = sb_get(
        "paper_fills",
        [
            ("select", "fill_id,order_id,fill_price,fees,filled_at,fill_method"),
            ("order", "filled_at.desc"),
            ("limit", str(limit)),
        ],
    )
    df = pd.DataFrame(rows)
    if df.empty:
        return df
    df["filled_at"] = pd.to_datetime(df["filled_at"], errors="coerce")
    return df


@st.cache_data(ttl=60)
def pipeline_runs(limit: int = 80) -> pd.DataFrame:
    table = os.getenv("SUPABASE_PIPELINE_TABLE", "pipeline_runs")
    rows = sb_get(
        table,
        [
            ("select", "run_id,tag,stage,status,date,started_at,ended_at"),
            ("order", "started_at.desc"),
            ("limit", str(limit)),
        ],
    )
    df = pd.DataFrame(rows)
    if df.empty:
        return df
    for c in ["started_at", "ended_at", "date"]:
        df[c] = pd.to_datetime(df[c], errors="coerce")
    return df


def read_todos() -> str:
    p = REPO / "directives" / "todos.md"
    if not p.exists():
        return "(no directives/todos.md yet)"
    return p.read_text(encoding="utf-8")


def main() -> None:
    load_env()

    st.set_page_config(page_title="SignalSmith Dashboard", layout="wide")
    st.title("SignalSmith — Swing Dashboard")
    st.caption("Swing book only. Data refreshes automatically.")

    # We only support the swing portfolio going forward.
    portfolio_id = "swing"

    with st.sidebar:
        st.header("Controls")
        days = st.selectbox("Equity window", options=[30, 90, 180, 365, 730], index=1)
        st.caption("All panels are Swing book only.")

    tab1, tab2, tab3, tab4, tab5 = st.tabs(["Overview", "Equity curve", "Positions", "Orders & Fills", "Runs & Todos"])

    with tab1:
        eq = latest_equity(portfolio_id)
        if eq:
            st.metric("Equity", f"${float(eq['equity']):,.2f}")
            st.metric("Cash", f"${float(eq['cash']):,.2f}")
            st.caption(f"As of {eq['date']}")
        else:
            st.info("No equity data yet for this portfolio.")

        df_pos = latest_positions(portfolio_id)
        if not df_pos.empty:
            st.subheader("Current positions")
            st.dataframe(df_pos, use_container_width=True, hide_index=True)
        else:
            st.info("No positions yet.")

    with tab2:
        df = equity_curve(portfolio_id, days=days)
        if df.empty:
            st.info("No equity curve yet.")
        else:
            df = df.sort_values("date")
            # Key stats
            start_eq = float(df["equity"].iloc[0])
            end_eq = float(df["equity"].iloc[-1])
            pnl = end_eq - start_eq
            pnl_pct = (pnl / start_eq) if start_eq else 0.0

            # Drawdown
            peak = df["equity"].cummax()
            dd = (df["equity"] / peak) - 1.0
            max_dd = float(dd.min())

            c1, c2, c3, c4 = st.columns(4)
            c1.metric("Start equity", f"${start_eq:,.0f}")
            c2.metric("Current equity", f"${end_eq:,.0f}", f"{pnl:+,.0f} ({pnl_pct:+.2%})")
            c3.metric("Max drawdown", f"{max_dd:.2%}")
            # crude daily vol
            ret = df["equity"].pct_change().dropna()
            vol = float(ret.std()) if len(ret) else 0.0
            c4.metric("Daily vol (std)", f"{vol:.2%}")

            fig = go.Figure()
            fig.add_trace(go.Scatter(x=df["date"], y=df["equity"], mode="lines", name="Equity"))
            fig.add_trace(go.Scatter(x=df["date"], y=peak, mode="lines", name="Peak", line=dict(dash="dot")))
            fig.update_layout(
                title=f"Equity curve — {portfolio_id}",
                margin=dict(l=10, r=10, t=50, b=10),
                height=420,
                hovermode="x unified",
            )
            st.plotly_chart(fig, use_container_width=True)

            dd_fig = go.Figure()
            dd_fig.add_trace(go.Scatter(x=df["date"], y=dd, mode="lines", name="Drawdown"))
            dd_fig.update_layout(
                title="Drawdown",
                margin=dict(l=10, r=10, t=50, b=10),
                height=240,
                hovermode="x unified",
                yaxis_tickformat=".0%",
            )
            st.plotly_chart(dd_fig, use_container_width=True)

            with st.expander("Equity table (last 50)"):
                df2 = df.copy()
                df2["ret"] = df2["equity"].pct_change()
                df2["drawdown"] = dd
                st.dataframe(df2.tail(50), use_container_width=True, hide_index=True)

    with tab3:
        df_pos = latest_positions(portfolio_id)
        if df_pos.empty:
            st.info("No positions yet.")
        else:
            st.subheader("Positions")
            st.dataframe(df_pos, use_container_width=True, hide_index=True)

    with tab4:
        c1, c2 = st.columns(2)
        with c1:
            st.subheader("Recent orders")
            st.dataframe(recent_orders(portfolio_id), use_container_width=True, hide_index=True)
        with c2:
            st.subheader("Recent fills")
            st.dataframe(recent_fills(), use_container_width=True, hide_index=True)

    with tab5:
        st.subheader("Pipeline runs")
        df_runs = pipeline_runs()
        if df_runs.empty:
            st.info("No pipeline runs found (or table not present).")
        else:
            st.dataframe(df_runs, use_container_width=True, hide_index=True)

        st.subheader("To-dos")
        st.markdown(read_todos())


if __name__ == "__main__":
    main()
