-- Paper trading tables for MVP.

create table if not exists paper_portfolio (
  portfolio_id text primary key,
  name text,
  starting_cash double precision,
  rules_json jsonb,
  created_at timestamptz not null default now()
);

create table if not exists paper_orders (
  order_id text primary key,
  date date not null,
  ticker text not null,
  side text not null,
  target_weight double precision,
  qty_estimate double precision,
  status text,
  created_at timestamptz not null default now()
);

create index if not exists idx_paper_orders_date on paper_orders(date desc);

create table if not exists paper_fills (
  fill_id text primary key,
  order_id text references paper_orders(order_id) on delete cascade,
  fill_price double precision,
  fill_method text,
  slippage_bps double precision,
  fees double precision,
  filled_at timestamptz,
  created_at timestamptz not null default now()
);

create index if not exists idx_paper_fills_order on paper_fills(order_id);

create table if not exists paper_positions (
  date date not null,
  portfolio_id text not null references paper_portfolio(portfolio_id),
  ticker text not null,
  qty double precision,
  avg_cost double precision,
  market_value double precision,
  entry_date date,
  eligible_sell_date date,
  created_at timestamptz not null default now(),
  primary key (date, portfolio_id, ticker)
);

create index if not exists idx_paper_positions_portfolio_date on paper_positions(portfolio_id, date desc);

create table if not exists paper_equity_curve (
  date date not null,
  portfolio_id text not null references paper_portfolio(portfolio_id),
  equity double precision,
  cash double precision,
  drawdown double precision,
  turnover double precision,
  created_at timestamptz not null default now(),
  primary key (date, portfolio_id)
);

create index if not exists idx_paper_equity_curve_portfolio_date on paper_equity_curve(portfolio_id, date desc);
