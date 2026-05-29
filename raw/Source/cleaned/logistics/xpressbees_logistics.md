# XpressBees Logistics Knowledge — Parser Ready v6 Role-Split Manifest-Aligned Unified Edges
## 0. Document Metadata
```yaml
document_metadata:
  document_id: xpressbees_logistics_parser_ready_v6_role_split
  title: XpressBees Logistics Knowledge — Parser Ready v6 Role-Split Manifest-Aligned Unified Edges
  domain: logistics
  vendor: XpressBees
  source_docx: /mnt/data/Logistics KB Doc.docx
  frame_of_reference: logistics_gold_std_canonical_card_frame_v5 plus flipkart_v8_unified_edges_style plus marketplace_cleanup_manifest_consolidated_v2
  generated_on: '2026-05-24'
  version: 6.0-role-split-manifest-aligned-unified-edges
  scope: xpressbees_vendor_logistics_with_unified_edges
  logistics_only: true
  allowed_card_types:
  - column
  - metric
  - metric_implementation
  - platform
  - platform_context
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
  id: evidence.xpressbees.vendor_scope
  source_document: Logistics KB Doc.docx
  summary: 'Vendor-specific extracted evidence for xpressbees: table role, coverage status, metrics, caveats, and joins.'
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
  source_evidence_id: ev.xpressbees.tables.settlement_sparse
  source_document: Logistics KB Doc.docx
  source_section: Tables DTDC, Ekart, XpressBees / Table 5 zs_observe.xpressbees_settlement / Overview, Key Fields, Enriched Data, Data Quality Issues, Workaround for Reconciliation, Join Patterns
  evidence_type: caveat
  supported_semantics:
  - XpressBees native settlement is sparse/partial/low-confidence
  - shipping_id is mostly null and native analysis requires populated-field validation
  - Shiprocket fallback is preferred for normal reconciliation
  unsupported_semantics:
  - blindly using native XpressBees settlement as authoritative COD remittance evidence
  allowed_card_types:
  - table
  - column
  - metric_implementation
  - value_profile
  - rule
  - validation_test
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
  vendor: XpressBees
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
  vendor: xpressbees
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
  vendor: xpressbees
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
  review_id: review.xpressbees.native_sparse_fallback_preferred
  source_manifest: metric_implementation_manifest
  severity: high
  status: accepted_guardrail
  applies_to:
  - table.zs_observe.xpressbees_settlement
  finding: XpressBees native settlement is sparse/low-confidence; Shiprocket fallback is preferred for normal reconciliation unless the user asks for native-source validation.
  deterministic_action: Keep native implementations low_confidence and fallback implementations active where documented.
```


## 4. Candidate Cards

### 4.1 platform cards

```yaml
candidate_card:
  card_type: platform
  card_id: platform.xpressbees
  name: XpressBees
  fields:
    name: XpressBees
    description: XpressBees logistics platform/vendor in the logistics domain.
    status: active
    confidence: curated
    source_documents:
    - Logistics KB Doc.docx
    - Cognee KB Design v4.md
    - logistics_gold_std_raw_md_frame_v3.md
    - logistics_gold_std_canonical_card_frame_v5.md
    created_by: kb_authoring_assistant
    updated_by: kb_authoring_assistant
    version: 5.0-manifest-aligned
    platform_name: XpressBees
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
  card_id: platform_context.xpressbees.in
  name: XpressBees India
  fields:
    name: XpressBees India
    description: India logistics context for XpressBees.
    status: active
    confidence: curated
    source_documents:
    - Logistics KB Doc.docx
    - Cognee KB Design v4.md
    - logistics_gold_std_raw_md_frame_v3.md
    - logistics_gold_std_canonical_card_frame_v5.md
    created_by: kb_authoring_assistant
    updated_by: kb_authoring_assistant
    version: 5.0-manifest-aligned
    platform_id: platform.xpressbees
    context_name: XpressBees India
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
  card_id: table.zs_observe.xpressbees_settlement
  name: XpressBees Settlement
  fields:
    name: XpressBees Settlement
    description: 'XpressBees Settlement: XpressBees native settlement rows; most operational/financial fields are sparse.'
    status: active
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
    table_name: xpressbees_settlement
    full_reference: zs_observe.xpressbees_settlement
    engine: Athena v3 / Trino SQL
    table_type: low_confidence_cod_settlement
    source_platform_ids:
    - platform.xpressbees
    source_platform_types:
    - logistics
    business_purpose: XpressBees native settlement rows; most operational/financial fields are sparse.
    grain: XpressBees native settlement rows; most operational/financial fields are sparse.
    grain_keys:
    - awb/order/reference as specified by columns
    date_columns:
    - see date column cards
    recommended_date_columns:
    - see metric implementations
    avoid_columns:
    - see amount semantics caveats
    structural_applicability: platform.xpressbees; account filters are not defined here
    coverage_status: partial_low_confidence
    row_count: '3487'
    period: Jan-Nov 2025
    group_ids: '22'
    schema_coverage: only 56 enriched rows; 98.4% sparse; fallback Shiprocket settlement preferred
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
  card_id: column.zs_observe.xpressbees_settlement.order_id
  name: xpressbees_settlement.order_id
  fields:
    name: xpressbees_settlement.order_id
    description: 15-digit XpressBees order reference.
    status: active
    confidence: curated
    source_documents:
    - Logistics KB Doc.docx
    - Cognee KB Design v4.md
    - logistics_gold_std_raw_md_frame_v3.md
    - logistics_gold_std_canonical_card_frame_v5.md
    created_by: kb_authoring_assistant
    updated_by: kb_authoring_assistant
    version: 5.0-manifest-aligned
    table_id: table.zs_observe.xpressbees_settlement
    column_name: order_id
    data_type: unknown
    semantic_roles: identifier
    business_concepts:
    - 15-digit XpressBees order reference.
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
  card_id: column.zs_observe.xpressbees_settlement.shipping_id
  name: xpressbees_settlement.shipping_id
  fields:
    name: xpressbees_settlement.shipping_id
    description: XpressBees AWB, mostly null.
    status: active
    confidence: curated
    source_documents:
    - Logistics KB Doc.docx
    - Cognee KB Design v4.md
    - logistics_gold_std_raw_md_frame_v3.md
    - logistics_gold_std_canonical_card_frame_v5.md
    created_by: kb_authoring_assistant
    updated_by: kb_authoring_assistant
    version: 5.0-manifest-aligned
    table_id: table.zs_observe.xpressbees_settlement
    column_name: shipping_id
    data_type: unknown
    semantic_roles: identifier;join_key;reconciliation_key
    business_concepts:
    - XpressBees AWB, mostly null.
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
  card_id: column.zs_observe.xpressbees_settlement.service_type
  name: xpressbees_settlement.service_type
  fields:
    name: xpressbees_settlement.service_type
    description: COD when populated.
    status: active
    confidence: curated
    source_documents:
    - Logistics KB Doc.docx
    - Cognee KB Design v4.md
    - logistics_gold_std_raw_md_frame_v3.md
    - logistics_gold_std_canonical_card_frame_v5.md
    created_by: kb_authoring_assistant
    updated_by: kb_authoring_assistant
    version: 5.0-manifest-aligned
    table_id: table.zs_observe.xpressbees_settlement
    column_name: service_type
    data_type: unknown
    semantic_roles: dimension;filter
    business_concepts:
    - COD when populated.
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
  card_id: column.zs_observe.xpressbees_settlement.shipment_status
  name: xpressbees_settlement.shipment_status
  fields:
    name: xpressbees_settlement.shipment_status
    description: Delivered when populated.
    status: active
    confidence: curated
    source_documents:
    - Logistics KB Doc.docx
    - Cognee KB Design v4.md
    - logistics_gold_std_raw_md_frame_v3.md
    - logistics_gold_std_canonical_card_frame_v5.md
    created_by: kb_authoring_assistant
    updated_by: kb_authoring_assistant
    version: 5.0-manifest-aligned
    table_id: table.zs_observe.xpressbees_settlement
    column_name: shipment_status
    data_type: unknown
    semantic_roles: status;filter
    business_concepts:
    - Delivered when populated.
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
  card_id: column.zs_observe.xpressbees_settlement.transaction_type
  name: xpressbees_settlement.transaction_type
  fields:
    name: xpressbees_settlement.transaction_type
    description: COD for rows.
    status: active
    confidence: curated
    source_documents:
    - Logistics KB Doc.docx
    - Cognee KB Design v4.md
    - logistics_gold_std_raw_md_frame_v3.md
    - logistics_gold_std_canonical_card_frame_v5.md
    created_by: kb_authoring_assistant
    updated_by: kb_authoring_assistant
    version: 5.0-manifest-aligned
    table_id: table.zs_observe.xpressbees_settlement
    column_name: transaction_type
    data_type: unknown
    semantic_roles: status;filter
    business_concepts:
    - COD for rows.
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
  card_id: column.zs_observe.xpressbees_settlement.transaction_date
  name: xpressbees_settlement.transaction_date
  fields:
    name: xpressbees_settlement.transaction_date
    description: Remittance date, mostly null.
    status: active
    confidence: curated
    source_documents:
    - Logistics KB Doc.docx
    - Cognee KB Design v4.md
    - logistics_gold_std_raw_md_frame_v3.md
    - logistics_gold_std_canonical_card_frame_v5.md
    created_by: kb_authoring_assistant
    updated_by: kb_authoring_assistant
    version: 5.0-manifest-aligned
    table_id: table.zs_observe.xpressbees_settlement
    column_name: transaction_date
    data_type: unknown
    semantic_roles: date
    business_concepts:
    - Remittance date, mostly null.
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
  card_id: column.zs_observe.xpressbees_settlement.net_payment
  name: xpressbees_settlement.net_payment
  fields:
    name: xpressbees_settlement.net_payment
    description: COD amount remitted when populated.
    status: active
    confidence: curated
    source_documents:
    - Logistics KB Doc.docx
    - Cognee KB Design v4.md
    - logistics_gold_std_raw_md_frame_v3.md
    - logistics_gold_std_canonical_card_frame_v5.md
    created_by: kb_authoring_assistant
    updated_by: kb_authoring_assistant
    version: 5.0-manifest-aligned
    table_id: table.zs_observe.xpressbees_settlement
    column_name: net_payment
    data_type: unknown
    semantic_roles: measure
    business_concepts:
    - COD amount remitted when populated.
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
  card_id: column.zs_observe.xpressbees_settlement.poid
  name: xpressbees_settlement.poid
  fields:
    name: xpressbees_settlement.poid
    description: Purchase order ID, mostly null.
    status: active
    confidence: curated
    source_documents:
    - Logistics KB Doc.docx
    - Cognee KB Design v4.md
    - logistics_gold_std_raw_md_frame_v3.md
    - logistics_gold_std_canonical_card_frame_v5.md
    created_by: kb_authoring_assistant
    updated_by: kb_authoring_assistant
    version: 5.0-manifest-aligned
    table_id: table.zs_observe.xpressbees_settlement
    column_name: poid
    data_type: unknown
    semantic_roles: identifier
    business_concepts:
    - Purchase order ID, mostly null.
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
  card_id: column.zs_observe.xpressbees_settlement.company
  name: xpressbees_settlement.company
  fields:
    name: xpressbees_settlement.company
    description: XpressBees company entity, mostly null.
    status: active
    confidence: curated
    source_documents:
    - Logistics KB Doc.docx
    - Cognee KB Design v4.md
    - logistics_gold_std_raw_md_frame_v3.md
    - logistics_gold_std_canonical_card_frame_v5.md
    created_by: kb_authoring_assistant
    updated_by: kb_authoring_assistant
    version: 5.0-manifest-aligned
    table_id: table.zs_observe.xpressbees_settlement
    column_name: company
    data_type: unknown
    semantic_roles: dimension
    business_concepts:
    - XpressBees company entity, mostly null.
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
  card_id: column.zs_observe.xpressbees_settlement.hub_name
  name: xpressbees_settlement.hub_name
  fields:
    name: xpressbees_settlement.hub_name
    description: Hub name, mostly null.
    status: active
    confidence: curated
    source_documents:
    - Logistics KB Doc.docx
    - Cognee KB Design v4.md
    - logistics_gold_std_raw_md_frame_v3.md
    - logistics_gold_std_canonical_card_frame_v5.md
    created_by: kb_authoring_assistant
    updated_by: kb_authoring_assistant
    version: 5.0-manifest-aligned
    table_id: table.zs_observe.xpressbees_settlement
    column_name: hub_name
    data_type: unknown
    semantic_roles: dimension
    business_concepts:
    - Hub name, mostly null.
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
  card_id: column.zs_observe.xpressbees_settlement.delivery_date
  name: xpressbees_settlement.delivery_date
  fields:
    name: xpressbees_settlement.delivery_date
    description: Delivery date.
    status: active
    confidence: curated
    source_documents:
    - Logistics KB Doc.docx
    - Cognee KB Design v4.md
    - logistics_gold_std_raw_md_frame_v3.md
    - logistics_gold_std_canonical_card_frame_v5.md
    created_by: kb_authoring_assistant
    updated_by: kb_authoring_assistant
    version: 5.0-manifest-aligned
    table_id: table.zs_observe.xpressbees_settlement
    column_name: delivery_date
    data_type: unknown
    semantic_roles: date
    business_concepts:
    - Delivery date.
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
  card_id: column.zs_observe.xpressbees_settlement.is_active
  name: xpressbees_settlement.is_active
  fields:
    name: xpressbees_settlement.is_active
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
    table_id: table.zs_observe.xpressbees_settlement
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
  card_id: column.zs_observe.xpressbees_settlement.group_level_id
  name: xpressbees_settlement.group_level_id
  fields:
    name: xpressbees_settlement.group_level_id
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
    table_id: table.zs_observe.xpressbees_settlement
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

### 4.7 value_profile cards

```yaml
candidate_card:
  card_type: value_profile
  card_id: value_profile.xpressbees_settlement.service_type
  name: xpressbees_settlement.service_type Value Profile
  fields:
    name: xpressbees_settlement.service_type Value Profile
    description: Known values and meanings for xpressbees_settlement.service_type.
    status: active
    confidence: curated
    source_documents:
    - Logistics KB Doc.docx
    - Cognee KB Design v4.md
    - logistics_gold_std_raw_md_frame_v3.md
    - logistics_gold_std_canonical_card_frame_v5.md
    created_by: kb_authoring_assistant
    updated_by: kb_authoring_assistant
    version: 5.0-manifest-aligned
    table_id: table.zs_observe.xpressbees_settlement
    column_id: column.zs_observe.xpressbees_settlement.service_type
    value_type: enum_or_enum_with_nulls
    values: COD=COD service when populated (cod); NULL=Sparse/unmapped row (unknown)
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
  card_id: value_profile.xpressbees_settlement.shipment_status
  name: xpressbees_settlement.shipment_status Value Profile
  fields:
    name: xpressbees_settlement.shipment_status Value Profile
    description: Known values and meanings for xpressbees_settlement.shipment_status.
    status: active
    confidence: curated
    source_documents:
    - Logistics KB Doc.docx
    - Cognee KB Design v4.md
    - logistics_gold_std_raw_md_frame_v3.md
    - logistics_gold_std_canonical_card_frame_v5.md
    created_by: kb_authoring_assistant
    updated_by: kb_authoring_assistant
    version: 5.0-manifest-aligned
    table_id: table.zs_observe.xpressbees_settlement
    column_id: column.zs_observe.xpressbees_settlement.shipment_status
    value_type: enum_or_enum_with_nulls
    values: Delivered=Delivered shipment when populated (delivered); NULL=Sparse/unmapped row (unknown)
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
  card_id: value_profile.xpressbees_settlement.transaction_type
  name: xpressbees_settlement.transaction_type Value Profile
  fields:
    name: xpressbees_settlement.transaction_type Value Profile
    description: Known values and meanings for xpressbees_settlement.transaction_type.
    status: active
    confidence: curated
    source_documents:
    - Logistics KB Doc.docx
    - Cognee KB Design v4.md
    - logistics_gold_std_raw_md_frame_v3.md
    - logistics_gold_std_canonical_card_frame_v5.md
    created_by: kb_authoring_assistant
    updated_by: kb_authoring_assistant
    version: 5.0-manifest-aligned
    table_id: table.zs_observe.xpressbees_settlement
    column_id: column.zs_observe.xpressbees_settlement.transaction_type
    value_type: enum_or_enum_with_nulls
    values: COD=COD settlement row (cod)
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
    - see metric_impl blocks in xpressbees_logistics_parser_ready_v6_role_split.md
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
    - see metric_impl blocks in xpressbees_logistics_parser_ready_v6_role_split.md
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
    - see metric_impl blocks in xpressbees_logistics_parser_ready_v6_role_split.md
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
    - see metric_impl blocks in xpressbees_logistics_parser_ready_v6_role_split.md
    evidence_refs:
    - evidence.logistics_kb_doc
    - evidence.cognee_design_v4
    - evidence.unified_edge_scope
```

```yaml
candidate_card:
  card_type: metric
  card_id: metric.populated_native_record_count
  name: Populated Native Record Count
  fields:
    name: Populated Native Record Count
    description: Count of native vendor rows with populated key fields.
    status: active
    confidence: curated
    source_documents:
    - Logistics KB Doc.docx
    - Cognee KB Design v4.md
    - logistics_gold_std_raw_md_frame_v3.md
    - logistics_gold_std_canonical_card_frame_v5.md
    created_by: kb_authoring_assistant
    updated_by: kb_authoring_assistant
    version: 5.0-manifest-aligned
    metric_name: Populated Native Record Count
    aliases:
    - usable native rows
    metric_type: amount/count/rate/days_by_metric
    unit: currency/count/percentage/days_by_metric
    default_aggregation: SUM or COUNT or ratio by metric
    default_grain: shipment_awb_or_settlement_batch
    polarity: context_dependent
    business_concepts:
    - logistics
    - populated_native_record_count
    domain_ids:
    - domain.logistics_reconciliation
    implementations:
    - see metric_impl blocks in xpressbees_logistics_parser_ready_v6_role_split.md
    evidence_refs:
    - evidence.logistics_kb_doc
    - evidence.cognee_design_v4
    - evidence.unified_edge_scope
```

```yaml
candidate_card:
  card_type: metric
  card_id: metric.sparse_native_record_count
  name: Sparse Native Record Count
  fields:
    name: Sparse Native Record Count
    description: Count of native vendor rows missing key operational/financial fields.
    status: active
    confidence: curated
    source_documents:
    - Logistics KB Doc.docx
    - Cognee KB Design v4.md
    - logistics_gold_std_raw_md_frame_v3.md
    - logistics_gold_std_canonical_card_frame_v5.md
    created_by: kb_authoring_assistant
    updated_by: kb_authoring_assistant
    version: 5.0-manifest-aligned
    metric_name: Sparse Native Record Count
    aliases:
    - records with missing key fields
    metric_type: amount/count/rate/days_by_metric
    unit: currency/count/percentage/days_by_metric
    default_aggregation: SUM or COUNT or ratio by metric
    default_grain: shipment_awb_or_settlement_batch
    polarity: context_dependent
    business_concepts:
    - logistics
    - sparse_native_record_count
    domain_ids:
    - domain.logistics_reconciliation
    implementations:
    - see metric_impl blocks in xpressbees_logistics_parser_ready_v6_role_split.md
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
    - see metric_impl blocks in xpressbees_logistics_parser_ready_v6_role_split.md
    evidence_refs:
    - evidence.logistics_kb_doc
    - evidence.cognee_design_v4
    - evidence.unified_edge_scope
```

### 4.9 metric_implementation cards

```yaml
candidate_card:
  card_type: metric_implementation
  card_id: metric_impl.xpressbees_settlement.populated_native_record_count
  name: XpressBees Populated Native Record Count Implementation
  fields:
    name: XpressBees Populated Native Record Count Implementation
    description: Populated Native Record Count implementation for XpressBees using xpressbees_settlement.
    status: active
    confidence: curated
    source_documents:
    - Logistics KB Doc.docx
    - Cognee KB Design v4.md
    - logistics_gold_std_raw_md_frame_v3.md
    - logistics_gold_std_canonical_card_frame_v5.md
    created_by: kb_authoring_assistant
    updated_by: kb_authoring_assistant
    version: 5.0-manifest-aligned
    metric_id: metric.populated_native_record_count
    implementation_name: XpressBees Populated Native Record Count
    metric_pattern: low_confidence_filtered_sum
    applicability: platform=xpressbees; table=zs_observe.xpressbees_settlement; account filters via Account Data Binding only
    base_tables:
    - table.zs_observe.xpressbees_settlement
    required_columns:
    - column.zs_observe.xpressbees_settlement.service_type
    - column.zs_observe.xpressbees_settlement.shipment_status
    - column.zs_observe.xpressbees_settlement.net_payment
    semantic_filters: []
    formula_description: COUNT_IF(service_type IS NOT NULL OR shipment_status IS NOT NULL OR net_payment IS NOT NULL)
    formula_sql: COUNT_IF(service_type IS NOT NULL OR shipment_status IS NOT NULL OR net_payment IS NOT NULL)
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
    - transaction_date
    - delivery_date
    unit: currency/count/percentage/days_by_metric
    precision: 2_decimal_places
    caveats: Native XpressBees table is sparse; fallback to Shiprocket settlement for Xpressbees Air when answering courier-level
      COD.
    evidence_refs:
    - evidence.logistics_kb_doc
    - evidence.cognee_design_v4
    - evidence.unified_edge_scope
    formula_template_id: formula_template.logistics.filtered_sum_amount
```

```yaml
candidate_card:
  card_type: metric_implementation
  card_id: metric_impl.xpressbees_settlement.sparse_native_record_count
  name: XpressBees Sparse Native Record Count Implementation
  fields:
    name: XpressBees Sparse Native Record Count Implementation
    description: Sparse Native Record Count implementation for XpressBees using xpressbees_settlement.
    status: active
    confidence: curated
    source_documents:
    - Logistics KB Doc.docx
    - Cognee KB Design v4.md
    - logistics_gold_std_raw_md_frame_v3.md
    - logistics_gold_std_canonical_card_frame_v5.md
    created_by: kb_authoring_assistant
    updated_by: kb_authoring_assistant
    version: 5.0-manifest-aligned
    metric_id: metric.sparse_native_record_count
    implementation_name: XpressBees Sparse Native Record Count
    metric_pattern: low_confidence_filtered_sum
    applicability: platform=xpressbees; table=zs_observe.xpressbees_settlement; account filters via Account Data Binding only
    base_tables:
    - table.zs_observe.xpressbees_settlement
    required_columns:
    - column.zs_observe.xpressbees_settlement.service_type
    - column.zs_observe.xpressbees_settlement.shipment_status
    - column.zs_observe.xpressbees_settlement.net_payment
    semantic_filters: []
    formula_description: COUNT_IF(service_type IS NULL AND shipment_status IS NULL AND net_payment IS NULL)
    formula_sql: COUNT_IF(service_type IS NULL AND shipment_status IS NULL AND net_payment IS NULL)
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
    - transaction_date
    - delivery_date
    unit: currency/count/percentage/days_by_metric
    precision: 2_decimal_places
    caveats: Native XpressBees table is sparse; fallback to Shiprocket settlement for Xpressbees Air when answering courier-level
      COD.
    evidence_refs:
    - evidence.logistics_kb_doc
    - evidence.cognee_design_v4
    - evidence.unified_edge_scope
    formula_template_id: formula_template.logistics.filtered_sum_amount
```

```yaml
candidate_card:
  card_type: metric_implementation
  card_id: metric_impl.xpressbees_settlement.cod_remitted_amount
  name: XpressBees COD Remitted Amount Implementation
  fields:
    name: XpressBees COD Remitted Amount Implementation
    description: COD Remitted Amount implementation for XpressBees using xpressbees_settlement.
    status: active
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
    implementation_name: XpressBees COD Remitted Amount
    metric_pattern: low_confidence_filtered_sum
    applicability: platform=xpressbees; table=zs_observe.xpressbees_settlement; account filters via Account Data Binding only
    base_tables:
    - table.zs_observe.xpressbees_settlement
    required_columns:
    - column.zs_observe.xpressbees_settlement.net_payment
    semantic_filters:
    - service_type='COD' AND shipment_status='Delivered'
    formula_description: SUM(net_payment)
    formula_sql: SUM(net_payment)
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
    - transaction_date
    - delivery_date
    unit: currency/count/percentage/days_by_metric
    precision: 2_decimal_places
    caveats: Native XpressBees table is sparse; fallback to Shiprocket settlement for Xpressbees Air when answering courier-level
      COD.
    evidence_refs:
    - evidence.logistics_kb_doc
    - evidence.cognee_design_v4
    - evidence.unified_edge_scope
    formula_template_id: formula_template.logistics.filtered_sum_amount
```

```yaml
candidate_card:
  card_type: metric_implementation
  card_id: metric_impl.xpressbees_settlement.unique_awb_count
  name: XpressBees Unique AWB Count Implementation
  fields:
    name: XpressBees Unique AWB Count Implementation
    description: Unique AWB Count implementation for XpressBees using xpressbees_settlement.
    status: active
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
    implementation_name: XpressBees Unique AWB Count
    metric_pattern: low_confidence_filtered_sum
    applicability: platform=xpressbees; table=zs_observe.xpressbees_settlement; account filters via Account Data Binding only
    base_tables:
    - table.zs_observe.xpressbees_settlement
    required_columns:
    - column.zs_observe.xpressbees_settlement.shipping_id
    semantic_filters:
    - shipping_id IS NOT NULL
    formula_description: COUNT(DISTINCT shipping_id)
    formula_sql: COUNT(DISTINCT shipping_id)
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
    - transaction_date
    - delivery_date
    unit: currency/count/percentage/days_by_metric
    precision: 2_decimal_places
    caveats: Native XpressBees table is sparse; fallback to Shiprocket settlement for Xpressbees Air when answering courier-level
      COD.
    evidence_refs:
    - evidence.logistics_kb_doc
    - evidence.cognee_design_v4
    - evidence.unified_edge_scope
    formula_template_id: formula_template.logistics.filtered_sum_amount
```

```yaml
candidate_card:
  card_type: metric_implementation
  card_id: metric_impl.xpressbees_settlement.delivered_shipment_count
  name: XpressBees Delivered Shipment Count Implementation
  fields:
    name: XpressBees Delivered Shipment Count Implementation
    description: Delivered Shipment Count implementation for XpressBees using xpressbees_settlement.
    status: active
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
    implementation_name: XpressBees Delivered Shipment Count
    metric_pattern: low_confidence_filtered_sum
    applicability: platform=xpressbees; table=zs_observe.xpressbees_settlement; account filters via Account Data Binding only
    base_tables:
    - table.zs_observe.xpressbees_settlement
    required_columns:
    - column.zs_observe.xpressbees_settlement.shipment_status
    semantic_filters:
    - shipment_status='Delivered'
    formula_description: COUNT_IF(shipment_status='Delivered')
    formula_sql: COUNT_IF(shipment_status='Delivered')
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
    - transaction_date
    - delivery_date
    unit: currency/count/percentage/days_by_metric
    precision: 2_decimal_places
    caveats: Native XpressBees table is sparse; fallback to Shiprocket settlement for Xpressbees Air when answering courier-level
      COD.
    evidence_refs:
    - evidence.logistics_kb_doc
    - evidence.cognee_design_v4
    - evidence.unified_edge_scope
    formula_template_id: formula_template.logistics.filtered_sum_amount
```

```yaml
candidate_card:
  card_type: metric_implementation
  card_id: metric_impl.xpressbees_settlement.cod_collected_amount
  name: XpressBees COD Collected Amount Implementation
  fields:
    name: XpressBees COD Collected Amount Implementation
    description: COD Collected Amount implementation for XpressBees using xpressbees_settlement.
    status: active
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
    implementation_name: XpressBees COD Collected Amount
    metric_pattern: low_confidence_filtered_sum
    applicability: platform=xpressbees; table=zs_observe.xpressbees_settlement; account filters via Account Data Binding only
    base_tables:
    - table.zs_observe.xpressbees_settlement
    required_columns:
    - column.zs_observe.xpressbees_settlement.net_payment
    semantic_filters:
    - service_type='COD' AND shipment_status='Delivered'
    formula_description: SUM(net_payment)
    formula_sql: SUM(net_payment)
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
    - transaction_date
    - delivery_date
    unit: currency/count/percentage/days_by_metric
    precision: 2_decimal_places
    caveats: Native XpressBees table is sparse; fallback to Shiprocket settlement for Xpressbees Air when answering courier-level
      COD.
    evidence_refs:
    - evidence.logistics_kb_doc
    - evidence.cognee_design_v4
    - evidence.unified_edge_scope
    formula_template_id: formula_template.logistics.filtered_sum_amount
```

```yaml
candidate_card:
  card_type: metric_implementation
  card_id: metric_impl.shiprocket_settlement.xpressbees_air.cod_remitted_amount
  name: XpressBees COD Remitted Amount Implementation
  fields:
    name: XpressBees COD Remitted Amount Implementation
    description: COD Remitted Amount implementation for XpressBees using shiprocket_settlement.
    status: active
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
    implementation_name: XpressBees COD Remitted Amount
    metric_pattern: fallback_filtered_sum
    applicability: platform=xpressbees; table=zs_observe.shiprocket_settlement; account filters via Account Data Binding only
    base_tables:
    - table.zs_observe.shiprocket_settlement
    required_columns:
    - column.zs_observe.shiprocket_settlement.charged_amount
    - column.zs_observe.shiprocket_settlement.courier_partner
    semantic_filters:
    - courier_partner='Xpressbees Air'
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
    unit: currency/count/percentage/days_by_metric
    precision: 2_decimal_places
    caveats: Preferred fallback for XpressBees COD because native table has mostly null key fields.
    evidence_refs:
    - evidence.logistics_kb_doc
    - evidence.cognee_design_v4
    - evidence.unified_edge_scope
    formula_template_id: formula_template.logistics.filtered_sum_amount
```

```yaml
candidate_card:
  card_type: metric_implementation
  card_id: metric_impl.shiprocket_invoice.xpressbees_air.freight_billed_amount
  name: XpressBees Freight Billed Amount Implementation
  fields:
    name: XpressBees Freight Billed Amount Implementation
    description: Freight Billed Amount implementation for XpressBees using shiprocket_invoice.
    status: active
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
    implementation_name: XpressBees Freight Billed Amount
    metric_pattern: fallback_filtered_sum
    applicability: platform=xpressbees; table=zs_observe.shiprocket_invoice; account filters via Account Data Binding only
    base_tables:
    - table.zs_observe.shiprocket_invoice
    required_columns:
    - column.zs_observe.shiprocket_invoice.charged_amount
    - column.zs_observe.shiprocket_invoice.courier_partner
    semantic_filters:
    - courier_partner='Xpressbees Air'
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
  edge_id: edge.metric.populated_native_record_count.belongs_to_domain.domain.logistics_reconciliation
  edge_type: BELONGS_TO_DOMAIN
  source: metric.populated_native_record_count
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
  edge_id: edge.metric.sparse_native_record_count.belongs_to_domain.domain.logistics_reconciliation
  edge_type: BELONGS_TO_DOMAIN
  source: metric.sparse_native_record_count
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
  edge_id: edge.platform_context.xpressbees.in.belongs_to_platform.platform.xpressbees
  edge_type: BELONGS_TO_PLATFORM
  source: platform_context.xpressbees.in
  target: platform.xpressbees
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
  edge_id: edge.platform.xpressbees.has_platform_context.platform_context.xpressbees.in
  edge_type: HAS_PLATFORM_CONTEXT
  source: platform.xpressbees
  target: platform_context.xpressbees.in
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
    materialized_from: edge.platform_context.xpressbees.in.belongs_to_platform.platform.xpressbees
```

```yaml
candidate_edge:
  edge_id: edge.table.zs_observe.xpressbees_settlement.sourced_from_platform.platform.xpressbees
  edge_type: SOURCED_FROM_PLATFORM
  source: table.zs_observe.xpressbees_settlement
  target: platform.xpressbees
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
  edge_id: edge.table.zs_observe.xpressbees_settlement.applies_to_platform.platform.xpressbees
  edge_type: APPLIES_TO_PLATFORM
  source: table.zs_observe.xpressbees_settlement
  target: platform.xpressbees
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
  edge_id: edge.table.zs_observe.xpressbees_settlement.has_column.column.zs_observe.xpressbees_settlement.order_id
  edge_type: HAS_COLUMN
  source: table.zs_observe.xpressbees_settlement
  target: column.zs_observe.xpressbees_settlement.order_id
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
  edge_id: edge.column.zs_observe.xpressbees_settlement.order_id.belongs_to_table.table.zs_observe.xpressbees_settlement
  edge_type: BELONGS_TO_TABLE
  source: column.zs_observe.xpressbees_settlement.order_id
  target: table.zs_observe.xpressbees_settlement
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
    materialized_from: edge.table.zs_observe.xpressbees_settlement.has_column.column.zs_observe.xpressbees_settlement.order_id
```

```yaml
candidate_edge:
  edge_id: edge.table.zs_observe.xpressbees_settlement.has_column.column.zs_observe.xpressbees_settlement.shipping_id
  edge_type: HAS_COLUMN
  source: table.zs_observe.xpressbees_settlement
  target: column.zs_observe.xpressbees_settlement.shipping_id
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
  edge_id: edge.column.zs_observe.xpressbees_settlement.shipping_id.belongs_to_table.table.zs_observe.xpressbees_settlement
  edge_type: BELONGS_TO_TABLE
  source: column.zs_observe.xpressbees_settlement.shipping_id
  target: table.zs_observe.xpressbees_settlement
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
    materialized_from: edge.table.zs_observe.xpressbees_settlement.has_column.column.zs_observe.xpressbees_settlement.shipping_id
```

```yaml
candidate_edge:
  edge_id: edge.table.zs_observe.xpressbees_settlement.has_column.column.zs_observe.xpressbees_settlement.service_type
  edge_type: HAS_COLUMN
  source: table.zs_observe.xpressbees_settlement
  target: column.zs_observe.xpressbees_settlement.service_type
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
  edge_id: edge.column.zs_observe.xpressbees_settlement.service_type.belongs_to_table.table.zs_observe.xpressbees_settlement
  edge_type: BELONGS_TO_TABLE
  source: column.zs_observe.xpressbees_settlement.service_type
  target: table.zs_observe.xpressbees_settlement
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
    materialized_from: edge.table.zs_observe.xpressbees_settlement.has_column.column.zs_observe.xpressbees_settlement.service_type
```

```yaml
candidate_edge:
  edge_id: edge.table.zs_observe.xpressbees_settlement.has_column.column.zs_observe.xpressbees_settlement.shipment_status
  edge_type: HAS_COLUMN
  source: table.zs_observe.xpressbees_settlement
  target: column.zs_observe.xpressbees_settlement.shipment_status
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
  edge_id: edge.column.zs_observe.xpressbees_settlement.shipment_status.belongs_to_table.table.zs_observe.xpressbees_settlement
  edge_type: BELONGS_TO_TABLE
  source: column.zs_observe.xpressbees_settlement.shipment_status
  target: table.zs_observe.xpressbees_settlement
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
    materialized_from: edge.table.zs_observe.xpressbees_settlement.has_column.column.zs_observe.xpressbees_settlement.shipment_status
```

```yaml
candidate_edge:
  edge_id: edge.table.zs_observe.xpressbees_settlement.has_column.column.zs_observe.xpressbees_settlement.transaction_type
  edge_type: HAS_COLUMN
  source: table.zs_observe.xpressbees_settlement
  target: column.zs_observe.xpressbees_settlement.transaction_type
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
  edge_id: edge.column.zs_observe.xpressbees_settlement.transaction_type.belongs_to_table.table.zs_observe.xpressbees_settlement
  edge_type: BELONGS_TO_TABLE
  source: column.zs_observe.xpressbees_settlement.transaction_type
  target: table.zs_observe.xpressbees_settlement
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
    materialized_from: edge.table.zs_observe.xpressbees_settlement.has_column.column.zs_observe.xpressbees_settlement.transaction_type
```

```yaml
candidate_edge:
  edge_id: edge.table.zs_observe.xpressbees_settlement.has_column.column.zs_observe.xpressbees_settlement.transaction_date
  edge_type: HAS_COLUMN
  source: table.zs_observe.xpressbees_settlement
  target: column.zs_observe.xpressbees_settlement.transaction_date
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
  edge_id: edge.column.zs_observe.xpressbees_settlement.transaction_date.belongs_to_table.table.zs_observe.xpressbees_settlement
  edge_type: BELONGS_TO_TABLE
  source: column.zs_observe.xpressbees_settlement.transaction_date
  target: table.zs_observe.xpressbees_settlement
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
    materialized_from: edge.table.zs_observe.xpressbees_settlement.has_column.column.zs_observe.xpressbees_settlement.transaction_date
```

```yaml
candidate_edge:
  edge_id: edge.table.zs_observe.xpressbees_settlement.has_column.column.zs_observe.xpressbees_settlement.net_payment
  edge_type: HAS_COLUMN
  source: table.zs_observe.xpressbees_settlement
  target: column.zs_observe.xpressbees_settlement.net_payment
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
  edge_id: edge.column.zs_observe.xpressbees_settlement.net_payment.belongs_to_table.table.zs_observe.xpressbees_settlement
  edge_type: BELONGS_TO_TABLE
  source: column.zs_observe.xpressbees_settlement.net_payment
  target: table.zs_observe.xpressbees_settlement
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
    materialized_from: edge.table.zs_observe.xpressbees_settlement.has_column.column.zs_observe.xpressbees_settlement.net_payment
```

```yaml
candidate_edge:
  edge_id: edge.table.zs_observe.xpressbees_settlement.has_column.column.zs_observe.xpressbees_settlement.poid
  edge_type: HAS_COLUMN
  source: table.zs_observe.xpressbees_settlement
  target: column.zs_observe.xpressbees_settlement.poid
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
  edge_id: edge.column.zs_observe.xpressbees_settlement.poid.belongs_to_table.table.zs_observe.xpressbees_settlement
  edge_type: BELONGS_TO_TABLE
  source: column.zs_observe.xpressbees_settlement.poid
  target: table.zs_observe.xpressbees_settlement
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
    materialized_from: edge.table.zs_observe.xpressbees_settlement.has_column.column.zs_observe.xpressbees_settlement.poid
```

```yaml
candidate_edge:
  edge_id: edge.table.zs_observe.xpressbees_settlement.has_column.column.zs_observe.xpressbees_settlement.company
  edge_type: HAS_COLUMN
  source: table.zs_observe.xpressbees_settlement
  target: column.zs_observe.xpressbees_settlement.company
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
  edge_id: edge.column.zs_observe.xpressbees_settlement.company.belongs_to_table.table.zs_observe.xpressbees_settlement
  edge_type: BELONGS_TO_TABLE
  source: column.zs_observe.xpressbees_settlement.company
  target: table.zs_observe.xpressbees_settlement
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
    materialized_from: edge.table.zs_observe.xpressbees_settlement.has_column.column.zs_observe.xpressbees_settlement.company
```

```yaml
candidate_edge:
  edge_id: edge.table.zs_observe.xpressbees_settlement.has_column.column.zs_observe.xpressbees_settlement.hub_name
  edge_type: HAS_COLUMN
  source: table.zs_observe.xpressbees_settlement
  target: column.zs_observe.xpressbees_settlement.hub_name
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
  edge_id: edge.column.zs_observe.xpressbees_settlement.hub_name.belongs_to_table.table.zs_observe.xpressbees_settlement
  edge_type: BELONGS_TO_TABLE
  source: column.zs_observe.xpressbees_settlement.hub_name
  target: table.zs_observe.xpressbees_settlement
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
    materialized_from: edge.table.zs_observe.xpressbees_settlement.has_column.column.zs_observe.xpressbees_settlement.hub_name
```

```yaml
candidate_edge:
  edge_id: edge.table.zs_observe.xpressbees_settlement.has_column.column.zs_observe.xpressbees_settlement.delivery_date
  edge_type: HAS_COLUMN
  source: table.zs_observe.xpressbees_settlement
  target: column.zs_observe.xpressbees_settlement.delivery_date
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
  edge_id: edge.column.zs_observe.xpressbees_settlement.delivery_date.belongs_to_table.table.zs_observe.xpressbees_settlement
  edge_type: BELONGS_TO_TABLE
  source: column.zs_observe.xpressbees_settlement.delivery_date
  target: table.zs_observe.xpressbees_settlement
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
    materialized_from: edge.table.zs_observe.xpressbees_settlement.has_column.column.zs_observe.xpressbees_settlement.delivery_date
```

```yaml
candidate_edge:
  edge_id: edge.table.zs_observe.xpressbees_settlement.has_column.column.zs_observe.xpressbees_settlement.is_active
  edge_type: HAS_COLUMN
  source: table.zs_observe.xpressbees_settlement
  target: column.zs_observe.xpressbees_settlement.is_active
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
  edge_id: edge.column.zs_observe.xpressbees_settlement.is_active.belongs_to_table.table.zs_observe.xpressbees_settlement
  edge_type: BELONGS_TO_TABLE
  source: column.zs_observe.xpressbees_settlement.is_active
  target: table.zs_observe.xpressbees_settlement
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
    materialized_from: edge.table.zs_observe.xpressbees_settlement.has_column.column.zs_observe.xpressbees_settlement.is_active
```

```yaml
candidate_edge:
  edge_id: edge.table.zs_observe.xpressbees_settlement.has_column.column.zs_observe.xpressbees_settlement.group_level_id
  edge_type: HAS_COLUMN
  source: table.zs_observe.xpressbees_settlement
  target: column.zs_observe.xpressbees_settlement.group_level_id
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
  edge_id: edge.column.zs_observe.xpressbees_settlement.group_level_id.belongs_to_table.table.zs_observe.xpressbees_settlement
  edge_type: BELONGS_TO_TABLE
  source: column.zs_observe.xpressbees_settlement.group_level_id
  target: table.zs_observe.xpressbees_settlement
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
    materialized_from: edge.table.zs_observe.xpressbees_settlement.has_column.column.zs_observe.xpressbees_settlement.group_level_id
```

```yaml
candidate_edge:
  edge_id: edge.table.zs_observe.xpressbees_settlement.has_value_profile.value_profile.xpressbees_settlement.service_type
  edge_type: HAS_VALUE_PROFILE
  source: table.zs_observe.xpressbees_settlement
  target: value_profile.xpressbees_settlement.service_type
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
  edge_id: edge.value_profile.xpressbees_settlement.service_type.profiles_column.column.zs_observe.xpressbees_settlement.service_type
  edge_type: PROFILES_COLUMN
  source: value_profile.xpressbees_settlement.service_type
  target: column.zs_observe.xpressbees_settlement.service_type
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
  edge_id: edge.column.zs_observe.xpressbees_settlement.service_type.has_value_profile.value_profile.xpressbees_settlement.service_type
  edge_type: HAS_VALUE_PROFILE
  source: column.zs_observe.xpressbees_settlement.service_type
  target: value_profile.xpressbees_settlement.service_type
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
    materialized_from: edge.value_profile.xpressbees_settlement.service_type.profiles_column.column.zs_observe.xpressbees_settlement.service_type
```

```yaml
candidate_edge:
  edge_id: edge.value_profile.xpressbees_settlement.service_type.profiles_table.table.zs_observe.xpressbees_settlement
  edge_type: PROFILES_TABLE
  source: value_profile.xpressbees_settlement.service_type
  target: table.zs_observe.xpressbees_settlement
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
  edge_id: edge.table.zs_observe.xpressbees_settlement.has_value_profile.value_profile.xpressbees_settlement.shipment_status
  edge_type: HAS_VALUE_PROFILE
  source: table.zs_observe.xpressbees_settlement
  target: value_profile.xpressbees_settlement.shipment_status
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
  edge_id: edge.value_profile.xpressbees_settlement.shipment_status.profiles_column.column.zs_observe.xpressbees_settlement.shipment_status
  edge_type: PROFILES_COLUMN
  source: value_profile.xpressbees_settlement.shipment_status
  target: column.zs_observe.xpressbees_settlement.shipment_status
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
  edge_id: edge.column.zs_observe.xpressbees_settlement.shipment_status.has_value_profile.value_profile.xpressbees_settlement.shipment_status
  edge_type: HAS_VALUE_PROFILE
  source: column.zs_observe.xpressbees_settlement.shipment_status
  target: value_profile.xpressbees_settlement.shipment_status
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
    materialized_from: edge.value_profile.xpressbees_settlement.shipment_status.profiles_column.column.zs_observe.xpressbees_settlement.shipment_status
```

```yaml
candidate_edge:
  edge_id: edge.value_profile.xpressbees_settlement.shipment_status.profiles_table.table.zs_observe.xpressbees_settlement
  edge_type: PROFILES_TABLE
  source: value_profile.xpressbees_settlement.shipment_status
  target: table.zs_observe.xpressbees_settlement
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
  edge_id: edge.table.zs_observe.xpressbees_settlement.has_value_profile.value_profile.xpressbees_settlement.transaction_type
  edge_type: HAS_VALUE_PROFILE
  source: table.zs_observe.xpressbees_settlement
  target: value_profile.xpressbees_settlement.transaction_type
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
  edge_id: edge.value_profile.xpressbees_settlement.transaction_type.profiles_column.column.zs_observe.xpressbees_settlement.transaction_type
  edge_type: PROFILES_COLUMN
  source: value_profile.xpressbees_settlement.transaction_type
  target: column.zs_observe.xpressbees_settlement.transaction_type
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
  edge_id: edge.column.zs_observe.xpressbees_settlement.transaction_type.has_value_profile.value_profile.xpressbees_settlement.transaction_type
  edge_type: HAS_VALUE_PROFILE
  source: column.zs_observe.xpressbees_settlement.transaction_type
  target: value_profile.xpressbees_settlement.transaction_type
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
    materialized_from: edge.value_profile.xpressbees_settlement.transaction_type.profiles_column.column.zs_observe.xpressbees_settlement.transaction_type
```

```yaml
candidate_edge:
  edge_id: edge.value_profile.xpressbees_settlement.transaction_type.profiles_table.table.zs_observe.xpressbees_settlement
  edge_type: PROFILES_TABLE
  source: value_profile.xpressbees_settlement.transaction_type
  target: table.zs_observe.xpressbees_settlement
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
  edge_id: edge.metric.populated_native_record_count.has_implementation.metric_impl.xpressbees_settlement.populated_native_record_count
  edge_type: HAS_IMPLEMENTATION
  source: metric.populated_native_record_count
  target: metric_impl.xpressbees_settlement.populated_native_record_count
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
  edge_id: edge.metric_impl.xpressbees_settlement.populated_native_record_count.implements_metric.metric.populated_native_record_count
  edge_type: IMPLEMENTS_METRIC
  source: metric_impl.xpressbees_settlement.populated_native_record_count
  target: metric.populated_native_record_count
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
    materialized_from: edge.metric.populated_native_record_count.has_implementation.metric_impl.xpressbees_settlement.populated_native_record_count
```

```yaml
candidate_edge:
  edge_id: edge.metric_impl.xpressbees_settlement.populated_native_record_count.uses_table.table.zs_observe.xpressbees_settlement
  edge_type: USES_TABLE
  source: metric_impl.xpressbees_settlement.populated_native_record_count
  target: table.zs_observe.xpressbees_settlement
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
  edge_id: edge.metric_impl.xpressbees_settlement.populated_native_record_count.uses_column.column.zs_observe.xpressbees_settlement.service_type.28a8df7f
  edge_type: USES_COLUMN
  source: metric_impl.xpressbees_settlement.populated_native_record_count
  target: column.zs_observe.xpressbees_settlement.service_type
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
  edge_id: edge.metric_impl.xpressbees_settlement.populated_native_record_count.uses_column.column.zs_observe.xpressbees_settlement.shipment_status.28a8df7f
  edge_type: USES_COLUMN
  source: metric_impl.xpressbees_settlement.populated_native_record_count
  target: column.zs_observe.xpressbees_settlement.shipment_status
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
  edge_id: edge.metric_impl.xpressbees_settlement.populated_native_record_count.uses_column.column.zs_observe.xpressbees_settlement.net_payment.8737448c
  edge_type: USES_COLUMN
  source: metric_impl.xpressbees_settlement.populated_native_record_count
  target: column.zs_observe.xpressbees_settlement.net_payment
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
  edge_id: edge.metric_impl.xpressbees_settlement.populated_native_record_count.uses_formula_template.formula_template.logistics.filtered_sum_amount
  edge_type: USES_FORMULA_TEMPLATE
  source: metric_impl.xpressbees_settlement.populated_native_record_count
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
  edge_id: edge.metric.sparse_native_record_count.has_implementation.metric_impl.xpressbees_settlement.sparse_native_record_count
  edge_type: HAS_IMPLEMENTATION
  source: metric.sparse_native_record_count
  target: metric_impl.xpressbees_settlement.sparse_native_record_count
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
  edge_id: edge.metric_impl.xpressbees_settlement.sparse_native_record_count.implements_metric.metric.sparse_native_record_count
  edge_type: IMPLEMENTS_METRIC
  source: metric_impl.xpressbees_settlement.sparse_native_record_count
  target: metric.sparse_native_record_count
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
    materialized_from: edge.metric.sparse_native_record_count.has_implementation.metric_impl.xpressbees_settlement.sparse_native_record_count
```

```yaml
candidate_edge:
  edge_id: edge.metric_impl.xpressbees_settlement.sparse_native_record_count.uses_table.table.zs_observe.xpressbees_settlement
  edge_type: USES_TABLE
  source: metric_impl.xpressbees_settlement.sparse_native_record_count
  target: table.zs_observe.xpressbees_settlement
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
  edge_id: edge.metric_impl.xpressbees_settlement.sparse_native_record_count.uses_column.column.zs_observe.xpressbees_settlement.service_type.28a8df7f
  edge_type: USES_COLUMN
  source: metric_impl.xpressbees_settlement.sparse_native_record_count
  target: column.zs_observe.xpressbees_settlement.service_type
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
  edge_id: edge.metric_impl.xpressbees_settlement.sparse_native_record_count.uses_column.column.zs_observe.xpressbees_settlement.shipment_status.28a8df7f
  edge_type: USES_COLUMN
  source: metric_impl.xpressbees_settlement.sparse_native_record_count
  target: column.zs_observe.xpressbees_settlement.shipment_status
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
  edge_id: edge.metric_impl.xpressbees_settlement.sparse_native_record_count.uses_column.column.zs_observe.xpressbees_settlement.net_payment.8737448c
  edge_type: USES_COLUMN
  source: metric_impl.xpressbees_settlement.sparse_native_record_count
  target: column.zs_observe.xpressbees_settlement.net_payment
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
  edge_id: edge.metric_impl.xpressbees_settlement.sparse_native_record_count.uses_formula_template.formula_template.logistics.filtered_sum_amount
  edge_type: USES_FORMULA_TEMPLATE
  source: metric_impl.xpressbees_settlement.sparse_native_record_count
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
  edge_id: edge.metric.cod_remitted_amount.has_implementation.metric_impl.xpressbees_settlement.cod_remitted_amount
  edge_type: HAS_IMPLEMENTATION
  source: metric.cod_remitted_amount
  target: metric_impl.xpressbees_settlement.cod_remitted_amount
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
  edge_id: edge.metric_impl.xpressbees_settlement.cod_remitted_amount.implements_metric.metric.cod_remitted_amount
  edge_type: IMPLEMENTS_METRIC
  source: metric_impl.xpressbees_settlement.cod_remitted_amount
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
    materialized_from: edge.metric.cod_remitted_amount.has_implementation.metric_impl.xpressbees_settlement.cod_remitted_amount
```

```yaml
candidate_edge:
  edge_id: edge.metric_impl.xpressbees_settlement.cod_remitted_amount.uses_table.table.zs_observe.xpressbees_settlement
  edge_type: USES_TABLE
  source: metric_impl.xpressbees_settlement.cod_remitted_amount
  target: table.zs_observe.xpressbees_settlement
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
  edge_id: edge.metric_impl.xpressbees_settlement.cod_remitted_amount.uses_column.column.zs_observe.xpressbees_settlement.net_payment.8737448c
  edge_type: USES_COLUMN
  source: metric_impl.xpressbees_settlement.cod_remitted_amount
  target: column.zs_observe.xpressbees_settlement.net_payment
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
  edge_id: edge.metric_impl.xpressbees_settlement.cod_remitted_amount.uses_formula_template.formula_template.logistics.filtered_sum_amount
  edge_type: USES_FORMULA_TEMPLATE
  source: metric_impl.xpressbees_settlement.cod_remitted_amount
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
  edge_id: edge.metric.unique_awb_count.has_implementation.metric_impl.xpressbees_settlement.unique_awb_count
  edge_type: HAS_IMPLEMENTATION
  source: metric.unique_awb_count
  target: metric_impl.xpressbees_settlement.unique_awb_count
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
  edge_id: edge.metric_impl.xpressbees_settlement.unique_awb_count.implements_metric.metric.unique_awb_count
  edge_type: IMPLEMENTS_METRIC
  source: metric_impl.xpressbees_settlement.unique_awb_count
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
    materialized_from: edge.metric.unique_awb_count.has_implementation.metric_impl.xpressbees_settlement.unique_awb_count
```

```yaml
candidate_edge:
  edge_id: edge.metric_impl.xpressbees_settlement.unique_awb_count.uses_table.table.zs_observe.xpressbees_settlement
  edge_type: USES_TABLE
  source: metric_impl.xpressbees_settlement.unique_awb_count
  target: table.zs_observe.xpressbees_settlement
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
  edge_id: edge.metric_impl.xpressbees_settlement.unique_awb_count.uses_column.column.zs_observe.xpressbees_settlement.shipping_id.340e855f
  edge_type: USES_COLUMN
  source: metric_impl.xpressbees_settlement.unique_awb_count
  target: column.zs_observe.xpressbees_settlement.shipping_id
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
  edge_id: edge.metric_impl.xpressbees_settlement.unique_awb_count.uses_formula_template.formula_template.logistics.filtered_sum_amount
  edge_type: USES_FORMULA_TEMPLATE
  source: metric_impl.xpressbees_settlement.unique_awb_count
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
  edge_id: edge.metric.delivered_shipment_count.has_implementation.metric_impl.xpressbees_settlement.delivered_shipment_count
  edge_type: HAS_IMPLEMENTATION
  source: metric.delivered_shipment_count
  target: metric_impl.xpressbees_settlement.delivered_shipment_count
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
  edge_id: edge.metric_impl.xpressbees_settlement.delivered_shipment_count.implements_metric.metric.delivered_shipment_count
  edge_type: IMPLEMENTS_METRIC
  source: metric_impl.xpressbees_settlement.delivered_shipment_count
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
    materialized_from: edge.metric.delivered_shipment_count.has_implementation.metric_impl.xpressbees_settlement.delivered_shipment_count
```

```yaml
candidate_edge:
  edge_id: edge.metric_impl.xpressbees_settlement.delivered_shipment_count.uses_table.table.zs_observe.xpressbees_settlement
  edge_type: USES_TABLE
  source: metric_impl.xpressbees_settlement.delivered_shipment_count
  target: table.zs_observe.xpressbees_settlement
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
  edge_id: edge.metric_impl.xpressbees_settlement.delivered_shipment_count.uses_column.column.zs_observe.xpressbees_settlement.shipment_status.28a8df7f
  edge_type: USES_COLUMN
  source: metric_impl.xpressbees_settlement.delivered_shipment_count
  target: column.zs_observe.xpressbees_settlement.shipment_status
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
  edge_id: edge.metric_impl.xpressbees_settlement.delivered_shipment_count.uses_formula_template.formula_template.logistics.filtered_sum_amount
  edge_type: USES_FORMULA_TEMPLATE
  source: metric_impl.xpressbees_settlement.delivered_shipment_count
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
  edge_id: edge.metric.cod_collected_amount.has_implementation.metric_impl.xpressbees_settlement.cod_collected_amount
  edge_type: HAS_IMPLEMENTATION
  source: metric.cod_collected_amount
  target: metric_impl.xpressbees_settlement.cod_collected_amount
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
  edge_id: edge.metric_impl.xpressbees_settlement.cod_collected_amount.implements_metric.metric.cod_collected_amount
  edge_type: IMPLEMENTS_METRIC
  source: metric_impl.xpressbees_settlement.cod_collected_amount
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
    materialized_from: edge.metric.cod_collected_amount.has_implementation.metric_impl.xpressbees_settlement.cod_collected_amount
```

```yaml
candidate_edge:
  edge_id: edge.metric_impl.xpressbees_settlement.cod_collected_amount.uses_table.table.zs_observe.xpressbees_settlement
  edge_type: USES_TABLE
  source: metric_impl.xpressbees_settlement.cod_collected_amount
  target: table.zs_observe.xpressbees_settlement
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
  edge_id: edge.metric_impl.xpressbees_settlement.cod_collected_amount.uses_column.column.zs_observe.xpressbees_settlement.net_payment.8737448c
  edge_type: USES_COLUMN
  source: metric_impl.xpressbees_settlement.cod_collected_amount
  target: column.zs_observe.xpressbees_settlement.net_payment
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
  edge_id: edge.metric_impl.xpressbees_settlement.cod_collected_amount.uses_formula_template.formula_template.logistics.filtered_sum_amount
  edge_type: USES_FORMULA_TEMPLATE
  source: metric_impl.xpressbees_settlement.cod_collected_amount
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
  edge_id: edge.metric.cod_remitted_amount.has_implementation.metric_impl.shiprocket_settlement.xpressbees_air.cod_remitted_amount
  edge_type: HAS_IMPLEMENTATION
  source: metric.cod_remitted_amount
  target: metric_impl.shiprocket_settlement.xpressbees_air.cod_remitted_amount
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
  edge_id: edge.metric_impl.shiprocket_settlement.xpressbees_air.cod_remitted_amount.implements_metric.metric.cod_remitted_amount
  edge_type: IMPLEMENTS_METRIC
  source: metric_impl.shiprocket_settlement.xpressbees_air.cod_remitted_amount
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
    materialized_from: edge.metric.cod_remitted_amount.has_implementation.metric_impl.shiprocket_settlement.xpressbees_air.cod_remitted_amount
```

```yaml
candidate_edge:
  edge_id: edge.metric_impl.shiprocket_settlement.xpressbees_air.cod_remitted_amount.uses_table.table.zs_observe.shiprocket_settlement
  edge_type: USES_TABLE
  source: metric_impl.shiprocket_settlement.xpressbees_air.cod_remitted_amount
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
  edge_id: edge.metric_impl.shiprocket_settlement.xpressbees_air.cod_remitted_amount.uses_column.column.zs_observe.shiprocket_settlement.charged_amount.8737448c
  edge_type: USES_COLUMN
  source: metric_impl.shiprocket_settlement.xpressbees_air.cod_remitted_amount
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
  edge_id: edge.metric_impl.shiprocket_settlement.xpressbees_air.cod_remitted_amount.uses_column.column.zs_observe.shiprocket_settlement.courier_partner.28a8df7f
  edge_type: USES_COLUMN
  source: metric_impl.shiprocket_settlement.xpressbees_air.cod_remitted_amount
  target: column.zs_observe.shiprocket_settlement.courier_partner
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
  edge_id: edge.metric_impl.shiprocket_settlement.xpressbees_air.cod_remitted_amount.uses_formula_template.formula_template.logistics.filtered_sum_amount
  edge_type: USES_FORMULA_TEMPLATE
  source: metric_impl.shiprocket_settlement.xpressbees_air.cod_remitted_amount
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
  edge_id: edge.metric.freight_billed_amount.has_implementation.metric_impl.shiprocket_invoice.xpressbees_air.freight_billed_amount
  edge_type: HAS_IMPLEMENTATION
  source: metric.freight_billed_amount
  target: metric_impl.shiprocket_invoice.xpressbees_air.freight_billed_amount
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
  edge_id: edge.metric_impl.shiprocket_invoice.xpressbees_air.freight_billed_amount.implements_metric.metric.freight_billed_amount
  edge_type: IMPLEMENTS_METRIC
  source: metric_impl.shiprocket_invoice.xpressbees_air.freight_billed_amount
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
    materialized_from: edge.metric.freight_billed_amount.has_implementation.metric_impl.shiprocket_invoice.xpressbees_air.freight_billed_amount
```

```yaml
candidate_edge:
  edge_id: edge.metric_impl.shiprocket_invoice.xpressbees_air.freight_billed_amount.uses_table.table.zs_observe.shiprocket_invoice
  edge_type: USES_TABLE
  source: metric_impl.shiprocket_invoice.xpressbees_air.freight_billed_amount
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
  edge_id: edge.metric_impl.shiprocket_invoice.xpressbees_air.freight_billed_amount.uses_column.column.zs_observe.shiprocket_invoice.charged_amount.8737448c
  edge_type: USES_COLUMN
  source: metric_impl.shiprocket_invoice.xpressbees_air.freight_billed_amount
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
  edge_id: edge.metric_impl.shiprocket_invoice.xpressbees_air.freight_billed_amount.uses_column.column.zs_observe.shiprocket_invoice.courier_partner.28a8df7f
  edge_type: USES_COLUMN
  source: metric_impl.shiprocket_invoice.xpressbees_air.freight_billed_amount
  target: column.zs_observe.shiprocket_invoice.courier_partner
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
  edge_id: edge.metric_impl.shiprocket_invoice.xpressbees_air.freight_billed_amount.uses_formula_template.formula_template.logistics.filtered_sum_amount
  edge_type: USES_FORMULA_TEMPLATE
  source: metric_impl.shiprocket_invoice.xpressbees_air.freight_billed_amount
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
  id: review.xpressbees_logistics_parser_ready_v6_role_split.business_flow_boundary
  topic: Business Flow Binding boundary
  instruction: No Business Flow Binding, tenant, group, platform account, or account data binding cards should be emitted
    from this generic logistics document.
  severity: high
  status: open_for_ingestion_validation
```

## 7. Validation Summary

```yaml
validation_summary:
  document_id: xpressbees_logistics_parser_ready_v6_role_split
  candidate_cards: 34
  candidate_edges: 95
  card_types:
    metric: 7
    platform: 1
    platform_context: 1
    table: 1
    column: 13
    value_profile: 3
    metric_implementation: 8
  edge_types:
    BELONGS_TO_DOMAIN: 7
    BELONGS_TO_PLATFORM: 1
    HAS_PLATFORM_CONTEXT: 1
    SOURCED_FROM_PLATFORM: 1
    APPLIES_TO_PLATFORM: 1
    HAS_COLUMN: 13
    BELONGS_TO_TABLE: 13
    HAS_VALUE_PROFILE: 6
    PROFILES_COLUMN: 3
    PROFILES_TABLE: 3
    HAS_IMPLEMENTATION: 8
    IMPLEMENTS_METRIC: 8
    USES_TABLE: 8
    USES_COLUMN: 14
    USES_FORMULA_TEMPLATE: 8
  forbidden_card_types_present: []
  parser_boundary: generic logistics reusable knowledge only
```
