# Omni KB

Omni KB is the canonical knowledge-base pipeline for ZenStatement reconciliation knowledge.

The project takes structured raw KB documents, turns them into canonical cards and edges, loads those artifacts into Cognee, and then runs Cognee search / SQL-handoff evaluation batches.

Cognee is the only retrieval runtime for this repo. Local graph DB and LanceDB paths were removed.

## Pipeline

```text
raw/Source/cleaned/
  -> zenkb extract
  -> processed_kb_docs/cleaned/ + build/intermediate/
  -> zenkb promote
  -> canonical/
  -> cognee/scripts/cognee_ingest_simple.py
  -> cognee/shaped_export/
  -> local Cognee runtime
  -> cognee/scripts/cognee_search.py
  -> cognee/scripts/cognee_sql_handoff.py
  -> eval_runs/
```

## Directory Map

```text
raw/Source/cleaned/        Human-authored structured KB source docs.
processed_kb_docs/         Raw KB parser and normalized parser outputs.
build/chunks/              Optional generated semantic chunks; not Cognee runtime.
build/intermediate/        Temporary candidate cards/edges for promotion.
canonical/                 Canonical cards, edges, per-card JSON, and manifest.
cognee/                    Cognee Docker/runtime scripts, prompts, and generated ingest packs.
cognee/shaped_export/      Generated Cognee markdown packs from canonical artifacts.
cognee/query_outputs/      Local single-query debug outputs.
eval_runs/                 Batch search and SQL-handoff runners plus saved eval outputs.
src/zenkb/                 Python package and `zenkb` CLI.
tests/                     Regression tests.
```

Generated runtime/output folders are ignored where appropriate. Placeholder `README.md` files keep those folders visible.

## Setup

```bash
python3 -m venv .venv
source .venv/bin/activate
python -m pip install -e .
```

The core KB pipeline uses local files and the Python standard library. Cognee itself runs separately through Docker Compose.

## 1. Parse Raw KB Source

Use `zenkb extract` as the normal entrypoint.

```bash
source .venv/bin/activate
zenkb extract
```

This calls the raw KB parser:

```text
processed_kb_docs/ingest_cleaned_v2.py
```

It reads:

```text
raw/Source/cleaned/
```

It writes normalized parser outputs:

```text
processed_kb_docs/cleaned/cards.jsonl
processed_kb_docs/cleaned/edges.jsonl
processed_kb_docs/cleaned/evidence.jsonl
processed_kb_docs/cleaned/sql_patterns.jsonl
processed_kb_docs/cleaned/review_items.jsonl
processed_kb_docs/cleaned/manifest.json
```

It also writes promotion inputs:

```text
build/intermediate/candidate_cards.jsonl
build/intermediate/candidate_edges.jsonl
build/intermediate/review_items.jsonl
```

Use the parser directly only when debugging parser behavior:

```bash
python processed_kb_docs/ingest_cleaned_v2.py \
  --source-dir raw/Source/cleaned \
  --output-dir processed_kb_docs/cleaned
```

## 2. Promote Candidates To Canonical

Promotion turns parser candidates into stable canonical artifacts.

```bash
source .venv/bin/activate
zenkb promote
```

It reads:

```text
build/intermediate/candidate_cards.jsonl
build/intermediate/candidate_edges.jsonl
build/intermediate/review_items.jsonl
```

It writes:

```text
canonical/cards.jsonl
canonical/edges.jsonl
canonical/cards/<card_type>/*.json
canonical/manifest.json
```

Validate the canonical artifacts:

```bash
zenkb validate \
  --cards canonical/cards.jsonl \
  --edges canonical/edges.jsonl
```

`canonical/` is the source of truth for Cognee ingestion and SQL handoff.

Optional one-document-per-card export:

```bash
zenkb export-cognee
```

This writes `cognee/export/`. The main ingest path below uses shaped packs instead.

## 3. Configure Cognee

Create a local Cognee env file:

```bash
cp cognee/.env.example cognee/.env
```

Edit `cognee/.env` with the provider credentials you want to use.

Default Azure shape:

```text
COGNEE_LLM_PROVIDER=azure
COGNEE_EMBEDDING_PROVIDER=azure
AZURE_API_BASE=
AZURE_API_KEY=
AZURE_API_VERSION=
AZURE_OPENAI_DEPLOYMENT=gpt-4o-mini
AZURE_OPENAI_EMBEDDING_DEPLOYMENT=text-embedding-3-small
```

Start Cognee:

```bash
cognee/scripts/cognee_up.sh
```

Check health:

```bash
cognee/scripts/cognee_health.sh
```

Cognee should be available at:

```text
http://localhost:8000
http://localhost:8000/docs
```

Local Cognee runtime state is ignored:

```text
cognee/runtime/
.chromadb_data/
cognee/.env
```

## 4. Shape And Ingest Canonical KB Into Cognee

Use the simple Cognee ingest flow as the main path.

```bash
source .venv/bin/activate
python cognee/scripts/cognee_ingest_simple.py
```

This script does three things:

```text
canonical/cards.jsonl + canonical/edges.jsonl
  -> cognee/shaped_export/documents/canonical_pack_*.md
  -> Cognee /api/v1/add
  -> Cognee /api/v1/cognify
```

The shaped export keeps whole canonical cards together and splits documents into manageable packs for Cognee.

To only generate the markdown packs without calling Cognee:

```bash
python cognee/scripts/cognee_ingest_simple.py --shape-only
```

To reuse already-shaped packs:

```bash
python cognee/scripts/cognee_ingest_simple.py --skip-shape
```

For large runs, process Cognee cognify in batches:

```bash
python cognee/scripts/cognee_ingest_simple.py \
  --cognify-dataset-size 50 \
  --cognify-scope separate-datasets
```

`processed_kb_docs/dump_canonical_bundles.py` is an older alternate export helper that creates fewer large bundle files under `cognee/bundled_export/`. Prefer `cognee_ingest_simple.py` unless you are intentionally testing bundled ingestion.

## 5. Run A Single Cognee Search

Use `cognee_search.py` for direct Cognee search debugging.

```bash
python cognee/scripts/cognee_search.py \
  --dataset zenstatement_canonical \
  --search-type RAG_COMPLETION \
  "Which channel has the highest order volume share?"
```

Run every search type exposed by the helper:

```bash
python cognee/scripts/cognee_search.py \
  --dataset zenstatement_canonical \
  --both \
  "Generate a courier-wise channel mapping report."
```

Add scope when needed:

```bash
python cognee/scripts/cognee_search.py \
  --tenant tenant.prism_fashion \
  --platform platform.amazon \
  "Gross sales trend across all marketplaces."
```

## 6. Run A Single SQL Handoff

Use `cognee_sql_handoff.py` when you want the staged SQL-planning output for one question.

```bash
python cognee/scripts/cognee_sql_handoff.py \
  --dataset zenstatement_canonical \
  --output cognee/query_outputs/amazon_gmv_handoff.json \
  --markdown-output cognee/query_outputs/amazon_gmv_handoff.md \
  "Amazon gross sales GMV SQL"
```

The SQL handoff flow uses Cognee for context discovery and staged reasoning. It returns:

```text
raw_intent
grounded_intent
source_resolution
field_join_resolution
sql_handoff
validation
```

## 7. Run Batch Search Evaluations

Batch runners live in:

```text
eval_runs/
```

Use `eval_runs/cognee_batch_search.py` for plain Cognee search batches.

```bash
python eval_runs/cognee_batch_search.py \
  --dataset zenstatement_canonical \
  --search-type RAG_COMPLETION \
  --output-dir eval_runs/gemini25/test7_search
```

Run every search type exposed by the batch helper:

```bash
python eval_runs/cognee_batch_search.py \
  --dataset zenstatement_canonical \
  --both \
  --output-dir eval_runs/gemini25/test7_search_both
```

Pass a custom question file:

```bash
python eval_runs/cognee_batch_search.py \
  --questions eval_runs/questions.txt \
  --dataset zenstatement_canonical \
  --output-dir eval_runs/gemini25/test7_custom_questions
```

Question files can be `.txt`, `.json`, or `.jsonl`.

Each batch run writes:

```text
eval_runs/<run_name>/index.json
eval_runs/<run_name>/all_results.md
eval_runs/<run_name>/<question>.json
eval_runs/<run_name>/<question>.md
```

## 8. Run Batch SQL-Handoff Evaluations

Use `eval_runs/cognee_sql_handoff_batch.py` for staged SQL-handoff batches.

```bash
python eval_runs/cognee_sql_handoff_batch.py \
  --dataset zenstatement_canonical \
  --search-type RAG_COMPLETION \
  --output-dir eval_runs/gemini25/test7_sql_handoff
```

Run both discovery modes:

```bash
python eval_runs/cognee_sql_handoff_batch.py \
  --dataset zenstatement_canonical \
  --both \
  --output-dir eval_runs/gemini25/test7_sql_handoff_both
```

Add scope for tenant/platform-specific evals:

```bash
python eval_runs/cognee_sql_handoff_batch.py \
  --dataset zenstatement_canonical \
  --tenant tenant.prism_fashion \
  --platform platform.amazon \
  --output-dir eval_runs/gemini25/test7_prism_amazon_handoff
```

Each handoff batch writes the same result shape:

```text
index.json
all_results.md
per-question .json files
per-question .md files
```

## 9. Stop Or Reset Cognee

Stop Cognee without deleting runtime state:

```bash
cognee/scripts/cognee_down.sh
```

Reset local Cognee runtime state:

```bash
cognee/scripts/cognee_reset.sh
```

## Common Commands

Run tests:

```bash
PYTHONPATH=src python3 -m unittest discover tests
```

Show the CLI:

```bash
PYTHONPATH=src python3 -m zenkb --help
```

## What To Commit

Commit:

```text
raw/Source/cleaned/
processed_kb_docs/
canonical/
cognee/
eval_runs/ runners and selected reviewed outputs
src/
tests/
docs/
```

Do not commit:

```text
.venv/
cognee/runtime/
cognee/.env
raw/saved_stage/
generated Cognee export contents
generated local query/debug outputs
```

This repo does not use Git LFS. Large runtime artifacts should stay ignored and be recreated locally.
