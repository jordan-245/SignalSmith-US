# CLAUDE.md - AI Assistant Guide for SignalSmith US

**Last Updated:** 2026-02-09  
**Project:** SignalSmith US - Autonomous Swing Trading System (Paper Only)

---

## 🎯 Quick Overview

SignalSmith US is an **always-on, long-only US equity swing trading system** that runs on a Hostinger VPS with OpenClaw orchestration. It scans equities, generates signals, executes paper trades, and notifies the operator via Telegram.

**Critical:** This is **PAPER ONLY** by default. No live trading without explicit approval gates.

---

## 📁 Project Structure

```
/srv/signalsmith/SignalSmith-US/
├── directives/          # SOPs - natural language instructions per pipeline
├── execution/           # Deterministic Python scripts (the actual work)
├── data/                # Local data cache
├── output/              # Pipeline outputs, backtests, reports
├── schema/              # Supabase SQL schemas
├── docs/                # Documentation
├── .env                 # Environment variables (Supabase, API keys)
├── .venv/               # Python virtual environment
├── signalsmith-prd.md   # Full Product Requirements Document
├── AGENTS.md            # 3-layer architecture explanation
├── HEARTBEAT.md         # Heartbeat monitoring checklist
└── CLAUDE.md            # This file
```

---

## 🏗️ Architecture (3 Layers)

You operate within a 3-layer architecture that separates concerns to maximize reliability. **LLMs are probabilistic, whereas most business logic is deterministic and requires consistency.** This system fixes that mismatch.

### Layer 1: Directive (What to do)
- Basically just SOPs written in Markdown, live in `directives/`
- Define the goals, inputs, tools/scripts to use, outputs, and edge cases
- Natural language instructions, like you'd give a mid-level employee
- **Examples:** `ingest_docs.md`, `swing_scan.md`, `build_features.md`

### Layer 2: Orchestration (Decision making) — **THIS IS YOU**
- **Your job:** Intelligent routing
- Read directives, call execution tools in the right order, handle errors, ask for clarification, update directives with learnings
- You're the glue between intent and execution
- **Example:** You don't try scraping websites yourself; you read `directives/scrape_website.md`, define inputs/outputs, then run `execution/scrape_single_site.py`

### Layer 3: Execution (Doing the work)
- Deterministic Python scripts in `execution/`
- Environment variables, API tokens, etc are stored in `.env`
- Handle API calls, data processing, file operations, database interactions
- Reliable, testable, fast. Use scripts instead of manual work
- **Examples:** `swing_scan.py`, `ingest_prices.py`, `ingest_docs.py`

**Why this works:** If you do everything yourself, errors compound. 90% accuracy per step = 59% success over 5 steps. The solution is to push complexity into deterministic code. That way you just focus on decision-making.

---

## ⚙️ Core Constraints

- **Market:** US equities only
- **Direction:** Long-only
- **Portfolio:** $5,000 paper portfolio (Swing Book)
- **Data:** Free stack (yfinance, RSS, HTML scraping)
- **Execution:** Paper trades only (first-hour VWAP from 1h bars)
- **Timezone:** Market timing = `America/New_York`, Operator = `Australia/Brisbane`
- **Benchmark:** SPY

---

## 🚀 Getting Started

### 1. Activate Virtual Environment
**ALWAYS** activate the venv before running Python scripts:
```bash
cd /srv/signalsmith/SignalSmith-US
source .venv/bin/activate
```

### 2. Check What's Running
```bash
openclaw cron list
openclaw status
```

### 3. Common Commands

**Run a directive:**
1. Read the directive: `directives/swing_scan.md`
2. Identify the execution script: `execution/swing_scan.py`
3. Run it: `python3 execution/swing_scan.py --help`

**Ingest prices (daily):**
```bash
source .venv/bin/activate
python3 execution/ingest_prices.py --date 2026-02-08
```

**Run swing scan (pre-open):**
```bash
source .venv/bin/activate
python3 execution/swing_scan.py --mode pre
```

**Check positions:**
```bash
source .venv/bin/activate
python3 execution/check_positions.py --portfolio-id swing
```

**Ingest news/docs:**
```bash
source .venv/bin/activate
python3 execution/ingest_docs.py --cutoff "08:15" --tz "America/New_York"
```

---

## 📋 Scheduled Jobs (OpenClaw Cron)

All times are `America/New_York` unless noted:

### Swing Trading (Active)
- **08:30 ET** - Swing scan (pre-open), Mon–Fri
- **16:45 ET** - Swing scan (post-close), Mon–Fri

### Idea Formation
- **08:05 ET** - Idea candidates digest (premarket), Mon–Fri
- **17:05 ET** - Idea candidates digest (post-close), Mon–Fri

### News Ingestion
- **Hourly** - RSS feed ingest

### Operations
- **Every 30 min (UTC)** - Approval timeout sweep

---

## 🛠️ Common Tasks

### Task: Fix a Broken Pipeline
1. Read the error logs
2. Check the relevant directive (e.g., `directives/ingest_docs.md`)
3. Fix the execution script (e.g., `execution/ingest_docs.py`)
4. Test the fix: `python3 execution/ingest_docs.py --dry-run`
5. Update the directive with learnings (add to "Learnings / Updates")

### Task: Add a New Feature
1. Check if a directive exists for this pipeline stage
2. If not, create one in `directives/`
3. Write the execution script in `execution/`
4. Test it thoroughly
5. Add to cron schedule if needed

### Task: Self-Anneal (Fix + Learn)
When something breaks:
1. **Fix it** (update the script)
2. **Test the tool** (make sure it works)
3. **Update the directive** (document what you learned)
4. **System is now stronger**

---

## 🔑 Key Files to Read

1. **signalsmith-prd.md** - Full product requirements
2. **AGENTS.md** - 3-layer architecture explained
3. **HEARTBEAT.md** - What to check during heartbeats
4. **SOUL.md** - Your personality and operating principles
5. **directives/*.md** - Pipeline-specific instructions

---

## 🧪 Data Sources

### Prices
- **Primary:** `yfinance` (daily OHLCV, 1h bars for execution)
- **Storage:** Supabase (`prices_daily`, `benchmark_prices_daily`)

### News
- **Sources:** RSS/Atom feeds → HTML fetch → text extraction
- **Extraction:** `readability-lxml` + BeautifulSoup fallback
- **Storage:** Supabase (`docs_raw`, `docs_text`, `docs_extracted`)

### Market Calendar
- **Library:** `exchange-calendars` (XNYS)
- **Purpose:** Skip pre-open pipelines on market-closed days

---

## 📊 Supabase Tables (Key)

### Trading
- `paper_portfolio` - Portfolio metadata
- `paper_orders` - Generated orders
- `paper_fills` - Executed fills
- `paper_positions` - Current positions
- `paper_equity_curve` - Portfolio value over time

### Market Data
- `prices_daily` - Daily OHLCV
- `benchmark_prices_daily` - SPY daily data
- `features_daily` - Derived features
- `labels` - Target labels for ML

### News & Docs
- `docs_raw` - Raw HTML/content
- `docs_text` - Cleaned text
- `docs_extracted` - LLM-extracted entities

### Operations
- `pipeline_runs` - Execution logs
- `approval_requests` - Pending approvals
- `approval_actions` - Approval history

---

## ⚠️ Operating Principles (Critical)

### 1. Check for Tools First
Before writing a script, check `execution/` per your directive. Only create new scripts if none exist.

### 2. Self-Anneal When Things Break
- Read the error message and stack trace
- Fix the script and test it again (unless it uses paid tokens/credits/etc, in which case check with the user first)
- Update the directive with what you learned (API limits, timing, edge cases)

**Example:** You hit an API rate limit → investigate the API → find a batch endpoint → rewrite the script to accommodate → test → update the directive.

### 3. Update Directives as You Learn
Directives are living documents. When you discover API constraints, better approaches, common errors, or timing expectations, update the directive.

**BUT:** Don't create or overwrite directives without asking unless explicitly told to. Directives are your instruction set and must be preserved and improved over time, not used and discarded.

### 4. Self-Annealing Loop
Errors are learning opportunities. When something breaks:
1. Fix it
2. Update the tool
3. Test the tool, make sure it works
4. Update the directive to include the new flow
5. System is now stronger

### 5. Reliability First
- Fail loudly with actionable logs
- Prefer idempotent runs
- Log everything to `pipeline_runs`

### 6. Paper Only
No live trading without explicit approval gates. Period.

---

**Remember:** You are the middle layer between human intent (directives) and deterministic execution (Python scripts). Read instructions, make decisions, call tools, handle errors, continuously improve system.

- Be reliable.
- Self-anneal.

---

## 🐛 Debugging Tips

### Dependency Issues
All scripts require the venv:
```bash
source .venv/bin/activate
```

### Missing Data
Check Supabase connectivity:
```bash
python3 -c "from dotenv import load_dotenv; load_dotenv(); import os; print(os.getenv('SUPABASE_URL'))"
```

### Cron Job Failures
Check recent runs:
```bash
openclaw cron runs --job-id <job-id>
```

### Pipeline Logs
Query Supabase `pipeline_runs` table for error messages.

---

## 📞 Getting Help

- **Full PRD:** `signalsmith-prd.md`
- **Architecture:** `AGENTS.md`
- **Operator:** Jordan (Telegram via OpenClaw)
- **Timezone:** Australia/Brisbane

---

## 🎓 Remember

You are **Layer 2 (Orchestration)**:
- Read directives
- Call execution scripts
- Handle errors
- Update directives with learnings
- Be resourceful before asking

You are **NOT**:
- A script executor (that's Layer 3)
- A directive writer (that's the operator, unless explicitly delegated)
- A live trader (paper only)

**Be reliable. Be deterministic. Self-anneal.**

---

_End of CLAUDE.md_
