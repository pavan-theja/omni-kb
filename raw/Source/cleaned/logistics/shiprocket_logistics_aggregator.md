# Shiprocket Services Aggregator Knowledge — Parser Ready v6 Role-Split Unified Edges
## 0. Document Metadata
```yaml
document_metadata:
  document_id: shiprocket_services_aggregator_parser_ready_v6_role_split
  title: Shiprocket Services Aggregator Knowledge — Parser Ready v6 Role-Split Unified Edges
  domain: logistics
  vendor: Shiprocket
  source_docx: /mnt/data/Logistics KB Doc.docx
  frame_of_reference: logistics_gold_std_canonical_card_frame_v5 plus flipkart_v8_unified_edges_style plus marketplace_cleanup_manifest_consolidated_v2
  generated_on: '2026-05-24'
  version: 6.0-role-split-manifest-aligned-unified-edges
  scope: shiprocket_services_aggregator_financial_intermediary_with_unified_edges
  logistics_only: true
  shiprocket_role_split: services_aggregator
  single_canonical_platform_id: platform.shiprocket
  allowed_card_types:
  - platform
  - platform_context
  - table
  - column
  - relationship
  - value_profile
  - metric
  - metric_implementation
  forbidden_card_types:
  - tenant
  - group
  - platform_account
  - account_data_binding
  - business_scope_set
  - business_flow_binding
  - logistics_route_binding
  - courier_bank_route_binding
  - payment_route_binding
  - bank_route_binding
  - erp_bank_route_binding
```

## 0.1 V6 Refactor Notes — Shiprocket Role Split
```yaml
v6_refactor_notes:
  refactor_basis:
  - Logistics KB Doc.docx as source-of-truth evidence
  - marketplace_cleanup_manifest_consolidated_v2.md as cleanup/review gate source
  - canonical_edge_taxonomy_registry.md as allowed edge universe
  - v5 manifest-aligned logistics markdowns as structural base
  refactor_goal: Split Shiprocket into role-specific logistics-partner and services-aggregator documents while preserving one canonical platform.shiprocket and deterministic candidate_card/candidate_edge ingestion.
  semantic_change_policy: No unsupported tenant/group/account binding is introduced in generic logistics files; role split changes document ownership, not canonical platform identity.
  parser_contract:
  - candidate_card and candidate_edge blocks remain the primary ingestible units
  - candidate cards are deduped by card_id; repeated metric/platform cards remain readability duplicates
  - candidate edges should be validated by edge_id and by source/target referential integrity
  - Shiprocket role-specific docs must not create new platform IDs
```

## 0. Parser Instructions

This document is intended to be parsed deterministically. It is not prose-only. The parser should emit `candidate_card` blocks and `candidate_edge` blocks, normalize legacy aliases into the canonical uppercase edge taxonomy, and dedupe repeated cards by `card_id`.

Critical parser rules:

- Create only logistics-scoped reusable cards from this document.
- Keep exactly one canonical Shiprocket platform: `platform.shiprocket`. Do not create `platform.shiprocket_logistics_partner` or `platform.shiprocket_services_aggregator`.
- Treat this file as the Shiprocket **services aggregator / financial intermediary** role view.
- Do not create tenant, group, platform account, account data binding, business scope set, or business flow binding cards from generic vendor/domain documents.
- Treat scope-like fields such as `group_level_id`, `group_id`, `merchant_id`, `bank_name`, and similar values as columns/caveats only.
- Metric cards own colloquial/business meaning; metric implementation cards own platform/table-specific formulas.
- Materialize inverse edges only when `materialize_inverse: true`; otherwise use graph reverse indexes.
- Do not invent domain-specific route-binding edges. Use Business Flow Binding only in separate business-flow applicability docs.

## 1. Source Intake and Evidence Registry
```yaml
source_evidence:
  id: evidence.logistics_kb_doc
  source_document: Logistics KB Doc.docx
  summary: Primary logistics/courier KB covering order flow, money flow, table statuses, join keys, vendor roles, amount semantics, and reconciliation hierarchy.
  confidence: high
```
```yaml
source_evidence:
  id: evidence.cognee_design_v4
  source_document: Cognee KB Design v4.md
  summary: Canonical card schema, scope model, graph edge primacy, and card-family responsibilities.
  confidence: high
```
```yaml
source_evidence:
  id: evidence.unified_edge_scope
  source_document: Pasted text.txt
  summary: Canonical edge taxonomy, inverse edge policy, legacy edge aliases, and domain-specific use guidance for logistics/payment/bank/ERP docs.
  confidence: high
```
```yaml
source_evidence:
  id: evidence.flipkart_v8_format
  source_document: flipkart_marketplace_clean_md_v8_unified_edges.md
  summary: Deterministic ingestion style reference using candidate_card and candidate_edge YAML blocks with edge metadata.
  confidence: high
```
```yaml
source_evidence:
  id: evidence.logistics_gold_frame
  source_document: logistics_gold_std_raw_md_frame_v3.md and logistics_gold_std_canonical_card_frame_v5.md
  summary: Logistics domain authoring boundary, business flow binding handoff, amount semantics, table block structure, and logistics card scope.
  confidence: high
```
```yaml
source_evidence:
  id: evidence.shiprocket.vendor_scope
  source_document: Logistics KB Doc.docx
  summary: 'Vendor-specific extracted evidence for shiprocket: table role, coverage status, metrics, caveats, and joins.'
  confidence: high
```

## 2. Out-of-Scope Registry
```yaml
out_of_scope_item:
  id: oos.logistics.tenant_group
  topic: Tenant/group/platform account/business flow cards
  instruction: Do not create tenant, group, platform_account, account_data_binding, business_scope_set, or business_flow_binding cards from generic logistics files. Use business flow applicability docs for that layer.
  allowed_as: source column, caveat, review item, or business-flow applicability input only
```
```yaml
out_of_scope_item:
  id: oos.logistics.account_filters
  topic: Account filters and group_level_id values
  instruction: Treat group_level_id, merchant_id, bank_name, and similar scope fields as source columns or caveats only unless a dedicated Account Data Binding doc is being authored.
  allowed_as: source column, caveat, review item, or business-flow applicability input only
```
```yaml
out_of_scope_item:
  id: oos.logistics.bank_statement_execution
  topic: Bank statement execution
  instruction: Generic logistics docs can expose UTR and bank-reference bridge fields, but actual bank account selection and bank statement matching require Banking KB plus Business Flow Binding.
  allowed_as: source column, caveat, review item, or business-flow applicability input only
```
```yaml
out_of_scope_item:
  id: oos.logistics.unsupported_native_tables
  topic: Unsupported native courier tables
  instruction: Do not create fake native table evidence for Shadowfax or Ecom Express; use indirect/fallback evidence only where documented.
  allowed_as: source column, caveat, review item, or business-flow applicability input only
```

## 3. Compact Semantic Field Contract

| card family | required semantic intent |
|---|---|
| `platform/platform_context` | one canonical Shiprocket identity, India logistics context, role-specific evidence refs |
| `table/column/value_profile` | grain, amount semantics, join/filter roles, coverage status, known values, caveats |
| `relationship` | source/target table, join keys, cardinality, safe usage, aggregation risk |
| `metric/metric_implementation` | colloquial metric meaning vs table-specific formula, metric_pattern, required columns, filters, allowed grains |
| `execution governance` | manifest gates and review items that constrain deterministic extraction |

## 3.1 Shiprocket Role Contract
```yaml
shiprocket_role_contract:
  role_name: Shiprocket as Services Aggregator
  canonical_platform_id: platform.shiprocket
  role_summary: Financial intermediary and courier services aggregator for consolidated freight billing, underlying courier attribution, COD collection/remittance evidence, and schema-only settlement report handling.
  owned_source_tables:
  - table.zs_observe.shiprocket_invoice
  - table.zs_observe.shiprocket_settlement
  - table.zs_observe.shiprocket_settlement_report
  owned_process_variant_id: process_variant.shiprocket_services_aggregator.financial_intermediary
  primary_business_processes:
  - business_process.shipment_to_freight_invoice
  - business_process.freight_charge_validation
  - business_process.cod_delivery_to_courier_remittance
  handoff_relationships:
  - relationship.shiprocket_invoice.dtdc_settlement.awb
  - relationship.shiprocket_invoice.ekart_settlement.awb
  - relationship.shiprocket_invoice.shiprocket_settlement.awb
  - relationship.shiprocket_invoice.xpressbees_settlement.awb
  - relationship.shiprocket_oms.shiprocket_invoice.awb
  - relationship.shiprocket_oms.shiprocket_settlement.awb
  - relationship.shiprocket_settlement.delhivery_settlement.awb
  - relationship.shiprocket_settlement.xpressbees_settlement.awb
  role_boundary_policy:
  - owns primary Shiprocket freight invoice and COD remittance formulas
  - does not own operational AWB assignment/state lifecycle except through handoff relationships to shiprocket_oms
  - does not create native tables for indirect couriers
  - does not own tenant/group bank destination routing
```

## Manifest Layer A — Evidence Anchor Manifests
```yaml
evidence_anchor_manifest:
  source_evidence_id: ev.shiprocket.services_aggregator.financial_tables
  source_section: Logistics KB Doc.docx / Money Flows, Freight Invoice Chain, COD Order Settlement Chain, Shiprocket Financial Tables
  evidence_type: prose | table_status | metric_definition | schema_reference | reconciliation_playbook
  supported_semantics:
  - Shiprocket acts as courier services aggregator and financial intermediary for consolidated freight billing and COD settlement
  - shiprocket_invoice is per-AWB consolidated freight invoice evidence raised by Shiprocket regardless of underlying courier
  - shiprocket_settlement is per-AWB COD remittance evidence where the courier collects cash and Shiprocket remits to seller
  - shiprocket_settlement_report is schema-only/empty and must not be used as active evidence until rows are loaded
  unsupported_semantics:
  - Do not use shiprocket_settlement_report as an accepted active implementation while row_count is zero
  - Do not treat shiprocket_invoice.charged_amount and shiprocket_settlement.charged_amount as the same amount concept
  - Do not create tenant/group/account/business-flow bindings from group_level_id observations
  allowed_card_types:
  - platform
  - platform_context
  - table
  - column
  - relationship
  - value_profile
  - metric
  - metric_implementation
  forbidden_card_types:
  - tenant
  - group
  - platform_account
  - account_data_binding
  - business_scope_set
  - business_flow_binding
  confidence_policy:
    explicit_table_or_formula: high
    inferred_from_prose: medium
    absent_or_ambiguous: review_required
```

## Manifest Layer B — Cleanup Manifest Gates Applied to This File
```yaml
manifest_gate:
  id: gate.logistics.evidence_anchor_resolution
  derived_from_manifest: evidence_anchor_manifest
  applies_to:
  - candidate_card
  - candidate_edge
  deterministic_parser_action:
  - resolve broad evidence_refs into exact evidence_anchor_manifest IDs before accepting the object
  - reject or convert to review_item when no exact anchor supports the specific semantic claim
  - never promote prose-only evidence into executable formula evidence unless the table/field/formula section supports it
  card_resolution_rules:
    platform: ev.logistics.courier_partner_summary
    platform_context: ev.logistics.courier_partner_summary
    table: ev.logistics.table_status.summary plus any vendor-specific table anchor
    column: vendor-specific table anchor or ev.logistics.scope.group_level_ids for scope columns
    relationship: ev.logistics.join_keys.cross_table_join_map
    value_profile: source table status/value section or vendor-specific transaction/status section
    metric: ev.logistics.money_flow.* or ev.logistics.reconciliation.hierarchy
    metric_implementation: vendor-specific table anchor with documented columns and formula_sql
    business_process: ev.logistics.order_flow.high_level_order_flow or ev.logistics.money_flow.*
    workflow_step: process anchor plus at least one table/column/status evidence anchor
    state_transition: state/value profile anchor plus process anchor
    process_variant: ev.logistics.fulfilment.fbf_non_fbf or vendor-specific coverage anchor
    reconciliation_profile: ev.logistics.reconciliation.hierarchy
    query_pattern: reconciliation/profile anchor plus table/relationship/metric implementation anchors
```
```yaml
manifest_gate:
  id: gate.logistics.card_type_fit
  derived_from_manifest: card_type_fit_manifest
  applies_to_card_types:
  - business_process
  - workflow_step
  - state_transition
  - process_variant
  - reconciliation_profile
  - reconciliation_variant
  - value_profile
  - rule
  - execution_constraint_set
  fit_rules:
    use_business_process_when: source documents ordered operational events or lifecycle expectation
    use_reconciliation_profile_when: source documents expected side, actual side, gap, match, amount comparison, timing mismatch, or settlement-vs-bank bridge
    use_process_variant_when: source documents a materially different sequence, state progression, evidence source, or matching logic
    use_value_profile_when: source only defines allowed values, labels, segments, or statuses
    use_rule_when: source states a semantic interpretation, mandatory filter, fallback rule, or unsafe assumption
    use_execution_constraint_set_when: multiple query patterns require the same cross-cutting safety behavior
  fail_if:
  - segment_or_label_becomes_process_variant_without_lifecycle_change
  - reconciliation_semantics_are_encoded_as_generic_lifecycle_only
  - rule_like_business_constraint_is_encoded_as_execution_constraint_without_cross_pattern_runtime_scope
  remediation:
  - recast_card_type
  - downgrade_to_note
  - convert_to_review_item
  - keep_as_is_when_source_evidence_is_explicit
```
```yaml
manifest_gate:
  id: gate.logistics.lazy_load_detection
  derived_from_manifest: lazy_load_detection_manifest
  applies_to_card_types:
  - business_process
  - workflow_step
  - state_transition
  - process_variant
  - metric_implementation
  - query_pattern
  - execution_constraint_set
  fail_if:
  - description_repeats_name_without_source_specific_content
  - workflow_step_has_no_table_column_status_metric_or_reconciliation_side
  - state_transition_has_no_from_state_or_to_state_or_evidence_column
  - process_variant_is_only_a_vendor_label_or_group_label
  - metric_implementation_formula_contains_natural_language_placeholder
  - query_pattern_has_no_metric_reconciliation_rule_or_output_contract_targets
  - execution_constraint_set_has_no_rules_or_validation_tests
  remediation:
  - replace_with_source_specific_definition
  - convert_to_rule_or_reconciliation_step
  - delete_if_no_material_semantic_content
  - open_review_item_only_if_source_gap_is_real
```
```yaml
manifest_gate:
  id: gate.logistics.metric_implementation_executability
  derived_from_manifest: metric_implementation_manifest
  applies_to_card_types:
  - metric_implementation
  formula_must:
  - reference existing table cards through USES_TABLE edges
  - reference existing column cards through USES_COLUMN edges
  - include required filters and status/value semantics
  - respect amount semantics and grain
  - be executable SQL-like logic or explicitly marked unsupported_empty, indirect_only, or low_confidence
  fail_if:
  - formula_sql_contains_undefined_component
  - formula_sql_references_column_without_column_card
  - formula_sql_uses_charged_amount_without_table_specific_amount_semantics
  - implementation_uses_empty_schema_only_table_as_active_evidence
  - implementation_omits_required_status_or_payment_mode_filter_when metric semantics require it
  remediation:
  - keep_metric_card_but_remove_or_review_implementation
  - convert_to_unsupported_metric_implementation
  - add_sql_pattern_ref_or_formula_sql
  - add_review_item_for_missing_schema_or_formula
```
```yaml
manifest_gate:
  id: gate.logistics.formula_and_sign_semantics
  derived_from_manifest: formula_sign_manifest
  amount_semantics_rules:
    column.zs_observe.shiprocket_invoice.charged_amount: freight_billed_amount
    column.zs_observe.shiprocket_settlement.charged_amount: cod_collected_or_remitted_amount
    column.zs_observe.shiprocket_oms.charged_amount: declared_product_value_not_freight
    column.zs_observe.delhivery_invoice.charged_amount: declared_product_value_not_freight
    column.zs_observe.dtdc_settlement.charged_amount: cod_or_product_settlement_value_not_freight
    column.zs_observe.ekart_settlement.charged_amount: cod_or_product_settlement_value_not_freight
    column.zs_observe.xpressbees_settlement.net_payment: cod_remitted_when_populated_low_confidence
  fail_if:
  - sums_any_charged_amount_without_table_semantics
  - compares_declared_product_value_to_freight_or_cod_without_explicit_transformation
  - treats_batch_total_as_awb_level_amount
```
```yaml
manifest_gate:
  id: gate.logistics.schema_type_fidelity
  derived_from_manifest: schema_type_manifest
  applies_to_card_types:
  - table
  - column
  - metric_implementation
  - query_pattern
  type_policy:
    when_source_declared_type_absent: keep data_type unknown and require cast note before executable SQL
    when_source_declared_type_present: canonical_data_type must match source or include cast_required=true
    scope_columns: retain as source columns only; do not emit account-binding cards from generic logistics docs
  fail_if:
  - source_string_marked_as_date_without_cast_or_review
  - mandatory active/status filters omitted where source section documents them
  - known physical column count is claimed fully represented when only key fields were listed
```
```yaml
manifest_gate:
  id: gate.logistics.sql_ref_integrity
  derived_from_manifest: sql_ref_integrity_manifest
  required_for_card_types:
  - metric_implementation
  - query_pattern
  - validation_test
  acceptance_policy:
    metric_implementation: accepted when formula_sql is executable and references declared columns
    query_pattern: accepted when edge targets and query_shape are sufficient; sql_ref may be review_required until a concrete SQL block exists
    validation_test: accepted when test_logic is deterministic and references rules/cards; sql_ref optional unless runtime SQL is needed
  fail_if:
  - sql_ref_points_to_missing_sql_pattern_block
  - formula_sql_and_sql_ref_disagree
  - sql_pattern_uses_undefined_column_or_deleted_card
```
```yaml
manifest_gate:
  id: gate.logistics.edge_referential_integrity
  derived_from_manifest: edge_integrity_manifest
  applies_to:
  - candidate_edge
  checks:
  - every_edge_source_id_exists_or_is_allowed_external_reference
  - every_edge_target_id_exists_or_is_allowed_external_reference
  - edge_type_is_in_canonical_edge_taxonomy_registry
  - inverse_edge_type_is_present
  - materialize_inverse_policy_is_valid
  - source_type_and_target_type_match_edge_catalog
  semantic_checks:
  - transition_edges_bind_to_correct_process
  - process_variant_edges_only_if_variant_valid
  - reconciliation_side_edges_match_profile_and_side_role
  - query_pattern_edges_match_primary_metric_reconciliation_rule_and_output_contract
  remediation:
  - delete_edge
  - remap_edge
  - recreate_missing_card_only_if_source_supports_it
  - convert_to_review_item
```

## Manifest Layer C — Vendor-Specific Manifest Enforcement
```yaml
vendor_manifest_enforcement:
  vendor: Shiprocket
  role: services_aggregator
  source_docx: Logistics KB Doc.docx
  no_tenant_group_cards: true
  no_business_flow_binding_cards: true
  single_canonical_platform_id: platform.shiprocket
  forbidden_platform_ids:
  - platform.shiprocket_logistics_partner
  - platform.shiprocket_services_aggregator
  allowed_scope_fields_as_columns_only:
  - group_level_id
  - group_id
  - merchant_id
  - bank_name
  - bank_account_id
  metric_implementation_policy:
    generic_metric_cards_allowed_for_single_file_readability: true
    canonical_metric_dedupe_key: card_id
    metric_implementations_must_reference_role_owned_table_or_explicit_fallback_table: true
    unsupported_or_indirect_coverage_must_be_explicit: true
  role_boundary_policy:
  - owns primary Shiprocket freight invoice and COD remittance formulas
  - does not own operational AWB assignment/state lifecycle except through handoff relationships to shiprocket_oms
  - does not create native tables for indirect couriers
  - does not own tenant/group bank destination routing
```

## Manifest Layer D — Review Items
```yaml
review_item:
  review_id: review.logistics.scope.business_flow_applicability_needed
  source_manifest: card_type_fit_manifest
  severity: medium
  status: open
  applies_to:
  - business_flow_binding
  - account_data_binding
  finding: Generic logistics docs intentionally do not create tenant/group/account-specific bindings. Queries crossing marketplace/channel to logistics or logistics to bank require a separate Business Flow Applicability document.
  deterministic_action: Do not emit Business Flow Binding from this file; retrieval must request tenant/group applicability context when runtime scope is required.
```
```yaml
review_item:
  review_id: review.logistics.sql_ref.query_patterns_need_runtime_sql_registry
  source_manifest: sql_ref_integrity_manifest
  severity: medium
  status: open
  applies_to:
  - query_pattern
  - validation_test
  finding: Query patterns are card/edge complete, but some query_pattern cards use pseudo-SQL shape rather than a concrete sql_ref block. This is acceptable for KB ingestion but should be completed before runtime SQL generation.
  deterministic_action: Keep cards active for retrieval; mark SQL generation as requiring orchestrator completion or downstream SQL-pattern registry.
```
```yaml
review_item:
  review_id: review.logistics.bank_statement_placeholder_external_dependency
  source_manifest: process_reconciliation_manifest
  severity: medium
  status: open
  applies_to:
  - reconciliation_profile.courier_batch_to_bank_credit
  - table.zs_observe.bank_statement
  finding: Bank statement table semantics are represented only as a placeholder in logistics reconciliation patterns. Actual bank account selection and bank table semantics must be supplied by Banking KB and Business Flow Binding.
  deterministic_action: Use bank_statement placeholder for graph traversal only; do not treat it as the final bank source schema.
```
```yaml
review_item:
  id: review.shiprocket_logistics_parser_ready_v5_manifest_aligned.business_flow_boundary
  topic: Business Flow Binding boundary
  instruction: No Business Flow Binding, tenant, group, platform account, or account data binding cards should be emitted from this generic logistics document.
  severity: high
  status: open_for_ingestion_validation
```
```yaml
review_item:
  review_id: review.shiprocket.services_aggregator.role_split_boundary
  source_manifest: card_type_fit_manifest
  severity: medium
  status: open_for_ingestion_validation
  applies_to:
  - shiprocket_services_aggregator_parser_ready_v6_role_split
  finding: Shiprocket has dual logistics roles. This file intentionally owns only one role-specific subset while using the same platform.shiprocket card.
  deterministic_action: Do not merge role semantics back into a single ambiguous Shiprocket vendor doc during ingestion; upsert shared cards by card_id and preserve role-specific metric implementation/table ownership.
```

## 4. Candidate Cards

### 4.1 platform cards

```yaml
candidate_card:
  card_type: platform
  card_id: platform.shiprocket
  name: Shiprocket
  fields:
    name: Shiprocket
    description: Shiprocket logistics platform/vendor in the logistics domain.
    status: active
    confidence: curated
    source_documents:
    - Logistics KB Doc.docx
    - Cognee KB Design v4.md
    - logistics_gold_std_raw_md_frame_v3.md
    - logistics_gold_std_canonical_card_frame_v5.md
    created_by: kb_authoring_assistant
    updated_by: kb_authoring_assistant
    version: 5.0-manifest-aligned
    platform_name: Shiprocket
    platform_type: courier_aggregator
    active: true
    evidence_refs:
    - evidence.logistics_kb_doc
    - evidence.cognee_design_v4
    - evidence.unified_edge_scope
```

### 4.2 platform_context cards

```yaml
candidate_card:
  card_type: platform_context
  card_id: platform_context.shiprocket.in
  name: Shiprocket India
  fields:
    name: Shiprocket India
    description: India logistics context for Shiprocket.
    status: active
    confidence: curated
    source_documents:
    - Logistics KB Doc.docx
    - Cognee KB Design v4.md
    - logistics_gold_std_raw_md_frame_v3.md
    - logistics_gold_std_canonical_card_frame_v5.md
    created_by: kb_authoring_assistant
    updated_by: kb_authoring_assistant
    version: 5.0-manifest-aligned
    platform_id: platform.shiprocket
    context_name: Shiprocket India
    context_type: logistics_region
    source_context_code: IN
    country: India
    region: IN
    currency: INR
    timezone: Asia/Kolkata
    active: true
    evidence_refs:
    - evidence.logistics_kb_doc
    - evidence.cognee_design_v4
    - evidence.unified_edge_scope
```

### 4.4 table cards

```yaml
candidate_card:
  card_type: table
  card_id: table.zs_observe.shiprocket_invoice
  name: Shiprocket Invoice
  fields:
    name: Shiprocket Invoice
    description: 'Shiprocket Invoice: One row per AWB-level Shiprocket freight invoice.'
    status: active
    confidence: curated
    source_documents:
    - Logistics KB Doc.docx
    - Cognee KB Design v4.md
    - logistics_gold_std_raw_md_frame_v3.md
    - logistics_gold_std_canonical_card_frame_v5.md
    created_by: kb_authoring_assistant
    updated_by: kb_authoring_assistant
    version: 5.0-manifest-aligned
    schema: zs_observe
    table_name: shiprocket_invoice
    full_reference: zs_observe.shiprocket_invoice
    engine: Athena v3 / Trino SQL
    table_type: freight_invoice
    source_platform_ids:
    - platform.shiprocket
    source_platform_types:
    - logistics
    business_purpose: One row per AWB-level Shiprocket freight invoice.
    grain: One row per AWB-level Shiprocket freight invoice.
    grain_keys:
    - awb/order/reference as specified by columns
    date_columns:
    - see date column cards
    recommended_date_columns:
    - see metric implementations
    avoid_columns:
    - see amount semantics caveats
    structural_applicability: platform.shiprocket; account filters are not defined here
    coverage_status: active
    row_count: '5038'
    period: Jan-Oct 2025
    group_ids: '203'
    schema_coverage: curated_key_fields
    evidence_refs:
    - evidence.logistics_kb_doc
    - evidence.cognee_design_v4
    - evidence.unified_edge_scope
    scope_caveat: Observed group/account values are source data observations only. Do not create tenant, group, platform_account, account_data_binding, business_scope_set, or business_flow_binding cards from this generic logistics document.
```
```yaml
candidate_card:
  card_type: table
  card_id: table.zs_observe.shiprocket_settlement
  name: Shiprocket Settlement
  fields:
    name: Shiprocket Settlement
    description: 'Shiprocket Settlement: One row per AWB-level Shiprocket COD settlement.'
    status: active
    confidence: curated
    source_documents:
    - Logistics KB Doc.docx
    - Cognee KB Design v4.md
    - logistics_gold_std_raw_md_frame_v3.md
    - logistics_gold_std_canonical_card_frame_v5.md
    created_by: kb_authoring_assistant
    updated_by: kb_authoring_assistant
    version: 5.0-manifest-aligned
    schema: zs_observe
    table_name: shiprocket_settlement
    full_reference: zs_observe.shiprocket_settlement
    engine: Athena v3 / Trino SQL
    table_type: cod_settlement
    source_platform_ids:
    - platform.shiprocket
    source_platform_types:
    - logistics
    business_purpose: One row per AWB-level Shiprocket COD settlement.
    grain: One row per AWB-level Shiprocket COD settlement.
    grain_keys:
    - awb/order/reference as specified by columns
    date_columns:
    - see date column cards
    recommended_date_columns:
    - see metric implementations
    avoid_columns:
    - see amount semantics caveats
    structural_applicability: platform.shiprocket; account filters are not defined here
    coverage_status: active
    row_count: '1200'
    period: Jan-Nov 2025
    group_ids: '203'
    schema_coverage: curated_key_fields
    evidence_refs:
    - evidence.logistics_kb_doc
    - evidence.cognee_design_v4
    - evidence.unified_edge_scope
    scope_caveat: Observed group/account values are source data observations only. Do not create tenant, group, platform_account, account_data_binding, business_scope_set, or business_flow_binding cards from this generic logistics document.
```
```yaml
candidate_card:
  card_type: table
  card_id: table.zs_observe.shiprocket_settlement_report
  name: Shiprocket Settlement Report
  fields:
    name: Shiprocket Settlement Report
    description: 'Shiprocket Settlement Report: Schema-only detailed settlement report; zero rows loaded.'
    status: active
    confidence: curated
    source_documents:
    - Logistics KB Doc.docx
    - Cognee KB Design v4.md
    - logistics_gold_std_raw_md_frame_v3.md
    - logistics_gold_std_canonical_card_frame_v5.md
    created_by: kb_authoring_assistant
    updated_by: kb_authoring_assistant
    version: 5.0-manifest-aligned
    schema: zs_observe
    table_name: shiprocket_settlement_report
    full_reference: zs_observe.shiprocket_settlement_report
    engine: Athena v3 / Trino SQL
    table_type: schema_only_report
    source_platform_ids:
    - platform.shiprocket
    source_platform_types:
    - logistics
    business_purpose: Schema-only detailed settlement report; zero rows loaded.
    grain: Schema-only detailed settlement report; zero rows loaded.
    grain_keys:
    - awb/order/reference as specified by columns
    date_columns:
    - see date column cards
    recommended_date_columns:
    - see metric implementations
    avoid_columns:
    - see amount semantics caveats
    structural_applicability: platform.shiprocket; account filters are not defined here
    coverage_status: empty_schema_only
    row_count: '0'
    period: '-'
    group_ids: '-'
    schema_coverage: schema_only
    evidence_refs:
    - evidence.logistics_kb_doc
    - evidence.cognee_design_v4
    - evidence.unified_edge_scope
    scope_caveat: Observed group/account values are source data observations only. Do not create tenant, group, platform_account, account_data_binding, business_scope_set, or business_flow_binding cards from this generic logistics document.
```

### 4.5 column cards

```yaml
candidate_card:
  card_type: column
  card_id: column.zs_observe.shiprocket_invoice.order_id
  name: shiprocket_invoice.order_id
  fields:
    name: shiprocket_invoice.order_id
    description: Shiprocket order ID.
    status: active
    confidence: curated
    source_documents:
    - Logistics KB Doc.docx
    - Cognee KB Design v4.md
    - logistics_gold_std_raw_md_frame_v3.md
    - logistics_gold_std_canonical_card_frame_v5.md
    created_by: kb_authoring_assistant
    updated_by: kb_authoring_assistant
    version: 5.0-manifest-aligned
    table_id: table.zs_observe.shiprocket_invoice
    column_name: order_id
    data_type: unknown
    semantic_roles: identifier
    business_concepts:
    - Shiprocket order ID.
    default_aggregation: SUM if financial measure else none
    sign_convention: positive_or_source_specific
    amount_semantics: not_applicable
    usable_for_filtering: false
    usable_for_grouping: false
    usable_for_metrics: false
    usable_for_joining: true
    usable_for_reconciliation: false
    evidence_refs:
    - evidence.logistics_kb_doc
    - evidence.cognee_design_v4
    - evidence.unified_edge_scope
```
```yaml
candidate_card:
  card_type: column
  card_id: column.zs_observe.shiprocket_invoice.other_id
  name: shiprocket_invoice.other_id
  fields:
    name: shiprocket_invoice.other_id
    description: AWB number; joins to shiprocket_oms.awb_code.
    status: active
    confidence: curated
    source_documents:
    - Logistics KB Doc.docx
    - Cognee KB Design v4.md
    - logistics_gold_std_raw_md_frame_v3.md
    - logistics_gold_std_canonical_card_frame_v5.md
    created_by: kb_authoring_assistant
    updated_by: kb_authoring_assistant
    version: 5.0-manifest-aligned
    table_id: table.zs_observe.shiprocket_invoice
    column_name: other_id
    data_type: unknown
    semantic_roles: identifier;join_key;reconciliation_key
    business_concepts:
    - AWB number
    - joins to shiprocket_oms.awb_code.
    default_aggregation: SUM if financial measure else none
    sign_convention: positive_or_source_specific
    amount_semantics: not_applicable
    usable_for_filtering: false
    usable_for_grouping: false
    usable_for_metrics: false
    usable_for_joining: true
    usable_for_reconciliation: true
    evidence_refs:
    - evidence.logistics_kb_doc
    - evidence.cognee_design_v4
    - evidence.unified_edge_scope
```
```yaml
candidate_card:
  card_type: column
  card_id: column.zs_observe.shiprocket_invoice.courier_partner
  name: shiprocket_invoice.courier_partner
  fields:
    name: shiprocket_invoice.courier_partner
    description: 'Actual courier used: DTDC Air, Delhivery Air, Xpressbees Air, Ekart Logistics Air, Ecom Air.'
    status: active
    confidence: curated
    source_documents:
    - Logistics KB Doc.docx
    - Cognee KB Design v4.md
    - logistics_gold_std_raw_md_frame_v3.md
    - logistics_gold_std_canonical_card_frame_v5.md
    created_by: kb_authoring_assistant
    updated_by: kb_authoring_assistant
    version: 5.0-manifest-aligned
    table_id: table.zs_observe.shiprocket_invoice
    column_name: courier_partner
    data_type: unknown
    semantic_roles: dimension;filter
    business_concepts:
    - 'Actual courier used: DTDC Air, Delhivery Air, Xpressbees Air, Ekart Logistics Air, Ecom Air.'
    default_aggregation: SUM if financial measure else none
    sign_convention: positive_or_source_specific
    amount_semantics: not_applicable
    usable_for_filtering: true
    usable_for_grouping: true
    usable_for_metrics: false
    usable_for_joining: false
    usable_for_reconciliation: false
    evidence_refs:
    - evidence.logistics_kb_doc
    - evidence.cognee_design_v4
    - evidence.unified_edge_scope
```
```yaml
candidate_card:
  card_type: column
  card_id: column.zs_observe.shiprocket_invoice.order_status
  name: shiprocket_invoice.order_status
  fields:
    name: shiprocket_invoice.order_status
    description: DELIVERED, RTO DELIVERED, LOST.
    status: active
    confidence: curated
    source_documents:
    - Logistics KB Doc.docx
    - Cognee KB Design v4.md
    - logistics_gold_std_raw_md_frame_v3.md
    - logistics_gold_std_canonical_card_frame_v5.md
    created_by: kb_authoring_assistant
    updated_by: kb_authoring_assistant
    version: 5.0-manifest-aligned
    table_id: table.zs_observe.shiprocket_invoice
    column_name: order_status
    data_type: unknown
    semantic_roles: status;filter
    business_concepts:
    - DELIVERED, RTO DELIVERED, LOST.
    default_aggregation: SUM if financial measure else none
    sign_convention: positive_or_source_specific
    amount_semantics: not_applicable
    usable_for_filtering: true
    usable_for_grouping: true
    usable_for_metrics: false
    usable_for_joining: false
    usable_for_reconciliation: false
    evidence_refs:
    - evidence.logistics_kb_doc
    - evidence.cognee_design_v4
    - evidence.unified_edge_scope
```
```yaml
candidate_card:
  card_type: column
  card_id: column.zs_observe.shiprocket_invoice.zone
  name: shiprocket_invoice.zone
  fields:
    name: shiprocket_invoice.zone
    description: Delivery zone a/b/c/d.
    status: active
    confidence: curated
    source_documents:
    - Logistics KB Doc.docx
    - Cognee KB Design v4.md
    - logistics_gold_std_raw_md_frame_v3.md
    - logistics_gold_std_canonical_card_frame_v5.md
    created_by: kb_authoring_assistant
    updated_by: kb_authoring_assistant
    version: 5.0-manifest-aligned
    table_id: table.zs_observe.shiprocket_invoice
    column_name: zone
    data_type: unknown
    semantic_roles: dimension;filter
    business_concepts:
    - Delivery zone a/b/c/d.
    default_aggregation: SUM if financial measure else none
    sign_convention: positive_or_source_specific
    amount_semantics: not_applicable
    usable_for_filtering: true
    usable_for_grouping: true
    usable_for_metrics: false
    usable_for_joining: false
    usable_for_reconciliation: false
    evidence_refs:
    - evidence.logistics_kb_doc
    - evidence.cognee_design_v4
    - evidence.unified_edge_scope
```
```yaml
candidate_card:
  card_type: column
  card_id: column.zs_observe.shiprocket_invoice.payment_mode
  name: shiprocket_invoice.payment_mode
  fields:
    name: shiprocket_invoice.payment_mode
    description: prepaid or cod.
    status: active
    confidence: curated
    source_documents:
    - Logistics KB Doc.docx
    - Cognee KB Design v4.md
    - logistics_gold_std_raw_md_frame_v3.md
    - logistics_gold_std_canonical_card_frame_v5.md
    created_by: kb_authoring_assistant
    updated_by: kb_authoring_assistant
    version: 5.0-manifest-aligned
    table_id: table.zs_observe.shiprocket_invoice
    column_name: payment_mode
    data_type: unknown
    semantic_roles: dimension;filter
    business_concepts:
    - prepaid or cod.
    default_aggregation: SUM if financial measure else none
    sign_convention: positive_or_source_specific
    amount_semantics: table_specific_financial_amount; do not generalize by column name
    usable_for_filtering: true
    usable_for_grouping: true
    usable_for_metrics: false
    usable_for_joining: false
    usable_for_reconciliation: false
    evidence_refs:
    - evidence.logistics_kb_doc
    - evidence.cognee_design_v4
    - evidence.unified_edge_scope
```
```yaml
candidate_card:
  card_type: column
  card_id: column.zs_observe.shiprocket_invoice.charged_amount
  name: shiprocket_invoice.charged_amount
  fields:
    name: shiprocket_invoice.charged_amount
    description: Total freight bill for this AWB.
    status: active
    confidence: curated
    source_documents:
    - Logistics KB Doc.docx
    - Cognee KB Design v4.md
    - logistics_gold_std_raw_md_frame_v3.md
    - logistics_gold_std_canonical_card_frame_v5.md
    created_by: kb_authoring_assistant
    updated_by: kb_authoring_assistant
    version: 5.0-manifest-aligned
    table_id: table.zs_observe.shiprocket_invoice
    column_name: charged_amount
    data_type: unknown
    semantic_roles: measure
    business_concepts:
    - Total freight bill for this AWB.
    default_aggregation: SUM if financial measure else none
    sign_convention: positive_or_source_specific
    amount_semantics: freight_billed_amount
    usable_for_filtering: false
    usable_for_grouping: false
    usable_for_metrics: true
    usable_for_joining: false
    usable_for_reconciliation: true
    evidence_refs:
    - evidence.logistics_kb_doc
    - evidence.cognee_design_v4
    - evidence.unified_edge_scope
```
```yaml
candidate_card:
  card_type: column
  card_id: column.zs_observe.shiprocket_invoice.charged_amount_excluding_tax
  name: shiprocket_invoice.charged_amount_excluding_tax
  fields:
    name: shiprocket_invoice.charged_amount_excluding_tax
    description: Freight before GST.
    status: active
    confidence: curated
    source_documents:
    - Logistics KB Doc.docx
    - Cognee KB Design v4.md
    - logistics_gold_std_raw_md_frame_v3.md
    - logistics_gold_std_canonical_card_frame_v5.md
    created_by: kb_authoring_assistant
    updated_by: kb_authoring_assistant
    version: 5.0-manifest-aligned
    table_id: table.zs_observe.shiprocket_invoice
    column_name: charged_amount_excluding_tax
    data_type: unknown
    semantic_roles: measure
    business_concepts:
    - Freight before GST.
    default_aggregation: SUM if financial measure else none
    sign_convention: positive_or_source_specific
    amount_semantics: table_specific_financial_amount; do not generalize by column name
    usable_for_filtering: false
    usable_for_grouping: false
    usable_for_metrics: true
    usable_for_joining: false
    usable_for_reconciliation: true
    evidence_refs:
    - evidence.logistics_kb_doc
    - evidence.cognee_design_v4
    - evidence.unified_edge_scope
```
```yaml
candidate_card:
  card_type: column
  card_id: column.zs_observe.shiprocket_invoice.total_tax
  name: shiprocket_invoice.total_tax
  fields:
    name: shiprocket_invoice.total_tax
    description: GST/tax on freight.
    status: active
    confidence: curated
    source_documents:
    - Logistics KB Doc.docx
    - Cognee KB Design v4.md
    - logistics_gold_std_raw_md_frame_v3.md
    - logistics_gold_std_canonical_card_frame_v5.md
    created_by: kb_authoring_assistant
    updated_by: kb_authoring_assistant
    version: 5.0-manifest-aligned
    table_id: table.zs_observe.shiprocket_invoice
    column_name: total_tax
    data_type: unknown
    semantic_roles: measure
    business_concepts:
    - GST/tax on freight.
    default_aggregation: SUM if financial measure else none
    sign_convention: positive_or_source_specific
    amount_semantics: table_specific_financial_amount; do not generalize by column name
    usable_for_filtering: false
    usable_for_grouping: false
    usable_for_metrics: true
    usable_for_joining: false
    usable_for_reconciliation: true
    evidence_refs:
    - evidence.logistics_kb_doc
    - evidence.cognee_design_v4
    - evidence.unified_edge_scope
```
```yaml
candidate_card:
  card_type: column
  card_id: column.zs_observe.shiprocket_invoice.charge_fsc
  name: shiprocket_invoice.charge_fsc
  fields:
    name: shiprocket_invoice.charge_fsc
    description: Fuel surcharge.
    status: active
    confidence: curated
    source_documents:
    - Logistics KB Doc.docx
    - Cognee KB Design v4.md
    - logistics_gold_std_raw_md_frame_v3.md
    - logistics_gold_std_canonical_card_frame_v5.md
    created_by: kb_authoring_assistant
    updated_by: kb_authoring_assistant
    version: 5.0-manifest-aligned
    table_id: table.zs_observe.shiprocket_invoice
    column_name: charge_fsc
    data_type: unknown
    semantic_roles: measure
    business_concepts:
    - Fuel surcharge.
    default_aggregation: SUM if financial measure else none
    sign_convention: positive_or_source_specific
    amount_semantics: table_specific_financial_amount; do not generalize by column name
    usable_for_filtering: false
    usable_for_grouping: false
    usable_for_metrics: true
    usable_for_joining: false
    usable_for_reconciliation: true
    evidence_refs:
    - evidence.logistics_kb_doc
    - evidence.cognee_design_v4
    - evidence.unified_edge_scope
```
```yaml
candidate_card:
  card_type: column
  card_id: column.zs_observe.shiprocket_invoice.charge_rto
  name: shiprocket_invoice.charge_rto
  fields:
    name: shiprocket_invoice.charge_rto
    description: RTO charge.
    status: active
    confidence: curated
    source_documents:
    - Logistics KB Doc.docx
    - Cognee KB Design v4.md
    - logistics_gold_std_raw_md_frame_v3.md
    - logistics_gold_std_canonical_card_frame_v5.md
    created_by: kb_authoring_assistant
    updated_by: kb_authoring_assistant
    version: 5.0-manifest-aligned
    table_id: table.zs_observe.shiprocket_invoice
    column_name: charge_rto
    data_type: unknown
    semantic_roles: measure
    business_concepts:
    - RTO charge.
    default_aggregation: SUM if financial measure else none
    sign_convention: positive_or_source_specific
    amount_semantics: table_specific_financial_amount; do not generalize by column name
    usable_for_filtering: false
    usable_for_grouping: false
    usable_for_metrics: true
    usable_for_joining: false
    usable_for_reconciliation: true
    evidence_refs:
    - evidence.logistics_kb_doc
    - evidence.cognee_design_v4
    - evidence.unified_edge_scope
```
```yaml
candidate_card:
  card_type: column
  card_id: column.zs_observe.shiprocket_invoice.charge_cod
  name: shiprocket_invoice.charge_cod
  fields:
    name: shiprocket_invoice.charge_cod
    description: COD handling fee.
    status: active
    confidence: curated
    source_documents:
    - Logistics KB Doc.docx
    - Cognee KB Design v4.md
    - logistics_gold_std_raw_md_frame_v3.md
    - logistics_gold_std_canonical_card_frame_v5.md
    created_by: kb_authoring_assistant
    updated_by: kb_authoring_assistant
    version: 5.0-manifest-aligned
    table_id: table.zs_observe.shiprocket_invoice
    column_name: charge_cod
    data_type: unknown
    semantic_roles: measure
    business_concepts:
    - COD handling fee.
    default_aggregation: SUM if financial measure else none
    sign_convention: positive_or_source_specific
    amount_semantics: table_specific_financial_amount; do not generalize by column name
    usable_for_filtering: false
    usable_for_grouping: false
    usable_for_metrics: true
    usable_for_joining: false
    usable_for_reconciliation: true
    evidence_refs:
    - evidence.logistics_kb_doc
    - evidence.cognee_design_v4
    - evidence.unified_edge_scope
```
```yaml
candidate_card:
  card_type: column
  card_id: column.zs_observe.shiprocket_invoice.charge_cod_adjust
  name: shiprocket_invoice.charge_cod_adjust
  fields:
    name: shiprocket_invoice.charge_cod_adjust
    description: COD adjustment.
    status: active
    confidence: curated
    source_documents:
    - Logistics KB Doc.docx
    - Cognee KB Design v4.md
    - logistics_gold_std_raw_md_frame_v3.md
    - logistics_gold_std_canonical_card_frame_v5.md
    created_by: kb_authoring_assistant
    updated_by: kb_authoring_assistant
    version: 5.0-manifest-aligned
    table_id: table.zs_observe.shiprocket_invoice
    column_name: charge_cod_adjust
    data_type: unknown
    semantic_roles: measure
    business_concepts:
    - COD adjustment.
    default_aggregation: SUM if financial measure else none
    sign_convention: positive_or_source_specific
    amount_semantics: table_specific_financial_amount; do not generalize by column name
    usable_for_filtering: false
    usable_for_grouping: false
    usable_for_metrics: true
    usable_for_joining: false
    usable_for_reconciliation: true
    evidence_refs:
    - evidence.logistics_kb_doc
    - evidence.cognee_design_v4
    - evidence.unified_edge_scope
```
```yaml
candidate_card:
  card_type: column
  card_id: column.zs_observe.shiprocket_invoice.charge_dl
  name: shiprocket_invoice.charge_dl
  fields:
    name: shiprocket_invoice.charge_dl
    description: Delivery charge.
    status: active
    confidence: curated
    source_documents:
    - Logistics KB Doc.docx
    - Cognee KB Design v4.md
    - logistics_gold_std_raw_md_frame_v3.md
    - logistics_gold_std_canonical_card_frame_v5.md
    created_by: kb_authoring_assistant
    updated_by: kb_authoring_assistant
    version: 5.0-manifest-aligned
    table_id: table.zs_observe.shiprocket_invoice
    column_name: charge_dl
    data_type: unknown
    semantic_roles: measure
    business_concepts:
    - Delivery charge.
    default_aggregation: SUM if financial measure else none
    sign_convention: positive_or_source_specific
    amount_semantics: table_specific_financial_amount; do not generalize by column name
    usable_for_filtering: false
    usable_for_grouping: false
    usable_for_metrics: true
    usable_for_joining: false
    usable_for_reconciliation: true
    evidence_refs:
    - evidence.logistics_kb_doc
    - evidence.cognee_design_v4
    - evidence.unified_edge_scope
```
```yaml
candidate_card:
  card_type: column
  card_id: column.zs_observe.shiprocket_invoice.final_weight
  name: shiprocket_invoice.final_weight
  fields:
    name: shiprocket_invoice.final_weight
    description: Actual/final weight.
    status: active
    confidence: curated
    source_documents:
    - Logistics KB Doc.docx
    - Cognee KB Design v4.md
    - logistics_gold_std_raw_md_frame_v3.md
    - logistics_gold_std_canonical_card_frame_v5.md
    created_by: kb_authoring_assistant
    updated_by: kb_authoring_assistant
    version: 5.0-manifest-aligned
    table_id: table.zs_observe.shiprocket_invoice
    column_name: final_weight
    data_type: unknown
    semantic_roles: measure
    business_concepts:
    - Actual/final weight.
    default_aggregation: SUM if financial measure else none
    sign_convention: positive_or_source_specific
    amount_semantics: table_specific_financial_amount; do not generalize by column name
    usable_for_filtering: false
    usable_for_grouping: false
    usable_for_metrics: true
    usable_for_joining: false
    usable_for_reconciliation: true
    evidence_refs:
    - evidence.logistics_kb_doc
    - evidence.cognee_design_v4
    - evidence.unified_edge_scope
```
```yaml
candidate_card:
  card_type: column
  card_id: column.zs_observe.shiprocket_invoice.charged_weight
  name: shiprocket_invoice.charged_weight
  fields:
    name: shiprocket_invoice.charged_weight
    description: Billable weight.
    status: active
    confidence: curated
    source_documents:
    - Logistics KB Doc.docx
    - Cognee KB Design v4.md
    - logistics_gold_std_raw_md_frame_v3.md
    - logistics_gold_std_canonical_card_frame_v5.md
    created_by: kb_authoring_assistant
    updated_by: kb_authoring_assistant
    version: 5.0-manifest-aligned
    table_id: table.zs_observe.shiprocket_invoice
    column_name: charged_weight
    data_type: unknown
    semantic_roles: measure
    business_concepts:
    - Billable weight.
    default_aggregation: SUM if financial measure else none
    sign_convention: positive_or_source_specific
    amount_semantics: table_specific_financial_amount; do not generalize by column name
    usable_for_filtering: false
    usable_for_grouping: false
    usable_for_metrics: true
    usable_for_joining: false
    usable_for_reconciliation: true
    evidence_refs:
    - evidence.logistics_kb_doc
    - evidence.cognee_design_v4
    - evidence.unified_edge_scope
```
```yaml
candidate_card:
  card_type: column
  card_id: column.zs_observe.shiprocket_invoice.settled_amount
  name: shiprocket_invoice.settled_amount
  fields:
    name: shiprocket_invoice.settled_amount
    description: Net freight settled after deductions.
    status: active
    confidence: curated
    source_documents:
    - Logistics KB Doc.docx
    - Cognee KB Design v4.md
    - logistics_gold_std_raw_md_frame_v3.md
    - logistics_gold_std_canonical_card_frame_v5.md
    created_by: kb_authoring_assistant
    updated_by: kb_authoring_assistant
    version: 5.0-manifest-aligned
    table_id: table.zs_observe.shiprocket_invoice
    column_name: settled_amount
    data_type: unknown
    semantic_roles: measure
    business_concepts:
    - Net freight settled after deductions.
    default_aggregation: SUM if financial measure else none
    sign_convention: positive_or_source_specific
    amount_semantics: table_specific_financial_amount; do not generalize by column name
    usable_for_filtering: false
    usable_for_grouping: false
    usable_for_metrics: true
    usable_for_joining: false
    usable_for_reconciliation: true
    evidence_refs:
    - evidence.logistics_kb_doc
    - evidence.cognee_design_v4
    - evidence.unified_edge_scope
```
```yaml
candidate_card:
  card_type: column
  card_id: column.zs_observe.shiprocket_invoice.referal_fee
  name: shiprocket_invoice.referal_fee
  fields:
    name: shiprocket_invoice.referal_fee
    description: Shiprocket referral/platform fee.
    status: active
    confidence: curated
    source_documents:
    - Logistics KB Doc.docx
    - Cognee KB Design v4.md
    - logistics_gold_std_raw_md_frame_v3.md
    - logistics_gold_std_canonical_card_frame_v5.md
    created_by: kb_authoring_assistant
    updated_by: kb_authoring_assistant
    version: 5.0-manifest-aligned
    table_id: table.zs_observe.shiprocket_invoice
    column_name: referal_fee
    data_type: unknown
    semantic_roles: measure
    business_concepts:
    - Shiprocket referral/platform fee.
    default_aggregation: SUM if financial measure else none
    sign_convention: positive_or_source_specific
    amount_semantics: not_applicable
    usable_for_filtering: false
    usable_for_grouping: false
    usable_for_metrics: true
    usable_for_joining: false
    usable_for_reconciliation: true
    evidence_refs:
    - evidence.logistics_kb_doc
    - evidence.cognee_design_v4
    - evidence.unified_edge_scope
```
```yaml
candidate_card:
  card_type: column
  card_id: column.zs_observe.shiprocket_invoice.mp_sin
  name: shiprocket_invoice.mp_sin
  fields:
    name: shiprocket_invoice.mp_sin
    description: Shiprocket internal order reference.
    status: active
    confidence: curated
    source_documents:
    - Logistics KB Doc.docx
    - Cognee KB Design v4.md
    - logistics_gold_std_raw_md_frame_v3.md
    - logistics_gold_std_canonical_card_frame_v5.md
    created_by: kb_authoring_assistant
    updated_by: kb_authoring_assistant
    version: 5.0-manifest-aligned
    table_id: table.zs_observe.shiprocket_invoice
    column_name: mp_sin
    data_type: unknown
    semantic_roles: identifier
    business_concepts:
    - Shiprocket internal order reference.
    default_aggregation: SUM if financial measure else none
    sign_convention: positive_or_source_specific
    amount_semantics: not_applicable
    usable_for_filtering: false
    usable_for_grouping: false
    usable_for_metrics: false
    usable_for_joining: true
    usable_for_reconciliation: false
    evidence_refs:
    - evidence.logistics_kb_doc
    - evidence.cognee_design_v4
    - evidence.unified_edge_scope
```
```yaml
candidate_card:
  card_type: column
  card_id: column.zs_observe.shiprocket_invoice.source_zipcode
  name: shiprocket_invoice.source_zipcode
  fields:
    name: shiprocket_invoice.source_zipcode
    description: Origin pincode.
    status: active
    confidence: curated
    source_documents:
    - Logistics KB Doc.docx
    - Cognee KB Design v4.md
    - logistics_gold_std_raw_md_frame_v3.md
    - logistics_gold_std_canonical_card_frame_v5.md
    created_by: kb_authoring_assistant
    updated_by: kb_authoring_assistant
    version: 5.0-manifest-aligned
    table_id: table.zs_observe.shiprocket_invoice
    column_name: source_zipcode
    data_type: unknown
    semantic_roles: dimension
    business_concepts:
    - Origin pincode.
    default_aggregation: SUM if financial measure else none
    sign_convention: positive_or_source_specific
    amount_semantics: not_applicable
    usable_for_filtering: true
    usable_for_grouping: true
    usable_for_metrics: false
    usable_for_joining: false
    usable_for_reconciliation: false
    evidence_refs:
    - evidence.logistics_kb_doc
    - evidence.cognee_design_v4
    - evidence.unified_edge_scope
```
```yaml
candidate_card:
  card_type: column
  card_id: column.zs_observe.shiprocket_invoice.destination_zipcode
  name: shiprocket_invoice.destination_zipcode
  fields:
    name: shiprocket_invoice.destination_zipcode
    description: Destination pincode.
    status: active
    confidence: curated
    source_documents:
    - Logistics KB Doc.docx
    - Cognee KB Design v4.md
    - logistics_gold_std_raw_md_frame_v3.md
    - logistics_gold_std_canonical_card_frame_v5.md
    created_by: kb_authoring_assistant
    updated_by: kb_authoring_assistant
    version: 5.0-manifest-aligned
    table_id: table.zs_observe.shiprocket_invoice
    column_name: destination_zipcode
    data_type: unknown
    semantic_roles: dimension
    business_concepts:
    - Destination pincode.
    default_aggregation: SUM if financial measure else none
    sign_convention: positive_or_source_specific
    amount_semantics: not_applicable
    usable_for_filtering: true
    usable_for_grouping: true
    usable_for_metrics: false
    usable_for_joining: false
    usable_for_reconciliation: false
    evidence_refs:
    - evidence.logistics_kb_doc
    - evidence.cognee_design_v4
    - evidence.unified_edge_scope
```
```yaml
candidate_card:
  card_type: column
  card_id: column.zs_observe.shiprocket_invoice.is_active
  name: shiprocket_invoice.is_active
  fields:
    name: shiprocket_invoice.is_active
    description: Active row flag.
    status: active
    confidence: curated
    source_documents:
    - Logistics KB Doc.docx
    - Cognee KB Design v4.md
    - logistics_gold_std_raw_md_frame_v3.md
    - logistics_gold_std_canonical_card_frame_v5.md
    created_by: kb_authoring_assistant
    updated_by: kb_authoring_assistant
    version: 5.0-manifest-aligned
    table_id: table.zs_observe.shiprocket_invoice
    column_name: is_active
    data_type: unknown
    semantic_roles: filter
    business_concepts:
    - Active row flag.
    default_aggregation: SUM if financial measure else none
    sign_convention: positive_or_source_specific
    amount_semantics: not_applicable
    usable_for_filtering: true
    usable_for_grouping: false
    usable_for_metrics: false
    usable_for_joining: false
    usable_for_reconciliation: false
    evidence_refs:
    - evidence.logistics_kb_doc
    - evidence.cognee_design_v4
    - evidence.unified_edge_scope
```
```yaml
candidate_card:
  card_type: column
  card_id: column.zs_observe.shiprocket_invoice.group_level_id
  name: shiprocket_invoice.group_level_id
  fields:
    name: shiprocket_invoice.group_level_id
    description: Observed account/group scope candidate.
    status: active
    confidence: curated
    source_documents:
    - Logistics KB Doc.docx
    - Cognee KB Design v4.md
    - logistics_gold_std_raw_md_frame_v3.md
    - logistics_gold_std_canonical_card_frame_v5.md
    created_by: kb_authoring_assistant
    updated_by: kb_authoring_assistant
    version: 5.0-manifest-aligned
    table_id: table.zs_observe.shiprocket_invoice
    column_name: group_level_id
    data_type: unknown
    semantic_roles: scope_filter
    business_concepts:
    - Observed account/group scope candidate.
    default_aggregation: SUM if financial measure else none
    sign_convention: positive_or_source_specific
    amount_semantics: not_applicable
    usable_for_filtering: true
    usable_for_grouping: false
    usable_for_metrics: false
    usable_for_joining: false
    usable_for_reconciliation: false
    evidence_refs:
    - evidence.logistics_kb_doc
    - evidence.cognee_design_v4
    - evidence.unified_edge_scope
```
```yaml
candidate_card:
  card_type: column
  card_id: column.zs_observe.shiprocket_settlement.order_id
  name: shiprocket_settlement.order_id
  fields:
    name: shiprocket_settlement.order_id
    description: Shiprocket order ID.
    status: active
    confidence: curated
    source_documents:
    - Logistics KB Doc.docx
    - Cognee KB Design v4.md
    - logistics_gold_std_raw_md_frame_v3.md
    - logistics_gold_std_canonical_card_frame_v5.md
    created_by: kb_authoring_assistant
    updated_by: kb_authoring_assistant
    version: 5.0-manifest-aligned
    table_id: table.zs_observe.shiprocket_settlement
    column_name: order_id
    data_type: unknown
    semantic_roles: identifier
    business_concepts:
    - Shiprocket order ID.
    default_aggregation: SUM if financial measure else none
    sign_convention: positive_or_source_specific
    amount_semantics: not_applicable
    usable_for_filtering: false
    usable_for_grouping: false
    usable_for_metrics: false
    usable_for_joining: true
    usable_for_reconciliation: false
    evidence_refs:
    - evidence.logistics_kb_doc
    - evidence.cognee_design_v4
    - evidence.unified_edge_scope
```
```yaml
candidate_card:
  card_type: column
  card_id: column.zs_observe.shiprocket_settlement.awb_number
  name: shiprocket_settlement.awb_number
  fields:
    name: shiprocket_settlement.awb_number
    description: AWB; joins to shiprocket_oms.awb_code and shiprocket_invoice.other_id.
    status: active
    confidence: curated
    source_documents:
    - Logistics KB Doc.docx
    - Cognee KB Design v4.md
    - logistics_gold_std_raw_md_frame_v3.md
    - logistics_gold_std_canonical_card_frame_v5.md
    created_by: kb_authoring_assistant
    updated_by: kb_authoring_assistant
    version: 5.0-manifest-aligned
    table_id: table.zs_observe.shiprocket_settlement
    column_name: awb_number
    data_type: unknown
    semantic_roles: identifier;join_key;reconciliation_key
    business_concepts:
    - AWB
    - joins to shiprocket_oms.awb_code and shiprocket_invoice.other_id.
    default_aggregation: SUM if financial measure else none
    sign_convention: positive_or_source_specific
    amount_semantics: not_applicable
    usable_for_filtering: false
    usable_for_grouping: false
    usable_for_metrics: false
    usable_for_joining: true
    usable_for_reconciliation: true
    evidence_refs:
    - evidence.logistics_kb_doc
    - evidence.cognee_design_v4
    - evidence.unified_edge_scope
```
```yaml
candidate_card:
  card_type: column
  card_id: column.zs_observe.shiprocket_settlement.courier_partner
  name: shiprocket_settlement.courier_partner
  fields:
    name: shiprocket_settlement.courier_partner
    description: Courier that collected COD.
    status: active
    confidence: curated
    source_documents:
    - Logistics KB Doc.docx
    - Cognee KB Design v4.md
    - logistics_gold_std_raw_md_frame_v3.md
    - logistics_gold_std_canonical_card_frame_v5.md
    created_by: kb_authoring_assistant
    updated_by: kb_authoring_assistant
    version: 5.0-manifest-aligned
    table_id: table.zs_observe.shiprocket_settlement
    column_name: courier_partner
    data_type: unknown
    semantic_roles: dimension;filter
    business_concepts:
    - Courier that collected COD.
    default_aggregation: SUM if financial measure else none
    sign_convention: positive_or_source_specific
    amount_semantics: not_applicable
    usable_for_filtering: true
    usable_for_grouping: true
    usable_for_metrics: false
    usable_for_joining: false
    usable_for_reconciliation: false
    evidence_refs:
    - evidence.logistics_kb_doc
    - evidence.cognee_design_v4
    - evidence.unified_edge_scope
```
```yaml
candidate_card:
  card_type: column
  card_id: column.zs_observe.shiprocket_settlement.charged_amount
  name: shiprocket_settlement.charged_amount
  fields:
    name: shiprocket_settlement.charged_amount
    description: COD amount collected/remitted from customer.
    status: active
    confidence: curated
    source_documents:
    - Logistics KB Doc.docx
    - Cognee KB Design v4.md
    - logistics_gold_std_raw_md_frame_v3.md
    - logistics_gold_std_canonical_card_frame_v5.md
    created_by: kb_authoring_assistant
    updated_by: kb_authoring_assistant
    version: 5.0-manifest-aligned
    table_id: table.zs_observe.shiprocket_settlement
    column_name: charged_amount
    data_type: unknown
    semantic_roles: measure
    business_concepts:
    - COD amount collected/remitted from customer.
    default_aggregation: SUM if financial measure else none
    sign_convention: positive_or_source_specific
    amount_semantics: cod_collected_or_remitted_amount
    usable_for_filtering: false
    usable_for_grouping: false
    usable_for_metrics: true
    usable_for_joining: false
    usable_for_reconciliation: true
    evidence_refs:
    - evidence.logistics_kb_doc
    - evidence.cognee_design_v4
    - evidence.unified_edge_scope
```
```yaml
candidate_card:
  card_type: column
  card_id: column.zs_observe.shiprocket_settlement.delivered_date
  name: shiprocket_settlement.delivered_date
  fields:
    name: shiprocket_settlement.delivered_date
    description: Date of delivery.
    status: active
    confidence: curated
    source_documents:
    - Logistics KB Doc.docx
    - Cognee KB Design v4.md
    - logistics_gold_std_raw_md_frame_v3.md
    - logistics_gold_std_canonical_card_frame_v5.md
    created_by: kb_authoring_assistant
    updated_by: kb_authoring_assistant
    version: 5.0-manifest-aligned
    table_id: table.zs_observe.shiprocket_settlement
    column_name: delivered_date
    data_type: unknown
    semantic_roles: date
    business_concepts:
    - Date of delivery.
    default_aggregation: SUM if financial measure else none
    sign_convention: positive_or_source_specific
    amount_semantics: not_applicable
    usable_for_filtering: false
    usable_for_grouping: false
    usable_for_metrics: false
    usable_for_joining: false
    usable_for_reconciliation: false
    evidence_refs:
    - evidence.logistics_kb_doc
    - evidence.cognee_design_v4
    - evidence.unified_edge_scope
```
```yaml
candidate_card:
  card_type: column
  card_id: column.zs_observe.shiprocket_settlement.settlement_date
  name: shiprocket_settlement.settlement_date
  fields:
    name: shiprocket_settlement.settlement_date
    description: COD settlement/remittance date.
    status: active
    confidence: curated
    source_documents:
    - Logistics KB Doc.docx
    - Cognee KB Design v4.md
    - logistics_gold_std_raw_md_frame_v3.md
    - logistics_gold_std_canonical_card_frame_v5.md
    created_by: kb_authoring_assistant
    updated_by: kb_authoring_assistant
    version: 5.0-manifest-aligned
    table_id: table.zs_observe.shiprocket_settlement
    column_name: settlement_date
    data_type: unknown
    semantic_roles: date
    business_concepts:
    - COD settlement/remittance date.
    default_aggregation: SUM if financial measure else none
    sign_convention: positive_or_source_specific
    amount_semantics: not_applicable
    usable_for_filtering: false
    usable_for_grouping: false
    usable_for_metrics: false
    usable_for_joining: false
    usable_for_reconciliation: false
    evidence_refs:
    - evidence.logistics_kb_doc
    - evidence.cognee_design_v4
    - evidence.unified_edge_scope
```
```yaml
candidate_card:
  card_type: column
  card_id: column.zs_observe.shiprocket_settlement.is_active
  name: shiprocket_settlement.is_active
  fields:
    name: shiprocket_settlement.is_active
    description: Active row flag.
    status: active
    confidence: curated
    source_documents:
    - Logistics KB Doc.docx
    - Cognee KB Design v4.md
    - logistics_gold_std_raw_md_frame_v3.md
    - logistics_gold_std_canonical_card_frame_v5.md
    created_by: kb_authoring_assistant
    updated_by: kb_authoring_assistant
    version: 5.0-manifest-aligned
    table_id: table.zs_observe.shiprocket_settlement
    column_name: is_active
    data_type: unknown
    semantic_roles: filter
    business_concepts:
    - Active row flag.
    default_aggregation: SUM if financial measure else none
    sign_convention: positive_or_source_specific
    amount_semantics: not_applicable
    usable_for_filtering: true
    usable_for_grouping: false
    usable_for_metrics: false
    usable_for_joining: false
    usable_for_reconciliation: false
    evidence_refs:
    - evidence.logistics_kb_doc
    - evidence.cognee_design_v4
    - evidence.unified_edge_scope
```
```yaml
candidate_card:
  card_type: column
  card_id: column.zs_observe.shiprocket_settlement.group_level_id
  name: shiprocket_settlement.group_level_id
  fields:
    name: shiprocket_settlement.group_level_id
    description: Observed account/group scope candidate.
    status: active
    confidence: curated
    source_documents:
    - Logistics KB Doc.docx
    - Cognee KB Design v4.md
    - logistics_gold_std_raw_md_frame_v3.md
    - logistics_gold_std_canonical_card_frame_v5.md
    created_by: kb_authoring_assistant
    updated_by: kb_authoring_assistant
    version: 5.0-manifest-aligned
    table_id: table.zs_observe.shiprocket_settlement
    column_name: group_level_id
    data_type: unknown
    semantic_roles: scope_filter
    business_concepts:
    - Observed account/group scope candidate.
    default_aggregation: SUM if financial measure else none
    sign_convention: positive_or_source_specific
    amount_semantics: not_applicable
    usable_for_filtering: true
    usable_for_grouping: false
    usable_for_metrics: false
    usable_for_joining: false
    usable_for_reconciliation: false
    evidence_refs:
    - evidence.logistics_kb_doc
    - evidence.cognee_design_v4
    - evidence.unified_edge_scope
```
```yaml
candidate_card:
  card_type: column
  card_id: column.zs_observe.shiprocket_settlement_report.order_id
  name: shiprocket_settlement_report.order_id
  fields:
    name: shiprocket_settlement_report.order_id
    description: Order reference.
    status: active
    confidence: curated
    source_documents:
    - Logistics KB Doc.docx
    - Cognee KB Design v4.md
    - logistics_gold_std_raw_md_frame_v3.md
    - logistics_gold_std_canonical_card_frame_v5.md
    created_by: kb_authoring_assistant
    updated_by: kb_authoring_assistant
    version: 5.0-manifest-aligned
    table_id: table.zs_observe.shiprocket_settlement_report
    column_name: order_id
    data_type: unknown
    semantic_roles: identifier
    business_concepts:
    - Order reference.
    default_aggregation: SUM if financial measure else none
    sign_convention: positive_or_source_specific
    amount_semantics: not_applicable
    usable_for_filtering: false
    usable_for_grouping: false
    usable_for_metrics: false
    usable_for_joining: true
    usable_for_reconciliation: false
    evidence_refs:
    - evidence.logistics_kb_doc
    - evidence.cognee_design_v4
    - evidence.unified_edge_scope
```
```yaml
candidate_card:
  card_type: column
  card_id: column.zs_observe.shiprocket_settlement_report.courier_partner
  name: shiprocket_settlement_report.courier_partner
  fields:
    name: shiprocket_settlement_report.courier_partner
    description: Courier name.
    status: active
    confidence: curated
    source_documents:
    - Logistics KB Doc.docx
    - Cognee KB Design v4.md
    - logistics_gold_std_raw_md_frame_v3.md
    - logistics_gold_std_canonical_card_frame_v5.md
    created_by: kb_authoring_assistant
    updated_by: kb_authoring_assistant
    version: 5.0-manifest-aligned
    table_id: table.zs_observe.shiprocket_settlement_report
    column_name: courier_partner
    data_type: unknown
    semantic_roles: dimension
    business_concepts:
    - Courier name.
    default_aggregation: SUM if financial measure else none
    sign_convention: positive_or_source_specific
    amount_semantics: not_applicable
    usable_for_filtering: true
    usable_for_grouping: true
    usable_for_metrics: false
    usable_for_joining: false
    usable_for_reconciliation: false
    evidence_refs:
    - evidence.logistics_kb_doc
    - evidence.cognee_design_v4
    - evidence.unified_edge_scope
```
```yaml
candidate_card:
  card_type: column
  card_id: column.zs_observe.shiprocket_settlement_report.awb_remittance_status
  name: shiprocket_settlement_report.awb_remittance_status
  fields:
    name: shiprocket_settlement_report.awb_remittance_status
    description: Status of AWB-level remittance.
    status: active
    confidence: curated
    source_documents:
    - Logistics KB Doc.docx
    - Cognee KB Design v4.md
    - logistics_gold_std_raw_md_frame_v3.md
    - logistics_gold_std_canonical_card_frame_v5.md
    created_by: kb_authoring_assistant
    updated_by: kb_authoring_assistant
    version: 5.0-manifest-aligned
    table_id: table.zs_observe.shiprocket_settlement_report
    column_name: awb_remittance_status
    data_type: unknown
    semantic_roles: status
    business_concepts:
    - Status of AWB-level remittance.
    default_aggregation: SUM if financial measure else none
    sign_convention: positive_or_source_specific
    amount_semantics: not_applicable
    usable_for_filtering: true
    usable_for_grouping: true
    usable_for_metrics: false
    usable_for_joining: false
    usable_for_reconciliation: false
    evidence_refs:
    - evidence.logistics_kb_doc
    - evidence.cognee_design_v4
    - evidence.unified_edge_scope
```
```yaml
candidate_card:
  card_type: column
  card_id: column.zs_observe.shiprocket_settlement_report.courier_received_amount
  name: shiprocket_settlement_report.courier_received_amount
  fields:
    name: shiprocket_settlement_report.courier_received_amount
    description: Amount courier received versus expected.
    status: active
    confidence: curated
    source_documents:
    - Logistics KB Doc.docx
    - Cognee KB Design v4.md
    - logistics_gold_std_raw_md_frame_v3.md
    - logistics_gold_std_canonical_card_frame_v5.md
    created_by: kb_authoring_assistant
    updated_by: kb_authoring_assistant
    version: 5.0-manifest-aligned
    table_id: table.zs_observe.shiprocket_settlement_report
    column_name: courier_received_amount
    data_type: unknown
    semantic_roles: measure
    business_concepts:
    - Amount courier received versus expected.
    default_aggregation: SUM if financial measure else none
    sign_convention: positive_or_source_specific
    amount_semantics: table_specific_financial_amount; do not generalize by column name
    usable_for_filtering: false
    usable_for_grouping: false
    usable_for_metrics: true
    usable_for_joining: false
    usable_for_reconciliation: true
    evidence_refs:
    - evidence.logistics_kb_doc
    - evidence.cognee_design_v4
    - evidence.unified_edge_scope
```
```yaml
candidate_card:
  card_type: column
  card_id: column.zs_observe.shiprocket_settlement_report.settlement_id
  name: shiprocket_settlement_report.settlement_id
  fields:
    name: shiprocket_settlement_report.settlement_id
    description: Batch settlement identifier.
    status: active
    confidence: curated
    source_documents:
    - Logistics KB Doc.docx
    - Cognee KB Design v4.md
    - logistics_gold_std_raw_md_frame_v3.md
    - logistics_gold_std_canonical_card_frame_v5.md
    created_by: kb_authoring_assistant
    updated_by: kb_authoring_assistant
    version: 5.0-manifest-aligned
    table_id: table.zs_observe.shiprocket_settlement_report
    column_name: settlement_id
    data_type: unknown
    semantic_roles: identifier
    business_concepts:
    - Batch settlement identifier.
    default_aggregation: SUM if financial measure else none
    sign_convention: positive_or_source_specific
    amount_semantics: not_applicable
    usable_for_filtering: false
    usable_for_grouping: false
    usable_for_metrics: false
    usable_for_joining: true
    usable_for_reconciliation: false
    evidence_refs:
    - evidence.logistics_kb_doc
    - evidence.cognee_design_v4
    - evidence.unified_edge_scope
```
```yaml
candidate_card:
  card_type: column
  card_id: column.zs_observe.shiprocket_settlement_report.source_gst_name
  name: shiprocket_settlement_report.source_gst_name
  fields:
    name: shiprocket_settlement_report.source_gst_name
    description: GST entity name.
    status: active
    confidence: curated
    source_documents:
    - Logistics KB Doc.docx
    - Cognee KB Design v4.md
    - logistics_gold_std_raw_md_frame_v3.md
    - logistics_gold_std_canonical_card_frame_v5.md
    created_by: kb_authoring_assistant
    updated_by: kb_authoring_assistant
    version: 5.0-manifest-aligned
    table_id: table.zs_observe.shiprocket_settlement_report
    column_name: source_gst_name
    data_type: unknown
    semantic_roles: dimension
    business_concepts:
    - GST entity name.
    default_aggregation: SUM if financial measure else none
    sign_convention: positive_or_source_specific
    amount_semantics: not_applicable
    usable_for_filtering: true
    usable_for_grouping: true
    usable_for_metrics: false
    usable_for_joining: false
    usable_for_reconciliation: false
    evidence_refs:
    - evidence.logistics_kb_doc
    - evidence.cognee_design_v4
    - evidence.unified_edge_scope
```
```yaml
candidate_card:
  card_type: column
  card_id: column.zs_observe.shiprocket_settlement_report.source_gst_id
  name: shiprocket_settlement_report.source_gst_id
  fields:
    name: shiprocket_settlement_report.source_gst_id
    description: GST identifier.
    status: active
    confidence: curated
    source_documents:
    - Logistics KB Doc.docx
    - Cognee KB Design v4.md
    - logistics_gold_std_raw_md_frame_v3.md
    - logistics_gold_std_canonical_card_frame_v5.md
    created_by: kb_authoring_assistant
    updated_by: kb_authoring_assistant
    version: 5.0-manifest-aligned
    table_id: table.zs_observe.shiprocket_settlement_report
    column_name: source_gst_id
    data_type: unknown
    semantic_roles: identifier
    business_concepts:
    - GST identifier.
    default_aggregation: SUM if financial measure else none
    sign_convention: positive_or_source_specific
    amount_semantics: not_applicable
    usable_for_filtering: false
    usable_for_grouping: false
    usable_for_metrics: false
    usable_for_joining: true
    usable_for_reconciliation: false
    evidence_refs:
    - evidence.logistics_kb_doc
    - evidence.cognee_design_v4
    - evidence.unified_edge_scope
```
```yaml
candidate_card:
  card_type: column
  card_id: column.zs_observe.shiprocket_settlement_report.offer_adjustment_settled_amount
  name: shiprocket_settlement_report.offer_adjustment_settled_amount
  fields:
    name: shiprocket_settlement_report.offer_adjustment_settled_amount
    description: Offer adjustment amount settled.
    status: active
    confidence: curated
    source_documents:
    - Logistics KB Doc.docx
    - Cognee KB Design v4.md
    - logistics_gold_std_raw_md_frame_v3.md
    - logistics_gold_std_canonical_card_frame_v5.md
    created_by: kb_authoring_assistant
    updated_by: kb_authoring_assistant
    version: 5.0-manifest-aligned
    table_id: table.zs_observe.shiprocket_settlement_report
    column_name: offer_adjustment_settled_amount
    data_type: unknown
    semantic_roles: measure
    business_concepts:
    - Offer adjustment amount settled.
    default_aggregation: SUM if financial measure else none
    sign_convention: positive_or_source_specific
    amount_semantics: table_specific_financial_amount; do not generalize by column name
    usable_for_filtering: false
    usable_for_grouping: false
    usable_for_metrics: true
    usable_for_joining: false
    usable_for_reconciliation: true
    evidence_refs:
    - evidence.logistics_kb_doc
    - evidence.cognee_design_v4
    - evidence.unified_edge_scope
```
```yaml
candidate_card:
  card_type: column
  card_id: column.zs_observe.shiprocket_settlement_report.parent_id
  name: shiprocket_settlement_report.parent_id
  fields:
    name: shiprocket_settlement_report.parent_id
    description: Parent order reference.
    status: active
    confidence: curated
    source_documents:
    - Logistics KB Doc.docx
    - Cognee KB Design v4.md
    - logistics_gold_std_raw_md_frame_v3.md
    - logistics_gold_std_canonical_card_frame_v5.md
    created_by: kb_authoring_assistant
    updated_by: kb_authoring_assistant
    version: 5.0-manifest-aligned
    table_id: table.zs_observe.shiprocket_settlement_report
    column_name: parent_id
    data_type: unknown
    semantic_roles: identifier
    business_concepts:
    - Parent order reference.
    default_aggregation: SUM if financial measure else none
    sign_convention: positive_or_source_specific
    amount_semantics: not_applicable
    usable_for_filtering: false
    usable_for_grouping: false
    usable_for_metrics: false
    usable_for_joining: true
    usable_for_reconciliation: false
    evidence_refs:
    - evidence.logistics_kb_doc
    - evidence.cognee_design_v4
    - evidence.unified_edge_scope
```

### 4.6 relationship cards

```yaml
candidate_card:
  card_type: relationship
  card_id: relationship.shiprocket_oms.shiprocket_invoice.awb
  name: shiprocket_oms to shiprocket_invoice by awb
  fields:
    name: shiprocket_oms to shiprocket_invoice by awb
    description: Validate shipments have freight invoice evidence.
    status: active
    confidence: curated
    source_documents:
    - Logistics KB Doc.docx
    - Cognee KB Design v4.md
    - logistics_gold_std_raw_md_frame_v3.md
    - logistics_gold_std_canonical_card_frame_v5.md
    created_by: kb_authoring_assistant
    updated_by: kb_authoring_assistant
    version: 5.0-manifest-aligned
    source_table: table.zs_observe.shiprocket_oms
    target_table: table.zs_observe.shiprocket_invoice
    relationship_type: join; reconciliation_relation
    join_keys: awb_code = other_id
    cardinality: one_to_zero_or_many
    join_type_recommendation: left_join for diagnostics; inner_join for matched-only analysis
    business_use: Validate shipments have freight invoice evidence.
    safe_for_metrics: false unless pre-aggregated
    safe_for_reconciliation: true
    aggregation_risk: pre-aggregate to reconciliation unit before joining; avoid fanout
    evidence_refs:
    - evidence.logistics_kb_doc
    - evidence.cognee_design_v4
    - evidence.unified_edge_scope
```
```yaml
candidate_card:
  card_type: relationship
  card_id: relationship.shiprocket_oms.shiprocket_settlement.awb
  name: shiprocket_oms to shiprocket_settlement by awb
  fields:
    name: shiprocket_oms to shiprocket_settlement by awb
    description: Validate COD shipments have COD settlement evidence.
    status: active
    confidence: curated
    source_documents:
    - Logistics KB Doc.docx
    - Cognee KB Design v4.md
    - logistics_gold_std_raw_md_frame_v3.md
    - logistics_gold_std_canonical_card_frame_v5.md
    created_by: kb_authoring_assistant
    updated_by: kb_authoring_assistant
    version: 5.0-manifest-aligned
    source_table: table.zs_observe.shiprocket_oms
    target_table: table.zs_observe.shiprocket_settlement
    relationship_type: join; reconciliation_relation
    join_keys: awb_code = awb_number
    cardinality: one_to_zero_or_many
    join_type_recommendation: left_join for diagnostics; inner_join for matched-only analysis
    business_use: Validate COD shipments have COD settlement evidence.
    safe_for_metrics: false unless pre-aggregated
    safe_for_reconciliation: true
    aggregation_risk: pre-aggregate to reconciliation unit before joining; avoid fanout
    evidence_refs:
    - evidence.logistics_kb_doc
    - evidence.cognee_design_v4
    - evidence.unified_edge_scope
```
```yaml
candidate_card:
  card_type: relationship
  card_id: relationship.shiprocket_invoice.shiprocket_settlement.awb
  name: shiprocket_invoice to shiprocket_settlement by awb
  fields:
    name: shiprocket_invoice to shiprocket_settlement by awb
    description: Cross-check freight invoice and COD settlement for same AWB.
    status: active
    confidence: curated
    source_documents:
    - Logistics KB Doc.docx
    - Cognee KB Design v4.md
    - logistics_gold_std_raw_md_frame_v3.md
    - logistics_gold_std_canonical_card_frame_v5.md
    created_by: kb_authoring_assistant
    updated_by: kb_authoring_assistant
    version: 5.0-manifest-aligned
    source_table: table.zs_observe.shiprocket_invoice
    target_table: table.zs_observe.shiprocket_settlement
    relationship_type: join; reconciliation_relation
    join_keys: other_id = awb_number
    cardinality: one_to_zero_or_many
    join_type_recommendation: left_join for diagnostics; inner_join for matched-only analysis
    business_use: Cross-check freight invoice and COD settlement for same AWB.
    safe_for_metrics: false unless pre-aggregated
    safe_for_reconciliation: true
    aggregation_risk: pre-aggregate to reconciliation unit before joining; avoid fanout
    evidence_refs:
    - evidence.logistics_kb_doc
    - evidence.cognee_design_v4
    - evidence.unified_edge_scope
```
```yaml
candidate_card:
  card_type: relationship
  card_id: relationship.shiprocket_settlement.delhivery_settlement.awb
  name: shiprocket_settlement to delhivery_settlement by awb
  fields:
    name: shiprocket_settlement to delhivery_settlement by awb
    description: Compare Shiprocket aggregated Delhivery COD to direct Delhivery settlement.
    status: active
    confidence: curated
    source_documents:
    - Logistics KB Doc.docx
    - Cognee KB Design v4.md
    - logistics_gold_std_raw_md_frame_v3.md
    - logistics_gold_std_canonical_card_frame_v5.md
    created_by: kb_authoring_assistant
    updated_by: kb_authoring_assistant
    version: 5.0-manifest-aligned
    source_table: table.zs_observe.shiprocket_settlement
    target_table: table.zs_observe.delhivery_settlement
    relationship_type: join; reconciliation_relation
    join_keys: awb_number = waybill_num
    cardinality: one_to_zero_or_many
    join_type_recommendation: left_join for diagnostics; inner_join for matched-only analysis
    business_use: Compare Shiprocket aggregated Delhivery COD to direct Delhivery settlement.
    safe_for_metrics: false unless pre-aggregated
    safe_for_reconciliation: true
    aggregation_risk: pre-aggregate to reconciliation unit before joining; avoid fanout
    evidence_refs:
    - evidence.logistics_kb_doc
    - evidence.cognee_design_v4
    - evidence.unified_edge_scope
```
```yaml
candidate_card:
  card_type: relationship
  card_id: relationship.shiprocket_invoice.dtdc_settlement.awb
  name: shiprocket_invoice to dtdc_settlement by awb
  fields:
    name: shiprocket_invoice to dtdc_settlement by awb
    description: Cross-check Shiprocket DTDC freight invoices with DTDC COD settlement.
    status: active
    confidence: curated
    source_documents:
    - Logistics KB Doc.docx
    - Cognee KB Design v4.md
    - logistics_gold_std_raw_md_frame_v3.md
    - logistics_gold_std_canonical_card_frame_v5.md
    created_by: kb_authoring_assistant
    updated_by: kb_authoring_assistant
    version: 5.0-manifest-aligned
    source_table: table.zs_observe.shiprocket_invoice
    target_table: table.zs_observe.dtdc_settlement
    relationship_type: join; reconciliation_relation
    join_keys: other_id = airwaybill_number
    cardinality: one_to_zero_or_many
    join_type_recommendation: left_join for diagnostics; inner_join for matched-only analysis
    business_use: Cross-check Shiprocket DTDC freight invoices with DTDC COD settlement.
    safe_for_metrics: false unless pre-aggregated
    safe_for_reconciliation: true
    aggregation_risk: pre-aggregate to reconciliation unit before joining; avoid fanout
    evidence_refs:
    - evidence.logistics_kb_doc
    - evidence.cognee_design_v4
    - evidence.unified_edge_scope
```
```yaml
candidate_card:
  card_type: relationship
  card_id: relationship.shiprocket_invoice.ekart_settlement.awb
  name: shiprocket_invoice to ekart_settlement by awb
  fields:
    name: shiprocket_invoice to ekart_settlement by awb
    description: Cross-check Shiprocket Ekart freight rows to Ekart settlement when present.
    status: active
    confidence: curated
    source_documents:
    - Logistics KB Doc.docx
    - Cognee KB Design v4.md
    - logistics_gold_std_raw_md_frame_v3.md
    - logistics_gold_std_canonical_card_frame_v5.md
    created_by: kb_authoring_assistant
    updated_by: kb_authoring_assistant
    version: 5.0-manifest-aligned
    source_table: table.zs_observe.shiprocket_invoice
    target_table: table.zs_observe.ekart_settlement
    relationship_type: join; reconciliation_relation
    join_keys: other_id = shipment_id
    cardinality: one_to_zero_or_many
    join_type_recommendation: left_join for diagnostics; inner_join for matched-only analysis
    business_use: Cross-check Shiprocket Ekart freight rows to Ekart settlement when present.
    safe_for_metrics: false unless pre-aggregated
    safe_for_reconciliation: true
    aggregation_risk: pre-aggregate to reconciliation unit before joining; avoid fanout
    evidence_refs:
    - evidence.logistics_kb_doc
    - evidence.cognee_design_v4
    - evidence.unified_edge_scope
```
```yaml
candidate_card:
  card_type: relationship
  card_id: relationship.shiprocket_settlement.xpressbees_settlement.awb
  name: shiprocket_settlement to xpressbees_settlement by awb
  fields:
    name: shiprocket_settlement to xpressbees_settlement by awb
    description: Compare Shiprocket XpressBees COD fallback with sparse native table.
    status: active
    confidence: curated
    source_documents:
    - Logistics KB Doc.docx
    - Cognee KB Design v4.md
    - logistics_gold_std_raw_md_frame_v3.md
    - logistics_gold_std_canonical_card_frame_v5.md
    created_by: kb_authoring_assistant
    updated_by: kb_authoring_assistant
    version: 5.0-manifest-aligned
    source_table: table.zs_observe.shiprocket_settlement
    target_table: table.zs_observe.xpressbees_settlement
    relationship_type: join; reconciliation_relation
    join_keys: awb_number = shipping_id
    cardinality: one_to_zero_or_many
    join_type_recommendation: left_join for diagnostics; inner_join for matched-only analysis
    business_use: Compare Shiprocket XpressBees COD fallback with sparse native table.
    safe_for_metrics: false unless pre-aggregated
    safe_for_reconciliation: true
    aggregation_risk: pre-aggregate to reconciliation unit before joining; avoid fanout
    evidence_refs:
    - evidence.logistics_kb_doc
    - evidence.cognee_design_v4
    - evidence.unified_edge_scope
```
```yaml
candidate_card:
  card_type: relationship
  card_id: relationship.shiprocket_invoice.xpressbees_settlement.awb
  name: shiprocket_invoice to xpressbees_settlement by awb
  fields:
    name: shiprocket_invoice to xpressbees_settlement by awb
    description: Cross-check Shiprocket XpressBees freight with sparse native table.
    status: active
    confidence: curated
    source_documents:
    - Logistics KB Doc.docx
    - Cognee KB Design v4.md
    - logistics_gold_std_raw_md_frame_v3.md
    - logistics_gold_std_canonical_card_frame_v5.md
    created_by: kb_authoring_assistant
    updated_by: kb_authoring_assistant
    version: 5.0-manifest-aligned
    source_table: table.zs_observe.shiprocket_invoice
    target_table: table.zs_observe.xpressbees_settlement
    relationship_type: join; reconciliation_relation
    join_keys: other_id = shipping_id
    cardinality: one_to_zero_or_many
    join_type_recommendation: left_join for diagnostics; inner_join for matched-only analysis
    business_use: Cross-check Shiprocket XpressBees freight with sparse native table.
    safe_for_metrics: false unless pre-aggregated
    safe_for_reconciliation: true
    aggregation_risk: pre-aggregate to reconciliation unit before joining; avoid fanout
    evidence_refs:
    - evidence.logistics_kb_doc
    - evidence.cognee_design_v4
    - evidence.unified_edge_scope
```

### 4.7 value_profile cards

```yaml
candidate_card:
  card_type: value_profile
  card_id: value_profile.shiprocket_invoice.courier_partner
  name: shiprocket_invoice.courier_partner Value Profile
  fields:
    name: shiprocket_invoice.courier_partner Value Profile
    description: Known values and meanings for shiprocket_invoice.courier_partner.
    status: active
    confidence: curated
    source_documents:
    - Logistics KB Doc.docx
    - Cognee KB Design v4.md
    - logistics_gold_std_raw_md_frame_v3.md
    - logistics_gold_std_canonical_card_frame_v5.md
    created_by: kb_authoring_assistant
    updated_by: kb_authoring_assistant
    version: 5.0-manifest-aligned
    table_id: table.zs_observe.shiprocket_invoice
    column_id: column.zs_observe.shiprocket_invoice.courier_partner
    value_type: enum_or_enum_with_nulls
    values: DTDC Air 500gm=DTDC via Shiprocket (dtdc); Delhivery Air=Delhivery via Shiprocket (delhivery); Xpressbees Air=XpressBees via Shiprocket (xpressbees); Ekart Logistics Air=Ekart via Shiprocket (ekart); Ecom Air 500gm=Ecom Express via Shiprocket (ecom)
    null_handling: Do not infer business meaning when value is null unless explicitly stated.
    business_usage: filtering; grouping; metric semantic filters; reconciliation classification
    evidence_refs:
    - evidence.logistics_kb_doc
    - evidence.cognee_design_v4
    - evidence.unified_edge_scope
```
```yaml
candidate_card:
  card_type: value_profile
  card_id: value_profile.shiprocket_invoice.order_status
  name: shiprocket_invoice.order_status Value Profile
  fields:
    name: shiprocket_invoice.order_status Value Profile
    description: Known values and meanings for shiprocket_invoice.order_status.
    status: active
    confidence: curated
    source_documents:
    - Logistics KB Doc.docx
    - Cognee KB Design v4.md
    - logistics_gold_std_raw_md_frame_v3.md
    - logistics_gold_std_canonical_card_frame_v5.md
    created_by: kb_authoring_assistant
    updated_by: kb_authoring_assistant
    version: 5.0-manifest-aligned
    table_id: table.zs_observe.shiprocket_invoice
    column_id: column.zs_observe.shiprocket_invoice.order_status
    value_type: enum_or_enum_with_nulls
    values: DELIVERED=Delivered shipment invoice (delivered); RTO DELIVERED=RTO shipment invoice (rto); LOST=Lost shipment invoice (exception)
    null_handling: Do not infer business meaning when value is null unless explicitly stated.
    business_usage: filtering; grouping; metric semantic filters; reconciliation classification
    evidence_refs:
    - evidence.logistics_kb_doc
    - evidence.cognee_design_v4
    - evidence.unified_edge_scope
```
```yaml
candidate_card:
  card_type: value_profile
  card_id: value_profile.shiprocket_invoice.payment_mode
  name: shiprocket_invoice.payment_mode Value Profile
  fields:
    name: shiprocket_invoice.payment_mode Value Profile
    description: Known values and meanings for shiprocket_invoice.payment_mode.
    status: active
    confidence: curated
    source_documents:
    - Logistics KB Doc.docx
    - Cognee KB Design v4.md
    - logistics_gold_std_raw_md_frame_v3.md
    - logistics_gold_std_canonical_card_frame_v5.md
    created_by: kb_authoring_assistant
    updated_by: kb_authoring_assistant
    version: 5.0-manifest-aligned
    table_id: table.zs_observe.shiprocket_invoice
    column_id: column.zs_observe.shiprocket_invoice.payment_mode
    value_type: enum_or_enum_with_nulls
    values: prepaid=Prepaid shipment (prepaid); cod=COD shipment (cod)
    null_handling: Do not infer business meaning when value is null unless explicitly stated.
    business_usage: filtering; grouping; metric semantic filters; reconciliation classification
    evidence_refs:
    - evidence.logistics_kb_doc
    - evidence.cognee_design_v4
    - evidence.unified_edge_scope
```
```yaml
candidate_card:
  card_type: value_profile
  card_id: value_profile.shiprocket_invoice.zone
  name: shiprocket_invoice.zone Value Profile
  fields:
    name: shiprocket_invoice.zone Value Profile
    description: Known values and meanings for shiprocket_invoice.zone.
    status: active
    confidence: curated
    source_documents:
    - Logistics KB Doc.docx
    - Cognee KB Design v4.md
    - logistics_gold_std_raw_md_frame_v3.md
    - logistics_gold_std_canonical_card_frame_v5.md
    created_by: kb_authoring_assistant
    updated_by: kb_authoring_assistant
    version: 5.0-manifest-aligned
    table_id: table.zs_observe.shiprocket_invoice
    column_id: column.zs_observe.shiprocket_invoice.zone
    value_type: enum_or_enum_with_nulls
    values: a=Local/near zone (zone_a); b=Regional zone (zone_b); c=Medium distance zone (zone_c); d=Farthest/dominant zone (zone_d)
    null_handling: Do not infer business meaning when value is null unless explicitly stated.
    business_usage: filtering; grouping; metric semantic filters; reconciliation classification
    evidence_refs:
    - evidence.logistics_kb_doc
    - evidence.cognee_design_v4
    - evidence.unified_edge_scope
```
```yaml
candidate_card:
  card_type: value_profile
  card_id: value_profile.shiprocket_settlement.courier_partner
  name: shiprocket_settlement.courier_partner Value Profile
  fields:
    name: shiprocket_settlement.courier_partner Value Profile
    description: Known values and meanings for shiprocket_settlement.courier_partner.
    status: active
    confidence: curated
    source_documents:
    - Logistics KB Doc.docx
    - Cognee KB Design v4.md
    - logistics_gold_std_raw_md_frame_v3.md
    - logistics_gold_std_canonical_card_frame_v5.md
    created_by: kb_authoring_assistant
    updated_by: kb_authoring_assistant
    version: 5.0-manifest-aligned
    table_id: table.zs_observe.shiprocket_settlement
    column_id: column.zs_observe.shiprocket_settlement.courier_partner
    value_type: enum_or_enum_with_nulls
    values: Delhivery Air=Delhivery COD via Shiprocket (delhivery); DTDC Air 500gm=DTDC COD via Shiprocket (dtdc); Xpressbees Air=XpressBees COD via Shiprocket (xpressbees); Ekart Logistics Air=Ekart COD via Shiprocket (ekart); Ecom Air 500gm=Ecom COD via Shiprocket (ecom)
    null_handling: Do not infer business meaning when value is null unless explicitly stated.
    business_usage: filtering; grouping; metric semantic filters; reconciliation classification
    evidence_refs:
    - evidence.logistics_kb_doc
    - evidence.cognee_design_v4
    - evidence.unified_edge_scope
```
```yaml
candidate_card:
  card_type: value_profile
  card_id: value_profile.shiprocket_settlement_report.awb_remittance_status
  name: shiprocket_settlement_report.awb_remittance_status Value Profile
  fields:
    name: shiprocket_settlement_report.awb_remittance_status Value Profile
    description: Known values and meanings for shiprocket_settlement_report.awb_remittance_status.
    status: active
    confidence: curated
    source_documents:
    - Logistics KB Doc.docx
    - Cognee KB Design v4.md
    - logistics_gold_std_raw_md_frame_v3.md
    - logistics_gold_std_canonical_card_frame_v5.md
    created_by: kb_authoring_assistant
    updated_by: kb_authoring_assistant
    version: 5.0-manifest-aligned
    table_id: table.zs_observe.shiprocket_settlement_report
    column_id: column.zs_observe.shiprocket_settlement_report.awb_remittance_status
    value_type: enum_or_enum_with_nulls
    values: schema_only=Status values unavailable until rows load (schema_only)
    null_handling: Do not infer business meaning when value is null unless explicitly stated.
    business_usage: filtering; grouping; metric semantic filters; reconciliation classification
    evidence_refs:
    - evidence.logistics_kb_doc
    - evidence.cognee_design_v4
    - evidence.unified_edge_scope
```

### 4.8 metric cards

```yaml
candidate_card:
  card_type: metric
  card_id: metric.actual_weight
  name: Actual Weight
  fields:
    name: Actual Weight
    description: Actual or final weight of shipment.
    status: active
    confidence: curated
    source_documents:
    - Logistics KB Doc.docx
    - Cognee KB Design v4.md
    - logistics_gold_std_raw_md_frame_v3.md
    - logistics_gold_std_canonical_card_frame_v5.md
    created_by: kb_authoring_assistant
    updated_by: kb_authoring_assistant
    version: 5.0-manifest-aligned
    metric_name: Actual Weight
    aliases:
    - final weight
    - physical weight
    metric_type: amount/count/rate/days_by_metric
    unit: currency/count/percentage/days_by_metric
    default_aggregation: SUM or COUNT or ratio by metric
    default_grain: shipment_awb_or_settlement_batch
    polarity: context_dependent
    business_concepts:
    - logistics
    - actual_weight
    domain_ids:
    - domain.logistics_reconciliation
    implementations:
    - see metric_impl blocks in shiprocket_logistics_partner_parser_ready_v6_role_split.md and shiprocket_services_aggregator_parser_ready_v6_role_split.md
    evidence_refs:
    - evidence.logistics_kb_doc
    - evidence.cognee_design_v4
    - evidence.unified_edge_scope
```
```yaml
candidate_card:
  card_type: metric
  card_id: metric.average_freight_per_awb
  name: Average Freight per AWB
  fields:
    name: Average Freight per AWB
    description: Freight billed divided by unique AWB count.
    status: active
    confidence: curated
    source_documents:
    - Logistics KB Doc.docx
    - Cognee KB Design v4.md
    - logistics_gold_std_raw_md_frame_v3.md
    - logistics_gold_std_canonical_card_frame_v5.md
    created_by: kb_authoring_assistant
    updated_by: kb_authoring_assistant
    version: 5.0-manifest-aligned
    metric_name: Average Freight per AWB
    aliases:
    - average shipping cost
    - avg freight
    metric_type: amount/count/rate/days_by_metric
    unit: currency/count/percentage/days_by_metric
    default_aggregation: SUM or COUNT or ratio by metric
    default_grain: shipment_awb_or_settlement_batch
    polarity: context_dependent
    business_concepts:
    - logistics
    - average_freight_per_awb
    domain_ids:
    - domain.logistics_reconciliation
    implementations:
    - see metric_impl blocks in shiprocket_logistics_partner_parser_ready_v6_role_split.md and shiprocket_services_aggregator_parser_ready_v6_role_split.md
    evidence_refs:
    - evidence.logistics_kb_doc
    - evidence.cognee_design_v4
    - evidence.unified_edge_scope
```
```yaml
candidate_card:
  card_type: metric
  card_id: metric.batch_settlement_amount
  name: Batch Settlement Amount
  fields:
    name: Batch Settlement Amount
    description: Amount for a settlement/remittance batch.
    status: active
    confidence: curated
    source_documents:
    - Logistics KB Doc.docx
    - Cognee KB Design v4.md
    - logistics_gold_std_raw_md_frame_v3.md
    - logistics_gold_std_canonical_card_frame_v5.md
    created_by: kb_authoring_assistant
    updated_by: kb_authoring_assistant
    version: 5.0-manifest-aligned
    metric_name: Batch Settlement Amount
    aliases:
    - settlement batch amount
    - batch total
    metric_type: amount/count/rate/days_by_metric
    unit: currency/count/percentage/days_by_metric
    default_aggregation: SUM or COUNT or ratio by metric
    default_grain: shipment_awb_or_settlement_batch
    polarity: context_dependent
    business_concepts:
    - logistics
    - batch_settlement_amount
    domain_ids:
    - domain.logistics_reconciliation
    implementations:
    - see metric_impl blocks in shiprocket_logistics_partner_parser_ready_v6_role_split.md and shiprocket_services_aggregator_parser_ready_v6_role_split.md
    evidence_refs:
    - evidence.logistics_kb_doc
    - evidence.cognee_design_v4
    - evidence.unified_edge_scope
```
```yaml
candidate_card:
  card_type: metric
  card_id: metric.billable_weight
  name: Billable Weight
  fields:
    name: Billable Weight
    description: Billable or charged weight used for freight calculation.
    status: active
    confidence: curated
    source_documents:
    - Logistics KB Doc.docx
    - Cognee KB Design v4.md
    - logistics_gold_std_raw_md_frame_v3.md
    - logistics_gold_std_canonical_card_frame_v5.md
    created_by: kb_authoring_assistant
    updated_by: kb_authoring_assistant
    version: 5.0-manifest-aligned
    metric_name: Billable Weight
    aliases:
    - charged weight
    metric_type: amount/count/rate/days_by_metric
    unit: currency/count/percentage/days_by_metric
    default_aggregation: SUM or COUNT or ratio by metric
    default_grain: shipment_awb_or_settlement_batch
    polarity: context_dependent
    business_concepts:
    - logistics
    - billable_weight
    domain_ids:
    - domain.logistics_reconciliation
    implementations:
    - see metric_impl blocks in shiprocket_logistics_partner_parser_ready_v6_role_split.md and shiprocket_services_aggregator_parser_ready_v6_role_split.md
    evidence_refs:
    - evidence.logistics_kb_doc
    - evidence.cognee_design_v4
    - evidence.unified_edge_scope
```
```yaml
candidate_card:
  card_type: metric
  card_id: metric.cod_collected_amount
  name: COD Collected Amount
  fields:
    name: COD Collected Amount
    description: Cash/COD amount collected by courier from customer.
    status: active
    confidence: curated
    source_documents:
    - Logistics KB Doc.docx
    - Cognee KB Design v4.md
    - logistics_gold_std_raw_md_frame_v3.md
    - logistics_gold_std_canonical_card_frame_v5.md
    created_by: kb_authoring_assistant
    updated_by: kb_authoring_assistant
    version: 5.0-manifest-aligned
    metric_name: COD Collected Amount
    aliases:
    - cash collected
    - COD collected
    metric_type: amount/count/rate/days_by_metric
    unit: currency/count/percentage/days_by_metric
    default_aggregation: SUM or COUNT or ratio by metric
    default_grain: shipment_awb_or_settlement_batch
    polarity: context_dependent
    business_concepts:
    - logistics
    - cod_collected_amount
    domain_ids:
    - domain.logistics_reconciliation
    implementations:
    - see metric_impl blocks in shiprocket_logistics_partner_parser_ready_v6_role_split.md and shiprocket_services_aggregator_parser_ready_v6_role_split.md
    evidence_refs:
    - evidence.logistics_kb_doc
    - evidence.cognee_design_v4
    - evidence.unified_edge_scope
```
```yaml
candidate_card:
  card_type: metric
  card_id: metric.cod_fee_amount
  name: COD Fee Amount
  fields:
    name: COD Fee Amount
    description: Fee charged for COD handling or collection.
    status: active
    confidence: curated
    source_documents:
    - Logistics KB Doc.docx
    - Cognee KB Design v4.md
    - logistics_gold_std_raw_md_frame_v3.md
    - logistics_gold_std_canonical_card_frame_v5.md
    created_by: kb_authoring_assistant
    updated_by: kb_authoring_assistant
    version: 5.0-manifest-aligned
    metric_name: COD Fee Amount
    aliases:
    - COD handling fee
    - COD collection charge
    metric_type: amount/count/rate/days_by_metric
    unit: currency/count/percentage/days_by_metric
    default_aggregation: SUM or COUNT or ratio by metric
    default_grain: shipment_awb_or_settlement_batch
    polarity: context_dependent
    business_concepts:
    - logistics
    - cod_fee_amount
    domain_ids:
    - domain.logistics_reconciliation
    implementations:
    - see metric_impl blocks in shiprocket_logistics_partner_parser_ready_v6_role_split.md and shiprocket_services_aggregator_parser_ready_v6_role_split.md
    evidence_refs:
    - evidence.logistics_kb_doc
    - evidence.cognee_design_v4
    - evidence.unified_edge_scope
```
```yaml
candidate_card:
  card_type: metric
  card_id: metric.cod_remittance_lag_days
  name: COD Remittance Lag Days
  fields:
    name: COD Remittance Lag Days
    description: Days between delivery and COD settlement/remittance.
    status: active
    confidence: curated
    source_documents:
    - Logistics KB Doc.docx
    - Cognee KB Design v4.md
    - logistics_gold_std_raw_md_frame_v3.md
    - logistics_gold_std_canonical_card_frame_v5.md
    created_by: kb_authoring_assistant
    updated_by: kb_authoring_assistant
    version: 5.0-manifest-aligned
    metric_name: COD Remittance Lag Days
    aliases:
    - COD settlement lag
    - delivery to remittance lag
    metric_type: amount/count/rate/days_by_metric
    unit: currency/count/percentage/days_by_metric
    default_aggregation: SUM or COUNT or ratio by metric
    default_grain: shipment_awb_or_settlement_batch
    polarity: context_dependent
    business_concepts:
    - logistics
    - cod_remittance_lag_days
    domain_ids:
    - domain.logistics_reconciliation
    implementations:
    - see metric_impl blocks in shiprocket_logistics_partner_parser_ready_v6_role_split.md and shiprocket_services_aggregator_parser_ready_v6_role_split.md
    evidence_refs:
    - evidence.logistics_kb_doc
    - evidence.cognee_design_v4
    - evidence.unified_edge_scope
```
```yaml
candidate_card:
  card_type: metric
  card_id: metric.cod_remitted_amount
  name: COD Remitted Amount
  fields:
    name: COD Remitted Amount
    description: COD amount remitted by courier, aggregator, or fulfilment platform.
    status: active
    confidence: curated
    source_documents:
    - Logistics KB Doc.docx
    - Cognee KB Design v4.md
    - logistics_gold_std_raw_md_frame_v3.md
    - logistics_gold_std_canonical_card_frame_v5.md
    created_by: kb_authoring_assistant
    updated_by: kb_authoring_assistant
    version: 5.0-manifest-aligned
    metric_name: COD Remitted Amount
    aliases:
    - COD received from courier
    - COD settlement amount
    - COD remittance
    metric_type: amount/count/rate/days_by_metric
    unit: currency/count/percentage/days_by_metric
    default_aggregation: SUM or COUNT or ratio by metric
    default_grain: shipment_awb_or_settlement_batch
    polarity: context_dependent
    business_concepts:
    - logistics
    - cod_remitted_amount
    domain_ids:
    - domain.logistics_reconciliation
    implementations:
    - see metric_impl blocks in shiprocket_logistics_partner_parser_ready_v6_role_split.md and shiprocket_services_aggregator_parser_ready_v6_role_split.md
    evidence_refs:
    - evidence.logistics_kb_doc
    - evidence.cognee_design_v4
    - evidence.unified_edge_scope
```
```yaml
candidate_card:
  card_type: metric
  card_id: metric.forward_freight_amount
  name: Forward Freight Amount
  fields:
    name: Forward Freight Amount
    description: Forward delivery freight amount.
    status: active
    confidence: curated
    source_documents:
    - Logistics KB Doc.docx
    - Cognee KB Design v4.md
    - logistics_gold_std_raw_md_frame_v3.md
    - logistics_gold_std_canonical_card_frame_v5.md
    created_by: kb_authoring_assistant
    updated_by: kb_authoring_assistant
    version: 5.0-manifest-aligned
    metric_name: Forward Freight Amount
    aliases:
    - delivery charge
    - forward freight
    metric_type: amount/count/rate/days_by_metric
    unit: currency/count/percentage/days_by_metric
    default_aggregation: SUM or COUNT or ratio by metric
    default_grain: shipment_awb_or_settlement_batch
    polarity: context_dependent
    business_concepts:
    - logistics
    - forward_freight_amount
    domain_ids:
    - domain.logistics_reconciliation
    implementations:
    - see metric_impl blocks in shiprocket_logistics_partner_parser_ready_v6_role_split.md and shiprocket_services_aggregator_parser_ready_v6_role_split.md
    evidence_refs:
    - evidence.logistics_kb_doc
    - evidence.cognee_design_v4
    - evidence.unified_edge_scope
```
```yaml
candidate_card:
  card_type: metric
  card_id: metric.freight_billed_amount
  name: Freight Billed Amount
  fields:
    name: Freight Billed Amount
    description: Total freight charged for shipments.
    status: active
    confidence: curated
    source_documents:
    - Logistics KB Doc.docx
    - Cognee KB Design v4.md
    - logistics_gold_std_raw_md_frame_v3.md
    - logistics_gold_std_canonical_card_frame_v5.md
    created_by: kb_authoring_assistant
    updated_by: kb_authoring_assistant
    version: 5.0-manifest-aligned
    metric_name: Freight Billed Amount
    aliases:
    - freight charged
    - shipping cost
    - courier charges
    metric_type: amount/count/rate/days_by_metric
    unit: currency/count/percentage/days_by_metric
    default_aggregation: SUM or COUNT or ratio by metric
    default_grain: shipment_awb_or_settlement_batch
    polarity: context_dependent
    business_concepts:
    - logistics
    - freight_billed_amount
    domain_ids:
    - domain.logistics_reconciliation
    implementations:
    - see metric_impl blocks in shiprocket_logistics_partner_parser_ready_v6_role_split.md and shiprocket_services_aggregator_parser_ready_v6_role_split.md
    evidence_refs:
    - evidence.logistics_kb_doc
    - evidence.cognee_design_v4
    - evidence.unified_edge_scope
```
```yaml
candidate_card:
  card_type: metric
  card_id: metric.freight_excluding_tax_amount
  name: Freight Excluding Tax Amount
  fields:
    name: Freight Excluding Tax Amount
    description: Freight amount before tax.
    status: active
    confidence: curated
    source_documents:
    - Logistics KB Doc.docx
    - Cognee KB Design v4.md
    - logistics_gold_std_raw_md_frame_v3.md
    - logistics_gold_std_canonical_card_frame_v5.md
    created_by: kb_authoring_assistant
    updated_by: kb_authoring_assistant
    version: 5.0-manifest-aligned
    metric_name: Freight Excluding Tax Amount
    aliases:
    - pre GST freight
    - freight before GST
    metric_type: amount/count/rate/days_by_metric
    unit: currency/count/percentage/days_by_metric
    default_aggregation: SUM or COUNT or ratio by metric
    default_grain: shipment_awb_or_settlement_batch
    polarity: context_dependent
    business_concepts:
    - logistics
    - freight_excluding_tax_amount
    domain_ids:
    - domain.logistics_reconciliation
    implementations:
    - see metric_impl blocks in shiprocket_logistics_partner_parser_ready_v6_role_split.md and shiprocket_services_aggregator_parser_ready_v6_role_split.md
    evidence_refs:
    - evidence.logistics_kb_doc
    - evidence.cognee_design_v4
    - evidence.unified_edge_scope
```
```yaml
candidate_card:
  card_type: metric
  card_id: metric.fuel_surcharge_amount
  name: Fuel Surcharge Amount
  fields:
    name: Fuel Surcharge Amount
    description: Fuel surcharge component of freight.
    status: active
    confidence: curated
    source_documents:
    - Logistics KB Doc.docx
    - Cognee KB Design v4.md
    - logistics_gold_std_raw_md_frame_v3.md
    - logistics_gold_std_canonical_card_frame_v5.md
    created_by: kb_authoring_assistant
    updated_by: kb_authoring_assistant
    version: 5.0-manifest-aligned
    metric_name: Fuel Surcharge Amount
    aliases:
    - FSC
    - fuel surcharge
    metric_type: amount/count/rate/days_by_metric
    unit: currency/count/percentage/days_by_metric
    default_aggregation: SUM or COUNT or ratio by metric
    default_grain: shipment_awb_or_settlement_batch
    polarity: context_dependent
    business_concepts:
    - logistics
    - fuel_surcharge_amount
    domain_ids:
    - domain.logistics_reconciliation
    implementations:
    - see metric_impl blocks in shiprocket_logistics_partner_parser_ready_v6_role_split.md and shiprocket_services_aggregator_parser_ready_v6_role_split.md
    evidence_refs:
    - evidence.logistics_kb_doc
    - evidence.cognee_design_v4
    - evidence.unified_edge_scope
```
```yaml
candidate_card:
  card_type: metric
  card_id: metric.gst_on_freight_amount
  name: GST on Freight Amount
  fields:
    name: GST on Freight Amount
    description: GST or tax applied to freight.
    status: active
    confidence: curated
    source_documents:
    - Logistics KB Doc.docx
    - Cognee KB Design v4.md
    - logistics_gold_std_raw_md_frame_v3.md
    - logistics_gold_std_canonical_card_frame_v5.md
    created_by: kb_authoring_assistant
    updated_by: kb_authoring_assistant
    version: 5.0-manifest-aligned
    metric_name: GST on Freight Amount
    aliases:
    - freight tax
    - GST on courier charges
    metric_type: amount/count/rate/days_by_metric
    unit: currency/count/percentage/days_by_metric
    default_aggregation: SUM or COUNT or ratio by metric
    default_grain: shipment_awb_or_settlement_batch
    polarity: context_dependent
    business_concepts:
    - logistics
    - gst_on_freight_amount
    domain_ids:
    - domain.logistics_reconciliation
    implementations:
    - see metric_impl blocks in shiprocket_logistics_partner_parser_ready_v6_role_split.md and shiprocket_services_aggregator_parser_ready_v6_role_split.md
    evidence_refs:
    - evidence.logistics_kb_doc
    - evidence.cognee_design_v4
    - evidence.unified_edge_scope
```
```yaml
candidate_card:
  card_type: metric
  card_id: metric.rto_freight_amount
  name: RTO Freight Amount
  fields:
    name: RTO Freight Amount
    description: Freight amount charged for return-to-origin movement.
    status: active
    confidence: curated
    source_documents:
    - Logistics KB Doc.docx
    - Cognee KB Design v4.md
    - logistics_gold_std_raw_md_frame_v3.md
    - logistics_gold_std_canonical_card_frame_v5.md
    created_by: kb_authoring_assistant
    updated_by: kb_authoring_assistant
    version: 5.0-manifest-aligned
    metric_name: RTO Freight Amount
    aliases:
    - return freight
    - RTO charge
    metric_type: amount/count/rate/days_by_metric
    unit: currency/count/percentage/days_by_metric
    default_aggregation: SUM or COUNT or ratio by metric
    default_grain: shipment_awb_or_settlement_batch
    polarity: context_dependent
    business_concepts:
    - logistics
    - rto_freight_amount
    domain_ids:
    - domain.logistics_reconciliation
    implementations:
    - see metric_impl blocks in shiprocket_logistics_partner_parser_ready_v6_role_split.md and shiprocket_services_aggregator_parser_ready_v6_role_split.md
    evidence_refs:
    - evidence.logistics_kb_doc
    - evidence.cognee_design_v4
    - evidence.unified_edge_scope
```
```yaml
candidate_card:
  card_type: metric
  card_id: metric.unique_awb_count
  name: Unique AWB Count
  fields:
    name: Unique AWB Count
    description: Distinct count of AWB/waybill/tracking identifiers.
    status: active
    confidence: curated
    source_documents:
    - Logistics KB Doc.docx
    - Cognee KB Design v4.md
    - logistics_gold_std_raw_md_frame_v3.md
    - logistics_gold_std_canonical_card_frame_v5.md
    created_by: kb_authoring_assistant
    updated_by: kb_authoring_assistant
    version: 5.0-manifest-aligned
    metric_name: Unique AWB Count
    aliases:
    - distinct AWBs
    - unique waybills
    metric_type: amount/count/rate/days_by_metric
    unit: currency/count/percentage/days_by_metric
    default_aggregation: SUM or COUNT or ratio by metric
    default_grain: shipment_awb_or_settlement_batch
    polarity: context_dependent
    business_concepts:
    - logistics
    - unique_awb_count
    domain_ids:
    - domain.logistics_reconciliation
    implementations:
    - see metric_impl blocks in shiprocket_logistics_partner_parser_ready_v6_role_split.md and shiprocket_services_aggregator_parser_ready_v6_role_split.md
    evidence_refs:
    - evidence.logistics_kb_doc
    - evidence.cognee_design_v4
    - evidence.unified_edge_scope
```

### 4.9 metric_implementation cards

```yaml
candidate_card:
  card_type: metric_implementation
  card_id: metric_impl.shiprocket_invoice.freight_billed_amount
  name: Shiprocket Freight Billed Amount Implementation
  fields:
    name: Shiprocket Freight Billed Amount Implementation
    description: Freight Billed Amount implementation for Shiprocket using shiprocket_invoice.
    status: active
    confidence: curated
    source_documents:
    - Logistics KB Doc.docx
    - Cognee KB Design v4.md
    - logistics_gold_std_raw_md_frame_v3.md
    - logistics_gold_std_canonical_card_frame_v5.md
    created_by: kb_authoring_assistant
    updated_by: kb_authoring_assistant
    version: 5.0-manifest-aligned
    metric_id: metric.freight_billed_amount
    implementation_name: Shiprocket Freight Billed Amount
    metric_pattern: sum_component_amounts
    applicability: platform=shiprocket; table=zs_observe.shiprocket_invoice; account filters via Account Data Binding only
    base_tables:
    - table.zs_observe.shiprocket_invoice
    required_columns:
    - column.zs_observe.shiprocket_invoice.charged_amount
    semantic_filters: []
    formula_description: SUM(charged_amount)
    formula_sql: SUM(charged_amount)
    dependent_metrics: []
    allowed_dimensions:
    - courier_partner
    - date
    - awb
    allowed_grains:
    - awb
    - order
    - day
    - month
    - courier_partner
    - batch where safe
    recommended_date_columns:
    - invoice_date_or_period
    - recommended table date if available
    unit: currency/count/percentage/days_by_metric
    precision: 2_decimal_places
    caveats: charged_amount in shiprocket_invoice is freight, unlike other logistics tables.
    evidence_refs:
    - evidence.logistics_kb_doc
    - evidence.cognee_design_v4
    - evidence.unified_edge_scope
    formula_template_id: formula_template.logistics.component_sum
```
```yaml
candidate_card:
  card_type: metric_implementation
  card_id: metric_impl.shiprocket_invoice.freight_excluding_tax_amount
  name: Shiprocket Freight Excluding Tax Amount Implementation
  fields:
    name: Shiprocket Freight Excluding Tax Amount Implementation
    description: Freight Excluding Tax Amount implementation for Shiprocket using shiprocket_invoice.
    status: active
    confidence: curated
    source_documents:
    - Logistics KB Doc.docx
    - Cognee KB Design v4.md
    - logistics_gold_std_raw_md_frame_v3.md
    - logistics_gold_std_canonical_card_frame_v5.md
    created_by: kb_authoring_assistant
    updated_by: kb_authoring_assistant
    version: 5.0-manifest-aligned
    metric_id: metric.freight_excluding_tax_amount
    implementation_name: Shiprocket Freight Excluding Tax Amount
    metric_pattern: sum_component_amounts
    applicability: platform=shiprocket; table=zs_observe.shiprocket_invoice; account filters via Account Data Binding only
    base_tables:
    - table.zs_observe.shiprocket_invoice
    required_columns:
    - column.zs_observe.shiprocket_invoice.charged_amount_excluding_tax
    semantic_filters: []
    formula_description: SUM(charged_amount_excluding_tax)
    formula_sql: SUM(charged_amount_excluding_tax)
    dependent_metrics: []
    allowed_dimensions:
    - courier_partner
    - date
    - awb
    allowed_grains:
    - awb
    - order
    - day
    - month
    - courier_partner
    - batch where safe
    recommended_date_columns:
    - invoice_date_or_period
    - recommended table date if available
    unit: currency/count/percentage/days_by_metric
    precision: 2_decimal_places
    caveats: charged_amount in shiprocket_invoice is freight, unlike other logistics tables.
    evidence_refs:
    - evidence.logistics_kb_doc
    - evidence.cognee_design_v4
    - evidence.unified_edge_scope
    formula_template_id: formula_template.logistics.component_sum
```
```yaml
candidate_card:
  card_type: metric_implementation
  card_id: metric_impl.shiprocket_invoice.gst_on_freight_amount
  name: Shiprocket GST on Freight Amount Implementation
  fields:
    name: Shiprocket GST on Freight Amount Implementation
    description: GST on Freight Amount implementation for Shiprocket using shiprocket_invoice.
    status: active
    confidence: curated
    source_documents:
    - Logistics KB Doc.docx
    - Cognee KB Design v4.md
    - logistics_gold_std_raw_md_frame_v3.md
    - logistics_gold_std_canonical_card_frame_v5.md
    created_by: kb_authoring_assistant
    updated_by: kb_authoring_assistant
    version: 5.0-manifest-aligned
    metric_id: metric.gst_on_freight_amount
    implementation_name: Shiprocket GST on Freight Amount
    metric_pattern: sum_component_amounts
    applicability: platform=shiprocket; table=zs_observe.shiprocket_invoice; account filters via Account Data Binding only
    base_tables:
    - table.zs_observe.shiprocket_invoice
    required_columns:
    - column.zs_observe.shiprocket_invoice.total_tax
    semantic_filters: []
    formula_description: SUM(total_tax)
    formula_sql: SUM(total_tax)
    dependent_metrics: []
    allowed_dimensions:
    - courier_partner
    - date
    - awb
    allowed_grains:
    - awb
    - order
    - day
    - month
    - courier_partner
    - batch where safe
    recommended_date_columns:
    - invoice_date_or_period
    - recommended table date if available
    unit: currency/count/percentage/days_by_metric
    precision: 2_decimal_places
    caveats: charged_amount in shiprocket_invoice is freight, unlike other logistics tables.
    evidence_refs:
    - evidence.logistics_kb_doc
    - evidence.cognee_design_v4
    - evidence.unified_edge_scope
    formula_template_id: formula_template.logistics.component_sum
```
```yaml
candidate_card:
  card_type: metric_implementation
  card_id: metric_impl.shiprocket_invoice.fuel_surcharge_amount
  name: Shiprocket Fuel Surcharge Amount Implementation
  fields:
    name: Shiprocket Fuel Surcharge Amount Implementation
    description: Fuel Surcharge Amount implementation for Shiprocket using shiprocket_invoice.
    status: active
    confidence: curated
    source_documents:
    - Logistics KB Doc.docx
    - Cognee KB Design v4.md
    - logistics_gold_std_raw_md_frame_v3.md
    - logistics_gold_std_canonical_card_frame_v5.md
    created_by: kb_authoring_assistant
    updated_by: kb_authoring_assistant
    version: 5.0-manifest-aligned
    metric_id: metric.fuel_surcharge_amount
    implementation_name: Shiprocket Fuel Surcharge Amount
    metric_pattern: sum_component_amounts
    applicability: platform=shiprocket; table=zs_observe.shiprocket_invoice; account filters via Account Data Binding only
    base_tables:
    - table.zs_observe.shiprocket_invoice
    required_columns:
    - column.zs_observe.shiprocket_invoice.charge_fsc
    semantic_filters: []
    formula_description: SUM(charge_fsc)
    formula_sql: SUM(charge_fsc)
    dependent_metrics: []
    allowed_dimensions:
    - courier_partner
    - date
    - awb
    allowed_grains:
    - awb
    - order
    - day
    - month
    - courier_partner
    - batch where safe
    recommended_date_columns:
    - invoice_date_or_period
    - recommended table date if available
    unit: currency/count/percentage/days_by_metric
    precision: 2_decimal_places
    caveats: charged_amount in shiprocket_invoice is freight, unlike other logistics tables.
    evidence_refs:
    - evidence.logistics_kb_doc
    - evidence.cognee_design_v4
    - evidence.unified_edge_scope
    formula_template_id: formula_template.logistics.component_sum
```
```yaml
candidate_card:
  card_type: metric_implementation
  card_id: metric_impl.shiprocket_invoice.rto_freight_amount
  name: Shiprocket RTO Freight Amount Implementation
  fields:
    name: Shiprocket RTO Freight Amount Implementation
    description: RTO Freight Amount implementation for Shiprocket using shiprocket_invoice.
    status: active
    confidence: curated
    source_documents:
    - Logistics KB Doc.docx
    - Cognee KB Design v4.md
    - logistics_gold_std_raw_md_frame_v3.md
    - logistics_gold_std_canonical_card_frame_v5.md
    created_by: kb_authoring_assistant
    updated_by: kb_authoring_assistant
    version: 5.0-manifest-aligned
    metric_id: metric.rto_freight_amount
    implementation_name: Shiprocket RTO Freight Amount
    metric_pattern: sum_component_amounts
    applicability: platform=shiprocket; table=zs_observe.shiprocket_invoice; account filters via Account Data Binding only
    base_tables:
    - table.zs_observe.shiprocket_invoice
    required_columns:
    - column.zs_observe.shiprocket_invoice.charge_rto
    semantic_filters: []
    formula_description: SUM(charge_rto)
    formula_sql: SUM(charge_rto)
    dependent_metrics: []
    allowed_dimensions:
    - courier_partner
    - date
    - awb
    allowed_grains:
    - awb
    - order
    - day
    - month
    - courier_partner
    - batch where safe
    recommended_date_columns:
    - invoice_date_or_period
    - recommended table date if available
    unit: currency/count/percentage/days_by_metric
    precision: 2_decimal_places
    caveats: charged_amount in shiprocket_invoice is freight, unlike other logistics tables.
    evidence_refs:
    - evidence.logistics_kb_doc
    - evidence.cognee_design_v4
    - evidence.unified_edge_scope
    formula_template_id: formula_template.logistics.component_sum
```
```yaml
candidate_card:
  card_type: metric_implementation
  card_id: metric_impl.shiprocket_invoice.cod_fee_amount
  name: Shiprocket COD Fee Amount Implementation
  fields:
    name: Shiprocket COD Fee Amount Implementation
    description: COD Fee Amount implementation for Shiprocket using shiprocket_invoice.
    status: active
    confidence: curated
    source_documents:
    - Logistics KB Doc.docx
    - Cognee KB Design v4.md
    - logistics_gold_std_raw_md_frame_v3.md
    - logistics_gold_std_canonical_card_frame_v5.md
    created_by: kb_authoring_assistant
    updated_by: kb_authoring_assistant
    version: 5.0-manifest-aligned
    metric_id: metric.cod_fee_amount
    implementation_name: Shiprocket COD Fee Amount
    metric_pattern: sum_component_amounts
    applicability: platform=shiprocket; table=zs_observe.shiprocket_invoice; account filters via Account Data Binding only
    base_tables:
    - table.zs_observe.shiprocket_invoice
    required_columns:
    - column.zs_observe.shiprocket_invoice.charge_cod
    semantic_filters: []
    formula_description: SUM(charge_cod)
    formula_sql: SUM(charge_cod)
    dependent_metrics: []
    allowed_dimensions:
    - courier_partner
    - date
    - awb
    allowed_grains:
    - awb
    - order
    - day
    - month
    - courier_partner
    - batch where safe
    recommended_date_columns:
    - invoice_date_or_period
    - recommended table date if available
    unit: currency/count/percentage/days_by_metric
    precision: 2_decimal_places
    caveats: charged_amount in shiprocket_invoice is freight, unlike other logistics tables.
    evidence_refs:
    - evidence.logistics_kb_doc
    - evidence.cognee_design_v4
    - evidence.unified_edge_scope
    formula_template_id: formula_template.logistics.component_sum
```
```yaml
candidate_card:
  card_type: metric_implementation
  card_id: metric_impl.shiprocket_invoice.forward_freight_amount
  name: Shiprocket Forward Freight Amount Implementation
  fields:
    name: Shiprocket Forward Freight Amount Implementation
    description: Forward Freight Amount implementation for Shiprocket using shiprocket_invoice.
    status: active
    confidence: curated
    source_documents:
    - Logistics KB Doc.docx
    - Cognee KB Design v4.md
    - logistics_gold_std_raw_md_frame_v3.md
    - logistics_gold_std_canonical_card_frame_v5.md
    created_by: kb_authoring_assistant
    updated_by: kb_authoring_assistant
    version: 5.0-manifest-aligned
    metric_id: metric.forward_freight_amount
    implementation_name: Shiprocket Forward Freight Amount
    metric_pattern: sum_component_amounts
    applicability: platform=shiprocket; table=zs_observe.shiprocket_invoice; account filters via Account Data Binding only
    base_tables:
    - table.zs_observe.shiprocket_invoice
    required_columns:
    - column.zs_observe.shiprocket_invoice.charge_dl
    semantic_filters: []
    formula_description: SUM(charge_dl)
    formula_sql: SUM(charge_dl)
    dependent_metrics: []
    allowed_dimensions:
    - courier_partner
    - date
    - awb
    allowed_grains:
    - awb
    - order
    - day
    - month
    - courier_partner
    - batch where safe
    recommended_date_columns:
    - invoice_date_or_period
    - recommended table date if available
    unit: currency/count/percentage/days_by_metric
    precision: 2_decimal_places
    caveats: charged_amount in shiprocket_invoice is freight, unlike other logistics tables.
    evidence_refs:
    - evidence.logistics_kb_doc
    - evidence.cognee_design_v4
    - evidence.unified_edge_scope
    formula_template_id: formula_template.logistics.component_sum
```
```yaml
candidate_card:
  card_type: metric_implementation
  card_id: metric_impl.shiprocket_invoice.actual_weight
  name: Shiprocket Actual Weight Implementation
  fields:
    name: Shiprocket Actual Weight Implementation
    description: Actual Weight implementation for Shiprocket using shiprocket_invoice.
    status: active
    confidence: curated
    source_documents:
    - Logistics KB Doc.docx
    - Cognee KB Design v4.md
    - logistics_gold_std_raw_md_frame_v3.md
    - logistics_gold_std_canonical_card_frame_v5.md
    created_by: kb_authoring_assistant
    updated_by: kb_authoring_assistant
    version: 5.0-manifest-aligned
    metric_id: metric.actual_weight
    implementation_name: Shiprocket Actual Weight
    metric_pattern: sum_component_amounts
    applicability: platform=shiprocket; table=zs_observe.shiprocket_invoice; account filters via Account Data Binding only
    base_tables:
    - table.zs_observe.shiprocket_invoice
    required_columns:
    - column.zs_observe.shiprocket_invoice.final_weight
    semantic_filters: []
    formula_description: SUM(final_weight)
    formula_sql: SUM(final_weight)
    dependent_metrics: []
    allowed_dimensions:
    - courier_partner
    - date
    - awb
    allowed_grains:
    - awb
    - order
    - day
    - month
    - courier_partner
    - batch where safe
    recommended_date_columns:
    - invoice_date_or_period
    - recommended table date if available
    unit: currency/count/percentage/days_by_metric
    precision: 2_decimal_places
    caveats: charged_amount in shiprocket_invoice is freight, unlike other logistics tables.
    evidence_refs:
    - evidence.logistics_kb_doc
    - evidence.cognee_design_v4
    - evidence.unified_edge_scope
    formula_template_id: formula_template.logistics.component_sum
```
```yaml
candidate_card:
  card_type: metric_implementation
  card_id: metric_impl.shiprocket_invoice.billable_weight
  name: Shiprocket Billable Weight Implementation
  fields:
    name: Shiprocket Billable Weight Implementation
    description: Billable Weight implementation for Shiprocket using shiprocket_invoice.
    status: active
    confidence: curated
    source_documents:
    - Logistics KB Doc.docx
    - Cognee KB Design v4.md
    - logistics_gold_std_raw_md_frame_v3.md
    - logistics_gold_std_canonical_card_frame_v5.md
    created_by: kb_authoring_assistant
    updated_by: kb_authoring_assistant
    version: 5.0-manifest-aligned
    metric_id: metric.billable_weight
    implementation_name: Shiprocket Billable Weight
    metric_pattern: sum_component_amounts
    applicability: platform=shiprocket; table=zs_observe.shiprocket_invoice; account filters via Account Data Binding only
    base_tables:
    - table.zs_observe.shiprocket_invoice
    required_columns:
    - column.zs_observe.shiprocket_invoice.charged_weight
    semantic_filters: []
    formula_description: SUM(charged_weight)
    formula_sql: SUM(charged_weight)
    dependent_metrics: []
    allowed_dimensions:
    - courier_partner
    - date
    - awb
    allowed_grains:
    - awb
    - order
    - day
    - month
    - courier_partner
    - batch where safe
    recommended_date_columns:
    - invoice_date_or_period
    - recommended table date if available
    unit: currency/count/percentage/days_by_metric
    precision: 2_decimal_places
    caveats: charged_amount in shiprocket_invoice is freight, unlike other logistics tables.
    evidence_refs:
    - evidence.logistics_kb_doc
    - evidence.cognee_design_v4
    - evidence.unified_edge_scope
    formula_template_id: formula_template.logistics.component_sum
```
```yaml
candidate_card:
  card_type: metric_implementation
  card_id: metric_impl.shiprocket_invoice.average_freight_per_awb
  name: Shiprocket Average Freight per AWB Implementation
  fields:
    name: Shiprocket Average Freight per AWB Implementation
    description: Average Freight per AWB implementation for Shiprocket using shiprocket_invoice.
    status: active
    confidence: curated
    source_documents:
    - Logistics KB Doc.docx
    - Cognee KB Design v4.md
    - logistics_gold_std_raw_md_frame_v3.md
    - logistics_gold_std_canonical_card_frame_v5.md
    created_by: kb_authoring_assistant
    updated_by: kb_authoring_assistant
    version: 5.0-manifest-aligned
    metric_id: metric.average_freight_per_awb
    implementation_name: Shiprocket Average Freight per AWB
    metric_pattern: ratio_sum_to_distinct_awb
    applicability: platform=shiprocket; table=zs_observe.shiprocket_invoice; account filters via Account Data Binding only
    base_tables:
    - table.zs_observe.shiprocket_invoice
    required_columns:
    - column.zs_observe.shiprocket_invoice.charged_amount
    - column.zs_observe.shiprocket_invoice.other_id
    semantic_filters: []
    formula_description: SUM(charged_amount)/NULLIF(COUNT(DISTINCT other_id),0)
    formula_sql: SUM(charged_amount)/NULLIF(COUNT(DISTINCT other_id),0)
    dependent_metrics: []
    allowed_dimensions:
    - courier_partner
    - date
    - awb
    allowed_grains:
    - awb
    - order
    - day
    - month
    - courier_partner
    - batch where safe
    recommended_date_columns:
    - invoice_date_or_period
    unit: currency/count/percentage/days_by_metric
    precision: 2_decimal_places
    caveats: Use only with documented amount semantics and grain safety.
    evidence_refs:
    - evidence.logistics_kb_doc
    - evidence.cognee_design_v4
    - evidence.unified_edge_scope
    formula_template_id: formula_template.logistics.ratio_rate
```
```yaml
candidate_card:
  card_type: metric_implementation
  card_id: metric_impl.shiprocket_settlement.cod_collected_amount
  name: Shiprocket COD Collected Amount Implementation
  fields:
    name: Shiprocket COD Collected Amount Implementation
    description: COD Collected Amount implementation for Shiprocket using shiprocket_settlement.
    status: active
    confidence: curated
    source_documents:
    - Logistics KB Doc.docx
    - Cognee KB Design v4.md
    - logistics_gold_std_raw_md_frame_v3.md
    - logistics_gold_std_canonical_card_frame_v5.md
    created_by: kb_authoring_assistant
    updated_by: kb_authoring_assistant
    version: 5.0-manifest-aligned
    metric_id: metric.cod_collected_amount
    implementation_name: Shiprocket COD Collected Amount
    metric_pattern: settlement_sum_or_lag
    applicability: platform=shiprocket; table=zs_observe.shiprocket_settlement; account filters via Account Data Binding only
    base_tables:
    - table.zs_observe.shiprocket_settlement
    required_columns:
    - column.zs_observe.shiprocket_settlement.charged_amount
    semantic_filters: []
    formula_description: SUM(charged_amount)
    formula_sql: SUM(charged_amount)
    dependent_metrics: []
    allowed_dimensions:
    - courier_partner
    - date
    - awb
    allowed_grains:
    - awb
    - order
    - day
    - month
    - courier_partner
    - batch where safe
    recommended_date_columns:
    - settlement_date
    - delivered_date
    unit: currency/count/percentage/days_by_metric
    precision: 2_decimal_places
    caveats: charged_amount in shiprocket_settlement means COD collected/remitted, not freight.
    evidence_refs:
    - evidence.logistics_kb_doc
    - evidence.cognee_design_v4
    - evidence.unified_edge_scope
```
```yaml
candidate_card:
  card_type: metric_implementation
  card_id: metric_impl.shiprocket_settlement.cod_remitted_amount
  name: Shiprocket COD Remitted Amount Implementation
  fields:
    name: Shiprocket COD Remitted Amount Implementation
    description: COD Remitted Amount implementation for Shiprocket using shiprocket_settlement.
    status: active
    confidence: curated
    source_documents:
    - Logistics KB Doc.docx
    - Cognee KB Design v4.md
    - logistics_gold_std_raw_md_frame_v3.md
    - logistics_gold_std_canonical_card_frame_v5.md
    created_by: kb_authoring_assistant
    updated_by: kb_authoring_assistant
    version: 5.0-manifest-aligned
    metric_id: metric.cod_remitted_amount
    implementation_name: Shiprocket COD Remitted Amount
    metric_pattern: settlement_sum_or_lag
    applicability: platform=shiprocket; table=zs_observe.shiprocket_settlement; account filters via Account Data Binding only
    base_tables:
    - table.zs_observe.shiprocket_settlement
    required_columns:
    - column.zs_observe.shiprocket_settlement.charged_amount
    semantic_filters: []
    formula_description: SUM(charged_amount)
    formula_sql: SUM(charged_amount)
    dependent_metrics: []
    allowed_dimensions:
    - courier_partner
    - date
    - awb
    allowed_grains:
    - awb
    - order
    - day
    - month
    - courier_partner
    - batch where safe
    recommended_date_columns:
    - settlement_date
    - delivered_date
    unit: currency/count/percentage/days_by_metric
    precision: 2_decimal_places
    caveats: charged_amount in shiprocket_settlement means COD collected/remitted, not freight.
    evidence_refs:
    - evidence.logistics_kb_doc
    - evidence.cognee_design_v4
    - evidence.unified_edge_scope
```
```yaml
candidate_card:
  card_type: metric_implementation
  card_id: metric_impl.shiprocket_settlement.cod_remittance_lag_days
  name: Shiprocket COD Remittance Lag Days Implementation
  fields:
    name: Shiprocket COD Remittance Lag Days Implementation
    description: COD Remittance Lag Days implementation for Shiprocket using shiprocket_settlement.
    status: active
    confidence: curated
    source_documents:
    - Logistics KB Doc.docx
    - Cognee KB Design v4.md
    - logistics_gold_std_raw_md_frame_v3.md
    - logistics_gold_std_canonical_card_frame_v5.md
    created_by: kb_authoring_assistant
    updated_by: kb_authoring_assistant
    version: 5.0-manifest-aligned
    metric_id: metric.cod_remittance_lag_days
    implementation_name: Shiprocket COD Remittance Lag Days
    metric_pattern: settlement_sum_or_lag
    applicability: platform=shiprocket; table=zs_observe.shiprocket_settlement; account filters via Account Data Binding only
    base_tables:
    - table.zs_observe.shiprocket_settlement
    required_columns:
    - column.zs_observe.shiprocket_settlement.delivered_date
    - column.zs_observe.shiprocket_settlement.settlement_date
    semantic_filters: []
    formula_description: AVG(DATE_DIFF('day', delivered_date, settlement_date))
    formula_sql: AVG(DATE_DIFF('day', delivered_date, settlement_date))
    dependent_metrics: []
    allowed_dimensions:
    - courier_partner
    - date
    - awb
    allowed_grains:
    - awb
    - order
    - day
    - month
    - courier_partner
    - batch where safe
    recommended_date_columns:
    - settlement_date
    - delivered_date
    unit: currency/count/percentage/days_by_metric
    precision: 2_decimal_places
    caveats: charged_amount in shiprocket_settlement means COD collected/remitted, not freight.
    evidence_refs:
    - evidence.logistics_kb_doc
    - evidence.cognee_design_v4
    - evidence.unified_edge_scope
```
```yaml
candidate_card:
  card_type: metric_implementation
  card_id: metric_impl.shiprocket_settlement.unique_awb_count
  name: Shiprocket Unique AWB Count Implementation
  fields:
    name: Shiprocket Unique AWB Count Implementation
    description: Unique AWB Count implementation for Shiprocket using shiprocket_settlement.
    status: active
    confidence: curated
    source_documents:
    - Logistics KB Doc.docx
    - Cognee KB Design v4.md
    - logistics_gold_std_raw_md_frame_v3.md
    - logistics_gold_std_canonical_card_frame_v5.md
    created_by: kb_authoring_assistant
    updated_by: kb_authoring_assistant
    version: 5.0-manifest-aligned
    metric_id: metric.unique_awb_count
    implementation_name: Shiprocket Unique AWB Count
    metric_pattern: settlement_sum_or_lag
    applicability: platform=shiprocket; table=zs_observe.shiprocket_settlement; account filters via Account Data Binding only
    base_tables:
    - table.zs_observe.shiprocket_settlement
    required_columns:
    - column.zs_observe.shiprocket_settlement.awb_number
    semantic_filters: []
    formula_description: COUNT(DISTINCT awb_number)
    formula_sql: COUNT(DISTINCT awb_number)
    dependent_metrics: []
    allowed_dimensions:
    - courier_partner
    - date
    - awb
    allowed_grains:
    - awb
    - order
    - day
    - month
    - courier_partner
    - batch where safe
    recommended_date_columns:
    - settlement_date
    - delivered_date
    unit: currency/count/percentage/days_by_metric
    precision: 2_decimal_places
    caveats: charged_amount in shiprocket_settlement means COD collected/remitted, not freight.
    evidence_refs:
    - evidence.logistics_kb_doc
    - evidence.cognee_design_v4
    - evidence.unified_edge_scope
```
```yaml
candidate_card:
  card_type: metric_implementation
  card_id: metric_impl.shiprocket_settlement_report.cod_remitted_amount.unsupported_until_loaded
  name: Shiprocket COD Remitted Amount Implementation
  fields:
    name: Shiprocket COD Remitted Amount Implementation
    description: COD Remitted Amount implementation for Shiprocket using shiprocket_settlement_report.
    status: active
    confidence: curated
    source_documents:
    - Logistics KB Doc.docx
    - Cognee KB Design v4.md
    - logistics_gold_std_raw_md_frame_v3.md
    - logistics_gold_std_canonical_card_frame_v5.md
    created_by: kb_authoring_assistant
    updated_by: kb_authoring_assistant
    version: 5.0-manifest-aligned
    metric_id: metric.cod_remitted_amount
    implementation_name: Shiprocket COD Remitted Amount
    metric_pattern: unsupported_schema_only
    applicability: platform=shiprocket; table=zs_observe.shiprocket_settlement_report; account filters via Account Data Binding only
    base_tables:
    - table.zs_observe.shiprocket_settlement_report
    required_columns:
    - column.zs_observe.shiprocket_settlement_report.settlement_id
    semantic_filters: []
    formula_description: UNSUPPORTED_EMPTY_TABLE
    formula_sql: UNSUPPORTED_EMPTY_TABLE
    dependent_metrics: []
    allowed_dimensions:
    - courier_partner
    - date
    - awb
    allowed_grains:
    - awb
    - order
    - day
    - month
    - courier_partner
    - batch where safe
    recommended_date_columns:
    - none
    unit: currency/count/percentage/days_by_metric
    precision: 2_decimal_places
    caveats: shiprocket_settlement_report has zero rows; retain schema only until data loads.
    evidence_refs:
    - evidence.logistics_kb_doc
    - evidence.cognee_design_v4
    - evidence.unified_edge_scope
```
```yaml
candidate_card:
  card_type: metric_implementation
  card_id: metric_impl.shiprocket_settlement_report.batch_settlement_amount.unsupported_until_loaded
  name: Shiprocket Batch Settlement Amount Implementation
  fields:
    name: Shiprocket Batch Settlement Amount Implementation
    description: Batch Settlement Amount implementation for Shiprocket using shiprocket_settlement_report.
    status: active
    confidence: curated
    source_documents:
    - Logistics KB Doc.docx
    - Cognee KB Design v4.md
    - logistics_gold_std_raw_md_frame_v3.md
    - logistics_gold_std_canonical_card_frame_v5.md
    created_by: kb_authoring_assistant
    updated_by: kb_authoring_assistant
    version: 5.0-manifest-aligned
    metric_id: metric.batch_settlement_amount
    implementation_name: Shiprocket Batch Settlement Amount
    metric_pattern: unsupported_schema_only
    applicability: platform=shiprocket; table=zs_observe.shiprocket_settlement_report; account filters via Account Data Binding only
    base_tables:
    - table.zs_observe.shiprocket_settlement_report
    required_columns:
    - column.zs_observe.shiprocket_settlement_report.settlement_id
    semantic_filters: []
    formula_description: UNSUPPORTED_EMPTY_TABLE
    formula_sql: UNSUPPORTED_EMPTY_TABLE
    dependent_metrics: []
    allowed_dimensions:
    - courier_partner
    - date
    - awb
    allowed_grains:
    - awb
    - order
    - day
    - month
    - courier_partner
    - batch where safe
    recommended_date_columns:
    - none
    unit: currency/count/percentage/days_by_metric
    precision: 2_decimal_places
    caveats: shiprocket_settlement_report has zero rows; retain schema only until data loads.
    evidence_refs:
    - evidence.logistics_kb_doc
    - evidence.cognee_design_v4
    - evidence.unified_edge_scope
```

## 5. Candidate Edges — Unified Edge Taxonomy

### 5.0 Unified Edge Rules
```yaml
unified_edge_rules:
  canonical_edge_format: UPPERCASE_UNDERSCORE
  accepted_legacy_aliases: true
  canonicalize_legacy_aliases_before_ingestion: true
  store_directed_edge_as_source_of_truth: true
  include_inverse_edge_type_on_every_edge: true
  materialize_inverse_when_materialize_inverse_true: true
  materialize_inverse_defaults:
    always_materialize:
    - HAS_PLATFORM_CONTEXT <-> BELONGS_TO_PLATFORM
    - HAS_COLUMN <-> BELONGS_TO_TABLE
    - HAS_IMPLEMENTATION <-> IMPLEMENTS_METRIC
    - HAS_WORKFLOW_STEP <-> BELONGS_TO_PROCESS
    - HAS_STATE_TRANSITION <-> BELONGS_TO_PROCESS
    - HAS_PROCESS_VARIANT <-> EXTENDS_PROCESS
    - HAS_RECONCILIATION_PROFILE <-> SUPPORTS_PROCESS
    - HAS_RECONCILIATION_SIDE <-> BELONGS_TO_RECONCILIATION_PROFILE
    - USES_MATCHING_LOGIC <-> SUPPORTS_RECONCILIATION_PROFILE
    index_reverse_lookup_only:
    - SOURCED_FROM_PLATFORM
    - SOURCED_FROM_PLATFORM_CONTEXT
    - USES_TABLE
    - USES_COLUMN
    - PRODUCES_METRIC
    - USES_RECONCILIATION_PROFILE
    - REQUIRES_RULE
    - USES_OUTPUT_CONTRACT
    - INCLUDES_RULE
    - INCLUDES_VALIDATION_TEST
    - APPLIES_TO_QUERY_PATTERN
  generic_logistics_boundary: Generic vendor/domain docs must not emit tenant, group, platform account, account data binding, business scope set, or business flow binding cards.
```

### 5.1 Candidate Edge Registry

```yaml
candidate_edge:
  edge_id: edge.metric.actual_weight.belongs_to_domain.domain.logistics_reconciliation
  edge_type: BELONGS_TO_DOMAIN
  source: metric.actual_weight
  target: domain.logistics_reconciliation
  fields:
    edge_family: metric_understanding
    evidence_basis: metric.fields.domain_ids
    confidence: high
    canonical_cognee_edge: true
    logistics_only: true
    canonical_edge_type: BELONGS_TO_DOMAIN
    inverse_edge_type: HAS_METRIC_OR_HAS_BUSINESS_PROCESS
    materialize_inverse: false
    edge_class: canonical
    source_type: metric
    target_type: domain
```
```yaml
candidate_edge:
  edge_id: edge.metric.average_freight_per_awb.belongs_to_domain.domain.logistics_reconciliation
  edge_type: BELONGS_TO_DOMAIN
  source: metric.average_freight_per_awb
  target: domain.logistics_reconciliation
  fields:
    edge_family: metric_understanding
    evidence_basis: metric.fields.domain_ids
    confidence: high
    canonical_cognee_edge: true
    logistics_only: true
    canonical_edge_type: BELONGS_TO_DOMAIN
    inverse_edge_type: HAS_METRIC_OR_HAS_BUSINESS_PROCESS
    materialize_inverse: false
    edge_class: canonical
    source_type: metric
    target_type: domain
```
```yaml
candidate_edge:
  edge_id: edge.metric.batch_settlement_amount.belongs_to_domain.domain.logistics_reconciliation
  edge_type: BELONGS_TO_DOMAIN
  source: metric.batch_settlement_amount
  target: domain.logistics_reconciliation
  fields:
    edge_family: metric_understanding
    evidence_basis: metric.fields.domain_ids
    confidence: high
    canonical_cognee_edge: true
    logistics_only: true
    canonical_edge_type: BELONGS_TO_DOMAIN
    inverse_edge_type: HAS_METRIC_OR_HAS_BUSINESS_PROCESS
    materialize_inverse: false
    edge_class: canonical
    source_type: metric
    target_type: domain
```
```yaml
candidate_edge:
  edge_id: edge.metric.billable_weight.belongs_to_domain.domain.logistics_reconciliation
  edge_type: BELONGS_TO_DOMAIN
  source: metric.billable_weight
  target: domain.logistics_reconciliation
  fields:
    edge_family: metric_understanding
    evidence_basis: metric.fields.domain_ids
    confidence: high
    canonical_cognee_edge: true
    logistics_only: true
    canonical_edge_type: BELONGS_TO_DOMAIN
    inverse_edge_type: HAS_METRIC_OR_HAS_BUSINESS_PROCESS
    materialize_inverse: false
    edge_class: canonical
    source_type: metric
    target_type: domain
```
```yaml
candidate_edge:
  edge_id: edge.metric.cod_collected_amount.belongs_to_domain.domain.logistics_reconciliation
  edge_type: BELONGS_TO_DOMAIN
  source: metric.cod_collected_amount
  target: domain.logistics_reconciliation
  fields:
    edge_family: metric_understanding
    evidence_basis: metric.fields.domain_ids
    confidence: high
    canonical_cognee_edge: true
    logistics_only: true
    canonical_edge_type: BELONGS_TO_DOMAIN
    inverse_edge_type: HAS_METRIC_OR_HAS_BUSINESS_PROCESS
    materialize_inverse: false
    edge_class: canonical
    source_type: metric
    target_type: domain
```
```yaml
candidate_edge:
  edge_id: edge.metric.cod_fee_amount.belongs_to_domain.domain.logistics_reconciliation
  edge_type: BELONGS_TO_DOMAIN
  source: metric.cod_fee_amount
  target: domain.logistics_reconciliation
  fields:
    edge_family: metric_understanding
    evidence_basis: metric.fields.domain_ids
    confidence: high
    canonical_cognee_edge: true
    logistics_only: true
    canonical_edge_type: BELONGS_TO_DOMAIN
    inverse_edge_type: HAS_METRIC_OR_HAS_BUSINESS_PROCESS
    materialize_inverse: false
    edge_class: canonical
    source_type: metric
    target_type: domain
```
```yaml
candidate_edge:
  edge_id: edge.metric.cod_remittance_lag_days.belongs_to_domain.domain.logistics_reconciliation
  edge_type: BELONGS_TO_DOMAIN
  source: metric.cod_remittance_lag_days
  target: domain.logistics_reconciliation
  fields:
    edge_family: metric_understanding
    evidence_basis: metric.fields.domain_ids
    confidence: high
    canonical_cognee_edge: true
    logistics_only: true
    canonical_edge_type: BELONGS_TO_DOMAIN
    inverse_edge_type: HAS_METRIC_OR_HAS_BUSINESS_PROCESS
    materialize_inverse: false
    edge_class: canonical
    source_type: metric
    target_type: domain
```
```yaml
candidate_edge:
  edge_id: edge.metric.cod_remitted_amount.belongs_to_domain.domain.logistics_reconciliation
  edge_type: BELONGS_TO_DOMAIN
  source: metric.cod_remitted_amount
  target: domain.logistics_reconciliation
  fields:
    edge_family: metric_understanding
    evidence_basis: metric.fields.domain_ids
    confidence: high
    canonical_cognee_edge: true
    logistics_only: true
    canonical_edge_type: BELONGS_TO_DOMAIN
    inverse_edge_type: HAS_METRIC_OR_HAS_BUSINESS_PROCESS
    materialize_inverse: false
    edge_class: canonical
    source_type: metric
    target_type: domain
```
```yaml
candidate_edge:
  edge_id: edge.metric.forward_freight_amount.belongs_to_domain.domain.logistics_reconciliation
  edge_type: BELONGS_TO_DOMAIN
  source: metric.forward_freight_amount
  target: domain.logistics_reconciliation
  fields:
    edge_family: metric_understanding
    evidence_basis: metric.fields.domain_ids
    confidence: high
    canonical_cognee_edge: true
    logistics_only: true
    canonical_edge_type: BELONGS_TO_DOMAIN
    inverse_edge_type: HAS_METRIC_OR_HAS_BUSINESS_PROCESS
    materialize_inverse: false
    edge_class: canonical
    source_type: metric
    target_type: domain
```
```yaml
candidate_edge:
  edge_id: edge.metric.freight_billed_amount.belongs_to_domain.domain.logistics_reconciliation
  edge_type: BELONGS_TO_DOMAIN
  source: metric.freight_billed_amount
  target: domain.logistics_reconciliation
  fields:
    edge_family: metric_understanding
    evidence_basis: metric.fields.domain_ids
    confidence: high
    canonical_cognee_edge: true
    logistics_only: true
    canonical_edge_type: BELONGS_TO_DOMAIN
    inverse_edge_type: HAS_METRIC_OR_HAS_BUSINESS_PROCESS
    materialize_inverse: false
    edge_class: canonical
    source_type: metric
    target_type: domain
```
```yaml
candidate_edge:
  edge_id: edge.metric.freight_excluding_tax_amount.belongs_to_domain.domain.logistics_reconciliation
  edge_type: BELONGS_TO_DOMAIN
  source: metric.freight_excluding_tax_amount
  target: domain.logistics_reconciliation
  fields:
    edge_family: metric_understanding
    evidence_basis: metric.fields.domain_ids
    confidence: high
    canonical_cognee_edge: true
    logistics_only: true
    canonical_edge_type: BELONGS_TO_DOMAIN
    inverse_edge_type: HAS_METRIC_OR_HAS_BUSINESS_PROCESS
    materialize_inverse: false
    edge_class: canonical
    source_type: metric
    target_type: domain
```
```yaml
candidate_edge:
  edge_id: edge.metric.fuel_surcharge_amount.belongs_to_domain.domain.logistics_reconciliation
  edge_type: BELONGS_TO_DOMAIN
  source: metric.fuel_surcharge_amount
  target: domain.logistics_reconciliation
  fields:
    edge_family: metric_understanding
    evidence_basis: metric.fields.domain_ids
    confidence: high
    canonical_cognee_edge: true
    logistics_only: true
    canonical_edge_type: BELONGS_TO_DOMAIN
    inverse_edge_type: HAS_METRIC_OR_HAS_BUSINESS_PROCESS
    materialize_inverse: false
    edge_class: canonical
    source_type: metric
    target_type: domain
```
```yaml
candidate_edge:
  edge_id: edge.metric.gst_on_freight_amount.belongs_to_domain.domain.logistics_reconciliation
  edge_type: BELONGS_TO_DOMAIN
  source: metric.gst_on_freight_amount
  target: domain.logistics_reconciliation
  fields:
    edge_family: metric_understanding
    evidence_basis: metric.fields.domain_ids
    confidence: high
    canonical_cognee_edge: true
    logistics_only: true
    canonical_edge_type: BELONGS_TO_DOMAIN
    inverse_edge_type: HAS_METRIC_OR_HAS_BUSINESS_PROCESS
    materialize_inverse: false
    edge_class: canonical
    source_type: metric
    target_type: domain
```
```yaml
candidate_edge:
  edge_id: edge.metric.rto_freight_amount.belongs_to_domain.domain.logistics_reconciliation
  edge_type: BELONGS_TO_DOMAIN
  source: metric.rto_freight_amount
  target: domain.logistics_reconciliation
  fields:
    edge_family: metric_understanding
    evidence_basis: metric.fields.domain_ids
    confidence: high
    canonical_cognee_edge: true
    logistics_only: true
    canonical_edge_type: BELONGS_TO_DOMAIN
    inverse_edge_type: HAS_METRIC_OR_HAS_BUSINESS_PROCESS
    materialize_inverse: false
    edge_class: canonical
    source_type: metric
    target_type: domain
```
```yaml
candidate_edge:
  edge_id: edge.metric.unique_awb_count.belongs_to_domain.domain.logistics_reconciliation
  edge_type: BELONGS_TO_DOMAIN
  source: metric.unique_awb_count
  target: domain.logistics_reconciliation
  fields:
    edge_family: metric_understanding
    evidence_basis: metric.fields.domain_ids
    confidence: high
    canonical_cognee_edge: true
    logistics_only: true
    canonical_edge_type: BELONGS_TO_DOMAIN
    inverse_edge_type: HAS_METRIC_OR_HAS_BUSINESS_PROCESS
    materialize_inverse: false
    edge_class: canonical
    source_type: metric
    target_type: domain
```
```yaml
candidate_edge:
  edge_id: edge.platform_context.shiprocket.in.belongs_to_platform.platform.shiprocket
  edge_type: BELONGS_TO_PLATFORM
  source: platform_context.shiprocket.in
  target: platform.shiprocket
  fields:
    edge_family: platform_context
    evidence_basis: platform_context.fields.platform_id
    confidence: high
    canonical_cognee_edge: true
    logistics_only: true
    canonical_edge_type: BELONGS_TO_PLATFORM
    inverse_edge_type: HAS_PLATFORM_CONTEXT
    materialize_inverse: true
    edge_class: canonical
    source_type: platform_context
    target_type: platform
```
```yaml
candidate_edge:
  edge_id: edge.platform.shiprocket.has_platform_context.platform_context.shiprocket.in
  edge_type: HAS_PLATFORM_CONTEXT
  source: platform.shiprocket
  target: platform_context.shiprocket.in
  fields:
    edge_family: platform_context
    evidence_basis: materialized inverse of BELONGS_TO_PLATFORM
    confidence: high
    canonical_cognee_edge: true
    logistics_only: true
    canonical_edge_type: HAS_PLATFORM_CONTEXT
    inverse_edge_type: BELONGS_TO_PLATFORM
    materialize_inverse: true
    edge_class: canonical
    source_type: platform
    target_type: platform_context
    materialized_from: edge.platform_context.shiprocket.in.belongs_to_platform.platform.shiprocket
```
```yaml
candidate_edge:
  edge_id: edge.table.zs_observe.shiprocket_invoice.sourced_from_platform.platform.shiprocket
  edge_type: SOURCED_FROM_PLATFORM
  source: table.zs_observe.shiprocket_invoice
  target: platform.shiprocket
  fields:
    edge_family: platform_context
    evidence_basis: table.fields.source_platform_ids
    confidence: high
    canonical_cognee_edge: true
    logistics_only: true
    canonical_edge_type: SOURCED_FROM_PLATFORM
    inverse_edge_type: HAS_SOURCE_TABLE
    materialize_inverse: false
    edge_class: canonical
    source_type: table
    target_type: platform
```
```yaml
candidate_edge:
  edge_id: edge.table.zs_observe.shiprocket_invoice.applies_to_platform.platform.shiprocket
  edge_type: APPLIES_TO_PLATFORM
  source: table.zs_observe.shiprocket_invoice
  target: platform.shiprocket
  fields:
    edge_family: applicability
    evidence_basis: table.fields.structural_applicability
    confidence: high
    canonical_cognee_edge: true
    logistics_only: true
    canonical_edge_type: APPLIES_TO_PLATFORM
    inverse_edge_type: HAS_APPLICABLE_CARD
    materialize_inverse: false
    edge_class: canonical
    source_type: table
    target_type: platform
```
```yaml
candidate_edge:
  edge_id: edge.table.zs_observe.shiprocket_invoice.has_column.column.zs_observe.shiprocket_invoice.order_id
  edge_type: HAS_COLUMN
  source: table.zs_observe.shiprocket_invoice
  target: column.zs_observe.shiprocket_invoice.order_id
  fields:
    edge_family: data_understanding
    evidence_basis: column.fields.table_id
    confidence: high
    canonical_cognee_edge: true
    logistics_only: true
    canonical_edge_type: HAS_COLUMN
    inverse_edge_type: BELONGS_TO_TABLE
    materialize_inverse: true
    edge_class: canonical
    source_type: table
    target_type: column
```
```yaml
candidate_edge:
  edge_id: edge.column.zs_observe.shiprocket_invoice.order_id.belongs_to_table.table.zs_observe.shiprocket_invoice
  edge_type: BELONGS_TO_TABLE
  source: column.zs_observe.shiprocket_invoice.order_id
  target: table.zs_observe.shiprocket_invoice
  fields:
    edge_family: data_understanding
    evidence_basis: materialized inverse of HAS_COLUMN
    confidence: high
    canonical_cognee_edge: true
    logistics_only: true
    canonical_edge_type: BELONGS_TO_TABLE
    inverse_edge_type: HAS_COLUMN
    materialize_inverse: true
    edge_class: canonical
    source_type: column
    target_type: table
    materialized_from: edge.table.zs_observe.shiprocket_invoice.has_column.column.zs_observe.shiprocket_invoice.order_id
```
```yaml
candidate_edge:
  edge_id: edge.table.zs_observe.shiprocket_invoice.has_column.column.zs_observe.shiprocket_invoice.other_id
  edge_type: HAS_COLUMN
  source: table.zs_observe.shiprocket_invoice
  target: column.zs_observe.shiprocket_invoice.other_id
  fields:
    edge_family: data_understanding
    evidence_basis: column.fields.table_id
    confidence: high
    canonical_cognee_edge: true
    logistics_only: true
    canonical_edge_type: HAS_COLUMN
    inverse_edge_type: BELONGS_TO_TABLE
    materialize_inverse: true
    edge_class: canonical
    source_type: table
    target_type: column
```
```yaml
candidate_edge:
  edge_id: edge.column.zs_observe.shiprocket_invoice.other_id.belongs_to_table.table.zs_observe.shiprocket_invoice
  edge_type: BELONGS_TO_TABLE
  source: column.zs_observe.shiprocket_invoice.other_id
  target: table.zs_observe.shiprocket_invoice
  fields:
    edge_family: data_understanding
    evidence_basis: materialized inverse of HAS_COLUMN
    confidence: high
    canonical_cognee_edge: true
    logistics_only: true
    canonical_edge_type: BELONGS_TO_TABLE
    inverse_edge_type: HAS_COLUMN
    materialize_inverse: true
    edge_class: canonical
    source_type: column
    target_type: table
    materialized_from: edge.table.zs_observe.shiprocket_invoice.has_column.column.zs_observe.shiprocket_invoice.other_id
```
```yaml
candidate_edge:
  edge_id: edge.table.zs_observe.shiprocket_invoice.has_column.column.zs_observe.shiprocket_invoice.courier_partner
  edge_type: HAS_COLUMN
  source: table.zs_observe.shiprocket_invoice
  target: column.zs_observe.shiprocket_invoice.courier_partner
  fields:
    edge_family: data_understanding
    evidence_basis: column.fields.table_id
    confidence: high
    canonical_cognee_edge: true
    logistics_only: true
    canonical_edge_type: HAS_COLUMN
    inverse_edge_type: BELONGS_TO_TABLE
    materialize_inverse: true
    edge_class: canonical
    source_type: table
    target_type: column
```
```yaml
candidate_edge:
  edge_id: edge.column.zs_observe.shiprocket_invoice.courier_partner.belongs_to_table.table.zs_observe.shiprocket_invoice
  edge_type: BELONGS_TO_TABLE
  source: column.zs_observe.shiprocket_invoice.courier_partner
  target: table.zs_observe.shiprocket_invoice
  fields:
    edge_family: data_understanding
    evidence_basis: materialized inverse of HAS_COLUMN
    confidence: high
    canonical_cognee_edge: true
    logistics_only: true
    canonical_edge_type: BELONGS_TO_TABLE
    inverse_edge_type: HAS_COLUMN
    materialize_inverse: true
    edge_class: canonical
    source_type: column
    target_type: table
    materialized_from: edge.table.zs_observe.shiprocket_invoice.has_column.column.zs_observe.shiprocket_invoice.courier_partner
```
```yaml
candidate_edge:
  edge_id: edge.table.zs_observe.shiprocket_invoice.has_column.column.zs_observe.shiprocket_invoice.order_status
  edge_type: HAS_COLUMN
  source: table.zs_observe.shiprocket_invoice
  target: column.zs_observe.shiprocket_invoice.order_status
  fields:
    edge_family: data_understanding
    evidence_basis: column.fields.table_id
    confidence: high
    canonical_cognee_edge: true
    logistics_only: true
    canonical_edge_type: HAS_COLUMN
    inverse_edge_type: BELONGS_TO_TABLE
    materialize_inverse: true
    edge_class: canonical
    source_type: table
    target_type: column
```
```yaml
candidate_edge:
  edge_id: edge.column.zs_observe.shiprocket_invoice.order_status.belongs_to_table.table.zs_observe.shiprocket_invoice
  edge_type: BELONGS_TO_TABLE
  source: column.zs_observe.shiprocket_invoice.order_status
  target: table.zs_observe.shiprocket_invoice
  fields:
    edge_family: data_understanding
    evidence_basis: materialized inverse of HAS_COLUMN
    confidence: high
    canonical_cognee_edge: true
    logistics_only: true
    canonical_edge_type: BELONGS_TO_TABLE
    inverse_edge_type: HAS_COLUMN
    materialize_inverse: true
    edge_class: canonical
    source_type: column
    target_type: table
    materialized_from: edge.table.zs_observe.shiprocket_invoice.has_column.column.zs_observe.shiprocket_invoice.order_status
```
```yaml
candidate_edge:
  edge_id: edge.table.zs_observe.shiprocket_invoice.has_column.column.zs_observe.shiprocket_invoice.zone
  edge_type: HAS_COLUMN
  source: table.zs_observe.shiprocket_invoice
  target: column.zs_observe.shiprocket_invoice.zone
  fields:
    edge_family: data_understanding
    evidence_basis: column.fields.table_id
    confidence: high
    canonical_cognee_edge: true
    logistics_only: true
    canonical_edge_type: HAS_COLUMN
    inverse_edge_type: BELONGS_TO_TABLE
    materialize_inverse: true
    edge_class: canonical
    source_type: table
    target_type: column
```
```yaml
candidate_edge:
  edge_id: edge.column.zs_observe.shiprocket_invoice.zone.belongs_to_table.table.zs_observe.shiprocket_invoice
  edge_type: BELONGS_TO_TABLE
  source: column.zs_observe.shiprocket_invoice.zone
  target: table.zs_observe.shiprocket_invoice
  fields:
    edge_family: data_understanding
    evidence_basis: materialized inverse of HAS_COLUMN
    confidence: high
    canonical_cognee_edge: true
    logistics_only: true
    canonical_edge_type: BELONGS_TO_TABLE
    inverse_edge_type: HAS_COLUMN
    materialize_inverse: true
    edge_class: canonical
    source_type: column
    target_type: table
    materialized_from: edge.table.zs_observe.shiprocket_invoice.has_column.column.zs_observe.shiprocket_invoice.zone
```
```yaml
candidate_edge:
  edge_id: edge.table.zs_observe.shiprocket_invoice.has_column.column.zs_observe.shiprocket_invoice.payment_mode
  edge_type: HAS_COLUMN
  source: table.zs_observe.shiprocket_invoice
  target: column.zs_observe.shiprocket_invoice.payment_mode
  fields:
    edge_family: data_understanding
    evidence_basis: column.fields.table_id
    confidence: high
    canonical_cognee_edge: true
    logistics_only: true
    canonical_edge_type: HAS_COLUMN
    inverse_edge_type: BELONGS_TO_TABLE
    materialize_inverse: true
    edge_class: canonical
    source_type: table
    target_type: column
```
```yaml
candidate_edge:
  edge_id: edge.column.zs_observe.shiprocket_invoice.payment_mode.belongs_to_table.table.zs_observe.shiprocket_invoice
  edge_type: BELONGS_TO_TABLE
  source: column.zs_observe.shiprocket_invoice.payment_mode
  target: table.zs_observe.shiprocket_invoice
  fields:
    edge_family: data_understanding
    evidence_basis: materialized inverse of HAS_COLUMN
    confidence: high
    canonical_cognee_edge: true
    logistics_only: true
    canonical_edge_type: BELONGS_TO_TABLE
    inverse_edge_type: HAS_COLUMN
    materialize_inverse: true
    edge_class: canonical
    source_type: column
    target_type: table
    materialized_from: edge.table.zs_observe.shiprocket_invoice.has_column.column.zs_observe.shiprocket_invoice.payment_mode
```
```yaml
candidate_edge:
  edge_id: edge.table.zs_observe.shiprocket_invoice.has_column.column.zs_observe.shiprocket_invoice.charged_amount
  edge_type: HAS_COLUMN
  source: table.zs_observe.shiprocket_invoice
  target: column.zs_observe.shiprocket_invoice.charged_amount
  fields:
    edge_family: data_understanding
    evidence_basis: column.fields.table_id
    confidence: high
    canonical_cognee_edge: true
    logistics_only: true
    canonical_edge_type: HAS_COLUMN
    inverse_edge_type: BELONGS_TO_TABLE
    materialize_inverse: true
    edge_class: canonical
    source_type: table
    target_type: column
```
```yaml
candidate_edge:
  edge_id: edge.column.zs_observe.shiprocket_invoice.charged_amount.belongs_to_table.table.zs_observe.shiprocket_invoice
  edge_type: BELONGS_TO_TABLE
  source: column.zs_observe.shiprocket_invoice.charged_amount
  target: table.zs_observe.shiprocket_invoice
  fields:
    edge_family: data_understanding
    evidence_basis: materialized inverse of HAS_COLUMN
    confidence: high
    canonical_cognee_edge: true
    logistics_only: true
    canonical_edge_type: BELONGS_TO_TABLE
    inverse_edge_type: HAS_COLUMN
    materialize_inverse: true
    edge_class: canonical
    source_type: column
    target_type: table
    materialized_from: edge.table.zs_observe.shiprocket_invoice.has_column.column.zs_observe.shiprocket_invoice.charged_amount
```
```yaml
candidate_edge:
  edge_id: edge.table.zs_observe.shiprocket_invoice.has_column.column.zs_observe.shiprocket_invoice.charged_amount_excluding_tax
  edge_type: HAS_COLUMN
  source: table.zs_observe.shiprocket_invoice
  target: column.zs_observe.shiprocket_invoice.charged_amount_excluding_tax
  fields:
    edge_family: data_understanding
    evidence_basis: column.fields.table_id
    confidence: high
    canonical_cognee_edge: true
    logistics_only: true
    canonical_edge_type: HAS_COLUMN
    inverse_edge_type: BELONGS_TO_TABLE
    materialize_inverse: true
    edge_class: canonical
    source_type: table
    target_type: column
```
```yaml
candidate_edge:
  edge_id: edge.column.zs_observe.shiprocket_invoice.charged_amount_excluding_tax.belongs_to_table.table.zs_observe.shiprocket_invoice
  edge_type: BELONGS_TO_TABLE
  source: column.zs_observe.shiprocket_invoice.charged_amount_excluding_tax
  target: table.zs_observe.shiprocket_invoice
  fields:
    edge_family: data_understanding
    evidence_basis: materialized inverse of HAS_COLUMN
    confidence: high
    canonical_cognee_edge: true
    logistics_only: true
    canonical_edge_type: BELONGS_TO_TABLE
    inverse_edge_type: HAS_COLUMN
    materialize_inverse: true
    edge_class: canonical
    source_type: column
    target_type: table
    materialized_from: edge.table.zs_observe.shiprocket_invoice.has_column.column.zs_observe.shiprocket_invoice.charged_amount_excluding_tax
```
```yaml
candidate_edge:
  edge_id: edge.table.zs_observe.shiprocket_invoice.has_column.column.zs_observe.shiprocket_invoice.total_tax
  edge_type: HAS_COLUMN
  source: table.zs_observe.shiprocket_invoice
  target: column.zs_observe.shiprocket_invoice.total_tax
  fields:
    edge_family: data_understanding
    evidence_basis: column.fields.table_id
    confidence: high
    canonical_cognee_edge: true
    logistics_only: true
    canonical_edge_type: HAS_COLUMN
    inverse_edge_type: BELONGS_TO_TABLE
    materialize_inverse: true
    edge_class: canonical
    source_type: table
    target_type: column
```
```yaml
candidate_edge:
  edge_id: edge.column.zs_observe.shiprocket_invoice.total_tax.belongs_to_table.table.zs_observe.shiprocket_invoice
  edge_type: BELONGS_TO_TABLE
  source: column.zs_observe.shiprocket_invoice.total_tax
  target: table.zs_observe.shiprocket_invoice
  fields:
    edge_family: data_understanding
    evidence_basis: materialized inverse of HAS_COLUMN
    confidence: high
    canonical_cognee_edge: true
    logistics_only: true
    canonical_edge_type: BELONGS_TO_TABLE
    inverse_edge_type: HAS_COLUMN
    materialize_inverse: true
    edge_class: canonical
    source_type: column
    target_type: table
    materialized_from: edge.table.zs_observe.shiprocket_invoice.has_column.column.zs_observe.shiprocket_invoice.total_tax
```
```yaml
candidate_edge:
  edge_id: edge.table.zs_observe.shiprocket_invoice.has_column.column.zs_observe.shiprocket_invoice.charge_fsc
  edge_type: HAS_COLUMN
  source: table.zs_observe.shiprocket_invoice
  target: column.zs_observe.shiprocket_invoice.charge_fsc
  fields:
    edge_family: data_understanding
    evidence_basis: column.fields.table_id
    confidence: high
    canonical_cognee_edge: true
    logistics_only: true
    canonical_edge_type: HAS_COLUMN
    inverse_edge_type: BELONGS_TO_TABLE
    materialize_inverse: true
    edge_class: canonical
    source_type: table
    target_type: column
```
```yaml
candidate_edge:
  edge_id: edge.column.zs_observe.shiprocket_invoice.charge_fsc.belongs_to_table.table.zs_observe.shiprocket_invoice
  edge_type: BELONGS_TO_TABLE
  source: column.zs_observe.shiprocket_invoice.charge_fsc
  target: table.zs_observe.shiprocket_invoice
  fields:
    edge_family: data_understanding
    evidence_basis: materialized inverse of HAS_COLUMN
    confidence: high
    canonical_cognee_edge: true
    logistics_only: true
    canonical_edge_type: BELONGS_TO_TABLE
    inverse_edge_type: HAS_COLUMN
    materialize_inverse: true
    edge_class: canonical
    source_type: column
    target_type: table
    materialized_from: edge.table.zs_observe.shiprocket_invoice.has_column.column.zs_observe.shiprocket_invoice.charge_fsc
```
```yaml
candidate_edge:
  edge_id: edge.table.zs_observe.shiprocket_invoice.has_column.column.zs_observe.shiprocket_invoice.charge_rto
  edge_type: HAS_COLUMN
  source: table.zs_observe.shiprocket_invoice
  target: column.zs_observe.shiprocket_invoice.charge_rto
  fields:
    edge_family: data_understanding
    evidence_basis: column.fields.table_id
    confidence: high
    canonical_cognee_edge: true
    logistics_only: true
    canonical_edge_type: HAS_COLUMN
    inverse_edge_type: BELONGS_TO_TABLE
    materialize_inverse: true
    edge_class: canonical
    source_type: table
    target_type: column
```
```yaml
candidate_edge:
  edge_id: edge.column.zs_observe.shiprocket_invoice.charge_rto.belongs_to_table.table.zs_observe.shiprocket_invoice
  edge_type: BELONGS_TO_TABLE
  source: column.zs_observe.shiprocket_invoice.charge_rto
  target: table.zs_observe.shiprocket_invoice
  fields:
    edge_family: data_understanding
    evidence_basis: materialized inverse of HAS_COLUMN
    confidence: high
    canonical_cognee_edge: true
    logistics_only: true
    canonical_edge_type: BELONGS_TO_TABLE
    inverse_edge_type: HAS_COLUMN
    materialize_inverse: true
    edge_class: canonical
    source_type: column
    target_type: table
    materialized_from: edge.table.zs_observe.shiprocket_invoice.has_column.column.zs_observe.shiprocket_invoice.charge_rto
```
```yaml
candidate_edge:
  edge_id: edge.table.zs_observe.shiprocket_invoice.has_column.column.zs_observe.shiprocket_invoice.charge_cod
  edge_type: HAS_COLUMN
  source: table.zs_observe.shiprocket_invoice
  target: column.zs_observe.shiprocket_invoice.charge_cod
  fields:
    edge_family: data_understanding
    evidence_basis: column.fields.table_id
    confidence: high
    canonical_cognee_edge: true
    logistics_only: true
    canonical_edge_type: HAS_COLUMN
    inverse_edge_type: BELONGS_TO_TABLE
    materialize_inverse: true
    edge_class: canonical
    source_type: table
    target_type: column
```
```yaml
candidate_edge:
  edge_id: edge.column.zs_observe.shiprocket_invoice.charge_cod.belongs_to_table.table.zs_observe.shiprocket_invoice
  edge_type: BELONGS_TO_TABLE
  source: column.zs_observe.shiprocket_invoice.charge_cod
  target: table.zs_observe.shiprocket_invoice
  fields:
    edge_family: data_understanding
    evidence_basis: materialized inverse of HAS_COLUMN
    confidence: high
    canonical_cognee_edge: true
    logistics_only: true
    canonical_edge_type: BELONGS_TO_TABLE
    inverse_edge_type: HAS_COLUMN
    materialize_inverse: true
    edge_class: canonical
    source_type: column
    target_type: table
    materialized_from: edge.table.zs_observe.shiprocket_invoice.has_column.column.zs_observe.shiprocket_invoice.charge_cod
```
```yaml
candidate_edge:
  edge_id: edge.table.zs_observe.shiprocket_invoice.has_column.column.zs_observe.shiprocket_invoice.charge_cod_adjust
  edge_type: HAS_COLUMN
  source: table.zs_observe.shiprocket_invoice
  target: column.zs_observe.shiprocket_invoice.charge_cod_adjust
  fields:
    edge_family: data_understanding
    evidence_basis: column.fields.table_id
    confidence: high
    canonical_cognee_edge: true
    logistics_only: true
    canonical_edge_type: HAS_COLUMN
    inverse_edge_type: BELONGS_TO_TABLE
    materialize_inverse: true
    edge_class: canonical
    source_type: table
    target_type: column
```
```yaml
candidate_edge:
  edge_id: edge.column.zs_observe.shiprocket_invoice.charge_cod_adjust.belongs_to_table.table.zs_observe.shiprocket_invoice
  edge_type: BELONGS_TO_TABLE
  source: column.zs_observe.shiprocket_invoice.charge_cod_adjust
  target: table.zs_observe.shiprocket_invoice
  fields:
    edge_family: data_understanding
    evidence_basis: materialized inverse of HAS_COLUMN
    confidence: high
    canonical_cognee_edge: true
    logistics_only: true
    canonical_edge_type: BELONGS_TO_TABLE
    inverse_edge_type: HAS_COLUMN
    materialize_inverse: true
    edge_class: canonical
    source_type: column
    target_type: table
    materialized_from: edge.table.zs_observe.shiprocket_invoice.has_column.column.zs_observe.shiprocket_invoice.charge_cod_adjust
```
```yaml
candidate_edge:
  edge_id: edge.table.zs_observe.shiprocket_invoice.has_column.column.zs_observe.shiprocket_invoice.charge_dl
  edge_type: HAS_COLUMN
  source: table.zs_observe.shiprocket_invoice
  target: column.zs_observe.shiprocket_invoice.charge_dl
  fields:
    edge_family: data_understanding
    evidence_basis: column.fields.table_id
    confidence: high
    canonical_cognee_edge: true
    logistics_only: true
    canonical_edge_type: HAS_COLUMN
    inverse_edge_type: BELONGS_TO_TABLE
    materialize_inverse: true
    edge_class: canonical
    source_type: table
    target_type: column
```
```yaml
candidate_edge:
  edge_id: edge.column.zs_observe.shiprocket_invoice.charge_dl.belongs_to_table.table.zs_observe.shiprocket_invoice
  edge_type: BELONGS_TO_TABLE
  source: column.zs_observe.shiprocket_invoice.charge_dl
  target: table.zs_observe.shiprocket_invoice
  fields:
    edge_family: data_understanding
    evidence_basis: materialized inverse of HAS_COLUMN
    confidence: high
    canonical_cognee_edge: true
    logistics_only: true
    canonical_edge_type: BELONGS_TO_TABLE
    inverse_edge_type: HAS_COLUMN
    materialize_inverse: true
    edge_class: canonical
    source_type: column
    target_type: table
    materialized_from: edge.table.zs_observe.shiprocket_invoice.has_column.column.zs_observe.shiprocket_invoice.charge_dl
```
```yaml
candidate_edge:
  edge_id: edge.table.zs_observe.shiprocket_invoice.has_column.column.zs_observe.shiprocket_invoice.final_weight
  edge_type: HAS_COLUMN
  source: table.zs_observe.shiprocket_invoice
  target: column.zs_observe.shiprocket_invoice.final_weight
  fields:
    edge_family: data_understanding
    evidence_basis: column.fields.table_id
    confidence: high
    canonical_cognee_edge: true
    logistics_only: true
    canonical_edge_type: HAS_COLUMN
    inverse_edge_type: BELONGS_TO_TABLE
    materialize_inverse: true
    edge_class: canonical
    source_type: table
    target_type: column
```
```yaml
candidate_edge:
  edge_id: edge.column.zs_observe.shiprocket_invoice.final_weight.belongs_to_table.table.zs_observe.shiprocket_invoice
  edge_type: BELONGS_TO_TABLE
  source: column.zs_observe.shiprocket_invoice.final_weight
  target: table.zs_observe.shiprocket_invoice
  fields:
    edge_family: data_understanding
    evidence_basis: materialized inverse of HAS_COLUMN
    confidence: high
    canonical_cognee_edge: true
    logistics_only: true
    canonical_edge_type: BELONGS_TO_TABLE
    inverse_edge_type: HAS_COLUMN
    materialize_inverse: true
    edge_class: canonical
    source_type: column
    target_type: table
    materialized_from: edge.table.zs_observe.shiprocket_invoice.has_column.column.zs_observe.shiprocket_invoice.final_weight
```
```yaml
candidate_edge:
  edge_id: edge.table.zs_observe.shiprocket_invoice.has_column.column.zs_observe.shiprocket_invoice.charged_weight
  edge_type: HAS_COLUMN
  source: table.zs_observe.shiprocket_invoice
  target: column.zs_observe.shiprocket_invoice.charged_weight
  fields:
    edge_family: data_understanding
    evidence_basis: column.fields.table_id
    confidence: high
    canonical_cognee_edge: true
    logistics_only: true
    canonical_edge_type: HAS_COLUMN
    inverse_edge_type: BELONGS_TO_TABLE
    materialize_inverse: true
    edge_class: canonical
    source_type: table
    target_type: column
```
```yaml
candidate_edge:
  edge_id: edge.column.zs_observe.shiprocket_invoice.charged_weight.belongs_to_table.table.zs_observe.shiprocket_invoice
  edge_type: BELONGS_TO_TABLE
  source: column.zs_observe.shiprocket_invoice.charged_weight
  target: table.zs_observe.shiprocket_invoice
  fields:
    edge_family: data_understanding
    evidence_basis: materialized inverse of HAS_COLUMN
    confidence: high
    canonical_cognee_edge: true
    logistics_only: true
    canonical_edge_type: BELONGS_TO_TABLE
    inverse_edge_type: HAS_COLUMN
    materialize_inverse: true
    edge_class: canonical
    source_type: column
    target_type: table
    materialized_from: edge.table.zs_observe.shiprocket_invoice.has_column.column.zs_observe.shiprocket_invoice.charged_weight
```
```yaml
candidate_edge:
  edge_id: edge.table.zs_observe.shiprocket_invoice.has_column.column.zs_observe.shiprocket_invoice.settled_amount
  edge_type: HAS_COLUMN
  source: table.zs_observe.shiprocket_invoice
  target: column.zs_observe.shiprocket_invoice.settled_amount
  fields:
    edge_family: data_understanding
    evidence_basis: column.fields.table_id
    confidence: high
    canonical_cognee_edge: true
    logistics_only: true
    canonical_edge_type: HAS_COLUMN
    inverse_edge_type: BELONGS_TO_TABLE
    materialize_inverse: true
    edge_class: canonical
    source_type: table
    target_type: column
```
```yaml
candidate_edge:
  edge_id: edge.column.zs_observe.shiprocket_invoice.settled_amount.belongs_to_table.table.zs_observe.shiprocket_invoice
  edge_type: BELONGS_TO_TABLE
  source: column.zs_observe.shiprocket_invoice.settled_amount
  target: table.zs_observe.shiprocket_invoice
  fields:
    edge_family: data_understanding
    evidence_basis: materialized inverse of HAS_COLUMN
    confidence: high
    canonical_cognee_edge: true
    logistics_only: true
    canonical_edge_type: BELONGS_TO_TABLE
    inverse_edge_type: HAS_COLUMN
    materialize_inverse: true
    edge_class: canonical
    source_type: column
    target_type: table
    materialized_from: edge.table.zs_observe.shiprocket_invoice.has_column.column.zs_observe.shiprocket_invoice.settled_amount
```
```yaml
candidate_edge:
  edge_id: edge.table.zs_observe.shiprocket_invoice.has_column.column.zs_observe.shiprocket_invoice.referal_fee
  edge_type: HAS_COLUMN
  source: table.zs_observe.shiprocket_invoice
  target: column.zs_observe.shiprocket_invoice.referal_fee
  fields:
    edge_family: data_understanding
    evidence_basis: column.fields.table_id
    confidence: high
    canonical_cognee_edge: true
    logistics_only: true
    canonical_edge_type: HAS_COLUMN
    inverse_edge_type: BELONGS_TO_TABLE
    materialize_inverse: true
    edge_class: canonical
    source_type: table
    target_type: column
```
```yaml
candidate_edge:
  edge_id: edge.column.zs_observe.shiprocket_invoice.referal_fee.belongs_to_table.table.zs_observe.shiprocket_invoice
  edge_type: BELONGS_TO_TABLE
  source: column.zs_observe.shiprocket_invoice.referal_fee
  target: table.zs_observe.shiprocket_invoice
  fields:
    edge_family: data_understanding
    evidence_basis: materialized inverse of HAS_COLUMN
    confidence: high
    canonical_cognee_edge: true
    logistics_only: true
    canonical_edge_type: BELONGS_TO_TABLE
    inverse_edge_type: HAS_COLUMN
    materialize_inverse: true
    edge_class: canonical
    source_type: column
    target_type: table
    materialized_from: edge.table.zs_observe.shiprocket_invoice.has_column.column.zs_observe.shiprocket_invoice.referal_fee
```
```yaml
candidate_edge:
  edge_id: edge.table.zs_observe.shiprocket_invoice.has_column.column.zs_observe.shiprocket_invoice.mp_sin
  edge_type: HAS_COLUMN
  source: table.zs_observe.shiprocket_invoice
  target: column.zs_observe.shiprocket_invoice.mp_sin
  fields:
    edge_family: data_understanding
    evidence_basis: column.fields.table_id
    confidence: high
    canonical_cognee_edge: true
    logistics_only: true
    canonical_edge_type: HAS_COLUMN
    inverse_edge_type: BELONGS_TO_TABLE
    materialize_inverse: true
    edge_class: canonical
    source_type: table
    target_type: column
```
```yaml
candidate_edge:
  edge_id: edge.column.zs_observe.shiprocket_invoice.mp_sin.belongs_to_table.table.zs_observe.shiprocket_invoice
  edge_type: BELONGS_TO_TABLE
  source: column.zs_observe.shiprocket_invoice.mp_sin
  target: table.zs_observe.shiprocket_invoice
  fields:
    edge_family: data_understanding
    evidence_basis: materialized inverse of HAS_COLUMN
    confidence: high
    canonical_cognee_edge: true
    logistics_only: true
    canonical_edge_type: BELONGS_TO_TABLE
    inverse_edge_type: HAS_COLUMN
    materialize_inverse: true
    edge_class: canonical
    source_type: column
    target_type: table
    materialized_from: edge.table.zs_observe.shiprocket_invoice.has_column.column.zs_observe.shiprocket_invoice.mp_sin
```
```yaml
candidate_edge:
  edge_id: edge.table.zs_observe.shiprocket_invoice.has_column.column.zs_observe.shiprocket_invoice.source_zipcode
  edge_type: HAS_COLUMN
  source: table.zs_observe.shiprocket_invoice
  target: column.zs_observe.shiprocket_invoice.source_zipcode
  fields:
    edge_family: data_understanding
    evidence_basis: column.fields.table_id
    confidence: high
    canonical_cognee_edge: true
    logistics_only: true
    canonical_edge_type: HAS_COLUMN
    inverse_edge_type: BELONGS_TO_TABLE
    materialize_inverse: true
    edge_class: canonical
    source_type: table
    target_type: column
```
```yaml
candidate_edge:
  edge_id: edge.column.zs_observe.shiprocket_invoice.source_zipcode.belongs_to_table.table.zs_observe.shiprocket_invoice
  edge_type: BELONGS_TO_TABLE
  source: column.zs_observe.shiprocket_invoice.source_zipcode
  target: table.zs_observe.shiprocket_invoice
  fields:
    edge_family: data_understanding
    evidence_basis: materialized inverse of HAS_COLUMN
    confidence: high
    canonical_cognee_edge: true
    logistics_only: true
    canonical_edge_type: BELONGS_TO_TABLE
    inverse_edge_type: HAS_COLUMN
    materialize_inverse: true
    edge_class: canonical
    source_type: column
    target_type: table
    materialized_from: edge.table.zs_observe.shiprocket_invoice.has_column.column.zs_observe.shiprocket_invoice.source_zipcode
```
```yaml
candidate_edge:
  edge_id: edge.table.zs_observe.shiprocket_invoice.has_column.column.zs_observe.shiprocket_invoice.destination_zipcode
  edge_type: HAS_COLUMN
  source: table.zs_observe.shiprocket_invoice
  target: column.zs_observe.shiprocket_invoice.destination_zipcode
  fields:
    edge_family: data_understanding
    evidence_basis: column.fields.table_id
    confidence: high
    canonical_cognee_edge: true
    logistics_only: true
    canonical_edge_type: HAS_COLUMN
    inverse_edge_type: BELONGS_TO_TABLE
    materialize_inverse: true
    edge_class: canonical
    source_type: table
    target_type: column
```
```yaml
candidate_edge:
  edge_id: edge.column.zs_observe.shiprocket_invoice.destination_zipcode.belongs_to_table.table.zs_observe.shiprocket_invoice
  edge_type: BELONGS_TO_TABLE
  source: column.zs_observe.shiprocket_invoice.destination_zipcode
  target: table.zs_observe.shiprocket_invoice
  fields:
    edge_family: data_understanding
    evidence_basis: materialized inverse of HAS_COLUMN
    confidence: high
    canonical_cognee_edge: true
    logistics_only: true
    canonical_edge_type: BELONGS_TO_TABLE
    inverse_edge_type: HAS_COLUMN
    materialize_inverse: true
    edge_class: canonical
    source_type: column
    target_type: table
    materialized_from: edge.table.zs_observe.shiprocket_invoice.has_column.column.zs_observe.shiprocket_invoice.destination_zipcode
```
```yaml
candidate_edge:
  edge_id: edge.table.zs_observe.shiprocket_invoice.has_column.column.zs_observe.shiprocket_invoice.is_active
  edge_type: HAS_COLUMN
  source: table.zs_observe.shiprocket_invoice
  target: column.zs_observe.shiprocket_invoice.is_active
  fields:
    edge_family: data_understanding
    evidence_basis: column.fields.table_id
    confidence: high
    canonical_cognee_edge: true
    logistics_only: true
    canonical_edge_type: HAS_COLUMN
    inverse_edge_type: BELONGS_TO_TABLE
    materialize_inverse: true
    edge_class: canonical
    source_type: table
    target_type: column
```
```yaml
candidate_edge:
  edge_id: edge.column.zs_observe.shiprocket_invoice.is_active.belongs_to_table.table.zs_observe.shiprocket_invoice
  edge_type: BELONGS_TO_TABLE
  source: column.zs_observe.shiprocket_invoice.is_active
  target: table.zs_observe.shiprocket_invoice
  fields:
    edge_family: data_understanding
    evidence_basis: materialized inverse of HAS_COLUMN
    confidence: high
    canonical_cognee_edge: true
    logistics_only: true
    canonical_edge_type: BELONGS_TO_TABLE
    inverse_edge_type: HAS_COLUMN
    materialize_inverse: true
    edge_class: canonical
    source_type: column
    target_type: table
    materialized_from: edge.table.zs_observe.shiprocket_invoice.has_column.column.zs_observe.shiprocket_invoice.is_active
```
```yaml
candidate_edge:
  edge_id: edge.table.zs_observe.shiprocket_invoice.has_column.column.zs_observe.shiprocket_invoice.group_level_id
  edge_type: HAS_COLUMN
  source: table.zs_observe.shiprocket_invoice
  target: column.zs_observe.shiprocket_invoice.group_level_id
  fields:
    edge_family: data_understanding
    evidence_basis: column.fields.table_id
    confidence: high
    canonical_cognee_edge: true
    logistics_only: true
    canonical_edge_type: HAS_COLUMN
    inverse_edge_type: BELONGS_TO_TABLE
    materialize_inverse: true
    edge_class: canonical
    source_type: table
    target_type: column
```
```yaml
candidate_edge:
  edge_id: edge.column.zs_observe.shiprocket_invoice.group_level_id.belongs_to_table.table.zs_observe.shiprocket_invoice
  edge_type: BELONGS_TO_TABLE
  source: column.zs_observe.shiprocket_invoice.group_level_id
  target: table.zs_observe.shiprocket_invoice
  fields:
    edge_family: data_understanding
    evidence_basis: materialized inverse of HAS_COLUMN
    confidence: high
    canonical_cognee_edge: true
    logistics_only: true
    canonical_edge_type: BELONGS_TO_TABLE
    inverse_edge_type: HAS_COLUMN
    materialize_inverse: true
    edge_class: canonical
    source_type: column
    target_type: table
    materialized_from: edge.table.zs_observe.shiprocket_invoice.has_column.column.zs_observe.shiprocket_invoice.group_level_id
```
```yaml
candidate_edge:
  edge_id: edge.table.zs_observe.shiprocket_settlement.sourced_from_platform.platform.shiprocket
  edge_type: SOURCED_FROM_PLATFORM
  source: table.zs_observe.shiprocket_settlement
  target: platform.shiprocket
  fields:
    edge_family: platform_context
    evidence_basis: table.fields.source_platform_ids
    confidence: high
    canonical_cognee_edge: true
    logistics_only: true
    canonical_edge_type: SOURCED_FROM_PLATFORM
    inverse_edge_type: HAS_SOURCE_TABLE
    materialize_inverse: false
    edge_class: canonical
    source_type: table
    target_type: platform
```
```yaml
candidate_edge:
  edge_id: edge.table.zs_observe.shiprocket_settlement.applies_to_platform.platform.shiprocket
  edge_type: APPLIES_TO_PLATFORM
  source: table.zs_observe.shiprocket_settlement
  target: platform.shiprocket
  fields:
    edge_family: applicability
    evidence_basis: table.fields.structural_applicability
    confidence: high
    canonical_cognee_edge: true
    logistics_only: true
    canonical_edge_type: APPLIES_TO_PLATFORM
    inverse_edge_type: HAS_APPLICABLE_CARD
    materialize_inverse: false
    edge_class: canonical
    source_type: table
    target_type: platform
```
```yaml
candidate_edge:
  edge_id: edge.table.zs_observe.shiprocket_settlement.has_column.column.zs_observe.shiprocket_settlement.order_id
  edge_type: HAS_COLUMN
  source: table.zs_observe.shiprocket_settlement
  target: column.zs_observe.shiprocket_settlement.order_id
  fields:
    edge_family: data_understanding
    evidence_basis: column.fields.table_id
    confidence: high
    canonical_cognee_edge: true
    logistics_only: true
    canonical_edge_type: HAS_COLUMN
    inverse_edge_type: BELONGS_TO_TABLE
    materialize_inverse: true
    edge_class: canonical
    source_type: table
    target_type: column
```
```yaml
candidate_edge:
  edge_id: edge.column.zs_observe.shiprocket_settlement.order_id.belongs_to_table.table.zs_observe.shiprocket_settlement
  edge_type: BELONGS_TO_TABLE
  source: column.zs_observe.shiprocket_settlement.order_id
  target: table.zs_observe.shiprocket_settlement
  fields:
    edge_family: data_understanding
    evidence_basis: materialized inverse of HAS_COLUMN
    confidence: high
    canonical_cognee_edge: true
    logistics_only: true
    canonical_edge_type: BELONGS_TO_TABLE
    inverse_edge_type: HAS_COLUMN
    materialize_inverse: true
    edge_class: canonical
    source_type: column
    target_type: table
    materialized_from: edge.table.zs_observe.shiprocket_settlement.has_column.column.zs_observe.shiprocket_settlement.order_id
```
```yaml
candidate_edge:
  edge_id: edge.table.zs_observe.shiprocket_settlement.has_column.column.zs_observe.shiprocket_settlement.awb_number
  edge_type: HAS_COLUMN
  source: table.zs_observe.shiprocket_settlement
  target: column.zs_observe.shiprocket_settlement.awb_number
  fields:
    edge_family: data_understanding
    evidence_basis: column.fields.table_id
    confidence: high
    canonical_cognee_edge: true
    logistics_only: true
    canonical_edge_type: HAS_COLUMN
    inverse_edge_type: BELONGS_TO_TABLE
    materialize_inverse: true
    edge_class: canonical
    source_type: table
    target_type: column
```
```yaml
candidate_edge:
  edge_id: edge.column.zs_observe.shiprocket_settlement.awb_number.belongs_to_table.table.zs_observe.shiprocket_settlement
  edge_type: BELONGS_TO_TABLE
  source: column.zs_observe.shiprocket_settlement.awb_number
  target: table.zs_observe.shiprocket_settlement
  fields:
    edge_family: data_understanding
    evidence_basis: materialized inverse of HAS_COLUMN
    confidence: high
    canonical_cognee_edge: true
    logistics_only: true
    canonical_edge_type: BELONGS_TO_TABLE
    inverse_edge_type: HAS_COLUMN
    materialize_inverse: true
    edge_class: canonical
    source_type: column
    target_type: table
    materialized_from: edge.table.zs_observe.shiprocket_settlement.has_column.column.zs_observe.shiprocket_settlement.awb_number
```
```yaml
candidate_edge:
  edge_id: edge.table.zs_observe.shiprocket_settlement.has_column.column.zs_observe.shiprocket_settlement.courier_partner
  edge_type: HAS_COLUMN
  source: table.zs_observe.shiprocket_settlement
  target: column.zs_observe.shiprocket_settlement.courier_partner
  fields:
    edge_family: data_understanding
    evidence_basis: column.fields.table_id
    confidence: high
    canonical_cognee_edge: true
    logistics_only: true
    canonical_edge_type: HAS_COLUMN
    inverse_edge_type: BELONGS_TO_TABLE
    materialize_inverse: true
    edge_class: canonical
    source_type: table
    target_type: column
```
```yaml
candidate_edge:
  edge_id: edge.column.zs_observe.shiprocket_settlement.courier_partner.belongs_to_table.table.zs_observe.shiprocket_settlement
  edge_type: BELONGS_TO_TABLE
  source: column.zs_observe.shiprocket_settlement.courier_partner
  target: table.zs_observe.shiprocket_settlement
  fields:
    edge_family: data_understanding
    evidence_basis: materialized inverse of HAS_COLUMN
    confidence: high
    canonical_cognee_edge: true
    logistics_only: true
    canonical_edge_type: BELONGS_TO_TABLE
    inverse_edge_type: HAS_COLUMN
    materialize_inverse: true
    edge_class: canonical
    source_type: column
    target_type: table
    materialized_from: edge.table.zs_observe.shiprocket_settlement.has_column.column.zs_observe.shiprocket_settlement.courier_partner
```
```yaml
candidate_edge:
  edge_id: edge.table.zs_observe.shiprocket_settlement.has_column.column.zs_observe.shiprocket_settlement.charged_amount
  edge_type: HAS_COLUMN
  source: table.zs_observe.shiprocket_settlement
  target: column.zs_observe.shiprocket_settlement.charged_amount
  fields:
    edge_family: data_understanding
    evidence_basis: column.fields.table_id
    confidence: high
    canonical_cognee_edge: true
    logistics_only: true
    canonical_edge_type: HAS_COLUMN
    inverse_edge_type: BELONGS_TO_TABLE
    materialize_inverse: true
    edge_class: canonical
    source_type: table
    target_type: column
```
```yaml
candidate_edge:
  edge_id: edge.column.zs_observe.shiprocket_settlement.charged_amount.belongs_to_table.table.zs_observe.shiprocket_settlement
  edge_type: BELONGS_TO_TABLE
  source: column.zs_observe.shiprocket_settlement.charged_amount
  target: table.zs_observe.shiprocket_settlement
  fields:
    edge_family: data_understanding
    evidence_basis: materialized inverse of HAS_COLUMN
    confidence: high
    canonical_cognee_edge: true
    logistics_only: true
    canonical_edge_type: BELONGS_TO_TABLE
    inverse_edge_type: HAS_COLUMN
    materialize_inverse: true
    edge_class: canonical
    source_type: column
    target_type: table
    materialized_from: edge.table.zs_observe.shiprocket_settlement.has_column.column.zs_observe.shiprocket_settlement.charged_amount
```
```yaml
candidate_edge:
  edge_id: edge.table.zs_observe.shiprocket_settlement.has_column.column.zs_observe.shiprocket_settlement.delivered_date
  edge_type: HAS_COLUMN
  source: table.zs_observe.shiprocket_settlement
  target: column.zs_observe.shiprocket_settlement.delivered_date
  fields:
    edge_family: data_understanding
    evidence_basis: column.fields.table_id
    confidence: high
    canonical_cognee_edge: true
    logistics_only: true
    canonical_edge_type: HAS_COLUMN
    inverse_edge_type: BELONGS_TO_TABLE
    materialize_inverse: true
    edge_class: canonical
    source_type: table
    target_type: column
```
```yaml
candidate_edge:
  edge_id: edge.column.zs_observe.shiprocket_settlement.delivered_date.belongs_to_table.table.zs_observe.shiprocket_settlement
  edge_type: BELONGS_TO_TABLE
  source: column.zs_observe.shiprocket_settlement.delivered_date
  target: table.zs_observe.shiprocket_settlement
  fields:
    edge_family: data_understanding
    evidence_basis: materialized inverse of HAS_COLUMN
    confidence: high
    canonical_cognee_edge: true
    logistics_only: true
    canonical_edge_type: BELONGS_TO_TABLE
    inverse_edge_type: HAS_COLUMN
    materialize_inverse: true
    edge_class: canonical
    source_type: column
    target_type: table
    materialized_from: edge.table.zs_observe.shiprocket_settlement.has_column.column.zs_observe.shiprocket_settlement.delivered_date
```
```yaml
candidate_edge:
  edge_id: edge.table.zs_observe.shiprocket_settlement.has_column.column.zs_observe.shiprocket_settlement.settlement_date
  edge_type: HAS_COLUMN
  source: table.zs_observe.shiprocket_settlement
  target: column.zs_observe.shiprocket_settlement.settlement_date
  fields:
    edge_family: data_understanding
    evidence_basis: column.fields.table_id
    confidence: high
    canonical_cognee_edge: true
    logistics_only: true
    canonical_edge_type: HAS_COLUMN
    inverse_edge_type: BELONGS_TO_TABLE
    materialize_inverse: true
    edge_class: canonical
    source_type: table
    target_type: column
```
```yaml
candidate_edge:
  edge_id: edge.column.zs_observe.shiprocket_settlement.settlement_date.belongs_to_table.table.zs_observe.shiprocket_settlement
  edge_type: BELONGS_TO_TABLE
  source: column.zs_observe.shiprocket_settlement.settlement_date
  target: table.zs_observe.shiprocket_settlement
  fields:
    edge_family: data_understanding
    evidence_basis: materialized inverse of HAS_COLUMN
    confidence: high
    canonical_cognee_edge: true
    logistics_only: true
    canonical_edge_type: BELONGS_TO_TABLE
    inverse_edge_type: HAS_COLUMN
    materialize_inverse: true
    edge_class: canonical
    source_type: column
    target_type: table
    materialized_from: edge.table.zs_observe.shiprocket_settlement.has_column.column.zs_observe.shiprocket_settlement.settlement_date
```
```yaml
candidate_edge:
  edge_id: edge.table.zs_observe.shiprocket_settlement.has_column.column.zs_observe.shiprocket_settlement.is_active
  edge_type: HAS_COLUMN
  source: table.zs_observe.shiprocket_settlement
  target: column.zs_observe.shiprocket_settlement.is_active
  fields:
    edge_family: data_understanding
    evidence_basis: column.fields.table_id
    confidence: high
    canonical_cognee_edge: true
    logistics_only: true
    canonical_edge_type: HAS_COLUMN
    inverse_edge_type: BELONGS_TO_TABLE
    materialize_inverse: true
    edge_class: canonical
    source_type: table
    target_type: column
```
```yaml
candidate_edge:
  edge_id: edge.column.zs_observe.shiprocket_settlement.is_active.belongs_to_table.table.zs_observe.shiprocket_settlement
  edge_type: BELONGS_TO_TABLE
  source: column.zs_observe.shiprocket_settlement.is_active
  target: table.zs_observe.shiprocket_settlement
  fields:
    edge_family: data_understanding
    evidence_basis: materialized inverse of HAS_COLUMN
    confidence: high
    canonical_cognee_edge: true
    logistics_only: true
    canonical_edge_type: BELONGS_TO_TABLE
    inverse_edge_type: HAS_COLUMN
    materialize_inverse: true
    edge_class: canonical
    source_type: column
    target_type: table
    materialized_from: edge.table.zs_observe.shiprocket_settlement.has_column.column.zs_observe.shiprocket_settlement.is_active
```
```yaml
candidate_edge:
  edge_id: edge.table.zs_observe.shiprocket_settlement.has_column.column.zs_observe.shiprocket_settlement.group_level_id
  edge_type: HAS_COLUMN
  source: table.zs_observe.shiprocket_settlement
  target: column.zs_observe.shiprocket_settlement.group_level_id
  fields:
    edge_family: data_understanding
    evidence_basis: column.fields.table_id
    confidence: high
    canonical_cognee_edge: true
    logistics_only: true
    canonical_edge_type: HAS_COLUMN
    inverse_edge_type: BELONGS_TO_TABLE
    materialize_inverse: true
    edge_class: canonical
    source_type: table
    target_type: column
```
```yaml
candidate_edge:
  edge_id: edge.column.zs_observe.shiprocket_settlement.group_level_id.belongs_to_table.table.zs_observe.shiprocket_settlement
  edge_type: BELONGS_TO_TABLE
  source: column.zs_observe.shiprocket_settlement.group_level_id
  target: table.zs_observe.shiprocket_settlement
  fields:
    edge_family: data_understanding
    evidence_basis: materialized inverse of HAS_COLUMN
    confidence: high
    canonical_cognee_edge: true
    logistics_only: true
    canonical_edge_type: BELONGS_TO_TABLE
    inverse_edge_type: HAS_COLUMN
    materialize_inverse: true
    edge_class: canonical
    source_type: column
    target_type: table
    materialized_from: edge.table.zs_observe.shiprocket_settlement.has_column.column.zs_observe.shiprocket_settlement.group_level_id
```
```yaml
candidate_edge:
  edge_id: edge.table.zs_observe.shiprocket_settlement_report.sourced_from_platform.platform.shiprocket
  edge_type: SOURCED_FROM_PLATFORM
  source: table.zs_observe.shiprocket_settlement_report
  target: platform.shiprocket
  fields:
    edge_family: platform_context
    evidence_basis: table.fields.source_platform_ids
    confidence: high
    canonical_cognee_edge: true
    logistics_only: true
    canonical_edge_type: SOURCED_FROM_PLATFORM
    inverse_edge_type: HAS_SOURCE_TABLE
    materialize_inverse: false
    edge_class: canonical
    source_type: table
    target_type: platform
```
```yaml
candidate_edge:
  edge_id: edge.table.zs_observe.shiprocket_settlement_report.applies_to_platform.platform.shiprocket
  edge_type: APPLIES_TO_PLATFORM
  source: table.zs_observe.shiprocket_settlement_report
  target: platform.shiprocket
  fields:
    edge_family: applicability
    evidence_basis: table.fields.structural_applicability
    confidence: high
    canonical_cognee_edge: true
    logistics_only: true
    canonical_edge_type: APPLIES_TO_PLATFORM
    inverse_edge_type: HAS_APPLICABLE_CARD
    materialize_inverse: false
    edge_class: canonical
    source_type: table
    target_type: platform
```
```yaml
candidate_edge:
  edge_id: edge.table.zs_observe.shiprocket_settlement_report.has_column.column.zs_observe.shiprocket_settlement_report.order_id
  edge_type: HAS_COLUMN
  source: table.zs_observe.shiprocket_settlement_report
  target: column.zs_observe.shiprocket_settlement_report.order_id
  fields:
    edge_family: data_understanding
    evidence_basis: column.fields.table_id
    confidence: high
    canonical_cognee_edge: true
    logistics_only: true
    canonical_edge_type: HAS_COLUMN
    inverse_edge_type: BELONGS_TO_TABLE
    materialize_inverse: true
    edge_class: canonical
    source_type: table
    target_type: column
```
```yaml
candidate_edge:
  edge_id: edge.column.zs_observe.shiprocket_settlement_report.order_id.belongs_to_table.table.zs_observe.shiprocket_settlement_report
  edge_type: BELONGS_TO_TABLE
  source: column.zs_observe.shiprocket_settlement_report.order_id
  target: table.zs_observe.shiprocket_settlement_report
  fields:
    edge_family: data_understanding
    evidence_basis: materialized inverse of HAS_COLUMN
    confidence: high
    canonical_cognee_edge: true
    logistics_only: true
    canonical_edge_type: BELONGS_TO_TABLE
    inverse_edge_type: HAS_COLUMN
    materialize_inverse: true
    edge_class: canonical
    source_type: column
    target_type: table
    materialized_from: edge.table.zs_observe.shiprocket_settlement_report.has_column.column.zs_observe.shiprocket_settlement_report.order_id
```
```yaml
candidate_edge:
  edge_id: edge.table.zs_observe.shiprocket_settlement_report.has_column.column.zs_observe.shiprocket_settlement_report.courier_partner
  edge_type: HAS_COLUMN
  source: table.zs_observe.shiprocket_settlement_report
  target: column.zs_observe.shiprocket_settlement_report.courier_partner
  fields:
    edge_family: data_understanding
    evidence_basis: column.fields.table_id
    confidence: high
    canonical_cognee_edge: true
    logistics_only: true
    canonical_edge_type: HAS_COLUMN
    inverse_edge_type: BELONGS_TO_TABLE
    materialize_inverse: true
    edge_class: canonical
    source_type: table
    target_type: column
```
```yaml
candidate_edge:
  edge_id: edge.column.zs_observe.shiprocket_settlement_report.courier_partner.belongs_to_table.table.zs_observe.shiprocket_settlement_report
  edge_type: BELONGS_TO_TABLE
  source: column.zs_observe.shiprocket_settlement_report.courier_partner
  target: table.zs_observe.shiprocket_settlement_report
  fields:
    edge_family: data_understanding
    evidence_basis: materialized inverse of HAS_COLUMN
    confidence: high
    canonical_cognee_edge: true
    logistics_only: true
    canonical_edge_type: BELONGS_TO_TABLE
    inverse_edge_type: HAS_COLUMN
    materialize_inverse: true
    edge_class: canonical
    source_type: column
    target_type: table
    materialized_from: edge.table.zs_observe.shiprocket_settlement_report.has_column.column.zs_observe.shiprocket_settlement_report.courier_partner
```
```yaml
candidate_edge:
  edge_id: edge.table.zs_observe.shiprocket_settlement_report.has_column.column.zs_observe.shiprocket_settlement_report.awb_remittance_status
  edge_type: HAS_COLUMN
  source: table.zs_observe.shiprocket_settlement_report
  target: column.zs_observe.shiprocket_settlement_report.awb_remittance_status
  fields:
    edge_family: data_understanding
    evidence_basis: column.fields.table_id
    confidence: high
    canonical_cognee_edge: true
    logistics_only: true
    canonical_edge_type: HAS_COLUMN
    inverse_edge_type: BELONGS_TO_TABLE
    materialize_inverse: true
    edge_class: canonical
    source_type: table
    target_type: column
```
```yaml
candidate_edge:
  edge_id: edge.column.zs_observe.shiprocket_settlement_report.awb_remittance_status.belongs_to_table.table.zs_observe.shiprocket_settlement_report
  edge_type: BELONGS_TO_TABLE
  source: column.zs_observe.shiprocket_settlement_report.awb_remittance_status
  target: table.zs_observe.shiprocket_settlement_report
  fields:
    edge_family: data_understanding
    evidence_basis: materialized inverse of HAS_COLUMN
    confidence: high
    canonical_cognee_edge: true
    logistics_only: true
    canonical_edge_type: BELONGS_TO_TABLE
    inverse_edge_type: HAS_COLUMN
    materialize_inverse: true
    edge_class: canonical
    source_type: column
    target_type: table
    materialized_from: edge.table.zs_observe.shiprocket_settlement_report.has_column.column.zs_observe.shiprocket_settlement_report.awb_remittance_status
```
```yaml
candidate_edge:
  edge_id: edge.table.zs_observe.shiprocket_settlement_report.has_column.column.zs_observe.shiprocket_settlement_report.courier_received_amount
  edge_type: HAS_COLUMN
  source: table.zs_observe.shiprocket_settlement_report
  target: column.zs_observe.shiprocket_settlement_report.courier_received_amount
  fields:
    edge_family: data_understanding
    evidence_basis: column.fields.table_id
    confidence: high
    canonical_cognee_edge: true
    logistics_only: true
    canonical_edge_type: HAS_COLUMN
    inverse_edge_type: BELONGS_TO_TABLE
    materialize_inverse: true
    edge_class: canonical
    source_type: table
    target_type: column
```
```yaml
candidate_edge:
  edge_id: edge.column.zs_observe.shiprocket_settlement_report.courier_received_amount.belongs_to_table.table.zs_observe.shiprocket_settlement_report
  edge_type: BELONGS_TO_TABLE
  source: column.zs_observe.shiprocket_settlement_report.courier_received_amount
  target: table.zs_observe.shiprocket_settlement_report
  fields:
    edge_family: data_understanding
    evidence_basis: materialized inverse of HAS_COLUMN
    confidence: high
    canonical_cognee_edge: true
    logistics_only: true
    canonical_edge_type: BELONGS_TO_TABLE
    inverse_edge_type: HAS_COLUMN
    materialize_inverse: true
    edge_class: canonical
    source_type: column
    target_type: table
    materialized_from: edge.table.zs_observe.shiprocket_settlement_report.has_column.column.zs_observe.shiprocket_settlement_report.courier_received_amount
```
```yaml
candidate_edge:
  edge_id: edge.table.zs_observe.shiprocket_settlement_report.has_column.column.zs_observe.shiprocket_settlement_report.settlement_id
  edge_type: HAS_COLUMN
  source: table.zs_observe.shiprocket_settlement_report
  target: column.zs_observe.shiprocket_settlement_report.settlement_id
  fields:
    edge_family: data_understanding
    evidence_basis: column.fields.table_id
    confidence: high
    canonical_cognee_edge: true
    logistics_only: true
    canonical_edge_type: HAS_COLUMN
    inverse_edge_type: BELONGS_TO_TABLE
    materialize_inverse: true
    edge_class: canonical
    source_type: table
    target_type: column
```
```yaml
candidate_edge:
  edge_id: edge.column.zs_observe.shiprocket_settlement_report.settlement_id.belongs_to_table.table.zs_observe.shiprocket_settlement_report
  edge_type: BELONGS_TO_TABLE
  source: column.zs_observe.shiprocket_settlement_report.settlement_id
  target: table.zs_observe.shiprocket_settlement_report
  fields:
    edge_family: data_understanding
    evidence_basis: materialized inverse of HAS_COLUMN
    confidence: high
    canonical_cognee_edge: true
    logistics_only: true
    canonical_edge_type: BELONGS_TO_TABLE
    inverse_edge_type: HAS_COLUMN
    materialize_inverse: true
    edge_class: canonical
    source_type: column
    target_type: table
    materialized_from: edge.table.zs_observe.shiprocket_settlement_report.has_column.column.zs_observe.shiprocket_settlement_report.settlement_id
```
```yaml
candidate_edge:
  edge_id: edge.table.zs_observe.shiprocket_settlement_report.has_column.column.zs_observe.shiprocket_settlement_report.source_gst_name
  edge_type: HAS_COLUMN
  source: table.zs_observe.shiprocket_settlement_report
  target: column.zs_observe.shiprocket_settlement_report.source_gst_name
  fields:
    edge_family: data_understanding
    evidence_basis: column.fields.table_id
    confidence: high
    canonical_cognee_edge: true
    logistics_only: true
    canonical_edge_type: HAS_COLUMN
    inverse_edge_type: BELONGS_TO_TABLE
    materialize_inverse: true
    edge_class: canonical
    source_type: table
    target_type: column
```
```yaml
candidate_edge:
  edge_id: edge.column.zs_observe.shiprocket_settlement_report.source_gst_name.belongs_to_table.table.zs_observe.shiprocket_settlement_report
  edge_type: BELONGS_TO_TABLE
  source: column.zs_observe.shiprocket_settlement_report.source_gst_name
  target: table.zs_observe.shiprocket_settlement_report
  fields:
    edge_family: data_understanding
    evidence_basis: materialized inverse of HAS_COLUMN
    confidence: high
    canonical_cognee_edge: true
    logistics_only: true
    canonical_edge_type: BELONGS_TO_TABLE
    inverse_edge_type: HAS_COLUMN
    materialize_inverse: true
    edge_class: canonical
    source_type: column
    target_type: table
    materialized_from: edge.table.zs_observe.shiprocket_settlement_report.has_column.column.zs_observe.shiprocket_settlement_report.source_gst_name
```
```yaml
candidate_edge:
  edge_id: edge.table.zs_observe.shiprocket_settlement_report.has_column.column.zs_observe.shiprocket_settlement_report.source_gst_id
  edge_type: HAS_COLUMN
  source: table.zs_observe.shiprocket_settlement_report
  target: column.zs_observe.shiprocket_settlement_report.source_gst_id
  fields:
    edge_family: data_understanding
    evidence_basis: column.fields.table_id
    confidence: high
    canonical_cognee_edge: true
    logistics_only: true
    canonical_edge_type: HAS_COLUMN
    inverse_edge_type: BELONGS_TO_TABLE
    materialize_inverse: true
    edge_class: canonical
    source_type: table
    target_type: column
```
```yaml
candidate_edge:
  edge_id: edge.column.zs_observe.shiprocket_settlement_report.source_gst_id.belongs_to_table.table.zs_observe.shiprocket_settlement_report
  edge_type: BELONGS_TO_TABLE
  source: column.zs_observe.shiprocket_settlement_report.source_gst_id
  target: table.zs_observe.shiprocket_settlement_report
  fields:
    edge_family: data_understanding
    evidence_basis: materialized inverse of HAS_COLUMN
    confidence: high
    canonical_cognee_edge: true
    logistics_only: true
    canonical_edge_type: BELONGS_TO_TABLE
    inverse_edge_type: HAS_COLUMN
    materialize_inverse: true
    edge_class: canonical
    source_type: column
    target_type: table
    materialized_from: edge.table.zs_observe.shiprocket_settlement_report.has_column.column.zs_observe.shiprocket_settlement_report.source_gst_id
```
```yaml
candidate_edge:
  edge_id: edge.table.zs_observe.shiprocket_settlement_report.has_column.column.zs_observe.shiprocket_settlement_report.offer_adjustment_settled_amount
  edge_type: HAS_COLUMN
  source: table.zs_observe.shiprocket_settlement_report
  target: column.zs_observe.shiprocket_settlement_report.offer_adjustment_settled_amount
  fields:
    edge_family: data_understanding
    evidence_basis: column.fields.table_id
    confidence: high
    canonical_cognee_edge: true
    logistics_only: true
    canonical_edge_type: HAS_COLUMN
    inverse_edge_type: BELONGS_TO_TABLE
    materialize_inverse: true
    edge_class: canonical
    source_type: table
    target_type: column
```
```yaml
candidate_edge:
  edge_id: edge.column.zs_observe.shiprocket_settlement_report.offer_adjustment_settled_amount.belongs_to_table.table.zs_observe.shiprocket_settlement_report
  edge_type: BELONGS_TO_TABLE
  source: column.zs_observe.shiprocket_settlement_report.offer_adjustment_settled_amount
  target: table.zs_observe.shiprocket_settlement_report
  fields:
    edge_family: data_understanding
    evidence_basis: materialized inverse of HAS_COLUMN
    confidence: high
    canonical_cognee_edge: true
    logistics_only: true
    canonical_edge_type: BELONGS_TO_TABLE
    inverse_edge_type: HAS_COLUMN
    materialize_inverse: true
    edge_class: canonical
    source_type: column
    target_type: table
    materialized_from: edge.table.zs_observe.shiprocket_settlement_report.has_column.column.zs_observe.shiprocket_settlement_report.offer_adjustment_settled_amount
```
```yaml
candidate_edge:
  edge_id: edge.table.zs_observe.shiprocket_settlement_report.has_column.column.zs_observe.shiprocket_settlement_report.parent_id
  edge_type: HAS_COLUMN
  source: table.zs_observe.shiprocket_settlement_report
  target: column.zs_observe.shiprocket_settlement_report.parent_id
  fields:
    edge_family: data_understanding
    evidence_basis: column.fields.table_id
    confidence: high
    canonical_cognee_edge: true
    logistics_only: true
    canonical_edge_type: HAS_COLUMN
    inverse_edge_type: BELONGS_TO_TABLE
    materialize_inverse: true
    edge_class: canonical
    source_type: table
    target_type: column
```
```yaml
candidate_edge:
  edge_id: edge.column.zs_observe.shiprocket_settlement_report.parent_id.belongs_to_table.table.zs_observe.shiprocket_settlement_report
  edge_type: BELONGS_TO_TABLE
  source: column.zs_observe.shiprocket_settlement_report.parent_id
  target: table.zs_observe.shiprocket_settlement_report
  fields:
    edge_family: data_understanding
    evidence_basis: materialized inverse of HAS_COLUMN
    confidence: high
    canonical_cognee_edge: true
    logistics_only: true
    canonical_edge_type: BELONGS_TO_TABLE
    inverse_edge_type: HAS_COLUMN
    materialize_inverse: true
    edge_class: canonical
    source_type: column
    target_type: table
    materialized_from: edge.table.zs_observe.shiprocket_settlement_report.has_column.column.zs_observe.shiprocket_settlement_report.parent_id
```
```yaml
candidate_edge:
  edge_id: edge.table.zs_observe.shiprocket_oms.has_relationship.relationship.shiprocket_oms.shiprocket_invoice.awb
  edge_type: HAS_RELATIONSHIP
  source: table.zs_observe.shiprocket_oms
  target: relationship.shiprocket_oms.shiprocket_invoice.awb
  fields:
    edge_family: data_understanding
    evidence_basis: relationship.fields.source_table
    confidence: high
    canonical_cognee_edge: true
    logistics_only: true
    canonical_edge_type: HAS_RELATIONSHIP
    inverse_edge_type: RELATIONSHIP_OF_TABLE
    materialize_inverse: false
    edge_class: canonical
    source_type: table
    target_type: relationship
```
```yaml
candidate_edge:
  edge_id: edge.relationship.shiprocket_oms.shiprocket_invoice.awb.source_table.table.zs_observe.shiprocket_oms
  edge_type: SOURCE_TABLE
  source: relationship.shiprocket_oms.shiprocket_invoice.awb
  target: table.zs_observe.shiprocket_oms
  fields:
    edge_family: data_understanding
    evidence_basis: relationship.fields.source_table
    confidence: high
    canonical_cognee_edge: true
    logistics_only: true
    canonical_edge_type: SOURCE_TABLE
    inverse_edge_type: SOURCE_OF_RELATIONSHIP
    materialize_inverse: false
    edge_class: canonical
    source_type: relationship
    target_type: table
```
```yaml
candidate_edge:
  edge_id: edge.table.zs_observe.shiprocket_invoice.has_relationship.relationship.shiprocket_oms.shiprocket_invoice.awb
  edge_type: HAS_RELATIONSHIP
  source: table.zs_observe.shiprocket_invoice
  target: relationship.shiprocket_oms.shiprocket_invoice.awb
  fields:
    edge_family: data_understanding
    evidence_basis: relationship.fields.target_table
    confidence: high
    canonical_cognee_edge: true
    logistics_only: true
    canonical_edge_type: HAS_RELATIONSHIP
    inverse_edge_type: RELATIONSHIP_OF_TABLE
    materialize_inverse: false
    edge_class: canonical
    source_type: table
    target_type: relationship
```
```yaml
candidate_edge:
  edge_id: edge.relationship.shiprocket_oms.shiprocket_invoice.awb.target_table.table.zs_observe.shiprocket_invoice
  edge_type: TARGET_TABLE
  source: relationship.shiprocket_oms.shiprocket_invoice.awb
  target: table.zs_observe.shiprocket_invoice
  fields:
    edge_family: data_understanding
    evidence_basis: relationship.fields.target_table
    confidence: high
    canonical_cognee_edge: true
    logistics_only: true
    canonical_edge_type: TARGET_TABLE
    inverse_edge_type: TARGET_OF_RELATIONSHIP
    materialize_inverse: false
    edge_class: canonical
    source_type: relationship
    target_type: table
```
```yaml
candidate_edge:
  edge_id: edge.relationship.shiprocket_oms.shiprocket_invoice.awb.uses_source_column.column.zs_observe.shiprocket_oms.awb_code
  edge_type: USES_SOURCE_COLUMN
  source: relationship.shiprocket_oms.shiprocket_invoice.awb
  target: column.zs_observe.shiprocket_oms.awb_code
  fields:
    edge_family: data_understanding
    evidence_basis: relationship.fields.join_keys
    confidence: high
    canonical_cognee_edge: true
    logistics_only: true
    canonical_edge_type: USES_SOURCE_COLUMN
    inverse_edge_type: SOURCE_COLUMN_OF_RELATIONSHIP
    materialize_inverse: false
    edge_class: canonical
    source_type: relationship
    target_type: column
```
```yaml
candidate_edge:
  edge_id: edge.relationship.shiprocket_oms.shiprocket_invoice.awb.uses_target_column.column.zs_observe.shiprocket_invoice.other_id
  edge_type: USES_TARGET_COLUMN
  source: relationship.shiprocket_oms.shiprocket_invoice.awb
  target: column.zs_observe.shiprocket_invoice.other_id
  fields:
    edge_family: data_understanding
    evidence_basis: relationship.fields.join_keys
    confidence: high
    canonical_cognee_edge: true
    logistics_only: true
    canonical_edge_type: USES_TARGET_COLUMN
    inverse_edge_type: TARGET_COLUMN_OF_RELATIONSHIP
    materialize_inverse: false
    edge_class: canonical
    source_type: relationship
    target_type: column
```
```yaml
candidate_edge:
  edge_id: edge.table.zs_observe.shiprocket_oms.has_relationship.relationship.shiprocket_oms.shiprocket_settlement.awb
  edge_type: HAS_RELATIONSHIP
  source: table.zs_observe.shiprocket_oms
  target: relationship.shiprocket_oms.shiprocket_settlement.awb
  fields:
    edge_family: data_understanding
    evidence_basis: relationship.fields.source_table
    confidence: high
    canonical_cognee_edge: true
    logistics_only: true
    canonical_edge_type: HAS_RELATIONSHIP
    inverse_edge_type: RELATIONSHIP_OF_TABLE
    materialize_inverse: false
    edge_class: canonical
    source_type: table
    target_type: relationship
```
```yaml
candidate_edge:
  edge_id: edge.relationship.shiprocket_oms.shiprocket_settlement.awb.source_table.table.zs_observe.shiprocket_oms
  edge_type: SOURCE_TABLE
  source: relationship.shiprocket_oms.shiprocket_settlement.awb
  target: table.zs_observe.shiprocket_oms
  fields:
    edge_family: data_understanding
    evidence_basis: relationship.fields.source_table
    confidence: high
    canonical_cognee_edge: true
    logistics_only: true
    canonical_edge_type: SOURCE_TABLE
    inverse_edge_type: SOURCE_OF_RELATIONSHIP
    materialize_inverse: false
    edge_class: canonical
    source_type: relationship
    target_type: table
```
```yaml
candidate_edge:
  edge_id: edge.table.zs_observe.shiprocket_settlement.has_relationship.relationship.shiprocket_oms.shiprocket_settlement.awb
  edge_type: HAS_RELATIONSHIP
  source: table.zs_observe.shiprocket_settlement
  target: relationship.shiprocket_oms.shiprocket_settlement.awb
  fields:
    edge_family: data_understanding
    evidence_basis: relationship.fields.target_table
    confidence: high
    canonical_cognee_edge: true
    logistics_only: true
    canonical_edge_type: HAS_RELATIONSHIP
    inverse_edge_type: RELATIONSHIP_OF_TABLE
    materialize_inverse: false
    edge_class: canonical
    source_type: table
    target_type: relationship
```
```yaml
candidate_edge:
  edge_id: edge.relationship.shiprocket_oms.shiprocket_settlement.awb.target_table.table.zs_observe.shiprocket_settlement
  edge_type: TARGET_TABLE
  source: relationship.shiprocket_oms.shiprocket_settlement.awb
  target: table.zs_observe.shiprocket_settlement
  fields:
    edge_family: data_understanding
    evidence_basis: relationship.fields.target_table
    confidence: high
    canonical_cognee_edge: true
    logistics_only: true
    canonical_edge_type: TARGET_TABLE
    inverse_edge_type: TARGET_OF_RELATIONSHIP
    materialize_inverse: false
    edge_class: canonical
    source_type: relationship
    target_type: table
```
```yaml
candidate_edge:
  edge_id: edge.relationship.shiprocket_oms.shiprocket_settlement.awb.uses_source_column.column.zs_observe.shiprocket_oms.awb_code
  edge_type: USES_SOURCE_COLUMN
  source: relationship.shiprocket_oms.shiprocket_settlement.awb
  target: column.zs_observe.shiprocket_oms.awb_code
  fields:
    edge_family: data_understanding
    evidence_basis: relationship.fields.join_keys
    confidence: high
    canonical_cognee_edge: true
    logistics_only: true
    canonical_edge_type: USES_SOURCE_COLUMN
    inverse_edge_type: SOURCE_COLUMN_OF_RELATIONSHIP
    materialize_inverse: false
    edge_class: canonical
    source_type: relationship
    target_type: column
```
```yaml
candidate_edge:
  edge_id: edge.relationship.shiprocket_oms.shiprocket_settlement.awb.uses_target_column.column.zs_observe.shiprocket_settlement.awb_number
  edge_type: USES_TARGET_COLUMN
  source: relationship.shiprocket_oms.shiprocket_settlement.awb
  target: column.zs_observe.shiprocket_settlement.awb_number
  fields:
    edge_family: data_understanding
    evidence_basis: relationship.fields.join_keys
    confidence: high
    canonical_cognee_edge: true
    logistics_only: true
    canonical_edge_type: USES_TARGET_COLUMN
    inverse_edge_type: TARGET_COLUMN_OF_RELATIONSHIP
    materialize_inverse: false
    edge_class: canonical
    source_type: relationship
    target_type: column
```
```yaml
candidate_edge:
  edge_id: edge.table.zs_observe.shiprocket_invoice.has_relationship.relationship.shiprocket_invoice.shiprocket_settlement.awb
  edge_type: HAS_RELATIONSHIP
  source: table.zs_observe.shiprocket_invoice
  target: relationship.shiprocket_invoice.shiprocket_settlement.awb
  fields:
    edge_family: data_understanding
    evidence_basis: relationship.fields.source_table
    confidence: high
    canonical_cognee_edge: true
    logistics_only: true
    canonical_edge_type: HAS_RELATIONSHIP
    inverse_edge_type: RELATIONSHIP_OF_TABLE
    materialize_inverse: false
    edge_class: canonical
    source_type: table
    target_type: relationship
```
```yaml
candidate_edge:
  edge_id: edge.relationship.shiprocket_invoice.shiprocket_settlement.awb.source_table.table.zs_observe.shiprocket_invoice
  edge_type: SOURCE_TABLE
  source: relationship.shiprocket_invoice.shiprocket_settlement.awb
  target: table.zs_observe.shiprocket_invoice
  fields:
    edge_family: data_understanding
    evidence_basis: relationship.fields.source_table
    confidence: high
    canonical_cognee_edge: true
    logistics_only: true
    canonical_edge_type: SOURCE_TABLE
    inverse_edge_type: SOURCE_OF_RELATIONSHIP
    materialize_inverse: false
    edge_class: canonical
    source_type: relationship
    target_type: table
```
```yaml
candidate_edge:
  edge_id: edge.table.zs_observe.shiprocket_settlement.has_relationship.relationship.shiprocket_invoice.shiprocket_settlement.awb
  edge_type: HAS_RELATIONSHIP
  source: table.zs_observe.shiprocket_settlement
  target: relationship.shiprocket_invoice.shiprocket_settlement.awb
  fields:
    edge_family: data_understanding
    evidence_basis: relationship.fields.target_table
    confidence: high
    canonical_cognee_edge: true
    logistics_only: true
    canonical_edge_type: HAS_RELATIONSHIP
    inverse_edge_type: RELATIONSHIP_OF_TABLE
    materialize_inverse: false
    edge_class: canonical
    source_type: table
    target_type: relationship
```
```yaml
candidate_edge:
  edge_id: edge.relationship.shiprocket_invoice.shiprocket_settlement.awb.target_table.table.zs_observe.shiprocket_settlement
  edge_type: TARGET_TABLE
  source: relationship.shiprocket_invoice.shiprocket_settlement.awb
  target: table.zs_observe.shiprocket_settlement
  fields:
    edge_family: data_understanding
    evidence_basis: relationship.fields.target_table
    confidence: high
    canonical_cognee_edge: true
    logistics_only: true
    canonical_edge_type: TARGET_TABLE
    inverse_edge_type: TARGET_OF_RELATIONSHIP
    materialize_inverse: false
    edge_class: canonical
    source_type: relationship
    target_type: table
```
```yaml
candidate_edge:
  edge_id: edge.relationship.shiprocket_invoice.shiprocket_settlement.awb.uses_source_column.column.zs_observe.shiprocket_invoice.other_id
  edge_type: USES_SOURCE_COLUMN
  source: relationship.shiprocket_invoice.shiprocket_settlement.awb
  target: column.zs_observe.shiprocket_invoice.other_id
  fields:
    edge_family: data_understanding
    evidence_basis: relationship.fields.join_keys
    confidence: high
    canonical_cognee_edge: true
    logistics_only: true
    canonical_edge_type: USES_SOURCE_COLUMN
    inverse_edge_type: SOURCE_COLUMN_OF_RELATIONSHIP
    materialize_inverse: false
    edge_class: canonical
    source_type: relationship
    target_type: column
```
```yaml
candidate_edge:
  edge_id: edge.relationship.shiprocket_invoice.shiprocket_settlement.awb.uses_target_column.column.zs_observe.shiprocket_settlement.awb_number
  edge_type: USES_TARGET_COLUMN
  source: relationship.shiprocket_invoice.shiprocket_settlement.awb
  target: column.zs_observe.shiprocket_settlement.awb_number
  fields:
    edge_family: data_understanding
    evidence_basis: relationship.fields.join_keys
    confidence: high
    canonical_cognee_edge: true
    logistics_only: true
    canonical_edge_type: USES_TARGET_COLUMN
    inverse_edge_type: TARGET_COLUMN_OF_RELATIONSHIP
    materialize_inverse: false
    edge_class: canonical
    source_type: relationship
    target_type: column
```
```yaml
candidate_edge:
  edge_id: edge.table.zs_observe.shiprocket_settlement.has_relationship.relationship.shiprocket_settlement.delhivery_settlement.awb
  edge_type: HAS_RELATIONSHIP
  source: table.zs_observe.shiprocket_settlement
  target: relationship.shiprocket_settlement.delhivery_settlement.awb
  fields:
    edge_family: data_understanding
    evidence_basis: relationship.fields.source_table
    confidence: high
    canonical_cognee_edge: true
    logistics_only: true
    canonical_edge_type: HAS_RELATIONSHIP
    inverse_edge_type: RELATIONSHIP_OF_TABLE
    materialize_inverse: false
    edge_class: canonical
    source_type: table
    target_type: relationship
```
```yaml
candidate_edge:
  edge_id: edge.relationship.shiprocket_settlement.delhivery_settlement.awb.source_table.table.zs_observe.shiprocket_settlement
  edge_type: SOURCE_TABLE
  source: relationship.shiprocket_settlement.delhivery_settlement.awb
  target: table.zs_observe.shiprocket_settlement
  fields:
    edge_family: data_understanding
    evidence_basis: relationship.fields.source_table
    confidence: high
    canonical_cognee_edge: true
    logistics_only: true
    canonical_edge_type: SOURCE_TABLE
    inverse_edge_type: SOURCE_OF_RELATIONSHIP
    materialize_inverse: false
    edge_class: canonical
    source_type: relationship
    target_type: table
```
```yaml
candidate_edge:
  edge_id: edge.table.zs_observe.delhivery_settlement.has_relationship.relationship.shiprocket_settlement.delhivery_settlement.awb
  edge_type: HAS_RELATIONSHIP
  source: table.zs_observe.delhivery_settlement
  target: relationship.shiprocket_settlement.delhivery_settlement.awb
  fields:
    edge_family: data_understanding
    evidence_basis: relationship.fields.target_table
    confidence: high
    canonical_cognee_edge: true
    logistics_only: true
    canonical_edge_type: HAS_RELATIONSHIP
    inverse_edge_type: RELATIONSHIP_OF_TABLE
    materialize_inverse: false
    edge_class: canonical
    source_type: table
    target_type: relationship
```
```yaml
candidate_edge:
  edge_id: edge.relationship.shiprocket_settlement.delhivery_settlement.awb.target_table.table.zs_observe.delhivery_settlement
  edge_type: TARGET_TABLE
  source: relationship.shiprocket_settlement.delhivery_settlement.awb
  target: table.zs_observe.delhivery_settlement
  fields:
    edge_family: data_understanding
    evidence_basis: relationship.fields.target_table
    confidence: high
    canonical_cognee_edge: true
    logistics_only: true
    canonical_edge_type: TARGET_TABLE
    inverse_edge_type: TARGET_OF_RELATIONSHIP
    materialize_inverse: false
    edge_class: canonical
    source_type: relationship
    target_type: table
```
```yaml
candidate_edge:
  edge_id: edge.relationship.shiprocket_settlement.delhivery_settlement.awb.uses_source_column.column.zs_observe.shiprocket_settlement.awb_number
  edge_type: USES_SOURCE_COLUMN
  source: relationship.shiprocket_settlement.delhivery_settlement.awb
  target: column.zs_observe.shiprocket_settlement.awb_number
  fields:
    edge_family: data_understanding
    evidence_basis: relationship.fields.join_keys
    confidence: high
    canonical_cognee_edge: true
    logistics_only: true
    canonical_edge_type: USES_SOURCE_COLUMN
    inverse_edge_type: SOURCE_COLUMN_OF_RELATIONSHIP
    materialize_inverse: false
    edge_class: canonical
    source_type: relationship
    target_type: column
```
```yaml
candidate_edge:
  edge_id: edge.relationship.shiprocket_settlement.delhivery_settlement.awb.uses_target_column.column.zs_observe.delhivery_settlement.waybill_num
  edge_type: USES_TARGET_COLUMN
  source: relationship.shiprocket_settlement.delhivery_settlement.awb
  target: column.zs_observe.delhivery_settlement.waybill_num
  fields:
    edge_family: data_understanding
    evidence_basis: relationship.fields.join_keys
    confidence: high
    canonical_cognee_edge: true
    logistics_only: true
    canonical_edge_type: USES_TARGET_COLUMN
    inverse_edge_type: TARGET_COLUMN_OF_RELATIONSHIP
    materialize_inverse: false
    edge_class: canonical
    source_type: relationship
    target_type: column
```
```yaml
candidate_edge:
  edge_id: edge.table.zs_observe.shiprocket_invoice.has_relationship.relationship.shiprocket_invoice.dtdc_settlement.awb
  edge_type: HAS_RELATIONSHIP
  source: table.zs_observe.shiprocket_invoice
  target: relationship.shiprocket_invoice.dtdc_settlement.awb
  fields:
    edge_family: data_understanding
    evidence_basis: relationship.fields.source_table
    confidence: high
    canonical_cognee_edge: true
    logistics_only: true
    canonical_edge_type: HAS_RELATIONSHIP
    inverse_edge_type: RELATIONSHIP_OF_TABLE
    materialize_inverse: false
    edge_class: canonical
    source_type: table
    target_type: relationship
```
```yaml
candidate_edge:
  edge_id: edge.relationship.shiprocket_invoice.dtdc_settlement.awb.source_table.table.zs_observe.shiprocket_invoice
  edge_type: SOURCE_TABLE
  source: relationship.shiprocket_invoice.dtdc_settlement.awb
  target: table.zs_observe.shiprocket_invoice
  fields:
    edge_family: data_understanding
    evidence_basis: relationship.fields.source_table
    confidence: high
    canonical_cognee_edge: true
    logistics_only: true
    canonical_edge_type: SOURCE_TABLE
    inverse_edge_type: SOURCE_OF_RELATIONSHIP
    materialize_inverse: false
    edge_class: canonical
    source_type: relationship
    target_type: table
```
```yaml
candidate_edge:
  edge_id: edge.table.zs_observe.dtdc_settlement.has_relationship.relationship.shiprocket_invoice.dtdc_settlement.awb
  edge_type: HAS_RELATIONSHIP
  source: table.zs_observe.dtdc_settlement
  target: relationship.shiprocket_invoice.dtdc_settlement.awb
  fields:
    edge_family: data_understanding
    evidence_basis: relationship.fields.target_table
    confidence: high
    canonical_cognee_edge: true
    logistics_only: true
    canonical_edge_type: HAS_RELATIONSHIP
    inverse_edge_type: RELATIONSHIP_OF_TABLE
    materialize_inverse: false
    edge_class: canonical
    source_type: table
    target_type: relationship
```
```yaml
candidate_edge:
  edge_id: edge.relationship.shiprocket_invoice.dtdc_settlement.awb.target_table.table.zs_observe.dtdc_settlement
  edge_type: TARGET_TABLE
  source: relationship.shiprocket_invoice.dtdc_settlement.awb
  target: table.zs_observe.dtdc_settlement
  fields:
    edge_family: data_understanding
    evidence_basis: relationship.fields.target_table
    confidence: high
    canonical_cognee_edge: true
    logistics_only: true
    canonical_edge_type: TARGET_TABLE
    inverse_edge_type: TARGET_OF_RELATIONSHIP
    materialize_inverse: false
    edge_class: canonical
    source_type: relationship
    target_type: table
```
```yaml
candidate_edge:
  edge_id: edge.relationship.shiprocket_invoice.dtdc_settlement.awb.uses_source_column.column.zs_observe.shiprocket_invoice.other_id
  edge_type: USES_SOURCE_COLUMN
  source: relationship.shiprocket_invoice.dtdc_settlement.awb
  target: column.zs_observe.shiprocket_invoice.other_id
  fields:
    edge_family: data_understanding
    evidence_basis: relationship.fields.join_keys
    confidence: high
    canonical_cognee_edge: true
    logistics_only: true
    canonical_edge_type: USES_SOURCE_COLUMN
    inverse_edge_type: SOURCE_COLUMN_OF_RELATIONSHIP
    materialize_inverse: false
    edge_class: canonical
    source_type: relationship
    target_type: column
```
```yaml
candidate_edge:
  edge_id: edge.relationship.shiprocket_invoice.dtdc_settlement.awb.uses_target_column.column.zs_observe.dtdc_settlement.airwaybill_number
  edge_type: USES_TARGET_COLUMN
  source: relationship.shiprocket_invoice.dtdc_settlement.awb
  target: column.zs_observe.dtdc_settlement.airwaybill_number
  fields:
    edge_family: data_understanding
    evidence_basis: relationship.fields.join_keys
    confidence: high
    canonical_cognee_edge: true
    logistics_only: true
    canonical_edge_type: USES_TARGET_COLUMN
    inverse_edge_type: TARGET_COLUMN_OF_RELATIONSHIP
    materialize_inverse: false
    edge_class: canonical
    source_type: relationship
    target_type: column
```
```yaml
candidate_edge:
  edge_id: edge.table.zs_observe.shiprocket_invoice.has_relationship.relationship.shiprocket_invoice.ekart_settlement.awb
  edge_type: HAS_RELATIONSHIP
  source: table.zs_observe.shiprocket_invoice
  target: relationship.shiprocket_invoice.ekart_settlement.awb
  fields:
    edge_family: data_understanding
    evidence_basis: relationship.fields.source_table
    confidence: high
    canonical_cognee_edge: true
    logistics_only: true
    canonical_edge_type: HAS_RELATIONSHIP
    inverse_edge_type: RELATIONSHIP_OF_TABLE
    materialize_inverse: false
    edge_class: canonical
    source_type: table
    target_type: relationship
```
```yaml
candidate_edge:
  edge_id: edge.relationship.shiprocket_invoice.ekart_settlement.awb.source_table.table.zs_observe.shiprocket_invoice
  edge_type: SOURCE_TABLE
  source: relationship.shiprocket_invoice.ekart_settlement.awb
  target: table.zs_observe.shiprocket_invoice
  fields:
    edge_family: data_understanding
    evidence_basis: relationship.fields.source_table
    confidence: high
    canonical_cognee_edge: true
    logistics_only: true
    canonical_edge_type: SOURCE_TABLE
    inverse_edge_type: SOURCE_OF_RELATIONSHIP
    materialize_inverse: false
    edge_class: canonical
    source_type: relationship
    target_type: table
```
```yaml
candidate_edge:
  edge_id: edge.table.zs_observe.ekart_settlement.has_relationship.relationship.shiprocket_invoice.ekart_settlement.awb
  edge_type: HAS_RELATIONSHIP
  source: table.zs_observe.ekart_settlement
  target: relationship.shiprocket_invoice.ekart_settlement.awb
  fields:
    edge_family: data_understanding
    evidence_basis: relationship.fields.target_table
    confidence: high
    canonical_cognee_edge: true
    logistics_only: true
    canonical_edge_type: HAS_RELATIONSHIP
    inverse_edge_type: RELATIONSHIP_OF_TABLE
    materialize_inverse: false
    edge_class: canonical
    source_type: table
    target_type: relationship
```
```yaml
candidate_edge:
  edge_id: edge.relationship.shiprocket_invoice.ekart_settlement.awb.target_table.table.zs_observe.ekart_settlement
  edge_type: TARGET_TABLE
  source: relationship.shiprocket_invoice.ekart_settlement.awb
  target: table.zs_observe.ekart_settlement
  fields:
    edge_family: data_understanding
    evidence_basis: relationship.fields.target_table
    confidence: high
    canonical_cognee_edge: true
    logistics_only: true
    canonical_edge_type: TARGET_TABLE
    inverse_edge_type: TARGET_OF_RELATIONSHIP
    materialize_inverse: false
    edge_class: canonical
    source_type: relationship
    target_type: table
```
```yaml
candidate_edge:
  edge_id: edge.relationship.shiprocket_invoice.ekart_settlement.awb.uses_source_column.column.zs_observe.shiprocket_invoice.other_id
  edge_type: USES_SOURCE_COLUMN
  source: relationship.shiprocket_invoice.ekart_settlement.awb
  target: column.zs_observe.shiprocket_invoice.other_id
  fields:
    edge_family: data_understanding
    evidence_basis: relationship.fields.join_keys
    confidence: high
    canonical_cognee_edge: true
    logistics_only: true
    canonical_edge_type: USES_SOURCE_COLUMN
    inverse_edge_type: SOURCE_COLUMN_OF_RELATIONSHIP
    materialize_inverse: false
    edge_class: canonical
    source_type: relationship
    target_type: column
```
```yaml
candidate_edge:
  edge_id: edge.relationship.shiprocket_invoice.ekart_settlement.awb.uses_target_column.column.zs_observe.ekart_settlement.shipment_id
  edge_type: USES_TARGET_COLUMN
  source: relationship.shiprocket_invoice.ekart_settlement.awb
  target: column.zs_observe.ekart_settlement.shipment_id
  fields:
    edge_family: data_understanding
    evidence_basis: relationship.fields.join_keys
    confidence: high
    canonical_cognee_edge: true
    logistics_only: true
    canonical_edge_type: USES_TARGET_COLUMN
    inverse_edge_type: TARGET_COLUMN_OF_RELATIONSHIP
    materialize_inverse: false
    edge_class: canonical
    source_type: relationship
    target_type: column
```
```yaml
candidate_edge:
  edge_id: edge.table.zs_observe.shiprocket_settlement.has_relationship.relationship.shiprocket_settlement.xpressbees_settlement.awb
  edge_type: HAS_RELATIONSHIP
  source: table.zs_observe.shiprocket_settlement
  target: relationship.shiprocket_settlement.xpressbees_settlement.awb
  fields:
    edge_family: data_understanding
    evidence_basis: relationship.fields.source_table
    confidence: high
    canonical_cognee_edge: true
    logistics_only: true
    canonical_edge_type: HAS_RELATIONSHIP
    inverse_edge_type: RELATIONSHIP_OF_TABLE
    materialize_inverse: false
    edge_class: canonical
    source_type: table
    target_type: relationship
```
```yaml
candidate_edge:
  edge_id: edge.relationship.shiprocket_settlement.xpressbees_settlement.awb.source_table.table.zs_observe.shiprocket_settlement
  edge_type: SOURCE_TABLE
  source: relationship.shiprocket_settlement.xpressbees_settlement.awb
  target: table.zs_observe.shiprocket_settlement
  fields:
    edge_family: data_understanding
    evidence_basis: relationship.fields.source_table
    confidence: high
    canonical_cognee_edge: true
    logistics_only: true
    canonical_edge_type: SOURCE_TABLE
    inverse_edge_type: SOURCE_OF_RELATIONSHIP
    materialize_inverse: false
    edge_class: canonical
    source_type: relationship
    target_type: table
```
```yaml
candidate_edge:
  edge_id: edge.table.zs_observe.xpressbees_settlement.has_relationship.relationship.shiprocket_settlement.xpressbees_settlement.awb
  edge_type: HAS_RELATIONSHIP
  source: table.zs_observe.xpressbees_settlement
  target: relationship.shiprocket_settlement.xpressbees_settlement.awb
  fields:
    edge_family: data_understanding
    evidence_basis: relationship.fields.target_table
    confidence: high
    canonical_cognee_edge: true
    logistics_only: true
    canonical_edge_type: HAS_RELATIONSHIP
    inverse_edge_type: RELATIONSHIP_OF_TABLE
    materialize_inverse: false
    edge_class: canonical
    source_type: table
    target_type: relationship
```
```yaml
candidate_edge:
  edge_id: edge.relationship.shiprocket_settlement.xpressbees_settlement.awb.target_table.table.zs_observe.xpressbees_settlement
  edge_type: TARGET_TABLE
  source: relationship.shiprocket_settlement.xpressbees_settlement.awb
  target: table.zs_observe.xpressbees_settlement
  fields:
    edge_family: data_understanding
    evidence_basis: relationship.fields.target_table
    confidence: high
    canonical_cognee_edge: true
    logistics_only: true
    canonical_edge_type: TARGET_TABLE
    inverse_edge_type: TARGET_OF_RELATIONSHIP
    materialize_inverse: false
    edge_class: canonical
    source_type: relationship
    target_type: table
```
```yaml
candidate_edge:
  edge_id: edge.relationship.shiprocket_settlement.xpressbees_settlement.awb.uses_source_column.column.zs_observe.shiprocket_settlement.awb_number
  edge_type: USES_SOURCE_COLUMN
  source: relationship.shiprocket_settlement.xpressbees_settlement.awb
  target: column.zs_observe.shiprocket_settlement.awb_number
  fields:
    edge_family: data_understanding
    evidence_basis: relationship.fields.join_keys
    confidence: high
    canonical_cognee_edge: true
    logistics_only: true
    canonical_edge_type: USES_SOURCE_COLUMN
    inverse_edge_type: SOURCE_COLUMN_OF_RELATIONSHIP
    materialize_inverse: false
    edge_class: canonical
    source_type: relationship
    target_type: column
```
```yaml
candidate_edge:
  edge_id: edge.relationship.shiprocket_settlement.xpressbees_settlement.awb.uses_target_column.column.zs_observe.xpressbees_settlement.shipping_id
  edge_type: USES_TARGET_COLUMN
  source: relationship.shiprocket_settlement.xpressbees_settlement.awb
  target: column.zs_observe.xpressbees_settlement.shipping_id
  fields:
    edge_family: data_understanding
    evidence_basis: relationship.fields.join_keys
    confidence: high
    canonical_cognee_edge: true
    logistics_only: true
    canonical_edge_type: USES_TARGET_COLUMN
    inverse_edge_type: TARGET_COLUMN_OF_RELATIONSHIP
    materialize_inverse: false
    edge_class: canonical
    source_type: relationship
    target_type: column
```
```yaml
candidate_edge:
  edge_id: edge.table.zs_observe.shiprocket_invoice.has_relationship.relationship.shiprocket_invoice.xpressbees_settlement.awb
  edge_type: HAS_RELATIONSHIP
  source: table.zs_observe.shiprocket_invoice
  target: relationship.shiprocket_invoice.xpressbees_settlement.awb
  fields:
    edge_family: data_understanding
    evidence_basis: relationship.fields.source_table
    confidence: high
    canonical_cognee_edge: true
    logistics_only: true
    canonical_edge_type: HAS_RELATIONSHIP
    inverse_edge_type: RELATIONSHIP_OF_TABLE
    materialize_inverse: false
    edge_class: canonical
    source_type: table
    target_type: relationship
```
```yaml
candidate_edge:
  edge_id: edge.relationship.shiprocket_invoice.xpressbees_settlement.awb.source_table.table.zs_observe.shiprocket_invoice
  edge_type: SOURCE_TABLE
  source: relationship.shiprocket_invoice.xpressbees_settlement.awb
  target: table.zs_observe.shiprocket_invoice
  fields:
    edge_family: data_understanding
    evidence_basis: relationship.fields.source_table
    confidence: high
    canonical_cognee_edge: true
    logistics_only: true
    canonical_edge_type: SOURCE_TABLE
    inverse_edge_type: SOURCE_OF_RELATIONSHIP
    materialize_inverse: false
    edge_class: canonical
    source_type: relationship
    target_type: table
```
```yaml
candidate_edge:
  edge_id: edge.table.zs_observe.xpressbees_settlement.has_relationship.relationship.shiprocket_invoice.xpressbees_settlement.awb
  edge_type: HAS_RELATIONSHIP
  source: table.zs_observe.xpressbees_settlement
  target: relationship.shiprocket_invoice.xpressbees_settlement.awb
  fields:
    edge_family: data_understanding
    evidence_basis: relationship.fields.target_table
    confidence: high
    canonical_cognee_edge: true
    logistics_only: true
    canonical_edge_type: HAS_RELATIONSHIP
    inverse_edge_type: RELATIONSHIP_OF_TABLE
    materialize_inverse: false
    edge_class: canonical
    source_type: table
    target_type: relationship
```
```yaml
candidate_edge:
  edge_id: edge.relationship.shiprocket_invoice.xpressbees_settlement.awb.target_table.table.zs_observe.xpressbees_settlement
  edge_type: TARGET_TABLE
  source: relationship.shiprocket_invoice.xpressbees_settlement.awb
  target: table.zs_observe.xpressbees_settlement
  fields:
    edge_family: data_understanding
    evidence_basis: relationship.fields.target_table
    confidence: high
    canonical_cognee_edge: true
    logistics_only: true
    canonical_edge_type: TARGET_TABLE
    inverse_edge_type: TARGET_OF_RELATIONSHIP
    materialize_inverse: false
    edge_class: canonical
    source_type: relationship
    target_type: table
```
```yaml
candidate_edge:
  edge_id: edge.relationship.shiprocket_invoice.xpressbees_settlement.awb.uses_source_column.column.zs_observe.shiprocket_invoice.other_id
  edge_type: USES_SOURCE_COLUMN
  source: relationship.shiprocket_invoice.xpressbees_settlement.awb
  target: column.zs_observe.shiprocket_invoice.other_id
  fields:
    edge_family: data_understanding
    evidence_basis: relationship.fields.join_keys
    confidence: high
    canonical_cognee_edge: true
    logistics_only: true
    canonical_edge_type: USES_SOURCE_COLUMN
    inverse_edge_type: SOURCE_COLUMN_OF_RELATIONSHIP
    materialize_inverse: false
    edge_class: canonical
    source_type: relationship
    target_type: column
```
```yaml
candidate_edge:
  edge_id: edge.relationship.shiprocket_invoice.xpressbees_settlement.awb.uses_target_column.column.zs_observe.xpressbees_settlement.shipping_id
  edge_type: USES_TARGET_COLUMN
  source: relationship.shiprocket_invoice.xpressbees_settlement.awb
  target: column.zs_observe.xpressbees_settlement.shipping_id
  fields:
    edge_family: data_understanding
    evidence_basis: relationship.fields.join_keys
    confidence: high
    canonical_cognee_edge: true
    logistics_only: true
    canonical_edge_type: USES_TARGET_COLUMN
    inverse_edge_type: TARGET_COLUMN_OF_RELATIONSHIP
    materialize_inverse: false
    edge_class: canonical
    source_type: relationship
    target_type: column
```
```yaml
candidate_edge:
  edge_id: edge.table.zs_observe.shiprocket_invoice.has_value_profile.value_profile.shiprocket_invoice.courier_partner
  edge_type: HAS_VALUE_PROFILE
  source: table.zs_observe.shiprocket_invoice
  target: value_profile.shiprocket_invoice.courier_partner
  fields:
    edge_family: data_understanding
    evidence_basis: value_profile.fields.column_id
    confidence: high
    canonical_cognee_edge: true
    logistics_only: true
    canonical_edge_type: HAS_VALUE_PROFILE
    inverse_edge_type: PROFILES_COLUMN_OR_PROFILES_TABLE
    materialize_inverse: true
    edge_class: canonical
    source_type: table
    target_type: value_profile
```
```yaml
candidate_edge:
  edge_id: edge.value_profile.shiprocket_invoice.courier_partner.profiles_column.column.zs_observe.shiprocket_invoice.courier_partner
  edge_type: PROFILES_COLUMN
  source: value_profile.shiprocket_invoice.courier_partner
  target: column.zs_observe.shiprocket_invoice.courier_partner
  fields:
    edge_family: data_understanding
    evidence_basis: value_profile.fields.column_id
    confidence: high
    canonical_cognee_edge: true
    logistics_only: true
    canonical_edge_type: PROFILES_COLUMN
    inverse_edge_type: HAS_VALUE_PROFILE
    materialize_inverse: true
    edge_class: canonical
    source_type: value_profile
    target_type: column
```
```yaml
candidate_edge:
  edge_id: edge.column.zs_observe.shiprocket_invoice.courier_partner.has_value_profile.value_profile.shiprocket_invoice.courier_partner
  edge_type: HAS_VALUE_PROFILE
  source: column.zs_observe.shiprocket_invoice.courier_partner
  target: value_profile.shiprocket_invoice.courier_partner
  fields:
    edge_family: data_understanding
    evidence_basis: materialized inverse of PROFILES_COLUMN
    confidence: high
    canonical_cognee_edge: true
    logistics_only: true
    canonical_edge_type: HAS_VALUE_PROFILE
    inverse_edge_type: PROFILES_COLUMN
    materialize_inverse: true
    edge_class: canonical
    source_type: column
    target_type: value_profile
    materialized_from: edge.value_profile.shiprocket_invoice.courier_partner.profiles_column.column.zs_observe.shiprocket_invoice.courier_partner
```
```yaml
candidate_edge:
  edge_id: edge.value_profile.shiprocket_invoice.courier_partner.profiles_table.table.zs_observe.shiprocket_invoice
  edge_type: PROFILES_TABLE
  source: value_profile.shiprocket_invoice.courier_partner
  target: table.zs_observe.shiprocket_invoice
  fields:
    edge_family: data_understanding
    evidence_basis: value_profile.fields.table_id
    confidence: high
    canonical_cognee_edge: true
    logistics_only: true
    canonical_edge_type: PROFILES_TABLE
    inverse_edge_type: HAS_VALUE_PROFILE
    materialize_inverse: true
    edge_class: canonical
    source_type: value_profile
    target_type: table
```
```yaml
candidate_edge:
  edge_id: edge.table.zs_observe.shiprocket_invoice.has_value_profile.value_profile.shiprocket_invoice.order_status
  edge_type: HAS_VALUE_PROFILE
  source: table.zs_observe.shiprocket_invoice
  target: value_profile.shiprocket_invoice.order_status
  fields:
    edge_family: data_understanding
    evidence_basis: value_profile.fields.column_id
    confidence: high
    canonical_cognee_edge: true
    logistics_only: true
    canonical_edge_type: HAS_VALUE_PROFILE
    inverse_edge_type: PROFILES_COLUMN_OR_PROFILES_TABLE
    materialize_inverse: true
    edge_class: canonical
    source_type: table
    target_type: value_profile
```
```yaml
candidate_edge:
  edge_id: edge.value_profile.shiprocket_invoice.order_status.profiles_column.column.zs_observe.shiprocket_invoice.order_status
  edge_type: PROFILES_COLUMN
  source: value_profile.shiprocket_invoice.order_status
  target: column.zs_observe.shiprocket_invoice.order_status
  fields:
    edge_family: data_understanding
    evidence_basis: value_profile.fields.column_id
    confidence: high
    canonical_cognee_edge: true
    logistics_only: true
    canonical_edge_type: PROFILES_COLUMN
    inverse_edge_type: HAS_VALUE_PROFILE
    materialize_inverse: true
    edge_class: canonical
    source_type: value_profile
    target_type: column
```
```yaml
candidate_edge:
  edge_id: edge.column.zs_observe.shiprocket_invoice.order_status.has_value_profile.value_profile.shiprocket_invoice.order_status
  edge_type: HAS_VALUE_PROFILE
  source: column.zs_observe.shiprocket_invoice.order_status
  target: value_profile.shiprocket_invoice.order_status
  fields:
    edge_family: data_understanding
    evidence_basis: materialized inverse of PROFILES_COLUMN
    confidence: high
    canonical_cognee_edge: true
    logistics_only: true
    canonical_edge_type: HAS_VALUE_PROFILE
    inverse_edge_type: PROFILES_COLUMN
    materialize_inverse: true
    edge_class: canonical
    source_type: column
    target_type: value_profile
    materialized_from: edge.value_profile.shiprocket_invoice.order_status.profiles_column.column.zs_observe.shiprocket_invoice.order_status
```
```yaml
candidate_edge:
  edge_id: edge.value_profile.shiprocket_invoice.order_status.profiles_table.table.zs_observe.shiprocket_invoice
  edge_type: PROFILES_TABLE
  source: value_profile.shiprocket_invoice.order_status
  target: table.zs_observe.shiprocket_invoice
  fields:
    edge_family: data_understanding
    evidence_basis: value_profile.fields.table_id
    confidence: high
    canonical_cognee_edge: true
    logistics_only: true
    canonical_edge_type: PROFILES_TABLE
    inverse_edge_type: HAS_VALUE_PROFILE
    materialize_inverse: true
    edge_class: canonical
    source_type: value_profile
    target_type: table
```
```yaml
candidate_edge:
  edge_id: edge.table.zs_observe.shiprocket_invoice.has_value_profile.value_profile.shiprocket_invoice.payment_mode
  edge_type: HAS_VALUE_PROFILE
  source: table.zs_observe.shiprocket_invoice
  target: value_profile.shiprocket_invoice.payment_mode
  fields:
    edge_family: data_understanding
    evidence_basis: value_profile.fields.column_id
    confidence: high
    canonical_cognee_edge: true
    logistics_only: true
    canonical_edge_type: HAS_VALUE_PROFILE
    inverse_edge_type: PROFILES_COLUMN_OR_PROFILES_TABLE
    materialize_inverse: true
    edge_class: canonical
    source_type: table
    target_type: value_profile
```
```yaml
candidate_edge:
  edge_id: edge.value_profile.shiprocket_invoice.payment_mode.profiles_column.column.zs_observe.shiprocket_invoice.payment_mode
  edge_type: PROFILES_COLUMN
  source: value_profile.shiprocket_invoice.payment_mode
  target: column.zs_observe.shiprocket_invoice.payment_mode
  fields:
    edge_family: data_understanding
    evidence_basis: value_profile.fields.column_id
    confidence: high
    canonical_cognee_edge: true
    logistics_only: true
    canonical_edge_type: PROFILES_COLUMN
    inverse_edge_type: HAS_VALUE_PROFILE
    materialize_inverse: true
    edge_class: canonical
    source_type: value_profile
    target_type: column
```
```yaml
candidate_edge:
  edge_id: edge.column.zs_observe.shiprocket_invoice.payment_mode.has_value_profile.value_profile.shiprocket_invoice.payment_mode
  edge_type: HAS_VALUE_PROFILE
  source: column.zs_observe.shiprocket_invoice.payment_mode
  target: value_profile.shiprocket_invoice.payment_mode
  fields:
    edge_family: data_understanding
    evidence_basis: materialized inverse of PROFILES_COLUMN
    confidence: high
    canonical_cognee_edge: true
    logistics_only: true
    canonical_edge_type: HAS_VALUE_PROFILE
    inverse_edge_type: PROFILES_COLUMN
    materialize_inverse: true
    edge_class: canonical
    source_type: column
    target_type: value_profile
    materialized_from: edge.value_profile.shiprocket_invoice.payment_mode.profiles_column.column.zs_observe.shiprocket_invoice.payment_mode
```
```yaml
candidate_edge:
  edge_id: edge.value_profile.shiprocket_invoice.payment_mode.profiles_table.table.zs_observe.shiprocket_invoice
  edge_type: PROFILES_TABLE
  source: value_profile.shiprocket_invoice.payment_mode
  target: table.zs_observe.shiprocket_invoice
  fields:
    edge_family: data_understanding
    evidence_basis: value_profile.fields.table_id
    confidence: high
    canonical_cognee_edge: true
    logistics_only: true
    canonical_edge_type: PROFILES_TABLE
    inverse_edge_type: HAS_VALUE_PROFILE
    materialize_inverse: true
    edge_class: canonical
    source_type: value_profile
    target_type: table
```
```yaml
candidate_edge:
  edge_id: edge.table.zs_observe.shiprocket_invoice.has_value_profile.value_profile.shiprocket_invoice.zone
  edge_type: HAS_VALUE_PROFILE
  source: table.zs_observe.shiprocket_invoice
  target: value_profile.shiprocket_invoice.zone
  fields:
    edge_family: data_understanding
    evidence_basis: value_profile.fields.column_id
    confidence: high
    canonical_cognee_edge: true
    logistics_only: true
    canonical_edge_type: HAS_VALUE_PROFILE
    inverse_edge_type: PROFILES_COLUMN_OR_PROFILES_TABLE
    materialize_inverse: true
    edge_class: canonical
    source_type: table
    target_type: value_profile
```
```yaml
candidate_edge:
  edge_id: edge.value_profile.shiprocket_invoice.zone.profiles_column.column.zs_observe.shiprocket_invoice.zone
  edge_type: PROFILES_COLUMN
  source: value_profile.shiprocket_invoice.zone
  target: column.zs_observe.shiprocket_invoice.zone
  fields:
    edge_family: data_understanding
    evidence_basis: value_profile.fields.column_id
    confidence: high
    canonical_cognee_edge: true
    logistics_only: true
    canonical_edge_type: PROFILES_COLUMN
    inverse_edge_type: HAS_VALUE_PROFILE
    materialize_inverse: true
    edge_class: canonical
    source_type: value_profile
    target_type: column
```
```yaml
candidate_edge:
  edge_id: edge.column.zs_observe.shiprocket_invoice.zone.has_value_profile.value_profile.shiprocket_invoice.zone
  edge_type: HAS_VALUE_PROFILE
  source: column.zs_observe.shiprocket_invoice.zone
  target: value_profile.shiprocket_invoice.zone
  fields:
    edge_family: data_understanding
    evidence_basis: materialized inverse of PROFILES_COLUMN
    confidence: high
    canonical_cognee_edge: true
    logistics_only: true
    canonical_edge_type: HAS_VALUE_PROFILE
    inverse_edge_type: PROFILES_COLUMN
    materialize_inverse: true
    edge_class: canonical
    source_type: column
    target_type: value_profile
    materialized_from: edge.value_profile.shiprocket_invoice.zone.profiles_column.column.zs_observe.shiprocket_invoice.zone
```
```yaml
candidate_edge:
  edge_id: edge.value_profile.shiprocket_invoice.zone.profiles_table.table.zs_observe.shiprocket_invoice
  edge_type: PROFILES_TABLE
  source: value_profile.shiprocket_invoice.zone
  target: table.zs_observe.shiprocket_invoice
  fields:
    edge_family: data_understanding
    evidence_basis: value_profile.fields.table_id
    confidence: high
    canonical_cognee_edge: true
    logistics_only: true
    canonical_edge_type: PROFILES_TABLE
    inverse_edge_type: HAS_VALUE_PROFILE
    materialize_inverse: true
    edge_class: canonical
    source_type: value_profile
    target_type: table
```
```yaml
candidate_edge:
  edge_id: edge.table.zs_observe.shiprocket_settlement.has_value_profile.value_profile.shiprocket_settlement.courier_partner
  edge_type: HAS_VALUE_PROFILE
  source: table.zs_observe.shiprocket_settlement
  target: value_profile.shiprocket_settlement.courier_partner
  fields:
    edge_family: data_understanding
    evidence_basis: value_profile.fields.column_id
    confidence: high
    canonical_cognee_edge: true
    logistics_only: true
    canonical_edge_type: HAS_VALUE_PROFILE
    inverse_edge_type: PROFILES_COLUMN_OR_PROFILES_TABLE
    materialize_inverse: true
    edge_class: canonical
    source_type: table
    target_type: value_profile
```
```yaml
candidate_edge:
  edge_id: edge.value_profile.shiprocket_settlement.courier_partner.profiles_column.column.zs_observe.shiprocket_settlement.courier_partner
  edge_type: PROFILES_COLUMN
  source: value_profile.shiprocket_settlement.courier_partner
  target: column.zs_observe.shiprocket_settlement.courier_partner
  fields:
    edge_family: data_understanding
    evidence_basis: value_profile.fields.column_id
    confidence: high
    canonical_cognee_edge: true
    logistics_only: true
    canonical_edge_type: PROFILES_COLUMN
    inverse_edge_type: HAS_VALUE_PROFILE
    materialize_inverse: true
    edge_class: canonical
    source_type: value_profile
    target_type: column
```
```yaml
candidate_edge:
  edge_id: edge.column.zs_observe.shiprocket_settlement.courier_partner.has_value_profile.value_profile.shiprocket_settlement.courier_partner
  edge_type: HAS_VALUE_PROFILE
  source: column.zs_observe.shiprocket_settlement.courier_partner
  target: value_profile.shiprocket_settlement.courier_partner
  fields:
    edge_family: data_understanding
    evidence_basis: materialized inverse of PROFILES_COLUMN
    confidence: high
    canonical_cognee_edge: true
    logistics_only: true
    canonical_edge_type: HAS_VALUE_PROFILE
    inverse_edge_type: PROFILES_COLUMN
    materialize_inverse: true
    edge_class: canonical
    source_type: column
    target_type: value_profile
    materialized_from: edge.value_profile.shiprocket_settlement.courier_partner.profiles_column.column.zs_observe.shiprocket_settlement.courier_partner
```
```yaml
candidate_edge:
  edge_id: edge.value_profile.shiprocket_settlement.courier_partner.profiles_table.table.zs_observe.shiprocket_settlement
  edge_type: PROFILES_TABLE
  source: value_profile.shiprocket_settlement.courier_partner
  target: table.zs_observe.shiprocket_settlement
  fields:
    edge_family: data_understanding
    evidence_basis: value_profile.fields.table_id
    confidence: high
    canonical_cognee_edge: true
    logistics_only: true
    canonical_edge_type: PROFILES_TABLE
    inverse_edge_type: HAS_VALUE_PROFILE
    materialize_inverse: true
    edge_class: canonical
    source_type: value_profile
    target_type: table
```
```yaml
candidate_edge:
  edge_id: edge.table.zs_observe.shiprocket_settlement_report.has_value_profile.value_profile.shiprocket_settlement_report.awb_remittance_status
  edge_type: HAS_VALUE_PROFILE
  source: table.zs_observe.shiprocket_settlement_report
  target: value_profile.shiprocket_settlement_report.awb_remittance_status
  fields:
    edge_family: data_understanding
    evidence_basis: value_profile.fields.column_id
    confidence: high
    canonical_cognee_edge: true
    logistics_only: true
    canonical_edge_type: HAS_VALUE_PROFILE
    inverse_edge_type: PROFILES_COLUMN_OR_PROFILES_TABLE
    materialize_inverse: true
    edge_class: canonical
    source_type: table
    target_type: value_profile
```
```yaml
candidate_edge:
  edge_id: edge.value_profile.shiprocket_settlement_report.awb_remittance_status.profiles_column.column.zs_observe.shiprocket_settlement_report.awb_remittance_status
  edge_type: PROFILES_COLUMN
  source: value_profile.shiprocket_settlement_report.awb_remittance_status
  target: column.zs_observe.shiprocket_settlement_report.awb_remittance_status
  fields:
    edge_family: data_understanding
    evidence_basis: value_profile.fields.column_id
    confidence: high
    canonical_cognee_edge: true
    logistics_only: true
    canonical_edge_type: PROFILES_COLUMN
    inverse_edge_type: HAS_VALUE_PROFILE
    materialize_inverse: true
    edge_class: canonical
    source_type: value_profile
    target_type: column
```
```yaml
candidate_edge:
  edge_id: edge.column.zs_observe.shiprocket_settlement_report.awb_remittance_status.has_value_profile.value_profile.shiprocket_settlement_report.awb_remittance_status
  edge_type: HAS_VALUE_PROFILE
  source: column.zs_observe.shiprocket_settlement_report.awb_remittance_status
  target: value_profile.shiprocket_settlement_report.awb_remittance_status
  fields:
    edge_family: data_understanding
    evidence_basis: materialized inverse of PROFILES_COLUMN
    confidence: high
    canonical_cognee_edge: true
    logistics_only: true
    canonical_edge_type: HAS_VALUE_PROFILE
    inverse_edge_type: PROFILES_COLUMN
    materialize_inverse: true
    edge_class: canonical
    source_type: column
    target_type: value_profile
    materialized_from: edge.value_profile.shiprocket_settlement_report.awb_remittance_status.profiles_column.column.zs_observe.shiprocket_settlement_report.awb_remittance_status
```
```yaml
candidate_edge:
  edge_id: edge.value_profile.shiprocket_settlement_report.awb_remittance_status.profiles_table.table.zs_observe.shiprocket_settlement_report
  edge_type: PROFILES_TABLE
  source: value_profile.shiprocket_settlement_report.awb_remittance_status
  target: table.zs_observe.shiprocket_settlement_report
  fields:
    edge_family: data_understanding
    evidence_basis: value_profile.fields.table_id
    confidence: high
    canonical_cognee_edge: true
    logistics_only: true
    canonical_edge_type: PROFILES_TABLE
    inverse_edge_type: HAS_VALUE_PROFILE
    materialize_inverse: true
    edge_class: canonical
    source_type: value_profile
    target_type: table
```
```yaml
candidate_edge:
  edge_id: edge.metric.freight_billed_amount.has_implementation.metric_impl.shiprocket_invoice.freight_billed_amount
  edge_type: HAS_IMPLEMENTATION
  source: metric.freight_billed_amount
  target: metric_impl.shiprocket_invoice.freight_billed_amount
  fields:
    edge_family: metric_understanding
    evidence_basis: metric_implementation.fields.metric_id
    confidence: high
    canonical_cognee_edge: true
    logistics_only: true
    canonical_edge_type: HAS_IMPLEMENTATION
    inverse_edge_type: IMPLEMENTS_METRIC
    materialize_inverse: true
    edge_class: canonical
    source_type: metric
    target_type: metric_implementation
```
```yaml
candidate_edge:
  edge_id: edge.metric_impl.shiprocket_invoice.freight_billed_amount.implements_metric.metric.freight_billed_amount
  edge_type: IMPLEMENTS_METRIC
  source: metric_impl.shiprocket_invoice.freight_billed_amount
  target: metric.freight_billed_amount
  fields:
    edge_family: metric_understanding
    evidence_basis: materialized inverse of HAS_IMPLEMENTATION
    confidence: high
    canonical_cognee_edge: true
    logistics_only: true
    canonical_edge_type: IMPLEMENTS_METRIC
    inverse_edge_type: HAS_IMPLEMENTATION
    materialize_inverse: true
    edge_class: canonical
    source_type: metric_implementation
    target_type: metric
    materialized_from: edge.metric.freight_billed_amount.has_implementation.metric_impl.shiprocket_invoice.freight_billed_amount
```
```yaml
candidate_edge:
  edge_id: edge.metric_impl.shiprocket_invoice.freight_billed_amount.uses_table.table.zs_observe.shiprocket_invoice
  edge_type: USES_TABLE
  source: metric_impl.shiprocket_invoice.freight_billed_amount
  target: table.zs_observe.shiprocket_invoice
  fields:
    edge_family: metric_understanding
    evidence_basis: metric_implementation.fields.base_tables
    confidence: high
    canonical_cognee_edge: true
    logistics_only: true
    canonical_edge_type: USES_TABLE
    inverse_edge_type: USED_BY_CONTEXT
    materialize_inverse: false
    edge_class: canonical
    source_type: metric_implementation
    target_type: table
```
```yaml
candidate_edge:
  edge_id: edge.metric_impl.shiprocket_invoice.freight_billed_amount.uses_column.column.zs_observe.shiprocket_invoice.charged_amount.8737448c
  edge_type: USES_COLUMN
  source: metric_impl.shiprocket_invoice.freight_billed_amount
  target: column.zs_observe.shiprocket_invoice.charged_amount
  fields:
    edge_family: metric_understanding
    evidence_basis: metric_implementation.fields.required_columns
    confidence: high
    canonical_cognee_edge: true
    logistics_only: true
    canonical_edge_type: USES_COLUMN
    inverse_edge_type: USED_BY_CONTEXT
    materialize_inverse: false
    edge_class: canonical
    source_type: metric_implementation
    target_type: column
    edge_properties:
      column_role: amount
```
```yaml
candidate_edge:
  edge_id: edge.metric_impl.shiprocket_invoice.freight_billed_amount.uses_formula_template.formula_template.logistics.component_sum
  edge_type: USES_FORMULA_TEMPLATE
  source: metric_impl.shiprocket_invoice.freight_billed_amount
  target: formula_template.logistics.component_sum
  fields:
    edge_family: metric_understanding
    evidence_basis: metric_implementation.fields.formula_template_id
    confidence: high
    canonical_cognee_edge: true
    logistics_only: true
    canonical_edge_type: USES_FORMULA_TEMPLATE
    inverse_edge_type: USED_BY_IMPLEMENTATION
    materialize_inverse: false
    edge_class: canonical
    source_type: metric_implementation
    target_type: formula_template
```
```yaml
candidate_edge:
  edge_id: edge.metric.freight_excluding_tax_amount.has_implementation.metric_impl.shiprocket_invoice.freight_excluding_tax_amount
  edge_type: HAS_IMPLEMENTATION
  source: metric.freight_excluding_tax_amount
  target: metric_impl.shiprocket_invoice.freight_excluding_tax_amount
  fields:
    edge_family: metric_understanding
    evidence_basis: metric_implementation.fields.metric_id
    confidence: high
    canonical_cognee_edge: true
    logistics_only: true
    canonical_edge_type: HAS_IMPLEMENTATION
    inverse_edge_type: IMPLEMENTS_METRIC
    materialize_inverse: true
    edge_class: canonical
    source_type: metric
    target_type: metric_implementation
```
```yaml
candidate_edge:
  edge_id: edge.metric_impl.shiprocket_invoice.freight_excluding_tax_amount.implements_metric.metric.freight_excluding_tax_amount
  edge_type: IMPLEMENTS_METRIC
  source: metric_impl.shiprocket_invoice.freight_excluding_tax_amount
  target: metric.freight_excluding_tax_amount
  fields:
    edge_family: metric_understanding
    evidence_basis: materialized inverse of HAS_IMPLEMENTATION
    confidence: high
    canonical_cognee_edge: true
    logistics_only: true
    canonical_edge_type: IMPLEMENTS_METRIC
    inverse_edge_type: HAS_IMPLEMENTATION
    materialize_inverse: true
    edge_class: canonical
    source_type: metric_implementation
    target_type: metric
    materialized_from: edge.metric.freight_excluding_tax_amount.has_implementation.metric_impl.shiprocket_invoice.freight_excluding_tax_amount
```
```yaml
candidate_edge:
  edge_id: edge.metric_impl.shiprocket_invoice.freight_excluding_tax_amount.uses_table.table.zs_observe.shiprocket_invoice
  edge_type: USES_TABLE
  source: metric_impl.shiprocket_invoice.freight_excluding_tax_amount
  target: table.zs_observe.shiprocket_invoice
  fields:
    edge_family: metric_understanding
    evidence_basis: metric_implementation.fields.base_tables
    confidence: high
    canonical_cognee_edge: true
    logistics_only: true
    canonical_edge_type: USES_TABLE
    inverse_edge_type: USED_BY_CONTEXT
    materialize_inverse: false
    edge_class: canonical
    source_type: metric_implementation
    target_type: table
```
```yaml
candidate_edge:
  edge_id: edge.metric_impl.shiprocket_invoice.freight_excluding_tax_amount.uses_column.column.zs_observe.shiprocket_invoice.charged_amount_excluding_tax.8737448c
  edge_type: USES_COLUMN
  source: metric_impl.shiprocket_invoice.freight_excluding_tax_amount
  target: column.zs_observe.shiprocket_invoice.charged_amount_excluding_tax
  fields:
    edge_family: metric_understanding
    evidence_basis: metric_implementation.fields.required_columns
    confidence: high
    canonical_cognee_edge: true
    logistics_only: true
    canonical_edge_type: USES_COLUMN
    inverse_edge_type: USED_BY_CONTEXT
    materialize_inverse: false
    edge_class: canonical
    source_type: metric_implementation
    target_type: column
    edge_properties:
      column_role: amount
```
```yaml
candidate_edge:
  edge_id: edge.metric_impl.shiprocket_invoice.freight_excluding_tax_amount.uses_formula_template.formula_template.logistics.component_sum
  edge_type: USES_FORMULA_TEMPLATE
  source: metric_impl.shiprocket_invoice.freight_excluding_tax_amount
  target: formula_template.logistics.component_sum
  fields:
    edge_family: metric_understanding
    evidence_basis: metric_implementation.fields.formula_template_id
    confidence: high
    canonical_cognee_edge: true
    logistics_only: true
    canonical_edge_type: USES_FORMULA_TEMPLATE
    inverse_edge_type: USED_BY_IMPLEMENTATION
    materialize_inverse: false
    edge_class: canonical
    source_type: metric_implementation
    target_type: formula_template
```
```yaml
candidate_edge:
  edge_id: edge.metric.gst_on_freight_amount.has_implementation.metric_impl.shiprocket_invoice.gst_on_freight_amount
  edge_type: HAS_IMPLEMENTATION
  source: metric.gst_on_freight_amount
  target: metric_impl.shiprocket_invoice.gst_on_freight_amount
  fields:
    edge_family: metric_understanding
    evidence_basis: metric_implementation.fields.metric_id
    confidence: high
    canonical_cognee_edge: true
    logistics_only: true
    canonical_edge_type: HAS_IMPLEMENTATION
    inverse_edge_type: IMPLEMENTS_METRIC
    materialize_inverse: true
    edge_class: canonical
    source_type: metric
    target_type: metric_implementation
```
```yaml
candidate_edge:
  edge_id: edge.metric_impl.shiprocket_invoice.gst_on_freight_amount.implements_metric.metric.gst_on_freight_amount
  edge_type: IMPLEMENTS_METRIC
  source: metric_impl.shiprocket_invoice.gst_on_freight_amount
  target: metric.gst_on_freight_amount
  fields:
    edge_family: metric_understanding
    evidence_basis: materialized inverse of HAS_IMPLEMENTATION
    confidence: high
    canonical_cognee_edge: true
    logistics_only: true
    canonical_edge_type: IMPLEMENTS_METRIC
    inverse_edge_type: HAS_IMPLEMENTATION
    materialize_inverse: true
    edge_class: canonical
    source_type: metric_implementation
    target_type: metric
    materialized_from: edge.metric.gst_on_freight_amount.has_implementation.metric_impl.shiprocket_invoice.gst_on_freight_amount
```
```yaml
candidate_edge:
  edge_id: edge.metric_impl.shiprocket_invoice.gst_on_freight_amount.uses_table.table.zs_observe.shiprocket_invoice
  edge_type: USES_TABLE
  source: metric_impl.shiprocket_invoice.gst_on_freight_amount
  target: table.zs_observe.shiprocket_invoice
  fields:
    edge_family: metric_understanding
    evidence_basis: metric_implementation.fields.base_tables
    confidence: high
    canonical_cognee_edge: true
    logistics_only: true
    canonical_edge_type: USES_TABLE
    inverse_edge_type: USED_BY_CONTEXT
    materialize_inverse: false
    edge_class: canonical
    source_type: metric_implementation
    target_type: table
```
```yaml
candidate_edge:
  edge_id: edge.metric_impl.shiprocket_invoice.gst_on_freight_amount.uses_column.column.zs_observe.shiprocket_invoice.total_tax.8737448c
  edge_type: USES_COLUMN
  source: metric_impl.shiprocket_invoice.gst_on_freight_amount
  target: column.zs_observe.shiprocket_invoice.total_tax
  fields:
    edge_family: metric_understanding
    evidence_basis: metric_implementation.fields.required_columns
    confidence: high
    canonical_cognee_edge: true
    logistics_only: true
    canonical_edge_type: USES_COLUMN
    inverse_edge_type: USED_BY_CONTEXT
    materialize_inverse: false
    edge_class: canonical
    source_type: metric_implementation
    target_type: column
    edge_properties:
      column_role: amount
```
```yaml
candidate_edge:
  edge_id: edge.metric_impl.shiprocket_invoice.gst_on_freight_amount.uses_formula_template.formula_template.logistics.component_sum
  edge_type: USES_FORMULA_TEMPLATE
  source: metric_impl.shiprocket_invoice.gst_on_freight_amount
  target: formula_template.logistics.component_sum
  fields:
    edge_family: metric_understanding
    evidence_basis: metric_implementation.fields.formula_template_id
    confidence: high
    canonical_cognee_edge: true
    logistics_only: true
    canonical_edge_type: USES_FORMULA_TEMPLATE
    inverse_edge_type: USED_BY_IMPLEMENTATION
    materialize_inverse: false
    edge_class: canonical
    source_type: metric_implementation
    target_type: formula_template
```
```yaml
candidate_edge:
  edge_id: edge.metric.fuel_surcharge_amount.has_implementation.metric_impl.shiprocket_invoice.fuel_surcharge_amount
  edge_type: HAS_IMPLEMENTATION
  source: metric.fuel_surcharge_amount
  target: metric_impl.shiprocket_invoice.fuel_surcharge_amount
  fields:
    edge_family: metric_understanding
    evidence_basis: metric_implementation.fields.metric_id
    confidence: high
    canonical_cognee_edge: true
    logistics_only: true
    canonical_edge_type: HAS_IMPLEMENTATION
    inverse_edge_type: IMPLEMENTS_METRIC
    materialize_inverse: true
    edge_class: canonical
    source_type: metric
    target_type: metric_implementation
```
```yaml
candidate_edge:
  edge_id: edge.metric_impl.shiprocket_invoice.fuel_surcharge_amount.implements_metric.metric.fuel_surcharge_amount
  edge_type: IMPLEMENTS_METRIC
  source: metric_impl.shiprocket_invoice.fuel_surcharge_amount
  target: metric.fuel_surcharge_amount
  fields:
    edge_family: metric_understanding
    evidence_basis: materialized inverse of HAS_IMPLEMENTATION
    confidence: high
    canonical_cognee_edge: true
    logistics_only: true
    canonical_edge_type: IMPLEMENTS_METRIC
    inverse_edge_type: HAS_IMPLEMENTATION
    materialize_inverse: true
    edge_class: canonical
    source_type: metric_implementation
    target_type: metric
    materialized_from: edge.metric.fuel_surcharge_amount.has_implementation.metric_impl.shiprocket_invoice.fuel_surcharge_amount
```
```yaml
candidate_edge:
  edge_id: edge.metric_impl.shiprocket_invoice.fuel_surcharge_amount.uses_table.table.zs_observe.shiprocket_invoice
  edge_type: USES_TABLE
  source: metric_impl.shiprocket_invoice.fuel_surcharge_amount
  target: table.zs_observe.shiprocket_invoice
  fields:
    edge_family: metric_understanding
    evidence_basis: metric_implementation.fields.base_tables
    confidence: high
    canonical_cognee_edge: true
    logistics_only: true
    canonical_edge_type: USES_TABLE
    inverse_edge_type: USED_BY_CONTEXT
    materialize_inverse: false
    edge_class: canonical
    source_type: metric_implementation
    target_type: table
```
```yaml
candidate_edge:
  edge_id: edge.metric_impl.shiprocket_invoice.fuel_surcharge_amount.uses_column.column.zs_observe.shiprocket_invoice.charge_fsc.8737448c
  edge_type: USES_COLUMN
  source: metric_impl.shiprocket_invoice.fuel_surcharge_amount
  target: column.zs_observe.shiprocket_invoice.charge_fsc
  fields:
    edge_family: metric_understanding
    evidence_basis: metric_implementation.fields.required_columns
    confidence: high
    canonical_cognee_edge: true
    logistics_only: true
    canonical_edge_type: USES_COLUMN
    inverse_edge_type: USED_BY_CONTEXT
    materialize_inverse: false
    edge_class: canonical
    source_type: metric_implementation
    target_type: column
    edge_properties:
      column_role: amount
```
```yaml
candidate_edge:
  edge_id: edge.metric_impl.shiprocket_invoice.fuel_surcharge_amount.uses_formula_template.formula_template.logistics.component_sum
  edge_type: USES_FORMULA_TEMPLATE
  source: metric_impl.shiprocket_invoice.fuel_surcharge_amount
  target: formula_template.logistics.component_sum
  fields:
    edge_family: metric_understanding
    evidence_basis: metric_implementation.fields.formula_template_id
    confidence: high
    canonical_cognee_edge: true
    logistics_only: true
    canonical_edge_type: USES_FORMULA_TEMPLATE
    inverse_edge_type: USED_BY_IMPLEMENTATION
    materialize_inverse: false
    edge_class: canonical
    source_type: metric_implementation
    target_type: formula_template
```
```yaml
candidate_edge:
  edge_id: edge.metric.rto_freight_amount.has_implementation.metric_impl.shiprocket_invoice.rto_freight_amount
  edge_type: HAS_IMPLEMENTATION
  source: metric.rto_freight_amount
  target: metric_impl.shiprocket_invoice.rto_freight_amount
  fields:
    edge_family: metric_understanding
    evidence_basis: metric_implementation.fields.metric_id
    confidence: high
    canonical_cognee_edge: true
    logistics_only: true
    canonical_edge_type: HAS_IMPLEMENTATION
    inverse_edge_type: IMPLEMENTS_METRIC
    materialize_inverse: true
    edge_class: canonical
    source_type: metric
    target_type: metric_implementation
```
```yaml
candidate_edge:
  edge_id: edge.metric_impl.shiprocket_invoice.rto_freight_amount.implements_metric.metric.rto_freight_amount
  edge_type: IMPLEMENTS_METRIC
  source: metric_impl.shiprocket_invoice.rto_freight_amount
  target: metric.rto_freight_amount
  fields:
    edge_family: metric_understanding
    evidence_basis: materialized inverse of HAS_IMPLEMENTATION
    confidence: high
    canonical_cognee_edge: true
    logistics_only: true
    canonical_edge_type: IMPLEMENTS_METRIC
    inverse_edge_type: HAS_IMPLEMENTATION
    materialize_inverse: true
    edge_class: canonical
    source_type: metric_implementation
    target_type: metric
    materialized_from: edge.metric.rto_freight_amount.has_implementation.metric_impl.shiprocket_invoice.rto_freight_amount
```
```yaml
candidate_edge:
  edge_id: edge.metric_impl.shiprocket_invoice.rto_freight_amount.uses_table.table.zs_observe.shiprocket_invoice
  edge_type: USES_TABLE
  source: metric_impl.shiprocket_invoice.rto_freight_amount
  target: table.zs_observe.shiprocket_invoice
  fields:
    edge_family: metric_understanding
    evidence_basis: metric_implementation.fields.base_tables
    confidence: high
    canonical_cognee_edge: true
    logistics_only: true
    canonical_edge_type: USES_TABLE
    inverse_edge_type: USED_BY_CONTEXT
    materialize_inverse: false
    edge_class: canonical
    source_type: metric_implementation
    target_type: table
```
```yaml
candidate_edge:
  edge_id: edge.metric_impl.shiprocket_invoice.rto_freight_amount.uses_column.column.zs_observe.shiprocket_invoice.charge_rto.8737448c
  edge_type: USES_COLUMN
  source: metric_impl.shiprocket_invoice.rto_freight_amount
  target: column.zs_observe.shiprocket_invoice.charge_rto
  fields:
    edge_family: metric_understanding
    evidence_basis: metric_implementation.fields.required_columns
    confidence: high
    canonical_cognee_edge: true
    logistics_only: true
    canonical_edge_type: USES_COLUMN
    inverse_edge_type: USED_BY_CONTEXT
    materialize_inverse: false
    edge_class: canonical
    source_type: metric_implementation
    target_type: column
    edge_properties:
      column_role: amount
```
```yaml
candidate_edge:
  edge_id: edge.metric_impl.shiprocket_invoice.rto_freight_amount.uses_formula_template.formula_template.logistics.component_sum
  edge_type: USES_FORMULA_TEMPLATE
  source: metric_impl.shiprocket_invoice.rto_freight_amount
  target: formula_template.logistics.component_sum
  fields:
    edge_family: metric_understanding
    evidence_basis: metric_implementation.fields.formula_template_id
    confidence: high
    canonical_cognee_edge: true
    logistics_only: true
    canonical_edge_type: USES_FORMULA_TEMPLATE
    inverse_edge_type: USED_BY_IMPLEMENTATION
    materialize_inverse: false
    edge_class: canonical
    source_type: metric_implementation
    target_type: formula_template
```
```yaml
candidate_edge:
  edge_id: edge.metric.cod_fee_amount.has_implementation.metric_impl.shiprocket_invoice.cod_fee_amount
  edge_type: HAS_IMPLEMENTATION
  source: metric.cod_fee_amount
  target: metric_impl.shiprocket_invoice.cod_fee_amount
  fields:
    edge_family: metric_understanding
    evidence_basis: metric_implementation.fields.metric_id
    confidence: high
    canonical_cognee_edge: true
    logistics_only: true
    canonical_edge_type: HAS_IMPLEMENTATION
    inverse_edge_type: IMPLEMENTS_METRIC
    materialize_inverse: true
    edge_class: canonical
    source_type: metric
    target_type: metric_implementation
```
```yaml
candidate_edge:
  edge_id: edge.metric_impl.shiprocket_invoice.cod_fee_amount.implements_metric.metric.cod_fee_amount
  edge_type: IMPLEMENTS_METRIC
  source: metric_impl.shiprocket_invoice.cod_fee_amount
  target: metric.cod_fee_amount
  fields:
    edge_family: metric_understanding
    evidence_basis: materialized inverse of HAS_IMPLEMENTATION
    confidence: high
    canonical_cognee_edge: true
    logistics_only: true
    canonical_edge_type: IMPLEMENTS_METRIC
    inverse_edge_type: HAS_IMPLEMENTATION
    materialize_inverse: true
    edge_class: canonical
    source_type: metric_implementation
    target_type: metric
    materialized_from: edge.metric.cod_fee_amount.has_implementation.metric_impl.shiprocket_invoice.cod_fee_amount
```
```yaml
candidate_edge:
  edge_id: edge.metric_impl.shiprocket_invoice.cod_fee_amount.uses_table.table.zs_observe.shiprocket_invoice
  edge_type: USES_TABLE
  source: metric_impl.shiprocket_invoice.cod_fee_amount
  target: table.zs_observe.shiprocket_invoice
  fields:
    edge_family: metric_understanding
    evidence_basis: metric_implementation.fields.base_tables
    confidence: high
    canonical_cognee_edge: true
    logistics_only: true
    canonical_edge_type: USES_TABLE
    inverse_edge_type: USED_BY_CONTEXT
    materialize_inverse: false
    edge_class: canonical
    source_type: metric_implementation
    target_type: table
```
```yaml
candidate_edge:
  edge_id: edge.metric_impl.shiprocket_invoice.cod_fee_amount.uses_column.column.zs_observe.shiprocket_invoice.charge_cod.8737448c
  edge_type: USES_COLUMN
  source: metric_impl.shiprocket_invoice.cod_fee_amount
  target: column.zs_observe.shiprocket_invoice.charge_cod
  fields:
    edge_family: metric_understanding
    evidence_basis: metric_implementation.fields.required_columns
    confidence: high
    canonical_cognee_edge: true
    logistics_only: true
    canonical_edge_type: USES_COLUMN
    inverse_edge_type: USED_BY_CONTEXT
    materialize_inverse: false
    edge_class: canonical
    source_type: metric_implementation
    target_type: column
    edge_properties:
      column_role: amount
```
```yaml
candidate_edge:
  edge_id: edge.metric_impl.shiprocket_invoice.cod_fee_amount.uses_formula_template.formula_template.logistics.component_sum
  edge_type: USES_FORMULA_TEMPLATE
  source: metric_impl.shiprocket_invoice.cod_fee_amount
  target: formula_template.logistics.component_sum
  fields:
    edge_family: metric_understanding
    evidence_basis: metric_implementation.fields.formula_template_id
    confidence: high
    canonical_cognee_edge: true
    logistics_only: true
    canonical_edge_type: USES_FORMULA_TEMPLATE
    inverse_edge_type: USED_BY_IMPLEMENTATION
    materialize_inverse: false
    edge_class: canonical
    source_type: metric_implementation
    target_type: formula_template
```
```yaml
candidate_edge:
  edge_id: edge.metric.forward_freight_amount.has_implementation.metric_impl.shiprocket_invoice.forward_freight_amount
  edge_type: HAS_IMPLEMENTATION
  source: metric.forward_freight_amount
  target: metric_impl.shiprocket_invoice.forward_freight_amount
  fields:
    edge_family: metric_understanding
    evidence_basis: metric_implementation.fields.metric_id
    confidence: high
    canonical_cognee_edge: true
    logistics_only: true
    canonical_edge_type: HAS_IMPLEMENTATION
    inverse_edge_type: IMPLEMENTS_METRIC
    materialize_inverse: true
    edge_class: canonical
    source_type: metric
    target_type: metric_implementation
```
```yaml
candidate_edge:
  edge_id: edge.metric_impl.shiprocket_invoice.forward_freight_amount.implements_metric.metric.forward_freight_amount
  edge_type: IMPLEMENTS_METRIC
  source: metric_impl.shiprocket_invoice.forward_freight_amount
  target: metric.forward_freight_amount
  fields:
    edge_family: metric_understanding
    evidence_basis: materialized inverse of HAS_IMPLEMENTATION
    confidence: high
    canonical_cognee_edge: true
    logistics_only: true
    canonical_edge_type: IMPLEMENTS_METRIC
    inverse_edge_type: HAS_IMPLEMENTATION
    materialize_inverse: true
    edge_class: canonical
    source_type: metric_implementation
    target_type: metric
    materialized_from: edge.metric.forward_freight_amount.has_implementation.metric_impl.shiprocket_invoice.forward_freight_amount
```
```yaml
candidate_edge:
  edge_id: edge.metric_impl.shiprocket_invoice.forward_freight_amount.uses_table.table.zs_observe.shiprocket_invoice
  edge_type: USES_TABLE
  source: metric_impl.shiprocket_invoice.forward_freight_amount
  target: table.zs_observe.shiprocket_invoice
  fields:
    edge_family: metric_understanding
    evidence_basis: metric_implementation.fields.base_tables
    confidence: high
    canonical_cognee_edge: true
    logistics_only: true
    canonical_edge_type: USES_TABLE
    inverse_edge_type: USED_BY_CONTEXT
    materialize_inverse: false
    edge_class: canonical
    source_type: metric_implementation
    target_type: table
```
```yaml
candidate_edge:
  edge_id: edge.metric_impl.shiprocket_invoice.forward_freight_amount.uses_column.column.zs_observe.shiprocket_invoice.charge_dl.8737448c
  edge_type: USES_COLUMN
  source: metric_impl.shiprocket_invoice.forward_freight_amount
  target: column.zs_observe.shiprocket_invoice.charge_dl
  fields:
    edge_family: metric_understanding
    evidence_basis: metric_implementation.fields.required_columns
    confidence: high
    canonical_cognee_edge: true
    logistics_only: true
    canonical_edge_type: USES_COLUMN
    inverse_edge_type: USED_BY_CONTEXT
    materialize_inverse: false
    edge_class: canonical
    source_type: metric_implementation
    target_type: column
    edge_properties:
      column_role: amount
```
```yaml
candidate_edge:
  edge_id: edge.metric_impl.shiprocket_invoice.forward_freight_amount.uses_formula_template.formula_template.logistics.component_sum
  edge_type: USES_FORMULA_TEMPLATE
  source: metric_impl.shiprocket_invoice.forward_freight_amount
  target: formula_template.logistics.component_sum
  fields:
    edge_family: metric_understanding
    evidence_basis: metric_implementation.fields.formula_template_id
    confidence: high
    canonical_cognee_edge: true
    logistics_only: true
    canonical_edge_type: USES_FORMULA_TEMPLATE
    inverse_edge_type: USED_BY_IMPLEMENTATION
    materialize_inverse: false
    edge_class: canonical
    source_type: metric_implementation
    target_type: formula_template
```
```yaml
candidate_edge:
  edge_id: edge.metric.actual_weight.has_implementation.metric_impl.shiprocket_invoice.actual_weight
  edge_type: HAS_IMPLEMENTATION
  source: metric.actual_weight
  target: metric_impl.shiprocket_invoice.actual_weight
  fields:
    edge_family: metric_understanding
    evidence_basis: metric_implementation.fields.metric_id
    confidence: high
    canonical_cognee_edge: true
    logistics_only: true
    canonical_edge_type: HAS_IMPLEMENTATION
    inverse_edge_type: IMPLEMENTS_METRIC
    materialize_inverse: true
    edge_class: canonical
    source_type: metric
    target_type: metric_implementation
```
```yaml
candidate_edge:
  edge_id: edge.metric_impl.shiprocket_invoice.actual_weight.implements_metric.metric.actual_weight
  edge_type: IMPLEMENTS_METRIC
  source: metric_impl.shiprocket_invoice.actual_weight
  target: metric.actual_weight
  fields:
    edge_family: metric_understanding
    evidence_basis: materialized inverse of HAS_IMPLEMENTATION
    confidence: high
    canonical_cognee_edge: true
    logistics_only: true
    canonical_edge_type: IMPLEMENTS_METRIC
    inverse_edge_type: HAS_IMPLEMENTATION
    materialize_inverse: true
    edge_class: canonical
    source_type: metric_implementation
    target_type: metric
    materialized_from: edge.metric.actual_weight.has_implementation.metric_impl.shiprocket_invoice.actual_weight
```
```yaml
candidate_edge:
  edge_id: edge.metric_impl.shiprocket_invoice.actual_weight.uses_table.table.zs_observe.shiprocket_invoice
  edge_type: USES_TABLE
  source: metric_impl.shiprocket_invoice.actual_weight
  target: table.zs_observe.shiprocket_invoice
  fields:
    edge_family: metric_understanding
    evidence_basis: metric_implementation.fields.base_tables
    confidence: high
    canonical_cognee_edge: true
    logistics_only: true
    canonical_edge_type: USES_TABLE
    inverse_edge_type: USED_BY_CONTEXT
    materialize_inverse: false
    edge_class: canonical
    source_type: metric_implementation
    target_type: table
```
```yaml
candidate_edge:
  edge_id: edge.metric_impl.shiprocket_invoice.actual_weight.uses_column.column.zs_observe.shiprocket_invoice.final_weight.340e855f
  edge_type: USES_COLUMN
  source: metric_impl.shiprocket_invoice.actual_weight
  target: column.zs_observe.shiprocket_invoice.final_weight
  fields:
    edge_family: metric_understanding
    evidence_basis: metric_implementation.fields.required_columns
    confidence: high
    canonical_cognee_edge: true
    logistics_only: true
    canonical_edge_type: USES_COLUMN
    inverse_edge_type: USED_BY_CONTEXT
    materialize_inverse: false
    edge_class: canonical
    source_type: metric_implementation
    target_type: column
    edge_properties:
      column_role: formula_component
```
```yaml
candidate_edge:
  edge_id: edge.metric_impl.shiprocket_invoice.actual_weight.uses_formula_template.formula_template.logistics.component_sum
  edge_type: USES_FORMULA_TEMPLATE
  source: metric_impl.shiprocket_invoice.actual_weight
  target: formula_template.logistics.component_sum
  fields:
    edge_family: metric_understanding
    evidence_basis: metric_implementation.fields.formula_template_id
    confidence: high
    canonical_cognee_edge: true
    logistics_only: true
    canonical_edge_type: USES_FORMULA_TEMPLATE
    inverse_edge_type: USED_BY_IMPLEMENTATION
    materialize_inverse: false
    edge_class: canonical
    source_type: metric_implementation
    target_type: formula_template
```
```yaml
candidate_edge:
  edge_id: edge.metric.billable_weight.has_implementation.metric_impl.shiprocket_invoice.billable_weight
  edge_type: HAS_IMPLEMENTATION
  source: metric.billable_weight
  target: metric_impl.shiprocket_invoice.billable_weight
  fields:
    edge_family: metric_understanding
    evidence_basis: metric_implementation.fields.metric_id
    confidence: high
    canonical_cognee_edge: true
    logistics_only: true
    canonical_edge_type: HAS_IMPLEMENTATION
    inverse_edge_type: IMPLEMENTS_METRIC
    materialize_inverse: true
    edge_class: canonical
    source_type: metric
    target_type: metric_implementation
```
```yaml
candidate_edge:
  edge_id: edge.metric_impl.shiprocket_invoice.billable_weight.implements_metric.metric.billable_weight
  edge_type: IMPLEMENTS_METRIC
  source: metric_impl.shiprocket_invoice.billable_weight
  target: metric.billable_weight
  fields:
    edge_family: metric_understanding
    evidence_basis: materialized inverse of HAS_IMPLEMENTATION
    confidence: high
    canonical_cognee_edge: true
    logistics_only: true
    canonical_edge_type: IMPLEMENTS_METRIC
    inverse_edge_type: HAS_IMPLEMENTATION
    materialize_inverse: true
    edge_class: canonical
    source_type: metric_implementation
    target_type: metric
    materialized_from: edge.metric.billable_weight.has_implementation.metric_impl.shiprocket_invoice.billable_weight
```
```yaml
candidate_edge:
  edge_id: edge.metric_impl.shiprocket_invoice.billable_weight.uses_table.table.zs_observe.shiprocket_invoice
  edge_type: USES_TABLE
  source: metric_impl.shiprocket_invoice.billable_weight
  target: table.zs_observe.shiprocket_invoice
  fields:
    edge_family: metric_understanding
    evidence_basis: metric_implementation.fields.base_tables
    confidence: high
    canonical_cognee_edge: true
    logistics_only: true
    canonical_edge_type: USES_TABLE
    inverse_edge_type: USED_BY_CONTEXT
    materialize_inverse: false
    edge_class: canonical
    source_type: metric_implementation
    target_type: table
```
```yaml
candidate_edge:
  edge_id: edge.metric_impl.shiprocket_invoice.billable_weight.uses_column.column.zs_observe.shiprocket_invoice.charged_weight.8737448c
  edge_type: USES_COLUMN
  source: metric_impl.shiprocket_invoice.billable_weight
  target: column.zs_observe.shiprocket_invoice.charged_weight
  fields:
    edge_family: metric_understanding
    evidence_basis: metric_implementation.fields.required_columns
    confidence: high
    canonical_cognee_edge: true
    logistics_only: true
    canonical_edge_type: USES_COLUMN
    inverse_edge_type: USED_BY_CONTEXT
    materialize_inverse: false
    edge_class: canonical
    source_type: metric_implementation
    target_type: column
    edge_properties:
      column_role: amount
```
```yaml
candidate_edge:
  edge_id: edge.metric_impl.shiprocket_invoice.billable_weight.uses_formula_template.formula_template.logistics.component_sum
  edge_type: USES_FORMULA_TEMPLATE
  source: metric_impl.shiprocket_invoice.billable_weight
  target: formula_template.logistics.component_sum
  fields:
    edge_family: metric_understanding
    evidence_basis: metric_implementation.fields.formula_template_id
    confidence: high
    canonical_cognee_edge: true
    logistics_only: true
    canonical_edge_type: USES_FORMULA_TEMPLATE
    inverse_edge_type: USED_BY_IMPLEMENTATION
    materialize_inverse: false
    edge_class: canonical
    source_type: metric_implementation
    target_type: formula_template
```
```yaml
candidate_edge:
  edge_id: edge.metric.average_freight_per_awb.has_implementation.metric_impl.shiprocket_invoice.average_freight_per_awb
  edge_type: HAS_IMPLEMENTATION
  source: metric.average_freight_per_awb
  target: metric_impl.shiprocket_invoice.average_freight_per_awb
  fields:
    edge_family: metric_understanding
    evidence_basis: metric_implementation.fields.metric_id
    confidence: high
    canonical_cognee_edge: true
    logistics_only: true
    canonical_edge_type: HAS_IMPLEMENTATION
    inverse_edge_type: IMPLEMENTS_METRIC
    materialize_inverse: true
    edge_class: canonical
    source_type: metric
    target_type: metric_implementation
```
```yaml
candidate_edge:
  edge_id: edge.metric_impl.shiprocket_invoice.average_freight_per_awb.implements_metric.metric.average_freight_per_awb
  edge_type: IMPLEMENTS_METRIC
  source: metric_impl.shiprocket_invoice.average_freight_per_awb
  target: metric.average_freight_per_awb
  fields:
    edge_family: metric_understanding
    evidence_basis: materialized inverse of HAS_IMPLEMENTATION
    confidence: high
    canonical_cognee_edge: true
    logistics_only: true
    canonical_edge_type: IMPLEMENTS_METRIC
    inverse_edge_type: HAS_IMPLEMENTATION
    materialize_inverse: true
    edge_class: canonical
    source_type: metric_implementation
    target_type: metric
    materialized_from: edge.metric.average_freight_per_awb.has_implementation.metric_impl.shiprocket_invoice.average_freight_per_awb
```
```yaml
candidate_edge:
  edge_id: edge.metric_impl.shiprocket_invoice.average_freight_per_awb.uses_table.table.zs_observe.shiprocket_invoice
  edge_type: USES_TABLE
  source: metric_impl.shiprocket_invoice.average_freight_per_awb
  target: table.zs_observe.shiprocket_invoice
  fields:
    edge_family: metric_understanding
    evidence_basis: metric_implementation.fields.base_tables
    confidence: high
    canonical_cognee_edge: true
    logistics_only: true
    canonical_edge_type: USES_TABLE
    inverse_edge_type: USED_BY_CONTEXT
    materialize_inverse: false
    edge_class: canonical
    source_type: metric_implementation
    target_type: table
```
```yaml
candidate_edge:
  edge_id: edge.metric_impl.shiprocket_invoice.average_freight_per_awb.uses_column.column.zs_observe.shiprocket_invoice.charged_amount.8737448c
  edge_type: USES_COLUMN
  source: metric_impl.shiprocket_invoice.average_freight_per_awb
  target: column.zs_observe.shiprocket_invoice.charged_amount
  fields:
    edge_family: metric_understanding
    evidence_basis: metric_implementation.fields.required_columns
    confidence: high
    canonical_cognee_edge: true
    logistics_only: true
    canonical_edge_type: USES_COLUMN
    inverse_edge_type: USED_BY_CONTEXT
    materialize_inverse: false
    edge_class: canonical
    source_type: metric_implementation
    target_type: column
    edge_properties:
      column_role: amount
```
```yaml
candidate_edge:
  edge_id: edge.metric_impl.shiprocket_invoice.average_freight_per_awb.uses_column.column.zs_observe.shiprocket_invoice.other_id.340e855f
  edge_type: USES_COLUMN
  source: metric_impl.shiprocket_invoice.average_freight_per_awb
  target: column.zs_observe.shiprocket_invoice.other_id
  fields:
    edge_family: metric_understanding
    evidence_basis: metric_implementation.fields.required_columns
    confidence: high
    canonical_cognee_edge: true
    logistics_only: true
    canonical_edge_type: USES_COLUMN
    inverse_edge_type: USED_BY_CONTEXT
    materialize_inverse: false
    edge_class: canonical
    source_type: metric_implementation
    target_type: column
    edge_properties:
      column_role: formula_component
```
```yaml
candidate_edge:
  edge_id: edge.metric_impl.shiprocket_invoice.average_freight_per_awb.uses_formula_template.formula_template.logistics.ratio_rate
  edge_type: USES_FORMULA_TEMPLATE
  source: metric_impl.shiprocket_invoice.average_freight_per_awb
  target: formula_template.logistics.ratio_rate
  fields:
    edge_family: metric_understanding
    evidence_basis: metric_implementation.fields.formula_template_id
    confidence: high
    canonical_cognee_edge: true
    logistics_only: true
    canonical_edge_type: USES_FORMULA_TEMPLATE
    inverse_edge_type: USED_BY_IMPLEMENTATION
    materialize_inverse: false
    edge_class: canonical
    source_type: metric_implementation
    target_type: formula_template
```
```yaml
candidate_edge:
  edge_id: edge.metric.cod_collected_amount.has_implementation.metric_impl.shiprocket_settlement.cod_collected_amount
  edge_type: HAS_IMPLEMENTATION
  source: metric.cod_collected_amount
  target: metric_impl.shiprocket_settlement.cod_collected_amount
  fields:
    edge_family: metric_understanding
    evidence_basis: metric_implementation.fields.metric_id
    confidence: high
    canonical_cognee_edge: true
    logistics_only: true
    canonical_edge_type: HAS_IMPLEMENTATION
    inverse_edge_type: IMPLEMENTS_METRIC
    materialize_inverse: true
    edge_class: canonical
    source_type: metric
    target_type: metric_implementation
```
```yaml
candidate_edge:
  edge_id: edge.metric_impl.shiprocket_settlement.cod_collected_amount.implements_metric.metric.cod_collected_amount
  edge_type: IMPLEMENTS_METRIC
  source: metric_impl.shiprocket_settlement.cod_collected_amount
  target: metric.cod_collected_amount
  fields:
    edge_family: metric_understanding
    evidence_basis: materialized inverse of HAS_IMPLEMENTATION
    confidence: high
    canonical_cognee_edge: true
    logistics_only: true
    canonical_edge_type: IMPLEMENTS_METRIC
    inverse_edge_type: HAS_IMPLEMENTATION
    materialize_inverse: true
    edge_class: canonical
    source_type: metric_implementation
    target_type: metric
    materialized_from: edge.metric.cod_collected_amount.has_implementation.metric_impl.shiprocket_settlement.cod_collected_amount
```
```yaml
candidate_edge:
  edge_id: edge.metric_impl.shiprocket_settlement.cod_collected_amount.uses_table.table.zs_observe.shiprocket_settlement
  edge_type: USES_TABLE
  source: metric_impl.shiprocket_settlement.cod_collected_amount
  target: table.zs_observe.shiprocket_settlement
  fields:
    edge_family: metric_understanding
    evidence_basis: metric_implementation.fields.base_tables
    confidence: high
    canonical_cognee_edge: true
    logistics_only: true
    canonical_edge_type: USES_TABLE
    inverse_edge_type: USED_BY_CONTEXT
    materialize_inverse: false
    edge_class: canonical
    source_type: metric_implementation
    target_type: table
```
```yaml
candidate_edge:
  edge_id: edge.metric_impl.shiprocket_settlement.cod_collected_amount.uses_column.column.zs_observe.shiprocket_settlement.charged_amount.8737448c
  edge_type: USES_COLUMN
  source: metric_impl.shiprocket_settlement.cod_collected_amount
  target: column.zs_observe.shiprocket_settlement.charged_amount
  fields:
    edge_family: metric_understanding
    evidence_basis: metric_implementation.fields.required_columns
    confidence: high
    canonical_cognee_edge: true
    logistics_only: true
    canonical_edge_type: USES_COLUMN
    inverse_edge_type: USED_BY_CONTEXT
    materialize_inverse: false
    edge_class: canonical
    source_type: metric_implementation
    target_type: column
    edge_properties:
      column_role: amount
```
```yaml
candidate_edge:
  edge_id: edge.metric.cod_remitted_amount.has_implementation.metric_impl.shiprocket_settlement.cod_remitted_amount
  edge_type: HAS_IMPLEMENTATION
  source: metric.cod_remitted_amount
  target: metric_impl.shiprocket_settlement.cod_remitted_amount
  fields:
    edge_family: metric_understanding
    evidence_basis: metric_implementation.fields.metric_id
    confidence: high
    canonical_cognee_edge: true
    logistics_only: true
    canonical_edge_type: HAS_IMPLEMENTATION
    inverse_edge_type: IMPLEMENTS_METRIC
    materialize_inverse: true
    edge_class: canonical
    source_type: metric
    target_type: metric_implementation
```
```yaml
candidate_edge:
  edge_id: edge.metric_impl.shiprocket_settlement.cod_remitted_amount.implements_metric.metric.cod_remitted_amount
  edge_type: IMPLEMENTS_METRIC
  source: metric_impl.shiprocket_settlement.cod_remitted_amount
  target: metric.cod_remitted_amount
  fields:
    edge_family: metric_understanding
    evidence_basis: materialized inverse of HAS_IMPLEMENTATION
    confidence: high
    canonical_cognee_edge: true
    logistics_only: true
    canonical_edge_type: IMPLEMENTS_METRIC
    inverse_edge_type: HAS_IMPLEMENTATION
    materialize_inverse: true
    edge_class: canonical
    source_type: metric_implementation
    target_type: metric
    materialized_from: edge.metric.cod_remitted_amount.has_implementation.metric_impl.shiprocket_settlement.cod_remitted_amount
```
```yaml
candidate_edge:
  edge_id: edge.metric_impl.shiprocket_settlement.cod_remitted_amount.uses_table.table.zs_observe.shiprocket_settlement
  edge_type: USES_TABLE
  source: metric_impl.shiprocket_settlement.cod_remitted_amount
  target: table.zs_observe.shiprocket_settlement
  fields:
    edge_family: metric_understanding
    evidence_basis: metric_implementation.fields.base_tables
    confidence: high
    canonical_cognee_edge: true
    logistics_only: true
    canonical_edge_type: USES_TABLE
    inverse_edge_type: USED_BY_CONTEXT
    materialize_inverse: false
    edge_class: canonical
    source_type: metric_implementation
    target_type: table
```
```yaml
candidate_edge:
  edge_id: edge.metric_impl.shiprocket_settlement.cod_remitted_amount.uses_column.column.zs_observe.shiprocket_settlement.charged_amount.8737448c
  edge_type: USES_COLUMN
  source: metric_impl.shiprocket_settlement.cod_remitted_amount
  target: column.zs_observe.shiprocket_settlement.charged_amount
  fields:
    edge_family: metric_understanding
    evidence_basis: metric_implementation.fields.required_columns
    confidence: high
    canonical_cognee_edge: true
    logistics_only: true
    canonical_edge_type: USES_COLUMN
    inverse_edge_type: USED_BY_CONTEXT
    materialize_inverse: false
    edge_class: canonical
    source_type: metric_implementation
    target_type: column
    edge_properties:
      column_role: amount
```
```yaml
candidate_edge:
  edge_id: edge.metric.cod_remittance_lag_days.has_implementation.metric_impl.shiprocket_settlement.cod_remittance_lag_days
  edge_type: HAS_IMPLEMENTATION
  source: metric.cod_remittance_lag_days
  target: metric_impl.shiprocket_settlement.cod_remittance_lag_days
  fields:
    edge_family: metric_understanding
    evidence_basis: metric_implementation.fields.metric_id
    confidence: high
    canonical_cognee_edge: true
    logistics_only: true
    canonical_edge_type: HAS_IMPLEMENTATION
    inverse_edge_type: IMPLEMENTS_METRIC
    materialize_inverse: true
    edge_class: canonical
    source_type: metric
    target_type: metric_implementation
```
```yaml
candidate_edge:
  edge_id: edge.metric_impl.shiprocket_settlement.cod_remittance_lag_days.implements_metric.metric.cod_remittance_lag_days
  edge_type: IMPLEMENTS_METRIC
  source: metric_impl.shiprocket_settlement.cod_remittance_lag_days
  target: metric.cod_remittance_lag_days
  fields:
    edge_family: metric_understanding
    evidence_basis: materialized inverse of HAS_IMPLEMENTATION
    confidence: high
    canonical_cognee_edge: true
    logistics_only: true
    canonical_edge_type: IMPLEMENTS_METRIC
    inverse_edge_type: HAS_IMPLEMENTATION
    materialize_inverse: true
    edge_class: canonical
    source_type: metric_implementation
    target_type: metric
    materialized_from: edge.metric.cod_remittance_lag_days.has_implementation.metric_impl.shiprocket_settlement.cod_remittance_lag_days
```
```yaml
candidate_edge:
  edge_id: edge.metric_impl.shiprocket_settlement.cod_remittance_lag_days.uses_table.table.zs_observe.shiprocket_settlement
  edge_type: USES_TABLE
  source: metric_impl.shiprocket_settlement.cod_remittance_lag_days
  target: table.zs_observe.shiprocket_settlement
  fields:
    edge_family: metric_understanding
    evidence_basis: metric_implementation.fields.base_tables
    confidence: high
    canonical_cognee_edge: true
    logistics_only: true
    canonical_edge_type: USES_TABLE
    inverse_edge_type: USED_BY_CONTEXT
    materialize_inverse: false
    edge_class: canonical
    source_type: metric_implementation
    target_type: table
```
```yaml
candidate_edge:
  edge_id: edge.metric_impl.shiprocket_settlement.cod_remittance_lag_days.uses_column.column.zs_observe.shiprocket_settlement.delivered_date.c5f42cea
  edge_type: USES_COLUMN
  source: metric_impl.shiprocket_settlement.cod_remittance_lag_days
  target: column.zs_observe.shiprocket_settlement.delivered_date
  fields:
    edge_family: metric_understanding
    evidence_basis: metric_implementation.fields.required_columns
    confidence: high
    canonical_cognee_edge: true
    logistics_only: true
    canonical_edge_type: USES_COLUMN
    inverse_edge_type: USED_BY_CONTEXT
    materialize_inverse: false
    edge_class: canonical
    source_type: metric_implementation
    target_type: column
    edge_properties:
      column_role: date
```
```yaml
candidate_edge:
  edge_id: edge.metric_impl.shiprocket_settlement.cod_remittance_lag_days.uses_column.column.zs_observe.shiprocket_settlement.settlement_date.c5f42cea
  edge_type: USES_COLUMN
  source: metric_impl.shiprocket_settlement.cod_remittance_lag_days
  target: column.zs_observe.shiprocket_settlement.settlement_date
  fields:
    edge_family: metric_understanding
    evidence_basis: metric_implementation.fields.required_columns
    confidence: high
    canonical_cognee_edge: true
    logistics_only: true
    canonical_edge_type: USES_COLUMN
    inverse_edge_type: USED_BY_CONTEXT
    materialize_inverse: false
    edge_class: canonical
    source_type: metric_implementation
    target_type: column
    edge_properties:
      column_role: date
```
```yaml
candidate_edge:
  edge_id: edge.metric.unique_awb_count.has_implementation.metric_impl.shiprocket_settlement.unique_awb_count
  edge_type: HAS_IMPLEMENTATION
  source: metric.unique_awb_count
  target: metric_impl.shiprocket_settlement.unique_awb_count
  fields:
    edge_family: metric_understanding
    evidence_basis: metric_implementation.fields.metric_id
    confidence: high
    canonical_cognee_edge: true
    logistics_only: true
    canonical_edge_type: HAS_IMPLEMENTATION
    inverse_edge_type: IMPLEMENTS_METRIC
    materialize_inverse: true
    edge_class: canonical
    source_type: metric
    target_type: metric_implementation
```
```yaml
candidate_edge:
  edge_id: edge.metric_impl.shiprocket_settlement.unique_awb_count.implements_metric.metric.unique_awb_count
  edge_type: IMPLEMENTS_METRIC
  source: metric_impl.shiprocket_settlement.unique_awb_count
  target: metric.unique_awb_count
  fields:
    edge_family: metric_understanding
    evidence_basis: materialized inverse of HAS_IMPLEMENTATION
    confidence: high
    canonical_cognee_edge: true
    logistics_only: true
    canonical_edge_type: IMPLEMENTS_METRIC
    inverse_edge_type: HAS_IMPLEMENTATION
    materialize_inverse: true
    edge_class: canonical
    source_type: metric_implementation
    target_type: metric
    materialized_from: edge.metric.unique_awb_count.has_implementation.metric_impl.shiprocket_settlement.unique_awb_count
```
```yaml
candidate_edge:
  edge_id: edge.metric_impl.shiprocket_settlement.unique_awb_count.uses_table.table.zs_observe.shiprocket_settlement
  edge_type: USES_TABLE
  source: metric_impl.shiprocket_settlement.unique_awb_count
  target: table.zs_observe.shiprocket_settlement
  fields:
    edge_family: metric_understanding
    evidence_basis: metric_implementation.fields.base_tables
    confidence: high
    canonical_cognee_edge: true
    logistics_only: true
    canonical_edge_type: USES_TABLE
    inverse_edge_type: USED_BY_CONTEXT
    materialize_inverse: false
    edge_class: canonical
    source_type: metric_implementation
    target_type: table
```
```yaml
candidate_edge:
  edge_id: edge.metric_impl.shiprocket_settlement.unique_awb_count.uses_column.column.zs_observe.shiprocket_settlement.awb_number.9e2adfd1
  edge_type: USES_COLUMN
  source: metric_impl.shiprocket_settlement.unique_awb_count
  target: column.zs_observe.shiprocket_settlement.awb_number
  fields:
    edge_family: metric_understanding
    evidence_basis: metric_implementation.fields.required_columns
    confidence: high
    canonical_cognee_edge: true
    logistics_only: true
    canonical_edge_type: USES_COLUMN
    inverse_edge_type: USED_BY_CONTEXT
    materialize_inverse: false
    edge_class: canonical
    source_type: metric_implementation
    target_type: column
    edge_properties:
      column_role: key
```
```yaml
candidate_edge:
  edge_id: edge.metric.cod_remitted_amount.has_implementation.metric_impl.shiprocket_settlement_report.cod_remitted_amount.unsupported_until_loaded
  edge_type: HAS_IMPLEMENTATION
  source: metric.cod_remitted_amount
  target: metric_impl.shiprocket_settlement_report.cod_remitted_amount.unsupported_until_loaded
  fields:
    edge_family: metric_understanding
    evidence_basis: metric_implementation.fields.metric_id
    confidence: high
    canonical_cognee_edge: true
    logistics_only: true
    canonical_edge_type: HAS_IMPLEMENTATION
    inverse_edge_type: IMPLEMENTS_METRIC
    materialize_inverse: true
    edge_class: canonical
    source_type: metric
    target_type: metric_implementation
```
```yaml
candidate_edge:
  edge_id: edge.metric_impl.shiprocket_settlement_report.cod_remitted_amount.unsupported_until_loaded.implements_metric.metric.cod_remitted_amount
  edge_type: IMPLEMENTS_METRIC
  source: metric_impl.shiprocket_settlement_report.cod_remitted_amount.unsupported_until_loaded
  target: metric.cod_remitted_amount
  fields:
    edge_family: metric_understanding
    evidence_basis: materialized inverse of HAS_IMPLEMENTATION
    confidence: high
    canonical_cognee_edge: true
    logistics_only: true
    canonical_edge_type: IMPLEMENTS_METRIC
    inverse_edge_type: HAS_IMPLEMENTATION
    materialize_inverse: true
    edge_class: canonical
    source_type: metric_implementation
    target_type: metric
    materialized_from: edge.metric.cod_remitted_amount.has_implementation.metric_impl.shiprocket_settlement_report.cod_remitted_amount.unsupported_until_loaded
```
```yaml
candidate_edge:
  edge_id: edge.metric_impl.shiprocket_settlement_report.cod_remitted_amount.unsupported_until_loaded.uses_table.table.zs_observe.shiprocket_settlement_report
  edge_type: USES_TABLE
  source: metric_impl.shiprocket_settlement_report.cod_remitted_amount.unsupported_until_loaded
  target: table.zs_observe.shiprocket_settlement_report
  fields:
    edge_family: metric_understanding
    evidence_basis: metric_implementation.fields.base_tables
    confidence: high
    canonical_cognee_edge: true
    logistics_only: true
    canonical_edge_type: USES_TABLE
    inverse_edge_type: USED_BY_CONTEXT
    materialize_inverse: false
    edge_class: canonical
    source_type: metric_implementation
    target_type: table
```
```yaml
candidate_edge:
  edge_id: edge.metric_impl.shiprocket_settlement_report.cod_remitted_amount.unsupported_until_loaded.uses_column.column.zs_observe.shiprocket_settlement_report.settlement_id.340e855f
  edge_type: USES_COLUMN
  source: metric_impl.shiprocket_settlement_report.cod_remitted_amount.unsupported_until_loaded
  target: column.zs_observe.shiprocket_settlement_report.settlement_id
  fields:
    edge_family: metric_understanding
    evidence_basis: metric_implementation.fields.required_columns
    confidence: high
    canonical_cognee_edge: true
    logistics_only: true
    canonical_edge_type: USES_COLUMN
    inverse_edge_type: USED_BY_CONTEXT
    materialize_inverse: false
    edge_class: canonical
    source_type: metric_implementation
    target_type: column
    edge_properties:
      column_role: formula_component
```
```yaml
candidate_edge:
  edge_id: edge.metric.batch_settlement_amount.has_implementation.metric_impl.shiprocket_settlement_report.batch_settlement_amount.unsupported_until_loaded
  edge_type: HAS_IMPLEMENTATION
  source: metric.batch_settlement_amount
  target: metric_impl.shiprocket_settlement_report.batch_settlement_amount.unsupported_until_loaded
  fields:
    edge_family: metric_understanding
    evidence_basis: metric_implementation.fields.metric_id
    confidence: high
    canonical_cognee_edge: true
    logistics_only: true
    canonical_edge_type: HAS_IMPLEMENTATION
    inverse_edge_type: IMPLEMENTS_METRIC
    materialize_inverse: true
    edge_class: canonical
    source_type: metric
    target_type: metric_implementation
```
```yaml
candidate_edge:
  edge_id: edge.metric_impl.shiprocket_settlement_report.batch_settlement_amount.unsupported_until_loaded.implements_metric.metric.batch_settlement_amount
  edge_type: IMPLEMENTS_METRIC
  source: metric_impl.shiprocket_settlement_report.batch_settlement_amount.unsupported_until_loaded
  target: metric.batch_settlement_amount
  fields:
    edge_family: metric_understanding
    evidence_basis: materialized inverse of HAS_IMPLEMENTATION
    confidence: high
    canonical_cognee_edge: true
    logistics_only: true
    canonical_edge_type: IMPLEMENTS_METRIC
    inverse_edge_type: HAS_IMPLEMENTATION
    materialize_inverse: true
    edge_class: canonical
    source_type: metric_implementation
    target_type: metric
    materialized_from: edge.metric.batch_settlement_amount.has_implementation.metric_impl.shiprocket_settlement_report.batch_settlement_amount.unsupported_until_loaded
```
```yaml
candidate_edge:
  edge_id: edge.metric_impl.shiprocket_settlement_report.batch_settlement_amount.unsupported_until_loaded.uses_table.table.zs_observe.shiprocket_settlement_report
  edge_type: USES_TABLE
  source: metric_impl.shiprocket_settlement_report.batch_settlement_amount.unsupported_until_loaded
  target: table.zs_observe.shiprocket_settlement_report
  fields:
    edge_family: metric_understanding
    evidence_basis: metric_implementation.fields.base_tables
    confidence: high
    canonical_cognee_edge: true
    logistics_only: true
    canonical_edge_type: USES_TABLE
    inverse_edge_type: USED_BY_CONTEXT
    materialize_inverse: false
    edge_class: canonical
    source_type: metric_implementation
    target_type: table
```
```yaml
candidate_edge:
  edge_id: edge.metric_impl.shiprocket_settlement_report.batch_settlement_amount.unsupported_until_loaded.uses_column.column.zs_observe.shiprocket_settlement_report.settlement_id.340e855f
  edge_type: USES_COLUMN
  source: metric_impl.shiprocket_settlement_report.batch_settlement_amount.unsupported_until_loaded
  target: column.zs_observe.shiprocket_settlement_report.settlement_id
  fields:
    edge_family: metric_understanding
    evidence_basis: metric_implementation.fields.required_columns
    confidence: high
    canonical_cognee_edge: true
    logistics_only: true
    canonical_edge_type: USES_COLUMN
    inverse_edge_type: USED_BY_CONTEXT
    materialize_inverse: false
    edge_class: canonical
    source_type: metric_implementation
    target_type: column
    edge_properties:
      column_role: formula_component
```

## 6. Validation Summary
```yaml
validation_summary:
  document_id: shiprocket_services_aggregator_parser_ready_v6_role_split
  shiprocket_role_split: services_aggregator
  candidate_cards: 90
  candidate_edges: 251
  candidate_cards_by_type:
    column: 40
    metric: 15
    metric_implementation: 16
    platform: 1
    platform_context: 1
    relationship: 8
    table: 3
    value_profile: 6
  candidate_edges_by_type:
    APPLIES_TO_PLATFORM: 3
    BELONGS_TO_DOMAIN: 15
    BELONGS_TO_PLATFORM: 1
    BELONGS_TO_TABLE: 40
    HAS_COLUMN: 40
    HAS_IMPLEMENTATION: 16
    HAS_PLATFORM_CONTEXT: 1
    HAS_RELATIONSHIP: 16
    HAS_VALUE_PROFILE: 12
    IMPLEMENTS_METRIC: 16
    PROFILES_COLUMN: 6
    PROFILES_TABLE: 6
    SOURCED_FROM_PLATFORM: 3
    SOURCE_TABLE: 8
    TARGET_TABLE: 8
    USES_COLUMN: 18
    USES_FORMULA_TEMPLATE: 10
    USES_SOURCE_COLUMN: 8
    USES_TABLE: 16
    USES_TARGET_COLUMN: 8
  forbidden_card_types_present: []
  unknown_edge_types_present: []
  result: pass
```
