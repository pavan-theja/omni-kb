# Cognee Runtime and Export

This directory owns everything needed to run the local Cognee instance and load
the canonical KB into it.

For the cleanup plan covering Docker boundaries and a unified ingestion script
for both current ingest commands, see
[`docs/cognee_docker_ingestion_refactor.md`](../docs/cognee_docker_ingestion_refactor.md).

```text
cognee/
  compose.yaml              # local Cognee Docker Compose stack
  .env.example              # Azure OpenAI settings template
  .env                      # local ignored secrets/config
  canonical_graph_model.json
  canonical_cognify_prompt.md
  export/                   # generated Cognee markdown export
  runtime/                  # ignored local Cognee runtime state
  scripts/                  # start, stop, reset, health, and ingest helpers
```

Typical vanilla flow:

```bash
source .venv/bin/activate
zenkb export-cognee
cognee/scripts/cognee_up.sh
cognee/scripts/cognee_ingest.py --mode full
```

Provider-specific startup:

```bash
cognee/scripts/cognee_up.sh \
  --env-file cognee/.env.vertex \
  --llm-provider vertex \
  --embedding-provider vertex

cognee/scripts/cognee_ingest_v2.py \
  --mode full \
  --llm-provider vertex \
  --embedding-provider vertex
```

The provider flags on `cognee_ingest.py` and `cognee_ingest_v2.py` validate
the running runtime configuration. The provider is actually applied when
`cognee/scripts/cognee_up.sh` prepares the generated runtime env and starts or
recreates the Docker service. Runtime DBs are isolated under
`cognee/runtime/instances/<runtime_key>/` so different provider/model
combinations do not share vectors or graph state.

For faster local population without letting one giant markdown file blur card
boundaries, use the simple shaped add path. It writes generated packs under
`cognee/shaped_export/documents`, keeping each complete card in one generated
file and targeting 6000 estimated tokens per pack. After add succeeds, the
script starts a simple background Cognify run for the same dataset:

```bash
cognee/scripts/cognee_ingest_simple.py --shape-only
cognee/scripts/cognee_ingest_simple.py
```

Use `--skip-cognify` when you only want to shape and add documents.

For a single-file bundle used mostly for inspection or experiments:

```bash
processed_kb_docs/dump_canonical_bundles.py
cognee/scripts/cognee_ingest.py \
  --mode full \
  --docs-dir cognee/bundled_export/documents
```

The bundled export keeps canonical IDs and explicit edge lists, but reduces the
upload surface from one file per card to one add-optimized bundle file by
default. For review-friendly card-type files, run:

```bash
processed_kb_docs/dump_canonical_bundles.py \
  --bundle-by card_type \
  --max-cards-per-file 500
```

Custom canonical-aware Cognify flow:

```bash
cognee/scripts/cognee_ingest_v2.py --mode full
```

`cognee/scripts/cognee_ingest_v2.py` uses the canonical graph model and Cognify
prompt by default. It also attempts to update the Cognee dataset schema before
starting Cognify. Override or disable that behavior with:

```bash
cognee/scripts/cognee_ingest_v2.py \
  --graph-model path/to/graph_model.json \
  --custom-prompt path/to/prompt.md

cognee/scripts/cognee_ingest_v2.py --skip-schema-update
```

Staged v2 flow:

```bash
cognee/scripts/cognee_ingest_v2.py \
  --mode staged \
  --stage build-embeddings

cognee/scripts/cognee_ingest_v2.py \
  --mode staged \
  --stage edge-cognify \
  --skip-add
```
