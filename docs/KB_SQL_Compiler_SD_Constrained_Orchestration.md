# ZenStatement KB SQL Compiler - Constrained Orchestration Scoping Design

**Document status:** Enriched copy / implementation scoping draft  
**Source spec:** `docs/KB_SQL_Compiler_SD.md`  
**Date:** 2026-05-29  
**Focus:** Repo changes and orchestration design for constraint-driven multi-step retrieval. This document deliberately narrows the original system design to the constrained retrieval and planning layer.

---

## 1. Executive summary

The base SQL compiler design already establishes the right architecture:

```text
canonicals -> semantic contracts -> runtime bindings -> query plan DAG -> SQL -> validation
```

This enriched copy focuses on the missing operational layer: **constrained orchestration**.

The orchestration layer should make retrieval behave like a compiler pipeline, not like a global top-k RAG call. Every stage should carry a structured constraint ledger that says what must be true, what must not be used, what is unresolved, and which retrieval class is allowed next.

Target flow:

```text
User question
  -> RequestEnvelope
  -> IntentIR
  -> ConstraintLedger
  -> ClassAwareRetrievalPlan
  -> CandidatePool
  -> ScopeResolution
  -> CapabilityMatrix
  -> ContractSelection
  -> JoinPathPlan
  -> QueryPlanDAG
  -> SQLContextPacket
  -> SQLArtifact or SafeFailurePacket
```

The key change is that Cognee remains the memory and discovery substrate, while deterministic repo code owns:

- scoping,
- candidate acceptance and rejection,
- runtime binding activation,
- contract selection,
- join path certification,
- blocked-plan behavior,
- traceability,
- SQL validation gates.

The current scripts already contain a useful prototype split:

- `src/zenkb/retrieval.py` builds a scoped SQL context bundle from canonical cards, edges, scope filters, and Cognee discovery.
- `cognee/scripts/cognee_sql_handoff.py` runs a staged prompt handoff: raw intent, discovery, grounded intent, source resolution, field/join resolution, SQL builder, and local validation.
- `cognee/skills/sql_handoff/*.md` contains prompt-stage boundaries that can be reused as LLM interpretation aids.

The next repo step is to formalize these into a first-class orchestration package with typed stage inputs/outputs and strict gates.

---

## 2. Design stance

### 2.1 What constrained orchestration means

Constraint-driven retrieval is not:

```text
question -> retrieve top-k chunks -> ask LLM for SQL
```

It is:

```text
question
  -> parse constraints
  -> retrieve only the evidence class needed by the current stage
  -> normalize candidate IDs
  -> apply hard gates
  -> issue targeted follow-up retrieval only for missing evidence
  -> assemble a compact SQL construction packet
```

Each stage is allowed to ask a narrower question than the user asked.

Example:

```text
User asks:
For Ardeur on Meesho, show brand-level GMV, returns, return logistics cost, and net revenue by month.

The orchestrator asks separate retrieval questions:
1. Which Ardeur Meesho platform account is active?
2. Which account_data_bindings bind that account to physical tables?
3. Which marketplace seller reconciliation roles are required?
4. Which Meesho contracts implement gross GMV, returns, return logistics cost, and net revenue?
5. Which certified relationship joins sales/reverse/settlement to brand?
6. Is brand-level allocation for return logistics certified?
```

The LLM can help interpret ambiguous business language, but deterministic code decides which evidence is executable.

### 2.2 Non-goals for this layer

This scope does not attempt to:

- redesign canonical authoring,
- replace Cognee,
- build a general autonomous SQL agent,
- make triplets the execution model,
- infer joins from column name similarity,
- produce production SQL when runtime scope or relationship contracts are missing,
- solve physical DB execution tuning.

The orchestration layer should output one of:

```text
validated SQL artifact
partial plan with limitations
blocked safe-failure packet
metadata inventory handoff
```

---

## 3. Current repo assets to build on

### 3.1 Existing source-of-truth artifacts

```text
canonical/cards.jsonl
canonical/edges.jsonl
canonical/manifest.json
canonical/cards/*
cognee/custom_shaped_export/documents/*
cognee/shaped_export/*
cognee/bundled_export/*
```

The orchestration layer should keep canonical cards and edges as the source of truth for card IDs, table IDs, relationships, metrics, rules, and runtime bindings.

### 3.2 Existing retrieval and Cognee runtime code

```text
src/zenkb/retrieval.py
src/zenkb/cognee_export.py
src/zenkb/canonical.py
src/zenkb/cognee_runtime/client.py
src/zenkb/cognee_runtime/ingestion.py
cognee/scripts/cognee_search.py
cognee/scripts/cognee_sql_handoff.py
cognee/scripts/sql_query_resolution_prompt.md
cognee/skills/sql_handoff/*.md
eval_runs/cognee_sql_handoff_batch.py
```

These pieces should not be discarded. The main change is to split orchestration concerns into explicit services rather than keeping them inside one long retrieval function or prompt script.

### 3.3 Current prototype behavior worth preserving

From `src/zenkb/retrieval.py`:

- scope resolution,
- Cognee candidate discovery,
- scoped graph expansion,
- SQL context grouping,
- completeness warnings,
- unsafe-for-SQL flags,
- handoff briefs.

From `cognee/scripts/cognee_sql_handoff.py`:

- pre-retrieval raw intent classification,
- staged prompting,
- `physical_sql` vs `metadata_inventory` vs `partial` routing,
- local validation that rejects SQL against canonical metadata,
- batch evaluation support.

The enriched design makes these behaviors typed, testable, and composable.

### 3.4 Observed failure mode: broad proxy beats settlement evidence

Recent full-context evaluation exposed an important arbitration failure.

Retrieval can successfully surface marketplace-specific settlement and reconciliation evidence, such as:

```text
metric implementations for overdue payment, amount pending settlement, and settlement velocity
business processes for marketplace order-to-settlement timing differences
settlement columns such as payment_date, settlement_date, payment_status
settlement amount and variance columns such as actual_settlement and differential_amount
```

But the final selection logic can still choose a single broad operational table, for example an order/WMS table, because the prompt over-rewards:

```text
one executable physical table
one broad cross-channel proxy
minimum viable alternative over null
```

That behavior is wrong for settlement-delay, payout, remittance, reconciliation, and marketplace-based settlement questions.

For those intents, the orchestrator must treat settlement/reconciliation evidence as the primary evidence family. A broad order or WMS table may be useful as supporting operational context, but it should not outrank a marketplace-specific settlement implementation merely because it covers more channels in one table.

Correct arbitration:

```text
1. Prefer domain-specific settlement/reconciliation tables and metric implementations.
2. If safe all-marketplace consolidation is not grounded, pick the best marketplace-specific settlement MVA.
3. If several marketplace-specific implementations are relevant, return a multi-section report plan rather than a weak broad proxy.
4. Use broad order/WMS/operations tables only as last-resort proxies.
5. Reject selected SQL if it uses fields not grounded for the selected physical table.
```

This is a design requirement, not only a prompt tweak.

---

## 4. Proposed repo additions

### 4.1 New package

Add a new package:

```text
src/zenkb/orchestration/
  __init__.py
  models.py
  constraints.py
  intent.py
  domain_router.py
  table_family_router.py
  retrieval_plan.py
  search_fanout.py
  search_agent.py
  cognee_discovery.py
  evidence_merger.py
  candidate_pool.py
  candidate_arbitrator.py
  scope_resolver.py
  runtime_resolver.py
  capability_matrix.py
  contract_selector.py
  join_path_planner.py
  dag_builder.py
  packet_assembler.py
  sql_compiler.py
  field_grounding.py
  validators.py
  repair.py
  trace.py
  cli.py
```

The package boundary should be:

```text
orchestration owns stage order, constraints, acceptance gates, and trace artifacts.
retrieval owns canonical/edge lookup and Cognee candidate discovery helpers.
cognee_runtime owns HTTP calls and ingestion/runtime client details.
canonical owns card and edge validation.
```

### 4.2 New contract outputs

Add generated execution-facing artifacts:

```text
canonical/contracts.jsonl
canonical/contract_edges.jsonl
canonical/platform_type_contexts.jsonl
canonical/runtime_capabilities.jsonl
build/orchestration/evidence_priority_profiles.json
build/orchestration/domain_route_index.json
build/orchestration/table_family_index.json
build/orchestration/contract_index.json
build/orchestration/table_role_index.json
build/orchestration/runtime_binding_index.json
build/orchestration/field_grounding_index.json
```

These can be generated incrementally. The first vertical slice can use only Meesho/Ardeur while preserving the final shape.

### 4.3 New Cognee exports

Add contract-aware Cognee exports:

```text
cognee/contract_shaped_export/
  documents/
  metadata.jsonl
  manifest.json

cognee/orchestration_graph_model.json
cognee/orchestration_cognify_prompt.md
```

The existing canonical export can remain. The contract-shaped export should optimize retrieval surfaces around execution use:

- table usage,
- column usage,
- metric implementations,
- relationships,
- runtime bindings,
- business flows,
- evidence priority profiles,
- rules,
- validation tests,
- output contracts.

### 4.4 New orchestration skills

Add a separate skill folder:

```text
cognee/skills/sql_orchestration/
  intent_parser.md
  ambiguity_resolver.md
  domain_evidence_router.md
  domain_search_agent.md
  table_search_agent.md
  evidence_merge_arbiter.md
  candidate_ranker.md
  blocked_plan_explainer.md
  repair_query_writer.md
```

These prompts should not own final selection. They should produce structured proposals that deterministic gates can accept or reject.

### 4.5 New scripts and eval harnesses

```text
cognee/scripts/cognee_sql_orchestrate.py
eval_runs/cognee_sql_orchestration_batch.py
eval_runs/fixtures/sql_orchestration_questions.jsonl
eval_runs/fixtures/sql_orchestration_expected.jsonl
```

The existing `cognee_sql_handoff.py` can remain as compatibility mode:

```text
prompt_handoff_mode: current script behavior
orchestrated_mode: new deterministic stage runner
```

---

## 5. Core data objects

### 5.1 RequestEnvelope

The request envelope captures the user question and explicit external scope.

```yaml
request_envelope:
  request_id: req_20260529_0001
  user_question: For Ardeur on Meesho, show brand-level GMV by month.
  explicit_scope:
    tenant: Ardeur Fashion Limited
    group: null
    platform: Meesho
    account: primary
  execution_mode: sql_or_metadata
  dialect_hint: athena_trino
  allow_partial_plan: true
  allow_metadata_inventory: true
  max_repair_rounds: 2
```

### 5.2 IntentIR

The intent IR should be produced before broad retrieval.

```yaml
intent_ir:
  answer_mode_hint: physical_sql
  domain_families:
    - marketplace_reconciliation
    - revenue
  requested_metrics:
    - gross_gmv
  dimensions:
    - month
    - brand
  filters:
    platform:
      - meesho
  output_grain:
    - month
    - brand
  domain_search_routes:
    - marketplace_reconciliation
    - settlement
  table_family_routes:
    - order_ledger
    - settlement_ledger
    - product_mapping
  required_roles:
    - order_ledger
    - product_mapping
  risk_flags:
    requires_runtime_scope: true
    requires_join_path: true
    requires_brand_enrichment: true
```

### 5.3 EvidencePriorityProfile

The evidence priority profile prevents a broad table from winning only because it is executable.

It is derived from intent terms, platform type, requested metric family, and retrieved candidate families.

For settlement-delay questions, the profile should look like:

```yaml
evidence_priority_profile:
  domain_intent: marketplace_settlement_delay
  trigger_terms:
    - marketplace-based settlements
    - settlement delay
    - overdue payment
    - pending settlement
    - remittance
    - payout
  primary_evidence_families:
    - settlement_ledger
    - reconciliation_profile
    - settlement_metric_implementation
    - payment_status_columns
    - settlement_date_columns
  adjacent_evidence_families:
    - order_ledger
    - oms_process
    - marketplace_account_binding
  last_resort_proxy_families:
    - wms_order_pipeline
    - broad_sales_order_fact
  primary_candidate_bonus:
    settlement_or_reconciliation_table: 200
    settlement_metric_implementation: 180
    payment_status_or_settlement_date_column: 120
  proxy_penalty:
    broad_order_table_for_settlement_delay: -250
    wms_table_for_marketplace_settlement: -300
```

Required arbitration behavior:

```text
If primary settlement/reconciliation candidates exist, do not select an adjacent or last-resort proxy unless every primary candidate is blocked.
If consolidation across marketplaces is unsafe, select marketplace-specific settlement MVAs or return a multi-section report plan.
If a proxy is selected, mark it weak and explain which primary evidence was missing or blocked.
```

### 5.4 ConstraintLedger

The constraint ledger is the central orchestration artifact.

```yaml
constraint_ledger:
  request_constraints:
    must_answer:
      - requested metric gross_gmv
      - output grain month, brand
    should_answer:
      - platform-specific Meesho semantics
    must_not_answer:
      - do not use another platform as proxy
      - do not query canonical metadata as business data

  scope_constraints:
    tenant_required: true
    platform_required: true
    runtime_scope_filters_required: true
    accepted_tenant_ids: []
    accepted_platform_account_ids: []

  retrieval_constraints:
    current_allowed_card_types:
      - tenant
      - group
      - platform_account
      - account_data_binding
    excluded_card_ids: []
    required_card_ids: []

  execution_constraints:
    required_runtime_bindings: []
    required_relationship_contracts: []
    required_validation_tests:
      - active_filter_present
      - runtime_scope_filter_present
      - no_undocumented_join

  unresolved_constraints:
    - tenant_id
    - platform_account_id
    - gross_gmv_metric_contract
    - brand_join_contract
```

Every stage reads the ledger and writes back:

```text
resolved constraints
new constraints
candidate evidence
rejected evidence
blocking gaps
```

### 5.5 SearchFanoutPlan

When one user request spans multiple domains or table families, the orchestrator should fan out into multiple logical search agents.

This is required for questions like:

```text
marketplace settlement delay risk by channel
profitability combining sales, returns, settlement, ads, and logistics
COD reconciliation across OMS, logistics, payment, and bank
inventory variance across WMS, marketplace, and customer-order inventory
```

The fan-out plan should be explicit:

```yaml
search_fanout_plan:
  fanout_id: fanout.req_20260529_0001
  strategy: domain_and_table_family_parallel
  global_constraints_ref: constraint_ledger.req_20260529_0001
  merge_policy:
    canonical_id_deduplication: true
    preserve_agent_scores: true
    prefer_primary_domain_evidence: true
    require_runtime_scope_before_executable_selection: true
  domain_agents:
    - agent_id: domain.marketplace_reconciliation
      domain: marketplace_reconciliation
      mission: Find marketplace reconciliation, settlement, return, fee, and variance evidence.
      evidence_priority_profile: marketplace_settlement_delay
      allowed_card_types:
        - metric_implementation
        - reconciliation_profile
        - relationship
        - table
        - column
        - rule
    - agent_id: domain.logistics
      domain: logistics
      mission: Find courier, AWB, freight, COD remittance, and invoice evidence.
      allowed_card_types:
        - business_flow_binding
        - matching_logic
        - relationship
        - table
        - column
  table_family_agents:
    - agent_id: table_family.settlement_ledger
      table_family: settlement_ledger
      mission: Find settlement tables, date/status fields, payout amounts, and pending/overdue metrics.
    - agent_id: table_family.order_ledger
      table_family: order_ledger
      mission: Find order grain, channel, brand, status, and join keys as supporting evidence.
```

Agents are logical units. The first implementation can execute them sequentially or with local concurrency. The contract is that each agent has its own mission, allowed evidence classes, constraints, and result packet.

### 5.6 SearchAgentResult

Each search agent returns scoped evidence, not a final SQL answer.

```yaml
search_agent_result:
  agent_id: table_family.settlement_ledger
  agent_type: table_family
  status: completed
  search_jobs:
    - rj_settlement_tables_001
    - rj_settlement_metrics_001
  accepted_candidates:
    - canonical_id: table.zs_observe.meesho_settlement
      evidence_family: primary
      table_family: settlement_ledger
      grounded_fields:
        - column.zs_observe.meesho_settlement.payment_date
        - column.zs_observe.meesho_settlement.settlement_date
    - canonical_id: metric_implementation.myntra_settlement.settlement_velocity
      evidence_family: primary
      table_family: settlement_metric
  rejected_candidates: []
  unresolved:
    - normalized_cross_marketplace_settlement_status
  agent_confidence: high
```

### 5.7 EvidenceMergeReport

After fan-out, the orchestrator must merge and arbitrate across agent outputs.

```yaml
evidence_merge_report:
  merge_id: merge.req_20260529_0001
  source_agents:
    - domain.marketplace_reconciliation
    - table_family.settlement_ledger
    - table_family.order_ledger
  merged_candidate_count: 42
  deduplicated_candidate_count: 31
  conflicts:
    - conflict_type: domain_priority
      primary_candidate: table.zs_observe.meesho_settlement
      competing_candidate: table.zs_observe.increff_sales
      resolution: settlement table wins for settlement-delay intent
    - conflict_type: field_semantics
      field: payment_date
      resolution: keep marketplace-specific semantics; do not normalize without contract
  missing_cross_agent_contracts:
    - normalized settlement status mapping across marketplaces
    - source precedence across marketplace settlement tables
```

The merge report feeds the candidate pool and arbitration report.

### 5.8 RetrievalJob

Retrieval should be decomposed into jobs.

```yaml
retrieval_job:
  job_id: rj_runtime_bindings_001
  stage: runtime_resolution
  purpose: Resolve active Ardeur Meesho account data bindings.
  query: Ardeur Fashion Meesho active account_data_binding table bindings
  datasets:
    - zenstatement_canonical
  search_types:
    - RAG_COMPLETION
    - GRAPH_COMPLETION
  node_names:
    - client.ardeur
    - canonical.vendor.meesho
  card_type_filter:
    - tenant
    - group
    - platform_account
    - account_data_binding
  hard_filters:
    tenant_code:
      - ardeur_fashion
    platform_code:
      - meesho
  top_k: 12
  accept_if:
    - canonical_id exists
    - card_type is allowed
    - status is active
```

### 5.9 CandidatePool

The candidate pool normalizes all retrieved items.

```yaml
candidate_pool:
  accepted:
    - canonical_id: account_data_binding.ardeur_fashion.meesho_in.primary.meesho_sales
      card_type: account_data_binding
      accepted_for_stage: runtime_resolution
      acceptance_reason:
        - tenant scope matched
        - platform scope matched
        - status active
        - binds physical table
  rejected:
    - canonical_id: account_data_binding.other_client.meesho_in.primary.meesho_sales
      rejection_reason:
        - rejected_by_tenant_scope
  ambiguous:
    - canonical_id: platform_account.ardeur_fashion.meesho_in.secondary
      ambiguity_reason:
        - account hint primary not enough to prove this account
  missing:
    - contract.meesho.gross_gmv
```

### 5.10 CandidateArbitrationReport

Candidate arbitration must compare candidates within the requested domain, not only by physical executability.

```yaml
candidate_arbitration_report:
  primary_domain: settlement_reconciliation
  selected_strategy: marketplace_specific_mva
  rejected_broad_proxy:
    table: table.zs_observe.increff_sales
    reason:
      - order/WMS pipeline table is adjacent evidence, not authoritative settlement evidence
      - settlement-specific metric implementations and settlement columns were retrieved
      - selected SQL would require ungrounded fields for this table
  primary_candidates:
    - table_id: table.zs_observe.ajio_settlement
      evidence:
        - payment_status supports paid/overdue/null settlement-delay classification
      decision: candidate_section
    - table_id: table.zs_observe.meesho_settlement
      evidence:
        - payment_date and settlement_date support timing analysis
      decision: candidate_section
    - table_id: table.zs_observe.myntra_settlement
      evidence:
        - amount_pending_settlement and settlement_velocity implementation available
      decision: candidate_section
  consolidation_status:
    safe_union_grounded: false
    missing:
      - schema mapping across marketplace settlement tables
      - deduplication/source precedence across marketplace settlements
  final_decision:
    - produce multi-section settlement report plan
    - do not use broad operational proxy as primary source
```

### 5.11 CapabilityMatrix

The runtime resolver should emit a capability matrix before SQL planning.

```yaml
capability_matrix:
  tenant_id: tenant.ardeur_fashion
  platform_account_id: platform_account.ardeur_fashion.meesho_in.primary
  platform_context_id: platform_context.meesho.in
  runtime_scope_filters:
    - column: group_id
      operator: =
      value: 65
    - column: group_level_id
      operator: =
      value: 221
  active_tables:
    order_ledger:
      table_id: table.zs_observe.meesho_sales
      binding_id: account_data_binding.ardeur_fashion.meesho_in.primary.meesho_sales
    product_mapping:
      table_id: table.zs_observe.meesho_brand_mapping
      binding_id: account_data_binding.ardeur_fashion.meesho_in.primary.meesho_brand_mapping
  unavailable_roles:
    settlement_ledger:
      reason: no active binding found
```

### 5.12 SQLContextPacket

The SQL compiler should receive a compact packet, not raw chunks.

```yaml
sql_context_packet:
  packet_id: packet.ardeur.meesho.gmv_month_brand.v1
  dialect: athena_trino
  request_id: req_20260529_0001
  intent_ref: intent.req_20260529_0001
  capability_matrix_ref: capability.ardeur.meesho.primary
  selected_contracts:
    metrics:
      - metric_impl.meesho.gross_gmv
    relationships:
      - relationship_contract.meesho.sales_to_brand_mapping
    rules:
      - rule.runtime.scope_filter_required
      - rule.table.active_filter_required
  table_scans:
    sales:
      physical_name: zs_observe.meesho_sales
      table_id: table.zs_observe.meesho_sales
      field_grounding:
        order_id: column.zs_observe.meesho_sales.order_id
        order_date: column.zs_observe.meesho_sales.order_date
        charged_amount: column.zs_observe.meesho_sales.charged_amount
      required_filters:
        - is_active = true
        - group_id = 65
        - group_level_id = 221
  joins:
    - join_certificate_id: join_cert.meesho.sales_brand_mapping
      condition: sales.order_id = brand_mapping.order_id
  output_contract:
    grain:
      - month
      - brand
    fields:
      - month
      - brand
      - gross_gmv
```

---

## 6. Stage-by-stage constrained orchestration

### 6.1 Stage 0 - Request normalization

Input:

```text
raw user question
CLI/API scope flags
dataset/search settings
```

Output:

```text
RequestEnvelope
```

Hard gates:

- If the user asks for production SQL and no tenant/client scope is available, return a clarification or blocked packet.
- If the user asks metadata inventory, tenant scope can be optional but must be represented as unknown.

Repo implementation:

```text
src/zenkb/orchestration/models.py
src/zenkb/orchestration/cli.py
```

### 6.2 Stage 1 - Raw intent parsing

This stage classifies the question before retrieval.

It should extend the current `classify_raw_intent` behavior in `cognee_sql_handoff.py`.

Output:

```text
IntentIR
EvidencePriorityProfile
initial ConstraintLedger
answer_mode_hint
required evidence classes
```

Hard gates:

- Do not select tables yet.
- Do not produce SQL.
- Do not let platform hints override explicit CLI/API scope.
- If the request contains settlement, payout, remittance, pending payment, overdue payment, marketplace-based settlement, or reconciliation-delay language, mark settlement/reconciliation as the primary evidence family.

Repo implementation:

```text
src/zenkb/orchestration/intent.py
src/zenkb/orchestration/domain_router.py
cognee/skills/sql_orchestration/intent_parser.md
```

### 6.3 Stage 2 - Constraint ledger initialization

Convert intent into explicit constraints.

Constraint classes:

```text
scope constraints
retrieval class constraints
candidate acceptance constraints
execution constraints
validation constraints
negative constraints
repair constraints
```

Example negative constraints:

```text
do not query canonical metadata as physical SQL
do not use inactive account_data_binding
do not use review_required binding for production SQL
do not join shared column names without a certified relationship
do not allocate lower-grain costs to higher-grain dimensions without allocation contract
do not let a broad order/WMS table outrank settlement evidence for settlement-delay intent
do not use a proxy table when primary settlement/reconciliation candidates are available and unblocked
do not generate SQL fields that are not grounded for the selected physical table
```

Repo implementation:

```text
src/zenkb/orchestration/constraints.py
```

### 6.4 Stage 3 - Class-aware fan-out retrieval planning

Build a retrieval plan made of domain agents, table-family agents, and independent retrieval jobs.

The orchestrator should fan out when:

```text
the intent contains multiple domain families
the requested metric needs multiple table families
the output needs both primary metric evidence and supporting dimension/join evidence
cross-domain flow participants are present
the first retrieval pass reveals strong candidates from more than one domain
```

Examples:

```text
settlement delay by marketplace -> settlement_ledger agent + order_ledger support agent
profitability by SKU -> sales agent + returns agent + settlement/fee agent + ads/logistics agent
COD remittance reconciliation -> OMS agent + logistics agent + payment/bank agent
inventory variance -> WMS movement agent + marketplace inventory agent + order reservation agent
```

The first plan should usually include:

```text
runtime_scope_job
platform_type_job
vendor_context_job
domain_search_agent_jobs
table_family_search_agent_jobs
metric_contract_job
settlement_reconciliation_evidence_job
relationship_contract_job
rule_contract_job
output_contract_job
```

Each job has:

```text
allowed card types
scope filters
search mode
node names
top-k
acceptance criteria
follow-up trigger
```

Each logical search agent has:

```text
mission
domain or table family
allowed card types
required and forbidden evidence families
search queries
budget/top-k
acceptance rules
agent-local unresolved items
```

Fan-out must have a deterministic fan-in step. Agents may propose candidates, but `evidence_merger` and `candidate_arbitrator` decide which candidates become executable.

Repo implementation:

```text
src/zenkb/orchestration/retrieval_plan.py
src/zenkb/orchestration/search_fanout.py
src/zenkb/orchestration/search_agent.py
src/zenkb/orchestration/table_family_router.py
```

### 6.5 Stage 4 - Cognee discovery

Cognee should execute retrieval jobs and search-agent jobs, then return raw evidence candidates grouped by agent.

Important rule:

```text
Cognee returns candidates. It does not finalize executable selections.
```

Search mode policy:

| Retrieval class | Preferred search style | Reason |
|---|---|---|
| Runtime bindings | exact/graph/context | Scope must be precise. |
| Platform type | summaries/graph | Finds abstract roles and patterns. |
| Vendor semantics | chunks plus graph | Finds concrete tables, columns, rules. |
| Settlement/reconciliation evidence | graph plus targeted semantic search | Finds settlement tables, payment status/date fields, payout metrics, variance metrics, and process timing rules before proxy selection. |
| Contracts | graph plus semantic search | Finds execution-facing objects. |
| Missing evidence repair | targeted query | Avoids global regeneration. |

Fan-out execution rules:

```text
Run domain agents independently so one domain does not crowd out another in top-k.
Run table-family agents independently when a query needs multiple table roles.
Apply per-agent top-k budgets before global merge.
Require every agent result to label accepted, rejected, ambiguous, and missing evidence.
Do not let a broad table-family agent consume the entire context budget for a multi-domain request.
```

Repo implementation:

```text
src/zenkb/orchestration/cognee_discovery.py
src/zenkb/orchestration/search_agent.py
src/zenkb/cognee_runtime/client.py
```

### 6.6 Stage 5 - Candidate normalization

Normalize Cognee results into canonical IDs and evidence records.

Rules:

- Accept only IDs present in the canonical registry or contract registry.
- Mark unrecognized canonical-looking IDs as unrecognized, not accepted.
- Separate physical runtime tables from canonical metadata.
- Preserve why each candidate was retrieved.
- Preserve which domain evidence family the candidate belongs to: primary, adjacent, or last-resort proxy.
- Preserve grounded field evidence for every column later used in SQL.
- Preserve raw Cognee snippets for traceability, but do not pass raw snippets to SQL generation unless needed for explanation.

Repo implementation:

```text
src/zenkb/orchestration/candidate_pool.py
src/zenkb/orchestration/field_grounding.py
src/zenkb/retrieval.py
```

### 6.7 Stage 6 - Evidence merge and conflict resolution

Merge search-agent outputs before final candidate arbitration.

The merge step should:

```text
deduplicate canonical IDs across agents
preserve which agent found each candidate
preserve agent-local scores and evidence-family labels
merge grounded fields for the same physical table
detect conflicting domain interpretations
detect table-family overlap
detect missing cross-agent contracts
```

Conflict examples:

```text
settlement agent finds marketplace-specific settlement tables
order agent finds one broad operational table
merge resolves this as settlement-primary, order-supporting

logistics agent finds AWB-level settlement
OMS agent finds order-level sales
merge marks AWB/order join key as required before cross-domain SQL

sales agent finds gross sales fields
settlement agent finds payout fields
merge blocks net settlement profitability until grain and source precedence are certified
```

Hard gates:

- No single agent can finalize `selected_source`.
- Cross-agent joins require relationship, matching, or flow contracts.
- If two agents assign different semantics to the same field name, keep the semantics separate until a normalization contract exists.
- Agent-local MVA proposals must be re-ranked globally after merge.

Repo implementation:

```text
src/zenkb/orchestration/evidence_merger.py
src/zenkb/orchestration/candidate_pool.py
```

### 6.8 Stage 7 - Domain-aware candidate arbitration

Before runtime capability and SQL planning, compare candidate sources against the evidence priority profile.

For settlement/reconciliation intent, primary candidates include:

```text
settlement tables
reconciliation tables/profiles
settlement metric implementations
payment status fields
settlement/payment/remittance date fields
amount pending settlement fields
settlement variance fields
order-to-settlement process timing evidence
```

Adjacent candidates include:

```text
OMS/order tables
sales tables
business process metadata
platform/account binding metadata
```

Last-resort proxies include:

```text
WMS pipeline tables
broad operational order facts without settlement fields
generic sales tables without payout/remittance semantics
```

Hard gates:

- If any primary settlement/reconciliation candidate is available, a last-resort proxy cannot be selected as the primary source unless every primary candidate is blocked by missing runtime binding, missing physical table, missing required fields, or unsafe status.
- If an all-marketplace settlement union is not safe, the orchestrator should choose the best marketplace-specific settlement MVA or emit a multi-section report plan.
- A broad operational proxy must carry `proxy_strength: weak` and must state which primary evidence was unavailable or blocked.
- Candidate arbitration must produce rejected-source reasons that name the exact domain mismatch, not vague relevance language.

Repo implementation:

```text
src/zenkb/orchestration/domain_router.py
src/zenkb/orchestration/candidate_arbitrator.py
```

### 6.9 Stage 8 - Scope resolution

Resolve tenant, group, platform, account, and business scope.

Input classes:

```text
tenant
group
platform
platform_account
account_data_binding
business_scope_set
business_flow_binding
```

Output:

```text
ScopeResolution
RuntimeResolution
```

Hard gates:

- Runtime scope from CLI/API beats semantic retrieval hints.
- Runtime binding must be active.
- Scope filters from account data bindings must be carried into every table scan.
- Client runtime bindings must not be invented from vendor canonicals.

Repo implementation:

```text
src/zenkb/orchestration/scope_resolver.py
src/zenkb/orchestration/runtime_resolver.py
```

### 6.10 Stage 9 - Capability matrix construction

Build capability from active bindings only.

Output:

```text
CapabilityMatrix
unavailable capabilities
blocked capabilities
scope filters
active table roles
```

Hard gates:

- A vendor table contract is not executable until a client runtime binding activates it.
- A table can be known globally and still unavailable for a client.
- A query requiring a missing role returns partial or blocked, not fabricated SQL.

Repo implementation:

```text
src/zenkb/orchestration/capability_matrix.py
```

### 6.11 Stage 10 - Contract selection

Select metric, table, column, relationship, rule, validation, and output contracts.

Selection order:

```text
platform type role contracts
vendor implementation contracts
runtime-bound table contracts
domain-primary metric and settlement/reconciliation contracts
metric implementation contracts
relationship contracts
rule and validation contracts
output contract
```

Hard gates:

- A metric implementation must reference available source tables.
- A relationship contract must connect runtime-bound tables.
- A settlement/reconciliation intent must prefer settlement/reconciliation contracts over broad order/sales proxy contracts.
- A rule contract with severity blocking must be enforced before SQL generation.
- Contracts with draft or review-required status should block production SQL unless explicitly allowed.

Repo implementation:

```text
src/zenkb/orchestration/contract_selector.py
canonical/contracts.jsonl
```

### 6.12 Stage 11 - Join path planning

Construct the join graph from certified edges only.

Allowed join evidence:

```text
RelationshipContract
MatchingLogicContract
FlowContract
explicit query_pattern with physical join columns
```

Forbidden:

```text
same column name
same business word
same platform
LLM intuition
```

Output:

```text
JoinPathPlan
JoinCertificate[]
GrainCertificate[]
```

Repo implementation:

```text
src/zenkb/orchestration/join_path_planner.py
```

### 6.13 Stage 12 - Query Plan DAG builder

Build a DAG before SQL.

Node types:

```text
table_scan
filter
normalize
preaggregate
join
metric_compute
union
final_project
```

Required annotations:

```text
input grain
output grain
source contract IDs
runtime binding IDs
mandatory filters
join certificate ID
validation requirements
```

Repo implementation:

```text
src/zenkb/orchestration/dag_builder.py
```

### 6.14 Stage 13 - SQL packet assembly

The packet assembler turns the DAG and selected contracts into the minimal compiler input.

It should exclude:

```text
unselected chunks
rejected candidates
long prose
unbounded graph neighborhoods
metadata-only cards not used as evidence
```

It should include:

```text
physical table names
allowed columns
required filters
metric formula contracts
join certificates
grain certificates
output contract
validation checklist
```

Repo implementation:

```text
src/zenkb/orchestration/packet_assembler.py
```

### 6.15 Stage 14 - SQL compile and validate

Compilation can be template-based, LLM-assisted, or hybrid. Validation must be deterministic.

Static checks:

```text
TableRuntimeBoundCheck
ActiveBindingCheck
ScopeFilterCheck
ActiveFilterCheck
JoinCertificateCheck
NoMetadataSQLCheck
FieldGroundingCheck
DomainEvidencePriorityCheck
ProxyDowngradeCheck
NoUndocumentedJoinCheck
PreaggregationCheck
MetricFormulaCheck
OutputContractCheck
```

Physical checks can be optional at first:

```text
information_schema table exists
information_schema column exists
sample rows for scope exist
EXPLAIN succeeds
LIMIT 10 succeeds
```

Repo implementation:

```text
src/zenkb/orchestration/sql_compiler.py
src/zenkb/orchestration/field_grounding.py
src/zenkb/orchestration/validators.py
```

### 6.16 Stage 15 - Targeted repair or safe failure

Repair should create a new retrieval job for exactly the missing evidence.

Examples:

```text
missing relationship contract -> retrieve relationship cards only
missing table binding -> retrieve account_data_binding only
missing cast rule -> retrieve column/rule contracts only
missing brand allocation rule -> retrieve output/allocation contracts only
```

If still unresolved, return:

```yaml
safe_failure_packet:
  plan_status: blocked
  blocked_stage: join_path_planning
  blocking_constraints:
    - brand allocation requires certified settlement-to-brand relationship
  missing_evidence:
    - relationship_contract.meesho.settlement_to_brand_mapping
  suggested_repo_actions:
    - author or generate relationship contract
    - add validation test for brand-grain allocation
```

Repo implementation:

```text
src/zenkb/orchestration/repair.py
```

---

## 7. Constraint ledger lifecycle

The ledger should become stricter as the pipeline advances.

```text
Stage 1: broad business constraints
Stage 3: retrieval class constraints
Stage 6: runtime scope constraints
Stage 8: contract execution constraints
Stage 9: relationship and grain constraints
Stage 12: SQL validation constraints
Stage 13: repair or blocked constraints
```

Example lifecycle:

```yaml
ledger_updates:
  - stage: intent_parsing
    added:
      unresolved_constraints:
        - tenant_id
        - platform_account_id
        - gross_gmv_metric

  - stage: runtime_resolution
    resolved:
      tenant_id: tenant.ardeur_fashion
      platform_account_id: platform_account.ardeur_fashion.meesho_in.primary
    added:
      execution_constraints:
        - group_id = 65 must apply to all scoped scans
        - group_level_id = 221 must apply to all scoped scans

  - stage: contract_selection
    resolved:
      gross_gmv_metric: metric_impl.meesho.gross_gmv
    added:
      required_table_ids:
        - table.zs_observe.meesho_sales

  - stage: join_path_planning
    blocked:
      - no certified relationship from settlement return logistics to brand
```

The ledger should be persisted in traces so every blocked or accepted decision can be audited.

---

## 8. Answer-mode routing

The orchestrator should explicitly route each request into one of four modes.

| Mode | Meaning | SQL behavior |
|---|---|---|
| `physical_sql` | Runtime tables can answer the question. | Build SQL only from physical tables. |
| `metadata_inventory` | User asks source topology, mappings, configured platforms, workflows, or dependency inventory. | Return metadata answer or commented handoff; do not query metadata as business SQL. |
| `partial_plan` | Useful runtime evidence exists, but some requirements are missing. | Return partial SQL or a multi-section report plan only if limitations are explicit and safe. |
| `blocked` | A hard gate fails. | Return SafeFailurePacket with missing evidence and suggested repo additions. |

This expands the current handoff script behavior and makes it a first-class decision object.

---

## 9. Settlement/reconciliation routing

Settlement, payout, remittance, overdue payment, pending settlement, and marketplace-based settlement questions need a stricter route than generic operational reporting.

### 9.1 Routing triggers

Set `primary_domain = settlement_reconciliation` when the request includes terms or intent such as:

```text
marketplace-based settlements
settlement delay
delayed settlement
overdue payment
pending settlement
payout delay
remittance delay
payment status
settlement velocity
amount pending settlement
order-to-settlement timing difference
settlement variance
reconciliation delay
```

### 9.2 Candidate priority

For this route, candidate classes must be prioritized as:

```text
Tier 1: settlement/reconciliation metric implementations
Tier 1: physical settlement tables and reconciliation tables
Tier 1: payment_status, settlement_date, payment_date, amount_pending, variance fields
Tier 2: OMS/order tables that have certified settlement joins
Tier 2: business_process or workflow evidence explaining order-to-settlement timing
Tier 3: broad sales/order/WMS operational proxies
```

Tier 3 candidates cannot win only because they are broad, single-table, or executable.

### 9.3 Cross-marketplace settlement reports

If the user asks for a report across marketplaces and no safe union is grounded:

```text
do not select a broad order/WMS proxy as the primary answer
do not fabricate a normalized settlement schema
do not union marketplace settlement tables without schema mapping, deduplication, and source precedence
```

Return one of:

```text
best marketplace-specific settlement MVA
multi-section report plan, one section per grounded marketplace settlement implementation
blocked packet listing missing cross-marketplace settlement normalization contracts
```

Example multi-section plan:

```yaml
multi_section_report_plan:
  report_intent: marketplace_settlement_delay_risk
  sections:
    - marketplace: AJIO
      source: zs_observe.ajio_settlement
      evidence: payment_status supports paid/overdue/null classification
    - marketplace: Meesho
      source: zs_observe.meesho_settlement
      evidence: payment_date and settlement_date support delay timing
    - marketplace: Myntra
      source: zs_observe.myntra_settlement
      evidence: amount_pending_settlement and settlement_velocity contracts available
    - marketplace: Nykaa
      source: zs_observe.nykaa_settlement
      evidence: actual_settlement and differential_amount support variance view
  consolidation_missing:
    - normalized settlement status mapping
    - common date semantics across settlement tables
    - cross-marketplace deduplication/source precedence
```

### 9.4 Proxy downgrade rule

A broad proxy table can be selected only when all are true:

```text
no settlement/reconciliation physical table is available, or every such table is blocked
no settlement/reconciliation metric implementation is usable
the proxy fields used in SQL are grounded for the selected table
the result is labeled as weak proxy/MVA
missing_or_ambiguous names the absent settlement evidence
```

For example, an order/WMS table with channel, order status, order date, and amount may support operational delay analysis, but it is not authoritative marketplace settlement evidence unless settlement fields or certified settlement joins are grounded.

### 9.5 Required validators

Add validators for this route:

```text
DomainEvidencePriorityCheck
  Fails when a Tier 3 proxy is selected while unblocked Tier 1 settlement/reconciliation candidates exist.

FieldGroundingCheck
  Fails when SQL uses columns not grounded for the selected physical table or selected join package.

ProxyDowngradeDisclosureCheck
  Fails when a proxy is selected but missing_or_ambiguous does not clearly state proxy scope and missing primary evidence.

SettlementConsolidationCheck
  Fails when marketplace settlement tables are UNIONed without grounded schema mapping, deduplication, and source precedence.
```

This rule directly addresses the failure where retrieved settlement evidence was available but the final package selected a broad operational table and emitted ungrounded fields.

---

## 10. Cross-domain orchestration

Cross-domain requests must add flow constraints before selecting tables.

Examples:

```text
marketplace settlement -> bank credit
D2C OMS -> payment gateway settlement
payment gateway payout -> bank credit
D2C COD orders -> logistics settlement
OMS -> WMS inventory
```

Required stages:

```text
1. Resolve business_scope_set.
2. Resolve business_flow_binding.
3. Resolve participant platform accounts.
4. Resolve account_data_bindings for every participant.
5. Resolve runtime join-key contracts.
6. Resolve flow-specific relationship/matching contracts.
7. Build flow DAG.
```

Hard rule:

```text
No cross-domain join is valid unless a business_flow_binding or FlowContract permits it and the runtime join keys are known.
```

Repo additions for cross-domain:

```text
canonical/contracts/flow_contracts.jsonl
canonical/contracts/runtime_join_key_contracts.jsonl
src/zenkb/orchestration/flow_resolver.py
tests/test_flow_resolver.py
tests/test_cross_domain_safe_failure.py
```

---

## 11. Repo change map

| Area | Current state | Proposed change |
|---|---|---|
| Canonical validation | `src/zenkb/canonical.py` validates cards and edges. | Add contract artifact validation and status/severity conventions. |
| Cognee export | `src/zenkb/cognee_export.py` emits card documents. | Add contract-shaped export optimized for execution retrieval. |
| Retrieval | `src/zenkb/retrieval.py` does bundle assembly and warnings. | Split into reusable discovery, candidate, scope, and handoff helpers. |
| Domain routing | Current prompt infers intent inside a broad MVA policy. | Add deterministic evidence priority profiles for settlement, reconciliation, inventory, logistics, and operational proxy routes. |
| Search fan-out | Current retrieval is effectively one global context stream. | Add logical domain and table-family search agents with per-agent budgets and independent result packets. |
| Evidence merge | No explicit fan-in layer exists after multi-domain retrieval. | Add deterministic merge reports that deduplicate candidates, preserve agent provenance, and detect cross-agent conflicts. |
| Candidate arbitration | Current prompt may over-reward one broad physical table. | Add domain-aware arbitration that downgrades broad proxies when primary evidence exists. |
| Field grounding | Current local validation rejects metadata SQL but not every ungrounded selected-table field. | Add field-level grounding certificates and reject SQL that uses ungrounded columns. |
| Handoff script | `cognee/scripts/cognee_sql_handoff.py` runs prompt stages. | Keep as compatibility, add orchestrated runner. |
| Skills | `cognee/skills/sql_handoff/*` owns staged prompts. | Add `sql_orchestration` prompts that propose, not decide. |
| Eval | `eval_runs/cognee_sql_handoff_batch.py` runs question batches. | Add orchestration batch with expected mode, missing evidence, and validation outcome. |
| Tests | Current tests cover retrieval and handoff helpers. | Add tests for each deterministic orchestration gate. |

---

## 12. Implementation plan by phase

### Phase A - Types, traces, and shell orchestration

Add:

```text
src/zenkb/orchestration/models.py
src/zenkb/orchestration/constraints.py
src/zenkb/orchestration/domain_router.py
src/zenkb/orchestration/table_family_router.py
src/zenkb/orchestration/trace.py
src/zenkb/orchestration/cli.py
```

Deliver:

```text
RequestEnvelope
IntentIR
EvidencePriorityProfile
ConstraintLedger
SearchFanoutPlan
SearchAgentResult
EvidenceMergeReport
RetrievalJob
CandidatePool
OrchestrationTrace
SafeFailurePacket
```

Tests:

```text
tests/test_orchestration_models.py
tests/test_constraint_ledger.py
tests/test_domain_router.py
tests/test_table_family_router.py
```

### Phase B - Fan-out retrieval and candidate normalization

Add:

```text
src/zenkb/orchestration/retrieval_plan.py
src/zenkb/orchestration/search_fanout.py
src/zenkb/orchestration/search_agent.py
src/zenkb/orchestration/cognee_discovery.py
src/zenkb/orchestration/evidence_merger.py
src/zenkb/orchestration/candidate_pool.py
src/zenkb/orchestration/candidate_arbitrator.py
```

Refactor from:

```text
src/zenkb/retrieval.py
cognee/scripts/cognee_sql_handoff.py
```

Deliver:

```text
retrieval jobs by evidence class
domain search agents by detected domain family
table-family search agents by required table role
per-agent top-k/context budgets
evidence merge report with agent provenance
accepted/rejected/ambiguous/missing candidate records
unrecognized canonical mention handling
domain-aware primary/adjacent/proxy candidate classification
settlement/reconciliation candidates outrank broad operational proxies for settlement-delay intent
```

Tests:

```text
tests/test_retrieval_plan.py
tests/test_search_fanout.py
tests/test_search_agent.py
tests/test_evidence_merger.py
tests/test_candidate_pool.py
tests/test_candidate_arbitrator.py
```

### Phase C - Scope resolver and capability matrix

Add:

```text
src/zenkb/orchestration/scope_resolver.py
src/zenkb/orchestration/runtime_resolver.py
src/zenkb/orchestration/capability_matrix.py
```

Deliver:

```text
tenant/group/platform/account resolution
active account_data_binding selection
runtime scope filter injection
unavailable capabilities
```

Tests:

```text
tests/test_scope_resolver.py
tests/test_runtime_resolver.py
tests/test_capability_matrix.py
```

### Phase D - Contract selection and join path planning

Add:

```text
canonical/contracts.jsonl
canonical/contract_edges.jsonl
src/zenkb/orchestration/contract_selector.py
src/zenkb/orchestration/join_path_planner.py
```

Deliver:

```text
selected metric/table/relationship/rule/output contracts
join certificates
grain certificates
blocked join decisions
```

Tests:

```text
tests/test_contract_selector.py
tests/test_join_path_planner.py
```

### Phase E - DAG, packet, validation

Add:

```text
src/zenkb/orchestration/dag_builder.py
src/zenkb/orchestration/packet_assembler.py
src/zenkb/orchestration/sql_compiler.py
src/zenkb/orchestration/field_grounding.py
src/zenkb/orchestration/validators.py
src/zenkb/orchestration/repair.py
```

Deliver:

```text
QueryPlanDAG
SQLContextPacket
SQLArtifact
ValidationReport
FieldGroundingCertificate
DomainEvidencePriorityCheck
ProxyDowngradeDisclosureCheck
targeted repair retrieval
```

Tests:

```text
tests/test_dag_builder.py
tests/test_packet_assembler.py
tests/test_sql_validation_gates.py
tests/test_field_grounding.py
tests/test_settlement_proxy_downgrade.py
tests/test_repair_loop.py
```

### Phase F - Eval and migration

Add:

```text
cognee/scripts/cognee_sql_orchestrate.py
eval_runs/cognee_sql_orchestration_batch.py
eval_runs/fixtures/sql_orchestration_questions.jsonl
```

Deliver:

```text
batch comparison against current handoff script
mode distribution report
blocked evidence report
contract coverage report
```

---

## 13. Minimum viable vertical slice

Start narrow:

```text
Client: Ardeur Fashion
Platform: Meesho
Domain: marketplace seller reconciliation
Questions:
  1. gross GMV by month
  2. gross GMV by month and brand
  3. returns by month
  4. net revenue by month
  5. OMS vs settlement match
  6. settlement-delay or pending-settlement risk by marketplace
```

Required artifacts:

```text
active Ardeur Meesho account_data_bindings
Meesho table usage contracts
Meesho gross GMV metric implementation contract
Meesho return metric implementation contract
Meesho sales-to-brand relationship contract
Meesho sales-to-settlement relationship or matching contract
Meesho settlement date/payment date column contracts
settlement-delay evidence priority profile
broad operational proxy downgrade rule
runtime scope filter rules
active filter rules
output contract for month/brand metrics
output contract for marketplace-specific settlement-delay report sections
```

The first vertical slice should prove:

- runtime bindings gate table usage,
- scope filters are injected,
- physical SQL never queries canonical metadata,
- joins are certified,
- missing brand allocation blocks or downgrades grain,
- settlement/reconciliation intent chooses settlement evidence before broad order/WMS proxies,
- unsafe all-marketplace settlement consolidation returns marketplace-specific sections or a blocked plan,
- SQL fields are grounded against selected physical tables,
- traces explain every decision.

---

## 14. Trace artifact

Every orchestration run should write a trace.

```yaml
orchestration_trace:
  trace_id: trace.req_20260529_0001
  request: ...
  stages:
    - name: intent_parsing
      status: passed
      inputs:
        - request_envelope
      outputs:
        - intent_ir
        - evidence_priority_profile
        - constraint_ledger
    - name: search_fanout
      status: passed
      agents_spawned:
        - domain.marketplace_reconciliation
        - table_family.settlement_ledger
        - table_family.order_ledger
      outputs:
        - search_fanout_plan
        - search_agent_results
    - name: evidence_merge
      status: passed
      conflicts_resolved:
        - settlement evidence outranked broad order proxy
      outputs:
        - evidence_merge_report
    - name: candidate_arbitration
      status: passed
      selected_strategy: marketplace_specific_mva
      rejected_proxy_candidates:
        - table.zs_observe.increff_sales
      reason:
        - settlement/reconciliation evidence available
        - operational proxy downgraded
    - name: runtime_resolution
      status: passed
      accepted_candidates:
        - account_data_binding.ardeur_fashion.meesho_in.primary.meesho_sales
      rejected_candidates:
        - account_data_binding.other_client.meesho_in.primary.meesho_sales
    - name: join_path_planning
      status: blocked
      missing_evidence:
        - relationship_contract.meesho.settlement_to_brand_mapping
  final_status: blocked
```

Default output locations:

```text
build/orchestration/runs/<timestamp>_<slug>/trace.json
build/orchestration/runs/<timestamp>_<slug>/constraint_ledger.json
build/orchestration/runs/<timestamp>_<slug>/search_fanout_plan.json
build/orchestration/runs/<timestamp>_<slug>/search_agent_results.json
build/orchestration/runs/<timestamp>_<slug>/evidence_merge_report.json
build/orchestration/runs/<timestamp>_<slug>/candidate_pool.json
build/orchestration/runs/<timestamp>_<slug>/candidate_arbitration.json
build/orchestration/runs/<timestamp>_<slug>/field_grounding.json
build/orchestration/runs/<timestamp>_<slug>/sql_context_packet.json
build/orchestration/runs/<timestamp>_<slug>/result.md
```

---

## 15. CLI shape

Add:

```text
python -m zenkb.orchestration.cli \
  "For Ardeur on Meesho, show brand-level GMV by month" \
  --tenant "Ardeur Fashion Limited" \
  --platform Meesho \
  --dataset zenstatement_canonical \
  --search-type RAG_COMPLETION \
  --also-search GRAPH_COMPLETION \
  --emit-trace build/orchestration/runs
```

Script wrapper:

```text
python cognee/scripts/cognee_sql_orchestrate.py \
  --query "For Ardeur on Meesho, show brand-level GMV by month" \
  --tenant "Ardeur Fashion Limited" \
  --platform Meesho \
  --output build/orchestration/runs/manual_001/result.json \
  --markdown-output build/orchestration/runs/manual_001/result.md
```

Expected result summary:

```yaml
result:
  status: sql_ready | partial_plan | metadata_inventory | blocked
  answer_mode: physical_sql
  sql_artifact: null_or_object
  safe_failure_packet: null_or_object
  trace_path: build/orchestration/runs/.../trace.json
```

---

## 16. Tests and acceptance criteria

### 16.1 Unit tests

Add tests for:

```text
IntentIR preserves explicit scope
DomainRouter marks settlement-delay intent as settlement_reconciliation
TableFamilyRouter derives required table families from requested roles/metrics
ConstraintLedger adds negative constraints
RetrievalPlan emits separate jobs by card type
SearchFanoutPlan spawns one agent per required domain and table family
SearchAgentResult preserves agent-local accepted/rejected/missing evidence
EvidenceMergeReport deduplicates candidates and preserves agent provenance
CandidatePool rejects wrong-tenant cards
CandidateArbitrator rejects broad order/WMS proxy when settlement candidates exist
RuntimeResolver requires active account_data_binding
CapabilityMatrix exposes unavailable roles
ContractSelector rejects contracts using unbound tables
JoinPathPlanner blocks undocumented joins
PacketAssembler excludes raw rejected evidence
Validator rejects SQL against canonical metadata
Validator rejects SQL fields not grounded on the selected physical table
Validator rejects unsafe all-marketplace settlement UNION without mapping/dedup/source precedence
RepairLoop issues targeted retrieval jobs
```

### 16.2 Fixture tests

Use small synthetic cards/edges to test:

```text
single-table metric query
multi-table certified join query
missing relationship contract
inactive binding
metadata inventory query
cross-domain flow missing AWB join key
multi-domain question spawns marketplace, logistics, payment, and bank agents
multi-table-family metric spawns order, settlement, return, fee, and mapping agents
settlement-delay query with AJIO/Meesho/Myntra/Nykaa settlement evidence and an Increff order proxy
broad proxy selected only when all settlement candidates are blocked
multi-section settlement report when safe union is not grounded
```

### 16.3 Eval criteria

For each batch question record:

```yaml
expected:
  status: sql_ready | partial_plan | metadata_inventory | blocked
  must_include_card_ids: []
  must_not_include_card_ids: []
  must_apply_filters:
    - group_id
    - group_level_id
  must_have_join_certificates: true
  domain_priority:
    settlement_reconciliation:
      must_prefer_primary_evidence_over_proxy: true
      allowed_proxy_only_if_primary_blocked: true
  must_ground_sql_fields_on_selected_tables: true
  fanout:
    expected_domain_agents: []
    expected_table_family_agents: []
    must_preserve_agent_provenance: true
  safe_union_requires:
    - schema_mapping
    - deduplication_rule
    - source_precedence_rule
  blocked_if_missing:
    - relationship_contract
    - account_data_binding
    - field_grounding
```

Success is not only SQL generation. A correct blocked result is success when required evidence is genuinely absent.

---

## 17. Open design decisions

1. **Use dataclasses or Pydantic for orchestration models?**  
   Recommendation: start with dataclasses plus explicit validators if the repo wants minimal dependencies. Move to Pydantic only if schema generation becomes valuable.

2. **Should contracts be generated into `canonical/contracts.jsonl` or stored as card types under `canonical/cards/`?**  
   Recommendation: generate standalone JSONL first, with back-references to canonical cards. Later, mirror into card folders if useful for review.

3. **Should SQL compilation be deterministic templates or LLM-assisted?**  
   Recommendation: hybrid. The DAG and packet are deterministic; rendering may be LLM-assisted, but validation decides.

4. **Should Cognee node sets be hard required?**  
   Recommendation: no for the first slice. Use dataset plus card-type filtering first, then add node sets as an optimization.

5. **Should missing tenant scope ask the user or return blocked?**  
   Recommendation: CLI/API should return `blocked` with `required_clarification: tenant` for production SQL. Interactive surfaces can ask the user.

6. **Should broad operational proxies ever satisfy settlement/reconciliation questions?**  
   Recommendation: only as explicit weak MVAs after all primary settlement/reconciliation candidates are unavailable or blocked. The trace must show the rejected primary candidates and the proxy downgrade reason.

---

## 18. Final orchestration contract

The orchestrator should obey this contract:

```text
1. Parse intent before retrieval.
2. Convert intent into explicit constraints.
3. Spawn logical search agents for every required domain and table family.
4. Retrieve by evidence class inside each agent, not global top-k.
5. Merge agent results with provenance and conflict resolution.
6. Accept only canonical or contract IDs known to the repo.
7. Resolve runtime scope before executable table selection.
8. Build capability only from active bindings.
9. Select contracts only when source tables are runtime-available.
10. Apply domain evidence priority before selecting an MVA/proxy.
11. Certify every join.
12. Ground every SQL field on the selected physical table or join package.
13. Build a Query Plan DAG before SQL.
14. Validate SQL against constraints.
15. Repair with targeted retrieval only.
16. Return a safe failure when hard gates remain unresolved.
```

Operational mantra:

```text
Cognee discovers candidates.
Search agents keep domains and table families from crowding each other out.
The merger preserves provenance and resolves conflicts.
The orchestrator applies constraints.
The planner emits a verified packet.
The compiler renders SQL.
The validator decides whether the result is executable.
```
