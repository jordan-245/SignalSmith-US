---
layer: directive
tags: [layer/directive]
---

# llm_extract

## Purpose
Use Gemini (stubbed here) to extract schema-valid JSON fields from cleaned documents within the $5/day budget, caching by content hash.

## Inputs
- Pending docs from `docs_text` (cleaned_text, metadata)
- Extraction schema (doc_type, event_types, sentiment, uncertainty, numeric_claims, tickers_mentioned, summary_bullets)
- Daily budget and priority rules; content_hash cache

## Outputs
- `docs_extracted` rows with schema_version, extracted_json, status, errors, cost/tokens
- Cache enforced by checking existing extraction per content_hash
- `pipeline_runs` entry for stage=llm_extract

## Tools/Scripts (links to execution scripts)
- [[20_EXECUTION/llm_extract]]

## Edge cases
- Budget cap reached; prioritize newest ticker-relevant docs and filings
- Invalid/partial JSON; retry once with stricter prompt then mark failed
- Non-English or low-quality text; drop or flag
- Timeouts/rate limits; enqueue for retry with backoff
- Duplicate content_hash: skip (cache)

## Run steps
1. Select cleaned docs from `docs_text`; skip content_hash already extracted.
2. Apply budget guard; estimate cost from tokens/length.
3. Extract (stub or Gemini); validate JSON and schema_version.
4. Write `docs_extracted` with cost/tokens/status; log run metrics.

## Learnings / Updates
- 
