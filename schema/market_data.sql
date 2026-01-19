-- Core market data + modeling tables.
-- Aligns with PRD defaults (US-only, S&P 500 universe, SPY benchmark).

create table if not exists instruments (
  ticker text primary key,
  company_name text,
  sector text,
  cik text,
  exchange text,
  active_flag boolean default true,
  created_at timestamptz not null default now()
);

create table if not exists universe_versions (
  version_id text primary key,
  as_of_date date not null,
  members_json jsonb not null,
  notes text,
  created_at timestamptz not null default now()
);

create index if not exists idx_universe_versions_as_of on universe_versions(as_of_date desc);

create table if not exists prices_daily (
  date date not null,
  ticker text not null references instruments(ticker),
  open double precision,
  high double precision,
  low double precision,
  close double precision,
  adj_close double precision,
  volume double precision,
  source text,
  ingested_at timestamptz not null default now(),
  primary key (date, ticker)
);

create index if not exists idx_prices_daily_ticker_date on prices_daily(ticker, date desc);

create table if not exists benchmark_prices_daily (
  date date not null,
  symbol text not null,
  open double precision,
  high double precision,
  low double precision,
  close double precision,
  adj_close double precision,
  volume double precision,
  source text,
  ingested_at timestamptz not null default now(),
  primary key (date, symbol)
);

create index if not exists idx_benchmark_prices_daily_symbol_date on benchmark_prices_daily(symbol, date desc);

-- Feature + label storage (market-first; doc features to follow)
create table if not exists features_daily (
  date date not null,
  ticker text not null references instruments(ticker),
  feature_set_version text not null,
  features_json jsonb not null,
  created_at timestamptz not null default now(),
  primary key (date, ticker, feature_set_version)
);

create index if not exists idx_features_daily_date on features_daily(date desc);
create index if not exists idx_features_daily_ticker on features_daily(ticker);

create table if not exists labels (
  date date not null,
  ticker text not null references instruments(ticker),
  horizon_days integer not null,
  excess_return double precision,
  y_class double precision,
  created_at timestamptz not null default now(),
  primary key (date, ticker, horizon_days)
);

create index if not exists idx_labels_ticker_horizon on labels(ticker, horizon_days);

create table if not exists model_runs (
  model_run_id text primary key,
  train_start date,
  train_end date,
  horizon_days integer,
  feature_set_version text,
  metrics_json jsonb,
  artifact_ref text,
  created_at timestamptz not null default now()
);

create index if not exists idx_model_runs_horizon on model_runs(horizon_days);
create index if not exists idx_model_runs_created on model_runs(created_at desc);

create table if not exists predictions (
  model_run_id text references model_runs(model_run_id),
  date date not null,
  ticker text not null references instruments(ticker),
  horizon_days integer not null,
  score double precision,
  rank integer,
  explanation_json jsonb,
  created_at timestamptz not null default now(),
  primary key (model_run_id, date, ticker, horizon_days)
);

create index if not exists idx_predictions_date_horizon on predictions(date, horizon_days);
create index if not exists idx_predictions_ticker on predictions(ticker);

