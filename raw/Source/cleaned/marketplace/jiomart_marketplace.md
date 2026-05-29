# JioMart Marketplace Clean Markdown — V9 Manifest-Refactored
```yaml
document_metadata:
  document_id: jiomart_marketplace_clean_md_v9_manifest_refactored
  vendor: JioMart
  source_docx: /mnt/data/JioMart Recon KB.docx
  source_md_previous: /mnt/data/jiomart_marketplace_clean_md_v8_unified_edges.md
  cleanup_manifest: /mnt/data/marketplace_cleanup_manifest_consolidated_v2.md
  generated_on: '2026-05-22'
  scope: marketplace_specific_clean_markdown_for_deterministic_parser
  marketplace_only: true
  refactor_policy: source-backed, correctly typed, executable, and connected to the right semantic neighborhood
  forbidden_card_types:
  - tenant
  - group
  - platform_account
  - account_data_binding
  - business_scope_set
  - business_flow_binding
  - logistics_account
  - bank_account
  - payment_gateway_account
  - erp_accounting_mapping
  - statutory_tax_filing
  removed_card_types:
  - state_transition
  - process_variant
  quality_summary:
    candidate_cards: 384
    candidate_edges: 1020
    source_evidence_count: 126
    sql_patterns: 29
    review_items: 5
    open_reviews: 5
    missing_edge_references: 0
    dangling_sql_refs: 0
    missing_evidence_refs: 0
    deleted_card_references: 0
    isolated_cards: 0
    lazy_workflow_steps: 0
    placeholder_metric_formulas: 0
    unsupported_metric_implementations: 0
    process_variants_review_required: 0
    state_transitions_without_state_column: 0
    unresolved_benchmark_reviews_without_reason: 0
    hard_threshold_benchmarks_without_rule: 0
    forbidden_scope_cards_from_scope_ids: 0
    raw_source_sha256: a36b68fa208f6753c02e6f975ad1f3785f89402a939b78b881ff3fec72384ca1
    raw_source_line_count: 1232
```
## 0. Parser Instructions

This V9 refactor applies the consolidated marketplace cleanup manifest to the JioMart marketplace source. It preserves source-backed table schemas, metric SQL, reconciliation logic, rules, caveats, and the raw DOCX capture, while removing or recasting lazy/non-executable cards from the prior V8 source.

Critical rules:

- Treat `group_level_id`, seller/entity/GSTIN values, warehouse/fulfilment/courier/AWB identifiers, payment modes, and scope-like values as columns, filters, caveats, or documented scope identifiers only.
- Use `order_id` as the primary OMS↔settlement and OMS↔returns join key. Do not model `jiomart_shipment` joins to the other three tables; the source states 0% match and a separate group/entity.
- Respect JioMart settlement sign/context semantics: `settled_amount` positive/negative depends on `event`, `transaction_type`, and `accountable_type`.
- Use only SQL-backed metric implementations. Commission/take-rate logic remains a rule/review because the source says explicit commission rows are not visible in settlement.
- RTO, doorstep return, and pre-shipment cancellation are source-backed business processes; fulfilment/payment/geography/seller labels are value profiles or rules, not process variants.
- `state_transition` cards are intentionally omitted; workflow steps retain source-specific status values without creating unsupported state-machine edges.

## 1. Applied Manifest Refactor Decisions


```yaml
refactor_decision:
  source_card_or_pattern: process_variant cards for RTO/Doorstep/Prepaid/COD/fulfilment/geography labels
  action: remove_or_recast
  resolution: |-
    RTO, doorstep, and pre-shipment flows are modeled as standalone business_process cards where source gives a sequence. Fulfilment, payment, GSTIN, and group labels are value profiles or rules, not process variants.
```


```yaml
refactor_decision:
  source_card_or_pattern: generic state_transition cards derived from status labels
  action: omit
  resolution: Workflow steps preserve status values and source flow. state_transition cards are not emitted because source
    does not require a deterministic state-machine edge set for parser use.
```


```yaml
refactor_decision:
  source_card_or_pattern: commission/take-rate metric implementations without commission rows
  action: downgrade_to_rule_and_review
  resolution: Source explicitly says no commission deductions are visible; fee structure remains caveat/rule until executable
    columns exist.
```


```yaml
refactor_decision:
  source_card_or_pattern: jiomart_shipment joins to OMS/settlement/returns
  action: block
  resolution: Source states 0% join coverage and separate group_level_id/entity. Added no-cross-join rule and validation.
```


```yaml
refactor_decision:
  source_card_or_pattern: invoice_number/document_number settlement joins
  action: recast
  resolution: order_id is the primary join key. invoice_number is lower coverage/format-different and document_number mostly
    NULL, so no ready relationship card is emitted for invoice joins.
```


```yaml
refactor_decision:
  source_card_or_pattern: reconciliation metrics mislabeled as metrics
  action: recast
  resolution: OMS-settlement, returns-chain, unreconciled order, and TCS comparisons are reconciliation_profile/query_pattern
    cards with metric outputs only where SQL is executable.
```


```yaml
refactor_decision:
  source_card_or_pattern: lazy workflow steps
  action: replace
  resolution: All workflow steps mention source-specific table, column, transaction_type, event, accountable_type, date, or
    amount semantics.
```


```yaml
refactor_decision:
  source_card_or_pattern: parser reviews for source-stated facts
  action: close_or_recast
  resolution: Documented scope values, no-cross-join caveat, type casts, NULL-event behavior, and TCS anomaly are encoded
    as rules/value profiles rather than open reviews.
```


## 2. Source Evidence Registry


```yaml
source_evidence:
  id: ev.jiomart.marketplace.jiomart_marketplace_business_knowledge_base
  source_section: JioMart Marketplace— Business Knowledge Base
  source_context: marketplace
  source_line_start: 2
  source_line_end: 2
  evidence_type: prose
  supported_semantics:
  - Prose semantics from source section JioMart Marketplace— Business Knowledge Base.
  unsupported_semantics:
  - Do not infer tenant/group/platform-account/bank/statutory-filing/external-logistics cards from this evidence.
  allowed_card_types:
  - platform
  - platform_context
  - domain
  - business_process
  - workflow_step
  - rule
  - value_profile
  forbidden_card_types:
  - tenant
  - group
  - platform_account
  - account_data_binding
  - business_scope_set
  - business_flow_binding
  - bank_account
  - payment_gateway_account
  - statutory_tax_filing
  - logistics_account
  confidence: high
```


```yaml
source_evidence:
  id: ev.jiomart.marketplace.1_jiomart_marketplace_overview
  source_section: 1. JioMart Marketplace Overview
  source_context: marketplace
  source_line_start: 3
  source_line_end: 3
  evidence_type: prose
  supported_semantics:
  - Prose semantics from source section 1. JioMart Marketplace Overview.
  unsupported_semantics:
  - Do not infer tenant/group/platform-account/bank/statutory-filing/external-logistics cards from this evidence.
  allowed_card_types:
  - platform
  - platform_context
  - domain
  - business_process
  - workflow_step
  - rule
  - value_profile
  forbidden_card_types:
  - tenant
  - group
  - platform_account
  - account_data_binding
  - business_scope_set
  - business_flow_binding
  - bank_account
  - payment_gateway_account
  - statutory_tax_filing
  - logistics_account
  confidence: high
```


```yaml
source_evidence:
  id: ev.jiomart.marketplace.1_1_background
  source_section: 1.1 Background
  source_context: marketplace
  source_line_start: 4
  source_line_end: 11
  evidence_type: prose
  supported_semantics:
  - Prose semantics from source section 1.1 Background.
  unsupported_semantics:
  - Do not infer tenant/group/platform-account/bank/statutory-filing/external-logistics cards from this evidence.
  allowed_card_types:
  - platform
  - platform_context
  - domain
  - business_process
  - workflow_step
  - rule
  - value_profile
  forbidden_card_types:
  - tenant
  - group
  - platform_account
  - account_data_binding
  - business_scope_set
  - business_flow_binding
  - bank_account
  - payment_gateway_account
  - statutory_tax_filing
  - logistics_account
  confidence: high
```


```yaml
source_evidence:
  id: ev.jiomart.marketplace.1_2_seller_portal
  source_section: 1.2 Seller Portal
  source_context: marketplace
  source_line_start: 12
  source_line_end: 13
  evidence_type: prose
  supported_semantics:
  - Prose semantics from source section 1.2 Seller Portal.
  unsupported_semantics:
  - Do not infer tenant/group/platform-account/bank/statutory-filing/external-logistics cards from this evidence.
  allowed_card_types:
  - platform
  - platform_context
  - domain
  - business_process
  - workflow_step
  - rule
  - value_profile
  forbidden_card_types:
  - tenant
  - group
  - platform_account
  - account_data_binding
  - business_scope_set
  - business_flow_binding
  - bank_account
  - payment_gateway_account
  - statutory_tax_filing
  - logistics_account
  confidence: high
```


```yaml
source_evidence:
  id: ev.jiomart.marketplace.1_3_seller_entities_in_dataset
  source_section: 1.3 Seller Entities in Dataset
  source_context: marketplace
  source_line_start: 14
  source_line_end: 18
  evidence_type: table
  supported_semantics:
  - Documented source values, observed distributions, benchmark/context tables, or table statistics for 1.3 Seller Entities
    in Dataset.
  unsupported_semantics:
  - Do not infer tenant/group/platform-account/bank/statutory-filing/external-logistics cards from this evidence.
  - Scope, GSTIN, fulfilment, or payment labels remain columns, value profiles, caveats, or rules only.
  allowed_card_types:
  - value_profile
  - column
  - metric
  - rule
  - table
  forbidden_card_types:
  - tenant
  - group
  - platform_account
  - account_data_binding
  - business_scope_set
  - business_flow_binding
  - bank_account
  - payment_gateway_account
  - statutory_tax_filing
  - logistics_account
  - process_variant
  confidence: high
```


```yaml
source_evidence:
  id: ev.jiomart.marketplace.1_4_myfitness_products_primary_seller_group_26
  source_section: 1.4 MYFITNESS Products (Primary Seller — group 26)
  source_context: marketplace
  source_line_start: 19
  source_line_end: 28
  evidence_type: table
  supported_semantics:
  - Documented source values, observed distributions, benchmark/context tables, or table statistics for 1.4 MYFITNESS Products
    (Primary Seller — group 26).
  unsupported_semantics:
  - Do not infer tenant/group/platform-account/bank/statutory-filing/external-logistics cards from this evidence.
  allowed_card_types:
  - value_profile
  - column
  - metric
  - rule
  - table
  forbidden_card_types:
  - tenant
  - group
  - platform_account
  - account_data_binding
  - business_scope_set
  - business_flow_binding
  - bank_account
  - payment_gateway_account
  - statutory_tax_filing
  - logistics_account
  confidence: high
```


```yaml
source_evidence:
  id: ev.jiomart.marketplace.1_5_multi_state_gstin_registration_tanvi_fitness
  source_section: 1.5 Multi-State GSTIN Registration (TANVI Fitness)
  source_context: marketplace
  source_line_start: 29
  source_line_end: 35
  evidence_type: table
  supported_semantics:
  - Documented source values, observed distributions, benchmark/context tables, or table statistics for 1.5 Multi-State GSTIN
    Registration (TANVI Fitness).
  unsupported_semantics:
  - Do not infer tenant/group/platform-account/bank/statutory-filing/external-logistics cards from this evidence.
  - Scope, GSTIN, fulfilment, or payment labels remain columns, value profiles, caveats, or rules only.
  allowed_card_types:
  - value_profile
  - column
  - metric
  - rule
  - table
  forbidden_card_types:
  - tenant
  - group
  - platform_account
  - account_data_binding
  - business_scope_set
  - business_flow_binding
  - bank_account
  - payment_gateway_account
  - statutory_tax_filing
  - logistics_account
  - process_variant
  confidence: high
```


```yaml
source_evidence:
  id: ev.jiomart.marketplace.2_jiomart_business_model_and_fee_structure
  source_section: 2. JioMart Business Model & Fee Structure
  source_context: marketplace
  source_line_start: 36
  source_line_end: 36
  evidence_type: prose
  supported_semantics:
  - Prose semantics from source section 2. JioMart Business Model & Fee Structure.
  unsupported_semantics:
  - Do not infer tenant/group/platform-account/bank/statutory-filing/external-logistics cards from this evidence.
  allowed_card_types:
  - platform
  - platform_context
  - domain
  - business_process
  - workflow_step
  - rule
  - value_profile
  forbidden_card_types:
  - tenant
  - group
  - platform_account
  - account_data_binding
  - business_scope_set
  - business_flow_binding
  - bank_account
  - payment_gateway_account
  - statutory_tax_filing
  - logistics_account
  confidence: high
```


```yaml
source_evidence:
  id: ev.jiomart.marketplace.2_1_jiomart_s_revenue_sources_from_sellers
  source_section: 2.1 JioMart's Revenue Sources from Sellers
  source_context: marketplace
  source_line_start: 37
  source_line_end: 47
  evidence_type: prose
  supported_semantics:
  - Prose semantics from source section 2.1 JioMart's Revenue Sources from Sellers.
  unsupported_semantics:
  - Do not infer tenant/group/platform-account/bank/statutory-filing/external-logistics cards from this evidence.
  allowed_card_types:
  - platform
  - platform_context
  - domain
  - business_process
  - workflow_step
  - rule
  - value_profile
  forbidden_card_types:
  - tenant
  - group
  - platform_account
  - account_data_binding
  - business_scope_set
  - business_flow_binding
  - bank_account
  - payment_gateway_account
  - statutory_tax_filing
  - logistics_account
  confidence: high
```


```yaml
source_evidence:
  id: ev.jiomart.marketplace.2_2_fulfilment_models
  source_section: 2.2 Fulfilment Models
  source_context: marketplace
  source_line_start: 48
  source_line_end: 52
  evidence_type: prose
  supported_semantics:
  - Prose semantics from source section 2.2 Fulfilment Models.
  unsupported_semantics:
  - Do not infer tenant/group/platform-account/bank/statutory-filing/external-logistics cards from this evidence.
  - Scope, GSTIN, fulfilment, or payment labels remain columns, value profiles, caveats, or rules only.
  allowed_card_types:
  - platform
  - platform_context
  - domain
  - business_process
  - workflow_step
  - rule
  - value_profile
  forbidden_card_types:
  - tenant
  - group
  - platform_account
  - account_data_binding
  - business_scope_set
  - business_flow_binding
  - bank_account
  - payment_gateway_account
  - statutory_tax_filing
  - logistics_account
  - process_variant
  confidence: high
```


```yaml
source_evidence:
  id: ev.jiomart.marketplace.2_3_payment_settlement_cycle
  source_section: 2.3 Payment Settlement Cycle
  source_context: marketplace
  source_line_start: 53
  source_line_end: 56
  evidence_type: prose
  supported_semantics:
  - Prose semantics from source section 2.3 Payment Settlement Cycle.
  unsupported_semantics:
  - Do not infer tenant/group/platform-account/bank/statutory-filing/external-logistics cards from this evidence.
  - Scope, GSTIN, fulfilment, or payment labels remain columns, value profiles, caveats, or rules only.
  allowed_card_types:
  - platform
  - platform_context
  - domain
  - business_process
  - workflow_step
  - rule
  - value_profile
  forbidden_card_types:
  - tenant
  - group
  - platform_account
  - account_data_binding
  - business_scope_set
  - business_flow_binding
  - bank_account
  - payment_gateway_account
  - statutory_tax_filing
  - logistics_account
  - process_variant
  confidence: high
```


```yaml
source_evidence:
  id: ev.jiomart.marketplace.3_transaction_lifecycle
  source_section: 3. Transaction Lifecycle
  source_context: marketplace
  source_line_start: 57
  source_line_end: 57
  evidence_type: prose
  supported_semantics:
  - Prose semantics from source section 3. Transaction Lifecycle.
  unsupported_semantics:
  - Do not infer tenant/group/platform-account/bank/statutory-filing/external-logistics cards from this evidence.
  - Do not create process variants unless a materially different source-backed sequence or matching logic exists.
  allowed_card_types:
  - platform
  - platform_context
  - domain
  - business_process
  - workflow_step
  - rule
  - value_profile
  forbidden_card_types:
  - tenant
  - group
  - platform_account
  - account_data_binding
  - business_scope_set
  - business_flow_binding
  - bank_account
  - payment_gateway_account
  - statutory_tax_filing
  - logistics_account
  confidence: high
```


```yaml
source_evidence:
  id: ev.jiomart.marketplace.3_1_forward_order_flow
  source_section: 3.1 Forward Order Flow
  source_context: marketplace
  source_line_start: 58
  source_line_end: 80
  evidence_type: prose
  supported_semantics:
  - Prose semantics from source section 3.1 Forward Order Flow.
  unsupported_semantics:
  - Do not infer tenant/group/platform-account/bank/statutory-filing/external-logistics cards from this evidence.
  - Do not create process variants unless a materially different source-backed sequence or matching logic exists.
  allowed_card_types:
  - platform
  - platform_context
  - domain
  - business_process
  - workflow_step
  - rule
  - value_profile
  forbidden_card_types:
  - tenant
  - group
  - platform_account
  - account_data_binding
  - business_scope_set
  - business_flow_binding
  - bank_account
  - payment_gateway_account
  - statutory_tax_filing
  - logistics_account
  confidence: high
```


```yaml
source_evidence:
  id: ev.jiomart.marketplace.3_2_rto_return_to_origin_flow
  source_section: 3.2 RTO (Return-to-Origin) Flow
  source_context: marketplace
  source_line_start: 81
  source_line_end: 97
  evidence_type: prose
  supported_semantics:
  - Prose semantics from source section 3.2 RTO (Return-to-Origin) Flow.
  unsupported_semantics:
  - Do not infer tenant/group/platform-account/bank/statutory-filing/external-logistics cards from this evidence.
  - Do not create process variants unless a materially different source-backed sequence or matching logic exists.
  allowed_card_types:
  - platform
  - platform_context
  - domain
  - business_process
  - workflow_step
  - rule
  - value_profile
  forbidden_card_types:
  - tenant
  - group
  - platform_account
  - account_data_binding
  - business_scope_set
  - business_flow_binding
  - bank_account
  - payment_gateway_account
  - statutory_tax_filing
  - logistics_account
  confidence: high
```


```yaml
source_evidence:
  id: ev.jiomart.marketplace.3_3_doorstep_return_flow
  source_section: 3.3 Doorstep Return Flow
  source_context: marketplace
  source_line_start: 98
  source_line_end: 109
  evidence_type: prose
  supported_semantics:
  - Prose semantics from source section 3.3 Doorstep Return Flow.
  unsupported_semantics:
  - Do not infer tenant/group/platform-account/bank/statutory-filing/external-logistics cards from this evidence.
  - Do not create process variants unless a materially different source-backed sequence or matching logic exists.
  allowed_card_types:
  - platform
  - platform_context
  - domain
  - business_process
  - workflow_step
  - rule
  - value_profile
  forbidden_card_types:
  - tenant
  - group
  - platform_account
  - account_data_binding
  - business_scope_set
  - business_flow_binding
  - bank_account
  - payment_gateway_account
  - statutory_tax_filing
  - logistics_account
  confidence: high
```


```yaml
source_evidence:
  id: ev.jiomart.marketplace.3_4_pre_shipment_cancellation_flow
  source_section: 3.4 Pre-Shipment Cancellation Flow
  source_context: marketplace
  source_line_start: 110
  source_line_end: 120
  evidence_type: prose
  supported_semantics:
  - Prose semantics from source section 3.4 Pre-Shipment Cancellation Flow.
  unsupported_semantics:
  - Do not infer tenant/group/platform-account/bank/statutory-filing/external-logistics cards from this evidence.
  - Do not create process variants unless a materially different source-backed sequence or matching logic exists.
  allowed_card_types:
  - platform
  - platform_context
  - domain
  - business_process
  - workflow_step
  - rule
  - value_profile
  forbidden_card_types:
  - tenant
  - group
  - platform_account
  - account_data_binding
  - business_scope_set
  - business_flow_binding
  - bank_account
  - payment_gateway_account
  - statutory_tax_filing
  - logistics_account
  confidence: high
```


```yaml
source_evidence:
  id: ev.jiomart.marketplace.4_entity_relationships_across_tables
  source_section: 4. Entity Relationships Across Tables
  source_context: marketplace
  source_line_start: 121
  source_line_end: 121
  evidence_type: prose
  supported_semantics:
  - Prose semantics from source section 4. Entity Relationships Across Tables.
  unsupported_semantics:
  - Do not infer tenant/group/platform-account/bank/statutory-filing/external-logistics cards from this evidence.
  allowed_card_types:
  - platform
  - platform_context
  - domain
  - business_process
  - workflow_step
  - rule
  - value_profile
  forbidden_card_types:
  - tenant
  - group
  - platform_account
  - account_data_binding
  - business_scope_set
  - business_flow_binding
  - bank_account
  - payment_gateway_account
  - statutory_tax_filing
  - logistics_account
  confidence: high
```


```yaml
source_evidence:
  id: ev.jiomart.marketplace.4_1_entity_map
  source_section: 4.1 Entity Map
  source_context: marketplace
  source_line_start: 122
  source_line_end: 130
  evidence_type: prose
  supported_semantics:
  - Prose semantics from source section 4.1 Entity Map.
  unsupported_semantics:
  - Do not infer tenant/group/platform-account/bank/statutory-filing/external-logistics cards from this evidence.
  allowed_card_types:
  - platform
  - platform_context
  - domain
  - business_process
  - workflow_step
  - rule
  - value_profile
  forbidden_card_types:
  - tenant
  - group
  - platform_account
  - account_data_binding
  - business_scope_set
  - business_flow_binding
  - bank_account
  - payment_gateway_account
  - statutory_tax_filing
  - logistics_account
  confidence: high
```


```yaml
source_evidence:
  id: ev.jiomart.marketplace.4_2_primary_join_keys
  source_section: 4.2 Primary Join Keys
  source_context: marketplace
  source_line_start: 131
  source_line_end: 139
  evidence_type: prose
  supported_semantics:
  - Prose semantics from source section 4.2 Primary Join Keys.
  unsupported_semantics:
  - Do not infer tenant/group/platform-account/bank/statutory-filing/external-logistics cards from this evidence.
  allowed_card_types:
  - platform
  - platform_context
  - domain
  - business_process
  - workflow_step
  - rule
  - value_profile
  forbidden_card_types:
  - tenant
  - group
  - platform_account
  - account_data_binding
  - business_scope_set
  - business_flow_binding
  - bank_account
  - payment_gateway_account
  - statutory_tax_filing
  - logistics_account
  confidence: high
```


```yaml
source_evidence:
  id: ev.jiomart.marketplace.5_gst_tax_framework
  source_section: 5. GST / Tax Framework
  source_context: marketplace
  source_line_start: 140
  source_line_end: 140
  evidence_type: prose
  supported_semantics:
  - Prose semantics from source section 5. GST / Tax Framework.
  unsupported_semantics:
  - Do not infer tenant/group/platform-account/bank/statutory-filing/external-logistics cards from this evidence.
  allowed_card_types:
  - platform
  - platform_context
  - domain
  - business_process
  - workflow_step
  - rule
  - value_profile
  forbidden_card_types:
  - tenant
  - group
  - platform_account
  - account_data_binding
  - business_scope_set
  - business_flow_binding
  - bank_account
  - payment_gateway_account
  - statutory_tax_filing
  - logistics_account
  confidence: high
```


```yaml
source_evidence:
  id: ev.jiomart.marketplace.5_1_product_gst_on_sales
  source_section: 5.1 Product GST on Sales
  source_context: marketplace
  source_line_start: 141
  source_line_end: 148
  evidence_type: prose
  supported_semantics:
  - Prose semantics from source section 5.1 Product GST on Sales.
  unsupported_semantics:
  - Do not infer tenant/group/platform-account/bank/statutory-filing/external-logistics cards from this evidence.
  allowed_card_types:
  - platform
  - platform_context
  - domain
  - business_process
  - workflow_step
  - rule
  - value_profile
  forbidden_card_types:
  - tenant
  - group
  - platform_account
  - account_data_binding
  - business_scope_set
  - business_flow_binding
  - bank_account
  - payment_gateway_account
  - statutory_tax_filing
  - logistics_account
  confidence: high
```


```yaml
source_evidence:
  id: ev.jiomart.marketplace.5_2_hsn_and_gst_rates
  source_section: 5.2 HSN and GST Rates
  source_context: marketplace
  source_line_start: 149
  source_line_end: 155
  evidence_type: table
  supported_semantics:
  - Documented source values, observed distributions, benchmark/context tables, or table statistics for 5.2 HSN and GST Rates.
  unsupported_semantics:
  - Do not infer tenant/group/platform-account/bank/statutory-filing/external-logistics cards from this evidence.
  allowed_card_types:
  - value_profile
  - column
  - metric
  - rule
  - table
  forbidden_card_types:
  - tenant
  - group
  - platform_account
  - account_data_binding
  - business_scope_set
  - business_flow_binding
  - bank_account
  - payment_gateway_account
  - statutory_tax_filing
  - logistics_account
  confidence: high
```


```yaml
source_evidence:
  id: ev.jiomart.marketplace.5_3_tcs_tax_collected_at_source_gst_52
  source_section: 5.3 TCS (Tax Collected at Source — GST § 52)
  source_context: marketplace
  source_line_start: 156
  source_line_end: 161
  evidence_type: prose
  supported_semantics:
  - Prose semantics from source section 5.3 TCS (Tax Collected at Source — GST § 52).
  unsupported_semantics:
  - Do not infer tenant/group/platform-account/bank/statutory-filing/external-logistics cards from this evidence.
  allowed_card_types:
  - platform
  - platform_context
  - domain
  - business_process
  - workflow_step
  - rule
  - value_profile
  forbidden_card_types:
  - tenant
  - group
  - platform_account
  - account_data_binding
  - business_scope_set
  - business_flow_binding
  - bank_account
  - payment_gateway_account
  - statutory_tax_filing
  - logistics_account
  confidence: high
```


```yaml
source_evidence:
  id: ev.jiomart.marketplace.5_4_tds_tax_deducted_at_source_income_tax_194_o
  source_section: 5.4 TDS (Tax Deducted at Source — Income Tax § 194-O)
  source_context: marketplace
  source_line_start: 162
  source_line_end: 169
  evidence_type: prose
  supported_semantics:
  - Prose semantics from source section 5.4 TDS (Tax Deducted at Source — Income Tax § 194-O).
  unsupported_semantics:
  - Do not infer tenant/group/platform-account/bank/statutory-filing/external-logistics cards from this evidence.
  allowed_card_types:
  - platform
  - platform_context
  - domain
  - business_process
  - workflow_step
  - rule
  - value_profile
  forbidden_card_types:
  - tenant
  - group
  - platform_account
  - account_data_binding
  - business_scope_set
  - business_flow_binding
  - bank_account
  - payment_gateway_account
  - statutory_tax_filing
  - logistics_account
  confidence: high
```


```yaml
source_evidence:
  id: ev.jiomart.marketplace.6_key_business_metrics_with_sql
  source_section: 6. Key Business Metrics (with SQL)
  source_context: marketplace
  source_line_start: 170
  source_line_end: 170
  evidence_type: query_example
  supported_semantics:
  - Executable/source-backed SQL query pattern for 6. Key Business Metrics (with SQL), including columns, filters, aggregation
    grain, and output aliases.
  unsupported_semantics:
  - Do not infer tenant/group/platform-account/bank/statutory-filing/external-logistics cards from this evidence.
  - Do not create metric implementations unless the SQL references documented tables/columns and required filters.
  allowed_card_types:
  - metric
  - metric_implementation
  - query_pattern
  - output_contract
  - validation_test
  - rule
  forbidden_card_types:
  - tenant
  - group
  - platform_account
  - account_data_binding
  - business_scope_set
  - business_flow_binding
  - bank_account
  - payment_gateway_account
  - statutory_tax_filing
  - logistics_account
  - non_executable_metric_implementation
  confidence: high
```


```yaml
source_evidence:
  id: ev.jiomart.marketplace.6_1_total_gmv
  source_section: 6.1 Total GMV
  source_context: marketplace
  source_line_start: 171
  source_line_end: 180
  evidence_type: query_example
  supported_semantics:
  - Executable/source-backed SQL query pattern for 6.1 Total GMV, including columns, filters, aggregation grain, and output
    aliases.
  unsupported_semantics:
  - Do not infer tenant/group/platform-account/bank/statutory-filing/external-logistics cards from this evidence.
  - Do not create metric implementations unless the SQL references documented tables/columns and required filters.
  allowed_card_types:
  - metric
  - metric_implementation
  - query_pattern
  - output_contract
  - validation_test
  - rule
  forbidden_card_types:
  - tenant
  - group
  - platform_account
  - account_data_binding
  - business_scope_set
  - business_flow_binding
  - bank_account
  - payment_gateway_account
  - statutory_tax_filing
  - logistics_account
  - non_executable_metric_implementation
  confidence: high
```


```yaml
source_evidence:
  id: ev.jiomart.marketplace.6_2_return_rate
  source_section: 6.2 Return Rate
  source_context: marketplace
  source_line_start: 181
  source_line_end: 191
  evidence_type: query_example
  supported_semantics:
  - Executable/source-backed SQL query pattern for 6.2 Return Rate, including columns, filters, aggregation grain, and output
    aliases.
  unsupported_semantics:
  - Do not infer tenant/group/platform-account/bank/statutory-filing/external-logistics cards from this evidence.
  - Do not create metric implementations unless the SQL references documented tables/columns and required filters.
  allowed_card_types:
  - metric
  - metric_implementation
  - query_pattern
  - output_contract
  - validation_test
  - rule
  forbidden_card_types:
  - tenant
  - group
  - platform_account
  - account_data_binding
  - business_scope_set
  - business_flow_binding
  - bank_account
  - payment_gateway_account
  - statutory_tax_filing
  - logistics_account
  - non_executable_metric_implementation
  confidence: high
```


```yaml
source_evidence:
  id: ev.jiomart.marketplace.6_3_average_order_value_aov
  source_section: 6.3 Average Order Value (AOV)
  source_context: marketplace
  source_line_start: 192
  source_line_end: 200
  evidence_type: query_example
  supported_semantics:
  - Executable/source-backed SQL query pattern for 6.3 Average Order Value (AOV), including columns, filters, aggregation
    grain, and output aliases.
  unsupported_semantics:
  - Do not infer tenant/group/platform-account/bank/statutory-filing/external-logistics cards from this evidence.
  - Do not create metric implementations unless the SQL references documented tables/columns and required filters.
  allowed_card_types:
  - metric
  - metric_implementation
  - query_pattern
  - output_contract
  - validation_test
  - rule
  forbidden_card_types:
  - tenant
  - group
  - platform_account
  - account_data_binding
  - business_scope_set
  - business_flow_binding
  - bank_account
  - payment_gateway_account
  - statutory_tax_filing
  - logistics_account
  - non_executable_metric_implementation
  confidence: high
```


```yaml
source_evidence:
  id: ev.jiomart.marketplace.6_4_net_settled_revenue
  source_section: 6.4 Net Settled Revenue
  source_context: marketplace
  source_line_start: 201
  source_line_end: 210
  evidence_type: query_example
  supported_semantics:
  - Executable/source-backed SQL query pattern for 6.4 Net Settled Revenue, including columns, filters, aggregation grain,
    and output aliases.
  unsupported_semantics:
  - Do not infer tenant/group/platform-account/bank/statutory-filing/external-logistics cards from this evidence.
  - Do not create metric implementations unless the SQL references documented tables/columns and required filters.
  allowed_card_types:
  - metric
  - metric_implementation
  - query_pattern
  - output_contract
  - validation_test
  - rule
  forbidden_card_types:
  - tenant
  - group
  - platform_account
  - account_data_binding
  - business_scope_set
  - business_flow_binding
  - bank_account
  - payment_gateway_account
  - statutory_tax_filing
  - logistics_account
  - non_executable_metric_implementation
  confidence: high
```


```yaml
source_evidence:
  id: ev.jiomart.marketplace.6_5_seller_coupon_discount_impact
  source_section: 6.5 Seller Coupon Discount Impact
  source_context: marketplace
  source_line_start: 211
  source_line_end: 222
  evidence_type: query_example
  supported_semantics:
  - Executable/source-backed SQL query pattern for 6.5 Seller Coupon Discount Impact, including columns, filters, aggregation
    grain, and output aliases.
  unsupported_semantics:
  - Do not infer tenant/group/platform-account/bank/statutory-filing/external-logistics cards from this evidence.
  - Do not create metric implementations unless the SQL references documented tables/columns and required filters.
  allowed_card_types:
  - metric
  - metric_implementation
  - query_pattern
  - output_contract
  - validation_test
  - rule
  forbidden_card_types:
  - tenant
  - group
  - platform_account
  - account_data_binding
  - business_scope_set
  - business_flow_binding
  - bank_account
  - payment_gateway_account
  - statutory_tax_filing
  - logistics_account
  - non_executable_metric_implementation
  confidence: high
```


```yaml
source_evidence:
  id: ev.jiomart.marketplace.6_6_monthly_forward_orders_and_gmv
  source_section: 6.6 Monthly Forward Orders and GMV
  source_context: marketplace
  source_line_start: 223
  source_line_end: 234
  evidence_type: query_example
  supported_semantics:
  - Executable/source-backed SQL query pattern for 6.6 Monthly Forward Orders and GMV, including columns, filters, aggregation
    grain, and output aliases.
  unsupported_semantics:
  - Do not infer tenant/group/platform-account/bank/statutory-filing/external-logistics cards from this evidence.
  - Do not create metric implementations unless the SQL references documented tables/columns and required filters.
  allowed_card_types:
  - metric
  - metric_implementation
  - query_pattern
  - output_contract
  - validation_test
  - rule
  forbidden_card_types:
  - tenant
  - group
  - platform_account
  - account_data_binding
  - business_scope_set
  - business_flow_binding
  - bank_account
  - payment_gateway_account
  - statutory_tax_filing
  - logistics_account
  - non_executable_metric_implementation
  confidence: high
```


```yaml
source_evidence:
  id: ev.jiomart.marketplace.7_reconciliation_use_cases
  source_section: 7. Reconciliation Use Cases
  source_context: marketplace
  source_line_start: 235
  source_line_end: 235
  evidence_type: reconciliation_playbook
  supported_semantics:
  - Source-backed JioMart reconciliation logic for 7. Reconciliation Use Cases, including tables, join keys, filters, and
    output fields.
  unsupported_semantics:
  - Do not infer tenant/group/platform-account/bank/statutory-filing/external-logistics cards from this evidence.
  allowed_card_types:
  - reconciliation_profile
  - reconciliation_side
  - reconciliation_unit
  - matching_logic
  - mismatch_category
  - query_pattern
  - rule
  forbidden_card_types:
  - tenant
  - group
  - platform_account
  - account_data_binding
  - business_scope_set
  - business_flow_binding
  - bank_account
  - payment_gateway_account
  - statutory_tax_filing
  - logistics_account
  confidence: high
```


```yaml
source_evidence:
  id: ev.jiomart.marketplace.7_1_oms_settlement_match_3_way_per_order
  source_section: 7.1 OMS → Settlement Match (3-Way Per Order)
  source_context: marketplace
  source_line_start: 236
  source_line_end: 255
  evidence_type: reconciliation_playbook
  supported_semantics:
  - Source-backed JioMart reconciliation logic for 7.1 OMS → Settlement Match (3-Way Per Order), including tables, join keys,
    filters, and output fields.
  unsupported_semantics:
  - Do not infer tenant/group/platform-account/bank/statutory-filing/external-logistics cards from this evidence.
  allowed_card_types:
  - reconciliation_profile
  - reconciliation_side
  - reconciliation_unit
  - matching_logic
  - mismatch_category
  - query_pattern
  - rule
  forbidden_card_types:
  - tenant
  - group
  - platform_account
  - account_data_binding
  - business_scope_set
  - business_flow_binding
  - bank_account
  - payment_gateway_account
  - statutory_tax_filing
  - logistics_account
  confidence: high
```


```yaml
source_evidence:
  id: ev.jiomart.marketplace.7_2_returns_oms_settlement_full_chain
  source_section: 7.2 Returns → OMS → Settlement Full Chain
  source_context: marketplace
  source_line_start: 256
  source_line_end: 269
  evidence_type: reconciliation_playbook
  supported_semantics:
  - Source-backed JioMart reconciliation logic for 7.2 Returns → OMS → Settlement Full Chain, including tables, join keys,
    filters, and output fields.
  unsupported_semantics:
  - Do not infer tenant/group/platform-account/bank/statutory-filing/external-logistics cards from this evidence.
  allowed_card_types:
  - reconciliation_profile
  - reconciliation_side
  - reconciliation_unit
  - matching_logic
  - mismatch_category
  - query_pattern
  - rule
  forbidden_card_types:
  - tenant
  - group
  - platform_account
  - account_data_binding
  - business_scope_set
  - business_flow_binding
  - bank_account
  - payment_gateway_account
  - statutory_tax_filing
  - logistics_account
  confidence: high
```


```yaml
source_evidence:
  id: ev.jiomart.marketplace.7_3_unreconciled_oms_orders_not_in_settlement
  source_section: 7.3 Unreconciled OMS Orders (Not in Settlement)
  source_context: marketplace
  source_line_start: 270
  source_line_end: 282
  evidence_type: reconciliation_playbook
  supported_semantics:
  - Source-backed JioMart reconciliation logic for 7.3 Unreconciled OMS Orders (Not in Settlement), including tables, join
    keys, filters, and output fields.
  unsupported_semantics:
  - Do not infer tenant/group/platform-account/bank/statutory-filing/external-logistics cards from this evidence.
  allowed_card_types:
  - reconciliation_profile
  - reconciliation_side
  - reconciliation_unit
  - matching_logic
  - mismatch_category
  - query_pattern
  - rule
  forbidden_card_types:
  - tenant
  - group
  - platform_account
  - account_data_binding
  - business_scope_set
  - business_flow_binding
  - bank_account
  - payment_gateway_account
  - statutory_tax_filing
  - logistics_account
  confidence: high
```


```yaml
source_evidence:
  id: ev.jiomart.marketplace.7_4_tcs_reconciliation
  source_section: 7.4 TCS Reconciliation
  source_context: marketplace
  source_line_start: 283
  source_line_end: 296
  evidence_type: reconciliation_playbook
  supported_semantics:
  - Source-backed JioMart reconciliation logic for 7.4 TCS Reconciliation, including tables, join keys, filters, and output
    fields.
  unsupported_semantics:
  - Do not infer tenant/group/platform-account/bank/statutory-filing/external-logistics cards from this evidence.
  allowed_card_types:
  - reconciliation_profile
  - reconciliation_side
  - reconciliation_unit
  - matching_logic
  - mismatch_category
  - query_pattern
  - rule
  forbidden_card_types:
  - tenant
  - group
  - platform_account
  - account_data_binding
  - business_scope_set
  - business_flow_binding
  - bank_account
  - payment_gateway_account
  - statutory_tax_filing
  - logistics_account
  confidence: high
```


```yaml
source_evidence:
  id: ev.jiomart.marketplace.8_data_quality_observations_and_known_issues
  source_section: 8. Data Quality Observations & Known Issues
  source_context: marketplace
  source_line_start: 297
  source_line_end: 310
  evidence_type: caveat
  supported_semantics:
  - Data quality, mandatory-filter, or operational caveat semantics for 8. Data Quality Observations & Known Issues.
  unsupported_semantics:
  - Do not infer tenant/group/platform-account/bank/statutory-filing/external-logistics cards from this evidence.
  allowed_card_types:
  - rule
  - review_item
  - validation_test
  - value_profile
  forbidden_card_types:
  - tenant
  - group
  - platform_account
  - account_data_binding
  - business_scope_set
  - business_flow_binding
  - bank_account
  - payment_gateway_account
  - statutory_tax_filing
  - logistics_account
  confidence: high
```


```yaml
source_evidence:
  id: ev.jiomart.marketplace.9_mandatory_query_filters
  source_section: 9. Mandatory Query Filters
  source_context: marketplace
  source_line_start: 311
  source_line_end: 323
  evidence_type: caveat
  supported_semantics:
  - Data quality, mandatory-filter, or operational caveat semantics for 9. Mandatory Query Filters.
  unsupported_semantics:
  - Do not infer tenant/group/platform-account/bank/statutory-filing/external-logistics cards from this evidence.
  allowed_card_types:
  - rule
  - review_item
  - validation_test
  - value_profile
  forbidden_card_types:
  - tenant
  - group
  - platform_account
  - account_data_binding
  - business_scope_set
  - business_flow_binding
  - bank_account
  - payment_gateway_account
  - statutory_tax_filing
  - logistics_account
  confidence: high
```


```yaml
source_evidence:
  id: ev.jiomart.marketplace.10_table_summary_reference
  source_section: 10. Table Summary Reference
  source_context: marketplace
  source_line_start: 324
  source_line_end: 331
  evidence_type: table
  supported_semantics:
  - Documented source values, observed distributions, benchmark/context tables, or table statistics for 10. Table Summary
    Reference.
  unsupported_semantics:
  - Do not infer tenant/group/platform-account/bank/statutory-filing/external-logistics cards from this evidence.
  allowed_card_types:
  - value_profile
  - column
  - metric
  - rule
  - table
  forbidden_card_types:
  - tenant
  - group
  - platform_account
  - account_data_binding
  - business_scope_set
  - business_flow_binding
  - bank_account
  - payment_gateway_account
  - statutory_tax_filing
  - logistics_account
  confidence: high
```


```yaml
source_evidence:
  id: ev.jiomart.shipment.table_jiomart_shipment
  source_section: 'Table : JioMart Shipment'
  source_context: shipment
  source_line_start: 332
  source_line_end: 334
  evidence_type: prose
  supported_semantics:
  - 'Prose semantics from source section Table : JioMart Shipment.'
  unsupported_semantics:
  - Do not infer tenant/group/platform-account/bank/statutory-filing/external-logistics cards from this evidence.
  allowed_card_types:
  - platform
  - platform_context
  - domain
  - business_process
  - workflow_step
  - rule
  - value_profile
  forbidden_card_types:
  - tenant
  - group
  - platform_account
  - account_data_binding
  - business_scope_set
  - business_flow_binding
  - bank_account
  - payment_gateway_account
  - statutory_tax_filing
  - logistics_account
  confidence: high
```


```yaml
source_evidence:
  id: ev.jiomart.shipment.1_table_overview
  source_section: 1. Table Overview
  source_context: shipment
  source_line_start: 335
  source_line_end: 344
  evidence_type: prose
  supported_semantics:
  - Prose semantics from source section 1. Table Overview.
  unsupported_semantics:
  - Do not infer tenant/group/platform-account/bank/statutory-filing/external-logistics cards from this evidence.
  allowed_card_types:
  - platform
  - platform_context
  - domain
  - business_process
  - workflow_step
  - rule
  - value_profile
  forbidden_card_types:
  - tenant
  - group
  - platform_account
  - account_data_binding
  - business_scope_set
  - business_flow_binding
  - bank_account
  - payment_gateway_account
  - statutory_tax_filing
  - logistics_account
  confidence: high
```


```yaml
source_evidence:
  id: ev.jiomart.shipment.2_key_statistics
  source_section: 2. Key Statistics
  source_context: shipment
  source_line_start: 345
  source_line_end: 361
  evidence_type: table
  supported_semantics:
  - Documented source values, observed distributions, benchmark/context tables, or table statistics for 2. Key Statistics.
  unsupported_semantics:
  - Do not infer tenant/group/platform-account/bank/statutory-filing/external-logistics cards from this evidence.
  allowed_card_types:
  - value_profile
  - column
  - metric
  - rule
  - table
  forbidden_card_types:
  - tenant
  - group
  - platform_account
  - account_data_binding
  - business_scope_set
  - business_flow_binding
  - bank_account
  - payment_gateway_account
  - statutory_tax_filing
  - logistics_account
  confidence: high
```


```yaml
source_evidence:
  id: ev.jiomart.shipment.3_schema_details_29_columns
  source_section: 3. Schema Details (29 Columns)
  source_context: shipment
  source_line_start: 362
  source_line_end: 386
  evidence_type: schema_reference
  supported_semantics:
  - shipment source table schema columns, source-declared types, and descriptions.
  unsupported_semantics:
  - Do not infer tenant/group/platform-account/bank/statutory-filing/external-logistics cards from this evidence.
  allowed_card_types:
  - table
  - column
  - relationship
  - rule
  - validation_test
  forbidden_card_types:
  - tenant
  - group
  - platform_account
  - account_data_binding
  - business_scope_set
  - business_flow_binding
  - bank_account
  - payment_gateway_account
  - statutory_tax_filing
  - logistics_account
  confidence: high
```


```yaml
source_evidence:
  id: ev.jiomart.shipment.4_distinct_value_analysis
  source_section: 4. Distinct Value Analysis
  source_context: shipment
  source_line_start: 387
  source_line_end: 387
  evidence_type: table
  supported_semantics:
  - Documented source values, observed distributions, benchmark/context tables, or table statistics for 4. Distinct Value
    Analysis.
  unsupported_semantics:
  - Do not infer tenant/group/platform-account/bank/statutory-filing/external-logistics cards from this evidence.
  allowed_card_types:
  - value_profile
  - column
  - metric
  - rule
  - table
  forbidden_card_types:
  - tenant
  - group
  - platform_account
  - account_data_binding
  - business_scope_set
  - business_flow_binding
  - bank_account
  - payment_gateway_account
  - statutory_tax_filing
  - logistics_account
  confidence: high
```


```yaml
source_evidence:
  id: ev.jiomart.shipment.order_status_distribution
  source_section: '`order_status` Distribution'
  source_context: shipment
  source_line_start: 388
  source_line_end: 393
  evidence_type: table
  supported_semantics:
  - Documented source values, observed distributions, benchmark/context tables, or table statistics for `order_status` Distribution.
  unsupported_semantics:
  - Do not infer tenant/group/platform-account/bank/statutory-filing/external-logistics cards from this evidence.
  allowed_card_types:
  - value_profile
  - column
  - metric
  - rule
  - table
  forbidden_card_types:
  - tenant
  - group
  - platform_account
  - account_data_binding
  - business_scope_set
  - business_flow_binding
  - bank_account
  - payment_gateway_account
  - statutory_tax_filing
  - logistics_account
  confidence: high
```


```yaml
source_evidence:
  id: ev.jiomart.shipment.sku_naming_convention_ardeur_fashions
  source_section: SKU Naming Convention (ARDEUR FASHIONS)
  source_context: shipment
  source_line_start: 394
  source_line_end: 399
  evidence_type: prose
  supported_semantics:
  - Prose semantics from source section SKU Naming Convention (ARDEUR FASHIONS).
  unsupported_semantics:
  - Do not infer tenant/group/platform-account/bank/statutory-filing/external-logistics cards from this evidence.
  allowed_card_types:
  - platform
  - platform_context
  - domain
  - business_process
  - workflow_step
  - rule
  - value_profile
  forbidden_card_types:
  - tenant
  - group
  - platform_account
  - account_data_binding
  - business_scope_set
  - business_flow_binding
  - bank_account
  - payment_gateway_account
  - statutory_tax_filing
  - logistics_account
  confidence: high
```


```yaml
source_evidence:
  id: ev.jiomart.shipment.promotional_discount_scale
  source_section: Promotional Discount Scale
  source_context: shipment
  source_line_start: 400
  source_line_end: 402
  evidence_type: prose
  supported_semantics:
  - Prose semantics from source section Promotional Discount Scale.
  unsupported_semantics:
  - Do not infer tenant/group/platform-account/bank/statutory-filing/external-logistics cards from this evidence.
  allowed_card_types:
  - platform
  - platform_context
  - domain
  - business_process
  - workflow_step
  - rule
  - value_profile
  forbidden_card_types:
  - tenant
  - group
  - platform_account
  - account_data_binding
  - business_scope_set
  - business_flow_binding
  - bank_account
  - payment_gateway_account
  - statutory_tax_filing
  - logistics_account
  confidence: high
```


```yaml
source_evidence:
  id: ev.jiomart.shipment.5_sample_records
  source_section: 5. Sample Records
  source_context: shipment
  source_line_start: 403
  source_line_end: 429
  evidence_type: prose
  supported_semantics:
  - Prose semantics from source section 5. Sample Records.
  unsupported_semantics:
  - Do not infer tenant/group/platform-account/bank/statutory-filing/external-logistics cards from this evidence.
  allowed_card_types:
  - platform
  - platform_context
  - domain
  - business_process
  - workflow_step
  - rule
  - value_profile
  forbidden_card_types:
  - tenant
  - group
  - platform_account
  - account_data_binding
  - business_scope_set
  - business_flow_binding
  - bank_account
  - payment_gateway_account
  - statutory_tax_filing
  - logistics_account
  confidence: high
```


```yaml
source_evidence:
  id: ev.jiomart.shipment.6_data_quality_observations
  source_section: 6. Data Quality Observations
  source_context: shipment
  source_line_start: 430
  source_line_end: 439
  evidence_type: caveat
  supported_semantics:
  - Data quality, mandatory-filter, or operational caveat semantics for 6. Data Quality Observations.
  unsupported_semantics:
  - Do not infer tenant/group/platform-account/bank/statutory-filing/external-logistics cards from this evidence.
  allowed_card_types:
  - rule
  - review_item
  - validation_test
  - value_profile
  forbidden_card_types:
  - tenant
  - group
  - platform_account
  - account_data_binding
  - business_scope_set
  - business_flow_binding
  - bank_account
  - payment_gateway_account
  - statutory_tax_filing
  - logistics_account
  confidence: high
```


```yaml
source_evidence:
  id: ev.jiomart.shipment.7_common_query_patterns
  source_section: 7. Common Query Patterns
  source_context: shipment
  source_line_start: 440
  source_line_end: 440
  evidence_type: query_example
  supported_semantics:
  - Executable/source-backed SQL query pattern for 7. Common Query Patterns, including columns, filters, aggregation grain,
    and output aliases.
  unsupported_semantics:
  - Do not infer tenant/group/platform-account/bank/statutory-filing/external-logistics cards from this evidence.
  - Do not create metric implementations unless the SQL references documented tables/columns and required filters.
  allowed_card_types:
  - metric
  - metric_implementation
  - query_pattern
  - output_contract
  - validation_test
  - rule
  forbidden_card_types:
  - tenant
  - group
  - platform_account
  - account_data_binding
  - business_scope_set
  - business_flow_binding
  - bank_account
  - payment_gateway_account
  - statutory_tax_filing
  - logistics_account
  - non_executable_metric_implementation
  confidence: high
```


```yaml
source_evidence:
  id: ev.jiomart.shipment.7_1_shipment_status_summary
  source_section: 7.1 Shipment Status Summary
  source_context: shipment
  source_line_start: 441
  source_line_end: 453
  evidence_type: prose
  supported_semantics:
  - Prose semantics from source section 7.1 Shipment Status Summary.
  unsupported_semantics:
  - Do not infer tenant/group/platform-account/bank/statutory-filing/external-logistics cards from this evidence.
  allowed_card_types:
  - platform
  - platform_context
  - domain
  - business_process
  - workflow_step
  - rule
  - value_profile
  forbidden_card_types:
  - tenant
  - group
  - platform_account
  - account_data_binding
  - business_scope_set
  - business_flow_binding
  - bank_account
  - payment_gateway_account
  - statutory_tax_filing
  - logistics_account
  confidence: high
```


```yaml
source_evidence:
  id: ev.jiomart.shipment.7_2_monthly_gmv
  source_section: 7.2 Monthly GMV
  source_context: shipment
  source_line_start: 454
  source_line_end: 464
  evidence_type: query_example
  supported_semantics:
  - Executable/source-backed SQL query pattern for 7.2 Monthly GMV, including columns, filters, aggregation grain, and output
    aliases.
  unsupported_semantics:
  - Do not infer tenant/group/platform-account/bank/statutory-filing/external-logistics cards from this evidence.
  - Do not create metric implementations unless the SQL references documented tables/columns and required filters.
  allowed_card_types:
  - metric
  - metric_implementation
  - query_pattern
  - output_contract
  - validation_test
  - rule
  forbidden_card_types:
  - tenant
  - group
  - platform_account
  - account_data_binding
  - business_scope_set
  - business_flow_binding
  - bank_account
  - payment_gateway_account
  - statutory_tax_filing
  - logistics_account
  - non_executable_metric_implementation
  confidence: high
```


```yaml
source_evidence:
  id: ev.jiomart.shipment.7_3_top_skus
  source_section: 7.3 Top SKUs
  source_context: shipment
  source_line_start: 465
  source_line_end: 478
  evidence_type: query_example
  supported_semantics:
  - Executable/source-backed SQL query pattern for 7.3 Top SKUs, including columns, filters, aggregation grain, and output
    aliases.
  unsupported_semantics:
  - Do not infer tenant/group/platform-account/bank/statutory-filing/external-logistics cards from this evidence.
  - Do not create metric implementations unless the SQL references documented tables/columns and required filters.
  allowed_card_types:
  - metric
  - metric_implementation
  - query_pattern
  - output_contract
  - validation_test
  - rule
  forbidden_card_types:
  - tenant
  - group
  - platform_account
  - account_data_binding
  - business_scope_set
  - business_flow_binding
  - bank_account
  - payment_gateway_account
  - statutory_tax_filing
  - logistics_account
  - non_executable_metric_implementation
  confidence: high
```


```yaml
source_evidence:
  id: ev.jiomart.settlement.table_jiomart_settlement_table_knowledge_base
  source_section: 'Table : JioMart Settlement — Table Knowledge Base'
  source_context: settlement
  source_line_start: 479
  source_line_end: 481
  evidence_type: prose
  supported_semantics:
  - 'Prose semantics from source section Table : JioMart Settlement — Table Knowledge Base.'
  unsupported_semantics:
  - Do not infer tenant/group/platform-account/bank/statutory-filing/external-logistics cards from this evidence.
  allowed_card_types:
  - platform
  - platform_context
  - domain
  - business_process
  - workflow_step
  - rule
  - value_profile
  forbidden_card_types:
  - tenant
  - group
  - platform_account
  - account_data_binding
  - business_scope_set
  - business_flow_binding
  - bank_account
  - payment_gateway_account
  - statutory_tax_filing
  - logistics_account
  confidence: high
```


```yaml
source_evidence:
  id: ev.jiomart.settlement.1_table_overview
  source_section: 1. Table Overview
  source_context: settlement
  source_line_start: 482
  source_line_end: 486
  evidence_type: prose
  supported_semantics:
  - Prose semantics from source section 1. Table Overview.
  unsupported_semantics:
  - Do not infer tenant/group/platform-account/bank/statutory-filing/external-logistics cards from this evidence.
  allowed_card_types:
  - platform
  - platform_context
  - domain
  - business_process
  - workflow_step
  - rule
  - value_profile
  forbidden_card_types:
  - tenant
  - group
  - platform_account
  - account_data_binding
  - business_scope_set
  - business_flow_binding
  - bank_account
  - payment_gateway_account
  - statutory_tax_filing
  - logistics_account
  confidence: high
```


```yaml
source_evidence:
  id: ev.jiomart.settlement.2_key_statistics
  source_section: 2. Key Statistics
  source_context: settlement
  source_line_start: 487
  source_line_end: 505
  evidence_type: table
  supported_semantics:
  - Documented source values, observed distributions, benchmark/context tables, or table statistics for 2. Key Statistics.
  unsupported_semantics:
  - Do not infer tenant/group/platform-account/bank/statutory-filing/external-logistics cards from this evidence.
  allowed_card_types:
  - value_profile
  - column
  - metric
  - rule
  - table
  forbidden_card_types:
  - tenant
  - group
  - platform_account
  - account_data_binding
  - business_scope_set
  - business_flow_binding
  - bank_account
  - payment_gateway_account
  - statutory_tax_filing
  - logistics_account
  confidence: high
```


```yaml
source_evidence:
  id: ev.jiomart.settlement.3_schema_details_40_columns
  source_section: 3. Schema Details (40 Columns)
  source_context: settlement
  source_line_start: 506
  source_line_end: 506
  evidence_type: schema_reference
  supported_semantics:
  - settlement source table schema columns, source-declared types, and descriptions.
  unsupported_semantics:
  - Do not infer tenant/group/platform-account/bank/statutory-filing/external-logistics cards from this evidence.
  allowed_card_types:
  - table
  - column
  - relationship
  - rule
  - validation_test
  forbidden_card_types:
  - tenant
  - group
  - platform_account
  - account_data_binding
  - business_scope_set
  - business_flow_binding
  - bank_account
  - payment_gateway_account
  - statutory_tax_filing
  - logistics_account
  confidence: high
```


```yaml
source_evidence:
  id: ev.jiomart.settlement.3_1_identity_columns
  source_section: 3.1 Identity Columns
  source_context: settlement
  source_line_start: 507
  source_line_end: 522
  evidence_type: prose
  supported_semantics:
  - Prose semantics from source section 3.1 Identity Columns.
  unsupported_semantics:
  - Do not infer tenant/group/platform-account/bank/statutory-filing/external-logistics cards from this evidence.
  allowed_card_types:
  - platform
  - platform_context
  - domain
  - business_process
  - workflow_step
  - rule
  - value_profile
  forbidden_card_types:
  - tenant
  - group
  - platform_account
  - account_data_binding
  - business_scope_set
  - business_flow_binding
  - bank_account
  - payment_gateway_account
  - statutory_tax_filing
  - logistics_account
  confidence: high
```


```yaml
source_evidence:
  id: ev.jiomart.settlement.3_2_date_columns
  source_section: 3.2 Date Columns
  source_context: settlement
  source_line_start: 523
  source_line_end: 529
  evidence_type: prose
  supported_semantics:
  - Prose semantics from source section 3.2 Date Columns.
  unsupported_semantics:
  - Do not infer tenant/group/platform-account/bank/statutory-filing/external-logistics cards from this evidence.
  allowed_card_types:
  - platform
  - platform_context
  - domain
  - business_process
  - workflow_step
  - rule
  - value_profile
  forbidden_card_types:
  - tenant
  - group
  - platform_account
  - account_data_binding
  - business_scope_set
  - business_flow_binding
  - bank_account
  - payment_gateway_account
  - statutory_tax_filing
  - logistics_account
  confidence: high
```


```yaml
source_evidence:
  id: ev.jiomart.settlement.3_3_financial_columns
  source_section: 3.3 Financial Columns
  source_context: settlement
  source_line_start: 530
  source_line_end: 534
  evidence_type: prose
  supported_semantics:
  - Prose semantics from source section 3.3 Financial Columns.
  unsupported_semantics:
  - Do not infer tenant/group/platform-account/bank/statutory-filing/external-logistics cards from this evidence.
  allowed_card_types:
  - platform
  - platform_context
  - domain
  - business_process
  - workflow_step
  - rule
  - value_profile
  forbidden_card_types:
  - tenant
  - group
  - platform_account
  - account_data_binding
  - business_scope_set
  - business_flow_binding
  - bank_account
  - payment_gateway_account
  - statutory_tax_filing
  - logistics_account
  confidence: high
```


```yaml
source_evidence:
  id: ev.jiomart.settlement.3_4_classification_columns
  source_section: 3.4 Classification Columns
  source_context: settlement
  source_line_start: 535
  source_line_end: 542
  evidence_type: prose
  supported_semantics:
  - Prose semantics from source section 3.4 Classification Columns.
  unsupported_semantics:
  - Do not infer tenant/group/platform-account/bank/statutory-filing/external-logistics cards from this evidence.
  allowed_card_types:
  - platform
  - platform_context
  - domain
  - business_process
  - workflow_step
  - rule
  - value_profile
  forbidden_card_types:
  - tenant
  - group
  - platform_account
  - account_data_binding
  - business_scope_set
  - business_flow_binding
  - bank_account
  - payment_gateway_account
  - statutory_tax_filing
  - logistics_account
  confidence: high
```


```yaml
source_evidence:
  id: ev.jiomart.settlement.3_5_system_metadata
  source_section: 3.5 System / Metadata
  source_context: settlement
  source_line_start: 543
  source_line_end: 554
  evidence_type: prose
  supported_semantics:
  - Prose semantics from source section 3.5 System / Metadata.
  unsupported_semantics:
  - Do not infer tenant/group/platform-account/bank/statutory-filing/external-logistics cards from this evidence.
  allowed_card_types:
  - platform
  - platform_context
  - domain
  - business_process
  - workflow_step
  - rule
  - value_profile
  forbidden_card_types:
  - tenant
  - group
  - platform_account
  - account_data_binding
  - business_scope_set
  - business_flow_binding
  - bank_account
  - payment_gateway_account
  - statutory_tax_filing
  - logistics_account
  confidence: high
```


```yaml
source_evidence:
  id: ev.jiomart.settlement.4_settlement_structure_event_based_multi_row_model
  source_section: 4. Settlement Structure — Event-Based Multi-Row Model
  source_context: settlement
  source_line_start: 555
  source_line_end: 555
  evidence_type: prose
  supported_semantics:
  - Prose semantics from source section 4. Settlement Structure — Event-Based Multi-Row Model.
  unsupported_semantics:
  - Do not infer tenant/group/platform-account/bank/statutory-filing/external-logistics cards from this evidence.
  allowed_card_types:
  - platform
  - platform_context
  - domain
  - business_process
  - workflow_step
  - rule
  - value_profile
  forbidden_card_types:
  - tenant
  - group
  - platform_account
  - account_data_binding
  - business_scope_set
  - business_flow_binding
  - bank_account
  - payment_gateway_account
  - statutory_tax_filing
  - logistics_account
  confidence: high
```


```yaml
source_evidence:
  id: ev.jiomart.settlement.how_jiomart_settlement_works
  source_section: How JioMart Settlement Works
  source_context: settlement
  source_line_start: 556
  source_line_end: 569
  evidence_type: prose
  supported_semantics:
  - Prose semantics from source section How JioMart Settlement Works.
  unsupported_semantics:
  - Do not infer tenant/group/platform-account/bank/statutory-filing/external-logistics cards from this evidence.
  allowed_card_types:
  - platform
  - platform_context
  - domain
  - business_process
  - workflow_step
  - rule
  - value_profile
  forbidden_card_types:
  - tenant
  - group
  - platform_account
  - account_data_binding
  - business_scope_set
  - business_flow_binding
  - bank_account
  - payment_gateway_account
  - statutory_tax_filing
  - logistics_account
  confidence: high
```


```yaml
source_evidence:
  id: ev.jiomart.settlement.full_event_accountabletype_matrix
  source_section: Full Event / AccountableType Matrix
  source_context: settlement
  source_line_start: 570
  source_line_end: 583
  evidence_type: table
  supported_semantics:
  - Documented source values, observed distributions, benchmark/context tables, or table statistics for Full Event / AccountableType
    Matrix.
  unsupported_semantics:
  - Do not infer tenant/group/platform-account/bank/statutory-filing/external-logistics cards from this evidence.
  allowed_card_types:
  - value_profile
  - column
  - metric
  - rule
  - table
  forbidden_card_types:
  - tenant
  - group
  - platform_account
  - account_data_binding
  - business_scope_set
  - business_flow_binding
  - bank_account
  - payment_gateway_account
  - statutory_tax_filing
  - logistics_account
  confidence: high
```


```yaml
source_evidence:
  id: ev.jiomart.settlement.5_financial_waterfall
  source_section: 5. Financial Waterfall
  source_context: settlement
  source_line_start: 584
  source_line_end: 599
  evidence_type: prose
  supported_semantics:
  - Prose semantics from source section 5. Financial Waterfall.
  unsupported_semantics:
  - Do not infer tenant/group/platform-account/bank/statutory-filing/external-logistics cards from this evidence.
  allowed_card_types:
  - platform
  - platform_context
  - domain
  - business_process
  - workflow_step
  - rule
  - value_profile
  forbidden_card_types:
  - tenant
  - group
  - platform_account
  - account_data_binding
  - business_scope_set
  - business_flow_binding
  - bank_account
  - payment_gateway_account
  - statutory_tax_filing
  - logistics_account
  confidence: high
```


```yaml
source_evidence:
  id: ev.jiomart.settlement.6_sample_records
  source_section: 6. Sample Records
  source_context: settlement
  source_line_start: 600
  source_line_end: 623
  evidence_type: prose
  supported_semantics:
  - Prose semantics from source section 6. Sample Records.
  unsupported_semantics:
  - Do not infer tenant/group/platform-account/bank/statutory-filing/external-logistics cards from this evidence.
  allowed_card_types:
  - platform
  - platform_context
  - domain
  - business_process
  - workflow_step
  - rule
  - value_profile
  forbidden_card_types:
  - tenant
  - group
  - platform_account
  - account_data_binding
  - business_scope_set
  - business_flow_binding
  - bank_account
  - payment_gateway_account
  - statutory_tax_filing
  - logistics_account
  confidence: high
```


```yaml
source_evidence:
  id: ev.jiomart.settlement.7_data_quality_observations
  source_section: 7. Data Quality Observations
  source_context: settlement
  source_line_start: 624
  source_line_end: 634
  evidence_type: caveat
  supported_semantics:
  - Data quality, mandatory-filter, or operational caveat semantics for 7. Data Quality Observations.
  unsupported_semantics:
  - Do not infer tenant/group/platform-account/bank/statutory-filing/external-logistics cards from this evidence.
  allowed_card_types:
  - rule
  - review_item
  - validation_test
  - value_profile
  forbidden_card_types:
  - tenant
  - group
  - platform_account
  - account_data_binding
  - business_scope_set
  - business_flow_binding
  - bank_account
  - payment_gateway_account
  - statutory_tax_filing
  - logistics_account
  confidence: high
```


```yaml
source_evidence:
  id: ev.jiomart.settlement.8_common_query_patterns
  source_section: 8. Common Query Patterns
  source_context: settlement
  source_line_start: 635
  source_line_end: 635
  evidence_type: query_example
  supported_semantics:
  - Executable/source-backed SQL query pattern for 8. Common Query Patterns, including columns, filters, aggregation grain,
    and output aliases.
  unsupported_semantics:
  - Do not infer tenant/group/platform-account/bank/statutory-filing/external-logistics cards from this evidence.
  - Do not create metric implementations unless the SQL references documented tables/columns and required filters.
  allowed_card_types:
  - metric
  - metric_implementation
  - query_pattern
  - output_contract
  - validation_test
  - rule
  forbidden_card_types:
  - tenant
  - group
  - platform_account
  - account_data_binding
  - business_scope_set
  - business_flow_binding
  - bank_account
  - payment_gateway_account
  - statutory_tax_filing
  - logistics_account
  - non_executable_metric_implementation
  confidence: high
```


```yaml
source_evidence:
  id: ev.jiomart.settlement.8_1_net_settlement_per_order_structured_rows
  source_section: 8.1 Net Settlement per Order (Structured Rows)
  source_context: settlement
  source_line_start: 636
  source_line_end: 649
  evidence_type: prose
  supported_semantics:
  - Prose semantics from source section 8.1 Net Settlement per Order (Structured Rows).
  unsupported_semantics:
  - Do not infer tenant/group/platform-account/bank/statutory-filing/external-logistics cards from this evidence.
  allowed_card_types:
  - platform
  - platform_context
  - domain
  - business_process
  - workflow_step
  - rule
  - value_profile
  forbidden_card_types:
  - tenant
  - group
  - platform_account
  - account_data_binding
  - business_scope_set
  - business_flow_binding
  - bank_account
  - payment_gateway_account
  - statutory_tax_filing
  - logistics_account
  confidence: high
```


```yaml
source_evidence:
  id: ev.jiomart.settlement.8_2_monthly_settlement_summary
  source_section: 8.2 Monthly Settlement Summary
  source_context: settlement
  source_line_start: 650
  source_line_end: 662
  evidence_type: query_example
  supported_semantics:
  - Executable/source-backed SQL query pattern for 8.2 Monthly Settlement Summary, including columns, filters, aggregation
    grain, and output aliases.
  unsupported_semantics:
  - Do not infer tenant/group/platform-account/bank/statutory-filing/external-logistics cards from this evidence.
  - Do not create metric implementations unless the SQL references documented tables/columns and required filters.
  allowed_card_types:
  - metric
  - metric_implementation
  - query_pattern
  - output_contract
  - validation_test
  - rule
  forbidden_card_types:
  - tenant
  - group
  - platform_account
  - account_data_binding
  - business_scope_set
  - business_flow_binding
  - bank_account
  - payment_gateway_account
  - statutory_tax_filing
  - logistics_account
  - non_executable_metric_implementation
  confidence: high
```


```yaml
source_evidence:
  id: ev.jiomart.settlement.8_3_settlement_oms_reconciliation
  source_section: 8.3 Settlement ↔ OMS Reconciliation
  source_context: settlement
  source_line_start: 663
  source_line_end: 684
  evidence_type: reconciliation_playbook
  supported_semantics:
  - Source-backed JioMart reconciliation logic for 8.3 Settlement ↔ OMS Reconciliation, including tables, join keys, filters,
    and output fields.
  unsupported_semantics:
  - Do not infer tenant/group/platform-account/bank/statutory-filing/external-logistics cards from this evidence.
  allowed_card_types:
  - reconciliation_profile
  - reconciliation_side
  - reconciliation_unit
  - matching_logic
  - mismatch_category
  - query_pattern
  - rule
  forbidden_card_types:
  - tenant
  - group
  - platform_account
  - account_data_binding
  - business_scope_set
  - business_flow_binding
  - bank_account
  - payment_gateway_account
  - statutory_tax_filing
  - logistics_account
  confidence: high
```


```yaml
source_evidence:
  id: ev.jiomart.settlement.8_4_tcs_reconciliation_oms_vs_settlement
  source_section: 8.4 TCS Reconciliation (OMS vs Settlement)
  source_context: settlement
  source_line_start: 685
  source_line_end: 694
  evidence_type: reconciliation_playbook
  supported_semantics:
  - Source-backed JioMart reconciliation logic for 8.4 TCS Reconciliation (OMS vs Settlement), including tables, join keys,
    filters, and output fields.
  unsupported_semantics:
  - Do not infer tenant/group/platform-account/bank/statutory-filing/external-logistics cards from this evidence.
  allowed_card_types:
  - reconciliation_profile
  - reconciliation_side
  - reconciliation_unit
  - matching_logic
  - mismatch_category
  - query_pattern
  - rule
  forbidden_card_types:
  - tenant
  - group
  - platform_account
  - account_data_binding
  - business_scope_set
  - business_flow_binding
  - bank_account
  - payment_gateway_account
  - statutory_tax_filing
  - logistics_account
  confidence: high
```


```yaml
source_evidence:
  id: ev.jiomart.settlement.8_5_credit_debit_notes
  source_section: 8.5 Credit / Debit Notes
  source_context: settlement
  source_line_start: 695
  source_line_end: 706
  evidence_type: query_example
  supported_semantics:
  - Executable/source-backed SQL query pattern for 8.5 Credit / Debit Notes, including columns, filters, aggregation grain,
    and output aliases.
  unsupported_semantics:
  - Do not infer tenant/group/platform-account/bank/statutory-filing/external-logistics cards from this evidence.
  - Do not create metric implementations unless the SQL references documented tables/columns and required filters.
  allowed_card_types:
  - metric
  - metric_implementation
  - query_pattern
  - output_contract
  - validation_test
  - rule
  forbidden_card_types:
  - tenant
  - group
  - platform_account
  - account_data_binding
  - business_scope_set
  - business_flow_binding
  - bank_account
  - payment_gateway_account
  - statutory_tax_filing
  - logistics_account
  - non_executable_metric_implementation
  confidence: high
```


```yaml
source_evidence:
  id: ev.jiomart.returns.table_jiomart_returns_table_knowledge_base
  source_section: 'Table: JioMart Returns — Table Knowledge Base'
  source_context: returns
  source_line_start: 707
  source_line_end: 709
  evidence_type: prose
  supported_semantics:
  - 'Prose semantics from source section Table: JioMart Returns — Table Knowledge Base.'
  unsupported_semantics:
  - Do not infer tenant/group/platform-account/bank/statutory-filing/external-logistics cards from this evidence.
  allowed_card_types:
  - platform
  - platform_context
  - domain
  - business_process
  - workflow_step
  - rule
  - value_profile
  forbidden_card_types:
  - tenant
  - group
  - platform_account
  - account_data_binding
  - business_scope_set
  - business_flow_binding
  - bank_account
  - payment_gateway_account
  - statutory_tax_filing
  - logistics_account
  confidence: high
```


```yaml
source_evidence:
  id: ev.jiomart.returns.1_table_overview
  source_section: 1. Table Overview
  source_context: returns
  source_line_start: 710
  source_line_end: 713
  evidence_type: prose
  supported_semantics:
  - Prose semantics from source section 1. Table Overview.
  unsupported_semantics:
  - Do not infer tenant/group/platform-account/bank/statutory-filing/external-logistics cards from this evidence.
  allowed_card_types:
  - platform
  - platform_context
  - domain
  - business_process
  - workflow_step
  - rule
  - value_profile
  forbidden_card_types:
  - tenant
  - group
  - platform_account
  - account_data_binding
  - business_scope_set
  - business_flow_binding
  - bank_account
  - payment_gateway_account
  - statutory_tax_filing
  - logistics_account
  confidence: high
```


```yaml
source_evidence:
  id: ev.jiomart.returns.2_key_statistics
  source_section: 2. Key Statistics
  source_context: returns
  source_line_start: 714
  source_line_end: 729
  evidence_type: table
  supported_semantics:
  - Documented source values, observed distributions, benchmark/context tables, or table statistics for 2. Key Statistics.
  unsupported_semantics:
  - Do not infer tenant/group/platform-account/bank/statutory-filing/external-logistics cards from this evidence.
  allowed_card_types:
  - value_profile
  - column
  - metric
  - rule
  - table
  forbidden_card_types:
  - tenant
  - group
  - platform_account
  - account_data_binding
  - business_scope_set
  - business_flow_binding
  - bank_account
  - payment_gateway_account
  - statutory_tax_filing
  - logistics_account
  confidence: high
```


```yaml
source_evidence:
  id: ev.jiomart.returns.3_schema_details_53_columns
  source_section: 3. Schema Details (53 Columns)
  source_context: returns
  source_line_start: 730
  source_line_end: 730
  evidence_type: schema_reference
  supported_semantics:
  - returns source table schema columns, source-declared types, and descriptions.
  unsupported_semantics:
  - Do not infer tenant/group/platform-account/bank/statutory-filing/external-logistics cards from this evidence.
  allowed_card_types:
  - table
  - column
  - relationship
  - rule
  - validation_test
  forbidden_card_types:
  - tenant
  - group
  - platform_account
  - account_data_binding
  - business_scope_set
  - business_flow_binding
  - bank_account
  - payment_gateway_account
  - statutory_tax_filing
  - logistics_account
  confidence: high
```


```yaml
source_evidence:
  id: ev.jiomart.returns.3_1_identity_columns
  source_section: 3.1 Identity Columns
  source_context: returns
  source_line_start: 731
  source_line_end: 746
  evidence_type: prose
  supported_semantics:
  - Prose semantics from source section 3.1 Identity Columns.
  unsupported_semantics:
  - Do not infer tenant/group/platform-account/bank/statutory-filing/external-logistics cards from this evidence.
  allowed_card_types:
  - platform
  - platform_context
  - domain
  - business_process
  - workflow_step
  - rule
  - value_profile
  forbidden_card_types:
  - tenant
  - group
  - platform_account
  - account_data_binding
  - business_scope_set
  - business_flow_binding
  - bank_account
  - payment_gateway_account
  - statutory_tax_filing
  - logistics_account
  confidence: high
```


```yaml
source_evidence:
  id: ev.jiomart.returns.3_2_date_columns
  source_section: 3.2 Date Columns
  source_context: returns
  source_line_start: 747
  source_line_end: 755
  evidence_type: prose
  supported_semantics:
  - Prose semantics from source section 3.2 Date Columns.
  unsupported_semantics:
  - Do not infer tenant/group/platform-account/bank/statutory-filing/external-logistics cards from this evidence.
  allowed_card_types:
  - platform
  - platform_context
  - domain
  - business_process
  - workflow_step
  - rule
  - value_profile
  forbidden_card_types:
  - tenant
  - group
  - platform_account
  - account_data_binding
  - business_scope_set
  - business_flow_binding
  - bank_account
  - payment_gateway_account
  - statutory_tax_filing
  - logistics_account
  confidence: high
```


```yaml
source_evidence:
  id: ev.jiomart.returns.3_3_financial_columns
  source_section: 3.3 Financial Columns
  source_context: returns
  source_line_start: 756
  source_line_end: 763
  evidence_type: prose
  supported_semantics:
  - Prose semantics from source section 3.3 Financial Columns.
  unsupported_semantics:
  - Do not infer tenant/group/platform-account/bank/statutory-filing/external-logistics cards from this evidence.
  allowed_card_types:
  - platform
  - platform_context
  - domain
  - business_process
  - workflow_step
  - rule
  - value_profile
  forbidden_card_types:
  - tenant
  - group
  - platform_account
  - account_data_binding
  - business_scope_set
  - business_flow_binding
  - bank_account
  - payment_gateway_account
  - statutory_tax_filing
  - logistics_account
  confidence: high
```


```yaml
source_evidence:
  id: ev.jiomart.returns.3_4_classification_columns
  source_section: 3.4 Classification Columns
  source_context: returns
  source_line_start: 764
  source_line_end: 774
  evidence_type: prose
  supported_semantics:
  - Prose semantics from source section 3.4 Classification Columns.
  unsupported_semantics:
  - Do not infer tenant/group/platform-account/bank/statutory-filing/external-logistics cards from this evidence.
  allowed_card_types:
  - platform
  - platform_context
  - domain
  - business_process
  - workflow_step
  - rule
  - value_profile
  forbidden_card_types:
  - tenant
  - group
  - platform_account
  - account_data_binding
  - business_scope_set
  - business_flow_binding
  - bank_account
  - payment_gateway_account
  - statutory_tax_filing
  - logistics_account
  confidence: high
```


```yaml
source_evidence:
  id: ev.jiomart.returns.3_5_logistics_columns
  source_section: 3.5 Logistics Columns
  source_context: returns
  source_line_start: 775
  source_line_end: 782
  evidence_type: prose
  supported_semantics:
  - Prose semantics from source section 3.5 Logistics Columns.
  unsupported_semantics:
  - Do not infer tenant/group/platform-account/bank/statutory-filing/external-logistics cards from this evidence.
  allowed_card_types:
  - platform
  - platform_context
  - domain
  - business_process
  - workflow_step
  - rule
  - value_profile
  forbidden_card_types:
  - tenant
  - group
  - platform_account
  - account_data_binding
  - business_scope_set
  - business_flow_binding
  - bank_account
  - payment_gateway_account
  - statutory_tax_filing
  - logistics_account
  confidence: high
```


```yaml
source_evidence:
  id: ev.jiomart.returns.3_6_system_metadata
  source_section: 3.6 System / Metadata
  source_context: returns
  source_line_start: 783
  source_line_end: 791
  evidence_type: prose
  supported_semantics:
  - Prose semantics from source section 3.6 System / Metadata.
  unsupported_semantics:
  - Do not infer tenant/group/platform-account/bank/statutory-filing/external-logistics cards from this evidence.
  allowed_card_types:
  - platform
  - platform_context
  - domain
  - business_process
  - workflow_step
  - rule
  - value_profile
  forbidden_card_types:
  - tenant
  - group
  - platform_account
  - account_data_binding
  - business_scope_set
  - business_flow_binding
  - bank_account
  - payment_gateway_account
  - statutory_tax_filing
  - logistics_account
  confidence: high
```


```yaml
source_evidence:
  id: ev.jiomart.returns.4_distinct_value_analysis
  source_section: 4. Distinct Value Analysis
  source_context: returns
  source_line_start: 792
  source_line_end: 792
  evidence_type: table
  supported_semantics:
  - Documented source values, observed distributions, benchmark/context tables, or table statistics for 4. Distinct Value
    Analysis.
  unsupported_semantics:
  - Do not infer tenant/group/platform-account/bank/statutory-filing/external-logistics cards from this evidence.
  allowed_card_types:
  - value_profile
  - column
  - metric
  - rule
  - table
  forbidden_card_types:
  - tenant
  - group
  - platform_account
  - account_data_binding
  - business_scope_set
  - business_flow_binding
  - bank_account
  - payment_gateway_account
  - statutory_tax_filing
  - logistics_account
  confidence: high
```


```yaml
source_evidence:
  id: ev.jiomart.returns.return_type_transaction_type_distribution
  source_section: '`return_type` / `transaction_type` Distribution'
  source_context: returns
  source_line_start: 793
  source_line_end: 799
  evidence_type: table
  supported_semantics:
  - Documented source values, observed distributions, benchmark/context tables, or table statistics for `return_type` / `transaction_type`
    Distribution.
  unsupported_semantics:
  - Do not infer tenant/group/platform-account/bank/statutory-filing/external-logistics cards from this evidence.
  allowed_card_types:
  - value_profile
  - column
  - metric
  - rule
  - table
  forbidden_card_types:
  - tenant
  - group
  - platform_account
  - account_data_binding
  - business_scope_set
  - business_flow_binding
  - bank_account
  - payment_gateway_account
  - statutory_tax_filing
  - logistics_account
  confidence: high
```


```yaml
source_evidence:
  id: ev.jiomart.returns.return_type_meanings
  source_section: Return Type Meanings
  source_context: returns
  source_line_start: 800
  source_line_end: 805
  evidence_type: table
  supported_semantics:
  - Documented source values, observed distributions, benchmark/context tables, or table statistics for Return Type Meanings.
  unsupported_semantics:
  - Do not infer tenant/group/platform-account/bank/statutory-filing/external-logistics cards from this evidence.
  allowed_card_types:
  - value_profile
  - column
  - metric
  - rule
  - table
  forbidden_card_types:
  - tenant
  - group
  - platform_account
  - account_data_binding
  - business_scope_set
  - business_flow_binding
  - bank_account
  - payment_gateway_account
  - statutory_tax_filing
  - logistics_account
  confidence: high
```


```yaml
source_evidence:
  id: ev.jiomart.returns.payment_mode
  source_section: '`payment_mode`'
  source_context: returns
  source_line_start: 806
  source_line_end: 810
  evidence_type: prose
  supported_semantics:
  - Prose semantics from source section `payment_mode`.
  unsupported_semantics:
  - Do not infer tenant/group/platform-account/bank/statutory-filing/external-logistics cards from this evidence.
  - Scope, GSTIN, fulfilment, or payment labels remain columns, value profiles, caveats, or rules only.
  allowed_card_types:
  - platform
  - platform_context
  - domain
  - business_process
  - workflow_step
  - rule
  - value_profile
  forbidden_card_types:
  - tenant
  - group
  - platform_account
  - account_data_binding
  - business_scope_set
  - business_flow_binding
  - bank_account
  - payment_gateway_account
  - statutory_tax_filing
  - logistics_account
  - process_variant
  confidence: high
```


```yaml
source_evidence:
  id: ev.jiomart.returns.couriers
  source_section: Couriers
  source_context: returns
  source_line_start: 811
  source_line_end: 816
  evidence_type: prose
  supported_semantics:
  - Prose semantics from source section Couriers.
  unsupported_semantics:
  - Do not infer tenant/group/platform-account/bank/statutory-filing/external-logistics cards from this evidence.
  allowed_card_types:
  - platform
  - platform_context
  - domain
  - business_process
  - workflow_step
  - rule
  - value_profile
  forbidden_card_types:
  - tenant
  - group
  - platform_account
  - account_data_binding
  - business_scope_set
  - business_flow_binding
  - bank_account
  - payment_gateway_account
  - statutory_tax_filing
  - logistics_account
  confidence: high
```


```yaml
source_evidence:
  id: ev.jiomart.returns.fulfilment_centres
  source_section: Fulfilment Centres
  source_context: returns
  source_line_start: 817
  source_line_end: 823
  evidence_type: prose
  supported_semantics:
  - Prose semantics from source section Fulfilment Centres.
  unsupported_semantics:
  - Do not infer tenant/group/platform-account/bank/statutory-filing/external-logistics cards from this evidence.
  - Scope, GSTIN, fulfilment, or payment labels remain columns, value profiles, caveats, or rules only.
  allowed_card_types:
  - platform
  - platform_context
  - domain
  - business_process
  - workflow_step
  - rule
  - value_profile
  forbidden_card_types:
  - tenant
  - group
  - platform_account
  - account_data_binding
  - business_scope_set
  - business_flow_binding
  - bank_account
  - payment_gateway_account
  - statutory_tax_filing
  - logistics_account
  - process_variant
  confidence: high
```


```yaml
source_evidence:
  id: ev.jiomart.returns.5_sample_records
  source_section: 5. Sample Records
  source_context: returns
  source_line_start: 824
  source_line_end: 857
  evidence_type: prose
  supported_semantics:
  - Prose semantics from source section 5. Sample Records.
  unsupported_semantics:
  - Do not infer tenant/group/platform-account/bank/statutory-filing/external-logistics cards from this evidence.
  allowed_card_types:
  - platform
  - platform_context
  - domain
  - business_process
  - workflow_step
  - rule
  - value_profile
  forbidden_card_types:
  - tenant
  - group
  - platform_account
  - account_data_binding
  - business_scope_set
  - business_flow_binding
  - bank_account
  - payment_gateway_account
  - statutory_tax_filing
  - logistics_account
  confidence: high
```


```yaml
source_evidence:
  id: ev.jiomart.returns.6_data_quality_observations
  source_section: 6. Data Quality Observations
  source_context: returns
  source_line_start: 858
  source_line_end: 868
  evidence_type: caveat
  supported_semantics:
  - Data quality, mandatory-filter, or operational caveat semantics for 6. Data Quality Observations.
  unsupported_semantics:
  - Do not infer tenant/group/platform-account/bank/statutory-filing/external-logistics cards from this evidence.
  allowed_card_types:
  - rule
  - review_item
  - validation_test
  - value_profile
  forbidden_card_types:
  - tenant
  - group
  - platform_account
  - account_data_binding
  - business_scope_set
  - business_flow_binding
  - bank_account
  - payment_gateway_account
  - statutory_tax_filing
  - logistics_account
  confidence: high
```


```yaml
source_evidence:
  id: ev.jiomart.returns.7_common_query_patterns
  source_section: 7. Common Query Patterns
  source_context: returns
  source_line_start: 869
  source_line_end: 869
  evidence_type: query_example
  supported_semantics:
  - Executable/source-backed SQL query pattern for 7. Common Query Patterns, including columns, filters, aggregation grain,
    and output aliases.
  unsupported_semantics:
  - Do not infer tenant/group/platform-account/bank/statutory-filing/external-logistics cards from this evidence.
  - Do not create metric implementations unless the SQL references documented tables/columns and required filters.
  allowed_card_types:
  - metric
  - metric_implementation
  - query_pattern
  - output_contract
  - validation_test
  - rule
  forbidden_card_types:
  - tenant
  - group
  - platform_account
  - account_data_binding
  - business_scope_set
  - business_flow_binding
  - bank_account
  - payment_gateway_account
  - statutory_tax_filing
  - logistics_account
  - non_executable_metric_implementation
  confidence: high
```


```yaml
source_evidence:
  id: ev.jiomart.returns.7_1_return_volume_by_type
  source_section: 7.1 Return Volume by Type
  source_context: returns
  source_line_start: 870
  source_line_end: 882
  evidence_type: prose
  supported_semantics:
  - Prose semantics from source section 7.1 Return Volume by Type.
  unsupported_semantics:
  - Do not infer tenant/group/platform-account/bank/statutory-filing/external-logistics cards from this evidence.
  allowed_card_types:
  - platform
  - platform_context
  - domain
  - business_process
  - workflow_step
  - rule
  - value_profile
  forbidden_card_types:
  - tenant
  - group
  - platform_account
  - account_data_binding
  - business_scope_set
  - business_flow_binding
  - bank_account
  - payment_gateway_account
  - statutory_tax_filing
  - logistics_account
  confidence: high
```


```yaml
source_evidence:
  id: ev.jiomart.returns.7_2_return_cycle_time_rto_turnaround
  source_section: 7.2 Return Cycle Time (RTO Turnaround)
  source_context: returns
  source_line_start: 883
  source_line_end: 897
  evidence_type: query_example
  supported_semantics:
  - Executable/source-backed SQL query pattern for 7.2 Return Cycle Time (RTO Turnaround), including columns, filters, aggregation
    grain, and output aliases.
  unsupported_semantics:
  - Do not infer tenant/group/platform-account/bank/statutory-filing/external-logistics cards from this evidence.
  - Do not create metric implementations unless the SQL references documented tables/columns and required filters.
  allowed_card_types:
  - metric
  - metric_implementation
  - query_pattern
  - output_contract
  - validation_test
  - rule
  forbidden_card_types:
  - tenant
  - group
  - platform_account
  - account_data_binding
  - business_scope_set
  - business_flow_binding
  - bank_account
  - payment_gateway_account
  - statutory_tax_filing
  - logistics_account
  - non_executable_metric_implementation
  confidence: high
```


```yaml
source_evidence:
  id: ev.jiomart.returns.7_3_returns_oms_reconciliation
  source_section: 7.3 Returns → OMS Reconciliation
  source_context: returns
  source_line_start: 898
  source_line_end: 912
  evidence_type: reconciliation_playbook
  supported_semantics:
  - Source-backed JioMart reconciliation logic for 7.3 Returns → OMS Reconciliation, including tables, join keys, filters,
    and output fields.
  unsupported_semantics:
  - Do not infer tenant/group/platform-account/bank/statutory-filing/external-logistics cards from this evidence.
  allowed_card_types:
  - reconciliation_profile
  - reconciliation_side
  - reconciliation_unit
  - matching_logic
  - mismatch_category
  - query_pattern
  - rule
  forbidden_card_types:
  - tenant
  - group
  - platform_account
  - account_data_binding
  - business_scope_set
  - business_flow_binding
  - bank_account
  - payment_gateway_account
  - statutory_tax_filing
  - logistics_account
  confidence: high
```


```yaml
source_evidence:
  id: ev.jiomart.returns.7_4_sku_level_return_rate
  source_section: 7.4 SKU-Level Return Rate
  source_context: returns
  source_line_start: 913
  source_line_end: 926
  evidence_type: query_example
  supported_semantics:
  - Executable/source-backed SQL query pattern for 7.4 SKU-Level Return Rate, including columns, filters, aggregation grain,
    and output aliases.
  unsupported_semantics:
  - Do not infer tenant/group/platform-account/bank/statutory-filing/external-logistics cards from this evidence.
  - Do not create metric implementations unless the SQL references documented tables/columns and required filters.
  allowed_card_types:
  - metric
  - metric_implementation
  - query_pattern
  - output_contract
  - validation_test
  - rule
  forbidden_card_types:
  - tenant
  - group
  - platform_account
  - account_data_binding
  - business_scope_set
  - business_flow_binding
  - bank_account
  - payment_gateway_account
  - statutory_tax_filing
  - logistics_account
  - non_executable_metric_implementation
  confidence: high
```


```yaml
source_evidence:
  id: ev.jiomart.oms.table_jiomart_oms_table_knowledge_base
  source_section: 'Table: JioMart OMS — Table Knowledge Base'
  source_context: oms
  source_line_start: 927
  source_line_end: 929
  evidence_type: prose
  supported_semantics:
  - 'Prose semantics from source section Table: JioMart OMS — Table Knowledge Base.'
  unsupported_semantics:
  - Do not infer tenant/group/platform-account/bank/statutory-filing/external-logistics cards from this evidence.
  allowed_card_types:
  - platform
  - platform_context
  - domain
  - business_process
  - workflow_step
  - rule
  - value_profile
  forbidden_card_types:
  - tenant
  - group
  - platform_account
  - account_data_binding
  - business_scope_set
  - business_flow_binding
  - bank_account
  - payment_gateway_account
  - statutory_tax_filing
  - logistics_account
  confidence: high
```


```yaml
source_evidence:
  id: ev.jiomart.oms.1_table_overview
  source_section: 1. Table Overview
  source_context: oms
  source_line_start: 930
  source_line_end: 934
  evidence_type: prose
  supported_semantics:
  - Prose semantics from source section 1. Table Overview.
  unsupported_semantics:
  - Do not infer tenant/group/platform-account/bank/statutory-filing/external-logistics cards from this evidence.
  allowed_card_types:
  - platform
  - platform_context
  - domain
  - business_process
  - workflow_step
  - rule
  - value_profile
  forbidden_card_types:
  - tenant
  - group
  - platform_account
  - account_data_binding
  - business_scope_set
  - business_flow_binding
  - bank_account
  - payment_gateway_account
  - statutory_tax_filing
  - logistics_account
  confidence: high
```


```yaml
source_evidence:
  id: ev.jiomart.oms.2_key_statistics
  source_section: 2. Key Statistics
  source_context: oms
  source_line_start: 935
  source_line_end: 956
  evidence_type: table
  supported_semantics:
  - Documented source values, observed distributions, benchmark/context tables, or table statistics for 2. Key Statistics.
  unsupported_semantics:
  - Do not infer tenant/group/platform-account/bank/statutory-filing/external-logistics cards from this evidence.
  allowed_card_types:
  - value_profile
  - column
  - metric
  - rule
  - table
  forbidden_card_types:
  - tenant
  - group
  - platform_account
  - account_data_binding
  - business_scope_set
  - business_flow_binding
  - bank_account
  - payment_gateway_account
  - statutory_tax_filing
  - logistics_account
  confidence: high
```


```yaml
source_evidence:
  id: ev.jiomart.oms.3_schema_details_115_columns
  source_section: 3. Schema Details (115 Columns)
  source_context: oms
  source_line_start: 957
  source_line_end: 957
  evidence_type: schema_reference
  supported_semantics:
  - oms source table schema columns, source-declared types, and descriptions.
  unsupported_semantics:
  - Do not infer tenant/group/platform-account/bank/statutory-filing/external-logistics cards from this evidence.
  allowed_card_types:
  - table
  - column
  - relationship
  - rule
  - validation_test
  forbidden_card_types:
  - tenant
  - group
  - platform_account
  - account_data_binding
  - business_scope_set
  - business_flow_binding
  - bank_account
  - payment_gateway_account
  - statutory_tax_filing
  - logistics_account
  confidence: high
```


```yaml
source_evidence:
  id: ev.jiomart.oms.3_1_identity_columns
  source_section: 3.1 Identity Columns
  source_context: oms
  source_line_start: 958
  source_line_end: 978
  evidence_type: prose
  supported_semantics:
  - Prose semantics from source section 3.1 Identity Columns.
  unsupported_semantics:
  - Do not infer tenant/group/platform-account/bank/statutory-filing/external-logistics cards from this evidence.
  allowed_card_types:
  - platform
  - platform_context
  - domain
  - business_process
  - workflow_step
  - rule
  - value_profile
  forbidden_card_types:
  - tenant
  - group
  - platform_account
  - account_data_binding
  - business_scope_set
  - business_flow_binding
  - bank_account
  - payment_gateway_account
  - statutory_tax_filing
  - logistics_account
  confidence: high
```


```yaml
source_evidence:
  id: ev.jiomart.oms.3_2_date_columns
  source_section: 3.2 Date Columns
  source_context: oms
  source_line_start: 979
  source_line_end: 986
  evidence_type: prose
  supported_semantics:
  - Prose semantics from source section 3.2 Date Columns.
  unsupported_semantics:
  - Do not infer tenant/group/platform-account/bank/statutory-filing/external-logistics cards from this evidence.
  allowed_card_types:
  - platform
  - platform_context
  - domain
  - business_process
  - workflow_step
  - rule
  - value_profile
  forbidden_card_types:
  - tenant
  - group
  - platform_account
  - account_data_binding
  - business_scope_set
  - business_flow_binding
  - bank_account
  - payment_gateway_account
  - statutory_tax_filing
  - logistics_account
  confidence: high
```


```yaml
source_evidence:
  id: ev.jiomart.oms.3_3_financial_columns
  source_section: 3.3 Financial Columns
  source_context: oms
  source_line_start: 987
  source_line_end: 996
  evidence_type: prose
  supported_semantics:
  - Prose semantics from source section 3.3 Financial Columns.
  unsupported_semantics:
  - Do not infer tenant/group/platform-account/bank/statutory-filing/external-logistics cards from this evidence.
  allowed_card_types:
  - platform
  - platform_context
  - domain
  - business_process
  - workflow_step
  - rule
  - value_profile
  forbidden_card_types:
  - tenant
  - group
  - platform_account
  - account_data_binding
  - business_scope_set
  - business_flow_binding
  - bank_account
  - payment_gateway_account
  - statutory_tax_filing
  - logistics_account
  confidence: high
```


```yaml
source_evidence:
  id: ev.jiomart.oms.3_4_tax_columns
  source_section: 3.4 Tax Columns
  source_context: oms
  source_line_start: 997
  source_line_end: 1012
  evidence_type: prose
  supported_semantics:
  - Prose semantics from source section 3.4 Tax Columns.
  unsupported_semantics:
  - Do not infer tenant/group/platform-account/bank/statutory-filing/external-logistics cards from this evidence.
  allowed_card_types:
  - platform
  - platform_context
  - domain
  - business_process
  - workflow_step
  - rule
  - value_profile
  forbidden_card_types:
  - tenant
  - group
  - platform_account
  - account_data_binding
  - business_scope_set
  - business_flow_binding
  - bank_account
  - payment_gateway_account
  - statutory_tax_filing
  - logistics_account
  confidence: high
```


```yaml
source_evidence:
  id: ev.jiomart.oms.3_5_tcs_tds_columns
  source_section: 3.5 TCS / TDS Columns
  source_context: oms
  source_line_start: 1013
  source_line_end: 1026
  evidence_type: prose
  supported_semantics:
  - Prose semantics from source section 3.5 TCS / TDS Columns.
  unsupported_semantics:
  - Do not infer tenant/group/platform-account/bank/statutory-filing/external-logistics cards from this evidence.
  allowed_card_types:
  - platform
  - platform_context
  - domain
  - business_process
  - workflow_step
  - rule
  - value_profile
  forbidden_card_types:
  - tenant
  - group
  - platform_account
  - account_data_binding
  - business_scope_set
  - business_flow_binding
  - bank_account
  - payment_gateway_account
  - statutory_tax_filing
  - logistics_account
  confidence: high
```


```yaml
source_evidence:
  id: ev.jiomart.oms.3_6_status_columns
  source_section: 3.6 Status Columns
  source_context: oms
  source_line_start: 1027
  source_line_end: 1037
  evidence_type: prose
  supported_semantics:
  - Prose semantics from source section 3.6 Status Columns.
  unsupported_semantics:
  - Do not infer tenant/group/platform-account/bank/statutory-filing/external-logistics cards from this evidence.
  allowed_card_types:
  - platform
  - platform_context
  - domain
  - business_process
  - workflow_step
  - rule
  - value_profile
  forbidden_card_types:
  - tenant
  - group
  - platform_account
  - account_data_binding
  - business_scope_set
  - business_flow_binding
  - bank_account
  - payment_gateway_account
  - statutory_tax_filing
  - logistics_account
  confidence: high
```


```yaml
source_evidence:
  id: ev.jiomart.oms.3_7_geographic_columns
  source_section: 3.7 Geographic Columns
  source_context: oms
  source_line_start: 1038
  source_line_end: 1048
  evidence_type: prose
  supported_semantics:
  - Prose semantics from source section 3.7 Geographic Columns.
  unsupported_semantics:
  - Do not infer tenant/group/platform-account/bank/statutory-filing/external-logistics cards from this evidence.
  allowed_card_types:
  - platform
  - platform_context
  - domain
  - business_process
  - workflow_step
  - rule
  - value_profile
  forbidden_card_types:
  - tenant
  - group
  - platform_account
  - account_data_binding
  - business_scope_set
  - business_flow_binding
  - bank_account
  - payment_gateway_account
  - statutory_tax_filing
  - logistics_account
  confidence: high
```


```yaml
source_evidence:
  id: ev.jiomart.oms.3_8_product_fulfilment_columns
  source_section: 3.8 Product / Fulfilment Columns
  source_context: oms
  source_line_start: 1049
  source_line_end: 1055
  evidence_type: prose
  supported_semantics:
  - Prose semantics from source section 3.8 Product / Fulfilment Columns.
  unsupported_semantics:
  - Do not infer tenant/group/platform-account/bank/statutory-filing/external-logistics cards from this evidence.
  - Scope, GSTIN, fulfilment, or payment labels remain columns, value profiles, caveats, or rules only.
  allowed_card_types:
  - platform
  - platform_context
  - domain
  - business_process
  - workflow_step
  - rule
  - value_profile
  forbidden_card_types:
  - tenant
  - group
  - platform_account
  - account_data_binding
  - business_scope_set
  - business_flow_binding
  - bank_account
  - payment_gateway_account
  - statutory_tax_filing
  - logistics_account
  - process_variant
  confidence: high
```


```yaml
source_evidence:
  id: ev.jiomart.oms.3_9_system_metadata
  source_section: 3.9 System / Metadata
  source_context: oms
  source_line_start: 1056
  source_line_end: 1066
  evidence_type: prose
  supported_semantics:
  - Prose semantics from source section 3.9 System / Metadata.
  unsupported_semantics:
  - Do not infer tenant/group/platform-account/bank/statutory-filing/external-logistics cards from this evidence.
  allowed_card_types:
  - platform
  - platform_context
  - domain
  - business_process
  - workflow_step
  - rule
  - value_profile
  forbidden_card_types:
  - tenant
  - group
  - platform_account
  - account_data_binding
  - business_scope_set
  - business_flow_binding
  - bank_account
  - payment_gateway_account
  - statutory_tax_filing
  - logistics_account
  confidence: high
```


```yaml
source_evidence:
  id: ev.jiomart.oms.4_distinct_value_analysis
  source_section: 4. Distinct Value Analysis
  source_context: oms
  source_line_start: 1067
  source_line_end: 1067
  evidence_type: table
  supported_semantics:
  - Documented source values, observed distributions, benchmark/context tables, or table statistics for 4. Distinct Value
    Analysis.
  unsupported_semantics:
  - Do not infer tenant/group/platform-account/bank/statutory-filing/external-logistics cards from this evidence.
  allowed_card_types:
  - value_profile
  - column
  - metric
  - rule
  - table
  forbidden_card_types:
  - tenant
  - group
  - platform_account
  - account_data_binding
  - business_scope_set
  - business_flow_binding
  - bank_account
  - payment_gateway_account
  - statutory_tax_filing
  - logistics_account
  confidence: high
```


```yaml
source_evidence:
  id: ev.jiomart.oms.transaction_type_order_status_financial_breakdown
  source_section: '`transaction_type` / `order_status` Financial Breakdown'
  source_context: oms
  source_line_start: 1068
  source_line_end: 1076
  evidence_type: prose
  supported_semantics:
  - Prose semantics from source section `transaction_type` / `order_status` Financial Breakdown.
  unsupported_semantics:
  - Do not infer tenant/group/platform-account/bank/statutory-filing/external-logistics cards from this evidence.
  allowed_card_types:
  - platform
  - platform_context
  - domain
  - business_process
  - workflow_step
  - rule
  - value_profile
  forbidden_card_types:
  - tenant
  - group
  - platform_account
  - account_data_binding
  - business_scope_set
  - business_flow_binding
  - bank_account
  - payment_gateway_account
  - statutory_tax_filing
  - logistics_account
  confidence: high
```


```yaml
source_evidence:
  id: ev.jiomart.oms.seller_gstins_warehouse_mapping
  source_section: Seller GSTINs → Warehouse Mapping
  source_context: oms
  source_line_start: 1077
  source_line_end: 1082
  evidence_type: table
  supported_semantics:
  - Documented source values, observed distributions, benchmark/context tables, or table statistics for Seller GSTINs → Warehouse
    Mapping.
  unsupported_semantics:
  - Do not infer tenant/group/platform-account/bank/statutory-filing/external-logistics cards from this evidence.
  - Scope, GSTIN, fulfilment, or payment labels remain columns, value profiles, caveats, or rules only.
  allowed_card_types:
  - value_profile
  - column
  - metric
  - rule
  - table
  forbidden_card_types:
  - tenant
  - group
  - platform_account
  - account_data_binding
  - business_scope_set
  - business_flow_binding
  - bank_account
  - payment_gateway_account
  - statutory_tax_filing
  - logistics_account
  - process_variant
  confidence: high
```


```yaml
source_evidence:
  id: ev.jiomart.oms.hsn_codes_and_products
  source_section: HSN Codes and Products
  source_context: oms
  source_line_start: 1083
  source_line_end: 1089
  evidence_type: table
  supported_semantics:
  - Documented source values, observed distributions, benchmark/context tables, or table statistics for HSN Codes and Products.
  unsupported_semantics:
  - Do not infer tenant/group/platform-account/bank/statutory-filing/external-logistics cards from this evidence.
  allowed_card_types:
  - value_profile
  - column
  - metric
  - rule
  - table
  forbidden_card_types:
  - tenant
  - group
  - platform_account
  - account_data_binding
  - business_scope_set
  - business_flow_binding
  - bank_account
  - payment_gateway_account
  - statutory_tax_filing
  - logistics_account
  confidence: high
```


```yaml
source_evidence:
  id: ev.jiomart.oms.top_skus_by_volume
  source_section: Top SKUs by Volume
  source_context: oms
  source_line_start: 1090
  source_line_end: 1097
  evidence_type: query_example
  supported_semantics:
  - Executable/source-backed SQL query pattern for Top SKUs by Volume, including columns, filters, aggregation grain, and
    output aliases.
  unsupported_semantics:
  - Do not infer tenant/group/platform-account/bank/statutory-filing/external-logistics cards from this evidence.
  - Do not create metric implementations unless the SQL references documented tables/columns and required filters.
  allowed_card_types:
  - metric
  - metric_implementation
  - query_pattern
  - output_contract
  - validation_test
  - rule
  forbidden_card_types:
  - tenant
  - group
  - platform_account
  - account_data_binding
  - business_scope_set
  - business_flow_binding
  - bank_account
  - payment_gateway_account
  - statutory_tax_filing
  - logistics_account
  - non_executable_metric_implementation
  confidence: high
```


```yaml
source_evidence:
  id: ev.jiomart.oms.seller_coupon_codes_observed
  source_section: Seller Coupon Codes Observed
  source_context: oms
  source_line_start: 1098
  source_line_end: 1099
  evidence_type: query_example
  supported_semantics:
  - Executable/source-backed SQL query pattern for Seller Coupon Codes Observed, including columns, filters, aggregation grain,
    and output aliases.
  unsupported_semantics:
  - Do not infer tenant/group/platform-account/bank/statutory-filing/external-logistics cards from this evidence.
  - Do not create metric implementations unless the SQL references documented tables/columns and required filters.
  allowed_card_types:
  - metric
  - metric_implementation
  - query_pattern
  - output_contract
  - validation_test
  - rule
  forbidden_card_types:
  - tenant
  - group
  - platform_account
  - account_data_binding
  - business_scope_set
  - business_flow_binding
  - bank_account
  - payment_gateway_account
  - statutory_tax_filing
  - logistics_account
  - non_executable_metric_implementation
  confidence: high
```


```yaml
source_evidence:
  id: ev.jiomart.oms.tcs_rates_observed
  source_section: TCS Rates Observed
  source_context: oms
  source_line_start: 1100
  source_line_end: 1102
  evidence_type: prose
  supported_semantics:
  - Prose semantics from source section TCS Rates Observed.
  unsupported_semantics:
  - Do not infer tenant/group/platform-account/bank/statutory-filing/external-logistics cards from this evidence.
  allowed_card_types:
  - platform
  - platform_context
  - domain
  - business_process
  - workflow_step
  - rule
  - value_profile
  forbidden_card_types:
  - tenant
  - group
  - platform_account
  - account_data_binding
  - business_scope_set
  - business_flow_binding
  - bank_account
  - payment_gateway_account
  - statutory_tax_filing
  - logistics_account
  confidence: high
```


```yaml
source_evidence:
  id: ev.jiomart.oms.5_sample_records
  source_section: 5. Sample Records
  source_context: oms
  source_line_start: 1103
  source_line_end: 1138
  evidence_type: prose
  supported_semantics:
  - Prose semantics from source section 5. Sample Records.
  unsupported_semantics:
  - Do not infer tenant/group/platform-account/bank/statutory-filing/external-logistics cards from this evidence.
  allowed_card_types:
  - platform
  - platform_context
  - domain
  - business_process
  - workflow_step
  - rule
  - value_profile
  forbidden_card_types:
  - tenant
  - group
  - platform_account
  - account_data_binding
  - business_scope_set
  - business_flow_binding
  - bank_account
  - payment_gateway_account
  - statutory_tax_filing
  - logistics_account
  confidence: high
```


```yaml
source_evidence:
  id: ev.jiomart.oms.6_data_quality_observations
  source_section: 6. Data Quality Observations
  source_context: oms
  source_line_start: 1139
  source_line_end: 1150
  evidence_type: caveat
  supported_semantics:
  - Data quality, mandatory-filter, or operational caveat semantics for 6. Data Quality Observations.
  unsupported_semantics:
  - Do not infer tenant/group/platform-account/bank/statutory-filing/external-logistics cards from this evidence.
  allowed_card_types:
  - rule
  - review_item
  - validation_test
  - value_profile
  forbidden_card_types:
  - tenant
  - group
  - platform_account
  - account_data_binding
  - business_scope_set
  - business_flow_binding
  - bank_account
  - payment_gateway_account
  - statutory_tax_filing
  - logistics_account
  confidence: high
```


```yaml
source_evidence:
  id: ev.jiomart.oms.7_common_query_patterns
  source_section: 7. Common Query Patterns
  source_context: oms
  source_line_start: 1151
  source_line_end: 1151
  evidence_type: query_example
  supported_semantics:
  - Executable/source-backed SQL query pattern for 7. Common Query Patterns, including columns, filters, aggregation grain,
    and output aliases.
  unsupported_semantics:
  - Do not infer tenant/group/platform-account/bank/statutory-filing/external-logistics cards from this evidence.
  - Do not create metric implementations unless the SQL references documented tables/columns and required filters.
  allowed_card_types:
  - metric
  - metric_implementation
  - query_pattern
  - output_contract
  - validation_test
  - rule
  forbidden_card_types:
  - tenant
  - group
  - platform_account
  - account_data_binding
  - business_scope_set
  - business_flow_binding
  - bank_account
  - payment_gateway_account
  - statutory_tax_filing
  - logistics_account
  - non_executable_metric_implementation
  confidence: high
```


```yaml
source_evidence:
  id: ev.jiomart.oms.7_1_monthly_gmv_clean_rows_only
  source_section: 7.1 Monthly GMV (Clean Rows Only)
  source_context: oms
  source_line_start: 1152
  source_line_end: 1165
  evidence_type: query_example
  supported_semantics:
  - Executable/source-backed SQL query pattern for 7.1 Monthly GMV (Clean Rows Only), including columns, filters, aggregation
    grain, and output aliases.
  unsupported_semantics:
  - Do not infer tenant/group/platform-account/bank/statutory-filing/external-logistics cards from this evidence.
  - Do not create metric implementations unless the SQL references documented tables/columns and required filters.
  allowed_card_types:
  - metric
  - metric_implementation
  - query_pattern
  - output_contract
  - validation_test
  - rule
  forbidden_card_types:
  - tenant
  - group
  - platform_account
  - account_data_binding
  - business_scope_set
  - business_flow_binding
  - bank_account
  - payment_gateway_account
  - statutory_tax_filing
  - logistics_account
  - non_executable_metric_implementation
  confidence: high
```


```yaml
source_evidence:
  id: ev.jiomart.oms.7_2_clean_forward_orders_exclude_column_shifted_rows
  source_section: 7.2 Clean Forward Orders (Exclude Column-Shifted Rows)
  source_context: oms
  source_line_start: 1166
  source_line_end: 1174
  evidence_type: prose
  supported_semantics:
  - Prose semantics from source section 7.2 Clean Forward Orders (Exclude Column-Shifted Rows).
  unsupported_semantics:
  - Do not infer tenant/group/platform-account/bank/statutory-filing/external-logistics cards from this evidence.
  allowed_card_types:
  - platform
  - platform_context
  - domain
  - business_process
  - workflow_step
  - rule
  - value_profile
  forbidden_card_types:
  - tenant
  - group
  - platform_account
  - account_data_binding
  - business_scope_set
  - business_flow_binding
  - bank_account
  - payment_gateway_account
  - statutory_tax_filing
  - logistics_account
  confidence: high
```


```yaml
source_evidence:
  id: ev.jiomart.oms.7_3_intra_state_vs_inter_state_gst_analysis
  source_section: 7.3 Intra-State vs Inter-State GST Analysis
  source_context: oms
  source_line_start: 1175
  source_line_end: 1191
  evidence_type: prose
  supported_semantics:
  - Prose semantics from source section 7.3 Intra-State vs Inter-State GST Analysis.
  unsupported_semantics:
  - Do not infer tenant/group/platform-account/bank/statutory-filing/external-logistics cards from this evidence.
  allowed_card_types:
  - platform
  - platform_context
  - domain
  - business_process
  - workflow_step
  - rule
  - value_profile
  forbidden_card_types:
  - tenant
  - group
  - platform_account
  - account_data_binding
  - business_scope_set
  - business_flow_binding
  - bank_account
  - payment_gateway_account
  - statutory_tax_filing
  - logistics_account
  confidence: high
```


```yaml
source_evidence:
  id: ev.jiomart.oms.7_4_sku_level_performance
  source_section: 7.4 SKU-Level Performance
  source_context: oms
  source_line_start: 1192
  source_line_end: 1204
  evidence_type: prose
  supported_semantics:
  - Prose semantics from source section 7.4 SKU-Level Performance.
  unsupported_semantics:
  - Do not infer tenant/group/platform-account/bank/statutory-filing/external-logistics cards from this evidence.
  allowed_card_types:
  - platform
  - platform_context
  - domain
  - business_process
  - workflow_step
  - rule
  - value_profile
  forbidden_card_types:
  - tenant
  - group
  - platform_account
  - account_data_binding
  - business_scope_set
  - business_flow_binding
  - bank_account
  - payment_gateway_account
  - statutory_tax_filing
  - logistics_account
  confidence: high
```


```yaml
source_evidence:
  id: ev.jiomart.oms.7_5_oms_settlement_join
  source_section: 7.5 OMS → Settlement Join
  source_context: oms
  source_line_start: 1205
  source_line_end: 1220
  evidence_type: prose
  supported_semantics:
  - Prose semantics from source section 7.5 OMS → Settlement Join.
  unsupported_semantics:
  - Do not infer tenant/group/platform-account/bank/statutory-filing/external-logistics cards from this evidence.
  allowed_card_types:
  - platform
  - platform_context
  - domain
  - business_process
  - workflow_step
  - rule
  - value_profile
  forbidden_card_types:
  - tenant
  - group
  - platform_account
  - account_data_binding
  - business_scope_set
  - business_flow_binding
  - bank_account
  - payment_gateway_account
  - statutory_tax_filing
  - logistics_account
  confidence: high
```


```yaml
source_evidence:
  id: ev.jiomart.oms.7_6_return_rate
  source_section: 7.6 Return Rate
  source_context: oms
  source_line_start: 1221
  source_line_end: 1232
  evidence_type: query_example
  supported_semantics:
  - Executable/source-backed SQL query pattern for 7.6 Return Rate, including columns, filters, aggregation grain, and output
    aliases.
  unsupported_semantics:
  - Do not infer tenant/group/platform-account/bank/statutory-filing/external-logistics cards from this evidence.
  - Do not create metric implementations unless the SQL references documented tables/columns and required filters.
  allowed_card_types:
  - metric
  - metric_implementation
  - query_pattern
  - output_contract
  - validation_test
  - rule
  forbidden_card_types:
  - tenant
  - group
  - platform_account
  - account_data_binding
  - business_scope_set
  - business_flow_binding
  - bank_account
  - payment_gateway_account
  - statutory_tax_filing
  - logistics_account
  - non_executable_metric_implementation
  confidence: high
```


## 3. SQL Pattern Registry


```yaml
sql_pattern:
  id: sql.jiomart.marketplace.6_1_total_gmv
  source_section: 6.1 Total GMV
  source_context: marketplace
  source_line_start: 172
  source_line_end: 180
  evidence_ref: ev.jiomart.marketplace.6_1_total_gmv
  sql_pattern: |-
    SELECT
      SUM(CASE WHEN transaction_type = 'forward' THEN charged_amount ELSE 0 END) AS forward_gmv,
      SUM(CASE WHEN transaction_type = 'reverse' THEN ABS(charged_amount) ELSE 0 END) AS reversed_gmv,
      SUM(charged_amount) AS net_gmv
    FROM zs_observe.jiomart_oms
    WHERE is_active = true;
    -- Forward GMV: ~₹1.63 Cr | Reversed: ~₹22.4L | Net: ~₹1.40 Cr
  required_tables:
  - table.zs_observe.jiomart_oms
  output_aliases_detected:
  - forward_gmv
  - reversed_gmv
  - net_gmv
  confidence: high
```


```yaml
sql_pattern:
  id: sql.jiomart.marketplace.6_2_return_rate
  source_section: 6.2 Return Rate
  source_context: marketplace
  source_line_start: 182
  source_line_end: 191
  evidence_ref: ev.jiomart.marketplace.6_2_return_rate
  sql_pattern: |-
    SELECT
      ROUND(100.0 * COUNT_IF(order_status = 'shipment_returned')
        / NULLIF(COUNT_IF(transaction_type = 'forward'), 0), 2) AS rto_rate_pct,
      ROUND(100.0 * COUNT_IF(transaction_type = 'reverse')
        / NULLIF(COUNT_IF(transaction_type = 'forward'), 0), 2) AS return_reversal_pct
    FROM zs_observe.jiomart_oms
    WHERE is_active = true;
    -- RTO rate: ~14.8% | Return reversal rate: ~13.8%
  required_tables:
  - table.zs_observe.jiomart_oms
  output_aliases_detected:
  - rto_rate_pct
  - return_reversal_pct
  confidence: high
```


```yaml
sql_pattern:
  id: sql.jiomart.marketplace.6_3_average_order_value_aov
  source_section: 6.3 Average Order Value (AOV)
  source_context: marketplace
  source_line_start: 193
  source_line_end: 200
  evidence_ref: ev.jiomart.marketplace.6_3_average_order_value_aov
  sql_pattern: |-
    SELECT AVG(charged_amount) AS aov
    FROM zs_observe.jiomart_oms
    WHERE is_active = true
      AND transaction_type = 'forward'
      AND order_status = 'delivered';
    -- Observed: ₹273.83
  required_tables:
  - table.zs_observe.jiomart_oms
  output_aliases_detected:
  - aov
  confidence: high
```


```yaml
sql_pattern:
  id: sql.jiomart.marketplace.6_4_net_settled_revenue
  source_section: 6.4 Net Settled Revenue
  source_context: marketplace
  source_line_start: 202
  source_line_end: 210
  evidence_ref: ev.jiomart.marketplace.6_4_net_settled_revenue
  sql_pattern: |-
    SELECT
      SUM(CASE WHEN accountable_type = 'Receivable' THEN settled_amount ELSE 0 END) AS gross_receivable,
      SUM(CASE WHEN accountable_type = 'BaseTcs' THEN settled_amount ELSE 0 END) AS tcs_net,
      SUM(CASE WHEN accountable_type = 'Tds' THEN settled_amount ELSE 0 END) AS tds_net,
      SUM(settled_amount) AS net_settled
    FROM zs_observe.jiomart_settlement
    WHERE is_active = true AND event IS NOT NULL;
  required_tables:
  - table.zs_observe.jiomart_settlement
  output_aliases_detected:
  - gross_receivable
  - tcs_net
  - tds_net
  - net_settled
  confidence: high
```


```yaml
sql_pattern:
  id: sql.jiomart.marketplace.6_5_seller_coupon_discount_impact
  source_section: 6.5 Seller Coupon Discount Impact
  source_context: marketplace
  source_line_start: 212
  source_line_end: 222
  evidence_ref: ev.jiomart.marketplace.6_5_seller_coupon_discount_impact
  sql_pattern: |-
    SELECT
      seller_coupon_code,
      COUNT(*) AS orders,
      SUM(ABS(COALESCE(CAST(seller_coupon_amount AS DOUBLE), 0))) AS total_discount
    FROM zs_observe.jiomart_oms
    WHERE is_active = true
      AND seller_coupon_code IS NOT NULL
    GROUP BY seller_coupon_code
    ORDER BY total_discount DESC;
  required_tables:
  - table.zs_observe.jiomart_oms
  output_aliases_detected:
  - orders
  - DOUBLE
  - total_discount
  confidence: high
```


```yaml
sql_pattern:
  id: sql.jiomart.marketplace.6_6_monthly_forward_orders_and_gmv
  source_section: 6.6 Monthly Forward Orders and GMV
  source_context: marketplace
  source_line_start: 224
  source_line_end: 233
  evidence_ref: ev.jiomart.marketplace.6_6_monthly_forward_orders_and_gmv
  sql_pattern: |-
    SELECT
      CAST(DATE_TRUNC('month', CAST(created_date AS TIMESTAMP)) AS DATE) AS month,
      COUNT(*) AS orders,
      SUM(charged_amount) AS gmv,
      AVG(charged_amount) AS aov
    FROM zs_observe.jiomart_oms
    WHERE is_active = true AND transaction_type = 'forward'
    GROUP BY 1 ORDER BY 1;
  required_tables:
  - table.zs_observe.jiomart_oms
  output_aliases_detected:
  - TIMESTAMP
  - DATE
  - month
  - orders
  - gmv
  - aov
  confidence: high
```


```yaml
sql_pattern:
  id: sql.jiomart.marketplace.7_1_oms_settlement_match_3_way_per_order
  source_section: 7.1 OMS → Settlement Match (3-Way Per Order)
  source_context: marketplace
  source_line_start: 237
  source_line_end: 255
  evidence_ref: ev.jiomart.marketplace.7_1_oms_settlement_match_3_way_per_order
  sql_pattern: |-
    SELECT
      o.order_id,
      o.charged_amount AS oms_gmv,
      o.total_tcs_amount AS oms_tcs,
      o.total_tds AS oms_tds,
      SUM(CASE WHEN s.accountable_type = 'Receivable' THEN s.settled_amount ELSE 0 END) AS stl_receivable,
      SUM(CASE WHEN s.accountable_type = 'BaseTcs' THEN s.settled_amount ELSE 0 END) AS stl_tcs,
      SUM(CASE WHEN s.accountable_type = 'Tds' THEN s.settled_amount ELSE 0 END) AS stl_tds,
      ROUND(o.total_tcs_amount + SUM(CASE WHEN s.accountable_type='BaseTcs' THEN s.settled_amount ELSE 0 END), 4) AS tcs_variance
    FROM zs_observe.jiomart_oms o
    LEFT JOIN zs_observe.jiomart_settlement s
      ON o.order_id = s.order_id AND s.is_active = true AND s.event IS NOT NULL
    WHERE o.is_active = true
      AND o.transaction_type = 'forward'
      AND o.order_status = 'delivered'
      AND o.hsn IS NOT NULL
    GROUP BY o.order_id, o.charged_amount, o.total_tcs_amount, o.total_tds;
  required_tables:
  - table.zs_observe.jiomart_oms
  - table.zs_observe.jiomart_settlement
  output_aliases_detected:
  - oms_gmv
  - oms_tcs
  - oms_tds
  - stl_receivable
  - stl_tcs
  - stl_tds
  - tcs_variance
  confidence: high
```


```yaml
sql_pattern:
  id: sql.jiomart.marketplace.7_2_returns_oms_settlement_full_chain
  source_section: 7.2 Returns → OMS → Settlement Full Chain
  source_context: marketplace
  source_line_start: 257
  source_line_end: 269
  evidence_ref: ev.jiomart.marketplace.7_2_returns_oms_settlement_full_chain
  sql_pattern: |-
    SELECT
      r.order_id,
      r.return_type,
      CAST(r.refund_amount AS DOUBLE) AS refund_issued,
      o.charged_amount AS original_sale,
      SUM(s.settled_amount) AS settlement_net
    FROM zs_observe.jiomart_returns r
    LEFT JOIN zs_observe.jiomart_oms o ON r.order_id = o.order_id AND o.is_active = true
    LEFT JOIN zs_observe.jiomart_settlement s ON r.order_id = s.order_id AND s.is_active = true
    WHERE r.is_active = true AND r.return_type IS NOT NULL
    GROUP BY r.order_id, r.return_type, r.refund_amount, o.charged_amount;
  required_tables:
  - table.zs_observe.jiomart_oms
  - table.zs_observe.jiomart_returns
  - table.zs_observe.jiomart_settlement
  output_aliases_detected:
  - DOUBLE
  - refund_issued
  - original_sale
  - settlement_net
  confidence: high
```


```yaml
sql_pattern:
  id: sql.jiomart.marketplace.7_3_unreconciled_oms_orders_not_in_settlement
  source_section: 7.3 Unreconciled OMS Orders (Not in Settlement)
  source_context: marketplace
  source_line_start: 271
  source_line_end: 282
  evidence_ref: ev.jiomart.marketplace.7_3_unreconciled_oms_orders_not_in_settlement
  sql_pattern: |-
    SELECT o.order_id, o.invoice_number, o.charged_amount, o.order_status
    FROM zs_observe.jiomart_oms o
    LEFT JOIN zs_observe.jiomart_settlement s
      ON o.order_id = s.order_id AND s.is_active = true
    WHERE o.is_active = true
      AND o.transaction_type = 'forward'
      AND o.order_status = 'delivered'
      AND o.hsn IS NOT NULL
      AND s.order_id IS NULL;
    -- Coverage gap: ~944 orders (1.6%)
  required_tables:
  - table.zs_observe.jiomart_oms
  - table.zs_observe.jiomart_settlement
  output_aliases_detected: []
  confidence: high
```


```yaml
sql_pattern:
  id: sql.jiomart.marketplace.7_4_tcs_reconciliation
  source_section: 7.4 TCS Reconciliation
  source_context: marketplace
  source_line_start: 284
  source_line_end: 295
  evidence_ref: ev.jiomart.marketplace.7_4_tcs_reconciliation
  sql_pattern: |-
    SELECT 'OMS TCS' AS source, SUM(total_tcs_amount) AS amount
    FROM zs_observe.jiomart_oms WHERE is_active = true AND transaction_type = 'forward'
    UNION ALL
    SELECT 'Settlement BaseTcs (Forward)', SUM(settled_amount)
    FROM zs_observe.jiomart_settlement
    WHERE is_active = true AND accountable_type = 'BaseTcs' AND transaction_type = 'forward'
    UNION ALL
    SELECT 'Settlement BaseTcs (Return Reversal)', SUM(settled_amount)
    FROM zs_observe.jiomart_settlement
    WHERE is_active = true AND accountable_type = 'BaseTcs' AND transaction_type = 'reverse';
  required_tables:
  - table.zs_observe.jiomart_oms
  - table.zs_observe.jiomart_settlement
  output_aliases_detected:
  - source
  - amount
  confidence: high
```


```yaml
sql_pattern:
  id: sql.jiomart.marketplace.9_mandatory_query_filters
  source_section: 9. Mandatory Query Filters
  source_context: marketplace
  source_line_start: 312
  source_line_end: 322
  evidence_ref: ev.jiomart.marketplace.9_mandatory_query_filters
  sql_pattern: |-
    -- jiomart_oms, jiomart_returns, jiomart_settlement (group 26 — MYFITNESS)
    WHERE is_active = true
      AND group_level_id = 26
    -- jiomart_oms — additional filter for clean rows
      AND hsn IS NOT NULL   -- removes column-shifted older rows
    -- jiomart_shipment (group 221 — ARDEUR FASHIONS)
    WHERE is_active = true
      AND group_level_id = 221
      AND qty > 0   -- removes cancelled orders
  required_tables: []
  output_aliases_detected: []
  confidence: high
```


```yaml
sql_pattern:
  id: sql.jiomart.shipment.7_1_shipment_status_summary
  source_section: 7.1 Shipment Status Summary
  source_context: shipment
  source_line_start: 442
  source_line_end: 453
  evidence_ref: ev.jiomart.shipment.7_1_shipment_status_summary
  sql_pattern: |-
    SELECT order_status,
      COUNT(*) AS cnt,
      SUM(charged_amount) AS gmv,
      SUM(mrp) AS total_mrp,
      SUM(item_promo_discount) AS total_discount,
      AVG(charged_amount) AS avg_selling_price,
      ROUND(100.0 * AVG(item_promo_discount) / NULLIF(AVG(mrp), 0), 2) AS avg_discount_pct
    FROM zs_observe.jiomart_shipment
    WHERE is_active = true
    GROUP BY order_status;
  required_tables:
  - table.zs_observe.jiomart_shipment
  output_aliases_detected:
  - cnt
  - gmv
  - total_mrp
  - total_discount
  - avg_selling_price
  - avg_discount_pct
  confidence: high
```


```yaml
sql_pattern:
  id: sql.jiomart.shipment.7_2_monthly_gmv
  source_section: 7.2 Monthly GMV
  source_context: shipment
  source_line_start: 455
  source_line_end: 464
  evidence_ref: ev.jiomart.shipment.7_2_monthly_gmv
  sql_pattern: |-
    SELECT
      CAST(DATE_TRUNC('month', CAST(created_date AS TIMESTAMP)) AS DATE) AS month,
      COUNT(*) AS shipments,
      SUM(charged_amount) AS gmv,
      SUM(item_promo_discount) AS promo_discount
    FROM zs_observe.jiomart_shipment
    WHERE is_active = true AND qty > 0
    GROUP BY 1 ORDER BY 1;
  required_tables:
  - table.zs_observe.jiomart_shipment
  output_aliases_detected:
  - TIMESTAMP
  - DATE
  - month
  - shipments
  - gmv
  - promo_discount
  confidence: high
```


```yaml
sql_pattern:
  id: sql.jiomart.shipment.7_3_top_skus
  source_section: 7.3 Top SKUs
  source_context: shipment
  source_line_start: 466
  source_line_end: 477
  evidence_ref: ev.jiomart.shipment.7_3_top_skus
  sql_pattern: |-
    SELECT sku_id,
      COUNT(*) AS orders,
      SUM(charged_amount) AS gmv,
      AVG(charged_amount) AS avg_price,
      AVG(item_promo_discount) AS avg_discount
    FROM zs_observe.jiomart_shipment
    WHERE is_active = true AND qty > 0
    GROUP BY sku_id
    ORDER BY gmv DESC
    LIMIT 20;
  required_tables:
  - table.zs_observe.jiomart_shipment
  output_aliases_detected:
  - orders
  - gmv
  - avg_price
  - avg_discount
  confidence: high
```


```yaml
sql_pattern:
  id: sql.jiomart.settlement.8_1_net_settlement_per_order_structured_rows
  source_section: 8.1 Net Settlement per Order (Structured Rows)
  source_context: settlement
  source_line_start: 637
  source_line_end: 649
  evidence_ref: ev.jiomart.settlement.8_1_net_settlement_per_order_structured_rows
  sql_pattern: |-
    SELECT
      order_id,
      SUM(CASE WHEN accountable_type = 'Receivable' THEN settled_amount ELSE 0 END) AS sale_proceeds,
      SUM(CASE WHEN accountable_type = 'BaseTcs' THEN settled_amount ELSE 0 END) AS tcs_impact,
      SUM(CASE WHEN accountable_type = 'Tds' THEN settled_amount ELSE 0 END) AS tds_impact,
      SUM(settled_amount) AS net_settled
    FROM zs_observe.jiomart_settlement
    WHERE is_active = true AND event IS NOT NULL
    GROUP BY order_id
    ORDER BY net_settled DESC
    LIMIT 20;
  required_tables:
  - table.zs_observe.jiomart_settlement
  output_aliases_detected:
  - sale_proceeds
  - tcs_impact
  - tds_impact
  - net_settled
  confidence: high
```


```yaml
sql_pattern:
  id: sql.jiomart.settlement.8_2_monthly_settlement_summary
  source_section: 8.2 Monthly Settlement Summary
  source_context: settlement
  source_line_start: 651
  source_line_end: 662
  evidence_ref: ev.jiomart.settlement.8_2_monthly_settlement_summary
  sql_pattern: |-
    SELECT
      DATE_TRUNC('month', settlement_date) AS month,
      transaction_type,
      accountable_type,
      COUNT(*) AS rows,
      SUM(settled_amount) AS total_settled
    FROM zs_observe.jiomart_settlement
    WHERE is_active = true AND event IS NOT NULL
    GROUP BY 1, 2, 3
    ORDER BY 1, 2, 3;
  required_tables:
  - table.zs_observe.jiomart_settlement
  output_aliases_detected:
  - month
  - rows
  - total_settled
  confidence: high
```


```yaml
sql_pattern:
  id: sql.jiomart.settlement.8_3_settlement_oms_reconciliation
  source_section: 8.3 Settlement ↔ OMS Reconciliation
  source_context: settlement
  source_line_start: 664
  source_line_end: 684
  evidence_ref: ev.jiomart.settlement.8_3_settlement_oms_reconciliation
  sql_pattern: |-
    SELECT
      o.order_id,
      o.charged_amount AS oms_gmv,
      o.total_tcs_amount AS oms_tcs,
      o.total_tds AS oms_tds,
      SUM(CASE WHEN s.accountable_type = 'Receivable' THEN s.settled_amount ELSE 0 END) AS settled_receivable,
      SUM(CASE WHEN s.accountable_type = 'BaseTcs' THEN s.settled_amount ELSE 0 END) AS settled_tcs,
      SUM(CASE WHEN s.accountable_type = 'Tds' THEN s.settled_amount ELSE 0 END) AS settled_tds,
      CASE WHEN SUM(s.settled_amount) IS NULL THEN 'Not in Settlement' ELSE 'Matched' END AS status
    FROM zs_observe.jiomart_oms o
    LEFT JOIN zs_observe.jiomart_settlement s
      ON o.order_id = s.order_id
      AND s.is_active = true
      AND s.event IS NOT NULL
    WHERE o.is_active = true
      AND o.transaction_type = 'forward'
      AND o.order_status = 'delivered'
      AND o.hsn IS NOT NULL
    GROUP BY o.order_id, o.charged_amount, o.total_tcs_amount, o.total_tds;
  required_tables:
  - table.zs_observe.jiomart_oms
  - table.zs_observe.jiomart_settlement
  output_aliases_detected:
  - oms_gmv
  - oms_tcs
  - oms_tds
  - settled_receivable
  - settled_tcs
  - settled_tds
  - status
  confidence: high
```


```yaml
sql_pattern:
  id: sql.jiomart.settlement.8_4_tcs_reconciliation_oms_vs_settlement
  source_section: 8.4 TCS Reconciliation (OMS vs Settlement)
  source_context: settlement
  source_line_start: 686
  source_line_end: 694
  evidence_ref: ev.jiomart.settlement.8_4_tcs_reconciliation_oms_vs_settlement
  sql_pattern: |-
    SELECT
      'OMS TCS' AS source, SUM(total_tcs_amount) AS total
    FROM zs_observe.jiomart_oms WHERE is_active = true AND transaction_type = 'forward'
    UNION ALL
    SELECT 'Settlement BaseTcs', SUM(settled_amount)
    FROM zs_observe.jiomart_settlement
    WHERE is_active = true AND accountable_type = 'BaseTcs' AND transaction_type = 'forward';
  required_tables:
  - table.zs_observe.jiomart_oms
  - table.zs_observe.jiomart_settlement
  output_aliases_detected:
  - source
  - total
  confidence: high
```


```yaml
sql_pattern:
  id: sql.jiomart.settlement.8_5_credit_debit_notes
  source_section: 8.5 Credit / Debit Notes
  source_context: settlement
  source_line_start: 696
  source_line_end: 705
  evidence_ref: ev.jiomart.settlement.8_5_credit_debit_notes
  sql_pattern: |-
    SELECT
      transaction_type, event, accountable_type,
      COUNT(*) AS cnt,
      SUM(settled_amount) AS total
    FROM zs_observe.jiomart_settlement
    WHERE is_active = true
      AND transaction_type IN ('Credit Note', 'Debit Note', 'Service Invoice', 'Bill Tds Refund')
    GROUP BY 1, 2, 3;
  required_tables:
  - table.zs_observe.jiomart_settlement
  output_aliases_detected:
  - cnt
  - total
  confidence: high
```


```yaml
sql_pattern:
  id: sql.jiomart.returns.7_1_return_volume_by_type
  source_section: 7.1 Return Volume by Type
  source_context: returns
  source_line_start: 871
  source_line_end: 882
  evidence_ref: ev.jiomart.returns.7_1_return_volume_by_type
  sql_pattern: |-
    SELECT
      COALESCE(return_type, 'Unknown/Old Format') AS return_type,
      return_status,
      COUNT(*) AS cnt,
      SUM(CAST(charged_amount AS DOUBLE)) AS total_charged,
      SUM(CAST(refund_amount AS DOUBLE)) AS total_refund
    FROM zs_observe.jiomart_returns
    WHERE is_active = true
    GROUP BY 1, 2
    ORDER BY cnt DESC;
  required_tables:
  - table.zs_observe.jiomart_returns
  output_aliases_detected:
  - return_type
  - cnt
  - DOUBLE
  - total_charged
  - DOUBLE
  - total_refund
  confidence: high
```


```yaml
sql_pattern:
  id: sql.jiomart.returns.7_2_return_cycle_time_rto_turnaround
  source_section: 7.2 Return Cycle Time (RTO Turnaround)
  source_context: returns
  source_line_start: 884
  source_line_end: 897
  evidence_ref: ev.jiomart.returns.7_2_return_cycle_time_rto_turnaround
  sql_pattern: |-
    SELECT
      courier_partner,
      COUNT(*) AS returns,
      AVG(DATE_DIFF('day',
        CAST(return_initiate_date AS TIMESTAMP),
        CAST(return_delivery_date AS TIMESTAMP))) AS avg_days_to_warehouse
    FROM zs_observe.jiomart_returns
    WHERE is_active = true
      AND return_type = 'ReturnToOrigin'
      AND return_initiate_date IS NOT NULL
      AND return_delivery_date IS NOT NULL
    GROUP BY courier_partner;
  required_tables:
  - table.zs_observe.jiomart_returns
  output_aliases_detected:
  - returns
  - TIMESTAMP
  - TIMESTAMP
  - avg_days_to_warehouse
  confidence: high
```


```yaml
sql_pattern:
  id: sql.jiomart.returns.7_3_returns_oms_reconciliation
  source_section: 7.3 Returns → OMS Reconciliation
  source_context: returns
  source_line_start: 899
  source_line_end: 912
  evidence_ref: ev.jiomart.returns.7_3_returns_oms_reconciliation
  sql_pattern: |-
    SELECT
      r.order_id, r.invoice_number,
      r.return_type,
      CAST(r.charged_amount AS DOUBLE) AS return_charged,
      CAST(r.refund_amount AS DOUBLE) AS refund,
      o.charged_amount AS oms_original_amount,
      o.order_status AS oms_status
    FROM zs_observe.jiomart_returns r
    LEFT JOIN zs_observe.jiomart_oms o
      ON r.order_id = o.order_id
      AND o.is_active = true
    WHERE r.is_active = true;
  required_tables:
  - table.zs_observe.jiomart_oms
  - table.zs_observe.jiomart_returns
  output_aliases_detected:
  - DOUBLE
  - return_charged
  - DOUBLE
  - refund
  - oms_original_amount
  - oms_status
  confidence: high
```


```yaml
sql_pattern:
  id: sql.jiomart.returns.7_4_sku_level_return_rate
  source_section: 7.4 SKU-Level Return Rate
  source_context: returns
  source_line_start: 914
  source_line_end: 923
  evidence_ref: ev.jiomart.returns.7_4_sku_level_return_rate
  sql_pattern: |-
    SELECT
      r.sku_id,
      COUNT(*) AS returns,
      SUM(CAST(r.charged_amount AS DOUBLE)) AS returned_value
    FROM zs_observe.jiomart_returns r
    WHERE r.is_active = true
    GROUP BY r.sku_id
    ORDER BY returns DESC;
  required_tables:
  - table.zs_observe.jiomart_returns
  output_aliases_detected:
  - returns
  - DOUBLE
  - returned_value
  confidence: high
```


```yaml
sql_pattern:
  id: sql.jiomart.oms.7_1_monthly_gmv_clean_rows_only
  source_section: 7.1 Monthly GMV (Clean Rows Only)
  source_context: oms
  source_line_start: 1153
  source_line_end: 1165
  evidence_ref: ev.jiomart.oms.7_1_monthly_gmv_clean_rows_only
  sql_pattern: |-
    SELECT
      CAST(DATE_TRUNC('month', CAST(created_date AS TIMESTAMP)) AS DATE) AS month,
      transaction_type,
      COUNT(*) AS orders,
      SUM(charged_amount) AS gmv,
      SUM(total_tcs_amount) AS tcs,
      SUM(total_tds) AS tds
    FROM zs_observe.jiomart_oms
    WHERE is_active = true
    GROUP BY 1, 2
    ORDER BY 1, 2;
  required_tables:
  - table.zs_observe.jiomart_oms
  output_aliases_detected:
  - TIMESTAMP
  - DATE
  - month
  - orders
  - gmv
  - tcs
  - tds
  confidence: high
```


```yaml
sql_pattern:
  id: sql.jiomart.oms.7_2_clean_forward_orders_exclude_column_shifted_rows
  source_section: 7.2 Clean Forward Orders (Exclude Column-Shifted Rows)
  source_context: oms
  source_line_start: 1167
  source_line_end: 1174
  evidence_ref: ev.jiomart.oms.7_2_clean_forward_orders_exclude_column_shifted_rows
  sql_pattern: |-
    SELECT *
    FROM zs_observe.jiomart_oms
    WHERE is_active = true
      AND transaction_type = 'forward'
      AND order_status = 'delivered'
      AND hsn IS NOT NULL;
  required_tables:
  - table.zs_observe.jiomart_oms
  output_aliases_detected: []
  confidence: high
```


```yaml
sql_pattern:
  id: sql.jiomart.oms.7_3_intra_state_vs_inter_state_gst_analysis
  source_section: 7.3 Intra-State vs Inter-State GST Analysis
  source_context: oms
  source_line_start: 1176
  source_line_end: 1191
  evidence_ref: ev.jiomart.oms.7_3_intra_state_vs_inter_state_gst_analysis
  sql_pattern: |-
    SELECT
      CASE
        WHEN UPPER(source_state) = UPPER(destination_state) THEN 'Intra-State'
        ELSE 'Inter-State'
      END AS gst_type,
      COUNT(*) AS cnt,
      SUM(charged_amount) AS gmv,
      SUM(tax_igst_amount) AS igst,
      SUM(tax_cgst_amount + tax_sgst_amount) AS cgst_sgst
    FROM zs_observe.jiomart_oms
    WHERE is_active = true
      AND transaction_type = 'forward'
      AND hsn IS NOT NULL
    GROUP BY 1;
  required_tables:
  - table.zs_observe.jiomart_oms
  output_aliases_detected:
  - gst_type
  - cnt
  - gmv
  - igst
  - cgst_sgst
  confidence: high
```


```yaml
sql_pattern:
  id: sql.jiomart.oms.7_4_sku_level_performance
  source_section: 7.4 SKU-Level Performance
  source_context: oms
  source_line_start: 1193
  source_line_end: 1204
  evidence_ref: ev.jiomart.oms.7_4_sku_level_performance
  sql_pattern: |-
    SELECT sku_id, mp_sin,
      COUNT(*) AS orders,
      SUM(charged_amount) AS gmv,
      AVG(charged_amount) AS avg_price,
      ROUND(100.0 * COUNT_IF(transaction_type = 'forward' AND order_status = 'shipment_returned')
        / NULLIF(COUNT_IF(transaction_type = 'forward'), 0), 2) AS rto_rate_pct
    FROM zs_observe.jiomart_oms
    WHERE is_active = true AND hsn IS NOT NULL
    GROUP BY sku_id, mp_sin
    ORDER BY gmv DESC;
  required_tables:
  - table.zs_observe.jiomart_oms
  output_aliases_detected:
  - orders
  - gmv
  - avg_price
  - rto_rate_pct
  confidence: high
```


```yaml
sql_pattern:
  id: sql.jiomart.oms.7_5_oms_settlement_join
  source_section: 7.5 OMS → Settlement Join
  source_context: oms
  source_line_start: 1206
  source_line_end: 1220
  evidence_ref: ev.jiomart.oms.7_5_oms_settlement_join
  sql_pattern: |-
    SELECT
      o.order_id, o.invoice_number,
      o.charged_amount AS oms_gmv,
      o.total_tcs_amount AS oms_tcs,
      s.settled_amount AS settlement_net,
      s.event, s.accountable_type
    FROM zs_observe.jiomart_oms o
    LEFT JOIN zs_observe.jiomart_settlement s
      ON o.order_id = s.order_id AND s.is_active = true
    WHERE o.is_active = true
      AND o.transaction_type = 'forward'
      AND o.order_status = 'delivered'
      AND o.hsn IS NOT NULL;
  required_tables:
  - table.zs_observe.jiomart_oms
  - table.zs_observe.jiomart_settlement
  output_aliases_detected:
  - oms_gmv
  - oms_tcs
  - settlement_net
  confidence: high
```


```yaml
sql_pattern:
  id: sql.jiomart.oms.7_6_return_rate
  source_section: 7.6 Return Rate
  source_context: oms
  source_line_start: 1222
  source_line_end: 1232
  evidence_ref: ev.jiomart.oms.7_6_return_rate
  sql_pattern: |-
    SELECT
      ROUND(100.0 *
        COUNT_IF(order_status = 'shipment_returned')
        / NULLIF(COUNT_IF(transaction_type = 'forward'), 0), 2) AS rto_rate_pct,
      ROUND(100.0 *
        COUNT_IF(transaction_type = 'reverse')
        / NULLIF(COUNT_IF(transaction_type = 'forward'), 0), 2) AS return_reversal_rate_pct
    FROM zs_observe.jiomart_oms
    WHERE is_active = true;
  required_tables:
  - table.zs_observe.jiomart_oms
  output_aliases_detected:
  - rto_rate_pct
  - return_reversal_rate_pct
  confidence: high
```


## 4. Candidate Cards

### 4.1 `platform` cards


```yaml
candidate_card:
  card_type: platform
  card_id: platform.jiomart
  display_name: JioMart
  canonical_name: JioMart
  aliases:
  - JioMart
  marketplace_category: indian_omnichannel_ecommerce_marketplace
  operator_or_parent_context: Reliance Retail / Reliance Industries context is preserved as source evidence only; no platform-account
    card emitted.
  evidence_refs:
  - ev.jiomart.marketplace.1_1_background
  confidence: high
  review_status: ready
```

### 4.2 `platform_context` cards


```yaml
candidate_card:
  card_type: platform_context
  card_id: platform_context.jiomart.in
  display_name: JioMart India marketplace context
  platform_id: platform.jiomart
  country_code: IN
  currency: INR
  timezone: Asia/Kolkata
  marketplace_model: phygital_O2O_marketplace_with_seller_fulfilment_variants
  scope_note: Marketplace-vendor semantic context only. group_level_id values are documented filters/columns; runtime account
    binding is external.
  evidence_refs:
  - ev.jiomart.marketplace.1_1_background
  - ev.jiomart.marketplace.1_3_seller_entities_in_dataset
  confidence: high
  review_status: ready
```

### 4.3 `domain` cards


```yaml
candidate_card:
  card_type: domain
  card_id: domain.jiomart.orders
  display_name: JioMart marketplace order, OMS, invoice, and shipment semantics
  domain_family: orders
  platform_context_id: platform_context.jiomart.in
  scope_note: Marketplace-vendor semantics only; external-domain card creation is forbidden in this markdown.
  evidence_refs:
  - ev.jiomart.marketplace.1_1_background
  confidence: high
  review_status: ready
```


```yaml
candidate_card:
  card_type: domain
  card_id: domain.jiomart.settlement
  display_name: JioMart event-based settlement, payout, receivable, TCS/TDS row semantics
  domain_family: settlement
  platform_context_id: platform_context.jiomart.in
  scope_note: Marketplace-vendor semantics only; external-domain card creation is forbidden in this markdown.
  evidence_refs:
  - ev.jiomart.marketplace.1_1_background
  confidence: high
  review_status: ready
```


```yaml
candidate_card:
  card_type: domain
  card_id: domain.jiomart.returns
  display_name: JioMart return, RTO, doorstep return, cancellation, refund, and return journey semantics
  domain_family: returns
  platform_context_id: platform_context.jiomart.in
  scope_note: Marketplace-vendor semantics only; external-domain card creation is forbidden in this markdown.
  evidence_refs:
  - ev.jiomart.marketplace.1_1_background
  confidence: high
  review_status: ready
```


```yaml
candidate_card:
  card_type: domain
  card_id: domain.jiomart.reconciliation
  display_name: JioMart marketplace-internal reconciliation semantics
  domain_family: reconciliation
  platform_context_id: platform_context.jiomart.in
  scope_note: Marketplace-vendor semantics only; external-domain card creation is forbidden in this markdown.
  evidence_refs:
  - ev.jiomart.marketplace.1_1_background
  confidence: high
  review_status: ready
```


```yaml
candidate_card:
  card_type: domain
  card_id: domain.jiomart.tax
  display_name: JioMart marketplace-side GST/TCS/TDS amount semantics, not statutory filing
  domain_family: tax
  platform_context_id: platform_context.jiomart.in
  scope_note: Marketplace-vendor semantics only; external-domain card creation is forbidden in this markdown.
  evidence_refs:
  - ev.jiomart.marketplace.1_1_background
  confidence: high
  review_status: ready
```


```yaml
candidate_card:
  card_type: domain
  card_id: domain.jiomart.fees
  display_name: JioMart fee/commission/cost semantics where explicitly visible or documented
  domain_family: fees
  platform_context_id: platform_context.jiomart.in
  scope_note: Marketplace-vendor semantics only; external-domain card creation is forbidden in this markdown.
  evidence_refs:
  - ev.jiomart.marketplace.1_1_background
  confidence: high
  review_status: ready
```


```yaml
candidate_card:
  card_type: domain
  card_id: domain.jiomart.fulfillment
  display_name: JioMart fulfilment/shipping/courier identifiers as marketplace columns, not external logistics accounts
  domain_family: fulfillment
  platform_context_id: platform_context.jiomart.in
  scope_note: Marketplace-vendor semantics only; external-domain card creation is forbidden in this markdown.
  evidence_refs:
  - ev.jiomart.marketplace.1_1_background
  confidence: high
  review_status: ready
```


```yaml
candidate_card:
  card_type: domain
  card_id: domain.jiomart.product
  display_name: JioMart SKU, HSN, product, brand, SIN, and catalogue semantics
  domain_family: product
  platform_context_id: platform_context.jiomart.in
  scope_note: Marketplace-vendor semantics only; external-domain card creation is forbidden in this markdown.
  evidence_refs:
  - ev.jiomart.marketplace.1_1_background
  confidence: high
  review_status: ready
```


```yaml
candidate_card:
  card_type: domain
  card_id: domain.jiomart.promotions
  display_name: JioMart seller coupon and promotional discount semantics
  domain_family: promotions
  platform_context_id: platform_context.jiomart.in
  scope_note: Marketplace-vendor semantics only; external-domain card creation is forbidden in this markdown.
  evidence_refs:
  - ev.jiomart.marketplace.1_1_background
  confidence: high
  review_status: ready
```


```yaml
candidate_card:
  card_type: domain
  card_id: domain.jiomart.payment_mode
  display_name: JioMart COD/Prepaid payment-mode semantics, not payment-gateway cards
  domain_family: payment_mode
  platform_context_id: platform_context.jiomart.in
  scope_note: Marketplace-vendor semantics only; external-domain card creation is forbidden in this markdown.
  evidence_refs:
  - ev.jiomart.marketplace.1_1_background
  confidence: high
  review_status: ready
```


```yaml
candidate_card:
  card_type: domain
  card_id: domain.jiomart.query_guidance
  display_name: JioMart parser query, filter, validation, and output guidance
  domain_family: query_guidance
  platform_context_id: platform_context.jiomart.in
  scope_note: Marketplace-vendor semantics only; external-domain card creation is forbidden in this markdown.
  evidence_refs:
  - ev.jiomart.marketplace.1_1_background
  confidence: high
  review_status: ready
```

### 4.4 `table` cards


```yaml
candidate_card:
  card_type: table
  card_id: table.zs_observe.jiomart_shipment
  display_name: zs_observe.jiomart_shipment
  schema: zs_observe
  table_name: jiomart_shipment
  table_role: orders_shipment
  business_purpose: Shipment report for ARDEUR FASHIONS / group_level_id 221; operational order/shipment status, MRP, charged
    amount, discounts, shipping date.
  semantic_domain_id: domain.jiomart.orders
  grain: shipment_order_item_line
  row_count_evidence: 425 total / 425 active
  date_range: 2025-10-01 to 2025-12-30
  documented_scope_values:
    group_level_id: 221
    entity: ARDEUR FASHIONS
    brand_context: CODEZ / ARDEUR
  mandatory_filters:
  - is_active = true
  - group_level_id = 221
  - qty > 0 for active shipments
  scope_caveats: group_level_id/seller/entity/GSTIN values are columns/filters/caveats only; no tenant/group/account cards
    emitted.
  join_caveat: 0% match with jiomart_oms; never cross-join with group 26 OMS/returns/settlement.
  evidence_refs:
  - ev.jiomart.shipment.1_table_overview
  - ev.jiomart.shipment.2_key_statistics
  - ev.jiomart.shipment.3_schema_details_29_columns
  confidence: high
  review_status: ready
```


```yaml
candidate_card:
  card_type: table
  card_id: table.zs_observe.jiomart_settlement
  display_name: zs_observe.jiomart_settlement
  schema: zs_observe
  table_name: jiomart_settlement
  table_role: settlement
  business_purpose: Event-based multi-row financial settlement ledger for TANVI Fitness / MYFITNESS group_level_id 26.
  semantic_domain_id: domain.jiomart.settlement
  grain: settlement_event_line; aggregate by order_id for per-order net
  row_count_evidence: 237,129 total / 188,345 active
  date_range: 2025-01-01 to 2025-12-31
  documented_scope_values:
    group_level_id: 26
    entity: TANVI Fitness Pvt Ltd / MYFITNESS
  mandatory_filters:
  - is_active = true
  - group_level_id = 26
  - event IS NOT NULL for structured event analysis
  scope_caveats: group_level_id/seller/entity/GSTIN values are columns/filters/caveats only; no tenant/group/account cards
    emitted.
  join_caveat: Use order_id for OMS/returns joins; invoice_number format differs and document_number is mostly NULL.
  evidence_refs:
  - ev.jiomart.settlement.1_table_overview
  - ev.jiomart.settlement.2_key_statistics
  - ev.jiomart.settlement.3_schema_details_40_columns
  confidence: high
  review_status: ready
```


```yaml
candidate_card:
  card_type: table
  card_id: table.zs_observe.jiomart_returns
  display_name: zs_observe.jiomart_returns
  schema: zs_observe
  table_name: jiomart_returns
  table_role: returns
  business_purpose: Return tracking table for RTO, doorstep, and pre-shipment return events with courier/AWB, refund amount,
    and timeline columns.
  semantic_domain_id: domain.jiomart.returns
  grain: return_event_order_line
  row_count_evidence: 8,367 active
  date_range: 2025-01-01 to 2025-12-31
  documented_scope_values:
    group_level_id: 26
    entity: TANVI Fitness Pvt Ltd / MYFITNESS
  mandatory_filters:
  - is_active = true
  - group_level_id = 26
  - return_type IS NOT NULL for return analysis
  scope_caveats: group_level_id/seller/entity/GSTIN values are columns/filters/caveats only; no tenant/group/account cards
    emitted.
  join_caveat: Join to OMS and settlement on order_id; invoice_number also maps to OMS but order_id is preferred.
  evidence_refs:
  - ev.jiomart.returns.1_table_overview
  - ev.jiomart.returns.2_key_statistics
  - ev.jiomart.returns.3_schema_details_53_columns
  confidence: high
  review_status: ready
```


```yaml
candidate_card:
  card_type: table
  card_id: table.zs_observe.jiomart_oms
  display_name: zs_observe.jiomart_oms
  schema: zs_observe
  table_name: jiomart_oms
  table_role: orders_oms
  business_purpose: Primary OMS/GST invoice ledger for JioMart MYFITNESS orders and returns.
  semantic_domain_id: domain.jiomart.orders
  grain: sub_order_item_invoice_or_credit_note_line
  row_count_evidence: 67,359 active
  date_range: 2025-01-01 to 2025-12-31
  documented_scope_values:
    group_level_id: 26
    entity: TANVI Fitness Pvt Ltd / MYFITNESS
    brand: MYFITNESS
  mandatory_filters:
  - is_active = true
  - group_level_id = 26
  - hsn IS NOT NULL for clean structured rows
  - created_date for time-series
  scope_caveats: group_level_id/seller/entity/GSTIN values are columns/filters/caveats only; no tenant/group/account cards
    emitted.
  join_caveat: Use order_id as primary join key to settlement/returns; use sku_id + mp_sin for product grouping when sku has
    older-row NULLs.
  evidence_refs:
  - ev.jiomart.oms.1_table_overview
  - ev.jiomart.oms.2_key_statistics
  - ev.jiomart.oms.3_schema_details_115_columns
  confidence: high
  review_status: ready
```

### 4.5 `column` cards


```yaml
candidate_card:
  card_type: column
  card_id: column.zs_observe.jiomart_shipment.unique_id
  display_name: jiomart_shipment.unique_id
  table_id: table.zs_observe.jiomart_shipment
  schema: zs_observe
  table_name: jiomart_shipment
  column_name: unique_id
  source_declared_type: varchar
  data_type: varchar
  column_group: Schema Details
  semantic_role: identity_or_join_key
  business_meaning: Row identifier
  evidence_refs:
  - ev.jiomart.shipment.3_schema_details_29_columns
  confidence: high
  review_status: ready
```


```yaml
candidate_card:
  card_type: column
  card_id: column.zs_observe.jiomart_shipment.txn_uuid
  display_name: jiomart_shipment.txn_uuid
  table_id: table.zs_observe.jiomart_shipment
  schema: zs_observe
  table_name: jiomart_shipment
  column_name: txn_uuid
  source_declared_type: varchar
  data_type: varchar
  column_group: Schema Details
  semantic_role: identity_or_join_key
  business_meaning: Pipeline UUID
  evidence_refs:
  - ev.jiomart.shipment.3_schema_details_29_columns
  confidence: high
  review_status: ready
```


```yaml
candidate_card:
  card_type: column
  card_id: column.zs_observe.jiomart_shipment.unique_value
  display_name: jiomart_shipment.unique_value
  table_id: table.zs_observe.jiomart_shipment
  schema: zs_observe
  table_name: jiomart_shipment
  column_name: unique_value
  source_declared_type: varchar
  data_type: varchar
  column_group: Schema Details
  semantic_role: financial_amount_or_rate
  business_meaning: Dedup hash
  evidence_refs:
  - ev.jiomart.shipment.3_schema_details_29_columns
  confidence: high
  review_status: ready
```


```yaml
candidate_card:
  card_type: column
  card_id: column.zs_observe.jiomart_shipment.source_gst_name
  display_name: jiomart_shipment.source_gst_name
  table_id: table.zs_observe.jiomart_shipment
  schema: zs_observe
  table_name: jiomart_shipment
  column_name: source_gst_name
  source_declared_type: varchar
  data_type: varchar
  column_group: Schema Details
  semantic_role: scope_column_preserved_not_card_boundary
  business_meaning: 'Seller name: `ARDEUR FASHIONS 641604`'
  scope_note: Scope-like field retained as a source column/filter/value only; do not create tenant/group/account cards.
  evidence_refs:
  - ev.jiomart.shipment.3_schema_details_29_columns
  confidence: high
  review_status: ready
```


```yaml
candidate_card:
  card_type: column
  card_id: column.zs_observe.jiomart_shipment.order_id
  display_name: jiomart_shipment.order_id
  table_id: table.zs_observe.jiomart_shipment
  schema: zs_observe
  table_name: jiomart_shipment
  column_name: order_id
  source_declared_type: varchar
  data_type: varchar
  column_group: Schema Details
  semantic_role: identity_or_join_key
  business_meaning: 'JioMart order ID (format: `17592870447301320654J`)'
  evidence_refs:
  - ev.jiomart.shipment.3_schema_details_29_columns
  confidence: high
  review_status: ready
```


```yaml
candidate_card:
  card_type: column
  card_id: column.zs_observe.jiomart_shipment.created_date
  display_name: jiomart_shipment.created_date
  table_id: table.zs_observe.jiomart_shipment
  schema: zs_observe
  table_name: jiomart_shipment
  column_name: created_date
  source_declared_type: timestamp
  data_type: timestamp
  column_group: Schema Details
  semantic_role: date_time
  business_meaning: Order creation timestamp
  evidence_refs:
  - ev.jiomart.shipment.3_schema_details_29_columns
  confidence: high
  review_status: ready
```


```yaml
candidate_card:
  card_type: column
  card_id: column.zs_observe.jiomart_shipment.order_status
  display_name: jiomart_shipment.order_status
  table_id: table.zs_observe.jiomart_shipment
  schema: zs_observe
  table_name: jiomart_shipment
  column_name: order_status
  source_declared_type: varchar
  data_type: varchar
  column_group: Schema Details
  semantic_role: marketplace_fulfillment_identifier
  business_meaning: '`delivered`, `shipment_returned`, `canceled`'
  evidence_refs:
  - ev.jiomart.shipment.3_schema_details_29_columns
  confidence: high
  review_status: ready
```


```yaml
candidate_card:
  card_type: column
  card_id: column.zs_observe.jiomart_shipment.qty
  display_name: jiomart_shipment.qty
  table_id: table.zs_observe.jiomart_shipment
  schema: zs_observe
  table_name: jiomart_shipment
  column_name: qty
  source_declared_type: integer
  data_type: integer
  column_group: Schema Details
  semantic_role: general_marketplace_attribute
  business_meaning: Quantity
  evidence_refs:
  - ev.jiomart.shipment.3_schema_details_29_columns
  confidence: high
  review_status: ready
```


```yaml
candidate_card:
  card_type: column
  card_id: column.zs_observe.jiomart_shipment.description
  display_name: jiomart_shipment.description
  table_id: table.zs_observe.jiomart_shipment
  schema: zs_observe
  table_name: jiomart_shipment
  column_name: description
  source_declared_type: varchar
  data_type: varchar
  column_group: Schema Details
  semantic_role: product_catalog
  business_meaning: Product description
  evidence_refs:
  - ev.jiomart.shipment.3_schema_details_29_columns
  confidence: high
  review_status: ready
```


```yaml
candidate_card:
  card_type: column
  card_id: column.zs_observe.jiomart_shipment.fulfillment_channel
  display_name: jiomart_shipment.fulfillment_channel
  table_id: table.zs_observe.jiomart_shipment
  schema: zs_observe
  table_name: jiomart_shipment
  column_name: fulfillment_channel
  source_declared_type: varchar
  data_type: varchar
  column_group: Schema Details
  semantic_role: marketplace_fulfillment_identifier
  business_meaning: '`Direct Shipment`'
  evidence_refs:
  - ev.jiomart.shipment.3_schema_details_29_columns
  confidence: high
  review_status: ready
```


```yaml
candidate_card:
  card_type: column
  card_id: column.zs_observe.jiomart_shipment.sku_id
  display_name: jiomart_shipment.sku_id
  table_id: table.zs_observe.jiomart_shipment
  schema: zs_observe
  table_name: jiomart_shipment
  column_name: sku_id
  source_declared_type: varchar
  data_type: varchar
  column_group: Schema Details
  semantic_role: product_catalog
  business_meaning: Seller SKU (e.g., `ASSJ18-MSH-CHR-XL`, `CBOT001-RT1-15Y-P1`)
  evidence_refs:
  - ev.jiomart.shipment.3_schema_details_29_columns
  confidence: high
  review_status: ready
```


```yaml
candidate_card:
  card_type: column
  card_id: column.zs_observe.jiomart_shipment.mrp
  display_name: jiomart_shipment.mrp
  table_id: table.zs_observe.jiomart_shipment
  schema: zs_observe
  table_name: jiomart_shipment
  column_name: mrp
  source_declared_type: decimal
  data_type: decimal
  column_group: Schema Details
  semantic_role: financial_amount_or_rate
  business_meaning: Maximum Retail Price
  evidence_refs:
  - ev.jiomart.shipment.3_schema_details_29_columns
  confidence: high
  review_status: ready
```


```yaml
candidate_card:
  card_type: column
  card_id: column.zs_observe.jiomart_shipment.charged_amount
  display_name: jiomart_shipment.charged_amount
  table_id: table.zs_observe.jiomart_shipment
  schema: zs_observe
  table_name: jiomart_shipment
  column_name: charged_amount
  source_declared_type: decimal
  data_type: decimal
  column_group: Schema Details
  semantic_role: financial_amount_or_rate
  business_meaning: Amount charged to buyer after discount
  evidence_refs:
  - ev.jiomart.shipment.3_schema_details_29_columns
  confidence: high
  review_status: ready
```


```yaml
candidate_card:
  card_type: column
  card_id: column.zs_observe.jiomart_shipment.item_promo_discount
  display_name: jiomart_shipment.item_promo_discount
  table_id: table.zs_observe.jiomart_shipment
  schema: zs_observe
  table_name: jiomart_shipment
  column_name: item_promo_discount
  source_declared_type: decimal
  data_type: decimal
  column_group: Schema Details
  semantic_role: financial_amount_or_rate
  business_meaning: Promotional discount applied (MRP − charged)
  evidence_refs:
  - ev.jiomart.shipment.3_schema_details_29_columns
  confidence: high
  review_status: ready
```


```yaml
candidate_card:
  card_type: column
  card_id: column.zs_observe.jiomart_shipment.payment_mode
  display_name: jiomart_shipment.payment_mode
  table_id: table.zs_observe.jiomart_shipment
  schema: zs_observe
  table_name: jiomart_shipment
  column_name: payment_mode
  source_declared_type: varchar
  data_type: varchar
  column_group: Schema Details
  semantic_role: classification_status_or_type
  business_meaning: '`COD` or `Prepaid_Payments`'
  evidence_refs:
  - ev.jiomart.shipment.3_schema_details_29_columns
  confidence: high
  review_status: ready
```


```yaml
candidate_card:
  card_type: column
  card_id: column.zs_observe.jiomart_shipment.shipping_date
  display_name: jiomart_shipment.shipping_date
  table_id: table.zs_observe.jiomart_shipment
  schema: zs_observe
  table_name: jiomart_shipment
  column_name: shipping_date
  source_declared_type: timestamp
  data_type: timestamp
  column_group: Schema Details
  semantic_role: marketplace_fulfillment_identifier
  business_meaning: Shipment dispatch date
  evidence_refs:
  - ev.jiomart.shipment.3_schema_details_29_columns
  confidence: high
  review_status: ready
```


```yaml
candidate_card:
  card_type: column
  card_id: column.zs_observe.jiomart_shipment.currency_type
  display_name: jiomart_shipment.currency_type
  table_id: table.zs_observe.jiomart_shipment
  schema: zs_observe
  table_name: jiomart_shipment
  column_name: currency_type
  source_declared_type: varchar
  data_type: varchar
  column_group: Schema Details
  semantic_role: classification_status_or_type
  business_meaning: '`INR`'
  evidence_refs:
  - ev.jiomart.shipment.3_schema_details_29_columns
  confidence: high
  review_status: ready
```


```yaml
candidate_card:
  card_type: column
  card_id: column.zs_observe.jiomart_shipment.is_active
  display_name: jiomart_shipment.is_active
  table_id: table.zs_observe.jiomart_shipment
  schema: zs_observe
  table_name: jiomart_shipment
  column_name: is_active
  source_declared_type: boolean
  data_type: boolean
  column_group: Schema Details
  semantic_role: general_marketplace_attribute
  business_meaning: Always `true`
  evidence_refs:
  - ev.jiomart.shipment.3_schema_details_29_columns
  confidence: high
  review_status: ready
```


```yaml
candidate_card:
  card_type: column
  card_id: column.zs_observe.jiomart_shipment.group_level_id
  display_name: jiomart_shipment.group_level_id
  table_id: table.zs_observe.jiomart_shipment
  schema: zs_observe
  table_name: jiomart_shipment
  column_name: group_level_id
  source_declared_type: integer
  data_type: integer
  column_group: Schema Details
  semantic_role: scope_column_preserved_not_card_boundary
  business_meaning: '`221`'
  scope_note: Scope-like field retained as a source column/filter/value only; do not create tenant/group/account cards.
  evidence_refs:
  - ev.jiomart.shipment.3_schema_details_29_columns
  confidence: high
  review_status: ready
```


```yaml
candidate_card:
  card_type: column
  card_id: column.zs_observe.jiomart_shipment.zen_sheet_name
  display_name: jiomart_shipment.zen_sheet_name
  table_id: table.zs_observe.jiomart_shipment
  schema: zs_observe
  table_name: jiomart_shipment
  column_name: zen_sheet_name
  source_declared_type: varchar
  data_type: varchar
  column_group: Schema Details
  semantic_role: general_marketplace_attribute
  business_meaning: Source sheet
  evidence_refs:
  - ev.jiomart.shipment.3_schema_details_29_columns
  confidence: high
  review_status: ready
```


```yaml
candidate_card:
  card_type: column
  card_id: column.zs_observe.jiomart_shipment.created_at
  display_name: jiomart_shipment.created_at
  table_id: table.zs_observe.jiomart_shipment
  schema: zs_observe
  table_name: jiomart_shipment
  column_name: created_at
  source_declared_type: timestamp
  data_type: timestamp
  column_group: Schema Details
  semantic_role: date_time
  business_meaning: Timestamps
  evidence_refs:
  - ev.jiomart.shipment.3_schema_details_29_columns
  confidence: high
  review_status: ready
```


```yaml
candidate_card:
  card_type: column
  card_id: column.zs_observe.jiomart_shipment.updated_at
  display_name: jiomart_shipment.updated_at
  table_id: table.zs_observe.jiomart_shipment
  schema: zs_observe
  table_name: jiomart_shipment
  column_name: updated_at
  source_declared_type: timestamp
  data_type: timestamp
  column_group: Schema Details
  semantic_role: date_time
  business_meaning: Timestamps
  evidence_refs:
  - ev.jiomart.shipment.3_schema_details_29_columns
  confidence: high
  review_status: ready
```


```yaml
candidate_card:
  card_type: column
  card_id: column.zs_observe.jiomart_settlement.unique_id
  display_name: jiomart_settlement.unique_id
  table_id: table.zs_observe.jiomart_settlement
  schema: zs_observe
  table_name: jiomart_settlement
  column_name: unique_id
  source_declared_type: varchar
  data_type: varchar
  column_group: 3.1 Identity Columns
  semantic_role: identity_or_join_key
  business_meaning: Row identifier
  evidence_refs:
  - ev.jiomart.settlement.3_schema_details_40_columns
  confidence: high
  review_status: ready
```


```yaml
candidate_card:
  card_type: column
  card_id: column.zs_observe.jiomart_settlement.txn_uuid
  display_name: jiomart_settlement.txn_uuid
  table_id: table.zs_observe.jiomart_settlement
  schema: zs_observe
  table_name: jiomart_settlement
  column_name: txn_uuid
  source_declared_type: varchar
  data_type: varchar
  column_group: 3.1 Identity Columns
  semantic_role: identity_or_join_key
  business_meaning: Pipeline UUID
  evidence_refs:
  - ev.jiomart.settlement.3_schema_details_40_columns
  confidence: high
  review_status: ready
```


```yaml
candidate_card:
  card_type: column
  card_id: column.zs_observe.jiomart_settlement.unique_value
  display_name: jiomart_settlement.unique_value
  table_id: table.zs_observe.jiomart_settlement
  schema: zs_observe
  table_name: jiomart_settlement
  column_name: unique_value
  source_declared_type: varchar
  data_type: varchar
  column_group: 3.1 Identity Columns
  semantic_role: financial_amount_or_rate
  business_meaning: Dedup hash
  evidence_refs:
  - ev.jiomart.settlement.3_schema_details_40_columns
  confidence: high
  review_status: ready
```


```yaml
candidate_card:
  card_type: column
  card_id: column.zs_observe.jiomart_settlement.invoice_number
  display_name: jiomart_settlement.invoice_number
  table_id: table.zs_observe.jiomart_settlement
  schema: zs_observe
  table_name: jiomart_settlement
  column_name: invoice_number
  source_declared_type: varchar
  data_type: varchar
  column_group: 3.1 Identity Columns
  semantic_role: identity_or_join_key
  business_meaning: Settlement invoice reference — **join key to jiomart_oms**
  evidence_refs:
  - ev.jiomart.settlement.3_schema_details_40_columns
  confidence: high
  review_status: ready
```


```yaml
candidate_card:
  card_type: column
  card_id: column.zs_observe.jiomart_settlement.order_id
  display_name: jiomart_settlement.order_id
  table_id: table.zs_observe.jiomart_settlement
  schema: zs_observe
  table_name: jiomart_settlement
  column_name: order_id
  source_declared_type: varchar
  data_type: varchar
  column_group: 3.1 Identity Columns
  semantic_role: identity_or_join_key
  business_meaning: JioMart order ID — **primary join key**
  evidence_refs:
  - ev.jiomart.settlement.3_schema_details_40_columns
  confidence: high
  review_status: ready
```


```yaml
candidate_card:
  card_type: column
  card_id: column.zs_observe.jiomart_settlement.item_id
  display_name: jiomart_settlement.item_id
  table_id: table.zs_observe.jiomart_settlement
  schema: zs_observe
  table_name: jiomart_settlement
  column_name: item_id
  source_declared_type: varchar
  data_type: varchar
  column_group: 3.1 Identity Columns
  semantic_role: identity_or_join_key
  business_meaning: Line item ID
  evidence_refs:
  - ev.jiomart.settlement.3_schema_details_40_columns
  confidence: high
  review_status: ready
```


```yaml
candidate_card:
  card_type: column
  card_id: column.zs_observe.jiomart_settlement.parent_id
  display_name: jiomart_settlement.parent_id
  table_id: table.zs_observe.jiomart_settlement
  schema: zs_observe
  table_name: jiomart_settlement
  column_name: parent_id
  source_declared_type: varchar
  data_type: varchar
  column_group: 3.1 Identity Columns
  semantic_role: identity_or_join_key
  business_meaning: Parent order reference
  evidence_refs:
  - ev.jiomart.settlement.3_schema_details_40_columns
  confidence: high
  review_status: ready
```


```yaml
candidate_card:
  card_type: column
  card_id: column.zs_observe.jiomart_settlement.other_id
  display_name: jiomart_settlement.other_id
  table_id: table.zs_observe.jiomart_settlement
  schema: zs_observe
  table_name: jiomart_settlement
  column_name: other_id
  source_declared_type: varchar
  data_type: varchar
  column_group: 3.1 Identity Columns
  semantic_role: identity_or_join_key
  business_meaning: Alternate reference ID
  evidence_refs:
  - ev.jiomart.settlement.3_schema_details_40_columns
  confidence: high
  review_status: ready
```


```yaml
candidate_card:
  card_type: column
  card_id: column.zs_observe.jiomart_settlement.document_number
  display_name: jiomart_settlement.document_number
  table_id: table.zs_observe.jiomart_settlement
  schema: zs_observe
  table_name: jiomart_settlement
  column_name: document_number
  source_declared_type: varchar
  data_type: varchar
  column_group: 3.1 Identity Columns
  semantic_role: identity_or_join_key
  business_meaning: Document reference (mostly NULL)
  evidence_refs:
  - ev.jiomart.settlement.3_schema_details_40_columns
  confidence: high
  review_status: ready
```


```yaml
candidate_card:
  card_type: column
  card_id: column.zs_observe.jiomart_settlement.shipment_number
  display_name: jiomart_settlement.shipment_number
  table_id: table.zs_observe.jiomart_settlement
  schema: zs_observe
  table_name: jiomart_settlement
  column_name: shipment_number
  source_declared_type: varchar
  data_type: varchar
  column_group: 3.1 Identity Columns
  semantic_role: marketplace_fulfillment_identifier
  business_meaning: Shipment reference
  evidence_refs:
  - ev.jiomart.settlement.3_schema_details_40_columns
  confidence: high
  review_status: ready
```


```yaml
candidate_card:
  card_type: column
  card_id: column.zs_observe.jiomart_settlement.accountable_number
  display_name: jiomart_settlement.accountable_number
  table_id: table.zs_observe.jiomart_settlement
  schema: zs_observe
  table_name: jiomart_settlement
  column_name: accountable_number
  source_declared_type: varchar
  data_type: varchar
  column_group: 3.1 Identity Columns
  semantic_role: identity_or_join_key
  business_meaning: Account line identifier
  evidence_refs:
  - ev.jiomart.settlement.3_schema_details_40_columns
  confidence: high
  review_status: ready
```


```yaml
candidate_card:
  card_type: column
  card_id: column.zs_observe.jiomart_settlement.number
  display_name: jiomart_settlement.number
  table_id: table.zs_observe.jiomart_settlement
  schema: zs_observe
  table_name: jiomart_settlement
  column_name: number
  source_declared_type: varchar
  data_type: varchar
  column_group: 3.1 Identity Columns
  semantic_role: identity_or_join_key
  business_meaning: Internal sequence number
  evidence_refs:
  - ev.jiomart.settlement.3_schema_details_40_columns
  confidence: high
  review_status: ready
```


```yaml
candidate_card:
  card_type: column
  card_id: column.zs_observe.jiomart_settlement.unique_id_1
  display_name: jiomart_settlement.unique_id_1
  table_id: table.zs_observe.jiomart_settlement
  schema: zs_observe
  table_name: jiomart_settlement
  column_name: unique_id_1
  source_declared_type: varchar
  data_type: varchar
  column_group: 3.1 Identity Columns
  semantic_role: identity_or_join_key
  business_meaning: Legacy unique ID
  evidence_refs:
  - ev.jiomart.settlement.3_schema_details_40_columns
  confidence: high
  review_status: ready
```


```yaml
candidate_card:
  card_type: column
  card_id: column.zs_observe.jiomart_settlement.settlement_date
  display_name: jiomart_settlement.settlement_date
  table_id: table.zs_observe.jiomart_settlement
  schema: zs_observe
  table_name: jiomart_settlement
  column_name: settlement_date
  source_declared_type: date
  data_type: date
  column_group: 3.2 Date Columns
  semantic_role: date_time
  business_meaning: '**Date of settlement** — primary date field'
  evidence_refs:
  - ev.jiomart.settlement.3_schema_details_40_columns
  confidence: high
  review_status: ready
```


```yaml
candidate_card:
  card_type: column
  card_id: column.zs_observe.jiomart_settlement.created_at
  display_name: jiomart_settlement.created_at
  table_id: table.zs_observe.jiomart_settlement
  schema: zs_observe
  table_name: jiomart_settlement
  column_name: created_at
  source_declared_type: timestamp
  data_type: timestamp
  column_group: 3.2 Date Columns
  semantic_role: date_time
  business_meaning: Record creation timestamp
  evidence_refs:
  - ev.jiomart.settlement.3_schema_details_40_columns
  confidence: high
  review_status: ready
```


```yaml
candidate_card:
  card_type: column
  card_id: column.zs_observe.jiomart_settlement.created_at_1
  display_name: jiomart_settlement.created_at_1
  table_id: table.zs_observe.jiomart_settlement
  schema: zs_observe
  table_name: jiomart_settlement
  column_name: created_at_1
  source_declared_type: varchar
  data_type: varchar
  column_group: 3.2 Date Columns
  semantic_role: date_time
  business_meaning: Legacy creation timestamp
  evidence_refs:
  - ev.jiomart.settlement.3_schema_details_40_columns
  confidence: high
  review_status: ready
```


```yaml
candidate_card:
  card_type: column
  card_id: column.zs_observe.jiomart_settlement.created_at_temp_old
  display_name: jiomart_settlement.created_at_temp_old
  table_id: table.zs_observe.jiomart_settlement
  schema: zs_observe
  table_name: jiomart_settlement
  column_name: created_at_temp_old
  source_declared_type: varchar
  data_type: varchar
  column_group: 3.2 Date Columns
  semantic_role: date_time
  business_meaning: Migration column
  evidence_refs:
  - ev.jiomart.settlement.3_schema_details_40_columns
  confidence: high
  review_status: ready
```


```yaml
candidate_card:
  card_type: column
  card_id: column.zs_observe.jiomart_settlement.settled_amount
  display_name: jiomart_settlement.settled_amount
  table_id: table.zs_observe.jiomart_settlement
  schema: zs_observe
  table_name: jiomart_settlement
  column_name: settled_amount
  source_declared_type: decimal
  data_type: decimal
  column_group: 3.3 Financial Columns
  semantic_role: financial_amount_or_rate
  business_meaning: '**Net financial impact on seller account** (positive = credit, negative = debit)'
  sign_or_context_semantics: In structured rows, positive settled_amount credits seller balance; negative debits seller balance.
    Receivable/BaseTcs/Tds context is required.
  evidence_refs:
  - ev.jiomart.settlement.3_schema_details_40_columns
  confidence: high
  review_status: ready
```


```yaml
candidate_card:
  card_type: column
  card_id: column.zs_observe.jiomart_settlement.amount
  display_name: jiomart_settlement.amount
  table_id: table.zs_observe.jiomart_settlement
  schema: zs_observe
  table_name: jiomart_settlement
  column_name: amount
  source_declared_type: decimal
  data_type: decimal
  column_group: 3.3 Financial Columns
  semantic_role: financial_amount_or_rate
  business_meaning: Raw transaction amount (= settled_amount for rows with event)
  sign_or_context_semantics: In structured rows, positive settled_amount credits seller balance; negative debits seller balance.
    Receivable/BaseTcs/Tds context is required.
  evidence_refs:
  - ev.jiomart.settlement.3_schema_details_40_columns
  confidence: high
  review_status: ready
```


```yaml
candidate_card:
  card_type: column
  card_id: column.zs_observe.jiomart_settlement.transaction_type
  display_name: jiomart_settlement.transaction_type
  table_id: table.zs_observe.jiomart_settlement
  schema: zs_observe
  table_name: jiomart_settlement
  column_name: transaction_type
  source_declared_type: varchar
  data_type: varchar
  column_group: 3.4 Classification Columns
  semantic_role: financial_amount_or_rate
  business_meaning: '`forward`, `reverse`, `Credit Note`, `Debit Note`, `Service Invoice`, `Bill Tds Refund`'
  sign_or_context_semantics: In structured rows, positive settled_amount credits seller balance; negative debits seller balance.
    Receivable/BaseTcs/Tds context is required.
  evidence_refs:
  - ev.jiomart.settlement.3_schema_details_40_columns
  confidence: high
  review_status: ready
```


```yaml
candidate_card:
  card_type: column
  card_id: column.zs_observe.jiomart_settlement.event
  display_name: jiomart_settlement.event
  table_id: table.zs_observe.jiomart_settlement
  schema: zs_observe
  table_name: jiomart_settlement
  column_name: event
  source_declared_type: varchar
  data_type: varchar
  column_group: 3.4 Classification Columns
  semantic_role: classification_status_or_type
  business_meaning: '`Invoice`, `Return`, `Credit Note`, `Debit Note`, `Service Invoice`'
  sign_or_context_semantics: In structured rows, positive settled_amount credits seller balance; negative debits seller balance.
    Receivable/BaseTcs/Tds context is required.
  evidence_refs:
  - ev.jiomart.settlement.3_schema_details_40_columns
  confidence: high
  review_status: ready
```


```yaml
candidate_card:
  card_type: column
  card_id: column.zs_observe.jiomart_settlement.accountable_type
  display_name: jiomart_settlement.accountable_type
  table_id: table.zs_observe.jiomart_settlement
  schema: zs_observe
  table_name: jiomart_settlement
  column_name: accountable_type
  source_declared_type: varchar
  data_type: varchar
  column_group: 3.4 Classification Columns
  semantic_role: financial_amount_or_rate
  business_meaning: '`Receivable`, `BaseTcs`, `Tds`, `CreditDebitNote`, `Bill`'
  sign_or_context_semantics: In structured rows, positive settled_amount credits seller balance; negative debits seller balance.
    Receivable/BaseTcs/Tds context is required.
  evidence_refs:
  - ev.jiomart.settlement.3_schema_details_40_columns
  confidence: high
  review_status: ready
```


```yaml
candidate_card:
  card_type: column
  card_id: column.zs_observe.jiomart_settlement.account_book
  display_name: jiomart_settlement.account_book
  table_id: table.zs_observe.jiomart_settlement
  schema: zs_observe
  table_name: jiomart_settlement
  column_name: account_book
  source_declared_type: varchar
  data_type: varchar
  column_group: 3.4 Classification Columns
  semantic_role: general_marketplace_attribute
  business_meaning: '`Seller payable` (always)'
  evidence_refs:
  - ev.jiomart.settlement.3_schema_details_40_columns
  confidence: high
  review_status: ready
```


```yaml
candidate_card:
  card_type: column
  card_id: column.zs_observe.jiomart_settlement.description
  display_name: jiomart_settlement.description
  table_id: table.zs_observe.jiomart_settlement
  schema: zs_observe
  table_name: jiomart_settlement
  column_name: description
  source_declared_type: varchar
  data_type: varchar
  column_group: 3.4 Classification Columns
  semantic_role: product_catalog
  business_meaning: Row description (= accountable_type for structured rows)
  evidence_refs:
  - ev.jiomart.settlement.3_schema_details_40_columns
  confidence: high
  review_status: ready
```


```yaml
candidate_card:
  card_type: column
  card_id: column.zs_observe.jiomart_settlement.group_level_id
  display_name: jiomart_settlement.group_level_id
  table_id: table.zs_observe.jiomart_settlement
  schema: zs_observe
  table_name: jiomart_settlement
  column_name: group_level_id
  source_declared_type: integer
  data_type: integer
  column_group: 3.5 System / Metadata
  semantic_role: scope_column_preserved_not_card_boundary
  business_meaning: '`26`'
  scope_note: Scope-like field retained as a source column/filter/value only; do not create tenant/group/account cards.
  evidence_refs:
  - ev.jiomart.settlement.3_schema_details_40_columns
  confidence: high
  review_status: ready
```


```yaml
candidate_card:
  card_type: column
  card_id: column.zs_observe.jiomart_settlement.currency_type
  display_name: jiomart_settlement.currency_type
  table_id: table.zs_observe.jiomart_settlement
  schema: zs_observe
  table_name: jiomart_settlement
  column_name: currency_type
  source_declared_type: varchar
  data_type: varchar
  column_group: 3.5 System / Metadata
  semantic_role: classification_status_or_type
  business_meaning: '`INR`'
  evidence_refs:
  - ev.jiomart.settlement.3_schema_details_40_columns
  confidence: high
  review_status: ready
```


```yaml
candidate_card:
  card_type: column
  card_id: column.zs_observe.jiomart_settlement.is_active
  display_name: jiomart_settlement.is_active
  table_id: table.zs_observe.jiomart_settlement
  schema: zs_observe
  table_name: jiomart_settlement
  column_name: is_active
  source_declared_type: boolean
  data_type: boolean
  column_group: 3.5 System / Metadata
  semantic_role: general_marketplace_attribute
  business_meaning: Filter `is_active = true` (188,345 of 237,129 active)
  evidence_refs:
  - ev.jiomart.settlement.3_schema_details_40_columns
  confidence: high
  review_status: ready
```


```yaml
candidate_card:
  card_type: column
  card_id: column.zs_observe.jiomart_settlement.is_duplicated
  display_name: jiomart_settlement.is_duplicated
  table_id: table.zs_observe.jiomart_settlement
  schema: zs_observe
  table_name: jiomart_settlement
  column_name: is_duplicated
  source_declared_type: boolean
  data_type: boolean
  column_group: 3.5 System / Metadata
  semantic_role: general_marketplace_attribute
  business_meaning: Dedup flag
  evidence_refs:
  - ev.jiomart.settlement.3_schema_details_40_columns
  confidence: high
  review_status: ready
```


```yaml
candidate_card:
  card_type: column
  card_id: column.zs_observe.jiomart_settlement.zen_status
  display_name: jiomart_settlement.zen_status
  table_id: table.zs_observe.jiomart_settlement
  schema: zs_observe
  table_name: jiomart_settlement
  column_name: zen_status
  source_declared_type: boolean
  data_type: boolean
  column_group: 3.5 System / Metadata
  semantic_role: classification_status_or_type
  business_meaning: Pipeline flag
  evidence_refs:
  - ev.jiomart.settlement.3_schema_details_40_columns
  confidence: high
  review_status: ready
```


```yaml
candidate_card:
  card_type: column
  card_id: column.zs_observe.jiomart_settlement.sheetname
  display_name: jiomart_settlement.sheetname
  table_id: table.zs_observe.jiomart_settlement
  schema: zs_observe
  table_name: jiomart_settlement
  column_name: sheetname
  source_declared_type: varchar
  data_type: varchar
  column_group: 3.5 System / Metadata
  semantic_role: general_marketplace_attribute
  business_meaning: Source sheet
  evidence_refs:
  - ev.jiomart.settlement.3_schema_details_40_columns
  confidence: high
  review_status: ready
```


```yaml
candidate_card:
  card_type: column
  card_id: column.zs_observe.jiomart_settlement.zen_sheet_name
  display_name: jiomart_settlement.zen_sheet_name
  table_id: table.zs_observe.jiomart_settlement
  schema: zs_observe
  table_name: jiomart_settlement
  column_name: zen_sheet_name
  source_declared_type: varchar
  data_type: varchar
  column_group: 3.5 System / Metadata
  semantic_role: general_marketplace_attribute
  business_meaning: Source sheet
  evidence_refs:
  - ev.jiomart.settlement.3_schema_details_40_columns
  confidence: high
  review_status: ready
```


```yaml
candidate_card:
  card_type: column
  card_id: column.zs_observe.jiomart_settlement.ancestry
  display_name: jiomart_settlement.ancestry
  table_id: table.zs_observe.jiomart_settlement
  schema: zs_observe
  table_name: jiomart_settlement
  column_name: ancestry
  source_declared_type: varchar
  data_type: varchar
  column_group: 3.5 System / Metadata
  semantic_role: general_marketplace_attribute
  business_meaning: Lineage
  evidence_refs:
  - ev.jiomart.settlement.3_schema_details_40_columns
  confidence: high
  review_status: ready
```


```yaml
candidate_card:
  card_type: column
  card_id: column.zs_observe.jiomart_settlement.event_temp_old
  display_name: jiomart_settlement.event_temp_old
  table_id: table.zs_observe.jiomart_settlement
  schema: zs_observe
  table_name: jiomart_settlement
  column_name: event_temp_old
  source_declared_type: varchar
  data_type: varchar
  column_group: 3.5 System / Metadata
  semantic_role: classification_status_or_type
  business_meaning: Legacy event field
  evidence_refs:
  - ev.jiomart.settlement.3_schema_details_40_columns
  confidence: high
  review_status: ready
```


```yaml
candidate_card:
  card_type: column
  card_id: column.zs_observe.jiomart_returns.unique_id
  display_name: jiomart_returns.unique_id
  table_id: table.zs_observe.jiomart_returns
  schema: zs_observe
  table_name: jiomart_returns
  column_name: unique_id
  source_declared_type: varchar
  data_type: varchar
  column_group: 3.1 Identity Columns
  semantic_role: identity_or_join_key
  business_meaning: Row identifier
  evidence_refs:
  - ev.jiomart.returns.3_schema_details_53_columns
  confidence: high
  review_status: ready
```


```yaml
candidate_card:
  card_type: column
  card_id: column.zs_observe.jiomart_returns.txn_uuid
  display_name: jiomart_returns.txn_uuid
  table_id: table.zs_observe.jiomart_returns
  schema: zs_observe
  table_name: jiomart_returns
  column_name: txn_uuid
  source_declared_type: varchar
  data_type: varchar
  column_group: 3.1 Identity Columns
  semantic_role: identity_or_join_key
  business_meaning: Pipeline UUID
  evidence_refs:
  - ev.jiomart.returns.3_schema_details_53_columns
  confidence: high
  review_status: ready
```


```yaml
candidate_card:
  card_type: column
  card_id: column.zs_observe.jiomart_returns.unique_value
  display_name: jiomart_returns.unique_value
  table_id: table.zs_observe.jiomart_returns
  schema: zs_observe
  table_name: jiomart_returns
  column_name: unique_value
  source_declared_type: varchar
  data_type: varchar
  column_group: 3.1 Identity Columns
  semantic_role: financial_amount_or_rate
  business_meaning: Dedup hash
  evidence_refs:
  - ev.jiomart.returns.3_schema_details_53_columns
  confidence: high
  review_status: ready
```


```yaml
candidate_card:
  card_type: column
  card_id: column.zs_observe.jiomart_returns.invoice_number
  display_name: jiomart_returns.invoice_number
  table_id: table.zs_observe.jiomart_returns
  schema: zs_observe
  table_name: jiomart_returns
  column_name: invoice_number
  source_declared_type: varchar
  data_type: varchar
  column_group: 3.1 Identity Columns
  semantic_role: identity_or_join_key
  business_meaning: JioMart invoice number — **join key to jiomart_oms**
  evidence_refs:
  - ev.jiomart.returns.3_schema_details_53_columns
  confidence: high
  review_status: ready
```


```yaml
candidate_card:
  card_type: column
  card_id: column.zs_observe.jiomart_returns.order_id
  display_name: jiomart_returns.order_id
  table_id: table.zs_observe.jiomart_returns
  schema: zs_observe
  table_name: jiomart_returns
  column_name: order_id
  source_declared_type: varchar
  data_type: varchar
  column_group: 3.1 Identity Columns
  semantic_role: identity_or_join_key
  business_meaning: Order ID — join key to oms and settlement
  evidence_refs:
  - ev.jiomart.returns.3_schema_details_53_columns
  confidence: high
  review_status: ready
```


```yaml
candidate_card:
  card_type: column
  card_id: column.zs_observe.jiomart_returns.item_id
  display_name: jiomart_returns.item_id
  table_id: table.zs_observe.jiomart_returns
  schema: zs_observe
  table_name: jiomart_returns
  column_name: item_id
  source_declared_type: varchar
  data_type: varchar
  column_group: 3.1 Identity Columns
  semantic_role: identity_or_join_key
  business_meaning: Line item ID
  evidence_refs:
  - ev.jiomart.returns.3_schema_details_53_columns
  confidence: high
  review_status: ready
```


```yaml
candidate_card:
  card_type: column
  card_id: column.zs_observe.jiomart_returns.sku_id
  display_name: jiomart_returns.sku_id
  table_id: table.zs_observe.jiomart_returns
  schema: zs_observe
  table_name: jiomart_returns
  column_name: sku_id
  source_declared_type: varchar
  data_type: varchar
  column_group: 3.1 Identity Columns
  semantic_role: product_catalog
  business_meaning: Seller SKU code
  evidence_refs:
  - ev.jiomart.returns.3_schema_details_53_columns
  confidence: high
  review_status: ready
```


```yaml
candidate_card:
  card_type: column
  card_id: column.zs_observe.jiomart_returns.sku
  display_name: jiomart_returns.sku
  table_id: table.zs_observe.jiomart_returns
  schema: zs_observe
  table_name: jiomart_returns
  column_name: sku
  source_declared_type: varchar
  data_type: varchar
  column_group: 3.1 Identity Columns
  semantic_role: product_catalog
  business_meaning: SKU alternate
  evidence_refs:
  - ev.jiomart.returns.3_schema_details_53_columns
  confidence: high
  review_status: ready
```


```yaml
candidate_card:
  card_type: column
  card_id: column.zs_observe.jiomart_returns.ean
  display_name: jiomart_returns.ean
  table_id: table.zs_observe.jiomart_returns
  schema: zs_observe
  table_name: jiomart_returns
  column_name: ean
  source_declared_type: varchar
  data_type: varchar
  column_group: 3.1 Identity Columns
  semantic_role: product_catalog
  business_meaning: EAN barcode
  evidence_refs:
  - ev.jiomart.returns.3_schema_details_53_columns
  confidence: high
  review_status: ready
```


```yaml
candidate_card:
  card_type: column
  card_id: column.zs_observe.jiomart_returns.forward_shipment_no
  display_name: jiomart_returns.forward_shipment_no
  table_id: table.zs_observe.jiomart_returns
  schema: zs_observe
  table_name: jiomart_returns
  column_name: forward_shipment_no
  source_declared_type: varchar
  data_type: varchar
  column_group: 3.1 Identity Columns
  semantic_role: marketplace_fulfillment_identifier
  business_meaning: Forward AWB / shipment number
  evidence_refs:
  - ev.jiomart.returns.3_schema_details_53_columns
  confidence: high
  review_status: ready
```


```yaml
candidate_card:
  card_type: column
  card_id: column.zs_observe.jiomart_returns.return_awb_number
  display_name: jiomart_returns.return_awb_number
  table_id: table.zs_observe.jiomart_returns
  schema: zs_observe
  table_name: jiomart_returns
  column_name: return_awb_number
  source_declared_type: varchar
  data_type: varchar
  column_group: 3.1 Identity Columns
  semantic_role: marketplace_fulfillment_identifier
  business_meaning: Return AWB number (courier tracking)
  evidence_refs:
  - ev.jiomart.returns.3_schema_details_53_columns
  confidence: high
  review_status: ready
```


```yaml
candidate_card:
  card_type: column
  card_id: column.zs_observe.jiomart_returns.return_awb_no
  display_name: jiomart_returns.return_awb_no
  table_id: table.zs_observe.jiomart_returns
  schema: zs_observe
  table_name: jiomart_returns
  column_name: return_awb_no
  source_declared_type: varchar
  data_type: varchar
  column_group: 3.1 Identity Columns
  semantic_role: marketplace_fulfillment_identifier
  business_meaning: Return AWB alternate field
  evidence_refs:
  - ev.jiomart.returns.3_schema_details_53_columns
  confidence: high
  review_status: ready
```


```yaml
candidate_card:
  card_type: column
  card_id: column.zs_observe.jiomart_returns.return_shipment_no
  display_name: jiomart_returns.return_shipment_no
  table_id: table.zs_observe.jiomart_returns
  schema: zs_observe
  table_name: jiomart_returns
  column_name: return_shipment_no
  source_declared_type: varchar
  data_type: varchar
  column_group: 3.1 Identity Columns
  semantic_role: marketplace_fulfillment_identifier
  business_meaning: Return shipment number
  evidence_refs:
  - ev.jiomart.returns.3_schema_details_53_columns
  confidence: high
  review_status: ready
```


```yaml
candidate_card:
  card_type: column
  card_id: column.zs_observe.jiomart_returns.created_date
  display_name: jiomart_returns.created_date
  table_id: table.zs_observe.jiomart_returns
  schema: zs_observe
  table_name: jiomart_returns
  column_name: created_date
  source_declared_type: timestamp
  data_type: timestamp
  column_group: 3.2 Date Columns
  semantic_role: date_time
  business_meaning: Record creation timestamp
  evidence_refs:
  - ev.jiomart.returns.3_schema_details_53_columns
  confidence: high
  review_status: ready
```


```yaml
candidate_card:
  card_type: column
  card_id: column.zs_observe.jiomart_returns.order_date
  display_name: jiomart_returns.order_date
  table_id: table.zs_observe.jiomart_returns
  schema: zs_observe
  table_name: jiomart_returns
  column_name: order_date
  source_declared_type: varchar
  data_type: varchar
  column_group: 3.2 Date Columns
  semantic_role: date_time
  business_meaning: Original order date
  evidence_refs:
  - ev.jiomart.returns.3_schema_details_53_columns
  confidence: high
  review_status: ready
```


```yaml
candidate_card:
  card_type: column
  card_id: column.zs_observe.jiomart_returns.return_initiate_date
  display_name: jiomart_returns.return_initiate_date
  table_id: table.zs_observe.jiomart_returns
  schema: zs_observe
  table_name: jiomart_returns
  column_name: return_initiate_date
  source_declared_type: varchar
  data_type: varchar
  column_group: 3.2 Date Columns
  semantic_role: date_time
  business_meaning: Date return was initiated by buyer
  evidence_refs:
  - ev.jiomart.returns.3_schema_details_53_columns
  confidence: high
  review_status: ready
```


```yaml
candidate_card:
  card_type: column
  card_id: column.zs_observe.jiomart_returns.return_date
  display_name: jiomart_returns.return_date
  table_id: table.zs_observe.jiomart_returns
  schema: zs_observe
  table_name: jiomart_returns
  column_name: return_date
  source_declared_type: timestamp
  data_type: timestamp
  column_group: 3.2 Date Columns
  semantic_role: date_time
  business_meaning: Return date (JioMart system)
  evidence_refs:
  - ev.jiomart.returns.3_schema_details_53_columns
  confidence: high
  review_status: ready
```


```yaml
candidate_card:
  card_type: column
  card_id: column.zs_observe.jiomart_returns.return_delivery_date
  display_name: jiomart_returns.return_delivery_date
  table_id: table.zs_observe.jiomart_returns
  schema: zs_observe
  table_name: jiomart_returns
  column_name: return_delivery_date
  source_declared_type: varchar
  data_type: varchar
  column_group: 3.2 Date Columns
  semantic_role: date_time
  business_meaning: Date return was delivered back to seller
  evidence_refs:
  - ev.jiomart.returns.3_schema_details_53_columns
  confidence: high
  review_status: ready
```


```yaml
candidate_card:
  card_type: column
  card_id: column.zs_observe.jiomart_returns.forward_delivery_date
  display_name: jiomart_returns.forward_delivery_date
  table_id: table.zs_observe.jiomart_returns
  schema: zs_observe
  table_name: jiomart_returns
  column_name: forward_delivery_date
  source_declared_type: varchar
  data_type: varchar
  column_group: 3.2 Date Columns
  semantic_role: date_time
  business_meaning: Original delivery date to buyer
  evidence_refs:
  - ev.jiomart.returns.3_schema_details_53_columns
  confidence: high
  review_status: ready
```


```yaml
candidate_card:
  card_type: column
  card_id: column.zs_observe.jiomart_returns.charged_amount
  display_name: jiomart_returns.charged_amount
  table_id: table.zs_observe.jiomart_returns
  schema: zs_observe
  table_name: jiomart_returns
  column_name: charged_amount
  source_declared_type: varchar
  data_type: varchar
  column_group: 3.3 Financial Columns
  semantic_role: financial_amount_or_rate
  business_meaning: Original sale value — **stored as varchar; cast to DOUBLE**
  cast_required: Stored as varchar; cast to DOUBLE before aggregation.
  evidence_refs:
  - ev.jiomart.returns.3_schema_details_53_columns
  confidence: high
  review_status: ready
```


```yaml
candidate_card:
  card_type: column
  card_id: column.zs_observe.jiomart_returns.refund_amount
  display_name: jiomart_returns.refund_amount
  table_id: table.zs_observe.jiomart_returns
  schema: zs_observe
  table_name: jiomart_returns
  column_name: refund_amount
  source_declared_type: varchar
  data_type: varchar
  column_group: 3.3 Financial Columns
  semantic_role: financial_amount_or_rate
  business_meaning: Refund issued to buyer — **stored as varchar; cast to DOUBLE**
  cast_required: Stored as varchar; cast to DOUBLE before aggregation.
  evidence_refs:
  - ev.jiomart.returns.3_schema_details_53_columns
  confidence: high
  review_status: ready
```


```yaml
candidate_card:
  card_type: column
  card_id: column.zs_observe.jiomart_returns.invoice_amount
  display_name: jiomart_returns.invoice_amount
  table_id: table.zs_observe.jiomart_returns
  schema: zs_observe
  table_name: jiomart_returns
  column_name: invoice_amount
  source_declared_type: varchar
  data_type: varchar
  column_group: 3.3 Financial Columns
  semantic_role: financial_amount_or_rate
  business_meaning: Invoice amount — stored as varchar
  cast_required: Stored as varchar; cast to DOUBLE before aggregation.
  evidence_refs:
  - ev.jiomart.returns.3_schema_details_53_columns
  confidence: high
  review_status: ready
```


```yaml
candidate_card:
  card_type: column
  card_id: column.zs_observe.jiomart_returns.pre_delivery_claims
  display_name: jiomart_returns.pre_delivery_claims
  table_id: table.zs_observe.jiomart_returns
  schema: zs_observe
  table_name: jiomart_returns
  column_name: pre_delivery_claims
  source_declared_type: varchar
  data_type: varchar
  column_group: 3.3 Financial Columns
  semantic_role: general_marketplace_attribute
  business_meaning: Claims before delivery (mostly NULL)
  evidence_refs:
  - ev.jiomart.returns.3_schema_details_53_columns
  confidence: high
  review_status: ready
```


```yaml
candidate_card:
  card_type: column
  card_id: column.zs_observe.jiomart_returns.post_delivery_claims
  display_name: jiomart_returns.post_delivery_claims
  table_id: table.zs_observe.jiomart_returns
  schema: zs_observe
  table_name: jiomart_returns
  column_name: post_delivery_claims
  source_declared_type: varchar
  data_type: varchar
  column_group: 3.3 Financial Columns
  semantic_role: classification_status_or_type
  business_meaning: Post-delivery claim status (`Closed`)
  evidence_refs:
  - ev.jiomart.returns.3_schema_details_53_columns
  confidence: high
  review_status: ready
```


```yaml
candidate_card:
  card_type: column
  card_id: column.zs_observe.jiomart_returns.transaction_type
  display_name: jiomart_returns.transaction_type
  table_id: table.zs_observe.jiomart_returns
  schema: zs_observe
  table_name: jiomart_returns
  column_name: transaction_type
  source_declared_type: varchar
  data_type: varchar
  column_group: 3.4 Classification Columns
  semantic_role: classification_status_or_type
  business_meaning: '`ReturnToOrigin`, `DoorStepReturn`, `BeforeShippingReturn`'
  evidence_refs:
  - ev.jiomart.returns.3_schema_details_53_columns
  confidence: high
  review_status: ready
```


```yaml
candidate_card:
  card_type: column
  card_id: column.zs_observe.jiomart_returns.return_type
  display_name: jiomart_returns.return_type
  table_id: table.zs_observe.jiomart_returns
  schema: zs_observe
  table_name: jiomart_returns
  column_name: return_type
  source_declared_type: varchar
  data_type: varchar
  column_group: 3.4 Classification Columns
  semantic_role: classification_status_or_type
  business_meaning: Same as `transaction_type`
  evidence_refs:
  - ev.jiomart.returns.3_schema_details_53_columns
  confidence: high
  review_status: ready
```


```yaml
candidate_card:
  card_type: column
  card_id: column.zs_observe.jiomart_returns.return_status
  display_name: jiomart_returns.return_status
  table_id: table.zs_observe.jiomart_returns
  schema: zs_observe
  table_name: jiomart_returns
  column_name: return_status
  source_declared_type: varchar
  data_type: varchar
  column_group: 3.4 Classification Columns
  semantic_role: classification_status_or_type
  business_meaning: '`complete`, `init`'
  evidence_refs:
  - ev.jiomart.returns.3_schema_details_53_columns
  confidence: high
  review_status: ready
```


```yaml
candidate_card:
  card_type: column
  card_id: column.zs_observe.jiomart_returns.order_status
  display_name: jiomart_returns.order_status
  table_id: table.zs_observe.jiomart_returns
  schema: zs_observe
  table_name: jiomart_returns
  column_name: order_status
  source_declared_type: varchar
  data_type: varchar
  column_group: 3.4 Classification Columns
  semantic_role: classification_status_or_type
  business_meaning: '`complete`, `init`'
  evidence_refs:
  - ev.jiomart.returns.3_schema_details_53_columns
  confidence: high
  review_status: ready
```


```yaml
candidate_card:
  card_type: column
  card_id: column.zs_observe.jiomart_returns.payment_mode
  display_name: jiomart_returns.payment_mode
  table_id: table.zs_observe.jiomart_returns
  schema: zs_observe
  table_name: jiomart_returns
  column_name: payment_mode
  source_declared_type: varchar
  data_type: varchar
  column_group: 3.4 Classification Columns
  semantic_role: classification_status_or_type
  business_meaning: '`COD`, `Prepaid_Payments`'
  evidence_refs:
  - ev.jiomart.returns.3_schema_details_53_columns
  confidence: high
  review_status: ready
```


```yaml
candidate_card:
  card_type: column
  card_id: column.zs_observe.jiomart_returns.payment_method
  display_name: jiomart_returns.payment_method
  table_id: table.zs_observe.jiomart_returns
  schema: zs_observe
  table_name: jiomart_returns
  column_name: payment_method
  source_declared_type: varchar
  data_type: varchar
  column_group: 3.4 Classification Columns
  semantic_role: classification_status_or_type
  business_meaning: '`Prepaid_Payments`, `COD`'
  evidence_refs:
  - ev.jiomart.returns.3_schema_details_53_columns
  confidence: high
  review_status: ready
```


```yaml
candidate_card:
  card_type: column
  card_id: column.zs_observe.jiomart_returns.reason
  display_name: jiomart_returns.reason
  table_id: table.zs_observe.jiomart_returns
  schema: zs_observe
  table_name: jiomart_returns
  column_name: reason
  source_declared_type: varchar
  data_type: varchar
  column_group: 3.4 Classification Columns
  semantic_role: classification_status_or_type
  business_meaning: Return reason (mostly NULL)
  evidence_refs:
  - ev.jiomart.returns.3_schema_details_53_columns
  confidence: high
  review_status: ready
```


```yaml
candidate_card:
  card_type: column
  card_id: column.zs_observe.jiomart_returns.quantity
  display_name: jiomart_returns.quantity
  table_id: table.zs_observe.jiomart_returns
  schema: zs_observe
  table_name: jiomart_returns
  column_name: quantity
  source_declared_type: varchar/integer
  data_type: varchar/integer
  column_group: 3.4 Classification Columns
  semantic_role: general_marketplace_attribute
  business_meaning: Quantity returned
  evidence_refs:
  - ev.jiomart.returns.3_schema_details_53_columns
  confidence: high
  review_status: ready
```


```yaml
candidate_card:
  card_type: column
  card_id: column.zs_observe.jiomart_returns.qty
  display_name: jiomart_returns.qty
  table_id: table.zs_observe.jiomart_returns
  schema: zs_observe
  table_name: jiomart_returns
  column_name: qty
  source_declared_type: varchar/integer
  data_type: varchar/integer
  column_group: 3.4 Classification Columns
  semantic_role: general_marketplace_attribute
  business_meaning: Quantity returned
  evidence_refs:
  - ev.jiomart.returns.3_schema_details_53_columns
  confidence: high
  review_status: ready
```


```yaml
candidate_card:
  card_type: column
  card_id: column.zs_observe.jiomart_returns.courier_partner
  display_name: jiomart_returns.courier_partner
  table_id: table.zs_observe.jiomart_returns
  schema: zs_observe
  table_name: jiomart_returns
  column_name: courier_partner
  source_declared_type: varchar
  data_type: varchar
  column_group: 3.5 Logistics Columns
  semantic_role: marketplace_fulfillment_identifier
  business_meaning: '`Delhivery`, `Shadowfax`, `Xpressbees Express`'
  evidence_refs:
  - ev.jiomart.returns.3_schema_details_53_columns
  confidence: high
  review_status: ready
```


```yaml
candidate_card:
  card_type: column
  card_id: column.zs_observe.jiomart_returns.fulfillment_channel
  display_name: jiomart_returns.fulfillment_channel
  table_id: table.zs_observe.jiomart_returns
  schema: zs_observe
  table_name: jiomart_returns
  column_name: fulfillment_channel
  source_declared_type: varchar
  data_type: varchar
  column_group: 3.5 Logistics Columns
  semantic_role: marketplace_fulfillment_identifier
  business_meaning: Channel used
  evidence_refs:
  - ev.jiomart.returns.3_schema_details_53_columns
  confidence: high
  review_status: ready
```


```yaml
candidate_card:
  card_type: column
  card_id: column.zs_observe.jiomart_returns.fulfillment_center
  display_name: jiomart_returns.fulfillment_center
  table_id: table.zs_observe.jiomart_returns
  schema: zs_observe
  table_name: jiomart_returns
  column_name: fulfillment_center
  source_declared_type: varchar
  data_type: varchar
  column_group: 3.5 Logistics Columns
  semantic_role: marketplace_fulfillment_identifier
  business_meaning: JioMart fulfilment centre (e.g., `Central BLR Warehouse 560083`)
  evidence_refs:
  - ev.jiomart.returns.3_schema_details_53_columns
  confidence: high
  review_status: ready
```


```yaml
candidate_card:
  card_type: column
  card_id: column.zs_observe.jiomart_returns.description
  display_name: jiomart_returns.description
  table_id: table.zs_observe.jiomart_returns
  schema: zs_observe
  table_name: jiomart_returns
  column_name: description
  source_declared_type: varchar
  data_type: varchar
  column_group: 3.5 Logistics Columns
  semantic_role: product_catalog
  business_meaning: Product description
  evidence_refs:
  - ev.jiomart.returns.3_schema_details_53_columns
  confidence: high
  review_status: ready
```


```yaml
candidate_card:
  card_type: column
  card_id: column.zs_observe.jiomart_returns.product_title
  display_name: jiomart_returns.product_title
  table_id: table.zs_observe.jiomart_returns
  schema: zs_observe
  table_name: jiomart_returns
  column_name: product_title
  source_declared_type: varchar
  data_type: varchar
  column_group: 3.5 Logistics Columns
  semantic_role: product_catalog
  business_meaning: Product title
  evidence_refs:
  - ev.jiomart.returns.3_schema_details_53_columns
  confidence: high
  review_status: ready
```


```yaml
candidate_card:
  card_type: column
  card_id: column.zs_observe.jiomart_returns.group_level_id
  display_name: jiomart_returns.group_level_id
  table_id: table.zs_observe.jiomart_returns
  schema: zs_observe
  table_name: jiomart_returns
  column_name: group_level_id
  source_declared_type: integer
  data_type: integer
  column_group: 3.6 System / Metadata
  semantic_role: scope_column_preserved_not_card_boundary
  business_meaning: '`26`'
  scope_note: Scope-like field retained as a source column/filter/value only; do not create tenant/group/account cards.
  evidence_refs:
  - ev.jiomart.returns.3_schema_details_53_columns
  confidence: high
  review_status: ready
```


```yaml
candidate_card:
  card_type: column
  card_id: column.zs_observe.jiomart_returns.currency_type
  display_name: jiomart_returns.currency_type
  table_id: table.zs_observe.jiomart_returns
  schema: zs_observe
  table_name: jiomart_returns
  column_name: currency_type
  source_declared_type: varchar
  data_type: varchar
  column_group: 3.6 System / Metadata
  semantic_role: classification_status_or_type
  business_meaning: '`INR`'
  evidence_refs:
  - ev.jiomart.returns.3_schema_details_53_columns
  confidence: high
  review_status: ready
```


```yaml
candidate_card:
  card_type: column
  card_id: column.zs_observe.jiomart_returns.is_active
  display_name: jiomart_returns.is_active
  table_id: table.zs_observe.jiomart_returns
  schema: zs_observe
  table_name: jiomart_returns
  column_name: is_active
  source_declared_type: boolean
  data_type: boolean
  column_group: 3.6 System / Metadata
  semantic_role: general_marketplace_attribute
  business_meaning: Always `true`
  evidence_refs:
  - ev.jiomart.returns.3_schema_details_53_columns
  confidence: high
  review_status: ready
```


```yaml
candidate_card:
  card_type: column
  card_id: column.zs_observe.jiomart_returns.zen_sheet_name
  display_name: jiomart_returns.zen_sheet_name
  table_id: table.zs_observe.jiomart_returns
  schema: zs_observe
  table_name: jiomart_returns
  column_name: zen_sheet_name
  source_declared_type: varchar
  data_type: varchar
  column_group: 3.6 System / Metadata
  semantic_role: general_marketplace_attribute
  business_meaning: Source sheet
  evidence_refs:
  - ev.jiomart.returns.3_schema_details_53_columns
  confidence: high
  review_status: ready
```


```yaml
candidate_card:
  card_type: column
  card_id: column.zs_observe.jiomart_returns.ancestry
  display_name: jiomart_returns.ancestry
  table_id: table.zs_observe.jiomart_returns
  schema: zs_observe
  table_name: jiomart_returns
  column_name: ancestry
  source_declared_type: varchar
  data_type: varchar
  column_group: 3.6 System / Metadata
  semantic_role: general_marketplace_attribute
  business_meaning: Lineage
  evidence_refs:
  - ev.jiomart.returns.3_schema_details_53_columns
  confidence: high
  review_status: ready
```


```yaml
candidate_card:
  card_type: column
  card_id: column.zs_observe.jiomart_oms.unique_id
  display_name: jiomart_oms.unique_id
  table_id: table.zs_observe.jiomart_oms
  schema: zs_observe
  table_name: jiomart_oms
  column_name: unique_id
  source_declared_type: varchar
  data_type: varchar
  column_group: 3.1 Identity Columns
  semantic_role: identity_or_join_key
  business_meaning: System row identifier
  evidence_refs:
  - ev.jiomart.oms.3_schema_details_115_columns
  confidence: high
  review_status: ready
```


```yaml
candidate_card:
  card_type: column
  card_id: column.zs_observe.jiomart_oms.txn_uuid
  display_name: jiomart_oms.txn_uuid
  table_id: table.zs_observe.jiomart_oms
  schema: zs_observe
  table_name: jiomart_oms
  column_name: txn_uuid
  source_declared_type: varchar
  data_type: varchar
  column_group: 3.1 Identity Columns
  semantic_role: identity_or_join_key
  business_meaning: Pipeline UUID
  evidence_refs:
  - ev.jiomart.oms.3_schema_details_115_columns
  confidence: high
  review_status: ready
```


```yaml
candidate_card:
  card_type: column
  card_id: column.zs_observe.jiomart_oms.unique_value
  display_name: jiomart_oms.unique_value
  table_id: table.zs_observe.jiomart_oms
  schema: zs_observe
  table_name: jiomart_oms
  column_name: unique_value
  source_declared_type: varchar
  data_type: varchar
  column_group: 3.1 Identity Columns
  semantic_role: financial_amount_or_rate
  business_meaning: Deduplication hash
  evidence_refs:
  - ev.jiomart.oms.3_schema_details_115_columns
  confidence: high
  review_status: ready
```


```yaml
candidate_card:
  card_type: column
  card_id: column.zs_observe.jiomart_oms.invoice_number
  display_name: jiomart_oms.invoice_number
  table_id: table.zs_observe.jiomart_oms
  schema: zs_observe
  table_name: jiomart_oms
  column_name: invoice_number
  source_declared_type: varchar
  data_type: varchar
  column_group: 3.1 Identity Columns
  semantic_role: identity_or_join_key
  business_meaning: 'JioMart seller invoice number (format: `S29BZXSO7FA35884`)'
  evidence_refs:
  - ev.jiomart.oms.3_schema_details_115_columns
  confidence: high
  review_status: ready
```


```yaml
candidate_card:
  card_type: column
  card_id: column.zs_observe.jiomart_oms.original_invoice_id
  display_name: jiomart_oms.original_invoice_id
  table_id: table.zs_observe.jiomart_oms
  schema: zs_observe
  table_name: jiomart_oms
  column_name: original_invoice_id
  source_declared_type: varchar
  data_type: varchar
  column_group: 3.1 Identity Columns
  semantic_role: identity_or_join_key
  business_meaning: Original invoice reference
  evidence_refs:
  - ev.jiomart.oms.3_schema_details_115_columns
  confidence: high
  review_status: ready
```


```yaml
candidate_card:
  card_type: column
  card_id: column.zs_observe.jiomart_oms.buyer_invoice_id
  display_name: jiomart_oms.buyer_invoice_id
  table_id: table.zs_observe.jiomart_oms
  schema: zs_observe
  table_name: jiomart_oms
  column_name: buyer_invoice_id
  source_declared_type: varchar
  data_type: varchar
  column_group: 3.1 Identity Columns
  semantic_role: identity_or_join_key
  business_meaning: Buyer-facing invoice number
  evidence_refs:
  - ev.jiomart.oms.3_schema_details_115_columns
  confidence: high
  review_status: ready
```


```yaml
candidate_card:
  card_type: column
  card_id: column.zs_observe.jiomart_oms.order_id
  display_name: jiomart_oms.order_id
  table_id: table.zs_observe.jiomart_oms
  schema: zs_observe
  table_name: jiomart_oms
  column_name: order_id
  source_declared_type: varchar
  data_type: varchar
  column_group: 3.1 Identity Columns
  semantic_role: identity_or_join_key
  business_meaning: 'JioMart order ID (format: `17620898178181505759J`)'
  evidence_refs:
  - ev.jiomart.oms.3_schema_details_115_columns
  confidence: high
  review_status: ready
```


```yaml
candidate_card:
  card_type: column
  card_id: column.zs_observe.jiomart_oms.item_id
  display_name: jiomart_oms.item_id
  table_id: table.zs_observe.jiomart_oms
  schema: zs_observe
  table_name: jiomart_oms
  column_name: item_id
  source_declared_type: varchar
  data_type: varchar
  column_group: 3.1 Identity Columns
  semantic_role: identity_or_join_key
  business_meaning: Line item ID
  evidence_refs:
  - ev.jiomart.oms.3_schema_details_115_columns
  confidence: high
  review_status: ready
```


```yaml
candidate_card:
  card_type: column
  card_id: column.zs_observe.jiomart_oms.order_item_id
  display_name: jiomart_oms.order_item_id
  table_id: table.zs_observe.jiomart_oms
  schema: zs_observe
  table_name: jiomart_oms
  column_name: order_item_id
  source_declared_type: varchar
  data_type: varchar
  column_group: 3.1 Identity Columns
  semantic_role: identity_or_join_key
  business_meaning: Order item ID (newer format)
  evidence_refs:
  - ev.jiomart.oms.3_schema_details_115_columns
  confidence: high
  review_status: ready
```


```yaml
candidate_card:
  card_type: column
  card_id: column.zs_observe.jiomart_oms.parent_id
  display_name: jiomart_oms.parent_id
  table_id: table.zs_observe.jiomart_oms
  schema: zs_observe
  table_name: jiomart_oms
  column_name: parent_id
  source_declared_type: varchar
  data_type: varchar
  column_group: 3.1 Identity Columns
  semantic_role: identity_or_join_key
  business_meaning: Parent order reference
  evidence_refs:
  - ev.jiomart.oms.3_schema_details_115_columns
  confidence: high
  review_status: ready
```


```yaml
candidate_card:
  card_type: column
  card_id: column.zs_observe.jiomart_oms.shipment_number
  display_name: jiomart_oms.shipment_number
  table_id: table.zs_observe.jiomart_oms
  schema: zs_observe
  table_name: jiomart_oms
  column_name: shipment_number
  source_declared_type: varchar
  data_type: varchar
  column_group: 3.1 Identity Columns
  semantic_role: marketplace_fulfillment_identifier
  business_meaning: Shipment tracking number (NULL for older rows)
  evidence_refs:
  - ev.jiomart.oms.3_schema_details_115_columns
  confidence: high
  review_status: ready
```


```yaml
candidate_card:
  card_type: column
  card_id: column.zs_observe.jiomart_oms.original_shipment_number
  display_name: jiomart_oms.original_shipment_number
  table_id: table.zs_observe.jiomart_oms
  schema: zs_observe
  table_name: jiomart_oms
  column_name: original_shipment_number
  source_declared_type: varchar
  data_type: varchar
  column_group: 3.1 Identity Columns
  semantic_role: marketplace_fulfillment_identifier
  business_meaning: Original shipment number
  evidence_refs:
  - ev.jiomart.oms.3_schema_details_115_columns
  confidence: high
  review_status: ready
```


```yaml
candidate_card:
  card_type: column
  card_id: column.zs_observe.jiomart_oms.mp_sin
  display_name: jiomart_oms.mp_sin
  table_id: table.zs_observe.jiomart_oms
  schema: zs_observe
  table_name: jiomart_oms
  column_name: mp_sin
  source_declared_type: varchar
  data_type: varchar
  column_group: 3.1 Identity Columns
  semantic_role: product_catalog
  business_meaning: JioMart product SIN — catalogue identifier (e.g., `RVKBCGYVWK`) — **always populated**
  evidence_refs:
  - ev.jiomart.oms.3_schema_details_115_columns
  confidence: high
  review_status: ready
```


```yaml
candidate_card:
  card_type: column
  card_id: column.zs_observe.jiomart_oms.sku_id
  display_name: jiomart_oms.sku_id
  table_id: table.zs_observe.jiomart_oms
  schema: zs_observe
  table_name: jiomart_oms
  column_name: sku_id
  source_declared_type: varchar
  data_type: varchar
  column_group: 3.1 Identity Columns
  semantic_role: product_catalog
  business_meaning: Seller SKU (e.g., `C5102_1`)
  evidence_refs:
  - ev.jiomart.oms.3_schema_details_115_columns
  confidence: high
  review_status: ready
```


```yaml
candidate_card:
  card_type: column
  card_id: column.zs_observe.jiomart_oms.sku
  display_name: jiomart_oms.sku
  table_id: table.zs_observe.jiomart_oms
  schema: zs_observe
  table_name: jiomart_oms
  column_name: sku
  source_declared_type: varchar
  data_type: varchar
  column_group: 3.1 Identity Columns
  semantic_role: product_catalog
  business_meaning: SKU alternate (NULL for \~37K older rows)
  evidence_refs:
  - ev.jiomart.oms.3_schema_details_115_columns
  confidence: high
  review_status: ready
```


```yaml
candidate_card:
  card_type: column
  card_id: column.zs_observe.jiomart_oms.fsn_product_id
  display_name: jiomart_oms.fsn___product_id
  table_id: table.zs_observe.jiomart_oms
  schema: zs_observe
  table_name: jiomart_oms
  column_name: fsn___product_id
  source_declared_type: varchar
  data_type: varchar
  column_group: 3.1 Identity Columns
  semantic_role: product_catalog
  business_meaning: Platform product ID
  evidence_refs:
  - ev.jiomart.oms.3_schema_details_115_columns
  confidence: high
  review_status: ready
```


```yaml
candidate_card:
  card_type: column
  card_id: column.zs_observe.jiomart_oms.source_gst_id
  display_name: jiomart_oms.source_gst_id
  table_id: table.zs_observe.jiomart_oms
  schema: zs_observe
  table_name: jiomart_oms
  column_name: source_gst_id
  source_declared_type: varchar
  data_type: varchar
  column_group: 3.1 Identity Columns
  semantic_role: scope_column_preserved_not_card_boundary
  business_meaning: Seller GSTIN
  scope_note: Scope-like field retained as a source column/filter/value only; do not create tenant/group/account cards.
  evidence_refs:
  - ev.jiomart.oms.3_schema_details_115_columns
  confidence: high
  review_status: ready
```


```yaml
candidate_card:
  card_type: column
  card_id: column.zs_observe.jiomart_oms.seller_gstin
  display_name: jiomart_oms.seller_gstin
  table_id: table.zs_observe.jiomart_oms
  schema: zs_observe
  table_name: jiomart_oms
  column_name: seller_gstin
  source_declared_type: varchar
  data_type: varchar
  column_group: 3.1 Identity Columns
  semantic_role: scope_column_preserved_not_card_boundary
  business_meaning: Seller GSTIN alternate
  scope_note: Scope-like field retained as a source column/filter/value only; do not create tenant/group/account cards.
  evidence_refs:
  - ev.jiomart.oms.3_schema_details_115_columns
  confidence: high
  review_status: ready
```


```yaml
candidate_card:
  card_type: column
  card_id: column.zs_observe.jiomart_oms.created_date
  display_name: jiomart_oms.created_date
  table_id: table.zs_observe.jiomart_oms
  schema: zs_observe
  table_name: jiomart_oms
  column_name: created_date
  source_declared_type: timestamp
  data_type: timestamp
  column_group: 3.2 Date Columns
  semantic_role: date_time
  business_meaning: Record creation timestamp — **primary reliable date**
  evidence_refs:
  - ev.jiomart.oms.3_schema_details_115_columns
  confidence: high
  review_status: ready
```


```yaml
candidate_card:
  card_type: column
  card_id: column.zs_observe.jiomart_oms.order_date
  display_name: jiomart_oms.order_date
  table_id: table.zs_observe.jiomart_oms
  schema: zs_observe
  table_name: jiomart_oms
  column_name: order_date
  source_declared_type: timestamp
  data_type: timestamp
  column_group: 3.2 Date Columns
  semantic_role: date_time
  business_meaning: Order placement date (NULL for \~37K older rows)
  evidence_refs:
  - ev.jiomart.oms.3_schema_details_115_columns
  confidence: high
  review_status: ready
```


```yaml
candidate_card:
  card_type: column
  card_id: column.zs_observe.jiomart_oms.order_approval_date
  display_name: jiomart_oms.order_approval_date
  table_id: table.zs_observe.jiomart_oms
  schema: zs_observe
  table_name: jiomart_oms
  column_name: order_approval_date
  source_declared_type: timestamp
  data_type: timestamp
  column_group: 3.2 Date Columns
  semantic_role: date_time
  business_meaning: Order approval
  evidence_refs:
  - ev.jiomart.oms.3_schema_details_115_columns
  confidence: high
  review_status: ready
```


```yaml
candidate_card:
  card_type: column
  card_id: column.zs_observe.jiomart_oms.buyer_invoice_date
  display_name: jiomart_oms.buyer_invoice_date
  table_id: table.zs_observe.jiomart_oms
  schema: zs_observe
  table_name: jiomart_oms
  column_name: buyer_invoice_date
  source_declared_type: timestamp
  data_type: timestamp
  column_group: 3.2 Date Columns
  semantic_role: date_time
  business_meaning: Buyer invoice date
  evidence_refs:
  - ev.jiomart.oms.3_schema_details_115_columns
  confidence: high
  review_status: ready
```


```yaml
candidate_card:
  card_type: column
  card_id: column.zs_observe.jiomart_oms.sale_sale_reversal_tcs_date
  display_name: jiomart_oms.sale_sale_reversal_tcs_date
  table_id: table.zs_observe.jiomart_oms
  schema: zs_observe
  table_name: jiomart_oms
  column_name: sale_sale_reversal_tcs_date
  source_declared_type: timestamp
  data_type: timestamp
  column_group: 3.2 Date Columns
  semantic_role: financial_amount_or_rate
  business_meaning: TCS deduction date
  evidence_refs:
  - ev.jiomart.oms.3_schema_details_115_columns
  confidence: high
  review_status: ready
```


```yaml
candidate_card:
  card_type: column
  card_id: column.zs_observe.jiomart_oms.charged_amount
  display_name: jiomart_oms.charged_amount
  table_id: table.zs_observe.jiomart_oms
  schema: zs_observe
  table_name: jiomart_oms
  column_name: charged_amount
  source_declared_type: decimal
  data_type: decimal
  column_group: 3.3 Financial Columns
  semantic_role: financial_amount_or_rate
  business_meaning: '**Buyer-facing price inclusive of GST** — primary GMV field'
  sign_or_context_semantics: Use transaction_type/order_status context; forward charged_amount is GMV and reverse rows represent
    returns/credit notes.
  evidence_refs:
  - ev.jiomart.oms.3_schema_details_115_columns
  confidence: high
  review_status: ready
```


```yaml
candidate_card:
  card_type: column
  card_id: column.zs_observe.jiomart_oms.charged_amount_excluding_tax
  display_name: jiomart_oms.charged_amount_excluding_tax
  table_id: table.zs_observe.jiomart_oms
  schema: zs_observe
  table_name: jiomart_oms
  column_name: charged_amount_excluding_tax
  source_declared_type: decimal
  data_type: decimal
  column_group: 3.3 Financial Columns
  semantic_role: financial_amount_or_rate
  business_meaning: Taxable base (excluding GST)
  evidence_refs:
  - ev.jiomart.oms.3_schema_details_115_columns
  confidence: high
  review_status: ready
```


```yaml
candidate_card:
  card_type: column
  card_id: column.zs_observe.jiomart_oms.taxable_value
  display_name: jiomart_oms.taxable_value
  table_id: table.zs_observe.jiomart_oms
  schema: zs_observe
  table_name: jiomart_oms
  column_name: taxable_value
  source_declared_type: decimal
  data_type: decimal
  column_group: 3.3 Financial Columns
  semantic_role: financial_amount_or_rate
  business_meaning: Taxable value (NULL for older rows — same as `charged_amount_excluding_tax`)
  evidence_refs:
  - ev.jiomart.oms.3_schema_details_115_columns
  confidence: high
  review_status: ready
```


```yaml
candidate_card:
  card_type: column
  card_id: column.zs_observe.jiomart_oms.offer_price
  display_name: jiomart_oms.offer_price
  table_id: table.zs_observe.jiomart_oms
  schema: zs_observe
  table_name: jiomart_oms
  column_name: offer_price
  source_declared_type: decimal
  data_type: decimal
  column_group: 3.3 Financial Columns
  semantic_role: financial_amount_or_rate
  business_meaning: Platform offer price
  evidence_refs:
  - ev.jiomart.oms.3_schema_details_115_columns
  confidence: high
  review_status: ready
```


```yaml
candidate_card:
  card_type: column
  card_id: column.zs_observe.jiomart_oms.buyer_invoice_amount
  display_name: jiomart_oms.buyer_invoice_amount
  table_id: table.zs_observe.jiomart_oms
  schema: zs_observe
  table_name: jiomart_oms
  column_name: buyer_invoice_amount
  source_declared_type: decimal
  data_type: decimal
  column_group: 3.3 Financial Columns
  semantic_role: financial_amount_or_rate
  business_meaning: Final buyer invoice amount
  evidence_refs:
  - ev.jiomart.oms.3_schema_details_115_columns
  confidence: high
  review_status: ready
```


```yaml
candidate_card:
  card_type: column
  card_id: column.zs_observe.jiomart_oms.final_invoice_amount
  display_name: jiomart_oms.final_invoice_amount
  table_id: table.zs_observe.jiomart_oms
  schema: zs_observe
  table_name: jiomart_oms
  column_name: final_invoice_amount
  source_declared_type: decimal
  data_type: decimal
  column_group: 3.3 Financial Columns
  semantic_role: financial_amount_or_rate
  business_meaning: Final invoice amount
  evidence_refs:
  - ev.jiomart.oms.3_schema_details_115_columns
  confidence: high
  review_status: ready
```


```yaml
candidate_card:
  card_type: column
  card_id: column.zs_observe.jiomart_oms.seller_coupon_amount
  display_name: jiomart_oms.seller_coupon_amount
  table_id: table.zs_observe.jiomart_oms
  schema: zs_observe
  table_name: jiomart_oms
  column_name: seller_coupon_amount
  source_declared_type: decimal
  data_type: decimal
  column_group: 3.3 Financial Columns
  semantic_role: financial_amount_or_rate
  business_meaning: Seller-funded coupon discount (negative = deduction)
  evidence_refs:
  - ev.jiomart.oms.3_schema_details_115_columns
  confidence: high
  review_status: ready
```


```yaml
candidate_card:
  card_type: column
  card_id: column.zs_observe.jiomart_oms.tax_igst_rate
  display_name: jiomart_oms.tax_igst_rate
  table_id: table.zs_observe.jiomart_oms
  schema: zs_observe
  table_name: jiomart_oms
  column_name: tax_igst_rate
  source_declared_type: decimal
  data_type: decimal
  column_group: 3.4 Tax Columns
  semantic_role: financial_amount_or_rate
  business_meaning: 'IGST rate: `0.0`, `0.05`, `0.12`, `0.18`'
  evidence_refs:
  - ev.jiomart.oms.3_schema_details_115_columns
  confidence: high
  review_status: ready
```


```yaml
candidate_card:
  card_type: column
  card_id: column.zs_observe.jiomart_oms.tax_igst_amount
  display_name: jiomart_oms.tax_igst_amount
  table_id: table.zs_observe.jiomart_oms
  schema: zs_observe
  table_name: jiomart_oms
  column_name: tax_igst_amount
  source_declared_type: decimal
  data_type: decimal
  column_group: 3.4 Tax Columns
  semantic_role: financial_amount_or_rate
  business_meaning: IGST amount (inter-state orders)
  evidence_refs:
  - ev.jiomart.oms.3_schema_details_115_columns
  confidence: high
  review_status: ready
```


```yaml
candidate_card:
  card_type: column
  card_id: column.zs_observe.jiomart_oms.tax_cgst_rate
  display_name: jiomart_oms.tax_cgst_rate
  table_id: table.zs_observe.jiomart_oms
  schema: zs_observe
  table_name: jiomart_oms
  column_name: tax_cgst_rate
  source_declared_type: decimal
  data_type: decimal
  column_group: 3.4 Tax Columns
  semantic_role: financial_amount_or_rate
  business_meaning: 'CGST rate: `0.0`, `0.025`, `0.06`, `0.09`'
  evidence_refs:
  - ev.jiomart.oms.3_schema_details_115_columns
  confidence: high
  review_status: ready
```


```yaml
candidate_card:
  card_type: column
  card_id: column.zs_observe.jiomart_oms.tax_cgst_amount
  display_name: jiomart_oms.tax_cgst_amount
  table_id: table.zs_observe.jiomart_oms
  schema: zs_observe
  table_name: jiomart_oms
  column_name: tax_cgst_amount
  source_declared_type: decimal
  data_type: decimal
  column_group: 3.4 Tax Columns
  semantic_role: financial_amount_or_rate
  business_meaning: CGST amount (intra-state orders)
  evidence_refs:
  - ev.jiomart.oms.3_schema_details_115_columns
  confidence: high
  review_status: ready
```


```yaml
candidate_card:
  card_type: column
  card_id: column.zs_observe.jiomart_oms.tax_sgst_rate
  display_name: jiomart_oms.tax_sgst_rate
  table_id: table.zs_observe.jiomart_oms
  schema: zs_observe
  table_name: jiomart_oms
  column_name: tax_sgst_rate
  source_declared_type: decimal
  data_type: decimal
  column_group: 3.4 Tax Columns
  semantic_role: financial_amount_or_rate
  business_meaning: SGST rate (mirrors CGST)
  evidence_refs:
  - ev.jiomart.oms.3_schema_details_115_columns
  confidence: high
  review_status: ready
```


```yaml
candidate_card:
  card_type: column
  card_id: column.zs_observe.jiomart_oms.tax_sgst_amount
  display_name: jiomart_oms.tax_sgst_amount
  table_id: table.zs_observe.jiomart_oms
  schema: zs_observe
  table_name: jiomart_oms
  column_name: tax_sgst_amount
  source_declared_type: decimal
  data_type: decimal
  column_group: 3.4 Tax Columns
  semantic_role: financial_amount_or_rate
  business_meaning: SGST amount
  evidence_refs:
  - ev.jiomart.oms.3_schema_details_115_columns
  confidence: high
  review_status: ready
```


```yaml
candidate_card:
  card_type: column
  card_id: column.zs_observe.jiomart_oms.type_of_tax
  display_name: jiomart_oms.type_of_tax
  table_id: table.zs_observe.jiomart_oms
  schema: zs_observe
  table_name: jiomart_oms
  column_name: type_of_tax
  source_declared_type: varchar
  data_type: varchar
  column_group: 3.4 Tax Columns
  semantic_role: financial_amount_or_rate
  business_meaning: '`GST` — 100%'
  evidence_refs:
  - ev.jiomart.oms.3_schema_details_115_columns
  confidence: high
  review_status: ready
```


```yaml
candidate_card:
  card_type: column
  card_id: column.zs_observe.jiomart_oms.hsn
  display_name: jiomart_oms.hsn
  table_id: table.zs_observe.jiomart_oms
  schema: zs_observe
  table_name: jiomart_oms
  column_name: hsn
  source_declared_type: varchar
  data_type: varchar
  column_group: 3.4 Tax Columns
  semantic_role: product_catalog
  business_meaning: HSN code — **primary field**
  evidence_refs:
  - ev.jiomart.oms.3_schema_details_115_columns
  confidence: high
  review_status: ready
```


```yaml
candidate_card:
  card_type: column
  card_id: column.zs_observe.jiomart_oms.hsn_code
  display_name: jiomart_oms.hsn_code
  table_id: table.zs_observe.jiomart_oms
  schema: zs_observe
  table_name: jiomart_oms
  column_name: hsn_code
  source_declared_type: varchar
  data_type: varchar
  column_group: 3.4 Tax Columns
  semantic_role: product_catalog
  business_meaning: HSN code alternate (NULL for older rows)
  evidence_refs:
  - ev.jiomart.oms.3_schema_details_115_columns
  confidence: high
  review_status: ready
```


```yaml
candidate_card:
  card_type: column
  card_id: column.zs_observe.jiomart_oms.hsn_generated
  display_name: jiomart_oms.hsn_generated
  table_id: table.zs_observe.jiomart_oms
  schema: zs_observe
  table_name: jiomart_oms
  column_name: hsn_generated
  source_declared_type: varchar
  data_type: varchar
  column_group: 3.4 Tax Columns
  semantic_role: financial_amount_or_rate
  business_meaning: System-generated HSN
  evidence_refs:
  - ev.jiomart.oms.3_schema_details_115_columns
  confidence: high
  review_status: ready
```


```yaml
candidate_card:
  card_type: column
  card_id: column.zs_observe.jiomart_oms.igst_rate
  display_name: jiomart_oms.igst_rate
  table_id: table.zs_observe.jiomart_oms
  schema: zs_observe
  table_name: jiomart_oms
  column_name: igst_rate
  source_declared_type: decimal
  data_type: decimal
  column_group: 3.4 Tax Columns
  semantic_role: financial_amount_or_rate
  business_meaning: Legacy IGST columns (older rows)
  evidence_refs:
  - ev.jiomart.oms.3_schema_details_115_columns
  confidence: high
  review_status: ready
```


```yaml
candidate_card:
  card_type: column
  card_id: column.zs_observe.jiomart_oms.igst_amount
  display_name: jiomart_oms.igst_amount
  table_id: table.zs_observe.jiomart_oms
  schema: zs_observe
  table_name: jiomart_oms
  column_name: igst_amount
  source_declared_type: decimal
  data_type: decimal
  column_group: 3.4 Tax Columns
  semantic_role: financial_amount_or_rate
  business_meaning: Legacy IGST columns (older rows)
  evidence_refs:
  - ev.jiomart.oms.3_schema_details_115_columns
  confidence: high
  review_status: ready
```


```yaml
candidate_card:
  card_type: column
  card_id: column.zs_observe.jiomart_oms.cgst_rate
  display_name: jiomart_oms.cgst_rate
  table_id: table.zs_observe.jiomart_oms
  schema: zs_observe
  table_name: jiomart_oms
  column_name: cgst_rate
  source_declared_type: decimal
  data_type: decimal
  column_group: 3.4 Tax Columns
  semantic_role: financial_amount_or_rate
  business_meaning: Legacy CGST columns
  evidence_refs:
  - ev.jiomart.oms.3_schema_details_115_columns
  confidence: high
  review_status: ready
```


```yaml
candidate_card:
  card_type: column
  card_id: column.zs_observe.jiomart_oms.cgst_amount
  display_name: jiomart_oms.cgst_amount
  table_id: table.zs_observe.jiomart_oms
  schema: zs_observe
  table_name: jiomart_oms
  column_name: cgst_amount
  source_declared_type: decimal
  data_type: decimal
  column_group: 3.4 Tax Columns
  semantic_role: financial_amount_or_rate
  business_meaning: Legacy CGST columns
  evidence_refs:
  - ev.jiomart.oms.3_schema_details_115_columns
  confidence: high
  review_status: ready
```


```yaml
candidate_card:
  card_type: column
  card_id: column.zs_observe.jiomart_oms.sgst_rate
  display_name: jiomart_oms.sgst_rate
  table_id: table.zs_observe.jiomart_oms
  schema: zs_observe
  table_name: jiomart_oms
  column_name: sgst_rate
  source_declared_type: decimal
  data_type: decimal
  column_group: 3.4 Tax Columns
  semantic_role: financial_amount_or_rate
  business_meaning: Legacy SGST columns
  evidence_refs:
  - ev.jiomart.oms.3_schema_details_115_columns
  confidence: high
  review_status: ready
```


```yaml
candidate_card:
  card_type: column
  card_id: column.zs_observe.jiomart_oms.sgst_amount
  display_name: jiomart_oms.sgst_amount
  table_id: table.zs_observe.jiomart_oms
  schema: zs_observe
  table_name: jiomart_oms
  column_name: sgst_amount
  source_declared_type: decimal
  data_type: decimal
  column_group: 3.4 Tax Columns
  semantic_role: financial_amount_or_rate
  business_meaning: Legacy SGST columns
  evidence_refs:
  - ev.jiomart.oms.3_schema_details_115_columns
  confidence: high
  review_status: ready
```


```yaml
candidate_card:
  card_type: column
  card_id: column.zs_observe.jiomart_oms.tcs_igst_rate
  display_name: jiomart_oms.tcs_igst_rate
  table_id: table.zs_observe.jiomart_oms
  schema: zs_observe
  table_name: jiomart_oms
  column_name: tcs_igst_rate
  source_declared_type: decimal
  data_type: decimal
  column_group: 3.5 TCS / TDS Columns
  semantic_role: financial_amount_or_rate
  business_meaning: TCS IGST rate (`0.0001`, `0.005`, `0.5`)
  evidence_refs:
  - ev.jiomart.oms.3_schema_details_115_columns
  confidence: high
  review_status: ready
```


```yaml
candidate_card:
  card_type: column
  card_id: column.zs_observe.jiomart_oms.tcs_cgst_rate
  display_name: jiomart_oms.tcs_cgst_rate
  table_id: table.zs_observe.jiomart_oms
  schema: zs_observe
  table_name: jiomart_oms
  column_name: tcs_cgst_rate
  source_declared_type: decimal
  data_type: decimal
  column_group: 3.5 TCS / TDS Columns
  semantic_role: financial_amount_or_rate
  business_meaning: TCS CGST rate (intra-state)
  evidence_refs:
  - ev.jiomart.oms.3_schema_details_115_columns
  confidence: high
  review_status: ready
```


```yaml
candidate_card:
  card_type: column
  card_id: column.zs_observe.jiomart_oms.tcs_sgst_rate
  display_name: jiomart_oms.tcs_sgst_rate
  table_id: table.zs_observe.jiomart_oms
  schema: zs_observe
  table_name: jiomart_oms
  column_name: tcs_sgst_rate
  source_declared_type: decimal
  data_type: decimal
  column_group: 3.5 TCS / TDS Columns
  semantic_role: financial_amount_or_rate
  business_meaning: TCS SGST rate
  evidence_refs:
  - ev.jiomart.oms.3_schema_details_115_columns
  confidence: high
  review_status: ready
```


```yaml
candidate_card:
  card_type: column
  card_id: column.zs_observe.jiomart_oms.total_tcs_amount
  display_name: jiomart_oms.total_tcs_amount
  table_id: table.zs_observe.jiomart_oms
  schema: zs_observe
  table_name: jiomart_oms
  column_name: total_tcs_amount
  source_declared_type: decimal
  data_type: decimal
  column_group: 3.5 TCS / TDS Columns
  semantic_role: financial_amount_or_rate
  business_meaning: '**Total TCS deducted** (GST § 52)'
  sign_or_context_semantics: Use transaction_type/order_status context; forward charged_amount is GMV and reverse rows represent
    returns/credit notes.
  evidence_refs:
  - ev.jiomart.oms.3_schema_details_115_columns
  confidence: high
  review_status: ready
```


```yaml
candidate_card:
  card_type: column
  card_id: column.zs_observe.jiomart_oms.tcs_igst_amount
  display_name: jiomart_oms.tcs_igst_amount
  table_id: table.zs_observe.jiomart_oms
  schema: zs_observe
  table_name: jiomart_oms
  column_name: tcs_igst_amount
  source_declared_type: decimal
  data_type: decimal
  column_group: 3.5 TCS / TDS Columns
  semantic_role: financial_amount_or_rate
  business_meaning: TCS IGST component
  evidence_refs:
  - ev.jiomart.oms.3_schema_details_115_columns
  confidence: high
  review_status: ready
```


```yaml
candidate_card:
  card_type: column
  card_id: column.zs_observe.jiomart_oms.tcs_cgst_amount
  display_name: jiomart_oms.tcs_cgst_amount
  table_id: table.zs_observe.jiomart_oms
  schema: zs_observe
  table_name: jiomart_oms
  column_name: tcs_cgst_amount
  source_declared_type: decimal
  data_type: decimal
  column_group: 3.5 TCS / TDS Columns
  semantic_role: financial_amount_or_rate
  business_meaning: TCS CGST component
  evidence_refs:
  - ev.jiomart.oms.3_schema_details_115_columns
  confidence: high
  review_status: ready
```


```yaml
candidate_card:
  card_type: column
  card_id: column.zs_observe.jiomart_oms.tcs_sgst_amount
  display_name: jiomart_oms.tcs_sgst_amount
  table_id: table.zs_observe.jiomart_oms
  schema: zs_observe
  table_name: jiomart_oms
  column_name: tcs_sgst_amount
  source_declared_type: decimal
  data_type: decimal
  column_group: 3.5 TCS / TDS Columns
  semantic_role: financial_amount_or_rate
  business_meaning: TCS SGST component
  evidence_refs:
  - ev.jiomart.oms.3_schema_details_115_columns
  confidence: high
  review_status: ready
```


```yaml
candidate_card:
  card_type: column
  card_id: column.zs_observe.jiomart_oms.total_tcs_deducted
  display_name: jiomart_oms.total_tcs_deducted
  table_id: table.zs_observe.jiomart_oms
  schema: zs_observe
  table_name: jiomart_oms
  column_name: total_tcs_deducted
  source_declared_type: decimal
  data_type: decimal
  column_group: 3.5 TCS / TDS Columns
  semantic_role: financial_amount_or_rate
  business_meaning: TCS deducted (alternate field)
  evidence_refs:
  - ev.jiomart.oms.3_schema_details_115_columns
  confidence: high
  review_status: ready
```


```yaml
candidate_card:
  card_type: column
  card_id: column.zs_observe.jiomart_oms.total_tds
  display_name: jiomart_oms.total_tds
  table_id: table.zs_observe.jiomart_oms
  schema: zs_observe
  table_name: jiomart_oms
  column_name: total_tds
  source_declared_type: decimal
  data_type: decimal
  column_group: 3.5 TCS / TDS Columns
  semantic_role: financial_amount_or_rate
  business_meaning: '**Total TDS** (Income Tax § 194-O)'
  sign_or_context_semantics: Use transaction_type/order_status context; forward charged_amount is GMV and reverse rows represent
    returns/credit notes.
  evidence_refs:
  - ev.jiomart.oms.3_schema_details_115_columns
  confidence: high
  review_status: ready
```


```yaml
candidate_card:
  card_type: column
  card_id: column.zs_observe.jiomart_oms.tds_194o_rate
  display_name: jiomart_oms.tds_194o_rate
  table_id: table.zs_observe.jiomart_oms
  schema: zs_observe
  table_name: jiomart_oms
  column_name: tds_194o_rate
  source_declared_type: decimal
  data_type: decimal
  column_group: 3.5 TCS / TDS Columns
  semantic_role: financial_amount_or_rate
  business_meaning: 'TDS rate: **0.1%**'
  evidence_refs:
  - ev.jiomart.oms.3_schema_details_115_columns
  confidence: high
  review_status: ready
```


```yaml
candidate_card:
  card_type: column
  card_id: column.zs_observe.jiomart_oms.tds_194o_amount
  display_name: jiomart_oms.tds_194o_amount
  table_id: table.zs_observe.jiomart_oms
  schema: zs_observe
  table_name: jiomart_oms
  column_name: tds_194o_amount
  source_declared_type: decimal
  data_type: decimal
  column_group: 3.5 TCS / TDS Columns
  semantic_role: financial_amount_or_rate
  business_meaning: TDS 194-O amount
  evidence_refs:
  - ev.jiomart.oms.3_schema_details_115_columns
  confidence: high
  review_status: ready
```


```yaml
candidate_card:
  card_type: column
  card_id: column.zs_observe.jiomart_oms.transaction_type
  display_name: jiomart_oms.transaction_type
  table_id: table.zs_observe.jiomart_oms
  schema: zs_observe
  table_name: jiomart_oms
  column_name: transaction_type
  source_declared_type: varchar
  data_type: varchar
  column_group: 3.6 Status Columns
  semantic_role: classification_status_or_type
  business_meaning: '`forward` (sale) or `reverse` (return credit note)'
  sign_or_context_semantics: Use transaction_type/order_status context; forward charged_amount is GMV and reverse rows represent
    returns/credit notes.
  evidence_refs:
  - ev.jiomart.oms.3_schema_details_115_columns
  confidence: high
  review_status: ready
```


```yaml
candidate_card:
  card_type: column
  card_id: column.zs_observe.jiomart_oms.order_status
  display_name: jiomart_oms.order_status
  table_id: table.zs_observe.jiomart_oms
  schema: zs_observe
  table_name: jiomart_oms
  column_name: order_status
  source_declared_type: varchar
  data_type: varchar
  column_group: 3.6 Status Columns
  semantic_role: marketplace_fulfillment_identifier
  business_meaning: '`delivered`, `complete`, `shipment_returned`, `pick_up_confirmed`, `invoiced`'
  sign_or_context_semantics: Use transaction_type/order_status context; forward charged_amount is GMV and reverse rows represent
    returns/credit notes.
  evidence_refs:
  - ev.jiomart.oms.3_schema_details_115_columns
  confidence: high
  review_status: ready
```


```yaml
candidate_card:
  card_type: column
  card_id: column.zs_observe.jiomart_oms.order_type
  display_name: jiomart_oms.order_type
  table_id: table.zs_observe.jiomart_oms
  schema: zs_observe
  table_name: jiomart_oms
  column_name: order_type
  source_declared_type: varchar
  data_type: varchar
  column_group: 3.6 Status Columns
  semantic_role: classification_status_or_type
  business_meaning: '`COD` or `Prepaid` (NULL for older rows)'
  evidence_refs:
  - ev.jiomart.oms.3_schema_details_115_columns
  confidence: high
  review_status: ready
```


```yaml
candidate_card:
  card_type: column
  card_id: column.zs_observe.jiomart_oms.event_type
  display_name: jiomart_oms.event_type
  table_id: table.zs_observe.jiomart_oms
  schema: zs_observe
  table_name: jiomart_oms
  column_name: event_type
  source_declared_type: varchar
  data_type: varchar
  column_group: 3.6 Status Columns
  semantic_role: classification_status_or_type
  business_meaning: Event classification
  evidence_refs:
  - ev.jiomart.oms.3_schema_details_115_columns
  confidence: high
  review_status: ready
```


```yaml
candidate_card:
  card_type: column
  card_id: column.zs_observe.jiomart_oms.event_sub_type
  display_name: jiomart_oms.event_sub_type
  table_id: table.zs_observe.jiomart_oms
  schema: zs_observe
  table_name: jiomart_oms
  column_name: event_sub_type
  source_declared_type: varchar
  data_type: varchar
  column_group: 3.6 Status Columns
  semantic_role: classification_status_or_type
  business_meaning: Event classification
  evidence_refs:
  - ev.jiomart.oms.3_schema_details_115_columns
  confidence: high
  review_status: ready
```


```yaml
candidate_card:
  card_type: column
  card_id: column.zs_observe.jiomart_oms.fulfilment_channel
  display_name: jiomart_oms.fulfilment_channel
  table_id: table.zs_observe.jiomart_oms
  schema: zs_observe
  table_name: jiomart_oms
  column_name: fulfilment_channel
  source_declared_type: varchar
  data_type: varchar
  column_group: 3.6 Status Columns
  semantic_role: marketplace_fulfillment_identifier
  business_meaning: '`Third Party Platform Shipment`'
  evidence_refs:
  - ev.jiomart.oms.3_schema_details_115_columns
  confidence: high
  review_status: ready
```


```yaml
candidate_card:
  card_type: column
  card_id: column.zs_observe.jiomart_oms.fulfillment_type
  display_name: jiomart_oms.fulfillment_type
  table_id: table.zs_observe.jiomart_oms
  schema: zs_observe
  table_name: jiomart_oms
  column_name: fulfillment_type
  source_declared_type: varchar
  data_type: varchar
  column_group: 3.6 Status Columns
  semantic_role: marketplace_fulfillment_identifier
  business_meaning: Same as above (newer rows)
  evidence_refs:
  - ev.jiomart.oms.3_schema_details_115_columns
  confidence: high
  review_status: ready
```


```yaml
candidate_card:
  card_type: column
  card_id: column.zs_observe.jiomart_oms.is_active
  display_name: jiomart_oms.is_active
  table_id: table.zs_observe.jiomart_oms
  schema: zs_observe
  table_name: jiomart_oms
  column_name: is_active
  source_declared_type: boolean
  data_type: boolean
  column_group: 3.6 Status Columns
  semantic_role: general_marketplace_attribute
  business_meaning: Always `true`
  evidence_refs:
  - ev.jiomart.oms.3_schema_details_115_columns
  confidence: high
  review_status: ready
```


```yaml
candidate_card:
  card_type: column
  card_id: column.zs_observe.jiomart_oms.is_duplicated
  display_name: jiomart_oms.is_duplicated
  table_id: table.zs_observe.jiomart_oms
  schema: zs_observe
  table_name: jiomart_oms
  column_name: is_duplicated
  source_declared_type: boolean
  data_type: boolean
  column_group: 3.6 Status Columns
  semantic_role: general_marketplace_attribute
  business_meaning: Dedup flag
  evidence_refs:
  - ev.jiomart.oms.3_schema_details_115_columns
  confidence: high
  review_status: ready
```


```yaml
candidate_card:
  card_type: column
  card_id: column.zs_observe.jiomart_oms.source_state
  display_name: jiomart_oms.source_state
  table_id: table.zs_observe.jiomart_oms
  schema: zs_observe
  table_name: jiomart_oms
  column_name: source_state
  source_declared_type: varchar
  data_type: varchar
  column_group: 3.7 Geographic Columns
  semantic_role: general_marketplace_attribute
  business_meaning: Seller dispatch state (`HARYANA`, `KARNATAKA`, `MAHARASHTRA`)
  evidence_refs:
  - ev.jiomart.oms.3_schema_details_115_columns
  confidence: high
  review_status: ready
```


```yaml
candidate_card:
  card_type: column
  card_id: column.zs_observe.jiomart_oms.source_state_code
  display_name: jiomart_oms.source_state_code
  table_id: table.zs_observe.jiomart_oms
  schema: zs_observe
  table_name: jiomart_oms
  column_name: source_state_code
  source_declared_type: varchar
  data_type: varchar
  column_group: 3.7 Geographic Columns
  semantic_role: general_marketplace_attribute
  business_meaning: State code
  evidence_refs:
  - ev.jiomart.oms.3_schema_details_115_columns
  confidence: high
  review_status: ready
```


```yaml
candidate_card:
  card_type: column
  card_id: column.zs_observe.jiomart_oms.destination_state
  display_name: jiomart_oms.destination_state
  table_id: table.zs_observe.jiomart_oms
  schema: zs_observe
  table_name: jiomart_oms
  column_name: destination_state
  source_declared_type: varchar
  data_type: varchar
  column_group: 3.7 Geographic Columns
  semantic_role: general_marketplace_attribute
  business_meaning: Buyer state (66 distinct)
  evidence_refs:
  - ev.jiomart.oms.3_schema_details_115_columns
  confidence: high
  review_status: ready
```


```yaml
candidate_card:
  card_type: column
  card_id: column.zs_observe.jiomart_oms.destination_state_code
  display_name: jiomart_oms.destination_state_code
  table_id: table.zs_observe.jiomart_oms
  schema: zs_observe
  table_name: jiomart_oms
  column_name: destination_state_code
  source_declared_type: varchar
  data_type: varchar
  column_group: 3.7 Geographic Columns
  semantic_role: general_marketplace_attribute
  business_meaning: Destination state code
  evidence_refs:
  - ev.jiomart.oms.3_schema_details_115_columns
  confidence: high
  review_status: ready
```


```yaml
candidate_card:
  card_type: column
  card_id: column.zs_observe.jiomart_oms.destination_zipcode
  display_name: jiomart_oms.destination_zipcode
  table_id: table.zs_observe.jiomart_oms
  schema: zs_observe
  table_name: jiomart_oms
  column_name: destination_zipcode
  source_declared_type: varchar
  data_type: varchar
  column_group: 3.7 Geographic Columns
  semantic_role: general_marketplace_attribute
  business_meaning: Buyer pincode
  evidence_refs:
  - ev.jiomart.oms.3_schema_details_115_columns
  confidence: high
  review_status: ready
```


```yaml
candidate_card:
  card_type: column
  card_id: column.zs_observe.jiomart_oms.order_billed_from
  display_name: jiomart_oms.order_billed_from
  table_id: table.zs_observe.jiomart_oms
  schema: zs_observe
  table_name: jiomart_oms
  column_name: order_billed_from
  source_declared_type: varchar
  data_type: varchar
  column_group: 3.7 Geographic Columns
  semantic_role: identity_or_join_key
  business_meaning: Billing / shipping state
  evidence_refs:
  - ev.jiomart.oms.3_schema_details_115_columns
  confidence: high
  review_status: ready
```


```yaml
candidate_card:
  card_type: column
  card_id: column.zs_observe.jiomart_oms.order_shipped_from
  display_name: jiomart_oms.order_shipped_from
  table_id: table.zs_observe.jiomart_oms
  schema: zs_observe
  table_name: jiomart_oms
  column_name: order_shipped_from
  source_declared_type: varchar
  data_type: varchar
  column_group: 3.7 Geographic Columns
  semantic_role: identity_or_join_key
  business_meaning: Billing / shipping state
  evidence_refs:
  - ev.jiomart.oms.3_schema_details_115_columns
  confidence: high
  review_status: ready
```


```yaml
candidate_card:
  card_type: column
  card_id: column.zs_observe.jiomart_oms.customer_s_billing_state
  display_name: jiomart_oms.customer_s_billing_state
  table_id: table.zs_observe.jiomart_oms
  schema: zs_observe
  table_name: jiomart_oms
  column_name: customer_s_billing_state
  source_declared_type: varchar
  data_type: varchar
  column_group: 3.7 Geographic Columns
  semantic_role: general_marketplace_attribute
  business_meaning: Customer billing state
  evidence_refs:
  - ev.jiomart.oms.3_schema_details_115_columns
  confidence: high
  review_status: ready
```


```yaml
candidate_card:
  card_type: column
  card_id: column.zs_observe.jiomart_oms.customer_s_delivery_state
  display_name: jiomart_oms.customer_s_delivery_state
  table_id: table.zs_observe.jiomart_oms
  schema: zs_observe
  table_name: jiomart_oms
  column_name: customer_s_delivery_state
  source_declared_type: varchar
  data_type: varchar
  column_group: 3.7 Geographic Columns
  semantic_role: general_marketplace_attribute
  business_meaning: Customer delivery state
  evidence_refs:
  - ev.jiomart.oms.3_schema_details_115_columns
  confidence: high
  review_status: ready
```


```yaml
candidate_card:
  card_type: column
  card_id: column.zs_observe.jiomart_oms.description
  display_name: jiomart_oms.description
  table_id: table.zs_observe.jiomart_oms
  schema: zs_observe
  table_name: jiomart_oms
  column_name: description
  source_declared_type: varchar
  data_type: varchar
  column_group: 3.8 Product / Fulfilment Columns
  semantic_role: product_catalog
  business_meaning: Product description
  evidence_refs:
  - ev.jiomart.oms.3_schema_details_115_columns
  confidence: high
  review_status: ready
```


```yaml
candidate_card:
  card_type: column
  card_id: column.zs_observe.jiomart_oms.product_title_description
  display_name: jiomart_oms.product_title_description
  table_id: table.zs_observe.jiomart_oms
  schema: zs_observe
  table_name: jiomart_oms
  column_name: product_title_description
  source_declared_type: varchar
  data_type: varchar
  column_group: 3.8 Product / Fulfilment Columns
  semantic_role: product_catalog
  business_meaning: Full product title
  evidence_refs:
  - ev.jiomart.oms.3_schema_details_115_columns
  confidence: high
  review_status: ready
```


```yaml
candidate_card:
  card_type: column
  card_id: column.zs_observe.jiomart_oms.quantity
  display_name: jiomart_oms.quantity
  table_id: table.zs_observe.jiomart_oms
  schema: zs_observe
  table_name: jiomart_oms
  column_name: quantity
  source_declared_type: decimal
  data_type: decimal
  column_group: 3.8 Product / Fulfilment Columns
  semantic_role: general_marketplace_attribute
  business_meaning: Quantity ordered
  evidence_refs:
  - ev.jiomart.oms.3_schema_details_115_columns
  confidence: high
  review_status: ready
```


```yaml
candidate_card:
  card_type: column
  card_id: column.zs_observe.jiomart_oms.item_quantity
  display_name: jiomart_oms.item_quantity
  table_id: table.zs_observe.jiomart_oms
  schema: zs_observe
  table_name: jiomart_oms
  column_name: item_quantity
  source_declared_type: decimal
  data_type: decimal
  column_group: 3.8 Product / Fulfilment Columns
  semantic_role: general_marketplace_attribute
  business_meaning: Quantity ordered
  evidence_refs:
  - ev.jiomart.oms.3_schema_details_115_columns
  confidence: high
  review_status: ready
```


```yaml
candidate_card:
  card_type: column
  card_id: column.zs_observe.jiomart_oms.fulfiller_name
  display_name: jiomart_oms.fulfiller_name
  table_id: table.zs_observe.jiomart_oms
  schema: zs_observe
  table_name: jiomart_oms
  column_name: fulfiller_name
  source_declared_type: varchar
  data_type: varchar
  column_group: 3.8 Product / Fulfilment Columns
  semantic_role: scope_column_preserved_not_card_boundary
  business_meaning: Fulfilment centre name
  scope_note: Scope-like field retained as a source column/filter/value only; do not create tenant/group/account cards.
  evidence_refs:
  - ev.jiomart.oms.3_schema_details_115_columns
  confidence: high
  review_status: ready
```


```yaml
candidate_card:
  card_type: column
  card_id: column.zs_observe.jiomart_oms.group_level_id
  display_name: jiomart_oms.group_level_id
  table_id: table.zs_observe.jiomart_oms
  schema: zs_observe
  table_name: jiomart_oms
  column_name: group_level_id
  source_declared_type: integer
  data_type: integer
  column_group: 3.9 System / Metadata
  semantic_role: scope_column_preserved_not_card_boundary
  business_meaning: '`26` — JioMart / MYFITNESS account'
  scope_note: Scope-like field retained as a source column/filter/value only; do not create tenant/group/account cards.
  evidence_refs:
  - ev.jiomart.oms.3_schema_details_115_columns
  confidence: high
  review_status: ready
```


```yaml
candidate_card:
  card_type: column
  card_id: column.zs_observe.jiomart_oms.brand
  display_name: jiomart_oms.brand
  table_id: table.zs_observe.jiomart_oms
  schema: zs_observe
  table_name: jiomart_oms
  column_name: brand
  source_declared_type: varchar
  data_type: varchar
  column_group: 3.9 System / Metadata
  semantic_role: product_catalog
  business_meaning: '`MYFITNESS` — always populated'
  evidence_refs:
  - ev.jiomart.oms.3_schema_details_115_columns
  confidence: high
  review_status: ready
```


```yaml
candidate_card:
  card_type: column
  card_id: column.zs_observe.jiomart_oms.brand_ref_1
  display_name: jiomart_oms.brand_ref_1
  table_id: table.zs_observe.jiomart_oms
  schema: zs_observe
  table_name: jiomart_oms
  column_name: brand_ref_1
  source_declared_type: varchar
  data_type: varchar
  column_group: 3.9 System / Metadata
  semantic_role: product_catalog
  business_meaning: Brand reference slugs
  evidence_refs:
  - ev.jiomart.oms.3_schema_details_115_columns
  confidence: high
  review_status: ready
```


```yaml
candidate_card:
  card_type: column
  card_id: column.zs_observe.jiomart_oms.brand_ref_2
  display_name: jiomart_oms.brand_ref_2
  table_id: table.zs_observe.jiomart_oms
  schema: zs_observe
  table_name: jiomart_oms
  column_name: brand_ref_2
  source_declared_type: varchar
  data_type: varchar
  column_group: 3.9 System / Metadata
  semantic_role: product_catalog
  business_meaning: Brand reference slugs
  evidence_refs:
  - ev.jiomart.oms.3_schema_details_115_columns
  confidence: high
  review_status: ready
```


```yaml
candidate_card:
  card_type: column
  card_id: column.zs_observe.jiomart_oms.seller_coupon_code
  display_name: jiomart_oms.seller_coupon_code
  table_id: table.zs_observe.jiomart_oms
  schema: zs_observe
  table_name: jiomart_oms
  column_name: seller_coupon_code
  source_declared_type: varchar
  data_type: varchar
  column_group: 3.9 System / Metadata
  semantic_role: general_marketplace_attribute
  business_meaning: Coupon code applied
  evidence_refs:
  - ev.jiomart.oms.3_schema_details_115_columns
  confidence: high
  review_status: ready
```


```yaml
candidate_card:
  card_type: column
  card_id: column.zs_observe.jiomart_oms.currency_type
  display_name: jiomart_oms.currency_type
  table_id: table.zs_observe.jiomart_oms
  schema: zs_observe
  table_name: jiomart_oms
  column_name: currency_type
  source_declared_type: varchar
  data_type: varchar
  column_group: 3.9 System / Metadata
  semantic_role: classification_status_or_type
  business_meaning: '`INR`'
  evidence_refs:
  - ev.jiomart.oms.3_schema_details_115_columns
  confidence: high
  review_status: ready
```


```yaml
candidate_card:
  card_type: column
  card_id: column.zs_observe.jiomart_oms.zen_sheet_name
  display_name: jiomart_oms.zen_sheet_name
  table_id: table.zs_observe.jiomart_oms
  schema: zs_observe
  table_name: jiomart_oms
  column_name: zen_sheet_name
  source_declared_type: varchar
  data_type: varchar
  column_group: 3.9 System / Metadata
  semantic_role: general_marketplace_attribute
  business_meaning: Source sheet
  evidence_refs:
  - ev.jiomart.oms.3_schema_details_115_columns
  confidence: high
  review_status: ready
```


```yaml
candidate_card:
  card_type: column
  card_id: column.zs_observe.jiomart_oms.temp_old_columns
  display_name: jiomart_oms.temp_old_columns
  table_id: table.zs_observe.jiomart_oms
  schema: zs_observe
  table_name: jiomart_oms
  column_name: temp_old_columns
  source_declared_type: various
  data_type: various
  column_group: 3.9 System / Metadata
  semantic_role: general_marketplace_attribute
  business_meaning: Legacy migration columns
  evidence_refs:
  - ev.jiomart.oms.3_schema_details_115_columns
  confidence: high
  review_status: ready
```

### 4.6 `relationship` cards


```yaml
candidate_card:
  card_type: relationship
  card_id: relationship.jiomart.oms_settlement.order_id
  display_name: JioMart OMS ↔ Settlement on order_id
  source_table_id: table.zs_observe.jiomart_oms
  target_table_id: table.zs_observe.jiomart_settlement
  relationship_type: marketplace_internal_join
  join_keys:
  - source_column: order_id
    target_column: order_id
  coverage: 56,733 / 57,677 = 98.4% documented coverage
  preaggregation_required: true
  grain_warning: jiomart_settlement is event-based multi-row; aggregate by order_id before comparing Receivable/BaseTcs/Tds
    to OMS values.
  evidence_refs:
  - ev.jiomart.marketplace.4_2_primary_join_keys
  - ev.jiomart.settlement.4_settlement_structure_event_based_multi_row_model
  confidence: high
  review_status: ready
```


```yaml
candidate_card:
  card_type: relationship
  card_id: relationship.jiomart.oms_returns.order_id
  display_name: JioMart OMS ↔ Returns on order_id
  source_table_id: table.zs_observe.jiomart_oms
  target_table_id: table.zs_observe.jiomart_returns
  relationship_type: marketplace_internal_join
  join_keys:
  - source_column: order_id
    target_column: order_id
  coverage: 8,018 / 8,367 = 95.8% documented coverage
  preaggregation_required: false
  grain_warning: Returns table provides richer return-journey detail; join by order_id for order-level return analysis.
  evidence_refs:
  - ev.jiomart.marketplace.4_2_primary_join_keys
  - ev.jiomart.returns.1_table_overview
  confidence: high
  review_status: ready
```


```yaml
candidate_card:
  card_type: relationship
  card_id: relationship.jiomart.settlement_returns.order_id
  display_name: JioMart Settlement ↔ Returns on order_id
  source_table_id: table.zs_observe.jiomart_settlement
  target_table_id: table.zs_observe.jiomart_returns
  relationship_type: marketplace_internal_join
  join_keys:
  - source_column: order_id
    target_column: order_id
  coverage: Coverage not numerically documented; key is documented in source join table.
  preaggregation_required: true
  grain_warning: Use order_id only; return rows may lack item_id in settlement.
  evidence_refs:
  - ev.jiomart.marketplace.4_2_primary_join_keys
  - ev.jiomart.settlement.7_data_quality_observations
  confidence: medium
  review_status: candidate
```

### 4.7 `value_profile` cards


```yaml
candidate_card:
  card_type: value_profile
  card_id: value_profile.jiomart.scope.group_level_id_26
  display_name: JioMart group_level_id 26 MYFITNESS/TANVI Fitness scope value
  profile_kind: observed_value_profile
  column_id: column.zs_observe.jiomart_oms.group_level_id
  observed_values:
  - '26'
  distribution_summary: Applies to jiomart_oms, jiomart_returns, jiomart_settlement for TANVI Fitness / MYFITNESS.
  normalization_rule: Preserve source spelling/case and code values; normalize only downstream where explicitly configured.
  evidence_refs:
  - ev.jiomart.marketplace.1_3_seller_entities_in_dataset
  confidence: high
  review_status: ready
```


```yaml
candidate_card:
  card_type: value_profile
  card_id: value_profile.jiomart.scope.group_level_id_221
  display_name: JioMart group_level_id 221 ARDEUR shipment scope value
  profile_kind: observed_value_profile
  column_id: column.zs_observe.jiomart_shipment.group_level_id
  observed_values:
  - '221'
  distribution_summary: Applies only to jiomart_shipment for ARDEUR FASHIONS; no join to MYFITNESS tables.
  normalization_rule: Preserve source spelling/case and code values; normalize only downstream where explicitly configured.
  evidence_refs:
  - ev.jiomart.marketplace.1_3_seller_entities_in_dataset
  - ev.jiomart.shipment.1_table_overview
  confidence: high
  review_status: ready
```


```yaml
candidate_card:
  card_type: value_profile
  card_id: value_profile.jiomart.products.myfitness_hsn
  display_name: MYFITNESS products and HSN/GST profiles
  profile_kind: product_hsn_profile
  table_id: table.zs_observe.jiomart_oms
  observed_values:
  - C5102_1
  - C22703
  - C12502_1
  - N5101
  - O12502_1
  - '20081100'
  - '11041200'
  - '18069030'
  - '21069099'
  distribution_summary: MYFITNESS peanut butter/oats/combo products with 5%, 12%, and 18% GST HSN context.
  normalization_rule: Preserve source spelling/case and code values; normalize only downstream where explicitly configured.
  evidence_refs:
  - ev.jiomart.marketplace.1_4_myfitness_products_primary_seller_group_26
  confidence: high
  review_status: ready
```


```yaml
candidate_card:
  card_type: value_profile
  card_id: value_profile.jiomart.gstin.tanvi_multistate
  display_name: TANVI Fitness multi-state GSTIN registration profile
  profile_kind: gstin_state_profile
  table_id: table.zs_observe.jiomart_oms
  observed_values:
  - 29AAHCT1518N1ZW
  - 27AAHCT1518N1Z0
  - 06AAHCT1518N1Z4
  distribution_summary: Karnataka, Maharashtra, and Haryana source GSTIN/warehouse mapping.
  normalization_rule: Preserve source spelling/case and code values; normalize only downstream where explicitly configured.
  evidence_refs:
  - ev.jiomart.marketplace.1_5_multi_state_gstin_registration_tanvi_fitness
  confidence: high
  review_status: ready
```


```yaml
candidate_card:
  card_type: value_profile
  card_id: value_profile.jiomart.shipment.order_status
  display_name: Shipment order_status profile
  profile_kind: observed_value_profile
  column_id: column.zs_observe.jiomart_shipment.order_status
  observed_values:
  - delivered
  - shipment_returned
  - canceled
  normalization_rule: Preserve source spelling/case and code values; normalize only downstream where explicitly configured.
  evidence_refs:
  - ev.jiomart.shipment.order_status_distribution
  confidence: high
  review_status: ready
```


```yaml
candidate_card:
  card_type: value_profile
  card_id: value_profile.jiomart.shipment.sku_prefixes
  display_name: ARDEUR/CODEZ shipment SKU naming profile
  profile_kind: observed_value_profile
  column_id: column.zs_observe.jiomart_shipment.sku_id
  observed_values:
  - ASSJ18-
  - AMSH-
  - CBOT-
  - CBHO-
  - CBSW-
  - CBHN-
  - AMJG-
  distribution_summary: ARDEUR Mens and CODEZ Boys SKU prefix conventions.
  normalization_rule: Preserve source spelling/case and code values; normalize only downstream where explicitly configured.
  evidence_refs:
  - ev.jiomart.shipment.sku_naming_convention_ardeur_fashions
  confidence: high
  review_status: ready
```


```yaml
candidate_card:
  card_type: value_profile
  card_id: value_profile.jiomart.shipment.payment_mode
  display_name: Shipment payment_mode profile
  profile_kind: observed_value_profile
  column_id: column.zs_observe.jiomart_shipment.payment_mode
  observed_values:
  - COD
  - Prepaid_Payments
  normalization_rule: Preserve source spelling/case and code values; normalize only downstream where explicitly configured.
  evidence_refs:
  - ev.jiomart.shipment.2_key_statistics
  confidence: high
  review_status: ready
```


```yaml
candidate_card:
  card_type: value_profile
  card_id: value_profile.jiomart.shipment.fulfillment_channel
  display_name: Direct Shipment fulfillment-channel profile
  profile_kind: observed_value_profile
  column_id: column.zs_observe.jiomart_shipment.fulfillment_channel
  observed_values:
  - Direct Shipment
  normalization_rule: Preserve source spelling/case and code values; normalize only downstream where explicitly configured.
  evidence_refs:
  - ev.jiomart.shipment.1_table_overview
  confidence: high
  review_status: ready
```


```yaml
candidate_card:
  card_type: value_profile
  card_id: value_profile.jiomart.shipment.promo_discount_scale
  display_name: Shipment promotional discount scale profile
  profile_kind: numeric_distribution_guidance
  column_id: column.zs_observe.jiomart_shipment.item_promo_discount
  distribution_summary: MRP 999-1999 and charged_amount 149-299; typical 70-87% discounts.
  normalization_rule: Preserve source spelling/case and code values; normalize only downstream where explicitly configured.
  evidence_refs:
  - ev.jiomart.shipment.promotional_discount_scale
  confidence: high
  review_status: ready
```


```yaml
candidate_card:
  card_type: value_profile
  card_id: value_profile.jiomart.settlement.transaction_type
  display_name: Settlement transaction_type profile
  profile_kind: observed_value_profile
  column_id: column.zs_observe.jiomart_settlement.transaction_type
  observed_values:
  - forward
  - reverse
  - Credit Note
  - Debit Note
  - Service Invoice
  - Bill Tds Refund
  normalization_rule: Preserve source spelling/case and code values; normalize only downstream where explicitly configured.
  evidence_refs:
  - ev.jiomart.settlement.3_schema_details_40_columns
  confidence: high
  review_status: ready
```


```yaml
candidate_card:
  card_type: value_profile
  card_id: value_profile.jiomart.settlement.event
  display_name: Settlement event profile
  profile_kind: observed_value_profile
  column_id: column.zs_observe.jiomart_settlement.event
  observed_values:
  - Invoice
  - Return
  - Credit Note
  - Debit Note
  - Service Invoice
  - null
  normalization_rule: Preserve source spelling/case and code values; normalize only downstream where explicitly configured.
  evidence_refs:
  - ev.jiomart.settlement.4_settlement_structure_event_based_multi_row_model
  confidence: high
  review_status: ready
```


```yaml
candidate_card:
  card_type: value_profile
  card_id: value_profile.jiomart.settlement.accountable_type
  display_name: Settlement accountable_type profile
  profile_kind: observed_value_profile
  column_id: column.zs_observe.jiomart_settlement.accountable_type
  observed_values:
  - Receivable
  - BaseTcs
  - Tds
  - CreditDebitNote
  - Bill
  normalization_rule: Preserve source spelling/case and code values; normalize only downstream where explicitly configured.
  evidence_refs:
  - ev.jiomart.settlement.4_settlement_structure_event_based_multi_row_model
  confidence: high
  review_status: ready
```


```yaml
candidate_card:
  card_type: value_profile
  card_id: value_profile.jiomart.settlement.event_accountable_matrix
  display_name: Settlement event/accountable-type matrix profile
  profile_kind: event_amount_matrix
  table_id: table.zs_observe.jiomart_settlement
  distribution_summary: Invoice-forward Receivable/BaseTcs/Tds and Return-reverse Receivable/BaseTcs/Tds rows; Credit/Debit
    Note and Service Invoice rows; NULL older-format rows.
  normalization_rule: Preserve source spelling/case and code values; normalize only downstream where explicitly configured.
  evidence_refs:
  - ev.jiomart.settlement.full_event_accountabletype_matrix
  confidence: high
  review_status: ready
```


```yaml
candidate_card:
  card_type: value_profile
  card_id: value_profile.jiomart.settlement.account_book
  display_name: Settlement account_book profile
  profile_kind: observed_value_profile
  column_id: column.zs_observe.jiomart_settlement.account_book
  observed_values:
  - Seller payable
  normalization_rule: Preserve source spelling/case and code values; normalize only downstream where explicitly configured.
  evidence_refs:
  - ev.jiomart.settlement.2_key_statistics
  confidence: high
  review_status: ready
```


```yaml
candidate_card:
  card_type: value_profile
  card_id: value_profile.jiomart.returns.return_type
  display_name: Returns return_type / transaction_type profile
  profile_kind: observed_value_profile
  column_id: column.zs_observe.jiomart_returns.return_type
  observed_values:
  - ReturnToOrigin
  - DoorStepReturn
  - BeforeShippingReturn
  normalization_rule: Preserve source spelling/case and code values; normalize only downstream where explicitly configured.
  evidence_refs:
  - ev.jiomart.returns.return_type_meanings
  confidence: high
  review_status: ready
```


```yaml
candidate_card:
  card_type: value_profile
  card_id: value_profile.jiomart.returns.return_status
  display_name: Returns status profile
  profile_kind: observed_value_profile
  column_id: column.zs_observe.jiomart_returns.return_status
  observed_values:
  - complete
  - init
  normalization_rule: Preserve source spelling/case and code values; normalize only downstream where explicitly configured.
  evidence_refs:
  - ev.jiomart.returns.3_schema_details_53_columns
  confidence: high
  review_status: ready
```


```yaml
candidate_card:
  card_type: value_profile
  card_id: value_profile.jiomart.returns.payment_mode
  display_name: Returns payment mode profile
  profile_kind: observed_value_profile
  column_id: column.zs_observe.jiomart_returns.payment_mode
  observed_values:
  - COD
  - Prepaid_Payments
  normalization_rule: Preserve source spelling/case and code values; normalize only downstream where explicitly configured.
  evidence_refs:
  - ev.jiomart.returns.payment_mode
  confidence: high
  review_status: ready
```


```yaml
candidate_card:
  card_type: value_profile
  card_id: value_profile.jiomart.returns.couriers
  display_name: Return courier profile
  profile_kind: observed_value_profile
  column_id: column.zs_observe.jiomart_returns.courier_partner
  observed_values:
  - Delhivery
  - Shadowfax
  - Xpressbees Express
  normalization_rule: Preserve source spelling/case and code values; normalize only downstream where explicitly configured.
  evidence_refs:
  - ev.jiomart.returns.couriers
  confidence: high
  review_status: ready
```


```yaml
candidate_card:
  card_type: value_profile
  card_id: value_profile.jiomart.returns.fulfillment_centers
  display_name: Returns fulfillment center profile
  profile_kind: observed_warehouse_profile
  column_id: column.zs_observe.jiomart_returns.fulfillment_center
  distribution_summary: Central BLR Warehouse 560083 and other fulfilment-centre names are marketplace return context only.
  normalization_rule: Preserve source spelling/case and code values; normalize only downstream where explicitly configured.
  evidence_refs:
  - ev.jiomart.returns.fulfilment_centres
  confidence: high
  review_status: ready
```


```yaml
candidate_card:
  card_type: value_profile
  card_id: value_profile.jiomart.oms.transaction_type
  display_name: OMS transaction_type profile
  profile_kind: observed_value_profile
  column_id: column.zs_observe.jiomart_oms.transaction_type
  observed_values:
  - forward
  - reverse
  normalization_rule: Preserve source spelling/case and code values; normalize only downstream where explicitly configured.
  evidence_refs:
  - ev.jiomart.oms.transaction_type_order_status_financial_breakdown
  confidence: high
  review_status: ready
```


```yaml
candidate_card:
  card_type: value_profile
  card_id: value_profile.jiomart.oms.order_status
  display_name: OMS order_status profile
  profile_kind: observed_value_profile
  column_id: column.zs_observe.jiomart_oms.order_status
  observed_values:
  - delivered
  - complete
  - shipment_returned
  - pick_up_confirmed
  - invoiced
  normalization_rule: Preserve source spelling/case and code values; normalize only downstream where explicitly configured.
  evidence_refs:
  - ev.jiomart.oms.transaction_type_order_status_financial_breakdown
  confidence: high
  review_status: ready
```


```yaml
candidate_card:
  card_type: value_profile
  card_id: value_profile.jiomart.oms.order_type
  display_name: OMS order_type profile
  profile_kind: observed_value_profile
  column_id: column.zs_observe.jiomart_oms.order_type
  observed_values:
  - COD
  - Prepaid
  normalization_rule: Preserve source spelling/case and code values; normalize only downstream where explicitly configured.
  evidence_refs:
  - ev.jiomart.oms.3_6_status_columns
  confidence: high
  review_status: ready
```


```yaml
candidate_card:
  card_type: value_profile
  card_id: value_profile.jiomart.oms.fulfilment_channel
  display_name: OMS fulfilment channel profile
  profile_kind: observed_value_profile
  column_id: column.zs_observe.jiomart_oms.fulfilment_channel
  observed_values:
  - Third Party Platform Shipment
  normalization_rule: Preserve source spelling/case and code values; normalize only downstream where explicitly configured.
  evidence_refs:
  - ev.jiomart.marketplace.2_2_fulfilment_models
  - ev.jiomart.oms.3_6_status_columns
  confidence: high
  review_status: ready
```


```yaml
candidate_card:
  card_type: value_profile
  card_id: value_profile.jiomart.oms.source_state
  display_name: OMS source_state profile
  profile_kind: observed_value_profile
  column_id: column.zs_observe.jiomart_oms.source_state
  observed_values:
  - HARYANA
  - KARNATAKA
  - MAHARASHTRA
  normalization_rule: Preserve source spelling/case and code values; normalize only downstream where explicitly configured.
  evidence_refs:
  - ev.jiomart.oms.seller_gstins_warehouse_mapping
  confidence: high
  review_status: ready
```


```yaml
candidate_card:
  card_type: value_profile
  card_id: value_profile.jiomart.oms.hsn_products
  display_name: OMS HSN/product profile
  profile_kind: observed_value_profile
  column_id: column.zs_observe.jiomart_oms.hsn
  observed_values:
  - '20081100'
  - '11041200'
  - '18069030'
  - '21069099'
  normalization_rule: Preserve source spelling/case and code values; normalize only downstream where explicitly configured.
  evidence_refs:
  - ev.jiomart.oms.hsn_codes_and_products
  confidence: high
  review_status: ready
```


```yaml
candidate_card:
  card_type: value_profile
  card_id: value_profile.jiomart.oms.top_skus
  display_name: OMS top SKU profile
  profile_kind: distinct_value_analysis
  column_id: column.zs_observe.jiomart_oms.sku_id
  distribution_summary: Top SKU volume examples include C5102_1 and other MYFITNESS SKU ids; use sku_id plus mp_sin for combined
    key when sku alternate is NULL.
  normalization_rule: Preserve source spelling/case and code values; normalize only downstream where explicitly configured.
  evidence_refs:
  - ev.jiomart.oms.top_skus_by_volume
  confidence: high
  review_status: ready
```


```yaml
candidate_card:
  card_type: value_profile
  card_id: value_profile.jiomart.oms.coupon_codes
  display_name: OMS seller coupon code profile
  profile_kind: observed_coupon_profile
  column_id: column.zs_observe.jiomart_oms.seller_coupon_code
  distribution_summary: Seller coupon codes observed in OMS; seller_coupon_amount is negative deduction.
  normalization_rule: Preserve source spelling/case and code values; normalize only downstream where explicitly configured.
  evidence_refs:
  - ev.jiomart.oms.seller_coupon_codes_observed
  confidence: high
  review_status: ready
```


```yaml
candidate_card:
  card_type: value_profile
  card_id: value_profile.jiomart.oms.tcs_rates
  display_name: OMS TCS rate anomaly profile
  profile_kind: observed_value_profile
  column_id: column.zs_observe.jiomart_oms.tcs_igst_rate
  observed_values:
  - '0.0001'
  - '0.005'
  - '0.5'
  distribution_summary: 0.5 is documented as likely data error; flag tcs_igst_rate > 0.05.
  normalization_rule: Preserve source spelling/case and code values; normalize only downstream where explicitly configured.
  evidence_refs:
  - ev.jiomart.oms.tcs_rates_observed
  confidence: high
  review_status: ready
```


```yaml
candidate_card:
  card_type: value_profile
  card_id: value_profile.jiomart.currency.inr
  display_name: JioMart currency profile
  profile_kind: currency_profile
  observed_values:
  - INR
  distribution_summary: Currency type INR is documented across source tables.
  normalization_rule: Preserve source spelling/case and code values; normalize only downstream where explicitly configured.
  evidence_refs:
  - ev.jiomart.marketplace.10_table_summary_reference
  confidence: high
  review_status: ready
```

### 4.8 `metric` cards


```yaml
candidate_card:
  card_type: metric
  card_id: metric.jiomart.total_gmv
  display_name: Total GMV
  metric_family: revenue
  domain_id: domain.jiomart.orders
  default_unit: INR
  default_grain: as specified by source SQL or query pattern
  business_definition: Total forward GMV, reversed GMV, and net GMV from jiomart_oms.
  colloquial_names: []
  evidence_refs:
  - ev.jiomart.marketplace.6_1_total_gmv
  confidence: high
  review_status: ready
```


```yaml
candidate_card:
  card_type: metric
  card_id: metric.jiomart.return_rate
  display_name: Return Rate
  metric_family: returns
  domain_id: domain.jiomart.returns
  default_unit: INR
  default_grain: as specified by source SQL or query pattern
  business_definition: RTO rate and return reversal percentage from jiomart_oms.
  colloquial_names: []
  evidence_refs:
  - ev.jiomart.marketplace.6_2_return_rate
  confidence: high
  review_status: ready
```


```yaml
candidate_card:
  card_type: metric
  card_id: metric.jiomart.average_order_value
  display_name: Average Order Value
  metric_family: revenue
  domain_id: domain.jiomart.orders
  default_unit: INR
  default_grain: as specified by source SQL or query pattern
  business_definition: Average charged_amount for delivered forward OMS rows.
  colloquial_names: []
  evidence_refs:
  - ev.jiomart.marketplace.6_3_average_order_value_aov
  confidence: high
  review_status: ready
```


```yaml
candidate_card:
  card_type: metric
  card_id: metric.jiomart.net_settled_revenue
  display_name: Net Settled Revenue
  metric_family: settlement
  domain_id: domain.jiomart.settlement
  default_unit: INR
  default_grain: as specified by source SQL or query pattern
  business_definition: Net settlement impact by Receivable/BaseTcs/Tds and total settled_amount.
  colloquial_names: []
  evidence_refs:
  - ev.jiomart.marketplace.6_4_net_settled_revenue
  confidence: high
  review_status: ready
```


```yaml
candidate_card:
  card_type: metric
  card_id: metric.jiomart.seller_coupon_discount_impact
  display_name: Seller Coupon Discount Impact
  metric_family: promotions
  domain_id: domain.jiomart.promotions
  default_unit: INR
  default_grain: as specified by source SQL or query pattern
  business_definition: Coupon-code level seller-funded discount impact from OMS.
  colloquial_names: []
  evidence_refs:
  - ev.jiomart.marketplace.6_5_seller_coupon_discount_impact
  confidence: high
  review_status: ready
```


```yaml
candidate_card:
  card_type: metric
  card_id: metric.jiomart.monthly_forward_orders_gmv
  display_name: Monthly Forward Orders and GMV
  metric_family: revenue
  domain_id: domain.jiomart.orders
  default_unit: INR
  default_grain: as specified by source SQL or query pattern
  business_definition: Month-level forward order count, GMV, and AOV from OMS.
  colloquial_names: []
  evidence_refs:
  - ev.jiomart.marketplace.6_6_monthly_forward_orders_and_gmv
  confidence: high
  review_status: ready
```


```yaml
candidate_card:
  card_type: metric
  card_id: metric.jiomart.shipment_status_gmv
  display_name: Shipment Status Summary
  metric_family: revenue
  domain_id: domain.jiomart.orders
  default_unit: INR
  default_grain: as specified by source SQL or query pattern
  business_definition: Shipment order_status counts, GMV, MRP, discount, and average selling price for ARDEUR shipments.
  colloquial_names: []
  evidence_refs:
  - ev.jiomart.shipment.7_1_shipment_status_summary
  confidence: high
  review_status: ready
```


```yaml
candidate_card:
  card_type: metric
  card_id: metric.jiomart.shipment_monthly_gmv
  display_name: Shipment Monthly GMV
  metric_family: revenue
  domain_id: domain.jiomart.orders
  default_unit: INR
  default_grain: as specified by source SQL or query pattern
  business_definition: Month-level shipment count, GMV, and promo discount for jiomart_shipment.
  colloquial_names: []
  evidence_refs:
  - ev.jiomart.shipment.7_2_monthly_gmv
  confidence: high
  review_status: ready
```


```yaml
candidate_card:
  card_type: metric
  card_id: metric.jiomart.top_shipment_skus
  display_name: Top Shipment SKUs
  metric_family: product
  domain_id: domain.jiomart.product
  default_unit: INR
  default_grain: as specified by source SQL or query pattern
  business_definition: Top SKU-level orders, GMV, average price, and discount for jiomart_shipment.
  colloquial_names: []
  evidence_refs:
  - ev.jiomart.shipment.7_3_top_skus
  confidence: high
  review_status: ready
```


```yaml
candidate_card:
  card_type: metric
  card_id: metric.jiomart.net_settlement_per_order
  display_name: Net Settlement per Order
  metric_family: settlement
  domain_id: domain.jiomart.settlement
  default_unit: INR
  default_grain: as specified by source SQL or query pattern
  business_definition: Order-level sale proceeds, TCS, TDS, and net settled amount from structured settlement rows.
  colloquial_names: []
  evidence_refs:
  - ev.jiomart.settlement.8_1_net_settlement_per_order_structured_rows
  confidence: high
  review_status: ready
```


```yaml
candidate_card:
  card_type: metric
  card_id: metric.jiomart.monthly_settlement_summary
  display_name: Monthly Settlement Summary
  metric_family: settlement
  domain_id: domain.jiomart.settlement
  default_unit: INR
  default_grain: as specified by source SQL or query pattern
  business_definition: Monthly settlement rows and settled_amount by transaction_type/accountable_type.
  colloquial_names: []
  evidence_refs:
  - ev.jiomart.settlement.8_2_monthly_settlement_summary
  confidence: high
  review_status: ready
```


```yaml
candidate_card:
  card_type: metric
  card_id: metric.jiomart.credit_debit_note_impact
  display_name: Credit / Debit Note Impact
  metric_family: settlement
  domain_id: domain.jiomart.settlement
  default_unit: INR
  default_grain: as specified by source SQL or query pattern
  business_definition: Credit Note, Debit Note, Service Invoice, and Bill Tds Refund counts and total settled amounts.
  colloquial_names: []
  evidence_refs:
  - ev.jiomart.settlement.8_5_credit_debit_notes
  confidence: high
  review_status: ready
```


```yaml
candidate_card:
  card_type: metric
  card_id: metric.jiomart.return_volume_by_type
  display_name: Return Volume by Type
  metric_family: returns
  domain_id: domain.jiomart.returns
  default_unit: INR
  default_grain: as specified by source SQL or query pattern
  business_definition: Return counts and refund amounts by return_type.
  colloquial_names: []
  evidence_refs:
  - ev.jiomart.returns.7_1_return_volume_by_type
  confidence: high
  review_status: ready
```


```yaml
candidate_card:
  card_type: metric
  card_id: metric.jiomart.return_cycle_time
  display_name: Return Cycle Time
  metric_family: returns
  domain_id: domain.jiomart.returns
  default_unit: INR
  default_grain: as specified by source SQL or query pattern
  business_definition: RTO turnaround days from return_initiate_date to return_delivery_date.
  colloquial_names: []
  evidence_refs:
  - ev.jiomart.returns.7_2_return_cycle_time_rto_turnaround
  confidence: high
  review_status: ready
```


```yaml
candidate_card:
  card_type: metric
  card_id: metric.jiomart.sku_return_rate
  display_name: SKU-Level Return Rate
  metric_family: returns
  domain_id: domain.jiomart.returns
  default_unit: INR
  default_grain: as specified by source SQL or query pattern
  business_definition: SKU-level return count and refund amount from returns table.
  colloquial_names: []
  evidence_refs:
  - ev.jiomart.returns.7_4_sku_level_return_rate
  confidence: high
  review_status: ready
```


```yaml
candidate_card:
  card_type: metric
  card_id: metric.jiomart.oms_monthly_gmv_clean
  display_name: OMS Monthly GMV Clean Rows
  metric_family: revenue
  domain_id: domain.jiomart.orders
  default_unit: INR
  default_grain: as specified by source SQL or query pattern
  business_definition: Clean row monthly forward/reverse GMV from OMS with hsn/order_date filters.
  colloquial_names: []
  evidence_refs:
  - ev.jiomart.oms.7_1_monthly_gmv_clean_rows_only
  confidence: high
  review_status: ready
```


```yaml
candidate_card:
  card_type: metric
  card_id: metric.jiomart.gst_breakdown
  display_name: Intra-State vs Inter-State GST
  metric_family: tax
  domain_id: domain.jiomart.tax
  default_unit: INR
  default_grain: as specified by source SQL or query pattern
  business_definition: GST type counts and amounts based on IGST vs CGST+SGST rates.
  colloquial_names: []
  evidence_refs:
  - ev.jiomart.oms.7_3_intra_state_vs_inter_state_gst_analysis
  confidence: high
  review_status: ready
```


```yaml
candidate_card:
  card_type: metric
  card_id: metric.jiomart.oms_sku_performance
  display_name: OMS SKU-Level Performance
  metric_family: product
  domain_id: domain.jiomart.product
  default_unit: INR
  default_grain: as specified by source SQL or query pattern
  business_definition: SKU-level orders, GMV, tax, and AOV from clean forward OMS rows.
  colloquial_names: []
  evidence_refs:
  - ev.jiomart.oms.7_4_sku_level_performance
  confidence: high
  review_status: ready
```


```yaml
candidate_card:
  card_type: metric
  card_id: metric.jiomart.tcs_deducted
  display_name: TCS Deducted / Reversed
  metric_family: tax
  domain_id: domain.jiomart.tax
  default_unit: TCS amount from OMS total_tcs_amount and settlement BaseTcs rows.
  default_grain: as specified by source SQL or query pattern
  business_definition: TCS Deducted / Reversed
  colloquial_names:
  - GST TCS
  - BaseTcs
  evidence_refs:
  - ev.jiomart.marketplace.5_3_tcs_tax_collected_at_source_gst_52
  - ev.jiomart.oms.tcs_rates_observed
  confidence: high
  review_status: ready
```


```yaml
candidate_card:
  card_type: metric
  card_id: metric.jiomart.tds_deducted
  display_name: TDS Deducted / Reversed
  metric_family: tax
  domain_id: domain.jiomart.tax
  default_unit: TDS amount from OMS total_tds and settlement Tds rows; reverse OMS rows have total_tds = 0.
  default_grain: as specified by source SQL or query pattern
  business_definition: TDS Deducted / Reversed
  colloquial_names:
  - 194-O TDS
  - Tds
  evidence_refs:
  - ev.jiomart.marketplace.5_4_tds_tax_deducted_at_source_income_tax_194_o
  - ev.jiomart.settlement.4_settlement_structure_event_based_multi_row_model
  confidence: high
  review_status: ready
```

### 4.9 `metric_implementation` cards


```yaml
candidate_card:
  card_type: metric_implementation
  card_id: metric_impl.jiomart.total_gmv
  metric_id: metric.jiomart.total_gmv
  platform_context_id: platform_context.jiomart.in
  display_name: JioMart implementation — Total GMV
  source_tables:
  - table.zs_observe.jiomart_oms
  source_columns:
  - charged_amount
  - transaction_type
  formula_sql_ref: sql.jiomart.marketplace.6_1_total_gmv
  formula_sql: |-
    SELECT
      SUM(CASE WHEN transaction_type = 'forward' THEN charged_amount ELSE 0 END) AS forward_gmv,
      SUM(CASE WHEN transaction_type = 'reverse' THEN ABS(charged_amount) ELSE 0 END) AS reversed_gmv,
      SUM(charged_amount) AS net_gmv
    FROM zs_observe.jiomart_oms
    WHERE is_active = true;
    -- Forward GMV: ~₹1.63 Cr | Reversed: ~₹22.4L | Net: ~₹1.40 Cr
  formula_text: Executable source SQL pattern retained verbatim.
  filters: Use filters exactly as shown in source SQL and mandatory filter rules.
  sign_semantics: Respect source transaction_type/accountable_type sign semantics before summing amounts.
  aggregation_order: Pre-aggregate multi-row settlement/return tables by order_id or source SQL grain before joining.
  evidence_refs:
  - ev.jiomart.marketplace.6_1_total_gmv
  confidence: high
  review_status: ready
```


```yaml
candidate_card:
  card_type: metric_implementation
  card_id: metric_impl.jiomart.return_rate
  metric_id: metric.jiomart.return_rate
  platform_context_id: platform_context.jiomart.in
  display_name: JioMart implementation — Return Rate
  source_tables:
  - table.zs_observe.jiomart_oms
  source_columns:
  - transaction_type
  - order_status
  formula_sql_ref: sql.jiomart.marketplace.6_2_return_rate
  formula_sql: |-
    SELECT
      ROUND(100.0 * COUNT_IF(order_status = 'shipment_returned')
        / NULLIF(COUNT_IF(transaction_type = 'forward'), 0), 2) AS rto_rate_pct,
      ROUND(100.0 * COUNT_IF(transaction_type = 'reverse')
        / NULLIF(COUNT_IF(transaction_type = 'forward'), 0), 2) AS return_reversal_pct
    FROM zs_observe.jiomart_oms
    WHERE is_active = true;
    -- RTO rate: ~14.8% | Return reversal rate: ~13.8%
  formula_text: Executable source SQL pattern retained verbatim.
  filters: Use filters exactly as shown in source SQL and mandatory filter rules.
  sign_semantics: Respect source transaction_type/accountable_type sign semantics before summing amounts.
  aggregation_order: Pre-aggregate multi-row settlement/return tables by order_id or source SQL grain before joining.
  evidence_refs:
  - ev.jiomart.marketplace.6_2_return_rate
  confidence: high
  review_status: ready
```


```yaml
candidate_card:
  card_type: metric_implementation
  card_id: metric_impl.jiomart.average_order_value
  metric_id: metric.jiomart.average_order_value
  platform_context_id: platform_context.jiomart.in
  display_name: JioMart implementation — Average Order Value
  source_tables:
  - table.zs_observe.jiomart_oms
  source_columns:
  - charged_amount
  - transaction_type
  - order_status
  formula_sql_ref: sql.jiomart.marketplace.6_3_average_order_value_aov
  formula_sql: |-
    SELECT AVG(charged_amount) AS aov
    FROM zs_observe.jiomart_oms
    WHERE is_active = true
      AND transaction_type = 'forward'
      AND order_status = 'delivered';
    -- Observed: ₹273.83
  formula_text: Executable source SQL pattern retained verbatim.
  filters: Use filters exactly as shown in source SQL and mandatory filter rules.
  sign_semantics: Respect source transaction_type/accountable_type sign semantics before summing amounts.
  aggregation_order: Pre-aggregate multi-row settlement/return tables by order_id or source SQL grain before joining.
  evidence_refs:
  - ev.jiomart.marketplace.6_3_average_order_value_aov
  confidence: high
  review_status: ready
```


```yaml
candidate_card:
  card_type: metric_implementation
  card_id: metric_impl.jiomart.net_settled_revenue
  metric_id: metric.jiomart.net_settled_revenue
  platform_context_id: platform_context.jiomart.in
  display_name: JioMart implementation — Net Settled Revenue
  source_tables:
  - table.zs_observe.jiomart_settlement
  source_columns:
  - settled_amount
  - accountable_type
  - event
  formula_sql_ref: sql.jiomart.marketplace.6_4_net_settled_revenue
  formula_sql: |-
    SELECT
      SUM(CASE WHEN accountable_type = 'Receivable' THEN settled_amount ELSE 0 END) AS gross_receivable,
      SUM(CASE WHEN accountable_type = 'BaseTcs' THEN settled_amount ELSE 0 END) AS tcs_net,
      SUM(CASE WHEN accountable_type = 'Tds' THEN settled_amount ELSE 0 END) AS tds_net,
      SUM(settled_amount) AS net_settled
    FROM zs_observe.jiomart_settlement
    WHERE is_active = true AND event IS NOT NULL;
  formula_text: Executable source SQL pattern retained verbatim.
  filters: Use filters exactly as shown in source SQL and mandatory filter rules.
  sign_semantics: Respect source transaction_type/accountable_type sign semantics before summing amounts.
  aggregation_order: Pre-aggregate multi-row settlement/return tables by order_id or source SQL grain before joining.
  evidence_refs:
  - ev.jiomart.marketplace.6_4_net_settled_revenue
  confidence: high
  review_status: ready
```


```yaml
candidate_card:
  card_type: metric_implementation
  card_id: metric_impl.jiomart.seller_coupon_discount_impact
  metric_id: metric.jiomart.seller_coupon_discount_impact
  platform_context_id: platform_context.jiomart.in
  display_name: JioMart implementation — Seller Coupon Discount Impact
  source_tables:
  - table.zs_observe.jiomart_oms
  source_columns:
  - seller_coupon_code
  - seller_coupon_amount
  formula_sql_ref: sql.jiomart.marketplace.6_5_seller_coupon_discount_impact
  formula_sql: |-
    SELECT
      seller_coupon_code,
      COUNT(*) AS orders,
      SUM(ABS(COALESCE(CAST(seller_coupon_amount AS DOUBLE), 0))) AS total_discount
    FROM zs_observe.jiomart_oms
    WHERE is_active = true
      AND seller_coupon_code IS NOT NULL
    GROUP BY seller_coupon_code
    ORDER BY total_discount DESC;
  formula_text: Executable source SQL pattern retained verbatim.
  filters: Use filters exactly as shown in source SQL and mandatory filter rules.
  sign_semantics: Respect source transaction_type/accountable_type sign semantics before summing amounts.
  aggregation_order: Pre-aggregate multi-row settlement/return tables by order_id or source SQL grain before joining.
  evidence_refs:
  - ev.jiomart.marketplace.6_5_seller_coupon_discount_impact
  confidence: high
  review_status: ready
```


```yaml
candidate_card:
  card_type: metric_implementation
  card_id: metric_impl.jiomart.monthly_forward_orders_and_gmv
  metric_id: metric.jiomart.monthly_forward_orders_gmv
  platform_context_id: platform_context.jiomart.in
  display_name: JioMart implementation — Monthly Forward Orders and GMV
  source_tables:
  - table.zs_observe.jiomart_oms
  source_columns:
  - created_date
  - charged_amount
  formula_sql_ref: sql.jiomart.marketplace.6_6_monthly_forward_orders_and_gmv
  formula_sql: |-
    SELECT
      CAST(DATE_TRUNC('month', CAST(created_date AS TIMESTAMP)) AS DATE) AS month,
      COUNT(*) AS orders,
      SUM(charged_amount) AS gmv,
      AVG(charged_amount) AS aov
    FROM zs_observe.jiomart_oms
    WHERE is_active = true AND transaction_type = 'forward'
    GROUP BY 1 ORDER BY 1;
  formula_text: Executable source SQL pattern retained verbatim.
  filters: Use filters exactly as shown in source SQL and mandatory filter rules.
  sign_semantics: Respect source transaction_type/accountable_type sign semantics before summing amounts.
  aggregation_order: Pre-aggregate multi-row settlement/return tables by order_id or source SQL grain before joining.
  evidence_refs:
  - ev.jiomart.marketplace.6_6_monthly_forward_orders_and_gmv
  confidence: high
  review_status: ready
```


```yaml
candidate_card:
  card_type: metric_implementation
  card_id: metric_impl.jiomart.shipment_status_summary
  metric_id: metric.jiomart.shipment_status_gmv
  platform_context_id: platform_context.jiomart.in
  display_name: JioMart implementation — Shipment Status Summary
  source_tables:
  - table.zs_observe.jiomart_shipment
  source_columns:
  - order_status
  - charged_amount
  - mrp
  - item_promo_discount
  formula_sql_ref: sql.jiomart.shipment.7_1_shipment_status_summary
  formula_sql: |-
    SELECT order_status,
      COUNT(*) AS cnt,
      SUM(charged_amount) AS gmv,
      SUM(mrp) AS total_mrp,
      SUM(item_promo_discount) AS total_discount,
      AVG(charged_amount) AS avg_selling_price,
      ROUND(100.0 * AVG(item_promo_discount) / NULLIF(AVG(mrp), 0), 2) AS avg_discount_pct
    FROM zs_observe.jiomart_shipment
    WHERE is_active = true
    GROUP BY order_status;
  formula_text: Executable source SQL pattern retained verbatim.
  filters: Use filters exactly as shown in source SQL and mandatory filter rules.
  sign_semantics: Respect source transaction_type/accountable_type sign semantics before summing amounts.
  aggregation_order: Pre-aggregate multi-row settlement/return tables by order_id or source SQL grain before joining.
  evidence_refs:
  - ev.jiomart.shipment.7_1_shipment_status_summary
  confidence: high
  review_status: ready
```


```yaml
candidate_card:
  card_type: metric_implementation
  card_id: metric_impl.jiomart.shipment_monthly_gmv
  metric_id: metric.jiomart.shipment_monthly_gmv
  platform_context_id: platform_context.jiomart.in
  display_name: JioMart implementation — Shipment Monthly GMV
  source_tables:
  - table.zs_observe.jiomart_shipment
  source_columns:
  - created_date
  - charged_amount
  - item_promo_discount
  formula_sql_ref: sql.jiomart.shipment.7_2_monthly_gmv
  formula_sql: |-
    SELECT
      CAST(DATE_TRUNC('month', CAST(created_date AS TIMESTAMP)) AS DATE) AS month,
      COUNT(*) AS shipments,
      SUM(charged_amount) AS gmv,
      SUM(item_promo_discount) AS promo_discount
    FROM zs_observe.jiomart_shipment
    WHERE is_active = true AND qty > 0
    GROUP BY 1 ORDER BY 1;
  formula_text: Executable source SQL pattern retained verbatim.
  filters: Use filters exactly as shown in source SQL and mandatory filter rules.
  sign_semantics: Respect source transaction_type/accountable_type sign semantics before summing amounts.
  aggregation_order: Pre-aggregate multi-row settlement/return tables by order_id or source SQL grain before joining.
  evidence_refs:
  - ev.jiomart.shipment.7_2_monthly_gmv
  confidence: high
  review_status: ready
```


```yaml
candidate_card:
  card_type: metric_implementation
  card_id: metric_impl.jiomart.top_shipment_skus
  metric_id: metric.jiomart.top_shipment_skus
  platform_context_id: platform_context.jiomart.in
  display_name: JioMart implementation — Top Shipment SKUs
  source_tables:
  - table.zs_observe.jiomart_shipment
  source_columns:
  - sku_id
  - charged_amount
  - item_promo_discount
  formula_sql_ref: sql.jiomart.shipment.7_3_top_skus
  formula_sql: |-
    SELECT sku_id,
      COUNT(*) AS orders,
      SUM(charged_amount) AS gmv,
      AVG(charged_amount) AS avg_price,
      AVG(item_promo_discount) AS avg_discount
    FROM zs_observe.jiomart_shipment
    WHERE is_active = true AND qty > 0
    GROUP BY sku_id
    ORDER BY gmv DESC
    LIMIT 20;
  formula_text: Executable source SQL pattern retained verbatim.
  filters: Use filters exactly as shown in source SQL and mandatory filter rules.
  sign_semantics: Respect source transaction_type/accountable_type sign semantics before summing amounts.
  aggregation_order: Pre-aggregate multi-row settlement/return tables by order_id or source SQL grain before joining.
  evidence_refs:
  - ev.jiomart.shipment.7_3_top_skus
  confidence: high
  review_status: ready
```


```yaml
candidate_card:
  card_type: metric_implementation
  card_id: metric_impl.jiomart.net_settlement_per_order
  metric_id: metric.jiomart.net_settlement_per_order
  platform_context_id: platform_context.jiomart.in
  display_name: JioMart implementation — Net Settlement per Order
  source_tables:
  - table.zs_observe.jiomart_settlement
  source_columns:
  - order_id
  - settled_amount
  - accountable_type
  formula_sql_ref: sql.jiomart.settlement.8_1_net_settlement_per_order_structured_rows
  formula_sql: |-
    SELECT
      order_id,
      SUM(CASE WHEN accountable_type = 'Receivable' THEN settled_amount ELSE 0 END) AS sale_proceeds,
      SUM(CASE WHEN accountable_type = 'BaseTcs' THEN settled_amount ELSE 0 END) AS tcs_impact,
      SUM(CASE WHEN accountable_type = 'Tds' THEN settled_amount ELSE 0 END) AS tds_impact,
      SUM(settled_amount) AS net_settled
    FROM zs_observe.jiomart_settlement
    WHERE is_active = true AND event IS NOT NULL
    GROUP BY order_id
    ORDER BY net_settled DESC
    LIMIT 20;
  formula_text: Executable source SQL pattern retained verbatim.
  filters: Use filters exactly as shown in source SQL and mandatory filter rules.
  sign_semantics: Respect source transaction_type/accountable_type sign semantics before summing amounts.
  aggregation_order: Pre-aggregate multi-row settlement/return tables by order_id or source SQL grain before joining.
  evidence_refs:
  - ev.jiomart.settlement.8_1_net_settlement_per_order_structured_rows
  confidence: high
  review_status: ready
```


```yaml
candidate_card:
  card_type: metric_implementation
  card_id: metric_impl.jiomart.monthly_settlement_summary
  metric_id: metric.jiomart.monthly_settlement_summary
  platform_context_id: platform_context.jiomart.in
  display_name: JioMart implementation — Monthly Settlement Summary
  source_tables:
  - table.zs_observe.jiomart_settlement
  source_columns:
  - settlement_date
  - transaction_type
  - accountable_type
  - settled_amount
  formula_sql_ref: sql.jiomart.settlement.8_2_monthly_settlement_summary
  formula_sql: |-
    SELECT
      DATE_TRUNC('month', settlement_date) AS month,
      transaction_type,
      accountable_type,
      COUNT(*) AS rows,
      SUM(settled_amount) AS total_settled
    FROM zs_observe.jiomart_settlement
    WHERE is_active = true AND event IS NOT NULL
    GROUP BY 1, 2, 3
    ORDER BY 1, 2, 3;
  formula_text: Executable source SQL pattern retained verbatim.
  filters: Use filters exactly as shown in source SQL and mandatory filter rules.
  sign_semantics: Respect source transaction_type/accountable_type sign semantics before summing amounts.
  aggregation_order: Pre-aggregate multi-row settlement/return tables by order_id or source SQL grain before joining.
  evidence_refs:
  - ev.jiomart.settlement.8_2_monthly_settlement_summary
  confidence: high
  review_status: ready
```


```yaml
candidate_card:
  card_type: metric_implementation
  card_id: metric_impl.jiomart.credit_debit_note_impact
  metric_id: metric.jiomart.credit_debit_note_impact
  platform_context_id: platform_context.jiomart.in
  display_name: JioMart implementation — Credit / Debit Note Impact
  source_tables:
  - table.zs_observe.jiomart_settlement
  source_columns:
  - transaction_type
  - event
  - accountable_type
  - settled_amount
  formula_sql_ref: sql.jiomart.settlement.8_5_credit_debit_notes
  formula_sql: |-
    SELECT
      transaction_type, event, accountable_type,
      COUNT(*) AS cnt,
      SUM(settled_amount) AS total
    FROM zs_observe.jiomart_settlement
    WHERE is_active = true
      AND transaction_type IN ('Credit Note', 'Debit Note', 'Service Invoice', 'Bill Tds Refund')
    GROUP BY 1, 2, 3;
  formula_text: Executable source SQL pattern retained verbatim.
  filters: Use filters exactly as shown in source SQL and mandatory filter rules.
  sign_semantics: Respect source transaction_type/accountable_type sign semantics before summing amounts.
  aggregation_order: Pre-aggregate multi-row settlement/return tables by order_id or source SQL grain before joining.
  evidence_refs:
  - ev.jiomart.settlement.8_5_credit_debit_notes
  confidence: high
  review_status: ready
```


```yaml
candidate_card:
  card_type: metric_implementation
  card_id: metric_impl.jiomart.return_volume_by_type
  metric_id: metric.jiomart.return_volume_by_type
  platform_context_id: platform_context.jiomart.in
  display_name: JioMart implementation — Return Volume by Type
  source_tables:
  - table.zs_observe.jiomart_returns
  source_columns:
  - return_type
  - refund_amount
  formula_sql_ref: sql.jiomart.returns.7_1_return_volume_by_type
  formula_sql: |-
    SELECT
      COALESCE(return_type, 'Unknown/Old Format') AS return_type,
      return_status,
      COUNT(*) AS cnt,
      SUM(CAST(charged_amount AS DOUBLE)) AS total_charged,
      SUM(CAST(refund_amount AS DOUBLE)) AS total_refund
    FROM zs_observe.jiomart_returns
    WHERE is_active = true
    GROUP BY 1, 2
    ORDER BY cnt DESC;
  formula_text: Executable source SQL pattern retained verbatim.
  filters: Use filters exactly as shown in source SQL and mandatory filter rules.
  sign_semantics: Respect source transaction_type/accountable_type sign semantics before summing amounts.
  aggregation_order: Pre-aggregate multi-row settlement/return tables by order_id or source SQL grain before joining.
  evidence_refs:
  - ev.jiomart.returns.7_1_return_volume_by_type
  confidence: high
  review_status: ready
```


```yaml
candidate_card:
  card_type: metric_implementation
  card_id: metric_impl.jiomart.return_cycle_time
  metric_id: metric.jiomart.return_cycle_time
  platform_context_id: platform_context.jiomart.in
  display_name: JioMart implementation — Return Cycle Time
  source_tables:
  - table.zs_observe.jiomart_returns
  source_columns:
  - return_initiate_date
  - return_delivery_date
  formula_sql_ref: sql.jiomart.returns.7_2_return_cycle_time_rto_turnaround
  formula_sql: |-
    SELECT
      courier_partner,
      COUNT(*) AS returns,
      AVG(DATE_DIFF('day',
        CAST(return_initiate_date AS TIMESTAMP),
        CAST(return_delivery_date AS TIMESTAMP))) AS avg_days_to_warehouse
    FROM zs_observe.jiomart_returns
    WHERE is_active = true
      AND return_type = 'ReturnToOrigin'
      AND return_initiate_date IS NOT NULL
      AND return_delivery_date IS NOT NULL
    GROUP BY courier_partner;
  formula_text: Executable source SQL pattern retained verbatim.
  filters: Use filters exactly as shown in source SQL and mandatory filter rules.
  sign_semantics: Respect source transaction_type/accountable_type sign semantics before summing amounts.
  aggregation_order: Pre-aggregate multi-row settlement/return tables by order_id or source SQL grain before joining.
  evidence_refs:
  - ev.jiomart.returns.7_2_return_cycle_time_rto_turnaround
  confidence: high
  review_status: ready
```


```yaml
candidate_card:
  card_type: metric_implementation
  card_id: metric_impl.jiomart.sku_level_return_rate
  metric_id: metric.jiomart.sku_return_rate
  platform_context_id: platform_context.jiomart.in
  display_name: JioMart implementation — SKU-Level Return Rate
  source_tables:
  - table.zs_observe.jiomart_returns
  source_columns:
  - sku_id
  - refund_amount
  formula_sql_ref: sql.jiomart.returns.7_4_sku_level_return_rate
  formula_sql: |-
    SELECT
      r.sku_id,
      COUNT(*) AS returns,
      SUM(CAST(r.charged_amount AS DOUBLE)) AS returned_value
    FROM zs_observe.jiomart_returns r
    WHERE r.is_active = true
    GROUP BY r.sku_id
    ORDER BY returns DESC;
  formula_text: Executable source SQL pattern retained verbatim.
  filters: Use filters exactly as shown in source SQL and mandatory filter rules.
  sign_semantics: Respect source transaction_type/accountable_type sign semantics before summing amounts.
  aggregation_order: Pre-aggregate multi-row settlement/return tables by order_id or source SQL grain before joining.
  evidence_refs:
  - ev.jiomart.returns.7_4_sku_level_return_rate
  confidence: high
  review_status: ready
```


```yaml
candidate_card:
  card_type: metric_implementation
  card_id: metric_impl.jiomart.oms_monthly_gmv_clean_rows
  metric_id: metric.jiomart.oms_monthly_gmv_clean
  platform_context_id: platform_context.jiomart.in
  display_name: JioMart implementation — OMS Monthly GMV Clean Rows
  source_tables:
  - table.zs_observe.jiomart_oms
  source_columns:
  - created_date
  - charged_amount
  - transaction_type
  - hsn
  - order_date
  formula_sql_ref: sql.jiomart.oms.7_1_monthly_gmv_clean_rows_only
  formula_sql: |-
    SELECT
      CAST(DATE_TRUNC('month', CAST(created_date AS TIMESTAMP)) AS DATE) AS month,
      transaction_type,
      COUNT(*) AS orders,
      SUM(charged_amount) AS gmv,
      SUM(total_tcs_amount) AS tcs,
      SUM(total_tds) AS tds
    FROM zs_observe.jiomart_oms
    WHERE is_active = true
    GROUP BY 1, 2
    ORDER BY 1, 2;
  formula_text: Executable source SQL pattern retained verbatim.
  filters: Use filters exactly as shown in source SQL and mandatory filter rules.
  sign_semantics: Respect source transaction_type/accountable_type sign semantics before summing amounts.
  aggregation_order: Pre-aggregate multi-row settlement/return tables by order_id or source SQL grain before joining.
  evidence_refs:
  - ev.jiomart.oms.7_1_monthly_gmv_clean_rows_only
  confidence: high
  review_status: ready
```


```yaml
candidate_card:
  card_type: metric_implementation
  card_id: metric_impl.jiomart.intra_state_vs_inter_state_gst
  metric_id: metric.jiomart.gst_breakdown
  platform_context_id: platform_context.jiomart.in
  display_name: JioMart implementation — Intra-State vs Inter-State GST
  source_tables:
  - table.zs_observe.jiomart_oms
  source_columns:
  - tax_igst_rate
  - tax_igst_amount
  - tax_cgst_amount
  - tax_sgst_amount
  formula_sql_ref: sql.jiomart.oms.7_3_intra_state_vs_inter_state_gst_analysis
  formula_sql: |-
    SELECT
      CASE
        WHEN UPPER(source_state) = UPPER(destination_state) THEN 'Intra-State'
        ELSE 'Inter-State'
      END AS gst_type,
      COUNT(*) AS cnt,
      SUM(charged_amount) AS gmv,
      SUM(tax_igst_amount) AS igst,
      SUM(tax_cgst_amount + tax_sgst_amount) AS cgst_sgst
    FROM zs_observe.jiomart_oms
    WHERE is_active = true
      AND transaction_type = 'forward'
      AND hsn IS NOT NULL
    GROUP BY 1;
  formula_text: Executable source SQL pattern retained verbatim.
  filters: Use filters exactly as shown in source SQL and mandatory filter rules.
  sign_semantics: Respect source transaction_type/accountable_type sign semantics before summing amounts.
  aggregation_order: Pre-aggregate multi-row settlement/return tables by order_id or source SQL grain before joining.
  evidence_refs:
  - ev.jiomart.oms.7_3_intra_state_vs_inter_state_gst_analysis
  confidence: high
  review_status: ready
```


```yaml
candidate_card:
  card_type: metric_implementation
  card_id: metric_impl.jiomart.oms_sku_level_performance
  metric_id: metric.jiomart.oms_sku_performance
  platform_context_id: platform_context.jiomart.in
  display_name: JioMart implementation — OMS SKU-Level Performance
  source_tables:
  - table.zs_observe.jiomart_oms
  source_columns:
  - sku_id
  - mp_sin
  - charged_amount
  formula_sql_ref: sql.jiomart.oms.7_4_sku_level_performance
  formula_sql: |-
    SELECT sku_id, mp_sin,
      COUNT(*) AS orders,
      SUM(charged_amount) AS gmv,
      AVG(charged_amount) AS avg_price,
      ROUND(100.0 * COUNT_IF(transaction_type = 'forward' AND order_status = 'shipment_returned')
        / NULLIF(COUNT_IF(transaction_type = 'forward'), 0), 2) AS rto_rate_pct
    FROM zs_observe.jiomart_oms
    WHERE is_active = true AND hsn IS NOT NULL
    GROUP BY sku_id, mp_sin
    ORDER BY gmv DESC;
  formula_text: Executable source SQL pattern retained verbatim.
  filters: Use filters exactly as shown in source SQL and mandatory filter rules.
  sign_semantics: Respect source transaction_type/accountable_type sign semantics before summing amounts.
  aggregation_order: Pre-aggregate multi-row settlement/return tables by order_id or source SQL grain before joining.
  evidence_refs:
  - ev.jiomart.oms.7_4_sku_level_performance
  confidence: high
  review_status: ready
```


```yaml
candidate_card:
  card_type: metric_implementation
  card_id: metric_impl.jiomart.tcs_reconciliation
  metric_id: metric.jiomart.tcs_deducted
  platform_context_id: platform_context.jiomart.in
  display_name: JioMart implementation — TCS Reconciliation
  source_tables:
  - table.zs_observe.jiomart_oms
  - table.zs_observe.jiomart_settlement
  source_columns:
  - total_tcs_amount
  - settled_amount
  - accountable_type
  - transaction_type
  formula_sql_ref: sql.jiomart.marketplace.7_4_tcs_reconciliation
  formula_sql: |-
    SELECT 'OMS TCS' AS source, SUM(total_tcs_amount) AS amount
    FROM zs_observe.jiomart_oms WHERE is_active = true AND transaction_type = 'forward'
    UNION ALL
    SELECT 'Settlement BaseTcs (Forward)', SUM(settled_amount)
    FROM zs_observe.jiomart_settlement
    WHERE is_active = true AND accountable_type = 'BaseTcs' AND transaction_type = 'forward'
    UNION ALL
    SELECT 'Settlement BaseTcs (Return Reversal)', SUM(settled_amount)
    FROM zs_observe.jiomart_settlement
    WHERE is_active = true AND accountable_type = 'BaseTcs' AND transaction_type = 'reverse';
  formula_text: Executable source SQL pattern retained verbatim.
  filters: Use filters exactly as shown in source SQL and mandatory filter rules.
  sign_semantics: Respect source transaction_type/accountable_type sign semantics before summing amounts.
  aggregation_order: Pre-aggregate multi-row settlement/return tables by order_id or source SQL grain before joining.
  evidence_refs:
  - ev.jiomart.marketplace.7_4_tcs_reconciliation
  confidence: high
  review_status: ready
```

### 4.10 `formula_template` cards


```yaml
candidate_card:
  card_type: formula_template
  card_id: formula.jiomart.structured_settlement_net
  display_name: Structured settlement per-order net
  formula_expression: SUM(settled_amount) grouped by order_id after filtering is_active = true AND event IS NOT NULL; break
    out accountable_type Receivable/BaseTcs/Tds.
  input_variables:
  - settled_amount
  - order_id
  - accountable_type
  - event
  aggregation_order: Follow source SQL grain and filters before calculating.
  null_handling: Use NULLIF/CASE/CAST patterns exactly as source SQL shows; do not aggregate varchar amounts without cast.
  evidence_refs:
  - ev.jiomart.settlement.8_1_net_settlement_per_order_structured_rows
  confidence: high
  review_status: ready
```


```yaml
candidate_card:
  card_type: formula_template
  card_id: formula.jiomart.forward_gmv
  display_name: Forward/reverse/net GMV from OMS
  formula_expression: forward_gmv = SUM(charged_amount where transaction_type='forward'); reversed_gmv = SUM(ABS(charged_amount)
    where transaction_type='reverse'); net_gmv = SUM(charged_amount).
  input_variables:
  - charged_amount
  - transaction_type
  aggregation_order: Follow source SQL grain and filters before calculating.
  null_handling: Use NULLIF/CASE/CAST patterns exactly as source SQL shows; do not aggregate varchar amounts without cast.
  evidence_refs:
  - ev.jiomart.marketplace.6_1_total_gmv
  confidence: high
  review_status: ready
```


```yaml
candidate_card:
  card_type: formula_template
  card_id: formula.jiomart.return_rate
  display_name: Return rate from OMS
  formula_expression: |-
    rto_rate_pct = COUNT_IF(order_status='shipment_returned') / COUNT_IF(transaction_type='forward'); return_reversal_pct = COUNT_IF(transaction_type='reverse') / COUNT_IF(transaction_type='forward').
  input_variables:
  - order_status
  - transaction_type
  aggregation_order: Follow source SQL grain and filters before calculating.
  null_handling: Use NULLIF/CASE/CAST patterns exactly as source SQL shows; do not aggregate varchar amounts without cast.
  evidence_refs:
  - ev.jiomart.marketplace.6_2_return_rate
  confidence: high
  review_status: ready
```


```yaml
candidate_card:
  card_type: formula_template
  card_id: formula.jiomart.tcs_variance
  display_name: TCS variance
  formula_expression: tcs_variance = o.total_tcs_amount + SUM(s.settled_amount where s.accountable_type='BaseTcs') by order_id;
    sign differs because BaseTcs forward rows are negative in settlement.
  input_variables:
  - total_tcs_amount
  - settled_amount
  - accountable_type
  aggregation_order: Follow source SQL grain and filters before calculating.
  null_handling: Use NULLIF/CASE/CAST patterns exactly as source SQL shows; do not aggregate varchar amounts without cast.
  evidence_refs:
  - ev.jiomart.marketplace.7_1_oms_settlement_match_3_way_per_order
  confidence: high
  review_status: ready
```


```yaml
candidate_card:
  card_type: formula_template
  card_id: formula.jiomart.return_cycle_days
  display_name: Return cycle days
  formula_expression: date_diff('day', CAST(return_initiate_date AS DATE), CAST(return_delivery_date AS DATE)) for RTO rows
    with both dates populated.
  input_variables:
  - return_initiate_date
  - return_delivery_date
  aggregation_order: Follow source SQL grain and filters before calculating.
  null_handling: Use NULLIF/CASE/CAST patterns exactly as source SQL shows; do not aggregate varchar amounts without cast.
  evidence_refs:
  - ev.jiomart.returns.7_2_return_cycle_time_rto_turnaround
  confidence: high
  review_status: ready
```

### 4.11 `business_process` cards


```yaml
candidate_card:
  card_type: business_process
  card_id: business_process.jiomart.forward_order_flow
  display_name: JioMart forward order flow
  process_family: orders
  description: JioMart forward order flow as explicitly described in the source DOCX using JioMart table/column/status semantics.
  entry_condition: See workflow steps; all steps name source tables/columns/values.
  exit_condition: See workflow steps and settlement/return conditions.
  source_tables:
  - table.zs_observe.jiomart_oms
  - table.zs_observe.jiomart_settlement
  state_fields: Status values are represented in workflow conditions and value profiles; no separate state_transition cards
    emitted.
  evidence_refs:
  - ev.jiomart.marketplace.3_1_forward_order_flow
  confidence: high
  review_status: ready
```


```yaml
candidate_card:
  card_type: business_process
  card_id: business_process.jiomart.rto_flow
  display_name: JioMart RTO return-to-origin flow
  process_family: returns
  description: JioMart RTO return-to-origin flow as explicitly described in the source DOCX using JioMart table/column/status
    semantics.
  entry_condition: See workflow steps; all steps name source tables/columns/values.
  exit_condition: See workflow steps and settlement/return conditions.
  source_tables:
  - table.zs_observe.jiomart_oms
  - table.zs_observe.jiomart_returns
  - table.zs_observe.jiomart_settlement
  state_fields: Status values are represented in workflow conditions and value profiles; no separate state_transition cards
    emitted.
  evidence_refs:
  - ev.jiomart.marketplace.3_2_rto_return_to_origin_flow
  confidence: high
  review_status: ready
```


```yaml
candidate_card:
  card_type: business_process
  card_id: business_process.jiomart.doorstep_return_flow
  display_name: JioMart doorstep return flow
  process_family: returns
  description: JioMart doorstep return flow as explicitly described in the source DOCX using JioMart table/column/status semantics.
  entry_condition: See workflow steps; all steps name source tables/columns/values.
  exit_condition: See workflow steps and settlement/return conditions.
  source_tables:
  - table.zs_observe.jiomart_returns
  - table.zs_observe.jiomart_settlement
  state_fields: Status values are represented in workflow conditions and value profiles; no separate state_transition cards
    emitted.
  evidence_refs:
  - ev.jiomart.marketplace.3_3_doorstep_return_flow
  confidence: high
  review_status: ready
```


```yaml
candidate_card:
  card_type: business_process
  card_id: business_process.jiomart.pre_shipment_cancellation_flow
  display_name: JioMart pre-shipment cancellation flow
  process_family: returns
  description: JioMart pre-shipment cancellation flow as explicitly described in the source DOCX using JioMart table/column/status
    semantics.
  entry_condition: See workflow steps; all steps name source tables/columns/values.
  exit_condition: See workflow steps and settlement/return conditions.
  source_tables:
  - table.zs_observe.jiomart_returns
  state_fields: Status values are represented in workflow conditions and value profiles; no separate state_transition cards
    emitted.
  evidence_refs:
  - ev.jiomart.marketplace.3_4_pre_shipment_cancellation_flow
  confidence: high
  review_status: ready
```


```yaml
candidate_card:
  card_type: business_process
  card_id: business_process.jiomart.settlement_event_model
  display_name: JioMart event-based settlement row model
  process_family: settlement
  description: JioMart event-based settlement row model as explicitly described in the source DOCX using JioMart table/column/status
    semantics.
  entry_condition: See workflow steps; all steps name source tables/columns/values.
  exit_condition: See workflow steps and settlement/return conditions.
  source_tables:
  - table.zs_observe.jiomart_settlement
  state_fields: Status values are represented in workflow conditions and value profiles; no separate state_transition cards
    emitted.
  evidence_refs:
  - ev.jiomart.settlement.4_settlement_structure_event_based_multi_row_model
  confidence: high
  review_status: ready
```

### 4.12 `workflow_step` cards


```yaml
candidate_card:
  card_type: workflow_step
  card_id: workflow_step.jiomart.forward_order_flow.01
  display_name: Order appears in jiomart_oms
  process_id: business_process.jiomart.forward_order_flow
  step_order: 1
  description: jiomart_oms transaction_type = forward and order_status = invoiced.
  input_tables:
  - table.zs_observe.jiomart_oms
  output_evidence: Source-specific status/amount/date fields are named in the description.
  responsible_platform_side: marketplace_or_seller_side_as_source_describes; no external account/logistics card emitted.
  evidence_refs:
  - ev.jiomart.marketplace.3_1_forward_order_flow
  confidence: high
  review_status: ready
```


```yaml
candidate_card:
  card_type: workflow_step
  card_id: workflow_step.jiomart.forward_order_flow.02
  display_name: Seller dispatch context set
  process_id: business_process.jiomart.forward_order_flow
  step_order: 2
  description: GSTIN determined by dispatch state; source_gst_id/seller_gstin/source_state columns preserve context.
  input_tables:
  - table.zs_observe.jiomart_oms
  output_evidence: Source-specific status/amount/date fields are named in the description.
  responsible_platform_side: marketplace_or_seller_side_as_source_describes; no external account/logistics card emitted.
  evidence_refs:
  - ev.jiomart.marketplace.3_1_forward_order_flow
  confidence: high
  review_status: ready
```


```yaml
candidate_card:
  card_type: workflow_step
  card_id: workflow_step.jiomart.forward_order_flow.03
  display_name: Courier pickup recorded
  process_id: business_process.jiomart.forward_order_flow
  step_order: 3
  description: order_status = pick_up_confirmed in jiomart_oms.
  input_tables:
  - table.zs_observe.jiomart_oms
  output_evidence: Source-specific status/amount/date fields are named in the description.
  responsible_platform_side: marketplace_or_seller_side_as_source_describes; no external account/logistics card emitted.
  evidence_refs:
  - ev.jiomart.marketplace.3_1_forward_order_flow
  confidence: high
  review_status: ready
```


```yaml
candidate_card:
  card_type: workflow_step
  card_id: workflow_step.jiomart.forward_order_flow.04
  display_name: Delivery completed
  process_id: business_process.jiomart.forward_order_flow
  step_order: 4
  description: order_status = delivered in jiomart_oms; 7-day return window starts.
  input_tables:
  - table.zs_observe.jiomart_oms
  output_evidence: Source-specific status/amount/date fields are named in the description.
  responsible_platform_side: marketplace_or_seller_side_as_source_describes; no external account/logistics card emitted.
  evidence_refs:
  - ev.jiomart.marketplace.3_1_forward_order_flow
  confidence: high
  review_status: ready
```


```yaml
candidate_card:
  card_type: workflow_step
  card_id: workflow_step.jiomart.forward_order_flow.05
  display_name: Settlement rows generated
  process_id: business_process.jiomart.forward_order_flow
  step_order: 5
  description: jiomart_settlement event = Invoice and accountable_type in Receivable/BaseTcs/Tds.
  input_tables:
  - table.zs_observe.jiomart_settlement
  output_evidence: Source-specific status/amount/date fields are named in the description.
  responsible_platform_side: marketplace_or_seller_side_as_source_describes; no external account/logistics card emitted.
  evidence_refs:
  - ev.jiomart.marketplace.3_1_forward_order_flow
  confidence: high
  review_status: ready
```


```yaml
candidate_card:
  card_type: workflow_step
  card_id: workflow_step.jiomart.rto_flow.01
  display_name: Delivery failure captured
  process_id: business_process.jiomart.rto_flow
  step_order: 1
  description: jiomart_oms order_status = shipment_returned and jiomart_returns transaction_type = ReturnToOrigin.
  input_tables:
  - table.zs_observe.jiomart_oms
  - table.zs_observe.jiomart_returns
  output_evidence: Source-specific status/amount/date fields are named in the description.
  responsible_platform_side: marketplace_or_seller_side_as_source_describes; no external account/logistics card emitted.
  evidence_refs:
  - ev.jiomart.marketplace.3_2_rto_return_to_origin_flow
  confidence: high
  review_status: ready
```


```yaml
candidate_card:
  card_type: workflow_step
  card_id: workflow_step.jiomart.rto_flow.02
  display_name: Return delivered back
  process_id: business_process.jiomart.rto_flow
  step_order: 2
  description: jiomart_returns return_delivery_date records courier return to origin warehouse.
  input_tables:
  - table.zs_observe.jiomart_returns
  output_evidence: Source-specific status/amount/date fields are named in the description.
  responsible_platform_side: marketplace_or_seller_side_as_source_describes; no external account/logistics card emitted.
  evidence_refs:
  - ev.jiomart.marketplace.3_2_rto_return_to_origin_flow
  confidence: high
  review_status: ready
```


```yaml
candidate_card:
  card_type: workflow_step
  card_id: workflow_step.jiomart.rto_flow.03
  display_name: Settlement reversed
  process_id: business_process.jiomart.rto_flow
  step_order: 3
  description: jiomart_settlement event = Return, accountable_type = Receivable with negative settled_amount.
  input_tables:
  - table.zs_observe.jiomart_settlement
  output_evidence: Source-specific status/amount/date fields are named in the description.
  responsible_platform_side: marketplace_or_seller_side_as_source_describes; no external account/logistics card emitted.
  evidence_refs:
  - ev.jiomart.marketplace.3_2_rto_return_to_origin_flow
  confidence: high
  review_status: ready
```


```yaml
candidate_card:
  card_type: workflow_step
  card_id: workflow_step.jiomart.rto_flow.04
  display_name: TCS reversed
  process_id: business_process.jiomart.rto_flow
  step_order: 4
  description: BaseTcs return entry has positive settled_amount.
  input_tables:
  - table.zs_observe.jiomart_settlement
  output_evidence: Source-specific status/amount/date fields are named in the description.
  responsible_platform_side: marketplace_or_seller_side_as_source_describes; no external account/logistics card emitted.
  evidence_refs:
  - ev.jiomart.marketplace.3_2_rto_return_to_origin_flow
  confidence: high
  review_status: ready
```


```yaml
candidate_card:
  card_type: workflow_step
  card_id: workflow_step.jiomart.doorstep_return_flow.01
  display_name: Doorstep return type captured
  process_id: business_process.jiomart.doorstep_return_flow
  step_order: 1
  description: jiomart_returns transaction_type = DoorStepReturn.
  input_tables:
  - table.zs_observe.jiomart_returns
  output_evidence: Source-specific status/amount/date fields are named in the description.
  responsible_platform_side: marketplace_or_seller_side_as_source_describes; no external account/logistics card emitted.
  evidence_refs:
  - ev.jiomart.marketplace.3_3_doorstep_return_flow
  confidence: high
  review_status: ready
```


```yaml
candidate_card:
  card_type: workflow_step
  card_id: workflow_step.jiomart.doorstep_return_flow.02
  display_name: Courier takes item back immediately
  process_id: business_process.jiomart.doorstep_return_flow
  step_order: 2
  description: return AWB/courier fields preserve marketplace return-journey detail.
  input_tables:
  - table.zs_observe.jiomart_returns
  output_evidence: Source-specific status/amount/date fields are named in the description.
  responsible_platform_side: marketplace_or_seller_side_as_source_describes; no external account/logistics card emitted.
  evidence_refs:
  - ev.jiomart.marketplace.3_3_doorstep_return_flow
  confidence: high
  review_status: ready
```


```yaml
candidate_card:
  card_type: workflow_step
  card_id: workflow_step.jiomart.doorstep_return_flow.03
  display_name: Full refund and settlement reversal
  process_id: business_process.jiomart.doorstep_return_flow
  step_order: 3
  description: jiomart_returns.refund_amount and jiomart_settlement transaction_type = reverse rows represent returned sale
    impact.
  input_tables:
  - table.zs_observe.jiomart_returns
  - table.zs_observe.jiomart_settlement
  output_evidence: Source-specific status/amount/date fields are named in the description.
  responsible_platform_side: marketplace_or_seller_side_as_source_describes; no external account/logistics card emitted.
  evidence_refs:
  - ev.jiomart.marketplace.3_3_doorstep_return_flow
  confidence: high
  review_status: ready
```


```yaml
candidate_card:
  card_type: workflow_step
  card_id: workflow_step.jiomart.pre_shipment_cancellation_flow.01
  display_name: Cancellation before dispatch
  process_id: business_process.jiomart.pre_shipment_cancellation_flow
  step_order: 1
  description: jiomart_returns transaction_type = BeforeShippingReturn.
  input_tables:
  - table.zs_observe.jiomart_returns
  output_evidence: Source-specific status/amount/date fields are named in the description.
  responsible_platform_side: marketplace_or_seller_side_as_source_describes; no external account/logistics card emitted.
  evidence_refs:
  - ev.jiomart.marketplace.3_4_pre_shipment_cancellation_flow
  confidence: high
  review_status: ready
```


```yaml
candidate_card:
  card_type: workflow_step
  card_id: workflow_step.jiomart.pre_shipment_cancellation_flow.02
  display_name: No courier movement
  process_id: business_process.jiomart.pre_shipment_cancellation_flow
  step_order: 2
  description: jiomart_returns transaction_type = BeforeShippingReturn has no shipping cost and no courier movement.
  input_tables:
  - table.zs_observe.jiomart_returns
  output_evidence: Source-specific status/amount/date fields are named in the description.
  responsible_platform_side: marketplace_or_seller_side_as_source_describes; no external account/logistics card emitted.
  evidence_refs:
  - ev.jiomart.marketplace.3_4_pre_shipment_cancellation_flow
  confidence: high
  review_status: ready
```


```yaml
candidate_card:
  card_type: workflow_step
  card_id: workflow_step.jiomart.pre_shipment_cancellation_flow.03
  display_name: Immediate refund
  process_id: business_process.jiomart.pre_shipment_cancellation_flow
  step_order: 3
  description: Refund processed immediately for jiomart_returns transaction_type = BeforeShippingReturn; use refund_amount
    when present.
  input_tables:
  - table.zs_observe.jiomart_returns
  output_evidence: Source-specific status/amount/date fields are named in the description.
  responsible_platform_side: marketplace_or_seller_side_as_source_describes; no external account/logistics card emitted.
  evidence_refs:
  - ev.jiomart.marketplace.3_4_pre_shipment_cancellation_flow
  confidence: high
  review_status: ready
```


```yaml
candidate_card:
  card_type: workflow_step
  card_id: workflow_step.jiomart.settlement_event_model.01
  display_name: Forward invoice rows
  process_id: business_process.jiomart.settlement_event_model
  step_order: 1
  description: For delivered orders, Receivable/BaseTcs/Tds rows are created with event = Invoice.
  input_tables:
  - table.zs_observe.jiomart_settlement
  output_evidence: Source-specific status/amount/date fields are named in the description.
  responsible_platform_side: marketplace_or_seller_side_as_source_describes; no external account/logistics card emitted.
  evidence_refs:
  - ev.jiomart.settlement.4_settlement_structure_event_based_multi_row_model
  confidence: high
  review_status: ready
```


```yaml
candidate_card:
  card_type: workflow_step
  card_id: workflow_step.jiomart.settlement_event_model.02
  display_name: Return rows
  process_id: business_process.jiomart.settlement_event_model
  step_order: 2
  description: For returns, Receivable/BaseTcs/Tds rows are created with event = Return and opposite signs.
  input_tables:
  - table.zs_observe.jiomart_settlement
  output_evidence: Source-specific status/amount/date fields are named in the description.
  responsible_platform_side: marketplace_or_seller_side_as_source_describes; no external account/logistics card emitted.
  evidence_refs:
  - ev.jiomart.settlement.4_settlement_structure_event_based_multi_row_model
  confidence: high
  review_status: ready
```


```yaml
candidate_card:
  card_type: workflow_step
  card_id: workflow_step.jiomart.settlement_event_model.03
  display_name: Older format rows handled
  process_id: business_process.jiomart.settlement_event_model
  step_order: 3
  description: event NULL rows are included for total settlement but excluded from structured analysis.
  input_tables:
  - table.zs_observe.jiomart_settlement
  output_evidence: Source-specific status/amount/date fields are named in the description.
  responsible_platform_side: marketplace_or_seller_side_as_source_describes; no external account/logistics card emitted.
  evidence_refs:
  - ev.jiomart.settlement.4_settlement_structure_event_based_multi_row_model
  confidence: high
  review_status: ready
```

### 4.13 `reconciliation_profile` cards


```yaml
candidate_card:
  card_type: reconciliation_profile
  card_id: reconciliation_profile.jiomart.oms_settlement_3way
  display_name: JioMart OMS → Settlement 3-way per-order reconciliation
  process_id: business_process.jiomart.settlement_event_model
  reconciliation_family: oms_to_settlement
  expected_side: reconciliation_side.jiomart.oms_settlement.expected_oms
  actual_side: reconciliation_side.jiomart.oms_settlement.actual_settlement
  unit_id: reconciliation_unit.jiomart.order_id
  matching_logic_id: matching_logic.jiomart.oms_settlement_3way
  tolerance: numeric tolerance not documented unless source SQL provides threshold; keep variance outputs diagnostic.
  timing_window: Use date filters in source SQL and mandatory filters; settlement/OMS date range gaps are caveats.
  mismatch_categories:
  - mismatch_category.jiomart.not_in_settlement
  - mismatch_category.jiomart.tcs_variance
  evidence_refs:
  - ev.jiomart.marketplace.7_1_oms_settlement_match_3_way_per_order
  confidence: high
  review_status: ready
```


```yaml
candidate_card:
  card_type: reconciliation_profile
  card_id: reconciliation_profile.jiomart.returns_oms_settlement_chain
  display_name: JioMart Returns → OMS → Settlement full-chain reconciliation
  process_id: business_process.jiomart.rto_flow
  reconciliation_family: returns_to_oms_to_settlement
  expected_side: reconciliation_side.jiomart.returns_chain.expected_returns
  actual_side: reconciliation_side.jiomart.returns_chain.actual_oms_settlement
  unit_id: reconciliation_unit.jiomart.order_id
  matching_logic_id: matching_logic.jiomart.returns_chain
  tolerance: numeric tolerance not documented unless source SQL provides threshold; keep variance outputs diagnostic.
  timing_window: Use date filters in source SQL and mandatory filters; settlement/OMS date range gaps are caveats.
  mismatch_categories:
  - mismatch_category.jiomart.return_value_variance
  - mismatch_category.jiomart.return_missing_oms_or_settlement
  evidence_refs:
  - ev.jiomart.marketplace.7_2_returns_oms_settlement_full_chain
  confidence: high
  review_status: ready
```


```yaml
candidate_card:
  card_type: reconciliation_profile
  card_id: reconciliation_profile.jiomart.unreconciled_oms_orders
  display_name: JioMart unreconciled OMS orders not found in settlement
  process_id: business_process.jiomart.forward_order_flow
  reconciliation_family: missing_settlement_detection
  expected_side: reconciliation_side.jiomart.unreconciled.expected_oms
  actual_side: reconciliation_side.jiomart.unreconciled.actual_settlement
  unit_id: reconciliation_unit.jiomart.order_id
  matching_logic_id: matching_logic.jiomart.unreconciled_oms
  tolerance: numeric tolerance not documented unless source SQL provides threshold; keep variance outputs diagnostic.
  timing_window: Use date filters in source SQL and mandatory filters; settlement/OMS date range gaps are caveats.
  mismatch_categories:
  - mismatch_category.jiomart.not_in_settlement
  evidence_refs:
  - ev.jiomart.marketplace.7_3_unreconciled_oms_orders_not_in_settlement
  confidence: high
  review_status: ready
```


```yaml
candidate_card:
  card_type: reconciliation_profile
  card_id: reconciliation_profile.jiomart.tcs_reconciliation
  display_name: JioMart TCS reconciliation across OMS and settlement BaseTcs rows
  process_id: business_process.jiomart.settlement_event_model
  reconciliation_family: tax_reconciliation
  expected_side: reconciliation_side.jiomart.tcs.expected_oms
  actual_side: reconciliation_side.jiomart.tcs.actual_settlement
  unit_id: reconciliation_unit.jiomart.period_or_order
  matching_logic_id: matching_logic.jiomart.tcs_reconciliation
  tolerance: numeric tolerance not documented unless source SQL provides threshold; keep variance outputs diagnostic.
  timing_window: Use date filters in source SQL and mandatory filters; settlement/OMS date range gaps are caveats.
  mismatch_categories:
  - mismatch_category.jiomart.tcs_variance
  - mismatch_category.jiomart.tcs_rate_anomaly
  evidence_refs:
  - ev.jiomart.marketplace.7_4_tcs_reconciliation
  confidence: high
  review_status: ready
```


```yaml
candidate_card:
  card_type: reconciliation_profile
  card_id: reconciliation_profile.jiomart.returns_oms_reconciliation
  display_name: JioMart Returns → OMS reconciliation
  process_id: business_process.jiomart.rto_flow
  reconciliation_family: returns_to_oms
  expected_side: reconciliation_side.jiomart.returns_oms.expected_returns
  actual_side: reconciliation_side.jiomart.returns_oms.actual_oms
  unit_id: reconciliation_unit.jiomart.order_id
  matching_logic_id: matching_logic.jiomart.returns_oms
  tolerance: numeric tolerance not documented unless source SQL provides threshold; keep variance outputs diagnostic.
  timing_window: Use date filters in source SQL and mandatory filters; settlement/OMS date range gaps are caveats.
  mismatch_categories:
  - mismatch_category.jiomart.return_missing_oms_or_settlement
  evidence_refs:
  - ev.jiomart.returns.7_3_returns_oms_reconciliation
  confidence: high
  review_status: ready
```

### 4.14 `reconciliation_side` cards


```yaml
candidate_card:
  card_type: reconciliation_side
  card_id: reconciliation_side.jiomart.oms_settlement.expected_oms
  display_name: expected oms
  profile_id: reconciliation_profile.jiomart.oms_settlement_3way
  side_role: expected
  source_table_id: table.zs_observe.jiomart_oms
  key_columns:
  - order_id
  amount_columns:
  - charged_amount
  - total_tcs_amount
  - total_tds
  filters:
  - is_active = true
  - transaction_type = forward
  - order_status = delivered
  - hsn IS NOT NULL
  grain: order_id unless SQL specifies aggregate period
  evidence_refs:
  - ev.jiomart.marketplace.7_1_oms_settlement_match_3_way_per_order
  confidence: high
  review_status: ready
```


```yaml
candidate_card:
  card_type: reconciliation_side
  card_id: reconciliation_side.jiomart.oms_settlement.actual_settlement
  display_name: actual settlement
  profile_id: reconciliation_profile.jiomart.oms_settlement_3way
  side_role: actual
  source_table_id: table.zs_observe.jiomart_settlement
  key_columns:
  - order_id
  amount_columns:
  - settled_amount by Receivable/BaseTcs/Tds
  filters:
  - is_active = true
  - event IS NOT NULL
  grain: order_id unless SQL specifies aggregate period
  evidence_refs:
  - ev.jiomart.marketplace.7_1_oms_settlement_match_3_way_per_order
  confidence: high
  review_status: ready
```


```yaml
candidate_card:
  card_type: reconciliation_side
  card_id: reconciliation_side.jiomart.returns_chain.expected_returns
  display_name: expected returns
  profile_id: reconciliation_profile.jiomart.returns_oms_settlement_chain
  side_role: expected
  source_table_id: table.zs_observe.jiomart_returns
  key_columns:
  - order_id
  amount_columns:
  - refund_amount
  - charged_amount
  filters:
  - is_active = true
  - return_type IS NOT NULL
  grain: order_id unless SQL specifies aggregate period
  evidence_refs:
  - ev.jiomart.marketplace.7_2_returns_oms_settlement_full_chain
  confidence: high
  review_status: ready
```


```yaml
candidate_card:
  card_type: reconciliation_side
  card_id: reconciliation_side.jiomart.returns_chain.actual_oms_settlement
  display_name: actual oms settlement
  profile_id: reconciliation_profile.jiomart.returns_oms_settlement_chain
  side_role: actual
  source_table_id: table.zs_observe.jiomart_oms
  key_columns:
  - order_id
  amount_columns:
  - charged_amount
  filters:
  - is_active = true
  grain: order_id unless SQL specifies aggregate period
  evidence_refs:
  - ev.jiomart.marketplace.7_2_returns_oms_settlement_full_chain
  confidence: high
  review_status: ready
```


```yaml
candidate_card:
  card_type: reconciliation_side
  card_id: reconciliation_side.jiomart.unreconciled.expected_oms
  display_name: expected oms
  profile_id: reconciliation_profile.jiomart.unreconciled_oms_orders
  side_role: expected
  source_table_id: table.zs_observe.jiomart_oms
  key_columns:
  - order_id
  amount_columns:
  - charged_amount
  filters:
  - is_active = true
  - transaction_type = forward
  - order_status = delivered
  - hsn IS NOT NULL
  grain: order_id unless SQL specifies aggregate period
  evidence_refs:
  - ev.jiomart.marketplace.7_3_unreconciled_oms_orders_not_in_settlement
  confidence: high
  review_status: ready
```


```yaml
candidate_card:
  card_type: reconciliation_side
  card_id: reconciliation_side.jiomart.unreconciled.actual_settlement
  display_name: actual settlement
  profile_id: reconciliation_profile.jiomart.unreconciled_oms_orders
  side_role: actual
  source_table_id: table.zs_observe.jiomart_settlement
  key_columns:
  - order_id
  amount_columns:
  - settled_amount
  filters:
  - is_active = true
  grain: order_id unless SQL specifies aggregate period
  evidence_refs:
  - ev.jiomart.marketplace.7_3_unreconciled_oms_orders_not_in_settlement
  confidence: high
  review_status: ready
```


```yaml
candidate_card:
  card_type: reconciliation_side
  card_id: reconciliation_side.jiomart.tcs.expected_oms
  display_name: expected oms
  profile_id: reconciliation_profile.jiomart.tcs_reconciliation
  side_role: expected
  source_table_id: table.zs_observe.jiomart_oms
  key_columns:
  - order_id
  amount_columns:
  - total_tcs_amount
  filters:
  - is_active = true
  - transaction_type = forward
  grain: order_id unless SQL specifies aggregate period
  evidence_refs:
  - ev.jiomart.marketplace.7_4_tcs_reconciliation
  confidence: high
  review_status: ready
```


```yaml
candidate_card:
  card_type: reconciliation_side
  card_id: reconciliation_side.jiomart.tcs.actual_settlement
  display_name: actual settlement
  profile_id: reconciliation_profile.jiomart.tcs_reconciliation
  side_role: actual
  source_table_id: table.zs_observe.jiomart_settlement
  key_columns:
  - order_id
  amount_columns:
  - settled_amount where accountable_type = BaseTcs
  filters:
  - is_active = true
  - accountable_type = BaseTcs
  grain: order_id unless SQL specifies aggregate period
  evidence_refs:
  - ev.jiomart.marketplace.7_4_tcs_reconciliation
  confidence: high
  review_status: ready
```


```yaml
candidate_card:
  card_type: reconciliation_side
  card_id: reconciliation_side.jiomart.returns_oms.expected_returns
  display_name: expected returns
  profile_id: reconciliation_profile.jiomart.returns_oms_reconciliation
  side_role: expected
  source_table_id: table.zs_observe.jiomart_returns
  key_columns:
  - order_id
  amount_columns:
  - refund_amount
  filters:
  - is_active = true
  - return_type IS NOT NULL
  grain: order_id unless SQL specifies aggregate period
  evidence_refs:
  - ev.jiomart.returns.7_3_returns_oms_reconciliation
  confidence: high
  review_status: ready
```


```yaml
candidate_card:
  card_type: reconciliation_side
  card_id: reconciliation_side.jiomart.returns_oms.actual_oms
  display_name: actual oms
  profile_id: reconciliation_profile.jiomart.returns_oms_reconciliation
  side_role: actual
  source_table_id: table.zs_observe.jiomart_oms
  key_columns:
  - order_id
  amount_columns:
  - charged_amount
  filters:
  - is_active = true
  grain: order_id unless SQL specifies aggregate period
  evidence_refs:
  - ev.jiomart.returns.7_3_returns_oms_reconciliation
  confidence: high
  review_status: ready
```

### 4.15 `reconciliation_unit` cards


```yaml
candidate_card:
  card_type: reconciliation_unit
  card_id: reconciliation_unit.jiomart.order_id
  display_name: JioMart order_id reconciliation unit
  unit_type: order
  unit_keys:
  - order_id
  grain: order_id
  aggregation_rule: Aggregate many-side settlement rows by order_id before comparison.
  evidence_refs:
  - ev.jiomart.marketplace.4_2_primary_join_keys
  confidence: high
  review_status: ready
```


```yaml
candidate_card:
  card_type: reconciliation_unit
  card_id: reconciliation_unit.jiomart.period_or_order
  display_name: JioMart period/order tax reconciliation unit
  unit_type: period_or_order
  unit_keys:
  - order_id
  - settlement_date or month
  grain: order_id + settlement_date or month
  aggregation_rule: TCS can be compared by order or aggregate period depending on source query.
  evidence_refs:
  - ev.jiomart.marketplace.7_4_tcs_reconciliation
  confidence: high
  review_status: ready
```

### 4.16 `matching_logic` cards


```yaml
candidate_card:
  card_type: matching_logic
  card_id: matching_logic.jiomart.oms_settlement_3way
  display_name: JioMart OMS → Settlement 3-way per-order reconciliation matching logic
  match_type: left_join_or_aggregate_compare_as_source_sql
  join_condition: Join on order_id; aggregate settlement rows where source uses SUM by accountable_type.
  key_normalization: No normalization beyond source key selection; never join jiomart_shipment to group 26 tables.
  amount_comparison: Compare source SQL amount aliases; keep variance/status outputs where present.
  aggregation_order: Aggregate settlement rows by order_id/accountable_type before joining to OMS or returns.
  tolerance_rule: Review required for hard numeric thresholds unless source SQL explicitly defines threshold.
  evidence_refs:
  - ev.jiomart.marketplace.7_1_oms_settlement_match_3_way_per_order
  confidence: high
  review_status: ready
```


```yaml
candidate_card:
  card_type: matching_logic
  card_id: matching_logic.jiomart.returns_chain
  display_name: JioMart Returns → OMS → Settlement full-chain reconciliation matching logic
  match_type: left_join_or_aggregate_compare_as_source_sql
  join_condition: Join on order_id; aggregate settlement rows where source uses SUM by accountable_type.
  key_normalization: No normalization beyond source key selection; never join jiomart_shipment to group 26 tables.
  amount_comparison: Compare source SQL amount aliases; keep variance/status outputs where present.
  aggregation_order: Aggregate settlement rows by order_id/accountable_type before joining to OMS or returns.
  tolerance_rule: Review required for hard numeric thresholds unless source SQL explicitly defines threshold.
  evidence_refs:
  - ev.jiomart.marketplace.7_2_returns_oms_settlement_full_chain
  confidence: high
  review_status: ready
```


```yaml
candidate_card:
  card_type: matching_logic
  card_id: matching_logic.jiomart.unreconciled_oms
  display_name: JioMart unreconciled OMS orders not found in settlement matching logic
  match_type: left_join_or_aggregate_compare_as_source_sql
  join_condition: Join on order_id; aggregate settlement rows where source uses SUM by accountable_type.
  key_normalization: No normalization beyond source key selection; never join jiomart_shipment to group 26 tables.
  amount_comparison: Compare source SQL amount aliases; keep variance/status outputs where present.
  aggregation_order: Aggregate settlement rows by order_id/accountable_type before joining to OMS or returns.
  tolerance_rule: Review required for hard numeric thresholds unless source SQL explicitly defines threshold.
  evidence_refs:
  - ev.jiomart.marketplace.7_3_unreconciled_oms_orders_not_in_settlement
  confidence: high
  review_status: ready
```


```yaml
candidate_card:
  card_type: matching_logic
  card_id: matching_logic.jiomart.tcs_reconciliation
  display_name: JioMart TCS reconciliation across OMS and settlement BaseTcs rows matching logic
  match_type: left_join_or_aggregate_compare_as_source_sql
  join_condition: Join on order_id; aggregate settlement rows where source uses SUM by accountable_type.
  key_normalization: No normalization beyond source key selection; never join jiomart_shipment to group 26 tables.
  amount_comparison: Compare source SQL amount aliases; keep variance/status outputs where present.
  aggregation_order: Aggregate settlement rows by order_id/accountable_type before joining to OMS or returns.
  tolerance_rule: Review required for hard numeric thresholds unless source SQL explicitly defines threshold.
  evidence_refs:
  - ev.jiomart.marketplace.7_4_tcs_reconciliation
  confidence: high
  review_status: ready
```


```yaml
candidate_card:
  card_type: matching_logic
  card_id: matching_logic.jiomart.returns_oms
  display_name: JioMart Returns → OMS reconciliation matching logic
  match_type: left_join_or_aggregate_compare_as_source_sql
  join_condition: Join on order_id; aggregate settlement rows where source uses SUM by accountable_type.
  key_normalization: No normalization beyond source key selection; never join jiomart_shipment to group 26 tables.
  amount_comparison: Compare source SQL amount aliases; keep variance/status outputs where present.
  aggregation_order: Aggregate settlement rows by order_id/accountable_type before joining to OMS or returns.
  tolerance_rule: Review required for hard numeric thresholds unless source SQL explicitly defines threshold.
  evidence_refs:
  - ev.jiomart.returns.7_3_returns_oms_reconciliation
  confidence: high
  review_status: ready
```

### 4.17 `mismatch_category` cards


```yaml
candidate_card:
  card_type: mismatch_category
  card_id: mismatch_category.jiomart.not_in_settlement
  display_name: Not in Settlement
  mismatch_type: not_in_settlement
  detection_logic: s.order_id IS NULL
  business_meaning: Forward delivered OMS order has no settlement row under source filters; documented coverage gap about
    944 orders / 1.6%.
  review_priority: medium
  evidence_refs:
  - ev.jiomart.marketplace.7_3_unreconciled_oms_orders_not_in_settlement
  confidence: high
  review_status: ready
```


```yaml
candidate_card:
  card_type: mismatch_category
  card_id: mismatch_category.jiomart.tcs_variance
  display_name: TCS variance
  mismatch_type: tcs_variance
  detection_logic: ROUND(o.total_tcs_amount + SUM(BaseTcs settled_amount), 4) != 0
  business_meaning: OMS TCS and settlement BaseTcs impact do not offset as expected.
  review_priority: medium
  evidence_refs:
  - ev.jiomart.marketplace.7_1_oms_settlement_match_3_way_per_order
  confidence: high
  review_status: ready
```


```yaml
candidate_card:
  card_type: mismatch_category
  card_id: mismatch_category.jiomart.return_value_variance
  display_name: Return value variance
  mismatch_type: return_value_variance
  detection_logic: ABS(CAST(r.refund_amount AS DOUBLE) - ABS(o.charged_amount)) requires runtime tolerance
  business_meaning: Return refund and OMS original sale differ; source does not define hard pass/fail threshold.
  review_priority: medium
  evidence_refs:
  - ev.jiomart.marketplace.7_2_returns_oms_settlement_full_chain
  confidence: high
  review_status: ready
```


```yaml
candidate_card:
  card_type: mismatch_category
  card_id: mismatch_category.jiomart.return_missing_oms_or_settlement
  display_name: Return missing OMS or settlement
  mismatch_type: return_missing_oms_or_settlement
  detection_logic: LEFT JOIN returns to OMS/settlement yields NULL joined side
  business_meaning: Return exists in returns table but lacks expected linked OMS or settlement detail.
  review_priority: medium
  evidence_refs:
  - ev.jiomart.marketplace.7_2_returns_oms_settlement_full_chain
  confidence: high
  review_status: ready
```


```yaml
candidate_card:
  card_type: mismatch_category
  card_id: mismatch_category.jiomart.tcs_rate_anomaly
  display_name: TCS rate anomaly
  mismatch_type: tcs_rate_anomaly
  detection_logic: tcs_igst_rate > 0.05
  business_meaning: Source documents tcs_igst_rate = 0.5 as likely data error; flag rows above 0.05.
  review_priority: medium
  evidence_refs:
  - ev.jiomart.oms.tcs_rates_observed
  confidence: high
  review_status: ready
```

### 4.18 `query_pattern` cards


```yaml
candidate_card:
  card_type: query_pattern
  card_id: query_pattern.jiomart.marketplace.6_1_total_gmv
  display_name: JioMart query — 6.1 Total GMV
  intent: metric_or_summary_query
  natural_language_patterns:
  - 6.1 Total GMV
  sql_ref: sql.jiomart.marketplace.6_1_total_gmv
  sql_template: |-
    SELECT
      SUM(CASE WHEN transaction_type = 'forward' THEN charged_amount ELSE 0 END) AS forward_gmv,
      SUM(CASE WHEN transaction_type = 'reverse' THEN ABS(charged_amount) ELSE 0 END) AS reversed_gmv,
      SUM(charged_amount) AS net_gmv
    FROM zs_observe.jiomart_oms
    WHERE is_active = true;
    -- Forward GMV: ~₹1.63 Cr | Reversed: ~₹22.4L | Net: ~₹1.40 Cr
  source_tables:
  - table.zs_observe.jiomart_oms
  required_filters: Use filters exactly as written in SQL plus applicable mandatory query filters.
  output_contract_id: output_contract.jiomart.metric_summary
  evidence_refs:
  - ev.jiomart.marketplace.6_1_total_gmv
  confidence: high
  review_status: ready
  primary_metric_id: metric.jiomart.total_gmv
```


```yaml
candidate_card:
  card_type: query_pattern
  card_id: query_pattern.jiomart.marketplace.6_2_return_rate
  display_name: JioMart query — 6.2 Return Rate
  intent: metric_or_summary_query
  natural_language_patterns:
  - 6.2 Return Rate
  sql_ref: sql.jiomart.marketplace.6_2_return_rate
  sql_template: |-
    SELECT
      ROUND(100.0 * COUNT_IF(order_status = 'shipment_returned')
        / NULLIF(COUNT_IF(transaction_type = 'forward'), 0), 2) AS rto_rate_pct,
      ROUND(100.0 * COUNT_IF(transaction_type = 'reverse')
        / NULLIF(COUNT_IF(transaction_type = 'forward'), 0), 2) AS return_reversal_pct
    FROM zs_observe.jiomart_oms
    WHERE is_active = true;
    -- RTO rate: ~14.8% | Return reversal rate: ~13.8%
  source_tables:
  - table.zs_observe.jiomart_oms
  required_filters: Use filters exactly as written in SQL plus applicable mandatory query filters.
  output_contract_id: output_contract.jiomart.metric_summary
  evidence_refs:
  - ev.jiomart.marketplace.6_2_return_rate
  confidence: high
  review_status: ready
  primary_metric_id: metric.jiomart.return_rate
```


```yaml
candidate_card:
  card_type: query_pattern
  card_id: query_pattern.jiomart.marketplace.6_3_average_order_value_aov
  display_name: JioMart query — 6.3 Average Order Value (AOV)
  intent: metric_or_summary_query
  natural_language_patterns:
  - 6.3 Average Order Value (AOV)
  sql_ref: sql.jiomart.marketplace.6_3_average_order_value_aov
  sql_template: |-
    SELECT AVG(charged_amount) AS aov
    FROM zs_observe.jiomart_oms
    WHERE is_active = true
      AND transaction_type = 'forward'
      AND order_status = 'delivered';
    -- Observed: ₹273.83
  source_tables:
  - table.zs_observe.jiomart_oms
  required_filters: Use filters exactly as written in SQL plus applicable mandatory query filters.
  output_contract_id: output_contract.jiomart.metric_summary
  evidence_refs:
  - ev.jiomart.marketplace.6_3_average_order_value_aov
  confidence: high
  review_status: ready
  primary_metric_id: metric.jiomart.average_order_value
```


```yaml
candidate_card:
  card_type: query_pattern
  card_id: query_pattern.jiomart.marketplace.6_4_net_settled_revenue
  display_name: JioMart query — 6.4 Net Settled Revenue
  intent: metric_or_summary_query
  natural_language_patterns:
  - 6.4 Net Settled Revenue
  sql_ref: sql.jiomart.marketplace.6_4_net_settled_revenue
  sql_template: |-
    SELECT
      SUM(CASE WHEN accountable_type = 'Receivable' THEN settled_amount ELSE 0 END) AS gross_receivable,
      SUM(CASE WHEN accountable_type = 'BaseTcs' THEN settled_amount ELSE 0 END) AS tcs_net,
      SUM(CASE WHEN accountable_type = 'Tds' THEN settled_amount ELSE 0 END) AS tds_net,
      SUM(settled_amount) AS net_settled
    FROM zs_observe.jiomart_settlement
    WHERE is_active = true AND event IS NOT NULL;
  source_tables:
  - table.zs_observe.jiomart_settlement
  required_filters: Use filters exactly as written in SQL plus applicable mandatory query filters.
  output_contract_id: output_contract.jiomart.metric_summary
  evidence_refs:
  - ev.jiomart.marketplace.6_4_net_settled_revenue
  confidence: high
  review_status: ready
  primary_metric_id: metric.jiomart.net_settled_revenue
```


```yaml
candidate_card:
  card_type: query_pattern
  card_id: query_pattern.jiomart.marketplace.6_5_seller_coupon_discount_impact
  display_name: JioMart query — 6.5 Seller Coupon Discount Impact
  intent: metric_or_summary_query
  natural_language_patterns:
  - 6.5 Seller Coupon Discount Impact
  sql_ref: sql.jiomart.marketplace.6_5_seller_coupon_discount_impact
  sql_template: |-
    SELECT
      seller_coupon_code,
      COUNT(*) AS orders,
      SUM(ABS(COALESCE(CAST(seller_coupon_amount AS DOUBLE), 0))) AS total_discount
    FROM zs_observe.jiomart_oms
    WHERE is_active = true
      AND seller_coupon_code IS NOT NULL
    GROUP BY seller_coupon_code
    ORDER BY total_discount DESC;
  source_tables:
  - table.zs_observe.jiomart_oms
  required_filters: Use filters exactly as written in SQL plus applicable mandatory query filters.
  output_contract_id: output_contract.jiomart.metric_summary
  evidence_refs:
  - ev.jiomart.marketplace.6_5_seller_coupon_discount_impact
  confidence: high
  review_status: ready
  primary_metric_id: metric.jiomart.seller_coupon_discount_impact
```


```yaml
candidate_card:
  card_type: query_pattern
  card_id: query_pattern.jiomart.marketplace.6_6_monthly_forward_orders_and_gmv
  display_name: JioMart query — 6.6 Monthly Forward Orders and GMV
  intent: metric_or_summary_query
  natural_language_patterns:
  - 6.6 Monthly Forward Orders and GMV
  sql_ref: sql.jiomart.marketplace.6_6_monthly_forward_orders_and_gmv
  sql_template: |-
    SELECT
      CAST(DATE_TRUNC('month', CAST(created_date AS TIMESTAMP)) AS DATE) AS month,
      COUNT(*) AS orders,
      SUM(charged_amount) AS gmv,
      AVG(charged_amount) AS aov
    FROM zs_observe.jiomart_oms
    WHERE is_active = true AND transaction_type = 'forward'
    GROUP BY 1 ORDER BY 1;
  source_tables:
  - table.zs_observe.jiomart_oms
  required_filters: Use filters exactly as written in SQL plus applicable mandatory query filters.
  output_contract_id: output_contract.jiomart.time_series
  evidence_refs:
  - ev.jiomart.marketplace.6_6_monthly_forward_orders_and_gmv
  confidence: high
  review_status: ready
  primary_metric_id: metric.jiomart.monthly_forward_orders_gmv
```


```yaml
candidate_card:
  card_type: query_pattern
  card_id: query_pattern.jiomart.marketplace.7_1_oms_settlement_match_3_way_per_order
  display_name: JioMart query — 7.1 OMS → Settlement Match (3-Way Per Order)
  intent: reconciliation
  natural_language_patterns:
  - 7.1 OMS to Settlement Match (3-Way Per Order)
  sql_ref: sql.jiomart.marketplace.7_1_oms_settlement_match_3_way_per_order
  sql_template: |-
    SELECT
      o.order_id,
      o.charged_amount AS oms_gmv,
      o.total_tcs_amount AS oms_tcs,
      o.total_tds AS oms_tds,
      SUM(CASE WHEN s.accountable_type = 'Receivable' THEN s.settled_amount ELSE 0 END) AS stl_receivable,
      SUM(CASE WHEN s.accountable_type = 'BaseTcs' THEN s.settled_amount ELSE 0 END) AS stl_tcs,
      SUM(CASE WHEN s.accountable_type = 'Tds' THEN s.settled_amount ELSE 0 END) AS stl_tds,
      ROUND(o.total_tcs_amount + SUM(CASE WHEN s.accountable_type='BaseTcs' THEN s.settled_amount ELSE 0 END), 4) AS tcs_variance
    FROM zs_observe.jiomart_oms o
    LEFT JOIN zs_observe.jiomart_settlement s
      ON o.order_id = s.order_id AND s.is_active = true AND s.event IS NOT NULL
    WHERE o.is_active = true
      AND o.transaction_type = 'forward'
      AND o.order_status = 'delivered'
      AND o.hsn IS NOT NULL
    GROUP BY o.order_id, o.charged_amount, o.total_tcs_amount, o.total_tds;
  source_tables:
  - table.zs_observe.jiomart_oms
  - table.zs_observe.jiomart_settlement
  required_filters: Use filters exactly as written in SQL plus applicable mandatory query filters.
  output_contract_id: output_contract.jiomart.order_reconciliation
  evidence_refs:
  - ev.jiomart.marketplace.7_1_oms_settlement_match_3_way_per_order
  confidence: high
  review_status: ready
  reconciliation_profile_id: reconciliation_profile.jiomart.oms_settlement_3way
```


```yaml
candidate_card:
  card_type: query_pattern
  card_id: query_pattern.jiomart.marketplace.7_2_returns_oms_settlement_full_chain
  display_name: JioMart query — 7.2 Returns → OMS → Settlement Full Chain
  intent: reconciliation
  natural_language_patterns:
  - 7.2 Returns to OMS to Settlement Full Chain
  sql_ref: sql.jiomart.marketplace.7_2_returns_oms_settlement_full_chain
  sql_template: |-
    SELECT
      r.order_id,
      r.return_type,
      CAST(r.refund_amount AS DOUBLE) AS refund_issued,
      o.charged_amount AS original_sale,
      SUM(s.settled_amount) AS settlement_net
    FROM zs_observe.jiomart_returns r
    LEFT JOIN zs_observe.jiomart_oms o ON r.order_id = o.order_id AND o.is_active = true
    LEFT JOIN zs_observe.jiomart_settlement s ON r.order_id = s.order_id AND s.is_active = true
    WHERE r.is_active = true AND r.return_type IS NOT NULL
    GROUP BY r.order_id, r.return_type, r.refund_amount, o.charged_amount;
  source_tables:
  - table.zs_observe.jiomart_oms
  - table.zs_observe.jiomart_returns
  - table.zs_observe.jiomart_settlement
  required_filters: Use filters exactly as written in SQL plus applicable mandatory query filters.
  output_contract_id: output_contract.jiomart.return_reconciliation
  evidence_refs:
  - ev.jiomart.marketplace.7_2_returns_oms_settlement_full_chain
  confidence: high
  review_status: ready
  reconciliation_profile_id: reconciliation_profile.jiomart.oms_settlement_3way
```


```yaml
candidate_card:
  card_type: query_pattern
  card_id: query_pattern.jiomart.marketplace.7_3_unreconciled_oms_orders_not_in_settlement
  display_name: JioMart query — 7.3 Unreconciled OMS Orders (Not in Settlement)
  intent: reconciliation
  natural_language_patterns:
  - 7.3 Unreconciled OMS Orders (Not in Settlement)
  sql_ref: sql.jiomart.marketplace.7_3_unreconciled_oms_orders_not_in_settlement
  sql_template: |-
    SELECT o.order_id, o.invoice_number, o.charged_amount, o.order_status
    FROM zs_observe.jiomart_oms o
    LEFT JOIN zs_observe.jiomart_settlement s
      ON o.order_id = s.order_id AND s.is_active = true
    WHERE o.is_active = true
      AND o.transaction_type = 'forward'
      AND o.order_status = 'delivered'
      AND o.hsn IS NOT NULL
      AND s.order_id IS NULL;
    -- Coverage gap: ~944 orders (1.6%)
  source_tables:
  - table.zs_observe.jiomart_oms
  - table.zs_observe.jiomart_settlement
  required_filters: Use filters exactly as written in SQL plus applicable mandatory query filters.
  output_contract_id: output_contract.jiomart.order_reconciliation
  evidence_refs:
  - ev.jiomart.marketplace.7_3_unreconciled_oms_orders_not_in_settlement
  confidence: high
  review_status: ready
  reconciliation_profile_id: reconciliation_profile.jiomart.oms_settlement_3way
```


```yaml
candidate_card:
  card_type: query_pattern
  card_id: query_pattern.jiomart.marketplace.7_4_tcs_reconciliation
  display_name: JioMart query — 7.4 TCS Reconciliation
  intent: reconciliation
  natural_language_patterns:
  - 7.4 TCS Reconciliation
  sql_ref: sql.jiomart.marketplace.7_4_tcs_reconciliation
  sql_template: |-
    SELECT 'OMS TCS' AS source, SUM(total_tcs_amount) AS amount
    FROM zs_observe.jiomart_oms WHERE is_active = true AND transaction_type = 'forward'
    UNION ALL
    SELECT 'Settlement BaseTcs (Forward)', SUM(settled_amount)
    FROM zs_observe.jiomart_settlement
    WHERE is_active = true AND accountable_type = 'BaseTcs' AND transaction_type = 'forward'
    UNION ALL
    SELECT 'Settlement BaseTcs (Return Reversal)', SUM(settled_amount)
    FROM zs_observe.jiomart_settlement
    WHERE is_active = true AND accountable_type = 'BaseTcs' AND transaction_type = 'reverse';
  source_tables:
  - table.zs_observe.jiomart_oms
  - table.zs_observe.jiomart_settlement
  required_filters: Use filters exactly as written in SQL plus applicable mandatory query filters.
  output_contract_id: output_contract.jiomart.order_reconciliation
  evidence_refs:
  - ev.jiomart.marketplace.7_4_tcs_reconciliation
  confidence: high
  review_status: ready
  primary_metric_id: metric.jiomart.tcs_deducted
  reconciliation_profile_id: reconciliation_profile.jiomart.tcs_reconciliation
```


```yaml
candidate_card:
  card_type: query_pattern
  card_id: query_pattern.jiomart.marketplace.9_mandatory_query_filters
  display_name: JioMart query — 9. Mandatory Query Filters
  intent: metric_or_summary_query
  natural_language_patterns:
  - 9. Mandatory Query Filters
  sql_ref: sql.jiomart.marketplace.9_mandatory_query_filters
  sql_template: |-
    -- jiomart_oms, jiomart_returns, jiomart_settlement (group 26 — MYFITNESS)
    WHERE is_active = true
      AND group_level_id = 26
    -- jiomart_oms — additional filter for clean rows
      AND hsn IS NOT NULL   -- removes column-shifted older rows
    -- jiomart_shipment (group 221 — ARDEUR FASHIONS)
    WHERE is_active = true
      AND group_level_id = 221
      AND qty > 0   -- removes cancelled orders
  source_tables: []
  required_filters: Use filters exactly as written in SQL plus applicable mandatory query filters.
  output_contract_id: output_contract.jiomart.metric_summary
  evidence_refs:
  - ev.jiomart.marketplace.9_mandatory_query_filters
  confidence: high
  review_status: ready
```


```yaml
candidate_card:
  card_type: query_pattern
  card_id: query_pattern.jiomart.shipment.7_1_shipment_status_summary
  display_name: JioMart query — 7.1 Shipment Status Summary
  intent: metric_or_summary_query
  natural_language_patterns:
  - 7.1 Shipment Status Summary
  sql_ref: sql.jiomart.shipment.7_1_shipment_status_summary
  sql_template: |-
    SELECT order_status,
      COUNT(*) AS cnt,
      SUM(charged_amount) AS gmv,
      SUM(mrp) AS total_mrp,
      SUM(item_promo_discount) AS total_discount,
      AVG(charged_amount) AS avg_selling_price,
      ROUND(100.0 * AVG(item_promo_discount) / NULLIF(AVG(mrp), 0), 2) AS avg_discount_pct
    FROM zs_observe.jiomart_shipment
    WHERE is_active = true
    GROUP BY order_status;
  source_tables:
  - table.zs_observe.jiomart_shipment
  required_filters: Use filters exactly as written in SQL plus applicable mandatory query filters.
  output_contract_id: output_contract.jiomart.shipment_summary
  evidence_refs:
  - ev.jiomart.shipment.7_1_shipment_status_summary
  confidence: high
  review_status: ready
  primary_metric_id: metric.jiomart.shipment_status_gmv
```


```yaml
candidate_card:
  card_type: query_pattern
  card_id: query_pattern.jiomart.shipment.7_2_monthly_gmv
  display_name: JioMart query — 7.2 Monthly GMV
  intent: metric_or_summary_query
  natural_language_patterns:
  - 7.2 Monthly GMV
  sql_ref: sql.jiomart.shipment.7_2_monthly_gmv
  sql_template: |-
    SELECT
      CAST(DATE_TRUNC('month', CAST(created_date AS TIMESTAMP)) AS DATE) AS month,
      COUNT(*) AS shipments,
      SUM(charged_amount) AS gmv,
      SUM(item_promo_discount) AS promo_discount
    FROM zs_observe.jiomart_shipment
    WHERE is_active = true AND qty > 0
    GROUP BY 1 ORDER BY 1;
  source_tables:
  - table.zs_observe.jiomart_shipment
  required_filters: Use filters exactly as written in SQL plus applicable mandatory query filters.
  output_contract_id: output_contract.jiomart.time_series
  evidence_refs:
  - ev.jiomart.shipment.7_2_monthly_gmv
  confidence: high
  review_status: ready
  primary_metric_id: metric.jiomart.shipment_monthly_gmv
```


```yaml
candidate_card:
  card_type: query_pattern
  card_id: query_pattern.jiomart.shipment.7_3_top_skus
  display_name: JioMart query — 7.3 Top SKUs
  intent: metric_or_summary_query
  natural_language_patterns:
  - 7.3 Top SKUs
  sql_ref: sql.jiomart.shipment.7_3_top_skus
  sql_template: |-
    SELECT sku_id,
      COUNT(*) AS orders,
      SUM(charged_amount) AS gmv,
      AVG(charged_amount) AS avg_price,
      AVG(item_promo_discount) AS avg_discount
    FROM zs_observe.jiomart_shipment
    WHERE is_active = true AND qty > 0
    GROUP BY sku_id
    ORDER BY gmv DESC
    LIMIT 20;
  source_tables:
  - table.zs_observe.jiomart_shipment
  required_filters: Use filters exactly as written in SQL plus applicable mandatory query filters.
  output_contract_id: output_contract.jiomart.sku_summary
  evidence_refs:
  - ev.jiomart.shipment.7_3_top_skus
  confidence: high
  review_status: ready
  primary_metric_id: metric.jiomart.top_shipment_skus
```


```yaml
candidate_card:
  card_type: query_pattern
  card_id: query_pattern.jiomart.settlement.8_1_net_settlement_per_order_structured_rows
  display_name: JioMart query — 8.1 Net Settlement per Order (Structured Rows)
  intent: metric_or_summary_query
  natural_language_patterns:
  - 8.1 Net Settlement per Order (Structured Rows)
  sql_ref: sql.jiomart.settlement.8_1_net_settlement_per_order_structured_rows
  sql_template: |-
    SELECT
      order_id,
      SUM(CASE WHEN accountable_type = 'Receivable' THEN settled_amount ELSE 0 END) AS sale_proceeds,
      SUM(CASE WHEN accountable_type = 'BaseTcs' THEN settled_amount ELSE 0 END) AS tcs_impact,
      SUM(CASE WHEN accountable_type = 'Tds' THEN settled_amount ELSE 0 END) AS tds_impact,
      SUM(settled_amount) AS net_settled
    FROM zs_observe.jiomart_settlement
    WHERE is_active = true AND event IS NOT NULL
    GROUP BY order_id
    ORDER BY net_settled DESC
    LIMIT 20;
  source_tables:
  - table.zs_observe.jiomart_settlement
  required_filters: Use filters exactly as written in SQL plus applicable mandatory query filters.
  output_contract_id: output_contract.jiomart.metric_summary
  evidence_refs:
  - ev.jiomart.settlement.8_1_net_settlement_per_order_structured_rows
  confidence: high
  review_status: ready
  primary_metric_id: metric.jiomart.net_settlement_per_order
```


```yaml
candidate_card:
  card_type: query_pattern
  card_id: query_pattern.jiomart.settlement.8_2_monthly_settlement_summary
  display_name: JioMart query — 8.2 Monthly Settlement Summary
  intent: metric_or_summary_query
  natural_language_patterns:
  - 8.2 Monthly Settlement Summary
  sql_ref: sql.jiomart.settlement.8_2_monthly_settlement_summary
  sql_template: |-
    SELECT
      DATE_TRUNC('month', settlement_date) AS month,
      transaction_type,
      accountable_type,
      COUNT(*) AS rows,
      SUM(settled_amount) AS total_settled
    FROM zs_observe.jiomart_settlement
    WHERE is_active = true AND event IS NOT NULL
    GROUP BY 1, 2, 3
    ORDER BY 1, 2, 3;
  source_tables:
  - table.zs_observe.jiomart_settlement
  required_filters: Use filters exactly as written in SQL plus applicable mandatory query filters.
  output_contract_id: output_contract.jiomart.time_series
  evidence_refs:
  - ev.jiomart.settlement.8_2_monthly_settlement_summary
  confidence: high
  review_status: ready
  primary_metric_id: metric.jiomart.monthly_settlement_summary
```


```yaml
candidate_card:
  card_type: query_pattern
  card_id: query_pattern.jiomart.settlement.8_3_settlement_oms_reconciliation
  display_name: JioMart query — 8.3 Settlement ↔ OMS Reconciliation
  intent: reconciliation
  natural_language_patterns:
  - 8.3 Settlement to OMS Reconciliation
  sql_ref: sql.jiomart.settlement.8_3_settlement_oms_reconciliation
  sql_template: |-
    SELECT
      o.order_id,
      o.charged_amount AS oms_gmv,
      o.total_tcs_amount AS oms_tcs,
      o.total_tds AS oms_tds,
      SUM(CASE WHEN s.accountable_type = 'Receivable' THEN s.settled_amount ELSE 0 END) AS settled_receivable,
      SUM(CASE WHEN s.accountable_type = 'BaseTcs' THEN s.settled_amount ELSE 0 END) AS settled_tcs,
      SUM(CASE WHEN s.accountable_type = 'Tds' THEN s.settled_amount ELSE 0 END) AS settled_tds,
      CASE WHEN SUM(s.settled_amount) IS NULL THEN 'Not in Settlement' ELSE 'Matched' END AS status
    FROM zs_observe.jiomart_oms o
    LEFT JOIN zs_observe.jiomart_settlement s
      ON o.order_id = s.order_id
      AND s.is_active = true
      AND s.event IS NOT NULL
    WHERE o.is_active = true
      AND o.transaction_type = 'forward'
      AND o.order_status = 'delivered'
      AND o.hsn IS NOT NULL
    GROUP BY o.order_id, o.charged_amount, o.total_tcs_amount, o.total_tds;
  source_tables:
  - table.zs_observe.jiomart_oms
  - table.zs_observe.jiomart_settlement
  required_filters: Use filters exactly as written in SQL plus applicable mandatory query filters.
  output_contract_id: output_contract.jiomart.order_reconciliation
  evidence_refs:
  - ev.jiomart.settlement.8_3_settlement_oms_reconciliation
  confidence: high
  review_status: ready
  reconciliation_profile_id: reconciliation_profile.jiomart.oms_settlement_3way
```


```yaml
candidate_card:
  card_type: query_pattern
  card_id: query_pattern.jiomart.settlement.8_4_tcs_reconciliation_oms_vs_settlement
  display_name: JioMart query — 8.4 TCS Reconciliation (OMS vs Settlement)
  intent: reconciliation
  natural_language_patterns:
  - 8.4 TCS Reconciliation (OMS vs Settlement)
  sql_ref: sql.jiomart.settlement.8_4_tcs_reconciliation_oms_vs_settlement
  sql_template: |-
    SELECT
      'OMS TCS' AS source, SUM(total_tcs_amount) AS total
    FROM zs_observe.jiomart_oms WHERE is_active = true AND transaction_type = 'forward'
    UNION ALL
    SELECT 'Settlement BaseTcs', SUM(settled_amount)
    FROM zs_observe.jiomart_settlement
    WHERE is_active = true AND accountable_type = 'BaseTcs' AND transaction_type = 'forward';
  source_tables:
  - table.zs_observe.jiomart_oms
  - table.zs_observe.jiomart_settlement
  required_filters: Use filters exactly as written in SQL plus applicable mandatory query filters.
  output_contract_id: output_contract.jiomart.order_reconciliation
  evidence_refs:
  - ev.jiomart.settlement.8_4_tcs_reconciliation_oms_vs_settlement
  confidence: high
  review_status: ready
  primary_metric_id: metric.jiomart.tcs_deducted
  reconciliation_profile_id: reconciliation_profile.jiomart.tcs_reconciliation
```


```yaml
candidate_card:
  card_type: query_pattern
  card_id: query_pattern.jiomart.settlement.8_5_credit_debit_notes
  display_name: JioMart query — 8.5 Credit / Debit Notes
  intent: metric_or_summary_query
  natural_language_patterns:
  - 8.5 Credit / Debit Notes
  sql_ref: sql.jiomart.settlement.8_5_credit_debit_notes
  sql_template: |-
    SELECT
      transaction_type, event, accountable_type,
      COUNT(*) AS cnt,
      SUM(settled_amount) AS total
    FROM zs_observe.jiomart_settlement
    WHERE is_active = true
      AND transaction_type IN ('Credit Note', 'Debit Note', 'Service Invoice', 'Bill Tds Refund')
    GROUP BY 1, 2, 3;
  source_tables:
  - table.zs_observe.jiomart_settlement
  required_filters: Use filters exactly as written in SQL plus applicable mandatory query filters.
  output_contract_id: output_contract.jiomart.settlement_event_summary
  evidence_refs:
  - ev.jiomart.settlement.8_5_credit_debit_notes
  confidence: high
  review_status: ready
  primary_metric_id: metric.jiomart.credit_debit_note_impact
```


```yaml
candidate_card:
  card_type: query_pattern
  card_id: query_pattern.jiomart.returns.7_1_return_volume_by_type
  display_name: JioMart query — 7.1 Return Volume by Type
  intent: metric_or_summary_query
  natural_language_patterns:
  - 7.1 Return Volume by Type
  sql_ref: sql.jiomart.returns.7_1_return_volume_by_type
  sql_template: |-
    SELECT
      COALESCE(return_type, 'Unknown/Old Format') AS return_type,
      return_status,
      COUNT(*) AS cnt,
      SUM(CAST(charged_amount AS DOUBLE)) AS total_charged,
      SUM(CAST(refund_amount AS DOUBLE)) AS total_refund
    FROM zs_observe.jiomart_returns
    WHERE is_active = true
    GROUP BY 1, 2
    ORDER BY cnt DESC;
  source_tables:
  - table.zs_observe.jiomart_returns
  required_filters: Use filters exactly as written in SQL plus applicable mandatory query filters.
  output_contract_id: output_contract.jiomart.metric_summary
  evidence_refs:
  - ev.jiomart.returns.7_1_return_volume_by_type
  confidence: high
  review_status: ready
  primary_metric_id: metric.jiomart.return_volume_by_type
```


```yaml
candidate_card:
  card_type: query_pattern
  card_id: query_pattern.jiomart.returns.7_2_return_cycle_time_rto_turnaround
  display_name: JioMart query — 7.2 Return Cycle Time (RTO Turnaround)
  intent: metric_or_summary_query
  natural_language_patterns:
  - 7.2 Return Cycle Time (RTO Turnaround)
  sql_ref: sql.jiomart.returns.7_2_return_cycle_time_rto_turnaround
  sql_template: |-
    SELECT
      courier_partner,
      COUNT(*) AS returns,
      AVG(DATE_DIFF('day',
        CAST(return_initiate_date AS TIMESTAMP),
        CAST(return_delivery_date AS TIMESTAMP))) AS avg_days_to_warehouse
    FROM zs_observe.jiomart_returns
    WHERE is_active = true
      AND return_type = 'ReturnToOrigin'
      AND return_initiate_date IS NOT NULL
      AND return_delivery_date IS NOT NULL
    GROUP BY courier_partner;
  source_tables:
  - table.zs_observe.jiomart_returns
  required_filters: Use filters exactly as written in SQL plus applicable mandatory query filters.
  output_contract_id: output_contract.jiomart.metric_summary
  evidence_refs:
  - ev.jiomart.returns.7_2_return_cycle_time_rto_turnaround
  confidence: high
  review_status: ready
  primary_metric_id: metric.jiomart.return_cycle_time
```


```yaml
candidate_card:
  card_type: query_pattern
  card_id: query_pattern.jiomart.returns.7_3_returns_oms_reconciliation
  display_name: JioMart query — 7.3 Returns → OMS Reconciliation
  intent: reconciliation
  natural_language_patterns:
  - 7.3 Returns to OMS Reconciliation
  sql_ref: sql.jiomart.returns.7_3_returns_oms_reconciliation
  sql_template: |-
    SELECT
      r.order_id, r.invoice_number,
      r.return_type,
      CAST(r.charged_amount AS DOUBLE) AS return_charged,
      CAST(r.refund_amount AS DOUBLE) AS refund,
      o.charged_amount AS oms_original_amount,
      o.order_status AS oms_status
    FROM zs_observe.jiomart_returns r
    LEFT JOIN zs_observe.jiomart_oms o
      ON r.order_id = o.order_id
      AND o.is_active = true
    WHERE r.is_active = true;
  source_tables:
  - table.zs_observe.jiomart_oms
  - table.zs_observe.jiomart_returns
  required_filters: Use filters exactly as written in SQL plus applicable mandatory query filters.
  output_contract_id: output_contract.jiomart.return_reconciliation
  evidence_refs:
  - ev.jiomart.returns.7_3_returns_oms_reconciliation
  confidence: high
  review_status: ready
```


```yaml
candidate_card:
  card_type: query_pattern
  card_id: query_pattern.jiomart.returns.7_4_sku_level_return_rate
  display_name: JioMart query — 7.4 SKU-Level Return Rate
  intent: metric_or_summary_query
  natural_language_patterns:
  - 7.4 SKU-Level Return Rate
  sql_ref: sql.jiomart.returns.7_4_sku_level_return_rate
  sql_template: |-
    SELECT
      r.sku_id,
      COUNT(*) AS returns,
      SUM(CAST(r.charged_amount AS DOUBLE)) AS returned_value
    FROM zs_observe.jiomart_returns r
    WHERE r.is_active = true
    GROUP BY r.sku_id
    ORDER BY returns DESC;
  source_tables:
  - table.zs_observe.jiomart_returns
  required_filters: Use filters exactly as written in SQL plus applicable mandatory query filters.
  output_contract_id: output_contract.jiomart.sku_summary
  evidence_refs:
  - ev.jiomart.returns.7_4_sku_level_return_rate
  confidence: high
  review_status: ready
  primary_metric_id: metric.jiomart.sku_return_rate
```


```yaml
candidate_card:
  card_type: query_pattern
  card_id: query_pattern.jiomart.oms.7_1_monthly_gmv_clean_rows_only
  display_name: JioMart query — 7.1 Monthly GMV (Clean Rows Only)
  intent: metric_or_summary_query
  natural_language_patterns:
  - 7.1 Monthly GMV (Clean Rows Only)
  sql_ref: sql.jiomart.oms.7_1_monthly_gmv_clean_rows_only
  sql_template: |-
    SELECT
      CAST(DATE_TRUNC('month', CAST(created_date AS TIMESTAMP)) AS DATE) AS month,
      transaction_type,
      COUNT(*) AS orders,
      SUM(charged_amount) AS gmv,
      SUM(total_tcs_amount) AS tcs,
      SUM(total_tds) AS tds
    FROM zs_observe.jiomart_oms
    WHERE is_active = true
    GROUP BY 1, 2
    ORDER BY 1, 2;
  source_tables:
  - table.zs_observe.jiomart_oms
  required_filters: Use filters exactly as written in SQL plus applicable mandatory query filters.
  output_contract_id: output_contract.jiomart.time_series
  evidence_refs:
  - ev.jiomart.oms.7_1_monthly_gmv_clean_rows_only
  confidence: high
  review_status: ready
  primary_metric_id: metric.jiomart.oms_monthly_gmv_clean
```


```yaml
candidate_card:
  card_type: query_pattern
  card_id: query_pattern.jiomart.oms.7_2_clean_forward_orders_exclude_column_shifted_rows
  display_name: JioMart query — 7.2 Clean Forward Orders (Exclude Column-Shifted Rows)
  intent: metric_or_summary_query
  natural_language_patterns:
  - 7.2 Clean Forward Orders (Exclude Column-Shifted Rows)
  sql_ref: sql.jiomart.oms.7_2_clean_forward_orders_exclude_column_shifted_rows
  sql_template: |-
    SELECT *
    FROM zs_observe.jiomart_oms
    WHERE is_active = true
      AND transaction_type = 'forward'
      AND order_status = 'delivered'
      AND hsn IS NOT NULL;
  source_tables:
  - table.zs_observe.jiomart_oms
  required_filters: Use filters exactly as written in SQL plus applicable mandatory query filters.
  output_contract_id: output_contract.jiomart.metric_summary
  evidence_refs:
  - ev.jiomart.oms.7_2_clean_forward_orders_exclude_column_shifted_rows
  confidence: high
  review_status: ready
```


```yaml
candidate_card:
  card_type: query_pattern
  card_id: query_pattern.jiomart.oms.7_3_intra_state_vs_inter_state_gst_analysis
  display_name: JioMart query — 7.3 Intra-State vs Inter-State GST Analysis
  intent: metric_or_summary_query
  natural_language_patterns:
  - 7.3 Intra-State vs Inter-State GST Analysis
  sql_ref: sql.jiomart.oms.7_3_intra_state_vs_inter_state_gst_analysis
  sql_template: |-
    SELECT
      CASE
        WHEN UPPER(source_state) = UPPER(destination_state) THEN 'Intra-State'
        ELSE 'Inter-State'
      END AS gst_type,
      COUNT(*) AS cnt,
      SUM(charged_amount) AS gmv,
      SUM(tax_igst_amount) AS igst,
      SUM(tax_cgst_amount + tax_sgst_amount) AS cgst_sgst
    FROM zs_observe.jiomart_oms
    WHERE is_active = true
      AND transaction_type = 'forward'
      AND hsn IS NOT NULL
    GROUP BY 1;
  source_tables:
  - table.zs_observe.jiomart_oms
  required_filters: Use filters exactly as written in SQL plus applicable mandatory query filters.
  output_contract_id: output_contract.jiomart.metric_summary
  evidence_refs:
  - ev.jiomart.oms.7_3_intra_state_vs_inter_state_gst_analysis
  confidence: high
  review_status: ready
  primary_metric_id: metric.jiomart.gst_breakdown
```


```yaml
candidate_card:
  card_type: query_pattern
  card_id: query_pattern.jiomart.oms.7_4_sku_level_performance
  display_name: JioMart query — 7.4 SKU-Level Performance
  intent: metric_or_summary_query
  natural_language_patterns:
  - 7.4 SKU-Level Performance
  sql_ref: sql.jiomart.oms.7_4_sku_level_performance
  sql_template: |-
    SELECT sku_id, mp_sin,
      COUNT(*) AS orders,
      SUM(charged_amount) AS gmv,
      AVG(charged_amount) AS avg_price,
      ROUND(100.0 * COUNT_IF(transaction_type = 'forward' AND order_status = 'shipment_returned')
        / NULLIF(COUNT_IF(transaction_type = 'forward'), 0), 2) AS rto_rate_pct
    FROM zs_observe.jiomart_oms
    WHERE is_active = true AND hsn IS NOT NULL
    GROUP BY sku_id, mp_sin
    ORDER BY gmv DESC;
  source_tables:
  - table.zs_observe.jiomart_oms
  required_filters: Use filters exactly as written in SQL plus applicable mandatory query filters.
  output_contract_id: output_contract.jiomart.sku_summary
  evidence_refs:
  - ev.jiomart.oms.7_4_sku_level_performance
  confidence: high
  review_status: ready
  primary_metric_id: metric.jiomart.oms_sku_performance
```


```yaml
candidate_card:
  card_type: query_pattern
  card_id: query_pattern.jiomart.oms.7_5_oms_settlement_join
  display_name: JioMart query — 7.5 OMS → Settlement Join
  intent: metric_or_summary_query
  natural_language_patterns:
  - 7.5 OMS to Settlement Join
  sql_ref: sql.jiomart.oms.7_5_oms_settlement_join
  sql_template: |-
    SELECT
      o.order_id, o.invoice_number,
      o.charged_amount AS oms_gmv,
      o.total_tcs_amount AS oms_tcs,
      s.settled_amount AS settlement_net,
      s.event, s.accountable_type
    FROM zs_observe.jiomart_oms o
    LEFT JOIN zs_observe.jiomart_settlement s
      ON o.order_id = s.order_id AND s.is_active = true
    WHERE o.is_active = true
      AND o.transaction_type = 'forward'
      AND o.order_status = 'delivered'
      AND o.hsn IS NOT NULL;
  source_tables:
  - table.zs_observe.jiomart_oms
  - table.zs_observe.jiomart_settlement
  required_filters: Use filters exactly as written in SQL plus applicable mandatory query filters.
  output_contract_id: output_contract.jiomart.metric_summary
  evidence_refs:
  - ev.jiomart.oms.7_5_oms_settlement_join
  confidence: high
  review_status: ready
  reconciliation_profile_id: reconciliation_profile.jiomart.oms_settlement_3way
```


```yaml
candidate_card:
  card_type: query_pattern
  card_id: query_pattern.jiomart.oms.7_6_return_rate
  display_name: JioMart query — 7.6 Return Rate
  intent: metric_or_summary_query
  natural_language_patterns:
  - 7.6 Return Rate
  sql_ref: sql.jiomart.oms.7_6_return_rate
  sql_template: |-
    SELECT
      ROUND(100.0 *
        COUNT_IF(order_status = 'shipment_returned')
        / NULLIF(COUNT_IF(transaction_type = 'forward'), 0), 2) AS rto_rate_pct,
      ROUND(100.0 *
        COUNT_IF(transaction_type = 'reverse')
        / NULLIF(COUNT_IF(transaction_type = 'forward'), 0), 2) AS return_reversal_rate_pct
    FROM zs_observe.jiomart_oms
    WHERE is_active = true;
  source_tables:
  - table.zs_observe.jiomart_oms
  required_filters: Use filters exactly as written in SQL plus applicable mandatory query filters.
  output_contract_id: output_contract.jiomart.metric_summary
  evidence_refs:
  - ev.jiomart.oms.7_6_return_rate
  confidence: high
  review_status: ready
```

### 4.19 `rule` cards


```yaml
candidate_card:
  card_type: rule
  card_id: rule.jiomart.scope_fields_are_columns
  display_name: Scope identifiers stay columns
  rule_type: scope_guardrail
  statement: |-
    group_level_id, seller/entity/GSTIN, seller code, GSTIN, warehouse, and courier values remain source columns, filters, caveats, or value profiles only; never emit tenant/group/account/logistics/statutory filing cards.
  applies_to_cards:
  - table.zs_observe.jiomart_oms
  - table.zs_observe.jiomart_settlement
  - table.zs_observe.jiomart_returns
  - table.zs_observe.jiomart_shipment
  severity: medium
  evidence_refs:
  - ev.jiomart.marketplace.1_3_seller_entities_in_dataset
  confidence: high
  review_status: ready
```


```yaml
candidate_card:
  card_type: rule
  card_id: rule.jiomart.mandatory_filters_group_26
  display_name: Mandatory group 26 filters
  rule_type: filter_rule
  statement: For jiomart_oms, jiomart_returns, and jiomart_settlement, apply is_active = true and group_level_id = 26 unless
    runtime scope explicitly overrides.
  applies_to_cards:
  - table.zs_observe.jiomart_oms
  - table.zs_observe.jiomart_settlement
  - table.zs_observe.jiomart_returns
  severity: high
  evidence_refs:
  - ev.jiomart.marketplace.9_mandatory_query_filters
  confidence: high
  review_status: ready
```


```yaml
candidate_card:
  card_type: rule
  card_id: rule.jiomart.mandatory_filters_group_221
  display_name: Mandatory shipment group 221 filters
  rule_type: filter_rule
  statement: For jiomart_shipment, apply is_active = true, group_level_id = 221, and qty > 0 for active shipment analysis.
  applies_to_cards:
  - table.zs_observe.jiomart_shipment
  severity: high
  evidence_refs:
  - ev.jiomart.marketplace.9_mandatory_query_filters
  confidence: high
  review_status: ready
```


```yaml
candidate_card:
  card_type: rule
  card_id: rule.jiomart.never_cross_join_shipment
  display_name: Never cross-join shipment to MYFITNESS tables
  rule_type: join_rule
  statement: jiomart_shipment is a separate ARDEUR FASHIONS entity with 0% order_id match to jiomart_oms; do not join it to
    OMS/returns/settlement without explicit external entity mapping.
  applies_to_cards:
  - table.zs_observe.jiomart_shipment
  - table.zs_observe.jiomart_oms
  severity: high
  evidence_refs:
  - ev.jiomart.marketplace.4_2_primary_join_keys
  confidence: high
  review_status: ready
```


```yaml
candidate_card:
  card_type: rule
  card_id: rule.jiomart.use_order_id_for_oms_settlement
  display_name: Use order_id for OMS-settlement joins
  rule_type: join_rule
  statement: Use jiomart_oms.order_id = jiomart_settlement.order_id. invoice_number has lower/format-different coverage and
    document_number is mostly NULL.
  applies_to_cards:
  - relationship.jiomart.oms_settlement.order_id
  severity: medium
  evidence_refs:
  - ev.jiomart.marketplace.4_2_primary_join_keys
  confidence: high
  review_status: ready
```


```yaml
candidate_card:
  card_type: rule
  card_id: rule.jiomart.aggregate_settlement_before_join
  display_name: Aggregate settlement rows before comparison
  rule_type: aggregation_rule
  statement: JioMart settlement is event-based and multi-row; group by order_id and accountable_type/event before comparing
    to OMS or returns.
  applies_to_cards:
  - table.zs_observe.jiomart_settlement
  severity: medium
  evidence_refs:
  - ev.jiomart.settlement.4_settlement_structure_event_based_multi_row_model
  confidence: high
  review_status: ready
```


```yaml
candidate_card:
  card_type: rule
  card_id: rule.jiomart.event_not_null_for_structured_analysis
  display_name: Use event IS NOT NULL for structured settlement analysis
  rule_type: filter_rule
  statement: Filter event IS NOT NULL for structured Receivable/BaseTcs/Tds analysis; include NULL event rows only for total
    settlement views.
  applies_to_cards:
  - table.zs_observe.jiomart_settlement
  severity: medium
  evidence_refs:
  - ev.jiomart.settlement.7_data_quality_observations
  confidence: high
  review_status: ready
```


```yaml
candidate_card:
  card_type: rule
  card_id: rule.jiomart.cast_return_amounts
  display_name: Cast JioMart returns amount fields
  rule_type: schema_type_rule
  statement: jiomart_returns charged_amount, refund_amount, and invoice_amount are varchar; cast to DOUBLE before numeric
    aggregation.
  applies_to_cards:
  - column.zs_observe.jiomart_returns.charged_amount
  - column.zs_observe.jiomart_returns.refund_amount
  severity: medium
  evidence_refs:
  - ev.jiomart.returns.3_schema_details_53_columns
  confidence: high
  review_status: ready
```


```yaml
candidate_card:
  card_type: rule
  card_id: rule.jiomart.use_created_date_for_oms_time_series
  display_name: Use created_date for OMS time-series
  rule_type: date_rule
  statement: order_date is NULL for older OMS rows; use created_date as the primary reliable time-series field.
  applies_to_cards:
  - column.zs_observe.jiomart_oms.created_date
  severity: medium
  evidence_refs:
  - ev.jiomart.oms.6_data_quality_observations
  confidence: high
  review_status: ready
```


```yaml
candidate_card:
  card_type: rule
  card_id: rule.jiomart.use_sku_id_mp_sin_combined_key
  display_name: Use sku_id + mp_sin for duplicate SKU analysis
  rule_type: product_key_rule
  statement: Duplicate SKU entries exist with sku null and sku populated; use sku_id plus mp_sin as a combined key for product
    grouping.
  applies_to_cards:
  - column.zs_observe.jiomart_oms.sku_id
  - column.zs_observe.jiomart_oms.mp_sin
  severity: medium
  evidence_refs:
  - ev.jiomart.marketplace.8_data_quality_observations_and_known_issues
  confidence: high
  review_status: ready
```


```yaml
candidate_card:
  card_type: rule
  card_id: rule.jiomart.flag_tcs_rate_anomaly
  display_name: Flag TCS rate anomaly
  rule_type: data_quality_rule
  statement: Flag rows where tcs_igst_rate > 0.05 because source documents tcs_igst_rate = 0.5 as likely data error.
  applies_to_cards:
  - column.zs_observe.jiomart_oms.tcs_igst_rate
  severity: medium
  evidence_refs:
  - ev.jiomart.marketplace.8_data_quality_observations_and_known_issues
  confidence: high
  review_status: ready
```


```yaml
candidate_card:
  card_type: rule
  card_id: rule.jiomart.no_explicit_commission_rows
  display_name: No explicit commission deductions visible in settlement
  rule_type: interpretation_rule
  statement: |-
    Do not create executable commission-fee implementation from jiomart_settlement because source states no explicit commission deductions are visible; Receivable may be post-commission payout.
  applies_to_cards:
  - table.zs_observe.jiomart_settlement
  severity: medium
  evidence_refs:
  - ev.jiomart.marketplace.2_1_jiomart_s_revenue_sources_from_sellers
  confidence: high
  review_status: ready
```

### 4.20 `validation_test` cards


```yaml
candidate_card:
  card_type: validation_test
  card_id: validation_test.jiomart.no_missing_active_filter
  display_name: Active filter present
  test_type: filter_validation
  assertion: Queries against active tables should include is_active = true unless explicitly performing raw load audit.
  expected_result: pass_or_flag
  failure_meaning: Parser should add or require is_active=true for core marketplace analytics.
  applies_to_rules:
  - rule.jiomart.mandatory_filters_group_26
  - rule.jiomart.mandatory_filters_group_221
  evidence_refs:
  - ev.jiomart.marketplace.9_mandatory_query_filters
  confidence: high
  review_status: ready
```


```yaml
candidate_card:
  card_type: validation_test
  card_id: validation_test.jiomart.no_shipment_cross_join
  display_name: Shipment cross-join blocked
  test_type: join_validation
  assertion: No query should join jiomart_shipment to jiomart_oms/returns/settlement without explicit external mapping.
  expected_result: pass_or_flag
  failure_meaning: Prevents mixing ARDEUR group 221 with MYFITNESS group 26.
  applies_to_rules:
  - rule.jiomart.never_cross_join_shipment
  evidence_refs:
  - ev.jiomart.marketplace.4_2_primary_join_keys
  confidence: high
  review_status: ready
```


```yaml
candidate_card:
  card_type: validation_test
  card_id: validation_test.jiomart.returns_amount_cast
  display_name: Return amount cast validation
  test_type: schema_validation
  assertion: Numeric aggregation over jiomart_returns.refund_amount/charged_amount must cast varchar fields to DOUBLE.
  expected_result: pass_or_flag
  failure_meaning: Prevents string aggregation/type errors.
  applies_to_rules:
  - rule.jiomart.cast_return_amounts
  evidence_refs:
  - ev.jiomart.returns.3_schema_details_53_columns
  confidence: high
  review_status: ready
```


```yaml
candidate_card:
  card_type: validation_test
  card_id: validation_test.jiomart.settlement_preaggregation
  display_name: Settlement pre-aggregation validation
  test_type: grain_validation
  assertion: OMS-settlement comparisons must aggregate settlement rows by order_id/accountable_type before comparing.
  expected_result: pass_or_flag
  failure_meaning: Prevents row multiplication in event-based settlement.
  applies_to_rules:
  - rule.jiomart.aggregate_settlement_before_join
  evidence_refs:
  - ev.jiomart.settlement.4_settlement_structure_event_based_multi_row_model
  confidence: high
  review_status: ready
```


```yaml
candidate_card:
  card_type: validation_test
  card_id: validation_test.jiomart.order_id_join_preferred
  display_name: Order ID join preferred
  test_type: join_validation
  assertion: OMS-settlement join should use order_id; invoice_number/document_number joins are not primary.
  expected_result: pass_or_flag
  failure_meaning: Prevents lower-coverage or format-mismatched joins.
  applies_to_rules:
  - rule.jiomart.use_order_id_for_oms_settlement
  evidence_refs:
  - ev.jiomart.marketplace.4_2_primary_join_keys
  confidence: high
  review_status: ready
```


```yaml
candidate_card:
  card_type: validation_test
  card_id: validation_test.jiomart.tcs_rate_anomaly
  display_name: TCS anomaly validation
  test_type: data_quality_validation
  assertion: Rows with tcs_igst_rate > 0.05 should be flagged.
  expected_result: pass_or_flag
  failure_meaning: Detects documented likely data error.
  applies_to_rules:
  - rule.jiomart.flag_tcs_rate_anomaly
  evidence_refs:
  - ev.jiomart.marketplace.8_data_quality_observations_and_known_issues
  confidence: high
  review_status: ready
```

### 4.21 `output_contract` cards


```yaml
candidate_card:
  card_type: output_contract
  card_id: output_contract.jiomart.metric_summary
  display_name: Metric summary output
  contract_type: parser_output_contract
  required_columns:
  - metric_value
  - grain_identifier
  - filters_applied
  grain: metric_or_dimension_grain
  sort_order: Use source SQL ORDER BY where provided.
  evidence_refs:
  - ev.jiomart.marketplace.6_key_business_metrics_with_sql
  confidence: high
  review_status: ready
```


```yaml
candidate_card:
  card_type: output_contract
  card_id: output_contract.jiomart.time_series
  display_name: Time series output
  contract_type: parser_output_contract
  required_columns:
  - month_or_date
  - metric_value
  - supporting_amounts
  grain: period
  sort_order: Use source SQL ORDER BY where provided.
  evidence_refs:
  - ev.jiomart.marketplace.6_key_business_metrics_with_sql
  confidence: high
  review_status: ready
```


```yaml
candidate_card:
  card_type: output_contract
  card_id: output_contract.jiomart.order_reconciliation
  display_name: Order reconciliation output
  contract_type: parser_output_contract
  required_columns:
  - order_id
  - expected_amount
  - actual_amount
  - variance
  - status
  grain: order_id
  sort_order: Use source SQL ORDER BY where provided.
  evidence_refs:
  - ev.jiomart.marketplace.6_key_business_metrics_with_sql
  confidence: high
  review_status: ready
```


```yaml
candidate_card:
  card_type: output_contract
  card_id: output_contract.jiomart.return_reconciliation
  display_name: Return reconciliation output
  contract_type: parser_output_contract
  required_columns:
  - order_id
  - return_type
  - refund_issued
  - original_sale
  - settlement_net
  grain: order_id
  sort_order: Use source SQL ORDER BY where provided.
  evidence_refs:
  - ev.jiomart.marketplace.6_key_business_metrics_with_sql
  confidence: high
  review_status: ready
```


```yaml
candidate_card:
  card_type: output_contract
  card_id: output_contract.jiomart.sku_summary
  display_name: SKU summary output
  contract_type: parser_output_contract
  required_columns:
  - sku_id
  - orders
  - gmv
  - aov_or_refund_amount
  grain: sku_id
  sort_order: Use source SQL ORDER BY where provided.
  evidence_refs:
  - ev.jiomart.marketplace.6_key_business_metrics_with_sql
  confidence: high
  review_status: ready
```


```yaml
candidate_card:
  card_type: output_contract
  card_id: output_contract.jiomart.settlement_event_summary
  display_name: Settlement event summary output
  contract_type: parser_output_contract
  required_columns:
  - transaction_type
  - event
  - accountable_type
  - rows
  - total_settled
  grain: event/accountable_type
  sort_order: Use source SQL ORDER BY where provided.
  evidence_refs:
  - ev.jiomart.marketplace.6_key_business_metrics_with_sql
  confidence: high
  review_status: ready
```


```yaml
candidate_card:
  card_type: output_contract
  card_id: output_contract.jiomart.shipment_summary
  display_name: Shipment summary output
  contract_type: parser_output_contract
  required_columns:
  - order_status_or_month_or_sku
  - shipments_or_orders
  - gmv
  - promo_discount
  grain: shipment_status_or_sku_or_period
  sort_order: Use source SQL ORDER BY where provided.
  evidence_refs:
  - ev.jiomart.marketplace.6_key_business_metrics_with_sql
  confidence: high
  review_status: ready
```

### 4.22 `execution_constraint_set` cards


```yaml
candidate_card:
  card_type: execution_constraint_set
  card_id: execution_constraint_set.jiomart.marketplace_query_constraints
  display_name: JioMart marketplace query constraints
  constraint_family: global_marketplace_query_generation
  required_filters:
  - is_active = true
  - group_level_id = 26 for jiomart_oms/returns/settlement
  - group_level_id = 221 and qty > 0 for jiomart_shipment active-shipment analytics
  aggregation_constraints:
  - Pre-aggregate jiomart_settlement event rows by order_id/accountable_type before comparison joins.
  join_constraints:
  - Use order_id for OMS↔settlement/returns joins.
  - Never cross-join jiomart_shipment to group 26 tables without external mapping.
  sign_constraints:
  - Interpret settlement settled_amount in transaction_type/event/accountable_type context.
  - Use source SQL ABS only where source SQL uses ABS.
  scope_boundaries:
  - No tenant/group/platform-account/bank/payment-gateway/logistics/statutory-filing cards.
  evidence_refs:
  - ev.jiomart.marketplace.9_mandatory_query_filters
  - ev.jiomart.marketplace.4_2_primary_join_keys
  confidence: high
  review_status: ready
```


## 5. Review Items and Source Caveats


```yaml
review_item:
  id: review_item.jiomart.explicit_commission_rows_missing
  source_section: 2.1 JioMart Revenue Sources from Sellers
  issue_type: missing_evidence
  issue_or_caveat: |-
    The source states no explicit commission deductions are visible in jiomart_settlement; commission may be netted into Receivable. Do not create an executable commission-rate implementation from settlement rows.
  recommended_parser_action: Keep fee/commission semantics as rule/caveat unless a separate source exposes commission rows
    or rate basis.
  related_cards:
  - rule.jiomart.no_explicit_commission_rows
  - table.zs_observe.jiomart_settlement
  severity: high
  confidence: high
  review_status: open
```


```yaml
review_item:
  id: review_item.jiomart.reconciliation_tolerance_not_documented
  source_section: 7 Reconciliation Use Cases
  issue_type: ambiguous_threshold
  issue_or_caveat: Source SQL outputs variances/statuses but does not define numeric pass/fail tolerances for TCS variance,
    price variance, or return value variance.
  recommended_parser_action: Expose variance columns as diagnostics; require runtime/user-supplied tolerance for hard validation.
  related_cards:
  - matching_logic.jiomart.oms_settlement_3way
  - matching_logic.jiomart.returns_chain
  - matching_logic.jiomart.tcs_reconciliation
  severity: medium
  confidence: high
  review_status: open
```


```yaml
review_item:
  id: review_item.jiomart.runtime_scope_selection
  source_section: 9 Mandatory Query Filters
  issue_type: external_runtime_scope
  issue_or_caveat: group_level_id=26 and group_level_id=221 are source-documented, but runtime user/account scope selection
    remains outside marketplace canonical semantics.
  recommended_parser_action: Retain group_level_id values as columns/filter guidance; runtime scope layer decides final tenant/account
    constraints.
  related_cards:
  - rule.jiomart.scope_fields_are_columns
  - value_profile.jiomart.scope.group_level_id_26
  - value_profile.jiomart.scope.group_level_id_221
  severity: medium
  confidence: high
  review_status: open
```


```yaml
review_item:
  id: review_item.jiomart.return_reason_analysis_unsupported
  source_section: 8 Data Quality Observations & Known Issues / Returns Data Quality
  issue_type: unsupported_column
  issue_or_caveat: Return reason is mostly NULL, so return-reason analysis is not supported by current JioMart returns data.
  recommended_parser_action: Block or caveat return-reason queries; use return_type/courier/fulfillment dimensions instead.
  related_cards:
  - column.zs_observe.jiomart_returns.reason
  - value_profile.jiomart.returns.return_type
  severity: medium
  confidence: high
  review_status: open
```


```yaml
review_item:
  id: review_item.jiomart.item_level_return_reconciliation_gap
  source_section: Settlement Data Quality Observations
  issue_type: unsupported_column
  issue_or_caveat: Settlement item_id is NULL for return rows, so return settlement reconciliation is safest at order_id grain
    rather than item_id grain.
  recommended_parser_action: Use order_id-grain matching for returns; request external item-level return source if item-level
    reconciliation is required.
  related_cards:
  - relationship.jiomart.settlement_returns.order_id
  - reconciliation_unit.jiomart.order_id
  severity: medium
  confidence: high
  review_status: open
```


## 6. Candidate Edges — Refactored Unified Taxonomy


```yaml
candidate_edge:
  edge_id: edge.jiomart.v9.00001.has_platform_context
  canonical_edge_type: HAS_PLATFORM_CONTEXT
  source_card_id: platform.jiomart
  target_card_id: platform_context.jiomart.in
  edge_class: canonical
  canonical_cognee_edge: true
  source_type: platform
  target_type: platform_context
```


```yaml
candidate_edge:
  edge_id: edge.jiomart.v9.00002.belongs_to_platform
  canonical_edge_type: BELONGS_TO_PLATFORM
  source_card_id: platform_context.jiomart.in
  target_card_id: platform.jiomart
  edge_class: canonical
  canonical_cognee_edge: true
  source_type: platform_context
  target_type: platform
```


```yaml
candidate_edge:
  edge_id: edge.jiomart.v9.00003.applies_to_platform_context
  canonical_edge_type: APPLIES_TO_PLATFORM_CONTEXT
  source_card_id: domain.jiomart.orders
  target_card_id: platform_context.jiomart.in
  edge_class: canonical
  canonical_cognee_edge: true
  source_type: domain
  target_type: platform_context
```


```yaml
candidate_edge:
  edge_id: edge.jiomart.v9.00004.applies_to_platform
  canonical_edge_type: APPLIES_TO_PLATFORM
  source_card_id: domain.jiomart.orders
  target_card_id: platform.jiomart
  edge_class: canonical
  canonical_cognee_edge: true
  source_type: domain
  target_type: platform
```


```yaml
candidate_edge:
  edge_id: edge.jiomart.v9.00005.applies_to_platform_context
  canonical_edge_type: APPLIES_TO_PLATFORM_CONTEXT
  source_card_id: domain.jiomart.settlement
  target_card_id: platform_context.jiomart.in
  edge_class: canonical
  canonical_cognee_edge: true
  source_type: domain
  target_type: platform_context
```


```yaml
candidate_edge:
  edge_id: edge.jiomart.v9.00006.applies_to_platform
  canonical_edge_type: APPLIES_TO_PLATFORM
  source_card_id: domain.jiomart.settlement
  target_card_id: platform.jiomart
  edge_class: canonical
  canonical_cognee_edge: true
  source_type: domain
  target_type: platform
```


```yaml
candidate_edge:
  edge_id: edge.jiomart.v9.00007.applies_to_platform_context
  canonical_edge_type: APPLIES_TO_PLATFORM_CONTEXT
  source_card_id: domain.jiomart.returns
  target_card_id: platform_context.jiomart.in
  edge_class: canonical
  canonical_cognee_edge: true
  source_type: domain
  target_type: platform_context
```


```yaml
candidate_edge:
  edge_id: edge.jiomart.v9.00008.applies_to_platform
  canonical_edge_type: APPLIES_TO_PLATFORM
  source_card_id: domain.jiomart.returns
  target_card_id: platform.jiomart
  edge_class: canonical
  canonical_cognee_edge: true
  source_type: domain
  target_type: platform
```


```yaml
candidate_edge:
  edge_id: edge.jiomart.v9.00009.applies_to_platform_context
  canonical_edge_type: APPLIES_TO_PLATFORM_CONTEXT
  source_card_id: domain.jiomart.reconciliation
  target_card_id: platform_context.jiomart.in
  edge_class: canonical
  canonical_cognee_edge: true
  source_type: domain
  target_type: platform_context
```


```yaml
candidate_edge:
  edge_id: edge.jiomart.v9.00010.applies_to_platform
  canonical_edge_type: APPLIES_TO_PLATFORM
  source_card_id: domain.jiomart.reconciliation
  target_card_id: platform.jiomart
  edge_class: canonical
  canonical_cognee_edge: true
  source_type: domain
  target_type: platform
```


```yaml
candidate_edge:
  edge_id: edge.jiomart.v9.00011.applies_to_platform_context
  canonical_edge_type: APPLIES_TO_PLATFORM_CONTEXT
  source_card_id: domain.jiomart.tax
  target_card_id: platform_context.jiomart.in
  edge_class: canonical
  canonical_cognee_edge: true
  source_type: domain
  target_type: platform_context
```


```yaml
candidate_edge:
  edge_id: edge.jiomart.v9.00012.applies_to_platform
  canonical_edge_type: APPLIES_TO_PLATFORM
  source_card_id: domain.jiomart.tax
  target_card_id: platform.jiomart
  edge_class: canonical
  canonical_cognee_edge: true
  source_type: domain
  target_type: platform
```


```yaml
candidate_edge:
  edge_id: edge.jiomart.v9.00013.applies_to_platform_context
  canonical_edge_type: APPLIES_TO_PLATFORM_CONTEXT
  source_card_id: domain.jiomart.fees
  target_card_id: platform_context.jiomart.in
  edge_class: canonical
  canonical_cognee_edge: true
  source_type: domain
  target_type: platform_context
```


```yaml
candidate_edge:
  edge_id: edge.jiomart.v9.00014.applies_to_platform
  canonical_edge_type: APPLIES_TO_PLATFORM
  source_card_id: domain.jiomart.fees
  target_card_id: platform.jiomart
  edge_class: canonical
  canonical_cognee_edge: true
  source_type: domain
  target_type: platform
```


```yaml
candidate_edge:
  edge_id: edge.jiomart.v9.00015.applies_to_platform_context
  canonical_edge_type: APPLIES_TO_PLATFORM_CONTEXT
  source_card_id: domain.jiomart.fulfillment
  target_card_id: platform_context.jiomart.in
  edge_class: canonical
  canonical_cognee_edge: true
  source_type: domain
  target_type: platform_context
```


```yaml
candidate_edge:
  edge_id: edge.jiomart.v9.00016.applies_to_platform
  canonical_edge_type: APPLIES_TO_PLATFORM
  source_card_id: domain.jiomart.fulfillment
  target_card_id: platform.jiomart
  edge_class: canonical
  canonical_cognee_edge: true
  source_type: domain
  target_type: platform
```


```yaml
candidate_edge:
  edge_id: edge.jiomart.v9.00017.applies_to_platform_context
  canonical_edge_type: APPLIES_TO_PLATFORM_CONTEXT
  source_card_id: domain.jiomart.product
  target_card_id: platform_context.jiomart.in
  edge_class: canonical
  canonical_cognee_edge: true
  source_type: domain
  target_type: platform_context
```


```yaml
candidate_edge:
  edge_id: edge.jiomart.v9.00018.applies_to_platform
  canonical_edge_type: APPLIES_TO_PLATFORM
  source_card_id: domain.jiomart.product
  target_card_id: platform.jiomart
  edge_class: canonical
  canonical_cognee_edge: true
  source_type: domain
  target_type: platform
```


```yaml
candidate_edge:
  edge_id: edge.jiomart.v9.00019.applies_to_platform_context
  canonical_edge_type: APPLIES_TO_PLATFORM_CONTEXT
  source_card_id: domain.jiomart.promotions
  target_card_id: platform_context.jiomart.in
  edge_class: canonical
  canonical_cognee_edge: true
  source_type: domain
  target_type: platform_context
```


```yaml
candidate_edge:
  edge_id: edge.jiomart.v9.00020.applies_to_platform
  canonical_edge_type: APPLIES_TO_PLATFORM
  source_card_id: domain.jiomart.promotions
  target_card_id: platform.jiomart
  edge_class: canonical
  canonical_cognee_edge: true
  source_type: domain
  target_type: platform
```


```yaml
candidate_edge:
  edge_id: edge.jiomart.v9.00021.applies_to_platform_context
  canonical_edge_type: APPLIES_TO_PLATFORM_CONTEXT
  source_card_id: domain.jiomart.payment_mode
  target_card_id: platform_context.jiomart.in
  edge_class: canonical
  canonical_cognee_edge: true
  source_type: domain
  target_type: platform_context
```


```yaml
candidate_edge:
  edge_id: edge.jiomart.v9.00022.applies_to_platform
  canonical_edge_type: APPLIES_TO_PLATFORM
  source_card_id: domain.jiomart.payment_mode
  target_card_id: platform.jiomart
  edge_class: canonical
  canonical_cognee_edge: true
  source_type: domain
  target_type: platform
```


```yaml
candidate_edge:
  edge_id: edge.jiomart.v9.00023.applies_to_platform_context
  canonical_edge_type: APPLIES_TO_PLATFORM_CONTEXT
  source_card_id: domain.jiomart.query_guidance
  target_card_id: platform_context.jiomart.in
  edge_class: canonical
  canonical_cognee_edge: true
  source_type: domain
  target_type: platform_context
```


```yaml
candidate_edge:
  edge_id: edge.jiomart.v9.00024.applies_to_platform
  canonical_edge_type: APPLIES_TO_PLATFORM
  source_card_id: domain.jiomart.query_guidance
  target_card_id: platform.jiomart
  edge_class: canonical
  canonical_cognee_edge: true
  source_type: domain
  target_type: platform
```


```yaml
candidate_edge:
  edge_id: edge.jiomart.v9.00025.sourced_from_platform
  canonical_edge_type: SOURCED_FROM_PLATFORM
  source_card_id: table.zs_observe.jiomart_shipment
  target_card_id: platform.jiomart
  edge_class: canonical
  canonical_cognee_edge: true
  source_type: table
  target_type: platform
```


```yaml
candidate_edge:
  edge_id: edge.jiomart.v9.00026.sourced_from_platform_context
  canonical_edge_type: SOURCED_FROM_PLATFORM_CONTEXT
  source_card_id: table.zs_observe.jiomart_shipment
  target_card_id: platform_context.jiomart.in
  edge_class: canonical
  canonical_cognee_edge: true
  source_type: table
  target_type: platform_context
```


```yaml
candidate_edge:
  edge_id: edge.jiomart.v9.00027.applies_to_platform_context
  canonical_edge_type: APPLIES_TO_PLATFORM_CONTEXT
  source_card_id: table.zs_observe.jiomart_shipment
  target_card_id: platform_context.jiomart.in
  edge_class: canonical
  canonical_cognee_edge: true
  source_type: table
  target_type: platform_context
```


```yaml
candidate_edge:
  edge_id: edge.jiomart.v9.00028.has_column
  canonical_edge_type: HAS_COLUMN
  source_card_id: table.zs_observe.jiomart_shipment
  target_card_id: column.zs_observe.jiomart_shipment.unique_id
  edge_class: canonical
  canonical_cognee_edge: true
  source_type: table
  target_type: column
```


```yaml
candidate_edge:
  edge_id: edge.jiomart.v9.00029.belongs_to_table
  canonical_edge_type: BELONGS_TO_TABLE
  source_card_id: column.zs_observe.jiomart_shipment.unique_id
  target_card_id: table.zs_observe.jiomart_shipment
  edge_class: canonical
  canonical_cognee_edge: true
  source_type: column
  target_type: table
```


```yaml
candidate_edge:
  edge_id: edge.jiomart.v9.00030.has_column
  canonical_edge_type: HAS_COLUMN
  source_card_id: table.zs_observe.jiomart_shipment
  target_card_id: column.zs_observe.jiomart_shipment.txn_uuid
  edge_class: canonical
  canonical_cognee_edge: true
  source_type: table
  target_type: column
```


```yaml
candidate_edge:
  edge_id: edge.jiomart.v9.00031.belongs_to_table
  canonical_edge_type: BELONGS_TO_TABLE
  source_card_id: column.zs_observe.jiomart_shipment.txn_uuid
  target_card_id: table.zs_observe.jiomart_shipment
  edge_class: canonical
  canonical_cognee_edge: true
  source_type: column
  target_type: table
```


```yaml
candidate_edge:
  edge_id: edge.jiomart.v9.00032.has_column
  canonical_edge_type: HAS_COLUMN
  source_card_id: table.zs_observe.jiomart_shipment
  target_card_id: column.zs_observe.jiomart_shipment.unique_value
  edge_class: canonical
  canonical_cognee_edge: true
  source_type: table
  target_type: column
```


```yaml
candidate_edge:
  edge_id: edge.jiomart.v9.00033.belongs_to_table
  canonical_edge_type: BELONGS_TO_TABLE
  source_card_id: column.zs_observe.jiomart_shipment.unique_value
  target_card_id: table.zs_observe.jiomart_shipment
  edge_class: canonical
  canonical_cognee_edge: true
  source_type: column
  target_type: table
```


```yaml
candidate_edge:
  edge_id: edge.jiomart.v9.00034.has_column
  canonical_edge_type: HAS_COLUMN
  source_card_id: table.zs_observe.jiomart_shipment
  target_card_id: column.zs_observe.jiomart_shipment.source_gst_name
  edge_class: canonical
  canonical_cognee_edge: true
  source_type: table
  target_type: column
```


```yaml
candidate_edge:
  edge_id: edge.jiomart.v9.00035.belongs_to_table
  canonical_edge_type: BELONGS_TO_TABLE
  source_card_id: column.zs_observe.jiomart_shipment.source_gst_name
  target_card_id: table.zs_observe.jiomart_shipment
  edge_class: canonical
  canonical_cognee_edge: true
  source_type: column
  target_type: table
```


```yaml
candidate_edge:
  edge_id: edge.jiomart.v9.00036.has_column
  canonical_edge_type: HAS_COLUMN
  source_card_id: table.zs_observe.jiomart_shipment
  target_card_id: column.zs_observe.jiomart_shipment.order_id
  edge_class: canonical
  canonical_cognee_edge: true
  source_type: table
  target_type: column
```


```yaml
candidate_edge:
  edge_id: edge.jiomart.v9.00037.belongs_to_table
  canonical_edge_type: BELONGS_TO_TABLE
  source_card_id: column.zs_observe.jiomart_shipment.order_id
  target_card_id: table.zs_observe.jiomart_shipment
  edge_class: canonical
  canonical_cognee_edge: true
  source_type: column
  target_type: table
```


```yaml
candidate_edge:
  edge_id: edge.jiomart.v9.00038.has_column
  canonical_edge_type: HAS_COLUMN
  source_card_id: table.zs_observe.jiomart_shipment
  target_card_id: column.zs_observe.jiomart_shipment.created_date
  edge_class: canonical
  canonical_cognee_edge: true
  source_type: table
  target_type: column
```


```yaml
candidate_edge:
  edge_id: edge.jiomart.v9.00039.belongs_to_table
  canonical_edge_type: BELONGS_TO_TABLE
  source_card_id: column.zs_observe.jiomart_shipment.created_date
  target_card_id: table.zs_observe.jiomart_shipment
  edge_class: canonical
  canonical_cognee_edge: true
  source_type: column
  target_type: table
```


```yaml
candidate_edge:
  edge_id: edge.jiomart.v9.00040.has_column
  canonical_edge_type: HAS_COLUMN
  source_card_id: table.zs_observe.jiomart_shipment
  target_card_id: column.zs_observe.jiomart_shipment.order_status
  edge_class: canonical
  canonical_cognee_edge: true
  source_type: table
  target_type: column
```


```yaml
candidate_edge:
  edge_id: edge.jiomart.v9.00041.belongs_to_table
  canonical_edge_type: BELONGS_TO_TABLE
  source_card_id: column.zs_observe.jiomart_shipment.order_status
  target_card_id: table.zs_observe.jiomart_shipment
  edge_class: canonical
  canonical_cognee_edge: true
  source_type: column
  target_type: table
```


```yaml
candidate_edge:
  edge_id: edge.jiomart.v9.00042.has_column
  canonical_edge_type: HAS_COLUMN
  source_card_id: table.zs_observe.jiomart_shipment
  target_card_id: column.zs_observe.jiomart_shipment.qty
  edge_class: canonical
  canonical_cognee_edge: true
  source_type: table
  target_type: column
```


```yaml
candidate_edge:
  edge_id: edge.jiomart.v9.00043.belongs_to_table
  canonical_edge_type: BELONGS_TO_TABLE
  source_card_id: column.zs_observe.jiomart_shipment.qty
  target_card_id: table.zs_observe.jiomart_shipment
  edge_class: canonical
  canonical_cognee_edge: true
  source_type: column
  target_type: table
```


```yaml
candidate_edge:
  edge_id: edge.jiomart.v9.00044.has_column
  canonical_edge_type: HAS_COLUMN
  source_card_id: table.zs_observe.jiomart_shipment
  target_card_id: column.zs_observe.jiomart_shipment.description
  edge_class: canonical
  canonical_cognee_edge: true
  source_type: table
  target_type: column
```


```yaml
candidate_edge:
  edge_id: edge.jiomart.v9.00045.belongs_to_table
  canonical_edge_type: BELONGS_TO_TABLE
  source_card_id: column.zs_observe.jiomart_shipment.description
  target_card_id: table.zs_observe.jiomart_shipment
  edge_class: canonical
  canonical_cognee_edge: true
  source_type: column
  target_type: table
```


```yaml
candidate_edge:
  edge_id: edge.jiomart.v9.00046.has_column
  canonical_edge_type: HAS_COLUMN
  source_card_id: table.zs_observe.jiomart_shipment
  target_card_id: column.zs_observe.jiomart_shipment.fulfillment_channel
  edge_class: canonical
  canonical_cognee_edge: true
  source_type: table
  target_type: column
```


```yaml
candidate_edge:
  edge_id: edge.jiomart.v9.00047.belongs_to_table
  canonical_edge_type: BELONGS_TO_TABLE
  source_card_id: column.zs_observe.jiomart_shipment.fulfillment_channel
  target_card_id: table.zs_observe.jiomart_shipment
  edge_class: canonical
  canonical_cognee_edge: true
  source_type: column
  target_type: table
```


```yaml
candidate_edge:
  edge_id: edge.jiomart.v9.00048.has_column
  canonical_edge_type: HAS_COLUMN
  source_card_id: table.zs_observe.jiomart_shipment
  target_card_id: column.zs_observe.jiomart_shipment.sku_id
  edge_class: canonical
  canonical_cognee_edge: true
  source_type: table
  target_type: column
```


```yaml
candidate_edge:
  edge_id: edge.jiomart.v9.00049.belongs_to_table
  canonical_edge_type: BELONGS_TO_TABLE
  source_card_id: column.zs_observe.jiomart_shipment.sku_id
  target_card_id: table.zs_observe.jiomart_shipment
  edge_class: canonical
  canonical_cognee_edge: true
  source_type: column
  target_type: table
```


```yaml
candidate_edge:
  edge_id: edge.jiomart.v9.00050.has_column
  canonical_edge_type: HAS_COLUMN
  source_card_id: table.zs_observe.jiomart_shipment
  target_card_id: column.zs_observe.jiomart_shipment.mrp
  edge_class: canonical
  canonical_cognee_edge: true
  source_type: table
  target_type: column
```


```yaml
candidate_edge:
  edge_id: edge.jiomart.v9.00051.belongs_to_table
  canonical_edge_type: BELONGS_TO_TABLE
  source_card_id: column.zs_observe.jiomart_shipment.mrp
  target_card_id: table.zs_observe.jiomart_shipment
  edge_class: canonical
  canonical_cognee_edge: true
  source_type: column
  target_type: table
```


```yaml
candidate_edge:
  edge_id: edge.jiomart.v9.00052.has_column
  canonical_edge_type: HAS_COLUMN
  source_card_id: table.zs_observe.jiomart_shipment
  target_card_id: column.zs_observe.jiomart_shipment.charged_amount
  edge_class: canonical
  canonical_cognee_edge: true
  source_type: table
  target_type: column
```


```yaml
candidate_edge:
  edge_id: edge.jiomart.v9.00053.belongs_to_table
  canonical_edge_type: BELONGS_TO_TABLE
  source_card_id: column.zs_observe.jiomart_shipment.charged_amount
  target_card_id: table.zs_observe.jiomart_shipment
  edge_class: canonical
  canonical_cognee_edge: true
  source_type: column
  target_type: table
```


```yaml
candidate_edge:
  edge_id: edge.jiomart.v9.00054.has_column
  canonical_edge_type: HAS_COLUMN
  source_card_id: table.zs_observe.jiomart_shipment
  target_card_id: column.zs_observe.jiomart_shipment.item_promo_discount
  edge_class: canonical
  canonical_cognee_edge: true
  source_type: table
  target_type: column
```


```yaml
candidate_edge:
  edge_id: edge.jiomart.v9.00055.belongs_to_table
  canonical_edge_type: BELONGS_TO_TABLE
  source_card_id: column.zs_observe.jiomart_shipment.item_promo_discount
  target_card_id: table.zs_observe.jiomart_shipment
  edge_class: canonical
  canonical_cognee_edge: true
  source_type: column
  target_type: table
```


```yaml
candidate_edge:
  edge_id: edge.jiomart.v9.00056.has_column
  canonical_edge_type: HAS_COLUMN
  source_card_id: table.zs_observe.jiomart_shipment
  target_card_id: column.zs_observe.jiomart_shipment.payment_mode
  edge_class: canonical
  canonical_cognee_edge: true
  source_type: table
  target_type: column
```


```yaml
candidate_edge:
  edge_id: edge.jiomart.v9.00057.belongs_to_table
  canonical_edge_type: BELONGS_TO_TABLE
  source_card_id: column.zs_observe.jiomart_shipment.payment_mode
  target_card_id: table.zs_observe.jiomart_shipment
  edge_class: canonical
  canonical_cognee_edge: true
  source_type: column
  target_type: table
```


```yaml
candidate_edge:
  edge_id: edge.jiomart.v9.00058.has_column
  canonical_edge_type: HAS_COLUMN
  source_card_id: table.zs_observe.jiomart_shipment
  target_card_id: column.zs_observe.jiomart_shipment.shipping_date
  edge_class: canonical
  canonical_cognee_edge: true
  source_type: table
  target_type: column
```


```yaml
candidate_edge:
  edge_id: edge.jiomart.v9.00059.belongs_to_table
  canonical_edge_type: BELONGS_TO_TABLE
  source_card_id: column.zs_observe.jiomart_shipment.shipping_date
  target_card_id: table.zs_observe.jiomart_shipment
  edge_class: canonical
  canonical_cognee_edge: true
  source_type: column
  target_type: table
```


```yaml
candidate_edge:
  edge_id: edge.jiomart.v9.00060.has_column
  canonical_edge_type: HAS_COLUMN
  source_card_id: table.zs_observe.jiomart_shipment
  target_card_id: column.zs_observe.jiomart_shipment.currency_type
  edge_class: canonical
  canonical_cognee_edge: true
  source_type: table
  target_type: column
```


```yaml
candidate_edge:
  edge_id: edge.jiomart.v9.00061.belongs_to_table
  canonical_edge_type: BELONGS_TO_TABLE
  source_card_id: column.zs_observe.jiomart_shipment.currency_type
  target_card_id: table.zs_observe.jiomart_shipment
  edge_class: canonical
  canonical_cognee_edge: true
  source_type: column
  target_type: table
```


```yaml
candidate_edge:
  edge_id: edge.jiomart.v9.00062.has_column
  canonical_edge_type: HAS_COLUMN
  source_card_id: table.zs_observe.jiomart_shipment
  target_card_id: column.zs_observe.jiomart_shipment.is_active
  edge_class: canonical
  canonical_cognee_edge: true
  source_type: table
  target_type: column
```


```yaml
candidate_edge:
  edge_id: edge.jiomart.v9.00063.belongs_to_table
  canonical_edge_type: BELONGS_TO_TABLE
  source_card_id: column.zs_observe.jiomart_shipment.is_active
  target_card_id: table.zs_observe.jiomart_shipment
  edge_class: canonical
  canonical_cognee_edge: true
  source_type: column
  target_type: table
```


```yaml
candidate_edge:
  edge_id: edge.jiomart.v9.00064.has_column
  canonical_edge_type: HAS_COLUMN
  source_card_id: table.zs_observe.jiomart_shipment
  target_card_id: column.zs_observe.jiomart_shipment.group_level_id
  edge_class: canonical
  canonical_cognee_edge: true
  source_type: table
  target_type: column
```


```yaml
candidate_edge:
  edge_id: edge.jiomart.v9.00065.belongs_to_table
  canonical_edge_type: BELONGS_TO_TABLE
  source_card_id: column.zs_observe.jiomart_shipment.group_level_id
  target_card_id: table.zs_observe.jiomart_shipment
  edge_class: canonical
  canonical_cognee_edge: true
  source_type: column
  target_type: table
```


```yaml
candidate_edge:
  edge_id: edge.jiomart.v9.00066.has_column
  canonical_edge_type: HAS_COLUMN
  source_card_id: table.zs_observe.jiomart_shipment
  target_card_id: column.zs_observe.jiomart_shipment.zen_sheet_name
  edge_class: canonical
  canonical_cognee_edge: true
  source_type: table
  target_type: column
```


```yaml
candidate_edge:
  edge_id: edge.jiomart.v9.00067.belongs_to_table
  canonical_edge_type: BELONGS_TO_TABLE
  source_card_id: column.zs_observe.jiomart_shipment.zen_sheet_name
  target_card_id: table.zs_observe.jiomart_shipment
  edge_class: canonical
  canonical_cognee_edge: true
  source_type: column
  target_type: table
```


```yaml
candidate_edge:
  edge_id: edge.jiomart.v9.00068.has_column
  canonical_edge_type: HAS_COLUMN
  source_card_id: table.zs_observe.jiomart_shipment
  target_card_id: column.zs_observe.jiomart_shipment.created_at
  edge_class: canonical
  canonical_cognee_edge: true
  source_type: table
  target_type: column
```


```yaml
candidate_edge:
  edge_id: edge.jiomart.v9.00069.belongs_to_table
  canonical_edge_type: BELONGS_TO_TABLE
  source_card_id: column.zs_observe.jiomart_shipment.created_at
  target_card_id: table.zs_observe.jiomart_shipment
  edge_class: canonical
  canonical_cognee_edge: true
  source_type: column
  target_type: table
```


```yaml
candidate_edge:
  edge_id: edge.jiomart.v9.00070.has_column
  canonical_edge_type: HAS_COLUMN
  source_card_id: table.zs_observe.jiomart_shipment
  target_card_id: column.zs_observe.jiomart_shipment.updated_at
  edge_class: canonical
  canonical_cognee_edge: true
  source_type: table
  target_type: column
```


```yaml
candidate_edge:
  edge_id: edge.jiomart.v9.00071.belongs_to_table
  canonical_edge_type: BELONGS_TO_TABLE
  source_card_id: column.zs_observe.jiomart_shipment.updated_at
  target_card_id: table.zs_observe.jiomart_shipment
  edge_class: canonical
  canonical_cognee_edge: true
  source_type: column
  target_type: table
```


```yaml
candidate_edge:
  edge_id: edge.jiomart.v9.00072.sourced_from_platform
  canonical_edge_type: SOURCED_FROM_PLATFORM
  source_card_id: table.zs_observe.jiomart_settlement
  target_card_id: platform.jiomart
  edge_class: canonical
  canonical_cognee_edge: true
  source_type: table
  target_type: platform
```


```yaml
candidate_edge:
  edge_id: edge.jiomart.v9.00073.sourced_from_platform_context
  canonical_edge_type: SOURCED_FROM_PLATFORM_CONTEXT
  source_card_id: table.zs_observe.jiomart_settlement
  target_card_id: platform_context.jiomart.in
  edge_class: canonical
  canonical_cognee_edge: true
  source_type: table
  target_type: platform_context
```


```yaml
candidate_edge:
  edge_id: edge.jiomart.v9.00074.applies_to_platform_context
  canonical_edge_type: APPLIES_TO_PLATFORM_CONTEXT
  source_card_id: table.zs_observe.jiomart_settlement
  target_card_id: platform_context.jiomart.in
  edge_class: canonical
  canonical_cognee_edge: true
  source_type: table
  target_type: platform_context
```


```yaml
candidate_edge:
  edge_id: edge.jiomart.v9.00075.has_column
  canonical_edge_type: HAS_COLUMN
  source_card_id: table.zs_observe.jiomart_settlement
  target_card_id: column.zs_observe.jiomart_settlement.unique_id
  edge_class: canonical
  canonical_cognee_edge: true
  source_type: table
  target_type: column
```


```yaml
candidate_edge:
  edge_id: edge.jiomart.v9.00076.belongs_to_table
  canonical_edge_type: BELONGS_TO_TABLE
  source_card_id: column.zs_observe.jiomart_settlement.unique_id
  target_card_id: table.zs_observe.jiomart_settlement
  edge_class: canonical
  canonical_cognee_edge: true
  source_type: column
  target_type: table
```


```yaml
candidate_edge:
  edge_id: edge.jiomart.v9.00077.has_column
  canonical_edge_type: HAS_COLUMN
  source_card_id: table.zs_observe.jiomart_settlement
  target_card_id: column.zs_observe.jiomart_settlement.txn_uuid
  edge_class: canonical
  canonical_cognee_edge: true
  source_type: table
  target_type: column
```


```yaml
candidate_edge:
  edge_id: edge.jiomart.v9.00078.belongs_to_table
  canonical_edge_type: BELONGS_TO_TABLE
  source_card_id: column.zs_observe.jiomart_settlement.txn_uuid
  target_card_id: table.zs_observe.jiomart_settlement
  edge_class: canonical
  canonical_cognee_edge: true
  source_type: column
  target_type: table
```


```yaml
candidate_edge:
  edge_id: edge.jiomart.v9.00079.has_column
  canonical_edge_type: HAS_COLUMN
  source_card_id: table.zs_observe.jiomart_settlement
  target_card_id: column.zs_observe.jiomart_settlement.unique_value
  edge_class: canonical
  canonical_cognee_edge: true
  source_type: table
  target_type: column
```


```yaml
candidate_edge:
  edge_id: edge.jiomart.v9.00080.belongs_to_table
  canonical_edge_type: BELONGS_TO_TABLE
  source_card_id: column.zs_observe.jiomart_settlement.unique_value
  target_card_id: table.zs_observe.jiomart_settlement
  edge_class: canonical
  canonical_cognee_edge: true
  source_type: column
  target_type: table
```


```yaml
candidate_edge:
  edge_id: edge.jiomart.v9.00081.has_column
  canonical_edge_type: HAS_COLUMN
  source_card_id: table.zs_observe.jiomart_settlement
  target_card_id: column.zs_observe.jiomart_settlement.invoice_number
  edge_class: canonical
  canonical_cognee_edge: true
  source_type: table
  target_type: column
```


```yaml
candidate_edge:
  edge_id: edge.jiomart.v9.00082.belongs_to_table
  canonical_edge_type: BELONGS_TO_TABLE
  source_card_id: column.zs_observe.jiomart_settlement.invoice_number
  target_card_id: table.zs_observe.jiomart_settlement
  edge_class: canonical
  canonical_cognee_edge: true
  source_type: column
  target_type: table
```


```yaml
candidate_edge:
  edge_id: edge.jiomart.v9.00083.has_column
  canonical_edge_type: HAS_COLUMN
  source_card_id: table.zs_observe.jiomart_settlement
  target_card_id: column.zs_observe.jiomart_settlement.order_id
  edge_class: canonical
  canonical_cognee_edge: true
  source_type: table
  target_type: column
```


```yaml
candidate_edge:
  edge_id: edge.jiomart.v9.00084.belongs_to_table
  canonical_edge_type: BELONGS_TO_TABLE
  source_card_id: column.zs_observe.jiomart_settlement.order_id
  target_card_id: table.zs_observe.jiomart_settlement
  edge_class: canonical
  canonical_cognee_edge: true
  source_type: column
  target_type: table
```


```yaml
candidate_edge:
  edge_id: edge.jiomart.v9.00085.has_column
  canonical_edge_type: HAS_COLUMN
  source_card_id: table.zs_observe.jiomart_settlement
  target_card_id: column.zs_observe.jiomart_settlement.item_id
  edge_class: canonical
  canonical_cognee_edge: true
  source_type: table
  target_type: column
```


```yaml
candidate_edge:
  edge_id: edge.jiomart.v9.00086.belongs_to_table
  canonical_edge_type: BELONGS_TO_TABLE
  source_card_id: column.zs_observe.jiomart_settlement.item_id
  target_card_id: table.zs_observe.jiomart_settlement
  edge_class: canonical
  canonical_cognee_edge: true
  source_type: column
  target_type: table
```


```yaml
candidate_edge:
  edge_id: edge.jiomart.v9.00087.has_column
  canonical_edge_type: HAS_COLUMN
  source_card_id: table.zs_observe.jiomart_settlement
  target_card_id: column.zs_observe.jiomart_settlement.parent_id
  edge_class: canonical
  canonical_cognee_edge: true
  source_type: table
  target_type: column
```


```yaml
candidate_edge:
  edge_id: edge.jiomart.v9.00088.belongs_to_table
  canonical_edge_type: BELONGS_TO_TABLE
  source_card_id: column.zs_observe.jiomart_settlement.parent_id
  target_card_id: table.zs_observe.jiomart_settlement
  edge_class: canonical
  canonical_cognee_edge: true
  source_type: column
  target_type: table
```


```yaml
candidate_edge:
  edge_id: edge.jiomart.v9.00089.has_column
  canonical_edge_type: HAS_COLUMN
  source_card_id: table.zs_observe.jiomart_settlement
  target_card_id: column.zs_observe.jiomart_settlement.other_id
  edge_class: canonical
  canonical_cognee_edge: true
  source_type: table
  target_type: column
```


```yaml
candidate_edge:
  edge_id: edge.jiomart.v9.00090.belongs_to_table
  canonical_edge_type: BELONGS_TO_TABLE
  source_card_id: column.zs_observe.jiomart_settlement.other_id
  target_card_id: table.zs_observe.jiomart_settlement
  edge_class: canonical
  canonical_cognee_edge: true
  source_type: column
  target_type: table
```


```yaml
candidate_edge:
  edge_id: edge.jiomart.v9.00091.has_column
  canonical_edge_type: HAS_COLUMN
  source_card_id: table.zs_observe.jiomart_settlement
  target_card_id: column.zs_observe.jiomart_settlement.document_number
  edge_class: canonical
  canonical_cognee_edge: true
  source_type: table
  target_type: column
```


```yaml
candidate_edge:
  edge_id: edge.jiomart.v9.00092.belongs_to_table
  canonical_edge_type: BELONGS_TO_TABLE
  source_card_id: column.zs_observe.jiomart_settlement.document_number
  target_card_id: table.zs_observe.jiomart_settlement
  edge_class: canonical
  canonical_cognee_edge: true
  source_type: column
  target_type: table
```


```yaml
candidate_edge:
  edge_id: edge.jiomart.v9.00093.has_column
  canonical_edge_type: HAS_COLUMN
  source_card_id: table.zs_observe.jiomart_settlement
  target_card_id: column.zs_observe.jiomart_settlement.shipment_number
  edge_class: canonical
  canonical_cognee_edge: true
  source_type: table
  target_type: column
```


```yaml
candidate_edge:
  edge_id: edge.jiomart.v9.00094.belongs_to_table
  canonical_edge_type: BELONGS_TO_TABLE
  source_card_id: column.zs_observe.jiomart_settlement.shipment_number
  target_card_id: table.zs_observe.jiomart_settlement
  edge_class: canonical
  canonical_cognee_edge: true
  source_type: column
  target_type: table
```


```yaml
candidate_edge:
  edge_id: edge.jiomart.v9.00095.has_column
  canonical_edge_type: HAS_COLUMN
  source_card_id: table.zs_observe.jiomart_settlement
  target_card_id: column.zs_observe.jiomart_settlement.accountable_number
  edge_class: canonical
  canonical_cognee_edge: true
  source_type: table
  target_type: column
```


```yaml
candidate_edge:
  edge_id: edge.jiomart.v9.00096.belongs_to_table
  canonical_edge_type: BELONGS_TO_TABLE
  source_card_id: column.zs_observe.jiomart_settlement.accountable_number
  target_card_id: table.zs_observe.jiomart_settlement
  edge_class: canonical
  canonical_cognee_edge: true
  source_type: column
  target_type: table
```


```yaml
candidate_edge:
  edge_id: edge.jiomart.v9.00097.has_column
  canonical_edge_type: HAS_COLUMN
  source_card_id: table.zs_observe.jiomart_settlement
  target_card_id: column.zs_observe.jiomart_settlement.number
  edge_class: canonical
  canonical_cognee_edge: true
  source_type: table
  target_type: column
```


```yaml
candidate_edge:
  edge_id: edge.jiomart.v9.00098.belongs_to_table
  canonical_edge_type: BELONGS_TO_TABLE
  source_card_id: column.zs_observe.jiomart_settlement.number
  target_card_id: table.zs_observe.jiomart_settlement
  edge_class: canonical
  canonical_cognee_edge: true
  source_type: column
  target_type: table
```


```yaml
candidate_edge:
  edge_id: edge.jiomart.v9.00099.has_column
  canonical_edge_type: HAS_COLUMN
  source_card_id: table.zs_observe.jiomart_settlement
  target_card_id: column.zs_observe.jiomart_settlement.unique_id_1
  edge_class: canonical
  canonical_cognee_edge: true
  source_type: table
  target_type: column
```


```yaml
candidate_edge:
  edge_id: edge.jiomart.v9.00100.belongs_to_table
  canonical_edge_type: BELONGS_TO_TABLE
  source_card_id: column.zs_observe.jiomart_settlement.unique_id_1
  target_card_id: table.zs_observe.jiomart_settlement
  edge_class: canonical
  canonical_cognee_edge: true
  source_type: column
  target_type: table
```


```yaml
candidate_edge:
  edge_id: edge.jiomart.v9.00101.has_column
  canonical_edge_type: HAS_COLUMN
  source_card_id: table.zs_observe.jiomart_settlement
  target_card_id: column.zs_observe.jiomart_settlement.settlement_date
  edge_class: canonical
  canonical_cognee_edge: true
  source_type: table
  target_type: column
```


```yaml
candidate_edge:
  edge_id: edge.jiomart.v9.00102.belongs_to_table
  canonical_edge_type: BELONGS_TO_TABLE
  source_card_id: column.zs_observe.jiomart_settlement.settlement_date
  target_card_id: table.zs_observe.jiomart_settlement
  edge_class: canonical
  canonical_cognee_edge: true
  source_type: column
  target_type: table
```


```yaml
candidate_edge:
  edge_id: edge.jiomart.v9.00103.has_column
  canonical_edge_type: HAS_COLUMN
  source_card_id: table.zs_observe.jiomart_settlement
  target_card_id: column.zs_observe.jiomart_settlement.created_at
  edge_class: canonical
  canonical_cognee_edge: true
  source_type: table
  target_type: column
```


```yaml
candidate_edge:
  edge_id: edge.jiomart.v9.00104.belongs_to_table
  canonical_edge_type: BELONGS_TO_TABLE
  source_card_id: column.zs_observe.jiomart_settlement.created_at
  target_card_id: table.zs_observe.jiomart_settlement
  edge_class: canonical
  canonical_cognee_edge: true
  source_type: column
  target_type: table
```


```yaml
candidate_edge:
  edge_id: edge.jiomart.v9.00105.has_column
  canonical_edge_type: HAS_COLUMN
  source_card_id: table.zs_observe.jiomart_settlement
  target_card_id: column.zs_observe.jiomart_settlement.created_at_1
  edge_class: canonical
  canonical_cognee_edge: true
  source_type: table
  target_type: column
```


```yaml
candidate_edge:
  edge_id: edge.jiomart.v9.00106.belongs_to_table
  canonical_edge_type: BELONGS_TO_TABLE
  source_card_id: column.zs_observe.jiomart_settlement.created_at_1
  target_card_id: table.zs_observe.jiomart_settlement
  edge_class: canonical
  canonical_cognee_edge: true
  source_type: column
  target_type: table
```


```yaml
candidate_edge:
  edge_id: edge.jiomart.v9.00107.has_column
  canonical_edge_type: HAS_COLUMN
  source_card_id: table.zs_observe.jiomart_settlement
  target_card_id: column.zs_observe.jiomart_settlement.created_at_temp_old
  edge_class: canonical
  canonical_cognee_edge: true
  source_type: table
  target_type: column
```


```yaml
candidate_edge:
  edge_id: edge.jiomart.v9.00108.belongs_to_table
  canonical_edge_type: BELONGS_TO_TABLE
  source_card_id: column.zs_observe.jiomart_settlement.created_at_temp_old
  target_card_id: table.zs_observe.jiomart_settlement
  edge_class: canonical
  canonical_cognee_edge: true
  source_type: column
  target_type: table
```


```yaml
candidate_edge:
  edge_id: edge.jiomart.v9.00109.has_column
  canonical_edge_type: HAS_COLUMN
  source_card_id: table.zs_observe.jiomart_settlement
  target_card_id: column.zs_observe.jiomart_settlement.settled_amount
  edge_class: canonical
  canonical_cognee_edge: true
  source_type: table
  target_type: column
```


```yaml
candidate_edge:
  edge_id: edge.jiomart.v9.00110.belongs_to_table
  canonical_edge_type: BELONGS_TO_TABLE
  source_card_id: column.zs_observe.jiomart_settlement.settled_amount
  target_card_id: table.zs_observe.jiomart_settlement
  edge_class: canonical
  canonical_cognee_edge: true
  source_type: column
  target_type: table
```


```yaml
candidate_edge:
  edge_id: edge.jiomart.v9.00111.has_column
  canonical_edge_type: HAS_COLUMN
  source_card_id: table.zs_observe.jiomart_settlement
  target_card_id: column.zs_observe.jiomart_settlement.amount
  edge_class: canonical
  canonical_cognee_edge: true
  source_type: table
  target_type: column
```


```yaml
candidate_edge:
  edge_id: edge.jiomart.v9.00112.belongs_to_table
  canonical_edge_type: BELONGS_TO_TABLE
  source_card_id: column.zs_observe.jiomart_settlement.amount
  target_card_id: table.zs_observe.jiomart_settlement
  edge_class: canonical
  canonical_cognee_edge: true
  source_type: column
  target_type: table
```


```yaml
candidate_edge:
  edge_id: edge.jiomart.v9.00113.has_column
  canonical_edge_type: HAS_COLUMN
  source_card_id: table.zs_observe.jiomart_settlement
  target_card_id: column.zs_observe.jiomart_settlement.transaction_type
  edge_class: canonical
  canonical_cognee_edge: true
  source_type: table
  target_type: column
```


```yaml
candidate_edge:
  edge_id: edge.jiomart.v9.00114.belongs_to_table
  canonical_edge_type: BELONGS_TO_TABLE
  source_card_id: column.zs_observe.jiomart_settlement.transaction_type
  target_card_id: table.zs_observe.jiomart_settlement
  edge_class: canonical
  canonical_cognee_edge: true
  source_type: column
  target_type: table
```


```yaml
candidate_edge:
  edge_id: edge.jiomart.v9.00115.has_column
  canonical_edge_type: HAS_COLUMN
  source_card_id: table.zs_observe.jiomart_settlement
  target_card_id: column.zs_observe.jiomart_settlement.event
  edge_class: canonical
  canonical_cognee_edge: true
  source_type: table
  target_type: column
```


```yaml
candidate_edge:
  edge_id: edge.jiomart.v9.00116.belongs_to_table
  canonical_edge_type: BELONGS_TO_TABLE
  source_card_id: column.zs_observe.jiomart_settlement.event
  target_card_id: table.zs_observe.jiomart_settlement
  edge_class: canonical
  canonical_cognee_edge: true
  source_type: column
  target_type: table
```


```yaml
candidate_edge:
  edge_id: edge.jiomart.v9.00117.has_column
  canonical_edge_type: HAS_COLUMN
  source_card_id: table.zs_observe.jiomart_settlement
  target_card_id: column.zs_observe.jiomart_settlement.accountable_type
  edge_class: canonical
  canonical_cognee_edge: true
  source_type: table
  target_type: column
```


```yaml
candidate_edge:
  edge_id: edge.jiomart.v9.00118.belongs_to_table
  canonical_edge_type: BELONGS_TO_TABLE
  source_card_id: column.zs_observe.jiomart_settlement.accountable_type
  target_card_id: table.zs_observe.jiomart_settlement
  edge_class: canonical
  canonical_cognee_edge: true
  source_type: column
  target_type: table
```


```yaml
candidate_edge:
  edge_id: edge.jiomart.v9.00119.has_column
  canonical_edge_type: HAS_COLUMN
  source_card_id: table.zs_observe.jiomart_settlement
  target_card_id: column.zs_observe.jiomart_settlement.account_book
  edge_class: canonical
  canonical_cognee_edge: true
  source_type: table
  target_type: column
```


```yaml
candidate_edge:
  edge_id: edge.jiomart.v9.00120.belongs_to_table
  canonical_edge_type: BELONGS_TO_TABLE
  source_card_id: column.zs_observe.jiomart_settlement.account_book
  target_card_id: table.zs_observe.jiomart_settlement
  edge_class: canonical
  canonical_cognee_edge: true
  source_type: column
  target_type: table
```


```yaml
candidate_edge:
  edge_id: edge.jiomart.v9.00121.has_column
  canonical_edge_type: HAS_COLUMN
  source_card_id: table.zs_observe.jiomart_settlement
  target_card_id: column.zs_observe.jiomart_settlement.description
  edge_class: canonical
  canonical_cognee_edge: true
  source_type: table
  target_type: column
```


```yaml
candidate_edge:
  edge_id: edge.jiomart.v9.00122.belongs_to_table
  canonical_edge_type: BELONGS_TO_TABLE
  source_card_id: column.zs_observe.jiomart_settlement.description
  target_card_id: table.zs_observe.jiomart_settlement
  edge_class: canonical
  canonical_cognee_edge: true
  source_type: column
  target_type: table
```


```yaml
candidate_edge:
  edge_id: edge.jiomart.v9.00123.has_column
  canonical_edge_type: HAS_COLUMN
  source_card_id: table.zs_observe.jiomart_settlement
  target_card_id: column.zs_observe.jiomart_settlement.group_level_id
  edge_class: canonical
  canonical_cognee_edge: true
  source_type: table
  target_type: column
```


```yaml
candidate_edge:
  edge_id: edge.jiomart.v9.00124.belongs_to_table
  canonical_edge_type: BELONGS_TO_TABLE
  source_card_id: column.zs_observe.jiomart_settlement.group_level_id
  target_card_id: table.zs_observe.jiomart_settlement
  edge_class: canonical
  canonical_cognee_edge: true
  source_type: column
  target_type: table
```


```yaml
candidate_edge:
  edge_id: edge.jiomart.v9.00125.has_column
  canonical_edge_type: HAS_COLUMN
  source_card_id: table.zs_observe.jiomart_settlement
  target_card_id: column.zs_observe.jiomart_settlement.currency_type
  edge_class: canonical
  canonical_cognee_edge: true
  source_type: table
  target_type: column
```


```yaml
candidate_edge:
  edge_id: edge.jiomart.v9.00126.belongs_to_table
  canonical_edge_type: BELONGS_TO_TABLE
  source_card_id: column.zs_observe.jiomart_settlement.currency_type
  target_card_id: table.zs_observe.jiomart_settlement
  edge_class: canonical
  canonical_cognee_edge: true
  source_type: column
  target_type: table
```


```yaml
candidate_edge:
  edge_id: edge.jiomart.v9.00127.has_column
  canonical_edge_type: HAS_COLUMN
  source_card_id: table.zs_observe.jiomart_settlement
  target_card_id: column.zs_observe.jiomart_settlement.is_active
  edge_class: canonical
  canonical_cognee_edge: true
  source_type: table
  target_type: column
```


```yaml
candidate_edge:
  edge_id: edge.jiomart.v9.00128.belongs_to_table
  canonical_edge_type: BELONGS_TO_TABLE
  source_card_id: column.zs_observe.jiomart_settlement.is_active
  target_card_id: table.zs_observe.jiomart_settlement
  edge_class: canonical
  canonical_cognee_edge: true
  source_type: column
  target_type: table
```


```yaml
candidate_edge:
  edge_id: edge.jiomart.v9.00129.has_column
  canonical_edge_type: HAS_COLUMN
  source_card_id: table.zs_observe.jiomart_settlement
  target_card_id: column.zs_observe.jiomart_settlement.is_duplicated
  edge_class: canonical
  canonical_cognee_edge: true
  source_type: table
  target_type: column
```


```yaml
candidate_edge:
  edge_id: edge.jiomart.v9.00130.belongs_to_table
  canonical_edge_type: BELONGS_TO_TABLE
  source_card_id: column.zs_observe.jiomart_settlement.is_duplicated
  target_card_id: table.zs_observe.jiomart_settlement
  edge_class: canonical
  canonical_cognee_edge: true
  source_type: column
  target_type: table
```


```yaml
candidate_edge:
  edge_id: edge.jiomart.v9.00131.has_column
  canonical_edge_type: HAS_COLUMN
  source_card_id: table.zs_observe.jiomart_settlement
  target_card_id: column.zs_observe.jiomart_settlement.zen_status
  edge_class: canonical
  canonical_cognee_edge: true
  source_type: table
  target_type: column
```


```yaml
candidate_edge:
  edge_id: edge.jiomart.v9.00132.belongs_to_table
  canonical_edge_type: BELONGS_TO_TABLE
  source_card_id: column.zs_observe.jiomart_settlement.zen_status
  target_card_id: table.zs_observe.jiomart_settlement
  edge_class: canonical
  canonical_cognee_edge: true
  source_type: column
  target_type: table
```


```yaml
candidate_edge:
  edge_id: edge.jiomart.v9.00133.has_column
  canonical_edge_type: HAS_COLUMN
  source_card_id: table.zs_observe.jiomart_settlement
  target_card_id: column.zs_observe.jiomart_settlement.sheetname
  edge_class: canonical
  canonical_cognee_edge: true
  source_type: table
  target_type: column
```


```yaml
candidate_edge:
  edge_id: edge.jiomart.v9.00134.belongs_to_table
  canonical_edge_type: BELONGS_TO_TABLE
  source_card_id: column.zs_observe.jiomart_settlement.sheetname
  target_card_id: table.zs_observe.jiomart_settlement
  edge_class: canonical
  canonical_cognee_edge: true
  source_type: column
  target_type: table
```


```yaml
candidate_edge:
  edge_id: edge.jiomart.v9.00135.has_column
  canonical_edge_type: HAS_COLUMN
  source_card_id: table.zs_observe.jiomart_settlement
  target_card_id: column.zs_observe.jiomart_settlement.zen_sheet_name
  edge_class: canonical
  canonical_cognee_edge: true
  source_type: table
  target_type: column
```


```yaml
candidate_edge:
  edge_id: edge.jiomart.v9.00136.belongs_to_table
  canonical_edge_type: BELONGS_TO_TABLE
  source_card_id: column.zs_observe.jiomart_settlement.zen_sheet_name
  target_card_id: table.zs_observe.jiomart_settlement
  edge_class: canonical
  canonical_cognee_edge: true
  source_type: column
  target_type: table
```


```yaml
candidate_edge:
  edge_id: edge.jiomart.v9.00137.has_column
  canonical_edge_type: HAS_COLUMN
  source_card_id: table.zs_observe.jiomart_settlement
  target_card_id: column.zs_observe.jiomart_settlement.ancestry
  edge_class: canonical
  canonical_cognee_edge: true
  source_type: table
  target_type: column
```


```yaml
candidate_edge:
  edge_id: edge.jiomart.v9.00138.belongs_to_table
  canonical_edge_type: BELONGS_TO_TABLE
  source_card_id: column.zs_observe.jiomart_settlement.ancestry
  target_card_id: table.zs_observe.jiomart_settlement
  edge_class: canonical
  canonical_cognee_edge: true
  source_type: column
  target_type: table
```


```yaml
candidate_edge:
  edge_id: edge.jiomart.v9.00139.has_column
  canonical_edge_type: HAS_COLUMN
  source_card_id: table.zs_observe.jiomart_settlement
  target_card_id: column.zs_observe.jiomart_settlement.event_temp_old
  edge_class: canonical
  canonical_cognee_edge: true
  source_type: table
  target_type: column
```


```yaml
candidate_edge:
  edge_id: edge.jiomart.v9.00140.belongs_to_table
  canonical_edge_type: BELONGS_TO_TABLE
  source_card_id: column.zs_observe.jiomart_settlement.event_temp_old
  target_card_id: table.zs_observe.jiomart_settlement
  edge_class: canonical
  canonical_cognee_edge: true
  source_type: column
  target_type: table
```


```yaml
candidate_edge:
  edge_id: edge.jiomart.v9.00141.sourced_from_platform
  canonical_edge_type: SOURCED_FROM_PLATFORM
  source_card_id: table.zs_observe.jiomart_returns
  target_card_id: platform.jiomart
  edge_class: canonical
  canonical_cognee_edge: true
  source_type: table
  target_type: platform
```


```yaml
candidate_edge:
  edge_id: edge.jiomart.v9.00142.sourced_from_platform_context
  canonical_edge_type: SOURCED_FROM_PLATFORM_CONTEXT
  source_card_id: table.zs_observe.jiomart_returns
  target_card_id: platform_context.jiomart.in
  edge_class: canonical
  canonical_cognee_edge: true
  source_type: table
  target_type: platform_context
```


```yaml
candidate_edge:
  edge_id: edge.jiomart.v9.00143.applies_to_platform_context
  canonical_edge_type: APPLIES_TO_PLATFORM_CONTEXT
  source_card_id: table.zs_observe.jiomart_returns
  target_card_id: platform_context.jiomart.in
  edge_class: canonical
  canonical_cognee_edge: true
  source_type: table
  target_type: platform_context
```


```yaml
candidate_edge:
  edge_id: edge.jiomart.v9.00144.has_column
  canonical_edge_type: HAS_COLUMN
  source_card_id: table.zs_observe.jiomart_returns
  target_card_id: column.zs_observe.jiomart_returns.unique_id
  edge_class: canonical
  canonical_cognee_edge: true
  source_type: table
  target_type: column
```


```yaml
candidate_edge:
  edge_id: edge.jiomart.v9.00145.belongs_to_table
  canonical_edge_type: BELONGS_TO_TABLE
  source_card_id: column.zs_observe.jiomart_returns.unique_id
  target_card_id: table.zs_observe.jiomart_returns
  edge_class: canonical
  canonical_cognee_edge: true
  source_type: column
  target_type: table
```


```yaml
candidate_edge:
  edge_id: edge.jiomart.v9.00146.has_column
  canonical_edge_type: HAS_COLUMN
  source_card_id: table.zs_observe.jiomart_returns
  target_card_id: column.zs_observe.jiomart_returns.txn_uuid
  edge_class: canonical
  canonical_cognee_edge: true
  source_type: table
  target_type: column
```


```yaml
candidate_edge:
  edge_id: edge.jiomart.v9.00147.belongs_to_table
  canonical_edge_type: BELONGS_TO_TABLE
  source_card_id: column.zs_observe.jiomart_returns.txn_uuid
  target_card_id: table.zs_observe.jiomart_returns
  edge_class: canonical
  canonical_cognee_edge: true
  source_type: column
  target_type: table
```


```yaml
candidate_edge:
  edge_id: edge.jiomart.v9.00148.has_column
  canonical_edge_type: HAS_COLUMN
  source_card_id: table.zs_observe.jiomart_returns
  target_card_id: column.zs_observe.jiomart_returns.unique_value
  edge_class: canonical
  canonical_cognee_edge: true
  source_type: table
  target_type: column
```


```yaml
candidate_edge:
  edge_id: edge.jiomart.v9.00149.belongs_to_table
  canonical_edge_type: BELONGS_TO_TABLE
  source_card_id: column.zs_observe.jiomart_returns.unique_value
  target_card_id: table.zs_observe.jiomart_returns
  edge_class: canonical
  canonical_cognee_edge: true
  source_type: column
  target_type: table
```


```yaml
candidate_edge:
  edge_id: edge.jiomart.v9.00150.has_column
  canonical_edge_type: HAS_COLUMN
  source_card_id: table.zs_observe.jiomart_returns
  target_card_id: column.zs_observe.jiomart_returns.invoice_number
  edge_class: canonical
  canonical_cognee_edge: true
  source_type: table
  target_type: column
```


```yaml
candidate_edge:
  edge_id: edge.jiomart.v9.00151.belongs_to_table
  canonical_edge_type: BELONGS_TO_TABLE
  source_card_id: column.zs_observe.jiomart_returns.invoice_number
  target_card_id: table.zs_observe.jiomart_returns
  edge_class: canonical
  canonical_cognee_edge: true
  source_type: column
  target_type: table
```


```yaml
candidate_edge:
  edge_id: edge.jiomart.v9.00152.has_column
  canonical_edge_type: HAS_COLUMN
  source_card_id: table.zs_observe.jiomart_returns
  target_card_id: column.zs_observe.jiomart_returns.order_id
  edge_class: canonical
  canonical_cognee_edge: true
  source_type: table
  target_type: column
```


```yaml
candidate_edge:
  edge_id: edge.jiomart.v9.00153.belongs_to_table
  canonical_edge_type: BELONGS_TO_TABLE
  source_card_id: column.zs_observe.jiomart_returns.order_id
  target_card_id: table.zs_observe.jiomart_returns
  edge_class: canonical
  canonical_cognee_edge: true
  source_type: column
  target_type: table
```


```yaml
candidate_edge:
  edge_id: edge.jiomart.v9.00154.has_column
  canonical_edge_type: HAS_COLUMN
  source_card_id: table.zs_observe.jiomart_returns
  target_card_id: column.zs_observe.jiomart_returns.item_id
  edge_class: canonical
  canonical_cognee_edge: true
  source_type: table
  target_type: column
```


```yaml
candidate_edge:
  edge_id: edge.jiomart.v9.00155.belongs_to_table
  canonical_edge_type: BELONGS_TO_TABLE
  source_card_id: column.zs_observe.jiomart_returns.item_id
  target_card_id: table.zs_observe.jiomart_returns
  edge_class: canonical
  canonical_cognee_edge: true
  source_type: column
  target_type: table
```


```yaml
candidate_edge:
  edge_id: edge.jiomart.v9.00156.has_column
  canonical_edge_type: HAS_COLUMN
  source_card_id: table.zs_observe.jiomart_returns
  target_card_id: column.zs_observe.jiomart_returns.sku_id
  edge_class: canonical
  canonical_cognee_edge: true
  source_type: table
  target_type: column
```


```yaml
candidate_edge:
  edge_id: edge.jiomart.v9.00157.belongs_to_table
  canonical_edge_type: BELONGS_TO_TABLE
  source_card_id: column.zs_observe.jiomart_returns.sku_id
  target_card_id: table.zs_observe.jiomart_returns
  edge_class: canonical
  canonical_cognee_edge: true
  source_type: column
  target_type: table
```


```yaml
candidate_edge:
  edge_id: edge.jiomart.v9.00158.has_column
  canonical_edge_type: HAS_COLUMN
  source_card_id: table.zs_observe.jiomart_returns
  target_card_id: column.zs_observe.jiomart_returns.sku
  edge_class: canonical
  canonical_cognee_edge: true
  source_type: table
  target_type: column
```


```yaml
candidate_edge:
  edge_id: edge.jiomart.v9.00159.belongs_to_table
  canonical_edge_type: BELONGS_TO_TABLE
  source_card_id: column.zs_observe.jiomart_returns.sku
  target_card_id: table.zs_observe.jiomart_returns
  edge_class: canonical
  canonical_cognee_edge: true
  source_type: column
  target_type: table
```


```yaml
candidate_edge:
  edge_id: edge.jiomart.v9.00160.has_column
  canonical_edge_type: HAS_COLUMN
  source_card_id: table.zs_observe.jiomart_returns
  target_card_id: column.zs_observe.jiomart_returns.ean
  edge_class: canonical
  canonical_cognee_edge: true
  source_type: table
  target_type: column
```


```yaml
candidate_edge:
  edge_id: edge.jiomart.v9.00161.belongs_to_table
  canonical_edge_type: BELONGS_TO_TABLE
  source_card_id: column.zs_observe.jiomart_returns.ean
  target_card_id: table.zs_observe.jiomart_returns
  edge_class: canonical
  canonical_cognee_edge: true
  source_type: column
  target_type: table
```


```yaml
candidate_edge:
  edge_id: edge.jiomart.v9.00162.has_column
  canonical_edge_type: HAS_COLUMN
  source_card_id: table.zs_observe.jiomart_returns
  target_card_id: column.zs_observe.jiomart_returns.forward_shipment_no
  edge_class: canonical
  canonical_cognee_edge: true
  source_type: table
  target_type: column
```


```yaml
candidate_edge:
  edge_id: edge.jiomart.v9.00163.belongs_to_table
  canonical_edge_type: BELONGS_TO_TABLE
  source_card_id: column.zs_observe.jiomart_returns.forward_shipment_no
  target_card_id: table.zs_observe.jiomart_returns
  edge_class: canonical
  canonical_cognee_edge: true
  source_type: column
  target_type: table
```


```yaml
candidate_edge:
  edge_id: edge.jiomart.v9.00164.has_column
  canonical_edge_type: HAS_COLUMN
  source_card_id: table.zs_observe.jiomart_returns
  target_card_id: column.zs_observe.jiomart_returns.return_awb_number
  edge_class: canonical
  canonical_cognee_edge: true
  source_type: table
  target_type: column
```


```yaml
candidate_edge:
  edge_id: edge.jiomart.v9.00165.belongs_to_table
  canonical_edge_type: BELONGS_TO_TABLE
  source_card_id: column.zs_observe.jiomart_returns.return_awb_number
  target_card_id: table.zs_observe.jiomart_returns
  edge_class: canonical
  canonical_cognee_edge: true
  source_type: column
  target_type: table
```


```yaml
candidate_edge:
  edge_id: edge.jiomart.v9.00166.has_column
  canonical_edge_type: HAS_COLUMN
  source_card_id: table.zs_observe.jiomart_returns
  target_card_id: column.zs_observe.jiomart_returns.return_awb_no
  edge_class: canonical
  canonical_cognee_edge: true
  source_type: table
  target_type: column
```


```yaml
candidate_edge:
  edge_id: edge.jiomart.v9.00167.belongs_to_table
  canonical_edge_type: BELONGS_TO_TABLE
  source_card_id: column.zs_observe.jiomart_returns.return_awb_no
  target_card_id: table.zs_observe.jiomart_returns
  edge_class: canonical
  canonical_cognee_edge: true
  source_type: column
  target_type: table
```


```yaml
candidate_edge:
  edge_id: edge.jiomart.v9.00168.has_column
  canonical_edge_type: HAS_COLUMN
  source_card_id: table.zs_observe.jiomart_returns
  target_card_id: column.zs_observe.jiomart_returns.return_shipment_no
  edge_class: canonical
  canonical_cognee_edge: true
  source_type: table
  target_type: column
```


```yaml
candidate_edge:
  edge_id: edge.jiomart.v9.00169.belongs_to_table
  canonical_edge_type: BELONGS_TO_TABLE
  source_card_id: column.zs_observe.jiomart_returns.return_shipment_no
  target_card_id: table.zs_observe.jiomart_returns
  edge_class: canonical
  canonical_cognee_edge: true
  source_type: column
  target_type: table
```


```yaml
candidate_edge:
  edge_id: edge.jiomart.v9.00170.has_column
  canonical_edge_type: HAS_COLUMN
  source_card_id: table.zs_observe.jiomart_returns
  target_card_id: column.zs_observe.jiomart_returns.created_date
  edge_class: canonical
  canonical_cognee_edge: true
  source_type: table
  target_type: column
```


```yaml
candidate_edge:
  edge_id: edge.jiomart.v9.00171.belongs_to_table
  canonical_edge_type: BELONGS_TO_TABLE
  source_card_id: column.zs_observe.jiomart_returns.created_date
  target_card_id: table.zs_observe.jiomart_returns
  edge_class: canonical
  canonical_cognee_edge: true
  source_type: column
  target_type: table
```


```yaml
candidate_edge:
  edge_id: edge.jiomart.v9.00172.has_column
  canonical_edge_type: HAS_COLUMN
  source_card_id: table.zs_observe.jiomart_returns
  target_card_id: column.zs_observe.jiomart_returns.order_date
  edge_class: canonical
  canonical_cognee_edge: true
  source_type: table
  target_type: column
```


```yaml
candidate_edge:
  edge_id: edge.jiomart.v9.00173.belongs_to_table
  canonical_edge_type: BELONGS_TO_TABLE
  source_card_id: column.zs_observe.jiomart_returns.order_date
  target_card_id: table.zs_observe.jiomart_returns
  edge_class: canonical
  canonical_cognee_edge: true
  source_type: column
  target_type: table
```


```yaml
candidate_edge:
  edge_id: edge.jiomart.v9.00174.has_column
  canonical_edge_type: HAS_COLUMN
  source_card_id: table.zs_observe.jiomart_returns
  target_card_id: column.zs_observe.jiomart_returns.return_initiate_date
  edge_class: canonical
  canonical_cognee_edge: true
  source_type: table
  target_type: column
```


```yaml
candidate_edge:
  edge_id: edge.jiomart.v9.00175.belongs_to_table
  canonical_edge_type: BELONGS_TO_TABLE
  source_card_id: column.zs_observe.jiomart_returns.return_initiate_date
  target_card_id: table.zs_observe.jiomart_returns
  edge_class: canonical
  canonical_cognee_edge: true
  source_type: column
  target_type: table
```


```yaml
candidate_edge:
  edge_id: edge.jiomart.v9.00176.has_column
  canonical_edge_type: HAS_COLUMN
  source_card_id: table.zs_observe.jiomart_returns
  target_card_id: column.zs_observe.jiomart_returns.return_date
  edge_class: canonical
  canonical_cognee_edge: true
  source_type: table
  target_type: column
```


```yaml
candidate_edge:
  edge_id: edge.jiomart.v9.00177.belongs_to_table
  canonical_edge_type: BELONGS_TO_TABLE
  source_card_id: column.zs_observe.jiomart_returns.return_date
  target_card_id: table.zs_observe.jiomart_returns
  edge_class: canonical
  canonical_cognee_edge: true
  source_type: column
  target_type: table
```


```yaml
candidate_edge:
  edge_id: edge.jiomart.v9.00178.has_column
  canonical_edge_type: HAS_COLUMN
  source_card_id: table.zs_observe.jiomart_returns
  target_card_id: column.zs_observe.jiomart_returns.return_delivery_date
  edge_class: canonical
  canonical_cognee_edge: true
  source_type: table
  target_type: column
```


```yaml
candidate_edge:
  edge_id: edge.jiomart.v9.00179.belongs_to_table
  canonical_edge_type: BELONGS_TO_TABLE
  source_card_id: column.zs_observe.jiomart_returns.return_delivery_date
  target_card_id: table.zs_observe.jiomart_returns
  edge_class: canonical
  canonical_cognee_edge: true
  source_type: column
  target_type: table
```


```yaml
candidate_edge:
  edge_id: edge.jiomart.v9.00180.has_column
  canonical_edge_type: HAS_COLUMN
  source_card_id: table.zs_observe.jiomart_returns
  target_card_id: column.zs_observe.jiomart_returns.forward_delivery_date
  edge_class: canonical
  canonical_cognee_edge: true
  source_type: table
  target_type: column
```


```yaml
candidate_edge:
  edge_id: edge.jiomart.v9.00181.belongs_to_table
  canonical_edge_type: BELONGS_TO_TABLE
  source_card_id: column.zs_observe.jiomart_returns.forward_delivery_date
  target_card_id: table.zs_observe.jiomart_returns
  edge_class: canonical
  canonical_cognee_edge: true
  source_type: column
  target_type: table
```


```yaml
candidate_edge:
  edge_id: edge.jiomart.v9.00182.has_column
  canonical_edge_type: HAS_COLUMN
  source_card_id: table.zs_observe.jiomart_returns
  target_card_id: column.zs_observe.jiomart_returns.charged_amount
  edge_class: canonical
  canonical_cognee_edge: true
  source_type: table
  target_type: column
```


```yaml
candidate_edge:
  edge_id: edge.jiomart.v9.00183.belongs_to_table
  canonical_edge_type: BELONGS_TO_TABLE
  source_card_id: column.zs_observe.jiomart_returns.charged_amount
  target_card_id: table.zs_observe.jiomart_returns
  edge_class: canonical
  canonical_cognee_edge: true
  source_type: column
  target_type: table
```


```yaml
candidate_edge:
  edge_id: edge.jiomart.v9.00184.has_column
  canonical_edge_type: HAS_COLUMN
  source_card_id: table.zs_observe.jiomart_returns
  target_card_id: column.zs_observe.jiomart_returns.refund_amount
  edge_class: canonical
  canonical_cognee_edge: true
  source_type: table
  target_type: column
```


```yaml
candidate_edge:
  edge_id: edge.jiomart.v9.00185.belongs_to_table
  canonical_edge_type: BELONGS_TO_TABLE
  source_card_id: column.zs_observe.jiomart_returns.refund_amount
  target_card_id: table.zs_observe.jiomart_returns
  edge_class: canonical
  canonical_cognee_edge: true
  source_type: column
  target_type: table
```


```yaml
candidate_edge:
  edge_id: edge.jiomart.v9.00186.has_column
  canonical_edge_type: HAS_COLUMN
  source_card_id: table.zs_observe.jiomart_returns
  target_card_id: column.zs_observe.jiomart_returns.invoice_amount
  edge_class: canonical
  canonical_cognee_edge: true
  source_type: table
  target_type: column
```


```yaml
candidate_edge:
  edge_id: edge.jiomart.v9.00187.belongs_to_table
  canonical_edge_type: BELONGS_TO_TABLE
  source_card_id: column.zs_observe.jiomart_returns.invoice_amount
  target_card_id: table.zs_observe.jiomart_returns
  edge_class: canonical
  canonical_cognee_edge: true
  source_type: column
  target_type: table
```


```yaml
candidate_edge:
  edge_id: edge.jiomart.v9.00188.has_column
  canonical_edge_type: HAS_COLUMN
  source_card_id: table.zs_observe.jiomart_returns
  target_card_id: column.zs_observe.jiomart_returns.pre_delivery_claims
  edge_class: canonical
  canonical_cognee_edge: true
  source_type: table
  target_type: column
```


```yaml
candidate_edge:
  edge_id: edge.jiomart.v9.00189.belongs_to_table
  canonical_edge_type: BELONGS_TO_TABLE
  source_card_id: column.zs_observe.jiomart_returns.pre_delivery_claims
  target_card_id: table.zs_observe.jiomart_returns
  edge_class: canonical
  canonical_cognee_edge: true
  source_type: column
  target_type: table
```


```yaml
candidate_edge:
  edge_id: edge.jiomart.v9.00190.has_column
  canonical_edge_type: HAS_COLUMN
  source_card_id: table.zs_observe.jiomart_returns
  target_card_id: column.zs_observe.jiomart_returns.post_delivery_claims
  edge_class: canonical
  canonical_cognee_edge: true
  source_type: table
  target_type: column
```


```yaml
candidate_edge:
  edge_id: edge.jiomart.v9.00191.belongs_to_table
  canonical_edge_type: BELONGS_TO_TABLE
  source_card_id: column.zs_observe.jiomart_returns.post_delivery_claims
  target_card_id: table.zs_observe.jiomart_returns
  edge_class: canonical
  canonical_cognee_edge: true
  source_type: column
  target_type: table
```


```yaml
candidate_edge:
  edge_id: edge.jiomart.v9.00192.has_column
  canonical_edge_type: HAS_COLUMN
  source_card_id: table.zs_observe.jiomart_returns
  target_card_id: column.zs_observe.jiomart_returns.transaction_type
  edge_class: canonical
  canonical_cognee_edge: true
  source_type: table
  target_type: column
```


```yaml
candidate_edge:
  edge_id: edge.jiomart.v9.00193.belongs_to_table
  canonical_edge_type: BELONGS_TO_TABLE
  source_card_id: column.zs_observe.jiomart_returns.transaction_type
  target_card_id: table.zs_observe.jiomart_returns
  edge_class: canonical
  canonical_cognee_edge: true
  source_type: column
  target_type: table
```


```yaml
candidate_edge:
  edge_id: edge.jiomart.v9.00194.has_column
  canonical_edge_type: HAS_COLUMN
  source_card_id: table.zs_observe.jiomart_returns
  target_card_id: column.zs_observe.jiomart_returns.return_type
  edge_class: canonical
  canonical_cognee_edge: true
  source_type: table
  target_type: column
```


```yaml
candidate_edge:
  edge_id: edge.jiomart.v9.00195.belongs_to_table
  canonical_edge_type: BELONGS_TO_TABLE
  source_card_id: column.zs_observe.jiomart_returns.return_type
  target_card_id: table.zs_observe.jiomart_returns
  edge_class: canonical
  canonical_cognee_edge: true
  source_type: column
  target_type: table
```


```yaml
candidate_edge:
  edge_id: edge.jiomart.v9.00196.has_column
  canonical_edge_type: HAS_COLUMN
  source_card_id: table.zs_observe.jiomart_returns
  target_card_id: column.zs_observe.jiomart_returns.return_status
  edge_class: canonical
  canonical_cognee_edge: true
  source_type: table
  target_type: column
```


```yaml
candidate_edge:
  edge_id: edge.jiomart.v9.00197.belongs_to_table
  canonical_edge_type: BELONGS_TO_TABLE
  source_card_id: column.zs_observe.jiomart_returns.return_status
  target_card_id: table.zs_observe.jiomart_returns
  edge_class: canonical
  canonical_cognee_edge: true
  source_type: column
  target_type: table
```


```yaml
candidate_edge:
  edge_id: edge.jiomart.v9.00198.has_column
  canonical_edge_type: HAS_COLUMN
  source_card_id: table.zs_observe.jiomart_returns
  target_card_id: column.zs_observe.jiomart_returns.order_status
  edge_class: canonical
  canonical_cognee_edge: true
  source_type: table
  target_type: column
```


```yaml
candidate_edge:
  edge_id: edge.jiomart.v9.00199.belongs_to_table
  canonical_edge_type: BELONGS_TO_TABLE
  source_card_id: column.zs_observe.jiomart_returns.order_status
  target_card_id: table.zs_observe.jiomart_returns
  edge_class: canonical
  canonical_cognee_edge: true
  source_type: column
  target_type: table
```


```yaml
candidate_edge:
  edge_id: edge.jiomart.v9.00200.has_column
  canonical_edge_type: HAS_COLUMN
  source_card_id: table.zs_observe.jiomart_returns
  target_card_id: column.zs_observe.jiomart_returns.payment_mode
  edge_class: canonical
  canonical_cognee_edge: true
  source_type: table
  target_type: column
```


```yaml
candidate_edge:
  edge_id: edge.jiomart.v9.00201.belongs_to_table
  canonical_edge_type: BELONGS_TO_TABLE
  source_card_id: column.zs_observe.jiomart_returns.payment_mode
  target_card_id: table.zs_observe.jiomart_returns
  edge_class: canonical
  canonical_cognee_edge: true
  source_type: column
  target_type: table
```


```yaml
candidate_edge:
  edge_id: edge.jiomart.v9.00202.has_column
  canonical_edge_type: HAS_COLUMN
  source_card_id: table.zs_observe.jiomart_returns
  target_card_id: column.zs_observe.jiomart_returns.payment_method
  edge_class: canonical
  canonical_cognee_edge: true
  source_type: table
  target_type: column
```


```yaml
candidate_edge:
  edge_id: edge.jiomart.v9.00203.belongs_to_table
  canonical_edge_type: BELONGS_TO_TABLE
  source_card_id: column.zs_observe.jiomart_returns.payment_method
  target_card_id: table.zs_observe.jiomart_returns
  edge_class: canonical
  canonical_cognee_edge: true
  source_type: column
  target_type: table
```


```yaml
candidate_edge:
  edge_id: edge.jiomart.v9.00204.has_column
  canonical_edge_type: HAS_COLUMN
  source_card_id: table.zs_observe.jiomart_returns
  target_card_id: column.zs_observe.jiomart_returns.reason
  edge_class: canonical
  canonical_cognee_edge: true
  source_type: table
  target_type: column
```


```yaml
candidate_edge:
  edge_id: edge.jiomart.v9.00205.belongs_to_table
  canonical_edge_type: BELONGS_TO_TABLE
  source_card_id: column.zs_observe.jiomart_returns.reason
  target_card_id: table.zs_observe.jiomart_returns
  edge_class: canonical
  canonical_cognee_edge: true
  source_type: column
  target_type: table
```


```yaml
candidate_edge:
  edge_id: edge.jiomart.v9.00206.has_column
  canonical_edge_type: HAS_COLUMN
  source_card_id: table.zs_observe.jiomart_returns
  target_card_id: column.zs_observe.jiomart_returns.quantity
  edge_class: canonical
  canonical_cognee_edge: true
  source_type: table
  target_type: column
```


```yaml
candidate_edge:
  edge_id: edge.jiomart.v9.00207.belongs_to_table
  canonical_edge_type: BELONGS_TO_TABLE
  source_card_id: column.zs_observe.jiomart_returns.quantity
  target_card_id: table.zs_observe.jiomart_returns
  edge_class: canonical
  canonical_cognee_edge: true
  source_type: column
  target_type: table
```


```yaml
candidate_edge:
  edge_id: edge.jiomart.v9.00208.has_column
  canonical_edge_type: HAS_COLUMN
  source_card_id: table.zs_observe.jiomart_returns
  target_card_id: column.zs_observe.jiomart_returns.qty
  edge_class: canonical
  canonical_cognee_edge: true
  source_type: table
  target_type: column
```


```yaml
candidate_edge:
  edge_id: edge.jiomart.v9.00209.belongs_to_table
  canonical_edge_type: BELONGS_TO_TABLE
  source_card_id: column.zs_observe.jiomart_returns.qty
  target_card_id: table.zs_observe.jiomart_returns
  edge_class: canonical
  canonical_cognee_edge: true
  source_type: column
  target_type: table
```


```yaml
candidate_edge:
  edge_id: edge.jiomart.v9.00210.has_column
  canonical_edge_type: HAS_COLUMN
  source_card_id: table.zs_observe.jiomart_returns
  target_card_id: column.zs_observe.jiomart_returns.courier_partner
  edge_class: canonical
  canonical_cognee_edge: true
  source_type: table
  target_type: column
```


```yaml
candidate_edge:
  edge_id: edge.jiomart.v9.00211.belongs_to_table
  canonical_edge_type: BELONGS_TO_TABLE
  source_card_id: column.zs_observe.jiomart_returns.courier_partner
  target_card_id: table.zs_observe.jiomart_returns
  edge_class: canonical
  canonical_cognee_edge: true
  source_type: column
  target_type: table
```


```yaml
candidate_edge:
  edge_id: edge.jiomart.v9.00212.has_column
  canonical_edge_type: HAS_COLUMN
  source_card_id: table.zs_observe.jiomart_returns
  target_card_id: column.zs_observe.jiomart_returns.fulfillment_channel
  edge_class: canonical
  canonical_cognee_edge: true
  source_type: table
  target_type: column
```


```yaml
candidate_edge:
  edge_id: edge.jiomart.v9.00213.belongs_to_table
  canonical_edge_type: BELONGS_TO_TABLE
  source_card_id: column.zs_observe.jiomart_returns.fulfillment_channel
  target_card_id: table.zs_observe.jiomart_returns
  edge_class: canonical
  canonical_cognee_edge: true
  source_type: column
  target_type: table
```


```yaml
candidate_edge:
  edge_id: edge.jiomart.v9.00214.has_column
  canonical_edge_type: HAS_COLUMN
  source_card_id: table.zs_observe.jiomart_returns
  target_card_id: column.zs_observe.jiomart_returns.fulfillment_center
  edge_class: canonical
  canonical_cognee_edge: true
  source_type: table
  target_type: column
```


```yaml
candidate_edge:
  edge_id: edge.jiomart.v9.00215.belongs_to_table
  canonical_edge_type: BELONGS_TO_TABLE
  source_card_id: column.zs_observe.jiomart_returns.fulfillment_center
  target_card_id: table.zs_observe.jiomart_returns
  edge_class: canonical
  canonical_cognee_edge: true
  source_type: column
  target_type: table
```


```yaml
candidate_edge:
  edge_id: edge.jiomart.v9.00216.has_column
  canonical_edge_type: HAS_COLUMN
  source_card_id: table.zs_observe.jiomart_returns
  target_card_id: column.zs_observe.jiomart_returns.description
  edge_class: canonical
  canonical_cognee_edge: true
  source_type: table
  target_type: column
```


```yaml
candidate_edge:
  edge_id: edge.jiomart.v9.00217.belongs_to_table
  canonical_edge_type: BELONGS_TO_TABLE
  source_card_id: column.zs_observe.jiomart_returns.description
  target_card_id: table.zs_observe.jiomart_returns
  edge_class: canonical
  canonical_cognee_edge: true
  source_type: column
  target_type: table
```


```yaml
candidate_edge:
  edge_id: edge.jiomart.v9.00218.has_column
  canonical_edge_type: HAS_COLUMN
  source_card_id: table.zs_observe.jiomart_returns
  target_card_id: column.zs_observe.jiomart_returns.product_title
  edge_class: canonical
  canonical_cognee_edge: true
  source_type: table
  target_type: column
```


```yaml
candidate_edge:
  edge_id: edge.jiomart.v9.00219.belongs_to_table
  canonical_edge_type: BELONGS_TO_TABLE
  source_card_id: column.zs_observe.jiomart_returns.product_title
  target_card_id: table.zs_observe.jiomart_returns
  edge_class: canonical
  canonical_cognee_edge: true
  source_type: column
  target_type: table
```


```yaml
candidate_edge:
  edge_id: edge.jiomart.v9.00220.has_column
  canonical_edge_type: HAS_COLUMN
  source_card_id: table.zs_observe.jiomart_returns
  target_card_id: column.zs_observe.jiomart_returns.group_level_id
  edge_class: canonical
  canonical_cognee_edge: true
  source_type: table
  target_type: column
```


```yaml
candidate_edge:
  edge_id: edge.jiomart.v9.00221.belongs_to_table
  canonical_edge_type: BELONGS_TO_TABLE
  source_card_id: column.zs_observe.jiomart_returns.group_level_id
  target_card_id: table.zs_observe.jiomart_returns
  edge_class: canonical
  canonical_cognee_edge: true
  source_type: column
  target_type: table
```


```yaml
candidate_edge:
  edge_id: edge.jiomart.v9.00222.has_column
  canonical_edge_type: HAS_COLUMN
  source_card_id: table.zs_observe.jiomart_returns
  target_card_id: column.zs_observe.jiomart_returns.currency_type
  edge_class: canonical
  canonical_cognee_edge: true
  source_type: table
  target_type: column
```


```yaml
candidate_edge:
  edge_id: edge.jiomart.v9.00223.belongs_to_table
  canonical_edge_type: BELONGS_TO_TABLE
  source_card_id: column.zs_observe.jiomart_returns.currency_type
  target_card_id: table.zs_observe.jiomart_returns
  edge_class: canonical
  canonical_cognee_edge: true
  source_type: column
  target_type: table
```


```yaml
candidate_edge:
  edge_id: edge.jiomart.v9.00224.has_column
  canonical_edge_type: HAS_COLUMN
  source_card_id: table.zs_observe.jiomart_returns
  target_card_id: column.zs_observe.jiomart_returns.is_active
  edge_class: canonical
  canonical_cognee_edge: true
  source_type: table
  target_type: column
```


```yaml
candidate_edge:
  edge_id: edge.jiomart.v9.00225.belongs_to_table
  canonical_edge_type: BELONGS_TO_TABLE
  source_card_id: column.zs_observe.jiomart_returns.is_active
  target_card_id: table.zs_observe.jiomart_returns
  edge_class: canonical
  canonical_cognee_edge: true
  source_type: column
  target_type: table
```


```yaml
candidate_edge:
  edge_id: edge.jiomart.v9.00226.has_column
  canonical_edge_type: HAS_COLUMN
  source_card_id: table.zs_observe.jiomart_returns
  target_card_id: column.zs_observe.jiomart_returns.zen_sheet_name
  edge_class: canonical
  canonical_cognee_edge: true
  source_type: table
  target_type: column
```


```yaml
candidate_edge:
  edge_id: edge.jiomart.v9.00227.belongs_to_table
  canonical_edge_type: BELONGS_TO_TABLE
  source_card_id: column.zs_observe.jiomart_returns.zen_sheet_name
  target_card_id: table.zs_observe.jiomart_returns
  edge_class: canonical
  canonical_cognee_edge: true
  source_type: column
  target_type: table
```


```yaml
candidate_edge:
  edge_id: edge.jiomart.v9.00228.has_column
  canonical_edge_type: HAS_COLUMN
  source_card_id: table.zs_observe.jiomart_returns
  target_card_id: column.zs_observe.jiomart_returns.ancestry
  edge_class: canonical
  canonical_cognee_edge: true
  source_type: table
  target_type: column
```


```yaml
candidate_edge:
  edge_id: edge.jiomart.v9.00229.belongs_to_table
  canonical_edge_type: BELONGS_TO_TABLE
  source_card_id: column.zs_observe.jiomart_returns.ancestry
  target_card_id: table.zs_observe.jiomart_returns
  edge_class: canonical
  canonical_cognee_edge: true
  source_type: column
  target_type: table
```


```yaml
candidate_edge:
  edge_id: edge.jiomart.v9.00230.sourced_from_platform
  canonical_edge_type: SOURCED_FROM_PLATFORM
  source_card_id: table.zs_observe.jiomart_oms
  target_card_id: platform.jiomart
  edge_class: canonical
  canonical_cognee_edge: true
  source_type: table
  target_type: platform
```


```yaml
candidate_edge:
  edge_id: edge.jiomart.v9.00231.sourced_from_platform_context
  canonical_edge_type: SOURCED_FROM_PLATFORM_CONTEXT
  source_card_id: table.zs_observe.jiomart_oms
  target_card_id: platform_context.jiomart.in
  edge_class: canonical
  canonical_cognee_edge: true
  source_type: table
  target_type: platform_context
```


```yaml
candidate_edge:
  edge_id: edge.jiomart.v9.00232.applies_to_platform_context
  canonical_edge_type: APPLIES_TO_PLATFORM_CONTEXT
  source_card_id: table.zs_observe.jiomart_oms
  target_card_id: platform_context.jiomart.in
  edge_class: canonical
  canonical_cognee_edge: true
  source_type: table
  target_type: platform_context
```


```yaml
candidate_edge:
  edge_id: edge.jiomart.v9.00233.has_column
  canonical_edge_type: HAS_COLUMN
  source_card_id: table.zs_observe.jiomart_oms
  target_card_id: column.zs_observe.jiomart_oms.unique_id
  edge_class: canonical
  canonical_cognee_edge: true
  source_type: table
  target_type: column
```


```yaml
candidate_edge:
  edge_id: edge.jiomart.v9.00234.belongs_to_table
  canonical_edge_type: BELONGS_TO_TABLE
  source_card_id: column.zs_observe.jiomart_oms.unique_id
  target_card_id: table.zs_observe.jiomart_oms
  edge_class: canonical
  canonical_cognee_edge: true
  source_type: column
  target_type: table
```


```yaml
candidate_edge:
  edge_id: edge.jiomart.v9.00235.has_column
  canonical_edge_type: HAS_COLUMN
  source_card_id: table.zs_observe.jiomart_oms
  target_card_id: column.zs_observe.jiomart_oms.txn_uuid
  edge_class: canonical
  canonical_cognee_edge: true
  source_type: table
  target_type: column
```


```yaml
candidate_edge:
  edge_id: edge.jiomart.v9.00236.belongs_to_table
  canonical_edge_type: BELONGS_TO_TABLE
  source_card_id: column.zs_observe.jiomart_oms.txn_uuid
  target_card_id: table.zs_observe.jiomart_oms
  edge_class: canonical
  canonical_cognee_edge: true
  source_type: column
  target_type: table
```


```yaml
candidate_edge:
  edge_id: edge.jiomart.v9.00237.has_column
  canonical_edge_type: HAS_COLUMN
  source_card_id: table.zs_observe.jiomart_oms
  target_card_id: column.zs_observe.jiomart_oms.unique_value
  edge_class: canonical
  canonical_cognee_edge: true
  source_type: table
  target_type: column
```


```yaml
candidate_edge:
  edge_id: edge.jiomart.v9.00238.belongs_to_table
  canonical_edge_type: BELONGS_TO_TABLE
  source_card_id: column.zs_observe.jiomart_oms.unique_value
  target_card_id: table.zs_observe.jiomart_oms
  edge_class: canonical
  canonical_cognee_edge: true
  source_type: column
  target_type: table
```


```yaml
candidate_edge:
  edge_id: edge.jiomart.v9.00239.has_column
  canonical_edge_type: HAS_COLUMN
  source_card_id: table.zs_observe.jiomart_oms
  target_card_id: column.zs_observe.jiomart_oms.invoice_number
  edge_class: canonical
  canonical_cognee_edge: true
  source_type: table
  target_type: column
```


```yaml
candidate_edge:
  edge_id: edge.jiomart.v9.00240.belongs_to_table
  canonical_edge_type: BELONGS_TO_TABLE
  source_card_id: column.zs_observe.jiomart_oms.invoice_number
  target_card_id: table.zs_observe.jiomart_oms
  edge_class: canonical
  canonical_cognee_edge: true
  source_type: column
  target_type: table
```


```yaml
candidate_edge:
  edge_id: edge.jiomart.v9.00241.has_column
  canonical_edge_type: HAS_COLUMN
  source_card_id: table.zs_observe.jiomart_oms
  target_card_id: column.zs_observe.jiomart_oms.original_invoice_id
  edge_class: canonical
  canonical_cognee_edge: true
  source_type: table
  target_type: column
```


```yaml
candidate_edge:
  edge_id: edge.jiomart.v9.00242.belongs_to_table
  canonical_edge_type: BELONGS_TO_TABLE
  source_card_id: column.zs_observe.jiomart_oms.original_invoice_id
  target_card_id: table.zs_observe.jiomart_oms
  edge_class: canonical
  canonical_cognee_edge: true
  source_type: column
  target_type: table
```


```yaml
candidate_edge:
  edge_id: edge.jiomart.v9.00243.has_column
  canonical_edge_type: HAS_COLUMN
  source_card_id: table.zs_observe.jiomart_oms
  target_card_id: column.zs_observe.jiomart_oms.buyer_invoice_id
  edge_class: canonical
  canonical_cognee_edge: true
  source_type: table
  target_type: column
```


```yaml
candidate_edge:
  edge_id: edge.jiomart.v9.00244.belongs_to_table
  canonical_edge_type: BELONGS_TO_TABLE
  source_card_id: column.zs_observe.jiomart_oms.buyer_invoice_id
  target_card_id: table.zs_observe.jiomart_oms
  edge_class: canonical
  canonical_cognee_edge: true
  source_type: column
  target_type: table
```


```yaml
candidate_edge:
  edge_id: edge.jiomart.v9.00245.has_column
  canonical_edge_type: HAS_COLUMN
  source_card_id: table.zs_observe.jiomart_oms
  target_card_id: column.zs_observe.jiomart_oms.order_id
  edge_class: canonical
  canonical_cognee_edge: true
  source_type: table
  target_type: column
```


```yaml
candidate_edge:
  edge_id: edge.jiomart.v9.00246.belongs_to_table
  canonical_edge_type: BELONGS_TO_TABLE
  source_card_id: column.zs_observe.jiomart_oms.order_id
  target_card_id: table.zs_observe.jiomart_oms
  edge_class: canonical
  canonical_cognee_edge: true
  source_type: column
  target_type: table
```


```yaml
candidate_edge:
  edge_id: edge.jiomart.v9.00247.has_column
  canonical_edge_type: HAS_COLUMN
  source_card_id: table.zs_observe.jiomart_oms
  target_card_id: column.zs_observe.jiomart_oms.item_id
  edge_class: canonical
  canonical_cognee_edge: true
  source_type: table
  target_type: column
```


```yaml
candidate_edge:
  edge_id: edge.jiomart.v9.00248.belongs_to_table
  canonical_edge_type: BELONGS_TO_TABLE
  source_card_id: column.zs_observe.jiomart_oms.item_id
  target_card_id: table.zs_observe.jiomart_oms
  edge_class: canonical
  canonical_cognee_edge: true
  source_type: column
  target_type: table
```


```yaml
candidate_edge:
  edge_id: edge.jiomart.v9.00249.has_column
  canonical_edge_type: HAS_COLUMN
  source_card_id: table.zs_observe.jiomart_oms
  target_card_id: column.zs_observe.jiomart_oms.order_item_id
  edge_class: canonical
  canonical_cognee_edge: true
  source_type: table
  target_type: column
```


```yaml
candidate_edge:
  edge_id: edge.jiomart.v9.00250.belongs_to_table
  canonical_edge_type: BELONGS_TO_TABLE
  source_card_id: column.zs_observe.jiomart_oms.order_item_id
  target_card_id: table.zs_observe.jiomart_oms
  edge_class: canonical
  canonical_cognee_edge: true
  source_type: column
  target_type: table
```


```yaml
candidate_edge:
  edge_id: edge.jiomart.v9.00251.has_column
  canonical_edge_type: HAS_COLUMN
  source_card_id: table.zs_observe.jiomart_oms
  target_card_id: column.zs_observe.jiomart_oms.parent_id
  edge_class: canonical
  canonical_cognee_edge: true
  source_type: table
  target_type: column
```


```yaml
candidate_edge:
  edge_id: edge.jiomart.v9.00252.belongs_to_table
  canonical_edge_type: BELONGS_TO_TABLE
  source_card_id: column.zs_observe.jiomart_oms.parent_id
  target_card_id: table.zs_observe.jiomart_oms
  edge_class: canonical
  canonical_cognee_edge: true
  source_type: column
  target_type: table
```


```yaml
candidate_edge:
  edge_id: edge.jiomart.v9.00253.has_column
  canonical_edge_type: HAS_COLUMN
  source_card_id: table.zs_observe.jiomart_oms
  target_card_id: column.zs_observe.jiomart_oms.shipment_number
  edge_class: canonical
  canonical_cognee_edge: true
  source_type: table
  target_type: column
```


```yaml
candidate_edge:
  edge_id: edge.jiomart.v9.00254.belongs_to_table
  canonical_edge_type: BELONGS_TO_TABLE
  source_card_id: column.zs_observe.jiomart_oms.shipment_number
  target_card_id: table.zs_observe.jiomart_oms
  edge_class: canonical
  canonical_cognee_edge: true
  source_type: column
  target_type: table
```


```yaml
candidate_edge:
  edge_id: edge.jiomart.v9.00255.has_column
  canonical_edge_type: HAS_COLUMN
  source_card_id: table.zs_observe.jiomart_oms
  target_card_id: column.zs_observe.jiomart_oms.original_shipment_number
  edge_class: canonical
  canonical_cognee_edge: true
  source_type: table
  target_type: column
```


```yaml
candidate_edge:
  edge_id: edge.jiomart.v9.00256.belongs_to_table
  canonical_edge_type: BELONGS_TO_TABLE
  source_card_id: column.zs_observe.jiomart_oms.original_shipment_number
  target_card_id: table.zs_observe.jiomart_oms
  edge_class: canonical
  canonical_cognee_edge: true
  source_type: column
  target_type: table
```


```yaml
candidate_edge:
  edge_id: edge.jiomart.v9.00257.has_column
  canonical_edge_type: HAS_COLUMN
  source_card_id: table.zs_observe.jiomart_oms
  target_card_id: column.zs_observe.jiomart_oms.mp_sin
  edge_class: canonical
  canonical_cognee_edge: true
  source_type: table
  target_type: column
```


```yaml
candidate_edge:
  edge_id: edge.jiomart.v9.00258.belongs_to_table
  canonical_edge_type: BELONGS_TO_TABLE
  source_card_id: column.zs_observe.jiomart_oms.mp_sin
  target_card_id: table.zs_observe.jiomart_oms
  edge_class: canonical
  canonical_cognee_edge: true
  source_type: column
  target_type: table
```


```yaml
candidate_edge:
  edge_id: edge.jiomart.v9.00259.has_column
  canonical_edge_type: HAS_COLUMN
  source_card_id: table.zs_observe.jiomart_oms
  target_card_id: column.zs_observe.jiomart_oms.sku_id
  edge_class: canonical
  canonical_cognee_edge: true
  source_type: table
  target_type: column
```


```yaml
candidate_edge:
  edge_id: edge.jiomart.v9.00260.belongs_to_table
  canonical_edge_type: BELONGS_TO_TABLE
  source_card_id: column.zs_observe.jiomart_oms.sku_id
  target_card_id: table.zs_observe.jiomart_oms
  edge_class: canonical
  canonical_cognee_edge: true
  source_type: column
  target_type: table
```


```yaml
candidate_edge:
  edge_id: edge.jiomart.v9.00261.has_column
  canonical_edge_type: HAS_COLUMN
  source_card_id: table.zs_observe.jiomart_oms
  target_card_id: column.zs_observe.jiomart_oms.sku
  edge_class: canonical
  canonical_cognee_edge: true
  source_type: table
  target_type: column
```


```yaml
candidate_edge:
  edge_id: edge.jiomart.v9.00262.belongs_to_table
  canonical_edge_type: BELONGS_TO_TABLE
  source_card_id: column.zs_observe.jiomart_oms.sku
  target_card_id: table.zs_observe.jiomart_oms
  edge_class: canonical
  canonical_cognee_edge: true
  source_type: column
  target_type: table
```


```yaml
candidate_edge:
  edge_id: edge.jiomart.v9.00263.has_column
  canonical_edge_type: HAS_COLUMN
  source_card_id: table.zs_observe.jiomart_oms
  target_card_id: column.zs_observe.jiomart_oms.fsn_product_id
  edge_class: canonical
  canonical_cognee_edge: true
  source_type: table
  target_type: column
```


```yaml
candidate_edge:
  edge_id: edge.jiomart.v9.00264.belongs_to_table
  canonical_edge_type: BELONGS_TO_TABLE
  source_card_id: column.zs_observe.jiomart_oms.fsn_product_id
  target_card_id: table.zs_observe.jiomart_oms
  edge_class: canonical
  canonical_cognee_edge: true
  source_type: column
  target_type: table
```


```yaml
candidate_edge:
  edge_id: edge.jiomart.v9.00265.has_column
  canonical_edge_type: HAS_COLUMN
  source_card_id: table.zs_observe.jiomart_oms
  target_card_id: column.zs_observe.jiomart_oms.source_gst_id
  edge_class: canonical
  canonical_cognee_edge: true
  source_type: table
  target_type: column
```


```yaml
candidate_edge:
  edge_id: edge.jiomart.v9.00266.belongs_to_table
  canonical_edge_type: BELONGS_TO_TABLE
  source_card_id: column.zs_observe.jiomart_oms.source_gst_id
  target_card_id: table.zs_observe.jiomart_oms
  edge_class: canonical
  canonical_cognee_edge: true
  source_type: column
  target_type: table
```


```yaml
candidate_edge:
  edge_id: edge.jiomart.v9.00267.has_column
  canonical_edge_type: HAS_COLUMN
  source_card_id: table.zs_observe.jiomart_oms
  target_card_id: column.zs_observe.jiomart_oms.seller_gstin
  edge_class: canonical
  canonical_cognee_edge: true
  source_type: table
  target_type: column
```


```yaml
candidate_edge:
  edge_id: edge.jiomart.v9.00268.belongs_to_table
  canonical_edge_type: BELONGS_TO_TABLE
  source_card_id: column.zs_observe.jiomart_oms.seller_gstin
  target_card_id: table.zs_observe.jiomart_oms
  edge_class: canonical
  canonical_cognee_edge: true
  source_type: column
  target_type: table
```


```yaml
candidate_edge:
  edge_id: edge.jiomart.v9.00269.has_column
  canonical_edge_type: HAS_COLUMN
  source_card_id: table.zs_observe.jiomart_oms
  target_card_id: column.zs_observe.jiomart_oms.created_date
  edge_class: canonical
  canonical_cognee_edge: true
  source_type: table
  target_type: column
```


```yaml
candidate_edge:
  edge_id: edge.jiomart.v9.00270.belongs_to_table
  canonical_edge_type: BELONGS_TO_TABLE
  source_card_id: column.zs_observe.jiomart_oms.created_date
  target_card_id: table.zs_observe.jiomart_oms
  edge_class: canonical
  canonical_cognee_edge: true
  source_type: column
  target_type: table
```


```yaml
candidate_edge:
  edge_id: edge.jiomart.v9.00271.has_column
  canonical_edge_type: HAS_COLUMN
  source_card_id: table.zs_observe.jiomart_oms
  target_card_id: column.zs_observe.jiomart_oms.order_date
  edge_class: canonical
  canonical_cognee_edge: true
  source_type: table
  target_type: column
```


```yaml
candidate_edge:
  edge_id: edge.jiomart.v9.00272.belongs_to_table
  canonical_edge_type: BELONGS_TO_TABLE
  source_card_id: column.zs_observe.jiomart_oms.order_date
  target_card_id: table.zs_observe.jiomart_oms
  edge_class: canonical
  canonical_cognee_edge: true
  source_type: column
  target_type: table
```


```yaml
candidate_edge:
  edge_id: edge.jiomart.v9.00273.has_column
  canonical_edge_type: HAS_COLUMN
  source_card_id: table.zs_observe.jiomart_oms
  target_card_id: column.zs_observe.jiomart_oms.order_approval_date
  edge_class: canonical
  canonical_cognee_edge: true
  source_type: table
  target_type: column
```


```yaml
candidate_edge:
  edge_id: edge.jiomart.v9.00274.belongs_to_table
  canonical_edge_type: BELONGS_TO_TABLE
  source_card_id: column.zs_observe.jiomart_oms.order_approval_date
  target_card_id: table.zs_observe.jiomart_oms
  edge_class: canonical
  canonical_cognee_edge: true
  source_type: column
  target_type: table
```


```yaml
candidate_edge:
  edge_id: edge.jiomart.v9.00275.has_column
  canonical_edge_type: HAS_COLUMN
  source_card_id: table.zs_observe.jiomart_oms
  target_card_id: column.zs_observe.jiomart_oms.buyer_invoice_date
  edge_class: canonical
  canonical_cognee_edge: true
  source_type: table
  target_type: column
```


```yaml
candidate_edge:
  edge_id: edge.jiomart.v9.00276.belongs_to_table
  canonical_edge_type: BELONGS_TO_TABLE
  source_card_id: column.zs_observe.jiomart_oms.buyer_invoice_date
  target_card_id: table.zs_observe.jiomart_oms
  edge_class: canonical
  canonical_cognee_edge: true
  source_type: column
  target_type: table
```


```yaml
candidate_edge:
  edge_id: edge.jiomart.v9.00277.has_column
  canonical_edge_type: HAS_COLUMN
  source_card_id: table.zs_observe.jiomart_oms
  target_card_id: column.zs_observe.jiomart_oms.sale_sale_reversal_tcs_date
  edge_class: canonical
  canonical_cognee_edge: true
  source_type: table
  target_type: column
```


```yaml
candidate_edge:
  edge_id: edge.jiomart.v9.00278.belongs_to_table
  canonical_edge_type: BELONGS_TO_TABLE
  source_card_id: column.zs_observe.jiomart_oms.sale_sale_reversal_tcs_date
  target_card_id: table.zs_observe.jiomart_oms
  edge_class: canonical
  canonical_cognee_edge: true
  source_type: column
  target_type: table
```


```yaml
candidate_edge:
  edge_id: edge.jiomart.v9.00279.has_column
  canonical_edge_type: HAS_COLUMN
  source_card_id: table.zs_observe.jiomart_oms
  target_card_id: column.zs_observe.jiomart_oms.charged_amount
  edge_class: canonical
  canonical_cognee_edge: true
  source_type: table
  target_type: column
```


```yaml
candidate_edge:
  edge_id: edge.jiomart.v9.00280.belongs_to_table
  canonical_edge_type: BELONGS_TO_TABLE
  source_card_id: column.zs_observe.jiomart_oms.charged_amount
  target_card_id: table.zs_observe.jiomart_oms
  edge_class: canonical
  canonical_cognee_edge: true
  source_type: column
  target_type: table
```


```yaml
candidate_edge:
  edge_id: edge.jiomart.v9.00281.has_column
  canonical_edge_type: HAS_COLUMN
  source_card_id: table.zs_observe.jiomart_oms
  target_card_id: column.zs_observe.jiomart_oms.charged_amount_excluding_tax
  edge_class: canonical
  canonical_cognee_edge: true
  source_type: table
  target_type: column
```


```yaml
candidate_edge:
  edge_id: edge.jiomart.v9.00282.belongs_to_table
  canonical_edge_type: BELONGS_TO_TABLE
  source_card_id: column.zs_observe.jiomart_oms.charged_amount_excluding_tax
  target_card_id: table.zs_observe.jiomart_oms
  edge_class: canonical
  canonical_cognee_edge: true
  source_type: column
  target_type: table
```


```yaml
candidate_edge:
  edge_id: edge.jiomart.v9.00283.has_column
  canonical_edge_type: HAS_COLUMN
  source_card_id: table.zs_observe.jiomart_oms
  target_card_id: column.zs_observe.jiomart_oms.taxable_value
  edge_class: canonical
  canonical_cognee_edge: true
  source_type: table
  target_type: column
```


```yaml
candidate_edge:
  edge_id: edge.jiomart.v9.00284.belongs_to_table
  canonical_edge_type: BELONGS_TO_TABLE
  source_card_id: column.zs_observe.jiomart_oms.taxable_value
  target_card_id: table.zs_observe.jiomart_oms
  edge_class: canonical
  canonical_cognee_edge: true
  source_type: column
  target_type: table
```


```yaml
candidate_edge:
  edge_id: edge.jiomart.v9.00285.has_column
  canonical_edge_type: HAS_COLUMN
  source_card_id: table.zs_observe.jiomart_oms
  target_card_id: column.zs_observe.jiomart_oms.offer_price
  edge_class: canonical
  canonical_cognee_edge: true
  source_type: table
  target_type: column
```


```yaml
candidate_edge:
  edge_id: edge.jiomart.v9.00286.belongs_to_table
  canonical_edge_type: BELONGS_TO_TABLE
  source_card_id: column.zs_observe.jiomart_oms.offer_price
  target_card_id: table.zs_observe.jiomart_oms
  edge_class: canonical
  canonical_cognee_edge: true
  source_type: column
  target_type: table
```


```yaml
candidate_edge:
  edge_id: edge.jiomart.v9.00287.has_column
  canonical_edge_type: HAS_COLUMN
  source_card_id: table.zs_observe.jiomart_oms
  target_card_id: column.zs_observe.jiomart_oms.buyer_invoice_amount
  edge_class: canonical
  canonical_cognee_edge: true
  source_type: table
  target_type: column
```


```yaml
candidate_edge:
  edge_id: edge.jiomart.v9.00288.belongs_to_table
  canonical_edge_type: BELONGS_TO_TABLE
  source_card_id: column.zs_observe.jiomart_oms.buyer_invoice_amount
  target_card_id: table.zs_observe.jiomart_oms
  edge_class: canonical
  canonical_cognee_edge: true
  source_type: column
  target_type: table
```


```yaml
candidate_edge:
  edge_id: edge.jiomart.v9.00289.has_column
  canonical_edge_type: HAS_COLUMN
  source_card_id: table.zs_observe.jiomart_oms
  target_card_id: column.zs_observe.jiomart_oms.final_invoice_amount
  edge_class: canonical
  canonical_cognee_edge: true
  source_type: table
  target_type: column
```


```yaml
candidate_edge:
  edge_id: edge.jiomart.v9.00290.belongs_to_table
  canonical_edge_type: BELONGS_TO_TABLE
  source_card_id: column.zs_observe.jiomart_oms.final_invoice_amount
  target_card_id: table.zs_observe.jiomart_oms
  edge_class: canonical
  canonical_cognee_edge: true
  source_type: column
  target_type: table
```


```yaml
candidate_edge:
  edge_id: edge.jiomart.v9.00291.has_column
  canonical_edge_type: HAS_COLUMN
  source_card_id: table.zs_observe.jiomart_oms
  target_card_id: column.zs_observe.jiomart_oms.seller_coupon_amount
  edge_class: canonical
  canonical_cognee_edge: true
  source_type: table
  target_type: column
```


```yaml
candidate_edge:
  edge_id: edge.jiomart.v9.00292.belongs_to_table
  canonical_edge_type: BELONGS_TO_TABLE
  source_card_id: column.zs_observe.jiomart_oms.seller_coupon_amount
  target_card_id: table.zs_observe.jiomart_oms
  edge_class: canonical
  canonical_cognee_edge: true
  source_type: column
  target_type: table
```


```yaml
candidate_edge:
  edge_id: edge.jiomart.v9.00293.has_column
  canonical_edge_type: HAS_COLUMN
  source_card_id: table.zs_observe.jiomart_oms
  target_card_id: column.zs_observe.jiomart_oms.tax_igst_rate
  edge_class: canonical
  canonical_cognee_edge: true
  source_type: table
  target_type: column
```


```yaml
candidate_edge:
  edge_id: edge.jiomart.v9.00294.belongs_to_table
  canonical_edge_type: BELONGS_TO_TABLE
  source_card_id: column.zs_observe.jiomart_oms.tax_igst_rate
  target_card_id: table.zs_observe.jiomart_oms
  edge_class: canonical
  canonical_cognee_edge: true
  source_type: column
  target_type: table
```


```yaml
candidate_edge:
  edge_id: edge.jiomart.v9.00295.has_column
  canonical_edge_type: HAS_COLUMN
  source_card_id: table.zs_observe.jiomart_oms
  target_card_id: column.zs_observe.jiomart_oms.tax_igst_amount
  edge_class: canonical
  canonical_cognee_edge: true
  source_type: table
  target_type: column
```


```yaml
candidate_edge:
  edge_id: edge.jiomart.v9.00296.belongs_to_table
  canonical_edge_type: BELONGS_TO_TABLE
  source_card_id: column.zs_observe.jiomart_oms.tax_igst_amount
  target_card_id: table.zs_observe.jiomart_oms
  edge_class: canonical
  canonical_cognee_edge: true
  source_type: column
  target_type: table
```


```yaml
candidate_edge:
  edge_id: edge.jiomart.v9.00297.has_column
  canonical_edge_type: HAS_COLUMN
  source_card_id: table.zs_observe.jiomart_oms
  target_card_id: column.zs_observe.jiomart_oms.tax_cgst_rate
  edge_class: canonical
  canonical_cognee_edge: true
  source_type: table
  target_type: column
```


```yaml
candidate_edge:
  edge_id: edge.jiomart.v9.00298.belongs_to_table
  canonical_edge_type: BELONGS_TO_TABLE
  source_card_id: column.zs_observe.jiomart_oms.tax_cgst_rate
  target_card_id: table.zs_observe.jiomart_oms
  edge_class: canonical
  canonical_cognee_edge: true
  source_type: column
  target_type: table
```


```yaml
candidate_edge:
  edge_id: edge.jiomart.v9.00299.has_column
  canonical_edge_type: HAS_COLUMN
  source_card_id: table.zs_observe.jiomart_oms
  target_card_id: column.zs_observe.jiomart_oms.tax_cgst_amount
  edge_class: canonical
  canonical_cognee_edge: true
  source_type: table
  target_type: column
```


```yaml
candidate_edge:
  edge_id: edge.jiomart.v9.00300.belongs_to_table
  canonical_edge_type: BELONGS_TO_TABLE
  source_card_id: column.zs_observe.jiomart_oms.tax_cgst_amount
  target_card_id: table.zs_observe.jiomart_oms
  edge_class: canonical
  canonical_cognee_edge: true
  source_type: column
  target_type: table
```


```yaml
candidate_edge:
  edge_id: edge.jiomart.v9.00301.has_column
  canonical_edge_type: HAS_COLUMN
  source_card_id: table.zs_observe.jiomart_oms
  target_card_id: column.zs_observe.jiomart_oms.tax_sgst_rate
  edge_class: canonical
  canonical_cognee_edge: true
  source_type: table
  target_type: column
```


```yaml
candidate_edge:
  edge_id: edge.jiomart.v9.00302.belongs_to_table
  canonical_edge_type: BELONGS_TO_TABLE
  source_card_id: column.zs_observe.jiomart_oms.tax_sgst_rate
  target_card_id: table.zs_observe.jiomart_oms
  edge_class: canonical
  canonical_cognee_edge: true
  source_type: column
  target_type: table
```


```yaml
candidate_edge:
  edge_id: edge.jiomart.v9.00303.has_column
  canonical_edge_type: HAS_COLUMN
  source_card_id: table.zs_observe.jiomart_oms
  target_card_id: column.zs_observe.jiomart_oms.tax_sgst_amount
  edge_class: canonical
  canonical_cognee_edge: true
  source_type: table
  target_type: column
```


```yaml
candidate_edge:
  edge_id: edge.jiomart.v9.00304.belongs_to_table
  canonical_edge_type: BELONGS_TO_TABLE
  source_card_id: column.zs_observe.jiomart_oms.tax_sgst_amount
  target_card_id: table.zs_observe.jiomart_oms
  edge_class: canonical
  canonical_cognee_edge: true
  source_type: column
  target_type: table
```


```yaml
candidate_edge:
  edge_id: edge.jiomart.v9.00305.has_column
  canonical_edge_type: HAS_COLUMN
  source_card_id: table.zs_observe.jiomart_oms
  target_card_id: column.zs_observe.jiomart_oms.type_of_tax
  edge_class: canonical
  canonical_cognee_edge: true
  source_type: table
  target_type: column
```


```yaml
candidate_edge:
  edge_id: edge.jiomart.v9.00306.belongs_to_table
  canonical_edge_type: BELONGS_TO_TABLE
  source_card_id: column.zs_observe.jiomart_oms.type_of_tax
  target_card_id: table.zs_observe.jiomart_oms
  edge_class: canonical
  canonical_cognee_edge: true
  source_type: column
  target_type: table
```


```yaml
candidate_edge:
  edge_id: edge.jiomart.v9.00307.has_column
  canonical_edge_type: HAS_COLUMN
  source_card_id: table.zs_observe.jiomart_oms
  target_card_id: column.zs_observe.jiomart_oms.hsn
  edge_class: canonical
  canonical_cognee_edge: true
  source_type: table
  target_type: column
```


```yaml
candidate_edge:
  edge_id: edge.jiomart.v9.00308.belongs_to_table
  canonical_edge_type: BELONGS_TO_TABLE
  source_card_id: column.zs_observe.jiomart_oms.hsn
  target_card_id: table.zs_observe.jiomart_oms
  edge_class: canonical
  canonical_cognee_edge: true
  source_type: column
  target_type: table
```


```yaml
candidate_edge:
  edge_id: edge.jiomart.v9.00309.has_column
  canonical_edge_type: HAS_COLUMN
  source_card_id: table.zs_observe.jiomart_oms
  target_card_id: column.zs_observe.jiomart_oms.hsn_code
  edge_class: canonical
  canonical_cognee_edge: true
  source_type: table
  target_type: column
```


```yaml
candidate_edge:
  edge_id: edge.jiomart.v9.00310.belongs_to_table
  canonical_edge_type: BELONGS_TO_TABLE
  source_card_id: column.zs_observe.jiomart_oms.hsn_code
  target_card_id: table.zs_observe.jiomart_oms
  edge_class: canonical
  canonical_cognee_edge: true
  source_type: column
  target_type: table
```


```yaml
candidate_edge:
  edge_id: edge.jiomart.v9.00311.has_column
  canonical_edge_type: HAS_COLUMN
  source_card_id: table.zs_observe.jiomart_oms
  target_card_id: column.zs_observe.jiomart_oms.hsn_generated
  edge_class: canonical
  canonical_cognee_edge: true
  source_type: table
  target_type: column
```


```yaml
candidate_edge:
  edge_id: edge.jiomart.v9.00312.belongs_to_table
  canonical_edge_type: BELONGS_TO_TABLE
  source_card_id: column.zs_observe.jiomart_oms.hsn_generated
  target_card_id: table.zs_observe.jiomart_oms
  edge_class: canonical
  canonical_cognee_edge: true
  source_type: column
  target_type: table
```


```yaml
candidate_edge:
  edge_id: edge.jiomart.v9.00313.has_column
  canonical_edge_type: HAS_COLUMN
  source_card_id: table.zs_observe.jiomart_oms
  target_card_id: column.zs_observe.jiomart_oms.igst_rate
  edge_class: canonical
  canonical_cognee_edge: true
  source_type: table
  target_type: column
```


```yaml
candidate_edge:
  edge_id: edge.jiomart.v9.00314.belongs_to_table
  canonical_edge_type: BELONGS_TO_TABLE
  source_card_id: column.zs_observe.jiomart_oms.igst_rate
  target_card_id: table.zs_observe.jiomart_oms
  edge_class: canonical
  canonical_cognee_edge: true
  source_type: column
  target_type: table
```


```yaml
candidate_edge:
  edge_id: edge.jiomart.v9.00315.has_column
  canonical_edge_type: HAS_COLUMN
  source_card_id: table.zs_observe.jiomart_oms
  target_card_id: column.zs_observe.jiomart_oms.igst_amount
  edge_class: canonical
  canonical_cognee_edge: true
  source_type: table
  target_type: column
```


```yaml
candidate_edge:
  edge_id: edge.jiomart.v9.00316.belongs_to_table
  canonical_edge_type: BELONGS_TO_TABLE
  source_card_id: column.zs_observe.jiomart_oms.igst_amount
  target_card_id: table.zs_observe.jiomart_oms
  edge_class: canonical
  canonical_cognee_edge: true
  source_type: column
  target_type: table
```


```yaml
candidate_edge:
  edge_id: edge.jiomart.v9.00317.has_column
  canonical_edge_type: HAS_COLUMN
  source_card_id: table.zs_observe.jiomart_oms
  target_card_id: column.zs_observe.jiomart_oms.cgst_rate
  edge_class: canonical
  canonical_cognee_edge: true
  source_type: table
  target_type: column
```


```yaml
candidate_edge:
  edge_id: edge.jiomart.v9.00318.belongs_to_table
  canonical_edge_type: BELONGS_TO_TABLE
  source_card_id: column.zs_observe.jiomart_oms.cgst_rate
  target_card_id: table.zs_observe.jiomart_oms
  edge_class: canonical
  canonical_cognee_edge: true
  source_type: column
  target_type: table
```


```yaml
candidate_edge:
  edge_id: edge.jiomart.v9.00319.has_column
  canonical_edge_type: HAS_COLUMN
  source_card_id: table.zs_observe.jiomart_oms
  target_card_id: column.zs_observe.jiomart_oms.cgst_amount
  edge_class: canonical
  canonical_cognee_edge: true
  source_type: table
  target_type: column
```


```yaml
candidate_edge:
  edge_id: edge.jiomart.v9.00320.belongs_to_table
  canonical_edge_type: BELONGS_TO_TABLE
  source_card_id: column.zs_observe.jiomart_oms.cgst_amount
  target_card_id: table.zs_observe.jiomart_oms
  edge_class: canonical
  canonical_cognee_edge: true
  source_type: column
  target_type: table
```


```yaml
candidate_edge:
  edge_id: edge.jiomart.v9.00321.has_column
  canonical_edge_type: HAS_COLUMN
  source_card_id: table.zs_observe.jiomart_oms
  target_card_id: column.zs_observe.jiomart_oms.sgst_rate
  edge_class: canonical
  canonical_cognee_edge: true
  source_type: table
  target_type: column
```


```yaml
candidate_edge:
  edge_id: edge.jiomart.v9.00322.belongs_to_table
  canonical_edge_type: BELONGS_TO_TABLE
  source_card_id: column.zs_observe.jiomart_oms.sgst_rate
  target_card_id: table.zs_observe.jiomart_oms
  edge_class: canonical
  canonical_cognee_edge: true
  source_type: column
  target_type: table
```


```yaml
candidate_edge:
  edge_id: edge.jiomart.v9.00323.has_column
  canonical_edge_type: HAS_COLUMN
  source_card_id: table.zs_observe.jiomart_oms
  target_card_id: column.zs_observe.jiomart_oms.sgst_amount
  edge_class: canonical
  canonical_cognee_edge: true
  source_type: table
  target_type: column
```


```yaml
candidate_edge:
  edge_id: edge.jiomart.v9.00324.belongs_to_table
  canonical_edge_type: BELONGS_TO_TABLE
  source_card_id: column.zs_observe.jiomart_oms.sgst_amount
  target_card_id: table.zs_observe.jiomart_oms
  edge_class: canonical
  canonical_cognee_edge: true
  source_type: column
  target_type: table
```


```yaml
candidate_edge:
  edge_id: edge.jiomart.v9.00325.has_column
  canonical_edge_type: HAS_COLUMN
  source_card_id: table.zs_observe.jiomart_oms
  target_card_id: column.zs_observe.jiomart_oms.tcs_igst_rate
  edge_class: canonical
  canonical_cognee_edge: true
  source_type: table
  target_type: column
```


```yaml
candidate_edge:
  edge_id: edge.jiomart.v9.00326.belongs_to_table
  canonical_edge_type: BELONGS_TO_TABLE
  source_card_id: column.zs_observe.jiomart_oms.tcs_igst_rate
  target_card_id: table.zs_observe.jiomart_oms
  edge_class: canonical
  canonical_cognee_edge: true
  source_type: column
  target_type: table
```


```yaml
candidate_edge:
  edge_id: edge.jiomart.v9.00327.has_column
  canonical_edge_type: HAS_COLUMN
  source_card_id: table.zs_observe.jiomart_oms
  target_card_id: column.zs_observe.jiomart_oms.tcs_cgst_rate
  edge_class: canonical
  canonical_cognee_edge: true
  source_type: table
  target_type: column
```


```yaml
candidate_edge:
  edge_id: edge.jiomart.v9.00328.belongs_to_table
  canonical_edge_type: BELONGS_TO_TABLE
  source_card_id: column.zs_observe.jiomart_oms.tcs_cgst_rate
  target_card_id: table.zs_observe.jiomart_oms
  edge_class: canonical
  canonical_cognee_edge: true
  source_type: column
  target_type: table
```


```yaml
candidate_edge:
  edge_id: edge.jiomart.v9.00329.has_column
  canonical_edge_type: HAS_COLUMN
  source_card_id: table.zs_observe.jiomart_oms
  target_card_id: column.zs_observe.jiomart_oms.tcs_sgst_rate
  edge_class: canonical
  canonical_cognee_edge: true
  source_type: table
  target_type: column
```


```yaml
candidate_edge:
  edge_id: edge.jiomart.v9.00330.belongs_to_table
  canonical_edge_type: BELONGS_TO_TABLE
  source_card_id: column.zs_observe.jiomart_oms.tcs_sgst_rate
  target_card_id: table.zs_observe.jiomart_oms
  edge_class: canonical
  canonical_cognee_edge: true
  source_type: column
  target_type: table
```


```yaml
candidate_edge:
  edge_id: edge.jiomart.v9.00331.has_column
  canonical_edge_type: HAS_COLUMN
  source_card_id: table.zs_observe.jiomart_oms
  target_card_id: column.zs_observe.jiomart_oms.total_tcs_amount
  edge_class: canonical
  canonical_cognee_edge: true
  source_type: table
  target_type: column
```


```yaml
candidate_edge:
  edge_id: edge.jiomart.v9.00332.belongs_to_table
  canonical_edge_type: BELONGS_TO_TABLE
  source_card_id: column.zs_observe.jiomart_oms.total_tcs_amount
  target_card_id: table.zs_observe.jiomart_oms
  edge_class: canonical
  canonical_cognee_edge: true
  source_type: column
  target_type: table
```


```yaml
candidate_edge:
  edge_id: edge.jiomart.v9.00333.has_column
  canonical_edge_type: HAS_COLUMN
  source_card_id: table.zs_observe.jiomart_oms
  target_card_id: column.zs_observe.jiomart_oms.tcs_igst_amount
  edge_class: canonical
  canonical_cognee_edge: true
  source_type: table
  target_type: column
```


```yaml
candidate_edge:
  edge_id: edge.jiomart.v9.00334.belongs_to_table
  canonical_edge_type: BELONGS_TO_TABLE
  source_card_id: column.zs_observe.jiomart_oms.tcs_igst_amount
  target_card_id: table.zs_observe.jiomart_oms
  edge_class: canonical
  canonical_cognee_edge: true
  source_type: column
  target_type: table
```


```yaml
candidate_edge:
  edge_id: edge.jiomart.v9.00335.has_column
  canonical_edge_type: HAS_COLUMN
  source_card_id: table.zs_observe.jiomart_oms
  target_card_id: column.zs_observe.jiomart_oms.tcs_cgst_amount
  edge_class: canonical
  canonical_cognee_edge: true
  source_type: table
  target_type: column
```


```yaml
candidate_edge:
  edge_id: edge.jiomart.v9.00336.belongs_to_table
  canonical_edge_type: BELONGS_TO_TABLE
  source_card_id: column.zs_observe.jiomart_oms.tcs_cgst_amount
  target_card_id: table.zs_observe.jiomart_oms
  edge_class: canonical
  canonical_cognee_edge: true
  source_type: column
  target_type: table
```


```yaml
candidate_edge:
  edge_id: edge.jiomart.v9.00337.has_column
  canonical_edge_type: HAS_COLUMN
  source_card_id: table.zs_observe.jiomart_oms
  target_card_id: column.zs_observe.jiomart_oms.tcs_sgst_amount
  edge_class: canonical
  canonical_cognee_edge: true
  source_type: table
  target_type: column
```


```yaml
candidate_edge:
  edge_id: edge.jiomart.v9.00338.belongs_to_table
  canonical_edge_type: BELONGS_TO_TABLE
  source_card_id: column.zs_observe.jiomart_oms.tcs_sgst_amount
  target_card_id: table.zs_observe.jiomart_oms
  edge_class: canonical
  canonical_cognee_edge: true
  source_type: column
  target_type: table
```


```yaml
candidate_edge:
  edge_id: edge.jiomart.v9.00339.has_column
  canonical_edge_type: HAS_COLUMN
  source_card_id: table.zs_observe.jiomart_oms
  target_card_id: column.zs_observe.jiomart_oms.total_tcs_deducted
  edge_class: canonical
  canonical_cognee_edge: true
  source_type: table
  target_type: column
```


```yaml
candidate_edge:
  edge_id: edge.jiomart.v9.00340.belongs_to_table
  canonical_edge_type: BELONGS_TO_TABLE
  source_card_id: column.zs_observe.jiomart_oms.total_tcs_deducted
  target_card_id: table.zs_observe.jiomart_oms
  edge_class: canonical
  canonical_cognee_edge: true
  source_type: column
  target_type: table
```


```yaml
candidate_edge:
  edge_id: edge.jiomart.v9.00341.has_column
  canonical_edge_type: HAS_COLUMN
  source_card_id: table.zs_observe.jiomart_oms
  target_card_id: column.zs_observe.jiomart_oms.total_tds
  edge_class: canonical
  canonical_cognee_edge: true
  source_type: table
  target_type: column
```


```yaml
candidate_edge:
  edge_id: edge.jiomart.v9.00342.belongs_to_table
  canonical_edge_type: BELONGS_TO_TABLE
  source_card_id: column.zs_observe.jiomart_oms.total_tds
  target_card_id: table.zs_observe.jiomart_oms
  edge_class: canonical
  canonical_cognee_edge: true
  source_type: column
  target_type: table
```


```yaml
candidate_edge:
  edge_id: edge.jiomart.v9.00343.has_column
  canonical_edge_type: HAS_COLUMN
  source_card_id: table.zs_observe.jiomart_oms
  target_card_id: column.zs_observe.jiomart_oms.tds_194o_rate
  edge_class: canonical
  canonical_cognee_edge: true
  source_type: table
  target_type: column
```


```yaml
candidate_edge:
  edge_id: edge.jiomart.v9.00344.belongs_to_table
  canonical_edge_type: BELONGS_TO_TABLE
  source_card_id: column.zs_observe.jiomart_oms.tds_194o_rate
  target_card_id: table.zs_observe.jiomart_oms
  edge_class: canonical
  canonical_cognee_edge: true
  source_type: column
  target_type: table
```


```yaml
candidate_edge:
  edge_id: edge.jiomart.v9.00345.has_column
  canonical_edge_type: HAS_COLUMN
  source_card_id: table.zs_observe.jiomart_oms
  target_card_id: column.zs_observe.jiomart_oms.tds_194o_amount
  edge_class: canonical
  canonical_cognee_edge: true
  source_type: table
  target_type: column
```


```yaml
candidate_edge:
  edge_id: edge.jiomart.v9.00346.belongs_to_table
  canonical_edge_type: BELONGS_TO_TABLE
  source_card_id: column.zs_observe.jiomart_oms.tds_194o_amount
  target_card_id: table.zs_observe.jiomart_oms
  edge_class: canonical
  canonical_cognee_edge: true
  source_type: column
  target_type: table
```


```yaml
candidate_edge:
  edge_id: edge.jiomart.v9.00347.has_column
  canonical_edge_type: HAS_COLUMN
  source_card_id: table.zs_observe.jiomart_oms
  target_card_id: column.zs_observe.jiomart_oms.transaction_type
  edge_class: canonical
  canonical_cognee_edge: true
  source_type: table
  target_type: column
```


```yaml
candidate_edge:
  edge_id: edge.jiomart.v9.00348.belongs_to_table
  canonical_edge_type: BELONGS_TO_TABLE
  source_card_id: column.zs_observe.jiomart_oms.transaction_type
  target_card_id: table.zs_observe.jiomart_oms
  edge_class: canonical
  canonical_cognee_edge: true
  source_type: column
  target_type: table
```


```yaml
candidate_edge:
  edge_id: edge.jiomart.v9.00349.has_column
  canonical_edge_type: HAS_COLUMN
  source_card_id: table.zs_observe.jiomart_oms
  target_card_id: column.zs_observe.jiomart_oms.order_status
  edge_class: canonical
  canonical_cognee_edge: true
  source_type: table
  target_type: column
```


```yaml
candidate_edge:
  edge_id: edge.jiomart.v9.00350.belongs_to_table
  canonical_edge_type: BELONGS_TO_TABLE
  source_card_id: column.zs_observe.jiomart_oms.order_status
  target_card_id: table.zs_observe.jiomart_oms
  edge_class: canonical
  canonical_cognee_edge: true
  source_type: column
  target_type: table
```


```yaml
candidate_edge:
  edge_id: edge.jiomart.v9.00351.has_column
  canonical_edge_type: HAS_COLUMN
  source_card_id: table.zs_observe.jiomart_oms
  target_card_id: column.zs_observe.jiomart_oms.order_type
  edge_class: canonical
  canonical_cognee_edge: true
  source_type: table
  target_type: column
```


```yaml
candidate_edge:
  edge_id: edge.jiomart.v9.00352.belongs_to_table
  canonical_edge_type: BELONGS_TO_TABLE
  source_card_id: column.zs_observe.jiomart_oms.order_type
  target_card_id: table.zs_observe.jiomart_oms
  edge_class: canonical
  canonical_cognee_edge: true
  source_type: column
  target_type: table
```


```yaml
candidate_edge:
  edge_id: edge.jiomart.v9.00353.has_column
  canonical_edge_type: HAS_COLUMN
  source_card_id: table.zs_observe.jiomart_oms
  target_card_id: column.zs_observe.jiomart_oms.event_type
  edge_class: canonical
  canonical_cognee_edge: true
  source_type: table
  target_type: column
```


```yaml
candidate_edge:
  edge_id: edge.jiomart.v9.00354.belongs_to_table
  canonical_edge_type: BELONGS_TO_TABLE
  source_card_id: column.zs_observe.jiomart_oms.event_type
  target_card_id: table.zs_observe.jiomart_oms
  edge_class: canonical
  canonical_cognee_edge: true
  source_type: column
  target_type: table
```


```yaml
candidate_edge:
  edge_id: edge.jiomart.v9.00355.has_column
  canonical_edge_type: HAS_COLUMN
  source_card_id: table.zs_observe.jiomart_oms
  target_card_id: column.zs_observe.jiomart_oms.event_sub_type
  edge_class: canonical
  canonical_cognee_edge: true
  source_type: table
  target_type: column
```


```yaml
candidate_edge:
  edge_id: edge.jiomart.v9.00356.belongs_to_table
  canonical_edge_type: BELONGS_TO_TABLE
  source_card_id: column.zs_observe.jiomart_oms.event_sub_type
  target_card_id: table.zs_observe.jiomart_oms
  edge_class: canonical
  canonical_cognee_edge: true
  source_type: column
  target_type: table
```


```yaml
candidate_edge:
  edge_id: edge.jiomart.v9.00357.has_column
  canonical_edge_type: HAS_COLUMN
  source_card_id: table.zs_observe.jiomart_oms
  target_card_id: column.zs_observe.jiomart_oms.fulfilment_channel
  edge_class: canonical
  canonical_cognee_edge: true
  source_type: table
  target_type: column
```


```yaml
candidate_edge:
  edge_id: edge.jiomart.v9.00358.belongs_to_table
  canonical_edge_type: BELONGS_TO_TABLE
  source_card_id: column.zs_observe.jiomart_oms.fulfilment_channel
  target_card_id: table.zs_observe.jiomart_oms
  edge_class: canonical
  canonical_cognee_edge: true
  source_type: column
  target_type: table
```


```yaml
candidate_edge:
  edge_id: edge.jiomart.v9.00359.has_column
  canonical_edge_type: HAS_COLUMN
  source_card_id: table.zs_observe.jiomart_oms
  target_card_id: column.zs_observe.jiomart_oms.fulfillment_type
  edge_class: canonical
  canonical_cognee_edge: true
  source_type: table
  target_type: column
```


```yaml
candidate_edge:
  edge_id: edge.jiomart.v9.00360.belongs_to_table
  canonical_edge_type: BELONGS_TO_TABLE
  source_card_id: column.zs_observe.jiomart_oms.fulfillment_type
  target_card_id: table.zs_observe.jiomart_oms
  edge_class: canonical
  canonical_cognee_edge: true
  source_type: column
  target_type: table
```


```yaml
candidate_edge:
  edge_id: edge.jiomart.v9.00361.has_column
  canonical_edge_type: HAS_COLUMN
  source_card_id: table.zs_observe.jiomart_oms
  target_card_id: column.zs_observe.jiomart_oms.is_active
  edge_class: canonical
  canonical_cognee_edge: true
  source_type: table
  target_type: column
```


```yaml
candidate_edge:
  edge_id: edge.jiomart.v9.00362.belongs_to_table
  canonical_edge_type: BELONGS_TO_TABLE
  source_card_id: column.zs_observe.jiomart_oms.is_active
  target_card_id: table.zs_observe.jiomart_oms
  edge_class: canonical
  canonical_cognee_edge: true
  source_type: column
  target_type: table
```


```yaml
candidate_edge:
  edge_id: edge.jiomart.v9.00363.has_column
  canonical_edge_type: HAS_COLUMN
  source_card_id: table.zs_observe.jiomart_oms
  target_card_id: column.zs_observe.jiomart_oms.is_duplicated
  edge_class: canonical
  canonical_cognee_edge: true
  source_type: table
  target_type: column
```


```yaml
candidate_edge:
  edge_id: edge.jiomart.v9.00364.belongs_to_table
  canonical_edge_type: BELONGS_TO_TABLE
  source_card_id: column.zs_observe.jiomart_oms.is_duplicated
  target_card_id: table.zs_observe.jiomart_oms
  edge_class: canonical
  canonical_cognee_edge: true
  source_type: column
  target_type: table
```


```yaml
candidate_edge:
  edge_id: edge.jiomart.v9.00365.has_column
  canonical_edge_type: HAS_COLUMN
  source_card_id: table.zs_observe.jiomart_oms
  target_card_id: column.zs_observe.jiomart_oms.source_state
  edge_class: canonical
  canonical_cognee_edge: true
  source_type: table
  target_type: column
```


```yaml
candidate_edge:
  edge_id: edge.jiomart.v9.00366.belongs_to_table
  canonical_edge_type: BELONGS_TO_TABLE
  source_card_id: column.zs_observe.jiomart_oms.source_state
  target_card_id: table.zs_observe.jiomart_oms
  edge_class: canonical
  canonical_cognee_edge: true
  source_type: column
  target_type: table
```


```yaml
candidate_edge:
  edge_id: edge.jiomart.v9.00367.has_column
  canonical_edge_type: HAS_COLUMN
  source_card_id: table.zs_observe.jiomart_oms
  target_card_id: column.zs_observe.jiomart_oms.source_state_code
  edge_class: canonical
  canonical_cognee_edge: true
  source_type: table
  target_type: column
```


```yaml
candidate_edge:
  edge_id: edge.jiomart.v9.00368.belongs_to_table
  canonical_edge_type: BELONGS_TO_TABLE
  source_card_id: column.zs_observe.jiomart_oms.source_state_code
  target_card_id: table.zs_observe.jiomart_oms
  edge_class: canonical
  canonical_cognee_edge: true
  source_type: column
  target_type: table
```


```yaml
candidate_edge:
  edge_id: edge.jiomart.v9.00369.has_column
  canonical_edge_type: HAS_COLUMN
  source_card_id: table.zs_observe.jiomart_oms
  target_card_id: column.zs_observe.jiomart_oms.destination_state
  edge_class: canonical
  canonical_cognee_edge: true
  source_type: table
  target_type: column
```


```yaml
candidate_edge:
  edge_id: edge.jiomart.v9.00370.belongs_to_table
  canonical_edge_type: BELONGS_TO_TABLE
  source_card_id: column.zs_observe.jiomart_oms.destination_state
  target_card_id: table.zs_observe.jiomart_oms
  edge_class: canonical
  canonical_cognee_edge: true
  source_type: column
  target_type: table
```


```yaml
candidate_edge:
  edge_id: edge.jiomart.v9.00371.has_column
  canonical_edge_type: HAS_COLUMN
  source_card_id: table.zs_observe.jiomart_oms
  target_card_id: column.zs_observe.jiomart_oms.destination_state_code
  edge_class: canonical
  canonical_cognee_edge: true
  source_type: table
  target_type: column
```


```yaml
candidate_edge:
  edge_id: edge.jiomart.v9.00372.belongs_to_table
  canonical_edge_type: BELONGS_TO_TABLE
  source_card_id: column.zs_observe.jiomart_oms.destination_state_code
  target_card_id: table.zs_observe.jiomart_oms
  edge_class: canonical
  canonical_cognee_edge: true
  source_type: column
  target_type: table
```


```yaml
candidate_edge:
  edge_id: edge.jiomart.v9.00373.has_column
  canonical_edge_type: HAS_COLUMN
  source_card_id: table.zs_observe.jiomart_oms
  target_card_id: column.zs_observe.jiomart_oms.destination_zipcode
  edge_class: canonical
  canonical_cognee_edge: true
  source_type: table
  target_type: column
```


```yaml
candidate_edge:
  edge_id: edge.jiomart.v9.00374.belongs_to_table
  canonical_edge_type: BELONGS_TO_TABLE
  source_card_id: column.zs_observe.jiomart_oms.destination_zipcode
  target_card_id: table.zs_observe.jiomart_oms
  edge_class: canonical
  canonical_cognee_edge: true
  source_type: column
  target_type: table
```


```yaml
candidate_edge:
  edge_id: edge.jiomart.v9.00375.has_column
  canonical_edge_type: HAS_COLUMN
  source_card_id: table.zs_observe.jiomart_oms
  target_card_id: column.zs_observe.jiomart_oms.order_billed_from
  edge_class: canonical
  canonical_cognee_edge: true
  source_type: table
  target_type: column
```


```yaml
candidate_edge:
  edge_id: edge.jiomart.v9.00376.belongs_to_table
  canonical_edge_type: BELONGS_TO_TABLE
  source_card_id: column.zs_observe.jiomart_oms.order_billed_from
  target_card_id: table.zs_observe.jiomart_oms
  edge_class: canonical
  canonical_cognee_edge: true
  source_type: column
  target_type: table
```


```yaml
candidate_edge:
  edge_id: edge.jiomart.v9.00377.has_column
  canonical_edge_type: HAS_COLUMN
  source_card_id: table.zs_observe.jiomart_oms
  target_card_id: column.zs_observe.jiomart_oms.order_shipped_from
  edge_class: canonical
  canonical_cognee_edge: true
  source_type: table
  target_type: column
```


```yaml
candidate_edge:
  edge_id: edge.jiomart.v9.00378.belongs_to_table
  canonical_edge_type: BELONGS_TO_TABLE
  source_card_id: column.zs_observe.jiomart_oms.order_shipped_from
  target_card_id: table.zs_observe.jiomart_oms
  edge_class: canonical
  canonical_cognee_edge: true
  source_type: column
  target_type: table
```


```yaml
candidate_edge:
  edge_id: edge.jiomart.v9.00379.has_column
  canonical_edge_type: HAS_COLUMN
  source_card_id: table.zs_observe.jiomart_oms
  target_card_id: column.zs_observe.jiomart_oms.customer_s_billing_state
  edge_class: canonical
  canonical_cognee_edge: true
  source_type: table
  target_type: column
```


```yaml
candidate_edge:
  edge_id: edge.jiomart.v9.00380.belongs_to_table
  canonical_edge_type: BELONGS_TO_TABLE
  source_card_id: column.zs_observe.jiomart_oms.customer_s_billing_state
  target_card_id: table.zs_observe.jiomart_oms
  edge_class: canonical
  canonical_cognee_edge: true
  source_type: column
  target_type: table
```


```yaml
candidate_edge:
  edge_id: edge.jiomart.v9.00381.has_column
  canonical_edge_type: HAS_COLUMN
  source_card_id: table.zs_observe.jiomart_oms
  target_card_id: column.zs_observe.jiomart_oms.customer_s_delivery_state
  edge_class: canonical
  canonical_cognee_edge: true
  source_type: table
  target_type: column
```


```yaml
candidate_edge:
  edge_id: edge.jiomart.v9.00382.belongs_to_table
  canonical_edge_type: BELONGS_TO_TABLE
  source_card_id: column.zs_observe.jiomart_oms.customer_s_delivery_state
  target_card_id: table.zs_observe.jiomart_oms
  edge_class: canonical
  canonical_cognee_edge: true
  source_type: column
  target_type: table
```


```yaml
candidate_edge:
  edge_id: edge.jiomart.v9.00383.has_column
  canonical_edge_type: HAS_COLUMN
  source_card_id: table.zs_observe.jiomart_oms
  target_card_id: column.zs_observe.jiomart_oms.description
  edge_class: canonical
  canonical_cognee_edge: true
  source_type: table
  target_type: column
```


```yaml
candidate_edge:
  edge_id: edge.jiomart.v9.00384.belongs_to_table
  canonical_edge_type: BELONGS_TO_TABLE
  source_card_id: column.zs_observe.jiomart_oms.description
  target_card_id: table.zs_observe.jiomart_oms
  edge_class: canonical
  canonical_cognee_edge: true
  source_type: column
  target_type: table
```


```yaml
candidate_edge:
  edge_id: edge.jiomart.v9.00385.has_column
  canonical_edge_type: HAS_COLUMN
  source_card_id: table.zs_observe.jiomart_oms
  target_card_id: column.zs_observe.jiomart_oms.product_title_description
  edge_class: canonical
  canonical_cognee_edge: true
  source_type: table
  target_type: column
```


```yaml
candidate_edge:
  edge_id: edge.jiomart.v9.00386.belongs_to_table
  canonical_edge_type: BELONGS_TO_TABLE
  source_card_id: column.zs_observe.jiomart_oms.product_title_description
  target_card_id: table.zs_observe.jiomart_oms
  edge_class: canonical
  canonical_cognee_edge: true
  source_type: column
  target_type: table
```


```yaml
candidate_edge:
  edge_id: edge.jiomart.v9.00387.has_column
  canonical_edge_type: HAS_COLUMN
  source_card_id: table.zs_observe.jiomart_oms
  target_card_id: column.zs_observe.jiomart_oms.quantity
  edge_class: canonical
  canonical_cognee_edge: true
  source_type: table
  target_type: column
```


```yaml
candidate_edge:
  edge_id: edge.jiomart.v9.00388.belongs_to_table
  canonical_edge_type: BELONGS_TO_TABLE
  source_card_id: column.zs_observe.jiomart_oms.quantity
  target_card_id: table.zs_observe.jiomart_oms
  edge_class: canonical
  canonical_cognee_edge: true
  source_type: column
  target_type: table
```


```yaml
candidate_edge:
  edge_id: edge.jiomart.v9.00389.has_column
  canonical_edge_type: HAS_COLUMN
  source_card_id: table.zs_observe.jiomart_oms
  target_card_id: column.zs_observe.jiomart_oms.item_quantity
  edge_class: canonical
  canonical_cognee_edge: true
  source_type: table
  target_type: column
```


```yaml
candidate_edge:
  edge_id: edge.jiomart.v9.00390.belongs_to_table
  canonical_edge_type: BELONGS_TO_TABLE
  source_card_id: column.zs_observe.jiomart_oms.item_quantity
  target_card_id: table.zs_observe.jiomart_oms
  edge_class: canonical
  canonical_cognee_edge: true
  source_type: column
  target_type: table
```


```yaml
candidate_edge:
  edge_id: edge.jiomart.v9.00391.has_column
  canonical_edge_type: HAS_COLUMN
  source_card_id: table.zs_observe.jiomart_oms
  target_card_id: column.zs_observe.jiomart_oms.fulfiller_name
  edge_class: canonical
  canonical_cognee_edge: true
  source_type: table
  target_type: column
```


```yaml
candidate_edge:
  edge_id: edge.jiomart.v9.00392.belongs_to_table
  canonical_edge_type: BELONGS_TO_TABLE
  source_card_id: column.zs_observe.jiomart_oms.fulfiller_name
  target_card_id: table.zs_observe.jiomart_oms
  edge_class: canonical
  canonical_cognee_edge: true
  source_type: column
  target_type: table
```


```yaml
candidate_edge:
  edge_id: edge.jiomart.v9.00393.has_column
  canonical_edge_type: HAS_COLUMN
  source_card_id: table.zs_observe.jiomart_oms
  target_card_id: column.zs_observe.jiomart_oms.group_level_id
  edge_class: canonical
  canonical_cognee_edge: true
  source_type: table
  target_type: column
```


```yaml
candidate_edge:
  edge_id: edge.jiomart.v9.00394.belongs_to_table
  canonical_edge_type: BELONGS_TO_TABLE
  source_card_id: column.zs_observe.jiomart_oms.group_level_id
  target_card_id: table.zs_observe.jiomart_oms
  edge_class: canonical
  canonical_cognee_edge: true
  source_type: column
  target_type: table
```


```yaml
candidate_edge:
  edge_id: edge.jiomart.v9.00395.has_column
  canonical_edge_type: HAS_COLUMN
  source_card_id: table.zs_observe.jiomart_oms
  target_card_id: column.zs_observe.jiomart_oms.brand
  edge_class: canonical
  canonical_cognee_edge: true
  source_type: table
  target_type: column
```


```yaml
candidate_edge:
  edge_id: edge.jiomart.v9.00396.belongs_to_table
  canonical_edge_type: BELONGS_TO_TABLE
  source_card_id: column.zs_observe.jiomart_oms.brand
  target_card_id: table.zs_observe.jiomart_oms
  edge_class: canonical
  canonical_cognee_edge: true
  source_type: column
  target_type: table
```


```yaml
candidate_edge:
  edge_id: edge.jiomart.v9.00397.has_column
  canonical_edge_type: HAS_COLUMN
  source_card_id: table.zs_observe.jiomart_oms
  target_card_id: column.zs_observe.jiomart_oms.brand_ref_1
  edge_class: canonical
  canonical_cognee_edge: true
  source_type: table
  target_type: column
```


```yaml
candidate_edge:
  edge_id: edge.jiomart.v9.00398.belongs_to_table
  canonical_edge_type: BELONGS_TO_TABLE
  source_card_id: column.zs_observe.jiomart_oms.brand_ref_1
  target_card_id: table.zs_observe.jiomart_oms
  edge_class: canonical
  canonical_cognee_edge: true
  source_type: column
  target_type: table
```


```yaml
candidate_edge:
  edge_id: edge.jiomart.v9.00399.has_column
  canonical_edge_type: HAS_COLUMN
  source_card_id: table.zs_observe.jiomart_oms
  target_card_id: column.zs_observe.jiomart_oms.brand_ref_2
  edge_class: canonical
  canonical_cognee_edge: true
  source_type: table
  target_type: column
```


```yaml
candidate_edge:
  edge_id: edge.jiomart.v9.00400.belongs_to_table
  canonical_edge_type: BELONGS_TO_TABLE
  source_card_id: column.zs_observe.jiomart_oms.brand_ref_2
  target_card_id: table.zs_observe.jiomart_oms
  edge_class: canonical
  canonical_cognee_edge: true
  source_type: column
  target_type: table
```


```yaml
candidate_edge:
  edge_id: edge.jiomart.v9.00401.has_column
  canonical_edge_type: HAS_COLUMN
  source_card_id: table.zs_observe.jiomart_oms
  target_card_id: column.zs_observe.jiomart_oms.seller_coupon_code
  edge_class: canonical
  canonical_cognee_edge: true
  source_type: table
  target_type: column
```


```yaml
candidate_edge:
  edge_id: edge.jiomart.v9.00402.belongs_to_table
  canonical_edge_type: BELONGS_TO_TABLE
  source_card_id: column.zs_observe.jiomart_oms.seller_coupon_code
  target_card_id: table.zs_observe.jiomart_oms
  edge_class: canonical
  canonical_cognee_edge: true
  source_type: column
  target_type: table
```


```yaml
candidate_edge:
  edge_id: edge.jiomart.v9.00403.has_column
  canonical_edge_type: HAS_COLUMN
  source_card_id: table.zs_observe.jiomart_oms
  target_card_id: column.zs_observe.jiomart_oms.currency_type
  edge_class: canonical
  canonical_cognee_edge: true
  source_type: table
  target_type: column
```


```yaml
candidate_edge:
  edge_id: edge.jiomart.v9.00404.belongs_to_table
  canonical_edge_type: BELONGS_TO_TABLE
  source_card_id: column.zs_observe.jiomart_oms.currency_type
  target_card_id: table.zs_observe.jiomart_oms
  edge_class: canonical
  canonical_cognee_edge: true
  source_type: column
  target_type: table
```


```yaml
candidate_edge:
  edge_id: edge.jiomart.v9.00405.has_column
  canonical_edge_type: HAS_COLUMN
  source_card_id: table.zs_observe.jiomart_oms
  target_card_id: column.zs_observe.jiomart_oms.zen_sheet_name
  edge_class: canonical
  canonical_cognee_edge: true
  source_type: table
  target_type: column
```


```yaml
candidate_edge:
  edge_id: edge.jiomart.v9.00406.belongs_to_table
  canonical_edge_type: BELONGS_TO_TABLE
  source_card_id: column.zs_observe.jiomart_oms.zen_sheet_name
  target_card_id: table.zs_observe.jiomart_oms
  edge_class: canonical
  canonical_cognee_edge: true
  source_type: column
  target_type: table
```


```yaml
candidate_edge:
  edge_id: edge.jiomart.v9.00407.has_column
  canonical_edge_type: HAS_COLUMN
  source_card_id: table.zs_observe.jiomart_oms
  target_card_id: column.zs_observe.jiomart_oms.temp_old_columns
  edge_class: canonical
  canonical_cognee_edge: true
  source_type: table
  target_type: column
```


```yaml
candidate_edge:
  edge_id: edge.jiomart.v9.00408.belongs_to_table
  canonical_edge_type: BELONGS_TO_TABLE
  source_card_id: column.zs_observe.jiomart_oms.temp_old_columns
  target_card_id: table.zs_observe.jiomart_oms
  edge_class: canonical
  canonical_cognee_edge: true
  source_type: column
  target_type: table
```


```yaml
candidate_edge:
  edge_id: edge.jiomart.v9.00409.source_table
  canonical_edge_type: SOURCE_TABLE
  source_card_id: relationship.jiomart.oms_settlement.order_id
  target_card_id: table.zs_observe.jiomart_oms
  edge_class: canonical
  canonical_cognee_edge: true
  source_type: relationship
  target_type: table
```


```yaml
candidate_edge:
  edge_id: edge.jiomart.v9.00410.target_table
  canonical_edge_type: TARGET_TABLE
  source_card_id: relationship.jiomart.oms_settlement.order_id
  target_card_id: table.zs_observe.jiomart_settlement
  edge_class: canonical
  canonical_cognee_edge: true
  source_type: relationship
  target_type: table
```


```yaml
candidate_edge:
  edge_id: edge.jiomart.v9.00411.uses_source_column
  canonical_edge_type: USES_SOURCE_COLUMN
  source_card_id: relationship.jiomart.oms_settlement.order_id
  target_card_id: column.zs_observe.jiomart_oms.order_id
  edge_class: canonical
  canonical_cognee_edge: true
  source_type: relationship
  target_type: column
```


```yaml
candidate_edge:
  edge_id: edge.jiomart.v9.00412.uses_target_column
  canonical_edge_type: USES_TARGET_COLUMN
  source_card_id: relationship.jiomart.oms_settlement.order_id
  target_card_id: column.zs_observe.jiomart_settlement.order_id
  edge_class: canonical
  canonical_cognee_edge: true
  source_type: relationship
  target_type: column
```


```yaml
candidate_edge:
  edge_id: edge.jiomart.v9.00413.source_table
  canonical_edge_type: SOURCE_TABLE
  source_card_id: relationship.jiomart.oms_returns.order_id
  target_card_id: table.zs_observe.jiomart_oms
  edge_class: canonical
  canonical_cognee_edge: true
  source_type: relationship
  target_type: table
```


```yaml
candidate_edge:
  edge_id: edge.jiomart.v9.00414.target_table
  canonical_edge_type: TARGET_TABLE
  source_card_id: relationship.jiomart.oms_returns.order_id
  target_card_id: table.zs_observe.jiomart_returns
  edge_class: canonical
  canonical_cognee_edge: true
  source_type: relationship
  target_type: table
```


```yaml
candidate_edge:
  edge_id: edge.jiomart.v9.00415.uses_source_column
  canonical_edge_type: USES_SOURCE_COLUMN
  source_card_id: relationship.jiomart.oms_returns.order_id
  target_card_id: column.zs_observe.jiomart_oms.order_id
  edge_class: canonical
  canonical_cognee_edge: true
  source_type: relationship
  target_type: column
```


```yaml
candidate_edge:
  edge_id: edge.jiomart.v9.00416.uses_target_column
  canonical_edge_type: USES_TARGET_COLUMN
  source_card_id: relationship.jiomart.oms_returns.order_id
  target_card_id: column.zs_observe.jiomart_returns.order_id
  edge_class: canonical
  canonical_cognee_edge: true
  source_type: relationship
  target_type: column
```


```yaml
candidate_edge:
  edge_id: edge.jiomart.v9.00417.source_table
  canonical_edge_type: SOURCE_TABLE
  source_card_id: relationship.jiomart.settlement_returns.order_id
  target_card_id: table.zs_observe.jiomart_settlement
  edge_class: canonical
  canonical_cognee_edge: true
  source_type: relationship
  target_type: table
```


```yaml
candidate_edge:
  edge_id: edge.jiomart.v9.00418.target_table
  canonical_edge_type: TARGET_TABLE
  source_card_id: relationship.jiomart.settlement_returns.order_id
  target_card_id: table.zs_observe.jiomart_returns
  edge_class: canonical
  canonical_cognee_edge: true
  source_type: relationship
  target_type: table
```


```yaml
candidate_edge:
  edge_id: edge.jiomart.v9.00419.uses_source_column
  canonical_edge_type: USES_SOURCE_COLUMN
  source_card_id: relationship.jiomart.settlement_returns.order_id
  target_card_id: column.zs_observe.jiomart_settlement.order_id
  edge_class: canonical
  canonical_cognee_edge: true
  source_type: relationship
  target_type: column
```


```yaml
candidate_edge:
  edge_id: edge.jiomart.v9.00420.uses_target_column
  canonical_edge_type: USES_TARGET_COLUMN
  source_card_id: relationship.jiomart.settlement_returns.order_id
  target_card_id: column.zs_observe.jiomart_returns.order_id
  edge_class: canonical
  canonical_cognee_edge: true
  source_type: relationship
  target_type: column
```


```yaml
candidate_edge:
  edge_id: edge.jiomart.v9.00421.profiles_column
  canonical_edge_type: PROFILES_COLUMN
  source_card_id: value_profile.jiomart.scope.group_level_id_26
  target_card_id: column.zs_observe.jiomart_oms.group_level_id
  edge_class: canonical
  canonical_cognee_edge: true
  source_type: value_profile
  target_type: column
```


```yaml
candidate_edge:
  edge_id: edge.jiomart.v9.00422.has_value_profile
  canonical_edge_type: HAS_VALUE_PROFILE
  source_card_id: column.zs_observe.jiomart_oms.group_level_id
  target_card_id: value_profile.jiomart.scope.group_level_id_26
  edge_class: canonical
  canonical_cognee_edge: true
  source_type: column
  target_type: value_profile
```


```yaml
candidate_edge:
  edge_id: edge.jiomart.v9.00423.profiles_column
  canonical_edge_type: PROFILES_COLUMN
  source_card_id: value_profile.jiomart.scope.group_level_id_221
  target_card_id: column.zs_observe.jiomart_shipment.group_level_id
  edge_class: canonical
  canonical_cognee_edge: true
  source_type: value_profile
  target_type: column
```


```yaml
candidate_edge:
  edge_id: edge.jiomart.v9.00424.has_value_profile
  canonical_edge_type: HAS_VALUE_PROFILE
  source_card_id: column.zs_observe.jiomart_shipment.group_level_id
  target_card_id: value_profile.jiomart.scope.group_level_id_221
  edge_class: canonical
  canonical_cognee_edge: true
  source_type: column
  target_type: value_profile
```


```yaml
candidate_edge:
  edge_id: edge.jiomart.v9.00425.profiles_table
  canonical_edge_type: PROFILES_TABLE
  source_card_id: value_profile.jiomart.products.myfitness_hsn
  target_card_id: table.zs_observe.jiomart_oms
  edge_class: canonical
  canonical_cognee_edge: true
  source_type: value_profile
  target_type: table
```


```yaml
candidate_edge:
  edge_id: edge.jiomart.v9.00426.has_value_profile
  canonical_edge_type: HAS_VALUE_PROFILE
  source_card_id: table.zs_observe.jiomart_oms
  target_card_id: value_profile.jiomart.products.myfitness_hsn
  edge_class: canonical
  canonical_cognee_edge: true
  source_type: table
  target_type: value_profile
```


```yaml
candidate_edge:
  edge_id: edge.jiomart.v9.00427.profiles_table
  canonical_edge_type: PROFILES_TABLE
  source_card_id: value_profile.jiomart.gstin.tanvi_multistate
  target_card_id: table.zs_observe.jiomart_oms
  edge_class: canonical
  canonical_cognee_edge: true
  source_type: value_profile
  target_type: table
```


```yaml
candidate_edge:
  edge_id: edge.jiomart.v9.00428.has_value_profile
  canonical_edge_type: HAS_VALUE_PROFILE
  source_card_id: table.zs_observe.jiomart_oms
  target_card_id: value_profile.jiomart.gstin.tanvi_multistate
  edge_class: canonical
  canonical_cognee_edge: true
  source_type: table
  target_type: value_profile
```


```yaml
candidate_edge:
  edge_id: edge.jiomart.v9.00429.profiles_column
  canonical_edge_type: PROFILES_COLUMN
  source_card_id: value_profile.jiomart.shipment.order_status
  target_card_id: column.zs_observe.jiomart_shipment.order_status
  edge_class: canonical
  canonical_cognee_edge: true
  source_type: value_profile
  target_type: column
```


```yaml
candidate_edge:
  edge_id: edge.jiomart.v9.00430.has_value_profile
  canonical_edge_type: HAS_VALUE_PROFILE
  source_card_id: column.zs_observe.jiomart_shipment.order_status
  target_card_id: value_profile.jiomart.shipment.order_status
  edge_class: canonical
  canonical_cognee_edge: true
  source_type: column
  target_type: value_profile
```


```yaml
candidate_edge:
  edge_id: edge.jiomart.v9.00431.profiles_column
  canonical_edge_type: PROFILES_COLUMN
  source_card_id: value_profile.jiomart.shipment.sku_prefixes
  target_card_id: column.zs_observe.jiomart_shipment.sku_id
  edge_class: canonical
  canonical_cognee_edge: true
  source_type: value_profile
  target_type: column
```


```yaml
candidate_edge:
  edge_id: edge.jiomart.v9.00432.has_value_profile
  canonical_edge_type: HAS_VALUE_PROFILE
  source_card_id: column.zs_observe.jiomart_shipment.sku_id
  target_card_id: value_profile.jiomart.shipment.sku_prefixes
  edge_class: canonical
  canonical_cognee_edge: true
  source_type: column
  target_type: value_profile
```


```yaml
candidate_edge:
  edge_id: edge.jiomart.v9.00433.profiles_column
  canonical_edge_type: PROFILES_COLUMN
  source_card_id: value_profile.jiomart.shipment.payment_mode
  target_card_id: column.zs_observe.jiomart_shipment.payment_mode
  edge_class: canonical
  canonical_cognee_edge: true
  source_type: value_profile
  target_type: column
```


```yaml
candidate_edge:
  edge_id: edge.jiomart.v9.00434.has_value_profile
  canonical_edge_type: HAS_VALUE_PROFILE
  source_card_id: column.zs_observe.jiomart_shipment.payment_mode
  target_card_id: value_profile.jiomart.shipment.payment_mode
  edge_class: canonical
  canonical_cognee_edge: true
  source_type: column
  target_type: value_profile
```


```yaml
candidate_edge:
  edge_id: edge.jiomart.v9.00435.profiles_column
  canonical_edge_type: PROFILES_COLUMN
  source_card_id: value_profile.jiomart.shipment.fulfillment_channel
  target_card_id: column.zs_observe.jiomart_shipment.fulfillment_channel
  edge_class: canonical
  canonical_cognee_edge: true
  source_type: value_profile
  target_type: column
```


```yaml
candidate_edge:
  edge_id: edge.jiomart.v9.00436.has_value_profile
  canonical_edge_type: HAS_VALUE_PROFILE
  source_card_id: column.zs_observe.jiomart_shipment.fulfillment_channel
  target_card_id: value_profile.jiomart.shipment.fulfillment_channel
  edge_class: canonical
  canonical_cognee_edge: true
  source_type: column
  target_type: value_profile
```


```yaml
candidate_edge:
  edge_id: edge.jiomart.v9.00437.profiles_column
  canonical_edge_type: PROFILES_COLUMN
  source_card_id: value_profile.jiomart.shipment.promo_discount_scale
  target_card_id: column.zs_observe.jiomart_shipment.item_promo_discount
  edge_class: canonical
  canonical_cognee_edge: true
  source_type: value_profile
  target_type: column
```


```yaml
candidate_edge:
  edge_id: edge.jiomart.v9.00438.has_value_profile
  canonical_edge_type: HAS_VALUE_PROFILE
  source_card_id: column.zs_observe.jiomart_shipment.item_promo_discount
  target_card_id: value_profile.jiomart.shipment.promo_discount_scale
  edge_class: canonical
  canonical_cognee_edge: true
  source_type: column
  target_type: value_profile
```


```yaml
candidate_edge:
  edge_id: edge.jiomart.v9.00439.profiles_column
  canonical_edge_type: PROFILES_COLUMN
  source_card_id: value_profile.jiomart.settlement.transaction_type
  target_card_id: column.zs_observe.jiomart_settlement.transaction_type
  edge_class: canonical
  canonical_cognee_edge: true
  source_type: value_profile
  target_type: column
```


```yaml
candidate_edge:
  edge_id: edge.jiomart.v9.00440.has_value_profile
  canonical_edge_type: HAS_VALUE_PROFILE
  source_card_id: column.zs_observe.jiomart_settlement.transaction_type
  target_card_id: value_profile.jiomart.settlement.transaction_type
  edge_class: canonical
  canonical_cognee_edge: true
  source_type: column
  target_type: value_profile
```


```yaml
candidate_edge:
  edge_id: edge.jiomart.v9.00441.profiles_column
  canonical_edge_type: PROFILES_COLUMN
  source_card_id: value_profile.jiomart.settlement.event
  target_card_id: column.zs_observe.jiomart_settlement.event
  edge_class: canonical
  canonical_cognee_edge: true
  source_type: value_profile
  target_type: column
```


```yaml
candidate_edge:
  edge_id: edge.jiomart.v9.00442.has_value_profile
  canonical_edge_type: HAS_VALUE_PROFILE
  source_card_id: column.zs_observe.jiomart_settlement.event
  target_card_id: value_profile.jiomart.settlement.event
  edge_class: canonical
  canonical_cognee_edge: true
  source_type: column
  target_type: value_profile
```


```yaml
candidate_edge:
  edge_id: edge.jiomart.v9.00443.profiles_column
  canonical_edge_type: PROFILES_COLUMN
  source_card_id: value_profile.jiomart.settlement.accountable_type
  target_card_id: column.zs_observe.jiomart_settlement.accountable_type
  edge_class: canonical
  canonical_cognee_edge: true
  source_type: value_profile
  target_type: column
```


```yaml
candidate_edge:
  edge_id: edge.jiomart.v9.00444.has_value_profile
  canonical_edge_type: HAS_VALUE_PROFILE
  source_card_id: column.zs_observe.jiomart_settlement.accountable_type
  target_card_id: value_profile.jiomart.settlement.accountable_type
  edge_class: canonical
  canonical_cognee_edge: true
  source_type: column
  target_type: value_profile
```


```yaml
candidate_edge:
  edge_id: edge.jiomart.v9.00445.profiles_table
  canonical_edge_type: PROFILES_TABLE
  source_card_id: value_profile.jiomart.settlement.event_accountable_matrix
  target_card_id: table.zs_observe.jiomart_settlement
  edge_class: canonical
  canonical_cognee_edge: true
  source_type: value_profile
  target_type: table
```


```yaml
candidate_edge:
  edge_id: edge.jiomart.v9.00446.has_value_profile
  canonical_edge_type: HAS_VALUE_PROFILE
  source_card_id: table.zs_observe.jiomart_settlement
  target_card_id: value_profile.jiomart.settlement.event_accountable_matrix
  edge_class: canonical
  canonical_cognee_edge: true
  source_type: table
  target_type: value_profile
```


```yaml
candidate_edge:
  edge_id: edge.jiomart.v9.00447.profiles_column
  canonical_edge_type: PROFILES_COLUMN
  source_card_id: value_profile.jiomart.settlement.account_book
  target_card_id: column.zs_observe.jiomart_settlement.account_book
  edge_class: canonical
  canonical_cognee_edge: true
  source_type: value_profile
  target_type: column
```


```yaml
candidate_edge:
  edge_id: edge.jiomart.v9.00448.has_value_profile
  canonical_edge_type: HAS_VALUE_PROFILE
  source_card_id: column.zs_observe.jiomart_settlement.account_book
  target_card_id: value_profile.jiomart.settlement.account_book
  edge_class: canonical
  canonical_cognee_edge: true
  source_type: column
  target_type: value_profile
```


```yaml
candidate_edge:
  edge_id: edge.jiomart.v9.00449.profiles_column
  canonical_edge_type: PROFILES_COLUMN
  source_card_id: value_profile.jiomart.returns.return_type
  target_card_id: column.zs_observe.jiomart_returns.return_type
  edge_class: canonical
  canonical_cognee_edge: true
  source_type: value_profile
  target_type: column
```


```yaml
candidate_edge:
  edge_id: edge.jiomart.v9.00450.has_value_profile
  canonical_edge_type: HAS_VALUE_PROFILE
  source_card_id: column.zs_observe.jiomart_returns.return_type
  target_card_id: value_profile.jiomart.returns.return_type
  edge_class: canonical
  canonical_cognee_edge: true
  source_type: column
  target_type: value_profile
```


```yaml
candidate_edge:
  edge_id: edge.jiomart.v9.00451.profiles_column
  canonical_edge_type: PROFILES_COLUMN
  source_card_id: value_profile.jiomart.returns.return_status
  target_card_id: column.zs_observe.jiomart_returns.return_status
  edge_class: canonical
  canonical_cognee_edge: true
  source_type: value_profile
  target_type: column
```


```yaml
candidate_edge:
  edge_id: edge.jiomart.v9.00452.has_value_profile
  canonical_edge_type: HAS_VALUE_PROFILE
  source_card_id: column.zs_observe.jiomart_returns.return_status
  target_card_id: value_profile.jiomart.returns.return_status
  edge_class: canonical
  canonical_cognee_edge: true
  source_type: column
  target_type: value_profile
```


```yaml
candidate_edge:
  edge_id: edge.jiomart.v9.00453.profiles_column
  canonical_edge_type: PROFILES_COLUMN
  source_card_id: value_profile.jiomart.returns.payment_mode
  target_card_id: column.zs_observe.jiomart_returns.payment_mode
  edge_class: canonical
  canonical_cognee_edge: true
  source_type: value_profile
  target_type: column
```


```yaml
candidate_edge:
  edge_id: edge.jiomart.v9.00454.has_value_profile
  canonical_edge_type: HAS_VALUE_PROFILE
  source_card_id: column.zs_observe.jiomart_returns.payment_mode
  target_card_id: value_profile.jiomart.returns.payment_mode
  edge_class: canonical
  canonical_cognee_edge: true
  source_type: column
  target_type: value_profile
```


```yaml
candidate_edge:
  edge_id: edge.jiomart.v9.00455.profiles_column
  canonical_edge_type: PROFILES_COLUMN
  source_card_id: value_profile.jiomart.returns.couriers
  target_card_id: column.zs_observe.jiomart_returns.courier_partner
  edge_class: canonical
  canonical_cognee_edge: true
  source_type: value_profile
  target_type: column
```


```yaml
candidate_edge:
  edge_id: edge.jiomart.v9.00456.has_value_profile
  canonical_edge_type: HAS_VALUE_PROFILE
  source_card_id: column.zs_observe.jiomart_returns.courier_partner
  target_card_id: value_profile.jiomart.returns.couriers
  edge_class: canonical
  canonical_cognee_edge: true
  source_type: column
  target_type: value_profile
```


```yaml
candidate_edge:
  edge_id: edge.jiomart.v9.00457.profiles_column
  canonical_edge_type: PROFILES_COLUMN
  source_card_id: value_profile.jiomart.returns.fulfillment_centers
  target_card_id: column.zs_observe.jiomart_returns.fulfillment_center
  edge_class: canonical
  canonical_cognee_edge: true
  source_type: value_profile
  target_type: column
```


```yaml
candidate_edge:
  edge_id: edge.jiomart.v9.00458.has_value_profile
  canonical_edge_type: HAS_VALUE_PROFILE
  source_card_id: column.zs_observe.jiomart_returns.fulfillment_center
  target_card_id: value_profile.jiomart.returns.fulfillment_centers
  edge_class: canonical
  canonical_cognee_edge: true
  source_type: column
  target_type: value_profile
```


```yaml
candidate_edge:
  edge_id: edge.jiomart.v9.00459.profiles_column
  canonical_edge_type: PROFILES_COLUMN
  source_card_id: value_profile.jiomart.oms.transaction_type
  target_card_id: column.zs_observe.jiomart_oms.transaction_type
  edge_class: canonical
  canonical_cognee_edge: true
  source_type: value_profile
  target_type: column
```


```yaml
candidate_edge:
  edge_id: edge.jiomart.v9.00460.has_value_profile
  canonical_edge_type: HAS_VALUE_PROFILE
  source_card_id: column.zs_observe.jiomart_oms.transaction_type
  target_card_id: value_profile.jiomart.oms.transaction_type
  edge_class: canonical
  canonical_cognee_edge: true
  source_type: column
  target_type: value_profile
```


```yaml
candidate_edge:
  edge_id: edge.jiomart.v9.00461.profiles_column
  canonical_edge_type: PROFILES_COLUMN
  source_card_id: value_profile.jiomart.oms.order_status
  target_card_id: column.zs_observe.jiomart_oms.order_status
  edge_class: canonical
  canonical_cognee_edge: true
  source_type: value_profile
  target_type: column
```


```yaml
candidate_edge:
  edge_id: edge.jiomart.v9.00462.has_value_profile
  canonical_edge_type: HAS_VALUE_PROFILE
  source_card_id: column.zs_observe.jiomart_oms.order_status
  target_card_id: value_profile.jiomart.oms.order_status
  edge_class: canonical
  canonical_cognee_edge: true
  source_type: column
  target_type: value_profile
```


```yaml
candidate_edge:
  edge_id: edge.jiomart.v9.00463.profiles_column
  canonical_edge_type: PROFILES_COLUMN
  source_card_id: value_profile.jiomart.oms.order_type
  target_card_id: column.zs_observe.jiomart_oms.order_type
  edge_class: canonical
  canonical_cognee_edge: true
  source_type: value_profile
  target_type: column
```


```yaml
candidate_edge:
  edge_id: edge.jiomart.v9.00464.has_value_profile
  canonical_edge_type: HAS_VALUE_PROFILE
  source_card_id: column.zs_observe.jiomart_oms.order_type
  target_card_id: value_profile.jiomart.oms.order_type
  edge_class: canonical
  canonical_cognee_edge: true
  source_type: column
  target_type: value_profile
```


```yaml
candidate_edge:
  edge_id: edge.jiomart.v9.00465.profiles_column
  canonical_edge_type: PROFILES_COLUMN
  source_card_id: value_profile.jiomart.oms.fulfilment_channel
  target_card_id: column.zs_observe.jiomart_oms.fulfilment_channel
  edge_class: canonical
  canonical_cognee_edge: true
  source_type: value_profile
  target_type: column
```


```yaml
candidate_edge:
  edge_id: edge.jiomart.v9.00466.has_value_profile
  canonical_edge_type: HAS_VALUE_PROFILE
  source_card_id: column.zs_observe.jiomart_oms.fulfilment_channel
  target_card_id: value_profile.jiomart.oms.fulfilment_channel
  edge_class: canonical
  canonical_cognee_edge: true
  source_type: column
  target_type: value_profile
```


```yaml
candidate_edge:
  edge_id: edge.jiomart.v9.00467.profiles_column
  canonical_edge_type: PROFILES_COLUMN
  source_card_id: value_profile.jiomart.oms.source_state
  target_card_id: column.zs_observe.jiomart_oms.source_state
  edge_class: canonical
  canonical_cognee_edge: true
  source_type: value_profile
  target_type: column
```


```yaml
candidate_edge:
  edge_id: edge.jiomart.v9.00468.has_value_profile
  canonical_edge_type: HAS_VALUE_PROFILE
  source_card_id: column.zs_observe.jiomart_oms.source_state
  target_card_id: value_profile.jiomart.oms.source_state
  edge_class: canonical
  canonical_cognee_edge: true
  source_type: column
  target_type: value_profile
```


```yaml
candidate_edge:
  edge_id: edge.jiomart.v9.00469.profiles_column
  canonical_edge_type: PROFILES_COLUMN
  source_card_id: value_profile.jiomart.oms.hsn_products
  target_card_id: column.zs_observe.jiomart_oms.hsn
  edge_class: canonical
  canonical_cognee_edge: true
  source_type: value_profile
  target_type: column
```


```yaml
candidate_edge:
  edge_id: edge.jiomart.v9.00470.has_value_profile
  canonical_edge_type: HAS_VALUE_PROFILE
  source_card_id: column.zs_observe.jiomart_oms.hsn
  target_card_id: value_profile.jiomart.oms.hsn_products
  edge_class: canonical
  canonical_cognee_edge: true
  source_type: column
  target_type: value_profile
```


```yaml
candidate_edge:
  edge_id: edge.jiomart.v9.00471.profiles_column
  canonical_edge_type: PROFILES_COLUMN
  source_card_id: value_profile.jiomart.oms.top_skus
  target_card_id: column.zs_observe.jiomart_oms.sku_id
  edge_class: canonical
  canonical_cognee_edge: true
  source_type: value_profile
  target_type: column
```


```yaml
candidate_edge:
  edge_id: edge.jiomart.v9.00472.has_value_profile
  canonical_edge_type: HAS_VALUE_PROFILE
  source_card_id: column.zs_observe.jiomart_oms.sku_id
  target_card_id: value_profile.jiomart.oms.top_skus
  edge_class: canonical
  canonical_cognee_edge: true
  source_type: column
  target_type: value_profile
```


```yaml
candidate_edge:
  edge_id: edge.jiomart.v9.00473.profiles_column
  canonical_edge_type: PROFILES_COLUMN
  source_card_id: value_profile.jiomart.oms.coupon_codes
  target_card_id: column.zs_observe.jiomart_oms.seller_coupon_code
  edge_class: canonical
  canonical_cognee_edge: true
  source_type: value_profile
  target_type: column
```


```yaml
candidate_edge:
  edge_id: edge.jiomart.v9.00474.has_value_profile
  canonical_edge_type: HAS_VALUE_PROFILE
  source_card_id: column.zs_observe.jiomart_oms.seller_coupon_code
  target_card_id: value_profile.jiomart.oms.coupon_codes
  edge_class: canonical
  canonical_cognee_edge: true
  source_type: column
  target_type: value_profile
```


```yaml
candidate_edge:
  edge_id: edge.jiomart.v9.00475.profiles_column
  canonical_edge_type: PROFILES_COLUMN
  source_card_id: value_profile.jiomart.oms.tcs_rates
  target_card_id: column.zs_observe.jiomart_oms.tcs_igst_rate
  edge_class: canonical
  canonical_cognee_edge: true
  source_type: value_profile
  target_type: column
```


```yaml
candidate_edge:
  edge_id: edge.jiomart.v9.00476.has_value_profile
  canonical_edge_type: HAS_VALUE_PROFILE
  source_card_id: column.zs_observe.jiomart_oms.tcs_igst_rate
  target_card_id: value_profile.jiomart.oms.tcs_rates
  edge_class: canonical
  canonical_cognee_edge: true
  source_type: column
  target_type: value_profile
```


```yaml
candidate_edge:
  edge_id: edge.jiomart.v9.00477.applies_to_platform_context
  canonical_edge_type: APPLIES_TO_PLATFORM_CONTEXT
  source_card_id: value_profile.jiomart.currency.inr
  target_card_id: platform_context.jiomart.in
  edge_class: canonical
  canonical_cognee_edge: true
  source_type: value_profile
  target_type: platform_context
```


```yaml
candidate_edge:
  edge_id: edge.jiomart.v9.00478.belongs_to_domain
  canonical_edge_type: BELONGS_TO_DOMAIN
  source_card_id: metric.jiomart.total_gmv
  target_card_id: domain.jiomart.orders
  edge_class: canonical
  canonical_cognee_edge: true
  source_type: metric
  target_type: domain
```


```yaml
candidate_edge:
  edge_id: edge.jiomart.v9.00479.applies_to_platform_context
  canonical_edge_type: APPLIES_TO_PLATFORM_CONTEXT
  source_card_id: metric.jiomart.total_gmv
  target_card_id: platform_context.jiomart.in
  edge_class: canonical
  canonical_cognee_edge: true
  source_type: metric
  target_type: platform_context
```


```yaml
candidate_edge:
  edge_id: edge.jiomart.v9.00480.implements_metric
  canonical_edge_type: IMPLEMENTS_METRIC
  source_card_id: metric_impl.jiomart.total_gmv
  target_card_id: metric.jiomart.total_gmv
  edge_class: canonical
  canonical_cognee_edge: true
  source_type: metric_implementation
  target_type: metric
```


```yaml
candidate_edge:
  edge_id: edge.jiomart.v9.00481.has_implementation
  canonical_edge_type: HAS_IMPLEMENTATION
  source_card_id: metric.jiomart.total_gmv
  target_card_id: metric_impl.jiomart.total_gmv
  edge_class: canonical
  canonical_cognee_edge: true
  source_type: metric
  target_type: metric_implementation
```


```yaml
candidate_edge:
  edge_id: edge.jiomart.v9.00482.uses_table
  canonical_edge_type: USES_TABLE
  source_card_id: metric_impl.jiomart.total_gmv
  target_card_id: table.zs_observe.jiomart_oms
  edge_class: canonical
  canonical_cognee_edge: true
  source_type: metric_implementation
  target_type: table
```


```yaml
candidate_edge:
  edge_id: edge.jiomart.v9.00483.uses_column
  canonical_edge_type: USES_COLUMN
  source_card_id: metric_impl.jiomart.total_gmv
  target_card_id: column.zs_observe.jiomart_oms.charged_amount
  edge_class: canonical
  canonical_cognee_edge: true
  source_type: metric_implementation
  target_type: column
```


```yaml
candidate_edge:
  edge_id: edge.jiomart.v9.00484.uses_column
  canonical_edge_type: USES_COLUMN
  source_card_id: metric_impl.jiomart.total_gmv
  target_card_id: column.zs_observe.jiomart_oms.transaction_type
  edge_class: canonical
  canonical_cognee_edge: true
  source_type: metric_implementation
  target_type: column
```


```yaml
candidate_edge:
  edge_id: edge.jiomart.v9.00485.belongs_to_domain
  canonical_edge_type: BELONGS_TO_DOMAIN
  source_card_id: metric.jiomart.return_rate
  target_card_id: domain.jiomart.returns
  edge_class: canonical
  canonical_cognee_edge: true
  source_type: metric
  target_type: domain
```


```yaml
candidate_edge:
  edge_id: edge.jiomart.v9.00486.applies_to_platform_context
  canonical_edge_type: APPLIES_TO_PLATFORM_CONTEXT
  source_card_id: metric.jiomart.return_rate
  target_card_id: platform_context.jiomart.in
  edge_class: canonical
  canonical_cognee_edge: true
  source_type: metric
  target_type: platform_context
```


```yaml
candidate_edge:
  edge_id: edge.jiomart.v9.00487.implements_metric
  canonical_edge_type: IMPLEMENTS_METRIC
  source_card_id: metric_impl.jiomart.return_rate
  target_card_id: metric.jiomart.return_rate
  edge_class: canonical
  canonical_cognee_edge: true
  source_type: metric_implementation
  target_type: metric
```


```yaml
candidate_edge:
  edge_id: edge.jiomart.v9.00488.has_implementation
  canonical_edge_type: HAS_IMPLEMENTATION
  source_card_id: metric.jiomart.return_rate
  target_card_id: metric_impl.jiomart.return_rate
  edge_class: canonical
  canonical_cognee_edge: true
  source_type: metric
  target_type: metric_implementation
```


```yaml
candidate_edge:
  edge_id: edge.jiomart.v9.00489.uses_table
  canonical_edge_type: USES_TABLE
  source_card_id: metric_impl.jiomart.return_rate
  target_card_id: table.zs_observe.jiomart_oms
  edge_class: canonical
  canonical_cognee_edge: true
  source_type: metric_implementation
  target_type: table
```


```yaml
candidate_edge:
  edge_id: edge.jiomart.v9.00490.uses_column
  canonical_edge_type: USES_COLUMN
  source_card_id: metric_impl.jiomart.return_rate
  target_card_id: column.zs_observe.jiomart_oms.transaction_type
  edge_class: canonical
  canonical_cognee_edge: true
  source_type: metric_implementation
  target_type: column
```


```yaml
candidate_edge:
  edge_id: edge.jiomart.v9.00491.uses_column
  canonical_edge_type: USES_COLUMN
  source_card_id: metric_impl.jiomart.return_rate
  target_card_id: column.zs_observe.jiomart_oms.order_status
  edge_class: canonical
  canonical_cognee_edge: true
  source_type: metric_implementation
  target_type: column
```


```yaml
candidate_edge:
  edge_id: edge.jiomart.v9.00492.belongs_to_domain
  canonical_edge_type: BELONGS_TO_DOMAIN
  source_card_id: metric.jiomart.average_order_value
  target_card_id: domain.jiomart.orders
  edge_class: canonical
  canonical_cognee_edge: true
  source_type: metric
  target_type: domain
```


```yaml
candidate_edge:
  edge_id: edge.jiomart.v9.00493.applies_to_platform_context
  canonical_edge_type: APPLIES_TO_PLATFORM_CONTEXT
  source_card_id: metric.jiomart.average_order_value
  target_card_id: platform_context.jiomart.in
  edge_class: canonical
  canonical_cognee_edge: true
  source_type: metric
  target_type: platform_context
```


```yaml
candidate_edge:
  edge_id: edge.jiomart.v9.00494.implements_metric
  canonical_edge_type: IMPLEMENTS_METRIC
  source_card_id: metric_impl.jiomart.average_order_value
  target_card_id: metric.jiomart.average_order_value
  edge_class: canonical
  canonical_cognee_edge: true
  source_type: metric_implementation
  target_type: metric
```


```yaml
candidate_edge:
  edge_id: edge.jiomart.v9.00495.has_implementation
  canonical_edge_type: HAS_IMPLEMENTATION
  source_card_id: metric.jiomart.average_order_value
  target_card_id: metric_impl.jiomart.average_order_value
  edge_class: canonical
  canonical_cognee_edge: true
  source_type: metric
  target_type: metric_implementation
```


```yaml
candidate_edge:
  edge_id: edge.jiomart.v9.00496.uses_table
  canonical_edge_type: USES_TABLE
  source_card_id: metric_impl.jiomart.average_order_value
  target_card_id: table.zs_observe.jiomart_oms
  edge_class: canonical
  canonical_cognee_edge: true
  source_type: metric_implementation
  target_type: table
```


```yaml
candidate_edge:
  edge_id: edge.jiomart.v9.00497.uses_column
  canonical_edge_type: USES_COLUMN
  source_card_id: metric_impl.jiomart.average_order_value
  target_card_id: column.zs_observe.jiomart_oms.charged_amount
  edge_class: canonical
  canonical_cognee_edge: true
  source_type: metric_implementation
  target_type: column
```


```yaml
candidate_edge:
  edge_id: edge.jiomart.v9.00498.uses_column
  canonical_edge_type: USES_COLUMN
  source_card_id: metric_impl.jiomart.average_order_value
  target_card_id: column.zs_observe.jiomart_oms.transaction_type
  edge_class: canonical
  canonical_cognee_edge: true
  source_type: metric_implementation
  target_type: column
```


```yaml
candidate_edge:
  edge_id: edge.jiomart.v9.00499.uses_column
  canonical_edge_type: USES_COLUMN
  source_card_id: metric_impl.jiomart.average_order_value
  target_card_id: column.zs_observe.jiomart_oms.order_status
  edge_class: canonical
  canonical_cognee_edge: true
  source_type: metric_implementation
  target_type: column
```


```yaml
candidate_edge:
  edge_id: edge.jiomart.v9.00500.belongs_to_domain
  canonical_edge_type: BELONGS_TO_DOMAIN
  source_card_id: metric.jiomart.net_settled_revenue
  target_card_id: domain.jiomart.settlement
  edge_class: canonical
  canonical_cognee_edge: true
  source_type: metric
  target_type: domain
```


```yaml
candidate_edge:
  edge_id: edge.jiomart.v9.00501.applies_to_platform_context
  canonical_edge_type: APPLIES_TO_PLATFORM_CONTEXT
  source_card_id: metric.jiomart.net_settled_revenue
  target_card_id: platform_context.jiomart.in
  edge_class: canonical
  canonical_cognee_edge: true
  source_type: metric
  target_type: platform_context
```


```yaml
candidate_edge:
  edge_id: edge.jiomart.v9.00502.implements_metric
  canonical_edge_type: IMPLEMENTS_METRIC
  source_card_id: metric_impl.jiomart.net_settled_revenue
  target_card_id: metric.jiomart.net_settled_revenue
  edge_class: canonical
  canonical_cognee_edge: true
  source_type: metric_implementation
  target_type: metric
```


```yaml
candidate_edge:
  edge_id: edge.jiomart.v9.00503.has_implementation
  canonical_edge_type: HAS_IMPLEMENTATION
  source_card_id: metric.jiomart.net_settled_revenue
  target_card_id: metric_impl.jiomart.net_settled_revenue
  edge_class: canonical
  canonical_cognee_edge: true
  source_type: metric
  target_type: metric_implementation
```


```yaml
candidate_edge:
  edge_id: edge.jiomart.v9.00504.uses_table
  canonical_edge_type: USES_TABLE
  source_card_id: metric_impl.jiomart.net_settled_revenue
  target_card_id: table.zs_observe.jiomart_settlement
  edge_class: canonical
  canonical_cognee_edge: true
  source_type: metric_implementation
  target_type: table
```


```yaml
candidate_edge:
  edge_id: edge.jiomart.v9.00505.uses_column
  canonical_edge_type: USES_COLUMN
  source_card_id: metric_impl.jiomart.net_settled_revenue
  target_card_id: column.zs_observe.jiomart_settlement.settled_amount
  edge_class: canonical
  canonical_cognee_edge: true
  source_type: metric_implementation
  target_type: column
```


```yaml
candidate_edge:
  edge_id: edge.jiomart.v9.00506.uses_column
  canonical_edge_type: USES_COLUMN
  source_card_id: metric_impl.jiomart.net_settled_revenue
  target_card_id: column.zs_observe.jiomart_settlement.accountable_type
  edge_class: canonical
  canonical_cognee_edge: true
  source_type: metric_implementation
  target_type: column
```


```yaml
candidate_edge:
  edge_id: edge.jiomart.v9.00507.uses_column
  canonical_edge_type: USES_COLUMN
  source_card_id: metric_impl.jiomart.net_settled_revenue
  target_card_id: column.zs_observe.jiomart_settlement.event
  edge_class: canonical
  canonical_cognee_edge: true
  source_type: metric_implementation
  target_type: column
```


```yaml
candidate_edge:
  edge_id: edge.jiomart.v9.00508.belongs_to_domain
  canonical_edge_type: BELONGS_TO_DOMAIN
  source_card_id: metric.jiomart.seller_coupon_discount_impact
  target_card_id: domain.jiomart.promotions
  edge_class: canonical
  canonical_cognee_edge: true
  source_type: metric
  target_type: domain
```


```yaml
candidate_edge:
  edge_id: edge.jiomart.v9.00509.applies_to_platform_context
  canonical_edge_type: APPLIES_TO_PLATFORM_CONTEXT
  source_card_id: metric.jiomart.seller_coupon_discount_impact
  target_card_id: platform_context.jiomart.in
  edge_class: canonical
  canonical_cognee_edge: true
  source_type: metric
  target_type: platform_context
```


```yaml
candidate_edge:
  edge_id: edge.jiomart.v9.00510.implements_metric
  canonical_edge_type: IMPLEMENTS_METRIC
  source_card_id: metric_impl.jiomart.seller_coupon_discount_impact
  target_card_id: metric.jiomart.seller_coupon_discount_impact
  edge_class: canonical
  canonical_cognee_edge: true
  source_type: metric_implementation
  target_type: metric
```


```yaml
candidate_edge:
  edge_id: edge.jiomart.v9.00511.has_implementation
  canonical_edge_type: HAS_IMPLEMENTATION
  source_card_id: metric.jiomart.seller_coupon_discount_impact
  target_card_id: metric_impl.jiomart.seller_coupon_discount_impact
  edge_class: canonical
  canonical_cognee_edge: true
  source_type: metric
  target_type: metric_implementation
```


```yaml
candidate_edge:
  edge_id: edge.jiomart.v9.00512.uses_table
  canonical_edge_type: USES_TABLE
  source_card_id: metric_impl.jiomart.seller_coupon_discount_impact
  target_card_id: table.zs_observe.jiomart_oms
  edge_class: canonical
  canonical_cognee_edge: true
  source_type: metric_implementation
  target_type: table
```


```yaml
candidate_edge:
  edge_id: edge.jiomart.v9.00513.uses_column
  canonical_edge_type: USES_COLUMN
  source_card_id: metric_impl.jiomart.seller_coupon_discount_impact
  target_card_id: column.zs_observe.jiomart_oms.seller_coupon_code
  edge_class: canonical
  canonical_cognee_edge: true
  source_type: metric_implementation
  target_type: column
```


```yaml
candidate_edge:
  edge_id: edge.jiomart.v9.00514.uses_column
  canonical_edge_type: USES_COLUMN
  source_card_id: metric_impl.jiomart.seller_coupon_discount_impact
  target_card_id: column.zs_observe.jiomart_oms.seller_coupon_amount
  edge_class: canonical
  canonical_cognee_edge: true
  source_type: metric_implementation
  target_type: column
```


```yaml
candidate_edge:
  edge_id: edge.jiomart.v9.00515.belongs_to_domain
  canonical_edge_type: BELONGS_TO_DOMAIN
  source_card_id: metric.jiomart.monthly_forward_orders_gmv
  target_card_id: domain.jiomart.orders
  edge_class: canonical
  canonical_cognee_edge: true
  source_type: metric
  target_type: domain
```


```yaml
candidate_edge:
  edge_id: edge.jiomart.v9.00516.applies_to_platform_context
  canonical_edge_type: APPLIES_TO_PLATFORM_CONTEXT
  source_card_id: metric.jiomart.monthly_forward_orders_gmv
  target_card_id: platform_context.jiomart.in
  edge_class: canonical
  canonical_cognee_edge: true
  source_type: metric
  target_type: platform_context
```


```yaml
candidate_edge:
  edge_id: edge.jiomart.v9.00517.implements_metric
  canonical_edge_type: IMPLEMENTS_METRIC
  source_card_id: metric_impl.jiomart.monthly_forward_orders_and_gmv
  target_card_id: metric.jiomart.monthly_forward_orders_gmv
  edge_class: canonical
  canonical_cognee_edge: true
  source_type: metric_implementation
  target_type: metric
```


```yaml
candidate_edge:
  edge_id: edge.jiomart.v9.00518.has_implementation
  canonical_edge_type: HAS_IMPLEMENTATION
  source_card_id: metric.jiomart.monthly_forward_orders_gmv
  target_card_id: metric_impl.jiomart.monthly_forward_orders_and_gmv
  edge_class: canonical
  canonical_cognee_edge: true
  source_type: metric
  target_type: metric_implementation
```


```yaml
candidate_edge:
  edge_id: edge.jiomart.v9.00519.uses_table
  canonical_edge_type: USES_TABLE
  source_card_id: metric_impl.jiomart.monthly_forward_orders_and_gmv
  target_card_id: table.zs_observe.jiomart_oms
  edge_class: canonical
  canonical_cognee_edge: true
  source_type: metric_implementation
  target_type: table
```


```yaml
candidate_edge:
  edge_id: edge.jiomart.v9.00520.uses_column
  canonical_edge_type: USES_COLUMN
  source_card_id: metric_impl.jiomart.monthly_forward_orders_and_gmv
  target_card_id: column.zs_observe.jiomart_oms.created_date
  edge_class: canonical
  canonical_cognee_edge: true
  source_type: metric_implementation
  target_type: column
```


```yaml
candidate_edge:
  edge_id: edge.jiomart.v9.00521.uses_column
  canonical_edge_type: USES_COLUMN
  source_card_id: metric_impl.jiomart.monthly_forward_orders_and_gmv
  target_card_id: column.zs_observe.jiomart_oms.charged_amount
  edge_class: canonical
  canonical_cognee_edge: true
  source_type: metric_implementation
  target_type: column
```


```yaml
candidate_edge:
  edge_id: edge.jiomart.v9.00522.belongs_to_domain
  canonical_edge_type: BELONGS_TO_DOMAIN
  source_card_id: metric.jiomart.shipment_status_gmv
  target_card_id: domain.jiomart.orders
  edge_class: canonical
  canonical_cognee_edge: true
  source_type: metric
  target_type: domain
```


```yaml
candidate_edge:
  edge_id: edge.jiomart.v9.00523.applies_to_platform_context
  canonical_edge_type: APPLIES_TO_PLATFORM_CONTEXT
  source_card_id: metric.jiomart.shipment_status_gmv
  target_card_id: platform_context.jiomart.in
  edge_class: canonical
  canonical_cognee_edge: true
  source_type: metric
  target_type: platform_context
```


```yaml
candidate_edge:
  edge_id: edge.jiomart.v9.00524.implements_metric
  canonical_edge_type: IMPLEMENTS_METRIC
  source_card_id: metric_impl.jiomart.shipment_status_summary
  target_card_id: metric.jiomart.shipment_status_gmv
  edge_class: canonical
  canonical_cognee_edge: true
  source_type: metric_implementation
  target_type: metric
```


```yaml
candidate_edge:
  edge_id: edge.jiomart.v9.00525.has_implementation
  canonical_edge_type: HAS_IMPLEMENTATION
  source_card_id: metric.jiomart.shipment_status_gmv
  target_card_id: metric_impl.jiomart.shipment_status_summary
  edge_class: canonical
  canonical_cognee_edge: true
  source_type: metric
  target_type: metric_implementation
```


```yaml
candidate_edge:
  edge_id: edge.jiomart.v9.00526.uses_table
  canonical_edge_type: USES_TABLE
  source_card_id: metric_impl.jiomart.shipment_status_summary
  target_card_id: table.zs_observe.jiomart_shipment
  edge_class: canonical
  canonical_cognee_edge: true
  source_type: metric_implementation
  target_type: table
```


```yaml
candidate_edge:
  edge_id: edge.jiomart.v9.00527.uses_column
  canonical_edge_type: USES_COLUMN
  source_card_id: metric_impl.jiomart.shipment_status_summary
  target_card_id: column.zs_observe.jiomart_shipment.order_status
  edge_class: canonical
  canonical_cognee_edge: true
  source_type: metric_implementation
  target_type: column
```


```yaml
candidate_edge:
  edge_id: edge.jiomart.v9.00528.uses_column
  canonical_edge_type: USES_COLUMN
  source_card_id: metric_impl.jiomart.shipment_status_summary
  target_card_id: column.zs_observe.jiomart_shipment.charged_amount
  edge_class: canonical
  canonical_cognee_edge: true
  source_type: metric_implementation
  target_type: column
```


```yaml
candidate_edge:
  edge_id: edge.jiomart.v9.00529.uses_column
  canonical_edge_type: USES_COLUMN
  source_card_id: metric_impl.jiomart.shipment_status_summary
  target_card_id: column.zs_observe.jiomart_shipment.mrp
  edge_class: canonical
  canonical_cognee_edge: true
  source_type: metric_implementation
  target_type: column
```


```yaml
candidate_edge:
  edge_id: edge.jiomart.v9.00530.uses_column
  canonical_edge_type: USES_COLUMN
  source_card_id: metric_impl.jiomart.shipment_status_summary
  target_card_id: column.zs_observe.jiomart_shipment.item_promo_discount
  edge_class: canonical
  canonical_cognee_edge: true
  source_type: metric_implementation
  target_type: column
```


```yaml
candidate_edge:
  edge_id: edge.jiomart.v9.00531.belongs_to_domain
  canonical_edge_type: BELONGS_TO_DOMAIN
  source_card_id: metric.jiomart.shipment_monthly_gmv
  target_card_id: domain.jiomart.orders
  edge_class: canonical
  canonical_cognee_edge: true
  source_type: metric
  target_type: domain
```


```yaml
candidate_edge:
  edge_id: edge.jiomart.v9.00532.applies_to_platform_context
  canonical_edge_type: APPLIES_TO_PLATFORM_CONTEXT
  source_card_id: metric.jiomart.shipment_monthly_gmv
  target_card_id: platform_context.jiomart.in
  edge_class: canonical
  canonical_cognee_edge: true
  source_type: metric
  target_type: platform_context
```


```yaml
candidate_edge:
  edge_id: edge.jiomart.v9.00533.implements_metric
  canonical_edge_type: IMPLEMENTS_METRIC
  source_card_id: metric_impl.jiomart.shipment_monthly_gmv
  target_card_id: metric.jiomart.shipment_monthly_gmv
  edge_class: canonical
  canonical_cognee_edge: true
  source_type: metric_implementation
  target_type: metric
```


```yaml
candidate_edge:
  edge_id: edge.jiomart.v9.00534.has_implementation
  canonical_edge_type: HAS_IMPLEMENTATION
  source_card_id: metric.jiomart.shipment_monthly_gmv
  target_card_id: metric_impl.jiomart.shipment_monthly_gmv
  edge_class: canonical
  canonical_cognee_edge: true
  source_type: metric
  target_type: metric_implementation
```


```yaml
candidate_edge:
  edge_id: edge.jiomart.v9.00535.uses_table
  canonical_edge_type: USES_TABLE
  source_card_id: metric_impl.jiomart.shipment_monthly_gmv
  target_card_id: table.zs_observe.jiomart_shipment
  edge_class: canonical
  canonical_cognee_edge: true
  source_type: metric_implementation
  target_type: table
```


```yaml
candidate_edge:
  edge_id: edge.jiomart.v9.00536.uses_column
  canonical_edge_type: USES_COLUMN
  source_card_id: metric_impl.jiomart.shipment_monthly_gmv
  target_card_id: column.zs_observe.jiomart_shipment.created_date
  edge_class: canonical
  canonical_cognee_edge: true
  source_type: metric_implementation
  target_type: column
```


```yaml
candidate_edge:
  edge_id: edge.jiomart.v9.00537.uses_column
  canonical_edge_type: USES_COLUMN
  source_card_id: metric_impl.jiomart.shipment_monthly_gmv
  target_card_id: column.zs_observe.jiomart_shipment.charged_amount
  edge_class: canonical
  canonical_cognee_edge: true
  source_type: metric_implementation
  target_type: column
```


```yaml
candidate_edge:
  edge_id: edge.jiomart.v9.00538.uses_column
  canonical_edge_type: USES_COLUMN
  source_card_id: metric_impl.jiomart.shipment_monthly_gmv
  target_card_id: column.zs_observe.jiomart_shipment.item_promo_discount
  edge_class: canonical
  canonical_cognee_edge: true
  source_type: metric_implementation
  target_type: column
```


```yaml
candidate_edge:
  edge_id: edge.jiomart.v9.00539.belongs_to_domain
  canonical_edge_type: BELONGS_TO_DOMAIN
  source_card_id: metric.jiomart.top_shipment_skus
  target_card_id: domain.jiomart.product
  edge_class: canonical
  canonical_cognee_edge: true
  source_type: metric
  target_type: domain
```


```yaml
candidate_edge:
  edge_id: edge.jiomart.v9.00540.applies_to_platform_context
  canonical_edge_type: APPLIES_TO_PLATFORM_CONTEXT
  source_card_id: metric.jiomart.top_shipment_skus
  target_card_id: platform_context.jiomart.in
  edge_class: canonical
  canonical_cognee_edge: true
  source_type: metric
  target_type: platform_context
```


```yaml
candidate_edge:
  edge_id: edge.jiomart.v9.00541.implements_metric
  canonical_edge_type: IMPLEMENTS_METRIC
  source_card_id: metric_impl.jiomart.top_shipment_skus
  target_card_id: metric.jiomart.top_shipment_skus
  edge_class: canonical
  canonical_cognee_edge: true
  source_type: metric_implementation
  target_type: metric
```


```yaml
candidate_edge:
  edge_id: edge.jiomart.v9.00542.has_implementation
  canonical_edge_type: HAS_IMPLEMENTATION
  source_card_id: metric.jiomart.top_shipment_skus
  target_card_id: metric_impl.jiomart.top_shipment_skus
  edge_class: canonical
  canonical_cognee_edge: true
  source_type: metric
  target_type: metric_implementation
```


```yaml
candidate_edge:
  edge_id: edge.jiomart.v9.00543.uses_table
  canonical_edge_type: USES_TABLE
  source_card_id: metric_impl.jiomart.top_shipment_skus
  target_card_id: table.zs_observe.jiomart_shipment
  edge_class: canonical
  canonical_cognee_edge: true
  source_type: metric_implementation
  target_type: table
```


```yaml
candidate_edge:
  edge_id: edge.jiomart.v9.00544.uses_column
  canonical_edge_type: USES_COLUMN
  source_card_id: metric_impl.jiomart.top_shipment_skus
  target_card_id: column.zs_observe.jiomart_shipment.sku_id
  edge_class: canonical
  canonical_cognee_edge: true
  source_type: metric_implementation
  target_type: column
```


```yaml
candidate_edge:
  edge_id: edge.jiomart.v9.00545.uses_column
  canonical_edge_type: USES_COLUMN
  source_card_id: metric_impl.jiomart.top_shipment_skus
  target_card_id: column.zs_observe.jiomart_shipment.charged_amount
  edge_class: canonical
  canonical_cognee_edge: true
  source_type: metric_implementation
  target_type: column
```


```yaml
candidate_edge:
  edge_id: edge.jiomart.v9.00546.uses_column
  canonical_edge_type: USES_COLUMN
  source_card_id: metric_impl.jiomart.top_shipment_skus
  target_card_id: column.zs_observe.jiomart_shipment.item_promo_discount
  edge_class: canonical
  canonical_cognee_edge: true
  source_type: metric_implementation
  target_type: column
```


```yaml
candidate_edge:
  edge_id: edge.jiomart.v9.00547.belongs_to_domain
  canonical_edge_type: BELONGS_TO_DOMAIN
  source_card_id: metric.jiomart.net_settlement_per_order
  target_card_id: domain.jiomart.settlement
  edge_class: canonical
  canonical_cognee_edge: true
  source_type: metric
  target_type: domain
```


```yaml
candidate_edge:
  edge_id: edge.jiomart.v9.00548.applies_to_platform_context
  canonical_edge_type: APPLIES_TO_PLATFORM_CONTEXT
  source_card_id: metric.jiomart.net_settlement_per_order
  target_card_id: platform_context.jiomart.in
  edge_class: canonical
  canonical_cognee_edge: true
  source_type: metric
  target_type: platform_context
```


```yaml
candidate_edge:
  edge_id: edge.jiomart.v9.00549.implements_metric
  canonical_edge_type: IMPLEMENTS_METRIC
  source_card_id: metric_impl.jiomart.net_settlement_per_order
  target_card_id: metric.jiomart.net_settlement_per_order
  edge_class: canonical
  canonical_cognee_edge: true
  source_type: metric_implementation
  target_type: metric
```


```yaml
candidate_edge:
  edge_id: edge.jiomart.v9.00550.has_implementation
  canonical_edge_type: HAS_IMPLEMENTATION
  source_card_id: metric.jiomart.net_settlement_per_order
  target_card_id: metric_impl.jiomart.net_settlement_per_order
  edge_class: canonical
  canonical_cognee_edge: true
  source_type: metric
  target_type: metric_implementation
```


```yaml
candidate_edge:
  edge_id: edge.jiomart.v9.00551.uses_table
  canonical_edge_type: USES_TABLE
  source_card_id: metric_impl.jiomart.net_settlement_per_order
  target_card_id: table.zs_observe.jiomart_settlement
  edge_class: canonical
  canonical_cognee_edge: true
  source_type: metric_implementation
  target_type: table
```


```yaml
candidate_edge:
  edge_id: edge.jiomart.v9.00552.uses_column
  canonical_edge_type: USES_COLUMN
  source_card_id: metric_impl.jiomart.net_settlement_per_order
  target_card_id: column.zs_observe.jiomart_settlement.order_id
  edge_class: canonical
  canonical_cognee_edge: true
  source_type: metric_implementation
  target_type: column
```


```yaml
candidate_edge:
  edge_id: edge.jiomart.v9.00553.uses_column
  canonical_edge_type: USES_COLUMN
  source_card_id: metric_impl.jiomart.net_settlement_per_order
  target_card_id: column.zs_observe.jiomart_settlement.settled_amount
  edge_class: canonical
  canonical_cognee_edge: true
  source_type: metric_implementation
  target_type: column
```


```yaml
candidate_edge:
  edge_id: edge.jiomart.v9.00554.uses_column
  canonical_edge_type: USES_COLUMN
  source_card_id: metric_impl.jiomart.net_settlement_per_order
  target_card_id: column.zs_observe.jiomart_settlement.accountable_type
  edge_class: canonical
  canonical_cognee_edge: true
  source_type: metric_implementation
  target_type: column
```


```yaml
candidate_edge:
  edge_id: edge.jiomart.v9.00555.belongs_to_domain
  canonical_edge_type: BELONGS_TO_DOMAIN
  source_card_id: metric.jiomart.monthly_settlement_summary
  target_card_id: domain.jiomart.settlement
  edge_class: canonical
  canonical_cognee_edge: true
  source_type: metric
  target_type: domain
```


```yaml
candidate_edge:
  edge_id: edge.jiomart.v9.00556.applies_to_platform_context
  canonical_edge_type: APPLIES_TO_PLATFORM_CONTEXT
  source_card_id: metric.jiomart.monthly_settlement_summary
  target_card_id: platform_context.jiomart.in
  edge_class: canonical
  canonical_cognee_edge: true
  source_type: metric
  target_type: platform_context
```


```yaml
candidate_edge:
  edge_id: edge.jiomart.v9.00557.implements_metric
  canonical_edge_type: IMPLEMENTS_METRIC
  source_card_id: metric_impl.jiomart.monthly_settlement_summary
  target_card_id: metric.jiomart.monthly_settlement_summary
  edge_class: canonical
  canonical_cognee_edge: true
  source_type: metric_implementation
  target_type: metric
```


```yaml
candidate_edge:
  edge_id: edge.jiomart.v9.00558.has_implementation
  canonical_edge_type: HAS_IMPLEMENTATION
  source_card_id: metric.jiomart.monthly_settlement_summary
  target_card_id: metric_impl.jiomart.monthly_settlement_summary
  edge_class: canonical
  canonical_cognee_edge: true
  source_type: metric
  target_type: metric_implementation
```


```yaml
candidate_edge:
  edge_id: edge.jiomart.v9.00559.uses_table
  canonical_edge_type: USES_TABLE
  source_card_id: metric_impl.jiomart.monthly_settlement_summary
  target_card_id: table.zs_observe.jiomart_settlement
  edge_class: canonical
  canonical_cognee_edge: true
  source_type: metric_implementation
  target_type: table
```


```yaml
candidate_edge:
  edge_id: edge.jiomart.v9.00560.uses_column
  canonical_edge_type: USES_COLUMN
  source_card_id: metric_impl.jiomart.monthly_settlement_summary
  target_card_id: column.zs_observe.jiomart_settlement.settlement_date
  edge_class: canonical
  canonical_cognee_edge: true
  source_type: metric_implementation
  target_type: column
```


```yaml
candidate_edge:
  edge_id: edge.jiomart.v9.00561.uses_column
  canonical_edge_type: USES_COLUMN
  source_card_id: metric_impl.jiomart.monthly_settlement_summary
  target_card_id: column.zs_observe.jiomart_settlement.transaction_type
  edge_class: canonical
  canonical_cognee_edge: true
  source_type: metric_implementation
  target_type: column
```


```yaml
candidate_edge:
  edge_id: edge.jiomart.v9.00562.uses_column
  canonical_edge_type: USES_COLUMN
  source_card_id: metric_impl.jiomart.monthly_settlement_summary
  target_card_id: column.zs_observe.jiomart_settlement.accountable_type
  edge_class: canonical
  canonical_cognee_edge: true
  source_type: metric_implementation
  target_type: column
```


```yaml
candidate_edge:
  edge_id: edge.jiomart.v9.00563.uses_column
  canonical_edge_type: USES_COLUMN
  source_card_id: metric_impl.jiomart.monthly_settlement_summary
  target_card_id: column.zs_observe.jiomart_settlement.settled_amount
  edge_class: canonical
  canonical_cognee_edge: true
  source_type: metric_implementation
  target_type: column
```


```yaml
candidate_edge:
  edge_id: edge.jiomart.v9.00564.belongs_to_domain
  canonical_edge_type: BELONGS_TO_DOMAIN
  source_card_id: metric.jiomart.credit_debit_note_impact
  target_card_id: domain.jiomart.settlement
  edge_class: canonical
  canonical_cognee_edge: true
  source_type: metric
  target_type: domain
```


```yaml
candidate_edge:
  edge_id: edge.jiomart.v9.00565.applies_to_platform_context
  canonical_edge_type: APPLIES_TO_PLATFORM_CONTEXT
  source_card_id: metric.jiomart.credit_debit_note_impact
  target_card_id: platform_context.jiomart.in
  edge_class: canonical
  canonical_cognee_edge: true
  source_type: metric
  target_type: platform_context
```


```yaml
candidate_edge:
  edge_id: edge.jiomart.v9.00566.implements_metric
  canonical_edge_type: IMPLEMENTS_METRIC
  source_card_id: metric_impl.jiomart.credit_debit_note_impact
  target_card_id: metric.jiomart.credit_debit_note_impact
  edge_class: canonical
  canonical_cognee_edge: true
  source_type: metric_implementation
  target_type: metric
```


```yaml
candidate_edge:
  edge_id: edge.jiomart.v9.00567.has_implementation
  canonical_edge_type: HAS_IMPLEMENTATION
  source_card_id: metric.jiomart.credit_debit_note_impact
  target_card_id: metric_impl.jiomart.credit_debit_note_impact
  edge_class: canonical
  canonical_cognee_edge: true
  source_type: metric
  target_type: metric_implementation
```


```yaml
candidate_edge:
  edge_id: edge.jiomart.v9.00568.uses_table
  canonical_edge_type: USES_TABLE
  source_card_id: metric_impl.jiomart.credit_debit_note_impact
  target_card_id: table.zs_observe.jiomart_settlement
  edge_class: canonical
  canonical_cognee_edge: true
  source_type: metric_implementation
  target_type: table
```


```yaml
candidate_edge:
  edge_id: edge.jiomart.v9.00569.uses_column
  canonical_edge_type: USES_COLUMN
  source_card_id: metric_impl.jiomart.credit_debit_note_impact
  target_card_id: column.zs_observe.jiomart_settlement.transaction_type
  edge_class: canonical
  canonical_cognee_edge: true
  source_type: metric_implementation
  target_type: column
```


```yaml
candidate_edge:
  edge_id: edge.jiomart.v9.00570.uses_column
  canonical_edge_type: USES_COLUMN
  source_card_id: metric_impl.jiomart.credit_debit_note_impact
  target_card_id: column.zs_observe.jiomart_settlement.event
  edge_class: canonical
  canonical_cognee_edge: true
  source_type: metric_implementation
  target_type: column
```


```yaml
candidate_edge:
  edge_id: edge.jiomart.v9.00571.uses_column
  canonical_edge_type: USES_COLUMN
  source_card_id: metric_impl.jiomart.credit_debit_note_impact
  target_card_id: column.zs_observe.jiomart_settlement.accountable_type
  edge_class: canonical
  canonical_cognee_edge: true
  source_type: metric_implementation
  target_type: column
```


```yaml
candidate_edge:
  edge_id: edge.jiomart.v9.00572.uses_column
  canonical_edge_type: USES_COLUMN
  source_card_id: metric_impl.jiomart.credit_debit_note_impact
  target_card_id: column.zs_observe.jiomart_settlement.settled_amount
  edge_class: canonical
  canonical_cognee_edge: true
  source_type: metric_implementation
  target_type: column
```


```yaml
candidate_edge:
  edge_id: edge.jiomart.v9.00573.belongs_to_domain
  canonical_edge_type: BELONGS_TO_DOMAIN
  source_card_id: metric.jiomart.return_volume_by_type
  target_card_id: domain.jiomart.returns
  edge_class: canonical
  canonical_cognee_edge: true
  source_type: metric
  target_type: domain
```


```yaml
candidate_edge:
  edge_id: edge.jiomart.v9.00574.applies_to_platform_context
  canonical_edge_type: APPLIES_TO_PLATFORM_CONTEXT
  source_card_id: metric.jiomart.return_volume_by_type
  target_card_id: platform_context.jiomart.in
  edge_class: canonical
  canonical_cognee_edge: true
  source_type: metric
  target_type: platform_context
```


```yaml
candidate_edge:
  edge_id: edge.jiomart.v9.00575.implements_metric
  canonical_edge_type: IMPLEMENTS_METRIC
  source_card_id: metric_impl.jiomart.return_volume_by_type
  target_card_id: metric.jiomart.return_volume_by_type
  edge_class: canonical
  canonical_cognee_edge: true
  source_type: metric_implementation
  target_type: metric
```


```yaml
candidate_edge:
  edge_id: edge.jiomart.v9.00576.has_implementation
  canonical_edge_type: HAS_IMPLEMENTATION
  source_card_id: metric.jiomart.return_volume_by_type
  target_card_id: metric_impl.jiomart.return_volume_by_type
  edge_class: canonical
  canonical_cognee_edge: true
  source_type: metric
  target_type: metric_implementation
```


```yaml
candidate_edge:
  edge_id: edge.jiomart.v9.00577.uses_table
  canonical_edge_type: USES_TABLE
  source_card_id: metric_impl.jiomart.return_volume_by_type
  target_card_id: table.zs_observe.jiomart_returns
  edge_class: canonical
  canonical_cognee_edge: true
  source_type: metric_implementation
  target_type: table
```


```yaml
candidate_edge:
  edge_id: edge.jiomart.v9.00578.uses_column
  canonical_edge_type: USES_COLUMN
  source_card_id: metric_impl.jiomart.return_volume_by_type
  target_card_id: column.zs_observe.jiomart_returns.return_type
  edge_class: canonical
  canonical_cognee_edge: true
  source_type: metric_implementation
  target_type: column
```


```yaml
candidate_edge:
  edge_id: edge.jiomart.v9.00579.uses_column
  canonical_edge_type: USES_COLUMN
  source_card_id: metric_impl.jiomart.return_volume_by_type
  target_card_id: column.zs_observe.jiomart_returns.refund_amount
  edge_class: canonical
  canonical_cognee_edge: true
  source_type: metric_implementation
  target_type: column
```


```yaml
candidate_edge:
  edge_id: edge.jiomart.v9.00580.belongs_to_domain
  canonical_edge_type: BELONGS_TO_DOMAIN
  source_card_id: metric.jiomart.return_cycle_time
  target_card_id: domain.jiomart.returns
  edge_class: canonical
  canonical_cognee_edge: true
  source_type: metric
  target_type: domain
```


```yaml
candidate_edge:
  edge_id: edge.jiomart.v9.00581.applies_to_platform_context
  canonical_edge_type: APPLIES_TO_PLATFORM_CONTEXT
  source_card_id: metric.jiomart.return_cycle_time
  target_card_id: platform_context.jiomart.in
  edge_class: canonical
  canonical_cognee_edge: true
  source_type: metric
  target_type: platform_context
```


```yaml
candidate_edge:
  edge_id: edge.jiomart.v9.00582.implements_metric
  canonical_edge_type: IMPLEMENTS_METRIC
  source_card_id: metric_impl.jiomart.return_cycle_time
  target_card_id: metric.jiomart.return_cycle_time
  edge_class: canonical
  canonical_cognee_edge: true
  source_type: metric_implementation
  target_type: metric
```


```yaml
candidate_edge:
  edge_id: edge.jiomart.v9.00583.has_implementation
  canonical_edge_type: HAS_IMPLEMENTATION
  source_card_id: metric.jiomart.return_cycle_time
  target_card_id: metric_impl.jiomart.return_cycle_time
  edge_class: canonical
  canonical_cognee_edge: true
  source_type: metric
  target_type: metric_implementation
```


```yaml
candidate_edge:
  edge_id: edge.jiomart.v9.00584.uses_table
  canonical_edge_type: USES_TABLE
  source_card_id: metric_impl.jiomart.return_cycle_time
  target_card_id: table.zs_observe.jiomart_returns
  edge_class: canonical
  canonical_cognee_edge: true
  source_type: metric_implementation
  target_type: table
```


```yaml
candidate_edge:
  edge_id: edge.jiomart.v9.00585.uses_column
  canonical_edge_type: USES_COLUMN
  source_card_id: metric_impl.jiomart.return_cycle_time
  target_card_id: column.zs_observe.jiomart_returns.return_initiate_date
  edge_class: canonical
  canonical_cognee_edge: true
  source_type: metric_implementation
  target_type: column
```


```yaml
candidate_edge:
  edge_id: edge.jiomart.v9.00586.uses_column
  canonical_edge_type: USES_COLUMN
  source_card_id: metric_impl.jiomart.return_cycle_time
  target_card_id: column.zs_observe.jiomart_returns.return_delivery_date
  edge_class: canonical
  canonical_cognee_edge: true
  source_type: metric_implementation
  target_type: column
```


```yaml
candidate_edge:
  edge_id: edge.jiomart.v9.00587.belongs_to_domain
  canonical_edge_type: BELONGS_TO_DOMAIN
  source_card_id: metric.jiomart.sku_return_rate
  target_card_id: domain.jiomart.returns
  edge_class: canonical
  canonical_cognee_edge: true
  source_type: metric
  target_type: domain
```


```yaml
candidate_edge:
  edge_id: edge.jiomart.v9.00588.applies_to_platform_context
  canonical_edge_type: APPLIES_TO_PLATFORM_CONTEXT
  source_card_id: metric.jiomart.sku_return_rate
  target_card_id: platform_context.jiomart.in
  edge_class: canonical
  canonical_cognee_edge: true
  source_type: metric
  target_type: platform_context
```


```yaml
candidate_edge:
  edge_id: edge.jiomart.v9.00589.implements_metric
  canonical_edge_type: IMPLEMENTS_METRIC
  source_card_id: metric_impl.jiomart.sku_level_return_rate
  target_card_id: metric.jiomart.sku_return_rate
  edge_class: canonical
  canonical_cognee_edge: true
  source_type: metric_implementation
  target_type: metric
```


```yaml
candidate_edge:
  edge_id: edge.jiomart.v9.00590.has_implementation
  canonical_edge_type: HAS_IMPLEMENTATION
  source_card_id: metric.jiomart.sku_return_rate
  target_card_id: metric_impl.jiomart.sku_level_return_rate
  edge_class: canonical
  canonical_cognee_edge: true
  source_type: metric
  target_type: metric_implementation
```


```yaml
candidate_edge:
  edge_id: edge.jiomart.v9.00591.uses_table
  canonical_edge_type: USES_TABLE
  source_card_id: metric_impl.jiomart.sku_level_return_rate
  target_card_id: table.zs_observe.jiomart_returns
  edge_class: canonical
  canonical_cognee_edge: true
  source_type: metric_implementation
  target_type: table
```


```yaml
candidate_edge:
  edge_id: edge.jiomart.v9.00592.uses_column
  canonical_edge_type: USES_COLUMN
  source_card_id: metric_impl.jiomart.sku_level_return_rate
  target_card_id: column.zs_observe.jiomart_returns.sku_id
  edge_class: canonical
  canonical_cognee_edge: true
  source_type: metric_implementation
  target_type: column
```


```yaml
candidate_edge:
  edge_id: edge.jiomart.v9.00593.uses_column
  canonical_edge_type: USES_COLUMN
  source_card_id: metric_impl.jiomart.sku_level_return_rate
  target_card_id: column.zs_observe.jiomart_returns.refund_amount
  edge_class: canonical
  canonical_cognee_edge: true
  source_type: metric_implementation
  target_type: column
```


```yaml
candidate_edge:
  edge_id: edge.jiomart.v9.00594.belongs_to_domain
  canonical_edge_type: BELONGS_TO_DOMAIN
  source_card_id: metric.jiomart.oms_monthly_gmv_clean
  target_card_id: domain.jiomart.orders
  edge_class: canonical
  canonical_cognee_edge: true
  source_type: metric
  target_type: domain
```


```yaml
candidate_edge:
  edge_id: edge.jiomart.v9.00595.applies_to_platform_context
  canonical_edge_type: APPLIES_TO_PLATFORM_CONTEXT
  source_card_id: metric.jiomart.oms_monthly_gmv_clean
  target_card_id: platform_context.jiomart.in
  edge_class: canonical
  canonical_cognee_edge: true
  source_type: metric
  target_type: platform_context
```


```yaml
candidate_edge:
  edge_id: edge.jiomart.v9.00596.implements_metric
  canonical_edge_type: IMPLEMENTS_METRIC
  source_card_id: metric_impl.jiomart.oms_monthly_gmv_clean_rows
  target_card_id: metric.jiomart.oms_monthly_gmv_clean
  edge_class: canonical
  canonical_cognee_edge: true
  source_type: metric_implementation
  target_type: metric
```


```yaml
candidate_edge:
  edge_id: edge.jiomart.v9.00597.has_implementation
  canonical_edge_type: HAS_IMPLEMENTATION
  source_card_id: metric.jiomart.oms_monthly_gmv_clean
  target_card_id: metric_impl.jiomart.oms_monthly_gmv_clean_rows
  edge_class: canonical
  canonical_cognee_edge: true
  source_type: metric
  target_type: metric_implementation
```


```yaml
candidate_edge:
  edge_id: edge.jiomart.v9.00598.uses_table
  canonical_edge_type: USES_TABLE
  source_card_id: metric_impl.jiomart.oms_monthly_gmv_clean_rows
  target_card_id: table.zs_observe.jiomart_oms
  edge_class: canonical
  canonical_cognee_edge: true
  source_type: metric_implementation
  target_type: table
```


```yaml
candidate_edge:
  edge_id: edge.jiomart.v9.00599.uses_column
  canonical_edge_type: USES_COLUMN
  source_card_id: metric_impl.jiomart.oms_monthly_gmv_clean_rows
  target_card_id: column.zs_observe.jiomart_oms.created_date
  edge_class: canonical
  canonical_cognee_edge: true
  source_type: metric_implementation
  target_type: column
```


```yaml
candidate_edge:
  edge_id: edge.jiomart.v9.00600.uses_column
  canonical_edge_type: USES_COLUMN
  source_card_id: metric_impl.jiomart.oms_monthly_gmv_clean_rows
  target_card_id: column.zs_observe.jiomart_oms.charged_amount
  edge_class: canonical
  canonical_cognee_edge: true
  source_type: metric_implementation
  target_type: column
```


```yaml
candidate_edge:
  edge_id: edge.jiomart.v9.00601.uses_column
  canonical_edge_type: USES_COLUMN
  source_card_id: metric_impl.jiomart.oms_monthly_gmv_clean_rows
  target_card_id: column.zs_observe.jiomart_oms.transaction_type
  edge_class: canonical
  canonical_cognee_edge: true
  source_type: metric_implementation
  target_type: column
```


```yaml
candidate_edge:
  edge_id: edge.jiomart.v9.00602.uses_column
  canonical_edge_type: USES_COLUMN
  source_card_id: metric_impl.jiomart.oms_monthly_gmv_clean_rows
  target_card_id: column.zs_observe.jiomart_oms.hsn
  edge_class: canonical
  canonical_cognee_edge: true
  source_type: metric_implementation
  target_type: column
```


```yaml
candidate_edge:
  edge_id: edge.jiomart.v9.00603.uses_column
  canonical_edge_type: USES_COLUMN
  source_card_id: metric_impl.jiomart.oms_monthly_gmv_clean_rows
  target_card_id: column.zs_observe.jiomart_oms.order_date
  edge_class: canonical
  canonical_cognee_edge: true
  source_type: metric_implementation
  target_type: column
```


```yaml
candidate_edge:
  edge_id: edge.jiomart.v9.00604.belongs_to_domain
  canonical_edge_type: BELONGS_TO_DOMAIN
  source_card_id: metric.jiomart.gst_breakdown
  target_card_id: domain.jiomart.tax
  edge_class: canonical
  canonical_cognee_edge: true
  source_type: metric
  target_type: domain
```


```yaml
candidate_edge:
  edge_id: edge.jiomart.v9.00605.applies_to_platform_context
  canonical_edge_type: APPLIES_TO_PLATFORM_CONTEXT
  source_card_id: metric.jiomart.gst_breakdown
  target_card_id: platform_context.jiomart.in
  edge_class: canonical
  canonical_cognee_edge: true
  source_type: metric
  target_type: platform_context
```


```yaml
candidate_edge:
  edge_id: edge.jiomart.v9.00606.implements_metric
  canonical_edge_type: IMPLEMENTS_METRIC
  source_card_id: metric_impl.jiomart.intra_state_vs_inter_state_gst
  target_card_id: metric.jiomart.gst_breakdown
  edge_class: canonical
  canonical_cognee_edge: true
  source_type: metric_implementation
  target_type: metric
```


```yaml
candidate_edge:
  edge_id: edge.jiomart.v9.00607.has_implementation
  canonical_edge_type: HAS_IMPLEMENTATION
  source_card_id: metric.jiomart.gst_breakdown
  target_card_id: metric_impl.jiomart.intra_state_vs_inter_state_gst
  edge_class: canonical
  canonical_cognee_edge: true
  source_type: metric
  target_type: metric_implementation
```


```yaml
candidate_edge:
  edge_id: edge.jiomart.v9.00608.uses_table
  canonical_edge_type: USES_TABLE
  source_card_id: metric_impl.jiomart.intra_state_vs_inter_state_gst
  target_card_id: table.zs_observe.jiomart_oms
  edge_class: canonical
  canonical_cognee_edge: true
  source_type: metric_implementation
  target_type: table
```


```yaml
candidate_edge:
  edge_id: edge.jiomart.v9.00609.uses_column
  canonical_edge_type: USES_COLUMN
  source_card_id: metric_impl.jiomart.intra_state_vs_inter_state_gst
  target_card_id: column.zs_observe.jiomart_oms.tax_igst_rate
  edge_class: canonical
  canonical_cognee_edge: true
  source_type: metric_implementation
  target_type: column
```


```yaml
candidate_edge:
  edge_id: edge.jiomart.v9.00610.uses_column
  canonical_edge_type: USES_COLUMN
  source_card_id: metric_impl.jiomart.intra_state_vs_inter_state_gst
  target_card_id: column.zs_observe.jiomart_oms.tax_igst_amount
  edge_class: canonical
  canonical_cognee_edge: true
  source_type: metric_implementation
  target_type: column
```


```yaml
candidate_edge:
  edge_id: edge.jiomart.v9.00611.uses_column
  canonical_edge_type: USES_COLUMN
  source_card_id: metric_impl.jiomart.intra_state_vs_inter_state_gst
  target_card_id: column.zs_observe.jiomart_oms.tax_cgst_amount
  edge_class: canonical
  canonical_cognee_edge: true
  source_type: metric_implementation
  target_type: column
```


```yaml
candidate_edge:
  edge_id: edge.jiomart.v9.00612.uses_column
  canonical_edge_type: USES_COLUMN
  source_card_id: metric_impl.jiomart.intra_state_vs_inter_state_gst
  target_card_id: column.zs_observe.jiomart_oms.tax_sgst_amount
  edge_class: canonical
  canonical_cognee_edge: true
  source_type: metric_implementation
  target_type: column
```


```yaml
candidate_edge:
  edge_id: edge.jiomart.v9.00613.belongs_to_domain
  canonical_edge_type: BELONGS_TO_DOMAIN
  source_card_id: metric.jiomart.oms_sku_performance
  target_card_id: domain.jiomart.product
  edge_class: canonical
  canonical_cognee_edge: true
  source_type: metric
  target_type: domain
```


```yaml
candidate_edge:
  edge_id: edge.jiomart.v9.00614.applies_to_platform_context
  canonical_edge_type: APPLIES_TO_PLATFORM_CONTEXT
  source_card_id: metric.jiomart.oms_sku_performance
  target_card_id: platform_context.jiomart.in
  edge_class: canonical
  canonical_cognee_edge: true
  source_type: metric
  target_type: platform_context
```


```yaml
candidate_edge:
  edge_id: edge.jiomart.v9.00615.implements_metric
  canonical_edge_type: IMPLEMENTS_METRIC
  source_card_id: metric_impl.jiomart.oms_sku_level_performance
  target_card_id: metric.jiomart.oms_sku_performance
  edge_class: canonical
  canonical_cognee_edge: true
  source_type: metric_implementation
  target_type: metric
```


```yaml
candidate_edge:
  edge_id: edge.jiomart.v9.00616.has_implementation
  canonical_edge_type: HAS_IMPLEMENTATION
  source_card_id: metric.jiomart.oms_sku_performance
  target_card_id: metric_impl.jiomart.oms_sku_level_performance
  edge_class: canonical
  canonical_cognee_edge: true
  source_type: metric
  target_type: metric_implementation
```


```yaml
candidate_edge:
  edge_id: edge.jiomart.v9.00617.uses_table
  canonical_edge_type: USES_TABLE
  source_card_id: metric_impl.jiomart.oms_sku_level_performance
  target_card_id: table.zs_observe.jiomart_oms
  edge_class: canonical
  canonical_cognee_edge: true
  source_type: metric_implementation
  target_type: table
```


```yaml
candidate_edge:
  edge_id: edge.jiomart.v9.00618.uses_column
  canonical_edge_type: USES_COLUMN
  source_card_id: metric_impl.jiomart.oms_sku_level_performance
  target_card_id: column.zs_observe.jiomart_oms.sku_id
  edge_class: canonical
  canonical_cognee_edge: true
  source_type: metric_implementation
  target_type: column
```


```yaml
candidate_edge:
  edge_id: edge.jiomart.v9.00619.uses_column
  canonical_edge_type: USES_COLUMN
  source_card_id: metric_impl.jiomart.oms_sku_level_performance
  target_card_id: column.zs_observe.jiomart_oms.mp_sin
  edge_class: canonical
  canonical_cognee_edge: true
  source_type: metric_implementation
  target_type: column
```


```yaml
candidate_edge:
  edge_id: edge.jiomart.v9.00620.uses_column
  canonical_edge_type: USES_COLUMN
  source_card_id: metric_impl.jiomart.oms_sku_level_performance
  target_card_id: column.zs_observe.jiomart_oms.charged_amount
  edge_class: canonical
  canonical_cognee_edge: true
  source_type: metric_implementation
  target_type: column
```


```yaml
candidate_edge:
  edge_id: edge.jiomart.v9.00621.belongs_to_domain
  canonical_edge_type: BELONGS_TO_DOMAIN
  source_card_id: metric.jiomart.tcs_deducted
  target_card_id: domain.jiomart.tax
  edge_class: canonical
  canonical_cognee_edge: true
  source_type: metric
  target_type: domain
```


```yaml
candidate_edge:
  edge_id: edge.jiomart.v9.00622.applies_to_platform_context
  canonical_edge_type: APPLIES_TO_PLATFORM_CONTEXT
  source_card_id: metric.jiomart.tcs_deducted
  target_card_id: platform_context.jiomart.in
  edge_class: canonical
  canonical_cognee_edge: true
  source_type: metric
  target_type: platform_context
```


```yaml
candidate_edge:
  edge_id: edge.jiomart.v9.00623.implements_metric
  canonical_edge_type: IMPLEMENTS_METRIC
  source_card_id: metric_impl.jiomart.tcs_reconciliation
  target_card_id: metric.jiomart.tcs_deducted
  edge_class: canonical
  canonical_cognee_edge: true
  source_type: metric_implementation
  target_type: metric
```


```yaml
candidate_edge:
  edge_id: edge.jiomart.v9.00624.has_implementation
  canonical_edge_type: HAS_IMPLEMENTATION
  source_card_id: metric.jiomart.tcs_deducted
  target_card_id: metric_impl.jiomart.tcs_reconciliation
  edge_class: canonical
  canonical_cognee_edge: true
  source_type: metric
  target_type: metric_implementation
```


```yaml
candidate_edge:
  edge_id: edge.jiomart.v9.00625.uses_table
  canonical_edge_type: USES_TABLE
  source_card_id: metric_impl.jiomart.tcs_reconciliation
  target_card_id: table.zs_observe.jiomart_oms
  edge_class: canonical
  canonical_cognee_edge: true
  source_type: metric_implementation
  target_type: table
```


```yaml
candidate_edge:
  edge_id: edge.jiomart.v9.00626.uses_table
  canonical_edge_type: USES_TABLE
  source_card_id: metric_impl.jiomart.tcs_reconciliation
  target_card_id: table.zs_observe.jiomart_settlement
  edge_class: canonical
  canonical_cognee_edge: true
  source_type: metric_implementation
  target_type: table
```


```yaml
candidate_edge:
  edge_id: edge.jiomart.v9.00627.uses_column
  canonical_edge_type: USES_COLUMN
  source_card_id: metric_impl.jiomart.tcs_reconciliation
  target_card_id: column.zs_observe.jiomart_oms.total_tcs_amount
  edge_class: canonical
  canonical_cognee_edge: true
  source_type: metric_implementation
  target_type: column
```


```yaml
candidate_edge:
  edge_id: edge.jiomart.v9.00628.uses_column
  canonical_edge_type: USES_COLUMN
  source_card_id: metric_impl.jiomart.tcs_reconciliation
  target_card_id: column.zs_observe.jiomart_settlement.settled_amount
  edge_class: canonical
  canonical_cognee_edge: true
  source_type: metric_implementation
  target_type: column
```


```yaml
candidate_edge:
  edge_id: edge.jiomart.v9.00629.uses_column
  canonical_edge_type: USES_COLUMN
  source_card_id: metric_impl.jiomart.tcs_reconciliation
  target_card_id: column.zs_observe.jiomart_settlement.accountable_type
  edge_class: canonical
  canonical_cognee_edge: true
  source_type: metric_implementation
  target_type: column
```


```yaml
candidate_edge:
  edge_id: edge.jiomart.v9.00630.uses_column
  canonical_edge_type: USES_COLUMN
  source_card_id: metric_impl.jiomart.tcs_reconciliation
  target_card_id: column.zs_observe.jiomart_oms.transaction_type
  edge_class: canonical
  canonical_cognee_edge: true
  source_type: metric_implementation
  target_type: column
```


```yaml
candidate_edge:
  edge_id: edge.jiomart.v9.00631.uses_column
  canonical_edge_type: USES_COLUMN
  source_card_id: metric_impl.jiomart.tcs_reconciliation
  target_card_id: column.zs_observe.jiomart_settlement.transaction_type
  edge_class: canonical
  canonical_cognee_edge: true
  source_type: metric_implementation
  target_type: column
```


```yaml
candidate_edge:
  edge_id: edge.jiomart.v9.00632.belongs_to_domain
  canonical_edge_type: BELONGS_TO_DOMAIN
  source_card_id: metric.jiomart.tds_deducted
  target_card_id: domain.jiomart.tax
  edge_class: canonical
  canonical_cognee_edge: true
  source_type: metric
  target_type: domain
```


```yaml
candidate_edge:
  edge_id: edge.jiomart.v9.00633.applies_to_platform_context
  canonical_edge_type: APPLIES_TO_PLATFORM_CONTEXT
  source_card_id: metric.jiomart.tds_deducted
  target_card_id: platform_context.jiomart.in
  edge_class: canonical
  canonical_cognee_edge: true
  source_type: metric
  target_type: platform_context
```


```yaml
candidate_edge:
  edge_id: edge.jiomart.v9.00634.applies_to_platform_context
  canonical_edge_type: APPLIES_TO_PLATFORM_CONTEXT
  source_card_id: formula.jiomart.structured_settlement_net
  target_card_id: platform_context.jiomart.in
  edge_class: canonical
  canonical_cognee_edge: true
  source_type: formula_template
  target_type: platform_context
```


```yaml
candidate_edge:
  edge_id: edge.jiomart.v9.00635.applies_to_platform_context
  canonical_edge_type: APPLIES_TO_PLATFORM_CONTEXT
  source_card_id: formula.jiomart.forward_gmv
  target_card_id: platform_context.jiomart.in
  edge_class: canonical
  canonical_cognee_edge: true
  source_type: formula_template
  target_type: platform_context
```


```yaml
candidate_edge:
  edge_id: edge.jiomart.v9.00636.applies_to_platform_context
  canonical_edge_type: APPLIES_TO_PLATFORM_CONTEXT
  source_card_id: formula.jiomart.return_rate
  target_card_id: platform_context.jiomart.in
  edge_class: canonical
  canonical_cognee_edge: true
  source_type: formula_template
  target_type: platform_context
```


```yaml
candidate_edge:
  edge_id: edge.jiomart.v9.00637.applies_to_platform_context
  canonical_edge_type: APPLIES_TO_PLATFORM_CONTEXT
  source_card_id: formula.jiomart.tcs_variance
  target_card_id: platform_context.jiomart.in
  edge_class: canonical
  canonical_cognee_edge: true
  source_type: formula_template
  target_type: platform_context
```


```yaml
candidate_edge:
  edge_id: edge.jiomart.v9.00638.applies_to_platform_context
  canonical_edge_type: APPLIES_TO_PLATFORM_CONTEXT
  source_card_id: formula.jiomart.return_cycle_days
  target_card_id: platform_context.jiomart.in
  edge_class: canonical
  canonical_cognee_edge: true
  source_type: formula_template
  target_type: platform_context
```


```yaml
candidate_edge:
  edge_id: edge.jiomart.v9.00639.has_business_process
  canonical_edge_type: HAS_BUSINESS_PROCESS
  source_card_id: domain.jiomart.orders
  target_card_id: business_process.jiomart.forward_order_flow
  edge_class: canonical
  canonical_cognee_edge: true
  source_type: domain
  target_type: business_process
```


```yaml
candidate_edge:
  edge_id: edge.jiomart.v9.00640.belongs_to_domain
  canonical_edge_type: BELONGS_TO_DOMAIN
  source_card_id: business_process.jiomart.forward_order_flow
  target_card_id: domain.jiomart.orders
  edge_class: canonical
  canonical_cognee_edge: true
  source_type: business_process
  target_type: domain
```


```yaml
candidate_edge:
  edge_id: edge.jiomart.v9.00641.uses_table
  canonical_edge_type: USES_TABLE
  source_card_id: business_process.jiomart.forward_order_flow
  target_card_id: table.zs_observe.jiomart_oms
  edge_class: canonical
  canonical_cognee_edge: true
  source_type: business_process
  target_type: table
```


```yaml
candidate_edge:
  edge_id: edge.jiomart.v9.00642.uses_table
  canonical_edge_type: USES_TABLE
  source_card_id: business_process.jiomart.forward_order_flow
  target_card_id: table.zs_observe.jiomart_settlement
  edge_class: canonical
  canonical_cognee_edge: true
  source_type: business_process
  target_type: table
```


```yaml
candidate_edge:
  edge_id: edge.jiomart.v9.00643.has_workflow_step
  canonical_edge_type: HAS_WORKFLOW_STEP
  source_card_id: business_process.jiomart.forward_order_flow
  target_card_id: workflow_step.jiomart.forward_order_flow.01
  edge_class: canonical
  canonical_cognee_edge: true
  source_type: business_process
  target_type: workflow_step
```


```yaml
candidate_edge:
  edge_id: edge.jiomart.v9.00644.belongs_to_process
  canonical_edge_type: BELONGS_TO_PROCESS
  source_card_id: workflow_step.jiomart.forward_order_flow.01
  target_card_id: business_process.jiomart.forward_order_flow
  edge_class: canonical
  canonical_cognee_edge: true
  source_type: workflow_step
  target_type: business_process
```


```yaml
candidate_edge:
  edge_id: edge.jiomart.v9.00645.uses_table
  canonical_edge_type: USES_TABLE
  source_card_id: workflow_step.jiomart.forward_order_flow.01
  target_card_id: table.zs_observe.jiomart_oms
  edge_class: canonical
  canonical_cognee_edge: true
  source_type: workflow_step
  target_type: table
```


```yaml
candidate_edge:
  edge_id: edge.jiomart.v9.00646.has_workflow_step
  canonical_edge_type: HAS_WORKFLOW_STEP
  source_card_id: business_process.jiomart.forward_order_flow
  target_card_id: workflow_step.jiomart.forward_order_flow.02
  edge_class: canonical
  canonical_cognee_edge: true
  source_type: business_process
  target_type: workflow_step
```


```yaml
candidate_edge:
  edge_id: edge.jiomart.v9.00647.belongs_to_process
  canonical_edge_type: BELONGS_TO_PROCESS
  source_card_id: workflow_step.jiomart.forward_order_flow.02
  target_card_id: business_process.jiomart.forward_order_flow
  edge_class: canonical
  canonical_cognee_edge: true
  source_type: workflow_step
  target_type: business_process
```


```yaml
candidate_edge:
  edge_id: edge.jiomart.v9.00648.uses_table
  canonical_edge_type: USES_TABLE
  source_card_id: workflow_step.jiomart.forward_order_flow.02
  target_card_id: table.zs_observe.jiomart_oms
  edge_class: canonical
  canonical_cognee_edge: true
  source_type: workflow_step
  target_type: table
```


```yaml
candidate_edge:
  edge_id: edge.jiomart.v9.00649.has_workflow_step
  canonical_edge_type: HAS_WORKFLOW_STEP
  source_card_id: business_process.jiomart.forward_order_flow
  target_card_id: workflow_step.jiomart.forward_order_flow.03
  edge_class: canonical
  canonical_cognee_edge: true
  source_type: business_process
  target_type: workflow_step
```


```yaml
candidate_edge:
  edge_id: edge.jiomart.v9.00650.belongs_to_process
  canonical_edge_type: BELONGS_TO_PROCESS
  source_card_id: workflow_step.jiomart.forward_order_flow.03
  target_card_id: business_process.jiomart.forward_order_flow
  edge_class: canonical
  canonical_cognee_edge: true
  source_type: workflow_step
  target_type: business_process
```


```yaml
candidate_edge:
  edge_id: edge.jiomart.v9.00651.uses_table
  canonical_edge_type: USES_TABLE
  source_card_id: workflow_step.jiomart.forward_order_flow.03
  target_card_id: table.zs_observe.jiomart_oms
  edge_class: canonical
  canonical_cognee_edge: true
  source_type: workflow_step
  target_type: table
```


```yaml
candidate_edge:
  edge_id: edge.jiomart.v9.00652.has_workflow_step
  canonical_edge_type: HAS_WORKFLOW_STEP
  source_card_id: business_process.jiomart.forward_order_flow
  target_card_id: workflow_step.jiomart.forward_order_flow.04
  edge_class: canonical
  canonical_cognee_edge: true
  source_type: business_process
  target_type: workflow_step
```


```yaml
candidate_edge:
  edge_id: edge.jiomart.v9.00653.belongs_to_process
  canonical_edge_type: BELONGS_TO_PROCESS
  source_card_id: workflow_step.jiomart.forward_order_flow.04
  target_card_id: business_process.jiomart.forward_order_flow
  edge_class: canonical
  canonical_cognee_edge: true
  source_type: workflow_step
  target_type: business_process
```


```yaml
candidate_edge:
  edge_id: edge.jiomart.v9.00654.uses_table
  canonical_edge_type: USES_TABLE
  source_card_id: workflow_step.jiomart.forward_order_flow.04
  target_card_id: table.zs_observe.jiomart_oms
  edge_class: canonical
  canonical_cognee_edge: true
  source_type: workflow_step
  target_type: table
```


```yaml
candidate_edge:
  edge_id: edge.jiomart.v9.00655.has_workflow_step
  canonical_edge_type: HAS_WORKFLOW_STEP
  source_card_id: business_process.jiomart.forward_order_flow
  target_card_id: workflow_step.jiomart.forward_order_flow.05
  edge_class: canonical
  canonical_cognee_edge: true
  source_type: business_process
  target_type: workflow_step
```


```yaml
candidate_edge:
  edge_id: edge.jiomart.v9.00656.belongs_to_process
  canonical_edge_type: BELONGS_TO_PROCESS
  source_card_id: workflow_step.jiomart.forward_order_flow.05
  target_card_id: business_process.jiomart.forward_order_flow
  edge_class: canonical
  canonical_cognee_edge: true
  source_type: workflow_step
  target_type: business_process
```


```yaml
candidate_edge:
  edge_id: edge.jiomart.v9.00657.uses_table
  canonical_edge_type: USES_TABLE
  source_card_id: workflow_step.jiomart.forward_order_flow.05
  target_card_id: table.zs_observe.jiomart_settlement
  edge_class: canonical
  canonical_cognee_edge: true
  source_type: workflow_step
  target_type: table
```


```yaml
candidate_edge:
  edge_id: edge.jiomart.v9.00658.has_business_process
  canonical_edge_type: HAS_BUSINESS_PROCESS
  source_card_id: domain.jiomart.returns
  target_card_id: business_process.jiomart.rto_flow
  edge_class: canonical
  canonical_cognee_edge: true
  source_type: domain
  target_type: business_process
```


```yaml
candidate_edge:
  edge_id: edge.jiomart.v9.00659.belongs_to_domain
  canonical_edge_type: BELONGS_TO_DOMAIN
  source_card_id: business_process.jiomart.rto_flow
  target_card_id: domain.jiomart.returns
  edge_class: canonical
  canonical_cognee_edge: true
  source_type: business_process
  target_type: domain
```


```yaml
candidate_edge:
  edge_id: edge.jiomart.v9.00660.uses_table
  canonical_edge_type: USES_TABLE
  source_card_id: business_process.jiomart.rto_flow
  target_card_id: table.zs_observe.jiomart_oms
  edge_class: canonical
  canonical_cognee_edge: true
  source_type: business_process
  target_type: table
```


```yaml
candidate_edge:
  edge_id: edge.jiomart.v9.00661.uses_table
  canonical_edge_type: USES_TABLE
  source_card_id: business_process.jiomart.rto_flow
  target_card_id: table.zs_observe.jiomart_returns
  edge_class: canonical
  canonical_cognee_edge: true
  source_type: business_process
  target_type: table
```


```yaml
candidate_edge:
  edge_id: edge.jiomart.v9.00662.uses_table
  canonical_edge_type: USES_TABLE
  source_card_id: business_process.jiomart.rto_flow
  target_card_id: table.zs_observe.jiomart_settlement
  edge_class: canonical
  canonical_cognee_edge: true
  source_type: business_process
  target_type: table
```


```yaml
candidate_edge:
  edge_id: edge.jiomart.v9.00663.has_workflow_step
  canonical_edge_type: HAS_WORKFLOW_STEP
  source_card_id: business_process.jiomart.rto_flow
  target_card_id: workflow_step.jiomart.rto_flow.01
  edge_class: canonical
  canonical_cognee_edge: true
  source_type: business_process
  target_type: workflow_step
```


```yaml
candidate_edge:
  edge_id: edge.jiomart.v9.00664.belongs_to_process
  canonical_edge_type: BELONGS_TO_PROCESS
  source_card_id: workflow_step.jiomart.rto_flow.01
  target_card_id: business_process.jiomart.rto_flow
  edge_class: canonical
  canonical_cognee_edge: true
  source_type: workflow_step
  target_type: business_process
```


```yaml
candidate_edge:
  edge_id: edge.jiomart.v9.00665.uses_table
  canonical_edge_type: USES_TABLE
  source_card_id: workflow_step.jiomart.rto_flow.01
  target_card_id: table.zs_observe.jiomart_oms
  edge_class: canonical
  canonical_cognee_edge: true
  source_type: workflow_step
  target_type: table
```


```yaml
candidate_edge:
  edge_id: edge.jiomart.v9.00666.uses_table
  canonical_edge_type: USES_TABLE
  source_card_id: workflow_step.jiomart.rto_flow.01
  target_card_id: table.zs_observe.jiomart_returns
  edge_class: canonical
  canonical_cognee_edge: true
  source_type: workflow_step
  target_type: table
```


```yaml
candidate_edge:
  edge_id: edge.jiomart.v9.00667.has_workflow_step
  canonical_edge_type: HAS_WORKFLOW_STEP
  source_card_id: business_process.jiomart.rto_flow
  target_card_id: workflow_step.jiomart.rto_flow.02
  edge_class: canonical
  canonical_cognee_edge: true
  source_type: business_process
  target_type: workflow_step
```


```yaml
candidate_edge:
  edge_id: edge.jiomart.v9.00668.belongs_to_process
  canonical_edge_type: BELONGS_TO_PROCESS
  source_card_id: workflow_step.jiomart.rto_flow.02
  target_card_id: business_process.jiomart.rto_flow
  edge_class: canonical
  canonical_cognee_edge: true
  source_type: workflow_step
  target_type: business_process
```


```yaml
candidate_edge:
  edge_id: edge.jiomart.v9.00669.uses_table
  canonical_edge_type: USES_TABLE
  source_card_id: workflow_step.jiomart.rto_flow.02
  target_card_id: table.zs_observe.jiomart_returns
  edge_class: canonical
  canonical_cognee_edge: true
  source_type: workflow_step
  target_type: table
```


```yaml
candidate_edge:
  edge_id: edge.jiomart.v9.00670.has_workflow_step
  canonical_edge_type: HAS_WORKFLOW_STEP
  source_card_id: business_process.jiomart.rto_flow
  target_card_id: workflow_step.jiomart.rto_flow.03
  edge_class: canonical
  canonical_cognee_edge: true
  source_type: business_process
  target_type: workflow_step
```


```yaml
candidate_edge:
  edge_id: edge.jiomart.v9.00671.belongs_to_process
  canonical_edge_type: BELONGS_TO_PROCESS
  source_card_id: workflow_step.jiomart.rto_flow.03
  target_card_id: business_process.jiomart.rto_flow
  edge_class: canonical
  canonical_cognee_edge: true
  source_type: workflow_step
  target_type: business_process
```


```yaml
candidate_edge:
  edge_id: edge.jiomart.v9.00672.uses_table
  canonical_edge_type: USES_TABLE
  source_card_id: workflow_step.jiomart.rto_flow.03
  target_card_id: table.zs_observe.jiomart_settlement
  edge_class: canonical
  canonical_cognee_edge: true
  source_type: workflow_step
  target_type: table
```


```yaml
candidate_edge:
  edge_id: edge.jiomart.v9.00673.has_workflow_step
  canonical_edge_type: HAS_WORKFLOW_STEP
  source_card_id: business_process.jiomart.rto_flow
  target_card_id: workflow_step.jiomart.rto_flow.04
  edge_class: canonical
  canonical_cognee_edge: true
  source_type: business_process
  target_type: workflow_step
```


```yaml
candidate_edge:
  edge_id: edge.jiomart.v9.00674.belongs_to_process
  canonical_edge_type: BELONGS_TO_PROCESS
  source_card_id: workflow_step.jiomart.rto_flow.04
  target_card_id: business_process.jiomart.rto_flow
  edge_class: canonical
  canonical_cognee_edge: true
  source_type: workflow_step
  target_type: business_process
```


```yaml
candidate_edge:
  edge_id: edge.jiomart.v9.00675.uses_table
  canonical_edge_type: USES_TABLE
  source_card_id: workflow_step.jiomart.rto_flow.04
  target_card_id: table.zs_observe.jiomart_settlement
  edge_class: canonical
  canonical_cognee_edge: true
  source_type: workflow_step
  target_type: table
```


```yaml
candidate_edge:
  edge_id: edge.jiomart.v9.00676.has_business_process
  canonical_edge_type: HAS_BUSINESS_PROCESS
  source_card_id: domain.jiomart.returns
  target_card_id: business_process.jiomart.doorstep_return_flow
  edge_class: canonical
  canonical_cognee_edge: true
  source_type: domain
  target_type: business_process
```


```yaml
candidate_edge:
  edge_id: edge.jiomart.v9.00677.belongs_to_domain
  canonical_edge_type: BELONGS_TO_DOMAIN
  source_card_id: business_process.jiomart.doorstep_return_flow
  target_card_id: domain.jiomart.returns
  edge_class: canonical
  canonical_cognee_edge: true
  source_type: business_process
  target_type: domain
```


```yaml
candidate_edge:
  edge_id: edge.jiomart.v9.00678.uses_table
  canonical_edge_type: USES_TABLE
  source_card_id: business_process.jiomart.doorstep_return_flow
  target_card_id: table.zs_observe.jiomart_returns
  edge_class: canonical
  canonical_cognee_edge: true
  source_type: business_process
  target_type: table
```


```yaml
candidate_edge:
  edge_id: edge.jiomart.v9.00679.uses_table
  canonical_edge_type: USES_TABLE
  source_card_id: business_process.jiomart.doorstep_return_flow
  target_card_id: table.zs_observe.jiomart_settlement
  edge_class: canonical
  canonical_cognee_edge: true
  source_type: business_process
  target_type: table
```


```yaml
candidate_edge:
  edge_id: edge.jiomart.v9.00680.has_workflow_step
  canonical_edge_type: HAS_WORKFLOW_STEP
  source_card_id: business_process.jiomart.doorstep_return_flow
  target_card_id: workflow_step.jiomart.doorstep_return_flow.01
  edge_class: canonical
  canonical_cognee_edge: true
  source_type: business_process
  target_type: workflow_step
```


```yaml
candidate_edge:
  edge_id: edge.jiomart.v9.00681.belongs_to_process
  canonical_edge_type: BELONGS_TO_PROCESS
  source_card_id: workflow_step.jiomart.doorstep_return_flow.01
  target_card_id: business_process.jiomart.doorstep_return_flow
  edge_class: canonical
  canonical_cognee_edge: true
  source_type: workflow_step
  target_type: business_process
```


```yaml
candidate_edge:
  edge_id: edge.jiomart.v9.00682.uses_table
  canonical_edge_type: USES_TABLE
  source_card_id: workflow_step.jiomart.doorstep_return_flow.01
  target_card_id: table.zs_observe.jiomart_returns
  edge_class: canonical
  canonical_cognee_edge: true
  source_type: workflow_step
  target_type: table
```


```yaml
candidate_edge:
  edge_id: edge.jiomart.v9.00683.has_workflow_step
  canonical_edge_type: HAS_WORKFLOW_STEP
  source_card_id: business_process.jiomart.doorstep_return_flow
  target_card_id: workflow_step.jiomart.doorstep_return_flow.02
  edge_class: canonical
  canonical_cognee_edge: true
  source_type: business_process
  target_type: workflow_step
```


```yaml
candidate_edge:
  edge_id: edge.jiomart.v9.00684.belongs_to_process
  canonical_edge_type: BELONGS_TO_PROCESS
  source_card_id: workflow_step.jiomart.doorstep_return_flow.02
  target_card_id: business_process.jiomart.doorstep_return_flow
  edge_class: canonical
  canonical_cognee_edge: true
  source_type: workflow_step
  target_type: business_process
```


```yaml
candidate_edge:
  edge_id: edge.jiomart.v9.00685.uses_table
  canonical_edge_type: USES_TABLE
  source_card_id: workflow_step.jiomart.doorstep_return_flow.02
  target_card_id: table.zs_observe.jiomart_returns
  edge_class: canonical
  canonical_cognee_edge: true
  source_type: workflow_step
  target_type: table
```


```yaml
candidate_edge:
  edge_id: edge.jiomart.v9.00686.has_workflow_step
  canonical_edge_type: HAS_WORKFLOW_STEP
  source_card_id: business_process.jiomart.doorstep_return_flow
  target_card_id: workflow_step.jiomart.doorstep_return_flow.03
  edge_class: canonical
  canonical_cognee_edge: true
  source_type: business_process
  target_type: workflow_step
```


```yaml
candidate_edge:
  edge_id: edge.jiomart.v9.00687.belongs_to_process
  canonical_edge_type: BELONGS_TO_PROCESS
  source_card_id: workflow_step.jiomart.doorstep_return_flow.03
  target_card_id: business_process.jiomart.doorstep_return_flow
  edge_class: canonical
  canonical_cognee_edge: true
  source_type: workflow_step
  target_type: business_process
```


```yaml
candidate_edge:
  edge_id: edge.jiomart.v9.00688.uses_table
  canonical_edge_type: USES_TABLE
  source_card_id: workflow_step.jiomart.doorstep_return_flow.03
  target_card_id: table.zs_observe.jiomart_returns
  edge_class: canonical
  canonical_cognee_edge: true
  source_type: workflow_step
  target_type: table
```


```yaml
candidate_edge:
  edge_id: edge.jiomart.v9.00689.uses_table
  canonical_edge_type: USES_TABLE
  source_card_id: workflow_step.jiomart.doorstep_return_flow.03
  target_card_id: table.zs_observe.jiomart_settlement
  edge_class: canonical
  canonical_cognee_edge: true
  source_type: workflow_step
  target_type: table
```


```yaml
candidate_edge:
  edge_id: edge.jiomart.v9.00690.has_business_process
  canonical_edge_type: HAS_BUSINESS_PROCESS
  source_card_id: domain.jiomart.returns
  target_card_id: business_process.jiomart.pre_shipment_cancellation_flow
  edge_class: canonical
  canonical_cognee_edge: true
  source_type: domain
  target_type: business_process
```


```yaml
candidate_edge:
  edge_id: edge.jiomart.v9.00691.belongs_to_domain
  canonical_edge_type: BELONGS_TO_DOMAIN
  source_card_id: business_process.jiomart.pre_shipment_cancellation_flow
  target_card_id: domain.jiomart.returns
  edge_class: canonical
  canonical_cognee_edge: true
  source_type: business_process
  target_type: domain
```


```yaml
candidate_edge:
  edge_id: edge.jiomart.v9.00692.uses_table
  canonical_edge_type: USES_TABLE
  source_card_id: business_process.jiomart.pre_shipment_cancellation_flow
  target_card_id: table.zs_observe.jiomart_returns
  edge_class: canonical
  canonical_cognee_edge: true
  source_type: business_process
  target_type: table
```


```yaml
candidate_edge:
  edge_id: edge.jiomart.v9.00693.has_workflow_step
  canonical_edge_type: HAS_WORKFLOW_STEP
  source_card_id: business_process.jiomart.pre_shipment_cancellation_flow
  target_card_id: workflow_step.jiomart.pre_shipment_cancellation_flow.01
  edge_class: canonical
  canonical_cognee_edge: true
  source_type: business_process
  target_type: workflow_step
```


```yaml
candidate_edge:
  edge_id: edge.jiomart.v9.00694.belongs_to_process
  canonical_edge_type: BELONGS_TO_PROCESS
  source_card_id: workflow_step.jiomart.pre_shipment_cancellation_flow.01
  target_card_id: business_process.jiomart.pre_shipment_cancellation_flow
  edge_class: canonical
  canonical_cognee_edge: true
  source_type: workflow_step
  target_type: business_process
```


```yaml
candidate_edge:
  edge_id: edge.jiomart.v9.00695.uses_table
  canonical_edge_type: USES_TABLE
  source_card_id: workflow_step.jiomart.pre_shipment_cancellation_flow.01
  target_card_id: table.zs_observe.jiomart_returns
  edge_class: canonical
  canonical_cognee_edge: true
  source_type: workflow_step
  target_type: table
```


```yaml
candidate_edge:
  edge_id: edge.jiomart.v9.00696.has_workflow_step
  canonical_edge_type: HAS_WORKFLOW_STEP
  source_card_id: business_process.jiomart.pre_shipment_cancellation_flow
  target_card_id: workflow_step.jiomart.pre_shipment_cancellation_flow.02
  edge_class: canonical
  canonical_cognee_edge: true
  source_type: business_process
  target_type: workflow_step
```


```yaml
candidate_edge:
  edge_id: edge.jiomart.v9.00697.belongs_to_process
  canonical_edge_type: BELONGS_TO_PROCESS
  source_card_id: workflow_step.jiomart.pre_shipment_cancellation_flow.02
  target_card_id: business_process.jiomart.pre_shipment_cancellation_flow
  edge_class: canonical
  canonical_cognee_edge: true
  source_type: workflow_step
  target_type: business_process
```


```yaml
candidate_edge:
  edge_id: edge.jiomart.v9.00698.uses_table
  canonical_edge_type: USES_TABLE
  source_card_id: workflow_step.jiomart.pre_shipment_cancellation_flow.02
  target_card_id: table.zs_observe.jiomart_returns
  edge_class: canonical
  canonical_cognee_edge: true
  source_type: workflow_step
  target_type: table
```


```yaml
candidate_edge:
  edge_id: edge.jiomart.v9.00699.has_workflow_step
  canonical_edge_type: HAS_WORKFLOW_STEP
  source_card_id: business_process.jiomart.pre_shipment_cancellation_flow
  target_card_id: workflow_step.jiomart.pre_shipment_cancellation_flow.03
  edge_class: canonical
  canonical_cognee_edge: true
  source_type: business_process
  target_type: workflow_step
```


```yaml
candidate_edge:
  edge_id: edge.jiomart.v9.00700.belongs_to_process
  canonical_edge_type: BELONGS_TO_PROCESS
  source_card_id: workflow_step.jiomart.pre_shipment_cancellation_flow.03
  target_card_id: business_process.jiomart.pre_shipment_cancellation_flow
  edge_class: canonical
  canonical_cognee_edge: true
  source_type: workflow_step
  target_type: business_process
```


```yaml
candidate_edge:
  edge_id: edge.jiomart.v9.00701.uses_table
  canonical_edge_type: USES_TABLE
  source_card_id: workflow_step.jiomart.pre_shipment_cancellation_flow.03
  target_card_id: table.zs_observe.jiomart_returns
  edge_class: canonical
  canonical_cognee_edge: true
  source_type: workflow_step
  target_type: table
```


```yaml
candidate_edge:
  edge_id: edge.jiomart.v9.00702.has_business_process
  canonical_edge_type: HAS_BUSINESS_PROCESS
  source_card_id: domain.jiomart.settlement
  target_card_id: business_process.jiomart.settlement_event_model
  edge_class: canonical
  canonical_cognee_edge: true
  source_type: domain
  target_type: business_process
```


```yaml
candidate_edge:
  edge_id: edge.jiomart.v9.00703.belongs_to_domain
  canonical_edge_type: BELONGS_TO_DOMAIN
  source_card_id: business_process.jiomart.settlement_event_model
  target_card_id: domain.jiomart.settlement
  edge_class: canonical
  canonical_cognee_edge: true
  source_type: business_process
  target_type: domain
```


```yaml
candidate_edge:
  edge_id: edge.jiomart.v9.00704.uses_table
  canonical_edge_type: USES_TABLE
  source_card_id: business_process.jiomart.settlement_event_model
  target_card_id: table.zs_observe.jiomart_settlement
  edge_class: canonical
  canonical_cognee_edge: true
  source_type: business_process
  target_type: table
```


```yaml
candidate_edge:
  edge_id: edge.jiomart.v9.00705.has_workflow_step
  canonical_edge_type: HAS_WORKFLOW_STEP
  source_card_id: business_process.jiomart.settlement_event_model
  target_card_id: workflow_step.jiomart.settlement_event_model.01
  edge_class: canonical
  canonical_cognee_edge: true
  source_type: business_process
  target_type: workflow_step
```


```yaml
candidate_edge:
  edge_id: edge.jiomart.v9.00706.belongs_to_process
  canonical_edge_type: BELONGS_TO_PROCESS
  source_card_id: workflow_step.jiomart.settlement_event_model.01
  target_card_id: business_process.jiomart.settlement_event_model
  edge_class: canonical
  canonical_cognee_edge: true
  source_type: workflow_step
  target_type: business_process
```


```yaml
candidate_edge:
  edge_id: edge.jiomart.v9.00707.uses_table
  canonical_edge_type: USES_TABLE
  source_card_id: workflow_step.jiomart.settlement_event_model.01
  target_card_id: table.zs_observe.jiomart_settlement
  edge_class: canonical
  canonical_cognee_edge: true
  source_type: workflow_step
  target_type: table
```


```yaml
candidate_edge:
  edge_id: edge.jiomart.v9.00708.has_workflow_step
  canonical_edge_type: HAS_WORKFLOW_STEP
  source_card_id: business_process.jiomart.settlement_event_model
  target_card_id: workflow_step.jiomart.settlement_event_model.02
  edge_class: canonical
  canonical_cognee_edge: true
  source_type: business_process
  target_type: workflow_step
```


```yaml
candidate_edge:
  edge_id: edge.jiomart.v9.00709.belongs_to_process
  canonical_edge_type: BELONGS_TO_PROCESS
  source_card_id: workflow_step.jiomart.settlement_event_model.02
  target_card_id: business_process.jiomart.settlement_event_model
  edge_class: canonical
  canonical_cognee_edge: true
  source_type: workflow_step
  target_type: business_process
```


```yaml
candidate_edge:
  edge_id: edge.jiomart.v9.00710.uses_table
  canonical_edge_type: USES_TABLE
  source_card_id: workflow_step.jiomart.settlement_event_model.02
  target_card_id: table.zs_observe.jiomart_settlement
  edge_class: canonical
  canonical_cognee_edge: true
  source_type: workflow_step
  target_type: table
```


```yaml
candidate_edge:
  edge_id: edge.jiomart.v9.00711.has_workflow_step
  canonical_edge_type: HAS_WORKFLOW_STEP
  source_card_id: business_process.jiomart.settlement_event_model
  target_card_id: workflow_step.jiomart.settlement_event_model.03
  edge_class: canonical
  canonical_cognee_edge: true
  source_type: business_process
  target_type: workflow_step
```


```yaml
candidate_edge:
  edge_id: edge.jiomart.v9.00712.belongs_to_process
  canonical_edge_type: BELONGS_TO_PROCESS
  source_card_id: workflow_step.jiomart.settlement_event_model.03
  target_card_id: business_process.jiomart.settlement_event_model
  edge_class: canonical
  canonical_cognee_edge: true
  source_type: workflow_step
  target_type: business_process
```


```yaml
candidate_edge:
  edge_id: edge.jiomart.v9.00713.uses_table
  canonical_edge_type: USES_TABLE
  source_card_id: workflow_step.jiomart.settlement_event_model.03
  target_card_id: table.zs_observe.jiomart_settlement
  edge_class: canonical
  canonical_cognee_edge: true
  source_type: workflow_step
  target_type: table
```


```yaml
candidate_edge:
  edge_id: edge.jiomart.v9.00714.applies_to_platform_context
  canonical_edge_type: APPLIES_TO_PLATFORM_CONTEXT
  source_card_id: reconciliation_unit.jiomart.order_id
  target_card_id: platform_context.jiomart.in
  edge_class: canonical
  canonical_cognee_edge: true
  source_type: reconciliation_unit
  target_type: platform_context
```


```yaml
candidate_edge:
  edge_id: edge.jiomart.v9.00715.applies_to_platform_context
  canonical_edge_type: APPLIES_TO_PLATFORM_CONTEXT
  source_card_id: reconciliation_unit.jiomart.period_or_order
  target_card_id: platform_context.jiomart.in
  edge_class: canonical
  canonical_cognee_edge: true
  source_type: reconciliation_unit
  target_type: platform_context
```


```yaml
candidate_edge:
  edge_id: edge.jiomart.v9.00716.has_reconciliation_profile
  canonical_edge_type: HAS_RECONCILIATION_PROFILE
  source_card_id: business_process.jiomart.settlement_event_model
  target_card_id: reconciliation_profile.jiomart.oms_settlement_3way
  edge_class: canonical
  canonical_cognee_edge: true
  source_type: business_process
  target_type: reconciliation_profile
```


```yaml
candidate_edge:
  edge_id: edge.jiomart.v9.00717.supports_process
  canonical_edge_type: SUPPORTS_PROCESS
  source_card_id: reconciliation_profile.jiomart.oms_settlement_3way
  target_card_id: business_process.jiomart.settlement_event_model
  edge_class: canonical
  canonical_cognee_edge: true
  source_type: reconciliation_profile
  target_type: business_process
```


```yaml
candidate_edge:
  edge_id: edge.jiomart.v9.00718.has_primary_unit
  canonical_edge_type: HAS_PRIMARY_UNIT
  source_card_id: reconciliation_profile.jiomart.oms_settlement_3way
  target_card_id: reconciliation_unit.jiomart.order_id
  edge_class: canonical
  canonical_cognee_edge: true
  source_type: reconciliation_profile
  target_type: reconciliation_unit
```


```yaml
candidate_edge:
  edge_id: edge.jiomart.v9.00719.uses_matching_logic
  canonical_edge_type: USES_MATCHING_LOGIC
  source_card_id: reconciliation_profile.jiomart.oms_settlement_3way
  target_card_id: matching_logic.jiomart.oms_settlement_3way
  edge_class: canonical
  canonical_cognee_edge: true
  source_type: reconciliation_profile
  target_type: matching_logic
```


```yaml
candidate_edge:
  edge_id: edge.jiomart.v9.00720.supports_reconciliation_profile
  canonical_edge_type: SUPPORTS_RECONCILIATION_PROFILE
  source_card_id: matching_logic.jiomart.oms_settlement_3way
  target_card_id: reconciliation_profile.jiomart.oms_settlement_3way
  edge_class: canonical
  canonical_cognee_edge: true
  source_type: matching_logic
  target_type: reconciliation_profile
```


```yaml
candidate_edge:
  edge_id: edge.jiomart.v9.00721.has_reconciliation_side
  canonical_edge_type: HAS_RECONCILIATION_SIDE
  source_card_id: reconciliation_profile.jiomart.oms_settlement_3way
  target_card_id: reconciliation_side.jiomart.oms_settlement.expected_oms
  edge_class: canonical
  canonical_cognee_edge: true
  source_type: reconciliation_profile
  target_type: reconciliation_side
```


```yaml
candidate_edge:
  edge_id: edge.jiomart.v9.00722.has_reconciliation_side
  canonical_edge_type: HAS_RECONCILIATION_SIDE
  source_card_id: reconciliation_profile.jiomart.oms_settlement_3way
  target_card_id: reconciliation_side.jiomart.oms_settlement.actual_settlement
  edge_class: canonical
  canonical_cognee_edge: true
  source_type: reconciliation_profile
  target_type: reconciliation_side
```


```yaml
candidate_edge:
  edge_id: edge.jiomart.v9.00723.has_mismatch_category
  canonical_edge_type: HAS_MISMATCH_CATEGORY
  source_card_id: reconciliation_profile.jiomart.oms_settlement_3way
  target_card_id: mismatch_category.jiomart.not_in_settlement
  edge_class: canonical
  canonical_cognee_edge: true
  source_type: reconciliation_profile
  target_type: mismatch_category
```


```yaml
candidate_edge:
  edge_id: edge.jiomart.v9.00724.has_mismatch_category
  canonical_edge_type: HAS_MISMATCH_CATEGORY
  source_card_id: reconciliation_profile.jiomart.oms_settlement_3way
  target_card_id: mismatch_category.jiomart.tcs_variance
  edge_class: canonical
  canonical_cognee_edge: true
  source_type: reconciliation_profile
  target_type: mismatch_category
```


```yaml
candidate_edge:
  edge_id: edge.jiomart.v9.00725.belongs_to_reconciliation_profile
  canonical_edge_type: BELONGS_TO_RECONCILIATION_PROFILE
  source_card_id: reconciliation_side.jiomart.oms_settlement.expected_oms
  target_card_id: reconciliation_profile.jiomart.oms_settlement_3way
  edge_class: canonical
  canonical_cognee_edge: true
  source_type: reconciliation_side
  target_type: reconciliation_profile
```


```yaml
candidate_edge:
  edge_id: edge.jiomart.v9.00726.uses_table
  canonical_edge_type: USES_TABLE
  source_card_id: reconciliation_side.jiomart.oms_settlement.expected_oms
  target_card_id: table.zs_observe.jiomart_oms
  edge_class: canonical
  canonical_cognee_edge: true
  source_type: reconciliation_side
  target_type: table
```


```yaml
candidate_edge:
  edge_id: edge.jiomart.v9.00727.uses_column
  canonical_edge_type: USES_COLUMN
  source_card_id: reconciliation_side.jiomart.oms_settlement.expected_oms
  target_card_id: column.zs_observe.jiomart_oms.order_id
  edge_class: canonical
  canonical_cognee_edge: true
  source_type: reconciliation_side
  target_type: column
```


```yaml
candidate_edge:
  edge_id: edge.jiomart.v9.00728.belongs_to_reconciliation_profile
  canonical_edge_type: BELONGS_TO_RECONCILIATION_PROFILE
  source_card_id: reconciliation_side.jiomart.oms_settlement.actual_settlement
  target_card_id: reconciliation_profile.jiomart.oms_settlement_3way
  edge_class: canonical
  canonical_cognee_edge: true
  source_type: reconciliation_side
  target_type: reconciliation_profile
```


```yaml
candidate_edge:
  edge_id: edge.jiomart.v9.00729.uses_table
  canonical_edge_type: USES_TABLE
  source_card_id: reconciliation_side.jiomart.oms_settlement.actual_settlement
  target_card_id: table.zs_observe.jiomart_settlement
  edge_class: canonical
  canonical_cognee_edge: true
  source_type: reconciliation_side
  target_type: table
```


```yaml
candidate_edge:
  edge_id: edge.jiomart.v9.00730.uses_column
  canonical_edge_type: USES_COLUMN
  source_card_id: reconciliation_side.jiomart.oms_settlement.actual_settlement
  target_card_id: column.zs_observe.jiomart_settlement.order_id
  edge_class: canonical
  canonical_cognee_edge: true
  source_type: reconciliation_side
  target_type: column
```


```yaml
candidate_edge:
  edge_id: edge.jiomart.v9.00731.applies_to_platform_context
  canonical_edge_type: APPLIES_TO_PLATFORM_CONTEXT
  source_card_id: matching_logic.jiomart.oms_settlement_3way
  target_card_id: platform_context.jiomart.in
  edge_class: canonical
  canonical_cognee_edge: true
  source_type: matching_logic
  target_type: platform_context
```


```yaml
candidate_edge:
  edge_id: edge.jiomart.v9.00732.has_reconciliation_profile
  canonical_edge_type: HAS_RECONCILIATION_PROFILE
  source_card_id: business_process.jiomart.rto_flow
  target_card_id: reconciliation_profile.jiomart.returns_oms_settlement_chain
  edge_class: canonical
  canonical_cognee_edge: true
  source_type: business_process
  target_type: reconciliation_profile
```


```yaml
candidate_edge:
  edge_id: edge.jiomart.v9.00733.supports_process
  canonical_edge_type: SUPPORTS_PROCESS
  source_card_id: reconciliation_profile.jiomart.returns_oms_settlement_chain
  target_card_id: business_process.jiomart.rto_flow
  edge_class: canonical
  canonical_cognee_edge: true
  source_type: reconciliation_profile
  target_type: business_process
```


```yaml
candidate_edge:
  edge_id: edge.jiomart.v9.00734.has_primary_unit
  canonical_edge_type: HAS_PRIMARY_UNIT
  source_card_id: reconciliation_profile.jiomart.returns_oms_settlement_chain
  target_card_id: reconciliation_unit.jiomart.order_id
  edge_class: canonical
  canonical_cognee_edge: true
  source_type: reconciliation_profile
  target_type: reconciliation_unit
```


```yaml
candidate_edge:
  edge_id: edge.jiomart.v9.00735.uses_matching_logic
  canonical_edge_type: USES_MATCHING_LOGIC
  source_card_id: reconciliation_profile.jiomart.returns_oms_settlement_chain
  target_card_id: matching_logic.jiomart.returns_chain
  edge_class: canonical
  canonical_cognee_edge: true
  source_type: reconciliation_profile
  target_type: matching_logic
```


```yaml
candidate_edge:
  edge_id: edge.jiomart.v9.00736.supports_reconciliation_profile
  canonical_edge_type: SUPPORTS_RECONCILIATION_PROFILE
  source_card_id: matching_logic.jiomart.returns_chain
  target_card_id: reconciliation_profile.jiomart.returns_oms_settlement_chain
  edge_class: canonical
  canonical_cognee_edge: true
  source_type: matching_logic
  target_type: reconciliation_profile
```


```yaml
candidate_edge:
  edge_id: edge.jiomart.v9.00737.has_reconciliation_side
  canonical_edge_type: HAS_RECONCILIATION_SIDE
  source_card_id: reconciliation_profile.jiomart.returns_oms_settlement_chain
  target_card_id: reconciliation_side.jiomart.returns_chain.expected_returns
  edge_class: canonical
  canonical_cognee_edge: true
  source_type: reconciliation_profile
  target_type: reconciliation_side
```


```yaml
candidate_edge:
  edge_id: edge.jiomart.v9.00738.has_reconciliation_side
  canonical_edge_type: HAS_RECONCILIATION_SIDE
  source_card_id: reconciliation_profile.jiomart.returns_oms_settlement_chain
  target_card_id: reconciliation_side.jiomart.returns_chain.actual_oms_settlement
  edge_class: canonical
  canonical_cognee_edge: true
  source_type: reconciliation_profile
  target_type: reconciliation_side
```


```yaml
candidate_edge:
  edge_id: edge.jiomart.v9.00739.has_mismatch_category
  canonical_edge_type: HAS_MISMATCH_CATEGORY
  source_card_id: reconciliation_profile.jiomart.returns_oms_settlement_chain
  target_card_id: mismatch_category.jiomart.return_value_variance
  edge_class: canonical
  canonical_cognee_edge: true
  source_type: reconciliation_profile
  target_type: mismatch_category
```


```yaml
candidate_edge:
  edge_id: edge.jiomart.v9.00740.has_mismatch_category
  canonical_edge_type: HAS_MISMATCH_CATEGORY
  source_card_id: reconciliation_profile.jiomart.returns_oms_settlement_chain
  target_card_id: mismatch_category.jiomart.return_missing_oms_or_settlement
  edge_class: canonical
  canonical_cognee_edge: true
  source_type: reconciliation_profile
  target_type: mismatch_category
```


```yaml
candidate_edge:
  edge_id: edge.jiomart.v9.00741.belongs_to_reconciliation_profile
  canonical_edge_type: BELONGS_TO_RECONCILIATION_PROFILE
  source_card_id: reconciliation_side.jiomart.returns_chain.expected_returns
  target_card_id: reconciliation_profile.jiomart.returns_oms_settlement_chain
  edge_class: canonical
  canonical_cognee_edge: true
  source_type: reconciliation_side
  target_type: reconciliation_profile
```


```yaml
candidate_edge:
  edge_id: edge.jiomart.v9.00742.uses_table
  canonical_edge_type: USES_TABLE
  source_card_id: reconciliation_side.jiomart.returns_chain.expected_returns
  target_card_id: table.zs_observe.jiomart_returns
  edge_class: canonical
  canonical_cognee_edge: true
  source_type: reconciliation_side
  target_type: table
```


```yaml
candidate_edge:
  edge_id: edge.jiomart.v9.00743.uses_column
  canonical_edge_type: USES_COLUMN
  source_card_id: reconciliation_side.jiomart.returns_chain.expected_returns
  target_card_id: column.zs_observe.jiomart_returns.order_id
  edge_class: canonical
  canonical_cognee_edge: true
  source_type: reconciliation_side
  target_type: column
```


```yaml
candidate_edge:
  edge_id: edge.jiomart.v9.00744.belongs_to_reconciliation_profile
  canonical_edge_type: BELONGS_TO_RECONCILIATION_PROFILE
  source_card_id: reconciliation_side.jiomart.returns_chain.actual_oms_settlement
  target_card_id: reconciliation_profile.jiomart.returns_oms_settlement_chain
  edge_class: canonical
  canonical_cognee_edge: true
  source_type: reconciliation_side
  target_type: reconciliation_profile
```


```yaml
candidate_edge:
  edge_id: edge.jiomart.v9.00745.uses_table
  canonical_edge_type: USES_TABLE
  source_card_id: reconciliation_side.jiomart.returns_chain.actual_oms_settlement
  target_card_id: table.zs_observe.jiomart_oms
  edge_class: canonical
  canonical_cognee_edge: true
  source_type: reconciliation_side
  target_type: table
```


```yaml
candidate_edge:
  edge_id: edge.jiomart.v9.00746.uses_column
  canonical_edge_type: USES_COLUMN
  source_card_id: reconciliation_side.jiomart.returns_chain.actual_oms_settlement
  target_card_id: column.zs_observe.jiomart_oms.order_id
  edge_class: canonical
  canonical_cognee_edge: true
  source_type: reconciliation_side
  target_type: column
```


```yaml
candidate_edge:
  edge_id: edge.jiomart.v9.00747.applies_to_platform_context
  canonical_edge_type: APPLIES_TO_PLATFORM_CONTEXT
  source_card_id: matching_logic.jiomart.returns_chain
  target_card_id: platform_context.jiomart.in
  edge_class: canonical
  canonical_cognee_edge: true
  source_type: matching_logic
  target_type: platform_context
```


```yaml
candidate_edge:
  edge_id: edge.jiomart.v9.00748.has_reconciliation_profile
  canonical_edge_type: HAS_RECONCILIATION_PROFILE
  source_card_id: business_process.jiomart.forward_order_flow
  target_card_id: reconciliation_profile.jiomart.unreconciled_oms_orders
  edge_class: canonical
  canonical_cognee_edge: true
  source_type: business_process
  target_type: reconciliation_profile
```


```yaml
candidate_edge:
  edge_id: edge.jiomart.v9.00749.supports_process
  canonical_edge_type: SUPPORTS_PROCESS
  source_card_id: reconciliation_profile.jiomart.unreconciled_oms_orders
  target_card_id: business_process.jiomart.forward_order_flow
  edge_class: canonical
  canonical_cognee_edge: true
  source_type: reconciliation_profile
  target_type: business_process
```


```yaml
candidate_edge:
  edge_id: edge.jiomart.v9.00750.has_primary_unit
  canonical_edge_type: HAS_PRIMARY_UNIT
  source_card_id: reconciliation_profile.jiomart.unreconciled_oms_orders
  target_card_id: reconciliation_unit.jiomart.order_id
  edge_class: canonical
  canonical_cognee_edge: true
  source_type: reconciliation_profile
  target_type: reconciliation_unit
```


```yaml
candidate_edge:
  edge_id: edge.jiomart.v9.00751.uses_matching_logic
  canonical_edge_type: USES_MATCHING_LOGIC
  source_card_id: reconciliation_profile.jiomart.unreconciled_oms_orders
  target_card_id: matching_logic.jiomart.unreconciled_oms
  edge_class: canonical
  canonical_cognee_edge: true
  source_type: reconciliation_profile
  target_type: matching_logic
```


```yaml
candidate_edge:
  edge_id: edge.jiomart.v9.00752.supports_reconciliation_profile
  canonical_edge_type: SUPPORTS_RECONCILIATION_PROFILE
  source_card_id: matching_logic.jiomart.unreconciled_oms
  target_card_id: reconciliation_profile.jiomart.unreconciled_oms_orders
  edge_class: canonical
  canonical_cognee_edge: true
  source_type: matching_logic
  target_type: reconciliation_profile
```


```yaml
candidate_edge:
  edge_id: edge.jiomart.v9.00753.has_reconciliation_side
  canonical_edge_type: HAS_RECONCILIATION_SIDE
  source_card_id: reconciliation_profile.jiomart.unreconciled_oms_orders
  target_card_id: reconciliation_side.jiomart.unreconciled.expected_oms
  edge_class: canonical
  canonical_cognee_edge: true
  source_type: reconciliation_profile
  target_type: reconciliation_side
```


```yaml
candidate_edge:
  edge_id: edge.jiomart.v9.00754.has_reconciliation_side
  canonical_edge_type: HAS_RECONCILIATION_SIDE
  source_card_id: reconciliation_profile.jiomart.unreconciled_oms_orders
  target_card_id: reconciliation_side.jiomart.unreconciled.actual_settlement
  edge_class: canonical
  canonical_cognee_edge: true
  source_type: reconciliation_profile
  target_type: reconciliation_side
```


```yaml
candidate_edge:
  edge_id: edge.jiomart.v9.00755.has_mismatch_category
  canonical_edge_type: HAS_MISMATCH_CATEGORY
  source_card_id: reconciliation_profile.jiomart.unreconciled_oms_orders
  target_card_id: mismatch_category.jiomart.not_in_settlement
  edge_class: canonical
  canonical_cognee_edge: true
  source_type: reconciliation_profile
  target_type: mismatch_category
```


```yaml
candidate_edge:
  edge_id: edge.jiomart.v9.00756.belongs_to_reconciliation_profile
  canonical_edge_type: BELONGS_TO_RECONCILIATION_PROFILE
  source_card_id: reconciliation_side.jiomart.unreconciled.expected_oms
  target_card_id: reconciliation_profile.jiomart.unreconciled_oms_orders
  edge_class: canonical
  canonical_cognee_edge: true
  source_type: reconciliation_side
  target_type: reconciliation_profile
```


```yaml
candidate_edge:
  edge_id: edge.jiomart.v9.00757.uses_table
  canonical_edge_type: USES_TABLE
  source_card_id: reconciliation_side.jiomart.unreconciled.expected_oms
  target_card_id: table.zs_observe.jiomart_oms
  edge_class: canonical
  canonical_cognee_edge: true
  source_type: reconciliation_side
  target_type: table
```


```yaml
candidate_edge:
  edge_id: edge.jiomart.v9.00758.uses_column
  canonical_edge_type: USES_COLUMN
  source_card_id: reconciliation_side.jiomart.unreconciled.expected_oms
  target_card_id: column.zs_observe.jiomart_oms.order_id
  edge_class: canonical
  canonical_cognee_edge: true
  source_type: reconciliation_side
  target_type: column
```


```yaml
candidate_edge:
  edge_id: edge.jiomart.v9.00759.belongs_to_reconciliation_profile
  canonical_edge_type: BELONGS_TO_RECONCILIATION_PROFILE
  source_card_id: reconciliation_side.jiomart.unreconciled.actual_settlement
  target_card_id: reconciliation_profile.jiomart.unreconciled_oms_orders
  edge_class: canonical
  canonical_cognee_edge: true
  source_type: reconciliation_side
  target_type: reconciliation_profile
```


```yaml
candidate_edge:
  edge_id: edge.jiomart.v9.00760.uses_table
  canonical_edge_type: USES_TABLE
  source_card_id: reconciliation_side.jiomart.unreconciled.actual_settlement
  target_card_id: table.zs_observe.jiomart_settlement
  edge_class: canonical
  canonical_cognee_edge: true
  source_type: reconciliation_side
  target_type: table
```


```yaml
candidate_edge:
  edge_id: edge.jiomart.v9.00761.uses_column
  canonical_edge_type: USES_COLUMN
  source_card_id: reconciliation_side.jiomart.unreconciled.actual_settlement
  target_card_id: column.zs_observe.jiomart_settlement.order_id
  edge_class: canonical
  canonical_cognee_edge: true
  source_type: reconciliation_side
  target_type: column
```


```yaml
candidate_edge:
  edge_id: edge.jiomart.v9.00762.applies_to_platform_context
  canonical_edge_type: APPLIES_TO_PLATFORM_CONTEXT
  source_card_id: matching_logic.jiomart.unreconciled_oms
  target_card_id: platform_context.jiomart.in
  edge_class: canonical
  canonical_cognee_edge: true
  source_type: matching_logic
  target_type: platform_context
```


```yaml
candidate_edge:
  edge_id: edge.jiomart.v9.00763.has_reconciliation_profile
  canonical_edge_type: HAS_RECONCILIATION_PROFILE
  source_card_id: business_process.jiomart.settlement_event_model
  target_card_id: reconciliation_profile.jiomart.tcs_reconciliation
  edge_class: canonical
  canonical_cognee_edge: true
  source_type: business_process
  target_type: reconciliation_profile
```


```yaml
candidate_edge:
  edge_id: edge.jiomart.v9.00764.supports_process
  canonical_edge_type: SUPPORTS_PROCESS
  source_card_id: reconciliation_profile.jiomart.tcs_reconciliation
  target_card_id: business_process.jiomart.settlement_event_model
  edge_class: canonical
  canonical_cognee_edge: true
  source_type: reconciliation_profile
  target_type: business_process
```


```yaml
candidate_edge:
  edge_id: edge.jiomart.v9.00765.has_primary_unit
  canonical_edge_type: HAS_PRIMARY_UNIT
  source_card_id: reconciliation_profile.jiomart.tcs_reconciliation
  target_card_id: reconciliation_unit.jiomart.period_or_order
  edge_class: canonical
  canonical_cognee_edge: true
  source_type: reconciliation_profile
  target_type: reconciliation_unit
```


```yaml
candidate_edge:
  edge_id: edge.jiomart.v9.00766.uses_matching_logic
  canonical_edge_type: USES_MATCHING_LOGIC
  source_card_id: reconciliation_profile.jiomart.tcs_reconciliation
  target_card_id: matching_logic.jiomart.tcs_reconciliation
  edge_class: canonical
  canonical_cognee_edge: true
  source_type: reconciliation_profile
  target_type: matching_logic
```


```yaml
candidate_edge:
  edge_id: edge.jiomart.v9.00767.supports_reconciliation_profile
  canonical_edge_type: SUPPORTS_RECONCILIATION_PROFILE
  source_card_id: matching_logic.jiomart.tcs_reconciliation
  target_card_id: reconciliation_profile.jiomart.tcs_reconciliation
  edge_class: canonical
  canonical_cognee_edge: true
  source_type: matching_logic
  target_type: reconciliation_profile
```


```yaml
candidate_edge:
  edge_id: edge.jiomart.v9.00768.has_reconciliation_side
  canonical_edge_type: HAS_RECONCILIATION_SIDE
  source_card_id: reconciliation_profile.jiomart.tcs_reconciliation
  target_card_id: reconciliation_side.jiomart.tcs.expected_oms
  edge_class: canonical
  canonical_cognee_edge: true
  source_type: reconciliation_profile
  target_type: reconciliation_side
```


```yaml
candidate_edge:
  edge_id: edge.jiomart.v9.00769.has_reconciliation_side
  canonical_edge_type: HAS_RECONCILIATION_SIDE
  source_card_id: reconciliation_profile.jiomart.tcs_reconciliation
  target_card_id: reconciliation_side.jiomart.tcs.actual_settlement
  edge_class: canonical
  canonical_cognee_edge: true
  source_type: reconciliation_profile
  target_type: reconciliation_side
```


```yaml
candidate_edge:
  edge_id: edge.jiomart.v9.00770.has_mismatch_category
  canonical_edge_type: HAS_MISMATCH_CATEGORY
  source_card_id: reconciliation_profile.jiomart.tcs_reconciliation
  target_card_id: mismatch_category.jiomart.tcs_variance
  edge_class: canonical
  canonical_cognee_edge: true
  source_type: reconciliation_profile
  target_type: mismatch_category
```


```yaml
candidate_edge:
  edge_id: edge.jiomart.v9.00771.has_mismatch_category
  canonical_edge_type: HAS_MISMATCH_CATEGORY
  source_card_id: reconciliation_profile.jiomart.tcs_reconciliation
  target_card_id: mismatch_category.jiomart.tcs_rate_anomaly
  edge_class: canonical
  canonical_cognee_edge: true
  source_type: reconciliation_profile
  target_type: mismatch_category
```


```yaml
candidate_edge:
  edge_id: edge.jiomart.v9.00772.belongs_to_reconciliation_profile
  canonical_edge_type: BELONGS_TO_RECONCILIATION_PROFILE
  source_card_id: reconciliation_side.jiomart.tcs.expected_oms
  target_card_id: reconciliation_profile.jiomart.tcs_reconciliation
  edge_class: canonical
  canonical_cognee_edge: true
  source_type: reconciliation_side
  target_type: reconciliation_profile
```


```yaml
candidate_edge:
  edge_id: edge.jiomart.v9.00773.uses_table
  canonical_edge_type: USES_TABLE
  source_card_id: reconciliation_side.jiomart.tcs.expected_oms
  target_card_id: table.zs_observe.jiomart_oms
  edge_class: canonical
  canonical_cognee_edge: true
  source_type: reconciliation_side
  target_type: table
```


```yaml
candidate_edge:
  edge_id: edge.jiomart.v9.00774.uses_column
  canonical_edge_type: USES_COLUMN
  source_card_id: reconciliation_side.jiomart.tcs.expected_oms
  target_card_id: column.zs_observe.jiomart_oms.order_id
  edge_class: canonical
  canonical_cognee_edge: true
  source_type: reconciliation_side
  target_type: column
```


```yaml
candidate_edge:
  edge_id: edge.jiomart.v9.00775.belongs_to_reconciliation_profile
  canonical_edge_type: BELONGS_TO_RECONCILIATION_PROFILE
  source_card_id: reconciliation_side.jiomart.tcs.actual_settlement
  target_card_id: reconciliation_profile.jiomart.tcs_reconciliation
  edge_class: canonical
  canonical_cognee_edge: true
  source_type: reconciliation_side
  target_type: reconciliation_profile
```


```yaml
candidate_edge:
  edge_id: edge.jiomart.v9.00776.uses_table
  canonical_edge_type: USES_TABLE
  source_card_id: reconciliation_side.jiomart.tcs.actual_settlement
  target_card_id: table.zs_observe.jiomart_settlement
  edge_class: canonical
  canonical_cognee_edge: true
  source_type: reconciliation_side
  target_type: table
```


```yaml
candidate_edge:
  edge_id: edge.jiomart.v9.00777.uses_column
  canonical_edge_type: USES_COLUMN
  source_card_id: reconciliation_side.jiomart.tcs.actual_settlement
  target_card_id: column.zs_observe.jiomart_settlement.order_id
  edge_class: canonical
  canonical_cognee_edge: true
  source_type: reconciliation_side
  target_type: column
```


```yaml
candidate_edge:
  edge_id: edge.jiomart.v9.00778.applies_to_platform_context
  canonical_edge_type: APPLIES_TO_PLATFORM_CONTEXT
  source_card_id: matching_logic.jiomart.tcs_reconciliation
  target_card_id: platform_context.jiomart.in
  edge_class: canonical
  canonical_cognee_edge: true
  source_type: matching_logic
  target_type: platform_context
```


```yaml
candidate_edge:
  edge_id: edge.jiomart.v9.00779.has_reconciliation_profile
  canonical_edge_type: HAS_RECONCILIATION_PROFILE
  source_card_id: business_process.jiomart.rto_flow
  target_card_id: reconciliation_profile.jiomart.returns_oms_reconciliation
  edge_class: canonical
  canonical_cognee_edge: true
  source_type: business_process
  target_type: reconciliation_profile
```


```yaml
candidate_edge:
  edge_id: edge.jiomart.v9.00780.supports_process
  canonical_edge_type: SUPPORTS_PROCESS
  source_card_id: reconciliation_profile.jiomart.returns_oms_reconciliation
  target_card_id: business_process.jiomart.rto_flow
  edge_class: canonical
  canonical_cognee_edge: true
  source_type: reconciliation_profile
  target_type: business_process
```


```yaml
candidate_edge:
  edge_id: edge.jiomart.v9.00781.has_primary_unit
  canonical_edge_type: HAS_PRIMARY_UNIT
  source_card_id: reconciliation_profile.jiomart.returns_oms_reconciliation
  target_card_id: reconciliation_unit.jiomart.order_id
  edge_class: canonical
  canonical_cognee_edge: true
  source_type: reconciliation_profile
  target_type: reconciliation_unit
```


```yaml
candidate_edge:
  edge_id: edge.jiomart.v9.00782.uses_matching_logic
  canonical_edge_type: USES_MATCHING_LOGIC
  source_card_id: reconciliation_profile.jiomart.returns_oms_reconciliation
  target_card_id: matching_logic.jiomart.returns_oms
  edge_class: canonical
  canonical_cognee_edge: true
  source_type: reconciliation_profile
  target_type: matching_logic
```


```yaml
candidate_edge:
  edge_id: edge.jiomart.v9.00783.supports_reconciliation_profile
  canonical_edge_type: SUPPORTS_RECONCILIATION_PROFILE
  source_card_id: matching_logic.jiomart.returns_oms
  target_card_id: reconciliation_profile.jiomart.returns_oms_reconciliation
  edge_class: canonical
  canonical_cognee_edge: true
  source_type: matching_logic
  target_type: reconciliation_profile
```


```yaml
candidate_edge:
  edge_id: edge.jiomart.v9.00784.has_reconciliation_side
  canonical_edge_type: HAS_RECONCILIATION_SIDE
  source_card_id: reconciliation_profile.jiomart.returns_oms_reconciliation
  target_card_id: reconciliation_side.jiomart.returns_oms.expected_returns
  edge_class: canonical
  canonical_cognee_edge: true
  source_type: reconciliation_profile
  target_type: reconciliation_side
```


```yaml
candidate_edge:
  edge_id: edge.jiomart.v9.00785.has_reconciliation_side
  canonical_edge_type: HAS_RECONCILIATION_SIDE
  source_card_id: reconciliation_profile.jiomart.returns_oms_reconciliation
  target_card_id: reconciliation_side.jiomart.returns_oms.actual_oms
  edge_class: canonical
  canonical_cognee_edge: true
  source_type: reconciliation_profile
  target_type: reconciliation_side
```


```yaml
candidate_edge:
  edge_id: edge.jiomart.v9.00786.has_mismatch_category
  canonical_edge_type: HAS_MISMATCH_CATEGORY
  source_card_id: reconciliation_profile.jiomart.returns_oms_reconciliation
  target_card_id: mismatch_category.jiomart.return_missing_oms_or_settlement
  edge_class: canonical
  canonical_cognee_edge: true
  source_type: reconciliation_profile
  target_type: mismatch_category
```


```yaml
candidate_edge:
  edge_id: edge.jiomart.v9.00787.belongs_to_reconciliation_profile
  canonical_edge_type: BELONGS_TO_RECONCILIATION_PROFILE
  source_card_id: reconciliation_side.jiomart.returns_oms.expected_returns
  target_card_id: reconciliation_profile.jiomart.returns_oms_reconciliation
  edge_class: canonical
  canonical_cognee_edge: true
  source_type: reconciliation_side
  target_type: reconciliation_profile
```


```yaml
candidate_edge:
  edge_id: edge.jiomart.v9.00788.uses_table
  canonical_edge_type: USES_TABLE
  source_card_id: reconciliation_side.jiomart.returns_oms.expected_returns
  target_card_id: table.zs_observe.jiomart_returns
  edge_class: canonical
  canonical_cognee_edge: true
  source_type: reconciliation_side
  target_type: table
```


```yaml
candidate_edge:
  edge_id: edge.jiomart.v9.00789.uses_column
  canonical_edge_type: USES_COLUMN
  source_card_id: reconciliation_side.jiomart.returns_oms.expected_returns
  target_card_id: column.zs_observe.jiomart_returns.order_id
  edge_class: canonical
  canonical_cognee_edge: true
  source_type: reconciliation_side
  target_type: column
```


```yaml
candidate_edge:
  edge_id: edge.jiomart.v9.00790.belongs_to_reconciliation_profile
  canonical_edge_type: BELONGS_TO_RECONCILIATION_PROFILE
  source_card_id: reconciliation_side.jiomart.returns_oms.actual_oms
  target_card_id: reconciliation_profile.jiomart.returns_oms_reconciliation
  edge_class: canonical
  canonical_cognee_edge: true
  source_type: reconciliation_side
  target_type: reconciliation_profile
```


```yaml
candidate_edge:
  edge_id: edge.jiomart.v9.00791.uses_table
  canonical_edge_type: USES_TABLE
  source_card_id: reconciliation_side.jiomart.returns_oms.actual_oms
  target_card_id: table.zs_observe.jiomart_oms
  edge_class: canonical
  canonical_cognee_edge: true
  source_type: reconciliation_side
  target_type: table
```


```yaml
candidate_edge:
  edge_id: edge.jiomart.v9.00792.uses_column
  canonical_edge_type: USES_COLUMN
  source_card_id: reconciliation_side.jiomart.returns_oms.actual_oms
  target_card_id: column.zs_observe.jiomart_oms.order_id
  edge_class: canonical
  canonical_cognee_edge: true
  source_type: reconciliation_side
  target_type: column
```


```yaml
candidate_edge:
  edge_id: edge.jiomart.v9.00793.applies_to_platform_context
  canonical_edge_type: APPLIES_TO_PLATFORM_CONTEXT
  source_card_id: matching_logic.jiomart.returns_oms
  target_card_id: platform_context.jiomart.in
  edge_class: canonical
  canonical_cognee_edge: true
  source_type: matching_logic
  target_type: platform_context
```


```yaml
candidate_edge:
  edge_id: edge.jiomart.v9.00794.applies_to_platform_context
  canonical_edge_type: APPLIES_TO_PLATFORM_CONTEXT
  source_card_id: mismatch_category.jiomart.not_in_settlement
  target_card_id: platform_context.jiomart.in
  edge_class: canonical
  canonical_cognee_edge: true
  source_type: mismatch_category
  target_type: platform_context
```


```yaml
candidate_edge:
  edge_id: edge.jiomart.v9.00795.applies_to_platform_context
  canonical_edge_type: APPLIES_TO_PLATFORM_CONTEXT
  source_card_id: mismatch_category.jiomart.tcs_variance
  target_card_id: platform_context.jiomart.in
  edge_class: canonical
  canonical_cognee_edge: true
  source_type: mismatch_category
  target_type: platform_context
```


```yaml
candidate_edge:
  edge_id: edge.jiomart.v9.00796.applies_to_platform_context
  canonical_edge_type: APPLIES_TO_PLATFORM_CONTEXT
  source_card_id: mismatch_category.jiomart.return_value_variance
  target_card_id: platform_context.jiomart.in
  edge_class: canonical
  canonical_cognee_edge: true
  source_type: mismatch_category
  target_type: platform_context
```


```yaml
candidate_edge:
  edge_id: edge.jiomart.v9.00797.applies_to_platform_context
  canonical_edge_type: APPLIES_TO_PLATFORM_CONTEXT
  source_card_id: mismatch_category.jiomart.return_missing_oms_or_settlement
  target_card_id: platform_context.jiomart.in
  edge_class: canonical
  canonical_cognee_edge: true
  source_type: mismatch_category
  target_type: platform_context
```


```yaml
candidate_edge:
  edge_id: edge.jiomart.v9.00798.applies_to_platform_context
  canonical_edge_type: APPLIES_TO_PLATFORM_CONTEXT
  source_card_id: mismatch_category.jiomart.tcs_rate_anomaly
  target_card_id: platform_context.jiomart.in
  edge_class: canonical
  canonical_cognee_edge: true
  source_type: mismatch_category
  target_type: platform_context
```


```yaml
candidate_edge:
  edge_id: edge.jiomart.v9.00799.applies_to_platform_context
  canonical_edge_type: APPLIES_TO_PLATFORM_CONTEXT
  source_card_id: output_contract.jiomart.metric_summary
  target_card_id: platform_context.jiomart.in
  edge_class: canonical
  canonical_cognee_edge: true
  source_type: output_contract
  target_type: platform_context
```


```yaml
candidate_edge:
  edge_id: edge.jiomart.v9.00800.applies_to_platform_context
  canonical_edge_type: APPLIES_TO_PLATFORM_CONTEXT
  source_card_id: output_contract.jiomart.time_series
  target_card_id: platform_context.jiomart.in
  edge_class: canonical
  canonical_cognee_edge: true
  source_type: output_contract
  target_type: platform_context
```


```yaml
candidate_edge:
  edge_id: edge.jiomart.v9.00801.applies_to_platform_context
  canonical_edge_type: APPLIES_TO_PLATFORM_CONTEXT
  source_card_id: output_contract.jiomart.order_reconciliation
  target_card_id: platform_context.jiomart.in
  edge_class: canonical
  canonical_cognee_edge: true
  source_type: output_contract
  target_type: platform_context
```


```yaml
candidate_edge:
  edge_id: edge.jiomart.v9.00802.applies_to_platform_context
  canonical_edge_type: APPLIES_TO_PLATFORM_CONTEXT
  source_card_id: output_contract.jiomart.return_reconciliation
  target_card_id: platform_context.jiomart.in
  edge_class: canonical
  canonical_cognee_edge: true
  source_type: output_contract
  target_type: platform_context
```


```yaml
candidate_edge:
  edge_id: edge.jiomart.v9.00803.applies_to_platform_context
  canonical_edge_type: APPLIES_TO_PLATFORM_CONTEXT
  source_card_id: output_contract.jiomart.sku_summary
  target_card_id: platform_context.jiomart.in
  edge_class: canonical
  canonical_cognee_edge: true
  source_type: output_contract
  target_type: platform_context
```


```yaml
candidate_edge:
  edge_id: edge.jiomart.v9.00804.applies_to_platform_context
  canonical_edge_type: APPLIES_TO_PLATFORM_CONTEXT
  source_card_id: output_contract.jiomart.settlement_event_summary
  target_card_id: platform_context.jiomart.in
  edge_class: canonical
  canonical_cognee_edge: true
  source_type: output_contract
  target_type: platform_context
```


```yaml
candidate_edge:
  edge_id: edge.jiomart.v9.00805.applies_to_platform_context
  canonical_edge_type: APPLIES_TO_PLATFORM_CONTEXT
  source_card_id: output_contract.jiomart.shipment_summary
  target_card_id: platform_context.jiomart.in
  edge_class: canonical
  canonical_cognee_edge: true
  source_type: output_contract
  target_type: platform_context
```


```yaml
candidate_edge:
  edge_id: edge.jiomart.v9.00806.uses_table
  canonical_edge_type: USES_TABLE
  source_card_id: query_pattern.jiomart.marketplace.6_1_total_gmv
  target_card_id: table.zs_observe.jiomart_oms
  edge_class: canonical
  canonical_cognee_edge: true
  source_type: query_pattern
  target_type: table
```


```yaml
candidate_edge:
  edge_id: edge.jiomart.v9.00807.produces_metric
  canonical_edge_type: PRODUCES_METRIC
  source_card_id: query_pattern.jiomart.marketplace.6_1_total_gmv
  target_card_id: metric.jiomart.total_gmv
  edge_class: canonical
  canonical_cognee_edge: true
  source_type: query_pattern
  target_type: metric
```


```yaml
candidate_edge:
  edge_id: edge.jiomart.v9.00808.uses_output_contract
  canonical_edge_type: USES_OUTPUT_CONTRACT
  source_card_id: query_pattern.jiomart.marketplace.6_1_total_gmv
  target_card_id: output_contract.jiomart.metric_summary
  edge_class: canonical
  canonical_cognee_edge: true
  source_type: query_pattern
  target_type: output_contract
```


```yaml
candidate_edge:
  edge_id: edge.jiomart.v9.00809.applies_to_platform_context
  canonical_edge_type: APPLIES_TO_PLATFORM_CONTEXT
  source_card_id: query_pattern.jiomart.marketplace.6_1_total_gmv
  target_card_id: platform_context.jiomart.in
  edge_class: canonical
  canonical_cognee_edge: true
  source_type: query_pattern
  target_type: platform_context
```


```yaml
candidate_edge:
  edge_id: edge.jiomart.v9.00810.uses_table
  canonical_edge_type: USES_TABLE
  source_card_id: query_pattern.jiomart.marketplace.6_2_return_rate
  target_card_id: table.zs_observe.jiomart_oms
  edge_class: canonical
  canonical_cognee_edge: true
  source_type: query_pattern
  target_type: table
```


```yaml
candidate_edge:
  edge_id: edge.jiomart.v9.00811.produces_metric
  canonical_edge_type: PRODUCES_METRIC
  source_card_id: query_pattern.jiomart.marketplace.6_2_return_rate
  target_card_id: metric.jiomart.return_rate
  edge_class: canonical
  canonical_cognee_edge: true
  source_type: query_pattern
  target_type: metric
```


```yaml
candidate_edge:
  edge_id: edge.jiomart.v9.00812.uses_output_contract
  canonical_edge_type: USES_OUTPUT_CONTRACT
  source_card_id: query_pattern.jiomart.marketplace.6_2_return_rate
  target_card_id: output_contract.jiomart.metric_summary
  edge_class: canonical
  canonical_cognee_edge: true
  source_type: query_pattern
  target_type: output_contract
```


```yaml
candidate_edge:
  edge_id: edge.jiomart.v9.00813.applies_to_platform_context
  canonical_edge_type: APPLIES_TO_PLATFORM_CONTEXT
  source_card_id: query_pattern.jiomart.marketplace.6_2_return_rate
  target_card_id: platform_context.jiomart.in
  edge_class: canonical
  canonical_cognee_edge: true
  source_type: query_pattern
  target_type: platform_context
```


```yaml
candidate_edge:
  edge_id: edge.jiomart.v9.00814.uses_table
  canonical_edge_type: USES_TABLE
  source_card_id: query_pattern.jiomart.marketplace.6_3_average_order_value_aov
  target_card_id: table.zs_observe.jiomart_oms
  edge_class: canonical
  canonical_cognee_edge: true
  source_type: query_pattern
  target_type: table
```


```yaml
candidate_edge:
  edge_id: edge.jiomart.v9.00815.produces_metric
  canonical_edge_type: PRODUCES_METRIC
  source_card_id: query_pattern.jiomart.marketplace.6_3_average_order_value_aov
  target_card_id: metric.jiomart.average_order_value
  edge_class: canonical
  canonical_cognee_edge: true
  source_type: query_pattern
  target_type: metric
```


```yaml
candidate_edge:
  edge_id: edge.jiomart.v9.00816.uses_output_contract
  canonical_edge_type: USES_OUTPUT_CONTRACT
  source_card_id: query_pattern.jiomart.marketplace.6_3_average_order_value_aov
  target_card_id: output_contract.jiomart.metric_summary
  edge_class: canonical
  canonical_cognee_edge: true
  source_type: query_pattern
  target_type: output_contract
```


```yaml
candidate_edge:
  edge_id: edge.jiomart.v9.00817.applies_to_platform_context
  canonical_edge_type: APPLIES_TO_PLATFORM_CONTEXT
  source_card_id: query_pattern.jiomart.marketplace.6_3_average_order_value_aov
  target_card_id: platform_context.jiomart.in
  edge_class: canonical
  canonical_cognee_edge: true
  source_type: query_pattern
  target_type: platform_context
```


```yaml
candidate_edge:
  edge_id: edge.jiomart.v9.00818.uses_table
  canonical_edge_type: USES_TABLE
  source_card_id: query_pattern.jiomart.marketplace.6_4_net_settled_revenue
  target_card_id: table.zs_observe.jiomart_settlement
  edge_class: canonical
  canonical_cognee_edge: true
  source_type: query_pattern
  target_type: table
```


```yaml
candidate_edge:
  edge_id: edge.jiomart.v9.00819.produces_metric
  canonical_edge_type: PRODUCES_METRIC
  source_card_id: query_pattern.jiomart.marketplace.6_4_net_settled_revenue
  target_card_id: metric.jiomart.net_settled_revenue
  edge_class: canonical
  canonical_cognee_edge: true
  source_type: query_pattern
  target_type: metric
```


```yaml
candidate_edge:
  edge_id: edge.jiomart.v9.00820.uses_output_contract
  canonical_edge_type: USES_OUTPUT_CONTRACT
  source_card_id: query_pattern.jiomart.marketplace.6_4_net_settled_revenue
  target_card_id: output_contract.jiomart.metric_summary
  edge_class: canonical
  canonical_cognee_edge: true
  source_type: query_pattern
  target_type: output_contract
```


```yaml
candidate_edge:
  edge_id: edge.jiomart.v9.00821.applies_to_platform_context
  canonical_edge_type: APPLIES_TO_PLATFORM_CONTEXT
  source_card_id: query_pattern.jiomart.marketplace.6_4_net_settled_revenue
  target_card_id: platform_context.jiomart.in
  edge_class: canonical
  canonical_cognee_edge: true
  source_type: query_pattern
  target_type: platform_context
```


```yaml
candidate_edge:
  edge_id: edge.jiomart.v9.00822.uses_table
  canonical_edge_type: USES_TABLE
  source_card_id: query_pattern.jiomart.marketplace.6_5_seller_coupon_discount_impact
  target_card_id: table.zs_observe.jiomart_oms
  edge_class: canonical
  canonical_cognee_edge: true
  source_type: query_pattern
  target_type: table
```


```yaml
candidate_edge:
  edge_id: edge.jiomart.v9.00823.produces_metric
  canonical_edge_type: PRODUCES_METRIC
  source_card_id: query_pattern.jiomart.marketplace.6_5_seller_coupon_discount_impact
  target_card_id: metric.jiomart.seller_coupon_discount_impact
  edge_class: canonical
  canonical_cognee_edge: true
  source_type: query_pattern
  target_type: metric
```


```yaml
candidate_edge:
  edge_id: edge.jiomart.v9.00824.uses_output_contract
  canonical_edge_type: USES_OUTPUT_CONTRACT
  source_card_id: query_pattern.jiomart.marketplace.6_5_seller_coupon_discount_impact
  target_card_id: output_contract.jiomart.metric_summary
  edge_class: canonical
  canonical_cognee_edge: true
  source_type: query_pattern
  target_type: output_contract
```


```yaml
candidate_edge:
  edge_id: edge.jiomart.v9.00825.applies_to_platform_context
  canonical_edge_type: APPLIES_TO_PLATFORM_CONTEXT
  source_card_id: query_pattern.jiomart.marketplace.6_5_seller_coupon_discount_impact
  target_card_id: platform_context.jiomart.in
  edge_class: canonical
  canonical_cognee_edge: true
  source_type: query_pattern
  target_type: platform_context
```


```yaml
candidate_edge:
  edge_id: edge.jiomart.v9.00826.uses_table
  canonical_edge_type: USES_TABLE
  source_card_id: query_pattern.jiomart.marketplace.6_6_monthly_forward_orders_and_gmv
  target_card_id: table.zs_observe.jiomart_oms
  edge_class: canonical
  canonical_cognee_edge: true
  source_type: query_pattern
  target_type: table
```


```yaml
candidate_edge:
  edge_id: edge.jiomart.v9.00827.produces_metric
  canonical_edge_type: PRODUCES_METRIC
  source_card_id: query_pattern.jiomart.marketplace.6_6_monthly_forward_orders_and_gmv
  target_card_id: metric.jiomart.monthly_forward_orders_gmv
  edge_class: canonical
  canonical_cognee_edge: true
  source_type: query_pattern
  target_type: metric
```


```yaml
candidate_edge:
  edge_id: edge.jiomart.v9.00828.uses_output_contract
  canonical_edge_type: USES_OUTPUT_CONTRACT
  source_card_id: query_pattern.jiomart.marketplace.6_6_monthly_forward_orders_and_gmv
  target_card_id: output_contract.jiomart.time_series
  edge_class: canonical
  canonical_cognee_edge: true
  source_type: query_pattern
  target_type: output_contract
```


```yaml
candidate_edge:
  edge_id: edge.jiomart.v9.00829.applies_to_platform_context
  canonical_edge_type: APPLIES_TO_PLATFORM_CONTEXT
  source_card_id: query_pattern.jiomart.marketplace.6_6_monthly_forward_orders_and_gmv
  target_card_id: platform_context.jiomart.in
  edge_class: canonical
  canonical_cognee_edge: true
  source_type: query_pattern
  target_type: platform_context
```


```yaml
candidate_edge:
  edge_id: edge.jiomart.v9.00830.uses_table
  canonical_edge_type: USES_TABLE
  source_card_id: query_pattern.jiomart.marketplace.7_1_oms_settlement_match_3_way_per_order
  target_card_id: table.zs_observe.jiomart_oms
  edge_class: canonical
  canonical_cognee_edge: true
  source_type: query_pattern
  target_type: table
```


```yaml
candidate_edge:
  edge_id: edge.jiomart.v9.00831.uses_table
  canonical_edge_type: USES_TABLE
  source_card_id: query_pattern.jiomart.marketplace.7_1_oms_settlement_match_3_way_per_order
  target_card_id: table.zs_observe.jiomart_settlement
  edge_class: canonical
  canonical_cognee_edge: true
  source_type: query_pattern
  target_type: table
```


```yaml
candidate_edge:
  edge_id: edge.jiomart.v9.00832.uses_reconciliation_profile
  canonical_edge_type: USES_RECONCILIATION_PROFILE
  source_card_id: query_pattern.jiomart.marketplace.7_1_oms_settlement_match_3_way_per_order
  target_card_id: reconciliation_profile.jiomart.oms_settlement_3way
  edge_class: canonical
  canonical_cognee_edge: true
  source_type: query_pattern
  target_type: reconciliation_profile
```


```yaml
candidate_edge:
  edge_id: edge.jiomart.v9.00833.uses_output_contract
  canonical_edge_type: USES_OUTPUT_CONTRACT
  source_card_id: query_pattern.jiomart.marketplace.7_1_oms_settlement_match_3_way_per_order
  target_card_id: output_contract.jiomart.order_reconciliation
  edge_class: canonical
  canonical_cognee_edge: true
  source_type: query_pattern
  target_type: output_contract
```


```yaml
candidate_edge:
  edge_id: edge.jiomart.v9.00834.applies_to_platform_context
  canonical_edge_type: APPLIES_TO_PLATFORM_CONTEXT
  source_card_id: query_pattern.jiomart.marketplace.7_1_oms_settlement_match_3_way_per_order
  target_card_id: platform_context.jiomart.in
  edge_class: canonical
  canonical_cognee_edge: true
  source_type: query_pattern
  target_type: platform_context
```


```yaml
candidate_edge:
  edge_id: edge.jiomart.v9.00835.uses_table
  canonical_edge_type: USES_TABLE
  source_card_id: query_pattern.jiomart.marketplace.7_2_returns_oms_settlement_full_chain
  target_card_id: table.zs_observe.jiomart_oms
  edge_class: canonical
  canonical_cognee_edge: true
  source_type: query_pattern
  target_type: table
```


```yaml
candidate_edge:
  edge_id: edge.jiomart.v9.00836.uses_table
  canonical_edge_type: USES_TABLE
  source_card_id: query_pattern.jiomart.marketplace.7_2_returns_oms_settlement_full_chain
  target_card_id: table.zs_observe.jiomart_returns
  edge_class: canonical
  canonical_cognee_edge: true
  source_type: query_pattern
  target_type: table
```


```yaml
candidate_edge:
  edge_id: edge.jiomart.v9.00837.uses_table
  canonical_edge_type: USES_TABLE
  source_card_id: query_pattern.jiomart.marketplace.7_2_returns_oms_settlement_full_chain
  target_card_id: table.zs_observe.jiomart_settlement
  edge_class: canonical
  canonical_cognee_edge: true
  source_type: query_pattern
  target_type: table
```


```yaml
candidate_edge:
  edge_id: edge.jiomart.v9.00838.uses_reconciliation_profile
  canonical_edge_type: USES_RECONCILIATION_PROFILE
  source_card_id: query_pattern.jiomart.marketplace.7_2_returns_oms_settlement_full_chain
  target_card_id: reconciliation_profile.jiomart.oms_settlement_3way
  edge_class: canonical
  canonical_cognee_edge: true
  source_type: query_pattern
  target_type: reconciliation_profile
```


```yaml
candidate_edge:
  edge_id: edge.jiomart.v9.00839.uses_output_contract
  canonical_edge_type: USES_OUTPUT_CONTRACT
  source_card_id: query_pattern.jiomart.marketplace.7_2_returns_oms_settlement_full_chain
  target_card_id: output_contract.jiomart.return_reconciliation
  edge_class: canonical
  canonical_cognee_edge: true
  source_type: query_pattern
  target_type: output_contract
```


```yaml
candidate_edge:
  edge_id: edge.jiomart.v9.00840.applies_to_platform_context
  canonical_edge_type: APPLIES_TO_PLATFORM_CONTEXT
  source_card_id: query_pattern.jiomart.marketplace.7_2_returns_oms_settlement_full_chain
  target_card_id: platform_context.jiomart.in
  edge_class: canonical
  canonical_cognee_edge: true
  source_type: query_pattern
  target_type: platform_context
```


```yaml
candidate_edge:
  edge_id: edge.jiomart.v9.00841.uses_table
  canonical_edge_type: USES_TABLE
  source_card_id: query_pattern.jiomart.marketplace.7_3_unreconciled_oms_orders_not_in_settlement
  target_card_id: table.zs_observe.jiomart_oms
  edge_class: canonical
  canonical_cognee_edge: true
  source_type: query_pattern
  target_type: table
```


```yaml
candidate_edge:
  edge_id: edge.jiomart.v9.00842.uses_table
  canonical_edge_type: USES_TABLE
  source_card_id: query_pattern.jiomart.marketplace.7_3_unreconciled_oms_orders_not_in_settlement
  target_card_id: table.zs_observe.jiomart_settlement
  edge_class: canonical
  canonical_cognee_edge: true
  source_type: query_pattern
  target_type: table
```


```yaml
candidate_edge:
  edge_id: edge.jiomart.v9.00843.uses_reconciliation_profile
  canonical_edge_type: USES_RECONCILIATION_PROFILE
  source_card_id: query_pattern.jiomart.marketplace.7_3_unreconciled_oms_orders_not_in_settlement
  target_card_id: reconciliation_profile.jiomart.oms_settlement_3way
  edge_class: canonical
  canonical_cognee_edge: true
  source_type: query_pattern
  target_type: reconciliation_profile
```


```yaml
candidate_edge:
  edge_id: edge.jiomart.v9.00844.uses_output_contract
  canonical_edge_type: USES_OUTPUT_CONTRACT
  source_card_id: query_pattern.jiomart.marketplace.7_3_unreconciled_oms_orders_not_in_settlement
  target_card_id: output_contract.jiomart.order_reconciliation
  edge_class: canonical
  canonical_cognee_edge: true
  source_type: query_pattern
  target_type: output_contract
```


```yaml
candidate_edge:
  edge_id: edge.jiomart.v9.00845.applies_to_platform_context
  canonical_edge_type: APPLIES_TO_PLATFORM_CONTEXT
  source_card_id: query_pattern.jiomart.marketplace.7_3_unreconciled_oms_orders_not_in_settlement
  target_card_id: platform_context.jiomart.in
  edge_class: canonical
  canonical_cognee_edge: true
  source_type: query_pattern
  target_type: platform_context
```


```yaml
candidate_edge:
  edge_id: edge.jiomart.v9.00846.uses_table
  canonical_edge_type: USES_TABLE
  source_card_id: query_pattern.jiomart.marketplace.7_4_tcs_reconciliation
  target_card_id: table.zs_observe.jiomart_oms
  edge_class: canonical
  canonical_cognee_edge: true
  source_type: query_pattern
  target_type: table
```


```yaml
candidate_edge:
  edge_id: edge.jiomart.v9.00847.uses_table
  canonical_edge_type: USES_TABLE
  source_card_id: query_pattern.jiomart.marketplace.7_4_tcs_reconciliation
  target_card_id: table.zs_observe.jiomart_settlement
  edge_class: canonical
  canonical_cognee_edge: true
  source_type: query_pattern
  target_type: table
```


```yaml
candidate_edge:
  edge_id: edge.jiomart.v9.00848.produces_metric
  canonical_edge_type: PRODUCES_METRIC
  source_card_id: query_pattern.jiomart.marketplace.7_4_tcs_reconciliation
  target_card_id: metric.jiomart.tcs_deducted
  edge_class: canonical
  canonical_cognee_edge: true
  source_type: query_pattern
  target_type: metric
```


```yaml
candidate_edge:
  edge_id: edge.jiomart.v9.00849.uses_reconciliation_profile
  canonical_edge_type: USES_RECONCILIATION_PROFILE
  source_card_id: query_pattern.jiomart.marketplace.7_4_tcs_reconciliation
  target_card_id: reconciliation_profile.jiomart.tcs_reconciliation
  edge_class: canonical
  canonical_cognee_edge: true
  source_type: query_pattern
  target_type: reconciliation_profile
```


```yaml
candidate_edge:
  edge_id: edge.jiomart.v9.00850.uses_output_contract
  canonical_edge_type: USES_OUTPUT_CONTRACT
  source_card_id: query_pattern.jiomart.marketplace.7_4_tcs_reconciliation
  target_card_id: output_contract.jiomart.order_reconciliation
  edge_class: canonical
  canonical_cognee_edge: true
  source_type: query_pattern
  target_type: output_contract
```


```yaml
candidate_edge:
  edge_id: edge.jiomart.v9.00851.applies_to_platform_context
  canonical_edge_type: APPLIES_TO_PLATFORM_CONTEXT
  source_card_id: query_pattern.jiomart.marketplace.7_4_tcs_reconciliation
  target_card_id: platform_context.jiomart.in
  edge_class: canonical
  canonical_cognee_edge: true
  source_type: query_pattern
  target_type: platform_context
```


```yaml
candidate_edge:
  edge_id: edge.jiomart.v9.00852.uses_output_contract
  canonical_edge_type: USES_OUTPUT_CONTRACT
  source_card_id: query_pattern.jiomart.marketplace.9_mandatory_query_filters
  target_card_id: output_contract.jiomart.metric_summary
  edge_class: canonical
  canonical_cognee_edge: true
  source_type: query_pattern
  target_type: output_contract
```


```yaml
candidate_edge:
  edge_id: edge.jiomart.v9.00853.applies_to_platform_context
  canonical_edge_type: APPLIES_TO_PLATFORM_CONTEXT
  source_card_id: query_pattern.jiomart.marketplace.9_mandatory_query_filters
  target_card_id: platform_context.jiomart.in
  edge_class: canonical
  canonical_cognee_edge: true
  source_type: query_pattern
  target_type: platform_context
```


```yaml
candidate_edge:
  edge_id: edge.jiomart.v9.00854.uses_table
  canonical_edge_type: USES_TABLE
  source_card_id: query_pattern.jiomart.shipment.7_1_shipment_status_summary
  target_card_id: table.zs_observe.jiomart_shipment
  edge_class: canonical
  canonical_cognee_edge: true
  source_type: query_pattern
  target_type: table
```


```yaml
candidate_edge:
  edge_id: edge.jiomart.v9.00855.produces_metric
  canonical_edge_type: PRODUCES_METRIC
  source_card_id: query_pattern.jiomart.shipment.7_1_shipment_status_summary
  target_card_id: metric.jiomart.shipment_status_gmv
  edge_class: canonical
  canonical_cognee_edge: true
  source_type: query_pattern
  target_type: metric
```


```yaml
candidate_edge:
  edge_id: edge.jiomart.v9.00856.uses_output_contract
  canonical_edge_type: USES_OUTPUT_CONTRACT
  source_card_id: query_pattern.jiomart.shipment.7_1_shipment_status_summary
  target_card_id: output_contract.jiomart.shipment_summary
  edge_class: canonical
  canonical_cognee_edge: true
  source_type: query_pattern
  target_type: output_contract
```


```yaml
candidate_edge:
  edge_id: edge.jiomart.v9.00857.applies_to_platform_context
  canonical_edge_type: APPLIES_TO_PLATFORM_CONTEXT
  source_card_id: query_pattern.jiomart.shipment.7_1_shipment_status_summary
  target_card_id: platform_context.jiomart.in
  edge_class: canonical
  canonical_cognee_edge: true
  source_type: query_pattern
  target_type: platform_context
```


```yaml
candidate_edge:
  edge_id: edge.jiomart.v9.00858.uses_table
  canonical_edge_type: USES_TABLE
  source_card_id: query_pattern.jiomart.shipment.7_2_monthly_gmv
  target_card_id: table.zs_observe.jiomart_shipment
  edge_class: canonical
  canonical_cognee_edge: true
  source_type: query_pattern
  target_type: table
```


```yaml
candidate_edge:
  edge_id: edge.jiomart.v9.00859.produces_metric
  canonical_edge_type: PRODUCES_METRIC
  source_card_id: query_pattern.jiomart.shipment.7_2_monthly_gmv
  target_card_id: metric.jiomart.shipment_monthly_gmv
  edge_class: canonical
  canonical_cognee_edge: true
  source_type: query_pattern
  target_type: metric
```


```yaml
candidate_edge:
  edge_id: edge.jiomart.v9.00860.uses_output_contract
  canonical_edge_type: USES_OUTPUT_CONTRACT
  source_card_id: query_pattern.jiomart.shipment.7_2_monthly_gmv
  target_card_id: output_contract.jiomart.time_series
  edge_class: canonical
  canonical_cognee_edge: true
  source_type: query_pattern
  target_type: output_contract
```


```yaml
candidate_edge:
  edge_id: edge.jiomart.v9.00861.applies_to_platform_context
  canonical_edge_type: APPLIES_TO_PLATFORM_CONTEXT
  source_card_id: query_pattern.jiomart.shipment.7_2_monthly_gmv
  target_card_id: platform_context.jiomart.in
  edge_class: canonical
  canonical_cognee_edge: true
  source_type: query_pattern
  target_type: platform_context
```


```yaml
candidate_edge:
  edge_id: edge.jiomart.v9.00862.uses_table
  canonical_edge_type: USES_TABLE
  source_card_id: query_pattern.jiomart.shipment.7_3_top_skus
  target_card_id: table.zs_observe.jiomart_shipment
  edge_class: canonical
  canonical_cognee_edge: true
  source_type: query_pattern
  target_type: table
```


```yaml
candidate_edge:
  edge_id: edge.jiomart.v9.00863.produces_metric
  canonical_edge_type: PRODUCES_METRIC
  source_card_id: query_pattern.jiomart.shipment.7_3_top_skus
  target_card_id: metric.jiomart.top_shipment_skus
  edge_class: canonical
  canonical_cognee_edge: true
  source_type: query_pattern
  target_type: metric
```


```yaml
candidate_edge:
  edge_id: edge.jiomart.v9.00864.uses_output_contract
  canonical_edge_type: USES_OUTPUT_CONTRACT
  source_card_id: query_pattern.jiomart.shipment.7_3_top_skus
  target_card_id: output_contract.jiomart.sku_summary
  edge_class: canonical
  canonical_cognee_edge: true
  source_type: query_pattern
  target_type: output_contract
```


```yaml
candidate_edge:
  edge_id: edge.jiomart.v9.00865.applies_to_platform_context
  canonical_edge_type: APPLIES_TO_PLATFORM_CONTEXT
  source_card_id: query_pattern.jiomart.shipment.7_3_top_skus
  target_card_id: platform_context.jiomart.in
  edge_class: canonical
  canonical_cognee_edge: true
  source_type: query_pattern
  target_type: platform_context
```


```yaml
candidate_edge:
  edge_id: edge.jiomart.v9.00866.uses_table
  canonical_edge_type: USES_TABLE
  source_card_id: query_pattern.jiomart.settlement.8_1_net_settlement_per_order_structured_rows
  target_card_id: table.zs_observe.jiomart_settlement
  edge_class: canonical
  canonical_cognee_edge: true
  source_type: query_pattern
  target_type: table
```


```yaml
candidate_edge:
  edge_id: edge.jiomart.v9.00867.produces_metric
  canonical_edge_type: PRODUCES_METRIC
  source_card_id: query_pattern.jiomart.settlement.8_1_net_settlement_per_order_structured_rows
  target_card_id: metric.jiomart.net_settlement_per_order
  edge_class: canonical
  canonical_cognee_edge: true
  source_type: query_pattern
  target_type: metric
```


```yaml
candidate_edge:
  edge_id: edge.jiomart.v9.00868.uses_output_contract
  canonical_edge_type: USES_OUTPUT_CONTRACT
  source_card_id: query_pattern.jiomart.settlement.8_1_net_settlement_per_order_structured_rows
  target_card_id: output_contract.jiomart.metric_summary
  edge_class: canonical
  canonical_cognee_edge: true
  source_type: query_pattern
  target_type: output_contract
```


```yaml
candidate_edge:
  edge_id: edge.jiomart.v9.00869.applies_to_platform_context
  canonical_edge_type: APPLIES_TO_PLATFORM_CONTEXT
  source_card_id: query_pattern.jiomart.settlement.8_1_net_settlement_per_order_structured_rows
  target_card_id: platform_context.jiomart.in
  edge_class: canonical
  canonical_cognee_edge: true
  source_type: query_pattern
  target_type: platform_context
```


```yaml
candidate_edge:
  edge_id: edge.jiomart.v9.00870.uses_table
  canonical_edge_type: USES_TABLE
  source_card_id: query_pattern.jiomart.settlement.8_2_monthly_settlement_summary
  target_card_id: table.zs_observe.jiomart_settlement
  edge_class: canonical
  canonical_cognee_edge: true
  source_type: query_pattern
  target_type: table
```


```yaml
candidate_edge:
  edge_id: edge.jiomart.v9.00871.produces_metric
  canonical_edge_type: PRODUCES_METRIC
  source_card_id: query_pattern.jiomart.settlement.8_2_monthly_settlement_summary
  target_card_id: metric.jiomart.monthly_settlement_summary
  edge_class: canonical
  canonical_cognee_edge: true
  source_type: query_pattern
  target_type: metric
```


```yaml
candidate_edge:
  edge_id: edge.jiomart.v9.00872.uses_output_contract
  canonical_edge_type: USES_OUTPUT_CONTRACT
  source_card_id: query_pattern.jiomart.settlement.8_2_monthly_settlement_summary
  target_card_id: output_contract.jiomart.time_series
  edge_class: canonical
  canonical_cognee_edge: true
  source_type: query_pattern
  target_type: output_contract
```


```yaml
candidate_edge:
  edge_id: edge.jiomart.v9.00873.applies_to_platform_context
  canonical_edge_type: APPLIES_TO_PLATFORM_CONTEXT
  source_card_id: query_pattern.jiomart.settlement.8_2_monthly_settlement_summary
  target_card_id: platform_context.jiomart.in
  edge_class: canonical
  canonical_cognee_edge: true
  source_type: query_pattern
  target_type: platform_context
```


```yaml
candidate_edge:
  edge_id: edge.jiomart.v9.00874.uses_table
  canonical_edge_type: USES_TABLE
  source_card_id: query_pattern.jiomart.settlement.8_3_settlement_oms_reconciliation
  target_card_id: table.zs_observe.jiomart_oms
  edge_class: canonical
  canonical_cognee_edge: true
  source_type: query_pattern
  target_type: table
```


```yaml
candidate_edge:
  edge_id: edge.jiomart.v9.00875.uses_table
  canonical_edge_type: USES_TABLE
  source_card_id: query_pattern.jiomart.settlement.8_3_settlement_oms_reconciliation
  target_card_id: table.zs_observe.jiomart_settlement
  edge_class: canonical
  canonical_cognee_edge: true
  source_type: query_pattern
  target_type: table
```


```yaml
candidate_edge:
  edge_id: edge.jiomart.v9.00876.uses_reconciliation_profile
  canonical_edge_type: USES_RECONCILIATION_PROFILE
  source_card_id: query_pattern.jiomart.settlement.8_3_settlement_oms_reconciliation
  target_card_id: reconciliation_profile.jiomart.oms_settlement_3way
  edge_class: canonical
  canonical_cognee_edge: true
  source_type: query_pattern
  target_type: reconciliation_profile
```


```yaml
candidate_edge:
  edge_id: edge.jiomart.v9.00877.uses_output_contract
  canonical_edge_type: USES_OUTPUT_CONTRACT
  source_card_id: query_pattern.jiomart.settlement.8_3_settlement_oms_reconciliation
  target_card_id: output_contract.jiomart.order_reconciliation
  edge_class: canonical
  canonical_cognee_edge: true
  source_type: query_pattern
  target_type: output_contract
```


```yaml
candidate_edge:
  edge_id: edge.jiomart.v9.00878.applies_to_platform_context
  canonical_edge_type: APPLIES_TO_PLATFORM_CONTEXT
  source_card_id: query_pattern.jiomart.settlement.8_3_settlement_oms_reconciliation
  target_card_id: platform_context.jiomart.in
  edge_class: canonical
  canonical_cognee_edge: true
  source_type: query_pattern
  target_type: platform_context
```


```yaml
candidate_edge:
  edge_id: edge.jiomart.v9.00879.uses_table
  canonical_edge_type: USES_TABLE
  source_card_id: query_pattern.jiomart.settlement.8_4_tcs_reconciliation_oms_vs_settlement
  target_card_id: table.zs_observe.jiomart_oms
  edge_class: canonical
  canonical_cognee_edge: true
  source_type: query_pattern
  target_type: table
```


```yaml
candidate_edge:
  edge_id: edge.jiomart.v9.00880.uses_table
  canonical_edge_type: USES_TABLE
  source_card_id: query_pattern.jiomart.settlement.8_4_tcs_reconciliation_oms_vs_settlement
  target_card_id: table.zs_observe.jiomart_settlement
  edge_class: canonical
  canonical_cognee_edge: true
  source_type: query_pattern
  target_type: table
```


```yaml
candidate_edge:
  edge_id: edge.jiomart.v9.00881.produces_metric
  canonical_edge_type: PRODUCES_METRIC
  source_card_id: query_pattern.jiomart.settlement.8_4_tcs_reconciliation_oms_vs_settlement
  target_card_id: metric.jiomart.tcs_deducted
  edge_class: canonical
  canonical_cognee_edge: true
  source_type: query_pattern
  target_type: metric
```


```yaml
candidate_edge:
  edge_id: edge.jiomart.v9.00882.uses_reconciliation_profile
  canonical_edge_type: USES_RECONCILIATION_PROFILE
  source_card_id: query_pattern.jiomart.settlement.8_4_tcs_reconciliation_oms_vs_settlement
  target_card_id: reconciliation_profile.jiomart.tcs_reconciliation
  edge_class: canonical
  canonical_cognee_edge: true
  source_type: query_pattern
  target_type: reconciliation_profile
```


```yaml
candidate_edge:
  edge_id: edge.jiomart.v9.00883.uses_output_contract
  canonical_edge_type: USES_OUTPUT_CONTRACT
  source_card_id: query_pattern.jiomart.settlement.8_4_tcs_reconciliation_oms_vs_settlement
  target_card_id: output_contract.jiomart.order_reconciliation
  edge_class: canonical
  canonical_cognee_edge: true
  source_type: query_pattern
  target_type: output_contract
```


```yaml
candidate_edge:
  edge_id: edge.jiomart.v9.00884.applies_to_platform_context
  canonical_edge_type: APPLIES_TO_PLATFORM_CONTEXT
  source_card_id: query_pattern.jiomart.settlement.8_4_tcs_reconciliation_oms_vs_settlement
  target_card_id: platform_context.jiomart.in
  edge_class: canonical
  canonical_cognee_edge: true
  source_type: query_pattern
  target_type: platform_context
```


```yaml
candidate_edge:
  edge_id: edge.jiomart.v9.00885.uses_table
  canonical_edge_type: USES_TABLE
  source_card_id: query_pattern.jiomart.settlement.8_5_credit_debit_notes
  target_card_id: table.zs_observe.jiomart_settlement
  edge_class: canonical
  canonical_cognee_edge: true
  source_type: query_pattern
  target_type: table
```


```yaml
candidate_edge:
  edge_id: edge.jiomart.v9.00886.produces_metric
  canonical_edge_type: PRODUCES_METRIC
  source_card_id: query_pattern.jiomart.settlement.8_5_credit_debit_notes
  target_card_id: metric.jiomart.credit_debit_note_impact
  edge_class: canonical
  canonical_cognee_edge: true
  source_type: query_pattern
  target_type: metric
```


```yaml
candidate_edge:
  edge_id: edge.jiomart.v9.00887.uses_output_contract
  canonical_edge_type: USES_OUTPUT_CONTRACT
  source_card_id: query_pattern.jiomart.settlement.8_5_credit_debit_notes
  target_card_id: output_contract.jiomart.settlement_event_summary
  edge_class: canonical
  canonical_cognee_edge: true
  source_type: query_pattern
  target_type: output_contract
```


```yaml
candidate_edge:
  edge_id: edge.jiomart.v9.00888.applies_to_platform_context
  canonical_edge_type: APPLIES_TO_PLATFORM_CONTEXT
  source_card_id: query_pattern.jiomart.settlement.8_5_credit_debit_notes
  target_card_id: platform_context.jiomart.in
  edge_class: canonical
  canonical_cognee_edge: true
  source_type: query_pattern
  target_type: platform_context
```


```yaml
candidate_edge:
  edge_id: edge.jiomart.v9.00889.uses_table
  canonical_edge_type: USES_TABLE
  source_card_id: query_pattern.jiomart.returns.7_1_return_volume_by_type
  target_card_id: table.zs_observe.jiomart_returns
  edge_class: canonical
  canonical_cognee_edge: true
  source_type: query_pattern
  target_type: table
```


```yaml
candidate_edge:
  edge_id: edge.jiomart.v9.00890.produces_metric
  canonical_edge_type: PRODUCES_METRIC
  source_card_id: query_pattern.jiomart.returns.7_1_return_volume_by_type
  target_card_id: metric.jiomart.return_volume_by_type
  edge_class: canonical
  canonical_cognee_edge: true
  source_type: query_pattern
  target_type: metric
```


```yaml
candidate_edge:
  edge_id: edge.jiomart.v9.00891.uses_output_contract
  canonical_edge_type: USES_OUTPUT_CONTRACT
  source_card_id: query_pattern.jiomart.returns.7_1_return_volume_by_type
  target_card_id: output_contract.jiomart.metric_summary
  edge_class: canonical
  canonical_cognee_edge: true
  source_type: query_pattern
  target_type: output_contract
```


```yaml
candidate_edge:
  edge_id: edge.jiomart.v9.00892.applies_to_platform_context
  canonical_edge_type: APPLIES_TO_PLATFORM_CONTEXT
  source_card_id: query_pattern.jiomart.returns.7_1_return_volume_by_type
  target_card_id: platform_context.jiomart.in
  edge_class: canonical
  canonical_cognee_edge: true
  source_type: query_pattern
  target_type: platform_context
```


```yaml
candidate_edge:
  edge_id: edge.jiomart.v9.00893.uses_table
  canonical_edge_type: USES_TABLE
  source_card_id: query_pattern.jiomart.returns.7_2_return_cycle_time_rto_turnaround
  target_card_id: table.zs_observe.jiomart_returns
  edge_class: canonical
  canonical_cognee_edge: true
  source_type: query_pattern
  target_type: table
```


```yaml
candidate_edge:
  edge_id: edge.jiomart.v9.00894.produces_metric
  canonical_edge_type: PRODUCES_METRIC
  source_card_id: query_pattern.jiomart.returns.7_2_return_cycle_time_rto_turnaround
  target_card_id: metric.jiomart.return_cycle_time
  edge_class: canonical
  canonical_cognee_edge: true
  source_type: query_pattern
  target_type: metric
```


```yaml
candidate_edge:
  edge_id: edge.jiomart.v9.00895.uses_output_contract
  canonical_edge_type: USES_OUTPUT_CONTRACT
  source_card_id: query_pattern.jiomart.returns.7_2_return_cycle_time_rto_turnaround
  target_card_id: output_contract.jiomart.metric_summary
  edge_class: canonical
  canonical_cognee_edge: true
  source_type: query_pattern
  target_type: output_contract
```


```yaml
candidate_edge:
  edge_id: edge.jiomart.v9.00896.applies_to_platform_context
  canonical_edge_type: APPLIES_TO_PLATFORM_CONTEXT
  source_card_id: query_pattern.jiomart.returns.7_2_return_cycle_time_rto_turnaround
  target_card_id: platform_context.jiomart.in
  edge_class: canonical
  canonical_cognee_edge: true
  source_type: query_pattern
  target_type: platform_context
```


```yaml
candidate_edge:
  edge_id: edge.jiomart.v9.00897.uses_table
  canonical_edge_type: USES_TABLE
  source_card_id: query_pattern.jiomart.returns.7_3_returns_oms_reconciliation
  target_card_id: table.zs_observe.jiomart_oms
  edge_class: canonical
  canonical_cognee_edge: true
  source_type: query_pattern
  target_type: table
```


```yaml
candidate_edge:
  edge_id: edge.jiomart.v9.00898.uses_table
  canonical_edge_type: USES_TABLE
  source_card_id: query_pattern.jiomart.returns.7_3_returns_oms_reconciliation
  target_card_id: table.zs_observe.jiomart_returns
  edge_class: canonical
  canonical_cognee_edge: true
  source_type: query_pattern
  target_type: table
```


```yaml
candidate_edge:
  edge_id: edge.jiomart.v9.00899.uses_output_contract
  canonical_edge_type: USES_OUTPUT_CONTRACT
  source_card_id: query_pattern.jiomart.returns.7_3_returns_oms_reconciliation
  target_card_id: output_contract.jiomart.return_reconciliation
  edge_class: canonical
  canonical_cognee_edge: true
  source_type: query_pattern
  target_type: output_contract
```


```yaml
candidate_edge:
  edge_id: edge.jiomart.v9.00900.applies_to_platform_context
  canonical_edge_type: APPLIES_TO_PLATFORM_CONTEXT
  source_card_id: query_pattern.jiomart.returns.7_3_returns_oms_reconciliation
  target_card_id: platform_context.jiomart.in
  edge_class: canonical
  canonical_cognee_edge: true
  source_type: query_pattern
  target_type: platform_context
```


```yaml
candidate_edge:
  edge_id: edge.jiomart.v9.00901.uses_table
  canonical_edge_type: USES_TABLE
  source_card_id: query_pattern.jiomart.returns.7_4_sku_level_return_rate
  target_card_id: table.zs_observe.jiomart_returns
  edge_class: canonical
  canonical_cognee_edge: true
  source_type: query_pattern
  target_type: table
```


```yaml
candidate_edge:
  edge_id: edge.jiomart.v9.00902.produces_metric
  canonical_edge_type: PRODUCES_METRIC
  source_card_id: query_pattern.jiomart.returns.7_4_sku_level_return_rate
  target_card_id: metric.jiomart.sku_return_rate
  edge_class: canonical
  canonical_cognee_edge: true
  source_type: query_pattern
  target_type: metric
```


```yaml
candidate_edge:
  edge_id: edge.jiomart.v9.00903.uses_output_contract
  canonical_edge_type: USES_OUTPUT_CONTRACT
  source_card_id: query_pattern.jiomart.returns.7_4_sku_level_return_rate
  target_card_id: output_contract.jiomart.sku_summary
  edge_class: canonical
  canonical_cognee_edge: true
  source_type: query_pattern
  target_type: output_contract
```


```yaml
candidate_edge:
  edge_id: edge.jiomart.v9.00904.applies_to_platform_context
  canonical_edge_type: APPLIES_TO_PLATFORM_CONTEXT
  source_card_id: query_pattern.jiomart.returns.7_4_sku_level_return_rate
  target_card_id: platform_context.jiomart.in
  edge_class: canonical
  canonical_cognee_edge: true
  source_type: query_pattern
  target_type: platform_context
```


```yaml
candidate_edge:
  edge_id: edge.jiomart.v9.00905.uses_table
  canonical_edge_type: USES_TABLE
  source_card_id: query_pattern.jiomart.oms.7_1_monthly_gmv_clean_rows_only
  target_card_id: table.zs_observe.jiomart_oms
  edge_class: canonical
  canonical_cognee_edge: true
  source_type: query_pattern
  target_type: table
```


```yaml
candidate_edge:
  edge_id: edge.jiomart.v9.00906.produces_metric
  canonical_edge_type: PRODUCES_METRIC
  source_card_id: query_pattern.jiomart.oms.7_1_monthly_gmv_clean_rows_only
  target_card_id: metric.jiomart.oms_monthly_gmv_clean
  edge_class: canonical
  canonical_cognee_edge: true
  source_type: query_pattern
  target_type: metric
```


```yaml
candidate_edge:
  edge_id: edge.jiomart.v9.00907.uses_output_contract
  canonical_edge_type: USES_OUTPUT_CONTRACT
  source_card_id: query_pattern.jiomart.oms.7_1_monthly_gmv_clean_rows_only
  target_card_id: output_contract.jiomart.time_series
  edge_class: canonical
  canonical_cognee_edge: true
  source_type: query_pattern
  target_type: output_contract
```


```yaml
candidate_edge:
  edge_id: edge.jiomart.v9.00908.applies_to_platform_context
  canonical_edge_type: APPLIES_TO_PLATFORM_CONTEXT
  source_card_id: query_pattern.jiomart.oms.7_1_monthly_gmv_clean_rows_only
  target_card_id: platform_context.jiomart.in
  edge_class: canonical
  canonical_cognee_edge: true
  source_type: query_pattern
  target_type: platform_context
```


```yaml
candidate_edge:
  edge_id: edge.jiomart.v9.00909.uses_table
  canonical_edge_type: USES_TABLE
  source_card_id: query_pattern.jiomart.oms.7_2_clean_forward_orders_exclude_column_shifted_rows
  target_card_id: table.zs_observe.jiomart_oms
  edge_class: canonical
  canonical_cognee_edge: true
  source_type: query_pattern
  target_type: table
```


```yaml
candidate_edge:
  edge_id: edge.jiomart.v9.00910.uses_output_contract
  canonical_edge_type: USES_OUTPUT_CONTRACT
  source_card_id: query_pattern.jiomart.oms.7_2_clean_forward_orders_exclude_column_shifted_rows
  target_card_id: output_contract.jiomart.metric_summary
  edge_class: canonical
  canonical_cognee_edge: true
  source_type: query_pattern
  target_type: output_contract
```


```yaml
candidate_edge:
  edge_id: edge.jiomart.v9.00911.applies_to_platform_context
  canonical_edge_type: APPLIES_TO_PLATFORM_CONTEXT
  source_card_id: query_pattern.jiomart.oms.7_2_clean_forward_orders_exclude_column_shifted_rows
  target_card_id: platform_context.jiomart.in
  edge_class: canonical
  canonical_cognee_edge: true
  source_type: query_pattern
  target_type: platform_context
```


```yaml
candidate_edge:
  edge_id: edge.jiomart.v9.00912.uses_table
  canonical_edge_type: USES_TABLE
  source_card_id: query_pattern.jiomart.oms.7_3_intra_state_vs_inter_state_gst_analysis
  target_card_id: table.zs_observe.jiomart_oms
  edge_class: canonical
  canonical_cognee_edge: true
  source_type: query_pattern
  target_type: table
```


```yaml
candidate_edge:
  edge_id: edge.jiomart.v9.00913.produces_metric
  canonical_edge_type: PRODUCES_METRIC
  source_card_id: query_pattern.jiomart.oms.7_3_intra_state_vs_inter_state_gst_analysis
  target_card_id: metric.jiomart.gst_breakdown
  edge_class: canonical
  canonical_cognee_edge: true
  source_type: query_pattern
  target_type: metric
```


```yaml
candidate_edge:
  edge_id: edge.jiomart.v9.00914.uses_output_contract
  canonical_edge_type: USES_OUTPUT_CONTRACT
  source_card_id: query_pattern.jiomart.oms.7_3_intra_state_vs_inter_state_gst_analysis
  target_card_id: output_contract.jiomart.metric_summary
  edge_class: canonical
  canonical_cognee_edge: true
  source_type: query_pattern
  target_type: output_contract
```


```yaml
candidate_edge:
  edge_id: edge.jiomart.v9.00915.applies_to_platform_context
  canonical_edge_type: APPLIES_TO_PLATFORM_CONTEXT
  source_card_id: query_pattern.jiomart.oms.7_3_intra_state_vs_inter_state_gst_analysis
  target_card_id: platform_context.jiomart.in
  edge_class: canonical
  canonical_cognee_edge: true
  source_type: query_pattern
  target_type: platform_context
```


```yaml
candidate_edge:
  edge_id: edge.jiomart.v9.00916.uses_table
  canonical_edge_type: USES_TABLE
  source_card_id: query_pattern.jiomart.oms.7_4_sku_level_performance
  target_card_id: table.zs_observe.jiomart_oms
  edge_class: canonical
  canonical_cognee_edge: true
  source_type: query_pattern
  target_type: table
```


```yaml
candidate_edge:
  edge_id: edge.jiomart.v9.00917.produces_metric
  canonical_edge_type: PRODUCES_METRIC
  source_card_id: query_pattern.jiomart.oms.7_4_sku_level_performance
  target_card_id: metric.jiomart.oms_sku_performance
  edge_class: canonical
  canonical_cognee_edge: true
  source_type: query_pattern
  target_type: metric
```


```yaml
candidate_edge:
  edge_id: edge.jiomart.v9.00918.uses_output_contract
  canonical_edge_type: USES_OUTPUT_CONTRACT
  source_card_id: query_pattern.jiomart.oms.7_4_sku_level_performance
  target_card_id: output_contract.jiomart.sku_summary
  edge_class: canonical
  canonical_cognee_edge: true
  source_type: query_pattern
  target_type: output_contract
```


```yaml
candidate_edge:
  edge_id: edge.jiomart.v9.00919.applies_to_platform_context
  canonical_edge_type: APPLIES_TO_PLATFORM_CONTEXT
  source_card_id: query_pattern.jiomart.oms.7_4_sku_level_performance
  target_card_id: platform_context.jiomart.in
  edge_class: canonical
  canonical_cognee_edge: true
  source_type: query_pattern
  target_type: platform_context
```


```yaml
candidate_edge:
  edge_id: edge.jiomart.v9.00920.uses_table
  canonical_edge_type: USES_TABLE
  source_card_id: query_pattern.jiomart.oms.7_5_oms_settlement_join
  target_card_id: table.zs_observe.jiomart_oms
  edge_class: canonical
  canonical_cognee_edge: true
  source_type: query_pattern
  target_type: table
```


```yaml
candidate_edge:
  edge_id: edge.jiomart.v9.00921.uses_table
  canonical_edge_type: USES_TABLE
  source_card_id: query_pattern.jiomart.oms.7_5_oms_settlement_join
  target_card_id: table.zs_observe.jiomart_settlement
  edge_class: canonical
  canonical_cognee_edge: true
  source_type: query_pattern
  target_type: table
```


```yaml
candidate_edge:
  edge_id: edge.jiomart.v9.00922.uses_reconciliation_profile
  canonical_edge_type: USES_RECONCILIATION_PROFILE
  source_card_id: query_pattern.jiomart.oms.7_5_oms_settlement_join
  target_card_id: reconciliation_profile.jiomart.oms_settlement_3way
  edge_class: canonical
  canonical_cognee_edge: true
  source_type: query_pattern
  target_type: reconciliation_profile
```


```yaml
candidate_edge:
  edge_id: edge.jiomart.v9.00923.uses_output_contract
  canonical_edge_type: USES_OUTPUT_CONTRACT
  source_card_id: query_pattern.jiomart.oms.7_5_oms_settlement_join
  target_card_id: output_contract.jiomart.metric_summary
  edge_class: canonical
  canonical_cognee_edge: true
  source_type: query_pattern
  target_type: output_contract
```


```yaml
candidate_edge:
  edge_id: edge.jiomart.v9.00924.applies_to_platform_context
  canonical_edge_type: APPLIES_TO_PLATFORM_CONTEXT
  source_card_id: query_pattern.jiomart.oms.7_5_oms_settlement_join
  target_card_id: platform_context.jiomart.in
  edge_class: canonical
  canonical_cognee_edge: true
  source_type: query_pattern
  target_type: platform_context
```


```yaml
candidate_edge:
  edge_id: edge.jiomart.v9.00925.uses_table
  canonical_edge_type: USES_TABLE
  source_card_id: query_pattern.jiomart.oms.7_6_return_rate
  target_card_id: table.zs_observe.jiomart_oms
  edge_class: canonical
  canonical_cognee_edge: true
  source_type: query_pattern
  target_type: table
```


```yaml
candidate_edge:
  edge_id: edge.jiomart.v9.00926.uses_output_contract
  canonical_edge_type: USES_OUTPUT_CONTRACT
  source_card_id: query_pattern.jiomart.oms.7_6_return_rate
  target_card_id: output_contract.jiomart.metric_summary
  edge_class: canonical
  canonical_cognee_edge: true
  source_type: query_pattern
  target_type: output_contract
```


```yaml
candidate_edge:
  edge_id: edge.jiomart.v9.00927.applies_to_platform_context
  canonical_edge_type: APPLIES_TO_PLATFORM_CONTEXT
  source_card_id: query_pattern.jiomart.oms.7_6_return_rate
  target_card_id: platform_context.jiomart.in
  edge_class: canonical
  canonical_cognee_edge: true
  source_type: query_pattern
  target_type: platform_context
```


```yaml
candidate_edge:
  edge_id: edge.jiomart.v9.00928.applies_to_platform_context
  canonical_edge_type: APPLIES_TO_PLATFORM_CONTEXT
  source_card_id: rule.jiomart.scope_fields_are_columns
  target_card_id: platform_context.jiomart.in
  edge_class: canonical
  canonical_cognee_edge: true
  source_type: rule
  target_type: platform_context
```


```yaml
candidate_edge:
  edge_id: edge.jiomart.v9.00929.targets_card
  canonical_edge_type: TARGETS_CARD
  source_card_id: rule.jiomart.scope_fields_are_columns
  target_card_id: table.zs_observe.jiomart_oms
  edge_class: canonical
  canonical_cognee_edge: true
  source_type: rule
  target_type: table
```


```yaml
candidate_edge:
  edge_id: edge.jiomart.v9.00930.targets_card
  canonical_edge_type: TARGETS_CARD
  source_card_id: rule.jiomart.scope_fields_are_columns
  target_card_id: table.zs_observe.jiomart_settlement
  edge_class: canonical
  canonical_cognee_edge: true
  source_type: rule
  target_type: table
```


```yaml
candidate_edge:
  edge_id: edge.jiomart.v9.00931.targets_card
  canonical_edge_type: TARGETS_CARD
  source_card_id: rule.jiomart.scope_fields_are_columns
  target_card_id: table.zs_observe.jiomart_returns
  edge_class: canonical
  canonical_cognee_edge: true
  source_type: rule
  target_type: table
```


```yaml
candidate_edge:
  edge_id: edge.jiomart.v9.00932.targets_card
  canonical_edge_type: TARGETS_CARD
  source_card_id: rule.jiomart.scope_fields_are_columns
  target_card_id: table.zs_observe.jiomart_shipment
  edge_class: canonical
  canonical_cognee_edge: true
  source_type: rule
  target_type: table
```


```yaml
candidate_edge:
  edge_id: edge.jiomart.v9.00933.includes_rule
  canonical_edge_type: INCLUDES_RULE
  source_card_id: execution_constraint_set.jiomart.marketplace_query_constraints
  target_card_id: rule.jiomart.scope_fields_are_columns
  edge_class: canonical
  canonical_cognee_edge: true
  source_type: execution_constraint_set
  target_type: rule
```


```yaml
candidate_edge:
  edge_id: edge.jiomart.v9.00934.applies_to_platform_context
  canonical_edge_type: APPLIES_TO_PLATFORM_CONTEXT
  source_card_id: rule.jiomart.mandatory_filters_group_26
  target_card_id: platform_context.jiomart.in
  edge_class: canonical
  canonical_cognee_edge: true
  source_type: rule
  target_type: platform_context
```


```yaml
candidate_edge:
  edge_id: edge.jiomart.v9.00935.targets_card
  canonical_edge_type: TARGETS_CARD
  source_card_id: rule.jiomart.mandatory_filters_group_26
  target_card_id: table.zs_observe.jiomart_oms
  edge_class: canonical
  canonical_cognee_edge: true
  source_type: rule
  target_type: table
```


```yaml
candidate_edge:
  edge_id: edge.jiomart.v9.00936.targets_card
  canonical_edge_type: TARGETS_CARD
  source_card_id: rule.jiomart.mandatory_filters_group_26
  target_card_id: table.zs_observe.jiomart_settlement
  edge_class: canonical
  canonical_cognee_edge: true
  source_type: rule
  target_type: table
```


```yaml
candidate_edge:
  edge_id: edge.jiomart.v9.00937.targets_card
  canonical_edge_type: TARGETS_CARD
  source_card_id: rule.jiomart.mandatory_filters_group_26
  target_card_id: table.zs_observe.jiomart_returns
  edge_class: canonical
  canonical_cognee_edge: true
  source_type: rule
  target_type: table
```


```yaml
candidate_edge:
  edge_id: edge.jiomart.v9.00938.includes_rule
  canonical_edge_type: INCLUDES_RULE
  source_card_id: execution_constraint_set.jiomart.marketplace_query_constraints
  target_card_id: rule.jiomart.mandatory_filters_group_26
  edge_class: canonical
  canonical_cognee_edge: true
  source_type: execution_constraint_set
  target_type: rule
```


```yaml
candidate_edge:
  edge_id: edge.jiomart.v9.00939.applies_to_platform_context
  canonical_edge_type: APPLIES_TO_PLATFORM_CONTEXT
  source_card_id: rule.jiomart.mandatory_filters_group_221
  target_card_id: platform_context.jiomart.in
  edge_class: canonical
  canonical_cognee_edge: true
  source_type: rule
  target_type: platform_context
```


```yaml
candidate_edge:
  edge_id: edge.jiomart.v9.00940.targets_card
  canonical_edge_type: TARGETS_CARD
  source_card_id: rule.jiomart.mandatory_filters_group_221
  target_card_id: table.zs_observe.jiomart_shipment
  edge_class: canonical
  canonical_cognee_edge: true
  source_type: rule
  target_type: table
```


```yaml
candidate_edge:
  edge_id: edge.jiomart.v9.00941.includes_rule
  canonical_edge_type: INCLUDES_RULE
  source_card_id: execution_constraint_set.jiomart.marketplace_query_constraints
  target_card_id: rule.jiomart.mandatory_filters_group_221
  edge_class: canonical
  canonical_cognee_edge: true
  source_type: execution_constraint_set
  target_type: rule
```


```yaml
candidate_edge:
  edge_id: edge.jiomart.v9.00942.applies_to_platform_context
  canonical_edge_type: APPLIES_TO_PLATFORM_CONTEXT
  source_card_id: rule.jiomart.never_cross_join_shipment
  target_card_id: platform_context.jiomart.in
  edge_class: canonical
  canonical_cognee_edge: true
  source_type: rule
  target_type: platform_context
```


```yaml
candidate_edge:
  edge_id: edge.jiomart.v9.00943.targets_card
  canonical_edge_type: TARGETS_CARD
  source_card_id: rule.jiomart.never_cross_join_shipment
  target_card_id: table.zs_observe.jiomart_shipment
  edge_class: canonical
  canonical_cognee_edge: true
  source_type: rule
  target_type: table
```


```yaml
candidate_edge:
  edge_id: edge.jiomart.v9.00944.targets_card
  canonical_edge_type: TARGETS_CARD
  source_card_id: rule.jiomart.never_cross_join_shipment
  target_card_id: table.zs_observe.jiomart_oms
  edge_class: canonical
  canonical_cognee_edge: true
  source_type: rule
  target_type: table
```


```yaml
candidate_edge:
  edge_id: edge.jiomart.v9.00945.includes_rule
  canonical_edge_type: INCLUDES_RULE
  source_card_id: execution_constraint_set.jiomart.marketplace_query_constraints
  target_card_id: rule.jiomart.never_cross_join_shipment
  edge_class: canonical
  canonical_cognee_edge: true
  source_type: execution_constraint_set
  target_type: rule
```


```yaml
candidate_edge:
  edge_id: edge.jiomart.v9.00946.applies_to_platform_context
  canonical_edge_type: APPLIES_TO_PLATFORM_CONTEXT
  source_card_id: rule.jiomart.use_order_id_for_oms_settlement
  target_card_id: platform_context.jiomart.in
  edge_class: canonical
  canonical_cognee_edge: true
  source_type: rule
  target_type: platform_context
```


```yaml
candidate_edge:
  edge_id: edge.jiomart.v9.00947.targets_card
  canonical_edge_type: TARGETS_CARD
  source_card_id: rule.jiomart.use_order_id_for_oms_settlement
  target_card_id: relationship.jiomart.oms_settlement.order_id
  edge_class: canonical
  canonical_cognee_edge: true
  source_type: rule
  target_type: relationship
```


```yaml
candidate_edge:
  edge_id: edge.jiomart.v9.00948.includes_rule
  canonical_edge_type: INCLUDES_RULE
  source_card_id: execution_constraint_set.jiomart.marketplace_query_constraints
  target_card_id: rule.jiomart.use_order_id_for_oms_settlement
  edge_class: canonical
  canonical_cognee_edge: true
  source_type: execution_constraint_set
  target_type: rule
```


```yaml
candidate_edge:
  edge_id: edge.jiomart.v9.00949.applies_to_platform_context
  canonical_edge_type: APPLIES_TO_PLATFORM_CONTEXT
  source_card_id: rule.jiomart.aggregate_settlement_before_join
  target_card_id: platform_context.jiomart.in
  edge_class: canonical
  canonical_cognee_edge: true
  source_type: rule
  target_type: platform_context
```


```yaml
candidate_edge:
  edge_id: edge.jiomart.v9.00950.targets_card
  canonical_edge_type: TARGETS_CARD
  source_card_id: rule.jiomart.aggregate_settlement_before_join
  target_card_id: table.zs_observe.jiomart_settlement
  edge_class: canonical
  canonical_cognee_edge: true
  source_type: rule
  target_type: table
```


```yaml
candidate_edge:
  edge_id: edge.jiomart.v9.00951.includes_rule
  canonical_edge_type: INCLUDES_RULE
  source_card_id: execution_constraint_set.jiomart.marketplace_query_constraints
  target_card_id: rule.jiomart.aggregate_settlement_before_join
  edge_class: canonical
  canonical_cognee_edge: true
  source_type: execution_constraint_set
  target_type: rule
```


```yaml
candidate_edge:
  edge_id: edge.jiomart.v9.00952.applies_to_platform_context
  canonical_edge_type: APPLIES_TO_PLATFORM_CONTEXT
  source_card_id: rule.jiomart.event_not_null_for_structured_analysis
  target_card_id: platform_context.jiomart.in
  edge_class: canonical
  canonical_cognee_edge: true
  source_type: rule
  target_type: platform_context
```


```yaml
candidate_edge:
  edge_id: edge.jiomart.v9.00953.targets_card
  canonical_edge_type: TARGETS_CARD
  source_card_id: rule.jiomart.event_not_null_for_structured_analysis
  target_card_id: table.zs_observe.jiomart_settlement
  edge_class: canonical
  canonical_cognee_edge: true
  source_type: rule
  target_type: table
```


```yaml
candidate_edge:
  edge_id: edge.jiomart.v9.00954.includes_rule
  canonical_edge_type: INCLUDES_RULE
  source_card_id: execution_constraint_set.jiomart.marketplace_query_constraints
  target_card_id: rule.jiomart.event_not_null_for_structured_analysis
  edge_class: canonical
  canonical_cognee_edge: true
  source_type: execution_constraint_set
  target_type: rule
```


```yaml
candidate_edge:
  edge_id: edge.jiomart.v9.00955.applies_to_platform_context
  canonical_edge_type: APPLIES_TO_PLATFORM_CONTEXT
  source_card_id: rule.jiomart.cast_return_amounts
  target_card_id: platform_context.jiomart.in
  edge_class: canonical
  canonical_cognee_edge: true
  source_type: rule
  target_type: platform_context
```


```yaml
candidate_edge:
  edge_id: edge.jiomart.v9.00956.targets_card
  canonical_edge_type: TARGETS_CARD
  source_card_id: rule.jiomart.cast_return_amounts
  target_card_id: column.zs_observe.jiomart_returns.charged_amount
  edge_class: canonical
  canonical_cognee_edge: true
  source_type: rule
  target_type: column
```


```yaml
candidate_edge:
  edge_id: edge.jiomart.v9.00957.targets_card
  canonical_edge_type: TARGETS_CARD
  source_card_id: rule.jiomart.cast_return_amounts
  target_card_id: column.zs_observe.jiomart_returns.refund_amount
  edge_class: canonical
  canonical_cognee_edge: true
  source_type: rule
  target_type: column
```


```yaml
candidate_edge:
  edge_id: edge.jiomart.v9.00958.includes_rule
  canonical_edge_type: INCLUDES_RULE
  source_card_id: execution_constraint_set.jiomart.marketplace_query_constraints
  target_card_id: rule.jiomart.cast_return_amounts
  edge_class: canonical
  canonical_cognee_edge: true
  source_type: execution_constraint_set
  target_type: rule
```


```yaml
candidate_edge:
  edge_id: edge.jiomart.v9.00959.applies_to_platform_context
  canonical_edge_type: APPLIES_TO_PLATFORM_CONTEXT
  source_card_id: rule.jiomart.use_created_date_for_oms_time_series
  target_card_id: platform_context.jiomart.in
  edge_class: canonical
  canonical_cognee_edge: true
  source_type: rule
  target_type: platform_context
```


```yaml
candidate_edge:
  edge_id: edge.jiomart.v9.00960.targets_card
  canonical_edge_type: TARGETS_CARD
  source_card_id: rule.jiomart.use_created_date_for_oms_time_series
  target_card_id: column.zs_observe.jiomart_oms.created_date
  edge_class: canonical
  canonical_cognee_edge: true
  source_type: rule
  target_type: column
```


```yaml
candidate_edge:
  edge_id: edge.jiomart.v9.00961.includes_rule
  canonical_edge_type: INCLUDES_RULE
  source_card_id: execution_constraint_set.jiomart.marketplace_query_constraints
  target_card_id: rule.jiomart.use_created_date_for_oms_time_series
  edge_class: canonical
  canonical_cognee_edge: true
  source_type: execution_constraint_set
  target_type: rule
```


```yaml
candidate_edge:
  edge_id: edge.jiomart.v9.00962.applies_to_platform_context
  canonical_edge_type: APPLIES_TO_PLATFORM_CONTEXT
  source_card_id: rule.jiomart.use_sku_id_mp_sin_combined_key
  target_card_id: platform_context.jiomart.in
  edge_class: canonical
  canonical_cognee_edge: true
  source_type: rule
  target_type: platform_context
```


```yaml
candidate_edge:
  edge_id: edge.jiomart.v9.00963.targets_card
  canonical_edge_type: TARGETS_CARD
  source_card_id: rule.jiomart.use_sku_id_mp_sin_combined_key
  target_card_id: column.zs_observe.jiomart_oms.sku_id
  edge_class: canonical
  canonical_cognee_edge: true
  source_type: rule
  target_type: column
```


```yaml
candidate_edge:
  edge_id: edge.jiomart.v9.00964.targets_card
  canonical_edge_type: TARGETS_CARD
  source_card_id: rule.jiomart.use_sku_id_mp_sin_combined_key
  target_card_id: column.zs_observe.jiomart_oms.mp_sin
  edge_class: canonical
  canonical_cognee_edge: true
  source_type: rule
  target_type: column
```


```yaml
candidate_edge:
  edge_id: edge.jiomart.v9.00965.includes_rule
  canonical_edge_type: INCLUDES_RULE
  source_card_id: execution_constraint_set.jiomart.marketplace_query_constraints
  target_card_id: rule.jiomart.use_sku_id_mp_sin_combined_key
  edge_class: canonical
  canonical_cognee_edge: true
  source_type: execution_constraint_set
  target_type: rule
```


```yaml
candidate_edge:
  edge_id: edge.jiomart.v9.00966.applies_to_platform_context
  canonical_edge_type: APPLIES_TO_PLATFORM_CONTEXT
  source_card_id: rule.jiomart.flag_tcs_rate_anomaly
  target_card_id: platform_context.jiomart.in
  edge_class: canonical
  canonical_cognee_edge: true
  source_type: rule
  target_type: platform_context
```


```yaml
candidate_edge:
  edge_id: edge.jiomart.v9.00967.targets_card
  canonical_edge_type: TARGETS_CARD
  source_card_id: rule.jiomart.flag_tcs_rate_anomaly
  target_card_id: column.zs_observe.jiomart_oms.tcs_igst_rate
  edge_class: canonical
  canonical_cognee_edge: true
  source_type: rule
  target_type: column
```


```yaml
candidate_edge:
  edge_id: edge.jiomart.v9.00968.includes_rule
  canonical_edge_type: INCLUDES_RULE
  source_card_id: execution_constraint_set.jiomart.marketplace_query_constraints
  target_card_id: rule.jiomart.flag_tcs_rate_anomaly
  edge_class: canonical
  canonical_cognee_edge: true
  source_type: execution_constraint_set
  target_type: rule
```


```yaml
candidate_edge:
  edge_id: edge.jiomart.v9.00969.applies_to_platform_context
  canonical_edge_type: APPLIES_TO_PLATFORM_CONTEXT
  source_card_id: rule.jiomart.no_explicit_commission_rows
  target_card_id: platform_context.jiomart.in
  edge_class: canonical
  canonical_cognee_edge: true
  source_type: rule
  target_type: platform_context
```


```yaml
candidate_edge:
  edge_id: edge.jiomart.v9.00970.targets_card
  canonical_edge_type: TARGETS_CARD
  source_card_id: rule.jiomart.no_explicit_commission_rows
  target_card_id: table.zs_observe.jiomart_settlement
  edge_class: canonical
  canonical_cognee_edge: true
  source_type: rule
  target_type: table
```


```yaml
candidate_edge:
  edge_id: edge.jiomart.v9.00971.includes_rule
  canonical_edge_type: INCLUDES_RULE
  source_card_id: execution_constraint_set.jiomart.marketplace_query_constraints
  target_card_id: rule.jiomart.no_explicit_commission_rows
  edge_class: canonical
  canonical_cognee_edge: true
  source_type: execution_constraint_set
  target_type: rule
```


```yaml
candidate_edge:
  edge_id: edge.jiomart.v9.00972.applies_to_platform_context
  canonical_edge_type: APPLIES_TO_PLATFORM_CONTEXT
  source_card_id: validation_test.jiomart.no_missing_active_filter
  target_card_id: platform_context.jiomart.in
  edge_class: canonical
  canonical_cognee_edge: true
  source_type: validation_test
  target_type: platform_context
```


```yaml
candidate_edge:
  edge_id: edge.jiomart.v9.00973.enforces_rule
  canonical_edge_type: ENFORCES_RULE
  source_card_id: validation_test.jiomart.no_missing_active_filter
  target_card_id: rule.jiomart.mandatory_filters_group_26
  edge_class: canonical
  canonical_cognee_edge: true
  source_type: validation_test
  target_type: rule
```


```yaml
candidate_edge:
  edge_id: edge.jiomart.v9.00974.enforces_rule
  canonical_edge_type: ENFORCES_RULE
  source_card_id: validation_test.jiomart.no_missing_active_filter
  target_card_id: rule.jiomart.mandatory_filters_group_221
  edge_class: canonical
  canonical_cognee_edge: true
  source_type: validation_test
  target_type: rule
```


```yaml
candidate_edge:
  edge_id: edge.jiomart.v9.00975.includes_validation_test
  canonical_edge_type: INCLUDES_VALIDATION_TEST
  source_card_id: execution_constraint_set.jiomart.marketplace_query_constraints
  target_card_id: validation_test.jiomart.no_missing_active_filter
  edge_class: canonical
  canonical_cognee_edge: true
  source_type: execution_constraint_set
  target_type: validation_test
```


```yaml
candidate_edge:
  edge_id: edge.jiomart.v9.00976.applies_to_platform_context
  canonical_edge_type: APPLIES_TO_PLATFORM_CONTEXT
  source_card_id: validation_test.jiomart.no_shipment_cross_join
  target_card_id: platform_context.jiomart.in
  edge_class: canonical
  canonical_cognee_edge: true
  source_type: validation_test
  target_type: platform_context
```


```yaml
candidate_edge:
  edge_id: edge.jiomart.v9.00977.enforces_rule
  canonical_edge_type: ENFORCES_RULE
  source_card_id: validation_test.jiomart.no_shipment_cross_join
  target_card_id: rule.jiomart.never_cross_join_shipment
  edge_class: canonical
  canonical_cognee_edge: true
  source_type: validation_test
  target_type: rule
```


```yaml
candidate_edge:
  edge_id: edge.jiomart.v9.00978.includes_validation_test
  canonical_edge_type: INCLUDES_VALIDATION_TEST
  source_card_id: execution_constraint_set.jiomart.marketplace_query_constraints
  target_card_id: validation_test.jiomart.no_shipment_cross_join
  edge_class: canonical
  canonical_cognee_edge: true
  source_type: execution_constraint_set
  target_type: validation_test
```


```yaml
candidate_edge:
  edge_id: edge.jiomart.v9.00979.applies_to_platform_context
  canonical_edge_type: APPLIES_TO_PLATFORM_CONTEXT
  source_card_id: validation_test.jiomart.returns_amount_cast
  target_card_id: platform_context.jiomart.in
  edge_class: canonical
  canonical_cognee_edge: true
  source_type: validation_test
  target_type: platform_context
```


```yaml
candidate_edge:
  edge_id: edge.jiomart.v9.00980.enforces_rule
  canonical_edge_type: ENFORCES_RULE
  source_card_id: validation_test.jiomart.returns_amount_cast
  target_card_id: rule.jiomart.cast_return_amounts
  edge_class: canonical
  canonical_cognee_edge: true
  source_type: validation_test
  target_type: rule
```


```yaml
candidate_edge:
  edge_id: edge.jiomart.v9.00981.includes_validation_test
  canonical_edge_type: INCLUDES_VALIDATION_TEST
  source_card_id: execution_constraint_set.jiomart.marketplace_query_constraints
  target_card_id: validation_test.jiomart.returns_amount_cast
  edge_class: canonical
  canonical_cognee_edge: true
  source_type: execution_constraint_set
  target_type: validation_test
```


```yaml
candidate_edge:
  edge_id: edge.jiomart.v9.00982.applies_to_platform_context
  canonical_edge_type: APPLIES_TO_PLATFORM_CONTEXT
  source_card_id: validation_test.jiomart.settlement_preaggregation
  target_card_id: platform_context.jiomart.in
  edge_class: canonical
  canonical_cognee_edge: true
  source_type: validation_test
  target_type: platform_context
```


```yaml
candidate_edge:
  edge_id: edge.jiomart.v9.00983.enforces_rule
  canonical_edge_type: ENFORCES_RULE
  source_card_id: validation_test.jiomart.settlement_preaggregation
  target_card_id: rule.jiomart.aggregate_settlement_before_join
  edge_class: canonical
  canonical_cognee_edge: true
  source_type: validation_test
  target_type: rule
```


```yaml
candidate_edge:
  edge_id: edge.jiomart.v9.00984.includes_validation_test
  canonical_edge_type: INCLUDES_VALIDATION_TEST
  source_card_id: execution_constraint_set.jiomart.marketplace_query_constraints
  target_card_id: validation_test.jiomart.settlement_preaggregation
  edge_class: canonical
  canonical_cognee_edge: true
  source_type: execution_constraint_set
  target_type: validation_test
```


```yaml
candidate_edge:
  edge_id: edge.jiomart.v9.00985.applies_to_platform_context
  canonical_edge_type: APPLIES_TO_PLATFORM_CONTEXT
  source_card_id: validation_test.jiomart.order_id_join_preferred
  target_card_id: platform_context.jiomart.in
  edge_class: canonical
  canonical_cognee_edge: true
  source_type: validation_test
  target_type: platform_context
```


```yaml
candidate_edge:
  edge_id: edge.jiomart.v9.00986.enforces_rule
  canonical_edge_type: ENFORCES_RULE
  source_card_id: validation_test.jiomart.order_id_join_preferred
  target_card_id: rule.jiomart.use_order_id_for_oms_settlement
  edge_class: canonical
  canonical_cognee_edge: true
  source_type: validation_test
  target_type: rule
```


```yaml
candidate_edge:
  edge_id: edge.jiomart.v9.00987.includes_validation_test
  canonical_edge_type: INCLUDES_VALIDATION_TEST
  source_card_id: execution_constraint_set.jiomart.marketplace_query_constraints
  target_card_id: validation_test.jiomart.order_id_join_preferred
  edge_class: canonical
  canonical_cognee_edge: true
  source_type: execution_constraint_set
  target_type: validation_test
```


```yaml
candidate_edge:
  edge_id: edge.jiomart.v9.00988.applies_to_platform_context
  canonical_edge_type: APPLIES_TO_PLATFORM_CONTEXT
  source_card_id: validation_test.jiomart.tcs_rate_anomaly
  target_card_id: platform_context.jiomart.in
  edge_class: canonical
  canonical_cognee_edge: true
  source_type: validation_test
  target_type: platform_context
```


```yaml
candidate_edge:
  edge_id: edge.jiomart.v9.00989.enforces_rule
  canonical_edge_type: ENFORCES_RULE
  source_card_id: validation_test.jiomart.tcs_rate_anomaly
  target_card_id: rule.jiomart.flag_tcs_rate_anomaly
  edge_class: canonical
  canonical_cognee_edge: true
  source_type: validation_test
  target_type: rule
```


```yaml
candidate_edge:
  edge_id: edge.jiomart.v9.00990.includes_validation_test
  canonical_edge_type: INCLUDES_VALIDATION_TEST
  source_card_id: execution_constraint_set.jiomart.marketplace_query_constraints
  target_card_id: validation_test.jiomart.tcs_rate_anomaly
  edge_class: canonical
  canonical_cognee_edge: true
  source_type: execution_constraint_set
  target_type: validation_test
```


```yaml
candidate_edge:
  edge_id: edge.jiomart.v9.00991.applies_to_platform_context
  canonical_edge_type: APPLIES_TO_PLATFORM_CONTEXT
  source_card_id: execution_constraint_set.jiomart.marketplace_query_constraints
  target_card_id: platform_context.jiomart.in
  edge_class: canonical
  canonical_cognee_edge: true
  source_type: execution_constraint_set
  target_type: platform_context
```


```yaml
candidate_edge:
  edge_id: edge.jiomart.v9.00992.applies_to_query_pattern
  canonical_edge_type: APPLIES_TO_QUERY_PATTERN
  source_card_id: execution_constraint_set.jiomart.marketplace_query_constraints
  target_card_id: query_pattern.jiomart.marketplace.6_1_total_gmv
  edge_class: canonical
  canonical_cognee_edge: true
  source_type: execution_constraint_set
  target_type: query_pattern
```


```yaml
candidate_edge:
  edge_id: edge.jiomart.v9.00993.applies_to_query_pattern
  canonical_edge_type: APPLIES_TO_QUERY_PATTERN
  source_card_id: execution_constraint_set.jiomart.marketplace_query_constraints
  target_card_id: query_pattern.jiomart.marketplace.6_2_return_rate
  edge_class: canonical
  canonical_cognee_edge: true
  source_type: execution_constraint_set
  target_type: query_pattern
```


```yaml
candidate_edge:
  edge_id: edge.jiomart.v9.00994.applies_to_query_pattern
  canonical_edge_type: APPLIES_TO_QUERY_PATTERN
  source_card_id: execution_constraint_set.jiomart.marketplace_query_constraints
  target_card_id: query_pattern.jiomart.marketplace.6_3_average_order_value_aov
  edge_class: canonical
  canonical_cognee_edge: true
  source_type: execution_constraint_set
  target_type: query_pattern
```


```yaml
candidate_edge:
  edge_id: edge.jiomart.v9.00995.applies_to_query_pattern
  canonical_edge_type: APPLIES_TO_QUERY_PATTERN
  source_card_id: execution_constraint_set.jiomart.marketplace_query_constraints
  target_card_id: query_pattern.jiomart.marketplace.6_4_net_settled_revenue
  edge_class: canonical
  canonical_cognee_edge: true
  source_type: execution_constraint_set
  target_type: query_pattern
```


```yaml
candidate_edge:
  edge_id: edge.jiomart.v9.00996.applies_to_query_pattern
  canonical_edge_type: APPLIES_TO_QUERY_PATTERN
  source_card_id: execution_constraint_set.jiomart.marketplace_query_constraints
  target_card_id: query_pattern.jiomart.marketplace.6_5_seller_coupon_discount_impact
  edge_class: canonical
  canonical_cognee_edge: true
  source_type: execution_constraint_set
  target_type: query_pattern
```


```yaml
candidate_edge:
  edge_id: edge.jiomart.v9.00997.applies_to_query_pattern
  canonical_edge_type: APPLIES_TO_QUERY_PATTERN
  source_card_id: execution_constraint_set.jiomart.marketplace_query_constraints
  target_card_id: query_pattern.jiomart.marketplace.6_6_monthly_forward_orders_and_gmv
  edge_class: canonical
  canonical_cognee_edge: true
  source_type: execution_constraint_set
  target_type: query_pattern
```


```yaml
candidate_edge:
  edge_id: edge.jiomart.v9.00998.applies_to_query_pattern
  canonical_edge_type: APPLIES_TO_QUERY_PATTERN
  source_card_id: execution_constraint_set.jiomart.marketplace_query_constraints
  target_card_id: query_pattern.jiomart.marketplace.7_1_oms_settlement_match_3_way_per_order
  edge_class: canonical
  canonical_cognee_edge: true
  source_type: execution_constraint_set
  target_type: query_pattern
```


```yaml
candidate_edge:
  edge_id: edge.jiomart.v9.00999.applies_to_query_pattern
  canonical_edge_type: APPLIES_TO_QUERY_PATTERN
  source_card_id: execution_constraint_set.jiomart.marketplace_query_constraints
  target_card_id: query_pattern.jiomart.marketplace.7_2_returns_oms_settlement_full_chain
  edge_class: canonical
  canonical_cognee_edge: true
  source_type: execution_constraint_set
  target_type: query_pattern
```


```yaml
candidate_edge:
  edge_id: edge.jiomart.v9.01000.applies_to_query_pattern
  canonical_edge_type: APPLIES_TO_QUERY_PATTERN
  source_card_id: execution_constraint_set.jiomart.marketplace_query_constraints
  target_card_id: query_pattern.jiomart.marketplace.7_3_unreconciled_oms_orders_not_in_settlement
  edge_class: canonical
  canonical_cognee_edge: true
  source_type: execution_constraint_set
  target_type: query_pattern
```


```yaml
candidate_edge:
  edge_id: edge.jiomart.v9.01001.applies_to_query_pattern
  canonical_edge_type: APPLIES_TO_QUERY_PATTERN
  source_card_id: execution_constraint_set.jiomart.marketplace_query_constraints
  target_card_id: query_pattern.jiomart.marketplace.7_4_tcs_reconciliation
  edge_class: canonical
  canonical_cognee_edge: true
  source_type: execution_constraint_set
  target_type: query_pattern
```


```yaml
candidate_edge:
  edge_id: edge.jiomart.v9.01002.applies_to_query_pattern
  canonical_edge_type: APPLIES_TO_QUERY_PATTERN
  source_card_id: execution_constraint_set.jiomart.marketplace_query_constraints
  target_card_id: query_pattern.jiomart.marketplace.9_mandatory_query_filters
  edge_class: canonical
  canonical_cognee_edge: true
  source_type: execution_constraint_set
  target_type: query_pattern
```


```yaml
candidate_edge:
  edge_id: edge.jiomart.v9.01003.applies_to_query_pattern
  canonical_edge_type: APPLIES_TO_QUERY_PATTERN
  source_card_id: execution_constraint_set.jiomart.marketplace_query_constraints
  target_card_id: query_pattern.jiomart.shipment.7_1_shipment_status_summary
  edge_class: canonical
  canonical_cognee_edge: true
  source_type: execution_constraint_set
  target_type: query_pattern
```


```yaml
candidate_edge:
  edge_id: edge.jiomart.v9.01004.applies_to_query_pattern
  canonical_edge_type: APPLIES_TO_QUERY_PATTERN
  source_card_id: execution_constraint_set.jiomart.marketplace_query_constraints
  target_card_id: query_pattern.jiomart.shipment.7_2_monthly_gmv
  edge_class: canonical
  canonical_cognee_edge: true
  source_type: execution_constraint_set
  target_type: query_pattern
```


```yaml
candidate_edge:
  edge_id: edge.jiomart.v9.01005.applies_to_query_pattern
  canonical_edge_type: APPLIES_TO_QUERY_PATTERN
  source_card_id: execution_constraint_set.jiomart.marketplace_query_constraints
  target_card_id: query_pattern.jiomart.shipment.7_3_top_skus
  edge_class: canonical
  canonical_cognee_edge: true
  source_type: execution_constraint_set
  target_type: query_pattern
```


```yaml
candidate_edge:
  edge_id: edge.jiomart.v9.01006.applies_to_query_pattern
  canonical_edge_type: APPLIES_TO_QUERY_PATTERN
  source_card_id: execution_constraint_set.jiomart.marketplace_query_constraints
  target_card_id: query_pattern.jiomart.settlement.8_1_net_settlement_per_order_structured_rows
  edge_class: canonical
  canonical_cognee_edge: true
  source_type: execution_constraint_set
  target_type: query_pattern
```


```yaml
candidate_edge:
  edge_id: edge.jiomart.v9.01007.applies_to_query_pattern
  canonical_edge_type: APPLIES_TO_QUERY_PATTERN
  source_card_id: execution_constraint_set.jiomart.marketplace_query_constraints
  target_card_id: query_pattern.jiomart.settlement.8_2_monthly_settlement_summary
  edge_class: canonical
  canonical_cognee_edge: true
  source_type: execution_constraint_set
  target_type: query_pattern
```


```yaml
candidate_edge:
  edge_id: edge.jiomart.v9.01008.applies_to_query_pattern
  canonical_edge_type: APPLIES_TO_QUERY_PATTERN
  source_card_id: execution_constraint_set.jiomart.marketplace_query_constraints
  target_card_id: query_pattern.jiomart.settlement.8_3_settlement_oms_reconciliation
  edge_class: canonical
  canonical_cognee_edge: true
  source_type: execution_constraint_set
  target_type: query_pattern
```


```yaml
candidate_edge:
  edge_id: edge.jiomart.v9.01009.applies_to_query_pattern
  canonical_edge_type: APPLIES_TO_QUERY_PATTERN
  source_card_id: execution_constraint_set.jiomart.marketplace_query_constraints
  target_card_id: query_pattern.jiomart.settlement.8_4_tcs_reconciliation_oms_vs_settlement
  edge_class: canonical
  canonical_cognee_edge: true
  source_type: execution_constraint_set
  target_type: query_pattern
```


```yaml
candidate_edge:
  edge_id: edge.jiomart.v9.01010.applies_to_query_pattern
  canonical_edge_type: APPLIES_TO_QUERY_PATTERN
  source_card_id: execution_constraint_set.jiomart.marketplace_query_constraints
  target_card_id: query_pattern.jiomart.settlement.8_5_credit_debit_notes
  edge_class: canonical
  canonical_cognee_edge: true
  source_type: execution_constraint_set
  target_type: query_pattern
```


```yaml
candidate_edge:
  edge_id: edge.jiomart.v9.01011.applies_to_query_pattern
  canonical_edge_type: APPLIES_TO_QUERY_PATTERN
  source_card_id: execution_constraint_set.jiomart.marketplace_query_constraints
  target_card_id: query_pattern.jiomart.returns.7_1_return_volume_by_type
  edge_class: canonical
  canonical_cognee_edge: true
  source_type: execution_constraint_set
  target_type: query_pattern
```


```yaml
candidate_edge:
  edge_id: edge.jiomart.v9.01012.applies_to_query_pattern
  canonical_edge_type: APPLIES_TO_QUERY_PATTERN
  source_card_id: execution_constraint_set.jiomart.marketplace_query_constraints
  target_card_id: query_pattern.jiomart.returns.7_2_return_cycle_time_rto_turnaround
  edge_class: canonical
  canonical_cognee_edge: true
  source_type: execution_constraint_set
  target_type: query_pattern
```


```yaml
candidate_edge:
  edge_id: edge.jiomart.v9.01013.applies_to_query_pattern
  canonical_edge_type: APPLIES_TO_QUERY_PATTERN
  source_card_id: execution_constraint_set.jiomart.marketplace_query_constraints
  target_card_id: query_pattern.jiomart.returns.7_3_returns_oms_reconciliation
  edge_class: canonical
  canonical_cognee_edge: true
  source_type: execution_constraint_set
  target_type: query_pattern
```


```yaml
candidate_edge:
  edge_id: edge.jiomart.v9.01014.applies_to_query_pattern
  canonical_edge_type: APPLIES_TO_QUERY_PATTERN
  source_card_id: execution_constraint_set.jiomart.marketplace_query_constraints
  target_card_id: query_pattern.jiomart.returns.7_4_sku_level_return_rate
  edge_class: canonical
  canonical_cognee_edge: true
  source_type: execution_constraint_set
  target_type: query_pattern
```


```yaml
candidate_edge:
  edge_id: edge.jiomart.v9.01015.applies_to_query_pattern
  canonical_edge_type: APPLIES_TO_QUERY_PATTERN
  source_card_id: execution_constraint_set.jiomart.marketplace_query_constraints
  target_card_id: query_pattern.jiomart.oms.7_1_monthly_gmv_clean_rows_only
  edge_class: canonical
  canonical_cognee_edge: true
  source_type: execution_constraint_set
  target_type: query_pattern
```


```yaml
candidate_edge:
  edge_id: edge.jiomart.v9.01016.applies_to_query_pattern
  canonical_edge_type: APPLIES_TO_QUERY_PATTERN
  source_card_id: execution_constraint_set.jiomart.marketplace_query_constraints
  target_card_id: query_pattern.jiomart.oms.7_2_clean_forward_orders_exclude_column_shifted_rows
  edge_class: canonical
  canonical_cognee_edge: true
  source_type: execution_constraint_set
  target_type: query_pattern
```


```yaml
candidate_edge:
  edge_id: edge.jiomart.v9.01017.applies_to_query_pattern
  canonical_edge_type: APPLIES_TO_QUERY_PATTERN
  source_card_id: execution_constraint_set.jiomart.marketplace_query_constraints
  target_card_id: query_pattern.jiomart.oms.7_3_intra_state_vs_inter_state_gst_analysis
  edge_class: canonical
  canonical_cognee_edge: true
  source_type: execution_constraint_set
  target_type: query_pattern
```


```yaml
candidate_edge:
  edge_id: edge.jiomart.v9.01018.applies_to_query_pattern
  canonical_edge_type: APPLIES_TO_QUERY_PATTERN
  source_card_id: execution_constraint_set.jiomart.marketplace_query_constraints
  target_card_id: query_pattern.jiomart.oms.7_4_sku_level_performance
  edge_class: canonical
  canonical_cognee_edge: true
  source_type: execution_constraint_set
  target_type: query_pattern
```


```yaml
candidate_edge:
  edge_id: edge.jiomart.v9.01019.applies_to_query_pattern
  canonical_edge_type: APPLIES_TO_QUERY_PATTERN
  source_card_id: execution_constraint_set.jiomart.marketplace_query_constraints
  target_card_id: query_pattern.jiomart.oms.7_5_oms_settlement_join
  edge_class: canonical
  canonical_cognee_edge: true
  source_type: execution_constraint_set
  target_type: query_pattern
```


```yaml
candidate_edge:
  edge_id: edge.jiomart.v9.01020.applies_to_query_pattern
  canonical_edge_type: APPLIES_TO_QUERY_PATTERN
  source_card_id: execution_constraint_set.jiomart.marketplace_query_constraints
  target_card_id: query_pattern.jiomart.oms.7_6_return_rate
  edge_class: canonical
  canonical_cognee_edge: true
  source_type: execution_constraint_set
  target_type: query_pattern
```


## 7. Parser QA Summary

```yaml
parser_quality_manifest:
  candidate_cards: 384
  candidate_edges: 1020
  source_evidence_count: 126
  sql_patterns: 29
  review_items: 5
  open_reviews: 5
  missing_edge_references: 0
  dangling_sql_refs: 0
  missing_evidence_refs: 0
  deleted_card_references: 0
  isolated_cards: 0
  lazy_workflow_steps: 0
  placeholder_metric_formulas: 0
  unsupported_metric_implementations: 0
  process_variants_review_required: 0
  state_transitions_without_state_column: 0
  unresolved_benchmark_reviews_without_reason: 0
  hard_threshold_benchmarks_without_rule: 0
  forbidden_scope_cards_from_scope_ids: 0
  raw_source_sha256: a36b68fa208f6753c02e6f975ad1f3785f89402a939b78b881ff3fec72384ca1
  raw_source_line_count: 1232
```

## 8. Source Capture Appendix — Full DOCX Text

The cleaned DOCX source text below is retained so every source fact remains auditable even when not materialized as a canonical marketplace card.

````markdown
Tab 1
# JioMart Marketplace— Business Knowledge Base
## 1. JioMart Marketplace Overview
### 1.1 Background
JioMart is an Indian e-commerce marketplace launched in **May 2020** by **Reliance Retail**, a subsidiary of Reliance Industries Limited. It started as a grocery/FMCG delivery platform leveraging Reliance's network of JioMart Partner kirana stores and Reliance Fresh outlets, and has since expanded into electronics, fashion, personal care, home, and food.
**Key characteristics:**
* **Phygital O2O model:** Combines offline Reliance retail stores with digital ordering (app, website, WhatsApp)
* **Local fulfilment:** Orders dispatched from nearby Reliance stores/warehouses for faster delivery
* **Zero onboarding fees:** Free registration for sellers
* **Category-based commission:** Referral fee varies by product category
* **Backed by Reliance Retail** — India's largest retailer by revenue
### 1.2 Seller Portal
Seller registration and management via `seller.jiomart.com`. Documents required: GSTIN (mandatory), PAN, bank account, business proof.
### 1.3 Seller Entities in Dataset
| group_level_id | Entity | Brand | Products | Tables |
|----------------|--------|-------|----------|--------|
| 26             | TANVI Fitness Pvt Ltd | MYFITNESS | Peanut butter, oats, nutrition | jiomart_oms, jiomart_returns, jiomart_settlement |
| 221            | ARDEUR FASHIONS | CODEZ, ARDEUR | Boys' apparel, men's clothing | jiomart_shipment |
### 1.4 MYFITNESS Products (Primary Seller — group 26)
| SKU ID | Product | HSN | GST |
|--------|---------|-----|-----|
| `C5102_1` | MYFITNESS Choc Peanut Butter Crunchy 510g | 20081100 | 5%  |
| `C22703` | MYFITNESS Choc PB Crispy | 20081100 | 5%  |
| `C12502_1` | MYFITNESS Choc PB 1.25kg | 20081100 | 5%  |
| `N5101` | MYFITNESS Natural PB Smooth 510g | 20081100 | 5%  |
| `O12502_1` | MYFITNESS Original Crunchy PB 1.25kg | 20081100 | 5%  |
| Various | MYFITNESS Rolled Oats | 11041200 | 5%  |
| Various | MYFITNESS Dark Choc Oats / Combos | 18069030 / 21069099 | 12–18% |
### 1.5 Multi-State GSTIN Registration (TANVI Fitness)
| GSTIN | State | Warehouse / Fulfilment Centre |
|-------|-------|-------------------------------|
| `29AAHCT1518N1ZW` | Karnataka | Central BLR Warehouse 560083 (Bangalore) |
| `27AAHCT1518N1Z0` | Maharashtra | Central MH Warehouse 421302   |
| `06AAHCT1518N1Z4` | Haryana | Central GGN Warehouse 122503 (Gurgaon) |
---
## 2. JioMart Business Model & Fee Structure
### 2.1 JioMart's Revenue Sources from Sellers
JioMart follows a category-based commission model, with a fixed fee charged on every successful order, shipping charges based on weight and delivery zone, and a payment processing fee of approximately 2% per transaction.
**Fee components (from research + data validation):**
| Fee Type | Description | How Charged |
|----------|-------------|-------------|
| Referral / Commission fee | % of selling price, category-based | Per sale, deducted in settlement |
| Fixed fee | Flat per-order charge (₹10–₹50) | Per order   |
| Shipping fee | Weight + zone based | Via logistics partner |
| Payment processing fee | \~2% per transaction | Per order   |
| Closing fee | Currently zero | N/A         |
> **Note:** In the current dataset, there are **no explicit commission deductions** visible in `jiomart_settlement` (unlike Amazon/Snapdeal which have dedicated commission rows). JioMart may net the commission into the `Receivable` amount — the `settled_amount` in `Receivable` rows represents post-commission payout.
### 2.2 Fulfilment Models
Sellers have two fulfilment choices: Self-Fulfilment (seller manages own inventory and logistics) and Warehouse Fulfilment (seller ships stock to JioMart warehouse, JioMart packs and delivers).
**In the dataset:**
* `Third Party Platform Shipment` (jiomart_oms): MYFITNESS self-fulfils from own warehouses via 3rd-party couriers
* `Direct Shipment` (jiomart_shipment): ARDEUR FASHIONS ships directly to buyers
### 2.3 Payment Settlement Cycle
Payments are paid directly to the seller's registered bank account after successful delivery, following the specified settlement cycle.
From the data: settlement dates are daily — every delivery day generates settlement rows, suggesting near-real-time settlement processing (typically 7-day hold after delivery for returns window).
---
## 3. Transaction Lifecycle
### 3.1 Forward Order Flow
~~~
Customer places order on JioMart (app/website/WhatsApp)
        ↓
Order created → appears in jiomart_oms
(transaction_type = 'forward', order_status = 'invoiced')
        ↓
Seller picks and packs from nearest warehouse
(GSTIN determined by dispatch state)
        ↓
Courier picks up
(order_status = 'pick_up_confirmed')
        ↓
Product Delivered
(order_status = 'delivered')
        ↓
7-day return window
        ↓
Settlement generated → jiomart_settlement
(event = 'Invoice', accountable_type = 'Receivable' / 'BaseTcs' / 'Tds')
        ↓
Payout to seller bank account
~~~
### 3.2 RTO (Return-to-Origin) Flow
~~~
Delivery attempt fails (buyer unavailable / wrong address / refusal)
        ↓
Courier marks as undeliverable
        ↓
In jiomart_oms: order_status = 'shipment_returned'
In jiomart_returns: transaction_type = 'ReturnToOrigin'
        ↓
Courier returns package to origin warehouse
(return_delivery_date in jiomart_returns)
        ↓
Settlement reversed → jiomart_settlement
(event = 'Return', accountable_type = 'Receivable' — negative)
        ↓
TCS reversed: BaseTcs entry with positive settled_amount
~~~
### 3.3 Doorstep Return Flow
~~~
Buyer receives item but refuses on delivery
(open-box check, wrong item, visible damage)
        ↓
jiomart_returns: transaction_type = 'DoorStepReturn'
        ↓
Courier takes item back immediately
        ↓
Full refund to buyer
Settlement reversed in jiomart_settlement
~~~
### 3.4 Pre-Shipment Cancellation Flow
~~~
Buyer or seller cancels order before dispatch
        ↓
jiomart_returns: transaction_type = 'BeforeShippingReturn'
        ↓
No shipping cost incurred
No courier movement
Refund processed immediately
~~~
---
## 4. Entity Relationships Across Tables
### 4.1 Entity Map
~~~
jiomart_oms (group_level_id = 26, MYFITNESS)
  order_id  ←──────────────────────────→  order_id   jiomart_settlement
  order_id  ←──────────────────────────→  order_id   jiomart_returns
  invoice_number ←──────────────────→  invoice_number  jiomart_settlement
jiomart_shipment (group_level_id = 221, ARDEUR)
  ← NO JOIN to other 3 tables → (separate seller entity)
~~~
### 4.2 Primary Join Keys
| Join | Left Table | Right Table | Key | Coverage |
|------|------------|-------------|-----|----------|
| OMS → Settlement | jiomart_oms | jiomart_settlement | `order_id` | 56,733 / 57,677 = **98.4%** |
| OMS → Returns | jiomart_oms | jiomart_returns | `order_id` | 8,018 / 8,367 = **95.8%** |
| Settlement → Returns | jiomart_settlement | jiomart_returns | `order_id` | —        |
| OMS → Settlement (invoice) | jiomart_oms | jiomart_settlement | `invoice_number` | Lower (format differs) |
> **Warning:** `jiomart_shipment.order_id` has **0% match** with `jiomart_oms.order_id` — completely separate entity (`group_level_id = 221` vs `26`).
---
## 5. GST / Tax Framework
### 5.1 Product GST on Sales
| Condition | Tax Type | Rate |
|-----------|----------|------|
| Source state ≠ Destination state | IGST     | 5% (peanut butter / oats), 12–18% (combos) |
| Source state = Destination state | CGST + SGST | 2.5% each (5% total) |
**Observed in data:**
* \~95% of orders are inter-state → IGST applied
* Intra-state orders (Karnataka→Karnataka) → CGST 2.5% + SGST 2.5%
### 5.2 HSN and GST Rates
| HSN | Description | IGST Rate |
|-----|-------------|-----------|
| `20081100` | Peanut butter — prepared/preserved nuts | **5%**    |
| `11041200` | Rolled oats (cereal grain) | **5%**    |
| `18069030` | Chocolate food preparations | **18%**   |
| `21069099` | Food preparations not elsewhere classified | **18%**   |
### 5.3 TCS (Tax Collected at Source — GST § 52)
* **Rate:** Predominantly `0.0001` (0.01%) in data — this is TCS IGST rate per transaction
* **Deducted by:** JioMart (as e-commerce operator)
* **Credited to:** Seller's GST ledger via GSTR-2A
* **In data:** `jiomart_oms.total_tcs_amount` and `jiomart_settlement.BaseTcs` rows
* **Total TCS deducted (2025):** ₹64,852 (OMS) / ₹32,583 (settlement Invoice rows)
### 5.4 TDS (Tax Deducted at Source — Income Tax § 194-O)
* **Rate:** **0.1%** (confirmed from `tds_194o_rate = 0.1000`)
* **Deducted by:** JioMart (as e-commerce operator)
* **Credited to:** Seller via Form 26AS (annual IT return)
* **In data:** `jiomart_oms.total_tds` and `jiomart_settlement.Tds` rows
* **Total TDS deducted (2025):** ₹15,010 (OMS) / ₹6,515 (settlement Invoice rows)
* **Not applicable on:** `reverse` / return transactions (`total_tds = 0` for reverse OMS rows)
---
## 6. Key Business Metrics (with SQL)
### 6.1 Total GMV
~~~sql
SELECT
  SUM(CASE WHEN transaction_type = 'forward' THEN charged_amount ELSE 0 END) AS forward_gmv,
  SUM(CASE WHEN transaction_type = 'reverse' THEN ABS(charged_amount) ELSE 0 END) AS reversed_gmv,
  SUM(charged_amount) AS net_gmv
FROM zs_observe.jiomart_oms
WHERE is_active = true;
-- Forward GMV: ~₹1.63 Cr | Reversed: ~₹22.4L | Net: ~₹1.40 Cr
~~~
### 6.2 Return Rate
~~~sql
SELECT
  ROUND(100.0 * COUNT_IF(order_status = 'shipment_returned')
    / NULLIF(COUNT_IF(transaction_type = 'forward'), 0), 2) AS rto_rate_pct,
  ROUND(100.0 * COUNT_IF(transaction_type = 'reverse')
    / NULLIF(COUNT_IF(transaction_type = 'forward'), 0), 2) AS return_reversal_pct
FROM zs_observe.jiomart_oms
WHERE is_active = true;
-- RTO rate: ~14.8% | Return reversal rate: ~13.8%
~~~
### 6.3 Average Order Value (AOV)
~~~sql
SELECT AVG(charged_amount) AS aov
FROM zs_observe.jiomart_oms
WHERE is_active = true
  AND transaction_type = 'forward'
  AND order_status = 'delivered';
-- Observed: ₹273.83
~~~
### 6.4 Net Settled Revenue
~~~sql
SELECT
  SUM(CASE WHEN accountable_type = 'Receivable' THEN settled_amount ELSE 0 END) AS gross_receivable,
  SUM(CASE WHEN accountable_type = 'BaseTcs' THEN settled_amount ELSE 0 END) AS tcs_net,
  SUM(CASE WHEN accountable_type = 'Tds' THEN settled_amount ELSE 0 END) AS tds_net,
  SUM(settled_amount) AS net_settled
FROM zs_observe.jiomart_settlement
WHERE is_active = true AND event IS NOT NULL;
~~~
### 6.5 Seller Coupon Discount Impact
~~~sql
SELECT
  seller_coupon_code,
  COUNT(*) AS orders,
  SUM(ABS(COALESCE(CAST(seller_coupon_amount AS DOUBLE), 0))) AS total_discount
FROM zs_observe.jiomart_oms
WHERE is_active = true
  AND seller_coupon_code IS NOT NULL
GROUP BY seller_coupon_code
ORDER BY total_discount DESC;
~~~
### 6.6 Monthly Forward Orders and GMV
~~~sql
SELECT
  CAST(DATE_TRUNC('month', CAST(created_date AS TIMESTAMP)) AS DATE) AS month,
  COUNT(*) AS orders,
  SUM(charged_amount) AS gmv,
  AVG(charged_amount) AS aov
FROM zs_observe.jiomart_oms
WHERE is_active = true AND transaction_type = 'forward'
GROUP BY 1 ORDER BY 1;
~~~
---
## 7. Reconciliation Use Cases
### 7.1 OMS → Settlement Match (3-Way Per Order)
~~~sql
SELECT
  o.order_id,
  o.charged_amount AS oms_gmv,
  o.total_tcs_amount AS oms_tcs,
  o.total_tds AS oms_tds,
  SUM(CASE WHEN s.accountable_type = 'Receivable' THEN s.settled_amount ELSE 0 END) AS stl_receivable,
  SUM(CASE WHEN s.accountable_type = 'BaseTcs' THEN s.settled_amount ELSE 0 END) AS stl_tcs,
  SUM(CASE WHEN s.accountable_type = 'Tds' THEN s.settled_amount ELSE 0 END) AS stl_tds,
  ROUND(o.total_tcs_amount + SUM(CASE WHEN s.accountable_type='BaseTcs' THEN s.settled_amount ELSE 0 END), 4) AS tcs_variance
FROM zs_observe.jiomart_oms o
LEFT JOIN zs_observe.jiomart_settlement s
  ON o.order_id = s.order_id AND s.is_active = true AND s.event IS NOT NULL
WHERE o.is_active = true
  AND o.transaction_type = 'forward'
  AND o.order_status = 'delivered'
  AND o.hsn IS NOT NULL
GROUP BY o.order_id, o.charged_amount, o.total_tcs_amount, o.total_tds;
~~~
### 7.2 Returns → OMS → Settlement Full Chain
~~~sql
SELECT
  r.order_id,
  r.return_type,
  CAST(r.refund_amount AS DOUBLE) AS refund_issued,
  o.charged_amount AS original_sale,
  SUM(s.settled_amount) AS settlement_net
FROM zs_observe.jiomart_returns r
LEFT JOIN zs_observe.jiomart_oms o ON r.order_id = o.order_id AND o.is_active = true
LEFT JOIN zs_observe.jiomart_settlement s ON r.order_id = s.order_id AND s.is_active = true
WHERE r.is_active = true AND r.return_type IS NOT NULL
GROUP BY r.order_id, r.return_type, r.refund_amount, o.charged_amount;
~~~
### 7.3 Unreconciled OMS Orders (Not in Settlement)
~~~sql
SELECT o.order_id, o.invoice_number, o.charged_amount, o.order_status
FROM zs_observe.jiomart_oms o
LEFT JOIN zs_observe.jiomart_settlement s
  ON o.order_id = s.order_id AND s.is_active = true
WHERE o.is_active = true
  AND o.transaction_type = 'forward'
  AND o.order_status = 'delivered'
  AND o.hsn IS NOT NULL
  AND s.order_id IS NULL;
-- Coverage gap: ~944 orders (1.6%)
~~~
### 7.4 TCS Reconciliation
~~~sql
SELECT 'OMS TCS' AS source, SUM(total_tcs_amount) AS amount
FROM zs_observe.jiomart_oms WHERE is_active = true AND transaction_type = 'forward'
UNION ALL
SELECT 'Settlement BaseTcs (Forward)', SUM(settled_amount)
FROM zs_observe.jiomart_settlement
WHERE is_active = true AND accountable_type = 'BaseTcs' AND transaction_type = 'forward'
UNION ALL
SELECT 'Settlement BaseTcs (Return Reversal)', SUM(settled_amount)
FROM zs_observe.jiomart_settlement
WHERE is_active = true AND accountable_type = 'BaseTcs' AND transaction_type = 'reverse';
~~~
---
## 8. Data Quality Observations & Known Issues
| Issue | Table(s) | Detail | Mitigation |
|-------|----------|--------|------------|
| \~37,604 OMS rows with column shifting | jiomart_oms | Older format — fields in wrong columns | Filter `WHERE hsn IS NOT NULL AND order_date IS NOT NULL` |
| `group_level_id = 221` in shipment | jiomart_shipment | Completely different entity (ARDEUR FASHIONS) | Never cross-join shipment with oms/returns/settlement |
| `charged_amount`, `refund_amount` as varchar | jiomart_returns | Cannot aggregate directly | `CAST(charged_amount AS DOUBLE)` |
| Settlement invoice format differs from OMS | jiomart_settlement | OMS: `S29BZXSO7FA35884`, Settlement: `LBZXSO7-H8N7UYB` | Use `order_id` not `invoice_number` for OMS↔Settlement joins |
| Duplicate SKU entries in OMS | jiomart_oms | `C5102_1` with `sku=null` and with `sku='C5102_1'` | Use `sku_id` + `mp_sin` as combined key |
| `event` NULL for 112,872 settlement rows | jiomart_settlement | Older format | Use `event IS NOT NULL` for structured analysis; include NULL rows for total |
| `tcs_igst_rate = 0.5` anomaly | jiomart_oms | Likely data error — should be 0.005 | Flag rows where `tcs_igst_rate > 0.05` |
| `order_date` NULL in OMS for \~55.8% | jiomart_oms | Older format | Use `created_date` for all time-series |
| 48,784 inactive settlement rows | jiomart_settlement | Superseded records | Always `WHERE is_active = true` |
| Returns `reason` = mostly NULL | jiomart_returns | Return reason not captured | Cannot analyse return reasons from data |
---
## 9. Mandatory Query Filters
~~~sql
-- jiomart_oms, jiomart_returns, jiomart_settlement (group 26 — MYFITNESS)
WHERE is_active = true
  AND group_level_id = 26
-- jiomart_oms — additional filter for clean rows
  AND hsn IS NOT NULL   -- removes column-shifted older rows
-- jiomart_shipment (group 221 — ARDEUR FASHIONS)
WHERE is_active = true
  AND group_level_id = 221
  AND qty > 0   -- removes cancelled orders
~~~
---
## 10. Table Summary Reference
| Table | Entity | Active Rows | Date Range | Primary Key | Join Key | group_level_id |
|-------|--------|-------------|------------|-------------|----------|----------------|
| `jiomart_oms` | MYFITNESS / TANVI Fitness | 67,359      | Jan–Dec 2025 | `order_id` / `invoice_number` | `order_id` | 26             |
| `jiomart_returns` | MYFITNESS / TANVI Fitness | 8,367       | Jan–Dec 2025 | `order_id`  | `order_id` | 26             |
| `jiomart_settlement` | MYFITNESS / TANVI Fitness | 188,345     | Jan–Dec 2025 | `invoice_number` | `order_id` | 26             |
| `jiomart_shipment` | **ARDEUR FASHIONS** | 425         | Oct–Dec 2025 | `order_id`  | **No cross-join** | **221**        |
Tab 2
# Table : JioMart Shipment
**Schema:** `zs_observe`  **Table:** `jiomart_shipment`  **Last Updated:** April 2025  **Maintained By:** ZenStatement Data Team
---
## 1. Table Overview
`jiomart_shipment` is the **shipment report** for JioMart — a lightweight operational table recording the status of each dispatched order: MRP, charged amount, promotional discount, shipping date, and order status. Unlike `jiomart_oms` (MYFITNESS / group 26), this table belongs to a **completely different seller entity**.
**Critical distinction:**
* `group_level_id = 221` — **ARDEUR FASHIONS** (not TANVI Fitness / MYFITNESS)
* Seller name: `ARDEUR FASHIONS 641604`
* Products: CODEZ and ARDEUR brand apparel (boys' hoodies, shorts, T-shirts)
* Fulfilment: `Direct Shipment` (vs `Third Party Platform Shipment` in OMS)
* Data range: Oct–Dec 2025 only
This table has **0% join coverage** with the other 3 JioMart tables — it is a separate seller's data coexisting in the same schema under a different `group_level_id`.
---
## 2. Key Statistics
| Metric | Value |
|--------|-------|
| Total rows | 425   |
| Active rows (`is_active = true`) | 425 (100%) |
| **group_level_id** | **221** (ARDEUR FASHIONS — different from OMS/Returns/Settlement) |
| Date range (`created_date`) | 2025-10-01 → 2025-12-30 |
| Distinct SKUs | 242   |
| Distinct orders | 364   |
| Total GMV (`charged_amount`) | ₹1,04,477.71 |
| Total MRP | ₹6,69,514 |
| Avg charged amount | ₹245.83 |
| Total promotional discount | ₹5,64,553 (avg ₹1,328 off MRP per item) |
| Payment modes | COD, Prepaid |
| Fulfilment channel | Direct Shipment |
| Currency | INR (100%) |
---
## 3. Schema Details (29 Columns)
| Column | Type | Description |
|--------|------|-------------|
| `unique_id` | varchar | Row identifier |
| `txn_uuid` | varchar | Pipeline UUID |
| `unique_value` | varchar | Dedup hash  |
| `source_gst_name` | varchar | Seller name: `ARDEUR FASHIONS 641604` |
| `order_id` | varchar | JioMart order ID (format: `17592870447301320654J`) |
| `created_date` | timestamp | Order creation timestamp |
| `order_status` | varchar | `delivered`, `shipment_returned`, `canceled` |
| `qty`  | integer | Quantity    |
| `description` | varchar | Product description |
| `fulfillment_channel` | varchar | `Direct Shipment` |
| `sku_id` | varchar | Seller SKU (e.g., `ASSJ18-MSH-CHR-XL`, `CBOT001-RT1-15Y-P1`) |
| `mrp`  | decimal | Maximum Retail Price |
| `charged_amount` | decimal | Amount charged to buyer after discount |
| `item_promo_discount` | decimal | Promotional discount applied (MRP − charged) |
| `payment_mode` | varchar | `COD` or `Prepaid_Payments` |
| `shipping_date` | timestamp | Shipment dispatch date |
| `currency_type` | varchar | `INR`       |
| `is_active` | boolean | Always `true` |
| `group_level_id` | integer | `221`       |
| `zen_sheet_name` | varchar | Source sheet |
| `created_at` / `updated_at` | timestamp | Timestamps  |
---
## 4. Distinct Value Analysis
### `order_status` Distribution
| Status | Count | Meaning |
|--------|-------|---------|
| `delivered` | —     | Successfully delivered to buyer |
| `shipment_returned` | —     | RTO — courier returned to seller |
| `canceled` | —     | Order cancelled (qty = 0, charged = 0) |
### SKU Naming Convention (ARDEUR FASHIONS)
| Prefix | Brand | Example SKU |
|--------|-------|-------------|
| `ASSJ18-` / `AMSH-` | ARDEUR Mens | `ASSJ18-MSH-CHR-XL` |
| `CBOT-` / `CBHO-` / `CBSW-` / `CBHN-` | CODEZ Boys | `CBOT001-RT1-15Y-P1` |
| `AMJG-` | ARDEUR Mens Joggers | `AMJG1004-CH1-P1` |
### Promotional Discount Scale
MRP ranges from ₹999 to ₹1,999 per item; charged_amount is ₹149–₹299 — representing **70–87% discounts** from MRP. This is typical of deep-discount flash-sale positioning on JioMart's fashion category.
---
## 5. Sample Records
~~~
source_gst_name    : ARDEUR FASHIONS 641604
created_date       : 2025-10-01 02:50:45
order_id           : 17592870447301320654J
order_status       : delivered
qty                : 1
description        : Ardeur Mens Shorts — Casual Shorts — Logo printed — XL
sku_id             : ASSJ18-MSH-CHR-XL
mrp                : 999.00
charged_amount     : 149.00
item_promo_discount: 850.00    ← 85% discount
payment_mode       : Prepaid_Payments
shipping_date      : 2025-10-01 05:50:45
group_level_id     : 221
~~~
~~~
source_gst_name    : ARDEUR FASHIONS 641604
description        : CODEZ Boys Oversized Pure Cotton Drop Shoulder Tshirts
sku_id             : CBOT001-RT1-15Y-P1
mrp                : 1999.00
charged_amount     : 295.12
item_promo_discount: 1703.88   ← 85% discount
payment_mode       : COD
order_status       : shipment_returned
~~~
---
## 6. Data Quality Observations
| Issue | Detail |
|-------|--------|
| **Different entity from other tables** | `group_level_id = 221` vs `26` — never join with jiomart_oms/returns/settlement without entity filter |
| Cancelled orders have `qty = 0`, `charged_amount = 0` | Expected — filter `qty > 0` for active shipments |
| No GST / TCS / TDS columns | This table has no tax detail — it is an operational shipment report only |
| No invoice_number | Cannot join to settlement or OMS via invoice |
| Date range only Oct–Dec 2025 | New seller onboarded in October 2025 |
| 242 distinct SKUs for only 425 rows | Highly diversified SKU base for a small order volume — catalogue-heavy, sales-light |
---
## 7. Common Query Patterns
### 7.1 Shipment Status Summary
~~~sql
SELECT order_status,
  COUNT(*) AS cnt,
  SUM(charged_amount) AS gmv,
  SUM(mrp) AS total_mrp,
  SUM(item_promo_discount) AS total_discount,
  AVG(charged_amount) AS avg_selling_price,
  ROUND(100.0 * AVG(item_promo_discount) / NULLIF(AVG(mrp), 0), 2) AS avg_discount_pct
FROM zs_observe.jiomart_shipment
WHERE is_active = true
GROUP BY order_status;
~~~
### 7.2 Monthly GMV
~~~sql
SELECT
  CAST(DATE_TRUNC('month', CAST(created_date AS TIMESTAMP)) AS DATE) AS month,
  COUNT(*) AS shipments,
  SUM(charged_amount) AS gmv,
  SUM(item_promo_discount) AS promo_discount
FROM zs_observe.jiomart_shipment
WHERE is_active = true AND qty > 0
GROUP BY 1 ORDER BY 1;
~~~
### 7.3 Top SKUs
~~~sql
SELECT sku_id,
  COUNT(*) AS orders,
  SUM(charged_amount) AS gmv,
  AVG(charged_amount) AS avg_price,
  AVG(item_promo_discount) AS avg_discount
FROM zs_observe.jiomart_shipment
WHERE is_active = true AND qty > 0
GROUP BY sku_id
ORDER BY gmv DESC
LIMIT 20;
~~~
Tab 3
# Table : JioMart Settlement — Table Knowledge Base
**Schema:** `zs_observe`  **Table:** `jiomart_settlement`  **Last Updated:** April 2025  **Maintained By:** ZenStatement Data Team
---
## 1. Table Overview
`jiomart_settlement` is the **financial settlement ledger** for JioMart — recording every payout and deduction in the seller's account book. Unlike other marketplaces where settlement is a single row per order, JioMart uses an **event-based multi-row structure**: each order generates multiple settlement rows (Receivable, BaseTcs, Tds, CreditDebitNote entries), each representing a separate financial line in the seller payable account.
The `settled_amount` field represents the net impact of each row on the seller's balance — positive for credits (sale proceeds), negative for debits (TCS, TDS, returns).
**Seller entity:** TANVI Fitness Pvt Ltd / MYFITNESS (group_level_id = 26)
---
## 2. Key Statistics
| Metric | Value |
|--------|-------|
| Total rows | 237,129 |
| Active rows (`is_active = true`) | 188,345 |
| group_level_id | 26    |
| Date range (`settlement_date`) | 2025-01-01 → 2025-12-31 |
| Distinct orders | 56,844 |
| Distinct invoices | 188,345 |
| Total settled (net all rows) | ₹92,68,296 |
| Total amount | ₹41,55,119 |
| Forward Receivable settled | ₹73,01,196 |
| Forward TCS deducted | −₹32,583 |
| Forward TDS deducted | −₹6,515 |
| Return Receivable reversed | −₹11,41,636 |
| Return TCS reversed | +₹5,092 |
| Currency | INR (100%) |
| Account book | `Seller payable` (100%) |
---
## 3. Schema Details (40 Columns)
### 3.1 Identity Columns
| Column | Type | Description |
|--------|------|-------------|
| `unique_id` | varchar | Row identifier |
| `txn_uuid` | varchar | Pipeline UUID |
| `unique_value` | varchar | Dedup hash  |
| `invoice_number` | varchar | Settlement invoice reference — **join key to jiomart_oms** |
| `order_id` | varchar | JioMart order ID — **primary join key** |
| `item_id` | varchar | Line item ID |
| `parent_id` | varchar | Parent order reference |
| `other_id` | varchar | Alternate reference ID |
| `document_number` | varchar | Document reference (mostly NULL) |
| `shipment_number` | varchar | Shipment reference |
| `accountable_number` | varchar | Account line identifier |
| `number` | varchar | Internal sequence number |
| `unique_id_1` | varchar | Legacy unique ID |
### 3.2 Date Columns
| Column | Type | Description |
|--------|------|-------------|
| `settlement_date` | date | **Date of settlement** — primary date field |
| `created_at` | timestamp | Record creation timestamp |
| `created_at_1` | varchar | Legacy creation timestamp |
| `created_at_temp_old` | varchar | Migration column |
### 3.3 Financial Columns
| Column | Type | Description |
|--------|------|-------------|
| `settled_amount` | decimal | **Net financial impact on seller account** (positive = credit, negative = debit) |
| `amount` | decimal | Raw transaction amount (= settled_amount for rows with event) |
### 3.4 Classification Columns
| Column | Type | Description |
|--------|------|-------------|
| `transaction_type` | varchar | `forward`, `reverse`, `Credit Note`, `Debit Note`, `Service Invoice`, `Bill Tds Refund` |
| `event` | varchar | `Invoice`, `Return`, `Credit Note`, `Debit Note`, `Service Invoice` |
| `accountable_type` | varchar | `Receivable`, `BaseTcs`, `Tds`, `CreditDebitNote`, `Bill` |
| `account_book` | varchar | `Seller payable` (always) |
| `description` | varchar | Row description (= accountable_type for structured rows) |
### 3.5 System / Metadata
| Column | Type | Description |
|--------|------|-------------|
| `group_level_id` | integer | `26`        |
| `currency_type` | varchar | `INR`       |
| `is_active` | boolean | Filter `is_active = true` (188,345 of 237,129 active) |
| `is_duplicated` | boolean | Dedup flag  |
| `zen_status` | boolean | Pipeline flag |
| `sheetname` / `zen_sheet_name` | varchar | Source sheet |
| `ancestry` | varchar | Lineage     |
| `event_temp_old` | varchar | Legacy event field |
---
## 4. Settlement Structure — Event-Based Multi-Row Model
### How JioMart Settlement Works
For each delivered order, JioMart creates **3 settlement rows** in the payable ledger:
~~~
Order: 17623280767681770113J  (Delivered — ₹259 order value)
  Row 1: event=Invoice, accountable_type=Receivable  → settled_amount = +327.10  (avg)
  Row 2: event=Invoice, accountable_type=BaseTcs     → settled_amount = -1.46   (avg TCS)
  Row 3: event=Invoice, accountable_type=Tds         → settled_amount = -0.29   (avg TDS)
~~~
For return orders:
~~~
  Row 4: event=Return, accountable_type=Receivable   → settled_amount = -320.14  (avg)
  Row 5: event=Return, accountable_type=BaseTcs      → settled_amount = +1.43    (TCS reversal)
  Row 6: event=Return, accountable_type=Tds          → settled_amount = +0.28    (TDS reversal)
~~~
### Full Event / AccountableType Matrix
| Event | Transaction Type | Accountable Type | Count | Total Settled | Meaning |
|-------|------------------|------------------|-------|---------------|---------|
| `Invoice` | `forward`        | `Receivable`     | 22,321 | +₹73,01,196   | Sale proceeds |
| `Invoice` | `forward`        | `BaseTcs`        | 22,321 | −₹32,583      | TCS deducted |
| `Invoice` | `forward`        | `Tds`            | 22,321 | −₹6,515       | TDS deducted |
| `Return` | `reverse`        | `Receivable`     | 3,566 | −₹11,41,636   | Return reversal |
| `Return` | `reverse`        | `BaseTcs`        | 3,566 | +₹5,092       | TCS reversal on return |
| `Return` | `reverse`        | `Tds`            | 3,566 | +₹1,017       | TDS reversal on return |
| `Credit Note` | `Credit Note`    | `CreditDebitNote` | \~few | —             | JioMart credit to seller |
| `Debit Note` | `Debit Note`     | `CreditDebitNote` | \~few | —             | JioMart debit to seller |
| `Service Invoice` | `Service Invoice` | `Bill`           | \~few | —             | Platform service charges |
| NULL event | `forward`/`reverse` | NULL             | 112,872 | ₹86,27,812    | Older data format rows |
---
## 5. Financial Waterfall
~~~
Forward Invoice — Receivable (Sale Proceeds)    +₹73,01,196
  − BaseTcs (TCS Deducted)                       −₹32,583
  − Tds (TDS Deducted)                           −₹6,515
                                               ────────────
  Net Forward Settled                         +₹72,62,098
Return Reversals — Receivable (Refund)           −₹11,41,636
  + BaseTcs Reversal (TCS Refunded)              +₹5,092
  + Tds Reversal (TDS Refunded)                  +₹1,017
                                               ────────────
  Net Return Settled                           −₹11,35,527
Net Settlement (Invoice rows only)            ₹61,26,571
Total Net Settlement (all active rows)        ₹92,68,296
~~~
---
## 6. Sample Records
~~~
invoice_number     : LBZXSO7-H8N7UYB
settlement_date    : 2025-09-06
transaction_type   : forward
event              : Invoice
accountable_type   : BaseTcs
account_book       : Seller payable
order_id           : 17571675512491986020J
item_id            : RBZXSO7-UZAGCZE
description        : BaseTcs
settled_amount     : -0.62    ← TCS deducted
amount             : -0.62
group_level_id     : 26
invoice_number     : LBZXSO7-EJPE5OG
settlement_date    : 2025-02-10
transaction_type   : reverse
event              : Return
accountable_type   : BaseTcs
order_id           : 17377996968821457796J
description        : BaseTcs
settled_amount     : +1.14    ← TCS reversed on return
~~~
---
## 7. Data Quality Observations
| Issue | Detail | Mitigation |
|-------|--------|------------|
| 48,784 inactive rows (237,129 − 188,345) | Superseded records | Always `WHERE is_active = true` |
| `event` NULL for 112,872 rows | Older data format — no event classification | Use `NULL event` rows for total settlement; filter `event IS NOT NULL` for structured analysis |
| `amount` NULL for 112,872 rows | Same older format | Use `settled_amount` as the reliable financial field |
| `document_number` mostly NULL | Not consistently sourced | Use `invoice_number` and `order_id` for joins |
| 3 rows per order (for structured event rows) | Multi-row model — summing `settled_amount` by `order_id` gives net | `GROUP BY order_id, SUM(settled_amount)` for per-order net |
| `item_id` NULL for return rows | Return reversals may not have item-level detail | Join on `order_id` only for returns |
| Invoice number format varies | `LBZXSO7-H8N7UYB` (settlement) vs `S29BZXSO7FA35884` (OMS) | Use `order_id` not `invoice_number` for OMS ↔ Settlement joins |
---
## 8. Common Query Patterns
### 8.1 Net Settlement per Order (Structured Rows)
~~~sql
SELECT
  order_id,
  SUM(CASE WHEN accountable_type = 'Receivable' THEN settled_amount ELSE 0 END) AS sale_proceeds,
  SUM(CASE WHEN accountable_type = 'BaseTcs' THEN settled_amount ELSE 0 END) AS tcs_impact,
  SUM(CASE WHEN accountable_type = 'Tds' THEN settled_amount ELSE 0 END) AS tds_impact,
  SUM(settled_amount) AS net_settled
FROM zs_observe.jiomart_settlement
WHERE is_active = true AND event IS NOT NULL
GROUP BY order_id
ORDER BY net_settled DESC
LIMIT 20;
~~~
### 8.2 Monthly Settlement Summary
~~~sql
SELECT
  DATE_TRUNC('month', settlement_date) AS month,
  transaction_type,
  accountable_type,
  COUNT(*) AS rows,
  SUM(settled_amount) AS total_settled
FROM zs_observe.jiomart_settlement
WHERE is_active = true AND event IS NOT NULL
GROUP BY 1, 2, 3
ORDER BY 1, 2, 3;
~~~
### 8.3 Settlement ↔ OMS Reconciliation
~~~sql
SELECT
  o.order_id,
  o.charged_amount AS oms_gmv,
  o.total_tcs_amount AS oms_tcs,
  o.total_tds AS oms_tds,
  SUM(CASE WHEN s.accountable_type = 'Receivable' THEN s.settled_amount ELSE 0 END) AS settled_receivable,
  SUM(CASE WHEN s.accountable_type = 'BaseTcs' THEN s.settled_amount ELSE 0 END) AS settled_tcs,
  SUM(CASE WHEN s.accountable_type = 'Tds' THEN s.settled_amount ELSE 0 END) AS settled_tds,
  CASE WHEN SUM(s.settled_amount) IS NULL THEN 'Not in Settlement' ELSE 'Matched' END AS status
FROM zs_observe.jiomart_oms o
LEFT JOIN zs_observe.jiomart_settlement s
  ON o.order_id = s.order_id
  AND s.is_active = true
  AND s.event IS NOT NULL
WHERE o.is_active = true
  AND o.transaction_type = 'forward'
  AND o.order_status = 'delivered'
  AND o.hsn IS NOT NULL
GROUP BY o.order_id, o.charged_amount, o.total_tcs_amount, o.total_tds;
~~~
### 8.4 TCS Reconciliation (OMS vs Settlement)
~~~sql
SELECT
  'OMS TCS' AS source, SUM(total_tcs_amount) AS total
FROM zs_observe.jiomart_oms WHERE is_active = true AND transaction_type = 'forward'
UNION ALL
SELECT 'Settlement BaseTcs', SUM(settled_amount)
FROM zs_observe.jiomart_settlement
WHERE is_active = true AND accountable_type = 'BaseTcs' AND transaction_type = 'forward';
~~~
### 8.5 Credit / Debit Notes
~~~sql
SELECT
  transaction_type, event, accountable_type,
  COUNT(*) AS cnt,
  SUM(settled_amount) AS total
FROM zs_observe.jiomart_settlement
WHERE is_active = true
  AND transaction_type IN ('Credit Note', 'Debit Note', 'Service Invoice', 'Bill Tds Refund')
GROUP BY 1, 2, 3;
~~~
Tab 4
# Table: JioMart Returns — Table Knowledge Base
**Schema:** `zs_observe`  **Table:** `jiomart_returns`  **Last Updated:** April 2025  **Maintained By:** ZenStatement Data Team
---
## 1. Table Overview
`jiomart_returns` is the **return tracking and management table** for JioMart. It records every return event at the order level — capturing the return type (RTO, doorstep, pre-shipment), courier AWB, fulfilment centre, refund amount, and timeline (initiation, delivery back to seller). It is the operational complement to `jiomart_oms`'s `reverse` transaction type, providing richer return-journey detail.
**Seller entity:** TANVI Fitness Pvt Ltd / MYFITNESS (group_level_id = 26)\n**Couriers used:** Delhivery, Shadowfax, Xpressbees Express
---
## 2. Key Statistics
| Metric | Value |
|--------|-------|
| Total rows | 8,367 |
| Active rows (`is_active = true`) | 8,367 (100%) |
| group_level_id | 26    |
| Date range (`created_date`) | 2025-01-16 → 2025-12-31 |
| Distinct orders | 8,018 |
| Distinct SKUs | 38    |
| Total charged (original sale value) | ₹28,45,973 |
| Total refund issued | ₹11,80,938 |
| Return types | 3     |
| Couriers | 3     |
| Payment modes | COD, Prepaid |
| Currency | INR (100%) |
---
## 3. Schema Details (53 Columns)
### 3.1 Identity Columns
| Column | Type | Description |
|--------|------|-------------|
| `unique_id` | varchar | Row identifier |
| `txn_uuid` | varchar | Pipeline UUID |
| `unique_value` | varchar | Dedup hash  |
| `invoice_number` | varchar | JioMart invoice number — **join key to jiomart_oms** |
| `order_id` | varchar | Order ID — join key to oms and settlement |
| `item_id` | varchar | Line item ID |
| `sku_id` | varchar | Seller SKU code |
| `sku`  | varchar | SKU alternate |
| `ean`  | varchar | EAN barcode |
| `forward_shipment_no` | varchar | Forward AWB / shipment number |
| `return_awb_number` | varchar | Return AWB number (courier tracking) |
| `return_awb_no` | varchar | Return AWB alternate field |
| `return_shipment_no` | varchar | Return shipment number |
### 3.2 Date Columns
| Column | Type | Description |
|--------|------|-------------|
| `created_date` | timestamp | Record creation timestamp |
| `order_date` | varchar | Original order date |
| `return_initiate_date` | varchar | Date return was initiated by buyer |
| `return_date` | timestamp | Return date (JioMart system) |
| `return_delivery_date` | varchar | Date return was delivered back to seller |
| `forward_delivery_date` | varchar | Original delivery date to buyer |
### 3.3 Financial Columns
| Column | Type | Description |
|--------|------|-------------|
| `charged_amount` | varchar | Original sale value — **stored as varchar; cast to DOUBLE** |
| `refund_amount` | varchar | Refund issued to buyer — **stored as varchar; cast to DOUBLE** |
| `invoice_amount` | varchar | Invoice amount — stored as varchar |
| `pre_delivery_claims` | varchar | Claims before delivery (mostly NULL) |
| `post_delivery_claims` | varchar | Post-delivery claim status (`Closed`) |
### 3.4 Classification Columns
| Column | Type | Description |
|--------|------|-------------|
| `transaction_type` | varchar | `ReturnToOrigin`, `DoorStepReturn`, `BeforeShippingReturn` |
| `return_type` | varchar | Same as `transaction_type` |
| `return_status` | varchar | `complete`, `init` |
| `order_status` | varchar | `complete`, `init` |
| `payment_mode` | varchar | `COD`, `Prepaid_Payments` |
| `payment_method` | varchar | `Prepaid_Payments`, `COD` |
| `reason` | varchar | Return reason (mostly NULL) |
| `quantity` / `qty` | varchar/integer | Quantity returned |
### 3.5 Logistics Columns
| Column | Type | Description |
|--------|------|-------------|
| `courier_partner` | varchar | `Delhivery`, `Shadowfax`, `Xpressbees Express` |
| `fulfillment_channel` | varchar | Channel used |
| `fulfillment_center` | varchar | JioMart fulfilment centre (e.g., `Central BLR Warehouse 560083`) |
| `description` | varchar | Product description |
| `product_title` | varchar | Product title |
### 3.6 System / Metadata
| Column | Type | Description |
|--------|------|-------------|
| `group_level_id` | integer | `26`        |
| `currency_type` | varchar | `INR`       |
| `is_active` | boolean | Always `true` |
| `zen_sheet_name` | varchar | Source sheet |
| `ancestry` | varchar | Lineage     |
---
## 4. Distinct Value Analysis
### `return_type` / `transaction_type` Distribution
| Return Type | Count | Total Charged | Total Refund | Couriers |
|-------------|-------|---------------|--------------|----------|
| NULL (older format) | 5,178 | ₹16,41,971    | NULL         | NULL     |
| `ReturnToOrigin` | 2,136 | ₹7,88,114     | ₹7,70,986    | Delhivery, Shadowfax, Xpressbees |
| `DoorStepReturn` | 407   | ₹1,43,127     | ₹1,42,122    | Delhivery, Shadowfax |
| `BeforeShippingReturn` | 374   | ₹1,39,881     | ₹1,34,949    | None (never shipped) |
### Return Type Meanings
| Type | Meaning | When It Occurs |
|------|---------|----------------|
| `ReturnToOrigin` | Courier attempted delivery but could not deliver; shipment returned to origin warehouse | Buyer unavailable, wrong address, refused delivery |
| `DoorStepReturn` | Buyer received item but initiates return at time of delivery (refuses on doorstep) | Open-box rejection, wrong item |
| `BeforeShippingReturn` | Order cancelled before shipping; never dispatched | Buyer cancellation, seller cancellation |
### `payment_mode`
| Value | Meaning |
|-------|---------|
| `COD` | Cash on Delivery — full refund to buyer |
| `Prepaid_Payments` | Prepaid — refund to source payment method |
### Couriers
| Courier | AWB Format Example |
|---------|--------------------|
| `Shadowfax` | `SF1897330411JIM`  |
| `Delhivery` | `115761160539141`  |
| `Xpressbees Express` | `14591751654159`   |
### Fulfilment Centres
| Centre | Pincode | State |
|--------|---------|-------|
| `Central BLR Warehouse 560083` | 560083  | Karnataka |
| `Central GGN Warehouse 122503` | 122503  | Haryana |
| `Central MH Warehouse 421302` | 421302  | Maharashtra |
---
## 5. Sample Records
**ReturnToOrigin (RTO):**
~~~
invoice_number         : S06BZXSO7FA07103
created_date           : 2025-07-18
order_date             : 2025-07-18
transaction_type       : ReturnToOrigin
order_id               : 17528121998411731690J
order_status           : complete
return_status          : complete
sku_id                 : N5101
quantity               : 1
product_title          : MyFitness Peanut Butter Natural Peanut Butter Smooth 510g
payment_mode           : Prepaid_Payments
charged_amount         : 256.00
refund_amount          : 256.00     ← full refund for RTO
return_awb_number      : SF1897330411JIM
return_initiate_date   : 2025-08-01
return_delivery_date   : 2025-08-07   ← 6 days to return to warehouse
courier_partner        : Shadowfax
fulfillment_center     : Central GGN Warehouse 122503
group_level_id         : 26
~~~
**DoorStepReturn:**
~~~
transaction_type       : DoorStepReturn
order_id               : 17537860557061965082J
payment_mode           : COD
charged_amount         : 239.00
refund_amount          : 239.00
courier_partner        : Shadowfax
return_awb_number      : SF1935001976JIM
~~~
---
## 6. Data Quality Observations
| Issue | Detail | Mitigation |
|-------|--------|------------|
| `charged_amount`, `refund_amount`, `invoice_amount` stored as varchar | Cannot aggregate directly | Use `SUM(CAST(charged_amount AS DOUBLE))` |
| `return_type` NULL for 5,178 rows (62%) | Older format — transaction_type is also NULL | Use `order_status = 'complete'` to identify closed returns |
| `order_date` stored as varchar | Date parsing required | `CAST(order_date AS TIMESTAMP)` |
| `return_initiate_date` and `return_delivery_date` stored as varchar | Not natively date-filterable | Cast before comparison |
| `reason` mostly NULL | Return reason not populated | Cannot analyse return reasons |
| `post_delivery_claims` = `'Closed'` | All closed claims observed — open claims may exist when data grows |            |
| `distinct_skus = 38` | Fewer SKUs than OMS — some SKUs may have no returns in current period |            |
---
## 7. Common Query Patterns
### 7.1 Return Volume by Type
~~~sql
SELECT
  COALESCE(return_type, 'Unknown/Old Format') AS return_type,
  return_status,
  COUNT(*) AS cnt,
  SUM(CAST(charged_amount AS DOUBLE)) AS total_charged,
  SUM(CAST(refund_amount AS DOUBLE)) AS total_refund
FROM zs_observe.jiomart_returns
WHERE is_active = true
GROUP BY 1, 2
ORDER BY cnt DESC;
~~~
### 7.2 Return Cycle Time (RTO Turnaround)
~~~sql
SELECT
  courier_partner,
  COUNT(*) AS returns,
  AVG(DATE_DIFF('day',
    CAST(return_initiate_date AS TIMESTAMP),
    CAST(return_delivery_date AS TIMESTAMP))) AS avg_days_to_warehouse
FROM zs_observe.jiomart_returns
WHERE is_active = true
  AND return_type = 'ReturnToOrigin'
  AND return_initiate_date IS NOT NULL
  AND return_delivery_date IS NOT NULL
GROUP BY courier_partner;
~~~
### 7.3 Returns → OMS Reconciliation
~~~sql
SELECT
  r.order_id, r.invoice_number,
  r.return_type,
  CAST(r.charged_amount AS DOUBLE) AS return_charged,
  CAST(r.refund_amount AS DOUBLE) AS refund,
  o.charged_amount AS oms_original_amount,
  o.order_status AS oms_status
FROM zs_observe.jiomart_returns r
LEFT JOIN zs_observe.jiomart_oms o
  ON r.order_id = o.order_id
  AND o.is_active = true
WHERE r.is_active = true;
~~~
### 7.4 SKU-Level Return Rate
~~~sql
SELECT
  r.sku_id,
  COUNT(*) AS returns,
  SUM(CAST(r.charged_amount AS DOUBLE)) AS returned_value
FROM zs_observe.jiomart_returns r
WHERE r.is_active = true
GROUP BY r.sku_id
ORDER BY returns DESC;
~~~
---
---
Tab 5
# Table: JioMart OMS — Table Knowledge Base
**Schema:** `zs_observe`  **Table:** `jiomart_oms`  **Last Updated:** April 2025  **Maintained By:** ZenStatement Data Team
---
## 1. Table Overview
`jiomart_oms` is the **Order Management System (OMS) table** for JioMart — the primary financial ledger capturing every sub-order item shipped or returned on the marketplace. It records the full invoice-level detail: charged amount, product GST (IGST / CGST / SGST), TCS (Tax Collected at Source under GST § 52), TDS (Income Tax § 194-O), order status, and logistics routing.
**Seller entity:** TANVI Fitness Pvt Ltd\n**Brand:** MYFITNESS (peanut butter, oats, nutrition products — 100% of data)\n**Fulfilment model:** Third Party Platform Shipment — seller-fulfilled from 3 owned warehouses
> **Critical data format note:** \~37,604 of 67,359 rows have **column shifting** (older ingestion format). In these rows, field values appear in the wrong columns — `source_state` may contain a warehouse code, `destination_state` may contain a state name, `charged_amount` may contain a description string. These rows have `order_date IS NULL`, `order_type IS NULL`, `sku IS NULL`, `taxable_value IS NULL`. Use `hsn IS NOT NULL` or `order_date IS NOT NULL` to filter to well-formed rows only (\~29,755 rows).
---
## 2. Key Statistics
| Metric | Value |
|--------|-------|
| Total rows | 67,359 |
| Active rows (`is_active = true`) | 67,359 (100%) |
| group_level_id | 26    |
| Date range (`created_date`) | 2025-01--01 → 2025-12-31 |
| Distinct orders | 57,677 |
| Distinct invoices | 64,458 |
| Distinct SKUs (`sku_id`) | 47    |
| Distinct HSN codes | 4     |
| Source states (warehouses) | 3 (Haryana, Karnataka, Maharashtra) |
| Destination states | 66    |
| Brand  | MYFITNESS (100%) |
| Seller GSTINs | 3     |
| Total GMV (`charged_amount`) | ₹1,40,34,661 |
| Total TCS deducted | ₹64,852.48 |
| Total TDS deducted | ₹15,010.44 |
| Total seller coupon discounts | −₹1,88,688 |
| Payment modes | COD, Prepaid |
| Currency | INR (100%) |
---
## 3. Schema Details (115 Columns)
### 3.1 Identity Columns
| Column | Type | Description |
|--------|------|-------------|
| `unique_id` | varchar | System row identifier |
| `txn_uuid` | varchar | Pipeline UUID |
| `unique_value` | varchar | Deduplication hash |
| `invoice_number` | varchar | JioMart seller invoice number (format: `S29BZXSO7FA35884`) |
| `original_invoice_id` | varchar | Original invoice reference |
| `buyer_invoice_id` | varchar | Buyer-facing invoice number |
| `order_id` | varchar | JioMart order ID (format: `17620898178181505759J`) |
| `item_id` | varchar | Line item ID |
| `order_item_id` | varchar | Order item ID (newer format) |
| `parent_id` | varchar | Parent order reference |
| `shipment_number` | varchar | Shipment tracking number (NULL for older rows) |
| `original_shipment_number` | varchar | Original shipment number |
| `mp_sin` | varchar | JioMart product SIN — catalogue identifier (e.g., `RVKBCGYVWK`) — **always populated** |
| `sku_id` | varchar | Seller SKU (e.g., `C5102_1`) |
| `sku`  | varchar | SKU alternate (NULL for \~37K older rows) |
| `fsn___product_id` | varchar | Platform product ID |
| `source_gst_id` | varchar | Seller GSTIN |
| `seller_gstin` | varchar | Seller GSTIN alternate |
### 3.2 Date Columns
| Column | Type | Description |
|--------|------|-------------|
| `created_date` | timestamp | Record creation timestamp — **primary reliable date** |
| `order_date` | timestamp | Order placement date (NULL for \~37K older rows) |
| `order_approval_date` | timestamp | Order approval |
| `buyer_invoice_date` | timestamp | Buyer invoice date |
| `sale_sale_reversal_tcs_date` | timestamp | TCS deduction date |
### 3.3 Financial Columns
| Column | Type | Description |
|--------|------|-------------|
| `charged_amount` | decimal | **Buyer-facing price inclusive of GST** — primary GMV field |
| `charged_amount_excluding_tax` | decimal | Taxable base (excluding GST) |
| `taxable_value` | decimal | Taxable value (NULL for older rows — same as `charged_amount_excluding_tax`) |
| `offer_price` | decimal | Platform offer price |
| `buyer_invoice_amount` | decimal | Final buyer invoice amount |
| `final_invoice_amount` | decimal | Final invoice amount |
| `seller_coupon_amount` | decimal | Seller-funded coupon discount (negative = deduction) |
### 3.4 Tax Columns
| Column | Type | Description |
|--------|------|-------------|
| `tax_igst_rate` | decimal | IGST rate: `0.0`, `0.05`, `0.12`, `0.18` |
| `tax_igst_amount` | decimal | IGST amount (inter-state orders) |
| `tax_cgst_rate` | decimal | CGST rate: `0.0`, `0.025`, `0.06`, `0.09` |
| `tax_cgst_amount` | decimal | CGST amount (intra-state orders) |
| `tax_sgst_rate` | decimal | SGST rate (mirrors CGST) |
| `tax_sgst_amount` | decimal | SGST amount |
| `type_of_tax` | varchar | `GST` — 100% |
| `hsn`  | varchar | HSN code — **primary field** |
| `hsn_code` | varchar | HSN code alternate (NULL for older rows) |
| `hsn_generated` | varchar | System-generated HSN |
| `igst_rate/amount` | decimal | Legacy IGST columns (older rows) |
| `cgst_rate/amount` | decimal | Legacy CGST columns |
| `sgst_rate/amount` | decimal | Legacy SGST columns |
### 3.5 TCS / TDS Columns
| Column | Type | Description |
|--------|------|-------------|
| `tcs_igst_rate` | decimal | TCS IGST rate (`0.0001`, `0.005`, `0.5`) |
| `tcs_cgst_rate` | decimal | TCS CGST rate (intra-state) |
| `tcs_sgst_rate` | decimal | TCS SGST rate |
| `total_tcs_amount` | decimal | **Total TCS deducted** (GST § 52) |
| `tcs_igst_amount` | decimal | TCS IGST component |
| `tcs_cgst_amount` | decimal | TCS CGST component |
| `tcs_sgst_amount` | decimal | TCS SGST component |
| `total_tcs_deducted` | decimal | TCS deducted (alternate field) |
| `total_tds` | decimal | **Total TDS** (Income Tax § 194-O) |
| `tds_194o_rate` | decimal | TDS rate: **0.1%** |
| `tds_194o_amount` | decimal | TDS 194-O amount |
### 3.6 Status Columns
| Column | Type | Description |
|--------|------|-------------|
| `transaction_type` | varchar | `forward` (sale) or `reverse` (return credit note) |
| `order_status` | varchar | `delivered`, `complete`, `shipment_returned`, `pick_up_confirmed`, `invoiced` |
| `order_type` | varchar | `COD` or `Prepaid` (NULL for older rows) |
| `event_type` / `event_sub_type` | varchar | Event classification |
| `fulfilment_channel` | varchar | `Third Party Platform Shipment` |
| `fulfillment_type` | varchar | Same as above (newer rows) |
| `is_active` | boolean | Always `true` |
| `is_duplicated` | boolean | Dedup flag  |
### 3.7 Geographic Columns
| Column | Type | Description |
|--------|------|-------------|
| `source_state` | varchar | Seller dispatch state (`HARYANA`, `KARNATAKA`, `MAHARASHTRA`) |
| `source_state_code` | varchar | State code  |
| `destination_state` | varchar | Buyer state (66 distinct) |
| `destination_state_code` | varchar | Destination state code |
| `destination_zipcode` | varchar | Buyer pincode |
| `order_billed_from` / `order_shipped_from` | varchar | Billing / shipping state |
| `customer_s_billing_state` | varchar | Customer billing state |
| `customer_s_delivery_state` | varchar | Customer delivery state |
### 3.8 Product / Fulfilment Columns
| Column | Type | Description |
|--------|------|-------------|
| `description` | varchar | Product description |
| `product_title_description` | varchar | Full product title |
| `quantity` / `item_quantity` | decimal | Quantity ordered |
| `fulfiller_name` | varchar | Fulfilment centre name |
### 3.9 System / Metadata
| Column | Type | Description |
|--------|------|-------------|
| `group_level_id` | integer | `26` — JioMart / MYFITNESS account |
| `brand` | varchar | `MYFITNESS` — always populated |
| `brand_ref_1` / `brand_ref_2` | varchar | Brand reference slugs |
| `seller_coupon_code` | varchar | Coupon code applied |
| `currency_type` | varchar | `INR`       |
| `zen_sheet_name` | varchar | Source sheet |
| `*_temp_old` | various | Legacy migration columns |
---
## 4. Distinct Value Analysis
### `transaction_type` / `order_status` Financial Breakdown
| Txn Type | Order Status | Count | GMV | Avg Price |
|----------|--------------|-------|-----|-----------|
| `forward` | `delivered`  | 49,438 | ₹1,35,37,477 | ₹273.83   |
| `forward` | `shipment_returned` | 8,703 | ₹24,28,933 | ₹279.09   |
| `reverse` | `complete`   | 8,067 | −₹22,38,885 | −₹277.54  |
| `forward` | `pick_up_confirmed` | 1,143 | ₹3,05,124 | ₹266.95   |
| `forward` | `invoiced`   | 8     | ₹2,013 | ₹251.57   |
> `shipment_returned` = courier RTO (undelivered shipment returned to seller).\n`reverse` = return credit note applied to a previously delivered order.
### Seller GSTINs → Warehouse Mapping
| GSTIN | State | Fulfilment Centre |
|-------|-------|-------------------|
| `29AAHCT1518N1ZW` | Karnataka | Central BLR Warehouse 560083 |
| `27AAHCT1518N1Z0` | Maharashtra | Central MH Warehouse 421302 |
| `06AAHCT1518N1Z4` | Haryana | Central GGN Warehouse 122503 |
### HSN Codes and Products
| HSN | Product | IGST Rate (Inter-state) | Count |
|-----|---------|-------------------------|-------|
| `20081100` | Peanut butter (prepared nuts) | 5%                      | \~66,391 |
| `18069030` | Chocolate combo products | \~12%                   | 474   |
| `11041200` | Rolled oats | 5%                      | 242   |
| `21069099` | Dark choc oats / whey products | \~12–18%                | 129   |
### Top SKUs by Volume
| SKU ID | Product | Orders (Forward) |
|--------|---------|------------------|
| `C5102_1` | MYFITNESS Choc Peanut Butter Crunchy 510g | \~26,464         |
| `C22703` | MYFITNESS Choc Peanut Butter Crispy | \~8,102          |
| `C12502_1` | MYFITNESS Choc Peanut Butter 1.25kg | \~3,248          |
| `N5101` | MYFITNESS Natural PB Smooth 510g | —                |
| `O12502_1` | MYFITNESS Original Crunchy PB 1.25kg | —                |
### Seller Coupon Codes Observed
`DHAMAKA50`, `FESTIVE50`, `JMNEW100`, `LOOT50`, `LOYAL100`, `MELA50`, `NEW100`, `NEWUSER3P`, `UTSAV50`, `WELCOME10`
### TCS Rates Observed
`0.0001` (0.01%) predominant, `0.005` (0.5%), `0.5` (50% — likely a data anomaly).\nTDS: uniformly `0.1%` where applied.
---
## 5. Sample Records
**Inter-state (IGST):**
~~~
invoice_number           : S29BZXSO7FA35813
created_date             : 2025-11-04 23:08:06
transaction_type         : forward
order_status             : delivered
order_id                 : 17622778855801261851J
item_id                  : 57998041
quantity                 : 2
description              : MYFITNESS Peanut Butter Chocolate Spread Crunchy 510g
sku_id                   : C5102_1
hsn                      : 20081100
source_state             : KARNATAKA
destination_state        : Jharkhand   ← inter-state
charged_amount           : 330.00
charged_amount_excl_tax  : 314.29
tax_igst_rate            : 0.05   ← 5% IGST
tax_igst_amount          : 15.71
tcs_igst_rate            : 0.0001
total_tcs_amount         : 1.57
total_tds                : 0.31
brand                    : MYFITNESS
group_level_id           : 26
~~~
**Intra-state (CGST + SGST):**
~~~
source_state             : KARNATAKA
destination_state        : Karnataka   ← same state
tax_igst_rate            : 0.0000   ← no IGST
tax_cgst_rate            : 0.0250   ← CGST applied
tax_cgst_amount          : 6.16
tax_sgst_rate            : 0.0250
tax_sgst_amount          : 6.16
~~~
---
## 6. Data Quality Observations
| Issue | Detail | Mitigation |
|-------|--------|------------|
| \~37,604 rows have column shifting | Older data format — values appear in wrong columns | Filter: `WHERE hsn IS NOT NULL AND order_date IS NOT NULL` |
| Duplicate SKU entries | `C5102_1` appears with `sku=null` and `sku='C5102_1'` — 2 data formats | Use `sku_id` as primary; de-duplicate if needed |
| `order_date` NULL for 55.8% of rows | Older format | Use `created_date` for all date-based analysis |
| `total_tds = 0` for `reverse` rows | Expected — TDS not deducted on return credit notes | Filter `transaction_type = 'forward'` for TDS totals |
| `tcs_igst_rate = 0.5` (anomaly) | Value is likely `0.005` (0.5%) in some rows — verify | Treat `tcs_igst_rate > 0.05` as suspect |
| Source state uppercase | `KARNATAKA` in source vs `Karnataka` in destination | Normalize with `UPPER()` for joins |
| Multiple HSN columns | `hsn`, `hsn_code`, `hsn_generated` | Use `hsn` as primary; `COALESCE(hsn, hsn_code, hsn_generated)` |
| `seller_coupon_amount` NULL | \~37K older rows | SUM with NULL handling: `SUM(COALESCE(seller_coupon_amount,0))` |
---
## 7. Common Query Patterns
### 7.1 Monthly GMV (Clean Rows Only)
~~~sql
SELECT
  CAST(DATE_TRUNC('month', CAST(created_date AS TIMESTAMP)) AS DATE) AS month,
  transaction_type,
  COUNT(*) AS orders,
  SUM(charged_amount) AS gmv,
  SUM(total_tcs_amount) AS tcs,
  SUM(total_tds) AS tds
FROM zs_observe.jiomart_oms
WHERE is_active = true
GROUP BY 1, 2
ORDER BY 1, 2;
~~~
### 7.2 Clean Forward Orders (Exclude Column-Shifted Rows)
~~~sql
SELECT *
FROM zs_observe.jiomart_oms
WHERE is_active = true
  AND transaction_type = 'forward'
  AND order_status = 'delivered'
  AND hsn IS NOT NULL;
~~~
### 7.3 Intra-State vs Inter-State GST Analysis
~~~sql
SELECT
  CASE
    WHEN UPPER(source_state) = UPPER(destination_state) THEN 'Intra-State'
    ELSE 'Inter-State'
  END AS gst_type,
  COUNT(*) AS cnt,
  SUM(charged_amount) AS gmv,
  SUM(tax_igst_amount) AS igst,
  SUM(tax_cgst_amount + tax_sgst_amount) AS cgst_sgst
FROM zs_observe.jiomart_oms
WHERE is_active = true
  AND transaction_type = 'forward'
  AND hsn IS NOT NULL
GROUP BY 1;
~~~
### 7.4 SKU-Level Performance
~~~sql
SELECT sku_id, mp_sin,
  COUNT(*) AS orders,
  SUM(charged_amount) AS gmv,
  AVG(charged_amount) AS avg_price,
  ROUND(100.0 * COUNT_IF(transaction_type = 'forward' AND order_status = 'shipment_returned')
    / NULLIF(COUNT_IF(transaction_type = 'forward'), 0), 2) AS rto_rate_pct
FROM zs_observe.jiomart_oms
WHERE is_active = true AND hsn IS NOT NULL
GROUP BY sku_id, mp_sin
ORDER BY gmv DESC;
~~~
### 7.5 OMS → Settlement Join
~~~sql
SELECT
  o.order_id, o.invoice_number,
  o.charged_amount AS oms_gmv,
  o.total_tcs_amount AS oms_tcs,
  s.settled_amount AS settlement_net,
  s.event, s.accountable_type
FROM zs_observe.jiomart_oms o
LEFT JOIN zs_observe.jiomart_settlement s
  ON o.order_id = s.order_id AND s.is_active = true
WHERE o.is_active = true
  AND o.transaction_type = 'forward'
  AND o.order_status = 'delivered'
  AND o.hsn IS NOT NULL;
~~~
### 7.6 Return Rate
~~~sql
SELECT
  ROUND(100.0 *
    COUNT_IF(order_status = 'shipment_returned')
    / NULLIF(COUNT_IF(transaction_type = 'forward'), 0), 2) AS rto_rate_pct,
  ROUND(100.0 *
    COUNT_IF(transaction_type = 'reverse')
    / NULLIF(COUNT_IF(transaction_type = 'forward'), 0), 2) AS return_reversal_rate_pct
FROM zs_observe.jiomart_oms
WHERE is_active = true;
~~~
````
