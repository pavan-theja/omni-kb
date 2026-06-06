# Constrained Search Build

Build-only constrained-search scaffold for `raw/Source/refactored_v2`.

This directory is intentionally limited to generated build artifacts and the
local `kb_pipeline/` needed to produce them. It does not add runtime packages
under `src/` and does not add operator/runtime scaffolding under `cognee/`.

## Source

```text
raw/Source/refactored_v2/
```

Layer policy:

```text
client/          -> runtime
marketplaces/    -> reusable semantic
logistics/       -> reusable semantic
oms/             -> reusable semantic
wms/             -> reusable semantic
bank/            -> reusable semantic
payment_gateway/ -> reusable semantic
```

## Output

```text
build/constrained_search/build/
  cards.jsonl
  edges.jsonl
  pack_manifest.json
  parse_errors.json
  resolver_catalog/
  cognee_docs/cards/
  cognee_ingestion/
  readiness/
```

`resolver_catalog/` is read-only runtime support for validating future Cognee
NodeSet contracts. It is not a local retrieval engine.

`readiness/` is the build readiness pack. It summarizes whether the generated
Cognee add/cognify pack is structurally ready, whether the authored contracts
validate cleanly, and which runtime bindings remain blocked by missing scope
columns.

## Build

`build_refactored_v2.py` is a thin CLI wrapper. The build implementation lives
under `kb_pipeline/`:

```text
kb_pipeline/
  markdown_parser.py
  normalizer.py
  validator.py
  render_docs.py
  catalog_builder.py
  ingestion_batches.py
  readiness.py
  slice_profiles.py
  build_pipeline.py
```

Use the repo root virtualenv:

```bash
.venv/bin/python build/constrained_search/build_refactored_v2.py --clean
```

The generator only reads `raw/Source/refactored_v2` and writes under
`build/constrained_search/build`.

For the constrained-search ingestion trial, build only the marketplace runtime
slice:

```bash
.venv/bin/python build/constrained_search/build_refactored_v2.py --profile marketplace_runtime --clean
```

That writes a separate pack under:

```text
build/constrained_search/build_marketplace_runtime/
```

The profile keeps Amazon, Flipkart, Myntra, Nykaa, and Meesho marketplace
semantic cards, shared marketplace semantic cards, selected marketplace
client-runtime cards, their runtime owner cards, and table-local semantic
dependencies referenced by those runtime bindings.
