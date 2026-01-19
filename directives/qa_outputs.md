---
layer: directive
tags: [layer/directive]
---

# qa_outputs

## Purpose
Quality-check extracted JSON and downstream features to catch bad parses, hallucinations, or mapping errors before modeling.

## Inputs
- Samples from `docs_extracted` (by doc_type, source)
- Validation rules (schema adherence, sentiment bounds, ticker confidence)
- Feature summaries from `features_daily`

## Outputs
- QA findings and issue list
- Corrections or exclusions applied to bad rows
- `pipeline_runs` entry for stage=qa_outputs

## Tools/Scripts (links to execution scripts)
- [[20_EXECUTION/qa_outputs]]

## Edge cases
- Over-filtering that drops too many docs; monitor coverage
- Ambiguous tickers or low-confidence mappings; flag for manual review
- Schema/version drift; ensure QA rules match current schema

## Run steps
1. Sample extractions across sources/types; validate against schema and bounds.
2. Spot-check sentiment/tone for obvious hallucinations.
3. Cross-check ticker mentions vs entities; adjust or drop low-confidence rows.
4. Update or mark `docs_extracted`/features for exclusion; log issues.
5. Feed findings into directives and extraction prompts.

## Learnings / Updates
- 
