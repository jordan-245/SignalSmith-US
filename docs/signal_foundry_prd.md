---
title: Signal Foundry - PRD (Free-First, US + ASX)
project: SignalSmith-US
type: prd
status: draft
version: 0.1
owner: Jordan
updated: 2026-02-07
tags: [signal_foundry, prd, multi_agent, ml, market_data, parquet, free_first]
---

# Signal Foundry
Product Requirements Document (PRD)
Free-first data, dual-market (US + ASX), parquet feature store, separate report page.

## 1) Vision
Signal Foundry is a daily stock prediction workbench that produces probabilistic forecasts, catalyst context, and rule-based trade plans for US and ASX equities. It is designed for multi-agent workflows: data, modeling, regime detection, skepticism, and execution design are separated into deterministic pipelines with explicit quality gates.

## 2) Goals
1. Generate daily probabilistic direction forecasts for 1D, 5D, and 20D horizons.
2. Provide a catalyst map per ticker with what matters right now.
3. Produce a model consensus from multiple model families with calibrated probabilities.
4. Output a rules-based trade plan with entries, invalidations, and position sizing guidance.
5. Provide a reality check with walk-forward backtests and calibration diagnostics.
6. Support US and ASX universes with the same architecture.
7. Run pre-open and after close pipelines for both exchanges.

## 3) Non-Goals
1. Live trading or broker integration.
2. Intraday trading or high-frequency execution.
3. Options or derivatives coverage in MVP.
4. Paid data dependency for MVP.

## 4) Users
1. Primary: single operator running research and paper trading.
2. Secondary: future multi-user team with shared reports and task queues.

## 5) Scope: MVP vs V1
MVP scope is intentionally narrow to validate data, modeling, and reporting quality before scaling.

MVP includes:
1. Universe: watchlist 20-50 tickers in US and ASX.
2. Data: daily OHLCV plus a small macro set.
3. Models: baseline logistic regression plus one tree model.
4. Output: a single daily report page per market.
5. Backtest: walk-forward on 3-5 years of daily data.

V1 adds:
1. Feature store with broader coverage and caching.
2. Ensemble model with calibration (Platt or Isotonic).
3. Regime-aware forecasting and regime-conditioned performance.
4. Paper trading ledger and performance dashboard.
5. Quality gates that block report promotion if minimum standards fail.

## 6) Core Constraints
1. Markets: United States and Australia (ASX).
2. Data: free-first sources, rate-limit aware.
3. Storage: parquet feature store as canonical analytics store.
4. Reports: separate report page per market, published daily.
5. Schedule: pre-open and after close for both exchanges.
6. Reliability: deterministic, idempotent pipelines with explicit run logs.

## 7) Inputs
1. Universe definitions:
2. US: S&P 500, watchlist, or user-defined list.
3. ASX: ASX 200, watchlist, or user-defined list.
4. Market data:
5. Daily OHLCV for all tickers and benchmarks.
6. Macro and sector proxies where available.
7. News and catalysts:
8. RSS feeds and HTML fetch for selected sources.

## 8) Outputs
Per market, per run:
1. Distribution forecasts per ticker: P(up 1D / 5D / 20D), expected return, downside tail risk.
2. Catalyst map: events, sentiment summary, and recency.
3. Model consensus: baseline + tree + regime-conditioned scores, with calibration.
4. Trade plan: entries, invalidations, position sizing suggestion.
5. Reality check: walk-forward metrics and calibration plots.
6. Summary rankings and top candidates.

## 9) Data Sources (Free-First)
Primary target sources for MVP:
1. Prices: yfinance or equivalent free source.
2. Macro: FRED and free public datasets where applicable.
3. Corporate actions: free provider if available, otherwise inferred from price series.
4. News: RSS feeds + direct HTML ingestion via readability.

Constraints:
1. Free sources may have gaps and rate limits.
2. Missing data is allowed but must be surfaced in warnings and coverage metrics.

## 10) Storage and Data Model
Canonical analytics store:
1. Parquet feature store for features, labels, predictions, and backtests.
2. Organized by market, date, and feature_set_version.

Operational store:
1. Supabase for pipeline run logs, audit trail, and lightweight UI queries.
2. Supabase remains optional but recommended for dashboards.

Minimum parquet layout:
1. data/foundry/features/market=US/feature_set=v1/date=YYYY-MM-DD/part.parquet
2. data/foundry/features/market=ASX/feature_set=v1/date=YYYY-MM-DD/part.parquet
3. data/foundry/labels/market=US/horizon=5d/date=YYYY-MM-DD/part.parquet
4. data/foundry/predictions/market=US/run_id=YYYYMMDDHHMM/part.parquet
5. data/foundry/backtests/market=US/run_id=YYYYMMDDHHMM/part.parquet

## 11) Model Stack
Baseline:
1. Logistic regression with market features.

Tree model:
1. LightGBM or CatBoost (free local training).

Ensemble:
1. Simple weighted average or stacking.
2. Calibration step applied to final probabilities.

Regime-aware layer:
1. Regime classifier outputs a discrete regime label.
2. Model performance and calibration computed per regime.

## 12) Feature Engineering
Market features:
1. Returns: 1D, 5D, 20D.
2. Volatility: rolling 20D.
3. Trend: MA ratios, price vs MA.
4. Relative strength vs benchmark.

Catalyst features:
1. Event flags from RSS and filings.
2. Sentiment aggregates per ticker and lookback window.

Regime features:
1. Risk-on vs risk-off proxies.
2. Volatility regime classification.
3. Macro change rates where available.

## 13) Backtesting and Evaluation
Walk-forward protocol:
1. Train on trailing window.
2. Score on next period.
3. Roll forward by fixed step.

Metrics:
1. AUC and precision-recall for direction.
2. Calibration and reliability curves.
3. Hit rate vs baseline.
4. Tail risk and drawdown proxies.

Quality gates:
1. Minimum training rows and coverage.
2. Performance must exceed baseline by a defined margin.
3. Calibration slope and error within tolerance.
4. No lookahead in feature or label generation.

## 14) Pipeline Schedule
Each market has its own pre-open and after-close run.

US schedule:
1. Pre-open run at 08:15 America/New_York.
2. After-close run at 16:45 America/New_York.

ASX schedule:
1. Pre-open run at 09:30 Australia/Sydney.
2. After-close run at 16:30 Australia/Sydney.

All schedules must use exchange calendars for holidays and early closes.

## 15) Reporting
Separate report page per market:
1. Foundry US report page.
2. Foundry ASX report page.

Report sections:
1. Top rankings with probabilities and expected return.
2. Catalyst map.
3. Regime summary.
4. Trade plans with entry and invalidation levels.
5. Calibration and recent backtest summary.

Publishing:
1. Reports are generated after each run.
2. Stored as Markdown and rendered to HTML for a static page.
3. Stored separately from swing dashboards.

## 16) Orchestration
Orchestrator responsibilities:
1. Sequential step execution with deterministic ordering.
2. Pipeline run logging with status and warnings.
3. Ability to run per market or both markets.
4. Ability to run on-demand for a custom universe.

## 17) Risks and Mitigations
1. Data gaps from free sources.
2. Mitigation: coverage checks, warn, and skip low-coverage tickers.
3. Model overfit due to small data.
4. Mitigation: baselines, cross-period evaluation, and calibration.
5. Lookahead leakage.
6. Mitigation: explicit cutoff times and strict date joins.
7. Schedule mismatches from time zones and DST.
8. Mitigation: exchange calendars and timezone-aware scheduling.

## 18) Acceptance Criteria
MVP acceptance:
1. Daily report generated for US and ASX for at least 10 consecutive trading days.
2. Walk-forward backtest runs with no lookahead flags.
3. Probabilities are calibrated within defined tolerance.
4. Report includes trade plan and catalyst map per ticker.

V1 acceptance:
1. Ensemble model with calibration.
2. Regime-aware forecasts with per-regime diagnostics.
3. Quality gates enforced before report publication.

## 19) Open Questions
1. Which ASX source is preferred for OHLCV if yfinance coverage is inconsistent.
2. Minimum acceptable universe size for ASX MVP.
3. Whether the report should be published via Streamlit or static HTML.
4. Whether a shared cross-market composite report is required.
