# Generic Evidence Profile Orchestration Plan

## Summary

Implement a generic post-table evidence planning layer for constrained search.

The system must not route by example query, marketplace, SKU, courier, or any other source-specific shortcut. It should route by a generic evidence profile registry. The LLM chooses one or more profiles from that registry based on the query's answer obligations and the legal catalog evidence available for selected tables/domains.

Core flow:

```text
query
  -> tenant/group scope
  -> platform/account/binding/domain/table selection
  -> table/domain evidence manifest
  -> LLM evidence profile selection
  -> profile-derived Cognee contracts
  -> evidence pack
  -> SQL handoff
```

## Card Type Purpose Map

### Runtime Scope

- `tenant`: Tenant/client root.
- `group`: Tenant group/group-level runtime scope.
- `platform`: Source system/platform.
- `platform_context`: Platform context such as geography, currency, fulfilment mode, or source context.
- `platform_account`: Tenant/group-specific connected source account.
- `account_data_binding`: Runtime proof that a tenant/group/platform account can use a table/domain/source role.
- `business_scope_set`: Runtime scope bundle across platform accounts and bindings.
- `business_flow_binding`: Runtime binding of a tenant/group to a business flow.

### Source, Domain, And Table

- `domain`: Business domain bucket under a source/system.
- `table`: Physical/source table contract.
- `column`: Field-level semantics, data type, grain/filter/join/metric roles, and optional value profile pointer.
- `relationship`: Table join/link evidence and join-safety guidance.

### Metrics And Reporting

- `metric`: Global business metric definition.
- `metric_implementation`: Table-specific implementation of a metric.
- `metric_dependency`: Dependency between metrics or metric components.
- `formula_template`: Reusable formula/calculation template.
- `query_pattern`: Query/report blueprint.
- `output_contract`: Expected output shape/report contract.
- `execution_constraint_set`: Constraints required for safe execution.

### Values, Rules, And Quality

- `value_profile`: Known values, status semantics, normalization, and null/value interpretation.
- `rule`: Business rule, guardrail, or deterministic action.
- `validation_test`: Data quality or correctness test.
- `state_transition`: Lifecycle/status transition semantics.

### Process And Operations

- `business_process`: Process flow definition.
- `workflow_step`: Operational step within a process.
- `process_variant`: Special case or variant of a process.

### Reconciliation

- `reconciliation_profile`: Overall reconciliation scenario.
- `reconciliation_side`: One side of a reconciliation.
- `reconciliation_unit`: Grain/unit of matching.
- `matching_logic`: Matching keys, tolerances, and strategy.
- `mismatch_category`: Mismatch classification and likely causes.
- `reconciliation_variant`: Special case or variant of a reconciliation profile.

## Evidence Profile Registry

The profile registry is generic. It describes evidence obligations, not source-specific examples.

- `runtime_scope_resolution`
  - Purpose: Resolve legal tenant/group runtime sources.
  - Card types: `tenant`, `group`, `platform`, `platform_context`, `platform_account`, `account_data_binding`, `business_scope_set`, `business_flow_binding`.

- `source_domain_resolution`
  - Purpose: Resolve relevant domains and source areas within legal runtime scope.
  - Card types: `domain`, `account_data_binding`, `table`.

- `table_contract_resolution`
  - Purpose: Resolve table contracts and table-level source semantics.
  - Card types: `table`, `column`, `relationship`.

- `field_semantics_resolution`
  - Purpose: Resolve fields, values, statuses, filters, grouping, joins, and value semantics.
  - Card types: `column`, `value_profile`, `state_transition`, `rule`.

- `measure_calculation_resolution`
  - Purpose: Resolve counts, amounts, rates, ratios, trends, and derived measures.
  - Card types: `metric`, `metric_implementation`, `metric_dependency`, `formula_template`, `column`, `value_profile`.

- `query_shape_resolution`
  - Purpose: Resolve report/query shape, required fields, grouping, filters, ordering, and expected output.
  - Card types: `query_pattern`, `output_contract`, `execution_constraint_set`, `column`, `metric_implementation`.

- `relationship_join_resolution`
  - Purpose: Resolve joins, relationship safety, cardinality, and pre-aggregation requirements.
  - Card types: `relationship`, `table`, `column`.

- `process_flow_resolution`
  - Purpose: Resolve operational process flow, workflow steps, variants, and lifecycle states.
  - Card types: `business_process`, `workflow_step`, `process_variant`, `state_transition`, `table`, `column`.

- `reconciliation_resolution`
  - Purpose: Resolve reconciliation sides, units, matching logic, mismatch categories, and variants.
  - Card types: `reconciliation_profile`, `reconciliation_side`, `reconciliation_unit`, `matching_logic`, `mismatch_category`, `reconciliation_variant`, `relationship`, `rule`, `validation_test`.

- `validation_guardrail_resolution`
  - Purpose: Resolve data quality checks, execution guardrails, mandatory filters, and blocking/warning constraints.
  - Card types: `rule`, `validation_test`, `execution_constraint_set`, `value_profile`, `column`.

## Implementation Plan

1. Add a generic card-type purpose registry.
   - It must include every generated card type listed above.
   - It must be source-agnostic and platform-agnostic.
   - Tests should fail if the generated catalog contains a card type missing from the registry.

2. Add a generic evidence profile registry.
   - Profiles must reference only valid card types.
   - Profiles must describe answer obligations, required card types, optional card types, and whether field-level evidence may be needed.
   - Profiles must not contain marketplace-specific or example-query-specific rules.

3. Add a table/domain evidence manifest builder.
   - Build it after finalized table frames and active account binding verification.
   - Summarize evidence available for each selected table/domain by card type.
   - Keep candidate ids compact and bounded.
   - Separate table-local evidence from domain-local evidence.

4. Add an LLM evidence profile selector.
   - Input: query text, runtime context, selected table/domain scope, card-type purpose registry, evidence profile registry, evidence manifest.
   - Output: selected profile ids, answer obligation per profile, required/optional card types, per-table/per-domain evidence requests, and column strategy: `none`, `targeted`, or `broad`.
   - The selector must choose only profile ids from the registry.

5. Convert selected profile requests into Cognee contracts.
   - `table_local_<card_type>_search` contracts require `card_type:<card_type>` and `table_id:<table_id>`.
   - `domain_local_<card_type>_search` contracts require `card_type:<card_type>` and `domain_id:<domain_id>`.
   - Exact dereference may be used for known ids already present in the manifest.
   - Deterministic code only enforces legality, catalog reachability, contract validation, exact dereference, and evidence sufficiency.

6. Update the state machine.
   - After `semantic_table_frame_search`, build the evidence manifest.
   - Call the profile selector.
   - Emit profile-derived contracts.
   - Skip the old generic table planner when the profile selector emits valid profile contracts.
   - Keep the old planner only as fallback for non-table paths or profile-selection failure.

7. Update branch ledger and evidence pack behavior.
   - Track evidence card ids by all supported card types.
   - Make branch usability profile-aware instead of hardcoding query pattern/metric/column sufficiency.
   - Include selected profiles, manifest summary, and selected evidence grouped by card type in the evidence pack.

## Acceptance Criteria

- No deterministic source/use-case routing is introduced.
- Evidence profile selection is LLM-driven and constrained to the generic registry.
- Runtime legality remains deterministic.
- Table/domain evidence manifests are present in search traces.
- Search traces show `evidence_profile_selector` decisions.
- Evidence packs include selected profiles and card-type-grouped evidence.
- Broad column fetch happens only when the selector chooses `column_strategy: broad`.
- Existing constrained-search tests continue to pass.
- New tests cover profile selection, manifest creation, generic contract validation, profile-aware branch usability, and card-type registry coverage.

## Out Of Scope

- Swarm or parallel execution.
- SQL compiler changes.
- Marketplace-specific profile routing.
- Hardcoded query-to-profile keyword mapping.
