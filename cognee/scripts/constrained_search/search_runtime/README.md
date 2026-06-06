# search_runtime

Cognee-facing constrained-search orchestration.

Runtime path:

```text
../search_trace.py
  -> search_runtime.search_trace
  -> search_runtime.cognee_client.CogneeClient
  -> search_runtime.llm_plane.LLMPlane
  -> search_runtime.search_state_machine.CogneeSearchStateMachine
  -> Cognee recall-context search
```

Traversal primitive:

```text
previous result -> LLM emits SearchContract.node_sets -> validator approves -> Cognee searches those NodeSets
```

The runtime does not perform local retrieval, local ranking, Cypher traversal, or source-role term expansion. Resolver catalogs are loaded from `<pack-dir>/resolver_catalog/` only to validate contracts, route datasets, and validate/enrich cards observed in Cognee output.

