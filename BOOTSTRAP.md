# SignalSmith US - Project Bootstrap

**Project:** SignalSmith US  
**Type:** Autonomous Swing Trading System (Paper Only)  
**Owner:** Jordan  
**Timezone:** Australia/Brisbane  
**Market:** US Equities (America/New_York)  
**Status:** Production (Paper Trading)

---

## What Is This?

SignalSmith US is an **always-on, long-only US equity swing trading system** that:
- Scans a universe of equities + commodity proxies
- Generates buy/sell signals based on technical + momentum filters
- Executes **paper trades** automatically (first-hour VWAP model)
- Sends notifications and trade rationale via Telegram
- Maintains a $5,000 paper portfolio (Swing Book)

**Critical:** This is **PAPER ONLY** by default. No live trading without explicit approval gates and broker integration.

---

## Tech Stack

- **Orchestration:** OpenClaw (Telegram bot + cron scheduler)
- **Execution:** Python 3.12 scripts (deterministic)
- **Data:** Free stack (yfinance, RSS/HTML scraping, exchange-calendars)
- **Storage:** Supabase (PostgreSQL)
- **Hosting:** Hostinger VPS (systemd user service)
- **Notifications:** Telegram

---

## Architecture Summary

**3-Layer Design:**
1. **Directives** (`directives/`) - Natural language SOPs (what to do)
2. **Orchestration** (OpenClaw AI) - Intelligent routing (decision-making)
3. **Execution** (`execution/`) - Deterministic Python scripts (the actual work)

This separates probabilistic AI (orchestration) from deterministic logic (execution) to maximize reliability.

---

## Key Constraints

- **Market:** US equities only
- **Direction:** Long-only
- **Portfolio Size:** $5,000 (paper)
- **Trading Style:** Swing (days to weeks)
- **Min Hold:** 5 trading days
- **Benchmark:** SPY
- **Data Sources:** yfinance (free), RSS feeds (free)
- **Execution Model:** First-hour VWAP from 1h bars

---

## Daily Schedule (America/New_York)

### Pre-Market
- **08:05 ET** - Idea candidates digest (premarket)
- **08:30 ET** - Swing scan (pre-open)

### Post-Market  
- **16:45 ET** - Swing scan (post-close)
- **17:05 ET** - Idea candidates digest (post-close)

### Continuous
- **Hourly** - RSS news ingestion
- **Every 30 min (UTC)** - Approval timeout sweep

---

## Critical Files

### Configuration & Guidance
- **CLAUDE.md** - AI assistant quick-start guide (read this first!)
- **signalsmith-prd.md** - Full product requirements document
- **AGENTS.md** - 3-layer architecture details
- **SOUL.md** - Personality and behavior guidelines
- **HEARTBEAT.md** - Monitoring checklist

### Code Organization
- **directives/** - Pipeline SOPs (natural language)
- **execution/** - Python scripts (deterministic)
- **schema/** - Supabase table definitions
- **.env** - Environment variables (Supabase, API keys)
- **.venv/** - Python virtual environment

---

## Quick Start (For AI Assistants)

1. **Read CLAUDE.md first** - Full context and instructions
2. **Always activate venv:** `source .venv/bin/activate`
3. **Check directives before acting:** `directives/<pipeline>.md`
4. **Run execution scripts:** `python3 execution/<script>.py`
5. **Update directives when you learn something**

---

## Operating Principles

1. **Check for tools first** - Don't write new scripts if one exists
2. **Self-anneal** - Fix errors, test, update directives, make system stronger
3. **Reliability first** - Fail loudly, log everything, prefer idempotent runs
4. **Paper only** - No live trading without explicit approval

---

## Data Model (Supabase)

### Trading Tables
- `paper_portfolio` - Portfolio metadata
- `paper_orders` - Generated orders
- `paper_fills` - Executed trades
- `paper_positions` - Current holdings
- `paper_equity_curve` - Portfolio value history

### Market Data
- `prices_daily` - OHLCV data
- `benchmark_prices_daily` - SPY data
- `features_daily` - Derived features

### News & Documents
- `docs_raw` - Raw content
- `docs_text` - Cleaned text
- `docs_extracted` - LLM extractions

### Operations
- `pipeline_runs` - Execution logs
- `approval_requests` - Pending approvals

---

## Current Status

- ✅ **Swing Book:** Active (paper trading)
- ✅ **News Ingestion:** Active (hourly RSS)
- ✅ **Idea Digests:** Active (pre/post market)
- ❌ **Model Book (Top 10):** De-scoped (not active)
- ❌ **Live Trading:** Out of scope

---

## Getting Help

- **Full Documentation:** `/srv/signalsmith/SignalSmith-US/docs/`
- **PRD:** `signalsmith-prd.md`
- **AI Guide:** `CLAUDE.md`
- **Operator:** Jordan (via Telegram)

---

_For detailed instructions, see CLAUDE.md_
