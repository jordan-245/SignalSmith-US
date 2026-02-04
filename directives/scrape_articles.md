# Scrape Articles (HTML → readable text)

## Goal
Fetch a news article HTML page, extract the main content, and store it in Supabase as a document.

## Scope / Safety
- Do **not** bypass paywalls or logins.
- Default to **allowlisted sources** (RSS list). Ad-hoc URLs are allowed but should remain manual and low-volume.
- Rate limits: keep requests low per domain (handled in `execution/ingest_docs.py` retry/backoff).

## Tools
- `execution/ingest_docs.py` — fetch+clean+store (uses readability-lxml when installed)
- `execution/ingest_rss.py` — discovers URLs from RSS and hands off to ingest_docs

## Ad-hoc scrape (manual)
```bash
cd /srv/signalsmith/SignalSmith-US
source .venv/bin/activate
python execution/ingest_docs.py --url "https://example.com/article" --max-docs 1
```

## RSS-driven ingest
1) Add feeds to `directives/rss_sources.txt`
2) Run:
```bash
cd /srv/signalsmith/SignalSmith-US
source .venv/bin/activate
python execution/ingest_rss.py --feeds-file directives/rss_sources.txt --max-items 50
```

## Data model expectations
This uses existing Supabase tables referenced by `ingest_docs.py`:
- `docs_raw`
- `docs_text`
