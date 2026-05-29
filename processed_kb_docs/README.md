# Processed KB Docs

This directory contains the `raw/Source/cleaned` ingestion adapter and its cleaned
outputs.

Run:

```bash
.venv/bin/python processed_kb_docs/ingest_cleaned_v2.py
```

The adapter skips `raw/Source/cleaned/reference docs`, `.DS_Store`, and QA-only
validation reports. It parses structured Markdown YAML blocks and client JSON
runtime packs, then writes normalized JSONL files to `processed_kb_docs/cleaned`.
It uses `tqdm` progress bars when `tqdm` is installed in the active venv, and
falls back to simple stderr progress messages otherwise.

It also materializes review-friendly scoped folders:

- `cleaned/scoped/source_type/<source-folder>/<source-file>/`
- `cleaned/scoped/platform_type/<type>/<platform-or-source-system>/`

Within each scoped folder, cards are split by `cards/<card_type>.jsonl`; edges,
evidence, SQL patterns, reviews, and metadata are written as sidecar JSONL files.

Useful flags:

```bash
.venv/bin/python processed_kb_docs/ingest_cleaned_v2.py --no-progress
.venv/bin/python processed_kb_docs/ingest_cleaned_v2.py --log-file processed_kb_docs/cleaned/ingest.log
```

Outputs:

- `cards.jsonl`
- `edges.jsonl`
- `evidence.jsonl`
- `sql_patterns.jsonl`
- `review_items.jsonl`
- `documents.jsonl`
- `semantic_mappings.jsonl`
- `future_context_gaps.jsonl`
- `manifest.json`
- `ingest.log`
- `scoped/`
