---
title: SignalSmith US - PRD (Revised for moomoo OpenAPI Market Data)
project: SignalSmith-US
type: prd
status: living
version: 0.3
owner: Jordan
updated: 2026-02-04
tags: [signalsmith, prd, trading-bot, ml, moomoo, market-data, supabase, openclaw, hostinger, telegram]
---

# SignalSmith US
**Product Requirements Document (PRD)**
_Revised to incorporate moomoo OpenAPI market data + quotas/limits._

---

## 1. Product vision
SignalSmith US is a long-only US stock ranking and paper-trading system that produces a **daily Top 10** list designed to **outperform SPY (S&P 500 proxy)** over a **short horizon**, while enforcing a **minimum hold period of 5 trading days**.
It also operates as an **always-on agent** that monitors news and announcements 24/7, updates the research context, and alerts the operator as meaningful events occur.

The MVP is intentionally “simple but real”: a reliable daily pipeline, solid market data ingestion, deterministic paper trading with VWAP fills, and a supervised-learning baseline. Once that spine is sturdy, we layer in higher-signal data (flows, options, microstructure, LLM-extracted news fields) and improve the model.

---

## 2. Core constraints (from current requirements)
- **Market:** US only
- **Direction:** Long-only
- **Ranking cadence:** Daily (pre-open)
- **Picks:** Top **N = 10**
- **Minimum hold:** **5 trading days**
- **Portfolio size:** **$5,000 USD** (paper)
- **Benchmark:** **SPY**
- **Execution model:** **VWAP**
- **LLM:** Gemini, budget **$5/day**
- **Infrastructure:** Python, deployed on a Hostinger VPS with OpenClaw Gateway, tables in Supabase
- **Orchestration:** OpenClaw heartbeat + cron, with approval gates for any live trading actions (Telegram inline buttons)
- **Notifications:** Telegram (already configured in this repo)
- **Timezone:** Australia/Brisbane (AEST, no DST) for operator context; market timing computed in America/New_York with DST handling
- **Trading mode:** Paper trading now; live trading later with explicit approval gates
- **Live broker (future):** moomoo OpenAPI Trade API
- **Pre-open awareness:** system should incorporate news and pre-market state before the open

---

## 3. Success criteria
### 3.1 MVP success (engineering)
- Runs daily without manual intervention (or fails loudly with actionable logs).
- Produces a reproducible Top 10 + feature snapshot + model score artifact.
- Paper trading executes deterministically (VWAP-based fills), positions are tracked, and performance vs SPY is computed daily.
- All key events are logged to Supabase (inputs → outputs → trades → PnL).
- OpenClaw runs 24/7 on the Hostinger VPS with stable heartbeat/cron scheduling and Telegram notifications.
- Self-annealing loop captures failures, applies fixes, adds tests, and updates directives with approval.

### 3.2 MVP success (quant)
- The baseline model/backtest framework is valid (no obvious leakage, survivorship bias is acknowledged and mitigated where feasible).
- A first supervised model produces a measurable lift over trivial baselines in offline evaluation (even if modest).

---

## 4. System overview
SignalSmith US is built in your **3-layer architecture**:

- **Layer 1: Directives** (SOPs): define “what to do” per pipeline segment.
- **Layer 2: Orchestration**: routes daily runs, handles errors, manages budget, writes logs.
- **Layer 3: Execution** (Python): deterministic ingestion, transforms, feature building, backtests, paper execution.

In Obsidian, this maps cleanly to your hub:
- Control Panel, PRD, pipeline canvas
- Directive index + execution index
- Orchestration notes (Daily Pre-open Run, Backfill + Rebuild, LLM Budget Control)
- Logs (daily run logs)

OpenClaw Gateway provides the always-on orchestration layer on the Hostinger VPS:
- Runs heartbeat for continuous monitoring and cron for scheduled tasks (operator timezone: Australia/Brisbane; market timing in America/New_York with DST handling).
- Exposes deterministic scripts in `execution/` as tools and follows directives in `directives/`.
- Uses Telegram for alerts, summaries, and approval requests (inline buttons).
- Enforces approval gates for any live trading actions (paper trading is fully automated).

### 4.1 Automation schedule (ET + Brisbane reference)
Market-timed cron jobs are scheduled in `America/New_York` so DST is handled automatically. Operator context and heartbeat timing use `Australia/Brisbane`.

**Cron jobs (recurring)**
- **Pre-open full run:** 08:45 ET, Mon-Fri
  - Brisbane reference: 23:45 AEST (during US standard time), 22:45 AEST (during US daylight time)
- **Post-close report:** 16:30 ET, Mon-Fri
  - Brisbane reference: 07:30 AEST next day (US standard time), 06:30 AEST next day (US daylight time)
- **Approval timeout sweep:** every 5 minutes (UTC)
- **After-hours digest (optional):** 19:30 ET, Mon-Fri
  - Brisbane reference: 10:30 AEST next day (US standard time), 09:30 AEST next day (US daylight time)
- **Weekly maintenance (optional):** 10:00 AEST, Sat

**Heartbeat**
- Every 30 minutes, 24/7 (quiet by default; only emits alerts when needed).

---

## 5. Market data strategy (moomoo OpenAPI)
This revision assumes moomoo OpenAPI is a primary market data “engine”. The most leverage comes from combining:

1) **Price/volume + cross-sectional momentum/mean reversion (baseline)**
2) **Pre-market information** (pre-market price/volume/turnover)
3) **Liquidity + microstructure proxies** (bid/ask, spread, volume ratio, bid-ask ratio)
4) **Capital flow** (if available via API)
5) **Derivatives / options surface signals** (if available via API)
6) **LLM-extracted fields from news/filings** (budgeted)

### 5.1 Highest-leverage endpoints to implement early
**Quote Interface (core)**  
Implement these first because they create the backbone for features and execution timing:
- `get_market_snapshot` (batch snapshot)
- `get_cur_kline` / historical kline request (candles)
- `get_stock_quote` (if snapshot doesn’t cover what you need)
- `get_order_book` + `get_rt_ticker` (later, if you pursue microstructure)
These are explicitly listed under Quote Interface in the docs. :contentReference[oaicite:0]{index=0}

**Market-state awareness**  
Use `get_market_state` so the scheduler behaves correctly around pre-market/open/close. Docs explicitly recommend it for US due to trading-time differences. :contentReference[oaicite:1]{index=1}

### 5.2 What “snapshot” gives you (why it’s gold)
The `get_market_snapshot` response includes many fields that are directly useful as features:
- price/ohlc-ish fields: high/open/low/lastClose/curPrice
- liquidity fields: askPrice/bidPrice, askVol/bidVol
- **microstructure proxies:** `bidAskRatio`, `volumeRatio`
- **pre-market:** `prePrice`, `preHighPrice`, `preLowPrice`, `preVolume`, `preTurnover`
- additional useful items: avgPrice, turnoverRate, 52-week highs/lows, etc. :contentReference[oaicite:2]{index=2}

It also includes an `equityExData` block with fundamental-ish ratios like PE/PB and dividends, which can be used for cross-sectional ranking features (value/quality-ish factors). :contentReference[oaicite:3]{index=3}

### 5.3 API limits/quotas you must design around
- **Frequency limiting example:** “Get Market Snapshot” allows **max 60 requests every 30 seconds**. :contentReference[oaicite:4]{index=4}
- Snapshot request supports up to **400 codes** per call via `code_list`. :contentReference[oaicite:5]{index=5}
- Docs also describe **subscription quota + historical candlestick quota** tiers (important for scaling real-time subscriptions and historical requests). :contentReference[oaicite:6]{index=6}

### 5.4 Connection hygiene (reliability)
The docs emphasize closing the quote context to avoid too many connections. :contentReference[oaicite:7]{index=7}  
Push data (if you use subscriptions later) requires starting/stopping the internal processing loop. :contentReference[oaicite:8]{index=8}

---

## 6. MVP scope (what we build first)
### 6.1 In scope (MVP)
- Universe: S&P 500 constituents (initially static list; later auto-refresh)
- Daily pre-open run that:
  1) checks market state
  2) pulls snapshot + required candles
  3) builds features
  4) scores and ranks (supervised baseline)
  5) generates Top 10 and target weights
  6) paper-trades using VWAP simulation
  7) logs everything to Supabase and writes Obsidian run log
- Backtest harness (walk-forward capable, even if simple in v1)
- Model registry: store model metadata + feature versions
- LLM extraction pipeline (budgeted) for a limited set of sources/fields
- OpenClaw Gateway running on Hostinger VPS with heartbeat/cron scheduling in Australia/Brisbane and Telegram alerting

### 6.2 Out of scope (MVP)
- Live trading with real money (until approval gates and broker integration are implemented)
- Complex portfolio optimizers (mean-variance, CVaR)
- High-frequency strategies
- Full-scale news ingestion across “everything on the internet” (we’ll narrow to a controlled set first)

---

## 7. Data model (Supabase tables)
Design the schema to support both: (a) daily runs, (b) backtests, (c) auditing.

**Core**
- `universe_symbols` (symbol, source, active_from/to, sector, etc.)
- `market_snapshot_raw` (run_id, ts, symbol, raw_json, permission_level)
- `bars_ohlcv` (symbol, timeframe, ts, open, high, low, close, volume, vwap_if_available)
- `features_daily` (run_id, symbol, feature_version, feature_json or wide columns)
- `signals` (run_id, symbol, score, rank, model_version, explanation_refs)
- `portfolio_positions` (as-of, symbol, qty, avg_cost, hold_days_remaining)
- `paper_orders` (run_id, symbol, side, target_qty, decision_ts)
- `paper_fills` (order_id, fill_ts, fill_price, fill_method = VWAP)
- `pnl_daily` (date, portfolio_value, return, benchmark_return, drawdown)
- `run_log` (run_id, stage, status, metrics_json, error_text)

**LLM**
- `documents_raw` (source, url, fetched_ts, raw_text)
- `documents_extracted` (doc_id, model, cost, extracted_fields_json, confidence)
- `entity_events` (symbol, event_type, event_ts, payload_json)

**Governance / Ops**
- `approval_requests` (request_id, created_ts, request_type, payload_json, status, approved_by, approved_ts)
- `approval_actions` (request_id, action_ts, channel, actor, action, notes)
- `notifications` (channel, severity, created_ts, payload_json, delivered_ts, status)

---

## 8. Modeling approach (MVP = supervised learning baseline)
### 8.1 Prediction target (initial)
- Predict **forward 5-trading-day return** (regression) or **outperformance vs SPY** (classification).
- Enforce hold constraint by construction: once picked, it stays in portfolio until min-hold satisfied (unless risk rules trigger).

### 8.2 Feature sets (phased)
**Phase 1 (baseline “price + snapshot”)**
- Momentum: 1d/5d/20d returns
- Volatility: 5d/20d realized vol
- Volume anomalies: volume ratio proxies
- Liquidity proxies: spread (ask-bid), bidAskRatio, turnoverRate
- Pre-market deltas: prePrice vs lastClose, preVolume, preTurnover (from snapshot) :contentReference[oaicite:9]{index=9}

**Phase 2 (flows + richer structure)**
- Add capital-flow endpoints if used (listed in docs as quote interface items). :contentReference[oaicite:10]{index=10}

**Phase 3 (options / derivatives)**
- If you enable option endpoints (docs list “Option quote interface”). :contentReference[oaicite:11]{index=11}
- Derived signals: implied vol level, skew, IV change, put/call proxies (depending on what the API actually returns)

**Phase 4 (LLM-extracted fields)**
- Extract structured “event features” from news/filings:
  - earnings beats/misses
  - guidance up/down
  - lawsuits/regulatory flags
  - analyst upgrades/downgrades
  - insider buying/selling (if sourced)
- Hard budget guardrails (Gemini $5/day) with caching + priority queue.

---

## 9. Paper trading (VWAP)
Paper trading is the only execution mode in the MVP. Live trading will be added later behind explicit approval gates and broker integration.
### 9.1 Execution rules
- Rebalance once per day (pre-open decision, “execute” at market open VWAP or first-hour VWAP depending on simulation choice).
- Long-only, equal-weight Top 10 by default.
- Respect minimum hold: no sells until day 5 unless a safety rule triggers.

### 9.2 Fill model (MVP)
- VWAP fills computed from intraday bars (if available) or approximated with daily VWAP proxy.
- Slippage model (simple): spread-based + volatility-based haircuts (start small and conservative).

---

## 10. Observability & controls
- Every run produces:
  - run_id
  - dataset versions (snapshot timestamp, bars timestamp)
  - feature version hash
  - model version hash
  - Top 10 + scores
  - paper orders + fills
  - SPY benchmark return and portfolio return

- Notifications are delivered via Telegram (run summaries and alerts).
- Approval gates are mandatory for any live trading action; approvals use Telegram inline buttons and are logged with full audit trail.
- Alerts:
  - market data missing for >X% of universe
  - API limit warnings (snapshot frequency, quotas) :contentReference[oaicite:12]{index=12}
- LLM budget exceeded
- pipeline stage failure

### 10.1 Self-annealing loop (core requirement)
- Detect: classify failures from run logs, API responses, and data-quality checks.
- Diagnose: identify root cause and propose deterministic fixes (script changes, retries, new guards).
- Repair: implement fix in execution scripts and add/extend tests.
- Document: update relevant directive with the new edge case or constraint (with approval).
- Validate: re-run the failed stage in isolation and verify expected outputs.

### 10.2 Approval UX (Telegram inline buttons)
- Buttons: `Approve`, `Deny`, `Defer` (if time allows).
- Callback data values: `approve`, `deny`, `defer`.
- On click, the callback is routed back to the agent as a message and logged to `approval_actions`.
- Timeout: auto-deny after 15 minutes with `actor=auto_timeout`, a logged audit entry, and a Telegram notification that includes request details.

---

## 11. Delivery phases & milestones

### Phase 0 — Foundation (DONE / mostly done)
**Goal:** Obsidian hub + repo scaffold + pipeline map.
**Milestone checklist**
- Control Panel, indexes, orchestration notes, logs, pipeline canvas created.
- Repo structure matches the 3-layer design.
**Acceptance:** You can navigate the system in Obsidian and know “where things go”.

---

### Phase 0.5 — Agent Ops (OpenClaw on Hostinger VPS)
**Goal:** 24/7 runtime, scheduling, Telegram alerting, and approval gates for live actions.
**Milestone checklist**
- Provision Hostinger VPS and install OpenClaw Gateway as a daemon.
- Configure agent workspace to the repo path on the VPS (and local dev path) and load directives/skills.
- Configure tools: web search/fetch, execution scripts, and Telegram channel integration.
- Add cron jobs for pre-open and EOD runs; add heartbeat for continuous news monitoring.
- Implement approval-gate workflow for any live trading action (Telegram inline buttons; paper trading auto-allowed).
**Acceptance:** Agent runs continuously, posts heartbeat summaries to Telegram, and cron jobs execute on schedule.

---

### Phase 1 — Market Data Spine (moomoo OpenAPI)
**Goal:** Reliable US market data ingestion + feature-ready storage.

**Milestone 1.1: Connection + health**
- Stand up moomoo OpenAPI connectivity from your runtime environment.
- Ensure quote context opens/closes cleanly. (Avoid connection buildup.) :contentReference[oaicite:13]{index=13}
- Write a “health probe” execution script:
  - checks `get_market_state` :contentReference[oaicite:14]{index=14}
  - pulls a small snapshot set (e.g., SPY, AAPL, MSFT)

**Milestone 1.2: Snapshot ingestion**
- Implement `get_market_snapshot(code_list)` batch pull. :contentReference[oaicite:15]{index=15}
- Persist raw snapshot JSON + parsed columns.
- Respect constraints:
  - max 400 symbols per call :contentReference[oaicite:16]{index=16}
  - rate limits (design batching/throttling) :contentReference[oaicite:17]{index=17}

**Milestone 1.3: Candles (daily OHLCV)**
- Implement daily kline ingestion (current + historical backfill).
- Store `bars_ohlcv` and verify continuity.

**Deliverables**
- `execution/ingest_snapshot.py`
- `execution/ingest_bars.py`
- `directives/ingest_market_data.md` (SOP: timing, limits, retries, storage)

**Acceptance**
- You can ingest and store snapshot + daily bars for the whole universe daily without errors.

---

### Phase 2 — Baseline Ranking + Paper Trading
**Goal:** Produce daily Top 10 + execute paper portfolio with VWAP.

**Milestone 2.1: Feature builder v1**
- Compute baseline features (momentum/vol/volume/liquidity/pre-market).
- Use snapshot fields like bid/ask, bidAskRatio, volumeRatio, pre-market fields. :contentReference[oaicite:18]{index=18}

**Milestone 2.2: Ranker v0**
- Start with a deterministic scoring baseline (before ML):
  - e.g., momentum + liquidity filter + volatility penalty
- Output: Top 10 + score breakdown.

**Milestone 2.3: Paper execution**
- Portfolio rules:
  - equal weight Top 10
  - min-hold 5 trading days
- VWAP fill simulation and PnL tracking vs SPY.

**Deliverables**
- `execution/build_features_v1.py`
- `execution/rank_v0.py`
- `execution/paper_trade_v1.py`
- `directives/paper_trading.md`

**Acceptance**
- You get a daily run artifact: Top 10 + trades + updated portfolio + benchmark comparison.

---

### Phase 3 — Supervised Learning MVP
**Goal:** Replace heuristic scoring with a supervised model.

**Milestone 3.1: Labeling + dataset build**
- Create forward-5d return labels and train dataset snapshots.
- Implement leakage guards: strict “as-of” timestamps.

**Milestone 3.2: Train baseline model**
- Start with:
  - regularized linear model OR gradient boosting baseline
- Track:
  - feature importance
  - out-of-sample metrics
  - stability across regimes

**Milestone 3.3: Model registry + promotion**
- Store model artifacts, metadata, and training config.
- Promotion rule: only deploy if it beats baseline in backtest.

**Deliverables**
- `execution/build_training_set.py`
- `execution/train_model_v1.py`
- `execution/score_model_v1.py`
- `directives/model_training.md`

**Acceptance**
- The daily run uses the supervised model scores to rank Top 10 and logs model version.

---

### Phase 4 — LLM Extraction (Budgeted) + Pre-open News Layer
**Goal:** Add structured event features from unstructured text without blowing the $5/day budget.

**Milestone 4.1: Source shortlist + fetchers**
- Pick 3–5 sources to start (SEC filings feed, earnings press releases, a news feed).
- Fetch and store raw documents.

**Milestone 4.2: Extraction schema**
- Define a stable JSON schema of extracted fields (event_type, sentiment, magnitude, confidence, symbol mapping).
- Use caching (hash-based) so repeated docs don’t cost more.

**Milestone 4.3: Budget controller**
- Enforce:
  - daily spend cap ($5)
  - symbol priority queue (only run LLM for candidates near the cutoff / held names)

**Deliverables**
- `execution/fetch_docs.py`
- `execution/extract_fields_gemini.py`
- `execution/merge_llm_features.py`
- `directives/llm_extraction.md`

**Acceptance**
- Pre-open ranking includes LLM-derived event features for a controlled subset of symbols.

---

### Phase 5 — Higher-signal Market Data (Flows, Options, Microstructure)
**Goal:** Add the “spicy ingredients” only after the kitchen is clean.

**Milestone 5.1: Capital flow**
- Implement quote interface flow endpoints (listed in docs). :contentReference[oaicite:19]{index=19}
- Evaluate whether flow features improve short-horizon predictability.

**Milestone 5.2: Options (if supported)**
- Implement option quote interface endpoints. :contentReference[oaicite:20]{index=20}
- Build derived IV-based features.

**Milestone 5.3: Microstructure (optional)**
- Add `get_order_book`, `get_rt_ticker`, broker queue only if you have a clear use case. :contentReference[oaicite:21]{index=21}
- This increases complexity and runtime sensitivity.

**Acceptance**
- You can A/B test feature groups and keep only what improves real metrics.

---

### Phase 6 — Live Trading (Moomoo Trade API, gated)
**Goal:** Enable live execution only after approvals, testing, and risk controls are in place.

**Milestone 6.1: Broker integration (trade API)**
- Integrate moomoo OpenAPI Trade API for order routing.
- Enforce paper/live separation at config level (no accidental live calls).

**Milestone 6.2: Approval workflow**
- Telegram inline buttons for approve/deny.
- Timeout + escalation path (configurable).
- All approvals logged to `approval_requests` and `approval_actions`.

**Milestone 6.3: Risk controls**
- Max position size, max daily turnover, and kill switch.
- Circuit breaker if data quality or model drift fails thresholds.

**Acceptance**
- Live trades only occur with explicit approval and logged audit trail.

---

## 12. Risks & mitigations
- **Overfitting:** use walk-forward validation, keep features minimal early, log performance decay.
- **Leakage:** strict “as-of” data; do not use future bars in feature windows.
- **Survivorship bias:** if using current S&P list, acknowledge bias; later ingest historical membership.
- **API limits/quotas:** bake throttling and batching into ingestion. :contentReference[oaicite:22]{index=22}
- **Infrastructure mismatch:** moomoo OpenAPI may require OpenD and stable connectivity; treat this as a first-class reliability requirement.
- **Timezone/DST errors:** compute market timing in America/New_York and log derived Brisbane schedule daily.
- **VPS single point of failure:** add uptime monitoring + restart policies; keep backup configs.

---

## 13. Open questions (to lock the next sprint)
1) **Approval escalation:** Telegram inline buttons are confirmed; auto-deny after 15 minutes with Telegram notification. Escalation beyond that is optional.
2) **Universe source:** do you want *current* S&P 500 constituents only, or a broader universe (e.g., Russell 3000) later?
3) **Decision time:** how many minutes before the US open do you want the ranking frozen (T-60? T-30?) and do you want to incorporate *pre-market moves* into the score?
4) **Paper VWAP definition:** open-to-close VWAP? first-hour VWAP? or “market open VWAP proxy”?
5) **Rebalance style:** equal-weight Top 10 daily, or only replace names when they fall below a rank threshold (turnover control)?
6) **LLM sources:** what’s your initial “starter pack” shortlist (SEC filings + earnings releases + one news feed), or do you want me to propose one?

---

## 14. Practical next step (recommended)
Treat the next sprint as: **Phase 0.5 (Agent Ops)** followed by **Phase 1, Milestone 1.1–1.2**.
If OpenClaw uptime + scheduling are rock solid and snapshot + market-state + storage are stable, everything else becomes much easier (and cheaper).
