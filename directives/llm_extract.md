---
layer: directive
tags: [layer/directive]
---

# llm_extract

## Purpose
Use Gemini to extract schema-valid JSON within the $5/day budget.

## Inputs
- Pending docs from `docs_text`
- Extraction schema and priority rules
- Daily budget

## Outputs
- `docs_extracted` with JSON, status, cost
- Cache by content_hash
- Run log entry for llm_extract

## Tools/Scripts (links to execution scripts)
- [[20_EXECUTION/llm_extract]]

## Edge cases
- Budget cap; prioritize and pause low-priority docs
- JSON failures; retry once, then mark failed
- Timeouts/rate limits; backoff and queue

## Run steps
1. Build priority queue by relevance/recency/source.
2. Check budget; skip low-priority if tight.
3. Extract with Gemini; validate JSON; retry once on parse failure.
4. Cache by content_hash; write `docs_extracted` with cost/logs.

## Learnings / Updates
- 
