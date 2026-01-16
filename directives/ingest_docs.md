---
layer: directive
tags: [layer/directive]
---

# ingest_docs

## Purpose
Collect web docs (news, filings, reports, holdings pages) before cutoff.

## Inputs
- Source configs
- Universe tickers, cutoff (08:15 ET)

## Outputs
- `docs_raw` with metadata + content_hash
- Run log entry for document_ingest

## Tools/Scripts (links to execution scripts)
- [[20_EXECUTION/ingest_docs]]

## Edge cases
- Robots/anti-bot; use cache/alt sources
- Dedupe by content_hash
- Rate limits/timeouts; backoff + queue

## Run steps
1. Queue docs by recency/relevance.
2. Fetch before cutoff; respect robots + rate limits.
3. Dedupe by hash; mark skips.
4. Store metadata/content in `docs_raw`; log counts/errors.

## Learnings / Updates
- 
