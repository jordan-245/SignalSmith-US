create table if not exists docs_raw (
  doc_id uuid primary key default gen_random_uuid(),
  url text not null,
  source text,
  published_at timestamptz,
  observed_at timestamptz not null default now(),
  content_type text,
  content_hash text not null,
  raw_content text,
  status text default 'ingested',
  created_at timestamptz not null default now()
);

create table if not exists docs_text (
  doc_id uuid primary key references docs_raw(doc_id) on delete cascade,
  cleaned_text text,
  language text,
  text_hash text,
  status text default 'cleaned',
  created_at timestamptz not null default now()
);

create unique index if not exists idx_docs_raw_content_hash on docs_raw(content_hash);
create index if not exists idx_docs_raw_published on docs_raw(published_at);
create unique index if not exists idx_docs_text_doc_id on docs_text(doc_id);
create index if not exists idx_docs_text_text_hash on docs_text(text_hash);

create table if not exists docs_extracted (
  doc_id uuid primary key references docs_raw(doc_id) on delete cascade,
  schema_version text,
  extracted_json jsonb,
  confidence double precision,
  status text default 'success',
  error_msg text,
  tokens_in integer,
  tokens_out integer,
  cost_estimate double precision,
  created_at timestamptz not null default now()
);

create index if not exists idx_docs_extracted_status on docs_extracted(status);
