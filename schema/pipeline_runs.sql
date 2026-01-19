create table if not exists pipeline_runs (
  id uuid primary key default gen_random_uuid(),
  run_id text not null,
  tag text,
  stage text default 'unspecified',
  status text default 'unknown',
  date date not null,
  started_at timestamptz default now(),
  ended_at timestamptz,
  stats_json jsonb,
  warnings_json jsonb,
  val_auc double precision,
  top jsonb,
  positions jsonb,
  equity jsonb,
  report_path text,
  missing_tickers jsonb,
  created_at timestamptz not null default now()
);

create index if not exists idx_pipeline_runs_date on pipeline_runs(date desc);
create index if not exists idx_pipeline_runs_run_id on pipeline_runs(run_id);
create index if not exists idx_pipeline_runs_stage on pipeline_runs(stage);
