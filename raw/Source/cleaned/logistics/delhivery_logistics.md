# Delhivery Logistics Knowledge — Parser Ready v6 Role-Split Manifest-Aligned Unified Edges
## 0. Document Metadata
```yaml
document_metadata:
  document_id: delhivery_logistics_parser_ready_v6_role_split
  title: Delhivery Logistics Knowledge — Parser Ready v6 Role-Split Manifest-Aligned Unified Edges
  domain: logistics
  vendor: Delhivery
  source_docx: /mnt/data/Logistics KB Doc.docx
  frame_of_reference: logistics_gold_std_canonical_card_frame_v5 plus flipkart_v8_unified_edges_style plus marketplace_cleanup_manifest_consolidated_v2
  generated_on: '2026-05-24'
  version: 6.0-role-split-manifest-aligned-unified-edges
  scope: delhivery_vendor_logistics_with_unified_edges
  logistics_only: true
  allowed_card_types:
  - column
  - metric
  - metric_implementation
  - platform
  - platform_context
  - relationship
  - table
  - value_profile
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
```yaml
source_evidence:
  id: evidence.delhivery.vendor_scope
  source_document: Logistics KB Doc.docx
  summary: 'Vendor-specific extracted evidence for delhivery: table role, coverage status, metrics, caveats, and joins.'
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


### Vendor-specific source anchors


```yaml
evidence_anchor_manifest:
  source_evidence_id: ev.delhivery.tables.invoice
  source_document: Logistics KB Doc.docx
  source_section: Tables Delhivery / Table 1 zs_observe.delhivery_invoice / Overview, Key Fields, Freight Components, Freight Calculation, Join Patterns
  evidence_type: table
  supported_semantics:
  - Delhivery direct freight invoice evidence
  - freight component amount fields such as charge_dl, charge_rto, charge_cod, charge_fsc, charge_fs, charge_fov, charge_air
  - charged_amount is declared product value, not freight
  - forward_awb_number join key
  unsupported_semantics:
  - COD remittance from invoice freight components
  allowed_card_types:
  - table
  - column
  - metric_implementation
  - relationship
  - value_profile
  - rule
```

```yaml
evidence_anchor_manifest:
  source_evidence_id: ev.delhivery.tables.settlement
  source_document: Logistics KB Doc.docx
  source_section: Tables Delhivery / Table 2 zs_observe.delhivery_settlement / Overview, Key Fields, Settlement Mechanics, Join Patterns, Data Quality Notes
  evidence_type: table
  supported_semantics:
  - Delhivery COD settlement and remittance evidence
  - waybill_num as AWB/waybill key
  - payable/UTR bridge fields where present
  - dual group-level observations as source fields only
  unsupported_semantics:
  - Account Data Binding creation from generic vendor doc
  allowed_card_types:
  - table
  - column
  - metric_implementation
  - relationship
  - value_profile
  - rule
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
  vendor: Delhivery
  source_docx: Logistics KB Doc.docx
  no_tenant_group_cards: true
  no_business_flow_binding_cards: true
  allowed_scope_fields_as_columns_only:
  - group_level_id
  - group_id
  - merchant_id
  - bank_name
  - bank_account_id
  metric_implementation_policy:
    generic_metric_cards_allowed_for_single_file_readability: true
    canonical_metric_dedupe_key: card_id
    metric_implementations_must_reference_vendor_or_fallback_table: true
    unsupported_or_indirect_coverage_must_be_explicit: true
  fallback_policy:
    indirect_only_vendors_use_fallback_sources_only_when_source_docx_says_so: true
    low_confidence_native_sources_must_emit low_confidence or fallback_preferred caveats: true
```

```yaml
metric_implementation_manifest:
  vendor: delhivery
  formula_requirements:
  - metric_id must point to an existing metric card
  - base_tables must point to existing table cards or explicitly documented fallback tables
  - required_columns must point to existing column cards unless implementation status is unsupported_empty or indirect_only
  - semantic_filters must be explicit when source values are needed, such as COD, POS, Delivered, RTO, courier_partner, or payment_mode
  - formula_sql must be executable SQL-like syntax for accepted implementations
  - amount_semantics must not be inferred from column name alone
  unsupported_status_values:
  - unsupported_empty
  - schema_only
  - indirect_only
  - low_confidence
  - fallback_preferred
```

```yaml
formula_sign_manifest:
  vendor: delhivery
  table_specific_amount_semantics: vendor_file_cards_own_exact_semantics
  global_guardrails:
  - never treat charged_amount as generic freight or COD
  - never compare product value to freight billed without explicit transformation
  - never use empty invoice tables as active invoice evidence
  - never use sparse native settlement as authoritative when fallback is documented as preferred
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
  review_id: review.delhivery_invoice.source_heading_typo
  source_manifest: evidence_anchor_manifest
  severity: low
  status: open
  applies_to:
  - table.zs_observe.delhivery_invoice
  finding: Source heading appears as zs_observe.delhivery_invoic in one section, while the table status and surrounding context use delhivery_invoice.
  deterministic_action: Keep canonical table_id as table.zs_observe.delhivery_invoice; retain typo as source-section caveat.
```


## 4. Candidate Cards

### 4.1 platform cards

```yaml
candidate_card:
  card_type: platform
  card_id: platform.delhivery
  name: Delhivery
  fields:
    name: Delhivery
    description: Delhivery logistics platform/vendor in the logistics domain.
    status: active
    confidence: curated
    source_documents:
    - Logistics KB Doc.docx
    - Cognee KB Design v4.md
    - logistics_gold_std_raw_md_frame_v3.md
    - logistics_gold_std_canonical_card_frame_v5.md
    created_by: kb_authoring_assistant
    updated_by: kb_authoring_assistant
    version: 5.0-manifest-aligned
    platform_name: Delhivery
    platform_type: courier
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
  card_id: platform_context.delhivery.in
  name: Delhivery India
  fields:
    name: Delhivery India
    description: India logistics context for Delhivery.
    status: active
    confidence: curated
    source_documents:
    - Logistics KB Doc.docx
    - Cognee KB Design v4.md
    - logistics_gold_std_raw_md_frame_v3.md
    - logistics_gold_std_canonical_card_frame_v5.md
    created_by: kb_authoring_assistant
    updated_by: kb_authoring_assistant
    version: 5.0-manifest-aligned
    platform_id: platform.delhivery
    context_name: Delhivery India
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
  card_id: table.zs_observe.delhivery_invoice
  name: Delhivery Invoice
  fields:
    name: Delhivery Invoice
    description: 'Delhivery Invoice: One row per Delhivery shipment lifecycle/billing event.'
    status: active
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
    table_name: delhivery_invoice
    full_reference: zs_observe.delhivery_invoice
    engine: Athena v3 / Trino SQL
    table_type: direct_freight_invoice
    source_platform_ids:
    - platform.delhivery
    source_platform_types:
    - logistics
    business_purpose: One row per Delhivery shipment lifecycle/billing event.
    grain: One row per Delhivery shipment lifecycle/billing event.
    grain_keys:
    - awb/order/reference as specified by columns
    date_columns:
    - see date column cards
    recommended_date_columns:
    - see metric implementations
    avoid_columns:
    - see amount semantics caveats
    structural_applicability: platform.delhivery; account filters are not defined here
    coverage_status: active
    row_count: '2880'
    period: '-'
    group_ids: '203'
    schema_coverage: curated_key_fields
    evidence_refs:
    - evidence.logistics_kb_doc
    - evidence.cognee_design_v4
    - evidence.unified_edge_scope
    scope_caveat: Observed group/account values are source data observations only. Do not create tenant, group, platform_account,
      account_data_binding, business_scope_set, or business_flow_binding cards from this generic logistics document.
```

```yaml
candidate_card:
  card_type: table
  card_id: table.zs_observe.delhivery_settlement
  name: Delhivery Settlement
  fields:
    name: Delhivery Settlement
    description: 'Delhivery Settlement: One row per Delhivery COD remittance record.'
    status: active
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
    table_name: delhivery_settlement
    full_reference: zs_observe.delhivery_settlement
    engine: Athena v3 / Trino SQL
    table_type: cod_settlement
    source_platform_ids:
    - platform.delhivery
    source_platform_types:
    - logistics
    business_purpose: One row per Delhivery COD remittance record.
    grain: One row per Delhivery COD remittance record.
    grain_keys:
    - awb/order/reference as specified by columns
    date_columns:
    - see date column cards
    recommended_date_columns:
    - see metric implementations
    avoid_columns:
    - see amount semantics caveats
    structural_applicability: platform.delhivery; account filters are not defined here
    coverage_status: active
    row_count: '2641'
    period: Jan-Dec 2025
    group_ids: 22;203
    schema_coverage: curated_key_fields
    evidence_refs:
    - evidence.logistics_kb_doc
    - evidence.cognee_design_v4
    - evidence.unified_edge_scope
    scope_caveat: Observed group/account values are source data observations only. Do not create tenant, group, platform_account,
      account_data_binding, business_scope_set, or business_flow_binding cards from this generic logistics document.
```

### 4.5 column cards

```yaml
candidate_card:
  card_type: column
  card_id: column.zs_observe.delhivery_invoice.order_id
  name: delhivery_invoice.order_id
  fields:
    name: delhivery_invoice.order_id
    description: Merchant order ID.
    status: active
    confidence: curated
    source_documents:
    - Logistics KB Doc.docx
    - Cognee KB Design v4.md
    - logistics_gold_std_raw_md_frame_v3.md
    - logistics_gold_std_canonical_card_frame_v5.md
    created_by: kb_authoring_assistant
    updated_by: kb_authoring_assistant
    version: 5.0-manifest-aligned
    table_id: table.zs_observe.delhivery_invoice
    column_name: order_id
    data_type: unknown
    semantic_roles: identifier
    business_concepts:
    - Merchant order ID.
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
  card_id: column.zs_observe.delhivery_invoice.forward_awb_number
  name: delhivery_invoice.forward_awb_number
  fields:
    name: delhivery_invoice.forward_awb_number
    description: Forward AWB number.
    status: active
    confidence: curated
    source_documents:
    - Logistics KB Doc.docx
    - Cognee KB Design v4.md
    - logistics_gold_std_raw_md_frame_v3.md
    - logistics_gold_std_canonical_card_frame_v5.md
    created_by: kb_authoring_assistant
    updated_by: kb_authoring_assistant
    version: 5.0-manifest-aligned
    table_id: table.zs_observe.delhivery_invoice
    column_name: forward_awb_number
    data_type: unknown
    semantic_roles: identifier;join_key;reconciliation_key
    business_concepts:
    - Forward AWB number.
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
  card_id: column.zs_observe.delhivery_invoice.return_awb_number
  name: delhivery_invoice.return_awb_number
  fields:
    name: delhivery_invoice.return_awb_number
    description: Return/RTO AWB number.
    status: active
    confidence: curated
    source_documents:
    - Logistics KB Doc.docx
    - Cognee KB Design v4.md
    - logistics_gold_std_raw_md_frame_v3.md
    - logistics_gold_std_canonical_card_frame_v5.md
    created_by: kb_authoring_assistant
    updated_by: kb_authoring_assistant
    version: 5.0-manifest-aligned
    table_id: table.zs_observe.delhivery_invoice
    column_name: return_awb_number
    data_type: unknown
    semantic_roles: identifier;join_key
    business_concepts:
    - Return/RTO AWB number.
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
  card_id: column.zs_observe.delhivery_invoice.transaction_type
  name: delhivery_invoice.transaction_type
  fields:
    name: delhivery_invoice.transaction_type
    description: delivered, rto, dto.
    status: active
    confidence: curated
    source_documents:
    - Logistics KB Doc.docx
    - Cognee KB Design v4.md
    - logistics_gold_std_raw_md_frame_v3.md
    - logistics_gold_std_canonical_card_frame_v5.md
    created_by: kb_authoring_assistant
    updated_by: kb_authoring_assistant
    version: 5.0-manifest-aligned
    table_id: table.zs_observe.delhivery_invoice
    column_name: transaction_type
    data_type: unknown
    semantic_roles: status;filter
    business_concepts:
    - delivered, rto, dto.
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
  card_id: column.zs_observe.delhivery_invoice.order_status
  name: delhivery_invoice.order_status
  fields:
    name: delhivery_invoice.order_status
    description: Pre-paid, COD, Pickup.
    status: active
    confidence: curated
    source_documents:
    - Logistics KB Doc.docx
    - Cognee KB Design v4.md
    - logistics_gold_std_raw_md_frame_v3.md
    - logistics_gold_std_canonical_card_frame_v5.md
    created_by: kb_authoring_assistant
    updated_by: kb_authoring_assistant
    version: 5.0-manifest-aligned
    table_id: table.zs_observe.delhivery_invoice
    column_name: order_status
    data_type: unknown
    semantic_roles: status;filter
    business_concepts:
    - Pre-paid, COD, Pickup.
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
  card_id: column.zs_observe.delhivery_invoice.invoice_number
  name: delhivery_invoice.invoice_number
  fields:
    name: delhivery_invoice.invoice_number
    description: Delhivery invoice number.
    status: active
    confidence: curated
    source_documents:
    - Logistics KB Doc.docx
    - Cognee KB Design v4.md
    - logistics_gold_std_raw_md_frame_v3.md
    - logistics_gold_std_canonical_card_frame_v5.md
    created_by: kb_authoring_assistant
    updated_by: kb_authoring_assistant
    version: 5.0-manifest-aligned
    table_id: table.zs_observe.delhivery_invoice
    column_name: invoice_number
    data_type: unknown
    semantic_roles: identifier
    business_concepts:
    - Delhivery invoice number.
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
  card_id: column.zs_observe.delhivery_invoice.charged_amount
  name: delhivery_invoice.charged_amount
  fields:
    name: delhivery_invoice.charged_amount
    description: Declared product value, not freight.
    status: active
    confidence: curated
    source_documents:
    - Logistics KB Doc.docx
    - Cognee KB Design v4.md
    - logistics_gold_std_raw_md_frame_v3.md
    - logistics_gold_std_canonical_card_frame_v5.md
    created_by: kb_authoring_assistant
    updated_by: kb_authoring_assistant
    version: 5.0-manifest-aligned
    table_id: table.zs_observe.delhivery_invoice
    column_name: charged_amount
    data_type: unknown
    semantic_roles: measure
    business_concepts:
    - Declared product value, not freight.
    default_aggregation: SUM if financial measure else none
    sign_convention: positive_or_source_specific
    amount_semantics: declared_product_value_not_freight
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
  card_id: column.zs_observe.delhivery_invoice.cod_amount
  name: delhivery_invoice.cod_amount
  fields:
    name: delhivery_invoice.cod_amount
    description: COD amount to be collected.
    status: active
    confidence: curated
    source_documents:
    - Logistics KB Doc.docx
    - Cognee KB Design v4.md
    - logistics_gold_std_raw_md_frame_v3.md
    - logistics_gold_std_canonical_card_frame_v5.md
    created_by: kb_authoring_assistant
    updated_by: kb_authoring_assistant
    version: 5.0-manifest-aligned
    table_id: table.zs_observe.delhivery_invoice
    column_name: cod_amount
    data_type: unknown
    semantic_roles: measure
    business_concepts:
    - COD amount to be collected.
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
  card_id: column.zs_observe.delhivery_invoice.order_value
  name: delhivery_invoice.order_value
  fields:
    name: delhivery_invoice.order_value
    description: Order value.
    status: active
    confidence: curated
    source_documents:
    - Logistics KB Doc.docx
    - Cognee KB Design v4.md
    - logistics_gold_std_raw_md_frame_v3.md
    - logistics_gold_std_canonical_card_frame_v5.md
    created_by: kb_authoring_assistant
    updated_by: kb_authoring_assistant
    version: 5.0-manifest-aligned
    table_id: table.zs_observe.delhivery_invoice
    column_name: order_value
    data_type: unknown
    semantic_roles: measure
    business_concepts:
    - Order value.
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
  card_id: column.zs_observe.delhivery_invoice.product_value
  name: delhivery_invoice.product_value
  fields:
    name: delhivery_invoice.product_value
    description: Product price/value.
    status: active
    confidence: curated
    source_documents:
    - Logistics KB Doc.docx
    - Cognee KB Design v4.md
    - logistics_gold_std_raw_md_frame_v3.md
    - logistics_gold_std_canonical_card_frame_v5.md
    created_by: kb_authoring_assistant
    updated_by: kb_authoring_assistant
    version: 5.0-manifest-aligned
    table_id: table.zs_observe.delhivery_invoice
    column_name: product_value
    data_type: unknown
    semantic_roles: measure
    business_concepts:
    - Product price/value.
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
  card_id: column.zs_observe.delhivery_invoice.charge_dl
  name: delhivery_invoice.charge_dl
  fields:
    name: delhivery_invoice.charge_dl
    description: Forward delivery freight charge.
    status: active
    confidence: curated
    source_documents:
    - Logistics KB Doc.docx
    - Cognee KB Design v4.md
    - logistics_gold_std_raw_md_frame_v3.md
    - logistics_gold_std_canonical_card_frame_v5.md
    created_by: kb_authoring_assistant
    updated_by: kb_authoring_assistant
    version: 5.0-manifest-aligned
    table_id: table.zs_observe.delhivery_invoice
    column_name: charge_dl
    data_type: unknown
    semantic_roles: measure
    business_concepts:
    - Forward delivery freight charge.
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
  card_id: column.zs_observe.delhivery_invoice.charge_rto
  name: delhivery_invoice.charge_rto
  fields:
    name: delhivery_invoice.charge_rto
    description: RTO freight charge.
    status: active
    confidence: curated
    source_documents:
    - Logistics KB Doc.docx
    - Cognee KB Design v4.md
    - logistics_gold_std_raw_md_frame_v3.md
    - logistics_gold_std_canonical_card_frame_v5.md
    created_by: kb_authoring_assistant
    updated_by: kb_authoring_assistant
    version: 5.0-manifest-aligned
    table_id: table.zs_observe.delhivery_invoice
    column_name: charge_rto
    data_type: unknown
    semantic_roles: measure
    business_concepts:
    - RTO freight charge.
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
  card_id: column.zs_observe.delhivery_invoice.charge_dto
  name: delhivery_invoice.charge_dto
  fields:
    name: delhivery_invoice.charge_dto
    description: DTO charge.
    status: active
    confidence: curated
    source_documents:
    - Logistics KB Doc.docx
    - Cognee KB Design v4.md
    - logistics_gold_std_raw_md_frame_v3.md
    - logistics_gold_std_canonical_card_frame_v5.md
    created_by: kb_authoring_assistant
    updated_by: kb_authoring_assistant
    version: 5.0-manifest-aligned
    table_id: table.zs_observe.delhivery_invoice
    column_name: charge_dto
    data_type: unknown
    semantic_roles: measure
    business_concepts:
    - DTO charge.
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
  card_id: column.zs_observe.delhivery_invoice.charge_cod
  name: delhivery_invoice.charge_cod
  fields:
    name: delhivery_invoice.charge_cod
    description: COD collection fee.
    status: active
    confidence: curated
    source_documents:
    - Logistics KB Doc.docx
    - Cognee KB Design v4.md
    - logistics_gold_std_raw_md_frame_v3.md
    - logistics_gold_std_canonical_card_frame_v5.md
    created_by: kb_authoring_assistant
    updated_by: kb_authoring_assistant
    version: 5.0-manifest-aligned
    table_id: table.zs_observe.delhivery_invoice
    column_name: charge_cod
    data_type: unknown
    semantic_roles: measure
    business_concepts:
    - COD collection fee.
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
  card_id: column.zs_observe.delhivery_invoice.charge_fsc
  name: delhivery_invoice.charge_fsc
  fields:
    name: delhivery_invoice.charge_fsc
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
    table_id: table.zs_observe.delhivery_invoice
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
  card_id: column.zs_observe.delhivery_invoice.charge_fs
  name: delhivery_invoice.charge_fs
  fields:
    name: delhivery_invoice.charge_fs
    description: Freight surcharge.
    status: active
    confidence: curated
    source_documents:
    - Logistics KB Doc.docx
    - Cognee KB Design v4.md
    - logistics_gold_std_raw_md_frame_v3.md
    - logistics_gold_std_canonical_card_frame_v5.md
    created_by: kb_authoring_assistant
    updated_by: kb_authoring_assistant
    version: 5.0-manifest-aligned
    table_id: table.zs_observe.delhivery_invoice
    column_name: charge_fs
    data_type: unknown
    semantic_roles: measure
    business_concepts:
    - Freight surcharge.
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
  card_id: column.zs_observe.delhivery_invoice.charge_fov
  name: delhivery_invoice.charge_fov
  fields:
    name: delhivery_invoice.charge_fov
    description: Freight-on-value insurance charge.
    status: active
    confidence: curated
    source_documents:
    - Logistics KB Doc.docx
    - Cognee KB Design v4.md
    - logistics_gold_std_raw_md_frame_v3.md
    - logistics_gold_std_canonical_card_frame_v5.md
    created_by: kb_authoring_assistant
    updated_by: kb_authoring_assistant
    version: 5.0-manifest-aligned
    table_id: table.zs_observe.delhivery_invoice
    column_name: charge_fov
    data_type: unknown
    semantic_roles: measure
    business_concepts:
    - Freight-on-value insurance charge.
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
  card_id: column.zs_observe.delhivery_invoice.charge_air
  name: delhivery_invoice.charge_air
  fields:
    name: delhivery_invoice.charge_air
    description: Air freight component.
    status: active
    confidence: curated
    source_documents:
    - Logistics KB Doc.docx
    - Cognee KB Design v4.md
    - logistics_gold_std_raw_md_frame_v3.md
    - logistics_gold_std_canonical_card_frame_v5.md
    created_by: kb_authoring_assistant
    updated_by: kb_authoring_assistant
    version: 5.0-manifest-aligned
    table_id: table.zs_observe.delhivery_invoice
    column_name: charge_air
    data_type: unknown
    semantic_roles: measure
    business_concepts:
    - Air freight component.
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
  card_id: column.zs_observe.delhivery_invoice.charge_pickup
  name: delhivery_invoice.charge_pickup
  fields:
    name: delhivery_invoice.charge_pickup
    description: Pickup charge.
    status: active
    confidence: curated
    source_documents:
    - Logistics KB Doc.docx
    - Cognee KB Design v4.md
    - logistics_gold_std_raw_md_frame_v3.md
    - logistics_gold_std_canonical_card_frame_v5.md
    created_by: kb_authoring_assistant
    updated_by: kb_authoring_assistant
    version: 5.0-manifest-aligned
    table_id: table.zs_observe.delhivery_invoice
    column_name: charge_pickup
    data_type: unknown
    semantic_roles: measure
    business_concepts:
    - Pickup charge.
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
  card_id: column.zs_observe.delhivery_invoice.charge_peak
  name: delhivery_invoice.charge_peak
  fields:
    name: delhivery_invoice.charge_peak
    description: Peak season surcharge.
    status: active
    confidence: curated
    source_documents:
    - Logistics KB Doc.docx
    - Cognee KB Design v4.md
    - logistics_gold_std_raw_md_frame_v3.md
    - logistics_gold_std_canonical_card_frame_v5.md
    created_by: kb_authoring_assistant
    updated_by: kb_authoring_assistant
    version: 5.0-manifest-aligned
    table_id: table.zs_observe.delhivery_invoice
    column_name: charge_peak
    data_type: unknown
    semantic_roles: measure
    business_concepts:
    - Peak season surcharge.
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
  card_id: column.zs_observe.delhivery_invoice.charge_reattempt
  name: delhivery_invoice.charge_reattempt
  fields:
    name: delhivery_invoice.charge_reattempt
    description: Reattempt fee.
    status: active
    confidence: curated
    source_documents:
    - Logistics KB Doc.docx
    - Cognee KB Design v4.md
    - logistics_gold_std_raw_md_frame_v3.md
    - logistics_gold_std_canonical_card_frame_v5.md
    created_by: kb_authoring_assistant
    updated_by: kb_authoring_assistant
    version: 5.0-manifest-aligned
    table_id: table.zs_observe.delhivery_invoice
    column_name: charge_reattempt
    data_type: unknown
    semantic_roles: measure
    business_concepts:
    - Reattempt fee.
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
  card_id: column.zs_observe.delhivery_invoice.charge_wod
  name: delhivery_invoice.charge_wod
  fields:
    name: delhivery_invoice.charge_wod
    description: Weekend/holiday delivery charge.
    status: active
    confidence: curated
    source_documents:
    - Logistics KB Doc.docx
    - Cognee KB Design v4.md
    - logistics_gold_std_raw_md_frame_v3.md
    - logistics_gold_std_canonical_card_frame_v5.md
    created_by: kb_authoring_assistant
    updated_by: kb_authoring_assistant
    version: 5.0-manifest-aligned
    table_id: table.zs_observe.delhivery_invoice
    column_name: charge_wod
    data_type: unknown
    semantic_roles: measure
    business_concepts:
    - Weekend/holiday delivery charge.
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
  card_id: column.zs_observe.delhivery_invoice.charged_weight
  name: delhivery_invoice.charged_weight
  fields:
    name: delhivery_invoice.charged_weight
    description: Billable weight in grams.
    status: active
    confidence: curated
    source_documents:
    - Logistics KB Doc.docx
    - Cognee KB Design v4.md
    - logistics_gold_std_raw_md_frame_v3.md
    - logistics_gold_std_canonical_card_frame_v5.md
    created_by: kb_authoring_assistant
    updated_by: kb_authoring_assistant
    version: 5.0-manifest-aligned
    table_id: table.zs_observe.delhivery_invoice
    column_name: charged_weight
    data_type: unknown
    semantic_roles: measure
    business_concepts:
    - Billable weight in grams.
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
  card_id: column.zs_observe.delhivery_invoice.zone
  name: delhivery_invoice.zone
  fields:
    name: delhivery_invoice.zone
    description: Zone A/B/C/D/E.
    status: active
    confidence: curated
    source_documents:
    - Logistics KB Doc.docx
    - Cognee KB Design v4.md
    - logistics_gold_std_raw_md_frame_v3.md
    - logistics_gold_std_canonical_card_frame_v5.md
    created_by: kb_authoring_assistant
    updated_by: kb_authoring_assistant
    version: 5.0-manifest-aligned
    table_id: table.zs_observe.delhivery_invoice
    column_name: zone
    data_type: unknown
    semantic_roles: dimension;filter
    business_concepts:
    - Zone A/B/C/D/E.
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
  card_id: column.zs_observe.delhivery_invoice.zen_vendor_payout_forward_charge
  name: delhivery_invoice.zen_vendor_payout_forward_charge
  fields:
    name: delhivery_invoice.zen_vendor_payout_forward_charge
    description: Expected forward freight payout.
    status: active
    confidence: curated
    source_documents:
    - Logistics KB Doc.docx
    - Cognee KB Design v4.md
    - logistics_gold_std_raw_md_frame_v3.md
    - logistics_gold_std_canonical_card_frame_v5.md
    created_by: kb_authoring_assistant
    updated_by: kb_authoring_assistant
    version: 5.0-manifest-aligned
    table_id: table.zs_observe.delhivery_invoice
    column_name: zen_vendor_payout_forward_charge
    data_type: unknown
    semantic_roles: measure
    business_concepts:
    - Expected forward freight payout.
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
  card_id: column.zs_observe.delhivery_invoice.zen_vendor_payout_rto_charge
  name: delhivery_invoice.zen_vendor_payout_rto_charge
  fields:
    name: delhivery_invoice.zen_vendor_payout_rto_charge
    description: Expected RTO freight payout.
    status: active
    confidence: curated
    source_documents:
    - Logistics KB Doc.docx
    - Cognee KB Design v4.md
    - logistics_gold_std_raw_md_frame_v3.md
    - logistics_gold_std_canonical_card_frame_v5.md
    created_by: kb_authoring_assistant
    updated_by: kb_authoring_assistant
    version: 5.0-manifest-aligned
    table_id: table.zs_observe.delhivery_invoice
    column_name: zen_vendor_payout_rto_charge
    data_type: unknown
    semantic_roles: measure
    business_concepts:
    - Expected RTO freight payout.
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
  card_id: column.zs_observe.delhivery_invoice.zen_vendor_payout_cod_charge
  name: delhivery_invoice.zen_vendor_payout_cod_charge
  fields:
    name: delhivery_invoice.zen_vendor_payout_cod_charge
    description: Expected COD fee payout.
    status: active
    confidence: curated
    source_documents:
    - Logistics KB Doc.docx
    - Cognee KB Design v4.md
    - logistics_gold_std_raw_md_frame_v3.md
    - logistics_gold_std_canonical_card_frame_v5.md
    created_by: kb_authoring_assistant
    updated_by: kb_authoring_assistant
    version: 5.0-manifest-aligned
    table_id: table.zs_observe.delhivery_invoice
    column_name: zen_vendor_payout_cod_charge
    data_type: unknown
    semantic_roles: measure
    business_concepts:
    - Expected COD fee payout.
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
  card_id: column.zs_observe.delhivery_invoice.zen_vendor_payout_dto_charge
  name: delhivery_invoice.zen_vendor_payout_dto_charge
  fields:
    name: delhivery_invoice.zen_vendor_payout_dto_charge
    description: Expected DTO payout.
    status: active
    confidence: curated
    source_documents:
    - Logistics KB Doc.docx
    - Cognee KB Design v4.md
    - logistics_gold_std_raw_md_frame_v3.md
    - logistics_gold_std_canonical_card_frame_v5.md
    created_by: kb_authoring_assistant
    updated_by: kb_authoring_assistant
    version: 5.0-manifest-aligned
    table_id: table.zs_observe.delhivery_invoice
    column_name: zen_vendor_payout_dto_charge
    data_type: unknown
    semantic_roles: measure
    business_concepts:
    - Expected DTO payout.
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
  card_id: column.zs_observe.delhivery_invoice.tax_cgst_amount
  name: delhivery_invoice.tax_cgst_amount
  fields:
    name: delhivery_invoice.tax_cgst_amount
    description: CGST on freight.
    status: active
    confidence: curated
    source_documents:
    - Logistics KB Doc.docx
    - Cognee KB Design v4.md
    - logistics_gold_std_raw_md_frame_v3.md
    - logistics_gold_std_canonical_card_frame_v5.md
    created_by: kb_authoring_assistant
    updated_by: kb_authoring_assistant
    version: 5.0-manifest-aligned
    table_id: table.zs_observe.delhivery_invoice
    column_name: tax_cgst_amount
    data_type: unknown
    semantic_roles: measure
    business_concepts:
    - CGST on freight.
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
  card_id: column.zs_observe.delhivery_invoice.tax_sgst_amount
  name: delhivery_invoice.tax_sgst_amount
  fields:
    name: delhivery_invoice.tax_sgst_amount
    description: SGST on freight.
    status: active
    confidence: curated
    source_documents:
    - Logistics KB Doc.docx
    - Cognee KB Design v4.md
    - logistics_gold_std_raw_md_frame_v3.md
    - logistics_gold_std_canonical_card_frame_v5.md
    created_by: kb_authoring_assistant
    updated_by: kb_authoring_assistant
    version: 5.0-manifest-aligned
    table_id: table.zs_observe.delhivery_invoice
    column_name: tax_sgst_amount
    data_type: unknown
    semantic_roles: measure
    business_concepts:
    - SGST on freight.
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
  card_id: column.zs_observe.delhivery_invoice.tax_igst_amount
  name: delhivery_invoice.tax_igst_amount
  fields:
    name: delhivery_invoice.tax_igst_amount
    description: IGST on freight.
    status: active
    confidence: curated
    source_documents:
    - Logistics KB Doc.docx
    - Cognee KB Design v4.md
    - logistics_gold_std_raw_md_frame_v3.md
    - logistics_gold_std_canonical_card_frame_v5.md
    created_by: kb_authoring_assistant
    updated_by: kb_authoring_assistant
    version: 5.0-manifest-aligned
    table_id: table.zs_observe.delhivery_invoice
    column_name: tax_igst_amount
    data_type: unknown
    semantic_roles: measure
    business_concepts:
    - IGST on freight.
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
  card_id: column.zs_observe.delhivery_invoice.is_active
  name: delhivery_invoice.is_active
  fields:
    name: delhivery_invoice.is_active
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
    table_id: table.zs_observe.delhivery_invoice
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
  card_id: column.zs_observe.delhivery_invoice.group_level_id
  name: delhivery_invoice.group_level_id
  fields:
    name: delhivery_invoice.group_level_id
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
    table_id: table.zs_observe.delhivery_invoice
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
  card_id: column.zs_observe.delhivery_settlement.order_id
  name: delhivery_settlement.order_id
  fields:
    name: delhivery_settlement.order_id
    description: Merchant order ID.
    status: active
    confidence: curated
    source_documents:
    - Logistics KB Doc.docx
    - Cognee KB Design v4.md
    - logistics_gold_std_raw_md_frame_v3.md
    - logistics_gold_std_canonical_card_frame_v5.md
    created_by: kb_authoring_assistant
    updated_by: kb_authoring_assistant
    version: 5.0-manifest-aligned
    table_id: table.zs_observe.delhivery_settlement
    column_name: order_id
    data_type: unknown
    semantic_roles: identifier
    business_concepts:
    - Merchant order ID.
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
  card_id: column.zs_observe.delhivery_settlement.waybill_num
  name: delhivery_settlement.waybill_num
  fields:
    name: delhivery_settlement.waybill_num
    description: Delhivery AWB; joins to invoice forward_awb_number.
    status: active
    confidence: curated
    source_documents:
    - Logistics KB Doc.docx
    - Cognee KB Design v4.md
    - logistics_gold_std_raw_md_frame_v3.md
    - logistics_gold_std_canonical_card_frame_v5.md
    created_by: kb_authoring_assistant
    updated_by: kb_authoring_assistant
    version: 5.0-manifest-aligned
    table_id: table.zs_observe.delhivery_settlement
    column_name: waybill_num
    data_type: unknown
    semantic_roles: identifier;join_key;reconciliation_key
    business_concepts:
    - Delhivery AWB
    - joins to invoice forward_awb_number.
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
  card_id: column.zs_observe.delhivery_settlement.waybill_number
  name: delhivery_settlement.waybill_number
  fields:
    name: delhivery_settlement.waybill_number
    description: Alternate AWB field, same as waybill_num.
    status: active
    confidence: curated
    source_documents:
    - Logistics KB Doc.docx
    - Cognee KB Design v4.md
    - logistics_gold_std_raw_md_frame_v3.md
    - logistics_gold_std_canonical_card_frame_v5.md
    created_by: kb_authoring_assistant
    updated_by: kb_authoring_assistant
    version: 5.0-manifest-aligned
    table_id: table.zs_observe.delhivery_settlement
    column_name: waybill_number
    data_type: unknown
    semantic_roles: identifier;join_key
    business_concepts:
    - Alternate AWB field, same as waybill_num.
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
  card_id: column.zs_observe.delhivery_settlement.txn_type
  name: delhivery_settlement.txn_type
  fields:
    name: delhivery_settlement.txn_type
    description: CR means credit/remittance to seller.
    status: active
    confidence: curated
    source_documents:
    - Logistics KB Doc.docx
    - Cognee KB Design v4.md
    - logistics_gold_std_raw_md_frame_v3.md
    - logistics_gold_std_canonical_card_frame_v5.md
    created_by: kb_authoring_assistant
    updated_by: kb_authoring_assistant
    version: 5.0-manifest-aligned
    table_id: table.zs_observe.delhivery_settlement
    column_name: txn_type
    data_type: unknown
    semantic_roles: status;filter
    business_concepts:
    - CR means credit/remittance to seller.
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
  card_id: column.zs_observe.delhivery_settlement.order_status
  name: delhivery_settlement.order_status
  fields:
    name: delhivery_settlement.order_status
    description: Delivered.
    status: active
    confidence: curated
    source_documents:
    - Logistics KB Doc.docx
    - Cognee KB Design v4.md
    - logistics_gold_std_raw_md_frame_v3.md
    - logistics_gold_std_canonical_card_frame_v5.md
    created_by: kb_authoring_assistant
    updated_by: kb_authoring_assistant
    version: 5.0-manifest-aligned
    table_id: table.zs_observe.delhivery_settlement
    column_name: order_status
    data_type: unknown
    semantic_roles: status
    business_concepts:
    - Delivered.
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
  card_id: column.zs_observe.delhivery_settlement.status
  name: delhivery_settlement.status
  fields:
    name: delhivery_settlement.status
    description: Delivered.
    status: active
    confidence: curated
    source_documents:
    - Logistics KB Doc.docx
    - Cognee KB Design v4.md
    - logistics_gold_std_raw_md_frame_v3.md
    - logistics_gold_std_canonical_card_frame_v5.md
    created_by: kb_authoring_assistant
    updated_by: kb_authoring_assistant
    version: 5.0-manifest-aligned
    table_id: table.zs_observe.delhivery_settlement
    column_name: status
    data_type: unknown
    semantic_roles: status
    business_concepts:
    - Delivered.
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
  card_id: column.zs_observe.delhivery_settlement.payment_mode
  name: delhivery_settlement.payment_mode
  fields:
    name: delhivery_settlement.payment_mode
    description: QR for at-door QR collection or null for cash.
    status: active
    confidence: curated
    source_documents:
    - Logistics KB Doc.docx
    - Cognee KB Design v4.md
    - logistics_gold_std_raw_md_frame_v3.md
    - logistics_gold_std_canonical_card_frame_v5.md
    created_by: kb_authoring_assistant
    updated_by: kb_authoring_assistant
    version: 5.0-manifest-aligned
    table_id: table.zs_observe.delhivery_settlement
    column_name: payment_mode
    data_type: unknown
    semantic_roles: dimension;filter
    business_concepts:
    - QR for at-door QR collection or null for cash.
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
  card_id: column.zs_observe.delhivery_settlement.charged_amount
  name: delhivery_settlement.charged_amount
  fields:
    name: delhivery_settlement.charged_amount
    description: Total COD amount for settlement.
    status: active
    confidence: curated
    source_documents:
    - Logistics KB Doc.docx
    - Cognee KB Design v4.md
    - logistics_gold_std_raw_md_frame_v3.md
    - logistics_gold_std_canonical_card_frame_v5.md
    created_by: kb_authoring_assistant
    updated_by: kb_authoring_assistant
    version: 5.0-manifest-aligned
    table_id: table.zs_observe.delhivery_settlement
    column_name: charged_amount
    data_type: unknown
    semantic_roles: measure
    business_concepts:
    - Total COD amount for settlement.
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
  card_id: column.zs_observe.delhivery_settlement.cod_amount
  name: delhivery_settlement.cod_amount
  fields:
    name: delhivery_settlement.cod_amount
    description: COD amount collected per shipment.
    status: active
    confidence: curated
    source_documents:
    - Logistics KB Doc.docx
    - Cognee KB Design v4.md
    - logistics_gold_std_raw_md_frame_v3.md
    - logistics_gold_std_canonical_card_frame_v5.md
    created_by: kb_authoring_assistant
    updated_by: kb_authoring_assistant
    version: 5.0-manifest-aligned
    table_id: table.zs_observe.delhivery_settlement
    column_name: cod_amount
    data_type: unknown
    semantic_roles: measure
    business_concepts:
    - COD amount collected per shipment.
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
  card_id: column.zs_observe.delhivery_settlement.payable
  name: delhivery_settlement.payable
  fields:
    name: delhivery_settlement.payable
    description: Net payable after deductions.
    status: active
    confidence: curated
    source_documents:
    - Logistics KB Doc.docx
    - Cognee KB Design v4.md
    - logistics_gold_std_raw_md_frame_v3.md
    - logistics_gold_std_canonical_card_frame_v5.md
    created_by: kb_authoring_assistant
    updated_by: kb_authoring_assistant
    version: 5.0-manifest-aligned
    table_id: table.zs_observe.delhivery_settlement
    column_name: payable
    data_type: unknown
    semantic_roles: measure
    business_concepts:
    - Net payable after deductions.
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
  card_id: column.zs_observe.delhivery_settlement.remittance_number
  name: delhivery_settlement.remittance_number
  fields:
    name: delhivery_settlement.remittance_number
    description: Batch remittance reference.
    status: active
    confidence: curated
    source_documents:
    - Logistics KB Doc.docx
    - Cognee KB Design v4.md
    - logistics_gold_std_raw_md_frame_v3.md
    - logistics_gold_std_canonical_card_frame_v5.md
    created_by: kb_authoring_assistant
    updated_by: kb_authoring_assistant
    version: 5.0-manifest-aligned
    table_id: table.zs_observe.delhivery_settlement
    column_name: remittance_number
    data_type: unknown
    semantic_roles: identifier
    business_concepts:
    - Batch remittance reference.
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
  card_id: column.zs_observe.delhivery_settlement.utr_no
  name: delhivery_settlement.utr_no
  fields:
    name: delhivery_settlement.utr_no
    description: Bank UTR for transfer.
    status: active
    confidence: curated
    source_documents:
    - Logistics KB Doc.docx
    - Cognee KB Design v4.md
    - logistics_gold_std_raw_md_frame_v3.md
    - logistics_gold_std_canonical_card_frame_v5.md
    created_by: kb_authoring_assistant
    updated_by: kb_authoring_assistant
    version: 5.0-manifest-aligned
    table_id: table.zs_observe.delhivery_settlement
    column_name: utr_no
    data_type: unknown
    semantic_roles: identifier;bank_bridge
    business_concepts:
    - Bank UTR for transfer.
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
  card_id: column.zs_observe.delhivery_settlement.settlement_date
  name: delhivery_settlement.settlement_date
  fields:
    name: delhivery_settlement.settlement_date
    description: Date of bank transfer/remittance.
    status: active
    confidence: curated
    source_documents:
    - Logistics KB Doc.docx
    - Cognee KB Design v4.md
    - logistics_gold_std_raw_md_frame_v3.md
    - logistics_gold_std_canonical_card_frame_v5.md
    created_by: kb_authoring_assistant
    updated_by: kb_authoring_assistant
    version: 5.0-manifest-aligned
    table_id: table.zs_observe.delhivery_settlement
    column_name: settlement_date
    data_type: unknown
    semantic_roles: date
    business_concepts:
    - Date of bank transfer/remittance.
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
  card_id: column.zs_observe.delhivery_settlement.created_date
  name: delhivery_settlement.created_date
  fields:
    name: delhivery_settlement.created_date
    description: Original order creation date.
    status: active
    confidence: curated
    source_documents:
    - Logistics KB Doc.docx
    - Cognee KB Design v4.md
    - logistics_gold_std_raw_md_frame_v3.md
    - logistics_gold_std_canonical_card_frame_v5.md
    created_by: kb_authoring_assistant
    updated_by: kb_authoring_assistant
    version: 5.0-manifest-aligned
    table_id: table.zs_observe.delhivery_settlement
    column_name: created_date
    data_type: unknown
    semantic_roles: date
    business_concepts:
    - Original order creation date.
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
  card_id: column.zs_observe.delhivery_settlement.source_city
  name: delhivery_settlement.source_city
  fields:
    name: delhivery_settlement.source_city
    description: Origin city.
    status: active
    confidence: curated
    source_documents:
    - Logistics KB Doc.docx
    - Cognee KB Design v4.md
    - logistics_gold_std_raw_md_frame_v3.md
    - logistics_gold_std_canonical_card_frame_v5.md
    created_by: kb_authoring_assistant
    updated_by: kb_authoring_assistant
    version: 5.0-manifest-aligned
    table_id: table.zs_observe.delhivery_settlement
    column_name: source_city
    data_type: unknown
    semantic_roles: dimension
    business_concepts:
    - Origin city.
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
  card_id: column.zs_observe.delhivery_settlement.destination_city
  name: delhivery_settlement.destination_city
  fields:
    name: delhivery_settlement.destination_city
    description: Destination city.
    status: active
    confidence: curated
    source_documents:
    - Logistics KB Doc.docx
    - Cognee KB Design v4.md
    - logistics_gold_std_raw_md_frame_v3.md
    - logistics_gold_std_canonical_card_frame_v5.md
    created_by: kb_authoring_assistant
    updated_by: kb_authoring_assistant
    version: 5.0-manifest-aligned
    table_id: table.zs_observe.delhivery_settlement
    column_name: destination_city
    data_type: unknown
    semantic_roles: dimension
    business_concepts:
    - Destination city.
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
  card_id: column.zs_observe.delhivery_settlement.pincode
  name: delhivery_settlement.pincode
  fields:
    name: delhivery_settlement.pincode
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
    table_id: table.zs_observe.delhivery_settlement
    column_name: pincode
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
  card_id: column.zs_observe.delhivery_settlement.destination_pin
  name: delhivery_settlement.destination_pin
  fields:
    name: delhivery_settlement.destination_pin
    description: Destination pincode alternate.
    status: active
    confidence: curated
    source_documents:
    - Logistics KB Doc.docx
    - Cognee KB Design v4.md
    - logistics_gold_std_raw_md_frame_v3.md
    - logistics_gold_std_canonical_card_frame_v5.md
    created_by: kb_authoring_assistant
    updated_by: kb_authoring_assistant
    version: 5.0-manifest-aligned
    table_id: table.zs_observe.delhivery_settlement
    column_name: destination_pin
    data_type: unknown
    semantic_roles: dimension
    business_concepts:
    - Destination pincode alternate.
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
  card_id: column.zs_observe.delhivery_settlement.is_active
  name: delhivery_settlement.is_active
  fields:
    name: delhivery_settlement.is_active
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
    table_id: table.zs_observe.delhivery_settlement
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
  card_id: column.zs_observe.delhivery_settlement.group_level_id
  name: delhivery_settlement.group_level_id
  fields:
    name: delhivery_settlement.group_level_id
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
    table_id: table.zs_observe.delhivery_settlement
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

### 4.6 relationship cards

```yaml
candidate_card:
  card_type: relationship
  card_id: relationship.delhivery_invoice.delhivery_settlement.awb
  name: delhivery_invoice to delhivery_settlement by awb
  fields:
    name: delhivery_invoice to delhivery_settlement by awb
    description: Join Delhivery direct invoice to Delhivery COD settlement.
    status: active
    confidence: curated
    source_documents:
    - Logistics KB Doc.docx
    - Cognee KB Design v4.md
    - logistics_gold_std_raw_md_frame_v3.md
    - logistics_gold_std_canonical_card_frame_v5.md
    created_by: kb_authoring_assistant
    updated_by: kb_authoring_assistant
    version: 5.0-manifest-aligned
    source_table: table.zs_observe.delhivery_invoice
    target_table: table.zs_observe.delhivery_settlement
    relationship_type: join; reconciliation_relation
    join_keys: forward_awb_number = waybill_num
    cardinality: one_to_zero_or_many
    join_type_recommendation: left_join for diagnostics; inner_join for matched-only analysis
    business_use: Join Delhivery direct invoice to Delhivery COD settlement.
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
  card_id: relationship.delhivery_invoice.shiprocket_invoice.awb_crosscheck
  name: delhivery_invoice to shiprocket_invoice by awb_crosscheck
  fields:
    name: delhivery_invoice to shiprocket_invoice by awb_crosscheck
    description: Cross-check direct Delhivery invoice with Shiprocket consolidated invoice for Delhivery AWBs.
    status: active
    confidence: curated
    source_documents:
    - Logistics KB Doc.docx
    - Cognee KB Design v4.md
    - logistics_gold_std_raw_md_frame_v3.md
    - logistics_gold_std_canonical_card_frame_v5.md
    created_by: kb_authoring_assistant
    updated_by: kb_authoring_assistant
    version: 5.0-manifest-aligned
    source_table: table.zs_observe.delhivery_invoice
    target_table: table.zs_observe.shiprocket_invoice
    relationship_type: join; reconciliation_relation
    join_keys: forward_awb_number = other_id
    cardinality: one_to_zero_or_many
    join_type_recommendation: left_join for diagnostics; inner_join for matched-only analysis
    business_use: Cross-check direct Delhivery invoice with Shiprocket consolidated invoice for Delhivery AWBs.
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
  card_id: value_profile.delhivery_invoice.transaction_type
  name: delhivery_invoice.transaction_type Value Profile
  fields:
    name: delhivery_invoice.transaction_type Value Profile
    description: Known values and meanings for delhivery_invoice.transaction_type.
    status: active
    confidence: curated
    source_documents:
    - Logistics KB Doc.docx
    - Cognee KB Design v4.md
    - logistics_gold_std_raw_md_frame_v3.md
    - logistics_gold_std_canonical_card_frame_v5.md
    created_by: kb_authoring_assistant
    updated_by: kb_authoring_assistant
    version: 5.0-manifest-aligned
    table_id: table.zs_observe.delhivery_invoice
    column_id: column.zs_observe.delhivery_invoice.transaction_type
    value_type: enum_or_enum_with_nulls
    values: delivered=Forward shipment delivered (delivered); rto=Return to origin (rto); dto=Dispatch to origin/pickup issue
      (dto)
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
  card_id: value_profile.delhivery_invoice.order_status
  name: delhivery_invoice.order_status Value Profile
  fields:
    name: delhivery_invoice.order_status Value Profile
    description: Known values and meanings for delhivery_invoice.order_status.
    status: active
    confidence: curated
    source_documents:
    - Logistics KB Doc.docx
    - Cognee KB Design v4.md
    - logistics_gold_std_raw_md_frame_v3.md
    - logistics_gold_std_canonical_card_frame_v5.md
    created_by: kb_authoring_assistant
    updated_by: kb_authoring_assistant
    version: 5.0-manifest-aligned
    table_id: table.zs_observe.delhivery_invoice
    column_id: column.zs_observe.delhivery_invoice.order_status
    value_type: enum_or_enum_with_nulls
    values: Pre-paid=Prepaid delivered or RTO context (prepaid); COD=COD delivery/RTO context (cod); Pickup=Pickup/DTO context
      (pickup)
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
  card_id: value_profile.delhivery_invoice.zone
  name: delhivery_invoice.zone Value Profile
  fields:
    name: delhivery_invoice.zone Value Profile
    description: Known values and meanings for delhivery_invoice.zone.
    status: active
    confidence: curated
    source_documents:
    - Logistics KB Doc.docx
    - Cognee KB Design v4.md
    - logistics_gold_std_raw_md_frame_v3.md
    - logistics_gold_std_canonical_card_frame_v5.md
    created_by: kb_authoring_assistant
    updated_by: kb_authoring_assistant
    version: 5.0-manifest-aligned
    table_id: table.zs_observe.delhivery_invoice
    column_id: column.zs_observe.delhivery_invoice.zone
    value_type: enum_or_enum_with_nulls
    values: A=Local zone (zone_a); B=Regional zone (zone_b); C=Mid zone (zone_c); D=Far zone (zone_d); E=Farthest zone (zone_e)
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
  card_id: value_profile.delhivery_settlement.txn_type
  name: delhivery_settlement.txn_type Value Profile
  fields:
    name: delhivery_settlement.txn_type Value Profile
    description: Known values and meanings for delhivery_settlement.txn_type.
    status: active
    confidence: curated
    source_documents:
    - Logistics KB Doc.docx
    - Cognee KB Design v4.md
    - logistics_gold_std_raw_md_frame_v3.md
    - logistics_gold_std_canonical_card_frame_v5.md
    created_by: kb_authoring_assistant
    updated_by: kb_authoring_assistant
    version: 5.0-manifest-aligned
    table_id: table.zs_observe.delhivery_settlement
    column_id: column.zs_observe.delhivery_settlement.txn_type
    value_type: enum_or_enum_with_nulls
    values: CR=Credit/remittance to seller (credit); NULL=Unknown/partial older ingestion (unknown)
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
  card_id: value_profile.delhivery_settlement.payment_mode
  name: delhivery_settlement.payment_mode Value Profile
  fields:
    name: delhivery_settlement.payment_mode Value Profile
    description: Known values and meanings for delhivery_settlement.payment_mode.
    status: active
    confidence: curated
    source_documents:
    - Logistics KB Doc.docx
    - Cognee KB Design v4.md
    - logistics_gold_std_raw_md_frame_v3.md
    - logistics_gold_std_canonical_card_frame_v5.md
    created_by: kb_authoring_assistant
    updated_by: kb_authoring_assistant
    version: 5.0-manifest-aligned
    table_id: table.zs_observe.delhivery_settlement
    column_id: column.zs_observe.delhivery_settlement.payment_mode
    value_type: enum_or_enum_with_nulls
    values: QR=Customer paid by QR at door (qr_cod); NULL=Cash or unknown COD mode (cash_or_unknown)
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
  card_id: value_profile.delhivery_settlement.status
  name: delhivery_settlement.status Value Profile
  fields:
    name: delhivery_settlement.status Value Profile
    description: Known values and meanings for delhivery_settlement.status.
    status: active
    confidence: curated
    source_documents:
    - Logistics KB Doc.docx
    - Cognee KB Design v4.md
    - logistics_gold_std_raw_md_frame_v3.md
    - logistics_gold_std_canonical_card_frame_v5.md
    created_by: kb_authoring_assistant
    updated_by: kb_authoring_assistant
    version: 5.0-manifest-aligned
    table_id: table.zs_observe.delhivery_settlement
    column_id: column.zs_observe.delhivery_settlement.status
    value_type: enum_or_enum_with_nulls
    values: Delivered=COD delivered/settled context (delivered)
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
    - see metric_impl blocks in delhivery_logistics_parser_ready_v6_role_split.md
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
    - see metric_impl blocks in delhivery_logistics_parser_ready_v6_role_split.md
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
    - see metric_impl blocks in delhivery_logistics_parser_ready_v6_role_split.md
    evidence_refs:
    - evidence.logistics_kb_doc
    - evidence.cognee_design_v4
    - evidence.unified_edge_scope
```

```yaml
candidate_card:
  card_type: metric
  card_id: metric.cod_expected_amount
  name: COD Expected Amount
  fields:
    name: COD Expected Amount
    description: COD amount expected from customer/order.
    status: active
    confidence: curated
    source_documents:
    - Logistics KB Doc.docx
    - Cognee KB Design v4.md
    - logistics_gold_std_raw_md_frame_v3.md
    - logistics_gold_std_canonical_card_frame_v5.md
    created_by: kb_authoring_assistant
    updated_by: kb_authoring_assistant
    version: 5.0-manifest-aligned
    metric_name: COD Expected Amount
    aliases:
    - COD payable
    - COD due from customer
    metric_type: amount/count/rate/days_by_metric
    unit: currency/count/percentage/days_by_metric
    default_aggregation: SUM or COUNT or ratio by metric
    default_grain: shipment_awb_or_settlement_batch
    polarity: context_dependent
    business_concepts:
    - logistics
    - cod_expected_amount
    domain_ids:
    - domain.logistics_reconciliation
    implementations:
    - see metric_impl blocks in delhivery_logistics_parser_ready_v6_role_split.md
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
    - see metric_impl blocks in delhivery_logistics_parser_ready_v6_role_split.md
    evidence_refs:
    - evidence.logistics_kb_doc
    - evidence.cognee_design_v4
    - evidence.unified_edge_scope
```

```yaml
candidate_card:
  card_type: metric
  card_id: metric.cod_gap_amount
  name: COD Gap Amount
  fields:
    name: COD Gap Amount
    description: Difference between COD expected and COD remitted/collected.
    status: active
    confidence: curated
    source_documents:
    - Logistics KB Doc.docx
    - Cognee KB Design v4.md
    - logistics_gold_std_raw_md_frame_v3.md
    - logistics_gold_std_canonical_card_frame_v5.md
    created_by: kb_authoring_assistant
    updated_by: kb_authoring_assistant
    version: 5.0-manifest-aligned
    metric_name: COD Gap Amount
    aliases:
    - COD shortfall
    - COD mismatch
    metric_type: amount/count/rate/days_by_metric
    unit: currency/count/percentage/days_by_metric
    default_aggregation: SUM or COUNT or ratio by metric
    default_grain: shipment_awb_or_settlement_batch
    polarity: context_dependent
    business_concepts:
    - logistics
    - cod_gap_amount
    domain_ids:
    - domain.logistics_reconciliation
    implementations:
    - see metric_impl blocks in delhivery_logistics_parser_ready_v6_role_split.md
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
    - see metric_impl blocks in delhivery_logistics_parser_ready_v6_role_split.md
    evidence_refs:
    - evidence.logistics_kb_doc
    - evidence.cognee_design_v4
    - evidence.unified_edge_scope
```

```yaml
candidate_card:
  card_type: metric
  card_id: metric.declared_product_value
  name: Declared Product Value
  fields:
    name: Declared Product Value
    description: Product/order value declared to courier or logistics platform.
    status: active
    confidence: curated
    source_documents:
    - Logistics KB Doc.docx
    - Cognee KB Design v4.md
    - logistics_gold_std_raw_md_frame_v3.md
    - logistics_gold_std_canonical_card_frame_v5.md
    created_by: kb_authoring_assistant
    updated_by: kb_authoring_assistant
    version: 5.0-manifest-aligned
    metric_name: Declared Product Value
    aliases:
    - declared value
    - order value for FOV
    metric_type: amount/count/rate/days_by_metric
    unit: currency/count/percentage/days_by_metric
    default_aggregation: SUM or COUNT or ratio by metric
    default_grain: shipment_awb_or_settlement_batch
    polarity: context_dependent
    business_concepts:
    - logistics
    - declared_product_value
    domain_ids:
    - domain.logistics_reconciliation
    implementations:
    - see metric_impl blocks in delhivery_logistics_parser_ready_v6_role_split.md
    evidence_refs:
    - evidence.logistics_kb_doc
    - evidence.cognee_design_v4
    - evidence.unified_edge_scope
```

```yaml
candidate_card:
  card_type: metric
  card_id: metric.delivered_shipment_count
  name: Delivered Shipment Count
  fields:
    name: Delivered Shipment Count
    description: Count of shipments delivered to customer.
    status: active
    confidence: curated
    source_documents:
    - Logistics KB Doc.docx
    - Cognee KB Design v4.md
    - logistics_gold_std_raw_md_frame_v3.md
    - logistics_gold_std_canonical_card_frame_v5.md
    created_by: kb_authoring_assistant
    updated_by: kb_authoring_assistant
    version: 5.0-manifest-aligned
    metric_name: Delivered Shipment Count
    aliases:
    - delivered shipments
    - successful deliveries
    metric_type: amount/count/rate/days_by_metric
    unit: currency/count/percentage/days_by_metric
    default_aggregation: SUM or COUNT or ratio by metric
    default_grain: shipment_awb_or_settlement_batch
    polarity: context_dependent
    business_concepts:
    - logistics
    - delivered_shipment_count
    domain_ids:
    - domain.logistics_reconciliation
    implementations:
    - see metric_impl blocks in delhivery_logistics_parser_ready_v6_role_split.md
    evidence_refs:
    - evidence.logistics_kb_doc
    - evidence.cognee_design_v4
    - evidence.unified_edge_scope
```

```yaml
candidate_card:
  card_type: metric
  card_id: metric.dto_freight_amount
  name: DTO Freight Amount
  fields:
    name: DTO Freight Amount
    description: Freight amount charged for DTO or dispatch-to-origin movement.
    status: active
    confidence: curated
    source_documents:
    - Logistics KB Doc.docx
    - Cognee KB Design v4.md
    - logistics_gold_std_raw_md_frame_v3.md
    - logistics_gold_std_canonical_card_frame_v5.md
    created_by: kb_authoring_assistant
    updated_by: kb_authoring_assistant
    version: 5.0-manifest-aligned
    metric_name: DTO Freight Amount
    aliases:
    - dispatch to origin charge
    - DTO charge
    metric_type: amount/count/rate/days_by_metric
    unit: currency/count/percentage/days_by_metric
    default_aggregation: SUM or COUNT or ratio by metric
    default_grain: shipment_awb_or_settlement_batch
    polarity: context_dependent
    business_concepts:
    - logistics
    - dto_freight_amount
    domain_ids:
    - domain.logistics_reconciliation
    implementations:
    - see metric_impl blocks in delhivery_logistics_parser_ready_v6_role_split.md
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
    - see metric_impl blocks in delhivery_logistics_parser_ready_v6_role_split.md
    evidence_refs:
    - evidence.logistics_kb_doc
    - evidence.cognee_design_v4
    - evidence.unified_edge_scope
```

```yaml
candidate_card:
  card_type: metric
  card_id: metric.fov_insurance_amount
  name: FOV or Insurance Amount
  fields:
    name: FOV or Insurance Amount
    description: Insurance/FOV component of freight.
    status: active
    confidence: curated
    source_documents:
    - Logistics KB Doc.docx
    - Cognee KB Design v4.md
    - logistics_gold_std_raw_md_frame_v3.md
    - logistics_gold_std_canonical_card_frame_v5.md
    created_by: kb_authoring_assistant
    updated_by: kb_authoring_assistant
    version: 5.0-manifest-aligned
    metric_name: FOV or Insurance Amount
    aliases:
    - insurance charge
    - freight on value
    metric_type: amount/count/rate/days_by_metric
    unit: currency/count/percentage/days_by_metric
    default_aggregation: SUM or COUNT or ratio by metric
    default_grain: shipment_awb_or_settlement_batch
    polarity: context_dependent
    business_concepts:
    - logistics
    - fov_insurance_amount
    domain_ids:
    - domain.logistics_reconciliation
    implementations:
    - see metric_impl blocks in delhivery_logistics_parser_ready_v6_role_split.md
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
    - see metric_impl blocks in delhivery_logistics_parser_ready_v6_role_split.md
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
    - see metric_impl blocks in delhivery_logistics_parser_ready_v6_role_split.md
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
    - see metric_impl blocks in delhivery_logistics_parser_ready_v6_role_split.md
    evidence_refs:
    - evidence.logistics_kb_doc
    - evidence.cognee_design_v4
    - evidence.unified_edge_scope
```

```yaml
candidate_card:
  card_type: metric
  card_id: metric.payable_amount
  name: Payable Amount
  fields:
    name: Payable Amount
    description: Net amount payable to seller after deductions.
    status: active
    confidence: curated
    source_documents:
    - Logistics KB Doc.docx
    - Cognee KB Design v4.md
    - logistics_gold_std_raw_md_frame_v3.md
    - logistics_gold_std_canonical_card_frame_v5.md
    created_by: kb_authoring_assistant
    updated_by: kb_authoring_assistant
    version: 5.0-manifest-aligned
    metric_name: Payable Amount
    aliases:
    - net payable
    - courier payable
    metric_type: amount/count/rate/days_by_metric
    unit: currency/count/percentage/days_by_metric
    default_aggregation: SUM or COUNT or ratio by metric
    default_grain: shipment_awb_or_settlement_batch
    polarity: context_dependent
    business_concepts:
    - logistics
    - payable_amount
    domain_ids:
    - domain.logistics_reconciliation
    implementations:
    - see metric_impl blocks in delhivery_logistics_parser_ready_v6_role_split.md
    evidence_refs:
    - evidence.logistics_kb_doc
    - evidence.cognee_design_v4
    - evidence.unified_edge_scope
```

```yaml
candidate_card:
  card_type: metric
  card_id: metric.peak_surcharge_amount
  name: Peak Surcharge Amount
  fields:
    name: Peak Surcharge Amount
    description: Peak season surcharge component of freight.
    status: active
    confidence: curated
    source_documents:
    - Logistics KB Doc.docx
    - Cognee KB Design v4.md
    - logistics_gold_std_raw_md_frame_v3.md
    - logistics_gold_std_canonical_card_frame_v5.md
    created_by: kb_authoring_assistant
    updated_by: kb_authoring_assistant
    version: 5.0-manifest-aligned
    metric_name: Peak Surcharge Amount
    aliases:
    - peak season fee
    metric_type: amount/count/rate/days_by_metric
    unit: currency/count/percentage/days_by_metric
    default_aggregation: SUM or COUNT or ratio by metric
    default_grain: shipment_awb_or_settlement_batch
    polarity: context_dependent
    business_concepts:
    - logistics
    - peak_surcharge_amount
    domain_ids:
    - domain.logistics_reconciliation
    implementations:
    - see metric_impl blocks in delhivery_logistics_parser_ready_v6_role_split.md
    evidence_refs:
    - evidence.logistics_kb_doc
    - evidence.cognee_design_v4
    - evidence.unified_edge_scope
```

```yaml
candidate_card:
  card_type: metric
  card_id: metric.pickup_charge_amount
  name: Pickup Charge Amount
  fields:
    name: Pickup Charge Amount
    description: Pickup charge component of freight.
    status: active
    confidence: curated
    source_documents:
    - Logistics KB Doc.docx
    - Cognee KB Design v4.md
    - logistics_gold_std_raw_md_frame_v3.md
    - logistics_gold_std_canonical_card_frame_v5.md
    created_by: kb_authoring_assistant
    updated_by: kb_authoring_assistant
    version: 5.0-manifest-aligned
    metric_name: Pickup Charge Amount
    aliases:
    - pickup fee
    metric_type: amount/count/rate/days_by_metric
    unit: currency/count/percentage/days_by_metric
    default_aggregation: SUM or COUNT or ratio by metric
    default_grain: shipment_awb_or_settlement_batch
    polarity: context_dependent
    business_concepts:
    - logistics
    - pickup_charge_amount
    domain_ids:
    - domain.logistics_reconciliation
    implementations:
    - see metric_impl blocks in delhivery_logistics_parser_ready_v6_role_split.md
    evidence_refs:
    - evidence.logistics_kb_doc
    - evidence.cognee_design_v4
    - evidence.unified_edge_scope
```

```yaml
candidate_card:
  card_type: metric
  card_id: metric.qr_cod_remitted_amount
  name: QR COD Remitted Amount
  fields:
    name: QR COD Remitted Amount
    description: COD remitted where payment mode indicates QR or at-door digital collection.
    status: active
    confidence: curated
    source_documents:
    - Logistics KB Doc.docx
    - Cognee KB Design v4.md
    - logistics_gold_std_raw_md_frame_v3.md
    - logistics_gold_std_canonical_card_frame_v5.md
    created_by: kb_authoring_assistant
    updated_by: kb_authoring_assistant
    version: 5.0-manifest-aligned
    metric_name: QR COD Remitted Amount
    aliases:
    - QR based COD
    - digital COD collection
    metric_type: amount/count/rate/days_by_metric
    unit: currency/count/percentage/days_by_metric
    default_aggregation: SUM or COUNT or ratio by metric
    default_grain: shipment_awb_or_settlement_batch
    polarity: context_dependent
    business_concepts:
    - logistics
    - qr_cod_remitted_amount
    domain_ids:
    - domain.logistics_reconciliation
    implementations:
    - see metric_impl blocks in delhivery_logistics_parser_ready_v6_role_split.md
    evidence_refs:
    - evidence.logistics_kb_doc
    - evidence.cognee_design_v4
    - evidence.unified_edge_scope
```

```yaml
candidate_card:
  card_type: metric
  card_id: metric.rto_count
  name: RTO Count
  fields:
    name: RTO Count
    description: Count of shipments returned to origin after failed delivery.
    status: active
    confidence: curated
    source_documents:
    - Logistics KB Doc.docx
    - Cognee KB Design v4.md
    - logistics_gold_std_raw_md_frame_v3.md
    - logistics_gold_std_canonical_card_frame_v5.md
    created_by: kb_authoring_assistant
    updated_by: kb_authoring_assistant
    version: 5.0-manifest-aligned
    metric_name: RTO Count
    aliases:
    - return to origin count
    - RTO shipments
    metric_type: amount/count/rate/days_by_metric
    unit: currency/count/percentage/days_by_metric
    default_aggregation: SUM or COUNT or ratio by metric
    default_grain: shipment_awb_or_settlement_batch
    polarity: context_dependent
    business_concepts:
    - logistics
    - rto_count
    domain_ids:
    - domain.logistics_reconciliation
    implementations:
    - see metric_impl blocks in delhivery_logistics_parser_ready_v6_role_split.md
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
    - see metric_impl blocks in delhivery_logistics_parser_ready_v6_role_split.md
    evidence_refs:
    - evidence.logistics_kb_doc
    - evidence.cognee_design_v4
    - evidence.unified_edge_scope
```

```yaml
candidate_card:
  card_type: metric
  card_id: metric.settlement_batch_count
  name: Settlement Batch Count
  fields:
    name: Settlement Batch Count
    description: Count of settlement or remittance batches.
    status: active
    confidence: curated
    source_documents:
    - Logistics KB Doc.docx
    - Cognee KB Design v4.md
    - logistics_gold_std_raw_md_frame_v3.md
    - logistics_gold_std_canonical_card_frame_v5.md
    created_by: kb_authoring_assistant
    updated_by: kb_authoring_assistant
    version: 5.0-manifest-aligned
    metric_name: Settlement Batch Count
    aliases:
    - remittance batch count
    metric_type: amount/count/rate/days_by_metric
    unit: currency/count/percentage/days_by_metric
    default_aggregation: SUM or COUNT or ratio by metric
    default_grain: shipment_awb_or_settlement_batch
    polarity: context_dependent
    business_concepts:
    - logistics
    - settlement_batch_count
    domain_ids:
    - domain.logistics_reconciliation
    implementations:
    - see metric_impl blocks in delhivery_logistics_parser_ready_v6_role_split.md
    evidence_refs:
    - evidence.logistics_kb_doc
    - evidence.cognee_design_v4
    - evidence.unified_edge_scope
```

```yaml
candidate_card:
  card_type: metric
  card_id: metric.shipment_count
  name: Shipment Count
  fields:
    name: Shipment Count
    description: Count of shipment or AWB records.
    status: active
    confidence: curated
    source_documents:
    - Logistics KB Doc.docx
    - Cognee KB Design v4.md
    - logistics_gold_std_raw_md_frame_v3.md
    - logistics_gold_std_canonical_card_frame_v5.md
    created_by: kb_authoring_assistant
    updated_by: kb_authoring_assistant
    version: 5.0-manifest-aligned
    metric_name: Shipment Count
    aliases:
    - shipments
    - shipment volume
    - AWB count
    metric_type: amount/count/rate/days_by_metric
    unit: currency/count/percentage/days_by_metric
    default_aggregation: SUM or COUNT or ratio by metric
    default_grain: shipment_awb_or_settlement_batch
    polarity: context_dependent
    business_concepts:
    - logistics
    - shipment_count
    domain_ids:
    - domain.logistics_reconciliation
    implementations:
    - see metric_impl blocks in delhivery_logistics_parser_ready_v6_role_split.md
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
    - see metric_impl blocks in delhivery_logistics_parser_ready_v6_role_split.md
    evidence_refs:
    - evidence.logistics_kb_doc
    - evidence.cognee_design_v4
    - evidence.unified_edge_scope
```

### 4.9 metric_implementation cards

```yaml
candidate_card:
  card_type: metric_implementation
  card_id: metric_impl.delhivery_invoice.freight_billed_amount
  name: Delhivery Freight Billed Amount Implementation
  fields:
    name: Delhivery Freight Billed Amount Implementation
    description: Freight Billed Amount implementation for Delhivery using delhivery_invoice.
    status: active
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
    implementation_name: Delhivery Freight Billed Amount
    metric_pattern: sum_component_amounts
    applicability: platform=delhivery; table=zs_observe.delhivery_invoice; account filters via Account Data Binding only
    base_tables:
    - table.zs_observe.delhivery_invoice
    required_columns:
    - column.zs_observe.delhivery_invoice.charge_dl
    - column.zs_observe.delhivery_invoice.charge_rto
    - column.zs_observe.delhivery_invoice.charge_dto
    - column.zs_observe.delhivery_invoice.charge_cod
    - column.zs_observe.delhivery_invoice.charge_fsc
    - column.zs_observe.delhivery_invoice.charge_fs
    - column.zs_observe.delhivery_invoice.charge_fov
    - column.zs_observe.delhivery_invoice.charge_air
    - column.zs_observe.delhivery_invoice.charge_pickup
    - column.zs_observe.delhivery_invoice.charge_peak
    semantic_filters: []
    formula_description: SUM(charge_dl + charge_rto + charge_dto + charge_cod + charge_fsc + charge_fs + charge_fov + charge_air
      + charge_pickup + charge_peak)
    formula_sql: SUM(charge_dl + charge_rto + charge_dto + charge_cod + charge_fsc + charge_fs + charge_fov + charge_air +
      charge_pickup + charge_peak)
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
    - invoice_date_or_created_date
    unit: currency/count/percentage/days_by_metric
    precision: 2_decimal_places
    caveats: charged_amount in delhivery_invoice is declared product value, not freight.
    evidence_refs:
    - evidence.logistics_kb_doc
    - evidence.cognee_design_v4
    - evidence.unified_edge_scope
    formula_template_id: formula_template.logistics.component_sum
```

```yaml
candidate_card:
  card_type: metric_implementation
  card_id: metric_impl.delhivery_invoice.forward_freight_amount
  name: Delhivery Forward Freight Amount Implementation
  fields:
    name: Delhivery Forward Freight Amount Implementation
    description: Forward Freight Amount implementation for Delhivery using delhivery_invoice.
    status: active
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
    implementation_name: Delhivery Forward Freight Amount
    metric_pattern: sum_component_amounts
    applicability: platform=delhivery; table=zs_observe.delhivery_invoice; account filters via Account Data Binding only
    base_tables:
    - table.zs_observe.delhivery_invoice
    required_columns:
    - column.zs_observe.delhivery_invoice.charge_dl
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
    - invoice_date_or_created_date
    unit: currency/count/percentage/days_by_metric
    precision: 2_decimal_places
    caveats: charged_amount in delhivery_invoice is declared product value, not freight.
    evidence_refs:
    - evidence.logistics_kb_doc
    - evidence.cognee_design_v4
    - evidence.unified_edge_scope
    formula_template_id: formula_template.logistics.component_sum
```

```yaml
candidate_card:
  card_type: metric_implementation
  card_id: metric_impl.delhivery_invoice.rto_freight_amount
  name: Delhivery RTO Freight Amount Implementation
  fields:
    name: Delhivery RTO Freight Amount Implementation
    description: RTO Freight Amount implementation for Delhivery using delhivery_invoice.
    status: active
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
    implementation_name: Delhivery RTO Freight Amount
    metric_pattern: sum_component_amounts
    applicability: platform=delhivery; table=zs_observe.delhivery_invoice; account filters via Account Data Binding only
    base_tables:
    - table.zs_observe.delhivery_invoice
    required_columns:
    - column.zs_observe.delhivery_invoice.charge_rto
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
    - invoice_date_or_created_date
    unit: currency/count/percentage/days_by_metric
    precision: 2_decimal_places
    caveats: charged_amount in delhivery_invoice is declared product value, not freight.
    evidence_refs:
    - evidence.logistics_kb_doc
    - evidence.cognee_design_v4
    - evidence.unified_edge_scope
    formula_template_id: formula_template.logistics.component_sum
```

```yaml
candidate_card:
  card_type: metric_implementation
  card_id: metric_impl.delhivery_invoice.dto_freight_amount
  name: Delhivery DTO Freight Amount Implementation
  fields:
    name: Delhivery DTO Freight Amount Implementation
    description: DTO Freight Amount implementation for Delhivery using delhivery_invoice.
    status: active
    confidence: curated
    source_documents:
    - Logistics KB Doc.docx
    - Cognee KB Design v4.md
    - logistics_gold_std_raw_md_frame_v3.md
    - logistics_gold_std_canonical_card_frame_v5.md
    created_by: kb_authoring_assistant
    updated_by: kb_authoring_assistant
    version: 5.0-manifest-aligned
    metric_id: metric.dto_freight_amount
    implementation_name: Delhivery DTO Freight Amount
    metric_pattern: sum_component_amounts
    applicability: platform=delhivery; table=zs_observe.delhivery_invoice; account filters via Account Data Binding only
    base_tables:
    - table.zs_observe.delhivery_invoice
    required_columns:
    - column.zs_observe.delhivery_invoice.charge_dto
    semantic_filters: []
    formula_description: SUM(charge_dto)
    formula_sql: SUM(charge_dto)
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
    - invoice_date_or_created_date
    unit: currency/count/percentage/days_by_metric
    precision: 2_decimal_places
    caveats: charged_amount in delhivery_invoice is declared product value, not freight.
    evidence_refs:
    - evidence.logistics_kb_doc
    - evidence.cognee_design_v4
    - evidence.unified_edge_scope
    formula_template_id: formula_template.logistics.component_sum
```

```yaml
candidate_card:
  card_type: metric_implementation
  card_id: metric_impl.delhivery_invoice.cod_fee_amount
  name: Delhivery COD Fee Amount Implementation
  fields:
    name: Delhivery COD Fee Amount Implementation
    description: COD Fee Amount implementation for Delhivery using delhivery_invoice.
    status: active
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
    implementation_name: Delhivery COD Fee Amount
    metric_pattern: sum_component_amounts
    applicability: platform=delhivery; table=zs_observe.delhivery_invoice; account filters via Account Data Binding only
    base_tables:
    - table.zs_observe.delhivery_invoice
    required_columns:
    - column.zs_observe.delhivery_invoice.charge_cod
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
    - invoice_date_or_created_date
    unit: currency/count/percentage/days_by_metric
    precision: 2_decimal_places
    caveats: charged_amount in delhivery_invoice is declared product value, not freight.
    evidence_refs:
    - evidence.logistics_kb_doc
    - evidence.cognee_design_v4
    - evidence.unified_edge_scope
    formula_template_id: formula_template.logistics.component_sum
```

```yaml
candidate_card:
  card_type: metric_implementation
  card_id: metric_impl.delhivery_invoice.fuel_surcharge_amount
  name: Delhivery Fuel Surcharge Amount Implementation
  fields:
    name: Delhivery Fuel Surcharge Amount Implementation
    description: Fuel Surcharge Amount implementation for Delhivery using delhivery_invoice.
    status: active
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
    implementation_name: Delhivery Fuel Surcharge Amount
    metric_pattern: sum_component_amounts
    applicability: platform=delhivery; table=zs_observe.delhivery_invoice; account filters via Account Data Binding only
    base_tables:
    - table.zs_observe.delhivery_invoice
    required_columns:
    - column.zs_observe.delhivery_invoice.charge_fsc
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
    - invoice_date_or_created_date
    unit: currency/count/percentage/days_by_metric
    precision: 2_decimal_places
    caveats: charged_amount in delhivery_invoice is declared product value, not freight.
    evidence_refs:
    - evidence.logistics_kb_doc
    - evidence.cognee_design_v4
    - evidence.unified_edge_scope
    formula_template_id: formula_template.logistics.component_sum
```

```yaml
candidate_card:
  card_type: metric_implementation
  card_id: metric_impl.delhivery_invoice.fov_insurance_amount
  name: Delhivery FOV or Insurance Amount Implementation
  fields:
    name: Delhivery FOV or Insurance Amount Implementation
    description: FOV or Insurance Amount implementation for Delhivery using delhivery_invoice.
    status: active
    confidence: curated
    source_documents:
    - Logistics KB Doc.docx
    - Cognee KB Design v4.md
    - logistics_gold_std_raw_md_frame_v3.md
    - logistics_gold_std_canonical_card_frame_v5.md
    created_by: kb_authoring_assistant
    updated_by: kb_authoring_assistant
    version: 5.0-manifest-aligned
    metric_id: metric.fov_insurance_amount
    implementation_name: Delhivery FOV or Insurance Amount
    metric_pattern: sum_component_amounts
    applicability: platform=delhivery; table=zs_observe.delhivery_invoice; account filters via Account Data Binding only
    base_tables:
    - table.zs_observe.delhivery_invoice
    required_columns:
    - column.zs_observe.delhivery_invoice.charge_fov
    semantic_filters: []
    formula_description: SUM(charge_fov)
    formula_sql: SUM(charge_fov)
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
    - invoice_date_or_created_date
    unit: currency/count/percentage/days_by_metric
    precision: 2_decimal_places
    caveats: charged_amount in delhivery_invoice is declared product value, not freight.
    evidence_refs:
    - evidence.logistics_kb_doc
    - evidence.cognee_design_v4
    - evidence.unified_edge_scope
    formula_template_id: formula_template.logistics.component_sum
```

```yaml
candidate_card:
  card_type: metric_implementation
  card_id: metric_impl.delhivery_invoice.pickup_charge_amount
  name: Delhivery Pickup Charge Amount Implementation
  fields:
    name: Delhivery Pickup Charge Amount Implementation
    description: Pickup Charge Amount implementation for Delhivery using delhivery_invoice.
    status: active
    confidence: curated
    source_documents:
    - Logistics KB Doc.docx
    - Cognee KB Design v4.md
    - logistics_gold_std_raw_md_frame_v3.md
    - logistics_gold_std_canonical_card_frame_v5.md
    created_by: kb_authoring_assistant
    updated_by: kb_authoring_assistant
    version: 5.0-manifest-aligned
    metric_id: metric.pickup_charge_amount
    implementation_name: Delhivery Pickup Charge Amount
    metric_pattern: sum_component_amounts
    applicability: platform=delhivery; table=zs_observe.delhivery_invoice; account filters via Account Data Binding only
    base_tables:
    - table.zs_observe.delhivery_invoice
    required_columns:
    - column.zs_observe.delhivery_invoice.charge_pickup
    semantic_filters: []
    formula_description: SUM(charge_pickup)
    formula_sql: SUM(charge_pickup)
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
    - invoice_date_or_created_date
    unit: currency/count/percentage/days_by_metric
    precision: 2_decimal_places
    caveats: charged_amount in delhivery_invoice is declared product value, not freight.
    evidence_refs:
    - evidence.logistics_kb_doc
    - evidence.cognee_design_v4
    - evidence.unified_edge_scope
    formula_template_id: formula_template.logistics.component_sum
```

```yaml
candidate_card:
  card_type: metric_implementation
  card_id: metric_impl.delhivery_invoice.peak_surcharge_amount
  name: Delhivery Peak Surcharge Amount Implementation
  fields:
    name: Delhivery Peak Surcharge Amount Implementation
    description: Peak Surcharge Amount implementation for Delhivery using delhivery_invoice.
    status: active
    confidence: curated
    source_documents:
    - Logistics KB Doc.docx
    - Cognee KB Design v4.md
    - logistics_gold_std_raw_md_frame_v3.md
    - logistics_gold_std_canonical_card_frame_v5.md
    created_by: kb_authoring_assistant
    updated_by: kb_authoring_assistant
    version: 5.0-manifest-aligned
    metric_id: metric.peak_surcharge_amount
    implementation_name: Delhivery Peak Surcharge Amount
    metric_pattern: sum_component_amounts
    applicability: platform=delhivery; table=zs_observe.delhivery_invoice; account filters via Account Data Binding only
    base_tables:
    - table.zs_observe.delhivery_invoice
    required_columns:
    - column.zs_observe.delhivery_invoice.charge_peak
    semantic_filters: []
    formula_description: SUM(charge_peak)
    formula_sql: SUM(charge_peak)
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
    - invoice_date_or_created_date
    unit: currency/count/percentage/days_by_metric
    precision: 2_decimal_places
    caveats: charged_amount in delhivery_invoice is declared product value, not freight.
    evidence_refs:
    - evidence.logistics_kb_doc
    - evidence.cognee_design_v4
    - evidence.unified_edge_scope
    formula_template_id: formula_template.logistics.component_sum
```

```yaml
candidate_card:
  card_type: metric_implementation
  card_id: metric_impl.delhivery_invoice.gst_on_freight_amount
  name: Delhivery GST on Freight Amount Implementation
  fields:
    name: Delhivery GST on Freight Amount Implementation
    description: GST on Freight Amount implementation for Delhivery using delhivery_invoice.
    status: active
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
    implementation_name: Delhivery GST on Freight Amount
    metric_pattern: sum_component_amounts
    applicability: platform=delhivery; table=zs_observe.delhivery_invoice; account filters via Account Data Binding only
    base_tables:
    - table.zs_observe.delhivery_invoice
    required_columns:
    - column.zs_observe.delhivery_invoice.tax_cgst_amount
    - column.zs_observe.delhivery_invoice.tax_sgst_amount
    - column.zs_observe.delhivery_invoice.tax_igst_amount
    semantic_filters: []
    formula_description: SUM(tax_cgst_amount + tax_sgst_amount + tax_igst_amount)
    formula_sql: SUM(tax_cgst_amount + tax_sgst_amount + tax_igst_amount)
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
    - invoice_date_or_created_date
    unit: currency/count/percentage/days_by_metric
    precision: 2_decimal_places
    caveats: charged_amount in delhivery_invoice is declared product value, not freight.
    evidence_refs:
    - evidence.logistics_kb_doc
    - evidence.cognee_design_v4
    - evidence.unified_edge_scope
    formula_template_id: formula_template.logistics.component_sum
```

```yaml
candidate_card:
  card_type: metric_implementation
  card_id: metric_impl.delhivery_invoice.declared_product_value
  name: Delhivery Declared Product Value Implementation
  fields:
    name: Delhivery Declared Product Value Implementation
    description: Declared Product Value implementation for Delhivery using delhivery_invoice.
    status: active
    confidence: curated
    source_documents:
    - Logistics KB Doc.docx
    - Cognee KB Design v4.md
    - logistics_gold_std_raw_md_frame_v3.md
    - logistics_gold_std_canonical_card_frame_v5.md
    created_by: kb_authoring_assistant
    updated_by: kb_authoring_assistant
    version: 5.0-manifest-aligned
    metric_id: metric.declared_product_value
    implementation_name: Delhivery Declared Product Value
    metric_pattern: sum_component_amounts
    applicability: platform=delhivery; table=zs_observe.delhivery_invoice; account filters via Account Data Binding only
    base_tables:
    - table.zs_observe.delhivery_invoice
    required_columns:
    - column.zs_observe.delhivery_invoice.charged_amount
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
    - invoice_date_or_created_date
    unit: currency/count/percentage/days_by_metric
    precision: 2_decimal_places
    caveats: charged_amount in delhivery_invoice is declared product value, not freight.
    evidence_refs:
    - evidence.logistics_kb_doc
    - evidence.cognee_design_v4
    - evidence.unified_edge_scope
    formula_template_id: formula_template.logistics.component_sum
```

```yaml
candidate_card:
  card_type: metric_implementation
  card_id: metric_impl.delhivery_invoice.cod_expected_amount
  name: Delhivery COD Expected Amount Implementation
  fields:
    name: Delhivery COD Expected Amount Implementation
    description: COD Expected Amount implementation for Delhivery using delhivery_invoice.
    status: active
    confidence: curated
    source_documents:
    - Logistics KB Doc.docx
    - Cognee KB Design v4.md
    - logistics_gold_std_raw_md_frame_v3.md
    - logistics_gold_std_canonical_card_frame_v5.md
    created_by: kb_authoring_assistant
    updated_by: kb_authoring_assistant
    version: 5.0-manifest-aligned
    metric_id: metric.cod_expected_amount
    implementation_name: Delhivery COD Expected Amount
    metric_pattern: sum_component_amounts
    applicability: platform=delhivery; table=zs_observe.delhivery_invoice; account filters via Account Data Binding only
    base_tables:
    - table.zs_observe.delhivery_invoice
    required_columns:
    - column.zs_observe.delhivery_invoice.cod_amount
    semantic_filters: []
    formula_description: SUM(cod_amount)
    formula_sql: SUM(cod_amount)
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
    - invoice_date_or_created_date
    unit: currency/count/percentage/days_by_metric
    precision: 2_decimal_places
    caveats: charged_amount in delhivery_invoice is declared product value, not freight.
    evidence_refs:
    - evidence.logistics_kb_doc
    - evidence.cognee_design_v4
    - evidence.unified_edge_scope
    formula_template_id: formula_template.logistics.component_sum
```

```yaml
candidate_card:
  card_type: metric_implementation
  card_id: metric_impl.delhivery_invoice.billable_weight
  name: Delhivery Billable Weight Implementation
  fields:
    name: Delhivery Billable Weight Implementation
    description: Billable Weight implementation for Delhivery using delhivery_invoice.
    status: active
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
    implementation_name: Delhivery Billable Weight
    metric_pattern: sum_component_amounts
    applicability: platform=delhivery; table=zs_observe.delhivery_invoice; account filters via Account Data Binding only
    base_tables:
    - table.zs_observe.delhivery_invoice
    required_columns:
    - column.zs_observe.delhivery_invoice.charged_weight
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
    - invoice_date_or_created_date
    unit: currency/count/percentage/days_by_metric
    precision: 2_decimal_places
    caveats: charged_amount in delhivery_invoice is declared product value, not freight.
    evidence_refs:
    - evidence.logistics_kb_doc
    - evidence.cognee_design_v4
    - evidence.unified_edge_scope
    formula_template_id: formula_template.logistics.component_sum
```

```yaml
candidate_card:
  card_type: metric_implementation
  card_id: metric_impl.delhivery_invoice.shipment_count
  name: Delhivery Shipment Count Implementation
  fields:
    name: Delhivery Shipment Count Implementation
    description: Shipment Count implementation for Delhivery using delhivery_invoice.
    status: active
    confidence: curated
    source_documents:
    - Logistics KB Doc.docx
    - Cognee KB Design v4.md
    - logistics_gold_std_raw_md_frame_v3.md
    - logistics_gold_std_canonical_card_frame_v5.md
    created_by: kb_authoring_assistant
    updated_by: kb_authoring_assistant
    version: 5.0-manifest-aligned
    metric_id: metric.shipment_count
    implementation_name: Delhivery Shipment Count
    metric_pattern: filtered_count_or_ratio
    applicability: platform=delhivery; table=zs_observe.delhivery_invoice; account filters via Account Data Binding only
    base_tables:
    - table.zs_observe.delhivery_invoice
    required_columns:
    - column.zs_observe.delhivery_invoice.forward_awb_number
    semantic_filters: []
    formula_description: COUNT(*)
    formula_sql: COUNT(*)
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
    - created_date_or_invoice_period
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
  card_id: metric_impl.delhivery_invoice.delivered_shipment_count
  name: Delhivery Delivered Shipment Count Implementation
  fields:
    name: Delhivery Delivered Shipment Count Implementation
    description: Delivered Shipment Count implementation for Delhivery using delhivery_invoice.
    status: active
    confidence: curated
    source_documents:
    - Logistics KB Doc.docx
    - Cognee KB Design v4.md
    - logistics_gold_std_raw_md_frame_v3.md
    - logistics_gold_std_canonical_card_frame_v5.md
    created_by: kb_authoring_assistant
    updated_by: kb_authoring_assistant
    version: 5.0-manifest-aligned
    metric_id: metric.delivered_shipment_count
    implementation_name: Delhivery Delivered Shipment Count
    metric_pattern: filtered_count_or_ratio
    applicability: platform=delhivery; table=zs_observe.delhivery_invoice; account filters via Account Data Binding only
    base_tables:
    - table.zs_observe.delhivery_invoice
    required_columns:
    - column.zs_observe.delhivery_invoice.transaction_type
    semantic_filters:
    - transaction_type='delivered'
    formula_description: COUNT_IF(transaction_type='delivered')
    formula_sql: COUNT_IF(transaction_type='delivered')
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
    - created_date_or_invoice_period
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
  card_id: metric_impl.delhivery_invoice.rto_count
  name: Delhivery RTO Count Implementation
  fields:
    name: Delhivery RTO Count Implementation
    description: RTO Count implementation for Delhivery using delhivery_invoice.
    status: active
    confidence: curated
    source_documents:
    - Logistics KB Doc.docx
    - Cognee KB Design v4.md
    - logistics_gold_std_raw_md_frame_v3.md
    - logistics_gold_std_canonical_card_frame_v5.md
    created_by: kb_authoring_assistant
    updated_by: kb_authoring_assistant
    version: 5.0-manifest-aligned
    metric_id: metric.rto_count
    implementation_name: Delhivery RTO Count
    metric_pattern: filtered_count_or_ratio
    applicability: platform=delhivery; table=zs_observe.delhivery_invoice; account filters via Account Data Binding only
    base_tables:
    - table.zs_observe.delhivery_invoice
    required_columns:
    - column.zs_observe.delhivery_invoice.transaction_type
    semantic_filters:
    - transaction_type='rto'
    formula_description: COUNT_IF(transaction_type='rto')
    formula_sql: COUNT_IF(transaction_type='rto')
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
    - created_date_or_invoice_period
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
  card_id: metric_impl.delhivery_invoice.cod_collected_amount
  name: Delhivery COD Collected Amount Implementation
  fields:
    name: Delhivery COD Collected Amount Implementation
    description: COD Collected Amount implementation for Delhivery using delhivery_invoice.
    status: active
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
    implementation_name: Delhivery COD Collected Amount
    metric_pattern: filtered_count_or_ratio
    applicability: platform=delhivery; table=zs_observe.delhivery_invoice; account filters via Account Data Binding only
    base_tables:
    - table.zs_observe.delhivery_invoice
    required_columns:
    - column.zs_observe.delhivery_invoice.cod_amount
    semantic_filters:
    - order_status='COD'
    formula_description: SUM(cod_amount)
    formula_sql: SUM(cod_amount)
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
    - created_date_or_invoice_period
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
  card_id: metric_impl.delhivery_invoice.average_freight_per_awb
  name: Delhivery Average Freight per AWB Implementation
  fields:
    name: Delhivery Average Freight per AWB Implementation
    description: Average Freight per AWB implementation for Delhivery using delhivery_invoice.
    status: active
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
    implementation_name: Delhivery Average Freight per AWB
    metric_pattern: filtered_count_or_ratio
    applicability: platform=delhivery; table=zs_observe.delhivery_invoice; account filters via Account Data Binding only
    base_tables:
    - table.zs_observe.delhivery_invoice
    required_columns:
    - column.zs_observe.delhivery_invoice.forward_awb_number
    semantic_filters: []
    formula_description: SUM(charge_dl + charge_rto + charge_dto + charge_cod + charge_fsc + charge_fs + charge_fov + charge_air
      + charge_pickup + charge_peak)/NULLIF(COUNT(DISTINCT forward_awb_number),0)
    formula_sql: SUM(charge_dl + charge_rto + charge_dto + charge_cod + charge_fsc + charge_fs + charge_fov + charge_air +
      charge_pickup + charge_peak)/NULLIF(COUNT(DISTINCT forward_awb_number),0)
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
    - created_date_or_invoice_period
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
  card_id: metric_impl.delhivery_settlement.cod_collected_amount
  name: Delhivery COD Collected Amount Implementation
  fields:
    name: Delhivery COD Collected Amount Implementation
    description: COD Collected Amount implementation for Delhivery using delhivery_settlement.
    status: active
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
    implementation_name: Delhivery COD Collected Amount
    metric_pattern: filtered_sum_amount
    applicability: platform=delhivery; table=zs_observe.delhivery_settlement; account filters via Account Data Binding only
    base_tables:
    - table.zs_observe.delhivery_settlement
    required_columns:
    - column.zs_observe.delhivery_settlement.cod_amount
    semantic_filters:
    - txn_type='CR'
    formula_description: SUM(cod_amount)
    formula_sql: SUM(cod_amount)
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
    unit: currency/count/percentage/days_by_metric
    precision: 2_decimal_places
    caveats: Use only with documented amount semantics and grain safety.
    evidence_refs:
    - evidence.logistics_kb_doc
    - evidence.cognee_design_v4
    - evidence.unified_edge_scope
    formula_template_id: formula_template.logistics.filtered_sum_amount
```

```yaml
candidate_card:
  card_type: metric_implementation
  card_id: metric_impl.delhivery_settlement.cod_remitted_amount
  name: Delhivery COD Remitted Amount Implementation
  fields:
    name: Delhivery COD Remitted Amount Implementation
    description: COD Remitted Amount implementation for Delhivery using delhivery_settlement.
    status: active
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
    implementation_name: Delhivery COD Remitted Amount
    metric_pattern: filtered_sum_amount
    applicability: platform=delhivery; table=zs_observe.delhivery_settlement; account filters via Account Data Binding only
    base_tables:
    - table.zs_observe.delhivery_settlement
    required_columns:
    - column.zs_observe.delhivery_settlement.payable
    semantic_filters:
    - txn_type='CR'
    formula_description: SUM(payable)
    formula_sql: SUM(payable)
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
    unit: currency/count/percentage/days_by_metric
    precision: 2_decimal_places
    caveats: Use only with documented amount semantics and grain safety.
    evidence_refs:
    - evidence.logistics_kb_doc
    - evidence.cognee_design_v4
    - evidence.unified_edge_scope
    formula_template_id: formula_template.logistics.filtered_sum_amount
```

```yaml
candidate_card:
  card_type: metric_implementation
  card_id: metric_impl.delhivery_settlement.qr_cod_remitted_amount
  name: Delhivery QR COD Remitted Amount Implementation
  fields:
    name: Delhivery QR COD Remitted Amount Implementation
    description: QR COD Remitted Amount implementation for Delhivery using delhivery_settlement.
    status: active
    confidence: curated
    source_documents:
    - Logistics KB Doc.docx
    - Cognee KB Design v4.md
    - logistics_gold_std_raw_md_frame_v3.md
    - logistics_gold_std_canonical_card_frame_v5.md
    created_by: kb_authoring_assistant
    updated_by: kb_authoring_assistant
    version: 5.0-manifest-aligned
    metric_id: metric.qr_cod_remitted_amount
    implementation_name: Delhivery QR COD Remitted Amount
    metric_pattern: filtered_sum_amount
    applicability: platform=delhivery; table=zs_observe.delhivery_settlement; account filters via Account Data Binding only
    base_tables:
    - table.zs_observe.delhivery_settlement
    required_columns:
    - column.zs_observe.delhivery_settlement.payable
    semantic_filters:
    - payment_mode='QR'
    formula_description: SUM(payable)
    formula_sql: SUM(payable)
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
    unit: currency/count/percentage/days_by_metric
    precision: 2_decimal_places
    caveats: Use only with documented amount semantics and grain safety.
    evidence_refs:
    - evidence.logistics_kb_doc
    - evidence.cognee_design_v4
    - evidence.unified_edge_scope
    formula_template_id: formula_template.logistics.filtered_sum_amount
```

```yaml
candidate_card:
  card_type: metric_implementation
  card_id: metric_impl.delhivery_settlement.payable_amount
  name: Delhivery Payable Amount Implementation
  fields:
    name: Delhivery Payable Amount Implementation
    description: Payable Amount implementation for Delhivery using delhivery_settlement.
    status: active
    confidence: curated
    source_documents:
    - Logistics KB Doc.docx
    - Cognee KB Design v4.md
    - logistics_gold_std_raw_md_frame_v3.md
    - logistics_gold_std_canonical_card_frame_v5.md
    created_by: kb_authoring_assistant
    updated_by: kb_authoring_assistant
    version: 5.0-manifest-aligned
    metric_id: metric.payable_amount
    implementation_name: Delhivery Payable Amount
    metric_pattern: filtered_sum_amount
    applicability: platform=delhivery; table=zs_observe.delhivery_settlement; account filters via Account Data Binding only
    base_tables:
    - table.zs_observe.delhivery_settlement
    required_columns:
    - column.zs_observe.delhivery_settlement.payable
    semantic_filters:
    - txn_type='CR'
    formula_description: SUM(payable)
    formula_sql: SUM(payable)
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
    unit: currency/count/percentage/days_by_metric
    precision: 2_decimal_places
    caveats: Use only with documented amount semantics and grain safety.
    evidence_refs:
    - evidence.logistics_kb_doc
    - evidence.cognee_design_v4
    - evidence.unified_edge_scope
    formula_template_id: formula_template.logistics.filtered_sum_amount
```

```yaml
candidate_card:
  card_type: metric_implementation
  card_id: metric_impl.delhivery_settlement.cod_gap_amount
  name: Delhivery COD Gap Amount Implementation
  fields:
    name: Delhivery COD Gap Amount Implementation
    description: COD Gap Amount implementation for Delhivery using delhivery_settlement.
    status: active
    confidence: curated
    source_documents:
    - Logistics KB Doc.docx
    - Cognee KB Design v4.md
    - logistics_gold_std_raw_md_frame_v3.md
    - logistics_gold_std_canonical_card_frame_v5.md
    created_by: kb_authoring_assistant
    updated_by: kb_authoring_assistant
    version: 5.0-manifest-aligned
    metric_id: metric.cod_gap_amount
    implementation_name: Delhivery COD Gap Amount
    metric_pattern: filtered_sum_amount
    applicability: platform=delhivery; table=zs_observe.delhivery_settlement; account filters via Account Data Binding only
    base_tables:
    - table.zs_observe.delhivery_settlement
    required_columns:
    - column.zs_observe.delhivery_settlement.cod_amount
    - column.zs_observe.delhivery_settlement.payable
    semantic_filters:
    - txn_type='CR'
    formula_description: SUM(cod_amount)-SUM(payable)
    formula_sql: SUM(cod_amount)-SUM(payable)
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
    unit: currency/count/percentage/days_by_metric
    precision: 2_decimal_places
    caveats: Use only with documented amount semantics and grain safety.
    evidence_refs:
    - evidence.logistics_kb_doc
    - evidence.cognee_design_v4
    - evidence.unified_edge_scope
    formula_template_id: formula_template.logistics.filtered_sum_amount
```

```yaml
candidate_card:
  card_type: metric_implementation
  card_id: metric_impl.delhivery_settlement.settlement_batch_count
  name: Delhivery Settlement Batch Count Implementation
  fields:
    name: Delhivery Settlement Batch Count Implementation
    description: Settlement Batch Count implementation for Delhivery using delhivery_settlement.
    status: active
    confidence: curated
    source_documents:
    - Logistics KB Doc.docx
    - Cognee KB Design v4.md
    - logistics_gold_std_raw_md_frame_v3.md
    - logistics_gold_std_canonical_card_frame_v5.md
    created_by: kb_authoring_assistant
    updated_by: kb_authoring_assistant
    version: 5.0-manifest-aligned
    metric_id: metric.settlement_batch_count
    implementation_name: Delhivery Settlement Batch Count
    metric_pattern: filtered_sum_amount
    applicability: platform=delhivery; table=zs_observe.delhivery_settlement; account filters via Account Data Binding only
    base_tables:
    - table.zs_observe.delhivery_settlement
    required_columns:
    - column.zs_observe.delhivery_settlement.remittance_number
    semantic_filters: []
    formula_description: COUNT(DISTINCT remittance_number)
    formula_sql: COUNT(DISTINCT remittance_number)
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
    unit: currency/count/percentage/days_by_metric
    precision: 2_decimal_places
    caveats: Use only with documented amount semantics and grain safety.
    evidence_refs:
    - evidence.logistics_kb_doc
    - evidence.cognee_design_v4
    - evidence.unified_edge_scope
    formula_template_id: formula_template.logistics.filtered_sum_amount
```

```yaml
candidate_card:
  card_type: metric_implementation
  card_id: metric_impl.delhivery_settlement.unique_awb_count
  name: Delhivery Unique AWB Count Implementation
  fields:
    name: Delhivery Unique AWB Count Implementation
    description: Unique AWB Count implementation for Delhivery using delhivery_settlement.
    status: active
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
    implementation_name: Delhivery Unique AWB Count
    metric_pattern: filtered_sum_amount
    applicability: platform=delhivery; table=zs_observe.delhivery_settlement; account filters via Account Data Binding only
    base_tables:
    - table.zs_observe.delhivery_settlement
    required_columns:
    - column.zs_observe.delhivery_settlement.waybill_num
    semantic_filters: []
    formula_description: COUNT(DISTINCT waybill_num)
    formula_sql: COUNT(DISTINCT waybill_num)
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
    unit: currency/count/percentage/days_by_metric
    precision: 2_decimal_places
    caveats: Use only with documented amount semantics and grain safety.
    evidence_refs:
    - evidence.logistics_kb_doc
    - evidence.cognee_design_v4
    - evidence.unified_edge_scope
    formula_template_id: formula_template.logistics.filtered_sum_amount
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
  edge_id: edge.metric.cod_expected_amount.belongs_to_domain.domain.logistics_reconciliation
  edge_type: BELONGS_TO_DOMAIN
  source: metric.cod_expected_amount
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
  edge_id: edge.metric.cod_gap_amount.belongs_to_domain.domain.logistics_reconciliation
  edge_type: BELONGS_TO_DOMAIN
  source: metric.cod_gap_amount
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
  edge_id: edge.metric.declared_product_value.belongs_to_domain.domain.logistics_reconciliation
  edge_type: BELONGS_TO_DOMAIN
  source: metric.declared_product_value
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
  edge_id: edge.metric.delivered_shipment_count.belongs_to_domain.domain.logistics_reconciliation
  edge_type: BELONGS_TO_DOMAIN
  source: metric.delivered_shipment_count
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
  edge_id: edge.metric.dto_freight_amount.belongs_to_domain.domain.logistics_reconciliation
  edge_type: BELONGS_TO_DOMAIN
  source: metric.dto_freight_amount
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
  edge_id: edge.metric.fov_insurance_amount.belongs_to_domain.domain.logistics_reconciliation
  edge_type: BELONGS_TO_DOMAIN
  source: metric.fov_insurance_amount
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
  edge_id: edge.metric.payable_amount.belongs_to_domain.domain.logistics_reconciliation
  edge_type: BELONGS_TO_DOMAIN
  source: metric.payable_amount
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
  edge_id: edge.metric.peak_surcharge_amount.belongs_to_domain.domain.logistics_reconciliation
  edge_type: BELONGS_TO_DOMAIN
  source: metric.peak_surcharge_amount
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
  edge_id: edge.metric.pickup_charge_amount.belongs_to_domain.domain.logistics_reconciliation
  edge_type: BELONGS_TO_DOMAIN
  source: metric.pickup_charge_amount
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
  edge_id: edge.metric.qr_cod_remitted_amount.belongs_to_domain.domain.logistics_reconciliation
  edge_type: BELONGS_TO_DOMAIN
  source: metric.qr_cod_remitted_amount
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
  edge_id: edge.metric.rto_count.belongs_to_domain.domain.logistics_reconciliation
  edge_type: BELONGS_TO_DOMAIN
  source: metric.rto_count
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
  edge_id: edge.metric.settlement_batch_count.belongs_to_domain.domain.logistics_reconciliation
  edge_type: BELONGS_TO_DOMAIN
  source: metric.settlement_batch_count
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
  edge_id: edge.metric.shipment_count.belongs_to_domain.domain.logistics_reconciliation
  edge_type: BELONGS_TO_DOMAIN
  source: metric.shipment_count
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
  edge_id: edge.platform_context.delhivery.in.belongs_to_platform.platform.delhivery
  edge_type: BELONGS_TO_PLATFORM
  source: platform_context.delhivery.in
  target: platform.delhivery
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
  edge_id: edge.platform.delhivery.has_platform_context.platform_context.delhivery.in
  edge_type: HAS_PLATFORM_CONTEXT
  source: platform.delhivery
  target: platform_context.delhivery.in
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
    materialized_from: edge.platform_context.delhivery.in.belongs_to_platform.platform.delhivery
```

```yaml
candidate_edge:
  edge_id: edge.table.zs_observe.delhivery_invoice.sourced_from_platform.platform.delhivery
  edge_type: SOURCED_FROM_PLATFORM
  source: table.zs_observe.delhivery_invoice
  target: platform.delhivery
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
  edge_id: edge.table.zs_observe.delhivery_invoice.applies_to_platform.platform.delhivery
  edge_type: APPLIES_TO_PLATFORM
  source: table.zs_observe.delhivery_invoice
  target: platform.delhivery
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
  edge_id: edge.table.zs_observe.delhivery_invoice.has_column.column.zs_observe.delhivery_invoice.order_id
  edge_type: HAS_COLUMN
  source: table.zs_observe.delhivery_invoice
  target: column.zs_observe.delhivery_invoice.order_id
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
  edge_id: edge.column.zs_observe.delhivery_invoice.order_id.belongs_to_table.table.zs_observe.delhivery_invoice
  edge_type: BELONGS_TO_TABLE
  source: column.zs_observe.delhivery_invoice.order_id
  target: table.zs_observe.delhivery_invoice
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
    materialized_from: edge.table.zs_observe.delhivery_invoice.has_column.column.zs_observe.delhivery_invoice.order_id
```

```yaml
candidate_edge:
  edge_id: edge.table.zs_observe.delhivery_invoice.has_column.column.zs_observe.delhivery_invoice.forward_awb_number
  edge_type: HAS_COLUMN
  source: table.zs_observe.delhivery_invoice
  target: column.zs_observe.delhivery_invoice.forward_awb_number
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
  edge_id: edge.column.zs_observe.delhivery_invoice.forward_awb_number.belongs_to_table.table.zs_observe.delhivery_invoice
  edge_type: BELONGS_TO_TABLE
  source: column.zs_observe.delhivery_invoice.forward_awb_number
  target: table.zs_observe.delhivery_invoice
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
    materialized_from: edge.table.zs_observe.delhivery_invoice.has_column.column.zs_observe.delhivery_invoice.forward_awb_number
```

```yaml
candidate_edge:
  edge_id: edge.table.zs_observe.delhivery_invoice.has_column.column.zs_observe.delhivery_invoice.return_awb_number
  edge_type: HAS_COLUMN
  source: table.zs_observe.delhivery_invoice
  target: column.zs_observe.delhivery_invoice.return_awb_number
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
  edge_id: edge.column.zs_observe.delhivery_invoice.return_awb_number.belongs_to_table.table.zs_observe.delhivery_invoice
  edge_type: BELONGS_TO_TABLE
  source: column.zs_observe.delhivery_invoice.return_awb_number
  target: table.zs_observe.delhivery_invoice
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
    materialized_from: edge.table.zs_observe.delhivery_invoice.has_column.column.zs_observe.delhivery_invoice.return_awb_number
```

```yaml
candidate_edge:
  edge_id: edge.table.zs_observe.delhivery_invoice.has_column.column.zs_observe.delhivery_invoice.transaction_type
  edge_type: HAS_COLUMN
  source: table.zs_observe.delhivery_invoice
  target: column.zs_observe.delhivery_invoice.transaction_type
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
  edge_id: edge.column.zs_observe.delhivery_invoice.transaction_type.belongs_to_table.table.zs_observe.delhivery_invoice
  edge_type: BELONGS_TO_TABLE
  source: column.zs_observe.delhivery_invoice.transaction_type
  target: table.zs_observe.delhivery_invoice
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
    materialized_from: edge.table.zs_observe.delhivery_invoice.has_column.column.zs_observe.delhivery_invoice.transaction_type
```

```yaml
candidate_edge:
  edge_id: edge.table.zs_observe.delhivery_invoice.has_column.column.zs_observe.delhivery_invoice.order_status
  edge_type: HAS_COLUMN
  source: table.zs_observe.delhivery_invoice
  target: column.zs_observe.delhivery_invoice.order_status
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
  edge_id: edge.column.zs_observe.delhivery_invoice.order_status.belongs_to_table.table.zs_observe.delhivery_invoice
  edge_type: BELONGS_TO_TABLE
  source: column.zs_observe.delhivery_invoice.order_status
  target: table.zs_observe.delhivery_invoice
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
    materialized_from: edge.table.zs_observe.delhivery_invoice.has_column.column.zs_observe.delhivery_invoice.order_status
```

```yaml
candidate_edge:
  edge_id: edge.table.zs_observe.delhivery_invoice.has_column.column.zs_observe.delhivery_invoice.invoice_number
  edge_type: HAS_COLUMN
  source: table.zs_observe.delhivery_invoice
  target: column.zs_observe.delhivery_invoice.invoice_number
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
  edge_id: edge.column.zs_observe.delhivery_invoice.invoice_number.belongs_to_table.table.zs_observe.delhivery_invoice
  edge_type: BELONGS_TO_TABLE
  source: column.zs_observe.delhivery_invoice.invoice_number
  target: table.zs_observe.delhivery_invoice
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
    materialized_from: edge.table.zs_observe.delhivery_invoice.has_column.column.zs_observe.delhivery_invoice.invoice_number
```

```yaml
candidate_edge:
  edge_id: edge.table.zs_observe.delhivery_invoice.has_column.column.zs_observe.delhivery_invoice.charged_amount
  edge_type: HAS_COLUMN
  source: table.zs_observe.delhivery_invoice
  target: column.zs_observe.delhivery_invoice.charged_amount
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
  edge_id: edge.column.zs_observe.delhivery_invoice.charged_amount.belongs_to_table.table.zs_observe.delhivery_invoice
  edge_type: BELONGS_TO_TABLE
  source: column.zs_observe.delhivery_invoice.charged_amount
  target: table.zs_observe.delhivery_invoice
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
    materialized_from: edge.table.zs_observe.delhivery_invoice.has_column.column.zs_observe.delhivery_invoice.charged_amount
```

```yaml
candidate_edge:
  edge_id: edge.table.zs_observe.delhivery_invoice.has_column.column.zs_observe.delhivery_invoice.cod_amount
  edge_type: HAS_COLUMN
  source: table.zs_observe.delhivery_invoice
  target: column.zs_observe.delhivery_invoice.cod_amount
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
  edge_id: edge.column.zs_observe.delhivery_invoice.cod_amount.belongs_to_table.table.zs_observe.delhivery_invoice
  edge_type: BELONGS_TO_TABLE
  source: column.zs_observe.delhivery_invoice.cod_amount
  target: table.zs_observe.delhivery_invoice
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
    materialized_from: edge.table.zs_observe.delhivery_invoice.has_column.column.zs_observe.delhivery_invoice.cod_amount
```

```yaml
candidate_edge:
  edge_id: edge.table.zs_observe.delhivery_invoice.has_column.column.zs_observe.delhivery_invoice.order_value
  edge_type: HAS_COLUMN
  source: table.zs_observe.delhivery_invoice
  target: column.zs_observe.delhivery_invoice.order_value
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
  edge_id: edge.column.zs_observe.delhivery_invoice.order_value.belongs_to_table.table.zs_observe.delhivery_invoice
  edge_type: BELONGS_TO_TABLE
  source: column.zs_observe.delhivery_invoice.order_value
  target: table.zs_observe.delhivery_invoice
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
    materialized_from: edge.table.zs_observe.delhivery_invoice.has_column.column.zs_observe.delhivery_invoice.order_value
```

```yaml
candidate_edge:
  edge_id: edge.table.zs_observe.delhivery_invoice.has_column.column.zs_observe.delhivery_invoice.product_value
  edge_type: HAS_COLUMN
  source: table.zs_observe.delhivery_invoice
  target: column.zs_observe.delhivery_invoice.product_value
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
  edge_id: edge.column.zs_observe.delhivery_invoice.product_value.belongs_to_table.table.zs_observe.delhivery_invoice
  edge_type: BELONGS_TO_TABLE
  source: column.zs_observe.delhivery_invoice.product_value
  target: table.zs_observe.delhivery_invoice
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
    materialized_from: edge.table.zs_observe.delhivery_invoice.has_column.column.zs_observe.delhivery_invoice.product_value
```

```yaml
candidate_edge:
  edge_id: edge.table.zs_observe.delhivery_invoice.has_column.column.zs_observe.delhivery_invoice.charge_dl
  edge_type: HAS_COLUMN
  source: table.zs_observe.delhivery_invoice
  target: column.zs_observe.delhivery_invoice.charge_dl
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
  edge_id: edge.column.zs_observe.delhivery_invoice.charge_dl.belongs_to_table.table.zs_observe.delhivery_invoice
  edge_type: BELONGS_TO_TABLE
  source: column.zs_observe.delhivery_invoice.charge_dl
  target: table.zs_observe.delhivery_invoice
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
    materialized_from: edge.table.zs_observe.delhivery_invoice.has_column.column.zs_observe.delhivery_invoice.charge_dl
```

```yaml
candidate_edge:
  edge_id: edge.table.zs_observe.delhivery_invoice.has_column.column.zs_observe.delhivery_invoice.charge_rto
  edge_type: HAS_COLUMN
  source: table.zs_observe.delhivery_invoice
  target: column.zs_observe.delhivery_invoice.charge_rto
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
  edge_id: edge.column.zs_observe.delhivery_invoice.charge_rto.belongs_to_table.table.zs_observe.delhivery_invoice
  edge_type: BELONGS_TO_TABLE
  source: column.zs_observe.delhivery_invoice.charge_rto
  target: table.zs_observe.delhivery_invoice
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
    materialized_from: edge.table.zs_observe.delhivery_invoice.has_column.column.zs_observe.delhivery_invoice.charge_rto
```

```yaml
candidate_edge:
  edge_id: edge.table.zs_observe.delhivery_invoice.has_column.column.zs_observe.delhivery_invoice.charge_dto
  edge_type: HAS_COLUMN
  source: table.zs_observe.delhivery_invoice
  target: column.zs_observe.delhivery_invoice.charge_dto
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
  edge_id: edge.column.zs_observe.delhivery_invoice.charge_dto.belongs_to_table.table.zs_observe.delhivery_invoice
  edge_type: BELONGS_TO_TABLE
  source: column.zs_observe.delhivery_invoice.charge_dto
  target: table.zs_observe.delhivery_invoice
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
    materialized_from: edge.table.zs_observe.delhivery_invoice.has_column.column.zs_observe.delhivery_invoice.charge_dto
```

```yaml
candidate_edge:
  edge_id: edge.table.zs_observe.delhivery_invoice.has_column.column.zs_observe.delhivery_invoice.charge_cod
  edge_type: HAS_COLUMN
  source: table.zs_observe.delhivery_invoice
  target: column.zs_observe.delhivery_invoice.charge_cod
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
  edge_id: edge.column.zs_observe.delhivery_invoice.charge_cod.belongs_to_table.table.zs_observe.delhivery_invoice
  edge_type: BELONGS_TO_TABLE
  source: column.zs_observe.delhivery_invoice.charge_cod
  target: table.zs_observe.delhivery_invoice
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
    materialized_from: edge.table.zs_observe.delhivery_invoice.has_column.column.zs_observe.delhivery_invoice.charge_cod
```

```yaml
candidate_edge:
  edge_id: edge.table.zs_observe.delhivery_invoice.has_column.column.zs_observe.delhivery_invoice.charge_fsc
  edge_type: HAS_COLUMN
  source: table.zs_observe.delhivery_invoice
  target: column.zs_observe.delhivery_invoice.charge_fsc
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
  edge_id: edge.column.zs_observe.delhivery_invoice.charge_fsc.belongs_to_table.table.zs_observe.delhivery_invoice
  edge_type: BELONGS_TO_TABLE
  source: column.zs_observe.delhivery_invoice.charge_fsc
  target: table.zs_observe.delhivery_invoice
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
    materialized_from: edge.table.zs_observe.delhivery_invoice.has_column.column.zs_observe.delhivery_invoice.charge_fsc
```

```yaml
candidate_edge:
  edge_id: edge.table.zs_observe.delhivery_invoice.has_column.column.zs_observe.delhivery_invoice.charge_fs
  edge_type: HAS_COLUMN
  source: table.zs_observe.delhivery_invoice
  target: column.zs_observe.delhivery_invoice.charge_fs
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
  edge_id: edge.column.zs_observe.delhivery_invoice.charge_fs.belongs_to_table.table.zs_observe.delhivery_invoice
  edge_type: BELONGS_TO_TABLE
  source: column.zs_observe.delhivery_invoice.charge_fs
  target: table.zs_observe.delhivery_invoice
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
    materialized_from: edge.table.zs_observe.delhivery_invoice.has_column.column.zs_observe.delhivery_invoice.charge_fs
```

```yaml
candidate_edge:
  edge_id: edge.table.zs_observe.delhivery_invoice.has_column.column.zs_observe.delhivery_invoice.charge_fov
  edge_type: HAS_COLUMN
  source: table.zs_observe.delhivery_invoice
  target: column.zs_observe.delhivery_invoice.charge_fov
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
  edge_id: edge.column.zs_observe.delhivery_invoice.charge_fov.belongs_to_table.table.zs_observe.delhivery_invoice
  edge_type: BELONGS_TO_TABLE
  source: column.zs_observe.delhivery_invoice.charge_fov
  target: table.zs_observe.delhivery_invoice
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
    materialized_from: edge.table.zs_observe.delhivery_invoice.has_column.column.zs_observe.delhivery_invoice.charge_fov
```

```yaml
candidate_edge:
  edge_id: edge.table.zs_observe.delhivery_invoice.has_column.column.zs_observe.delhivery_invoice.charge_air
  edge_type: HAS_COLUMN
  source: table.zs_observe.delhivery_invoice
  target: column.zs_observe.delhivery_invoice.charge_air
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
  edge_id: edge.column.zs_observe.delhivery_invoice.charge_air.belongs_to_table.table.zs_observe.delhivery_invoice
  edge_type: BELONGS_TO_TABLE
  source: column.zs_observe.delhivery_invoice.charge_air
  target: table.zs_observe.delhivery_invoice
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
    materialized_from: edge.table.zs_observe.delhivery_invoice.has_column.column.zs_observe.delhivery_invoice.charge_air
```

```yaml
candidate_edge:
  edge_id: edge.table.zs_observe.delhivery_invoice.has_column.column.zs_observe.delhivery_invoice.charge_pickup
  edge_type: HAS_COLUMN
  source: table.zs_observe.delhivery_invoice
  target: column.zs_observe.delhivery_invoice.charge_pickup
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
  edge_id: edge.column.zs_observe.delhivery_invoice.charge_pickup.belongs_to_table.table.zs_observe.delhivery_invoice
  edge_type: BELONGS_TO_TABLE
  source: column.zs_observe.delhivery_invoice.charge_pickup
  target: table.zs_observe.delhivery_invoice
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
    materialized_from: edge.table.zs_observe.delhivery_invoice.has_column.column.zs_observe.delhivery_invoice.charge_pickup
```

```yaml
candidate_edge:
  edge_id: edge.table.zs_observe.delhivery_invoice.has_column.column.zs_observe.delhivery_invoice.charge_peak
  edge_type: HAS_COLUMN
  source: table.zs_observe.delhivery_invoice
  target: column.zs_observe.delhivery_invoice.charge_peak
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
  edge_id: edge.column.zs_observe.delhivery_invoice.charge_peak.belongs_to_table.table.zs_observe.delhivery_invoice
  edge_type: BELONGS_TO_TABLE
  source: column.zs_observe.delhivery_invoice.charge_peak
  target: table.zs_observe.delhivery_invoice
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
    materialized_from: edge.table.zs_observe.delhivery_invoice.has_column.column.zs_observe.delhivery_invoice.charge_peak
```

```yaml
candidate_edge:
  edge_id: edge.table.zs_observe.delhivery_invoice.has_column.column.zs_observe.delhivery_invoice.charge_reattempt
  edge_type: HAS_COLUMN
  source: table.zs_observe.delhivery_invoice
  target: column.zs_observe.delhivery_invoice.charge_reattempt
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
  edge_id: edge.column.zs_observe.delhivery_invoice.charge_reattempt.belongs_to_table.table.zs_observe.delhivery_invoice
  edge_type: BELONGS_TO_TABLE
  source: column.zs_observe.delhivery_invoice.charge_reattempt
  target: table.zs_observe.delhivery_invoice
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
    materialized_from: edge.table.zs_observe.delhivery_invoice.has_column.column.zs_observe.delhivery_invoice.charge_reattempt
```

```yaml
candidate_edge:
  edge_id: edge.table.zs_observe.delhivery_invoice.has_column.column.zs_observe.delhivery_invoice.charge_wod
  edge_type: HAS_COLUMN
  source: table.zs_observe.delhivery_invoice
  target: column.zs_observe.delhivery_invoice.charge_wod
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
  edge_id: edge.column.zs_observe.delhivery_invoice.charge_wod.belongs_to_table.table.zs_observe.delhivery_invoice
  edge_type: BELONGS_TO_TABLE
  source: column.zs_observe.delhivery_invoice.charge_wod
  target: table.zs_observe.delhivery_invoice
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
    materialized_from: edge.table.zs_observe.delhivery_invoice.has_column.column.zs_observe.delhivery_invoice.charge_wod
```

```yaml
candidate_edge:
  edge_id: edge.table.zs_observe.delhivery_invoice.has_column.column.zs_observe.delhivery_invoice.charged_weight
  edge_type: HAS_COLUMN
  source: table.zs_observe.delhivery_invoice
  target: column.zs_observe.delhivery_invoice.charged_weight
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
  edge_id: edge.column.zs_observe.delhivery_invoice.charged_weight.belongs_to_table.table.zs_observe.delhivery_invoice
  edge_type: BELONGS_TO_TABLE
  source: column.zs_observe.delhivery_invoice.charged_weight
  target: table.zs_observe.delhivery_invoice
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
    materialized_from: edge.table.zs_observe.delhivery_invoice.has_column.column.zs_observe.delhivery_invoice.charged_weight
```

```yaml
candidate_edge:
  edge_id: edge.table.zs_observe.delhivery_invoice.has_column.column.zs_observe.delhivery_invoice.zone
  edge_type: HAS_COLUMN
  source: table.zs_observe.delhivery_invoice
  target: column.zs_observe.delhivery_invoice.zone
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
  edge_id: edge.column.zs_observe.delhivery_invoice.zone.belongs_to_table.table.zs_observe.delhivery_invoice
  edge_type: BELONGS_TO_TABLE
  source: column.zs_observe.delhivery_invoice.zone
  target: table.zs_observe.delhivery_invoice
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
    materialized_from: edge.table.zs_observe.delhivery_invoice.has_column.column.zs_observe.delhivery_invoice.zone
```

```yaml
candidate_edge:
  edge_id: edge.table.zs_observe.delhivery_invoice.has_column.column.zs_observe.delhivery_invoice.zen_vendor_payout_forward_charge
  edge_type: HAS_COLUMN
  source: table.zs_observe.delhivery_invoice
  target: column.zs_observe.delhivery_invoice.zen_vendor_payout_forward_charge
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
  edge_id: edge.column.zs_observe.delhivery_invoice.zen_vendor_payout_forward_charge.belongs_to_table.table.zs_observe.delhivery_invoice
  edge_type: BELONGS_TO_TABLE
  source: column.zs_observe.delhivery_invoice.zen_vendor_payout_forward_charge
  target: table.zs_observe.delhivery_invoice
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
    materialized_from: edge.table.zs_observe.delhivery_invoice.has_column.column.zs_observe.delhivery_invoice.zen_vendor_payout_forward_charge
```

```yaml
candidate_edge:
  edge_id: edge.table.zs_observe.delhivery_invoice.has_column.column.zs_observe.delhivery_invoice.zen_vendor_payout_rto_charge
  edge_type: HAS_COLUMN
  source: table.zs_observe.delhivery_invoice
  target: column.zs_observe.delhivery_invoice.zen_vendor_payout_rto_charge
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
  edge_id: edge.column.zs_observe.delhivery_invoice.zen_vendor_payout_rto_charge.belongs_to_table.table.zs_observe.delhivery_invoice
  edge_type: BELONGS_TO_TABLE
  source: column.zs_observe.delhivery_invoice.zen_vendor_payout_rto_charge
  target: table.zs_observe.delhivery_invoice
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
    materialized_from: edge.table.zs_observe.delhivery_invoice.has_column.column.zs_observe.delhivery_invoice.zen_vendor_payout_rto_charge
```

```yaml
candidate_edge:
  edge_id: edge.table.zs_observe.delhivery_invoice.has_column.column.zs_observe.delhivery_invoice.zen_vendor_payout_cod_charge
  edge_type: HAS_COLUMN
  source: table.zs_observe.delhivery_invoice
  target: column.zs_observe.delhivery_invoice.zen_vendor_payout_cod_charge
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
  edge_id: edge.column.zs_observe.delhivery_invoice.zen_vendor_payout_cod_charge.belongs_to_table.table.zs_observe.delhivery_invoice
  edge_type: BELONGS_TO_TABLE
  source: column.zs_observe.delhivery_invoice.zen_vendor_payout_cod_charge
  target: table.zs_observe.delhivery_invoice
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
    materialized_from: edge.table.zs_observe.delhivery_invoice.has_column.column.zs_observe.delhivery_invoice.zen_vendor_payout_cod_charge
```

```yaml
candidate_edge:
  edge_id: edge.table.zs_observe.delhivery_invoice.has_column.column.zs_observe.delhivery_invoice.zen_vendor_payout_dto_charge
  edge_type: HAS_COLUMN
  source: table.zs_observe.delhivery_invoice
  target: column.zs_observe.delhivery_invoice.zen_vendor_payout_dto_charge
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
  edge_id: edge.column.zs_observe.delhivery_invoice.zen_vendor_payout_dto_charge.belongs_to_table.table.zs_observe.delhivery_invoice
  edge_type: BELONGS_TO_TABLE
  source: column.zs_observe.delhivery_invoice.zen_vendor_payout_dto_charge
  target: table.zs_observe.delhivery_invoice
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
    materialized_from: edge.table.zs_observe.delhivery_invoice.has_column.column.zs_observe.delhivery_invoice.zen_vendor_payout_dto_charge
```

```yaml
candidate_edge:
  edge_id: edge.table.zs_observe.delhivery_invoice.has_column.column.zs_observe.delhivery_invoice.tax_cgst_amount
  edge_type: HAS_COLUMN
  source: table.zs_observe.delhivery_invoice
  target: column.zs_observe.delhivery_invoice.tax_cgst_amount
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
  edge_id: edge.column.zs_observe.delhivery_invoice.tax_cgst_amount.belongs_to_table.table.zs_observe.delhivery_invoice
  edge_type: BELONGS_TO_TABLE
  source: column.zs_observe.delhivery_invoice.tax_cgst_amount
  target: table.zs_observe.delhivery_invoice
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
    materialized_from: edge.table.zs_observe.delhivery_invoice.has_column.column.zs_observe.delhivery_invoice.tax_cgst_amount
```

```yaml
candidate_edge:
  edge_id: edge.table.zs_observe.delhivery_invoice.has_column.column.zs_observe.delhivery_invoice.tax_sgst_amount
  edge_type: HAS_COLUMN
  source: table.zs_observe.delhivery_invoice
  target: column.zs_observe.delhivery_invoice.tax_sgst_amount
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
  edge_id: edge.column.zs_observe.delhivery_invoice.tax_sgst_amount.belongs_to_table.table.zs_observe.delhivery_invoice
  edge_type: BELONGS_TO_TABLE
  source: column.zs_observe.delhivery_invoice.tax_sgst_amount
  target: table.zs_observe.delhivery_invoice
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
    materialized_from: edge.table.zs_observe.delhivery_invoice.has_column.column.zs_observe.delhivery_invoice.tax_sgst_amount
```

```yaml
candidate_edge:
  edge_id: edge.table.zs_observe.delhivery_invoice.has_column.column.zs_observe.delhivery_invoice.tax_igst_amount
  edge_type: HAS_COLUMN
  source: table.zs_observe.delhivery_invoice
  target: column.zs_observe.delhivery_invoice.tax_igst_amount
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
  edge_id: edge.column.zs_observe.delhivery_invoice.tax_igst_amount.belongs_to_table.table.zs_observe.delhivery_invoice
  edge_type: BELONGS_TO_TABLE
  source: column.zs_observe.delhivery_invoice.tax_igst_amount
  target: table.zs_observe.delhivery_invoice
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
    materialized_from: edge.table.zs_observe.delhivery_invoice.has_column.column.zs_observe.delhivery_invoice.tax_igst_amount
```

```yaml
candidate_edge:
  edge_id: edge.table.zs_observe.delhivery_invoice.has_column.column.zs_observe.delhivery_invoice.is_active
  edge_type: HAS_COLUMN
  source: table.zs_observe.delhivery_invoice
  target: column.zs_observe.delhivery_invoice.is_active
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
  edge_id: edge.column.zs_observe.delhivery_invoice.is_active.belongs_to_table.table.zs_observe.delhivery_invoice
  edge_type: BELONGS_TO_TABLE
  source: column.zs_observe.delhivery_invoice.is_active
  target: table.zs_observe.delhivery_invoice
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
    materialized_from: edge.table.zs_observe.delhivery_invoice.has_column.column.zs_observe.delhivery_invoice.is_active
```

```yaml
candidate_edge:
  edge_id: edge.table.zs_observe.delhivery_invoice.has_column.column.zs_observe.delhivery_invoice.group_level_id
  edge_type: HAS_COLUMN
  source: table.zs_observe.delhivery_invoice
  target: column.zs_observe.delhivery_invoice.group_level_id
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
  edge_id: edge.column.zs_observe.delhivery_invoice.group_level_id.belongs_to_table.table.zs_observe.delhivery_invoice
  edge_type: BELONGS_TO_TABLE
  source: column.zs_observe.delhivery_invoice.group_level_id
  target: table.zs_observe.delhivery_invoice
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
    materialized_from: edge.table.zs_observe.delhivery_invoice.has_column.column.zs_observe.delhivery_invoice.group_level_id
```

```yaml
candidate_edge:
  edge_id: edge.table.zs_observe.delhivery_settlement.sourced_from_platform.platform.delhivery
  edge_type: SOURCED_FROM_PLATFORM
  source: table.zs_observe.delhivery_settlement
  target: platform.delhivery
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
  edge_id: edge.table.zs_observe.delhivery_settlement.applies_to_platform.platform.delhivery
  edge_type: APPLIES_TO_PLATFORM
  source: table.zs_observe.delhivery_settlement
  target: platform.delhivery
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
  edge_id: edge.table.zs_observe.delhivery_settlement.has_column.column.zs_observe.delhivery_settlement.order_id
  edge_type: HAS_COLUMN
  source: table.zs_observe.delhivery_settlement
  target: column.zs_observe.delhivery_settlement.order_id
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
  edge_id: edge.column.zs_observe.delhivery_settlement.order_id.belongs_to_table.table.zs_observe.delhivery_settlement
  edge_type: BELONGS_TO_TABLE
  source: column.zs_observe.delhivery_settlement.order_id
  target: table.zs_observe.delhivery_settlement
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
    materialized_from: edge.table.zs_observe.delhivery_settlement.has_column.column.zs_observe.delhivery_settlement.order_id
```

```yaml
candidate_edge:
  edge_id: edge.table.zs_observe.delhivery_settlement.has_column.column.zs_observe.delhivery_settlement.waybill_num
  edge_type: HAS_COLUMN
  source: table.zs_observe.delhivery_settlement
  target: column.zs_observe.delhivery_settlement.waybill_num
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
  edge_id: edge.column.zs_observe.delhivery_settlement.waybill_num.belongs_to_table.table.zs_observe.delhivery_settlement
  edge_type: BELONGS_TO_TABLE
  source: column.zs_observe.delhivery_settlement.waybill_num
  target: table.zs_observe.delhivery_settlement
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
    materialized_from: edge.table.zs_observe.delhivery_settlement.has_column.column.zs_observe.delhivery_settlement.waybill_num
```

```yaml
candidate_edge:
  edge_id: edge.table.zs_observe.delhivery_settlement.has_column.column.zs_observe.delhivery_settlement.waybill_number
  edge_type: HAS_COLUMN
  source: table.zs_observe.delhivery_settlement
  target: column.zs_observe.delhivery_settlement.waybill_number
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
  edge_id: edge.column.zs_observe.delhivery_settlement.waybill_number.belongs_to_table.table.zs_observe.delhivery_settlement
  edge_type: BELONGS_TO_TABLE
  source: column.zs_observe.delhivery_settlement.waybill_number
  target: table.zs_observe.delhivery_settlement
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
    materialized_from: edge.table.zs_observe.delhivery_settlement.has_column.column.zs_observe.delhivery_settlement.waybill_number
```

```yaml
candidate_edge:
  edge_id: edge.table.zs_observe.delhivery_settlement.has_column.column.zs_observe.delhivery_settlement.txn_type
  edge_type: HAS_COLUMN
  source: table.zs_observe.delhivery_settlement
  target: column.zs_observe.delhivery_settlement.txn_type
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
  edge_id: edge.column.zs_observe.delhivery_settlement.txn_type.belongs_to_table.table.zs_observe.delhivery_settlement
  edge_type: BELONGS_TO_TABLE
  source: column.zs_observe.delhivery_settlement.txn_type
  target: table.zs_observe.delhivery_settlement
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
    materialized_from: edge.table.zs_observe.delhivery_settlement.has_column.column.zs_observe.delhivery_settlement.txn_type
```

```yaml
candidate_edge:
  edge_id: edge.table.zs_observe.delhivery_settlement.has_column.column.zs_observe.delhivery_settlement.order_status
  edge_type: HAS_COLUMN
  source: table.zs_observe.delhivery_settlement
  target: column.zs_observe.delhivery_settlement.order_status
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
  edge_id: edge.column.zs_observe.delhivery_settlement.order_status.belongs_to_table.table.zs_observe.delhivery_settlement
  edge_type: BELONGS_TO_TABLE
  source: column.zs_observe.delhivery_settlement.order_status
  target: table.zs_observe.delhivery_settlement
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
    materialized_from: edge.table.zs_observe.delhivery_settlement.has_column.column.zs_observe.delhivery_settlement.order_status
```

```yaml
candidate_edge:
  edge_id: edge.table.zs_observe.delhivery_settlement.has_column.column.zs_observe.delhivery_settlement.status
  edge_type: HAS_COLUMN
  source: table.zs_observe.delhivery_settlement
  target: column.zs_observe.delhivery_settlement.status
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
  edge_id: edge.column.zs_observe.delhivery_settlement.status.belongs_to_table.table.zs_observe.delhivery_settlement
  edge_type: BELONGS_TO_TABLE
  source: column.zs_observe.delhivery_settlement.status
  target: table.zs_observe.delhivery_settlement
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
    materialized_from: edge.table.zs_observe.delhivery_settlement.has_column.column.zs_observe.delhivery_settlement.status
```

```yaml
candidate_edge:
  edge_id: edge.table.zs_observe.delhivery_settlement.has_column.column.zs_observe.delhivery_settlement.payment_mode
  edge_type: HAS_COLUMN
  source: table.zs_observe.delhivery_settlement
  target: column.zs_observe.delhivery_settlement.payment_mode
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
  edge_id: edge.column.zs_observe.delhivery_settlement.payment_mode.belongs_to_table.table.zs_observe.delhivery_settlement
  edge_type: BELONGS_TO_TABLE
  source: column.zs_observe.delhivery_settlement.payment_mode
  target: table.zs_observe.delhivery_settlement
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
    materialized_from: edge.table.zs_observe.delhivery_settlement.has_column.column.zs_observe.delhivery_settlement.payment_mode
```

```yaml
candidate_edge:
  edge_id: edge.table.zs_observe.delhivery_settlement.has_column.column.zs_observe.delhivery_settlement.charged_amount
  edge_type: HAS_COLUMN
  source: table.zs_observe.delhivery_settlement
  target: column.zs_observe.delhivery_settlement.charged_amount
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
  edge_id: edge.column.zs_observe.delhivery_settlement.charged_amount.belongs_to_table.table.zs_observe.delhivery_settlement
  edge_type: BELONGS_TO_TABLE
  source: column.zs_observe.delhivery_settlement.charged_amount
  target: table.zs_observe.delhivery_settlement
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
    materialized_from: edge.table.zs_observe.delhivery_settlement.has_column.column.zs_observe.delhivery_settlement.charged_amount
```

```yaml
candidate_edge:
  edge_id: edge.table.zs_observe.delhivery_settlement.has_column.column.zs_observe.delhivery_settlement.cod_amount
  edge_type: HAS_COLUMN
  source: table.zs_observe.delhivery_settlement
  target: column.zs_observe.delhivery_settlement.cod_amount
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
  edge_id: edge.column.zs_observe.delhivery_settlement.cod_amount.belongs_to_table.table.zs_observe.delhivery_settlement
  edge_type: BELONGS_TO_TABLE
  source: column.zs_observe.delhivery_settlement.cod_amount
  target: table.zs_observe.delhivery_settlement
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
    materialized_from: edge.table.zs_observe.delhivery_settlement.has_column.column.zs_observe.delhivery_settlement.cod_amount
```

```yaml
candidate_edge:
  edge_id: edge.table.zs_observe.delhivery_settlement.has_column.column.zs_observe.delhivery_settlement.payable
  edge_type: HAS_COLUMN
  source: table.zs_observe.delhivery_settlement
  target: column.zs_observe.delhivery_settlement.payable
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
  edge_id: edge.column.zs_observe.delhivery_settlement.payable.belongs_to_table.table.zs_observe.delhivery_settlement
  edge_type: BELONGS_TO_TABLE
  source: column.zs_observe.delhivery_settlement.payable
  target: table.zs_observe.delhivery_settlement
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
    materialized_from: edge.table.zs_observe.delhivery_settlement.has_column.column.zs_observe.delhivery_settlement.payable
```

```yaml
candidate_edge:
  edge_id: edge.table.zs_observe.delhivery_settlement.has_column.column.zs_observe.delhivery_settlement.remittance_number
  edge_type: HAS_COLUMN
  source: table.zs_observe.delhivery_settlement
  target: column.zs_observe.delhivery_settlement.remittance_number
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
  edge_id: edge.column.zs_observe.delhivery_settlement.remittance_number.belongs_to_table.table.zs_observe.delhivery_settlement
  edge_type: BELONGS_TO_TABLE
  source: column.zs_observe.delhivery_settlement.remittance_number
  target: table.zs_observe.delhivery_settlement
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
    materialized_from: edge.table.zs_observe.delhivery_settlement.has_column.column.zs_observe.delhivery_settlement.remittance_number
```

```yaml
candidate_edge:
  edge_id: edge.table.zs_observe.delhivery_settlement.has_column.column.zs_observe.delhivery_settlement.utr_no
  edge_type: HAS_COLUMN
  source: table.zs_observe.delhivery_settlement
  target: column.zs_observe.delhivery_settlement.utr_no
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
  edge_id: edge.column.zs_observe.delhivery_settlement.utr_no.belongs_to_table.table.zs_observe.delhivery_settlement
  edge_type: BELONGS_TO_TABLE
  source: column.zs_observe.delhivery_settlement.utr_no
  target: table.zs_observe.delhivery_settlement
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
    materialized_from: edge.table.zs_observe.delhivery_settlement.has_column.column.zs_observe.delhivery_settlement.utr_no
```

```yaml
candidate_edge:
  edge_id: edge.table.zs_observe.delhivery_settlement.has_column.column.zs_observe.delhivery_settlement.settlement_date
  edge_type: HAS_COLUMN
  source: table.zs_observe.delhivery_settlement
  target: column.zs_observe.delhivery_settlement.settlement_date
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
  edge_id: edge.column.zs_observe.delhivery_settlement.settlement_date.belongs_to_table.table.zs_observe.delhivery_settlement
  edge_type: BELONGS_TO_TABLE
  source: column.zs_observe.delhivery_settlement.settlement_date
  target: table.zs_observe.delhivery_settlement
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
    materialized_from: edge.table.zs_observe.delhivery_settlement.has_column.column.zs_observe.delhivery_settlement.settlement_date
```

```yaml
candidate_edge:
  edge_id: edge.table.zs_observe.delhivery_settlement.has_column.column.zs_observe.delhivery_settlement.created_date
  edge_type: HAS_COLUMN
  source: table.zs_observe.delhivery_settlement
  target: column.zs_observe.delhivery_settlement.created_date
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
  edge_id: edge.column.zs_observe.delhivery_settlement.created_date.belongs_to_table.table.zs_observe.delhivery_settlement
  edge_type: BELONGS_TO_TABLE
  source: column.zs_observe.delhivery_settlement.created_date
  target: table.zs_observe.delhivery_settlement
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
    materialized_from: edge.table.zs_observe.delhivery_settlement.has_column.column.zs_observe.delhivery_settlement.created_date
```

```yaml
candidate_edge:
  edge_id: edge.table.zs_observe.delhivery_settlement.has_column.column.zs_observe.delhivery_settlement.source_city
  edge_type: HAS_COLUMN
  source: table.zs_observe.delhivery_settlement
  target: column.zs_observe.delhivery_settlement.source_city
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
  edge_id: edge.column.zs_observe.delhivery_settlement.source_city.belongs_to_table.table.zs_observe.delhivery_settlement
  edge_type: BELONGS_TO_TABLE
  source: column.zs_observe.delhivery_settlement.source_city
  target: table.zs_observe.delhivery_settlement
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
    materialized_from: edge.table.zs_observe.delhivery_settlement.has_column.column.zs_observe.delhivery_settlement.source_city
```

```yaml
candidate_edge:
  edge_id: edge.table.zs_observe.delhivery_settlement.has_column.column.zs_observe.delhivery_settlement.destination_city
  edge_type: HAS_COLUMN
  source: table.zs_observe.delhivery_settlement
  target: column.zs_observe.delhivery_settlement.destination_city
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
  edge_id: edge.column.zs_observe.delhivery_settlement.destination_city.belongs_to_table.table.zs_observe.delhivery_settlement
  edge_type: BELONGS_TO_TABLE
  source: column.zs_observe.delhivery_settlement.destination_city
  target: table.zs_observe.delhivery_settlement
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
    materialized_from: edge.table.zs_observe.delhivery_settlement.has_column.column.zs_observe.delhivery_settlement.destination_city
```

```yaml
candidate_edge:
  edge_id: edge.table.zs_observe.delhivery_settlement.has_column.column.zs_observe.delhivery_settlement.pincode
  edge_type: HAS_COLUMN
  source: table.zs_observe.delhivery_settlement
  target: column.zs_observe.delhivery_settlement.pincode
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
  edge_id: edge.column.zs_observe.delhivery_settlement.pincode.belongs_to_table.table.zs_observe.delhivery_settlement
  edge_type: BELONGS_TO_TABLE
  source: column.zs_observe.delhivery_settlement.pincode
  target: table.zs_observe.delhivery_settlement
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
    materialized_from: edge.table.zs_observe.delhivery_settlement.has_column.column.zs_observe.delhivery_settlement.pincode
```

```yaml
candidate_edge:
  edge_id: edge.table.zs_observe.delhivery_settlement.has_column.column.zs_observe.delhivery_settlement.destination_pin
  edge_type: HAS_COLUMN
  source: table.zs_observe.delhivery_settlement
  target: column.zs_observe.delhivery_settlement.destination_pin
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
  edge_id: edge.column.zs_observe.delhivery_settlement.destination_pin.belongs_to_table.table.zs_observe.delhivery_settlement
  edge_type: BELONGS_TO_TABLE
  source: column.zs_observe.delhivery_settlement.destination_pin
  target: table.zs_observe.delhivery_settlement
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
    materialized_from: edge.table.zs_observe.delhivery_settlement.has_column.column.zs_observe.delhivery_settlement.destination_pin
```

```yaml
candidate_edge:
  edge_id: edge.table.zs_observe.delhivery_settlement.has_column.column.zs_observe.delhivery_settlement.is_active
  edge_type: HAS_COLUMN
  source: table.zs_observe.delhivery_settlement
  target: column.zs_observe.delhivery_settlement.is_active
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
  edge_id: edge.column.zs_observe.delhivery_settlement.is_active.belongs_to_table.table.zs_observe.delhivery_settlement
  edge_type: BELONGS_TO_TABLE
  source: column.zs_observe.delhivery_settlement.is_active
  target: table.zs_observe.delhivery_settlement
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
    materialized_from: edge.table.zs_observe.delhivery_settlement.has_column.column.zs_observe.delhivery_settlement.is_active
```

```yaml
candidate_edge:
  edge_id: edge.table.zs_observe.delhivery_settlement.has_column.column.zs_observe.delhivery_settlement.group_level_id
  edge_type: HAS_COLUMN
  source: table.zs_observe.delhivery_settlement
  target: column.zs_observe.delhivery_settlement.group_level_id
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
  edge_id: edge.column.zs_observe.delhivery_settlement.group_level_id.belongs_to_table.table.zs_observe.delhivery_settlement
  edge_type: BELONGS_TO_TABLE
  source: column.zs_observe.delhivery_settlement.group_level_id
  target: table.zs_observe.delhivery_settlement
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
    materialized_from: edge.table.zs_observe.delhivery_settlement.has_column.column.zs_observe.delhivery_settlement.group_level_id
```

```yaml
candidate_edge:
  edge_id: edge.table.zs_observe.delhivery_invoice.has_relationship.relationship.delhivery_invoice.delhivery_settlement.awb
  edge_type: HAS_RELATIONSHIP
  source: table.zs_observe.delhivery_invoice
  target: relationship.delhivery_invoice.delhivery_settlement.awb
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
  edge_id: edge.relationship.delhivery_invoice.delhivery_settlement.awb.source_table.table.zs_observe.delhivery_invoice
  edge_type: SOURCE_TABLE
  source: relationship.delhivery_invoice.delhivery_settlement.awb
  target: table.zs_observe.delhivery_invoice
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
  edge_id: edge.table.zs_observe.delhivery_settlement.has_relationship.relationship.delhivery_invoice.delhivery_settlement.awb
  edge_type: HAS_RELATIONSHIP
  source: table.zs_observe.delhivery_settlement
  target: relationship.delhivery_invoice.delhivery_settlement.awb
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
  edge_id: edge.relationship.delhivery_invoice.delhivery_settlement.awb.target_table.table.zs_observe.delhivery_settlement
  edge_type: TARGET_TABLE
  source: relationship.delhivery_invoice.delhivery_settlement.awb
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
  edge_id: edge.relationship.delhivery_invoice.delhivery_settlement.awb.uses_source_column.column.zs_observe.delhivery_invoice.forward_awb_number
  edge_type: USES_SOURCE_COLUMN
  source: relationship.delhivery_invoice.delhivery_settlement.awb
  target: column.zs_observe.delhivery_invoice.forward_awb_number
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
  edge_id: edge.relationship.delhivery_invoice.delhivery_settlement.awb.uses_target_column.column.zs_observe.delhivery_settlement.waybill_num
  edge_type: USES_TARGET_COLUMN
  source: relationship.delhivery_invoice.delhivery_settlement.awb
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
  edge_id: edge.table.zs_observe.delhivery_invoice.has_relationship.relationship.delhivery_invoice.shiprocket_invoice.awb_crosscheck
  edge_type: HAS_RELATIONSHIP
  source: table.zs_observe.delhivery_invoice
  target: relationship.delhivery_invoice.shiprocket_invoice.awb_crosscheck
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
  edge_id: edge.relationship.delhivery_invoice.shiprocket_invoice.awb_crosscheck.source_table.table.zs_observe.delhivery_invoice
  edge_type: SOURCE_TABLE
  source: relationship.delhivery_invoice.shiprocket_invoice.awb_crosscheck
  target: table.zs_observe.delhivery_invoice
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
  edge_id: edge.table.zs_observe.shiprocket_invoice.has_relationship.relationship.delhivery_invoice.shiprocket_invoice.awb_crosscheck
  edge_type: HAS_RELATIONSHIP
  source: table.zs_observe.shiprocket_invoice
  target: relationship.delhivery_invoice.shiprocket_invoice.awb_crosscheck
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
  edge_id: edge.relationship.delhivery_invoice.shiprocket_invoice.awb_crosscheck.target_table.table.zs_observe.shiprocket_invoice
  edge_type: TARGET_TABLE
  source: relationship.delhivery_invoice.shiprocket_invoice.awb_crosscheck
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
  edge_id: edge.relationship.delhivery_invoice.shiprocket_invoice.awb_crosscheck.uses_source_column.column.zs_observe.delhivery_invoice.forward_awb_number
  edge_type: USES_SOURCE_COLUMN
  source: relationship.delhivery_invoice.shiprocket_invoice.awb_crosscheck
  target: column.zs_observe.delhivery_invoice.forward_awb_number
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
  edge_id: edge.relationship.delhivery_invoice.shiprocket_invoice.awb_crosscheck.uses_target_column.column.zs_observe.shiprocket_invoice.other_id
  edge_type: USES_TARGET_COLUMN
  source: relationship.delhivery_invoice.shiprocket_invoice.awb_crosscheck
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
  edge_id: edge.table.zs_observe.delhivery_invoice.has_value_profile.value_profile.delhivery_invoice.transaction_type
  edge_type: HAS_VALUE_PROFILE
  source: table.zs_observe.delhivery_invoice
  target: value_profile.delhivery_invoice.transaction_type
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
  edge_id: edge.value_profile.delhivery_invoice.transaction_type.profiles_column.column.zs_observe.delhivery_invoice.transaction_type
  edge_type: PROFILES_COLUMN
  source: value_profile.delhivery_invoice.transaction_type
  target: column.zs_observe.delhivery_invoice.transaction_type
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
  edge_id: edge.column.zs_observe.delhivery_invoice.transaction_type.has_value_profile.value_profile.delhivery_invoice.transaction_type
  edge_type: HAS_VALUE_PROFILE
  source: column.zs_observe.delhivery_invoice.transaction_type
  target: value_profile.delhivery_invoice.transaction_type
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
    materialized_from: edge.value_profile.delhivery_invoice.transaction_type.profiles_column.column.zs_observe.delhivery_invoice.transaction_type
```

```yaml
candidate_edge:
  edge_id: edge.value_profile.delhivery_invoice.transaction_type.profiles_table.table.zs_observe.delhivery_invoice
  edge_type: PROFILES_TABLE
  source: value_profile.delhivery_invoice.transaction_type
  target: table.zs_observe.delhivery_invoice
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
  edge_id: edge.table.zs_observe.delhivery_invoice.has_value_profile.value_profile.delhivery_invoice.order_status
  edge_type: HAS_VALUE_PROFILE
  source: table.zs_observe.delhivery_invoice
  target: value_profile.delhivery_invoice.order_status
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
  edge_id: edge.value_profile.delhivery_invoice.order_status.profiles_column.column.zs_observe.delhivery_invoice.order_status
  edge_type: PROFILES_COLUMN
  source: value_profile.delhivery_invoice.order_status
  target: column.zs_observe.delhivery_invoice.order_status
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
  edge_id: edge.column.zs_observe.delhivery_invoice.order_status.has_value_profile.value_profile.delhivery_invoice.order_status
  edge_type: HAS_VALUE_PROFILE
  source: column.zs_observe.delhivery_invoice.order_status
  target: value_profile.delhivery_invoice.order_status
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
    materialized_from: edge.value_profile.delhivery_invoice.order_status.profiles_column.column.zs_observe.delhivery_invoice.order_status
```

```yaml
candidate_edge:
  edge_id: edge.value_profile.delhivery_invoice.order_status.profiles_table.table.zs_observe.delhivery_invoice
  edge_type: PROFILES_TABLE
  source: value_profile.delhivery_invoice.order_status
  target: table.zs_observe.delhivery_invoice
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
  edge_id: edge.table.zs_observe.delhivery_invoice.has_value_profile.value_profile.delhivery_invoice.zone
  edge_type: HAS_VALUE_PROFILE
  source: table.zs_observe.delhivery_invoice
  target: value_profile.delhivery_invoice.zone
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
  edge_id: edge.value_profile.delhivery_invoice.zone.profiles_column.column.zs_observe.delhivery_invoice.zone
  edge_type: PROFILES_COLUMN
  source: value_profile.delhivery_invoice.zone
  target: column.zs_observe.delhivery_invoice.zone
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
  edge_id: edge.column.zs_observe.delhivery_invoice.zone.has_value_profile.value_profile.delhivery_invoice.zone
  edge_type: HAS_VALUE_PROFILE
  source: column.zs_observe.delhivery_invoice.zone
  target: value_profile.delhivery_invoice.zone
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
    materialized_from: edge.value_profile.delhivery_invoice.zone.profiles_column.column.zs_observe.delhivery_invoice.zone
```

```yaml
candidate_edge:
  edge_id: edge.value_profile.delhivery_invoice.zone.profiles_table.table.zs_observe.delhivery_invoice
  edge_type: PROFILES_TABLE
  source: value_profile.delhivery_invoice.zone
  target: table.zs_observe.delhivery_invoice
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
  edge_id: edge.table.zs_observe.delhivery_settlement.has_value_profile.value_profile.delhivery_settlement.txn_type
  edge_type: HAS_VALUE_PROFILE
  source: table.zs_observe.delhivery_settlement
  target: value_profile.delhivery_settlement.txn_type
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
  edge_id: edge.value_profile.delhivery_settlement.txn_type.profiles_column.column.zs_observe.delhivery_settlement.txn_type
  edge_type: PROFILES_COLUMN
  source: value_profile.delhivery_settlement.txn_type
  target: column.zs_observe.delhivery_settlement.txn_type
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
  edge_id: edge.column.zs_observe.delhivery_settlement.txn_type.has_value_profile.value_profile.delhivery_settlement.txn_type
  edge_type: HAS_VALUE_PROFILE
  source: column.zs_observe.delhivery_settlement.txn_type
  target: value_profile.delhivery_settlement.txn_type
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
    materialized_from: edge.value_profile.delhivery_settlement.txn_type.profiles_column.column.zs_observe.delhivery_settlement.txn_type
```

```yaml
candidate_edge:
  edge_id: edge.value_profile.delhivery_settlement.txn_type.profiles_table.table.zs_observe.delhivery_settlement
  edge_type: PROFILES_TABLE
  source: value_profile.delhivery_settlement.txn_type
  target: table.zs_observe.delhivery_settlement
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
  edge_id: edge.table.zs_observe.delhivery_settlement.has_value_profile.value_profile.delhivery_settlement.payment_mode
  edge_type: HAS_VALUE_PROFILE
  source: table.zs_observe.delhivery_settlement
  target: value_profile.delhivery_settlement.payment_mode
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
  edge_id: edge.value_profile.delhivery_settlement.payment_mode.profiles_column.column.zs_observe.delhivery_settlement.payment_mode
  edge_type: PROFILES_COLUMN
  source: value_profile.delhivery_settlement.payment_mode
  target: column.zs_observe.delhivery_settlement.payment_mode
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
  edge_id: edge.column.zs_observe.delhivery_settlement.payment_mode.has_value_profile.value_profile.delhivery_settlement.payment_mode
  edge_type: HAS_VALUE_PROFILE
  source: column.zs_observe.delhivery_settlement.payment_mode
  target: value_profile.delhivery_settlement.payment_mode
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
    materialized_from: edge.value_profile.delhivery_settlement.payment_mode.profiles_column.column.zs_observe.delhivery_settlement.payment_mode
```

```yaml
candidate_edge:
  edge_id: edge.value_profile.delhivery_settlement.payment_mode.profiles_table.table.zs_observe.delhivery_settlement
  edge_type: PROFILES_TABLE
  source: value_profile.delhivery_settlement.payment_mode
  target: table.zs_observe.delhivery_settlement
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
  edge_id: edge.table.zs_observe.delhivery_settlement.has_value_profile.value_profile.delhivery_settlement.status
  edge_type: HAS_VALUE_PROFILE
  source: table.zs_observe.delhivery_settlement
  target: value_profile.delhivery_settlement.status
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
  edge_id: edge.value_profile.delhivery_settlement.status.profiles_column.column.zs_observe.delhivery_settlement.status
  edge_type: PROFILES_COLUMN
  source: value_profile.delhivery_settlement.status
  target: column.zs_observe.delhivery_settlement.status
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
  edge_id: edge.column.zs_observe.delhivery_settlement.status.has_value_profile.value_profile.delhivery_settlement.status
  edge_type: HAS_VALUE_PROFILE
  source: column.zs_observe.delhivery_settlement.status
  target: value_profile.delhivery_settlement.status
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
    materialized_from: edge.value_profile.delhivery_settlement.status.profiles_column.column.zs_observe.delhivery_settlement.status
```

```yaml
candidate_edge:
  edge_id: edge.value_profile.delhivery_settlement.status.profiles_table.table.zs_observe.delhivery_settlement
  edge_type: PROFILES_TABLE
  source: value_profile.delhivery_settlement.status
  target: table.zs_observe.delhivery_settlement
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
  edge_id: edge.metric.freight_billed_amount.has_implementation.metric_impl.delhivery_invoice.freight_billed_amount
  edge_type: HAS_IMPLEMENTATION
  source: metric.freight_billed_amount
  target: metric_impl.delhivery_invoice.freight_billed_amount
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
  edge_id: edge.metric_impl.delhivery_invoice.freight_billed_amount.implements_metric.metric.freight_billed_amount
  edge_type: IMPLEMENTS_METRIC
  source: metric_impl.delhivery_invoice.freight_billed_amount
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
    materialized_from: edge.metric.freight_billed_amount.has_implementation.metric_impl.delhivery_invoice.freight_billed_amount
```

```yaml
candidate_edge:
  edge_id: edge.metric_impl.delhivery_invoice.freight_billed_amount.uses_table.table.zs_observe.delhivery_invoice
  edge_type: USES_TABLE
  source: metric_impl.delhivery_invoice.freight_billed_amount
  target: table.zs_observe.delhivery_invoice
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
  edge_id: edge.metric_impl.delhivery_invoice.freight_billed_amount.uses_column.column.zs_observe.delhivery_invoice.charge_dl.8737448c
  edge_type: USES_COLUMN
  source: metric_impl.delhivery_invoice.freight_billed_amount
  target: column.zs_observe.delhivery_invoice.charge_dl
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
  edge_id: edge.metric_impl.delhivery_invoice.freight_billed_amount.uses_column.column.zs_observe.delhivery_invoice.charge_rto.8737448c
  edge_type: USES_COLUMN
  source: metric_impl.delhivery_invoice.freight_billed_amount
  target: column.zs_observe.delhivery_invoice.charge_rto
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
  edge_id: edge.metric_impl.delhivery_invoice.freight_billed_amount.uses_column.column.zs_observe.delhivery_invoice.charge_dto.8737448c
  edge_type: USES_COLUMN
  source: metric_impl.delhivery_invoice.freight_billed_amount
  target: column.zs_observe.delhivery_invoice.charge_dto
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
  edge_id: edge.metric_impl.delhivery_invoice.freight_billed_amount.uses_column.column.zs_observe.delhivery_invoice.charge_cod.8737448c
  edge_type: USES_COLUMN
  source: metric_impl.delhivery_invoice.freight_billed_amount
  target: column.zs_observe.delhivery_invoice.charge_cod
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
  edge_id: edge.metric_impl.delhivery_invoice.freight_billed_amount.uses_column.column.zs_observe.delhivery_invoice.charge_fsc.8737448c
  edge_type: USES_COLUMN
  source: metric_impl.delhivery_invoice.freight_billed_amount
  target: column.zs_observe.delhivery_invoice.charge_fsc
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
  edge_id: edge.metric_impl.delhivery_invoice.freight_billed_amount.uses_column.column.zs_observe.delhivery_invoice.charge_fs.8737448c
  edge_type: USES_COLUMN
  source: metric_impl.delhivery_invoice.freight_billed_amount
  target: column.zs_observe.delhivery_invoice.charge_fs
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
  edge_id: edge.metric_impl.delhivery_invoice.freight_billed_amount.uses_column.column.zs_observe.delhivery_invoice.charge_fov.8737448c
  edge_type: USES_COLUMN
  source: metric_impl.delhivery_invoice.freight_billed_amount
  target: column.zs_observe.delhivery_invoice.charge_fov
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
  edge_id: edge.metric_impl.delhivery_invoice.freight_billed_amount.uses_column.column.zs_observe.delhivery_invoice.charge_air.8737448c
  edge_type: USES_COLUMN
  source: metric_impl.delhivery_invoice.freight_billed_amount
  target: column.zs_observe.delhivery_invoice.charge_air
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
  edge_id: edge.metric_impl.delhivery_invoice.freight_billed_amount.uses_column.column.zs_observe.delhivery_invoice.charge_pickup.8737448c
  edge_type: USES_COLUMN
  source: metric_impl.delhivery_invoice.freight_billed_amount
  target: column.zs_observe.delhivery_invoice.charge_pickup
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
  edge_id: edge.metric_impl.delhivery_invoice.freight_billed_amount.uses_column.column.zs_observe.delhivery_invoice.charge_peak.8737448c
  edge_type: USES_COLUMN
  source: metric_impl.delhivery_invoice.freight_billed_amount
  target: column.zs_observe.delhivery_invoice.charge_peak
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
  edge_id: edge.metric_impl.delhivery_invoice.freight_billed_amount.uses_formula_template.formula_template.logistics.component_sum
  edge_type: USES_FORMULA_TEMPLATE
  source: metric_impl.delhivery_invoice.freight_billed_amount
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
  edge_id: edge.metric.forward_freight_amount.has_implementation.metric_impl.delhivery_invoice.forward_freight_amount
  edge_type: HAS_IMPLEMENTATION
  source: metric.forward_freight_amount
  target: metric_impl.delhivery_invoice.forward_freight_amount
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
  edge_id: edge.metric_impl.delhivery_invoice.forward_freight_amount.implements_metric.metric.forward_freight_amount
  edge_type: IMPLEMENTS_METRIC
  source: metric_impl.delhivery_invoice.forward_freight_amount
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
    materialized_from: edge.metric.forward_freight_amount.has_implementation.metric_impl.delhivery_invoice.forward_freight_amount
```

```yaml
candidate_edge:
  edge_id: edge.metric_impl.delhivery_invoice.forward_freight_amount.uses_table.table.zs_observe.delhivery_invoice
  edge_type: USES_TABLE
  source: metric_impl.delhivery_invoice.forward_freight_amount
  target: table.zs_observe.delhivery_invoice
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
  edge_id: edge.metric_impl.delhivery_invoice.forward_freight_amount.uses_column.column.zs_observe.delhivery_invoice.charge_dl.8737448c
  edge_type: USES_COLUMN
  source: metric_impl.delhivery_invoice.forward_freight_amount
  target: column.zs_observe.delhivery_invoice.charge_dl
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
  edge_id: edge.metric_impl.delhivery_invoice.forward_freight_amount.uses_formula_template.formula_template.logistics.component_sum
  edge_type: USES_FORMULA_TEMPLATE
  source: metric_impl.delhivery_invoice.forward_freight_amount
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
  edge_id: edge.metric.rto_freight_amount.has_implementation.metric_impl.delhivery_invoice.rto_freight_amount
  edge_type: HAS_IMPLEMENTATION
  source: metric.rto_freight_amount
  target: metric_impl.delhivery_invoice.rto_freight_amount
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
  edge_id: edge.metric_impl.delhivery_invoice.rto_freight_amount.implements_metric.metric.rto_freight_amount
  edge_type: IMPLEMENTS_METRIC
  source: metric_impl.delhivery_invoice.rto_freight_amount
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
    materialized_from: edge.metric.rto_freight_amount.has_implementation.metric_impl.delhivery_invoice.rto_freight_amount
```

```yaml
candidate_edge:
  edge_id: edge.metric_impl.delhivery_invoice.rto_freight_amount.uses_table.table.zs_observe.delhivery_invoice
  edge_type: USES_TABLE
  source: metric_impl.delhivery_invoice.rto_freight_amount
  target: table.zs_observe.delhivery_invoice
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
  edge_id: edge.metric_impl.delhivery_invoice.rto_freight_amount.uses_column.column.zs_observe.delhivery_invoice.charge_rto.8737448c
  edge_type: USES_COLUMN
  source: metric_impl.delhivery_invoice.rto_freight_amount
  target: column.zs_observe.delhivery_invoice.charge_rto
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
  edge_id: edge.metric_impl.delhivery_invoice.rto_freight_amount.uses_formula_template.formula_template.logistics.component_sum
  edge_type: USES_FORMULA_TEMPLATE
  source: metric_impl.delhivery_invoice.rto_freight_amount
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
  edge_id: edge.metric.dto_freight_amount.has_implementation.metric_impl.delhivery_invoice.dto_freight_amount
  edge_type: HAS_IMPLEMENTATION
  source: metric.dto_freight_amount
  target: metric_impl.delhivery_invoice.dto_freight_amount
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
  edge_id: edge.metric_impl.delhivery_invoice.dto_freight_amount.implements_metric.metric.dto_freight_amount
  edge_type: IMPLEMENTS_METRIC
  source: metric_impl.delhivery_invoice.dto_freight_amount
  target: metric.dto_freight_amount
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
    materialized_from: edge.metric.dto_freight_amount.has_implementation.metric_impl.delhivery_invoice.dto_freight_amount
```

```yaml
candidate_edge:
  edge_id: edge.metric_impl.delhivery_invoice.dto_freight_amount.uses_table.table.zs_observe.delhivery_invoice
  edge_type: USES_TABLE
  source: metric_impl.delhivery_invoice.dto_freight_amount
  target: table.zs_observe.delhivery_invoice
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
  edge_id: edge.metric_impl.delhivery_invoice.dto_freight_amount.uses_column.column.zs_observe.delhivery_invoice.charge_dto.8737448c
  edge_type: USES_COLUMN
  source: metric_impl.delhivery_invoice.dto_freight_amount
  target: column.zs_observe.delhivery_invoice.charge_dto
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
  edge_id: edge.metric_impl.delhivery_invoice.dto_freight_amount.uses_formula_template.formula_template.logistics.component_sum
  edge_type: USES_FORMULA_TEMPLATE
  source: metric_impl.delhivery_invoice.dto_freight_amount
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
  edge_id: edge.metric.cod_fee_amount.has_implementation.metric_impl.delhivery_invoice.cod_fee_amount
  edge_type: HAS_IMPLEMENTATION
  source: metric.cod_fee_amount
  target: metric_impl.delhivery_invoice.cod_fee_amount
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
  edge_id: edge.metric_impl.delhivery_invoice.cod_fee_amount.implements_metric.metric.cod_fee_amount
  edge_type: IMPLEMENTS_METRIC
  source: metric_impl.delhivery_invoice.cod_fee_amount
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
    materialized_from: edge.metric.cod_fee_amount.has_implementation.metric_impl.delhivery_invoice.cod_fee_amount
```

```yaml
candidate_edge:
  edge_id: edge.metric_impl.delhivery_invoice.cod_fee_amount.uses_table.table.zs_observe.delhivery_invoice
  edge_type: USES_TABLE
  source: metric_impl.delhivery_invoice.cod_fee_amount
  target: table.zs_observe.delhivery_invoice
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
  edge_id: edge.metric_impl.delhivery_invoice.cod_fee_amount.uses_column.column.zs_observe.delhivery_invoice.charge_cod.8737448c
  edge_type: USES_COLUMN
  source: metric_impl.delhivery_invoice.cod_fee_amount
  target: column.zs_observe.delhivery_invoice.charge_cod
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
  edge_id: edge.metric_impl.delhivery_invoice.cod_fee_amount.uses_formula_template.formula_template.logistics.component_sum
  edge_type: USES_FORMULA_TEMPLATE
  source: metric_impl.delhivery_invoice.cod_fee_amount
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
  edge_id: edge.metric.fuel_surcharge_amount.has_implementation.metric_impl.delhivery_invoice.fuel_surcharge_amount
  edge_type: HAS_IMPLEMENTATION
  source: metric.fuel_surcharge_amount
  target: metric_impl.delhivery_invoice.fuel_surcharge_amount
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
  edge_id: edge.metric_impl.delhivery_invoice.fuel_surcharge_amount.implements_metric.metric.fuel_surcharge_amount
  edge_type: IMPLEMENTS_METRIC
  source: metric_impl.delhivery_invoice.fuel_surcharge_amount
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
    materialized_from: edge.metric.fuel_surcharge_amount.has_implementation.metric_impl.delhivery_invoice.fuel_surcharge_amount
```

```yaml
candidate_edge:
  edge_id: edge.metric_impl.delhivery_invoice.fuel_surcharge_amount.uses_table.table.zs_observe.delhivery_invoice
  edge_type: USES_TABLE
  source: metric_impl.delhivery_invoice.fuel_surcharge_amount
  target: table.zs_observe.delhivery_invoice
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
  edge_id: edge.metric_impl.delhivery_invoice.fuel_surcharge_amount.uses_column.column.zs_observe.delhivery_invoice.charge_fsc.8737448c
  edge_type: USES_COLUMN
  source: metric_impl.delhivery_invoice.fuel_surcharge_amount
  target: column.zs_observe.delhivery_invoice.charge_fsc
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
  edge_id: edge.metric_impl.delhivery_invoice.fuel_surcharge_amount.uses_formula_template.formula_template.logistics.component_sum
  edge_type: USES_FORMULA_TEMPLATE
  source: metric_impl.delhivery_invoice.fuel_surcharge_amount
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
  edge_id: edge.metric.fov_insurance_amount.has_implementation.metric_impl.delhivery_invoice.fov_insurance_amount
  edge_type: HAS_IMPLEMENTATION
  source: metric.fov_insurance_amount
  target: metric_impl.delhivery_invoice.fov_insurance_amount
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
  edge_id: edge.metric_impl.delhivery_invoice.fov_insurance_amount.implements_metric.metric.fov_insurance_amount
  edge_type: IMPLEMENTS_METRIC
  source: metric_impl.delhivery_invoice.fov_insurance_amount
  target: metric.fov_insurance_amount
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
    materialized_from: edge.metric.fov_insurance_amount.has_implementation.metric_impl.delhivery_invoice.fov_insurance_amount
```

```yaml
candidate_edge:
  edge_id: edge.metric_impl.delhivery_invoice.fov_insurance_amount.uses_table.table.zs_observe.delhivery_invoice
  edge_type: USES_TABLE
  source: metric_impl.delhivery_invoice.fov_insurance_amount
  target: table.zs_observe.delhivery_invoice
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
  edge_id: edge.metric_impl.delhivery_invoice.fov_insurance_amount.uses_column.column.zs_observe.delhivery_invoice.charge_fov.8737448c
  edge_type: USES_COLUMN
  source: metric_impl.delhivery_invoice.fov_insurance_amount
  target: column.zs_observe.delhivery_invoice.charge_fov
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
  edge_id: edge.metric_impl.delhivery_invoice.fov_insurance_amount.uses_formula_template.formula_template.logistics.component_sum
  edge_type: USES_FORMULA_TEMPLATE
  source: metric_impl.delhivery_invoice.fov_insurance_amount
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
  edge_id: edge.metric.pickup_charge_amount.has_implementation.metric_impl.delhivery_invoice.pickup_charge_amount
  edge_type: HAS_IMPLEMENTATION
  source: metric.pickup_charge_amount
  target: metric_impl.delhivery_invoice.pickup_charge_amount
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
  edge_id: edge.metric_impl.delhivery_invoice.pickup_charge_amount.implements_metric.metric.pickup_charge_amount
  edge_type: IMPLEMENTS_METRIC
  source: metric_impl.delhivery_invoice.pickup_charge_amount
  target: metric.pickup_charge_amount
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
    materialized_from: edge.metric.pickup_charge_amount.has_implementation.metric_impl.delhivery_invoice.pickup_charge_amount
```

```yaml
candidate_edge:
  edge_id: edge.metric_impl.delhivery_invoice.pickup_charge_amount.uses_table.table.zs_observe.delhivery_invoice
  edge_type: USES_TABLE
  source: metric_impl.delhivery_invoice.pickup_charge_amount
  target: table.zs_observe.delhivery_invoice
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
  edge_id: edge.metric_impl.delhivery_invoice.pickup_charge_amount.uses_column.column.zs_observe.delhivery_invoice.charge_pickup.8737448c
  edge_type: USES_COLUMN
  source: metric_impl.delhivery_invoice.pickup_charge_amount
  target: column.zs_observe.delhivery_invoice.charge_pickup
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
  edge_id: edge.metric_impl.delhivery_invoice.pickup_charge_amount.uses_formula_template.formula_template.logistics.component_sum
  edge_type: USES_FORMULA_TEMPLATE
  source: metric_impl.delhivery_invoice.pickup_charge_amount
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
  edge_id: edge.metric.peak_surcharge_amount.has_implementation.metric_impl.delhivery_invoice.peak_surcharge_amount
  edge_type: HAS_IMPLEMENTATION
  source: metric.peak_surcharge_amount
  target: metric_impl.delhivery_invoice.peak_surcharge_amount
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
  edge_id: edge.metric_impl.delhivery_invoice.peak_surcharge_amount.implements_metric.metric.peak_surcharge_amount
  edge_type: IMPLEMENTS_METRIC
  source: metric_impl.delhivery_invoice.peak_surcharge_amount
  target: metric.peak_surcharge_amount
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
    materialized_from: edge.metric.peak_surcharge_amount.has_implementation.metric_impl.delhivery_invoice.peak_surcharge_amount
```

```yaml
candidate_edge:
  edge_id: edge.metric_impl.delhivery_invoice.peak_surcharge_amount.uses_table.table.zs_observe.delhivery_invoice
  edge_type: USES_TABLE
  source: metric_impl.delhivery_invoice.peak_surcharge_amount
  target: table.zs_observe.delhivery_invoice
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
  edge_id: edge.metric_impl.delhivery_invoice.peak_surcharge_amount.uses_column.column.zs_observe.delhivery_invoice.charge_peak.8737448c
  edge_type: USES_COLUMN
  source: metric_impl.delhivery_invoice.peak_surcharge_amount
  target: column.zs_observe.delhivery_invoice.charge_peak
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
  edge_id: edge.metric_impl.delhivery_invoice.peak_surcharge_amount.uses_formula_template.formula_template.logistics.component_sum
  edge_type: USES_FORMULA_TEMPLATE
  source: metric_impl.delhivery_invoice.peak_surcharge_amount
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
  edge_id: edge.metric.gst_on_freight_amount.has_implementation.metric_impl.delhivery_invoice.gst_on_freight_amount
  edge_type: HAS_IMPLEMENTATION
  source: metric.gst_on_freight_amount
  target: metric_impl.delhivery_invoice.gst_on_freight_amount
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
  edge_id: edge.metric_impl.delhivery_invoice.gst_on_freight_amount.implements_metric.metric.gst_on_freight_amount
  edge_type: IMPLEMENTS_METRIC
  source: metric_impl.delhivery_invoice.gst_on_freight_amount
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
    materialized_from: edge.metric.gst_on_freight_amount.has_implementation.metric_impl.delhivery_invoice.gst_on_freight_amount
```

```yaml
candidate_edge:
  edge_id: edge.metric_impl.delhivery_invoice.gst_on_freight_amount.uses_table.table.zs_observe.delhivery_invoice
  edge_type: USES_TABLE
  source: metric_impl.delhivery_invoice.gst_on_freight_amount
  target: table.zs_observe.delhivery_invoice
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
  edge_id: edge.metric_impl.delhivery_invoice.gst_on_freight_amount.uses_column.column.zs_observe.delhivery_invoice.tax_cgst_amount.8737448c
  edge_type: USES_COLUMN
  source: metric_impl.delhivery_invoice.gst_on_freight_amount
  target: column.zs_observe.delhivery_invoice.tax_cgst_amount
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
  edge_id: edge.metric_impl.delhivery_invoice.gst_on_freight_amount.uses_column.column.zs_observe.delhivery_invoice.tax_sgst_amount.8737448c
  edge_type: USES_COLUMN
  source: metric_impl.delhivery_invoice.gst_on_freight_amount
  target: column.zs_observe.delhivery_invoice.tax_sgst_amount
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
  edge_id: edge.metric_impl.delhivery_invoice.gst_on_freight_amount.uses_column.column.zs_observe.delhivery_invoice.tax_igst_amount.8737448c
  edge_type: USES_COLUMN
  source: metric_impl.delhivery_invoice.gst_on_freight_amount
  target: column.zs_observe.delhivery_invoice.tax_igst_amount
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
  edge_id: edge.metric_impl.delhivery_invoice.gst_on_freight_amount.uses_formula_template.formula_template.logistics.component_sum
  edge_type: USES_FORMULA_TEMPLATE
  source: metric_impl.delhivery_invoice.gst_on_freight_amount
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
  edge_id: edge.metric.declared_product_value.has_implementation.metric_impl.delhivery_invoice.declared_product_value
  edge_type: HAS_IMPLEMENTATION
  source: metric.declared_product_value
  target: metric_impl.delhivery_invoice.declared_product_value
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
  edge_id: edge.metric_impl.delhivery_invoice.declared_product_value.implements_metric.metric.declared_product_value
  edge_type: IMPLEMENTS_METRIC
  source: metric_impl.delhivery_invoice.declared_product_value
  target: metric.declared_product_value
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
    materialized_from: edge.metric.declared_product_value.has_implementation.metric_impl.delhivery_invoice.declared_product_value
```

```yaml
candidate_edge:
  edge_id: edge.metric_impl.delhivery_invoice.declared_product_value.uses_table.table.zs_observe.delhivery_invoice
  edge_type: USES_TABLE
  source: metric_impl.delhivery_invoice.declared_product_value
  target: table.zs_observe.delhivery_invoice
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
  edge_id: edge.metric_impl.delhivery_invoice.declared_product_value.uses_column.column.zs_observe.delhivery_invoice.charged_amount.8737448c
  edge_type: USES_COLUMN
  source: metric_impl.delhivery_invoice.declared_product_value
  target: column.zs_observe.delhivery_invoice.charged_amount
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
  edge_id: edge.metric_impl.delhivery_invoice.declared_product_value.uses_formula_template.formula_template.logistics.component_sum
  edge_type: USES_FORMULA_TEMPLATE
  source: metric_impl.delhivery_invoice.declared_product_value
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
  edge_id: edge.metric.cod_expected_amount.has_implementation.metric_impl.delhivery_invoice.cod_expected_amount
  edge_type: HAS_IMPLEMENTATION
  source: metric.cod_expected_amount
  target: metric_impl.delhivery_invoice.cod_expected_amount
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
  edge_id: edge.metric_impl.delhivery_invoice.cod_expected_amount.implements_metric.metric.cod_expected_amount
  edge_type: IMPLEMENTS_METRIC
  source: metric_impl.delhivery_invoice.cod_expected_amount
  target: metric.cod_expected_amount
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
    materialized_from: edge.metric.cod_expected_amount.has_implementation.metric_impl.delhivery_invoice.cod_expected_amount
```

```yaml
candidate_edge:
  edge_id: edge.metric_impl.delhivery_invoice.cod_expected_amount.uses_table.table.zs_observe.delhivery_invoice
  edge_type: USES_TABLE
  source: metric_impl.delhivery_invoice.cod_expected_amount
  target: table.zs_observe.delhivery_invoice
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
  edge_id: edge.metric_impl.delhivery_invoice.cod_expected_amount.uses_column.column.zs_observe.delhivery_invoice.cod_amount.8737448c
  edge_type: USES_COLUMN
  source: metric_impl.delhivery_invoice.cod_expected_amount
  target: column.zs_observe.delhivery_invoice.cod_amount
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
  edge_id: edge.metric_impl.delhivery_invoice.cod_expected_amount.uses_formula_template.formula_template.logistics.component_sum
  edge_type: USES_FORMULA_TEMPLATE
  source: metric_impl.delhivery_invoice.cod_expected_amount
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
  edge_id: edge.metric.billable_weight.has_implementation.metric_impl.delhivery_invoice.billable_weight
  edge_type: HAS_IMPLEMENTATION
  source: metric.billable_weight
  target: metric_impl.delhivery_invoice.billable_weight
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
  edge_id: edge.metric_impl.delhivery_invoice.billable_weight.implements_metric.metric.billable_weight
  edge_type: IMPLEMENTS_METRIC
  source: metric_impl.delhivery_invoice.billable_weight
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
    materialized_from: edge.metric.billable_weight.has_implementation.metric_impl.delhivery_invoice.billable_weight
```

```yaml
candidate_edge:
  edge_id: edge.metric_impl.delhivery_invoice.billable_weight.uses_table.table.zs_observe.delhivery_invoice
  edge_type: USES_TABLE
  source: metric_impl.delhivery_invoice.billable_weight
  target: table.zs_observe.delhivery_invoice
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
  edge_id: edge.metric_impl.delhivery_invoice.billable_weight.uses_column.column.zs_observe.delhivery_invoice.charged_weight.8737448c
  edge_type: USES_COLUMN
  source: metric_impl.delhivery_invoice.billable_weight
  target: column.zs_observe.delhivery_invoice.charged_weight
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
  edge_id: edge.metric_impl.delhivery_invoice.billable_weight.uses_formula_template.formula_template.logistics.component_sum
  edge_type: USES_FORMULA_TEMPLATE
  source: metric_impl.delhivery_invoice.billable_weight
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
  edge_id: edge.metric.shipment_count.has_implementation.metric_impl.delhivery_invoice.shipment_count
  edge_type: HAS_IMPLEMENTATION
  source: metric.shipment_count
  target: metric_impl.delhivery_invoice.shipment_count
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
  edge_id: edge.metric_impl.delhivery_invoice.shipment_count.implements_metric.metric.shipment_count
  edge_type: IMPLEMENTS_METRIC
  source: metric_impl.delhivery_invoice.shipment_count
  target: metric.shipment_count
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
    materialized_from: edge.metric.shipment_count.has_implementation.metric_impl.delhivery_invoice.shipment_count
```

```yaml
candidate_edge:
  edge_id: edge.metric_impl.delhivery_invoice.shipment_count.uses_table.table.zs_observe.delhivery_invoice
  edge_type: USES_TABLE
  source: metric_impl.delhivery_invoice.shipment_count
  target: table.zs_observe.delhivery_invoice
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
  edge_id: edge.metric_impl.delhivery_invoice.shipment_count.uses_column.column.zs_observe.delhivery_invoice.forward_awb_number.9e2adfd1
  edge_type: USES_COLUMN
  source: metric_impl.delhivery_invoice.shipment_count
  target: column.zs_observe.delhivery_invoice.forward_awb_number
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
  edge_id: edge.metric_impl.delhivery_invoice.shipment_count.uses_formula_template.formula_template.logistics.ratio_rate
  edge_type: USES_FORMULA_TEMPLATE
  source: metric_impl.delhivery_invoice.shipment_count
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
  edge_id: edge.metric.delivered_shipment_count.has_implementation.metric_impl.delhivery_invoice.delivered_shipment_count
  edge_type: HAS_IMPLEMENTATION
  source: metric.delivered_shipment_count
  target: metric_impl.delhivery_invoice.delivered_shipment_count
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
  edge_id: edge.metric_impl.delhivery_invoice.delivered_shipment_count.implements_metric.metric.delivered_shipment_count
  edge_type: IMPLEMENTS_METRIC
  source: metric_impl.delhivery_invoice.delivered_shipment_count
  target: metric.delivered_shipment_count
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
    materialized_from: edge.metric.delivered_shipment_count.has_implementation.metric_impl.delhivery_invoice.delivered_shipment_count
```

```yaml
candidate_edge:
  edge_id: edge.metric_impl.delhivery_invoice.delivered_shipment_count.uses_table.table.zs_observe.delhivery_invoice
  edge_type: USES_TABLE
  source: metric_impl.delhivery_invoice.delivered_shipment_count
  target: table.zs_observe.delhivery_invoice
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
  edge_id: edge.metric_impl.delhivery_invoice.delivered_shipment_count.uses_column.column.zs_observe.delhivery_invoice.transaction_type.28a8df7f
  edge_type: USES_COLUMN
  source: metric_impl.delhivery_invoice.delivered_shipment_count
  target: column.zs_observe.delhivery_invoice.transaction_type
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
      column_role: filter
```

```yaml
candidate_edge:
  edge_id: edge.metric_impl.delhivery_invoice.delivered_shipment_count.uses_formula_template.formula_template.logistics.ratio_rate
  edge_type: USES_FORMULA_TEMPLATE
  source: metric_impl.delhivery_invoice.delivered_shipment_count
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
  edge_id: edge.metric.rto_count.has_implementation.metric_impl.delhivery_invoice.rto_count
  edge_type: HAS_IMPLEMENTATION
  source: metric.rto_count
  target: metric_impl.delhivery_invoice.rto_count
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
  edge_id: edge.metric_impl.delhivery_invoice.rto_count.implements_metric.metric.rto_count
  edge_type: IMPLEMENTS_METRIC
  source: metric_impl.delhivery_invoice.rto_count
  target: metric.rto_count
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
    materialized_from: edge.metric.rto_count.has_implementation.metric_impl.delhivery_invoice.rto_count
```

```yaml
candidate_edge:
  edge_id: edge.metric_impl.delhivery_invoice.rto_count.uses_table.table.zs_observe.delhivery_invoice
  edge_type: USES_TABLE
  source: metric_impl.delhivery_invoice.rto_count
  target: table.zs_observe.delhivery_invoice
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
  edge_id: edge.metric_impl.delhivery_invoice.rto_count.uses_column.column.zs_observe.delhivery_invoice.transaction_type.28a8df7f
  edge_type: USES_COLUMN
  source: metric_impl.delhivery_invoice.rto_count
  target: column.zs_observe.delhivery_invoice.transaction_type
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
      column_role: filter
```

```yaml
candidate_edge:
  edge_id: edge.metric_impl.delhivery_invoice.rto_count.uses_formula_template.formula_template.logistics.ratio_rate
  edge_type: USES_FORMULA_TEMPLATE
  source: metric_impl.delhivery_invoice.rto_count
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
  edge_id: edge.metric.cod_collected_amount.has_implementation.metric_impl.delhivery_invoice.cod_collected_amount
  edge_type: HAS_IMPLEMENTATION
  source: metric.cod_collected_amount
  target: metric_impl.delhivery_invoice.cod_collected_amount
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
  edge_id: edge.metric_impl.delhivery_invoice.cod_collected_amount.implements_metric.metric.cod_collected_amount
  edge_type: IMPLEMENTS_METRIC
  source: metric_impl.delhivery_invoice.cod_collected_amount
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
    materialized_from: edge.metric.cod_collected_amount.has_implementation.metric_impl.delhivery_invoice.cod_collected_amount
```

```yaml
candidate_edge:
  edge_id: edge.metric_impl.delhivery_invoice.cod_collected_amount.uses_table.table.zs_observe.delhivery_invoice
  edge_type: USES_TABLE
  source: metric_impl.delhivery_invoice.cod_collected_amount
  target: table.zs_observe.delhivery_invoice
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
  edge_id: edge.metric_impl.delhivery_invoice.cod_collected_amount.uses_column.column.zs_observe.delhivery_invoice.cod_amount.8737448c
  edge_type: USES_COLUMN
  source: metric_impl.delhivery_invoice.cod_collected_amount
  target: column.zs_observe.delhivery_invoice.cod_amount
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
  edge_id: edge.metric_impl.delhivery_invoice.cod_collected_amount.uses_formula_template.formula_template.logistics.ratio_rate
  edge_type: USES_FORMULA_TEMPLATE
  source: metric_impl.delhivery_invoice.cod_collected_amount
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
  edge_id: edge.metric.average_freight_per_awb.has_implementation.metric_impl.delhivery_invoice.average_freight_per_awb
  edge_type: HAS_IMPLEMENTATION
  source: metric.average_freight_per_awb
  target: metric_impl.delhivery_invoice.average_freight_per_awb
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
  edge_id: edge.metric_impl.delhivery_invoice.average_freight_per_awb.implements_metric.metric.average_freight_per_awb
  edge_type: IMPLEMENTS_METRIC
  source: metric_impl.delhivery_invoice.average_freight_per_awb
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
    materialized_from: edge.metric.average_freight_per_awb.has_implementation.metric_impl.delhivery_invoice.average_freight_per_awb
```

```yaml
candidate_edge:
  edge_id: edge.metric_impl.delhivery_invoice.average_freight_per_awb.uses_table.table.zs_observe.delhivery_invoice
  edge_type: USES_TABLE
  source: metric_impl.delhivery_invoice.average_freight_per_awb
  target: table.zs_observe.delhivery_invoice
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
  edge_id: edge.metric_impl.delhivery_invoice.average_freight_per_awb.uses_column.column.zs_observe.delhivery_invoice.forward_awb_number.9e2adfd1
  edge_type: USES_COLUMN
  source: metric_impl.delhivery_invoice.average_freight_per_awb
  target: column.zs_observe.delhivery_invoice.forward_awb_number
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
  edge_id: edge.metric_impl.delhivery_invoice.average_freight_per_awb.uses_formula_template.formula_template.logistics.ratio_rate
  edge_type: USES_FORMULA_TEMPLATE
  source: metric_impl.delhivery_invoice.average_freight_per_awb
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
  edge_id: edge.metric.cod_collected_amount.has_implementation.metric_impl.delhivery_settlement.cod_collected_amount
  edge_type: HAS_IMPLEMENTATION
  source: metric.cod_collected_amount
  target: metric_impl.delhivery_settlement.cod_collected_amount
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
  edge_id: edge.metric_impl.delhivery_settlement.cod_collected_amount.implements_metric.metric.cod_collected_amount
  edge_type: IMPLEMENTS_METRIC
  source: metric_impl.delhivery_settlement.cod_collected_amount
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
    materialized_from: edge.metric.cod_collected_amount.has_implementation.metric_impl.delhivery_settlement.cod_collected_amount
```

```yaml
candidate_edge:
  edge_id: edge.metric_impl.delhivery_settlement.cod_collected_amount.uses_table.table.zs_observe.delhivery_settlement
  edge_type: USES_TABLE
  source: metric_impl.delhivery_settlement.cod_collected_amount
  target: table.zs_observe.delhivery_settlement
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
  edge_id: edge.metric_impl.delhivery_settlement.cod_collected_amount.uses_column.column.zs_observe.delhivery_settlement.cod_amount.8737448c
  edge_type: USES_COLUMN
  source: metric_impl.delhivery_settlement.cod_collected_amount
  target: column.zs_observe.delhivery_settlement.cod_amount
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
  edge_id: edge.metric_impl.delhivery_settlement.cod_collected_amount.uses_formula_template.formula_template.logistics.filtered_sum_amount
  edge_type: USES_FORMULA_TEMPLATE
  source: metric_impl.delhivery_settlement.cod_collected_amount
  target: formula_template.logistics.filtered_sum_amount
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
  edge_id: edge.metric.cod_remitted_amount.has_implementation.metric_impl.delhivery_settlement.cod_remitted_amount
  edge_type: HAS_IMPLEMENTATION
  source: metric.cod_remitted_amount
  target: metric_impl.delhivery_settlement.cod_remitted_amount
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
  edge_id: edge.metric_impl.delhivery_settlement.cod_remitted_amount.implements_metric.metric.cod_remitted_amount
  edge_type: IMPLEMENTS_METRIC
  source: metric_impl.delhivery_settlement.cod_remitted_amount
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
    materialized_from: edge.metric.cod_remitted_amount.has_implementation.metric_impl.delhivery_settlement.cod_remitted_amount
```

```yaml
candidate_edge:
  edge_id: edge.metric_impl.delhivery_settlement.cod_remitted_amount.uses_table.table.zs_observe.delhivery_settlement
  edge_type: USES_TABLE
  source: metric_impl.delhivery_settlement.cod_remitted_amount
  target: table.zs_observe.delhivery_settlement
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
  edge_id: edge.metric_impl.delhivery_settlement.cod_remitted_amount.uses_column.column.zs_observe.delhivery_settlement.payable.8737448c
  edge_type: USES_COLUMN
  source: metric_impl.delhivery_settlement.cod_remitted_amount
  target: column.zs_observe.delhivery_settlement.payable
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
  edge_id: edge.metric_impl.delhivery_settlement.cod_remitted_amount.uses_formula_template.formula_template.logistics.filtered_sum_amount
  edge_type: USES_FORMULA_TEMPLATE
  source: metric_impl.delhivery_settlement.cod_remitted_amount
  target: formula_template.logistics.filtered_sum_amount
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
  edge_id: edge.metric.qr_cod_remitted_amount.has_implementation.metric_impl.delhivery_settlement.qr_cod_remitted_amount
  edge_type: HAS_IMPLEMENTATION
  source: metric.qr_cod_remitted_amount
  target: metric_impl.delhivery_settlement.qr_cod_remitted_amount
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
  edge_id: edge.metric_impl.delhivery_settlement.qr_cod_remitted_amount.implements_metric.metric.qr_cod_remitted_amount
  edge_type: IMPLEMENTS_METRIC
  source: metric_impl.delhivery_settlement.qr_cod_remitted_amount
  target: metric.qr_cod_remitted_amount
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
    materialized_from: edge.metric.qr_cod_remitted_amount.has_implementation.metric_impl.delhivery_settlement.qr_cod_remitted_amount
```

```yaml
candidate_edge:
  edge_id: edge.metric_impl.delhivery_settlement.qr_cod_remitted_amount.uses_table.table.zs_observe.delhivery_settlement
  edge_type: USES_TABLE
  source: metric_impl.delhivery_settlement.qr_cod_remitted_amount
  target: table.zs_observe.delhivery_settlement
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
  edge_id: edge.metric_impl.delhivery_settlement.qr_cod_remitted_amount.uses_column.column.zs_observe.delhivery_settlement.payable.8737448c
  edge_type: USES_COLUMN
  source: metric_impl.delhivery_settlement.qr_cod_remitted_amount
  target: column.zs_observe.delhivery_settlement.payable
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
  edge_id: edge.metric_impl.delhivery_settlement.qr_cod_remitted_amount.uses_formula_template.formula_template.logistics.filtered_sum_amount
  edge_type: USES_FORMULA_TEMPLATE
  source: metric_impl.delhivery_settlement.qr_cod_remitted_amount
  target: formula_template.logistics.filtered_sum_amount
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
  edge_id: edge.metric.payable_amount.has_implementation.metric_impl.delhivery_settlement.payable_amount
  edge_type: HAS_IMPLEMENTATION
  source: metric.payable_amount
  target: metric_impl.delhivery_settlement.payable_amount
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
  edge_id: edge.metric_impl.delhivery_settlement.payable_amount.implements_metric.metric.payable_amount
  edge_type: IMPLEMENTS_METRIC
  source: metric_impl.delhivery_settlement.payable_amount
  target: metric.payable_amount
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
    materialized_from: edge.metric.payable_amount.has_implementation.metric_impl.delhivery_settlement.payable_amount
```

```yaml
candidate_edge:
  edge_id: edge.metric_impl.delhivery_settlement.payable_amount.uses_table.table.zs_observe.delhivery_settlement
  edge_type: USES_TABLE
  source: metric_impl.delhivery_settlement.payable_amount
  target: table.zs_observe.delhivery_settlement
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
  edge_id: edge.metric_impl.delhivery_settlement.payable_amount.uses_column.column.zs_observe.delhivery_settlement.payable.8737448c
  edge_type: USES_COLUMN
  source: metric_impl.delhivery_settlement.payable_amount
  target: column.zs_observe.delhivery_settlement.payable
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
  edge_id: edge.metric_impl.delhivery_settlement.payable_amount.uses_formula_template.formula_template.logistics.filtered_sum_amount
  edge_type: USES_FORMULA_TEMPLATE
  source: metric_impl.delhivery_settlement.payable_amount
  target: formula_template.logistics.filtered_sum_amount
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
  edge_id: edge.metric.cod_gap_amount.has_implementation.metric_impl.delhivery_settlement.cod_gap_amount
  edge_type: HAS_IMPLEMENTATION
  source: metric.cod_gap_amount
  target: metric_impl.delhivery_settlement.cod_gap_amount
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
  edge_id: edge.metric_impl.delhivery_settlement.cod_gap_amount.implements_metric.metric.cod_gap_amount
  edge_type: IMPLEMENTS_METRIC
  source: metric_impl.delhivery_settlement.cod_gap_amount
  target: metric.cod_gap_amount
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
    materialized_from: edge.metric.cod_gap_amount.has_implementation.metric_impl.delhivery_settlement.cod_gap_amount
```

```yaml
candidate_edge:
  edge_id: edge.metric_impl.delhivery_settlement.cod_gap_amount.uses_table.table.zs_observe.delhivery_settlement
  edge_type: USES_TABLE
  source: metric_impl.delhivery_settlement.cod_gap_amount
  target: table.zs_observe.delhivery_settlement
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
  edge_id: edge.metric_impl.delhivery_settlement.cod_gap_amount.uses_column.column.zs_observe.delhivery_settlement.cod_amount.8737448c
  edge_type: USES_COLUMN
  source: metric_impl.delhivery_settlement.cod_gap_amount
  target: column.zs_observe.delhivery_settlement.cod_amount
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
  edge_id: edge.metric_impl.delhivery_settlement.cod_gap_amount.uses_column.column.zs_observe.delhivery_settlement.payable.8737448c
  edge_type: USES_COLUMN
  source: metric_impl.delhivery_settlement.cod_gap_amount
  target: column.zs_observe.delhivery_settlement.payable
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
  edge_id: edge.metric_impl.delhivery_settlement.cod_gap_amount.uses_formula_template.formula_template.logistics.filtered_sum_amount
  edge_type: USES_FORMULA_TEMPLATE
  source: metric_impl.delhivery_settlement.cod_gap_amount
  target: formula_template.logistics.filtered_sum_amount
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
  edge_id: edge.metric.settlement_batch_count.has_implementation.metric_impl.delhivery_settlement.settlement_batch_count
  edge_type: HAS_IMPLEMENTATION
  source: metric.settlement_batch_count
  target: metric_impl.delhivery_settlement.settlement_batch_count
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
  edge_id: edge.metric_impl.delhivery_settlement.settlement_batch_count.implements_metric.metric.settlement_batch_count
  edge_type: IMPLEMENTS_METRIC
  source: metric_impl.delhivery_settlement.settlement_batch_count
  target: metric.settlement_batch_count
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
    materialized_from: edge.metric.settlement_batch_count.has_implementation.metric_impl.delhivery_settlement.settlement_batch_count
```

```yaml
candidate_edge:
  edge_id: edge.metric_impl.delhivery_settlement.settlement_batch_count.uses_table.table.zs_observe.delhivery_settlement
  edge_type: USES_TABLE
  source: metric_impl.delhivery_settlement.settlement_batch_count
  target: table.zs_observe.delhivery_settlement
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
  edge_id: edge.metric_impl.delhivery_settlement.settlement_batch_count.uses_column.column.zs_observe.delhivery_settlement.remittance_number.340e855f
  edge_type: USES_COLUMN
  source: metric_impl.delhivery_settlement.settlement_batch_count
  target: column.zs_observe.delhivery_settlement.remittance_number
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
  edge_id: edge.metric_impl.delhivery_settlement.settlement_batch_count.uses_formula_template.formula_template.logistics.filtered_sum_amount
  edge_type: USES_FORMULA_TEMPLATE
  source: metric_impl.delhivery_settlement.settlement_batch_count
  target: formula_template.logistics.filtered_sum_amount
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
  edge_id: edge.metric.unique_awb_count.has_implementation.metric_impl.delhivery_settlement.unique_awb_count
  edge_type: HAS_IMPLEMENTATION
  source: metric.unique_awb_count
  target: metric_impl.delhivery_settlement.unique_awb_count
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
  edge_id: edge.metric_impl.delhivery_settlement.unique_awb_count.implements_metric.metric.unique_awb_count
  edge_type: IMPLEMENTS_METRIC
  source: metric_impl.delhivery_settlement.unique_awb_count
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
    materialized_from: edge.metric.unique_awb_count.has_implementation.metric_impl.delhivery_settlement.unique_awb_count
```

```yaml
candidate_edge:
  edge_id: edge.metric_impl.delhivery_settlement.unique_awb_count.uses_table.table.zs_observe.delhivery_settlement
  edge_type: USES_TABLE
  source: metric_impl.delhivery_settlement.unique_awb_count
  target: table.zs_observe.delhivery_settlement
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
  edge_id: edge.metric_impl.delhivery_settlement.unique_awb_count.uses_column.column.zs_observe.delhivery_settlement.waybill_num.9e2adfd1
  edge_type: USES_COLUMN
  source: metric_impl.delhivery_settlement.unique_awb_count
  target: column.zs_observe.delhivery_settlement.waybill_num
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
  edge_id: edge.metric_impl.delhivery_settlement.unique_awb_count.uses_formula_template.formula_template.logistics.filtered_sum_amount
  edge_type: USES_FORMULA_TEMPLATE
  source: metric_impl.delhivery_settlement.unique_awb_count
  target: formula_template.logistics.filtered_sum_amount
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

## 6. Review Items

```yaml
review_item:
  id: review.delhivery_logistics_parser_ready_v6_role_split.business_flow_boundary
  topic: Business Flow Binding boundary
  instruction: No Business Flow Binding, tenant, group, platform account, or account data binding cards should be emitted
    from this generic logistics document.
  severity: high
  status: open_for_ingestion_validation
```

## 7. Validation Summary

```yaml
validation_summary:
  document_id: delhivery_logistics_parser_ready_v6_role_split
  candidate_cards: 114
  candidate_edges: 309
  card_types:
    metric: 24
    platform: 1
    platform_context: 1
    table: 2
    column: 53
    relationship: 2
    value_profile: 6
    metric_implementation: 25
  edge_types:
    BELONGS_TO_DOMAIN: 24
    BELONGS_TO_PLATFORM: 1
    HAS_PLATFORM_CONTEXT: 1
    SOURCED_FROM_PLATFORM: 2
    APPLIES_TO_PLATFORM: 2
    HAS_COLUMN: 53
    BELONGS_TO_TABLE: 53
    HAS_RELATIONSHIP: 4
    SOURCE_TABLE: 2
    TARGET_TABLE: 2
    USES_SOURCE_COLUMN: 2
    USES_TARGET_COLUMN: 2
    HAS_VALUE_PROFILE: 12
    PROFILES_COLUMN: 6
    PROFILES_TABLE: 6
    HAS_IMPLEMENTATION: 25
    IMPLEMENTS_METRIC: 25
    USES_TABLE: 25
    USES_COLUMN: 37
    USES_FORMULA_TEMPLATE: 25
  forbidden_card_types_present: []
  parser_boundary: generic logistics reusable knowledge only
```
