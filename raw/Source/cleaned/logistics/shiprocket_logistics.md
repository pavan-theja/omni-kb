# Shiprocket Logistics Partner Knowledge — Parser Ready v6 Role-Split Unified Edges
## 0. Document Metadata
```yaml
document_metadata:
  document_id: shiprocket_logistics_partner_parser_ready_v6_role_split
  title: Shiprocket Logistics Partner Knowledge — Parser Ready v6 Role-Split Unified Edges
  domain: logistics
  vendor: Shiprocket
  source_docx: /mnt/data/Logistics KB Doc.docx
  frame_of_reference: logistics_gold_std_canonical_card_frame_v5 plus flipkart_v8_unified_edges_style plus marketplace_cleanup_manifest_consolidated_v2
  generated_on: '2026-05-24'
  version: 6.0-role-split-manifest-aligned-unified-edges
  scope: shiprocket_logistics_partner_operational_handoff_with_unified_edges
  logistics_only: true
  shiprocket_role_split: logistics_partner
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
- Treat this file as the Shiprocket **logistics partner / operational handoff** role view.
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
  role_name: Shiprocket as Logistics Partner
  canonical_platform_id: platform.shiprocket
  role_summary: Operational Non-FBF logistics handoff, AWB assignment, courier routing, shipment status, delivery/RTO/return state, NDR/attempt evidence, and COD expected amount evidence through shiprocket_oms.
  owned_source_tables:
  - table.zs_observe.shiprocket_oms
  owned_process_variant_id: process_variant.shiprocket_logistics_partner.operational_handoff
  primary_business_processes:
  - business_process.order_to_shipment_flow
  - business_process.warehouse_to_courier_handoff
  - business_process.shipment_tracking_and_delivery
  - business_process.delivery_rto_return_resolution
  handoff_relationships:
  - relationship.shiprocket_oms.delhivery_invoice.awb
  - relationship.shiprocket_oms.delhivery_settlement.awb
  - relationship.shiprocket_oms.dtdc_settlement.awb
  - relationship.shiprocket_oms.ekart_settlement.shipment_id
  - relationship.shiprocket_oms.ekart_settlement.tracking_id
  - relationship.shiprocket_oms.xpressbees_settlement.shipping_id
  role_boundary_policy:
  - owns operational shipment evidence only
  - does not own primary freight invoice formulas
  - does not own primary COD remittance formulas when shiprocket_settlement exists
  - does not own tenant/group logistics routing
```

## Manifest Layer A — Evidence Anchor Manifests
```yaml
evidence_anchor_manifest:
  source_evidence_id: ev.shiprocket.logistics_partner.shiprocket_oms
  source_section: Logistics KB Doc.docx / High-Level Order Flow, FBF vs Non-FBF, Courier Partner Summary, Key Join Keys, Table Status Summary, Shiprocket OMS table sections
  evidence_type: prose | table_status | join_key_map | schema_reference
  supported_semantics:
  - Shiprocket participates as the Non-FBF logistics handoff partner and courier aggregator at the operational shipment layer
  - shiprocket_oms is operational shipment/order export evidence for order handoff, AWB assignment, courier routing, shipment status, delivery/RTO/return, and COD expected amount
  - shiprocket_oms.awb_code is the primary operational shipment key used to reach freight invoice and COD settlement evidence
  - underlying courier attribution appears in shiprocket_oms courier fields such as courier_company, master_courier, and fulfilment_channel
  unsupported_semantics:
  - Do not calculate primary freight billed from shiprocket_oms when shiprocket_invoice exists
  - Do not calculate authoritative COD remitted from shiprocket_oms when shiprocket_settlement exists
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
  role: logistics_partner
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
  - owns operational shipment evidence only
  - does not own primary freight invoice formulas
  - does not own primary COD remittance formulas when shiprocket_settlement exists
  - does not own tenant/group logistics routing
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
  review_id: review.shiprocket_oms.schema_coverage.key_fields_only
  source_manifest: schema_type_manifest
  severity: medium
  status: open
  applies_to:
  - table.zs_observe.shiprocket_oms
  finding: Source states shiprocket_oms has a large export schema, but the card set models only key fields listed in the Logistics KB Doc.
  deterministic_action: Treat unlisted physical columns as unmodeled; do not emit additional column cards without a full schema source.
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
  review_id: review.shiprocket.logistics_partner.role_split_boundary
  source_manifest: card_type_fit_manifest
  severity: medium
  status: open_for_ingestion_validation
  applies_to:
  - shiprocket_logistics_partner_parser_ready_v6_role_split
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
  card_id: table.zs_observe.shiprocket_oms
  name: Shiprocket OMS
  fields:
    name: Shiprocket OMS
    description: 'Shiprocket OMS: One row per Shiprocket shipment/order export record.'
    status: active
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
    table_name: shiprocket_oms
    full_reference: zs_observe.shiprocket_oms
    engine: Athena v3 / Trino SQL
    table_type: hybrid_order_shipment_tracking
    source_platform_ids:
    - platform.shiprocket
    source_platform_types:
    - logistics
    business_purpose: One row per Shiprocket shipment/order export record.
    grain: One row per Shiprocket shipment/order export record.
    grain_keys:
    - awb/order/reference as specified by columns
    date_columns:
    - see date column cards
    recommended_date_columns:
    - see metric implementations
    avoid_columns:
    - see amount semantics caveats
    structural_applicability: platform.shiprocket; account filters are not defined here
    coverage_status: active_partial
    row_count: '25914'
    period: Jan-Feb 2025
    group_ids: '22'
    schema_coverage: key_fields_only; known physical columns 244
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
  card_id: column.zs_observe.shiprocket_oms.order_id
  name: shiprocket_oms.order_id
  fields:
    name: shiprocket_oms.order_id
    description: Composite Shopify order id plus Shiprocket shipment suffix.
    status: active
    confidence: curated
    source_documents:
    - Logistics KB Doc.docx
    - Cognee KB Design v4.md
    - logistics_gold_std_raw_md_frame_v3.md
    - logistics_gold_std_canonical_card_frame_v5.md
    created_by: kb_authoring_assistant
    updated_by: kb_authoring_assistant
    version: 5.0-manifest-aligned
    table_id: table.zs_observe.shiprocket_oms
    column_name: order_id
    data_type: unknown
    semantic_roles: identifier;join_key
    business_concepts:
    - Composite Shopify order id plus Shiprocket shipment suffix.
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
  card_id: column.zs_observe.shiprocket_oms.channel
  name: shiprocket_oms.channel
  fields:
    name: shiprocket_oms.channel
    description: Always CUSTOM for D2C custom integration.
    status: active
    confidence: curated
    source_documents:
    - Logistics KB Doc.docx
    - Cognee KB Design v4.md
    - logistics_gold_std_raw_md_frame_v3.md
    - logistics_gold_std_canonical_card_frame_v5.md
    created_by: kb_authoring_assistant
    updated_by: kb_authoring_assistant
    version: 5.0-manifest-aligned
    table_id: table.zs_observe.shiprocket_oms
    column_name: channel
    data_type: unknown
    semantic_roles: dimension
    business_concepts:
    - Always CUSTOM for D2C custom integration.
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
  card_id: column.zs_observe.shiprocket_oms.channel_sku
  name: shiprocket_oms.channel_sku
  fields:
    name: shiprocket_oms.channel_sku
    description: Channel SKU/product identifier.
    status: active
    confidence: curated
    source_documents:
    - Logistics KB Doc.docx
    - Cognee KB Design v4.md
    - logistics_gold_std_raw_md_frame_v3.md
    - logistics_gold_std_canonical_card_frame_v5.md
    created_by: kb_authoring_assistant
    updated_by: kb_authoring_assistant
    version: 5.0-manifest-aligned
    table_id: table.zs_observe.shiprocket_oms
    column_name: channel_sku
    data_type: unknown
    semantic_roles: dimension
    business_concepts:
    - Channel SKU/product identifier.
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
  card_id: column.zs_observe.shiprocket_oms.master_sku
  name: shiprocket_oms.master_sku
  fields:
    name: shiprocket_oms.master_sku
    description: Master SKU/product identifier.
    status: active
    confidence: curated
    source_documents:
    - Logistics KB Doc.docx
    - Cognee KB Design v4.md
    - logistics_gold_std_raw_md_frame_v3.md
    - logistics_gold_std_canonical_card_frame_v5.md
    created_by: kb_authoring_assistant
    updated_by: kb_authoring_assistant
    version: 5.0-manifest-aligned
    table_id: table.zs_observe.shiprocket_oms
    column_name: master_sku
    data_type: unknown
    semantic_roles: dimension
    business_concepts:
    - Master SKU/product identifier.
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
  card_id: column.zs_observe.shiprocket_oms.product_name
  name: shiprocket_oms.product_name
  fields:
    name: shiprocket_oms.product_name
    description: Product name.
    status: active
    confidence: curated
    source_documents:
    - Logistics KB Doc.docx
    - Cognee KB Design v4.md
    - logistics_gold_std_raw_md_frame_v3.md
    - logistics_gold_std_canonical_card_frame_v5.md
    created_by: kb_authoring_assistant
    updated_by: kb_authoring_assistant
    version: 5.0-manifest-aligned
    table_id: table.zs_observe.shiprocket_oms
    column_name: product_name
    data_type: unknown
    semantic_roles: dimension
    business_concepts:
    - Product name.
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
  card_id: column.zs_observe.shiprocket_oms.product_category
  name: shiprocket_oms.product_category
  fields:
    name: shiprocket_oms.product_category
    description: Product category.
    status: active
    confidence: curated
    source_documents:
    - Logistics KB Doc.docx
    - Cognee KB Design v4.md
    - logistics_gold_std_raw_md_frame_v3.md
    - logistics_gold_std_canonical_card_frame_v5.md
    created_by: kb_authoring_assistant
    updated_by: kb_authoring_assistant
    version: 5.0-manifest-aligned
    table_id: table.zs_observe.shiprocket_oms
    column_name: product_category
    data_type: unknown
    semantic_roles: dimension
    business_concepts:
    - Product category.
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
  card_id: column.zs_observe.shiprocket_oms.fulfilment_channel
  name: shiprocket_oms.fulfilment_channel
  fields:
    name: shiprocket_oms.fulfilment_channel
    description: Courier company name, same meaning as courier_company.
    status: active
    confidence: curated
    source_documents:
    - Logistics KB Doc.docx
    - Cognee KB Design v4.md
    - logistics_gold_std_raw_md_frame_v3.md
    - logistics_gold_std_canonical_card_frame_v5.md
    created_by: kb_authoring_assistant
    updated_by: kb_authoring_assistant
    version: 5.0-manifest-aligned
    table_id: table.zs_observe.shiprocket_oms
    column_name: fulfilment_channel
    data_type: unknown
    semantic_roles: dimension;filter
    business_concepts:
    - Courier company name, same meaning as courier_company.
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
  card_id: column.zs_observe.shiprocket_oms.courier_company
  name: shiprocket_oms.courier_company
  fields:
    name: shiprocket_oms.courier_company
    description: Assigned courier such as Ekart, Delhivery, Xbees, Shadowfax.
    status: active
    confidence: curated
    source_documents:
    - Logistics KB Doc.docx
    - Cognee KB Design v4.md
    - logistics_gold_std_raw_md_frame_v3.md
    - logistics_gold_std_canonical_card_frame_v5.md
    created_by: kb_authoring_assistant
    updated_by: kb_authoring_assistant
    version: 5.0-manifest-aligned
    table_id: table.zs_observe.shiprocket_oms
    column_name: courier_company
    data_type: unknown
    semantic_roles: dimension;filter
    business_concepts:
    - Assigned courier such as Ekart, Delhivery, Xbees, Shadowfax.
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
  card_id: column.zs_observe.shiprocket_oms.awb_code
  name: shiprocket_oms.awb_code
  fields:
    name: shiprocket_oms.awb_code
    description: AWB/tracking number; primary shipment join key.
    status: active
    confidence: curated
    source_documents:
    - Logistics KB Doc.docx
    - Cognee KB Design v4.md
    - logistics_gold_std_raw_md_frame_v3.md
    - logistics_gold_std_canonical_card_frame_v5.md
    created_by: kb_authoring_assistant
    updated_by: kb_authoring_assistant
    version: 5.0-manifest-aligned
    table_id: table.zs_observe.shiprocket_oms
    column_name: awb_code
    data_type: unknown
    semantic_roles: identifier;join_key;reconciliation_key
    business_concepts:
    - AWB/tracking number
    - primary shipment join key.
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
  card_id: column.zs_observe.shiprocket_oms.master_courier
  name: shiprocket_oms.master_courier
  fields:
    name: shiprocket_oms.master_courier
    description: Aggregated courier name.
    status: active
    confidence: curated
    source_documents:
    - Logistics KB Doc.docx
    - Cognee KB Design v4.md
    - logistics_gold_std_raw_md_frame_v3.md
    - logistics_gold_std_canonical_card_frame_v5.md
    created_by: kb_authoring_assistant
    updated_by: kb_authoring_assistant
    version: 5.0-manifest-aligned
    table_id: table.zs_observe.shiprocket_oms
    column_name: master_courier
    data_type: unknown
    semantic_roles: dimension
    business_concepts:
    - Aggregated courier name.
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
  card_id: column.zs_observe.shiprocket_oms.transaction_type
  name: shiprocket_oms.transaction_type
  fields:
    name: shiprocket_oms.transaction_type
    description: forward, return, cancelled, pending, in transit, damaged/lost.
    status: active
    confidence: curated
    source_documents:
    - Logistics KB Doc.docx
    - Cognee KB Design v4.md
    - logistics_gold_std_raw_md_frame_v3.md
    - logistics_gold_std_canonical_card_frame_v5.md
    created_by: kb_authoring_assistant
    updated_by: kb_authoring_assistant
    version: 5.0-manifest-aligned
    table_id: table.zs_observe.shiprocket_oms
    column_name: transaction_type
    data_type: unknown
    semantic_roles: status;filter
    business_concepts:
    - forward, return, cancelled, pending, in transit, damaged/lost.
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
  card_id: column.zs_observe.shiprocket_oms.status
  name: shiprocket_oms.status
  fields:
    name: shiprocket_oms.status
    description: Delivery/RTO/return status.
    status: active
    confidence: curated
    source_documents:
    - Logistics KB Doc.docx
    - Cognee KB Design v4.md
    - logistics_gold_std_raw_md_frame_v3.md
    - logistics_gold_std_canonical_card_frame_v5.md
    created_by: kb_authoring_assistant
    updated_by: kb_authoring_assistant
    version: 5.0-manifest-aligned
    table_id: table.zs_observe.shiprocket_oms
    column_name: status
    data_type: unknown
    semantic_roles: status;filter
    business_concepts:
    - Delivery/RTO/return status.
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
  card_id: column.zs_observe.shiprocket_oms.charged_amount
  name: shiprocket_oms.charged_amount
  fields:
    name: shiprocket_oms.charged_amount
    description: Declared product/order value to Shiprocket, not freight.
    status: active
    confidence: curated
    source_documents:
    - Logistics KB Doc.docx
    - Cognee KB Design v4.md
    - logistics_gold_std_raw_md_frame_v3.md
    - logistics_gold_std_canonical_card_frame_v5.md
    created_by: kb_authoring_assistant
    updated_by: kb_authoring_assistant
    version: 5.0-manifest-aligned
    table_id: table.zs_observe.shiprocket_oms
    column_name: charged_amount
    data_type: unknown
    semantic_roles: measure
    business_concepts:
    - Declared product/order value to Shiprocket, not freight.
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
  card_id: column.zs_observe.shiprocket_oms.order_total
  name: shiprocket_oms.order_total
  fields:
    name: shiprocket_oms.order_total
    description: Order total from channel/order context.
    status: active
    confidence: curated
    source_documents:
    - Logistics KB Doc.docx
    - Cognee KB Design v4.md
    - logistics_gold_std_raw_md_frame_v3.md
    - logistics_gold_std_canonical_card_frame_v5.md
    created_by: kb_authoring_assistant
    updated_by: kb_authoring_assistant
    version: 5.0-manifest-aligned
    table_id: table.zs_observe.shiprocket_oms
    column_name: order_total
    data_type: unknown
    semantic_roles: measure
    business_concepts:
    - Order total from channel/order context.
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
  card_id: column.zs_observe.shiprocket_oms.cod_payble_amount
  name: shiprocket_oms.cod_payble_amount
  fields:
    name: shiprocket_oms.cod_payble_amount
    description: COD amount expected from customer.
    status: active
    confidence: curated
    source_documents:
    - Logistics KB Doc.docx
    - Cognee KB Design v4.md
    - logistics_gold_std_raw_md_frame_v3.md
    - logistics_gold_std_canonical_card_frame_v5.md
    created_by: kb_authoring_assistant
    updated_by: kb_authoring_assistant
    version: 5.0-manifest-aligned
    table_id: table.zs_observe.shiprocket_oms
    column_name: cod_payble_amount
    data_type: unknown
    semantic_roles: measure
    business_concepts:
    - COD amount expected from customer.
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
  card_id: column.zs_observe.shiprocket_oms.payment_method
  name: shiprocket_oms.payment_method
  fields:
    name: shiprocket_oms.payment_method
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
    table_id: table.zs_observe.shiprocket_oms
    column_name: payment_method
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
  card_id: column.zs_observe.shiprocket_oms.remitted_amount
  name: shiprocket_oms.remitted_amount
  fields:
    name: shiprocket_oms.remitted_amount
    description: COD amount remitted by courier/Shiprocket where populated.
    status: active
    confidence: curated
    source_documents:
    - Logistics KB Doc.docx
    - Cognee KB Design v4.md
    - logistics_gold_std_raw_md_frame_v3.md
    - logistics_gold_std_canonical_card_frame_v5.md
    created_by: kb_authoring_assistant
    updated_by: kb_authoring_assistant
    version: 5.0-manifest-aligned
    table_id: table.zs_observe.shiprocket_oms
    column_name: remitted_amount
    data_type: unknown
    semantic_roles: measure
    business_concepts:
    - COD amount remitted by courier/Shiprocket where populated.
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
  card_id: column.zs_observe.shiprocket_oms.cod_remittance_date
  name: shiprocket_oms.cod_remittance_date
  fields:
    name: shiprocket_oms.cod_remittance_date
    description: Date COD was remitted.
    status: active
    confidence: curated
    source_documents:
    - Logistics KB Doc.docx
    - Cognee KB Design v4.md
    - logistics_gold_std_raw_md_frame_v3.md
    - logistics_gold_std_canonical_card_frame_v5.md
    created_by: kb_authoring_assistant
    updated_by: kb_authoring_assistant
    version: 5.0-manifest-aligned
    table_id: table.zs_observe.shiprocket_oms
    column_name: cod_remittance_date
    data_type: unknown
    semantic_roles: date
    business_concepts:
    - Date COD was remitted.
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
  card_id: column.zs_observe.shiprocket_oms.freight_total_amount
  name: shiprocket_oms.freight_total_amount
  fields:
    name: shiprocket_oms.freight_total_amount
    description: Freight charged for shipment where populated.
    status: active
    confidence: curated
    source_documents:
    - Logistics KB Doc.docx
    - Cognee KB Design v4.md
    - logistics_gold_std_raw_md_frame_v3.md
    - logistics_gold_std_canonical_card_frame_v5.md
    created_by: kb_authoring_assistant
    updated_by: kb_authoring_assistant
    version: 5.0-manifest-aligned
    table_id: table.zs_observe.shiprocket_oms
    column_name: freight_total_amount
    data_type: unknown
    semantic_roles: measure
    business_concepts:
    - Freight charged for shipment where populated.
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
  card_id: column.zs_observe.shiprocket_oms.shipping_charges
  name: shiprocket_oms.shipping_charges
  fields:
    name: shiprocket_oms.shipping_charges
    description: Shipping charge breakdown or amount.
    status: active
    confidence: curated
    source_documents:
    - Logistics KB Doc.docx
    - Cognee KB Design v4.md
    - logistics_gold_std_raw_md_frame_v3.md
    - logistics_gold_std_canonical_card_frame_v5.md
    created_by: kb_authoring_assistant
    updated_by: kb_authoring_assistant
    version: 5.0-manifest-aligned
    table_id: table.zs_observe.shiprocket_oms
    column_name: shipping_charges
    data_type: unknown
    semantic_roles: measure
    business_concepts:
    - Shipping charge breakdown or amount.
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
  card_id: column.zs_observe.shiprocket_oms.created_date
  name: shiprocket_oms.created_date
  fields:
    name: shiprocket_oms.created_date
    description: Shipment creation date.
    status: active
    confidence: curated
    source_documents:
    - Logistics KB Doc.docx
    - Cognee KB Design v4.md
    - logistics_gold_std_raw_md_frame_v3.md
    - logistics_gold_std_canonical_card_frame_v5.md
    created_by: kb_authoring_assistant
    updated_by: kb_authoring_assistant
    version: 5.0-manifest-aligned
    table_id: table.zs_observe.shiprocket_oms
    column_name: created_date
    data_type: unknown
    semantic_roles: date
    business_concepts:
    - Shipment creation date.
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
  card_id: column.zs_observe.shiprocket_oms.awb_assigned_date
  name: shiprocket_oms.awb_assigned_date
  fields:
    name: shiprocket_oms.awb_assigned_date
    description: Date AWB assigned.
    status: active
    confidence: curated
    source_documents:
    - Logistics KB Doc.docx
    - Cognee KB Design v4.md
    - logistics_gold_std_raw_md_frame_v3.md
    - logistics_gold_std_canonical_card_frame_v5.md
    created_by: kb_authoring_assistant
    updated_by: kb_authoring_assistant
    version: 5.0-manifest-aligned
    table_id: table.zs_observe.shiprocket_oms
    column_name: awb_assigned_date
    data_type: unknown
    semantic_roles: date
    business_concepts:
    - Date AWB assigned.
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
  card_id: column.zs_observe.shiprocket_oms.pickup_scheduled_date
  name: shiprocket_oms.pickup_scheduled_date
  fields:
    name: shiprocket_oms.pickup_scheduled_date
    description: Scheduled pickup date.
    status: active
    confidence: curated
    source_documents:
    - Logistics KB Doc.docx
    - Cognee KB Design v4.md
    - logistics_gold_std_raw_md_frame_v3.md
    - logistics_gold_std_canonical_card_frame_v5.md
    created_by: kb_authoring_assistant
    updated_by: kb_authoring_assistant
    version: 5.0-manifest-aligned
    table_id: table.zs_observe.shiprocket_oms
    column_name: pickup_scheduled_date
    data_type: unknown
    semantic_roles: date
    business_concepts:
    - Scheduled pickup date.
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
  card_id: column.zs_observe.shiprocket_oms.order_picked_up_date
  name: shiprocket_oms.order_picked_up_date
  fields:
    name: shiprocket_oms.order_picked_up_date
    description: Actual pickup date.
    status: active
    confidence: curated
    source_documents:
    - Logistics KB Doc.docx
    - Cognee KB Design v4.md
    - logistics_gold_std_raw_md_frame_v3.md
    - logistics_gold_std_canonical_card_frame_v5.md
    created_by: kb_authoring_assistant
    updated_by: kb_authoring_assistant
    version: 5.0-manifest-aligned
    table_id: table.zs_observe.shiprocket_oms
    column_name: order_picked_up_date
    data_type: unknown
    semantic_roles: date
    business_concepts:
    - Actual pickup date.
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
  card_id: column.zs_observe.shiprocket_oms.edd
  name: shiprocket_oms.edd
  fields:
    name: shiprocket_oms.edd
    description: Expected delivery date.
    status: active
    confidence: curated
    source_documents:
    - Logistics KB Doc.docx
    - Cognee KB Design v4.md
    - logistics_gold_std_raw_md_frame_v3.md
    - logistics_gold_std_canonical_card_frame_v5.md
    created_by: kb_authoring_assistant
    updated_by: kb_authoring_assistant
    version: 5.0-manifest-aligned
    table_id: table.zs_observe.shiprocket_oms
    column_name: edd
    data_type: unknown
    semantic_roles: date
    business_concepts:
    - Expected delivery date.
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
  card_id: column.zs_observe.shiprocket_oms.order_delivered_date
  name: shiprocket_oms.order_delivered_date
  fields:
    name: shiprocket_oms.order_delivered_date
    description: Actual customer delivery date.
    status: active
    confidence: curated
    source_documents:
    - Logistics KB Doc.docx
    - Cognee KB Design v4.md
    - logistics_gold_std_raw_md_frame_v3.md
    - logistics_gold_std_canonical_card_frame_v5.md
    created_by: kb_authoring_assistant
    updated_by: kb_authoring_assistant
    version: 5.0-manifest-aligned
    table_id: table.zs_observe.shiprocket_oms
    column_name: order_delivered_date
    data_type: unknown
    semantic_roles: date
    business_concepts:
    - Actual customer delivery date.
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
  card_id: column.zs_observe.shiprocket_oms.rto_initiated_date
  name: shiprocket_oms.rto_initiated_date
  fields:
    name: shiprocket_oms.rto_initiated_date
    description: RTO initiation date.
    status: active
    confidence: curated
    source_documents:
    - Logistics KB Doc.docx
    - Cognee KB Design v4.md
    - logistics_gold_std_raw_md_frame_v3.md
    - logistics_gold_std_canonical_card_frame_v5.md
    created_by: kb_authoring_assistant
    updated_by: kb_authoring_assistant
    version: 5.0-manifest-aligned
    table_id: table.zs_observe.shiprocket_oms
    column_name: rto_initiated_date
    data_type: unknown
    semantic_roles: date
    business_concepts:
    - RTO initiation date.
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
  card_id: column.zs_observe.shiprocket_oms.rto_delivered_date
  name: shiprocket_oms.rto_delivered_date
  fields:
    name: shiprocket_oms.rto_delivered_date
    description: RTO delivery back to origin date.
    status: active
    confidence: curated
    source_documents:
    - Logistics KB Doc.docx
    - Cognee KB Design v4.md
    - logistics_gold_std_raw_md_frame_v3.md
    - logistics_gold_std_canonical_card_frame_v5.md
    created_by: kb_authoring_assistant
    updated_by: kb_authoring_assistant
    version: 5.0-manifest-aligned
    table_id: table.zs_observe.shiprocket_oms
    column_name: rto_delivered_date
    data_type: unknown
    semantic_roles: date
    business_concepts:
    - RTO delivery back to origin date.
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
  card_id: column.zs_observe.shiprocket_oms.ndr_1_attempt_date
  name: shiprocket_oms.ndr_1_attempt_date
  fields:
    name: shiprocket_oms.ndr_1_attempt_date
    description: First non-delivery attempt date.
    status: active
    confidence: curated
    source_documents:
    - Logistics KB Doc.docx
    - Cognee KB Design v4.md
    - logistics_gold_std_raw_md_frame_v3.md
    - logistics_gold_std_canonical_card_frame_v5.md
    created_by: kb_authoring_assistant
    updated_by: kb_authoring_assistant
    version: 5.0-manifest-aligned
    table_id: table.zs_observe.shiprocket_oms
    column_name: ndr_1_attempt_date
    data_type: unknown
    semantic_roles: date
    business_concepts:
    - First non-delivery attempt date.
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
  card_id: column.zs_observe.shiprocket_oms.ndr_1_remark
  name: shiprocket_oms.ndr_1_remark
  fields:
    name: shiprocket_oms.ndr_1_remark
    description: First NDR remark.
    status: active
    confidence: curated
    source_documents:
    - Logistics KB Doc.docx
    - Cognee KB Design v4.md
    - logistics_gold_std_raw_md_frame_v3.md
    - logistics_gold_std_canonical_card_frame_v5.md
    created_by: kb_authoring_assistant
    updated_by: kb_authoring_assistant
    version: 5.0-manifest-aligned
    table_id: table.zs_observe.shiprocket_oms
    column_name: ndr_1_remark
    data_type: unknown
    semantic_roles: status;dimension
    business_concepts:
    - First NDR remark.
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
  card_id: column.zs_observe.shiprocket_oms.ndr_2_remark
  name: shiprocket_oms.ndr_2_remark
  fields:
    name: shiprocket_oms.ndr_2_remark
    description: Second NDR remark.
    status: active
    confidence: curated
    source_documents:
    - Logistics KB Doc.docx
    - Cognee KB Design v4.md
    - logistics_gold_std_raw_md_frame_v3.md
    - logistics_gold_std_canonical_card_frame_v5.md
    created_by: kb_authoring_assistant
    updated_by: kb_authoring_assistant
    version: 5.0-manifest-aligned
    table_id: table.zs_observe.shiprocket_oms
    column_name: ndr_2_remark
    data_type: unknown
    semantic_roles: status;dimension
    business_concepts:
    - Second NDR remark.
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
  card_id: column.zs_observe.shiprocket_oms.latest_ndr_date
  name: shiprocket_oms.latest_ndr_date
  fields:
    name: shiprocket_oms.latest_ndr_date
    description: Latest NDR date.
    status: active
    confidence: curated
    source_documents:
    - Logistics KB Doc.docx
    - Cognee KB Design v4.md
    - logistics_gold_std_raw_md_frame_v3.md
    - logistics_gold_std_canonical_card_frame_v5.md
    created_by: kb_authoring_assistant
    updated_by: kb_authoring_assistant
    version: 5.0-manifest-aligned
    table_id: table.zs_observe.shiprocket_oms
    column_name: latest_ndr_date
    data_type: unknown
    semantic_roles: date
    business_concepts:
    - Latest NDR date.
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
  card_id: column.zs_observe.shiprocket_oms.latest_ndr_reason
  name: shiprocket_oms.latest_ndr_reason
  fields:
    name: shiprocket_oms.latest_ndr_reason
    description: Latest NDR reason.
    status: active
    confidence: curated
    source_documents:
    - Logistics KB Doc.docx
    - Cognee KB Design v4.md
    - logistics_gold_std_raw_md_frame_v3.md
    - logistics_gold_std_canonical_card_frame_v5.md
    created_by: kb_authoring_assistant
    updated_by: kb_authoring_assistant
    version: 5.0-manifest-aligned
    table_id: table.zs_observe.shiprocket_oms
    column_name: latest_ndr_reason
    data_type: unknown
    semantic_roles: status;dimension
    business_concepts:
    - Latest NDR reason.
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
  card_id: column.zs_observe.shiprocket_oms.attempt_count
  name: shiprocket_oms.attempt_count
  fields:
    name: shiprocket_oms.attempt_count
    description: Total delivery attempts.
    status: active
    confidence: curated
    source_documents:
    - Logistics KB Doc.docx
    - Cognee KB Design v4.md
    - logistics_gold_std_raw_md_frame_v3.md
    - logistics_gold_std_canonical_card_frame_v5.md
    created_by: kb_authoring_assistant
    updated_by: kb_authoring_assistant
    version: 5.0-manifest-aligned
    table_id: table.zs_observe.shiprocket_oms
    column_name: attempt_count
    data_type: unknown
    semantic_roles: measure
    business_concepts:
    - Total delivery attempts.
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
  card_id: column.zs_observe.shiprocket_oms.rto_reason
  name: shiprocket_oms.rto_reason
  fields:
    name: shiprocket_oms.rto_reason
    description: RTO reason.
    status: active
    confidence: curated
    source_documents:
    - Logistics KB Doc.docx
    - Cognee KB Design v4.md
    - logistics_gold_std_raw_md_frame_v3.md
    - logistics_gold_std_canonical_card_frame_v5.md
    created_by: kb_authoring_assistant
    updated_by: kb_authoring_assistant
    version: 5.0-manifest-aligned
    table_id: table.zs_observe.shiprocket_oms
    column_name: rto_reason
    data_type: unknown
    semantic_roles: status;dimension
    business_concepts:
    - RTO reason.
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
  card_id: column.zs_observe.shiprocket_oms.rto_reason_1
  name: shiprocket_oms.rto_reason_1
  fields:
    name: shiprocket_oms.rto_reason_1
    description: Alternate RTO reason.
    status: active
    confidence: curated
    source_documents:
    - Logistics KB Doc.docx
    - Cognee KB Design v4.md
    - logistics_gold_std_raw_md_frame_v3.md
    - logistics_gold_std_canonical_card_frame_v5.md
    created_by: kb_authoring_assistant
    updated_by: kb_authoring_assistant
    version: 5.0-manifest-aligned
    table_id: table.zs_observe.shiprocket_oms
    column_name: rto_reason_1
    data_type: unknown
    semantic_roles: status;dimension
    business_concepts:
    - Alternate RTO reason.
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
  card_id: column.zs_observe.shiprocket_oms.utr_no
  name: shiprocket_oms.utr_no
  fields:
    name: shiprocket_oms.utr_no
    description: Bank UTR for COD settlement where present.
    status: active
    confidence: curated
    source_documents:
    - Logistics KB Doc.docx
    - Cognee KB Design v4.md
    - logistics_gold_std_raw_md_frame_v3.md
    - logistics_gold_std_canonical_card_frame_v5.md
    created_by: kb_authoring_assistant
    updated_by: kb_authoring_assistant
    version: 5.0-manifest-aligned
    table_id: table.zs_observe.shiprocket_oms
    column_name: utr_no
    data_type: unknown
    semantic_roles: identifier;bank_bridge
    business_concepts:
    - Bank UTR for COD settlement where present.
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
  card_id: column.zs_observe.shiprocket_oms.crf_id
  name: shiprocket_oms.crf_id
  fields:
    name: shiprocket_oms.crf_id
    description: COD remittance file ID.
    status: active
    confidence: curated
    source_documents:
    - Logistics KB Doc.docx
    - Cognee KB Design v4.md
    - logistics_gold_std_raw_md_frame_v3.md
    - logistics_gold_std_canonical_card_frame_v5.md
    created_by: kb_authoring_assistant
    updated_by: kb_authoring_assistant
    version: 5.0-manifest-aligned
    table_id: table.zs_observe.shiprocket_oms
    column_name: crf_id
    data_type: unknown
    semantic_roles: identifier
    business_concepts:
    - COD remittance file ID.
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
  card_id: column.zs_observe.shiprocket_oms.customer_invoice_id
  name: shiprocket_oms.customer_invoice_id
  fields:
    name: shiprocket_oms.customer_invoice_id
    description: Courier invoice reference.
    status: active
    confidence: curated
    source_documents:
    - Logistics KB Doc.docx
    - Cognee KB Design v4.md
    - logistics_gold_std_raw_md_frame_v3.md
    - logistics_gold_std_canonical_card_frame_v5.md
    created_by: kb_authoring_assistant
    updated_by: kb_authoring_assistant
    version: 5.0-manifest-aligned
    table_id: table.zs_observe.shiprocket_oms
    column_name: customer_invoice_id
    data_type: unknown
    semantic_roles: identifier
    business_concepts:
    - Courier invoice reference.
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
  card_id: column.zs_observe.shiprocket_oms.is_active
  name: shiprocket_oms.is_active
  fields:
    name: shiprocket_oms.is_active
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
    table_id: table.zs_observe.shiprocket_oms
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
  card_id: column.zs_observe.shiprocket_oms.group_level_id
  name: shiprocket_oms.group_level_id
  fields:
    name: shiprocket_oms.group_level_id
    description: Observed account/group scope candidate, not universal rule.
    status: active
    confidence: curated
    source_documents:
    - Logistics KB Doc.docx
    - Cognee KB Design v4.md
    - logistics_gold_std_raw_md_frame_v3.md
    - logistics_gold_std_canonical_card_frame_v5.md
    created_by: kb_authoring_assistant
    updated_by: kb_authoring_assistant
    version: 5.0-manifest-aligned
    table_id: table.zs_observe.shiprocket_oms
    column_name: group_level_id
    data_type: unknown
    semantic_roles: scope_filter
    business_concepts:
    - Observed account/group scope candidate, not universal rule.
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
  card_id: relationship.shiprocket_oms.delhivery_invoice.awb
  name: shiprocket_oms to delhivery_invoice by awb
  fields:
    name: shiprocket_oms to delhivery_invoice by awb
    description: Join Shiprocket-routed Delhivery shipments to Delhivery invoice.
    status: active
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
    target_table: table.zs_observe.delhivery_invoice
    relationship_type: join; reconciliation_relation
    join_keys: awb_code = forward_awb_number
    cardinality: one_to_zero_or_many
    join_type_recommendation: left_join for diagnostics; inner_join for matched-only analysis
    business_use: Join Shiprocket-routed Delhivery shipments to Delhivery invoice.
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
  card_id: relationship.shiprocket_oms.delhivery_settlement.awb
  name: shiprocket_oms to delhivery_settlement by awb
  fields:
    name: shiprocket_oms to delhivery_settlement by awb
    description: Join Shiprocket-routed Delhivery shipments to Delhivery COD settlement.
    status: active
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
    target_table: table.zs_observe.delhivery_settlement
    relationship_type: join; reconciliation_relation
    join_keys: awb_code = waybill_num
    cardinality: one_to_zero_or_many
    join_type_recommendation: left_join for diagnostics; inner_join for matched-only analysis
    business_use: Join Shiprocket-routed Delhivery shipments to Delhivery COD settlement.
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
  card_id: relationship.shiprocket_oms.dtdc_settlement.awb
  name: shiprocket_oms to dtdc_settlement by awb
  fields:
    name: shiprocket_oms to dtdc_settlement by awb
    description: Join Shiprocket-routed DTDC shipments to DTDC settlement.
    status: active
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
    target_table: table.zs_observe.dtdc_settlement
    relationship_type: join; reconciliation_relation
    join_keys: awb_code = airwaybill_number
    cardinality: one_to_zero_or_many
    join_type_recommendation: left_join for diagnostics; inner_join for matched-only analysis
    business_use: Join Shiprocket-routed DTDC shipments to DTDC settlement.
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
  card_id: relationship.shiprocket_oms.ekart_settlement.shipment_id
  name: shiprocket_oms to ekart_settlement by shipment_id
  fields:
    name: shiprocket_oms to ekart_settlement by shipment_id
    description: Join Shiprocket OMS to Ekart settlement by shipment_id for Ekart/FBF evidence.
    status: active
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
    target_table: table.zs_observe.ekart_settlement
    relationship_type: join; reconciliation_relation
    join_keys: awb_code = shipment_id
    cardinality: one_to_zero_or_many
    join_type_recommendation: left_join for diagnostics; inner_join for matched-only analysis
    business_use: Join Shiprocket OMS to Ekart settlement by shipment_id for Ekart/FBF evidence.
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
  card_id: relationship.shiprocket_oms.ekart_settlement.tracking_id
  name: shiprocket_oms to ekart_settlement by tracking_id
  fields:
    name: shiprocket_oms to ekart_settlement by tracking_id
    description: Fallback join from Shiprocket OMS AWB to Ekart tracking_id.
    status: active
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
    target_table: table.zs_observe.ekart_settlement
    relationship_type: join; reconciliation_relation
    join_keys: awb_code = tracking_id
    cardinality: one_to_zero_or_many
    join_type_recommendation: left_join for diagnostics; inner_join for matched-only analysis
    business_use: Fallback join from Shiprocket OMS AWB to Ekart tracking_id.
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
  card_id: relationship.shiprocket_oms.xpressbees_settlement.shipping_id
  name: shiprocket_oms to xpressbees_settlement by shipping_id
  fields:
    name: shiprocket_oms to xpressbees_settlement by shipping_id
    description: Join Shiprocket OMS to sparse XpressBees native settlement where shipping_id is populated.
    status: active
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
    target_table: table.zs_observe.xpressbees_settlement
    relationship_type: join; reconciliation_relation
    join_keys: awb_code = shipping_id
    cardinality: one_to_zero_or_many
    join_type_recommendation: left_join for diagnostics; inner_join for matched-only analysis
    business_use: Join Shiprocket OMS to sparse XpressBees native settlement where shipping_id is populated.
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
  card_id: value_profile.shiprocket_oms.transaction_type
  name: shiprocket_oms.transaction_type Value Profile
  fields:
    name: shiprocket_oms.transaction_type Value Profile
    description: Known values and meanings for shiprocket_oms.transaction_type.
    status: active
    confidence: curated
    source_documents:
    - Logistics KB Doc.docx
    - Cognee KB Design v4.md
    - logistics_gold_std_raw_md_frame_v3.md
    - logistics_gold_std_canonical_card_frame_v5.md
    created_by: kb_authoring_assistant
    updated_by: kb_authoring_assistant
    version: 5.0-manifest-aligned
    table_id: table.zs_observe.shiprocket_oms
    column_id: column.zs_observe.shiprocket_oms.transaction_type
    value_type: enum_or_enum_with_nulls
    values: forward=Outbound shipment (forward); return=Customer/reverse return (return); cancelled=Cancelled before dispatch (cancel); in transit=Shipment in transit (active); damaged/lost=Damaged or lost shipment (exception)
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
  card_id: value_profile.shiprocket_oms.status
  name: shiprocket_oms.status Value Profile
  fields:
    name: shiprocket_oms.status Value Profile
    description: Known values and meanings for shiprocket_oms.status.
    status: active
    confidence: curated
    source_documents:
    - Logistics KB Doc.docx
    - Cognee KB Design v4.md
    - logistics_gold_std_raw_md_frame_v3.md
    - logistics_gold_std_canonical_card_frame_v5.md
    created_by: kb_authoring_assistant
    updated_by: kb_authoring_assistant
    version: 5.0-manifest-aligned
    table_id: table.zs_observe.shiprocket_oms
    column_id: column.zs_observe.shiprocket_oms.status
    value_type: enum_or_enum_with_nulls
    values: DELIVERED=Delivered to customer (delivered); RTO DELIVERED=Returned to origin (rto); RETURN DELIVERED=Customer return delivered (return); CANCELLED=Cancelled (cancel); DAMAGED/LOST=Damaged or lost (exception)
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
  card_id: value_profile.shiprocket_oms.payment_method
  name: shiprocket_oms.payment_method Value Profile
  fields:
    name: shiprocket_oms.payment_method Value Profile
    description: Known values and meanings for shiprocket_oms.payment_method.
    status: active
    confidence: curated
    source_documents:
    - Logistics KB Doc.docx
    - Cognee KB Design v4.md
    - logistics_gold_std_raw_md_frame_v3.md
    - logistics_gold_std_canonical_card_frame_v5.md
    created_by: kb_authoring_assistant
    updated_by: kb_authoring_assistant
    version: 5.0-manifest-aligned
    table_id: table.zs_observe.shiprocket_oms
    column_id: column.zs_observe.shiprocket_oms.payment_method
    value_type: enum_or_enum_with_nulls
    values: prepaid=Online/prepaid order (prepaid); cod=Cash on delivery order (cod)
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
  card_id: value_profile.shiprocket_oms.courier_company
  name: shiprocket_oms.courier_company Value Profile
  fields:
    name: shiprocket_oms.courier_company Value Profile
    description: Known values and meanings for shiprocket_oms.courier_company.
    status: active
    confidence: curated
    source_documents:
    - Logistics KB Doc.docx
    - Cognee KB Design v4.md
    - logistics_gold_std_raw_md_frame_v3.md
    - logistics_gold_std_canonical_card_frame_v5.md
    created_by: kb_authoring_assistant
    updated_by: kb_authoring_assistant
    version: 5.0-manifest-aligned
    table_id: table.zs_observe.shiprocket_oms
    column_id: column.zs_observe.shiprocket_oms.courier_company
    value_type: enum_or_enum_with_nulls
    values: Ekart_Direct SFC=Ekart direct/FBF-like logistics (ekart); Delhivery_SFC _Direct=Delhivery direct (delhivery); Dlv_Direct_SFC=Delhivery direct alternate (delhivery); Xbees_Direct_AIR=XpressBees air (xpressbees); Shadowfax Direct Rev QC=Shadowfax reverse QC only (shadowfax)
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
  card_id: metric.average_delivery_attempts
  name: Average Delivery Attempts
  fields:
    name: Average Delivery Attempts
    description: Average delivery attempts per shipment.
    status: active
    confidence: curated
    source_documents:
    - Logistics KB Doc.docx
    - Cognee KB Design v4.md
    - logistics_gold_std_raw_md_frame_v3.md
    - logistics_gold_std_canonical_card_frame_v5.md
    created_by: kb_authoring_assistant
    updated_by: kb_authoring_assistant
    version: 5.0-manifest-aligned
    metric_name: Average Delivery Attempts
    aliases:
    - avg attempts
    metric_type: amount/count/rate/days_by_metric
    unit: currency/count/percentage/days_by_metric
    default_aggregation: SUM or COUNT or ratio by metric
    default_grain: shipment_awb_or_settlement_batch
    polarity: context_dependent
    business_concepts:
    - logistics
    - average_delivery_attempts
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
  card_id: metric.cancelled_shipment_count
  name: Cancelled Shipment Count
  fields:
    name: Cancelled Shipment Count
    description: Count of shipments cancelled before completion.
    status: active
    confidence: curated
    source_documents:
    - Logistics KB Doc.docx
    - Cognee KB Design v4.md
    - logistics_gold_std_raw_md_frame_v3.md
    - logistics_gold_std_canonical_card_frame_v5.md
    created_by: kb_authoring_assistant
    updated_by: kb_authoring_assistant
    version: 5.0-manifest-aligned
    metric_name: Cancelled Shipment Count
    aliases:
    - cancelled shipments
    metric_type: amount/count/rate/days_by_metric
    unit: currency/count/percentage/days_by_metric
    default_aggregation: SUM or COUNT or ratio by metric
    default_grain: shipment_awb_or_settlement_batch
    polarity: context_dependent
    business_concepts:
    - logistics
    - cancelled_shipment_count
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
  card_id: metric.damaged_lost_shipment_count
  name: Damaged or Lost Shipment Count
  fields:
    name: Damaged or Lost Shipment Count
    description: Count of shipments marked damaged or lost.
    status: active
    confidence: curated
    source_documents:
    - Logistics KB Doc.docx
    - Cognee KB Design v4.md
    - logistics_gold_std_raw_md_frame_v3.md
    - logistics_gold_std_canonical_card_frame_v5.md
    created_by: kb_authoring_assistant
    updated_by: kb_authoring_assistant
    version: 5.0-manifest-aligned
    metric_name: Damaged or Lost Shipment Count
    aliases:
    - lost shipments
    - damaged shipments
    metric_type: amount/count/rate/days_by_metric
    unit: currency/count/percentage/days_by_metric
    default_aggregation: SUM or COUNT or ratio by metric
    default_grain: shipment_awb_or_settlement_batch
    polarity: context_dependent
    business_concepts:
    - logistics
    - damaged_lost_shipment_count
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
    - see metric_impl blocks in shiprocket_logistics_partner_parser_ready_v6_role_split.md and shiprocket_services_aggregator_parser_ready_v6_role_split.md
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
    - see metric_impl blocks in shiprocket_logistics_partner_parser_ready_v6_role_split.md and shiprocket_services_aggregator_parser_ready_v6_role_split.md
    evidence_refs:
    - evidence.logistics_kb_doc
    - evidence.cognee_design_v4
    - evidence.unified_edge_scope
```
```yaml
candidate_card:
  card_type: metric
  card_id: metric.delivery_success_rate
  name: Delivery Success Rate
  fields:
    name: Delivery Success Rate
    description: Delivered shipments divided by shipped or forward shipments.
    status: active
    confidence: curated
    source_documents:
    - Logistics KB Doc.docx
    - Cognee KB Design v4.md
    - logistics_gold_std_raw_md_frame_v3.md
    - logistics_gold_std_canonical_card_frame_v5.md
    created_by: kb_authoring_assistant
    updated_by: kb_authoring_assistant
    version: 5.0-manifest-aligned
    metric_name: Delivery Success Rate
    aliases:
    - delivery rate
    - successful delivery percentage
    metric_type: amount/count/rate/days_by_metric
    unit: currency/count/percentage/days_by_metric
    default_aggregation: SUM or COUNT or ratio by metric
    default_grain: shipment_awb_or_settlement_batch
    polarity: context_dependent
    business_concepts:
    - logistics
    - delivery_success_rate
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
  card_id: metric.delivery_tat_days
  name: Delivery TAT Days
  fields:
    name: Delivery TAT Days
    description: Days between pickup/dispatch and delivery.
    status: active
    confidence: curated
    source_documents:
    - Logistics KB Doc.docx
    - Cognee KB Design v4.md
    - logistics_gold_std_raw_md_frame_v3.md
    - logistics_gold_std_canonical_card_frame_v5.md
    created_by: kb_authoring_assistant
    updated_by: kb_authoring_assistant
    version: 5.0-manifest-aligned
    metric_name: Delivery TAT Days
    aliases:
    - delivery turnaround time
    - delivery lag
    metric_type: amount/count/rate/days_by_metric
    unit: currency/count/percentage/days_by_metric
    default_aggregation: SUM or COUNT or ratio by metric
    default_grain: shipment_awb_or_settlement_batch
    polarity: context_dependent
    business_concepts:
    - logistics
    - delivery_tat_days
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
  card_id: metric.forward_shipment_count
  name: Forward Shipment Count
  fields:
    name: Forward Shipment Count
    description: Count of outbound forward shipments.
    status: active
    confidence: curated
    source_documents:
    - Logistics KB Doc.docx
    - Cognee KB Design v4.md
    - logistics_gold_std_raw_md_frame_v3.md
    - logistics_gold_std_canonical_card_frame_v5.md
    created_by: kb_authoring_assistant
    updated_by: kb_authoring_assistant
    version: 5.0-manifest-aligned
    metric_name: Forward Shipment Count
    aliases:
    - outbound shipments
    - forward orders shipped
    metric_type: amount/count/rate/days_by_metric
    unit: currency/count/percentage/days_by_metric
    default_aggregation: SUM or COUNT or ratio by metric
    default_grain: shipment_awb_or_settlement_batch
    polarity: context_dependent
    business_concepts:
    - logistics
    - forward_shipment_count
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
  card_id: metric.in_transit_shipment_count
  name: In-Transit Shipment Count
  fields:
    name: In-Transit Shipment Count
    description: Count of shipments currently or historically marked in transit.
    status: active
    confidence: curated
    source_documents:
    - Logistics KB Doc.docx
    - Cognee KB Design v4.md
    - logistics_gold_std_raw_md_frame_v3.md
    - logistics_gold_std_canonical_card_frame_v5.md
    created_by: kb_authoring_assistant
    updated_by: kb_authoring_assistant
    version: 5.0-manifest-aligned
    metric_name: In-Transit Shipment Count
    aliases:
    - in transit shipments
    metric_type: amount/count/rate/days_by_metric
    unit: currency/count/percentage/days_by_metric
    default_aggregation: SUM or COUNT or ratio by metric
    default_grain: shipment_awb_or_settlement_batch
    polarity: context_dependent
    business_concepts:
    - logistics
    - in_transit_shipment_count
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
  card_id: metric.ndr_attempt_count
  name: NDR Attempt Count
  fields:
    name: NDR Attempt Count
    description: Count or total of non-delivery attempts.
    status: active
    confidence: curated
    source_documents:
    - Logistics KB Doc.docx
    - Cognee KB Design v4.md
    - logistics_gold_std_raw_md_frame_v3.md
    - logistics_gold_std_canonical_card_frame_v5.md
    created_by: kb_authoring_assistant
    updated_by: kb_authoring_assistant
    version: 5.0-manifest-aligned
    metric_name: NDR Attempt Count
    aliases:
    - failed delivery attempts
    - non delivery attempts
    metric_type: amount/count/rate/days_by_metric
    unit: currency/count/percentage/days_by_metric
    default_aggregation: SUM or COUNT or ratio by metric
    default_grain: shipment_awb_or_settlement_batch
    polarity: context_dependent
    business_concepts:
    - logistics
    - ndr_attempt_count
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
  card_id: metric.order_total_amount
  name: Order Total Amount
  fields:
    name: Order Total Amount
    description: Total amount of order from channel/order source.
    status: active
    confidence: curated
    source_documents:
    - Logistics KB Doc.docx
    - Cognee KB Design v4.md
    - logistics_gold_std_raw_md_frame_v3.md
    - logistics_gold_std_canonical_card_frame_v5.md
    created_by: kb_authoring_assistant
    updated_by: kb_authoring_assistant
    version: 5.0-manifest-aligned
    metric_name: Order Total Amount
    aliases:
    - order total
    - GMV for order
    metric_type: amount/count/rate/days_by_metric
    unit: currency/count/percentage/days_by_metric
    default_aggregation: SUM or COUNT or ratio by metric
    default_grain: shipment_awb_or_settlement_batch
    polarity: context_dependent
    business_concepts:
    - logistics
    - order_total_amount
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
  card_id: metric.return_shipment_count
  name: Return Shipment Count
  fields:
    name: Return Shipment Count
    description: Count of customer-initiated reverse/return shipments.
    status: active
    confidence: curated
    source_documents:
    - Logistics KB Doc.docx
    - Cognee KB Design v4.md
    - logistics_gold_std_raw_md_frame_v3.md
    - logistics_gold_std_canonical_card_frame_v5.md
    created_by: kb_authoring_assistant
    updated_by: kb_authoring_assistant
    version: 5.0-manifest-aligned
    metric_name: Return Shipment Count
    aliases:
    - customer returns
    - reverse shipments
    metric_type: amount/count/rate/days_by_metric
    unit: currency/count/percentage/days_by_metric
    default_aggregation: SUM or COUNT or ratio by metric
    default_grain: shipment_awb_or_settlement_batch
    polarity: context_dependent
    business_concepts:
    - logistics
    - return_shipment_count
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
    - see metric_impl blocks in shiprocket_logistics_partner_parser_ready_v6_role_split.md and shiprocket_services_aggregator_parser_ready_v6_role_split.md
    evidence_refs:
    - evidence.logistics_kb_doc
    - evidence.cognee_design_v4
    - evidence.unified_edge_scope
```
```yaml
candidate_card:
  card_type: metric
  card_id: metric.rto_rate
  name: RTO Rate
  fields:
    name: RTO Rate
    description: RTO shipments divided by forward shipments.
    status: active
    confidence: curated
    source_documents:
    - Logistics KB Doc.docx
    - Cognee KB Design v4.md
    - logistics_gold_std_raw_md_frame_v3.md
    - logistics_gold_std_canonical_card_frame_v5.md
    created_by: kb_authoring_assistant
    updated_by: kb_authoring_assistant
    version: 5.0-manifest-aligned
    metric_name: RTO Rate
    aliases:
    - return to origin rate
    metric_type: amount/count/rate/days_by_metric
    unit: currency/count/percentage/days_by_metric
    default_aggregation: SUM or COUNT or ratio by metric
    default_grain: shipment_awb_or_settlement_batch
    polarity: context_dependent
    business_concepts:
    - logistics
    - rto_rate
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
  card_id: metric.rto_tat_days
  name: RTO TAT Days
  fields:
    name: RTO TAT Days
    description: Days between RTO initiation and RTO delivery.
    status: active
    confidence: curated
    source_documents:
    - Logistics KB Doc.docx
    - Cognee KB Design v4.md
    - logistics_gold_std_raw_md_frame_v3.md
    - logistics_gold_std_canonical_card_frame_v5.md
    created_by: kb_authoring_assistant
    updated_by: kb_authoring_assistant
    version: 5.0-manifest-aligned
    metric_name: RTO TAT Days
    aliases:
    - RTO turnaround time
    metric_type: amount/count/rate/days_by_metric
    unit: currency/count/percentage/days_by_metric
    default_aggregation: SUM or COUNT or ratio by metric
    default_grain: shipment_awb_or_settlement_batch
    polarity: context_dependent
    business_concepts:
    - logistics
    - rto_tat_days
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
    - see metric_impl blocks in shiprocket_logistics_partner_parser_ready_v6_role_split.md and shiprocket_services_aggregator_parser_ready_v6_role_split.md
    evidence_refs:
    - evidence.logistics_kb_doc
    - evidence.cognee_design_v4
    - evidence.unified_edge_scope
```
```yaml
candidate_card:
  card_type: metric
  card_id: metric.shipment_pickup_lag_days
  name: Shipment Pickup Lag Days
  fields:
    name: Shipment Pickup Lag Days
    description: Days between AWB assignment or shipment creation and pickup.
    status: active
    confidence: curated
    source_documents:
    - Logistics KB Doc.docx
    - Cognee KB Design v4.md
    - logistics_gold_std_raw_md_frame_v3.md
    - logistics_gold_std_canonical_card_frame_v5.md
    created_by: kb_authoring_assistant
    updated_by: kb_authoring_assistant
    version: 5.0-manifest-aligned
    metric_name: Shipment Pickup Lag Days
    aliases:
    - pickup delay
    - AWB to pickup lag
    metric_type: amount/count/rate/days_by_metric
    unit: currency/count/percentage/days_by_metric
    default_aggregation: SUM or COUNT or ratio by metric
    default_grain: shipment_awb_or_settlement_batch
    polarity: context_dependent
    business_concepts:
    - logistics
    - shipment_pickup_lag_days
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
  card_id: metric_impl.shiprocket_oms.shipment_count
  name: Shiprocket Shipment Count Implementation
  fields:
    name: Shiprocket Shipment Count Implementation
    description: Shipment Count implementation for Shiprocket using shiprocket_oms.
    status: active
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
    implementation_name: Shiprocket Shipment Count
    metric_pattern: filtered_sum_or_count
    applicability: platform=shiprocket; table=zs_observe.shiprocket_oms; account filters via Account Data Binding only
    base_tables:
    - table.zs_observe.shiprocket_oms
    required_columns:
    - column.zs_observe.shiprocket_oms.awb_code
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
    - created_date
    - order_delivered_date
    unit: currency/count/percentage/days_by_metric
    precision: 2_decimal_places
    caveats: Use only with documented amount semantics and grain safety.
    evidence_refs:
    - evidence.logistics_kb_doc
    - evidence.cognee_design_v4
    - evidence.unified_edge_scope
    formula_template_id: formula_template.logistics.filtered_count
```
```yaml
candidate_card:
  card_type: metric_implementation
  card_id: metric_impl.shiprocket_oms.unique_awb_count
  name: Shiprocket Unique AWB Count Implementation
  fields:
    name: Shiprocket Unique AWB Count Implementation
    description: Unique AWB Count implementation for Shiprocket using shiprocket_oms.
    status: active
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
    metric_pattern: filtered_sum_or_count
    applicability: platform=shiprocket; table=zs_observe.shiprocket_oms; account filters via Account Data Binding only
    base_tables:
    - table.zs_observe.shiprocket_oms
    required_columns:
    - column.zs_observe.shiprocket_oms.awb_code
    semantic_filters: []
    formula_description: COUNT(DISTINCT awb_code)
    formula_sql: COUNT(DISTINCT awb_code)
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
    - created_date
    - order_delivered_date
    unit: currency/count/percentage/days_by_metric
    precision: 2_decimal_places
    caveats: Use only with documented amount semantics and grain safety.
    evidence_refs:
    - evidence.logistics_kb_doc
    - evidence.cognee_design_v4
    - evidence.unified_edge_scope
    formula_template_id: formula_template.logistics.filtered_count
```
```yaml
candidate_card:
  card_type: metric_implementation
  card_id: metric_impl.shiprocket_oms.forward_shipment_count
  name: Shiprocket Forward Shipment Count Implementation
  fields:
    name: Shiprocket Forward Shipment Count Implementation
    description: Forward Shipment Count implementation for Shiprocket using shiprocket_oms.
    status: active
    confidence: curated
    source_documents:
    - Logistics KB Doc.docx
    - Cognee KB Design v4.md
    - logistics_gold_std_raw_md_frame_v3.md
    - logistics_gold_std_canonical_card_frame_v5.md
    created_by: kb_authoring_assistant
    updated_by: kb_authoring_assistant
    version: 5.0-manifest-aligned
    metric_id: metric.forward_shipment_count
    implementation_name: Shiprocket Forward Shipment Count
    metric_pattern: filtered_sum_or_count
    applicability: platform=shiprocket; table=zs_observe.shiprocket_oms; account filters via Account Data Binding only
    base_tables:
    - table.zs_observe.shiprocket_oms
    required_columns:
    - column.zs_observe.shiprocket_oms.transaction_type
    semantic_filters:
    - transaction_type='forward'
    formula_description: COUNT_IF(transaction_type='forward')
    formula_sql: COUNT_IF(transaction_type='forward')
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
    - created_date
    - order_delivered_date
    unit: currency/count/percentage/days_by_metric
    precision: 2_decimal_places
    caveats: Use only with documented amount semantics and grain safety.
    evidence_refs:
    - evidence.logistics_kb_doc
    - evidence.cognee_design_v4
    - evidence.unified_edge_scope
    formula_template_id: formula_template.logistics.filtered_count
```
```yaml
candidate_card:
  card_type: metric_implementation
  card_id: metric_impl.shiprocket_oms.delivered_shipment_count
  name: Shiprocket Delivered Shipment Count Implementation
  fields:
    name: Shiprocket Delivered Shipment Count Implementation
    description: Delivered Shipment Count implementation for Shiprocket using shiprocket_oms.
    status: active
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
    implementation_name: Shiprocket Delivered Shipment Count
    metric_pattern: filtered_sum_or_count
    applicability: platform=shiprocket; table=zs_observe.shiprocket_oms; account filters via Account Data Binding only
    base_tables:
    - table.zs_observe.shiprocket_oms
    required_columns:
    - column.zs_observe.shiprocket_oms.status
    semantic_filters:
    - status='DELIVERED'
    formula_description: COUNT_IF(status='DELIVERED')
    formula_sql: COUNT_IF(status='DELIVERED')
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
    - created_date
    - order_delivered_date
    unit: currency/count/percentage/days_by_metric
    precision: 2_decimal_places
    caveats: Use only with documented amount semantics and grain safety.
    evidence_refs:
    - evidence.logistics_kb_doc
    - evidence.cognee_design_v4
    - evidence.unified_edge_scope
    formula_template_id: formula_template.logistics.filtered_count
```
```yaml
candidate_card:
  card_type: metric_implementation
  card_id: metric_impl.shiprocket_oms.rto_count
  name: Shiprocket RTO Count Implementation
  fields:
    name: Shiprocket RTO Count Implementation
    description: RTO Count implementation for Shiprocket using shiprocket_oms.
    status: active
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
    implementation_name: Shiprocket RTO Count
    metric_pattern: filtered_sum_or_count
    applicability: platform=shiprocket; table=zs_observe.shiprocket_oms; account filters via Account Data Binding only
    base_tables:
    - table.zs_observe.shiprocket_oms
    required_columns:
    - column.zs_observe.shiprocket_oms.status
    semantic_filters:
    - status='RTO DELIVERED'
    formula_description: COUNT_IF(status='RTO DELIVERED')
    formula_sql: COUNT_IF(status='RTO DELIVERED')
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
    - created_date
    - order_delivered_date
    unit: currency/count/percentage/days_by_metric
    precision: 2_decimal_places
    caveats: Use only with documented amount semantics and grain safety.
    evidence_refs:
    - evidence.logistics_kb_doc
    - evidence.cognee_design_v4
    - evidence.unified_edge_scope
    formula_template_id: formula_template.logistics.filtered_count
```
```yaml
candidate_card:
  card_type: metric_implementation
  card_id: metric_impl.shiprocket_oms.return_shipment_count
  name: Shiprocket Return Shipment Count Implementation
  fields:
    name: Shiprocket Return Shipment Count Implementation
    description: Return Shipment Count implementation for Shiprocket using shiprocket_oms.
    status: active
    confidence: curated
    source_documents:
    - Logistics KB Doc.docx
    - Cognee KB Design v4.md
    - logistics_gold_std_raw_md_frame_v3.md
    - logistics_gold_std_canonical_card_frame_v5.md
    created_by: kb_authoring_assistant
    updated_by: kb_authoring_assistant
    version: 5.0-manifest-aligned
    metric_id: metric.return_shipment_count
    implementation_name: Shiprocket Return Shipment Count
    metric_pattern: filtered_sum_or_count
    applicability: platform=shiprocket; table=zs_observe.shiprocket_oms; account filters via Account Data Binding only
    base_tables:
    - table.zs_observe.shiprocket_oms
    required_columns:
    - column.zs_observe.shiprocket_oms.transaction_type
    semantic_filters:
    - transaction_type='return'
    formula_description: COUNT_IF(transaction_type='return')
    formula_sql: COUNT_IF(transaction_type='return')
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
    - created_date
    - order_delivered_date
    unit: currency/count/percentage/days_by_metric
    precision: 2_decimal_places
    caveats: Use only with documented amount semantics and grain safety.
    evidence_refs:
    - evidence.logistics_kb_doc
    - evidence.cognee_design_v4
    - evidence.unified_edge_scope
    formula_template_id: formula_template.logistics.filtered_count
```
```yaml
candidate_card:
  card_type: metric_implementation
  card_id: metric_impl.shiprocket_oms.cancelled_shipment_count
  name: Shiprocket Cancelled Shipment Count Implementation
  fields:
    name: Shiprocket Cancelled Shipment Count Implementation
    description: Cancelled Shipment Count implementation for Shiprocket using shiprocket_oms.
    status: active
    confidence: curated
    source_documents:
    - Logistics KB Doc.docx
    - Cognee KB Design v4.md
    - logistics_gold_std_raw_md_frame_v3.md
    - logistics_gold_std_canonical_card_frame_v5.md
    created_by: kb_authoring_assistant
    updated_by: kb_authoring_assistant
    version: 5.0-manifest-aligned
    metric_id: metric.cancelled_shipment_count
    implementation_name: Shiprocket Cancelled Shipment Count
    metric_pattern: filtered_sum_or_count
    applicability: platform=shiprocket; table=zs_observe.shiprocket_oms; account filters via Account Data Binding only
    base_tables:
    - table.zs_observe.shiprocket_oms
    required_columns:
    - column.zs_observe.shiprocket_oms.transaction_type
    - column.zs_observe.shiprocket_oms.status
    semantic_filters:
    - cancelled statuses
    formula_description: COUNT_IF(transaction_type='cancelled' OR status='CANCELLED')
    formula_sql: COUNT_IF(transaction_type='cancelled' OR status='CANCELLED')
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
    - created_date
    - order_delivered_date
    unit: currency/count/percentage/days_by_metric
    precision: 2_decimal_places
    caveats: Use only with documented amount semantics and grain safety.
    evidence_refs:
    - evidence.logistics_kb_doc
    - evidence.cognee_design_v4
    - evidence.unified_edge_scope
    formula_template_id: formula_template.logistics.filtered_count
```
```yaml
candidate_card:
  card_type: metric_implementation
  card_id: metric_impl.shiprocket_oms.in_transit_shipment_count
  name: Shiprocket In-Transit Shipment Count Implementation
  fields:
    name: Shiprocket In-Transit Shipment Count Implementation
    description: In-Transit Shipment Count implementation for Shiprocket using shiprocket_oms.
    status: active
    confidence: curated
    source_documents:
    - Logistics KB Doc.docx
    - Cognee KB Design v4.md
    - logistics_gold_std_raw_md_frame_v3.md
    - logistics_gold_std_canonical_card_frame_v5.md
    created_by: kb_authoring_assistant
    updated_by: kb_authoring_assistant
    version: 5.0-manifest-aligned
    metric_id: metric.in_transit_shipment_count
    implementation_name: Shiprocket In-Transit Shipment Count
    metric_pattern: filtered_sum_or_count
    applicability: platform=shiprocket; table=zs_observe.shiprocket_oms; account filters via Account Data Binding only
    base_tables:
    - table.zs_observe.shiprocket_oms
    required_columns:
    - column.zs_observe.shiprocket_oms.transaction_type
    semantic_filters:
    - transaction_type='in transit'
    formula_description: COUNT_IF(transaction_type='in transit')
    formula_sql: COUNT_IF(transaction_type='in transit')
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
    - created_date
    - order_delivered_date
    unit: currency/count/percentage/days_by_metric
    precision: 2_decimal_places
    caveats: Use only with documented amount semantics and grain safety.
    evidence_refs:
    - evidence.logistics_kb_doc
    - evidence.cognee_design_v4
    - evidence.unified_edge_scope
    formula_template_id: formula_template.logistics.filtered_count
```
```yaml
candidate_card:
  card_type: metric_implementation
  card_id: metric_impl.shiprocket_oms.damaged_lost_shipment_count
  name: Shiprocket Damaged or Lost Shipment Count Implementation
  fields:
    name: Shiprocket Damaged or Lost Shipment Count Implementation
    description: Damaged or Lost Shipment Count implementation for Shiprocket using shiprocket_oms.
    status: active
    confidence: curated
    source_documents:
    - Logistics KB Doc.docx
    - Cognee KB Design v4.md
    - logistics_gold_std_raw_md_frame_v3.md
    - logistics_gold_std_canonical_card_frame_v5.md
    created_by: kb_authoring_assistant
    updated_by: kb_authoring_assistant
    version: 5.0-manifest-aligned
    metric_id: metric.damaged_lost_shipment_count
    implementation_name: Shiprocket Damaged or Lost Shipment Count
    metric_pattern: filtered_sum_or_count
    applicability: platform=shiprocket; table=zs_observe.shiprocket_oms; account filters via Account Data Binding only
    base_tables:
    - table.zs_observe.shiprocket_oms
    required_columns:
    - column.zs_observe.shiprocket_oms.transaction_type
    - column.zs_observe.shiprocket_oms.status
    semantic_filters:
    - damaged/lost statuses
    formula_description: COUNT_IF(transaction_type='damaged/lost' OR status='DAMAGED/LOST')
    formula_sql: COUNT_IF(transaction_type='damaged/lost' OR status='DAMAGED/LOST')
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
    - created_date
    - order_delivered_date
    unit: currency/count/percentage/days_by_metric
    precision: 2_decimal_places
    caveats: Use only with documented amount semantics and grain safety.
    evidence_refs:
    - evidence.logistics_kb_doc
    - evidence.cognee_design_v4
    - evidence.unified_edge_scope
    formula_template_id: formula_template.logistics.filtered_count
```
```yaml
candidate_card:
  card_type: metric_implementation
  card_id: metric_impl.shiprocket_oms.delivery_success_rate
  name: Shiprocket Delivery Success Rate Implementation
  fields:
    name: Shiprocket Delivery Success Rate Implementation
    description: Delivery Success Rate implementation for Shiprocket using shiprocket_oms.
    status: active
    confidence: curated
    source_documents:
    - Logistics KB Doc.docx
    - Cognee KB Design v4.md
    - logistics_gold_std_raw_md_frame_v3.md
    - logistics_gold_std_canonical_card_frame_v5.md
    created_by: kb_authoring_assistant
    updated_by: kb_authoring_assistant
    version: 5.0-manifest-aligned
    metric_id: metric.delivery_success_rate
    implementation_name: Shiprocket Delivery Success Rate
    metric_pattern: count_or_rate_or_lag
    applicability: platform=shiprocket; table=zs_observe.shiprocket_oms; account filters via Account Data Binding only
    base_tables:
    - table.zs_observe.shiprocket_oms
    required_columns:
    - column.zs_observe.shiprocket_oms.status
    - column.zs_observe.shiprocket_oms.transaction_type
    semantic_filters:
    - forward delivered denominator
    formula_description: delivered_shipment_count / NULLIF(forward_shipment_count,0)
    formula_sql: delivered_shipment_count / NULLIF(forward_shipment_count,0)
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
    - created_date
    - order_delivered_date
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
  card_id: metric_impl.shiprocket_oms.rto_rate
  name: Shiprocket RTO Rate Implementation
  fields:
    name: Shiprocket RTO Rate Implementation
    description: RTO Rate implementation for Shiprocket using shiprocket_oms.
    status: active
    confidence: curated
    source_documents:
    - Logistics KB Doc.docx
    - Cognee KB Design v4.md
    - logistics_gold_std_raw_md_frame_v3.md
    - logistics_gold_std_canonical_card_frame_v5.md
    created_by: kb_authoring_assistant
    updated_by: kb_authoring_assistant
    version: 5.0-manifest-aligned
    metric_id: metric.rto_rate
    implementation_name: Shiprocket RTO Rate
    metric_pattern: count_or_rate_or_lag
    applicability: platform=shiprocket; table=zs_observe.shiprocket_oms; account filters via Account Data Binding only
    base_tables:
    - table.zs_observe.shiprocket_oms
    required_columns:
    - column.zs_observe.shiprocket_oms.status
    - column.zs_observe.shiprocket_oms.transaction_type
    semantic_filters:
    - forward denominator
    formula_description: rto_count / NULLIF(forward_shipment_count,0)
    formula_sql: rto_count / NULLIF(forward_shipment_count,0)
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
    - created_date
    - order_delivered_date
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
  card_id: metric_impl.shiprocket_oms.declared_product_value
  name: Shiprocket Declared Product Value Implementation
  fields:
    name: Shiprocket Declared Product Value Implementation
    description: Declared Product Value implementation for Shiprocket using shiprocket_oms.
    status: active
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
    implementation_name: Shiprocket Declared Product Value
    metric_pattern: filtered_sum_or_count
    applicability: platform=shiprocket; table=zs_observe.shiprocket_oms; account filters via Account Data Binding only
    base_tables:
    - table.zs_observe.shiprocket_oms
    required_columns:
    - column.zs_observe.shiprocket_oms.charged_amount
    semantic_filters:
    - charged_amount is declared product value
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
    - created_date
    - order_delivered_date
    unit: currency/count/percentage/days_by_metric
    precision: 2_decimal_places
    caveats: Use only with documented amount semantics and grain safety.
    evidence_refs:
    - evidence.logistics_kb_doc
    - evidence.cognee_design_v4
    - evidence.unified_edge_scope
    formula_template_id: formula_template.logistics.filtered_count
```
```yaml
candidate_card:
  card_type: metric_implementation
  card_id: metric_impl.shiprocket_oms.order_total_amount
  name: Shiprocket Order Total Amount Implementation
  fields:
    name: Shiprocket Order Total Amount Implementation
    description: Order Total Amount implementation for Shiprocket using shiprocket_oms.
    status: active
    confidence: curated
    source_documents:
    - Logistics KB Doc.docx
    - Cognee KB Design v4.md
    - logistics_gold_std_raw_md_frame_v3.md
    - logistics_gold_std_canonical_card_frame_v5.md
    created_by: kb_authoring_assistant
    updated_by: kb_authoring_assistant
    version: 5.0-manifest-aligned
    metric_id: metric.order_total_amount
    implementation_name: Shiprocket Order Total Amount
    metric_pattern: filtered_sum_or_count
    applicability: platform=shiprocket; table=zs_observe.shiprocket_oms; account filters via Account Data Binding only
    base_tables:
    - table.zs_observe.shiprocket_oms
    required_columns:
    - column.zs_observe.shiprocket_oms.order_total
    semantic_filters: []
    formula_description: SUM(order_total)
    formula_sql: SUM(order_total)
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
    - created_date
    - order_delivered_date
    unit: currency/count/percentage/days_by_metric
    precision: 2_decimal_places
    caveats: Use only with documented amount semantics and grain safety.
    evidence_refs:
    - evidence.logistics_kb_doc
    - evidence.cognee_design_v4
    - evidence.unified_edge_scope
    formula_template_id: formula_template.logistics.filtered_count
```
```yaml
candidate_card:
  card_type: metric_implementation
  card_id: metric_impl.shiprocket_oms.cod_expected_amount
  name: Shiprocket COD Expected Amount Implementation
  fields:
    name: Shiprocket COD Expected Amount Implementation
    description: COD Expected Amount implementation for Shiprocket using shiprocket_oms.
    status: active
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
    implementation_name: Shiprocket COD Expected Amount
    metric_pattern: filtered_sum_or_count
    applicability: platform=shiprocket; table=zs_observe.shiprocket_oms; account filters via Account Data Binding only
    base_tables:
    - table.zs_observe.shiprocket_oms
    required_columns:
    - column.zs_observe.shiprocket_oms.cod_payble_amount
    semantic_filters:
    - payment_method='cod'
    formula_description: SUM(cod_payble_amount)
    formula_sql: SUM(cod_payble_amount)
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
    - created_date
    - order_delivered_date
    unit: currency/count/percentage/days_by_metric
    precision: 2_decimal_places
    caveats: Use only with documented amount semantics and grain safety.
    evidence_refs:
    - evidence.logistics_kb_doc
    - evidence.cognee_design_v4
    - evidence.unified_edge_scope
    formula_template_id: formula_template.logistics.filtered_count
```
```yaml
candidate_card:
  card_type: metric_implementation
  card_id: metric_impl.shiprocket_oms.cod_remitted_amount
  name: Shiprocket COD Remitted Amount Implementation
  fields:
    name: Shiprocket COD Remitted Amount Implementation
    description: COD Remitted Amount implementation for Shiprocket using shiprocket_oms.
    status: active
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
    metric_pattern: filtered_sum_or_count
    applicability: platform=shiprocket; table=zs_observe.shiprocket_oms; account filters via Account Data Binding only
    base_tables:
    - table.zs_observe.shiprocket_oms
    required_columns:
    - column.zs_observe.shiprocket_oms.remitted_amount
    semantic_filters: []
    formula_description: SUM(remitted_amount)
    formula_sql: SUM(remitted_amount)
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
    - created_date
    - order_delivered_date
    unit: currency/count/percentage/days_by_metric
    precision: 2_decimal_places
    caveats: Use only with documented amount semantics and grain safety.
    evidence_refs:
    - evidence.logistics_kb_doc
    - evidence.cognee_design_v4
    - evidence.unified_edge_scope
    formula_template_id: formula_template.logistics.filtered_count
```
```yaml
candidate_card:
  card_type: metric_implementation
  card_id: metric_impl.shiprocket_oms.cod_remittance_lag_days
  name: Shiprocket COD Remittance Lag Days Implementation
  fields:
    name: Shiprocket COD Remittance Lag Days Implementation
    description: COD Remittance Lag Days implementation for Shiprocket using shiprocket_oms.
    status: active
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
    metric_pattern: count_or_rate_or_lag
    applicability: platform=shiprocket; table=zs_observe.shiprocket_oms; account filters via Account Data Binding only
    base_tables:
    - table.zs_observe.shiprocket_oms
    required_columns:
    - column.zs_observe.shiprocket_oms.order_delivered_date
    - column.zs_observe.shiprocket_oms.cod_remittance_date
    semantic_filters: []
    formula_description: AVG(DATE_DIFF('day', order_delivered_date, cod_remittance_date))
    formula_sql: AVG(DATE_DIFF('day', order_delivered_date, cod_remittance_date))
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
    - created_date
    - order_delivered_date
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
  card_id: metric_impl.shiprocket_oms.shipment_pickup_lag_days
  name: Shiprocket Shipment Pickup Lag Days Implementation
  fields:
    name: Shiprocket Shipment Pickup Lag Days Implementation
    description: Shipment Pickup Lag Days implementation for Shiprocket using shiprocket_oms.
    status: active
    confidence: curated
    source_documents:
    - Logistics KB Doc.docx
    - Cognee KB Design v4.md
    - logistics_gold_std_raw_md_frame_v3.md
    - logistics_gold_std_canonical_card_frame_v5.md
    created_by: kb_authoring_assistant
    updated_by: kb_authoring_assistant
    version: 5.0-manifest-aligned
    metric_id: metric.shipment_pickup_lag_days
    implementation_name: Shiprocket Shipment Pickup Lag Days
    metric_pattern: count_or_rate_or_lag
    applicability: platform=shiprocket; table=zs_observe.shiprocket_oms; account filters via Account Data Binding only
    base_tables:
    - table.zs_observe.shiprocket_oms
    required_columns:
    - column.zs_observe.shiprocket_oms.awb_assigned_date
    - column.zs_observe.shiprocket_oms.order_picked_up_date
    semantic_filters: []
    formula_description: AVG(DATE_DIFF('day', awb_assigned_date, order_picked_up_date))
    formula_sql: AVG(DATE_DIFF('day', awb_assigned_date, order_picked_up_date))
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
    - created_date
    - order_delivered_date
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
  card_id: metric_impl.shiprocket_oms.delivery_tat_days
  name: Shiprocket Delivery TAT Days Implementation
  fields:
    name: Shiprocket Delivery TAT Days Implementation
    description: Delivery TAT Days implementation for Shiprocket using shiprocket_oms.
    status: active
    confidence: curated
    source_documents:
    - Logistics KB Doc.docx
    - Cognee KB Design v4.md
    - logistics_gold_std_raw_md_frame_v3.md
    - logistics_gold_std_canonical_card_frame_v5.md
    created_by: kb_authoring_assistant
    updated_by: kb_authoring_assistant
    version: 5.0-manifest-aligned
    metric_id: metric.delivery_tat_days
    implementation_name: Shiprocket Delivery TAT Days
    metric_pattern: filtered_sum_or_count
    applicability: platform=shiprocket; table=zs_observe.shiprocket_oms; account filters via Account Data Binding only
    base_tables:
    - table.zs_observe.shiprocket_oms
    required_columns:
    - column.zs_observe.shiprocket_oms.order_picked_up_date
    - column.zs_observe.shiprocket_oms.order_delivered_date
    semantic_filters: []
    formula_description: AVG(DATE_DIFF('day', order_picked_up_date, order_delivered_date))
    formula_sql: AVG(DATE_DIFF('day', order_picked_up_date, order_delivered_date))
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
    - created_date
    - order_delivered_date
    unit: currency/count/percentage/days_by_metric
    precision: 2_decimal_places
    caveats: Use only with documented amount semantics and grain safety.
    evidence_refs:
    - evidence.logistics_kb_doc
    - evidence.cognee_design_v4
    - evidence.unified_edge_scope
    formula_template_id: formula_template.logistics.filtered_count
```
```yaml
candidate_card:
  card_type: metric_implementation
  card_id: metric_impl.shiprocket_oms.rto_tat_days
  name: Shiprocket RTO TAT Days Implementation
  fields:
    name: Shiprocket RTO TAT Days Implementation
    description: RTO TAT Days implementation for Shiprocket using shiprocket_oms.
    status: active
    confidence: curated
    source_documents:
    - Logistics KB Doc.docx
    - Cognee KB Design v4.md
    - logistics_gold_std_raw_md_frame_v3.md
    - logistics_gold_std_canonical_card_frame_v5.md
    created_by: kb_authoring_assistant
    updated_by: kb_authoring_assistant
    version: 5.0-manifest-aligned
    metric_id: metric.rto_tat_days
    implementation_name: Shiprocket RTO TAT Days
    metric_pattern: filtered_sum_or_count
    applicability: platform=shiprocket; table=zs_observe.shiprocket_oms; account filters via Account Data Binding only
    base_tables:
    - table.zs_observe.shiprocket_oms
    required_columns:
    - column.zs_observe.shiprocket_oms.rto_initiated_date
    - column.zs_observe.shiprocket_oms.rto_delivered_date
    semantic_filters: []
    formula_description: AVG(DATE_DIFF('day', rto_initiated_date, rto_delivered_date))
    formula_sql: AVG(DATE_DIFF('day', rto_initiated_date, rto_delivered_date))
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
    - created_date
    - order_delivered_date
    unit: currency/count/percentage/days_by_metric
    precision: 2_decimal_places
    caveats: Use only with documented amount semantics and grain safety.
    evidence_refs:
    - evidence.logistics_kb_doc
    - evidence.cognee_design_v4
    - evidence.unified_edge_scope
    formula_template_id: formula_template.logistics.filtered_count
```
```yaml
candidate_card:
  card_type: metric_implementation
  card_id: metric_impl.shiprocket_oms.ndr_attempt_count
  name: Shiprocket NDR Attempt Count Implementation
  fields:
    name: Shiprocket NDR Attempt Count Implementation
    description: NDR Attempt Count implementation for Shiprocket using shiprocket_oms.
    status: active
    confidence: curated
    source_documents:
    - Logistics KB Doc.docx
    - Cognee KB Design v4.md
    - logistics_gold_std_raw_md_frame_v3.md
    - logistics_gold_std_canonical_card_frame_v5.md
    created_by: kb_authoring_assistant
    updated_by: kb_authoring_assistant
    version: 5.0-manifest-aligned
    metric_id: metric.ndr_attempt_count
    implementation_name: Shiprocket NDR Attempt Count
    metric_pattern: filtered_sum_or_count
    applicability: platform=shiprocket; table=zs_observe.shiprocket_oms; account filters via Account Data Binding only
    base_tables:
    - table.zs_observe.shiprocket_oms
    required_columns:
    - column.zs_observe.shiprocket_oms.attempt_count
    semantic_filters: []
    formula_description: SUM(attempt_count)
    formula_sql: SUM(attempt_count)
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
    - created_date
    - order_delivered_date
    unit: currency/count/percentage/days_by_metric
    precision: 2_decimal_places
    caveats: Use only with documented amount semantics and grain safety.
    evidence_refs:
    - evidence.logistics_kb_doc
    - evidence.cognee_design_v4
    - evidence.unified_edge_scope
    formula_template_id: formula_template.logistics.filtered_count
```
```yaml
candidate_card:
  card_type: metric_implementation
  card_id: metric_impl.shiprocket_oms.average_delivery_attempts
  name: Shiprocket Average Delivery Attempts Implementation
  fields:
    name: Shiprocket Average Delivery Attempts Implementation
    description: Average Delivery Attempts implementation for Shiprocket using shiprocket_oms.
    status: active
    confidence: curated
    source_documents:
    - Logistics KB Doc.docx
    - Cognee KB Design v4.md
    - logistics_gold_std_raw_md_frame_v3.md
    - logistics_gold_std_canonical_card_frame_v5.md
    created_by: kb_authoring_assistant
    updated_by: kb_authoring_assistant
    version: 5.0-manifest-aligned
    metric_id: metric.average_delivery_attempts
    implementation_name: Shiprocket Average Delivery Attempts
    metric_pattern: filtered_sum_or_count
    applicability: platform=shiprocket; table=zs_observe.shiprocket_oms; account filters via Account Data Binding only
    base_tables:
    - table.zs_observe.shiprocket_oms
    required_columns:
    - column.zs_observe.shiprocket_oms.attempt_count
    semantic_filters: []
    formula_description: AVG(attempt_count)
    formula_sql: AVG(attempt_count)
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
    - created_date
    - order_delivered_date
    unit: currency/count/percentage/days_by_metric
    precision: 2_decimal_places
    caveats: Use only with documented amount semantics and grain safety.
    evidence_refs:
    - evidence.logistics_kb_doc
    - evidence.cognee_design_v4
    - evidence.unified_edge_scope
    formula_template_id: formula_template.logistics.filtered_count
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
  edge_id: edge.metric.average_delivery_attempts.belongs_to_domain.domain.logistics_reconciliation
  edge_type: BELONGS_TO_DOMAIN
  source: metric.average_delivery_attempts
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
  edge_id: edge.metric.cancelled_shipment_count.belongs_to_domain.domain.logistics_reconciliation
  edge_type: BELONGS_TO_DOMAIN
  source: metric.cancelled_shipment_count
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
  edge_id: edge.metric.damaged_lost_shipment_count.belongs_to_domain.domain.logistics_reconciliation
  edge_type: BELONGS_TO_DOMAIN
  source: metric.damaged_lost_shipment_count
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
  edge_id: edge.metric.delivery_success_rate.belongs_to_domain.domain.logistics_reconciliation
  edge_type: BELONGS_TO_DOMAIN
  source: metric.delivery_success_rate
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
  edge_id: edge.metric.delivery_tat_days.belongs_to_domain.domain.logistics_reconciliation
  edge_type: BELONGS_TO_DOMAIN
  source: metric.delivery_tat_days
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
  edge_id: edge.metric.forward_shipment_count.belongs_to_domain.domain.logistics_reconciliation
  edge_type: BELONGS_TO_DOMAIN
  source: metric.forward_shipment_count
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
  edge_id: edge.metric.in_transit_shipment_count.belongs_to_domain.domain.logistics_reconciliation
  edge_type: BELONGS_TO_DOMAIN
  source: metric.in_transit_shipment_count
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
  edge_id: edge.metric.ndr_attempt_count.belongs_to_domain.domain.logistics_reconciliation
  edge_type: BELONGS_TO_DOMAIN
  source: metric.ndr_attempt_count
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
  edge_id: edge.metric.order_total_amount.belongs_to_domain.domain.logistics_reconciliation
  edge_type: BELONGS_TO_DOMAIN
  source: metric.order_total_amount
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
  edge_id: edge.metric.return_shipment_count.belongs_to_domain.domain.logistics_reconciliation
  edge_type: BELONGS_TO_DOMAIN
  source: metric.return_shipment_count
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
  edge_id: edge.metric.rto_rate.belongs_to_domain.domain.logistics_reconciliation
  edge_type: BELONGS_TO_DOMAIN
  source: metric.rto_rate
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
  edge_id: edge.metric.rto_tat_days.belongs_to_domain.domain.logistics_reconciliation
  edge_type: BELONGS_TO_DOMAIN
  source: metric.rto_tat_days
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
  edge_id: edge.metric.shipment_pickup_lag_days.belongs_to_domain.domain.logistics_reconciliation
  edge_type: BELONGS_TO_DOMAIN
  source: metric.shipment_pickup_lag_days
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
  edge_id: edge.table.zs_observe.shiprocket_oms.sourced_from_platform.platform.shiprocket
  edge_type: SOURCED_FROM_PLATFORM
  source: table.zs_observe.shiprocket_oms
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
  edge_id: edge.table.zs_observe.shiprocket_oms.applies_to_platform.platform.shiprocket
  edge_type: APPLIES_TO_PLATFORM
  source: table.zs_observe.shiprocket_oms
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
  edge_id: edge.table.zs_observe.shiprocket_oms.has_column.column.zs_observe.shiprocket_oms.order_id
  edge_type: HAS_COLUMN
  source: table.zs_observe.shiprocket_oms
  target: column.zs_observe.shiprocket_oms.order_id
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
  edge_id: edge.column.zs_observe.shiprocket_oms.order_id.belongs_to_table.table.zs_observe.shiprocket_oms
  edge_type: BELONGS_TO_TABLE
  source: column.zs_observe.shiprocket_oms.order_id
  target: table.zs_observe.shiprocket_oms
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
    materialized_from: edge.table.zs_observe.shiprocket_oms.has_column.column.zs_observe.shiprocket_oms.order_id
```
```yaml
candidate_edge:
  edge_id: edge.table.zs_observe.shiprocket_oms.has_column.column.zs_observe.shiprocket_oms.channel
  edge_type: HAS_COLUMN
  source: table.zs_observe.shiprocket_oms
  target: column.zs_observe.shiprocket_oms.channel
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
  edge_id: edge.column.zs_observe.shiprocket_oms.channel.belongs_to_table.table.zs_observe.shiprocket_oms
  edge_type: BELONGS_TO_TABLE
  source: column.zs_observe.shiprocket_oms.channel
  target: table.zs_observe.shiprocket_oms
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
    materialized_from: edge.table.zs_observe.shiprocket_oms.has_column.column.zs_observe.shiprocket_oms.channel
```
```yaml
candidate_edge:
  edge_id: edge.table.zs_observe.shiprocket_oms.has_column.column.zs_observe.shiprocket_oms.channel_sku
  edge_type: HAS_COLUMN
  source: table.zs_observe.shiprocket_oms
  target: column.zs_observe.shiprocket_oms.channel_sku
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
  edge_id: edge.column.zs_observe.shiprocket_oms.channel_sku.belongs_to_table.table.zs_observe.shiprocket_oms
  edge_type: BELONGS_TO_TABLE
  source: column.zs_observe.shiprocket_oms.channel_sku
  target: table.zs_observe.shiprocket_oms
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
    materialized_from: edge.table.zs_observe.shiprocket_oms.has_column.column.zs_observe.shiprocket_oms.channel_sku
```
```yaml
candidate_edge:
  edge_id: edge.table.zs_observe.shiprocket_oms.has_column.column.zs_observe.shiprocket_oms.master_sku
  edge_type: HAS_COLUMN
  source: table.zs_observe.shiprocket_oms
  target: column.zs_observe.shiprocket_oms.master_sku
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
  edge_id: edge.column.zs_observe.shiprocket_oms.master_sku.belongs_to_table.table.zs_observe.shiprocket_oms
  edge_type: BELONGS_TO_TABLE
  source: column.zs_observe.shiprocket_oms.master_sku
  target: table.zs_observe.shiprocket_oms
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
    materialized_from: edge.table.zs_observe.shiprocket_oms.has_column.column.zs_observe.shiprocket_oms.master_sku
```
```yaml
candidate_edge:
  edge_id: edge.table.zs_observe.shiprocket_oms.has_column.column.zs_observe.shiprocket_oms.product_name
  edge_type: HAS_COLUMN
  source: table.zs_observe.shiprocket_oms
  target: column.zs_observe.shiprocket_oms.product_name
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
  edge_id: edge.column.zs_observe.shiprocket_oms.product_name.belongs_to_table.table.zs_observe.shiprocket_oms
  edge_type: BELONGS_TO_TABLE
  source: column.zs_observe.shiprocket_oms.product_name
  target: table.zs_observe.shiprocket_oms
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
    materialized_from: edge.table.zs_observe.shiprocket_oms.has_column.column.zs_observe.shiprocket_oms.product_name
```
```yaml
candidate_edge:
  edge_id: edge.table.zs_observe.shiprocket_oms.has_column.column.zs_observe.shiprocket_oms.product_category
  edge_type: HAS_COLUMN
  source: table.zs_observe.shiprocket_oms
  target: column.zs_observe.shiprocket_oms.product_category
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
  edge_id: edge.column.zs_observe.shiprocket_oms.product_category.belongs_to_table.table.zs_observe.shiprocket_oms
  edge_type: BELONGS_TO_TABLE
  source: column.zs_observe.shiprocket_oms.product_category
  target: table.zs_observe.shiprocket_oms
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
    materialized_from: edge.table.zs_observe.shiprocket_oms.has_column.column.zs_observe.shiprocket_oms.product_category
```
```yaml
candidate_edge:
  edge_id: edge.table.zs_observe.shiprocket_oms.has_column.column.zs_observe.shiprocket_oms.fulfilment_channel
  edge_type: HAS_COLUMN
  source: table.zs_observe.shiprocket_oms
  target: column.zs_observe.shiprocket_oms.fulfilment_channel
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
  edge_id: edge.column.zs_observe.shiprocket_oms.fulfilment_channel.belongs_to_table.table.zs_observe.shiprocket_oms
  edge_type: BELONGS_TO_TABLE
  source: column.zs_observe.shiprocket_oms.fulfilment_channel
  target: table.zs_observe.shiprocket_oms
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
    materialized_from: edge.table.zs_observe.shiprocket_oms.has_column.column.zs_observe.shiprocket_oms.fulfilment_channel
```
```yaml
candidate_edge:
  edge_id: edge.table.zs_observe.shiprocket_oms.has_column.column.zs_observe.shiprocket_oms.courier_company
  edge_type: HAS_COLUMN
  source: table.zs_observe.shiprocket_oms
  target: column.zs_observe.shiprocket_oms.courier_company
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
  edge_id: edge.column.zs_observe.shiprocket_oms.courier_company.belongs_to_table.table.zs_observe.shiprocket_oms
  edge_type: BELONGS_TO_TABLE
  source: column.zs_observe.shiprocket_oms.courier_company
  target: table.zs_observe.shiprocket_oms
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
    materialized_from: edge.table.zs_observe.shiprocket_oms.has_column.column.zs_observe.shiprocket_oms.courier_company
```
```yaml
candidate_edge:
  edge_id: edge.table.zs_observe.shiprocket_oms.has_column.column.zs_observe.shiprocket_oms.awb_code
  edge_type: HAS_COLUMN
  source: table.zs_observe.shiprocket_oms
  target: column.zs_observe.shiprocket_oms.awb_code
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
  edge_id: edge.column.zs_observe.shiprocket_oms.awb_code.belongs_to_table.table.zs_observe.shiprocket_oms
  edge_type: BELONGS_TO_TABLE
  source: column.zs_observe.shiprocket_oms.awb_code
  target: table.zs_observe.shiprocket_oms
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
    materialized_from: edge.table.zs_observe.shiprocket_oms.has_column.column.zs_observe.shiprocket_oms.awb_code
```
```yaml
candidate_edge:
  edge_id: edge.table.zs_observe.shiprocket_oms.has_column.column.zs_observe.shiprocket_oms.master_courier
  edge_type: HAS_COLUMN
  source: table.zs_observe.shiprocket_oms
  target: column.zs_observe.shiprocket_oms.master_courier
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
  edge_id: edge.column.zs_observe.shiprocket_oms.master_courier.belongs_to_table.table.zs_observe.shiprocket_oms
  edge_type: BELONGS_TO_TABLE
  source: column.zs_observe.shiprocket_oms.master_courier
  target: table.zs_observe.shiprocket_oms
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
    materialized_from: edge.table.zs_observe.shiprocket_oms.has_column.column.zs_observe.shiprocket_oms.master_courier
```
```yaml
candidate_edge:
  edge_id: edge.table.zs_observe.shiprocket_oms.has_column.column.zs_observe.shiprocket_oms.transaction_type
  edge_type: HAS_COLUMN
  source: table.zs_observe.shiprocket_oms
  target: column.zs_observe.shiprocket_oms.transaction_type
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
  edge_id: edge.column.zs_observe.shiprocket_oms.transaction_type.belongs_to_table.table.zs_observe.shiprocket_oms
  edge_type: BELONGS_TO_TABLE
  source: column.zs_observe.shiprocket_oms.transaction_type
  target: table.zs_observe.shiprocket_oms
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
    materialized_from: edge.table.zs_observe.shiprocket_oms.has_column.column.zs_observe.shiprocket_oms.transaction_type
```
```yaml
candidate_edge:
  edge_id: edge.table.zs_observe.shiprocket_oms.has_column.column.zs_observe.shiprocket_oms.status
  edge_type: HAS_COLUMN
  source: table.zs_observe.shiprocket_oms
  target: column.zs_observe.shiprocket_oms.status
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
  edge_id: edge.column.zs_observe.shiprocket_oms.status.belongs_to_table.table.zs_observe.shiprocket_oms
  edge_type: BELONGS_TO_TABLE
  source: column.zs_observe.shiprocket_oms.status
  target: table.zs_observe.shiprocket_oms
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
    materialized_from: edge.table.zs_observe.shiprocket_oms.has_column.column.zs_observe.shiprocket_oms.status
```
```yaml
candidate_edge:
  edge_id: edge.table.zs_observe.shiprocket_oms.has_column.column.zs_observe.shiprocket_oms.charged_amount
  edge_type: HAS_COLUMN
  source: table.zs_observe.shiprocket_oms
  target: column.zs_observe.shiprocket_oms.charged_amount
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
  edge_id: edge.column.zs_observe.shiprocket_oms.charged_amount.belongs_to_table.table.zs_observe.shiprocket_oms
  edge_type: BELONGS_TO_TABLE
  source: column.zs_observe.shiprocket_oms.charged_amount
  target: table.zs_observe.shiprocket_oms
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
    materialized_from: edge.table.zs_observe.shiprocket_oms.has_column.column.zs_observe.shiprocket_oms.charged_amount
```
```yaml
candidate_edge:
  edge_id: edge.table.zs_observe.shiprocket_oms.has_column.column.zs_observe.shiprocket_oms.order_total
  edge_type: HAS_COLUMN
  source: table.zs_observe.shiprocket_oms
  target: column.zs_observe.shiprocket_oms.order_total
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
  edge_id: edge.column.zs_observe.shiprocket_oms.order_total.belongs_to_table.table.zs_observe.shiprocket_oms
  edge_type: BELONGS_TO_TABLE
  source: column.zs_observe.shiprocket_oms.order_total
  target: table.zs_observe.shiprocket_oms
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
    materialized_from: edge.table.zs_observe.shiprocket_oms.has_column.column.zs_observe.shiprocket_oms.order_total
```
```yaml
candidate_edge:
  edge_id: edge.table.zs_observe.shiprocket_oms.has_column.column.zs_observe.shiprocket_oms.cod_payble_amount
  edge_type: HAS_COLUMN
  source: table.zs_observe.shiprocket_oms
  target: column.zs_observe.shiprocket_oms.cod_payble_amount
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
  edge_id: edge.column.zs_observe.shiprocket_oms.cod_payble_amount.belongs_to_table.table.zs_observe.shiprocket_oms
  edge_type: BELONGS_TO_TABLE
  source: column.zs_observe.shiprocket_oms.cod_payble_amount
  target: table.zs_observe.shiprocket_oms
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
    materialized_from: edge.table.zs_observe.shiprocket_oms.has_column.column.zs_observe.shiprocket_oms.cod_payble_amount
```
```yaml
candidate_edge:
  edge_id: edge.table.zs_observe.shiprocket_oms.has_column.column.zs_observe.shiprocket_oms.payment_method
  edge_type: HAS_COLUMN
  source: table.zs_observe.shiprocket_oms
  target: column.zs_observe.shiprocket_oms.payment_method
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
  edge_id: edge.column.zs_observe.shiprocket_oms.payment_method.belongs_to_table.table.zs_observe.shiprocket_oms
  edge_type: BELONGS_TO_TABLE
  source: column.zs_observe.shiprocket_oms.payment_method
  target: table.zs_observe.shiprocket_oms
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
    materialized_from: edge.table.zs_observe.shiprocket_oms.has_column.column.zs_observe.shiprocket_oms.payment_method
```
```yaml
candidate_edge:
  edge_id: edge.table.zs_observe.shiprocket_oms.has_column.column.zs_observe.shiprocket_oms.remitted_amount
  edge_type: HAS_COLUMN
  source: table.zs_observe.shiprocket_oms
  target: column.zs_observe.shiprocket_oms.remitted_amount
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
  edge_id: edge.column.zs_observe.shiprocket_oms.remitted_amount.belongs_to_table.table.zs_observe.shiprocket_oms
  edge_type: BELONGS_TO_TABLE
  source: column.zs_observe.shiprocket_oms.remitted_amount
  target: table.zs_observe.shiprocket_oms
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
    materialized_from: edge.table.zs_observe.shiprocket_oms.has_column.column.zs_observe.shiprocket_oms.remitted_amount
```
```yaml
candidate_edge:
  edge_id: edge.table.zs_observe.shiprocket_oms.has_column.column.zs_observe.shiprocket_oms.cod_remittance_date
  edge_type: HAS_COLUMN
  source: table.zs_observe.shiprocket_oms
  target: column.zs_observe.shiprocket_oms.cod_remittance_date
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
  edge_id: edge.column.zs_observe.shiprocket_oms.cod_remittance_date.belongs_to_table.table.zs_observe.shiprocket_oms
  edge_type: BELONGS_TO_TABLE
  source: column.zs_observe.shiprocket_oms.cod_remittance_date
  target: table.zs_observe.shiprocket_oms
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
    materialized_from: edge.table.zs_observe.shiprocket_oms.has_column.column.zs_observe.shiprocket_oms.cod_remittance_date
```
```yaml
candidate_edge:
  edge_id: edge.table.zs_observe.shiprocket_oms.has_column.column.zs_observe.shiprocket_oms.freight_total_amount
  edge_type: HAS_COLUMN
  source: table.zs_observe.shiprocket_oms
  target: column.zs_observe.shiprocket_oms.freight_total_amount
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
  edge_id: edge.column.zs_observe.shiprocket_oms.freight_total_amount.belongs_to_table.table.zs_observe.shiprocket_oms
  edge_type: BELONGS_TO_TABLE
  source: column.zs_observe.shiprocket_oms.freight_total_amount
  target: table.zs_observe.shiprocket_oms
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
    materialized_from: edge.table.zs_observe.shiprocket_oms.has_column.column.zs_observe.shiprocket_oms.freight_total_amount
```
```yaml
candidate_edge:
  edge_id: edge.table.zs_observe.shiprocket_oms.has_column.column.zs_observe.shiprocket_oms.shipping_charges
  edge_type: HAS_COLUMN
  source: table.zs_observe.shiprocket_oms
  target: column.zs_observe.shiprocket_oms.shipping_charges
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
  edge_id: edge.column.zs_observe.shiprocket_oms.shipping_charges.belongs_to_table.table.zs_observe.shiprocket_oms
  edge_type: BELONGS_TO_TABLE
  source: column.zs_observe.shiprocket_oms.shipping_charges
  target: table.zs_observe.shiprocket_oms
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
    materialized_from: edge.table.zs_observe.shiprocket_oms.has_column.column.zs_observe.shiprocket_oms.shipping_charges
```
```yaml
candidate_edge:
  edge_id: edge.table.zs_observe.shiprocket_oms.has_column.column.zs_observe.shiprocket_oms.created_date
  edge_type: HAS_COLUMN
  source: table.zs_observe.shiprocket_oms
  target: column.zs_observe.shiprocket_oms.created_date
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
  edge_id: edge.column.zs_observe.shiprocket_oms.created_date.belongs_to_table.table.zs_observe.shiprocket_oms
  edge_type: BELONGS_TO_TABLE
  source: column.zs_observe.shiprocket_oms.created_date
  target: table.zs_observe.shiprocket_oms
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
    materialized_from: edge.table.zs_observe.shiprocket_oms.has_column.column.zs_observe.shiprocket_oms.created_date
```
```yaml
candidate_edge:
  edge_id: edge.table.zs_observe.shiprocket_oms.has_column.column.zs_observe.shiprocket_oms.awb_assigned_date
  edge_type: HAS_COLUMN
  source: table.zs_observe.shiprocket_oms
  target: column.zs_observe.shiprocket_oms.awb_assigned_date
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
  edge_id: edge.column.zs_observe.shiprocket_oms.awb_assigned_date.belongs_to_table.table.zs_observe.shiprocket_oms
  edge_type: BELONGS_TO_TABLE
  source: column.zs_observe.shiprocket_oms.awb_assigned_date
  target: table.zs_observe.shiprocket_oms
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
    materialized_from: edge.table.zs_observe.shiprocket_oms.has_column.column.zs_observe.shiprocket_oms.awb_assigned_date
```
```yaml
candidate_edge:
  edge_id: edge.table.zs_observe.shiprocket_oms.has_column.column.zs_observe.shiprocket_oms.pickup_scheduled_date
  edge_type: HAS_COLUMN
  source: table.zs_observe.shiprocket_oms
  target: column.zs_observe.shiprocket_oms.pickup_scheduled_date
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
  edge_id: edge.column.zs_observe.shiprocket_oms.pickup_scheduled_date.belongs_to_table.table.zs_observe.shiprocket_oms
  edge_type: BELONGS_TO_TABLE
  source: column.zs_observe.shiprocket_oms.pickup_scheduled_date
  target: table.zs_observe.shiprocket_oms
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
    materialized_from: edge.table.zs_observe.shiprocket_oms.has_column.column.zs_observe.shiprocket_oms.pickup_scheduled_date
```
```yaml
candidate_edge:
  edge_id: edge.table.zs_observe.shiprocket_oms.has_column.column.zs_observe.shiprocket_oms.order_picked_up_date
  edge_type: HAS_COLUMN
  source: table.zs_observe.shiprocket_oms
  target: column.zs_observe.shiprocket_oms.order_picked_up_date
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
  edge_id: edge.column.zs_observe.shiprocket_oms.order_picked_up_date.belongs_to_table.table.zs_observe.shiprocket_oms
  edge_type: BELONGS_TO_TABLE
  source: column.zs_observe.shiprocket_oms.order_picked_up_date
  target: table.zs_observe.shiprocket_oms
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
    materialized_from: edge.table.zs_observe.shiprocket_oms.has_column.column.zs_observe.shiprocket_oms.order_picked_up_date
```
```yaml
candidate_edge:
  edge_id: edge.table.zs_observe.shiprocket_oms.has_column.column.zs_observe.shiprocket_oms.edd
  edge_type: HAS_COLUMN
  source: table.zs_observe.shiprocket_oms
  target: column.zs_observe.shiprocket_oms.edd
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
  edge_id: edge.column.zs_observe.shiprocket_oms.edd.belongs_to_table.table.zs_observe.shiprocket_oms
  edge_type: BELONGS_TO_TABLE
  source: column.zs_observe.shiprocket_oms.edd
  target: table.zs_observe.shiprocket_oms
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
    materialized_from: edge.table.zs_observe.shiprocket_oms.has_column.column.zs_observe.shiprocket_oms.edd
```
```yaml
candidate_edge:
  edge_id: edge.table.zs_observe.shiprocket_oms.has_column.column.zs_observe.shiprocket_oms.order_delivered_date
  edge_type: HAS_COLUMN
  source: table.zs_observe.shiprocket_oms
  target: column.zs_observe.shiprocket_oms.order_delivered_date
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
  edge_id: edge.column.zs_observe.shiprocket_oms.order_delivered_date.belongs_to_table.table.zs_observe.shiprocket_oms
  edge_type: BELONGS_TO_TABLE
  source: column.zs_observe.shiprocket_oms.order_delivered_date
  target: table.zs_observe.shiprocket_oms
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
    materialized_from: edge.table.zs_observe.shiprocket_oms.has_column.column.zs_observe.shiprocket_oms.order_delivered_date
```
```yaml
candidate_edge:
  edge_id: edge.table.zs_observe.shiprocket_oms.has_column.column.zs_observe.shiprocket_oms.rto_initiated_date
  edge_type: HAS_COLUMN
  source: table.zs_observe.shiprocket_oms
  target: column.zs_observe.shiprocket_oms.rto_initiated_date
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
  edge_id: edge.column.zs_observe.shiprocket_oms.rto_initiated_date.belongs_to_table.table.zs_observe.shiprocket_oms
  edge_type: BELONGS_TO_TABLE
  source: column.zs_observe.shiprocket_oms.rto_initiated_date
  target: table.zs_observe.shiprocket_oms
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
    materialized_from: edge.table.zs_observe.shiprocket_oms.has_column.column.zs_observe.shiprocket_oms.rto_initiated_date
```
```yaml
candidate_edge:
  edge_id: edge.table.zs_observe.shiprocket_oms.has_column.column.zs_observe.shiprocket_oms.rto_delivered_date
  edge_type: HAS_COLUMN
  source: table.zs_observe.shiprocket_oms
  target: column.zs_observe.shiprocket_oms.rto_delivered_date
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
  edge_id: edge.column.zs_observe.shiprocket_oms.rto_delivered_date.belongs_to_table.table.zs_observe.shiprocket_oms
  edge_type: BELONGS_TO_TABLE
  source: column.zs_observe.shiprocket_oms.rto_delivered_date
  target: table.zs_observe.shiprocket_oms
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
    materialized_from: edge.table.zs_observe.shiprocket_oms.has_column.column.zs_observe.shiprocket_oms.rto_delivered_date
```
```yaml
candidate_edge:
  edge_id: edge.table.zs_observe.shiprocket_oms.has_column.column.zs_observe.shiprocket_oms.ndr_1_attempt_date
  edge_type: HAS_COLUMN
  source: table.zs_observe.shiprocket_oms
  target: column.zs_observe.shiprocket_oms.ndr_1_attempt_date
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
  edge_id: edge.column.zs_observe.shiprocket_oms.ndr_1_attempt_date.belongs_to_table.table.zs_observe.shiprocket_oms
  edge_type: BELONGS_TO_TABLE
  source: column.zs_observe.shiprocket_oms.ndr_1_attempt_date
  target: table.zs_observe.shiprocket_oms
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
    materialized_from: edge.table.zs_observe.shiprocket_oms.has_column.column.zs_observe.shiprocket_oms.ndr_1_attempt_date
```
```yaml
candidate_edge:
  edge_id: edge.table.zs_observe.shiprocket_oms.has_column.column.zs_observe.shiprocket_oms.ndr_1_remark
  edge_type: HAS_COLUMN
  source: table.zs_observe.shiprocket_oms
  target: column.zs_observe.shiprocket_oms.ndr_1_remark
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
  edge_id: edge.column.zs_observe.shiprocket_oms.ndr_1_remark.belongs_to_table.table.zs_observe.shiprocket_oms
  edge_type: BELONGS_TO_TABLE
  source: column.zs_observe.shiprocket_oms.ndr_1_remark
  target: table.zs_observe.shiprocket_oms
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
    materialized_from: edge.table.zs_observe.shiprocket_oms.has_column.column.zs_observe.shiprocket_oms.ndr_1_remark
```
```yaml
candidate_edge:
  edge_id: edge.table.zs_observe.shiprocket_oms.has_column.column.zs_observe.shiprocket_oms.ndr_2_remark
  edge_type: HAS_COLUMN
  source: table.zs_observe.shiprocket_oms
  target: column.zs_observe.shiprocket_oms.ndr_2_remark
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
  edge_id: edge.column.zs_observe.shiprocket_oms.ndr_2_remark.belongs_to_table.table.zs_observe.shiprocket_oms
  edge_type: BELONGS_TO_TABLE
  source: column.zs_observe.shiprocket_oms.ndr_2_remark
  target: table.zs_observe.shiprocket_oms
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
    materialized_from: edge.table.zs_observe.shiprocket_oms.has_column.column.zs_observe.shiprocket_oms.ndr_2_remark
```
```yaml
candidate_edge:
  edge_id: edge.table.zs_observe.shiprocket_oms.has_column.column.zs_observe.shiprocket_oms.latest_ndr_date
  edge_type: HAS_COLUMN
  source: table.zs_observe.shiprocket_oms
  target: column.zs_observe.shiprocket_oms.latest_ndr_date
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
  edge_id: edge.column.zs_observe.shiprocket_oms.latest_ndr_date.belongs_to_table.table.zs_observe.shiprocket_oms
  edge_type: BELONGS_TO_TABLE
  source: column.zs_observe.shiprocket_oms.latest_ndr_date
  target: table.zs_observe.shiprocket_oms
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
    materialized_from: edge.table.zs_observe.shiprocket_oms.has_column.column.zs_observe.shiprocket_oms.latest_ndr_date
```
```yaml
candidate_edge:
  edge_id: edge.table.zs_observe.shiprocket_oms.has_column.column.zs_observe.shiprocket_oms.latest_ndr_reason
  edge_type: HAS_COLUMN
  source: table.zs_observe.shiprocket_oms
  target: column.zs_observe.shiprocket_oms.latest_ndr_reason
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
  edge_id: edge.column.zs_observe.shiprocket_oms.latest_ndr_reason.belongs_to_table.table.zs_observe.shiprocket_oms
  edge_type: BELONGS_TO_TABLE
  source: column.zs_observe.shiprocket_oms.latest_ndr_reason
  target: table.zs_observe.shiprocket_oms
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
    materialized_from: edge.table.zs_observe.shiprocket_oms.has_column.column.zs_observe.shiprocket_oms.latest_ndr_reason
```
```yaml
candidate_edge:
  edge_id: edge.table.zs_observe.shiprocket_oms.has_column.column.zs_observe.shiprocket_oms.attempt_count
  edge_type: HAS_COLUMN
  source: table.zs_observe.shiprocket_oms
  target: column.zs_observe.shiprocket_oms.attempt_count
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
  edge_id: edge.column.zs_observe.shiprocket_oms.attempt_count.belongs_to_table.table.zs_observe.shiprocket_oms
  edge_type: BELONGS_TO_TABLE
  source: column.zs_observe.shiprocket_oms.attempt_count
  target: table.zs_observe.shiprocket_oms
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
    materialized_from: edge.table.zs_observe.shiprocket_oms.has_column.column.zs_observe.shiprocket_oms.attempt_count
```
```yaml
candidate_edge:
  edge_id: edge.table.zs_observe.shiprocket_oms.has_column.column.zs_observe.shiprocket_oms.rto_reason
  edge_type: HAS_COLUMN
  source: table.zs_observe.shiprocket_oms
  target: column.zs_observe.shiprocket_oms.rto_reason
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
  edge_id: edge.column.zs_observe.shiprocket_oms.rto_reason.belongs_to_table.table.zs_observe.shiprocket_oms
  edge_type: BELONGS_TO_TABLE
  source: column.zs_observe.shiprocket_oms.rto_reason
  target: table.zs_observe.shiprocket_oms
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
    materialized_from: edge.table.zs_observe.shiprocket_oms.has_column.column.zs_observe.shiprocket_oms.rto_reason
```
```yaml
candidate_edge:
  edge_id: edge.table.zs_observe.shiprocket_oms.has_column.column.zs_observe.shiprocket_oms.rto_reason_1
  edge_type: HAS_COLUMN
  source: table.zs_observe.shiprocket_oms
  target: column.zs_observe.shiprocket_oms.rto_reason_1
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
  edge_id: edge.column.zs_observe.shiprocket_oms.rto_reason_1.belongs_to_table.table.zs_observe.shiprocket_oms
  edge_type: BELONGS_TO_TABLE
  source: column.zs_observe.shiprocket_oms.rto_reason_1
  target: table.zs_observe.shiprocket_oms
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
    materialized_from: edge.table.zs_observe.shiprocket_oms.has_column.column.zs_observe.shiprocket_oms.rto_reason_1
```
```yaml
candidate_edge:
  edge_id: edge.table.zs_observe.shiprocket_oms.has_column.column.zs_observe.shiprocket_oms.utr_no
  edge_type: HAS_COLUMN
  source: table.zs_observe.shiprocket_oms
  target: column.zs_observe.shiprocket_oms.utr_no
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
  edge_id: edge.column.zs_observe.shiprocket_oms.utr_no.belongs_to_table.table.zs_observe.shiprocket_oms
  edge_type: BELONGS_TO_TABLE
  source: column.zs_observe.shiprocket_oms.utr_no
  target: table.zs_observe.shiprocket_oms
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
    materialized_from: edge.table.zs_observe.shiprocket_oms.has_column.column.zs_observe.shiprocket_oms.utr_no
```
```yaml
candidate_edge:
  edge_id: edge.table.zs_observe.shiprocket_oms.has_column.column.zs_observe.shiprocket_oms.crf_id
  edge_type: HAS_COLUMN
  source: table.zs_observe.shiprocket_oms
  target: column.zs_observe.shiprocket_oms.crf_id
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
  edge_id: edge.column.zs_observe.shiprocket_oms.crf_id.belongs_to_table.table.zs_observe.shiprocket_oms
  edge_type: BELONGS_TO_TABLE
  source: column.zs_observe.shiprocket_oms.crf_id
  target: table.zs_observe.shiprocket_oms
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
    materialized_from: edge.table.zs_observe.shiprocket_oms.has_column.column.zs_observe.shiprocket_oms.crf_id
```
```yaml
candidate_edge:
  edge_id: edge.table.zs_observe.shiprocket_oms.has_column.column.zs_observe.shiprocket_oms.customer_invoice_id
  edge_type: HAS_COLUMN
  source: table.zs_observe.shiprocket_oms
  target: column.zs_observe.shiprocket_oms.customer_invoice_id
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
  edge_id: edge.column.zs_observe.shiprocket_oms.customer_invoice_id.belongs_to_table.table.zs_observe.shiprocket_oms
  edge_type: BELONGS_TO_TABLE
  source: column.zs_observe.shiprocket_oms.customer_invoice_id
  target: table.zs_observe.shiprocket_oms
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
    materialized_from: edge.table.zs_observe.shiprocket_oms.has_column.column.zs_observe.shiprocket_oms.customer_invoice_id
```
```yaml
candidate_edge:
  edge_id: edge.table.zs_observe.shiprocket_oms.has_column.column.zs_observe.shiprocket_oms.is_active
  edge_type: HAS_COLUMN
  source: table.zs_observe.shiprocket_oms
  target: column.zs_observe.shiprocket_oms.is_active
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
  edge_id: edge.column.zs_observe.shiprocket_oms.is_active.belongs_to_table.table.zs_observe.shiprocket_oms
  edge_type: BELONGS_TO_TABLE
  source: column.zs_observe.shiprocket_oms.is_active
  target: table.zs_observe.shiprocket_oms
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
    materialized_from: edge.table.zs_observe.shiprocket_oms.has_column.column.zs_observe.shiprocket_oms.is_active
```
```yaml
candidate_edge:
  edge_id: edge.table.zs_observe.shiprocket_oms.has_column.column.zs_observe.shiprocket_oms.group_level_id
  edge_type: HAS_COLUMN
  source: table.zs_observe.shiprocket_oms
  target: column.zs_observe.shiprocket_oms.group_level_id
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
  edge_id: edge.column.zs_observe.shiprocket_oms.group_level_id.belongs_to_table.table.zs_observe.shiprocket_oms
  edge_type: BELONGS_TO_TABLE
  source: column.zs_observe.shiprocket_oms.group_level_id
  target: table.zs_observe.shiprocket_oms
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
    materialized_from: edge.table.zs_observe.shiprocket_oms.has_column.column.zs_observe.shiprocket_oms.group_level_id
```
```yaml
candidate_edge:
  edge_id: edge.table.zs_observe.shiprocket_oms.has_relationship.relationship.shiprocket_oms.delhivery_invoice.awb
  edge_type: HAS_RELATIONSHIP
  source: table.zs_observe.shiprocket_oms
  target: relationship.shiprocket_oms.delhivery_invoice.awb
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
  edge_id: edge.relationship.shiprocket_oms.delhivery_invoice.awb.source_table.table.zs_observe.shiprocket_oms
  edge_type: SOURCE_TABLE
  source: relationship.shiprocket_oms.delhivery_invoice.awb
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
  edge_id: edge.table.zs_observe.delhivery_invoice.has_relationship.relationship.shiprocket_oms.delhivery_invoice.awb
  edge_type: HAS_RELATIONSHIP
  source: table.zs_observe.delhivery_invoice
  target: relationship.shiprocket_oms.delhivery_invoice.awb
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
  edge_id: edge.relationship.shiprocket_oms.delhivery_invoice.awb.target_table.table.zs_observe.delhivery_invoice
  edge_type: TARGET_TABLE
  source: relationship.shiprocket_oms.delhivery_invoice.awb
  target: table.zs_observe.delhivery_invoice
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
  edge_id: edge.relationship.shiprocket_oms.delhivery_invoice.awb.uses_source_column.column.zs_observe.shiprocket_oms.awb_code
  edge_type: USES_SOURCE_COLUMN
  source: relationship.shiprocket_oms.delhivery_invoice.awb
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
  edge_id: edge.relationship.shiprocket_oms.delhivery_invoice.awb.uses_target_column.column.zs_observe.delhivery_invoice.forward_awb_number
  edge_type: USES_TARGET_COLUMN
  source: relationship.shiprocket_oms.delhivery_invoice.awb
  target: column.zs_observe.delhivery_invoice.forward_awb_number
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
  edge_id: edge.table.zs_observe.shiprocket_oms.has_relationship.relationship.shiprocket_oms.delhivery_settlement.awb
  edge_type: HAS_RELATIONSHIP
  source: table.zs_observe.shiprocket_oms
  target: relationship.shiprocket_oms.delhivery_settlement.awb
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
  edge_id: edge.relationship.shiprocket_oms.delhivery_settlement.awb.source_table.table.zs_observe.shiprocket_oms
  edge_type: SOURCE_TABLE
  source: relationship.shiprocket_oms.delhivery_settlement.awb
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
  edge_id: edge.table.zs_observe.delhivery_settlement.has_relationship.relationship.shiprocket_oms.delhivery_settlement.awb
  edge_type: HAS_RELATIONSHIP
  source: table.zs_observe.delhivery_settlement
  target: relationship.shiprocket_oms.delhivery_settlement.awb
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
  edge_id: edge.relationship.shiprocket_oms.delhivery_settlement.awb.target_table.table.zs_observe.delhivery_settlement
  edge_type: TARGET_TABLE
  source: relationship.shiprocket_oms.delhivery_settlement.awb
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
  edge_id: edge.relationship.shiprocket_oms.delhivery_settlement.awb.uses_source_column.column.zs_observe.shiprocket_oms.awb_code
  edge_type: USES_SOURCE_COLUMN
  source: relationship.shiprocket_oms.delhivery_settlement.awb
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
  edge_id: edge.relationship.shiprocket_oms.delhivery_settlement.awb.uses_target_column.column.zs_observe.delhivery_settlement.waybill_num
  edge_type: USES_TARGET_COLUMN
  source: relationship.shiprocket_oms.delhivery_settlement.awb
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
  edge_id: edge.table.zs_observe.shiprocket_oms.has_relationship.relationship.shiprocket_oms.dtdc_settlement.awb
  edge_type: HAS_RELATIONSHIP
  source: table.zs_observe.shiprocket_oms
  target: relationship.shiprocket_oms.dtdc_settlement.awb
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
  edge_id: edge.relationship.shiprocket_oms.dtdc_settlement.awb.source_table.table.zs_observe.shiprocket_oms
  edge_type: SOURCE_TABLE
  source: relationship.shiprocket_oms.dtdc_settlement.awb
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
  edge_id: edge.table.zs_observe.dtdc_settlement.has_relationship.relationship.shiprocket_oms.dtdc_settlement.awb
  edge_type: HAS_RELATIONSHIP
  source: table.zs_observe.dtdc_settlement
  target: relationship.shiprocket_oms.dtdc_settlement.awb
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
  edge_id: edge.relationship.shiprocket_oms.dtdc_settlement.awb.target_table.table.zs_observe.dtdc_settlement
  edge_type: TARGET_TABLE
  source: relationship.shiprocket_oms.dtdc_settlement.awb
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
  edge_id: edge.relationship.shiprocket_oms.dtdc_settlement.awb.uses_source_column.column.zs_observe.shiprocket_oms.awb_code
  edge_type: USES_SOURCE_COLUMN
  source: relationship.shiprocket_oms.dtdc_settlement.awb
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
  edge_id: edge.relationship.shiprocket_oms.dtdc_settlement.awb.uses_target_column.column.zs_observe.dtdc_settlement.airwaybill_number
  edge_type: USES_TARGET_COLUMN
  source: relationship.shiprocket_oms.dtdc_settlement.awb
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
  edge_id: edge.table.zs_observe.shiprocket_oms.has_relationship.relationship.shiprocket_oms.ekart_settlement.shipment_id
  edge_type: HAS_RELATIONSHIP
  source: table.zs_observe.shiprocket_oms
  target: relationship.shiprocket_oms.ekart_settlement.shipment_id
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
  edge_id: edge.relationship.shiprocket_oms.ekart_settlement.shipment_id.source_table.table.zs_observe.shiprocket_oms
  edge_type: SOURCE_TABLE
  source: relationship.shiprocket_oms.ekart_settlement.shipment_id
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
  edge_id: edge.table.zs_observe.ekart_settlement.has_relationship.relationship.shiprocket_oms.ekart_settlement.shipment_id
  edge_type: HAS_RELATIONSHIP
  source: table.zs_observe.ekart_settlement
  target: relationship.shiprocket_oms.ekart_settlement.shipment_id
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
  edge_id: edge.relationship.shiprocket_oms.ekart_settlement.shipment_id.target_table.table.zs_observe.ekart_settlement
  edge_type: TARGET_TABLE
  source: relationship.shiprocket_oms.ekart_settlement.shipment_id
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
  edge_id: edge.relationship.shiprocket_oms.ekart_settlement.shipment_id.uses_source_column.column.zs_observe.shiprocket_oms.awb_code
  edge_type: USES_SOURCE_COLUMN
  source: relationship.shiprocket_oms.ekart_settlement.shipment_id
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
  edge_id: edge.relationship.shiprocket_oms.ekart_settlement.shipment_id.uses_target_column.column.zs_observe.ekart_settlement.shipment_id
  edge_type: USES_TARGET_COLUMN
  source: relationship.shiprocket_oms.ekart_settlement.shipment_id
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
  edge_id: edge.table.zs_observe.shiprocket_oms.has_relationship.relationship.shiprocket_oms.ekart_settlement.tracking_id
  edge_type: HAS_RELATIONSHIP
  source: table.zs_observe.shiprocket_oms
  target: relationship.shiprocket_oms.ekart_settlement.tracking_id
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
  edge_id: edge.relationship.shiprocket_oms.ekart_settlement.tracking_id.source_table.table.zs_observe.shiprocket_oms
  edge_type: SOURCE_TABLE
  source: relationship.shiprocket_oms.ekart_settlement.tracking_id
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
  edge_id: edge.table.zs_observe.ekart_settlement.has_relationship.relationship.shiprocket_oms.ekart_settlement.tracking_id
  edge_type: HAS_RELATIONSHIP
  source: table.zs_observe.ekart_settlement
  target: relationship.shiprocket_oms.ekart_settlement.tracking_id
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
  edge_id: edge.relationship.shiprocket_oms.ekart_settlement.tracking_id.target_table.table.zs_observe.ekart_settlement
  edge_type: TARGET_TABLE
  source: relationship.shiprocket_oms.ekart_settlement.tracking_id
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
  edge_id: edge.relationship.shiprocket_oms.ekart_settlement.tracking_id.uses_source_column.column.zs_observe.shiprocket_oms.awb_code
  edge_type: USES_SOURCE_COLUMN
  source: relationship.shiprocket_oms.ekart_settlement.tracking_id
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
  edge_id: edge.relationship.shiprocket_oms.ekart_settlement.tracking_id.uses_target_column.column.zs_observe.ekart_settlement.tracking_id
  edge_type: USES_TARGET_COLUMN
  source: relationship.shiprocket_oms.ekart_settlement.tracking_id
  target: column.zs_observe.ekart_settlement.tracking_id
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
  edge_id: edge.table.zs_observe.shiprocket_oms.has_relationship.relationship.shiprocket_oms.xpressbees_settlement.shipping_id
  edge_type: HAS_RELATIONSHIP
  source: table.zs_observe.shiprocket_oms
  target: relationship.shiprocket_oms.xpressbees_settlement.shipping_id
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
  edge_id: edge.relationship.shiprocket_oms.xpressbees_settlement.shipping_id.source_table.table.zs_observe.shiprocket_oms
  edge_type: SOURCE_TABLE
  source: relationship.shiprocket_oms.xpressbees_settlement.shipping_id
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
  edge_id: edge.table.zs_observe.xpressbees_settlement.has_relationship.relationship.shiprocket_oms.xpressbees_settlement.shipping_id
  edge_type: HAS_RELATIONSHIP
  source: table.zs_observe.xpressbees_settlement
  target: relationship.shiprocket_oms.xpressbees_settlement.shipping_id
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
  edge_id: edge.relationship.shiprocket_oms.xpressbees_settlement.shipping_id.target_table.table.zs_observe.xpressbees_settlement
  edge_type: TARGET_TABLE
  source: relationship.shiprocket_oms.xpressbees_settlement.shipping_id
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
  edge_id: edge.relationship.shiprocket_oms.xpressbees_settlement.shipping_id.uses_source_column.column.zs_observe.shiprocket_oms.awb_code
  edge_type: USES_SOURCE_COLUMN
  source: relationship.shiprocket_oms.xpressbees_settlement.shipping_id
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
  edge_id: edge.relationship.shiprocket_oms.xpressbees_settlement.shipping_id.uses_target_column.column.zs_observe.xpressbees_settlement.shipping_id
  edge_type: USES_TARGET_COLUMN
  source: relationship.shiprocket_oms.xpressbees_settlement.shipping_id
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
  edge_id: edge.table.zs_observe.shiprocket_oms.has_value_profile.value_profile.shiprocket_oms.transaction_type
  edge_type: HAS_VALUE_PROFILE
  source: table.zs_observe.shiprocket_oms
  target: value_profile.shiprocket_oms.transaction_type
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
  edge_id: edge.value_profile.shiprocket_oms.transaction_type.profiles_column.column.zs_observe.shiprocket_oms.transaction_type
  edge_type: PROFILES_COLUMN
  source: value_profile.shiprocket_oms.transaction_type
  target: column.zs_observe.shiprocket_oms.transaction_type
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
  edge_id: edge.column.zs_observe.shiprocket_oms.transaction_type.has_value_profile.value_profile.shiprocket_oms.transaction_type
  edge_type: HAS_VALUE_PROFILE
  source: column.zs_observe.shiprocket_oms.transaction_type
  target: value_profile.shiprocket_oms.transaction_type
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
    materialized_from: edge.value_profile.shiprocket_oms.transaction_type.profiles_column.column.zs_observe.shiprocket_oms.transaction_type
```
```yaml
candidate_edge:
  edge_id: edge.value_profile.shiprocket_oms.transaction_type.profiles_table.table.zs_observe.shiprocket_oms
  edge_type: PROFILES_TABLE
  source: value_profile.shiprocket_oms.transaction_type
  target: table.zs_observe.shiprocket_oms
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
  edge_id: edge.table.zs_observe.shiprocket_oms.has_value_profile.value_profile.shiprocket_oms.status
  edge_type: HAS_VALUE_PROFILE
  source: table.zs_observe.shiprocket_oms
  target: value_profile.shiprocket_oms.status
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
  edge_id: edge.value_profile.shiprocket_oms.status.profiles_column.column.zs_observe.shiprocket_oms.status
  edge_type: PROFILES_COLUMN
  source: value_profile.shiprocket_oms.status
  target: column.zs_observe.shiprocket_oms.status
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
  edge_id: edge.column.zs_observe.shiprocket_oms.status.has_value_profile.value_profile.shiprocket_oms.status
  edge_type: HAS_VALUE_PROFILE
  source: column.zs_observe.shiprocket_oms.status
  target: value_profile.shiprocket_oms.status
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
    materialized_from: edge.value_profile.shiprocket_oms.status.profiles_column.column.zs_observe.shiprocket_oms.status
```
```yaml
candidate_edge:
  edge_id: edge.value_profile.shiprocket_oms.status.profiles_table.table.zs_observe.shiprocket_oms
  edge_type: PROFILES_TABLE
  source: value_profile.shiprocket_oms.status
  target: table.zs_observe.shiprocket_oms
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
  edge_id: edge.table.zs_observe.shiprocket_oms.has_value_profile.value_profile.shiprocket_oms.payment_method
  edge_type: HAS_VALUE_PROFILE
  source: table.zs_observe.shiprocket_oms
  target: value_profile.shiprocket_oms.payment_method
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
  edge_id: edge.value_profile.shiprocket_oms.payment_method.profiles_column.column.zs_observe.shiprocket_oms.payment_method
  edge_type: PROFILES_COLUMN
  source: value_profile.shiprocket_oms.payment_method
  target: column.zs_observe.shiprocket_oms.payment_method
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
  edge_id: edge.column.zs_observe.shiprocket_oms.payment_method.has_value_profile.value_profile.shiprocket_oms.payment_method
  edge_type: HAS_VALUE_PROFILE
  source: column.zs_observe.shiprocket_oms.payment_method
  target: value_profile.shiprocket_oms.payment_method
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
    materialized_from: edge.value_profile.shiprocket_oms.payment_method.profiles_column.column.zs_observe.shiprocket_oms.payment_method
```
```yaml
candidate_edge:
  edge_id: edge.value_profile.shiprocket_oms.payment_method.profiles_table.table.zs_observe.shiprocket_oms
  edge_type: PROFILES_TABLE
  source: value_profile.shiprocket_oms.payment_method
  target: table.zs_observe.shiprocket_oms
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
  edge_id: edge.table.zs_observe.shiprocket_oms.has_value_profile.value_profile.shiprocket_oms.courier_company
  edge_type: HAS_VALUE_PROFILE
  source: table.zs_observe.shiprocket_oms
  target: value_profile.shiprocket_oms.courier_company
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
  edge_id: edge.value_profile.shiprocket_oms.courier_company.profiles_column.column.zs_observe.shiprocket_oms.courier_company
  edge_type: PROFILES_COLUMN
  source: value_profile.shiprocket_oms.courier_company
  target: column.zs_observe.shiprocket_oms.courier_company
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
  edge_id: edge.column.zs_observe.shiprocket_oms.courier_company.has_value_profile.value_profile.shiprocket_oms.courier_company
  edge_type: HAS_VALUE_PROFILE
  source: column.zs_observe.shiprocket_oms.courier_company
  target: value_profile.shiprocket_oms.courier_company
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
    materialized_from: edge.value_profile.shiprocket_oms.courier_company.profiles_column.column.zs_observe.shiprocket_oms.courier_company
```
```yaml
candidate_edge:
  edge_id: edge.value_profile.shiprocket_oms.courier_company.profiles_table.table.zs_observe.shiprocket_oms
  edge_type: PROFILES_TABLE
  source: value_profile.shiprocket_oms.courier_company
  target: table.zs_observe.shiprocket_oms
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
  edge_id: edge.metric.shipment_count.has_implementation.metric_impl.shiprocket_oms.shipment_count
  edge_type: HAS_IMPLEMENTATION
  source: metric.shipment_count
  target: metric_impl.shiprocket_oms.shipment_count
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
  edge_id: edge.metric_impl.shiprocket_oms.shipment_count.implements_metric.metric.shipment_count
  edge_type: IMPLEMENTS_METRIC
  source: metric_impl.shiprocket_oms.shipment_count
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
    materialized_from: edge.metric.shipment_count.has_implementation.metric_impl.shiprocket_oms.shipment_count
```
```yaml
candidate_edge:
  edge_id: edge.metric_impl.shiprocket_oms.shipment_count.uses_table.table.zs_observe.shiprocket_oms
  edge_type: USES_TABLE
  source: metric_impl.shiprocket_oms.shipment_count
  target: table.zs_observe.shiprocket_oms
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
  edge_id: edge.metric_impl.shiprocket_oms.shipment_count.uses_column.column.zs_observe.shiprocket_oms.awb_code.8737448c
  edge_type: USES_COLUMN
  source: metric_impl.shiprocket_oms.shipment_count
  target: column.zs_observe.shiprocket_oms.awb_code
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
  edge_id: edge.metric_impl.shiprocket_oms.shipment_count.uses_formula_template.formula_template.logistics.filtered_count
  edge_type: USES_FORMULA_TEMPLATE
  source: metric_impl.shiprocket_oms.shipment_count
  target: formula_template.logistics.filtered_count
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
  edge_id: edge.metric.unique_awb_count.has_implementation.metric_impl.shiprocket_oms.unique_awb_count
  edge_type: HAS_IMPLEMENTATION
  source: metric.unique_awb_count
  target: metric_impl.shiprocket_oms.unique_awb_count
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
  edge_id: edge.metric_impl.shiprocket_oms.unique_awb_count.implements_metric.metric.unique_awb_count
  edge_type: IMPLEMENTS_METRIC
  source: metric_impl.shiprocket_oms.unique_awb_count
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
    materialized_from: edge.metric.unique_awb_count.has_implementation.metric_impl.shiprocket_oms.unique_awb_count
```
```yaml
candidate_edge:
  edge_id: edge.metric_impl.shiprocket_oms.unique_awb_count.uses_table.table.zs_observe.shiprocket_oms
  edge_type: USES_TABLE
  source: metric_impl.shiprocket_oms.unique_awb_count
  target: table.zs_observe.shiprocket_oms
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
  edge_id: edge.metric_impl.shiprocket_oms.unique_awb_count.uses_column.column.zs_observe.shiprocket_oms.awb_code.8737448c
  edge_type: USES_COLUMN
  source: metric_impl.shiprocket_oms.unique_awb_count
  target: column.zs_observe.shiprocket_oms.awb_code
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
  edge_id: edge.metric_impl.shiprocket_oms.unique_awb_count.uses_formula_template.formula_template.logistics.filtered_count
  edge_type: USES_FORMULA_TEMPLATE
  source: metric_impl.shiprocket_oms.unique_awb_count
  target: formula_template.logistics.filtered_count
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
  edge_id: edge.metric.forward_shipment_count.has_implementation.metric_impl.shiprocket_oms.forward_shipment_count
  edge_type: HAS_IMPLEMENTATION
  source: metric.forward_shipment_count
  target: metric_impl.shiprocket_oms.forward_shipment_count
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
  edge_id: edge.metric_impl.shiprocket_oms.forward_shipment_count.implements_metric.metric.forward_shipment_count
  edge_type: IMPLEMENTS_METRIC
  source: metric_impl.shiprocket_oms.forward_shipment_count
  target: metric.forward_shipment_count
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
    materialized_from: edge.metric.forward_shipment_count.has_implementation.metric_impl.shiprocket_oms.forward_shipment_count
```
```yaml
candidate_edge:
  edge_id: edge.metric_impl.shiprocket_oms.forward_shipment_count.uses_table.table.zs_observe.shiprocket_oms
  edge_type: USES_TABLE
  source: metric_impl.shiprocket_oms.forward_shipment_count
  target: table.zs_observe.shiprocket_oms
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
  edge_id: edge.metric_impl.shiprocket_oms.forward_shipment_count.uses_column.column.zs_observe.shiprocket_oms.transaction_type.28a8df7f
  edge_type: USES_COLUMN
  source: metric_impl.shiprocket_oms.forward_shipment_count
  target: column.zs_observe.shiprocket_oms.transaction_type
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
  edge_id: edge.metric_impl.shiprocket_oms.forward_shipment_count.uses_formula_template.formula_template.logistics.filtered_count
  edge_type: USES_FORMULA_TEMPLATE
  source: metric_impl.shiprocket_oms.forward_shipment_count
  target: formula_template.logistics.filtered_count
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
  edge_id: edge.metric.delivered_shipment_count.has_implementation.metric_impl.shiprocket_oms.delivered_shipment_count
  edge_type: HAS_IMPLEMENTATION
  source: metric.delivered_shipment_count
  target: metric_impl.shiprocket_oms.delivered_shipment_count
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
  edge_id: edge.metric_impl.shiprocket_oms.delivered_shipment_count.implements_metric.metric.delivered_shipment_count
  edge_type: IMPLEMENTS_METRIC
  source: metric_impl.shiprocket_oms.delivered_shipment_count
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
    materialized_from: edge.metric.delivered_shipment_count.has_implementation.metric_impl.shiprocket_oms.delivered_shipment_count
```
```yaml
candidate_edge:
  edge_id: edge.metric_impl.shiprocket_oms.delivered_shipment_count.uses_table.table.zs_observe.shiprocket_oms
  edge_type: USES_TABLE
  source: metric_impl.shiprocket_oms.delivered_shipment_count
  target: table.zs_observe.shiprocket_oms
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
  edge_id: edge.metric_impl.shiprocket_oms.delivered_shipment_count.uses_column.column.zs_observe.shiprocket_oms.status.28a8df7f
  edge_type: USES_COLUMN
  source: metric_impl.shiprocket_oms.delivered_shipment_count
  target: column.zs_observe.shiprocket_oms.status
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
  edge_id: edge.metric_impl.shiprocket_oms.delivered_shipment_count.uses_formula_template.formula_template.logistics.filtered_count
  edge_type: USES_FORMULA_TEMPLATE
  source: metric_impl.shiprocket_oms.delivered_shipment_count
  target: formula_template.logistics.filtered_count
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
  edge_id: edge.metric.rto_count.has_implementation.metric_impl.shiprocket_oms.rto_count
  edge_type: HAS_IMPLEMENTATION
  source: metric.rto_count
  target: metric_impl.shiprocket_oms.rto_count
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
  edge_id: edge.metric_impl.shiprocket_oms.rto_count.implements_metric.metric.rto_count
  edge_type: IMPLEMENTS_METRIC
  source: metric_impl.shiprocket_oms.rto_count
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
    materialized_from: edge.metric.rto_count.has_implementation.metric_impl.shiprocket_oms.rto_count
```
```yaml
candidate_edge:
  edge_id: edge.metric_impl.shiprocket_oms.rto_count.uses_table.table.zs_observe.shiprocket_oms
  edge_type: USES_TABLE
  source: metric_impl.shiprocket_oms.rto_count
  target: table.zs_observe.shiprocket_oms
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
  edge_id: edge.metric_impl.shiprocket_oms.rto_count.uses_column.column.zs_observe.shiprocket_oms.status.28a8df7f
  edge_type: USES_COLUMN
  source: metric_impl.shiprocket_oms.rto_count
  target: column.zs_observe.shiprocket_oms.status
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
  edge_id: edge.metric_impl.shiprocket_oms.rto_count.uses_formula_template.formula_template.logistics.filtered_count
  edge_type: USES_FORMULA_TEMPLATE
  source: metric_impl.shiprocket_oms.rto_count
  target: formula_template.logistics.filtered_count
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
  edge_id: edge.metric.return_shipment_count.has_implementation.metric_impl.shiprocket_oms.return_shipment_count
  edge_type: HAS_IMPLEMENTATION
  source: metric.return_shipment_count
  target: metric_impl.shiprocket_oms.return_shipment_count
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
  edge_id: edge.metric_impl.shiprocket_oms.return_shipment_count.implements_metric.metric.return_shipment_count
  edge_type: IMPLEMENTS_METRIC
  source: metric_impl.shiprocket_oms.return_shipment_count
  target: metric.return_shipment_count
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
    materialized_from: edge.metric.return_shipment_count.has_implementation.metric_impl.shiprocket_oms.return_shipment_count
```
```yaml
candidate_edge:
  edge_id: edge.metric_impl.shiprocket_oms.return_shipment_count.uses_table.table.zs_observe.shiprocket_oms
  edge_type: USES_TABLE
  source: metric_impl.shiprocket_oms.return_shipment_count
  target: table.zs_observe.shiprocket_oms
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
  edge_id: edge.metric_impl.shiprocket_oms.return_shipment_count.uses_column.column.zs_observe.shiprocket_oms.transaction_type.28a8df7f
  edge_type: USES_COLUMN
  source: metric_impl.shiprocket_oms.return_shipment_count
  target: column.zs_observe.shiprocket_oms.transaction_type
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
  edge_id: edge.metric_impl.shiprocket_oms.return_shipment_count.uses_formula_template.formula_template.logistics.filtered_count
  edge_type: USES_FORMULA_TEMPLATE
  source: metric_impl.shiprocket_oms.return_shipment_count
  target: formula_template.logistics.filtered_count
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
  edge_id: edge.metric.cancelled_shipment_count.has_implementation.metric_impl.shiprocket_oms.cancelled_shipment_count
  edge_type: HAS_IMPLEMENTATION
  source: metric.cancelled_shipment_count
  target: metric_impl.shiprocket_oms.cancelled_shipment_count
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
  edge_id: edge.metric_impl.shiprocket_oms.cancelled_shipment_count.implements_metric.metric.cancelled_shipment_count
  edge_type: IMPLEMENTS_METRIC
  source: metric_impl.shiprocket_oms.cancelled_shipment_count
  target: metric.cancelled_shipment_count
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
    materialized_from: edge.metric.cancelled_shipment_count.has_implementation.metric_impl.shiprocket_oms.cancelled_shipment_count
```
```yaml
candidate_edge:
  edge_id: edge.metric_impl.shiprocket_oms.cancelled_shipment_count.uses_table.table.zs_observe.shiprocket_oms
  edge_type: USES_TABLE
  source: metric_impl.shiprocket_oms.cancelled_shipment_count
  target: table.zs_observe.shiprocket_oms
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
  edge_id: edge.metric_impl.shiprocket_oms.cancelled_shipment_count.uses_column.column.zs_observe.shiprocket_oms.transaction_type.28a8df7f
  edge_type: USES_COLUMN
  source: metric_impl.shiprocket_oms.cancelled_shipment_count
  target: column.zs_observe.shiprocket_oms.transaction_type
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
  edge_id: edge.metric_impl.shiprocket_oms.cancelled_shipment_count.uses_column.column.zs_observe.shiprocket_oms.status.28a8df7f
  edge_type: USES_COLUMN
  source: metric_impl.shiprocket_oms.cancelled_shipment_count
  target: column.zs_observe.shiprocket_oms.status
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
  edge_id: edge.metric_impl.shiprocket_oms.cancelled_shipment_count.uses_formula_template.formula_template.logistics.filtered_count
  edge_type: USES_FORMULA_TEMPLATE
  source: metric_impl.shiprocket_oms.cancelled_shipment_count
  target: formula_template.logistics.filtered_count
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
  edge_id: edge.metric.in_transit_shipment_count.has_implementation.metric_impl.shiprocket_oms.in_transit_shipment_count
  edge_type: HAS_IMPLEMENTATION
  source: metric.in_transit_shipment_count
  target: metric_impl.shiprocket_oms.in_transit_shipment_count
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
  edge_id: edge.metric_impl.shiprocket_oms.in_transit_shipment_count.implements_metric.metric.in_transit_shipment_count
  edge_type: IMPLEMENTS_METRIC
  source: metric_impl.shiprocket_oms.in_transit_shipment_count
  target: metric.in_transit_shipment_count
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
    materialized_from: edge.metric.in_transit_shipment_count.has_implementation.metric_impl.shiprocket_oms.in_transit_shipment_count
```
```yaml
candidate_edge:
  edge_id: edge.metric_impl.shiprocket_oms.in_transit_shipment_count.uses_table.table.zs_observe.shiprocket_oms
  edge_type: USES_TABLE
  source: metric_impl.shiprocket_oms.in_transit_shipment_count
  target: table.zs_observe.shiprocket_oms
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
  edge_id: edge.metric_impl.shiprocket_oms.in_transit_shipment_count.uses_column.column.zs_observe.shiprocket_oms.transaction_type.28a8df7f
  edge_type: USES_COLUMN
  source: metric_impl.shiprocket_oms.in_transit_shipment_count
  target: column.zs_observe.shiprocket_oms.transaction_type
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
  edge_id: edge.metric_impl.shiprocket_oms.in_transit_shipment_count.uses_formula_template.formula_template.logistics.filtered_count
  edge_type: USES_FORMULA_TEMPLATE
  source: metric_impl.shiprocket_oms.in_transit_shipment_count
  target: formula_template.logistics.filtered_count
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
  edge_id: edge.metric.damaged_lost_shipment_count.has_implementation.metric_impl.shiprocket_oms.damaged_lost_shipment_count
  edge_type: HAS_IMPLEMENTATION
  source: metric.damaged_lost_shipment_count
  target: metric_impl.shiprocket_oms.damaged_lost_shipment_count
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
  edge_id: edge.metric_impl.shiprocket_oms.damaged_lost_shipment_count.implements_metric.metric.damaged_lost_shipment_count
  edge_type: IMPLEMENTS_METRIC
  source: metric_impl.shiprocket_oms.damaged_lost_shipment_count
  target: metric.damaged_lost_shipment_count
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
    materialized_from: edge.metric.damaged_lost_shipment_count.has_implementation.metric_impl.shiprocket_oms.damaged_lost_shipment_count
```
```yaml
candidate_edge:
  edge_id: edge.metric_impl.shiprocket_oms.damaged_lost_shipment_count.uses_table.table.zs_observe.shiprocket_oms
  edge_type: USES_TABLE
  source: metric_impl.shiprocket_oms.damaged_lost_shipment_count
  target: table.zs_observe.shiprocket_oms
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
  edge_id: edge.metric_impl.shiprocket_oms.damaged_lost_shipment_count.uses_column.column.zs_observe.shiprocket_oms.transaction_type.28a8df7f
  edge_type: USES_COLUMN
  source: metric_impl.shiprocket_oms.damaged_lost_shipment_count
  target: column.zs_observe.shiprocket_oms.transaction_type
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
  edge_id: edge.metric_impl.shiprocket_oms.damaged_lost_shipment_count.uses_column.column.zs_observe.shiprocket_oms.status.28a8df7f
  edge_type: USES_COLUMN
  source: metric_impl.shiprocket_oms.damaged_lost_shipment_count
  target: column.zs_observe.shiprocket_oms.status
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
  edge_id: edge.metric_impl.shiprocket_oms.damaged_lost_shipment_count.uses_formula_template.formula_template.logistics.filtered_count
  edge_type: USES_FORMULA_TEMPLATE
  source: metric_impl.shiprocket_oms.damaged_lost_shipment_count
  target: formula_template.logistics.filtered_count
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
  edge_id: edge.metric.delivery_success_rate.has_implementation.metric_impl.shiprocket_oms.delivery_success_rate
  edge_type: HAS_IMPLEMENTATION
  source: metric.delivery_success_rate
  target: metric_impl.shiprocket_oms.delivery_success_rate
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
  edge_id: edge.metric_impl.shiprocket_oms.delivery_success_rate.implements_metric.metric.delivery_success_rate
  edge_type: IMPLEMENTS_METRIC
  source: metric_impl.shiprocket_oms.delivery_success_rate
  target: metric.delivery_success_rate
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
    materialized_from: edge.metric.delivery_success_rate.has_implementation.metric_impl.shiprocket_oms.delivery_success_rate
```
```yaml
candidate_edge:
  edge_id: edge.metric_impl.shiprocket_oms.delivery_success_rate.uses_table.table.zs_observe.shiprocket_oms
  edge_type: USES_TABLE
  source: metric_impl.shiprocket_oms.delivery_success_rate
  target: table.zs_observe.shiprocket_oms
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
  edge_id: edge.metric_impl.shiprocket_oms.delivery_success_rate.uses_column.column.zs_observe.shiprocket_oms.status.28a8df7f
  edge_type: USES_COLUMN
  source: metric_impl.shiprocket_oms.delivery_success_rate
  target: column.zs_observe.shiprocket_oms.status
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
  edge_id: edge.metric_impl.shiprocket_oms.delivery_success_rate.uses_column.column.zs_observe.shiprocket_oms.transaction_type.28a8df7f
  edge_type: USES_COLUMN
  source: metric_impl.shiprocket_oms.delivery_success_rate
  target: column.zs_observe.shiprocket_oms.transaction_type
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
  edge_id: edge.metric_impl.shiprocket_oms.delivery_success_rate.uses_formula_template.formula_template.logistics.ratio_rate
  edge_type: USES_FORMULA_TEMPLATE
  source: metric_impl.shiprocket_oms.delivery_success_rate
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
  edge_id: edge.metric.rto_rate.has_implementation.metric_impl.shiprocket_oms.rto_rate
  edge_type: HAS_IMPLEMENTATION
  source: metric.rto_rate
  target: metric_impl.shiprocket_oms.rto_rate
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
  edge_id: edge.metric_impl.shiprocket_oms.rto_rate.implements_metric.metric.rto_rate
  edge_type: IMPLEMENTS_METRIC
  source: metric_impl.shiprocket_oms.rto_rate
  target: metric.rto_rate
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
    materialized_from: edge.metric.rto_rate.has_implementation.metric_impl.shiprocket_oms.rto_rate
```
```yaml
candidate_edge:
  edge_id: edge.metric_impl.shiprocket_oms.rto_rate.uses_table.table.zs_observe.shiprocket_oms
  edge_type: USES_TABLE
  source: metric_impl.shiprocket_oms.rto_rate
  target: table.zs_observe.shiprocket_oms
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
  edge_id: edge.metric_impl.shiprocket_oms.rto_rate.uses_column.column.zs_observe.shiprocket_oms.status.28a8df7f
  edge_type: USES_COLUMN
  source: metric_impl.shiprocket_oms.rto_rate
  target: column.zs_observe.shiprocket_oms.status
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
  edge_id: edge.metric_impl.shiprocket_oms.rto_rate.uses_column.column.zs_observe.shiprocket_oms.transaction_type.28a8df7f
  edge_type: USES_COLUMN
  source: metric_impl.shiprocket_oms.rto_rate
  target: column.zs_observe.shiprocket_oms.transaction_type
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
  edge_id: edge.metric_impl.shiprocket_oms.rto_rate.uses_formula_template.formula_template.logistics.ratio_rate
  edge_type: USES_FORMULA_TEMPLATE
  source: metric_impl.shiprocket_oms.rto_rate
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
  edge_id: edge.metric.declared_product_value.has_implementation.metric_impl.shiprocket_oms.declared_product_value
  edge_type: HAS_IMPLEMENTATION
  source: metric.declared_product_value
  target: metric_impl.shiprocket_oms.declared_product_value
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
  edge_id: edge.metric_impl.shiprocket_oms.declared_product_value.implements_metric.metric.declared_product_value
  edge_type: IMPLEMENTS_METRIC
  source: metric_impl.shiprocket_oms.declared_product_value
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
    materialized_from: edge.metric.declared_product_value.has_implementation.metric_impl.shiprocket_oms.declared_product_value
```
```yaml
candidate_edge:
  edge_id: edge.metric_impl.shiprocket_oms.declared_product_value.uses_table.table.zs_observe.shiprocket_oms
  edge_type: USES_TABLE
  source: metric_impl.shiprocket_oms.declared_product_value
  target: table.zs_observe.shiprocket_oms
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
  edge_id: edge.metric_impl.shiprocket_oms.declared_product_value.uses_column.column.zs_observe.shiprocket_oms.charged_amount.8737448c
  edge_type: USES_COLUMN
  source: metric_impl.shiprocket_oms.declared_product_value
  target: column.zs_observe.shiprocket_oms.charged_amount
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
  edge_id: edge.metric_impl.shiprocket_oms.declared_product_value.uses_formula_template.formula_template.logistics.filtered_count
  edge_type: USES_FORMULA_TEMPLATE
  source: metric_impl.shiprocket_oms.declared_product_value
  target: formula_template.logistics.filtered_count
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
  edge_id: edge.metric.order_total_amount.has_implementation.metric_impl.shiprocket_oms.order_total_amount
  edge_type: HAS_IMPLEMENTATION
  source: metric.order_total_amount
  target: metric_impl.shiprocket_oms.order_total_amount
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
  edge_id: edge.metric_impl.shiprocket_oms.order_total_amount.implements_metric.metric.order_total_amount
  edge_type: IMPLEMENTS_METRIC
  source: metric_impl.shiprocket_oms.order_total_amount
  target: metric.order_total_amount
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
    materialized_from: edge.metric.order_total_amount.has_implementation.metric_impl.shiprocket_oms.order_total_amount
```
```yaml
candidate_edge:
  edge_id: edge.metric_impl.shiprocket_oms.order_total_amount.uses_table.table.zs_observe.shiprocket_oms
  edge_type: USES_TABLE
  source: metric_impl.shiprocket_oms.order_total_amount
  target: table.zs_observe.shiprocket_oms
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
  edge_id: edge.metric_impl.shiprocket_oms.order_total_amount.uses_column.column.zs_observe.shiprocket_oms.order_total.340e855f
  edge_type: USES_COLUMN
  source: metric_impl.shiprocket_oms.order_total_amount
  target: column.zs_observe.shiprocket_oms.order_total
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
  edge_id: edge.metric_impl.shiprocket_oms.order_total_amount.uses_formula_template.formula_template.logistics.filtered_count
  edge_type: USES_FORMULA_TEMPLATE
  source: metric_impl.shiprocket_oms.order_total_amount
  target: formula_template.logistics.filtered_count
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
  edge_id: edge.metric.cod_expected_amount.has_implementation.metric_impl.shiprocket_oms.cod_expected_amount
  edge_type: HAS_IMPLEMENTATION
  source: metric.cod_expected_amount
  target: metric_impl.shiprocket_oms.cod_expected_amount
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
  edge_id: edge.metric_impl.shiprocket_oms.cod_expected_amount.implements_metric.metric.cod_expected_amount
  edge_type: IMPLEMENTS_METRIC
  source: metric_impl.shiprocket_oms.cod_expected_amount
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
    materialized_from: edge.metric.cod_expected_amount.has_implementation.metric_impl.shiprocket_oms.cod_expected_amount
```
```yaml
candidate_edge:
  edge_id: edge.metric_impl.shiprocket_oms.cod_expected_amount.uses_table.table.zs_observe.shiprocket_oms
  edge_type: USES_TABLE
  source: metric_impl.shiprocket_oms.cod_expected_amount
  target: table.zs_observe.shiprocket_oms
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
  edge_id: edge.metric_impl.shiprocket_oms.cod_expected_amount.uses_column.column.zs_observe.shiprocket_oms.cod_payble_amount.8737448c
  edge_type: USES_COLUMN
  source: metric_impl.shiprocket_oms.cod_expected_amount
  target: column.zs_observe.shiprocket_oms.cod_payble_amount
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
  edge_id: edge.metric_impl.shiprocket_oms.cod_expected_amount.uses_formula_template.formula_template.logistics.filtered_count
  edge_type: USES_FORMULA_TEMPLATE
  source: metric_impl.shiprocket_oms.cod_expected_amount
  target: formula_template.logistics.filtered_count
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
  edge_id: edge.metric.cod_remitted_amount.has_implementation.metric_impl.shiprocket_oms.cod_remitted_amount
  edge_type: HAS_IMPLEMENTATION
  source: metric.cod_remitted_amount
  target: metric_impl.shiprocket_oms.cod_remitted_amount
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
  edge_id: edge.metric_impl.shiprocket_oms.cod_remitted_amount.implements_metric.metric.cod_remitted_amount
  edge_type: IMPLEMENTS_METRIC
  source: metric_impl.shiprocket_oms.cod_remitted_amount
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
    materialized_from: edge.metric.cod_remitted_amount.has_implementation.metric_impl.shiprocket_oms.cod_remitted_amount
```
```yaml
candidate_edge:
  edge_id: edge.metric_impl.shiprocket_oms.cod_remitted_amount.uses_table.table.zs_observe.shiprocket_oms
  edge_type: USES_TABLE
  source: metric_impl.shiprocket_oms.cod_remitted_amount
  target: table.zs_observe.shiprocket_oms
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
  edge_id: edge.metric_impl.shiprocket_oms.cod_remitted_amount.uses_column.column.zs_observe.shiprocket_oms.remitted_amount.8737448c
  edge_type: USES_COLUMN
  source: metric_impl.shiprocket_oms.cod_remitted_amount
  target: column.zs_observe.shiprocket_oms.remitted_amount
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
  edge_id: edge.metric_impl.shiprocket_oms.cod_remitted_amount.uses_formula_template.formula_template.logistics.filtered_count
  edge_type: USES_FORMULA_TEMPLATE
  source: metric_impl.shiprocket_oms.cod_remitted_amount
  target: formula_template.logistics.filtered_count
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
  edge_id: edge.metric.cod_remittance_lag_days.has_implementation.metric_impl.shiprocket_oms.cod_remittance_lag_days
  edge_type: HAS_IMPLEMENTATION
  source: metric.cod_remittance_lag_days
  target: metric_impl.shiprocket_oms.cod_remittance_lag_days
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
  edge_id: edge.metric_impl.shiprocket_oms.cod_remittance_lag_days.implements_metric.metric.cod_remittance_lag_days
  edge_type: IMPLEMENTS_METRIC
  source: metric_impl.shiprocket_oms.cod_remittance_lag_days
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
    materialized_from: edge.metric.cod_remittance_lag_days.has_implementation.metric_impl.shiprocket_oms.cod_remittance_lag_days
```
```yaml
candidate_edge:
  edge_id: edge.metric_impl.shiprocket_oms.cod_remittance_lag_days.uses_table.table.zs_observe.shiprocket_oms
  edge_type: USES_TABLE
  source: metric_impl.shiprocket_oms.cod_remittance_lag_days
  target: table.zs_observe.shiprocket_oms
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
  edge_id: edge.metric_impl.shiprocket_oms.cod_remittance_lag_days.uses_column.column.zs_observe.shiprocket_oms.order_delivered_date.c5f42cea
  edge_type: USES_COLUMN
  source: metric_impl.shiprocket_oms.cod_remittance_lag_days
  target: column.zs_observe.shiprocket_oms.order_delivered_date
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
  edge_id: edge.metric_impl.shiprocket_oms.cod_remittance_lag_days.uses_column.column.zs_observe.shiprocket_oms.cod_remittance_date.8737448c
  edge_type: USES_COLUMN
  source: metric_impl.shiprocket_oms.cod_remittance_lag_days
  target: column.zs_observe.shiprocket_oms.cod_remittance_date
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
  edge_id: edge.metric_impl.shiprocket_oms.cod_remittance_lag_days.uses_formula_template.formula_template.logistics.ratio_rate
  edge_type: USES_FORMULA_TEMPLATE
  source: metric_impl.shiprocket_oms.cod_remittance_lag_days
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
  edge_id: edge.metric.shipment_pickup_lag_days.has_implementation.metric_impl.shiprocket_oms.shipment_pickup_lag_days
  edge_type: HAS_IMPLEMENTATION
  source: metric.shipment_pickup_lag_days
  target: metric_impl.shiprocket_oms.shipment_pickup_lag_days
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
  edge_id: edge.metric_impl.shiprocket_oms.shipment_pickup_lag_days.implements_metric.metric.shipment_pickup_lag_days
  edge_type: IMPLEMENTS_METRIC
  source: metric_impl.shiprocket_oms.shipment_pickup_lag_days
  target: metric.shipment_pickup_lag_days
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
    materialized_from: edge.metric.shipment_pickup_lag_days.has_implementation.metric_impl.shiprocket_oms.shipment_pickup_lag_days
```
```yaml
candidate_edge:
  edge_id: edge.metric_impl.shiprocket_oms.shipment_pickup_lag_days.uses_table.table.zs_observe.shiprocket_oms
  edge_type: USES_TABLE
  source: metric_impl.shiprocket_oms.shipment_pickup_lag_days
  target: table.zs_observe.shiprocket_oms
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
  edge_id: edge.metric_impl.shiprocket_oms.shipment_pickup_lag_days.uses_column.column.zs_observe.shiprocket_oms.awb_assigned_date.c5f42cea
  edge_type: USES_COLUMN
  source: metric_impl.shiprocket_oms.shipment_pickup_lag_days
  target: column.zs_observe.shiprocket_oms.awb_assigned_date
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
  edge_id: edge.metric_impl.shiprocket_oms.shipment_pickup_lag_days.uses_column.column.zs_observe.shiprocket_oms.order_picked_up_date.c5f42cea
  edge_type: USES_COLUMN
  source: metric_impl.shiprocket_oms.shipment_pickup_lag_days
  target: column.zs_observe.shiprocket_oms.order_picked_up_date
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
  edge_id: edge.metric_impl.shiprocket_oms.shipment_pickup_lag_days.uses_formula_template.formula_template.logistics.ratio_rate
  edge_type: USES_FORMULA_TEMPLATE
  source: metric_impl.shiprocket_oms.shipment_pickup_lag_days
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
  edge_id: edge.metric.delivery_tat_days.has_implementation.metric_impl.shiprocket_oms.delivery_tat_days
  edge_type: HAS_IMPLEMENTATION
  source: metric.delivery_tat_days
  target: metric_impl.shiprocket_oms.delivery_tat_days
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
  edge_id: edge.metric_impl.shiprocket_oms.delivery_tat_days.implements_metric.metric.delivery_tat_days
  edge_type: IMPLEMENTS_METRIC
  source: metric_impl.shiprocket_oms.delivery_tat_days
  target: metric.delivery_tat_days
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
    materialized_from: edge.metric.delivery_tat_days.has_implementation.metric_impl.shiprocket_oms.delivery_tat_days
```
```yaml
candidate_edge:
  edge_id: edge.metric_impl.shiprocket_oms.delivery_tat_days.uses_table.table.zs_observe.shiprocket_oms
  edge_type: USES_TABLE
  source: metric_impl.shiprocket_oms.delivery_tat_days
  target: table.zs_observe.shiprocket_oms
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
  edge_id: edge.metric_impl.shiprocket_oms.delivery_tat_days.uses_column.column.zs_observe.shiprocket_oms.order_picked_up_date.c5f42cea
  edge_type: USES_COLUMN
  source: metric_impl.shiprocket_oms.delivery_tat_days
  target: column.zs_observe.shiprocket_oms.order_picked_up_date
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
  edge_id: edge.metric_impl.shiprocket_oms.delivery_tat_days.uses_column.column.zs_observe.shiprocket_oms.order_delivered_date.c5f42cea
  edge_type: USES_COLUMN
  source: metric_impl.shiprocket_oms.delivery_tat_days
  target: column.zs_observe.shiprocket_oms.order_delivered_date
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
  edge_id: edge.metric_impl.shiprocket_oms.delivery_tat_days.uses_formula_template.formula_template.logistics.filtered_count
  edge_type: USES_FORMULA_TEMPLATE
  source: metric_impl.shiprocket_oms.delivery_tat_days
  target: formula_template.logistics.filtered_count
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
  edge_id: edge.metric.rto_tat_days.has_implementation.metric_impl.shiprocket_oms.rto_tat_days
  edge_type: HAS_IMPLEMENTATION
  source: metric.rto_tat_days
  target: metric_impl.shiprocket_oms.rto_tat_days
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
  edge_id: edge.metric_impl.shiprocket_oms.rto_tat_days.implements_metric.metric.rto_tat_days
  edge_type: IMPLEMENTS_METRIC
  source: metric_impl.shiprocket_oms.rto_tat_days
  target: metric.rto_tat_days
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
    materialized_from: edge.metric.rto_tat_days.has_implementation.metric_impl.shiprocket_oms.rto_tat_days
```
```yaml
candidate_edge:
  edge_id: edge.metric_impl.shiprocket_oms.rto_tat_days.uses_table.table.zs_observe.shiprocket_oms
  edge_type: USES_TABLE
  source: metric_impl.shiprocket_oms.rto_tat_days
  target: table.zs_observe.shiprocket_oms
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
  edge_id: edge.metric_impl.shiprocket_oms.rto_tat_days.uses_column.column.zs_observe.shiprocket_oms.rto_initiated_date.c5f42cea
  edge_type: USES_COLUMN
  source: metric_impl.shiprocket_oms.rto_tat_days
  target: column.zs_observe.shiprocket_oms.rto_initiated_date
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
  edge_id: edge.metric_impl.shiprocket_oms.rto_tat_days.uses_column.column.zs_observe.shiprocket_oms.rto_delivered_date.c5f42cea
  edge_type: USES_COLUMN
  source: metric_impl.shiprocket_oms.rto_tat_days
  target: column.zs_observe.shiprocket_oms.rto_delivered_date
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
  edge_id: edge.metric_impl.shiprocket_oms.rto_tat_days.uses_formula_template.formula_template.logistics.filtered_count
  edge_type: USES_FORMULA_TEMPLATE
  source: metric_impl.shiprocket_oms.rto_tat_days
  target: formula_template.logistics.filtered_count
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
  edge_id: edge.metric.ndr_attempt_count.has_implementation.metric_impl.shiprocket_oms.ndr_attempt_count
  edge_type: HAS_IMPLEMENTATION
  source: metric.ndr_attempt_count
  target: metric_impl.shiprocket_oms.ndr_attempt_count
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
  edge_id: edge.metric_impl.shiprocket_oms.ndr_attempt_count.implements_metric.metric.ndr_attempt_count
  edge_type: IMPLEMENTS_METRIC
  source: metric_impl.shiprocket_oms.ndr_attempt_count
  target: metric.ndr_attempt_count
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
    materialized_from: edge.metric.ndr_attempt_count.has_implementation.metric_impl.shiprocket_oms.ndr_attempt_count
```
```yaml
candidate_edge:
  edge_id: edge.metric_impl.shiprocket_oms.ndr_attempt_count.uses_table.table.zs_observe.shiprocket_oms
  edge_type: USES_TABLE
  source: metric_impl.shiprocket_oms.ndr_attempt_count
  target: table.zs_observe.shiprocket_oms
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
  edge_id: edge.metric_impl.shiprocket_oms.ndr_attempt_count.uses_column.column.zs_observe.shiprocket_oms.attempt_count.340e855f
  edge_type: USES_COLUMN
  source: metric_impl.shiprocket_oms.ndr_attempt_count
  target: column.zs_observe.shiprocket_oms.attempt_count
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
  edge_id: edge.metric_impl.shiprocket_oms.ndr_attempt_count.uses_formula_template.formula_template.logistics.filtered_count
  edge_type: USES_FORMULA_TEMPLATE
  source: metric_impl.shiprocket_oms.ndr_attempt_count
  target: formula_template.logistics.filtered_count
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
  edge_id: edge.metric.average_delivery_attempts.has_implementation.metric_impl.shiprocket_oms.average_delivery_attempts
  edge_type: HAS_IMPLEMENTATION
  source: metric.average_delivery_attempts
  target: metric_impl.shiprocket_oms.average_delivery_attempts
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
  edge_id: edge.metric_impl.shiprocket_oms.average_delivery_attempts.implements_metric.metric.average_delivery_attempts
  edge_type: IMPLEMENTS_METRIC
  source: metric_impl.shiprocket_oms.average_delivery_attempts
  target: metric.average_delivery_attempts
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
    materialized_from: edge.metric.average_delivery_attempts.has_implementation.metric_impl.shiprocket_oms.average_delivery_attempts
```
```yaml
candidate_edge:
  edge_id: edge.metric_impl.shiprocket_oms.average_delivery_attempts.uses_table.table.zs_observe.shiprocket_oms
  edge_type: USES_TABLE
  source: metric_impl.shiprocket_oms.average_delivery_attempts
  target: table.zs_observe.shiprocket_oms
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
  edge_id: edge.metric_impl.shiprocket_oms.average_delivery_attempts.uses_column.column.zs_observe.shiprocket_oms.attempt_count.340e855f
  edge_type: USES_COLUMN
  source: metric_impl.shiprocket_oms.average_delivery_attempts
  target: column.zs_observe.shiprocket_oms.attempt_count
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
  edge_id: edge.metric_impl.shiprocket_oms.average_delivery_attempts.uses_formula_template.formula_template.logistics.filtered_count
  edge_type: USES_FORMULA_TEMPLATE
  source: metric_impl.shiprocket_oms.average_delivery_attempts
  target: formula_template.logistics.filtered_count
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

## 6. Validation Summary
```yaml
validation_summary:
  document_id: shiprocket_logistics_partner_parser_ready_v6_role_split
  shiprocket_role_split: logistics_partner
  candidate_cards: 96
  candidate_edges: 272
  candidate_cards_by_type:
    column: 41
    metric: 21
    metric_implementation: 21
    platform: 1
    platform_context: 1
    relationship: 6
    table: 1
    value_profile: 4
  candidate_edges_by_type:
    APPLIES_TO_PLATFORM: 1
    BELONGS_TO_DOMAIN: 21
    BELONGS_TO_PLATFORM: 1
    BELONGS_TO_TABLE: 41
    HAS_COLUMN: 41
    HAS_IMPLEMENTATION: 21
    HAS_PLATFORM_CONTEXT: 1
    HAS_RELATIONSHIP: 12
    HAS_VALUE_PROFILE: 8
    IMPLEMENTS_METRIC: 21
    PROFILES_COLUMN: 4
    PROFILES_TABLE: 4
    SOURCED_FROM_PLATFORM: 1
    SOURCE_TABLE: 6
    TARGET_TABLE: 6
    USES_COLUMN: 29
    USES_FORMULA_TEMPLATE: 21
    USES_SOURCE_COLUMN: 6
    USES_TABLE: 21
    USES_TARGET_COLUMN: 6
  forbidden_card_types_present: []
  unknown_edge_types_present: []
  result: pass
```
