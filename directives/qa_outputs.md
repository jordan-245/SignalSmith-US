---
layer: directive
tags: [layer/directive]
---

# qa_outputs

## Purpose
QA extracted JSON and features to catch bad parses/mappings.

## Inputs
- Samples from `docs_extracted`
- QA rules (schema, sentiment bounds, ticker confidence)
- Feature summaries from `features_daily`

## Outputs
- QA findings and issue list
- Corrections/exclusions
- Run log for qa_outputs

## Tools/Scripts (links to execution scripts)
- [[20_EXECUTION/qa_outputs]]

## Edge cases
- Over-filtering; watch coverage
- Ambiguous/low-confidence tickers; manual review
- Schema drift; align QA rules

## Run steps
1. Sample extractions; validate schema/bounds.
2. Spot-check sentiment/tone; flag hallucinations.
3. Cross-check tickers vs entities; drop/adjust low-confidence.
4. Mark fixes/exclusions; log issues and feed back into prompts.

## Learnings / Updates
- 
