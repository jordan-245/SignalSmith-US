-- Governance / Ops: approval request + audit trail tables
-- Used by execution/approval_timeout.py and Telegram approval workflows.

-- Requires pgcrypto for gen_random_uuid() (enabled by default on Supabase).

create table if not exists public.approval_requests (
  request_id uuid primary key default gen_random_uuid(),
  created_ts timestamptz not null default now(),
  request_type text not null,
  payload_json jsonb not null default '{}'::jsonb,
  status text not null default 'pending',
  approved_by text,
  approved_ts timestamptz,
  -- basic hygiene
  constraint approval_requests_status_chk
    check (status in ('pending','approved','denied','expired','cancelled')),
  constraint approval_requests_approved_fields_chk
    check (
      (status = 'pending' and approved_by is null and approved_ts is null)
      or (status <> 'pending')
    )
);

create index if not exists idx_approval_requests_status_created
  on public.approval_requests (status, created_ts);

create index if not exists idx_approval_requests_created
  on public.approval_requests (created_ts desc);

create table if not exists public.approval_actions (
  action_id uuid primary key default gen_random_uuid(),
  request_id uuid not null references public.approval_requests(request_id) on delete cascade,
  action_ts timestamptz not null default now(),
  channel text,
  actor text,
  action text not null,
  notes text
);

create index if not exists idx_approval_actions_request_ts
  on public.approval_actions (request_id, action_ts desc);
