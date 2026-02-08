---
layer: directive
tags: [layer/directive]
---

# ingest_docs

## Purpose
Collect web documents (news, filings, reports, holdings pages) and persist raw content + cleaned text for downstream extraction.

## Inputs
- Source configs (feeds, crawl targets, scraping rules)
- Universe tickers for relevance filtering
- Cutoff time (default: 08:15 ET, America/New_York)
- URL list or file of URLs to fetch

## Outputs
- `docs_raw` rows with url, source, published_at, observed_at, content_type, content_hash, raw_content, status
- `docs_text` rows with cleaned_text, language (optional), text_hash, status
- `pipeline_runs` entry for stage=document_ingest

## Tools/Scripts (links to execution scripts)
- [[20_EXECUTION/ingest_docs]]

## Edge cases
- Robots/anti-bot defenses; switch to cached sources where needed
- Hash dedupe by `content_hash` (batch + Supabase check)
- Large or binary assets; skip or store references only
- Rate limits/timeouts; backoff and queue for retry
- Cutoff enforcement: skip docs where published_at/observed_at > cutoff

## Run steps
1. Build URL list (args or file); enforce max_docs.
2. Fetch with user-agent; respect cutoff (published_at or observed_at).
3. Hash content; batch dedupe; skip existing hashes in Supabase.
4. Insert `docs_raw` then `docs_text` (cleaned HTML stripped of scripts/styles).
5. Log counts/errors.

## Learnings / Updates
- **2026-02-08**: Dependency issue resolved - `beautifulsoup4` was listed in requirements.txt but needed explicit venv activation. Created `check_new_docs.py` to track ingestion cadence and `preflight_check.py` to verify script imports before pipeline runs.
- All execution scripts require activating the venv: `source .venv/bin/activate` before running any Python scripts in the execution layer.
