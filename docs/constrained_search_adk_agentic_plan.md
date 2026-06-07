# Constrained Search ADK Agentic Plan

## Summary
The constrained-search runtime should become an agentic control plane without giving up the safety of NodeSet constraints. Cognee remains the KB recall engine. The agentic layer sits above it and runs the search as a fixed sequence of bounded skills and tools: resolve runtime scope, select sources, select domains, finalize legal tables, select evidence profiles, fetch profile evidence in parallel, then assemble the handoff.

This is not a free-form tool loop. Every LLM decision chooses from candidates returned by Cognee/catalog lookup, and every tool call emits validated `SearchContract` / `SearchResult` artifacts.

## Architecture
- **Skills** are coarse capabilities: runtime scope resolution, domain/table resolution, evidence profile selection, evidence sufficiency, and SQL handoff preparation.
- **Tools** are typed wrappers over existing constrained-search functions: contract repair/validation, Cognee recall, platform/domain/table selection, binding verification, evidence manifest creation, profile contract generation, evidence pack assembly, and handoff writing.
- **Sequential runner** owns the mandatory order: tenant/group scope -> platforms -> bindings -> domains -> tables -> evidence profile plan -> handoff.
- **Parallel runner** starts only after table finalization, where independent table/profile/card-type evidence contracts can be fetched safely in parallel.
- **Trace ledger** remains the source of truth. Branch status, missing evidence, chosen profiles, timings, and handoff output must remain inspectable in `last_search_trace.json` and eval artifacts.

## Skill And Tool Registry
- `query_anchor_skill`: sequential `extract_anchors`.
- `contract_execution_skill`: sequential `execute_contract`.
- `route_selection_skill`: sequential `select_runtime_bindings`, `plan_next_nodesets`, and `rank_bounded_candidates`.
- `evidence_profile_skill`: sequential `select_evidence_profiles`.
- `profile_evidence_fanout_skill`: parallel `execute_profile_evidence_contract`.
- `handoff_skill`: sequential `write_sql_handoff`.

Each ADK trace records `skill_id`, `tool_name`, `runner`, latency, and contract ID where applicable.

## Implementation Shape
- Keep `search_trace.py` default behavior as the existing serialized runtime.
- Add `--orchestrator serial|adk`, defaulting to `serial`.
- Add `--evidence-concurrency N` for the ADK/agentic evidence fanout lane.
- Add an agentic runtime class that reuses the current state-machine route selection but changes post-table behavior:
  - table selection remains sequential and constrained;
  - evidence profile contracts are generated from the manifest;
  - profile evidence contracts execute with bounded parallelism;
  - profile evidence results do not trigger the legacy planner/ranker again.
- Update eval metrics so evidence-profile LLM calls and ADK runner events are visible.

## Guardrails
- No hardcoded marketplaces, platforms, source roles, domains, or tables.
- Do not bypass account binding verification after table selection.
- Do not let profile evidence contracts spawn open-ended follow-up searches.
- Do not silently drop branches. Incomplete branches must surface as partial/best-effort warnings or blocked reasons.
- Keep serial mode compatible so live regressions can be bisected against the previous path.

## Acceptance Tests
- `--orchestrator serial` remains compatible with current tests.
- `--orchestrator adk` runs a live search through the same CLI.
- Profile evidence contracts execute through a parallel runner and produce trace events with contract IDs, concurrency, and result counts.
- Profile evidence contracts do not call `plan_next_nodesets` or `rank_bounded_candidates` afterward.
- Eval output under `eval_runs/constrained_search` includes orchestrator and evidence-concurrency metadata.
- Eval metrics include ADK sequential tool count, parallel evidence run count, parallel tool count, evidence contract count, and evidence failure count.

## Rollout
Start with the agentic evidence fanout lane only. Once this is stable, the next step is to move platform/domain/table branches into a true ADK swarm with per-branch budgets and fan-in assembly.
