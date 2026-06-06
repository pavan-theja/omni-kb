# Serialized Constrained Search Hardening Plan

## Summary

This document specifies the next engineering step for constrained search: make the
serialized flow reliable before building the parallel swarm approach.

The current serialized search loop is useful but too fragile for broad runtime
fanout queries. It can spend the global step budget on first-layer platform
account discovery, accepts too much LLM variability, and does not yet produce
branch-level completion or missing-evidence reporting. The goal of this plan is
to harden the serial path while keeping the current LLM-driven next-step
planning model.

Dry-run checks are only pre-flight validation. Live end-to-end evals against the
populated Cognee dataset are the real acceptance gate.

## Goals

- Keep the serialized search flow as the active implementation path.
- Keep LLM-driven next-step planning for now.
- Repair common LLM contract mistakes before validation.
- Validate repaired contracts strictly against resolver catalogs.
- Track runtime-source branch lineage in the serial queue.
- Support runtime-source fanout beyond marketplaces, including OMS, WMS,
  logistics, bank/bank_statement, payment gateway, and manual/CSV operational
  sources when represented in the pack.
- Use best-effort completion by default:
  - Return usable evidence and handoff when at least one branch is complete.
  - Report incomplete branches as warnings.
  - Block only when no branch has enough evidence for handoff.
- Store live eval results under `eval_runs/constrained_search`.

## Non-Goals

- Do not implement swarm/parallel branch execution yet.
- Do not introduce OS processes for branch execution.
- Do not hardcode marketplace, platform, courier, bank, OMS, or payment-gateway
  lists in the search runtime.
- Do not treat dry-run or LLM dry-run as proof that search works end to end.

## Current State

The current constrained-search runtime is a single serialized loop:

1. `search_trace.py` loads the pack, env, catalogs, LLM provider, and Cognee
   client.
2. `CogneeSearchStateMachine` asks the LLM anchor extractor for initial
   `SearchContract` objects.
3. The runtime validates contracts against `resolver_catalog`.
4. The runtime executes one contract at a time through `CogneeClient.search`,
   which calls Cognee recall with NodeSet filters.
5. After every result, the runtime asks LLM planner/ranker prompts for next
   contracts.
6. Terminal evidence is checked globally.
7. If the global `--max-steps` budget is exhausted before evidence is ready, the
   run blocks.

This breaks down on wide fanout queries. For example, a query like "Top 5
selling SKUs across all marketplaces" can discover many runtime source branches.
The current global queue can spend all steps on platform account discovery before
it reaches account bindings, tables, query patterns, or SQL handoff evidence.

## Target Serialized Flow

The target remains serial, but it becomes branch-aware and repair-first:

```text
query
  -> LLM anchor contracts
  -> contract repair
  -> strict validation
  -> branch-aware serial queue
  -> Cognee recall
  -> returned-card validation
  -> branch ledger update
  -> LLM next-step planning
  -> contract repair
  -> strict validation
  -> repeat until best-effort terminal evidence or global safety budget
```

### Runtime Source Branch

A runtime branch represents one scoped path through the client's configured
runtime sources. It is not marketplace-specific.

Branch identity should be derived from the strongest available scope keys:

- `tenant_id`
- `group_id`
- `runtime_source_family`
- `platform_id`
- `platform_context_id`
- `platform_account_id`
- `account_data_binding_id`
- `source_role`
- `table_id`

Examples of runtime source branches:

- Amazon marketplace account to OMS sales binding.
- Shopify/own website OMS binding.
- Unicommerce WMS binding.
- Delhivery or Xpressbees logistics binding.
- Razorpay or Cashfree payment-gateway settlement binding.
- HDFC/Axis/IDFC bank statement binding.
- Manual CSV operational source binding.

### Branch Ledger

Add a branch ledger to the serial state machine. The ledger records branch
identity, evidence collected, status, and missing evidence.

Recommended branch status values:

- `pending`: branch discovered but not searched deeply.
- `in_progress`: at least one contract executed for the branch.
- `usable`: enough evidence exists for handoff under best-effort policy.
- `partial`: some evidence exists but required handoff evidence is missing.
- `blocked`: a branch-specific blocker was found.
- `failed`: contract execution or validation failed in a non-repairable way.

Each branch should track:

- platform account cards
- account data binding cards
- table cards
- column cards
- query pattern cards
- metric implementation cards
- contract repairs
- contract rejections
- warnings
- blocked reasons
- executed step count

### Branch-Aware Serial Scheduling

Replace flat queue behavior with branch-aware ordering while still executing one
contract at a time.

Scheduling rules:

- Do not let first-layer fanout consume the whole global step budget.
- Prefer deepening a branch to usable evidence once a branch has a runtime
  binding candidate.
- Rotate across branches so broad queries do not starve later branches.
- Deduplicate by contract signature.
- Preserve predecessor/carry-forward lineage.
- Cap pending queue size with `--max-pending`.

`--max-steps` remains a global safety fuse. It should not be treated as the only
meaningful progress budget for fanout. Use `--branch-max-steps` to prevent any
single branch from consuming the run.

## Contract Repair And Strict Validation

LLM output remains part of the flow, but it must pass through a repair layer
before validation. The repair layer should make safe, deterministic corrections
only when the intended contract is unambiguous.

### Repair Rules

The repair layer should support:

- Stage alias repair:
  - Convert `runtime_account_data_binding_search` to
    `runtime_account_binding_search`.
  - Reject unsupported stage names after alias repair.
- Missing `card_type` NodeSet repair:
  - If `allowed_card_types` has exactly one type and the stage template expects
    the same type, add `card_type:<type>`.
  - Reject if multiple allowed card types exist or the type conflicts with the
    stage template.
- Canonical NodeSet repair:
  - Use `CatalogBundle.canonicalize_node_set` for aliases.
  - Do not hardcode platform names.
- Carry-forward repair:
  - Fill unambiguous `tenant_id`, `group_id`, `platform_account_id`,
    `account_data_binding_id`, `source_role`, and `table_id` from predecessor
    cards or current branch state.
  - Reject if more than one value is possible.
- Runtime branch expansion:
  - If a runtime platform-account search is missing `platform_id`, expand it
    using catalog-discovered runtime source scope for the tenant/group.
  - This expansion must support all runtime source families present in catalogs,
    not just marketplaces.

Every repair must be recorded in the trace. Every rejected contract must include
a rejection reason and the source LLM event.

### Validation Rules

After repair, validation should be strict:

- Unknown stages are errors.
- Missing template-required NodeSet keys are errors.
- Unknown NodeSets are errors.
- Unknown table IDs are errors.
- Returned cards must contain the contract's required NodeSets.
- Returned card type must match `allowed_card_types`.
- Catalog-authored NodeSets must match returned card claims.

Warnings are acceptable only for non-blocking metadata issues. Invalid search
boundaries must not be executed.

## Completion Policy

Default completion policy: `best_effort`.

Under best-effort:

- If one or more branches are usable, the run can return a best-effort result.
- Incomplete branches must be included as warnings.
- The handoff must only use validated evidence from usable branches.
- The handoff must not silently drop branches.
- If no branch is usable, the run returns `blocked`.

Recommended output status values:

- `complete`: all required branches have usable evidence.
- `best_effort`: at least one branch is usable, but some branches are missing or
  incomplete.
- `partial`: evidence exists, but a final handoff cannot be safely written.
- `blocked`: no usable branch exists or required global evidence is absent.

## CLI And Config Changes

Add these options to the constrained-search runtime:

```text
--branch-max-steps
  Default: 8
  Maximum number of executed contracts allowed per branch.

--max-pending
  Default: 32
  Maximum number of queued contracts after repair/deduplication.

--completion-policy strict|partial|best_effort
  Default: best_effort
  Controls final status when some branches are incomplete.

--eval-output-dir
  Default: eval_runs/constrained_search
  Root directory for live E2E eval artifacts.
```

Existing options remain:

- `--max-steps`: global safety budget.
- `--dry-run`: pack/env/prompt pre-flight only.
- `--llm-dry-run`: LLM contract generation and repair/validation pre-flight only.
- `--pack-dir`
- `--env-file`
- `--provider`
- `--tenant-id`
- `--group-id`
- `--dataset`
- `--all-datasets`

## Trace Additions

Extend `traces/last_search_trace.json` with:

- `branches`
- `branch_status`
- `branch_order`
- `branch_step_counts`
- `contract_repairs`
- `contract_rejections`
- `best_effort_warnings`
- `usable_branch_count`
- `incomplete_branch_count`
- `completion_policy`
- `global_step_count`
- `recall_count`
- `llm_call_count`

The trace must make it obvious why a run completed, returned best effort, or
blocked.

## Live E2E Eval Strategy

Dry-run tests are not evals. They only catch wiring and contract-shape problems
early. The real acceptance gate is live end-to-end execution:

```text
LLM planning
  -> contract repair
  -> strict validation
  -> Cognee recall
  -> returned-card validation
  -> branch evidence tracking
  -> handoff or blocked/best-effort result
  -> persisted artifacts
```

### Eval Output Location

Store every eval run under:

```text
eval_runs/constrained_search
```

Recommended layout:

```text
eval_runs/constrained_search/
  <run_id>/
    manifest.json
    summary.md
    aggregate_metrics.json
    queries/
      001/
        query.txt
        result.json
        trace.json
        stdout.log
        stderr.log
        metrics.json
        summary.md
      002/
        ...
```

### Per-Query Metrics

Capture at least:

- query text
- status
- completion policy
- handoff status
- total latency
- LLM call count
- Cognee recall count
- contract repair count
- contract rejection count
- global step count
- usable branch count
- incomplete branch count
- selected runtime bindings
- selected tables
- selected query patterns
- selected metric implementations
- warnings
- blocked reasons

## Eval Query Set

Run these as live E2E evals:

1. `Top 5 selling SKUs across all marketplaces.`
2. `Amazon settlement cash position for this group.`
3. `Payment gateway settlement status for this group.`
4. `Bank statement cash movement for this group.`
5. `WMS shipment/order fulfilment status for this group.`
6. `Logistics settlement or COD reconciliation for this group.`
7. `OMS sales and returns summary for this group.`
8. `Which channel has the highest order volume share?`
9. `Generate a report of all channels using Manual CSV integration.`
10. `List all marketplaces handled through Unicommerce.`
11. `Generate a courier-wise channel mapping report.`
12. `Which courier handles the own website shipments?`
13. `Generate a report showing COD remittance type by courier.`
14. `Which channels use marketplace-managed returns?`
15. `Generate a summary report of OMS systems and their connected marketplaces.`
16. `Calculate the combined marketplace contribution vs own website contribution.`
17. `Identify channels with higher operational dependency on manual processes.`
18. `Create a marketplace risk report showing which channels depend on the same OMS.`
19. `Generate a logistics dependency matrix showing courier concentration across marketplaces.`
20. `Build a report identifying channels that may face reconciliation delays due to marketplace-based settlements.`
21. `Compare return handling models between own website and marketplace channels.`
22. `Generate a report showing potential operational bottlenecks if Unicommerce becomes unavailable.`
23. `Create a sales concentration analysis report to determine dependency on top 2 marketplaces.`
24. `Generate a unified dashboard combining sales, OMS dependency, courier dependency, and return ownership.`
25. `Design a profitability analysis report estimating operational complexity cost per marketplace.`
26. `Build a SKU profitability report.`
27. `Build an Average order value report per channel.`
28. `Gross sales trend across all marketplaces.`
29. `Return trend across all the marketplaces.`

Not every query is expected to produce a `complete` result. Some queries may
correctly return `best_effort`, `partial`, or `blocked` if the pack does not
contain the required profitability assumptions, operational cost model, source
bindings, columns, or query patterns. Correct missing-evidence reporting is a
valid outcome.

## Test Plan

### Unit Tests

- Contract repair:
  - illegal stage alias repair
  - missing `card_type` repair
  - canonical NodeSet repair
  - ambiguous carry-forward rejection
  - unknown stage rejection after repair
- Validation:
  - template-required NodeSet enforcement
  - unknown NodeSet rejection
  - returned-card NodeSet validation
  - returned-card type validation
- Branch scheduling:
  - branch ledger creation
  - branch step accounting
  - branch-aware queue ordering
  - max pending enforcement
  - best-effort completion with partial branch coverage
- Evidence:
  - branch-level runtime binding detection
  - table/query-pattern evidence detection
  - incomplete branch warning generation

### Pre-Flight Checks

- `--dry-run` validates pack/env/prompt wiring only.
- `--llm-dry-run` validates LLM contract generation, repair, and validation only.
- Neither pre-flight mode is an E2E eval.

### Live E2E Evals

- Execute every eval query against the populated Cognee dataset.
- Persist all artifacts under `eval_runs/constrained_search`.
- Treat live eval results as the real acceptance gate.
- Fail the eval suite if:
  - runtime crashes
  - trace is missing
  - result artifact is missing
  - invalid contracts are executed
  - branches are silently dropped
  - zero actionable missing-evidence reasons are reported for blocked queries

## Implementation Phases

### Phase 1: Repair And Validation

- Add contract repair layer.
- Convert known stage aliases.
- Add deterministic `card_type` repair.
- Record repairs and rejections in trace.
- Make unknown stages errors after repair.

### Phase 2: Branch Ledger

- Add branch identity extraction from contracts and returned cards.
- Track branch evidence and branch step counts.
- Add branch statuses and missing-evidence reasons.

### Phase 3: Branch-Aware Serial Queue

- Replace flat pending prioritization with branch-aware ordering.
- Keep execution serial.
- Add `--branch-max-steps` and `--max-pending`.
- Keep `--max-steps` as global safety fuse.

### Phase 4: Best-Effort Completion

- Add `--completion-policy`.
- Build evidence pack only from validated usable branches.
- Emit warnings for incomplete branches.
- Block only when no usable branch exists.

### Phase 5: Live E2E Eval Runner

- Add eval runner that executes the query set live.
- Store artifacts under `eval_runs/constrained_search`.
- Generate per-query and aggregate summaries.

## Acceptance Criteria

- Serialized search does not execute invalid contracts.
- Contract repair handles common LLM mistakes and records every repair.
- Runtime source fanout is catalog-driven and not marketplace-only.
- Serial scheduling reaches deeper evidence instead of exhausting steps on
  first-layer fanout.
- Best-effort completion returns usable evidence with explicit incomplete-branch
  warnings.
- Live E2E eval artifacts are stored under `eval_runs/constrained_search`.
- Dry-run is documented and treated only as pre-flight.
- Swarm implementation remains out of scope until serial reliability is stable.
