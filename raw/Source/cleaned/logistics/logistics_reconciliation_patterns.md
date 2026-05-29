# Logistics Reconciliation Patterns — Parser Ready v6 Role-Split Manifest-Aligned Unified Edges
## 0. Document Metadata
```yaml
document_metadata:
  document_id: logistics_reconciliation_patterns_parser_ready_v6_role_split
  title: Logistics Reconciliation Patterns — Parser Ready v6 Role-Split Manifest-Aligned Unified Edges
  domain: logistics
  vendor: shared_logistics
  source_docx: /mnt/data/Logistics KB Doc.docx
  frame_of_reference: logistics_gold_std_canonical_card_frame_v5 plus flipkart_v8_unified_edges_style plus marketplace_cleanup_manifest_consolidated_v2
  generated_on: '2026-05-24'
  version: 6.0-role-split-manifest-aligned-unified-edges
  scope: logistics_reconciliation_patterns_with_unified_edges
  logistics_only: true
  allowed_card_types:
  - column
  - execution_constraint_set
  - matching_logic
  - mismatch_category
  - output_contract
  - query_pattern
  - reconciliation_profile
  - reconciliation_side
  - reconciliation_unit
  - reconciliation_variant
  - relationship
  - rule
  - table
  - validation_test
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

## 0.1 V6 Refactor Notes — Manifest-Aligned Deterministic Ingestion

```yaml
v6_refactor_notes:
  refactor_basis:
  - Logistics KB Doc.docx as source-of-truth evidence
  - marketplace_cleanup_manifest_consolidated_v2.md as cleanup/review gate source
  - canonical_edge_taxonomy_registry.md as allowed edge universe
  - v4 unified-edge logistics markdowns as structural base
  refactor_goal: preserve manifest-aligned deterministic ingestion while splitting Shiprocket into role-specific logistics-partner and services-aggregator documents.
  semantic_change_policy: no unsupported tenant/group/account binding is introduced in generic logistics files.
  parser_contract:
  - candidate_card and candidate_edge blocks remain the primary ingestible units
  - review_item and manifest_gate blocks are parser governance objects, not canonical domain cards unless the ingestion pipeline explicitly supports review cards
  - candidate cards are deduped by card_id; repeated metric cards remain readability duplicates
```


## 0. Parser Instructions

This document is intended to be parsed deterministically. It is not prose-only. The parser should emit `candidate_card` blocks and `candidate_edge` blocks, normalize legacy aliases into the canonical uppercase edge taxonomy, and dedupe repeated cards by `card_id`.

Critical parser rules:

- Create only logistics-scoped reusable cards from this document.
- Do not create tenant, group, platform account, account data binding, business scope set, or business flow binding cards from generic vendor/domain documents.
- Treat scope-like fields such as `group_level_id`, `group_id`, `merchant_id`, `bank_name`, and similar values as columns/caveats only.
- Metric cards own colloquial/business meaning; metric implementation cards own platform/table-specific formulas.
- Process cards must be operational: each workflow step and state transition should identify evidence, expected state, lag/failure logic, or a review item.
- Materialize inverse edges only when `materialize_inverse: true`; otherwise use graph reverse indexes.
- Do not invent domain-specific route-binding edges. Use Business Flow Binding only in separate business-flow applicability docs.

## 1. Source Intake and Evidence Registry

```yaml
source_evidence:
  id: evidence.logistics_kb_doc
  source_document: Logistics KB Doc.docx
  summary: Primary logistics/courier KB covering order flow, money flow, table statuses, join keys, vendor roles, amount semantics,
    and reconciliation hierarchy.
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
  summary: Canonical edge taxonomy, inverse edge policy, legacy edge aliases, and domain-specific use guidance for logistics/payment/bank/ERP
    docs.
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
  summary: Logistics domain authoring boundary, business flow binding handoff, amount semantics, table block structure, and
    logistics card scope.
  confidence: high
```

## 2. Out-of-Scope Registry

```yaml
out_of_scope_item:
  id: oos.logistics.tenant_group
  topic: Tenant/group/platform account/business flow cards
  instruction: Do not create tenant, group, platform_account, account_data_binding, business_scope_set, or business_flow_binding
    cards from generic logistics files. Use business flow applicability docs for that layer.
  allowed_as: source column, caveat, review item, or business-flow applicability input only
```
```yaml
out_of_scope_item:
  id: oos.logistics.account_filters
  topic: Account filters and group_level_id values
  instruction: Treat group_level_id, merchant_id, bank_name, and similar scope fields as source columns or caveats only unless
    a dedicated Account Data Binding doc is being authored.
  allowed_as: source column, caveat, review item, or business-flow applicability input only
```
```yaml
out_of_scope_item:
  id: oos.logistics.bank_statement_execution
  topic: Bank statement execution
  instruction: Generic logistics docs can expose UTR and bank-reference bridge fields, but actual bank account selection and
    bank statement matching require Banking KB plus Business Flow Binding.
  allowed_as: source column, caveat, review item, or business-flow applicability input only
```
```yaml
out_of_scope_item:
  id: oos.logistics.unsupported_native_tables
  topic: Unsupported native courier tables
  instruction: Do not create fake native table evidence for Shadowfax or Ecom Express; use indirect/fallback evidence only
    where documented.
  allowed_as: source column, caveat, review item, or business-flow applicability input only
```

## 3. Compact Semantic Field Contract

| card family | required semantic intent |
|---|---|
| `platform/platform_context` | platform identity, region/context, platform_type, source codes, evidence refs |
| `table/column/value_profile` | grain, amount semantics, join/filter roles, coverage status, known values, caveats |
| `relationship` | source/target table, join keys, cardinality, safe usage, aggregation risk |
| `metric/metric_implementation` | colloquial metric meaning vs vendor/table formula, metric_pattern, required columns, filters, allowed grains |
| `business_process/workflow_step/state_transition/process_variant` | lifecycle, evidence-bearing checkpoint, from/to state, lag/failure logic, operating-model variant |
| `reconciliation cards` | profile, expected/actual sides, unit, matching logic, mismatch category, variants |
| `execution guidance` | query pattern, rule, validation test, output contract, constraint set |


## Manifest Layer A — Evidence Anchor Manifests

These anchors convert broad source references into exact source sections. A deterministic parser should resolve every `candidate_card.fields.evidence_refs` entry to one or more of these anchor IDs using the resolution rules below. Do not infer semantics outside the `supported_semantics` list.

```yaml
evidence_anchor_manifest:
  source_evidence_id: ev.logistics.order_flow.high_level_order_flow
  source_document: Logistics KB Doc.docx
  source_section: Logistics & Courier Knowledge Base — Order Flow Overview / 1. High-Level Order Flow
  evidence_type: prose
  supported_semantics:
  - order-to-shipment lifecycle
  - marketplace/channel handoff into warehouse and courier routing
  - Shiprocket as non-FBF courier aggregator
  - Ekart as FBF courier/fulfilment evidence
  - Shadowfax reverse-only and Ecom Express no-separate-table coverage notes
  unsupported_semantics:
  - tenant/group-specific route binding
  - bank account destination selection
  - executable metric formulas without table sections
  allowed_card_types:
  - business_process
  - workflow_step
  - state_transition
  - process_variant
  - platform
  - platform_context
  - rule
  forbidden_card_types:
  - tenant
  - group
  - platform_account
  - account_data_binding
  - business_flow_binding
  confidence_policy:
    explicit_table_or_formula: high
    inferred_from_prose: medium
    absent_or_ambiguous: review_required
```

```yaml
evidence_anchor_manifest:
  source_evidence_id: ev.logistics.money_flow.cod_order_settlement_chain
  source_document: Logistics KB Doc.docx
  source_section: Logistics & Courier Knowledge Base — Order Flow Overview / 2. Money Flows / 2a. COD Order Settlement Chain
  evidence_type: prose
  supported_semantics:
  - COD collection by courier on delivery
  - 7-14 day default courier remittance lag
  - courier-level COD settlement tables
  - Shiprocket settlement as aggregator COD settlement evidence
  unsupported_semantics:
  - guaranteed bank credit without banking evidence
  - COD formula from a table unless table-specific columns are documented
  allowed_card_types:
  - business_process
  - workflow_step
  - state_transition
  - metric
  - reconciliation_profile
  - reconciliation_side
  - matching_logic
  - mismatch_category
  - query_pattern
  - rule
```

```yaml
evidence_anchor_manifest:
  source_evidence_id: ev.logistics.money_flow.freight_invoice_chain
  source_document: Logistics KB Doc.docx
  source_section: Logistics & Courier Knowledge Base — Order Flow Overview / 2. Money Flows / 2b. Freight Invoice Chain
  evidence_type: prose
  supported_semantics:
  - courier freight charged per AWB
  - Shiprocket consolidated freight invoice role
  - Delhivery direct freight invoice role
  - DTDC and Ekart invoice tables being empty
  unsupported_semantics:
  - table-specific freight amount formula unless key fields or freight formula section supports it
  - use of empty invoice tables as evidence
  allowed_card_types:
  - business_process
  - workflow_step
  - state_transition
  - table
  - rule
  - query_pattern
  - validation_test
```

```yaml
evidence_anchor_manifest:
  source_evidence_id: ev.logistics.money_flow.prepaid_pos_settlement_chain
  source_document: Logistics KB Doc.docx
  source_section: Logistics & Courier Knowledge Base — Order Flow Overview / 2. Money Flows / 2c. Prepaid Digital Settlement Chain
  evidence_type: prose
  supported_semantics:
  - prepaid settlement is primarily payment-gateway/marketplace owned
  - Ekart settlement can represent FBF POS settlement
  unsupported_semantics:
  - logistics-native bank settlement for all prepaid orders
  - payment-gateway card creation from logistics docs
  allowed_card_types:
  - business_process
  - process_variant
  - metric
  - metric_implementation
  - reconciliation_profile
  - rule
```

```yaml
evidence_anchor_manifest:
  source_evidence_id: ev.logistics.scope.group_level_ids
  source_document: Logistics KB Doc.docx
  source_section: Logistics & Courier Knowledge Base — Order Flow Overview / 3. Group Level IDs in Logistics Domain
  evidence_type: table
  supported_semantics:
  - observed table-level group/account scope fields
  - Account Data Binding input candidates
  unsupported_semantics:
  - direct creation of tenant/group/platform_account cards from generic logistics docs
  - universal group_level_id filters across logistics tables
  allowed_card_types:
  - column
  - rule
  - validation_test
  - review_item
  forbidden_card_types:
  - tenant
  - group
  - platform_account
  - account_data_binding
  - business_scope_set
  - business_flow_binding
```

```yaml
evidence_anchor_manifest:
  source_evidence_id: ev.logistics.fulfilment.fbf_non_fbf
  source_document: Logistics KB Doc.docx
  source_section: Logistics & Courier Knowledge Base — Order Flow Overview / 4. FBF vs Non-FBF Distinction
  evidence_type: table
  supported_semantics:
  - platform_fulfilled vs aggregator_routed operating models
  - Ekart FBF settlement evidence
  - Shiprocket/Delhivery/DTDC/XpressBees non-FBF evidence families
  unsupported_semantics:
  - process variant creation from label alone without operational difference
  - tenant/group-specific route choice
  allowed_card_types:
  - process_variant
  - value_profile
  - rule
  - query_pattern
```

```yaml
evidence_anchor_manifest:
  source_evidence_id: ev.logistics.courier_partner_summary
  source_document: Logistics KB Doc.docx
  source_section: Logistics & Courier Knowledge Base — Order Flow Overview / 5. Courier Partner Summary
  evidence_type: table
  supported_semantics:
  - vendor/platform role
  - data table coverage by courier
  - direct vs indirect vs reverse-only vendor coverage
  unsupported_semantics:
  - fake native tables for vendors documented as indirect/no-table
  - reliable native source for sparse/partial vendors without validation
  allowed_card_types:
  - platform
  - platform_context
  - table
  - metric_implementation
  - rule
  - validation_test
```

```yaml
evidence_anchor_manifest:
  source_evidence_id: ev.logistics.join_keys.cross_table_join_map
  source_document: Logistics KB Doc.docx
  source_section: Logistics & Courier Knowledge Base — Order Flow Overview / 6. Key Join Keys Across Tables
  evidence_type: reconciliation_playbook
  supported_semantics:
  - Shopify order to Shiprocket composite order parsing
  - AWB/waybill/tracking relationships across logistics tables
  - safe relationship card creation with pre-aggregation caveats
  unsupported_semantics:
  - direct bank matching without batch/UTR evidence
  - metric aggregation safety without grain rules
  allowed_card_types:
  - relationship
  - reconciliation_unit
  - matching_logic
  - query_pattern
  - rule
```

```yaml
evidence_anchor_manifest:
  source_evidence_id: ev.logistics.table_status.summary
  source_document: Logistics KB Doc.docx
  source_section: Logistics & Courier Knowledge Base — Order Flow Overview / 7. Table Status Summary
  evidence_type: table
  supported_semantics:
  - table row counts and coverage status
  - active, partial, empty, and schema-only classifications
  - observed group IDs as scope-column observations
  unsupported_semantics:
  - account binding creation from row count table
  - use of empty table as analytical evidence
  allowed_card_types:
  - table
  - rule
  - validation_test
  - review_item
```

```yaml
evidence_anchor_manifest:
  source_evidence_id: ev.logistics.reconciliation.hierarchy
  source_document: Logistics KB Doc.docx
  source_section: Logistics & Courier Knowledge Base — Order Flow Overview / 8. Reconciliation Hierarchy
  evidence_type: reconciliation_playbook
  supported_semantics:
  - order, shipment, financial, and batch settlement reconciliation levels
  - expected-vs-actual matching paths
  - AWB-level and batch-level grain separation
  unsupported_semantics:
  - tenant-specific bank account selection
  - direct AWB-to-bank comparison without aggregation
  allowed_card_types:
  - reconciliation_profile
  - reconciliation_side
  - reconciliation_unit
  - matching_logic
  - mismatch_category
  - query_pattern
  - rule
  - validation_test
```
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


## Manifest Layer C — Reconciliation Manifest Enforcement

```yaml
process_reconciliation_manifest:
  logistics_reconciliation_profiles:
    order_to_shipment:
      expected_side: marketplace/channel order evidence
      actual_side: logistics shipment/AWB evidence
      primary_unit: order_id then AWB
      source_anchor: ev.logistics.reconciliation.hierarchy
    shipment_to_freight_invoice:
      expected_side: dispatched shipment/AWB evidence
      actual_side: freight invoice evidence
      primary_unit: AWB/waybill/tracking ID
      source_anchor: ev.logistics.reconciliation.hierarchy
    freight_charge_validation:
      expected_side: shipment/courier/zone/weight context
      actual_side: freight charge components
      primary_unit: AWB plus charge components
      source_anchor: ev.logistics.reconciliation.hierarchy
    cod_expected_to_courier_remittance:
      expected_side: delivered COD shipment expected amount
      actual_side: courier/aggregator COD remittance
      primary_unit: AWB, with batch fallback only after aggregation
      source_anchor: ev.logistics.money_flow.cod_order_settlement_chain
    courier_batch_to_bank_credit:
      expected_side: courier settlement batch, UTR, or bank reference
      actual_side: bank statement credit
      primary_unit: batch/UTR/bank_reference, not AWB
      source_anchor: ev.logistics.reconciliation.hierarchy
  fail_if:
  - side_role_missing_or_swapped
  - AWB_level_data_is_joined_directly_to_bank_credit_without_batch_aggregation
  - bank_statement_placeholder_is_treated_as fully owned logistics schema
```

```yaml
matching_logic_manifest:
  required_matching_properties:
  - primary_key_or_unit
  - fallback_key_or_unit_when_available
  - date_window_or_lag_basis
  - amount_comparison_basis
  - pre_aggregation_rule
  - failure_modes
  logistics_grain_policy:
    order_to_shipment: order_id_to_AWB
    shipment_to_freight_invoice: AWB_to_invoice_line
    cod_expected_to_courier_remittance: delivered_COD_AWB_to_settlement_AWB
    courier_batch_to_bank_credit: settlement_batch_or_UTR_to_bank_credit
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


## 4. Candidate Cards

### 4.4 table cards

```yaml
candidate_card:
  card_type: table
  card_id: table.zs_observe.bank_statement
  name: Bank Statement Placeholder
  fields:
    name: Bank Statement Placeholder
    description: Generic bank statement evidence table placeholder for logistics-to-bank bridge patterns; actual banking KB
      owns detailed semantics.
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
    table_name: bank_statement
    full_reference: zs_observe.bank_statement
    table_type: bank_ledger
    source_platform_types:
    - banking
    business_purpose: Actual bank credit evidence for courier remittance reconciliation
    grain: one bank transaction row
    grain_keys:
    - bank_transaction_id
    - utr_no
    - bank_reference_no
    coverage_status: external_to_logistics_kb
    evidence_refs:
    - evidence.logistics_kb_doc
    - evidence.cognee_design_v4
    - evidence.unified_edge_scope
```

### 4.5 column cards

```yaml
candidate_card:
  card_type: column
  card_id: column.zs_observe.bank_statement.utr_no
  name: bank_statement.utr_no
  fields:
    name: bank_statement.utr_no
    description: Bank UTR/reference.
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
    table_id: table.zs_observe.bank_statement
    column_name: utr_no
    data_type: unknown
    semantic_roles: identifier;bank_bridge
    business_concepts:
    - Bank UTR/reference.
    default_aggregation: SUM if credit_amount else none
    sign_convention: positive for credits
    amount_semantics: not_applicable
    usable_for_filtering: true
    usable_for_grouping: true
    usable_for_metrics: false
    usable_for_joining: true
    evidence_refs:
    - evidence.logistics_kb_doc
    - evidence.cognee_design_v4
    - evidence.unified_edge_scope
```

```yaml
candidate_card:
  card_type: column
  card_id: column.zs_observe.bank_statement.bank_reference_no
  name: bank_statement.bank_reference_no
  fields:
    name: bank_statement.bank_reference_no
    description: Bank reference number.
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
    table_id: table.zs_observe.bank_statement
    column_name: bank_reference_no
    data_type: unknown
    semantic_roles: identifier;bank_bridge
    business_concepts:
    - Bank reference number.
    default_aggregation: SUM if credit_amount else none
    sign_convention: positive for credits
    amount_semantics: not_applicable
    usable_for_filtering: true
    usable_for_grouping: true
    usable_for_metrics: false
    usable_for_joining: true
    evidence_refs:
    - evidence.logistics_kb_doc
    - evidence.cognee_design_v4
    - evidence.unified_edge_scope
```

```yaml
candidate_card:
  card_type: column
  card_id: column.zs_observe.bank_statement.credit_amount
  name: bank_statement.credit_amount
  fields:
    name: bank_statement.credit_amount
    description: Credit amount received.
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
    table_id: table.zs_observe.bank_statement
    column_name: credit_amount
    data_type: unknown
    semantic_roles: measure
    business_concepts:
    - Credit amount received.
    default_aggregation: SUM if credit_amount else none
    sign_convention: positive for credits
    amount_semantics: bank_credit_amount
    usable_for_filtering: true
    usable_for_grouping: true
    usable_for_metrics: true
    usable_for_joining: true
    evidence_refs:
    - evidence.logistics_kb_doc
    - evidence.cognee_design_v4
    - evidence.unified_edge_scope
```

```yaml
candidate_card:
  card_type: column
  card_id: column.zs_observe.bank_statement.transaction_date
  name: bank_statement.transaction_date
  fields:
    name: bank_statement.transaction_date
    description: Bank transaction date.
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
    table_id: table.zs_observe.bank_statement
    column_name: transaction_date
    data_type: unknown
    semantic_roles: date
    business_concepts:
    - Bank transaction date.
    default_aggregation: SUM if credit_amount else none
    sign_convention: positive for credits
    amount_semantics: not_applicable
    usable_for_filtering: true
    usable_for_grouping: true
    usable_for_metrics: false
    usable_for_joining: true
    evidence_refs:
    - evidence.logistics_kb_doc
    - evidence.cognee_design_v4
    - evidence.unified_edge_scope
```

```yaml
candidate_card:
  card_type: column
  card_id: column.zs_observe.bank_statement.bank_account_id
  name: bank_statement.bank_account_id
  fields:
    name: bank_statement.bank_account_id
    description: Bank account scope key resolved by Account Data Binding.
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
    table_id: table.zs_observe.bank_statement
    column_name: bank_account_id
    data_type: unknown
    semantic_roles: scope_filter
    business_concepts:
    - Bank account scope key resolved by Account Data Binding.
    default_aggregation: SUM if credit_amount else none
    sign_convention: positive for credits
    amount_semantics: not_applicable
    usable_for_filtering: true
    usable_for_grouping: true
    usable_for_metrics: false
    usable_for_joining: true
    evidence_refs:
    - evidence.logistics_kb_doc
    - evidence.cognee_design_v4
    - evidence.unified_edge_scope
```

### 4.6 relationship cards

```yaml
candidate_card:
  card_type: relationship
  card_id: relationship.dtdc_settlement.bank_statement.utr
  name: dtdc_settlement to bank_statement by utr
  fields:
    name: dtdc_settlement to bank_statement by utr
    description: Bridge DTDC COD remittance to bank statement by UTR.
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
    source_table: table.zs_observe.dtdc_settlement
    target_table: table.zs_observe.bank_statement
    relationship_type: join; reconciliation_relation
    join_keys: utr_no = utr_no
    cardinality: one_to_zero_or_many
    join_type_recommendation: left_join for diagnostics; inner_join for matched-only analysis
    business_use: Bridge DTDC COD remittance to bank statement by UTR.
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
  card_id: relationship.dtdc_settlement.bank_statement.bank_ref
  name: dtdc_settlement to bank_statement by bank_ref
  fields:
    name: dtdc_settlement to bank_statement by bank_ref
    description: Bridge DTDC COD remittance to bank by bank reference.
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
    source_table: table.zs_observe.dtdc_settlement
    target_table: table.zs_observe.bank_statement
    relationship_type: join; reconciliation_relation
    join_keys: bank_ref_number = bank_reference_no
    cardinality: one_to_zero_or_many
    join_type_recommendation: left_join for diagnostics; inner_join for matched-only analysis
    business_use: Bridge DTDC COD remittance to bank by bank reference.
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
  card_id: relationship.delhivery_settlement.bank_statement.utr
  name: delhivery_settlement to bank_statement by utr
  fields:
    name: delhivery_settlement to bank_statement by utr
    description: Bridge Delhivery COD remittance to bank statement by UTR.
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
    source_table: table.zs_observe.delhivery_settlement
    target_table: table.zs_observe.bank_statement
    relationship_type: join; reconciliation_relation
    join_keys: utr_no = utr_no
    cardinality: one_to_zero_or_many
    join_type_recommendation: left_join for diagnostics; inner_join for matched-only analysis
    business_use: Bridge Delhivery COD remittance to bank statement by UTR.
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
  card_id: relationship.ekart_settlement.bank_statement.bank_ref
  name: ekart_settlement to bank_statement by bank_ref
  fields:
    name: ekart_settlement to bank_statement by bank_ref
    description: Bridge Ekart settlement batch to bank reference.
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
    source_table: table.zs_observe.ekart_settlement
    target_table: table.zs_observe.bank_statement
    relationship_type: join; reconciliation_relation
    join_keys: bank_reference_no = bank_reference_no
    cardinality: one_to_zero_or_many
    join_type_recommendation: left_join for diagnostics; inner_join for matched-only analysis
    business_use: Bridge Ekart settlement batch to bank reference.
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
  card_id: relationship.shiprocket_oms.bank_statement.utr
  name: shiprocket_oms to bank_statement by utr
  fields:
    name: shiprocket_oms to bank_statement by utr
    description: Bridge Shiprocket OMS remittance UTR to bank statement where populated.
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
    target_table: table.zs_observe.bank_statement
    relationship_type: join; reconciliation_relation
    join_keys: utr_no = utr_no
    cardinality: one_to_zero_or_many
    join_type_recommendation: left_join for diagnostics; inner_join for matched-only analysis
    business_use: Bridge Shiprocket OMS remittance UTR to bank statement where populated.
    safe_for_metrics: false unless pre-aggregated
    safe_for_reconciliation: true
    aggregation_risk: pre-aggregate to reconciliation unit before joining; avoid fanout
    evidence_refs:
    - evidence.logistics_kb_doc
    - evidence.cognee_design_v4
    - evidence.unified_edge_scope
```

### 4.16 reconciliation_profile cards

```yaml
candidate_card:
  card_type: reconciliation_profile
  card_id: reconciliation_profile.order_to_shipment
  name: Order to Shipment Reconciliation
  fields:
    name: Order to Shipment Reconciliation
    description: Reusable reconciliation profile for Order to Shipment Reconciliation.
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
    profile_name: Order to Shipment Reconciliation
    business_process_id: business_process.order_to_shipment_flow
    reconciliation_type: order_to_shipment
    participating_platform_types:
    - marketplace
    - logistics
    - courier
    - banking by profile
    reconciliation_sides: reconciliation_side.order_to_shipment.expected; reconciliation_side.order_to_shipment.actual
    business_object: order/shipment/awb/settlement/bank_credit
    primary_reconciliation_unit_id: reconciliation_unit.order_to_shipment.primary
    secondary_reconciliation_unit_ids: reconciliation_unit.order_to_shipment.fallback
    expected_alignment_type: one_to_one or aggregated by profile
    matching_logic_id: matching_logic.order_to_shipment
    mismatch_categories:
    - mismatch_category.order_to_shipment.missing_expected
    - mismatch_category.order_to_shipment.missing_actual
    - mismatch_category.order_to_shipment.amount_mismatch
    - mismatch_category.order_to_shipment.timing_mismatch
    applicability_scope: platform_type=logistics; tenant/group participation via Business Flow Binding
    evidence_refs:
    - evidence.logistics_kb_doc
    - evidence.cognee_design_v4
    - evidence.unified_edge_scope
    supports_process_note: Profile is reusable; tenant/group-specific account participation is supplied by Business Flow Binding.
```

```yaml
candidate_card:
  card_type: reconciliation_profile
  card_id: reconciliation_profile.shipment_to_freight_invoice
  name: Shipment to Freight Invoice Reconciliation
  fields:
    name: Shipment to Freight Invoice Reconciliation
    description: Reusable reconciliation profile for Shipment to Freight Invoice Reconciliation.
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
    profile_name: Shipment to Freight Invoice Reconciliation
    business_process_id: business_process.shipment_to_freight_invoice
    reconciliation_type: shipment_to_invoice
    participating_platform_types:
    - marketplace
    - logistics
    - courier
    - banking by profile
    reconciliation_sides: reconciliation_side.shipment_to_freight_invoice.expected; reconciliation_side.shipment_to_freight_invoice.actual
    business_object: order/shipment/awb/settlement/bank_credit
    primary_reconciliation_unit_id: reconciliation_unit.shipment_to_freight_invoice.primary
    secondary_reconciliation_unit_ids: reconciliation_unit.shipment_to_freight_invoice.fallback
    expected_alignment_type: one_to_one or aggregated by profile
    matching_logic_id: matching_logic.shipment_to_freight_invoice
    mismatch_categories:
    - mismatch_category.shipment_to_freight_invoice.missing_expected
    - mismatch_category.shipment_to_freight_invoice.missing_actual
    - mismatch_category.shipment_to_freight_invoice.amount_mismatch
    - mismatch_category.shipment_to_freight_invoice.timing_mismatch
    applicability_scope: platform_type=logistics; tenant/group participation via Business Flow Binding
    evidence_refs:
    - evidence.logistics_kb_doc
    - evidence.cognee_design_v4
    - evidence.unified_edge_scope
    supports_process_note: Profile is reusable; tenant/group-specific account participation is supplied by Business Flow Binding.
```

```yaml
candidate_card:
  card_type: reconciliation_profile
  card_id: reconciliation_profile.freight_charge_validation
  name: Freight Charge Validation
  fields:
    name: Freight Charge Validation
    description: Reusable reconciliation profile for Freight Charge Validation.
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
    profile_name: Freight Charge Validation
    business_process_id: business_process.freight_charge_validation
    reconciliation_type: freight_charge
    participating_platform_types:
    - marketplace
    - logistics
    - courier
    - banking by profile
    reconciliation_sides: reconciliation_side.freight_charge_validation.expected; reconciliation_side.freight_charge_validation.actual
    business_object: order/shipment/awb/settlement/bank_credit
    primary_reconciliation_unit_id: reconciliation_unit.freight_charge_validation.primary
    secondary_reconciliation_unit_ids: reconciliation_unit.freight_charge_validation.fallback
    expected_alignment_type: one_to_one or aggregated by profile
    matching_logic_id: matching_logic.freight_charge_validation
    mismatch_categories:
    - mismatch_category.freight_charge_validation.missing_expected
    - mismatch_category.freight_charge_validation.missing_actual
    - mismatch_category.freight_charge_validation.amount_mismatch
    - mismatch_category.freight_charge_validation.timing_mismatch
    applicability_scope: platform_type=logistics; tenant/group participation via Business Flow Binding
    evidence_refs:
    - evidence.logistics_kb_doc
    - evidence.cognee_design_v4
    - evidence.unified_edge_scope
    supports_process_note: Profile is reusable; tenant/group-specific account participation is supplied by Business Flow Binding.
```

```yaml
candidate_card:
  card_type: reconciliation_profile
  card_id: reconciliation_profile.cod_expected_to_courier_remittance
  name: COD Expected to Courier Remittance Reconciliation
  fields:
    name: COD Expected to Courier Remittance Reconciliation
    description: Reusable reconciliation profile for COD Expected to Courier Remittance Reconciliation.
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
    profile_name: COD Expected to Courier Remittance Reconciliation
    business_process_id: business_process.cod_delivery_to_courier_remittance
    reconciliation_type: cod_reconciliation
    participating_platform_types:
    - marketplace
    - logistics
    - courier
    - banking by profile
    reconciliation_sides: reconciliation_side.cod_expected_to_courier_remittance.expected; reconciliation_side.cod_expected_to_courier_remittance.actual
    business_object: order/shipment/awb/settlement/bank_credit
    primary_reconciliation_unit_id: reconciliation_unit.cod_expected_to_courier_remittance.primary
    secondary_reconciliation_unit_ids: reconciliation_unit.cod_expected_to_courier_remittance.fallback
    expected_alignment_type: one_to_one or aggregated by profile
    matching_logic_id: matching_logic.cod_expected_to_courier_remittance
    mismatch_categories:
    - mismatch_category.cod_expected_to_courier_remittance.missing_expected
    - mismatch_category.cod_expected_to_courier_remittance.missing_actual
    - mismatch_category.cod_expected_to_courier_remittance.amount_mismatch
    - mismatch_category.cod_expected_to_courier_remittance.timing_mismatch
    applicability_scope: platform_type=logistics; tenant/group participation via Business Flow Binding
    evidence_refs:
    - evidence.logistics_kb_doc
    - evidence.cognee_design_v4
    - evidence.unified_edge_scope
    supports_process_note: Profile is reusable; tenant/group-specific account participation is supplied by Business Flow Binding.
```

```yaml
candidate_card:
  card_type: reconciliation_profile
  card_id: reconciliation_profile.courier_batch_to_bank_credit
  name: Courier Batch to Bank Credit Reconciliation
  fields:
    name: Courier Batch to Bank Credit Reconciliation
    description: Reusable reconciliation profile for Courier Batch to Bank Credit Reconciliation.
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
    profile_name: Courier Batch to Bank Credit Reconciliation
    business_process_id: business_process.courier_batch_to_bank_reconciliation
    reconciliation_type: settlement_to_bank
    participating_platform_types:
    - marketplace
    - logistics
    - courier
    - banking by profile
    reconciliation_sides: reconciliation_side.courier_batch_to_bank_credit.expected; reconciliation_side.courier_batch_to_bank_credit.actual
    business_object: order/shipment/awb/settlement/bank_credit
    primary_reconciliation_unit_id: reconciliation_unit.courier_batch_to_bank_credit.primary
    secondary_reconciliation_unit_ids: reconciliation_unit.courier_batch_to_bank_credit.fallback
    expected_alignment_type: one_to_one or aggregated by profile
    matching_logic_id: matching_logic.courier_batch_to_bank_credit
    mismatch_categories:
    - mismatch_category.courier_batch_to_bank_credit.missing_expected
    - mismatch_category.courier_batch_to_bank_credit.missing_actual
    - mismatch_category.courier_batch_to_bank_credit.amount_mismatch
    - mismatch_category.courier_batch_to_bank_credit.timing_mismatch
    applicability_scope: platform_type=logistics; tenant/group participation via Business Flow Binding
    evidence_refs:
    - evidence.logistics_kb_doc
    - evidence.cognee_design_v4
    - evidence.unified_edge_scope
    supports_process_note: Profile is reusable; tenant/group-specific account participation is supplied by Business Flow Binding.
```

```yaml
candidate_card:
  card_type: reconciliation_profile
  card_id: reconciliation_profile.prepaid_pos_logistics_settlement
  name: Prepaid/POS Logistics Settlement Reconciliation
  fields:
    name: Prepaid/POS Logistics Settlement Reconciliation
    description: Reusable reconciliation profile for Prepaid/POS Logistics Settlement Reconciliation.
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
    profile_name: Prepaid/POS Logistics Settlement Reconciliation
    business_process_id: business_process.prepaid_pos_logistics_settlement
    reconciliation_type: pos_settlement
    participating_platform_types:
    - marketplace
    - logistics
    - courier
    - banking by profile
    reconciliation_sides: reconciliation_side.prepaid_pos_logistics_settlement.expected; reconciliation_side.prepaid_pos_logistics_settlement.actual
    business_object: order/shipment/awb/settlement/bank_credit
    primary_reconciliation_unit_id: reconciliation_unit.prepaid_pos_logistics_settlement.primary
    secondary_reconciliation_unit_ids: reconciliation_unit.prepaid_pos_logistics_settlement.fallback
    expected_alignment_type: one_to_one or aggregated by profile
    matching_logic_id: matching_logic.prepaid_pos_logistics_settlement
    mismatch_categories:
    - mismatch_category.prepaid_pos_logistics_settlement.missing_expected
    - mismatch_category.prepaid_pos_logistics_settlement.missing_actual
    - mismatch_category.prepaid_pos_logistics_settlement.amount_mismatch
    - mismatch_category.prepaid_pos_logistics_settlement.timing_mismatch
    applicability_scope: platform_type=logistics; tenant/group participation via Business Flow Binding
    evidence_refs:
    - evidence.logistics_kb_doc
    - evidence.cognee_design_v4
    - evidence.unified_edge_scope
```

```yaml
candidate_card:
  card_type: reconciliation_profile
  card_id: reconciliation_profile.low_confidence_native_to_fallback
  name: Low Confidence Native to Fallback Validation
  fields:
    name: Low Confidence Native to Fallback Validation
    description: Reusable reconciliation profile for Low Confidence Native to Fallback Validation.
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
    profile_name: Low Confidence Native to Fallback Validation
    business_process_id: business_process.cod_delivery_to_courier_remittance
    reconciliation_type: data_quality_reconciliation
    participating_platform_types:
    - marketplace
    - logistics
    - courier
    - banking by profile
    reconciliation_sides: reconciliation_side.low_confidence_native_to_fallback.expected; reconciliation_side.low_confidence_native_to_fallback.actual
    business_object: order/shipment/awb/settlement/bank_credit
    primary_reconciliation_unit_id: reconciliation_unit.low_confidence_native_to_fallback.primary
    secondary_reconciliation_unit_ids: reconciliation_unit.low_confidence_native_to_fallback.fallback
    expected_alignment_type: one_to_one or aggregated by profile
    matching_logic_id: matching_logic.low_confidence_native_to_fallback
    mismatch_categories:
    - mismatch_category.low_confidence_native_to_fallback.missing_expected
    - mismatch_category.low_confidence_native_to_fallback.missing_actual
    - mismatch_category.low_confidence_native_to_fallback.amount_mismatch
    - mismatch_category.low_confidence_native_to_fallback.timing_mismatch
    applicability_scope: platform_type=logistics; tenant/group participation via Business Flow Binding
    evidence_refs:
    - evidence.logistics_kb_doc
    - evidence.cognee_design_v4
    - evidence.unified_edge_scope
```

### 4.17 reconciliation_side cards

```yaml
candidate_card:
  card_type: reconciliation_side
  card_id: reconciliation_side.order_to_shipment.expected
  name: Order to Shipment Reconciliation Expected Side
  fields:
    name: Order to Shipment Reconciliation Expected Side
    description: Expected side of Order to Shipment Reconciliation.
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
    side_name: Order to Shipment Reconciliation expected
    side_role: expected
    platform_type: marketplace/logistics/courier/banking_by_profile
    business_object: order/shipment/awb/settlement/bank_credit
    expected_state: profile_specific
    amount_concept: profile_specific_amount_metric
    date_concept: profile_specific_date
    identifier_concepts: order_id; awb; settlement_id; remittance_number; utr; bank_reference
    recommended_metrics: metric.shipment_count; metric.freight_billed_amount; metric.cod_remitted_amount; metric.bank_credit_matched_amount
    typical_tables: see query patterns
    evidence_refs:
    - evidence.logistics_kb_doc
    - evidence.cognee_design_v4
    - evidence.unified_edge_scope
    side_operational_purpose: Defines one evidence side of a reconciliation profile; account filters are not encoded here.
```

```yaml
candidate_card:
  card_type: reconciliation_side
  card_id: reconciliation_side.order_to_shipment.actual
  name: Order to Shipment Reconciliation Actual Side
  fields:
    name: Order to Shipment Reconciliation Actual Side
    description: Actual side of Order to Shipment Reconciliation.
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
    side_name: Order to Shipment Reconciliation actual
    side_role: actual
    platform_type: marketplace/logistics/courier/banking_by_profile
    business_object: order/shipment/awb/settlement/bank_credit
    expected_state: profile_specific
    amount_concept: profile_specific_amount_metric
    date_concept: profile_specific_date
    identifier_concepts: order_id; awb; settlement_id; remittance_number; utr; bank_reference
    recommended_metrics: metric.shipment_count; metric.freight_billed_amount; metric.cod_remitted_amount; metric.bank_credit_matched_amount
    typical_tables: see query patterns
    evidence_refs:
    - evidence.logistics_kb_doc
    - evidence.cognee_design_v4
    - evidence.unified_edge_scope
    side_operational_purpose: Defines one evidence side of a reconciliation profile; account filters are not encoded here.
```

```yaml
candidate_card:
  card_type: reconciliation_side
  card_id: reconciliation_side.shipment_to_freight_invoice.expected
  name: Shipment to Freight Invoice Reconciliation Expected Side
  fields:
    name: Shipment to Freight Invoice Reconciliation Expected Side
    description: Expected side of Shipment to Freight Invoice Reconciliation.
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
    side_name: Shipment to Freight Invoice Reconciliation expected
    side_role: expected
    platform_type: marketplace/logistics/courier/banking_by_profile
    business_object: order/shipment/awb/settlement/bank_credit
    expected_state: profile_specific
    amount_concept: profile_specific_amount_metric
    date_concept: profile_specific_date
    identifier_concepts: order_id; awb; settlement_id; remittance_number; utr; bank_reference
    recommended_metrics: metric.shipment_count; metric.freight_billed_amount; metric.cod_remitted_amount; metric.bank_credit_matched_amount
    typical_tables: see query patterns
    evidence_refs:
    - evidence.logistics_kb_doc
    - evidence.cognee_design_v4
    - evidence.unified_edge_scope
    side_operational_purpose: Defines one evidence side of a reconciliation profile; account filters are not encoded here.
```

```yaml
candidate_card:
  card_type: reconciliation_side
  card_id: reconciliation_side.shipment_to_freight_invoice.actual
  name: Shipment to Freight Invoice Reconciliation Actual Side
  fields:
    name: Shipment to Freight Invoice Reconciliation Actual Side
    description: Actual side of Shipment to Freight Invoice Reconciliation.
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
    side_name: Shipment to Freight Invoice Reconciliation actual
    side_role: actual
    platform_type: marketplace/logistics/courier/banking_by_profile
    business_object: order/shipment/awb/settlement/bank_credit
    expected_state: profile_specific
    amount_concept: profile_specific_amount_metric
    date_concept: profile_specific_date
    identifier_concepts: order_id; awb; settlement_id; remittance_number; utr; bank_reference
    recommended_metrics: metric.shipment_count; metric.freight_billed_amount; metric.cod_remitted_amount; metric.bank_credit_matched_amount
    typical_tables: see query patterns
    evidence_refs:
    - evidence.logistics_kb_doc
    - evidence.cognee_design_v4
    - evidence.unified_edge_scope
    side_operational_purpose: Defines one evidence side of a reconciliation profile; account filters are not encoded here.
```

```yaml
candidate_card:
  card_type: reconciliation_side
  card_id: reconciliation_side.freight_charge_validation.expected
  name: Freight Charge Validation Expected Side
  fields:
    name: Freight Charge Validation Expected Side
    description: Expected side of Freight Charge Validation.
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
    side_name: Freight Charge Validation expected
    side_role: expected
    platform_type: marketplace/logistics/courier/banking_by_profile
    business_object: order/shipment/awb/settlement/bank_credit
    expected_state: profile_specific
    amount_concept: profile_specific_amount_metric
    date_concept: profile_specific_date
    identifier_concepts: order_id; awb; settlement_id; remittance_number; utr; bank_reference
    recommended_metrics: metric.shipment_count; metric.freight_billed_amount; metric.cod_remitted_amount; metric.bank_credit_matched_amount
    typical_tables: see query patterns
    evidence_refs:
    - evidence.logistics_kb_doc
    - evidence.cognee_design_v4
    - evidence.unified_edge_scope
    side_operational_purpose: Defines one evidence side of a reconciliation profile; account filters are not encoded here.
```

```yaml
candidate_card:
  card_type: reconciliation_side
  card_id: reconciliation_side.freight_charge_validation.actual
  name: Freight Charge Validation Actual Side
  fields:
    name: Freight Charge Validation Actual Side
    description: Actual side of Freight Charge Validation.
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
    side_name: Freight Charge Validation actual
    side_role: actual
    platform_type: marketplace/logistics/courier/banking_by_profile
    business_object: order/shipment/awb/settlement/bank_credit
    expected_state: profile_specific
    amount_concept: profile_specific_amount_metric
    date_concept: profile_specific_date
    identifier_concepts: order_id; awb; settlement_id; remittance_number; utr; bank_reference
    recommended_metrics: metric.shipment_count; metric.freight_billed_amount; metric.cod_remitted_amount; metric.bank_credit_matched_amount
    typical_tables: see query patterns
    evidence_refs:
    - evidence.logistics_kb_doc
    - evidence.cognee_design_v4
    - evidence.unified_edge_scope
    side_operational_purpose: Defines one evidence side of a reconciliation profile; account filters are not encoded here.
```

```yaml
candidate_card:
  card_type: reconciliation_side
  card_id: reconciliation_side.cod_expected_to_courier_remittance.expected
  name: COD Expected to Courier Remittance Reconciliation Expected Side
  fields:
    name: COD Expected to Courier Remittance Reconciliation Expected Side
    description: Expected side of COD Expected to Courier Remittance Reconciliation.
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
    side_name: COD Expected to Courier Remittance Reconciliation expected
    side_role: expected
    platform_type: marketplace/logistics/courier/banking_by_profile
    business_object: order/shipment/awb/settlement/bank_credit
    expected_state: profile_specific
    amount_concept: profile_specific_amount_metric
    date_concept: profile_specific_date
    identifier_concepts: order_id; awb; settlement_id; remittance_number; utr; bank_reference
    recommended_metrics: metric.shipment_count; metric.freight_billed_amount; metric.cod_remitted_amount; metric.bank_credit_matched_amount
    typical_tables: see query patterns
    evidence_refs:
    - evidence.logistics_kb_doc
    - evidence.cognee_design_v4
    - evidence.unified_edge_scope
    side_operational_purpose: Defines one evidence side of a reconciliation profile; account filters are not encoded here.
```

```yaml
candidate_card:
  card_type: reconciliation_side
  card_id: reconciliation_side.cod_expected_to_courier_remittance.actual
  name: COD Expected to Courier Remittance Reconciliation Actual Side
  fields:
    name: COD Expected to Courier Remittance Reconciliation Actual Side
    description: Actual side of COD Expected to Courier Remittance Reconciliation.
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
    side_name: COD Expected to Courier Remittance Reconciliation actual
    side_role: actual
    platform_type: marketplace/logistics/courier/banking_by_profile
    business_object: order/shipment/awb/settlement/bank_credit
    expected_state: profile_specific
    amount_concept: profile_specific_amount_metric
    date_concept: profile_specific_date
    identifier_concepts: order_id; awb; settlement_id; remittance_number; utr; bank_reference
    recommended_metrics: metric.shipment_count; metric.freight_billed_amount; metric.cod_remitted_amount; metric.bank_credit_matched_amount
    typical_tables: see query patterns
    evidence_refs:
    - evidence.logistics_kb_doc
    - evidence.cognee_design_v4
    - evidence.unified_edge_scope
    side_operational_purpose: Defines one evidence side of a reconciliation profile; account filters are not encoded here.
```

```yaml
candidate_card:
  card_type: reconciliation_side
  card_id: reconciliation_side.courier_batch_to_bank_credit.expected
  name: Courier Batch to Bank Credit Reconciliation Expected Side
  fields:
    name: Courier Batch to Bank Credit Reconciliation Expected Side
    description: Expected side of Courier Batch to Bank Credit Reconciliation.
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
    side_name: Courier Batch to Bank Credit Reconciliation expected
    side_role: expected
    platform_type: marketplace/logistics/courier/banking_by_profile
    business_object: order/shipment/awb/settlement/bank_credit
    expected_state: profile_specific
    amount_concept: profile_specific_amount_metric
    date_concept: profile_specific_date
    identifier_concepts: order_id; awb; settlement_id; remittance_number; utr; bank_reference
    recommended_metrics: metric.shipment_count; metric.freight_billed_amount; metric.cod_remitted_amount; metric.bank_credit_matched_amount
    typical_tables: see query patterns
    evidence_refs:
    - evidence.logistics_kb_doc
    - evidence.cognee_design_v4
    - evidence.unified_edge_scope
    side_operational_purpose: Defines one evidence side of a reconciliation profile; account filters are not encoded here.
```

```yaml
candidate_card:
  card_type: reconciliation_side
  card_id: reconciliation_side.courier_batch_to_bank_credit.actual
  name: Courier Batch to Bank Credit Reconciliation Actual Side
  fields:
    name: Courier Batch to Bank Credit Reconciliation Actual Side
    description: Actual side of Courier Batch to Bank Credit Reconciliation.
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
    side_name: Courier Batch to Bank Credit Reconciliation actual
    side_role: actual
    platform_type: marketplace/logistics/courier/banking_by_profile
    business_object: order/shipment/awb/settlement/bank_credit
    expected_state: profile_specific
    amount_concept: profile_specific_amount_metric
    date_concept: profile_specific_date
    identifier_concepts: order_id; awb; settlement_id; remittance_number; utr; bank_reference
    recommended_metrics: metric.shipment_count; metric.freight_billed_amount; metric.cod_remitted_amount; metric.bank_credit_matched_amount
    typical_tables: see query patterns
    evidence_refs:
    - evidence.logistics_kb_doc
    - evidence.cognee_design_v4
    - evidence.unified_edge_scope
    side_operational_purpose: Defines one evidence side of a reconciliation profile; account filters are not encoded here.
```

```yaml
candidate_card:
  card_type: reconciliation_side
  card_id: reconciliation_side.prepaid_pos_logistics_settlement.expected
  name: Prepaid/POS Logistics Settlement Reconciliation Expected Side
  fields:
    name: Prepaid/POS Logistics Settlement Reconciliation Expected Side
    description: Expected side of Prepaid/POS Logistics Settlement Reconciliation.
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
    side_name: Prepaid/POS Logistics Settlement Reconciliation expected
    side_role: expected
    platform_type: marketplace/logistics/courier/banking_by_profile
    business_object: order/shipment/awb/settlement/bank_credit
    expected_state: profile_specific
    amount_concept: profile_specific_amount_metric
    date_concept: profile_specific_date
    identifier_concepts: order_id; awb; settlement_id; remittance_number; utr; bank_reference
    recommended_metrics: metric.shipment_count; metric.freight_billed_amount; metric.cod_remitted_amount; metric.bank_credit_matched_amount
    typical_tables: see query patterns
    evidence_refs:
    - evidence.logistics_kb_doc
    - evidence.cognee_design_v4
    - evidence.unified_edge_scope
    side_operational_purpose: Defines one evidence side of a reconciliation profile; account filters are not encoded here.
```

```yaml
candidate_card:
  card_type: reconciliation_side
  card_id: reconciliation_side.prepaid_pos_logistics_settlement.actual
  name: Prepaid/POS Logistics Settlement Reconciliation Actual Side
  fields:
    name: Prepaid/POS Logistics Settlement Reconciliation Actual Side
    description: Actual side of Prepaid/POS Logistics Settlement Reconciliation.
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
    side_name: Prepaid/POS Logistics Settlement Reconciliation actual
    side_role: actual
    platform_type: marketplace/logistics/courier/banking_by_profile
    business_object: order/shipment/awb/settlement/bank_credit
    expected_state: profile_specific
    amount_concept: profile_specific_amount_metric
    date_concept: profile_specific_date
    identifier_concepts: order_id; awb; settlement_id; remittance_number; utr; bank_reference
    recommended_metrics: metric.shipment_count; metric.freight_billed_amount; metric.cod_remitted_amount; metric.bank_credit_matched_amount
    typical_tables: see query patterns
    evidence_refs:
    - evidence.logistics_kb_doc
    - evidence.cognee_design_v4
    - evidence.unified_edge_scope
    side_operational_purpose: Defines one evidence side of a reconciliation profile; account filters are not encoded here.
```

```yaml
candidate_card:
  card_type: reconciliation_side
  card_id: reconciliation_side.low_confidence_native_to_fallback.expected
  name: Low Confidence Native to Fallback Validation Expected Side
  fields:
    name: Low Confidence Native to Fallback Validation Expected Side
    description: Expected side of Low Confidence Native to Fallback Validation.
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
    side_name: Low Confidence Native to Fallback Validation expected
    side_role: expected
    platform_type: marketplace/logistics/courier/banking_by_profile
    business_object: order/shipment/awb/settlement/bank_credit
    expected_state: profile_specific
    amount_concept: profile_specific_amount_metric
    date_concept: profile_specific_date
    identifier_concepts: order_id; awb; settlement_id; remittance_number; utr; bank_reference
    recommended_metrics: metric.shipment_count; metric.freight_billed_amount; metric.cod_remitted_amount; metric.bank_credit_matched_amount
    typical_tables: see query patterns
    evidence_refs:
    - evidence.logistics_kb_doc
    - evidence.cognee_design_v4
    - evidence.unified_edge_scope
    side_operational_purpose: Defines one evidence side of a reconciliation profile; account filters are not encoded here.
```

```yaml
candidate_card:
  card_type: reconciliation_side
  card_id: reconciliation_side.low_confidence_native_to_fallback.actual
  name: Low Confidence Native to Fallback Validation Actual Side
  fields:
    name: Low Confidence Native to Fallback Validation Actual Side
    description: Actual side of Low Confidence Native to Fallback Validation.
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
    side_name: Low Confidence Native to Fallback Validation actual
    side_role: actual
    platform_type: marketplace/logistics/courier/banking_by_profile
    business_object: order/shipment/awb/settlement/bank_credit
    expected_state: profile_specific
    amount_concept: profile_specific_amount_metric
    date_concept: profile_specific_date
    identifier_concepts: order_id; awb; settlement_id; remittance_number; utr; bank_reference
    recommended_metrics: metric.shipment_count; metric.freight_billed_amount; metric.cod_remitted_amount; metric.bank_credit_matched_amount
    typical_tables: see query patterns
    evidence_refs:
    - evidence.logistics_kb_doc
    - evidence.cognee_design_v4
    - evidence.unified_edge_scope
    side_operational_purpose: Defines one evidence side of a reconciliation profile; account filters are not encoded here.
```

### 4.18 reconciliation_unit cards

```yaml
candidate_card:
  card_type: reconciliation_unit
  card_id: reconciliation_unit.order_to_shipment.primary
  name: Order to Shipment Reconciliation Primary Unit
  fields:
    name: Order to Shipment Reconciliation Primary Unit
    description: Primary reconciliation grain for Order to Shipment Reconciliation.
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
    unit_name: Order to Shipment Reconciliation primary unit
    unit_type: order/shipment/awb/settlement_batch/bank_transaction
    identifier_concepts: profile-specific primary identifiers
    typical_platform_types: marketplace; logistics; courier; banking
    expected_uniqueness: mostly_unique_or_composite_required
    preferred_usage: primary
    evidence_refs:
    - evidence.logistics_kb_doc
    - evidence.cognee_design_v4
    - evidence.unified_edge_scope
```

```yaml
candidate_card:
  card_type: reconciliation_unit
  card_id: reconciliation_unit.order_to_shipment.fallback
  name: Order to Shipment Reconciliation Fallback Unit
  fields:
    name: Order to Shipment Reconciliation Fallback Unit
    description: Fallback reconciliation grain for Order to Shipment Reconciliation.
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
    unit_name: Order to Shipment Reconciliation fallback unit
    unit_type: composite
    identifier_concepts: amount; date window; courier; account; batch; reference
    typical_platform_types: marketplace; logistics; courier; banking
    expected_uniqueness: composite_required
    preferred_usage: fallback
    known_issues: risk of false matches; use only when primary references are missing
    evidence_refs:
    - evidence.logistics_kb_doc
    - evidence.cognee_design_v4
    - evidence.unified_edge_scope
```

```yaml
candidate_card:
  card_type: reconciliation_unit
  card_id: reconciliation_unit.shipment_to_freight_invoice.primary
  name: Shipment to Freight Invoice Reconciliation Primary Unit
  fields:
    name: Shipment to Freight Invoice Reconciliation Primary Unit
    description: Primary reconciliation grain for Shipment to Freight Invoice Reconciliation.
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
    unit_name: Shipment to Freight Invoice Reconciliation primary unit
    unit_type: order/shipment/awb/settlement_batch/bank_transaction
    identifier_concepts: profile-specific primary identifiers
    typical_platform_types: marketplace; logistics; courier; banking
    expected_uniqueness: mostly_unique_or_composite_required
    preferred_usage: primary
    evidence_refs:
    - evidence.logistics_kb_doc
    - evidence.cognee_design_v4
    - evidence.unified_edge_scope
```

```yaml
candidate_card:
  card_type: reconciliation_unit
  card_id: reconciliation_unit.shipment_to_freight_invoice.fallback
  name: Shipment to Freight Invoice Reconciliation Fallback Unit
  fields:
    name: Shipment to Freight Invoice Reconciliation Fallback Unit
    description: Fallback reconciliation grain for Shipment to Freight Invoice Reconciliation.
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
    unit_name: Shipment to Freight Invoice Reconciliation fallback unit
    unit_type: composite
    identifier_concepts: amount; date window; courier; account; batch; reference
    typical_platform_types: marketplace; logistics; courier; banking
    expected_uniqueness: composite_required
    preferred_usage: fallback
    known_issues: risk of false matches; use only when primary references are missing
    evidence_refs:
    - evidence.logistics_kb_doc
    - evidence.cognee_design_v4
    - evidence.unified_edge_scope
```

```yaml
candidate_card:
  card_type: reconciliation_unit
  card_id: reconciliation_unit.freight_charge_validation.primary
  name: Freight Charge Validation Primary Unit
  fields:
    name: Freight Charge Validation Primary Unit
    description: Primary reconciliation grain for Freight Charge Validation.
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
    unit_name: Freight Charge Validation primary unit
    unit_type: order/shipment/awb/settlement_batch/bank_transaction
    identifier_concepts: profile-specific primary identifiers
    typical_platform_types: marketplace; logistics; courier; banking
    expected_uniqueness: mostly_unique_or_composite_required
    preferred_usage: primary
    evidence_refs:
    - evidence.logistics_kb_doc
    - evidence.cognee_design_v4
    - evidence.unified_edge_scope
```

```yaml
candidate_card:
  card_type: reconciliation_unit
  card_id: reconciliation_unit.freight_charge_validation.fallback
  name: Freight Charge Validation Fallback Unit
  fields:
    name: Freight Charge Validation Fallback Unit
    description: Fallback reconciliation grain for Freight Charge Validation.
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
    unit_name: Freight Charge Validation fallback unit
    unit_type: composite
    identifier_concepts: amount; date window; courier; account; batch; reference
    typical_platform_types: marketplace; logistics; courier; banking
    expected_uniqueness: composite_required
    preferred_usage: fallback
    known_issues: risk of false matches; use only when primary references are missing
    evidence_refs:
    - evidence.logistics_kb_doc
    - evidence.cognee_design_v4
    - evidence.unified_edge_scope
```

```yaml
candidate_card:
  card_type: reconciliation_unit
  card_id: reconciliation_unit.cod_expected_to_courier_remittance.primary
  name: COD Expected to Courier Remittance Reconciliation Primary Unit
  fields:
    name: COD Expected to Courier Remittance Reconciliation Primary Unit
    description: Primary reconciliation grain for COD Expected to Courier Remittance Reconciliation.
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
    unit_name: COD Expected to Courier Remittance Reconciliation primary unit
    unit_type: order/shipment/awb/settlement_batch/bank_transaction
    identifier_concepts: profile-specific primary identifiers
    typical_platform_types: marketplace; logistics; courier; banking
    expected_uniqueness: mostly_unique_or_composite_required
    preferred_usage: primary
    evidence_refs:
    - evidence.logistics_kb_doc
    - evidence.cognee_design_v4
    - evidence.unified_edge_scope
```

```yaml
candidate_card:
  card_type: reconciliation_unit
  card_id: reconciliation_unit.cod_expected_to_courier_remittance.fallback
  name: COD Expected to Courier Remittance Reconciliation Fallback Unit
  fields:
    name: COD Expected to Courier Remittance Reconciliation Fallback Unit
    description: Fallback reconciliation grain for COD Expected to Courier Remittance Reconciliation.
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
    unit_name: COD Expected to Courier Remittance Reconciliation fallback unit
    unit_type: composite
    identifier_concepts: amount; date window; courier; account; batch; reference
    typical_platform_types: marketplace; logistics; courier; banking
    expected_uniqueness: composite_required
    preferred_usage: fallback
    known_issues: risk of false matches; use only when primary references are missing
    evidence_refs:
    - evidence.logistics_kb_doc
    - evidence.cognee_design_v4
    - evidence.unified_edge_scope
```

```yaml
candidate_card:
  card_type: reconciliation_unit
  card_id: reconciliation_unit.courier_batch_to_bank_credit.primary
  name: Courier Batch to Bank Credit Reconciliation Primary Unit
  fields:
    name: Courier Batch to Bank Credit Reconciliation Primary Unit
    description: Primary reconciliation grain for Courier Batch to Bank Credit Reconciliation.
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
    unit_name: Courier Batch to Bank Credit Reconciliation primary unit
    unit_type: order/shipment/awb/settlement_batch/bank_transaction
    identifier_concepts: profile-specific primary identifiers
    typical_platform_types: marketplace; logistics; courier; banking
    expected_uniqueness: mostly_unique_or_composite_required
    preferred_usage: primary
    evidence_refs:
    - evidence.logistics_kb_doc
    - evidence.cognee_design_v4
    - evidence.unified_edge_scope
```

```yaml
candidate_card:
  card_type: reconciliation_unit
  card_id: reconciliation_unit.courier_batch_to_bank_credit.fallback
  name: Courier Batch to Bank Credit Reconciliation Fallback Unit
  fields:
    name: Courier Batch to Bank Credit Reconciliation Fallback Unit
    description: Fallback reconciliation grain for Courier Batch to Bank Credit Reconciliation.
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
    unit_name: Courier Batch to Bank Credit Reconciliation fallback unit
    unit_type: composite
    identifier_concepts: amount; date window; courier; account; batch; reference
    typical_platform_types: marketplace; logistics; courier; banking
    expected_uniqueness: composite_required
    preferred_usage: fallback
    known_issues: risk of false matches; use only when primary references are missing
    evidence_refs:
    - evidence.logistics_kb_doc
    - evidence.cognee_design_v4
    - evidence.unified_edge_scope
```

```yaml
candidate_card:
  card_type: reconciliation_unit
  card_id: reconciliation_unit.prepaid_pos_logistics_settlement.primary
  name: Prepaid/POS Logistics Settlement Reconciliation Primary Unit
  fields:
    name: Prepaid/POS Logistics Settlement Reconciliation Primary Unit
    description: Primary reconciliation grain for Prepaid/POS Logistics Settlement Reconciliation.
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
    unit_name: Prepaid/POS Logistics Settlement Reconciliation primary unit
    unit_type: order/shipment/awb/settlement_batch/bank_transaction
    identifier_concepts: profile-specific primary identifiers
    typical_platform_types: marketplace; logistics; courier; banking
    expected_uniqueness: mostly_unique_or_composite_required
    preferred_usage: primary
    evidence_refs:
    - evidence.logistics_kb_doc
    - evidence.cognee_design_v4
    - evidence.unified_edge_scope
```

```yaml
candidate_card:
  card_type: reconciliation_unit
  card_id: reconciliation_unit.prepaid_pos_logistics_settlement.fallback
  name: Prepaid/POS Logistics Settlement Reconciliation Fallback Unit
  fields:
    name: Prepaid/POS Logistics Settlement Reconciliation Fallback Unit
    description: Fallback reconciliation grain for Prepaid/POS Logistics Settlement Reconciliation.
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
    unit_name: Prepaid/POS Logistics Settlement Reconciliation fallback unit
    unit_type: composite
    identifier_concepts: amount; date window; courier; account; batch; reference
    typical_platform_types: marketplace; logistics; courier; banking
    expected_uniqueness: composite_required
    preferred_usage: fallback
    known_issues: risk of false matches; use only when primary references are missing
    evidence_refs:
    - evidence.logistics_kb_doc
    - evidence.cognee_design_v4
    - evidence.unified_edge_scope
```

```yaml
candidate_card:
  card_type: reconciliation_unit
  card_id: reconciliation_unit.low_confidence_native_to_fallback.primary
  name: Low Confidence Native to Fallback Validation Primary Unit
  fields:
    name: Low Confidence Native to Fallback Validation Primary Unit
    description: Primary reconciliation grain for Low Confidence Native to Fallback Validation.
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
    unit_name: Low Confidence Native to Fallback Validation primary unit
    unit_type: order/shipment/awb/settlement_batch/bank_transaction
    identifier_concepts: profile-specific primary identifiers
    typical_platform_types: marketplace; logistics; courier; banking
    expected_uniqueness: mostly_unique_or_composite_required
    preferred_usage: primary
    evidence_refs:
    - evidence.logistics_kb_doc
    - evidence.cognee_design_v4
    - evidence.unified_edge_scope
```

```yaml
candidate_card:
  card_type: reconciliation_unit
  card_id: reconciliation_unit.low_confidence_native_to_fallback.fallback
  name: Low Confidence Native to Fallback Validation Fallback Unit
  fields:
    name: Low Confidence Native to Fallback Validation Fallback Unit
    description: Fallback reconciliation grain for Low Confidence Native to Fallback Validation.
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
    unit_name: Low Confidence Native to Fallback Validation fallback unit
    unit_type: composite
    identifier_concepts: amount; date window; courier; account; batch; reference
    typical_platform_types: marketplace; logistics; courier; banking
    expected_uniqueness: composite_required
    preferred_usage: fallback
    known_issues: risk of false matches; use only when primary references are missing
    evidence_refs:
    - evidence.logistics_kb_doc
    - evidence.cognee_design_v4
    - evidence.unified_edge_scope
```

```yaml
candidate_card:
  card_type: reconciliation_unit
  card_id: reconciliation_unit.order_id
  name: Order Id
  fields:
    name: Order Id
    description: 'Generic reconciliation unit: order_id.'
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
    unit_name: order_id
    unit_type: identifier_or_composite
    identifier_concepts: order_id
    typical_platform_types: logistics; courier; banking; marketplace
    expected_uniqueness: source_specific
    preferred_usage: primary_or_fallback
    evidence_refs:
    - evidence.logistics_kb_doc
    - evidence.cognee_design_v4
    - evidence.unified_edge_scope
```

```yaml
candidate_card:
  card_type: reconciliation_unit
  card_id: reconciliation_unit.awb
  name: Awb
  fields:
    name: Awb
    description: 'Generic reconciliation unit: awb.'
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
    unit_name: awb
    unit_type: identifier_or_composite
    identifier_concepts: awb
    typical_platform_types: logistics; courier; banking; marketplace
    expected_uniqueness: source_specific
    preferred_usage: primary_or_fallback
    evidence_refs:
    - evidence.logistics_kb_doc
    - evidence.cognee_design_v4
    - evidence.unified_edge_scope
```

```yaml
candidate_card:
  card_type: reconciliation_unit
  card_id: reconciliation_unit.waybill
  name: Waybill
  fields:
    name: Waybill
    description: 'Generic reconciliation unit: waybill.'
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
    unit_name: waybill
    unit_type: identifier_or_composite
    identifier_concepts: waybill
    typical_platform_types: logistics; courier; banking; marketplace
    expected_uniqueness: source_specific
    preferred_usage: primary_or_fallback
    evidence_refs:
    - evidence.logistics_kb_doc
    - evidence.cognee_design_v4
    - evidence.unified_edge_scope
```

```yaml
candidate_card:
  card_type: reconciliation_unit
  card_id: reconciliation_unit.tracking_id
  name: Tracking Id
  fields:
    name: Tracking Id
    description: 'Generic reconciliation unit: tracking_id.'
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
    unit_name: tracking_id
    unit_type: identifier_or_composite
    identifier_concepts: tracking_id
    typical_platform_types: logistics; courier; banking; marketplace
    expected_uniqueness: source_specific
    preferred_usage: primary_or_fallback
    evidence_refs:
    - evidence.logistics_kb_doc
    - evidence.cognee_design_v4
    - evidence.unified_edge_scope
```

```yaml
candidate_card:
  card_type: reconciliation_unit
  card_id: reconciliation_unit.invoice_number
  name: Invoice Number
  fields:
    name: Invoice Number
    description: 'Generic reconciliation unit: invoice_number.'
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
    unit_name: invoice_number
    unit_type: identifier_or_composite
    identifier_concepts: invoice_number
    typical_platform_types: logistics; courier; banking; marketplace
    expected_uniqueness: source_specific
    preferred_usage: primary_or_fallback
    evidence_refs:
    - evidence.logistics_kb_doc
    - evidence.cognee_design_v4
    - evidence.unified_edge_scope
```

```yaml
candidate_card:
  card_type: reconciliation_unit
  card_id: reconciliation_unit.settlement_id
  name: Settlement Id
  fields:
    name: Settlement Id
    description: 'Generic reconciliation unit: settlement_id.'
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
    unit_name: settlement_id
    unit_type: identifier_or_composite
    identifier_concepts: settlement_id
    typical_platform_types: logistics; courier; banking; marketplace
    expected_uniqueness: source_specific
    preferred_usage: primary_or_fallback
    evidence_refs:
    - evidence.logistics_kb_doc
    - evidence.cognee_design_v4
    - evidence.unified_edge_scope
```

```yaml
candidate_card:
  card_type: reconciliation_unit
  card_id: reconciliation_unit.remittance_number
  name: Remittance Number
  fields:
    name: Remittance Number
    description: 'Generic reconciliation unit: remittance_number.'
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
    unit_name: remittance_number
    unit_type: identifier_or_composite
    identifier_concepts: remittance_number
    typical_platform_types: logistics; courier; banking; marketplace
    expected_uniqueness: source_specific
    preferred_usage: primary_or_fallback
    evidence_refs:
    - evidence.logistics_kb_doc
    - evidence.cognee_design_v4
    - evidence.unified_edge_scope
```

```yaml
candidate_card:
  card_type: reconciliation_unit
  card_id: reconciliation_unit.utr
  name: Utr
  fields:
    name: Utr
    description: 'Generic reconciliation unit: utr.'
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
    unit_name: utr
    unit_type: identifier_or_composite
    identifier_concepts: utr
    typical_platform_types: logistics; courier; banking; marketplace
    expected_uniqueness: source_specific
    preferred_usage: primary_or_fallback
    evidence_refs:
    - evidence.logistics_kb_doc
    - evidence.cognee_design_v4
    - evidence.unified_edge_scope
```

```yaml
candidate_card:
  card_type: reconciliation_unit
  card_id: reconciliation_unit.bank_reference
  name: Bank Reference
  fields:
    name: Bank Reference
    description: 'Generic reconciliation unit: bank_reference.'
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
    unit_name: bank_reference
    unit_type: identifier_or_composite
    identifier_concepts: bank_reference
    typical_platform_types: logistics; courier; banking; marketplace
    expected_uniqueness: source_specific
    preferred_usage: primary_or_fallback
    evidence_refs:
    - evidence.logistics_kb_doc
    - evidence.cognee_design_v4
    - evidence.unified_edge_scope
```

```yaml
candidate_card:
  card_type: reconciliation_unit
  card_id: reconciliation_unit.amount_date_courier
  name: Amount Date Courier
  fields:
    name: Amount Date Courier
    description: 'Generic reconciliation unit: amount_date_courier.'
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
    unit_name: amount_date_courier
    unit_type: identifier_or_composite
    identifier_concepts: amount_date_courier
    typical_platform_types: logistics; courier; banking; marketplace
    expected_uniqueness: source_specific
    preferred_usage: primary_or_fallback
    evidence_refs:
    - evidence.logistics_kb_doc
    - evidence.cognee_design_v4
    - evidence.unified_edge_scope
```

```yaml
candidate_card:
  card_type: reconciliation_unit
  card_id: reconciliation_unit.amount_date_bank_account
  name: Amount Date Bank Account
  fields:
    name: Amount Date Bank Account
    description: 'Generic reconciliation unit: amount_date_bank_account.'
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
    unit_name: amount_date_bank_account
    unit_type: identifier_or_composite
    identifier_concepts: amount_date_bank_account
    typical_platform_types: logistics; courier; banking; marketplace
    expected_uniqueness: source_specific
    preferred_usage: primary_or_fallback
    evidence_refs:
    - evidence.logistics_kb_doc
    - evidence.cognee_design_v4
    - evidence.unified_edge_scope
```

```yaml
candidate_card:
  card_type: reconciliation_unit
  card_id: reconciliation_unit.awb_plus_courier
  name: Awb Plus Courier
  fields:
    name: Awb Plus Courier
    description: 'Generic reconciliation unit: awb_plus_courier.'
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
    unit_name: awb_plus_courier
    unit_type: identifier_or_composite
    identifier_concepts: awb_plus_courier
    typical_platform_types: logistics; courier; banking; marketplace
    expected_uniqueness: source_specific
    preferred_usage: primary_or_fallback
    evidence_refs:
    - evidence.logistics_kb_doc
    - evidence.cognee_design_v4
    - evidence.unified_edge_scope
```

### 4.19 matching_logic cards

```yaml
candidate_card:
  card_type: matching_logic
  card_id: matching_logic.order_to_shipment
  name: Order to Shipment Reconciliation Matching Logic
  fields:
    name: Order to Shipment Reconciliation Matching Logic
    description: Matching logic for Order to Shipment Reconciliation.
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
    logic_name: Order to Shipment Reconciliation matching
    reconciliation_profile_id: reconciliation_profile.order_to_shipment
    matching_strategy: staged; exact_primary_then_fallback_composite
    primary_match_keys: order_id/awb/settlement_id/utr by profile
    secondary_match_keys: amount; date window; courier; account
    fallback_match_strategy: amount_plus_date_window_plus_courier_or_bank_account
    expected_alignment_type: profile_specific
    amount_tolerance: 0 unless bank rounding/source-specific tolerance is configured
    time_tolerance: same day to source-specific remittance window
    match_confidence_rules: exact reference=high; amount/date fallback=medium; sparse native=low
    unmatched_handling: classify into mismatch categories
    evidence_refs:
    - evidence.logistics_kb_doc
    - evidence.cognee_design_v4
    - evidence.unified_edge_scope
    matching_logic_boundary: Defines generic matching behavior, not tenant/group account routing.
```

```yaml
candidate_card:
  card_type: matching_logic
  card_id: matching_logic.shipment_to_freight_invoice
  name: Shipment to Freight Invoice Reconciliation Matching Logic
  fields:
    name: Shipment to Freight Invoice Reconciliation Matching Logic
    description: Matching logic for Shipment to Freight Invoice Reconciliation.
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
    logic_name: Shipment to Freight Invoice Reconciliation matching
    reconciliation_profile_id: reconciliation_profile.shipment_to_freight_invoice
    matching_strategy: staged; exact_primary_then_fallback_composite
    primary_match_keys: order_id/awb/settlement_id/utr by profile
    secondary_match_keys: amount; date window; courier; account
    fallback_match_strategy: amount_plus_date_window_plus_courier_or_bank_account
    expected_alignment_type: profile_specific
    amount_tolerance: 0 unless bank rounding/source-specific tolerance is configured
    time_tolerance: same day to source-specific remittance window
    match_confidence_rules: exact reference=high; amount/date fallback=medium; sparse native=low
    unmatched_handling: classify into mismatch categories
    evidence_refs:
    - evidence.logistics_kb_doc
    - evidence.cognee_design_v4
    - evidence.unified_edge_scope
    matching_logic_boundary: Defines generic matching behavior, not tenant/group account routing.
```

```yaml
candidate_card:
  card_type: matching_logic
  card_id: matching_logic.freight_charge_validation
  name: Freight Charge Validation Matching Logic
  fields:
    name: Freight Charge Validation Matching Logic
    description: Matching logic for Freight Charge Validation.
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
    logic_name: Freight Charge Validation matching
    reconciliation_profile_id: reconciliation_profile.freight_charge_validation
    matching_strategy: staged; exact_primary_then_fallback_composite
    primary_match_keys: order_id/awb/settlement_id/utr by profile
    secondary_match_keys: amount; date window; courier; account
    fallback_match_strategy: amount_plus_date_window_plus_courier_or_bank_account
    expected_alignment_type: profile_specific
    amount_tolerance: 0 unless bank rounding/source-specific tolerance is configured
    time_tolerance: same day to source-specific remittance window
    match_confidence_rules: exact reference=high; amount/date fallback=medium; sparse native=low
    unmatched_handling: classify into mismatch categories
    evidence_refs:
    - evidence.logistics_kb_doc
    - evidence.cognee_design_v4
    - evidence.unified_edge_scope
    matching_logic_boundary: Defines generic matching behavior, not tenant/group account routing.
```

```yaml
candidate_card:
  card_type: matching_logic
  card_id: matching_logic.cod_expected_to_courier_remittance
  name: COD Expected to Courier Remittance Reconciliation Matching Logic
  fields:
    name: COD Expected to Courier Remittance Reconciliation Matching Logic
    description: Matching logic for COD Expected to Courier Remittance Reconciliation.
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
    logic_name: COD Expected to Courier Remittance Reconciliation matching
    reconciliation_profile_id: reconciliation_profile.cod_expected_to_courier_remittance
    matching_strategy: staged; exact_primary_then_fallback_composite
    primary_match_keys: order_id/awb/settlement_id/utr by profile
    secondary_match_keys: amount; date window; courier; account
    fallback_match_strategy: amount_plus_date_window_plus_courier_or_bank_account
    expected_alignment_type: profile_specific
    amount_tolerance: 0 unless bank rounding/source-specific tolerance is configured
    time_tolerance: same day to source-specific remittance window
    match_confidence_rules: exact reference=high; amount/date fallback=medium; sparse native=low
    unmatched_handling: classify into mismatch categories
    evidence_refs:
    - evidence.logistics_kb_doc
    - evidence.cognee_design_v4
    - evidence.unified_edge_scope
    matching_logic_boundary: Defines generic matching behavior, not tenant/group account routing.
```

```yaml
candidate_card:
  card_type: matching_logic
  card_id: matching_logic.courier_batch_to_bank_credit
  name: Courier Batch to Bank Credit Reconciliation Matching Logic
  fields:
    name: Courier Batch to Bank Credit Reconciliation Matching Logic
    description: Matching logic for Courier Batch to Bank Credit Reconciliation.
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
    logic_name: Courier Batch to Bank Credit Reconciliation matching
    reconciliation_profile_id: reconciliation_profile.courier_batch_to_bank_credit
    matching_strategy: staged; exact_primary_then_fallback_composite
    primary_match_keys: order_id/awb/settlement_id/utr by profile
    secondary_match_keys: amount; date window; courier; account
    fallback_match_strategy: amount_plus_date_window_plus_courier_or_bank_account
    expected_alignment_type: profile_specific
    amount_tolerance: 0 unless bank rounding/source-specific tolerance is configured
    time_tolerance: same day to source-specific remittance window
    match_confidence_rules: exact reference=high; amount/date fallback=medium; sparse native=low
    unmatched_handling: classify into mismatch categories
    evidence_refs:
    - evidence.logistics_kb_doc
    - evidence.cognee_design_v4
    - evidence.unified_edge_scope
    matching_logic_boundary: Defines generic matching behavior, not tenant/group account routing.
```

```yaml
candidate_card:
  card_type: matching_logic
  card_id: matching_logic.prepaid_pos_logistics_settlement
  name: Prepaid/POS Logistics Settlement Reconciliation Matching Logic
  fields:
    name: Prepaid/POS Logistics Settlement Reconciliation Matching Logic
    description: Matching logic for Prepaid/POS Logistics Settlement Reconciliation.
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
    logic_name: Prepaid/POS Logistics Settlement Reconciliation matching
    reconciliation_profile_id: reconciliation_profile.prepaid_pos_logistics_settlement
    matching_strategy: staged; exact_primary_then_fallback_composite
    primary_match_keys: order_id/awb/settlement_id/utr by profile
    secondary_match_keys: amount; date window; courier; account
    fallback_match_strategy: amount_plus_date_window_plus_courier_or_bank_account
    expected_alignment_type: profile_specific
    amount_tolerance: 0 unless bank rounding/source-specific tolerance is configured
    time_tolerance: same day to source-specific remittance window
    match_confidence_rules: exact reference=high; amount/date fallback=medium; sparse native=low
    unmatched_handling: classify into mismatch categories
    evidence_refs:
    - evidence.logistics_kb_doc
    - evidence.cognee_design_v4
    - evidence.unified_edge_scope
    matching_logic_boundary: Defines generic matching behavior, not tenant/group account routing.
```

```yaml
candidate_card:
  card_type: matching_logic
  card_id: matching_logic.low_confidence_native_to_fallback
  name: Low Confidence Native to Fallback Validation Matching Logic
  fields:
    name: Low Confidence Native to Fallback Validation Matching Logic
    description: Matching logic for Low Confidence Native to Fallback Validation.
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
    logic_name: Low Confidence Native to Fallback Validation matching
    reconciliation_profile_id: reconciliation_profile.low_confidence_native_to_fallback
    matching_strategy: staged; exact_primary_then_fallback_composite
    primary_match_keys: order_id/awb/settlement_id/utr by profile
    secondary_match_keys: amount; date window; courier; account
    fallback_match_strategy: amount_plus_date_window_plus_courier_or_bank_account
    expected_alignment_type: profile_specific
    amount_tolerance: 0 unless bank rounding/source-specific tolerance is configured
    time_tolerance: same day to source-specific remittance window
    match_confidence_rules: exact reference=high; amount/date fallback=medium; sparse native=low
    unmatched_handling: classify into mismatch categories
    evidence_refs:
    - evidence.logistics_kb_doc
    - evidence.cognee_design_v4
    - evidence.unified_edge_scope
    matching_logic_boundary: Defines generic matching behavior, not tenant/group account routing.
```

```yaml
candidate_card:
  card_type: matching_logic
  card_id: matching_logic.logistics.exact_awb_match
  name: Exact AWB Match
  fields:
    name: Exact AWB Match
    description: Exact match on AWB, waybill, tracking_id, shipping_id, or other_id after normalization.
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
    logic_name: Exact AWB Match
    reconciliation_profile_id: applies_to_multiple_logistics_reconciliation_profiles
    matching_strategy: exact
    primary_match_keys: awb; waybill; tracking_id; shipping_id; other_id
    secondary_match_keys: amount; date window; platform/vendor; account scope when needed
    fallback_match_strategy: use staged fallback only after primary reference failure
    expected_alignment_type: one_to_one_or_aggregated_by_pattern
    amount_tolerance: 0 unless documented by source-specific rule
    time_tolerance: source-specific date window
    match_confidence_rules: exact reference high; batch/reference medium-high; amount/date fallback medium; sparse native
      low
    unmatched_handling: classify using mismatch_category cards
    notes: This additional matching logic card expands profile-level matching into reusable deterministic key-level patterns.
    evidence_refs:
    - evidence.logistics_kb_doc
    - evidence.cognee_design_v4
    - evidence.unified_edge_scope
    matching_logic_boundary: Defines generic matching behavior, not tenant/group account routing.
```

```yaml
candidate_card:
  card_type: matching_logic
  card_id: matching_logic.logistics.parsed_shopify_to_shiprocket_order_match
  name: Parsed Shopify to Shiprocket Order Match
  fields:
    name: Parsed Shopify to Shiprocket Order Match
    description: Match Shopify order_id to Shiprocket composite order_id by stripping the -s shipment suffix.
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
    logic_name: Parsed Shopify to Shiprocket Order Match
    reconciliation_profile_id: applies_to_multiple_logistics_reconciliation_profiles
    matching_strategy: rule_based
    primary_match_keys: shopify_order_id; parsed_shiprocket_order_id
    secondary_match_keys: amount; date window; platform/vendor; account scope when needed
    fallback_match_strategy: use staged fallback only after primary reference failure
    expected_alignment_type: one_to_one_or_aggregated_by_pattern
    amount_tolerance: 0 unless documented by source-specific rule
    time_tolerance: source-specific date window
    match_confidence_rules: exact reference high; batch/reference medium-high; amount/date fallback medium; sparse native
      low
    unmatched_handling: classify using mismatch_category cards
    notes: This additional matching logic card expands profile-level matching into reusable deterministic key-level patterns.
    evidence_refs:
    - evidence.logistics_kb_doc
    - evidence.cognee_design_v4
    - evidence.unified_edge_scope
    matching_logic_boundary: Defines generic matching behavior, not tenant/group account routing.
```

```yaml
candidate_card:
  card_type: matching_logic
  card_id: matching_logic.logistics.utr_bank_credit_match
  name: UTR to Bank Credit Match
  fields:
    name: UTR to Bank Credit Match
    description: Match logistics remittance records to bank credits using UTR.
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
    logic_name: UTR to Bank Credit Match
    reconciliation_profile_id: applies_to_multiple_logistics_reconciliation_profiles
    matching_strategy: exact
    primary_match_keys: utr_no
    secondary_match_keys: amount; date window; platform/vendor; account scope when needed
    fallback_match_strategy: use staged fallback only after primary reference failure
    expected_alignment_type: one_to_one_or_aggregated_by_pattern
    amount_tolerance: 0 unless documented by source-specific rule
    time_tolerance: source-specific date window
    match_confidence_rules: exact reference high; batch/reference medium-high; amount/date fallback medium; sparse native
      low
    unmatched_handling: classify using mismatch_category cards
    notes: This additional matching logic card expands profile-level matching into reusable deterministic key-level patterns.
    evidence_refs:
    - evidence.logistics_kb_doc
    - evidence.cognee_design_v4
    - evidence.unified_edge_scope
    matching_logic_boundary: Defines generic matching behavior, not tenant/group account routing.
```

```yaml
candidate_card:
  card_type: matching_logic
  card_id: matching_logic.logistics.bank_reference_match
  name: Bank Reference Match
  fields:
    name: Bank Reference Match
    description: Match settlement or remittance records to bank credits using bank reference number.
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
    logic_name: Bank Reference Match
    reconciliation_profile_id: applies_to_multiple_logistics_reconciliation_profiles
    matching_strategy: exact
    primary_match_keys: bank_reference_no; remittance_number; settlement_id
    secondary_match_keys: amount; date window; platform/vendor; account scope when needed
    fallback_match_strategy: use staged fallback only after primary reference failure
    expected_alignment_type: one_to_one_or_aggregated_by_pattern
    amount_tolerance: 0 unless documented by source-specific rule
    time_tolerance: source-specific date window
    match_confidence_rules: exact reference high; batch/reference medium-high; amount/date fallback medium; sparse native
      low
    unmatched_handling: classify using mismatch_category cards
    notes: This additional matching logic card expands profile-level matching into reusable deterministic key-level patterns.
    evidence_refs:
    - evidence.logistics_kb_doc
    - evidence.cognee_design_v4
    - evidence.unified_edge_scope
    matching_logic_boundary: Defines generic matching behavior, not tenant/group account routing.
```

```yaml
candidate_card:
  card_type: matching_logic
  card_id: matching_logic.logistics.amount_date_courier_window_match
  name: Amount Date Courier Window Match
  fields:
    name: Amount Date Courier Window Match
    description: Fallback match using amount, courier/vendor, account, and date window when references are missing.
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
    logic_name: Amount Date Courier Window Match
    reconciliation_profile_id: applies_to_multiple_logistics_reconciliation_profiles
    matching_strategy: hybrid
    primary_match_keys: amount; date_window; courier_partner; bank_account
    secondary_match_keys: amount; date window; platform/vendor; account scope when needed
    fallback_match_strategy: use staged fallback only after primary reference failure
    expected_alignment_type: one_to_one_or_aggregated_by_pattern
    amount_tolerance: 0 unless documented by source-specific rule
    time_tolerance: source-specific date window
    match_confidence_rules: exact reference high; batch/reference medium-high; amount/date fallback medium; sparse native
      low
    unmatched_handling: classify using mismatch_category cards
    notes: This additional matching logic card expands profile-level matching into reusable deterministic key-level patterns.
    evidence_refs:
    - evidence.logistics_kb_doc
    - evidence.cognee_design_v4
    - evidence.unified_edge_scope
    matching_logic_boundary: Defines generic matching behavior, not tenant/group account routing.
```

```yaml
candidate_card:
  card_type: matching_logic
  card_id: matching_logic.logistics.batch_deduplicated_amount_match
  name: Batch Deduplicated Amount Match
  fields:
    name: Batch Deduplicated Amount Match
    description: Aggregate AWB-level records to settlement batch before matching a bank credit.
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
    logic_name: Batch Deduplicated Amount Match
    reconciliation_profile_id: applies_to_multiple_logistics_reconciliation_profiles
    matching_strategy: aggregated
    primary_match_keys: settlement_id; total_amount_of_batch; utr; bank_reference
    secondary_match_keys: amount; date window; platform/vendor; account scope when needed
    fallback_match_strategy: use staged fallback only after primary reference failure
    expected_alignment_type: one_to_one_or_aggregated_by_pattern
    amount_tolerance: 0 unless documented by source-specific rule
    time_tolerance: source-specific date window
    match_confidence_rules: exact reference high; batch/reference medium-high; amount/date fallback medium; sparse native
      low
    unmatched_handling: classify using mismatch_category cards
    notes: This additional matching logic card expands profile-level matching into reusable deterministic key-level patterns.
    evidence_refs:
    - evidence.logistics_kb_doc
    - evidence.cognee_design_v4
    - evidence.unified_edge_scope
    matching_logic_boundary: Defines generic matching behavior, not tenant/group account routing.
```

```yaml
candidate_card:
  card_type: matching_logic
  card_id: matching_logic.logistics.low_confidence_native_vs_fallback_match
  name: Low Confidence Native vs Fallback Match
  fields:
    name: Low Confidence Native vs Fallback Match
    description: Compare sparse native courier data against documented fallback aggregator evidence.
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
    logic_name: Low Confidence Native vs Fallback Match
    reconciliation_profile_id: applies_to_multiple_logistics_reconciliation_profiles
    matching_strategy: staged
    primary_match_keys: native_awb; fallback_awb; courier_partner; amount
    secondary_match_keys: amount; date window; platform/vendor; account scope when needed
    fallback_match_strategy: use staged fallback only after primary reference failure
    expected_alignment_type: one_to_one_or_aggregated_by_pattern
    amount_tolerance: 0 unless documented by source-specific rule
    time_tolerance: source-specific date window
    match_confidence_rules: exact reference high; batch/reference medium-high; amount/date fallback medium; sparse native
      low
    unmatched_handling: classify using mismatch_category cards
    notes: This additional matching logic card expands profile-level matching into reusable deterministic key-level patterns.
    evidence_refs:
    - evidence.logistics_kb_doc
    - evidence.cognee_design_v4
    - evidence.unified_edge_scope
    matching_logic_boundary: Defines generic matching behavior, not tenant/group account routing.
```

```yaml
candidate_card:
  card_type: matching_logic
  card_id: matching_logic.logistics.component_sum_freight_match
  name: Freight Component Sum Match
  fields:
    name: Freight Component Sum Match
    description: Compare total freight to sum of component charges and tax fields.
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
    logic_name: Freight Component Sum Match
    reconciliation_profile_id: applies_to_multiple_logistics_reconciliation_profiles
    matching_strategy: rule_based
    primary_match_keys: charge_dl; charge_rto; charge_cod; charge_fsc; gst
    secondary_match_keys: amount; date window; platform/vendor; account scope when needed
    fallback_match_strategy: use staged fallback only after primary reference failure
    expected_alignment_type: one_to_one_or_aggregated_by_pattern
    amount_tolerance: 0 unless documented by source-specific rule
    time_tolerance: source-specific date window
    match_confidence_rules: exact reference high; batch/reference medium-high; amount/date fallback medium; sparse native
      low
    unmatched_handling: classify using mismatch_category cards
    notes: This additional matching logic card expands profile-level matching into reusable deterministic key-level patterns.
    evidence_refs:
    - evidence.logistics_kb_doc
    - evidence.cognee_design_v4
    - evidence.unified_edge_scope
    matching_logic_boundary: Defines generic matching behavior, not tenant/group account routing.
```

### 4.20 mismatch_category cards

```yaml
candidate_card:
  card_type: mismatch_category
  card_id: mismatch_category.order_to_shipment.missing_expected
  name: Order to Shipment Reconciliation Missing Expected
  fields:
    name: Order to Shipment Reconciliation Missing Expected
    description: Missing Expected mismatch for Order to Shipment Reconciliation.
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
    category_name: Order to Shipment Reconciliation missing_expected
    category_type: missing_expected
    affected_side: expected_side/actual_side/both_by_case
    business_interpretation: Investigate missing_expected for Order to Shipment Reconciliation.
    severity: medium
    temporary_or_final: depends_on_window
    typical_root_causes: missing load; delayed remittance; wrong key; sparse native data; amount semantics error
    recommended_next_actions: check evidence tables, source statuses, references, date window, and fallback source
    evidence_refs:
    - evidence.logistics_kb_doc
    - evidence.cognee_design_v4
    - evidence.unified_edge_scope
```

```yaml
candidate_card:
  card_type: mismatch_category
  card_id: mismatch_category.order_to_shipment.missing_actual
  name: Order to Shipment Reconciliation Missing Actual
  fields:
    name: Order to Shipment Reconciliation Missing Actual
    description: Missing Actual mismatch for Order to Shipment Reconciliation.
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
    category_name: Order to Shipment Reconciliation missing_actual
    category_type: missing_actual
    affected_side: expected_side/actual_side/both_by_case
    business_interpretation: Investigate missing_actual for Order to Shipment Reconciliation.
    severity: medium
    temporary_or_final: depends_on_window
    typical_root_causes: missing load; delayed remittance; wrong key; sparse native data; amount semantics error
    recommended_next_actions: check evidence tables, source statuses, references, date window, and fallback source
    evidence_refs:
    - evidence.logistics_kb_doc
    - evidence.cognee_design_v4
    - evidence.unified_edge_scope
```

```yaml
candidate_card:
  card_type: mismatch_category
  card_id: mismatch_category.order_to_shipment.amount_mismatch
  name: Order to Shipment Reconciliation Amount Mismatch
  fields:
    name: Order to Shipment Reconciliation Amount Mismatch
    description: Amount Mismatch mismatch for Order to Shipment Reconciliation.
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
    category_name: Order to Shipment Reconciliation amount_mismatch
    category_type: amount_mismatch
    affected_side: expected_side/actual_side/both_by_case
    business_interpretation: Investigate amount_mismatch for Order to Shipment Reconciliation.
    severity: medium
    temporary_or_final: depends_on_window
    typical_root_causes: missing load; delayed remittance; wrong key; sparse native data; amount semantics error
    recommended_next_actions: check evidence tables, source statuses, references, date window, and fallback source
    evidence_refs:
    - evidence.logistics_kb_doc
    - evidence.cognee_design_v4
    - evidence.unified_edge_scope
```

```yaml
candidate_card:
  card_type: mismatch_category
  card_id: mismatch_category.order_to_shipment.timing_mismatch
  name: Order to Shipment Reconciliation Timing Mismatch
  fields:
    name: Order to Shipment Reconciliation Timing Mismatch
    description: Timing Mismatch mismatch for Order to Shipment Reconciliation.
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
    category_name: Order to Shipment Reconciliation timing_mismatch
    category_type: timing_mismatch
    affected_side: expected_side/actual_side/both_by_case
    business_interpretation: Investigate timing_mismatch for Order to Shipment Reconciliation.
    severity: medium
    temporary_or_final: depends_on_window
    typical_root_causes: missing load; delayed remittance; wrong key; sparse native data; amount semantics error
    recommended_next_actions: check evidence tables, source statuses, references, date window, and fallback source
    evidence_refs:
    - evidence.logistics_kb_doc
    - evidence.cognee_design_v4
    - evidence.unified_edge_scope
```

```yaml
candidate_card:
  card_type: mismatch_category
  card_id: mismatch_category.order_to_shipment.duplicate_reference
  name: Order to Shipment Reconciliation Duplicate Reference
  fields:
    name: Order to Shipment Reconciliation Duplicate Reference
    description: Duplicate Reference mismatch for Order to Shipment Reconciliation.
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
    category_name: Order to Shipment Reconciliation duplicate_reference
    category_type: duplicate_reference
    affected_side: expected_side/actual_side/both_by_case
    business_interpretation: Investigate duplicate_reference for Order to Shipment Reconciliation.
    severity: medium
    temporary_or_final: depends_on_window
    typical_root_causes: missing load; delayed remittance; wrong key; sparse native data; amount semantics error
    recommended_next_actions: check evidence tables, source statuses, references, date window, and fallback source
    evidence_refs:
    - evidence.logistics_kb_doc
    - evidence.cognee_design_v4
    - evidence.unified_edge_scope
```

```yaml
candidate_card:
  card_type: mismatch_category
  card_id: mismatch_category.shipment_to_freight_invoice.missing_expected
  name: Shipment to Freight Invoice Reconciliation Missing Expected
  fields:
    name: Shipment to Freight Invoice Reconciliation Missing Expected
    description: Missing Expected mismatch for Shipment to Freight Invoice Reconciliation.
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
    category_name: Shipment to Freight Invoice Reconciliation missing_expected
    category_type: missing_expected
    affected_side: expected_side/actual_side/both_by_case
    business_interpretation: Investigate missing_expected for Shipment to Freight Invoice Reconciliation.
    severity: medium
    temporary_or_final: depends_on_window
    typical_root_causes: missing load; delayed remittance; wrong key; sparse native data; amount semantics error
    recommended_next_actions: check evidence tables, source statuses, references, date window, and fallback source
    evidence_refs:
    - evidence.logistics_kb_doc
    - evidence.cognee_design_v4
    - evidence.unified_edge_scope
```

```yaml
candidate_card:
  card_type: mismatch_category
  card_id: mismatch_category.shipment_to_freight_invoice.missing_actual
  name: Shipment to Freight Invoice Reconciliation Missing Actual
  fields:
    name: Shipment to Freight Invoice Reconciliation Missing Actual
    description: Missing Actual mismatch for Shipment to Freight Invoice Reconciliation.
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
    category_name: Shipment to Freight Invoice Reconciliation missing_actual
    category_type: missing_actual
    affected_side: expected_side/actual_side/both_by_case
    business_interpretation: Investigate missing_actual for Shipment to Freight Invoice Reconciliation.
    severity: medium
    temporary_or_final: depends_on_window
    typical_root_causes: missing load; delayed remittance; wrong key; sparse native data; amount semantics error
    recommended_next_actions: check evidence tables, source statuses, references, date window, and fallback source
    evidence_refs:
    - evidence.logistics_kb_doc
    - evidence.cognee_design_v4
    - evidence.unified_edge_scope
```

```yaml
candidate_card:
  card_type: mismatch_category
  card_id: mismatch_category.shipment_to_freight_invoice.amount_mismatch
  name: Shipment to Freight Invoice Reconciliation Amount Mismatch
  fields:
    name: Shipment to Freight Invoice Reconciliation Amount Mismatch
    description: Amount Mismatch mismatch for Shipment to Freight Invoice Reconciliation.
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
    category_name: Shipment to Freight Invoice Reconciliation amount_mismatch
    category_type: amount_mismatch
    affected_side: expected_side/actual_side/both_by_case
    business_interpretation: Investigate amount_mismatch for Shipment to Freight Invoice Reconciliation.
    severity: medium
    temporary_or_final: depends_on_window
    typical_root_causes: missing load; delayed remittance; wrong key; sparse native data; amount semantics error
    recommended_next_actions: check evidence tables, source statuses, references, date window, and fallback source
    evidence_refs:
    - evidence.logistics_kb_doc
    - evidence.cognee_design_v4
    - evidence.unified_edge_scope
```

```yaml
candidate_card:
  card_type: mismatch_category
  card_id: mismatch_category.shipment_to_freight_invoice.timing_mismatch
  name: Shipment to Freight Invoice Reconciliation Timing Mismatch
  fields:
    name: Shipment to Freight Invoice Reconciliation Timing Mismatch
    description: Timing Mismatch mismatch for Shipment to Freight Invoice Reconciliation.
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
    category_name: Shipment to Freight Invoice Reconciliation timing_mismatch
    category_type: timing_mismatch
    affected_side: expected_side/actual_side/both_by_case
    business_interpretation: Investigate timing_mismatch for Shipment to Freight Invoice Reconciliation.
    severity: medium
    temporary_or_final: depends_on_window
    typical_root_causes: missing load; delayed remittance; wrong key; sparse native data; amount semantics error
    recommended_next_actions: check evidence tables, source statuses, references, date window, and fallback source
    evidence_refs:
    - evidence.logistics_kb_doc
    - evidence.cognee_design_v4
    - evidence.unified_edge_scope
```

```yaml
candidate_card:
  card_type: mismatch_category
  card_id: mismatch_category.shipment_to_freight_invoice.duplicate_reference
  name: Shipment to Freight Invoice Reconciliation Duplicate Reference
  fields:
    name: Shipment to Freight Invoice Reconciliation Duplicate Reference
    description: Duplicate Reference mismatch for Shipment to Freight Invoice Reconciliation.
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
    category_name: Shipment to Freight Invoice Reconciliation duplicate_reference
    category_type: duplicate_reference
    affected_side: expected_side/actual_side/both_by_case
    business_interpretation: Investigate duplicate_reference for Shipment to Freight Invoice Reconciliation.
    severity: medium
    temporary_or_final: depends_on_window
    typical_root_causes: missing load; delayed remittance; wrong key; sparse native data; amount semantics error
    recommended_next_actions: check evidence tables, source statuses, references, date window, and fallback source
    evidence_refs:
    - evidence.logistics_kb_doc
    - evidence.cognee_design_v4
    - evidence.unified_edge_scope
```

```yaml
candidate_card:
  card_type: mismatch_category
  card_id: mismatch_category.freight_charge_validation.missing_expected
  name: Freight Charge Validation Missing Expected
  fields:
    name: Freight Charge Validation Missing Expected
    description: Missing Expected mismatch for Freight Charge Validation.
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
    category_name: Freight Charge Validation missing_expected
    category_type: missing_expected
    affected_side: expected_side/actual_side/both_by_case
    business_interpretation: Investigate missing_expected for Freight Charge Validation.
    severity: medium
    temporary_or_final: depends_on_window
    typical_root_causes: missing load; delayed remittance; wrong key; sparse native data; amount semantics error
    recommended_next_actions: check evidence tables, source statuses, references, date window, and fallback source
    evidence_refs:
    - evidence.logistics_kb_doc
    - evidence.cognee_design_v4
    - evidence.unified_edge_scope
```

```yaml
candidate_card:
  card_type: mismatch_category
  card_id: mismatch_category.freight_charge_validation.missing_actual
  name: Freight Charge Validation Missing Actual
  fields:
    name: Freight Charge Validation Missing Actual
    description: Missing Actual mismatch for Freight Charge Validation.
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
    category_name: Freight Charge Validation missing_actual
    category_type: missing_actual
    affected_side: expected_side/actual_side/both_by_case
    business_interpretation: Investigate missing_actual for Freight Charge Validation.
    severity: medium
    temporary_or_final: depends_on_window
    typical_root_causes: missing load; delayed remittance; wrong key; sparse native data; amount semantics error
    recommended_next_actions: check evidence tables, source statuses, references, date window, and fallback source
    evidence_refs:
    - evidence.logistics_kb_doc
    - evidence.cognee_design_v4
    - evidence.unified_edge_scope
```

```yaml
candidate_card:
  card_type: mismatch_category
  card_id: mismatch_category.freight_charge_validation.amount_mismatch
  name: Freight Charge Validation Amount Mismatch
  fields:
    name: Freight Charge Validation Amount Mismatch
    description: Amount Mismatch mismatch for Freight Charge Validation.
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
    category_name: Freight Charge Validation amount_mismatch
    category_type: amount_mismatch
    affected_side: expected_side/actual_side/both_by_case
    business_interpretation: Investigate amount_mismatch for Freight Charge Validation.
    severity: medium
    temporary_or_final: depends_on_window
    typical_root_causes: missing load; delayed remittance; wrong key; sparse native data; amount semantics error
    recommended_next_actions: check evidence tables, source statuses, references, date window, and fallback source
    evidence_refs:
    - evidence.logistics_kb_doc
    - evidence.cognee_design_v4
    - evidence.unified_edge_scope
```

```yaml
candidate_card:
  card_type: mismatch_category
  card_id: mismatch_category.freight_charge_validation.timing_mismatch
  name: Freight Charge Validation Timing Mismatch
  fields:
    name: Freight Charge Validation Timing Mismatch
    description: Timing Mismatch mismatch for Freight Charge Validation.
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
    category_name: Freight Charge Validation timing_mismatch
    category_type: timing_mismatch
    affected_side: expected_side/actual_side/both_by_case
    business_interpretation: Investigate timing_mismatch for Freight Charge Validation.
    severity: medium
    temporary_or_final: depends_on_window
    typical_root_causes: missing load; delayed remittance; wrong key; sparse native data; amount semantics error
    recommended_next_actions: check evidence tables, source statuses, references, date window, and fallback source
    evidence_refs:
    - evidence.logistics_kb_doc
    - evidence.cognee_design_v4
    - evidence.unified_edge_scope
```

```yaml
candidate_card:
  card_type: mismatch_category
  card_id: mismatch_category.freight_charge_validation.duplicate_reference
  name: Freight Charge Validation Duplicate Reference
  fields:
    name: Freight Charge Validation Duplicate Reference
    description: Duplicate Reference mismatch for Freight Charge Validation.
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
    category_name: Freight Charge Validation duplicate_reference
    category_type: duplicate_reference
    affected_side: expected_side/actual_side/both_by_case
    business_interpretation: Investigate duplicate_reference for Freight Charge Validation.
    severity: medium
    temporary_or_final: depends_on_window
    typical_root_causes: missing load; delayed remittance; wrong key; sparse native data; amount semantics error
    recommended_next_actions: check evidence tables, source statuses, references, date window, and fallback source
    evidence_refs:
    - evidence.logistics_kb_doc
    - evidence.cognee_design_v4
    - evidence.unified_edge_scope
```

```yaml
candidate_card:
  card_type: mismatch_category
  card_id: mismatch_category.cod_expected_to_courier_remittance.missing_expected
  name: COD Expected to Courier Remittance Reconciliation Missing Expected
  fields:
    name: COD Expected to Courier Remittance Reconciliation Missing Expected
    description: Missing Expected mismatch for COD Expected to Courier Remittance Reconciliation.
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
    category_name: COD Expected to Courier Remittance Reconciliation missing_expected
    category_type: missing_expected
    affected_side: expected_side/actual_side/both_by_case
    business_interpretation: Investigate missing_expected for COD Expected to Courier Remittance Reconciliation.
    severity: medium
    temporary_or_final: depends_on_window
    typical_root_causes: missing load; delayed remittance; wrong key; sparse native data; amount semantics error
    recommended_next_actions: check evidence tables, source statuses, references, date window, and fallback source
    evidence_refs:
    - evidence.logistics_kb_doc
    - evidence.cognee_design_v4
    - evidence.unified_edge_scope
```

```yaml
candidate_card:
  card_type: mismatch_category
  card_id: mismatch_category.cod_expected_to_courier_remittance.missing_actual
  name: COD Expected to Courier Remittance Reconciliation Missing Actual
  fields:
    name: COD Expected to Courier Remittance Reconciliation Missing Actual
    description: Missing Actual mismatch for COD Expected to Courier Remittance Reconciliation.
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
    category_name: COD Expected to Courier Remittance Reconciliation missing_actual
    category_type: missing_actual
    affected_side: expected_side/actual_side/both_by_case
    business_interpretation: Investigate missing_actual for COD Expected to Courier Remittance Reconciliation.
    severity: medium
    temporary_or_final: depends_on_window
    typical_root_causes: missing load; delayed remittance; wrong key; sparse native data; amount semantics error
    recommended_next_actions: check evidence tables, source statuses, references, date window, and fallback source
    evidence_refs:
    - evidence.logistics_kb_doc
    - evidence.cognee_design_v4
    - evidence.unified_edge_scope
```

```yaml
candidate_card:
  card_type: mismatch_category
  card_id: mismatch_category.cod_expected_to_courier_remittance.amount_mismatch
  name: COD Expected to Courier Remittance Reconciliation Amount Mismatch
  fields:
    name: COD Expected to Courier Remittance Reconciliation Amount Mismatch
    description: Amount Mismatch mismatch for COD Expected to Courier Remittance Reconciliation.
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
    category_name: COD Expected to Courier Remittance Reconciliation amount_mismatch
    category_type: amount_mismatch
    affected_side: expected_side/actual_side/both_by_case
    business_interpretation: Investigate amount_mismatch for COD Expected to Courier Remittance Reconciliation.
    severity: medium
    temporary_or_final: depends_on_window
    typical_root_causes: missing load; delayed remittance; wrong key; sparse native data; amount semantics error
    recommended_next_actions: check evidence tables, source statuses, references, date window, and fallback source
    evidence_refs:
    - evidence.logistics_kb_doc
    - evidence.cognee_design_v4
    - evidence.unified_edge_scope
```

```yaml
candidate_card:
  card_type: mismatch_category
  card_id: mismatch_category.cod_expected_to_courier_remittance.timing_mismatch
  name: COD Expected to Courier Remittance Reconciliation Timing Mismatch
  fields:
    name: COD Expected to Courier Remittance Reconciliation Timing Mismatch
    description: Timing Mismatch mismatch for COD Expected to Courier Remittance Reconciliation.
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
    category_name: COD Expected to Courier Remittance Reconciliation timing_mismatch
    category_type: timing_mismatch
    affected_side: expected_side/actual_side/both_by_case
    business_interpretation: Investigate timing_mismatch for COD Expected to Courier Remittance Reconciliation.
    severity: medium
    temporary_or_final: depends_on_window
    typical_root_causes: missing load; delayed remittance; wrong key; sparse native data; amount semantics error
    recommended_next_actions: check evidence tables, source statuses, references, date window, and fallback source
    evidence_refs:
    - evidence.logistics_kb_doc
    - evidence.cognee_design_v4
    - evidence.unified_edge_scope
```

```yaml
candidate_card:
  card_type: mismatch_category
  card_id: mismatch_category.cod_expected_to_courier_remittance.duplicate_reference
  name: COD Expected to Courier Remittance Reconciliation Duplicate Reference
  fields:
    name: COD Expected to Courier Remittance Reconciliation Duplicate Reference
    description: Duplicate Reference mismatch for COD Expected to Courier Remittance Reconciliation.
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
    category_name: COD Expected to Courier Remittance Reconciliation duplicate_reference
    category_type: duplicate_reference
    affected_side: expected_side/actual_side/both_by_case
    business_interpretation: Investigate duplicate_reference for COD Expected to Courier Remittance Reconciliation.
    severity: medium
    temporary_or_final: depends_on_window
    typical_root_causes: missing load; delayed remittance; wrong key; sparse native data; amount semantics error
    recommended_next_actions: check evidence tables, source statuses, references, date window, and fallback source
    evidence_refs:
    - evidence.logistics_kb_doc
    - evidence.cognee_design_v4
    - evidence.unified_edge_scope
```

```yaml
candidate_card:
  card_type: mismatch_category
  card_id: mismatch_category.courier_batch_to_bank_credit.missing_expected
  name: Courier Batch to Bank Credit Reconciliation Missing Expected
  fields:
    name: Courier Batch to Bank Credit Reconciliation Missing Expected
    description: Missing Expected mismatch for Courier Batch to Bank Credit Reconciliation.
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
    category_name: Courier Batch to Bank Credit Reconciliation missing_expected
    category_type: missing_expected
    affected_side: expected_side/actual_side/both_by_case
    business_interpretation: Investigate missing_expected for Courier Batch to Bank Credit Reconciliation.
    severity: medium
    temporary_or_final: depends_on_window
    typical_root_causes: missing load; delayed remittance; wrong key; sparse native data; amount semantics error
    recommended_next_actions: check evidence tables, source statuses, references, date window, and fallback source
    evidence_refs:
    - evidence.logistics_kb_doc
    - evidence.cognee_design_v4
    - evidence.unified_edge_scope
```

```yaml
candidate_card:
  card_type: mismatch_category
  card_id: mismatch_category.courier_batch_to_bank_credit.missing_actual
  name: Courier Batch to Bank Credit Reconciliation Missing Actual
  fields:
    name: Courier Batch to Bank Credit Reconciliation Missing Actual
    description: Missing Actual mismatch for Courier Batch to Bank Credit Reconciliation.
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
    category_name: Courier Batch to Bank Credit Reconciliation missing_actual
    category_type: missing_actual
    affected_side: expected_side/actual_side/both_by_case
    business_interpretation: Investigate missing_actual for Courier Batch to Bank Credit Reconciliation.
    severity: medium
    temporary_or_final: depends_on_window
    typical_root_causes: missing load; delayed remittance; wrong key; sparse native data; amount semantics error
    recommended_next_actions: check evidence tables, source statuses, references, date window, and fallback source
    evidence_refs:
    - evidence.logistics_kb_doc
    - evidence.cognee_design_v4
    - evidence.unified_edge_scope
```

```yaml
candidate_card:
  card_type: mismatch_category
  card_id: mismatch_category.courier_batch_to_bank_credit.amount_mismatch
  name: Courier Batch to Bank Credit Reconciliation Amount Mismatch
  fields:
    name: Courier Batch to Bank Credit Reconciliation Amount Mismatch
    description: Amount Mismatch mismatch for Courier Batch to Bank Credit Reconciliation.
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
    category_name: Courier Batch to Bank Credit Reconciliation amount_mismatch
    category_type: amount_mismatch
    affected_side: expected_side/actual_side/both_by_case
    business_interpretation: Investigate amount_mismatch for Courier Batch to Bank Credit Reconciliation.
    severity: medium
    temporary_or_final: depends_on_window
    typical_root_causes: missing load; delayed remittance; wrong key; sparse native data; amount semantics error
    recommended_next_actions: check evidence tables, source statuses, references, date window, and fallback source
    evidence_refs:
    - evidence.logistics_kb_doc
    - evidence.cognee_design_v4
    - evidence.unified_edge_scope
```

```yaml
candidate_card:
  card_type: mismatch_category
  card_id: mismatch_category.courier_batch_to_bank_credit.timing_mismatch
  name: Courier Batch to Bank Credit Reconciliation Timing Mismatch
  fields:
    name: Courier Batch to Bank Credit Reconciliation Timing Mismatch
    description: Timing Mismatch mismatch for Courier Batch to Bank Credit Reconciliation.
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
    category_name: Courier Batch to Bank Credit Reconciliation timing_mismatch
    category_type: timing_mismatch
    affected_side: expected_side/actual_side/both_by_case
    business_interpretation: Investigate timing_mismatch for Courier Batch to Bank Credit Reconciliation.
    severity: medium
    temporary_or_final: depends_on_window
    typical_root_causes: missing load; delayed remittance; wrong key; sparse native data; amount semantics error
    recommended_next_actions: check evidence tables, source statuses, references, date window, and fallback source
    evidence_refs:
    - evidence.logistics_kb_doc
    - evidence.cognee_design_v4
    - evidence.unified_edge_scope
```

```yaml
candidate_card:
  card_type: mismatch_category
  card_id: mismatch_category.courier_batch_to_bank_credit.duplicate_reference
  name: Courier Batch to Bank Credit Reconciliation Duplicate Reference
  fields:
    name: Courier Batch to Bank Credit Reconciliation Duplicate Reference
    description: Duplicate Reference mismatch for Courier Batch to Bank Credit Reconciliation.
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
    category_name: Courier Batch to Bank Credit Reconciliation duplicate_reference
    category_type: duplicate_reference
    affected_side: expected_side/actual_side/both_by_case
    business_interpretation: Investigate duplicate_reference for Courier Batch to Bank Credit Reconciliation.
    severity: medium
    temporary_or_final: depends_on_window
    typical_root_causes: missing load; delayed remittance; wrong key; sparse native data; amount semantics error
    recommended_next_actions: check evidence tables, source statuses, references, date window, and fallback source
    evidence_refs:
    - evidence.logistics_kb_doc
    - evidence.cognee_design_v4
    - evidence.unified_edge_scope
```

```yaml
candidate_card:
  card_type: mismatch_category
  card_id: mismatch_category.prepaid_pos_logistics_settlement.missing_expected
  name: Prepaid/POS Logistics Settlement Reconciliation Missing Expected
  fields:
    name: Prepaid/POS Logistics Settlement Reconciliation Missing Expected
    description: Missing Expected mismatch for Prepaid/POS Logistics Settlement Reconciliation.
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
    category_name: Prepaid/POS Logistics Settlement Reconciliation missing_expected
    category_type: missing_expected
    affected_side: expected_side/actual_side/both_by_case
    business_interpretation: Investigate missing_expected for Prepaid/POS Logistics Settlement Reconciliation.
    severity: medium
    temporary_or_final: depends_on_window
    typical_root_causes: missing load; delayed remittance; wrong key; sparse native data; amount semantics error
    recommended_next_actions: check evidence tables, source statuses, references, date window, and fallback source
    evidence_refs:
    - evidence.logistics_kb_doc
    - evidence.cognee_design_v4
    - evidence.unified_edge_scope
```

```yaml
candidate_card:
  card_type: mismatch_category
  card_id: mismatch_category.prepaid_pos_logistics_settlement.missing_actual
  name: Prepaid/POS Logistics Settlement Reconciliation Missing Actual
  fields:
    name: Prepaid/POS Logistics Settlement Reconciliation Missing Actual
    description: Missing Actual mismatch for Prepaid/POS Logistics Settlement Reconciliation.
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
    category_name: Prepaid/POS Logistics Settlement Reconciliation missing_actual
    category_type: missing_actual
    affected_side: expected_side/actual_side/both_by_case
    business_interpretation: Investigate missing_actual for Prepaid/POS Logistics Settlement Reconciliation.
    severity: medium
    temporary_or_final: depends_on_window
    typical_root_causes: missing load; delayed remittance; wrong key; sparse native data; amount semantics error
    recommended_next_actions: check evidence tables, source statuses, references, date window, and fallback source
    evidence_refs:
    - evidence.logistics_kb_doc
    - evidence.cognee_design_v4
    - evidence.unified_edge_scope
```

```yaml
candidate_card:
  card_type: mismatch_category
  card_id: mismatch_category.prepaid_pos_logistics_settlement.amount_mismatch
  name: Prepaid/POS Logistics Settlement Reconciliation Amount Mismatch
  fields:
    name: Prepaid/POS Logistics Settlement Reconciliation Amount Mismatch
    description: Amount Mismatch mismatch for Prepaid/POS Logistics Settlement Reconciliation.
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
    category_name: Prepaid/POS Logistics Settlement Reconciliation amount_mismatch
    category_type: amount_mismatch
    affected_side: expected_side/actual_side/both_by_case
    business_interpretation: Investigate amount_mismatch for Prepaid/POS Logistics Settlement Reconciliation.
    severity: medium
    temporary_or_final: depends_on_window
    typical_root_causes: missing load; delayed remittance; wrong key; sparse native data; amount semantics error
    recommended_next_actions: check evidence tables, source statuses, references, date window, and fallback source
    evidence_refs:
    - evidence.logistics_kb_doc
    - evidence.cognee_design_v4
    - evidence.unified_edge_scope
```

```yaml
candidate_card:
  card_type: mismatch_category
  card_id: mismatch_category.prepaid_pos_logistics_settlement.timing_mismatch
  name: Prepaid/POS Logistics Settlement Reconciliation Timing Mismatch
  fields:
    name: Prepaid/POS Logistics Settlement Reconciliation Timing Mismatch
    description: Timing Mismatch mismatch for Prepaid/POS Logistics Settlement Reconciliation.
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
    category_name: Prepaid/POS Logistics Settlement Reconciliation timing_mismatch
    category_type: timing_mismatch
    affected_side: expected_side/actual_side/both_by_case
    business_interpretation: Investigate timing_mismatch for Prepaid/POS Logistics Settlement Reconciliation.
    severity: medium
    temporary_or_final: depends_on_window
    typical_root_causes: missing load; delayed remittance; wrong key; sparse native data; amount semantics error
    recommended_next_actions: check evidence tables, source statuses, references, date window, and fallback source
    evidence_refs:
    - evidence.logistics_kb_doc
    - evidence.cognee_design_v4
    - evidence.unified_edge_scope
```

```yaml
candidate_card:
  card_type: mismatch_category
  card_id: mismatch_category.prepaid_pos_logistics_settlement.duplicate_reference
  name: Prepaid/POS Logistics Settlement Reconciliation Duplicate Reference
  fields:
    name: Prepaid/POS Logistics Settlement Reconciliation Duplicate Reference
    description: Duplicate Reference mismatch for Prepaid/POS Logistics Settlement Reconciliation.
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
    category_name: Prepaid/POS Logistics Settlement Reconciliation duplicate_reference
    category_type: duplicate_reference
    affected_side: expected_side/actual_side/both_by_case
    business_interpretation: Investigate duplicate_reference for Prepaid/POS Logistics Settlement Reconciliation.
    severity: medium
    temporary_or_final: depends_on_window
    typical_root_causes: missing load; delayed remittance; wrong key; sparse native data; amount semantics error
    recommended_next_actions: check evidence tables, source statuses, references, date window, and fallback source
    evidence_refs:
    - evidence.logistics_kb_doc
    - evidence.cognee_design_v4
    - evidence.unified_edge_scope
```

```yaml
candidate_card:
  card_type: mismatch_category
  card_id: mismatch_category.low_confidence_native_to_fallback.missing_expected
  name: Low Confidence Native to Fallback Validation Missing Expected
  fields:
    name: Low Confidence Native to Fallback Validation Missing Expected
    description: Missing Expected mismatch for Low Confidence Native to Fallback Validation.
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
    category_name: Low Confidence Native to Fallback Validation missing_expected
    category_type: missing_expected
    affected_side: expected_side/actual_side/both_by_case
    business_interpretation: Investigate missing_expected for Low Confidence Native to Fallback Validation.
    severity: medium
    temporary_or_final: depends_on_window
    typical_root_causes: missing load; delayed remittance; wrong key; sparse native data; amount semantics error
    recommended_next_actions: check evidence tables, source statuses, references, date window, and fallback source
    evidence_refs:
    - evidence.logistics_kb_doc
    - evidence.cognee_design_v4
    - evidence.unified_edge_scope
```

```yaml
candidate_card:
  card_type: mismatch_category
  card_id: mismatch_category.low_confidence_native_to_fallback.missing_actual
  name: Low Confidence Native to Fallback Validation Missing Actual
  fields:
    name: Low Confidence Native to Fallback Validation Missing Actual
    description: Missing Actual mismatch for Low Confidence Native to Fallback Validation.
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
    category_name: Low Confidence Native to Fallback Validation missing_actual
    category_type: missing_actual
    affected_side: expected_side/actual_side/both_by_case
    business_interpretation: Investigate missing_actual for Low Confidence Native to Fallback Validation.
    severity: medium
    temporary_or_final: depends_on_window
    typical_root_causes: missing load; delayed remittance; wrong key; sparse native data; amount semantics error
    recommended_next_actions: check evidence tables, source statuses, references, date window, and fallback source
    evidence_refs:
    - evidence.logistics_kb_doc
    - evidence.cognee_design_v4
    - evidence.unified_edge_scope
```

```yaml
candidate_card:
  card_type: mismatch_category
  card_id: mismatch_category.low_confidence_native_to_fallback.amount_mismatch
  name: Low Confidence Native to Fallback Validation Amount Mismatch
  fields:
    name: Low Confidence Native to Fallback Validation Amount Mismatch
    description: Amount Mismatch mismatch for Low Confidence Native to Fallback Validation.
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
    category_name: Low Confidence Native to Fallback Validation amount_mismatch
    category_type: amount_mismatch
    affected_side: expected_side/actual_side/both_by_case
    business_interpretation: Investigate amount_mismatch for Low Confidence Native to Fallback Validation.
    severity: medium
    temporary_or_final: depends_on_window
    typical_root_causes: missing load; delayed remittance; wrong key; sparse native data; amount semantics error
    recommended_next_actions: check evidence tables, source statuses, references, date window, and fallback source
    evidence_refs:
    - evidence.logistics_kb_doc
    - evidence.cognee_design_v4
    - evidence.unified_edge_scope
```

```yaml
candidate_card:
  card_type: mismatch_category
  card_id: mismatch_category.low_confidence_native_to_fallback.timing_mismatch
  name: Low Confidence Native to Fallback Validation Timing Mismatch
  fields:
    name: Low Confidence Native to Fallback Validation Timing Mismatch
    description: Timing Mismatch mismatch for Low Confidence Native to Fallback Validation.
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
    category_name: Low Confidence Native to Fallback Validation timing_mismatch
    category_type: timing_mismatch
    affected_side: expected_side/actual_side/both_by_case
    business_interpretation: Investigate timing_mismatch for Low Confidence Native to Fallback Validation.
    severity: medium
    temporary_or_final: depends_on_window
    typical_root_causes: missing load; delayed remittance; wrong key; sparse native data; amount semantics error
    recommended_next_actions: check evidence tables, source statuses, references, date window, and fallback source
    evidence_refs:
    - evidence.logistics_kb_doc
    - evidence.cognee_design_v4
    - evidence.unified_edge_scope
```

```yaml
candidate_card:
  card_type: mismatch_category
  card_id: mismatch_category.low_confidence_native_to_fallback.duplicate_reference
  name: Low Confidence Native to Fallback Validation Duplicate Reference
  fields:
    name: Low Confidence Native to Fallback Validation Duplicate Reference
    description: Duplicate Reference mismatch for Low Confidence Native to Fallback Validation.
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
    category_name: Low Confidence Native to Fallback Validation duplicate_reference
    category_type: duplicate_reference
    affected_side: expected_side/actual_side/both_by_case
    business_interpretation: Investigate duplicate_reference for Low Confidence Native to Fallback Validation.
    severity: medium
    temporary_or_final: depends_on_window
    typical_root_causes: missing load; delayed remittance; wrong key; sparse native data; amount semantics error
    recommended_next_actions: check evidence tables, source statuses, references, date window, and fallback source
    evidence_refs:
    - evidence.logistics_kb_doc
    - evidence.cognee_design_v4
    - evidence.unified_edge_scope
```

```yaml
candidate_card:
  card_type: mismatch_category
  card_id: mismatch_category.delivered_cod_not_remitted
  name: Delivered Cod Not Remitted
  fields:
    name: Delivered Cod Not Remitted
    description: 'Logistics mismatch category: delivered_cod_not_remitted.'
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
    category_name: delivered_cod_not_remitted
    category_type: logistics_specific
    affected_side: expected_side/actual_side/both
    business_interpretation: delivered cod not remitted
    severity: medium_to_high_by_context
    temporary_or_final: depends_on_window
    typical_root_causes: data delay; wrong grain; source sparsity; operational exception
    recommended_next_actions: inspect source-specific evidence, fallback path, amount semantics, and status/value profiles
    evidence_refs:
    - evidence.logistics_kb_doc
    - evidence.cognee_design_v4
    - evidence.unified_edge_scope
```

```yaml
candidate_card:
  card_type: mismatch_category
  card_id: mismatch_category.shipment_missing_invoice
  name: Shipment Missing Invoice
  fields:
    name: Shipment Missing Invoice
    description: 'Logistics mismatch category: shipment_missing_invoice.'
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
    category_name: shipment_missing_invoice
    category_type: logistics_specific
    affected_side: expected_side/actual_side/both
    business_interpretation: shipment missing invoice
    severity: medium_to_high_by_context
    temporary_or_final: depends_on_window
    typical_root_causes: data delay; wrong grain; source sparsity; operational exception
    recommended_next_actions: inspect source-specific evidence, fallback path, amount semantics, and status/value profiles
    evidence_refs:
    - evidence.logistics_kb_doc
    - evidence.cognee_design_v4
    - evidence.unified_edge_scope
```

```yaml
candidate_card:
  card_type: mismatch_category
  card_id: mismatch_category.invoice_without_shipment
  name: Invoice Without Shipment
  fields:
    name: Invoice Without Shipment
    description: 'Logistics mismatch category: invoice_without_shipment.'
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
    category_name: invoice_without_shipment
    category_type: logistics_specific
    affected_side: expected_side/actual_side/both
    business_interpretation: invoice without shipment
    severity: medium_to_high_by_context
    temporary_or_final: depends_on_window
    typical_root_causes: data delay; wrong grain; source sparsity; operational exception
    recommended_next_actions: inspect source-specific evidence, fallback path, amount semantics, and status/value profiles
    evidence_refs:
    - evidence.logistics_kb_doc
    - evidence.cognee_design_v4
    - evidence.unified_edge_scope
```

```yaml
candidate_card:
  card_type: mismatch_category
  card_id: mismatch_category.freight_overcharge
  name: Freight Overcharge
  fields:
    name: Freight Overcharge
    description: 'Logistics mismatch category: freight_overcharge.'
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
    category_name: freight_overcharge
    category_type: logistics_specific
    affected_side: expected_side/actual_side/both
    business_interpretation: freight overcharge
    severity: medium_to_high_by_context
    temporary_or_final: depends_on_window
    typical_root_causes: data delay; wrong grain; source sparsity; operational exception
    recommended_next_actions: inspect source-specific evidence, fallback path, amount semantics, and status/value profiles
    evidence_refs:
    - evidence.logistics_kb_doc
    - evidence.cognee_design_v4
    - evidence.unified_edge_scope
```

```yaml
candidate_card:
  card_type: mismatch_category
  card_id: mismatch_category.cod_charge_on_prepaid
  name: Cod Charge On Prepaid
  fields:
    name: Cod Charge On Prepaid
    description: 'Logistics mismatch category: cod_charge_on_prepaid.'
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
    category_name: cod_charge_on_prepaid
    category_type: logistics_specific
    affected_side: expected_side/actual_side/both
    business_interpretation: cod charge on prepaid
    severity: medium_to_high_by_context
    temporary_or_final: depends_on_window
    typical_root_causes: data delay; wrong grain; source sparsity; operational exception
    recommended_next_actions: inspect source-specific evidence, fallback path, amount semantics, and status/value profiles
    evidence_refs:
    - evidence.logistics_kb_doc
    - evidence.cognee_design_v4
    - evidence.unified_edge_scope
```

```yaml
candidate_card:
  card_type: mismatch_category
  card_id: mismatch_category.unexpected_rto_charge
  name: Unexpected Rto Charge
  fields:
    name: Unexpected Rto Charge
    description: 'Logistics mismatch category: unexpected_rto_charge.'
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
    category_name: unexpected_rto_charge
    category_type: logistics_specific
    affected_side: expected_side/actual_side/both
    business_interpretation: unexpected rto charge
    severity: medium_to_high_by_context
    temporary_or_final: depends_on_window
    typical_root_causes: data delay; wrong grain; source sparsity; operational exception
    recommended_next_actions: inspect source-specific evidence, fallback path, amount semantics, and status/value profiles
    evidence_refs:
    - evidence.logistics_kb_doc
    - evidence.cognee_design_v4
    - evidence.unified_edge_scope
```

```yaml
candidate_card:
  card_type: mismatch_category
  card_id: mismatch_category.wrong_courier_partner
  name: Wrong Courier Partner
  fields:
    name: Wrong Courier Partner
    description: 'Logistics mismatch category: wrong_courier_partner.'
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
    category_name: wrong_courier_partner
    category_type: logistics_specific
    affected_side: expected_side/actual_side/both
    business_interpretation: wrong courier partner
    severity: medium_to_high_by_context
    temporary_or_final: depends_on_window
    typical_root_causes: data delay; wrong grain; source sparsity; operational exception
    recommended_next_actions: inspect source-specific evidence, fallback path, amount semantics, and status/value profiles
    evidence_refs:
    - evidence.logistics_kb_doc
    - evidence.cognee_design_v4
    - evidence.unified_edge_scope
```

```yaml
candidate_card:
  card_type: mismatch_category
  card_id: mismatch_category.wrong_zone_or_weight
  name: Wrong Zone Or Weight
  fields:
    name: Wrong Zone Or Weight
    description: 'Logistics mismatch category: wrong_zone_or_weight.'
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
    category_name: wrong_zone_or_weight
    category_type: logistics_specific
    affected_side: expected_side/actual_side/both
    business_interpretation: wrong zone or weight
    severity: medium_to_high_by_context
    temporary_or_final: depends_on_window
    typical_root_causes: data delay; wrong grain; source sparsity; operational exception
    recommended_next_actions: inspect source-specific evidence, fallback path, amount semantics, and status/value profiles
    evidence_refs:
    - evidence.logistics_kb_doc
    - evidence.cognee_design_v4
    - evidence.unified_edge_scope
```

```yaml
candidate_card:
  card_type: mismatch_category
  card_id: mismatch_category.missing_or_malformed_utr
  name: Missing Or Malformed Utr
  fields:
    name: Missing Or Malformed Utr
    description: 'Logistics mismatch category: missing_or_malformed_utr.'
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
    category_name: missing_or_malformed_utr
    category_type: logistics_specific
    affected_side: expected_side/actual_side/both
    business_interpretation: missing or malformed utr
    severity: medium_to_high_by_context
    temporary_or_final: depends_on_window
    typical_root_causes: data delay; wrong grain; source sparsity; operational exception
    recommended_next_actions: inspect source-specific evidence, fallback path, amount semantics, and status/value profiles
    evidence_refs:
    - evidence.logistics_kb_doc
    - evidence.cognee_design_v4
    - evidence.unified_edge_scope
```

```yaml
candidate_card:
  card_type: mismatch_category
  card_id: mismatch_category.batch_amount_differs_from_awb_sum
  name: Batch Amount Differs From Awb Sum
  fields:
    name: Batch Amount Differs From Awb Sum
    description: 'Logistics mismatch category: batch_amount_differs_from_awb_sum.'
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
    category_name: batch_amount_differs_from_awb_sum
    category_type: logistics_specific
    affected_side: expected_side/actual_side/both
    business_interpretation: batch amount differs from awb sum
    severity: medium_to_high_by_context
    temporary_or_final: depends_on_window
    typical_root_causes: data delay; wrong grain; source sparsity; operational exception
    recommended_next_actions: inspect source-specific evidence, fallback path, amount semantics, and status/value profiles
    evidence_refs:
    - evidence.logistics_kb_doc
    - evidence.cognee_design_v4
    - evidence.unified_edge_scope
```

```yaml
candidate_card:
  card_type: mismatch_category
  card_id: mismatch_category.split_bank_credit
  name: Split Bank Credit
  fields:
    name: Split Bank Credit
    description: 'Logistics mismatch category: split_bank_credit.'
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
    category_name: split_bank_credit
    category_type: logistics_specific
    affected_side: expected_side/actual_side/both
    business_interpretation: split bank credit
    severity: medium_to_high_by_context
    temporary_or_final: depends_on_window
    typical_root_causes: data delay; wrong grain; source sparsity; operational exception
    recommended_next_actions: inspect source-specific evidence, fallback path, amount semantics, and status/value profiles
    evidence_refs:
    - evidence.logistics_kb_doc
    - evidence.cognee_design_v4
    - evidence.unified_edge_scope
```

```yaml
candidate_card:
  card_type: mismatch_category
  card_id: mismatch_category.merged_bank_credit
  name: Merged Bank Credit
  fields:
    name: Merged Bank Credit
    description: 'Logistics mismatch category: merged_bank_credit.'
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
    category_name: merged_bank_credit
    category_type: logistics_specific
    affected_side: expected_side/actual_side/both
    business_interpretation: merged bank credit
    severity: medium_to_high_by_context
    temporary_or_final: depends_on_window
    typical_root_causes: data delay; wrong grain; source sparsity; operational exception
    recommended_next_actions: inspect source-specific evidence, fallback path, amount semantics, and status/value profiles
    evidence_refs:
    - evidence.logistics_kb_doc
    - evidence.cognee_design_v4
    - evidence.unified_edge_scope
```

```yaml
candidate_card:
  card_type: mismatch_category
  card_id: mismatch_category.native_table_sparse
  name: Native Table Sparse
  fields:
    name: Native Table Sparse
    description: 'Logistics mismatch category: native_table_sparse.'
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
    category_name: native_table_sparse
    category_type: logistics_specific
    affected_side: expected_side/actual_side/both
    business_interpretation: native table sparse
    severity: medium_to_high_by_context
    temporary_or_final: depends_on_window
    typical_root_causes: data delay; wrong grain; source sparsity; operational exception
    recommended_next_actions: inspect source-specific evidence, fallback path, amount semantics, and status/value profiles
    evidence_refs:
    - evidence.logistics_kb_doc
    - evidence.cognee_design_v4
    - evidence.unified_edge_scope
```

```yaml
candidate_card:
  card_type: mismatch_category
  card_id: mismatch_category.fallback_source_preferred
  name: Fallback Source Preferred
  fields:
    name: Fallback Source Preferred
    description: 'Logistics mismatch category: fallback_source_preferred.'
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
    category_name: fallback_source_preferred
    category_type: logistics_specific
    affected_side: expected_side/actual_side/both
    business_interpretation: fallback source preferred
    severity: medium_to_high_by_context
    temporary_or_final: depends_on_window
    typical_root_causes: data delay; wrong grain; source sparsity; operational exception
    recommended_next_actions: inspect source-specific evidence, fallback path, amount semantics, and status/value profiles
    evidence_refs:
    - evidence.logistics_kb_doc
    - evidence.cognee_design_v4
    - evidence.unified_edge_scope
```

### 4.21 reconciliation_variant cards

```yaml
candidate_card:
  card_type: reconciliation_variant
  card_id: reconciliation_variant.order_to_shipment.fallback_or_batch
  name: Order to Shipment Reconciliation Fallback or Batch Variant
  fields:
    name: Order to Shipment Reconciliation Fallback or Batch Variant
    description: Variant for Order to Shipment Reconciliation when direct references are absent or bank/settlement data is
      batch-level.
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
    base_reconciliation_profile_id: reconciliation_profile.order_to_shipment
    variant_name: fallback_or_batch
    variant_reason: references absent or bank batch aggregation required
    applicability_scope: when primary reference unavailable or bank credit is batch-level
    matching_logic_override_id: matching_logic.order_to_shipment
    tolerance_overrides: use date window and batch aggregation
    mismatch_category_overrides: add delayed/partial/split/merged categories
    evidence_refs:
    - evidence.logistics_kb_doc
    - evidence.cognee_design_v4
    - evidence.unified_edge_scope
```

```yaml
candidate_card:
  card_type: reconciliation_variant
  card_id: reconciliation_variant.shipment_to_freight_invoice.fallback_or_batch
  name: Shipment to Freight Invoice Reconciliation Fallback or Batch Variant
  fields:
    name: Shipment to Freight Invoice Reconciliation Fallback or Batch Variant
    description: Variant for Shipment to Freight Invoice Reconciliation when direct references are absent or bank/settlement
      data is batch-level.
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
    base_reconciliation_profile_id: reconciliation_profile.shipment_to_freight_invoice
    variant_name: fallback_or_batch
    variant_reason: references absent or bank batch aggregation required
    applicability_scope: when primary reference unavailable or bank credit is batch-level
    matching_logic_override_id: matching_logic.shipment_to_freight_invoice
    tolerance_overrides: use date window and batch aggregation
    mismatch_category_overrides: add delayed/partial/split/merged categories
    evidence_refs:
    - evidence.logistics_kb_doc
    - evidence.cognee_design_v4
    - evidence.unified_edge_scope
```

```yaml
candidate_card:
  card_type: reconciliation_variant
  card_id: reconciliation_variant.freight_charge_validation.fallback_or_batch
  name: Freight Charge Validation Fallback or Batch Variant
  fields:
    name: Freight Charge Validation Fallback or Batch Variant
    description: Variant for Freight Charge Validation when direct references are absent or bank/settlement data is batch-level.
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
    base_reconciliation_profile_id: reconciliation_profile.freight_charge_validation
    variant_name: fallback_or_batch
    variant_reason: references absent or bank batch aggregation required
    applicability_scope: when primary reference unavailable or bank credit is batch-level
    matching_logic_override_id: matching_logic.freight_charge_validation
    tolerance_overrides: use date window and batch aggregation
    mismatch_category_overrides: add delayed/partial/split/merged categories
    evidence_refs:
    - evidence.logistics_kb_doc
    - evidence.cognee_design_v4
    - evidence.unified_edge_scope
```

```yaml
candidate_card:
  card_type: reconciliation_variant
  card_id: reconciliation_variant.cod_expected_to_courier_remittance.fallback_or_batch
  name: COD Expected to Courier Remittance Reconciliation Fallback or Batch Variant
  fields:
    name: COD Expected to Courier Remittance Reconciliation Fallback or Batch Variant
    description: Variant for COD Expected to Courier Remittance Reconciliation when direct references are absent or bank/settlement
      data is batch-level.
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
    base_reconciliation_profile_id: reconciliation_profile.cod_expected_to_courier_remittance
    variant_name: fallback_or_batch
    variant_reason: references absent or bank batch aggregation required
    applicability_scope: when primary reference unavailable or bank credit is batch-level
    matching_logic_override_id: matching_logic.cod_expected_to_courier_remittance
    tolerance_overrides: use date window and batch aggregation
    mismatch_category_overrides: add delayed/partial/split/merged categories
    evidence_refs:
    - evidence.logistics_kb_doc
    - evidence.cognee_design_v4
    - evidence.unified_edge_scope
```

```yaml
candidate_card:
  card_type: reconciliation_variant
  card_id: reconciliation_variant.courier_batch_to_bank_credit.fallback_or_batch
  name: Courier Batch to Bank Credit Reconciliation Fallback or Batch Variant
  fields:
    name: Courier Batch to Bank Credit Reconciliation Fallback or Batch Variant
    description: Variant for Courier Batch to Bank Credit Reconciliation when direct references are absent or bank/settlement
      data is batch-level.
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
    base_reconciliation_profile_id: reconciliation_profile.courier_batch_to_bank_credit
    variant_name: fallback_or_batch
    variant_reason: references absent or bank batch aggregation required
    applicability_scope: when primary reference unavailable or bank credit is batch-level
    matching_logic_override_id: matching_logic.courier_batch_to_bank_credit
    tolerance_overrides: use date window and batch aggregation
    mismatch_category_overrides: add delayed/partial/split/merged categories
    evidence_refs:
    - evidence.logistics_kb_doc
    - evidence.cognee_design_v4
    - evidence.unified_edge_scope
```

```yaml
candidate_card:
  card_type: reconciliation_variant
  card_id: reconciliation_variant.prepaid_pos_logistics_settlement.fallback_or_batch
  name: Prepaid/POS Logistics Settlement Reconciliation Fallback or Batch Variant
  fields:
    name: Prepaid/POS Logistics Settlement Reconciliation Fallback or Batch Variant
    description: Variant for Prepaid/POS Logistics Settlement Reconciliation when direct references are absent or bank/settlement
      data is batch-level.
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
    base_reconciliation_profile_id: reconciliation_profile.prepaid_pos_logistics_settlement
    variant_name: fallback_or_batch
    variant_reason: references absent or bank batch aggregation required
    applicability_scope: when primary reference unavailable or bank credit is batch-level
    matching_logic_override_id: matching_logic.prepaid_pos_logistics_settlement
    tolerance_overrides: use date window and batch aggregation
    mismatch_category_overrides: add delayed/partial/split/merged categories
    evidence_refs:
    - evidence.logistics_kb_doc
    - evidence.cognee_design_v4
    - evidence.unified_edge_scope
```

```yaml
candidate_card:
  card_type: reconciliation_variant
  card_id: reconciliation_variant.low_confidence_native_to_fallback.fallback_or_batch
  name: Low Confidence Native to Fallback Validation Fallback or Batch Variant
  fields:
    name: Low Confidence Native to Fallback Validation Fallback or Batch Variant
    description: Variant for Low Confidence Native to Fallback Validation when direct references are absent or bank/settlement
      data is batch-level.
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
    base_reconciliation_profile_id: reconciliation_profile.low_confidence_native_to_fallback
    variant_name: fallback_or_batch
    variant_reason: references absent or bank batch aggregation required
    applicability_scope: when primary reference unavailable or bank credit is batch-level
    matching_logic_override_id: matching_logic.low_confidence_native_to_fallback
    tolerance_overrides: use date window and batch aggregation
    mismatch_category_overrides: add delayed/partial/split/merged categories
    evidence_refs:
    - evidence.logistics_kb_doc
    - evidence.cognee_design_v4
    - evidence.unified_edge_scope
```

### 4.22 query_pattern cards

```yaml
candidate_card:
  card_type: query_pattern
  card_id: query_pattern.logistics.shipment_count_by_courier
  name: Shipment Count By Courier
  fields:
    name: Shipment Count By Courier
    description: Approved logistics query pattern for shipment_count_by_courier.
    status: active
    confidence: high
    source_documents:
    - Logistics KB Doc.docx
    - Cognee KB Design v4.md
    - logistics_gold_std_raw_md_frame_v3.md
    - logistics_gold_std_canonical_card_frame_v5.md
    created_by: kb_authoring_assistant
    updated_by: kb_authoring_assistant
    version: 5.0-manifest-aligned
    pattern_name: shipment_count_by_courier
    pattern_type: analytical; reconciliation; diagnostic
    supported_intents: shipment count by courier
    applicability_scope: logistics domain; account scope injected at runtime
    required_tables:
    - profile/vendor specific
    - table.zs_observe.shiprocket_oms
    optional_tables: bank_statement; fallback aggregator tables
    required_metrics: profile-specific metrics
    allowed_dimensions:
    - courier_partner
    - status
    - payment_mode
    - zone
    - date
    - awb when safe
    allowed_grains:
    - awb
    - order
    - day
    - month
    - batch
    recommended_date_columns:
    - source-specific recommended date columns
    semantic_filters:
    - is_active=true when present
    - status/value filters by profile
    join_constraints: use relationship cards; pre-aggregate before joins
    aggregation_rules: avoid fanout; aggregate AWB to batch before bank matching
    query_shape: pseudo_sql_pattern_available_from card fields and vendor implementations
    linked_rules: rule.logistics.required_scope_context; rule.logistics.amount_semantics_not_by_name; rule.logistics.grain_safe_reconciliation
    validation_tests:
    - validation_test.logistics.required_scope_context
    - validation_test.logistics.amount_semantics_not_by_name
    output_contract_id: output_contract.logistics_reconciliation_summary
    evidence_refs:
    - evidence.logistics_kb_doc
    - evidence.cognee_design_v4
    - evidence.unified_edge_scope
    produces_metric:
    - metric.shipment_count
    - metric.unique_awb_count
    uses_reconciliation_profile: []
    rules:
    - rule.logistics.active_filter_when_available
    - rule.logistics.awb_primary_reconciliation_unit
    output_contracts:
    - output_contract.logistics_metric_summary
    query_pattern_boundary: Account filters and Business Flow Binding are resolved outside this generic query pattern.
    edge_enrichment_note: v4 adds PRODUCES_METRIC / USES_RECONCILIATION_PROFILE / REQUIRES_RULE / USES_OUTPUT_CONTRACT / USES_TABLE
      edges where targets exist.
```

```yaml
candidate_card:
  card_type: query_pattern
  card_id: query_pattern.logistics.delivery_and_rto_rate
  name: Delivery And Rto Rate
  fields:
    name: Delivery And Rto Rate
    description: Approved logistics query pattern for delivery_and_rto_rate.
    status: active
    confidence: high
    source_documents:
    - Logistics KB Doc.docx
    - Cognee KB Design v4.md
    - logistics_gold_std_raw_md_frame_v3.md
    - logistics_gold_std_canonical_card_frame_v5.md
    created_by: kb_authoring_assistant
    updated_by: kb_authoring_assistant
    version: 5.0-manifest-aligned
    pattern_name: delivery_and_rto_rate
    pattern_type: analytical; reconciliation; diagnostic
    supported_intents: delivery and rto rate
    applicability_scope: logistics domain; account scope injected at runtime
    required_tables:
    - profile/vendor specific
    - table.zs_observe.shiprocket_oms
    optional_tables: bank_statement; fallback aggregator tables
    required_metrics: profile-specific metrics
    allowed_dimensions:
    - courier_partner
    - status
    - payment_mode
    - zone
    - date
    - awb when safe
    allowed_grains:
    - awb
    - order
    - day
    - month
    - batch
    recommended_date_columns:
    - source-specific recommended date columns
    semantic_filters:
    - is_active=true when present
    - status/value filters by profile
    join_constraints: use relationship cards; pre-aggregate before joins
    aggregation_rules: avoid fanout; aggregate AWB to batch before bank matching
    query_shape: pseudo_sql_pattern_available_from card fields and vendor implementations
    linked_rules: rule.logistics.required_scope_context; rule.logistics.amount_semantics_not_by_name; rule.logistics.grain_safe_reconciliation
    validation_tests:
    - validation_test.logistics.required_scope_context
    - validation_test.logistics.amount_semantics_not_by_name
    output_contract_id: output_contract.logistics_reconciliation_summary
    evidence_refs:
    - evidence.logistics_kb_doc
    - evidence.cognee_design_v4
    - evidence.unified_edge_scope
    produces_metric:
    - metric.delivery_success_rate
    - metric.rto_rate
    - metric.delivered_shipment_count
    - metric.rto_count
    uses_reconciliation_profile: []
    rules:
    - rule.logistics.delivered_date_for_delivery_metrics
    - rule.logistics.payment_mode_value_profile_required
    output_contracts:
    - output_contract.logistics_metric_summary
    query_pattern_boundary: Account filters and Business Flow Binding are resolved outside this generic query pattern.
    edge_enrichment_note: v4 adds PRODUCES_METRIC / USES_RECONCILIATION_PROFILE / REQUIRES_RULE / USES_OUTPUT_CONTRACT / USES_TABLE
      edges where targets exist.
```

```yaml
candidate_card:
  card_type: query_pattern
  card_id: query_pattern.logistics.shipments_without_invoice
  name: Shipments Without Invoice
  fields:
    name: Shipments Without Invoice
    description: Approved logistics query pattern for shipments_without_invoice.
    status: active
    confidence: high
    source_documents:
    - Logistics KB Doc.docx
    - Cognee KB Design v4.md
    - logistics_gold_std_raw_md_frame_v3.md
    - logistics_gold_std_canonical_card_frame_v5.md
    created_by: kb_authoring_assistant
    updated_by: kb_authoring_assistant
    version: 5.0-manifest-aligned
    pattern_name: shipments_without_invoice
    pattern_type: analytical; reconciliation; diagnostic
    supported_intents: shipments without invoice
    applicability_scope: logistics domain; account scope injected at runtime
    required_tables:
    - profile/vendor specific
    - table.zs_observe.shiprocket_oms
    - table.zs_observe.shiprocket_invoice
    optional_tables: bank_statement; fallback aggregator tables
    required_metrics: profile-specific metrics
    allowed_dimensions:
    - courier_partner
    - status
    - payment_mode
    - zone
    - date
    - awb when safe
    allowed_grains:
    - awb
    - order
    - day
    - month
    - batch
    recommended_date_columns:
    - source-specific recommended date columns
    semantic_filters:
    - is_active=true when present
    - status/value filters by profile
    join_constraints: use relationship cards; pre-aggregate before joins
    aggregation_rules: avoid fanout; aggregate AWB to batch before bank matching
    query_shape: pseudo_sql_pattern_available_from card fields and vendor implementations
    linked_rules: rule.logistics.required_scope_context; rule.logistics.amount_semantics_not_by_name; rule.logistics.grain_safe_reconciliation
    validation_tests:
    - validation_test.logistics.required_scope_context
    - validation_test.logistics.amount_semantics_not_by_name
    output_contract_id: output_contract.logistics_reconciliation_summary
    evidence_refs:
    - evidence.logistics_kb_doc
    - evidence.cognee_design_v4
    - evidence.unified_edge_scope
    produces_metric:
    - metric.shipment_missing_invoice_count
    uses_reconciliation_profile:
    - reconciliation_profile.shipment_to_freight_invoice
    rules:
    - rule.logistics.awb_primary_reconciliation_unit
    - rule.logistics.empty_tables_schema_only
    output_contracts:
    - output_contract.logistics_diagnostic_summary
    query_pattern_boundary: Account filters and Business Flow Binding are resolved outside this generic query pattern.
    edge_enrichment_note: v4 adds PRODUCES_METRIC / USES_RECONCILIATION_PROFILE / REQUIRES_RULE / USES_OUTPUT_CONTRACT / USES_TABLE
      edges where targets exist.
```

```yaml
candidate_card:
  card_type: query_pattern
  card_id: query_pattern.logistics.shipments_without_cod_remittance
  name: Shipments Without Cod Remittance
  fields:
    name: Shipments Without Cod Remittance
    description: Approved logistics query pattern for shipments_without_cod_remittance.
    status: active
    confidence: high
    source_documents:
    - Logistics KB Doc.docx
    - Cognee KB Design v4.md
    - logistics_gold_std_raw_md_frame_v3.md
    - logistics_gold_std_canonical_card_frame_v5.md
    created_by: kb_authoring_assistant
    updated_by: kb_authoring_assistant
    version: 5.0-manifest-aligned
    pattern_name: shipments_without_cod_remittance
    pattern_type: analytical; reconciliation; diagnostic
    supported_intents: shipments without cod remittance
    applicability_scope: logistics domain; account scope injected at runtime
    required_tables:
    - profile/vendor specific
    - table.zs_observe.shiprocket_oms
    - table.zs_observe.shiprocket_settlement
    optional_tables: bank_statement; fallback aggregator tables
    required_metrics: profile-specific metrics
    allowed_dimensions:
    - courier_partner
    - status
    - payment_mode
    - zone
    - date
    - awb when safe
    allowed_grains:
    - awb
    - order
    - day
    - month
    - batch
    recommended_date_columns:
    - source-specific recommended date columns
    semantic_filters:
    - is_active=true when present
    - status/value filters by profile
    join_constraints: use relationship cards; pre-aggregate before joins
    aggregation_rules: avoid fanout; aggregate AWB to batch before bank matching
    query_shape: pseudo_sql_pattern_available_from card fields and vendor implementations
    linked_rules: rule.logistics.required_scope_context; rule.logistics.amount_semantics_not_by_name; rule.logistics.grain_safe_reconciliation
    validation_tests:
    - validation_test.logistics.required_scope_context
    - validation_test.logistics.amount_semantics_not_by_name
    output_contract_id: output_contract.logistics_reconciliation_summary
    evidence_refs:
    - evidence.logistics_kb_doc
    - evidence.cognee_design_v4
    - evidence.unified_edge_scope
    produces_metric:
    - metric.cod_gap_amount
    - metric.unmatched_awb_count
    uses_reconciliation_profile:
    - reconciliation_profile.cod_expected_to_courier_remittance
    rules:
    - rule.logistics.settlement_date_for_cod_remittance
    - rule.logistics.do_not_join_awb_to_bank_without_batch
    output_contracts:
    - output_contract.logistics_diagnostic_summary
    query_pattern_boundary: Account filters and Business Flow Binding are resolved outside this generic query pattern.
    edge_enrichment_note: v4 adds PRODUCES_METRIC / USES_RECONCILIATION_PROFILE / REQUIRES_RULE / USES_OUTPUT_CONTRACT / USES_TABLE
      edges where targets exist.
```

```yaml
candidate_card:
  card_type: query_pattern
  card_id: query_pattern.logistics.freight_billed_by_awb
  name: Freight Billed By Awb
  fields:
    name: Freight Billed By Awb
    description: Approved logistics query pattern for freight_billed_by_awb.
    status: active
    confidence: high
    source_documents:
    - Logistics KB Doc.docx
    - Cognee KB Design v4.md
    - logistics_gold_std_raw_md_frame_v3.md
    - logistics_gold_std_canonical_card_frame_v5.md
    created_by: kb_authoring_assistant
    updated_by: kb_authoring_assistant
    version: 5.0-manifest-aligned
    pattern_name: freight_billed_by_awb
    pattern_type: analytical; reconciliation; diagnostic
    supported_intents: freight billed by awb
    applicability_scope: logistics domain; account scope injected at runtime
    required_tables:
    - profile/vendor specific
    - table.zs_observe.shiprocket_invoice
    optional_tables: bank_statement; fallback aggregator tables
    required_metrics: profile-specific metrics
    allowed_dimensions:
    - courier_partner
    - status
    - payment_mode
    - zone
    - date
    - awb when safe
    allowed_grains:
    - awb
    - order
    - day
    - month
    - batch
    recommended_date_columns:
    - source-specific recommended date columns
    semantic_filters:
    - is_active=true when present
    - status/value filters by profile
    join_constraints: use relationship cards; pre-aggregate before joins
    aggregation_rules: avoid fanout; aggregate AWB to batch before bank matching
    query_shape: pseudo_sql_pattern_available_from card fields and vendor implementations
    linked_rules: rule.logistics.required_scope_context; rule.logistics.amount_semantics_not_by_name; rule.logistics.grain_safe_reconciliation
    validation_tests:
    - validation_test.logistics.required_scope_context
    - validation_test.logistics.amount_semantics_not_by_name
    output_contract_id: output_contract.logistics_reconciliation_summary
    evidence_refs:
    - evidence.logistics_kb_doc
    - evidence.cognee_design_v4
    - evidence.unified_edge_scope
    produces_metric:
    - metric.freight_billed_amount
    - metric.average_freight_per_awb
    uses_reconciliation_profile:
    - reconciliation_profile.shipment_to_freight_invoice
    rules:
    - rule.logistics.shiprocket_invoice_charged_amount_freight
    - rule.logistics.awb_primary_reconciliation_unit
    output_contracts:
    - output_contract.logistics_metric_summary
    query_pattern_boundary: Account filters and Business Flow Binding are resolved outside this generic query pattern.
    edge_enrichment_note: v4 adds PRODUCES_METRIC / USES_RECONCILIATION_PROFILE / REQUIRES_RULE / USES_OUTPUT_CONTRACT / USES_TABLE
      edges where targets exist.
```

```yaml
candidate_card:
  card_type: query_pattern
  card_id: query_pattern.logistics.freight_component_breakdown
  name: Freight Component Breakdown
  fields:
    name: Freight Component Breakdown
    description: Approved logistics query pattern for freight_component_breakdown.
    status: active
    confidence: high
    source_documents:
    - Logistics KB Doc.docx
    - Cognee KB Design v4.md
    - logistics_gold_std_raw_md_frame_v3.md
    - logistics_gold_std_canonical_card_frame_v5.md
    created_by: kb_authoring_assistant
    updated_by: kb_authoring_assistant
    version: 5.0-manifest-aligned
    pattern_name: freight_component_breakdown
    pattern_type: analytical; reconciliation; diagnostic
    supported_intents: freight component breakdown
    applicability_scope: logistics domain; account scope injected at runtime
    required_tables:
    - profile/vendor specific
    - table.zs_observe.shiprocket_invoice
    - table.zs_observe.delhivery_invoice
    optional_tables: bank_statement; fallback aggregator tables
    required_metrics: profile-specific metrics
    allowed_dimensions:
    - courier_partner
    - status
    - payment_mode
    - zone
    - date
    - awb when safe
    allowed_grains:
    - awb
    - order
    - day
    - month
    - batch
    recommended_date_columns:
    - source-specific recommended date columns
    semantic_filters:
    - is_active=true when present
    - status/value filters by profile
    join_constraints: use relationship cards; pre-aggregate before joins
    aggregation_rules: avoid fanout; aggregate AWB to batch before bank matching
    query_shape: pseudo_sql_pattern_available_from card fields and vendor implementations
    linked_rules: rule.logistics.required_scope_context; rule.logistics.amount_semantics_not_by_name; rule.logistics.grain_safe_reconciliation
    validation_tests:
    - validation_test.logistics.required_scope_context
    - validation_test.logistics.amount_semantics_not_by_name
    output_contract_id: output_contract.logistics_reconciliation_summary
    evidence_refs:
    - evidence.logistics_kb_doc
    - evidence.cognee_design_v4
    - evidence.unified_edge_scope
    produces_metric:
    - metric.freight_billed_amount
    - metric.forward_freight_amount
    - metric.rto_freight_amount
    - metric.cod_fee_amount
    - metric.gst_on_freight_amount
    uses_reconciliation_profile:
    - reconciliation_profile.freight_charge_validation
    rules:
    - rule.logistics.cod_fee_only_for_cod
    - rule.logistics.rto_charge_only_for_rto
    output_contracts:
    - output_contract.logistics_metric_summary
    query_pattern_boundary: Account filters and Business Flow Binding are resolved outside this generic query pattern.
    edge_enrichment_note: v4 adds PRODUCES_METRIC / USES_RECONCILIATION_PROFILE / REQUIRES_RULE / USES_OUTPUT_CONTRACT / USES_TABLE
      edges where targets exist.
```

```yaml
candidate_card:
  card_type: query_pattern
  card_id: query_pattern.logistics.freight_overcharge_check
  name: Freight Overcharge Check
  fields:
    name: Freight Overcharge Check
    description: Approved logistics query pattern for freight_overcharge_check.
    status: active
    confidence: high
    source_documents:
    - Logistics KB Doc.docx
    - Cognee KB Design v4.md
    - logistics_gold_std_raw_md_frame_v3.md
    - logistics_gold_std_canonical_card_frame_v5.md
    created_by: kb_authoring_assistant
    updated_by: kb_authoring_assistant
    version: 5.0-manifest-aligned
    pattern_name: freight_overcharge_check
    pattern_type: analytical; reconciliation; diagnostic
    supported_intents: freight overcharge check
    applicability_scope: logistics domain; account scope injected at runtime
    required_tables:
    - profile/vendor specific
    - table.zs_observe.shiprocket_invoice
    - table.zs_observe.delhivery_invoice
    optional_tables: bank_statement; fallback aggregator tables
    required_metrics: profile-specific metrics
    allowed_dimensions:
    - courier_partner
    - status
    - payment_mode
    - zone
    - date
    - awb when safe
    allowed_grains:
    - awb
    - order
    - day
    - month
    - batch
    recommended_date_columns:
    - source-specific recommended date columns
    semantic_filters:
    - is_active=true when present
    - status/value filters by profile
    join_constraints: use relationship cards; pre-aggregate before joins
    aggregation_rules: avoid fanout; aggregate AWB to batch before bank matching
    query_shape: pseudo_sql_pattern_available_from card fields and vendor implementations
    linked_rules: rule.logistics.required_scope_context; rule.logistics.amount_semantics_not_by_name; rule.logistics.grain_safe_reconciliation
    validation_tests:
    - validation_test.logistics.required_scope_context
    - validation_test.logistics.amount_semantics_not_by_name
    output_contract_id: output_contract.logistics_reconciliation_summary
    evidence_refs:
    - evidence.logistics_kb_doc
    - evidence.cognee_design_v4
    - evidence.unified_edge_scope
    produces_metric:
    - metric.freight_overcharge_amount
    - metric.freight_variance_amount
    uses_reconciliation_profile:
    - reconciliation_profile.freight_charge_validation
    rules:
    - rule.logistics.zone_value_profile_required
    - rule.logistics.payment_mode_value_profile_required
    output_contracts:
    - output_contract.logistics_reconciliation_summary
    query_pattern_boundary: Account filters and Business Flow Binding are resolved outside this generic query pattern.
    edge_enrichment_note: v4 adds PRODUCES_METRIC / USES_RECONCILIATION_PROFILE / REQUIRES_RULE / USES_OUTPUT_CONTRACT / USES_TABLE
      edges where targets exist.
```

```yaml
candidate_card:
  card_type: query_pattern
  card_id: query_pattern.logistics.cod_expected_vs_remitted
  name: Cod Expected Vs Remitted
  fields:
    name: Cod Expected Vs Remitted
    description: Approved logistics query pattern for cod_expected_vs_remitted.
    status: active
    confidence: high
    source_documents:
    - Logistics KB Doc.docx
    - Cognee KB Design v4.md
    - logistics_gold_std_raw_md_frame_v3.md
    - logistics_gold_std_canonical_card_frame_v5.md
    created_by: kb_authoring_assistant
    updated_by: kb_authoring_assistant
    version: 5.0-manifest-aligned
    pattern_name: cod_expected_vs_remitted
    pattern_type: analytical; reconciliation; diagnostic
    supported_intents: cod expected vs remitted
    applicability_scope: logistics domain; account scope injected at runtime
    required_tables:
    - profile/vendor specific
    - table.zs_observe.shiprocket_oms
    - table.zs_observe.shiprocket_settlement
    optional_tables: bank_statement; fallback aggregator tables
    required_metrics: profile-specific metrics
    allowed_dimensions:
    - courier_partner
    - status
    - payment_mode
    - zone
    - date
    - awb when safe
    allowed_grains:
    - awb
    - order
    - day
    - month
    - batch
    recommended_date_columns:
    - source-specific recommended date columns
    semantic_filters:
    - is_active=true when present
    - status/value filters by profile
    join_constraints: use relationship cards; pre-aggregate before joins
    aggregation_rules: avoid fanout; aggregate AWB to batch before bank matching
    query_shape: pseudo_sql_pattern_available_from card fields and vendor implementations
    linked_rules: rule.logistics.required_scope_context; rule.logistics.amount_semantics_not_by_name; rule.logistics.grain_safe_reconciliation
    validation_tests:
    - validation_test.logistics.required_scope_context
    - validation_test.logistics.amount_semantics_not_by_name
    output_contract_id: output_contract.logistics_reconciliation_summary
    evidence_refs:
    - evidence.logistics_kb_doc
    - evidence.cognee_design_v4
    - evidence.unified_edge_scope
    produces_metric:
    - metric.cod_expected_amount
    - metric.cod_remitted_amount
    - metric.cod_gap_amount
    uses_reconciliation_profile:
    - reconciliation_profile.cod_expected_to_courier_remittance
    rules:
    - rule.logistics.shiprocket_settlement_charged_amount_cod
    - rule.logistics.delhivery_charged_amount_declared_value
    output_contracts:
    - output_contract.logistics_reconciliation_summary
    query_pattern_boundary: Account filters and Business Flow Binding are resolved outside this generic query pattern.
    edge_enrichment_note: v4 adds PRODUCES_METRIC / USES_RECONCILIATION_PROFILE / REQUIRES_RULE / USES_OUTPUT_CONTRACT / USES_TABLE
      edges where targets exist.
```

```yaml
candidate_card:
  card_type: query_pattern
  card_id: query_pattern.logistics.cod_remittance_lag
  name: Cod Remittance Lag
  fields:
    name: Cod Remittance Lag
    description: Approved logistics query pattern for cod_remittance_lag.
    status: active
    confidence: high
    source_documents:
    - Logistics KB Doc.docx
    - Cognee KB Design v4.md
    - logistics_gold_std_raw_md_frame_v3.md
    - logistics_gold_std_canonical_card_frame_v5.md
    created_by: kb_authoring_assistant
    updated_by: kb_authoring_assistant
    version: 5.0-manifest-aligned
    pattern_name: cod_remittance_lag
    pattern_type: analytical; reconciliation; diagnostic
    supported_intents: cod remittance lag
    applicability_scope: logistics domain; account scope injected at runtime
    required_tables:
    - profile/vendor specific
    - table.zs_observe.shiprocket_settlement
    - table.zs_observe.ekart_settlement
    - table.zs_observe.dtdc_settlement
    optional_tables: bank_statement; fallback aggregator tables
    required_metrics: profile-specific metrics
    allowed_dimensions:
    - courier_partner
    - status
    - payment_mode
    - zone
    - date
    - awb when safe
    allowed_grains:
    - awb
    - order
    - day
    - month
    - batch
    recommended_date_columns:
    - source-specific recommended date columns
    semantic_filters:
    - is_active=true when present
    - status/value filters by profile
    join_constraints: use relationship cards; pre-aggregate before joins
    aggregation_rules: avoid fanout; aggregate AWB to batch before bank matching
    query_shape: pseudo_sql_pattern_available_from card fields and vendor implementations
    linked_rules: rule.logistics.required_scope_context; rule.logistics.amount_semantics_not_by_name; rule.logistics.grain_safe_reconciliation
    validation_tests:
    - validation_test.logistics.required_scope_context
    - validation_test.logistics.amount_semantics_not_by_name
    output_contract_id: output_contract.logistics_reconciliation_summary
    evidence_refs:
    - evidence.logistics_kb_doc
    - evidence.cognee_design_v4
    - evidence.unified_edge_scope
    produces_metric:
    - metric.cod_remittance_lag_days
    uses_reconciliation_profile:
    - reconciliation_profile.cod_expected_to_courier_remittance
    rules:
    - rule.logistics.settlement_date_for_cod_remittance
    - rule.logistics.delivered_date_for_delivery_metrics
    output_contracts:
    - output_contract.logistics_metric_summary
    query_pattern_boundary: Account filters and Business Flow Binding are resolved outside this generic query pattern.
    edge_enrichment_note: v4 adds PRODUCES_METRIC / USES_RECONCILIATION_PROFILE / REQUIRES_RULE / USES_OUTPUT_CONTRACT / USES_TABLE
      edges where targets exist.
```

```yaml
candidate_card:
  card_type: query_pattern
  card_id: query_pattern.logistics.courier_batch_to_bank_bridge
  name: Courier Batch To Bank Bridge
  fields:
    name: Courier Batch To Bank Bridge
    description: Approved logistics query pattern for courier_batch_to_bank_bridge.
    status: active
    confidence: high
    source_documents:
    - Logistics KB Doc.docx
    - Cognee KB Design v4.md
    - logistics_gold_std_raw_md_frame_v3.md
    - logistics_gold_std_canonical_card_frame_v5.md
    created_by: kb_authoring_assistant
    updated_by: kb_authoring_assistant
    version: 5.0-manifest-aligned
    pattern_name: courier_batch_to_bank_bridge
    pattern_type: analytical; reconciliation; diagnostic
    supported_intents: courier batch to bank bridge
    applicability_scope: logistics domain; account scope injected at runtime
    required_tables:
    - profile/vendor specific
    - table.zs_observe.delhivery_settlement
    - table.zs_observe.dtdc_settlement
    - table.zs_observe.ekart_settlement
    optional_tables: bank_statement; fallback aggregator tables
    required_metrics: profile-specific metrics
    allowed_dimensions:
    - courier_partner
    - status
    - payment_mode
    - zone
    - date
    - awb when safe
    allowed_grains:
    - awb
    - order
    - day
    - month
    - batch
    recommended_date_columns:
    - source-specific recommended date columns
    semantic_filters:
    - is_active=true when present
    - status/value filters by profile
    join_constraints: use relationship cards; pre-aggregate before joins
    aggregation_rules: avoid fanout; aggregate AWB to batch before bank matching
    query_shape: pseudo_sql_pattern_available_from card fields and vendor implementations
    linked_rules: rule.logistics.required_scope_context; rule.logistics.amount_semantics_not_by_name; rule.logistics.grain_safe_reconciliation
    validation_tests:
    - validation_test.logistics.required_scope_context
    - validation_test.logistics.amount_semantics_not_by_name
    output_contract_id: output_contract.logistics_reconciliation_summary
    evidence_refs:
    - evidence.logistics_kb_doc
    - evidence.cognee_design_v4
    - evidence.unified_edge_scope
    produces_metric:
    - metric.batch_settlement_amount
    - metric.bank_credit_matched_amount
    - metric.reconciliation_gap_amount
    uses_reconciliation_profile:
    - reconciliation_profile.courier_batch_to_bank_credit
    rules:
    - rule.logistics.bank_reference_required_for_bank_match
    - rule.logistics.utr_preferred_for_bank_bridge
    - rule.logistics.batch_amount_deduplicate
    output_contracts:
    - output_contract.logistics_money_flow_trace
    query_pattern_boundary: Account filters and Business Flow Binding are resolved outside this generic query pattern.
    edge_enrichment_note: v4 adds PRODUCES_METRIC / USES_RECONCILIATION_PROFILE / REQUIRES_RULE / USES_OUTPUT_CONTRACT / USES_TABLE
      edges where targets exist.
```

```yaml
candidate_card:
  card_type: query_pattern
  card_id: query_pattern.logistics.low_confidence_native_validation
  name: Low Confidence Native Validation
  fields:
    name: Low Confidence Native Validation
    description: Approved logistics query pattern for low_confidence_native_validation.
    status: active
    confidence: high
    source_documents:
    - Logistics KB Doc.docx
    - Cognee KB Design v4.md
    - logistics_gold_std_raw_md_frame_v3.md
    - logistics_gold_std_canonical_card_frame_v5.md
    created_by: kb_authoring_assistant
    updated_by: kb_authoring_assistant
    version: 5.0-manifest-aligned
    pattern_name: low_confidence_native_validation
    pattern_type: analytical; reconciliation; diagnostic
    supported_intents: low confidence native validation
    applicability_scope: logistics domain; account scope injected at runtime
    required_tables:
    - profile/vendor specific
    - table.zs_observe.xpressbees_settlement
    optional_tables: bank_statement; fallback aggregator tables
    required_metrics: profile-specific metrics
    allowed_dimensions:
    - courier_partner
    - status
    - payment_mode
    - zone
    - date
    - awb when safe
    allowed_grains:
    - awb
    - order
    - day
    - month
    - batch
    recommended_date_columns:
    - source-specific recommended date columns
    semantic_filters:
    - is_active=true when present
    - status/value filters by profile
    join_constraints: use relationship cards; pre-aggregate before joins
    aggregation_rules: avoid fanout; aggregate AWB to batch before bank matching
    query_shape: pseudo_sql_pattern_available_from card fields and vendor implementations
    linked_rules: rule.logistics.required_scope_context; rule.logistics.amount_semantics_not_by_name; rule.logistics.grain_safe_reconciliation
    validation_tests:
    - validation_test.logistics.required_scope_context
    - validation_test.logistics.amount_semantics_not_by_name
    output_contract_id: output_contract.logistics_reconciliation_summary
    evidence_refs:
    - evidence.logistics_kb_doc
    - evidence.cognee_design_v4
    - evidence.unified_edge_scope
    produces_metric:
    - metric.populated_native_record_count
    uses_reconciliation_profile: []
    rules:
    - rule.logistics.low_confidence_requires_warning
    - rule.logistics.xpressbees_native_low_confidence
    - rule.logistics.xpressbees_fallback_shiprocket_preferred
    output_contracts:
    - output_contract.logistics_data_quality_report
    query_pattern_boundary: Account filters and Business Flow Binding are resolved outside this generic query pattern.
    edge_enrichment_note: v4 adds PRODUCES_METRIC / USES_RECONCILIATION_PROFILE / REQUIRES_RULE / USES_OUTPUT_CONTRACT / USES_TABLE
      edges where targets exist.
```

```yaml
candidate_card:
  card_type: query_pattern
  card_id: query_pattern.logistics.shiprocket_courier_partner_freight_split
  name: Shiprocket Courier Partner Freight Split
  fields:
    name: Shiprocket Courier Partner Freight Split
    description: Approved logistics query pattern for shiprocket_courier_partner_freight_split.
    status: active
    confidence: high
    source_documents:
    - Logistics KB Doc.docx
    - Cognee KB Design v4.md
    - logistics_gold_std_raw_md_frame_v3.md
    - logistics_gold_std_canonical_card_frame_v5.md
    created_by: kb_authoring_assistant
    updated_by: kb_authoring_assistant
    version: 5.0-manifest-aligned
    pattern_name: shiprocket_courier_partner_freight_split
    pattern_type: analytical; reconciliation; diagnostic
    supported_intents: shiprocket courier partner freight split
    applicability_scope: logistics domain; account scope injected at runtime
    required_tables:
    - profile/vendor specific
    - table.zs_observe.shiprocket_invoice
    optional_tables: bank_statement; fallback aggregator tables
    required_metrics: profile-specific metrics
    allowed_dimensions:
    - courier_partner
    - status
    - payment_mode
    - zone
    - date
    - awb when safe
    allowed_grains:
    - awb
    - order
    - day
    - month
    - batch
    recommended_date_columns:
    - source-specific recommended date columns
    semantic_filters:
    - is_active=true when present
    - status/value filters by profile
    join_constraints: use relationship cards; pre-aggregate before joins
    aggregation_rules: avoid fanout; aggregate AWB to batch before bank matching
    query_shape: pseudo_sql_pattern_available_from card fields and vendor implementations
    linked_rules: rule.logistics.required_scope_context; rule.logistics.amount_semantics_not_by_name; rule.logistics.grain_safe_reconciliation
    validation_tests:
    - validation_test.logistics.required_scope_context
    - validation_test.logistics.amount_semantics_not_by_name
    output_contract_id: output_contract.logistics_reconciliation_summary
    evidence_refs:
    - evidence.logistics_kb_doc
    - evidence.cognee_design_v4
    - evidence.unified_edge_scope
    produces_metric:
    - metric.freight_billed_amount
    - metric.average_freight_per_awb
    uses_reconciliation_profile:
    - reconciliation_profile.shipment_to_freight_invoice
    rules:
    - rule.logistics.courier_partner_filter_exact_or_profiled
    - rule.logistics.shiprocket_invoice_charged_amount_freight
    output_contracts:
    - output_contract.logistics_metric_summary
    query_pattern_boundary: Account filters and Business Flow Binding are resolved outside this generic query pattern.
    edge_enrichment_note: v4 adds PRODUCES_METRIC / USES_RECONCILIATION_PROFILE / REQUIRES_RULE / USES_OUTPUT_CONTRACT / USES_TABLE
      edges where targets exist.
```

```yaml
candidate_card:
  card_type: query_pattern
  card_id: query_pattern.logistics.shiprocket_cod_by_underlying_courier
  name: Shiprocket Cod By Underlying Courier
  fields:
    name: Shiprocket Cod By Underlying Courier
    description: Approved logistics query pattern for shiprocket_cod_by_underlying_courier.
    status: active
    confidence: high
    source_documents:
    - Logistics KB Doc.docx
    - Cognee KB Design v4.md
    - logistics_gold_std_raw_md_frame_v3.md
    - logistics_gold_std_canonical_card_frame_v5.md
    created_by: kb_authoring_assistant
    updated_by: kb_authoring_assistant
    version: 5.0-manifest-aligned
    pattern_name: shiprocket_cod_by_underlying_courier
    pattern_type: analytical; reconciliation; diagnostic
    supported_intents: shiprocket cod by underlying courier
    applicability_scope: logistics domain; account scope injected at runtime
    required_tables:
    - profile/vendor specific
    - table.zs_observe.shiprocket_settlement
    optional_tables: bank_statement; fallback aggregator tables
    required_metrics: profile-specific metrics
    allowed_dimensions:
    - courier_partner
    - status
    - payment_mode
    - zone
    - date
    - awb when safe
    allowed_grains:
    - awb
    - order
    - day
    - month
    - batch
    recommended_date_columns:
    - source-specific recommended date columns
    semantic_filters:
    - is_active=true when present
    - status/value filters by profile
    join_constraints: use relationship cards; pre-aggregate before joins
    aggregation_rules: avoid fanout; aggregate AWB to batch before bank matching
    query_shape: pseudo_sql_pattern_available_from card fields and vendor implementations
    linked_rules: rule.logistics.required_scope_context; rule.logistics.amount_semantics_not_by_name; rule.logistics.grain_safe_reconciliation
    validation_tests:
    - validation_test.logistics.required_scope_context
    - validation_test.logistics.amount_semantics_not_by_name
    output_contract_id: output_contract.logistics_reconciliation_summary
    evidence_refs:
    - evidence.logistics_kb_doc
    - evidence.cognee_design_v4
    - evidence.unified_edge_scope
    produces_metric:
    - metric.cod_remitted_amount
    - metric.cod_remittance_lag_days
    uses_reconciliation_profile:
    - reconciliation_profile.cod_expected_to_courier_remittance
    rules:
    - rule.logistics.courier_partner_filter_exact_or_profiled
    - rule.logistics.shiprocket_settlement_charged_amount_cod
    output_contracts:
    - output_contract.logistics_metric_summary
    query_pattern_boundary: Account filters and Business Flow Binding are resolved outside this generic query pattern.
    edge_enrichment_note: v4 adds PRODUCES_METRIC / USES_RECONCILIATION_PROFILE / REQUIRES_RULE / USES_OUTPUT_CONTRACT / USES_TABLE
      edges where targets exist.
```

```yaml
candidate_card:
  card_type: query_pattern
  card_id: query_pattern.logistics.delhivery_freight_component_reconciliation
  name: Delhivery Freight Component Reconciliation
  fields:
    name: Delhivery Freight Component Reconciliation
    description: Approved logistics query pattern for delhivery_freight_component_reconciliation.
    status: active
    confidence: high
    source_documents:
    - Logistics KB Doc.docx
    - Cognee KB Design v4.md
    - logistics_gold_std_raw_md_frame_v3.md
    - logistics_gold_std_canonical_card_frame_v5.md
    created_by: kb_authoring_assistant
    updated_by: kb_authoring_assistant
    version: 5.0-manifest-aligned
    pattern_name: delhivery_freight_component_reconciliation
    pattern_type: analytical; reconciliation; diagnostic
    supported_intents: delhivery freight component reconciliation
    applicability_scope: logistics domain; account scope injected at runtime
    required_tables:
    - profile/vendor specific
    - table.zs_observe.delhivery_invoice
    optional_tables: bank_statement; fallback aggregator tables
    required_metrics: profile-specific metrics
    allowed_dimensions:
    - courier_partner
    - status
    - payment_mode
    - zone
    - date
    - awb when safe
    allowed_grains:
    - awb
    - order
    - day
    - month
    - batch
    recommended_date_columns:
    - source-specific recommended date columns
    semantic_filters:
    - is_active=true when present
    - status/value filters by profile
    join_constraints: use relationship cards; pre-aggregate before joins
    aggregation_rules: avoid fanout; aggregate AWB to batch before bank matching
    query_shape: pseudo_sql_pattern_available_from card fields and vendor implementations
    linked_rules: rule.logistics.required_scope_context; rule.logistics.amount_semantics_not_by_name; rule.logistics.grain_safe_reconciliation
    validation_tests:
    - validation_test.logistics.required_scope_context
    - validation_test.logistics.amount_semantics_not_by_name
    output_contract_id: output_contract.logistics_reconciliation_summary
    evidence_refs:
    - evidence.logistics_kb_doc
    - evidence.cognee_design_v4
    - evidence.unified_edge_scope
    produces_metric:
    - metric.freight_billed_amount
    - metric.forward_freight_amount
    - metric.rto_freight_amount
    - metric.cod_fee_amount
    uses_reconciliation_profile:
    - reconciliation_profile.freight_charge_validation
    rules:
    - rule.logistics.delhivery_charged_amount_declared_value
    - rule.logistics.preaggregate_before_order_join
    output_contracts:
    - output_contract.logistics_reconciliation_summary
    query_pattern_boundary: Account filters and Business Flow Binding are resolved outside this generic query pattern.
    edge_enrichment_note: v4 adds PRODUCES_METRIC / USES_RECONCILIATION_PROFILE / REQUIRES_RULE / USES_OUTPUT_CONTRACT / USES_TABLE
      edges where targets exist.
```

```yaml
candidate_card:
  card_type: query_pattern
  card_id: query_pattern.logistics.delhivery_cod_qr_vs_cash
  name: Delhivery Cod Qr Vs Cash
  fields:
    name: Delhivery Cod Qr Vs Cash
    description: Approved logistics query pattern for delhivery_cod_qr_vs_cash.
    status: active
    confidence: high
    source_documents:
    - Logistics KB Doc.docx
    - Cognee KB Design v4.md
    - logistics_gold_std_raw_md_frame_v3.md
    - logistics_gold_std_canonical_card_frame_v5.md
    created_by: kb_authoring_assistant
    updated_by: kb_authoring_assistant
    version: 5.0-manifest-aligned
    pattern_name: delhivery_cod_qr_vs_cash
    pattern_type: analytical; reconciliation; diagnostic
    supported_intents: delhivery cod qr vs cash
    applicability_scope: logistics domain; account scope injected at runtime
    required_tables:
    - profile/vendor specific
    - table.zs_observe.delhivery_settlement
    optional_tables: bank_statement; fallback aggregator tables
    required_metrics: profile-specific metrics
    allowed_dimensions:
    - courier_partner
    - status
    - payment_mode
    - zone
    - date
    - awb when safe
    allowed_grains:
    - awb
    - order
    - day
    - month
    - batch
    recommended_date_columns:
    - source-specific recommended date columns
    semantic_filters:
    - is_active=true when present
    - status/value filters by profile
    join_constraints: use relationship cards; pre-aggregate before joins
    aggregation_rules: avoid fanout; aggregate AWB to batch before bank matching
    query_shape: pseudo_sql_pattern_available_from card fields and vendor implementations
    linked_rules: rule.logistics.required_scope_context; rule.logistics.amount_semantics_not_by_name; rule.logistics.grain_safe_reconciliation
    validation_tests:
    - validation_test.logistics.required_scope_context
    - validation_test.logistics.amount_semantics_not_by_name
    output_contract_id: output_contract.logistics_reconciliation_summary
    evidence_refs:
    - evidence.logistics_kb_doc
    - evidence.cognee_design_v4
    - evidence.unified_edge_scope
    produces_metric:
    - metric.cod_remitted_amount
    - metric.payable_amount
    uses_reconciliation_profile:
    - reconciliation_profile.cod_expected_to_courier_remittance
    rules:
    - rule.logistics.qr_cod_separate_from_cash
    output_contracts:
    - output_contract.logistics_metric_summary
    query_pattern_boundary: Account filters and Business Flow Binding are resolved outside this generic query pattern.
    edge_enrichment_note: v4 adds PRODUCES_METRIC / USES_RECONCILIATION_PROFILE / REQUIRES_RULE / USES_OUTPUT_CONTRACT / USES_TABLE
      edges where targets exist.
```

```yaml
candidate_card:
  card_type: query_pattern
  card_id: query_pattern.logistics.dtdc_settlement_to_shiprocket_freight_fallback
  name: Dtdc Settlement To Shiprocket Freight Fallback
  fields:
    name: Dtdc Settlement To Shiprocket Freight Fallback
    description: Approved logistics query pattern for dtdc_settlement_to_shiprocket_freight_fallback.
    status: active
    confidence: high
    source_documents:
    - Logistics KB Doc.docx
    - Cognee KB Design v4.md
    - logistics_gold_std_raw_md_frame_v3.md
    - logistics_gold_std_canonical_card_frame_v5.md
    created_by: kb_authoring_assistant
    updated_by: kb_authoring_assistant
    version: 5.0-manifest-aligned
    pattern_name: dtdc_settlement_to_shiprocket_freight_fallback
    pattern_type: analytical; reconciliation; diagnostic
    supported_intents: dtdc settlement to shiprocket freight fallback
    applicability_scope: logistics domain; account scope injected at runtime
    required_tables:
    - profile/vendor specific
    - table.zs_observe.dtdc_settlement
    - table.zs_observe.shiprocket_invoice
    optional_tables: bank_statement; fallback aggregator tables
    required_metrics: profile-specific metrics
    allowed_dimensions:
    - courier_partner
    - status
    - payment_mode
    - zone
    - date
    - awb when safe
    allowed_grains:
    - awb
    - order
    - day
    - month
    - batch
    recommended_date_columns:
    - source-specific recommended date columns
    semantic_filters:
    - is_active=true when present
    - status/value filters by profile
    join_constraints: use relationship cards; pre-aggregate before joins
    aggregation_rules: avoid fanout; aggregate AWB to batch before bank matching
    query_shape: pseudo_sql_pattern_available_from card fields and vendor implementations
    linked_rules: rule.logistics.required_scope_context; rule.logistics.amount_semantics_not_by_name; rule.logistics.grain_safe_reconciliation
    validation_tests:
    - validation_test.logistics.required_scope_context
    - validation_test.logistics.amount_semantics_not_by_name
    output_contract_id: output_contract.logistics_reconciliation_summary
    evidence_refs:
    - evidence.logistics_kb_doc
    - evidence.cognee_design_v4
    - evidence.unified_edge_scope
    produces_metric:
    - metric.cod_remitted_amount
    - metric.freight_billed_amount
    uses_reconciliation_profile:
    - reconciliation_profile.cod_expected_to_courier_remittance
    - reconciliation_profile.shipment_to_freight_invoice
    rules:
    - rule.logistics.dtdc_invoice_empty
    - rule.logistics.fallback_sources_explicit_only
    output_contracts:
    - output_contract.logistics_diagnostic_summary
    query_pattern_boundary: Account filters and Business Flow Binding are resolved outside this generic query pattern.
    edge_enrichment_note: v4 adds PRODUCES_METRIC / USES_RECONCILIATION_PROFILE / REQUIRES_RULE / USES_OUTPUT_CONTRACT / USES_TABLE
      edges where targets exist.
```

```yaml
candidate_card:
  card_type: query_pattern
  card_id: query_pattern.logistics.dtdc_utr_bank_bridge
  name: Dtdc Utr Bank Bridge
  fields:
    name: Dtdc Utr Bank Bridge
    description: Approved logistics query pattern for dtdc_utr_bank_bridge.
    status: active
    confidence: high
    source_documents:
    - Logistics KB Doc.docx
    - Cognee KB Design v4.md
    - logistics_gold_std_raw_md_frame_v3.md
    - logistics_gold_std_canonical_card_frame_v5.md
    created_by: kb_authoring_assistant
    updated_by: kb_authoring_assistant
    version: 5.0-manifest-aligned
    pattern_name: dtdc_utr_bank_bridge
    pattern_type: analytical; reconciliation; diagnostic
    supported_intents: dtdc utr bank bridge
    applicability_scope: logistics domain; account scope injected at runtime
    required_tables:
    - profile/vendor specific
    - table.zs_observe.dtdc_settlement
    optional_tables: bank_statement; fallback aggregator tables
    required_metrics: profile-specific metrics
    allowed_dimensions:
    - courier_partner
    - status
    - payment_mode
    - zone
    - date
    - awb when safe
    allowed_grains:
    - awb
    - order
    - day
    - month
    - batch
    recommended_date_columns:
    - source-specific recommended date columns
    semantic_filters:
    - is_active=true when present
    - status/value filters by profile
    join_constraints: use relationship cards; pre-aggregate before joins
    aggregation_rules: avoid fanout; aggregate AWB to batch before bank matching
    query_shape: pseudo_sql_pattern_available_from card fields and vendor implementations
    linked_rules: rule.logistics.required_scope_context; rule.logistics.amount_semantics_not_by_name; rule.logistics.grain_safe_reconciliation
    validation_tests:
    - validation_test.logistics.required_scope_context
    - validation_test.logistics.amount_semantics_not_by_name
    output_contract_id: output_contract.logistics_reconciliation_summary
    evidence_refs:
    - evidence.logistics_kb_doc
    - evidence.cognee_design_v4
    - evidence.unified_edge_scope
    produces_metric:
    - metric.batch_settlement_amount
    - metric.bank_credit_matched_amount
    uses_reconciliation_profile:
    - reconciliation_profile.courier_batch_to_bank_credit
    rules:
    - rule.logistics.utr_preferred_for_bank_bridge
    - rule.logistics.bank_reference_required_for_bank_match
    output_contracts:
    - output_contract.logistics_money_flow_trace
    query_pattern_boundary: Account filters and Business Flow Binding are resolved outside this generic query pattern.
    edge_enrichment_note: v4 adds PRODUCES_METRIC / USES_RECONCILIATION_PROFILE / REQUIRES_RULE / USES_OUTPUT_CONTRACT / USES_TABLE
      edges where targets exist.
```

```yaml
candidate_card:
  card_type: query_pattern
  card_id: query_pattern.logistics.ekart_cod_pos_split
  name: Ekart Cod Pos Split
  fields:
    name: Ekart Cod Pos Split
    description: Approved logistics query pattern for ekart_cod_pos_split.
    status: active
    confidence: high
    source_documents:
    - Logistics KB Doc.docx
    - Cognee KB Design v4.md
    - logistics_gold_std_raw_md_frame_v3.md
    - logistics_gold_std_canonical_card_frame_v5.md
    created_by: kb_authoring_assistant
    updated_by: kb_authoring_assistant
    version: 5.0-manifest-aligned
    pattern_name: ekart_cod_pos_split
    pattern_type: analytical; reconciliation; diagnostic
    supported_intents: ekart cod pos split
    applicability_scope: logistics domain; account scope injected at runtime
    required_tables:
    - profile/vendor specific
    - table.zs_observe.ekart_settlement
    optional_tables: bank_statement; fallback aggregator tables
    required_metrics: profile-specific metrics
    allowed_dimensions:
    - courier_partner
    - status
    - payment_mode
    - zone
    - date
    - awb when safe
    allowed_grains:
    - awb
    - order
    - day
    - month
    - batch
    recommended_date_columns:
    - source-specific recommended date columns
    semantic_filters:
    - is_active=true when present
    - status/value filters by profile
    join_constraints: use relationship cards; pre-aggregate before joins
    aggregation_rules: avoid fanout; aggregate AWB to batch before bank matching
    query_shape: pseudo_sql_pattern_available_from card fields and vendor implementations
    linked_rules: rule.logistics.required_scope_context; rule.logistics.amount_semantics_not_by_name; rule.logistics.grain_safe_reconciliation
    validation_tests:
    - validation_test.logistics.required_scope_context
    - validation_test.logistics.amount_semantics_not_by_name
    output_contract_id: output_contract.logistics_reconciliation_summary
    evidence_refs:
    - evidence.logistics_kb_doc
    - evidence.cognee_design_v4
    - evidence.unified_edge_scope
    produces_metric:
    - metric.cod_remitted_amount
    - metric.pos_settled_amount
    - metric.batch_settlement_amount
    uses_reconciliation_profile:
    - reconciliation_profile.prepaid_pos_settlement
    - reconciliation_profile.cod_expected_to_courier_remittance
    rules:
    - rule.logistics.ekart_settlement_transaction_type_required
    - rule.logistics.total_amount_of_batch_not_awb_level
    output_contracts:
    - output_contract.logistics_metric_summary
    query_pattern_boundary: Account filters and Business Flow Binding are resolved outside this generic query pattern.
    edge_enrichment_note: v4 adds PRODUCES_METRIC / USES_RECONCILIATION_PROFILE / REQUIRES_RULE / USES_OUTPUT_CONTRACT / USES_TABLE
      edges where targets exist.
```

```yaml
candidate_card:
  card_type: query_pattern
  card_id: query_pattern.logistics.ekart_batch_deduplicated_bank_bridge
  name: Ekart Batch Deduplicated Bank Bridge
  fields:
    name: Ekart Batch Deduplicated Bank Bridge
    description: Approved logistics query pattern for ekart_batch_deduplicated_bank_bridge.
    status: active
    confidence: high
    source_documents:
    - Logistics KB Doc.docx
    - Cognee KB Design v4.md
    - logistics_gold_std_raw_md_frame_v3.md
    - logistics_gold_std_canonical_card_frame_v5.md
    created_by: kb_authoring_assistant
    updated_by: kb_authoring_assistant
    version: 5.0-manifest-aligned
    pattern_name: ekart_batch_deduplicated_bank_bridge
    pattern_type: analytical; reconciliation; diagnostic
    supported_intents: ekart batch deduplicated bank bridge
    applicability_scope: logistics domain; account scope injected at runtime
    required_tables:
    - profile/vendor specific
    - table.zs_observe.ekart_settlement
    optional_tables: bank_statement; fallback aggregator tables
    required_metrics: profile-specific metrics
    allowed_dimensions:
    - courier_partner
    - status
    - payment_mode
    - zone
    - date
    - awb when safe
    allowed_grains:
    - awb
    - order
    - day
    - month
    - batch
    recommended_date_columns:
    - source-specific recommended date columns
    semantic_filters:
    - is_active=true when present
    - status/value filters by profile
    join_constraints: use relationship cards; pre-aggregate before joins
    aggregation_rules: avoid fanout; aggregate AWB to batch before bank matching
    query_shape: pseudo_sql_pattern_available_from card fields and vendor implementations
    linked_rules: rule.logistics.required_scope_context; rule.logistics.amount_semantics_not_by_name; rule.logistics.grain_safe_reconciliation
    validation_tests:
    - validation_test.logistics.required_scope_context
    - validation_test.logistics.amount_semantics_not_by_name
    output_contract_id: output_contract.logistics_reconciliation_summary
    evidence_refs:
    - evidence.logistics_kb_doc
    - evidence.cognee_design_v4
    - evidence.unified_edge_scope
    produces_metric:
    - metric.batch_settlement_amount
    - metric.bank_reference_amount
    uses_reconciliation_profile:
    - reconciliation_profile.courier_batch_to_bank_credit
    rules:
    - rule.logistics.batch_amount_deduplicate
    - rule.logistics.total_amount_of_batch_not_awb_level
    output_contracts:
    - output_contract.logistics_money_flow_trace
    query_pattern_boundary: Account filters and Business Flow Binding are resolved outside this generic query pattern.
    edge_enrichment_note: v4 adds PRODUCES_METRIC / USES_RECONCILIATION_PROFILE / REQUIRES_RULE / USES_OUTPUT_CONTRACT / USES_TABLE
      edges where targets exist.
```

```yaml
candidate_card:
  card_type: query_pattern
  card_id: query_pattern.logistics.xpressbees_native_vs_shiprocket_fallback
  name: Xpressbees Native Vs Shiprocket Fallback
  fields:
    name: Xpressbees Native Vs Shiprocket Fallback
    description: Approved logistics query pattern for xpressbees_native_vs_shiprocket_fallback.
    status: active
    confidence: high
    source_documents:
    - Logistics KB Doc.docx
    - Cognee KB Design v4.md
    - logistics_gold_std_raw_md_frame_v3.md
    - logistics_gold_std_canonical_card_frame_v5.md
    created_by: kb_authoring_assistant
    updated_by: kb_authoring_assistant
    version: 5.0-manifest-aligned
    pattern_name: xpressbees_native_vs_shiprocket_fallback
    pattern_type: analytical; reconciliation; diagnostic
    supported_intents: xpressbees native vs shiprocket fallback
    applicability_scope: logistics domain; account scope injected at runtime
    required_tables:
    - profile/vendor specific
    - table.zs_observe.xpressbees_settlement
    - table.zs_observe.shiprocket_settlement
    optional_tables: bank_statement; fallback aggregator tables
    required_metrics: profile-specific metrics
    allowed_dimensions:
    - courier_partner
    - status
    - payment_mode
    - zone
    - date
    - awb when safe
    allowed_grains:
    - awb
    - order
    - day
    - month
    - batch
    recommended_date_columns:
    - source-specific recommended date columns
    semantic_filters:
    - is_active=true when present
    - status/value filters by profile
    join_constraints: use relationship cards; pre-aggregate before joins
    aggregation_rules: avoid fanout; aggregate AWB to batch before bank matching
    query_shape: pseudo_sql_pattern_available_from card fields and vendor implementations
    linked_rules: rule.logistics.required_scope_context; rule.logistics.amount_semantics_not_by_name; rule.logistics.grain_safe_reconciliation
    validation_tests:
    - validation_test.logistics.required_scope_context
    - validation_test.logistics.amount_semantics_not_by_name
    output_contract_id: output_contract.logistics_reconciliation_summary
    evidence_refs:
    - evidence.logistics_kb_doc
    - evidence.cognee_design_v4
    - evidence.unified_edge_scope
    produces_metric:
    - metric.cod_remitted_amount
    - metric.populated_native_record_count
    uses_reconciliation_profile:
    - reconciliation_profile.cod_expected_to_courier_remittance
    rules:
    - rule.logistics.xpressbees_native_low_confidence
    - rule.logistics.xpressbees_fallback_shiprocket_preferred
    output_contracts:
    - output_contract.logistics_data_quality_report
    query_pattern_boundary: Account filters and Business Flow Binding are resolved outside this generic query pattern.
    edge_enrichment_note: v4 adds PRODUCES_METRIC / USES_RECONCILIATION_PROFILE / REQUIRES_RULE / USES_OUTPUT_CONTRACT / USES_TABLE
      edges where targets exist.
```

```yaml
candidate_card:
  card_type: query_pattern
  card_id: query_pattern.logistics.shadowfax_reverse_only_evidence
  name: Shadowfax Reverse Only Evidence
  fields:
    name: Shadowfax Reverse Only Evidence
    description: Approved logistics query pattern for shadowfax_reverse_only_evidence.
    status: active
    confidence: high
    source_documents:
    - Logistics KB Doc.docx
    - Cognee KB Design v4.md
    - logistics_gold_std_raw_md_frame_v3.md
    - logistics_gold_std_canonical_card_frame_v5.md
    created_by: kb_authoring_assistant
    updated_by: kb_authoring_assistant
    version: 5.0-manifest-aligned
    pattern_name: shadowfax_reverse_only_evidence
    pattern_type: analytical; reconciliation; diagnostic
    supported_intents: shadowfax reverse only evidence
    applicability_scope: logistics domain; account scope injected at runtime
    required_tables:
    - profile/vendor specific
    - table.zs_observe.shiprocket_oms
    optional_tables: bank_statement; fallback aggregator tables
    required_metrics: profile-specific metrics
    allowed_dimensions:
    - courier_partner
    - status
    - payment_mode
    - zone
    - date
    - awb when safe
    allowed_grains:
    - awb
    - order
    - day
    - month
    - batch
    recommended_date_columns:
    - source-specific recommended date columns
    semantic_filters:
    - is_active=true when present
    - status/value filters by profile
    join_constraints: use relationship cards; pre-aggregate before joins
    aggregation_rules: avoid fanout; aggregate AWB to batch before bank matching
    query_shape: pseudo_sql_pattern_available_from card fields and vendor implementations
    linked_rules: rule.logistics.required_scope_context; rule.logistics.amount_semantics_not_by_name; rule.logistics.grain_safe_reconciliation
    validation_tests:
    - validation_test.logistics.required_scope_context
    - validation_test.logistics.amount_semantics_not_by_name
    output_contract_id: output_contract.logistics_reconciliation_summary
    evidence_refs:
    - evidence.logistics_kb_doc
    - evidence.cognee_design_v4
    - evidence.unified_edge_scope
    produces_metric:
    - metric.return_shipment_count
    - metric.reverse_qc_count
    uses_reconciliation_profile:
    - reconciliation_profile.return_rto_resolution
    rules:
    - rule.logistics.shadowfax_no_native_settlement
    output_contracts:
    - output_contract.logistics_diagnostic_summary
    query_pattern_boundary: Account filters and Business Flow Binding are resolved outside this generic query pattern.
    edge_enrichment_note: v4 adds PRODUCES_METRIC / USES_RECONCILIATION_PROFILE / REQUIRES_RULE / USES_OUTPUT_CONTRACT / USES_TABLE
      edges where targets exist.
```

```yaml
candidate_card:
  card_type: query_pattern
  card_id: query_pattern.logistics.ecom_indirect_shiprocket_evidence
  name: Ecom Indirect Shiprocket Evidence
  fields:
    name: Ecom Indirect Shiprocket Evidence
    description: Approved logistics query pattern for ecom_indirect_shiprocket_evidence.
    status: active
    confidence: high
    source_documents:
    - Logistics KB Doc.docx
    - Cognee KB Design v4.md
    - logistics_gold_std_raw_md_frame_v3.md
    - logistics_gold_std_canonical_card_frame_v5.md
    created_by: kb_authoring_assistant
    updated_by: kb_authoring_assistant
    version: 5.0-manifest-aligned
    pattern_name: ecom_indirect_shiprocket_evidence
    pattern_type: analytical; reconciliation; diagnostic
    supported_intents: ecom indirect shiprocket evidence
    applicability_scope: logistics domain; account scope injected at runtime
    required_tables:
    - profile/vendor specific
    - table.zs_observe.shiprocket_invoice
    - table.zs_observe.shiprocket_settlement
    optional_tables: bank_statement; fallback aggregator tables
    required_metrics: profile-specific metrics
    allowed_dimensions:
    - courier_partner
    - status
    - payment_mode
    - zone
    - date
    - awb when safe
    allowed_grains:
    - awb
    - order
    - day
    - month
    - batch
    recommended_date_columns:
    - source-specific recommended date columns
    semantic_filters:
    - is_active=true when present
    - status/value filters by profile
    join_constraints: use relationship cards; pre-aggregate before joins
    aggregation_rules: avoid fanout; aggregate AWB to batch before bank matching
    query_shape: pseudo_sql_pattern_available_from card fields and vendor implementations
    linked_rules: rule.logistics.required_scope_context; rule.logistics.amount_semantics_not_by_name; rule.logistics.grain_safe_reconciliation
    validation_tests:
    - validation_test.logistics.required_scope_context
    - validation_test.logistics.amount_semantics_not_by_name
    output_contract_id: output_contract.logistics_reconciliation_summary
    evidence_refs:
    - evidence.logistics_kb_doc
    - evidence.cognee_design_v4
    - evidence.unified_edge_scope
    produces_metric:
    - metric.freight_billed_amount
    - metric.cod_remitted_amount
    uses_reconciliation_profile:
    - reconciliation_profile.shipment_to_freight_invoice
    - reconciliation_profile.cod_expected_to_courier_remittance
    rules:
    - rule.logistics.ecom_no_native_table
    - rule.logistics.fallback_sources_explicit_only
    output_contracts:
    - output_contract.logistics_diagnostic_summary
    query_pattern_boundary: Account filters and Business Flow Binding are resolved outside this generic query pattern.
    edge_enrichment_note: v4 adds PRODUCES_METRIC / USES_RECONCILIATION_PROFILE / REQUIRES_RULE / USES_OUTPUT_CONTRACT / USES_TABLE
      edges where targets exist.
```

```yaml
candidate_card:
  card_type: query_pattern
  card_id: query_pattern.logistics.order_to_shipment_missing_awb
  name: Order To Shipment Missing Awb
  fields:
    name: Order To Shipment Missing Awb
    description: Approved logistics query pattern for order_to_shipment_missing_awb.
    status: active
    confidence: high
    source_documents:
    - Logistics KB Doc.docx
    - Cognee KB Design v4.md
    - logistics_gold_std_raw_md_frame_v3.md
    - logistics_gold_std_canonical_card_frame_v5.md
    created_by: kb_authoring_assistant
    updated_by: kb_authoring_assistant
    version: 5.0-manifest-aligned
    pattern_name: order_to_shipment_missing_awb
    pattern_type: analytical; reconciliation; diagnostic
    supported_intents: order to shipment missing awb
    applicability_scope: logistics domain; account scope injected at runtime
    required_tables:
    - profile/vendor specific
    - table.zs_observe.shiprocket_oms
    optional_tables: bank_statement; fallback aggregator tables
    required_metrics: profile-specific metrics
    allowed_dimensions:
    - courier_partner
    - status
    - payment_mode
    - zone
    - date
    - awb when safe
    allowed_grains:
    - awb
    - order
    - day
    - month
    - batch
    recommended_date_columns:
    - source-specific recommended date columns
    semantic_filters:
    - is_active=true when present
    - status/value filters by profile
    join_constraints: use relationship cards; pre-aggregate before joins
    aggregation_rules: avoid fanout; aggregate AWB to batch before bank matching
    query_shape: pseudo_sql_pattern_available_from card fields and vendor implementations
    linked_rules: rule.logistics.required_scope_context; rule.logistics.amount_semantics_not_by_name; rule.logistics.grain_safe_reconciliation
    validation_tests:
    - validation_test.logistics.required_scope_context
    - validation_test.logistics.amount_semantics_not_by_name
    output_contract_id: output_contract.logistics_reconciliation_summary
    evidence_refs:
    - evidence.logistics_kb_doc
    - evidence.cognee_design_v4
    - evidence.unified_edge_scope
    produces_metric:
    - metric.unmatched_awb_count
    uses_reconciliation_profile:
    - reconciliation_profile.order_to_shipment
    rules:
    - rule.logistics.parse_shiprocket_order_id_before_shopify_join
    output_contracts:
    - output_contract.logistics_diagnostic_summary
    query_pattern_boundary: Account filters and Business Flow Binding are resolved outside this generic query pattern.
    edge_enrichment_note: v4 adds PRODUCES_METRIC / USES_RECONCILIATION_PROFILE / REQUIRES_RULE / USES_OUTPUT_CONTRACT / USES_TABLE
      edges where targets exist.
```

```yaml
candidate_card:
  card_type: query_pattern
  card_id: query_pattern.logistics.awb_duplicate_detection
  name: Awb Duplicate Detection
  fields:
    name: Awb Duplicate Detection
    description: Approved logistics query pattern for awb_duplicate_detection.
    status: active
    confidence: high
    source_documents:
    - Logistics KB Doc.docx
    - Cognee KB Design v4.md
    - logistics_gold_std_raw_md_frame_v3.md
    - logistics_gold_std_canonical_card_frame_v5.md
    created_by: kb_authoring_assistant
    updated_by: kb_authoring_assistant
    version: 5.0-manifest-aligned
    pattern_name: awb_duplicate_detection
    pattern_type: analytical; reconciliation; diagnostic
    supported_intents: awb duplicate detection
    applicability_scope: logistics domain; account scope injected at runtime
    required_tables:
    - profile/vendor specific
    - table.zs_observe.shiprocket_oms
    - table.zs_observe.shiprocket_invoice
    - table.zs_observe.shiprocket_settlement
    optional_tables: bank_statement; fallback aggregator tables
    required_metrics: profile-specific metrics
    allowed_dimensions:
    - courier_partner
    - status
    - payment_mode
    - zone
    - date
    - awb when safe
    allowed_grains:
    - awb
    - order
    - day
    - month
    - batch
    recommended_date_columns:
    - source-specific recommended date columns
    semantic_filters:
    - is_active=true when present
    - status/value filters by profile
    join_constraints: use relationship cards; pre-aggregate before joins
    aggregation_rules: avoid fanout; aggregate AWB to batch before bank matching
    query_shape: pseudo_sql_pattern_available_from card fields and vendor implementations
    linked_rules: rule.logistics.required_scope_context; rule.logistics.amount_semantics_not_by_name; rule.logistics.grain_safe_reconciliation
    validation_tests:
    - validation_test.logistics.required_scope_context
    - validation_test.logistics.amount_semantics_not_by_name
    output_contract_id: output_contract.logistics_reconciliation_summary
    evidence_refs:
    - evidence.logistics_kb_doc
    - evidence.cognee_design_v4
    - evidence.unified_edge_scope
    produces_metric:
    - metric.duplicate_awb_count
    uses_reconciliation_profile:
    - reconciliation_profile.order_to_shipment
    rules:
    - rule.logistics.awb_primary_reconciliation_unit
    output_contracts:
    - output_contract.logistics_data_quality_report
    query_pattern_boundary: Account filters and Business Flow Binding are resolved outside this generic query pattern.
    edge_enrichment_note: v4 adds PRODUCES_METRIC / USES_RECONCILIATION_PROFILE / REQUIRES_RULE / USES_OUTPUT_CONTRACT / USES_TABLE
      edges where targets exist.
```

```yaml
candidate_card:
  card_type: query_pattern
  card_id: query_pattern.logistics.rto_freight_validation
  name: Rto Freight Validation
  fields:
    name: Rto Freight Validation
    description: Approved logistics query pattern for rto_freight_validation.
    status: active
    confidence: high
    source_documents:
    - Logistics KB Doc.docx
    - Cognee KB Design v4.md
    - logistics_gold_std_raw_md_frame_v3.md
    - logistics_gold_std_canonical_card_frame_v5.md
    created_by: kb_authoring_assistant
    updated_by: kb_authoring_assistant
    version: 5.0-manifest-aligned
    pattern_name: rto_freight_validation
    pattern_type: analytical; reconciliation; diagnostic
    supported_intents: rto freight validation
    applicability_scope: logistics domain; account scope injected at runtime
    required_tables:
    - profile/vendor specific
    - table.zs_observe.shiprocket_invoice
    - table.zs_observe.delhivery_invoice
    optional_tables: bank_statement; fallback aggregator tables
    required_metrics: profile-specific metrics
    allowed_dimensions:
    - courier_partner
    - status
    - payment_mode
    - zone
    - date
    - awb when safe
    allowed_grains:
    - awb
    - order
    - day
    - month
    - batch
    recommended_date_columns:
    - source-specific recommended date columns
    semantic_filters:
    - is_active=true when present
    - status/value filters by profile
    join_constraints: use relationship cards; pre-aggregate before joins
    aggregation_rules: avoid fanout; aggregate AWB to batch before bank matching
    query_shape: pseudo_sql_pattern_available_from card fields and vendor implementations
    linked_rules: rule.logistics.required_scope_context; rule.logistics.amount_semantics_not_by_name; rule.logistics.grain_safe_reconciliation
    validation_tests:
    - validation_test.logistics.required_scope_context
    - validation_test.logistics.amount_semantics_not_by_name
    output_contract_id: output_contract.logistics_reconciliation_summary
    evidence_refs:
    - evidence.logistics_kb_doc
    - evidence.cognee_design_v4
    - evidence.unified_edge_scope
    produces_metric:
    - metric.rto_freight_amount
    uses_reconciliation_profile:
    - reconciliation_profile.freight_charge_validation
    rules:
    - rule.logistics.rto_charge_only_for_rto
    output_contracts:
    - output_contract.logistics_reconciliation_summary
    query_pattern_boundary: Account filters and Business Flow Binding are resolved outside this generic query pattern.
    edge_enrichment_note: v4 adds PRODUCES_METRIC / USES_RECONCILIATION_PROFILE / REQUIRES_RULE / USES_OUTPUT_CONTRACT / USES_TABLE
      edges where targets exist.
```

```yaml
candidate_card:
  card_type: query_pattern
  card_id: query_pattern.logistics.cod_fee_on_prepaid_detection
  name: Cod Fee On Prepaid Detection
  fields:
    name: Cod Fee On Prepaid Detection
    description: Approved logistics query pattern for cod_fee_on_prepaid_detection.
    status: active
    confidence: high
    source_documents:
    - Logistics KB Doc.docx
    - Cognee KB Design v4.md
    - logistics_gold_std_raw_md_frame_v3.md
    - logistics_gold_std_canonical_card_frame_v5.md
    created_by: kb_authoring_assistant
    updated_by: kb_authoring_assistant
    version: 5.0-manifest-aligned
    pattern_name: cod_fee_on_prepaid_detection
    pattern_type: analytical; reconciliation; diagnostic
    supported_intents: cod fee on prepaid detection
    applicability_scope: logistics domain; account scope injected at runtime
    required_tables:
    - profile/vendor specific
    - table.zs_observe.shiprocket_invoice
    - table.zs_observe.delhivery_invoice
    optional_tables: bank_statement; fallback aggregator tables
    required_metrics: profile-specific metrics
    allowed_dimensions:
    - courier_partner
    - status
    - payment_mode
    - zone
    - date
    - awb when safe
    allowed_grains:
    - awb
    - order
    - day
    - month
    - batch
    recommended_date_columns:
    - source-specific recommended date columns
    semantic_filters:
    - is_active=true when present
    - status/value filters by profile
    join_constraints: use relationship cards; pre-aggregate before joins
    aggregation_rules: avoid fanout; aggregate AWB to batch before bank matching
    query_shape: pseudo_sql_pattern_available_from card fields and vendor implementations
    linked_rules: rule.logistics.required_scope_context; rule.logistics.amount_semantics_not_by_name; rule.logistics.grain_safe_reconciliation
    validation_tests:
    - validation_test.logistics.required_scope_context
    - validation_test.logistics.amount_semantics_not_by_name
    output_contract_id: output_contract.logistics_reconciliation_summary
    evidence_refs:
    - evidence.logistics_kb_doc
    - evidence.cognee_design_v4
    - evidence.unified_edge_scope
    produces_metric:
    - metric.cod_fee_amount
    uses_reconciliation_profile:
    - reconciliation_profile.freight_charge_validation
    rules:
    - rule.logistics.cod_fee_only_for_cod
    output_contracts:
    - output_contract.logistics_reconciliation_summary
    query_pattern_boundary: Account filters and Business Flow Binding are resolved outside this generic query pattern.
    edge_enrichment_note: v4 adds PRODUCES_METRIC / USES_RECONCILIATION_PROFILE / REQUIRES_RULE / USES_OUTPUT_CONTRACT / USES_TABLE
      edges where targets exist.
```

```yaml
candidate_card:
  card_type: query_pattern
  card_id: query_pattern.logistics.empty_table_guardrail_query
  name: Empty Table Guardrail Query
  fields:
    name: Empty Table Guardrail Query
    description: Approved logistics query pattern for empty_table_guardrail_query.
    status: active
    confidence: high
    source_documents:
    - Logistics KB Doc.docx
    - Cognee KB Design v4.md
    - logistics_gold_std_raw_md_frame_v3.md
    - logistics_gold_std_canonical_card_frame_v5.md
    created_by: kb_authoring_assistant
    updated_by: kb_authoring_assistant
    version: 5.0-manifest-aligned
    pattern_name: empty_table_guardrail_query
    pattern_type: analytical; reconciliation; diagnostic
    supported_intents: empty table guardrail query
    applicability_scope: logistics domain; account scope injected at runtime
    required_tables:
    - profile/vendor specific
    - table.zs_observe.dtdc_invoice
    - table.zs_observe.ekart_invoice
    - table.zs_observe.shiprocket_settlement_report
    optional_tables: bank_statement; fallback aggregator tables
    required_metrics: profile-specific metrics
    allowed_dimensions:
    - courier_partner
    - status
    - payment_mode
    - zone
    - date
    - awb when safe
    allowed_grains:
    - awb
    - order
    - day
    - month
    - batch
    recommended_date_columns:
    - source-specific recommended date columns
    semantic_filters:
    - is_active=true when present
    - status/value filters by profile
    join_constraints: use relationship cards; pre-aggregate before joins
    aggregation_rules: avoid fanout; aggregate AWB to batch before bank matching
    query_shape: pseudo_sql_pattern_available_from card fields and vendor implementations
    linked_rules: rule.logistics.required_scope_context; rule.logistics.amount_semantics_not_by_name; rule.logistics.grain_safe_reconciliation
    validation_tests:
    - validation_test.logistics.required_scope_context
    - validation_test.logistics.amount_semantics_not_by_name
    output_contract_id: output_contract.logistics_reconciliation_summary
    evidence_refs:
    - evidence.logistics_kb_doc
    - evidence.cognee_design_v4
    - evidence.unified_edge_scope
    produces_metric: []
    uses_reconciliation_profile: []
    rules:
    - rule.logistics.empty_tables_schema_only
    - rule.logistics.dtdc_invoice_empty
    - rule.logistics.ekart_invoice_empty
    - rule.logistics.shiprocket_settlement_report_empty
    output_contracts:
    - output_contract.logistics_data_quality_report
    query_pattern_boundary: Account filters and Business Flow Binding are resolved outside this generic query pattern.
    edge_enrichment_note: v4 adds PRODUCES_METRIC / USES_RECONCILIATION_PROFILE / REQUIRES_RULE / USES_OUTPUT_CONTRACT / USES_TABLE
      edges where targets exist.
```

```yaml
candidate_card:
  card_type: query_pattern
  card_id: query_pattern.logistics.amount_semantics_audit
  name: Amount Semantics Audit
  fields:
    name: Amount Semantics Audit
    description: Approved logistics query pattern for amount_semantics_audit.
    status: active
    confidence: high
    source_documents:
    - Logistics KB Doc.docx
    - Cognee KB Design v4.md
    - logistics_gold_std_raw_md_frame_v3.md
    - logistics_gold_std_canonical_card_frame_v5.md
    created_by: kb_authoring_assistant
    updated_by: kb_authoring_assistant
    version: 5.0-manifest-aligned
    pattern_name: amount_semantics_audit
    pattern_type: analytical; reconciliation; diagnostic
    supported_intents: amount semantics audit
    applicability_scope: logistics domain; account scope injected at runtime
    required_tables:
    - profile/vendor specific
    - table.zs_observe.shiprocket_oms
    - table.zs_observe.shiprocket_invoice
    - table.zs_observe.shiprocket_settlement
    - table.zs_observe.delhivery_invoice
    optional_tables: bank_statement; fallback aggregator tables
    required_metrics: profile-specific metrics
    allowed_dimensions:
    - courier_partner
    - status
    - payment_mode
    - zone
    - date
    - awb when safe
    allowed_grains:
    - awb
    - order
    - day
    - month
    - batch
    recommended_date_columns:
    - source-specific recommended date columns
    semantic_filters:
    - is_active=true when present
    - status/value filters by profile
    join_constraints: use relationship cards; pre-aggregate before joins
    aggregation_rules: avoid fanout; aggregate AWB to batch before bank matching
    query_shape: pseudo_sql_pattern_available_from card fields and vendor implementations
    linked_rules: rule.logistics.required_scope_context; rule.logistics.amount_semantics_not_by_name; rule.logistics.grain_safe_reconciliation
    validation_tests:
    - validation_test.logistics.required_scope_context
    - validation_test.logistics.amount_semantics_not_by_name
    output_contract_id: output_contract.logistics_reconciliation_summary
    evidence_refs:
    - evidence.logistics_kb_doc
    - evidence.cognee_design_v4
    - evidence.unified_edge_scope
    produces_metric: []
    uses_reconciliation_profile: []
    rules:
    - rule.logistics.amount_semantics_not_by_name
    - rule.logistics.charged_amount_table_specific
    output_contracts:
    - output_contract.logistics_data_quality_report
    query_pattern_boundary: Account filters and Business Flow Binding are resolved outside this generic query pattern.
    edge_enrichment_note: v4 adds PRODUCES_METRIC / USES_RECONCILIATION_PROFILE / REQUIRES_RULE / USES_OUTPUT_CONTRACT / USES_TABLE
      edges where targets exist.
```

```yaml
candidate_card:
  card_type: query_pattern
  card_id: query_pattern.logistics.scope_binding_injection_check
  name: Scope Binding Injection Check
  fields:
    name: Scope Binding Injection Check
    description: Approved logistics query pattern for scope_binding_injection_check.
    status: active
    confidence: high
    source_documents:
    - Logistics KB Doc.docx
    - Cognee KB Design v4.md
    - logistics_gold_std_raw_md_frame_v3.md
    - logistics_gold_std_canonical_card_frame_v5.md
    created_by: kb_authoring_assistant
    updated_by: kb_authoring_assistant
    version: 5.0-manifest-aligned
    pattern_name: scope_binding_injection_check
    pattern_type: analytical; reconciliation; diagnostic
    supported_intents: scope binding injection check
    applicability_scope: logistics domain; account scope injected at runtime
    required_tables:
    - profile/vendor specific
    optional_tables: bank_statement; fallback aggregator tables
    required_metrics: profile-specific metrics
    allowed_dimensions:
    - courier_partner
    - status
    - payment_mode
    - zone
    - date
    - awb when safe
    allowed_grains:
    - awb
    - order
    - day
    - month
    - batch
    recommended_date_columns:
    - source-specific recommended date columns
    semantic_filters:
    - is_active=true when present
    - status/value filters by profile
    join_constraints: use relationship cards; pre-aggregate before joins
    aggregation_rules: avoid fanout; aggregate AWB to batch before bank matching
    query_shape: pseudo_sql_pattern_available_from card fields and vendor implementations
    linked_rules: rule.logistics.required_scope_context; rule.logistics.amount_semantics_not_by_name; rule.logistics.grain_safe_reconciliation
    validation_tests:
    - validation_test.logistics.required_scope_context
    - validation_test.logistics.amount_semantics_not_by_name
    output_contract_id: output_contract.logistics_reconciliation_summary
    evidence_refs:
    - evidence.logistics_kb_doc
    - evidence.cognee_design_v4
    - evidence.unified_edge_scope
    produces_metric: []
    uses_reconciliation_profile: []
    rules:
    - rule.logistics.required_scope_context
    - rule.logistics.account_filters_from_adb_only
    - rule.logistics.business_flow_binding_required_for_cross_platform
    output_contracts:
    - output_contract.logistics_data_quality_report
    query_pattern_boundary: Account filters and Business Flow Binding are resolved outside this generic query pattern.
    edge_enrichment_note: v4 adds PRODUCES_METRIC / USES_RECONCILIATION_PROFILE / REQUIRES_RULE / USES_OUTPUT_CONTRACT / USES_TABLE
      edges where targets exist.
```

```yaml
candidate_card:
  card_type: query_pattern
  card_id: query_pattern.logistics.bank_credit_unmatched_courier_reference
  name: Bank Credit Unmatched Courier Reference
  fields:
    name: Bank Credit Unmatched Courier Reference
    description: Approved logistics query pattern for bank_credit_unmatched_courier_reference.
    status: active
    confidence: high
    source_documents:
    - Logistics KB Doc.docx
    - Cognee KB Design v4.md
    - logistics_gold_std_raw_md_frame_v3.md
    - logistics_gold_std_canonical_card_frame_v5.md
    created_by: kb_authoring_assistant
    updated_by: kb_authoring_assistant
    version: 5.0-manifest-aligned
    pattern_name: bank_credit_unmatched_courier_reference
    pattern_type: analytical; reconciliation; diagnostic
    supported_intents: bank credit unmatched courier reference
    applicability_scope: logistics domain; account scope injected at runtime
    required_tables:
    - profile/vendor specific
    - table.zs_observe.delhivery_settlement
    - table.zs_observe.dtdc_settlement
    - table.zs_observe.ekart_settlement
    optional_tables: bank_statement; fallback aggregator tables
    required_metrics: profile-specific metrics
    allowed_dimensions:
    - courier_partner
    - status
    - payment_mode
    - zone
    - date
    - awb when safe
    allowed_grains:
    - awb
    - order
    - day
    - month
    - batch
    recommended_date_columns:
    - source-specific recommended date columns
    semantic_filters:
    - is_active=true when present
    - status/value filters by profile
    join_constraints: use relationship cards; pre-aggregate before joins
    aggregation_rules: avoid fanout; aggregate AWB to batch before bank matching
    query_shape: pseudo_sql_pattern_available_from card fields and vendor implementations
    linked_rules: rule.logistics.required_scope_context; rule.logistics.amount_semantics_not_by_name; rule.logistics.grain_safe_reconciliation
    validation_tests:
    - validation_test.logistics.required_scope_context
    - validation_test.logistics.amount_semantics_not_by_name
    output_contract_id: output_contract.logistics_reconciliation_summary
    evidence_refs:
    - evidence.logistics_kb_doc
    - evidence.cognee_design_v4
    - evidence.unified_edge_scope
    produces_metric:
    - metric.unmatched_bank_credit_amount
    uses_reconciliation_profile:
    - reconciliation_profile.courier_batch_to_bank_credit
    rules:
    - rule.logistics.bank_reference_required_for_bank_match
    - rule.logistics.utr_preferred_for_bank_bridge
    output_contracts:
    - output_contract.logistics_reconciliation_summary
    query_pattern_boundary: Account filters and Business Flow Binding are resolved outside this generic query pattern.
    edge_enrichment_note: v4 adds PRODUCES_METRIC / USES_RECONCILIATION_PROFILE / REQUIRES_RULE / USES_OUTPUT_CONTRACT / USES_TABLE
      edges where targets exist.
```

```yaml
candidate_card:
  card_type: query_pattern
  card_id: query_pattern.logistics.end_to_end_logistics_money_flow_trace
  name: End To End Logistics Money Flow Trace
  fields:
    name: End To End Logistics Money Flow Trace
    description: Approved logistics query pattern for end_to_end_logistics_money_flow_trace.
    status: active
    confidence: high
    source_documents:
    - Logistics KB Doc.docx
    - Cognee KB Design v4.md
    - logistics_gold_std_raw_md_frame_v3.md
    - logistics_gold_std_canonical_card_frame_v5.md
    created_by: kb_authoring_assistant
    updated_by: kb_authoring_assistant
    version: 5.0-manifest-aligned
    pattern_name: end_to_end_logistics_money_flow_trace
    pattern_type: analytical; reconciliation; diagnostic
    supported_intents: end to end logistics money flow trace
    applicability_scope: logistics domain; account scope injected at runtime
    required_tables:
    - profile/vendor specific
    - table.zs_observe.shiprocket_oms
    - table.zs_observe.shiprocket_invoice
    - table.zs_observe.shiprocket_settlement
    optional_tables: bank_statement; fallback aggregator tables
    required_metrics: profile-specific metrics
    allowed_dimensions:
    - courier_partner
    - status
    - payment_mode
    - zone
    - date
    - awb when safe
    allowed_grains:
    - awb
    - order
    - day
    - month
    - batch
    recommended_date_columns:
    - source-specific recommended date columns
    semantic_filters:
    - is_active=true when present
    - status/value filters by profile
    join_constraints: use relationship cards; pre-aggregate before joins
    aggregation_rules: avoid fanout; aggregate AWB to batch before bank matching
    query_shape: pseudo_sql_pattern_available_from card fields and vendor implementations
    linked_rules: rule.logistics.required_scope_context; rule.logistics.amount_semantics_not_by_name; rule.logistics.grain_safe_reconciliation
    validation_tests:
    - validation_test.logistics.required_scope_context
    - validation_test.logistics.amount_semantics_not_by_name
    output_contract_id: output_contract.logistics_reconciliation_summary
    evidence_refs:
    - evidence.logistics_kb_doc
    - evidence.cognee_design_v4
    - evidence.unified_edge_scope
    produces_metric:
    - metric.freight_billed_amount
    - metric.cod_remitted_amount
    - metric.batch_settlement_amount
    - metric.reconciliation_gap_amount
    uses_reconciliation_profile:
    - reconciliation_profile.order_to_shipment
    - reconciliation_profile.shipment_to_freight_invoice
    - reconciliation_profile.cod_expected_to_courier_remittance
    - reconciliation_profile.courier_batch_to_bank_credit
    rules:
    - rule.logistics.business_flow_binding_required_for_cross_platform
    - rule.logistics.do_not_join_awb_to_bank_without_batch
    output_contracts:
    - output_contract.logistics_money_flow_trace
    query_pattern_boundary: Account filters and Business Flow Binding are resolved outside this generic query pattern.
    edge_enrichment_note: v4 adds PRODUCES_METRIC / USES_RECONCILIATION_PROFILE / REQUIRES_RULE / USES_OUTPUT_CONTRACT / USES_TABLE
      edges where targets exist.
```

### 4.23 rule cards

```yaml
candidate_card:
  card_type: rule
  card_id: rule.logistics.required_scope_context
  name: Required Scope Context
  fields:
    name: Required Scope Context
    description: 'Mandatory logistics rule: required_scope_context.'
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
    rule_name: required_scope_context
    rule_type: scope_filter/date_safety/join_safety/metric_semantics/aggregation_safety
    severity: critical
    applies_to:
    - logistics query patterns
    - metric implementations
    - reconciliation profiles
    rule_statement: required scope context
    required_pattern: semantic_check_required
    forbidden_pattern: unsafe assumption or unsupported source
    failure_mode: incorrect metric/reconciliation due to wrong scope, amount semantics, grain, or source reliability
    auto_fix_hint: use referenced table/column/value/profile/relationship cards and inject runtime scope
    validator_type: semantic_check
    evidence_refs:
    - evidence.logistics_kb_doc
    - evidence.cognee_design_v4
    - evidence.unified_edge_scope
```

```yaml
candidate_card:
  card_type: rule
  card_id: rule.logistics.business_flow_binding_required_for_cross_platform
  name: Business Flow Binding Required For Cross Platform
  fields:
    name: Business Flow Binding Required For Cross Platform
    description: 'Mandatory logistics rule: business_flow_binding_required_for_cross_platform.'
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
    rule_name: business_flow_binding_required_for_cross_platform
    rule_type: scope_filter/date_safety/join_safety/metric_semantics/aggregation_safety
    severity: high
    applies_to:
    - logistics query patterns
    - metric implementations
    - reconciliation profiles
    rule_statement: business flow binding required for cross platform
    required_pattern: semantic_check_required
    forbidden_pattern: unsafe assumption or unsupported source
    failure_mode: incorrect metric/reconciliation due to wrong scope, amount semantics, grain, or source reliability
    auto_fix_hint: use referenced table/column/value/profile/relationship cards and inject runtime scope
    validator_type: semantic_check
    evidence_refs:
    - evidence.logistics_kb_doc
    - evidence.cognee_design_v4
    - evidence.unified_edge_scope
```

```yaml
candidate_card:
  card_type: rule
  card_id: rule.logistics.do_not_create_bfb_from_generic_vendor_doc
  name: Do Not Create Bfb From Generic Vendor Doc
  fields:
    name: Do Not Create Bfb From Generic Vendor Doc
    description: 'Mandatory logistics rule: do_not_create_bfb_from_generic_vendor_doc.'
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
    rule_name: do_not_create_bfb_from_generic_vendor_doc
    rule_type: scope_filter/date_safety/join_safety/metric_semantics/aggregation_safety
    severity: high
    applies_to:
    - logistics query patterns
    - metric implementations
    - reconciliation profiles
    rule_statement: do not create bfb from generic vendor doc
    required_pattern: semantic_check_required
    forbidden_pattern: unsafe assumption or unsupported source
    failure_mode: incorrect metric/reconciliation due to wrong scope, amount semantics, grain, or source reliability
    auto_fix_hint: use referenced table/column/value/profile/relationship cards and inject runtime scope
    validator_type: semantic_check
    evidence_refs:
    - evidence.logistics_kb_doc
    - evidence.cognee_design_v4
    - evidence.unified_edge_scope
```

```yaml
candidate_card:
  card_type: rule
  card_id: rule.logistics.amount_semantics_not_by_name
  name: Amount Semantics Not By Name
  fields:
    name: Amount Semantics Not By Name
    description: 'Mandatory logistics rule: amount_semantics_not_by_name.'
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
    rule_name: amount_semantics_not_by_name
    rule_type: scope_filter/date_safety/join_safety/metric_semantics/aggregation_safety
    severity: critical
    applies_to:
    - logistics query patterns
    - metric implementations
    - reconciliation profiles
    rule_statement: amount semantics not by name
    required_pattern: semantic_check_required
    forbidden_pattern: unsafe assumption or unsupported source
    failure_mode: incorrect metric/reconciliation due to wrong scope, amount semantics, grain, or source reliability
    auto_fix_hint: use referenced table/column/value/profile/relationship cards and inject runtime scope
    validator_type: semantic_check
    evidence_refs:
    - evidence.logistics_kb_doc
    - evidence.cognee_design_v4
    - evidence.unified_edge_scope
```

```yaml
candidate_card:
  card_type: rule
  card_id: rule.logistics.charged_amount_table_specific
  name: Charged Amount Table Specific
  fields:
    name: Charged Amount Table Specific
    description: 'Mandatory logistics rule: charged_amount_table_specific.'
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
    rule_name: charged_amount_table_specific
    rule_type: scope_filter/date_safety/join_safety/metric_semantics/aggregation_safety
    severity: high
    applies_to:
    - logistics query patterns
    - metric implementations
    - reconciliation profiles
    rule_statement: charged amount table specific
    required_pattern: semantic_check_required
    forbidden_pattern: unsafe assumption or unsupported source
    failure_mode: incorrect metric/reconciliation due to wrong scope, amount semantics, grain, or source reliability
    auto_fix_hint: use referenced table/column/value/profile/relationship cards and inject runtime scope
    validator_type: semantic_check
    evidence_refs:
    - evidence.logistics_kb_doc
    - evidence.cognee_design_v4
    - evidence.unified_edge_scope
```

```yaml
candidate_card:
  card_type: rule
  card_id: rule.logistics.active_filter_when_available
  name: Active Filter When Available
  fields:
    name: Active Filter When Available
    description: 'Mandatory logistics rule: active_filter_when_available.'
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
    rule_name: active_filter_when_available
    rule_type: scope_filter/date_safety/join_safety/metric_semantics/aggregation_safety
    severity: high
    applies_to:
    - logistics query patterns
    - metric implementations
    - reconciliation profiles
    rule_statement: active filter when available
    required_pattern: semantic_check_required
    forbidden_pattern: unsafe assumption or unsupported source
    failure_mode: incorrect metric/reconciliation due to wrong scope, amount semantics, grain, or source reliability
    auto_fix_hint: use referenced table/column/value/profile/relationship cards and inject runtime scope
    validator_type: semantic_check
    evidence_refs:
    - evidence.logistics_kb_doc
    - evidence.cognee_design_v4
    - evidence.unified_edge_scope
```

```yaml
candidate_card:
  card_type: rule
  card_id: rule.logistics.empty_tables_schema_only
  name: Empty Tables Schema Only
  fields:
    name: Empty Tables Schema Only
    description: 'Mandatory logistics rule: empty_tables_schema_only.'
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
    rule_name: empty_tables_schema_only
    rule_type: scope_filter/date_safety/join_safety/metric_semantics/aggregation_safety
    severity: critical
    applies_to:
    - logistics query patterns
    - metric implementations
    - reconciliation profiles
    rule_statement: empty tables schema only
    required_pattern: semantic_check_required
    forbidden_pattern: unsafe assumption or unsupported source
    failure_mode: incorrect metric/reconciliation due to wrong scope, amount semantics, grain, or source reliability
    auto_fix_hint: use referenced table/column/value/profile/relationship cards and inject runtime scope
    validator_type: semantic_check
    evidence_refs:
    - evidence.logistics_kb_doc
    - evidence.cognee_design_v4
    - evidence.unified_edge_scope
```

```yaml
candidate_card:
  card_type: rule
  card_id: rule.logistics.low_confidence_requires_warning
  name: Low Confidence Requires Warning
  fields:
    name: Low Confidence Requires Warning
    description: 'Mandatory logistics rule: low_confidence_requires_warning.'
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
    rule_name: low_confidence_requires_warning
    rule_type: scope_filter/date_safety/join_safety/metric_semantics/aggregation_safety
    severity: high
    applies_to:
    - logistics query patterns
    - metric implementations
    - reconciliation profiles
    rule_statement: low confidence requires warning
    required_pattern: semantic_check_required
    forbidden_pattern: unsafe assumption or unsupported source
    failure_mode: incorrect metric/reconciliation due to wrong scope, amount semantics, grain, or source reliability
    auto_fix_hint: use referenced table/column/value/profile/relationship cards and inject runtime scope
    validator_type: semantic_check
    evidence_refs:
    - evidence.logistics_kb_doc
    - evidence.cognee_design_v4
    - evidence.unified_edge_scope
```

```yaml
candidate_card:
  card_type: rule
  card_id: rule.logistics.fallback_sources_explicit_only
  name: Fallback Sources Explicit Only
  fields:
    name: Fallback Sources Explicit Only
    description: 'Mandatory logistics rule: fallback_sources_explicit_only.'
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
    rule_name: fallback_sources_explicit_only
    rule_type: scope_filter/date_safety/join_safety/metric_semantics/aggregation_safety
    severity: high
    applies_to:
    - logistics query patterns
    - metric implementations
    - reconciliation profiles
    rule_statement: fallback sources explicit only
    required_pattern: semantic_check_required
    forbidden_pattern: unsafe assumption or unsupported source
    failure_mode: incorrect metric/reconciliation due to wrong scope, amount semantics, grain, or source reliability
    auto_fix_hint: use referenced table/column/value/profile/relationship cards and inject runtime scope
    validator_type: semantic_check
    evidence_refs:
    - evidence.logistics_kb_doc
    - evidence.cognee_design_v4
    - evidence.unified_edge_scope
```

```yaml
candidate_card:
  card_type: rule
  card_id: rule.logistics.awb_primary_reconciliation_unit
  name: Awb Primary Reconciliation Unit
  fields:
    name: Awb Primary Reconciliation Unit
    description: 'Mandatory logistics rule: awb_primary_reconciliation_unit.'
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
    rule_name: awb_primary_reconciliation_unit
    rule_type: scope_filter/date_safety/join_safety/metric_semantics/aggregation_safety
    severity: high
    applies_to:
    - logistics query patterns
    - metric implementations
    - reconciliation profiles
    rule_statement: awb primary reconciliation unit
    required_pattern: semantic_check_required
    forbidden_pattern: unsafe assumption or unsupported source
    failure_mode: incorrect metric/reconciliation due to wrong scope, amount semantics, grain, or source reliability
    auto_fix_hint: use referenced table/column/value/profile/relationship cards and inject runtime scope
    validator_type: semantic_check
    evidence_refs:
    - evidence.logistics_kb_doc
    - evidence.cognee_design_v4
    - evidence.unified_edge_scope
```

```yaml
candidate_card:
  card_type: rule
  card_id: rule.logistics.do_not_join_awb_to_bank_without_batch
  name: Do Not Join Awb To Bank Without Batch
  fields:
    name: Do Not Join Awb To Bank Without Batch
    description: 'Mandatory logistics rule: do_not_join_awb_to_bank_without_batch.'
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
    rule_name: do_not_join_awb_to_bank_without_batch
    rule_type: scope_filter/date_safety/join_safety/metric_semantics/aggregation_safety
    severity: critical
    applies_to:
    - logistics query patterns
    - metric implementations
    - reconciliation profiles
    rule_statement: do not join awb to bank without batch
    required_pattern: semantic_check_required
    forbidden_pattern: unsafe assumption or unsupported source
    failure_mode: incorrect metric/reconciliation due to wrong scope, amount semantics, grain, or source reliability
    auto_fix_hint: use referenced table/column/value/profile/relationship cards and inject runtime scope
    validator_type: semantic_check
    evidence_refs:
    - evidence.logistics_kb_doc
    - evidence.cognee_design_v4
    - evidence.unified_edge_scope
```

```yaml
candidate_card:
  card_type: rule
  card_id: rule.logistics.preaggregate_before_order_join
  name: Preaggregate Before Order Join
  fields:
    name: Preaggregate Before Order Join
    description: 'Mandatory logistics rule: preaggregate_before_order_join.'
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
    rule_name: preaggregate_before_order_join
    rule_type: scope_filter/date_safety/join_safety/metric_semantics/aggregation_safety
    severity: high
    applies_to:
    - logistics query patterns
    - metric implementations
    - reconciliation profiles
    rule_statement: preaggregate before order join
    required_pattern: semantic_check_required
    forbidden_pattern: unsafe assumption or unsupported source
    failure_mode: incorrect metric/reconciliation due to wrong scope, amount semantics, grain, or source reliability
    auto_fix_hint: use referenced table/column/value/profile/relationship cards and inject runtime scope
    validator_type: semantic_check
    evidence_refs:
    - evidence.logistics_kb_doc
    - evidence.cognee_design_v4
    - evidence.unified_edge_scope
```

```yaml
candidate_card:
  card_type: rule
  card_id: rule.logistics.preaggregate_fee_rows_before_join
  name: Preaggregate Fee Rows Before Join
  fields:
    name: Preaggregate Fee Rows Before Join
    description: 'Mandatory logistics rule: preaggregate_fee_rows_before_join.'
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
    rule_name: preaggregate_fee_rows_before_join
    rule_type: scope_filter/date_safety/join_safety/metric_semantics/aggregation_safety
    severity: high
    applies_to:
    - logistics query patterns
    - metric implementations
    - reconciliation profiles
    rule_statement: preaggregate fee rows before join
    required_pattern: semantic_check_required
    forbidden_pattern: unsafe assumption or unsupported source
    failure_mode: incorrect metric/reconciliation due to wrong scope, amount semantics, grain, or source reliability
    auto_fix_hint: use referenced table/column/value/profile/relationship cards and inject runtime scope
    validator_type: semantic_check
    evidence_refs:
    - evidence.logistics_kb_doc
    - evidence.cognee_design_v4
    - evidence.unified_edge_scope
```

```yaml
candidate_card:
  card_type: rule
  card_id: rule.logistics.parse_shiprocket_order_id_before_shopify_join
  name: Parse Shiprocket Order Id Before Shopify Join
  fields:
    name: Parse Shiprocket Order Id Before Shopify Join
    description: 'Mandatory logistics rule: parse_shiprocket_order_id_before_shopify_join.'
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
    rule_name: parse_shiprocket_order_id_before_shopify_join
    rule_type: scope_filter/date_safety/join_safety/metric_semantics/aggregation_safety
    severity: high
    applies_to:
    - logistics query patterns
    - metric implementations
    - reconciliation profiles
    rule_statement: parse shiprocket order id before shopify join
    required_pattern: semantic_check_required
    forbidden_pattern: unsafe assumption or unsupported source
    failure_mode: incorrect metric/reconciliation due to wrong scope, amount semantics, grain, or source reliability
    auto_fix_hint: use referenced table/column/value/profile/relationship cards and inject runtime scope
    validator_type: semantic_check
    evidence_refs:
    - evidence.logistics_kb_doc
    - evidence.cognee_design_v4
    - evidence.unified_edge_scope
```

```yaml
candidate_card:
  card_type: rule
  card_id: rule.logistics.xpressbees_native_low_confidence
  name: Xpressbees Native Low Confidence
  fields:
    name: Xpressbees Native Low Confidence
    description: 'Mandatory logistics rule: xpressbees_native_low_confidence.'
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
    rule_name: xpressbees_native_low_confidence
    rule_type: scope_filter/date_safety/join_safety/metric_semantics/aggregation_safety
    severity: high
    applies_to:
    - logistics query patterns
    - metric implementations
    - reconciliation profiles
    rule_statement: xpressbees native low confidence
    required_pattern: semantic_check_required
    forbidden_pattern: unsafe assumption or unsupported source
    failure_mode: incorrect metric/reconciliation due to wrong scope, amount semantics, grain, or source reliability
    auto_fix_hint: use referenced table/column/value/profile/relationship cards and inject runtime scope
    validator_type: semantic_check
    evidence_refs:
    - evidence.logistics_kb_doc
    - evidence.cognee_design_v4
    - evidence.unified_edge_scope
```

```yaml
candidate_card:
  card_type: rule
  card_id: rule.logistics.xpressbees_fallback_shiprocket_preferred
  name: Xpressbees Fallback Shiprocket Preferred
  fields:
    name: Xpressbees Fallback Shiprocket Preferred
    description: 'Mandatory logistics rule: xpressbees_fallback_shiprocket_preferred.'
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
    rule_name: xpressbees_fallback_shiprocket_preferred
    rule_type: scope_filter/date_safety/join_safety/metric_semantics/aggregation_safety
    severity: high
    applies_to:
    - logistics query patterns
    - metric implementations
    - reconciliation profiles
    rule_statement: xpressbees fallback shiprocket preferred
    required_pattern: semantic_check_required
    forbidden_pattern: unsafe assumption or unsupported source
    failure_mode: incorrect metric/reconciliation due to wrong scope, amount semantics, grain, or source reliability
    auto_fix_hint: use referenced table/column/value/profile/relationship cards and inject runtime scope
    validator_type: semantic_check
    evidence_refs:
    - evidence.logistics_kb_doc
    - evidence.cognee_design_v4
    - evidence.unified_edge_scope
```

```yaml
candidate_card:
  card_type: rule
  card_id: rule.logistics.shadowfax_no_native_settlement
  name: Shadowfax No Native Settlement
  fields:
    name: Shadowfax No Native Settlement
    description: 'Mandatory logistics rule: shadowfax_no_native_settlement.'
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
    rule_name: shadowfax_no_native_settlement
    rule_type: scope_filter/date_safety/join_safety/metric_semantics/aggregation_safety
    severity: high
    applies_to:
    - logistics query patterns
    - metric implementations
    - reconciliation profiles
    rule_statement: shadowfax no native settlement
    required_pattern: semantic_check_required
    forbidden_pattern: unsafe assumption or unsupported source
    failure_mode: incorrect metric/reconciliation due to wrong scope, amount semantics, grain, or source reliability
    auto_fix_hint: use referenced table/column/value/profile/relationship cards and inject runtime scope
    validator_type: semantic_check
    evidence_refs:
    - evidence.logistics_kb_doc
    - evidence.cognee_design_v4
    - evidence.unified_edge_scope
```

```yaml
candidate_card:
  card_type: rule
  card_id: rule.logistics.ecom_no_native_table
  name: Ecom No Native Table
  fields:
    name: Ecom No Native Table
    description: 'Mandatory logistics rule: ecom_no_native_table.'
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
    rule_name: ecom_no_native_table
    rule_type: scope_filter/date_safety/join_safety/metric_semantics/aggregation_safety
    severity: high
    applies_to:
    - logistics query patterns
    - metric implementations
    - reconciliation profiles
    rule_statement: ecom no native table
    required_pattern: semantic_check_required
    forbidden_pattern: unsafe assumption or unsupported source
    failure_mode: incorrect metric/reconciliation due to wrong scope, amount semantics, grain, or source reliability
    auto_fix_hint: use referenced table/column/value/profile/relationship cards and inject runtime scope
    validator_type: semantic_check
    evidence_refs:
    - evidence.logistics_kb_doc
    - evidence.cognee_design_v4
    - evidence.unified_edge_scope
```

```yaml
candidate_card:
  card_type: rule
  card_id: rule.logistics.dtdc_invoice_empty
  name: Dtdc Invoice Empty
  fields:
    name: Dtdc Invoice Empty
    description: 'Mandatory logistics rule: dtdc_invoice_empty.'
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
    rule_name: dtdc_invoice_empty
    rule_type: scope_filter/date_safety/join_safety/metric_semantics/aggregation_safety
    severity: high
    applies_to:
    - logistics query patterns
    - metric implementations
    - reconciliation profiles
    rule_statement: dtdc invoice empty
    required_pattern: semantic_check_required
    forbidden_pattern: unsafe assumption or unsupported source
    failure_mode: incorrect metric/reconciliation due to wrong scope, amount semantics, grain, or source reliability
    auto_fix_hint: use referenced table/column/value/profile/relationship cards and inject runtime scope
    validator_type: semantic_check
    evidence_refs:
    - evidence.logistics_kb_doc
    - evidence.cognee_design_v4
    - evidence.unified_edge_scope
```

```yaml
candidate_card:
  card_type: rule
  card_id: rule.logistics.ekart_invoice_empty
  name: Ekart Invoice Empty
  fields:
    name: Ekart Invoice Empty
    description: 'Mandatory logistics rule: ekart_invoice_empty.'
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
    rule_name: ekart_invoice_empty
    rule_type: scope_filter/date_safety/join_safety/metric_semantics/aggregation_safety
    severity: high
    applies_to:
    - logistics query patterns
    - metric implementations
    - reconciliation profiles
    rule_statement: ekart invoice empty
    required_pattern: semantic_check_required
    forbidden_pattern: unsafe assumption or unsupported source
    failure_mode: incorrect metric/reconciliation due to wrong scope, amount semantics, grain, or source reliability
    auto_fix_hint: use referenced table/column/value/profile/relationship cards and inject runtime scope
    validator_type: semantic_check
    evidence_refs:
    - evidence.logistics_kb_doc
    - evidence.cognee_design_v4
    - evidence.unified_edge_scope
```

```yaml
candidate_card:
  card_type: rule
  card_id: rule.logistics.shiprocket_settlement_report_empty
  name: Shiprocket Settlement Report Empty
  fields:
    name: Shiprocket Settlement Report Empty
    description: 'Mandatory logistics rule: shiprocket_settlement_report_empty.'
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
    rule_name: shiprocket_settlement_report_empty
    rule_type: scope_filter/date_safety/join_safety/metric_semantics/aggregation_safety
    severity: high
    applies_to:
    - logistics query patterns
    - metric implementations
    - reconciliation profiles
    rule_statement: shiprocket settlement report empty
    required_pattern: semantic_check_required
    forbidden_pattern: unsafe assumption or unsupported source
    failure_mode: incorrect metric/reconciliation due to wrong scope, amount semantics, grain, or source reliability
    auto_fix_hint: use referenced table/column/value/profile/relationship cards and inject runtime scope
    validator_type: semantic_check
    evidence_refs:
    - evidence.logistics_kb_doc
    - evidence.cognee_design_v4
    - evidence.unified_edge_scope
```

```yaml
candidate_card:
  card_type: rule
  card_id: rule.logistics.cod_fee_only_for_cod
  name: Cod Fee Only For Cod
  fields:
    name: Cod Fee Only For Cod
    description: 'Mandatory logistics rule: cod_fee_only_for_cod.'
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
    rule_name: cod_fee_only_for_cod
    rule_type: scope_filter/date_safety/join_safety/metric_semantics/aggregation_safety
    severity: high
    applies_to:
    - logistics query patterns
    - metric implementations
    - reconciliation profiles
    rule_statement: cod fee only for cod
    required_pattern: semantic_check_required
    forbidden_pattern: unsafe assumption or unsupported source
    failure_mode: incorrect metric/reconciliation due to wrong scope, amount semantics, grain, or source reliability
    auto_fix_hint: use referenced table/column/value/profile/relationship cards and inject runtime scope
    validator_type: semantic_check
    evidence_refs:
    - evidence.logistics_kb_doc
    - evidence.cognee_design_v4
    - evidence.unified_edge_scope
```

```yaml
candidate_card:
  card_type: rule
  card_id: rule.logistics.rto_charge_only_for_rto
  name: Rto Charge Only For Rto
  fields:
    name: Rto Charge Only For Rto
    description: 'Mandatory logistics rule: rto_charge_only_for_rto.'
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
    rule_name: rto_charge_only_for_rto
    rule_type: scope_filter/date_safety/join_safety/metric_semantics/aggregation_safety
    severity: high
    applies_to:
    - logistics query patterns
    - metric implementations
    - reconciliation profiles
    rule_statement: rto charge only for rto
    required_pattern: semantic_check_required
    forbidden_pattern: unsafe assumption or unsupported source
    failure_mode: incorrect metric/reconciliation due to wrong scope, amount semantics, grain, or source reliability
    auto_fix_hint: use referenced table/column/value/profile/relationship cards and inject runtime scope
    validator_type: semantic_check
    evidence_refs:
    - evidence.logistics_kb_doc
    - evidence.cognee_design_v4
    - evidence.unified_edge_scope
```

```yaml
candidate_card:
  card_type: rule
  card_id: rule.logistics.zone_value_profile_required
  name: Zone Value Profile Required
  fields:
    name: Zone Value Profile Required
    description: 'Mandatory logistics rule: zone_value_profile_required.'
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
    rule_name: zone_value_profile_required
    rule_type: scope_filter/date_safety/join_safety/metric_semantics/aggregation_safety
    severity: high
    applies_to:
    - logistics query patterns
    - metric implementations
    - reconciliation profiles
    rule_statement: zone value profile required
    required_pattern: semantic_check_required
    forbidden_pattern: unsafe assumption or unsupported source
    failure_mode: incorrect metric/reconciliation due to wrong scope, amount semantics, grain, or source reliability
    auto_fix_hint: use referenced table/column/value/profile/relationship cards and inject runtime scope
    validator_type: semantic_check
    evidence_refs:
    - evidence.logistics_kb_doc
    - evidence.cognee_design_v4
    - evidence.unified_edge_scope
```

```yaml
candidate_card:
  card_type: rule
  card_id: rule.logistics.payment_mode_value_profile_required
  name: Payment Mode Value Profile Required
  fields:
    name: Payment Mode Value Profile Required
    description: 'Mandatory logistics rule: payment_mode_value_profile_required.'
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
    rule_name: payment_mode_value_profile_required
    rule_type: scope_filter/date_safety/join_safety/metric_semantics/aggregation_safety
    severity: high
    applies_to:
    - logistics query patterns
    - metric implementations
    - reconciliation profiles
    rule_statement: payment mode value profile required
    required_pattern: semantic_check_required
    forbidden_pattern: unsafe assumption or unsupported source
    failure_mode: incorrect metric/reconciliation due to wrong scope, amount semantics, grain, or source reliability
    auto_fix_hint: use referenced table/column/value/profile/relationship cards and inject runtime scope
    validator_type: semantic_check
    evidence_refs:
    - evidence.logistics_kb_doc
    - evidence.cognee_design_v4
    - evidence.unified_edge_scope
```

```yaml
candidate_card:
  card_type: rule
  card_id: rule.logistics.courier_partner_filter_exact_or_profiled
  name: Courier Partner Filter Exact Or Profiled
  fields:
    name: Courier Partner Filter Exact Or Profiled
    description: 'Mandatory logistics rule: courier_partner_filter_exact_or_profiled.'
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
    rule_name: courier_partner_filter_exact_or_profiled
    rule_type: scope_filter/date_safety/join_safety/metric_semantics/aggregation_safety
    severity: high
    applies_to:
    - logistics query patterns
    - metric implementations
    - reconciliation profiles
    rule_statement: courier partner filter exact or profiled
    required_pattern: semantic_check_required
    forbidden_pattern: unsafe assumption or unsupported source
    failure_mode: incorrect metric/reconciliation due to wrong scope, amount semantics, grain, or source reliability
    auto_fix_hint: use referenced table/column/value/profile/relationship cards and inject runtime scope
    validator_type: semantic_check
    evidence_refs:
    - evidence.logistics_kb_doc
    - evidence.cognee_design_v4
    - evidence.unified_edge_scope
```

```yaml
candidate_card:
  card_type: rule
  card_id: rule.logistics.date_column_must_match_metric
  name: Date Column Must Match Metric
  fields:
    name: Date Column Must Match Metric
    description: 'Mandatory logistics rule: date_column_must_match_metric.'
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
    rule_name: date_column_must_match_metric
    rule_type: scope_filter/date_safety/join_safety/metric_semantics/aggregation_safety
    severity: high
    applies_to:
    - logistics query patterns
    - metric implementations
    - reconciliation profiles
    rule_statement: date column must match metric
    required_pattern: semantic_check_required
    forbidden_pattern: unsafe assumption or unsupported source
    failure_mode: incorrect metric/reconciliation due to wrong scope, amount semantics, grain, or source reliability
    auto_fix_hint: use referenced table/column/value/profile/relationship cards and inject runtime scope
    validator_type: semantic_check
    evidence_refs:
    - evidence.logistics_kb_doc
    - evidence.cognee_design_v4
    - evidence.unified_edge_scope
```

```yaml
candidate_card:
  card_type: rule
  card_id: rule.logistics.settlement_date_for_cod_remittance
  name: Settlement Date For Cod Remittance
  fields:
    name: Settlement Date For Cod Remittance
    description: 'Mandatory logistics rule: settlement_date_for_cod_remittance.'
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
    rule_name: settlement_date_for_cod_remittance
    rule_type: scope_filter/date_safety/join_safety/metric_semantics/aggregation_safety
    severity: high
    applies_to:
    - logistics query patterns
    - metric implementations
    - reconciliation profiles
    rule_statement: settlement date for cod remittance
    required_pattern: semantic_check_required
    forbidden_pattern: unsafe assumption or unsupported source
    failure_mode: incorrect metric/reconciliation due to wrong scope, amount semantics, grain, or source reliability
    auto_fix_hint: use referenced table/column/value/profile/relationship cards and inject runtime scope
    validator_type: semantic_check
    evidence_refs:
    - evidence.logistics_kb_doc
    - evidence.cognee_design_v4
    - evidence.unified_edge_scope
```

```yaml
candidate_card:
  card_type: rule
  card_id: rule.logistics.delivered_date_for_delivery_metrics
  name: Delivered Date For Delivery Metrics
  fields:
    name: Delivered Date For Delivery Metrics
    description: 'Mandatory logistics rule: delivered_date_for_delivery_metrics.'
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
    rule_name: delivered_date_for_delivery_metrics
    rule_type: scope_filter/date_safety/join_safety/metric_semantics/aggregation_safety
    severity: high
    applies_to:
    - logistics query patterns
    - metric implementations
    - reconciliation profiles
    rule_statement: delivered date for delivery metrics
    required_pattern: semantic_check_required
    forbidden_pattern: unsafe assumption or unsupported source
    failure_mode: incorrect metric/reconciliation due to wrong scope, amount semantics, grain, or source reliability
    auto_fix_hint: use referenced table/column/value/profile/relationship cards and inject runtime scope
    validator_type: semantic_check
    evidence_refs:
    - evidence.logistics_kb_doc
    - evidence.cognee_design_v4
    - evidence.unified_edge_scope
```

```yaml
candidate_card:
  card_type: rule
  card_id: rule.logistics.bank_reference_required_for_bank_match
  name: Bank Reference Required For Bank Match
  fields:
    name: Bank Reference Required For Bank Match
    description: 'Mandatory logistics rule: bank_reference_required_for_bank_match.'
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
    rule_name: bank_reference_required_for_bank_match
    rule_type: scope_filter/date_safety/join_safety/metric_semantics/aggregation_safety
    severity: high
    applies_to:
    - logistics query patterns
    - metric implementations
    - reconciliation profiles
    rule_statement: bank reference required for bank match
    required_pattern: semantic_check_required
    forbidden_pattern: unsafe assumption or unsupported source
    failure_mode: incorrect metric/reconciliation due to wrong scope, amount semantics, grain, or source reliability
    auto_fix_hint: use referenced table/column/value/profile/relationship cards and inject runtime scope
    validator_type: semantic_check
    evidence_refs:
    - evidence.logistics_kb_doc
    - evidence.cognee_design_v4
    - evidence.unified_edge_scope
```

```yaml
candidate_card:
  card_type: rule
  card_id: rule.logistics.utr_preferred_for_bank_bridge
  name: Utr Preferred For Bank Bridge
  fields:
    name: Utr Preferred For Bank Bridge
    description: 'Mandatory logistics rule: utr_preferred_for_bank_bridge.'
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
    rule_name: utr_preferred_for_bank_bridge
    rule_type: scope_filter/date_safety/join_safety/metric_semantics/aggregation_safety
    severity: high
    applies_to:
    - logistics query patterns
    - metric implementations
    - reconciliation profiles
    rule_statement: utr preferred for bank bridge
    required_pattern: semantic_check_required
    forbidden_pattern: unsafe assumption or unsupported source
    failure_mode: incorrect metric/reconciliation due to wrong scope, amount semantics, grain, or source reliability
    auto_fix_hint: use referenced table/column/value/profile/relationship cards and inject runtime scope
    validator_type: semantic_check
    evidence_refs:
    - evidence.logistics_kb_doc
    - evidence.cognee_design_v4
    - evidence.unified_edge_scope
```

```yaml
candidate_card:
  card_type: rule
  card_id: rule.logistics.batch_amount_deduplicate
  name: Batch Amount Deduplicate
  fields:
    name: Batch Amount Deduplicate
    description: 'Mandatory logistics rule: batch_amount_deduplicate.'
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
    rule_name: batch_amount_deduplicate
    rule_type: scope_filter/date_safety/join_safety/metric_semantics/aggregation_safety
    severity: high
    applies_to:
    - logistics query patterns
    - metric implementations
    - reconciliation profiles
    rule_statement: batch amount deduplicate
    required_pattern: semantic_check_required
    forbidden_pattern: unsafe assumption or unsupported source
    failure_mode: incorrect metric/reconciliation due to wrong scope, amount semantics, grain, or source reliability
    auto_fix_hint: use referenced table/column/value/profile/relationship cards and inject runtime scope
    validator_type: semantic_check
    evidence_refs:
    - evidence.logistics_kb_doc
    - evidence.cognee_design_v4
    - evidence.unified_edge_scope
```

```yaml
candidate_card:
  card_type: rule
  card_id: rule.logistics.total_amount_of_batch_not_awb_level
  name: Total Amount Of Batch Not Awb Level
  fields:
    name: Total Amount Of Batch Not Awb Level
    description: 'Mandatory logistics rule: total_amount_of_batch_not_awb_level.'
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
    rule_name: total_amount_of_batch_not_awb_level
    rule_type: scope_filter/date_safety/join_safety/metric_semantics/aggregation_safety
    severity: high
    applies_to:
    - logistics query patterns
    - metric implementations
    - reconciliation profiles
    rule_statement: total amount of batch not awb level
    required_pattern: semantic_check_required
    forbidden_pattern: unsafe assumption or unsupported source
    failure_mode: incorrect metric/reconciliation due to wrong scope, amount semantics, grain, or source reliability
    auto_fix_hint: use referenced table/column/value/profile/relationship cards and inject runtime scope
    validator_type: semantic_check
    evidence_refs:
    - evidence.logistics_kb_doc
    - evidence.cognee_design_v4
    - evidence.unified_edge_scope
```

```yaml
candidate_card:
  card_type: rule
  card_id: rule.logistics.delhivery_charged_amount_declared_value
  name: Delhivery Charged Amount Declared Value
  fields:
    name: Delhivery Charged Amount Declared Value
    description: 'Mandatory logistics rule: delhivery_charged_amount_declared_value.'
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
    rule_name: delhivery_charged_amount_declared_value
    rule_type: scope_filter/date_safety/join_safety/metric_semantics/aggregation_safety
    severity: high
    applies_to:
    - logistics query patterns
    - metric implementations
    - reconciliation profiles
    rule_statement: delhivery charged amount declared value
    required_pattern: semantic_check_required
    forbidden_pattern: unsafe assumption or unsupported source
    failure_mode: incorrect metric/reconciliation due to wrong scope, amount semantics, grain, or source reliability
    auto_fix_hint: use referenced table/column/value/profile/relationship cards and inject runtime scope
    validator_type: semantic_check
    evidence_refs:
    - evidence.logistics_kb_doc
    - evidence.cognee_design_v4
    - evidence.unified_edge_scope
```

```yaml
candidate_card:
  card_type: rule
  card_id: rule.logistics.shiprocket_oms_charged_amount_declared_value
  name: Shiprocket Oms Charged Amount Declared Value
  fields:
    name: Shiprocket Oms Charged Amount Declared Value
    description: 'Mandatory logistics rule: shiprocket_oms_charged_amount_declared_value.'
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
    rule_name: shiprocket_oms_charged_amount_declared_value
    rule_type: scope_filter/date_safety/join_safety/metric_semantics/aggregation_safety
    severity: high
    applies_to:
    - logistics query patterns
    - metric implementations
    - reconciliation profiles
    rule_statement: shiprocket oms charged amount declared value
    required_pattern: semantic_check_required
    forbidden_pattern: unsafe assumption or unsupported source
    failure_mode: incorrect metric/reconciliation due to wrong scope, amount semantics, grain, or source reliability
    auto_fix_hint: use referenced table/column/value/profile/relationship cards and inject runtime scope
    validator_type: semantic_check
    evidence_refs:
    - evidence.logistics_kb_doc
    - evidence.cognee_design_v4
    - evidence.unified_edge_scope
```

```yaml
candidate_card:
  card_type: rule
  card_id: rule.logistics.shiprocket_invoice_charged_amount_freight
  name: Shiprocket Invoice Charged Amount Freight
  fields:
    name: Shiprocket Invoice Charged Amount Freight
    description: 'Mandatory logistics rule: shiprocket_invoice_charged_amount_freight.'
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
    rule_name: shiprocket_invoice_charged_amount_freight
    rule_type: scope_filter/date_safety/join_safety/metric_semantics/aggregation_safety
    severity: high
    applies_to:
    - logistics query patterns
    - metric implementations
    - reconciliation profiles
    rule_statement: shiprocket invoice charged amount freight
    required_pattern: semantic_check_required
    forbidden_pattern: unsafe assumption or unsupported source
    failure_mode: incorrect metric/reconciliation due to wrong scope, amount semantics, grain, or source reliability
    auto_fix_hint: use referenced table/column/value/profile/relationship cards and inject runtime scope
    validator_type: semantic_check
    evidence_refs:
    - evidence.logistics_kb_doc
    - evidence.cognee_design_v4
    - evidence.unified_edge_scope
```

```yaml
candidate_card:
  card_type: rule
  card_id: rule.logistics.shiprocket_settlement_charged_amount_cod
  name: Shiprocket Settlement Charged Amount Cod
  fields:
    name: Shiprocket Settlement Charged Amount Cod
    description: 'Mandatory logistics rule: shiprocket_settlement_charged_amount_cod.'
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
    rule_name: shiprocket_settlement_charged_amount_cod
    rule_type: scope_filter/date_safety/join_safety/metric_semantics/aggregation_safety
    severity: high
    applies_to:
    - logistics query patterns
    - metric implementations
    - reconciliation profiles
    rule_statement: shiprocket settlement charged amount cod
    required_pattern: semantic_check_required
    forbidden_pattern: unsafe assumption or unsupported source
    failure_mode: incorrect metric/reconciliation due to wrong scope, amount semantics, grain, or source reliability
    auto_fix_hint: use referenced table/column/value/profile/relationship cards and inject runtime scope
    validator_type: semantic_check
    evidence_refs:
    - evidence.logistics_kb_doc
    - evidence.cognee_design_v4
    - evidence.unified_edge_scope
```

```yaml
candidate_card:
  card_type: rule
  card_id: rule.logistics.dtdc_settlement_charged_amount_cod_value
  name: Dtdc Settlement Charged Amount Cod Value
  fields:
    name: Dtdc Settlement Charged Amount Cod Value
    description: 'Mandatory logistics rule: dtdc_settlement_charged_amount_cod_value.'
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
    rule_name: dtdc_settlement_charged_amount_cod_value
    rule_type: scope_filter/date_safety/join_safety/metric_semantics/aggregation_safety
    severity: high
    applies_to:
    - logistics query patterns
    - metric implementations
    - reconciliation profiles
    rule_statement: dtdc settlement charged amount cod value
    required_pattern: semantic_check_required
    forbidden_pattern: unsafe assumption or unsupported source
    failure_mode: incorrect metric/reconciliation due to wrong scope, amount semantics, grain, or source reliability
    auto_fix_hint: use referenced table/column/value/profile/relationship cards and inject runtime scope
    validator_type: semantic_check
    evidence_refs:
    - evidence.logistics_kb_doc
    - evidence.cognee_design_v4
    - evidence.unified_edge_scope
```

```yaml
candidate_card:
  card_type: rule
  card_id: rule.logistics.ekart_settlement_transaction_type_required
  name: Ekart Settlement Transaction Type Required
  fields:
    name: Ekart Settlement Transaction Type Required
    description: 'Mandatory logistics rule: ekart_settlement_transaction_type_required.'
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
    rule_name: ekart_settlement_transaction_type_required
    rule_type: scope_filter/date_safety/join_safety/metric_semantics/aggregation_safety
    severity: high
    applies_to:
    - logistics query patterns
    - metric implementations
    - reconciliation profiles
    rule_statement: ekart settlement transaction type required
    required_pattern: semantic_check_required
    forbidden_pattern: unsafe assumption or unsupported source
    failure_mode: incorrect metric/reconciliation due to wrong scope, amount semantics, grain, or source reliability
    auto_fix_hint: use referenced table/column/value/profile/relationship cards and inject runtime scope
    validator_type: semantic_check
    evidence_refs:
    - evidence.logistics_kb_doc
    - evidence.cognee_design_v4
    - evidence.unified_edge_scope
```

```yaml
candidate_card:
  card_type: rule
  card_id: rule.logistics.qr_cod_separate_from_cash
  name: Qr Cod Separate From Cash
  fields:
    name: Qr Cod Separate From Cash
    description: 'Mandatory logistics rule: qr_cod_separate_from_cash.'
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
    rule_name: qr_cod_separate_from_cash
    rule_type: scope_filter/date_safety/join_safety/metric_semantics/aggregation_safety
    severity: high
    applies_to:
    - logistics query patterns
    - metric implementations
    - reconciliation profiles
    rule_statement: qr cod separate from cash
    required_pattern: semantic_check_required
    forbidden_pattern: unsafe assumption or unsupported source
    failure_mode: incorrect metric/reconciliation due to wrong scope, amount semantics, grain, or source reliability
    auto_fix_hint: use referenced table/column/value/profile/relationship cards and inject runtime scope
    validator_type: semantic_check
    evidence_refs:
    - evidence.logistics_kb_doc
    - evidence.cognee_design_v4
    - evidence.unified_edge_scope
```

```yaml
candidate_card:
  card_type: rule
  card_id: rule.logistics.avoid_null_value_inference
  name: Avoid Null Value Inference
  fields:
    name: Avoid Null Value Inference
    description: 'Mandatory logistics rule: avoid_null_value_inference.'
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
    rule_name: avoid_null_value_inference
    rule_type: scope_filter/date_safety/join_safety/metric_semantics/aggregation_safety
    severity: high
    applies_to:
    - logistics query patterns
    - metric implementations
    - reconciliation profiles
    rule_statement: avoid null value inference
    required_pattern: semantic_check_required
    forbidden_pattern: unsafe assumption or unsupported source
    failure_mode: incorrect metric/reconciliation due to wrong scope, amount semantics, grain, or source reliability
    auto_fix_hint: use referenced table/column/value/profile/relationship cards and inject runtime scope
    validator_type: semantic_check
    evidence_refs:
    - evidence.logistics_kb_doc
    - evidence.cognee_design_v4
    - evidence.unified_edge_scope
```

```yaml
candidate_card:
  card_type: rule
  card_id: rule.logistics.integer_scope_filters_not_strings
  name: Integer Scope Filters Not Strings
  fields:
    name: Integer Scope Filters Not Strings
    description: 'Mandatory logistics rule: integer_scope_filters_not_strings.'
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
    rule_name: integer_scope_filters_not_strings
    rule_type: scope_filter/date_safety/join_safety/metric_semantics/aggregation_safety
    severity: high
    applies_to:
    - logistics query patterns
    - metric implementations
    - reconciliation profiles
    rule_statement: integer scope filters not strings
    required_pattern: semantic_check_required
    forbidden_pattern: unsafe assumption or unsupported source
    failure_mode: incorrect metric/reconciliation due to wrong scope, amount semantics, grain, or source reliability
    auto_fix_hint: use referenced table/column/value/profile/relationship cards and inject runtime scope
    validator_type: semantic_check
    evidence_refs:
    - evidence.logistics_kb_doc
    - evidence.cognee_design_v4
    - evidence.unified_edge_scope
```

```yaml
candidate_card:
  card_type: rule
  card_id: rule.logistics.account_filters_from_adb_only
  name: Account Filters From Adb Only
  fields:
    name: Account Filters From Adb Only
    description: 'Mandatory logistics rule: account_filters_from_adb_only.'
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
    rule_name: account_filters_from_adb_only
    rule_type: scope_filter/date_safety/join_safety/metric_semantics/aggregation_safety
    severity: high
    applies_to:
    - logistics query patterns
    - metric implementations
    - reconciliation profiles
    rule_statement: account filters from adb only
    required_pattern: semantic_check_required
    forbidden_pattern: unsafe assumption or unsupported source
    failure_mode: incorrect metric/reconciliation due to wrong scope, amount semantics, grain, or source reliability
    auto_fix_hint: use referenced table/column/value/profile/relationship cards and inject runtime scope
    validator_type: semantic_check
    evidence_refs:
    - evidence.logistics_kb_doc
    - evidence.cognee_design_v4
    - evidence.unified_edge_scope
```

```yaml
candidate_card:
  card_type: rule
  card_id: rule.logistics.document_unsupported_reason_when_metric_missing
  name: Document Unsupported Reason When Metric Missing
  fields:
    name: Document Unsupported Reason When Metric Missing
    description: 'Mandatory logistics rule: document_unsupported_reason_when_metric_missing.'
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
    rule_name: document_unsupported_reason_when_metric_missing
    rule_type: scope_filter/date_safety/join_safety/metric_semantics/aggregation_safety
    severity: high
    applies_to:
    - logistics query patterns
    - metric implementations
    - reconciliation profiles
    rule_statement: document unsupported reason when metric missing
    required_pattern: semantic_check_required
    forbidden_pattern: unsafe assumption or unsupported source
    failure_mode: incorrect metric/reconciliation due to wrong scope, amount semantics, grain, or source reliability
    auto_fix_hint: use referenced table/column/value/profile/relationship cards and inject runtime scope
    validator_type: semantic_check
    evidence_refs:
    - evidence.logistics_kb_doc
    - evidence.cognee_design_v4
    - evidence.unified_edge_scope
```

### 4.24 validation_test cards

```yaml
candidate_card:
  card_type: validation_test
  card_id: validation_test.logistics.required_scope_context
  name: Required Scope Context Validation
  fields:
    name: Required Scope Context Validation
    description: Validation test enforcing rule required_scope_context.
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
    test_name: required_scope_context_validation
    test_type: semantic_check
    linked_rule_id: rule.logistics.required_scope_context
    applies_to:
    - generated_sql
    - retrieval_bundle
    - card_extraction
    required_pattern: rule condition satisfied
    forbidden_pattern: rule violation
    semantic_condition: required scope context
    severity: critical
    failure_message: 'Logistics validation failed: required_scope_context'
    auto_fix_hint: repair using relevant canonical cards
    blocking: true
    evidence_refs:
    - evidence.logistics_kb_doc
    - evidence.cognee_design_v4
    - evidence.unified_edge_scope
```

```yaml
candidate_card:
  card_type: validation_test
  card_id: validation_test.logistics.business_flow_binding_required_for_cross_platform
  name: Business Flow Binding Required For Cross Platform Validation
  fields:
    name: Business Flow Binding Required For Cross Platform Validation
    description: Validation test enforcing rule business_flow_binding_required_for_cross_platform.
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
    test_name: business_flow_binding_required_for_cross_platform_validation
    test_type: semantic_check
    linked_rule_id: rule.logistics.business_flow_binding_required_for_cross_platform
    applies_to:
    - generated_sql
    - retrieval_bundle
    - card_extraction
    required_pattern: rule condition satisfied
    forbidden_pattern: rule violation
    semantic_condition: business flow binding required for cross platform
    severity: high
    failure_message: 'Logistics validation failed: business_flow_binding_required_for_cross_platform'
    auto_fix_hint: repair using relevant canonical cards
    blocking: false
    evidence_refs:
    - evidence.logistics_kb_doc
    - evidence.cognee_design_v4
    - evidence.unified_edge_scope
```

```yaml
candidate_card:
  card_type: validation_test
  card_id: validation_test.logistics.do_not_create_bfb_from_generic_vendor_doc
  name: Do Not Create Bfb From Generic Vendor Doc Validation
  fields:
    name: Do Not Create Bfb From Generic Vendor Doc Validation
    description: Validation test enforcing rule do_not_create_bfb_from_generic_vendor_doc.
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
    test_name: do_not_create_bfb_from_generic_vendor_doc_validation
    test_type: semantic_check
    linked_rule_id: rule.logistics.do_not_create_bfb_from_generic_vendor_doc
    applies_to:
    - generated_sql
    - retrieval_bundle
    - card_extraction
    required_pattern: rule condition satisfied
    forbidden_pattern: rule violation
    semantic_condition: do not create bfb from generic vendor doc
    severity: high
    failure_message: 'Logistics validation failed: do_not_create_bfb_from_generic_vendor_doc'
    auto_fix_hint: repair using relevant canonical cards
    blocking: false
    evidence_refs:
    - evidence.logistics_kb_doc
    - evidence.cognee_design_v4
    - evidence.unified_edge_scope
```

```yaml
candidate_card:
  card_type: validation_test
  card_id: validation_test.logistics.amount_semantics_not_by_name
  name: Amount Semantics Not By Name Validation
  fields:
    name: Amount Semantics Not By Name Validation
    description: Validation test enforcing rule amount_semantics_not_by_name.
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
    test_name: amount_semantics_not_by_name_validation
    test_type: semantic_check
    linked_rule_id: rule.logistics.amount_semantics_not_by_name
    applies_to:
    - generated_sql
    - retrieval_bundle
    - card_extraction
    required_pattern: rule condition satisfied
    forbidden_pattern: rule violation
    semantic_condition: amount semantics not by name
    severity: critical
    failure_message: 'Logistics validation failed: amount_semantics_not_by_name'
    auto_fix_hint: repair using relevant canonical cards
    blocking: true
    evidence_refs:
    - evidence.logistics_kb_doc
    - evidence.cognee_design_v4
    - evidence.unified_edge_scope
```

```yaml
candidate_card:
  card_type: validation_test
  card_id: validation_test.logistics.charged_amount_table_specific
  name: Charged Amount Table Specific Validation
  fields:
    name: Charged Amount Table Specific Validation
    description: Validation test enforcing rule charged_amount_table_specific.
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
    test_name: charged_amount_table_specific_validation
    test_type: semantic_check
    linked_rule_id: rule.logistics.charged_amount_table_specific
    applies_to:
    - generated_sql
    - retrieval_bundle
    - card_extraction
    required_pattern: rule condition satisfied
    forbidden_pattern: rule violation
    semantic_condition: charged amount table specific
    severity: high
    failure_message: 'Logistics validation failed: charged_amount_table_specific'
    auto_fix_hint: repair using relevant canonical cards
    blocking: false
    evidence_refs:
    - evidence.logistics_kb_doc
    - evidence.cognee_design_v4
    - evidence.unified_edge_scope
```

```yaml
candidate_card:
  card_type: validation_test
  card_id: validation_test.logistics.active_filter_when_available
  name: Active Filter When Available Validation
  fields:
    name: Active Filter When Available Validation
    description: Validation test enforcing rule active_filter_when_available.
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
    test_name: active_filter_when_available_validation
    test_type: semantic_check
    linked_rule_id: rule.logistics.active_filter_when_available
    applies_to:
    - generated_sql
    - retrieval_bundle
    - card_extraction
    required_pattern: rule condition satisfied
    forbidden_pattern: rule violation
    semantic_condition: active filter when available
    severity: high
    failure_message: 'Logistics validation failed: active_filter_when_available'
    auto_fix_hint: repair using relevant canonical cards
    blocking: false
    evidence_refs:
    - evidence.logistics_kb_doc
    - evidence.cognee_design_v4
    - evidence.unified_edge_scope
```

```yaml
candidate_card:
  card_type: validation_test
  card_id: validation_test.logistics.empty_tables_schema_only
  name: Empty Tables Schema Only Validation
  fields:
    name: Empty Tables Schema Only Validation
    description: Validation test enforcing rule empty_tables_schema_only.
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
    test_name: empty_tables_schema_only_validation
    test_type: semantic_check
    linked_rule_id: rule.logistics.empty_tables_schema_only
    applies_to:
    - generated_sql
    - retrieval_bundle
    - card_extraction
    required_pattern: rule condition satisfied
    forbidden_pattern: rule violation
    semantic_condition: empty tables schema only
    severity: critical
    failure_message: 'Logistics validation failed: empty_tables_schema_only'
    auto_fix_hint: repair using relevant canonical cards
    blocking: true
    evidence_refs:
    - evidence.logistics_kb_doc
    - evidence.cognee_design_v4
    - evidence.unified_edge_scope
```

```yaml
candidate_card:
  card_type: validation_test
  card_id: validation_test.logistics.low_confidence_requires_warning
  name: Low Confidence Requires Warning Validation
  fields:
    name: Low Confidence Requires Warning Validation
    description: Validation test enforcing rule low_confidence_requires_warning.
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
    test_name: low_confidence_requires_warning_validation
    test_type: semantic_check
    linked_rule_id: rule.logistics.low_confidence_requires_warning
    applies_to:
    - generated_sql
    - retrieval_bundle
    - card_extraction
    required_pattern: rule condition satisfied
    forbidden_pattern: rule violation
    semantic_condition: low confidence requires warning
    severity: high
    failure_message: 'Logistics validation failed: low_confidence_requires_warning'
    auto_fix_hint: repair using relevant canonical cards
    blocking: false
    evidence_refs:
    - evidence.logistics_kb_doc
    - evidence.cognee_design_v4
    - evidence.unified_edge_scope
```

```yaml
candidate_card:
  card_type: validation_test
  card_id: validation_test.logistics.fallback_sources_explicit_only
  name: Fallback Sources Explicit Only Validation
  fields:
    name: Fallback Sources Explicit Only Validation
    description: Validation test enforcing rule fallback_sources_explicit_only.
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
    test_name: fallback_sources_explicit_only_validation
    test_type: semantic_check
    linked_rule_id: rule.logistics.fallback_sources_explicit_only
    applies_to:
    - generated_sql
    - retrieval_bundle
    - card_extraction
    required_pattern: rule condition satisfied
    forbidden_pattern: rule violation
    semantic_condition: fallback sources explicit only
    severity: high
    failure_message: 'Logistics validation failed: fallback_sources_explicit_only'
    auto_fix_hint: repair using relevant canonical cards
    blocking: false
    evidence_refs:
    - evidence.logistics_kb_doc
    - evidence.cognee_design_v4
    - evidence.unified_edge_scope
```

```yaml
candidate_card:
  card_type: validation_test
  card_id: validation_test.logistics.awb_primary_reconciliation_unit
  name: Awb Primary Reconciliation Unit Validation
  fields:
    name: Awb Primary Reconciliation Unit Validation
    description: Validation test enforcing rule awb_primary_reconciliation_unit.
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
    test_name: awb_primary_reconciliation_unit_validation
    test_type: semantic_check
    linked_rule_id: rule.logistics.awb_primary_reconciliation_unit
    applies_to:
    - generated_sql
    - retrieval_bundle
    - card_extraction
    required_pattern: rule condition satisfied
    forbidden_pattern: rule violation
    semantic_condition: awb primary reconciliation unit
    severity: high
    failure_message: 'Logistics validation failed: awb_primary_reconciliation_unit'
    auto_fix_hint: repair using relevant canonical cards
    blocking: false
    evidence_refs:
    - evidence.logistics_kb_doc
    - evidence.cognee_design_v4
    - evidence.unified_edge_scope
```

```yaml
candidate_card:
  card_type: validation_test
  card_id: validation_test.logistics.do_not_join_awb_to_bank_without_batch
  name: Do Not Join Awb To Bank Without Batch Validation
  fields:
    name: Do Not Join Awb To Bank Without Batch Validation
    description: Validation test enforcing rule do_not_join_awb_to_bank_without_batch.
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
    test_name: do_not_join_awb_to_bank_without_batch_validation
    test_type: semantic_check
    linked_rule_id: rule.logistics.do_not_join_awb_to_bank_without_batch
    applies_to:
    - generated_sql
    - retrieval_bundle
    - card_extraction
    required_pattern: rule condition satisfied
    forbidden_pattern: rule violation
    semantic_condition: do not join awb to bank without batch
    severity: critical
    failure_message: 'Logistics validation failed: do_not_join_awb_to_bank_without_batch'
    auto_fix_hint: repair using relevant canonical cards
    blocking: true
    evidence_refs:
    - evidence.logistics_kb_doc
    - evidence.cognee_design_v4
    - evidence.unified_edge_scope
```

```yaml
candidate_card:
  card_type: validation_test
  card_id: validation_test.logistics.preaggregate_before_order_join
  name: Preaggregate Before Order Join Validation
  fields:
    name: Preaggregate Before Order Join Validation
    description: Validation test enforcing rule preaggregate_before_order_join.
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
    test_name: preaggregate_before_order_join_validation
    test_type: semantic_check
    linked_rule_id: rule.logistics.preaggregate_before_order_join
    applies_to:
    - generated_sql
    - retrieval_bundle
    - card_extraction
    required_pattern: rule condition satisfied
    forbidden_pattern: rule violation
    semantic_condition: preaggregate before order join
    severity: high
    failure_message: 'Logistics validation failed: preaggregate_before_order_join'
    auto_fix_hint: repair using relevant canonical cards
    blocking: false
    evidence_refs:
    - evidence.logistics_kb_doc
    - evidence.cognee_design_v4
    - evidence.unified_edge_scope
```

```yaml
candidate_card:
  card_type: validation_test
  card_id: validation_test.logistics.preaggregate_fee_rows_before_join
  name: Preaggregate Fee Rows Before Join Validation
  fields:
    name: Preaggregate Fee Rows Before Join Validation
    description: Validation test enforcing rule preaggregate_fee_rows_before_join.
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
    test_name: preaggregate_fee_rows_before_join_validation
    test_type: semantic_check
    linked_rule_id: rule.logistics.preaggregate_fee_rows_before_join
    applies_to:
    - generated_sql
    - retrieval_bundle
    - card_extraction
    required_pattern: rule condition satisfied
    forbidden_pattern: rule violation
    semantic_condition: preaggregate fee rows before join
    severity: high
    failure_message: 'Logistics validation failed: preaggregate_fee_rows_before_join'
    auto_fix_hint: repair using relevant canonical cards
    blocking: false
    evidence_refs:
    - evidence.logistics_kb_doc
    - evidence.cognee_design_v4
    - evidence.unified_edge_scope
```

```yaml
candidate_card:
  card_type: validation_test
  card_id: validation_test.logistics.parse_shiprocket_order_id_before_shopify_join
  name: Parse Shiprocket Order Id Before Shopify Join Validation
  fields:
    name: Parse Shiprocket Order Id Before Shopify Join Validation
    description: Validation test enforcing rule parse_shiprocket_order_id_before_shopify_join.
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
    test_name: parse_shiprocket_order_id_before_shopify_join_validation
    test_type: semantic_check
    linked_rule_id: rule.logistics.parse_shiprocket_order_id_before_shopify_join
    applies_to:
    - generated_sql
    - retrieval_bundle
    - card_extraction
    required_pattern: rule condition satisfied
    forbidden_pattern: rule violation
    semantic_condition: parse shiprocket order id before shopify join
    severity: high
    failure_message: 'Logistics validation failed: parse_shiprocket_order_id_before_shopify_join'
    auto_fix_hint: repair using relevant canonical cards
    blocking: false
    evidence_refs:
    - evidence.logistics_kb_doc
    - evidence.cognee_design_v4
    - evidence.unified_edge_scope
```

```yaml
candidate_card:
  card_type: validation_test
  card_id: validation_test.logistics.xpressbees_native_low_confidence
  name: Xpressbees Native Low Confidence Validation
  fields:
    name: Xpressbees Native Low Confidence Validation
    description: Validation test enforcing rule xpressbees_native_low_confidence.
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
    test_name: xpressbees_native_low_confidence_validation
    test_type: semantic_check
    linked_rule_id: rule.logistics.xpressbees_native_low_confidence
    applies_to:
    - generated_sql
    - retrieval_bundle
    - card_extraction
    required_pattern: rule condition satisfied
    forbidden_pattern: rule violation
    semantic_condition: xpressbees native low confidence
    severity: high
    failure_message: 'Logistics validation failed: xpressbees_native_low_confidence'
    auto_fix_hint: repair using relevant canonical cards
    blocking: false
    evidence_refs:
    - evidence.logistics_kb_doc
    - evidence.cognee_design_v4
    - evidence.unified_edge_scope
```

```yaml
candidate_card:
  card_type: validation_test
  card_id: validation_test.logistics.xpressbees_fallback_shiprocket_preferred
  name: Xpressbees Fallback Shiprocket Preferred Validation
  fields:
    name: Xpressbees Fallback Shiprocket Preferred Validation
    description: Validation test enforcing rule xpressbees_fallback_shiprocket_preferred.
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
    test_name: xpressbees_fallback_shiprocket_preferred_validation
    test_type: semantic_check
    linked_rule_id: rule.logistics.xpressbees_fallback_shiprocket_preferred
    applies_to:
    - generated_sql
    - retrieval_bundle
    - card_extraction
    required_pattern: rule condition satisfied
    forbidden_pattern: rule violation
    semantic_condition: xpressbees fallback shiprocket preferred
    severity: high
    failure_message: 'Logistics validation failed: xpressbees_fallback_shiprocket_preferred'
    auto_fix_hint: repair using relevant canonical cards
    blocking: false
    evidence_refs:
    - evidence.logistics_kb_doc
    - evidence.cognee_design_v4
    - evidence.unified_edge_scope
```

```yaml
candidate_card:
  card_type: validation_test
  card_id: validation_test.logistics.shadowfax_no_native_settlement
  name: Shadowfax No Native Settlement Validation
  fields:
    name: Shadowfax No Native Settlement Validation
    description: Validation test enforcing rule shadowfax_no_native_settlement.
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
    test_name: shadowfax_no_native_settlement_validation
    test_type: semantic_check
    linked_rule_id: rule.logistics.shadowfax_no_native_settlement
    applies_to:
    - generated_sql
    - retrieval_bundle
    - card_extraction
    required_pattern: rule condition satisfied
    forbidden_pattern: rule violation
    semantic_condition: shadowfax no native settlement
    severity: high
    failure_message: 'Logistics validation failed: shadowfax_no_native_settlement'
    auto_fix_hint: repair using relevant canonical cards
    blocking: false
    evidence_refs:
    - evidence.logistics_kb_doc
    - evidence.cognee_design_v4
    - evidence.unified_edge_scope
```

```yaml
candidate_card:
  card_type: validation_test
  card_id: validation_test.logistics.ecom_no_native_table
  name: Ecom No Native Table Validation
  fields:
    name: Ecom No Native Table Validation
    description: Validation test enforcing rule ecom_no_native_table.
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
    test_name: ecom_no_native_table_validation
    test_type: semantic_check
    linked_rule_id: rule.logistics.ecom_no_native_table
    applies_to:
    - generated_sql
    - retrieval_bundle
    - card_extraction
    required_pattern: rule condition satisfied
    forbidden_pattern: rule violation
    semantic_condition: ecom no native table
    severity: high
    failure_message: 'Logistics validation failed: ecom_no_native_table'
    auto_fix_hint: repair using relevant canonical cards
    blocking: false
    evidence_refs:
    - evidence.logistics_kb_doc
    - evidence.cognee_design_v4
    - evidence.unified_edge_scope
```

```yaml
candidate_card:
  card_type: validation_test
  card_id: validation_test.logistics.dtdc_invoice_empty
  name: Dtdc Invoice Empty Validation
  fields:
    name: Dtdc Invoice Empty Validation
    description: Validation test enforcing rule dtdc_invoice_empty.
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
    test_name: dtdc_invoice_empty_validation
    test_type: semantic_check
    linked_rule_id: rule.logistics.dtdc_invoice_empty
    applies_to:
    - generated_sql
    - retrieval_bundle
    - card_extraction
    required_pattern: rule condition satisfied
    forbidden_pattern: rule violation
    semantic_condition: dtdc invoice empty
    severity: high
    failure_message: 'Logistics validation failed: dtdc_invoice_empty'
    auto_fix_hint: repair using relevant canonical cards
    blocking: false
    evidence_refs:
    - evidence.logistics_kb_doc
    - evidence.cognee_design_v4
    - evidence.unified_edge_scope
```

```yaml
candidate_card:
  card_type: validation_test
  card_id: validation_test.logistics.ekart_invoice_empty
  name: Ekart Invoice Empty Validation
  fields:
    name: Ekart Invoice Empty Validation
    description: Validation test enforcing rule ekart_invoice_empty.
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
    test_name: ekart_invoice_empty_validation
    test_type: semantic_check
    linked_rule_id: rule.logistics.ekart_invoice_empty
    applies_to:
    - generated_sql
    - retrieval_bundle
    - card_extraction
    required_pattern: rule condition satisfied
    forbidden_pattern: rule violation
    semantic_condition: ekart invoice empty
    severity: high
    failure_message: 'Logistics validation failed: ekart_invoice_empty'
    auto_fix_hint: repair using relevant canonical cards
    blocking: false
    evidence_refs:
    - evidence.logistics_kb_doc
    - evidence.cognee_design_v4
    - evidence.unified_edge_scope
```

```yaml
candidate_card:
  card_type: validation_test
  card_id: validation_test.logistics.shiprocket_settlement_report_empty
  name: Shiprocket Settlement Report Empty Validation
  fields:
    name: Shiprocket Settlement Report Empty Validation
    description: Validation test enforcing rule shiprocket_settlement_report_empty.
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
    test_name: shiprocket_settlement_report_empty_validation
    test_type: semantic_check
    linked_rule_id: rule.logistics.shiprocket_settlement_report_empty
    applies_to:
    - generated_sql
    - retrieval_bundle
    - card_extraction
    required_pattern: rule condition satisfied
    forbidden_pattern: rule violation
    semantic_condition: shiprocket settlement report empty
    severity: high
    failure_message: 'Logistics validation failed: shiprocket_settlement_report_empty'
    auto_fix_hint: repair using relevant canonical cards
    blocking: false
    evidence_refs:
    - evidence.logistics_kb_doc
    - evidence.cognee_design_v4
    - evidence.unified_edge_scope
```

```yaml
candidate_card:
  card_type: validation_test
  card_id: validation_test.logistics.cod_fee_only_for_cod
  name: Cod Fee Only For Cod Validation
  fields:
    name: Cod Fee Only For Cod Validation
    description: Validation test enforcing rule cod_fee_only_for_cod.
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
    test_name: cod_fee_only_for_cod_validation
    test_type: semantic_check
    linked_rule_id: rule.logistics.cod_fee_only_for_cod
    applies_to:
    - generated_sql
    - retrieval_bundle
    - card_extraction
    required_pattern: rule condition satisfied
    forbidden_pattern: rule violation
    semantic_condition: cod fee only for cod
    severity: high
    failure_message: 'Logistics validation failed: cod_fee_only_for_cod'
    auto_fix_hint: repair using relevant canonical cards
    blocking: false
    evidence_refs:
    - evidence.logistics_kb_doc
    - evidence.cognee_design_v4
    - evidence.unified_edge_scope
```

```yaml
candidate_card:
  card_type: validation_test
  card_id: validation_test.logistics.rto_charge_only_for_rto
  name: Rto Charge Only For Rto Validation
  fields:
    name: Rto Charge Only For Rto Validation
    description: Validation test enforcing rule rto_charge_only_for_rto.
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
    test_name: rto_charge_only_for_rto_validation
    test_type: semantic_check
    linked_rule_id: rule.logistics.rto_charge_only_for_rto
    applies_to:
    - generated_sql
    - retrieval_bundle
    - card_extraction
    required_pattern: rule condition satisfied
    forbidden_pattern: rule violation
    semantic_condition: rto charge only for rto
    severity: high
    failure_message: 'Logistics validation failed: rto_charge_only_for_rto'
    auto_fix_hint: repair using relevant canonical cards
    blocking: false
    evidence_refs:
    - evidence.logistics_kb_doc
    - evidence.cognee_design_v4
    - evidence.unified_edge_scope
```

```yaml
candidate_card:
  card_type: validation_test
  card_id: validation_test.logistics.zone_value_profile_required
  name: Zone Value Profile Required Validation
  fields:
    name: Zone Value Profile Required Validation
    description: Validation test enforcing rule zone_value_profile_required.
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
    test_name: zone_value_profile_required_validation
    test_type: semantic_check
    linked_rule_id: rule.logistics.zone_value_profile_required
    applies_to:
    - generated_sql
    - retrieval_bundle
    - card_extraction
    required_pattern: rule condition satisfied
    forbidden_pattern: rule violation
    semantic_condition: zone value profile required
    severity: high
    failure_message: 'Logistics validation failed: zone_value_profile_required'
    auto_fix_hint: repair using relevant canonical cards
    blocking: false
    evidence_refs:
    - evidence.logistics_kb_doc
    - evidence.cognee_design_v4
    - evidence.unified_edge_scope
```

```yaml
candidate_card:
  card_type: validation_test
  card_id: validation_test.logistics.payment_mode_value_profile_required
  name: Payment Mode Value Profile Required Validation
  fields:
    name: Payment Mode Value Profile Required Validation
    description: Validation test enforcing rule payment_mode_value_profile_required.
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
    test_name: payment_mode_value_profile_required_validation
    test_type: semantic_check
    linked_rule_id: rule.logistics.payment_mode_value_profile_required
    applies_to:
    - generated_sql
    - retrieval_bundle
    - card_extraction
    required_pattern: rule condition satisfied
    forbidden_pattern: rule violation
    semantic_condition: payment mode value profile required
    severity: high
    failure_message: 'Logistics validation failed: payment_mode_value_profile_required'
    auto_fix_hint: repair using relevant canonical cards
    blocking: false
    evidence_refs:
    - evidence.logistics_kb_doc
    - evidence.cognee_design_v4
    - evidence.unified_edge_scope
```

```yaml
candidate_card:
  card_type: validation_test
  card_id: validation_test.logistics.courier_partner_filter_exact_or_profiled
  name: Courier Partner Filter Exact Or Profiled Validation
  fields:
    name: Courier Partner Filter Exact Or Profiled Validation
    description: Validation test enforcing rule courier_partner_filter_exact_or_profiled.
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
    test_name: courier_partner_filter_exact_or_profiled_validation
    test_type: semantic_check
    linked_rule_id: rule.logistics.courier_partner_filter_exact_or_profiled
    applies_to:
    - generated_sql
    - retrieval_bundle
    - card_extraction
    required_pattern: rule condition satisfied
    forbidden_pattern: rule violation
    semantic_condition: courier partner filter exact or profiled
    severity: high
    failure_message: 'Logistics validation failed: courier_partner_filter_exact_or_profiled'
    auto_fix_hint: repair using relevant canonical cards
    blocking: false
    evidence_refs:
    - evidence.logistics_kb_doc
    - evidence.cognee_design_v4
    - evidence.unified_edge_scope
```

```yaml
candidate_card:
  card_type: validation_test
  card_id: validation_test.logistics.date_column_must_match_metric
  name: Date Column Must Match Metric Validation
  fields:
    name: Date Column Must Match Metric Validation
    description: Validation test enforcing rule date_column_must_match_metric.
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
    test_name: date_column_must_match_metric_validation
    test_type: semantic_check
    linked_rule_id: rule.logistics.date_column_must_match_metric
    applies_to:
    - generated_sql
    - retrieval_bundle
    - card_extraction
    required_pattern: rule condition satisfied
    forbidden_pattern: rule violation
    semantic_condition: date column must match metric
    severity: high
    failure_message: 'Logistics validation failed: date_column_must_match_metric'
    auto_fix_hint: repair using relevant canonical cards
    blocking: false
    evidence_refs:
    - evidence.logistics_kb_doc
    - evidence.cognee_design_v4
    - evidence.unified_edge_scope
```

```yaml
candidate_card:
  card_type: validation_test
  card_id: validation_test.logistics.settlement_date_for_cod_remittance
  name: Settlement Date For Cod Remittance Validation
  fields:
    name: Settlement Date For Cod Remittance Validation
    description: Validation test enforcing rule settlement_date_for_cod_remittance.
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
    test_name: settlement_date_for_cod_remittance_validation
    test_type: semantic_check
    linked_rule_id: rule.logistics.settlement_date_for_cod_remittance
    applies_to:
    - generated_sql
    - retrieval_bundle
    - card_extraction
    required_pattern: rule condition satisfied
    forbidden_pattern: rule violation
    semantic_condition: settlement date for cod remittance
    severity: high
    failure_message: 'Logistics validation failed: settlement_date_for_cod_remittance'
    auto_fix_hint: repair using relevant canonical cards
    blocking: false
    evidence_refs:
    - evidence.logistics_kb_doc
    - evidence.cognee_design_v4
    - evidence.unified_edge_scope
```

```yaml
candidate_card:
  card_type: validation_test
  card_id: validation_test.logistics.delivered_date_for_delivery_metrics
  name: Delivered Date For Delivery Metrics Validation
  fields:
    name: Delivered Date For Delivery Metrics Validation
    description: Validation test enforcing rule delivered_date_for_delivery_metrics.
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
    test_name: delivered_date_for_delivery_metrics_validation
    test_type: semantic_check
    linked_rule_id: rule.logistics.delivered_date_for_delivery_metrics
    applies_to:
    - generated_sql
    - retrieval_bundle
    - card_extraction
    required_pattern: rule condition satisfied
    forbidden_pattern: rule violation
    semantic_condition: delivered date for delivery metrics
    severity: high
    failure_message: 'Logistics validation failed: delivered_date_for_delivery_metrics'
    auto_fix_hint: repair using relevant canonical cards
    blocking: false
    evidence_refs:
    - evidence.logistics_kb_doc
    - evidence.cognee_design_v4
    - evidence.unified_edge_scope
```

```yaml
candidate_card:
  card_type: validation_test
  card_id: validation_test.logistics.bank_reference_required_for_bank_match
  name: Bank Reference Required For Bank Match Validation
  fields:
    name: Bank Reference Required For Bank Match Validation
    description: Validation test enforcing rule bank_reference_required_for_bank_match.
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
    test_name: bank_reference_required_for_bank_match_validation
    test_type: semantic_check
    linked_rule_id: rule.logistics.bank_reference_required_for_bank_match
    applies_to:
    - generated_sql
    - retrieval_bundle
    - card_extraction
    required_pattern: rule condition satisfied
    forbidden_pattern: rule violation
    semantic_condition: bank reference required for bank match
    severity: high
    failure_message: 'Logistics validation failed: bank_reference_required_for_bank_match'
    auto_fix_hint: repair using relevant canonical cards
    blocking: false
    evidence_refs:
    - evidence.logistics_kb_doc
    - evidence.cognee_design_v4
    - evidence.unified_edge_scope
```

```yaml
candidate_card:
  card_type: validation_test
  card_id: validation_test.logistics.utr_preferred_for_bank_bridge
  name: Utr Preferred For Bank Bridge Validation
  fields:
    name: Utr Preferred For Bank Bridge Validation
    description: Validation test enforcing rule utr_preferred_for_bank_bridge.
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
    test_name: utr_preferred_for_bank_bridge_validation
    test_type: semantic_check
    linked_rule_id: rule.logistics.utr_preferred_for_bank_bridge
    applies_to:
    - generated_sql
    - retrieval_bundle
    - card_extraction
    required_pattern: rule condition satisfied
    forbidden_pattern: rule violation
    semantic_condition: utr preferred for bank bridge
    severity: high
    failure_message: 'Logistics validation failed: utr_preferred_for_bank_bridge'
    auto_fix_hint: repair using relevant canonical cards
    blocking: false
    evidence_refs:
    - evidence.logistics_kb_doc
    - evidence.cognee_design_v4
    - evidence.unified_edge_scope
```

```yaml
candidate_card:
  card_type: validation_test
  card_id: validation_test.logistics.batch_amount_deduplicate
  name: Batch Amount Deduplicate Validation
  fields:
    name: Batch Amount Deduplicate Validation
    description: Validation test enforcing rule batch_amount_deduplicate.
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
    test_name: batch_amount_deduplicate_validation
    test_type: semantic_check
    linked_rule_id: rule.logistics.batch_amount_deduplicate
    applies_to:
    - generated_sql
    - retrieval_bundle
    - card_extraction
    required_pattern: rule condition satisfied
    forbidden_pattern: rule violation
    semantic_condition: batch amount deduplicate
    severity: high
    failure_message: 'Logistics validation failed: batch_amount_deduplicate'
    auto_fix_hint: repair using relevant canonical cards
    blocking: false
    evidence_refs:
    - evidence.logistics_kb_doc
    - evidence.cognee_design_v4
    - evidence.unified_edge_scope
```

```yaml
candidate_card:
  card_type: validation_test
  card_id: validation_test.logistics.total_amount_of_batch_not_awb_level
  name: Total Amount Of Batch Not Awb Level Validation
  fields:
    name: Total Amount Of Batch Not Awb Level Validation
    description: Validation test enforcing rule total_amount_of_batch_not_awb_level.
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
    test_name: total_amount_of_batch_not_awb_level_validation
    test_type: semantic_check
    linked_rule_id: rule.logistics.total_amount_of_batch_not_awb_level
    applies_to:
    - generated_sql
    - retrieval_bundle
    - card_extraction
    required_pattern: rule condition satisfied
    forbidden_pattern: rule violation
    semantic_condition: total amount of batch not awb level
    severity: high
    failure_message: 'Logistics validation failed: total_amount_of_batch_not_awb_level'
    auto_fix_hint: repair using relevant canonical cards
    blocking: false
    evidence_refs:
    - evidence.logistics_kb_doc
    - evidence.cognee_design_v4
    - evidence.unified_edge_scope
```

```yaml
candidate_card:
  card_type: validation_test
  card_id: validation_test.logistics.delhivery_charged_amount_declared_value
  name: Delhivery Charged Amount Declared Value Validation
  fields:
    name: Delhivery Charged Amount Declared Value Validation
    description: Validation test enforcing rule delhivery_charged_amount_declared_value.
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
    test_name: delhivery_charged_amount_declared_value_validation
    test_type: semantic_check
    linked_rule_id: rule.logistics.delhivery_charged_amount_declared_value
    applies_to:
    - generated_sql
    - retrieval_bundle
    - card_extraction
    required_pattern: rule condition satisfied
    forbidden_pattern: rule violation
    semantic_condition: delhivery charged amount declared value
    severity: high
    failure_message: 'Logistics validation failed: delhivery_charged_amount_declared_value'
    auto_fix_hint: repair using relevant canonical cards
    blocking: false
    evidence_refs:
    - evidence.logistics_kb_doc
    - evidence.cognee_design_v4
    - evidence.unified_edge_scope
```

```yaml
candidate_card:
  card_type: validation_test
  card_id: validation_test.logistics.shiprocket_oms_charged_amount_declared_value
  name: Shiprocket Oms Charged Amount Declared Value Validation
  fields:
    name: Shiprocket Oms Charged Amount Declared Value Validation
    description: Validation test enforcing rule shiprocket_oms_charged_amount_declared_value.
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
    test_name: shiprocket_oms_charged_amount_declared_value_validation
    test_type: semantic_check
    linked_rule_id: rule.logistics.shiprocket_oms_charged_amount_declared_value
    applies_to:
    - generated_sql
    - retrieval_bundle
    - card_extraction
    required_pattern: rule condition satisfied
    forbidden_pattern: rule violation
    semantic_condition: shiprocket oms charged amount declared value
    severity: high
    failure_message: 'Logistics validation failed: shiprocket_oms_charged_amount_declared_value'
    auto_fix_hint: repair using relevant canonical cards
    blocking: false
    evidence_refs:
    - evidence.logistics_kb_doc
    - evidence.cognee_design_v4
    - evidence.unified_edge_scope
```

```yaml
candidate_card:
  card_type: validation_test
  card_id: validation_test.logistics.shiprocket_invoice_charged_amount_freight
  name: Shiprocket Invoice Charged Amount Freight Validation
  fields:
    name: Shiprocket Invoice Charged Amount Freight Validation
    description: Validation test enforcing rule shiprocket_invoice_charged_amount_freight.
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
    test_name: shiprocket_invoice_charged_amount_freight_validation
    test_type: semantic_check
    linked_rule_id: rule.logistics.shiprocket_invoice_charged_amount_freight
    applies_to:
    - generated_sql
    - retrieval_bundle
    - card_extraction
    required_pattern: rule condition satisfied
    forbidden_pattern: rule violation
    semantic_condition: shiprocket invoice charged amount freight
    severity: high
    failure_message: 'Logistics validation failed: shiprocket_invoice_charged_amount_freight'
    auto_fix_hint: repair using relevant canonical cards
    blocking: false
    evidence_refs:
    - evidence.logistics_kb_doc
    - evidence.cognee_design_v4
    - evidence.unified_edge_scope
```

```yaml
candidate_card:
  card_type: validation_test
  card_id: validation_test.logistics.shiprocket_settlement_charged_amount_cod
  name: Shiprocket Settlement Charged Amount Cod Validation
  fields:
    name: Shiprocket Settlement Charged Amount Cod Validation
    description: Validation test enforcing rule shiprocket_settlement_charged_amount_cod.
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
    test_name: shiprocket_settlement_charged_amount_cod_validation
    test_type: semantic_check
    linked_rule_id: rule.logistics.shiprocket_settlement_charged_amount_cod
    applies_to:
    - generated_sql
    - retrieval_bundle
    - card_extraction
    required_pattern: rule condition satisfied
    forbidden_pattern: rule violation
    semantic_condition: shiprocket settlement charged amount cod
    severity: high
    failure_message: 'Logistics validation failed: shiprocket_settlement_charged_amount_cod'
    auto_fix_hint: repair using relevant canonical cards
    blocking: false
    evidence_refs:
    - evidence.logistics_kb_doc
    - evidence.cognee_design_v4
    - evidence.unified_edge_scope
```

```yaml
candidate_card:
  card_type: validation_test
  card_id: validation_test.logistics.dtdc_settlement_charged_amount_cod_value
  name: Dtdc Settlement Charged Amount Cod Value Validation
  fields:
    name: Dtdc Settlement Charged Amount Cod Value Validation
    description: Validation test enforcing rule dtdc_settlement_charged_amount_cod_value.
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
    test_name: dtdc_settlement_charged_amount_cod_value_validation
    test_type: semantic_check
    linked_rule_id: rule.logistics.dtdc_settlement_charged_amount_cod_value
    applies_to:
    - generated_sql
    - retrieval_bundle
    - card_extraction
    required_pattern: rule condition satisfied
    forbidden_pattern: rule violation
    semantic_condition: dtdc settlement charged amount cod value
    severity: high
    failure_message: 'Logistics validation failed: dtdc_settlement_charged_amount_cod_value'
    auto_fix_hint: repair using relevant canonical cards
    blocking: false
    evidence_refs:
    - evidence.logistics_kb_doc
    - evidence.cognee_design_v4
    - evidence.unified_edge_scope
```

```yaml
candidate_card:
  card_type: validation_test
  card_id: validation_test.logistics.ekart_settlement_transaction_type_required
  name: Ekart Settlement Transaction Type Required Validation
  fields:
    name: Ekart Settlement Transaction Type Required Validation
    description: Validation test enforcing rule ekart_settlement_transaction_type_required.
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
    test_name: ekart_settlement_transaction_type_required_validation
    test_type: semantic_check
    linked_rule_id: rule.logistics.ekart_settlement_transaction_type_required
    applies_to:
    - generated_sql
    - retrieval_bundle
    - card_extraction
    required_pattern: rule condition satisfied
    forbidden_pattern: rule violation
    semantic_condition: ekart settlement transaction type required
    severity: high
    failure_message: 'Logistics validation failed: ekart_settlement_transaction_type_required'
    auto_fix_hint: repair using relevant canonical cards
    blocking: false
    evidence_refs:
    - evidence.logistics_kb_doc
    - evidence.cognee_design_v4
    - evidence.unified_edge_scope
```

```yaml
candidate_card:
  card_type: validation_test
  card_id: validation_test.logistics.qr_cod_separate_from_cash
  name: Qr Cod Separate From Cash Validation
  fields:
    name: Qr Cod Separate From Cash Validation
    description: Validation test enforcing rule qr_cod_separate_from_cash.
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
    test_name: qr_cod_separate_from_cash_validation
    test_type: semantic_check
    linked_rule_id: rule.logistics.qr_cod_separate_from_cash
    applies_to:
    - generated_sql
    - retrieval_bundle
    - card_extraction
    required_pattern: rule condition satisfied
    forbidden_pattern: rule violation
    semantic_condition: qr cod separate from cash
    severity: high
    failure_message: 'Logistics validation failed: qr_cod_separate_from_cash'
    auto_fix_hint: repair using relevant canonical cards
    blocking: false
    evidence_refs:
    - evidence.logistics_kb_doc
    - evidence.cognee_design_v4
    - evidence.unified_edge_scope
```

```yaml
candidate_card:
  card_type: validation_test
  card_id: validation_test.logistics.avoid_null_value_inference
  name: Avoid Null Value Inference Validation
  fields:
    name: Avoid Null Value Inference Validation
    description: Validation test enforcing rule avoid_null_value_inference.
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
    test_name: avoid_null_value_inference_validation
    test_type: semantic_check
    linked_rule_id: rule.logistics.avoid_null_value_inference
    applies_to:
    - generated_sql
    - retrieval_bundle
    - card_extraction
    required_pattern: rule condition satisfied
    forbidden_pattern: rule violation
    semantic_condition: avoid null value inference
    severity: high
    failure_message: 'Logistics validation failed: avoid_null_value_inference'
    auto_fix_hint: repair using relevant canonical cards
    blocking: false
    evidence_refs:
    - evidence.logistics_kb_doc
    - evidence.cognee_design_v4
    - evidence.unified_edge_scope
```

```yaml
candidate_card:
  card_type: validation_test
  card_id: validation_test.logistics.integer_scope_filters_not_strings
  name: Integer Scope Filters Not Strings Validation
  fields:
    name: Integer Scope Filters Not Strings Validation
    description: Validation test enforcing rule integer_scope_filters_not_strings.
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
    test_name: integer_scope_filters_not_strings_validation
    test_type: semantic_check
    linked_rule_id: rule.logistics.integer_scope_filters_not_strings
    applies_to:
    - generated_sql
    - retrieval_bundle
    - card_extraction
    required_pattern: rule condition satisfied
    forbidden_pattern: rule violation
    semantic_condition: integer scope filters not strings
    severity: high
    failure_message: 'Logistics validation failed: integer_scope_filters_not_strings'
    auto_fix_hint: repair using relevant canonical cards
    blocking: false
    evidence_refs:
    - evidence.logistics_kb_doc
    - evidence.cognee_design_v4
    - evidence.unified_edge_scope
```

```yaml
candidate_card:
  card_type: validation_test
  card_id: validation_test.logistics.account_filters_from_adb_only
  name: Account Filters From Adb Only Validation
  fields:
    name: Account Filters From Adb Only Validation
    description: Validation test enforcing rule account_filters_from_adb_only.
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
    test_name: account_filters_from_adb_only_validation
    test_type: semantic_check
    linked_rule_id: rule.logistics.account_filters_from_adb_only
    applies_to:
    - generated_sql
    - retrieval_bundle
    - card_extraction
    required_pattern: rule condition satisfied
    forbidden_pattern: rule violation
    semantic_condition: account filters from adb only
    severity: high
    failure_message: 'Logistics validation failed: account_filters_from_adb_only'
    auto_fix_hint: repair using relevant canonical cards
    blocking: false
    evidence_refs:
    - evidence.logistics_kb_doc
    - evidence.cognee_design_v4
    - evidence.unified_edge_scope
```

```yaml
candidate_card:
  card_type: validation_test
  card_id: validation_test.logistics.document_unsupported_reason_when_metric_missing
  name: Document Unsupported Reason When Metric Missing Validation
  fields:
    name: Document Unsupported Reason When Metric Missing Validation
    description: Validation test enforcing rule document_unsupported_reason_when_metric_missing.
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
    test_name: document_unsupported_reason_when_metric_missing_validation
    test_type: semantic_check
    linked_rule_id: rule.logistics.document_unsupported_reason_when_metric_missing
    applies_to:
    - generated_sql
    - retrieval_bundle
    - card_extraction
    required_pattern: rule condition satisfied
    forbidden_pattern: rule violation
    semantic_condition: document unsupported reason when metric missing
    severity: high
    failure_message: 'Logistics validation failed: document_unsupported_reason_when_metric_missing'
    auto_fix_hint: repair using relevant canonical cards
    blocking: false
    evidence_refs:
    - evidence.logistics_kb_doc
    - evidence.cognee_design_v4
    - evidence.unified_edge_scope
```

### 4.25 output_contract cards

```yaml
candidate_card:
  card_type: output_contract
  card_id: output_contract.logistics_reconciliation_summary
  name: Logistics Reconciliation Summary
  fields:
    name: Logistics Reconciliation Summary
    description: Output contract for logistics_reconciliation_summary.
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
    contract_name: logistics_reconciliation_summary
    output_type: reconciliation
    required_sections: summary; resolved_scope; evidence_tables; metrics_or_matches; caveats; confidence; next_actions
    optional_sections: unmatched_records; top_drivers; fallback_sources; validation_warnings
    schema: structured markdown/json-compatible sections
    required_fields:
    - query
    - date_range
    - scope
    - metrics
    - caveats
    - source_confidence
    record_grouping: by courier/date/awb/batch depending on query
    sorting_guidance: largest variance or latest date first
    display_guidance: show amount semantics and source caveats
    failure_output_shape: unresolved_scope_or_unsupported_source_report
    evidence_refs:
    - evidence.logistics_kb_doc
    - evidence.cognee_design_v4
    - evidence.unified_edge_scope
```

```yaml
candidate_card:
  card_type: output_contract
  card_id: output_contract.logistics_metric_summary
  name: Logistics Metric Summary
  fields:
    name: Logistics Metric Summary
    description: Output contract for logistics_metric_summary.
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
    contract_name: logistics_metric_summary
    output_type: analytical
    required_sections: summary; resolved_scope; evidence_tables; metrics_or_matches; caveats; confidence; next_actions
    optional_sections: unmatched_records; top_drivers; fallback_sources; validation_warnings
    schema: structured markdown/json-compatible sections
    required_fields:
    - query
    - date_range
    - scope
    - metrics
    - caveats
    - source_confidence
    record_grouping: by courier/date/awb/batch depending on query
    sorting_guidance: largest variance or latest date first
    display_guidance: show amount semantics and source caveats
    failure_output_shape: unresolved_scope_or_unsupported_source_report
    evidence_refs:
    - evidence.logistics_kb_doc
    - evidence.cognee_design_v4
    - evidence.unified_edge_scope
```

```yaml
candidate_card:
  card_type: output_contract
  card_id: output_contract.logistics_diagnostic_summary
  name: Logistics Diagnostic Summary
  fields:
    name: Logistics Diagnostic Summary
    description: Output contract for logistics_diagnostic_summary.
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
    contract_name: logistics_diagnostic_summary
    output_type: diagnostic
    required_sections: summary; resolved_scope; evidence_tables; metrics_or_matches; caveats; confidence; next_actions
    optional_sections: unmatched_records; top_drivers; fallback_sources; validation_warnings
    schema: structured markdown/json-compatible sections
    required_fields:
    - query
    - date_range
    - scope
    - metrics
    - caveats
    - source_confidence
    record_grouping: by courier/date/awb/batch depending on query
    sorting_guidance: largest variance or latest date first
    display_guidance: show amount semantics and source caveats
    failure_output_shape: unresolved_scope_or_unsupported_source_report
    evidence_refs:
    - evidence.logistics_kb_doc
    - evidence.cognee_design_v4
    - evidence.unified_edge_scope
```

```yaml
candidate_card:
  card_type: output_contract
  card_id: output_contract.logistics_money_flow_trace
  name: Logistics Money Flow Trace
  fields:
    name: Logistics Money Flow Trace
    description: Output contract for logistics_money_flow_trace.
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
    contract_name: logistics_money_flow_trace
    output_type: diagnostic
    required_sections: summary; resolved_scope; evidence_tables; metrics_or_matches; caveats; confidence; next_actions
    optional_sections: unmatched_records; top_drivers; fallback_sources; validation_warnings
    schema: structured markdown/json-compatible sections
    required_fields:
    - query
    - date_range
    - scope
    - metrics
    - caveats
    - source_confidence
    record_grouping: by courier/date/awb/batch depending on query
    sorting_guidance: largest variance or latest date first
    display_guidance: show amount semantics and source caveats
    failure_output_shape: unresolved_scope_or_unsupported_source_report
    evidence_refs:
    - evidence.logistics_kb_doc
    - evidence.cognee_design_v4
    - evidence.unified_edge_scope
```

```yaml
candidate_card:
  card_type: output_contract
  card_id: output_contract.logistics_data_quality_report
  name: Logistics Data Quality Report
  fields:
    name: Logistics Data Quality Report
    description: Output contract for logistics_data_quality_report.
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
    contract_name: logistics_data_quality_report
    output_type: diagnostic
    required_sections: summary; resolved_scope; evidence_tables; metrics_or_matches; caveats; confidence; next_actions
    optional_sections: unmatched_records; top_drivers; fallback_sources; validation_warnings
    schema: structured markdown/json-compatible sections
    required_fields:
    - query
    - date_range
    - scope
    - metrics
    - caveats
    - source_confidence
    record_grouping: by courier/date/awb/batch depending on query
    sorting_guidance: largest variance or latest date first
    display_guidance: show amount semantics and source caveats
    failure_output_shape: unresolved_scope_or_unsupported_source_report
    evidence_refs:
    - evidence.logistics_kb_doc
    - evidence.cognee_design_v4
    - evidence.unified_edge_scope
```

### 4.26 execution_constraint_set cards

```yaml
candidate_card:
  card_type: execution_constraint_set
  card_id: execution_constraint_set.logistics_general_analytics
  name: Logistics General Analytics
  fields:
    name: Logistics General Analytics
    description: Execution constraint bundle for logistics_general_analytics.
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
    constraint_set_name: logistics_general_analytics
    constraint_set_type: analytical; reconciliation; diagnostic
    applies_to:
    - logistics query patterns and metric implementations
    rules:
    - rule.logistics.required_scope_context
    - rule.logistics.business_flow_binding_required_for_cross_platform
    - rule.logistics.do_not_create_bfb_from_generic_vendor_doc
    - rule.logistics.amount_semantics_not_by_name
    - rule.logistics.charged_amount_table_specific
    - rule.logistics.active_filter_when_available
    - rule.logistics.empty_tables_schema_only
    - rule.logistics.low_confidence_requires_warning
    - rule.logistics.fallback_sources_explicit_only
    - rule.logistics.awb_primary_reconciliation_unit
    - rule.logistics.do_not_join_awb_to_bank_without_batch
    - rule.logistics.preaggregate_before_order_join
    validation_tests:
    - validation_test.logistics.required_scope_context
    - validation_test.logistics.business_flow_binding_required_for_cross_platform
    - validation_test.logistics.do_not_create_bfb_from_generic_vendor_doc
    - validation_test.logistics.amount_semantics_not_by_name
    - validation_test.logistics.charged_amount_table_specific
    - validation_test.logistics.active_filter_when_available
    - validation_test.logistics.empty_tables_schema_only
    - validation_test.logistics.low_confidence_requires_warning
    - validation_test.logistics.fallback_sources_explicit_only
    - validation_test.logistics.awb_primary_reconciliation_unit
    - validation_test.logistics.do_not_join_awb_to_bank_without_batch
    - validation_test.logistics.preaggregate_before_order_join
    query_patterns:
    - query_pattern.logistics.shipment_count_by_courier
    - query_pattern.logistics.delivery_and_rto_rate
    - query_pattern.logistics.amount_semantics_audit
    - query_pattern.logistics.scope_binding_injection_check
    output_contract_id: output_contract.logistics_reconciliation_summary
    blocking_failures: missing scope; unsafe amount semantics; empty table usage; AWB to bank grain mismatch
    warning_failures: low confidence native source; fallback source used
    evidence_refs:
    - evidence.logistics_kb_doc
    - evidence.cognee_design_v4
    - evidence.unified_edge_scope
```

```yaml
candidate_card:
  card_type: execution_constraint_set
  card_id: execution_constraint_set.logistics_reconciliation
  name: Logistics Reconciliation
  fields:
    name: Logistics Reconciliation
    description: Execution constraint bundle for logistics_reconciliation.
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
    constraint_set_name: logistics_reconciliation
    constraint_set_type: analytical; reconciliation; diagnostic
    applies_to:
    - logistics query patterns and metric implementations
    rules:
    - rule.logistics.required_scope_context
    - rule.logistics.business_flow_binding_required_for_cross_platform
    - rule.logistics.do_not_create_bfb_from_generic_vendor_doc
    - rule.logistics.amount_semantics_not_by_name
    - rule.logistics.charged_amount_table_specific
    - rule.logistics.active_filter_when_available
    - rule.logistics.empty_tables_schema_only
    - rule.logistics.low_confidence_requires_warning
    - rule.logistics.fallback_sources_explicit_only
    - rule.logistics.awb_primary_reconciliation_unit
    - rule.logistics.do_not_join_awb_to_bank_without_batch
    - rule.logistics.preaggregate_before_order_join
    validation_tests:
    - validation_test.logistics.required_scope_context
    - validation_test.logistics.business_flow_binding_required_for_cross_platform
    - validation_test.logistics.do_not_create_bfb_from_generic_vendor_doc
    - validation_test.logistics.amount_semantics_not_by_name
    - validation_test.logistics.charged_amount_table_specific
    - validation_test.logistics.active_filter_when_available
    - validation_test.logistics.empty_tables_schema_only
    - validation_test.logistics.low_confidence_requires_warning
    - validation_test.logistics.fallback_sources_explicit_only
    - validation_test.logistics.awb_primary_reconciliation_unit
    - validation_test.logistics.do_not_join_awb_to_bank_without_batch
    - validation_test.logistics.preaggregate_before_order_join
    query_patterns:
    - query_pattern.logistics.shipments_without_invoice
    - query_pattern.logistics.shipments_without_cod_remittance
    - query_pattern.logistics.freight_overcharge_check
    - query_pattern.logistics.cod_expected_vs_remitted
    output_contract_id: output_contract.logistics_reconciliation_summary
    blocking_failures: missing scope; unsafe amount semantics; empty table usage; AWB to bank grain mismatch
    warning_failures: low confidence native source; fallback source used
    evidence_refs:
    - evidence.logistics_kb_doc
    - evidence.cognee_design_v4
    - evidence.unified_edge_scope
```

```yaml
candidate_card:
  card_type: execution_constraint_set
  card_id: execution_constraint_set.logistics_cod_reconciliation
  name: Logistics Cod Reconciliation
  fields:
    name: Logistics Cod Reconciliation
    description: Execution constraint bundle for logistics_cod_reconciliation.
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
    constraint_set_name: logistics_cod_reconciliation
    constraint_set_type: analytical; reconciliation; diagnostic
    applies_to:
    - logistics query patterns and metric implementations
    rules:
    - rule.logistics.required_scope_context
    - rule.logistics.business_flow_binding_required_for_cross_platform
    - rule.logistics.do_not_create_bfb_from_generic_vendor_doc
    - rule.logistics.amount_semantics_not_by_name
    - rule.logistics.charged_amount_table_specific
    - rule.logistics.active_filter_when_available
    - rule.logistics.empty_tables_schema_only
    - rule.logistics.low_confidence_requires_warning
    - rule.logistics.fallback_sources_explicit_only
    - rule.logistics.awb_primary_reconciliation_unit
    - rule.logistics.do_not_join_awb_to_bank_without_batch
    - rule.logistics.preaggregate_before_order_join
    validation_tests:
    - validation_test.logistics.required_scope_context
    - validation_test.logistics.business_flow_binding_required_for_cross_platform
    - validation_test.logistics.do_not_create_bfb_from_generic_vendor_doc
    - validation_test.logistics.amount_semantics_not_by_name
    - validation_test.logistics.charged_amount_table_specific
    - validation_test.logistics.active_filter_when_available
    - validation_test.logistics.empty_tables_schema_only
    - validation_test.logistics.low_confidence_requires_warning
    - validation_test.logistics.fallback_sources_explicit_only
    - validation_test.logistics.awb_primary_reconciliation_unit
    - validation_test.logistics.do_not_join_awb_to_bank_without_batch
    - validation_test.logistics.preaggregate_before_order_join
    query_patterns:
    - query_pattern.logistics.cod_expected_vs_remitted
    - query_pattern.logistics.cod_remittance_lag
    - query_pattern.logistics.shipments_without_cod_remittance
    output_contract_id: output_contract.logistics_reconciliation_summary
    blocking_failures: missing scope; unsafe amount semantics; empty table usage; AWB to bank grain mismatch
    warning_failures: low confidence native source; fallback source used
    evidence_refs:
    - evidence.logistics_kb_doc
    - evidence.cognee_design_v4
    - evidence.unified_edge_scope
```

```yaml
candidate_card:
  card_type: execution_constraint_set
  card_id: execution_constraint_set.logistics_freight_reconciliation
  name: Logistics Freight Reconciliation
  fields:
    name: Logistics Freight Reconciliation
    description: Execution constraint bundle for logistics_freight_reconciliation.
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
    constraint_set_name: logistics_freight_reconciliation
    constraint_set_type: analytical; reconciliation; diagnostic
    applies_to:
    - logistics query patterns and metric implementations
    rules:
    - rule.logistics.required_scope_context
    - rule.logistics.business_flow_binding_required_for_cross_platform
    - rule.logistics.do_not_create_bfb_from_generic_vendor_doc
    - rule.logistics.amount_semantics_not_by_name
    - rule.logistics.charged_amount_table_specific
    - rule.logistics.active_filter_when_available
    - rule.logistics.empty_tables_schema_only
    - rule.logistics.low_confidence_requires_warning
    - rule.logistics.fallback_sources_explicit_only
    - rule.logistics.awb_primary_reconciliation_unit
    - rule.logistics.do_not_join_awb_to_bank_without_batch
    - rule.logistics.preaggregate_before_order_join
    validation_tests:
    - validation_test.logistics.required_scope_context
    - validation_test.logistics.business_flow_binding_required_for_cross_platform
    - validation_test.logistics.do_not_create_bfb_from_generic_vendor_doc
    - validation_test.logistics.amount_semantics_not_by_name
    - validation_test.logistics.charged_amount_table_specific
    - validation_test.logistics.active_filter_when_available
    - validation_test.logistics.empty_tables_schema_only
    - validation_test.logistics.low_confidence_requires_warning
    - validation_test.logistics.fallback_sources_explicit_only
    - validation_test.logistics.awb_primary_reconciliation_unit
    - validation_test.logistics.do_not_join_awb_to_bank_without_batch
    - validation_test.logistics.preaggregate_before_order_join
    query_patterns:
    - query_pattern.logistics.freight_billed_by_awb
    - query_pattern.logistics.freight_component_breakdown
    - query_pattern.logistics.freight_overcharge_check
    - query_pattern.logistics.rto_freight_validation
    - query_pattern.logistics.cod_fee_on_prepaid_detection
    output_contract_id: output_contract.logistics_reconciliation_summary
    blocking_failures: missing scope; unsafe amount semantics; empty table usage; AWB to bank grain mismatch
    warning_failures: low confidence native source; fallback source used
    evidence_refs:
    - evidence.logistics_kb_doc
    - evidence.cognee_design_v4
    - evidence.unified_edge_scope
```

```yaml
candidate_card:
  card_type: execution_constraint_set
  card_id: execution_constraint_set.logistics_batch_to_bank
  name: Logistics Batch To Bank
  fields:
    name: Logistics Batch To Bank
    description: Execution constraint bundle for logistics_batch_to_bank.
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
    constraint_set_name: logistics_batch_to_bank
    constraint_set_type: analytical; reconciliation; diagnostic
    applies_to:
    - logistics query patterns and metric implementations
    rules:
    - rule.logistics.required_scope_context
    - rule.logistics.business_flow_binding_required_for_cross_platform
    - rule.logistics.do_not_create_bfb_from_generic_vendor_doc
    - rule.logistics.amount_semantics_not_by_name
    - rule.logistics.charged_amount_table_specific
    - rule.logistics.active_filter_when_available
    - rule.logistics.empty_tables_schema_only
    - rule.logistics.low_confidence_requires_warning
    - rule.logistics.fallback_sources_explicit_only
    - rule.logistics.awb_primary_reconciliation_unit
    - rule.logistics.do_not_join_awb_to_bank_without_batch
    - rule.logistics.preaggregate_before_order_join
    validation_tests:
    - validation_test.logistics.required_scope_context
    - validation_test.logistics.business_flow_binding_required_for_cross_platform
    - validation_test.logistics.do_not_create_bfb_from_generic_vendor_doc
    - validation_test.logistics.amount_semantics_not_by_name
    - validation_test.logistics.charged_amount_table_specific
    - validation_test.logistics.active_filter_when_available
    - validation_test.logistics.empty_tables_schema_only
    - validation_test.logistics.low_confidence_requires_warning
    - validation_test.logistics.fallback_sources_explicit_only
    - validation_test.logistics.awb_primary_reconciliation_unit
    - validation_test.logistics.do_not_join_awb_to_bank_without_batch
    - validation_test.logistics.preaggregate_before_order_join
    query_patterns:
    - query_pattern.logistics.courier_batch_to_bank_bridge
    - query_pattern.logistics.bank_credit_unmatched_courier_reference
    - query_pattern.logistics.end_to_end_logistics_money_flow_trace
    output_contract_id: output_contract.logistics_reconciliation_summary
    blocking_failures: missing scope; unsafe amount semantics; empty table usage; AWB to bank grain mismatch
    warning_failures: low confidence native source; fallback source used
    evidence_refs:
    - evidence.logistics_kb_doc
    - evidence.cognee_design_v4
    - evidence.unified_edge_scope
```

```yaml
candidate_card:
  card_type: execution_constraint_set
  card_id: execution_constraint_set.shiprocket_guardrails
  name: Shiprocket Guardrails
  fields:
    name: Shiprocket Guardrails
    description: Execution constraint bundle for shiprocket_guardrails.
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
    constraint_set_name: shiprocket_guardrails
    constraint_set_type: analytical; reconciliation; diagnostic
    applies_to:
    - logistics query patterns and metric implementations
    rules:
    - rule.logistics.required_scope_context
    - rule.logistics.business_flow_binding_required_for_cross_platform
    - rule.logistics.do_not_create_bfb_from_generic_vendor_doc
    - rule.logistics.amount_semantics_not_by_name
    - rule.logistics.charged_amount_table_specific
    - rule.logistics.active_filter_when_available
    - rule.logistics.empty_tables_schema_only
    - rule.logistics.low_confidence_requires_warning
    - rule.logistics.fallback_sources_explicit_only
    - rule.logistics.awb_primary_reconciliation_unit
    - rule.logistics.do_not_join_awb_to_bank_without_batch
    - rule.logistics.preaggregate_before_order_join
    validation_tests:
    - validation_test.logistics.required_scope_context
    - validation_test.logistics.business_flow_binding_required_for_cross_platform
    - validation_test.logistics.do_not_create_bfb_from_generic_vendor_doc
    - validation_test.logistics.amount_semantics_not_by_name
    - validation_test.logistics.charged_amount_table_specific
    - validation_test.logistics.active_filter_when_available
    - validation_test.logistics.empty_tables_schema_only
    - validation_test.logistics.low_confidence_requires_warning
    - validation_test.logistics.fallback_sources_explicit_only
    - validation_test.logistics.awb_primary_reconciliation_unit
    - validation_test.logistics.do_not_join_awb_to_bank_without_batch
    - validation_test.logistics.preaggregate_before_order_join
    query_patterns:
    - query_pattern.logistics.shiprocket_courier_partner_freight_split
    - query_pattern.logistics.shiprocket_cod_by_underlying_courier
    output_contract_id: output_contract.logistics_reconciliation_summary
    blocking_failures: missing scope; unsafe amount semantics; empty table usage; AWB to bank grain mismatch
    warning_failures: low confidence native source; fallback source used
    evidence_refs:
    - evidence.logistics_kb_doc
    - evidence.cognee_design_v4
    - evidence.unified_edge_scope
```

```yaml
candidate_card:
  card_type: execution_constraint_set
  card_id: execution_constraint_set.delhivery_guardrails
  name: Delhivery Guardrails
  fields:
    name: Delhivery Guardrails
    description: Execution constraint bundle for delhivery_guardrails.
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
    constraint_set_name: delhivery_guardrails
    constraint_set_type: analytical; reconciliation; diagnostic
    applies_to:
    - logistics query patterns and metric implementations
    rules:
    - rule.logistics.required_scope_context
    - rule.logistics.business_flow_binding_required_for_cross_platform
    - rule.logistics.do_not_create_bfb_from_generic_vendor_doc
    - rule.logistics.amount_semantics_not_by_name
    - rule.logistics.charged_amount_table_specific
    - rule.logistics.active_filter_when_available
    - rule.logistics.empty_tables_schema_only
    - rule.logistics.low_confidence_requires_warning
    - rule.logistics.fallback_sources_explicit_only
    - rule.logistics.awb_primary_reconciliation_unit
    - rule.logistics.do_not_join_awb_to_bank_without_batch
    - rule.logistics.preaggregate_before_order_join
    validation_tests:
    - validation_test.logistics.required_scope_context
    - validation_test.logistics.business_flow_binding_required_for_cross_platform
    - validation_test.logistics.do_not_create_bfb_from_generic_vendor_doc
    - validation_test.logistics.amount_semantics_not_by_name
    - validation_test.logistics.charged_amount_table_specific
    - validation_test.logistics.active_filter_when_available
    - validation_test.logistics.empty_tables_schema_only
    - validation_test.logistics.low_confidence_requires_warning
    - validation_test.logistics.fallback_sources_explicit_only
    - validation_test.logistics.awb_primary_reconciliation_unit
    - validation_test.logistics.do_not_join_awb_to_bank_without_batch
    - validation_test.logistics.preaggregate_before_order_join
    query_patterns:
    - query_pattern.logistics.delhivery_freight_component_reconciliation
    - query_pattern.logistics.delhivery_cod_qr_vs_cash
    output_contract_id: output_contract.logistics_reconciliation_summary
    blocking_failures: missing scope; unsafe amount semantics; empty table usage; AWB to bank grain mismatch
    warning_failures: low confidence native source; fallback source used
    evidence_refs:
    - evidence.logistics_kb_doc
    - evidence.cognee_design_v4
    - evidence.unified_edge_scope
```

```yaml
candidate_card:
  card_type: execution_constraint_set
  card_id: execution_constraint_set.dtdc_guardrails
  name: Dtdc Guardrails
  fields:
    name: Dtdc Guardrails
    description: Execution constraint bundle for dtdc_guardrails.
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
    constraint_set_name: dtdc_guardrails
    constraint_set_type: analytical; reconciliation; diagnostic
    applies_to:
    - logistics query patterns and metric implementations
    rules:
    - rule.logistics.required_scope_context
    - rule.logistics.business_flow_binding_required_for_cross_platform
    - rule.logistics.do_not_create_bfb_from_generic_vendor_doc
    - rule.logistics.amount_semantics_not_by_name
    - rule.logistics.charged_amount_table_specific
    - rule.logistics.active_filter_when_available
    - rule.logistics.empty_tables_schema_only
    - rule.logistics.low_confidence_requires_warning
    - rule.logistics.fallback_sources_explicit_only
    - rule.logistics.awb_primary_reconciliation_unit
    - rule.logistics.do_not_join_awb_to_bank_without_batch
    - rule.logistics.preaggregate_before_order_join
    validation_tests:
    - validation_test.logistics.required_scope_context
    - validation_test.logistics.business_flow_binding_required_for_cross_platform
    - validation_test.logistics.do_not_create_bfb_from_generic_vendor_doc
    - validation_test.logistics.amount_semantics_not_by_name
    - validation_test.logistics.charged_amount_table_specific
    - validation_test.logistics.active_filter_when_available
    - validation_test.logistics.empty_tables_schema_only
    - validation_test.logistics.low_confidence_requires_warning
    - validation_test.logistics.fallback_sources_explicit_only
    - validation_test.logistics.awb_primary_reconciliation_unit
    - validation_test.logistics.do_not_join_awb_to_bank_without_batch
    - validation_test.logistics.preaggregate_before_order_join
    query_patterns:
    - query_pattern.logistics.dtdc_settlement_to_shiprocket_freight_fallback
    - query_pattern.logistics.dtdc_utr_bank_bridge
    output_contract_id: output_contract.logistics_reconciliation_summary
    blocking_failures: missing scope; unsafe amount semantics; empty table usage; AWB to bank grain mismatch
    warning_failures: low confidence native source; fallback source used
    evidence_refs:
    - evidence.logistics_kb_doc
    - evidence.cognee_design_v4
    - evidence.unified_edge_scope
```

```yaml
candidate_card:
  card_type: execution_constraint_set
  card_id: execution_constraint_set.ekart_guardrails
  name: Ekart Guardrails
  fields:
    name: Ekart Guardrails
    description: Execution constraint bundle for ekart_guardrails.
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
    constraint_set_name: ekart_guardrails
    constraint_set_type: analytical; reconciliation; diagnostic
    applies_to:
    - logistics query patterns and metric implementations
    rules:
    - rule.logistics.required_scope_context
    - rule.logistics.business_flow_binding_required_for_cross_platform
    - rule.logistics.do_not_create_bfb_from_generic_vendor_doc
    - rule.logistics.amount_semantics_not_by_name
    - rule.logistics.charged_amount_table_specific
    - rule.logistics.active_filter_when_available
    - rule.logistics.empty_tables_schema_only
    - rule.logistics.low_confidence_requires_warning
    - rule.logistics.fallback_sources_explicit_only
    - rule.logistics.awb_primary_reconciliation_unit
    - rule.logistics.do_not_join_awb_to_bank_without_batch
    - rule.logistics.preaggregate_before_order_join
    validation_tests:
    - validation_test.logistics.required_scope_context
    - validation_test.logistics.business_flow_binding_required_for_cross_platform
    - validation_test.logistics.do_not_create_bfb_from_generic_vendor_doc
    - validation_test.logistics.amount_semantics_not_by_name
    - validation_test.logistics.charged_amount_table_specific
    - validation_test.logistics.active_filter_when_available
    - validation_test.logistics.empty_tables_schema_only
    - validation_test.logistics.low_confidence_requires_warning
    - validation_test.logistics.fallback_sources_explicit_only
    - validation_test.logistics.awb_primary_reconciliation_unit
    - validation_test.logistics.do_not_join_awb_to_bank_without_batch
    - validation_test.logistics.preaggregate_before_order_join
    query_patterns:
    - query_pattern.logistics.ekart_cod_pos_split
    - query_pattern.logistics.ekart_batch_deduplicated_bank_bridge
    output_contract_id: output_contract.logistics_reconciliation_summary
    blocking_failures: missing scope; unsafe amount semantics; empty table usage; AWB to bank grain mismatch
    warning_failures: low confidence native source; fallback source used
    evidence_refs:
    - evidence.logistics_kb_doc
    - evidence.cognee_design_v4
    - evidence.unified_edge_scope
```

```yaml
candidate_card:
  card_type: execution_constraint_set
  card_id: execution_constraint_set.xpressbees_low_confidence_guardrails
  name: Xpressbees Low Confidence Guardrails
  fields:
    name: Xpressbees Low Confidence Guardrails
    description: Execution constraint bundle for xpressbees_low_confidence_guardrails.
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
    constraint_set_name: xpressbees_low_confidence_guardrails
    constraint_set_type: analytical; reconciliation; diagnostic
    applies_to:
    - logistics query patterns and metric implementations
    rules:
    - rule.logistics.required_scope_context
    - rule.logistics.business_flow_binding_required_for_cross_platform
    - rule.logistics.do_not_create_bfb_from_generic_vendor_doc
    - rule.logistics.amount_semantics_not_by_name
    - rule.logistics.charged_amount_table_specific
    - rule.logistics.active_filter_when_available
    - rule.logistics.empty_tables_schema_only
    - rule.logistics.low_confidence_requires_warning
    - rule.logistics.fallback_sources_explicit_only
    - rule.logistics.awb_primary_reconciliation_unit
    - rule.logistics.do_not_join_awb_to_bank_without_batch
    - rule.logistics.preaggregate_before_order_join
    validation_tests:
    - validation_test.logistics.required_scope_context
    - validation_test.logistics.business_flow_binding_required_for_cross_platform
    - validation_test.logistics.do_not_create_bfb_from_generic_vendor_doc
    - validation_test.logistics.amount_semantics_not_by_name
    - validation_test.logistics.charged_amount_table_specific
    - validation_test.logistics.active_filter_when_available
    - validation_test.logistics.empty_tables_schema_only
    - validation_test.logistics.low_confidence_requires_warning
    - validation_test.logistics.fallback_sources_explicit_only
    - validation_test.logistics.awb_primary_reconciliation_unit
    - validation_test.logistics.do_not_join_awb_to_bank_without_batch
    - validation_test.logistics.preaggregate_before_order_join
    query_patterns:
    - query_pattern.logistics.xpressbees_native_vs_shiprocket_fallback
    - query_pattern.logistics.low_confidence_native_validation
    output_contract_id: output_contract.logistics_reconciliation_summary
    blocking_failures: missing scope; unsafe amount semantics; empty table usage; AWB to bank grain mismatch
    warning_failures: low confidence native source; fallback source used
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
  generic_logistics_boundary: Generic vendor/domain docs must not emit tenant, group, platform account, account data binding,
    business scope set, or business flow binding cards.
```

### 5.1 Candidate Edge Registry

```yaml
candidate_edge:
  edge_id: edge.table.zs_observe.dtdc_settlement.has_relationship.relationship.dtdc_settlement.bank_statement.utr
  edge_type: HAS_RELATIONSHIP
  source: table.zs_observe.dtdc_settlement
  target: relationship.dtdc_settlement.bank_statement.utr
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
  edge_id: edge.relationship.dtdc_settlement.bank_statement.utr.source_table.table.zs_observe.dtdc_settlement
  edge_type: SOURCE_TABLE
  source: relationship.dtdc_settlement.bank_statement.utr
  target: table.zs_observe.dtdc_settlement
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
  edge_id: edge.table.zs_observe.bank_statement.has_relationship.relationship.dtdc_settlement.bank_statement.utr
  edge_type: HAS_RELATIONSHIP
  source: table.zs_observe.bank_statement
  target: relationship.dtdc_settlement.bank_statement.utr
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
  edge_id: edge.relationship.dtdc_settlement.bank_statement.utr.target_table.table.zs_observe.bank_statement
  edge_type: TARGET_TABLE
  source: relationship.dtdc_settlement.bank_statement.utr
  target: table.zs_observe.bank_statement
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
  edge_id: edge.relationship.dtdc_settlement.bank_statement.utr.uses_source_column.column.zs_observe.dtdc_settlement.utr_no
  edge_type: USES_SOURCE_COLUMN
  source: relationship.dtdc_settlement.bank_statement.utr
  target: column.zs_observe.dtdc_settlement.utr_no
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
  edge_id: edge.relationship.dtdc_settlement.bank_statement.utr.uses_target_column.column.zs_observe.bank_statement.utr_no
  edge_type: USES_TARGET_COLUMN
  source: relationship.dtdc_settlement.bank_statement.utr
  target: column.zs_observe.bank_statement.utr_no
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
  edge_id: edge.table.zs_observe.dtdc_settlement.has_relationship.relationship.dtdc_settlement.bank_statement.bank_ref
  edge_type: HAS_RELATIONSHIP
  source: table.zs_observe.dtdc_settlement
  target: relationship.dtdc_settlement.bank_statement.bank_ref
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
  edge_id: edge.relationship.dtdc_settlement.bank_statement.bank_ref.source_table.table.zs_observe.dtdc_settlement
  edge_type: SOURCE_TABLE
  source: relationship.dtdc_settlement.bank_statement.bank_ref
  target: table.zs_observe.dtdc_settlement
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
  edge_id: edge.table.zs_observe.bank_statement.has_relationship.relationship.dtdc_settlement.bank_statement.bank_ref
  edge_type: HAS_RELATIONSHIP
  source: table.zs_observe.bank_statement
  target: relationship.dtdc_settlement.bank_statement.bank_ref
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
  edge_id: edge.relationship.dtdc_settlement.bank_statement.bank_ref.target_table.table.zs_observe.bank_statement
  edge_type: TARGET_TABLE
  source: relationship.dtdc_settlement.bank_statement.bank_ref
  target: table.zs_observe.bank_statement
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
  edge_id: edge.relationship.dtdc_settlement.bank_statement.bank_ref.uses_source_column.column.zs_observe.dtdc_settlement.bank_ref_number
  edge_type: USES_SOURCE_COLUMN
  source: relationship.dtdc_settlement.bank_statement.bank_ref
  target: column.zs_observe.dtdc_settlement.bank_ref_number
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
  edge_id: edge.relationship.dtdc_settlement.bank_statement.bank_ref.uses_target_column.column.zs_observe.bank_statement.bank_reference_no
  edge_type: USES_TARGET_COLUMN
  source: relationship.dtdc_settlement.bank_statement.bank_ref
  target: column.zs_observe.bank_statement.bank_reference_no
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
  edge_id: edge.table.zs_observe.delhivery_settlement.has_relationship.relationship.delhivery_settlement.bank_statement.utr
  edge_type: HAS_RELATIONSHIP
  source: table.zs_observe.delhivery_settlement
  target: relationship.delhivery_settlement.bank_statement.utr
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
  edge_id: edge.relationship.delhivery_settlement.bank_statement.utr.source_table.table.zs_observe.delhivery_settlement
  edge_type: SOURCE_TABLE
  source: relationship.delhivery_settlement.bank_statement.utr
  target: table.zs_observe.delhivery_settlement
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
  edge_id: edge.table.zs_observe.bank_statement.has_relationship.relationship.delhivery_settlement.bank_statement.utr
  edge_type: HAS_RELATIONSHIP
  source: table.zs_observe.bank_statement
  target: relationship.delhivery_settlement.bank_statement.utr
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
  edge_id: edge.relationship.delhivery_settlement.bank_statement.utr.target_table.table.zs_observe.bank_statement
  edge_type: TARGET_TABLE
  source: relationship.delhivery_settlement.bank_statement.utr
  target: table.zs_observe.bank_statement
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
  edge_id: edge.relationship.delhivery_settlement.bank_statement.utr.uses_source_column.column.zs_observe.delhivery_settlement.utr_no
  edge_type: USES_SOURCE_COLUMN
  source: relationship.delhivery_settlement.bank_statement.utr
  target: column.zs_observe.delhivery_settlement.utr_no
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
  edge_id: edge.relationship.delhivery_settlement.bank_statement.utr.uses_target_column.column.zs_observe.bank_statement.utr_no
  edge_type: USES_TARGET_COLUMN
  source: relationship.delhivery_settlement.bank_statement.utr
  target: column.zs_observe.bank_statement.utr_no
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
  edge_id: edge.table.zs_observe.ekart_settlement.has_relationship.relationship.ekart_settlement.bank_statement.bank_ref
  edge_type: HAS_RELATIONSHIP
  source: table.zs_observe.ekart_settlement
  target: relationship.ekart_settlement.bank_statement.bank_ref
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
  edge_id: edge.relationship.ekart_settlement.bank_statement.bank_ref.source_table.table.zs_observe.ekart_settlement
  edge_type: SOURCE_TABLE
  source: relationship.ekart_settlement.bank_statement.bank_ref
  target: table.zs_observe.ekart_settlement
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
  edge_id: edge.table.zs_observe.bank_statement.has_relationship.relationship.ekart_settlement.bank_statement.bank_ref
  edge_type: HAS_RELATIONSHIP
  source: table.zs_observe.bank_statement
  target: relationship.ekart_settlement.bank_statement.bank_ref
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
  edge_id: edge.relationship.ekart_settlement.bank_statement.bank_ref.target_table.table.zs_observe.bank_statement
  edge_type: TARGET_TABLE
  source: relationship.ekart_settlement.bank_statement.bank_ref
  target: table.zs_observe.bank_statement
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
  edge_id: edge.relationship.ekart_settlement.bank_statement.bank_ref.uses_source_column.column.zs_observe.ekart_settlement.bank_reference_no
  edge_type: USES_SOURCE_COLUMN
  source: relationship.ekart_settlement.bank_statement.bank_ref
  target: column.zs_observe.ekart_settlement.bank_reference_no
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
  edge_id: edge.relationship.ekart_settlement.bank_statement.bank_ref.uses_target_column.column.zs_observe.bank_statement.bank_reference_no
  edge_type: USES_TARGET_COLUMN
  source: relationship.ekart_settlement.bank_statement.bank_ref
  target: column.zs_observe.bank_statement.bank_reference_no
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
  edge_id: edge.table.zs_observe.shiprocket_oms.has_relationship.relationship.shiprocket_oms.bank_statement.utr
  edge_type: HAS_RELATIONSHIP
  source: table.zs_observe.shiprocket_oms
  target: relationship.shiprocket_oms.bank_statement.utr
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
  edge_id: edge.relationship.shiprocket_oms.bank_statement.utr.source_table.table.zs_observe.shiprocket_oms
  edge_type: SOURCE_TABLE
  source: relationship.shiprocket_oms.bank_statement.utr
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
  edge_id: edge.table.zs_observe.bank_statement.has_relationship.relationship.shiprocket_oms.bank_statement.utr
  edge_type: HAS_RELATIONSHIP
  source: table.zs_observe.bank_statement
  target: relationship.shiprocket_oms.bank_statement.utr
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
  edge_id: edge.relationship.shiprocket_oms.bank_statement.utr.target_table.table.zs_observe.bank_statement
  edge_type: TARGET_TABLE
  source: relationship.shiprocket_oms.bank_statement.utr
  target: table.zs_observe.bank_statement
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
  edge_id: edge.relationship.shiprocket_oms.bank_statement.utr.uses_source_column.column.zs_observe.shiprocket_oms.utr_no
  edge_type: USES_SOURCE_COLUMN
  source: relationship.shiprocket_oms.bank_statement.utr
  target: column.zs_observe.shiprocket_oms.utr_no
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
  edge_id: edge.relationship.shiprocket_oms.bank_statement.utr.uses_target_column.column.zs_observe.bank_statement.utr_no
  edge_type: USES_TARGET_COLUMN
  source: relationship.shiprocket_oms.bank_statement.utr
  target: column.zs_observe.bank_statement.utr_no
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
  edge_id: edge.table.zs_observe.bank_statement.has_column.column.zs_observe.bank_statement.utr_no
  edge_type: HAS_COLUMN
  source: table.zs_observe.bank_statement
  target: column.zs_observe.bank_statement.utr_no
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
  edge_id: edge.column.zs_observe.bank_statement.utr_no.belongs_to_table.table.zs_observe.bank_statement
  edge_type: BELONGS_TO_TABLE
  source: column.zs_observe.bank_statement.utr_no
  target: table.zs_observe.bank_statement
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
    materialized_from: edge.table.zs_observe.bank_statement.has_column.column.zs_observe.bank_statement.utr_no
```

```yaml
candidate_edge:
  edge_id: edge.table.zs_observe.bank_statement.has_column.column.zs_observe.bank_statement.bank_reference_no
  edge_type: HAS_COLUMN
  source: table.zs_observe.bank_statement
  target: column.zs_observe.bank_statement.bank_reference_no
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
  edge_id: edge.column.zs_observe.bank_statement.bank_reference_no.belongs_to_table.table.zs_observe.bank_statement
  edge_type: BELONGS_TO_TABLE
  source: column.zs_observe.bank_statement.bank_reference_no
  target: table.zs_observe.bank_statement
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
    materialized_from: edge.table.zs_observe.bank_statement.has_column.column.zs_observe.bank_statement.bank_reference_no
```

```yaml
candidate_edge:
  edge_id: edge.table.zs_observe.bank_statement.has_column.column.zs_observe.bank_statement.credit_amount
  edge_type: HAS_COLUMN
  source: table.zs_observe.bank_statement
  target: column.zs_observe.bank_statement.credit_amount
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
  edge_id: edge.column.zs_observe.bank_statement.credit_amount.belongs_to_table.table.zs_observe.bank_statement
  edge_type: BELONGS_TO_TABLE
  source: column.zs_observe.bank_statement.credit_amount
  target: table.zs_observe.bank_statement
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
    materialized_from: edge.table.zs_observe.bank_statement.has_column.column.zs_observe.bank_statement.credit_amount
```

```yaml
candidate_edge:
  edge_id: edge.table.zs_observe.bank_statement.has_column.column.zs_observe.bank_statement.transaction_date
  edge_type: HAS_COLUMN
  source: table.zs_observe.bank_statement
  target: column.zs_observe.bank_statement.transaction_date
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
  edge_id: edge.column.zs_observe.bank_statement.transaction_date.belongs_to_table.table.zs_observe.bank_statement
  edge_type: BELONGS_TO_TABLE
  source: column.zs_observe.bank_statement.transaction_date
  target: table.zs_observe.bank_statement
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
    materialized_from: edge.table.zs_observe.bank_statement.has_column.column.zs_observe.bank_statement.transaction_date
```

```yaml
candidate_edge:
  edge_id: edge.table.zs_observe.bank_statement.has_column.column.zs_observe.bank_statement.bank_account_id
  edge_type: HAS_COLUMN
  source: table.zs_observe.bank_statement
  target: column.zs_observe.bank_statement.bank_account_id
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
  edge_id: edge.column.zs_observe.bank_statement.bank_account_id.belongs_to_table.table.zs_observe.bank_statement
  edge_type: BELONGS_TO_TABLE
  source: column.zs_observe.bank_statement.bank_account_id
  target: table.zs_observe.bank_statement
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
    materialized_from: edge.table.zs_observe.bank_statement.has_column.column.zs_observe.bank_statement.bank_account_id
```

```yaml
candidate_edge:
  edge_id: edge.business_process.order_to_shipment_flow.has_reconciliation_profile.reconciliation_profile.order_to_shipment
  edge_type: HAS_RECONCILIATION_PROFILE
  source: business_process.order_to_shipment_flow
  target: reconciliation_profile.order_to_shipment
  fields:
    edge_family: reconciliation_understanding
    evidence_basis: reconciliation_profile.fields.business_process_id
    confidence: high
    canonical_cognee_edge: true
    logistics_only: true
    canonical_edge_type: HAS_RECONCILIATION_PROFILE
    inverse_edge_type: SUPPORTS_PROCESS
    materialize_inverse: true
    edge_class: canonical
    source_type: business_process
    target_type: reconciliation_profile
```

```yaml
candidate_edge:
  edge_id: edge.reconciliation_profile.order_to_shipment.supports_process.business_process.order_to_shipment_flow
  edge_type: SUPPORTS_PROCESS
  source: reconciliation_profile.order_to_shipment
  target: business_process.order_to_shipment_flow
  fields:
    edge_family: reconciliation_understanding
    evidence_basis: materialized inverse of HAS_RECONCILIATION_PROFILE
    confidence: high
    canonical_cognee_edge: true
    logistics_only: true
    canonical_edge_type: SUPPORTS_PROCESS
    inverse_edge_type: HAS_RECONCILIATION_PROFILE
    materialize_inverse: true
    edge_class: canonical
    source_type: reconciliation_profile
    target_type: business_process
    materialized_from: edge.business_process.order_to_shipment_flow.has_reconciliation_profile.reconciliation_profile.order_to_shipment
```

```yaml
candidate_edge:
  edge_id: edge.reconciliation_profile.order_to_shipment.has_reconciliation_side.reconciliation_side.order_to_shipment.expected.5c1d27e4
  edge_type: HAS_RECONCILIATION_SIDE
  source: reconciliation_profile.order_to_shipment
  target: reconciliation_side.order_to_shipment.expected
  fields:
    edge_family: reconciliation_understanding
    evidence_basis: reconciliation_profile.fields.sides
    confidence: high
    canonical_cognee_edge: true
    logistics_only: true
    canonical_edge_type: HAS_RECONCILIATION_SIDE
    inverse_edge_type: BELONGS_TO_RECONCILIATION_PROFILE
    materialize_inverse: true
    edge_class: canonical
    source_type: reconciliation_profile
    target_type: reconciliation_side
    edge_properties:
      side_role: expected
```

```yaml
candidate_edge:
  edge_id: edge.reconciliation_side.order_to_shipment.expected.belongs_to_reconciliation_profile.reconciliation_profile.order_to_shipment.5c1d27e4
  edge_type: BELONGS_TO_RECONCILIATION_PROFILE
  source: reconciliation_side.order_to_shipment.expected
  target: reconciliation_profile.order_to_shipment
  fields:
    edge_family: reconciliation_understanding
    evidence_basis: materialized inverse of HAS_RECONCILIATION_SIDE
    confidence: high
    canonical_cognee_edge: true
    logistics_only: true
    canonical_edge_type: BELONGS_TO_RECONCILIATION_PROFILE
    inverse_edge_type: HAS_RECONCILIATION_SIDE
    materialize_inverse: true
    edge_class: canonical
    source_type: reconciliation_side
    target_type: reconciliation_profile
    materialized_from: edge.reconciliation_profile.order_to_shipment.has_reconciliation_side.reconciliation_side.order_to_shipment.expected.5c1d27e4
    edge_properties:
      side_role: expected
```

```yaml
candidate_edge:
  edge_id: edge.reconciliation_profile.order_to_shipment.has_reconciliation_side.reconciliation_side.order_to_shipment.actual.0342fa18
  edge_type: HAS_RECONCILIATION_SIDE
  source: reconciliation_profile.order_to_shipment
  target: reconciliation_side.order_to_shipment.actual
  fields:
    edge_family: reconciliation_understanding
    evidence_basis: reconciliation_profile.fields.sides
    confidence: high
    canonical_cognee_edge: true
    logistics_only: true
    canonical_edge_type: HAS_RECONCILIATION_SIDE
    inverse_edge_type: BELONGS_TO_RECONCILIATION_PROFILE
    materialize_inverse: true
    edge_class: canonical
    source_type: reconciliation_profile
    target_type: reconciliation_side
    edge_properties:
      side_role: actual
```

```yaml
candidate_edge:
  edge_id: edge.reconciliation_side.order_to_shipment.actual.belongs_to_reconciliation_profile.reconciliation_profile.order_to_shipment.0342fa18
  edge_type: BELONGS_TO_RECONCILIATION_PROFILE
  source: reconciliation_side.order_to_shipment.actual
  target: reconciliation_profile.order_to_shipment
  fields:
    edge_family: reconciliation_understanding
    evidence_basis: materialized inverse of HAS_RECONCILIATION_SIDE
    confidence: high
    canonical_cognee_edge: true
    logistics_only: true
    canonical_edge_type: BELONGS_TO_RECONCILIATION_PROFILE
    inverse_edge_type: HAS_RECONCILIATION_SIDE
    materialize_inverse: true
    edge_class: canonical
    source_type: reconciliation_side
    target_type: reconciliation_profile
    materialized_from: edge.reconciliation_profile.order_to_shipment.has_reconciliation_side.reconciliation_side.order_to_shipment.actual.0342fa18
    edge_properties:
      side_role: actual
```

```yaml
candidate_edge:
  edge_id: edge.reconciliation_profile.order_to_shipment.uses_matching_logic.matching_logic.order_to_shipment
  edge_type: USES_MATCHING_LOGIC
  source: reconciliation_profile.order_to_shipment
  target: matching_logic.order_to_shipment
  fields:
    edge_family: reconciliation_understanding
    evidence_basis: reconciliation_profile.fields.matching_logic
    confidence: high
    canonical_cognee_edge: true
    logistics_only: true
    canonical_edge_type: USES_MATCHING_LOGIC
    inverse_edge_type: SUPPORTS_RECONCILIATION_PROFILE
    materialize_inverse: true
    edge_class: canonical
    source_type: reconciliation_profile
    target_type: matching_logic
```

```yaml
candidate_edge:
  edge_id: edge.matching_logic.order_to_shipment.supports_reconciliation_profile.reconciliation_profile.order_to_shipment
  edge_type: SUPPORTS_RECONCILIATION_PROFILE
  source: matching_logic.order_to_shipment
  target: reconciliation_profile.order_to_shipment
  fields:
    edge_family: reconciliation_understanding
    evidence_basis: materialized inverse of USES_MATCHING_LOGIC
    confidence: high
    canonical_cognee_edge: true
    logistics_only: true
    canonical_edge_type: SUPPORTS_RECONCILIATION_PROFILE
    inverse_edge_type: USES_MATCHING_LOGIC
    materialize_inverse: true
    edge_class: canonical
    source_type: matching_logic
    target_type: reconciliation_profile
    materialized_from: edge.reconciliation_profile.order_to_shipment.uses_matching_logic.matching_logic.order_to_shipment
```

```yaml
candidate_edge:
  edge_id: edge.reconciliation_profile.order_to_shipment.has_mismatch_category.mismatch_category.order_to_shipment.missing_expected
  edge_type: HAS_MISMATCH_CATEGORY
  source: reconciliation_profile.order_to_shipment
  target: mismatch_category.order_to_shipment.missing_expected
  fields:
    edge_family: reconciliation_understanding
    evidence_basis: reconciliation_profile.fields.mismatch_categories
    confidence: high
    canonical_cognee_edge: true
    logistics_only: true
    canonical_edge_type: HAS_MISMATCH_CATEGORY
    inverse_edge_type: MISMATCH_OF_PROFILE
    materialize_inverse: false
    edge_class: canonical
    source_type: reconciliation_profile
    target_type: mismatch_category
```

```yaml
candidate_edge:
  edge_id: edge.reconciliation_profile.order_to_shipment.has_mismatch_category.mismatch_category.order_to_shipment.missing_actual
  edge_type: HAS_MISMATCH_CATEGORY
  source: reconciliation_profile.order_to_shipment
  target: mismatch_category.order_to_shipment.missing_actual
  fields:
    edge_family: reconciliation_understanding
    evidence_basis: reconciliation_profile.fields.mismatch_categories
    confidence: high
    canonical_cognee_edge: true
    logistics_only: true
    canonical_edge_type: HAS_MISMATCH_CATEGORY
    inverse_edge_type: MISMATCH_OF_PROFILE
    materialize_inverse: false
    edge_class: canonical
    source_type: reconciliation_profile
    target_type: mismatch_category
```

```yaml
candidate_edge:
  edge_id: edge.reconciliation_profile.order_to_shipment.has_mismatch_category.mismatch_category.order_to_shipment.amount_mismatch
  edge_type: HAS_MISMATCH_CATEGORY
  source: reconciliation_profile.order_to_shipment
  target: mismatch_category.order_to_shipment.amount_mismatch
  fields:
    edge_family: reconciliation_understanding
    evidence_basis: reconciliation_profile.fields.mismatch_categories
    confidence: high
    canonical_cognee_edge: true
    logistics_only: true
    canonical_edge_type: HAS_MISMATCH_CATEGORY
    inverse_edge_type: MISMATCH_OF_PROFILE
    materialize_inverse: false
    edge_class: canonical
    source_type: reconciliation_profile
    target_type: mismatch_category
```

```yaml
candidate_edge:
  edge_id: edge.reconciliation_profile.order_to_shipment.has_mismatch_category.mismatch_category.order_to_shipment.timing_mismatch
  edge_type: HAS_MISMATCH_CATEGORY
  source: reconciliation_profile.order_to_shipment
  target: mismatch_category.order_to_shipment.timing_mismatch
  fields:
    edge_family: reconciliation_understanding
    evidence_basis: reconciliation_profile.fields.mismatch_categories
    confidence: high
    canonical_cognee_edge: true
    logistics_only: true
    canonical_edge_type: HAS_MISMATCH_CATEGORY
    inverse_edge_type: MISMATCH_OF_PROFILE
    materialize_inverse: false
    edge_class: canonical
    source_type: reconciliation_profile
    target_type: mismatch_category
```

```yaml
candidate_edge:
  edge_id: edge.business_process.shipment_to_freight_invoice.has_reconciliation_profile.reconciliation_profile.shipment_to_freight_invoice
  edge_type: HAS_RECONCILIATION_PROFILE
  source: business_process.shipment_to_freight_invoice
  target: reconciliation_profile.shipment_to_freight_invoice
  fields:
    edge_family: reconciliation_understanding
    evidence_basis: reconciliation_profile.fields.business_process_id
    confidence: high
    canonical_cognee_edge: true
    logistics_only: true
    canonical_edge_type: HAS_RECONCILIATION_PROFILE
    inverse_edge_type: SUPPORTS_PROCESS
    materialize_inverse: true
    edge_class: canonical
    source_type: business_process
    target_type: reconciliation_profile
```

```yaml
candidate_edge:
  edge_id: edge.reconciliation_profile.shipment_to_freight_invoice.supports_process.business_process.shipment_to_freight_invoice
  edge_type: SUPPORTS_PROCESS
  source: reconciliation_profile.shipment_to_freight_invoice
  target: business_process.shipment_to_freight_invoice
  fields:
    edge_family: reconciliation_understanding
    evidence_basis: materialized inverse of HAS_RECONCILIATION_PROFILE
    confidence: high
    canonical_cognee_edge: true
    logistics_only: true
    canonical_edge_type: SUPPORTS_PROCESS
    inverse_edge_type: HAS_RECONCILIATION_PROFILE
    materialize_inverse: true
    edge_class: canonical
    source_type: reconciliation_profile
    target_type: business_process
    materialized_from: edge.business_process.shipment_to_freight_invoice.has_reconciliation_profile.reconciliation_profile.shipment_to_freight_invoice
```

```yaml
candidate_edge:
  edge_id: edge.reconciliation_profile.shipment_to_freight_invoice.has_reconciliation_side.reconciliation_side.shipment_to_freight_invoice.expected.5c1d27e4
  edge_type: HAS_RECONCILIATION_SIDE
  source: reconciliation_profile.shipment_to_freight_invoice
  target: reconciliation_side.shipment_to_freight_invoice.expected
  fields:
    edge_family: reconciliation_understanding
    evidence_basis: reconciliation_profile.fields.sides
    confidence: high
    canonical_cognee_edge: true
    logistics_only: true
    canonical_edge_type: HAS_RECONCILIATION_SIDE
    inverse_edge_type: BELONGS_TO_RECONCILIATION_PROFILE
    materialize_inverse: true
    edge_class: canonical
    source_type: reconciliation_profile
    target_type: reconciliation_side
    edge_properties:
      side_role: expected
```

```yaml
candidate_edge:
  edge_id: edge.reconciliation_side.shipment_to_freight_invoice.expected.belongs_to_reconciliation_profile.reconciliation_profile.shipment_to_freight_invoice.5c1d27e4
  edge_type: BELONGS_TO_RECONCILIATION_PROFILE
  source: reconciliation_side.shipment_to_freight_invoice.expected
  target: reconciliation_profile.shipment_to_freight_invoice
  fields:
    edge_family: reconciliation_understanding
    evidence_basis: materialized inverse of HAS_RECONCILIATION_SIDE
    confidence: high
    canonical_cognee_edge: true
    logistics_only: true
    canonical_edge_type: BELONGS_TO_RECONCILIATION_PROFILE
    inverse_edge_type: HAS_RECONCILIATION_SIDE
    materialize_inverse: true
    edge_class: canonical
    source_type: reconciliation_side
    target_type: reconciliation_profile
    materialized_from: edge.reconciliation_profile.shipment_to_freight_invoice.has_reconciliation_side.reconciliation_side.shipment_to_freight_invoice.expected.5c1d27e4
    edge_properties:
      side_role: expected
```

```yaml
candidate_edge:
  edge_id: edge.reconciliation_profile.shipment_to_freight_invoice.has_reconciliation_side.reconciliation_side.shipment_to_freight_invoice.actual.0342fa18
  edge_type: HAS_RECONCILIATION_SIDE
  source: reconciliation_profile.shipment_to_freight_invoice
  target: reconciliation_side.shipment_to_freight_invoice.actual
  fields:
    edge_family: reconciliation_understanding
    evidence_basis: reconciliation_profile.fields.sides
    confidence: high
    canonical_cognee_edge: true
    logistics_only: true
    canonical_edge_type: HAS_RECONCILIATION_SIDE
    inverse_edge_type: BELONGS_TO_RECONCILIATION_PROFILE
    materialize_inverse: true
    edge_class: canonical
    source_type: reconciliation_profile
    target_type: reconciliation_side
    edge_properties:
      side_role: actual
```

```yaml
candidate_edge:
  edge_id: edge.reconciliation_side.shipment_to_freight_invoice.actual.belongs_to_reconciliation_profile.reconciliation_profile.shipment_to_freight_invoice.0342fa18
  edge_type: BELONGS_TO_RECONCILIATION_PROFILE
  source: reconciliation_side.shipment_to_freight_invoice.actual
  target: reconciliation_profile.shipment_to_freight_invoice
  fields:
    edge_family: reconciliation_understanding
    evidence_basis: materialized inverse of HAS_RECONCILIATION_SIDE
    confidence: high
    canonical_cognee_edge: true
    logistics_only: true
    canonical_edge_type: BELONGS_TO_RECONCILIATION_PROFILE
    inverse_edge_type: HAS_RECONCILIATION_SIDE
    materialize_inverse: true
    edge_class: canonical
    source_type: reconciliation_side
    target_type: reconciliation_profile
    materialized_from: edge.reconciliation_profile.shipment_to_freight_invoice.has_reconciliation_side.reconciliation_side.shipment_to_freight_invoice.actual.0342fa18
    edge_properties:
      side_role: actual
```

```yaml
candidate_edge:
  edge_id: edge.reconciliation_profile.shipment_to_freight_invoice.uses_matching_logic.matching_logic.shipment_to_freight_invoice
  edge_type: USES_MATCHING_LOGIC
  source: reconciliation_profile.shipment_to_freight_invoice
  target: matching_logic.shipment_to_freight_invoice
  fields:
    edge_family: reconciliation_understanding
    evidence_basis: reconciliation_profile.fields.matching_logic
    confidence: high
    canonical_cognee_edge: true
    logistics_only: true
    canonical_edge_type: USES_MATCHING_LOGIC
    inverse_edge_type: SUPPORTS_RECONCILIATION_PROFILE
    materialize_inverse: true
    edge_class: canonical
    source_type: reconciliation_profile
    target_type: matching_logic
```

```yaml
candidate_edge:
  edge_id: edge.matching_logic.shipment_to_freight_invoice.supports_reconciliation_profile.reconciliation_profile.shipment_to_freight_invoice
  edge_type: SUPPORTS_RECONCILIATION_PROFILE
  source: matching_logic.shipment_to_freight_invoice
  target: reconciliation_profile.shipment_to_freight_invoice
  fields:
    edge_family: reconciliation_understanding
    evidence_basis: materialized inverse of USES_MATCHING_LOGIC
    confidence: high
    canonical_cognee_edge: true
    logistics_only: true
    canonical_edge_type: SUPPORTS_RECONCILIATION_PROFILE
    inverse_edge_type: USES_MATCHING_LOGIC
    materialize_inverse: true
    edge_class: canonical
    source_type: matching_logic
    target_type: reconciliation_profile
    materialized_from: edge.reconciliation_profile.shipment_to_freight_invoice.uses_matching_logic.matching_logic.shipment_to_freight_invoice
```

```yaml
candidate_edge:
  edge_id: edge.reconciliation_profile.shipment_to_freight_invoice.has_mismatch_category.mismatch_category.shipment_to_freight_invoice.missing_expected
  edge_type: HAS_MISMATCH_CATEGORY
  source: reconciliation_profile.shipment_to_freight_invoice
  target: mismatch_category.shipment_to_freight_invoice.missing_expected
  fields:
    edge_family: reconciliation_understanding
    evidence_basis: reconciliation_profile.fields.mismatch_categories
    confidence: high
    canonical_cognee_edge: true
    logistics_only: true
    canonical_edge_type: HAS_MISMATCH_CATEGORY
    inverse_edge_type: MISMATCH_OF_PROFILE
    materialize_inverse: false
    edge_class: canonical
    source_type: reconciliation_profile
    target_type: mismatch_category
```

```yaml
candidate_edge:
  edge_id: edge.reconciliation_profile.shipment_to_freight_invoice.has_mismatch_category.mismatch_category.shipment_to_freight_invoice.missing_actual
  edge_type: HAS_MISMATCH_CATEGORY
  source: reconciliation_profile.shipment_to_freight_invoice
  target: mismatch_category.shipment_to_freight_invoice.missing_actual
  fields:
    edge_family: reconciliation_understanding
    evidence_basis: reconciliation_profile.fields.mismatch_categories
    confidence: high
    canonical_cognee_edge: true
    logistics_only: true
    canonical_edge_type: HAS_MISMATCH_CATEGORY
    inverse_edge_type: MISMATCH_OF_PROFILE
    materialize_inverse: false
    edge_class: canonical
    source_type: reconciliation_profile
    target_type: mismatch_category
```

```yaml
candidate_edge:
  edge_id: edge.reconciliation_profile.shipment_to_freight_invoice.has_mismatch_category.mismatch_category.shipment_to_freight_invoice.amount_mismatch
  edge_type: HAS_MISMATCH_CATEGORY
  source: reconciliation_profile.shipment_to_freight_invoice
  target: mismatch_category.shipment_to_freight_invoice.amount_mismatch
  fields:
    edge_family: reconciliation_understanding
    evidence_basis: reconciliation_profile.fields.mismatch_categories
    confidence: high
    canonical_cognee_edge: true
    logistics_only: true
    canonical_edge_type: HAS_MISMATCH_CATEGORY
    inverse_edge_type: MISMATCH_OF_PROFILE
    materialize_inverse: false
    edge_class: canonical
    source_type: reconciliation_profile
    target_type: mismatch_category
```

```yaml
candidate_edge:
  edge_id: edge.reconciliation_profile.shipment_to_freight_invoice.has_mismatch_category.mismatch_category.shipment_to_freight_invoice.timing_mismatch
  edge_type: HAS_MISMATCH_CATEGORY
  source: reconciliation_profile.shipment_to_freight_invoice
  target: mismatch_category.shipment_to_freight_invoice.timing_mismatch
  fields:
    edge_family: reconciliation_understanding
    evidence_basis: reconciliation_profile.fields.mismatch_categories
    confidence: high
    canonical_cognee_edge: true
    logistics_only: true
    canonical_edge_type: HAS_MISMATCH_CATEGORY
    inverse_edge_type: MISMATCH_OF_PROFILE
    materialize_inverse: false
    edge_class: canonical
    source_type: reconciliation_profile
    target_type: mismatch_category
```

```yaml
candidate_edge:
  edge_id: edge.business_process.freight_charge_validation.has_reconciliation_profile.reconciliation_profile.freight_charge_validation
  edge_type: HAS_RECONCILIATION_PROFILE
  source: business_process.freight_charge_validation
  target: reconciliation_profile.freight_charge_validation
  fields:
    edge_family: reconciliation_understanding
    evidence_basis: reconciliation_profile.fields.business_process_id
    confidence: high
    canonical_cognee_edge: true
    logistics_only: true
    canonical_edge_type: HAS_RECONCILIATION_PROFILE
    inverse_edge_type: SUPPORTS_PROCESS
    materialize_inverse: true
    edge_class: canonical
    source_type: business_process
    target_type: reconciliation_profile
```

```yaml
candidate_edge:
  edge_id: edge.reconciliation_profile.freight_charge_validation.supports_process.business_process.freight_charge_validation
  edge_type: SUPPORTS_PROCESS
  source: reconciliation_profile.freight_charge_validation
  target: business_process.freight_charge_validation
  fields:
    edge_family: reconciliation_understanding
    evidence_basis: materialized inverse of HAS_RECONCILIATION_PROFILE
    confidence: high
    canonical_cognee_edge: true
    logistics_only: true
    canonical_edge_type: SUPPORTS_PROCESS
    inverse_edge_type: HAS_RECONCILIATION_PROFILE
    materialize_inverse: true
    edge_class: canonical
    source_type: reconciliation_profile
    target_type: business_process
    materialized_from: edge.business_process.freight_charge_validation.has_reconciliation_profile.reconciliation_profile.freight_charge_validation
```

```yaml
candidate_edge:
  edge_id: edge.reconciliation_profile.freight_charge_validation.has_reconciliation_side.reconciliation_side.freight_charge_validation.expected.5c1d27e4
  edge_type: HAS_RECONCILIATION_SIDE
  source: reconciliation_profile.freight_charge_validation
  target: reconciliation_side.freight_charge_validation.expected
  fields:
    edge_family: reconciliation_understanding
    evidence_basis: reconciliation_profile.fields.sides
    confidence: high
    canonical_cognee_edge: true
    logistics_only: true
    canonical_edge_type: HAS_RECONCILIATION_SIDE
    inverse_edge_type: BELONGS_TO_RECONCILIATION_PROFILE
    materialize_inverse: true
    edge_class: canonical
    source_type: reconciliation_profile
    target_type: reconciliation_side
    edge_properties:
      side_role: expected
```

```yaml
candidate_edge:
  edge_id: edge.reconciliation_side.freight_charge_validation.expected.belongs_to_reconciliation_profile.reconciliation_profile.freight_charge_validation.5c1d27e4
  edge_type: BELONGS_TO_RECONCILIATION_PROFILE
  source: reconciliation_side.freight_charge_validation.expected
  target: reconciliation_profile.freight_charge_validation
  fields:
    edge_family: reconciliation_understanding
    evidence_basis: materialized inverse of HAS_RECONCILIATION_SIDE
    confidence: high
    canonical_cognee_edge: true
    logistics_only: true
    canonical_edge_type: BELONGS_TO_RECONCILIATION_PROFILE
    inverse_edge_type: HAS_RECONCILIATION_SIDE
    materialize_inverse: true
    edge_class: canonical
    source_type: reconciliation_side
    target_type: reconciliation_profile
    materialized_from: edge.reconciliation_profile.freight_charge_validation.has_reconciliation_side.reconciliation_side.freight_charge_validation.expected.5c1d27e4
    edge_properties:
      side_role: expected
```

```yaml
candidate_edge:
  edge_id: edge.reconciliation_profile.freight_charge_validation.has_reconciliation_side.reconciliation_side.freight_charge_validation.actual.0342fa18
  edge_type: HAS_RECONCILIATION_SIDE
  source: reconciliation_profile.freight_charge_validation
  target: reconciliation_side.freight_charge_validation.actual
  fields:
    edge_family: reconciliation_understanding
    evidence_basis: reconciliation_profile.fields.sides
    confidence: high
    canonical_cognee_edge: true
    logistics_only: true
    canonical_edge_type: HAS_RECONCILIATION_SIDE
    inverse_edge_type: BELONGS_TO_RECONCILIATION_PROFILE
    materialize_inverse: true
    edge_class: canonical
    source_type: reconciliation_profile
    target_type: reconciliation_side
    edge_properties:
      side_role: actual
```

```yaml
candidate_edge:
  edge_id: edge.reconciliation_side.freight_charge_validation.actual.belongs_to_reconciliation_profile.reconciliation_profile.freight_charge_validation.0342fa18
  edge_type: BELONGS_TO_RECONCILIATION_PROFILE
  source: reconciliation_side.freight_charge_validation.actual
  target: reconciliation_profile.freight_charge_validation
  fields:
    edge_family: reconciliation_understanding
    evidence_basis: materialized inverse of HAS_RECONCILIATION_SIDE
    confidence: high
    canonical_cognee_edge: true
    logistics_only: true
    canonical_edge_type: BELONGS_TO_RECONCILIATION_PROFILE
    inverse_edge_type: HAS_RECONCILIATION_SIDE
    materialize_inverse: true
    edge_class: canonical
    source_type: reconciliation_side
    target_type: reconciliation_profile
    materialized_from: edge.reconciliation_profile.freight_charge_validation.has_reconciliation_side.reconciliation_side.freight_charge_validation.actual.0342fa18
    edge_properties:
      side_role: actual
```

```yaml
candidate_edge:
  edge_id: edge.reconciliation_profile.freight_charge_validation.uses_matching_logic.matching_logic.freight_charge_validation
  edge_type: USES_MATCHING_LOGIC
  source: reconciliation_profile.freight_charge_validation
  target: matching_logic.freight_charge_validation
  fields:
    edge_family: reconciliation_understanding
    evidence_basis: reconciliation_profile.fields.matching_logic
    confidence: high
    canonical_cognee_edge: true
    logistics_only: true
    canonical_edge_type: USES_MATCHING_LOGIC
    inverse_edge_type: SUPPORTS_RECONCILIATION_PROFILE
    materialize_inverse: true
    edge_class: canonical
    source_type: reconciliation_profile
    target_type: matching_logic
```

```yaml
candidate_edge:
  edge_id: edge.matching_logic.freight_charge_validation.supports_reconciliation_profile.reconciliation_profile.freight_charge_validation
  edge_type: SUPPORTS_RECONCILIATION_PROFILE
  source: matching_logic.freight_charge_validation
  target: reconciliation_profile.freight_charge_validation
  fields:
    edge_family: reconciliation_understanding
    evidence_basis: materialized inverse of USES_MATCHING_LOGIC
    confidence: high
    canonical_cognee_edge: true
    logistics_only: true
    canonical_edge_type: SUPPORTS_RECONCILIATION_PROFILE
    inverse_edge_type: USES_MATCHING_LOGIC
    materialize_inverse: true
    edge_class: canonical
    source_type: matching_logic
    target_type: reconciliation_profile
    materialized_from: edge.reconciliation_profile.freight_charge_validation.uses_matching_logic.matching_logic.freight_charge_validation
```

```yaml
candidate_edge:
  edge_id: edge.reconciliation_profile.freight_charge_validation.has_mismatch_category.mismatch_category.freight_charge_validation.missing_expected
  edge_type: HAS_MISMATCH_CATEGORY
  source: reconciliation_profile.freight_charge_validation
  target: mismatch_category.freight_charge_validation.missing_expected
  fields:
    edge_family: reconciliation_understanding
    evidence_basis: reconciliation_profile.fields.mismatch_categories
    confidence: high
    canonical_cognee_edge: true
    logistics_only: true
    canonical_edge_type: HAS_MISMATCH_CATEGORY
    inverse_edge_type: MISMATCH_OF_PROFILE
    materialize_inverse: false
    edge_class: canonical
    source_type: reconciliation_profile
    target_type: mismatch_category
```

```yaml
candidate_edge:
  edge_id: edge.reconciliation_profile.freight_charge_validation.has_mismatch_category.mismatch_category.freight_charge_validation.missing_actual
  edge_type: HAS_MISMATCH_CATEGORY
  source: reconciliation_profile.freight_charge_validation
  target: mismatch_category.freight_charge_validation.missing_actual
  fields:
    edge_family: reconciliation_understanding
    evidence_basis: reconciliation_profile.fields.mismatch_categories
    confidence: high
    canonical_cognee_edge: true
    logistics_only: true
    canonical_edge_type: HAS_MISMATCH_CATEGORY
    inverse_edge_type: MISMATCH_OF_PROFILE
    materialize_inverse: false
    edge_class: canonical
    source_type: reconciliation_profile
    target_type: mismatch_category
```

```yaml
candidate_edge:
  edge_id: edge.reconciliation_profile.freight_charge_validation.has_mismatch_category.mismatch_category.freight_charge_validation.amount_mismatch
  edge_type: HAS_MISMATCH_CATEGORY
  source: reconciliation_profile.freight_charge_validation
  target: mismatch_category.freight_charge_validation.amount_mismatch
  fields:
    edge_family: reconciliation_understanding
    evidence_basis: reconciliation_profile.fields.mismatch_categories
    confidence: high
    canonical_cognee_edge: true
    logistics_only: true
    canonical_edge_type: HAS_MISMATCH_CATEGORY
    inverse_edge_type: MISMATCH_OF_PROFILE
    materialize_inverse: false
    edge_class: canonical
    source_type: reconciliation_profile
    target_type: mismatch_category
```

```yaml
candidate_edge:
  edge_id: edge.reconciliation_profile.freight_charge_validation.has_mismatch_category.mismatch_category.freight_charge_validation.timing_mismatch
  edge_type: HAS_MISMATCH_CATEGORY
  source: reconciliation_profile.freight_charge_validation
  target: mismatch_category.freight_charge_validation.timing_mismatch
  fields:
    edge_family: reconciliation_understanding
    evidence_basis: reconciliation_profile.fields.mismatch_categories
    confidence: high
    canonical_cognee_edge: true
    logistics_only: true
    canonical_edge_type: HAS_MISMATCH_CATEGORY
    inverse_edge_type: MISMATCH_OF_PROFILE
    materialize_inverse: false
    edge_class: canonical
    source_type: reconciliation_profile
    target_type: mismatch_category
```

```yaml
candidate_edge:
  edge_id: edge.business_process.cod_delivery_to_courier_remittance.has_reconciliation_profile.reconciliation_profile.cod_expected_to_courier_remittance
  edge_type: HAS_RECONCILIATION_PROFILE
  source: business_process.cod_delivery_to_courier_remittance
  target: reconciliation_profile.cod_expected_to_courier_remittance
  fields:
    edge_family: reconciliation_understanding
    evidence_basis: reconciliation_profile.fields.business_process_id
    confidence: high
    canonical_cognee_edge: true
    logistics_only: true
    canonical_edge_type: HAS_RECONCILIATION_PROFILE
    inverse_edge_type: SUPPORTS_PROCESS
    materialize_inverse: true
    edge_class: canonical
    source_type: business_process
    target_type: reconciliation_profile
```

```yaml
candidate_edge:
  edge_id: edge.reconciliation_profile.cod_expected_to_courier_remittance.supports_process.business_process.cod_delivery_to_courier_remittance
  edge_type: SUPPORTS_PROCESS
  source: reconciliation_profile.cod_expected_to_courier_remittance
  target: business_process.cod_delivery_to_courier_remittance
  fields:
    edge_family: reconciliation_understanding
    evidence_basis: materialized inverse of HAS_RECONCILIATION_PROFILE
    confidence: high
    canonical_cognee_edge: true
    logistics_only: true
    canonical_edge_type: SUPPORTS_PROCESS
    inverse_edge_type: HAS_RECONCILIATION_PROFILE
    materialize_inverse: true
    edge_class: canonical
    source_type: reconciliation_profile
    target_type: business_process
    materialized_from: edge.business_process.cod_delivery_to_courier_remittance.has_reconciliation_profile.reconciliation_profile.cod_expected_to_courier_remittance
```

```yaml
candidate_edge:
  edge_id: edge.reconciliation_profile.cod_expected_to_courier_remittance.has_reconciliation_side.reconciliation_side.cod_expected_to_courier_remittance.expected.5c1d27e4
  edge_type: HAS_RECONCILIATION_SIDE
  source: reconciliation_profile.cod_expected_to_courier_remittance
  target: reconciliation_side.cod_expected_to_courier_remittance.expected
  fields:
    edge_family: reconciliation_understanding
    evidence_basis: reconciliation_profile.fields.sides
    confidence: high
    canonical_cognee_edge: true
    logistics_only: true
    canonical_edge_type: HAS_RECONCILIATION_SIDE
    inverse_edge_type: BELONGS_TO_RECONCILIATION_PROFILE
    materialize_inverse: true
    edge_class: canonical
    source_type: reconciliation_profile
    target_type: reconciliation_side
    edge_properties:
      side_role: expected
```

```yaml
candidate_edge:
  edge_id: edge.reconciliation_side.cod_expected_to_courier_remittance.expected.belongs_to_reconciliation_profile.reconciliation_profile.cod_expected_to_courier_remittance.5c1d27e4
  edge_type: BELONGS_TO_RECONCILIATION_PROFILE
  source: reconciliation_side.cod_expected_to_courier_remittance.expected
  target: reconciliation_profile.cod_expected_to_courier_remittance
  fields:
    edge_family: reconciliation_understanding
    evidence_basis: materialized inverse of HAS_RECONCILIATION_SIDE
    confidence: high
    canonical_cognee_edge: true
    logistics_only: true
    canonical_edge_type: BELONGS_TO_RECONCILIATION_PROFILE
    inverse_edge_type: HAS_RECONCILIATION_SIDE
    materialize_inverse: true
    edge_class: canonical
    source_type: reconciliation_side
    target_type: reconciliation_profile
    materialized_from: edge.reconciliation_profile.cod_expected_to_courier_remittance.has_reconciliation_side.reconciliation_side.cod_expected_to_courier_remittance.expected.5c1d27e4
    edge_properties:
      side_role: expected
```

```yaml
candidate_edge:
  edge_id: edge.reconciliation_profile.cod_expected_to_courier_remittance.has_reconciliation_side.reconciliation_side.cod_expected_to_courier_remittance.actual.5c1d27e4
  edge_type: HAS_RECONCILIATION_SIDE
  source: reconciliation_profile.cod_expected_to_courier_remittance
  target: reconciliation_side.cod_expected_to_courier_remittance.actual
  fields:
    edge_family: reconciliation_understanding
    evidence_basis: reconciliation_profile.fields.sides
    confidence: high
    canonical_cognee_edge: true
    logistics_only: true
    canonical_edge_type: HAS_RECONCILIATION_SIDE
    inverse_edge_type: BELONGS_TO_RECONCILIATION_PROFILE
    materialize_inverse: true
    edge_class: canonical
    source_type: reconciliation_profile
    target_type: reconciliation_side
    edge_properties:
      side_role: expected
```

```yaml
candidate_edge:
  edge_id: edge.reconciliation_side.cod_expected_to_courier_remittance.actual.belongs_to_reconciliation_profile.reconciliation_profile.cod_expected_to_courier_remittance.5c1d27e4
  edge_type: BELONGS_TO_RECONCILIATION_PROFILE
  source: reconciliation_side.cod_expected_to_courier_remittance.actual
  target: reconciliation_profile.cod_expected_to_courier_remittance
  fields:
    edge_family: reconciliation_understanding
    evidence_basis: materialized inverse of HAS_RECONCILIATION_SIDE
    confidence: high
    canonical_cognee_edge: true
    logistics_only: true
    canonical_edge_type: BELONGS_TO_RECONCILIATION_PROFILE
    inverse_edge_type: HAS_RECONCILIATION_SIDE
    materialize_inverse: true
    edge_class: canonical
    source_type: reconciliation_side
    target_type: reconciliation_profile
    materialized_from: edge.reconciliation_profile.cod_expected_to_courier_remittance.has_reconciliation_side.reconciliation_side.cod_expected_to_courier_remittance.actual.5c1d27e4
    edge_properties:
      side_role: expected
```

```yaml
candidate_edge:
  edge_id: edge.reconciliation_profile.cod_expected_to_courier_remittance.uses_matching_logic.matching_logic.cod_expected_to_courier_remittance
  edge_type: USES_MATCHING_LOGIC
  source: reconciliation_profile.cod_expected_to_courier_remittance
  target: matching_logic.cod_expected_to_courier_remittance
  fields:
    edge_family: reconciliation_understanding
    evidence_basis: reconciliation_profile.fields.matching_logic
    confidence: high
    canonical_cognee_edge: true
    logistics_only: true
    canonical_edge_type: USES_MATCHING_LOGIC
    inverse_edge_type: SUPPORTS_RECONCILIATION_PROFILE
    materialize_inverse: true
    edge_class: canonical
    source_type: reconciliation_profile
    target_type: matching_logic
```

```yaml
candidate_edge:
  edge_id: edge.matching_logic.cod_expected_to_courier_remittance.supports_reconciliation_profile.reconciliation_profile.cod_expected_to_courier_remittance
  edge_type: SUPPORTS_RECONCILIATION_PROFILE
  source: matching_logic.cod_expected_to_courier_remittance
  target: reconciliation_profile.cod_expected_to_courier_remittance
  fields:
    edge_family: reconciliation_understanding
    evidence_basis: materialized inverse of USES_MATCHING_LOGIC
    confidence: high
    canonical_cognee_edge: true
    logistics_only: true
    canonical_edge_type: SUPPORTS_RECONCILIATION_PROFILE
    inverse_edge_type: USES_MATCHING_LOGIC
    materialize_inverse: true
    edge_class: canonical
    source_type: matching_logic
    target_type: reconciliation_profile
    materialized_from: edge.reconciliation_profile.cod_expected_to_courier_remittance.uses_matching_logic.matching_logic.cod_expected_to_courier_remittance
```

```yaml
candidate_edge:
  edge_id: edge.reconciliation_profile.cod_expected_to_courier_remittance.has_mismatch_category.mismatch_category.cod_expected_to_courier_remittance.missing_expected
  edge_type: HAS_MISMATCH_CATEGORY
  source: reconciliation_profile.cod_expected_to_courier_remittance
  target: mismatch_category.cod_expected_to_courier_remittance.missing_expected
  fields:
    edge_family: reconciliation_understanding
    evidence_basis: reconciliation_profile.fields.mismatch_categories
    confidence: high
    canonical_cognee_edge: true
    logistics_only: true
    canonical_edge_type: HAS_MISMATCH_CATEGORY
    inverse_edge_type: MISMATCH_OF_PROFILE
    materialize_inverse: false
    edge_class: canonical
    source_type: reconciliation_profile
    target_type: mismatch_category
```

```yaml
candidate_edge:
  edge_id: edge.reconciliation_profile.cod_expected_to_courier_remittance.has_mismatch_category.mismatch_category.cod_expected_to_courier_remittance.missing_actual
  edge_type: HAS_MISMATCH_CATEGORY
  source: reconciliation_profile.cod_expected_to_courier_remittance
  target: mismatch_category.cod_expected_to_courier_remittance.missing_actual
  fields:
    edge_family: reconciliation_understanding
    evidence_basis: reconciliation_profile.fields.mismatch_categories
    confidence: high
    canonical_cognee_edge: true
    logistics_only: true
    canonical_edge_type: HAS_MISMATCH_CATEGORY
    inverse_edge_type: MISMATCH_OF_PROFILE
    materialize_inverse: false
    edge_class: canonical
    source_type: reconciliation_profile
    target_type: mismatch_category
```

```yaml
candidate_edge:
  edge_id: edge.reconciliation_profile.cod_expected_to_courier_remittance.has_mismatch_category.mismatch_category.cod_expected_to_courier_remittance.amount_mismatch
  edge_type: HAS_MISMATCH_CATEGORY
  source: reconciliation_profile.cod_expected_to_courier_remittance
  target: mismatch_category.cod_expected_to_courier_remittance.amount_mismatch
  fields:
    edge_family: reconciliation_understanding
    evidence_basis: reconciliation_profile.fields.mismatch_categories
    confidence: high
    canonical_cognee_edge: true
    logistics_only: true
    canonical_edge_type: HAS_MISMATCH_CATEGORY
    inverse_edge_type: MISMATCH_OF_PROFILE
    materialize_inverse: false
    edge_class: canonical
    source_type: reconciliation_profile
    target_type: mismatch_category
```

```yaml
candidate_edge:
  edge_id: edge.reconciliation_profile.cod_expected_to_courier_remittance.has_mismatch_category.mismatch_category.cod_expected_to_courier_remittance.timing_mismatch
  edge_type: HAS_MISMATCH_CATEGORY
  source: reconciliation_profile.cod_expected_to_courier_remittance
  target: mismatch_category.cod_expected_to_courier_remittance.timing_mismatch
  fields:
    edge_family: reconciliation_understanding
    evidence_basis: reconciliation_profile.fields.mismatch_categories
    confidence: high
    canonical_cognee_edge: true
    logistics_only: true
    canonical_edge_type: HAS_MISMATCH_CATEGORY
    inverse_edge_type: MISMATCH_OF_PROFILE
    materialize_inverse: false
    edge_class: canonical
    source_type: reconciliation_profile
    target_type: mismatch_category
```

```yaml
candidate_edge:
  edge_id: edge.business_process.courier_batch_to_bank_reconciliation.has_reconciliation_profile.reconciliation_profile.courier_batch_to_bank_credit
  edge_type: HAS_RECONCILIATION_PROFILE
  source: business_process.courier_batch_to_bank_reconciliation
  target: reconciliation_profile.courier_batch_to_bank_credit
  fields:
    edge_family: reconciliation_understanding
    evidence_basis: reconciliation_profile.fields.business_process_id
    confidence: high
    canonical_cognee_edge: true
    logistics_only: true
    canonical_edge_type: HAS_RECONCILIATION_PROFILE
    inverse_edge_type: SUPPORTS_PROCESS
    materialize_inverse: true
    edge_class: canonical
    source_type: business_process
    target_type: reconciliation_profile
```

```yaml
candidate_edge:
  edge_id: edge.reconciliation_profile.courier_batch_to_bank_credit.supports_process.business_process.courier_batch_to_bank_reconciliation
  edge_type: SUPPORTS_PROCESS
  source: reconciliation_profile.courier_batch_to_bank_credit
  target: business_process.courier_batch_to_bank_reconciliation
  fields:
    edge_family: reconciliation_understanding
    evidence_basis: materialized inverse of HAS_RECONCILIATION_PROFILE
    confidence: high
    canonical_cognee_edge: true
    logistics_only: true
    canonical_edge_type: SUPPORTS_PROCESS
    inverse_edge_type: HAS_RECONCILIATION_PROFILE
    materialize_inverse: true
    edge_class: canonical
    source_type: reconciliation_profile
    target_type: business_process
    materialized_from: edge.business_process.courier_batch_to_bank_reconciliation.has_reconciliation_profile.reconciliation_profile.courier_batch_to_bank_credit
```

```yaml
candidate_edge:
  edge_id: edge.reconciliation_profile.courier_batch_to_bank_credit.has_reconciliation_side.reconciliation_side.courier_batch_to_bank_credit.expected.5c1d27e4
  edge_type: HAS_RECONCILIATION_SIDE
  source: reconciliation_profile.courier_batch_to_bank_credit
  target: reconciliation_side.courier_batch_to_bank_credit.expected
  fields:
    edge_family: reconciliation_understanding
    evidence_basis: reconciliation_profile.fields.sides
    confidence: high
    canonical_cognee_edge: true
    logistics_only: true
    canonical_edge_type: HAS_RECONCILIATION_SIDE
    inverse_edge_type: BELONGS_TO_RECONCILIATION_PROFILE
    materialize_inverse: true
    edge_class: canonical
    source_type: reconciliation_profile
    target_type: reconciliation_side
    edge_properties:
      side_role: expected
```

```yaml
candidate_edge:
  edge_id: edge.reconciliation_side.courier_batch_to_bank_credit.expected.belongs_to_reconciliation_profile.reconciliation_profile.courier_batch_to_bank_credit.5c1d27e4
  edge_type: BELONGS_TO_RECONCILIATION_PROFILE
  source: reconciliation_side.courier_batch_to_bank_credit.expected
  target: reconciliation_profile.courier_batch_to_bank_credit
  fields:
    edge_family: reconciliation_understanding
    evidence_basis: materialized inverse of HAS_RECONCILIATION_SIDE
    confidence: high
    canonical_cognee_edge: true
    logistics_only: true
    canonical_edge_type: BELONGS_TO_RECONCILIATION_PROFILE
    inverse_edge_type: HAS_RECONCILIATION_SIDE
    materialize_inverse: true
    edge_class: canonical
    source_type: reconciliation_side
    target_type: reconciliation_profile
    materialized_from: edge.reconciliation_profile.courier_batch_to_bank_credit.has_reconciliation_side.reconciliation_side.courier_batch_to_bank_credit.expected.5c1d27e4
    edge_properties:
      side_role: expected
```

```yaml
candidate_edge:
  edge_id: edge.reconciliation_profile.courier_batch_to_bank_credit.has_reconciliation_side.reconciliation_side.courier_batch_to_bank_credit.actual.0342fa18
  edge_type: HAS_RECONCILIATION_SIDE
  source: reconciliation_profile.courier_batch_to_bank_credit
  target: reconciliation_side.courier_batch_to_bank_credit.actual
  fields:
    edge_family: reconciliation_understanding
    evidence_basis: reconciliation_profile.fields.sides
    confidence: high
    canonical_cognee_edge: true
    logistics_only: true
    canonical_edge_type: HAS_RECONCILIATION_SIDE
    inverse_edge_type: BELONGS_TO_RECONCILIATION_PROFILE
    materialize_inverse: true
    edge_class: canonical
    source_type: reconciliation_profile
    target_type: reconciliation_side
    edge_properties:
      side_role: actual
```

```yaml
candidate_edge:
  edge_id: edge.reconciliation_side.courier_batch_to_bank_credit.actual.belongs_to_reconciliation_profile.reconciliation_profile.courier_batch_to_bank_credit.0342fa18
  edge_type: BELONGS_TO_RECONCILIATION_PROFILE
  source: reconciliation_side.courier_batch_to_bank_credit.actual
  target: reconciliation_profile.courier_batch_to_bank_credit
  fields:
    edge_family: reconciliation_understanding
    evidence_basis: materialized inverse of HAS_RECONCILIATION_SIDE
    confidence: high
    canonical_cognee_edge: true
    logistics_only: true
    canonical_edge_type: BELONGS_TO_RECONCILIATION_PROFILE
    inverse_edge_type: HAS_RECONCILIATION_SIDE
    materialize_inverse: true
    edge_class: canonical
    source_type: reconciliation_side
    target_type: reconciliation_profile
    materialized_from: edge.reconciliation_profile.courier_batch_to_bank_credit.has_reconciliation_side.reconciliation_side.courier_batch_to_bank_credit.actual.0342fa18
    edge_properties:
      side_role: actual
```

```yaml
candidate_edge:
  edge_id: edge.reconciliation_profile.courier_batch_to_bank_credit.uses_matching_logic.matching_logic.courier_batch_to_bank_credit
  edge_type: USES_MATCHING_LOGIC
  source: reconciliation_profile.courier_batch_to_bank_credit
  target: matching_logic.courier_batch_to_bank_credit
  fields:
    edge_family: reconciliation_understanding
    evidence_basis: reconciliation_profile.fields.matching_logic
    confidence: high
    canonical_cognee_edge: true
    logistics_only: true
    canonical_edge_type: USES_MATCHING_LOGIC
    inverse_edge_type: SUPPORTS_RECONCILIATION_PROFILE
    materialize_inverse: true
    edge_class: canonical
    source_type: reconciliation_profile
    target_type: matching_logic
```

```yaml
candidate_edge:
  edge_id: edge.matching_logic.courier_batch_to_bank_credit.supports_reconciliation_profile.reconciliation_profile.courier_batch_to_bank_credit
  edge_type: SUPPORTS_RECONCILIATION_PROFILE
  source: matching_logic.courier_batch_to_bank_credit
  target: reconciliation_profile.courier_batch_to_bank_credit
  fields:
    edge_family: reconciliation_understanding
    evidence_basis: materialized inverse of USES_MATCHING_LOGIC
    confidence: high
    canonical_cognee_edge: true
    logistics_only: true
    canonical_edge_type: SUPPORTS_RECONCILIATION_PROFILE
    inverse_edge_type: USES_MATCHING_LOGIC
    materialize_inverse: true
    edge_class: canonical
    source_type: matching_logic
    target_type: reconciliation_profile
    materialized_from: edge.reconciliation_profile.courier_batch_to_bank_credit.uses_matching_logic.matching_logic.courier_batch_to_bank_credit
```

```yaml
candidate_edge:
  edge_id: edge.reconciliation_profile.courier_batch_to_bank_credit.has_mismatch_category.mismatch_category.courier_batch_to_bank_credit.missing_expected
  edge_type: HAS_MISMATCH_CATEGORY
  source: reconciliation_profile.courier_batch_to_bank_credit
  target: mismatch_category.courier_batch_to_bank_credit.missing_expected
  fields:
    edge_family: reconciliation_understanding
    evidence_basis: reconciliation_profile.fields.mismatch_categories
    confidence: high
    canonical_cognee_edge: true
    logistics_only: true
    canonical_edge_type: HAS_MISMATCH_CATEGORY
    inverse_edge_type: MISMATCH_OF_PROFILE
    materialize_inverse: false
    edge_class: canonical
    source_type: reconciliation_profile
    target_type: mismatch_category
```

```yaml
candidate_edge:
  edge_id: edge.reconciliation_profile.courier_batch_to_bank_credit.has_mismatch_category.mismatch_category.courier_batch_to_bank_credit.missing_actual
  edge_type: HAS_MISMATCH_CATEGORY
  source: reconciliation_profile.courier_batch_to_bank_credit
  target: mismatch_category.courier_batch_to_bank_credit.missing_actual
  fields:
    edge_family: reconciliation_understanding
    evidence_basis: reconciliation_profile.fields.mismatch_categories
    confidence: high
    canonical_cognee_edge: true
    logistics_only: true
    canonical_edge_type: HAS_MISMATCH_CATEGORY
    inverse_edge_type: MISMATCH_OF_PROFILE
    materialize_inverse: false
    edge_class: canonical
    source_type: reconciliation_profile
    target_type: mismatch_category
```

```yaml
candidate_edge:
  edge_id: edge.reconciliation_profile.courier_batch_to_bank_credit.has_mismatch_category.mismatch_category.courier_batch_to_bank_credit.amount_mismatch
  edge_type: HAS_MISMATCH_CATEGORY
  source: reconciliation_profile.courier_batch_to_bank_credit
  target: mismatch_category.courier_batch_to_bank_credit.amount_mismatch
  fields:
    edge_family: reconciliation_understanding
    evidence_basis: reconciliation_profile.fields.mismatch_categories
    confidence: high
    canonical_cognee_edge: true
    logistics_only: true
    canonical_edge_type: HAS_MISMATCH_CATEGORY
    inverse_edge_type: MISMATCH_OF_PROFILE
    materialize_inverse: false
    edge_class: canonical
    source_type: reconciliation_profile
    target_type: mismatch_category
```

```yaml
candidate_edge:
  edge_id: edge.reconciliation_profile.courier_batch_to_bank_credit.has_mismatch_category.mismatch_category.courier_batch_to_bank_credit.timing_mismatch
  edge_type: HAS_MISMATCH_CATEGORY
  source: reconciliation_profile.courier_batch_to_bank_credit
  target: mismatch_category.courier_batch_to_bank_credit.timing_mismatch
  fields:
    edge_family: reconciliation_understanding
    evidence_basis: reconciliation_profile.fields.mismatch_categories
    confidence: high
    canonical_cognee_edge: true
    logistics_only: true
    canonical_edge_type: HAS_MISMATCH_CATEGORY
    inverse_edge_type: MISMATCH_OF_PROFILE
    materialize_inverse: false
    edge_class: canonical
    source_type: reconciliation_profile
    target_type: mismatch_category
```

```yaml
candidate_edge:
  edge_id: edge.business_process.prepaid_pos_logistics_settlement.has_reconciliation_profile.reconciliation_profile.prepaid_pos_logistics_settlement
  edge_type: HAS_RECONCILIATION_PROFILE
  source: business_process.prepaid_pos_logistics_settlement
  target: reconciliation_profile.prepaid_pos_logistics_settlement
  fields:
    edge_family: reconciliation_understanding
    evidence_basis: reconciliation_profile.fields.business_process_id
    confidence: high
    canonical_cognee_edge: true
    logistics_only: true
    canonical_edge_type: HAS_RECONCILIATION_PROFILE
    inverse_edge_type: SUPPORTS_PROCESS
    materialize_inverse: true
    edge_class: canonical
    source_type: business_process
    target_type: reconciliation_profile
```

```yaml
candidate_edge:
  edge_id: edge.reconciliation_profile.prepaid_pos_logistics_settlement.supports_process.business_process.prepaid_pos_logistics_settlement
  edge_type: SUPPORTS_PROCESS
  source: reconciliation_profile.prepaid_pos_logistics_settlement
  target: business_process.prepaid_pos_logistics_settlement
  fields:
    edge_family: reconciliation_understanding
    evidence_basis: materialized inverse of HAS_RECONCILIATION_PROFILE
    confidence: high
    canonical_cognee_edge: true
    logistics_only: true
    canonical_edge_type: SUPPORTS_PROCESS
    inverse_edge_type: HAS_RECONCILIATION_PROFILE
    materialize_inverse: true
    edge_class: canonical
    source_type: reconciliation_profile
    target_type: business_process
    materialized_from: edge.business_process.prepaid_pos_logistics_settlement.has_reconciliation_profile.reconciliation_profile.prepaid_pos_logistics_settlement
```

```yaml
candidate_edge:
  edge_id: edge.reconciliation_profile.prepaid_pos_logistics_settlement.has_reconciliation_side.reconciliation_side.prepaid_pos_logistics_settlement.expected.5c1d27e4
  edge_type: HAS_RECONCILIATION_SIDE
  source: reconciliation_profile.prepaid_pos_logistics_settlement
  target: reconciliation_side.prepaid_pos_logistics_settlement.expected
  fields:
    edge_family: reconciliation_understanding
    evidence_basis: reconciliation_profile.fields.sides
    confidence: high
    canonical_cognee_edge: true
    logistics_only: true
    canonical_edge_type: HAS_RECONCILIATION_SIDE
    inverse_edge_type: BELONGS_TO_RECONCILIATION_PROFILE
    materialize_inverse: true
    edge_class: canonical
    source_type: reconciliation_profile
    target_type: reconciliation_side
    edge_properties:
      side_role: expected
```

```yaml
candidate_edge:
  edge_id: edge.reconciliation_side.prepaid_pos_logistics_settlement.expected.belongs_to_reconciliation_profile.reconciliation_profile.prepaid_pos_logistics_settlement.5c1d27e4
  edge_type: BELONGS_TO_RECONCILIATION_PROFILE
  source: reconciliation_side.prepaid_pos_logistics_settlement.expected
  target: reconciliation_profile.prepaid_pos_logistics_settlement
  fields:
    edge_family: reconciliation_understanding
    evidence_basis: materialized inverse of HAS_RECONCILIATION_SIDE
    confidence: high
    canonical_cognee_edge: true
    logistics_only: true
    canonical_edge_type: BELONGS_TO_RECONCILIATION_PROFILE
    inverse_edge_type: HAS_RECONCILIATION_SIDE
    materialize_inverse: true
    edge_class: canonical
    source_type: reconciliation_side
    target_type: reconciliation_profile
    materialized_from: edge.reconciliation_profile.prepaid_pos_logistics_settlement.has_reconciliation_side.reconciliation_side.prepaid_pos_logistics_settlement.expected.5c1d27e4
    edge_properties:
      side_role: expected
```

```yaml
candidate_edge:
  edge_id: edge.reconciliation_profile.prepaid_pos_logistics_settlement.has_reconciliation_side.reconciliation_side.prepaid_pos_logistics_settlement.actual.0342fa18
  edge_type: HAS_RECONCILIATION_SIDE
  source: reconciliation_profile.prepaid_pos_logistics_settlement
  target: reconciliation_side.prepaid_pos_logistics_settlement.actual
  fields:
    edge_family: reconciliation_understanding
    evidence_basis: reconciliation_profile.fields.sides
    confidence: high
    canonical_cognee_edge: true
    logistics_only: true
    canonical_edge_type: HAS_RECONCILIATION_SIDE
    inverse_edge_type: BELONGS_TO_RECONCILIATION_PROFILE
    materialize_inverse: true
    edge_class: canonical
    source_type: reconciliation_profile
    target_type: reconciliation_side
    edge_properties:
      side_role: actual
```

```yaml
candidate_edge:
  edge_id: edge.reconciliation_side.prepaid_pos_logistics_settlement.actual.belongs_to_reconciliation_profile.reconciliation_profile.prepaid_pos_logistics_settlement.0342fa18
  edge_type: BELONGS_TO_RECONCILIATION_PROFILE
  source: reconciliation_side.prepaid_pos_logistics_settlement.actual
  target: reconciliation_profile.prepaid_pos_logistics_settlement
  fields:
    edge_family: reconciliation_understanding
    evidence_basis: materialized inverse of HAS_RECONCILIATION_SIDE
    confidence: high
    canonical_cognee_edge: true
    logistics_only: true
    canonical_edge_type: BELONGS_TO_RECONCILIATION_PROFILE
    inverse_edge_type: HAS_RECONCILIATION_SIDE
    materialize_inverse: true
    edge_class: canonical
    source_type: reconciliation_side
    target_type: reconciliation_profile
    materialized_from: edge.reconciliation_profile.prepaid_pos_logistics_settlement.has_reconciliation_side.reconciliation_side.prepaid_pos_logistics_settlement.actual.0342fa18
    edge_properties:
      side_role: actual
```

```yaml
candidate_edge:
  edge_id: edge.reconciliation_profile.prepaid_pos_logistics_settlement.uses_matching_logic.matching_logic.prepaid_pos_logistics_settlement
  edge_type: USES_MATCHING_LOGIC
  source: reconciliation_profile.prepaid_pos_logistics_settlement
  target: matching_logic.prepaid_pos_logistics_settlement
  fields:
    edge_family: reconciliation_understanding
    evidence_basis: reconciliation_profile.fields.matching_logic
    confidence: high
    canonical_cognee_edge: true
    logistics_only: true
    canonical_edge_type: USES_MATCHING_LOGIC
    inverse_edge_type: SUPPORTS_RECONCILIATION_PROFILE
    materialize_inverse: true
    edge_class: canonical
    source_type: reconciliation_profile
    target_type: matching_logic
```

```yaml
candidate_edge:
  edge_id: edge.matching_logic.prepaid_pos_logistics_settlement.supports_reconciliation_profile.reconciliation_profile.prepaid_pos_logistics_settlement
  edge_type: SUPPORTS_RECONCILIATION_PROFILE
  source: matching_logic.prepaid_pos_logistics_settlement
  target: reconciliation_profile.prepaid_pos_logistics_settlement
  fields:
    edge_family: reconciliation_understanding
    evidence_basis: materialized inverse of USES_MATCHING_LOGIC
    confidence: high
    canonical_cognee_edge: true
    logistics_only: true
    canonical_edge_type: SUPPORTS_RECONCILIATION_PROFILE
    inverse_edge_type: USES_MATCHING_LOGIC
    materialize_inverse: true
    edge_class: canonical
    source_type: matching_logic
    target_type: reconciliation_profile
    materialized_from: edge.reconciliation_profile.prepaid_pos_logistics_settlement.uses_matching_logic.matching_logic.prepaid_pos_logistics_settlement
```

```yaml
candidate_edge:
  edge_id: edge.reconciliation_profile.prepaid_pos_logistics_settlement.has_mismatch_category.mismatch_category.prepaid_pos_logistics_settlement.missing_expected
  edge_type: HAS_MISMATCH_CATEGORY
  source: reconciliation_profile.prepaid_pos_logistics_settlement
  target: mismatch_category.prepaid_pos_logistics_settlement.missing_expected
  fields:
    edge_family: reconciliation_understanding
    evidence_basis: reconciliation_profile.fields.mismatch_categories
    confidence: high
    canonical_cognee_edge: true
    logistics_only: true
    canonical_edge_type: HAS_MISMATCH_CATEGORY
    inverse_edge_type: MISMATCH_OF_PROFILE
    materialize_inverse: false
    edge_class: canonical
    source_type: reconciliation_profile
    target_type: mismatch_category
```

```yaml
candidate_edge:
  edge_id: edge.reconciliation_profile.prepaid_pos_logistics_settlement.has_mismatch_category.mismatch_category.prepaid_pos_logistics_settlement.missing_actual
  edge_type: HAS_MISMATCH_CATEGORY
  source: reconciliation_profile.prepaid_pos_logistics_settlement
  target: mismatch_category.prepaid_pos_logistics_settlement.missing_actual
  fields:
    edge_family: reconciliation_understanding
    evidence_basis: reconciliation_profile.fields.mismatch_categories
    confidence: high
    canonical_cognee_edge: true
    logistics_only: true
    canonical_edge_type: HAS_MISMATCH_CATEGORY
    inverse_edge_type: MISMATCH_OF_PROFILE
    materialize_inverse: false
    edge_class: canonical
    source_type: reconciliation_profile
    target_type: mismatch_category
```

```yaml
candidate_edge:
  edge_id: edge.reconciliation_profile.prepaid_pos_logistics_settlement.has_mismatch_category.mismatch_category.prepaid_pos_logistics_settlement.amount_mismatch
  edge_type: HAS_MISMATCH_CATEGORY
  source: reconciliation_profile.prepaid_pos_logistics_settlement
  target: mismatch_category.prepaid_pos_logistics_settlement.amount_mismatch
  fields:
    edge_family: reconciliation_understanding
    evidence_basis: reconciliation_profile.fields.mismatch_categories
    confidence: high
    canonical_cognee_edge: true
    logistics_only: true
    canonical_edge_type: HAS_MISMATCH_CATEGORY
    inverse_edge_type: MISMATCH_OF_PROFILE
    materialize_inverse: false
    edge_class: canonical
    source_type: reconciliation_profile
    target_type: mismatch_category
```

```yaml
candidate_edge:
  edge_id: edge.reconciliation_profile.prepaid_pos_logistics_settlement.has_mismatch_category.mismatch_category.prepaid_pos_logistics_settlement.timing_mismatch
  edge_type: HAS_MISMATCH_CATEGORY
  source: reconciliation_profile.prepaid_pos_logistics_settlement
  target: mismatch_category.prepaid_pos_logistics_settlement.timing_mismatch
  fields:
    edge_family: reconciliation_understanding
    evidence_basis: reconciliation_profile.fields.mismatch_categories
    confidence: high
    canonical_cognee_edge: true
    logistics_only: true
    canonical_edge_type: HAS_MISMATCH_CATEGORY
    inverse_edge_type: MISMATCH_OF_PROFILE
    materialize_inverse: false
    edge_class: canonical
    source_type: reconciliation_profile
    target_type: mismatch_category
```

```yaml
candidate_edge:
  edge_id: edge.business_process.cod_delivery_to_courier_remittance.has_reconciliation_profile.reconciliation_profile.low_confidence_native_to_fallback
  edge_type: HAS_RECONCILIATION_PROFILE
  source: business_process.cod_delivery_to_courier_remittance
  target: reconciliation_profile.low_confidence_native_to_fallback
  fields:
    edge_family: reconciliation_understanding
    evidence_basis: reconciliation_profile.fields.business_process_id
    confidence: high
    canonical_cognee_edge: true
    logistics_only: true
    canonical_edge_type: HAS_RECONCILIATION_PROFILE
    inverse_edge_type: SUPPORTS_PROCESS
    materialize_inverse: true
    edge_class: canonical
    source_type: business_process
    target_type: reconciliation_profile
```

```yaml
candidate_edge:
  edge_id: edge.reconciliation_profile.low_confidence_native_to_fallback.supports_process.business_process.cod_delivery_to_courier_remittance
  edge_type: SUPPORTS_PROCESS
  source: reconciliation_profile.low_confidence_native_to_fallback
  target: business_process.cod_delivery_to_courier_remittance
  fields:
    edge_family: reconciliation_understanding
    evidence_basis: materialized inverse of HAS_RECONCILIATION_PROFILE
    confidence: high
    canonical_cognee_edge: true
    logistics_only: true
    canonical_edge_type: SUPPORTS_PROCESS
    inverse_edge_type: HAS_RECONCILIATION_PROFILE
    materialize_inverse: true
    edge_class: canonical
    source_type: reconciliation_profile
    target_type: business_process
    materialized_from: edge.business_process.cod_delivery_to_courier_remittance.has_reconciliation_profile.reconciliation_profile.low_confidence_native_to_fallback
```

```yaml
candidate_edge:
  edge_id: edge.reconciliation_profile.low_confidence_native_to_fallback.has_reconciliation_side.reconciliation_side.low_confidence_native_to_fallback.expected.5c1d27e4
  edge_type: HAS_RECONCILIATION_SIDE
  source: reconciliation_profile.low_confidence_native_to_fallback
  target: reconciliation_side.low_confidence_native_to_fallback.expected
  fields:
    edge_family: reconciliation_understanding
    evidence_basis: reconciliation_profile.fields.sides
    confidence: high
    canonical_cognee_edge: true
    logistics_only: true
    canonical_edge_type: HAS_RECONCILIATION_SIDE
    inverse_edge_type: BELONGS_TO_RECONCILIATION_PROFILE
    materialize_inverse: true
    edge_class: canonical
    source_type: reconciliation_profile
    target_type: reconciliation_side
    edge_properties:
      side_role: expected
```

```yaml
candidate_edge:
  edge_id: edge.reconciliation_side.low_confidence_native_to_fallback.expected.belongs_to_reconciliation_profile.reconciliation_profile.low_confidence_native_to_fallback.5c1d27e4
  edge_type: BELONGS_TO_RECONCILIATION_PROFILE
  source: reconciliation_side.low_confidence_native_to_fallback.expected
  target: reconciliation_profile.low_confidence_native_to_fallback
  fields:
    edge_family: reconciliation_understanding
    evidence_basis: materialized inverse of HAS_RECONCILIATION_SIDE
    confidence: high
    canonical_cognee_edge: true
    logistics_only: true
    canonical_edge_type: BELONGS_TO_RECONCILIATION_PROFILE
    inverse_edge_type: HAS_RECONCILIATION_SIDE
    materialize_inverse: true
    edge_class: canonical
    source_type: reconciliation_side
    target_type: reconciliation_profile
    materialized_from: edge.reconciliation_profile.low_confidence_native_to_fallback.has_reconciliation_side.reconciliation_side.low_confidence_native_to_fallback.expected.5c1d27e4
    edge_properties:
      side_role: expected
```

```yaml
candidate_edge:
  edge_id: edge.reconciliation_profile.low_confidence_native_to_fallback.has_reconciliation_side.reconciliation_side.low_confidence_native_to_fallback.actual.0342fa18
  edge_type: HAS_RECONCILIATION_SIDE
  source: reconciliation_profile.low_confidence_native_to_fallback
  target: reconciliation_side.low_confidence_native_to_fallback.actual
  fields:
    edge_family: reconciliation_understanding
    evidence_basis: reconciliation_profile.fields.sides
    confidence: high
    canonical_cognee_edge: true
    logistics_only: true
    canonical_edge_type: HAS_RECONCILIATION_SIDE
    inverse_edge_type: BELONGS_TO_RECONCILIATION_PROFILE
    materialize_inverse: true
    edge_class: canonical
    source_type: reconciliation_profile
    target_type: reconciliation_side
    edge_properties:
      side_role: actual
```

```yaml
candidate_edge:
  edge_id: edge.reconciliation_side.low_confidence_native_to_fallback.actual.belongs_to_reconciliation_profile.reconciliation_profile.low_confidence_native_to_fallback.0342fa18
  edge_type: BELONGS_TO_RECONCILIATION_PROFILE
  source: reconciliation_side.low_confidence_native_to_fallback.actual
  target: reconciliation_profile.low_confidence_native_to_fallback
  fields:
    edge_family: reconciliation_understanding
    evidence_basis: materialized inverse of HAS_RECONCILIATION_SIDE
    confidence: high
    canonical_cognee_edge: true
    logistics_only: true
    canonical_edge_type: BELONGS_TO_RECONCILIATION_PROFILE
    inverse_edge_type: HAS_RECONCILIATION_SIDE
    materialize_inverse: true
    edge_class: canonical
    source_type: reconciliation_side
    target_type: reconciliation_profile
    materialized_from: edge.reconciliation_profile.low_confidence_native_to_fallback.has_reconciliation_side.reconciliation_side.low_confidence_native_to_fallback.actual.0342fa18
    edge_properties:
      side_role: actual
```

```yaml
candidate_edge:
  edge_id: edge.reconciliation_profile.low_confidence_native_to_fallback.uses_matching_logic.matching_logic.low_confidence_native_to_fallback
  edge_type: USES_MATCHING_LOGIC
  source: reconciliation_profile.low_confidence_native_to_fallback
  target: matching_logic.low_confidence_native_to_fallback
  fields:
    edge_family: reconciliation_understanding
    evidence_basis: reconciliation_profile.fields.matching_logic
    confidence: high
    canonical_cognee_edge: true
    logistics_only: true
    canonical_edge_type: USES_MATCHING_LOGIC
    inverse_edge_type: SUPPORTS_RECONCILIATION_PROFILE
    materialize_inverse: true
    edge_class: canonical
    source_type: reconciliation_profile
    target_type: matching_logic
```

```yaml
candidate_edge:
  edge_id: edge.matching_logic.low_confidence_native_to_fallback.supports_reconciliation_profile.reconciliation_profile.low_confidence_native_to_fallback
  edge_type: SUPPORTS_RECONCILIATION_PROFILE
  source: matching_logic.low_confidence_native_to_fallback
  target: reconciliation_profile.low_confidence_native_to_fallback
  fields:
    edge_family: reconciliation_understanding
    evidence_basis: materialized inverse of USES_MATCHING_LOGIC
    confidence: high
    canonical_cognee_edge: true
    logistics_only: true
    canonical_edge_type: SUPPORTS_RECONCILIATION_PROFILE
    inverse_edge_type: USES_MATCHING_LOGIC
    materialize_inverse: true
    edge_class: canonical
    source_type: matching_logic
    target_type: reconciliation_profile
    materialized_from: edge.reconciliation_profile.low_confidence_native_to_fallback.uses_matching_logic.matching_logic.low_confidence_native_to_fallback
```

```yaml
candidate_edge:
  edge_id: edge.reconciliation_profile.low_confidence_native_to_fallback.has_mismatch_category.mismatch_category.low_confidence_native_to_fallback.missing_expected
  edge_type: HAS_MISMATCH_CATEGORY
  source: reconciliation_profile.low_confidence_native_to_fallback
  target: mismatch_category.low_confidence_native_to_fallback.missing_expected
  fields:
    edge_family: reconciliation_understanding
    evidence_basis: reconciliation_profile.fields.mismatch_categories
    confidence: high
    canonical_cognee_edge: true
    logistics_only: true
    canonical_edge_type: HAS_MISMATCH_CATEGORY
    inverse_edge_type: MISMATCH_OF_PROFILE
    materialize_inverse: false
    edge_class: canonical
    source_type: reconciliation_profile
    target_type: mismatch_category
```

```yaml
candidate_edge:
  edge_id: edge.reconciliation_profile.low_confidence_native_to_fallback.has_mismatch_category.mismatch_category.low_confidence_native_to_fallback.missing_actual
  edge_type: HAS_MISMATCH_CATEGORY
  source: reconciliation_profile.low_confidence_native_to_fallback
  target: mismatch_category.low_confidence_native_to_fallback.missing_actual
  fields:
    edge_family: reconciliation_understanding
    evidence_basis: reconciliation_profile.fields.mismatch_categories
    confidence: high
    canonical_cognee_edge: true
    logistics_only: true
    canonical_edge_type: HAS_MISMATCH_CATEGORY
    inverse_edge_type: MISMATCH_OF_PROFILE
    materialize_inverse: false
    edge_class: canonical
    source_type: reconciliation_profile
    target_type: mismatch_category
```

```yaml
candidate_edge:
  edge_id: edge.reconciliation_profile.low_confidence_native_to_fallback.has_mismatch_category.mismatch_category.low_confidence_native_to_fallback.amount_mismatch
  edge_type: HAS_MISMATCH_CATEGORY
  source: reconciliation_profile.low_confidence_native_to_fallback
  target: mismatch_category.low_confidence_native_to_fallback.amount_mismatch
  fields:
    edge_family: reconciliation_understanding
    evidence_basis: reconciliation_profile.fields.mismatch_categories
    confidence: high
    canonical_cognee_edge: true
    logistics_only: true
    canonical_edge_type: HAS_MISMATCH_CATEGORY
    inverse_edge_type: MISMATCH_OF_PROFILE
    materialize_inverse: false
    edge_class: canonical
    source_type: reconciliation_profile
    target_type: mismatch_category
```

```yaml
candidate_edge:
  edge_id: edge.reconciliation_profile.low_confidence_native_to_fallback.has_mismatch_category.mismatch_category.low_confidence_native_to_fallback.timing_mismatch
  edge_type: HAS_MISMATCH_CATEGORY
  source: reconciliation_profile.low_confidence_native_to_fallback
  target: mismatch_category.low_confidence_native_to_fallback.timing_mismatch
  fields:
    edge_family: reconciliation_understanding
    evidence_basis: reconciliation_profile.fields.mismatch_categories
    confidence: high
    canonical_cognee_edge: true
    logistics_only: true
    canonical_edge_type: HAS_MISMATCH_CATEGORY
    inverse_edge_type: MISMATCH_OF_PROFILE
    materialize_inverse: false
    edge_class: canonical
    source_type: reconciliation_profile
    target_type: mismatch_category
```

```yaml
candidate_edge:
  edge_id: edge.query_pattern.logistics.shipment_count_by_courier.produces_metric.metric.shipment_count
  edge_type: PRODUCES_METRIC
  source: query_pattern.logistics.shipment_count_by_courier
  target: metric.shipment_count
  fields:
    edge_family: execution_guidance
    evidence_basis: query_pattern.fields.canonical_metric_or_object
    confidence: high
    canonical_cognee_edge: true
    logistics_only: true
    canonical_edge_type: PRODUCES_METRIC
    inverse_edge_type: PRODUCED_BY_QUERY_PATTERN
    materialize_inverse: false
    edge_class: canonical
    source_type: query_pattern
    target_type: metric
```

```yaml
candidate_edge:
  edge_id: edge.query_pattern.logistics.shipment_count_by_courier.produces_metric.metric.unique_awb_count
  edge_type: PRODUCES_METRIC
  source: query_pattern.logistics.shipment_count_by_courier
  target: metric.unique_awb_count
  fields:
    edge_family: execution_guidance
    evidence_basis: query_pattern.fields.canonical_metric_or_object
    confidence: high
    canonical_cognee_edge: true
    logistics_only: true
    canonical_edge_type: PRODUCES_METRIC
    inverse_edge_type: PRODUCED_BY_QUERY_PATTERN
    materialize_inverse: false
    edge_class: canonical
    source_type: query_pattern
    target_type: metric
```

```yaml
candidate_edge:
  edge_id: edge.query_pattern.logistics.shipment_count_by_courier.uses_table.table.zs_observe.shiprocket_oms
  edge_type: USES_TABLE
  source: query_pattern.logistics.shipment_count_by_courier
  target: table.zs_observe.shiprocket_oms
  fields:
    edge_family: metric_understanding
    evidence_basis: query_pattern.fields.required_tables
    confidence: high
    canonical_cognee_edge: true
    logistics_only: true
    canonical_edge_type: USES_TABLE
    inverse_edge_type: USED_BY_CONTEXT
    materialize_inverse: false
    edge_class: canonical
    source_type: query_pattern
    target_type: table
```

```yaml
candidate_edge:
  edge_id: edge.query_pattern.logistics.shipment_count_by_courier.requires_rule.rule.logistics.active_filter_when_available
  edge_type: REQUIRES_RULE
  source: query_pattern.logistics.shipment_count_by_courier
  target: rule.logistics.active_filter_when_available
  fields:
    edge_family: execution_guidance
    evidence_basis: query_pattern.fields.rules
    confidence: high
    canonical_cognee_edge: true
    logistics_only: true
    canonical_edge_type: REQUIRES_RULE
    inverse_edge_type: REQUIRED_BY_QUERY_PATTERN
    materialize_inverse: false
    edge_class: canonical
    source_type: query_pattern
    target_type: rule
```

```yaml
candidate_edge:
  edge_id: edge.query_pattern.logistics.shipment_count_by_courier.requires_rule.rule.logistics.awb_primary_reconciliation_unit
  edge_type: REQUIRES_RULE
  source: query_pattern.logistics.shipment_count_by_courier
  target: rule.logistics.awb_primary_reconciliation_unit
  fields:
    edge_family: execution_guidance
    evidence_basis: query_pattern.fields.rules
    confidence: high
    canonical_cognee_edge: true
    logistics_only: true
    canonical_edge_type: REQUIRES_RULE
    inverse_edge_type: REQUIRED_BY_QUERY_PATTERN
    materialize_inverse: false
    edge_class: canonical
    source_type: query_pattern
    target_type: rule
```

```yaml
candidate_edge:
  edge_id: edge.query_pattern.logistics.shipment_count_by_courier.has_validation_test.validation_test.logistics.required_scope_context
  edge_type: HAS_VALIDATION_TEST
  source: query_pattern.logistics.shipment_count_by_courier
  target: validation_test.logistics.required_scope_context
  fields:
    edge_family: execution_guidance
    evidence_basis: query_pattern.fields.validation_tests
    confidence: high
    canonical_cognee_edge: true
    logistics_only: true
    canonical_edge_type: HAS_VALIDATION_TEST
    inverse_edge_type: VALIDATES_QUERY_PATTERN_OR_ENFORCES_RULE
    materialize_inverse: false
    edge_class: canonical
    source_type: query_pattern
    target_type: validation_test
```

```yaml
candidate_edge:
  edge_id: edge.query_pattern.logistics.shipment_count_by_courier.has_validation_test.validation_test.logistics.amount_semantics_not_by_name
  edge_type: HAS_VALIDATION_TEST
  source: query_pattern.logistics.shipment_count_by_courier
  target: validation_test.logistics.amount_semantics_not_by_name
  fields:
    edge_family: execution_guidance
    evidence_basis: query_pattern.fields.validation_tests
    confidence: high
    canonical_cognee_edge: true
    logistics_only: true
    canonical_edge_type: HAS_VALIDATION_TEST
    inverse_edge_type: VALIDATES_QUERY_PATTERN_OR_ENFORCES_RULE
    materialize_inverse: false
    edge_class: canonical
    source_type: query_pattern
    target_type: validation_test
```

```yaml
candidate_edge:
  edge_id: edge.query_pattern.logistics.shipment_count_by_courier.uses_output_contract.output_contract.logistics_metric_summary
  edge_type: USES_OUTPUT_CONTRACT
  source: query_pattern.logistics.shipment_count_by_courier
  target: output_contract.logistics_metric_summary
  fields:
    edge_family: execution_guidance
    evidence_basis: query_pattern.fields.output_contracts
    confidence: high
    canonical_cognee_edge: true
    logistics_only: true
    canonical_edge_type: USES_OUTPUT_CONTRACT
    inverse_edge_type: USED_BY_CONTEXT
    materialize_inverse: false
    edge_class: canonical
    source_type: query_pattern
    target_type: output_contract
```

```yaml
candidate_edge:
  edge_id: edge.query_pattern.logistics.delivery_and_rto_rate.produces_metric.metric.delivery_success_rate
  edge_type: PRODUCES_METRIC
  source: query_pattern.logistics.delivery_and_rto_rate
  target: metric.delivery_success_rate
  fields:
    edge_family: execution_guidance
    evidence_basis: query_pattern.fields.canonical_metric_or_object
    confidence: high
    canonical_cognee_edge: true
    logistics_only: true
    canonical_edge_type: PRODUCES_METRIC
    inverse_edge_type: PRODUCED_BY_QUERY_PATTERN
    materialize_inverse: false
    edge_class: canonical
    source_type: query_pattern
    target_type: metric
```

```yaml
candidate_edge:
  edge_id: edge.query_pattern.logistics.delivery_and_rto_rate.produces_metric.metric.rto_rate
  edge_type: PRODUCES_METRIC
  source: query_pattern.logistics.delivery_and_rto_rate
  target: metric.rto_rate
  fields:
    edge_family: execution_guidance
    evidence_basis: query_pattern.fields.canonical_metric_or_object
    confidence: high
    canonical_cognee_edge: true
    logistics_only: true
    canonical_edge_type: PRODUCES_METRIC
    inverse_edge_type: PRODUCED_BY_QUERY_PATTERN
    materialize_inverse: false
    edge_class: canonical
    source_type: query_pattern
    target_type: metric
```

```yaml
candidate_edge:
  edge_id: edge.query_pattern.logistics.delivery_and_rto_rate.produces_metric.metric.delivered_shipment_count
  edge_type: PRODUCES_METRIC
  source: query_pattern.logistics.delivery_and_rto_rate
  target: metric.delivered_shipment_count
  fields:
    edge_family: execution_guidance
    evidence_basis: query_pattern.fields.canonical_metric_or_object
    confidence: high
    canonical_cognee_edge: true
    logistics_only: true
    canonical_edge_type: PRODUCES_METRIC
    inverse_edge_type: PRODUCED_BY_QUERY_PATTERN
    materialize_inverse: false
    edge_class: canonical
    source_type: query_pattern
    target_type: metric
```

```yaml
candidate_edge:
  edge_id: edge.query_pattern.logistics.delivery_and_rto_rate.produces_metric.metric.rto_count
  edge_type: PRODUCES_METRIC
  source: query_pattern.logistics.delivery_and_rto_rate
  target: metric.rto_count
  fields:
    edge_family: execution_guidance
    evidence_basis: query_pattern.fields.canonical_metric_or_object
    confidence: high
    canonical_cognee_edge: true
    logistics_only: true
    canonical_edge_type: PRODUCES_METRIC
    inverse_edge_type: PRODUCED_BY_QUERY_PATTERN
    materialize_inverse: false
    edge_class: canonical
    source_type: query_pattern
    target_type: metric
```

```yaml
candidate_edge:
  edge_id: edge.query_pattern.logistics.delivery_and_rto_rate.uses_table.table.zs_observe.shiprocket_oms
  edge_type: USES_TABLE
  source: query_pattern.logistics.delivery_and_rto_rate
  target: table.zs_observe.shiprocket_oms
  fields:
    edge_family: metric_understanding
    evidence_basis: query_pattern.fields.required_tables
    confidence: high
    canonical_cognee_edge: true
    logistics_only: true
    canonical_edge_type: USES_TABLE
    inverse_edge_type: USED_BY_CONTEXT
    materialize_inverse: false
    edge_class: canonical
    source_type: query_pattern
    target_type: table
```

```yaml
candidate_edge:
  edge_id: edge.query_pattern.logistics.delivery_and_rto_rate.requires_rule.rule.logistics.delivered_date_for_delivery_metrics
  edge_type: REQUIRES_RULE
  source: query_pattern.logistics.delivery_and_rto_rate
  target: rule.logistics.delivered_date_for_delivery_metrics
  fields:
    edge_family: execution_guidance
    evidence_basis: query_pattern.fields.rules
    confidence: high
    canonical_cognee_edge: true
    logistics_only: true
    canonical_edge_type: REQUIRES_RULE
    inverse_edge_type: REQUIRED_BY_QUERY_PATTERN
    materialize_inverse: false
    edge_class: canonical
    source_type: query_pattern
    target_type: rule
```

```yaml
candidate_edge:
  edge_id: edge.query_pattern.logistics.delivery_and_rto_rate.requires_rule.rule.logistics.payment_mode_value_profile_required
  edge_type: REQUIRES_RULE
  source: query_pattern.logistics.delivery_and_rto_rate
  target: rule.logistics.payment_mode_value_profile_required
  fields:
    edge_family: execution_guidance
    evidence_basis: query_pattern.fields.rules
    confidence: high
    canonical_cognee_edge: true
    logistics_only: true
    canonical_edge_type: REQUIRES_RULE
    inverse_edge_type: REQUIRED_BY_QUERY_PATTERN
    materialize_inverse: false
    edge_class: canonical
    source_type: query_pattern
    target_type: rule
```

```yaml
candidate_edge:
  edge_id: edge.query_pattern.logistics.delivery_and_rto_rate.has_validation_test.validation_test.logistics.required_scope_context
  edge_type: HAS_VALIDATION_TEST
  source: query_pattern.logistics.delivery_and_rto_rate
  target: validation_test.logistics.required_scope_context
  fields:
    edge_family: execution_guidance
    evidence_basis: query_pattern.fields.validation_tests
    confidence: high
    canonical_cognee_edge: true
    logistics_only: true
    canonical_edge_type: HAS_VALIDATION_TEST
    inverse_edge_type: VALIDATES_QUERY_PATTERN_OR_ENFORCES_RULE
    materialize_inverse: false
    edge_class: canonical
    source_type: query_pattern
    target_type: validation_test
```

```yaml
candidate_edge:
  edge_id: edge.query_pattern.logistics.delivery_and_rto_rate.has_validation_test.validation_test.logistics.amount_semantics_not_by_name
  edge_type: HAS_VALIDATION_TEST
  source: query_pattern.logistics.delivery_and_rto_rate
  target: validation_test.logistics.amount_semantics_not_by_name
  fields:
    edge_family: execution_guidance
    evidence_basis: query_pattern.fields.validation_tests
    confidence: high
    canonical_cognee_edge: true
    logistics_only: true
    canonical_edge_type: HAS_VALIDATION_TEST
    inverse_edge_type: VALIDATES_QUERY_PATTERN_OR_ENFORCES_RULE
    materialize_inverse: false
    edge_class: canonical
    source_type: query_pattern
    target_type: validation_test
```

```yaml
candidate_edge:
  edge_id: edge.query_pattern.logistics.delivery_and_rto_rate.uses_output_contract.output_contract.logistics_metric_summary
  edge_type: USES_OUTPUT_CONTRACT
  source: query_pattern.logistics.delivery_and_rto_rate
  target: output_contract.logistics_metric_summary
  fields:
    edge_family: execution_guidance
    evidence_basis: query_pattern.fields.output_contracts
    confidence: high
    canonical_cognee_edge: true
    logistics_only: true
    canonical_edge_type: USES_OUTPUT_CONTRACT
    inverse_edge_type: USED_BY_CONTEXT
    materialize_inverse: false
    edge_class: canonical
    source_type: query_pattern
    target_type: output_contract
```

```yaml
candidate_edge:
  edge_id: edge.query_pattern.logistics.shipments_without_invoice.uses_reconciliation_profile.reconciliation_profile.shipment_to_freight_invoice
  edge_type: USES_RECONCILIATION_PROFILE
  source: query_pattern.logistics.shipments_without_invoice
  target: reconciliation_profile.shipment_to_freight_invoice
  fields:
    edge_family: execution_guidance
    evidence_basis: query_pattern.fields.canonical_metric_or_object
    confidence: high
    canonical_cognee_edge: true
    logistics_only: true
    canonical_edge_type: USES_RECONCILIATION_PROFILE
    inverse_edge_type: USED_BY_QUERY_PATTERN
    materialize_inverse: false
    edge_class: canonical
    source_type: query_pattern
    target_type: reconciliation_profile
```

```yaml
candidate_edge:
  edge_id: edge.query_pattern.logistics.shipments_without_invoice.uses_table.table.zs_observe.shiprocket_oms
  edge_type: USES_TABLE
  source: query_pattern.logistics.shipments_without_invoice
  target: table.zs_observe.shiprocket_oms
  fields:
    edge_family: metric_understanding
    evidence_basis: query_pattern.fields.required_tables
    confidence: high
    canonical_cognee_edge: true
    logistics_only: true
    canonical_edge_type: USES_TABLE
    inverse_edge_type: USED_BY_CONTEXT
    materialize_inverse: false
    edge_class: canonical
    source_type: query_pattern
    target_type: table
```

```yaml
candidate_edge:
  edge_id: edge.query_pattern.logistics.shipments_without_invoice.uses_table.table.zs_observe.shiprocket_invoice
  edge_type: USES_TABLE
  source: query_pattern.logistics.shipments_without_invoice
  target: table.zs_observe.shiprocket_invoice
  fields:
    edge_family: metric_understanding
    evidence_basis: query_pattern.fields.required_tables
    confidence: high
    canonical_cognee_edge: true
    logistics_only: true
    canonical_edge_type: USES_TABLE
    inverse_edge_type: USED_BY_CONTEXT
    materialize_inverse: false
    edge_class: canonical
    source_type: query_pattern
    target_type: table
```

```yaml
candidate_edge:
  edge_id: edge.query_pattern.logistics.shipments_without_invoice.requires_rule.rule.logistics.awb_primary_reconciliation_unit
  edge_type: REQUIRES_RULE
  source: query_pattern.logistics.shipments_without_invoice
  target: rule.logistics.awb_primary_reconciliation_unit
  fields:
    edge_family: execution_guidance
    evidence_basis: query_pattern.fields.rules
    confidence: high
    canonical_cognee_edge: true
    logistics_only: true
    canonical_edge_type: REQUIRES_RULE
    inverse_edge_type: REQUIRED_BY_QUERY_PATTERN
    materialize_inverse: false
    edge_class: canonical
    source_type: query_pattern
    target_type: rule
```

```yaml
candidate_edge:
  edge_id: edge.query_pattern.logistics.shipments_without_invoice.requires_rule.rule.logistics.empty_tables_schema_only
  edge_type: REQUIRES_RULE
  source: query_pattern.logistics.shipments_without_invoice
  target: rule.logistics.empty_tables_schema_only
  fields:
    edge_family: execution_guidance
    evidence_basis: query_pattern.fields.rules
    confidence: high
    canonical_cognee_edge: true
    logistics_only: true
    canonical_edge_type: REQUIRES_RULE
    inverse_edge_type: REQUIRED_BY_QUERY_PATTERN
    materialize_inverse: false
    edge_class: canonical
    source_type: query_pattern
    target_type: rule
```

```yaml
candidate_edge:
  edge_id: edge.query_pattern.logistics.shipments_without_invoice.has_validation_test.validation_test.logistics.required_scope_context
  edge_type: HAS_VALIDATION_TEST
  source: query_pattern.logistics.shipments_without_invoice
  target: validation_test.logistics.required_scope_context
  fields:
    edge_family: execution_guidance
    evidence_basis: query_pattern.fields.validation_tests
    confidence: high
    canonical_cognee_edge: true
    logistics_only: true
    canonical_edge_type: HAS_VALIDATION_TEST
    inverse_edge_type: VALIDATES_QUERY_PATTERN_OR_ENFORCES_RULE
    materialize_inverse: false
    edge_class: canonical
    source_type: query_pattern
    target_type: validation_test
```

```yaml
candidate_edge:
  edge_id: edge.query_pattern.logistics.shipments_without_invoice.has_validation_test.validation_test.logistics.amount_semantics_not_by_name
  edge_type: HAS_VALIDATION_TEST
  source: query_pattern.logistics.shipments_without_invoice
  target: validation_test.logistics.amount_semantics_not_by_name
  fields:
    edge_family: execution_guidance
    evidence_basis: query_pattern.fields.validation_tests
    confidence: high
    canonical_cognee_edge: true
    logistics_only: true
    canonical_edge_type: HAS_VALIDATION_TEST
    inverse_edge_type: VALIDATES_QUERY_PATTERN_OR_ENFORCES_RULE
    materialize_inverse: false
    edge_class: canonical
    source_type: query_pattern
    target_type: validation_test
```

```yaml
candidate_edge:
  edge_id: edge.query_pattern.logistics.shipments_without_invoice.uses_output_contract.output_contract.logistics_diagnostic_summary
  edge_type: USES_OUTPUT_CONTRACT
  source: query_pattern.logistics.shipments_without_invoice
  target: output_contract.logistics_diagnostic_summary
  fields:
    edge_family: execution_guidance
    evidence_basis: query_pattern.fields.output_contracts
    confidence: high
    canonical_cognee_edge: true
    logistics_only: true
    canonical_edge_type: USES_OUTPUT_CONTRACT
    inverse_edge_type: USED_BY_CONTEXT
    materialize_inverse: false
    edge_class: canonical
    source_type: query_pattern
    target_type: output_contract
```

```yaml
candidate_edge:
  edge_id: edge.query_pattern.logistics.shipments_without_cod_remittance.produces_metric.metric.cod_gap_amount
  edge_type: PRODUCES_METRIC
  source: query_pattern.logistics.shipments_without_cod_remittance
  target: metric.cod_gap_amount
  fields:
    edge_family: execution_guidance
    evidence_basis: query_pattern.fields.canonical_metric_or_object
    confidence: high
    canonical_cognee_edge: true
    logistics_only: true
    canonical_edge_type: PRODUCES_METRIC
    inverse_edge_type: PRODUCED_BY_QUERY_PATTERN
    materialize_inverse: false
    edge_class: canonical
    source_type: query_pattern
    target_type: metric
```

```yaml
candidate_edge:
  edge_id: edge.query_pattern.logistics.shipments_without_cod_remittance.produces_metric.metric.unmatched_awb_count
  edge_type: PRODUCES_METRIC
  source: query_pattern.logistics.shipments_without_cod_remittance
  target: metric.unmatched_awb_count
  fields:
    edge_family: execution_guidance
    evidence_basis: query_pattern.fields.canonical_metric_or_object
    confidence: high
    canonical_cognee_edge: true
    logistics_only: true
    canonical_edge_type: PRODUCES_METRIC
    inverse_edge_type: PRODUCED_BY_QUERY_PATTERN
    materialize_inverse: false
    edge_class: canonical
    source_type: query_pattern
    target_type: metric
```

```yaml
candidate_edge:
  edge_id: edge.query_pattern.logistics.shipments_without_cod_remittance.uses_reconciliation_profile.reconciliation_profile.cod_expected_to_courier_remittance
  edge_type: USES_RECONCILIATION_PROFILE
  source: query_pattern.logistics.shipments_without_cod_remittance
  target: reconciliation_profile.cod_expected_to_courier_remittance
  fields:
    edge_family: execution_guidance
    evidence_basis: query_pattern.fields.canonical_metric_or_object
    confidence: high
    canonical_cognee_edge: true
    logistics_only: true
    canonical_edge_type: USES_RECONCILIATION_PROFILE
    inverse_edge_type: USED_BY_QUERY_PATTERN
    materialize_inverse: false
    edge_class: canonical
    source_type: query_pattern
    target_type: reconciliation_profile
```

```yaml
candidate_edge:
  edge_id: edge.query_pattern.logistics.shipments_without_cod_remittance.uses_table.table.zs_observe.shiprocket_oms
  edge_type: USES_TABLE
  source: query_pattern.logistics.shipments_without_cod_remittance
  target: table.zs_observe.shiprocket_oms
  fields:
    edge_family: metric_understanding
    evidence_basis: query_pattern.fields.required_tables
    confidence: high
    canonical_cognee_edge: true
    logistics_only: true
    canonical_edge_type: USES_TABLE
    inverse_edge_type: USED_BY_CONTEXT
    materialize_inverse: false
    edge_class: canonical
    source_type: query_pattern
    target_type: table
```

```yaml
candidate_edge:
  edge_id: edge.query_pattern.logistics.shipments_without_cod_remittance.uses_table.table.zs_observe.shiprocket_settlement
  edge_type: USES_TABLE
  source: query_pattern.logistics.shipments_without_cod_remittance
  target: table.zs_observe.shiprocket_settlement
  fields:
    edge_family: metric_understanding
    evidence_basis: query_pattern.fields.required_tables
    confidence: high
    canonical_cognee_edge: true
    logistics_only: true
    canonical_edge_type: USES_TABLE
    inverse_edge_type: USED_BY_CONTEXT
    materialize_inverse: false
    edge_class: canonical
    source_type: query_pattern
    target_type: table
```

```yaml
candidate_edge:
  edge_id: edge.query_pattern.logistics.shipments_without_cod_remittance.requires_rule.rule.logistics.settlement_date_for_cod_remittance
  edge_type: REQUIRES_RULE
  source: query_pattern.logistics.shipments_without_cod_remittance
  target: rule.logistics.settlement_date_for_cod_remittance
  fields:
    edge_family: execution_guidance
    evidence_basis: query_pattern.fields.rules
    confidence: high
    canonical_cognee_edge: true
    logistics_only: true
    canonical_edge_type: REQUIRES_RULE
    inverse_edge_type: REQUIRED_BY_QUERY_PATTERN
    materialize_inverse: false
    edge_class: canonical
    source_type: query_pattern
    target_type: rule
```

```yaml
candidate_edge:
  edge_id: edge.query_pattern.logistics.shipments_without_cod_remittance.requires_rule.rule.logistics.do_not_join_awb_to_bank_without_batch
  edge_type: REQUIRES_RULE
  source: query_pattern.logistics.shipments_without_cod_remittance
  target: rule.logistics.do_not_join_awb_to_bank_without_batch
  fields:
    edge_family: execution_guidance
    evidence_basis: query_pattern.fields.rules
    confidence: high
    canonical_cognee_edge: true
    logistics_only: true
    canonical_edge_type: REQUIRES_RULE
    inverse_edge_type: REQUIRED_BY_QUERY_PATTERN
    materialize_inverse: false
    edge_class: canonical
    source_type: query_pattern
    target_type: rule
```

```yaml
candidate_edge:
  edge_id: edge.query_pattern.logistics.shipments_without_cod_remittance.has_validation_test.validation_test.logistics.required_scope_context
  edge_type: HAS_VALIDATION_TEST
  source: query_pattern.logistics.shipments_without_cod_remittance
  target: validation_test.logistics.required_scope_context
  fields:
    edge_family: execution_guidance
    evidence_basis: query_pattern.fields.validation_tests
    confidence: high
    canonical_cognee_edge: true
    logistics_only: true
    canonical_edge_type: HAS_VALIDATION_TEST
    inverse_edge_type: VALIDATES_QUERY_PATTERN_OR_ENFORCES_RULE
    materialize_inverse: false
    edge_class: canonical
    source_type: query_pattern
    target_type: validation_test
```

```yaml
candidate_edge:
  edge_id: edge.query_pattern.logistics.shipments_without_cod_remittance.has_validation_test.validation_test.logistics.amount_semantics_not_by_name
  edge_type: HAS_VALIDATION_TEST
  source: query_pattern.logistics.shipments_without_cod_remittance
  target: validation_test.logistics.amount_semantics_not_by_name
  fields:
    edge_family: execution_guidance
    evidence_basis: query_pattern.fields.validation_tests
    confidence: high
    canonical_cognee_edge: true
    logistics_only: true
    canonical_edge_type: HAS_VALIDATION_TEST
    inverse_edge_type: VALIDATES_QUERY_PATTERN_OR_ENFORCES_RULE
    materialize_inverse: false
    edge_class: canonical
    source_type: query_pattern
    target_type: validation_test
```

```yaml
candidate_edge:
  edge_id: edge.query_pattern.logistics.shipments_without_cod_remittance.uses_output_contract.output_contract.logistics_diagnostic_summary
  edge_type: USES_OUTPUT_CONTRACT
  source: query_pattern.logistics.shipments_without_cod_remittance
  target: output_contract.logistics_diagnostic_summary
  fields:
    edge_family: execution_guidance
    evidence_basis: query_pattern.fields.output_contracts
    confidence: high
    canonical_cognee_edge: true
    logistics_only: true
    canonical_edge_type: USES_OUTPUT_CONTRACT
    inverse_edge_type: USED_BY_CONTEXT
    materialize_inverse: false
    edge_class: canonical
    source_type: query_pattern
    target_type: output_contract
```

```yaml
candidate_edge:
  edge_id: edge.query_pattern.logistics.freight_billed_by_awb.produces_metric.metric.freight_billed_amount
  edge_type: PRODUCES_METRIC
  source: query_pattern.logistics.freight_billed_by_awb
  target: metric.freight_billed_amount
  fields:
    edge_family: execution_guidance
    evidence_basis: query_pattern.fields.canonical_metric_or_object
    confidence: high
    canonical_cognee_edge: true
    logistics_only: true
    canonical_edge_type: PRODUCES_METRIC
    inverse_edge_type: PRODUCED_BY_QUERY_PATTERN
    materialize_inverse: false
    edge_class: canonical
    source_type: query_pattern
    target_type: metric
```

```yaml
candidate_edge:
  edge_id: edge.query_pattern.logistics.freight_billed_by_awb.produces_metric.metric.average_freight_per_awb
  edge_type: PRODUCES_METRIC
  source: query_pattern.logistics.freight_billed_by_awb
  target: metric.average_freight_per_awb
  fields:
    edge_family: execution_guidance
    evidence_basis: query_pattern.fields.canonical_metric_or_object
    confidence: high
    canonical_cognee_edge: true
    logistics_only: true
    canonical_edge_type: PRODUCES_METRIC
    inverse_edge_type: PRODUCED_BY_QUERY_PATTERN
    materialize_inverse: false
    edge_class: canonical
    source_type: query_pattern
    target_type: metric
```

```yaml
candidate_edge:
  edge_id: edge.query_pattern.logistics.freight_billed_by_awb.uses_reconciliation_profile.reconciliation_profile.shipment_to_freight_invoice
  edge_type: USES_RECONCILIATION_PROFILE
  source: query_pattern.logistics.freight_billed_by_awb
  target: reconciliation_profile.shipment_to_freight_invoice
  fields:
    edge_family: execution_guidance
    evidence_basis: query_pattern.fields.canonical_metric_or_object
    confidence: high
    canonical_cognee_edge: true
    logistics_only: true
    canonical_edge_type: USES_RECONCILIATION_PROFILE
    inverse_edge_type: USED_BY_QUERY_PATTERN
    materialize_inverse: false
    edge_class: canonical
    source_type: query_pattern
    target_type: reconciliation_profile
```

```yaml
candidate_edge:
  edge_id: edge.query_pattern.logistics.freight_billed_by_awb.uses_table.table.zs_observe.shiprocket_invoice
  edge_type: USES_TABLE
  source: query_pattern.logistics.freight_billed_by_awb
  target: table.zs_observe.shiprocket_invoice
  fields:
    edge_family: metric_understanding
    evidence_basis: query_pattern.fields.required_tables
    confidence: high
    canonical_cognee_edge: true
    logistics_only: true
    canonical_edge_type: USES_TABLE
    inverse_edge_type: USED_BY_CONTEXT
    materialize_inverse: false
    edge_class: canonical
    source_type: query_pattern
    target_type: table
```

```yaml
candidate_edge:
  edge_id: edge.query_pattern.logistics.freight_billed_by_awb.requires_rule.rule.logistics.shiprocket_invoice_charged_amount_freight
  edge_type: REQUIRES_RULE
  source: query_pattern.logistics.freight_billed_by_awb
  target: rule.logistics.shiprocket_invoice_charged_amount_freight
  fields:
    edge_family: execution_guidance
    evidence_basis: query_pattern.fields.rules
    confidence: high
    canonical_cognee_edge: true
    logistics_only: true
    canonical_edge_type: REQUIRES_RULE
    inverse_edge_type: REQUIRED_BY_QUERY_PATTERN
    materialize_inverse: false
    edge_class: canonical
    source_type: query_pattern
    target_type: rule
```

```yaml
candidate_edge:
  edge_id: edge.query_pattern.logistics.freight_billed_by_awb.requires_rule.rule.logistics.awb_primary_reconciliation_unit
  edge_type: REQUIRES_RULE
  source: query_pattern.logistics.freight_billed_by_awb
  target: rule.logistics.awb_primary_reconciliation_unit
  fields:
    edge_family: execution_guidance
    evidence_basis: query_pattern.fields.rules
    confidence: high
    canonical_cognee_edge: true
    logistics_only: true
    canonical_edge_type: REQUIRES_RULE
    inverse_edge_type: REQUIRED_BY_QUERY_PATTERN
    materialize_inverse: false
    edge_class: canonical
    source_type: query_pattern
    target_type: rule
```

```yaml
candidate_edge:
  edge_id: edge.query_pattern.logistics.freight_billed_by_awb.has_validation_test.validation_test.logistics.required_scope_context
  edge_type: HAS_VALIDATION_TEST
  source: query_pattern.logistics.freight_billed_by_awb
  target: validation_test.logistics.required_scope_context
  fields:
    edge_family: execution_guidance
    evidence_basis: query_pattern.fields.validation_tests
    confidence: high
    canonical_cognee_edge: true
    logistics_only: true
    canonical_edge_type: HAS_VALIDATION_TEST
    inverse_edge_type: VALIDATES_QUERY_PATTERN_OR_ENFORCES_RULE
    materialize_inverse: false
    edge_class: canonical
    source_type: query_pattern
    target_type: validation_test
```

```yaml
candidate_edge:
  edge_id: edge.query_pattern.logistics.freight_billed_by_awb.has_validation_test.validation_test.logistics.amount_semantics_not_by_name
  edge_type: HAS_VALIDATION_TEST
  source: query_pattern.logistics.freight_billed_by_awb
  target: validation_test.logistics.amount_semantics_not_by_name
  fields:
    edge_family: execution_guidance
    evidence_basis: query_pattern.fields.validation_tests
    confidence: high
    canonical_cognee_edge: true
    logistics_only: true
    canonical_edge_type: HAS_VALIDATION_TEST
    inverse_edge_type: VALIDATES_QUERY_PATTERN_OR_ENFORCES_RULE
    materialize_inverse: false
    edge_class: canonical
    source_type: query_pattern
    target_type: validation_test
```

```yaml
candidate_edge:
  edge_id: edge.query_pattern.logistics.freight_billed_by_awb.uses_output_contract.output_contract.logistics_metric_summary
  edge_type: USES_OUTPUT_CONTRACT
  source: query_pattern.logistics.freight_billed_by_awb
  target: output_contract.logistics_metric_summary
  fields:
    edge_family: execution_guidance
    evidence_basis: query_pattern.fields.output_contracts
    confidence: high
    canonical_cognee_edge: true
    logistics_only: true
    canonical_edge_type: USES_OUTPUT_CONTRACT
    inverse_edge_type: USED_BY_CONTEXT
    materialize_inverse: false
    edge_class: canonical
    source_type: query_pattern
    target_type: output_contract
```

```yaml
candidate_edge:
  edge_id: edge.query_pattern.logistics.freight_component_breakdown.produces_metric.metric.freight_billed_amount
  edge_type: PRODUCES_METRIC
  source: query_pattern.logistics.freight_component_breakdown
  target: metric.freight_billed_amount
  fields:
    edge_family: execution_guidance
    evidence_basis: query_pattern.fields.canonical_metric_or_object
    confidence: high
    canonical_cognee_edge: true
    logistics_only: true
    canonical_edge_type: PRODUCES_METRIC
    inverse_edge_type: PRODUCED_BY_QUERY_PATTERN
    materialize_inverse: false
    edge_class: canonical
    source_type: query_pattern
    target_type: metric
```

```yaml
candidate_edge:
  edge_id: edge.query_pattern.logistics.freight_component_breakdown.produces_metric.metric.forward_freight_amount
  edge_type: PRODUCES_METRIC
  source: query_pattern.logistics.freight_component_breakdown
  target: metric.forward_freight_amount
  fields:
    edge_family: execution_guidance
    evidence_basis: query_pattern.fields.canonical_metric_or_object
    confidence: high
    canonical_cognee_edge: true
    logistics_only: true
    canonical_edge_type: PRODUCES_METRIC
    inverse_edge_type: PRODUCED_BY_QUERY_PATTERN
    materialize_inverse: false
    edge_class: canonical
    source_type: query_pattern
    target_type: metric
```

```yaml
candidate_edge:
  edge_id: edge.query_pattern.logistics.freight_component_breakdown.produces_metric.metric.rto_freight_amount
  edge_type: PRODUCES_METRIC
  source: query_pattern.logistics.freight_component_breakdown
  target: metric.rto_freight_amount
  fields:
    edge_family: execution_guidance
    evidence_basis: query_pattern.fields.canonical_metric_or_object
    confidence: high
    canonical_cognee_edge: true
    logistics_only: true
    canonical_edge_type: PRODUCES_METRIC
    inverse_edge_type: PRODUCED_BY_QUERY_PATTERN
    materialize_inverse: false
    edge_class: canonical
    source_type: query_pattern
    target_type: metric
```

```yaml
candidate_edge:
  edge_id: edge.query_pattern.logistics.freight_component_breakdown.produces_metric.metric.cod_fee_amount
  edge_type: PRODUCES_METRIC
  source: query_pattern.logistics.freight_component_breakdown
  target: metric.cod_fee_amount
  fields:
    edge_family: execution_guidance
    evidence_basis: query_pattern.fields.canonical_metric_or_object
    confidence: high
    canonical_cognee_edge: true
    logistics_only: true
    canonical_edge_type: PRODUCES_METRIC
    inverse_edge_type: PRODUCED_BY_QUERY_PATTERN
    materialize_inverse: false
    edge_class: canonical
    source_type: query_pattern
    target_type: metric
```

```yaml
candidate_edge:
  edge_id: edge.query_pattern.logistics.freight_component_breakdown.produces_metric.metric.gst_on_freight_amount
  edge_type: PRODUCES_METRIC
  source: query_pattern.logistics.freight_component_breakdown
  target: metric.gst_on_freight_amount
  fields:
    edge_family: execution_guidance
    evidence_basis: query_pattern.fields.canonical_metric_or_object
    confidence: high
    canonical_cognee_edge: true
    logistics_only: true
    canonical_edge_type: PRODUCES_METRIC
    inverse_edge_type: PRODUCED_BY_QUERY_PATTERN
    materialize_inverse: false
    edge_class: canonical
    source_type: query_pattern
    target_type: metric
```

```yaml
candidate_edge:
  edge_id: edge.query_pattern.logistics.freight_component_breakdown.uses_reconciliation_profile.reconciliation_profile.freight_charge_validation
  edge_type: USES_RECONCILIATION_PROFILE
  source: query_pattern.logistics.freight_component_breakdown
  target: reconciliation_profile.freight_charge_validation
  fields:
    edge_family: execution_guidance
    evidence_basis: query_pattern.fields.canonical_metric_or_object
    confidence: high
    canonical_cognee_edge: true
    logistics_only: true
    canonical_edge_type: USES_RECONCILIATION_PROFILE
    inverse_edge_type: USED_BY_QUERY_PATTERN
    materialize_inverse: false
    edge_class: canonical
    source_type: query_pattern
    target_type: reconciliation_profile
```

```yaml
candidate_edge:
  edge_id: edge.query_pattern.logistics.freight_component_breakdown.uses_table.table.zs_observe.shiprocket_invoice
  edge_type: USES_TABLE
  source: query_pattern.logistics.freight_component_breakdown
  target: table.zs_observe.shiprocket_invoice
  fields:
    edge_family: metric_understanding
    evidence_basis: query_pattern.fields.required_tables
    confidence: high
    canonical_cognee_edge: true
    logistics_only: true
    canonical_edge_type: USES_TABLE
    inverse_edge_type: USED_BY_CONTEXT
    materialize_inverse: false
    edge_class: canonical
    source_type: query_pattern
    target_type: table
```

```yaml
candidate_edge:
  edge_id: edge.query_pattern.logistics.freight_component_breakdown.uses_table.table.zs_observe.delhivery_invoice
  edge_type: USES_TABLE
  source: query_pattern.logistics.freight_component_breakdown
  target: table.zs_observe.delhivery_invoice
  fields:
    edge_family: metric_understanding
    evidence_basis: query_pattern.fields.required_tables
    confidence: high
    canonical_cognee_edge: true
    logistics_only: true
    canonical_edge_type: USES_TABLE
    inverse_edge_type: USED_BY_CONTEXT
    materialize_inverse: false
    edge_class: canonical
    source_type: query_pattern
    target_type: table
```

```yaml
candidate_edge:
  edge_id: edge.query_pattern.logistics.freight_component_breakdown.requires_rule.rule.logistics.cod_fee_only_for_cod
  edge_type: REQUIRES_RULE
  source: query_pattern.logistics.freight_component_breakdown
  target: rule.logistics.cod_fee_only_for_cod
  fields:
    edge_family: execution_guidance
    evidence_basis: query_pattern.fields.rules
    confidence: high
    canonical_cognee_edge: true
    logistics_only: true
    canonical_edge_type: REQUIRES_RULE
    inverse_edge_type: REQUIRED_BY_QUERY_PATTERN
    materialize_inverse: false
    edge_class: canonical
    source_type: query_pattern
    target_type: rule
```

```yaml
candidate_edge:
  edge_id: edge.query_pattern.logistics.freight_component_breakdown.requires_rule.rule.logistics.rto_charge_only_for_rto
  edge_type: REQUIRES_RULE
  source: query_pattern.logistics.freight_component_breakdown
  target: rule.logistics.rto_charge_only_for_rto
  fields:
    edge_family: execution_guidance
    evidence_basis: query_pattern.fields.rules
    confidence: high
    canonical_cognee_edge: true
    logistics_only: true
    canonical_edge_type: REQUIRES_RULE
    inverse_edge_type: REQUIRED_BY_QUERY_PATTERN
    materialize_inverse: false
    edge_class: canonical
    source_type: query_pattern
    target_type: rule
```

```yaml
candidate_edge:
  edge_id: edge.query_pattern.logistics.freight_component_breakdown.has_validation_test.validation_test.logistics.required_scope_context
  edge_type: HAS_VALIDATION_TEST
  source: query_pattern.logistics.freight_component_breakdown
  target: validation_test.logistics.required_scope_context
  fields:
    edge_family: execution_guidance
    evidence_basis: query_pattern.fields.validation_tests
    confidence: high
    canonical_cognee_edge: true
    logistics_only: true
    canonical_edge_type: HAS_VALIDATION_TEST
    inverse_edge_type: VALIDATES_QUERY_PATTERN_OR_ENFORCES_RULE
    materialize_inverse: false
    edge_class: canonical
    source_type: query_pattern
    target_type: validation_test
```

```yaml
candidate_edge:
  edge_id: edge.query_pattern.logistics.freight_component_breakdown.has_validation_test.validation_test.logistics.amount_semantics_not_by_name
  edge_type: HAS_VALIDATION_TEST
  source: query_pattern.logistics.freight_component_breakdown
  target: validation_test.logistics.amount_semantics_not_by_name
  fields:
    edge_family: execution_guidance
    evidence_basis: query_pattern.fields.validation_tests
    confidence: high
    canonical_cognee_edge: true
    logistics_only: true
    canonical_edge_type: HAS_VALIDATION_TEST
    inverse_edge_type: VALIDATES_QUERY_PATTERN_OR_ENFORCES_RULE
    materialize_inverse: false
    edge_class: canonical
    source_type: query_pattern
    target_type: validation_test
```

```yaml
candidate_edge:
  edge_id: edge.query_pattern.logistics.freight_component_breakdown.uses_output_contract.output_contract.logistics_metric_summary
  edge_type: USES_OUTPUT_CONTRACT
  source: query_pattern.logistics.freight_component_breakdown
  target: output_contract.logistics_metric_summary
  fields:
    edge_family: execution_guidance
    evidence_basis: query_pattern.fields.output_contracts
    confidence: high
    canonical_cognee_edge: true
    logistics_only: true
    canonical_edge_type: USES_OUTPUT_CONTRACT
    inverse_edge_type: USED_BY_CONTEXT
    materialize_inverse: false
    edge_class: canonical
    source_type: query_pattern
    target_type: output_contract
```

```yaml
candidate_edge:
  edge_id: edge.query_pattern.logistics.freight_overcharge_check.produces_metric.metric.freight_overcharge_amount
  edge_type: PRODUCES_METRIC
  source: query_pattern.logistics.freight_overcharge_check
  target: metric.freight_overcharge_amount
  fields:
    edge_family: execution_guidance
    evidence_basis: query_pattern.fields.canonical_metric_or_object
    confidence: high
    canonical_cognee_edge: true
    logistics_only: true
    canonical_edge_type: PRODUCES_METRIC
    inverse_edge_type: PRODUCED_BY_QUERY_PATTERN
    materialize_inverse: false
    edge_class: canonical
    source_type: query_pattern
    target_type: metric
```

```yaml
candidate_edge:
  edge_id: edge.query_pattern.logistics.freight_overcharge_check.uses_reconciliation_profile.reconciliation_profile.freight_charge_validation
  edge_type: USES_RECONCILIATION_PROFILE
  source: query_pattern.logistics.freight_overcharge_check
  target: reconciliation_profile.freight_charge_validation
  fields:
    edge_family: execution_guidance
    evidence_basis: query_pattern.fields.canonical_metric_or_object
    confidence: high
    canonical_cognee_edge: true
    logistics_only: true
    canonical_edge_type: USES_RECONCILIATION_PROFILE
    inverse_edge_type: USED_BY_QUERY_PATTERN
    materialize_inverse: false
    edge_class: canonical
    source_type: query_pattern
    target_type: reconciliation_profile
```

```yaml
candidate_edge:
  edge_id: edge.query_pattern.logistics.freight_overcharge_check.uses_table.table.zs_observe.shiprocket_invoice
  edge_type: USES_TABLE
  source: query_pattern.logistics.freight_overcharge_check
  target: table.zs_observe.shiprocket_invoice
  fields:
    edge_family: metric_understanding
    evidence_basis: query_pattern.fields.required_tables
    confidence: high
    canonical_cognee_edge: true
    logistics_only: true
    canonical_edge_type: USES_TABLE
    inverse_edge_type: USED_BY_CONTEXT
    materialize_inverse: false
    edge_class: canonical
    source_type: query_pattern
    target_type: table
```

```yaml
candidate_edge:
  edge_id: edge.query_pattern.logistics.freight_overcharge_check.uses_table.table.zs_observe.delhivery_invoice
  edge_type: USES_TABLE
  source: query_pattern.logistics.freight_overcharge_check
  target: table.zs_observe.delhivery_invoice
  fields:
    edge_family: metric_understanding
    evidence_basis: query_pattern.fields.required_tables
    confidence: high
    canonical_cognee_edge: true
    logistics_only: true
    canonical_edge_type: USES_TABLE
    inverse_edge_type: USED_BY_CONTEXT
    materialize_inverse: false
    edge_class: canonical
    source_type: query_pattern
    target_type: table
```

```yaml
candidate_edge:
  edge_id: edge.query_pattern.logistics.freight_overcharge_check.requires_rule.rule.logistics.zone_value_profile_required
  edge_type: REQUIRES_RULE
  source: query_pattern.logistics.freight_overcharge_check
  target: rule.logistics.zone_value_profile_required
  fields:
    edge_family: execution_guidance
    evidence_basis: query_pattern.fields.rules
    confidence: high
    canonical_cognee_edge: true
    logistics_only: true
    canonical_edge_type: REQUIRES_RULE
    inverse_edge_type: REQUIRED_BY_QUERY_PATTERN
    materialize_inverse: false
    edge_class: canonical
    source_type: query_pattern
    target_type: rule
```

```yaml
candidate_edge:
  edge_id: edge.query_pattern.logistics.freight_overcharge_check.requires_rule.rule.logistics.payment_mode_value_profile_required
  edge_type: REQUIRES_RULE
  source: query_pattern.logistics.freight_overcharge_check
  target: rule.logistics.payment_mode_value_profile_required
  fields:
    edge_family: execution_guidance
    evidence_basis: query_pattern.fields.rules
    confidence: high
    canonical_cognee_edge: true
    logistics_only: true
    canonical_edge_type: REQUIRES_RULE
    inverse_edge_type: REQUIRED_BY_QUERY_PATTERN
    materialize_inverse: false
    edge_class: canonical
    source_type: query_pattern
    target_type: rule
```

```yaml
candidate_edge:
  edge_id: edge.query_pattern.logistics.freight_overcharge_check.has_validation_test.validation_test.logistics.required_scope_context
  edge_type: HAS_VALIDATION_TEST
  source: query_pattern.logistics.freight_overcharge_check
  target: validation_test.logistics.required_scope_context
  fields:
    edge_family: execution_guidance
    evidence_basis: query_pattern.fields.validation_tests
    confidence: high
    canonical_cognee_edge: true
    logistics_only: true
    canonical_edge_type: HAS_VALIDATION_TEST
    inverse_edge_type: VALIDATES_QUERY_PATTERN_OR_ENFORCES_RULE
    materialize_inverse: false
    edge_class: canonical
    source_type: query_pattern
    target_type: validation_test
```

```yaml
candidate_edge:
  edge_id: edge.query_pattern.logistics.freight_overcharge_check.has_validation_test.validation_test.logistics.amount_semantics_not_by_name
  edge_type: HAS_VALIDATION_TEST
  source: query_pattern.logistics.freight_overcharge_check
  target: validation_test.logistics.amount_semantics_not_by_name
  fields:
    edge_family: execution_guidance
    evidence_basis: query_pattern.fields.validation_tests
    confidence: high
    canonical_cognee_edge: true
    logistics_only: true
    canonical_edge_type: HAS_VALIDATION_TEST
    inverse_edge_type: VALIDATES_QUERY_PATTERN_OR_ENFORCES_RULE
    materialize_inverse: false
    edge_class: canonical
    source_type: query_pattern
    target_type: validation_test
```

```yaml
candidate_edge:
  edge_id: edge.query_pattern.logistics.freight_overcharge_check.uses_output_contract.output_contract.logistics_reconciliation_summary
  edge_type: USES_OUTPUT_CONTRACT
  source: query_pattern.logistics.freight_overcharge_check
  target: output_contract.logistics_reconciliation_summary
  fields:
    edge_family: execution_guidance
    evidence_basis: query_pattern.fields.output_contracts
    confidence: high
    canonical_cognee_edge: true
    logistics_only: true
    canonical_edge_type: USES_OUTPUT_CONTRACT
    inverse_edge_type: USED_BY_CONTEXT
    materialize_inverse: false
    edge_class: canonical
    source_type: query_pattern
    target_type: output_contract
```

```yaml
candidate_edge:
  edge_id: edge.query_pattern.logistics.cod_expected_vs_remitted.produces_metric.metric.cod_expected_amount
  edge_type: PRODUCES_METRIC
  source: query_pattern.logistics.cod_expected_vs_remitted
  target: metric.cod_expected_amount
  fields:
    edge_family: execution_guidance
    evidence_basis: query_pattern.fields.canonical_metric_or_object
    confidence: high
    canonical_cognee_edge: true
    logistics_only: true
    canonical_edge_type: PRODUCES_METRIC
    inverse_edge_type: PRODUCED_BY_QUERY_PATTERN
    materialize_inverse: false
    edge_class: canonical
    source_type: query_pattern
    target_type: metric
```

```yaml
candidate_edge:
  edge_id: edge.query_pattern.logistics.cod_expected_vs_remitted.produces_metric.metric.cod_remitted_amount
  edge_type: PRODUCES_METRIC
  source: query_pattern.logistics.cod_expected_vs_remitted
  target: metric.cod_remitted_amount
  fields:
    edge_family: execution_guidance
    evidence_basis: query_pattern.fields.canonical_metric_or_object
    confidence: high
    canonical_cognee_edge: true
    logistics_only: true
    canonical_edge_type: PRODUCES_METRIC
    inverse_edge_type: PRODUCED_BY_QUERY_PATTERN
    materialize_inverse: false
    edge_class: canonical
    source_type: query_pattern
    target_type: metric
```

```yaml
candidate_edge:
  edge_id: edge.query_pattern.logistics.cod_expected_vs_remitted.produces_metric.metric.cod_gap_amount
  edge_type: PRODUCES_METRIC
  source: query_pattern.logistics.cod_expected_vs_remitted
  target: metric.cod_gap_amount
  fields:
    edge_family: execution_guidance
    evidence_basis: query_pattern.fields.canonical_metric_or_object
    confidence: high
    canonical_cognee_edge: true
    logistics_only: true
    canonical_edge_type: PRODUCES_METRIC
    inverse_edge_type: PRODUCED_BY_QUERY_PATTERN
    materialize_inverse: false
    edge_class: canonical
    source_type: query_pattern
    target_type: metric
```

```yaml
candidate_edge:
  edge_id: edge.query_pattern.logistics.cod_expected_vs_remitted.uses_reconciliation_profile.reconciliation_profile.cod_expected_to_courier_remittance
  edge_type: USES_RECONCILIATION_PROFILE
  source: query_pattern.logistics.cod_expected_vs_remitted
  target: reconciliation_profile.cod_expected_to_courier_remittance
  fields:
    edge_family: execution_guidance
    evidence_basis: query_pattern.fields.canonical_metric_or_object
    confidence: high
    canonical_cognee_edge: true
    logistics_only: true
    canonical_edge_type: USES_RECONCILIATION_PROFILE
    inverse_edge_type: USED_BY_QUERY_PATTERN
    materialize_inverse: false
    edge_class: canonical
    source_type: query_pattern
    target_type: reconciliation_profile
```

```yaml
candidate_edge:
  edge_id: edge.query_pattern.logistics.cod_expected_vs_remitted.uses_table.table.zs_observe.shiprocket_oms
  edge_type: USES_TABLE
  source: query_pattern.logistics.cod_expected_vs_remitted
  target: table.zs_observe.shiprocket_oms
  fields:
    edge_family: metric_understanding
    evidence_basis: query_pattern.fields.required_tables
    confidence: high
    canonical_cognee_edge: true
    logistics_only: true
    canonical_edge_type: USES_TABLE
    inverse_edge_type: USED_BY_CONTEXT
    materialize_inverse: false
    edge_class: canonical
    source_type: query_pattern
    target_type: table
```

```yaml
candidate_edge:
  edge_id: edge.query_pattern.logistics.cod_expected_vs_remitted.uses_table.table.zs_observe.shiprocket_settlement
  edge_type: USES_TABLE
  source: query_pattern.logistics.cod_expected_vs_remitted
  target: table.zs_observe.shiprocket_settlement
  fields:
    edge_family: metric_understanding
    evidence_basis: query_pattern.fields.required_tables
    confidence: high
    canonical_cognee_edge: true
    logistics_only: true
    canonical_edge_type: USES_TABLE
    inverse_edge_type: USED_BY_CONTEXT
    materialize_inverse: false
    edge_class: canonical
    source_type: query_pattern
    target_type: table
```

```yaml
candidate_edge:
  edge_id: edge.query_pattern.logistics.cod_expected_vs_remitted.requires_rule.rule.logistics.shiprocket_settlement_charged_amount_cod
  edge_type: REQUIRES_RULE
  source: query_pattern.logistics.cod_expected_vs_remitted
  target: rule.logistics.shiprocket_settlement_charged_amount_cod
  fields:
    edge_family: execution_guidance
    evidence_basis: query_pattern.fields.rules
    confidence: high
    canonical_cognee_edge: true
    logistics_only: true
    canonical_edge_type: REQUIRES_RULE
    inverse_edge_type: REQUIRED_BY_QUERY_PATTERN
    materialize_inverse: false
    edge_class: canonical
    source_type: query_pattern
    target_type: rule
```

```yaml
candidate_edge:
  edge_id: edge.query_pattern.logistics.cod_expected_vs_remitted.requires_rule.rule.logistics.delhivery_charged_amount_declared_value
  edge_type: REQUIRES_RULE
  source: query_pattern.logistics.cod_expected_vs_remitted
  target: rule.logistics.delhivery_charged_amount_declared_value
  fields:
    edge_family: execution_guidance
    evidence_basis: query_pattern.fields.rules
    confidence: high
    canonical_cognee_edge: true
    logistics_only: true
    canonical_edge_type: REQUIRES_RULE
    inverse_edge_type: REQUIRED_BY_QUERY_PATTERN
    materialize_inverse: false
    edge_class: canonical
    source_type: query_pattern
    target_type: rule
```

```yaml
candidate_edge:
  edge_id: edge.query_pattern.logistics.cod_expected_vs_remitted.has_validation_test.validation_test.logistics.required_scope_context
  edge_type: HAS_VALIDATION_TEST
  source: query_pattern.logistics.cod_expected_vs_remitted
  target: validation_test.logistics.required_scope_context
  fields:
    edge_family: execution_guidance
    evidence_basis: query_pattern.fields.validation_tests
    confidence: high
    canonical_cognee_edge: true
    logistics_only: true
    canonical_edge_type: HAS_VALIDATION_TEST
    inverse_edge_type: VALIDATES_QUERY_PATTERN_OR_ENFORCES_RULE
    materialize_inverse: false
    edge_class: canonical
    source_type: query_pattern
    target_type: validation_test
```

```yaml
candidate_edge:
  edge_id: edge.query_pattern.logistics.cod_expected_vs_remitted.has_validation_test.validation_test.logistics.amount_semantics_not_by_name
  edge_type: HAS_VALIDATION_TEST
  source: query_pattern.logistics.cod_expected_vs_remitted
  target: validation_test.logistics.amount_semantics_not_by_name
  fields:
    edge_family: execution_guidance
    evidence_basis: query_pattern.fields.validation_tests
    confidence: high
    canonical_cognee_edge: true
    logistics_only: true
    canonical_edge_type: HAS_VALIDATION_TEST
    inverse_edge_type: VALIDATES_QUERY_PATTERN_OR_ENFORCES_RULE
    materialize_inverse: false
    edge_class: canonical
    source_type: query_pattern
    target_type: validation_test
```

```yaml
candidate_edge:
  edge_id: edge.query_pattern.logistics.cod_expected_vs_remitted.uses_output_contract.output_contract.logistics_reconciliation_summary
  edge_type: USES_OUTPUT_CONTRACT
  source: query_pattern.logistics.cod_expected_vs_remitted
  target: output_contract.logistics_reconciliation_summary
  fields:
    edge_family: execution_guidance
    evidence_basis: query_pattern.fields.output_contracts
    confidence: high
    canonical_cognee_edge: true
    logistics_only: true
    canonical_edge_type: USES_OUTPUT_CONTRACT
    inverse_edge_type: USED_BY_CONTEXT
    materialize_inverse: false
    edge_class: canonical
    source_type: query_pattern
    target_type: output_contract
```

```yaml
candidate_edge:
  edge_id: edge.query_pattern.logistics.cod_remittance_lag.produces_metric.metric.cod_remittance_lag_days
  edge_type: PRODUCES_METRIC
  source: query_pattern.logistics.cod_remittance_lag
  target: metric.cod_remittance_lag_days
  fields:
    edge_family: execution_guidance
    evidence_basis: query_pattern.fields.canonical_metric_or_object
    confidence: high
    canonical_cognee_edge: true
    logistics_only: true
    canonical_edge_type: PRODUCES_METRIC
    inverse_edge_type: PRODUCED_BY_QUERY_PATTERN
    materialize_inverse: false
    edge_class: canonical
    source_type: query_pattern
    target_type: metric
```

```yaml
candidate_edge:
  edge_id: edge.query_pattern.logistics.cod_remittance_lag.uses_reconciliation_profile.reconciliation_profile.cod_expected_to_courier_remittance
  edge_type: USES_RECONCILIATION_PROFILE
  source: query_pattern.logistics.cod_remittance_lag
  target: reconciliation_profile.cod_expected_to_courier_remittance
  fields:
    edge_family: execution_guidance
    evidence_basis: query_pattern.fields.canonical_metric_or_object
    confidence: high
    canonical_cognee_edge: true
    logistics_only: true
    canonical_edge_type: USES_RECONCILIATION_PROFILE
    inverse_edge_type: USED_BY_QUERY_PATTERN
    materialize_inverse: false
    edge_class: canonical
    source_type: query_pattern
    target_type: reconciliation_profile
```

```yaml
candidate_edge:
  edge_id: edge.query_pattern.logistics.cod_remittance_lag.uses_table.table.zs_observe.shiprocket_settlement
  edge_type: USES_TABLE
  source: query_pattern.logistics.cod_remittance_lag
  target: table.zs_observe.shiprocket_settlement
  fields:
    edge_family: metric_understanding
    evidence_basis: query_pattern.fields.required_tables
    confidence: high
    canonical_cognee_edge: true
    logistics_only: true
    canonical_edge_type: USES_TABLE
    inverse_edge_type: USED_BY_CONTEXT
    materialize_inverse: false
    edge_class: canonical
    source_type: query_pattern
    target_type: table
```

```yaml
candidate_edge:
  edge_id: edge.query_pattern.logistics.cod_remittance_lag.uses_table.table.zs_observe.ekart_settlement
  edge_type: USES_TABLE
  source: query_pattern.logistics.cod_remittance_lag
  target: table.zs_observe.ekart_settlement
  fields:
    edge_family: metric_understanding
    evidence_basis: query_pattern.fields.required_tables
    confidence: high
    canonical_cognee_edge: true
    logistics_only: true
    canonical_edge_type: USES_TABLE
    inverse_edge_type: USED_BY_CONTEXT
    materialize_inverse: false
    edge_class: canonical
    source_type: query_pattern
    target_type: table
```

```yaml
candidate_edge:
  edge_id: edge.query_pattern.logistics.cod_remittance_lag.uses_table.table.zs_observe.dtdc_settlement
  edge_type: USES_TABLE
  source: query_pattern.logistics.cod_remittance_lag
  target: table.zs_observe.dtdc_settlement
  fields:
    edge_family: metric_understanding
    evidence_basis: query_pattern.fields.required_tables
    confidence: high
    canonical_cognee_edge: true
    logistics_only: true
    canonical_edge_type: USES_TABLE
    inverse_edge_type: USED_BY_CONTEXT
    materialize_inverse: false
    edge_class: canonical
    source_type: query_pattern
    target_type: table
```

```yaml
candidate_edge:
  edge_id: edge.query_pattern.logistics.cod_remittance_lag.requires_rule.rule.logistics.settlement_date_for_cod_remittance
  edge_type: REQUIRES_RULE
  source: query_pattern.logistics.cod_remittance_lag
  target: rule.logistics.settlement_date_for_cod_remittance
  fields:
    edge_family: execution_guidance
    evidence_basis: query_pattern.fields.rules
    confidence: high
    canonical_cognee_edge: true
    logistics_only: true
    canonical_edge_type: REQUIRES_RULE
    inverse_edge_type: REQUIRED_BY_QUERY_PATTERN
    materialize_inverse: false
    edge_class: canonical
    source_type: query_pattern
    target_type: rule
```

```yaml
candidate_edge:
  edge_id: edge.query_pattern.logistics.cod_remittance_lag.requires_rule.rule.logistics.delivered_date_for_delivery_metrics
  edge_type: REQUIRES_RULE
  source: query_pattern.logistics.cod_remittance_lag
  target: rule.logistics.delivered_date_for_delivery_metrics
  fields:
    edge_family: execution_guidance
    evidence_basis: query_pattern.fields.rules
    confidence: high
    canonical_cognee_edge: true
    logistics_only: true
    canonical_edge_type: REQUIRES_RULE
    inverse_edge_type: REQUIRED_BY_QUERY_PATTERN
    materialize_inverse: false
    edge_class: canonical
    source_type: query_pattern
    target_type: rule
```

```yaml
candidate_edge:
  edge_id: edge.query_pattern.logistics.cod_remittance_lag.has_validation_test.validation_test.logistics.required_scope_context
  edge_type: HAS_VALIDATION_TEST
  source: query_pattern.logistics.cod_remittance_lag
  target: validation_test.logistics.required_scope_context
  fields:
    edge_family: execution_guidance
    evidence_basis: query_pattern.fields.validation_tests
    confidence: high
    canonical_cognee_edge: true
    logistics_only: true
    canonical_edge_type: HAS_VALIDATION_TEST
    inverse_edge_type: VALIDATES_QUERY_PATTERN_OR_ENFORCES_RULE
    materialize_inverse: false
    edge_class: canonical
    source_type: query_pattern
    target_type: validation_test
```

```yaml
candidate_edge:
  edge_id: edge.query_pattern.logistics.cod_remittance_lag.has_validation_test.validation_test.logistics.amount_semantics_not_by_name
  edge_type: HAS_VALIDATION_TEST
  source: query_pattern.logistics.cod_remittance_lag
  target: validation_test.logistics.amount_semantics_not_by_name
  fields:
    edge_family: execution_guidance
    evidence_basis: query_pattern.fields.validation_tests
    confidence: high
    canonical_cognee_edge: true
    logistics_only: true
    canonical_edge_type: HAS_VALIDATION_TEST
    inverse_edge_type: VALIDATES_QUERY_PATTERN_OR_ENFORCES_RULE
    materialize_inverse: false
    edge_class: canonical
    source_type: query_pattern
    target_type: validation_test
```

```yaml
candidate_edge:
  edge_id: edge.query_pattern.logistics.cod_remittance_lag.uses_output_contract.output_contract.logistics_metric_summary
  edge_type: USES_OUTPUT_CONTRACT
  source: query_pattern.logistics.cod_remittance_lag
  target: output_contract.logistics_metric_summary
  fields:
    edge_family: execution_guidance
    evidence_basis: query_pattern.fields.output_contracts
    confidence: high
    canonical_cognee_edge: true
    logistics_only: true
    canonical_edge_type: USES_OUTPUT_CONTRACT
    inverse_edge_type: USED_BY_CONTEXT
    materialize_inverse: false
    edge_class: canonical
    source_type: query_pattern
    target_type: output_contract
```

```yaml
candidate_edge:
  edge_id: edge.query_pattern.logistics.courier_batch_to_bank_bridge.produces_metric.metric.batch_settlement_amount
  edge_type: PRODUCES_METRIC
  source: query_pattern.logistics.courier_batch_to_bank_bridge
  target: metric.batch_settlement_amount
  fields:
    edge_family: execution_guidance
    evidence_basis: query_pattern.fields.canonical_metric_or_object
    confidence: high
    canonical_cognee_edge: true
    logistics_only: true
    canonical_edge_type: PRODUCES_METRIC
    inverse_edge_type: PRODUCED_BY_QUERY_PATTERN
    materialize_inverse: false
    edge_class: canonical
    source_type: query_pattern
    target_type: metric
```

```yaml
candidate_edge:
  edge_id: edge.query_pattern.logistics.courier_batch_to_bank_bridge.produces_metric.metric.bank_credit_matched_amount
  edge_type: PRODUCES_METRIC
  source: query_pattern.logistics.courier_batch_to_bank_bridge
  target: metric.bank_credit_matched_amount
  fields:
    edge_family: execution_guidance
    evidence_basis: query_pattern.fields.canonical_metric_or_object
    confidence: high
    canonical_cognee_edge: true
    logistics_only: true
    canonical_edge_type: PRODUCES_METRIC
    inverse_edge_type: PRODUCED_BY_QUERY_PATTERN
    materialize_inverse: false
    edge_class: canonical
    source_type: query_pattern
    target_type: metric
```

```yaml
candidate_edge:
  edge_id: edge.query_pattern.logistics.courier_batch_to_bank_bridge.uses_reconciliation_profile.reconciliation_profile.courier_batch_to_bank_credit
  edge_type: USES_RECONCILIATION_PROFILE
  source: query_pattern.logistics.courier_batch_to_bank_bridge
  target: reconciliation_profile.courier_batch_to_bank_credit
  fields:
    edge_family: execution_guidance
    evidence_basis: query_pattern.fields.canonical_metric_or_object
    confidence: high
    canonical_cognee_edge: true
    logistics_only: true
    canonical_edge_type: USES_RECONCILIATION_PROFILE
    inverse_edge_type: USED_BY_QUERY_PATTERN
    materialize_inverse: false
    edge_class: canonical
    source_type: query_pattern
    target_type: reconciliation_profile
```

```yaml
candidate_edge:
  edge_id: edge.query_pattern.logistics.courier_batch_to_bank_bridge.uses_table.table.zs_observe.delhivery_settlement
  edge_type: USES_TABLE
  source: query_pattern.logistics.courier_batch_to_bank_bridge
  target: table.zs_observe.delhivery_settlement
  fields:
    edge_family: metric_understanding
    evidence_basis: query_pattern.fields.required_tables
    confidence: high
    canonical_cognee_edge: true
    logistics_only: true
    canonical_edge_type: USES_TABLE
    inverse_edge_type: USED_BY_CONTEXT
    materialize_inverse: false
    edge_class: canonical
    source_type: query_pattern
    target_type: table
```

```yaml
candidate_edge:
  edge_id: edge.query_pattern.logistics.courier_batch_to_bank_bridge.uses_table.table.zs_observe.dtdc_settlement
  edge_type: USES_TABLE
  source: query_pattern.logistics.courier_batch_to_bank_bridge
  target: table.zs_observe.dtdc_settlement
  fields:
    edge_family: metric_understanding
    evidence_basis: query_pattern.fields.required_tables
    confidence: high
    canonical_cognee_edge: true
    logistics_only: true
    canonical_edge_type: USES_TABLE
    inverse_edge_type: USED_BY_CONTEXT
    materialize_inverse: false
    edge_class: canonical
    source_type: query_pattern
    target_type: table
```

```yaml
candidate_edge:
  edge_id: edge.query_pattern.logistics.courier_batch_to_bank_bridge.uses_table.table.zs_observe.ekart_settlement
  edge_type: USES_TABLE
  source: query_pattern.logistics.courier_batch_to_bank_bridge
  target: table.zs_observe.ekart_settlement
  fields:
    edge_family: metric_understanding
    evidence_basis: query_pattern.fields.required_tables
    confidence: high
    canonical_cognee_edge: true
    logistics_only: true
    canonical_edge_type: USES_TABLE
    inverse_edge_type: USED_BY_CONTEXT
    materialize_inverse: false
    edge_class: canonical
    source_type: query_pattern
    target_type: table
```

```yaml
candidate_edge:
  edge_id: edge.query_pattern.logistics.courier_batch_to_bank_bridge.requires_rule.rule.logistics.bank_reference_required_for_bank_match
  edge_type: REQUIRES_RULE
  source: query_pattern.logistics.courier_batch_to_bank_bridge
  target: rule.logistics.bank_reference_required_for_bank_match
  fields:
    edge_family: execution_guidance
    evidence_basis: query_pattern.fields.rules
    confidence: high
    canonical_cognee_edge: true
    logistics_only: true
    canonical_edge_type: REQUIRES_RULE
    inverse_edge_type: REQUIRED_BY_QUERY_PATTERN
    materialize_inverse: false
    edge_class: canonical
    source_type: query_pattern
    target_type: rule
```

```yaml
candidate_edge:
  edge_id: edge.query_pattern.logistics.courier_batch_to_bank_bridge.requires_rule.rule.logistics.utr_preferred_for_bank_bridge
  edge_type: REQUIRES_RULE
  source: query_pattern.logistics.courier_batch_to_bank_bridge
  target: rule.logistics.utr_preferred_for_bank_bridge
  fields:
    edge_family: execution_guidance
    evidence_basis: query_pattern.fields.rules
    confidence: high
    canonical_cognee_edge: true
    logistics_only: true
    canonical_edge_type: REQUIRES_RULE
    inverse_edge_type: REQUIRED_BY_QUERY_PATTERN
    materialize_inverse: false
    edge_class: canonical
    source_type: query_pattern
    target_type: rule
```

```yaml
candidate_edge:
  edge_id: edge.query_pattern.logistics.courier_batch_to_bank_bridge.requires_rule.rule.logistics.batch_amount_deduplicate
  edge_type: REQUIRES_RULE
  source: query_pattern.logistics.courier_batch_to_bank_bridge
  target: rule.logistics.batch_amount_deduplicate
  fields:
    edge_family: execution_guidance
    evidence_basis: query_pattern.fields.rules
    confidence: high
    canonical_cognee_edge: true
    logistics_only: true
    canonical_edge_type: REQUIRES_RULE
    inverse_edge_type: REQUIRED_BY_QUERY_PATTERN
    materialize_inverse: false
    edge_class: canonical
    source_type: query_pattern
    target_type: rule
```

```yaml
candidate_edge:
  edge_id: edge.query_pattern.logistics.courier_batch_to_bank_bridge.has_validation_test.validation_test.logistics.required_scope_context
  edge_type: HAS_VALIDATION_TEST
  source: query_pattern.logistics.courier_batch_to_bank_bridge
  target: validation_test.logistics.required_scope_context
  fields:
    edge_family: execution_guidance
    evidence_basis: query_pattern.fields.validation_tests
    confidence: high
    canonical_cognee_edge: true
    logistics_only: true
    canonical_edge_type: HAS_VALIDATION_TEST
    inverse_edge_type: VALIDATES_QUERY_PATTERN_OR_ENFORCES_RULE
    materialize_inverse: false
    edge_class: canonical
    source_type: query_pattern
    target_type: validation_test
```

```yaml
candidate_edge:
  edge_id: edge.query_pattern.logistics.courier_batch_to_bank_bridge.has_validation_test.validation_test.logistics.amount_semantics_not_by_name
  edge_type: HAS_VALIDATION_TEST
  source: query_pattern.logistics.courier_batch_to_bank_bridge
  target: validation_test.logistics.amount_semantics_not_by_name
  fields:
    edge_family: execution_guidance
    evidence_basis: query_pattern.fields.validation_tests
    confidence: high
    canonical_cognee_edge: true
    logistics_only: true
    canonical_edge_type: HAS_VALIDATION_TEST
    inverse_edge_type: VALIDATES_QUERY_PATTERN_OR_ENFORCES_RULE
    materialize_inverse: false
    edge_class: canonical
    source_type: query_pattern
    target_type: validation_test
```

```yaml
candidate_edge:
  edge_id: edge.query_pattern.logistics.courier_batch_to_bank_bridge.uses_output_contract.output_contract.logistics_money_flow_trace
  edge_type: USES_OUTPUT_CONTRACT
  source: query_pattern.logistics.courier_batch_to_bank_bridge
  target: output_contract.logistics_money_flow_trace
  fields:
    edge_family: execution_guidance
    evidence_basis: query_pattern.fields.output_contracts
    confidence: high
    canonical_cognee_edge: true
    logistics_only: true
    canonical_edge_type: USES_OUTPUT_CONTRACT
    inverse_edge_type: USED_BY_CONTEXT
    materialize_inverse: false
    edge_class: canonical
    source_type: query_pattern
    target_type: output_contract
```

```yaml
candidate_edge:
  edge_id: edge.query_pattern.logistics.low_confidence_native_validation.produces_metric.metric.populated_native_record_count
  edge_type: PRODUCES_METRIC
  source: query_pattern.logistics.low_confidence_native_validation
  target: metric.populated_native_record_count
  fields:
    edge_family: execution_guidance
    evidence_basis: query_pattern.fields.canonical_metric_or_object
    confidence: high
    canonical_cognee_edge: true
    logistics_only: true
    canonical_edge_type: PRODUCES_METRIC
    inverse_edge_type: PRODUCED_BY_QUERY_PATTERN
    materialize_inverse: false
    edge_class: canonical
    source_type: query_pattern
    target_type: metric
```

```yaml
candidate_edge:
  edge_id: edge.query_pattern.logistics.low_confidence_native_validation.uses_table.table.zs_observe.xpressbees_settlement
  edge_type: USES_TABLE
  source: query_pattern.logistics.low_confidence_native_validation
  target: table.zs_observe.xpressbees_settlement
  fields:
    edge_family: metric_understanding
    evidence_basis: query_pattern.fields.required_tables
    confidence: high
    canonical_cognee_edge: true
    logistics_only: true
    canonical_edge_type: USES_TABLE
    inverse_edge_type: USED_BY_CONTEXT
    materialize_inverse: false
    edge_class: canonical
    source_type: query_pattern
    target_type: table
```

```yaml
candidate_edge:
  edge_id: edge.query_pattern.logistics.low_confidence_native_validation.requires_rule.rule.logistics.low_confidence_requires_warning
  edge_type: REQUIRES_RULE
  source: query_pattern.logistics.low_confidence_native_validation
  target: rule.logistics.low_confidence_requires_warning
  fields:
    edge_family: execution_guidance
    evidence_basis: query_pattern.fields.rules
    confidence: high
    canonical_cognee_edge: true
    logistics_only: true
    canonical_edge_type: REQUIRES_RULE
    inverse_edge_type: REQUIRED_BY_QUERY_PATTERN
    materialize_inverse: false
    edge_class: canonical
    source_type: query_pattern
    target_type: rule
```

```yaml
candidate_edge:
  edge_id: edge.query_pattern.logistics.low_confidence_native_validation.requires_rule.rule.logistics.xpressbees_native_low_confidence
  edge_type: REQUIRES_RULE
  source: query_pattern.logistics.low_confidence_native_validation
  target: rule.logistics.xpressbees_native_low_confidence
  fields:
    edge_family: execution_guidance
    evidence_basis: query_pattern.fields.rules
    confidence: high
    canonical_cognee_edge: true
    logistics_only: true
    canonical_edge_type: REQUIRES_RULE
    inverse_edge_type: REQUIRED_BY_QUERY_PATTERN
    materialize_inverse: false
    edge_class: canonical
    source_type: query_pattern
    target_type: rule
```

```yaml
candidate_edge:
  edge_id: edge.query_pattern.logistics.low_confidence_native_validation.requires_rule.rule.logistics.xpressbees_fallback_shiprocket_preferred
  edge_type: REQUIRES_RULE
  source: query_pattern.logistics.low_confidence_native_validation
  target: rule.logistics.xpressbees_fallback_shiprocket_preferred
  fields:
    edge_family: execution_guidance
    evidence_basis: query_pattern.fields.rules
    confidence: high
    canonical_cognee_edge: true
    logistics_only: true
    canonical_edge_type: REQUIRES_RULE
    inverse_edge_type: REQUIRED_BY_QUERY_PATTERN
    materialize_inverse: false
    edge_class: canonical
    source_type: query_pattern
    target_type: rule
```

```yaml
candidate_edge:
  edge_id: edge.query_pattern.logistics.low_confidence_native_validation.has_validation_test.validation_test.logistics.required_scope_context
  edge_type: HAS_VALIDATION_TEST
  source: query_pattern.logistics.low_confidence_native_validation
  target: validation_test.logistics.required_scope_context
  fields:
    edge_family: execution_guidance
    evidence_basis: query_pattern.fields.validation_tests
    confidence: high
    canonical_cognee_edge: true
    logistics_only: true
    canonical_edge_type: HAS_VALIDATION_TEST
    inverse_edge_type: VALIDATES_QUERY_PATTERN_OR_ENFORCES_RULE
    materialize_inverse: false
    edge_class: canonical
    source_type: query_pattern
    target_type: validation_test
```

```yaml
candidate_edge:
  edge_id: edge.query_pattern.logistics.low_confidence_native_validation.has_validation_test.validation_test.logistics.amount_semantics_not_by_name
  edge_type: HAS_VALIDATION_TEST
  source: query_pattern.logistics.low_confidence_native_validation
  target: validation_test.logistics.amount_semantics_not_by_name
  fields:
    edge_family: execution_guidance
    evidence_basis: query_pattern.fields.validation_tests
    confidence: high
    canonical_cognee_edge: true
    logistics_only: true
    canonical_edge_type: HAS_VALIDATION_TEST
    inverse_edge_type: VALIDATES_QUERY_PATTERN_OR_ENFORCES_RULE
    materialize_inverse: false
    edge_class: canonical
    source_type: query_pattern
    target_type: validation_test
```

```yaml
candidate_edge:
  edge_id: edge.query_pattern.logistics.low_confidence_native_validation.uses_output_contract.output_contract.logistics_data_quality_report
  edge_type: USES_OUTPUT_CONTRACT
  source: query_pattern.logistics.low_confidence_native_validation
  target: output_contract.logistics_data_quality_report
  fields:
    edge_family: execution_guidance
    evidence_basis: query_pattern.fields.output_contracts
    confidence: high
    canonical_cognee_edge: true
    logistics_only: true
    canonical_edge_type: USES_OUTPUT_CONTRACT
    inverse_edge_type: USED_BY_CONTEXT
    materialize_inverse: false
    edge_class: canonical
    source_type: query_pattern
    target_type: output_contract
```

```yaml
candidate_edge:
  edge_id: edge.query_pattern.logistics.shiprocket_courier_partner_freight_split.produces_metric.metric.freight_billed_amount
  edge_type: PRODUCES_METRIC
  source: query_pattern.logistics.shiprocket_courier_partner_freight_split
  target: metric.freight_billed_amount
  fields:
    edge_family: execution_guidance
    evidence_basis: query_pattern.fields.canonical_metric_or_object
    confidence: high
    canonical_cognee_edge: true
    logistics_only: true
    canonical_edge_type: PRODUCES_METRIC
    inverse_edge_type: PRODUCED_BY_QUERY_PATTERN
    materialize_inverse: false
    edge_class: canonical
    source_type: query_pattern
    target_type: metric
```

```yaml
candidate_edge:
  edge_id: edge.query_pattern.logistics.shiprocket_courier_partner_freight_split.produces_metric.metric.average_freight_per_awb
  edge_type: PRODUCES_METRIC
  source: query_pattern.logistics.shiprocket_courier_partner_freight_split
  target: metric.average_freight_per_awb
  fields:
    edge_family: execution_guidance
    evidence_basis: query_pattern.fields.canonical_metric_or_object
    confidence: high
    canonical_cognee_edge: true
    logistics_only: true
    canonical_edge_type: PRODUCES_METRIC
    inverse_edge_type: PRODUCED_BY_QUERY_PATTERN
    materialize_inverse: false
    edge_class: canonical
    source_type: query_pattern
    target_type: metric
```

```yaml
candidate_edge:
  edge_id: edge.query_pattern.logistics.shiprocket_courier_partner_freight_split.uses_reconciliation_profile.reconciliation_profile.shipment_to_freight_invoice
  edge_type: USES_RECONCILIATION_PROFILE
  source: query_pattern.logistics.shiprocket_courier_partner_freight_split
  target: reconciliation_profile.shipment_to_freight_invoice
  fields:
    edge_family: execution_guidance
    evidence_basis: query_pattern.fields.canonical_metric_or_object
    confidence: high
    canonical_cognee_edge: true
    logistics_only: true
    canonical_edge_type: USES_RECONCILIATION_PROFILE
    inverse_edge_type: USED_BY_QUERY_PATTERN
    materialize_inverse: false
    edge_class: canonical
    source_type: query_pattern
    target_type: reconciliation_profile
```

```yaml
candidate_edge:
  edge_id: edge.query_pattern.logistics.shiprocket_courier_partner_freight_split.uses_table.table.zs_observe.shiprocket_invoice
  edge_type: USES_TABLE
  source: query_pattern.logistics.shiprocket_courier_partner_freight_split
  target: table.zs_observe.shiprocket_invoice
  fields:
    edge_family: metric_understanding
    evidence_basis: query_pattern.fields.required_tables
    confidence: high
    canonical_cognee_edge: true
    logistics_only: true
    canonical_edge_type: USES_TABLE
    inverse_edge_type: USED_BY_CONTEXT
    materialize_inverse: false
    edge_class: canonical
    source_type: query_pattern
    target_type: table
```

```yaml
candidate_edge:
  edge_id: edge.query_pattern.logistics.shiprocket_courier_partner_freight_split.requires_rule.rule.logistics.courier_partner_filter_exact_or_profiled
  edge_type: REQUIRES_RULE
  source: query_pattern.logistics.shiprocket_courier_partner_freight_split
  target: rule.logistics.courier_partner_filter_exact_or_profiled
  fields:
    edge_family: execution_guidance
    evidence_basis: query_pattern.fields.rules
    confidence: high
    canonical_cognee_edge: true
    logistics_only: true
    canonical_edge_type: REQUIRES_RULE
    inverse_edge_type: REQUIRED_BY_QUERY_PATTERN
    materialize_inverse: false
    edge_class: canonical
    source_type: query_pattern
    target_type: rule
```

```yaml
candidate_edge:
  edge_id: edge.query_pattern.logistics.shiprocket_courier_partner_freight_split.requires_rule.rule.logistics.shiprocket_invoice_charged_amount_freight
  edge_type: REQUIRES_RULE
  source: query_pattern.logistics.shiprocket_courier_partner_freight_split
  target: rule.logistics.shiprocket_invoice_charged_amount_freight
  fields:
    edge_family: execution_guidance
    evidence_basis: query_pattern.fields.rules
    confidence: high
    canonical_cognee_edge: true
    logistics_only: true
    canonical_edge_type: REQUIRES_RULE
    inverse_edge_type: REQUIRED_BY_QUERY_PATTERN
    materialize_inverse: false
    edge_class: canonical
    source_type: query_pattern
    target_type: rule
```

```yaml
candidate_edge:
  edge_id: edge.query_pattern.logistics.shiprocket_courier_partner_freight_split.has_validation_test.validation_test.logistics.required_scope_context
  edge_type: HAS_VALIDATION_TEST
  source: query_pattern.logistics.shiprocket_courier_partner_freight_split
  target: validation_test.logistics.required_scope_context
  fields:
    edge_family: execution_guidance
    evidence_basis: query_pattern.fields.validation_tests
    confidence: high
    canonical_cognee_edge: true
    logistics_only: true
    canonical_edge_type: HAS_VALIDATION_TEST
    inverse_edge_type: VALIDATES_QUERY_PATTERN_OR_ENFORCES_RULE
    materialize_inverse: false
    edge_class: canonical
    source_type: query_pattern
    target_type: validation_test
```

```yaml
candidate_edge:
  edge_id: edge.query_pattern.logistics.shiprocket_courier_partner_freight_split.has_validation_test.validation_test.logistics.amount_semantics_not_by_name
  edge_type: HAS_VALIDATION_TEST
  source: query_pattern.logistics.shiprocket_courier_partner_freight_split
  target: validation_test.logistics.amount_semantics_not_by_name
  fields:
    edge_family: execution_guidance
    evidence_basis: query_pattern.fields.validation_tests
    confidence: high
    canonical_cognee_edge: true
    logistics_only: true
    canonical_edge_type: HAS_VALIDATION_TEST
    inverse_edge_type: VALIDATES_QUERY_PATTERN_OR_ENFORCES_RULE
    materialize_inverse: false
    edge_class: canonical
    source_type: query_pattern
    target_type: validation_test
```

```yaml
candidate_edge:
  edge_id: edge.query_pattern.logistics.shiprocket_courier_partner_freight_split.uses_output_contract.output_contract.logistics_metric_summary
  edge_type: USES_OUTPUT_CONTRACT
  source: query_pattern.logistics.shiprocket_courier_partner_freight_split
  target: output_contract.logistics_metric_summary
  fields:
    edge_family: execution_guidance
    evidence_basis: query_pattern.fields.output_contracts
    confidence: high
    canonical_cognee_edge: true
    logistics_only: true
    canonical_edge_type: USES_OUTPUT_CONTRACT
    inverse_edge_type: USED_BY_CONTEXT
    materialize_inverse: false
    edge_class: canonical
    source_type: query_pattern
    target_type: output_contract
```

```yaml
candidate_edge:
  edge_id: edge.query_pattern.logistics.shiprocket_cod_by_underlying_courier.produces_metric.metric.cod_remitted_amount
  edge_type: PRODUCES_METRIC
  source: query_pattern.logistics.shiprocket_cod_by_underlying_courier
  target: metric.cod_remitted_amount
  fields:
    edge_family: execution_guidance
    evidence_basis: query_pattern.fields.canonical_metric_or_object
    confidence: high
    canonical_cognee_edge: true
    logistics_only: true
    canonical_edge_type: PRODUCES_METRIC
    inverse_edge_type: PRODUCED_BY_QUERY_PATTERN
    materialize_inverse: false
    edge_class: canonical
    source_type: query_pattern
    target_type: metric
```

```yaml
candidate_edge:
  edge_id: edge.query_pattern.logistics.shiprocket_cod_by_underlying_courier.produces_metric.metric.cod_remittance_lag_days
  edge_type: PRODUCES_METRIC
  source: query_pattern.logistics.shiprocket_cod_by_underlying_courier
  target: metric.cod_remittance_lag_days
  fields:
    edge_family: execution_guidance
    evidence_basis: query_pattern.fields.canonical_metric_or_object
    confidence: high
    canonical_cognee_edge: true
    logistics_only: true
    canonical_edge_type: PRODUCES_METRIC
    inverse_edge_type: PRODUCED_BY_QUERY_PATTERN
    materialize_inverse: false
    edge_class: canonical
    source_type: query_pattern
    target_type: metric
```

```yaml
candidate_edge:
  edge_id: edge.query_pattern.logistics.shiprocket_cod_by_underlying_courier.uses_reconciliation_profile.reconciliation_profile.cod_expected_to_courier_remittance
  edge_type: USES_RECONCILIATION_PROFILE
  source: query_pattern.logistics.shiprocket_cod_by_underlying_courier
  target: reconciliation_profile.cod_expected_to_courier_remittance
  fields:
    edge_family: execution_guidance
    evidence_basis: query_pattern.fields.canonical_metric_or_object
    confidence: high
    canonical_cognee_edge: true
    logistics_only: true
    canonical_edge_type: USES_RECONCILIATION_PROFILE
    inverse_edge_type: USED_BY_QUERY_PATTERN
    materialize_inverse: false
    edge_class: canonical
    source_type: query_pattern
    target_type: reconciliation_profile
```

```yaml
candidate_edge:
  edge_id: edge.query_pattern.logistics.shiprocket_cod_by_underlying_courier.uses_table.table.zs_observe.shiprocket_settlement
  edge_type: USES_TABLE
  source: query_pattern.logistics.shiprocket_cod_by_underlying_courier
  target: table.zs_observe.shiprocket_settlement
  fields:
    edge_family: metric_understanding
    evidence_basis: query_pattern.fields.required_tables
    confidence: high
    canonical_cognee_edge: true
    logistics_only: true
    canonical_edge_type: USES_TABLE
    inverse_edge_type: USED_BY_CONTEXT
    materialize_inverse: false
    edge_class: canonical
    source_type: query_pattern
    target_type: table
```

```yaml
candidate_edge:
  edge_id: edge.query_pattern.logistics.shiprocket_cod_by_underlying_courier.requires_rule.rule.logistics.courier_partner_filter_exact_or_profiled
  edge_type: REQUIRES_RULE
  source: query_pattern.logistics.shiprocket_cod_by_underlying_courier
  target: rule.logistics.courier_partner_filter_exact_or_profiled
  fields:
    edge_family: execution_guidance
    evidence_basis: query_pattern.fields.rules
    confidence: high
    canonical_cognee_edge: true
    logistics_only: true
    canonical_edge_type: REQUIRES_RULE
    inverse_edge_type: REQUIRED_BY_QUERY_PATTERN
    materialize_inverse: false
    edge_class: canonical
    source_type: query_pattern
    target_type: rule
```

```yaml
candidate_edge:
  edge_id: edge.query_pattern.logistics.shiprocket_cod_by_underlying_courier.requires_rule.rule.logistics.shiprocket_settlement_charged_amount_cod
  edge_type: REQUIRES_RULE
  source: query_pattern.logistics.shiprocket_cod_by_underlying_courier
  target: rule.logistics.shiprocket_settlement_charged_amount_cod
  fields:
    edge_family: execution_guidance
    evidence_basis: query_pattern.fields.rules
    confidence: high
    canonical_cognee_edge: true
    logistics_only: true
    canonical_edge_type: REQUIRES_RULE
    inverse_edge_type: REQUIRED_BY_QUERY_PATTERN
    materialize_inverse: false
    edge_class: canonical
    source_type: query_pattern
    target_type: rule
```

```yaml
candidate_edge:
  edge_id: edge.query_pattern.logistics.shiprocket_cod_by_underlying_courier.has_validation_test.validation_test.logistics.required_scope_context
  edge_type: HAS_VALIDATION_TEST
  source: query_pattern.logistics.shiprocket_cod_by_underlying_courier
  target: validation_test.logistics.required_scope_context
  fields:
    edge_family: execution_guidance
    evidence_basis: query_pattern.fields.validation_tests
    confidence: high
    canonical_cognee_edge: true
    logistics_only: true
    canonical_edge_type: HAS_VALIDATION_TEST
    inverse_edge_type: VALIDATES_QUERY_PATTERN_OR_ENFORCES_RULE
    materialize_inverse: false
    edge_class: canonical
    source_type: query_pattern
    target_type: validation_test
```

```yaml
candidate_edge:
  edge_id: edge.query_pattern.logistics.shiprocket_cod_by_underlying_courier.has_validation_test.validation_test.logistics.amount_semantics_not_by_name
  edge_type: HAS_VALIDATION_TEST
  source: query_pattern.logistics.shiprocket_cod_by_underlying_courier
  target: validation_test.logistics.amount_semantics_not_by_name
  fields:
    edge_family: execution_guidance
    evidence_basis: query_pattern.fields.validation_tests
    confidence: high
    canonical_cognee_edge: true
    logistics_only: true
    canonical_edge_type: HAS_VALIDATION_TEST
    inverse_edge_type: VALIDATES_QUERY_PATTERN_OR_ENFORCES_RULE
    materialize_inverse: false
    edge_class: canonical
    source_type: query_pattern
    target_type: validation_test
```

```yaml
candidate_edge:
  edge_id: edge.query_pattern.logistics.shiprocket_cod_by_underlying_courier.uses_output_contract.output_contract.logistics_metric_summary
  edge_type: USES_OUTPUT_CONTRACT
  source: query_pattern.logistics.shiprocket_cod_by_underlying_courier
  target: output_contract.logistics_metric_summary
  fields:
    edge_family: execution_guidance
    evidence_basis: query_pattern.fields.output_contracts
    confidence: high
    canonical_cognee_edge: true
    logistics_only: true
    canonical_edge_type: USES_OUTPUT_CONTRACT
    inverse_edge_type: USED_BY_CONTEXT
    materialize_inverse: false
    edge_class: canonical
    source_type: query_pattern
    target_type: output_contract
```

```yaml
candidate_edge:
  edge_id: edge.query_pattern.logistics.delhivery_freight_component_reconciliation.produces_metric.metric.freight_billed_amount
  edge_type: PRODUCES_METRIC
  source: query_pattern.logistics.delhivery_freight_component_reconciliation
  target: metric.freight_billed_amount
  fields:
    edge_family: execution_guidance
    evidence_basis: query_pattern.fields.canonical_metric_or_object
    confidence: high
    canonical_cognee_edge: true
    logistics_only: true
    canonical_edge_type: PRODUCES_METRIC
    inverse_edge_type: PRODUCED_BY_QUERY_PATTERN
    materialize_inverse: false
    edge_class: canonical
    source_type: query_pattern
    target_type: metric
```

```yaml
candidate_edge:
  edge_id: edge.query_pattern.logistics.delhivery_freight_component_reconciliation.produces_metric.metric.forward_freight_amount
  edge_type: PRODUCES_METRIC
  source: query_pattern.logistics.delhivery_freight_component_reconciliation
  target: metric.forward_freight_amount
  fields:
    edge_family: execution_guidance
    evidence_basis: query_pattern.fields.canonical_metric_or_object
    confidence: high
    canonical_cognee_edge: true
    logistics_only: true
    canonical_edge_type: PRODUCES_METRIC
    inverse_edge_type: PRODUCED_BY_QUERY_PATTERN
    materialize_inverse: false
    edge_class: canonical
    source_type: query_pattern
    target_type: metric
```

```yaml
candidate_edge:
  edge_id: edge.query_pattern.logistics.delhivery_freight_component_reconciliation.produces_metric.metric.rto_freight_amount
  edge_type: PRODUCES_METRIC
  source: query_pattern.logistics.delhivery_freight_component_reconciliation
  target: metric.rto_freight_amount
  fields:
    edge_family: execution_guidance
    evidence_basis: query_pattern.fields.canonical_metric_or_object
    confidence: high
    canonical_cognee_edge: true
    logistics_only: true
    canonical_edge_type: PRODUCES_METRIC
    inverse_edge_type: PRODUCED_BY_QUERY_PATTERN
    materialize_inverse: false
    edge_class: canonical
    source_type: query_pattern
    target_type: metric
```

```yaml
candidate_edge:
  edge_id: edge.query_pattern.logistics.delhivery_freight_component_reconciliation.produces_metric.metric.cod_fee_amount
  edge_type: PRODUCES_METRIC
  source: query_pattern.logistics.delhivery_freight_component_reconciliation
  target: metric.cod_fee_amount
  fields:
    edge_family: execution_guidance
    evidence_basis: query_pattern.fields.canonical_metric_or_object
    confidence: high
    canonical_cognee_edge: true
    logistics_only: true
    canonical_edge_type: PRODUCES_METRIC
    inverse_edge_type: PRODUCED_BY_QUERY_PATTERN
    materialize_inverse: false
    edge_class: canonical
    source_type: query_pattern
    target_type: metric
```

```yaml
candidate_edge:
  edge_id: edge.query_pattern.logistics.delhivery_freight_component_reconciliation.uses_reconciliation_profile.reconciliation_profile.freight_charge_validation
  edge_type: USES_RECONCILIATION_PROFILE
  source: query_pattern.logistics.delhivery_freight_component_reconciliation
  target: reconciliation_profile.freight_charge_validation
  fields:
    edge_family: execution_guidance
    evidence_basis: query_pattern.fields.canonical_metric_or_object
    confidence: high
    canonical_cognee_edge: true
    logistics_only: true
    canonical_edge_type: USES_RECONCILIATION_PROFILE
    inverse_edge_type: USED_BY_QUERY_PATTERN
    materialize_inverse: false
    edge_class: canonical
    source_type: query_pattern
    target_type: reconciliation_profile
```

```yaml
candidate_edge:
  edge_id: edge.query_pattern.logistics.delhivery_freight_component_reconciliation.uses_table.table.zs_observe.delhivery_invoice
  edge_type: USES_TABLE
  source: query_pattern.logistics.delhivery_freight_component_reconciliation
  target: table.zs_observe.delhivery_invoice
  fields:
    edge_family: metric_understanding
    evidence_basis: query_pattern.fields.required_tables
    confidence: high
    canonical_cognee_edge: true
    logistics_only: true
    canonical_edge_type: USES_TABLE
    inverse_edge_type: USED_BY_CONTEXT
    materialize_inverse: false
    edge_class: canonical
    source_type: query_pattern
    target_type: table
```

```yaml
candidate_edge:
  edge_id: edge.query_pattern.logistics.delhivery_freight_component_reconciliation.requires_rule.rule.logistics.delhivery_charged_amount_declared_value
  edge_type: REQUIRES_RULE
  source: query_pattern.logistics.delhivery_freight_component_reconciliation
  target: rule.logistics.delhivery_charged_amount_declared_value
  fields:
    edge_family: execution_guidance
    evidence_basis: query_pattern.fields.rules
    confidence: high
    canonical_cognee_edge: true
    logistics_only: true
    canonical_edge_type: REQUIRES_RULE
    inverse_edge_type: REQUIRED_BY_QUERY_PATTERN
    materialize_inverse: false
    edge_class: canonical
    source_type: query_pattern
    target_type: rule
```

```yaml
candidate_edge:
  edge_id: edge.query_pattern.logistics.delhivery_freight_component_reconciliation.requires_rule.rule.logistics.preaggregate_before_order_join
  edge_type: REQUIRES_RULE
  source: query_pattern.logistics.delhivery_freight_component_reconciliation
  target: rule.logistics.preaggregate_before_order_join
  fields:
    edge_family: execution_guidance
    evidence_basis: query_pattern.fields.rules
    confidence: high
    canonical_cognee_edge: true
    logistics_only: true
    canonical_edge_type: REQUIRES_RULE
    inverse_edge_type: REQUIRED_BY_QUERY_PATTERN
    materialize_inverse: false
    edge_class: canonical
    source_type: query_pattern
    target_type: rule
```

```yaml
candidate_edge:
  edge_id: edge.query_pattern.logistics.delhivery_freight_component_reconciliation.has_validation_test.validation_test.logistics.required_scope_context
  edge_type: HAS_VALIDATION_TEST
  source: query_pattern.logistics.delhivery_freight_component_reconciliation
  target: validation_test.logistics.required_scope_context
  fields:
    edge_family: execution_guidance
    evidence_basis: query_pattern.fields.validation_tests
    confidence: high
    canonical_cognee_edge: true
    logistics_only: true
    canonical_edge_type: HAS_VALIDATION_TEST
    inverse_edge_type: VALIDATES_QUERY_PATTERN_OR_ENFORCES_RULE
    materialize_inverse: false
    edge_class: canonical
    source_type: query_pattern
    target_type: validation_test
```

```yaml
candidate_edge:
  edge_id: edge.query_pattern.logistics.delhivery_freight_component_reconciliation.has_validation_test.validation_test.logistics.amount_semantics_not_by_name
  edge_type: HAS_VALIDATION_TEST
  source: query_pattern.logistics.delhivery_freight_component_reconciliation
  target: validation_test.logistics.amount_semantics_not_by_name
  fields:
    edge_family: execution_guidance
    evidence_basis: query_pattern.fields.validation_tests
    confidence: high
    canonical_cognee_edge: true
    logistics_only: true
    canonical_edge_type: HAS_VALIDATION_TEST
    inverse_edge_type: VALIDATES_QUERY_PATTERN_OR_ENFORCES_RULE
    materialize_inverse: false
    edge_class: canonical
    source_type: query_pattern
    target_type: validation_test
```

```yaml
candidate_edge:
  edge_id: edge.query_pattern.logistics.delhivery_freight_component_reconciliation.uses_output_contract.output_contract.logistics_reconciliation_summary
  edge_type: USES_OUTPUT_CONTRACT
  source: query_pattern.logistics.delhivery_freight_component_reconciliation
  target: output_contract.logistics_reconciliation_summary
  fields:
    edge_family: execution_guidance
    evidence_basis: query_pattern.fields.output_contracts
    confidence: high
    canonical_cognee_edge: true
    logistics_only: true
    canonical_edge_type: USES_OUTPUT_CONTRACT
    inverse_edge_type: USED_BY_CONTEXT
    materialize_inverse: false
    edge_class: canonical
    source_type: query_pattern
    target_type: output_contract
```

```yaml
candidate_edge:
  edge_id: edge.query_pattern.logistics.delhivery_cod_qr_vs_cash.produces_metric.metric.cod_remitted_amount
  edge_type: PRODUCES_METRIC
  source: query_pattern.logistics.delhivery_cod_qr_vs_cash
  target: metric.cod_remitted_amount
  fields:
    edge_family: execution_guidance
    evidence_basis: query_pattern.fields.canonical_metric_or_object
    confidence: high
    canonical_cognee_edge: true
    logistics_only: true
    canonical_edge_type: PRODUCES_METRIC
    inverse_edge_type: PRODUCED_BY_QUERY_PATTERN
    materialize_inverse: false
    edge_class: canonical
    source_type: query_pattern
    target_type: metric
```

```yaml
candidate_edge:
  edge_id: edge.query_pattern.logistics.delhivery_cod_qr_vs_cash.produces_metric.metric.payable_amount
  edge_type: PRODUCES_METRIC
  source: query_pattern.logistics.delhivery_cod_qr_vs_cash
  target: metric.payable_amount
  fields:
    edge_family: execution_guidance
    evidence_basis: query_pattern.fields.canonical_metric_or_object
    confidence: high
    canonical_cognee_edge: true
    logistics_only: true
    canonical_edge_type: PRODUCES_METRIC
    inverse_edge_type: PRODUCED_BY_QUERY_PATTERN
    materialize_inverse: false
    edge_class: canonical
    source_type: query_pattern
    target_type: metric
```

```yaml
candidate_edge:
  edge_id: edge.query_pattern.logistics.delhivery_cod_qr_vs_cash.uses_reconciliation_profile.reconciliation_profile.cod_expected_to_courier_remittance
  edge_type: USES_RECONCILIATION_PROFILE
  source: query_pattern.logistics.delhivery_cod_qr_vs_cash
  target: reconciliation_profile.cod_expected_to_courier_remittance
  fields:
    edge_family: execution_guidance
    evidence_basis: query_pattern.fields.canonical_metric_or_object
    confidence: high
    canonical_cognee_edge: true
    logistics_only: true
    canonical_edge_type: USES_RECONCILIATION_PROFILE
    inverse_edge_type: USED_BY_QUERY_PATTERN
    materialize_inverse: false
    edge_class: canonical
    source_type: query_pattern
    target_type: reconciliation_profile
```

```yaml
candidate_edge:
  edge_id: edge.query_pattern.logistics.delhivery_cod_qr_vs_cash.uses_table.table.zs_observe.delhivery_settlement
  edge_type: USES_TABLE
  source: query_pattern.logistics.delhivery_cod_qr_vs_cash
  target: table.zs_observe.delhivery_settlement
  fields:
    edge_family: metric_understanding
    evidence_basis: query_pattern.fields.required_tables
    confidence: high
    canonical_cognee_edge: true
    logistics_only: true
    canonical_edge_type: USES_TABLE
    inverse_edge_type: USED_BY_CONTEXT
    materialize_inverse: false
    edge_class: canonical
    source_type: query_pattern
    target_type: table
```

```yaml
candidate_edge:
  edge_id: edge.query_pattern.logistics.delhivery_cod_qr_vs_cash.requires_rule.rule.logistics.qr_cod_separate_from_cash
  edge_type: REQUIRES_RULE
  source: query_pattern.logistics.delhivery_cod_qr_vs_cash
  target: rule.logistics.qr_cod_separate_from_cash
  fields:
    edge_family: execution_guidance
    evidence_basis: query_pattern.fields.rules
    confidence: high
    canonical_cognee_edge: true
    logistics_only: true
    canonical_edge_type: REQUIRES_RULE
    inverse_edge_type: REQUIRED_BY_QUERY_PATTERN
    materialize_inverse: false
    edge_class: canonical
    source_type: query_pattern
    target_type: rule
```

```yaml
candidate_edge:
  edge_id: edge.query_pattern.logistics.delhivery_cod_qr_vs_cash.has_validation_test.validation_test.logistics.required_scope_context
  edge_type: HAS_VALIDATION_TEST
  source: query_pattern.logistics.delhivery_cod_qr_vs_cash
  target: validation_test.logistics.required_scope_context
  fields:
    edge_family: execution_guidance
    evidence_basis: query_pattern.fields.validation_tests
    confidence: high
    canonical_cognee_edge: true
    logistics_only: true
    canonical_edge_type: HAS_VALIDATION_TEST
    inverse_edge_type: VALIDATES_QUERY_PATTERN_OR_ENFORCES_RULE
    materialize_inverse: false
    edge_class: canonical
    source_type: query_pattern
    target_type: validation_test
```

```yaml
candidate_edge:
  edge_id: edge.query_pattern.logistics.delhivery_cod_qr_vs_cash.has_validation_test.validation_test.logistics.amount_semantics_not_by_name
  edge_type: HAS_VALIDATION_TEST
  source: query_pattern.logistics.delhivery_cod_qr_vs_cash
  target: validation_test.logistics.amount_semantics_not_by_name
  fields:
    edge_family: execution_guidance
    evidence_basis: query_pattern.fields.validation_tests
    confidence: high
    canonical_cognee_edge: true
    logistics_only: true
    canonical_edge_type: HAS_VALIDATION_TEST
    inverse_edge_type: VALIDATES_QUERY_PATTERN_OR_ENFORCES_RULE
    materialize_inverse: false
    edge_class: canonical
    source_type: query_pattern
    target_type: validation_test
```

```yaml
candidate_edge:
  edge_id: edge.query_pattern.logistics.delhivery_cod_qr_vs_cash.uses_output_contract.output_contract.logistics_metric_summary
  edge_type: USES_OUTPUT_CONTRACT
  source: query_pattern.logistics.delhivery_cod_qr_vs_cash
  target: output_contract.logistics_metric_summary
  fields:
    edge_family: execution_guidance
    evidence_basis: query_pattern.fields.output_contracts
    confidence: high
    canonical_cognee_edge: true
    logistics_only: true
    canonical_edge_type: USES_OUTPUT_CONTRACT
    inverse_edge_type: USED_BY_CONTEXT
    materialize_inverse: false
    edge_class: canonical
    source_type: query_pattern
    target_type: output_contract
```

```yaml
candidate_edge:
  edge_id: edge.query_pattern.logistics.dtdc_settlement_to_shiprocket_freight_fallback.produces_metric.metric.cod_remitted_amount
  edge_type: PRODUCES_METRIC
  source: query_pattern.logistics.dtdc_settlement_to_shiprocket_freight_fallback
  target: metric.cod_remitted_amount
  fields:
    edge_family: execution_guidance
    evidence_basis: query_pattern.fields.canonical_metric_or_object
    confidence: high
    canonical_cognee_edge: true
    logistics_only: true
    canonical_edge_type: PRODUCES_METRIC
    inverse_edge_type: PRODUCED_BY_QUERY_PATTERN
    materialize_inverse: false
    edge_class: canonical
    source_type: query_pattern
    target_type: metric
```

```yaml
candidate_edge:
  edge_id: edge.query_pattern.logistics.dtdc_settlement_to_shiprocket_freight_fallback.produces_metric.metric.freight_billed_amount
  edge_type: PRODUCES_METRIC
  source: query_pattern.logistics.dtdc_settlement_to_shiprocket_freight_fallback
  target: metric.freight_billed_amount
  fields:
    edge_family: execution_guidance
    evidence_basis: query_pattern.fields.canonical_metric_or_object
    confidence: high
    canonical_cognee_edge: true
    logistics_only: true
    canonical_edge_type: PRODUCES_METRIC
    inverse_edge_type: PRODUCED_BY_QUERY_PATTERN
    materialize_inverse: false
    edge_class: canonical
    source_type: query_pattern
    target_type: metric
```

```yaml
candidate_edge:
  edge_id: edge.query_pattern.logistics.dtdc_settlement_to_shiprocket_freight_fallback.uses_reconciliation_profile.reconciliation_profile.cod_expected_to_courier_remittance
  edge_type: USES_RECONCILIATION_PROFILE
  source: query_pattern.logistics.dtdc_settlement_to_shiprocket_freight_fallback
  target: reconciliation_profile.cod_expected_to_courier_remittance
  fields:
    edge_family: execution_guidance
    evidence_basis: query_pattern.fields.canonical_metric_or_object
    confidence: high
    canonical_cognee_edge: true
    logistics_only: true
    canonical_edge_type: USES_RECONCILIATION_PROFILE
    inverse_edge_type: USED_BY_QUERY_PATTERN
    materialize_inverse: false
    edge_class: canonical
    source_type: query_pattern
    target_type: reconciliation_profile
```

```yaml
candidate_edge:
  edge_id: edge.query_pattern.logistics.dtdc_settlement_to_shiprocket_freight_fallback.uses_reconciliation_profile.reconciliation_profile.shipment_to_freight_invoice
  edge_type: USES_RECONCILIATION_PROFILE
  source: query_pattern.logistics.dtdc_settlement_to_shiprocket_freight_fallback
  target: reconciliation_profile.shipment_to_freight_invoice
  fields:
    edge_family: execution_guidance
    evidence_basis: query_pattern.fields.canonical_metric_or_object
    confidence: high
    canonical_cognee_edge: true
    logistics_only: true
    canonical_edge_type: USES_RECONCILIATION_PROFILE
    inverse_edge_type: USED_BY_QUERY_PATTERN
    materialize_inverse: false
    edge_class: canonical
    source_type: query_pattern
    target_type: reconciliation_profile
```

```yaml
candidate_edge:
  edge_id: edge.query_pattern.logistics.dtdc_settlement_to_shiprocket_freight_fallback.uses_table.table.zs_observe.dtdc_settlement
  edge_type: USES_TABLE
  source: query_pattern.logistics.dtdc_settlement_to_shiprocket_freight_fallback
  target: table.zs_observe.dtdc_settlement
  fields:
    edge_family: metric_understanding
    evidence_basis: query_pattern.fields.required_tables
    confidence: high
    canonical_cognee_edge: true
    logistics_only: true
    canonical_edge_type: USES_TABLE
    inverse_edge_type: USED_BY_CONTEXT
    materialize_inverse: false
    edge_class: canonical
    source_type: query_pattern
    target_type: table
```

```yaml
candidate_edge:
  edge_id: edge.query_pattern.logistics.dtdc_settlement_to_shiprocket_freight_fallback.uses_table.table.zs_observe.shiprocket_invoice
  edge_type: USES_TABLE
  source: query_pattern.logistics.dtdc_settlement_to_shiprocket_freight_fallback
  target: table.zs_observe.shiprocket_invoice
  fields:
    edge_family: metric_understanding
    evidence_basis: query_pattern.fields.required_tables
    confidence: high
    canonical_cognee_edge: true
    logistics_only: true
    canonical_edge_type: USES_TABLE
    inverse_edge_type: USED_BY_CONTEXT
    materialize_inverse: false
    edge_class: canonical
    source_type: query_pattern
    target_type: table
```

```yaml
candidate_edge:
  edge_id: edge.query_pattern.logistics.dtdc_settlement_to_shiprocket_freight_fallback.requires_rule.rule.logistics.dtdc_invoice_empty
  edge_type: REQUIRES_RULE
  source: query_pattern.logistics.dtdc_settlement_to_shiprocket_freight_fallback
  target: rule.logistics.dtdc_invoice_empty
  fields:
    edge_family: execution_guidance
    evidence_basis: query_pattern.fields.rules
    confidence: high
    canonical_cognee_edge: true
    logistics_only: true
    canonical_edge_type: REQUIRES_RULE
    inverse_edge_type: REQUIRED_BY_QUERY_PATTERN
    materialize_inverse: false
    edge_class: canonical
    source_type: query_pattern
    target_type: rule
```

```yaml
candidate_edge:
  edge_id: edge.query_pattern.logistics.dtdc_settlement_to_shiprocket_freight_fallback.requires_rule.rule.logistics.fallback_sources_explicit_only
  edge_type: REQUIRES_RULE
  source: query_pattern.logistics.dtdc_settlement_to_shiprocket_freight_fallback
  target: rule.logistics.fallback_sources_explicit_only
  fields:
    edge_family: execution_guidance
    evidence_basis: query_pattern.fields.rules
    confidence: high
    canonical_cognee_edge: true
    logistics_only: true
    canonical_edge_type: REQUIRES_RULE
    inverse_edge_type: REQUIRED_BY_QUERY_PATTERN
    materialize_inverse: false
    edge_class: canonical
    source_type: query_pattern
    target_type: rule
```

```yaml
candidate_edge:
  edge_id: edge.query_pattern.logistics.dtdc_settlement_to_shiprocket_freight_fallback.has_validation_test.validation_test.logistics.required_scope_context
  edge_type: HAS_VALIDATION_TEST
  source: query_pattern.logistics.dtdc_settlement_to_shiprocket_freight_fallback
  target: validation_test.logistics.required_scope_context
  fields:
    edge_family: execution_guidance
    evidence_basis: query_pattern.fields.validation_tests
    confidence: high
    canonical_cognee_edge: true
    logistics_only: true
    canonical_edge_type: HAS_VALIDATION_TEST
    inverse_edge_type: VALIDATES_QUERY_PATTERN_OR_ENFORCES_RULE
    materialize_inverse: false
    edge_class: canonical
    source_type: query_pattern
    target_type: validation_test
```

```yaml
candidate_edge:
  edge_id: edge.query_pattern.logistics.dtdc_settlement_to_shiprocket_freight_fallback.has_validation_test.validation_test.logistics.amount_semantics_not_by_name
  edge_type: HAS_VALIDATION_TEST
  source: query_pattern.logistics.dtdc_settlement_to_shiprocket_freight_fallback
  target: validation_test.logistics.amount_semantics_not_by_name
  fields:
    edge_family: execution_guidance
    evidence_basis: query_pattern.fields.validation_tests
    confidence: high
    canonical_cognee_edge: true
    logistics_only: true
    canonical_edge_type: HAS_VALIDATION_TEST
    inverse_edge_type: VALIDATES_QUERY_PATTERN_OR_ENFORCES_RULE
    materialize_inverse: false
    edge_class: canonical
    source_type: query_pattern
    target_type: validation_test
```

```yaml
candidate_edge:
  edge_id: edge.query_pattern.logistics.dtdc_settlement_to_shiprocket_freight_fallback.uses_output_contract.output_contract.logistics_diagnostic_summary
  edge_type: USES_OUTPUT_CONTRACT
  source: query_pattern.logistics.dtdc_settlement_to_shiprocket_freight_fallback
  target: output_contract.logistics_diagnostic_summary
  fields:
    edge_family: execution_guidance
    evidence_basis: query_pattern.fields.output_contracts
    confidence: high
    canonical_cognee_edge: true
    logistics_only: true
    canonical_edge_type: USES_OUTPUT_CONTRACT
    inverse_edge_type: USED_BY_CONTEXT
    materialize_inverse: false
    edge_class: canonical
    source_type: query_pattern
    target_type: output_contract
```

```yaml
candidate_edge:
  edge_id: edge.query_pattern.logistics.dtdc_utr_bank_bridge.produces_metric.metric.batch_settlement_amount
  edge_type: PRODUCES_METRIC
  source: query_pattern.logistics.dtdc_utr_bank_bridge
  target: metric.batch_settlement_amount
  fields:
    edge_family: execution_guidance
    evidence_basis: query_pattern.fields.canonical_metric_or_object
    confidence: high
    canonical_cognee_edge: true
    logistics_only: true
    canonical_edge_type: PRODUCES_METRIC
    inverse_edge_type: PRODUCED_BY_QUERY_PATTERN
    materialize_inverse: false
    edge_class: canonical
    source_type: query_pattern
    target_type: metric
```

```yaml
candidate_edge:
  edge_id: edge.query_pattern.logistics.dtdc_utr_bank_bridge.produces_metric.metric.bank_credit_matched_amount
  edge_type: PRODUCES_METRIC
  source: query_pattern.logistics.dtdc_utr_bank_bridge
  target: metric.bank_credit_matched_amount
  fields:
    edge_family: execution_guidance
    evidence_basis: query_pattern.fields.canonical_metric_or_object
    confidence: high
    canonical_cognee_edge: true
    logistics_only: true
    canonical_edge_type: PRODUCES_METRIC
    inverse_edge_type: PRODUCED_BY_QUERY_PATTERN
    materialize_inverse: false
    edge_class: canonical
    source_type: query_pattern
    target_type: metric
```

```yaml
candidate_edge:
  edge_id: edge.query_pattern.logistics.dtdc_utr_bank_bridge.uses_reconciliation_profile.reconciliation_profile.courier_batch_to_bank_credit
  edge_type: USES_RECONCILIATION_PROFILE
  source: query_pattern.logistics.dtdc_utr_bank_bridge
  target: reconciliation_profile.courier_batch_to_bank_credit
  fields:
    edge_family: execution_guidance
    evidence_basis: query_pattern.fields.canonical_metric_or_object
    confidence: high
    canonical_cognee_edge: true
    logistics_only: true
    canonical_edge_type: USES_RECONCILIATION_PROFILE
    inverse_edge_type: USED_BY_QUERY_PATTERN
    materialize_inverse: false
    edge_class: canonical
    source_type: query_pattern
    target_type: reconciliation_profile
```

```yaml
candidate_edge:
  edge_id: edge.query_pattern.logistics.dtdc_utr_bank_bridge.uses_table.table.zs_observe.dtdc_settlement
  edge_type: USES_TABLE
  source: query_pattern.logistics.dtdc_utr_bank_bridge
  target: table.zs_observe.dtdc_settlement
  fields:
    edge_family: metric_understanding
    evidence_basis: query_pattern.fields.required_tables
    confidence: high
    canonical_cognee_edge: true
    logistics_only: true
    canonical_edge_type: USES_TABLE
    inverse_edge_type: USED_BY_CONTEXT
    materialize_inverse: false
    edge_class: canonical
    source_type: query_pattern
    target_type: table
```

```yaml
candidate_edge:
  edge_id: edge.query_pattern.logistics.dtdc_utr_bank_bridge.requires_rule.rule.logistics.utr_preferred_for_bank_bridge
  edge_type: REQUIRES_RULE
  source: query_pattern.logistics.dtdc_utr_bank_bridge
  target: rule.logistics.utr_preferred_for_bank_bridge
  fields:
    edge_family: execution_guidance
    evidence_basis: query_pattern.fields.rules
    confidence: high
    canonical_cognee_edge: true
    logistics_only: true
    canonical_edge_type: REQUIRES_RULE
    inverse_edge_type: REQUIRED_BY_QUERY_PATTERN
    materialize_inverse: false
    edge_class: canonical
    source_type: query_pattern
    target_type: rule
```

```yaml
candidate_edge:
  edge_id: edge.query_pattern.logistics.dtdc_utr_bank_bridge.requires_rule.rule.logistics.bank_reference_required_for_bank_match
  edge_type: REQUIRES_RULE
  source: query_pattern.logistics.dtdc_utr_bank_bridge
  target: rule.logistics.bank_reference_required_for_bank_match
  fields:
    edge_family: execution_guidance
    evidence_basis: query_pattern.fields.rules
    confidence: high
    canonical_cognee_edge: true
    logistics_only: true
    canonical_edge_type: REQUIRES_RULE
    inverse_edge_type: REQUIRED_BY_QUERY_PATTERN
    materialize_inverse: false
    edge_class: canonical
    source_type: query_pattern
    target_type: rule
```

```yaml
candidate_edge:
  edge_id: edge.query_pattern.logistics.dtdc_utr_bank_bridge.has_validation_test.validation_test.logistics.required_scope_context
  edge_type: HAS_VALIDATION_TEST
  source: query_pattern.logistics.dtdc_utr_bank_bridge
  target: validation_test.logistics.required_scope_context
  fields:
    edge_family: execution_guidance
    evidence_basis: query_pattern.fields.validation_tests
    confidence: high
    canonical_cognee_edge: true
    logistics_only: true
    canonical_edge_type: HAS_VALIDATION_TEST
    inverse_edge_type: VALIDATES_QUERY_PATTERN_OR_ENFORCES_RULE
    materialize_inverse: false
    edge_class: canonical
    source_type: query_pattern
    target_type: validation_test
```

```yaml
candidate_edge:
  edge_id: edge.query_pattern.logistics.dtdc_utr_bank_bridge.has_validation_test.validation_test.logistics.amount_semantics_not_by_name
  edge_type: HAS_VALIDATION_TEST
  source: query_pattern.logistics.dtdc_utr_bank_bridge
  target: validation_test.logistics.amount_semantics_not_by_name
  fields:
    edge_family: execution_guidance
    evidence_basis: query_pattern.fields.validation_tests
    confidence: high
    canonical_cognee_edge: true
    logistics_only: true
    canonical_edge_type: HAS_VALIDATION_TEST
    inverse_edge_type: VALIDATES_QUERY_PATTERN_OR_ENFORCES_RULE
    materialize_inverse: false
    edge_class: canonical
    source_type: query_pattern
    target_type: validation_test
```

```yaml
candidate_edge:
  edge_id: edge.query_pattern.logistics.dtdc_utr_bank_bridge.uses_output_contract.output_contract.logistics_money_flow_trace
  edge_type: USES_OUTPUT_CONTRACT
  source: query_pattern.logistics.dtdc_utr_bank_bridge
  target: output_contract.logistics_money_flow_trace
  fields:
    edge_family: execution_guidance
    evidence_basis: query_pattern.fields.output_contracts
    confidence: high
    canonical_cognee_edge: true
    logistics_only: true
    canonical_edge_type: USES_OUTPUT_CONTRACT
    inverse_edge_type: USED_BY_CONTEXT
    materialize_inverse: false
    edge_class: canonical
    source_type: query_pattern
    target_type: output_contract
```

```yaml
candidate_edge:
  edge_id: edge.query_pattern.logistics.ekart_cod_pos_split.produces_metric.metric.cod_remitted_amount
  edge_type: PRODUCES_METRIC
  source: query_pattern.logistics.ekart_cod_pos_split
  target: metric.cod_remitted_amount
  fields:
    edge_family: execution_guidance
    evidence_basis: query_pattern.fields.canonical_metric_or_object
    confidence: high
    canonical_cognee_edge: true
    logistics_only: true
    canonical_edge_type: PRODUCES_METRIC
    inverse_edge_type: PRODUCED_BY_QUERY_PATTERN
    materialize_inverse: false
    edge_class: canonical
    source_type: query_pattern
    target_type: metric
```

```yaml
candidate_edge:
  edge_id: edge.query_pattern.logistics.ekart_cod_pos_split.produces_metric.metric.pos_settled_amount
  edge_type: PRODUCES_METRIC
  source: query_pattern.logistics.ekart_cod_pos_split
  target: metric.pos_settled_amount
  fields:
    edge_family: execution_guidance
    evidence_basis: query_pattern.fields.canonical_metric_or_object
    confidence: high
    canonical_cognee_edge: true
    logistics_only: true
    canonical_edge_type: PRODUCES_METRIC
    inverse_edge_type: PRODUCED_BY_QUERY_PATTERN
    materialize_inverse: false
    edge_class: canonical
    source_type: query_pattern
    target_type: metric
```

```yaml
candidate_edge:
  edge_id: edge.query_pattern.logistics.ekart_cod_pos_split.produces_metric.metric.batch_settlement_amount
  edge_type: PRODUCES_METRIC
  source: query_pattern.logistics.ekart_cod_pos_split
  target: metric.batch_settlement_amount
  fields:
    edge_family: execution_guidance
    evidence_basis: query_pattern.fields.canonical_metric_or_object
    confidence: high
    canonical_cognee_edge: true
    logistics_only: true
    canonical_edge_type: PRODUCES_METRIC
    inverse_edge_type: PRODUCED_BY_QUERY_PATTERN
    materialize_inverse: false
    edge_class: canonical
    source_type: query_pattern
    target_type: metric
```

```yaml
candidate_edge:
  edge_id: edge.query_pattern.logistics.ekart_cod_pos_split.uses_reconciliation_profile.reconciliation_profile.cod_expected_to_courier_remittance
  edge_type: USES_RECONCILIATION_PROFILE
  source: query_pattern.logistics.ekart_cod_pos_split
  target: reconciliation_profile.cod_expected_to_courier_remittance
  fields:
    edge_family: execution_guidance
    evidence_basis: query_pattern.fields.canonical_metric_or_object
    confidence: high
    canonical_cognee_edge: true
    logistics_only: true
    canonical_edge_type: USES_RECONCILIATION_PROFILE
    inverse_edge_type: USED_BY_QUERY_PATTERN
    materialize_inverse: false
    edge_class: canonical
    source_type: query_pattern
    target_type: reconciliation_profile
```

```yaml
candidate_edge:
  edge_id: edge.query_pattern.logistics.ekart_cod_pos_split.uses_table.table.zs_observe.ekart_settlement
  edge_type: USES_TABLE
  source: query_pattern.logistics.ekart_cod_pos_split
  target: table.zs_observe.ekart_settlement
  fields:
    edge_family: metric_understanding
    evidence_basis: query_pattern.fields.required_tables
    confidence: high
    canonical_cognee_edge: true
    logistics_only: true
    canonical_edge_type: USES_TABLE
    inverse_edge_type: USED_BY_CONTEXT
    materialize_inverse: false
    edge_class: canonical
    source_type: query_pattern
    target_type: table
```

```yaml
candidate_edge:
  edge_id: edge.query_pattern.logistics.ekart_cod_pos_split.requires_rule.rule.logistics.ekart_settlement_transaction_type_required
  edge_type: REQUIRES_RULE
  source: query_pattern.logistics.ekart_cod_pos_split
  target: rule.logistics.ekart_settlement_transaction_type_required
  fields:
    edge_family: execution_guidance
    evidence_basis: query_pattern.fields.rules
    confidence: high
    canonical_cognee_edge: true
    logistics_only: true
    canonical_edge_type: REQUIRES_RULE
    inverse_edge_type: REQUIRED_BY_QUERY_PATTERN
    materialize_inverse: false
    edge_class: canonical
    source_type: query_pattern
    target_type: rule
```

```yaml
candidate_edge:
  edge_id: edge.query_pattern.logistics.ekart_cod_pos_split.requires_rule.rule.logistics.total_amount_of_batch_not_awb_level
  edge_type: REQUIRES_RULE
  source: query_pattern.logistics.ekart_cod_pos_split
  target: rule.logistics.total_amount_of_batch_not_awb_level
  fields:
    edge_family: execution_guidance
    evidence_basis: query_pattern.fields.rules
    confidence: high
    canonical_cognee_edge: true
    logistics_only: true
    canonical_edge_type: REQUIRES_RULE
    inverse_edge_type: REQUIRED_BY_QUERY_PATTERN
    materialize_inverse: false
    edge_class: canonical
    source_type: query_pattern
    target_type: rule
```

```yaml
candidate_edge:
  edge_id: edge.query_pattern.logistics.ekart_cod_pos_split.has_validation_test.validation_test.logistics.required_scope_context
  edge_type: HAS_VALIDATION_TEST
  source: query_pattern.logistics.ekart_cod_pos_split
  target: validation_test.logistics.required_scope_context
  fields:
    edge_family: execution_guidance
    evidence_basis: query_pattern.fields.validation_tests
    confidence: high
    canonical_cognee_edge: true
    logistics_only: true
    canonical_edge_type: HAS_VALIDATION_TEST
    inverse_edge_type: VALIDATES_QUERY_PATTERN_OR_ENFORCES_RULE
    materialize_inverse: false
    edge_class: canonical
    source_type: query_pattern
    target_type: validation_test
```

```yaml
candidate_edge:
  edge_id: edge.query_pattern.logistics.ekart_cod_pos_split.has_validation_test.validation_test.logistics.amount_semantics_not_by_name
  edge_type: HAS_VALIDATION_TEST
  source: query_pattern.logistics.ekart_cod_pos_split
  target: validation_test.logistics.amount_semantics_not_by_name
  fields:
    edge_family: execution_guidance
    evidence_basis: query_pattern.fields.validation_tests
    confidence: high
    canonical_cognee_edge: true
    logistics_only: true
    canonical_edge_type: HAS_VALIDATION_TEST
    inverse_edge_type: VALIDATES_QUERY_PATTERN_OR_ENFORCES_RULE
    materialize_inverse: false
    edge_class: canonical
    source_type: query_pattern
    target_type: validation_test
```

```yaml
candidate_edge:
  edge_id: edge.query_pattern.logistics.ekart_cod_pos_split.uses_output_contract.output_contract.logistics_metric_summary
  edge_type: USES_OUTPUT_CONTRACT
  source: query_pattern.logistics.ekart_cod_pos_split
  target: output_contract.logistics_metric_summary
  fields:
    edge_family: execution_guidance
    evidence_basis: query_pattern.fields.output_contracts
    confidence: high
    canonical_cognee_edge: true
    logistics_only: true
    canonical_edge_type: USES_OUTPUT_CONTRACT
    inverse_edge_type: USED_BY_CONTEXT
    materialize_inverse: false
    edge_class: canonical
    source_type: query_pattern
    target_type: output_contract
```

```yaml
candidate_edge:
  edge_id: edge.query_pattern.logistics.ekart_batch_deduplicated_bank_bridge.produces_metric.metric.batch_settlement_amount
  edge_type: PRODUCES_METRIC
  source: query_pattern.logistics.ekart_batch_deduplicated_bank_bridge
  target: metric.batch_settlement_amount
  fields:
    edge_family: execution_guidance
    evidence_basis: query_pattern.fields.canonical_metric_or_object
    confidence: high
    canonical_cognee_edge: true
    logistics_only: true
    canonical_edge_type: PRODUCES_METRIC
    inverse_edge_type: PRODUCED_BY_QUERY_PATTERN
    materialize_inverse: false
    edge_class: canonical
    source_type: query_pattern
    target_type: metric
```

```yaml
candidate_edge:
  edge_id: edge.query_pattern.logistics.ekart_batch_deduplicated_bank_bridge.uses_reconciliation_profile.reconciliation_profile.courier_batch_to_bank_credit
  edge_type: USES_RECONCILIATION_PROFILE
  source: query_pattern.logistics.ekart_batch_deduplicated_bank_bridge
  target: reconciliation_profile.courier_batch_to_bank_credit
  fields:
    edge_family: execution_guidance
    evidence_basis: query_pattern.fields.canonical_metric_or_object
    confidence: high
    canonical_cognee_edge: true
    logistics_only: true
    canonical_edge_type: USES_RECONCILIATION_PROFILE
    inverse_edge_type: USED_BY_QUERY_PATTERN
    materialize_inverse: false
    edge_class: canonical
    source_type: query_pattern
    target_type: reconciliation_profile
```

```yaml
candidate_edge:
  edge_id: edge.query_pattern.logistics.ekart_batch_deduplicated_bank_bridge.uses_table.table.zs_observe.ekart_settlement
  edge_type: USES_TABLE
  source: query_pattern.logistics.ekart_batch_deduplicated_bank_bridge
  target: table.zs_observe.ekart_settlement
  fields:
    edge_family: metric_understanding
    evidence_basis: query_pattern.fields.required_tables
    confidence: high
    canonical_cognee_edge: true
    logistics_only: true
    canonical_edge_type: USES_TABLE
    inverse_edge_type: USED_BY_CONTEXT
    materialize_inverse: false
    edge_class: canonical
    source_type: query_pattern
    target_type: table
```

```yaml
candidate_edge:
  edge_id: edge.query_pattern.logistics.ekart_batch_deduplicated_bank_bridge.requires_rule.rule.logistics.batch_amount_deduplicate
  edge_type: REQUIRES_RULE
  source: query_pattern.logistics.ekart_batch_deduplicated_bank_bridge
  target: rule.logistics.batch_amount_deduplicate
  fields:
    edge_family: execution_guidance
    evidence_basis: query_pattern.fields.rules
    confidence: high
    canonical_cognee_edge: true
    logistics_only: true
    canonical_edge_type: REQUIRES_RULE
    inverse_edge_type: REQUIRED_BY_QUERY_PATTERN
    materialize_inverse: false
    edge_class: canonical
    source_type: query_pattern
    target_type: rule
```

```yaml
candidate_edge:
  edge_id: edge.query_pattern.logistics.ekart_batch_deduplicated_bank_bridge.requires_rule.rule.logistics.total_amount_of_batch_not_awb_level
  edge_type: REQUIRES_RULE
  source: query_pattern.logistics.ekart_batch_deduplicated_bank_bridge
  target: rule.logistics.total_amount_of_batch_not_awb_level
  fields:
    edge_family: execution_guidance
    evidence_basis: query_pattern.fields.rules
    confidence: high
    canonical_cognee_edge: true
    logistics_only: true
    canonical_edge_type: REQUIRES_RULE
    inverse_edge_type: REQUIRED_BY_QUERY_PATTERN
    materialize_inverse: false
    edge_class: canonical
    source_type: query_pattern
    target_type: rule
```

```yaml
candidate_edge:
  edge_id: edge.query_pattern.logistics.ekart_batch_deduplicated_bank_bridge.has_validation_test.validation_test.logistics.required_scope_context
  edge_type: HAS_VALIDATION_TEST
  source: query_pattern.logistics.ekart_batch_deduplicated_bank_bridge
  target: validation_test.logistics.required_scope_context
  fields:
    edge_family: execution_guidance
    evidence_basis: query_pattern.fields.validation_tests
    confidence: high
    canonical_cognee_edge: true
    logistics_only: true
    canonical_edge_type: HAS_VALIDATION_TEST
    inverse_edge_type: VALIDATES_QUERY_PATTERN_OR_ENFORCES_RULE
    materialize_inverse: false
    edge_class: canonical
    source_type: query_pattern
    target_type: validation_test
```

```yaml
candidate_edge:
  edge_id: edge.query_pattern.logistics.ekart_batch_deduplicated_bank_bridge.has_validation_test.validation_test.logistics.amount_semantics_not_by_name
  edge_type: HAS_VALIDATION_TEST
  source: query_pattern.logistics.ekart_batch_deduplicated_bank_bridge
  target: validation_test.logistics.amount_semantics_not_by_name
  fields:
    edge_family: execution_guidance
    evidence_basis: query_pattern.fields.validation_tests
    confidence: high
    canonical_cognee_edge: true
    logistics_only: true
    canonical_edge_type: HAS_VALIDATION_TEST
    inverse_edge_type: VALIDATES_QUERY_PATTERN_OR_ENFORCES_RULE
    materialize_inverse: false
    edge_class: canonical
    source_type: query_pattern
    target_type: validation_test
```

```yaml
candidate_edge:
  edge_id: edge.query_pattern.logistics.ekart_batch_deduplicated_bank_bridge.uses_output_contract.output_contract.logistics_money_flow_trace
  edge_type: USES_OUTPUT_CONTRACT
  source: query_pattern.logistics.ekart_batch_deduplicated_bank_bridge
  target: output_contract.logistics_money_flow_trace
  fields:
    edge_family: execution_guidance
    evidence_basis: query_pattern.fields.output_contracts
    confidence: high
    canonical_cognee_edge: true
    logistics_only: true
    canonical_edge_type: USES_OUTPUT_CONTRACT
    inverse_edge_type: USED_BY_CONTEXT
    materialize_inverse: false
    edge_class: canonical
    source_type: query_pattern
    target_type: output_contract
```

```yaml
candidate_edge:
  edge_id: edge.query_pattern.logistics.xpressbees_native_vs_shiprocket_fallback.produces_metric.metric.cod_remitted_amount
  edge_type: PRODUCES_METRIC
  source: query_pattern.logistics.xpressbees_native_vs_shiprocket_fallback
  target: metric.cod_remitted_amount
  fields:
    edge_family: execution_guidance
    evidence_basis: query_pattern.fields.canonical_metric_or_object
    confidence: high
    canonical_cognee_edge: true
    logistics_only: true
    canonical_edge_type: PRODUCES_METRIC
    inverse_edge_type: PRODUCED_BY_QUERY_PATTERN
    materialize_inverse: false
    edge_class: canonical
    source_type: query_pattern
    target_type: metric
```

```yaml
candidate_edge:
  edge_id: edge.query_pattern.logistics.xpressbees_native_vs_shiprocket_fallback.produces_metric.metric.populated_native_record_count
  edge_type: PRODUCES_METRIC
  source: query_pattern.logistics.xpressbees_native_vs_shiprocket_fallback
  target: metric.populated_native_record_count
  fields:
    edge_family: execution_guidance
    evidence_basis: query_pattern.fields.canonical_metric_or_object
    confidence: high
    canonical_cognee_edge: true
    logistics_only: true
    canonical_edge_type: PRODUCES_METRIC
    inverse_edge_type: PRODUCED_BY_QUERY_PATTERN
    materialize_inverse: false
    edge_class: canonical
    source_type: query_pattern
    target_type: metric
```

```yaml
candidate_edge:
  edge_id: edge.query_pattern.logistics.xpressbees_native_vs_shiprocket_fallback.uses_reconciliation_profile.reconciliation_profile.cod_expected_to_courier_remittance
  edge_type: USES_RECONCILIATION_PROFILE
  source: query_pattern.logistics.xpressbees_native_vs_shiprocket_fallback
  target: reconciliation_profile.cod_expected_to_courier_remittance
  fields:
    edge_family: execution_guidance
    evidence_basis: query_pattern.fields.canonical_metric_or_object
    confidence: high
    canonical_cognee_edge: true
    logistics_only: true
    canonical_edge_type: USES_RECONCILIATION_PROFILE
    inverse_edge_type: USED_BY_QUERY_PATTERN
    materialize_inverse: false
    edge_class: canonical
    source_type: query_pattern
    target_type: reconciliation_profile
```

```yaml
candidate_edge:
  edge_id: edge.query_pattern.logistics.xpressbees_native_vs_shiprocket_fallback.uses_table.table.zs_observe.xpressbees_settlement
  edge_type: USES_TABLE
  source: query_pattern.logistics.xpressbees_native_vs_shiprocket_fallback
  target: table.zs_observe.xpressbees_settlement
  fields:
    edge_family: metric_understanding
    evidence_basis: query_pattern.fields.required_tables
    confidence: high
    canonical_cognee_edge: true
    logistics_only: true
    canonical_edge_type: USES_TABLE
    inverse_edge_type: USED_BY_CONTEXT
    materialize_inverse: false
    edge_class: canonical
    source_type: query_pattern
    target_type: table
```

```yaml
candidate_edge:
  edge_id: edge.query_pattern.logistics.xpressbees_native_vs_shiprocket_fallback.uses_table.table.zs_observe.shiprocket_settlement
  edge_type: USES_TABLE
  source: query_pattern.logistics.xpressbees_native_vs_shiprocket_fallback
  target: table.zs_observe.shiprocket_settlement
  fields:
    edge_family: metric_understanding
    evidence_basis: query_pattern.fields.required_tables
    confidence: high
    canonical_cognee_edge: true
    logistics_only: true
    canonical_edge_type: USES_TABLE
    inverse_edge_type: USED_BY_CONTEXT
    materialize_inverse: false
    edge_class: canonical
    source_type: query_pattern
    target_type: table
```

```yaml
candidate_edge:
  edge_id: edge.query_pattern.logistics.xpressbees_native_vs_shiprocket_fallback.requires_rule.rule.logistics.xpressbees_native_low_confidence
  edge_type: REQUIRES_RULE
  source: query_pattern.logistics.xpressbees_native_vs_shiprocket_fallback
  target: rule.logistics.xpressbees_native_low_confidence
  fields:
    edge_family: execution_guidance
    evidence_basis: query_pattern.fields.rules
    confidence: high
    canonical_cognee_edge: true
    logistics_only: true
    canonical_edge_type: REQUIRES_RULE
    inverse_edge_type: REQUIRED_BY_QUERY_PATTERN
    materialize_inverse: false
    edge_class: canonical
    source_type: query_pattern
    target_type: rule
```

```yaml
candidate_edge:
  edge_id: edge.query_pattern.logistics.xpressbees_native_vs_shiprocket_fallback.requires_rule.rule.logistics.xpressbees_fallback_shiprocket_preferred
  edge_type: REQUIRES_RULE
  source: query_pattern.logistics.xpressbees_native_vs_shiprocket_fallback
  target: rule.logistics.xpressbees_fallback_shiprocket_preferred
  fields:
    edge_family: execution_guidance
    evidence_basis: query_pattern.fields.rules
    confidence: high
    canonical_cognee_edge: true
    logistics_only: true
    canonical_edge_type: REQUIRES_RULE
    inverse_edge_type: REQUIRED_BY_QUERY_PATTERN
    materialize_inverse: false
    edge_class: canonical
    source_type: query_pattern
    target_type: rule
```

```yaml
candidate_edge:
  edge_id: edge.query_pattern.logistics.xpressbees_native_vs_shiprocket_fallback.has_validation_test.validation_test.logistics.required_scope_context
  edge_type: HAS_VALIDATION_TEST
  source: query_pattern.logistics.xpressbees_native_vs_shiprocket_fallback
  target: validation_test.logistics.required_scope_context
  fields:
    edge_family: execution_guidance
    evidence_basis: query_pattern.fields.validation_tests
    confidence: high
    canonical_cognee_edge: true
    logistics_only: true
    canonical_edge_type: HAS_VALIDATION_TEST
    inverse_edge_type: VALIDATES_QUERY_PATTERN_OR_ENFORCES_RULE
    materialize_inverse: false
    edge_class: canonical
    source_type: query_pattern
    target_type: validation_test
```

```yaml
candidate_edge:
  edge_id: edge.query_pattern.logistics.xpressbees_native_vs_shiprocket_fallback.has_validation_test.validation_test.logistics.amount_semantics_not_by_name
  edge_type: HAS_VALIDATION_TEST
  source: query_pattern.logistics.xpressbees_native_vs_shiprocket_fallback
  target: validation_test.logistics.amount_semantics_not_by_name
  fields:
    edge_family: execution_guidance
    evidence_basis: query_pattern.fields.validation_tests
    confidence: high
    canonical_cognee_edge: true
    logistics_only: true
    canonical_edge_type: HAS_VALIDATION_TEST
    inverse_edge_type: VALIDATES_QUERY_PATTERN_OR_ENFORCES_RULE
    materialize_inverse: false
    edge_class: canonical
    source_type: query_pattern
    target_type: validation_test
```

```yaml
candidate_edge:
  edge_id: edge.query_pattern.logistics.xpressbees_native_vs_shiprocket_fallback.uses_output_contract.output_contract.logistics_data_quality_report
  edge_type: USES_OUTPUT_CONTRACT
  source: query_pattern.logistics.xpressbees_native_vs_shiprocket_fallback
  target: output_contract.logistics_data_quality_report
  fields:
    edge_family: execution_guidance
    evidence_basis: query_pattern.fields.output_contracts
    confidence: high
    canonical_cognee_edge: true
    logistics_only: true
    canonical_edge_type: USES_OUTPUT_CONTRACT
    inverse_edge_type: USED_BY_CONTEXT
    materialize_inverse: false
    edge_class: canonical
    source_type: query_pattern
    target_type: output_contract
```

```yaml
candidate_edge:
  edge_id: edge.query_pattern.logistics.shadowfax_reverse_only_evidence.produces_metric.metric.return_shipment_count
  edge_type: PRODUCES_METRIC
  source: query_pattern.logistics.shadowfax_reverse_only_evidence
  target: metric.return_shipment_count
  fields:
    edge_family: execution_guidance
    evidence_basis: query_pattern.fields.canonical_metric_or_object
    confidence: high
    canonical_cognee_edge: true
    logistics_only: true
    canonical_edge_type: PRODUCES_METRIC
    inverse_edge_type: PRODUCED_BY_QUERY_PATTERN
    materialize_inverse: false
    edge_class: canonical
    source_type: query_pattern
    target_type: metric
```

```yaml
candidate_edge:
  edge_id: edge.query_pattern.logistics.shadowfax_reverse_only_evidence.uses_table.table.zs_observe.shiprocket_oms
  edge_type: USES_TABLE
  source: query_pattern.logistics.shadowfax_reverse_only_evidence
  target: table.zs_observe.shiprocket_oms
  fields:
    edge_family: metric_understanding
    evidence_basis: query_pattern.fields.required_tables
    confidence: high
    canonical_cognee_edge: true
    logistics_only: true
    canonical_edge_type: USES_TABLE
    inverse_edge_type: USED_BY_CONTEXT
    materialize_inverse: false
    edge_class: canonical
    source_type: query_pattern
    target_type: table
```

```yaml
candidate_edge:
  edge_id: edge.query_pattern.logistics.shadowfax_reverse_only_evidence.requires_rule.rule.logistics.shadowfax_no_native_settlement
  edge_type: REQUIRES_RULE
  source: query_pattern.logistics.shadowfax_reverse_only_evidence
  target: rule.logistics.shadowfax_no_native_settlement
  fields:
    edge_family: execution_guidance
    evidence_basis: query_pattern.fields.rules
    confidence: high
    canonical_cognee_edge: true
    logistics_only: true
    canonical_edge_type: REQUIRES_RULE
    inverse_edge_type: REQUIRED_BY_QUERY_PATTERN
    materialize_inverse: false
    edge_class: canonical
    source_type: query_pattern
    target_type: rule
```

```yaml
candidate_edge:
  edge_id: edge.query_pattern.logistics.shadowfax_reverse_only_evidence.has_validation_test.validation_test.logistics.required_scope_context
  edge_type: HAS_VALIDATION_TEST
  source: query_pattern.logistics.shadowfax_reverse_only_evidence
  target: validation_test.logistics.required_scope_context
  fields:
    edge_family: execution_guidance
    evidence_basis: query_pattern.fields.validation_tests
    confidence: high
    canonical_cognee_edge: true
    logistics_only: true
    canonical_edge_type: HAS_VALIDATION_TEST
    inverse_edge_type: VALIDATES_QUERY_PATTERN_OR_ENFORCES_RULE
    materialize_inverse: false
    edge_class: canonical
    source_type: query_pattern
    target_type: validation_test
```

```yaml
candidate_edge:
  edge_id: edge.query_pattern.logistics.shadowfax_reverse_only_evidence.has_validation_test.validation_test.logistics.amount_semantics_not_by_name
  edge_type: HAS_VALIDATION_TEST
  source: query_pattern.logistics.shadowfax_reverse_only_evidence
  target: validation_test.logistics.amount_semantics_not_by_name
  fields:
    edge_family: execution_guidance
    evidence_basis: query_pattern.fields.validation_tests
    confidence: high
    canonical_cognee_edge: true
    logistics_only: true
    canonical_edge_type: HAS_VALIDATION_TEST
    inverse_edge_type: VALIDATES_QUERY_PATTERN_OR_ENFORCES_RULE
    materialize_inverse: false
    edge_class: canonical
    source_type: query_pattern
    target_type: validation_test
```

```yaml
candidate_edge:
  edge_id: edge.query_pattern.logistics.shadowfax_reverse_only_evidence.uses_output_contract.output_contract.logistics_diagnostic_summary
  edge_type: USES_OUTPUT_CONTRACT
  source: query_pattern.logistics.shadowfax_reverse_only_evidence
  target: output_contract.logistics_diagnostic_summary
  fields:
    edge_family: execution_guidance
    evidence_basis: query_pattern.fields.output_contracts
    confidence: high
    canonical_cognee_edge: true
    logistics_only: true
    canonical_edge_type: USES_OUTPUT_CONTRACT
    inverse_edge_type: USED_BY_CONTEXT
    materialize_inverse: false
    edge_class: canonical
    source_type: query_pattern
    target_type: output_contract
```

```yaml
candidate_edge:
  edge_id: edge.query_pattern.logistics.ecom_indirect_shiprocket_evidence.produces_metric.metric.freight_billed_amount
  edge_type: PRODUCES_METRIC
  source: query_pattern.logistics.ecom_indirect_shiprocket_evidence
  target: metric.freight_billed_amount
  fields:
    edge_family: execution_guidance
    evidence_basis: query_pattern.fields.canonical_metric_or_object
    confidence: high
    canonical_cognee_edge: true
    logistics_only: true
    canonical_edge_type: PRODUCES_METRIC
    inverse_edge_type: PRODUCED_BY_QUERY_PATTERN
    materialize_inverse: false
    edge_class: canonical
    source_type: query_pattern
    target_type: metric
```

```yaml
candidate_edge:
  edge_id: edge.query_pattern.logistics.ecom_indirect_shiprocket_evidence.produces_metric.metric.cod_remitted_amount
  edge_type: PRODUCES_METRIC
  source: query_pattern.logistics.ecom_indirect_shiprocket_evidence
  target: metric.cod_remitted_amount
  fields:
    edge_family: execution_guidance
    evidence_basis: query_pattern.fields.canonical_metric_or_object
    confidence: high
    canonical_cognee_edge: true
    logistics_only: true
    canonical_edge_type: PRODUCES_METRIC
    inverse_edge_type: PRODUCED_BY_QUERY_PATTERN
    materialize_inverse: false
    edge_class: canonical
    source_type: query_pattern
    target_type: metric
```

```yaml
candidate_edge:
  edge_id: edge.query_pattern.logistics.ecom_indirect_shiprocket_evidence.uses_reconciliation_profile.reconciliation_profile.shipment_to_freight_invoice
  edge_type: USES_RECONCILIATION_PROFILE
  source: query_pattern.logistics.ecom_indirect_shiprocket_evidence
  target: reconciliation_profile.shipment_to_freight_invoice
  fields:
    edge_family: execution_guidance
    evidence_basis: query_pattern.fields.canonical_metric_or_object
    confidence: high
    canonical_cognee_edge: true
    logistics_only: true
    canonical_edge_type: USES_RECONCILIATION_PROFILE
    inverse_edge_type: USED_BY_QUERY_PATTERN
    materialize_inverse: false
    edge_class: canonical
    source_type: query_pattern
    target_type: reconciliation_profile
```

```yaml
candidate_edge:
  edge_id: edge.query_pattern.logistics.ecom_indirect_shiprocket_evidence.uses_reconciliation_profile.reconciliation_profile.cod_expected_to_courier_remittance
  edge_type: USES_RECONCILIATION_PROFILE
  source: query_pattern.logistics.ecom_indirect_shiprocket_evidence
  target: reconciliation_profile.cod_expected_to_courier_remittance
  fields:
    edge_family: execution_guidance
    evidence_basis: query_pattern.fields.canonical_metric_or_object
    confidence: high
    canonical_cognee_edge: true
    logistics_only: true
    canonical_edge_type: USES_RECONCILIATION_PROFILE
    inverse_edge_type: USED_BY_QUERY_PATTERN
    materialize_inverse: false
    edge_class: canonical
    source_type: query_pattern
    target_type: reconciliation_profile
```

```yaml
candidate_edge:
  edge_id: edge.query_pattern.logistics.ecom_indirect_shiprocket_evidence.uses_table.table.zs_observe.shiprocket_invoice
  edge_type: USES_TABLE
  source: query_pattern.logistics.ecom_indirect_shiprocket_evidence
  target: table.zs_observe.shiprocket_invoice
  fields:
    edge_family: metric_understanding
    evidence_basis: query_pattern.fields.required_tables
    confidence: high
    canonical_cognee_edge: true
    logistics_only: true
    canonical_edge_type: USES_TABLE
    inverse_edge_type: USED_BY_CONTEXT
    materialize_inverse: false
    edge_class: canonical
    source_type: query_pattern
    target_type: table
```

```yaml
candidate_edge:
  edge_id: edge.query_pattern.logistics.ecom_indirect_shiprocket_evidence.uses_table.table.zs_observe.shiprocket_settlement
  edge_type: USES_TABLE
  source: query_pattern.logistics.ecom_indirect_shiprocket_evidence
  target: table.zs_observe.shiprocket_settlement
  fields:
    edge_family: metric_understanding
    evidence_basis: query_pattern.fields.required_tables
    confidence: high
    canonical_cognee_edge: true
    logistics_only: true
    canonical_edge_type: USES_TABLE
    inverse_edge_type: USED_BY_CONTEXT
    materialize_inverse: false
    edge_class: canonical
    source_type: query_pattern
    target_type: table
```

```yaml
candidate_edge:
  edge_id: edge.query_pattern.logistics.ecom_indirect_shiprocket_evidence.requires_rule.rule.logistics.ecom_no_native_table
  edge_type: REQUIRES_RULE
  source: query_pattern.logistics.ecom_indirect_shiprocket_evidence
  target: rule.logistics.ecom_no_native_table
  fields:
    edge_family: execution_guidance
    evidence_basis: query_pattern.fields.rules
    confidence: high
    canonical_cognee_edge: true
    logistics_only: true
    canonical_edge_type: REQUIRES_RULE
    inverse_edge_type: REQUIRED_BY_QUERY_PATTERN
    materialize_inverse: false
    edge_class: canonical
    source_type: query_pattern
    target_type: rule
```

```yaml
candidate_edge:
  edge_id: edge.query_pattern.logistics.ecom_indirect_shiprocket_evidence.requires_rule.rule.logistics.fallback_sources_explicit_only
  edge_type: REQUIRES_RULE
  source: query_pattern.logistics.ecom_indirect_shiprocket_evidence
  target: rule.logistics.fallback_sources_explicit_only
  fields:
    edge_family: execution_guidance
    evidence_basis: query_pattern.fields.rules
    confidence: high
    canonical_cognee_edge: true
    logistics_only: true
    canonical_edge_type: REQUIRES_RULE
    inverse_edge_type: REQUIRED_BY_QUERY_PATTERN
    materialize_inverse: false
    edge_class: canonical
    source_type: query_pattern
    target_type: rule
```

```yaml
candidate_edge:
  edge_id: edge.query_pattern.logistics.ecom_indirect_shiprocket_evidence.has_validation_test.validation_test.logistics.required_scope_context
  edge_type: HAS_VALIDATION_TEST
  source: query_pattern.logistics.ecom_indirect_shiprocket_evidence
  target: validation_test.logistics.required_scope_context
  fields:
    edge_family: execution_guidance
    evidence_basis: query_pattern.fields.validation_tests
    confidence: high
    canonical_cognee_edge: true
    logistics_only: true
    canonical_edge_type: HAS_VALIDATION_TEST
    inverse_edge_type: VALIDATES_QUERY_PATTERN_OR_ENFORCES_RULE
    materialize_inverse: false
    edge_class: canonical
    source_type: query_pattern
    target_type: validation_test
```

```yaml
candidate_edge:
  edge_id: edge.query_pattern.logistics.ecom_indirect_shiprocket_evidence.has_validation_test.validation_test.logistics.amount_semantics_not_by_name
  edge_type: HAS_VALIDATION_TEST
  source: query_pattern.logistics.ecom_indirect_shiprocket_evidence
  target: validation_test.logistics.amount_semantics_not_by_name
  fields:
    edge_family: execution_guidance
    evidence_basis: query_pattern.fields.validation_tests
    confidence: high
    canonical_cognee_edge: true
    logistics_only: true
    canonical_edge_type: HAS_VALIDATION_TEST
    inverse_edge_type: VALIDATES_QUERY_PATTERN_OR_ENFORCES_RULE
    materialize_inverse: false
    edge_class: canonical
    source_type: query_pattern
    target_type: validation_test
```

```yaml
candidate_edge:
  edge_id: edge.query_pattern.logistics.ecom_indirect_shiprocket_evidence.uses_output_contract.output_contract.logistics_diagnostic_summary
  edge_type: USES_OUTPUT_CONTRACT
  source: query_pattern.logistics.ecom_indirect_shiprocket_evidence
  target: output_contract.logistics_diagnostic_summary
  fields:
    edge_family: execution_guidance
    evidence_basis: query_pattern.fields.output_contracts
    confidence: high
    canonical_cognee_edge: true
    logistics_only: true
    canonical_edge_type: USES_OUTPUT_CONTRACT
    inverse_edge_type: USED_BY_CONTEXT
    materialize_inverse: false
    edge_class: canonical
    source_type: query_pattern
    target_type: output_contract
```

```yaml
candidate_edge:
  edge_id: edge.query_pattern.logistics.order_to_shipment_missing_awb.produces_metric.metric.unmatched_awb_count
  edge_type: PRODUCES_METRIC
  source: query_pattern.logistics.order_to_shipment_missing_awb
  target: metric.unmatched_awb_count
  fields:
    edge_family: execution_guidance
    evidence_basis: query_pattern.fields.canonical_metric_or_object
    confidence: high
    canonical_cognee_edge: true
    logistics_only: true
    canonical_edge_type: PRODUCES_METRIC
    inverse_edge_type: PRODUCED_BY_QUERY_PATTERN
    materialize_inverse: false
    edge_class: canonical
    source_type: query_pattern
    target_type: metric
```

```yaml
candidate_edge:
  edge_id: edge.query_pattern.logistics.order_to_shipment_missing_awb.uses_reconciliation_profile.reconciliation_profile.order_to_shipment
  edge_type: USES_RECONCILIATION_PROFILE
  source: query_pattern.logistics.order_to_shipment_missing_awb
  target: reconciliation_profile.order_to_shipment
  fields:
    edge_family: execution_guidance
    evidence_basis: query_pattern.fields.canonical_metric_or_object
    confidence: high
    canonical_cognee_edge: true
    logistics_only: true
    canonical_edge_type: USES_RECONCILIATION_PROFILE
    inverse_edge_type: USED_BY_QUERY_PATTERN
    materialize_inverse: false
    edge_class: canonical
    source_type: query_pattern
    target_type: reconciliation_profile
```

```yaml
candidate_edge:
  edge_id: edge.query_pattern.logistics.order_to_shipment_missing_awb.uses_table.table.zs_observe.shiprocket_oms
  edge_type: USES_TABLE
  source: query_pattern.logistics.order_to_shipment_missing_awb
  target: table.zs_observe.shiprocket_oms
  fields:
    edge_family: metric_understanding
    evidence_basis: query_pattern.fields.required_tables
    confidence: high
    canonical_cognee_edge: true
    logistics_only: true
    canonical_edge_type: USES_TABLE
    inverse_edge_type: USED_BY_CONTEXT
    materialize_inverse: false
    edge_class: canonical
    source_type: query_pattern
    target_type: table
```

```yaml
candidate_edge:
  edge_id: edge.query_pattern.logistics.order_to_shipment_missing_awb.requires_rule.rule.logistics.parse_shiprocket_order_id_before_shopify_join
  edge_type: REQUIRES_RULE
  source: query_pattern.logistics.order_to_shipment_missing_awb
  target: rule.logistics.parse_shiprocket_order_id_before_shopify_join
  fields:
    edge_family: execution_guidance
    evidence_basis: query_pattern.fields.rules
    confidence: high
    canonical_cognee_edge: true
    logistics_only: true
    canonical_edge_type: REQUIRES_RULE
    inverse_edge_type: REQUIRED_BY_QUERY_PATTERN
    materialize_inverse: false
    edge_class: canonical
    source_type: query_pattern
    target_type: rule
```

```yaml
candidate_edge:
  edge_id: edge.query_pattern.logistics.order_to_shipment_missing_awb.has_validation_test.validation_test.logistics.required_scope_context
  edge_type: HAS_VALIDATION_TEST
  source: query_pattern.logistics.order_to_shipment_missing_awb
  target: validation_test.logistics.required_scope_context
  fields:
    edge_family: execution_guidance
    evidence_basis: query_pattern.fields.validation_tests
    confidence: high
    canonical_cognee_edge: true
    logistics_only: true
    canonical_edge_type: HAS_VALIDATION_TEST
    inverse_edge_type: VALIDATES_QUERY_PATTERN_OR_ENFORCES_RULE
    materialize_inverse: false
    edge_class: canonical
    source_type: query_pattern
    target_type: validation_test
```

```yaml
candidate_edge:
  edge_id: edge.query_pattern.logistics.order_to_shipment_missing_awb.has_validation_test.validation_test.logistics.amount_semantics_not_by_name
  edge_type: HAS_VALIDATION_TEST
  source: query_pattern.logistics.order_to_shipment_missing_awb
  target: validation_test.logistics.amount_semantics_not_by_name
  fields:
    edge_family: execution_guidance
    evidence_basis: query_pattern.fields.validation_tests
    confidence: high
    canonical_cognee_edge: true
    logistics_only: true
    canonical_edge_type: HAS_VALIDATION_TEST
    inverse_edge_type: VALIDATES_QUERY_PATTERN_OR_ENFORCES_RULE
    materialize_inverse: false
    edge_class: canonical
    source_type: query_pattern
    target_type: validation_test
```

```yaml
candidate_edge:
  edge_id: edge.query_pattern.logistics.order_to_shipment_missing_awb.uses_output_contract.output_contract.logistics_diagnostic_summary
  edge_type: USES_OUTPUT_CONTRACT
  source: query_pattern.logistics.order_to_shipment_missing_awb
  target: output_contract.logistics_diagnostic_summary
  fields:
    edge_family: execution_guidance
    evidence_basis: query_pattern.fields.output_contracts
    confidence: high
    canonical_cognee_edge: true
    logistics_only: true
    canonical_edge_type: USES_OUTPUT_CONTRACT
    inverse_edge_type: USED_BY_CONTEXT
    materialize_inverse: false
    edge_class: canonical
    source_type: query_pattern
    target_type: output_contract
```

```yaml
candidate_edge:
  edge_id: edge.query_pattern.logistics.awb_duplicate_detection.uses_reconciliation_profile.reconciliation_profile.order_to_shipment
  edge_type: USES_RECONCILIATION_PROFILE
  source: query_pattern.logistics.awb_duplicate_detection
  target: reconciliation_profile.order_to_shipment
  fields:
    edge_family: execution_guidance
    evidence_basis: query_pattern.fields.canonical_metric_or_object
    confidence: high
    canonical_cognee_edge: true
    logistics_only: true
    canonical_edge_type: USES_RECONCILIATION_PROFILE
    inverse_edge_type: USED_BY_QUERY_PATTERN
    materialize_inverse: false
    edge_class: canonical
    source_type: query_pattern
    target_type: reconciliation_profile
```

```yaml
candidate_edge:
  edge_id: edge.query_pattern.logistics.awb_duplicate_detection.uses_table.table.zs_observe.shiprocket_oms
  edge_type: USES_TABLE
  source: query_pattern.logistics.awb_duplicate_detection
  target: table.zs_observe.shiprocket_oms
  fields:
    edge_family: metric_understanding
    evidence_basis: query_pattern.fields.required_tables
    confidence: high
    canonical_cognee_edge: true
    logistics_only: true
    canonical_edge_type: USES_TABLE
    inverse_edge_type: USED_BY_CONTEXT
    materialize_inverse: false
    edge_class: canonical
    source_type: query_pattern
    target_type: table
```

```yaml
candidate_edge:
  edge_id: edge.query_pattern.logistics.awb_duplicate_detection.uses_table.table.zs_observe.shiprocket_invoice
  edge_type: USES_TABLE
  source: query_pattern.logistics.awb_duplicate_detection
  target: table.zs_observe.shiprocket_invoice
  fields:
    edge_family: metric_understanding
    evidence_basis: query_pattern.fields.required_tables
    confidence: high
    canonical_cognee_edge: true
    logistics_only: true
    canonical_edge_type: USES_TABLE
    inverse_edge_type: USED_BY_CONTEXT
    materialize_inverse: false
    edge_class: canonical
    source_type: query_pattern
    target_type: table
```

```yaml
candidate_edge:
  edge_id: edge.query_pattern.logistics.awb_duplicate_detection.uses_table.table.zs_observe.shiprocket_settlement
  edge_type: USES_TABLE
  source: query_pattern.logistics.awb_duplicate_detection
  target: table.zs_observe.shiprocket_settlement
  fields:
    edge_family: metric_understanding
    evidence_basis: query_pattern.fields.required_tables
    confidence: high
    canonical_cognee_edge: true
    logistics_only: true
    canonical_edge_type: USES_TABLE
    inverse_edge_type: USED_BY_CONTEXT
    materialize_inverse: false
    edge_class: canonical
    source_type: query_pattern
    target_type: table
```

```yaml
candidate_edge:
  edge_id: edge.query_pattern.logistics.awb_duplicate_detection.requires_rule.rule.logistics.awb_primary_reconciliation_unit
  edge_type: REQUIRES_RULE
  source: query_pattern.logistics.awb_duplicate_detection
  target: rule.logistics.awb_primary_reconciliation_unit
  fields:
    edge_family: execution_guidance
    evidence_basis: query_pattern.fields.rules
    confidence: high
    canonical_cognee_edge: true
    logistics_only: true
    canonical_edge_type: REQUIRES_RULE
    inverse_edge_type: REQUIRED_BY_QUERY_PATTERN
    materialize_inverse: false
    edge_class: canonical
    source_type: query_pattern
    target_type: rule
```

```yaml
candidate_edge:
  edge_id: edge.query_pattern.logistics.awb_duplicate_detection.has_validation_test.validation_test.logistics.required_scope_context
  edge_type: HAS_VALIDATION_TEST
  source: query_pattern.logistics.awb_duplicate_detection
  target: validation_test.logistics.required_scope_context
  fields:
    edge_family: execution_guidance
    evidence_basis: query_pattern.fields.validation_tests
    confidence: high
    canonical_cognee_edge: true
    logistics_only: true
    canonical_edge_type: HAS_VALIDATION_TEST
    inverse_edge_type: VALIDATES_QUERY_PATTERN_OR_ENFORCES_RULE
    materialize_inverse: false
    edge_class: canonical
    source_type: query_pattern
    target_type: validation_test
```

```yaml
candidate_edge:
  edge_id: edge.query_pattern.logistics.awb_duplicate_detection.has_validation_test.validation_test.logistics.amount_semantics_not_by_name
  edge_type: HAS_VALIDATION_TEST
  source: query_pattern.logistics.awb_duplicate_detection
  target: validation_test.logistics.amount_semantics_not_by_name
  fields:
    edge_family: execution_guidance
    evidence_basis: query_pattern.fields.validation_tests
    confidence: high
    canonical_cognee_edge: true
    logistics_only: true
    canonical_edge_type: HAS_VALIDATION_TEST
    inverse_edge_type: VALIDATES_QUERY_PATTERN_OR_ENFORCES_RULE
    materialize_inverse: false
    edge_class: canonical
    source_type: query_pattern
    target_type: validation_test
```

```yaml
candidate_edge:
  edge_id: edge.query_pattern.logistics.awb_duplicate_detection.uses_output_contract.output_contract.logistics_data_quality_report
  edge_type: USES_OUTPUT_CONTRACT
  source: query_pattern.logistics.awb_duplicate_detection
  target: output_contract.logistics_data_quality_report
  fields:
    edge_family: execution_guidance
    evidence_basis: query_pattern.fields.output_contracts
    confidence: high
    canonical_cognee_edge: true
    logistics_only: true
    canonical_edge_type: USES_OUTPUT_CONTRACT
    inverse_edge_type: USED_BY_CONTEXT
    materialize_inverse: false
    edge_class: canonical
    source_type: query_pattern
    target_type: output_contract
```

```yaml
candidate_edge:
  edge_id: edge.query_pattern.logistics.rto_freight_validation.produces_metric.metric.rto_freight_amount
  edge_type: PRODUCES_METRIC
  source: query_pattern.logistics.rto_freight_validation
  target: metric.rto_freight_amount
  fields:
    edge_family: execution_guidance
    evidence_basis: query_pattern.fields.canonical_metric_or_object
    confidence: high
    canonical_cognee_edge: true
    logistics_only: true
    canonical_edge_type: PRODUCES_METRIC
    inverse_edge_type: PRODUCED_BY_QUERY_PATTERN
    materialize_inverse: false
    edge_class: canonical
    source_type: query_pattern
    target_type: metric
```

```yaml
candidate_edge:
  edge_id: edge.query_pattern.logistics.rto_freight_validation.uses_reconciliation_profile.reconciliation_profile.freight_charge_validation
  edge_type: USES_RECONCILIATION_PROFILE
  source: query_pattern.logistics.rto_freight_validation
  target: reconciliation_profile.freight_charge_validation
  fields:
    edge_family: execution_guidance
    evidence_basis: query_pattern.fields.canonical_metric_or_object
    confidence: high
    canonical_cognee_edge: true
    logistics_only: true
    canonical_edge_type: USES_RECONCILIATION_PROFILE
    inverse_edge_type: USED_BY_QUERY_PATTERN
    materialize_inverse: false
    edge_class: canonical
    source_type: query_pattern
    target_type: reconciliation_profile
```

```yaml
candidate_edge:
  edge_id: edge.query_pattern.logistics.rto_freight_validation.uses_table.table.zs_observe.shiprocket_invoice
  edge_type: USES_TABLE
  source: query_pattern.logistics.rto_freight_validation
  target: table.zs_observe.shiprocket_invoice
  fields:
    edge_family: metric_understanding
    evidence_basis: query_pattern.fields.required_tables
    confidence: high
    canonical_cognee_edge: true
    logistics_only: true
    canonical_edge_type: USES_TABLE
    inverse_edge_type: USED_BY_CONTEXT
    materialize_inverse: false
    edge_class: canonical
    source_type: query_pattern
    target_type: table
```

```yaml
candidate_edge:
  edge_id: edge.query_pattern.logistics.rto_freight_validation.uses_table.table.zs_observe.delhivery_invoice
  edge_type: USES_TABLE
  source: query_pattern.logistics.rto_freight_validation
  target: table.zs_observe.delhivery_invoice
  fields:
    edge_family: metric_understanding
    evidence_basis: query_pattern.fields.required_tables
    confidence: high
    canonical_cognee_edge: true
    logistics_only: true
    canonical_edge_type: USES_TABLE
    inverse_edge_type: USED_BY_CONTEXT
    materialize_inverse: false
    edge_class: canonical
    source_type: query_pattern
    target_type: table
```

```yaml
candidate_edge:
  edge_id: edge.query_pattern.logistics.rto_freight_validation.requires_rule.rule.logistics.rto_charge_only_for_rto
  edge_type: REQUIRES_RULE
  source: query_pattern.logistics.rto_freight_validation
  target: rule.logistics.rto_charge_only_for_rto
  fields:
    edge_family: execution_guidance
    evidence_basis: query_pattern.fields.rules
    confidence: high
    canonical_cognee_edge: true
    logistics_only: true
    canonical_edge_type: REQUIRES_RULE
    inverse_edge_type: REQUIRED_BY_QUERY_PATTERN
    materialize_inverse: false
    edge_class: canonical
    source_type: query_pattern
    target_type: rule
```

```yaml
candidate_edge:
  edge_id: edge.query_pattern.logistics.rto_freight_validation.has_validation_test.validation_test.logistics.required_scope_context
  edge_type: HAS_VALIDATION_TEST
  source: query_pattern.logistics.rto_freight_validation
  target: validation_test.logistics.required_scope_context
  fields:
    edge_family: execution_guidance
    evidence_basis: query_pattern.fields.validation_tests
    confidence: high
    canonical_cognee_edge: true
    logistics_only: true
    canonical_edge_type: HAS_VALIDATION_TEST
    inverse_edge_type: VALIDATES_QUERY_PATTERN_OR_ENFORCES_RULE
    materialize_inverse: false
    edge_class: canonical
    source_type: query_pattern
    target_type: validation_test
```

```yaml
candidate_edge:
  edge_id: edge.query_pattern.logistics.rto_freight_validation.has_validation_test.validation_test.logistics.amount_semantics_not_by_name
  edge_type: HAS_VALIDATION_TEST
  source: query_pattern.logistics.rto_freight_validation
  target: validation_test.logistics.amount_semantics_not_by_name
  fields:
    edge_family: execution_guidance
    evidence_basis: query_pattern.fields.validation_tests
    confidence: high
    canonical_cognee_edge: true
    logistics_only: true
    canonical_edge_type: HAS_VALIDATION_TEST
    inverse_edge_type: VALIDATES_QUERY_PATTERN_OR_ENFORCES_RULE
    materialize_inverse: false
    edge_class: canonical
    source_type: query_pattern
    target_type: validation_test
```

```yaml
candidate_edge:
  edge_id: edge.query_pattern.logistics.rto_freight_validation.uses_output_contract.output_contract.logistics_reconciliation_summary
  edge_type: USES_OUTPUT_CONTRACT
  source: query_pattern.logistics.rto_freight_validation
  target: output_contract.logistics_reconciliation_summary
  fields:
    edge_family: execution_guidance
    evidence_basis: query_pattern.fields.output_contracts
    confidence: high
    canonical_cognee_edge: true
    logistics_only: true
    canonical_edge_type: USES_OUTPUT_CONTRACT
    inverse_edge_type: USED_BY_CONTEXT
    materialize_inverse: false
    edge_class: canonical
    source_type: query_pattern
    target_type: output_contract
```

```yaml
candidate_edge:
  edge_id: edge.query_pattern.logistics.cod_fee_on_prepaid_detection.produces_metric.metric.cod_fee_amount
  edge_type: PRODUCES_METRIC
  source: query_pattern.logistics.cod_fee_on_prepaid_detection
  target: metric.cod_fee_amount
  fields:
    edge_family: execution_guidance
    evidence_basis: query_pattern.fields.canonical_metric_or_object
    confidence: high
    canonical_cognee_edge: true
    logistics_only: true
    canonical_edge_type: PRODUCES_METRIC
    inverse_edge_type: PRODUCED_BY_QUERY_PATTERN
    materialize_inverse: false
    edge_class: canonical
    source_type: query_pattern
    target_type: metric
```

```yaml
candidate_edge:
  edge_id: edge.query_pattern.logistics.cod_fee_on_prepaid_detection.uses_reconciliation_profile.reconciliation_profile.freight_charge_validation
  edge_type: USES_RECONCILIATION_PROFILE
  source: query_pattern.logistics.cod_fee_on_prepaid_detection
  target: reconciliation_profile.freight_charge_validation
  fields:
    edge_family: execution_guidance
    evidence_basis: query_pattern.fields.canonical_metric_or_object
    confidence: high
    canonical_cognee_edge: true
    logistics_only: true
    canonical_edge_type: USES_RECONCILIATION_PROFILE
    inverse_edge_type: USED_BY_QUERY_PATTERN
    materialize_inverse: false
    edge_class: canonical
    source_type: query_pattern
    target_type: reconciliation_profile
```

```yaml
candidate_edge:
  edge_id: edge.query_pattern.logistics.cod_fee_on_prepaid_detection.uses_table.table.zs_observe.shiprocket_invoice
  edge_type: USES_TABLE
  source: query_pattern.logistics.cod_fee_on_prepaid_detection
  target: table.zs_observe.shiprocket_invoice
  fields:
    edge_family: metric_understanding
    evidence_basis: query_pattern.fields.required_tables
    confidence: high
    canonical_cognee_edge: true
    logistics_only: true
    canonical_edge_type: USES_TABLE
    inverse_edge_type: USED_BY_CONTEXT
    materialize_inverse: false
    edge_class: canonical
    source_type: query_pattern
    target_type: table
```

```yaml
candidate_edge:
  edge_id: edge.query_pattern.logistics.cod_fee_on_prepaid_detection.uses_table.table.zs_observe.delhivery_invoice
  edge_type: USES_TABLE
  source: query_pattern.logistics.cod_fee_on_prepaid_detection
  target: table.zs_observe.delhivery_invoice
  fields:
    edge_family: metric_understanding
    evidence_basis: query_pattern.fields.required_tables
    confidence: high
    canonical_cognee_edge: true
    logistics_only: true
    canonical_edge_type: USES_TABLE
    inverse_edge_type: USED_BY_CONTEXT
    materialize_inverse: false
    edge_class: canonical
    source_type: query_pattern
    target_type: table
```

```yaml
candidate_edge:
  edge_id: edge.query_pattern.logistics.cod_fee_on_prepaid_detection.requires_rule.rule.logistics.cod_fee_only_for_cod
  edge_type: REQUIRES_RULE
  source: query_pattern.logistics.cod_fee_on_prepaid_detection
  target: rule.logistics.cod_fee_only_for_cod
  fields:
    edge_family: execution_guidance
    evidence_basis: query_pattern.fields.rules
    confidence: high
    canonical_cognee_edge: true
    logistics_only: true
    canonical_edge_type: REQUIRES_RULE
    inverse_edge_type: REQUIRED_BY_QUERY_PATTERN
    materialize_inverse: false
    edge_class: canonical
    source_type: query_pattern
    target_type: rule
```

```yaml
candidate_edge:
  edge_id: edge.query_pattern.logistics.cod_fee_on_prepaid_detection.has_validation_test.validation_test.logistics.required_scope_context
  edge_type: HAS_VALIDATION_TEST
  source: query_pattern.logistics.cod_fee_on_prepaid_detection
  target: validation_test.logistics.required_scope_context
  fields:
    edge_family: execution_guidance
    evidence_basis: query_pattern.fields.validation_tests
    confidence: high
    canonical_cognee_edge: true
    logistics_only: true
    canonical_edge_type: HAS_VALIDATION_TEST
    inverse_edge_type: VALIDATES_QUERY_PATTERN_OR_ENFORCES_RULE
    materialize_inverse: false
    edge_class: canonical
    source_type: query_pattern
    target_type: validation_test
```

```yaml
candidate_edge:
  edge_id: edge.query_pattern.logistics.cod_fee_on_prepaid_detection.has_validation_test.validation_test.logistics.amount_semantics_not_by_name
  edge_type: HAS_VALIDATION_TEST
  source: query_pattern.logistics.cod_fee_on_prepaid_detection
  target: validation_test.logistics.amount_semantics_not_by_name
  fields:
    edge_family: execution_guidance
    evidence_basis: query_pattern.fields.validation_tests
    confidence: high
    canonical_cognee_edge: true
    logistics_only: true
    canonical_edge_type: HAS_VALIDATION_TEST
    inverse_edge_type: VALIDATES_QUERY_PATTERN_OR_ENFORCES_RULE
    materialize_inverse: false
    edge_class: canonical
    source_type: query_pattern
    target_type: validation_test
```

```yaml
candidate_edge:
  edge_id: edge.query_pattern.logistics.cod_fee_on_prepaid_detection.uses_output_contract.output_contract.logistics_reconciliation_summary
  edge_type: USES_OUTPUT_CONTRACT
  source: query_pattern.logistics.cod_fee_on_prepaid_detection
  target: output_contract.logistics_reconciliation_summary
  fields:
    edge_family: execution_guidance
    evidence_basis: query_pattern.fields.output_contracts
    confidence: high
    canonical_cognee_edge: true
    logistics_only: true
    canonical_edge_type: USES_OUTPUT_CONTRACT
    inverse_edge_type: USED_BY_CONTEXT
    materialize_inverse: false
    edge_class: canonical
    source_type: query_pattern
    target_type: output_contract
```

```yaml
candidate_edge:
  edge_id: edge.query_pattern.logistics.empty_table_guardrail_query.uses_table.table.zs_observe.dtdc_invoice
  edge_type: USES_TABLE
  source: query_pattern.logistics.empty_table_guardrail_query
  target: table.zs_observe.dtdc_invoice
  fields:
    edge_family: metric_understanding
    evidence_basis: query_pattern.fields.required_tables
    confidence: high
    canonical_cognee_edge: true
    logistics_only: true
    canonical_edge_type: USES_TABLE
    inverse_edge_type: USED_BY_CONTEXT
    materialize_inverse: false
    edge_class: canonical
    source_type: query_pattern
    target_type: table
```

```yaml
candidate_edge:
  edge_id: edge.query_pattern.logistics.empty_table_guardrail_query.uses_table.table.zs_observe.ekart_invoice
  edge_type: USES_TABLE
  source: query_pattern.logistics.empty_table_guardrail_query
  target: table.zs_observe.ekart_invoice
  fields:
    edge_family: metric_understanding
    evidence_basis: query_pattern.fields.required_tables
    confidence: high
    canonical_cognee_edge: true
    logistics_only: true
    canonical_edge_type: USES_TABLE
    inverse_edge_type: USED_BY_CONTEXT
    materialize_inverse: false
    edge_class: canonical
    source_type: query_pattern
    target_type: table
```

```yaml
candidate_edge:
  edge_id: edge.query_pattern.logistics.empty_table_guardrail_query.uses_table.table.zs_observe.shiprocket_settlement_report
  edge_type: USES_TABLE
  source: query_pattern.logistics.empty_table_guardrail_query
  target: table.zs_observe.shiprocket_settlement_report
  fields:
    edge_family: metric_understanding
    evidence_basis: query_pattern.fields.required_tables
    confidence: high
    canonical_cognee_edge: true
    logistics_only: true
    canonical_edge_type: USES_TABLE
    inverse_edge_type: USED_BY_CONTEXT
    materialize_inverse: false
    edge_class: canonical
    source_type: query_pattern
    target_type: table
```

```yaml
candidate_edge:
  edge_id: edge.query_pattern.logistics.empty_table_guardrail_query.requires_rule.rule.logistics.empty_tables_schema_only
  edge_type: REQUIRES_RULE
  source: query_pattern.logistics.empty_table_guardrail_query
  target: rule.logistics.empty_tables_schema_only
  fields:
    edge_family: execution_guidance
    evidence_basis: query_pattern.fields.rules
    confidence: high
    canonical_cognee_edge: true
    logistics_only: true
    canonical_edge_type: REQUIRES_RULE
    inverse_edge_type: REQUIRED_BY_QUERY_PATTERN
    materialize_inverse: false
    edge_class: canonical
    source_type: query_pattern
    target_type: rule
```

```yaml
candidate_edge:
  edge_id: edge.query_pattern.logistics.empty_table_guardrail_query.requires_rule.rule.logistics.dtdc_invoice_empty
  edge_type: REQUIRES_RULE
  source: query_pattern.logistics.empty_table_guardrail_query
  target: rule.logistics.dtdc_invoice_empty
  fields:
    edge_family: execution_guidance
    evidence_basis: query_pattern.fields.rules
    confidence: high
    canonical_cognee_edge: true
    logistics_only: true
    canonical_edge_type: REQUIRES_RULE
    inverse_edge_type: REQUIRED_BY_QUERY_PATTERN
    materialize_inverse: false
    edge_class: canonical
    source_type: query_pattern
    target_type: rule
```

```yaml
candidate_edge:
  edge_id: edge.query_pattern.logistics.empty_table_guardrail_query.requires_rule.rule.logistics.ekart_invoice_empty
  edge_type: REQUIRES_RULE
  source: query_pattern.logistics.empty_table_guardrail_query
  target: rule.logistics.ekart_invoice_empty
  fields:
    edge_family: execution_guidance
    evidence_basis: query_pattern.fields.rules
    confidence: high
    canonical_cognee_edge: true
    logistics_only: true
    canonical_edge_type: REQUIRES_RULE
    inverse_edge_type: REQUIRED_BY_QUERY_PATTERN
    materialize_inverse: false
    edge_class: canonical
    source_type: query_pattern
    target_type: rule
```

```yaml
candidate_edge:
  edge_id: edge.query_pattern.logistics.empty_table_guardrail_query.requires_rule.rule.logistics.shiprocket_settlement_report_empty
  edge_type: REQUIRES_RULE
  source: query_pattern.logistics.empty_table_guardrail_query
  target: rule.logistics.shiprocket_settlement_report_empty
  fields:
    edge_family: execution_guidance
    evidence_basis: query_pattern.fields.rules
    confidence: high
    canonical_cognee_edge: true
    logistics_only: true
    canonical_edge_type: REQUIRES_RULE
    inverse_edge_type: REQUIRED_BY_QUERY_PATTERN
    materialize_inverse: false
    edge_class: canonical
    source_type: query_pattern
    target_type: rule
```

```yaml
candidate_edge:
  edge_id: edge.query_pattern.logistics.empty_table_guardrail_query.has_validation_test.validation_test.logistics.required_scope_context
  edge_type: HAS_VALIDATION_TEST
  source: query_pattern.logistics.empty_table_guardrail_query
  target: validation_test.logistics.required_scope_context
  fields:
    edge_family: execution_guidance
    evidence_basis: query_pattern.fields.validation_tests
    confidence: high
    canonical_cognee_edge: true
    logistics_only: true
    canonical_edge_type: HAS_VALIDATION_TEST
    inverse_edge_type: VALIDATES_QUERY_PATTERN_OR_ENFORCES_RULE
    materialize_inverse: false
    edge_class: canonical
    source_type: query_pattern
    target_type: validation_test
```

```yaml
candidate_edge:
  edge_id: edge.query_pattern.logistics.empty_table_guardrail_query.has_validation_test.validation_test.logistics.amount_semantics_not_by_name
  edge_type: HAS_VALIDATION_TEST
  source: query_pattern.logistics.empty_table_guardrail_query
  target: validation_test.logistics.amount_semantics_not_by_name
  fields:
    edge_family: execution_guidance
    evidence_basis: query_pattern.fields.validation_tests
    confidence: high
    canonical_cognee_edge: true
    logistics_only: true
    canonical_edge_type: HAS_VALIDATION_TEST
    inverse_edge_type: VALIDATES_QUERY_PATTERN_OR_ENFORCES_RULE
    materialize_inverse: false
    edge_class: canonical
    source_type: query_pattern
    target_type: validation_test
```

```yaml
candidate_edge:
  edge_id: edge.query_pattern.logistics.empty_table_guardrail_query.uses_output_contract.output_contract.logistics_data_quality_report
  edge_type: USES_OUTPUT_CONTRACT
  source: query_pattern.logistics.empty_table_guardrail_query
  target: output_contract.logistics_data_quality_report
  fields:
    edge_family: execution_guidance
    evidence_basis: query_pattern.fields.output_contracts
    confidence: high
    canonical_cognee_edge: true
    logistics_only: true
    canonical_edge_type: USES_OUTPUT_CONTRACT
    inverse_edge_type: USED_BY_CONTEXT
    materialize_inverse: false
    edge_class: canonical
    source_type: query_pattern
    target_type: output_contract
```

```yaml
candidate_edge:
  edge_id: edge.query_pattern.logistics.amount_semantics_audit.uses_table.table.zs_observe.shiprocket_oms
  edge_type: USES_TABLE
  source: query_pattern.logistics.amount_semantics_audit
  target: table.zs_observe.shiprocket_oms
  fields:
    edge_family: metric_understanding
    evidence_basis: query_pattern.fields.required_tables
    confidence: high
    canonical_cognee_edge: true
    logistics_only: true
    canonical_edge_type: USES_TABLE
    inverse_edge_type: USED_BY_CONTEXT
    materialize_inverse: false
    edge_class: canonical
    source_type: query_pattern
    target_type: table
```

```yaml
candidate_edge:
  edge_id: edge.query_pattern.logistics.amount_semantics_audit.uses_table.table.zs_observe.shiprocket_invoice
  edge_type: USES_TABLE
  source: query_pattern.logistics.amount_semantics_audit
  target: table.zs_observe.shiprocket_invoice
  fields:
    edge_family: metric_understanding
    evidence_basis: query_pattern.fields.required_tables
    confidence: high
    canonical_cognee_edge: true
    logistics_only: true
    canonical_edge_type: USES_TABLE
    inverse_edge_type: USED_BY_CONTEXT
    materialize_inverse: false
    edge_class: canonical
    source_type: query_pattern
    target_type: table
```

```yaml
candidate_edge:
  edge_id: edge.query_pattern.logistics.amount_semantics_audit.uses_table.table.zs_observe.shiprocket_settlement
  edge_type: USES_TABLE
  source: query_pattern.logistics.amount_semantics_audit
  target: table.zs_observe.shiprocket_settlement
  fields:
    edge_family: metric_understanding
    evidence_basis: query_pattern.fields.required_tables
    confidence: high
    canonical_cognee_edge: true
    logistics_only: true
    canonical_edge_type: USES_TABLE
    inverse_edge_type: USED_BY_CONTEXT
    materialize_inverse: false
    edge_class: canonical
    source_type: query_pattern
    target_type: table
```

```yaml
candidate_edge:
  edge_id: edge.query_pattern.logistics.amount_semantics_audit.uses_table.table.zs_observe.delhivery_invoice
  edge_type: USES_TABLE
  source: query_pattern.logistics.amount_semantics_audit
  target: table.zs_observe.delhivery_invoice
  fields:
    edge_family: metric_understanding
    evidence_basis: query_pattern.fields.required_tables
    confidence: high
    canonical_cognee_edge: true
    logistics_only: true
    canonical_edge_type: USES_TABLE
    inverse_edge_type: USED_BY_CONTEXT
    materialize_inverse: false
    edge_class: canonical
    source_type: query_pattern
    target_type: table
```

```yaml
candidate_edge:
  edge_id: edge.query_pattern.logistics.amount_semantics_audit.requires_rule.rule.logistics.amount_semantics_not_by_name
  edge_type: REQUIRES_RULE
  source: query_pattern.logistics.amount_semantics_audit
  target: rule.logistics.amount_semantics_not_by_name
  fields:
    edge_family: execution_guidance
    evidence_basis: query_pattern.fields.rules
    confidence: high
    canonical_cognee_edge: true
    logistics_only: true
    canonical_edge_type: REQUIRES_RULE
    inverse_edge_type: REQUIRED_BY_QUERY_PATTERN
    materialize_inverse: false
    edge_class: canonical
    source_type: query_pattern
    target_type: rule
```

```yaml
candidate_edge:
  edge_id: edge.query_pattern.logistics.amount_semantics_audit.requires_rule.rule.logistics.charged_amount_table_specific
  edge_type: REQUIRES_RULE
  source: query_pattern.logistics.amount_semantics_audit
  target: rule.logistics.charged_amount_table_specific
  fields:
    edge_family: execution_guidance
    evidence_basis: query_pattern.fields.rules
    confidence: high
    canonical_cognee_edge: true
    logistics_only: true
    canonical_edge_type: REQUIRES_RULE
    inverse_edge_type: REQUIRED_BY_QUERY_PATTERN
    materialize_inverse: false
    edge_class: canonical
    source_type: query_pattern
    target_type: rule
```

```yaml
candidate_edge:
  edge_id: edge.query_pattern.logistics.amount_semantics_audit.has_validation_test.validation_test.logistics.required_scope_context
  edge_type: HAS_VALIDATION_TEST
  source: query_pattern.logistics.amount_semantics_audit
  target: validation_test.logistics.required_scope_context
  fields:
    edge_family: execution_guidance
    evidence_basis: query_pattern.fields.validation_tests
    confidence: high
    canonical_cognee_edge: true
    logistics_only: true
    canonical_edge_type: HAS_VALIDATION_TEST
    inverse_edge_type: VALIDATES_QUERY_PATTERN_OR_ENFORCES_RULE
    materialize_inverse: false
    edge_class: canonical
    source_type: query_pattern
    target_type: validation_test
```

```yaml
candidate_edge:
  edge_id: edge.query_pattern.logistics.amount_semantics_audit.has_validation_test.validation_test.logistics.amount_semantics_not_by_name
  edge_type: HAS_VALIDATION_TEST
  source: query_pattern.logistics.amount_semantics_audit
  target: validation_test.logistics.amount_semantics_not_by_name
  fields:
    edge_family: execution_guidance
    evidence_basis: query_pattern.fields.validation_tests
    confidence: high
    canonical_cognee_edge: true
    logistics_only: true
    canonical_edge_type: HAS_VALIDATION_TEST
    inverse_edge_type: VALIDATES_QUERY_PATTERN_OR_ENFORCES_RULE
    materialize_inverse: false
    edge_class: canonical
    source_type: query_pattern
    target_type: validation_test
```

```yaml
candidate_edge:
  edge_id: edge.query_pattern.logistics.amount_semantics_audit.uses_output_contract.output_contract.logistics_data_quality_report
  edge_type: USES_OUTPUT_CONTRACT
  source: query_pattern.logistics.amount_semantics_audit
  target: output_contract.logistics_data_quality_report
  fields:
    edge_family: execution_guidance
    evidence_basis: query_pattern.fields.output_contracts
    confidence: high
    canonical_cognee_edge: true
    logistics_only: true
    canonical_edge_type: USES_OUTPUT_CONTRACT
    inverse_edge_type: USED_BY_CONTEXT
    materialize_inverse: false
    edge_class: canonical
    source_type: query_pattern
    target_type: output_contract
```

```yaml
candidate_edge:
  edge_id: edge.query_pattern.logistics.scope_binding_injection_check.requires_rule.rule.logistics.required_scope_context
  edge_type: REQUIRES_RULE
  source: query_pattern.logistics.scope_binding_injection_check
  target: rule.logistics.required_scope_context
  fields:
    edge_family: execution_guidance
    evidence_basis: query_pattern.fields.rules
    confidence: high
    canonical_cognee_edge: true
    logistics_only: true
    canonical_edge_type: REQUIRES_RULE
    inverse_edge_type: REQUIRED_BY_QUERY_PATTERN
    materialize_inverse: false
    edge_class: canonical
    source_type: query_pattern
    target_type: rule
```

```yaml
candidate_edge:
  edge_id: edge.query_pattern.logistics.scope_binding_injection_check.requires_rule.rule.logistics.account_filters_from_adb_only
  edge_type: REQUIRES_RULE
  source: query_pattern.logistics.scope_binding_injection_check
  target: rule.logistics.account_filters_from_adb_only
  fields:
    edge_family: execution_guidance
    evidence_basis: query_pattern.fields.rules
    confidence: high
    canonical_cognee_edge: true
    logistics_only: true
    canonical_edge_type: REQUIRES_RULE
    inverse_edge_type: REQUIRED_BY_QUERY_PATTERN
    materialize_inverse: false
    edge_class: canonical
    source_type: query_pattern
    target_type: rule
```

```yaml
candidate_edge:
  edge_id: edge.query_pattern.logistics.scope_binding_injection_check.requires_rule.rule.logistics.business_flow_binding_required_for_cross_platform
  edge_type: REQUIRES_RULE
  source: query_pattern.logistics.scope_binding_injection_check
  target: rule.logistics.business_flow_binding_required_for_cross_platform
  fields:
    edge_family: execution_guidance
    evidence_basis: query_pattern.fields.rules
    confidence: high
    canonical_cognee_edge: true
    logistics_only: true
    canonical_edge_type: REQUIRES_RULE
    inverse_edge_type: REQUIRED_BY_QUERY_PATTERN
    materialize_inverse: false
    edge_class: canonical
    source_type: query_pattern
    target_type: rule
```

```yaml
candidate_edge:
  edge_id: edge.query_pattern.logistics.scope_binding_injection_check.has_validation_test.validation_test.logistics.required_scope_context
  edge_type: HAS_VALIDATION_TEST
  source: query_pattern.logistics.scope_binding_injection_check
  target: validation_test.logistics.required_scope_context
  fields:
    edge_family: execution_guidance
    evidence_basis: query_pattern.fields.validation_tests
    confidence: high
    canonical_cognee_edge: true
    logistics_only: true
    canonical_edge_type: HAS_VALIDATION_TEST
    inverse_edge_type: VALIDATES_QUERY_PATTERN_OR_ENFORCES_RULE
    materialize_inverse: false
    edge_class: canonical
    source_type: query_pattern
    target_type: validation_test
```

```yaml
candidate_edge:
  edge_id: edge.query_pattern.logistics.scope_binding_injection_check.has_validation_test.validation_test.logistics.amount_semantics_not_by_name
  edge_type: HAS_VALIDATION_TEST
  source: query_pattern.logistics.scope_binding_injection_check
  target: validation_test.logistics.amount_semantics_not_by_name
  fields:
    edge_family: execution_guidance
    evidence_basis: query_pattern.fields.validation_tests
    confidence: high
    canonical_cognee_edge: true
    logistics_only: true
    canonical_edge_type: HAS_VALIDATION_TEST
    inverse_edge_type: VALIDATES_QUERY_PATTERN_OR_ENFORCES_RULE
    materialize_inverse: false
    edge_class: canonical
    source_type: query_pattern
    target_type: validation_test
```

```yaml
candidate_edge:
  edge_id: edge.query_pattern.logistics.scope_binding_injection_check.uses_output_contract.output_contract.logistics_data_quality_report
  edge_type: USES_OUTPUT_CONTRACT
  source: query_pattern.logistics.scope_binding_injection_check
  target: output_contract.logistics_data_quality_report
  fields:
    edge_family: execution_guidance
    evidence_basis: query_pattern.fields.output_contracts
    confidence: high
    canonical_cognee_edge: true
    logistics_only: true
    canonical_edge_type: USES_OUTPUT_CONTRACT
    inverse_edge_type: USED_BY_CONTEXT
    materialize_inverse: false
    edge_class: canonical
    source_type: query_pattern
    target_type: output_contract
```

```yaml
candidate_edge:
  edge_id: edge.query_pattern.logistics.bank_credit_unmatched_courier_reference.produces_metric.metric.unmatched_bank_credit_amount
  edge_type: PRODUCES_METRIC
  source: query_pattern.logistics.bank_credit_unmatched_courier_reference
  target: metric.unmatched_bank_credit_amount
  fields:
    edge_family: execution_guidance
    evidence_basis: query_pattern.fields.canonical_metric_or_object
    confidence: high
    canonical_cognee_edge: true
    logistics_only: true
    canonical_edge_type: PRODUCES_METRIC
    inverse_edge_type: PRODUCED_BY_QUERY_PATTERN
    materialize_inverse: false
    edge_class: canonical
    source_type: query_pattern
    target_type: metric
```

```yaml
candidate_edge:
  edge_id: edge.query_pattern.logistics.bank_credit_unmatched_courier_reference.uses_reconciliation_profile.reconciliation_profile.courier_batch_to_bank_credit
  edge_type: USES_RECONCILIATION_PROFILE
  source: query_pattern.logistics.bank_credit_unmatched_courier_reference
  target: reconciliation_profile.courier_batch_to_bank_credit
  fields:
    edge_family: execution_guidance
    evidence_basis: query_pattern.fields.canonical_metric_or_object
    confidence: high
    canonical_cognee_edge: true
    logistics_only: true
    canonical_edge_type: USES_RECONCILIATION_PROFILE
    inverse_edge_type: USED_BY_QUERY_PATTERN
    materialize_inverse: false
    edge_class: canonical
    source_type: query_pattern
    target_type: reconciliation_profile
```

```yaml
candidate_edge:
  edge_id: edge.query_pattern.logistics.bank_credit_unmatched_courier_reference.uses_table.table.zs_observe.delhivery_settlement
  edge_type: USES_TABLE
  source: query_pattern.logistics.bank_credit_unmatched_courier_reference
  target: table.zs_observe.delhivery_settlement
  fields:
    edge_family: metric_understanding
    evidence_basis: query_pattern.fields.required_tables
    confidence: high
    canonical_cognee_edge: true
    logistics_only: true
    canonical_edge_type: USES_TABLE
    inverse_edge_type: USED_BY_CONTEXT
    materialize_inverse: false
    edge_class: canonical
    source_type: query_pattern
    target_type: table
```

```yaml
candidate_edge:
  edge_id: edge.query_pattern.logistics.bank_credit_unmatched_courier_reference.uses_table.table.zs_observe.dtdc_settlement
  edge_type: USES_TABLE
  source: query_pattern.logistics.bank_credit_unmatched_courier_reference
  target: table.zs_observe.dtdc_settlement
  fields:
    edge_family: metric_understanding
    evidence_basis: query_pattern.fields.required_tables
    confidence: high
    canonical_cognee_edge: true
    logistics_only: true
    canonical_edge_type: USES_TABLE
    inverse_edge_type: USED_BY_CONTEXT
    materialize_inverse: false
    edge_class: canonical
    source_type: query_pattern
    target_type: table
```

```yaml
candidate_edge:
  edge_id: edge.query_pattern.logistics.bank_credit_unmatched_courier_reference.uses_table.table.zs_observe.ekart_settlement
  edge_type: USES_TABLE
  source: query_pattern.logistics.bank_credit_unmatched_courier_reference
  target: table.zs_observe.ekart_settlement
  fields:
    edge_family: metric_understanding
    evidence_basis: query_pattern.fields.required_tables
    confidence: high
    canonical_cognee_edge: true
    logistics_only: true
    canonical_edge_type: USES_TABLE
    inverse_edge_type: USED_BY_CONTEXT
    materialize_inverse: false
    edge_class: canonical
    source_type: query_pattern
    target_type: table
```

```yaml
candidate_edge:
  edge_id: edge.query_pattern.logistics.bank_credit_unmatched_courier_reference.requires_rule.rule.logistics.bank_reference_required_for_bank_match
  edge_type: REQUIRES_RULE
  source: query_pattern.logistics.bank_credit_unmatched_courier_reference
  target: rule.logistics.bank_reference_required_for_bank_match
  fields:
    edge_family: execution_guidance
    evidence_basis: query_pattern.fields.rules
    confidence: high
    canonical_cognee_edge: true
    logistics_only: true
    canonical_edge_type: REQUIRES_RULE
    inverse_edge_type: REQUIRED_BY_QUERY_PATTERN
    materialize_inverse: false
    edge_class: canonical
    source_type: query_pattern
    target_type: rule
```

```yaml
candidate_edge:
  edge_id: edge.query_pattern.logistics.bank_credit_unmatched_courier_reference.requires_rule.rule.logistics.utr_preferred_for_bank_bridge
  edge_type: REQUIRES_RULE
  source: query_pattern.logistics.bank_credit_unmatched_courier_reference
  target: rule.logistics.utr_preferred_for_bank_bridge
  fields:
    edge_family: execution_guidance
    evidence_basis: query_pattern.fields.rules
    confidence: high
    canonical_cognee_edge: true
    logistics_only: true
    canonical_edge_type: REQUIRES_RULE
    inverse_edge_type: REQUIRED_BY_QUERY_PATTERN
    materialize_inverse: false
    edge_class: canonical
    source_type: query_pattern
    target_type: rule
```

```yaml
candidate_edge:
  edge_id: edge.query_pattern.logistics.bank_credit_unmatched_courier_reference.has_validation_test.validation_test.logistics.required_scope_context
  edge_type: HAS_VALIDATION_TEST
  source: query_pattern.logistics.bank_credit_unmatched_courier_reference
  target: validation_test.logistics.required_scope_context
  fields:
    edge_family: execution_guidance
    evidence_basis: query_pattern.fields.validation_tests
    confidence: high
    canonical_cognee_edge: true
    logistics_only: true
    canonical_edge_type: HAS_VALIDATION_TEST
    inverse_edge_type: VALIDATES_QUERY_PATTERN_OR_ENFORCES_RULE
    materialize_inverse: false
    edge_class: canonical
    source_type: query_pattern
    target_type: validation_test
```

```yaml
candidate_edge:
  edge_id: edge.query_pattern.logistics.bank_credit_unmatched_courier_reference.has_validation_test.validation_test.logistics.amount_semantics_not_by_name
  edge_type: HAS_VALIDATION_TEST
  source: query_pattern.logistics.bank_credit_unmatched_courier_reference
  target: validation_test.logistics.amount_semantics_not_by_name
  fields:
    edge_family: execution_guidance
    evidence_basis: query_pattern.fields.validation_tests
    confidence: high
    canonical_cognee_edge: true
    logistics_only: true
    canonical_edge_type: HAS_VALIDATION_TEST
    inverse_edge_type: VALIDATES_QUERY_PATTERN_OR_ENFORCES_RULE
    materialize_inverse: false
    edge_class: canonical
    source_type: query_pattern
    target_type: validation_test
```

```yaml
candidate_edge:
  edge_id: edge.query_pattern.logistics.bank_credit_unmatched_courier_reference.uses_output_contract.output_contract.logistics_reconciliation_summary
  edge_type: USES_OUTPUT_CONTRACT
  source: query_pattern.logistics.bank_credit_unmatched_courier_reference
  target: output_contract.logistics_reconciliation_summary
  fields:
    edge_family: execution_guidance
    evidence_basis: query_pattern.fields.output_contracts
    confidence: high
    canonical_cognee_edge: true
    logistics_only: true
    canonical_edge_type: USES_OUTPUT_CONTRACT
    inverse_edge_type: USED_BY_CONTEXT
    materialize_inverse: false
    edge_class: canonical
    source_type: query_pattern
    target_type: output_contract
```

```yaml
candidate_edge:
  edge_id: edge.query_pattern.logistics.end_to_end_logistics_money_flow_trace.produces_metric.metric.freight_billed_amount
  edge_type: PRODUCES_METRIC
  source: query_pattern.logistics.end_to_end_logistics_money_flow_trace
  target: metric.freight_billed_amount
  fields:
    edge_family: execution_guidance
    evidence_basis: query_pattern.fields.canonical_metric_or_object
    confidence: high
    canonical_cognee_edge: true
    logistics_only: true
    canonical_edge_type: PRODUCES_METRIC
    inverse_edge_type: PRODUCED_BY_QUERY_PATTERN
    materialize_inverse: false
    edge_class: canonical
    source_type: query_pattern
    target_type: metric
```

```yaml
candidate_edge:
  edge_id: edge.query_pattern.logistics.end_to_end_logistics_money_flow_trace.produces_metric.metric.cod_remitted_amount
  edge_type: PRODUCES_METRIC
  source: query_pattern.logistics.end_to_end_logistics_money_flow_trace
  target: metric.cod_remitted_amount
  fields:
    edge_family: execution_guidance
    evidence_basis: query_pattern.fields.canonical_metric_or_object
    confidence: high
    canonical_cognee_edge: true
    logistics_only: true
    canonical_edge_type: PRODUCES_METRIC
    inverse_edge_type: PRODUCED_BY_QUERY_PATTERN
    materialize_inverse: false
    edge_class: canonical
    source_type: query_pattern
    target_type: metric
```

```yaml
candidate_edge:
  edge_id: edge.query_pattern.logistics.end_to_end_logistics_money_flow_trace.produces_metric.metric.batch_settlement_amount
  edge_type: PRODUCES_METRIC
  source: query_pattern.logistics.end_to_end_logistics_money_flow_trace
  target: metric.batch_settlement_amount
  fields:
    edge_family: execution_guidance
    evidence_basis: query_pattern.fields.canonical_metric_or_object
    confidence: high
    canonical_cognee_edge: true
    logistics_only: true
    canonical_edge_type: PRODUCES_METRIC
    inverse_edge_type: PRODUCED_BY_QUERY_PATTERN
    materialize_inverse: false
    edge_class: canonical
    source_type: query_pattern
    target_type: metric
```

```yaml
candidate_edge:
  edge_id: edge.query_pattern.logistics.end_to_end_logistics_money_flow_trace.uses_reconciliation_profile.reconciliation_profile.order_to_shipment
  edge_type: USES_RECONCILIATION_PROFILE
  source: query_pattern.logistics.end_to_end_logistics_money_flow_trace
  target: reconciliation_profile.order_to_shipment
  fields:
    edge_family: execution_guidance
    evidence_basis: query_pattern.fields.canonical_metric_or_object
    confidence: high
    canonical_cognee_edge: true
    logistics_only: true
    canonical_edge_type: USES_RECONCILIATION_PROFILE
    inverse_edge_type: USED_BY_QUERY_PATTERN
    materialize_inverse: false
    edge_class: canonical
    source_type: query_pattern
    target_type: reconciliation_profile
```

```yaml
candidate_edge:
  edge_id: edge.query_pattern.logistics.end_to_end_logistics_money_flow_trace.uses_reconciliation_profile.reconciliation_profile.shipment_to_freight_invoice
  edge_type: USES_RECONCILIATION_PROFILE
  source: query_pattern.logistics.end_to_end_logistics_money_flow_trace
  target: reconciliation_profile.shipment_to_freight_invoice
  fields:
    edge_family: execution_guidance
    evidence_basis: query_pattern.fields.canonical_metric_or_object
    confidence: high
    canonical_cognee_edge: true
    logistics_only: true
    canonical_edge_type: USES_RECONCILIATION_PROFILE
    inverse_edge_type: USED_BY_QUERY_PATTERN
    materialize_inverse: false
    edge_class: canonical
    source_type: query_pattern
    target_type: reconciliation_profile
```

```yaml
candidate_edge:
  edge_id: edge.query_pattern.logistics.end_to_end_logistics_money_flow_trace.uses_reconciliation_profile.reconciliation_profile.cod_expected_to_courier_remittance
  edge_type: USES_RECONCILIATION_PROFILE
  source: query_pattern.logistics.end_to_end_logistics_money_flow_trace
  target: reconciliation_profile.cod_expected_to_courier_remittance
  fields:
    edge_family: execution_guidance
    evidence_basis: query_pattern.fields.canonical_metric_or_object
    confidence: high
    canonical_cognee_edge: true
    logistics_only: true
    canonical_edge_type: USES_RECONCILIATION_PROFILE
    inverse_edge_type: USED_BY_QUERY_PATTERN
    materialize_inverse: false
    edge_class: canonical
    source_type: query_pattern
    target_type: reconciliation_profile
```

```yaml
candidate_edge:
  edge_id: edge.query_pattern.logistics.end_to_end_logistics_money_flow_trace.uses_reconciliation_profile.reconciliation_profile.courier_batch_to_bank_credit
  edge_type: USES_RECONCILIATION_PROFILE
  source: query_pattern.logistics.end_to_end_logistics_money_flow_trace
  target: reconciliation_profile.courier_batch_to_bank_credit
  fields:
    edge_family: execution_guidance
    evidence_basis: query_pattern.fields.canonical_metric_or_object
    confidence: high
    canonical_cognee_edge: true
    logistics_only: true
    canonical_edge_type: USES_RECONCILIATION_PROFILE
    inverse_edge_type: USED_BY_QUERY_PATTERN
    materialize_inverse: false
    edge_class: canonical
    source_type: query_pattern
    target_type: reconciliation_profile
```

```yaml
candidate_edge:
  edge_id: edge.query_pattern.logistics.end_to_end_logistics_money_flow_trace.uses_table.table.zs_observe.shiprocket_oms
  edge_type: USES_TABLE
  source: query_pattern.logistics.end_to_end_logistics_money_flow_trace
  target: table.zs_observe.shiprocket_oms
  fields:
    edge_family: metric_understanding
    evidence_basis: query_pattern.fields.required_tables
    confidence: high
    canonical_cognee_edge: true
    logistics_only: true
    canonical_edge_type: USES_TABLE
    inverse_edge_type: USED_BY_CONTEXT
    materialize_inverse: false
    edge_class: canonical
    source_type: query_pattern
    target_type: table
```

```yaml
candidate_edge:
  edge_id: edge.query_pattern.logistics.end_to_end_logistics_money_flow_trace.uses_table.table.zs_observe.shiprocket_invoice
  edge_type: USES_TABLE
  source: query_pattern.logistics.end_to_end_logistics_money_flow_trace
  target: table.zs_observe.shiprocket_invoice
  fields:
    edge_family: metric_understanding
    evidence_basis: query_pattern.fields.required_tables
    confidence: high
    canonical_cognee_edge: true
    logistics_only: true
    canonical_edge_type: USES_TABLE
    inverse_edge_type: USED_BY_CONTEXT
    materialize_inverse: false
    edge_class: canonical
    source_type: query_pattern
    target_type: table
```

```yaml
candidate_edge:
  edge_id: edge.query_pattern.logistics.end_to_end_logistics_money_flow_trace.uses_table.table.zs_observe.shiprocket_settlement
  edge_type: USES_TABLE
  source: query_pattern.logistics.end_to_end_logistics_money_flow_trace
  target: table.zs_observe.shiprocket_settlement
  fields:
    edge_family: metric_understanding
    evidence_basis: query_pattern.fields.required_tables
    confidence: high
    canonical_cognee_edge: true
    logistics_only: true
    canonical_edge_type: USES_TABLE
    inverse_edge_type: USED_BY_CONTEXT
    materialize_inverse: false
    edge_class: canonical
    source_type: query_pattern
    target_type: table
```

```yaml
candidate_edge:
  edge_id: edge.query_pattern.logistics.end_to_end_logistics_money_flow_trace.requires_rule.rule.logistics.business_flow_binding_required_for_cross_platform
  edge_type: REQUIRES_RULE
  source: query_pattern.logistics.end_to_end_logistics_money_flow_trace
  target: rule.logistics.business_flow_binding_required_for_cross_platform
  fields:
    edge_family: execution_guidance
    evidence_basis: query_pattern.fields.rules
    confidence: high
    canonical_cognee_edge: true
    logistics_only: true
    canonical_edge_type: REQUIRES_RULE
    inverse_edge_type: REQUIRED_BY_QUERY_PATTERN
    materialize_inverse: false
    edge_class: canonical
    source_type: query_pattern
    target_type: rule
```

```yaml
candidate_edge:
  edge_id: edge.query_pattern.logistics.end_to_end_logistics_money_flow_trace.requires_rule.rule.logistics.do_not_join_awb_to_bank_without_batch
  edge_type: REQUIRES_RULE
  source: query_pattern.logistics.end_to_end_logistics_money_flow_trace
  target: rule.logistics.do_not_join_awb_to_bank_without_batch
  fields:
    edge_family: execution_guidance
    evidence_basis: query_pattern.fields.rules
    confidence: high
    canonical_cognee_edge: true
    logistics_only: true
    canonical_edge_type: REQUIRES_RULE
    inverse_edge_type: REQUIRED_BY_QUERY_PATTERN
    materialize_inverse: false
    edge_class: canonical
    source_type: query_pattern
    target_type: rule
```

```yaml
candidate_edge:
  edge_id: edge.query_pattern.logistics.end_to_end_logistics_money_flow_trace.has_validation_test.validation_test.logistics.required_scope_context
  edge_type: HAS_VALIDATION_TEST
  source: query_pattern.logistics.end_to_end_logistics_money_flow_trace
  target: validation_test.logistics.required_scope_context
  fields:
    edge_family: execution_guidance
    evidence_basis: query_pattern.fields.validation_tests
    confidence: high
    canonical_cognee_edge: true
    logistics_only: true
    canonical_edge_type: HAS_VALIDATION_TEST
    inverse_edge_type: VALIDATES_QUERY_PATTERN_OR_ENFORCES_RULE
    materialize_inverse: false
    edge_class: canonical
    source_type: query_pattern
    target_type: validation_test
```

```yaml
candidate_edge:
  edge_id: edge.query_pattern.logistics.end_to_end_logistics_money_flow_trace.has_validation_test.validation_test.logistics.amount_semantics_not_by_name
  edge_type: HAS_VALIDATION_TEST
  source: query_pattern.logistics.end_to_end_logistics_money_flow_trace
  target: validation_test.logistics.amount_semantics_not_by_name
  fields:
    edge_family: execution_guidance
    evidence_basis: query_pattern.fields.validation_tests
    confidence: high
    canonical_cognee_edge: true
    logistics_only: true
    canonical_edge_type: HAS_VALIDATION_TEST
    inverse_edge_type: VALIDATES_QUERY_PATTERN_OR_ENFORCES_RULE
    materialize_inverse: false
    edge_class: canonical
    source_type: query_pattern
    target_type: validation_test
```

```yaml
candidate_edge:
  edge_id: edge.query_pattern.logistics.end_to_end_logistics_money_flow_trace.uses_output_contract.output_contract.logistics_money_flow_trace
  edge_type: USES_OUTPUT_CONTRACT
  source: query_pattern.logistics.end_to_end_logistics_money_flow_trace
  target: output_contract.logistics_money_flow_trace
  fields:
    edge_family: execution_guidance
    evidence_basis: query_pattern.fields.output_contracts
    confidence: high
    canonical_cognee_edge: true
    logistics_only: true
    canonical_edge_type: USES_OUTPUT_CONTRACT
    inverse_edge_type: USED_BY_CONTEXT
    materialize_inverse: false
    edge_class: canonical
    source_type: query_pattern
    target_type: output_contract
```

```yaml
candidate_edge:
  edge_id: edge.execution_constraint_set.logistics_general_analytics.includes_rule.rule.logistics.required_scope_context
  edge_type: INCLUDES_RULE
  source: execution_constraint_set.logistics_general_analytics
  target: rule.logistics.required_scope_context
  fields:
    edge_family: execution_guidance
    evidence_basis: execution_constraint_set.fields.rules
    confidence: high
    canonical_cognee_edge: true
    logistics_only: true
    canonical_edge_type: INCLUDES_RULE
    inverse_edge_type: INCLUDED_IN_CONSTRAINT_SET
    materialize_inverse: false
    edge_class: canonical
    source_type: execution_constraint_set
    target_type: rule
```

```yaml
candidate_edge:
  edge_id: edge.execution_constraint_set.logistics_general_analytics.includes_rule.rule.logistics.business_flow_binding_required_for_cross_platform
  edge_type: INCLUDES_RULE
  source: execution_constraint_set.logistics_general_analytics
  target: rule.logistics.business_flow_binding_required_for_cross_platform
  fields:
    edge_family: execution_guidance
    evidence_basis: execution_constraint_set.fields.rules
    confidence: high
    canonical_cognee_edge: true
    logistics_only: true
    canonical_edge_type: INCLUDES_RULE
    inverse_edge_type: INCLUDED_IN_CONSTRAINT_SET
    materialize_inverse: false
    edge_class: canonical
    source_type: execution_constraint_set
    target_type: rule
```

```yaml
candidate_edge:
  edge_id: edge.execution_constraint_set.logistics_general_analytics.includes_rule.rule.logistics.do_not_create_bfb_from_generic_vendor_doc
  edge_type: INCLUDES_RULE
  source: execution_constraint_set.logistics_general_analytics
  target: rule.logistics.do_not_create_bfb_from_generic_vendor_doc
  fields:
    edge_family: execution_guidance
    evidence_basis: execution_constraint_set.fields.rules
    confidence: high
    canonical_cognee_edge: true
    logistics_only: true
    canonical_edge_type: INCLUDES_RULE
    inverse_edge_type: INCLUDED_IN_CONSTRAINT_SET
    materialize_inverse: false
    edge_class: canonical
    source_type: execution_constraint_set
    target_type: rule
```

```yaml
candidate_edge:
  edge_id: edge.execution_constraint_set.logistics_general_analytics.includes_rule.rule.logistics.amount_semantics_not_by_name
  edge_type: INCLUDES_RULE
  source: execution_constraint_set.logistics_general_analytics
  target: rule.logistics.amount_semantics_not_by_name
  fields:
    edge_family: execution_guidance
    evidence_basis: execution_constraint_set.fields.rules
    confidence: high
    canonical_cognee_edge: true
    logistics_only: true
    canonical_edge_type: INCLUDES_RULE
    inverse_edge_type: INCLUDED_IN_CONSTRAINT_SET
    materialize_inverse: false
    edge_class: canonical
    source_type: execution_constraint_set
    target_type: rule
```

```yaml
candidate_edge:
  edge_id: edge.execution_constraint_set.logistics_general_analytics.includes_rule.rule.logistics.charged_amount_table_specific
  edge_type: INCLUDES_RULE
  source: execution_constraint_set.logistics_general_analytics
  target: rule.logistics.charged_amount_table_specific
  fields:
    edge_family: execution_guidance
    evidence_basis: execution_constraint_set.fields.rules
    confidence: high
    canonical_cognee_edge: true
    logistics_only: true
    canonical_edge_type: INCLUDES_RULE
    inverse_edge_type: INCLUDED_IN_CONSTRAINT_SET
    materialize_inverse: false
    edge_class: canonical
    source_type: execution_constraint_set
    target_type: rule
```

```yaml
candidate_edge:
  edge_id: edge.execution_constraint_set.logistics_general_analytics.includes_rule.rule.logistics.active_filter_when_available
  edge_type: INCLUDES_RULE
  source: execution_constraint_set.logistics_general_analytics
  target: rule.logistics.active_filter_when_available
  fields:
    edge_family: execution_guidance
    evidence_basis: execution_constraint_set.fields.rules
    confidence: high
    canonical_cognee_edge: true
    logistics_only: true
    canonical_edge_type: INCLUDES_RULE
    inverse_edge_type: INCLUDED_IN_CONSTRAINT_SET
    materialize_inverse: false
    edge_class: canonical
    source_type: execution_constraint_set
    target_type: rule
```

```yaml
candidate_edge:
  edge_id: edge.execution_constraint_set.logistics_general_analytics.includes_rule.rule.logistics.empty_tables_schema_only
  edge_type: INCLUDES_RULE
  source: execution_constraint_set.logistics_general_analytics
  target: rule.logistics.empty_tables_schema_only
  fields:
    edge_family: execution_guidance
    evidence_basis: execution_constraint_set.fields.rules
    confidence: high
    canonical_cognee_edge: true
    logistics_only: true
    canonical_edge_type: INCLUDES_RULE
    inverse_edge_type: INCLUDED_IN_CONSTRAINT_SET
    materialize_inverse: false
    edge_class: canonical
    source_type: execution_constraint_set
    target_type: rule
```

```yaml
candidate_edge:
  edge_id: edge.execution_constraint_set.logistics_general_analytics.includes_rule.rule.logistics.low_confidence_requires_warning
  edge_type: INCLUDES_RULE
  source: execution_constraint_set.logistics_general_analytics
  target: rule.logistics.low_confidence_requires_warning
  fields:
    edge_family: execution_guidance
    evidence_basis: execution_constraint_set.fields.rules
    confidence: high
    canonical_cognee_edge: true
    logistics_only: true
    canonical_edge_type: INCLUDES_RULE
    inverse_edge_type: INCLUDED_IN_CONSTRAINT_SET
    materialize_inverse: false
    edge_class: canonical
    source_type: execution_constraint_set
    target_type: rule
```

```yaml
candidate_edge:
  edge_id: edge.execution_constraint_set.logistics_general_analytics.includes_rule.rule.logistics.fallback_sources_explicit_only
  edge_type: INCLUDES_RULE
  source: execution_constraint_set.logistics_general_analytics
  target: rule.logistics.fallback_sources_explicit_only
  fields:
    edge_family: execution_guidance
    evidence_basis: execution_constraint_set.fields.rules
    confidence: high
    canonical_cognee_edge: true
    logistics_only: true
    canonical_edge_type: INCLUDES_RULE
    inverse_edge_type: INCLUDED_IN_CONSTRAINT_SET
    materialize_inverse: false
    edge_class: canonical
    source_type: execution_constraint_set
    target_type: rule
```

```yaml
candidate_edge:
  edge_id: edge.execution_constraint_set.logistics_general_analytics.includes_rule.rule.logistics.awb_primary_reconciliation_unit
  edge_type: INCLUDES_RULE
  source: execution_constraint_set.logistics_general_analytics
  target: rule.logistics.awb_primary_reconciliation_unit
  fields:
    edge_family: execution_guidance
    evidence_basis: execution_constraint_set.fields.rules
    confidence: high
    canonical_cognee_edge: true
    logistics_only: true
    canonical_edge_type: INCLUDES_RULE
    inverse_edge_type: INCLUDED_IN_CONSTRAINT_SET
    materialize_inverse: false
    edge_class: canonical
    source_type: execution_constraint_set
    target_type: rule
```

```yaml
candidate_edge:
  edge_id: edge.execution_constraint_set.logistics_general_analytics.includes_rule.rule.logistics.do_not_join_awb_to_bank_without_batch
  edge_type: INCLUDES_RULE
  source: execution_constraint_set.logistics_general_analytics
  target: rule.logistics.do_not_join_awb_to_bank_without_batch
  fields:
    edge_family: execution_guidance
    evidence_basis: execution_constraint_set.fields.rules
    confidence: high
    canonical_cognee_edge: true
    logistics_only: true
    canonical_edge_type: INCLUDES_RULE
    inverse_edge_type: INCLUDED_IN_CONSTRAINT_SET
    materialize_inverse: false
    edge_class: canonical
    source_type: execution_constraint_set
    target_type: rule
```

```yaml
candidate_edge:
  edge_id: edge.execution_constraint_set.logistics_general_analytics.includes_rule.rule.logistics.preaggregate_before_order_join
  edge_type: INCLUDES_RULE
  source: execution_constraint_set.logistics_general_analytics
  target: rule.logistics.preaggregate_before_order_join
  fields:
    edge_family: execution_guidance
    evidence_basis: execution_constraint_set.fields.rules
    confidence: high
    canonical_cognee_edge: true
    logistics_only: true
    canonical_edge_type: INCLUDES_RULE
    inverse_edge_type: INCLUDED_IN_CONSTRAINT_SET
    materialize_inverse: false
    edge_class: canonical
    source_type: execution_constraint_set
    target_type: rule
```

```yaml
candidate_edge:
  edge_id: edge.execution_constraint_set.logistics_general_analytics.includes_validation_test.validation_test.logistics.required_scope_context
  edge_type: INCLUDES_VALIDATION_TEST
  source: execution_constraint_set.logistics_general_analytics
  target: validation_test.logistics.required_scope_context
  fields:
    edge_family: execution_guidance
    evidence_basis: execution_constraint_set.fields.validation_tests
    confidence: high
    canonical_cognee_edge: true
    logistics_only: true
    canonical_edge_type: INCLUDES_VALIDATION_TEST
    inverse_edge_type: INCLUDED_IN_CONSTRAINT_SET
    materialize_inverse: false
    edge_class: canonical
    source_type: execution_constraint_set
    target_type: validation_test
```

```yaml
candidate_edge:
  edge_id: edge.execution_constraint_set.logistics_general_analytics.includes_validation_test.validation_test.logistics.business_flow_binding_required_for_cross_platform
  edge_type: INCLUDES_VALIDATION_TEST
  source: execution_constraint_set.logistics_general_analytics
  target: validation_test.logistics.business_flow_binding_required_for_cross_platform
  fields:
    edge_family: execution_guidance
    evidence_basis: execution_constraint_set.fields.validation_tests
    confidence: high
    canonical_cognee_edge: true
    logistics_only: true
    canonical_edge_type: INCLUDES_VALIDATION_TEST
    inverse_edge_type: INCLUDED_IN_CONSTRAINT_SET
    materialize_inverse: false
    edge_class: canonical
    source_type: execution_constraint_set
    target_type: validation_test
```

```yaml
candidate_edge:
  edge_id: edge.execution_constraint_set.logistics_general_analytics.includes_validation_test.validation_test.logistics.do_not_create_bfb_from_generic_vendor_doc
  edge_type: INCLUDES_VALIDATION_TEST
  source: execution_constraint_set.logistics_general_analytics
  target: validation_test.logistics.do_not_create_bfb_from_generic_vendor_doc
  fields:
    edge_family: execution_guidance
    evidence_basis: execution_constraint_set.fields.validation_tests
    confidence: high
    canonical_cognee_edge: true
    logistics_only: true
    canonical_edge_type: INCLUDES_VALIDATION_TEST
    inverse_edge_type: INCLUDED_IN_CONSTRAINT_SET
    materialize_inverse: false
    edge_class: canonical
    source_type: execution_constraint_set
    target_type: validation_test
```

```yaml
candidate_edge:
  edge_id: edge.execution_constraint_set.logistics_general_analytics.includes_validation_test.validation_test.logistics.amount_semantics_not_by_name
  edge_type: INCLUDES_VALIDATION_TEST
  source: execution_constraint_set.logistics_general_analytics
  target: validation_test.logistics.amount_semantics_not_by_name
  fields:
    edge_family: execution_guidance
    evidence_basis: execution_constraint_set.fields.validation_tests
    confidence: high
    canonical_cognee_edge: true
    logistics_only: true
    canonical_edge_type: INCLUDES_VALIDATION_TEST
    inverse_edge_type: INCLUDED_IN_CONSTRAINT_SET
    materialize_inverse: false
    edge_class: canonical
    source_type: execution_constraint_set
    target_type: validation_test
```

```yaml
candidate_edge:
  edge_id: edge.execution_constraint_set.logistics_general_analytics.includes_validation_test.validation_test.logistics.charged_amount_table_specific
  edge_type: INCLUDES_VALIDATION_TEST
  source: execution_constraint_set.logistics_general_analytics
  target: validation_test.logistics.charged_amount_table_specific
  fields:
    edge_family: execution_guidance
    evidence_basis: execution_constraint_set.fields.validation_tests
    confidence: high
    canonical_cognee_edge: true
    logistics_only: true
    canonical_edge_type: INCLUDES_VALIDATION_TEST
    inverse_edge_type: INCLUDED_IN_CONSTRAINT_SET
    materialize_inverse: false
    edge_class: canonical
    source_type: execution_constraint_set
    target_type: validation_test
```

```yaml
candidate_edge:
  edge_id: edge.execution_constraint_set.logistics_general_analytics.includes_validation_test.validation_test.logistics.active_filter_when_available
  edge_type: INCLUDES_VALIDATION_TEST
  source: execution_constraint_set.logistics_general_analytics
  target: validation_test.logistics.active_filter_when_available
  fields:
    edge_family: execution_guidance
    evidence_basis: execution_constraint_set.fields.validation_tests
    confidence: high
    canonical_cognee_edge: true
    logistics_only: true
    canonical_edge_type: INCLUDES_VALIDATION_TEST
    inverse_edge_type: INCLUDED_IN_CONSTRAINT_SET
    materialize_inverse: false
    edge_class: canonical
    source_type: execution_constraint_set
    target_type: validation_test
```

```yaml
candidate_edge:
  edge_id: edge.execution_constraint_set.logistics_general_analytics.includes_validation_test.validation_test.logistics.empty_tables_schema_only
  edge_type: INCLUDES_VALIDATION_TEST
  source: execution_constraint_set.logistics_general_analytics
  target: validation_test.logistics.empty_tables_schema_only
  fields:
    edge_family: execution_guidance
    evidence_basis: execution_constraint_set.fields.validation_tests
    confidence: high
    canonical_cognee_edge: true
    logistics_only: true
    canonical_edge_type: INCLUDES_VALIDATION_TEST
    inverse_edge_type: INCLUDED_IN_CONSTRAINT_SET
    materialize_inverse: false
    edge_class: canonical
    source_type: execution_constraint_set
    target_type: validation_test
```

```yaml
candidate_edge:
  edge_id: edge.execution_constraint_set.logistics_general_analytics.includes_validation_test.validation_test.logistics.low_confidence_requires_warning
  edge_type: INCLUDES_VALIDATION_TEST
  source: execution_constraint_set.logistics_general_analytics
  target: validation_test.logistics.low_confidence_requires_warning
  fields:
    edge_family: execution_guidance
    evidence_basis: execution_constraint_set.fields.validation_tests
    confidence: high
    canonical_cognee_edge: true
    logistics_only: true
    canonical_edge_type: INCLUDES_VALIDATION_TEST
    inverse_edge_type: INCLUDED_IN_CONSTRAINT_SET
    materialize_inverse: false
    edge_class: canonical
    source_type: execution_constraint_set
    target_type: validation_test
```

```yaml
candidate_edge:
  edge_id: edge.execution_constraint_set.logistics_general_analytics.includes_validation_test.validation_test.logistics.fallback_sources_explicit_only
  edge_type: INCLUDES_VALIDATION_TEST
  source: execution_constraint_set.logistics_general_analytics
  target: validation_test.logistics.fallback_sources_explicit_only
  fields:
    edge_family: execution_guidance
    evidence_basis: execution_constraint_set.fields.validation_tests
    confidence: high
    canonical_cognee_edge: true
    logistics_only: true
    canonical_edge_type: INCLUDES_VALIDATION_TEST
    inverse_edge_type: INCLUDED_IN_CONSTRAINT_SET
    materialize_inverse: false
    edge_class: canonical
    source_type: execution_constraint_set
    target_type: validation_test
```

```yaml
candidate_edge:
  edge_id: edge.execution_constraint_set.logistics_general_analytics.includes_validation_test.validation_test.logistics.awb_primary_reconciliation_unit
  edge_type: INCLUDES_VALIDATION_TEST
  source: execution_constraint_set.logistics_general_analytics
  target: validation_test.logistics.awb_primary_reconciliation_unit
  fields:
    edge_family: execution_guidance
    evidence_basis: execution_constraint_set.fields.validation_tests
    confidence: high
    canonical_cognee_edge: true
    logistics_only: true
    canonical_edge_type: INCLUDES_VALIDATION_TEST
    inverse_edge_type: INCLUDED_IN_CONSTRAINT_SET
    materialize_inverse: false
    edge_class: canonical
    source_type: execution_constraint_set
    target_type: validation_test
```

```yaml
candidate_edge:
  edge_id: edge.execution_constraint_set.logistics_general_analytics.includes_validation_test.validation_test.logistics.do_not_join_awb_to_bank_without_batch
  edge_type: INCLUDES_VALIDATION_TEST
  source: execution_constraint_set.logistics_general_analytics
  target: validation_test.logistics.do_not_join_awb_to_bank_without_batch
  fields:
    edge_family: execution_guidance
    evidence_basis: execution_constraint_set.fields.validation_tests
    confidence: high
    canonical_cognee_edge: true
    logistics_only: true
    canonical_edge_type: INCLUDES_VALIDATION_TEST
    inverse_edge_type: INCLUDED_IN_CONSTRAINT_SET
    materialize_inverse: false
    edge_class: canonical
    source_type: execution_constraint_set
    target_type: validation_test
```

```yaml
candidate_edge:
  edge_id: edge.execution_constraint_set.logistics_general_analytics.includes_validation_test.validation_test.logistics.preaggregate_before_order_join
  edge_type: INCLUDES_VALIDATION_TEST
  source: execution_constraint_set.logistics_general_analytics
  target: validation_test.logistics.preaggregate_before_order_join
  fields:
    edge_family: execution_guidance
    evidence_basis: execution_constraint_set.fields.validation_tests
    confidence: high
    canonical_cognee_edge: true
    logistics_only: true
    canonical_edge_type: INCLUDES_VALIDATION_TEST
    inverse_edge_type: INCLUDED_IN_CONSTRAINT_SET
    materialize_inverse: false
    edge_class: canonical
    source_type: execution_constraint_set
    target_type: validation_test
```

```yaml
candidate_edge:
  edge_id: edge.execution_constraint_set.logistics_general_analytics.applies_to_query_pattern.query_pattern.logistics.shipment_count_by_courier
  edge_type: APPLIES_TO_QUERY_PATTERN
  source: execution_constraint_set.logistics_general_analytics
  target: query_pattern.logistics.shipment_count_by_courier
  fields:
    edge_family: execution_guidance
    evidence_basis: execution_constraint_set.fields.query_patterns
    confidence: high
    canonical_cognee_edge: true
    logistics_only: true
    canonical_edge_type: APPLIES_TO_QUERY_PATTERN
    inverse_edge_type: HAS_EXECUTION_CONSTRAINT_SET
    materialize_inverse: false
    edge_class: canonical
    source_type: execution_constraint_set
    target_type: query_pattern
```

```yaml
candidate_edge:
  edge_id: edge.execution_constraint_set.logistics_general_analytics.applies_to_query_pattern.query_pattern.logistics.delivery_and_rto_rate
  edge_type: APPLIES_TO_QUERY_PATTERN
  source: execution_constraint_set.logistics_general_analytics
  target: query_pattern.logistics.delivery_and_rto_rate
  fields:
    edge_family: execution_guidance
    evidence_basis: execution_constraint_set.fields.query_patterns
    confidence: high
    canonical_cognee_edge: true
    logistics_only: true
    canonical_edge_type: APPLIES_TO_QUERY_PATTERN
    inverse_edge_type: HAS_EXECUTION_CONSTRAINT_SET
    materialize_inverse: false
    edge_class: canonical
    source_type: execution_constraint_set
    target_type: query_pattern
```

```yaml
candidate_edge:
  edge_id: edge.execution_constraint_set.logistics_general_analytics.applies_to_query_pattern.query_pattern.logistics.amount_semantics_audit
  edge_type: APPLIES_TO_QUERY_PATTERN
  source: execution_constraint_set.logistics_general_analytics
  target: query_pattern.logistics.amount_semantics_audit
  fields:
    edge_family: execution_guidance
    evidence_basis: execution_constraint_set.fields.query_patterns
    confidence: high
    canonical_cognee_edge: true
    logistics_only: true
    canonical_edge_type: APPLIES_TO_QUERY_PATTERN
    inverse_edge_type: HAS_EXECUTION_CONSTRAINT_SET
    materialize_inverse: false
    edge_class: canonical
    source_type: execution_constraint_set
    target_type: query_pattern
```

```yaml
candidate_edge:
  edge_id: edge.execution_constraint_set.logistics_general_analytics.applies_to_query_pattern.query_pattern.logistics.scope_binding_injection_check
  edge_type: APPLIES_TO_QUERY_PATTERN
  source: execution_constraint_set.logistics_general_analytics
  target: query_pattern.logistics.scope_binding_injection_check
  fields:
    edge_family: execution_guidance
    evidence_basis: execution_constraint_set.fields.query_patterns
    confidence: high
    canonical_cognee_edge: true
    logistics_only: true
    canonical_edge_type: APPLIES_TO_QUERY_PATTERN
    inverse_edge_type: HAS_EXECUTION_CONSTRAINT_SET
    materialize_inverse: false
    edge_class: canonical
    source_type: execution_constraint_set
    target_type: query_pattern
```

```yaml
candidate_edge:
  edge_id: edge.execution_constraint_set.logistics_reconciliation.includes_rule.rule.logistics.required_scope_context
  edge_type: INCLUDES_RULE
  source: execution_constraint_set.logistics_reconciliation
  target: rule.logistics.required_scope_context
  fields:
    edge_family: execution_guidance
    evidence_basis: execution_constraint_set.fields.rules
    confidence: high
    canonical_cognee_edge: true
    logistics_only: true
    canonical_edge_type: INCLUDES_RULE
    inverse_edge_type: INCLUDED_IN_CONSTRAINT_SET
    materialize_inverse: false
    edge_class: canonical
    source_type: execution_constraint_set
    target_type: rule
```

```yaml
candidate_edge:
  edge_id: edge.execution_constraint_set.logistics_reconciliation.includes_rule.rule.logistics.business_flow_binding_required_for_cross_platform
  edge_type: INCLUDES_RULE
  source: execution_constraint_set.logistics_reconciliation
  target: rule.logistics.business_flow_binding_required_for_cross_platform
  fields:
    edge_family: execution_guidance
    evidence_basis: execution_constraint_set.fields.rules
    confidence: high
    canonical_cognee_edge: true
    logistics_only: true
    canonical_edge_type: INCLUDES_RULE
    inverse_edge_type: INCLUDED_IN_CONSTRAINT_SET
    materialize_inverse: false
    edge_class: canonical
    source_type: execution_constraint_set
    target_type: rule
```

```yaml
candidate_edge:
  edge_id: edge.execution_constraint_set.logistics_reconciliation.includes_rule.rule.logistics.do_not_create_bfb_from_generic_vendor_doc
  edge_type: INCLUDES_RULE
  source: execution_constraint_set.logistics_reconciliation
  target: rule.logistics.do_not_create_bfb_from_generic_vendor_doc
  fields:
    edge_family: execution_guidance
    evidence_basis: execution_constraint_set.fields.rules
    confidence: high
    canonical_cognee_edge: true
    logistics_only: true
    canonical_edge_type: INCLUDES_RULE
    inverse_edge_type: INCLUDED_IN_CONSTRAINT_SET
    materialize_inverse: false
    edge_class: canonical
    source_type: execution_constraint_set
    target_type: rule
```

```yaml
candidate_edge:
  edge_id: edge.execution_constraint_set.logistics_reconciliation.includes_rule.rule.logistics.amount_semantics_not_by_name
  edge_type: INCLUDES_RULE
  source: execution_constraint_set.logistics_reconciliation
  target: rule.logistics.amount_semantics_not_by_name
  fields:
    edge_family: execution_guidance
    evidence_basis: execution_constraint_set.fields.rules
    confidence: high
    canonical_cognee_edge: true
    logistics_only: true
    canonical_edge_type: INCLUDES_RULE
    inverse_edge_type: INCLUDED_IN_CONSTRAINT_SET
    materialize_inverse: false
    edge_class: canonical
    source_type: execution_constraint_set
    target_type: rule
```

```yaml
candidate_edge:
  edge_id: edge.execution_constraint_set.logistics_reconciliation.includes_rule.rule.logistics.charged_amount_table_specific
  edge_type: INCLUDES_RULE
  source: execution_constraint_set.logistics_reconciliation
  target: rule.logistics.charged_amount_table_specific
  fields:
    edge_family: execution_guidance
    evidence_basis: execution_constraint_set.fields.rules
    confidence: high
    canonical_cognee_edge: true
    logistics_only: true
    canonical_edge_type: INCLUDES_RULE
    inverse_edge_type: INCLUDED_IN_CONSTRAINT_SET
    materialize_inverse: false
    edge_class: canonical
    source_type: execution_constraint_set
    target_type: rule
```

```yaml
candidate_edge:
  edge_id: edge.execution_constraint_set.logistics_reconciliation.includes_rule.rule.logistics.active_filter_when_available
  edge_type: INCLUDES_RULE
  source: execution_constraint_set.logistics_reconciliation
  target: rule.logistics.active_filter_when_available
  fields:
    edge_family: execution_guidance
    evidence_basis: execution_constraint_set.fields.rules
    confidence: high
    canonical_cognee_edge: true
    logistics_only: true
    canonical_edge_type: INCLUDES_RULE
    inverse_edge_type: INCLUDED_IN_CONSTRAINT_SET
    materialize_inverse: false
    edge_class: canonical
    source_type: execution_constraint_set
    target_type: rule
```

```yaml
candidate_edge:
  edge_id: edge.execution_constraint_set.logistics_reconciliation.includes_rule.rule.logistics.empty_tables_schema_only
  edge_type: INCLUDES_RULE
  source: execution_constraint_set.logistics_reconciliation
  target: rule.logistics.empty_tables_schema_only
  fields:
    edge_family: execution_guidance
    evidence_basis: execution_constraint_set.fields.rules
    confidence: high
    canonical_cognee_edge: true
    logistics_only: true
    canonical_edge_type: INCLUDES_RULE
    inverse_edge_type: INCLUDED_IN_CONSTRAINT_SET
    materialize_inverse: false
    edge_class: canonical
    source_type: execution_constraint_set
    target_type: rule
```

```yaml
candidate_edge:
  edge_id: edge.execution_constraint_set.logistics_reconciliation.includes_rule.rule.logistics.low_confidence_requires_warning
  edge_type: INCLUDES_RULE
  source: execution_constraint_set.logistics_reconciliation
  target: rule.logistics.low_confidence_requires_warning
  fields:
    edge_family: execution_guidance
    evidence_basis: execution_constraint_set.fields.rules
    confidence: high
    canonical_cognee_edge: true
    logistics_only: true
    canonical_edge_type: INCLUDES_RULE
    inverse_edge_type: INCLUDED_IN_CONSTRAINT_SET
    materialize_inverse: false
    edge_class: canonical
    source_type: execution_constraint_set
    target_type: rule
```

```yaml
candidate_edge:
  edge_id: edge.execution_constraint_set.logistics_reconciliation.includes_rule.rule.logistics.fallback_sources_explicit_only
  edge_type: INCLUDES_RULE
  source: execution_constraint_set.logistics_reconciliation
  target: rule.logistics.fallback_sources_explicit_only
  fields:
    edge_family: execution_guidance
    evidence_basis: execution_constraint_set.fields.rules
    confidence: high
    canonical_cognee_edge: true
    logistics_only: true
    canonical_edge_type: INCLUDES_RULE
    inverse_edge_type: INCLUDED_IN_CONSTRAINT_SET
    materialize_inverse: false
    edge_class: canonical
    source_type: execution_constraint_set
    target_type: rule
```

```yaml
candidate_edge:
  edge_id: edge.execution_constraint_set.logistics_reconciliation.includes_rule.rule.logistics.awb_primary_reconciliation_unit
  edge_type: INCLUDES_RULE
  source: execution_constraint_set.logistics_reconciliation
  target: rule.logistics.awb_primary_reconciliation_unit
  fields:
    edge_family: execution_guidance
    evidence_basis: execution_constraint_set.fields.rules
    confidence: high
    canonical_cognee_edge: true
    logistics_only: true
    canonical_edge_type: INCLUDES_RULE
    inverse_edge_type: INCLUDED_IN_CONSTRAINT_SET
    materialize_inverse: false
    edge_class: canonical
    source_type: execution_constraint_set
    target_type: rule
```

```yaml
candidate_edge:
  edge_id: edge.execution_constraint_set.logistics_reconciliation.includes_rule.rule.logistics.do_not_join_awb_to_bank_without_batch
  edge_type: INCLUDES_RULE
  source: execution_constraint_set.logistics_reconciliation
  target: rule.logistics.do_not_join_awb_to_bank_without_batch
  fields:
    edge_family: execution_guidance
    evidence_basis: execution_constraint_set.fields.rules
    confidence: high
    canonical_cognee_edge: true
    logistics_only: true
    canonical_edge_type: INCLUDES_RULE
    inverse_edge_type: INCLUDED_IN_CONSTRAINT_SET
    materialize_inverse: false
    edge_class: canonical
    source_type: execution_constraint_set
    target_type: rule
```

```yaml
candidate_edge:
  edge_id: edge.execution_constraint_set.logistics_reconciliation.includes_rule.rule.logistics.preaggregate_before_order_join
  edge_type: INCLUDES_RULE
  source: execution_constraint_set.logistics_reconciliation
  target: rule.logistics.preaggregate_before_order_join
  fields:
    edge_family: execution_guidance
    evidence_basis: execution_constraint_set.fields.rules
    confidence: high
    canonical_cognee_edge: true
    logistics_only: true
    canonical_edge_type: INCLUDES_RULE
    inverse_edge_type: INCLUDED_IN_CONSTRAINT_SET
    materialize_inverse: false
    edge_class: canonical
    source_type: execution_constraint_set
    target_type: rule
```

```yaml
candidate_edge:
  edge_id: edge.execution_constraint_set.logistics_reconciliation.includes_validation_test.validation_test.logistics.required_scope_context
  edge_type: INCLUDES_VALIDATION_TEST
  source: execution_constraint_set.logistics_reconciliation
  target: validation_test.logistics.required_scope_context
  fields:
    edge_family: execution_guidance
    evidence_basis: execution_constraint_set.fields.validation_tests
    confidence: high
    canonical_cognee_edge: true
    logistics_only: true
    canonical_edge_type: INCLUDES_VALIDATION_TEST
    inverse_edge_type: INCLUDED_IN_CONSTRAINT_SET
    materialize_inverse: false
    edge_class: canonical
    source_type: execution_constraint_set
    target_type: validation_test
```

```yaml
candidate_edge:
  edge_id: edge.execution_constraint_set.logistics_reconciliation.includes_validation_test.validation_test.logistics.business_flow_binding_required_for_cross_platform
  edge_type: INCLUDES_VALIDATION_TEST
  source: execution_constraint_set.logistics_reconciliation
  target: validation_test.logistics.business_flow_binding_required_for_cross_platform
  fields:
    edge_family: execution_guidance
    evidence_basis: execution_constraint_set.fields.validation_tests
    confidence: high
    canonical_cognee_edge: true
    logistics_only: true
    canonical_edge_type: INCLUDES_VALIDATION_TEST
    inverse_edge_type: INCLUDED_IN_CONSTRAINT_SET
    materialize_inverse: false
    edge_class: canonical
    source_type: execution_constraint_set
    target_type: validation_test
```

```yaml
candidate_edge:
  edge_id: edge.execution_constraint_set.logistics_reconciliation.includes_validation_test.validation_test.logistics.do_not_create_bfb_from_generic_vendor_doc
  edge_type: INCLUDES_VALIDATION_TEST
  source: execution_constraint_set.logistics_reconciliation
  target: validation_test.logistics.do_not_create_bfb_from_generic_vendor_doc
  fields:
    edge_family: execution_guidance
    evidence_basis: execution_constraint_set.fields.validation_tests
    confidence: high
    canonical_cognee_edge: true
    logistics_only: true
    canonical_edge_type: INCLUDES_VALIDATION_TEST
    inverse_edge_type: INCLUDED_IN_CONSTRAINT_SET
    materialize_inverse: false
    edge_class: canonical
    source_type: execution_constraint_set
    target_type: validation_test
```

```yaml
candidate_edge:
  edge_id: edge.execution_constraint_set.logistics_reconciliation.includes_validation_test.validation_test.logistics.amount_semantics_not_by_name
  edge_type: INCLUDES_VALIDATION_TEST
  source: execution_constraint_set.logistics_reconciliation
  target: validation_test.logistics.amount_semantics_not_by_name
  fields:
    edge_family: execution_guidance
    evidence_basis: execution_constraint_set.fields.validation_tests
    confidence: high
    canonical_cognee_edge: true
    logistics_only: true
    canonical_edge_type: INCLUDES_VALIDATION_TEST
    inverse_edge_type: INCLUDED_IN_CONSTRAINT_SET
    materialize_inverse: false
    edge_class: canonical
    source_type: execution_constraint_set
    target_type: validation_test
```

```yaml
candidate_edge:
  edge_id: edge.execution_constraint_set.logistics_reconciliation.includes_validation_test.validation_test.logistics.charged_amount_table_specific
  edge_type: INCLUDES_VALIDATION_TEST
  source: execution_constraint_set.logistics_reconciliation
  target: validation_test.logistics.charged_amount_table_specific
  fields:
    edge_family: execution_guidance
    evidence_basis: execution_constraint_set.fields.validation_tests
    confidence: high
    canonical_cognee_edge: true
    logistics_only: true
    canonical_edge_type: INCLUDES_VALIDATION_TEST
    inverse_edge_type: INCLUDED_IN_CONSTRAINT_SET
    materialize_inverse: false
    edge_class: canonical
    source_type: execution_constraint_set
    target_type: validation_test
```

```yaml
candidate_edge:
  edge_id: edge.execution_constraint_set.logistics_reconciliation.includes_validation_test.validation_test.logistics.active_filter_when_available
  edge_type: INCLUDES_VALIDATION_TEST
  source: execution_constraint_set.logistics_reconciliation
  target: validation_test.logistics.active_filter_when_available
  fields:
    edge_family: execution_guidance
    evidence_basis: execution_constraint_set.fields.validation_tests
    confidence: high
    canonical_cognee_edge: true
    logistics_only: true
    canonical_edge_type: INCLUDES_VALIDATION_TEST
    inverse_edge_type: INCLUDED_IN_CONSTRAINT_SET
    materialize_inverse: false
    edge_class: canonical
    source_type: execution_constraint_set
    target_type: validation_test
```

```yaml
candidate_edge:
  edge_id: edge.execution_constraint_set.logistics_reconciliation.includes_validation_test.validation_test.logistics.empty_tables_schema_only
  edge_type: INCLUDES_VALIDATION_TEST
  source: execution_constraint_set.logistics_reconciliation
  target: validation_test.logistics.empty_tables_schema_only
  fields:
    edge_family: execution_guidance
    evidence_basis: execution_constraint_set.fields.validation_tests
    confidence: high
    canonical_cognee_edge: true
    logistics_only: true
    canonical_edge_type: INCLUDES_VALIDATION_TEST
    inverse_edge_type: INCLUDED_IN_CONSTRAINT_SET
    materialize_inverse: false
    edge_class: canonical
    source_type: execution_constraint_set
    target_type: validation_test
```

```yaml
candidate_edge:
  edge_id: edge.execution_constraint_set.logistics_reconciliation.includes_validation_test.validation_test.logistics.low_confidence_requires_warning
  edge_type: INCLUDES_VALIDATION_TEST
  source: execution_constraint_set.logistics_reconciliation
  target: validation_test.logistics.low_confidence_requires_warning
  fields:
    edge_family: execution_guidance
    evidence_basis: execution_constraint_set.fields.validation_tests
    confidence: high
    canonical_cognee_edge: true
    logistics_only: true
    canonical_edge_type: INCLUDES_VALIDATION_TEST
    inverse_edge_type: INCLUDED_IN_CONSTRAINT_SET
    materialize_inverse: false
    edge_class: canonical
    source_type: execution_constraint_set
    target_type: validation_test
```

```yaml
candidate_edge:
  edge_id: edge.execution_constraint_set.logistics_reconciliation.includes_validation_test.validation_test.logistics.fallback_sources_explicit_only
  edge_type: INCLUDES_VALIDATION_TEST
  source: execution_constraint_set.logistics_reconciliation
  target: validation_test.logistics.fallback_sources_explicit_only
  fields:
    edge_family: execution_guidance
    evidence_basis: execution_constraint_set.fields.validation_tests
    confidence: high
    canonical_cognee_edge: true
    logistics_only: true
    canonical_edge_type: INCLUDES_VALIDATION_TEST
    inverse_edge_type: INCLUDED_IN_CONSTRAINT_SET
    materialize_inverse: false
    edge_class: canonical
    source_type: execution_constraint_set
    target_type: validation_test
```

```yaml
candidate_edge:
  edge_id: edge.execution_constraint_set.logistics_reconciliation.includes_validation_test.validation_test.logistics.awb_primary_reconciliation_unit
  edge_type: INCLUDES_VALIDATION_TEST
  source: execution_constraint_set.logistics_reconciliation
  target: validation_test.logistics.awb_primary_reconciliation_unit
  fields:
    edge_family: execution_guidance
    evidence_basis: execution_constraint_set.fields.validation_tests
    confidence: high
    canonical_cognee_edge: true
    logistics_only: true
    canonical_edge_type: INCLUDES_VALIDATION_TEST
    inverse_edge_type: INCLUDED_IN_CONSTRAINT_SET
    materialize_inverse: false
    edge_class: canonical
    source_type: execution_constraint_set
    target_type: validation_test
```

```yaml
candidate_edge:
  edge_id: edge.execution_constraint_set.logistics_reconciliation.includes_validation_test.validation_test.logistics.do_not_join_awb_to_bank_without_batch
  edge_type: INCLUDES_VALIDATION_TEST
  source: execution_constraint_set.logistics_reconciliation
  target: validation_test.logistics.do_not_join_awb_to_bank_without_batch
  fields:
    edge_family: execution_guidance
    evidence_basis: execution_constraint_set.fields.validation_tests
    confidence: high
    canonical_cognee_edge: true
    logistics_only: true
    canonical_edge_type: INCLUDES_VALIDATION_TEST
    inverse_edge_type: INCLUDED_IN_CONSTRAINT_SET
    materialize_inverse: false
    edge_class: canonical
    source_type: execution_constraint_set
    target_type: validation_test
```

```yaml
candidate_edge:
  edge_id: edge.execution_constraint_set.logistics_reconciliation.includes_validation_test.validation_test.logistics.preaggregate_before_order_join
  edge_type: INCLUDES_VALIDATION_TEST
  source: execution_constraint_set.logistics_reconciliation
  target: validation_test.logistics.preaggregate_before_order_join
  fields:
    edge_family: execution_guidance
    evidence_basis: execution_constraint_set.fields.validation_tests
    confidence: high
    canonical_cognee_edge: true
    logistics_only: true
    canonical_edge_type: INCLUDES_VALIDATION_TEST
    inverse_edge_type: INCLUDED_IN_CONSTRAINT_SET
    materialize_inverse: false
    edge_class: canonical
    source_type: execution_constraint_set
    target_type: validation_test
```

```yaml
candidate_edge:
  edge_id: edge.execution_constraint_set.logistics_reconciliation.applies_to_query_pattern.query_pattern.logistics.shipments_without_invoice
  edge_type: APPLIES_TO_QUERY_PATTERN
  source: execution_constraint_set.logistics_reconciliation
  target: query_pattern.logistics.shipments_without_invoice
  fields:
    edge_family: execution_guidance
    evidence_basis: execution_constraint_set.fields.query_patterns
    confidence: high
    canonical_cognee_edge: true
    logistics_only: true
    canonical_edge_type: APPLIES_TO_QUERY_PATTERN
    inverse_edge_type: HAS_EXECUTION_CONSTRAINT_SET
    materialize_inverse: false
    edge_class: canonical
    source_type: execution_constraint_set
    target_type: query_pattern
```

```yaml
candidate_edge:
  edge_id: edge.execution_constraint_set.logistics_reconciliation.applies_to_query_pattern.query_pattern.logistics.shipments_without_cod_remittance
  edge_type: APPLIES_TO_QUERY_PATTERN
  source: execution_constraint_set.logistics_reconciliation
  target: query_pattern.logistics.shipments_without_cod_remittance
  fields:
    edge_family: execution_guidance
    evidence_basis: execution_constraint_set.fields.query_patterns
    confidence: high
    canonical_cognee_edge: true
    logistics_only: true
    canonical_edge_type: APPLIES_TO_QUERY_PATTERN
    inverse_edge_type: HAS_EXECUTION_CONSTRAINT_SET
    materialize_inverse: false
    edge_class: canonical
    source_type: execution_constraint_set
    target_type: query_pattern
```

```yaml
candidate_edge:
  edge_id: edge.execution_constraint_set.logistics_reconciliation.applies_to_query_pattern.query_pattern.logistics.freight_overcharge_check
  edge_type: APPLIES_TO_QUERY_PATTERN
  source: execution_constraint_set.logistics_reconciliation
  target: query_pattern.logistics.freight_overcharge_check
  fields:
    edge_family: execution_guidance
    evidence_basis: execution_constraint_set.fields.query_patterns
    confidence: high
    canonical_cognee_edge: true
    logistics_only: true
    canonical_edge_type: APPLIES_TO_QUERY_PATTERN
    inverse_edge_type: HAS_EXECUTION_CONSTRAINT_SET
    materialize_inverse: false
    edge_class: canonical
    source_type: execution_constraint_set
    target_type: query_pattern
```

```yaml
candidate_edge:
  edge_id: edge.execution_constraint_set.logistics_reconciliation.applies_to_query_pattern.query_pattern.logistics.cod_expected_vs_remitted
  edge_type: APPLIES_TO_QUERY_PATTERN
  source: execution_constraint_set.logistics_reconciliation
  target: query_pattern.logistics.cod_expected_vs_remitted
  fields:
    edge_family: execution_guidance
    evidence_basis: execution_constraint_set.fields.query_patterns
    confidence: high
    canonical_cognee_edge: true
    logistics_only: true
    canonical_edge_type: APPLIES_TO_QUERY_PATTERN
    inverse_edge_type: HAS_EXECUTION_CONSTRAINT_SET
    materialize_inverse: false
    edge_class: canonical
    source_type: execution_constraint_set
    target_type: query_pattern
```

```yaml
candidate_edge:
  edge_id: edge.execution_constraint_set.logistics_cod_reconciliation.includes_rule.rule.logistics.required_scope_context
  edge_type: INCLUDES_RULE
  source: execution_constraint_set.logistics_cod_reconciliation
  target: rule.logistics.required_scope_context
  fields:
    edge_family: execution_guidance
    evidence_basis: execution_constraint_set.fields.rules
    confidence: high
    canonical_cognee_edge: true
    logistics_only: true
    canonical_edge_type: INCLUDES_RULE
    inverse_edge_type: INCLUDED_IN_CONSTRAINT_SET
    materialize_inverse: false
    edge_class: canonical
    source_type: execution_constraint_set
    target_type: rule
```

```yaml
candidate_edge:
  edge_id: edge.execution_constraint_set.logistics_cod_reconciliation.includes_rule.rule.logistics.business_flow_binding_required_for_cross_platform
  edge_type: INCLUDES_RULE
  source: execution_constraint_set.logistics_cod_reconciliation
  target: rule.logistics.business_flow_binding_required_for_cross_platform
  fields:
    edge_family: execution_guidance
    evidence_basis: execution_constraint_set.fields.rules
    confidence: high
    canonical_cognee_edge: true
    logistics_only: true
    canonical_edge_type: INCLUDES_RULE
    inverse_edge_type: INCLUDED_IN_CONSTRAINT_SET
    materialize_inverse: false
    edge_class: canonical
    source_type: execution_constraint_set
    target_type: rule
```

```yaml
candidate_edge:
  edge_id: edge.execution_constraint_set.logistics_cod_reconciliation.includes_rule.rule.logistics.do_not_create_bfb_from_generic_vendor_doc
  edge_type: INCLUDES_RULE
  source: execution_constraint_set.logistics_cod_reconciliation
  target: rule.logistics.do_not_create_bfb_from_generic_vendor_doc
  fields:
    edge_family: execution_guidance
    evidence_basis: execution_constraint_set.fields.rules
    confidence: high
    canonical_cognee_edge: true
    logistics_only: true
    canonical_edge_type: INCLUDES_RULE
    inverse_edge_type: INCLUDED_IN_CONSTRAINT_SET
    materialize_inverse: false
    edge_class: canonical
    source_type: execution_constraint_set
    target_type: rule
```

```yaml
candidate_edge:
  edge_id: edge.execution_constraint_set.logistics_cod_reconciliation.includes_rule.rule.logistics.amount_semantics_not_by_name
  edge_type: INCLUDES_RULE
  source: execution_constraint_set.logistics_cod_reconciliation
  target: rule.logistics.amount_semantics_not_by_name
  fields:
    edge_family: execution_guidance
    evidence_basis: execution_constraint_set.fields.rules
    confidence: high
    canonical_cognee_edge: true
    logistics_only: true
    canonical_edge_type: INCLUDES_RULE
    inverse_edge_type: INCLUDED_IN_CONSTRAINT_SET
    materialize_inverse: false
    edge_class: canonical
    source_type: execution_constraint_set
    target_type: rule
```

```yaml
candidate_edge:
  edge_id: edge.execution_constraint_set.logistics_cod_reconciliation.includes_rule.rule.logistics.charged_amount_table_specific
  edge_type: INCLUDES_RULE
  source: execution_constraint_set.logistics_cod_reconciliation
  target: rule.logistics.charged_amount_table_specific
  fields:
    edge_family: execution_guidance
    evidence_basis: execution_constraint_set.fields.rules
    confidence: high
    canonical_cognee_edge: true
    logistics_only: true
    canonical_edge_type: INCLUDES_RULE
    inverse_edge_type: INCLUDED_IN_CONSTRAINT_SET
    materialize_inverse: false
    edge_class: canonical
    source_type: execution_constraint_set
    target_type: rule
```

```yaml
candidate_edge:
  edge_id: edge.execution_constraint_set.logistics_cod_reconciliation.includes_rule.rule.logistics.active_filter_when_available
  edge_type: INCLUDES_RULE
  source: execution_constraint_set.logistics_cod_reconciliation
  target: rule.logistics.active_filter_when_available
  fields:
    edge_family: execution_guidance
    evidence_basis: execution_constraint_set.fields.rules
    confidence: high
    canonical_cognee_edge: true
    logistics_only: true
    canonical_edge_type: INCLUDES_RULE
    inverse_edge_type: INCLUDED_IN_CONSTRAINT_SET
    materialize_inverse: false
    edge_class: canonical
    source_type: execution_constraint_set
    target_type: rule
```

```yaml
candidate_edge:
  edge_id: edge.execution_constraint_set.logistics_cod_reconciliation.includes_rule.rule.logistics.empty_tables_schema_only
  edge_type: INCLUDES_RULE
  source: execution_constraint_set.logistics_cod_reconciliation
  target: rule.logistics.empty_tables_schema_only
  fields:
    edge_family: execution_guidance
    evidence_basis: execution_constraint_set.fields.rules
    confidence: high
    canonical_cognee_edge: true
    logistics_only: true
    canonical_edge_type: INCLUDES_RULE
    inverse_edge_type: INCLUDED_IN_CONSTRAINT_SET
    materialize_inverse: false
    edge_class: canonical
    source_type: execution_constraint_set
    target_type: rule
```

```yaml
candidate_edge:
  edge_id: edge.execution_constraint_set.logistics_cod_reconciliation.includes_rule.rule.logistics.low_confidence_requires_warning
  edge_type: INCLUDES_RULE
  source: execution_constraint_set.logistics_cod_reconciliation
  target: rule.logistics.low_confidence_requires_warning
  fields:
    edge_family: execution_guidance
    evidence_basis: execution_constraint_set.fields.rules
    confidence: high
    canonical_cognee_edge: true
    logistics_only: true
    canonical_edge_type: INCLUDES_RULE
    inverse_edge_type: INCLUDED_IN_CONSTRAINT_SET
    materialize_inverse: false
    edge_class: canonical
    source_type: execution_constraint_set
    target_type: rule
```

```yaml
candidate_edge:
  edge_id: edge.execution_constraint_set.logistics_cod_reconciliation.includes_rule.rule.logistics.fallback_sources_explicit_only
  edge_type: INCLUDES_RULE
  source: execution_constraint_set.logistics_cod_reconciliation
  target: rule.logistics.fallback_sources_explicit_only
  fields:
    edge_family: execution_guidance
    evidence_basis: execution_constraint_set.fields.rules
    confidence: high
    canonical_cognee_edge: true
    logistics_only: true
    canonical_edge_type: INCLUDES_RULE
    inverse_edge_type: INCLUDED_IN_CONSTRAINT_SET
    materialize_inverse: false
    edge_class: canonical
    source_type: execution_constraint_set
    target_type: rule
```

```yaml
candidate_edge:
  edge_id: edge.execution_constraint_set.logistics_cod_reconciliation.includes_rule.rule.logistics.awb_primary_reconciliation_unit
  edge_type: INCLUDES_RULE
  source: execution_constraint_set.logistics_cod_reconciliation
  target: rule.logistics.awb_primary_reconciliation_unit
  fields:
    edge_family: execution_guidance
    evidence_basis: execution_constraint_set.fields.rules
    confidence: high
    canonical_cognee_edge: true
    logistics_only: true
    canonical_edge_type: INCLUDES_RULE
    inverse_edge_type: INCLUDED_IN_CONSTRAINT_SET
    materialize_inverse: false
    edge_class: canonical
    source_type: execution_constraint_set
    target_type: rule
```

```yaml
candidate_edge:
  edge_id: edge.execution_constraint_set.logistics_cod_reconciliation.includes_rule.rule.logistics.do_not_join_awb_to_bank_without_batch
  edge_type: INCLUDES_RULE
  source: execution_constraint_set.logistics_cod_reconciliation
  target: rule.logistics.do_not_join_awb_to_bank_without_batch
  fields:
    edge_family: execution_guidance
    evidence_basis: execution_constraint_set.fields.rules
    confidence: high
    canonical_cognee_edge: true
    logistics_only: true
    canonical_edge_type: INCLUDES_RULE
    inverse_edge_type: INCLUDED_IN_CONSTRAINT_SET
    materialize_inverse: false
    edge_class: canonical
    source_type: execution_constraint_set
    target_type: rule
```

```yaml
candidate_edge:
  edge_id: edge.execution_constraint_set.logistics_cod_reconciliation.includes_rule.rule.logistics.preaggregate_before_order_join
  edge_type: INCLUDES_RULE
  source: execution_constraint_set.logistics_cod_reconciliation
  target: rule.logistics.preaggregate_before_order_join
  fields:
    edge_family: execution_guidance
    evidence_basis: execution_constraint_set.fields.rules
    confidence: high
    canonical_cognee_edge: true
    logistics_only: true
    canonical_edge_type: INCLUDES_RULE
    inverse_edge_type: INCLUDED_IN_CONSTRAINT_SET
    materialize_inverse: false
    edge_class: canonical
    source_type: execution_constraint_set
    target_type: rule
```

```yaml
candidate_edge:
  edge_id: edge.execution_constraint_set.logistics_cod_reconciliation.includes_validation_test.validation_test.logistics.required_scope_context
  edge_type: INCLUDES_VALIDATION_TEST
  source: execution_constraint_set.logistics_cod_reconciliation
  target: validation_test.logistics.required_scope_context
  fields:
    edge_family: execution_guidance
    evidence_basis: execution_constraint_set.fields.validation_tests
    confidence: high
    canonical_cognee_edge: true
    logistics_only: true
    canonical_edge_type: INCLUDES_VALIDATION_TEST
    inverse_edge_type: INCLUDED_IN_CONSTRAINT_SET
    materialize_inverse: false
    edge_class: canonical
    source_type: execution_constraint_set
    target_type: validation_test
```

```yaml
candidate_edge:
  edge_id: edge.execution_constraint_set.logistics_cod_reconciliation.includes_validation_test.validation_test.logistics.business_flow_binding_required_for_cross_platform
  edge_type: INCLUDES_VALIDATION_TEST
  source: execution_constraint_set.logistics_cod_reconciliation
  target: validation_test.logistics.business_flow_binding_required_for_cross_platform
  fields:
    edge_family: execution_guidance
    evidence_basis: execution_constraint_set.fields.validation_tests
    confidence: high
    canonical_cognee_edge: true
    logistics_only: true
    canonical_edge_type: INCLUDES_VALIDATION_TEST
    inverse_edge_type: INCLUDED_IN_CONSTRAINT_SET
    materialize_inverse: false
    edge_class: canonical
    source_type: execution_constraint_set
    target_type: validation_test
```

```yaml
candidate_edge:
  edge_id: edge.execution_constraint_set.logistics_cod_reconciliation.includes_validation_test.validation_test.logistics.do_not_create_bfb_from_generic_vendor_doc
  edge_type: INCLUDES_VALIDATION_TEST
  source: execution_constraint_set.logistics_cod_reconciliation
  target: validation_test.logistics.do_not_create_bfb_from_generic_vendor_doc
  fields:
    edge_family: execution_guidance
    evidence_basis: execution_constraint_set.fields.validation_tests
    confidence: high
    canonical_cognee_edge: true
    logistics_only: true
    canonical_edge_type: INCLUDES_VALIDATION_TEST
    inverse_edge_type: INCLUDED_IN_CONSTRAINT_SET
    materialize_inverse: false
    edge_class: canonical
    source_type: execution_constraint_set
    target_type: validation_test
```

```yaml
candidate_edge:
  edge_id: edge.execution_constraint_set.logistics_cod_reconciliation.includes_validation_test.validation_test.logistics.amount_semantics_not_by_name
  edge_type: INCLUDES_VALIDATION_TEST
  source: execution_constraint_set.logistics_cod_reconciliation
  target: validation_test.logistics.amount_semantics_not_by_name
  fields:
    edge_family: execution_guidance
    evidence_basis: execution_constraint_set.fields.validation_tests
    confidence: high
    canonical_cognee_edge: true
    logistics_only: true
    canonical_edge_type: INCLUDES_VALIDATION_TEST
    inverse_edge_type: INCLUDED_IN_CONSTRAINT_SET
    materialize_inverse: false
    edge_class: canonical
    source_type: execution_constraint_set
    target_type: validation_test
```

```yaml
candidate_edge:
  edge_id: edge.execution_constraint_set.logistics_cod_reconciliation.includes_validation_test.validation_test.logistics.charged_amount_table_specific
  edge_type: INCLUDES_VALIDATION_TEST
  source: execution_constraint_set.logistics_cod_reconciliation
  target: validation_test.logistics.charged_amount_table_specific
  fields:
    edge_family: execution_guidance
    evidence_basis: execution_constraint_set.fields.validation_tests
    confidence: high
    canonical_cognee_edge: true
    logistics_only: true
    canonical_edge_type: INCLUDES_VALIDATION_TEST
    inverse_edge_type: INCLUDED_IN_CONSTRAINT_SET
    materialize_inverse: false
    edge_class: canonical
    source_type: execution_constraint_set
    target_type: validation_test
```

```yaml
candidate_edge:
  edge_id: edge.execution_constraint_set.logistics_cod_reconciliation.includes_validation_test.validation_test.logistics.active_filter_when_available
  edge_type: INCLUDES_VALIDATION_TEST
  source: execution_constraint_set.logistics_cod_reconciliation
  target: validation_test.logistics.active_filter_when_available
  fields:
    edge_family: execution_guidance
    evidence_basis: execution_constraint_set.fields.validation_tests
    confidence: high
    canonical_cognee_edge: true
    logistics_only: true
    canonical_edge_type: INCLUDES_VALIDATION_TEST
    inverse_edge_type: INCLUDED_IN_CONSTRAINT_SET
    materialize_inverse: false
    edge_class: canonical
    source_type: execution_constraint_set
    target_type: validation_test
```

```yaml
candidate_edge:
  edge_id: edge.execution_constraint_set.logistics_cod_reconciliation.includes_validation_test.validation_test.logistics.empty_tables_schema_only
  edge_type: INCLUDES_VALIDATION_TEST
  source: execution_constraint_set.logistics_cod_reconciliation
  target: validation_test.logistics.empty_tables_schema_only
  fields:
    edge_family: execution_guidance
    evidence_basis: execution_constraint_set.fields.validation_tests
    confidence: high
    canonical_cognee_edge: true
    logistics_only: true
    canonical_edge_type: INCLUDES_VALIDATION_TEST
    inverse_edge_type: INCLUDED_IN_CONSTRAINT_SET
    materialize_inverse: false
    edge_class: canonical
    source_type: execution_constraint_set
    target_type: validation_test
```

```yaml
candidate_edge:
  edge_id: edge.execution_constraint_set.logistics_cod_reconciliation.includes_validation_test.validation_test.logistics.low_confidence_requires_warning
  edge_type: INCLUDES_VALIDATION_TEST
  source: execution_constraint_set.logistics_cod_reconciliation
  target: validation_test.logistics.low_confidence_requires_warning
  fields:
    edge_family: execution_guidance
    evidence_basis: execution_constraint_set.fields.validation_tests
    confidence: high
    canonical_cognee_edge: true
    logistics_only: true
    canonical_edge_type: INCLUDES_VALIDATION_TEST
    inverse_edge_type: INCLUDED_IN_CONSTRAINT_SET
    materialize_inverse: false
    edge_class: canonical
    source_type: execution_constraint_set
    target_type: validation_test
```

```yaml
candidate_edge:
  edge_id: edge.execution_constraint_set.logistics_cod_reconciliation.includes_validation_test.validation_test.logistics.fallback_sources_explicit_only
  edge_type: INCLUDES_VALIDATION_TEST
  source: execution_constraint_set.logistics_cod_reconciliation
  target: validation_test.logistics.fallback_sources_explicit_only
  fields:
    edge_family: execution_guidance
    evidence_basis: execution_constraint_set.fields.validation_tests
    confidence: high
    canonical_cognee_edge: true
    logistics_only: true
    canonical_edge_type: INCLUDES_VALIDATION_TEST
    inverse_edge_type: INCLUDED_IN_CONSTRAINT_SET
    materialize_inverse: false
    edge_class: canonical
    source_type: execution_constraint_set
    target_type: validation_test
```

```yaml
candidate_edge:
  edge_id: edge.execution_constraint_set.logistics_cod_reconciliation.includes_validation_test.validation_test.logistics.awb_primary_reconciliation_unit
  edge_type: INCLUDES_VALIDATION_TEST
  source: execution_constraint_set.logistics_cod_reconciliation
  target: validation_test.logistics.awb_primary_reconciliation_unit
  fields:
    edge_family: execution_guidance
    evidence_basis: execution_constraint_set.fields.validation_tests
    confidence: high
    canonical_cognee_edge: true
    logistics_only: true
    canonical_edge_type: INCLUDES_VALIDATION_TEST
    inverse_edge_type: INCLUDED_IN_CONSTRAINT_SET
    materialize_inverse: false
    edge_class: canonical
    source_type: execution_constraint_set
    target_type: validation_test
```

```yaml
candidate_edge:
  edge_id: edge.execution_constraint_set.logistics_cod_reconciliation.includes_validation_test.validation_test.logistics.do_not_join_awb_to_bank_without_batch
  edge_type: INCLUDES_VALIDATION_TEST
  source: execution_constraint_set.logistics_cod_reconciliation
  target: validation_test.logistics.do_not_join_awb_to_bank_without_batch
  fields:
    edge_family: execution_guidance
    evidence_basis: execution_constraint_set.fields.validation_tests
    confidence: high
    canonical_cognee_edge: true
    logistics_only: true
    canonical_edge_type: INCLUDES_VALIDATION_TEST
    inverse_edge_type: INCLUDED_IN_CONSTRAINT_SET
    materialize_inverse: false
    edge_class: canonical
    source_type: execution_constraint_set
    target_type: validation_test
```

```yaml
candidate_edge:
  edge_id: edge.execution_constraint_set.logistics_cod_reconciliation.includes_validation_test.validation_test.logistics.preaggregate_before_order_join
  edge_type: INCLUDES_VALIDATION_TEST
  source: execution_constraint_set.logistics_cod_reconciliation
  target: validation_test.logistics.preaggregate_before_order_join
  fields:
    edge_family: execution_guidance
    evidence_basis: execution_constraint_set.fields.validation_tests
    confidence: high
    canonical_cognee_edge: true
    logistics_only: true
    canonical_edge_type: INCLUDES_VALIDATION_TEST
    inverse_edge_type: INCLUDED_IN_CONSTRAINT_SET
    materialize_inverse: false
    edge_class: canonical
    source_type: execution_constraint_set
    target_type: validation_test
```

```yaml
candidate_edge:
  edge_id: edge.execution_constraint_set.logistics_cod_reconciliation.applies_to_query_pattern.query_pattern.logistics.cod_expected_vs_remitted
  edge_type: APPLIES_TO_QUERY_PATTERN
  source: execution_constraint_set.logistics_cod_reconciliation
  target: query_pattern.logistics.cod_expected_vs_remitted
  fields:
    edge_family: execution_guidance
    evidence_basis: execution_constraint_set.fields.query_patterns
    confidence: high
    canonical_cognee_edge: true
    logistics_only: true
    canonical_edge_type: APPLIES_TO_QUERY_PATTERN
    inverse_edge_type: HAS_EXECUTION_CONSTRAINT_SET
    materialize_inverse: false
    edge_class: canonical
    source_type: execution_constraint_set
    target_type: query_pattern
```

```yaml
candidate_edge:
  edge_id: edge.execution_constraint_set.logistics_cod_reconciliation.applies_to_query_pattern.query_pattern.logistics.cod_remittance_lag
  edge_type: APPLIES_TO_QUERY_PATTERN
  source: execution_constraint_set.logistics_cod_reconciliation
  target: query_pattern.logistics.cod_remittance_lag
  fields:
    edge_family: execution_guidance
    evidence_basis: execution_constraint_set.fields.query_patterns
    confidence: high
    canonical_cognee_edge: true
    logistics_only: true
    canonical_edge_type: APPLIES_TO_QUERY_PATTERN
    inverse_edge_type: HAS_EXECUTION_CONSTRAINT_SET
    materialize_inverse: false
    edge_class: canonical
    source_type: execution_constraint_set
    target_type: query_pattern
```

```yaml
candidate_edge:
  edge_id: edge.execution_constraint_set.logistics_cod_reconciliation.applies_to_query_pattern.query_pattern.logistics.shipments_without_cod_remittance
  edge_type: APPLIES_TO_QUERY_PATTERN
  source: execution_constraint_set.logistics_cod_reconciliation
  target: query_pattern.logistics.shipments_without_cod_remittance
  fields:
    edge_family: execution_guidance
    evidence_basis: execution_constraint_set.fields.query_patterns
    confidence: high
    canonical_cognee_edge: true
    logistics_only: true
    canonical_edge_type: APPLIES_TO_QUERY_PATTERN
    inverse_edge_type: HAS_EXECUTION_CONSTRAINT_SET
    materialize_inverse: false
    edge_class: canonical
    source_type: execution_constraint_set
    target_type: query_pattern
```

```yaml
candidate_edge:
  edge_id: edge.execution_constraint_set.logistics_freight_reconciliation.includes_rule.rule.logistics.required_scope_context
  edge_type: INCLUDES_RULE
  source: execution_constraint_set.logistics_freight_reconciliation
  target: rule.logistics.required_scope_context
  fields:
    edge_family: execution_guidance
    evidence_basis: execution_constraint_set.fields.rules
    confidence: high
    canonical_cognee_edge: true
    logistics_only: true
    canonical_edge_type: INCLUDES_RULE
    inverse_edge_type: INCLUDED_IN_CONSTRAINT_SET
    materialize_inverse: false
    edge_class: canonical
    source_type: execution_constraint_set
    target_type: rule
```

```yaml
candidate_edge:
  edge_id: edge.execution_constraint_set.logistics_freight_reconciliation.includes_rule.rule.logistics.business_flow_binding_required_for_cross_platform
  edge_type: INCLUDES_RULE
  source: execution_constraint_set.logistics_freight_reconciliation
  target: rule.logistics.business_flow_binding_required_for_cross_platform
  fields:
    edge_family: execution_guidance
    evidence_basis: execution_constraint_set.fields.rules
    confidence: high
    canonical_cognee_edge: true
    logistics_only: true
    canonical_edge_type: INCLUDES_RULE
    inverse_edge_type: INCLUDED_IN_CONSTRAINT_SET
    materialize_inverse: false
    edge_class: canonical
    source_type: execution_constraint_set
    target_type: rule
```

```yaml
candidate_edge:
  edge_id: edge.execution_constraint_set.logistics_freight_reconciliation.includes_rule.rule.logistics.do_not_create_bfb_from_generic_vendor_doc
  edge_type: INCLUDES_RULE
  source: execution_constraint_set.logistics_freight_reconciliation
  target: rule.logistics.do_not_create_bfb_from_generic_vendor_doc
  fields:
    edge_family: execution_guidance
    evidence_basis: execution_constraint_set.fields.rules
    confidence: high
    canonical_cognee_edge: true
    logistics_only: true
    canonical_edge_type: INCLUDES_RULE
    inverse_edge_type: INCLUDED_IN_CONSTRAINT_SET
    materialize_inverse: false
    edge_class: canonical
    source_type: execution_constraint_set
    target_type: rule
```

```yaml
candidate_edge:
  edge_id: edge.execution_constraint_set.logistics_freight_reconciliation.includes_rule.rule.logistics.amount_semantics_not_by_name
  edge_type: INCLUDES_RULE
  source: execution_constraint_set.logistics_freight_reconciliation
  target: rule.logistics.amount_semantics_not_by_name
  fields:
    edge_family: execution_guidance
    evidence_basis: execution_constraint_set.fields.rules
    confidence: high
    canonical_cognee_edge: true
    logistics_only: true
    canonical_edge_type: INCLUDES_RULE
    inverse_edge_type: INCLUDED_IN_CONSTRAINT_SET
    materialize_inverse: false
    edge_class: canonical
    source_type: execution_constraint_set
    target_type: rule
```

```yaml
candidate_edge:
  edge_id: edge.execution_constraint_set.logistics_freight_reconciliation.includes_rule.rule.logistics.charged_amount_table_specific
  edge_type: INCLUDES_RULE
  source: execution_constraint_set.logistics_freight_reconciliation
  target: rule.logistics.charged_amount_table_specific
  fields:
    edge_family: execution_guidance
    evidence_basis: execution_constraint_set.fields.rules
    confidence: high
    canonical_cognee_edge: true
    logistics_only: true
    canonical_edge_type: INCLUDES_RULE
    inverse_edge_type: INCLUDED_IN_CONSTRAINT_SET
    materialize_inverse: false
    edge_class: canonical
    source_type: execution_constraint_set
    target_type: rule
```

```yaml
candidate_edge:
  edge_id: edge.execution_constraint_set.logistics_freight_reconciliation.includes_rule.rule.logistics.active_filter_when_available
  edge_type: INCLUDES_RULE
  source: execution_constraint_set.logistics_freight_reconciliation
  target: rule.logistics.active_filter_when_available
  fields:
    edge_family: execution_guidance
    evidence_basis: execution_constraint_set.fields.rules
    confidence: high
    canonical_cognee_edge: true
    logistics_only: true
    canonical_edge_type: INCLUDES_RULE
    inverse_edge_type: INCLUDED_IN_CONSTRAINT_SET
    materialize_inverse: false
    edge_class: canonical
    source_type: execution_constraint_set
    target_type: rule
```

```yaml
candidate_edge:
  edge_id: edge.execution_constraint_set.logistics_freight_reconciliation.includes_rule.rule.logistics.empty_tables_schema_only
  edge_type: INCLUDES_RULE
  source: execution_constraint_set.logistics_freight_reconciliation
  target: rule.logistics.empty_tables_schema_only
  fields:
    edge_family: execution_guidance
    evidence_basis: execution_constraint_set.fields.rules
    confidence: high
    canonical_cognee_edge: true
    logistics_only: true
    canonical_edge_type: INCLUDES_RULE
    inverse_edge_type: INCLUDED_IN_CONSTRAINT_SET
    materialize_inverse: false
    edge_class: canonical
    source_type: execution_constraint_set
    target_type: rule
```

```yaml
candidate_edge:
  edge_id: edge.execution_constraint_set.logistics_freight_reconciliation.includes_rule.rule.logistics.low_confidence_requires_warning
  edge_type: INCLUDES_RULE
  source: execution_constraint_set.logistics_freight_reconciliation
  target: rule.logistics.low_confidence_requires_warning
  fields:
    edge_family: execution_guidance
    evidence_basis: execution_constraint_set.fields.rules
    confidence: high
    canonical_cognee_edge: true
    logistics_only: true
    canonical_edge_type: INCLUDES_RULE
    inverse_edge_type: INCLUDED_IN_CONSTRAINT_SET
    materialize_inverse: false
    edge_class: canonical
    source_type: execution_constraint_set
    target_type: rule
```

```yaml
candidate_edge:
  edge_id: edge.execution_constraint_set.logistics_freight_reconciliation.includes_rule.rule.logistics.fallback_sources_explicit_only
  edge_type: INCLUDES_RULE
  source: execution_constraint_set.logistics_freight_reconciliation
  target: rule.logistics.fallback_sources_explicit_only
  fields:
    edge_family: execution_guidance
    evidence_basis: execution_constraint_set.fields.rules
    confidence: high
    canonical_cognee_edge: true
    logistics_only: true
    canonical_edge_type: INCLUDES_RULE
    inverse_edge_type: INCLUDED_IN_CONSTRAINT_SET
    materialize_inverse: false
    edge_class: canonical
    source_type: execution_constraint_set
    target_type: rule
```

```yaml
candidate_edge:
  edge_id: edge.execution_constraint_set.logistics_freight_reconciliation.includes_rule.rule.logistics.awb_primary_reconciliation_unit
  edge_type: INCLUDES_RULE
  source: execution_constraint_set.logistics_freight_reconciliation
  target: rule.logistics.awb_primary_reconciliation_unit
  fields:
    edge_family: execution_guidance
    evidence_basis: execution_constraint_set.fields.rules
    confidence: high
    canonical_cognee_edge: true
    logistics_only: true
    canonical_edge_type: INCLUDES_RULE
    inverse_edge_type: INCLUDED_IN_CONSTRAINT_SET
    materialize_inverse: false
    edge_class: canonical
    source_type: execution_constraint_set
    target_type: rule
```

```yaml
candidate_edge:
  edge_id: edge.execution_constraint_set.logistics_freight_reconciliation.includes_rule.rule.logistics.do_not_join_awb_to_bank_without_batch
  edge_type: INCLUDES_RULE
  source: execution_constraint_set.logistics_freight_reconciliation
  target: rule.logistics.do_not_join_awb_to_bank_without_batch
  fields:
    edge_family: execution_guidance
    evidence_basis: execution_constraint_set.fields.rules
    confidence: high
    canonical_cognee_edge: true
    logistics_only: true
    canonical_edge_type: INCLUDES_RULE
    inverse_edge_type: INCLUDED_IN_CONSTRAINT_SET
    materialize_inverse: false
    edge_class: canonical
    source_type: execution_constraint_set
    target_type: rule
```

```yaml
candidate_edge:
  edge_id: edge.execution_constraint_set.logistics_freight_reconciliation.includes_rule.rule.logistics.preaggregate_before_order_join
  edge_type: INCLUDES_RULE
  source: execution_constraint_set.logistics_freight_reconciliation
  target: rule.logistics.preaggregate_before_order_join
  fields:
    edge_family: execution_guidance
    evidence_basis: execution_constraint_set.fields.rules
    confidence: high
    canonical_cognee_edge: true
    logistics_only: true
    canonical_edge_type: INCLUDES_RULE
    inverse_edge_type: INCLUDED_IN_CONSTRAINT_SET
    materialize_inverse: false
    edge_class: canonical
    source_type: execution_constraint_set
    target_type: rule
```

```yaml
candidate_edge:
  edge_id: edge.execution_constraint_set.logistics_freight_reconciliation.includes_validation_test.validation_test.logistics.required_scope_context
  edge_type: INCLUDES_VALIDATION_TEST
  source: execution_constraint_set.logistics_freight_reconciliation
  target: validation_test.logistics.required_scope_context
  fields:
    edge_family: execution_guidance
    evidence_basis: execution_constraint_set.fields.validation_tests
    confidence: high
    canonical_cognee_edge: true
    logistics_only: true
    canonical_edge_type: INCLUDES_VALIDATION_TEST
    inverse_edge_type: INCLUDED_IN_CONSTRAINT_SET
    materialize_inverse: false
    edge_class: canonical
    source_type: execution_constraint_set
    target_type: validation_test
```

```yaml
candidate_edge:
  edge_id: edge.execution_constraint_set.logistics_freight_reconciliation.includes_validation_test.validation_test.logistics.business_flow_binding_required_for_cross_platform
  edge_type: INCLUDES_VALIDATION_TEST
  source: execution_constraint_set.logistics_freight_reconciliation
  target: validation_test.logistics.business_flow_binding_required_for_cross_platform
  fields:
    edge_family: execution_guidance
    evidence_basis: execution_constraint_set.fields.validation_tests
    confidence: high
    canonical_cognee_edge: true
    logistics_only: true
    canonical_edge_type: INCLUDES_VALIDATION_TEST
    inverse_edge_type: INCLUDED_IN_CONSTRAINT_SET
    materialize_inverse: false
    edge_class: canonical
    source_type: execution_constraint_set
    target_type: validation_test
```

```yaml
candidate_edge:
  edge_id: edge.execution_constraint_set.logistics_freight_reconciliation.includes_validation_test.validation_test.logistics.do_not_create_bfb_from_generic_vendor_doc
  edge_type: INCLUDES_VALIDATION_TEST
  source: execution_constraint_set.logistics_freight_reconciliation
  target: validation_test.logistics.do_not_create_bfb_from_generic_vendor_doc
  fields:
    edge_family: execution_guidance
    evidence_basis: execution_constraint_set.fields.validation_tests
    confidence: high
    canonical_cognee_edge: true
    logistics_only: true
    canonical_edge_type: INCLUDES_VALIDATION_TEST
    inverse_edge_type: INCLUDED_IN_CONSTRAINT_SET
    materialize_inverse: false
    edge_class: canonical
    source_type: execution_constraint_set
    target_type: validation_test
```

```yaml
candidate_edge:
  edge_id: edge.execution_constraint_set.logistics_freight_reconciliation.includes_validation_test.validation_test.logistics.amount_semantics_not_by_name
  edge_type: INCLUDES_VALIDATION_TEST
  source: execution_constraint_set.logistics_freight_reconciliation
  target: validation_test.logistics.amount_semantics_not_by_name
  fields:
    edge_family: execution_guidance
    evidence_basis: execution_constraint_set.fields.validation_tests
    confidence: high
    canonical_cognee_edge: true
    logistics_only: true
    canonical_edge_type: INCLUDES_VALIDATION_TEST
    inverse_edge_type: INCLUDED_IN_CONSTRAINT_SET
    materialize_inverse: false
    edge_class: canonical
    source_type: execution_constraint_set
    target_type: validation_test
```

```yaml
candidate_edge:
  edge_id: edge.execution_constraint_set.logistics_freight_reconciliation.includes_validation_test.validation_test.logistics.charged_amount_table_specific
  edge_type: INCLUDES_VALIDATION_TEST
  source: execution_constraint_set.logistics_freight_reconciliation
  target: validation_test.logistics.charged_amount_table_specific
  fields:
    edge_family: execution_guidance
    evidence_basis: execution_constraint_set.fields.validation_tests
    confidence: high
    canonical_cognee_edge: true
    logistics_only: true
    canonical_edge_type: INCLUDES_VALIDATION_TEST
    inverse_edge_type: INCLUDED_IN_CONSTRAINT_SET
    materialize_inverse: false
    edge_class: canonical
    source_type: execution_constraint_set
    target_type: validation_test
```

```yaml
candidate_edge:
  edge_id: edge.execution_constraint_set.logistics_freight_reconciliation.includes_validation_test.validation_test.logistics.active_filter_when_available
  edge_type: INCLUDES_VALIDATION_TEST
  source: execution_constraint_set.logistics_freight_reconciliation
  target: validation_test.logistics.active_filter_when_available
  fields:
    edge_family: execution_guidance
    evidence_basis: execution_constraint_set.fields.validation_tests
    confidence: high
    canonical_cognee_edge: true
    logistics_only: true
    canonical_edge_type: INCLUDES_VALIDATION_TEST
    inverse_edge_type: INCLUDED_IN_CONSTRAINT_SET
    materialize_inverse: false
    edge_class: canonical
    source_type: execution_constraint_set
    target_type: validation_test
```

```yaml
candidate_edge:
  edge_id: edge.execution_constraint_set.logistics_freight_reconciliation.includes_validation_test.validation_test.logistics.empty_tables_schema_only
  edge_type: INCLUDES_VALIDATION_TEST
  source: execution_constraint_set.logistics_freight_reconciliation
  target: validation_test.logistics.empty_tables_schema_only
  fields:
    edge_family: execution_guidance
    evidence_basis: execution_constraint_set.fields.validation_tests
    confidence: high
    canonical_cognee_edge: true
    logistics_only: true
    canonical_edge_type: INCLUDES_VALIDATION_TEST
    inverse_edge_type: INCLUDED_IN_CONSTRAINT_SET
    materialize_inverse: false
    edge_class: canonical
    source_type: execution_constraint_set
    target_type: validation_test
```

```yaml
candidate_edge:
  edge_id: edge.execution_constraint_set.logistics_freight_reconciliation.includes_validation_test.validation_test.logistics.low_confidence_requires_warning
  edge_type: INCLUDES_VALIDATION_TEST
  source: execution_constraint_set.logistics_freight_reconciliation
  target: validation_test.logistics.low_confidence_requires_warning
  fields:
    edge_family: execution_guidance
    evidence_basis: execution_constraint_set.fields.validation_tests
    confidence: high
    canonical_cognee_edge: true
    logistics_only: true
    canonical_edge_type: INCLUDES_VALIDATION_TEST
    inverse_edge_type: INCLUDED_IN_CONSTRAINT_SET
    materialize_inverse: false
    edge_class: canonical
    source_type: execution_constraint_set
    target_type: validation_test
```

```yaml
candidate_edge:
  edge_id: edge.execution_constraint_set.logistics_freight_reconciliation.includes_validation_test.validation_test.logistics.fallback_sources_explicit_only
  edge_type: INCLUDES_VALIDATION_TEST
  source: execution_constraint_set.logistics_freight_reconciliation
  target: validation_test.logistics.fallback_sources_explicit_only
  fields:
    edge_family: execution_guidance
    evidence_basis: execution_constraint_set.fields.validation_tests
    confidence: high
    canonical_cognee_edge: true
    logistics_only: true
    canonical_edge_type: INCLUDES_VALIDATION_TEST
    inverse_edge_type: INCLUDED_IN_CONSTRAINT_SET
    materialize_inverse: false
    edge_class: canonical
    source_type: execution_constraint_set
    target_type: validation_test
```

```yaml
candidate_edge:
  edge_id: edge.execution_constraint_set.logistics_freight_reconciliation.includes_validation_test.validation_test.logistics.awb_primary_reconciliation_unit
  edge_type: INCLUDES_VALIDATION_TEST
  source: execution_constraint_set.logistics_freight_reconciliation
  target: validation_test.logistics.awb_primary_reconciliation_unit
  fields:
    edge_family: execution_guidance
    evidence_basis: execution_constraint_set.fields.validation_tests
    confidence: high
    canonical_cognee_edge: true
    logistics_only: true
    canonical_edge_type: INCLUDES_VALIDATION_TEST
    inverse_edge_type: INCLUDED_IN_CONSTRAINT_SET
    materialize_inverse: false
    edge_class: canonical
    source_type: execution_constraint_set
    target_type: validation_test
```

```yaml
candidate_edge:
  edge_id: edge.execution_constraint_set.logistics_freight_reconciliation.includes_validation_test.validation_test.logistics.do_not_join_awb_to_bank_without_batch
  edge_type: INCLUDES_VALIDATION_TEST
  source: execution_constraint_set.logistics_freight_reconciliation
  target: validation_test.logistics.do_not_join_awb_to_bank_without_batch
  fields:
    edge_family: execution_guidance
    evidence_basis: execution_constraint_set.fields.validation_tests
    confidence: high
    canonical_cognee_edge: true
    logistics_only: true
    canonical_edge_type: INCLUDES_VALIDATION_TEST
    inverse_edge_type: INCLUDED_IN_CONSTRAINT_SET
    materialize_inverse: false
    edge_class: canonical
    source_type: execution_constraint_set
    target_type: validation_test
```

```yaml
candidate_edge:
  edge_id: edge.execution_constraint_set.logistics_freight_reconciliation.includes_validation_test.validation_test.logistics.preaggregate_before_order_join
  edge_type: INCLUDES_VALIDATION_TEST
  source: execution_constraint_set.logistics_freight_reconciliation
  target: validation_test.logistics.preaggregate_before_order_join
  fields:
    edge_family: execution_guidance
    evidence_basis: execution_constraint_set.fields.validation_tests
    confidence: high
    canonical_cognee_edge: true
    logistics_only: true
    canonical_edge_type: INCLUDES_VALIDATION_TEST
    inverse_edge_type: INCLUDED_IN_CONSTRAINT_SET
    materialize_inverse: false
    edge_class: canonical
    source_type: execution_constraint_set
    target_type: validation_test
```

```yaml
candidate_edge:
  edge_id: edge.execution_constraint_set.logistics_freight_reconciliation.applies_to_query_pattern.query_pattern.logistics.freight_billed_by_awb
  edge_type: APPLIES_TO_QUERY_PATTERN
  source: execution_constraint_set.logistics_freight_reconciliation
  target: query_pattern.logistics.freight_billed_by_awb
  fields:
    edge_family: execution_guidance
    evidence_basis: execution_constraint_set.fields.query_patterns
    confidence: high
    canonical_cognee_edge: true
    logistics_only: true
    canonical_edge_type: APPLIES_TO_QUERY_PATTERN
    inverse_edge_type: HAS_EXECUTION_CONSTRAINT_SET
    materialize_inverse: false
    edge_class: canonical
    source_type: execution_constraint_set
    target_type: query_pattern
```

```yaml
candidate_edge:
  edge_id: edge.execution_constraint_set.logistics_freight_reconciliation.applies_to_query_pattern.query_pattern.logistics.freight_component_breakdown
  edge_type: APPLIES_TO_QUERY_PATTERN
  source: execution_constraint_set.logistics_freight_reconciliation
  target: query_pattern.logistics.freight_component_breakdown
  fields:
    edge_family: execution_guidance
    evidence_basis: execution_constraint_set.fields.query_patterns
    confidence: high
    canonical_cognee_edge: true
    logistics_only: true
    canonical_edge_type: APPLIES_TO_QUERY_PATTERN
    inverse_edge_type: HAS_EXECUTION_CONSTRAINT_SET
    materialize_inverse: false
    edge_class: canonical
    source_type: execution_constraint_set
    target_type: query_pattern
```

```yaml
candidate_edge:
  edge_id: edge.execution_constraint_set.logistics_freight_reconciliation.applies_to_query_pattern.query_pattern.logistics.freight_overcharge_check
  edge_type: APPLIES_TO_QUERY_PATTERN
  source: execution_constraint_set.logistics_freight_reconciliation
  target: query_pattern.logistics.freight_overcharge_check
  fields:
    edge_family: execution_guidance
    evidence_basis: execution_constraint_set.fields.query_patterns
    confidence: high
    canonical_cognee_edge: true
    logistics_only: true
    canonical_edge_type: APPLIES_TO_QUERY_PATTERN
    inverse_edge_type: HAS_EXECUTION_CONSTRAINT_SET
    materialize_inverse: false
    edge_class: canonical
    source_type: execution_constraint_set
    target_type: query_pattern
```

```yaml
candidate_edge:
  edge_id: edge.execution_constraint_set.logistics_freight_reconciliation.applies_to_query_pattern.query_pattern.logistics.rto_freight_validation
  edge_type: APPLIES_TO_QUERY_PATTERN
  source: execution_constraint_set.logistics_freight_reconciliation
  target: query_pattern.logistics.rto_freight_validation
  fields:
    edge_family: execution_guidance
    evidence_basis: execution_constraint_set.fields.query_patterns
    confidence: high
    canonical_cognee_edge: true
    logistics_only: true
    canonical_edge_type: APPLIES_TO_QUERY_PATTERN
    inverse_edge_type: HAS_EXECUTION_CONSTRAINT_SET
    materialize_inverse: false
    edge_class: canonical
    source_type: execution_constraint_set
    target_type: query_pattern
```

```yaml
candidate_edge:
  edge_id: edge.execution_constraint_set.logistics_freight_reconciliation.applies_to_query_pattern.query_pattern.logistics.cod_fee_on_prepaid_detection
  edge_type: APPLIES_TO_QUERY_PATTERN
  source: execution_constraint_set.logistics_freight_reconciliation
  target: query_pattern.logistics.cod_fee_on_prepaid_detection
  fields:
    edge_family: execution_guidance
    evidence_basis: execution_constraint_set.fields.query_patterns
    confidence: high
    canonical_cognee_edge: true
    logistics_only: true
    canonical_edge_type: APPLIES_TO_QUERY_PATTERN
    inverse_edge_type: HAS_EXECUTION_CONSTRAINT_SET
    materialize_inverse: false
    edge_class: canonical
    source_type: execution_constraint_set
    target_type: query_pattern
```

```yaml
candidate_edge:
  edge_id: edge.execution_constraint_set.logistics_batch_to_bank.includes_rule.rule.logistics.required_scope_context
  edge_type: INCLUDES_RULE
  source: execution_constraint_set.logistics_batch_to_bank
  target: rule.logistics.required_scope_context
  fields:
    edge_family: execution_guidance
    evidence_basis: execution_constraint_set.fields.rules
    confidence: high
    canonical_cognee_edge: true
    logistics_only: true
    canonical_edge_type: INCLUDES_RULE
    inverse_edge_type: INCLUDED_IN_CONSTRAINT_SET
    materialize_inverse: false
    edge_class: canonical
    source_type: execution_constraint_set
    target_type: rule
```

```yaml
candidate_edge:
  edge_id: edge.execution_constraint_set.logistics_batch_to_bank.includes_rule.rule.logistics.business_flow_binding_required_for_cross_platform
  edge_type: INCLUDES_RULE
  source: execution_constraint_set.logistics_batch_to_bank
  target: rule.logistics.business_flow_binding_required_for_cross_platform
  fields:
    edge_family: execution_guidance
    evidence_basis: execution_constraint_set.fields.rules
    confidence: high
    canonical_cognee_edge: true
    logistics_only: true
    canonical_edge_type: INCLUDES_RULE
    inverse_edge_type: INCLUDED_IN_CONSTRAINT_SET
    materialize_inverse: false
    edge_class: canonical
    source_type: execution_constraint_set
    target_type: rule
```

```yaml
candidate_edge:
  edge_id: edge.execution_constraint_set.logistics_batch_to_bank.includes_rule.rule.logistics.do_not_create_bfb_from_generic_vendor_doc
  edge_type: INCLUDES_RULE
  source: execution_constraint_set.logistics_batch_to_bank
  target: rule.logistics.do_not_create_bfb_from_generic_vendor_doc
  fields:
    edge_family: execution_guidance
    evidence_basis: execution_constraint_set.fields.rules
    confidence: high
    canonical_cognee_edge: true
    logistics_only: true
    canonical_edge_type: INCLUDES_RULE
    inverse_edge_type: INCLUDED_IN_CONSTRAINT_SET
    materialize_inverse: false
    edge_class: canonical
    source_type: execution_constraint_set
    target_type: rule
```

```yaml
candidate_edge:
  edge_id: edge.execution_constraint_set.logistics_batch_to_bank.includes_rule.rule.logistics.amount_semantics_not_by_name
  edge_type: INCLUDES_RULE
  source: execution_constraint_set.logistics_batch_to_bank
  target: rule.logistics.amount_semantics_not_by_name
  fields:
    edge_family: execution_guidance
    evidence_basis: execution_constraint_set.fields.rules
    confidence: high
    canonical_cognee_edge: true
    logistics_only: true
    canonical_edge_type: INCLUDES_RULE
    inverse_edge_type: INCLUDED_IN_CONSTRAINT_SET
    materialize_inverse: false
    edge_class: canonical
    source_type: execution_constraint_set
    target_type: rule
```

```yaml
candidate_edge:
  edge_id: edge.execution_constraint_set.logistics_batch_to_bank.includes_rule.rule.logistics.charged_amount_table_specific
  edge_type: INCLUDES_RULE
  source: execution_constraint_set.logistics_batch_to_bank
  target: rule.logistics.charged_amount_table_specific
  fields:
    edge_family: execution_guidance
    evidence_basis: execution_constraint_set.fields.rules
    confidence: high
    canonical_cognee_edge: true
    logistics_only: true
    canonical_edge_type: INCLUDES_RULE
    inverse_edge_type: INCLUDED_IN_CONSTRAINT_SET
    materialize_inverse: false
    edge_class: canonical
    source_type: execution_constraint_set
    target_type: rule
```

```yaml
candidate_edge:
  edge_id: edge.execution_constraint_set.logistics_batch_to_bank.includes_rule.rule.logistics.active_filter_when_available
  edge_type: INCLUDES_RULE
  source: execution_constraint_set.logistics_batch_to_bank
  target: rule.logistics.active_filter_when_available
  fields:
    edge_family: execution_guidance
    evidence_basis: execution_constraint_set.fields.rules
    confidence: high
    canonical_cognee_edge: true
    logistics_only: true
    canonical_edge_type: INCLUDES_RULE
    inverse_edge_type: INCLUDED_IN_CONSTRAINT_SET
    materialize_inverse: false
    edge_class: canonical
    source_type: execution_constraint_set
    target_type: rule
```

```yaml
candidate_edge:
  edge_id: edge.execution_constraint_set.logistics_batch_to_bank.includes_rule.rule.logistics.empty_tables_schema_only
  edge_type: INCLUDES_RULE
  source: execution_constraint_set.logistics_batch_to_bank
  target: rule.logistics.empty_tables_schema_only
  fields:
    edge_family: execution_guidance
    evidence_basis: execution_constraint_set.fields.rules
    confidence: high
    canonical_cognee_edge: true
    logistics_only: true
    canonical_edge_type: INCLUDES_RULE
    inverse_edge_type: INCLUDED_IN_CONSTRAINT_SET
    materialize_inverse: false
    edge_class: canonical
    source_type: execution_constraint_set
    target_type: rule
```

```yaml
candidate_edge:
  edge_id: edge.execution_constraint_set.logistics_batch_to_bank.includes_rule.rule.logistics.low_confidence_requires_warning
  edge_type: INCLUDES_RULE
  source: execution_constraint_set.logistics_batch_to_bank
  target: rule.logistics.low_confidence_requires_warning
  fields:
    edge_family: execution_guidance
    evidence_basis: execution_constraint_set.fields.rules
    confidence: high
    canonical_cognee_edge: true
    logistics_only: true
    canonical_edge_type: INCLUDES_RULE
    inverse_edge_type: INCLUDED_IN_CONSTRAINT_SET
    materialize_inverse: false
    edge_class: canonical
    source_type: execution_constraint_set
    target_type: rule
```

```yaml
candidate_edge:
  edge_id: edge.execution_constraint_set.logistics_batch_to_bank.includes_rule.rule.logistics.fallback_sources_explicit_only
  edge_type: INCLUDES_RULE
  source: execution_constraint_set.logistics_batch_to_bank
  target: rule.logistics.fallback_sources_explicit_only
  fields:
    edge_family: execution_guidance
    evidence_basis: execution_constraint_set.fields.rules
    confidence: high
    canonical_cognee_edge: true
    logistics_only: true
    canonical_edge_type: INCLUDES_RULE
    inverse_edge_type: INCLUDED_IN_CONSTRAINT_SET
    materialize_inverse: false
    edge_class: canonical
    source_type: execution_constraint_set
    target_type: rule
```

```yaml
candidate_edge:
  edge_id: edge.execution_constraint_set.logistics_batch_to_bank.includes_rule.rule.logistics.awb_primary_reconciliation_unit
  edge_type: INCLUDES_RULE
  source: execution_constraint_set.logistics_batch_to_bank
  target: rule.logistics.awb_primary_reconciliation_unit
  fields:
    edge_family: execution_guidance
    evidence_basis: execution_constraint_set.fields.rules
    confidence: high
    canonical_cognee_edge: true
    logistics_only: true
    canonical_edge_type: INCLUDES_RULE
    inverse_edge_type: INCLUDED_IN_CONSTRAINT_SET
    materialize_inverse: false
    edge_class: canonical
    source_type: execution_constraint_set
    target_type: rule
```

```yaml
candidate_edge:
  edge_id: edge.execution_constraint_set.logistics_batch_to_bank.includes_rule.rule.logistics.do_not_join_awb_to_bank_without_batch
  edge_type: INCLUDES_RULE
  source: execution_constraint_set.logistics_batch_to_bank
  target: rule.logistics.do_not_join_awb_to_bank_without_batch
  fields:
    edge_family: execution_guidance
    evidence_basis: execution_constraint_set.fields.rules
    confidence: high
    canonical_cognee_edge: true
    logistics_only: true
    canonical_edge_type: INCLUDES_RULE
    inverse_edge_type: INCLUDED_IN_CONSTRAINT_SET
    materialize_inverse: false
    edge_class: canonical
    source_type: execution_constraint_set
    target_type: rule
```

```yaml
candidate_edge:
  edge_id: edge.execution_constraint_set.logistics_batch_to_bank.includes_rule.rule.logistics.preaggregate_before_order_join
  edge_type: INCLUDES_RULE
  source: execution_constraint_set.logistics_batch_to_bank
  target: rule.logistics.preaggregate_before_order_join
  fields:
    edge_family: execution_guidance
    evidence_basis: execution_constraint_set.fields.rules
    confidence: high
    canonical_cognee_edge: true
    logistics_only: true
    canonical_edge_type: INCLUDES_RULE
    inverse_edge_type: INCLUDED_IN_CONSTRAINT_SET
    materialize_inverse: false
    edge_class: canonical
    source_type: execution_constraint_set
    target_type: rule
```

```yaml
candidate_edge:
  edge_id: edge.execution_constraint_set.logistics_batch_to_bank.includes_validation_test.validation_test.logistics.required_scope_context
  edge_type: INCLUDES_VALIDATION_TEST
  source: execution_constraint_set.logistics_batch_to_bank
  target: validation_test.logistics.required_scope_context
  fields:
    edge_family: execution_guidance
    evidence_basis: execution_constraint_set.fields.validation_tests
    confidence: high
    canonical_cognee_edge: true
    logistics_only: true
    canonical_edge_type: INCLUDES_VALIDATION_TEST
    inverse_edge_type: INCLUDED_IN_CONSTRAINT_SET
    materialize_inverse: false
    edge_class: canonical
    source_type: execution_constraint_set
    target_type: validation_test
```

```yaml
candidate_edge:
  edge_id: edge.execution_constraint_set.logistics_batch_to_bank.includes_validation_test.validation_test.logistics.business_flow_binding_required_for_cross_platform
  edge_type: INCLUDES_VALIDATION_TEST
  source: execution_constraint_set.logistics_batch_to_bank
  target: validation_test.logistics.business_flow_binding_required_for_cross_platform
  fields:
    edge_family: execution_guidance
    evidence_basis: execution_constraint_set.fields.validation_tests
    confidence: high
    canonical_cognee_edge: true
    logistics_only: true
    canonical_edge_type: INCLUDES_VALIDATION_TEST
    inverse_edge_type: INCLUDED_IN_CONSTRAINT_SET
    materialize_inverse: false
    edge_class: canonical
    source_type: execution_constraint_set
    target_type: validation_test
```

```yaml
candidate_edge:
  edge_id: edge.execution_constraint_set.logistics_batch_to_bank.includes_validation_test.validation_test.logistics.do_not_create_bfb_from_generic_vendor_doc
  edge_type: INCLUDES_VALIDATION_TEST
  source: execution_constraint_set.logistics_batch_to_bank
  target: validation_test.logistics.do_not_create_bfb_from_generic_vendor_doc
  fields:
    edge_family: execution_guidance
    evidence_basis: execution_constraint_set.fields.validation_tests
    confidence: high
    canonical_cognee_edge: true
    logistics_only: true
    canonical_edge_type: INCLUDES_VALIDATION_TEST
    inverse_edge_type: INCLUDED_IN_CONSTRAINT_SET
    materialize_inverse: false
    edge_class: canonical
    source_type: execution_constraint_set
    target_type: validation_test
```

```yaml
candidate_edge:
  edge_id: edge.execution_constraint_set.logistics_batch_to_bank.includes_validation_test.validation_test.logistics.amount_semantics_not_by_name
  edge_type: INCLUDES_VALIDATION_TEST
  source: execution_constraint_set.logistics_batch_to_bank
  target: validation_test.logistics.amount_semantics_not_by_name
  fields:
    edge_family: execution_guidance
    evidence_basis: execution_constraint_set.fields.validation_tests
    confidence: high
    canonical_cognee_edge: true
    logistics_only: true
    canonical_edge_type: INCLUDES_VALIDATION_TEST
    inverse_edge_type: INCLUDED_IN_CONSTRAINT_SET
    materialize_inverse: false
    edge_class: canonical
    source_type: execution_constraint_set
    target_type: validation_test
```

```yaml
candidate_edge:
  edge_id: edge.execution_constraint_set.logistics_batch_to_bank.includes_validation_test.validation_test.logistics.charged_amount_table_specific
  edge_type: INCLUDES_VALIDATION_TEST
  source: execution_constraint_set.logistics_batch_to_bank
  target: validation_test.logistics.charged_amount_table_specific
  fields:
    edge_family: execution_guidance
    evidence_basis: execution_constraint_set.fields.validation_tests
    confidence: high
    canonical_cognee_edge: true
    logistics_only: true
    canonical_edge_type: INCLUDES_VALIDATION_TEST
    inverse_edge_type: INCLUDED_IN_CONSTRAINT_SET
    materialize_inverse: false
    edge_class: canonical
    source_type: execution_constraint_set
    target_type: validation_test
```

```yaml
candidate_edge:
  edge_id: edge.execution_constraint_set.logistics_batch_to_bank.includes_validation_test.validation_test.logistics.active_filter_when_available
  edge_type: INCLUDES_VALIDATION_TEST
  source: execution_constraint_set.logistics_batch_to_bank
  target: validation_test.logistics.active_filter_when_available
  fields:
    edge_family: execution_guidance
    evidence_basis: execution_constraint_set.fields.validation_tests
    confidence: high
    canonical_cognee_edge: true
    logistics_only: true
    canonical_edge_type: INCLUDES_VALIDATION_TEST
    inverse_edge_type: INCLUDED_IN_CONSTRAINT_SET
    materialize_inverse: false
    edge_class: canonical
    source_type: execution_constraint_set
    target_type: validation_test
```

```yaml
candidate_edge:
  edge_id: edge.execution_constraint_set.logistics_batch_to_bank.includes_validation_test.validation_test.logistics.empty_tables_schema_only
  edge_type: INCLUDES_VALIDATION_TEST
  source: execution_constraint_set.logistics_batch_to_bank
  target: validation_test.logistics.empty_tables_schema_only
  fields:
    edge_family: execution_guidance
    evidence_basis: execution_constraint_set.fields.validation_tests
    confidence: high
    canonical_cognee_edge: true
    logistics_only: true
    canonical_edge_type: INCLUDES_VALIDATION_TEST
    inverse_edge_type: INCLUDED_IN_CONSTRAINT_SET
    materialize_inverse: false
    edge_class: canonical
    source_type: execution_constraint_set
    target_type: validation_test
```

```yaml
candidate_edge:
  edge_id: edge.execution_constraint_set.logistics_batch_to_bank.includes_validation_test.validation_test.logistics.low_confidence_requires_warning
  edge_type: INCLUDES_VALIDATION_TEST
  source: execution_constraint_set.logistics_batch_to_bank
  target: validation_test.logistics.low_confidence_requires_warning
  fields:
    edge_family: execution_guidance
    evidence_basis: execution_constraint_set.fields.validation_tests
    confidence: high
    canonical_cognee_edge: true
    logistics_only: true
    canonical_edge_type: INCLUDES_VALIDATION_TEST
    inverse_edge_type: INCLUDED_IN_CONSTRAINT_SET
    materialize_inverse: false
    edge_class: canonical
    source_type: execution_constraint_set
    target_type: validation_test
```

```yaml
candidate_edge:
  edge_id: edge.execution_constraint_set.logistics_batch_to_bank.includes_validation_test.validation_test.logistics.fallback_sources_explicit_only
  edge_type: INCLUDES_VALIDATION_TEST
  source: execution_constraint_set.logistics_batch_to_bank
  target: validation_test.logistics.fallback_sources_explicit_only
  fields:
    edge_family: execution_guidance
    evidence_basis: execution_constraint_set.fields.validation_tests
    confidence: high
    canonical_cognee_edge: true
    logistics_only: true
    canonical_edge_type: INCLUDES_VALIDATION_TEST
    inverse_edge_type: INCLUDED_IN_CONSTRAINT_SET
    materialize_inverse: false
    edge_class: canonical
    source_type: execution_constraint_set
    target_type: validation_test
```

```yaml
candidate_edge:
  edge_id: edge.execution_constraint_set.logistics_batch_to_bank.includes_validation_test.validation_test.logistics.awb_primary_reconciliation_unit
  edge_type: INCLUDES_VALIDATION_TEST
  source: execution_constraint_set.logistics_batch_to_bank
  target: validation_test.logistics.awb_primary_reconciliation_unit
  fields:
    edge_family: execution_guidance
    evidence_basis: execution_constraint_set.fields.validation_tests
    confidence: high
    canonical_cognee_edge: true
    logistics_only: true
    canonical_edge_type: INCLUDES_VALIDATION_TEST
    inverse_edge_type: INCLUDED_IN_CONSTRAINT_SET
    materialize_inverse: false
    edge_class: canonical
    source_type: execution_constraint_set
    target_type: validation_test
```

```yaml
candidate_edge:
  edge_id: edge.execution_constraint_set.logistics_batch_to_bank.includes_validation_test.validation_test.logistics.do_not_join_awb_to_bank_without_batch
  edge_type: INCLUDES_VALIDATION_TEST
  source: execution_constraint_set.logistics_batch_to_bank
  target: validation_test.logistics.do_not_join_awb_to_bank_without_batch
  fields:
    edge_family: execution_guidance
    evidence_basis: execution_constraint_set.fields.validation_tests
    confidence: high
    canonical_cognee_edge: true
    logistics_only: true
    canonical_edge_type: INCLUDES_VALIDATION_TEST
    inverse_edge_type: INCLUDED_IN_CONSTRAINT_SET
    materialize_inverse: false
    edge_class: canonical
    source_type: execution_constraint_set
    target_type: validation_test
```

```yaml
candidate_edge:
  edge_id: edge.execution_constraint_set.logistics_batch_to_bank.includes_validation_test.validation_test.logistics.preaggregate_before_order_join
  edge_type: INCLUDES_VALIDATION_TEST
  source: execution_constraint_set.logistics_batch_to_bank
  target: validation_test.logistics.preaggregate_before_order_join
  fields:
    edge_family: execution_guidance
    evidence_basis: execution_constraint_set.fields.validation_tests
    confidence: high
    canonical_cognee_edge: true
    logistics_only: true
    canonical_edge_type: INCLUDES_VALIDATION_TEST
    inverse_edge_type: INCLUDED_IN_CONSTRAINT_SET
    materialize_inverse: false
    edge_class: canonical
    source_type: execution_constraint_set
    target_type: validation_test
```

```yaml
candidate_edge:
  edge_id: edge.execution_constraint_set.logistics_batch_to_bank.applies_to_query_pattern.query_pattern.logistics.courier_batch_to_bank_bridge
  edge_type: APPLIES_TO_QUERY_PATTERN
  source: execution_constraint_set.logistics_batch_to_bank
  target: query_pattern.logistics.courier_batch_to_bank_bridge
  fields:
    edge_family: execution_guidance
    evidence_basis: execution_constraint_set.fields.query_patterns
    confidence: high
    canonical_cognee_edge: true
    logistics_only: true
    canonical_edge_type: APPLIES_TO_QUERY_PATTERN
    inverse_edge_type: HAS_EXECUTION_CONSTRAINT_SET
    materialize_inverse: false
    edge_class: canonical
    source_type: execution_constraint_set
    target_type: query_pattern
```

```yaml
candidate_edge:
  edge_id: edge.execution_constraint_set.logistics_batch_to_bank.applies_to_query_pattern.query_pattern.logistics.bank_credit_unmatched_courier_reference
  edge_type: APPLIES_TO_QUERY_PATTERN
  source: execution_constraint_set.logistics_batch_to_bank
  target: query_pattern.logistics.bank_credit_unmatched_courier_reference
  fields:
    edge_family: execution_guidance
    evidence_basis: execution_constraint_set.fields.query_patterns
    confidence: high
    canonical_cognee_edge: true
    logistics_only: true
    canonical_edge_type: APPLIES_TO_QUERY_PATTERN
    inverse_edge_type: HAS_EXECUTION_CONSTRAINT_SET
    materialize_inverse: false
    edge_class: canonical
    source_type: execution_constraint_set
    target_type: query_pattern
```

```yaml
candidate_edge:
  edge_id: edge.execution_constraint_set.logistics_batch_to_bank.applies_to_query_pattern.query_pattern.logistics.end_to_end_logistics_money_flow_trace
  edge_type: APPLIES_TO_QUERY_PATTERN
  source: execution_constraint_set.logistics_batch_to_bank
  target: query_pattern.logistics.end_to_end_logistics_money_flow_trace
  fields:
    edge_family: execution_guidance
    evidence_basis: execution_constraint_set.fields.query_patterns
    confidence: high
    canonical_cognee_edge: true
    logistics_only: true
    canonical_edge_type: APPLIES_TO_QUERY_PATTERN
    inverse_edge_type: HAS_EXECUTION_CONSTRAINT_SET
    materialize_inverse: false
    edge_class: canonical
    source_type: execution_constraint_set
    target_type: query_pattern
```

```yaml
candidate_edge:
  edge_id: edge.execution_constraint_set.shiprocket_guardrails.includes_rule.rule.logistics.required_scope_context
  edge_type: INCLUDES_RULE
  source: execution_constraint_set.shiprocket_guardrails
  target: rule.logistics.required_scope_context
  fields:
    edge_family: execution_guidance
    evidence_basis: execution_constraint_set.fields.rules
    confidence: high
    canonical_cognee_edge: true
    logistics_only: true
    canonical_edge_type: INCLUDES_RULE
    inverse_edge_type: INCLUDED_IN_CONSTRAINT_SET
    materialize_inverse: false
    edge_class: canonical
    source_type: execution_constraint_set
    target_type: rule
```

```yaml
candidate_edge:
  edge_id: edge.execution_constraint_set.shiprocket_guardrails.includes_rule.rule.logistics.business_flow_binding_required_for_cross_platform
  edge_type: INCLUDES_RULE
  source: execution_constraint_set.shiprocket_guardrails
  target: rule.logistics.business_flow_binding_required_for_cross_platform
  fields:
    edge_family: execution_guidance
    evidence_basis: execution_constraint_set.fields.rules
    confidence: high
    canonical_cognee_edge: true
    logistics_only: true
    canonical_edge_type: INCLUDES_RULE
    inverse_edge_type: INCLUDED_IN_CONSTRAINT_SET
    materialize_inverse: false
    edge_class: canonical
    source_type: execution_constraint_set
    target_type: rule
```

```yaml
candidate_edge:
  edge_id: edge.execution_constraint_set.shiprocket_guardrails.includes_rule.rule.logistics.do_not_create_bfb_from_generic_vendor_doc
  edge_type: INCLUDES_RULE
  source: execution_constraint_set.shiprocket_guardrails
  target: rule.logistics.do_not_create_bfb_from_generic_vendor_doc
  fields:
    edge_family: execution_guidance
    evidence_basis: execution_constraint_set.fields.rules
    confidence: high
    canonical_cognee_edge: true
    logistics_only: true
    canonical_edge_type: INCLUDES_RULE
    inverse_edge_type: INCLUDED_IN_CONSTRAINT_SET
    materialize_inverse: false
    edge_class: canonical
    source_type: execution_constraint_set
    target_type: rule
```

```yaml
candidate_edge:
  edge_id: edge.execution_constraint_set.shiprocket_guardrails.includes_rule.rule.logistics.amount_semantics_not_by_name
  edge_type: INCLUDES_RULE
  source: execution_constraint_set.shiprocket_guardrails
  target: rule.logistics.amount_semantics_not_by_name
  fields:
    edge_family: execution_guidance
    evidence_basis: execution_constraint_set.fields.rules
    confidence: high
    canonical_cognee_edge: true
    logistics_only: true
    canonical_edge_type: INCLUDES_RULE
    inverse_edge_type: INCLUDED_IN_CONSTRAINT_SET
    materialize_inverse: false
    edge_class: canonical
    source_type: execution_constraint_set
    target_type: rule
```

```yaml
candidate_edge:
  edge_id: edge.execution_constraint_set.shiprocket_guardrails.includes_rule.rule.logistics.charged_amount_table_specific
  edge_type: INCLUDES_RULE
  source: execution_constraint_set.shiprocket_guardrails
  target: rule.logistics.charged_amount_table_specific
  fields:
    edge_family: execution_guidance
    evidence_basis: execution_constraint_set.fields.rules
    confidence: high
    canonical_cognee_edge: true
    logistics_only: true
    canonical_edge_type: INCLUDES_RULE
    inverse_edge_type: INCLUDED_IN_CONSTRAINT_SET
    materialize_inverse: false
    edge_class: canonical
    source_type: execution_constraint_set
    target_type: rule
```

```yaml
candidate_edge:
  edge_id: edge.execution_constraint_set.shiprocket_guardrails.includes_rule.rule.logistics.active_filter_when_available
  edge_type: INCLUDES_RULE
  source: execution_constraint_set.shiprocket_guardrails
  target: rule.logistics.active_filter_when_available
  fields:
    edge_family: execution_guidance
    evidence_basis: execution_constraint_set.fields.rules
    confidence: high
    canonical_cognee_edge: true
    logistics_only: true
    canonical_edge_type: INCLUDES_RULE
    inverse_edge_type: INCLUDED_IN_CONSTRAINT_SET
    materialize_inverse: false
    edge_class: canonical
    source_type: execution_constraint_set
    target_type: rule
```

```yaml
candidate_edge:
  edge_id: edge.execution_constraint_set.shiprocket_guardrails.includes_rule.rule.logistics.empty_tables_schema_only
  edge_type: INCLUDES_RULE
  source: execution_constraint_set.shiprocket_guardrails
  target: rule.logistics.empty_tables_schema_only
  fields:
    edge_family: execution_guidance
    evidence_basis: execution_constraint_set.fields.rules
    confidence: high
    canonical_cognee_edge: true
    logistics_only: true
    canonical_edge_type: INCLUDES_RULE
    inverse_edge_type: INCLUDED_IN_CONSTRAINT_SET
    materialize_inverse: false
    edge_class: canonical
    source_type: execution_constraint_set
    target_type: rule
```

```yaml
candidate_edge:
  edge_id: edge.execution_constraint_set.shiprocket_guardrails.includes_rule.rule.logistics.low_confidence_requires_warning
  edge_type: INCLUDES_RULE
  source: execution_constraint_set.shiprocket_guardrails
  target: rule.logistics.low_confidence_requires_warning
  fields:
    edge_family: execution_guidance
    evidence_basis: execution_constraint_set.fields.rules
    confidence: high
    canonical_cognee_edge: true
    logistics_only: true
    canonical_edge_type: INCLUDES_RULE
    inverse_edge_type: INCLUDED_IN_CONSTRAINT_SET
    materialize_inverse: false
    edge_class: canonical
    source_type: execution_constraint_set
    target_type: rule
```

```yaml
candidate_edge:
  edge_id: edge.execution_constraint_set.shiprocket_guardrails.includes_rule.rule.logistics.fallback_sources_explicit_only
  edge_type: INCLUDES_RULE
  source: execution_constraint_set.shiprocket_guardrails
  target: rule.logistics.fallback_sources_explicit_only
  fields:
    edge_family: execution_guidance
    evidence_basis: execution_constraint_set.fields.rules
    confidence: high
    canonical_cognee_edge: true
    logistics_only: true
    canonical_edge_type: INCLUDES_RULE
    inverse_edge_type: INCLUDED_IN_CONSTRAINT_SET
    materialize_inverse: false
    edge_class: canonical
    source_type: execution_constraint_set
    target_type: rule
```

```yaml
candidate_edge:
  edge_id: edge.execution_constraint_set.shiprocket_guardrails.includes_rule.rule.logistics.awb_primary_reconciliation_unit
  edge_type: INCLUDES_RULE
  source: execution_constraint_set.shiprocket_guardrails
  target: rule.logistics.awb_primary_reconciliation_unit
  fields:
    edge_family: execution_guidance
    evidence_basis: execution_constraint_set.fields.rules
    confidence: high
    canonical_cognee_edge: true
    logistics_only: true
    canonical_edge_type: INCLUDES_RULE
    inverse_edge_type: INCLUDED_IN_CONSTRAINT_SET
    materialize_inverse: false
    edge_class: canonical
    source_type: execution_constraint_set
    target_type: rule
```

```yaml
candidate_edge:
  edge_id: edge.execution_constraint_set.shiprocket_guardrails.includes_rule.rule.logistics.do_not_join_awb_to_bank_without_batch
  edge_type: INCLUDES_RULE
  source: execution_constraint_set.shiprocket_guardrails
  target: rule.logistics.do_not_join_awb_to_bank_without_batch
  fields:
    edge_family: execution_guidance
    evidence_basis: execution_constraint_set.fields.rules
    confidence: high
    canonical_cognee_edge: true
    logistics_only: true
    canonical_edge_type: INCLUDES_RULE
    inverse_edge_type: INCLUDED_IN_CONSTRAINT_SET
    materialize_inverse: false
    edge_class: canonical
    source_type: execution_constraint_set
    target_type: rule
```

```yaml
candidate_edge:
  edge_id: edge.execution_constraint_set.shiprocket_guardrails.includes_rule.rule.logistics.preaggregate_before_order_join
  edge_type: INCLUDES_RULE
  source: execution_constraint_set.shiprocket_guardrails
  target: rule.logistics.preaggregate_before_order_join
  fields:
    edge_family: execution_guidance
    evidence_basis: execution_constraint_set.fields.rules
    confidence: high
    canonical_cognee_edge: true
    logistics_only: true
    canonical_edge_type: INCLUDES_RULE
    inverse_edge_type: INCLUDED_IN_CONSTRAINT_SET
    materialize_inverse: false
    edge_class: canonical
    source_type: execution_constraint_set
    target_type: rule
```

```yaml
candidate_edge:
  edge_id: edge.execution_constraint_set.shiprocket_guardrails.includes_validation_test.validation_test.logistics.required_scope_context
  edge_type: INCLUDES_VALIDATION_TEST
  source: execution_constraint_set.shiprocket_guardrails
  target: validation_test.logistics.required_scope_context
  fields:
    edge_family: execution_guidance
    evidence_basis: execution_constraint_set.fields.validation_tests
    confidence: high
    canonical_cognee_edge: true
    logistics_only: true
    canonical_edge_type: INCLUDES_VALIDATION_TEST
    inverse_edge_type: INCLUDED_IN_CONSTRAINT_SET
    materialize_inverse: false
    edge_class: canonical
    source_type: execution_constraint_set
    target_type: validation_test
```

```yaml
candidate_edge:
  edge_id: edge.execution_constraint_set.shiprocket_guardrails.includes_validation_test.validation_test.logistics.business_flow_binding_required_for_cross_platform
  edge_type: INCLUDES_VALIDATION_TEST
  source: execution_constraint_set.shiprocket_guardrails
  target: validation_test.logistics.business_flow_binding_required_for_cross_platform
  fields:
    edge_family: execution_guidance
    evidence_basis: execution_constraint_set.fields.validation_tests
    confidence: high
    canonical_cognee_edge: true
    logistics_only: true
    canonical_edge_type: INCLUDES_VALIDATION_TEST
    inverse_edge_type: INCLUDED_IN_CONSTRAINT_SET
    materialize_inverse: false
    edge_class: canonical
    source_type: execution_constraint_set
    target_type: validation_test
```

```yaml
candidate_edge:
  edge_id: edge.execution_constraint_set.shiprocket_guardrails.includes_validation_test.validation_test.logistics.do_not_create_bfb_from_generic_vendor_doc
  edge_type: INCLUDES_VALIDATION_TEST
  source: execution_constraint_set.shiprocket_guardrails
  target: validation_test.logistics.do_not_create_bfb_from_generic_vendor_doc
  fields:
    edge_family: execution_guidance
    evidence_basis: execution_constraint_set.fields.validation_tests
    confidence: high
    canonical_cognee_edge: true
    logistics_only: true
    canonical_edge_type: INCLUDES_VALIDATION_TEST
    inverse_edge_type: INCLUDED_IN_CONSTRAINT_SET
    materialize_inverse: false
    edge_class: canonical
    source_type: execution_constraint_set
    target_type: validation_test
```

```yaml
candidate_edge:
  edge_id: edge.execution_constraint_set.shiprocket_guardrails.includes_validation_test.validation_test.logistics.amount_semantics_not_by_name
  edge_type: INCLUDES_VALIDATION_TEST
  source: execution_constraint_set.shiprocket_guardrails
  target: validation_test.logistics.amount_semantics_not_by_name
  fields:
    edge_family: execution_guidance
    evidence_basis: execution_constraint_set.fields.validation_tests
    confidence: high
    canonical_cognee_edge: true
    logistics_only: true
    canonical_edge_type: INCLUDES_VALIDATION_TEST
    inverse_edge_type: INCLUDED_IN_CONSTRAINT_SET
    materialize_inverse: false
    edge_class: canonical
    source_type: execution_constraint_set
    target_type: validation_test
```

```yaml
candidate_edge:
  edge_id: edge.execution_constraint_set.shiprocket_guardrails.includes_validation_test.validation_test.logistics.charged_amount_table_specific
  edge_type: INCLUDES_VALIDATION_TEST
  source: execution_constraint_set.shiprocket_guardrails
  target: validation_test.logistics.charged_amount_table_specific
  fields:
    edge_family: execution_guidance
    evidence_basis: execution_constraint_set.fields.validation_tests
    confidence: high
    canonical_cognee_edge: true
    logistics_only: true
    canonical_edge_type: INCLUDES_VALIDATION_TEST
    inverse_edge_type: INCLUDED_IN_CONSTRAINT_SET
    materialize_inverse: false
    edge_class: canonical
    source_type: execution_constraint_set
    target_type: validation_test
```

```yaml
candidate_edge:
  edge_id: edge.execution_constraint_set.shiprocket_guardrails.includes_validation_test.validation_test.logistics.active_filter_when_available
  edge_type: INCLUDES_VALIDATION_TEST
  source: execution_constraint_set.shiprocket_guardrails
  target: validation_test.logistics.active_filter_when_available
  fields:
    edge_family: execution_guidance
    evidence_basis: execution_constraint_set.fields.validation_tests
    confidence: high
    canonical_cognee_edge: true
    logistics_only: true
    canonical_edge_type: INCLUDES_VALIDATION_TEST
    inverse_edge_type: INCLUDED_IN_CONSTRAINT_SET
    materialize_inverse: false
    edge_class: canonical
    source_type: execution_constraint_set
    target_type: validation_test
```

```yaml
candidate_edge:
  edge_id: edge.execution_constraint_set.shiprocket_guardrails.includes_validation_test.validation_test.logistics.empty_tables_schema_only
  edge_type: INCLUDES_VALIDATION_TEST
  source: execution_constraint_set.shiprocket_guardrails
  target: validation_test.logistics.empty_tables_schema_only
  fields:
    edge_family: execution_guidance
    evidence_basis: execution_constraint_set.fields.validation_tests
    confidence: high
    canonical_cognee_edge: true
    logistics_only: true
    canonical_edge_type: INCLUDES_VALIDATION_TEST
    inverse_edge_type: INCLUDED_IN_CONSTRAINT_SET
    materialize_inverse: false
    edge_class: canonical
    source_type: execution_constraint_set
    target_type: validation_test
```

```yaml
candidate_edge:
  edge_id: edge.execution_constraint_set.shiprocket_guardrails.includes_validation_test.validation_test.logistics.low_confidence_requires_warning
  edge_type: INCLUDES_VALIDATION_TEST
  source: execution_constraint_set.shiprocket_guardrails
  target: validation_test.logistics.low_confidence_requires_warning
  fields:
    edge_family: execution_guidance
    evidence_basis: execution_constraint_set.fields.validation_tests
    confidence: high
    canonical_cognee_edge: true
    logistics_only: true
    canonical_edge_type: INCLUDES_VALIDATION_TEST
    inverse_edge_type: INCLUDED_IN_CONSTRAINT_SET
    materialize_inverse: false
    edge_class: canonical
    source_type: execution_constraint_set
    target_type: validation_test
```

```yaml
candidate_edge:
  edge_id: edge.execution_constraint_set.shiprocket_guardrails.includes_validation_test.validation_test.logistics.fallback_sources_explicit_only
  edge_type: INCLUDES_VALIDATION_TEST
  source: execution_constraint_set.shiprocket_guardrails
  target: validation_test.logistics.fallback_sources_explicit_only
  fields:
    edge_family: execution_guidance
    evidence_basis: execution_constraint_set.fields.validation_tests
    confidence: high
    canonical_cognee_edge: true
    logistics_only: true
    canonical_edge_type: INCLUDES_VALIDATION_TEST
    inverse_edge_type: INCLUDED_IN_CONSTRAINT_SET
    materialize_inverse: false
    edge_class: canonical
    source_type: execution_constraint_set
    target_type: validation_test
```

```yaml
candidate_edge:
  edge_id: edge.execution_constraint_set.shiprocket_guardrails.includes_validation_test.validation_test.logistics.awb_primary_reconciliation_unit
  edge_type: INCLUDES_VALIDATION_TEST
  source: execution_constraint_set.shiprocket_guardrails
  target: validation_test.logistics.awb_primary_reconciliation_unit
  fields:
    edge_family: execution_guidance
    evidence_basis: execution_constraint_set.fields.validation_tests
    confidence: high
    canonical_cognee_edge: true
    logistics_only: true
    canonical_edge_type: INCLUDES_VALIDATION_TEST
    inverse_edge_type: INCLUDED_IN_CONSTRAINT_SET
    materialize_inverse: false
    edge_class: canonical
    source_type: execution_constraint_set
    target_type: validation_test
```

```yaml
candidate_edge:
  edge_id: edge.execution_constraint_set.shiprocket_guardrails.includes_validation_test.validation_test.logistics.do_not_join_awb_to_bank_without_batch
  edge_type: INCLUDES_VALIDATION_TEST
  source: execution_constraint_set.shiprocket_guardrails
  target: validation_test.logistics.do_not_join_awb_to_bank_without_batch
  fields:
    edge_family: execution_guidance
    evidence_basis: execution_constraint_set.fields.validation_tests
    confidence: high
    canonical_cognee_edge: true
    logistics_only: true
    canonical_edge_type: INCLUDES_VALIDATION_TEST
    inverse_edge_type: INCLUDED_IN_CONSTRAINT_SET
    materialize_inverse: false
    edge_class: canonical
    source_type: execution_constraint_set
    target_type: validation_test
```

```yaml
candidate_edge:
  edge_id: edge.execution_constraint_set.shiprocket_guardrails.includes_validation_test.validation_test.logistics.preaggregate_before_order_join
  edge_type: INCLUDES_VALIDATION_TEST
  source: execution_constraint_set.shiprocket_guardrails
  target: validation_test.logistics.preaggregate_before_order_join
  fields:
    edge_family: execution_guidance
    evidence_basis: execution_constraint_set.fields.validation_tests
    confidence: high
    canonical_cognee_edge: true
    logistics_only: true
    canonical_edge_type: INCLUDES_VALIDATION_TEST
    inverse_edge_type: INCLUDED_IN_CONSTRAINT_SET
    materialize_inverse: false
    edge_class: canonical
    source_type: execution_constraint_set
    target_type: validation_test
```

```yaml
candidate_edge:
  edge_id: edge.execution_constraint_set.shiprocket_guardrails.applies_to_query_pattern.query_pattern.logistics.shiprocket_courier_partner_freight_split
  edge_type: APPLIES_TO_QUERY_PATTERN
  source: execution_constraint_set.shiprocket_guardrails
  target: query_pattern.logistics.shiprocket_courier_partner_freight_split
  fields:
    edge_family: execution_guidance
    evidence_basis: execution_constraint_set.fields.query_patterns
    confidence: high
    canonical_cognee_edge: true
    logistics_only: true
    canonical_edge_type: APPLIES_TO_QUERY_PATTERN
    inverse_edge_type: HAS_EXECUTION_CONSTRAINT_SET
    materialize_inverse: false
    edge_class: canonical
    source_type: execution_constraint_set
    target_type: query_pattern
```

```yaml
candidate_edge:
  edge_id: edge.execution_constraint_set.shiprocket_guardrails.applies_to_query_pattern.query_pattern.logistics.shiprocket_cod_by_underlying_courier
  edge_type: APPLIES_TO_QUERY_PATTERN
  source: execution_constraint_set.shiprocket_guardrails
  target: query_pattern.logistics.shiprocket_cod_by_underlying_courier
  fields:
    edge_family: execution_guidance
    evidence_basis: execution_constraint_set.fields.query_patterns
    confidence: high
    canonical_cognee_edge: true
    logistics_only: true
    canonical_edge_type: APPLIES_TO_QUERY_PATTERN
    inverse_edge_type: HAS_EXECUTION_CONSTRAINT_SET
    materialize_inverse: false
    edge_class: canonical
    source_type: execution_constraint_set
    target_type: query_pattern
```

```yaml
candidate_edge:
  edge_id: edge.execution_constraint_set.delhivery_guardrails.includes_rule.rule.logistics.required_scope_context
  edge_type: INCLUDES_RULE
  source: execution_constraint_set.delhivery_guardrails
  target: rule.logistics.required_scope_context
  fields:
    edge_family: execution_guidance
    evidence_basis: execution_constraint_set.fields.rules
    confidence: high
    canonical_cognee_edge: true
    logistics_only: true
    canonical_edge_type: INCLUDES_RULE
    inverse_edge_type: INCLUDED_IN_CONSTRAINT_SET
    materialize_inverse: false
    edge_class: canonical
    source_type: execution_constraint_set
    target_type: rule
```

```yaml
candidate_edge:
  edge_id: edge.execution_constraint_set.delhivery_guardrails.includes_rule.rule.logistics.business_flow_binding_required_for_cross_platform
  edge_type: INCLUDES_RULE
  source: execution_constraint_set.delhivery_guardrails
  target: rule.logistics.business_flow_binding_required_for_cross_platform
  fields:
    edge_family: execution_guidance
    evidence_basis: execution_constraint_set.fields.rules
    confidence: high
    canonical_cognee_edge: true
    logistics_only: true
    canonical_edge_type: INCLUDES_RULE
    inverse_edge_type: INCLUDED_IN_CONSTRAINT_SET
    materialize_inverse: false
    edge_class: canonical
    source_type: execution_constraint_set
    target_type: rule
```

```yaml
candidate_edge:
  edge_id: edge.execution_constraint_set.delhivery_guardrails.includes_rule.rule.logistics.do_not_create_bfb_from_generic_vendor_doc
  edge_type: INCLUDES_RULE
  source: execution_constraint_set.delhivery_guardrails
  target: rule.logistics.do_not_create_bfb_from_generic_vendor_doc
  fields:
    edge_family: execution_guidance
    evidence_basis: execution_constraint_set.fields.rules
    confidence: high
    canonical_cognee_edge: true
    logistics_only: true
    canonical_edge_type: INCLUDES_RULE
    inverse_edge_type: INCLUDED_IN_CONSTRAINT_SET
    materialize_inverse: false
    edge_class: canonical
    source_type: execution_constraint_set
    target_type: rule
```

```yaml
candidate_edge:
  edge_id: edge.execution_constraint_set.delhivery_guardrails.includes_rule.rule.logistics.amount_semantics_not_by_name
  edge_type: INCLUDES_RULE
  source: execution_constraint_set.delhivery_guardrails
  target: rule.logistics.amount_semantics_not_by_name
  fields:
    edge_family: execution_guidance
    evidence_basis: execution_constraint_set.fields.rules
    confidence: high
    canonical_cognee_edge: true
    logistics_only: true
    canonical_edge_type: INCLUDES_RULE
    inverse_edge_type: INCLUDED_IN_CONSTRAINT_SET
    materialize_inverse: false
    edge_class: canonical
    source_type: execution_constraint_set
    target_type: rule
```

```yaml
candidate_edge:
  edge_id: edge.execution_constraint_set.delhivery_guardrails.includes_rule.rule.logistics.charged_amount_table_specific
  edge_type: INCLUDES_RULE
  source: execution_constraint_set.delhivery_guardrails
  target: rule.logistics.charged_amount_table_specific
  fields:
    edge_family: execution_guidance
    evidence_basis: execution_constraint_set.fields.rules
    confidence: high
    canonical_cognee_edge: true
    logistics_only: true
    canonical_edge_type: INCLUDES_RULE
    inverse_edge_type: INCLUDED_IN_CONSTRAINT_SET
    materialize_inverse: false
    edge_class: canonical
    source_type: execution_constraint_set
    target_type: rule
```

```yaml
candidate_edge:
  edge_id: edge.execution_constraint_set.delhivery_guardrails.includes_rule.rule.logistics.active_filter_when_available
  edge_type: INCLUDES_RULE
  source: execution_constraint_set.delhivery_guardrails
  target: rule.logistics.active_filter_when_available
  fields:
    edge_family: execution_guidance
    evidence_basis: execution_constraint_set.fields.rules
    confidence: high
    canonical_cognee_edge: true
    logistics_only: true
    canonical_edge_type: INCLUDES_RULE
    inverse_edge_type: INCLUDED_IN_CONSTRAINT_SET
    materialize_inverse: false
    edge_class: canonical
    source_type: execution_constraint_set
    target_type: rule
```

```yaml
candidate_edge:
  edge_id: edge.execution_constraint_set.delhivery_guardrails.includes_rule.rule.logistics.empty_tables_schema_only
  edge_type: INCLUDES_RULE
  source: execution_constraint_set.delhivery_guardrails
  target: rule.logistics.empty_tables_schema_only
  fields:
    edge_family: execution_guidance
    evidence_basis: execution_constraint_set.fields.rules
    confidence: high
    canonical_cognee_edge: true
    logistics_only: true
    canonical_edge_type: INCLUDES_RULE
    inverse_edge_type: INCLUDED_IN_CONSTRAINT_SET
    materialize_inverse: false
    edge_class: canonical
    source_type: execution_constraint_set
    target_type: rule
```

```yaml
candidate_edge:
  edge_id: edge.execution_constraint_set.delhivery_guardrails.includes_rule.rule.logistics.low_confidence_requires_warning
  edge_type: INCLUDES_RULE
  source: execution_constraint_set.delhivery_guardrails
  target: rule.logistics.low_confidence_requires_warning
  fields:
    edge_family: execution_guidance
    evidence_basis: execution_constraint_set.fields.rules
    confidence: high
    canonical_cognee_edge: true
    logistics_only: true
    canonical_edge_type: INCLUDES_RULE
    inverse_edge_type: INCLUDED_IN_CONSTRAINT_SET
    materialize_inverse: false
    edge_class: canonical
    source_type: execution_constraint_set
    target_type: rule
```

```yaml
candidate_edge:
  edge_id: edge.execution_constraint_set.delhivery_guardrails.includes_rule.rule.logistics.fallback_sources_explicit_only
  edge_type: INCLUDES_RULE
  source: execution_constraint_set.delhivery_guardrails
  target: rule.logistics.fallback_sources_explicit_only
  fields:
    edge_family: execution_guidance
    evidence_basis: execution_constraint_set.fields.rules
    confidence: high
    canonical_cognee_edge: true
    logistics_only: true
    canonical_edge_type: INCLUDES_RULE
    inverse_edge_type: INCLUDED_IN_CONSTRAINT_SET
    materialize_inverse: false
    edge_class: canonical
    source_type: execution_constraint_set
    target_type: rule
```

```yaml
candidate_edge:
  edge_id: edge.execution_constraint_set.delhivery_guardrails.includes_rule.rule.logistics.awb_primary_reconciliation_unit
  edge_type: INCLUDES_RULE
  source: execution_constraint_set.delhivery_guardrails
  target: rule.logistics.awb_primary_reconciliation_unit
  fields:
    edge_family: execution_guidance
    evidence_basis: execution_constraint_set.fields.rules
    confidence: high
    canonical_cognee_edge: true
    logistics_only: true
    canonical_edge_type: INCLUDES_RULE
    inverse_edge_type: INCLUDED_IN_CONSTRAINT_SET
    materialize_inverse: false
    edge_class: canonical
    source_type: execution_constraint_set
    target_type: rule
```

```yaml
candidate_edge:
  edge_id: edge.execution_constraint_set.delhivery_guardrails.includes_rule.rule.logistics.do_not_join_awb_to_bank_without_batch
  edge_type: INCLUDES_RULE
  source: execution_constraint_set.delhivery_guardrails
  target: rule.logistics.do_not_join_awb_to_bank_without_batch
  fields:
    edge_family: execution_guidance
    evidence_basis: execution_constraint_set.fields.rules
    confidence: high
    canonical_cognee_edge: true
    logistics_only: true
    canonical_edge_type: INCLUDES_RULE
    inverse_edge_type: INCLUDED_IN_CONSTRAINT_SET
    materialize_inverse: false
    edge_class: canonical
    source_type: execution_constraint_set
    target_type: rule
```

```yaml
candidate_edge:
  edge_id: edge.execution_constraint_set.delhivery_guardrails.includes_rule.rule.logistics.preaggregate_before_order_join
  edge_type: INCLUDES_RULE
  source: execution_constraint_set.delhivery_guardrails
  target: rule.logistics.preaggregate_before_order_join
  fields:
    edge_family: execution_guidance
    evidence_basis: execution_constraint_set.fields.rules
    confidence: high
    canonical_cognee_edge: true
    logistics_only: true
    canonical_edge_type: INCLUDES_RULE
    inverse_edge_type: INCLUDED_IN_CONSTRAINT_SET
    materialize_inverse: false
    edge_class: canonical
    source_type: execution_constraint_set
    target_type: rule
```

```yaml
candidate_edge:
  edge_id: edge.execution_constraint_set.delhivery_guardrails.includes_validation_test.validation_test.logistics.required_scope_context
  edge_type: INCLUDES_VALIDATION_TEST
  source: execution_constraint_set.delhivery_guardrails
  target: validation_test.logistics.required_scope_context
  fields:
    edge_family: execution_guidance
    evidence_basis: execution_constraint_set.fields.validation_tests
    confidence: high
    canonical_cognee_edge: true
    logistics_only: true
    canonical_edge_type: INCLUDES_VALIDATION_TEST
    inverse_edge_type: INCLUDED_IN_CONSTRAINT_SET
    materialize_inverse: false
    edge_class: canonical
    source_type: execution_constraint_set
    target_type: validation_test
```

```yaml
candidate_edge:
  edge_id: edge.execution_constraint_set.delhivery_guardrails.includes_validation_test.validation_test.logistics.business_flow_binding_required_for_cross_platform
  edge_type: INCLUDES_VALIDATION_TEST
  source: execution_constraint_set.delhivery_guardrails
  target: validation_test.logistics.business_flow_binding_required_for_cross_platform
  fields:
    edge_family: execution_guidance
    evidence_basis: execution_constraint_set.fields.validation_tests
    confidence: high
    canonical_cognee_edge: true
    logistics_only: true
    canonical_edge_type: INCLUDES_VALIDATION_TEST
    inverse_edge_type: INCLUDED_IN_CONSTRAINT_SET
    materialize_inverse: false
    edge_class: canonical
    source_type: execution_constraint_set
    target_type: validation_test
```

```yaml
candidate_edge:
  edge_id: edge.execution_constraint_set.delhivery_guardrails.includes_validation_test.validation_test.logistics.do_not_create_bfb_from_generic_vendor_doc
  edge_type: INCLUDES_VALIDATION_TEST
  source: execution_constraint_set.delhivery_guardrails
  target: validation_test.logistics.do_not_create_bfb_from_generic_vendor_doc
  fields:
    edge_family: execution_guidance
    evidence_basis: execution_constraint_set.fields.validation_tests
    confidence: high
    canonical_cognee_edge: true
    logistics_only: true
    canonical_edge_type: INCLUDES_VALIDATION_TEST
    inverse_edge_type: INCLUDED_IN_CONSTRAINT_SET
    materialize_inverse: false
    edge_class: canonical
    source_type: execution_constraint_set
    target_type: validation_test
```

```yaml
candidate_edge:
  edge_id: edge.execution_constraint_set.delhivery_guardrails.includes_validation_test.validation_test.logistics.amount_semantics_not_by_name
  edge_type: INCLUDES_VALIDATION_TEST
  source: execution_constraint_set.delhivery_guardrails
  target: validation_test.logistics.amount_semantics_not_by_name
  fields:
    edge_family: execution_guidance
    evidence_basis: execution_constraint_set.fields.validation_tests
    confidence: high
    canonical_cognee_edge: true
    logistics_only: true
    canonical_edge_type: INCLUDES_VALIDATION_TEST
    inverse_edge_type: INCLUDED_IN_CONSTRAINT_SET
    materialize_inverse: false
    edge_class: canonical
    source_type: execution_constraint_set
    target_type: validation_test
```

```yaml
candidate_edge:
  edge_id: edge.execution_constraint_set.delhivery_guardrails.includes_validation_test.validation_test.logistics.charged_amount_table_specific
  edge_type: INCLUDES_VALIDATION_TEST
  source: execution_constraint_set.delhivery_guardrails
  target: validation_test.logistics.charged_amount_table_specific
  fields:
    edge_family: execution_guidance
    evidence_basis: execution_constraint_set.fields.validation_tests
    confidence: high
    canonical_cognee_edge: true
    logistics_only: true
    canonical_edge_type: INCLUDES_VALIDATION_TEST
    inverse_edge_type: INCLUDED_IN_CONSTRAINT_SET
    materialize_inverse: false
    edge_class: canonical
    source_type: execution_constraint_set
    target_type: validation_test
```

```yaml
candidate_edge:
  edge_id: edge.execution_constraint_set.delhivery_guardrails.includes_validation_test.validation_test.logistics.active_filter_when_available
  edge_type: INCLUDES_VALIDATION_TEST
  source: execution_constraint_set.delhivery_guardrails
  target: validation_test.logistics.active_filter_when_available
  fields:
    edge_family: execution_guidance
    evidence_basis: execution_constraint_set.fields.validation_tests
    confidence: high
    canonical_cognee_edge: true
    logistics_only: true
    canonical_edge_type: INCLUDES_VALIDATION_TEST
    inverse_edge_type: INCLUDED_IN_CONSTRAINT_SET
    materialize_inverse: false
    edge_class: canonical
    source_type: execution_constraint_set
    target_type: validation_test
```

```yaml
candidate_edge:
  edge_id: edge.execution_constraint_set.delhivery_guardrails.includes_validation_test.validation_test.logistics.empty_tables_schema_only
  edge_type: INCLUDES_VALIDATION_TEST
  source: execution_constraint_set.delhivery_guardrails
  target: validation_test.logistics.empty_tables_schema_only
  fields:
    edge_family: execution_guidance
    evidence_basis: execution_constraint_set.fields.validation_tests
    confidence: high
    canonical_cognee_edge: true
    logistics_only: true
    canonical_edge_type: INCLUDES_VALIDATION_TEST
    inverse_edge_type: INCLUDED_IN_CONSTRAINT_SET
    materialize_inverse: false
    edge_class: canonical
    source_type: execution_constraint_set
    target_type: validation_test
```

```yaml
candidate_edge:
  edge_id: edge.execution_constraint_set.delhivery_guardrails.includes_validation_test.validation_test.logistics.low_confidence_requires_warning
  edge_type: INCLUDES_VALIDATION_TEST
  source: execution_constraint_set.delhivery_guardrails
  target: validation_test.logistics.low_confidence_requires_warning
  fields:
    edge_family: execution_guidance
    evidence_basis: execution_constraint_set.fields.validation_tests
    confidence: high
    canonical_cognee_edge: true
    logistics_only: true
    canonical_edge_type: INCLUDES_VALIDATION_TEST
    inverse_edge_type: INCLUDED_IN_CONSTRAINT_SET
    materialize_inverse: false
    edge_class: canonical
    source_type: execution_constraint_set
    target_type: validation_test
```

```yaml
candidate_edge:
  edge_id: edge.execution_constraint_set.delhivery_guardrails.includes_validation_test.validation_test.logistics.fallback_sources_explicit_only
  edge_type: INCLUDES_VALIDATION_TEST
  source: execution_constraint_set.delhivery_guardrails
  target: validation_test.logistics.fallback_sources_explicit_only
  fields:
    edge_family: execution_guidance
    evidence_basis: execution_constraint_set.fields.validation_tests
    confidence: high
    canonical_cognee_edge: true
    logistics_only: true
    canonical_edge_type: INCLUDES_VALIDATION_TEST
    inverse_edge_type: INCLUDED_IN_CONSTRAINT_SET
    materialize_inverse: false
    edge_class: canonical
    source_type: execution_constraint_set
    target_type: validation_test
```

```yaml
candidate_edge:
  edge_id: edge.execution_constraint_set.delhivery_guardrails.includes_validation_test.validation_test.logistics.awb_primary_reconciliation_unit
  edge_type: INCLUDES_VALIDATION_TEST
  source: execution_constraint_set.delhivery_guardrails
  target: validation_test.logistics.awb_primary_reconciliation_unit
  fields:
    edge_family: execution_guidance
    evidence_basis: execution_constraint_set.fields.validation_tests
    confidence: high
    canonical_cognee_edge: true
    logistics_only: true
    canonical_edge_type: INCLUDES_VALIDATION_TEST
    inverse_edge_type: INCLUDED_IN_CONSTRAINT_SET
    materialize_inverse: false
    edge_class: canonical
    source_type: execution_constraint_set
    target_type: validation_test
```

```yaml
candidate_edge:
  edge_id: edge.execution_constraint_set.delhivery_guardrails.includes_validation_test.validation_test.logistics.do_not_join_awb_to_bank_without_batch
  edge_type: INCLUDES_VALIDATION_TEST
  source: execution_constraint_set.delhivery_guardrails
  target: validation_test.logistics.do_not_join_awb_to_bank_without_batch
  fields:
    edge_family: execution_guidance
    evidence_basis: execution_constraint_set.fields.validation_tests
    confidence: high
    canonical_cognee_edge: true
    logistics_only: true
    canonical_edge_type: INCLUDES_VALIDATION_TEST
    inverse_edge_type: INCLUDED_IN_CONSTRAINT_SET
    materialize_inverse: false
    edge_class: canonical
    source_type: execution_constraint_set
    target_type: validation_test
```

```yaml
candidate_edge:
  edge_id: edge.execution_constraint_set.delhivery_guardrails.includes_validation_test.validation_test.logistics.preaggregate_before_order_join
  edge_type: INCLUDES_VALIDATION_TEST
  source: execution_constraint_set.delhivery_guardrails
  target: validation_test.logistics.preaggregate_before_order_join
  fields:
    edge_family: execution_guidance
    evidence_basis: execution_constraint_set.fields.validation_tests
    confidence: high
    canonical_cognee_edge: true
    logistics_only: true
    canonical_edge_type: INCLUDES_VALIDATION_TEST
    inverse_edge_type: INCLUDED_IN_CONSTRAINT_SET
    materialize_inverse: false
    edge_class: canonical
    source_type: execution_constraint_set
    target_type: validation_test
```

```yaml
candidate_edge:
  edge_id: edge.execution_constraint_set.delhivery_guardrails.applies_to_query_pattern.query_pattern.logistics.delhivery_freight_component_reconciliation
  edge_type: APPLIES_TO_QUERY_PATTERN
  source: execution_constraint_set.delhivery_guardrails
  target: query_pattern.logistics.delhivery_freight_component_reconciliation
  fields:
    edge_family: execution_guidance
    evidence_basis: execution_constraint_set.fields.query_patterns
    confidence: high
    canonical_cognee_edge: true
    logistics_only: true
    canonical_edge_type: APPLIES_TO_QUERY_PATTERN
    inverse_edge_type: HAS_EXECUTION_CONSTRAINT_SET
    materialize_inverse: false
    edge_class: canonical
    source_type: execution_constraint_set
    target_type: query_pattern
```

```yaml
candidate_edge:
  edge_id: edge.execution_constraint_set.delhivery_guardrails.applies_to_query_pattern.query_pattern.logistics.delhivery_cod_qr_vs_cash
  edge_type: APPLIES_TO_QUERY_PATTERN
  source: execution_constraint_set.delhivery_guardrails
  target: query_pattern.logistics.delhivery_cod_qr_vs_cash
  fields:
    edge_family: execution_guidance
    evidence_basis: execution_constraint_set.fields.query_patterns
    confidence: high
    canonical_cognee_edge: true
    logistics_only: true
    canonical_edge_type: APPLIES_TO_QUERY_PATTERN
    inverse_edge_type: HAS_EXECUTION_CONSTRAINT_SET
    materialize_inverse: false
    edge_class: canonical
    source_type: execution_constraint_set
    target_type: query_pattern
```

```yaml
candidate_edge:
  edge_id: edge.execution_constraint_set.dtdc_guardrails.includes_rule.rule.logistics.required_scope_context
  edge_type: INCLUDES_RULE
  source: execution_constraint_set.dtdc_guardrails
  target: rule.logistics.required_scope_context
  fields:
    edge_family: execution_guidance
    evidence_basis: execution_constraint_set.fields.rules
    confidence: high
    canonical_cognee_edge: true
    logistics_only: true
    canonical_edge_type: INCLUDES_RULE
    inverse_edge_type: INCLUDED_IN_CONSTRAINT_SET
    materialize_inverse: false
    edge_class: canonical
    source_type: execution_constraint_set
    target_type: rule
```

```yaml
candidate_edge:
  edge_id: edge.execution_constraint_set.dtdc_guardrails.includes_rule.rule.logistics.business_flow_binding_required_for_cross_platform
  edge_type: INCLUDES_RULE
  source: execution_constraint_set.dtdc_guardrails
  target: rule.logistics.business_flow_binding_required_for_cross_platform
  fields:
    edge_family: execution_guidance
    evidence_basis: execution_constraint_set.fields.rules
    confidence: high
    canonical_cognee_edge: true
    logistics_only: true
    canonical_edge_type: INCLUDES_RULE
    inverse_edge_type: INCLUDED_IN_CONSTRAINT_SET
    materialize_inverse: false
    edge_class: canonical
    source_type: execution_constraint_set
    target_type: rule
```

```yaml
candidate_edge:
  edge_id: edge.execution_constraint_set.dtdc_guardrails.includes_rule.rule.logistics.do_not_create_bfb_from_generic_vendor_doc
  edge_type: INCLUDES_RULE
  source: execution_constraint_set.dtdc_guardrails
  target: rule.logistics.do_not_create_bfb_from_generic_vendor_doc
  fields:
    edge_family: execution_guidance
    evidence_basis: execution_constraint_set.fields.rules
    confidence: high
    canonical_cognee_edge: true
    logistics_only: true
    canonical_edge_type: INCLUDES_RULE
    inverse_edge_type: INCLUDED_IN_CONSTRAINT_SET
    materialize_inverse: false
    edge_class: canonical
    source_type: execution_constraint_set
    target_type: rule
```

```yaml
candidate_edge:
  edge_id: edge.execution_constraint_set.dtdc_guardrails.includes_rule.rule.logistics.amount_semantics_not_by_name
  edge_type: INCLUDES_RULE
  source: execution_constraint_set.dtdc_guardrails
  target: rule.logistics.amount_semantics_not_by_name
  fields:
    edge_family: execution_guidance
    evidence_basis: execution_constraint_set.fields.rules
    confidence: high
    canonical_cognee_edge: true
    logistics_only: true
    canonical_edge_type: INCLUDES_RULE
    inverse_edge_type: INCLUDED_IN_CONSTRAINT_SET
    materialize_inverse: false
    edge_class: canonical
    source_type: execution_constraint_set
    target_type: rule
```

```yaml
candidate_edge:
  edge_id: edge.execution_constraint_set.dtdc_guardrails.includes_rule.rule.logistics.charged_amount_table_specific
  edge_type: INCLUDES_RULE
  source: execution_constraint_set.dtdc_guardrails
  target: rule.logistics.charged_amount_table_specific
  fields:
    edge_family: execution_guidance
    evidence_basis: execution_constraint_set.fields.rules
    confidence: high
    canonical_cognee_edge: true
    logistics_only: true
    canonical_edge_type: INCLUDES_RULE
    inverse_edge_type: INCLUDED_IN_CONSTRAINT_SET
    materialize_inverse: false
    edge_class: canonical
    source_type: execution_constraint_set
    target_type: rule
```

```yaml
candidate_edge:
  edge_id: edge.execution_constraint_set.dtdc_guardrails.includes_rule.rule.logistics.active_filter_when_available
  edge_type: INCLUDES_RULE
  source: execution_constraint_set.dtdc_guardrails
  target: rule.logistics.active_filter_when_available
  fields:
    edge_family: execution_guidance
    evidence_basis: execution_constraint_set.fields.rules
    confidence: high
    canonical_cognee_edge: true
    logistics_only: true
    canonical_edge_type: INCLUDES_RULE
    inverse_edge_type: INCLUDED_IN_CONSTRAINT_SET
    materialize_inverse: false
    edge_class: canonical
    source_type: execution_constraint_set
    target_type: rule
```

```yaml
candidate_edge:
  edge_id: edge.execution_constraint_set.dtdc_guardrails.includes_rule.rule.logistics.empty_tables_schema_only
  edge_type: INCLUDES_RULE
  source: execution_constraint_set.dtdc_guardrails
  target: rule.logistics.empty_tables_schema_only
  fields:
    edge_family: execution_guidance
    evidence_basis: execution_constraint_set.fields.rules
    confidence: high
    canonical_cognee_edge: true
    logistics_only: true
    canonical_edge_type: INCLUDES_RULE
    inverse_edge_type: INCLUDED_IN_CONSTRAINT_SET
    materialize_inverse: false
    edge_class: canonical
    source_type: execution_constraint_set
    target_type: rule
```

```yaml
candidate_edge:
  edge_id: edge.execution_constraint_set.dtdc_guardrails.includes_rule.rule.logistics.low_confidence_requires_warning
  edge_type: INCLUDES_RULE
  source: execution_constraint_set.dtdc_guardrails
  target: rule.logistics.low_confidence_requires_warning
  fields:
    edge_family: execution_guidance
    evidence_basis: execution_constraint_set.fields.rules
    confidence: high
    canonical_cognee_edge: true
    logistics_only: true
    canonical_edge_type: INCLUDES_RULE
    inverse_edge_type: INCLUDED_IN_CONSTRAINT_SET
    materialize_inverse: false
    edge_class: canonical
    source_type: execution_constraint_set
    target_type: rule
```

```yaml
candidate_edge:
  edge_id: edge.execution_constraint_set.dtdc_guardrails.includes_rule.rule.logistics.fallback_sources_explicit_only
  edge_type: INCLUDES_RULE
  source: execution_constraint_set.dtdc_guardrails
  target: rule.logistics.fallback_sources_explicit_only
  fields:
    edge_family: execution_guidance
    evidence_basis: execution_constraint_set.fields.rules
    confidence: high
    canonical_cognee_edge: true
    logistics_only: true
    canonical_edge_type: INCLUDES_RULE
    inverse_edge_type: INCLUDED_IN_CONSTRAINT_SET
    materialize_inverse: false
    edge_class: canonical
    source_type: execution_constraint_set
    target_type: rule
```

```yaml
candidate_edge:
  edge_id: edge.execution_constraint_set.dtdc_guardrails.includes_rule.rule.logistics.awb_primary_reconciliation_unit
  edge_type: INCLUDES_RULE
  source: execution_constraint_set.dtdc_guardrails
  target: rule.logistics.awb_primary_reconciliation_unit
  fields:
    edge_family: execution_guidance
    evidence_basis: execution_constraint_set.fields.rules
    confidence: high
    canonical_cognee_edge: true
    logistics_only: true
    canonical_edge_type: INCLUDES_RULE
    inverse_edge_type: INCLUDED_IN_CONSTRAINT_SET
    materialize_inverse: false
    edge_class: canonical
    source_type: execution_constraint_set
    target_type: rule
```

```yaml
candidate_edge:
  edge_id: edge.execution_constraint_set.dtdc_guardrails.includes_rule.rule.logistics.do_not_join_awb_to_bank_without_batch
  edge_type: INCLUDES_RULE
  source: execution_constraint_set.dtdc_guardrails
  target: rule.logistics.do_not_join_awb_to_bank_without_batch
  fields:
    edge_family: execution_guidance
    evidence_basis: execution_constraint_set.fields.rules
    confidence: high
    canonical_cognee_edge: true
    logistics_only: true
    canonical_edge_type: INCLUDES_RULE
    inverse_edge_type: INCLUDED_IN_CONSTRAINT_SET
    materialize_inverse: false
    edge_class: canonical
    source_type: execution_constraint_set
    target_type: rule
```

```yaml
candidate_edge:
  edge_id: edge.execution_constraint_set.dtdc_guardrails.includes_rule.rule.logistics.preaggregate_before_order_join
  edge_type: INCLUDES_RULE
  source: execution_constraint_set.dtdc_guardrails
  target: rule.logistics.preaggregate_before_order_join
  fields:
    edge_family: execution_guidance
    evidence_basis: execution_constraint_set.fields.rules
    confidence: high
    canonical_cognee_edge: true
    logistics_only: true
    canonical_edge_type: INCLUDES_RULE
    inverse_edge_type: INCLUDED_IN_CONSTRAINT_SET
    materialize_inverse: false
    edge_class: canonical
    source_type: execution_constraint_set
    target_type: rule
```

```yaml
candidate_edge:
  edge_id: edge.execution_constraint_set.dtdc_guardrails.includes_validation_test.validation_test.logistics.required_scope_context
  edge_type: INCLUDES_VALIDATION_TEST
  source: execution_constraint_set.dtdc_guardrails
  target: validation_test.logistics.required_scope_context
  fields:
    edge_family: execution_guidance
    evidence_basis: execution_constraint_set.fields.validation_tests
    confidence: high
    canonical_cognee_edge: true
    logistics_only: true
    canonical_edge_type: INCLUDES_VALIDATION_TEST
    inverse_edge_type: INCLUDED_IN_CONSTRAINT_SET
    materialize_inverse: false
    edge_class: canonical
    source_type: execution_constraint_set
    target_type: validation_test
```

```yaml
candidate_edge:
  edge_id: edge.execution_constraint_set.dtdc_guardrails.includes_validation_test.validation_test.logistics.business_flow_binding_required_for_cross_platform
  edge_type: INCLUDES_VALIDATION_TEST
  source: execution_constraint_set.dtdc_guardrails
  target: validation_test.logistics.business_flow_binding_required_for_cross_platform
  fields:
    edge_family: execution_guidance
    evidence_basis: execution_constraint_set.fields.validation_tests
    confidence: high
    canonical_cognee_edge: true
    logistics_only: true
    canonical_edge_type: INCLUDES_VALIDATION_TEST
    inverse_edge_type: INCLUDED_IN_CONSTRAINT_SET
    materialize_inverse: false
    edge_class: canonical
    source_type: execution_constraint_set
    target_type: validation_test
```

```yaml
candidate_edge:
  edge_id: edge.execution_constraint_set.dtdc_guardrails.includes_validation_test.validation_test.logistics.do_not_create_bfb_from_generic_vendor_doc
  edge_type: INCLUDES_VALIDATION_TEST
  source: execution_constraint_set.dtdc_guardrails
  target: validation_test.logistics.do_not_create_bfb_from_generic_vendor_doc
  fields:
    edge_family: execution_guidance
    evidence_basis: execution_constraint_set.fields.validation_tests
    confidence: high
    canonical_cognee_edge: true
    logistics_only: true
    canonical_edge_type: INCLUDES_VALIDATION_TEST
    inverse_edge_type: INCLUDED_IN_CONSTRAINT_SET
    materialize_inverse: false
    edge_class: canonical
    source_type: execution_constraint_set
    target_type: validation_test
```

```yaml
candidate_edge:
  edge_id: edge.execution_constraint_set.dtdc_guardrails.includes_validation_test.validation_test.logistics.amount_semantics_not_by_name
  edge_type: INCLUDES_VALIDATION_TEST
  source: execution_constraint_set.dtdc_guardrails
  target: validation_test.logistics.amount_semantics_not_by_name
  fields:
    edge_family: execution_guidance
    evidence_basis: execution_constraint_set.fields.validation_tests
    confidence: high
    canonical_cognee_edge: true
    logistics_only: true
    canonical_edge_type: INCLUDES_VALIDATION_TEST
    inverse_edge_type: INCLUDED_IN_CONSTRAINT_SET
    materialize_inverse: false
    edge_class: canonical
    source_type: execution_constraint_set
    target_type: validation_test
```

```yaml
candidate_edge:
  edge_id: edge.execution_constraint_set.dtdc_guardrails.includes_validation_test.validation_test.logistics.charged_amount_table_specific
  edge_type: INCLUDES_VALIDATION_TEST
  source: execution_constraint_set.dtdc_guardrails
  target: validation_test.logistics.charged_amount_table_specific
  fields:
    edge_family: execution_guidance
    evidence_basis: execution_constraint_set.fields.validation_tests
    confidence: high
    canonical_cognee_edge: true
    logistics_only: true
    canonical_edge_type: INCLUDES_VALIDATION_TEST
    inverse_edge_type: INCLUDED_IN_CONSTRAINT_SET
    materialize_inverse: false
    edge_class: canonical
    source_type: execution_constraint_set
    target_type: validation_test
```

```yaml
candidate_edge:
  edge_id: edge.execution_constraint_set.dtdc_guardrails.includes_validation_test.validation_test.logistics.active_filter_when_available
  edge_type: INCLUDES_VALIDATION_TEST
  source: execution_constraint_set.dtdc_guardrails
  target: validation_test.logistics.active_filter_when_available
  fields:
    edge_family: execution_guidance
    evidence_basis: execution_constraint_set.fields.validation_tests
    confidence: high
    canonical_cognee_edge: true
    logistics_only: true
    canonical_edge_type: INCLUDES_VALIDATION_TEST
    inverse_edge_type: INCLUDED_IN_CONSTRAINT_SET
    materialize_inverse: false
    edge_class: canonical
    source_type: execution_constraint_set
    target_type: validation_test
```

```yaml
candidate_edge:
  edge_id: edge.execution_constraint_set.dtdc_guardrails.includes_validation_test.validation_test.logistics.empty_tables_schema_only
  edge_type: INCLUDES_VALIDATION_TEST
  source: execution_constraint_set.dtdc_guardrails
  target: validation_test.logistics.empty_tables_schema_only
  fields:
    edge_family: execution_guidance
    evidence_basis: execution_constraint_set.fields.validation_tests
    confidence: high
    canonical_cognee_edge: true
    logistics_only: true
    canonical_edge_type: INCLUDES_VALIDATION_TEST
    inverse_edge_type: INCLUDED_IN_CONSTRAINT_SET
    materialize_inverse: false
    edge_class: canonical
    source_type: execution_constraint_set
    target_type: validation_test
```

```yaml
candidate_edge:
  edge_id: edge.execution_constraint_set.dtdc_guardrails.includes_validation_test.validation_test.logistics.low_confidence_requires_warning
  edge_type: INCLUDES_VALIDATION_TEST
  source: execution_constraint_set.dtdc_guardrails
  target: validation_test.logistics.low_confidence_requires_warning
  fields:
    edge_family: execution_guidance
    evidence_basis: execution_constraint_set.fields.validation_tests
    confidence: high
    canonical_cognee_edge: true
    logistics_only: true
    canonical_edge_type: INCLUDES_VALIDATION_TEST
    inverse_edge_type: INCLUDED_IN_CONSTRAINT_SET
    materialize_inverse: false
    edge_class: canonical
    source_type: execution_constraint_set
    target_type: validation_test
```

```yaml
candidate_edge:
  edge_id: edge.execution_constraint_set.dtdc_guardrails.includes_validation_test.validation_test.logistics.fallback_sources_explicit_only
  edge_type: INCLUDES_VALIDATION_TEST
  source: execution_constraint_set.dtdc_guardrails
  target: validation_test.logistics.fallback_sources_explicit_only
  fields:
    edge_family: execution_guidance
    evidence_basis: execution_constraint_set.fields.validation_tests
    confidence: high
    canonical_cognee_edge: true
    logistics_only: true
    canonical_edge_type: INCLUDES_VALIDATION_TEST
    inverse_edge_type: INCLUDED_IN_CONSTRAINT_SET
    materialize_inverse: false
    edge_class: canonical
    source_type: execution_constraint_set
    target_type: validation_test
```

```yaml
candidate_edge:
  edge_id: edge.execution_constraint_set.dtdc_guardrails.includes_validation_test.validation_test.logistics.awb_primary_reconciliation_unit
  edge_type: INCLUDES_VALIDATION_TEST
  source: execution_constraint_set.dtdc_guardrails
  target: validation_test.logistics.awb_primary_reconciliation_unit
  fields:
    edge_family: execution_guidance
    evidence_basis: execution_constraint_set.fields.validation_tests
    confidence: high
    canonical_cognee_edge: true
    logistics_only: true
    canonical_edge_type: INCLUDES_VALIDATION_TEST
    inverse_edge_type: INCLUDED_IN_CONSTRAINT_SET
    materialize_inverse: false
    edge_class: canonical
    source_type: execution_constraint_set
    target_type: validation_test
```

```yaml
candidate_edge:
  edge_id: edge.execution_constraint_set.dtdc_guardrails.includes_validation_test.validation_test.logistics.do_not_join_awb_to_bank_without_batch
  edge_type: INCLUDES_VALIDATION_TEST
  source: execution_constraint_set.dtdc_guardrails
  target: validation_test.logistics.do_not_join_awb_to_bank_without_batch
  fields:
    edge_family: execution_guidance
    evidence_basis: execution_constraint_set.fields.validation_tests
    confidence: high
    canonical_cognee_edge: true
    logistics_only: true
    canonical_edge_type: INCLUDES_VALIDATION_TEST
    inverse_edge_type: INCLUDED_IN_CONSTRAINT_SET
    materialize_inverse: false
    edge_class: canonical
    source_type: execution_constraint_set
    target_type: validation_test
```

```yaml
candidate_edge:
  edge_id: edge.execution_constraint_set.dtdc_guardrails.includes_validation_test.validation_test.logistics.preaggregate_before_order_join
  edge_type: INCLUDES_VALIDATION_TEST
  source: execution_constraint_set.dtdc_guardrails
  target: validation_test.logistics.preaggregate_before_order_join
  fields:
    edge_family: execution_guidance
    evidence_basis: execution_constraint_set.fields.validation_tests
    confidence: high
    canonical_cognee_edge: true
    logistics_only: true
    canonical_edge_type: INCLUDES_VALIDATION_TEST
    inverse_edge_type: INCLUDED_IN_CONSTRAINT_SET
    materialize_inverse: false
    edge_class: canonical
    source_type: execution_constraint_set
    target_type: validation_test
```

```yaml
candidate_edge:
  edge_id: edge.execution_constraint_set.dtdc_guardrails.applies_to_query_pattern.query_pattern.logistics.dtdc_settlement_to_shiprocket_freight_fallback
  edge_type: APPLIES_TO_QUERY_PATTERN
  source: execution_constraint_set.dtdc_guardrails
  target: query_pattern.logistics.dtdc_settlement_to_shiprocket_freight_fallback
  fields:
    edge_family: execution_guidance
    evidence_basis: execution_constraint_set.fields.query_patterns
    confidence: high
    canonical_cognee_edge: true
    logistics_only: true
    canonical_edge_type: APPLIES_TO_QUERY_PATTERN
    inverse_edge_type: HAS_EXECUTION_CONSTRAINT_SET
    materialize_inverse: false
    edge_class: canonical
    source_type: execution_constraint_set
    target_type: query_pattern
```

```yaml
candidate_edge:
  edge_id: edge.execution_constraint_set.dtdc_guardrails.applies_to_query_pattern.query_pattern.logistics.dtdc_utr_bank_bridge
  edge_type: APPLIES_TO_QUERY_PATTERN
  source: execution_constraint_set.dtdc_guardrails
  target: query_pattern.logistics.dtdc_utr_bank_bridge
  fields:
    edge_family: execution_guidance
    evidence_basis: execution_constraint_set.fields.query_patterns
    confidence: high
    canonical_cognee_edge: true
    logistics_only: true
    canonical_edge_type: APPLIES_TO_QUERY_PATTERN
    inverse_edge_type: HAS_EXECUTION_CONSTRAINT_SET
    materialize_inverse: false
    edge_class: canonical
    source_type: execution_constraint_set
    target_type: query_pattern
```

```yaml
candidate_edge:
  edge_id: edge.execution_constraint_set.ekart_guardrails.includes_rule.rule.logistics.required_scope_context
  edge_type: INCLUDES_RULE
  source: execution_constraint_set.ekart_guardrails
  target: rule.logistics.required_scope_context
  fields:
    edge_family: execution_guidance
    evidence_basis: execution_constraint_set.fields.rules
    confidence: high
    canonical_cognee_edge: true
    logistics_only: true
    canonical_edge_type: INCLUDES_RULE
    inverse_edge_type: INCLUDED_IN_CONSTRAINT_SET
    materialize_inverse: false
    edge_class: canonical
    source_type: execution_constraint_set
    target_type: rule
```

```yaml
candidate_edge:
  edge_id: edge.execution_constraint_set.ekart_guardrails.includes_rule.rule.logistics.business_flow_binding_required_for_cross_platform
  edge_type: INCLUDES_RULE
  source: execution_constraint_set.ekart_guardrails
  target: rule.logistics.business_flow_binding_required_for_cross_platform
  fields:
    edge_family: execution_guidance
    evidence_basis: execution_constraint_set.fields.rules
    confidence: high
    canonical_cognee_edge: true
    logistics_only: true
    canonical_edge_type: INCLUDES_RULE
    inverse_edge_type: INCLUDED_IN_CONSTRAINT_SET
    materialize_inverse: false
    edge_class: canonical
    source_type: execution_constraint_set
    target_type: rule
```

```yaml
candidate_edge:
  edge_id: edge.execution_constraint_set.ekart_guardrails.includes_rule.rule.logistics.do_not_create_bfb_from_generic_vendor_doc
  edge_type: INCLUDES_RULE
  source: execution_constraint_set.ekart_guardrails
  target: rule.logistics.do_not_create_bfb_from_generic_vendor_doc
  fields:
    edge_family: execution_guidance
    evidence_basis: execution_constraint_set.fields.rules
    confidence: high
    canonical_cognee_edge: true
    logistics_only: true
    canonical_edge_type: INCLUDES_RULE
    inverse_edge_type: INCLUDED_IN_CONSTRAINT_SET
    materialize_inverse: false
    edge_class: canonical
    source_type: execution_constraint_set
    target_type: rule
```

```yaml
candidate_edge:
  edge_id: edge.execution_constraint_set.ekart_guardrails.includes_rule.rule.logistics.amount_semantics_not_by_name
  edge_type: INCLUDES_RULE
  source: execution_constraint_set.ekart_guardrails
  target: rule.logistics.amount_semantics_not_by_name
  fields:
    edge_family: execution_guidance
    evidence_basis: execution_constraint_set.fields.rules
    confidence: high
    canonical_cognee_edge: true
    logistics_only: true
    canonical_edge_type: INCLUDES_RULE
    inverse_edge_type: INCLUDED_IN_CONSTRAINT_SET
    materialize_inverse: false
    edge_class: canonical
    source_type: execution_constraint_set
    target_type: rule
```

```yaml
candidate_edge:
  edge_id: edge.execution_constraint_set.ekart_guardrails.includes_rule.rule.logistics.charged_amount_table_specific
  edge_type: INCLUDES_RULE
  source: execution_constraint_set.ekart_guardrails
  target: rule.logistics.charged_amount_table_specific
  fields:
    edge_family: execution_guidance
    evidence_basis: execution_constraint_set.fields.rules
    confidence: high
    canonical_cognee_edge: true
    logistics_only: true
    canonical_edge_type: INCLUDES_RULE
    inverse_edge_type: INCLUDED_IN_CONSTRAINT_SET
    materialize_inverse: false
    edge_class: canonical
    source_type: execution_constraint_set
    target_type: rule
```

```yaml
candidate_edge:
  edge_id: edge.execution_constraint_set.ekart_guardrails.includes_rule.rule.logistics.active_filter_when_available
  edge_type: INCLUDES_RULE
  source: execution_constraint_set.ekart_guardrails
  target: rule.logistics.active_filter_when_available
  fields:
    edge_family: execution_guidance
    evidence_basis: execution_constraint_set.fields.rules
    confidence: high
    canonical_cognee_edge: true
    logistics_only: true
    canonical_edge_type: INCLUDES_RULE
    inverse_edge_type: INCLUDED_IN_CONSTRAINT_SET
    materialize_inverse: false
    edge_class: canonical
    source_type: execution_constraint_set
    target_type: rule
```

```yaml
candidate_edge:
  edge_id: edge.execution_constraint_set.ekart_guardrails.includes_rule.rule.logistics.empty_tables_schema_only
  edge_type: INCLUDES_RULE
  source: execution_constraint_set.ekart_guardrails
  target: rule.logistics.empty_tables_schema_only
  fields:
    edge_family: execution_guidance
    evidence_basis: execution_constraint_set.fields.rules
    confidence: high
    canonical_cognee_edge: true
    logistics_only: true
    canonical_edge_type: INCLUDES_RULE
    inverse_edge_type: INCLUDED_IN_CONSTRAINT_SET
    materialize_inverse: false
    edge_class: canonical
    source_type: execution_constraint_set
    target_type: rule
```

```yaml
candidate_edge:
  edge_id: edge.execution_constraint_set.ekart_guardrails.includes_rule.rule.logistics.low_confidence_requires_warning
  edge_type: INCLUDES_RULE
  source: execution_constraint_set.ekart_guardrails
  target: rule.logistics.low_confidence_requires_warning
  fields:
    edge_family: execution_guidance
    evidence_basis: execution_constraint_set.fields.rules
    confidence: high
    canonical_cognee_edge: true
    logistics_only: true
    canonical_edge_type: INCLUDES_RULE
    inverse_edge_type: INCLUDED_IN_CONSTRAINT_SET
    materialize_inverse: false
    edge_class: canonical
    source_type: execution_constraint_set
    target_type: rule
```

```yaml
candidate_edge:
  edge_id: edge.execution_constraint_set.ekart_guardrails.includes_rule.rule.logistics.fallback_sources_explicit_only
  edge_type: INCLUDES_RULE
  source: execution_constraint_set.ekart_guardrails
  target: rule.logistics.fallback_sources_explicit_only
  fields:
    edge_family: execution_guidance
    evidence_basis: execution_constraint_set.fields.rules
    confidence: high
    canonical_cognee_edge: true
    logistics_only: true
    canonical_edge_type: INCLUDES_RULE
    inverse_edge_type: INCLUDED_IN_CONSTRAINT_SET
    materialize_inverse: false
    edge_class: canonical
    source_type: execution_constraint_set
    target_type: rule
```

```yaml
candidate_edge:
  edge_id: edge.execution_constraint_set.ekart_guardrails.includes_rule.rule.logistics.awb_primary_reconciliation_unit
  edge_type: INCLUDES_RULE
  source: execution_constraint_set.ekart_guardrails
  target: rule.logistics.awb_primary_reconciliation_unit
  fields:
    edge_family: execution_guidance
    evidence_basis: execution_constraint_set.fields.rules
    confidence: high
    canonical_cognee_edge: true
    logistics_only: true
    canonical_edge_type: INCLUDES_RULE
    inverse_edge_type: INCLUDED_IN_CONSTRAINT_SET
    materialize_inverse: false
    edge_class: canonical
    source_type: execution_constraint_set
    target_type: rule
```

```yaml
candidate_edge:
  edge_id: edge.execution_constraint_set.ekart_guardrails.includes_rule.rule.logistics.do_not_join_awb_to_bank_without_batch
  edge_type: INCLUDES_RULE
  source: execution_constraint_set.ekart_guardrails
  target: rule.logistics.do_not_join_awb_to_bank_without_batch
  fields:
    edge_family: execution_guidance
    evidence_basis: execution_constraint_set.fields.rules
    confidence: high
    canonical_cognee_edge: true
    logistics_only: true
    canonical_edge_type: INCLUDES_RULE
    inverse_edge_type: INCLUDED_IN_CONSTRAINT_SET
    materialize_inverse: false
    edge_class: canonical
    source_type: execution_constraint_set
    target_type: rule
```

```yaml
candidate_edge:
  edge_id: edge.execution_constraint_set.ekart_guardrails.includes_rule.rule.logistics.preaggregate_before_order_join
  edge_type: INCLUDES_RULE
  source: execution_constraint_set.ekart_guardrails
  target: rule.logistics.preaggregate_before_order_join
  fields:
    edge_family: execution_guidance
    evidence_basis: execution_constraint_set.fields.rules
    confidence: high
    canonical_cognee_edge: true
    logistics_only: true
    canonical_edge_type: INCLUDES_RULE
    inverse_edge_type: INCLUDED_IN_CONSTRAINT_SET
    materialize_inverse: false
    edge_class: canonical
    source_type: execution_constraint_set
    target_type: rule
```

```yaml
candidate_edge:
  edge_id: edge.execution_constraint_set.ekart_guardrails.includes_validation_test.validation_test.logistics.required_scope_context
  edge_type: INCLUDES_VALIDATION_TEST
  source: execution_constraint_set.ekart_guardrails
  target: validation_test.logistics.required_scope_context
  fields:
    edge_family: execution_guidance
    evidence_basis: execution_constraint_set.fields.validation_tests
    confidence: high
    canonical_cognee_edge: true
    logistics_only: true
    canonical_edge_type: INCLUDES_VALIDATION_TEST
    inverse_edge_type: INCLUDED_IN_CONSTRAINT_SET
    materialize_inverse: false
    edge_class: canonical
    source_type: execution_constraint_set
    target_type: validation_test
```

```yaml
candidate_edge:
  edge_id: edge.execution_constraint_set.ekart_guardrails.includes_validation_test.validation_test.logistics.business_flow_binding_required_for_cross_platform
  edge_type: INCLUDES_VALIDATION_TEST
  source: execution_constraint_set.ekart_guardrails
  target: validation_test.logistics.business_flow_binding_required_for_cross_platform
  fields:
    edge_family: execution_guidance
    evidence_basis: execution_constraint_set.fields.validation_tests
    confidence: high
    canonical_cognee_edge: true
    logistics_only: true
    canonical_edge_type: INCLUDES_VALIDATION_TEST
    inverse_edge_type: INCLUDED_IN_CONSTRAINT_SET
    materialize_inverse: false
    edge_class: canonical
    source_type: execution_constraint_set
    target_type: validation_test
```

```yaml
candidate_edge:
  edge_id: edge.execution_constraint_set.ekart_guardrails.includes_validation_test.validation_test.logistics.do_not_create_bfb_from_generic_vendor_doc
  edge_type: INCLUDES_VALIDATION_TEST
  source: execution_constraint_set.ekart_guardrails
  target: validation_test.logistics.do_not_create_bfb_from_generic_vendor_doc
  fields:
    edge_family: execution_guidance
    evidence_basis: execution_constraint_set.fields.validation_tests
    confidence: high
    canonical_cognee_edge: true
    logistics_only: true
    canonical_edge_type: INCLUDES_VALIDATION_TEST
    inverse_edge_type: INCLUDED_IN_CONSTRAINT_SET
    materialize_inverse: false
    edge_class: canonical
    source_type: execution_constraint_set
    target_type: validation_test
```

```yaml
candidate_edge:
  edge_id: edge.execution_constraint_set.ekart_guardrails.includes_validation_test.validation_test.logistics.amount_semantics_not_by_name
  edge_type: INCLUDES_VALIDATION_TEST
  source: execution_constraint_set.ekart_guardrails
  target: validation_test.logistics.amount_semantics_not_by_name
  fields:
    edge_family: execution_guidance
    evidence_basis: execution_constraint_set.fields.validation_tests
    confidence: high
    canonical_cognee_edge: true
    logistics_only: true
    canonical_edge_type: INCLUDES_VALIDATION_TEST
    inverse_edge_type: INCLUDED_IN_CONSTRAINT_SET
    materialize_inverse: false
    edge_class: canonical
    source_type: execution_constraint_set
    target_type: validation_test
```

```yaml
candidate_edge:
  edge_id: edge.execution_constraint_set.ekart_guardrails.includes_validation_test.validation_test.logistics.charged_amount_table_specific
  edge_type: INCLUDES_VALIDATION_TEST
  source: execution_constraint_set.ekart_guardrails
  target: validation_test.logistics.charged_amount_table_specific
  fields:
    edge_family: execution_guidance
    evidence_basis: execution_constraint_set.fields.validation_tests
    confidence: high
    canonical_cognee_edge: true
    logistics_only: true
    canonical_edge_type: INCLUDES_VALIDATION_TEST
    inverse_edge_type: INCLUDED_IN_CONSTRAINT_SET
    materialize_inverse: false
    edge_class: canonical
    source_type: execution_constraint_set
    target_type: validation_test
```

```yaml
candidate_edge:
  edge_id: edge.execution_constraint_set.ekart_guardrails.includes_validation_test.validation_test.logistics.active_filter_when_available
  edge_type: INCLUDES_VALIDATION_TEST
  source: execution_constraint_set.ekart_guardrails
  target: validation_test.logistics.active_filter_when_available
  fields:
    edge_family: execution_guidance
    evidence_basis: execution_constraint_set.fields.validation_tests
    confidence: high
    canonical_cognee_edge: true
    logistics_only: true
    canonical_edge_type: INCLUDES_VALIDATION_TEST
    inverse_edge_type: INCLUDED_IN_CONSTRAINT_SET
    materialize_inverse: false
    edge_class: canonical
    source_type: execution_constraint_set
    target_type: validation_test
```

```yaml
candidate_edge:
  edge_id: edge.execution_constraint_set.ekart_guardrails.includes_validation_test.validation_test.logistics.empty_tables_schema_only
  edge_type: INCLUDES_VALIDATION_TEST
  source: execution_constraint_set.ekart_guardrails
  target: validation_test.logistics.empty_tables_schema_only
  fields:
    edge_family: execution_guidance
    evidence_basis: execution_constraint_set.fields.validation_tests
    confidence: high
    canonical_cognee_edge: true
    logistics_only: true
    canonical_edge_type: INCLUDES_VALIDATION_TEST
    inverse_edge_type: INCLUDED_IN_CONSTRAINT_SET
    materialize_inverse: false
    edge_class: canonical
    source_type: execution_constraint_set
    target_type: validation_test
```

```yaml
candidate_edge:
  edge_id: edge.execution_constraint_set.ekart_guardrails.includes_validation_test.validation_test.logistics.low_confidence_requires_warning
  edge_type: INCLUDES_VALIDATION_TEST
  source: execution_constraint_set.ekart_guardrails
  target: validation_test.logistics.low_confidence_requires_warning
  fields:
    edge_family: execution_guidance
    evidence_basis: execution_constraint_set.fields.validation_tests
    confidence: high
    canonical_cognee_edge: true
    logistics_only: true
    canonical_edge_type: INCLUDES_VALIDATION_TEST
    inverse_edge_type: INCLUDED_IN_CONSTRAINT_SET
    materialize_inverse: false
    edge_class: canonical
    source_type: execution_constraint_set
    target_type: validation_test
```

```yaml
candidate_edge:
  edge_id: edge.execution_constraint_set.ekart_guardrails.includes_validation_test.validation_test.logistics.fallback_sources_explicit_only
  edge_type: INCLUDES_VALIDATION_TEST
  source: execution_constraint_set.ekart_guardrails
  target: validation_test.logistics.fallback_sources_explicit_only
  fields:
    edge_family: execution_guidance
    evidence_basis: execution_constraint_set.fields.validation_tests
    confidence: high
    canonical_cognee_edge: true
    logistics_only: true
    canonical_edge_type: INCLUDES_VALIDATION_TEST
    inverse_edge_type: INCLUDED_IN_CONSTRAINT_SET
    materialize_inverse: false
    edge_class: canonical
    source_type: execution_constraint_set
    target_type: validation_test
```

```yaml
candidate_edge:
  edge_id: edge.execution_constraint_set.ekart_guardrails.includes_validation_test.validation_test.logistics.awb_primary_reconciliation_unit
  edge_type: INCLUDES_VALIDATION_TEST
  source: execution_constraint_set.ekart_guardrails
  target: validation_test.logistics.awb_primary_reconciliation_unit
  fields:
    edge_family: execution_guidance
    evidence_basis: execution_constraint_set.fields.validation_tests
    confidence: high
    canonical_cognee_edge: true
    logistics_only: true
    canonical_edge_type: INCLUDES_VALIDATION_TEST
    inverse_edge_type: INCLUDED_IN_CONSTRAINT_SET
    materialize_inverse: false
    edge_class: canonical
    source_type: execution_constraint_set
    target_type: validation_test
```

```yaml
candidate_edge:
  edge_id: edge.execution_constraint_set.ekart_guardrails.includes_validation_test.validation_test.logistics.do_not_join_awb_to_bank_without_batch
  edge_type: INCLUDES_VALIDATION_TEST
  source: execution_constraint_set.ekart_guardrails
  target: validation_test.logistics.do_not_join_awb_to_bank_without_batch
  fields:
    edge_family: execution_guidance
    evidence_basis: execution_constraint_set.fields.validation_tests
    confidence: high
    canonical_cognee_edge: true
    logistics_only: true
    canonical_edge_type: INCLUDES_VALIDATION_TEST
    inverse_edge_type: INCLUDED_IN_CONSTRAINT_SET
    materialize_inverse: false
    edge_class: canonical
    source_type: execution_constraint_set
    target_type: validation_test
```

```yaml
candidate_edge:
  edge_id: edge.execution_constraint_set.ekart_guardrails.includes_validation_test.validation_test.logistics.preaggregate_before_order_join
  edge_type: INCLUDES_VALIDATION_TEST
  source: execution_constraint_set.ekart_guardrails
  target: validation_test.logistics.preaggregate_before_order_join
  fields:
    edge_family: execution_guidance
    evidence_basis: execution_constraint_set.fields.validation_tests
    confidence: high
    canonical_cognee_edge: true
    logistics_only: true
    canonical_edge_type: INCLUDES_VALIDATION_TEST
    inverse_edge_type: INCLUDED_IN_CONSTRAINT_SET
    materialize_inverse: false
    edge_class: canonical
    source_type: execution_constraint_set
    target_type: validation_test
```

```yaml
candidate_edge:
  edge_id: edge.execution_constraint_set.ekart_guardrails.applies_to_query_pattern.query_pattern.logistics.ekart_cod_pos_split
  edge_type: APPLIES_TO_QUERY_PATTERN
  source: execution_constraint_set.ekart_guardrails
  target: query_pattern.logistics.ekart_cod_pos_split
  fields:
    edge_family: execution_guidance
    evidence_basis: execution_constraint_set.fields.query_patterns
    confidence: high
    canonical_cognee_edge: true
    logistics_only: true
    canonical_edge_type: APPLIES_TO_QUERY_PATTERN
    inverse_edge_type: HAS_EXECUTION_CONSTRAINT_SET
    materialize_inverse: false
    edge_class: canonical
    source_type: execution_constraint_set
    target_type: query_pattern
```

```yaml
candidate_edge:
  edge_id: edge.execution_constraint_set.ekart_guardrails.applies_to_query_pattern.query_pattern.logistics.ekart_batch_deduplicated_bank_bridge
  edge_type: APPLIES_TO_QUERY_PATTERN
  source: execution_constraint_set.ekart_guardrails
  target: query_pattern.logistics.ekart_batch_deduplicated_bank_bridge
  fields:
    edge_family: execution_guidance
    evidence_basis: execution_constraint_set.fields.query_patterns
    confidence: high
    canonical_cognee_edge: true
    logistics_only: true
    canonical_edge_type: APPLIES_TO_QUERY_PATTERN
    inverse_edge_type: HAS_EXECUTION_CONSTRAINT_SET
    materialize_inverse: false
    edge_class: canonical
    source_type: execution_constraint_set
    target_type: query_pattern
```

```yaml
candidate_edge:
  edge_id: edge.execution_constraint_set.xpressbees_low_confidence_guardrails.includes_rule.rule.logistics.required_scope_context
  edge_type: INCLUDES_RULE
  source: execution_constraint_set.xpressbees_low_confidence_guardrails
  target: rule.logistics.required_scope_context
  fields:
    edge_family: execution_guidance
    evidence_basis: execution_constraint_set.fields.rules
    confidence: high
    canonical_cognee_edge: true
    logistics_only: true
    canonical_edge_type: INCLUDES_RULE
    inverse_edge_type: INCLUDED_IN_CONSTRAINT_SET
    materialize_inverse: false
    edge_class: canonical
    source_type: execution_constraint_set
    target_type: rule
```

```yaml
candidate_edge:
  edge_id: edge.execution_constraint_set.xpressbees_low_confidence_guardrails.includes_rule.rule.logistics.business_flow_binding_required_for_cross_platform
  edge_type: INCLUDES_RULE
  source: execution_constraint_set.xpressbees_low_confidence_guardrails
  target: rule.logistics.business_flow_binding_required_for_cross_platform
  fields:
    edge_family: execution_guidance
    evidence_basis: execution_constraint_set.fields.rules
    confidence: high
    canonical_cognee_edge: true
    logistics_only: true
    canonical_edge_type: INCLUDES_RULE
    inverse_edge_type: INCLUDED_IN_CONSTRAINT_SET
    materialize_inverse: false
    edge_class: canonical
    source_type: execution_constraint_set
    target_type: rule
```

```yaml
candidate_edge:
  edge_id: edge.execution_constraint_set.xpressbees_low_confidence_guardrails.includes_rule.rule.logistics.do_not_create_bfb_from_generic_vendor_doc
  edge_type: INCLUDES_RULE
  source: execution_constraint_set.xpressbees_low_confidence_guardrails
  target: rule.logistics.do_not_create_bfb_from_generic_vendor_doc
  fields:
    edge_family: execution_guidance
    evidence_basis: execution_constraint_set.fields.rules
    confidence: high
    canonical_cognee_edge: true
    logistics_only: true
    canonical_edge_type: INCLUDES_RULE
    inverse_edge_type: INCLUDED_IN_CONSTRAINT_SET
    materialize_inverse: false
    edge_class: canonical
    source_type: execution_constraint_set
    target_type: rule
```

```yaml
candidate_edge:
  edge_id: edge.execution_constraint_set.xpressbees_low_confidence_guardrails.includes_rule.rule.logistics.amount_semantics_not_by_name
  edge_type: INCLUDES_RULE
  source: execution_constraint_set.xpressbees_low_confidence_guardrails
  target: rule.logistics.amount_semantics_not_by_name
  fields:
    edge_family: execution_guidance
    evidence_basis: execution_constraint_set.fields.rules
    confidence: high
    canonical_cognee_edge: true
    logistics_only: true
    canonical_edge_type: INCLUDES_RULE
    inverse_edge_type: INCLUDED_IN_CONSTRAINT_SET
    materialize_inverse: false
    edge_class: canonical
    source_type: execution_constraint_set
    target_type: rule
```

```yaml
candidate_edge:
  edge_id: edge.execution_constraint_set.xpressbees_low_confidence_guardrails.includes_rule.rule.logistics.charged_amount_table_specific
  edge_type: INCLUDES_RULE
  source: execution_constraint_set.xpressbees_low_confidence_guardrails
  target: rule.logistics.charged_amount_table_specific
  fields:
    edge_family: execution_guidance
    evidence_basis: execution_constraint_set.fields.rules
    confidence: high
    canonical_cognee_edge: true
    logistics_only: true
    canonical_edge_type: INCLUDES_RULE
    inverse_edge_type: INCLUDED_IN_CONSTRAINT_SET
    materialize_inverse: false
    edge_class: canonical
    source_type: execution_constraint_set
    target_type: rule
```

```yaml
candidate_edge:
  edge_id: edge.execution_constraint_set.xpressbees_low_confidence_guardrails.includes_rule.rule.logistics.active_filter_when_available
  edge_type: INCLUDES_RULE
  source: execution_constraint_set.xpressbees_low_confidence_guardrails
  target: rule.logistics.active_filter_when_available
  fields:
    edge_family: execution_guidance
    evidence_basis: execution_constraint_set.fields.rules
    confidence: high
    canonical_cognee_edge: true
    logistics_only: true
    canonical_edge_type: INCLUDES_RULE
    inverse_edge_type: INCLUDED_IN_CONSTRAINT_SET
    materialize_inverse: false
    edge_class: canonical
    source_type: execution_constraint_set
    target_type: rule
```

```yaml
candidate_edge:
  edge_id: edge.execution_constraint_set.xpressbees_low_confidence_guardrails.includes_rule.rule.logistics.empty_tables_schema_only
  edge_type: INCLUDES_RULE
  source: execution_constraint_set.xpressbees_low_confidence_guardrails
  target: rule.logistics.empty_tables_schema_only
  fields:
    edge_family: execution_guidance
    evidence_basis: execution_constraint_set.fields.rules
    confidence: high
    canonical_cognee_edge: true
    logistics_only: true
    canonical_edge_type: INCLUDES_RULE
    inverse_edge_type: INCLUDED_IN_CONSTRAINT_SET
    materialize_inverse: false
    edge_class: canonical
    source_type: execution_constraint_set
    target_type: rule
```

```yaml
candidate_edge:
  edge_id: edge.execution_constraint_set.xpressbees_low_confidence_guardrails.includes_rule.rule.logistics.low_confidence_requires_warning
  edge_type: INCLUDES_RULE
  source: execution_constraint_set.xpressbees_low_confidence_guardrails
  target: rule.logistics.low_confidence_requires_warning
  fields:
    edge_family: execution_guidance
    evidence_basis: execution_constraint_set.fields.rules
    confidence: high
    canonical_cognee_edge: true
    logistics_only: true
    canonical_edge_type: INCLUDES_RULE
    inverse_edge_type: INCLUDED_IN_CONSTRAINT_SET
    materialize_inverse: false
    edge_class: canonical
    source_type: execution_constraint_set
    target_type: rule
```

```yaml
candidate_edge:
  edge_id: edge.execution_constraint_set.xpressbees_low_confidence_guardrails.includes_rule.rule.logistics.fallback_sources_explicit_only
  edge_type: INCLUDES_RULE
  source: execution_constraint_set.xpressbees_low_confidence_guardrails
  target: rule.logistics.fallback_sources_explicit_only
  fields:
    edge_family: execution_guidance
    evidence_basis: execution_constraint_set.fields.rules
    confidence: high
    canonical_cognee_edge: true
    logistics_only: true
    canonical_edge_type: INCLUDES_RULE
    inverse_edge_type: INCLUDED_IN_CONSTRAINT_SET
    materialize_inverse: false
    edge_class: canonical
    source_type: execution_constraint_set
    target_type: rule
```

```yaml
candidate_edge:
  edge_id: edge.execution_constraint_set.xpressbees_low_confidence_guardrails.includes_rule.rule.logistics.awb_primary_reconciliation_unit
  edge_type: INCLUDES_RULE
  source: execution_constraint_set.xpressbees_low_confidence_guardrails
  target: rule.logistics.awb_primary_reconciliation_unit
  fields:
    edge_family: execution_guidance
    evidence_basis: execution_constraint_set.fields.rules
    confidence: high
    canonical_cognee_edge: true
    logistics_only: true
    canonical_edge_type: INCLUDES_RULE
    inverse_edge_type: INCLUDED_IN_CONSTRAINT_SET
    materialize_inverse: false
    edge_class: canonical
    source_type: execution_constraint_set
    target_type: rule
```

```yaml
candidate_edge:
  edge_id: edge.execution_constraint_set.xpressbees_low_confidence_guardrails.includes_rule.rule.logistics.do_not_join_awb_to_bank_without_batch
  edge_type: INCLUDES_RULE
  source: execution_constraint_set.xpressbees_low_confidence_guardrails
  target: rule.logistics.do_not_join_awb_to_bank_without_batch
  fields:
    edge_family: execution_guidance
    evidence_basis: execution_constraint_set.fields.rules
    confidence: high
    canonical_cognee_edge: true
    logistics_only: true
    canonical_edge_type: INCLUDES_RULE
    inverse_edge_type: INCLUDED_IN_CONSTRAINT_SET
    materialize_inverse: false
    edge_class: canonical
    source_type: execution_constraint_set
    target_type: rule
```

```yaml
candidate_edge:
  edge_id: edge.execution_constraint_set.xpressbees_low_confidence_guardrails.includes_rule.rule.logistics.preaggregate_before_order_join
  edge_type: INCLUDES_RULE
  source: execution_constraint_set.xpressbees_low_confidence_guardrails
  target: rule.logistics.preaggregate_before_order_join
  fields:
    edge_family: execution_guidance
    evidence_basis: execution_constraint_set.fields.rules
    confidence: high
    canonical_cognee_edge: true
    logistics_only: true
    canonical_edge_type: INCLUDES_RULE
    inverse_edge_type: INCLUDED_IN_CONSTRAINT_SET
    materialize_inverse: false
    edge_class: canonical
    source_type: execution_constraint_set
    target_type: rule
```

```yaml
candidate_edge:
  edge_id: edge.execution_constraint_set.xpressbees_low_confidence_guardrails.includes_validation_test.validation_test.logistics.required_scope_context
  edge_type: INCLUDES_VALIDATION_TEST
  source: execution_constraint_set.xpressbees_low_confidence_guardrails
  target: validation_test.logistics.required_scope_context
  fields:
    edge_family: execution_guidance
    evidence_basis: execution_constraint_set.fields.validation_tests
    confidence: high
    canonical_cognee_edge: true
    logistics_only: true
    canonical_edge_type: INCLUDES_VALIDATION_TEST
    inverse_edge_type: INCLUDED_IN_CONSTRAINT_SET
    materialize_inverse: false
    edge_class: canonical
    source_type: execution_constraint_set
    target_type: validation_test
```

```yaml
candidate_edge:
  edge_id: edge.execution_constraint_set.xpressbees_low_confidence_guardrails.includes_validation_test.validation_test.logistics.business_flow_binding_required_for_cross_platform
  edge_type: INCLUDES_VALIDATION_TEST
  source: execution_constraint_set.xpressbees_low_confidence_guardrails
  target: validation_test.logistics.business_flow_binding_required_for_cross_platform
  fields:
    edge_family: execution_guidance
    evidence_basis: execution_constraint_set.fields.validation_tests
    confidence: high
    canonical_cognee_edge: true
    logistics_only: true
    canonical_edge_type: INCLUDES_VALIDATION_TEST
    inverse_edge_type: INCLUDED_IN_CONSTRAINT_SET
    materialize_inverse: false
    edge_class: canonical
    source_type: execution_constraint_set
    target_type: validation_test
```

```yaml
candidate_edge:
  edge_id: edge.execution_constraint_set.xpressbees_low_confidence_guardrails.includes_validation_test.validation_test.logistics.do_not_create_bfb_from_generic_vendor_doc
  edge_type: INCLUDES_VALIDATION_TEST
  source: execution_constraint_set.xpressbees_low_confidence_guardrails
  target: validation_test.logistics.do_not_create_bfb_from_generic_vendor_doc
  fields:
    edge_family: execution_guidance
    evidence_basis: execution_constraint_set.fields.validation_tests
    confidence: high
    canonical_cognee_edge: true
    logistics_only: true
    canonical_edge_type: INCLUDES_VALIDATION_TEST
    inverse_edge_type: INCLUDED_IN_CONSTRAINT_SET
    materialize_inverse: false
    edge_class: canonical
    source_type: execution_constraint_set
    target_type: validation_test
```

```yaml
candidate_edge:
  edge_id: edge.execution_constraint_set.xpressbees_low_confidence_guardrails.includes_validation_test.validation_test.logistics.amount_semantics_not_by_name
  edge_type: INCLUDES_VALIDATION_TEST
  source: execution_constraint_set.xpressbees_low_confidence_guardrails
  target: validation_test.logistics.amount_semantics_not_by_name
  fields:
    edge_family: execution_guidance
    evidence_basis: execution_constraint_set.fields.validation_tests
    confidence: high
    canonical_cognee_edge: true
    logistics_only: true
    canonical_edge_type: INCLUDES_VALIDATION_TEST
    inverse_edge_type: INCLUDED_IN_CONSTRAINT_SET
    materialize_inverse: false
    edge_class: canonical
    source_type: execution_constraint_set
    target_type: validation_test
```

```yaml
candidate_edge:
  edge_id: edge.execution_constraint_set.xpressbees_low_confidence_guardrails.includes_validation_test.validation_test.logistics.charged_amount_table_specific
  edge_type: INCLUDES_VALIDATION_TEST
  source: execution_constraint_set.xpressbees_low_confidence_guardrails
  target: validation_test.logistics.charged_amount_table_specific
  fields:
    edge_family: execution_guidance
    evidence_basis: execution_constraint_set.fields.validation_tests
    confidence: high
    canonical_cognee_edge: true
    logistics_only: true
    canonical_edge_type: INCLUDES_VALIDATION_TEST
    inverse_edge_type: INCLUDED_IN_CONSTRAINT_SET
    materialize_inverse: false
    edge_class: canonical
    source_type: execution_constraint_set
    target_type: validation_test
```

```yaml
candidate_edge:
  edge_id: edge.execution_constraint_set.xpressbees_low_confidence_guardrails.includes_validation_test.validation_test.logistics.active_filter_when_available
  edge_type: INCLUDES_VALIDATION_TEST
  source: execution_constraint_set.xpressbees_low_confidence_guardrails
  target: validation_test.logistics.active_filter_when_available
  fields:
    edge_family: execution_guidance
    evidence_basis: execution_constraint_set.fields.validation_tests
    confidence: high
    canonical_cognee_edge: true
    logistics_only: true
    canonical_edge_type: INCLUDES_VALIDATION_TEST
    inverse_edge_type: INCLUDED_IN_CONSTRAINT_SET
    materialize_inverse: false
    edge_class: canonical
    source_type: execution_constraint_set
    target_type: validation_test
```

```yaml
candidate_edge:
  edge_id: edge.execution_constraint_set.xpressbees_low_confidence_guardrails.includes_validation_test.validation_test.logistics.empty_tables_schema_only
  edge_type: INCLUDES_VALIDATION_TEST
  source: execution_constraint_set.xpressbees_low_confidence_guardrails
  target: validation_test.logistics.empty_tables_schema_only
  fields:
    edge_family: execution_guidance
    evidence_basis: execution_constraint_set.fields.validation_tests
    confidence: high
    canonical_cognee_edge: true
    logistics_only: true
    canonical_edge_type: INCLUDES_VALIDATION_TEST
    inverse_edge_type: INCLUDED_IN_CONSTRAINT_SET
    materialize_inverse: false
    edge_class: canonical
    source_type: execution_constraint_set
    target_type: validation_test
```

```yaml
candidate_edge:
  edge_id: edge.execution_constraint_set.xpressbees_low_confidence_guardrails.includes_validation_test.validation_test.logistics.low_confidence_requires_warning
  edge_type: INCLUDES_VALIDATION_TEST
  source: execution_constraint_set.xpressbees_low_confidence_guardrails
  target: validation_test.logistics.low_confidence_requires_warning
  fields:
    edge_family: execution_guidance
    evidence_basis: execution_constraint_set.fields.validation_tests
    confidence: high
    canonical_cognee_edge: true
    logistics_only: true
    canonical_edge_type: INCLUDES_VALIDATION_TEST
    inverse_edge_type: INCLUDED_IN_CONSTRAINT_SET
    materialize_inverse: false
    edge_class: canonical
    source_type: execution_constraint_set
    target_type: validation_test
```

```yaml
candidate_edge:
  edge_id: edge.execution_constraint_set.xpressbees_low_confidence_guardrails.includes_validation_test.validation_test.logistics.fallback_sources_explicit_only
  edge_type: INCLUDES_VALIDATION_TEST
  source: execution_constraint_set.xpressbees_low_confidence_guardrails
  target: validation_test.logistics.fallback_sources_explicit_only
  fields:
    edge_family: execution_guidance
    evidence_basis: execution_constraint_set.fields.validation_tests
    confidence: high
    canonical_cognee_edge: true
    logistics_only: true
    canonical_edge_type: INCLUDES_VALIDATION_TEST
    inverse_edge_type: INCLUDED_IN_CONSTRAINT_SET
    materialize_inverse: false
    edge_class: canonical
    source_type: execution_constraint_set
    target_type: validation_test
```

```yaml
candidate_edge:
  edge_id: edge.execution_constraint_set.xpressbees_low_confidence_guardrails.includes_validation_test.validation_test.logistics.awb_primary_reconciliation_unit
  edge_type: INCLUDES_VALIDATION_TEST
  source: execution_constraint_set.xpressbees_low_confidence_guardrails
  target: validation_test.logistics.awb_primary_reconciliation_unit
  fields:
    edge_family: execution_guidance
    evidence_basis: execution_constraint_set.fields.validation_tests
    confidence: high
    canonical_cognee_edge: true
    logistics_only: true
    canonical_edge_type: INCLUDES_VALIDATION_TEST
    inverse_edge_type: INCLUDED_IN_CONSTRAINT_SET
    materialize_inverse: false
    edge_class: canonical
    source_type: execution_constraint_set
    target_type: validation_test
```

```yaml
candidate_edge:
  edge_id: edge.execution_constraint_set.xpressbees_low_confidence_guardrails.includes_validation_test.validation_test.logistics.do_not_join_awb_to_bank_without_batch
  edge_type: INCLUDES_VALIDATION_TEST
  source: execution_constraint_set.xpressbees_low_confidence_guardrails
  target: validation_test.logistics.do_not_join_awb_to_bank_without_batch
  fields:
    edge_family: execution_guidance
    evidence_basis: execution_constraint_set.fields.validation_tests
    confidence: high
    canonical_cognee_edge: true
    logistics_only: true
    canonical_edge_type: INCLUDES_VALIDATION_TEST
    inverse_edge_type: INCLUDED_IN_CONSTRAINT_SET
    materialize_inverse: false
    edge_class: canonical
    source_type: execution_constraint_set
    target_type: validation_test
```

```yaml
candidate_edge:
  edge_id: edge.execution_constraint_set.xpressbees_low_confidence_guardrails.includes_validation_test.validation_test.logistics.preaggregate_before_order_join
  edge_type: INCLUDES_VALIDATION_TEST
  source: execution_constraint_set.xpressbees_low_confidence_guardrails
  target: validation_test.logistics.preaggregate_before_order_join
  fields:
    edge_family: execution_guidance
    evidence_basis: execution_constraint_set.fields.validation_tests
    confidence: high
    canonical_cognee_edge: true
    logistics_only: true
    canonical_edge_type: INCLUDES_VALIDATION_TEST
    inverse_edge_type: INCLUDED_IN_CONSTRAINT_SET
    materialize_inverse: false
    edge_class: canonical
    source_type: execution_constraint_set
    target_type: validation_test
```

```yaml
candidate_edge:
  edge_id: edge.execution_constraint_set.xpressbees_low_confidence_guardrails.applies_to_query_pattern.query_pattern.logistics.xpressbees_native_vs_shiprocket_fallback
  edge_type: APPLIES_TO_QUERY_PATTERN
  source: execution_constraint_set.xpressbees_low_confidence_guardrails
  target: query_pattern.logistics.xpressbees_native_vs_shiprocket_fallback
  fields:
    edge_family: execution_guidance
    evidence_basis: execution_constraint_set.fields.query_patterns
    confidence: high
    canonical_cognee_edge: true
    logistics_only: true
    canonical_edge_type: APPLIES_TO_QUERY_PATTERN
    inverse_edge_type: HAS_EXECUTION_CONSTRAINT_SET
    materialize_inverse: false
    edge_class: canonical
    source_type: execution_constraint_set
    target_type: query_pattern
```

```yaml
candidate_edge:
  edge_id: edge.execution_constraint_set.xpressbees_low_confidence_guardrails.applies_to_query_pattern.query_pattern.logistics.low_confidence_native_validation
  edge_type: APPLIES_TO_QUERY_PATTERN
  source: execution_constraint_set.xpressbees_low_confidence_guardrails
  target: query_pattern.logistics.low_confidence_native_validation
  fields:
    edge_family: execution_guidance
    evidence_basis: execution_constraint_set.fields.query_patterns
    confidence: high
    canonical_cognee_edge: true
    logistics_only: true
    canonical_edge_type: APPLIES_TO_QUERY_PATTERN
    inverse_edge_type: HAS_EXECUTION_CONSTRAINT_SET
    materialize_inverse: false
    edge_class: canonical
    source_type: execution_constraint_set
    target_type: query_pattern
```

## 6. Review Items

```yaml
review_item:
  id: review.logistics_reconciliation_patterns_parser_ready_v6_role_split.business_flow_boundary
  topic: Business Flow Binding boundary
  instruction: No Business Flow Binding, tenant, group, platform account, or account data binding cards should be emitted
    from this generic logistics document.
  severity: high
  status: open_for_ingestion_validation
```

## 7. Validation Summary

```yaml
validation_summary:
  document_id: logistics_reconciliation_patterns_parser_ready_v6_role_split
  candidate_cards: 263
  candidate_edges: 684
  card_types:
    relationship: 5
    table: 1
    column: 5
    reconciliation_profile: 7
    reconciliation_side: 14
    reconciliation_unit: 26
    matching_logic: 15
    reconciliation_variant: 7
    mismatch_category: 49
    query_pattern: 31
    rule: 44
    validation_test: 44
    output_contract: 5
    execution_constraint_set: 10
  edge_types:
    HAS_RELATIONSHIP: 10
    SOURCE_TABLE: 5
    TARGET_TABLE: 5
    USES_SOURCE_COLUMN: 5
    USES_TARGET_COLUMN: 5
    HAS_COLUMN: 5
    BELONGS_TO_TABLE: 5
    HAS_RECONCILIATION_PROFILE: 7
    SUPPORTS_PROCESS: 7
    HAS_RECONCILIATION_SIDE: 14
    BELONGS_TO_RECONCILIATION_PROFILE: 14
    USES_MATCHING_LOGIC: 7
    SUPPORTS_RECONCILIATION_PROFILE: 7
    HAS_MISMATCH_CATEGORY: 28
    PRODUCES_METRIC: 53
    USES_TABLE: 55
    REQUIRES_RULE: 61
    HAS_VALIDATION_TEST: 62
    USES_OUTPUT_CONTRACT: 31
    USES_RECONCILIATION_PROFILE: 29
    INCLUDES_RULE: 120
    INCLUDES_VALIDATION_TEST: 120
    APPLIES_TO_QUERY_PATTERN: 29
  forbidden_card_types_present: []
  parser_boundary: generic logistics reusable knowledge only
```
