---
layer: directive
tags: [layer/directive]
---

# budget_monitoring

## Purpose
Keep LLM extraction spend under $5/day while preserving priority docs.

## Inputs
- Spend metrics from `docs_extracted`
- Priority rules (relevance, recency, source)
- Daily budget

## Outputs
- Spend metrics/alerts
- Updated extraction queues
- Run log for budget_monitoring

## Tools/Scripts (links to execution scripts)
- [[20_EXECUTION/budget_monitoring]]

## Edge cases
- Doc surges; throttle low priority
- Cost estimate drift; recalibrate
- Budget hit mid-run; pause/resume next day

## Run steps
1. Summarize spend vs budget; forecast remaining.
2. Reorder/trim queue by priority.
3. Throttle/pause; log skipped items.
4. Alert if budget near/hit; record decisions.

## Learnings / Updates
- 
