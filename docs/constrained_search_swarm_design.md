# Constrained Search Swarm Technical Design Documentation

## Summary
Add a new engineering design document at `docs/constrained_search_swarm_design.md`. The doc will explain the current serial constrained-search runtime, the target parallel swarm architecture, latency goals, component responsibilities, interfaces, failure modes, and implementation roadmap.

The design will explicitly state that Cognee is the retrieval substrate, not the native swarm/control-plane engine. The swarm layer will be implemented above Cognee using bounded async branch execution, catalog-driven fanout, and deterministic evidence assembly.

## Key Documentation Content
- Document current state:
  - `search_trace.py` runs a single serial `CogneeSearchStateMachine`.
  - `max_steps` is currently global, so fanout queries like “all marketplaces” exhaust the budget before branch evidence matures.
  - Cognee recall is already async-capable, but branch orchestration is not yet implemented.
- Document target architecture:
  - `QueryIntentCompiler`: turns natural language into structured intent.
  - `RuntimeScopeResolver`: resolves tenant/group/platform-account branches from resolver catalogs without hardcoded marketplace IDs.
  - `BranchScheduler`: runs branches with bounded concurrency and per-branch budgets.
  - `BranchRunner`: resolves one branch from platform account to bindings, tables, columns, query patterns, and metric evidence.
  - `EvidenceAssembler`: merges branch outputs into one normalized evidence pack.
  - `TerminalValidator`: decides complete vs blocked/partial using branch coverage.
  - `SQLHandoffWriter`: emits final handoff from the validated evidence pack.
- Include Mermaid sequence diagrams:
  - Current serial flow.
  - Target swarm flow.
  - Branch execution and fan-in flow.
- Define latency target:
  - Interactive target: P50 under 60s, P90 around 90s.
  - Default v1 controls: `max_parallel_branches=5`, `branch_max_steps=4`, `recall_concurrency=6`, `llm_concurrency=2`, `global_timeout_seconds=90`, `soft_timeout_seconds=70`.
  - Emphasize no per-branch LLM calls in the common path.

## Interfaces And Behavior
- CLI additions to document for future implementation:
  - `--execution-mode serial|swarm`, default `serial` for compatibility.
  - `--branch-max-steps`, `--max-parallel-branches`, `--recall-concurrency`, `--llm-concurrency`.
  - `--global-timeout-seconds`, `--soft-timeout-seconds`.
- Internal model additions to document:
  - `QueryIntent`: analysis type, target entity, metric candidates, source-role preferences, scope.
  - `FanoutPlan`: fanout reason, branch list, budgets, global constraints.
  - `BranchScope`: tenant/group/platform/account/dataset routing.
  - `BranchEvidence`: bindings, tables, semantic cards, status, errors, latency.
  - `SwarmEvidencePack`: merged evidence, branch coverage, final readiness.
- Terminal behavior:
  - Strict default: complete only when every resolved in-scope branch has required sales evidence.
  - If some branches fail or lack evidence, return `blocked_with_partial_evidence` with branch-level reasons.
  - Never silently drop a marketplace branch from an “all marketplaces” query.

## Test Plan
- Unit tests:
  - Catalog-driven fanout returns platform accounts for tenant/group with no hardcoded platform names.
  - Branch budgets are per branch, while global timeout remains a safety fuse.
  - Evidence assembler dedupes canonical IDs and preserves branch lineage.
  - Terminal validator blocks when required branches are missing runtime bindings/table/query-pattern evidence.
- Integration tests:
  - Use the current Mensa marketplace query to verify swarm planning creates one branch per marketplace account.
  - Verify `--llm-dry-run --execution-mode swarm` produces a valid fanout plan without calling Cognee recall.
  - Verify live swarm search writes a trace containing `fanout_plan`, `branches`, `branch_status`, `evidence_pack`, and latency metrics.
- Acceptance criteria:
  - No hardcoded marketplace list.
  - Serial mode remains unchanged.
  - Swarm mode avoids global step exhaustion for 9-marketplace fanout.
  - Target query can either complete with full evidence or block with precise branch-level missing-evidence reasons.

## Assumptions
- Documentation-only change first; no runtime implementation in this step.
- v1 swarm uses bounded async tasks, not OS processes.
- Cognee remains the recall engine; resolver catalogs drive deterministic runtime scope resolution.
- The first implementation target is marketplace fanout, especially “top N selling SKUs across all marketplaces,” but the design should generalize to other fanout scopes later.

## Current Serial Flow

```mermaid
sequenceDiagram
    participant CLI as search_trace.py
    participant Env as runtime_env
    participant Catalog as CatalogBundle
    participant LLM as LLMPlane
    participant SM as Serial State Machine
    participant Cognee as CogneeClient
    participant SDK as cognee.recall
    participant Stores as Qdrant + Neo4j
    participant Handoff as SQL Handoff Writer

    CLI->>Env: load env + provider + pack-dir
    CLI->>Catalog: load resolver catalogs
    CLI->>LLM: extract_anchors(query, tenant/group)
    LLM-->>SM: initial search contracts

    SM->>SM: validate/coerce contracts
    SM->>SM: expand missing platform_id dynamically from catalog
    Note over SM: One pending queue<br/>One global max_steps

    loop while pending and steps < max_steps
        SM->>Cognee: execute next contract
        Cognee->>Catalog: route datasets
        Cognee->>SDK: recall(NodeSets, datasets)
        SDK->>Stores: graph/vector lookup
        Stores-->>SDK: context
        SDK-->>Cognee: recall result
        Cognee->>Catalog: normalize to canonical cards
        Cognee-->>SM: SearchResult

        SM->>SM: validate returned cards
        SM->>SM: check terminal evidence

        alt runtime cards found
            SM->>LLM: select runtime bindings
            LLM-->>SM: more contracts
        end

        SM->>LLM: plan next NodeSets
        LLM-->>SM: more contracts

        SM->>LLM: rank bounded candidates
        LLM-->>SM: more contracts

        SM->>SM: dedupe/prioritize pending queue
    end

    alt terminal evidence ready
        SM->>Handoff: write SQL handoff
        Handoff-->>CLI: complete
    else max_steps exhausted
        SM-->>CLI: blocked
    end
```

## Target Swarm Flow

```mermaid
sequenceDiagram
    participant CLI as search_trace.py
    participant Control as Search Control Plane
    participant Catalog as Resolver Catalog
    participant Planner as Anchor/Fanout Planner
    participant Scheduler as Branch Scheduler
    participant B1 as Branch: Amazon
    participant B2 as Branch: Flipkart
    participant BN as Branch: Other Marketplaces
    participant Cognee as Cognee Recall Layer
    participant Stores as Qdrant + Neo4j
    participant Assembler as Evidence Assembler
    participant Validator as Terminal Validator
    participant Handoff as SQL Handoff Writer

    CLI->>Control: run query
    Control->>Catalog: load pack catalogs
    Control->>Planner: extract anchors + fanout intent
    Planner->>Catalog: resolve marketplace platform accounts for tenant/group
    Catalog-->>Planner: N branch scopes
    Planner-->>Control: branch plan

    Control->>Scheduler: schedule branches
    Note over Scheduler: per-branch max_steps<br/>bounded concurrency<br/>global safety budget

    par branch execution
        Scheduler->>B1: run branch amazon
        B1->>Cognee: platform_account -> bindings -> table -> query patterns
        Cognee->>Stores: scoped recall
        Stores-->>Cognee: evidence
        Cognee-->>B1: canonical cards
        B1-->>Assembler: branch evidence
    and branch execution
        Scheduler->>B2: run branch flipkart
        B2->>Cognee: platform_account -> bindings -> table -> query patterns
        Cognee->>Stores: scoped recall
        Stores-->>Cognee: evidence
        Cognee-->>B2: canonical cards
        B2-->>Assembler: branch evidence
    and branch execution
        Scheduler->>BN: run remaining branches
        BN->>Cognee: same bounded branch search
        Cognee->>Stores: scoped recall
        Stores-->>Cognee: evidence
        Cognee-->>BN: canonical cards
        BN-->>Assembler: branch evidence
    end

    Assembler->>Assembler: dedupe canonical ids
    Assembler->>Assembler: mark branch status complete/partial/missing
    Assembler->>Validator: validate final evidence pack

    alt enough evidence
        Validator-->>Handoff: healthy cross-marketplace evidence pack
        Handoff-->>CLI: complete SQL/search handoff
    else gaps remain
        Validator-->>CLI: blocked with branch-level missing evidence
    end
```