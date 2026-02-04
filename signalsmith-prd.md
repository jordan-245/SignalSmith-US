---
title: SignalSmith US - PRD (Free Data Stack)
project: SignalSmith-US
type: prd
status: living
version: 0.4
owner: Jordan
updated: 2026-02-04
tags: [signalsmith, prd, trading-bot, ml, market-data, supabase, openclaw, hostinger, telegram, rss, yfinance]
---

# SignalSmith US
**Product Requirements Document (PRD)**
_Free data stack: yfinance + RSS + HTML scraping (readability)._

## 1) Vision
SignalSmith US is an always-on, long-only US equity system that:
- Produces a **daily Top 10** list designed to outperform **SPY** over a **short horizon**.
- Enforces a **minimum hold period of 5 trading days**.
- Executes **paper trading** deterministically (VWAP-based fills), logs everything, and alerts via Telegram.

In parallel, it runs an autonomous **Swing Book** (days–weeks) that:
- Forms market/regime hypotheses,
- Scans a universe of equities + commodity proxies,
- Executes paper trades when technical conditions are satisfied,
- Notifies the operator with rationale and risk.

**Paper-only by default.** Live trading remains out of scope until explicit approval gates + broker integration are implemented.

## 2) Core constraints (current)
- Market: **US**
- Direction: **Long-only**
- Benchmark: **SPY**
- Paper portfolio size: **$5,000 USD** (per book)
- Model book: **Top N = 10**
- Min hold: **5 trading days**
- Operator timezone: **Australia/Brisbane**
- Market timing: **America/New_York** (DST-aware)

## 3) Data sources (free-first)
### 3.1 Prices
- **Primary:** `yfinance`
  - Daily OHLCV for universe (stored to Supabase).
  - Intraday **1h** bars used for paper execution fills.

### 3.2 Market calendar / market open
- **exchange-calendars** (`XNYS`) for session open/closed.
  - Pre-open pipelines skip automatically on market-closed days.

### 3.3 News ingestion
- RSS/Atom discovery + HTML fetch + text extraction.
- Extraction uses **readability-lxml** with BeautifulSoup fallback.
- Sources are allowlisted in `directives/rss_sources.txt`.

**Notes / tradeoffs:**
- Some publishers block scraping (401/403). Those feeds are disabled or treated as headline-only.
- Intraday history is limited (often ~60 days for 1h). For older backtests, the system falls back to daily proxies and records the fallback in logs.

## 4) System architecture
Three layers:
1) **Directives** (`directives/`): SOPs per pipeline segment.
2) **Orchestration** (OpenClaw): scheduling, monitoring, notifications, approvals.
3) **Execution** (`execution/`): deterministic Python scripts.

OpenClaw runs on a Hostinger VPS:
- systemd user service enabled on boot (linger enabled)
- Telegram channel for alerts + approvals
- Self-update timer (safe FF-only pull when repo clean)

## 5) Books
### 5.1 Model Book (Top 10)
- Pre-open pipeline:
  - ingest prices
  - build features
  - train/score baseline model
  - generate Top 10
  - paper trade

### 5.2 Swing Book (autonomous trader)
- Portfolio id: `swing` (separate from model book)
- Universe: S&P 500 + commodity proxies/miners/sector ETFs (starter list in `execution/swing_book.py`).
- Entry (v0): trend + momentum + risk filters.
- Exit (v0): eligible-to-sell and (no longer a target) OR break below SMA50.
- Execution: first-hour VWAP from yfinance 1h (fallback to daily close proxy).

## 6) Paper execution model
- **First-hour VWAP** fill model from yfinance 1h bars (preferred).
- If missing, fallback to daily OHLC average proxy.
- Fees + slippage modeled via bps.

## 7) Scheduling (OpenClaw cron)
All schedules are anchored in `America/New_York` for DST correctness unless noted.

Core:
- **Model pre-open run:** 08:45 ET, Mon–Fri
- **Model post-close report:** 16:30 ET, Mon–Fri
- **Approval timeout sweep:** every 5 minutes (UTC)

Swing:
- **Swing scan (pre-open):** 08:30 ET, Mon–Fri
- **Swing scan (post-close):** 16:45 ET, Mon–Fri

News:
- **RSS ingest:** hourly
- **RSS feed health:** daily
- **RSS source discovery:** weekly (proposes changes; does not auto-apply)

Ops:
- **Daily self-update:** 06:00 Brisbane time (implemented as UTC 20:00) — safe FF-only pull; skips if repo dirty; restarts gateway on update.

## 8) Supabase data model (current + target)
Current repo uses:
- `prices_daily`, `benchmark_prices_daily`
- `features_daily`, `labels`
- `model_runs`, `predictions`
- `paper_portfolio`, `paper_orders`, `paper_fills`, `paper_positions`, `paper_equity_curve`
- `pipeline_runs`
- `docs_raw`, `docs_text`, `docs_extracted`

Governance / ops:
- `approval_requests`, `approval_actions` (schema in `schema/approvals.sql`)

Target (later clean-up): unify naming to a PRD-aligned schema (`run_log`, `signals`, etc.) once MVP is stable.

## 9) Controls & safety
- Paper trading is fully automated.
- Any future live trading must be gated by Telegram approvals and fully audited.
- Reliability first: fail loudly with actionable logs; prefer idempotent runs.

## 10) Near-term roadmap
1) Stabilize free data spine (universe refresh, ticker normalization, data-quality alerts).
2) Improve signal quality (features, regime detection, swing ruleset iterations).
3) Add lightweight evaluation + backtest harness for both books.
4) Only then consider paid data feeds or broker integration.
