---
layer: directive
tags: [layer/directive]
---

# budget_monitoring

## Purpose
Keep LLM extraction spend under $5/day while preserving priority docs.

## Inputs
- LLM cost estimates per doc/run (from `docs_extracted`)
- Priority rules (ticker relevance, recency, source type)
- Daily budget target

## Outputs
- Spend dashboard/metrics and alerts
- Updated queues (paused/allowed docs)
- `pipeline_runs` entry for stage=budget_monitoring

## Tools/Scripts (links to execution scripts)
- [[20_EXECUTION/budget_monitoring]]

## Edge cases
- Sudden doc surges; throttle lower-priority sources
- Cost estimate drift; recalibrate based on recent tokens/costs
- Budget exhaustion mid-run; pause and resume next day

## Run steps
1. Summarize spend vs budget and forecast remaining capacity.
2. Reorder/trim extraction queue based on priority rules.
3. Apply throttles/pauses; log skipped items.
4. Emit alerts/warnings if budget hit or forecasts exceed cap.
5. Record decisions and queue state for transparency.

## Learnings / Updates
- 
