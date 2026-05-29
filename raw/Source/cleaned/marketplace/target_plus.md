# Target Plus Marketplace Clean Markdown — V9 Manifest-Refactored

```yaml
document_metadata:
  document_id: target_plus_marketplace_clean_md_v9_manifest_refactored
  vendor: Target Plus
  source_docx: /mnt/data/Target Plus Recon KB.docx
  source_md_previous: /mnt/data/target_plus_marketplace_clean_md_v8_unified_edges.md
  cleanup_manifest: /mnt/data/marketplace_cleanup_manifest_consolidated_v2.md
  generated_on: '2026-05-22'
  scope: marketplace_specific_clean_markdown_for_deterministic_parser
  marketplace_only: true
  do_not_skip_docx_information: true
  refactor_policy: source-backed, correctly typed, executable, and connected to the right semantic neighborhood
  preservation_policy: |-
    All marketplace-relevant DOCX information is preserved as evidence, candidate cards, SQL patterns, rules, reviews, caveats, query/output guidance, or raw source appendix. Out-of-scope means no forbidden card types, not content loss.
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
  - process_variant
  - state_transition
  removed_card_types:
  - state_transition
  - process_variant
  quality_summary:
    candidate_cards: 286
    candidate_edges: 802
    source_evidence_count: 144
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
    raw_source_sha256: 2fb29194e31f683d26544cdfedd1e744ac4903c74e6fe89015618d6d8b6050e8
    raw_source_line_count: 1718
```
## 0. Parser Instructions

This V9 refactor applies the consolidated marketplace cleanup manifest to the Target Plus marketplace source. It keeps Target Plus marketplace semantics, table schemas, SQL/query patterns, reconciliation logic, business processes, rules, caveats, and the raw DOCX capture, while removing or recasting lazy/non-executable cards from the prior V8 source.

Critical rules:

- Treat `group_level_id`, `group_id`, seller/entity values, Stripe transfer/payment/payout IDs, carrier tracking IDs, and brand/category labels as columns, filters, caveats, source evidence, or documented scope identifiers only.
- Use `item_id` for Sales ↔ Settlement and Returns ↔ Settlement matching, `order_id` for Sales ↔ Returns, and `tcin` for all product mapping enrichment. Do not assume transaction `sku_id` directly matches clean mapping `sku_id`.
- Preserve the Target Plus currency caveat: fields are labelled INR but source says the financial values are USD-priced; label outputs accordingly.
- Keep `reverse charge` separate from customer returns. It is a US marketplace-facilitator tax adjustment, with `total_tax = 0`, `gross_commission = 0`, and negative `settled_amount`.
- Use only SQL-backed metric implementations. Prose-only operational details are represented as business processes, rules, value profiles, or open reviews.
- `state_transition` and `process_variant` cards are intentionally omitted; source flow/status details are preserved in workflow steps and value profiles without unsupported state-machine edges.

## 1. Applied Manifest Refactor Decisions

```yaml
refactor_decision:
  source_card_or_pattern: V8 process_variant cards from payment/brand/fulfilment/status segments
  action: remove_or_recast
  resolution: Brand, seller, payment, fulfilment, and status labels are value profiles/rules/caveats unless the source gives a materially
    different sequence or matching logic.
```
```yaml
refactor_decision:
  source_card_or_pattern: V8 state_transition cards generated from flow-line ordering
  action: omit
  resolution: Workflow steps preserve Target-specific status/type fields. No state_transition cards are emitted because the source does
    not define a state-machine edge set.
```
```yaml
refactor_decision:
  source_card_or_pattern: Generic workflow lines such as customer places order / buyer initiates return
  action: replace_with_source_specific_steps
  resolution: |-
    Workflow steps now include target_sales, target_returns, target_settlement, transaction_type, internal_txn_type, order_status, item_id, payout_id, transfer_id, total_tax, and amount semantics.
```
```yaml
refactor_decision:
  source_card_or_pattern: Relationship overreach using SKU or weak joins
  action: recast
  resolution: TCIN is the mapping enrichment join. item_id and order_id joins follow the source join map and SQL. Direct sku_id matching
    is left as review because formats differ.
```
```yaml
refactor_decision:
  source_card_or_pattern: Duplicate settlement table section in DOCX
  action: deduplicate_cards_preserve_source
  resolution: Canonical cards are emitted once; duplicate source text remains in the raw source appendix and evidence line ranges.
```
```yaml
refactor_decision:
  source_card_or_pattern: US tax and Stripe/payment/bank references
  action: scope_guardrail
  resolution: Tax and Stripe values are represented as marketplace columns/rules/value profiles; no statutory filing, payment gateway,
    or bank-account cards are emitted.
```
## 2. Source Evidence Registry

```yaml
source_evidence:
  id: ev.target_plus.marketplace.target_plus_business_knowledge_base
  source_section: Target Plus — Business Knowledge Base
  source_context: marketplace
  source_line_start: 2
  source_line_end: 3
  evidence_type: prose
  supported_semantics:
  - Prose semantics from source section Target Plus — Business Knowledge Base.
  unsupported_semantics:
  - Do not infer tenant/group/platform-account/bank/payment-gateway/statutory-filing/external-logistics cards from this evidence.
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
  id: ev.target_plus.marketplace.1_target_plus_marketplace_overview
  source_section: 1. Target Plus Marketplace Overview
  source_context: marketplace
  source_line_start: 4
  source_line_end: 5
  evidence_type: prose
  supported_semantics:
  - Prose semantics from source section 1. Target Plus Marketplace Overview.
  unsupported_semantics:
  - Do not infer tenant/group/platform-account/bank/payment-gateway/statutory-filing/external-logistics cards from this evidence.
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
  id: ev.target_plus.marketplace.1_1_background
  source_section: 1.1 Background
  source_context: marketplace
  source_line_start: 6
  source_line_end: 20
  evidence_type: prose
  supported_semantics:
  - Prose semantics from source section 1.1 Background.
  unsupported_semantics:
  - Do not infer tenant/group/platform-account/bank/payment-gateway/statutory-filing/external-logistics cards from this evidence.
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
  id: ev.target_plus.marketplace.1_2_seller_eligibility
  source_section: 1.2 Seller Eligibility
  source_context: marketplace
  source_line_start: 21
  source_line_end: 24
  evidence_type: prose
  supported_semantics:
  - Prose semantics from source section 1.2 Seller Eligibility.
  unsupported_semantics:
  - Do not infer tenant/group/platform-account/bank/payment-gateway/statutory-filing/external-logistics cards from this evidence.
  - Seller, brand, Stripe, bank, or carrier mentions remain columns, value profiles, rules, caveats, or raw evidence only.
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
  id: ev.target_plus.marketplace.1_3_seller_entities_in_dataset
  source_section: 1.3 Seller Entities in Dataset
  source_context: marketplace
  source_line_start: 25
  source_line_end: 30
  evidence_type: table
  supported_semantics:
  - Documented source values, observed distributions, table statistics, financial waterfall, fee/tax context, or benchmark guidance
    for 1.3 Seller Entities in Dataset.
  unsupported_semantics:
  - Do not infer tenant/group/platform-account/bank/payment-gateway/statutory-filing/external-logistics cards from this evidence.
  - Seller, brand, Stripe, bank, or carrier mentions remain columns, value profiles, rules, caveats, or raw evidence only.
  allowed_card_types:
  - value_profile
  - column
  - metric
  - rule
  - table
  - formula_template
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
  id: ev.target_plus.marketplace.1_4_brand_profiles
  source_section: 1.4 Brand Profiles
  source_context: marketplace
  source_line_start: 31
  source_line_end: 48
  evidence_type: table
  supported_semantics:
  - Documented source values, observed distributions, table statistics, financial waterfall, fee/tax context, or benchmark guidance
    for 1.4 Brand Profiles.
  unsupported_semantics:
  - Do not infer tenant/group/platform-account/bank/payment-gateway/statutory-filing/external-logistics cards from this evidence.
  - Seller, brand, Stripe, bank, or carrier mentions remain columns, value profiles, rules, caveats, or raw evidence only.
  allowed_card_types:
  - value_profile
  - column
  - metric
  - rule
  - table
  - formula_template
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
  id: ev.target_plus.marketplace.2_transaction_lifecycle
  source_section: 2. Transaction Lifecycle
  source_context: marketplace
  source_line_start: 49
  source_line_end: 50
  evidence_type: prose
  supported_semantics:
  - Prose semantics from source section 2. Transaction Lifecycle.
  unsupported_semantics:
  - Do not infer tenant/group/platform-account/bank/payment-gateway/statutory-filing/external-logistics cards from this evidence.
  - Do not create process variants unless the source gives a materially different sequence or matching logic.
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
  id: ev.target_plus.marketplace.2_1_forward_order_flow
  source_section: 2.1 Forward Order Flow
  source_context: marketplace
  source_line_start: 51
  source_line_end: 79
  evidence_type: prose
  supported_semantics:
  - Prose semantics from source section 2.1 Forward Order Flow.
  unsupported_semantics:
  - Do not infer tenant/group/platform-account/bank/payment-gateway/statutory-filing/external-logistics cards from this evidence.
  - Do not create process variants unless the source gives a materially different sequence or matching logic.
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
  id: ev.target_plus.marketplace.2_2_return_flow
  source_section: 2.2 Return Flow
  source_context: marketplace
  source_line_start: 80
  source_line_end: 101
  evidence_type: prose
  supported_semantics:
  - Prose semantics from source section 2.2 Return Flow.
  unsupported_semantics:
  - Do not infer tenant/group/platform-account/bank/payment-gateway/statutory-filing/external-logistics cards from this evidence.
  - Do not create process variants unless the source gives a materially different sequence or matching logic.
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
  id: ev.target_plus.marketplace.2_3_reverse_charge_flow
  source_section: 2.3 Reverse Charge Flow
  source_context: marketplace
  source_line_start: 102
  source_line_end: 117
  evidence_type: prose
  supported_semantics:
  - Prose semantics from source section 2.3 Reverse Charge Flow.
  unsupported_semantics:
  - Do not infer tenant/group/platform-account/bank/payment-gateway/statutory-filing/external-logistics cards from this evidence.
  - Do not create process variants unless the source gives a materially different sequence or matching logic.
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
  id: ev.target_plus.marketplace.3_entity_relationships_across_tables
  source_section: 3. Entity Relationships Across Tables
  source_context: marketplace
  source_line_start: 118
  source_line_end: 119
  evidence_type: prose
  supported_semantics:
  - Prose semantics from source section 3. Entity Relationships Across Tables.
  unsupported_semantics:
  - Do not infer tenant/group/platform-account/bank/payment-gateway/statutory-filing/external-logistics cards from this evidence.
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
  id: ev.target_plus.marketplace.3_1_join_map
  source_section: 3.1 Join Map
  source_context: marketplace
  source_line_start: 120
  source_line_end: 132
  evidence_type: prose
  supported_semantics:
  - Prose semantics from source section 3.1 Join Map.
  unsupported_semantics:
  - Do not infer tenant/group/platform-account/bank/payment-gateway/statutory-filing/external-logistics cards from this evidence.
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
  id: ev.target_plus.marketplace.3_2_primary_join_keys
  source_section: 3.2 Primary Join Keys
  source_context: marketplace
  source_line_start: 133
  source_line_end: 146
  evidence_type: table
  supported_semantics:
  - Documented source values, observed distributions, table statistics, financial waterfall, fee/tax context, or benchmark guidance
    for 3.2 Primary Join Keys.
  unsupported_semantics:
  - Do not infer tenant/group/platform-account/bank/payment-gateway/statutory-filing/external-logistics cards from this evidence.
  allowed_card_types:
  - value_profile
  - column
  - metric
  - rule
  - table
  - formula_template
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
  id: ev.target_plus.marketplace.4_fee_structure_and_financial_waterfall
  source_section: 4. Fee Structure & Financial Waterfall
  source_context: marketplace
  source_line_start: 147
  source_line_end: 148
  evidence_type: table
  supported_semantics:
  - Documented source values, observed distributions, table statistics, financial waterfall, fee/tax context, or benchmark guidance
    for 4. Fee Structure & Financial Waterfall.
  unsupported_semantics:
  - Do not infer tenant/group/platform-account/bank/payment-gateway/statutory-filing/external-logistics cards from this evidence.
  allowed_card_types:
  - value_profile
  - column
  - metric
  - rule
  - table
  - formula_template
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
  id: ev.target_plus.marketplace.4_1_commission_structure_confirmed_by_data
  source_section: 4.1 Commission Structure (Confirmed by Data)
  source_context: marketplace
  source_line_start: 149
  source_line_end: 163
  evidence_type: table
  supported_semantics:
  - Documented source values, observed distributions, table statistics, financial waterfall, fee/tax context, or benchmark guidance
    for 4.1 Commission Structure (Confirmed by Data).
  unsupported_semantics:
  - Do not infer tenant/group/platform-account/bank/payment-gateway/statutory-filing/external-logistics cards from this evidence.
  allowed_card_types:
  - value_profile
  - column
  - metric
  - rule
  - table
  - formula_template
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
  id: ev.target_plus.marketplace.4_2_full_payout_waterfall_forward_sales_observed
  source_section: 4.2 Full Payout Waterfall (Forward Sales — Observed)
  source_context: marketplace
  source_line_start: 164
  source_line_end: 181
  evidence_type: prose
  supported_semantics:
  - Prose semantics from source section 4.2 Full Payout Waterfall (Forward Sales — Observed).
  unsupported_semantics:
  - Do not infer tenant/group/platform-account/bank/payment-gateway/statutory-filing/external-logistics cards from this evidence.
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
  id: ev.target_plus.marketplace.4_3_us_sales_tax_marketplace_facilitator_model
  source_section: 4.3 US Sales Tax — Marketplace Facilitator Model
  source_context: marketplace
  source_line_start: 182
  source_line_end: 192
  evidence_type: table
  supported_semantics:
  - Documented source values, observed distributions, table statistics, financial waterfall, fee/tax context, or benchmark guidance
    for 4.3 US Sales Tax — Marketplace Facilitator Model.
  unsupported_semantics:
  - Do not infer tenant/group/platform-account/bank/payment-gateway/statutory-filing/external-logistics cards from this evidence.
  allowed_card_types:
  - value_profile
  - column
  - metric
  - rule
  - table
  - formula_template
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
  id: ev.target_plus.marketplace.4_4_return_handling
  source_section: 4.4 Return Handling
  source_context: marketplace
  source_line_start: 193
  source_line_end: 199
  evidence_type: prose
  supported_semantics:
  - Prose semantics from source section 4.4 Return Handling.
  unsupported_semantics:
  - Do not infer tenant/group/platform-account/bank/payment-gateway/statutory-filing/external-logistics cards from this evidence.
  - Seller, brand, Stripe, bank, or carrier mentions remain columns, value profiles, rules, caveats, or raw evidence only.
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
  id: ev.target_plus.marketplace.5_key_business_metrics_with_sql
  source_section: 5. Key Business Metrics (with SQL)
  source_context: marketplace
  source_line_start: 200
  source_line_end: 201
  evidence_type: query_example
  supported_semantics:
  - Executable/source-backed SQL query pattern for 5. Key Business Metrics (with SQL), including source tables, filters, aggregations,
    and output aliases.
  unsupported_semantics:
  - Do not infer tenant/group/platform-account/bank/payment-gateway/statutory-filing/external-logistics cards from this evidence.
  - Do not create metric implementations unless SQL references documented columns and required filters.
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
  id: ev.target_plus.marketplace.5_1_total_gmv
  source_section: 5.1 Total GMV
  source_context: marketplace
  source_line_start: 202
  source_line_end: 213
  evidence_type: query_example
  supported_semantics:
  - Executable/source-backed SQL query pattern for 5.1 Total GMV, including source tables, filters, aggregations, and output aliases.
  unsupported_semantics:
  - Do not infer tenant/group/platform-account/bank/payment-gateway/statutory-filing/external-logistics cards from this evidence.
  - Do not create metric implementations unless SQL references documented columns and required filters.
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
  id: ev.target_plus.marketplace.5_2_net_revenue_settlement_view
  source_section: 5.2 Net Revenue (Settlement View)
  source_context: marketplace
  source_line_start: 214
  source_line_end: 226
  evidence_type: prose
  supported_semantics:
  - Prose semantics from source section 5.2 Net Revenue (Settlement View).
  unsupported_semantics:
  - Do not infer tenant/group/platform-account/bank/payment-gateway/statutory-filing/external-logistics cards from this evidence.
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
  id: ev.target_plus.marketplace.5_3_return_rate
  source_section: 5.3 Return Rate
  source_context: marketplace
  source_line_start: 227
  source_line_end: 239
  evidence_type: query_example
  supported_semantics:
  - Executable/source-backed SQL query pattern for 5.3 Return Rate, including source tables, filters, aggregations, and output aliases.
  unsupported_semantics:
  - Do not infer tenant/group/platform-account/bank/payment-gateway/statutory-filing/external-logistics cards from this evidence.
  - Do not create metric implementations unless SQL references documented columns and required filters.
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
  id: ev.target_plus.marketplace.5_4_average_order_value_aov
  source_section: 5.4 Average Order Value (AOV)
  source_context: marketplace
  source_line_start: 240
  source_line_end: 248
  evidence_type: query_example
  supported_semantics:
  - Executable/source-backed SQL query pattern for 5.4 Average Order Value (AOV), including source tables, filters, aggregations, and
    output aliases.
  unsupported_semantics:
  - Do not infer tenant/group/platform-account/bank/payment-gateway/statutory-filing/external-logistics cards from this evidence.
  - Do not create metric implementations unless SQL references documented columns and required filters.
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
  id: ev.target_plus.marketplace.5_5_effective_payout_rate
  source_section: 5.5 Effective Payout Rate
  source_context: marketplace
  source_line_start: 249
  source_line_end: 259
  evidence_type: query_example
  supported_semantics:
  - Executable/source-backed SQL query pattern for 5.5 Effective Payout Rate, including source tables, filters, aggregations, and output
    aliases.
  unsupported_semantics:
  - Do not infer tenant/group/platform-account/bank/payment-gateway/statutory-filing/external-logistics cards from this evidence.
  - Do not create metric implementations unless SQL references documented columns and required filters.
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
  id: ev.target_plus.marketplace.5_6_top_selling_skus
  source_section: 5.6 Top Selling SKUs
  source_context: marketplace
  source_line_start: 260
  source_line_end: 274
  evidence_type: query_example
  supported_semantics:
  - Executable/source-backed SQL query pattern for 5.6 Top Selling SKUs, including source tables, filters, aggregations, and output
    aliases.
  unsupported_semantics:
  - Do not infer tenant/group/platform-account/bank/payment-gateway/statutory-filing/external-logistics cards from this evidence.
  - Do not create metric implementations unless SQL references documented columns and required filters.
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
  id: ev.target_plus.marketplace.5_7_cancellation_rate
  source_section: 5.7 Cancellation Rate
  source_context: marketplace
  source_line_start: 275
  source_line_end: 288
  evidence_type: query_example
  supported_semantics:
  - Executable/source-backed SQL query pattern for 5.7 Cancellation Rate, including source tables, filters, aggregations, and output
    aliases.
  unsupported_semantics:
  - Do not infer tenant/group/platform-account/bank/payment-gateway/statutory-filing/external-logistics cards from this evidence.
  - Do not create metric implementations unless SQL references documented columns and required filters.
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
  id: ev.target_plus.marketplace.6_reconciliation_use_cases
  source_section: 6. Reconciliation Use Cases
  source_context: marketplace
  source_line_start: 289
  source_line_end: 290
  evidence_type: reconciliation_playbook
  supported_semantics:
  - Source-backed Target Plus reconciliation logic for 6. Reconciliation Use Cases, including join keys, filters, amount comparison,
    and output status fields.
  unsupported_semantics:
  - Do not infer tenant/group/platform-account/bank/payment-gateway/statutory-filing/external-logistics cards from this evidence.
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
  id: ev.target_plus.marketplace.6_1_sales_settlement_reconciliation
  source_section: 6.1 Sales ↔ Settlement Reconciliation
  source_context: marketplace
  source_line_start: 291
  source_line_end: 312
  evidence_type: reconciliation_playbook
  supported_semantics:
  - Source-backed Target Plus reconciliation logic for 6.1 Sales ↔ Settlement Reconciliation, including join keys, filters, amount comparison,
    and output status fields.
  unsupported_semantics:
  - Do not infer tenant/group/platform-account/bank/payment-gateway/statutory-filing/external-logistics cards from this evidence.
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
  id: ev.target_plus.marketplace.6_2_returns_settlement_refund_match
  source_section: 6.2 Returns ↔ Settlement Refund Match
  source_context: marketplace
  source_line_start: 313
  source_line_end: 328
  evidence_type: reconciliation_playbook
  supported_semantics:
  - Source-backed Target Plus reconciliation logic for 6.2 Returns ↔ Settlement Refund Match, including join keys, filters, amount comparison,
    and output status fields.
  unsupported_semantics:
  - Do not infer tenant/group/platform-account/bank/payment-gateway/statutory-filing/external-logistics cards from this evidence.
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
  id: ev.target_plus.marketplace.6_3_commission_validation
  source_section: 6.3 Commission Validation
  source_context: marketplace
  source_line_start: 329
  source_line_end: 344
  evidence_type: query_example
  supported_semantics:
  - Executable/source-backed SQL query pattern for 6.3 Commission Validation, including source tables, filters, aggregations, and output
    aliases.
  unsupported_semantics:
  - Do not infer tenant/group/platform-account/bank/payment-gateway/statutory-filing/external-logistics cards from this evidence.
  - Do not create metric implementations unless SQL references documented columns and required filters.
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
  id: ev.target_plus.marketplace.6_4_payout_reconciliation
  source_section: 6.4 Payout Reconciliation
  source_context: marketplace
  source_line_start: 345
  source_line_end: 365
  evidence_type: reconciliation_playbook
  supported_semantics:
  - Source-backed Target Plus reconciliation logic for 6.4 Payout Reconciliation, including join keys, filters, amount comparison, and
    output status fields.
  unsupported_semantics:
  - Do not infer tenant/group/platform-account/bank/payment-gateway/statutory-filing/external-logistics cards from this evidence.
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
  id: ev.target_plus.marketplace.7_data_quality_observations_and_known_issues
  source_section: 7. Data Quality Observations & Known Issues
  source_context: marketplace
  source_line_start: 366
  source_line_end: 383
  evidence_type: caveat
  supported_semantics:
  - Data quality, mandatory-filter, timing, or scope caveat semantics for 7. Data Quality Observations & Known Issues.
  unsupported_semantics:
  - Do not infer tenant/group/platform-account/bank/payment-gateway/statutory-filing/external-logistics cards from this evidence.
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
  id: ev.target_plus.marketplace.8_mandatory_query_filters
  source_section: 8. Mandatory Query Filters
  source_context: marketplace
  source_line_start: 384
  source_line_end: 403
  evidence_type: caveat
  supported_semantics:
  - Data quality, mandatory-filter, timing, or scope caveat semantics for 8. Mandatory Query Filters.
  unsupported_semantics:
  - Do not infer tenant/group/platform-account/bank/payment-gateway/statutory-filing/external-logistics cards from this evidence.
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
  id: ev.target_plus.marketplace.9_table_summary_reference
  source_section: 9. Table Summary Reference
  source_context: marketplace
  source_line_start: 404
  source_line_end: 412
  evidence_type: table
  supported_semantics:
  - Documented source values, observed distributions, table statistics, financial waterfall, fee/tax context, or benchmark guidance
    for 9. Table Summary Reference.
  unsupported_semantics:
  - Do not infer tenant/group/platform-account/bank/payment-gateway/statutory-filing/external-logistics cards from this evidence.
  allowed_card_types:
  - value_profile
  - column
  - metric
  - rule
  - table
  - formula_template
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
  id: ev.target_plus.settlement.table_target_settlement_table_knowledge_base
  source_section: 'Table: Target Settlement — Table Knowledge Base'
  source_context: settlement
  source_line_start: 413
  source_line_end: 419
  evidence_type: prose
  supported_semantics:
  - 'Prose semantics from source section Table: Target Settlement — Table Knowledge Base.'
  unsupported_semantics:
  - Do not infer tenant/group/platform-account/bank/payment-gateway/statutory-filing/external-logistics cards from this evidence.
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
  id: ev.target_plus.settlement.1_table_overview
  source_section: 1. Table Overview
  source_context: settlement
  source_line_start: 420
  source_line_end: 432
  evidence_type: prose
  supported_semantics:
  - Prose semantics from source section 1. Table Overview.
  unsupported_semantics:
  - Do not infer tenant/group/platform-account/bank/payment-gateway/statutory-filing/external-logistics cards from this evidence.
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
  id: ev.target_plus.settlement.2_key_statistics
  source_section: 2. Key Statistics
  source_context: settlement
  source_line_start: 433
  source_line_end: 459
  evidence_type: table
  supported_semantics:
  - Documented source values, observed distributions, table statistics, financial waterfall, fee/tax context, or benchmark guidance
    for 2. Key Statistics.
  unsupported_semantics:
  - Do not infer tenant/group/platform-account/bank/payment-gateway/statutory-filing/external-logistics cards from this evidence.
  allowed_card_types:
  - value_profile
  - column
  - metric
  - rule
  - table
  - formula_template
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
  id: ev.target_plus.settlement.3_schema_details_37_columns
  source_section: 3. Schema Details (37 Columns)
  source_context: settlement
  source_line_start: 460
  source_line_end: 461
  evidence_type: schema_reference
  supported_semantics:
  - settlement source table schema columns, source-declared types, and source descriptions.
  unsupported_semantics:
  - Do not infer tenant/group/platform-account/bank/payment-gateway/statutory-filing/external-logistics cards from this evidence.
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
  id: ev.target_plus.settlement.3_1_identity_columns
  source_section: 3.1 Identity Columns
  source_context: settlement
  source_line_start: 462
  source_line_end: 476
  evidence_type: prose
  supported_semantics:
  - Prose semantics from source section 3.1 Identity Columns.
  unsupported_semantics:
  - Do not infer tenant/group/platform-account/bank/payment-gateway/statutory-filing/external-logistics cards from this evidence.
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
  id: ev.target_plus.settlement.3_2_date_columns
  source_section: 3.2 Date Columns
  source_context: settlement
  source_line_start: 477
  source_line_end: 483
  evidence_type: prose
  supported_semantics:
  - Prose semantics from source section 3.2 Date Columns.
  unsupported_semantics:
  - Do not infer tenant/group/platform-account/bank/payment-gateway/statutory-filing/external-logistics cards from this evidence.
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
  id: ev.target_plus.settlement.3_3_financial_columns
  source_section: 3.3 Financial Columns
  source_context: settlement
  source_line_start: 484
  source_line_end: 495
  evidence_type: prose
  supported_semantics:
  - Prose semantics from source section 3.3 Financial Columns.
  unsupported_semantics:
  - Do not infer tenant/group/platform-account/bank/payment-gateway/statutory-filing/external-logistics cards from this evidence.
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
  id: ev.target_plus.settlement.3_4_classification_columns
  source_section: 3.4 Classification Columns
  source_context: settlement
  source_line_start: 496
  source_line_end: 505
  evidence_type: prose
  supported_semantics:
  - Prose semantics from source section 3.4 Classification Columns.
  unsupported_semantics:
  - Do not infer tenant/group/platform-account/bank/payment-gateway/statutory-filing/external-logistics cards from this evidence.
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
  id: ev.target_plus.settlement.3_5_system_metadata_columns
  source_section: 3.5 System / Metadata Columns
  source_context: settlement
  source_line_start: 506
  source_line_end: 519
  evidence_type: prose
  supported_semantics:
  - Prose semantics from source section 3.5 System / Metadata Columns.
  unsupported_semantics:
  - Do not infer tenant/group/platform-account/bank/payment-gateway/statutory-filing/external-logistics cards from this evidence.
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
  id: ev.target_plus.settlement.4_distinct_value_analysis
  source_section: 4. Distinct Value Analysis
  source_context: settlement
  source_line_start: 520
  source_line_end: 521
  evidence_type: table
  supported_semantics:
  - Documented source values, observed distributions, table statistics, financial waterfall, fee/tax context, or benchmark guidance
    for 4. Distinct Value Analysis.
  unsupported_semantics:
  - Do not infer tenant/group/platform-account/bank/payment-gateway/statutory-filing/external-logistics cards from this evidence.
  allowed_card_types:
  - value_profile
  - column
  - metric
  - rule
  - table
  - formula_template
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
  id: ev.target_plus.settlement.transaction_type_internal_txn_type_full_breakdown
  source_section: '`transaction_type` / `internal_txn_type` Full Breakdown'
  source_context: settlement
  source_line_start: 522
  source_line_end: 529
  evidence_type: prose
  supported_semantics:
  - Prose semantics from source section `transaction_type` / `internal_txn_type` Full Breakdown.
  unsupported_semantics:
  - Do not infer tenant/group/platform-account/bank/payment-gateway/statutory-filing/external-logistics cards from this evidence.
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
  id: ev.target_plus.settlement.reverse_charge_what_is_it
  source_section: '`reverse charge` — What Is It?'
  source_context: settlement
  source_line_start: 530
  source_line_end: 533
  evidence_type: prose
  supported_semantics:
  - Prose semantics from source section `reverse charge` — What Is It?.
  unsupported_semantics:
  - Do not infer tenant/group/platform-account/bank/payment-gateway/statutory-filing/external-logistics cards from this evidence.
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
  id: ev.target_plus.settlement.total_tax_0_0_always
  source_section: '`total_tax = 0.0` (Always)'
  source_context: settlement
  source_line_start: 534
  source_line_end: 537
  evidence_type: table
  supported_semantics:
  - Documented source values, observed distributions, table statistics, financial waterfall, fee/tax context, or benchmark guidance
    for `total_tax = 0.0` (Always).
  unsupported_semantics:
  - Do not infer tenant/group/platform-account/bank/payment-gateway/statutory-filing/external-logistics cards from this evidence.
  allowed_card_types:
  - value_profile
  - column
  - metric
  - rule
  - table
  - formula_template
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
  id: ev.target_plus.settlement.payout_batch_structure
  source_section: Payout Batch Structure
  source_context: settlement
  source_line_start: 538
  source_line_end: 548
  evidence_type: table
  supported_semantics:
  - Documented source values, observed distributions, table statistics, financial waterfall, fee/tax context, or benchmark guidance
    for Payout Batch Structure.
  unsupported_semantics:
  - Do not infer tenant/group/platform-account/bank/payment-gateway/statutory-filing/external-logistics cards from this evidence.
  allowed_card_types:
  - value_profile
  - column
  - metric
  - rule
  - table
  - formula_template
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
  id: ev.target_plus.settlement.commission_rate
  source_section: Commission Rate
  source_context: settlement
  source_line_start: 549
  source_line_end: 552
  evidence_type: prose
  supported_semantics:
  - Prose semantics from source section Commission Rate.
  unsupported_semantics:
  - Do not infer tenant/group/platform-account/bank/payment-gateway/statutory-filing/external-logistics cards from this evidence.
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
  id: ev.target_plus.settlement.stripe_id_formats
  source_section: Stripe ID Formats
  source_context: settlement
  source_line_start: 553
  source_line_end: 563
  evidence_type: table
  supported_semantics:
  - Documented source values, observed distributions, table statistics, financial waterfall, fee/tax context, or benchmark guidance
    for Stripe ID Formats.
  unsupported_semantics:
  - Do not infer tenant/group/platform-account/bank/payment-gateway/statutory-filing/external-logistics cards from this evidence.
  - Seller, brand, Stripe, bank, or carrier mentions remain columns, value profiles, rules, caveats, or raw evidence only.
  allowed_card_types:
  - value_profile
  - column
  - metric
  - rule
  - table
  - formula_template
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
  id: ev.target_plus.settlement.5_financial_waterfall_forward_sales
  source_section: 5. Financial Waterfall (Forward Sales)
  source_context: settlement
  source_line_start: 564
  source_line_end: 589
  evidence_type: table
  supported_semantics:
  - Documented source values, observed distributions, table statistics, financial waterfall, fee/tax context, or benchmark guidance
    for 5. Financial Waterfall (Forward Sales).
  unsupported_semantics:
  - Do not infer tenant/group/platform-account/bank/payment-gateway/statutory-filing/external-logistics cards from this evidence.
  allowed_card_types:
  - value_profile
  - column
  - metric
  - rule
  - table
  - formula_template
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
  id: ev.target_plus.settlement.6_sample_records
  source_section: 6. Sample Records
  source_context: settlement
  source_line_start: 590
  source_line_end: 630
  evidence_type: prose
  supported_semantics:
  - Prose semantics from source section 6. Sample Records.
  unsupported_semantics:
  - Do not infer tenant/group/platform-account/bank/payment-gateway/statutory-filing/external-logistics cards from this evidence.
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
  id: ev.target_plus.settlement.7_data_quality_observations
  source_section: 7. Data Quality Observations
  source_context: settlement
  source_line_start: 631
  source_line_end: 645
  evidence_type: caveat
  supported_semantics:
  - Data quality, mandatory-filter, timing, or scope caveat semantics for 7. Data Quality Observations.
  unsupported_semantics:
  - Do not infer tenant/group/platform-account/bank/payment-gateway/statutory-filing/external-logistics cards from this evidence.
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
  id: ev.target_plus.settlement.8_common_query_patterns
  source_section: 8. Common Query Patterns
  source_context: settlement
  source_line_start: 646
  source_line_end: 647
  evidence_type: query_example
  supported_semantics:
  - Executable/source-backed SQL query pattern for 8. Common Query Patterns, including source tables, filters, aggregations, and output
    aliases.
  unsupported_semantics:
  - Do not infer tenant/group/platform-account/bank/payment-gateway/statutory-filing/external-logistics cards from this evidence.
  - Do not create metric implementations unless SQL references documented columns and required filters.
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
  id: ev.target_plus.settlement.8_1_payout_batch_summary
  source_section: 8.1 Payout Batch Summary
  source_context: settlement
  source_line_start: 648
  source_line_end: 665
  evidence_type: query_example
  supported_semantics:
  - Executable/source-backed SQL query pattern for 8.1 Payout Batch Summary, including source tables, filters, aggregations, and output
    aliases.
  unsupported_semantics:
  - Do not infer tenant/group/platform-account/bank/payment-gateway/statutory-filing/external-logistics cards from this evidence.
  - Do not create metric implementations unless SQL references documented columns and required filters.
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
  id: ev.target_plus.settlement.8_2_monthly_settlement_waterfall
  source_section: 8.2 Monthly Settlement Waterfall
  source_context: settlement
  source_line_start: 666
  source_line_end: 682
  evidence_type: query_example
  supported_semantics:
  - Executable/source-backed SQL query pattern for 8.2 Monthly Settlement Waterfall, including source tables, filters, aggregations,
    and output aliases.
  unsupported_semantics:
  - Do not infer tenant/group/platform-account/bank/payment-gateway/statutory-filing/external-logistics cards from this evidence.
  - Do not create metric implementations unless SQL references documented columns and required filters.
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
  id: ev.target_plus.settlement.8_3_commission_validation
  source_section: 8.3 Commission Validation
  source_context: settlement
  source_line_start: 683
  source_line_end: 697
  evidence_type: query_example
  supported_semantics:
  - Executable/source-backed SQL query pattern for 8.3 Commission Validation, including source tables, filters, aggregations, and output
    aliases.
  unsupported_semantics:
  - Do not infer tenant/group/platform-account/bank/payment-gateway/statutory-filing/external-logistics cards from this evidence.
  - Do not create metric implementations unless SQL references documented columns and required filters.
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
  id: ev.target_plus.settlement.8_4_sales_settlement_reconciliation
  source_section: 8.4 Sales ↔ Settlement Reconciliation
  source_context: settlement
  source_line_start: 698
  source_line_end: 713
  evidence_type: reconciliation_playbook
  supported_semantics:
  - Source-backed Target Plus reconciliation logic for 8.4 Sales ↔ Settlement Reconciliation, including join keys, filters, amount comparison,
    and output status fields.
  unsupported_semantics:
  - Do not infer tenant/group/platform-account/bank/payment-gateway/statutory-filing/external-logistics cards from this evidence.
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
  id: ev.target_plus.settlement.8_5_effective_payout_rate
  source_section: 8.5 Effective Payout Rate
  source_context: settlement
  source_line_start: 714
  source_line_end: 729
  evidence_type: query_example
  supported_semantics:
  - Executable/source-backed SQL query pattern for 8.5 Effective Payout Rate, including source tables, filters, aggregations, and output
    aliases.
  unsupported_semantics:
  - Do not infer tenant/group/platform-account/bank/payment-gateway/statutory-filing/external-logistics cards from this evidence.
  - Do not create metric implementations unless SQL references documented columns and required filters.
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
  id: ev.target_plus.settlement.1_table_overview_2
  source_section: 1. Table Overview
  source_context: settlement
  source_line_start: 730
  source_line_end: 742
  evidence_type: prose
  supported_semantics:
  - Prose semantics from source section 1. Table Overview.
  unsupported_semantics:
  - Do not infer tenant/group/platform-account/bank/payment-gateway/statutory-filing/external-logistics cards from this evidence.
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
  id: ev.target_plus.settlement.2_key_statistics_2
  source_section: 2. Key Statistics
  source_context: settlement
  source_line_start: 743
  source_line_end: 769
  evidence_type: table
  supported_semantics:
  - Documented source values, observed distributions, table statistics, financial waterfall, fee/tax context, or benchmark guidance
    for 2. Key Statistics.
  unsupported_semantics:
  - Do not infer tenant/group/platform-account/bank/payment-gateway/statutory-filing/external-logistics cards from this evidence.
  allowed_card_types:
  - value_profile
  - column
  - metric
  - rule
  - table
  - formula_template
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
  id: ev.target_plus.settlement.3_schema_details_37_columns_2
  source_section: 3. Schema Details (37 Columns)
  source_context: settlement
  source_line_start: 770
  source_line_end: 771
  evidence_type: schema_reference
  supported_semantics:
  - settlement source table schema columns, source-declared types, and source descriptions.
  unsupported_semantics:
  - Do not infer tenant/group/platform-account/bank/payment-gateway/statutory-filing/external-logistics cards from this evidence.
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
  id: ev.target_plus.settlement.3_1_identity_columns_2
  source_section: 3.1 Identity Columns
  source_context: settlement
  source_line_start: 772
  source_line_end: 786
  evidence_type: prose
  supported_semantics:
  - Prose semantics from source section 3.1 Identity Columns.
  unsupported_semantics:
  - Do not infer tenant/group/platform-account/bank/payment-gateway/statutory-filing/external-logistics cards from this evidence.
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
  id: ev.target_plus.settlement.3_2_date_columns_2
  source_section: 3.2 Date Columns
  source_context: settlement
  source_line_start: 787
  source_line_end: 793
  evidence_type: prose
  supported_semantics:
  - Prose semantics from source section 3.2 Date Columns.
  unsupported_semantics:
  - Do not infer tenant/group/platform-account/bank/payment-gateway/statutory-filing/external-logistics cards from this evidence.
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
  id: ev.target_plus.settlement.3_3_financial_columns_2
  source_section: 3.3 Financial Columns
  source_context: settlement
  source_line_start: 794
  source_line_end: 805
  evidence_type: prose
  supported_semantics:
  - Prose semantics from source section 3.3 Financial Columns.
  unsupported_semantics:
  - Do not infer tenant/group/platform-account/bank/payment-gateway/statutory-filing/external-logistics cards from this evidence.
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
  id: ev.target_plus.settlement.3_4_classification_columns_2
  source_section: 3.4 Classification Columns
  source_context: settlement
  source_line_start: 806
  source_line_end: 815
  evidence_type: prose
  supported_semantics:
  - Prose semantics from source section 3.4 Classification Columns.
  unsupported_semantics:
  - Do not infer tenant/group/platform-account/bank/payment-gateway/statutory-filing/external-logistics cards from this evidence.
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
  id: ev.target_plus.settlement.3_5_system_metadata_columns_2
  source_section: 3.5 System / Metadata Columns
  source_context: settlement
  source_line_start: 816
  source_line_end: 829
  evidence_type: prose
  supported_semantics:
  - Prose semantics from source section 3.5 System / Metadata Columns.
  unsupported_semantics:
  - Do not infer tenant/group/platform-account/bank/payment-gateway/statutory-filing/external-logistics cards from this evidence.
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
  id: ev.target_plus.settlement.4_distinct_value_analysis_2
  source_section: 4. Distinct Value Analysis
  source_context: settlement
  source_line_start: 830
  source_line_end: 831
  evidence_type: table
  supported_semantics:
  - Documented source values, observed distributions, table statistics, financial waterfall, fee/tax context, or benchmark guidance
    for 4. Distinct Value Analysis.
  unsupported_semantics:
  - Do not infer tenant/group/platform-account/bank/payment-gateway/statutory-filing/external-logistics cards from this evidence.
  allowed_card_types:
  - value_profile
  - column
  - metric
  - rule
  - table
  - formula_template
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
  id: ev.target_plus.settlement.transaction_type_internal_txn_type_full_breakdown_2
  source_section: '`transaction_type` / `internal_txn_type` Full Breakdown'
  source_context: settlement
  source_line_start: 832
  source_line_end: 839
  evidence_type: prose
  supported_semantics:
  - Prose semantics from source section `transaction_type` / `internal_txn_type` Full Breakdown.
  unsupported_semantics:
  - Do not infer tenant/group/platform-account/bank/payment-gateway/statutory-filing/external-logistics cards from this evidence.
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
  id: ev.target_plus.settlement.reverse_charge_what_is_it_2
  source_section: '`reverse charge` — What Is It?'
  source_context: settlement
  source_line_start: 840
  source_line_end: 843
  evidence_type: prose
  supported_semantics:
  - Prose semantics from source section `reverse charge` — What Is It?.
  unsupported_semantics:
  - Do not infer tenant/group/platform-account/bank/payment-gateway/statutory-filing/external-logistics cards from this evidence.
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
  id: ev.target_plus.settlement.total_tax_0_0_always_2
  source_section: '`total_tax = 0.0` (Always)'
  source_context: settlement
  source_line_start: 844
  source_line_end: 847
  evidence_type: table
  supported_semantics:
  - Documented source values, observed distributions, table statistics, financial waterfall, fee/tax context, or benchmark guidance
    for `total_tax = 0.0` (Always).
  unsupported_semantics:
  - Do not infer tenant/group/platform-account/bank/payment-gateway/statutory-filing/external-logistics cards from this evidence.
  allowed_card_types:
  - value_profile
  - column
  - metric
  - rule
  - table
  - formula_template
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
  id: ev.target_plus.settlement.payout_batch_structure_2
  source_section: Payout Batch Structure
  source_context: settlement
  source_line_start: 848
  source_line_end: 858
  evidence_type: table
  supported_semantics:
  - Documented source values, observed distributions, table statistics, financial waterfall, fee/tax context, or benchmark guidance
    for Payout Batch Structure.
  unsupported_semantics:
  - Do not infer tenant/group/platform-account/bank/payment-gateway/statutory-filing/external-logistics cards from this evidence.
  allowed_card_types:
  - value_profile
  - column
  - metric
  - rule
  - table
  - formula_template
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
  id: ev.target_plus.settlement.commission_rate_2
  source_section: Commission Rate
  source_context: settlement
  source_line_start: 859
  source_line_end: 862
  evidence_type: prose
  supported_semantics:
  - Prose semantics from source section Commission Rate.
  unsupported_semantics:
  - Do not infer tenant/group/platform-account/bank/payment-gateway/statutory-filing/external-logistics cards from this evidence.
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
  id: ev.target_plus.settlement.stripe_id_formats_2
  source_section: Stripe ID Formats
  source_context: settlement
  source_line_start: 863
  source_line_end: 873
  evidence_type: table
  supported_semantics:
  - Documented source values, observed distributions, table statistics, financial waterfall, fee/tax context, or benchmark guidance
    for Stripe ID Formats.
  unsupported_semantics:
  - Do not infer tenant/group/platform-account/bank/payment-gateway/statutory-filing/external-logistics cards from this evidence.
  - Seller, brand, Stripe, bank, or carrier mentions remain columns, value profiles, rules, caveats, or raw evidence only.
  allowed_card_types:
  - value_profile
  - column
  - metric
  - rule
  - table
  - formula_template
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
  id: ev.target_plus.settlement.5_financial_waterfall_forward_sales_2
  source_section: 5. Financial Waterfall (Forward Sales)
  source_context: settlement
  source_line_start: 874
  source_line_end: 899
  evidence_type: table
  supported_semantics:
  - Documented source values, observed distributions, table statistics, financial waterfall, fee/tax context, or benchmark guidance
    for 5. Financial Waterfall (Forward Sales).
  unsupported_semantics:
  - Do not infer tenant/group/platform-account/bank/payment-gateway/statutory-filing/external-logistics cards from this evidence.
  allowed_card_types:
  - value_profile
  - column
  - metric
  - rule
  - table
  - formula_template
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
  id: ev.target_plus.settlement.6_sample_records_2
  source_section: 6. Sample Records
  source_context: settlement
  source_line_start: 900
  source_line_end: 940
  evidence_type: prose
  supported_semantics:
  - Prose semantics from source section 6. Sample Records.
  unsupported_semantics:
  - Do not infer tenant/group/platform-account/bank/payment-gateway/statutory-filing/external-logistics cards from this evidence.
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
  id: ev.target_plus.settlement.7_data_quality_observations_2
  source_section: 7. Data Quality Observations
  source_context: settlement
  source_line_start: 941
  source_line_end: 955
  evidence_type: caveat
  supported_semantics:
  - Data quality, mandatory-filter, timing, or scope caveat semantics for 7. Data Quality Observations.
  unsupported_semantics:
  - Do not infer tenant/group/platform-account/bank/payment-gateway/statutory-filing/external-logistics cards from this evidence.
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
  id: ev.target_plus.settlement.8_common_query_patterns_2
  source_section: 8. Common Query Patterns
  source_context: settlement
  source_line_start: 956
  source_line_end: 957
  evidence_type: query_example
  supported_semantics:
  - Executable/source-backed SQL query pattern for 8. Common Query Patterns, including source tables, filters, aggregations, and output
    aliases.
  unsupported_semantics:
  - Do not infer tenant/group/platform-account/bank/payment-gateway/statutory-filing/external-logistics cards from this evidence.
  - Do not create metric implementations unless SQL references documented columns and required filters.
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
  id: ev.target_plus.settlement.8_1_payout_batch_summary_2
  source_section: 8.1 Payout Batch Summary
  source_context: settlement
  source_line_start: 958
  source_line_end: 975
  evidence_type: query_example
  supported_semantics:
  - Executable/source-backed SQL query pattern for 8.1 Payout Batch Summary, including source tables, filters, aggregations, and output
    aliases.
  unsupported_semantics:
  - Do not infer tenant/group/platform-account/bank/payment-gateway/statutory-filing/external-logistics cards from this evidence.
  - Do not create metric implementations unless SQL references documented columns and required filters.
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
  id: ev.target_plus.settlement.8_2_monthly_settlement_waterfall_2
  source_section: 8.2 Monthly Settlement Waterfall
  source_context: settlement
  source_line_start: 976
  source_line_end: 992
  evidence_type: query_example
  supported_semantics:
  - Executable/source-backed SQL query pattern for 8.2 Monthly Settlement Waterfall, including source tables, filters, aggregations,
    and output aliases.
  unsupported_semantics:
  - Do not infer tenant/group/platform-account/bank/payment-gateway/statutory-filing/external-logistics cards from this evidence.
  - Do not create metric implementations unless SQL references documented columns and required filters.
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
  id: ev.target_plus.settlement.8_3_commission_validation_2
  source_section: 8.3 Commission Validation
  source_context: settlement
  source_line_start: 993
  source_line_end: 1007
  evidence_type: query_example
  supported_semantics:
  - Executable/source-backed SQL query pattern for 8.3 Commission Validation, including source tables, filters, aggregations, and output
    aliases.
  unsupported_semantics:
  - Do not infer tenant/group/platform-account/bank/payment-gateway/statutory-filing/external-logistics cards from this evidence.
  - Do not create metric implementations unless SQL references documented columns and required filters.
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
  id: ev.target_plus.settlement.8_4_sales_settlement_reconciliation_2
  source_section: 8.4 Sales ↔ Settlement Reconciliation
  source_context: settlement
  source_line_start: 1008
  source_line_end: 1023
  evidence_type: reconciliation_playbook
  supported_semantics:
  - Source-backed Target Plus reconciliation logic for 8.4 Sales ↔ Settlement Reconciliation, including join keys, filters, amount comparison,
    and output status fields.
  unsupported_semantics:
  - Do not infer tenant/group/platform-account/bank/payment-gateway/statutory-filing/external-logistics cards from this evidence.
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
  id: ev.target_plus.settlement.8_5_effective_payout_rate_2
  source_section: 8.5 Effective Payout Rate
  source_context: settlement
  source_line_start: 1024
  source_line_end: 1034
  evidence_type: query_example
  supported_semantics:
  - Executable/source-backed SQL query pattern for 8.5 Effective Payout Rate, including source tables, filters, aggregations, and output
    aliases.
  unsupported_semantics:
  - Do not infer tenant/group/platform-account/bank/payment-gateway/statutory-filing/external-logistics cards from this evidence.
  - Do not create metric implementations unless SQL references documented columns and required filters.
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
  id: ev.target_plus.mapping.table_target_tcin_mapping_table_knowledge_base
  source_section: 'Table: Target TCIN Mapping — Table Knowledge Base'
  source_context: mapping
  source_line_start: 1035
  source_line_end: 1041
  evidence_type: prose
  supported_semantics:
  - 'Prose semantics from source section Table: Target TCIN Mapping — Table Knowledge Base.'
  unsupported_semantics:
  - Do not infer tenant/group/platform-account/bank/payment-gateway/statutory-filing/external-logistics cards from this evidence.
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
  id: ev.target_plus.mapping.1_table_overview
  source_section: 1. Table Overview
  source_context: mapping
  source_line_start: 1042
  source_line_end: 1052
  evidence_type: prose
  supported_semantics:
  - Prose semantics from source section 1. Table Overview.
  unsupported_semantics:
  - Do not infer tenant/group/platform-account/bank/payment-gateway/statutory-filing/external-logistics cards from this evidence.
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
  id: ev.target_plus.mapping.2_key_statistics
  source_section: 2. Key Statistics
  source_context: mapping
  source_line_start: 1053
  source_line_end: 1069
  evidence_type: table
  supported_semantics:
  - Documented source values, observed distributions, table statistics, financial waterfall, fee/tax context, or benchmark guidance
    for 2. Key Statistics.
  unsupported_semantics:
  - Do not infer tenant/group/platform-account/bank/payment-gateway/statutory-filing/external-logistics cards from this evidence.
  allowed_card_types:
  - value_profile
  - column
  - metric
  - rule
  - table
  - formula_template
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
  id: ev.target_plus.mapping.3_schema_details_21_columns
  source_section: 3. Schema Details (21 Columns)
  source_context: mapping
  source_line_start: 1070
  source_line_end: 1095
  evidence_type: schema_reference
  supported_semantics:
  - mapping source table schema columns, source-declared types, and source descriptions.
  unsupported_semantics:
  - Do not infer tenant/group/platform-account/bank/payment-gateway/statutory-filing/external-logistics cards from this evidence.
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
  id: ev.target_plus.mapping.4_distinct_value_analysis
  source_section: 4. Distinct Value Analysis
  source_context: mapping
  source_line_start: 1096
  source_line_end: 1097
  evidence_type: table
  supported_semantics:
  - Documented source values, observed distributions, table statistics, financial waterfall, fee/tax context, or benchmark guidance
    for 4. Distinct Value Analysis.
  unsupported_semantics:
  - Do not infer tenant/group/platform-account/bank/payment-gateway/statutory-filing/external-logistics cards from this evidence.
  allowed_card_types:
  - value_profile
  - column
  - metric
  - rule
  - table
  - formula_template
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
  id: ev.target_plus.mapping.brand_distribution
  source_section: Brand Distribution
  source_context: mapping
  source_line_start: 1098
  source_line_end: 1106
  evidence_type: table
  supported_semantics:
  - Documented source values, observed distributions, table statistics, financial waterfall, fee/tax context, or benchmark guidance
    for Brand Distribution.
  unsupported_semantics:
  - Do not infer tenant/group/platform-account/bank/payment-gateway/statutory-filing/external-logistics cards from this evidence.
  - Seller, brand, Stripe, bank, or carrier mentions remain columns, value profiles, rules, caveats, or raw evidence only.
  allowed_card_types:
  - value_profile
  - column
  - metric
  - rule
  - table
  - formula_template
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
  id: ev.target_plus.mapping.sku_naming_conventions
  source_section: SKU Naming Conventions
  source_context: mapping
  source_line_start: 1107
  source_line_end: 1113
  evidence_type: table
  supported_semantics:
  - Documented source values, observed distributions, table statistics, financial waterfall, fee/tax context, or benchmark guidance
    for SKU Naming Conventions.
  unsupported_semantics:
  - Do not infer tenant/group/platform-account/bank/payment-gateway/statutory-filing/external-logistics cards from this evidence.
  allowed_card_types:
  - value_profile
  - column
  - metric
  - rule
  - table
  - formula_template
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
  id: ev.target_plus.mapping.barcode_coverage
  source_section: Barcode Coverage
  source_context: mapping
  source_line_start: 1114
  source_line_end: 1119
  evidence_type: table
  supported_semantics:
  - Documented source values, observed distributions, table statistics, financial waterfall, fee/tax context, or benchmark guidance
    for Barcode Coverage.
  unsupported_semantics:
  - Do not infer tenant/group/platform-account/bank/payment-gateway/statutory-filing/external-logistics cards from this evidence.
  allowed_card_types:
  - value_profile
  - column
  - metric
  - rule
  - table
  - formula_template
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
  id: ev.target_plus.mapping.asin_cross_reference
  source_section: ASIN Cross-Reference
  source_context: mapping
  source_line_start: 1120
  source_line_end: 1126
  evidence_type: table
  supported_semantics:
  - Documented source values, observed distributions, table statistics, financial waterfall, fee/tax context, or benchmark guidance
    for ASIN Cross-Reference.
  unsupported_semantics:
  - Do not infer tenant/group/platform-account/bank/payment-gateway/statutory-filing/external-logistics cards from this evidence.
  allowed_card_types:
  - value_profile
  - column
  - metric
  - rule
  - table
  - formula_template
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
  id: ev.target_plus.mapping.5_sample_records
  source_section: 5. Sample Records
  source_context: mapping
  source_line_start: 1127
  source_line_end: 1147
  evidence_type: prose
  supported_semantics:
  - Prose semantics from source section 5. Sample Records.
  unsupported_semantics:
  - Do not infer tenant/group/platform-account/bank/payment-gateway/statutory-filing/external-logistics cards from this evidence.
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
  id: ev.target_plus.mapping.6_data_quality_observations
  source_section: 6. Data Quality Observations
  source_context: mapping
  source_line_start: 1148
  source_line_end: 1160
  evidence_type: caveat
  supported_semantics:
  - Data quality, mandatory-filter, timing, or scope caveat semantics for 6. Data Quality Observations.
  unsupported_semantics:
  - Do not infer tenant/group/platform-account/bank/payment-gateway/statutory-filing/external-logistics cards from this evidence.
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
  id: ev.target_plus.mapping.7_common_query_patterns
  source_section: 7. Common Query Patterns
  source_context: mapping
  source_line_start: 1161
  source_line_end: 1162
  evidence_type: query_example
  supported_semantics:
  - Executable/source-backed SQL query pattern for 7. Common Query Patterns, including source tables, filters, aggregations, and output
    aliases.
  unsupported_semantics:
  - Do not infer tenant/group/platform-account/bank/payment-gateway/statutory-filing/external-logistics cards from this evidence.
  - Do not create metric implementations unless SQL references documented columns and required filters.
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
  id: ev.target_plus.mapping.7_1_full_catalogue_with_sales_coverage
  source_section: 7.1 Full Catalogue with Sales Coverage
  source_context: mapping
  source_line_start: 1163
  source_line_end: 1177
  evidence_type: query_example
  supported_semantics:
  - Executable/source-backed SQL query pattern for 7.1 Full Catalogue with Sales Coverage, including source tables, filters, aggregations,
    and output aliases.
  unsupported_semantics:
  - Do not infer tenant/group/platform-account/bank/payment-gateway/statutory-filing/external-logistics cards from this evidence.
  - Do not create metric implementations unless SQL references documented columns and required filters.
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
  id: ev.target_plus.mapping.7_2_brand_level_sku_count
  source_section: 7.2 Brand-Level SKU Count
  source_context: mapping
  source_line_start: 1178
  source_line_end: 1190
  evidence_type: prose
  supported_semantics:
  - Prose semantics from source section 7.2 Brand-Level SKU Count.
  unsupported_semantics:
  - Do not infer tenant/group/platform-account/bank/payment-gateway/statutory-filing/external-logistics cards from this evidence.
  - Seller, brand, Stripe, bank, or carrier mentions remain columns, value profiles, rules, caveats, or raw evidence only.
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
  id: ev.target_plus.mapping.7_3_enrich_sales_with_mapping_data
  source_section: 7.3 Enrich Sales with Mapping Data
  source_context: mapping
  source_line_start: 1191
  source_line_end: 1204
  evidence_type: prose
  supported_semantics:
  - Prose semantics from source section 7.3 Enrich Sales with Mapping Data.
  unsupported_semantics:
  - Do not infer tenant/group/platform-account/bank/payment-gateway/statutory-filing/external-logistics cards from this evidence.
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
  id: ev.target_plus.returns.table_target_returns_table_knowledge_base
  source_section: 'Table: Target Returns — Table Knowledge Base'
  source_context: returns
  source_line_start: 1205
  source_line_end: 1211
  evidence_type: prose
  supported_semantics:
  - 'Prose semantics from source section Table: Target Returns — Table Knowledge Base.'
  unsupported_semantics:
  - Do not infer tenant/group/platform-account/bank/payment-gateway/statutory-filing/external-logistics cards from this evidence.
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
  id: ev.target_plus.returns.1_table_overview
  source_section: 1. Table Overview
  source_context: returns
  source_line_start: 1212
  source_line_end: 1220
  evidence_type: prose
  supported_semantics:
  - Prose semantics from source section 1. Table Overview.
  unsupported_semantics:
  - Do not infer tenant/group/platform-account/bank/payment-gateway/statutory-filing/external-logistics cards from this evidence.
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
  id: ev.target_plus.returns.2_key_statistics
  source_section: 2. Key Statistics
  source_context: returns
  source_line_start: 1221
  source_line_end: 1242
  evidence_type: table
  supported_semantics:
  - Documented source values, observed distributions, table statistics, financial waterfall, fee/tax context, or benchmark guidance
    for 2. Key Statistics.
  unsupported_semantics:
  - Do not infer tenant/group/platform-account/bank/payment-gateway/statutory-filing/external-logistics cards from this evidence.
  allowed_card_types:
  - value_profile
  - column
  - metric
  - rule
  - table
  - formula_template
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
  id: ev.target_plus.returns.3_schema_details_30_columns
  source_section: 3. Schema Details (30 Columns)
  source_context: returns
  source_line_start: 1243
  source_line_end: 1244
  evidence_type: schema_reference
  supported_semantics:
  - returns source table schema columns, source-declared types, and source descriptions.
  unsupported_semantics:
  - Do not infer tenant/group/platform-account/bank/payment-gateway/statutory-filing/external-logistics cards from this evidence.
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
  id: ev.target_plus.returns.3_1_identity_columns
  source_section: 3.1 Identity Columns
  source_context: returns
  source_line_start: 1245
  source_line_end: 1257
  evidence_type: prose
  supported_semantics:
  - Prose semantics from source section 3.1 Identity Columns.
  unsupported_semantics:
  - Do not infer tenant/group/platform-account/bank/payment-gateway/statutory-filing/external-logistics cards from this evidence.
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
  id: ev.target_plus.returns.3_2_date_columns
  source_section: 3.2 Date Columns
  source_context: returns
  source_line_start: 1258
  source_line_end: 1264
  evidence_type: prose
  supported_semantics:
  - Prose semantics from source section 3.2 Date Columns.
  unsupported_semantics:
  - Do not infer tenant/group/platform-account/bank/payment-gateway/statutory-filing/external-logistics cards from this evidence.
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
  id: ev.target_plus.returns.3_3_financial_columns
  source_section: 3.3 Financial Columns
  source_context: returns
  source_line_start: 1265
  source_line_end: 1271
  evidence_type: prose
  supported_semantics:
  - Prose semantics from source section 3.3 Financial Columns.
  unsupported_semantics:
  - Do not infer tenant/group/platform-account/bank/payment-gateway/statutory-filing/external-logistics cards from this evidence.
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
  id: ev.target_plus.returns.3_4_classification_columns
  source_section: 3.4 Classification Columns
  source_context: returns
  source_line_start: 1272
  source_line_end: 1281
  evidence_type: prose
  supported_semantics:
  - Prose semantics from source section 3.4 Classification Columns.
  unsupported_semantics:
  - Do not infer tenant/group/platform-account/bank/payment-gateway/statutory-filing/external-logistics cards from this evidence.
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
  id: ev.target_plus.returns.3_5_system_metadata_columns
  source_section: 3.5 System / Metadata Columns
  source_context: returns
  source_line_start: 1282
  source_line_end: 1295
  evidence_type: prose
  supported_semantics:
  - Prose semantics from source section 3.5 System / Metadata Columns.
  unsupported_semantics:
  - Do not infer tenant/group/platform-account/bank/payment-gateway/statutory-filing/external-logistics cards from this evidence.
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
  id: ev.target_plus.returns.4_distinct_value_analysis
  source_section: 4. Distinct Value Analysis
  source_context: returns
  source_line_start: 1296
  source_line_end: 1297
  evidence_type: table
  supported_semantics:
  - Documented source values, observed distributions, table statistics, financial waterfall, fee/tax context, or benchmark guidance
    for 4. Distinct Value Analysis.
  unsupported_semantics:
  - Do not infer tenant/group/platform-account/bank/payment-gateway/statutory-filing/external-logistics cards from this evidence.
  allowed_card_types:
  - value_profile
  - column
  - metric
  - rule
  - table
  - formula_template
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
  id: ev.target_plus.returns.internal_txn_type_distribution
  source_section: '`internal_txn_type` Distribution'
  source_context: returns
  source_line_start: 1298
  source_line_end: 1304
  evidence_type: table
  supported_semantics:
  - Documented source values, observed distributions, table statistics, financial waterfall, fee/tax context, or benchmark guidance
    for `internal_txn_type` Distribution.
  unsupported_semantics:
  - Do not infer tenant/group/platform-account/bank/payment-gateway/statutory-filing/external-logistics cards from this evidence.
  allowed_card_types:
  - value_profile
  - column
  - metric
  - rule
  - table
  - formula_template
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
  id: ev.target_plus.returns.order_status_when_populated
  source_section: '`order_status` (when populated)'
  source_context: returns
  source_line_start: 1305
  source_line_end: 1314
  evidence_type: prose
  supported_semantics:
  - Prose semantics from source section `order_status` (when populated).
  unsupported_semantics:
  - Do not infer tenant/group/platform-account/bank/payment-gateway/statutory-filing/external-logistics cards from this evidence.
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
  id: ev.target_plus.returns.return_reasons_description_field_top_17_values
  source_section: Return Reasons (`description` field) — Top 17 Values
  source_context: returns
  source_line_start: 1315
  source_line_end: 1332
  evidence_type: prose
  supported_semantics:
  - Prose semantics from source section Return Reasons (`description` field) — Top 17 Values.
  unsupported_semantics:
  - Do not infer tenant/group/platform-account/bank/payment-gateway/statutory-filing/external-logistics cards from this evidence.
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
  id: ev.target_plus.returns.other_id_carrier_tracking_numbers
  source_section: '`other_id` — Carrier Tracking Numbers'
  source_context: returns
  source_line_start: 1333
  source_line_end: 1344
  evidence_type: prose
  supported_semantics:
  - Prose semantics from source section `other_id` — Carrier Tracking Numbers.
  unsupported_semantics:
  - Do not infer tenant/group/platform-account/bank/payment-gateway/statutory-filing/external-logistics cards from this evidence.
  - Seller, brand, Stripe, bank, or carrier mentions remain columns, value profiles, rules, caveats, or raw evidence only.
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
  id: ev.target_plus.returns.5_sample_records
  source_section: 5. Sample Records
  source_context: returns
  source_line_start: 1345
  source_line_end: 1373
  evidence_type: prose
  supported_semantics:
  - Prose semantics from source section 5. Sample Records.
  unsupported_semantics:
  - Do not infer tenant/group/platform-account/bank/payment-gateway/statutory-filing/external-logistics cards from this evidence.
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
  id: ev.target_plus.returns.6_data_quality_observations
  source_section: 6. Data Quality Observations
  source_context: returns
  source_line_start: 1374
  source_line_end: 1387
  evidence_type: caveat
  supported_semantics:
  - Data quality, mandatory-filter, timing, or scope caveat semantics for 6. Data Quality Observations.
  unsupported_semantics:
  - Do not infer tenant/group/platform-account/bank/payment-gateway/statutory-filing/external-logistics cards from this evidence.
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
  id: ev.target_plus.returns.7_common_query_patterns
  source_section: 7. Common Query Patterns
  source_context: returns
  source_line_start: 1388
  source_line_end: 1389
  evidence_type: query_example
  supported_semantics:
  - Executable/source-backed SQL query pattern for 7. Common Query Patterns, including source tables, filters, aggregations, and output
    aliases.
  unsupported_semantics:
  - Do not infer tenant/group/platform-account/bank/payment-gateway/statutory-filing/external-logistics cards from this evidence.
  - Do not create metric implementations unless SQL references documented columns and required filters.
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
  id: ev.target_plus.returns.7_1_return_volume_and_value_by_reason
  source_section: 7.1 Return Volume and Value by Reason
  source_context: returns
  source_line_start: 1390
  source_line_end: 1406
  evidence_type: prose
  supported_semantics:
  - Prose semantics from source section 7.1 Return Volume and Value by Reason.
  unsupported_semantics:
  - Do not infer tenant/group/platform-account/bank/payment-gateway/statutory-filing/external-logistics cards from this evidence.
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
  id: ev.target_plus.returns.7_2_return_rate_by_brand
  source_section: 7.2 Return Rate by Brand
  source_context: returns
  source_line_start: 1407
  source_line_end: 1419
  evidence_type: query_example
  supported_semantics:
  - Executable/source-backed SQL query pattern for 7.2 Return Rate by Brand, including source tables, filters, aggregations, and output
    aliases.
  unsupported_semantics:
  - Do not infer tenant/group/platform-account/bank/payment-gateway/statutory-filing/external-logistics cards from this evidence.
  - Seller, brand, Stripe, bank, or carrier mentions remain columns, value profiles, rules, caveats, or raw evidence only.
  - Do not create metric implementations unless SQL references documented columns and required filters.
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
  - process_variant
  - non_executable_metric_implementation
  confidence: high
```
```yaml
source_evidence:
  id: ev.target_plus.returns.7_3_monthly_return_trend
  source_section: 7.3 Monthly Return Trend
  source_context: returns
  source_line_start: 1420
  source_line_end: 1431
  evidence_type: query_example
  supported_semantics:
  - Executable/source-backed SQL query pattern for 7.3 Monthly Return Trend, including source tables, filters, aggregations, and output
    aliases.
  unsupported_semantics:
  - Do not infer tenant/group/platform-account/bank/payment-gateway/statutory-filing/external-logistics cards from this evidence.
  - Do not create metric implementations unless SQL references documented columns and required filters.
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
  id: ev.target_plus.returns.7_4_returns_sales_reconciliation
  source_section: 7.4 Returns ↔ Sales Reconciliation
  source_context: returns
  source_line_start: 1432
  source_line_end: 1451
  evidence_type: reconciliation_playbook
  supported_semantics:
  - Source-backed Target Plus reconciliation logic for 7.4 Returns ↔ Sales Reconciliation, including join keys, filters, amount comparison,
    and output status fields.
  unsupported_semantics:
  - Do not infer tenant/group/platform-account/bank/payment-gateway/statutory-filing/external-logistics cards from this evidence.
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
  id: ev.target_plus.returns.7_5_sku_level_return_rate
  source_section: 7.5 SKU-Level Return Rate
  source_context: returns
  source_line_start: 1452
  source_line_end: 1475
  evidence_type: query_example
  supported_semantics:
  - Executable/source-backed SQL query pattern for 7.5 SKU-Level Return Rate, including source tables, filters, aggregations, and output
    aliases.
  unsupported_semantics:
  - Do not infer tenant/group/platform-account/bank/payment-gateway/statutory-filing/external-logistics cards from this evidence.
  - Do not create metric implementations unless SQL references documented columns and required filters.
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
  id: ev.target_plus.sales.table_target_sales_table_knowledge_base
  source_section: 'Table: Target Sales — Table Knowledge Base'
  source_context: sales
  source_line_start: 1476
  source_line_end: 1482
  evidence_type: prose
  supported_semantics:
  - 'Prose semantics from source section Table: Target Sales — Table Knowledge Base.'
  unsupported_semantics:
  - Do not infer tenant/group/platform-account/bank/payment-gateway/statutory-filing/external-logistics cards from this evidence.
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
  id: ev.target_plus.sales.1_table_overview
  source_section: 1. Table Overview
  source_context: sales
  source_line_start: 1483
  source_line_end: 1491
  evidence_type: prose
  supported_semantics:
  - Prose semantics from source section 1. Table Overview.
  unsupported_semantics:
  - Do not infer tenant/group/platform-account/bank/payment-gateway/statutory-filing/external-logistics cards from this evidence.
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
  id: ev.target_plus.sales.2_key_statistics
  source_section: 2. Key Statistics
  source_context: sales
  source_line_start: 1492
  source_line_end: 1513
  evidence_type: table
  supported_semantics:
  - Documented source values, observed distributions, table statistics, financial waterfall, fee/tax context, or benchmark guidance
    for 2. Key Statistics.
  unsupported_semantics:
  - Do not infer tenant/group/platform-account/bank/payment-gateway/statutory-filing/external-logistics cards from this evidence.
  allowed_card_types:
  - value_profile
  - column
  - metric
  - rule
  - table
  - formula_template
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
  id: ev.target_plus.sales.3_schema_details_29_columns
  source_section: 3. Schema Details (29 Columns)
  source_context: sales
  source_line_start: 1514
  source_line_end: 1515
  evidence_type: schema_reference
  supported_semantics:
  - sales source table schema columns, source-declared types, and source descriptions.
  unsupported_semantics:
  - Do not infer tenant/group/platform-account/bank/payment-gateway/statutory-filing/external-logistics cards from this evidence.
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
  id: ev.target_plus.sales.3_1_identity_columns
  source_section: 3.1 Identity Columns
  source_context: sales
  source_line_start: 1516
  source_line_end: 1528
  evidence_type: prose
  supported_semantics:
  - Prose semantics from source section 3.1 Identity Columns.
  unsupported_semantics:
  - Do not infer tenant/group/platform-account/bank/payment-gateway/statutory-filing/external-logistics cards from this evidence.
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
  id: ev.target_plus.sales.3_2_date_columns
  source_section: 3.2 Date Columns
  source_context: sales
  source_line_start: 1529
  source_line_end: 1534
  evidence_type: prose
  supported_semantics:
  - Prose semantics from source section 3.2 Date Columns.
  unsupported_semantics:
  - Do not infer tenant/group/platform-account/bank/payment-gateway/statutory-filing/external-logistics cards from this evidence.
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
  id: ev.target_plus.sales.3_3_financial_columns
  source_section: 3.3 Financial Columns
  source_context: sales
  source_line_start: 1535
  source_line_end: 1542
  evidence_type: prose
  supported_semantics:
  - Prose semantics from source section 3.3 Financial Columns.
  unsupported_semantics:
  - Do not infer tenant/group/platform-account/bank/payment-gateway/statutory-filing/external-logistics cards from this evidence.
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
  id: ev.target_plus.sales.3_4_classification_columns
  source_section: 3.4 Classification Columns
  source_context: sales
  source_line_start: 1543
  source_line_end: 1552
  evidence_type: prose
  supported_semantics:
  - Prose semantics from source section 3.4 Classification Columns.
  unsupported_semantics:
  - Do not infer tenant/group/platform-account/bank/payment-gateway/statutory-filing/external-logistics cards from this evidence.
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
  id: ev.target_plus.sales.3_5_system_metadata_columns
  source_section: 3.5 System / Metadata Columns
  source_context: sales
  source_line_start: 1553
  source_line_end: 1570
  evidence_type: prose
  supported_semantics:
  - Prose semantics from source section 3.5 System / Metadata Columns.
  unsupported_semantics:
  - Do not infer tenant/group/platform-account/bank/payment-gateway/statutory-filing/external-logistics cards from this evidence.
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
  id: ev.target_plus.sales.4_distinct_value_analysis
  source_section: 4. Distinct Value Analysis
  source_context: sales
  source_line_start: 1571
  source_line_end: 1572
  evidence_type: table
  supported_semantics:
  - Documented source values, observed distributions, table statistics, financial waterfall, fee/tax context, or benchmark guidance
    for 4. Distinct Value Analysis.
  unsupported_semantics:
  - Do not infer tenant/group/platform-account/bank/payment-gateway/statutory-filing/external-logistics cards from this evidence.
  allowed_card_types:
  - value_profile
  - column
  - metric
  - rule
  - table
  - formula_template
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
  id: ev.target_plus.sales.order_status_distribution
  source_section: '`order_status` Distribution'
  source_context: sales
  source_line_start: 1573
  source_line_end: 1579
  evidence_type: table
  supported_semantics:
  - Documented source values, observed distributions, table statistics, financial waterfall, fee/tax context, or benchmark guidance
    for `order_status` Distribution.
  unsupported_semantics:
  - Do not infer tenant/group/platform-account/bank/payment-gateway/statutory-filing/external-logistics cards from this evidence.
  allowed_card_types:
  - value_profile
  - column
  - metric
  - rule
  - table
  - formula_template
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
  id: ev.target_plus.sales.brand_distribution
  source_section: '`brand` Distribution'
  source_context: sales
  source_line_start: 1580
  source_line_end: 1587
  evidence_type: table
  supported_semantics:
  - Documented source values, observed distributions, table statistics, financial waterfall, fee/tax context, or benchmark guidance
    for `brand` Distribution.
  unsupported_semantics:
  - Do not infer tenant/group/platform-account/bank/payment-gateway/statutory-filing/external-logistics cards from this evidence.
  - Seller, brand, Stripe, bank, or carrier mentions remain columns, value profiles, rules, caveats, or raw evidence only.
  allowed_card_types:
  - value_profile
  - column
  - metric
  - rule
  - table
  - formula_template
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
  id: ev.target_plus.sales.order_id_format
  source_section: Order ID Format
  source_context: sales
  source_line_start: 1588
  source_line_end: 1595
  evidence_type: table
  supported_semantics:
  - Documented source values, observed distributions, table statistics, financial waterfall, fee/tax context, or benchmark guidance
    for Order ID Format.
  unsupported_semantics:
  - Do not infer tenant/group/platform-account/bank/payment-gateway/statutory-filing/external-logistics cards from this evidence.
  allowed_card_types:
  - value_profile
  - column
  - metric
  - rule
  - table
  - formula_template
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
  id: ev.target_plus.sales.item_id_format
  source_section: Item ID Format
  source_context: sales
  source_line_start: 1596
  source_line_end: 1599
  evidence_type: table
  supported_semantics:
  - Documented source values, observed distributions, table statistics, financial waterfall, fee/tax context, or benchmark guidance
    for Item ID Format.
  unsupported_semantics:
  - Do not infer tenant/group/platform-account/bank/payment-gateway/statutory-filing/external-logistics cards from this evidence.
  allowed_card_types:
  - value_profile
  - column
  - metric
  - rule
  - table
  - formula_template
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
  id: ev.target_plus.sales.sku_id_format
  source_section: SKU ID Format
  source_context: sales
  source_line_start: 1600
  source_line_end: 1603
  evidence_type: table
  supported_semantics:
  - Documented source values, observed distributions, table statistics, financial waterfall, fee/tax context, or benchmark guidance
    for SKU ID Format.
  unsupported_semantics:
  - Do not infer tenant/group/platform-account/bank/payment-gateway/statutory-filing/external-logistics cards from this evidence.
  allowed_card_types:
  - value_profile
  - column
  - metric
  - rule
  - table
  - formula_template
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
  id: ev.target_plus.sales.tcin_format
  source_section: TCIN Format
  source_context: sales
  source_line_start: 1604
  source_line_end: 1607
  evidence_type: table
  supported_semantics:
  - Documented source values, observed distributions, table statistics, financial waterfall, fee/tax context, or benchmark guidance
    for TCIN Format.
  unsupported_semantics:
  - Do not infer tenant/group/platform-account/bank/payment-gateway/statutory-filing/external-logistics cards from this evidence.
  allowed_card_types:
  - value_profile
  - column
  - metric
  - rule
  - table
  - formula_template
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
  id: ev.target_plus.sales.other_id
  source_section: '`other_id`'
  source_context: sales
  source_line_start: 1608
  source_line_end: 1614
  evidence_type: prose
  supported_semantics:
  - Prose semantics from source section `other_id`.
  unsupported_semantics:
  - Do not infer tenant/group/platform-account/bank/payment-gateway/statutory-filing/external-logistics cards from this evidence.
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
  id: ev.target_plus.sales.5_sample_records
  source_section: 5. Sample Records
  source_context: sales
  source_line_start: 1615
  source_line_end: 1643
  evidence_type: prose
  supported_semantics:
  - Prose semantics from source section 5. Sample Records.
  unsupported_semantics:
  - Do not infer tenant/group/platform-account/bank/payment-gateway/statutory-filing/external-logistics cards from this evidence.
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
  id: ev.target_plus.sales.6_data_quality_observations
  source_section: 6. Data Quality Observations
  source_context: sales
  source_line_start: 1644
  source_line_end: 1658
  evidence_type: caveat
  supported_semantics:
  - Data quality, mandatory-filter, timing, or scope caveat semantics for 6. Data Quality Observations.
  unsupported_semantics:
  - Do not infer tenant/group/platform-account/bank/payment-gateway/statutory-filing/external-logistics cards from this evidence.
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
  id: ev.target_plus.sales.7_common_query_patterns
  source_section: 7. Common Query Patterns
  source_context: sales
  source_line_start: 1659
  source_line_end: 1660
  evidence_type: query_example
  supported_semantics:
  - Executable/source-backed SQL query pattern for 7. Common Query Patterns, including source tables, filters, aggregations, and output
    aliases.
  unsupported_semantics:
  - Do not infer tenant/group/platform-account/bank/payment-gateway/statutory-filing/external-logistics cards from this evidence.
  - Do not create metric implementations unless SQL references documented columns and required filters.
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
  id: ev.target_plus.sales.7_1_monthly_sales_gmv_by_brand
  source_section: 7.1 Monthly Sales GMV by Brand
  source_context: sales
  source_line_start: 1661
  source_line_end: 1676
  evidence_type: query_example
  supported_semantics:
  - Executable/source-backed SQL query pattern for 7.1 Monthly Sales GMV by Brand, including source tables, filters, aggregations, and
    output aliases.
  unsupported_semantics:
  - Do not infer tenant/group/platform-account/bank/payment-gateway/statutory-filing/external-logistics cards from this evidence.
  - Seller, brand, Stripe, bank, or carrier mentions remain columns, value profiles, rules, caveats, or raw evidence only.
  - Do not create metric implementations unless SQL references documented columns and required filters.
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
  - process_variant
  - non_executable_metric_implementation
  confidence: high
```
```yaml
source_evidence:
  id: ev.target_plus.sales.7_2_sku_level_sales_performance
  source_section: 7.2 SKU-Level Sales Performance
  source_context: sales
  source_line_start: 1677
  source_line_end: 1691
  evidence_type: query_example
  supported_semantics:
  - Executable/source-backed SQL query pattern for 7.2 SKU-Level Sales Performance, including source tables, filters, aggregations,
    and output aliases.
  unsupported_semantics:
  - Do not infer tenant/group/platform-account/bank/payment-gateway/statutory-filing/external-logistics cards from this evidence.
  - Do not create metric implementations unless SQL references documented columns and required filters.
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
  id: ev.target_plus.sales.7_3_sales_settlement_join
  source_section: 7.3 Sales → Settlement Join
  source_context: sales
  source_line_start: 1692
  source_line_end: 1703
  evidence_type: prose
  supported_semantics:
  - Prose semantics from source section 7.3 Sales → Settlement Join.
  unsupported_semantics:
  - Do not infer tenant/group/platform-account/bank/payment-gateway/statutory-filing/external-logistics cards from this evidence.
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
  id: ev.target_plus.sales.7_4_return_rate_by_brand
  source_section: 7.4 Return Rate by Brand
  source_context: sales
  source_line_start: 1704
  source_line_end: 1718
  evidence_type: query_example
  supported_semantics:
  - Executable/source-backed SQL query pattern for 7.4 Return Rate by Brand, including source tables, filters, aggregations, and output
    aliases.
  unsupported_semantics:
  - Do not infer tenant/group/platform-account/bank/payment-gateway/statutory-filing/external-logistics cards from this evidence.
  - Seller, brand, Stripe, bank, or carrier mentions remain columns, value profiles, rules, caveats, or raw evidence only.
  - Do not create metric implementations unless SQL references documented columns and required filters.
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
  - process_variant
  - non_executable_metric_implementation
  confidence: high
```
## 3. SQL Pattern Registry

```yaml
sql_pattern:
  id: sql.target_plus.marketplace.5_1_total_gmv
  source_section: 5.1 Total GMV
  source_context: marketplace
  source_line_start: 204
  source_line_end: 212
  evidence_ref: ev.target_plus.marketplace.5_1_total_gmv
  sql_pattern: |-
    SELECT
      SUM(charged_amount) AS gross_gmv,
      SUM(discount_amount) AS total_discounts,
      SUM(charged_amount) + SUM(discount_amount) AS net_gmv
    FROM zs_observe.target_sales
    WHERE is_active = true AND order_status = 'SHIPPED';
    -- Observed: $169,909 gross GMV; −$2,834 discounts
  required_tables:
  - table.zs_observe.target_sales
  output_aliases_detected:
  - gross_gmv
  - total_discounts
  - net_gmv
  confidence: high
```
```yaml
sql_pattern:
  id: sql.target_plus.marketplace.5_2_net_revenue_settlement_view
  source_section: 5.2 Net Revenue (Settlement View)
  source_context: marketplace
  source_line_start: 216
  source_line_end: 225
  evidence_ref: ev.target_plus.marketplace.5_2_net_revenue_settlement_view
  sql_pattern: |-
    SELECT
      SUM(CASE WHEN transaction_type='forward' THEN settled_amount ELSE 0 END) AS forward_settled,
      SUM(CASE WHEN transaction_type='reverse' THEN settled_amount ELSE 0 END) AS return_adjustments,
      SUM(CASE WHEN transaction_type='reverse charge' THEN settled_amount ELSE 0 END) AS tax_adjustments,
      SUM(settled_amount) AS net_revenue
    FROM zs_observe.target_settlement
    WHERE is_active = true;
    -- Observed: $121,342 forward − $9,185 returns − $1,721 tax adj = $110,436 net
  required_tables:
  - table.zs_observe.target_settlement
  output_aliases_detected:
  - forward_settled
  - return_adjustments
  - tax_adjustments
  - net_revenue
  confidence: high
```
```yaml
sql_pattern:
  id: sql.target_plus.marketplace.5_3_return_rate
  source_section: 5.3 Return Rate
  source_context: marketplace
  source_line_start: 229
  source_line_end: 238
  evidence_ref: ev.target_plus.marketplace.5_3_return_rate
  sql_pattern: |-
    SELECT
      ROUND(100.0 * COUNT(DISTINCT r.order_id)
        / NULLIF(COUNT(DISTINCT s.order_id), 0), 2) AS return_rate_pct
    FROM zs_observe.target_sales s
    LEFT JOIN zs_observe.target_returns r
      ON s.order_id = r.order_id AND r.is_active = true
    WHERE s.is_active = true AND s.order_status = 'SHIPPED';
    -- Observed: ~12.3% (1050 returns / 8538 orders)
  required_tables:
  - table.zs_observe.target_returns
  - table.zs_observe.target_sales
  output_aliases_detected:
  - return_rate_pct
  confidence: high
```
```yaml
sql_pattern:
  id: sql.target_plus.marketplace.5_4_average_order_value_aov
  source_section: 5.4 Average Order Value (AOV)
  source_context: marketplace
  source_line_start: 242
  source_line_end: 247
  evidence_ref: ev.target_plus.marketplace.5_4_average_order_value_aov
  sql_pattern: |-
    SELECT AVG(charged_amount) AS aov
    FROM zs_observe.target_sales
    WHERE is_active = true AND order_status = 'SHIPPED';
    -- Observed: $23.37 (blended); Folkculture $25.56; Katchon $12.99
  required_tables:
  - table.zs_observe.target_sales
  output_aliases_detected:
  - aov
  confidence: high
```
```yaml
sql_pattern:
  id: sql.target_plus.marketplace.5_5_effective_payout_rate
  source_section: 5.5 Effective Payout Rate
  source_context: marketplace
  source_line_start: 251
  source_line_end: 258
  evidence_ref: ev.target_plus.marketplace.5_5_effective_payout_rate
  sql_pattern: |-
    SELECT
      ROUND(100.0 * SUM(settled_amount)
        / NULLIF(SUM(charged_amount_excluding_tax), 0), 2) AS payout_rate_pct
    FROM zs_observe.target_settlement
    WHERE is_active = true AND transaction_type = 'forward';
    -- Observed: 85.2%
  required_tables:
  - table.zs_observe.target_settlement
  output_aliases_detected:
  - payout_rate_pct
  confidence: high
```
```yaml
sql_pattern:
  id: sql.target_plus.marketplace.5_6_top_selling_skus
  source_section: 5.6 Top Selling SKUs
  source_context: marketplace
  source_line_start: 262
  source_line_end: 273
  evidence_ref: ev.target_plus.marketplace.5_6_top_selling_skus
  sql_pattern: |-
    SELECT
      s.tcin, m.sku_id, m.brand, m.asin,
      COUNT(s.order_id) AS units_sold,
      SUM(s.charged_amount) AS revenue
    FROM zs_observe.target_sales s
    JOIN zs_observe.target_tcin_mapping m ON s.tcin = m.tcin AND m.is_active = true
    WHERE s.is_active = true AND s.order_status = 'SHIPPED'
    GROUP BY s.tcin, m.sku_id, m.brand, m.asin
    ORDER BY units_sold DESC
    LIMIT 20;
  required_tables:
  - table.zs_observe.target_sales
  - table.zs_observe.target_tcin_mapping
  output_aliases_detected:
  - units_sold
  - revenue
  confidence: high
```
```yaml
sql_pattern:
  id: sql.target_plus.marketplace.5_7_cancellation_rate
  source_section: 5.7 Cancellation Rate
  source_context: marketplace
  source_line_start: 277
  source_line_end: 284
  evidence_ref: ev.target_plus.marketplace.5_7_cancellation_rate
  sql_pattern: |-
    SELECT
      ROUND(100.0 * COUNT_IF(order_status = 'CANCELED')
        / NULLIF(COUNT(*), 0), 2) AS cancel_rate_pct
    FROM zs_observe.target_sales
    WHERE is_active = true;
    -- Observed: 22/7291 = 0.30% (very low)
  required_tables:
  - table.zs_observe.target_sales
  output_aliases_detected:
  - cancel_rate_pct
  confidence: high
```
```yaml
sql_pattern:
  id: sql.target_plus.marketplace.6_1_sales_settlement_reconciliation
  source_section: 6.1 Sales ↔ Settlement Reconciliation
  source_context: marketplace
  source_line_start: 293
  source_line_end: 311
  evidence_ref: ev.target_plus.marketplace.6_1_sales_settlement_reconciliation
  sql_pattern: |-
    SELECT
      s.order_id, s.item_id, s.brand,
      s.charged_amount AS sales_price,
      st.charged_amount_excluding_tax AS settlement_revenue,
      st.gross_commission,
      st.settled_amount,
      CASE
        WHEN st.item_id IS NULL THEN 'Not Yet Settled'
        WHEN ABS(s.charged_amount - st.charged_amount) < 0.01 THEN 'Matched'
        ELSE 'Price Variance'
      END AS recon_status
    FROM zs_observe.target_sales s
    LEFT JOIN zs_observe.target_settlement st
      ON s.item_id = st.item_id
      AND st.is_active = true
      AND st.transaction_type = 'forward'
    WHERE s.is_active = true AND s.order_status = 'SHIPPED';
  required_tables:
  - table.zs_observe.target_sales
  - table.zs_observe.target_settlement
  output_aliases_detected:
  - sales_price
  - settlement_revenue
  - recon_status
  confidence: high
```
```yaml
sql_pattern:
  id: sql.target_plus.marketplace.6_2_returns_settlement_refund_match
  source_section: 6.2 Returns ↔ Settlement Refund Match
  source_context: marketplace
  source_line_start: 315
  source_line_end: 327
  evidence_ref: ev.target_plus.marketplace.6_2_returns_settlement_refund_match
  sql_pattern: |-
    SELECT
      r.order_id, r.tcin, r.description AS return_reason,
      r.charged_amount AS return_value,
      st.settled_amount AS refund_settled,
      CASE WHEN st.item_id IS NULL THEN 'Refund Pending' ELSE 'Refund Settled' END AS status
    FROM zs_observe.target_returns r
    LEFT JOIN zs_observe.target_settlement st
      ON r.item_id = st.item_id
      AND st.is_active = true
      AND st.transaction_type = 'reverse'
    WHERE r.is_active = true AND r.internal_txn_type = 'reverse';
  required_tables:
  - table.zs_observe.target_returns
  - table.zs_observe.target_settlement
  output_aliases_detected:
  - return_reason
  - return_value
  - refund_settled
  - status
  confidence: high
```
```yaml
sql_pattern:
  id: sql.target_plus.marketplace.6_3_commission_validation
  source_section: 6.3 Commission Validation
  source_context: marketplace
  source_line_start: 331
  source_line_end: 343
  evidence_ref: ev.target_plus.marketplace.6_3_commission_validation
  sql_pattern: |-
    SELECT
      st.brand, st.tcin,
      st.charged_amount_excluding_tax AS taxable_base,
      st.gross_commission AS commission_charged,
      ROUND(st.charged_amount_excluding_tax * 0.15, 4) AS expected_commission,
      ABS(st.gross_commission - ROUND(st.charged_amount_excluding_tax * 0.15, 4)) AS variance
    FROM zs_observe.target_settlement st
    WHERE is_active = true
      AND transaction_type = 'forward'
      AND ABS(st.gross_commission - ROUND(st.charged_amount_excluding_tax * 0.15, 4)) > 0.01;
    -- Identifies any rows where actual commission deviates from 15%
  required_tables:
  - table.zs_observe.target_settlement
  output_aliases_detected:
  - taxable_base
  - commission_charged
  - expected_commission
  - variance
  confidence: high
```
```yaml
sql_pattern:
  id: sql.target_plus.marketplace.6_4_payout_reconciliation
  source_section: 6.4 Payout Reconciliation
  source_context: marketplace
  source_line_start: 347
  source_line_end: 361
  evidence_ref: ev.target_plus.marketplace.6_4_payout_reconciliation
  sql_pattern: |-
    SELECT
      payout_id,
      SUM(settled_amount) AS total_payout,
      COUNT(DISTINCT order_id) AS orders_in_payout,
      MIN(created_date) AS earliest_txn,
      MAX(created_date) AS latest_txn,
      COUNT_IF(transaction_type = 'forward') AS sales_rows,
      COUNT_IF(transaction_type = 'reverse') AS return_rows,
      COUNT_IF(transaction_type = 'reverse charge') AS tax_rows
    FROM zs_observe.target_settlement
    WHERE is_active = true
    GROUP BY payout_id
    ORDER BY earliest_txn;
  required_tables:
  - table.zs_observe.target_settlement
  output_aliases_detected:
  - total_payout
  - orders_in_payout
  - earliest_txn
  - latest_txn
  - sales_rows
  - return_rows
  - tax_rows
  confidence: high
```
```yaml
sql_pattern:
  id: sql.target_plus.marketplace.8_mandatory_query_filters
  source_section: 8. Mandatory Query Filters
  source_context: marketplace
  source_line_start: 386
  source_line_end: 399
  evidence_ref: ev.target_plus.marketplace.8_mandatory_query_filters
  sql_pattern: |-
    -- All Target tables
    WHERE is_active = true
      AND group_level_id = 123

    -- Sales: active shipped orders only
    WHERE is_active = true AND order_status = 'SHIPPED'

    -- Settlement: forward sales only
    WHERE is_active = true AND transaction_type = 'forward'

    -- Returns: confirmed returns only
    WHERE is_active = true AND internal_txn_type = 'reverse'
  required_tables: []
  output_aliases_detected: []
  confidence: high
```
```yaml
sql_pattern:
  id: sql.target_plus.settlement.8_1_payout_batch_summary
  source_section: 8.1 Payout Batch Summary
  source_context: settlement
  source_line_start: 650
  source_line_end: 664
  evidence_ref: ev.target_plus.settlement.8_1_payout_batch_summary_2
  sql_pattern: |-
    SELECT
      payout_id,
      MIN(created_date) AS payout_start,
      MAX(created_date) AS payout_end,
      COUNT(*) AS line_items,
      SUM(CASE WHEN transaction_type = 'forward' THEN settled_amount ELSE 0 END) AS sales_settled,
      SUM(CASE WHEN transaction_type = 'reverse' THEN settled_amount ELSE 0 END) AS returns_settled,
      SUM(CASE WHEN transaction_type = 'reverse charge' THEN settled_amount ELSE 0 END) AS tax_adjustments,
      SUM(settled_amount) AS net_payout
    FROM zs_observe.target_settlement
    WHERE is_active = true
    GROUP BY payout_id
    ORDER BY payout_start;
  required_tables:
  - table.zs_observe.target_settlement
  output_aliases_detected:
  - payout_start
  - payout_end
  - line_items
  - sales_settled
  - returns_settled
  - tax_adjustments
  - net_payout
  confidence: high
```
```yaml
sql_pattern:
  id: sql.target_plus.settlement.8_2_monthly_settlement_waterfall
  source_section: 8.2 Monthly Settlement Waterfall
  source_context: settlement
  source_line_start: 668
  source_line_end: 681
  evidence_ref: ev.target_plus.settlement.8_2_monthly_settlement_waterfall_2
  sql_pattern: |-
    SELECT
      DATE_TRUNC('month', created_date) AS month,
      SUM(CASE WHEN transaction_type='forward' THEN charged_amount_excluding_tax ELSE 0 END) AS gross_gmv,
      SUM(CASE WHEN transaction_type='forward' THEN gross_commission ELSE 0 END) AS commission,
      SUM(CASE WHEN transaction_type='forward' THEN shipping_amount ELSE 0 END) AS shipping,
      SUM(CASE WHEN transaction_type='forward' THEN settled_amount ELSE 0 END) AS forward_settled,
      SUM(CASE WHEN transaction_type='reverse' THEN settled_amount ELSE 0 END) AS returns_settled,
      SUM(CASE WHEN transaction_type='reverse charge' THEN settled_amount ELSE 0 END) AS tax_adj,
      SUM(settled_amount) AS net_payout
    FROM zs_observe.target_settlement
    WHERE is_active = true
    GROUP BY 1 ORDER BY 1;
  required_tables:
  - table.zs_observe.target_settlement
  output_aliases_detected:
  - month
  - gross_gmv
  - commission
  - shipping
  - forward_settled
  - returns_settled
  - tax_adj
  - net_payout
  confidence: high
```
```yaml
sql_pattern:
  id: sql.target_plus.settlement.8_3_commission_validation
  source_section: 8.3 Commission Validation
  source_context: settlement
  source_line_start: 685
  source_line_end: 696
  evidence_ref: ev.target_plus.settlement.8_3_commission_validation_2
  sql_pattern: |-
    SELECT
      brand,
      SUM(charged_amount_excluding_tax) AS taxable_base,
      SUM(gross_commission) AS commission_charged,
      AVG(gross_commission_percentage) AS avg_commission_rate,
      ROUND(100.0 * SUM(gross_commission)
        / NULLIF(SUM(charged_amount_excluding_tax), 0), 4) AS effective_commission_pct
    FROM zs_observe.target_settlement
    WHERE is_active = true AND transaction_type = 'forward'
    GROUP BY brand;
  required_tables:
  - table.zs_observe.target_settlement
  output_aliases_detected:
  - taxable_base
  - commission_charged
  - avg_commission_rate
  - effective_commission_pct
  confidence: high
```
```yaml
sql_pattern:
  id: sql.target_plus.settlement.8_4_sales_settlement_reconciliation
  source_section: 8.4 Sales ↔ Settlement Reconciliation
  source_context: settlement
  source_line_start: 700
  source_line_end: 712
  evidence_ref: ev.target_plus.settlement.8_4_sales_settlement_reconciliation_2
  sql_pattern: |-
    SELECT
      s.order_id, s.item_id,
      s.charged_amount AS sales_unit_price,
      st.charged_amount_excluding_tax AS settlement_revenue,
      st.gross_commission,
      st.settled_amount,
      CASE WHEN st.item_id IS NULL THEN 'Not in Settlement' ELSE 'Matched' END AS status
    FROM zs_observe.target_sales s
    LEFT JOIN zs_observe.target_settlement st
      ON s.item_id = st.item_id AND st.is_active = true
    WHERE s.is_active = true AND s.order_status = 'SHIPPED';
  required_tables:
  - table.zs_observe.target_sales
  - table.zs_observe.target_settlement
  output_aliases_detected:
  - sales_unit_price
  - settlement_revenue
  - status
  confidence: high
```
```yaml
sql_pattern:
  id: sql.target_plus.settlement.8_5_effective_payout_rate
  source_section: 8.5 Effective Payout Rate
  source_context: settlement
  source_line_start: 716
  source_line_end: 723
  evidence_ref: ev.target_plus.settlement.8_5_effective_payout_rate_2
  sql_pattern: |-
    SELECT
      ROUND(100.0 * SUM(settled_amount)
        / NULLIF(SUM(charged_amount_excluding_tax), 0), 2) AS payout_rate_pct
    FROM zs_observe.target_settlement
    WHERE is_active = true AND transaction_type = 'forward';
    -- Observed: ~85.2% payout ratio (after 15% commission)
  required_tables:
  - table.zs_observe.target_settlement
  output_aliases_detected:
  - payout_rate_pct
  confidence: high
```
```yaml
sql_pattern:
  id: sql.target_plus.mapping.7_1_full_catalogue_with_sales_coverage
  source_section: 7.1 Full Catalogue with Sales Coverage
  source_context: mapping
  source_line_start: 1165
  source_line_end: 1176
  evidence_ref: ev.target_plus.mapping.7_1_full_catalogue_with_sales_coverage
  sql_pattern: |-
    SELECT
      m.tcin, m.sku_id, m.brand, m.asin, m.barcode,
      COUNT(s.order_id) AS total_sold,
      SUM(s.charged_amount) AS revenue
    FROM zs_observe.target_tcin_mapping m
    LEFT JOIN zs_observe.target_sales s
      ON m.tcin = s.tcin AND s.is_active = true AND s.order_status = 'SHIPPED'
    WHERE m.is_active = true
    GROUP BY m.tcin, m.sku_id, m.brand, m.asin, m.barcode
    ORDER BY total_sold DESC;
  required_tables:
  - table.zs_observe.target_sales
  - table.zs_observe.target_tcin_mapping
  output_aliases_detected:
  - total_sold
  - revenue
  confidence: high
```
```yaml
sql_pattern:
  id: sql.target_plus.mapping.7_2_brand_level_sku_count
  source_section: 7.2 Brand-Level SKU Count
  source_context: mapping
  source_line_start: 1180
  source_line_end: 1189
  evidence_ref: ev.target_plus.mapping.7_2_brand_level_sku_count
  sql_pattern: |-
    SELECT
      LOWER(brand) AS brand,
      COUNT(*) AS total_skus,
      COUNT_IF(barcode IS NOT NULL) AS skus_with_barcode,
      COUNT_IF(asin IS NOT NULL) AS skus_on_amazon
    FROM zs_observe.target_tcin_mapping
    WHERE is_active = true
    GROUP BY LOWER(brand);
  required_tables:
  - table.zs_observe.target_tcin_mapping
  output_aliases_detected:
  - brand
  - total_skus
  - skus_with_barcode
  - skus_on_amazon
  confidence: high
```
```yaml
sql_pattern:
  id: sql.target_plus.mapping.7_3_enrich_sales_with_mapping_data
  source_section: 7.3 Enrich Sales with Mapping Data
  source_context: mapping
  source_line_start: 1193
  source_line_end: 1203
  evidence_ref: ev.target_plus.mapping.7_3_enrich_sales_with_mapping_data
  sql_pattern: |-
    SELECT
      s.order_id, s.created_date, s.order_status,
      s.charged_amount, s.discount_amount,
      m.sku_id AS clean_sku, m.brand, m.asin, m.barcode
    FROM zs_observe.target_sales s
    JOIN zs_observe.target_tcin_mapping m
      ON s.tcin = m.tcin AND m.is_active = true
    WHERE s.is_active = true
      AND s.order_status = 'SHIPPED';
  required_tables:
  - table.zs_observe.target_sales
  - table.zs_observe.target_tcin_mapping
  output_aliases_detected:
  - clean_sku
  confidence: high
```
```yaml
sql_pattern:
  id: sql.target_plus.returns.7_1_return_volume_and_value_by_reason
  source_section: 7.1 Return Volume and Value by Reason
  source_context: returns
  source_line_start: 1392
  source_line_end: 1405
  evidence_ref: ev.target_plus.returns.7_1_return_volume_and_value_by_reason
  sql_pattern: |-
    SELECT
      description AS return_reason,
      COUNT(*) AS returns,
      SUM(charged_amount) AS total_refunded,
      AVG(charged_amount) AS avg_refund,
      ROUND(100.0 * COUNT(*) / SUM(COUNT(*)) OVER (), 2) AS pct_of_returns
    FROM zs_observe.target_returns
    WHERE is_active = true
      AND internal_txn_type = 'reverse'
      AND description IS NOT NULL
    GROUP BY description
    ORDER BY returns DESC;
  required_tables:
  - table.zs_observe.target_returns
  output_aliases_detected:
  - return_reason
  - returns
  - total_refunded
  - avg_refund
  - pct_of_returns
  confidence: high
```
```yaml
sql_pattern:
  id: sql.target_plus.returns.7_2_return_rate_by_brand
  source_section: 7.2 Return Rate by Brand
  source_context: returns
  source_line_start: 1409
  source_line_end: 1418
  evidence_ref: ev.target_plus.returns.7_2_return_rate_by_brand
  sql_pattern: |-
    SELECT
      brand,
      COUNT(DISTINCT order_id) AS returned_orders,
      SUM(charged_amount) AS total_refunded
    FROM zs_observe.target_returns
    WHERE is_active = true
    GROUP BY brand
    ORDER BY returned_orders DESC;
  required_tables:
  - table.zs_observe.target_returns
  output_aliases_detected:
  - returned_orders
  - total_refunded
  confidence: high
```
```yaml
sql_pattern:
  id: sql.target_plus.returns.7_3_monthly_return_trend
  source_section: 7.3 Monthly Return Trend
  source_context: returns
  source_line_start: 1422
  source_line_end: 1430
  evidence_ref: ev.target_plus.returns.7_3_monthly_return_trend
  sql_pattern: |-
    SELECT
      DATE_TRUNC('month', created_date) AS month,
      COUNT(*) AS returns,
      SUM(charged_amount) AS refund_value
    FROM zs_observe.target_returns
    WHERE is_active = true AND internal_txn_type = 'reverse'
    GROUP BY 1 ORDER BY 1;
  required_tables:
  - table.zs_observe.target_returns
  output_aliases_detected:
  - month
  - returns
  - refund_value
  confidence: high
```
```yaml
sql_pattern:
  id: sql.target_plus.returns.7_4_returns_sales_reconciliation
  source_section: 7.4 Returns ↔ Sales Reconciliation
  source_context: returns
  source_line_start: 1434
  source_line_end: 1450
  evidence_ref: ev.target_plus.returns.7_4_returns_sales_reconciliation
  sql_pattern: |-
    SELECT
      r.order_id,
      r.tcin,
      r.description AS return_reason,
      r.charged_amount AS refund_amount,
      r.returned_date,
      s.charged_amount AS original_sale_price,
      s.created_date AS sale_date
    FROM zs_observe.target_returns r
    LEFT JOIN zs_observe.target_sales s
      ON r.order_id = s.order_id
      AND r.tcin = s.tcin
      AND s.is_active = true
    WHERE r.is_active = true
      AND r.internal_txn_type = 'reverse';
  required_tables:
  - table.zs_observe.target_returns
  - table.zs_observe.target_sales
  output_aliases_detected:
  - return_reason
  - refund_amount
  - original_sale_price
  - sale_date
  confidence: high
```
```yaml
sql_pattern:
  id: sql.target_plus.returns.7_5_sku_level_return_rate
  source_section: 7.5 SKU-Level Return Rate
  source_context: returns
  source_line_start: 1454
  source_line_end: 1471
  evidence_ref: ev.target_plus.returns.7_5_sku_level_return_rate
  sql_pattern: |-
    SELECT
      r.tcin,
      m.brand,
      COUNT(DISTINCT r.order_id) AS returns,
      COUNT(DISTINCT s.order_id) AS sales,
      ROUND(100.0 * COUNT(DISTINCT r.order_id)
        / NULLIF(COUNT(DISTINCT s.order_id), 0), 2) AS return_rate_pct
    FROM zs_observe.target_returns r
    LEFT JOIN zs_observe.target_sales s
      ON r.tcin = s.tcin AND s.is_active = true AND s.order_status = 'SHIPPED'
    LEFT JOIN zs_observe.target_tcin_mapping m
      ON r.tcin = m.tcin AND m.is_active = true
    WHERE r.is_active = true AND r.internal_txn_type = 'reverse'
    GROUP BY r.tcin, m.brand
    HAVING COUNT(DISTINCT s.order_id) > 5
    ORDER BY return_rate_pct DESC;
  required_tables:
  - table.zs_observe.target_returns
  - table.zs_observe.target_sales
  - table.zs_observe.target_tcin_mapping
  output_aliases_detected:
  - returns
  - sales
  - return_rate_pct
  confidence: high
```
```yaml
sql_pattern:
  id: sql.target_plus.sales.7_1_monthly_sales_gmv_by_brand
  source_section: 7.1 Monthly Sales GMV by Brand
  source_context: sales
  source_line_start: 1663
  source_line_end: 1675
  evidence_ref: ev.target_plus.sales.7_1_monthly_sales_gmv_by_brand
  sql_pattern: |-
    SELECT
      DATE_TRUNC('month', created_date) AS month,
      brand,
      COUNT(*) AS orders,
      SUM(charged_amount) AS gmv,
      SUM(discount_amount) AS discounts,
      AVG(charged_amount) AS aov
    FROM zs_observe.target_sales
    WHERE is_active = true AND order_status = 'SHIPPED'
    GROUP BY 1, 2
    ORDER BY 1, 2;
  required_tables:
  - table.zs_observe.target_sales
  output_aliases_detected:
  - month
  - orders
  - gmv
  - discounts
  - aov
  confidence: high
```
```yaml
sql_pattern:
  id: sql.target_plus.sales.7_2_sku_level_sales_performance
  source_section: 7.2 SKU-Level Sales Performance
  source_context: sales
  source_line_start: 1679
  source_line_end: 1690
  evidence_ref: ev.target_plus.sales.7_2_sku_level_sales_performance
  sql_pattern: |-
    SELECT
      s.tcin, s.sku_id, m.brand,
      COUNT(*) AS units_sold,
      SUM(s.charged_amount) AS revenue,
      SUM(s.discount_amount) AS discounts
    FROM zs_observe.target_sales s
    LEFT JOIN zs_observe.target_tcin_mapping m ON s.tcin = m.tcin AND m.is_active = true
    WHERE s.is_active = true AND s.order_status = 'SHIPPED'
    GROUP BY s.tcin, s.sku_id, m.brand
    ORDER BY units_sold DESC;
  required_tables:
  - table.zs_observe.target_sales
  - table.zs_observe.target_tcin_mapping
  output_aliases_detected:
  - units_sold
  - revenue
  - discounts
  confidence: high
```
```yaml
sql_pattern:
  id: sql.target_plus.sales.7_3_sales_settlement_join
  source_section: 7.3 Sales → Settlement Join
  source_context: sales
  source_line_start: 1694
  source_line_end: 1702
  evidence_ref: ev.target_plus.sales.7_3_sales_settlement_join
  sql_pattern: |-
    SELECT
      s.order_id, s.item_id, s.charged_amount AS sales_price,
      st.settled_amount, st.gross_commission, st.gross_commission_percentage
    FROM zs_observe.target_sales s
    LEFT JOIN zs_observe.target_settlement st
      ON s.item_id = st.item_id AND st.is_active = true
    WHERE s.is_active = true AND s.order_status = 'SHIPPED';
  required_tables:
  - table.zs_observe.target_sales
  - table.zs_observe.target_settlement
  output_aliases_detected:
  - sales_price
  confidence: high
```
```yaml
sql_pattern:
  id: sql.target_plus.sales.7_4_return_rate_by_brand
  source_section: 7.4 Return Rate by Brand
  source_context: sales
  source_line_start: 1706
  source_line_end: 1718
  evidence_ref: ev.target_plus.sales.7_4_return_rate_by_brand
  sql_pattern: |-
    SELECT
      s.brand,
      COUNT(DISTINCT s.order_id) AS sold_orders,
      COUNT(DISTINCT r.order_id) AS returned_orders,
      ROUND(100.0 * COUNT(DISTINCT r.order_id)
        / NULLIF(COUNT(DISTINCT s.order_id), 0), 2) AS return_rate_pct
    FROM zs_observe.target_sales s
    LEFT JOIN zs_observe.target_returns r
      ON s.order_id = r.order_id AND r.is_active = true
    WHERE s.is_active = true AND s.order_status = 'SHIPPED'
    GROUP BY s.brand;
  required_tables:
  - table.zs_observe.target_returns
  - table.zs_observe.target_sales
  output_aliases_detected:
  - sold_orders
  - returned_orders
  - return_rate_pct
  confidence: high
```
## 4. Candidate Cards

### 4.1 platform

```yaml
candidate_card:
  card_type: platform
  card_id: platform.target_plus
  display_name: Target Plus
  canonical_name: Target Plus
  aliases:
  - Target Plus
  - Target+
  - Target.com Plus
  marketplace_category: curated_invite_only_us_ecommerce_marketplace
  operator_or_parent_context: Target Corporation context is preserved as source evidence only; no platform-account card emitted.
  evidence_refs:
  - ev.target_plus.marketplace.1_1_background
  confidence: high
  review_status: ready
```
### 4.2 platform_context

```yaml
candidate_card:
  card_type: platform_context
  card_id: platform_context.target_plus.us
  display_name: Target Plus United States marketplace context
  platform_id: platform.target_plus
  country_code: US
  currency: USD
  timezone: America/Chicago_or_US_marketplace_context
  marketplace_model: invite_only_curated_us_marketplace_with_seller_self_fulfilment_and_Target_MPFTax_model
  tax_model: US marketplace facilitator model; Target collects/remits sales tax; total_tax is 0 in seller settlement.
  scope_note: Marketplace-vendor semantic context only. group_level_id=123 is a documented filter/column; runtime account binding is
    external.
  evidence_refs:
  - ev.target_plus.marketplace.1_1_background
  - ev.target_plus.marketplace.1_3_seller_entities_in_dataset
  confidence: high
  review_status: ready
```
### 4.3 domain

```yaml
candidate_card:
  card_type: domain
  card_id: domain.target_plus.orders
  display_name: Target Plus order, OMS, forward sales, status, RedCard-discount, and order-line semantics
  domain_family: orders
  platform_context_id: platform_context.target_plus.us
  scope_note: Marketplace-vendor semantics only; external-domain card creation is forbidden in this markdown.
  evidence_refs:
  - ev.target_plus.marketplace.1_1_background
  confidence: high
  review_status: ready
```
```yaml
candidate_card:
  card_type: domain
  card_id: domain.target_plus.settlement
  display_name: Target Plus one-row-per-order-line/event settlement, Stripe transfer/payout, commission, payout and tax-adjustment semantics
  domain_family: settlement
  platform_context_id: platform_context.target_plus.us
  scope_note: Marketplace-vendor semantics only; external-domain card creation is forbidden in this markdown.
  evidence_refs:
  - ev.target_plus.marketplace.1_1_background
  confidence: high
  review_status: ready
```
```yaml
candidate_card:
  card_type: domain
  card_id: domain.target_plus.returns
  display_name: Target Plus return, reverse, refund, return-reason, and customer-return handling semantics
  domain_family: returns
  platform_context_id: platform_context.target_plus.us
  scope_note: Marketplace-vendor semantics only; external-domain card creation is forbidden in this markdown.
  evidence_refs:
  - ev.target_plus.marketplace.1_1_background
  confidence: high
  review_status: ready
```
```yaml
candidate_card:
  card_type: domain
  card_id: domain.target_plus.mapping_enrichment
  display_name: Target Plus TCIN/SKU/ASIN/barcode/brand product mapping and enrichment semantics
  domain_family: mapping_enrichment
  platform_context_id: platform_context.target_plus.us
  scope_note: Marketplace-vendor semantics only; external-domain card creation is forbidden in this markdown.
  evidence_refs:
  - ev.target_plus.marketplace.1_1_background
  confidence: high
  review_status: ready
```
```yaml
candidate_card:
  card_type: domain
  card_id: domain.target_plus.fees
  display_name: Target Plus referral fee, commission, shipping amount, payout-ratio, and zero monthly/listing/fulfillment fee semantics
  domain_family: fees
  platform_context_id: platform_context.target_plus.us
  scope_note: Marketplace-vendor semantics only; external-domain card creation is forbidden in this markdown.
  evidence_refs:
  - ev.target_plus.marketplace.1_1_background
  confidence: high
  review_status: ready
```
```yaml
candidate_card:
  card_type: domain
  card_id: domain.target_plus.tax
  display_name: Target Plus US marketplace-facilitator sales-tax and no-Indian-TCS/TDS semantics, not statutory filing
  domain_family: tax
  platform_context_id: platform_context.target_plus.us
  scope_note: Marketplace-vendor semantics only; external-domain card creation is forbidden in this markdown.
  evidence_refs:
  - ev.target_plus.marketplace.1_1_background
  confidence: high
  review_status: ready
```
```yaml
candidate_card:
  card_type: domain
  card_id: domain.target_plus.fulfillment
  display_name: Target Plus seller self-fulfilment, approved carrier, and return logistics context as marketplace caveats only
  domain_family: fulfillment
  platform_context_id: platform_context.target_plus.us
  scope_note: Marketplace-vendor semantics only; external-domain card creation is forbidden in this markdown.
  evidence_refs:
  - ev.target_plus.marketplace.1_1_background
  confidence: high
  review_status: ready
```
```yaml
candidate_card:
  card_type: domain
  card_id: domain.target_plus.payment
  display_name: Target Plus Stripe identifier and payout-batch semantics, not payment-gateway account cards
  domain_family: payment
  platform_context_id: platform_context.target_plus.us
  scope_note: Marketplace-vendor semantics only; external-domain card creation is forbidden in this markdown.
  evidence_refs:
  - ev.target_plus.marketplace.1_1_background
  confidence: high
  review_status: ready
```
```yaml
candidate_card:
  card_type: domain
  card_id: domain.target_plus.reconciliation
  display_name: Target Plus marketplace-internal reconciliation semantics
  domain_family: reconciliation
  platform_context_id: platform_context.target_plus.us
  scope_note: Marketplace-vendor semantics only; external-domain card creation is forbidden in this markdown.
  evidence_refs:
  - ev.target_plus.marketplace.1_1_background
  confidence: high
  review_status: ready
```
```yaml
candidate_card:
  card_type: domain
  card_id: domain.target_plus.query_guidance
  display_name: Target Plus parser query, filter, validation, SQL, and output guidance
  domain_family: query_guidance
  platform_context_id: platform_context.target_plus.us
  scope_note: Marketplace-vendor semantics only; external-domain card creation is forbidden in this markdown.
  evidence_refs:
  - ev.target_plus.marketplace.1_1_background
  confidence: high
  review_status: ready
```
### 4.4 table

```yaml
candidate_card:
  card_type: table
  card_id: table.zs_observe.target_sales
  display_name: zs_observe.target_sales
  schema: zs_observe
  table_name: target_sales
  table_role: orders_sales
  business_purpose: Forward OMS/order-line table for Target Plus sales; source for GMV, sales velocity, settlement and returns joins.
  semantic_domain_id: domain.target_plus.orders
  grain: forward_order_line_item
  row_count_evidence: 9,063 total / 7,291 active
  date_range: 2025-04-22 to 2025-12-31
  primary_key_candidates:
  - item_id
  - unique_id
  join_key_candidates:
  - item_id
  - tcin
  - order_id
  documented_scope_values:
    group_level_id: 123
    entity: Mensa brand group
    brands:
    - folkculture
    - katchon
  mandatory_filters:
  - is_active = true
  - group_level_id = 123
  - order_status = SHIPPED for shipped-sales metrics
  scope_caveats: group_level_id/seller/entity/brand/Stripe/carrier values are columns, filters, identifiers, caveats, or source evidence
    only; no account/bank/logistics/payment-gateway cards emitted.
  join_caveat: Use item_id for sales-settlement reconciliation, order_id for sales-returns, and tcin for mapping enrichment.
  evidence_refs:
  - ev.target_plus.sales.1_table_overview
  - ev.target_plus.sales.2_key_statistics
  - ev.target_plus.sales.3_schema_details_29_columns
  confidence: high
  review_status: ready
```
```yaml
candidate_card:
  card_type: table
  card_id: table.zs_observe.target_returns
  display_name: zs_observe.target_returns
  schema: zs_observe
  table_name: target_returns
  table_role: returns
  business_purpose: Return tracking table for Target Plus buyer returns, refund events, return reasons, carrier tracking, and reverse
    transaction context.
  semantic_domain_id: domain.target_plus.returns
  grain: return_or_refund_order_line_event
  row_count_evidence: 1,247 total / 1,179 active
  date_range: created_date 2025-05-05 to 2025-12-31; returned_date 2025-05-15 to 2026-02-16
  primary_key_candidates:
  - item_id
  - unique_id
  join_key_candidates:
  - order_id
  - item_id
  - tcin
  documented_scope_values:
    group_level_id: 123
    entity: Mensa brand group
    brands:
    - folkculture
    - katchon
  mandatory_filters:
  - is_active = true
  - group_level_id = 123
  - internal_txn_type = reverse for confirmed return events
  scope_caveats: group_level_id/seller/entity/brand/Stripe/carrier values are columns, filters, identifiers, caveats, or source evidence
    only; no account/bank/logistics/payment-gateway cards emitted.
  join_caveat: Use order_id for sales-return analysis; use item_id for returns-settlement refund match; use tcin for mapping enrichment.
  evidence_refs:
  - ev.target_plus.returns.1_table_overview
  - ev.target_plus.returns.2_key_statistics
  - ev.target_plus.returns.3_schema_details_30_columns
  confidence: high
  review_status: ready
```
```yaml
candidate_card:
  card_type: table
  card_id: table.zs_observe.target_settlement
  display_name: zs_observe.target_settlement
  schema: zs_observe
  table_name: target_settlement
  table_role: settlement
  business_purpose: Financial settlement and payout ledger for Target Plus; one row per order line per event with Stripe transfer, payout,
    commission, shipping, refund and reverse-charge tax-adjustment fields.
  semantic_domain_id: domain.target_plus.settlement
  grain: settlement_order_line_event
  row_count_evidence: 6,517 total / 6,517 active
  date_range: created_date 2025-04-22 to 2025-11-27; returned_date 2025-05-19 to 2025-11-30
  primary_key_candidates:
  - transfer_id
  - unique_id
  join_key_candidates:
  - item_id
  - order_id
  - payout_id
  - tcin
  documented_scope_values:
    group_level_id: 123
    entity: Mensa brand group
  mandatory_filters:
  - is_active = true
  - group_level_id = 123
  - transaction_type = forward for forward-settlement metrics
  scope_caveats: group_level_id/seller/entity/brand/Stripe/carrier values are columns, filters, identifiers, caveats, or source evidence
    only; no account/bank/logistics/payment-gateway cards emitted.
  join_caveat: Settlement ends Nov 2025 while sales run through Dec 2025; date-align periods before coverage assertions.
  evidence_refs:
  - ev.target_plus.settlement.1_table_overview_2
  - ev.target_plus.settlement.2_key_statistics_2
  - ev.target_plus.settlement.3_schema_details_37_columns_2
  confidence: high
  review_status: ready
```
```yaml
candidate_card:
  card_type: table
  card_id: table.zs_observe.target_tcin_mapping
  display_name: zs_observe.target_tcin_mapping
  schema: zs_observe
  table_name: target_tcin_mapping
  table_role: product_mapping
  business_purpose: Product catalogue cross-reference table mapping Target TCIN to clean seller SKU, ASIN, barcode, and brand.
  semantic_domain_id: domain.target_plus.mapping_enrichment
  grain: tcin_product_variant
  row_count_evidence: 331 total / 331 active
  date_range: not specified by source
  primary_key_candidates:
  - tcin
  - unique_id
  join_key_candidates:
  - tcin
  - sku_id
  - asin
  documented_scope_values:
    group_level_id: 123
    brands:
    - Folkculture
    - Katchon
  mandatory_filters:
  - is_active = true
  - group_level_id = 123
  scope_caveats: group_level_id/seller/entity/brand/Stripe/carrier values are columns, filters, identifiers, caveats, or source evidence
    only; no account/bank/logistics/payment-gateway cards emitted.
  join_caveat: Join sales/returns/settlement through tcin. Do not assume Shopify-format sku_id in sales/returns equals clean seller
    sku_id.
  evidence_refs:
  - ev.target_plus.mapping.1_table_overview
  - ev.target_plus.mapping.2_key_statistics
  - ev.target_plus.mapping.3_schema_details_21_columns
  confidence: high
  review_status: ready
```
### 4.5 column

```yaml
candidate_card:
  card_type: column
  card_id: column.zs_observe.target_settlement.unique_id
  display_name: target_settlement.unique_id
  table_id: table.zs_observe.target_settlement
  schema: zs_observe
  table_name: target_settlement
  column_name: unique_id
  source_declared_type: varchar
  data_type: varchar
  column_group: 3.1 Identity Columns
  description: Row identifier
  semantic_role: identity_or_join_key
  is_key: true
  is_amount: false
  is_date: false
  is_status: false
  is_scope_field: false
  evidence_refs:
  - ev.target_plus.settlement.3_schema_details_37_columns_2
  confidence: high
  review_status: ready
```
```yaml
candidate_card:
  card_type: column
  card_id: column.zs_observe.target_settlement.txn_uuid
  display_name: target_settlement.txn_uuid
  table_id: table.zs_observe.target_settlement
  schema: zs_observe
  table_name: target_settlement
  column_name: txn_uuid
  source_declared_type: varchar
  data_type: varchar
  column_group: 3.1 Identity Columns
  description: Pipeline UUID
  semantic_role: identity_or_join_key
  is_key: true
  is_amount: false
  is_date: false
  is_status: false
  is_scope_field: false
  evidence_refs:
  - ev.target_plus.settlement.3_schema_details_37_columns_2
  confidence: high
  review_status: ready
```
```yaml
candidate_card:
  card_type: column
  card_id: column.zs_observe.target_settlement.unique_value
  display_name: target_settlement.unique_value
  table_id: table.zs_observe.target_settlement
  schema: zs_observe
  table_name: target_settlement
  column_name: unique_value
  source_declared_type: varchar
  data_type: varchar
  column_group: 3.1 Identity Columns
  description: Dedup hash
  semantic_role: financial_amount_or_rate
  is_key: true
  is_amount: true
  is_date: false
  is_status: false
  is_scope_field: false
  evidence_refs:
  - ev.target_plus.settlement.3_schema_details_37_columns_2
  confidence: high
  review_status: ready
```
```yaml
candidate_card:
  card_type: column
  card_id: column.zs_observe.target_settlement.transfer_id
  display_name: target_settlement.transfer_id
  table_id: table.zs_observe.target_settlement
  schema: zs_observe
  table_name: target_settlement
  column_name: transfer_id
  source_declared_type: varchar
  data_type: varchar
  column_group: 3.1 Identity Columns
  description: '**Stripe transfer ID** (format: `tr_1SZX8wGxFTvW7WRNvTtE2N46`) — unique per row'
  semantic_role: identity_or_join_key
  is_key: true
  is_amount: false
  is_date: false
  is_status: false
  is_scope_field: false
  evidence_refs:
  - ev.target_plus.settlement.3_schema_details_37_columns_2
  confidence: high
  review_status: ready
```
```yaml
candidate_card:
  card_type: column
  card_id: column.zs_observe.target_settlement.payout_id
  display_name: target_settlement.payout_id
  table_id: table.zs_observe.target_settlement
  schema: zs_observe
  table_name: target_settlement
  column_name: payout_id
  source_declared_type: varchar
  data_type: varchar
  column_group: 3.1 Identity Columns
  description: '**Stripe payout ID** (format: `po_1SZh3kGgYJvT8MDtnFnpYLpX`) — groups rows into payment batches'
  semantic_role: financial_amount_or_rate
  is_key: true
  is_amount: true
  is_date: false
  is_status: false
  is_scope_field: false
  evidence_refs:
  - ev.target_plus.settlement.3_schema_details_37_columns_2
  confidence: high
  review_status: ready
```
```yaml
candidate_card:
  card_type: column
  card_id: column.zs_observe.target_settlement.payment_id
  display_name: target_settlement.payment_id
  table_id: table.zs_observe.target_settlement
  schema: zs_observe
  table_name: target_settlement
  column_name: payment_id
  source_declared_type: varchar
  data_type: varchar
  column_group: 3.1 Identity Columns
  description: '**Stripe payment charge ID** (format: `py_1SZX8wGgYJvT8MDtfSfVtQYV`)'
  semantic_role: identity_or_join_key
  is_key: true
  is_amount: false
  is_date: false
  is_status: false
  is_scope_field: false
  evidence_refs:
  - ev.target_plus.settlement.3_schema_details_37_columns_2
  confidence: high
  review_status: ready
```
```yaml
candidate_card:
  card_type: column
  card_id: column.zs_observe.target_settlement.order_id
  display_name: target_settlement.order_id
  table_id: table.zs_observe.target_settlement
  schema: zs_observe
  table_name: target_settlement
  column_name: order_id
  source_declared_type: varchar
  data_type: varchar
  column_group: 3.1 Identity Columns
  description: Target order number — **join key to sales and returns**
  semantic_role: identity_or_join_key
  is_key: true
  is_amount: false
  is_date: false
  is_status: false
  is_scope_field: false
  evidence_refs:
  - ev.target_plus.settlement.3_schema_details_37_columns_2
  confidence: high
  review_status: ready
```
```yaml
candidate_card:
  card_type: column
  card_id: column.zs_observe.target_settlement.item_id
  display_name: target_settlement.item_id
  table_id: table.zs_observe.target_settlement
  schema: zs_observe
  table_name: target_settlement
  column_name: item_id
  source_declared_type: varchar
  data_type: varchar
  column_group: 3.1 Identity Columns
  description: Order line item ID — **join key to sales and returns**
  semantic_role: identity_or_join_key
  is_key: true
  is_amount: false
  is_date: false
  is_status: false
  is_scope_field: false
  evidence_refs:
  - ev.target_plus.settlement.3_schema_details_37_columns_2
  confidence: high
  review_status: ready
```
```yaml
candidate_card:
  card_type: column
  card_id: column.zs_observe.target_settlement.sku_id
  display_name: target_settlement.sku_id
  table_id: table.zs_observe.target_settlement
  schema: zs_observe
  table_name: target_settlement
  column_name: sku_id
  source_declared_type: varchar
  data_type: varchar
  column_group: 3.1 Identity Columns
  description: Seller SKU (Shopify format)
  semantic_role: identity_or_join_key
  is_key: true
  is_amount: false
  is_date: false
  is_status: false
  is_scope_field: false
  evidence_refs:
  - ev.target_plus.settlement.3_schema_details_37_columns_2
  confidence: high
  review_status: ready
```
```yaml
candidate_card:
  card_type: column
  card_id: column.zs_observe.target_settlement.tcin
  display_name: target_settlement.tcin
  table_id: table.zs_observe.target_settlement
  schema: zs_observe
  table_name: target_settlement
  column_name: tcin
  source_declared_type: varchar
  data_type: varchar
  column_group: 3.1 Identity Columns
  description: Target TCIN — **join key to tcin_mapping**
  semantic_role: identity_or_join_key
  is_key: true
  is_amount: false
  is_date: false
  is_status: false
  is_scope_field: false
  evidence_refs:
  - ev.target_plus.settlement.3_schema_details_37_columns_2
  confidence: high
  review_status: ready
```
```yaml
candidate_card:
  card_type: column
  card_id: column.zs_observe.target_settlement.created_date
  display_name: target_settlement.created_date
  table_id: table.zs_observe.target_settlement
  schema: zs_observe
  table_name: target_settlement
  column_name: created_date
  source_declared_type: date
  data_type: date
  column_group: 3.2 Date Columns
  description: Settlement transaction date
  semantic_role: date_time
  is_key: false
  is_amount: false
  is_date: true
  is_status: false
  is_scope_field: false
  evidence_refs:
  - ev.target_plus.settlement.3_schema_details_37_columns_2
  confidence: high
  review_status: ready
```
```yaml
candidate_card:
  card_type: column
  card_id: column.zs_observe.target_settlement.returned_date
  display_name: target_settlement.returned_date
  table_id: table.zs_observe.target_settlement
  schema: zs_observe
  table_name: target_settlement
  column_name: returned_date
  source_declared_type: date
  data_type: date
  column_group: 3.2 Date Columns
  description: Return date (populated for reverse transactions)
  semantic_role: date_time
  is_key: false
  is_amount: false
  is_date: true
  is_status: false
  is_scope_field: false
  evidence_refs:
  - ev.target_plus.settlement.3_schema_details_37_columns_2
  confidence: high
  review_status: ready
```
```yaml
candidate_card:
  card_type: column
  card_id: column.zs_observe.target_settlement.charged_amount
  display_name: target_settlement.charged_amount
  table_id: table.zs_observe.target_settlement
  schema: zs_observe
  table_name: target_settlement
  column_name: charged_amount
  source_declared_type: decimal
  data_type: decimal
  column_group: 3.3 Financial Columns
  description: '**Per-unit sale price** (USD)'
  semantic_role: financial_amount_or_rate
  is_key: false
  is_amount: true
  is_date: false
  is_status: false
  is_scope_field: false
  evidence_refs:
  - ev.target_plus.settlement.3_schema_details_37_columns_2
  confidence: high
  review_status: ready
  sign_convention: Per-unit sale/refund/tax-base value; do not substitute for charged_amount_excluding_tax when quantity > 1.
```
```yaml
candidate_card:
  card_type: column
  card_id: column.zs_observe.target_settlement.charged_amount_excluding_tax
  display_name: target_settlement.charged_amount_excluding_tax
  table_id: table.zs_observe.target_settlement
  schema: zs_observe
  table_name: target_settlement
  column_name: charged_amount_excluding_tax
  source_declared_type: decimal
  data_type: decimal
  column_group: 3.3 Financial Columns
  description: '**Total order value net of tax** — for multi-qty orders: `charged_amount × quantity`; also used for refund totals'
  semantic_role: financial_amount_or_rate
  is_key: false
  is_amount: true
  is_date: false
  is_status: false
  is_scope_field: false
  evidence_refs:
  - ev.target_plus.settlement.3_schema_details_37_columns_2
  confidence: high
  review_status: ready
  sign_convention: Total order/refund value net of tax; use for revenue base, especially multi-quantity orders.
```
```yaml
candidate_card:
  card_type: column
  card_id: column.zs_observe.target_settlement.total_tax
  display_name: target_settlement.total_tax
  table_id: table.zs_observe.target_settlement
  schema: zs_observe
  table_name: target_settlement
  column_name: total_tax
  source_declared_type: decimal
  data_type: decimal
  column_group: 3.3 Financial Columns
  description: Tax amount — **₹0.00 for all rows** (Target collects and remits sales tax on behalf of sellers)
  semantic_role: financial_amount_or_rate
  is_key: false
  is_amount: true
  is_date: false
  is_status: false
  is_scope_field: false
  evidence_refs:
  - ev.target_plus.settlement.3_schema_details_37_columns_2
  confidence: high
  review_status: ready
  sign_convention: Always 0 because Target acts as marketplace facilitator and tax is invisible to seller settlement.
```
```yaml
candidate_card:
  card_type: column
  card_id: column.zs_observe.target_settlement.shipping_amount
  display_name: target_settlement.shipping_amount
  table_id: table.zs_observe.target_settlement
  schema: zs_observe
  table_name: target_settlement
  column_name: shipping_amount
  source_declared_type: decimal
  data_type: decimal
  column_group: 3.3 Financial Columns
  description: Shipping fee charged to buyer (if any)
  semantic_role: financial_amount_or_rate
  is_key: false
  is_amount: true
  is_date: false
  is_status: false
  is_scope_field: false
  evidence_refs:
  - ev.target_plus.settlement.3_schema_details_37_columns_2
  confidence: high
  review_status: ready
  sign_convention: Shipping amount charged to buyer when present; included before commission in forward payout waterfall.
```
```yaml
candidate_card:
  card_type: column
  card_id: column.zs_observe.target_settlement.gross_commission
  display_name: target_settlement.gross_commission
  table_id: table.zs_observe.target_settlement
  schema: zs_observe
  table_name: target_settlement
  column_name: gross_commission
  source_declared_type: decimal
  data_type: decimal
  column_group: 3.3 Financial Columns
  description: '**Commission charged by Target** (15% of `charged_amount_excluding_tax`)'
  semantic_role: financial_amount_or_rate
  is_key: false
  is_amount: true
  is_date: false
  is_status: false
  is_scope_field: false
  evidence_refs:
  - ev.target_plus.settlement.3_schema_details_37_columns_2
  confidence: high
  review_status: ready
  sign_convention: Forward rows charge 15% commission; reverse rows reverse commission credit; reverse charge rows have 0 commission.
```
```yaml
candidate_card:
  card_type: column
  card_id: column.zs_observe.target_settlement.settled_amount
  display_name: target_settlement.settled_amount
  table_id: table.zs_observe.target_settlement
  schema: zs_observe
  table_name: target_settlement
  column_name: settled_amount
  source_declared_type: decimal
  data_type: decimal
  column_group: 3.3 Financial Columns
  description: '**Net payout to seller** = `charged_amount_excluding_tax` + `shipping_amount` − `gross_commission`'
  semantic_role: financial_amount_or_rate
  is_key: false
  is_amount: true
  is_date: false
  is_status: false
  is_scope_field: false
  evidence_refs:
  - ev.target_plus.settlement.3_schema_details_37_columns_2
  confidence: high
  review_status: ready
  sign_convention: Forward rows are positive seller payout; reverse rows are negative refund adjustment; reverse charge rows are negative
    tax adjustment.
```
```yaml
candidate_card:
  card_type: column
  card_id: column.zs_observe.target_settlement.gross_commission_percentage
  display_name: target_settlement.gross_commission_percentage
  table_id: table.zs_observe.target_settlement
  schema: zs_observe
  table_name: target_settlement
  column_name: gross_commission_percentage
  source_declared_type: decimal
  data_type: decimal
  column_group: 3.3 Financial Columns
  description: Commission rate — **0.1500** (15%) for all forward/reverse rows; 0 for reverse charge rows
  semantic_role: financial_amount_or_rate
  is_key: false
  is_amount: true
  is_date: false
  is_status: false
  is_scope_field: false
  evidence_refs:
  - ev.target_plus.settlement.3_schema_details_37_columns_2
  confidence: high
  review_status: ready
  sign_convention: 0.1500 for forward/reverse product rows; 0 for reverse charge tax-adjustment rows.
```
```yaml
candidate_card:
  card_type: column
  card_id: column.zs_observe.target_settlement.transaction_type
  display_name: target_settlement.transaction_type
  table_id: table.zs_observe.target_settlement
  schema: zs_observe
  table_name: target_settlement
  column_name: transaction_type
  source_declared_type: varchar
  data_type: varchar
  column_group: 3.4 Classification Columns
  description: '`forward`, `reverse`, or `reverse charge`'
  semantic_role: classification_status_or_type
  is_key: false
  is_amount: false
  is_date: false
  is_status: true
  is_scope_field: false
  evidence_refs:
  - ev.target_plus.settlement.3_schema_details_37_columns_2
  confidence: high
  review_status: ready
```
```yaml
candidate_card:
  card_type: column
  card_id: column.zs_observe.target_settlement.internal_txn_type
  display_name: target_settlement.internal_txn_type
  table_id: table.zs_observe.target_settlement
  schema: zs_observe
  table_name: target_settlement
  column_name: internal_txn_type
  source_declared_type: varchar
  data_type: varchar
  column_group: 3.4 Classification Columns
  description: '`sales`, `refunds`, or `others`'
  semantic_role: classification_status_or_type
  is_key: false
  is_amount: false
  is_date: false
  is_status: true
  is_scope_field: false
  evidence_refs:
  - ev.target_plus.settlement.3_schema_details_37_columns_2
  confidence: high
  review_status: ready
```
```yaml
candidate_card:
  card_type: column
  card_id: column.zs_observe.target_settlement.description
  display_name: target_settlement.description
  table_id: table.zs_observe.target_settlement
  schema: zs_observe
  table_name: target_settlement
  column_name: description
  source_declared_type: integer
  data_type: integer
  column_group: 3.4 Classification Columns
  description: Description code (stored as integer — typically NULL)
  semantic_role: general_marketplace_attribute
  is_key: false
  is_amount: false
  is_date: false
  is_status: false
  is_scope_field: false
  evidence_refs:
  - ev.target_plus.settlement.3_schema_details_37_columns_2
  confidence: high
  review_status: ready
```
```yaml
candidate_card:
  card_type: column
  card_id: column.zs_observe.target_settlement.brand
  display_name: target_settlement.brand
  table_id: table.zs_observe.target_settlement
  schema: zs_observe
  table_name: target_settlement
  column_name: brand
  source_declared_type: varchar
  data_type: varchar
  column_group: 3.4 Classification Columns
  description: '`folkculture`, `katchon`, or NULL'
  semantic_role: general_marketplace_attribute
  is_key: false
  is_amount: false
  is_date: false
  is_status: false
  is_scope_field: false
  evidence_refs:
  - ev.target_plus.settlement.3_schema_details_37_columns_2
  confidence: high
  review_status: ready
```
```yaml
candidate_card:
  card_type: column
  card_id: column.zs_observe.target_settlement.quantity
  display_name: target_settlement.quantity
  table_id: table.zs_observe.target_settlement
  schema: zs_observe
  table_name: target_settlement
  column_name: quantity
  source_declared_type: integer
  data_type: integer
  column_group: 3.4 Classification Columns
  description: Quantity settled
  semantic_role: general_marketplace_attribute
  is_key: false
  is_amount: false
  is_date: false
  is_status: false
  is_scope_field: false
  evidence_refs:
  - ev.target_plus.settlement.3_schema_details_37_columns_2
  confidence: high
  review_status: ready
```
```yaml
candidate_card:
  card_type: column
  card_id: column.zs_observe.target_settlement.group_level_id
  display_name: target_settlement.group_level_id
  table_id: table.zs_observe.target_settlement
  schema: zs_observe
  table_name: target_settlement
  column_name: group_level_id
  source_declared_type: integer
  data_type: integer
  column_group: 3.5 System / Metadata Columns
  description: '`123`'
  semantic_role: scope_identifier_column
  is_key: true
  is_amount: false
  is_date: false
  is_status: false
  is_scope_field: true
  evidence_refs:
  - ev.target_plus.settlement.3_schema_details_37_columns_2
  confidence: high
  review_status: ready
  scope_note: Documented marketplace scope identifier retained as column/filter value only; do not emit tenant/group/account cards.
```
```yaml
candidate_card:
  card_type: column
  card_id: column.zs_observe.target_settlement.currency_type
  display_name: target_settlement.currency_type
  table_id: table.zs_observe.target_settlement
  schema: zs_observe
  table_name: target_settlement
  column_name: currency_type
  source_declared_type: varchar
  data_type: varchar
  column_group: 3.5 System / Metadata Columns
  description: '`INR` (label; values are USD)'
  semantic_role: classification_status_or_type
  is_key: false
  is_amount: false
  is_date: false
  is_status: true
  is_scope_field: false
  evidence_refs:
  - ev.target_plus.settlement.3_schema_details_37_columns_2
  confidence: high
  review_status: ready
```
```yaml
candidate_card:
  card_type: column
  card_id: column.zs_observe.target_settlement.is_active
  display_name: target_settlement.is_active
  table_id: table.zs_observe.target_settlement
  schema: zs_observe
  table_name: target_settlement
  column_name: is_active
  source_declared_type: boolean
  data_type: boolean
  column_group: 3.5 System / Metadata Columns
  description: Always `true`
  semantic_role: general_marketplace_attribute
  is_key: false
  is_amount: false
  is_date: false
  is_status: false
  is_scope_field: false
  evidence_refs:
  - ev.target_plus.settlement.3_schema_details_37_columns_2
  confidence: high
  review_status: ready
```
```yaml
candidate_card:
  card_type: column
  card_id: column.zs_observe.target_settlement.zen_sheet_name
  display_name: target_settlement.zen_sheet_name
  table_id: table.zs_observe.target_settlement
  schema: zs_observe
  table_name: target_settlement
  column_name: zen_sheet_name
  source_declared_type: varchar
  data_type: varchar
  column_group: 3.5 System / Metadata Columns
  description: Source sheet
  semantic_role: general_marketplace_attribute
  is_key: false
  is_amount: false
  is_date: false
  is_status: false
  is_scope_field: false
  evidence_refs:
  - ev.target_plus.settlement.3_schema_details_37_columns_2
  confidence: high
  review_status: ready
```
```yaml
candidate_card:
  card_type: column
  card_id: column.zs_observe.target_settlement.created_at
  display_name: target_settlement.created_at
  table_id: table.zs_observe.target_settlement
  schema: zs_observe
  table_name: target_settlement
  column_name: created_at
  source_declared_type: timestamp
  data_type: timestamp
  column_group: 3.5 System / Metadata Columns
  description: Timestamps
  semantic_role: date_time
  is_key: false
  is_amount: false
  is_date: true
  is_status: false
  is_scope_field: false
  evidence_refs:
  - ev.target_plus.settlement.3_schema_details_37_columns_2
  confidence: high
  review_status: ready
```
```yaml
candidate_card:
  card_type: column
  card_id: column.zs_observe.target_settlement.updated_at
  display_name: target_settlement.updated_at
  table_id: table.zs_observe.target_settlement
  schema: zs_observe
  table_name: target_settlement
  column_name: updated_at
  source_declared_type: timestamp
  data_type: timestamp
  column_group: 3.5 System / Metadata Columns
  description: Timestamps
  semantic_role: date_time
  is_key: false
  is_amount: false
  is_date: true
  is_status: false
  is_scope_field: false
  evidence_refs:
  - ev.target_plus.settlement.3_schema_details_37_columns_2
  confidence: high
  review_status: ready
```
```yaml
candidate_card:
  card_type: column
  card_id: column.zs_observe.target_settlement.deleted_at
  display_name: target_settlement.deleted_at
  table_id: table.zs_observe.target_settlement
  schema: zs_observe
  table_name: target_settlement
  column_name: deleted_at
  source_declared_type: varchar
  data_type: varchar
  column_group: 3.5 System / Metadata Columns
  description: Soft delete
  semantic_role: general_marketplace_attribute
  is_key: false
  is_amount: false
  is_date: false
  is_status: false
  is_scope_field: false
  evidence_refs:
  - ev.target_plus.settlement.3_schema_details_37_columns_2
  confidence: high
  review_status: ready
```
```yaml
candidate_card:
  card_type: column
  card_id: column.zs_observe.target_tcin_mapping.unique_id
  display_name: target_tcin_mapping.unique_id
  table_id: table.zs_observe.target_tcin_mapping
  schema: zs_observe
  table_name: target_tcin_mapping
  column_name: unique_id
  source_declared_type: varchar
  data_type: varchar
  column_group: 3. Schema Details (21 Columns)
  description: Row identifier
  semantic_role: identity_or_join_key
  is_key: true
  is_amount: false
  is_date: false
  is_status: false
  is_scope_field: false
  evidence_refs:
  - ev.target_plus.mapping.3_schema_details_21_columns
  confidence: high
  review_status: ready
```
```yaml
candidate_card:
  card_type: column
  card_id: column.zs_observe.target_tcin_mapping.txn_uuid
  display_name: target_tcin_mapping.txn_uuid
  table_id: table.zs_observe.target_tcin_mapping
  schema: zs_observe
  table_name: target_tcin_mapping
  column_name: txn_uuid
  source_declared_type: varchar
  data_type: varchar
  column_group: 3. Schema Details (21 Columns)
  description: Pipeline UUID
  semantic_role: identity_or_join_key
  is_key: true
  is_amount: false
  is_date: false
  is_status: false
  is_scope_field: false
  evidence_refs:
  - ev.target_plus.mapping.3_schema_details_21_columns
  confidence: high
  review_status: ready
```
```yaml
candidate_card:
  card_type: column
  card_id: column.zs_observe.target_tcin_mapping.unique_value
  display_name: target_tcin_mapping.unique_value
  table_id: table.zs_observe.target_tcin_mapping
  schema: zs_observe
  table_name: target_tcin_mapping
  column_name: unique_value
  source_declared_type: varchar
  data_type: varchar
  column_group: 3. Schema Details (21 Columns)
  description: Dedup hash
  semantic_role: financial_amount_or_rate
  is_key: true
  is_amount: true
  is_date: false
  is_status: false
  is_scope_field: false
  evidence_refs:
  - ev.target_plus.mapping.3_schema_details_21_columns
  confidence: high
  review_status: ready
```
```yaml
candidate_card:
  card_type: column
  card_id: column.zs_observe.target_tcin_mapping.sku_id
  display_name: target_tcin_mapping.sku_id
  table_id: table.zs_observe.target_tcin_mapping
  schema: zs_observe
  table_name: target_tcin_mapping
  column_name: sku_id
  source_declared_type: varchar
  data_type: varchar
  column_group: 3. Schema Details (21 Columns)
  description: '**Seller''s clean SKU code** (e.g., `1907AAA`, `KA-1-NB-BK-SNGL`)'
  semantic_role: identity_or_join_key
  is_key: true
  is_amount: false
  is_date: false
  is_status: false
  is_scope_field: false
  evidence_refs:
  - ev.target_plus.mapping.3_schema_details_21_columns
  confidence: high
  review_status: ready
```
```yaml
candidate_card:
  card_type: column
  card_id: column.zs_observe.target_tcin_mapping.tcin
  display_name: target_tcin_mapping.tcin
  table_id: table.zs_observe.target_tcin_mapping
  schema: zs_observe
  table_name: target_tcin_mapping
  column_name: tcin
  source_declared_type: varchar
  data_type: varchar
  column_group: 3. Schema Details (21 Columns)
  description: '**Target Catalogue Item Number** (e.g., `1002553169`) — primary join key'
  semantic_role: identity_or_join_key
  is_key: true
  is_amount: false
  is_date: false
  is_status: false
  is_scope_field: false
  evidence_refs:
  - ev.target_plus.mapping.3_schema_details_21_columns
  confidence: high
  review_status: ready
```
```yaml
candidate_card:
  card_type: column
  card_id: column.zs_observe.target_tcin_mapping.barcode
  display_name: target_tcin_mapping.barcode
  table_id: table.zs_observe.target_tcin_mapping
  schema: zs_observe
  table_name: target_tcin_mapping
  column_name: barcode
  source_declared_type: varchar
  data_type: varchar
  column_group: 3. Schema Details (21 Columns)
  description: UPC/EAN barcode (69 distinct values — multiple SKUs share barcodes)
  semantic_role: identity_or_join_key
  is_key: true
  is_amount: false
  is_date: false
  is_status: false
  is_scope_field: false
  evidence_refs:
  - ev.target_plus.mapping.3_schema_details_21_columns
  confidence: high
  review_status: ready
```
```yaml
candidate_card:
  card_type: column
  card_id: column.zs_observe.target_tcin_mapping.brand
  display_name: target_tcin_mapping.brand
  table_id: table.zs_observe.target_tcin_mapping
  schema: zs_observe
  table_name: target_tcin_mapping
  column_name: brand
  source_declared_type: varchar
  data_type: varchar
  column_group: 3. Schema Details (21 Columns)
  description: Brand name (`Folkculture`, `Katchon`) — note title case differs from sales table
  semantic_role: general_marketplace_attribute
  is_key: false
  is_amount: false
  is_date: false
  is_status: false
  is_scope_field: false
  evidence_refs:
  - ev.target_plus.mapping.3_schema_details_21_columns
  confidence: high
  review_status: ready
```
```yaml
candidate_card:
  card_type: column
  card_id: column.zs_observe.target_tcin_mapping.asin
  display_name: target_tcin_mapping.asin
  table_id: table.zs_observe.target_tcin_mapping
  schema: zs_observe
  table_name: target_tcin_mapping
  column_name: asin
  source_declared_type: varchar
  data_type: varchar
  column_group: 3. Schema Details (21 Columns)
  description: Amazon Standard Identification Number — confirms cross-channel listing
  semantic_role: identity_or_join_key
  is_key: true
  is_amount: false
  is_date: false
  is_status: false
  is_scope_field: false
  evidence_refs:
  - ev.target_plus.mapping.3_schema_details_21_columns
  confidence: high
  review_status: ready
```
```yaml
candidate_card:
  card_type: column
  card_id: column.zs_observe.target_tcin_mapping.currency_type
  display_name: target_tcin_mapping.currency_type
  table_id: table.zs_observe.target_tcin_mapping
  schema: zs_observe
  table_name: target_tcin_mapping
  column_name: currency_type
  source_declared_type: varchar
  data_type: varchar
  column_group: 3. Schema Details (21 Columns)
  description: '`INR`'
  semantic_role: classification_status_or_type
  is_key: false
  is_amount: false
  is_date: false
  is_status: true
  is_scope_field: false
  evidence_refs:
  - ev.target_plus.mapping.3_schema_details_21_columns
  confidence: high
  review_status: ready
```
```yaml
candidate_card:
  card_type: column
  card_id: column.zs_observe.target_tcin_mapping.group_level_id
  display_name: target_tcin_mapping.group_level_id
  table_id: table.zs_observe.target_tcin_mapping
  schema: zs_observe
  table_name: target_tcin_mapping
  column_name: group_level_id
  source_declared_type: integer
  data_type: integer
  column_group: 3. Schema Details (21 Columns)
  description: '`123`'
  semantic_role: scope_identifier_column
  is_key: true
  is_amount: false
  is_date: false
  is_status: false
  is_scope_field: true
  evidence_refs:
  - ev.target_plus.mapping.3_schema_details_21_columns
  confidence: high
  review_status: ready
  scope_note: Documented marketplace scope identifier retained as column/filter value only; do not emit tenant/group/account cards.
```
```yaml
candidate_card:
  card_type: column
  card_id: column.zs_observe.target_tcin_mapping.group_id
  display_name: target_tcin_mapping.group_id
  table_id: table.zs_observe.target_tcin_mapping
  schema: zs_observe
  table_name: target_tcin_mapping
  column_name: group_id
  source_declared_type: integer
  data_type: integer
  column_group: 3. Schema Details (21 Columns)
  description: Internal reference
  semantic_role: scope_identifier_column
  is_key: true
  is_amount: false
  is_date: false
  is_status: false
  is_scope_field: true
  evidence_refs:
  - ev.target_plus.mapping.3_schema_details_21_columns
  confidence: high
  review_status: ready
  scope_note: Documented marketplace scope identifier retained as column/filter value only; do not emit tenant/group/account cards.
```
```yaml
candidate_card:
  card_type: column
  card_id: column.zs_observe.target_tcin_mapping.file_uuid
  display_name: target_tcin_mapping.file_uuid
  table_id: table.zs_observe.target_tcin_mapping
  schema: zs_observe
  table_name: target_tcin_mapping
  column_name: file_uuid
  source_declared_type: varchar
  data_type: varchar
  column_group: 3. Schema Details (21 Columns)
  description: Source file UUID
  semantic_role: identity_or_join_key
  is_key: true
  is_amount: false
  is_date: false
  is_status: false
  is_scope_field: false
  evidence_refs:
  - ev.target_plus.mapping.3_schema_details_21_columns
  confidence: high
  review_status: ready
```
```yaml
candidate_card:
  card_type: column
  card_id: column.zs_observe.target_tcin_mapping.is_active
  display_name: target_tcin_mapping.is_active
  table_id: table.zs_observe.target_tcin_mapping
  schema: zs_observe
  table_name: target_tcin_mapping
  column_name: is_active
  source_declared_type: boolean
  data_type: boolean
  column_group: 3. Schema Details (21 Columns)
  description: Always `true`
  semantic_role: general_marketplace_attribute
  is_key: false
  is_amount: false
  is_date: false
  is_status: false
  is_scope_field: false
  evidence_refs:
  - ev.target_plus.mapping.3_schema_details_21_columns
  confidence: high
  review_status: ready
```
```yaml
candidate_card:
  card_type: column
  card_id: column.zs_observe.target_tcin_mapping.is_duplicated
  display_name: target_tcin_mapping.is_duplicated
  table_id: table.zs_observe.target_tcin_mapping
  schema: zs_observe
  table_name: target_tcin_mapping
  column_name: is_duplicated
  source_declared_type: boolean
  data_type: boolean
  column_group: 3. Schema Details (21 Columns)
  description: Dedup flag
  semantic_role: general_marketplace_attribute
  is_key: false
  is_amount: false
  is_date: false
  is_status: false
  is_scope_field: false
  evidence_refs:
  - ev.target_plus.mapping.3_schema_details_21_columns
  confidence: high
  review_status: ready
```
```yaml
candidate_card:
  card_type: column
  card_id: column.zs_observe.target_tcin_mapping.zen_status
  display_name: target_tcin_mapping.zen_status
  table_id: table.zs_observe.target_tcin_mapping
  schema: zs_observe
  table_name: target_tcin_mapping
  column_name: zen_status
  source_declared_type: boolean
  data_type: boolean
  column_group: 3. Schema Details (21 Columns)
  description: Pipeline flag
  semantic_role: classification_status_or_type
  is_key: false
  is_amount: false
  is_date: false
  is_status: true
  is_scope_field: false
  evidence_refs:
  - ev.target_plus.mapping.3_schema_details_21_columns
  confidence: high
  review_status: ready
```
```yaml
candidate_card:
  card_type: column
  card_id: column.zs_observe.target_tcin_mapping.zen_sheet_name
  display_name: target_tcin_mapping.zen_sheet_name
  table_id: table.zs_observe.target_tcin_mapping
  schema: zs_observe
  table_name: target_tcin_mapping
  column_name: zen_sheet_name
  source_declared_type: varchar
  data_type: varchar
  column_group: 3. Schema Details (21 Columns)
  description: Source sheet
  semantic_role: general_marketplace_attribute
  is_key: false
  is_amount: false
  is_date: false
  is_status: false
  is_scope_field: false
  evidence_refs:
  - ev.target_plus.mapping.3_schema_details_21_columns
  confidence: high
  review_status: ready
```
```yaml
candidate_card:
  card_type: column
  card_id: column.zs_observe.target_tcin_mapping.created_at
  display_name: target_tcin_mapping.created_at
  table_id: table.zs_observe.target_tcin_mapping
  schema: zs_observe
  table_name: target_tcin_mapping
  column_name: created_at
  source_declared_type: timestamp
  data_type: timestamp
  column_group: 3. Schema Details (21 Columns)
  description: Timestamps
  semantic_role: date_time
  is_key: false
  is_amount: false
  is_date: true
  is_status: false
  is_scope_field: false
  evidence_refs:
  - ev.target_plus.mapping.3_schema_details_21_columns
  confidence: high
  review_status: ready
```
```yaml
candidate_card:
  card_type: column
  card_id: column.zs_observe.target_tcin_mapping.updated_at
  display_name: target_tcin_mapping.updated_at
  table_id: table.zs_observe.target_tcin_mapping
  schema: zs_observe
  table_name: target_tcin_mapping
  column_name: updated_at
  source_declared_type: timestamp
  data_type: timestamp
  column_group: 3. Schema Details (21 Columns)
  description: Timestamps
  semantic_role: date_time
  is_key: false
  is_amount: false
  is_date: true
  is_status: false
  is_scope_field: false
  evidence_refs:
  - ev.target_plus.mapping.3_schema_details_21_columns
  confidence: high
  review_status: ready
```
```yaml
candidate_card:
  card_type: column
  card_id: column.zs_observe.target_tcin_mapping.deleted_at
  display_name: target_tcin_mapping.deleted_at
  table_id: table.zs_observe.target_tcin_mapping
  schema: zs_observe
  table_name: target_tcin_mapping
  column_name: deleted_at
  source_declared_type: varchar
  data_type: varchar
  column_group: 3. Schema Details (21 Columns)
  description: Soft delete
  semantic_role: general_marketplace_attribute
  is_key: false
  is_amount: false
  is_date: false
  is_status: false
  is_scope_field: false
  evidence_refs:
  - ev.target_plus.mapping.3_schema_details_21_columns
  confidence: high
  review_status: ready
```
```yaml
candidate_card:
  card_type: column
  card_id: column.zs_observe.target_returns.unique_id
  display_name: target_returns.unique_id
  table_id: table.zs_observe.target_returns
  schema: zs_observe
  table_name: target_returns
  column_name: unique_id
  source_declared_type: varchar
  data_type: varchar
  column_group: 3.1 Identity Columns
  description: Row identifier
  semantic_role: identity_or_join_key
  is_key: true
  is_amount: false
  is_date: false
  is_status: false
  is_scope_field: false
  evidence_refs:
  - ev.target_plus.returns.3_schema_details_30_columns
  confidence: high
  review_status: ready
```
```yaml
candidate_card:
  card_type: column
  card_id: column.zs_observe.target_returns.txn_uuid
  display_name: target_returns.txn_uuid
  table_id: table.zs_observe.target_returns
  schema: zs_observe
  table_name: target_returns
  column_name: txn_uuid
  source_declared_type: varchar
  data_type: varchar
  column_group: 3.1 Identity Columns
  description: Pipeline UUID
  semantic_role: identity_or_join_key
  is_key: true
  is_amount: false
  is_date: false
  is_status: false
  is_scope_field: false
  evidence_refs:
  - ev.target_plus.returns.3_schema_details_30_columns
  confidence: high
  review_status: ready
```
```yaml
candidate_card:
  card_type: column
  card_id: column.zs_observe.target_returns.unique_value
  display_name: target_returns.unique_value
  table_id: table.zs_observe.target_returns
  schema: zs_observe
  table_name: target_returns
  column_name: unique_value
  source_declared_type: varchar
  data_type: varchar
  column_group: 3.1 Identity Columns
  description: Dedup hash
  semantic_role: financial_amount_or_rate
  is_key: true
  is_amount: true
  is_date: false
  is_status: false
  is_scope_field: false
  evidence_refs:
  - ev.target_plus.returns.3_schema_details_30_columns
  confidence: high
  review_status: ready
```
```yaml
candidate_card:
  card_type: column
  card_id: column.zs_observe.target_returns.order_id
  display_name: target_returns.order_id
  table_id: table.zs_observe.target_returns
  schema: zs_observe
  table_name: target_returns
  column_name: order_id
  source_declared_type: varchar
  data_type: varchar
  column_group: 3.1 Identity Columns
  description: Original Target order number
  semantic_role: identity_or_join_key
  is_key: true
  is_amount: false
  is_date: false
  is_status: false
  is_scope_field: false
  evidence_refs:
  - ev.target_plus.returns.3_schema_details_30_columns
  confidence: high
  review_status: ready
```
```yaml
candidate_card:
  card_type: column
  card_id: column.zs_observe.target_returns.item_id
  display_name: target_returns.item_id
  table_id: table.zs_observe.target_returns
  schema: zs_observe
  table_name: target_returns
  column_name: item_id
  source_declared_type: varchar
  data_type: varchar
  column_group: 3.1 Identity Columns
  description: Order line item ID — **join key to sales and settlement**
  semantic_role: identity_or_join_key
  is_key: true
  is_amount: false
  is_date: false
  is_status: false
  is_scope_field: false
  evidence_refs:
  - ev.target_plus.returns.3_schema_details_30_columns
  confidence: high
  review_status: ready
```
```yaml
candidate_card:
  card_type: column
  card_id: column.zs_observe.target_returns.other_id
  display_name: target_returns.other_id
  table_id: table.zs_observe.target_returns
  schema: zs_observe
  table_name: target_returns
  column_name: other_id
  source_declared_type: varchar
  data_type: varchar
  column_group: 3.1 Identity Columns
  description: 'Carrier tracking number (format varies: `1ZE3656H0317269433` = UPS)'
  semantic_role: identity_or_join_key
  is_key: true
  is_amount: false
  is_date: false
  is_status: false
  is_scope_field: false
  evidence_refs:
  - ev.target_plus.returns.3_schema_details_30_columns
  confidence: high
  review_status: ready
```
```yaml
candidate_card:
  card_type: column
  card_id: column.zs_observe.target_returns.sku_id
  display_name: target_returns.sku_id
  table_id: table.zs_observe.target_returns
  schema: zs_observe
  table_name: target_returns
  column_name: sku_id
  source_declared_type: varchar
  data_type: varchar
  column_group: 3.1 Identity Columns
  description: 'Seller SKU (Shopify format: `#shop-XXXXXXXXX`)'
  semantic_role: identity_or_join_key
  is_key: true
  is_amount: false
  is_date: false
  is_status: false
  is_scope_field: false
  evidence_refs:
  - ev.target_plus.returns.3_schema_details_30_columns
  confidence: high
  review_status: ready
```
```yaml
candidate_card:
  card_type: column
  card_id: column.zs_observe.target_returns.tcin
  display_name: target_returns.tcin
  table_id: table.zs_observe.target_returns
  schema: zs_observe
  table_name: target_returns
  column_name: tcin
  source_declared_type: varchar
  data_type: varchar
  column_group: 3.1 Identity Columns
  description: Target product identifier — **join key to tcin_mapping**
  semantic_role: identity_or_join_key
  is_key: true
  is_amount: false
  is_date: false
  is_status: false
  is_scope_field: false
  evidence_refs:
  - ev.target_plus.returns.3_schema_details_30_columns
  confidence: high
  review_status: ready
```
```yaml
candidate_card:
  card_type: column
  card_id: column.zs_observe.target_returns.created_date
  display_name: target_returns.created_date
  table_id: table.zs_observe.target_returns
  schema: zs_observe
  table_name: target_returns
  column_name: created_date
  source_declared_type: date
  data_type: date
  column_group: 3.2 Date Columns
  description: Date return was created/registered in the system
  semantic_role: date_time
  is_key: false
  is_amount: false
  is_date: true
  is_status: false
  is_scope_field: false
  evidence_refs:
  - ev.target_plus.returns.3_schema_details_30_columns
  confidence: high
  review_status: ready
```
```yaml
candidate_card:
  card_type: column
  card_id: column.zs_observe.target_returns.returned_date
  display_name: target_returns.returned_date
  table_id: table.zs_observe.target_returns
  schema: zs_observe
  table_name: target_returns
  column_name: returned_date
  source_declared_type: date
  data_type: date
  column_group: 3.2 Date Columns
  description: Date the item was physically returned / refund was processed
  semantic_role: date_time
  is_key: false
  is_amount: false
  is_date: true
  is_status: false
  is_scope_field: false
  evidence_refs:
  - ev.target_plus.returns.3_schema_details_30_columns
  confidence: high
  review_status: ready
```
```yaml
candidate_card:
  card_type: column
  card_id: column.zs_observe.target_returns.charged_amount
  display_name: target_returns.charged_amount
  table_id: table.zs_observe.target_returns
  schema: zs_observe
  table_name: target_returns
  column_name: charged_amount
  source_declared_type: decimal
  data_type: decimal
  column_group: 3.3 Financial Columns
  description: Original sale price / refund amount
  semantic_role: financial_amount_or_rate
  is_key: false
  is_amount: true
  is_date: false
  is_status: false
  is_scope_field: false
  evidence_refs:
  - ev.target_plus.returns.3_schema_details_30_columns
  confidence: high
  review_status: ready
  sign_convention: Returned/refunded value; cast/aggregate at return-event grain as needed.
```
```yaml
candidate_card:
  card_type: column
  card_id: column.zs_observe.target_returns.quantity
  display_name: target_returns.quantity
  table_id: table.zs_observe.target_returns
  schema: zs_observe
  table_name: target_returns
  column_name: quantity
  source_declared_type: integer
  data_type: integer
  column_group: 3.3 Financial Columns
  description: Quantity returned
  semantic_role: general_marketplace_attribute
  is_key: false
  is_amount: false
  is_date: false
  is_status: false
  is_scope_field: false
  evidence_refs:
  - ev.target_plus.returns.3_schema_details_30_columns
  confidence: high
  review_status: ready
```
```yaml
candidate_card:
  card_type: column
  card_id: column.zs_observe.target_returns.transaction_type
  display_name: target_returns.transaction_type
  table_id: table.zs_observe.target_returns
  schema: zs_observe
  table_name: target_returns
  column_name: transaction_type
  source_declared_type: varchar
  data_type: varchar
  column_group: 3.4 Classification Columns
  description: '`reverse` — 100%'
  semantic_role: classification_status_or_type
  is_key: false
  is_amount: false
  is_date: false
  is_status: true
  is_scope_field: false
  evidence_refs:
  - ev.target_plus.returns.3_schema_details_30_columns
  confidence: high
  review_status: ready
```
```yaml
candidate_card:
  card_type: column
  card_id: column.zs_observe.target_returns.internal_txn_type
  display_name: target_returns.internal_txn_type
  table_id: table.zs_observe.target_returns
  schema: zs_observe
  table_name: target_returns
  column_name: internal_txn_type
  source_declared_type: varchar
  data_type: varchar
  column_group: 3.4 Classification Columns
  description: '`reverse` (return event) or `refunds` (refund processing event)'
  semantic_role: classification_status_or_type
  is_key: false
  is_amount: false
  is_date: false
  is_status: true
  is_scope_field: false
  evidence_refs:
  - ev.target_plus.returns.3_schema_details_30_columns
  confidence: high
  review_status: ready
```
```yaml
candidate_card:
  card_type: column
  card_id: column.zs_observe.target_returns.order_status
  display_name: target_returns.order_status
  table_id: table.zs_observe.target_returns
  schema: zs_observe
  table_name: target_returns
  column_name: order_status
  source_declared_type: varchar
  data_type: varchar
  column_group: 3.4 Classification Columns
  description: '`DELIVERED`, `IN_TRANSIT`, `OUT_FOR_DELIVERY`, `RETURNED`, or NULL'
  semantic_role: classification_status_or_type
  is_key: false
  is_amount: false
  is_date: false
  is_status: true
  is_scope_field: false
  evidence_refs:
  - ev.target_plus.returns.3_schema_details_30_columns
  confidence: high
  review_status: ready
```
```yaml
candidate_card:
  card_type: column
  card_id: column.zs_observe.target_returns.description
  display_name: target_returns.description
  table_id: table.zs_observe.target_returns
  schema: zs_observe
  table_name: target_returns
  column_name: description
  source_declared_type: varchar
  data_type: varchar
  column_group: 3.4 Classification Columns
  description: '**Return reason** — valuable qualitative field (see values below)'
  semantic_role: general_marketplace_attribute
  is_key: false
  is_amount: false
  is_date: false
  is_status: false
  is_scope_field: false
  evidence_refs:
  - ev.target_plus.returns.3_schema_details_30_columns
  confidence: high
  review_status: ready
```
```yaml
candidate_card:
  card_type: column
  card_id: column.zs_observe.target_returns.brand
  display_name: target_returns.brand
  table_id: table.zs_observe.target_returns
  schema: zs_observe
  table_name: target_returns
  column_name: brand
  source_declared_type: varchar
  data_type: varchar
  column_group: 3.4 Classification Columns
  description: '`folkculture`, `katchon`, or NULL'
  semantic_role: general_marketplace_attribute
  is_key: false
  is_amount: false
  is_date: false
  is_status: false
  is_scope_field: false
  evidence_refs:
  - ev.target_plus.returns.3_schema_details_30_columns
  confidence: high
  review_status: ready
```
```yaml
candidate_card:
  card_type: column
  card_id: column.zs_observe.target_returns.group_level_id
  display_name: target_returns.group_level_id
  table_id: table.zs_observe.target_returns
  schema: zs_observe
  table_name: target_returns
  column_name: group_level_id
  source_declared_type: integer
  data_type: integer
  column_group: 3.5 System / Metadata Columns
  description: '`123`'
  semantic_role: scope_identifier_column
  is_key: true
  is_amount: false
  is_date: false
  is_status: false
  is_scope_field: true
  evidence_refs:
  - ev.target_plus.returns.3_schema_details_30_columns
  confidence: high
  review_status: ready
  scope_note: Documented marketplace scope identifier retained as column/filter value only; do not emit tenant/group/account cards.
```
```yaml
candidate_card:
  card_type: column
  card_id: column.zs_observe.target_returns.currency_type
  display_name: target_returns.currency_type
  table_id: table.zs_observe.target_returns
  schema: zs_observe
  table_name: target_returns
  column_name: currency_type
  source_declared_type: varchar
  data_type: varchar
  column_group: 3.5 System / Metadata Columns
  description: '`INR` (label only; values are USD)'
  semantic_role: classification_status_or_type
  is_key: false
  is_amount: false
  is_date: false
  is_status: true
  is_scope_field: false
  evidence_refs:
  - ev.target_plus.returns.3_schema_details_30_columns
  confidence: high
  review_status: ready
```
```yaml
candidate_card:
  card_type: column
  card_id: column.zs_observe.target_returns.is_active
  display_name: target_returns.is_active
  table_id: table.zs_observe.target_returns
  schema: zs_observe
  table_name: target_returns
  column_name: is_active
  source_declared_type: boolean
  data_type: boolean
  column_group: 3.5 System / Metadata Columns
  description: Filter `is_active = true`
  semantic_role: general_marketplace_attribute
  is_key: false
  is_amount: false
  is_date: false
  is_status: false
  is_scope_field: false
  evidence_refs:
  - ev.target_plus.returns.3_schema_details_30_columns
  confidence: high
  review_status: ready
```
```yaml
candidate_card:
  card_type: column
  card_id: column.zs_observe.target_returns.zen_sheet_name
  display_name: target_returns.zen_sheet_name
  table_id: table.zs_observe.target_returns
  schema: zs_observe
  table_name: target_returns
  column_name: zen_sheet_name
  source_declared_type: varchar
  data_type: varchar
  column_group: 3.5 System / Metadata Columns
  description: Source sheet
  semantic_role: general_marketplace_attribute
  is_key: false
  is_amount: false
  is_date: false
  is_status: false
  is_scope_field: false
  evidence_refs:
  - ev.target_plus.returns.3_schema_details_30_columns
  confidence: high
  review_status: ready
```
```yaml
candidate_card:
  card_type: column
  card_id: column.zs_observe.target_returns.created_at
  display_name: target_returns.created_at
  table_id: table.zs_observe.target_returns
  schema: zs_observe
  table_name: target_returns
  column_name: created_at
  source_declared_type: timestamp
  data_type: timestamp
  column_group: 3.5 System / Metadata Columns
  description: Timestamps
  semantic_role: date_time
  is_key: false
  is_amount: false
  is_date: true
  is_status: false
  is_scope_field: false
  evidence_refs:
  - ev.target_plus.returns.3_schema_details_30_columns
  confidence: high
  review_status: ready
```
```yaml
candidate_card:
  card_type: column
  card_id: column.zs_observe.target_returns.updated_at
  display_name: target_returns.updated_at
  table_id: table.zs_observe.target_returns
  schema: zs_observe
  table_name: target_returns
  column_name: updated_at
  source_declared_type: timestamp
  data_type: timestamp
  column_group: 3.5 System / Metadata Columns
  description: Timestamps
  semantic_role: date_time
  is_key: false
  is_amount: false
  is_date: true
  is_status: false
  is_scope_field: false
  evidence_refs:
  - ev.target_plus.returns.3_schema_details_30_columns
  confidence: high
  review_status: ready
```
```yaml
candidate_card:
  card_type: column
  card_id: column.zs_observe.target_returns.deleted_at
  display_name: target_returns.deleted_at
  table_id: table.zs_observe.target_returns
  schema: zs_observe
  table_name: target_returns
  column_name: deleted_at
  source_declared_type: varchar
  data_type: varchar
  column_group: 3.5 System / Metadata Columns
  description: Soft delete
  semantic_role: general_marketplace_attribute
  is_key: false
  is_amount: false
  is_date: false
  is_status: false
  is_scope_field: false
  evidence_refs:
  - ev.target_plus.returns.3_schema_details_30_columns
  confidence: high
  review_status: ready
```
```yaml
candidate_card:
  card_type: column
  card_id: column.zs_observe.target_sales.unique_id
  display_name: target_sales.unique_id
  table_id: table.zs_observe.target_sales
  schema: zs_observe
  table_name: target_sales
  column_name: unique_id
  source_declared_type: varchar
  data_type: varchar
  column_group: 3.1 Identity Columns
  description: System row identifier
  semantic_role: identity_or_join_key
  is_key: true
  is_amount: false
  is_date: false
  is_status: false
  is_scope_field: false
  evidence_refs:
  - ev.target_plus.sales.3_schema_details_29_columns
  confidence: high
  review_status: ready
```
```yaml
candidate_card:
  card_type: column
  card_id: column.zs_observe.target_sales.txn_uuid
  display_name: target_sales.txn_uuid
  table_id: table.zs_observe.target_sales
  schema: zs_observe
  table_name: target_sales
  column_name: txn_uuid
  source_declared_type: varchar
  data_type: varchar
  column_group: 3.1 Identity Columns
  description: Pipeline UUID
  semantic_role: identity_or_join_key
  is_key: true
  is_amount: false
  is_date: false
  is_status: false
  is_scope_field: false
  evidence_refs:
  - ev.target_plus.sales.3_schema_details_29_columns
  confidence: high
  review_status: ready
```
```yaml
candidate_card:
  card_type: column
  card_id: column.zs_observe.target_sales.unique_value
  display_name: target_sales.unique_value
  table_id: table.zs_observe.target_sales
  schema: zs_observe
  table_name: target_sales
  column_name: unique_value
  source_declared_type: varchar
  data_type: varchar
  column_group: 3.1 Identity Columns
  description: Deduplication hash
  semantic_role: financial_amount_or_rate
  is_key: true
  is_amount: true
  is_date: false
  is_status: false
  is_scope_field: false
  evidence_refs:
  - ev.target_plus.sales.3_schema_details_29_columns
  confidence: high
  review_status: ready
```
```yaml
candidate_card:
  card_type: column
  card_id: column.zs_observe.target_sales.order_id
  display_name: target_sales.order_id
  table_id: table.zs_observe.target_sales
  schema: zs_observe
  table_name: target_sales
  column_name: order_id
  source_declared_type: varchar
  data_type: varchar
  column_group: 3.1 Identity Columns
  description: 'Target order number (format: `912003184143022`)'
  semantic_role: identity_or_join_key
  is_key: true
  is_amount: false
  is_date: false
  is_status: false
  is_scope_field: false
  evidence_refs:
  - ev.target_plus.sales.3_schema_details_29_columns
  confidence: high
  review_status: ready
```
```yaml
candidate_card:
  card_type: column
  card_id: column.zs_observe.target_sales.item_id
  display_name: target_sales.item_id
  table_id: table.zs_observe.target_sales
  schema: zs_observe
  table_name: target_sales
  column_name: item_id
  source_declared_type: varchar
  data_type: varchar
  column_group: 3.1 Identity Columns
  description: 'Order line item ID (format: `order_id-lineitem_no`, e.g., `912003184143022-8483691919`) — **join key to settlement**'
  semantic_role: identity_or_join_key
  is_key: true
  is_amount: false
  is_date: false
  is_status: false
  is_scope_field: false
  evidence_refs:
  - ev.target_plus.sales.3_schema_details_29_columns
  confidence: high
  review_status: ready
```
```yaml
candidate_card:
  card_type: column
  card_id: column.zs_observe.target_sales.other_id
  display_name: target_sales.other_id
  table_id: table.zs_observe.target_sales
  schema: zs_observe
  table_name: target_sales
  column_name: other_id
  source_declared_type: varchar
  data_type: varchar
  column_group: 3.1 Identity Columns
  description: Internal store reference code (e.g., `ZVBH`)
  semantic_role: identity_or_join_key
  is_key: true
  is_amount: false
  is_date: false
  is_status: false
  is_scope_field: false
  evidence_refs:
  - ev.target_plus.sales.3_schema_details_29_columns
  confidence: high
  review_status: ready
```
```yaml
candidate_card:
  card_type: column
  card_id: column.zs_observe.target_sales.sku_id
  display_name: target_sales.sku_id
  table_id: table.zs_observe.target_sales
  schema: zs_observe
  table_name: target_sales
  column_name: sku_id
  source_declared_type: varchar
  data_type: varchar
  column_group: 3.1 Identity Columns
  description: 'Seller SKU (Shopify format: `#shop-44218603077890`)'
  semantic_role: identity_or_join_key
  is_key: true
  is_amount: false
  is_date: false
  is_status: false
  is_scope_field: false
  evidence_refs:
  - ev.target_plus.sales.3_schema_details_29_columns
  confidence: high
  review_status: ready
```
```yaml
candidate_card:
  card_type: column
  card_id: column.zs_observe.target_sales.tcin
  display_name: target_sales.tcin
  table_id: table.zs_observe.target_sales
  schema: zs_observe
  table_name: target_sales
  column_name: tcin
  source_declared_type: varchar
  data_type: varchar
  column_group: 3.1 Identity Columns
  description: '**Target Catalogue Item Number** — Target''s product identifier (e.g., `1002637927`) — **join key to tcin_mapping**'
  semantic_role: identity_or_join_key
  is_key: true
  is_amount: false
  is_date: false
  is_status: false
  is_scope_field: false
  evidence_refs:
  - ev.target_plus.sales.3_schema_details_29_columns
  confidence: high
  review_status: ready
```
```yaml
candidate_card:
  card_type: column
  card_id: column.zs_observe.target_sales.created_date
  display_name: target_sales.created_date
  table_id: table.zs_observe.target_sales
  schema: zs_observe
  table_name: target_sales
  column_name: created_date
  source_declared_type: date
  data_type: date
  column_group: 3.2 Date Columns
  description: Order creation date
  semantic_role: date_time
  is_key: false
  is_amount: false
  is_date: true
  is_status: false
  is_scope_field: false
  evidence_refs:
  - ev.target_plus.sales.3_schema_details_29_columns
  confidence: high
  review_status: ready
```
```yaml
candidate_card:
  card_type: column
  card_id: column.zs_observe.target_sales.charged_amount
  display_name: target_sales.charged_amount
  table_id: table.zs_observe.target_sales
  schema: zs_observe
  table_name: target_sales
  column_name: charged_amount
  source_declared_type: decimal
  data_type: decimal
  column_group: 3.3 Financial Columns
  description: '**Per-unit price charged to buyer** (USD amount, e.g., 29.99)'
  semantic_role: financial_amount_or_rate
  is_key: false
  is_amount: true
  is_date: false
  is_status: false
  is_scope_field: false
  evidence_refs:
  - ev.target_plus.sales.3_schema_details_29_columns
  confidence: high
  review_status: ready
```
```yaml
candidate_card:
  card_type: column
  card_id: column.zs_observe.target_sales.discount_amount
  display_name: target_sales.discount_amount
  table_id: table.zs_observe.target_sales
  schema: zs_observe
  table_name: target_sales
  column_name: discount_amount
  source_declared_type: decimal
  data_type: decimal
  column_group: 3.3 Financial Columns
  description: Discount applied (negative value = reduction off charged_amount)
  semantic_role: financial_amount_or_rate
  is_key: false
  is_amount: true
  is_date: false
  is_status: false
  is_scope_field: false
  evidence_refs:
  - ev.target_plus.sales.3_schema_details_29_columns
  confidence: high
  review_status: ready
  sign_convention: Discount values are negative reductions off charged_amount.
```
```yaml
candidate_card:
  card_type: column
  card_id: column.zs_observe.target_sales.quantity
  display_name: target_sales.quantity
  table_id: table.zs_observe.target_sales
  schema: zs_observe
  table_name: target_sales
  column_name: quantity
  source_declared_type: integer
  data_type: integer
  column_group: 3.3 Financial Columns
  description: Units ordered (almost always 1)
  semantic_role: general_marketplace_attribute
  is_key: false
  is_amount: false
  is_date: false
  is_status: false
  is_scope_field: false
  evidence_refs:
  - ev.target_plus.sales.3_schema_details_29_columns
  confidence: high
  review_status: ready
```
```yaml
candidate_card:
  card_type: column
  card_id: column.zs_observe.target_sales.transaction_type
  display_name: target_sales.transaction_type
  table_id: table.zs_observe.target_sales
  schema: zs_observe
  table_name: target_sales
  column_name: transaction_type
  source_declared_type: varchar
  data_type: varchar
  column_group: 3.4 Classification Columns
  description: '`forward` — 100%'
  semantic_role: classification_status_or_type
  is_key: false
  is_amount: false
  is_date: false
  is_status: true
  is_scope_field: false
  evidence_refs:
  - ev.target_plus.sales.3_schema_details_29_columns
  confidence: high
  review_status: ready
```
```yaml
candidate_card:
  card_type: column
  card_id: column.zs_observe.target_sales.internal_txn_type
  display_name: target_sales.internal_txn_type
  table_id: table.zs_observe.target_sales
  schema: zs_observe
  table_name: target_sales
  column_name: internal_txn_type
  source_declared_type: varchar
  data_type: varchar
  column_group: 3.4 Classification Columns
  description: '`sales` — 100%'
  semantic_role: classification_status_or_type
  is_key: false
  is_amount: false
  is_date: false
  is_status: true
  is_scope_field: false
  evidence_refs:
  - ev.target_plus.sales.3_schema_details_29_columns
  confidence: high
  review_status: ready
```
```yaml
candidate_card:
  card_type: column
  card_id: column.zs_observe.target_sales.order_status
  display_name: target_sales.order_status
  table_id: table.zs_observe.target_sales
  schema: zs_observe
  table_name: target_sales
  column_name: order_status
  source_declared_type: varchar
  data_type: varchar
  column_group: 3.4 Classification Columns
  description: '`SHIPPED` or `CANCELED`'
  semantic_role: classification_status_or_type
  is_key: false
  is_amount: false
  is_date: false
  is_status: true
  is_scope_field: false
  evidence_refs:
  - ev.target_plus.sales.3_schema_details_29_columns
  confidence: high
  review_status: ready
```
```yaml
candidate_card:
  card_type: column
  card_id: column.zs_observe.target_sales.brand
  display_name: target_sales.brand
  table_id: table.zs_observe.target_sales
  schema: zs_observe
  table_name: target_sales
  column_name: brand
  source_declared_type: varchar
  data_type: varchar
  column_group: 3.4 Classification Columns
  description: '`folkculture`, `katchon`, or NULL'
  semantic_role: general_marketplace_attribute
  is_key: false
  is_amount: false
  is_date: false
  is_status: false
  is_scope_field: false
  evidence_refs:
  - ev.target_plus.sales.3_schema_details_29_columns
  confidence: high
  review_status: ready
```
```yaml
candidate_card:
  card_type: column
  card_id: column.zs_observe.target_sales.description
  display_name: target_sales.description
  table_id: table.zs_observe.target_sales
  schema: zs_observe
  table_name: target_sales
  column_name: description
  source_declared_type: varchar
  data_type: varchar
  column_group: 3.4 Classification Columns
  description: Product description
  semantic_role: general_marketplace_attribute
  is_key: false
  is_amount: false
  is_date: false
  is_status: false
  is_scope_field: false
  evidence_refs:
  - ev.target_plus.sales.3_schema_details_29_columns
  confidence: high
  review_status: ready
```
```yaml
candidate_card:
  card_type: column
  card_id: column.zs_observe.target_sales.group_level_id
  display_name: target_sales.group_level_id
  table_id: table.zs_observe.target_sales
  schema: zs_observe
  table_name: target_sales
  column_name: group_level_id
  source_declared_type: integer
  data_type: integer
  column_group: 3.5 System / Metadata Columns
  description: '`123` — Target seller account'
  semantic_role: scope_identifier_column
  is_key: true
  is_amount: false
  is_date: false
  is_status: false
  is_scope_field: true
  evidence_refs:
  - ev.target_plus.sales.3_schema_details_29_columns
  confidence: high
  review_status: ready
  scope_note: Documented marketplace scope identifier retained as column/filter value only; do not emit tenant/group/account cards.
```
```yaml
candidate_card:
  card_type: column
  card_id: column.zs_observe.target_sales.group_id
  display_name: target_sales.group_id
  table_id: table.zs_observe.target_sales
  schema: zs_observe
  table_name: target_sales
  column_name: group_id
  source_declared_type: integer
  data_type: integer
  column_group: 3.5 System / Metadata Columns
  description: Internal group reference
  semantic_role: scope_identifier_column
  is_key: true
  is_amount: false
  is_date: false
  is_status: false
  is_scope_field: true
  evidence_refs:
  - ev.target_plus.sales.3_schema_details_29_columns
  confidence: high
  review_status: ready
  scope_note: Documented marketplace scope identifier retained as column/filter value only; do not emit tenant/group/account cards.
```
```yaml
candidate_card:
  card_type: column
  card_id: column.zs_observe.target_sales.file_uuid
  display_name: target_sales.file_uuid
  table_id: table.zs_observe.target_sales
  schema: zs_observe
  table_name: target_sales
  column_name: file_uuid
  source_declared_type: varchar
  data_type: varchar
  column_group: 3.5 System / Metadata Columns
  description: Source file UUID
  semantic_role: identity_or_join_key
  is_key: true
  is_amount: false
  is_date: false
  is_status: false
  is_scope_field: false
  evidence_refs:
  - ev.target_plus.sales.3_schema_details_29_columns
  confidence: high
  review_status: ready
```
```yaml
candidate_card:
  card_type: column
  card_id: column.zs_observe.target_sales.currency_type
  display_name: target_sales.currency_type
  table_id: table.zs_observe.target_sales
  schema: zs_observe
  table_name: target_sales
  column_name: currency_type
  source_declared_type: varchar
  data_type: varchar
  column_group: 3.5 System / Metadata Columns
  description: '`INR` (field label only — actual values are USD prices)'
  semantic_role: classification_status_or_type
  is_key: false
  is_amount: false
  is_date: false
  is_status: true
  is_scope_field: false
  evidence_refs:
  - ev.target_plus.sales.3_schema_details_29_columns
  confidence: high
  review_status: ready
```
```yaml
candidate_card:
  card_type: column
  card_id: column.zs_observe.target_sales.is_active
  display_name: target_sales.is_active
  table_id: table.zs_observe.target_sales
  schema: zs_observe
  table_name: target_sales
  column_name: is_active
  source_declared_type: boolean
  data_type: boolean
  column_group: 3.5 System / Metadata Columns
  description: Filter `is_active = true`
  semantic_role: general_marketplace_attribute
  is_key: false
  is_amount: false
  is_date: false
  is_status: false
  is_scope_field: false
  evidence_refs:
  - ev.target_plus.sales.3_schema_details_29_columns
  confidence: high
  review_status: ready
```
```yaml
candidate_card:
  card_type: column
  card_id: column.zs_observe.target_sales.is_duplicated
  display_name: target_sales.is_duplicated
  table_id: table.zs_observe.target_sales
  schema: zs_observe
  table_name: target_sales
  column_name: is_duplicated
  source_declared_type: boolean
  data_type: boolean
  column_group: 3.5 System / Metadata Columns
  description: Dedup flag
  semantic_role: general_marketplace_attribute
  is_key: false
  is_amount: false
  is_date: false
  is_status: false
  is_scope_field: false
  evidence_refs:
  - ev.target_plus.sales.3_schema_details_29_columns
  confidence: high
  review_status: ready
```
```yaml
candidate_card:
  card_type: column
  card_id: column.zs_observe.target_sales.zen_status
  display_name: target_sales.zen_status
  table_id: table.zs_observe.target_sales
  schema: zs_observe
  table_name: target_sales
  column_name: zen_status
  source_declared_type: boolean
  data_type: boolean
  column_group: 3.5 System / Metadata Columns
  description: Pipeline status flag
  semantic_role: classification_status_or_type
  is_key: false
  is_amount: false
  is_date: false
  is_status: true
  is_scope_field: false
  evidence_refs:
  - ev.target_plus.sales.3_schema_details_29_columns
  confidence: high
  review_status: ready
```
```yaml
candidate_card:
  card_type: column
  card_id: column.zs_observe.target_sales.zen_sheet_name
  display_name: target_sales.zen_sheet_name
  table_id: table.zs_observe.target_sales
  schema: zs_observe
  table_name: target_sales
  column_name: zen_sheet_name
  source_declared_type: varchar
  data_type: varchar
  column_group: 3.5 System / Metadata Columns
  description: Source sheet name
  semantic_role: general_marketplace_attribute
  is_key: false
  is_amount: false
  is_date: false
  is_status: false
  is_scope_field: false
  evidence_refs:
  - ev.target_plus.sales.3_schema_details_29_columns
  confidence: high
  review_status: ready
```
```yaml
candidate_card:
  card_type: column
  card_id: column.zs_observe.target_sales.created_at
  display_name: target_sales.created_at
  table_id: table.zs_observe.target_sales
  schema: zs_observe
  table_name: target_sales
  column_name: created_at
  source_declared_type: timestamp
  data_type: timestamp
  column_group: 3.5 System / Metadata Columns
  description: Timestamps
  semantic_role: date_time
  is_key: false
  is_amount: false
  is_date: true
  is_status: false
  is_scope_field: false
  evidence_refs:
  - ev.target_plus.sales.3_schema_details_29_columns
  confidence: high
  review_status: ready
```
```yaml
candidate_card:
  card_type: column
  card_id: column.zs_observe.target_sales.updated_at
  display_name: target_sales.updated_at
  table_id: table.zs_observe.target_sales
  schema: zs_observe
  table_name: target_sales
  column_name: updated_at
  source_declared_type: timestamp
  data_type: timestamp
  column_group: 3.5 System / Metadata Columns
  description: Timestamps
  semantic_role: date_time
  is_key: false
  is_amount: false
  is_date: true
  is_status: false
  is_scope_field: false
  evidence_refs:
  - ev.target_plus.sales.3_schema_details_29_columns
  confidence: high
  review_status: ready
```
```yaml
candidate_card:
  card_type: column
  card_id: column.zs_observe.target_sales.deleted_at
  display_name: target_sales.deleted_at
  table_id: table.zs_observe.target_sales
  schema: zs_observe
  table_name: target_sales
  column_name: deleted_at
  source_declared_type: varchar
  data_type: varchar
  column_group: 3.5 System / Metadata Columns
  description: Soft delete timestamp
  semantic_role: general_marketplace_attribute
  is_key: false
  is_amount: false
  is_date: false
  is_status: false
  is_scope_field: false
  evidence_refs:
  - ev.target_plus.sales.3_schema_details_29_columns
  confidence: high
  review_status: ready
```
### 4.6 relationship

```yaml
candidate_card:
  card_type: relationship
  card_id: relationship.target_plus.sales_settlement.item_id
  display_name: Target Plus Sales → Settlement on item_id
  source_table_id: table.zs_observe.target_sales
  target_table_id: table.zs_observe.target_settlement
  relationship_type: marketplace_internal_join
  join_keys:
  - item_id
  join_condition: target_sales.item_id = target_settlement.item_id
  coverage: 5,363 / 8,538 sales orders = 63% coverage
  grain_warning: Use settlement transaction_type=forward and date-align periods; settlement ends Nov 2025.
  preaggregation_required: aggregate many-side settlement/return rows before comparing order-level metrics
  cardinality: source-documented coverage; validate grain before metric joins
  evidence_refs:
  - ev.target_plus.marketplace.3_2_primary_join_keys
  - ev.target_plus.marketplace.6_1_sales_settlement_reconciliation
  confidence: high
  review_status: ready
```
```yaml
candidate_card:
  card_type: relationship
  card_id: relationship.target_plus.sales_returns.order_id
  display_name: Target Plus Sales → Returns on order_id
  source_table_id: table.zs_observe.target_sales
  target_table_id: table.zs_observe.target_returns
  relationship_type: marketplace_internal_join
  join_keys:
  - order_id
  join_condition: target_sales.order_id = target_returns.order_id
  coverage: ~1,050 sales orders with returns
  grain_warning: order_id is order-level; multiple return/refund rows may exist.
  preaggregation_required: aggregate many-side settlement/return rows before comparing order-level metrics
  cardinality: source-documented coverage; validate grain before metric joins
  evidence_refs:
  - ev.target_plus.marketplace.3_2_primary_join_keys
  - ev.target_plus.returns.7_4_returns_sales_reconciliation
  confidence: high
  review_status: ready
```
```yaml
candidate_card:
  card_type: relationship
  card_id: relationship.target_plus.returns_settlement.item_id
  display_name: Target Plus Returns → Settlement on item_id
  source_table_id: table.zs_observe.target_returns
  target_table_id: table.zs_observe.target_settlement
  relationship_type: marketplace_internal_join
  join_keys:
  - item_id
  join_condition: target_returns.item_id = target_settlement.item_id AND target_settlement.transaction_type = reverse
  coverage: 385 / 1,050 returns = 37% coverage
  grain_warning: Return settlements may post later; use timing status categories.
  preaggregation_required: aggregate many-side settlement/return rows before comparing order-level metrics
  cardinality: source-documented coverage; validate grain before metric joins
  evidence_refs:
  - ev.target_plus.marketplace.3_2_primary_join_keys
  - ev.target_plus.marketplace.6_2_returns_settlement_refund_match
  confidence: high
  review_status: ready
```
```yaml
candidate_card:
  card_type: relationship
  card_id: relationship.target_plus.sales_mapping.tcin
  display_name: Target Plus Sales → TCIN Mapping on tcin
  source_table_id: table.zs_observe.target_sales
  target_table_id: table.zs_observe.target_tcin_mapping
  relationship_type: marketplace_internal_join
  join_keys:
  - tcin
  join_condition: target_sales.tcin = target_tcin_mapping.tcin
  coverage: Sales TCIN mapping coverage 291/293 = 99%
  grain_warning: Use tcin rather than direct sku_id because sales sku_id is Shopify-format.
  preaggregation_required: aggregate many-side settlement/return rows before comparing order-level metrics
  cardinality: source-documented coverage; validate grain before metric joins
  evidence_refs:
  - ev.target_plus.marketplace.3_2_primary_join_keys
  - ev.target_plus.mapping.7_3_enrich_sales_with_mapping_data
  confidence: high
  review_status: ready
```
```yaml
candidate_card:
  card_type: relationship
  card_id: relationship.target_plus.settlement_mapping.tcin
  display_name: Target Plus Settlement → TCIN Mapping on tcin
  source_table_id: table.zs_observe.target_settlement
  target_table_id: table.zs_observe.target_tcin_mapping
  relationship_type: marketplace_internal_join
  join_keys:
  - tcin
  join_condition: target_settlement.tcin = target_tcin_mapping.tcin
  coverage: source-supported mapping join by TCIN
  grain_warning: Use LOWER(brand) when comparing brand labels across mapping and transaction tables.
  preaggregation_required: aggregate many-side settlement/return rows before comparing order-level metrics
  cardinality: source-documented coverage; validate grain before metric joins
  evidence_refs:
  - ev.target_plus.marketplace.3_1_join_map
  - ev.target_plus.mapping.1_table_overview
  confidence: high
  review_status: ready
```
```yaml
candidate_card:
  card_type: relationship
  card_id: relationship.target_plus.returns_mapping.tcin
  display_name: Target Plus Returns → TCIN Mapping on tcin
  source_table_id: table.zs_observe.target_returns
  target_table_id: table.zs_observe.target_tcin_mapping
  relationship_type: marketplace_internal_join
  join_keys:
  - tcin
  join_condition: target_returns.tcin = target_tcin_mapping.tcin
  coverage: source-supported mapping join by TCIN
  grain_warning: Use mapping for brand/SKU enrichment; do not assume clean seller SKU equals Shopify SKU.
  preaggregation_required: aggregate many-side settlement/return rows before comparing order-level metrics
  cardinality: source-documented coverage; validate grain before metric joins
  evidence_refs:
  - ev.target_plus.marketplace.3_1_join_map
  - ev.target_plus.returns.7_5_sku_level_return_rate
  confidence: high
  review_status: ready
```
### 4.7 value_profile

```yaml
candidate_card:
  card_type: value_profile
  card_id: value_profile.target_plus.scope.group_level_id_123
  display_name: Target Plus group_level_id 123 Mensa brand group scope value
  profile_kind: observed_value_profile
  column_id: column.zs_observe.target_sales.group_level_id
  observed_values:
  - '123'
  distribution_summary: Applies to target_sales, target_returns, target_settlement, and target_tcin_mapping for Mensa brand group.
  normalization_rule: Preserve source spelling/case/code values; normalize only where source explicitly instructs or SQL uses LOWER/casts.
  evidence_refs:
  - ev.target_plus.marketplace.1_3_seller_entities_in_dataset
  - ev.target_plus.marketplace.8_mandatory_query_filters
  confidence: high
  review_status: ready
```
```yaml
candidate_card:
  card_type: value_profile
  card_id: value_profile.target_plus.brand_profiles
  display_name: Folkculture and Katchon brand profile
  profile_kind: brand_product_profile
  table_id: table.zs_observe.target_tcin_mapping
  observed_values:
  - 'Folkculture: 187 SKUs / 170 active in sales / ASP $25.56'
  - 'Katchon: 144 SKUs / 119 active in sales / ASP $12.99'
  distribution_summary: Party supplies, craft kits, seasonal décor, and craft/party accessory categories.
  normalization_rule: Preserve source spelling/case/code values; normalize only where source explicitly instructs or SQL uses LOWER/casts.
  evidence_refs:
  - ev.target_plus.marketplace.1_4_brand_profiles
  confidence: high
  review_status: ready
```
```yaml
candidate_card:
  card_type: value_profile
  card_id: value_profile.target_plus.mapping.brand_case
  display_name: Target mapping brand-case normalization profile
  profile_kind: observed_value_profile
  column_id: column.zs_observe.target_tcin_mapping.brand
  observed_values:
  - Folkculture
  - Katchon
  - folkculture
  - katchon
  distribution_summary: Mapping uses title case while sales/returns/settlement use lowercase or NULL.
  normalization_rule: Use LOWER(brand) or case-insensitive comparison for brand joins/groupings.
  evidence_refs:
  - ev.target_plus.mapping.brand_distribution
  confidence: high
  review_status: ready
```
```yaml
candidate_card:
  card_type: value_profile
  card_id: value_profile.target_plus.sales.order_status
  display_name: Target Sales order_status profile
  profile_kind: observed_value_profile
  column_id: column.zs_observe.target_sales.order_status
  observed_values:
  - 'SHIPPED: 7,269 / GMV 169,909.31'
  - 'CANCELED: 22 / GMV 478.28'
  normalization_rule: Preserve source spelling/case/code values; normalize only where source explicitly instructs or SQL uses LOWER/casts.
  evidence_refs:
  - ev.target_plus.sales.order_status_distribution
  confidence: high
  review_status: ready
```
```yaml
candidate_card:
  card_type: value_profile
  card_id: value_profile.target_plus.sales.brand_distribution
  display_name: Target Sales brand distribution profile
  profile_kind: observed_value_profile
  column_id: column.zs_observe.target_sales.brand
  observed_values:
  - 'folkculture: 5,658 rows / 170 SKUs / 5,363 orders / GMV 144,628 / ASP 25.56'
  - 'katchon: 1,177 rows / 119 SKUs / 1,109 orders / GMV 15,290 / ASP 12.99'
  - 'NULL: 456 rows / 35 SKUs / 442 orders / GMV 10,469 / ASP 22.96'
  normalization_rule: Preserve source spelling/case/code values; normalize only where source explicitly instructs or SQL uses LOWER/casts.
  evidence_refs:
  - ev.target_plus.sales.brand_distribution
  confidence: high
  review_status: ready
```
```yaml
candidate_card:
  card_type: value_profile
  card_id: value_profile.target_plus.sales.order_id_format
  display_name: Target Sales order_id format profile
  profile_kind: observed_value_profile
  column_id: column.zs_observe.target_sales.order_id
  observed_values:
  - 15-digit Target order number
  - prefix 9 standard Target.com order
  - prefix 1 and 2 observed
  normalization_rule: Preserve source spelling/case/code values; normalize only where source explicitly instructs or SQL uses LOWER/casts.
  evidence_refs:
  - ev.target_plus.sales.order_id_format
  confidence: high
  review_status: ready
```
```yaml
candidate_card:
  card_type: value_profile
  card_id: value_profile.target_plus.sales.item_id_format
  display_name: Target Sales item_id format profile
  profile_kind: observed_value_profile
  column_id: column.zs_observe.target_sales.item_id
  observed_values:
  - '{order_id}-{lineitem_number}'
  - 912003184143022-8483691919
  normalization_rule: Preserve source spelling/case/code values; normalize only where source explicitly instructs or SQL uses LOWER/casts.
  evidence_refs:
  - ev.target_plus.sales.item_id_format
  confidence: high
  review_status: ready
```
```yaml
candidate_card:
  card_type: value_profile
  card_id: value_profile.target_plus.sales.sku_id_format
  display_name: Target Sales sku_id Shopify-format profile
  profile_kind: observed_value_profile
  column_id: column.zs_observe.target_sales.sku_id
  observed_values:
  - '#shop-{shopify_variant_id}'
  - '#shop-44218603077890'
  distribution_summary: Shopify variant IDs assigned by seller; map to TCINs via target_tcin_mapping.
  normalization_rule: Preserve source spelling/case/code values; normalize only where source explicitly instructs or SQL uses LOWER/casts.
  evidence_refs:
  - ev.target_plus.sales.sku_id_format
  confidence: high
  review_status: ready
```
```yaml
candidate_card:
  card_type: value_profile
  card_id: value_profile.target_plus.sales.tcin_format
  display_name: Target Sales TCIN format profile
  profile_kind: observed_value_profile
  column_id: column.zs_observe.target_sales.tcin
  observed_values:
  - 10XXXXXXXX
  - '1002637927'
  normalization_rule: Preserve source spelling/case/code values; normalize only where source explicitly instructs or SQL uses LOWER/casts.
  evidence_refs:
  - ev.target_plus.sales.tcin_format
  confidence: high
  review_status: ready
```
```yaml
candidate_card:
  card_type: value_profile
  card_id: value_profile.target_plus.returns.internal_txn_type
  display_name: Target Returns internal_txn_type profile
  profile_kind: observed_value_profile
  column_id: column.zs_observe.target_returns.internal_txn_type
  observed_values:
  - 'reverse: 1,039 / returned value 22,424.61'
  - 'refunds: 140 / refunded value 1,527.90'
  normalization_rule: Preserve source spelling/case/code values; normalize only where source explicitly instructs or SQL uses LOWER/casts.
  evidence_refs:
  - ev.target_plus.returns.internal_txn_type_distribution
  confidence: high
  review_status: ready
```
```yaml
candidate_card:
  card_type: value_profile
  card_id: value_profile.target_plus.returns.order_status
  display_name: Target Returns order_status profile
  profile_kind: observed_value_profile
  column_id: column.zs_observe.target_returns.order_status
  observed_values:
  - NULL ~1,100
  - DELIVERED 19
  - IN_TRANSIT few
  - OUT_FOR_DELIVERY few
  - RETURNED few
  normalization_rule: Preserve source spelling/case/code values; normalize only where source explicitly instructs or SQL uses LOWER/casts.
  evidence_refs:
  - ev.target_plus.returns.order_status_when_populated
  confidence: high
  review_status: ready
```
```yaml
candidate_card:
  card_type: value_profile
  card_id: value_profile.target_plus.returns.reasons
  display_name: Target Returns reason profile
  profile_kind: observed_value_profile
  column_id: column.zs_observe.target_returns.description
  observed_values:
  - Changed Mind 765 / refunded 15,428 / avg 20.17
  - Doesnt Fit 132 / refunded 2,694 / avg 20.41
  - Poor Quality 75 / refunded 1,496 / avg 19.94
  - Arrived Late 44 / refunded 719 / avg 16.34
  - Missing Package 28 / refunded 568 / avg 20.29
  - Sent Wrong Item ~17
  - Missing Item or Shipment ~12
  - Defective few
  - Damaged During Shipping few
  - Not as Described few
  - Duplicate Order few
  distribution_summary: Changed Mind accounts for ~65% of returns.
  normalization_rule: Preserve source spelling/case/code values; normalize only where source explicitly instructs or SQL uses LOWER/casts.
  evidence_refs:
  - ev.target_plus.returns.return_reasons_description_field_top_17_values
  confidence: high
  review_status: ready
```
```yaml
candidate_card:
  card_type: value_profile
  card_id: value_profile.target_plus.returns.carrier_tracking
  display_name: Target Returns carrier tracking profile
  profile_kind: observed_value_profile
  column_id: column.zs_observe.target_returns.other_id
  observed_values:
  - 1ZE3656H0317269433
  - 1Z19R3A49025382586
  distribution_summary: UPS 1Z-format tracking when internal_txn_type=reverse and physical return shipment occurs.
  normalization_rule: Preserve source spelling/case/code values; normalize only where source explicitly instructs or SQL uses LOWER/casts.
  evidence_refs:
  - ev.target_plus.returns.other_id_carrier_tracking_numbers
  confidence: high
  review_status: ready
```
```yaml
candidate_card:
  card_type: value_profile
  card_id: value_profile.target_plus.settlement.transaction_breakdown
  display_name: Target Settlement transaction/internal type breakdown profile
  profile_kind: observed_value_profile
  column_id: column.zs_observe.target_settlement.transaction_type
  observed_values:
  - 'forward/sales: 5,659 rows; charged 132,081; commission 21,069; settled 121,342; 15%'
  - 'reverse/refunds: 450 rows; charged 10,937; commission -1,613; settled -9,185; 15% reversed'
  - 'reverse charge/others: 408 rows; charged 9,981; commission 0; settled -1,721; 0%'
  normalization_rule: Preserve source spelling/case/code values; normalize only where source explicitly instructs or SQL uses LOWER/casts.
  evidence_refs:
  - ev.target_plus.settlement.transaction_type_internal_txn_type_full_breakdown_2
  confidence: high
  review_status: ready
```
```yaml
candidate_card:
  card_type: value_profile
  card_id: value_profile.target_plus.settlement.total_tax_zero
  display_name: Target Settlement total_tax always zero profile
  profile_kind: observed_value_profile
  column_id: column.zs_observe.target_settlement.total_tax
  observed_values:
  - 0.00 in all rows
  distribution_summary: Target collects/remits US sales tax as marketplace facilitator; seller settlement does not expose gross tax
    amounts.
  normalization_rule: Preserve source spelling/case/code values; normalize only where source explicitly instructs or SQL uses LOWER/casts.
  evidence_refs:
  - ev.target_plus.settlement.total_tax_0_0_always_2
  confidence: high
  review_status: ready
```
```yaml
candidate_card:
  card_type: value_profile
  card_id: value_profile.target_plus.settlement.commission_rate
  display_name: Target Settlement flat commission rate profile
  profile_kind: observed_value_profile
  column_id: column.zs_observe.target_settlement.gross_commission_percentage
  observed_values:
  - 0.1500 for forward/reverse product rows
  - 0 for reverse charge rows
  distribution_summary: Observed flat 15% referral fee for current dataset.
  normalization_rule: Preserve source spelling/case/code values; normalize only where source explicitly instructs or SQL uses LOWER/casts.
  evidence_refs:
  - ev.target_plus.settlement.commission_rate_2
  confidence: high
  review_status: ready
```
```yaml
candidate_card:
  card_type: value_profile
  card_id: value_profile.target_plus.settlement.payout_batches
  display_name: Target Settlement payout batch profile
  profile_kind: observed_value_profile
  column_id: column.zs_observe.target_settlement.payout_id
  observed_values:
  - 31 distinct payout_id values
  - po_1SZh3kGgYJvT8MDtnFnpYLpX largest sample
  - po_1RLZ0yGgYJvT8MDt10K8Q4Ew first payout sample
  distribution_summary: payout_id groups multiple Stripe transfer rows into bank-deposit batches.
  normalization_rule: Preserve source spelling/case/code values; normalize only where source explicitly instructs or SQL uses LOWER/casts.
  evidence_refs:
  - ev.target_plus.settlement.payout_batch_structure_2
  confidence: high
  review_status: ready
```
```yaml
candidate_card:
  card_type: value_profile
  card_id: value_profile.target_plus.settlement.stripe_id_formats
  display_name: Target Settlement Stripe ID format profile
  profile_kind: observed_value_profile
  table_id: table.zs_observe.target_settlement
  observed_values:
  - transfer_id tr_1{...}GxFTvW7WRN{...}
  - payout_id po_1{...}GgYJvT8MDt{...}
  - payment_id py_1{...}GgYJvT8MDt{...}
  normalization_rule: Preserve source spelling/case/code values; normalize only where source explicitly instructs or SQL uses LOWER/casts.
  evidence_refs:
  - ev.target_plus.settlement.stripe_id_formats_2
  confidence: high
  review_status: ready
```
```yaml
candidate_card:
  card_type: value_profile
  card_id: value_profile.target_plus.mapping.sku_naming
  display_name: Target TCIN mapping SKU naming profile
  profile_kind: observed_value_profile
  column_id: column.zs_observe.target_tcin_mapping.sku_id
  observed_values:
  - YYYYXXX year+variant format for Folkculture, e.g. 1907AAA / 2010III
  - KA-{size}-{type}-{color}-{qty} for Katchon, e.g. KA-1-NB-BK-SNGL
  normalization_rule: Preserve source spelling/case/code values; normalize only where source explicitly instructs or SQL uses LOWER/casts.
  evidence_refs:
  - ev.target_plus.mapping.sku_naming_conventions
  confidence: high
  review_status: ready
```
```yaml
candidate_card:
  card_type: value_profile
  card_id: value_profile.target_plus.mapping.barcode_coverage
  display_name: Target TCIN mapping barcode coverage profile
  profile_kind: observed_value_profile
  column_id: column.zs_observe.target_tcin_mapping.barcode
  observed_values:
  - 331 SKUs
  - 69 distinct barcodes
  - scientific notation examples such as 8.90441E+12
  distribution_summary: Multiple SKU variants can share the same UPC/EAN barcode; cast/reformat before product matching.
  normalization_rule: Preserve source spelling/case/code values; normalize only where source explicitly instructs or SQL uses LOWER/casts.
  evidence_refs:
  - ev.target_plus.mapping.barcode_coverage
  confidence: high
  review_status: ready
```
```yaml
candidate_card:
  card_type: value_profile
  card_id: value_profile.target_plus.mapping.asin_cross_reference
  display_name: Target TCIN mapping ASIN cross-reference profile
  profile_kind: observed_value_profile
  column_id: column.zs_observe.target_tcin_mapping.asin
  observed_values:
  - 331 TCINs with ASIN = 100% coverage
  - ASIN B07... / B08... examples from brand profile
  distribution_summary: All mapped Target products have Amazon ASINs for catalogue cross-reference.
  normalization_rule: Preserve source spelling/case/code values; normalize only where source explicitly instructs or SQL uses LOWER/casts.
  evidence_refs:
  - ev.target_plus.mapping.asin_cross_reference
  confidence: high
  review_status: ready
```
```yaml
candidate_card:
  card_type: value_profile
  card_id: value_profile.target_plus.currency.label_values
  display_name: Target Plus currency label/value profile
  profile_kind: observed_value_profile
  table_id: table.zs_observe.target_settlement
  observed_values:
  - currency_type = INR label
  - actual amounts are USD-priced values
  distribution_summary: All four tables label currency as INR, but source instructs treating financial values as USD.
  normalization_rule: Preserve source spelling/case/code values; normalize only where source explicitly instructs or SQL uses LOWER/casts.
  evidence_refs:
  - ev.target_plus.marketplace.7_data_quality_observations_and_known_issues
  - ev.target_plus.settlement.2_key_statistics_2
  confidence: high
  review_status: ready
```
### 4.8 metric

```yaml
candidate_card:
  card_type: metric
  card_id: metric.target_plus.total_gmv
  display_name: Target Plus Total GMV
  metric_family: gmv
  domain_id: domain.target_plus.orders
  default_unit: USD
  default_grain: as specified by source SQL or query pattern
  business_definition: Gross GMV, discounts, and net GMV from target_sales shipped orders.
  colloquial_names:
  - gross_gmv
  - total_discounts
  - net_gmv
  evidence_refs:
  - ev.target_plus.marketplace.5_1_total_gmv
  confidence: high
  review_status: ready
```
```yaml
candidate_card:
  card_type: metric
  card_id: metric.target_plus.net_settlement_revenue
  display_name: Target Plus Net Revenue / Net Payout
  metric_family: settlement_revenue
  domain_id: domain.target_plus.settlement
  default_unit: USD
  default_grain: as specified by source SQL or query pattern
  business_definition: Forward settled amount net of return and reverse-charge adjustments from target_settlement.
  colloquial_names:
  - forward_settled
  - return_adjustments
  - tax_adjustments
  - net_revenue
  evidence_refs:
  - ev.target_plus.marketplace.5_2_net_revenue_settlement_view
  confidence: high
  review_status: ready
```
```yaml
candidate_card:
  card_type: metric
  card_id: metric.target_plus.return_rate
  display_name: Target Plus Return Rate
  metric_family: returns
  domain_id: domain.target_plus.returns
  default_unit: USD
  default_grain: as specified by source SQL or query pattern
  business_definition: Distinct returned orders divided by distinct shipped sales orders.
  colloquial_names:
  - return_rate_pct
  evidence_refs:
  - ev.target_plus.marketplace.5_3_return_rate
  confidence: high
  review_status: ready
```
```yaml
candidate_card:
  card_type: metric
  card_id: metric.target_plus.aov
  display_name: Target Plus Average Order Value
  metric_family: aov
  domain_id: domain.target_plus.orders
  default_unit: USD
  default_grain: as specified by source SQL or query pattern
  business_definition: Average charged_amount for shipped target_sales rows.
  colloquial_names:
  - aov
  evidence_refs:
  - ev.target_plus.marketplace.5_4_average_order_value_aov
  confidence: high
  review_status: ready
```
```yaml
candidate_card:
  card_type: metric
  card_id: metric.target_plus.effective_payout_rate
  display_name: Target Plus Effective Payout Rate
  metric_family: payout_rate
  domain_id: domain.target_plus.settlement
  default_unit: USD
  default_grain: as specified by source SQL or query pattern
  business_definition: Forward settled_amount divided by charged_amount_excluding_tax.
  colloquial_names:
  - payout_rate_pct
  evidence_refs:
  - ev.target_plus.marketplace.5_5_effective_payout_rate
  confidence: high
  review_status: ready
```
```yaml
candidate_card:
  card_type: metric
  card_id: metric.target_plus.top_selling_skus
  display_name: Target Plus Top Selling SKUs
  metric_family: sku_sales
  domain_id: domain.target_plus.mapping_enrichment
  default_unit: USD
  default_grain: as specified by source SQL or query pattern
  business_definition: TCIN/SKU/brand/ASIN-level units and revenue from sales joined to mapping.
  colloquial_names:
  - units_sold
  - revenue
  evidence_refs:
  - ev.target_plus.marketplace.5_6_top_selling_skus
  confidence: high
  review_status: ready
```
```yaml
candidate_card:
  card_type: metric
  card_id: metric.target_plus.cancellation_rate
  display_name: Target Plus Cancellation Rate
  metric_family: cancellations
  domain_id: domain.target_plus.orders
  default_unit: USD
  default_grain: as specified by source SQL or query pattern
  business_definition: Canceled rows divided by all active sales rows.
  colloquial_names:
  - cancel_rate_pct
  evidence_refs:
  - ev.target_plus.marketplace.5_7_cancellation_rate
  confidence: high
  review_status: ready
```
```yaml
candidate_card:
  card_type: metric
  card_id: metric.target_plus.commission_validation_variance
  display_name: Target Plus Commission Validation Variance
  metric_family: fee_validation
  domain_id: domain.target_plus.fees
  default_unit: USD
  default_grain: as specified by source SQL or query pattern
  business_definition: Difference between actual gross_commission and expected 15% commission.
  colloquial_names:
  - expected_commission
  - variance
  evidence_refs:
  - ev.target_plus.marketplace.6_3_commission_validation
  confidence: high
  review_status: ready
```
```yaml
candidate_card:
  card_type: metric
  card_id: metric.target_plus.payout_batch_total
  display_name: Target Plus Payout Batch Total
  metric_family: payout_batch
  domain_id: domain.target_plus.payment
  default_unit: USD
  default_grain: as specified by source SQL or query pattern
  business_definition: Sum of settled_amount and transaction counts per payout_id.
  colloquial_names:
  - total_payout
  - orders_in_payout
  - sales_rows
  - return_rows
  - tax_rows
  evidence_refs:
  - ev.target_plus.marketplace.6_4_payout_reconciliation
  confidence: high
  review_status: ready
```
```yaml
candidate_card:
  card_type: metric
  card_id: metric.target_plus.return_reason_value
  display_name: Target Plus Return Value by Reason
  metric_family: returns
  domain_id: domain.target_plus.returns
  default_unit: USD
  default_grain: as specified by source SQL or query pattern
  business_definition: Return count/value/average by target_returns.description.
  colloquial_names:
  - returns
  - total_return_value
  - avg_refund
  evidence_refs:
  - ev.target_plus.returns.7_1_return_volume_and_value_by_reason
  confidence: high
  review_status: ready
```
```yaml
candidate_card:
  card_type: metric
  card_id: metric.target_plus.brand_return_rate
  display_name: Target Plus Brand Return Rate
  metric_family: returns
  domain_id: domain.target_plus.returns
  default_unit: USD
  default_grain: as specified by source SQL or query pattern
  business_definition: Brand-level returned order count divided by shipped sales order count.
  colloquial_names:
  - return_rate_pct
  evidence_refs:
  - ev.target_plus.returns.7_2_return_rate_by_brand
  confidence: high
  review_status: ready
```
```yaml
candidate_card:
  card_type: metric
  card_id: metric.target_plus.monthly_sales_gmv
  display_name: Target Plus Monthly Sales GMV
  metric_family: gmv_trend
  domain_id: domain.target_plus.orders
  default_unit: USD
  default_grain: as specified by source SQL or query pattern
  business_definition: Month/brand sales, orders, units, GMV, discount, and AOV.
  colloquial_names:
  - orders
  - units
  - gmv
  - discount
  - aov
  evidence_refs:
  - ev.target_plus.sales.7_1_monthly_sales_gmv_by_brand
  confidence: high
  review_status: ready
```
```yaml
candidate_card:
  card_type: metric
  card_id: metric.target_plus.mapping_sales_coverage
  display_name: Target Plus Mapping Sales Coverage
  metric_family: mapping_coverage
  domain_id: domain.target_plus.mapping_enrichment
  default_unit: USD
  default_grain: as specified by source SQL or query pattern
  business_definition: Sales count and revenue by mapping dimensions.
  colloquial_names:
  - sales_count
  - revenue
  evidence_refs:
  - ev.target_plus.mapping.7_1_full_catalogue_with_sales_coverage
  confidence: high
  review_status: ready
```
### 4.9 metric_implementation

```yaml
candidate_card:
  card_type: metric_implementation
  card_id: metric_impl.target_plus.total_gmv
  metric_id: metric.target_plus.total_gmv
  platform_context_id: platform_context.target_plus.us
  display_name: Target Plus Total GMV from sales
  source_tables:
  - table.zs_observe.target_sales
  source_columns:
  - column.zs_observe.target_sales.charged_amount
  - column.zs_observe.target_sales.discount_amount
  formula_sql_ref: sql.target_plus.marketplace.5_1_total_gmv
  formula_text: SUM(charged_amount), SUM(discount_amount), SUM(charged_amount)+SUM(discount_amount)
  filters:
  - is_active = true
  - order_status = SHIPPED
  grain: source SQL grain
  sign_convention: Use source SQL and documented transaction_type context.
  aggregation_order: Apply filters before aggregation; aggregate many-side tables before joining where applicable.
  evidence_refs:
  - ev.target_plus.marketplace.5_1_total_gmv
  confidence: high
  review_status: ready
```
```yaml
candidate_card:
  card_type: metric_implementation
  card_id: metric_impl.target_plus.net_settlement_revenue
  metric_id: metric.target_plus.net_settlement_revenue
  platform_context_id: platform_context.target_plus.us
  display_name: Target Plus settlement-view net revenue
  source_tables:
  - table.zs_observe.target_settlement
  source_columns:
  - column.zs_observe.target_settlement.transaction_type
  - column.zs_observe.target_settlement.settled_amount
  formula_sql_ref: sql.target_plus.marketplace.5_2_net_revenue_settlement_view
  formula_text: Conditional SUM(settled_amount) by forward, reverse, and reverse charge transaction_type
  filters:
  - is_active = true
  grain: source SQL grain
  sign_convention: Use source SQL and documented transaction_type context.
  aggregation_order: Apply filters before aggregation; aggregate many-side tables before joining where applicable.
  evidence_refs:
  - ev.target_plus.marketplace.5_2_net_revenue_settlement_view
  confidence: high
  review_status: ready
```
```yaml
candidate_card:
  card_type: metric_implementation
  card_id: metric_impl.target_plus.return_rate
  metric_id: metric.target_plus.return_rate
  platform_context_id: platform_context.target_plus.us
  display_name: Target Plus return rate from sales and returns
  source_tables:
  - table.zs_observe.target_sales
  - table.zs_observe.target_returns
  source_columns:
  - column.zs_observe.target_sales.order_id
  - column.zs_observe.target_returns.order_id
  formula_sql_ref: sql.target_plus.marketplace.5_3_return_rate
  formula_text: COUNT(DISTINCT returns.order_id) / COUNT(DISTINCT sales.order_id)
  filters:
  - s.is_active = true
  - s.order_status = SHIPPED
  - r.is_active = true
  grain: source SQL grain
  sign_convention: Use source SQL and documented transaction_type context.
  aggregation_order: Apply filters before aggregation; aggregate many-side tables before joining where applicable.
  evidence_refs:
  - ev.target_plus.marketplace.5_3_return_rate
  confidence: high
  review_status: ready
```
```yaml
candidate_card:
  card_type: metric_implementation
  card_id: metric_impl.target_plus.aov
  metric_id: metric.target_plus.aov
  platform_context_id: platform_context.target_plus.us
  display_name: Target Plus AOV from shipped sales
  source_tables:
  - table.zs_observe.target_sales
  source_columns:
  - column.zs_observe.target_sales.charged_amount
  formula_sql_ref: sql.target_plus.marketplace.5_4_average_order_value_aov
  formula_text: AVG(charged_amount)
  filters:
  - is_active = true
  - order_status = SHIPPED
  grain: source SQL grain
  sign_convention: Use source SQL and documented transaction_type context.
  aggregation_order: Apply filters before aggregation; aggregate many-side tables before joining where applicable.
  evidence_refs:
  - ev.target_plus.marketplace.5_4_average_order_value_aov
  confidence: high
  review_status: ready
```
```yaml
candidate_card:
  card_type: metric_implementation
  card_id: metric_impl.target_plus.effective_payout_rate
  metric_id: metric.target_plus.effective_payout_rate
  platform_context_id: platform_context.target_plus.us
  display_name: Target Plus forward effective payout rate
  source_tables:
  - table.zs_observe.target_settlement
  source_columns:
  - column.zs_observe.target_settlement.settled_amount
  - column.zs_observe.target_settlement.charged_amount_excluding_tax
  formula_sql_ref: sql.target_plus.marketplace.5_5_effective_payout_rate
  formula_text: 100 * SUM(settled_amount) / SUM(charged_amount_excluding_tax)
  filters:
  - is_active = true
  - transaction_type = forward
  grain: source SQL grain
  sign_convention: Use source SQL and documented transaction_type context.
  aggregation_order: Apply filters before aggregation; aggregate many-side tables before joining where applicable.
  evidence_refs:
  - ev.target_plus.marketplace.5_5_effective_payout_rate
  confidence: high
  review_status: ready
```
```yaml
candidate_card:
  card_type: metric_implementation
  card_id: metric_impl.target_plus.top_selling_skus
  metric_id: metric.target_plus.top_selling_skus
  platform_context_id: platform_context.target_plus.us
  display_name: Target Plus top selling SKUs
  source_tables:
  - table.zs_observe.target_sales
  - table.zs_observe.target_tcin_mapping
  source_columns:
  - column.zs_observe.target_sales.tcin
  - column.zs_observe.target_tcin_mapping.tcin
  - column.zs_observe.target_sales.charged_amount
  formula_sql_ref: sql.target_plus.marketplace.5_6_top_selling_skus
  formula_text: COUNT(order_id), SUM(charged_amount) grouped by tcin/sku/brand/asin
  filters:
  - s.is_active = true
  - s.order_status = SHIPPED
  - m.is_active = true
  grain: source SQL grain
  sign_convention: Use source SQL and documented transaction_type context.
  aggregation_order: Apply filters before aggregation; aggregate many-side tables before joining where applicable.
  evidence_refs:
  - ev.target_plus.marketplace.5_6_top_selling_skus
  confidence: high
  review_status: ready
```
```yaml
candidate_card:
  card_type: metric_implementation
  card_id: metric_impl.target_plus.cancellation_rate
  metric_id: metric.target_plus.cancellation_rate
  platform_context_id: platform_context.target_plus.us
  display_name: Target Plus cancellation rate
  source_tables:
  - table.zs_observe.target_sales
  source_columns:
  - column.zs_observe.target_sales.order_status
  formula_sql_ref: sql.target_plus.marketplace.5_7_cancellation_rate
  formula_text: COUNT_IF(order_status = CANCELED) / COUNT(*)
  filters:
  - is_active = true
  grain: source SQL grain
  sign_convention: Use source SQL and documented transaction_type context.
  aggregation_order: Apply filters before aggregation; aggregate many-side tables before joining where applicable.
  evidence_refs:
  - ev.target_plus.marketplace.5_7_cancellation_rate
  confidence: high
  review_status: ready
```
```yaml
candidate_card:
  card_type: metric_implementation
  card_id: metric_impl.target_plus.commission_validation
  metric_id: metric.target_plus.commission_validation_variance
  platform_context_id: platform_context.target_plus.us
  display_name: Target Plus commission validation variance
  source_tables:
  - table.zs_observe.target_settlement
  source_columns:
  - column.zs_observe.target_settlement.charged_amount_excluding_tax
  - column.zs_observe.target_settlement.gross_commission
  formula_sql_ref: sql.target_plus.marketplace.6_3_commission_validation
  formula_text: ABS(gross_commission - ROUND(charged_amount_excluding_tax * 0.15, 4))
  filters:
  - is_active = true
  - transaction_type = forward
  - variance > 0.01
  grain: source SQL grain
  sign_convention: Use source SQL and documented transaction_type context.
  aggregation_order: Apply filters before aggregation; aggregate many-side tables before joining where applicable.
  evidence_refs:
  - ev.target_plus.marketplace.6_3_commission_validation
  confidence: high
  review_status: ready
```
```yaml
candidate_card:
  card_type: metric_implementation
  card_id: metric_impl.target_plus.payout_batch_total
  metric_id: metric.target_plus.payout_batch_total
  platform_context_id: platform_context.target_plus.us
  display_name: Target Plus payout batch total
  source_tables:
  - table.zs_observe.target_settlement
  source_columns:
  - column.zs_observe.target_settlement.payout_id
  - column.zs_observe.target_settlement.settled_amount
  formula_sql_ref: sql.target_plus.marketplace.6_4_payout_reconciliation
  formula_text: SUM(settled_amount) grouped by payout_id
  filters:
  - is_active = true
  grain: source SQL grain
  sign_convention: Use source SQL and documented transaction_type context.
  aggregation_order: Apply filters before aggregation; aggregate many-side tables before joining where applicable.
  evidence_refs:
  - ev.target_plus.marketplace.6_4_payout_reconciliation
  confidence: high
  review_status: ready
```
```yaml
candidate_card:
  card_type: metric_implementation
  card_id: metric_impl.target_plus.return_reason_value
  metric_id: metric.target_plus.return_reason_value
  platform_context_id: platform_context.target_plus.us
  display_name: Target Plus return value by reason
  source_tables:
  - table.zs_observe.target_returns
  source_columns:
  - column.zs_observe.target_returns.description
  - column.zs_observe.target_returns.charged_amount
  formula_sql_ref: sql.target_plus.returns.7_1_return_volume_and_value_by_reason
  formula_text: COUNT(*), SUM(charged_amount), AVG(charged_amount) grouped by description
  filters:
  - is_active = true
  - internal_txn_type = reverse
  grain: source SQL grain
  sign_convention: Use source SQL and documented transaction_type context.
  aggregation_order: Apply filters before aggregation; aggregate many-side tables before joining where applicable.
  evidence_refs:
  - ev.target_plus.returns.7_1_return_volume_and_value_by_reason
  confidence: high
  review_status: ready
```
```yaml
candidate_card:
  card_type: metric_implementation
  card_id: metric_impl.target_plus.brand_return_rate
  metric_id: metric.target_plus.brand_return_rate
  platform_context_id: platform_context.target_plus.us
  display_name: Target Plus brand return rate
  source_tables:
  - table.zs_observe.target_returns
  - table.zs_observe.target_sales
  source_columns:
  - column.zs_observe.target_returns.order_id
  - column.zs_observe.target_sales.order_id
  - column.zs_observe.target_sales.brand
  formula_sql_ref: sql.target_plus.returns.7_2_return_rate_by_brand
  formula_text: returned orders / shipped orders by brand
  filters:
  - r.is_active = true
  - s.is_active = true
  - s.order_status = SHIPPED
  grain: source SQL grain
  sign_convention: Use source SQL and documented transaction_type context.
  aggregation_order: Apply filters before aggregation; aggregate many-side tables before joining where applicable.
  evidence_refs:
  - ev.target_plus.returns.7_2_return_rate_by_brand
  confidence: high
  review_status: ready
```
```yaml
candidate_card:
  card_type: metric_implementation
  card_id: metric_impl.target_plus.monthly_sales_gmv
  metric_id: metric.target_plus.monthly_sales_gmv
  platform_context_id: platform_context.target_plus.us
  display_name: Target Plus monthly sales GMV by brand
  source_tables:
  - table.zs_observe.target_sales
  source_columns:
  - column.zs_observe.target_sales.created_date
  - column.zs_observe.target_sales.charged_amount
  formula_sql_ref: sql.target_plus.sales.7_1_monthly_sales_gmv_by_brand
  formula_text: DATE_TRUNC(month, created_date), COUNT(*), SUM(quantity), SUM(charged_amount), AVG(charged_amount)
  filters:
  - is_active = true
  - order_status = SHIPPED
  grain: source SQL grain
  sign_convention: Use source SQL and documented transaction_type context.
  aggregation_order: Apply filters before aggregation; aggregate many-side tables before joining where applicable.
  evidence_refs:
  - ev.target_plus.sales.7_1_monthly_sales_gmv_by_brand
  confidence: high
  review_status: ready
```
```yaml
candidate_card:
  card_type: metric_implementation
  card_id: metric_impl.target_plus.mapping_sales_coverage
  metric_id: metric.target_plus.mapping_sales_coverage
  platform_context_id: platform_context.target_plus.us
  display_name: Target Plus mapping sales coverage
  source_tables:
  - table.zs_observe.target_sales
  - table.zs_observe.target_tcin_mapping
  source_columns:
  - column.zs_observe.target_sales.tcin
  - column.zs_observe.target_tcin_mapping.tcin
  - column.zs_observe.target_sales.charged_amount
  formula_sql_ref: sql.target_plus.mapping.7_1_full_catalogue_with_sales_coverage
  formula_text: LEFT JOIN mapping to sales on tcin and aggregate sales_count/revenue
  filters:
  - m.is_active = true
  - s.is_active = true where joined
  grain: source SQL grain
  sign_convention: Use source SQL and documented transaction_type context.
  aggregation_order: Apply filters before aggregation; aggregate many-side tables before joining where applicable.
  evidence_refs:
  - ev.target_plus.mapping.7_1_full_catalogue_with_sales_coverage
  confidence: high
  review_status: ready
```
### 4.10 formula_template

```yaml
candidate_card:
  card_type: formula_template
  card_id: formula_template.target_plus.forward_payout_waterfall
  display_name: Target Plus forward payout waterfall
  formula_text: charged_amount_excluding_tax + shipping_amount - gross_commission = settled_amount for forward rows; source waterfall
    observed forward net settled 121,342 and payout rate 85.2%.
  unit: USD
  usage_notes: Forward product rows; use charged_amount_excluding_tax for multi-quantity order value.
  sign_convention: Use transaction_type/internal_txn_type context; do not mix forward, reverse, and reverse charge unless netting is
    intended.
  evidence_refs:
  - ev.target_plus.marketplace.4_2_full_payout_waterfall_forward_sales_observed
  - ev.target_plus.settlement.5_financial_waterfall_forward_sales_2
  confidence: high
  review_status: ready
```
```yaml
candidate_card:
  card_type: formula_template
  card_id: formula_template.target_plus.return_refund_netting
  display_name: Target Plus return refund netting
  formula_text: reverse settled impact = return refund amount minus/plus commission reversal per settlement sign; source shows net return
    settlement -9,185.
  unit: USD
  usage_notes: Reverse rows only; gross_commission may reverse as a credit to seller.
  sign_convention: Use transaction_type/internal_txn_type context; do not mix forward, reverse, and reverse charge unless netting is
    intended.
  evidence_refs:
  - ev.target_plus.marketplace.2_2_return_flow
  - ev.target_plus.settlement.5_financial_waterfall_forward_sales_2
  confidence: high
  review_status: ready
```
```yaml
candidate_card:
  card_type: formula_template
  card_id: formula_template.target_plus.reverse_charge_tax_adjustment
  display_name: Target Plus reverse-charge tax adjustment
  formula_text: |-
    reverse charge rows use transaction_type = reverse charge and internal_txn_type = others; gross_commission_percentage = 0; settled_amount is a negative tax adjustment while total_tax remains 0.
  unit: USD
  usage_notes: Not a customer return; filter reverse charge separately from transaction_type=reverse.
  sign_convention: Use transaction_type/internal_txn_type context; do not mix forward, reverse, and reverse charge unless netting is
    intended.
  evidence_refs:
  - ev.target_plus.marketplace.2_3_reverse_charge_flow
  - ev.target_plus.settlement.reverse_charge_what_is_it_2
  confidence: high
  review_status: ready
```
### 4.11 metric_dependency

```yaml
candidate_card:
  card_type: metric_dependency
  card_id: metric_dependency.target_plus.net_revenue_components
  parent_metric_id: metric.target_plus.net_settlement_revenue
  dependent_metric_ids:
  - metric.target_plus.total_gmv
  - metric.target_plus.return_rate
  - metric.target_plus.effective_payout_rate
  dependency_type: netting_context
  calculation_order: Use source-specific filters and transaction_type context before interpreting dependent metrics.
  evidence_refs:
  - ev.target_plus.marketplace.5_key_business_metrics_with_sql
  confidence: high
  review_status: ready
```
```yaml
candidate_card:
  card_type: metric_dependency
  card_id: metric_dependency.target_plus.return_rate_dependencies
  parent_metric_id: metric.target_plus.return_rate
  dependent_metric_ids:
  - metric.target_plus.total_gmv
  dependency_type: denominator_context
  calculation_order: Use source-specific filters and transaction_type context before interpreting dependent metrics.
  evidence_refs:
  - ev.target_plus.marketplace.5_key_business_metrics_with_sql
  confidence: high
  review_status: ready
```
```yaml
candidate_card:
  card_type: metric_dependency
  card_id: metric_dependency.target_plus.payout_rate_dependencies
  parent_metric_id: metric.target_plus.effective_payout_rate
  dependent_metric_ids:
  - metric.target_plus.commission_validation_variance
  dependency_type: fee_waterfall_context
  calculation_order: Use source-specific filters and transaction_type context before interpreting dependent metrics.
  evidence_refs:
  - ev.target_plus.marketplace.5_key_business_metrics_with_sql
  confidence: high
  review_status: ready
```
### 4.12 business_process

```yaml
candidate_card:
  card_type: business_process
  card_id: business_process.target_plus.forward_order_flow
  display_name: Target Plus forward order flow
  process_family: forward_order_to_settlement
  description: Customer order on Target.com / Target app becomes target_sales forward row, seller self-fulfils, Stripe transfer posts
    to target_settlement, and payout_id groups settlement rows.
  entry_condition: target_sales row with transaction_type=forward and order_status=SHIPPED
  exit_condition: target_settlement forward row with transfer_id and payout_id; settled_amount equals charged_amount_excluding_tax +
    shipping_amount - gross_commission
  source_tables:
  - table.zs_observe.target_sales
  - table.zs_observe.target_settlement
  state_fields: Status/type fields are preserved on workflow steps; no state_transition cards emitted.
  evidence_refs:
  - ev.target_plus.marketplace.2_1_forward_order_flow
  confidence: high
  review_status: ready
```
```yaml
candidate_card:
  card_type: business_process
  card_id: business_process.target_plus.return_flow
  display_name: Target Plus return and refund flow
  process_family: return_refund
  description: Buyer returns through Target.com/app/store; Target handles return logistics; target_returns records reverse/refund events
    and target_settlement posts reverse refund settlement.
  entry_condition: target_returns row with transaction_type=reverse and internal_txn_type reverse/refunds
  exit_condition: target_settlement reverse row with negative settled_amount and commission reversal
  source_tables:
  - table.zs_observe.target_returns
  - table.zs_observe.target_settlement
  - table.zs_observe.target_sales
  state_fields: Status/type fields are preserved on workflow steps; no state_transition cards emitted.
  evidence_refs:
  - ev.target_plus.marketplace.2_2_return_flow
  confidence: high
  review_status: ready
```
```yaml
candidate_card:
  card_type: business_process
  card_id: business_process.target_plus.reverse_charge_flow
  display_name: Target Plus marketplace-facilitator reverse-charge tax adjustment flow
  process_family: tax_adjustment
  description: Target collects/remits US sales tax as marketplace facilitator; target_settlement reverse charge/others rows represent
    internal tax accounting adjustments with total_tax=0.
  entry_condition: target_settlement reverse charge row with internal_txn_type=others
  exit_condition: negative settled_amount tax adjustment; gross_commission_percentage=0 and total_tax=0
  source_tables:
  - table.zs_observe.target_settlement
  state_fields: Status/type fields are preserved on workflow steps; no state_transition cards emitted.
  evidence_refs:
  - ev.target_plus.marketplace.2_3_reverse_charge_flow
  - ev.target_plus.marketplace.4_3_us_sales_tax_marketplace_facilitator_model
  confidence: high
  review_status: ready
```
```yaml
candidate_card:
  card_type: business_process
  card_id: business_process.target_plus.product_mapping_enrichment
  display_name: Target Plus TCIN mapping enrichment process
  process_family: mapping_enrichment
  description: Transaction rows are enriched through TCIN mapping to clean seller SKU, ASIN, barcode, and case-normalized brand context.
  entry_condition: target_sales/returns/settlement rows with tcin
  exit_condition: target_tcin_mapping joins on tcin; brand normalized with LOWER when compared to transaction tables
  source_tables:
  - table.zs_observe.target_sales
  - table.zs_observe.target_returns
  - table.zs_observe.target_settlement
  - table.zs_observe.target_tcin_mapping
  state_fields: Status/type fields are preserved on workflow steps; no state_transition cards emitted.
  evidence_refs:
  - ev.target_plus.marketplace.3_1_join_map
  - ev.target_plus.mapping.1_table_overview
  confidence: high
  review_status: ready
```
### 4.13 workflow_step

```yaml
candidate_card:
  card_type: workflow_step
  card_id: workflow_step.target_plus.forward_order_flow.01
  process_id: business_process.target_plus.forward_order_flow
  step_order: 1
  display_name: Order captured in target_sales
  description: |-
    Order appears in target_sales with transaction_type=forward, internal_txn_type=sales, order_status=SHIPPED, item_id = order_id + lineitem number, and optional RedCard/discount_amount context.
  input_tables:
  - table.zs_observe.target_sales
  output_tables:
  - table.zs_observe.target_sales
  status_conditions:
  - transaction_type='forward'
  - internal_txn_type='sales'
  - order_status='SHIPPED'
  evidence_refs:
  - ev.target_plus.marketplace.2_1_forward_order_flow
  confidence: high
  review_status: ready
```
```yaml
candidate_card:
  card_type: workflow_step
  card_id: workflow_step.target_plus.forward_order_flow.02
  process_id: business_process.target_plus.forward_order_flow
  step_order: 2
  display_name: Seller self-fulfils through approved carriers
  description: Seller ships the target_sales order_id/item_id within 24 hours using UPS/USPS/FedEx and unbranded packaging. Carrier
    rules are marketplace caveats only, not logistics account cards.
  input_tables:
  - table.zs_observe.target_sales
  output_tables: []
  status_conditions:
  - Target Plus self-fulfilment; no Target warehouse/FBA-style service
  evidence_refs:
  - ev.target_plus.marketplace.2_1_forward_order_flow
  confidence: high
  review_status: ready
```
```yaml
candidate_card:
  card_type: workflow_step
  card_id: workflow_step.target_plus.forward_order_flow.03
  process_id: business_process.target_plus.forward_order_flow
  step_order: 3
  display_name: Stripe transfer appears in settlement
  description: target_settlement records transfer_id/payment_id/payout_id with transaction_type=forward and gross_commission_percentage=0.1500.
  input_tables:
  - table.zs_observe.target_sales
  output_tables:
  - table.zs_observe.target_settlement
  status_conditions:
  - transaction_type='forward'
  - internal_txn_type='sales'
  - gross_commission_percentage=0.1500
  evidence_refs:
  - ev.target_plus.marketplace.2_1_forward_order_flow
  confidence: high
  review_status: ready
```
```yaml
candidate_card:
  card_type: workflow_step
  card_id: workflow_step.target_plus.forward_order_flow.04
  process_id: business_process.target_plus.forward_order_flow
  step_order: 4
  display_name: Payout batch aggregates transfers
  description: payout_id groups many transfer_id rows; settled_amount = charged_amount_excluding_tax + shipping_amount - gross_commission.
  input_tables:
  - table.zs_observe.target_settlement
  output_tables:
  - table.zs_observe.target_settlement
  status_conditions:
  - payout_id groups multiple transfer_id rows
  - settled_amount waterfall
  evidence_refs:
  - ev.target_plus.marketplace.2_1_forward_order_flow
  confidence: high
  review_status: ready
```
```yaml
candidate_card:
  card_type: workflow_step
  card_id: workflow_step.target_plus.return_flow.01
  process_id: business_process.target_plus.return_flow
  step_order: 1
  display_name: Return appears in target_returns
  description: target_returns captures order_id, item_id, tcin, description return reason, charged_amount, returned_date, and internal_txn_type
    reverse/refunds.
  input_tables:
  - table.zs_observe.target_returns
  output_tables:
  - table.zs_observe.target_returns
  status_conditions:
  - transaction_type='reverse'
  - internal_txn_type IN ('reverse','refunds')
  evidence_refs:
  - ev.target_plus.marketplace.2_2_return_flow
  confidence: high
  review_status: ready
```
```yaml
candidate_card:
  card_type: workflow_step
  card_id: workflow_step.target_plus.return_flow.02
  process_id: business_process.target_plus.return_flow
  step_order: 2
  display_name: Refund settlement posts
  description: target_settlement reverse/refunds row posts refund impact; settled_amount is negative and gross_commission may reverse
    as a seller credit.
  input_tables:
  - table.zs_observe.target_returns
  output_tables:
  - table.zs_observe.target_settlement
  status_conditions:
  - transaction_type='reverse'
  - internal_txn_type='refunds'
  evidence_refs:
  - ev.target_plus.marketplace.2_2_return_flow
  confidence: high
  review_status: ready
```
```yaml
candidate_card:
  card_type: workflow_step
  card_id: workflow_step.target_plus.return_flow.03
  process_id: business_process.target_plus.return_flow
  step_order: 3
  display_name: Return reason and timing analysis
  description: Return reason analysis uses target_returns.description; return-settlement coverage may lag because returned_date can
    extend beyond settlement cutoff.
  input_tables:
  - table.zs_observe.target_returns
  output_tables:
  - table.zs_observe.target_returns
  - table.zs_observe.target_settlement
  status_conditions:
  - description return reason
  - returned_date timing lag
  evidence_refs:
  - ev.target_plus.marketplace.2_2_return_flow
  confidence: high
  review_status: ready
```
```yaml
candidate_card:
  card_type: workflow_step
  card_id: workflow_step.target_plus.reverse_charge_flow.01
  process_id: business_process.target_plus.reverse_charge_flow
  step_order: 1
  display_name: Marketplace facilitator tax context
  description: Target collects/remits US sales tax; seller settlement shows total_tax=0 and no Indian TCS/TDS fields.
  input_tables:
  - table.zs_observe.target_settlement
  output_tables:
  - table.zs_observe.target_settlement
  status_conditions:
  - total_tax = 0
  - no total_tcs_amount or tds_194o_rate fields
  evidence_refs:
  - ev.target_plus.marketplace.2_3_reverse_charge_flow
  - ev.target_plus.marketplace.4_3_us_sales_tax_marketplace_facilitator_model
  confidence: high
  review_status: ready
```
```yaml
candidate_card:
  card_type: workflow_step
  card_id: workflow_step.target_plus.reverse_charge_flow.02
  process_id: business_process.target_plus.reverse_charge_flow
  step_order: 2
  display_name: Reverse charge settlement row posts
  description: |-
    target_settlement rows with transaction_type=reverse charge and internal_txn_type=others have charged_amount tax base, settled_amount negative, gross_commission=0, and gross_commission_percentage=0.
  input_tables:
  - table.zs_observe.target_settlement
  output_tables:
  - table.zs_observe.target_settlement
  status_conditions:
  - transaction_type='reverse charge'
  - internal_txn_type='others'
  - gross_commission_percentage=0
  evidence_refs:
  - ev.target_plus.marketplace.2_3_reverse_charge_flow
  - ev.target_plus.marketplace.4_3_us_sales_tax_marketplace_facilitator_model
  confidence: high
  review_status: ready
```
```yaml
candidate_card:
  card_type: workflow_step
  card_id: workflow_step.target_plus.product_mapping_enrichment.01
  process_id: business_process.target_plus.product_mapping_enrichment
  step_order: 1
  display_name: Join transaction rows to mapping on TCIN
  description: Use tcin across target_sales, target_returns, target_settlement and target_tcin_mapping; do not use Shopify sku_id as
    a clean seller SKU join.
  input_tables:
  - table.zs_observe.target_sales
  - table.zs_observe.target_returns
  - table.zs_observe.target_settlement
  output_tables:
  - table.zs_observe.target_tcin_mapping
  status_conditions:
  - tcin join key
  - sku_id format caveat
  evidence_refs:
  - ev.target_plus.mapping.1_table_overview
  - ev.target_plus.mapping.4_distinct_value_analysis
  confidence: high
  review_status: ready
```
```yaml
candidate_card:
  card_type: workflow_step
  card_id: workflow_step.target_plus.product_mapping_enrichment.02
  process_id: business_process.target_plus.product_mapping_enrichment
  step_order: 2
  display_name: Apply brand/cross-channel enrichment
  description: target_tcin_mapping provides title-case brand, clean seller SKU, ASIN, and barcode; normalize LOWER(brand) where needed
    and reformat scientific-notation barcodes for product matching.
  input_tables:
  - table.zs_observe.target_tcin_mapping
  output_tables:
  - table.zs_observe.target_tcin_mapping
  status_conditions:
  - LOWER(brand)
  - ASIN present 100%
  - barcode formatting caveat
  evidence_refs:
  - ev.target_plus.mapping.1_table_overview
  - ev.target_plus.mapping.4_distinct_value_analysis
  confidence: high
  review_status: ready
```
### 4.14 reconciliation_profile

```yaml
candidate_card:
  card_type: reconciliation_profile
  card_id: reconciliation_profile.target_plus.sales_settlement
  display_name: Target Plus Sales ↔ Settlement Reconciliation
  reconciliation_family: sales_settlement
  expected_side: target_sales shipped forward orders
  actual_side: target_settlement forward settlement rows
  unit_id: reconciliation_unit.target_plus.item_id_line
  matching_logic_id: matching_logic.target_plus.sales_settlement_item_id
  tolerance: Source SQL uses 0.01 amount tolerance where specified; otherwise review before hard validation.
  timing_window: 'Settlement timing gap: settlement Apr-Nov 2025 while sales/returns extend later.'
  evidence_refs:
  - ev.target_plus.marketplace.6_1_sales_settlement_reconciliation
  confidence: high
  review_status: ready
```
```yaml
candidate_card:
  card_type: reconciliation_profile
  card_id: reconciliation_profile.target_plus.returns_settlement
  display_name: Target Plus Returns ↔ Settlement Refund Match
  reconciliation_family: returns_settlement
  expected_side: target_returns reverse return events
  actual_side: target_settlement reverse settlement rows
  unit_id: reconciliation_unit.target_plus.item_id_line
  matching_logic_id: matching_logic.target_plus.returns_settlement_item_id
  tolerance: Source SQL uses 0.01 amount tolerance where specified; otherwise review before hard validation.
  timing_window: 'Settlement timing gap: settlement Apr-Nov 2025 while sales/returns extend later.'
  evidence_refs:
  - ev.target_plus.marketplace.6_2_returns_settlement_refund_match
  confidence: high
  review_status: ready
```
```yaml
candidate_card:
  card_type: reconciliation_profile
  card_id: reconciliation_profile.target_plus.commission_validation
  display_name: Target Plus Commission Validation
  reconciliation_family: fee_validation
  expected_side: charged_amount_excluding_tax × 0.15
  actual_side: target_settlement.gross_commission
  unit_id: reconciliation_unit.target_plus.item_id_line
  matching_logic_id: matching_logic.target_plus.commission_15pct
  tolerance: 0.01 variance threshold from source SQL.
  timing_window: No timing window; row-level settlement validation.
  evidence_refs:
  - ev.target_plus.marketplace.6_3_commission_validation
  confidence: high
  review_status: ready
```
```yaml
candidate_card:
  card_type: reconciliation_profile
  card_id: reconciliation_profile.target_plus.payout_batch
  display_name: Target Plus Payout Batch Reconciliation
  reconciliation_family: payout_reconciliation
  expected_side: payout_id grouped settlement rows
  actual_side: payout batch total and transaction mix
  unit_id: reconciliation_unit.target_plus.payout_id_batch
  matching_logic_id: matching_logic.target_plus.payout_batch_rollup
  tolerance: Source SQL uses 0.01 amount tolerance where specified; otherwise review before hard validation.
  timing_window: Payout batch spans multiple days; order by earliest_txn from source SQL.
  evidence_refs:
  - ev.target_plus.marketplace.6_4_payout_reconciliation
  confidence: high
  review_status: ready
```
```yaml
candidate_card:
  card_type: reconciliation_profile
  card_id: reconciliation_profile.target_plus.tcin_mapping
  display_name: Target Plus TCIN Mapping Coverage Reconciliation
  reconciliation_family: mapping_coverage
  expected_side: Target transaction TCIN values
  actual_side: target_tcin_mapping TCIN rows
  unit_id: reconciliation_unit.target_plus.tcin_product
  matching_logic_id: matching_logic.target_plus.tcin_mapping_join
  tolerance: Source SQL uses 0.01 amount tolerance where specified; otherwise review before hard validation.
  timing_window: No settlement timing; mapping coverage should be checked by tcin.
  evidence_refs:
  - ev.target_plus.marketplace.3_2_primary_join_keys
  - ev.target_plus.mapping.7_1_full_catalogue_with_sales_coverage
  confidence: high
  review_status: ready
```
### 4.15 reconciliation_side

```yaml
candidate_card:
  card_type: reconciliation_side
  card_id: reconciliation_side.target_plus.sales_settlement.sales
  profile_id: reconciliation_profile.target_plus.sales_settlement
  side_role: expected
  source_table_id: table.zs_observe.target_sales
  key_columns:
  - column.zs_observe.target_sales.item_id
  - column.zs_observe.target_sales.order_id
  - column.zs_observe.target_sales.brand
  amount_columns:
  - column.zs_observe.target_sales.charged_amount
  date_columns:
  - column.zs_observe.target_sales.created_date
  status_columns:
  - column.zs_observe.target_sales.order_status
  - column.zs_observe.target_sales.transaction_type
  filters:
  - is_active = true
  - order_status = SHIPPED
  grain: sales item_id/order-line
  evidence_refs:
  - ev.target_plus.marketplace.6_1_sales_settlement_reconciliation
  confidence: high
  review_status: ready
```
```yaml
candidate_card:
  card_type: reconciliation_side
  card_id: reconciliation_side.target_plus.sales_settlement.settlement
  profile_id: reconciliation_profile.target_plus.sales_settlement
  side_role: actual
  source_table_id: table.zs_observe.target_settlement
  key_columns:
  - column.zs_observe.target_settlement.item_id
  - column.zs_observe.target_settlement.order_id
  - column.zs_observe.target_settlement.brand
  amount_columns:
  - column.zs_observe.target_settlement.charged_amount
  - column.zs_observe.target_settlement.charged_amount_excluding_tax
  - column.zs_observe.target_settlement.gross_commission
  - column.zs_observe.target_settlement.settled_amount
  date_columns:
  - column.zs_observe.target_settlement.created_date
  status_columns:
  - column.zs_observe.target_settlement.transaction_type
  - column.zs_observe.target_settlement.internal_txn_type
  filters:
  - is_active = true
  - transaction_type = forward
  grain: settlement item_id/event-line
  evidence_refs:
  - ev.target_plus.marketplace.6_1_sales_settlement_reconciliation
  confidence: high
  review_status: ready
```
```yaml
candidate_card:
  card_type: reconciliation_side
  card_id: reconciliation_side.target_plus.returns_settlement.returns
  profile_id: reconciliation_profile.target_plus.returns_settlement
  side_role: expected
  source_table_id: table.zs_observe.target_returns
  key_columns:
  - column.zs_observe.target_returns.item_id
  - column.zs_observe.target_returns.order_id
  - column.zs_observe.target_returns.tcin
  amount_columns:
  - column.zs_observe.target_returns.charged_amount
  date_columns:
  - column.zs_observe.target_returns.returned_date
  - column.zs_observe.target_returns.created_date
  status_columns:
  - column.zs_observe.target_returns.internal_txn_type
  - column.zs_observe.target_returns.transaction_type
  filters:
  - is_active = true
  - internal_txn_type = reverse
  grain: return item_id/event-line
  evidence_refs:
  - ev.target_plus.marketplace.6_2_returns_settlement_refund_match
  confidence: high
  review_status: ready
```
```yaml
candidate_card:
  card_type: reconciliation_side
  card_id: reconciliation_side.target_plus.returns_settlement.settlement
  profile_id: reconciliation_profile.target_plus.returns_settlement
  side_role: actual
  source_table_id: table.zs_observe.target_settlement
  key_columns:
  - column.zs_observe.target_settlement.item_id
  - column.zs_observe.target_settlement.order_id
  - column.zs_observe.target_settlement.tcin
  amount_columns:
  - column.zs_observe.target_settlement.settled_amount
  - column.zs_observe.target_settlement.gross_commission
  - column.zs_observe.target_settlement.charged_amount_excluding_tax
  date_columns:
  - column.zs_observe.target_settlement.returned_date
  - column.zs_observe.target_settlement.created_date
  status_columns:
  - column.zs_observe.target_settlement.transaction_type
  - column.zs_observe.target_settlement.internal_txn_type
  filters:
  - is_active = true
  - transaction_type = reverse
  grain: settlement refund event-line
  evidence_refs:
  - ev.target_plus.marketplace.6_2_returns_settlement_refund_match
  confidence: high
  review_status: ready
```
```yaml
candidate_card:
  card_type: reconciliation_side
  card_id: reconciliation_side.target_plus.commission_validation.settlement_expected
  profile_id: reconciliation_profile.target_plus.commission_validation
  side_role: expected
  source_table_id: table.zs_observe.target_settlement
  key_columns:
  - column.zs_observe.target_settlement.item_id
  - column.zs_observe.target_settlement.transfer_id
  amount_columns:
  - column.zs_observe.target_settlement.charged_amount_excluding_tax
  date_columns:
  - column.zs_observe.target_settlement.created_date
  status_columns:
  - column.zs_observe.target_settlement.transaction_type
  filters:
  - is_active = true
  - transaction_type = forward
  grain: settlement row
  evidence_refs:
  - ev.target_plus.marketplace.6_3_commission_validation
  confidence: high
  review_status: ready
```
```yaml
candidate_card:
  card_type: reconciliation_side
  card_id: reconciliation_side.target_plus.commission_validation.settlement_actual
  profile_id: reconciliation_profile.target_plus.commission_validation
  side_role: actual
  source_table_id: table.zs_observe.target_settlement
  key_columns:
  - column.zs_observe.target_settlement.item_id
  - column.zs_observe.target_settlement.transfer_id
  amount_columns:
  - column.zs_observe.target_settlement.gross_commission
  date_columns:
  - column.zs_observe.target_settlement.created_date
  status_columns:
  - column.zs_observe.target_settlement.transaction_type
  filters:
  - is_active = true
  - transaction_type = forward
  grain: settlement row
  evidence_refs:
  - ev.target_plus.marketplace.6_3_commission_validation
  confidence: high
  review_status: ready
```
```yaml
candidate_card:
  card_type: reconciliation_side
  card_id: reconciliation_side.target_plus.payout_batch.settlement_rows
  profile_id: reconciliation_profile.target_plus.payout_batch
  side_role: actual
  source_table_id: table.zs_observe.target_settlement
  key_columns:
  - column.zs_observe.target_settlement.payout_id
  - column.zs_observe.target_settlement.order_id
  amount_columns:
  - column.zs_observe.target_settlement.settled_amount
  date_columns:
  - column.zs_observe.target_settlement.created_date
  status_columns:
  - column.zs_observe.target_settlement.transaction_type
  filters:
  - is_active = true
  grain: settlement event rows grouped by payout_id
  evidence_refs:
  - ev.target_plus.marketplace.6_4_payout_reconciliation
  confidence: high
  review_status: ready
```
```yaml
candidate_card:
  card_type: reconciliation_side
  card_id: reconciliation_side.target_plus.payout_batch.batch_rollup
  profile_id: reconciliation_profile.target_plus.payout_batch
  side_role: summary
  source_table_id: table.zs_observe.target_settlement
  key_columns:
  - column.zs_observe.target_settlement.payout_id
  amount_columns:
  - column.zs_observe.target_settlement.settled_amount
  date_columns:
  - column.zs_observe.target_settlement.created_date
  status_columns:
  - column.zs_observe.target_settlement.transaction_type
  filters:
  - is_active = true
  grain: payout_id aggregate
  evidence_refs:
  - ev.target_plus.marketplace.6_4_payout_reconciliation
  confidence: high
  review_status: ready
```
```yaml
candidate_card:
  card_type: reconciliation_side
  card_id: reconciliation_side.target_plus.tcin_mapping.transaction_tcins
  profile_id: reconciliation_profile.target_plus.tcin_mapping
  side_role: expected
  source_table_id: table.zs_observe.target_sales
  key_columns:
  - column.zs_observe.target_sales.tcin
  amount_columns:
  - column.zs_observe.target_sales.charged_amount
  date_columns:
  - column.zs_observe.target_sales.created_date
  status_columns:
  - column.zs_observe.target_sales.order_status
  filters:
  - is_active = true
  grain: sales TCIN values
  evidence_refs:
  - ev.target_plus.mapping.7_1_full_catalogue_with_sales_coverage
  confidence: high
  review_status: ready
```
```yaml
candidate_card:
  card_type: reconciliation_side
  card_id: reconciliation_side.target_plus.tcin_mapping.mapping
  profile_id: reconciliation_profile.target_plus.tcin_mapping
  side_role: actual
  source_table_id: table.zs_observe.target_tcin_mapping
  key_columns:
  - column.zs_observe.target_tcin_mapping.tcin
  - column.zs_observe.target_tcin_mapping.sku_id
  - column.zs_observe.target_tcin_mapping.asin
  amount_columns: []
  date_columns: []
  status_columns:
  - column.zs_observe.target_tcin_mapping.brand
  filters:
  - is_active = true
  grain: mapping TCIN product rows
  evidence_refs:
  - ev.target_plus.mapping.7_1_full_catalogue_with_sales_coverage
  confidence: high
  review_status: ready
```
### 4.16 reconciliation_unit

```yaml
candidate_card:
  card_type: reconciliation_unit
  card_id: reconciliation_unit.target_plus.item_id_line
  display_name: Target Plus item_id order-line unit
  unit_type: order_line
  unit_keys:
  - item_id
  grain: one Target order-line item
  aggregation_rule: Aggregate settlement rows by item_id and transaction_type before comparing sales/returns.
  evidence_refs:
  - ev.target_plus.marketplace.3_2_primary_join_keys
  confidence: high
  review_status: ready
```
```yaml
candidate_card:
  card_type: reconciliation_unit
  card_id: reconciliation_unit.target_plus.order_id_order
  display_name: Target Plus order_id order unit
  unit_type: order
  unit_keys:
  - order_id
  grain: Target order
  aggregation_rule: Use order_id for sales↔returns and brand return-rate analyses.
  evidence_refs:
  - ev.target_plus.marketplace.3_2_primary_join_keys
  confidence: high
  review_status: ready
```
```yaml
candidate_card:
  card_type: reconciliation_unit
  card_id: reconciliation_unit.target_plus.payout_id_batch
  display_name: Target Plus payout_id batch unit
  unit_type: payout_batch
  unit_keys:
  - payout_id
  grain: Stripe payout batch
  aggregation_rule: Aggregate all settlement rows by payout_id for payout reconciliation.
  evidence_refs:
  - ev.target_plus.marketplace.6_4_payout_reconciliation
  confidence: high
  review_status: ready
```
```yaml
candidate_card:
  card_type: reconciliation_unit
  card_id: reconciliation_unit.target_plus.tcin_product
  display_name: Target Plus TCIN product unit
  unit_type: product_variant
  unit_keys:
  - tcin
  grain: Target product variant
  aggregation_rule: Join mapping by tcin and aggregate sales/returns as needed.
  evidence_refs:
  - ev.target_plus.marketplace.3_1_join_map
  confidence: high
  review_status: ready
```
### 4.17 matching_logic

```yaml
candidate_card:
  card_type: matching_logic
  card_id: matching_logic.target_plus.sales_settlement_item_id
  display_name: Sales to settlement item_id matching
  match_type: left_join
  join_condition: target_sales.item_id = target_settlement.item_id AND target_settlement.transaction_type = forward
  key_normalization: Use exact key match unless brand case normalization or date casting is explicitly documented.
  amount_comparison: Compare target_sales.charged_amount to target_settlement.charged_amount or charged_amount_excluding_tax depending
    on multi-quantity context.
  aggregation_order: Filter sales shipped, settlement active forward; do not compare Dec sales unless settlement period available.
  timing_rule: Date-align periods because settlement ends before sales/returns source range.
  tolerance_rule: 0.01 where source SQL states; otherwise documented as review-required before hard failure.
  evidence_refs:
  - ev.target_plus.marketplace.6_1_sales_settlement_reconciliation
  confidence: high
  review_status: ready
```
```yaml
candidate_card:
  card_type: matching_logic
  card_id: matching_logic.target_plus.returns_settlement_item_id
  display_name: Returns to settlement refund matching
  match_type: left_join
  join_condition: target_returns.item_id = target_settlement.item_id AND target_settlement.transaction_type = reverse
  key_normalization: Use exact key match unless brand case normalization or date casting is explicitly documented.
  amount_comparison: Compare target_returns.charged_amount to ABS/negative refund settlement impact based on source SQL output.
  aggregation_order: Filter returns internal_txn_type=reverse and settlement transaction_type=reverse.
  timing_rule: Date-align periods because settlement ends before sales/returns source range.
  tolerance_rule: 0.01 where source SQL states; otherwise documented as review-required before hard failure.
  evidence_refs:
  - ev.target_plus.marketplace.6_2_returns_settlement_refund_match
  confidence: high
  review_status: ready
```
```yaml
candidate_card:
  card_type: matching_logic
  card_id: matching_logic.target_plus.commission_15pct
  display_name: Commission 15 percent validation
  match_type: formula_comparison
  join_condition: target_settlement rows filtered to transaction_type = forward
  key_normalization: Use exact key match unless brand case normalization or date casting is explicitly documented.
  amount_comparison: ABS(gross_commission - ROUND(charged_amount_excluding_tax * 0.15, 4)) > 0.01 flags variance.
  aggregation_order: No join required; row-level settlement validation.
  timing_rule: Date-align periods because settlement ends before sales/returns source range.
  tolerance_rule: 0.01 amount variance from source SQL.
  evidence_refs:
  - ev.target_plus.marketplace.6_3_commission_validation
  confidence: high
  review_status: ready
```
```yaml
candidate_card:
  card_type: matching_logic
  card_id: matching_logic.target_plus.payout_batch_rollup
  display_name: Payout batch settlement rollup
  match_type: group_by
  join_condition: GROUP BY target_settlement.payout_id
  key_normalization: Use exact key match unless brand case normalization or date casting is explicitly documented.
  amount_comparison: SUM(settled_amount), COUNT(DISTINCT order_id), transaction-type row counts per payout_id.
  aggregation_order: Aggregate settlement rows by payout_id.
  timing_rule: Date-align periods because settlement ends before sales/returns source range.
  tolerance_rule: 0.01 where source SQL states; otherwise documented as review-required before hard failure.
  evidence_refs:
  - ev.target_plus.marketplace.6_4_payout_reconciliation
  confidence: high
  review_status: ready
```
```yaml
candidate_card:
  card_type: matching_logic
  card_id: matching_logic.target_plus.tcin_mapping_join
  display_name: TCIN mapping enrichment matching
  match_type: join
  join_condition: transaction_table.tcin = target_tcin_mapping.tcin
  key_normalization: Use exact key match unless brand case normalization or date casting is explicitly documented.
  amount_comparison: No amount comparison; enrich with clean seller SKU, brand, ASIN, and barcode.
  aggregation_order: Join mapping first, then aggregate by SKU/brand as needed.
  timing_rule: Date-align periods because settlement ends before sales/returns source range.
  tolerance_rule: 0.01 where source SQL states; otherwise documented as review-required before hard failure.
  evidence_refs:
  - ev.target_plus.mapping.7_3_enrich_sales_with_mapping_data
  - ev.target_plus.marketplace.3_1_join_map
  confidence: high
  review_status: ready
```
### 4.18 mismatch_category

```yaml
candidate_card:
  card_type: mismatch_category
  card_id: mismatch_category.target_plus.sales_settlement.not_yet_settled
  profile_id: reconciliation_profile.target_plus.sales_settlement
  display_name: Not Yet Settled
  mismatch_type: timing_gap
  detection_logic: settlement.item_id IS NULL
  business_meaning: Expected for Dec 2025 sales or future settlement timing gaps; not automatically a data-quality defect.
  review_priority: low
  evidence_refs:
  - ev.target_plus.marketplace.3_2_primary_join_keys
  confidence: high
  review_status: ready
```
```yaml
candidate_card:
  card_type: mismatch_category
  card_id: mismatch_category.target_plus.sales_settlement.price_variance
  profile_id: reconciliation_profile.target_plus.sales_settlement
  display_name: Price Variance
  mismatch_type: amount_variance
  detection_logic: ABS(sales.charged_amount - settlement.charged_amount) >= 0.01
  business_meaning: Sales price and settlement price differ beyond source tolerance.
  review_priority: high
  evidence_refs:
  - ev.target_plus.marketplace.6_1_sales_settlement_reconciliation
  confidence: high
  review_status: ready
```
```yaml
candidate_card:
  card_type: mismatch_category
  card_id: mismatch_category.target_plus.returns_settlement.refund_pending
  profile_id: reconciliation_profile.target_plus.returns_settlement
  display_name: Refund Pending
  mismatch_type: timing_gap
  detection_logic: settlement.item_id IS NULL
  business_meaning: Return exists but corresponding settlement refund is not yet posted or outside settlement date range.
  review_priority: medium
  evidence_refs:
  - ev.target_plus.marketplace.6_2_returns_settlement_refund_match
  confidence: high
  review_status: ready
```
```yaml
candidate_card:
  card_type: mismatch_category
  card_id: mismatch_category.target_plus.returns_settlement.refund_settled
  profile_id: reconciliation_profile.target_plus.returns_settlement
  display_name: Refund Settled
  mismatch_type: matched
  detection_logic: settlement.item_id IS NOT NULL
  business_meaning: Return has matching reverse settlement row.
  review_priority: low
  evidence_refs:
  - ev.target_plus.marketplace.6_2_returns_settlement_refund_match
  confidence: high
  review_status: ready
```
```yaml
candidate_card:
  card_type: mismatch_category
  card_id: mismatch_category.target_plus.commission_validation.commission_variance
  profile_id: reconciliation_profile.target_plus.commission_validation
  display_name: Commission Variance
  mismatch_type: amount_variance
  detection_logic: ABS(gross_commission - ROUND(charged_amount_excluding_tax * 0.15, 4)) > 0.01
  business_meaning: Actual commission deviates from source-confirmed flat 15% rule.
  review_priority: high
  evidence_refs:
  - ev.target_plus.marketplace.6_3_commission_validation
  confidence: high
  review_status: ready
```
```yaml
candidate_card:
  card_type: mismatch_category
  card_id: mismatch_category.target_plus.payout_batch.empty_batch
  profile_id: reconciliation_profile.target_plus.payout_batch
  display_name: Empty or missing payout batch
  mismatch_type: missing_key
  detection_logic: payout_id IS NULL or no rows after active filter
  business_meaning: Payout grouping cannot be produced for rows without payout_id.
  review_priority: medium
  evidence_refs:
  - ev.target_plus.settlement.payout_batch_structure_2
  confidence: high
  review_status: ready
```
```yaml
candidate_card:
  card_type: mismatch_category
  card_id: mismatch_category.target_plus.tcin_mapping.missing_mapping
  profile_id: reconciliation_profile.target_plus.tcin_mapping
  display_name: Missing TCIN Mapping
  mismatch_type: missing_mapping
  detection_logic: target_tcin_mapping.tcin IS NULL after LEFT JOIN
  business_meaning: Sales TCIN is not represented in mapping table; source reports high coverage but not necessarily perfect.
  review_priority: medium
  evidence_refs:
  - ev.target_plus.mapping.7_1_full_catalogue_with_sales_coverage
  confidence: high
  review_status: ready
```
### 4.19 query_pattern

```yaml
candidate_card:
  card_type: query_pattern
  card_id: query_pattern.target_plus.marketplace.5_1_total_gmv
  display_name: Target Plus query pattern — 5.1 Total GMV
  intent: 5.1 Total GMV
  natural_language_patterns:
  - 5.1 Total GMV
  - Target Plus 5.1 Total GMV
  source_tables:
  - table.zs_observe.target_sales
  required_filters:
  - rule.target_plus.active_filter
  sql_ref: sql.target_plus.marketplace.5_1_total_gmv
  primary_metric_id: metric.target_plus.total_gmv
  reconciliation_profile_ids: []
  output_contract_id: output_contract.target_plus.metric_timeseries
  execution_constraints:
  - execution_constraint_set.target_plus.marketplace_parser_constraints
  evidence_refs:
  - ev.target_plus.marketplace.5_1_total_gmv
  confidence: high
  review_status: ready
```
```yaml
candidate_card:
  card_type: query_pattern
  card_id: query_pattern.target_plus.marketplace.5_2_net_revenue_settlement_view
  display_name: Target Plus query pattern — 5.2 Net Revenue (Settlement View)
  intent: 5.2 Net Revenue (Settlement View)
  natural_language_patterns:
  - 5.2 Net Revenue (Settlement View)
  - Target Plus 5.2 Net Revenue (Settlement View)
  source_tables:
  - table.zs_observe.target_settlement
  required_filters:
  - rule.target_plus.active_filter
  - rule.target_plus.currency_label_usd_values
  - rule.target_plus.settlement_recency_gap
  - rule.target_plus.reverse_charge_not_return
  sql_ref: sql.target_plus.marketplace.5_2_net_revenue_settlement_view
  primary_metric_id: metric.target_plus.net_settlement_revenue
  reconciliation_profile_ids: []
  output_contract_id: output_contract.target_plus.metric_timeseries
  execution_constraints:
  - execution_constraint_set.target_plus.marketplace_parser_constraints
  evidence_refs:
  - ev.target_plus.marketplace.5_2_net_revenue_settlement_view
  confidence: high
  review_status: ready
```
```yaml
candidate_card:
  card_type: query_pattern
  card_id: query_pattern.target_plus.marketplace.5_3_return_rate
  display_name: Target Plus query pattern — 5.3 Return Rate
  intent: 5.3 Return Rate
  natural_language_patterns:
  - 5.3 Return Rate
  - Target Plus 5.3 Return Rate
  source_tables:
  - table.zs_observe.target_returns
  - table.zs_observe.target_sales
  required_filters:
  - rule.target_plus.active_filter
  sql_ref: sql.target_plus.marketplace.5_3_return_rate
  primary_metric_id: metric.target_plus.return_rate
  reconciliation_profile_ids: []
  output_contract_id: output_contract.target_plus.metric_timeseries
  execution_constraints:
  - execution_constraint_set.target_plus.marketplace_parser_constraints
  evidence_refs:
  - ev.target_plus.marketplace.5_3_return_rate
  confidence: high
  review_status: ready
```
```yaml
candidate_card:
  card_type: query_pattern
  card_id: query_pattern.target_plus.marketplace.5_4_average_order_value_aov
  display_name: Target Plus query pattern — 5.4 Average Order Value (AOV)
  intent: 5.4 Average Order Value (AOV)
  natural_language_patterns:
  - 5.4 Average Order Value (AOV)
  - Target Plus 5.4 Average Order Value (AOV)
  source_tables:
  - table.zs_observe.target_sales
  required_filters:
  - rule.target_plus.active_filter
  sql_ref: sql.target_plus.marketplace.5_4_average_order_value_aov
  primary_metric_id: metric.target_plus.aov
  reconciliation_profile_ids: []
  output_contract_id: output_contract.target_plus.metric_timeseries
  execution_constraints:
  - execution_constraint_set.target_plus.marketplace_parser_constraints
  evidence_refs:
  - ev.target_plus.marketplace.5_4_average_order_value_aov
  confidence: high
  review_status: ready
```
```yaml
candidate_card:
  card_type: query_pattern
  card_id: query_pattern.target_plus.marketplace.5_5_effective_payout_rate
  display_name: Target Plus query pattern — 5.5 Effective Payout Rate
  intent: 5.5 Effective Payout Rate
  natural_language_patterns:
  - 5.5 Effective Payout Rate
  - Target Plus 5.5 Effective Payout Rate
  source_tables:
  - table.zs_observe.target_settlement
  required_filters:
  - rule.target_plus.active_filter
  - rule.target_plus.currency_label_usd_values
  sql_ref: sql.target_plus.marketplace.5_5_effective_payout_rate
  primary_metric_id: metric.target_plus.effective_payout_rate
  reconciliation_profile_ids: []
  output_contract_id: output_contract.target_plus.metric_timeseries
  execution_constraints:
  - execution_constraint_set.target_plus.marketplace_parser_constraints
  evidence_refs:
  - ev.target_plus.marketplace.5_5_effective_payout_rate
  confidence: high
  review_status: ready
```
```yaml
candidate_card:
  card_type: query_pattern
  card_id: query_pattern.target_plus.marketplace.5_6_top_selling_skus
  display_name: Target Plus query pattern — 5.6 Top Selling SKUs
  intent: 5.6 Top Selling SKUs
  natural_language_patterns:
  - 5.6 Top Selling SKUs
  - Target Plus 5.6 Top Selling SKUs
  source_tables:
  - table.zs_observe.target_sales
  - table.zs_observe.target_tcin_mapping
  required_filters:
  - rule.target_plus.active_filter
  sql_ref: sql.target_plus.marketplace.5_6_top_selling_skus
  primary_metric_id: metric.target_plus.top_selling_skus
  reconciliation_profile_ids: []
  output_contract_id: output_contract.target_plus.metric_timeseries
  execution_constraints:
  - execution_constraint_set.target_plus.marketplace_parser_constraints
  evidence_refs:
  - ev.target_plus.marketplace.5_6_top_selling_skus
  confidence: high
  review_status: ready
```
```yaml
candidate_card:
  card_type: query_pattern
  card_id: query_pattern.target_plus.marketplace.5_7_cancellation_rate
  display_name: Target Plus query pattern — 5.7 Cancellation Rate
  intent: 5.7 Cancellation Rate
  natural_language_patterns:
  - 5.7 Cancellation Rate
  - Target Plus 5.7 Cancellation Rate
  source_tables:
  - table.zs_observe.target_sales
  required_filters:
  - rule.target_plus.active_filter
  sql_ref: sql.target_plus.marketplace.5_7_cancellation_rate
  primary_metric_id: metric.target_plus.cancellation_rate
  reconciliation_profile_ids: []
  output_contract_id: output_contract.target_plus.metric_timeseries
  execution_constraints:
  - execution_constraint_set.target_plus.marketplace_parser_constraints
  evidence_refs:
  - ev.target_plus.marketplace.5_7_cancellation_rate
  confidence: high
  review_status: ready
```
```yaml
candidate_card:
  card_type: query_pattern
  card_id: query_pattern.target_plus.marketplace.6_1_sales_settlement_reconciliation
  display_name: Target Plus query pattern — 6.1 Sales ↔ Settlement Reconciliation
  intent: 6.1 Sales ↔ Settlement Reconciliation
  natural_language_patterns:
  - 6.1 Sales ↔ Settlement Reconciliation
  - Target Plus 6.1 Sales ↔ Settlement Reconciliation
  source_tables:
  - table.zs_observe.target_sales
  - table.zs_observe.target_settlement
  required_filters:
  - rule.target_plus.active_filter
  - rule.target_plus.currency_label_usd_values
  - rule.target_plus.settlement_recency_gap
  sql_ref: sql.target_plus.marketplace.6_1_sales_settlement_reconciliation
  primary_metric_id: null
  reconciliation_profile_ids:
  - reconciliation_profile.target_plus.sales_settlement
  output_contract_id: output_contract.target_plus.reconciliation_status
  execution_constraints:
  - execution_constraint_set.target_plus.marketplace_parser_constraints
  evidence_refs:
  - ev.target_plus.marketplace.6_1_sales_settlement_reconciliation
  confidence: high
  review_status: ready
```
```yaml
candidate_card:
  card_type: query_pattern
  card_id: query_pattern.target_plus.marketplace.6_2_returns_settlement_refund_match
  display_name: Target Plus query pattern — 6.2 Returns ↔ Settlement Refund Match
  intent: 6.2 Returns ↔ Settlement Refund Match
  natural_language_patterns:
  - 6.2 Returns ↔ Settlement Refund Match
  - Target Plus 6.2 Returns ↔ Settlement Refund Match
  source_tables:
  - table.zs_observe.target_returns
  - table.zs_observe.target_settlement
  required_filters:
  - rule.target_plus.active_filter
  - rule.target_plus.currency_label_usd_values
  - rule.target_plus.settlement_recency_gap
  sql_ref: sql.target_plus.marketplace.6_2_returns_settlement_refund_match
  primary_metric_id: null
  reconciliation_profile_ids:
  - reconciliation_profile.target_plus.returns_settlement
  output_contract_id: output_contract.target_plus.reconciliation_status
  execution_constraints:
  - execution_constraint_set.target_plus.marketplace_parser_constraints
  evidence_refs:
  - ev.target_plus.marketplace.6_2_returns_settlement_refund_match
  confidence: high
  review_status: ready
```
```yaml
candidate_card:
  card_type: query_pattern
  card_id: query_pattern.target_plus.marketplace.6_3_commission_validation
  display_name: Target Plus query pattern — 6.3 Commission Validation
  intent: 6.3 Commission Validation
  natural_language_patterns:
  - 6.3 Commission Validation
  - Target Plus 6.3 Commission Validation
  source_tables:
  - table.zs_observe.target_settlement
  required_filters:
  - rule.target_plus.active_filter
  - rule.target_plus.currency_label_usd_values
  sql_ref: sql.target_plus.marketplace.6_3_commission_validation
  primary_metric_id: metric.target_plus.commission_validation_variance
  reconciliation_profile_ids:
  - reconciliation_profile.target_plus.commission_validation
  output_contract_id: output_contract.target_plus.reconciliation_status
  execution_constraints:
  - execution_constraint_set.target_plus.marketplace_parser_constraints
  evidence_refs:
  - ev.target_plus.marketplace.6_3_commission_validation
  confidence: high
  review_status: ready
```
```yaml
candidate_card:
  card_type: query_pattern
  card_id: query_pattern.target_plus.marketplace.6_4_payout_reconciliation
  display_name: Target Plus query pattern — 6.4 Payout Reconciliation
  intent: 6.4 Payout Reconciliation
  natural_language_patterns:
  - 6.4 Payout Reconciliation
  - Target Plus 6.4 Payout Reconciliation
  source_tables:
  - table.zs_observe.target_settlement
  required_filters:
  - rule.target_plus.active_filter
  - rule.target_plus.currency_label_usd_values
  - rule.target_plus.settlement_recency_gap
  - rule.target_plus.reverse_charge_not_return
  sql_ref: sql.target_plus.marketplace.6_4_payout_reconciliation
  primary_metric_id: metric.target_plus.payout_batch_total
  reconciliation_profile_ids:
  - reconciliation_profile.target_plus.payout_batch
  output_contract_id: output_contract.target_plus.reconciliation_status
  execution_constraints:
  - execution_constraint_set.target_plus.marketplace_parser_constraints
  evidence_refs:
  - ev.target_plus.marketplace.6_4_payout_reconciliation
  confidence: high
  review_status: ready
```
```yaml
candidate_card:
  card_type: query_pattern
  card_id: query_pattern.target_plus.marketplace.8_mandatory_query_filters
  display_name: Target Plus query pattern — 8. Mandatory Query Filters
  intent: 8. Mandatory Query Filters
  natural_language_patterns:
  - 8. Mandatory Query Filters
  - Target Plus 8. Mandatory Query Filters
  source_tables: []
  required_filters: []
  sql_ref: sql.target_plus.marketplace.8_mandatory_query_filters
  primary_metric_id: null
  reconciliation_profile_ids: []
  output_contract_id: output_contract.target_plus.metric_timeseries
  execution_constraints:
  - execution_constraint_set.target_plus.marketplace_parser_constraints
  evidence_refs:
  - ev.target_plus.marketplace.8_mandatory_query_filters
  confidence: high
  review_status: ready
```
```yaml
candidate_card:
  card_type: query_pattern
  card_id: query_pattern.target_plus.settlement.8_1_payout_batch_summary
  display_name: Target Plus query pattern — 8.1 Payout Batch Summary
  intent: 8.1 Payout Batch Summary
  natural_language_patterns:
  - 8.1 Payout Batch Summary
  - Target Plus 8.1 Payout Batch Summary
  source_tables:
  - table.zs_observe.target_settlement
  required_filters:
  - rule.target_plus.active_filter
  - rule.target_plus.currency_label_usd_values
  - rule.target_plus.reverse_charge_not_return
  sql_ref: sql.target_plus.settlement.8_1_payout_batch_summary
  primary_metric_id: null
  reconciliation_profile_ids:
  - reconciliation_profile.target_plus.payout_batch
  output_contract_id: output_contract.target_plus.reconciliation_status
  execution_constraints:
  - execution_constraint_set.target_plus.marketplace_parser_constraints
  evidence_refs:
  - ev.target_plus.settlement.8_1_payout_batch_summary_2
  confidence: high
  review_status: ready
```
```yaml
candidate_card:
  card_type: query_pattern
  card_id: query_pattern.target_plus.settlement.8_2_monthly_settlement_waterfall
  display_name: Target Plus query pattern — 8.2 Monthly Settlement Waterfall
  intent: 8.2 Monthly Settlement Waterfall
  natural_language_patterns:
  - 8.2 Monthly Settlement Waterfall
  - Target Plus 8.2 Monthly Settlement Waterfall
  source_tables:
  - table.zs_observe.target_settlement
  required_filters:
  - rule.target_plus.active_filter
  - rule.target_plus.currency_label_usd_values
  - rule.target_plus.settlement_recency_gap
  - rule.target_plus.reverse_charge_not_return
  sql_ref: sql.target_plus.settlement.8_2_monthly_settlement_waterfall
  primary_metric_id: null
  reconciliation_profile_ids: []
  output_contract_id: output_contract.target_plus.metric_timeseries
  execution_constraints:
  - execution_constraint_set.target_plus.marketplace_parser_constraints
  evidence_refs:
  - ev.target_plus.settlement.8_2_monthly_settlement_waterfall_2
  confidence: high
  review_status: ready
```
```yaml
candidate_card:
  card_type: query_pattern
  card_id: query_pattern.target_plus.settlement.8_3_commission_validation
  display_name: Target Plus query pattern — 8.3 Commission Validation
  intent: 8.3 Commission Validation
  natural_language_patterns:
  - 8.3 Commission Validation
  - Target Plus 8.3 Commission Validation
  source_tables:
  - table.zs_observe.target_settlement
  required_filters:
  - rule.target_plus.active_filter
  - rule.target_plus.currency_label_usd_values
  sql_ref: sql.target_plus.settlement.8_3_commission_validation
  primary_metric_id: null
  reconciliation_profile_ids:
  - reconciliation_profile.target_plus.commission_validation
  output_contract_id: output_contract.target_plus.reconciliation_status
  execution_constraints:
  - execution_constraint_set.target_plus.marketplace_parser_constraints
  evidence_refs:
  - ev.target_plus.settlement.8_3_commission_validation_2
  confidence: high
  review_status: ready
```
```yaml
candidate_card:
  card_type: query_pattern
  card_id: query_pattern.target_plus.settlement.8_4_sales_settlement_reconciliation
  display_name: Target Plus query pattern — 8.4 Sales ↔ Settlement Reconciliation
  intent: 8.4 Sales ↔ Settlement Reconciliation
  natural_language_patterns:
  - 8.4 Sales ↔ Settlement Reconciliation
  - Target Plus 8.4 Sales ↔ Settlement Reconciliation
  source_tables:
  - table.zs_observe.target_sales
  - table.zs_observe.target_settlement
  required_filters:
  - rule.target_plus.active_filter
  - rule.target_plus.currency_label_usd_values
  - rule.target_plus.settlement_recency_gap
  sql_ref: sql.target_plus.settlement.8_4_sales_settlement_reconciliation
  primary_metric_id: null
  reconciliation_profile_ids:
  - reconciliation_profile.target_plus.sales_settlement
  output_contract_id: output_contract.target_plus.reconciliation_status
  execution_constraints:
  - execution_constraint_set.target_plus.marketplace_parser_constraints
  evidence_refs:
  - ev.target_plus.settlement.8_4_sales_settlement_reconciliation_2
  confidence: high
  review_status: ready
```
```yaml
candidate_card:
  card_type: query_pattern
  card_id: query_pattern.target_plus.settlement.8_5_effective_payout_rate
  display_name: Target Plus query pattern — 8.5 Effective Payout Rate
  intent: 8.5 Effective Payout Rate
  natural_language_patterns:
  - 8.5 Effective Payout Rate
  - Target Plus 8.5 Effective Payout Rate
  source_tables:
  - table.zs_observe.target_settlement
  required_filters:
  - rule.target_plus.active_filter
  - rule.target_plus.currency_label_usd_values
  sql_ref: sql.target_plus.settlement.8_5_effective_payout_rate
  primary_metric_id: null
  reconciliation_profile_ids: []
  output_contract_id: output_contract.target_plus.metric_timeseries
  execution_constraints:
  - execution_constraint_set.target_plus.marketplace_parser_constraints
  evidence_refs:
  - ev.target_plus.settlement.8_5_effective_payout_rate_2
  confidence: high
  review_status: ready
```
```yaml
candidate_card:
  card_type: query_pattern
  card_id: query_pattern.target_plus.mapping.7_1_full_catalogue_with_sales_coverage
  display_name: Target Plus query pattern — 7.1 Full Catalogue with Sales Coverage
  intent: 7.1 Full Catalogue with Sales Coverage
  natural_language_patterns:
  - 7.1 Full Catalogue with Sales Coverage
  - Target Plus 7.1 Full Catalogue with Sales Coverage
  source_tables:
  - table.zs_observe.target_sales
  - table.zs_observe.target_tcin_mapping
  required_filters:
  - rule.target_plus.active_filter
  - rule.target_plus.tcin_mapping_join
  sql_ref: sql.target_plus.mapping.7_1_full_catalogue_with_sales_coverage
  primary_metric_id: metric.target_plus.mapping_sales_coverage
  reconciliation_profile_ids:
  - reconciliation_profile.target_plus.tcin_mapping
  output_contract_id: output_contract.target_plus.reconciliation_status
  execution_constraints:
  - execution_constraint_set.target_plus.marketplace_parser_constraints
  evidence_refs:
  - ev.target_plus.mapping.7_1_full_catalogue_with_sales_coverage
  confidence: high
  review_status: ready
```
```yaml
candidate_card:
  card_type: query_pattern
  card_id: query_pattern.target_plus.mapping.7_2_brand_level_sku_count
  display_name: Target Plus query pattern — 7.2 Brand-Level SKU Count
  intent: 7.2 Brand-Level SKU Count
  natural_language_patterns:
  - 7.2 Brand-Level SKU Count
  - Target Plus 7.2 Brand-Level SKU Count
  source_tables:
  - table.zs_observe.target_tcin_mapping
  required_filters:
  - rule.target_plus.active_filter
  sql_ref: sql.target_plus.mapping.7_2_brand_level_sku_count
  primary_metric_id: null
  reconciliation_profile_ids: []
  output_contract_id: output_contract.target_plus.product_mapping
  execution_constraints:
  - execution_constraint_set.target_plus.marketplace_parser_constraints
  evidence_refs:
  - ev.target_plus.mapping.7_2_brand_level_sku_count
  confidence: high
  review_status: ready
```
```yaml
candidate_card:
  card_type: query_pattern
  card_id: query_pattern.target_plus.mapping.7_3_enrich_sales_with_mapping_data
  display_name: Target Plus query pattern — 7.3 Enrich Sales with Mapping Data
  intent: 7.3 Enrich Sales with Mapping Data
  natural_language_patterns:
  - 7.3 Enrich Sales with Mapping Data
  - Target Plus 7.3 Enrich Sales with Mapping Data
  source_tables:
  - table.zs_observe.target_sales
  - table.zs_observe.target_tcin_mapping
  required_filters:
  - rule.target_plus.active_filter
  - rule.target_plus.tcin_mapping_join
  sql_ref: sql.target_plus.mapping.7_3_enrich_sales_with_mapping_data
  primary_metric_id: null
  reconciliation_profile_ids:
  - reconciliation_profile.target_plus.tcin_mapping
  output_contract_id: output_contract.target_plus.reconciliation_status
  execution_constraints:
  - execution_constraint_set.target_plus.marketplace_parser_constraints
  evidence_refs:
  - ev.target_plus.mapping.7_3_enrich_sales_with_mapping_data
  confidence: high
  review_status: ready
```
```yaml
candidate_card:
  card_type: query_pattern
  card_id: query_pattern.target_plus.returns.7_1_return_volume_and_value_by_reason
  display_name: Target Plus query pattern — 7.1 Return Volume and Value by Reason
  intent: 7.1 Return Volume and Value by Reason
  natural_language_patterns:
  - 7.1 Return Volume and Value by Reason
  - Target Plus 7.1 Return Volume and Value by Reason
  source_tables:
  - table.zs_observe.target_returns
  required_filters:
  - rule.target_plus.active_filter
  sql_ref: sql.target_plus.returns.7_1_return_volume_and_value_by_reason
  primary_metric_id: metric.target_plus.return_reason_value
  reconciliation_profile_ids: []
  output_contract_id: output_contract.target_plus.metric_timeseries
  execution_constraints:
  - execution_constraint_set.target_plus.marketplace_parser_constraints
  evidence_refs:
  - ev.target_plus.returns.7_1_return_volume_and_value_by_reason
  confidence: high
  review_status: ready
```
```yaml
candidate_card:
  card_type: query_pattern
  card_id: query_pattern.target_plus.returns.7_2_return_rate_by_brand
  display_name: Target Plus query pattern — 7.2 Return Rate by Brand
  intent: 7.2 Return Rate by Brand
  natural_language_patterns:
  - 7.2 Return Rate by Brand
  - Target Plus 7.2 Return Rate by Brand
  source_tables:
  - table.zs_observe.target_returns
  required_filters:
  - rule.target_plus.active_filter
  sql_ref: sql.target_plus.returns.7_2_return_rate_by_brand
  primary_metric_id: metric.target_plus.brand_return_rate
  reconciliation_profile_ids: []
  output_contract_id: output_contract.target_plus.metric_timeseries
  execution_constraints:
  - execution_constraint_set.target_plus.marketplace_parser_constraints
  evidence_refs:
  - ev.target_plus.returns.7_2_return_rate_by_brand
  confidence: high
  review_status: ready
```
```yaml
candidate_card:
  card_type: query_pattern
  card_id: query_pattern.target_plus.returns.7_3_monthly_return_trend
  display_name: Target Plus query pattern — 7.3 Monthly Return Trend
  intent: 7.3 Monthly Return Trend
  natural_language_patterns:
  - 7.3 Monthly Return Trend
  - Target Plus 7.3 Monthly Return Trend
  source_tables:
  - table.zs_observe.target_returns
  required_filters:
  - rule.target_plus.active_filter
  sql_ref: sql.target_plus.returns.7_3_monthly_return_trend
  primary_metric_id: null
  reconciliation_profile_ids: []
  output_contract_id: output_contract.target_plus.metric_timeseries
  execution_constraints:
  - execution_constraint_set.target_plus.marketplace_parser_constraints
  evidence_refs:
  - ev.target_plus.returns.7_3_monthly_return_trend
  confidence: high
  review_status: ready
```
```yaml
candidate_card:
  card_type: query_pattern
  card_id: query_pattern.target_plus.returns.7_4_returns_sales_reconciliation
  display_name: Target Plus query pattern — 7.4 Returns ↔ Sales Reconciliation
  intent: 7.4 Returns ↔ Sales Reconciliation
  natural_language_patterns:
  - 7.4 Returns ↔ Sales Reconciliation
  - Target Plus 7.4 Returns ↔ Sales Reconciliation
  source_tables:
  - table.zs_observe.target_returns
  - table.zs_observe.target_sales
  required_filters:
  - rule.target_plus.active_filter
  - rule.target_plus.settlement_recency_gap
  sql_ref: sql.target_plus.returns.7_4_returns_sales_reconciliation
  primary_metric_id: null
  reconciliation_profile_ids:
  - reconciliation_profile.target_plus.sales_settlement
  output_contract_id: output_contract.target_plus.reconciliation_status
  execution_constraints:
  - execution_constraint_set.target_plus.marketplace_parser_constraints
  evidence_refs:
  - ev.target_plus.returns.7_4_returns_sales_reconciliation
  confidence: high
  review_status: ready
```
```yaml
candidate_card:
  card_type: query_pattern
  card_id: query_pattern.target_plus.returns.7_5_sku_level_return_rate
  display_name: Target Plus query pattern — 7.5 SKU-Level Return Rate
  intent: 7.5 SKU-Level Return Rate
  natural_language_patterns:
  - 7.5 SKU-Level Return Rate
  - Target Plus 7.5 SKU-Level Return Rate
  source_tables:
  - table.zs_observe.target_returns
  - table.zs_observe.target_sales
  - table.zs_observe.target_tcin_mapping
  required_filters:
  - rule.target_plus.active_filter
  sql_ref: sql.target_plus.returns.7_5_sku_level_return_rate
  primary_metric_id: null
  reconciliation_profile_ids: []
  output_contract_id: output_contract.target_plus.metric_timeseries
  execution_constraints:
  - execution_constraint_set.target_plus.marketplace_parser_constraints
  evidence_refs:
  - ev.target_plus.returns.7_5_sku_level_return_rate
  confidence: high
  review_status: ready
```
```yaml
candidate_card:
  card_type: query_pattern
  card_id: query_pattern.target_plus.sales.7_1_monthly_sales_gmv_by_brand
  display_name: Target Plus query pattern — 7.1 Monthly Sales GMV by Brand
  intent: 7.1 Monthly Sales GMV by Brand
  natural_language_patterns:
  - 7.1 Monthly Sales GMV by Brand
  - Target Plus 7.1 Monthly Sales GMV by Brand
  source_tables:
  - table.zs_observe.target_sales
  required_filters:
  - rule.target_plus.active_filter
  sql_ref: sql.target_plus.sales.7_1_monthly_sales_gmv_by_brand
  primary_metric_id: metric.target_plus.monthly_sales_gmv
  reconciliation_profile_ids: []
  output_contract_id: output_contract.target_plus.metric_timeseries
  execution_constraints:
  - execution_constraint_set.target_plus.marketplace_parser_constraints
  evidence_refs:
  - ev.target_plus.sales.7_1_monthly_sales_gmv_by_brand
  confidence: high
  review_status: ready
```
```yaml
candidate_card:
  card_type: query_pattern
  card_id: query_pattern.target_plus.sales.7_2_sku_level_sales_performance
  display_name: Target Plus query pattern — 7.2 SKU-Level Sales Performance
  intent: 7.2 SKU-Level Sales Performance
  natural_language_patterns:
  - 7.2 SKU-Level Sales Performance
  - Target Plus 7.2 SKU-Level Sales Performance
  source_tables:
  - table.zs_observe.target_sales
  - table.zs_observe.target_tcin_mapping
  required_filters:
  - rule.target_plus.active_filter
  sql_ref: sql.target_plus.sales.7_2_sku_level_sales_performance
  primary_metric_id: null
  reconciliation_profile_ids: []
  output_contract_id: output_contract.target_plus.metric_timeseries
  execution_constraints:
  - execution_constraint_set.target_plus.marketplace_parser_constraints
  evidence_refs:
  - ev.target_plus.sales.7_2_sku_level_sales_performance
  confidence: high
  review_status: ready
```
```yaml
candidate_card:
  card_type: query_pattern
  card_id: query_pattern.target_plus.sales.7_3_sales_settlement_join
  display_name: Target Plus query pattern — 7.3 Sales → Settlement Join
  intent: 7.3 Sales → Settlement Join
  natural_language_patterns:
  - 7.3 Sales → Settlement Join
  - Target Plus 7.3 Sales → Settlement Join
  source_tables:
  - table.zs_observe.target_sales
  - table.zs_observe.target_settlement
  required_filters:
  - rule.target_plus.active_filter
  - rule.target_plus.currency_label_usd_values
  - rule.target_plus.settlement_recency_gap
  sql_ref: sql.target_plus.sales.7_3_sales_settlement_join
  primary_metric_id: null
  reconciliation_profile_ids:
  - reconciliation_profile.target_plus.sales_settlement
  output_contract_id: output_contract.target_plus.reconciliation_status
  execution_constraints:
  - execution_constraint_set.target_plus.marketplace_parser_constraints
  evidence_refs:
  - ev.target_plus.sales.7_3_sales_settlement_join
  confidence: high
  review_status: ready
```
```yaml
candidate_card:
  card_type: query_pattern
  card_id: query_pattern.target_plus.sales.7_4_return_rate_by_brand
  display_name: Target Plus query pattern — 7.4 Return Rate by Brand
  intent: 7.4 Return Rate by Brand
  natural_language_patterns:
  - 7.4 Return Rate by Brand
  - Target Plus 7.4 Return Rate by Brand
  source_tables:
  - table.zs_observe.target_returns
  - table.zs_observe.target_sales
  required_filters:
  - rule.target_plus.active_filter
  sql_ref: sql.target_plus.sales.7_4_return_rate_by_brand
  primary_metric_id: null
  reconciliation_profile_ids: []
  output_contract_id: output_contract.target_plus.metric_timeseries
  execution_constraints:
  - execution_constraint_set.target_plus.marketplace_parser_constraints
  evidence_refs:
  - ev.target_plus.sales.7_4_return_rate_by_brand
  confidence: high
  review_status: ready
```
### 4.20 rule

```yaml
candidate_card:
  card_type: rule
  card_id: rule.target_plus.marketplace_boundary
  display_name: Target Plus marketplace-only boundary
  rule_type: scope_guardrail
  statement: Do not emit tenant, group, platform_account, logistics_account, bank_account, payment_gateway_account, ERP/accounting,
    or statutory_tax_filing cards from this markdown.
  condition: Always
  applies_to_cards:
  - platform.target_plus
  severity: critical
  evidence_refs:
  - ev.target_plus.marketplace.1_1_background
  confidence: high
  review_status: ready
```
```yaml
candidate_card:
  card_type: rule
  card_id: rule.target_plus.scope_group_123
  display_name: Target Plus group scope filter
  rule_type: query_filter
  statement: Apply group_level_id = 123 to all four Target Plus tables when group scope is required.
  condition: Target Plus table queries
  applies_to_cards:
  - table.zs_observe.target_sales
  - table.zs_observe.target_returns
  - table.zs_observe.target_settlement
  - table.zs_observe.target_tcin_mapping
  severity: high
  evidence_refs:
  - ev.target_plus.marketplace.8_mandatory_query_filters
  confidence: high
  review_status: ready
```
```yaml
candidate_card:
  card_type: rule
  card_id: rule.target_plus.active_filter
  display_name: Target Plus active row filter
  rule_type: query_filter
  statement: Apply is_active = true to all Target Plus source tables before analytics or reconciliation.
  condition: All Target tables
  applies_to_cards:
  - table.zs_observe.target_sales
  - table.zs_observe.target_returns
  - table.zs_observe.target_settlement
  - table.zs_observe.target_tcin_mapping
  severity: critical
  evidence_refs:
  - ev.target_plus.marketplace.8_mandatory_query_filters
  confidence: high
  review_status: ready
```
```yaml
candidate_card:
  card_type: rule
  card_id: rule.target_plus.sales_shipped_filter
  display_name: Target Plus shipped-sales filter
  rule_type: query_filter
  statement: Use order_status = 'SHIPPED' for shipped sales and GMV metrics from target_sales.
  condition: Sales metrics
  applies_to_cards:
  - table.zs_observe.target_sales
  - metric.target_plus.total_gmv
  severity: high
  evidence_refs:
  - ev.target_plus.marketplace.8_mandatory_query_filters
  - ev.target_plus.sales.order_status_distribution
  confidence: high
  review_status: ready
```
```yaml
candidate_card:
  card_type: rule
  card_id: rule.target_plus.settlement_forward_filter
  display_name: Target Plus forward settlement filter
  rule_type: query_filter
  statement: Use transaction_type = 'forward' for forward settlement/payout rate and commission metrics.
  condition: Forward settlement metrics
  applies_to_cards:
  - table.zs_observe.target_settlement
  - metric.target_plus.effective_payout_rate
  severity: high
  evidence_refs:
  - ev.target_plus.marketplace.8_mandatory_query_filters
  confidence: high
  review_status: ready
```
```yaml
candidate_card:
  card_type: rule
  card_id: rule.target_plus.returns_confirmed_filter
  display_name: Target Plus confirmed returns filter
  rule_type: query_filter
  statement: Use internal_txn_type = 'reverse' for confirmed physical return events in target_returns.
  condition: Return metrics
  applies_to_cards:
  - table.zs_observe.target_returns
  - metric.target_plus.return_reason_value
  severity: high
  evidence_refs:
  - ev.target_plus.marketplace.8_mandatory_query_filters
  confidence: high
  review_status: ready
```
```yaml
candidate_card:
  card_type: rule
  card_id: rule.target_plus.currency_label_usd_values
  display_name: Target Plus currency label caveat
  rule_type: semantic_rule
  statement: currency_type is labeled INR in tables, but financial values are USD-priced values; treat amounts as USD unless an external
    currency conversion layer says otherwise.
  condition: All financial analysis
  applies_to_cards:
  - table.zs_observe.target_sales
  - table.zs_observe.target_returns
  - table.zs_observe.target_settlement
  - table.zs_observe.target_tcin_mapping
  severity: high
  evidence_refs:
  - ev.target_plus.marketplace.7_data_quality_observations_and_known_issues
  - ev.target_plus.settlement.2_key_statistics_2
  confidence: high
  review_status: ready
```
```yaml
candidate_card:
  card_type: rule
  card_id: rule.target_plus.settlement_recency_gap
  display_name: Target Plus settlement recency gap rule
  rule_type: timing_rule
  statement: Settlement data runs Apr-Nov 2025 while sales run Apr-Dec 2025; date-align periods before classifying unmatched sales as
    issues.
  condition: Sales↔Settlement reconciliation
  applies_to_cards:
  - reconciliation_profile.target_plus.sales_settlement
  severity: high
  evidence_refs:
  - ev.target_plus.marketplace.3_2_primary_join_keys
  - ev.target_plus.marketplace.7_data_quality_observations_and_known_issues
  confidence: high
  review_status: ready
```
```yaml
candidate_card:
  card_type: rule
  card_id: rule.target_plus.charged_amount_excluding_tax
  display_name: Target Plus settlement revenue-base rule
  rule_type: semantic_rule
  statement: Use charged_amount_excluding_tax for settlement revenue base and charged_amount for per-unit price; they differ for multi-quantity
    orders.
  condition: Settlement revenue metrics
  applies_to_cards:
  - table.zs_observe.target_settlement
  - metric.target_plus.effective_payout_rate
  severity: high
  evidence_refs:
  - ev.target_plus.marketplace.7_data_quality_observations_and_known_issues
  - ev.target_plus.settlement.3_schema_details_37_columns_2
  confidence: high
  review_status: ready
```
```yaml
candidate_card:
  card_type: rule
  card_id: rule.target_plus.brand_case_normalization
  display_name: Target Plus brand case normalization rule
  rule_type: semantic_rule
  statement: Use LOWER(brand) or case-insensitive comparison between target_tcin_mapping and sales/returns/settlement brand values.
  condition: Brand joins and groupings
  applies_to_cards:
  - value_profile.target_plus.mapping.brand_case
  severity: medium
  evidence_refs:
  - ev.target_plus.mapping.brand_distribution
  - ev.target_plus.marketplace.7_data_quality_observations_and_known_issues
  confidence: high
  review_status: ready
```
```yaml
candidate_card:
  card_type: rule
  card_id: rule.target_plus.tcin_mapping_join
  display_name: Target Plus mapping join rule
  rule_type: join_rule
  statement: Use tcin for transaction-to-mapping enrichment; do not assume Shopify-format transaction sku_id equals clean seller SKU
    in mapping.
  condition: Product enrichment
  applies_to_cards:
  - relationship.target_plus.sales_mapping.tcin
  - relationship.target_plus.settlement_mapping.tcin
  - relationship.target_plus.returns_mapping.tcin
  severity: high
  evidence_refs:
  - ev.target_plus.marketplace.3_1_join_map
  - ev.target_plus.mapping.1_table_overview
  confidence: high
  review_status: ready
```
```yaml
candidate_card:
  card_type: rule
  card_id: rule.target_plus.reverse_charge_not_return
  display_name: Target Plus reverse charge classification rule
  rule_type: semantic_rule
  statement: transaction_type = 'reverse charge' is a marketplace-facilitator tax adjustment, not a customer return. Filter transaction_type
    = 'reverse' for return financial impact.
  condition: Settlement classification
  applies_to_cards:
  - table.zs_observe.target_settlement
  - business_process.target_plus.reverse_charge_flow
  severity: critical
  evidence_refs:
  - ev.target_plus.marketplace.2_3_reverse_charge_flow
  - ev.target_plus.marketplace.7_data_quality_observations_and_known_issues
  confidence: high
  review_status: ready
```
```yaml
candidate_card:
  card_type: rule
  card_id: rule.target_plus.total_tax_zero
  display_name: Target Plus total_tax zero rule
  rule_type: tax_rule
  statement: total_tax is 0 on settlement rows because Target collects/remits sales tax as marketplace facilitator; seller does not
    see gross tax amounts.
  condition: Settlement tax analysis
  applies_to_cards:
  - column.zs_observe.target_settlement.total_tax
  - value_profile.target_plus.settlement.total_tax_zero
  severity: high
  evidence_refs:
  - ev.target_plus.marketplace.4_3_us_sales_tax_marketplace_facilitator_model
  - ev.target_plus.settlement.total_tax_0_0_always_2
  confidence: high
  review_status: ready
```
```yaml
candidate_card:
  card_type: rule
  card_id: rule.target_plus.no_indian_tcs_tds
  display_name: Target Plus no Indian TCS/TDS rule
  rule_type: tax_rule
  statement: As a US marketplace, Target Plus has no Indian TCS/TDS obligations in these tables; no total_tcs_amount or tds_194o_rate
    fields are documented.
  condition: Tax semantics
  applies_to_cards:
  - domain.target_plus.tax
  - platform_context.target_plus.us
  severity: critical
  evidence_refs:
  - ev.target_plus.marketplace.4_3_us_sales_tax_marketplace_facilitator_model
  confidence: high
  review_status: ready
```
```yaml
candidate_card:
  card_type: rule
  card_id: rule.target_plus.barcode_formatting
  display_name: Target Plus barcode formatting caveat
  rule_type: data_quality_rule
  statement: Barcodes in target_tcin_mapping may be stored in scientific notation; cast or reformat before product matching.
  condition: Product matching
  applies_to_cards:
  - column.zs_observe.target_tcin_mapping.barcode
  - value_profile.target_plus.mapping.barcode_coverage
  severity: medium
  evidence_refs:
  - ev.target_plus.mapping.barcode_coverage
  confidence: high
  review_status: ready
```
```yaml
candidate_card:
  card_type: rule
  card_id: rule.target_plus.settlement_description_ignore
  display_name: Target Plus settlement description caveat
  rule_type: data_quality_rule
  statement: target_settlement.description is an integer and typically NULL; use transaction_type/internal_txn_type for classification.
  condition: Settlement classification
  applies_to_cards:
  - column.zs_observe.target_settlement.description
  - column.zs_observe.target_settlement.transaction_type
  severity: medium
  evidence_refs:
  - ev.target_plus.marketplace.7_data_quality_observations_and_known_issues
  - ev.target_plus.settlement.3_schema_details_37_columns_2
  confidence: high
  review_status: ready
```
```yaml
candidate_card:
  card_type: rule
  card_id: rule.target_plus.stripe_identifiers_columns_only
  display_name: Target Plus Stripe identifier scope rule
  rule_type: scope_guardrail
  statement: transfer_id, payout_id, and payment_id are Stripe identifiers in settlement; preserve as columns/value profiles, not payment
    gateway account cards.
  condition: Settlement payout analysis
  applies_to_cards:
  - value_profile.target_plus.settlement.stripe_id_formats
  - domain.target_plus.payment
  severity: high
  evidence_refs:
  - ev.target_plus.settlement.stripe_id_formats_2
  confidence: high
  review_status: ready
```
```yaml
candidate_card:
  card_type: rule
  card_id: rule.target_plus.external_logistics_boundary
  display_name: Target Plus external logistics boundary
  rule_type: scope_guardrail
  statement: UPS/USPS/FedEx/return logistics references are marketplace fulfillment caveats and columns only; do not emit logistics
    account or carrier-operation cards.
  condition: Fulfillment and returns
  applies_to_cards:
  - domain.target_plus.fulfillment
  - business_process.target_plus.return_flow
  severity: high
  evidence_refs:
  - ev.target_plus.marketplace.1_2_seller_eligibility
  - ev.target_plus.returns.other_id_carrier_tracking_numbers
  confidence: high
  review_status: ready
```
```yaml
candidate_card:
  card_type: rule
  card_id: rule.target_plus.one_row_per_event
  display_name: Target Plus one-row-per-event settlement rule
  rule_type: semantic_rule
  statement: Target settlement is one row per order line per event; settled_amount is already net payout after commission deduction.
  condition: Settlement grain
  applies_to_cards:
  - table.zs_observe.target_settlement
  severity: high
  evidence_refs:
  - ev.target_plus.settlement.1_table_overview_2
  confidence: high
  review_status: ready
```
### 4.21 validation_test

```yaml
candidate_card:
  card_type: validation_test
  card_id: validation_test.target_plus.active_filter
  display_name: Validate active filters
  test_type: sql_lint
  assertion: Generated SQL against Target Plus tables must include is_active = true unless explicitly querying inactive rows.
  expected_result: is_active filter present
  failure_meaning: Parser may count inactive/deleted rows.
  applies_to_cards:
  - table.zs_observe.target_sales
  - table.zs_observe.target_returns
  - table.zs_observe.target_settlement
  - table.zs_observe.target_tcin_mapping
  evidence_refs:
  - ev.target_plus.marketplace.8_mandatory_query_filters
  confidence: high
  review_status: ready
```
```yaml
candidate_card:
  card_type: validation_test
  card_id: validation_test.target_plus.scope_group_123
  display_name: Validate group_level_id scope
  test_type: sql_lint
  assertion: Generated SQL should include group_level_id = 123 when Target Plus source scope is required.
  expected_result: group_level_id = 123 present or runtime scope explicitly supplies it
  failure_meaning: Parser may mix source scopes.
  applies_to_cards:
  - table.zs_observe.target_sales
  - table.zs_observe.target_returns
  - table.zs_observe.target_settlement
  - table.zs_observe.target_tcin_mapping
  evidence_refs:
  - ev.target_plus.marketplace.8_mandatory_query_filters
  confidence: high
  review_status: ready
```
```yaml
candidate_card:
  card_type: validation_test
  card_id: validation_test.target_plus.no_forbidden_cards
  display_name: Validate marketplace-only card scope
  test_type: graph_lint
  assertion: No forbidden external-domain card types appear in candidate cards.
  expected_result: 0 forbidden-scope cards
  failure_meaning: Marketplace markdown leaked account/bank/tax/logistics entities.
  applies_to_cards:
  - platform.target_plus
  evidence_refs:
  - ev.target_plus.marketplace.1_1_background
  confidence: high
  review_status: ready
```
```yaml
candidate_card:
  card_type: validation_test
  card_id: validation_test.target_plus.no_reverse_charge_return_mix
  display_name: Validate reverse charge separation
  test_type: sql_lint
  assertion: Return-impact SQL must filter transaction_type = 'reverse' and must not include transaction_type = 'reverse charge' unless
    tax adjustment analysis is requested.
  expected_result: reverse charge excluded from customer-return metrics
  failure_meaning: Return financial impact overstated/misclassified.
  applies_to_cards:
  - table.zs_observe.target_settlement
  - rule.target_plus.reverse_charge_not_return
  evidence_refs:
  - ev.target_plus.marketplace.7_data_quality_observations_and_known_issues
  confidence: high
  review_status: ready
```
```yaml
candidate_card:
  card_type: validation_test
  card_id: validation_test.target_plus.currency_usd_label
  display_name: Validate USD interpretation caveat
  test_type: semantic_lint
  assertion: Financial output must label Target Plus amounts as USD-valued despite currency_type = INR label.
  expected_result: USD-valued caveat applied
  failure_meaning: Output may present amounts as Indian rupees incorrectly.
  applies_to_cards:
  - table.zs_observe.target_sales
  - table.zs_observe.target_returns
  - table.zs_observe.target_settlement
  - table.zs_observe.target_tcin_mapping
  evidence_refs:
  - ev.target_plus.marketplace.7_data_quality_observations_and_known_issues
  confidence: high
  review_status: ready
```
```yaml
candidate_card:
  card_type: validation_test
  card_id: validation_test.target_plus.mapping_join_tcin
  display_name: Validate TCIN mapping join
  test_type: sql_lint
  assertion: Product enrichment SQL should join transaction tables to target_tcin_mapping on tcin, not direct sku_id.
  expected_result: tcin join used
  failure_meaning: SKU-format mismatch may break enrichment.
  applies_to_cards:
  - relationship.target_plus.sales_mapping.tcin
  - rule.target_plus.tcin_mapping_join
  evidence_refs:
  - ev.target_plus.mapping.7_3_enrich_sales_with_mapping_data
  confidence: high
  review_status: ready
```
```yaml
candidate_card:
  card_type: validation_test
  card_id: validation_test.target_plus.date_aligned_recon
  display_name: Validate settlement date alignment
  test_type: semantic_lint
  assertion: Sales-settlement reconciliation over sales through Dec 2025 must identify Nov settlement cutoff timing gap.
  expected_result: timing gap surfaced as Not Yet Settled / date caveat
  failure_meaning: Dec sales may be falsely treated as missing settlement.
  applies_to_cards:
  - reconciliation_profile.target_plus.sales_settlement
  - rule.target_plus.settlement_recency_gap
  evidence_refs:
  - ev.target_plus.marketplace.3_2_primary_join_keys
  confidence: high
  review_status: ready
```
```yaml
candidate_card:
  card_type: validation_test
  card_id: validation_test.target_plus.commission_15pct
  display_name: Validate commission formula
  test_type: sql_lint
  assertion: Commission validation must compare gross_commission against charged_amount_excluding_tax * 0.15 for forward rows.
  expected_result: Formula and transaction_type filter present
  failure_meaning: Commission validation uses wrong base or includes reverse charge rows.
  applies_to_cards:
  - metric_impl.target_plus.commission_validation
  - matching_logic.target_plus.commission_15pct
  evidence_refs:
  - ev.target_plus.marketplace.6_3_commission_validation
  confidence: high
  review_status: ready
```
```yaml
candidate_card:
  card_type: validation_test
  card_id: validation_test.target_plus.no_indian_tax_impl
  display_name: Validate no Indian TCS/TDS implementation
  test_type: graph_lint
  assertion: Do not create TCS/TDS metric implementations for Target Plus because the source states no such fields exist.
  expected_result: No TCS/TDS metric_implementation cards
  failure_meaning: Unsupported Indian tax implementation created.
  applies_to_cards:
  - domain.target_plus.tax
  - rule.target_plus.no_indian_tcs_tds
  evidence_refs:
  - ev.target_plus.marketplace.4_3_us_sales_tax_marketplace_facilitator_model
  confidence: high
  review_status: ready
```
```yaml
candidate_card:
  card_type: validation_test
  card_id: validation_test.target_plus.barcode_cast
  display_name: Validate barcode formatting note
  test_type: semantic_lint
  assertion: Product matching that uses barcode must account for scientific notation formatting.
  expected_result: Formatting/cast caveat present
  failure_meaning: Barcode-based matching may use malformed UPC/EAN values.
  applies_to_cards:
  - column.zs_observe.target_tcin_mapping.barcode
  - rule.target_plus.barcode_formatting
  evidence_refs:
  - ev.target_plus.mapping.barcode_coverage
  confidence: high
  review_status: ready
```
### 4.22 output_contract

```yaml
candidate_card:
  card_type: output_contract
  card_id: output_contract.target_plus.metric_timeseries
  display_name: Target Plus metric time-series output
  contract_type: metric_output
  required_columns:
  - month
  - metric_value
  - brand_or_scope_optional
  - source_table
  - filters_applied
  optional_columns:
  - comparison_period
  - caveat
  grain: month or requested grain
  sort_order:
  - month ASC
  evidence_refs:
  - ev.target_plus.marketplace.5_key_business_metrics_with_sql
  confidence: high
  review_status: ready
```
```yaml
candidate_card:
  card_type: output_contract
  card_id: output_contract.target_plus.reconciliation_status
  display_name: Target Plus reconciliation status output
  contract_type: reconciliation_output
  required_columns:
  - grain_key
  - expected_amount
  - actual_amount
  - variance
  - recon_status
  - timing_caveat
  optional_columns:
  - brand
  - tcin
  - payout_id
  - transaction_type
  grain: item_id/order_id/payout_id depending on profile
  sort_order:
  - review_priority DESC
  - grain_key ASC
  evidence_refs:
  - ev.target_plus.marketplace.6_reconciliation_use_cases
  confidence: high
  review_status: ready
```
```yaml
candidate_card:
  card_type: output_contract
  card_id: output_contract.target_plus.product_mapping
  display_name: Target Plus product mapping output
  contract_type: enrichment_output
  required_columns:
  - tcin
  - sku_id
  - brand
  - asin
  - barcode
  - sales_count_or_revenue_optional
  optional_columns:
  - normalized_brand
  - barcode_cast_note
  grain: tcin product variant
  sort_order:
  - brand ASC
  - tcin ASC
  evidence_refs:
  - ev.target_plus.mapping.7_1_full_catalogue_with_sales_coverage
  confidence: high
  review_status: ready
```
### 4.23 execution_constraint_set

```yaml
candidate_card:
  card_type: execution_constraint_set
  card_id: execution_constraint_set.target_plus.marketplace_parser_constraints
  display_name: Target Plus marketplace parser constraints
  constraint_family: marketplace_query_generation
  required_filters:
  - is_active = true
  - group_level_id = 123 where Target Plus source scope is required
  - order_status = SHIPPED for shipped-sales metrics
  - transaction_type context for settlement metrics
  aggregation_constraints:
  - aggregate many-side settlement/return rows before order-level comparisons
  - use charged_amount_excluding_tax for settlement revenue base
  - use tcin for mapping enrichment
  join_constraints:
  - sales-settlement item_id
  - sales-returns order_id
  - returns-settlement item_id
  - mapping via tcin only
  sign_constraints:
  - separate forward, reverse, and reverse charge settlement rows
  - do not mix reverse charge with customer returns
  - treat Target currency labels as USD-valued amounts
  scope_boundaries:
  - no tenant/group/account/bank/logistics/payment-gateway/statutory-filing card creation
  evidence_refs:
  - ev.target_plus.marketplace.8_mandatory_query_filters
  - ev.target_plus.marketplace.7_data_quality_observations_and_known_issues
  confidence: high
  review_status: ready
```
## 5. Candidate Edges — Unified Taxonomy

```yaml
candidate_edge:
  edge_id: edge.target_plus.00001.has_platform_context
  canonical_edge_type: HAS_PLATFORM_CONTEXT
  source_card_id: platform.target_plus
  target_card_id: platform_context.target_plus.us
  source_type: platform
  target_type: platform_context
  inverse_edge_type: BELONGS_TO_PLATFORM
  materialize_inverse: true
  legacy_edge_aliases: []
  edge_class: canonical
  canonical_cognee_edge: true
```
```yaml
candidate_edge:
  edge_id: edge.target_plus.00002.belongs_to_platform
  canonical_edge_type: BELONGS_TO_PLATFORM
  source_card_id: platform_context.target_plus.us
  target_card_id: platform.target_plus
  source_type: platform_context
  target_type: platform
  inverse_edge_type: HAS_PLATFORM_CONTEXT
  materialize_inverse: false
  legacy_edge_aliases: []
  edge_class: canonical
  canonical_cognee_edge: true
```
```yaml
candidate_edge:
  edge_id: edge.target_plus.00003.applies_to_platform_context
  canonical_edge_type: APPLIES_TO_PLATFORM_CONTEXT
  source_card_id: domain.target_plus.orders
  target_card_id: platform_context.target_plus.us
  source_type: domain
  target_type: platform_context
  inverse_edge_type: null
  materialize_inverse: false
  legacy_edge_aliases: []
  edge_class: canonical
  canonical_cognee_edge: true
```
```yaml
candidate_edge:
  edge_id: edge.target_plus.00004.applies_to_platform_context
  canonical_edge_type: APPLIES_TO_PLATFORM_CONTEXT
  source_card_id: domain.target_plus.settlement
  target_card_id: platform_context.target_plus.us
  source_type: domain
  target_type: platform_context
  inverse_edge_type: null
  materialize_inverse: false
  legacy_edge_aliases: []
  edge_class: canonical
  canonical_cognee_edge: true
```
```yaml
candidate_edge:
  edge_id: edge.target_plus.00005.applies_to_platform_context
  canonical_edge_type: APPLIES_TO_PLATFORM_CONTEXT
  source_card_id: domain.target_plus.returns
  target_card_id: platform_context.target_plus.us
  source_type: domain
  target_type: platform_context
  inverse_edge_type: null
  materialize_inverse: false
  legacy_edge_aliases: []
  edge_class: canonical
  canonical_cognee_edge: true
```
```yaml
candidate_edge:
  edge_id: edge.target_plus.00006.applies_to_platform_context
  canonical_edge_type: APPLIES_TO_PLATFORM_CONTEXT
  source_card_id: domain.target_plus.mapping_enrichment
  target_card_id: platform_context.target_plus.us
  source_type: domain
  target_type: platform_context
  inverse_edge_type: null
  materialize_inverse: false
  legacy_edge_aliases: []
  edge_class: canonical
  canonical_cognee_edge: true
```
```yaml
candidate_edge:
  edge_id: edge.target_plus.00007.applies_to_platform_context
  canonical_edge_type: APPLIES_TO_PLATFORM_CONTEXT
  source_card_id: domain.target_plus.fees
  target_card_id: platform_context.target_plus.us
  source_type: domain
  target_type: platform_context
  inverse_edge_type: null
  materialize_inverse: false
  legacy_edge_aliases: []
  edge_class: canonical
  canonical_cognee_edge: true
```
```yaml
candidate_edge:
  edge_id: edge.target_plus.00008.applies_to_platform_context
  canonical_edge_type: APPLIES_TO_PLATFORM_CONTEXT
  source_card_id: domain.target_plus.tax
  target_card_id: platform_context.target_plus.us
  source_type: domain
  target_type: platform_context
  inverse_edge_type: null
  materialize_inverse: false
  legacy_edge_aliases: []
  edge_class: canonical
  canonical_cognee_edge: true
```
```yaml
candidate_edge:
  edge_id: edge.target_plus.00009.applies_to_platform_context
  canonical_edge_type: APPLIES_TO_PLATFORM_CONTEXT
  source_card_id: domain.target_plus.fulfillment
  target_card_id: platform_context.target_plus.us
  source_type: domain
  target_type: platform_context
  inverse_edge_type: null
  materialize_inverse: false
  legacy_edge_aliases: []
  edge_class: canonical
  canonical_cognee_edge: true
```
```yaml
candidate_edge:
  edge_id: edge.target_plus.00010.applies_to_platform_context
  canonical_edge_type: APPLIES_TO_PLATFORM_CONTEXT
  source_card_id: domain.target_plus.payment
  target_card_id: platform_context.target_plus.us
  source_type: domain
  target_type: platform_context
  inverse_edge_type: null
  materialize_inverse: false
  legacy_edge_aliases: []
  edge_class: canonical
  canonical_cognee_edge: true
```
```yaml
candidate_edge:
  edge_id: edge.target_plus.00011.applies_to_platform_context
  canonical_edge_type: APPLIES_TO_PLATFORM_CONTEXT
  source_card_id: domain.target_plus.reconciliation
  target_card_id: platform_context.target_plus.us
  source_type: domain
  target_type: platform_context
  inverse_edge_type: null
  materialize_inverse: false
  legacy_edge_aliases: []
  edge_class: canonical
  canonical_cognee_edge: true
```
```yaml
candidate_edge:
  edge_id: edge.target_plus.00012.applies_to_platform_context
  canonical_edge_type: APPLIES_TO_PLATFORM_CONTEXT
  source_card_id: domain.target_plus.query_guidance
  target_card_id: platform_context.target_plus.us
  source_type: domain
  target_type: platform_context
  inverse_edge_type: null
  materialize_inverse: false
  legacy_edge_aliases: []
  edge_class: canonical
  canonical_cognee_edge: true
```
```yaml
candidate_edge:
  edge_id: edge.target_plus.00013.sourced_from_platform_context
  canonical_edge_type: SOURCED_FROM_PLATFORM_CONTEXT
  source_card_id: table.zs_observe.target_sales
  target_card_id: platform_context.target_plus.us
  source_type: table
  target_type: platform_context
  inverse_edge_type: null
  materialize_inverse: false
  legacy_edge_aliases: []
  edge_class: canonical
  canonical_cognee_edge: true
```
```yaml
candidate_edge:
  edge_id: edge.target_plus.00014.belongs_to_domain
  canonical_edge_type: BELONGS_TO_DOMAIN
  source_card_id: table.zs_observe.target_sales
  target_card_id: domain.target_plus.orders
  source_type: table
  target_type: domain
  inverse_edge_type: null
  materialize_inverse: false
  legacy_edge_aliases: []
  edge_class: canonical
  canonical_cognee_edge: true
```
```yaml
candidate_edge:
  edge_id: edge.target_plus.00015.sourced_from_platform_context
  canonical_edge_type: SOURCED_FROM_PLATFORM_CONTEXT
  source_card_id: table.zs_observe.target_returns
  target_card_id: platform_context.target_plus.us
  source_type: table
  target_type: platform_context
  inverse_edge_type: null
  materialize_inverse: false
  legacy_edge_aliases: []
  edge_class: canonical
  canonical_cognee_edge: true
```
```yaml
candidate_edge:
  edge_id: edge.target_plus.00016.belongs_to_domain
  canonical_edge_type: BELONGS_TO_DOMAIN
  source_card_id: table.zs_observe.target_returns
  target_card_id: domain.target_plus.returns
  source_type: table
  target_type: domain
  inverse_edge_type: null
  materialize_inverse: false
  legacy_edge_aliases: []
  edge_class: canonical
  canonical_cognee_edge: true
```
```yaml
candidate_edge:
  edge_id: edge.target_plus.00017.sourced_from_platform_context
  canonical_edge_type: SOURCED_FROM_PLATFORM_CONTEXT
  source_card_id: table.zs_observe.target_settlement
  target_card_id: platform_context.target_plus.us
  source_type: table
  target_type: platform_context
  inverse_edge_type: null
  materialize_inverse: false
  legacy_edge_aliases: []
  edge_class: canonical
  canonical_cognee_edge: true
```
```yaml
candidate_edge:
  edge_id: edge.target_plus.00018.belongs_to_domain
  canonical_edge_type: BELONGS_TO_DOMAIN
  source_card_id: table.zs_observe.target_settlement
  target_card_id: domain.target_plus.settlement
  source_type: table
  target_type: domain
  inverse_edge_type: null
  materialize_inverse: false
  legacy_edge_aliases: []
  edge_class: canonical
  canonical_cognee_edge: true
```
```yaml
candidate_edge:
  edge_id: edge.target_plus.00019.sourced_from_platform_context
  canonical_edge_type: SOURCED_FROM_PLATFORM_CONTEXT
  source_card_id: table.zs_observe.target_tcin_mapping
  target_card_id: platform_context.target_plus.us
  source_type: table
  target_type: platform_context
  inverse_edge_type: null
  materialize_inverse: false
  legacy_edge_aliases: []
  edge_class: canonical
  canonical_cognee_edge: true
```
```yaml
candidate_edge:
  edge_id: edge.target_plus.00020.belongs_to_domain
  canonical_edge_type: BELONGS_TO_DOMAIN
  source_card_id: table.zs_observe.target_tcin_mapping
  target_card_id: domain.target_plus.mapping_enrichment
  source_type: table
  target_type: domain
  inverse_edge_type: null
  materialize_inverse: false
  legacy_edge_aliases: []
  edge_class: canonical
  canonical_cognee_edge: true
```
```yaml
candidate_edge:
  edge_id: edge.target_plus.00021.belongs_to_table
  canonical_edge_type: BELONGS_TO_TABLE
  source_card_id: column.zs_observe.target_settlement.unique_id
  target_card_id: table.zs_observe.target_settlement
  source_type: column
  target_type: table
  inverse_edge_type: HAS_COLUMN
  materialize_inverse: true
  legacy_edge_aliases:
  - column_belongs_to_table
  edge_class: canonical
  canonical_cognee_edge: true
```
```yaml
candidate_edge:
  edge_id: edge.target_plus.00022.has_column
  canonical_edge_type: HAS_COLUMN
  source_card_id: table.zs_observe.target_settlement
  target_card_id: column.zs_observe.target_settlement.unique_id
  source_type: table
  target_type: column
  inverse_edge_type: BELONGS_TO_TABLE
  materialize_inverse: true
  legacy_edge_aliases: []
  edge_class: canonical
  canonical_cognee_edge: true
```
```yaml
candidate_edge:
  edge_id: edge.target_plus.00023.belongs_to_table
  canonical_edge_type: BELONGS_TO_TABLE
  source_card_id: column.zs_observe.target_settlement.txn_uuid
  target_card_id: table.zs_observe.target_settlement
  source_type: column
  target_type: table
  inverse_edge_type: HAS_COLUMN
  materialize_inverse: true
  legacy_edge_aliases:
  - column_belongs_to_table
  edge_class: canonical
  canonical_cognee_edge: true
```
```yaml
candidate_edge:
  edge_id: edge.target_plus.00024.has_column
  canonical_edge_type: HAS_COLUMN
  source_card_id: table.zs_observe.target_settlement
  target_card_id: column.zs_observe.target_settlement.txn_uuid
  source_type: table
  target_type: column
  inverse_edge_type: BELONGS_TO_TABLE
  materialize_inverse: true
  legacy_edge_aliases: []
  edge_class: canonical
  canonical_cognee_edge: true
```
```yaml
candidate_edge:
  edge_id: edge.target_plus.00025.belongs_to_table
  canonical_edge_type: BELONGS_TO_TABLE
  source_card_id: column.zs_observe.target_settlement.unique_value
  target_card_id: table.zs_observe.target_settlement
  source_type: column
  target_type: table
  inverse_edge_type: HAS_COLUMN
  materialize_inverse: true
  legacy_edge_aliases:
  - column_belongs_to_table
  edge_class: canonical
  canonical_cognee_edge: true
```
```yaml
candidate_edge:
  edge_id: edge.target_plus.00026.has_column
  canonical_edge_type: HAS_COLUMN
  source_card_id: table.zs_observe.target_settlement
  target_card_id: column.zs_observe.target_settlement.unique_value
  source_type: table
  target_type: column
  inverse_edge_type: BELONGS_TO_TABLE
  materialize_inverse: true
  legacy_edge_aliases: []
  edge_class: canonical
  canonical_cognee_edge: true
```
```yaml
candidate_edge:
  edge_id: edge.target_plus.00027.belongs_to_table
  canonical_edge_type: BELONGS_TO_TABLE
  source_card_id: column.zs_observe.target_settlement.transfer_id
  target_card_id: table.zs_observe.target_settlement
  source_type: column
  target_type: table
  inverse_edge_type: HAS_COLUMN
  materialize_inverse: true
  legacy_edge_aliases:
  - column_belongs_to_table
  edge_class: canonical
  canonical_cognee_edge: true
```
```yaml
candidate_edge:
  edge_id: edge.target_plus.00028.has_column
  canonical_edge_type: HAS_COLUMN
  source_card_id: table.zs_observe.target_settlement
  target_card_id: column.zs_observe.target_settlement.transfer_id
  source_type: table
  target_type: column
  inverse_edge_type: BELONGS_TO_TABLE
  materialize_inverse: true
  legacy_edge_aliases: []
  edge_class: canonical
  canonical_cognee_edge: true
```
```yaml
candidate_edge:
  edge_id: edge.target_plus.00029.belongs_to_table
  canonical_edge_type: BELONGS_TO_TABLE
  source_card_id: column.zs_observe.target_settlement.payout_id
  target_card_id: table.zs_observe.target_settlement
  source_type: column
  target_type: table
  inverse_edge_type: HAS_COLUMN
  materialize_inverse: true
  legacy_edge_aliases:
  - column_belongs_to_table
  edge_class: canonical
  canonical_cognee_edge: true
```
```yaml
candidate_edge:
  edge_id: edge.target_plus.00030.has_column
  canonical_edge_type: HAS_COLUMN
  source_card_id: table.zs_observe.target_settlement
  target_card_id: column.zs_observe.target_settlement.payout_id
  source_type: table
  target_type: column
  inverse_edge_type: BELONGS_TO_TABLE
  materialize_inverse: true
  legacy_edge_aliases: []
  edge_class: canonical
  canonical_cognee_edge: true
```
```yaml
candidate_edge:
  edge_id: edge.target_plus.00031.belongs_to_table
  canonical_edge_type: BELONGS_TO_TABLE
  source_card_id: column.zs_observe.target_settlement.payment_id
  target_card_id: table.zs_observe.target_settlement
  source_type: column
  target_type: table
  inverse_edge_type: HAS_COLUMN
  materialize_inverse: true
  legacy_edge_aliases:
  - column_belongs_to_table
  edge_class: canonical
  canonical_cognee_edge: true
```
```yaml
candidate_edge:
  edge_id: edge.target_plus.00032.has_column
  canonical_edge_type: HAS_COLUMN
  source_card_id: table.zs_observe.target_settlement
  target_card_id: column.zs_observe.target_settlement.payment_id
  source_type: table
  target_type: column
  inverse_edge_type: BELONGS_TO_TABLE
  materialize_inverse: true
  legacy_edge_aliases: []
  edge_class: canonical
  canonical_cognee_edge: true
```
```yaml
candidate_edge:
  edge_id: edge.target_plus.00033.belongs_to_table
  canonical_edge_type: BELONGS_TO_TABLE
  source_card_id: column.zs_observe.target_settlement.order_id
  target_card_id: table.zs_observe.target_settlement
  source_type: column
  target_type: table
  inverse_edge_type: HAS_COLUMN
  materialize_inverse: true
  legacy_edge_aliases:
  - column_belongs_to_table
  edge_class: canonical
  canonical_cognee_edge: true
```
```yaml
candidate_edge:
  edge_id: edge.target_plus.00034.has_column
  canonical_edge_type: HAS_COLUMN
  source_card_id: table.zs_observe.target_settlement
  target_card_id: column.zs_observe.target_settlement.order_id
  source_type: table
  target_type: column
  inverse_edge_type: BELONGS_TO_TABLE
  materialize_inverse: true
  legacy_edge_aliases: []
  edge_class: canonical
  canonical_cognee_edge: true
```
```yaml
candidate_edge:
  edge_id: edge.target_plus.00035.belongs_to_table
  canonical_edge_type: BELONGS_TO_TABLE
  source_card_id: column.zs_observe.target_settlement.item_id
  target_card_id: table.zs_observe.target_settlement
  source_type: column
  target_type: table
  inverse_edge_type: HAS_COLUMN
  materialize_inverse: true
  legacy_edge_aliases:
  - column_belongs_to_table
  edge_class: canonical
  canonical_cognee_edge: true
```
```yaml
candidate_edge:
  edge_id: edge.target_plus.00036.has_column
  canonical_edge_type: HAS_COLUMN
  source_card_id: table.zs_observe.target_settlement
  target_card_id: column.zs_observe.target_settlement.item_id
  source_type: table
  target_type: column
  inverse_edge_type: BELONGS_TO_TABLE
  materialize_inverse: true
  legacy_edge_aliases: []
  edge_class: canonical
  canonical_cognee_edge: true
```
```yaml
candidate_edge:
  edge_id: edge.target_plus.00037.belongs_to_table
  canonical_edge_type: BELONGS_TO_TABLE
  source_card_id: column.zs_observe.target_settlement.sku_id
  target_card_id: table.zs_observe.target_settlement
  source_type: column
  target_type: table
  inverse_edge_type: HAS_COLUMN
  materialize_inverse: true
  legacy_edge_aliases:
  - column_belongs_to_table
  edge_class: canonical
  canonical_cognee_edge: true
```
```yaml
candidate_edge:
  edge_id: edge.target_plus.00038.has_column
  canonical_edge_type: HAS_COLUMN
  source_card_id: table.zs_observe.target_settlement
  target_card_id: column.zs_observe.target_settlement.sku_id
  source_type: table
  target_type: column
  inverse_edge_type: BELONGS_TO_TABLE
  materialize_inverse: true
  legacy_edge_aliases: []
  edge_class: canonical
  canonical_cognee_edge: true
```
```yaml
candidate_edge:
  edge_id: edge.target_plus.00039.belongs_to_table
  canonical_edge_type: BELONGS_TO_TABLE
  source_card_id: column.zs_observe.target_settlement.tcin
  target_card_id: table.zs_observe.target_settlement
  source_type: column
  target_type: table
  inverse_edge_type: HAS_COLUMN
  materialize_inverse: true
  legacy_edge_aliases:
  - column_belongs_to_table
  edge_class: canonical
  canonical_cognee_edge: true
```
```yaml
candidate_edge:
  edge_id: edge.target_plus.00040.has_column
  canonical_edge_type: HAS_COLUMN
  source_card_id: table.zs_observe.target_settlement
  target_card_id: column.zs_observe.target_settlement.tcin
  source_type: table
  target_type: column
  inverse_edge_type: BELONGS_TO_TABLE
  materialize_inverse: true
  legacy_edge_aliases: []
  edge_class: canonical
  canonical_cognee_edge: true
```
```yaml
candidate_edge:
  edge_id: edge.target_plus.00041.belongs_to_table
  canonical_edge_type: BELONGS_TO_TABLE
  source_card_id: column.zs_observe.target_settlement.created_date
  target_card_id: table.zs_observe.target_settlement
  source_type: column
  target_type: table
  inverse_edge_type: HAS_COLUMN
  materialize_inverse: true
  legacy_edge_aliases:
  - column_belongs_to_table
  edge_class: canonical
  canonical_cognee_edge: true
```
```yaml
candidate_edge:
  edge_id: edge.target_plus.00042.has_column
  canonical_edge_type: HAS_COLUMN
  source_card_id: table.zs_observe.target_settlement
  target_card_id: column.zs_observe.target_settlement.created_date
  source_type: table
  target_type: column
  inverse_edge_type: BELONGS_TO_TABLE
  materialize_inverse: true
  legacy_edge_aliases: []
  edge_class: canonical
  canonical_cognee_edge: true
```
```yaml
candidate_edge:
  edge_id: edge.target_plus.00043.belongs_to_table
  canonical_edge_type: BELONGS_TO_TABLE
  source_card_id: column.zs_observe.target_settlement.returned_date
  target_card_id: table.zs_observe.target_settlement
  source_type: column
  target_type: table
  inverse_edge_type: HAS_COLUMN
  materialize_inverse: true
  legacy_edge_aliases:
  - column_belongs_to_table
  edge_class: canonical
  canonical_cognee_edge: true
```
```yaml
candidate_edge:
  edge_id: edge.target_plus.00044.has_column
  canonical_edge_type: HAS_COLUMN
  source_card_id: table.zs_observe.target_settlement
  target_card_id: column.zs_observe.target_settlement.returned_date
  source_type: table
  target_type: column
  inverse_edge_type: BELONGS_TO_TABLE
  materialize_inverse: true
  legacy_edge_aliases: []
  edge_class: canonical
  canonical_cognee_edge: true
```
```yaml
candidate_edge:
  edge_id: edge.target_plus.00045.belongs_to_table
  canonical_edge_type: BELONGS_TO_TABLE
  source_card_id: column.zs_observe.target_settlement.charged_amount
  target_card_id: table.zs_observe.target_settlement
  source_type: column
  target_type: table
  inverse_edge_type: HAS_COLUMN
  materialize_inverse: true
  legacy_edge_aliases:
  - column_belongs_to_table
  edge_class: canonical
  canonical_cognee_edge: true
```
```yaml
candidate_edge:
  edge_id: edge.target_plus.00046.has_column
  canonical_edge_type: HAS_COLUMN
  source_card_id: table.zs_observe.target_settlement
  target_card_id: column.zs_observe.target_settlement.charged_amount
  source_type: table
  target_type: column
  inverse_edge_type: BELONGS_TO_TABLE
  materialize_inverse: true
  legacy_edge_aliases: []
  edge_class: canonical
  canonical_cognee_edge: true
```
```yaml
candidate_edge:
  edge_id: edge.target_plus.00047.belongs_to_table
  canonical_edge_type: BELONGS_TO_TABLE
  source_card_id: column.zs_observe.target_settlement.charged_amount_excluding_tax
  target_card_id: table.zs_observe.target_settlement
  source_type: column
  target_type: table
  inverse_edge_type: HAS_COLUMN
  materialize_inverse: true
  legacy_edge_aliases:
  - column_belongs_to_table
  edge_class: canonical
  canonical_cognee_edge: true
```
```yaml
candidate_edge:
  edge_id: edge.target_plus.00048.has_column
  canonical_edge_type: HAS_COLUMN
  source_card_id: table.zs_observe.target_settlement
  target_card_id: column.zs_observe.target_settlement.charged_amount_excluding_tax
  source_type: table
  target_type: column
  inverse_edge_type: BELONGS_TO_TABLE
  materialize_inverse: true
  legacy_edge_aliases: []
  edge_class: canonical
  canonical_cognee_edge: true
```
```yaml
candidate_edge:
  edge_id: edge.target_plus.00049.belongs_to_table
  canonical_edge_type: BELONGS_TO_TABLE
  source_card_id: column.zs_observe.target_settlement.total_tax
  target_card_id: table.zs_observe.target_settlement
  source_type: column
  target_type: table
  inverse_edge_type: HAS_COLUMN
  materialize_inverse: true
  legacy_edge_aliases:
  - column_belongs_to_table
  edge_class: canonical
  canonical_cognee_edge: true
```
```yaml
candidate_edge:
  edge_id: edge.target_plus.00050.has_column
  canonical_edge_type: HAS_COLUMN
  source_card_id: table.zs_observe.target_settlement
  target_card_id: column.zs_observe.target_settlement.total_tax
  source_type: table
  target_type: column
  inverse_edge_type: BELONGS_TO_TABLE
  materialize_inverse: true
  legacy_edge_aliases: []
  edge_class: canonical
  canonical_cognee_edge: true
```
```yaml
candidate_edge:
  edge_id: edge.target_plus.00051.belongs_to_table
  canonical_edge_type: BELONGS_TO_TABLE
  source_card_id: column.zs_observe.target_settlement.shipping_amount
  target_card_id: table.zs_observe.target_settlement
  source_type: column
  target_type: table
  inverse_edge_type: HAS_COLUMN
  materialize_inverse: true
  legacy_edge_aliases:
  - column_belongs_to_table
  edge_class: canonical
  canonical_cognee_edge: true
```
```yaml
candidate_edge:
  edge_id: edge.target_plus.00052.has_column
  canonical_edge_type: HAS_COLUMN
  source_card_id: table.zs_observe.target_settlement
  target_card_id: column.zs_observe.target_settlement.shipping_amount
  source_type: table
  target_type: column
  inverse_edge_type: BELONGS_TO_TABLE
  materialize_inverse: true
  legacy_edge_aliases: []
  edge_class: canonical
  canonical_cognee_edge: true
```
```yaml
candidate_edge:
  edge_id: edge.target_plus.00053.belongs_to_table
  canonical_edge_type: BELONGS_TO_TABLE
  source_card_id: column.zs_observe.target_settlement.gross_commission
  target_card_id: table.zs_observe.target_settlement
  source_type: column
  target_type: table
  inverse_edge_type: HAS_COLUMN
  materialize_inverse: true
  legacy_edge_aliases:
  - column_belongs_to_table
  edge_class: canonical
  canonical_cognee_edge: true
```
```yaml
candidate_edge:
  edge_id: edge.target_plus.00054.has_column
  canonical_edge_type: HAS_COLUMN
  source_card_id: table.zs_observe.target_settlement
  target_card_id: column.zs_observe.target_settlement.gross_commission
  source_type: table
  target_type: column
  inverse_edge_type: BELONGS_TO_TABLE
  materialize_inverse: true
  legacy_edge_aliases: []
  edge_class: canonical
  canonical_cognee_edge: true
```
```yaml
candidate_edge:
  edge_id: edge.target_plus.00055.belongs_to_table
  canonical_edge_type: BELONGS_TO_TABLE
  source_card_id: column.zs_observe.target_settlement.settled_amount
  target_card_id: table.zs_observe.target_settlement
  source_type: column
  target_type: table
  inverse_edge_type: HAS_COLUMN
  materialize_inverse: true
  legacy_edge_aliases:
  - column_belongs_to_table
  edge_class: canonical
  canonical_cognee_edge: true
```
```yaml
candidate_edge:
  edge_id: edge.target_plus.00056.has_column
  canonical_edge_type: HAS_COLUMN
  source_card_id: table.zs_observe.target_settlement
  target_card_id: column.zs_observe.target_settlement.settled_amount
  source_type: table
  target_type: column
  inverse_edge_type: BELONGS_TO_TABLE
  materialize_inverse: true
  legacy_edge_aliases: []
  edge_class: canonical
  canonical_cognee_edge: true
```
```yaml
candidate_edge:
  edge_id: edge.target_plus.00057.belongs_to_table
  canonical_edge_type: BELONGS_TO_TABLE
  source_card_id: column.zs_observe.target_settlement.gross_commission_percentage
  target_card_id: table.zs_observe.target_settlement
  source_type: column
  target_type: table
  inverse_edge_type: HAS_COLUMN
  materialize_inverse: true
  legacy_edge_aliases:
  - column_belongs_to_table
  edge_class: canonical
  canonical_cognee_edge: true
```
```yaml
candidate_edge:
  edge_id: edge.target_plus.00058.has_column
  canonical_edge_type: HAS_COLUMN
  source_card_id: table.zs_observe.target_settlement
  target_card_id: column.zs_observe.target_settlement.gross_commission_percentage
  source_type: table
  target_type: column
  inverse_edge_type: BELONGS_TO_TABLE
  materialize_inverse: true
  legacy_edge_aliases: []
  edge_class: canonical
  canonical_cognee_edge: true
```
```yaml
candidate_edge:
  edge_id: edge.target_plus.00059.belongs_to_table
  canonical_edge_type: BELONGS_TO_TABLE
  source_card_id: column.zs_observe.target_settlement.transaction_type
  target_card_id: table.zs_observe.target_settlement
  source_type: column
  target_type: table
  inverse_edge_type: HAS_COLUMN
  materialize_inverse: true
  legacy_edge_aliases:
  - column_belongs_to_table
  edge_class: canonical
  canonical_cognee_edge: true
```
```yaml
candidate_edge:
  edge_id: edge.target_plus.00060.has_column
  canonical_edge_type: HAS_COLUMN
  source_card_id: table.zs_observe.target_settlement
  target_card_id: column.zs_observe.target_settlement.transaction_type
  source_type: table
  target_type: column
  inverse_edge_type: BELONGS_TO_TABLE
  materialize_inverse: true
  legacy_edge_aliases: []
  edge_class: canonical
  canonical_cognee_edge: true
```
```yaml
candidate_edge:
  edge_id: edge.target_plus.00061.belongs_to_table
  canonical_edge_type: BELONGS_TO_TABLE
  source_card_id: column.zs_observe.target_settlement.internal_txn_type
  target_card_id: table.zs_observe.target_settlement
  source_type: column
  target_type: table
  inverse_edge_type: HAS_COLUMN
  materialize_inverse: true
  legacy_edge_aliases:
  - column_belongs_to_table
  edge_class: canonical
  canonical_cognee_edge: true
```
```yaml
candidate_edge:
  edge_id: edge.target_plus.00062.has_column
  canonical_edge_type: HAS_COLUMN
  source_card_id: table.zs_observe.target_settlement
  target_card_id: column.zs_observe.target_settlement.internal_txn_type
  source_type: table
  target_type: column
  inverse_edge_type: BELONGS_TO_TABLE
  materialize_inverse: true
  legacy_edge_aliases: []
  edge_class: canonical
  canonical_cognee_edge: true
```
```yaml
candidate_edge:
  edge_id: edge.target_plus.00063.belongs_to_table
  canonical_edge_type: BELONGS_TO_TABLE
  source_card_id: column.zs_observe.target_settlement.description
  target_card_id: table.zs_observe.target_settlement
  source_type: column
  target_type: table
  inverse_edge_type: HAS_COLUMN
  materialize_inverse: true
  legacy_edge_aliases:
  - column_belongs_to_table
  edge_class: canonical
  canonical_cognee_edge: true
```
```yaml
candidate_edge:
  edge_id: edge.target_plus.00064.has_column
  canonical_edge_type: HAS_COLUMN
  source_card_id: table.zs_observe.target_settlement
  target_card_id: column.zs_observe.target_settlement.description
  source_type: table
  target_type: column
  inverse_edge_type: BELONGS_TO_TABLE
  materialize_inverse: true
  legacy_edge_aliases: []
  edge_class: canonical
  canonical_cognee_edge: true
```
```yaml
candidate_edge:
  edge_id: edge.target_plus.00065.belongs_to_table
  canonical_edge_type: BELONGS_TO_TABLE
  source_card_id: column.zs_observe.target_settlement.brand
  target_card_id: table.zs_observe.target_settlement
  source_type: column
  target_type: table
  inverse_edge_type: HAS_COLUMN
  materialize_inverse: true
  legacy_edge_aliases:
  - column_belongs_to_table
  edge_class: canonical
  canonical_cognee_edge: true
```
```yaml
candidate_edge:
  edge_id: edge.target_plus.00066.has_column
  canonical_edge_type: HAS_COLUMN
  source_card_id: table.zs_observe.target_settlement
  target_card_id: column.zs_observe.target_settlement.brand
  source_type: table
  target_type: column
  inverse_edge_type: BELONGS_TO_TABLE
  materialize_inverse: true
  legacy_edge_aliases: []
  edge_class: canonical
  canonical_cognee_edge: true
```
```yaml
candidate_edge:
  edge_id: edge.target_plus.00067.belongs_to_table
  canonical_edge_type: BELONGS_TO_TABLE
  source_card_id: column.zs_observe.target_settlement.quantity
  target_card_id: table.zs_observe.target_settlement
  source_type: column
  target_type: table
  inverse_edge_type: HAS_COLUMN
  materialize_inverse: true
  legacy_edge_aliases:
  - column_belongs_to_table
  edge_class: canonical
  canonical_cognee_edge: true
```
```yaml
candidate_edge:
  edge_id: edge.target_plus.00068.has_column
  canonical_edge_type: HAS_COLUMN
  source_card_id: table.zs_observe.target_settlement
  target_card_id: column.zs_observe.target_settlement.quantity
  source_type: table
  target_type: column
  inverse_edge_type: BELONGS_TO_TABLE
  materialize_inverse: true
  legacy_edge_aliases: []
  edge_class: canonical
  canonical_cognee_edge: true
```
```yaml
candidate_edge:
  edge_id: edge.target_plus.00069.belongs_to_table
  canonical_edge_type: BELONGS_TO_TABLE
  source_card_id: column.zs_observe.target_settlement.group_level_id
  target_card_id: table.zs_observe.target_settlement
  source_type: column
  target_type: table
  inverse_edge_type: HAS_COLUMN
  materialize_inverse: true
  legacy_edge_aliases:
  - column_belongs_to_table
  edge_class: canonical
  canonical_cognee_edge: true
```
```yaml
candidate_edge:
  edge_id: edge.target_plus.00070.has_column
  canonical_edge_type: HAS_COLUMN
  source_card_id: table.zs_observe.target_settlement
  target_card_id: column.zs_observe.target_settlement.group_level_id
  source_type: table
  target_type: column
  inverse_edge_type: BELONGS_TO_TABLE
  materialize_inverse: true
  legacy_edge_aliases: []
  edge_class: canonical
  canonical_cognee_edge: true
```
```yaml
candidate_edge:
  edge_id: edge.target_plus.00071.belongs_to_table
  canonical_edge_type: BELONGS_TO_TABLE
  source_card_id: column.zs_observe.target_settlement.currency_type
  target_card_id: table.zs_observe.target_settlement
  source_type: column
  target_type: table
  inverse_edge_type: HAS_COLUMN
  materialize_inverse: true
  legacy_edge_aliases:
  - column_belongs_to_table
  edge_class: canonical
  canonical_cognee_edge: true
```
```yaml
candidate_edge:
  edge_id: edge.target_plus.00072.has_column
  canonical_edge_type: HAS_COLUMN
  source_card_id: table.zs_observe.target_settlement
  target_card_id: column.zs_observe.target_settlement.currency_type
  source_type: table
  target_type: column
  inverse_edge_type: BELONGS_TO_TABLE
  materialize_inverse: true
  legacy_edge_aliases: []
  edge_class: canonical
  canonical_cognee_edge: true
```
```yaml
candidate_edge:
  edge_id: edge.target_plus.00073.belongs_to_table
  canonical_edge_type: BELONGS_TO_TABLE
  source_card_id: column.zs_observe.target_settlement.is_active
  target_card_id: table.zs_observe.target_settlement
  source_type: column
  target_type: table
  inverse_edge_type: HAS_COLUMN
  materialize_inverse: true
  legacy_edge_aliases:
  - column_belongs_to_table
  edge_class: canonical
  canonical_cognee_edge: true
```
```yaml
candidate_edge:
  edge_id: edge.target_plus.00074.has_column
  canonical_edge_type: HAS_COLUMN
  source_card_id: table.zs_observe.target_settlement
  target_card_id: column.zs_observe.target_settlement.is_active
  source_type: table
  target_type: column
  inverse_edge_type: BELONGS_TO_TABLE
  materialize_inverse: true
  legacy_edge_aliases: []
  edge_class: canonical
  canonical_cognee_edge: true
```
```yaml
candidate_edge:
  edge_id: edge.target_plus.00075.belongs_to_table
  canonical_edge_type: BELONGS_TO_TABLE
  source_card_id: column.zs_observe.target_settlement.zen_sheet_name
  target_card_id: table.zs_observe.target_settlement
  source_type: column
  target_type: table
  inverse_edge_type: HAS_COLUMN
  materialize_inverse: true
  legacy_edge_aliases:
  - column_belongs_to_table
  edge_class: canonical
  canonical_cognee_edge: true
```
```yaml
candidate_edge:
  edge_id: edge.target_plus.00076.has_column
  canonical_edge_type: HAS_COLUMN
  source_card_id: table.zs_observe.target_settlement
  target_card_id: column.zs_observe.target_settlement.zen_sheet_name
  source_type: table
  target_type: column
  inverse_edge_type: BELONGS_TO_TABLE
  materialize_inverse: true
  legacy_edge_aliases: []
  edge_class: canonical
  canonical_cognee_edge: true
```
```yaml
candidate_edge:
  edge_id: edge.target_plus.00077.belongs_to_table
  canonical_edge_type: BELONGS_TO_TABLE
  source_card_id: column.zs_observe.target_settlement.created_at
  target_card_id: table.zs_observe.target_settlement
  source_type: column
  target_type: table
  inverse_edge_type: HAS_COLUMN
  materialize_inverse: true
  legacy_edge_aliases:
  - column_belongs_to_table
  edge_class: canonical
  canonical_cognee_edge: true
```
```yaml
candidate_edge:
  edge_id: edge.target_plus.00078.has_column
  canonical_edge_type: HAS_COLUMN
  source_card_id: table.zs_observe.target_settlement
  target_card_id: column.zs_observe.target_settlement.created_at
  source_type: table
  target_type: column
  inverse_edge_type: BELONGS_TO_TABLE
  materialize_inverse: true
  legacy_edge_aliases: []
  edge_class: canonical
  canonical_cognee_edge: true
```
```yaml
candidate_edge:
  edge_id: edge.target_plus.00079.belongs_to_table
  canonical_edge_type: BELONGS_TO_TABLE
  source_card_id: column.zs_observe.target_settlement.updated_at
  target_card_id: table.zs_observe.target_settlement
  source_type: column
  target_type: table
  inverse_edge_type: HAS_COLUMN
  materialize_inverse: true
  legacy_edge_aliases:
  - column_belongs_to_table
  edge_class: canonical
  canonical_cognee_edge: true
```
```yaml
candidate_edge:
  edge_id: edge.target_plus.00080.has_column
  canonical_edge_type: HAS_COLUMN
  source_card_id: table.zs_observe.target_settlement
  target_card_id: column.zs_observe.target_settlement.updated_at
  source_type: table
  target_type: column
  inverse_edge_type: BELONGS_TO_TABLE
  materialize_inverse: true
  legacy_edge_aliases: []
  edge_class: canonical
  canonical_cognee_edge: true
```
```yaml
candidate_edge:
  edge_id: edge.target_plus.00081.belongs_to_table
  canonical_edge_type: BELONGS_TO_TABLE
  source_card_id: column.zs_observe.target_settlement.deleted_at
  target_card_id: table.zs_observe.target_settlement
  source_type: column
  target_type: table
  inverse_edge_type: HAS_COLUMN
  materialize_inverse: true
  legacy_edge_aliases:
  - column_belongs_to_table
  edge_class: canonical
  canonical_cognee_edge: true
```
```yaml
candidate_edge:
  edge_id: edge.target_plus.00082.has_column
  canonical_edge_type: HAS_COLUMN
  source_card_id: table.zs_observe.target_settlement
  target_card_id: column.zs_observe.target_settlement.deleted_at
  source_type: table
  target_type: column
  inverse_edge_type: BELONGS_TO_TABLE
  materialize_inverse: true
  legacy_edge_aliases: []
  edge_class: canonical
  canonical_cognee_edge: true
```
```yaml
candidate_edge:
  edge_id: edge.target_plus.00083.belongs_to_table
  canonical_edge_type: BELONGS_TO_TABLE
  source_card_id: column.zs_observe.target_tcin_mapping.unique_id
  target_card_id: table.zs_observe.target_tcin_mapping
  source_type: column
  target_type: table
  inverse_edge_type: HAS_COLUMN
  materialize_inverse: true
  legacy_edge_aliases:
  - column_belongs_to_table
  edge_class: canonical
  canonical_cognee_edge: true
```
```yaml
candidate_edge:
  edge_id: edge.target_plus.00084.has_column
  canonical_edge_type: HAS_COLUMN
  source_card_id: table.zs_observe.target_tcin_mapping
  target_card_id: column.zs_observe.target_tcin_mapping.unique_id
  source_type: table
  target_type: column
  inverse_edge_type: BELONGS_TO_TABLE
  materialize_inverse: true
  legacy_edge_aliases: []
  edge_class: canonical
  canonical_cognee_edge: true
```
```yaml
candidate_edge:
  edge_id: edge.target_plus.00085.belongs_to_table
  canonical_edge_type: BELONGS_TO_TABLE
  source_card_id: column.zs_observe.target_tcin_mapping.txn_uuid
  target_card_id: table.zs_observe.target_tcin_mapping
  source_type: column
  target_type: table
  inverse_edge_type: HAS_COLUMN
  materialize_inverse: true
  legacy_edge_aliases:
  - column_belongs_to_table
  edge_class: canonical
  canonical_cognee_edge: true
```
```yaml
candidate_edge:
  edge_id: edge.target_plus.00086.has_column
  canonical_edge_type: HAS_COLUMN
  source_card_id: table.zs_observe.target_tcin_mapping
  target_card_id: column.zs_observe.target_tcin_mapping.txn_uuid
  source_type: table
  target_type: column
  inverse_edge_type: BELONGS_TO_TABLE
  materialize_inverse: true
  legacy_edge_aliases: []
  edge_class: canonical
  canonical_cognee_edge: true
```
```yaml
candidate_edge:
  edge_id: edge.target_plus.00087.belongs_to_table
  canonical_edge_type: BELONGS_TO_TABLE
  source_card_id: column.zs_observe.target_tcin_mapping.unique_value
  target_card_id: table.zs_observe.target_tcin_mapping
  source_type: column
  target_type: table
  inverse_edge_type: HAS_COLUMN
  materialize_inverse: true
  legacy_edge_aliases:
  - column_belongs_to_table
  edge_class: canonical
  canonical_cognee_edge: true
```
```yaml
candidate_edge:
  edge_id: edge.target_plus.00088.has_column
  canonical_edge_type: HAS_COLUMN
  source_card_id: table.zs_observe.target_tcin_mapping
  target_card_id: column.zs_observe.target_tcin_mapping.unique_value
  source_type: table
  target_type: column
  inverse_edge_type: BELONGS_TO_TABLE
  materialize_inverse: true
  legacy_edge_aliases: []
  edge_class: canonical
  canonical_cognee_edge: true
```
```yaml
candidate_edge:
  edge_id: edge.target_plus.00089.belongs_to_table
  canonical_edge_type: BELONGS_TO_TABLE
  source_card_id: column.zs_observe.target_tcin_mapping.sku_id
  target_card_id: table.zs_observe.target_tcin_mapping
  source_type: column
  target_type: table
  inverse_edge_type: HAS_COLUMN
  materialize_inverse: true
  legacy_edge_aliases:
  - column_belongs_to_table
  edge_class: canonical
  canonical_cognee_edge: true
```
```yaml
candidate_edge:
  edge_id: edge.target_plus.00090.has_column
  canonical_edge_type: HAS_COLUMN
  source_card_id: table.zs_observe.target_tcin_mapping
  target_card_id: column.zs_observe.target_tcin_mapping.sku_id
  source_type: table
  target_type: column
  inverse_edge_type: BELONGS_TO_TABLE
  materialize_inverse: true
  legacy_edge_aliases: []
  edge_class: canonical
  canonical_cognee_edge: true
```
```yaml
candidate_edge:
  edge_id: edge.target_plus.00091.belongs_to_table
  canonical_edge_type: BELONGS_TO_TABLE
  source_card_id: column.zs_observe.target_tcin_mapping.tcin
  target_card_id: table.zs_observe.target_tcin_mapping
  source_type: column
  target_type: table
  inverse_edge_type: HAS_COLUMN
  materialize_inverse: true
  legacy_edge_aliases:
  - column_belongs_to_table
  edge_class: canonical
  canonical_cognee_edge: true
```
```yaml
candidate_edge:
  edge_id: edge.target_plus.00092.has_column
  canonical_edge_type: HAS_COLUMN
  source_card_id: table.zs_observe.target_tcin_mapping
  target_card_id: column.zs_observe.target_tcin_mapping.tcin
  source_type: table
  target_type: column
  inverse_edge_type: BELONGS_TO_TABLE
  materialize_inverse: true
  legacy_edge_aliases: []
  edge_class: canonical
  canonical_cognee_edge: true
```
```yaml
candidate_edge:
  edge_id: edge.target_plus.00093.belongs_to_table
  canonical_edge_type: BELONGS_TO_TABLE
  source_card_id: column.zs_observe.target_tcin_mapping.barcode
  target_card_id: table.zs_observe.target_tcin_mapping
  source_type: column
  target_type: table
  inverse_edge_type: HAS_COLUMN
  materialize_inverse: true
  legacy_edge_aliases:
  - column_belongs_to_table
  edge_class: canonical
  canonical_cognee_edge: true
```
```yaml
candidate_edge:
  edge_id: edge.target_plus.00094.has_column
  canonical_edge_type: HAS_COLUMN
  source_card_id: table.zs_observe.target_tcin_mapping
  target_card_id: column.zs_observe.target_tcin_mapping.barcode
  source_type: table
  target_type: column
  inverse_edge_type: BELONGS_TO_TABLE
  materialize_inverse: true
  legacy_edge_aliases: []
  edge_class: canonical
  canonical_cognee_edge: true
```
```yaml
candidate_edge:
  edge_id: edge.target_plus.00095.belongs_to_table
  canonical_edge_type: BELONGS_TO_TABLE
  source_card_id: column.zs_observe.target_tcin_mapping.brand
  target_card_id: table.zs_observe.target_tcin_mapping
  source_type: column
  target_type: table
  inverse_edge_type: HAS_COLUMN
  materialize_inverse: true
  legacy_edge_aliases:
  - column_belongs_to_table
  edge_class: canonical
  canonical_cognee_edge: true
```
```yaml
candidate_edge:
  edge_id: edge.target_plus.00096.has_column
  canonical_edge_type: HAS_COLUMN
  source_card_id: table.zs_observe.target_tcin_mapping
  target_card_id: column.zs_observe.target_tcin_mapping.brand
  source_type: table
  target_type: column
  inverse_edge_type: BELONGS_TO_TABLE
  materialize_inverse: true
  legacy_edge_aliases: []
  edge_class: canonical
  canonical_cognee_edge: true
```
```yaml
candidate_edge:
  edge_id: edge.target_plus.00097.belongs_to_table
  canonical_edge_type: BELONGS_TO_TABLE
  source_card_id: column.zs_observe.target_tcin_mapping.asin
  target_card_id: table.zs_observe.target_tcin_mapping
  source_type: column
  target_type: table
  inverse_edge_type: HAS_COLUMN
  materialize_inverse: true
  legacy_edge_aliases:
  - column_belongs_to_table
  edge_class: canonical
  canonical_cognee_edge: true
```
```yaml
candidate_edge:
  edge_id: edge.target_plus.00098.has_column
  canonical_edge_type: HAS_COLUMN
  source_card_id: table.zs_observe.target_tcin_mapping
  target_card_id: column.zs_observe.target_tcin_mapping.asin
  source_type: table
  target_type: column
  inverse_edge_type: BELONGS_TO_TABLE
  materialize_inverse: true
  legacy_edge_aliases: []
  edge_class: canonical
  canonical_cognee_edge: true
```
```yaml
candidate_edge:
  edge_id: edge.target_plus.00099.belongs_to_table
  canonical_edge_type: BELONGS_TO_TABLE
  source_card_id: column.zs_observe.target_tcin_mapping.currency_type
  target_card_id: table.zs_observe.target_tcin_mapping
  source_type: column
  target_type: table
  inverse_edge_type: HAS_COLUMN
  materialize_inverse: true
  legacy_edge_aliases:
  - column_belongs_to_table
  edge_class: canonical
  canonical_cognee_edge: true
```
```yaml
candidate_edge:
  edge_id: edge.target_plus.00100.has_column
  canonical_edge_type: HAS_COLUMN
  source_card_id: table.zs_observe.target_tcin_mapping
  target_card_id: column.zs_observe.target_tcin_mapping.currency_type
  source_type: table
  target_type: column
  inverse_edge_type: BELONGS_TO_TABLE
  materialize_inverse: true
  legacy_edge_aliases: []
  edge_class: canonical
  canonical_cognee_edge: true
```
```yaml
candidate_edge:
  edge_id: edge.target_plus.00101.belongs_to_table
  canonical_edge_type: BELONGS_TO_TABLE
  source_card_id: column.zs_observe.target_tcin_mapping.group_level_id
  target_card_id: table.zs_observe.target_tcin_mapping
  source_type: column
  target_type: table
  inverse_edge_type: HAS_COLUMN
  materialize_inverse: true
  legacy_edge_aliases:
  - column_belongs_to_table
  edge_class: canonical
  canonical_cognee_edge: true
```
```yaml
candidate_edge:
  edge_id: edge.target_plus.00102.has_column
  canonical_edge_type: HAS_COLUMN
  source_card_id: table.zs_observe.target_tcin_mapping
  target_card_id: column.zs_observe.target_tcin_mapping.group_level_id
  source_type: table
  target_type: column
  inverse_edge_type: BELONGS_TO_TABLE
  materialize_inverse: true
  legacy_edge_aliases: []
  edge_class: canonical
  canonical_cognee_edge: true
```
```yaml
candidate_edge:
  edge_id: edge.target_plus.00103.belongs_to_table
  canonical_edge_type: BELONGS_TO_TABLE
  source_card_id: column.zs_observe.target_tcin_mapping.group_id
  target_card_id: table.zs_observe.target_tcin_mapping
  source_type: column
  target_type: table
  inverse_edge_type: HAS_COLUMN
  materialize_inverse: true
  legacy_edge_aliases:
  - column_belongs_to_table
  edge_class: canonical
  canonical_cognee_edge: true
```
```yaml
candidate_edge:
  edge_id: edge.target_plus.00104.has_column
  canonical_edge_type: HAS_COLUMN
  source_card_id: table.zs_observe.target_tcin_mapping
  target_card_id: column.zs_observe.target_tcin_mapping.group_id
  source_type: table
  target_type: column
  inverse_edge_type: BELONGS_TO_TABLE
  materialize_inverse: true
  legacy_edge_aliases: []
  edge_class: canonical
  canonical_cognee_edge: true
```
```yaml
candidate_edge:
  edge_id: edge.target_plus.00105.belongs_to_table
  canonical_edge_type: BELONGS_TO_TABLE
  source_card_id: column.zs_observe.target_tcin_mapping.file_uuid
  target_card_id: table.zs_observe.target_tcin_mapping
  source_type: column
  target_type: table
  inverse_edge_type: HAS_COLUMN
  materialize_inverse: true
  legacy_edge_aliases:
  - column_belongs_to_table
  edge_class: canonical
  canonical_cognee_edge: true
```
```yaml
candidate_edge:
  edge_id: edge.target_plus.00106.has_column
  canonical_edge_type: HAS_COLUMN
  source_card_id: table.zs_observe.target_tcin_mapping
  target_card_id: column.zs_observe.target_tcin_mapping.file_uuid
  source_type: table
  target_type: column
  inverse_edge_type: BELONGS_TO_TABLE
  materialize_inverse: true
  legacy_edge_aliases: []
  edge_class: canonical
  canonical_cognee_edge: true
```
```yaml
candidate_edge:
  edge_id: edge.target_plus.00107.belongs_to_table
  canonical_edge_type: BELONGS_TO_TABLE
  source_card_id: column.zs_observe.target_tcin_mapping.is_active
  target_card_id: table.zs_observe.target_tcin_mapping
  source_type: column
  target_type: table
  inverse_edge_type: HAS_COLUMN
  materialize_inverse: true
  legacy_edge_aliases:
  - column_belongs_to_table
  edge_class: canonical
  canonical_cognee_edge: true
```
```yaml
candidate_edge:
  edge_id: edge.target_plus.00108.has_column
  canonical_edge_type: HAS_COLUMN
  source_card_id: table.zs_observe.target_tcin_mapping
  target_card_id: column.zs_observe.target_tcin_mapping.is_active
  source_type: table
  target_type: column
  inverse_edge_type: BELONGS_TO_TABLE
  materialize_inverse: true
  legacy_edge_aliases: []
  edge_class: canonical
  canonical_cognee_edge: true
```
```yaml
candidate_edge:
  edge_id: edge.target_plus.00109.belongs_to_table
  canonical_edge_type: BELONGS_TO_TABLE
  source_card_id: column.zs_observe.target_tcin_mapping.is_duplicated
  target_card_id: table.zs_observe.target_tcin_mapping
  source_type: column
  target_type: table
  inverse_edge_type: HAS_COLUMN
  materialize_inverse: true
  legacy_edge_aliases:
  - column_belongs_to_table
  edge_class: canonical
  canonical_cognee_edge: true
```
```yaml
candidate_edge:
  edge_id: edge.target_plus.00110.has_column
  canonical_edge_type: HAS_COLUMN
  source_card_id: table.zs_observe.target_tcin_mapping
  target_card_id: column.zs_observe.target_tcin_mapping.is_duplicated
  source_type: table
  target_type: column
  inverse_edge_type: BELONGS_TO_TABLE
  materialize_inverse: true
  legacy_edge_aliases: []
  edge_class: canonical
  canonical_cognee_edge: true
```
```yaml
candidate_edge:
  edge_id: edge.target_plus.00111.belongs_to_table
  canonical_edge_type: BELONGS_TO_TABLE
  source_card_id: column.zs_observe.target_tcin_mapping.zen_status
  target_card_id: table.zs_observe.target_tcin_mapping
  source_type: column
  target_type: table
  inverse_edge_type: HAS_COLUMN
  materialize_inverse: true
  legacy_edge_aliases:
  - column_belongs_to_table
  edge_class: canonical
  canonical_cognee_edge: true
```
```yaml
candidate_edge:
  edge_id: edge.target_plus.00112.has_column
  canonical_edge_type: HAS_COLUMN
  source_card_id: table.zs_observe.target_tcin_mapping
  target_card_id: column.zs_observe.target_tcin_mapping.zen_status
  source_type: table
  target_type: column
  inverse_edge_type: BELONGS_TO_TABLE
  materialize_inverse: true
  legacy_edge_aliases: []
  edge_class: canonical
  canonical_cognee_edge: true
```
```yaml
candidate_edge:
  edge_id: edge.target_plus.00113.belongs_to_table
  canonical_edge_type: BELONGS_TO_TABLE
  source_card_id: column.zs_observe.target_tcin_mapping.zen_sheet_name
  target_card_id: table.zs_observe.target_tcin_mapping
  source_type: column
  target_type: table
  inverse_edge_type: HAS_COLUMN
  materialize_inverse: true
  legacy_edge_aliases:
  - column_belongs_to_table
  edge_class: canonical
  canonical_cognee_edge: true
```
```yaml
candidate_edge:
  edge_id: edge.target_plus.00114.has_column
  canonical_edge_type: HAS_COLUMN
  source_card_id: table.zs_observe.target_tcin_mapping
  target_card_id: column.zs_observe.target_tcin_mapping.zen_sheet_name
  source_type: table
  target_type: column
  inverse_edge_type: BELONGS_TO_TABLE
  materialize_inverse: true
  legacy_edge_aliases: []
  edge_class: canonical
  canonical_cognee_edge: true
```
```yaml
candidate_edge:
  edge_id: edge.target_plus.00115.belongs_to_table
  canonical_edge_type: BELONGS_TO_TABLE
  source_card_id: column.zs_observe.target_tcin_mapping.created_at
  target_card_id: table.zs_observe.target_tcin_mapping
  source_type: column
  target_type: table
  inverse_edge_type: HAS_COLUMN
  materialize_inverse: true
  legacy_edge_aliases:
  - column_belongs_to_table
  edge_class: canonical
  canonical_cognee_edge: true
```
```yaml
candidate_edge:
  edge_id: edge.target_plus.00116.has_column
  canonical_edge_type: HAS_COLUMN
  source_card_id: table.zs_observe.target_tcin_mapping
  target_card_id: column.zs_observe.target_tcin_mapping.created_at
  source_type: table
  target_type: column
  inverse_edge_type: BELONGS_TO_TABLE
  materialize_inverse: true
  legacy_edge_aliases: []
  edge_class: canonical
  canonical_cognee_edge: true
```
```yaml
candidate_edge:
  edge_id: edge.target_plus.00117.belongs_to_table
  canonical_edge_type: BELONGS_TO_TABLE
  source_card_id: column.zs_observe.target_tcin_mapping.updated_at
  target_card_id: table.zs_observe.target_tcin_mapping
  source_type: column
  target_type: table
  inverse_edge_type: HAS_COLUMN
  materialize_inverse: true
  legacy_edge_aliases:
  - column_belongs_to_table
  edge_class: canonical
  canonical_cognee_edge: true
```
```yaml
candidate_edge:
  edge_id: edge.target_plus.00118.has_column
  canonical_edge_type: HAS_COLUMN
  source_card_id: table.zs_observe.target_tcin_mapping
  target_card_id: column.zs_observe.target_tcin_mapping.updated_at
  source_type: table
  target_type: column
  inverse_edge_type: BELONGS_TO_TABLE
  materialize_inverse: true
  legacy_edge_aliases: []
  edge_class: canonical
  canonical_cognee_edge: true
```
```yaml
candidate_edge:
  edge_id: edge.target_plus.00119.belongs_to_table
  canonical_edge_type: BELONGS_TO_TABLE
  source_card_id: column.zs_observe.target_tcin_mapping.deleted_at
  target_card_id: table.zs_observe.target_tcin_mapping
  source_type: column
  target_type: table
  inverse_edge_type: HAS_COLUMN
  materialize_inverse: true
  legacy_edge_aliases:
  - column_belongs_to_table
  edge_class: canonical
  canonical_cognee_edge: true
```
```yaml
candidate_edge:
  edge_id: edge.target_plus.00120.has_column
  canonical_edge_type: HAS_COLUMN
  source_card_id: table.zs_observe.target_tcin_mapping
  target_card_id: column.zs_observe.target_tcin_mapping.deleted_at
  source_type: table
  target_type: column
  inverse_edge_type: BELONGS_TO_TABLE
  materialize_inverse: true
  legacy_edge_aliases: []
  edge_class: canonical
  canonical_cognee_edge: true
```
```yaml
candidate_edge:
  edge_id: edge.target_plus.00121.belongs_to_table
  canonical_edge_type: BELONGS_TO_TABLE
  source_card_id: column.zs_observe.target_returns.unique_id
  target_card_id: table.zs_observe.target_returns
  source_type: column
  target_type: table
  inverse_edge_type: HAS_COLUMN
  materialize_inverse: true
  legacy_edge_aliases:
  - column_belongs_to_table
  edge_class: canonical
  canonical_cognee_edge: true
```
```yaml
candidate_edge:
  edge_id: edge.target_plus.00122.has_column
  canonical_edge_type: HAS_COLUMN
  source_card_id: table.zs_observe.target_returns
  target_card_id: column.zs_observe.target_returns.unique_id
  source_type: table
  target_type: column
  inverse_edge_type: BELONGS_TO_TABLE
  materialize_inverse: true
  legacy_edge_aliases: []
  edge_class: canonical
  canonical_cognee_edge: true
```
```yaml
candidate_edge:
  edge_id: edge.target_plus.00123.belongs_to_table
  canonical_edge_type: BELONGS_TO_TABLE
  source_card_id: column.zs_observe.target_returns.txn_uuid
  target_card_id: table.zs_observe.target_returns
  source_type: column
  target_type: table
  inverse_edge_type: HAS_COLUMN
  materialize_inverse: true
  legacy_edge_aliases:
  - column_belongs_to_table
  edge_class: canonical
  canonical_cognee_edge: true
```
```yaml
candidate_edge:
  edge_id: edge.target_plus.00124.has_column
  canonical_edge_type: HAS_COLUMN
  source_card_id: table.zs_observe.target_returns
  target_card_id: column.zs_observe.target_returns.txn_uuid
  source_type: table
  target_type: column
  inverse_edge_type: BELONGS_TO_TABLE
  materialize_inverse: true
  legacy_edge_aliases: []
  edge_class: canonical
  canonical_cognee_edge: true
```
```yaml
candidate_edge:
  edge_id: edge.target_plus.00125.belongs_to_table
  canonical_edge_type: BELONGS_TO_TABLE
  source_card_id: column.zs_observe.target_returns.unique_value
  target_card_id: table.zs_observe.target_returns
  source_type: column
  target_type: table
  inverse_edge_type: HAS_COLUMN
  materialize_inverse: true
  legacy_edge_aliases:
  - column_belongs_to_table
  edge_class: canonical
  canonical_cognee_edge: true
```
```yaml
candidate_edge:
  edge_id: edge.target_plus.00126.has_column
  canonical_edge_type: HAS_COLUMN
  source_card_id: table.zs_observe.target_returns
  target_card_id: column.zs_observe.target_returns.unique_value
  source_type: table
  target_type: column
  inverse_edge_type: BELONGS_TO_TABLE
  materialize_inverse: true
  legacy_edge_aliases: []
  edge_class: canonical
  canonical_cognee_edge: true
```
```yaml
candidate_edge:
  edge_id: edge.target_plus.00127.belongs_to_table
  canonical_edge_type: BELONGS_TO_TABLE
  source_card_id: column.zs_observe.target_returns.order_id
  target_card_id: table.zs_observe.target_returns
  source_type: column
  target_type: table
  inverse_edge_type: HAS_COLUMN
  materialize_inverse: true
  legacy_edge_aliases:
  - column_belongs_to_table
  edge_class: canonical
  canonical_cognee_edge: true
```
```yaml
candidate_edge:
  edge_id: edge.target_plus.00128.has_column
  canonical_edge_type: HAS_COLUMN
  source_card_id: table.zs_observe.target_returns
  target_card_id: column.zs_observe.target_returns.order_id
  source_type: table
  target_type: column
  inverse_edge_type: BELONGS_TO_TABLE
  materialize_inverse: true
  legacy_edge_aliases: []
  edge_class: canonical
  canonical_cognee_edge: true
```
```yaml
candidate_edge:
  edge_id: edge.target_plus.00129.belongs_to_table
  canonical_edge_type: BELONGS_TO_TABLE
  source_card_id: column.zs_observe.target_returns.item_id
  target_card_id: table.zs_observe.target_returns
  source_type: column
  target_type: table
  inverse_edge_type: HAS_COLUMN
  materialize_inverse: true
  legacy_edge_aliases:
  - column_belongs_to_table
  edge_class: canonical
  canonical_cognee_edge: true
```
```yaml
candidate_edge:
  edge_id: edge.target_plus.00130.has_column
  canonical_edge_type: HAS_COLUMN
  source_card_id: table.zs_observe.target_returns
  target_card_id: column.zs_observe.target_returns.item_id
  source_type: table
  target_type: column
  inverse_edge_type: BELONGS_TO_TABLE
  materialize_inverse: true
  legacy_edge_aliases: []
  edge_class: canonical
  canonical_cognee_edge: true
```
```yaml
candidate_edge:
  edge_id: edge.target_plus.00131.belongs_to_table
  canonical_edge_type: BELONGS_TO_TABLE
  source_card_id: column.zs_observe.target_returns.other_id
  target_card_id: table.zs_observe.target_returns
  source_type: column
  target_type: table
  inverse_edge_type: HAS_COLUMN
  materialize_inverse: true
  legacy_edge_aliases:
  - column_belongs_to_table
  edge_class: canonical
  canonical_cognee_edge: true
```
```yaml
candidate_edge:
  edge_id: edge.target_plus.00132.has_column
  canonical_edge_type: HAS_COLUMN
  source_card_id: table.zs_observe.target_returns
  target_card_id: column.zs_observe.target_returns.other_id
  source_type: table
  target_type: column
  inverse_edge_type: BELONGS_TO_TABLE
  materialize_inverse: true
  legacy_edge_aliases: []
  edge_class: canonical
  canonical_cognee_edge: true
```
```yaml
candidate_edge:
  edge_id: edge.target_plus.00133.belongs_to_table
  canonical_edge_type: BELONGS_TO_TABLE
  source_card_id: column.zs_observe.target_returns.sku_id
  target_card_id: table.zs_observe.target_returns
  source_type: column
  target_type: table
  inverse_edge_type: HAS_COLUMN
  materialize_inverse: true
  legacy_edge_aliases:
  - column_belongs_to_table
  edge_class: canonical
  canonical_cognee_edge: true
```
```yaml
candidate_edge:
  edge_id: edge.target_plus.00134.has_column
  canonical_edge_type: HAS_COLUMN
  source_card_id: table.zs_observe.target_returns
  target_card_id: column.zs_observe.target_returns.sku_id
  source_type: table
  target_type: column
  inverse_edge_type: BELONGS_TO_TABLE
  materialize_inverse: true
  legacy_edge_aliases: []
  edge_class: canonical
  canonical_cognee_edge: true
```
```yaml
candidate_edge:
  edge_id: edge.target_plus.00135.belongs_to_table
  canonical_edge_type: BELONGS_TO_TABLE
  source_card_id: column.zs_observe.target_returns.tcin
  target_card_id: table.zs_observe.target_returns
  source_type: column
  target_type: table
  inverse_edge_type: HAS_COLUMN
  materialize_inverse: true
  legacy_edge_aliases:
  - column_belongs_to_table
  edge_class: canonical
  canonical_cognee_edge: true
```
```yaml
candidate_edge:
  edge_id: edge.target_plus.00136.has_column
  canonical_edge_type: HAS_COLUMN
  source_card_id: table.zs_observe.target_returns
  target_card_id: column.zs_observe.target_returns.tcin
  source_type: table
  target_type: column
  inverse_edge_type: BELONGS_TO_TABLE
  materialize_inverse: true
  legacy_edge_aliases: []
  edge_class: canonical
  canonical_cognee_edge: true
```
```yaml
candidate_edge:
  edge_id: edge.target_plus.00137.belongs_to_table
  canonical_edge_type: BELONGS_TO_TABLE
  source_card_id: column.zs_observe.target_returns.created_date
  target_card_id: table.zs_observe.target_returns
  source_type: column
  target_type: table
  inverse_edge_type: HAS_COLUMN
  materialize_inverse: true
  legacy_edge_aliases:
  - column_belongs_to_table
  edge_class: canonical
  canonical_cognee_edge: true
```
```yaml
candidate_edge:
  edge_id: edge.target_plus.00138.has_column
  canonical_edge_type: HAS_COLUMN
  source_card_id: table.zs_observe.target_returns
  target_card_id: column.zs_observe.target_returns.created_date
  source_type: table
  target_type: column
  inverse_edge_type: BELONGS_TO_TABLE
  materialize_inverse: true
  legacy_edge_aliases: []
  edge_class: canonical
  canonical_cognee_edge: true
```
```yaml
candidate_edge:
  edge_id: edge.target_plus.00139.belongs_to_table
  canonical_edge_type: BELONGS_TO_TABLE
  source_card_id: column.zs_observe.target_returns.returned_date
  target_card_id: table.zs_observe.target_returns
  source_type: column
  target_type: table
  inverse_edge_type: HAS_COLUMN
  materialize_inverse: true
  legacy_edge_aliases:
  - column_belongs_to_table
  edge_class: canonical
  canonical_cognee_edge: true
```
```yaml
candidate_edge:
  edge_id: edge.target_plus.00140.has_column
  canonical_edge_type: HAS_COLUMN
  source_card_id: table.zs_observe.target_returns
  target_card_id: column.zs_observe.target_returns.returned_date
  source_type: table
  target_type: column
  inverse_edge_type: BELONGS_TO_TABLE
  materialize_inverse: true
  legacy_edge_aliases: []
  edge_class: canonical
  canonical_cognee_edge: true
```
```yaml
candidate_edge:
  edge_id: edge.target_plus.00141.belongs_to_table
  canonical_edge_type: BELONGS_TO_TABLE
  source_card_id: column.zs_observe.target_returns.charged_amount
  target_card_id: table.zs_observe.target_returns
  source_type: column
  target_type: table
  inverse_edge_type: HAS_COLUMN
  materialize_inverse: true
  legacy_edge_aliases:
  - column_belongs_to_table
  edge_class: canonical
  canonical_cognee_edge: true
```
```yaml
candidate_edge:
  edge_id: edge.target_plus.00142.has_column
  canonical_edge_type: HAS_COLUMN
  source_card_id: table.zs_observe.target_returns
  target_card_id: column.zs_observe.target_returns.charged_amount
  source_type: table
  target_type: column
  inverse_edge_type: BELONGS_TO_TABLE
  materialize_inverse: true
  legacy_edge_aliases: []
  edge_class: canonical
  canonical_cognee_edge: true
```
```yaml
candidate_edge:
  edge_id: edge.target_plus.00143.belongs_to_table
  canonical_edge_type: BELONGS_TO_TABLE
  source_card_id: column.zs_observe.target_returns.quantity
  target_card_id: table.zs_observe.target_returns
  source_type: column
  target_type: table
  inverse_edge_type: HAS_COLUMN
  materialize_inverse: true
  legacy_edge_aliases:
  - column_belongs_to_table
  edge_class: canonical
  canonical_cognee_edge: true
```
```yaml
candidate_edge:
  edge_id: edge.target_plus.00144.has_column
  canonical_edge_type: HAS_COLUMN
  source_card_id: table.zs_observe.target_returns
  target_card_id: column.zs_observe.target_returns.quantity
  source_type: table
  target_type: column
  inverse_edge_type: BELONGS_TO_TABLE
  materialize_inverse: true
  legacy_edge_aliases: []
  edge_class: canonical
  canonical_cognee_edge: true
```
```yaml
candidate_edge:
  edge_id: edge.target_plus.00145.belongs_to_table
  canonical_edge_type: BELONGS_TO_TABLE
  source_card_id: column.zs_observe.target_returns.transaction_type
  target_card_id: table.zs_observe.target_returns
  source_type: column
  target_type: table
  inverse_edge_type: HAS_COLUMN
  materialize_inverse: true
  legacy_edge_aliases:
  - column_belongs_to_table
  edge_class: canonical
  canonical_cognee_edge: true
```
```yaml
candidate_edge:
  edge_id: edge.target_plus.00146.has_column
  canonical_edge_type: HAS_COLUMN
  source_card_id: table.zs_observe.target_returns
  target_card_id: column.zs_observe.target_returns.transaction_type
  source_type: table
  target_type: column
  inverse_edge_type: BELONGS_TO_TABLE
  materialize_inverse: true
  legacy_edge_aliases: []
  edge_class: canonical
  canonical_cognee_edge: true
```
```yaml
candidate_edge:
  edge_id: edge.target_plus.00147.belongs_to_table
  canonical_edge_type: BELONGS_TO_TABLE
  source_card_id: column.zs_observe.target_returns.internal_txn_type
  target_card_id: table.zs_observe.target_returns
  source_type: column
  target_type: table
  inverse_edge_type: HAS_COLUMN
  materialize_inverse: true
  legacy_edge_aliases:
  - column_belongs_to_table
  edge_class: canonical
  canonical_cognee_edge: true
```
```yaml
candidate_edge:
  edge_id: edge.target_plus.00148.has_column
  canonical_edge_type: HAS_COLUMN
  source_card_id: table.zs_observe.target_returns
  target_card_id: column.zs_observe.target_returns.internal_txn_type
  source_type: table
  target_type: column
  inverse_edge_type: BELONGS_TO_TABLE
  materialize_inverse: true
  legacy_edge_aliases: []
  edge_class: canonical
  canonical_cognee_edge: true
```
```yaml
candidate_edge:
  edge_id: edge.target_plus.00149.belongs_to_table
  canonical_edge_type: BELONGS_TO_TABLE
  source_card_id: column.zs_observe.target_returns.order_status
  target_card_id: table.zs_observe.target_returns
  source_type: column
  target_type: table
  inverse_edge_type: HAS_COLUMN
  materialize_inverse: true
  legacy_edge_aliases:
  - column_belongs_to_table
  edge_class: canonical
  canonical_cognee_edge: true
```
```yaml
candidate_edge:
  edge_id: edge.target_plus.00150.has_column
  canonical_edge_type: HAS_COLUMN
  source_card_id: table.zs_observe.target_returns
  target_card_id: column.zs_observe.target_returns.order_status
  source_type: table
  target_type: column
  inverse_edge_type: BELONGS_TO_TABLE
  materialize_inverse: true
  legacy_edge_aliases: []
  edge_class: canonical
  canonical_cognee_edge: true
```
```yaml
candidate_edge:
  edge_id: edge.target_plus.00151.belongs_to_table
  canonical_edge_type: BELONGS_TO_TABLE
  source_card_id: column.zs_observe.target_returns.description
  target_card_id: table.zs_observe.target_returns
  source_type: column
  target_type: table
  inverse_edge_type: HAS_COLUMN
  materialize_inverse: true
  legacy_edge_aliases:
  - column_belongs_to_table
  edge_class: canonical
  canonical_cognee_edge: true
```
```yaml
candidate_edge:
  edge_id: edge.target_plus.00152.has_column
  canonical_edge_type: HAS_COLUMN
  source_card_id: table.zs_observe.target_returns
  target_card_id: column.zs_observe.target_returns.description
  source_type: table
  target_type: column
  inverse_edge_type: BELONGS_TO_TABLE
  materialize_inverse: true
  legacy_edge_aliases: []
  edge_class: canonical
  canonical_cognee_edge: true
```
```yaml
candidate_edge:
  edge_id: edge.target_plus.00153.belongs_to_table
  canonical_edge_type: BELONGS_TO_TABLE
  source_card_id: column.zs_observe.target_returns.brand
  target_card_id: table.zs_observe.target_returns
  source_type: column
  target_type: table
  inverse_edge_type: HAS_COLUMN
  materialize_inverse: true
  legacy_edge_aliases:
  - column_belongs_to_table
  edge_class: canonical
  canonical_cognee_edge: true
```
```yaml
candidate_edge:
  edge_id: edge.target_plus.00154.has_column
  canonical_edge_type: HAS_COLUMN
  source_card_id: table.zs_observe.target_returns
  target_card_id: column.zs_observe.target_returns.brand
  source_type: table
  target_type: column
  inverse_edge_type: BELONGS_TO_TABLE
  materialize_inverse: true
  legacy_edge_aliases: []
  edge_class: canonical
  canonical_cognee_edge: true
```
```yaml
candidate_edge:
  edge_id: edge.target_plus.00155.belongs_to_table
  canonical_edge_type: BELONGS_TO_TABLE
  source_card_id: column.zs_observe.target_returns.group_level_id
  target_card_id: table.zs_observe.target_returns
  source_type: column
  target_type: table
  inverse_edge_type: HAS_COLUMN
  materialize_inverse: true
  legacy_edge_aliases:
  - column_belongs_to_table
  edge_class: canonical
  canonical_cognee_edge: true
```
```yaml
candidate_edge:
  edge_id: edge.target_plus.00156.has_column
  canonical_edge_type: HAS_COLUMN
  source_card_id: table.zs_observe.target_returns
  target_card_id: column.zs_observe.target_returns.group_level_id
  source_type: table
  target_type: column
  inverse_edge_type: BELONGS_TO_TABLE
  materialize_inverse: true
  legacy_edge_aliases: []
  edge_class: canonical
  canonical_cognee_edge: true
```
```yaml
candidate_edge:
  edge_id: edge.target_plus.00157.belongs_to_table
  canonical_edge_type: BELONGS_TO_TABLE
  source_card_id: column.zs_observe.target_returns.currency_type
  target_card_id: table.zs_observe.target_returns
  source_type: column
  target_type: table
  inverse_edge_type: HAS_COLUMN
  materialize_inverse: true
  legacy_edge_aliases:
  - column_belongs_to_table
  edge_class: canonical
  canonical_cognee_edge: true
```
```yaml
candidate_edge:
  edge_id: edge.target_plus.00158.has_column
  canonical_edge_type: HAS_COLUMN
  source_card_id: table.zs_observe.target_returns
  target_card_id: column.zs_observe.target_returns.currency_type
  source_type: table
  target_type: column
  inverse_edge_type: BELONGS_TO_TABLE
  materialize_inverse: true
  legacy_edge_aliases: []
  edge_class: canonical
  canonical_cognee_edge: true
```
```yaml
candidate_edge:
  edge_id: edge.target_plus.00159.belongs_to_table
  canonical_edge_type: BELONGS_TO_TABLE
  source_card_id: column.zs_observe.target_returns.is_active
  target_card_id: table.zs_observe.target_returns
  source_type: column
  target_type: table
  inverse_edge_type: HAS_COLUMN
  materialize_inverse: true
  legacy_edge_aliases:
  - column_belongs_to_table
  edge_class: canonical
  canonical_cognee_edge: true
```
```yaml
candidate_edge:
  edge_id: edge.target_plus.00160.has_column
  canonical_edge_type: HAS_COLUMN
  source_card_id: table.zs_observe.target_returns
  target_card_id: column.zs_observe.target_returns.is_active
  source_type: table
  target_type: column
  inverse_edge_type: BELONGS_TO_TABLE
  materialize_inverse: true
  legacy_edge_aliases: []
  edge_class: canonical
  canonical_cognee_edge: true
```
```yaml
candidate_edge:
  edge_id: edge.target_plus.00161.belongs_to_table
  canonical_edge_type: BELONGS_TO_TABLE
  source_card_id: column.zs_observe.target_returns.zen_sheet_name
  target_card_id: table.zs_observe.target_returns
  source_type: column
  target_type: table
  inverse_edge_type: HAS_COLUMN
  materialize_inverse: true
  legacy_edge_aliases:
  - column_belongs_to_table
  edge_class: canonical
  canonical_cognee_edge: true
```
```yaml
candidate_edge:
  edge_id: edge.target_plus.00162.has_column
  canonical_edge_type: HAS_COLUMN
  source_card_id: table.zs_observe.target_returns
  target_card_id: column.zs_observe.target_returns.zen_sheet_name
  source_type: table
  target_type: column
  inverse_edge_type: BELONGS_TO_TABLE
  materialize_inverse: true
  legacy_edge_aliases: []
  edge_class: canonical
  canonical_cognee_edge: true
```
```yaml
candidate_edge:
  edge_id: edge.target_plus.00163.belongs_to_table
  canonical_edge_type: BELONGS_TO_TABLE
  source_card_id: column.zs_observe.target_returns.created_at
  target_card_id: table.zs_observe.target_returns
  source_type: column
  target_type: table
  inverse_edge_type: HAS_COLUMN
  materialize_inverse: true
  legacy_edge_aliases:
  - column_belongs_to_table
  edge_class: canonical
  canonical_cognee_edge: true
```
```yaml
candidate_edge:
  edge_id: edge.target_plus.00164.has_column
  canonical_edge_type: HAS_COLUMN
  source_card_id: table.zs_observe.target_returns
  target_card_id: column.zs_observe.target_returns.created_at
  source_type: table
  target_type: column
  inverse_edge_type: BELONGS_TO_TABLE
  materialize_inverse: true
  legacy_edge_aliases: []
  edge_class: canonical
  canonical_cognee_edge: true
```
```yaml
candidate_edge:
  edge_id: edge.target_plus.00165.belongs_to_table
  canonical_edge_type: BELONGS_TO_TABLE
  source_card_id: column.zs_observe.target_returns.updated_at
  target_card_id: table.zs_observe.target_returns
  source_type: column
  target_type: table
  inverse_edge_type: HAS_COLUMN
  materialize_inverse: true
  legacy_edge_aliases:
  - column_belongs_to_table
  edge_class: canonical
  canonical_cognee_edge: true
```
```yaml
candidate_edge:
  edge_id: edge.target_plus.00166.has_column
  canonical_edge_type: HAS_COLUMN
  source_card_id: table.zs_observe.target_returns
  target_card_id: column.zs_observe.target_returns.updated_at
  source_type: table
  target_type: column
  inverse_edge_type: BELONGS_TO_TABLE
  materialize_inverse: true
  legacy_edge_aliases: []
  edge_class: canonical
  canonical_cognee_edge: true
```
```yaml
candidate_edge:
  edge_id: edge.target_plus.00167.belongs_to_table
  canonical_edge_type: BELONGS_TO_TABLE
  source_card_id: column.zs_observe.target_returns.deleted_at
  target_card_id: table.zs_observe.target_returns
  source_type: column
  target_type: table
  inverse_edge_type: HAS_COLUMN
  materialize_inverse: true
  legacy_edge_aliases:
  - column_belongs_to_table
  edge_class: canonical
  canonical_cognee_edge: true
```
```yaml
candidate_edge:
  edge_id: edge.target_plus.00168.has_column
  canonical_edge_type: HAS_COLUMN
  source_card_id: table.zs_observe.target_returns
  target_card_id: column.zs_observe.target_returns.deleted_at
  source_type: table
  target_type: column
  inverse_edge_type: BELONGS_TO_TABLE
  materialize_inverse: true
  legacy_edge_aliases: []
  edge_class: canonical
  canonical_cognee_edge: true
```
```yaml
candidate_edge:
  edge_id: edge.target_plus.00169.belongs_to_table
  canonical_edge_type: BELONGS_TO_TABLE
  source_card_id: column.zs_observe.target_sales.unique_id
  target_card_id: table.zs_observe.target_sales
  source_type: column
  target_type: table
  inverse_edge_type: HAS_COLUMN
  materialize_inverse: true
  legacy_edge_aliases:
  - column_belongs_to_table
  edge_class: canonical
  canonical_cognee_edge: true
```
```yaml
candidate_edge:
  edge_id: edge.target_plus.00170.has_column
  canonical_edge_type: HAS_COLUMN
  source_card_id: table.zs_observe.target_sales
  target_card_id: column.zs_observe.target_sales.unique_id
  source_type: table
  target_type: column
  inverse_edge_type: BELONGS_TO_TABLE
  materialize_inverse: true
  legacy_edge_aliases: []
  edge_class: canonical
  canonical_cognee_edge: true
```
```yaml
candidate_edge:
  edge_id: edge.target_plus.00171.belongs_to_table
  canonical_edge_type: BELONGS_TO_TABLE
  source_card_id: column.zs_observe.target_sales.txn_uuid
  target_card_id: table.zs_observe.target_sales
  source_type: column
  target_type: table
  inverse_edge_type: HAS_COLUMN
  materialize_inverse: true
  legacy_edge_aliases:
  - column_belongs_to_table
  edge_class: canonical
  canonical_cognee_edge: true
```
```yaml
candidate_edge:
  edge_id: edge.target_plus.00172.has_column
  canonical_edge_type: HAS_COLUMN
  source_card_id: table.zs_observe.target_sales
  target_card_id: column.zs_observe.target_sales.txn_uuid
  source_type: table
  target_type: column
  inverse_edge_type: BELONGS_TO_TABLE
  materialize_inverse: true
  legacy_edge_aliases: []
  edge_class: canonical
  canonical_cognee_edge: true
```
```yaml
candidate_edge:
  edge_id: edge.target_plus.00173.belongs_to_table
  canonical_edge_type: BELONGS_TO_TABLE
  source_card_id: column.zs_observe.target_sales.unique_value
  target_card_id: table.zs_observe.target_sales
  source_type: column
  target_type: table
  inverse_edge_type: HAS_COLUMN
  materialize_inverse: true
  legacy_edge_aliases:
  - column_belongs_to_table
  edge_class: canonical
  canonical_cognee_edge: true
```
```yaml
candidate_edge:
  edge_id: edge.target_plus.00174.has_column
  canonical_edge_type: HAS_COLUMN
  source_card_id: table.zs_observe.target_sales
  target_card_id: column.zs_observe.target_sales.unique_value
  source_type: table
  target_type: column
  inverse_edge_type: BELONGS_TO_TABLE
  materialize_inverse: true
  legacy_edge_aliases: []
  edge_class: canonical
  canonical_cognee_edge: true
```
```yaml
candidate_edge:
  edge_id: edge.target_plus.00175.belongs_to_table
  canonical_edge_type: BELONGS_TO_TABLE
  source_card_id: column.zs_observe.target_sales.order_id
  target_card_id: table.zs_observe.target_sales
  source_type: column
  target_type: table
  inverse_edge_type: HAS_COLUMN
  materialize_inverse: true
  legacy_edge_aliases:
  - column_belongs_to_table
  edge_class: canonical
  canonical_cognee_edge: true
```
```yaml
candidate_edge:
  edge_id: edge.target_plus.00176.has_column
  canonical_edge_type: HAS_COLUMN
  source_card_id: table.zs_observe.target_sales
  target_card_id: column.zs_observe.target_sales.order_id
  source_type: table
  target_type: column
  inverse_edge_type: BELONGS_TO_TABLE
  materialize_inverse: true
  legacy_edge_aliases: []
  edge_class: canonical
  canonical_cognee_edge: true
```
```yaml
candidate_edge:
  edge_id: edge.target_plus.00177.belongs_to_table
  canonical_edge_type: BELONGS_TO_TABLE
  source_card_id: column.zs_observe.target_sales.item_id
  target_card_id: table.zs_observe.target_sales
  source_type: column
  target_type: table
  inverse_edge_type: HAS_COLUMN
  materialize_inverse: true
  legacy_edge_aliases:
  - column_belongs_to_table
  edge_class: canonical
  canonical_cognee_edge: true
```
```yaml
candidate_edge:
  edge_id: edge.target_plus.00178.has_column
  canonical_edge_type: HAS_COLUMN
  source_card_id: table.zs_observe.target_sales
  target_card_id: column.zs_observe.target_sales.item_id
  source_type: table
  target_type: column
  inverse_edge_type: BELONGS_TO_TABLE
  materialize_inverse: true
  legacy_edge_aliases: []
  edge_class: canonical
  canonical_cognee_edge: true
```
```yaml
candidate_edge:
  edge_id: edge.target_plus.00179.belongs_to_table
  canonical_edge_type: BELONGS_TO_TABLE
  source_card_id: column.zs_observe.target_sales.other_id
  target_card_id: table.zs_observe.target_sales
  source_type: column
  target_type: table
  inverse_edge_type: HAS_COLUMN
  materialize_inverse: true
  legacy_edge_aliases:
  - column_belongs_to_table
  edge_class: canonical
  canonical_cognee_edge: true
```
```yaml
candidate_edge:
  edge_id: edge.target_plus.00180.has_column
  canonical_edge_type: HAS_COLUMN
  source_card_id: table.zs_observe.target_sales
  target_card_id: column.zs_observe.target_sales.other_id
  source_type: table
  target_type: column
  inverse_edge_type: BELONGS_TO_TABLE
  materialize_inverse: true
  legacy_edge_aliases: []
  edge_class: canonical
  canonical_cognee_edge: true
```
```yaml
candidate_edge:
  edge_id: edge.target_plus.00181.belongs_to_table
  canonical_edge_type: BELONGS_TO_TABLE
  source_card_id: column.zs_observe.target_sales.sku_id
  target_card_id: table.zs_observe.target_sales
  source_type: column
  target_type: table
  inverse_edge_type: HAS_COLUMN
  materialize_inverse: true
  legacy_edge_aliases:
  - column_belongs_to_table
  edge_class: canonical
  canonical_cognee_edge: true
```
```yaml
candidate_edge:
  edge_id: edge.target_plus.00182.has_column
  canonical_edge_type: HAS_COLUMN
  source_card_id: table.zs_observe.target_sales
  target_card_id: column.zs_observe.target_sales.sku_id
  source_type: table
  target_type: column
  inverse_edge_type: BELONGS_TO_TABLE
  materialize_inverse: true
  legacy_edge_aliases: []
  edge_class: canonical
  canonical_cognee_edge: true
```
```yaml
candidate_edge:
  edge_id: edge.target_plus.00183.belongs_to_table
  canonical_edge_type: BELONGS_TO_TABLE
  source_card_id: column.zs_observe.target_sales.tcin
  target_card_id: table.zs_observe.target_sales
  source_type: column
  target_type: table
  inverse_edge_type: HAS_COLUMN
  materialize_inverse: true
  legacy_edge_aliases:
  - column_belongs_to_table
  edge_class: canonical
  canonical_cognee_edge: true
```
```yaml
candidate_edge:
  edge_id: edge.target_plus.00184.has_column
  canonical_edge_type: HAS_COLUMN
  source_card_id: table.zs_observe.target_sales
  target_card_id: column.zs_observe.target_sales.tcin
  source_type: table
  target_type: column
  inverse_edge_type: BELONGS_TO_TABLE
  materialize_inverse: true
  legacy_edge_aliases: []
  edge_class: canonical
  canonical_cognee_edge: true
```
```yaml
candidate_edge:
  edge_id: edge.target_plus.00185.belongs_to_table
  canonical_edge_type: BELONGS_TO_TABLE
  source_card_id: column.zs_observe.target_sales.created_date
  target_card_id: table.zs_observe.target_sales
  source_type: column
  target_type: table
  inverse_edge_type: HAS_COLUMN
  materialize_inverse: true
  legacy_edge_aliases:
  - column_belongs_to_table
  edge_class: canonical
  canonical_cognee_edge: true
```
```yaml
candidate_edge:
  edge_id: edge.target_plus.00186.has_column
  canonical_edge_type: HAS_COLUMN
  source_card_id: table.zs_observe.target_sales
  target_card_id: column.zs_observe.target_sales.created_date
  source_type: table
  target_type: column
  inverse_edge_type: BELONGS_TO_TABLE
  materialize_inverse: true
  legacy_edge_aliases: []
  edge_class: canonical
  canonical_cognee_edge: true
```
```yaml
candidate_edge:
  edge_id: edge.target_plus.00187.belongs_to_table
  canonical_edge_type: BELONGS_TO_TABLE
  source_card_id: column.zs_observe.target_sales.charged_amount
  target_card_id: table.zs_observe.target_sales
  source_type: column
  target_type: table
  inverse_edge_type: HAS_COLUMN
  materialize_inverse: true
  legacy_edge_aliases:
  - column_belongs_to_table
  edge_class: canonical
  canonical_cognee_edge: true
```
```yaml
candidate_edge:
  edge_id: edge.target_plus.00188.has_column
  canonical_edge_type: HAS_COLUMN
  source_card_id: table.zs_observe.target_sales
  target_card_id: column.zs_observe.target_sales.charged_amount
  source_type: table
  target_type: column
  inverse_edge_type: BELONGS_TO_TABLE
  materialize_inverse: true
  legacy_edge_aliases: []
  edge_class: canonical
  canonical_cognee_edge: true
```
```yaml
candidate_edge:
  edge_id: edge.target_plus.00189.belongs_to_table
  canonical_edge_type: BELONGS_TO_TABLE
  source_card_id: column.zs_observe.target_sales.discount_amount
  target_card_id: table.zs_observe.target_sales
  source_type: column
  target_type: table
  inverse_edge_type: HAS_COLUMN
  materialize_inverse: true
  legacy_edge_aliases:
  - column_belongs_to_table
  edge_class: canonical
  canonical_cognee_edge: true
```
```yaml
candidate_edge:
  edge_id: edge.target_plus.00190.has_column
  canonical_edge_type: HAS_COLUMN
  source_card_id: table.zs_observe.target_sales
  target_card_id: column.zs_observe.target_sales.discount_amount
  source_type: table
  target_type: column
  inverse_edge_type: BELONGS_TO_TABLE
  materialize_inverse: true
  legacy_edge_aliases: []
  edge_class: canonical
  canonical_cognee_edge: true
```
```yaml
candidate_edge:
  edge_id: edge.target_plus.00191.belongs_to_table
  canonical_edge_type: BELONGS_TO_TABLE
  source_card_id: column.zs_observe.target_sales.quantity
  target_card_id: table.zs_observe.target_sales
  source_type: column
  target_type: table
  inverse_edge_type: HAS_COLUMN
  materialize_inverse: true
  legacy_edge_aliases:
  - column_belongs_to_table
  edge_class: canonical
  canonical_cognee_edge: true
```
```yaml
candidate_edge:
  edge_id: edge.target_plus.00192.has_column
  canonical_edge_type: HAS_COLUMN
  source_card_id: table.zs_observe.target_sales
  target_card_id: column.zs_observe.target_sales.quantity
  source_type: table
  target_type: column
  inverse_edge_type: BELONGS_TO_TABLE
  materialize_inverse: true
  legacy_edge_aliases: []
  edge_class: canonical
  canonical_cognee_edge: true
```
```yaml
candidate_edge:
  edge_id: edge.target_plus.00193.belongs_to_table
  canonical_edge_type: BELONGS_TO_TABLE
  source_card_id: column.zs_observe.target_sales.transaction_type
  target_card_id: table.zs_observe.target_sales
  source_type: column
  target_type: table
  inverse_edge_type: HAS_COLUMN
  materialize_inverse: true
  legacy_edge_aliases:
  - column_belongs_to_table
  edge_class: canonical
  canonical_cognee_edge: true
```
```yaml
candidate_edge:
  edge_id: edge.target_plus.00194.has_column
  canonical_edge_type: HAS_COLUMN
  source_card_id: table.zs_observe.target_sales
  target_card_id: column.zs_observe.target_sales.transaction_type
  source_type: table
  target_type: column
  inverse_edge_type: BELONGS_TO_TABLE
  materialize_inverse: true
  legacy_edge_aliases: []
  edge_class: canonical
  canonical_cognee_edge: true
```
```yaml
candidate_edge:
  edge_id: edge.target_plus.00195.belongs_to_table
  canonical_edge_type: BELONGS_TO_TABLE
  source_card_id: column.zs_observe.target_sales.internal_txn_type
  target_card_id: table.zs_observe.target_sales
  source_type: column
  target_type: table
  inverse_edge_type: HAS_COLUMN
  materialize_inverse: true
  legacy_edge_aliases:
  - column_belongs_to_table
  edge_class: canonical
  canonical_cognee_edge: true
```
```yaml
candidate_edge:
  edge_id: edge.target_plus.00196.has_column
  canonical_edge_type: HAS_COLUMN
  source_card_id: table.zs_observe.target_sales
  target_card_id: column.zs_observe.target_sales.internal_txn_type
  source_type: table
  target_type: column
  inverse_edge_type: BELONGS_TO_TABLE
  materialize_inverse: true
  legacy_edge_aliases: []
  edge_class: canonical
  canonical_cognee_edge: true
```
```yaml
candidate_edge:
  edge_id: edge.target_plus.00197.belongs_to_table
  canonical_edge_type: BELONGS_TO_TABLE
  source_card_id: column.zs_observe.target_sales.order_status
  target_card_id: table.zs_observe.target_sales
  source_type: column
  target_type: table
  inverse_edge_type: HAS_COLUMN
  materialize_inverse: true
  legacy_edge_aliases:
  - column_belongs_to_table
  edge_class: canonical
  canonical_cognee_edge: true
```
```yaml
candidate_edge:
  edge_id: edge.target_plus.00198.has_column
  canonical_edge_type: HAS_COLUMN
  source_card_id: table.zs_observe.target_sales
  target_card_id: column.zs_observe.target_sales.order_status
  source_type: table
  target_type: column
  inverse_edge_type: BELONGS_TO_TABLE
  materialize_inverse: true
  legacy_edge_aliases: []
  edge_class: canonical
  canonical_cognee_edge: true
```
```yaml
candidate_edge:
  edge_id: edge.target_plus.00199.belongs_to_table
  canonical_edge_type: BELONGS_TO_TABLE
  source_card_id: column.zs_observe.target_sales.brand
  target_card_id: table.zs_observe.target_sales
  source_type: column
  target_type: table
  inverse_edge_type: HAS_COLUMN
  materialize_inverse: true
  legacy_edge_aliases:
  - column_belongs_to_table
  edge_class: canonical
  canonical_cognee_edge: true
```
```yaml
candidate_edge:
  edge_id: edge.target_plus.00200.has_column
  canonical_edge_type: HAS_COLUMN
  source_card_id: table.zs_observe.target_sales
  target_card_id: column.zs_observe.target_sales.brand
  source_type: table
  target_type: column
  inverse_edge_type: BELONGS_TO_TABLE
  materialize_inverse: true
  legacy_edge_aliases: []
  edge_class: canonical
  canonical_cognee_edge: true
```
```yaml
candidate_edge:
  edge_id: edge.target_plus.00201.belongs_to_table
  canonical_edge_type: BELONGS_TO_TABLE
  source_card_id: column.zs_observe.target_sales.description
  target_card_id: table.zs_observe.target_sales
  source_type: column
  target_type: table
  inverse_edge_type: HAS_COLUMN
  materialize_inverse: true
  legacy_edge_aliases:
  - column_belongs_to_table
  edge_class: canonical
  canonical_cognee_edge: true
```
```yaml
candidate_edge:
  edge_id: edge.target_plus.00202.has_column
  canonical_edge_type: HAS_COLUMN
  source_card_id: table.zs_observe.target_sales
  target_card_id: column.zs_observe.target_sales.description
  source_type: table
  target_type: column
  inverse_edge_type: BELONGS_TO_TABLE
  materialize_inverse: true
  legacy_edge_aliases: []
  edge_class: canonical
  canonical_cognee_edge: true
```
```yaml
candidate_edge:
  edge_id: edge.target_plus.00203.belongs_to_table
  canonical_edge_type: BELONGS_TO_TABLE
  source_card_id: column.zs_observe.target_sales.group_level_id
  target_card_id: table.zs_observe.target_sales
  source_type: column
  target_type: table
  inverse_edge_type: HAS_COLUMN
  materialize_inverse: true
  legacy_edge_aliases:
  - column_belongs_to_table
  edge_class: canonical
  canonical_cognee_edge: true
```
```yaml
candidate_edge:
  edge_id: edge.target_plus.00204.has_column
  canonical_edge_type: HAS_COLUMN
  source_card_id: table.zs_observe.target_sales
  target_card_id: column.zs_observe.target_sales.group_level_id
  source_type: table
  target_type: column
  inverse_edge_type: BELONGS_TO_TABLE
  materialize_inverse: true
  legacy_edge_aliases: []
  edge_class: canonical
  canonical_cognee_edge: true
```
```yaml
candidate_edge:
  edge_id: edge.target_plus.00205.belongs_to_table
  canonical_edge_type: BELONGS_TO_TABLE
  source_card_id: column.zs_observe.target_sales.group_id
  target_card_id: table.zs_observe.target_sales
  source_type: column
  target_type: table
  inverse_edge_type: HAS_COLUMN
  materialize_inverse: true
  legacy_edge_aliases:
  - column_belongs_to_table
  edge_class: canonical
  canonical_cognee_edge: true
```
```yaml
candidate_edge:
  edge_id: edge.target_plus.00206.has_column
  canonical_edge_type: HAS_COLUMN
  source_card_id: table.zs_observe.target_sales
  target_card_id: column.zs_observe.target_sales.group_id
  source_type: table
  target_type: column
  inverse_edge_type: BELONGS_TO_TABLE
  materialize_inverse: true
  legacy_edge_aliases: []
  edge_class: canonical
  canonical_cognee_edge: true
```
```yaml
candidate_edge:
  edge_id: edge.target_plus.00207.belongs_to_table
  canonical_edge_type: BELONGS_TO_TABLE
  source_card_id: column.zs_observe.target_sales.file_uuid
  target_card_id: table.zs_observe.target_sales
  source_type: column
  target_type: table
  inverse_edge_type: HAS_COLUMN
  materialize_inverse: true
  legacy_edge_aliases:
  - column_belongs_to_table
  edge_class: canonical
  canonical_cognee_edge: true
```
```yaml
candidate_edge:
  edge_id: edge.target_plus.00208.has_column
  canonical_edge_type: HAS_COLUMN
  source_card_id: table.zs_observe.target_sales
  target_card_id: column.zs_observe.target_sales.file_uuid
  source_type: table
  target_type: column
  inverse_edge_type: BELONGS_TO_TABLE
  materialize_inverse: true
  legacy_edge_aliases: []
  edge_class: canonical
  canonical_cognee_edge: true
```
```yaml
candidate_edge:
  edge_id: edge.target_plus.00209.belongs_to_table
  canonical_edge_type: BELONGS_TO_TABLE
  source_card_id: column.zs_observe.target_sales.currency_type
  target_card_id: table.zs_observe.target_sales
  source_type: column
  target_type: table
  inverse_edge_type: HAS_COLUMN
  materialize_inverse: true
  legacy_edge_aliases:
  - column_belongs_to_table
  edge_class: canonical
  canonical_cognee_edge: true
```
```yaml
candidate_edge:
  edge_id: edge.target_plus.00210.has_column
  canonical_edge_type: HAS_COLUMN
  source_card_id: table.zs_observe.target_sales
  target_card_id: column.zs_observe.target_sales.currency_type
  source_type: table
  target_type: column
  inverse_edge_type: BELONGS_TO_TABLE
  materialize_inverse: true
  legacy_edge_aliases: []
  edge_class: canonical
  canonical_cognee_edge: true
```
```yaml
candidate_edge:
  edge_id: edge.target_plus.00211.belongs_to_table
  canonical_edge_type: BELONGS_TO_TABLE
  source_card_id: column.zs_observe.target_sales.is_active
  target_card_id: table.zs_observe.target_sales
  source_type: column
  target_type: table
  inverse_edge_type: HAS_COLUMN
  materialize_inverse: true
  legacy_edge_aliases:
  - column_belongs_to_table
  edge_class: canonical
  canonical_cognee_edge: true
```
```yaml
candidate_edge:
  edge_id: edge.target_plus.00212.has_column
  canonical_edge_type: HAS_COLUMN
  source_card_id: table.zs_observe.target_sales
  target_card_id: column.zs_observe.target_sales.is_active
  source_type: table
  target_type: column
  inverse_edge_type: BELONGS_TO_TABLE
  materialize_inverse: true
  legacy_edge_aliases: []
  edge_class: canonical
  canonical_cognee_edge: true
```
```yaml
candidate_edge:
  edge_id: edge.target_plus.00213.belongs_to_table
  canonical_edge_type: BELONGS_TO_TABLE
  source_card_id: column.zs_observe.target_sales.is_duplicated
  target_card_id: table.zs_observe.target_sales
  source_type: column
  target_type: table
  inverse_edge_type: HAS_COLUMN
  materialize_inverse: true
  legacy_edge_aliases:
  - column_belongs_to_table
  edge_class: canonical
  canonical_cognee_edge: true
```
```yaml
candidate_edge:
  edge_id: edge.target_plus.00214.has_column
  canonical_edge_type: HAS_COLUMN
  source_card_id: table.zs_observe.target_sales
  target_card_id: column.zs_observe.target_sales.is_duplicated
  source_type: table
  target_type: column
  inverse_edge_type: BELONGS_TO_TABLE
  materialize_inverse: true
  legacy_edge_aliases: []
  edge_class: canonical
  canonical_cognee_edge: true
```
```yaml
candidate_edge:
  edge_id: edge.target_plus.00215.belongs_to_table
  canonical_edge_type: BELONGS_TO_TABLE
  source_card_id: column.zs_observe.target_sales.zen_status
  target_card_id: table.zs_observe.target_sales
  source_type: column
  target_type: table
  inverse_edge_type: HAS_COLUMN
  materialize_inverse: true
  legacy_edge_aliases:
  - column_belongs_to_table
  edge_class: canonical
  canonical_cognee_edge: true
```
```yaml
candidate_edge:
  edge_id: edge.target_plus.00216.has_column
  canonical_edge_type: HAS_COLUMN
  source_card_id: table.zs_observe.target_sales
  target_card_id: column.zs_observe.target_sales.zen_status
  source_type: table
  target_type: column
  inverse_edge_type: BELONGS_TO_TABLE
  materialize_inverse: true
  legacy_edge_aliases: []
  edge_class: canonical
  canonical_cognee_edge: true
```
```yaml
candidate_edge:
  edge_id: edge.target_plus.00217.belongs_to_table
  canonical_edge_type: BELONGS_TO_TABLE
  source_card_id: column.zs_observe.target_sales.zen_sheet_name
  target_card_id: table.zs_observe.target_sales
  source_type: column
  target_type: table
  inverse_edge_type: HAS_COLUMN
  materialize_inverse: true
  legacy_edge_aliases:
  - column_belongs_to_table
  edge_class: canonical
  canonical_cognee_edge: true
```
```yaml
candidate_edge:
  edge_id: edge.target_plus.00218.has_column
  canonical_edge_type: HAS_COLUMN
  source_card_id: table.zs_observe.target_sales
  target_card_id: column.zs_observe.target_sales.zen_sheet_name
  source_type: table
  target_type: column
  inverse_edge_type: BELONGS_TO_TABLE
  materialize_inverse: true
  legacy_edge_aliases: []
  edge_class: canonical
  canonical_cognee_edge: true
```
```yaml
candidate_edge:
  edge_id: edge.target_plus.00219.belongs_to_table
  canonical_edge_type: BELONGS_TO_TABLE
  source_card_id: column.zs_observe.target_sales.created_at
  target_card_id: table.zs_observe.target_sales
  source_type: column
  target_type: table
  inverse_edge_type: HAS_COLUMN
  materialize_inverse: true
  legacy_edge_aliases:
  - column_belongs_to_table
  edge_class: canonical
  canonical_cognee_edge: true
```
```yaml
candidate_edge:
  edge_id: edge.target_plus.00220.has_column
  canonical_edge_type: HAS_COLUMN
  source_card_id: table.zs_observe.target_sales
  target_card_id: column.zs_observe.target_sales.created_at
  source_type: table
  target_type: column
  inverse_edge_type: BELONGS_TO_TABLE
  materialize_inverse: true
  legacy_edge_aliases: []
  edge_class: canonical
  canonical_cognee_edge: true
```
```yaml
candidate_edge:
  edge_id: edge.target_plus.00221.belongs_to_table
  canonical_edge_type: BELONGS_TO_TABLE
  source_card_id: column.zs_observe.target_sales.updated_at
  target_card_id: table.zs_observe.target_sales
  source_type: column
  target_type: table
  inverse_edge_type: HAS_COLUMN
  materialize_inverse: true
  legacy_edge_aliases:
  - column_belongs_to_table
  edge_class: canonical
  canonical_cognee_edge: true
```
```yaml
candidate_edge:
  edge_id: edge.target_plus.00222.has_column
  canonical_edge_type: HAS_COLUMN
  source_card_id: table.zs_observe.target_sales
  target_card_id: column.zs_observe.target_sales.updated_at
  source_type: table
  target_type: column
  inverse_edge_type: BELONGS_TO_TABLE
  materialize_inverse: true
  legacy_edge_aliases: []
  edge_class: canonical
  canonical_cognee_edge: true
```
```yaml
candidate_edge:
  edge_id: edge.target_plus.00223.belongs_to_table
  canonical_edge_type: BELONGS_TO_TABLE
  source_card_id: column.zs_observe.target_sales.deleted_at
  target_card_id: table.zs_observe.target_sales
  source_type: column
  target_type: table
  inverse_edge_type: HAS_COLUMN
  materialize_inverse: true
  legacy_edge_aliases:
  - column_belongs_to_table
  edge_class: canonical
  canonical_cognee_edge: true
```
```yaml
candidate_edge:
  edge_id: edge.target_plus.00224.has_column
  canonical_edge_type: HAS_COLUMN
  source_card_id: table.zs_observe.target_sales
  target_card_id: column.zs_observe.target_sales.deleted_at
  source_type: table
  target_type: column
  inverse_edge_type: BELONGS_TO_TABLE
  materialize_inverse: true
  legacy_edge_aliases: []
  edge_class: canonical
  canonical_cognee_edge: true
```
```yaml
candidate_edge:
  edge_id: edge.target_plus.00225.source_table
  canonical_edge_type: SOURCE_TABLE
  source_card_id: relationship.target_plus.sales_settlement.item_id
  target_card_id: table.zs_observe.target_sales
  source_type: relationship
  target_type: table
  inverse_edge_type: null
  materialize_inverse: false
  legacy_edge_aliases: []
  edge_class: canonical
  canonical_cognee_edge: true
```
```yaml
candidate_edge:
  edge_id: edge.target_plus.00226.target_table
  canonical_edge_type: TARGET_TABLE
  source_card_id: relationship.target_plus.sales_settlement.item_id
  target_card_id: table.zs_observe.target_settlement
  source_type: relationship
  target_type: table
  inverse_edge_type: null
  materialize_inverse: false
  legacy_edge_aliases: []
  edge_class: canonical
  canonical_cognee_edge: true
```
```yaml
candidate_edge:
  edge_id: edge.target_plus.00227.uses_source_column
  canonical_edge_type: USES_SOURCE_COLUMN
  source_card_id: relationship.target_plus.sales_settlement.item_id
  target_card_id: column.zs_observe.target_sales.item_id
  source_type: relationship
  target_type: column
  inverse_edge_type: null
  materialize_inverse: false
  legacy_edge_aliases: []
  edge_class: canonical
  canonical_cognee_edge: true
```
```yaml
candidate_edge:
  edge_id: edge.target_plus.00228.uses_target_column
  canonical_edge_type: USES_TARGET_COLUMN
  source_card_id: relationship.target_plus.sales_settlement.item_id
  target_card_id: column.zs_observe.target_settlement.item_id
  source_type: relationship
  target_type: column
  inverse_edge_type: null
  materialize_inverse: false
  legacy_edge_aliases: []
  edge_class: canonical
  canonical_cognee_edge: true
```
```yaml
candidate_edge:
  edge_id: edge.target_plus.00229.source_table
  canonical_edge_type: SOURCE_TABLE
  source_card_id: relationship.target_plus.sales_returns.order_id
  target_card_id: table.zs_observe.target_sales
  source_type: relationship
  target_type: table
  inverse_edge_type: null
  materialize_inverse: false
  legacy_edge_aliases: []
  edge_class: canonical
  canonical_cognee_edge: true
```
```yaml
candidate_edge:
  edge_id: edge.target_plus.00230.target_table
  canonical_edge_type: TARGET_TABLE
  source_card_id: relationship.target_plus.sales_returns.order_id
  target_card_id: table.zs_observe.target_returns
  source_type: relationship
  target_type: table
  inverse_edge_type: null
  materialize_inverse: false
  legacy_edge_aliases: []
  edge_class: canonical
  canonical_cognee_edge: true
```
```yaml
candidate_edge:
  edge_id: edge.target_plus.00231.uses_source_column
  canonical_edge_type: USES_SOURCE_COLUMN
  source_card_id: relationship.target_plus.sales_returns.order_id
  target_card_id: column.zs_observe.target_sales.order_id
  source_type: relationship
  target_type: column
  inverse_edge_type: null
  materialize_inverse: false
  legacy_edge_aliases: []
  edge_class: canonical
  canonical_cognee_edge: true
```
```yaml
candidate_edge:
  edge_id: edge.target_plus.00232.uses_target_column
  canonical_edge_type: USES_TARGET_COLUMN
  source_card_id: relationship.target_plus.sales_returns.order_id
  target_card_id: column.zs_observe.target_returns.order_id
  source_type: relationship
  target_type: column
  inverse_edge_type: null
  materialize_inverse: false
  legacy_edge_aliases: []
  edge_class: canonical
  canonical_cognee_edge: true
```
```yaml
candidate_edge:
  edge_id: edge.target_plus.00233.source_table
  canonical_edge_type: SOURCE_TABLE
  source_card_id: relationship.target_plus.returns_settlement.item_id
  target_card_id: table.zs_observe.target_returns
  source_type: relationship
  target_type: table
  inverse_edge_type: null
  materialize_inverse: false
  legacy_edge_aliases: []
  edge_class: canonical
  canonical_cognee_edge: true
```
```yaml
candidate_edge:
  edge_id: edge.target_plus.00234.target_table
  canonical_edge_type: TARGET_TABLE
  source_card_id: relationship.target_plus.returns_settlement.item_id
  target_card_id: table.zs_observe.target_settlement
  source_type: relationship
  target_type: table
  inverse_edge_type: null
  materialize_inverse: false
  legacy_edge_aliases: []
  edge_class: canonical
  canonical_cognee_edge: true
```
```yaml
candidate_edge:
  edge_id: edge.target_plus.00235.uses_source_column
  canonical_edge_type: USES_SOURCE_COLUMN
  source_card_id: relationship.target_plus.returns_settlement.item_id
  target_card_id: column.zs_observe.target_returns.item_id
  source_type: relationship
  target_type: column
  inverse_edge_type: null
  materialize_inverse: false
  legacy_edge_aliases: []
  edge_class: canonical
  canonical_cognee_edge: true
```
```yaml
candidate_edge:
  edge_id: edge.target_plus.00236.uses_target_column
  canonical_edge_type: USES_TARGET_COLUMN
  source_card_id: relationship.target_plus.returns_settlement.item_id
  target_card_id: column.zs_observe.target_settlement.item_id
  source_type: relationship
  target_type: column
  inverse_edge_type: null
  materialize_inverse: false
  legacy_edge_aliases: []
  edge_class: canonical
  canonical_cognee_edge: true
```
```yaml
candidate_edge:
  edge_id: edge.target_plus.00237.source_table
  canonical_edge_type: SOURCE_TABLE
  source_card_id: relationship.target_plus.sales_mapping.tcin
  target_card_id: table.zs_observe.target_sales
  source_type: relationship
  target_type: table
  inverse_edge_type: null
  materialize_inverse: false
  legacy_edge_aliases: []
  edge_class: canonical
  canonical_cognee_edge: true
```
```yaml
candidate_edge:
  edge_id: edge.target_plus.00238.target_table
  canonical_edge_type: TARGET_TABLE
  source_card_id: relationship.target_plus.sales_mapping.tcin
  target_card_id: table.zs_observe.target_tcin_mapping
  source_type: relationship
  target_type: table
  inverse_edge_type: null
  materialize_inverse: false
  legacy_edge_aliases: []
  edge_class: canonical
  canonical_cognee_edge: true
```
```yaml
candidate_edge:
  edge_id: edge.target_plus.00239.uses_source_column
  canonical_edge_type: USES_SOURCE_COLUMN
  source_card_id: relationship.target_plus.sales_mapping.tcin
  target_card_id: column.zs_observe.target_sales.tcin
  source_type: relationship
  target_type: column
  inverse_edge_type: null
  materialize_inverse: false
  legacy_edge_aliases: []
  edge_class: canonical
  canonical_cognee_edge: true
```
```yaml
candidate_edge:
  edge_id: edge.target_plus.00240.uses_target_column
  canonical_edge_type: USES_TARGET_COLUMN
  source_card_id: relationship.target_plus.sales_mapping.tcin
  target_card_id: column.zs_observe.target_tcin_mapping.tcin
  source_type: relationship
  target_type: column
  inverse_edge_type: null
  materialize_inverse: false
  legacy_edge_aliases: []
  edge_class: canonical
  canonical_cognee_edge: true
```
```yaml
candidate_edge:
  edge_id: edge.target_plus.00241.source_table
  canonical_edge_type: SOURCE_TABLE
  source_card_id: relationship.target_plus.settlement_mapping.tcin
  target_card_id: table.zs_observe.target_settlement
  source_type: relationship
  target_type: table
  inverse_edge_type: null
  materialize_inverse: false
  legacy_edge_aliases: []
  edge_class: canonical
  canonical_cognee_edge: true
```
```yaml
candidate_edge:
  edge_id: edge.target_plus.00242.target_table
  canonical_edge_type: TARGET_TABLE
  source_card_id: relationship.target_plus.settlement_mapping.tcin
  target_card_id: table.zs_observe.target_tcin_mapping
  source_type: relationship
  target_type: table
  inverse_edge_type: null
  materialize_inverse: false
  legacy_edge_aliases: []
  edge_class: canonical
  canonical_cognee_edge: true
```
```yaml
candidate_edge:
  edge_id: edge.target_plus.00243.uses_source_column
  canonical_edge_type: USES_SOURCE_COLUMN
  source_card_id: relationship.target_plus.settlement_mapping.tcin
  target_card_id: column.zs_observe.target_settlement.tcin
  source_type: relationship
  target_type: column
  inverse_edge_type: null
  materialize_inverse: false
  legacy_edge_aliases: []
  edge_class: canonical
  canonical_cognee_edge: true
```
```yaml
candidate_edge:
  edge_id: edge.target_plus.00244.uses_target_column
  canonical_edge_type: USES_TARGET_COLUMN
  source_card_id: relationship.target_plus.settlement_mapping.tcin
  target_card_id: column.zs_observe.target_tcin_mapping.tcin
  source_type: relationship
  target_type: column
  inverse_edge_type: null
  materialize_inverse: false
  legacy_edge_aliases: []
  edge_class: canonical
  canonical_cognee_edge: true
```
```yaml
candidate_edge:
  edge_id: edge.target_plus.00245.source_table
  canonical_edge_type: SOURCE_TABLE
  source_card_id: relationship.target_plus.returns_mapping.tcin
  target_card_id: table.zs_observe.target_returns
  source_type: relationship
  target_type: table
  inverse_edge_type: null
  materialize_inverse: false
  legacy_edge_aliases: []
  edge_class: canonical
  canonical_cognee_edge: true
```
```yaml
candidate_edge:
  edge_id: edge.target_plus.00246.target_table
  canonical_edge_type: TARGET_TABLE
  source_card_id: relationship.target_plus.returns_mapping.tcin
  target_card_id: table.zs_observe.target_tcin_mapping
  source_type: relationship
  target_type: table
  inverse_edge_type: null
  materialize_inverse: false
  legacy_edge_aliases: []
  edge_class: canonical
  canonical_cognee_edge: true
```
```yaml
candidate_edge:
  edge_id: edge.target_plus.00247.uses_source_column
  canonical_edge_type: USES_SOURCE_COLUMN
  source_card_id: relationship.target_plus.returns_mapping.tcin
  target_card_id: column.zs_observe.target_returns.tcin
  source_type: relationship
  target_type: column
  inverse_edge_type: null
  materialize_inverse: false
  legacy_edge_aliases: []
  edge_class: canonical
  canonical_cognee_edge: true
```
```yaml
candidate_edge:
  edge_id: edge.target_plus.00248.uses_target_column
  canonical_edge_type: USES_TARGET_COLUMN
  source_card_id: relationship.target_plus.returns_mapping.tcin
  target_card_id: column.zs_observe.target_tcin_mapping.tcin
  source_type: relationship
  target_type: column
  inverse_edge_type: null
  materialize_inverse: false
  legacy_edge_aliases: []
  edge_class: canonical
  canonical_cognee_edge: true
```
```yaml
candidate_edge:
  edge_id: edge.target_plus.00249.profiles_column
  canonical_edge_type: PROFILES_COLUMN
  source_card_id: value_profile.target_plus.scope.group_level_id_123
  target_card_id: column.zs_observe.target_sales.group_level_id
  source_type: value_profile
  target_type: column
  inverse_edge_type: HAS_VALUE_PROFILE
  materialize_inverse: true
  legacy_edge_aliases:
  - value_profile_describes_column
  edge_class: canonical
  canonical_cognee_edge: true
```
```yaml
candidate_edge:
  edge_id: edge.target_plus.00250.profiles_table
  canonical_edge_type: PROFILES_TABLE
  source_card_id: value_profile.target_plus.brand_profiles
  target_card_id: table.zs_observe.target_tcin_mapping
  source_type: value_profile
  target_type: table
  inverse_edge_type: HAS_VALUE_PROFILE
  materialize_inverse: true
  legacy_edge_aliases: []
  edge_class: canonical
  canonical_cognee_edge: true
```
```yaml
candidate_edge:
  edge_id: edge.target_plus.00251.profiles_column
  canonical_edge_type: PROFILES_COLUMN
  source_card_id: value_profile.target_plus.mapping.brand_case
  target_card_id: column.zs_observe.target_tcin_mapping.brand
  source_type: value_profile
  target_type: column
  inverse_edge_type: HAS_VALUE_PROFILE
  materialize_inverse: true
  legacy_edge_aliases:
  - value_profile_describes_column
  edge_class: canonical
  canonical_cognee_edge: true
```
```yaml
candidate_edge:
  edge_id: edge.target_plus.00252.profiles_column
  canonical_edge_type: PROFILES_COLUMN
  source_card_id: value_profile.target_plus.sales.order_status
  target_card_id: column.zs_observe.target_sales.order_status
  source_type: value_profile
  target_type: column
  inverse_edge_type: HAS_VALUE_PROFILE
  materialize_inverse: true
  legacy_edge_aliases:
  - value_profile_describes_column
  edge_class: canonical
  canonical_cognee_edge: true
```
```yaml
candidate_edge:
  edge_id: edge.target_plus.00253.profiles_column
  canonical_edge_type: PROFILES_COLUMN
  source_card_id: value_profile.target_plus.sales.brand_distribution
  target_card_id: column.zs_observe.target_sales.brand
  source_type: value_profile
  target_type: column
  inverse_edge_type: HAS_VALUE_PROFILE
  materialize_inverse: true
  legacy_edge_aliases:
  - value_profile_describes_column
  edge_class: canonical
  canonical_cognee_edge: true
```
```yaml
candidate_edge:
  edge_id: edge.target_plus.00254.profiles_column
  canonical_edge_type: PROFILES_COLUMN
  source_card_id: value_profile.target_plus.sales.order_id_format
  target_card_id: column.zs_observe.target_sales.order_id
  source_type: value_profile
  target_type: column
  inverse_edge_type: HAS_VALUE_PROFILE
  materialize_inverse: true
  legacy_edge_aliases:
  - value_profile_describes_column
  edge_class: canonical
  canonical_cognee_edge: true
```
```yaml
candidate_edge:
  edge_id: edge.target_plus.00255.profiles_column
  canonical_edge_type: PROFILES_COLUMN
  source_card_id: value_profile.target_plus.sales.item_id_format
  target_card_id: column.zs_observe.target_sales.item_id
  source_type: value_profile
  target_type: column
  inverse_edge_type: HAS_VALUE_PROFILE
  materialize_inverse: true
  legacy_edge_aliases:
  - value_profile_describes_column
  edge_class: canonical
  canonical_cognee_edge: true
```
```yaml
candidate_edge:
  edge_id: edge.target_plus.00256.profiles_column
  canonical_edge_type: PROFILES_COLUMN
  source_card_id: value_profile.target_plus.sales.sku_id_format
  target_card_id: column.zs_observe.target_sales.sku_id
  source_type: value_profile
  target_type: column
  inverse_edge_type: HAS_VALUE_PROFILE
  materialize_inverse: true
  legacy_edge_aliases:
  - value_profile_describes_column
  edge_class: canonical
  canonical_cognee_edge: true
```
```yaml
candidate_edge:
  edge_id: edge.target_plus.00257.profiles_column
  canonical_edge_type: PROFILES_COLUMN
  source_card_id: value_profile.target_plus.sales.tcin_format
  target_card_id: column.zs_observe.target_sales.tcin
  source_type: value_profile
  target_type: column
  inverse_edge_type: HAS_VALUE_PROFILE
  materialize_inverse: true
  legacy_edge_aliases:
  - value_profile_describes_column
  edge_class: canonical
  canonical_cognee_edge: true
```
```yaml
candidate_edge:
  edge_id: edge.target_plus.00258.profiles_column
  canonical_edge_type: PROFILES_COLUMN
  source_card_id: value_profile.target_plus.returns.internal_txn_type
  target_card_id: column.zs_observe.target_returns.internal_txn_type
  source_type: value_profile
  target_type: column
  inverse_edge_type: HAS_VALUE_PROFILE
  materialize_inverse: true
  legacy_edge_aliases:
  - value_profile_describes_column
  edge_class: canonical
  canonical_cognee_edge: true
```
```yaml
candidate_edge:
  edge_id: edge.target_plus.00259.profiles_column
  canonical_edge_type: PROFILES_COLUMN
  source_card_id: value_profile.target_plus.returns.order_status
  target_card_id: column.zs_observe.target_returns.order_status
  source_type: value_profile
  target_type: column
  inverse_edge_type: HAS_VALUE_PROFILE
  materialize_inverse: true
  legacy_edge_aliases:
  - value_profile_describes_column
  edge_class: canonical
  canonical_cognee_edge: true
```
```yaml
candidate_edge:
  edge_id: edge.target_plus.00260.profiles_column
  canonical_edge_type: PROFILES_COLUMN
  source_card_id: value_profile.target_plus.returns.reasons
  target_card_id: column.zs_observe.target_returns.description
  source_type: value_profile
  target_type: column
  inverse_edge_type: HAS_VALUE_PROFILE
  materialize_inverse: true
  legacy_edge_aliases:
  - value_profile_describes_column
  edge_class: canonical
  canonical_cognee_edge: true
```
```yaml
candidate_edge:
  edge_id: edge.target_plus.00261.profiles_column
  canonical_edge_type: PROFILES_COLUMN
  source_card_id: value_profile.target_plus.returns.carrier_tracking
  target_card_id: column.zs_observe.target_returns.other_id
  source_type: value_profile
  target_type: column
  inverse_edge_type: HAS_VALUE_PROFILE
  materialize_inverse: true
  legacy_edge_aliases:
  - value_profile_describes_column
  edge_class: canonical
  canonical_cognee_edge: true
```
```yaml
candidate_edge:
  edge_id: edge.target_plus.00262.profiles_column
  canonical_edge_type: PROFILES_COLUMN
  source_card_id: value_profile.target_plus.settlement.transaction_breakdown
  target_card_id: column.zs_observe.target_settlement.transaction_type
  source_type: value_profile
  target_type: column
  inverse_edge_type: HAS_VALUE_PROFILE
  materialize_inverse: true
  legacy_edge_aliases:
  - value_profile_describes_column
  edge_class: canonical
  canonical_cognee_edge: true
```
```yaml
candidate_edge:
  edge_id: edge.target_plus.00263.profiles_column
  canonical_edge_type: PROFILES_COLUMN
  source_card_id: value_profile.target_plus.settlement.total_tax_zero
  target_card_id: column.zs_observe.target_settlement.total_tax
  source_type: value_profile
  target_type: column
  inverse_edge_type: HAS_VALUE_PROFILE
  materialize_inverse: true
  legacy_edge_aliases:
  - value_profile_describes_column
  edge_class: canonical
  canonical_cognee_edge: true
```
```yaml
candidate_edge:
  edge_id: edge.target_plus.00264.profiles_column
  canonical_edge_type: PROFILES_COLUMN
  source_card_id: value_profile.target_plus.settlement.commission_rate
  target_card_id: column.zs_observe.target_settlement.gross_commission_percentage
  source_type: value_profile
  target_type: column
  inverse_edge_type: HAS_VALUE_PROFILE
  materialize_inverse: true
  legacy_edge_aliases:
  - value_profile_describes_column
  edge_class: canonical
  canonical_cognee_edge: true
```
```yaml
candidate_edge:
  edge_id: edge.target_plus.00265.profiles_column
  canonical_edge_type: PROFILES_COLUMN
  source_card_id: value_profile.target_plus.settlement.payout_batches
  target_card_id: column.zs_observe.target_settlement.payout_id
  source_type: value_profile
  target_type: column
  inverse_edge_type: HAS_VALUE_PROFILE
  materialize_inverse: true
  legacy_edge_aliases:
  - value_profile_describes_column
  edge_class: canonical
  canonical_cognee_edge: true
```
```yaml
candidate_edge:
  edge_id: edge.target_plus.00266.profiles_table
  canonical_edge_type: PROFILES_TABLE
  source_card_id: value_profile.target_plus.settlement.stripe_id_formats
  target_card_id: table.zs_observe.target_settlement
  source_type: value_profile
  target_type: table
  inverse_edge_type: HAS_VALUE_PROFILE
  materialize_inverse: true
  legacy_edge_aliases: []
  edge_class: canonical
  canonical_cognee_edge: true
```
```yaml
candidate_edge:
  edge_id: edge.target_plus.00267.profiles_column
  canonical_edge_type: PROFILES_COLUMN
  source_card_id: value_profile.target_plus.mapping.sku_naming
  target_card_id: column.zs_observe.target_tcin_mapping.sku_id
  source_type: value_profile
  target_type: column
  inverse_edge_type: HAS_VALUE_PROFILE
  materialize_inverse: true
  legacy_edge_aliases:
  - value_profile_describes_column
  edge_class: canonical
  canonical_cognee_edge: true
```
```yaml
candidate_edge:
  edge_id: edge.target_plus.00268.profiles_column
  canonical_edge_type: PROFILES_COLUMN
  source_card_id: value_profile.target_plus.mapping.barcode_coverage
  target_card_id: column.zs_observe.target_tcin_mapping.barcode
  source_type: value_profile
  target_type: column
  inverse_edge_type: HAS_VALUE_PROFILE
  materialize_inverse: true
  legacy_edge_aliases:
  - value_profile_describes_column
  edge_class: canonical
  canonical_cognee_edge: true
```
```yaml
candidate_edge:
  edge_id: edge.target_plus.00269.profiles_column
  canonical_edge_type: PROFILES_COLUMN
  source_card_id: value_profile.target_plus.mapping.asin_cross_reference
  target_card_id: column.zs_observe.target_tcin_mapping.asin
  source_type: value_profile
  target_type: column
  inverse_edge_type: HAS_VALUE_PROFILE
  materialize_inverse: true
  legacy_edge_aliases:
  - value_profile_describes_column
  edge_class: canonical
  canonical_cognee_edge: true
```
```yaml
candidate_edge:
  edge_id: edge.target_plus.00270.profiles_table
  canonical_edge_type: PROFILES_TABLE
  source_card_id: value_profile.target_plus.currency.label_values
  target_card_id: table.zs_observe.target_settlement
  source_type: value_profile
  target_type: table
  inverse_edge_type: HAS_VALUE_PROFILE
  materialize_inverse: true
  legacy_edge_aliases: []
  edge_class: canonical
  canonical_cognee_edge: true
```
```yaml
candidate_edge:
  edge_id: edge.target_plus.00271.belongs_to_domain
  canonical_edge_type: BELONGS_TO_DOMAIN
  source_card_id: metric.target_plus.total_gmv
  target_card_id: domain.target_plus.orders
  source_type: metric
  target_type: domain
  inverse_edge_type: null
  materialize_inverse: false
  legacy_edge_aliases: []
  edge_class: canonical
  canonical_cognee_edge: true
```
```yaml
candidate_edge:
  edge_id: edge.target_plus.00272.belongs_to_domain
  canonical_edge_type: BELONGS_TO_DOMAIN
  source_card_id: metric.target_plus.net_settlement_revenue
  target_card_id: domain.target_plus.settlement
  source_type: metric
  target_type: domain
  inverse_edge_type: null
  materialize_inverse: false
  legacy_edge_aliases: []
  edge_class: canonical
  canonical_cognee_edge: true
```
```yaml
candidate_edge:
  edge_id: edge.target_plus.00273.belongs_to_domain
  canonical_edge_type: BELONGS_TO_DOMAIN
  source_card_id: metric.target_plus.return_rate
  target_card_id: domain.target_plus.returns
  source_type: metric
  target_type: domain
  inverse_edge_type: null
  materialize_inverse: false
  legacy_edge_aliases: []
  edge_class: canonical
  canonical_cognee_edge: true
```
```yaml
candidate_edge:
  edge_id: edge.target_plus.00274.belongs_to_domain
  canonical_edge_type: BELONGS_TO_DOMAIN
  source_card_id: metric.target_plus.aov
  target_card_id: domain.target_plus.orders
  source_type: metric
  target_type: domain
  inverse_edge_type: null
  materialize_inverse: false
  legacy_edge_aliases: []
  edge_class: canonical
  canonical_cognee_edge: true
```
```yaml
candidate_edge:
  edge_id: edge.target_plus.00275.belongs_to_domain
  canonical_edge_type: BELONGS_TO_DOMAIN
  source_card_id: metric.target_plus.effective_payout_rate
  target_card_id: domain.target_plus.settlement
  source_type: metric
  target_type: domain
  inverse_edge_type: null
  materialize_inverse: false
  legacy_edge_aliases: []
  edge_class: canonical
  canonical_cognee_edge: true
```
```yaml
candidate_edge:
  edge_id: edge.target_plus.00276.belongs_to_domain
  canonical_edge_type: BELONGS_TO_DOMAIN
  source_card_id: metric.target_plus.top_selling_skus
  target_card_id: domain.target_plus.mapping_enrichment
  source_type: metric
  target_type: domain
  inverse_edge_type: null
  materialize_inverse: false
  legacy_edge_aliases: []
  edge_class: canonical
  canonical_cognee_edge: true
```
```yaml
candidate_edge:
  edge_id: edge.target_plus.00277.belongs_to_domain
  canonical_edge_type: BELONGS_TO_DOMAIN
  source_card_id: metric.target_plus.cancellation_rate
  target_card_id: domain.target_plus.orders
  source_type: metric
  target_type: domain
  inverse_edge_type: null
  materialize_inverse: false
  legacy_edge_aliases: []
  edge_class: canonical
  canonical_cognee_edge: true
```
```yaml
candidate_edge:
  edge_id: edge.target_plus.00278.belongs_to_domain
  canonical_edge_type: BELONGS_TO_DOMAIN
  source_card_id: metric.target_plus.commission_validation_variance
  target_card_id: domain.target_plus.fees
  source_type: metric
  target_type: domain
  inverse_edge_type: null
  materialize_inverse: false
  legacy_edge_aliases: []
  edge_class: canonical
  canonical_cognee_edge: true
```
```yaml
candidate_edge:
  edge_id: edge.target_plus.00279.belongs_to_domain
  canonical_edge_type: BELONGS_TO_DOMAIN
  source_card_id: metric.target_plus.payout_batch_total
  target_card_id: domain.target_plus.payment
  source_type: metric
  target_type: domain
  inverse_edge_type: null
  materialize_inverse: false
  legacy_edge_aliases: []
  edge_class: canonical
  canonical_cognee_edge: true
```
```yaml
candidate_edge:
  edge_id: edge.target_plus.00280.belongs_to_domain
  canonical_edge_type: BELONGS_TO_DOMAIN
  source_card_id: metric.target_plus.return_reason_value
  target_card_id: domain.target_plus.returns
  source_type: metric
  target_type: domain
  inverse_edge_type: null
  materialize_inverse: false
  legacy_edge_aliases: []
  edge_class: canonical
  canonical_cognee_edge: true
```
```yaml
candidate_edge:
  edge_id: edge.target_plus.00281.belongs_to_domain
  canonical_edge_type: BELONGS_TO_DOMAIN
  source_card_id: metric.target_plus.brand_return_rate
  target_card_id: domain.target_plus.returns
  source_type: metric
  target_type: domain
  inverse_edge_type: null
  materialize_inverse: false
  legacy_edge_aliases: []
  edge_class: canonical
  canonical_cognee_edge: true
```
```yaml
candidate_edge:
  edge_id: edge.target_plus.00282.belongs_to_domain
  canonical_edge_type: BELONGS_TO_DOMAIN
  source_card_id: metric.target_plus.monthly_sales_gmv
  target_card_id: domain.target_plus.orders
  source_type: metric
  target_type: domain
  inverse_edge_type: null
  materialize_inverse: false
  legacy_edge_aliases: []
  edge_class: canonical
  canonical_cognee_edge: true
```
```yaml
candidate_edge:
  edge_id: edge.target_plus.00283.belongs_to_domain
  canonical_edge_type: BELONGS_TO_DOMAIN
  source_card_id: metric.target_plus.mapping_sales_coverage
  target_card_id: domain.target_plus.mapping_enrichment
  source_type: metric
  target_type: domain
  inverse_edge_type: null
  materialize_inverse: false
  legacy_edge_aliases: []
  edge_class: canonical
  canonical_cognee_edge: true
```
```yaml
candidate_edge:
  edge_id: edge.target_plus.00284.uses_formula_template
  canonical_edge_type: USES_FORMULA_TEMPLATE
  source_card_id: metric_impl.target_plus.effective_payout_rate
  target_card_id: formula_template.target_plus.forward_payout_waterfall
  source_type: metric_implementation
  target_type: formula_template
  inverse_edge_type: null
  materialize_inverse: false
  legacy_edge_aliases: []
  edge_class: canonical
  canonical_cognee_edge: true
```
```yaml
candidate_edge:
  edge_id: edge.target_plus.00285.uses_formula_template
  canonical_edge_type: USES_FORMULA_TEMPLATE
  source_card_id: metric_impl.target_plus.net_settlement_revenue
  target_card_id: formula_template.target_plus.return_refund_netting
  source_type: metric_implementation
  target_type: formula_template
  inverse_edge_type: null
  materialize_inverse: false
  legacy_edge_aliases: []
  edge_class: canonical
  canonical_cognee_edge: true
```
```yaml
candidate_edge:
  edge_id: edge.target_plus.00286.applies_to_platform_context
  canonical_edge_type: APPLIES_TO_PLATFORM_CONTEXT
  source_card_id: formula_template.target_plus.reverse_charge_tax_adjustment
  target_card_id: platform_context.target_plus.us
  source_type: formula_template
  target_type: platform_context
  inverse_edge_type: null
  materialize_inverse: false
  legacy_edge_aliases: []
  edge_class: canonical
  canonical_cognee_edge: true
```
```yaml
candidate_edge:
  edge_id: edge.target_plus.00287.implements_metric
  canonical_edge_type: IMPLEMENTS_METRIC
  source_card_id: metric_impl.target_plus.total_gmv
  target_card_id: metric.target_plus.total_gmv
  source_type: metric_implementation
  target_type: metric
  inverse_edge_type: HAS_IMPLEMENTATION
  materialize_inverse: true
  legacy_edge_aliases:
  - implements_metric
  edge_class: canonical
  canonical_cognee_edge: true
```
```yaml
candidate_edge:
  edge_id: edge.target_plus.00288.has_implementation
  canonical_edge_type: HAS_IMPLEMENTATION
  source_card_id: metric.target_plus.total_gmv
  target_card_id: metric_impl.target_plus.total_gmv
  source_type: metric
  target_type: metric_implementation
  inverse_edge_type: IMPLEMENTS_METRIC
  materialize_inverse: true
  legacy_edge_aliases: []
  edge_class: canonical
  canonical_cognee_edge: true
```
```yaml
candidate_edge:
  edge_id: edge.target_plus.00289.uses_table
  canonical_edge_type: USES_TABLE
  source_card_id: metric_impl.target_plus.total_gmv
  target_card_id: table.zs_observe.target_sales
  source_type: metric_implementation
  target_type: table
  inverse_edge_type: null
  materialize_inverse: false
  legacy_edge_aliases:
  - implementation_uses_table
  edge_class: canonical
  canonical_cognee_edge: true
```
```yaml
candidate_edge:
  edge_id: edge.target_plus.00290.uses_column
  canonical_edge_type: USES_COLUMN
  source_card_id: metric_impl.target_plus.total_gmv
  target_card_id: column.zs_observe.target_sales.charged_amount
  source_type: metric_implementation
  target_type: column
  inverse_edge_type: null
  materialize_inverse: false
  legacy_edge_aliases:
  - implementation_uses_column
  edge_class: canonical
  canonical_cognee_edge: true
```
```yaml
candidate_edge:
  edge_id: edge.target_plus.00291.uses_column
  canonical_edge_type: USES_COLUMN
  source_card_id: metric_impl.target_plus.total_gmv
  target_card_id: column.zs_observe.target_sales.discount_amount
  source_type: metric_implementation
  target_type: column
  inverse_edge_type: null
  materialize_inverse: false
  legacy_edge_aliases:
  - implementation_uses_column
  edge_class: canonical
  canonical_cognee_edge: true
```
```yaml
candidate_edge:
  edge_id: edge.target_plus.00292.implements_metric
  canonical_edge_type: IMPLEMENTS_METRIC
  source_card_id: metric_impl.target_plus.net_settlement_revenue
  target_card_id: metric.target_plus.net_settlement_revenue
  source_type: metric_implementation
  target_type: metric
  inverse_edge_type: HAS_IMPLEMENTATION
  materialize_inverse: true
  legacy_edge_aliases:
  - implements_metric
  edge_class: canonical
  canonical_cognee_edge: true
```
```yaml
candidate_edge:
  edge_id: edge.target_plus.00293.has_implementation
  canonical_edge_type: HAS_IMPLEMENTATION
  source_card_id: metric.target_plus.net_settlement_revenue
  target_card_id: metric_impl.target_plus.net_settlement_revenue
  source_type: metric
  target_type: metric_implementation
  inverse_edge_type: IMPLEMENTS_METRIC
  materialize_inverse: true
  legacy_edge_aliases: []
  edge_class: canonical
  canonical_cognee_edge: true
```
```yaml
candidate_edge:
  edge_id: edge.target_plus.00294.uses_table
  canonical_edge_type: USES_TABLE
  source_card_id: metric_impl.target_plus.net_settlement_revenue
  target_card_id: table.zs_observe.target_settlement
  source_type: metric_implementation
  target_type: table
  inverse_edge_type: null
  materialize_inverse: false
  legacy_edge_aliases:
  - implementation_uses_table
  edge_class: canonical
  canonical_cognee_edge: true
```
```yaml
candidate_edge:
  edge_id: edge.target_plus.00295.uses_column
  canonical_edge_type: USES_COLUMN
  source_card_id: metric_impl.target_plus.net_settlement_revenue
  target_card_id: column.zs_observe.target_settlement.transaction_type
  source_type: metric_implementation
  target_type: column
  inverse_edge_type: null
  materialize_inverse: false
  legacy_edge_aliases:
  - implementation_uses_column
  edge_class: canonical
  canonical_cognee_edge: true
```
```yaml
candidate_edge:
  edge_id: edge.target_plus.00296.uses_column
  canonical_edge_type: USES_COLUMN
  source_card_id: metric_impl.target_plus.net_settlement_revenue
  target_card_id: column.zs_observe.target_settlement.settled_amount
  source_type: metric_implementation
  target_type: column
  inverse_edge_type: null
  materialize_inverse: false
  legacy_edge_aliases:
  - implementation_uses_column
  edge_class: canonical
  canonical_cognee_edge: true
```
```yaml
candidate_edge:
  edge_id: edge.target_plus.00297.implements_metric
  canonical_edge_type: IMPLEMENTS_METRIC
  source_card_id: metric_impl.target_plus.return_rate
  target_card_id: metric.target_plus.return_rate
  source_type: metric_implementation
  target_type: metric
  inverse_edge_type: HAS_IMPLEMENTATION
  materialize_inverse: true
  legacy_edge_aliases:
  - implements_metric
  edge_class: canonical
  canonical_cognee_edge: true
```
```yaml
candidate_edge:
  edge_id: edge.target_plus.00298.has_implementation
  canonical_edge_type: HAS_IMPLEMENTATION
  source_card_id: metric.target_plus.return_rate
  target_card_id: metric_impl.target_plus.return_rate
  source_type: metric
  target_type: metric_implementation
  inverse_edge_type: IMPLEMENTS_METRIC
  materialize_inverse: true
  legacy_edge_aliases: []
  edge_class: canonical
  canonical_cognee_edge: true
```
```yaml
candidate_edge:
  edge_id: edge.target_plus.00299.uses_table
  canonical_edge_type: USES_TABLE
  source_card_id: metric_impl.target_plus.return_rate
  target_card_id: table.zs_observe.target_sales
  source_type: metric_implementation
  target_type: table
  inverse_edge_type: null
  materialize_inverse: false
  legacy_edge_aliases:
  - implementation_uses_table
  edge_class: canonical
  canonical_cognee_edge: true
```
```yaml
candidate_edge:
  edge_id: edge.target_plus.00300.uses_table
  canonical_edge_type: USES_TABLE
  source_card_id: metric_impl.target_plus.return_rate
  target_card_id: table.zs_observe.target_returns
  source_type: metric_implementation
  target_type: table
  inverse_edge_type: null
  materialize_inverse: false
  legacy_edge_aliases:
  - implementation_uses_table
  edge_class: canonical
  canonical_cognee_edge: true
```
```yaml
candidate_edge:
  edge_id: edge.target_plus.00301.uses_column
  canonical_edge_type: USES_COLUMN
  source_card_id: metric_impl.target_plus.return_rate
  target_card_id: column.zs_observe.target_sales.order_id
  source_type: metric_implementation
  target_type: column
  inverse_edge_type: null
  materialize_inverse: false
  legacy_edge_aliases:
  - implementation_uses_column
  edge_class: canonical
  canonical_cognee_edge: true
```
```yaml
candidate_edge:
  edge_id: edge.target_plus.00302.uses_column
  canonical_edge_type: USES_COLUMN
  source_card_id: metric_impl.target_plus.return_rate
  target_card_id: column.zs_observe.target_returns.order_id
  source_type: metric_implementation
  target_type: column
  inverse_edge_type: null
  materialize_inverse: false
  legacy_edge_aliases:
  - implementation_uses_column
  edge_class: canonical
  canonical_cognee_edge: true
```
```yaml
candidate_edge:
  edge_id: edge.target_plus.00303.implements_metric
  canonical_edge_type: IMPLEMENTS_METRIC
  source_card_id: metric_impl.target_plus.aov
  target_card_id: metric.target_plus.aov
  source_type: metric_implementation
  target_type: metric
  inverse_edge_type: HAS_IMPLEMENTATION
  materialize_inverse: true
  legacy_edge_aliases:
  - implements_metric
  edge_class: canonical
  canonical_cognee_edge: true
```
```yaml
candidate_edge:
  edge_id: edge.target_plus.00304.has_implementation
  canonical_edge_type: HAS_IMPLEMENTATION
  source_card_id: metric.target_plus.aov
  target_card_id: metric_impl.target_plus.aov
  source_type: metric
  target_type: metric_implementation
  inverse_edge_type: IMPLEMENTS_METRIC
  materialize_inverse: true
  legacy_edge_aliases: []
  edge_class: canonical
  canonical_cognee_edge: true
```
```yaml
candidate_edge:
  edge_id: edge.target_plus.00305.uses_table
  canonical_edge_type: USES_TABLE
  source_card_id: metric_impl.target_plus.aov
  target_card_id: table.zs_observe.target_sales
  source_type: metric_implementation
  target_type: table
  inverse_edge_type: null
  materialize_inverse: false
  legacy_edge_aliases:
  - implementation_uses_table
  edge_class: canonical
  canonical_cognee_edge: true
```
```yaml
candidate_edge:
  edge_id: edge.target_plus.00306.uses_column
  canonical_edge_type: USES_COLUMN
  source_card_id: metric_impl.target_plus.aov
  target_card_id: column.zs_observe.target_sales.charged_amount
  source_type: metric_implementation
  target_type: column
  inverse_edge_type: null
  materialize_inverse: false
  legacy_edge_aliases:
  - implementation_uses_column
  edge_class: canonical
  canonical_cognee_edge: true
```
```yaml
candidate_edge:
  edge_id: edge.target_plus.00307.implements_metric
  canonical_edge_type: IMPLEMENTS_METRIC
  source_card_id: metric_impl.target_plus.effective_payout_rate
  target_card_id: metric.target_plus.effective_payout_rate
  source_type: metric_implementation
  target_type: metric
  inverse_edge_type: HAS_IMPLEMENTATION
  materialize_inverse: true
  legacy_edge_aliases:
  - implements_metric
  edge_class: canonical
  canonical_cognee_edge: true
```
```yaml
candidate_edge:
  edge_id: edge.target_plus.00308.has_implementation
  canonical_edge_type: HAS_IMPLEMENTATION
  source_card_id: metric.target_plus.effective_payout_rate
  target_card_id: metric_impl.target_plus.effective_payout_rate
  source_type: metric
  target_type: metric_implementation
  inverse_edge_type: IMPLEMENTS_METRIC
  materialize_inverse: true
  legacy_edge_aliases: []
  edge_class: canonical
  canonical_cognee_edge: true
```
```yaml
candidate_edge:
  edge_id: edge.target_plus.00309.uses_table
  canonical_edge_type: USES_TABLE
  source_card_id: metric_impl.target_plus.effective_payout_rate
  target_card_id: table.zs_observe.target_settlement
  source_type: metric_implementation
  target_type: table
  inverse_edge_type: null
  materialize_inverse: false
  legacy_edge_aliases:
  - implementation_uses_table
  edge_class: canonical
  canonical_cognee_edge: true
```
```yaml
candidate_edge:
  edge_id: edge.target_plus.00310.uses_column
  canonical_edge_type: USES_COLUMN
  source_card_id: metric_impl.target_plus.effective_payout_rate
  target_card_id: column.zs_observe.target_settlement.settled_amount
  source_type: metric_implementation
  target_type: column
  inverse_edge_type: null
  materialize_inverse: false
  legacy_edge_aliases:
  - implementation_uses_column
  edge_class: canonical
  canonical_cognee_edge: true
```
```yaml
candidate_edge:
  edge_id: edge.target_plus.00311.uses_column
  canonical_edge_type: USES_COLUMN
  source_card_id: metric_impl.target_plus.effective_payout_rate
  target_card_id: column.zs_observe.target_settlement.charged_amount_excluding_tax
  source_type: metric_implementation
  target_type: column
  inverse_edge_type: null
  materialize_inverse: false
  legacy_edge_aliases:
  - implementation_uses_column
  edge_class: canonical
  canonical_cognee_edge: true
```
```yaml
candidate_edge:
  edge_id: edge.target_plus.00312.implements_metric
  canonical_edge_type: IMPLEMENTS_METRIC
  source_card_id: metric_impl.target_plus.top_selling_skus
  target_card_id: metric.target_plus.top_selling_skus
  source_type: metric_implementation
  target_type: metric
  inverse_edge_type: HAS_IMPLEMENTATION
  materialize_inverse: true
  legacy_edge_aliases:
  - implements_metric
  edge_class: canonical
  canonical_cognee_edge: true
```
```yaml
candidate_edge:
  edge_id: edge.target_plus.00313.has_implementation
  canonical_edge_type: HAS_IMPLEMENTATION
  source_card_id: metric.target_plus.top_selling_skus
  target_card_id: metric_impl.target_plus.top_selling_skus
  source_type: metric
  target_type: metric_implementation
  inverse_edge_type: IMPLEMENTS_METRIC
  materialize_inverse: true
  legacy_edge_aliases: []
  edge_class: canonical
  canonical_cognee_edge: true
```
```yaml
candidate_edge:
  edge_id: edge.target_plus.00314.uses_table
  canonical_edge_type: USES_TABLE
  source_card_id: metric_impl.target_plus.top_selling_skus
  target_card_id: table.zs_observe.target_sales
  source_type: metric_implementation
  target_type: table
  inverse_edge_type: null
  materialize_inverse: false
  legacy_edge_aliases:
  - implementation_uses_table
  edge_class: canonical
  canonical_cognee_edge: true
```
```yaml
candidate_edge:
  edge_id: edge.target_plus.00315.uses_table
  canonical_edge_type: USES_TABLE
  source_card_id: metric_impl.target_plus.top_selling_skus
  target_card_id: table.zs_observe.target_tcin_mapping
  source_type: metric_implementation
  target_type: table
  inverse_edge_type: null
  materialize_inverse: false
  legacy_edge_aliases:
  - implementation_uses_table
  edge_class: canonical
  canonical_cognee_edge: true
```
```yaml
candidate_edge:
  edge_id: edge.target_plus.00316.uses_column
  canonical_edge_type: USES_COLUMN
  source_card_id: metric_impl.target_plus.top_selling_skus
  target_card_id: column.zs_observe.target_sales.tcin
  source_type: metric_implementation
  target_type: column
  inverse_edge_type: null
  materialize_inverse: false
  legacy_edge_aliases:
  - implementation_uses_column
  edge_class: canonical
  canonical_cognee_edge: true
```
```yaml
candidate_edge:
  edge_id: edge.target_plus.00317.uses_column
  canonical_edge_type: USES_COLUMN
  source_card_id: metric_impl.target_plus.top_selling_skus
  target_card_id: column.zs_observe.target_tcin_mapping.tcin
  source_type: metric_implementation
  target_type: column
  inverse_edge_type: null
  materialize_inverse: false
  legacy_edge_aliases:
  - implementation_uses_column
  edge_class: canonical
  canonical_cognee_edge: true
```
```yaml
candidate_edge:
  edge_id: edge.target_plus.00318.uses_column
  canonical_edge_type: USES_COLUMN
  source_card_id: metric_impl.target_plus.top_selling_skus
  target_card_id: column.zs_observe.target_sales.charged_amount
  source_type: metric_implementation
  target_type: column
  inverse_edge_type: null
  materialize_inverse: false
  legacy_edge_aliases:
  - implementation_uses_column
  edge_class: canonical
  canonical_cognee_edge: true
```
```yaml
candidate_edge:
  edge_id: edge.target_plus.00319.implements_metric
  canonical_edge_type: IMPLEMENTS_METRIC
  source_card_id: metric_impl.target_plus.cancellation_rate
  target_card_id: metric.target_plus.cancellation_rate
  source_type: metric_implementation
  target_type: metric
  inverse_edge_type: HAS_IMPLEMENTATION
  materialize_inverse: true
  legacy_edge_aliases:
  - implements_metric
  edge_class: canonical
  canonical_cognee_edge: true
```
```yaml
candidate_edge:
  edge_id: edge.target_plus.00320.has_implementation
  canonical_edge_type: HAS_IMPLEMENTATION
  source_card_id: metric.target_plus.cancellation_rate
  target_card_id: metric_impl.target_plus.cancellation_rate
  source_type: metric
  target_type: metric_implementation
  inverse_edge_type: IMPLEMENTS_METRIC
  materialize_inverse: true
  legacy_edge_aliases: []
  edge_class: canonical
  canonical_cognee_edge: true
```
```yaml
candidate_edge:
  edge_id: edge.target_plus.00321.uses_table
  canonical_edge_type: USES_TABLE
  source_card_id: metric_impl.target_plus.cancellation_rate
  target_card_id: table.zs_observe.target_sales
  source_type: metric_implementation
  target_type: table
  inverse_edge_type: null
  materialize_inverse: false
  legacy_edge_aliases:
  - implementation_uses_table
  edge_class: canonical
  canonical_cognee_edge: true
```
```yaml
candidate_edge:
  edge_id: edge.target_plus.00322.uses_column
  canonical_edge_type: USES_COLUMN
  source_card_id: metric_impl.target_plus.cancellation_rate
  target_card_id: column.zs_observe.target_sales.order_status
  source_type: metric_implementation
  target_type: column
  inverse_edge_type: null
  materialize_inverse: false
  legacy_edge_aliases:
  - implementation_uses_column
  edge_class: canonical
  canonical_cognee_edge: true
```
```yaml
candidate_edge:
  edge_id: edge.target_plus.00323.implements_metric
  canonical_edge_type: IMPLEMENTS_METRIC
  source_card_id: metric_impl.target_plus.commission_validation
  target_card_id: metric.target_plus.commission_validation_variance
  source_type: metric_implementation
  target_type: metric
  inverse_edge_type: HAS_IMPLEMENTATION
  materialize_inverse: true
  legacy_edge_aliases:
  - implements_metric
  edge_class: canonical
  canonical_cognee_edge: true
```
```yaml
candidate_edge:
  edge_id: edge.target_plus.00324.has_implementation
  canonical_edge_type: HAS_IMPLEMENTATION
  source_card_id: metric.target_plus.commission_validation_variance
  target_card_id: metric_impl.target_plus.commission_validation
  source_type: metric
  target_type: metric_implementation
  inverse_edge_type: IMPLEMENTS_METRIC
  materialize_inverse: true
  legacy_edge_aliases: []
  edge_class: canonical
  canonical_cognee_edge: true
```
```yaml
candidate_edge:
  edge_id: edge.target_plus.00325.uses_table
  canonical_edge_type: USES_TABLE
  source_card_id: metric_impl.target_plus.commission_validation
  target_card_id: table.zs_observe.target_settlement
  source_type: metric_implementation
  target_type: table
  inverse_edge_type: null
  materialize_inverse: false
  legacy_edge_aliases:
  - implementation_uses_table
  edge_class: canonical
  canonical_cognee_edge: true
```
```yaml
candidate_edge:
  edge_id: edge.target_plus.00326.uses_column
  canonical_edge_type: USES_COLUMN
  source_card_id: metric_impl.target_plus.commission_validation
  target_card_id: column.zs_observe.target_settlement.charged_amount_excluding_tax
  source_type: metric_implementation
  target_type: column
  inverse_edge_type: null
  materialize_inverse: false
  legacy_edge_aliases:
  - implementation_uses_column
  edge_class: canonical
  canonical_cognee_edge: true
```
```yaml
candidate_edge:
  edge_id: edge.target_plus.00327.uses_column
  canonical_edge_type: USES_COLUMN
  source_card_id: metric_impl.target_plus.commission_validation
  target_card_id: column.zs_observe.target_settlement.gross_commission
  source_type: metric_implementation
  target_type: column
  inverse_edge_type: null
  materialize_inverse: false
  legacy_edge_aliases:
  - implementation_uses_column
  edge_class: canonical
  canonical_cognee_edge: true
```
```yaml
candidate_edge:
  edge_id: edge.target_plus.00328.implements_metric
  canonical_edge_type: IMPLEMENTS_METRIC
  source_card_id: metric_impl.target_plus.payout_batch_total
  target_card_id: metric.target_plus.payout_batch_total
  source_type: metric_implementation
  target_type: metric
  inverse_edge_type: HAS_IMPLEMENTATION
  materialize_inverse: true
  legacy_edge_aliases:
  - implements_metric
  edge_class: canonical
  canonical_cognee_edge: true
```
```yaml
candidate_edge:
  edge_id: edge.target_plus.00329.has_implementation
  canonical_edge_type: HAS_IMPLEMENTATION
  source_card_id: metric.target_plus.payout_batch_total
  target_card_id: metric_impl.target_plus.payout_batch_total
  source_type: metric
  target_type: metric_implementation
  inverse_edge_type: IMPLEMENTS_METRIC
  materialize_inverse: true
  legacy_edge_aliases: []
  edge_class: canonical
  canonical_cognee_edge: true
```
```yaml
candidate_edge:
  edge_id: edge.target_plus.00330.uses_table
  canonical_edge_type: USES_TABLE
  source_card_id: metric_impl.target_plus.payout_batch_total
  target_card_id: table.zs_observe.target_settlement
  source_type: metric_implementation
  target_type: table
  inverse_edge_type: null
  materialize_inverse: false
  legacy_edge_aliases:
  - implementation_uses_table
  edge_class: canonical
  canonical_cognee_edge: true
```
```yaml
candidate_edge:
  edge_id: edge.target_plus.00331.uses_column
  canonical_edge_type: USES_COLUMN
  source_card_id: metric_impl.target_plus.payout_batch_total
  target_card_id: column.zs_observe.target_settlement.payout_id
  source_type: metric_implementation
  target_type: column
  inverse_edge_type: null
  materialize_inverse: false
  legacy_edge_aliases:
  - implementation_uses_column
  edge_class: canonical
  canonical_cognee_edge: true
```
```yaml
candidate_edge:
  edge_id: edge.target_plus.00332.uses_column
  canonical_edge_type: USES_COLUMN
  source_card_id: metric_impl.target_plus.payout_batch_total
  target_card_id: column.zs_observe.target_settlement.settled_amount
  source_type: metric_implementation
  target_type: column
  inverse_edge_type: null
  materialize_inverse: false
  legacy_edge_aliases:
  - implementation_uses_column
  edge_class: canonical
  canonical_cognee_edge: true
```
```yaml
candidate_edge:
  edge_id: edge.target_plus.00333.implements_metric
  canonical_edge_type: IMPLEMENTS_METRIC
  source_card_id: metric_impl.target_plus.return_reason_value
  target_card_id: metric.target_plus.return_reason_value
  source_type: metric_implementation
  target_type: metric
  inverse_edge_type: HAS_IMPLEMENTATION
  materialize_inverse: true
  legacy_edge_aliases:
  - implements_metric
  edge_class: canonical
  canonical_cognee_edge: true
```
```yaml
candidate_edge:
  edge_id: edge.target_plus.00334.has_implementation
  canonical_edge_type: HAS_IMPLEMENTATION
  source_card_id: metric.target_plus.return_reason_value
  target_card_id: metric_impl.target_plus.return_reason_value
  source_type: metric
  target_type: metric_implementation
  inverse_edge_type: IMPLEMENTS_METRIC
  materialize_inverse: true
  legacy_edge_aliases: []
  edge_class: canonical
  canonical_cognee_edge: true
```
```yaml
candidate_edge:
  edge_id: edge.target_plus.00335.uses_table
  canonical_edge_type: USES_TABLE
  source_card_id: metric_impl.target_plus.return_reason_value
  target_card_id: table.zs_observe.target_returns
  source_type: metric_implementation
  target_type: table
  inverse_edge_type: null
  materialize_inverse: false
  legacy_edge_aliases:
  - implementation_uses_table
  edge_class: canonical
  canonical_cognee_edge: true
```
```yaml
candidate_edge:
  edge_id: edge.target_plus.00336.uses_column
  canonical_edge_type: USES_COLUMN
  source_card_id: metric_impl.target_plus.return_reason_value
  target_card_id: column.zs_observe.target_returns.description
  source_type: metric_implementation
  target_type: column
  inverse_edge_type: null
  materialize_inverse: false
  legacy_edge_aliases:
  - implementation_uses_column
  edge_class: canonical
  canonical_cognee_edge: true
```
```yaml
candidate_edge:
  edge_id: edge.target_plus.00337.uses_column
  canonical_edge_type: USES_COLUMN
  source_card_id: metric_impl.target_plus.return_reason_value
  target_card_id: column.zs_observe.target_returns.charged_amount
  source_type: metric_implementation
  target_type: column
  inverse_edge_type: null
  materialize_inverse: false
  legacy_edge_aliases:
  - implementation_uses_column
  edge_class: canonical
  canonical_cognee_edge: true
```
```yaml
candidate_edge:
  edge_id: edge.target_plus.00338.implements_metric
  canonical_edge_type: IMPLEMENTS_METRIC
  source_card_id: metric_impl.target_plus.brand_return_rate
  target_card_id: metric.target_plus.brand_return_rate
  source_type: metric_implementation
  target_type: metric
  inverse_edge_type: HAS_IMPLEMENTATION
  materialize_inverse: true
  legacy_edge_aliases:
  - implements_metric
  edge_class: canonical
  canonical_cognee_edge: true
```
```yaml
candidate_edge:
  edge_id: edge.target_plus.00339.has_implementation
  canonical_edge_type: HAS_IMPLEMENTATION
  source_card_id: metric.target_plus.brand_return_rate
  target_card_id: metric_impl.target_plus.brand_return_rate
  source_type: metric
  target_type: metric_implementation
  inverse_edge_type: IMPLEMENTS_METRIC
  materialize_inverse: true
  legacy_edge_aliases: []
  edge_class: canonical
  canonical_cognee_edge: true
```
```yaml
candidate_edge:
  edge_id: edge.target_plus.00340.uses_table
  canonical_edge_type: USES_TABLE
  source_card_id: metric_impl.target_plus.brand_return_rate
  target_card_id: table.zs_observe.target_returns
  source_type: metric_implementation
  target_type: table
  inverse_edge_type: null
  materialize_inverse: false
  legacy_edge_aliases:
  - implementation_uses_table
  edge_class: canonical
  canonical_cognee_edge: true
```
```yaml
candidate_edge:
  edge_id: edge.target_plus.00341.uses_table
  canonical_edge_type: USES_TABLE
  source_card_id: metric_impl.target_plus.brand_return_rate
  target_card_id: table.zs_observe.target_sales
  source_type: metric_implementation
  target_type: table
  inverse_edge_type: null
  materialize_inverse: false
  legacy_edge_aliases:
  - implementation_uses_table
  edge_class: canonical
  canonical_cognee_edge: true
```
```yaml
candidate_edge:
  edge_id: edge.target_plus.00342.uses_column
  canonical_edge_type: USES_COLUMN
  source_card_id: metric_impl.target_plus.brand_return_rate
  target_card_id: column.zs_observe.target_returns.order_id
  source_type: metric_implementation
  target_type: column
  inverse_edge_type: null
  materialize_inverse: false
  legacy_edge_aliases:
  - implementation_uses_column
  edge_class: canonical
  canonical_cognee_edge: true
```
```yaml
candidate_edge:
  edge_id: edge.target_plus.00343.uses_column
  canonical_edge_type: USES_COLUMN
  source_card_id: metric_impl.target_plus.brand_return_rate
  target_card_id: column.zs_observe.target_sales.order_id
  source_type: metric_implementation
  target_type: column
  inverse_edge_type: null
  materialize_inverse: false
  legacy_edge_aliases:
  - implementation_uses_column
  edge_class: canonical
  canonical_cognee_edge: true
```
```yaml
candidate_edge:
  edge_id: edge.target_plus.00344.uses_column
  canonical_edge_type: USES_COLUMN
  source_card_id: metric_impl.target_plus.brand_return_rate
  target_card_id: column.zs_observe.target_sales.brand
  source_type: metric_implementation
  target_type: column
  inverse_edge_type: null
  materialize_inverse: false
  legacy_edge_aliases:
  - implementation_uses_column
  edge_class: canonical
  canonical_cognee_edge: true
```
```yaml
candidate_edge:
  edge_id: edge.target_plus.00345.implements_metric
  canonical_edge_type: IMPLEMENTS_METRIC
  source_card_id: metric_impl.target_plus.monthly_sales_gmv
  target_card_id: metric.target_plus.monthly_sales_gmv
  source_type: metric_implementation
  target_type: metric
  inverse_edge_type: HAS_IMPLEMENTATION
  materialize_inverse: true
  legacy_edge_aliases:
  - implements_metric
  edge_class: canonical
  canonical_cognee_edge: true
```
```yaml
candidate_edge:
  edge_id: edge.target_plus.00346.has_implementation
  canonical_edge_type: HAS_IMPLEMENTATION
  source_card_id: metric.target_plus.monthly_sales_gmv
  target_card_id: metric_impl.target_plus.monthly_sales_gmv
  source_type: metric
  target_type: metric_implementation
  inverse_edge_type: IMPLEMENTS_METRIC
  materialize_inverse: true
  legacy_edge_aliases: []
  edge_class: canonical
  canonical_cognee_edge: true
```
```yaml
candidate_edge:
  edge_id: edge.target_plus.00347.uses_table
  canonical_edge_type: USES_TABLE
  source_card_id: metric_impl.target_plus.monthly_sales_gmv
  target_card_id: table.zs_observe.target_sales
  source_type: metric_implementation
  target_type: table
  inverse_edge_type: null
  materialize_inverse: false
  legacy_edge_aliases:
  - implementation_uses_table
  edge_class: canonical
  canonical_cognee_edge: true
```
```yaml
candidate_edge:
  edge_id: edge.target_plus.00348.uses_column
  canonical_edge_type: USES_COLUMN
  source_card_id: metric_impl.target_plus.monthly_sales_gmv
  target_card_id: column.zs_observe.target_sales.created_date
  source_type: metric_implementation
  target_type: column
  inverse_edge_type: null
  materialize_inverse: false
  legacy_edge_aliases:
  - implementation_uses_column
  edge_class: canonical
  canonical_cognee_edge: true
```
```yaml
candidate_edge:
  edge_id: edge.target_plus.00349.uses_column
  canonical_edge_type: USES_COLUMN
  source_card_id: metric_impl.target_plus.monthly_sales_gmv
  target_card_id: column.zs_observe.target_sales.charged_amount
  source_type: metric_implementation
  target_type: column
  inverse_edge_type: null
  materialize_inverse: false
  legacy_edge_aliases:
  - implementation_uses_column
  edge_class: canonical
  canonical_cognee_edge: true
```
```yaml
candidate_edge:
  edge_id: edge.target_plus.00350.implements_metric
  canonical_edge_type: IMPLEMENTS_METRIC
  source_card_id: metric_impl.target_plus.mapping_sales_coverage
  target_card_id: metric.target_plus.mapping_sales_coverage
  source_type: metric_implementation
  target_type: metric
  inverse_edge_type: HAS_IMPLEMENTATION
  materialize_inverse: true
  legacy_edge_aliases:
  - implements_metric
  edge_class: canonical
  canonical_cognee_edge: true
```
```yaml
candidate_edge:
  edge_id: edge.target_plus.00351.has_implementation
  canonical_edge_type: HAS_IMPLEMENTATION
  source_card_id: metric.target_plus.mapping_sales_coverage
  target_card_id: metric_impl.target_plus.mapping_sales_coverage
  source_type: metric
  target_type: metric_implementation
  inverse_edge_type: IMPLEMENTS_METRIC
  materialize_inverse: true
  legacy_edge_aliases: []
  edge_class: canonical
  canonical_cognee_edge: true
```
```yaml
candidate_edge:
  edge_id: edge.target_plus.00352.uses_table
  canonical_edge_type: USES_TABLE
  source_card_id: metric_impl.target_plus.mapping_sales_coverage
  target_card_id: table.zs_observe.target_sales
  source_type: metric_implementation
  target_type: table
  inverse_edge_type: null
  materialize_inverse: false
  legacy_edge_aliases:
  - implementation_uses_table
  edge_class: canonical
  canonical_cognee_edge: true
```
```yaml
candidate_edge:
  edge_id: edge.target_plus.00353.uses_table
  canonical_edge_type: USES_TABLE
  source_card_id: metric_impl.target_plus.mapping_sales_coverage
  target_card_id: table.zs_observe.target_tcin_mapping
  source_type: metric_implementation
  target_type: table
  inverse_edge_type: null
  materialize_inverse: false
  legacy_edge_aliases:
  - implementation_uses_table
  edge_class: canonical
  canonical_cognee_edge: true
```
```yaml
candidate_edge:
  edge_id: edge.target_plus.00354.uses_column
  canonical_edge_type: USES_COLUMN
  source_card_id: metric_impl.target_plus.mapping_sales_coverage
  target_card_id: column.zs_observe.target_sales.tcin
  source_type: metric_implementation
  target_type: column
  inverse_edge_type: null
  materialize_inverse: false
  legacy_edge_aliases:
  - implementation_uses_column
  edge_class: canonical
  canonical_cognee_edge: true
```
```yaml
candidate_edge:
  edge_id: edge.target_plus.00355.uses_column
  canonical_edge_type: USES_COLUMN
  source_card_id: metric_impl.target_plus.mapping_sales_coverage
  target_card_id: column.zs_observe.target_tcin_mapping.tcin
  source_type: metric_implementation
  target_type: column
  inverse_edge_type: null
  materialize_inverse: false
  legacy_edge_aliases:
  - implementation_uses_column
  edge_class: canonical
  canonical_cognee_edge: true
```
```yaml
candidate_edge:
  edge_id: edge.target_plus.00356.uses_column
  canonical_edge_type: USES_COLUMN
  source_card_id: metric_impl.target_plus.mapping_sales_coverage
  target_card_id: column.zs_observe.target_sales.charged_amount
  source_type: metric_implementation
  target_type: column
  inverse_edge_type: null
  materialize_inverse: false
  legacy_edge_aliases:
  - implementation_uses_column
  edge_class: canonical
  canonical_cognee_edge: true
```
```yaml
candidate_edge:
  edge_id: edge.target_plus.00357.parent_metric
  canonical_edge_type: PARENT_METRIC
  source_card_id: metric_dependency.target_plus.net_revenue_components
  target_card_id: metric.target_plus.net_settlement_revenue
  source_type: metric_dependency
  target_type: metric
  inverse_edge_type: null
  materialize_inverse: false
  legacy_edge_aliases: []
  edge_class: canonical
  canonical_cognee_edge: true
```
```yaml
candidate_edge:
  edge_id: edge.target_plus.00358.uses_dependent_metric
  canonical_edge_type: USES_DEPENDENT_METRIC
  source_card_id: metric_dependency.target_plus.net_revenue_components
  target_card_id: metric.target_plus.total_gmv
  source_type: metric_dependency
  target_type: metric
  inverse_edge_type: null
  materialize_inverse: false
  legacy_edge_aliases: []
  edge_class: canonical
  canonical_cognee_edge: true
```
```yaml
candidate_edge:
  edge_id: edge.target_plus.00359.uses_dependent_metric
  canonical_edge_type: USES_DEPENDENT_METRIC
  source_card_id: metric_dependency.target_plus.net_revenue_components
  target_card_id: metric.target_plus.return_rate
  source_type: metric_dependency
  target_type: metric
  inverse_edge_type: null
  materialize_inverse: false
  legacy_edge_aliases: []
  edge_class: canonical
  canonical_cognee_edge: true
```
```yaml
candidate_edge:
  edge_id: edge.target_plus.00360.uses_dependent_metric
  canonical_edge_type: USES_DEPENDENT_METRIC
  source_card_id: metric_dependency.target_plus.net_revenue_components
  target_card_id: metric.target_plus.effective_payout_rate
  source_type: metric_dependency
  target_type: metric
  inverse_edge_type: null
  materialize_inverse: false
  legacy_edge_aliases: []
  edge_class: canonical
  canonical_cognee_edge: true
```
```yaml
candidate_edge:
  edge_id: edge.target_plus.00361.parent_metric
  canonical_edge_type: PARENT_METRIC
  source_card_id: metric_dependency.target_plus.return_rate_dependencies
  target_card_id: metric.target_plus.return_rate
  source_type: metric_dependency
  target_type: metric
  inverse_edge_type: null
  materialize_inverse: false
  legacy_edge_aliases: []
  edge_class: canonical
  canonical_cognee_edge: true
```
```yaml
candidate_edge:
  edge_id: edge.target_plus.00362.uses_dependent_metric
  canonical_edge_type: USES_DEPENDENT_METRIC
  source_card_id: metric_dependency.target_plus.return_rate_dependencies
  target_card_id: metric.target_plus.total_gmv
  source_type: metric_dependency
  target_type: metric
  inverse_edge_type: null
  materialize_inverse: false
  legacy_edge_aliases: []
  edge_class: canonical
  canonical_cognee_edge: true
```
```yaml
candidate_edge:
  edge_id: edge.target_plus.00363.parent_metric
  canonical_edge_type: PARENT_METRIC
  source_card_id: metric_dependency.target_plus.payout_rate_dependencies
  target_card_id: metric.target_plus.effective_payout_rate
  source_type: metric_dependency
  target_type: metric
  inverse_edge_type: null
  materialize_inverse: false
  legacy_edge_aliases: []
  edge_class: canonical
  canonical_cognee_edge: true
```
```yaml
candidate_edge:
  edge_id: edge.target_plus.00364.uses_dependent_metric
  canonical_edge_type: USES_DEPENDENT_METRIC
  source_card_id: metric_dependency.target_plus.payout_rate_dependencies
  target_card_id: metric.target_plus.commission_validation_variance
  source_type: metric_dependency
  target_type: metric
  inverse_edge_type: null
  materialize_inverse: false
  legacy_edge_aliases: []
  edge_class: canonical
  canonical_cognee_edge: true
```
```yaml
candidate_edge:
  edge_id: edge.target_plus.00365.belongs_to_domain
  canonical_edge_type: BELONGS_TO_DOMAIN
  source_card_id: business_process.target_plus.forward_order_flow
  target_card_id: domain.target_plus.orders
  source_type: business_process
  target_type: domain
  inverse_edge_type: null
  materialize_inverse: false
  legacy_edge_aliases: []
  edge_class: canonical
  canonical_cognee_edge: true
```
```yaml
candidate_edge:
  edge_id: edge.target_plus.00366.uses_table
  canonical_edge_type: USES_TABLE
  source_card_id: business_process.target_plus.forward_order_flow
  target_card_id: table.zs_observe.target_sales
  source_type: business_process
  target_type: table
  inverse_edge_type: null
  materialize_inverse: false
  legacy_edge_aliases:
  - process_uses_table
  edge_class: canonical
  canonical_cognee_edge: true
```
```yaml
candidate_edge:
  edge_id: edge.target_plus.00367.uses_table
  canonical_edge_type: USES_TABLE
  source_card_id: business_process.target_plus.forward_order_flow
  target_card_id: table.zs_observe.target_settlement
  source_type: business_process
  target_type: table
  inverse_edge_type: null
  materialize_inverse: false
  legacy_edge_aliases:
  - process_uses_table
  edge_class: canonical
  canonical_cognee_edge: true
```
```yaml
candidate_edge:
  edge_id: edge.target_plus.00368.belongs_to_process
  canonical_edge_type: BELONGS_TO_PROCESS
  source_card_id: workflow_step.target_plus.forward_order_flow.01
  target_card_id: business_process.target_plus.forward_order_flow
  source_type: workflow_step
  target_type: business_process
  inverse_edge_type: HAS_WORKFLOW_STEP
  materialize_inverse: true
  legacy_edge_aliases:
  - step_in_process
  edge_class: canonical
  canonical_cognee_edge: true
```
```yaml
candidate_edge:
  edge_id: edge.target_plus.00369.has_workflow_step
  canonical_edge_type: HAS_WORKFLOW_STEP
  source_card_id: business_process.target_plus.forward_order_flow
  target_card_id: workflow_step.target_plus.forward_order_flow.01
  source_type: business_process
  target_type: workflow_step
  inverse_edge_type: BELONGS_TO_PROCESS
  materialize_inverse: true
  legacy_edge_aliases: []
  edge_class: canonical
  canonical_cognee_edge: true
```
```yaml
candidate_edge:
  edge_id: edge.target_plus.00370.uses_table
  canonical_edge_type: USES_TABLE
  source_card_id: workflow_step.target_plus.forward_order_flow.01
  target_card_id: table.zs_observe.target_sales
  source_type: workflow_step
  target_type: table
  inverse_edge_type: null
  materialize_inverse: false
  legacy_edge_aliases:
  - process_uses_table
  edge_class: canonical
  canonical_cognee_edge: true
```
```yaml
candidate_edge:
  edge_id: edge.target_plus.00371.uses_table
  canonical_edge_type: USES_TABLE
  source_card_id: workflow_step.target_plus.forward_order_flow.01
  target_card_id: table.zs_observe.target_sales
  source_type: workflow_step
  target_type: table
  inverse_edge_type: null
  materialize_inverse: false
  legacy_edge_aliases:
  - process_uses_table
  edge_class: canonical
  canonical_cognee_edge: true
```
```yaml
candidate_edge:
  edge_id: edge.target_plus.00372.belongs_to_process
  canonical_edge_type: BELONGS_TO_PROCESS
  source_card_id: workflow_step.target_plus.forward_order_flow.02
  target_card_id: business_process.target_plus.forward_order_flow
  source_type: workflow_step
  target_type: business_process
  inverse_edge_type: HAS_WORKFLOW_STEP
  materialize_inverse: true
  legacy_edge_aliases:
  - step_in_process
  edge_class: canonical
  canonical_cognee_edge: true
```
```yaml
candidate_edge:
  edge_id: edge.target_plus.00373.has_workflow_step
  canonical_edge_type: HAS_WORKFLOW_STEP
  source_card_id: business_process.target_plus.forward_order_flow
  target_card_id: workflow_step.target_plus.forward_order_flow.02
  source_type: business_process
  target_type: workflow_step
  inverse_edge_type: BELONGS_TO_PROCESS
  materialize_inverse: true
  legacy_edge_aliases: []
  edge_class: canonical
  canonical_cognee_edge: true
```
```yaml
candidate_edge:
  edge_id: edge.target_plus.00374.uses_table
  canonical_edge_type: USES_TABLE
  source_card_id: workflow_step.target_plus.forward_order_flow.02
  target_card_id: table.zs_observe.target_sales
  source_type: workflow_step
  target_type: table
  inverse_edge_type: null
  materialize_inverse: false
  legacy_edge_aliases:
  - process_uses_table
  edge_class: canonical
  canonical_cognee_edge: true
```
```yaml
candidate_edge:
  edge_id: edge.target_plus.00375.belongs_to_process
  canonical_edge_type: BELONGS_TO_PROCESS
  source_card_id: workflow_step.target_plus.forward_order_flow.03
  target_card_id: business_process.target_plus.forward_order_flow
  source_type: workflow_step
  target_type: business_process
  inverse_edge_type: HAS_WORKFLOW_STEP
  materialize_inverse: true
  legacy_edge_aliases:
  - step_in_process
  edge_class: canonical
  canonical_cognee_edge: true
```
```yaml
candidate_edge:
  edge_id: edge.target_plus.00376.has_workflow_step
  canonical_edge_type: HAS_WORKFLOW_STEP
  source_card_id: business_process.target_plus.forward_order_flow
  target_card_id: workflow_step.target_plus.forward_order_flow.03
  source_type: business_process
  target_type: workflow_step
  inverse_edge_type: BELONGS_TO_PROCESS
  materialize_inverse: true
  legacy_edge_aliases: []
  edge_class: canonical
  canonical_cognee_edge: true
```
```yaml
candidate_edge:
  edge_id: edge.target_plus.00377.uses_table
  canonical_edge_type: USES_TABLE
  source_card_id: workflow_step.target_plus.forward_order_flow.03
  target_card_id: table.zs_observe.target_sales
  source_type: workflow_step
  target_type: table
  inverse_edge_type: null
  materialize_inverse: false
  legacy_edge_aliases:
  - process_uses_table
  edge_class: canonical
  canonical_cognee_edge: true
```
```yaml
candidate_edge:
  edge_id: edge.target_plus.00378.uses_table
  canonical_edge_type: USES_TABLE
  source_card_id: workflow_step.target_plus.forward_order_flow.03
  target_card_id: table.zs_observe.target_settlement
  source_type: workflow_step
  target_type: table
  inverse_edge_type: null
  materialize_inverse: false
  legacy_edge_aliases:
  - process_uses_table
  edge_class: canonical
  canonical_cognee_edge: true
```
```yaml
candidate_edge:
  edge_id: edge.target_plus.00379.belongs_to_process
  canonical_edge_type: BELONGS_TO_PROCESS
  source_card_id: workflow_step.target_plus.forward_order_flow.04
  target_card_id: business_process.target_plus.forward_order_flow
  source_type: workflow_step
  target_type: business_process
  inverse_edge_type: HAS_WORKFLOW_STEP
  materialize_inverse: true
  legacy_edge_aliases:
  - step_in_process
  edge_class: canonical
  canonical_cognee_edge: true
```
```yaml
candidate_edge:
  edge_id: edge.target_plus.00380.has_workflow_step
  canonical_edge_type: HAS_WORKFLOW_STEP
  source_card_id: business_process.target_plus.forward_order_flow
  target_card_id: workflow_step.target_plus.forward_order_flow.04
  source_type: business_process
  target_type: workflow_step
  inverse_edge_type: BELONGS_TO_PROCESS
  materialize_inverse: true
  legacy_edge_aliases: []
  edge_class: canonical
  canonical_cognee_edge: true
```
```yaml
candidate_edge:
  edge_id: edge.target_plus.00381.uses_table
  canonical_edge_type: USES_TABLE
  source_card_id: workflow_step.target_plus.forward_order_flow.04
  target_card_id: table.zs_observe.target_settlement
  source_type: workflow_step
  target_type: table
  inverse_edge_type: null
  materialize_inverse: false
  legacy_edge_aliases:
  - process_uses_table
  edge_class: canonical
  canonical_cognee_edge: true
```
```yaml
candidate_edge:
  edge_id: edge.target_plus.00382.uses_table
  canonical_edge_type: USES_TABLE
  source_card_id: workflow_step.target_plus.forward_order_flow.04
  target_card_id: table.zs_observe.target_settlement
  source_type: workflow_step
  target_type: table
  inverse_edge_type: null
  materialize_inverse: false
  legacy_edge_aliases:
  - process_uses_table
  edge_class: canonical
  canonical_cognee_edge: true
```
```yaml
candidate_edge:
  edge_id: edge.target_plus.00383.belongs_to_domain
  canonical_edge_type: BELONGS_TO_DOMAIN
  source_card_id: business_process.target_plus.return_flow
  target_card_id: domain.target_plus.returns
  source_type: business_process
  target_type: domain
  inverse_edge_type: null
  materialize_inverse: false
  legacy_edge_aliases: []
  edge_class: canonical
  canonical_cognee_edge: true
```
```yaml
candidate_edge:
  edge_id: edge.target_plus.00384.uses_table
  canonical_edge_type: USES_TABLE
  source_card_id: business_process.target_plus.return_flow
  target_card_id: table.zs_observe.target_returns
  source_type: business_process
  target_type: table
  inverse_edge_type: null
  materialize_inverse: false
  legacy_edge_aliases:
  - process_uses_table
  edge_class: canonical
  canonical_cognee_edge: true
```
```yaml
candidate_edge:
  edge_id: edge.target_plus.00385.uses_table
  canonical_edge_type: USES_TABLE
  source_card_id: business_process.target_plus.return_flow
  target_card_id: table.zs_observe.target_settlement
  source_type: business_process
  target_type: table
  inverse_edge_type: null
  materialize_inverse: false
  legacy_edge_aliases:
  - process_uses_table
  edge_class: canonical
  canonical_cognee_edge: true
```
```yaml
candidate_edge:
  edge_id: edge.target_plus.00386.uses_table
  canonical_edge_type: USES_TABLE
  source_card_id: business_process.target_plus.return_flow
  target_card_id: table.zs_observe.target_sales
  source_type: business_process
  target_type: table
  inverse_edge_type: null
  materialize_inverse: false
  legacy_edge_aliases:
  - process_uses_table
  edge_class: canonical
  canonical_cognee_edge: true
```
```yaml
candidate_edge:
  edge_id: edge.target_plus.00387.belongs_to_process
  canonical_edge_type: BELONGS_TO_PROCESS
  source_card_id: workflow_step.target_plus.return_flow.01
  target_card_id: business_process.target_plus.return_flow
  source_type: workflow_step
  target_type: business_process
  inverse_edge_type: HAS_WORKFLOW_STEP
  materialize_inverse: true
  legacy_edge_aliases:
  - step_in_process
  edge_class: canonical
  canonical_cognee_edge: true
```
```yaml
candidate_edge:
  edge_id: edge.target_plus.00388.has_workflow_step
  canonical_edge_type: HAS_WORKFLOW_STEP
  source_card_id: business_process.target_plus.return_flow
  target_card_id: workflow_step.target_plus.return_flow.01
  source_type: business_process
  target_type: workflow_step
  inverse_edge_type: BELONGS_TO_PROCESS
  materialize_inverse: true
  legacy_edge_aliases: []
  edge_class: canonical
  canonical_cognee_edge: true
```
```yaml
candidate_edge:
  edge_id: edge.target_plus.00389.uses_table
  canonical_edge_type: USES_TABLE
  source_card_id: workflow_step.target_plus.return_flow.01
  target_card_id: table.zs_observe.target_returns
  source_type: workflow_step
  target_type: table
  inverse_edge_type: null
  materialize_inverse: false
  legacy_edge_aliases:
  - process_uses_table
  edge_class: canonical
  canonical_cognee_edge: true
```
```yaml
candidate_edge:
  edge_id: edge.target_plus.00390.uses_table
  canonical_edge_type: USES_TABLE
  source_card_id: workflow_step.target_plus.return_flow.01
  target_card_id: table.zs_observe.target_returns
  source_type: workflow_step
  target_type: table
  inverse_edge_type: null
  materialize_inverse: false
  legacy_edge_aliases:
  - process_uses_table
  edge_class: canonical
  canonical_cognee_edge: true
```
```yaml
candidate_edge:
  edge_id: edge.target_plus.00391.belongs_to_process
  canonical_edge_type: BELONGS_TO_PROCESS
  source_card_id: workflow_step.target_plus.return_flow.02
  target_card_id: business_process.target_plus.return_flow
  source_type: workflow_step
  target_type: business_process
  inverse_edge_type: HAS_WORKFLOW_STEP
  materialize_inverse: true
  legacy_edge_aliases:
  - step_in_process
  edge_class: canonical
  canonical_cognee_edge: true
```
```yaml
candidate_edge:
  edge_id: edge.target_plus.00392.has_workflow_step
  canonical_edge_type: HAS_WORKFLOW_STEP
  source_card_id: business_process.target_plus.return_flow
  target_card_id: workflow_step.target_plus.return_flow.02
  source_type: business_process
  target_type: workflow_step
  inverse_edge_type: BELONGS_TO_PROCESS
  materialize_inverse: true
  legacy_edge_aliases: []
  edge_class: canonical
  canonical_cognee_edge: true
```
```yaml
candidate_edge:
  edge_id: edge.target_plus.00393.uses_table
  canonical_edge_type: USES_TABLE
  source_card_id: workflow_step.target_plus.return_flow.02
  target_card_id: table.zs_observe.target_returns
  source_type: workflow_step
  target_type: table
  inverse_edge_type: null
  materialize_inverse: false
  legacy_edge_aliases:
  - process_uses_table
  edge_class: canonical
  canonical_cognee_edge: true
```
```yaml
candidate_edge:
  edge_id: edge.target_plus.00394.uses_table
  canonical_edge_type: USES_TABLE
  source_card_id: workflow_step.target_plus.return_flow.02
  target_card_id: table.zs_observe.target_settlement
  source_type: workflow_step
  target_type: table
  inverse_edge_type: null
  materialize_inverse: false
  legacy_edge_aliases:
  - process_uses_table
  edge_class: canonical
  canonical_cognee_edge: true
```
```yaml
candidate_edge:
  edge_id: edge.target_plus.00395.belongs_to_process
  canonical_edge_type: BELONGS_TO_PROCESS
  source_card_id: workflow_step.target_plus.return_flow.03
  target_card_id: business_process.target_plus.return_flow
  source_type: workflow_step
  target_type: business_process
  inverse_edge_type: HAS_WORKFLOW_STEP
  materialize_inverse: true
  legacy_edge_aliases:
  - step_in_process
  edge_class: canonical
  canonical_cognee_edge: true
```
```yaml
candidate_edge:
  edge_id: edge.target_plus.00396.has_workflow_step
  canonical_edge_type: HAS_WORKFLOW_STEP
  source_card_id: business_process.target_plus.return_flow
  target_card_id: workflow_step.target_plus.return_flow.03
  source_type: business_process
  target_type: workflow_step
  inverse_edge_type: BELONGS_TO_PROCESS
  materialize_inverse: true
  legacy_edge_aliases: []
  edge_class: canonical
  canonical_cognee_edge: true
```
```yaml
candidate_edge:
  edge_id: edge.target_plus.00397.uses_table
  canonical_edge_type: USES_TABLE
  source_card_id: workflow_step.target_plus.return_flow.03
  target_card_id: table.zs_observe.target_returns
  source_type: workflow_step
  target_type: table
  inverse_edge_type: null
  materialize_inverse: false
  legacy_edge_aliases:
  - process_uses_table
  edge_class: canonical
  canonical_cognee_edge: true
```
```yaml
candidate_edge:
  edge_id: edge.target_plus.00398.uses_table
  canonical_edge_type: USES_TABLE
  source_card_id: workflow_step.target_plus.return_flow.03
  target_card_id: table.zs_observe.target_returns
  source_type: workflow_step
  target_type: table
  inverse_edge_type: null
  materialize_inverse: false
  legacy_edge_aliases:
  - process_uses_table
  edge_class: canonical
  canonical_cognee_edge: true
```
```yaml
candidate_edge:
  edge_id: edge.target_plus.00399.uses_table
  canonical_edge_type: USES_TABLE
  source_card_id: workflow_step.target_plus.return_flow.03
  target_card_id: table.zs_observe.target_settlement
  source_type: workflow_step
  target_type: table
  inverse_edge_type: null
  materialize_inverse: false
  legacy_edge_aliases:
  - process_uses_table
  edge_class: canonical
  canonical_cognee_edge: true
```
```yaml
candidate_edge:
  edge_id: edge.target_plus.00400.belongs_to_domain
  canonical_edge_type: BELONGS_TO_DOMAIN
  source_card_id: business_process.target_plus.reverse_charge_flow
  target_card_id: domain.target_plus.tax
  source_type: business_process
  target_type: domain
  inverse_edge_type: null
  materialize_inverse: false
  legacy_edge_aliases: []
  edge_class: canonical
  canonical_cognee_edge: true
```
```yaml
candidate_edge:
  edge_id: edge.target_plus.00401.uses_table
  canonical_edge_type: USES_TABLE
  source_card_id: business_process.target_plus.reverse_charge_flow
  target_card_id: table.zs_observe.target_settlement
  source_type: business_process
  target_type: table
  inverse_edge_type: null
  materialize_inverse: false
  legacy_edge_aliases:
  - process_uses_table
  edge_class: canonical
  canonical_cognee_edge: true
```
```yaml
candidate_edge:
  edge_id: edge.target_plus.00402.belongs_to_process
  canonical_edge_type: BELONGS_TO_PROCESS
  source_card_id: workflow_step.target_plus.reverse_charge_flow.01
  target_card_id: business_process.target_plus.reverse_charge_flow
  source_type: workflow_step
  target_type: business_process
  inverse_edge_type: HAS_WORKFLOW_STEP
  materialize_inverse: true
  legacy_edge_aliases:
  - step_in_process
  edge_class: canonical
  canonical_cognee_edge: true
```
```yaml
candidate_edge:
  edge_id: edge.target_plus.00403.has_workflow_step
  canonical_edge_type: HAS_WORKFLOW_STEP
  source_card_id: business_process.target_plus.reverse_charge_flow
  target_card_id: workflow_step.target_plus.reverse_charge_flow.01
  source_type: business_process
  target_type: workflow_step
  inverse_edge_type: BELONGS_TO_PROCESS
  materialize_inverse: true
  legacy_edge_aliases: []
  edge_class: canonical
  canonical_cognee_edge: true
```
```yaml
candidate_edge:
  edge_id: edge.target_plus.00404.uses_table
  canonical_edge_type: USES_TABLE
  source_card_id: workflow_step.target_plus.reverse_charge_flow.01
  target_card_id: table.zs_observe.target_settlement
  source_type: workflow_step
  target_type: table
  inverse_edge_type: null
  materialize_inverse: false
  legacy_edge_aliases:
  - process_uses_table
  edge_class: canonical
  canonical_cognee_edge: true
```
```yaml
candidate_edge:
  edge_id: edge.target_plus.00405.uses_table
  canonical_edge_type: USES_TABLE
  source_card_id: workflow_step.target_plus.reverse_charge_flow.01
  target_card_id: table.zs_observe.target_settlement
  source_type: workflow_step
  target_type: table
  inverse_edge_type: null
  materialize_inverse: false
  legacy_edge_aliases:
  - process_uses_table
  edge_class: canonical
  canonical_cognee_edge: true
```
```yaml
candidate_edge:
  edge_id: edge.target_plus.00406.belongs_to_process
  canonical_edge_type: BELONGS_TO_PROCESS
  source_card_id: workflow_step.target_plus.reverse_charge_flow.02
  target_card_id: business_process.target_plus.reverse_charge_flow
  source_type: workflow_step
  target_type: business_process
  inverse_edge_type: HAS_WORKFLOW_STEP
  materialize_inverse: true
  legacy_edge_aliases:
  - step_in_process
  edge_class: canonical
  canonical_cognee_edge: true
```
```yaml
candidate_edge:
  edge_id: edge.target_plus.00407.has_workflow_step
  canonical_edge_type: HAS_WORKFLOW_STEP
  source_card_id: business_process.target_plus.reverse_charge_flow
  target_card_id: workflow_step.target_plus.reverse_charge_flow.02
  source_type: business_process
  target_type: workflow_step
  inverse_edge_type: BELONGS_TO_PROCESS
  materialize_inverse: true
  legacy_edge_aliases: []
  edge_class: canonical
  canonical_cognee_edge: true
```
```yaml
candidate_edge:
  edge_id: edge.target_plus.00408.uses_table
  canonical_edge_type: USES_TABLE
  source_card_id: workflow_step.target_plus.reverse_charge_flow.02
  target_card_id: table.zs_observe.target_settlement
  source_type: workflow_step
  target_type: table
  inverse_edge_type: null
  materialize_inverse: false
  legacy_edge_aliases:
  - process_uses_table
  edge_class: canonical
  canonical_cognee_edge: true
```
```yaml
candidate_edge:
  edge_id: edge.target_plus.00409.uses_table
  canonical_edge_type: USES_TABLE
  source_card_id: workflow_step.target_plus.reverse_charge_flow.02
  target_card_id: table.zs_observe.target_settlement
  source_type: workflow_step
  target_type: table
  inverse_edge_type: null
  materialize_inverse: false
  legacy_edge_aliases:
  - process_uses_table
  edge_class: canonical
  canonical_cognee_edge: true
```
```yaml
candidate_edge:
  edge_id: edge.target_plus.00410.belongs_to_domain
  canonical_edge_type: BELONGS_TO_DOMAIN
  source_card_id: business_process.target_plus.product_mapping_enrichment
  target_card_id: domain.target_plus.mapping_enrichment
  source_type: business_process
  target_type: domain
  inverse_edge_type: null
  materialize_inverse: false
  legacy_edge_aliases: []
  edge_class: canonical
  canonical_cognee_edge: true
```
```yaml
candidate_edge:
  edge_id: edge.target_plus.00411.uses_table
  canonical_edge_type: USES_TABLE
  source_card_id: business_process.target_plus.product_mapping_enrichment
  target_card_id: table.zs_observe.target_sales
  source_type: business_process
  target_type: table
  inverse_edge_type: null
  materialize_inverse: false
  legacy_edge_aliases:
  - process_uses_table
  edge_class: canonical
  canonical_cognee_edge: true
```
```yaml
candidate_edge:
  edge_id: edge.target_plus.00412.uses_table
  canonical_edge_type: USES_TABLE
  source_card_id: business_process.target_plus.product_mapping_enrichment
  target_card_id: table.zs_observe.target_returns
  source_type: business_process
  target_type: table
  inverse_edge_type: null
  materialize_inverse: false
  legacy_edge_aliases:
  - process_uses_table
  edge_class: canonical
  canonical_cognee_edge: true
```
```yaml
candidate_edge:
  edge_id: edge.target_plus.00413.uses_table
  canonical_edge_type: USES_TABLE
  source_card_id: business_process.target_plus.product_mapping_enrichment
  target_card_id: table.zs_observe.target_settlement
  source_type: business_process
  target_type: table
  inverse_edge_type: null
  materialize_inverse: false
  legacy_edge_aliases:
  - process_uses_table
  edge_class: canonical
  canonical_cognee_edge: true
```
```yaml
candidate_edge:
  edge_id: edge.target_plus.00414.uses_table
  canonical_edge_type: USES_TABLE
  source_card_id: business_process.target_plus.product_mapping_enrichment
  target_card_id: table.zs_observe.target_tcin_mapping
  source_type: business_process
  target_type: table
  inverse_edge_type: null
  materialize_inverse: false
  legacy_edge_aliases:
  - process_uses_table
  edge_class: canonical
  canonical_cognee_edge: true
```
```yaml
candidate_edge:
  edge_id: edge.target_plus.00415.belongs_to_process
  canonical_edge_type: BELONGS_TO_PROCESS
  source_card_id: workflow_step.target_plus.product_mapping_enrichment.01
  target_card_id: business_process.target_plus.product_mapping_enrichment
  source_type: workflow_step
  target_type: business_process
  inverse_edge_type: HAS_WORKFLOW_STEP
  materialize_inverse: true
  legacy_edge_aliases:
  - step_in_process
  edge_class: canonical
  canonical_cognee_edge: true
```
```yaml
candidate_edge:
  edge_id: edge.target_plus.00416.has_workflow_step
  canonical_edge_type: HAS_WORKFLOW_STEP
  source_card_id: business_process.target_plus.product_mapping_enrichment
  target_card_id: workflow_step.target_plus.product_mapping_enrichment.01
  source_type: business_process
  target_type: workflow_step
  inverse_edge_type: BELONGS_TO_PROCESS
  materialize_inverse: true
  legacy_edge_aliases: []
  edge_class: canonical
  canonical_cognee_edge: true
```
```yaml
candidate_edge:
  edge_id: edge.target_plus.00417.uses_table
  canonical_edge_type: USES_TABLE
  source_card_id: workflow_step.target_plus.product_mapping_enrichment.01
  target_card_id: table.zs_observe.target_sales
  source_type: workflow_step
  target_type: table
  inverse_edge_type: null
  materialize_inverse: false
  legacy_edge_aliases:
  - process_uses_table
  edge_class: canonical
  canonical_cognee_edge: true
```
```yaml
candidate_edge:
  edge_id: edge.target_plus.00418.uses_table
  canonical_edge_type: USES_TABLE
  source_card_id: workflow_step.target_plus.product_mapping_enrichment.01
  target_card_id: table.zs_observe.target_returns
  source_type: workflow_step
  target_type: table
  inverse_edge_type: null
  materialize_inverse: false
  legacy_edge_aliases:
  - process_uses_table
  edge_class: canonical
  canonical_cognee_edge: true
```
```yaml
candidate_edge:
  edge_id: edge.target_plus.00419.uses_table
  canonical_edge_type: USES_TABLE
  source_card_id: workflow_step.target_plus.product_mapping_enrichment.01
  target_card_id: table.zs_observe.target_settlement
  source_type: workflow_step
  target_type: table
  inverse_edge_type: null
  materialize_inverse: false
  legacy_edge_aliases:
  - process_uses_table
  edge_class: canonical
  canonical_cognee_edge: true
```
```yaml
candidate_edge:
  edge_id: edge.target_plus.00420.uses_table
  canonical_edge_type: USES_TABLE
  source_card_id: workflow_step.target_plus.product_mapping_enrichment.01
  target_card_id: table.zs_observe.target_tcin_mapping
  source_type: workflow_step
  target_type: table
  inverse_edge_type: null
  materialize_inverse: false
  legacy_edge_aliases:
  - process_uses_table
  edge_class: canonical
  canonical_cognee_edge: true
```
```yaml
candidate_edge:
  edge_id: edge.target_plus.00421.belongs_to_process
  canonical_edge_type: BELONGS_TO_PROCESS
  source_card_id: workflow_step.target_plus.product_mapping_enrichment.02
  target_card_id: business_process.target_plus.product_mapping_enrichment
  source_type: workflow_step
  target_type: business_process
  inverse_edge_type: HAS_WORKFLOW_STEP
  materialize_inverse: true
  legacy_edge_aliases:
  - step_in_process
  edge_class: canonical
  canonical_cognee_edge: true
```
```yaml
candidate_edge:
  edge_id: edge.target_plus.00422.has_workflow_step
  canonical_edge_type: HAS_WORKFLOW_STEP
  source_card_id: business_process.target_plus.product_mapping_enrichment
  target_card_id: workflow_step.target_plus.product_mapping_enrichment.02
  source_type: business_process
  target_type: workflow_step
  inverse_edge_type: BELONGS_TO_PROCESS
  materialize_inverse: true
  legacy_edge_aliases: []
  edge_class: canonical
  canonical_cognee_edge: true
```
```yaml
candidate_edge:
  edge_id: edge.target_plus.00423.uses_table
  canonical_edge_type: USES_TABLE
  source_card_id: workflow_step.target_plus.product_mapping_enrichment.02
  target_card_id: table.zs_observe.target_tcin_mapping
  source_type: workflow_step
  target_type: table
  inverse_edge_type: null
  materialize_inverse: false
  legacy_edge_aliases:
  - process_uses_table
  edge_class: canonical
  canonical_cognee_edge: true
```
```yaml
candidate_edge:
  edge_id: edge.target_plus.00424.uses_table
  canonical_edge_type: USES_TABLE
  source_card_id: workflow_step.target_plus.product_mapping_enrichment.02
  target_card_id: table.zs_observe.target_tcin_mapping
  source_type: workflow_step
  target_type: table
  inverse_edge_type: null
  materialize_inverse: false
  legacy_edge_aliases:
  - process_uses_table
  edge_class: canonical
  canonical_cognee_edge: true
```
```yaml
candidate_edge:
  edge_id: edge.target_plus.00425.belongs_to_domain
  canonical_edge_type: BELONGS_TO_DOMAIN
  source_card_id: reconciliation_profile.target_plus.sales_settlement
  target_card_id: domain.target_plus.reconciliation
  source_type: reconciliation_profile
  target_type: domain
  inverse_edge_type: null
  materialize_inverse: false
  legacy_edge_aliases: []
  edge_class: canonical
  canonical_cognee_edge: true
```
```yaml
candidate_edge:
  edge_id: edge.target_plus.00426.has_primary_unit
  canonical_edge_type: HAS_PRIMARY_UNIT
  source_card_id: reconciliation_profile.target_plus.sales_settlement
  target_card_id: reconciliation_unit.target_plus.item_id_line
  source_type: reconciliation_profile
  target_type: reconciliation_unit
  inverse_edge_type: null
  materialize_inverse: false
  legacy_edge_aliases:
  - profile_uses_unit
  edge_class: canonical
  canonical_cognee_edge: true
```
```yaml
candidate_edge:
  edge_id: edge.target_plus.00427.uses_matching_logic
  canonical_edge_type: USES_MATCHING_LOGIC
  source_card_id: reconciliation_profile.target_plus.sales_settlement
  target_card_id: matching_logic.target_plus.sales_settlement_item_id
  source_type: reconciliation_profile
  target_type: matching_logic
  inverse_edge_type: SUPPORTS_RECONCILIATION_PROFILE
  materialize_inverse: true
  legacy_edge_aliases:
  - profile_uses_matching_logic
  edge_class: canonical
  canonical_cognee_edge: true
```
```yaml
candidate_edge:
  edge_id: edge.target_plus.00428.belongs_to_reconciliation_profile
  canonical_edge_type: BELONGS_TO_RECONCILIATION_PROFILE
  source_card_id: reconciliation_side.target_plus.sales_settlement.sales
  target_card_id: reconciliation_profile.target_plus.sales_settlement
  source_type: reconciliation_side
  target_type: reconciliation_profile
  inverse_edge_type: HAS_RECONCILIATION_SIDE
  materialize_inverse: true
  legacy_edge_aliases: []
  edge_class: canonical
  canonical_cognee_edge: true
```
```yaml
candidate_edge:
  edge_id: edge.target_plus.00429.has_reconciliation_side
  canonical_edge_type: HAS_RECONCILIATION_SIDE
  source_card_id: reconciliation_profile.target_plus.sales_settlement
  target_card_id: reconciliation_side.target_plus.sales_settlement.sales
  source_type: reconciliation_profile
  target_type: reconciliation_side
  inverse_edge_type: BELONGS_TO_RECONCILIATION_PROFILE
  materialize_inverse: true
  legacy_edge_aliases:
  - profile_expected_side
  edge_class: canonical
  canonical_cognee_edge: true
```
```yaml
candidate_edge:
  edge_id: edge.target_plus.00430.uses_table
  canonical_edge_type: USES_TABLE
  source_card_id: reconciliation_side.target_plus.sales_settlement.sales
  target_card_id: table.zs_observe.target_sales
  source_type: reconciliation_side
  target_type: table
  inverse_edge_type: null
  materialize_inverse: false
  legacy_edge_aliases:
  - side_uses_table
  edge_class: canonical
  canonical_cognee_edge: true
```
```yaml
candidate_edge:
  edge_id: edge.target_plus.00431.uses_column
  canonical_edge_type: USES_COLUMN
  source_card_id: reconciliation_side.target_plus.sales_settlement.sales
  target_card_id: column.zs_observe.target_sales.item_id
  source_type: reconciliation_side
  target_type: column
  inverse_edge_type: null
  materialize_inverse: false
  legacy_edge_aliases:
  - side_uses_key_column
  edge_class: canonical
  canonical_cognee_edge: true
```
```yaml
candidate_edge:
  edge_id: edge.target_plus.00432.uses_column
  canonical_edge_type: USES_COLUMN
  source_card_id: reconciliation_side.target_plus.sales_settlement.sales
  target_card_id: column.zs_observe.target_sales.order_id
  source_type: reconciliation_side
  target_type: column
  inverse_edge_type: null
  materialize_inverse: false
  legacy_edge_aliases:
  - side_uses_key_column
  edge_class: canonical
  canonical_cognee_edge: true
```
```yaml
candidate_edge:
  edge_id: edge.target_plus.00433.uses_column
  canonical_edge_type: USES_COLUMN
  source_card_id: reconciliation_side.target_plus.sales_settlement.sales
  target_card_id: column.zs_observe.target_sales.brand
  source_type: reconciliation_side
  target_type: column
  inverse_edge_type: null
  materialize_inverse: false
  legacy_edge_aliases:
  - side_uses_key_column
  edge_class: canonical
  canonical_cognee_edge: true
```
```yaml
candidate_edge:
  edge_id: edge.target_plus.00434.uses_column
  canonical_edge_type: USES_COLUMN
  source_card_id: reconciliation_side.target_plus.sales_settlement.sales
  target_card_id: column.zs_observe.target_sales.charged_amount
  source_type: reconciliation_side
  target_type: column
  inverse_edge_type: null
  materialize_inverse: false
  legacy_edge_aliases:
  - side_uses_key_column
  edge_class: canonical
  canonical_cognee_edge: true
```
```yaml
candidate_edge:
  edge_id: edge.target_plus.00435.uses_column
  canonical_edge_type: USES_COLUMN
  source_card_id: reconciliation_side.target_plus.sales_settlement.sales
  target_card_id: column.zs_observe.target_sales.created_date
  source_type: reconciliation_side
  target_type: column
  inverse_edge_type: null
  materialize_inverse: false
  legacy_edge_aliases:
  - side_uses_key_column
  edge_class: canonical
  canonical_cognee_edge: true
```
```yaml
candidate_edge:
  edge_id: edge.target_plus.00436.uses_column
  canonical_edge_type: USES_COLUMN
  source_card_id: reconciliation_side.target_plus.sales_settlement.sales
  target_card_id: column.zs_observe.target_sales.order_status
  source_type: reconciliation_side
  target_type: column
  inverse_edge_type: null
  materialize_inverse: false
  legacy_edge_aliases:
  - side_uses_key_column
  edge_class: canonical
  canonical_cognee_edge: true
```
```yaml
candidate_edge:
  edge_id: edge.target_plus.00437.uses_column
  canonical_edge_type: USES_COLUMN
  source_card_id: reconciliation_side.target_plus.sales_settlement.sales
  target_card_id: column.zs_observe.target_sales.transaction_type
  source_type: reconciliation_side
  target_type: column
  inverse_edge_type: null
  materialize_inverse: false
  legacy_edge_aliases:
  - side_uses_key_column
  edge_class: canonical
  canonical_cognee_edge: true
```
```yaml
candidate_edge:
  edge_id: edge.target_plus.00438.belongs_to_reconciliation_profile
  canonical_edge_type: BELONGS_TO_RECONCILIATION_PROFILE
  source_card_id: reconciliation_side.target_plus.sales_settlement.settlement
  target_card_id: reconciliation_profile.target_plus.sales_settlement
  source_type: reconciliation_side
  target_type: reconciliation_profile
  inverse_edge_type: HAS_RECONCILIATION_SIDE
  materialize_inverse: true
  legacy_edge_aliases: []
  edge_class: canonical
  canonical_cognee_edge: true
```
```yaml
candidate_edge:
  edge_id: edge.target_plus.00439.has_reconciliation_side
  canonical_edge_type: HAS_RECONCILIATION_SIDE
  source_card_id: reconciliation_profile.target_plus.sales_settlement
  target_card_id: reconciliation_side.target_plus.sales_settlement.settlement
  source_type: reconciliation_profile
  target_type: reconciliation_side
  inverse_edge_type: BELONGS_TO_RECONCILIATION_PROFILE
  materialize_inverse: true
  legacy_edge_aliases:
  - profile_actual_side
  edge_class: canonical
  canonical_cognee_edge: true
```
```yaml
candidate_edge:
  edge_id: edge.target_plus.00440.uses_table
  canonical_edge_type: USES_TABLE
  source_card_id: reconciliation_side.target_plus.sales_settlement.settlement
  target_card_id: table.zs_observe.target_settlement
  source_type: reconciliation_side
  target_type: table
  inverse_edge_type: null
  materialize_inverse: false
  legacy_edge_aliases:
  - side_uses_table
  edge_class: canonical
  canonical_cognee_edge: true
```
```yaml
candidate_edge:
  edge_id: edge.target_plus.00441.uses_column
  canonical_edge_type: USES_COLUMN
  source_card_id: reconciliation_side.target_plus.sales_settlement.settlement
  target_card_id: column.zs_observe.target_settlement.item_id
  source_type: reconciliation_side
  target_type: column
  inverse_edge_type: null
  materialize_inverse: false
  legacy_edge_aliases:
  - side_uses_key_column
  edge_class: canonical
  canonical_cognee_edge: true
```
```yaml
candidate_edge:
  edge_id: edge.target_plus.00442.uses_column
  canonical_edge_type: USES_COLUMN
  source_card_id: reconciliation_side.target_plus.sales_settlement.settlement
  target_card_id: column.zs_observe.target_settlement.order_id
  source_type: reconciliation_side
  target_type: column
  inverse_edge_type: null
  materialize_inverse: false
  legacy_edge_aliases:
  - side_uses_key_column
  edge_class: canonical
  canonical_cognee_edge: true
```
```yaml
candidate_edge:
  edge_id: edge.target_plus.00443.uses_column
  canonical_edge_type: USES_COLUMN
  source_card_id: reconciliation_side.target_plus.sales_settlement.settlement
  target_card_id: column.zs_observe.target_settlement.brand
  source_type: reconciliation_side
  target_type: column
  inverse_edge_type: null
  materialize_inverse: false
  legacy_edge_aliases:
  - side_uses_key_column
  edge_class: canonical
  canonical_cognee_edge: true
```
```yaml
candidate_edge:
  edge_id: edge.target_plus.00444.uses_column
  canonical_edge_type: USES_COLUMN
  source_card_id: reconciliation_side.target_plus.sales_settlement.settlement
  target_card_id: column.zs_observe.target_settlement.charged_amount
  source_type: reconciliation_side
  target_type: column
  inverse_edge_type: null
  materialize_inverse: false
  legacy_edge_aliases:
  - side_uses_key_column
  edge_class: canonical
  canonical_cognee_edge: true
```
```yaml
candidate_edge:
  edge_id: edge.target_plus.00445.uses_column
  canonical_edge_type: USES_COLUMN
  source_card_id: reconciliation_side.target_plus.sales_settlement.settlement
  target_card_id: column.zs_observe.target_settlement.charged_amount_excluding_tax
  source_type: reconciliation_side
  target_type: column
  inverse_edge_type: null
  materialize_inverse: false
  legacy_edge_aliases:
  - side_uses_key_column
  edge_class: canonical
  canonical_cognee_edge: true
```
```yaml
candidate_edge:
  edge_id: edge.target_plus.00446.uses_column
  canonical_edge_type: USES_COLUMN
  source_card_id: reconciliation_side.target_plus.sales_settlement.settlement
  target_card_id: column.zs_observe.target_settlement.gross_commission
  source_type: reconciliation_side
  target_type: column
  inverse_edge_type: null
  materialize_inverse: false
  legacy_edge_aliases:
  - side_uses_key_column
  edge_class: canonical
  canonical_cognee_edge: true
```
```yaml
candidate_edge:
  edge_id: edge.target_plus.00447.uses_column
  canonical_edge_type: USES_COLUMN
  source_card_id: reconciliation_side.target_plus.sales_settlement.settlement
  target_card_id: column.zs_observe.target_settlement.settled_amount
  source_type: reconciliation_side
  target_type: column
  inverse_edge_type: null
  materialize_inverse: false
  legacy_edge_aliases:
  - side_uses_key_column
  edge_class: canonical
  canonical_cognee_edge: true
```
```yaml
candidate_edge:
  edge_id: edge.target_plus.00448.uses_column
  canonical_edge_type: USES_COLUMN
  source_card_id: reconciliation_side.target_plus.sales_settlement.settlement
  target_card_id: column.zs_observe.target_settlement.created_date
  source_type: reconciliation_side
  target_type: column
  inverse_edge_type: null
  materialize_inverse: false
  legacy_edge_aliases:
  - side_uses_key_column
  edge_class: canonical
  canonical_cognee_edge: true
```
```yaml
candidate_edge:
  edge_id: edge.target_plus.00449.uses_column
  canonical_edge_type: USES_COLUMN
  source_card_id: reconciliation_side.target_plus.sales_settlement.settlement
  target_card_id: column.zs_observe.target_settlement.transaction_type
  source_type: reconciliation_side
  target_type: column
  inverse_edge_type: null
  materialize_inverse: false
  legacy_edge_aliases:
  - side_uses_key_column
  edge_class: canonical
  canonical_cognee_edge: true
```
```yaml
candidate_edge:
  edge_id: edge.target_plus.00450.uses_column
  canonical_edge_type: USES_COLUMN
  source_card_id: reconciliation_side.target_plus.sales_settlement.settlement
  target_card_id: column.zs_observe.target_settlement.internal_txn_type
  source_type: reconciliation_side
  target_type: column
  inverse_edge_type: null
  materialize_inverse: false
  legacy_edge_aliases:
  - side_uses_key_column
  edge_class: canonical
  canonical_cognee_edge: true
```
```yaml
candidate_edge:
  edge_id: edge.target_plus.00451.mismatch_of_profile
  canonical_edge_type: MISMATCH_OF_PROFILE
  source_card_id: mismatch_category.target_plus.sales_settlement.not_yet_settled
  target_card_id: reconciliation_profile.target_plus.sales_settlement
  source_type: mismatch_category
  target_type: reconciliation_profile
  inverse_edge_type: HAS_MISMATCH_CATEGORY
  materialize_inverse: true
  legacy_edge_aliases: []
  edge_class: canonical
  canonical_cognee_edge: true
```
```yaml
candidate_edge:
  edge_id: edge.target_plus.00452.has_mismatch_category
  canonical_edge_type: HAS_MISMATCH_CATEGORY
  source_card_id: reconciliation_profile.target_plus.sales_settlement
  target_card_id: mismatch_category.target_plus.sales_settlement.not_yet_settled
  source_type: reconciliation_profile
  target_type: mismatch_category
  inverse_edge_type: MISMATCH_OF_PROFILE
  materialize_inverse: false
  legacy_edge_aliases:
  - profile_has_mismatch_category
  edge_class: canonical
  canonical_cognee_edge: true
```
```yaml
candidate_edge:
  edge_id: edge.target_plus.00453.mismatch_of_profile
  canonical_edge_type: MISMATCH_OF_PROFILE
  source_card_id: mismatch_category.target_plus.sales_settlement.price_variance
  target_card_id: reconciliation_profile.target_plus.sales_settlement
  source_type: mismatch_category
  target_type: reconciliation_profile
  inverse_edge_type: HAS_MISMATCH_CATEGORY
  materialize_inverse: true
  legacy_edge_aliases: []
  edge_class: canonical
  canonical_cognee_edge: true
```
```yaml
candidate_edge:
  edge_id: edge.target_plus.00454.has_mismatch_category
  canonical_edge_type: HAS_MISMATCH_CATEGORY
  source_card_id: reconciliation_profile.target_plus.sales_settlement
  target_card_id: mismatch_category.target_plus.sales_settlement.price_variance
  source_type: reconciliation_profile
  target_type: mismatch_category
  inverse_edge_type: MISMATCH_OF_PROFILE
  materialize_inverse: false
  legacy_edge_aliases:
  - profile_has_mismatch_category
  edge_class: canonical
  canonical_cognee_edge: true
```
```yaml
candidate_edge:
  edge_id: edge.target_plus.00455.belongs_to_domain
  canonical_edge_type: BELONGS_TO_DOMAIN
  source_card_id: reconciliation_profile.target_plus.returns_settlement
  target_card_id: domain.target_plus.reconciliation
  source_type: reconciliation_profile
  target_type: domain
  inverse_edge_type: null
  materialize_inverse: false
  legacy_edge_aliases: []
  edge_class: canonical
  canonical_cognee_edge: true
```
```yaml
candidate_edge:
  edge_id: edge.target_plus.00456.has_primary_unit
  canonical_edge_type: HAS_PRIMARY_UNIT
  source_card_id: reconciliation_profile.target_plus.returns_settlement
  target_card_id: reconciliation_unit.target_plus.item_id_line
  source_type: reconciliation_profile
  target_type: reconciliation_unit
  inverse_edge_type: null
  materialize_inverse: false
  legacy_edge_aliases:
  - profile_uses_unit
  edge_class: canonical
  canonical_cognee_edge: true
```
```yaml
candidate_edge:
  edge_id: edge.target_plus.00457.uses_matching_logic
  canonical_edge_type: USES_MATCHING_LOGIC
  source_card_id: reconciliation_profile.target_plus.returns_settlement
  target_card_id: matching_logic.target_plus.returns_settlement_item_id
  source_type: reconciliation_profile
  target_type: matching_logic
  inverse_edge_type: SUPPORTS_RECONCILIATION_PROFILE
  materialize_inverse: true
  legacy_edge_aliases:
  - profile_uses_matching_logic
  edge_class: canonical
  canonical_cognee_edge: true
```
```yaml
candidate_edge:
  edge_id: edge.target_plus.00458.belongs_to_reconciliation_profile
  canonical_edge_type: BELONGS_TO_RECONCILIATION_PROFILE
  source_card_id: reconciliation_side.target_plus.returns_settlement.returns
  target_card_id: reconciliation_profile.target_plus.returns_settlement
  source_type: reconciliation_side
  target_type: reconciliation_profile
  inverse_edge_type: HAS_RECONCILIATION_SIDE
  materialize_inverse: true
  legacy_edge_aliases: []
  edge_class: canonical
  canonical_cognee_edge: true
```
```yaml
candidate_edge:
  edge_id: edge.target_plus.00459.has_reconciliation_side
  canonical_edge_type: HAS_RECONCILIATION_SIDE
  source_card_id: reconciliation_profile.target_plus.returns_settlement
  target_card_id: reconciliation_side.target_plus.returns_settlement.returns
  source_type: reconciliation_profile
  target_type: reconciliation_side
  inverse_edge_type: BELONGS_TO_RECONCILIATION_PROFILE
  materialize_inverse: true
  legacy_edge_aliases:
  - profile_expected_side
  edge_class: canonical
  canonical_cognee_edge: true
```
```yaml
candidate_edge:
  edge_id: edge.target_plus.00460.uses_table
  canonical_edge_type: USES_TABLE
  source_card_id: reconciliation_side.target_plus.returns_settlement.returns
  target_card_id: table.zs_observe.target_returns
  source_type: reconciliation_side
  target_type: table
  inverse_edge_type: null
  materialize_inverse: false
  legacy_edge_aliases:
  - side_uses_table
  edge_class: canonical
  canonical_cognee_edge: true
```
```yaml
candidate_edge:
  edge_id: edge.target_plus.00461.uses_column
  canonical_edge_type: USES_COLUMN
  source_card_id: reconciliation_side.target_plus.returns_settlement.returns
  target_card_id: column.zs_observe.target_returns.item_id
  source_type: reconciliation_side
  target_type: column
  inverse_edge_type: null
  materialize_inverse: false
  legacy_edge_aliases:
  - side_uses_key_column
  edge_class: canonical
  canonical_cognee_edge: true
```
```yaml
candidate_edge:
  edge_id: edge.target_plus.00462.uses_column
  canonical_edge_type: USES_COLUMN
  source_card_id: reconciliation_side.target_plus.returns_settlement.returns
  target_card_id: column.zs_observe.target_returns.order_id
  source_type: reconciliation_side
  target_type: column
  inverse_edge_type: null
  materialize_inverse: false
  legacy_edge_aliases:
  - side_uses_key_column
  edge_class: canonical
  canonical_cognee_edge: true
```
```yaml
candidate_edge:
  edge_id: edge.target_plus.00463.uses_column
  canonical_edge_type: USES_COLUMN
  source_card_id: reconciliation_side.target_plus.returns_settlement.returns
  target_card_id: column.zs_observe.target_returns.tcin
  source_type: reconciliation_side
  target_type: column
  inverse_edge_type: null
  materialize_inverse: false
  legacy_edge_aliases:
  - side_uses_key_column
  edge_class: canonical
  canonical_cognee_edge: true
```
```yaml
candidate_edge:
  edge_id: edge.target_plus.00464.uses_column
  canonical_edge_type: USES_COLUMN
  source_card_id: reconciliation_side.target_plus.returns_settlement.returns
  target_card_id: column.zs_observe.target_returns.charged_amount
  source_type: reconciliation_side
  target_type: column
  inverse_edge_type: null
  materialize_inverse: false
  legacy_edge_aliases:
  - side_uses_key_column
  edge_class: canonical
  canonical_cognee_edge: true
```
```yaml
candidate_edge:
  edge_id: edge.target_plus.00465.uses_column
  canonical_edge_type: USES_COLUMN
  source_card_id: reconciliation_side.target_plus.returns_settlement.returns
  target_card_id: column.zs_observe.target_returns.returned_date
  source_type: reconciliation_side
  target_type: column
  inverse_edge_type: null
  materialize_inverse: false
  legacy_edge_aliases:
  - side_uses_key_column
  edge_class: canonical
  canonical_cognee_edge: true
```
```yaml
candidate_edge:
  edge_id: edge.target_plus.00466.uses_column
  canonical_edge_type: USES_COLUMN
  source_card_id: reconciliation_side.target_plus.returns_settlement.returns
  target_card_id: column.zs_observe.target_returns.created_date
  source_type: reconciliation_side
  target_type: column
  inverse_edge_type: null
  materialize_inverse: false
  legacy_edge_aliases:
  - side_uses_key_column
  edge_class: canonical
  canonical_cognee_edge: true
```
```yaml
candidate_edge:
  edge_id: edge.target_plus.00467.uses_column
  canonical_edge_type: USES_COLUMN
  source_card_id: reconciliation_side.target_plus.returns_settlement.returns
  target_card_id: column.zs_observe.target_returns.internal_txn_type
  source_type: reconciliation_side
  target_type: column
  inverse_edge_type: null
  materialize_inverse: false
  legacy_edge_aliases:
  - side_uses_key_column
  edge_class: canonical
  canonical_cognee_edge: true
```
```yaml
candidate_edge:
  edge_id: edge.target_plus.00468.uses_column
  canonical_edge_type: USES_COLUMN
  source_card_id: reconciliation_side.target_plus.returns_settlement.returns
  target_card_id: column.zs_observe.target_returns.transaction_type
  source_type: reconciliation_side
  target_type: column
  inverse_edge_type: null
  materialize_inverse: false
  legacy_edge_aliases:
  - side_uses_key_column
  edge_class: canonical
  canonical_cognee_edge: true
```
```yaml
candidate_edge:
  edge_id: edge.target_plus.00469.belongs_to_reconciliation_profile
  canonical_edge_type: BELONGS_TO_RECONCILIATION_PROFILE
  source_card_id: reconciliation_side.target_plus.returns_settlement.settlement
  target_card_id: reconciliation_profile.target_plus.returns_settlement
  source_type: reconciliation_side
  target_type: reconciliation_profile
  inverse_edge_type: HAS_RECONCILIATION_SIDE
  materialize_inverse: true
  legacy_edge_aliases: []
  edge_class: canonical
  canonical_cognee_edge: true
```
```yaml
candidate_edge:
  edge_id: edge.target_plus.00470.has_reconciliation_side
  canonical_edge_type: HAS_RECONCILIATION_SIDE
  source_card_id: reconciliation_profile.target_plus.returns_settlement
  target_card_id: reconciliation_side.target_plus.returns_settlement.settlement
  source_type: reconciliation_profile
  target_type: reconciliation_side
  inverse_edge_type: BELONGS_TO_RECONCILIATION_PROFILE
  materialize_inverse: true
  legacy_edge_aliases:
  - profile_actual_side
  edge_class: canonical
  canonical_cognee_edge: true
```
```yaml
candidate_edge:
  edge_id: edge.target_plus.00471.uses_table
  canonical_edge_type: USES_TABLE
  source_card_id: reconciliation_side.target_plus.returns_settlement.settlement
  target_card_id: table.zs_observe.target_settlement
  source_type: reconciliation_side
  target_type: table
  inverse_edge_type: null
  materialize_inverse: false
  legacy_edge_aliases:
  - side_uses_table
  edge_class: canonical
  canonical_cognee_edge: true
```
```yaml
candidate_edge:
  edge_id: edge.target_plus.00472.uses_column
  canonical_edge_type: USES_COLUMN
  source_card_id: reconciliation_side.target_plus.returns_settlement.settlement
  target_card_id: column.zs_observe.target_settlement.item_id
  source_type: reconciliation_side
  target_type: column
  inverse_edge_type: null
  materialize_inverse: false
  legacy_edge_aliases:
  - side_uses_key_column
  edge_class: canonical
  canonical_cognee_edge: true
```
```yaml
candidate_edge:
  edge_id: edge.target_plus.00473.uses_column
  canonical_edge_type: USES_COLUMN
  source_card_id: reconciliation_side.target_plus.returns_settlement.settlement
  target_card_id: column.zs_observe.target_settlement.order_id
  source_type: reconciliation_side
  target_type: column
  inverse_edge_type: null
  materialize_inverse: false
  legacy_edge_aliases:
  - side_uses_key_column
  edge_class: canonical
  canonical_cognee_edge: true
```
```yaml
candidate_edge:
  edge_id: edge.target_plus.00474.uses_column
  canonical_edge_type: USES_COLUMN
  source_card_id: reconciliation_side.target_plus.returns_settlement.settlement
  target_card_id: column.zs_observe.target_settlement.tcin
  source_type: reconciliation_side
  target_type: column
  inverse_edge_type: null
  materialize_inverse: false
  legacy_edge_aliases:
  - side_uses_key_column
  edge_class: canonical
  canonical_cognee_edge: true
```
```yaml
candidate_edge:
  edge_id: edge.target_plus.00475.uses_column
  canonical_edge_type: USES_COLUMN
  source_card_id: reconciliation_side.target_plus.returns_settlement.settlement
  target_card_id: column.zs_observe.target_settlement.settled_amount
  source_type: reconciliation_side
  target_type: column
  inverse_edge_type: null
  materialize_inverse: false
  legacy_edge_aliases:
  - side_uses_key_column
  edge_class: canonical
  canonical_cognee_edge: true
```
```yaml
candidate_edge:
  edge_id: edge.target_plus.00476.uses_column
  canonical_edge_type: USES_COLUMN
  source_card_id: reconciliation_side.target_plus.returns_settlement.settlement
  target_card_id: column.zs_observe.target_settlement.gross_commission
  source_type: reconciliation_side
  target_type: column
  inverse_edge_type: null
  materialize_inverse: false
  legacy_edge_aliases:
  - side_uses_key_column
  edge_class: canonical
  canonical_cognee_edge: true
```
```yaml
candidate_edge:
  edge_id: edge.target_plus.00477.uses_column
  canonical_edge_type: USES_COLUMN
  source_card_id: reconciliation_side.target_plus.returns_settlement.settlement
  target_card_id: column.zs_observe.target_settlement.charged_amount_excluding_tax
  source_type: reconciliation_side
  target_type: column
  inverse_edge_type: null
  materialize_inverse: false
  legacy_edge_aliases:
  - side_uses_key_column
  edge_class: canonical
  canonical_cognee_edge: true
```
```yaml
candidate_edge:
  edge_id: edge.target_plus.00478.uses_column
  canonical_edge_type: USES_COLUMN
  source_card_id: reconciliation_side.target_plus.returns_settlement.settlement
  target_card_id: column.zs_observe.target_settlement.returned_date
  source_type: reconciliation_side
  target_type: column
  inverse_edge_type: null
  materialize_inverse: false
  legacy_edge_aliases:
  - side_uses_key_column
  edge_class: canonical
  canonical_cognee_edge: true
```
```yaml
candidate_edge:
  edge_id: edge.target_plus.00479.uses_column
  canonical_edge_type: USES_COLUMN
  source_card_id: reconciliation_side.target_plus.returns_settlement.settlement
  target_card_id: column.zs_observe.target_settlement.created_date
  source_type: reconciliation_side
  target_type: column
  inverse_edge_type: null
  materialize_inverse: false
  legacy_edge_aliases:
  - side_uses_key_column
  edge_class: canonical
  canonical_cognee_edge: true
```
```yaml
candidate_edge:
  edge_id: edge.target_plus.00480.uses_column
  canonical_edge_type: USES_COLUMN
  source_card_id: reconciliation_side.target_plus.returns_settlement.settlement
  target_card_id: column.zs_observe.target_settlement.transaction_type
  source_type: reconciliation_side
  target_type: column
  inverse_edge_type: null
  materialize_inverse: false
  legacy_edge_aliases:
  - side_uses_key_column
  edge_class: canonical
  canonical_cognee_edge: true
```
```yaml
candidate_edge:
  edge_id: edge.target_plus.00481.uses_column
  canonical_edge_type: USES_COLUMN
  source_card_id: reconciliation_side.target_plus.returns_settlement.settlement
  target_card_id: column.zs_observe.target_settlement.internal_txn_type
  source_type: reconciliation_side
  target_type: column
  inverse_edge_type: null
  materialize_inverse: false
  legacy_edge_aliases:
  - side_uses_key_column
  edge_class: canonical
  canonical_cognee_edge: true
```
```yaml
candidate_edge:
  edge_id: edge.target_plus.00482.mismatch_of_profile
  canonical_edge_type: MISMATCH_OF_PROFILE
  source_card_id: mismatch_category.target_plus.returns_settlement.refund_pending
  target_card_id: reconciliation_profile.target_plus.returns_settlement
  source_type: mismatch_category
  target_type: reconciliation_profile
  inverse_edge_type: HAS_MISMATCH_CATEGORY
  materialize_inverse: true
  legacy_edge_aliases: []
  edge_class: canonical
  canonical_cognee_edge: true
```
```yaml
candidate_edge:
  edge_id: edge.target_plus.00483.has_mismatch_category
  canonical_edge_type: HAS_MISMATCH_CATEGORY
  source_card_id: reconciliation_profile.target_plus.returns_settlement
  target_card_id: mismatch_category.target_plus.returns_settlement.refund_pending
  source_type: reconciliation_profile
  target_type: mismatch_category
  inverse_edge_type: MISMATCH_OF_PROFILE
  materialize_inverse: false
  legacy_edge_aliases:
  - profile_has_mismatch_category
  edge_class: canonical
  canonical_cognee_edge: true
```
```yaml
candidate_edge:
  edge_id: edge.target_plus.00484.mismatch_of_profile
  canonical_edge_type: MISMATCH_OF_PROFILE
  source_card_id: mismatch_category.target_plus.returns_settlement.refund_settled
  target_card_id: reconciliation_profile.target_plus.returns_settlement
  source_type: mismatch_category
  target_type: reconciliation_profile
  inverse_edge_type: HAS_MISMATCH_CATEGORY
  materialize_inverse: true
  legacy_edge_aliases: []
  edge_class: canonical
  canonical_cognee_edge: true
```
```yaml
candidate_edge:
  edge_id: edge.target_plus.00485.has_mismatch_category
  canonical_edge_type: HAS_MISMATCH_CATEGORY
  source_card_id: reconciliation_profile.target_plus.returns_settlement
  target_card_id: mismatch_category.target_plus.returns_settlement.refund_settled
  source_type: reconciliation_profile
  target_type: mismatch_category
  inverse_edge_type: MISMATCH_OF_PROFILE
  materialize_inverse: false
  legacy_edge_aliases:
  - profile_has_mismatch_category
  edge_class: canonical
  canonical_cognee_edge: true
```
```yaml
candidate_edge:
  edge_id: edge.target_plus.00486.belongs_to_domain
  canonical_edge_type: BELONGS_TO_DOMAIN
  source_card_id: reconciliation_profile.target_plus.commission_validation
  target_card_id: domain.target_plus.reconciliation
  source_type: reconciliation_profile
  target_type: domain
  inverse_edge_type: null
  materialize_inverse: false
  legacy_edge_aliases: []
  edge_class: canonical
  canonical_cognee_edge: true
```
```yaml
candidate_edge:
  edge_id: edge.target_plus.00487.has_primary_unit
  canonical_edge_type: HAS_PRIMARY_UNIT
  source_card_id: reconciliation_profile.target_plus.commission_validation
  target_card_id: reconciliation_unit.target_plus.item_id_line
  source_type: reconciliation_profile
  target_type: reconciliation_unit
  inverse_edge_type: null
  materialize_inverse: false
  legacy_edge_aliases:
  - profile_uses_unit
  edge_class: canonical
  canonical_cognee_edge: true
```
```yaml
candidate_edge:
  edge_id: edge.target_plus.00488.uses_matching_logic
  canonical_edge_type: USES_MATCHING_LOGIC
  source_card_id: reconciliation_profile.target_plus.commission_validation
  target_card_id: matching_logic.target_plus.commission_15pct
  source_type: reconciliation_profile
  target_type: matching_logic
  inverse_edge_type: SUPPORTS_RECONCILIATION_PROFILE
  materialize_inverse: true
  legacy_edge_aliases:
  - profile_uses_matching_logic
  edge_class: canonical
  canonical_cognee_edge: true
```
```yaml
candidate_edge:
  edge_id: edge.target_plus.00489.belongs_to_reconciliation_profile
  canonical_edge_type: BELONGS_TO_RECONCILIATION_PROFILE
  source_card_id: reconciliation_side.target_plus.commission_validation.settlement_expected
  target_card_id: reconciliation_profile.target_plus.commission_validation
  source_type: reconciliation_side
  target_type: reconciliation_profile
  inverse_edge_type: HAS_RECONCILIATION_SIDE
  materialize_inverse: true
  legacy_edge_aliases: []
  edge_class: canonical
  canonical_cognee_edge: true
```
```yaml
candidate_edge:
  edge_id: edge.target_plus.00490.has_reconciliation_side
  canonical_edge_type: HAS_RECONCILIATION_SIDE
  source_card_id: reconciliation_profile.target_plus.commission_validation
  target_card_id: reconciliation_side.target_plus.commission_validation.settlement_expected
  source_type: reconciliation_profile
  target_type: reconciliation_side
  inverse_edge_type: BELONGS_TO_RECONCILIATION_PROFILE
  materialize_inverse: true
  legacy_edge_aliases:
  - profile_expected_side
  edge_class: canonical
  canonical_cognee_edge: true
```
```yaml
candidate_edge:
  edge_id: edge.target_plus.00491.uses_table
  canonical_edge_type: USES_TABLE
  source_card_id: reconciliation_side.target_plus.commission_validation.settlement_expected
  target_card_id: table.zs_observe.target_settlement
  source_type: reconciliation_side
  target_type: table
  inverse_edge_type: null
  materialize_inverse: false
  legacy_edge_aliases:
  - side_uses_table
  edge_class: canonical
  canonical_cognee_edge: true
```
```yaml
candidate_edge:
  edge_id: edge.target_plus.00492.uses_column
  canonical_edge_type: USES_COLUMN
  source_card_id: reconciliation_side.target_plus.commission_validation.settlement_expected
  target_card_id: column.zs_observe.target_settlement.item_id
  source_type: reconciliation_side
  target_type: column
  inverse_edge_type: null
  materialize_inverse: false
  legacy_edge_aliases:
  - side_uses_key_column
  edge_class: canonical
  canonical_cognee_edge: true
```
```yaml
candidate_edge:
  edge_id: edge.target_plus.00493.uses_column
  canonical_edge_type: USES_COLUMN
  source_card_id: reconciliation_side.target_plus.commission_validation.settlement_expected
  target_card_id: column.zs_observe.target_settlement.transfer_id
  source_type: reconciliation_side
  target_type: column
  inverse_edge_type: null
  materialize_inverse: false
  legacy_edge_aliases:
  - side_uses_key_column
  edge_class: canonical
  canonical_cognee_edge: true
```
```yaml
candidate_edge:
  edge_id: edge.target_plus.00494.uses_column
  canonical_edge_type: USES_COLUMN
  source_card_id: reconciliation_side.target_plus.commission_validation.settlement_expected
  target_card_id: column.zs_observe.target_settlement.charged_amount_excluding_tax
  source_type: reconciliation_side
  target_type: column
  inverse_edge_type: null
  materialize_inverse: false
  legacy_edge_aliases:
  - side_uses_key_column
  edge_class: canonical
  canonical_cognee_edge: true
```
```yaml
candidate_edge:
  edge_id: edge.target_plus.00495.uses_column
  canonical_edge_type: USES_COLUMN
  source_card_id: reconciliation_side.target_plus.commission_validation.settlement_expected
  target_card_id: column.zs_observe.target_settlement.created_date
  source_type: reconciliation_side
  target_type: column
  inverse_edge_type: null
  materialize_inverse: false
  legacy_edge_aliases:
  - side_uses_key_column
  edge_class: canonical
  canonical_cognee_edge: true
```
```yaml
candidate_edge:
  edge_id: edge.target_plus.00496.uses_column
  canonical_edge_type: USES_COLUMN
  source_card_id: reconciliation_side.target_plus.commission_validation.settlement_expected
  target_card_id: column.zs_observe.target_settlement.transaction_type
  source_type: reconciliation_side
  target_type: column
  inverse_edge_type: null
  materialize_inverse: false
  legacy_edge_aliases:
  - side_uses_key_column
  edge_class: canonical
  canonical_cognee_edge: true
```
```yaml
candidate_edge:
  edge_id: edge.target_plus.00497.belongs_to_reconciliation_profile
  canonical_edge_type: BELONGS_TO_RECONCILIATION_PROFILE
  source_card_id: reconciliation_side.target_plus.commission_validation.settlement_actual
  target_card_id: reconciliation_profile.target_plus.commission_validation
  source_type: reconciliation_side
  target_type: reconciliation_profile
  inverse_edge_type: HAS_RECONCILIATION_SIDE
  materialize_inverse: true
  legacy_edge_aliases: []
  edge_class: canonical
  canonical_cognee_edge: true
```
```yaml
candidate_edge:
  edge_id: edge.target_plus.00498.has_reconciliation_side
  canonical_edge_type: HAS_RECONCILIATION_SIDE
  source_card_id: reconciliation_profile.target_plus.commission_validation
  target_card_id: reconciliation_side.target_plus.commission_validation.settlement_actual
  source_type: reconciliation_profile
  target_type: reconciliation_side
  inverse_edge_type: BELONGS_TO_RECONCILIATION_PROFILE
  materialize_inverse: true
  legacy_edge_aliases:
  - profile_actual_side
  edge_class: canonical
  canonical_cognee_edge: true
```
```yaml
candidate_edge:
  edge_id: edge.target_plus.00499.uses_table
  canonical_edge_type: USES_TABLE
  source_card_id: reconciliation_side.target_plus.commission_validation.settlement_actual
  target_card_id: table.zs_observe.target_settlement
  source_type: reconciliation_side
  target_type: table
  inverse_edge_type: null
  materialize_inverse: false
  legacy_edge_aliases:
  - side_uses_table
  edge_class: canonical
  canonical_cognee_edge: true
```
```yaml
candidate_edge:
  edge_id: edge.target_plus.00500.uses_column
  canonical_edge_type: USES_COLUMN
  source_card_id: reconciliation_side.target_plus.commission_validation.settlement_actual
  target_card_id: column.zs_observe.target_settlement.item_id
  source_type: reconciliation_side
  target_type: column
  inverse_edge_type: null
  materialize_inverse: false
  legacy_edge_aliases:
  - side_uses_key_column
  edge_class: canonical
  canonical_cognee_edge: true
```
```yaml
candidate_edge:
  edge_id: edge.target_plus.00501.uses_column
  canonical_edge_type: USES_COLUMN
  source_card_id: reconciliation_side.target_plus.commission_validation.settlement_actual
  target_card_id: column.zs_observe.target_settlement.transfer_id
  source_type: reconciliation_side
  target_type: column
  inverse_edge_type: null
  materialize_inverse: false
  legacy_edge_aliases:
  - side_uses_key_column
  edge_class: canonical
  canonical_cognee_edge: true
```
```yaml
candidate_edge:
  edge_id: edge.target_plus.00502.uses_column
  canonical_edge_type: USES_COLUMN
  source_card_id: reconciliation_side.target_plus.commission_validation.settlement_actual
  target_card_id: column.zs_observe.target_settlement.gross_commission
  source_type: reconciliation_side
  target_type: column
  inverse_edge_type: null
  materialize_inverse: false
  legacy_edge_aliases:
  - side_uses_key_column
  edge_class: canonical
  canonical_cognee_edge: true
```
```yaml
candidate_edge:
  edge_id: edge.target_plus.00503.uses_column
  canonical_edge_type: USES_COLUMN
  source_card_id: reconciliation_side.target_plus.commission_validation.settlement_actual
  target_card_id: column.zs_observe.target_settlement.created_date
  source_type: reconciliation_side
  target_type: column
  inverse_edge_type: null
  materialize_inverse: false
  legacy_edge_aliases:
  - side_uses_key_column
  edge_class: canonical
  canonical_cognee_edge: true
```
```yaml
candidate_edge:
  edge_id: edge.target_plus.00504.uses_column
  canonical_edge_type: USES_COLUMN
  source_card_id: reconciliation_side.target_plus.commission_validation.settlement_actual
  target_card_id: column.zs_observe.target_settlement.transaction_type
  source_type: reconciliation_side
  target_type: column
  inverse_edge_type: null
  materialize_inverse: false
  legacy_edge_aliases:
  - side_uses_key_column
  edge_class: canonical
  canonical_cognee_edge: true
```
```yaml
candidate_edge:
  edge_id: edge.target_plus.00505.mismatch_of_profile
  canonical_edge_type: MISMATCH_OF_PROFILE
  source_card_id: mismatch_category.target_plus.commission_validation.commission_variance
  target_card_id: reconciliation_profile.target_plus.commission_validation
  source_type: mismatch_category
  target_type: reconciliation_profile
  inverse_edge_type: HAS_MISMATCH_CATEGORY
  materialize_inverse: true
  legacy_edge_aliases: []
  edge_class: canonical
  canonical_cognee_edge: true
```
```yaml
candidate_edge:
  edge_id: edge.target_plus.00506.has_mismatch_category
  canonical_edge_type: HAS_MISMATCH_CATEGORY
  source_card_id: reconciliation_profile.target_plus.commission_validation
  target_card_id: mismatch_category.target_plus.commission_validation.commission_variance
  source_type: reconciliation_profile
  target_type: mismatch_category
  inverse_edge_type: MISMATCH_OF_PROFILE
  materialize_inverse: false
  legacy_edge_aliases:
  - profile_has_mismatch_category
  edge_class: canonical
  canonical_cognee_edge: true
```
```yaml
candidate_edge:
  edge_id: edge.target_plus.00507.belongs_to_domain
  canonical_edge_type: BELONGS_TO_DOMAIN
  source_card_id: reconciliation_profile.target_plus.payout_batch
  target_card_id: domain.target_plus.reconciliation
  source_type: reconciliation_profile
  target_type: domain
  inverse_edge_type: null
  materialize_inverse: false
  legacy_edge_aliases: []
  edge_class: canonical
  canonical_cognee_edge: true
```
```yaml
candidate_edge:
  edge_id: edge.target_plus.00508.has_primary_unit
  canonical_edge_type: HAS_PRIMARY_UNIT
  source_card_id: reconciliation_profile.target_plus.payout_batch
  target_card_id: reconciliation_unit.target_plus.payout_id_batch
  source_type: reconciliation_profile
  target_type: reconciliation_unit
  inverse_edge_type: null
  materialize_inverse: false
  legacy_edge_aliases:
  - profile_uses_unit
  edge_class: canonical
  canonical_cognee_edge: true
```
```yaml
candidate_edge:
  edge_id: edge.target_plus.00509.uses_matching_logic
  canonical_edge_type: USES_MATCHING_LOGIC
  source_card_id: reconciliation_profile.target_plus.payout_batch
  target_card_id: matching_logic.target_plus.payout_batch_rollup
  source_type: reconciliation_profile
  target_type: matching_logic
  inverse_edge_type: SUPPORTS_RECONCILIATION_PROFILE
  materialize_inverse: true
  legacy_edge_aliases:
  - profile_uses_matching_logic
  edge_class: canonical
  canonical_cognee_edge: true
```
```yaml
candidate_edge:
  edge_id: edge.target_plus.00510.belongs_to_reconciliation_profile
  canonical_edge_type: BELONGS_TO_RECONCILIATION_PROFILE
  source_card_id: reconciliation_side.target_plus.payout_batch.settlement_rows
  target_card_id: reconciliation_profile.target_plus.payout_batch
  source_type: reconciliation_side
  target_type: reconciliation_profile
  inverse_edge_type: HAS_RECONCILIATION_SIDE
  materialize_inverse: true
  legacy_edge_aliases: []
  edge_class: canonical
  canonical_cognee_edge: true
```
```yaml
candidate_edge:
  edge_id: edge.target_plus.00511.has_reconciliation_side
  canonical_edge_type: HAS_RECONCILIATION_SIDE
  source_card_id: reconciliation_profile.target_plus.payout_batch
  target_card_id: reconciliation_side.target_plus.payout_batch.settlement_rows
  source_type: reconciliation_profile
  target_type: reconciliation_side
  inverse_edge_type: BELONGS_TO_RECONCILIATION_PROFILE
  materialize_inverse: true
  legacy_edge_aliases:
  - profile_actual_side
  edge_class: canonical
  canonical_cognee_edge: true
```
```yaml
candidate_edge:
  edge_id: edge.target_plus.00512.uses_table
  canonical_edge_type: USES_TABLE
  source_card_id: reconciliation_side.target_plus.payout_batch.settlement_rows
  target_card_id: table.zs_observe.target_settlement
  source_type: reconciliation_side
  target_type: table
  inverse_edge_type: null
  materialize_inverse: false
  legacy_edge_aliases:
  - side_uses_table
  edge_class: canonical
  canonical_cognee_edge: true
```
```yaml
candidate_edge:
  edge_id: edge.target_plus.00513.uses_column
  canonical_edge_type: USES_COLUMN
  source_card_id: reconciliation_side.target_plus.payout_batch.settlement_rows
  target_card_id: column.zs_observe.target_settlement.payout_id
  source_type: reconciliation_side
  target_type: column
  inverse_edge_type: null
  materialize_inverse: false
  legacy_edge_aliases:
  - side_uses_key_column
  edge_class: canonical
  canonical_cognee_edge: true
```
```yaml
candidate_edge:
  edge_id: edge.target_plus.00514.uses_column
  canonical_edge_type: USES_COLUMN
  source_card_id: reconciliation_side.target_plus.payout_batch.settlement_rows
  target_card_id: column.zs_observe.target_settlement.order_id
  source_type: reconciliation_side
  target_type: column
  inverse_edge_type: null
  materialize_inverse: false
  legacy_edge_aliases:
  - side_uses_key_column
  edge_class: canonical
  canonical_cognee_edge: true
```
```yaml
candidate_edge:
  edge_id: edge.target_plus.00515.uses_column
  canonical_edge_type: USES_COLUMN
  source_card_id: reconciliation_side.target_plus.payout_batch.settlement_rows
  target_card_id: column.zs_observe.target_settlement.settled_amount
  source_type: reconciliation_side
  target_type: column
  inverse_edge_type: null
  materialize_inverse: false
  legacy_edge_aliases:
  - side_uses_key_column
  edge_class: canonical
  canonical_cognee_edge: true
```
```yaml
candidate_edge:
  edge_id: edge.target_plus.00516.uses_column
  canonical_edge_type: USES_COLUMN
  source_card_id: reconciliation_side.target_plus.payout_batch.settlement_rows
  target_card_id: column.zs_observe.target_settlement.created_date
  source_type: reconciliation_side
  target_type: column
  inverse_edge_type: null
  materialize_inverse: false
  legacy_edge_aliases:
  - side_uses_key_column
  edge_class: canonical
  canonical_cognee_edge: true
```
```yaml
candidate_edge:
  edge_id: edge.target_plus.00517.uses_column
  canonical_edge_type: USES_COLUMN
  source_card_id: reconciliation_side.target_plus.payout_batch.settlement_rows
  target_card_id: column.zs_observe.target_settlement.transaction_type
  source_type: reconciliation_side
  target_type: column
  inverse_edge_type: null
  materialize_inverse: false
  legacy_edge_aliases:
  - side_uses_key_column
  edge_class: canonical
  canonical_cognee_edge: true
```
```yaml
candidate_edge:
  edge_id: edge.target_plus.00518.belongs_to_reconciliation_profile
  canonical_edge_type: BELONGS_TO_RECONCILIATION_PROFILE
  source_card_id: reconciliation_side.target_plus.payout_batch.batch_rollup
  target_card_id: reconciliation_profile.target_plus.payout_batch
  source_type: reconciliation_side
  target_type: reconciliation_profile
  inverse_edge_type: HAS_RECONCILIATION_SIDE
  materialize_inverse: true
  legacy_edge_aliases: []
  edge_class: canonical
  canonical_cognee_edge: true
```
```yaml
candidate_edge:
  edge_id: edge.target_plus.00519.has_reconciliation_side
  canonical_edge_type: HAS_RECONCILIATION_SIDE
  source_card_id: reconciliation_profile.target_plus.payout_batch
  target_card_id: reconciliation_side.target_plus.payout_batch.batch_rollup
  source_type: reconciliation_profile
  target_type: reconciliation_side
  inverse_edge_type: BELONGS_TO_RECONCILIATION_PROFILE
  materialize_inverse: true
  legacy_edge_aliases:
  - profile_actual_side
  edge_class: canonical
  canonical_cognee_edge: true
```
```yaml
candidate_edge:
  edge_id: edge.target_plus.00520.uses_table
  canonical_edge_type: USES_TABLE
  source_card_id: reconciliation_side.target_plus.payout_batch.batch_rollup
  target_card_id: table.zs_observe.target_settlement
  source_type: reconciliation_side
  target_type: table
  inverse_edge_type: null
  materialize_inverse: false
  legacy_edge_aliases:
  - side_uses_table
  edge_class: canonical
  canonical_cognee_edge: true
```
```yaml
candidate_edge:
  edge_id: edge.target_plus.00521.uses_column
  canonical_edge_type: USES_COLUMN
  source_card_id: reconciliation_side.target_plus.payout_batch.batch_rollup
  target_card_id: column.zs_observe.target_settlement.payout_id
  source_type: reconciliation_side
  target_type: column
  inverse_edge_type: null
  materialize_inverse: false
  legacy_edge_aliases:
  - side_uses_key_column
  edge_class: canonical
  canonical_cognee_edge: true
```
```yaml
candidate_edge:
  edge_id: edge.target_plus.00522.uses_column
  canonical_edge_type: USES_COLUMN
  source_card_id: reconciliation_side.target_plus.payout_batch.batch_rollup
  target_card_id: column.zs_observe.target_settlement.settled_amount
  source_type: reconciliation_side
  target_type: column
  inverse_edge_type: null
  materialize_inverse: false
  legacy_edge_aliases:
  - side_uses_key_column
  edge_class: canonical
  canonical_cognee_edge: true
```
```yaml
candidate_edge:
  edge_id: edge.target_plus.00523.uses_column
  canonical_edge_type: USES_COLUMN
  source_card_id: reconciliation_side.target_plus.payout_batch.batch_rollup
  target_card_id: column.zs_observe.target_settlement.created_date
  source_type: reconciliation_side
  target_type: column
  inverse_edge_type: null
  materialize_inverse: false
  legacy_edge_aliases:
  - side_uses_key_column
  edge_class: canonical
  canonical_cognee_edge: true
```
```yaml
candidate_edge:
  edge_id: edge.target_plus.00524.uses_column
  canonical_edge_type: USES_COLUMN
  source_card_id: reconciliation_side.target_plus.payout_batch.batch_rollup
  target_card_id: column.zs_observe.target_settlement.transaction_type
  source_type: reconciliation_side
  target_type: column
  inverse_edge_type: null
  materialize_inverse: false
  legacy_edge_aliases:
  - side_uses_key_column
  edge_class: canonical
  canonical_cognee_edge: true
```
```yaml
candidate_edge:
  edge_id: edge.target_plus.00525.mismatch_of_profile
  canonical_edge_type: MISMATCH_OF_PROFILE
  source_card_id: mismatch_category.target_plus.payout_batch.empty_batch
  target_card_id: reconciliation_profile.target_plus.payout_batch
  source_type: mismatch_category
  target_type: reconciliation_profile
  inverse_edge_type: HAS_MISMATCH_CATEGORY
  materialize_inverse: true
  legacy_edge_aliases: []
  edge_class: canonical
  canonical_cognee_edge: true
```
```yaml
candidate_edge:
  edge_id: edge.target_plus.00526.has_mismatch_category
  canonical_edge_type: HAS_MISMATCH_CATEGORY
  source_card_id: reconciliation_profile.target_plus.payout_batch
  target_card_id: mismatch_category.target_plus.payout_batch.empty_batch
  source_type: reconciliation_profile
  target_type: mismatch_category
  inverse_edge_type: MISMATCH_OF_PROFILE
  materialize_inverse: false
  legacy_edge_aliases:
  - profile_has_mismatch_category
  edge_class: canonical
  canonical_cognee_edge: true
```
```yaml
candidate_edge:
  edge_id: edge.target_plus.00527.belongs_to_domain
  canonical_edge_type: BELONGS_TO_DOMAIN
  source_card_id: reconciliation_profile.target_plus.tcin_mapping
  target_card_id: domain.target_plus.reconciliation
  source_type: reconciliation_profile
  target_type: domain
  inverse_edge_type: null
  materialize_inverse: false
  legacy_edge_aliases: []
  edge_class: canonical
  canonical_cognee_edge: true
```
```yaml
candidate_edge:
  edge_id: edge.target_plus.00528.has_primary_unit
  canonical_edge_type: HAS_PRIMARY_UNIT
  source_card_id: reconciliation_profile.target_plus.tcin_mapping
  target_card_id: reconciliation_unit.target_plus.tcin_product
  source_type: reconciliation_profile
  target_type: reconciliation_unit
  inverse_edge_type: null
  materialize_inverse: false
  legacy_edge_aliases:
  - profile_uses_unit
  edge_class: canonical
  canonical_cognee_edge: true
```
```yaml
candidate_edge:
  edge_id: edge.target_plus.00529.uses_matching_logic
  canonical_edge_type: USES_MATCHING_LOGIC
  source_card_id: reconciliation_profile.target_plus.tcin_mapping
  target_card_id: matching_logic.target_plus.tcin_mapping_join
  source_type: reconciliation_profile
  target_type: matching_logic
  inverse_edge_type: SUPPORTS_RECONCILIATION_PROFILE
  materialize_inverse: true
  legacy_edge_aliases:
  - profile_uses_matching_logic
  edge_class: canonical
  canonical_cognee_edge: true
```
```yaml
candidate_edge:
  edge_id: edge.target_plus.00530.belongs_to_reconciliation_profile
  canonical_edge_type: BELONGS_TO_RECONCILIATION_PROFILE
  source_card_id: reconciliation_side.target_plus.tcin_mapping.transaction_tcins
  target_card_id: reconciliation_profile.target_plus.tcin_mapping
  source_type: reconciliation_side
  target_type: reconciliation_profile
  inverse_edge_type: HAS_RECONCILIATION_SIDE
  materialize_inverse: true
  legacy_edge_aliases: []
  edge_class: canonical
  canonical_cognee_edge: true
```
```yaml
candidate_edge:
  edge_id: edge.target_plus.00531.has_reconciliation_side
  canonical_edge_type: HAS_RECONCILIATION_SIDE
  source_card_id: reconciliation_profile.target_plus.tcin_mapping
  target_card_id: reconciliation_side.target_plus.tcin_mapping.transaction_tcins
  source_type: reconciliation_profile
  target_type: reconciliation_side
  inverse_edge_type: BELONGS_TO_RECONCILIATION_PROFILE
  materialize_inverse: true
  legacy_edge_aliases:
  - profile_expected_side
  edge_class: canonical
  canonical_cognee_edge: true
```
```yaml
candidate_edge:
  edge_id: edge.target_plus.00532.uses_table
  canonical_edge_type: USES_TABLE
  source_card_id: reconciliation_side.target_plus.tcin_mapping.transaction_tcins
  target_card_id: table.zs_observe.target_sales
  source_type: reconciliation_side
  target_type: table
  inverse_edge_type: null
  materialize_inverse: false
  legacy_edge_aliases:
  - side_uses_table
  edge_class: canonical
  canonical_cognee_edge: true
```
```yaml
candidate_edge:
  edge_id: edge.target_plus.00533.uses_column
  canonical_edge_type: USES_COLUMN
  source_card_id: reconciliation_side.target_plus.tcin_mapping.transaction_tcins
  target_card_id: column.zs_observe.target_sales.tcin
  source_type: reconciliation_side
  target_type: column
  inverse_edge_type: null
  materialize_inverse: false
  legacy_edge_aliases:
  - side_uses_key_column
  edge_class: canonical
  canonical_cognee_edge: true
```
```yaml
candidate_edge:
  edge_id: edge.target_plus.00534.uses_column
  canonical_edge_type: USES_COLUMN
  source_card_id: reconciliation_side.target_plus.tcin_mapping.transaction_tcins
  target_card_id: column.zs_observe.target_sales.charged_amount
  source_type: reconciliation_side
  target_type: column
  inverse_edge_type: null
  materialize_inverse: false
  legacy_edge_aliases:
  - side_uses_key_column
  edge_class: canonical
  canonical_cognee_edge: true
```
```yaml
candidate_edge:
  edge_id: edge.target_plus.00535.uses_column
  canonical_edge_type: USES_COLUMN
  source_card_id: reconciliation_side.target_plus.tcin_mapping.transaction_tcins
  target_card_id: column.zs_observe.target_sales.created_date
  source_type: reconciliation_side
  target_type: column
  inverse_edge_type: null
  materialize_inverse: false
  legacy_edge_aliases:
  - side_uses_key_column
  edge_class: canonical
  canonical_cognee_edge: true
```
```yaml
candidate_edge:
  edge_id: edge.target_plus.00536.uses_column
  canonical_edge_type: USES_COLUMN
  source_card_id: reconciliation_side.target_plus.tcin_mapping.transaction_tcins
  target_card_id: column.zs_observe.target_sales.order_status
  source_type: reconciliation_side
  target_type: column
  inverse_edge_type: null
  materialize_inverse: false
  legacy_edge_aliases:
  - side_uses_key_column
  edge_class: canonical
  canonical_cognee_edge: true
```
```yaml
candidate_edge:
  edge_id: edge.target_plus.00537.belongs_to_reconciliation_profile
  canonical_edge_type: BELONGS_TO_RECONCILIATION_PROFILE
  source_card_id: reconciliation_side.target_plus.tcin_mapping.mapping
  target_card_id: reconciliation_profile.target_plus.tcin_mapping
  source_type: reconciliation_side
  target_type: reconciliation_profile
  inverse_edge_type: HAS_RECONCILIATION_SIDE
  materialize_inverse: true
  legacy_edge_aliases: []
  edge_class: canonical
  canonical_cognee_edge: true
```
```yaml
candidate_edge:
  edge_id: edge.target_plus.00538.has_reconciliation_side
  canonical_edge_type: HAS_RECONCILIATION_SIDE
  source_card_id: reconciliation_profile.target_plus.tcin_mapping
  target_card_id: reconciliation_side.target_plus.tcin_mapping.mapping
  source_type: reconciliation_profile
  target_type: reconciliation_side
  inverse_edge_type: BELONGS_TO_RECONCILIATION_PROFILE
  materialize_inverse: true
  legacy_edge_aliases:
  - profile_actual_side
  edge_class: canonical
  canonical_cognee_edge: true
```
```yaml
candidate_edge:
  edge_id: edge.target_plus.00539.uses_table
  canonical_edge_type: USES_TABLE
  source_card_id: reconciliation_side.target_plus.tcin_mapping.mapping
  target_card_id: table.zs_observe.target_tcin_mapping
  source_type: reconciliation_side
  target_type: table
  inverse_edge_type: null
  materialize_inverse: false
  legacy_edge_aliases:
  - side_uses_table
  edge_class: canonical
  canonical_cognee_edge: true
```
```yaml
candidate_edge:
  edge_id: edge.target_plus.00540.uses_column
  canonical_edge_type: USES_COLUMN
  source_card_id: reconciliation_side.target_plus.tcin_mapping.mapping
  target_card_id: column.zs_observe.target_tcin_mapping.tcin
  source_type: reconciliation_side
  target_type: column
  inverse_edge_type: null
  materialize_inverse: false
  legacy_edge_aliases:
  - side_uses_key_column
  edge_class: canonical
  canonical_cognee_edge: true
```
```yaml
candidate_edge:
  edge_id: edge.target_plus.00541.uses_column
  canonical_edge_type: USES_COLUMN
  source_card_id: reconciliation_side.target_plus.tcin_mapping.mapping
  target_card_id: column.zs_observe.target_tcin_mapping.sku_id
  source_type: reconciliation_side
  target_type: column
  inverse_edge_type: null
  materialize_inverse: false
  legacy_edge_aliases:
  - side_uses_key_column
  edge_class: canonical
  canonical_cognee_edge: true
```
```yaml
candidate_edge:
  edge_id: edge.target_plus.00542.uses_column
  canonical_edge_type: USES_COLUMN
  source_card_id: reconciliation_side.target_plus.tcin_mapping.mapping
  target_card_id: column.zs_observe.target_tcin_mapping.asin
  source_type: reconciliation_side
  target_type: column
  inverse_edge_type: null
  materialize_inverse: false
  legacy_edge_aliases:
  - side_uses_key_column
  edge_class: canonical
  canonical_cognee_edge: true
```
```yaml
candidate_edge:
  edge_id: edge.target_plus.00543.uses_column
  canonical_edge_type: USES_COLUMN
  source_card_id: reconciliation_side.target_plus.tcin_mapping.mapping
  target_card_id: column.zs_observe.target_tcin_mapping.brand
  source_type: reconciliation_side
  target_type: column
  inverse_edge_type: null
  materialize_inverse: false
  legacy_edge_aliases:
  - side_uses_key_column
  edge_class: canonical
  canonical_cognee_edge: true
```
```yaml
candidate_edge:
  edge_id: edge.target_plus.00544.mismatch_of_profile
  canonical_edge_type: MISMATCH_OF_PROFILE
  source_card_id: mismatch_category.target_plus.tcin_mapping.missing_mapping
  target_card_id: reconciliation_profile.target_plus.tcin_mapping
  source_type: mismatch_category
  target_type: reconciliation_profile
  inverse_edge_type: HAS_MISMATCH_CATEGORY
  materialize_inverse: true
  legacy_edge_aliases: []
  edge_class: canonical
  canonical_cognee_edge: true
```
```yaml
candidate_edge:
  edge_id: edge.target_plus.00545.has_mismatch_category
  canonical_edge_type: HAS_MISMATCH_CATEGORY
  source_card_id: reconciliation_profile.target_plus.tcin_mapping
  target_card_id: mismatch_category.target_plus.tcin_mapping.missing_mapping
  source_type: reconciliation_profile
  target_type: mismatch_category
  inverse_edge_type: MISMATCH_OF_PROFILE
  materialize_inverse: false
  legacy_edge_aliases:
  - profile_has_mismatch_category
  edge_class: canonical
  canonical_cognee_edge: true
```
```yaml
candidate_edge:
  edge_id: edge.target_plus.00546.applies_to_platform_context
  canonical_edge_type: APPLIES_TO_PLATFORM_CONTEXT
  source_card_id: reconciliation_unit.target_plus.order_id_order
  target_card_id: platform_context.target_plus.us
  source_type: reconciliation_unit
  target_type: platform_context
  inverse_edge_type: null
  materialize_inverse: false
  legacy_edge_aliases: []
  edge_class: canonical
  canonical_cognee_edge: true
```
```yaml
candidate_edge:
  edge_id: edge.target_plus.00547.applies_to_card
  canonical_edge_type: APPLIES_TO_CARD
  source_card_id: rule.target_plus.marketplace_boundary
  target_card_id: platform.target_plus
  source_type: rule
  target_type: platform
  inverse_edge_type: null
  materialize_inverse: false
  legacy_edge_aliases: []
  edge_class: canonical
  canonical_cognee_edge: true
```
```yaml
candidate_edge:
  edge_id: edge.target_plus.00548.applies_to_card
  canonical_edge_type: APPLIES_TO_CARD
  source_card_id: rule.target_plus.scope_group_123
  target_card_id: table.zs_observe.target_sales
  source_type: rule
  target_type: table
  inverse_edge_type: null
  materialize_inverse: false
  legacy_edge_aliases: []
  edge_class: canonical
  canonical_cognee_edge: true
```
```yaml
candidate_edge:
  edge_id: edge.target_plus.00549.applies_to_card
  canonical_edge_type: APPLIES_TO_CARD
  source_card_id: rule.target_plus.scope_group_123
  target_card_id: table.zs_observe.target_returns
  source_type: rule
  target_type: table
  inverse_edge_type: null
  materialize_inverse: false
  legacy_edge_aliases: []
  edge_class: canonical
  canonical_cognee_edge: true
```
```yaml
candidate_edge:
  edge_id: edge.target_plus.00550.applies_to_card
  canonical_edge_type: APPLIES_TO_CARD
  source_card_id: rule.target_plus.scope_group_123
  target_card_id: table.zs_observe.target_settlement
  source_type: rule
  target_type: table
  inverse_edge_type: null
  materialize_inverse: false
  legacy_edge_aliases: []
  edge_class: canonical
  canonical_cognee_edge: true
```
```yaml
candidate_edge:
  edge_id: edge.target_plus.00551.applies_to_card
  canonical_edge_type: APPLIES_TO_CARD
  source_card_id: rule.target_plus.scope_group_123
  target_card_id: table.zs_observe.target_tcin_mapping
  source_type: rule
  target_type: table
  inverse_edge_type: null
  materialize_inverse: false
  legacy_edge_aliases: []
  edge_class: canonical
  canonical_cognee_edge: true
```
```yaml
candidate_edge:
  edge_id: edge.target_plus.00552.applies_to_card
  canonical_edge_type: APPLIES_TO_CARD
  source_card_id: rule.target_plus.active_filter
  target_card_id: table.zs_observe.target_sales
  source_type: rule
  target_type: table
  inverse_edge_type: null
  materialize_inverse: false
  legacy_edge_aliases: []
  edge_class: canonical
  canonical_cognee_edge: true
```
```yaml
candidate_edge:
  edge_id: edge.target_plus.00553.applies_to_card
  canonical_edge_type: APPLIES_TO_CARD
  source_card_id: rule.target_plus.active_filter
  target_card_id: table.zs_observe.target_returns
  source_type: rule
  target_type: table
  inverse_edge_type: null
  materialize_inverse: false
  legacy_edge_aliases: []
  edge_class: canonical
  canonical_cognee_edge: true
```
```yaml
candidate_edge:
  edge_id: edge.target_plus.00554.applies_to_card
  canonical_edge_type: APPLIES_TO_CARD
  source_card_id: rule.target_plus.active_filter
  target_card_id: table.zs_observe.target_settlement
  source_type: rule
  target_type: table
  inverse_edge_type: null
  materialize_inverse: false
  legacy_edge_aliases: []
  edge_class: canonical
  canonical_cognee_edge: true
```
```yaml
candidate_edge:
  edge_id: edge.target_plus.00555.applies_to_card
  canonical_edge_type: APPLIES_TO_CARD
  source_card_id: rule.target_plus.active_filter
  target_card_id: table.zs_observe.target_tcin_mapping
  source_type: rule
  target_type: table
  inverse_edge_type: null
  materialize_inverse: false
  legacy_edge_aliases: []
  edge_class: canonical
  canonical_cognee_edge: true
```
```yaml
candidate_edge:
  edge_id: edge.target_plus.00556.applies_to_card
  canonical_edge_type: APPLIES_TO_CARD
  source_card_id: rule.target_plus.sales_shipped_filter
  target_card_id: table.zs_observe.target_sales
  source_type: rule
  target_type: table
  inverse_edge_type: null
  materialize_inverse: false
  legacy_edge_aliases: []
  edge_class: canonical
  canonical_cognee_edge: true
```
```yaml
candidate_edge:
  edge_id: edge.target_plus.00557.applies_to_card
  canonical_edge_type: APPLIES_TO_CARD
  source_card_id: rule.target_plus.sales_shipped_filter
  target_card_id: metric.target_plus.total_gmv
  source_type: rule
  target_type: metric
  inverse_edge_type: null
  materialize_inverse: false
  legacy_edge_aliases: []
  edge_class: canonical
  canonical_cognee_edge: true
```
```yaml
candidate_edge:
  edge_id: edge.target_plus.00558.applies_to_card
  canonical_edge_type: APPLIES_TO_CARD
  source_card_id: rule.target_plus.settlement_forward_filter
  target_card_id: table.zs_observe.target_settlement
  source_type: rule
  target_type: table
  inverse_edge_type: null
  materialize_inverse: false
  legacy_edge_aliases: []
  edge_class: canonical
  canonical_cognee_edge: true
```
```yaml
candidate_edge:
  edge_id: edge.target_plus.00559.applies_to_card
  canonical_edge_type: APPLIES_TO_CARD
  source_card_id: rule.target_plus.settlement_forward_filter
  target_card_id: metric.target_plus.effective_payout_rate
  source_type: rule
  target_type: metric
  inverse_edge_type: null
  materialize_inverse: false
  legacy_edge_aliases: []
  edge_class: canonical
  canonical_cognee_edge: true
```
```yaml
candidate_edge:
  edge_id: edge.target_plus.00560.applies_to_card
  canonical_edge_type: APPLIES_TO_CARD
  source_card_id: rule.target_plus.returns_confirmed_filter
  target_card_id: table.zs_observe.target_returns
  source_type: rule
  target_type: table
  inverse_edge_type: null
  materialize_inverse: false
  legacy_edge_aliases: []
  edge_class: canonical
  canonical_cognee_edge: true
```
```yaml
candidate_edge:
  edge_id: edge.target_plus.00561.applies_to_card
  canonical_edge_type: APPLIES_TO_CARD
  source_card_id: rule.target_plus.returns_confirmed_filter
  target_card_id: metric.target_plus.return_reason_value
  source_type: rule
  target_type: metric
  inverse_edge_type: null
  materialize_inverse: false
  legacy_edge_aliases: []
  edge_class: canonical
  canonical_cognee_edge: true
```
```yaml
candidate_edge:
  edge_id: edge.target_plus.00562.applies_to_card
  canonical_edge_type: APPLIES_TO_CARD
  source_card_id: rule.target_plus.currency_label_usd_values
  target_card_id: table.zs_observe.target_sales
  source_type: rule
  target_type: table
  inverse_edge_type: null
  materialize_inverse: false
  legacy_edge_aliases: []
  edge_class: canonical
  canonical_cognee_edge: true
```
```yaml
candidate_edge:
  edge_id: edge.target_plus.00563.applies_to_card
  canonical_edge_type: APPLIES_TO_CARD
  source_card_id: rule.target_plus.currency_label_usd_values
  target_card_id: table.zs_observe.target_returns
  source_type: rule
  target_type: table
  inverse_edge_type: null
  materialize_inverse: false
  legacy_edge_aliases: []
  edge_class: canonical
  canonical_cognee_edge: true
```
```yaml
candidate_edge:
  edge_id: edge.target_plus.00564.applies_to_card
  canonical_edge_type: APPLIES_TO_CARD
  source_card_id: rule.target_plus.currency_label_usd_values
  target_card_id: table.zs_observe.target_settlement
  source_type: rule
  target_type: table
  inverse_edge_type: null
  materialize_inverse: false
  legacy_edge_aliases: []
  edge_class: canonical
  canonical_cognee_edge: true
```
```yaml
candidate_edge:
  edge_id: edge.target_plus.00565.applies_to_card
  canonical_edge_type: APPLIES_TO_CARD
  source_card_id: rule.target_plus.currency_label_usd_values
  target_card_id: table.zs_observe.target_tcin_mapping
  source_type: rule
  target_type: table
  inverse_edge_type: null
  materialize_inverse: false
  legacy_edge_aliases: []
  edge_class: canonical
  canonical_cognee_edge: true
```
```yaml
candidate_edge:
  edge_id: edge.target_plus.00566.applies_to_card
  canonical_edge_type: APPLIES_TO_CARD
  source_card_id: rule.target_plus.settlement_recency_gap
  target_card_id: reconciliation_profile.target_plus.sales_settlement
  source_type: rule
  target_type: reconciliation_profile
  inverse_edge_type: null
  materialize_inverse: false
  legacy_edge_aliases: []
  edge_class: canonical
  canonical_cognee_edge: true
```
```yaml
candidate_edge:
  edge_id: edge.target_plus.00567.applies_to_card
  canonical_edge_type: APPLIES_TO_CARD
  source_card_id: rule.target_plus.charged_amount_excluding_tax
  target_card_id: table.zs_observe.target_settlement
  source_type: rule
  target_type: table
  inverse_edge_type: null
  materialize_inverse: false
  legacy_edge_aliases: []
  edge_class: canonical
  canonical_cognee_edge: true
```
```yaml
candidate_edge:
  edge_id: edge.target_plus.00568.applies_to_card
  canonical_edge_type: APPLIES_TO_CARD
  source_card_id: rule.target_plus.charged_amount_excluding_tax
  target_card_id: metric.target_plus.effective_payout_rate
  source_type: rule
  target_type: metric
  inverse_edge_type: null
  materialize_inverse: false
  legacy_edge_aliases: []
  edge_class: canonical
  canonical_cognee_edge: true
```
```yaml
candidate_edge:
  edge_id: edge.target_plus.00569.applies_to_card
  canonical_edge_type: APPLIES_TO_CARD
  source_card_id: rule.target_plus.brand_case_normalization
  target_card_id: value_profile.target_plus.mapping.brand_case
  source_type: rule
  target_type: value_profile
  inverse_edge_type: null
  materialize_inverse: false
  legacy_edge_aliases: []
  edge_class: canonical
  canonical_cognee_edge: true
```
```yaml
candidate_edge:
  edge_id: edge.target_plus.00570.applies_to_card
  canonical_edge_type: APPLIES_TO_CARD
  source_card_id: rule.target_plus.tcin_mapping_join
  target_card_id: relationship.target_plus.sales_mapping.tcin
  source_type: rule
  target_type: relationship
  inverse_edge_type: null
  materialize_inverse: false
  legacy_edge_aliases: []
  edge_class: canonical
  canonical_cognee_edge: true
```
```yaml
candidate_edge:
  edge_id: edge.target_plus.00571.applies_to_card
  canonical_edge_type: APPLIES_TO_CARD
  source_card_id: rule.target_plus.tcin_mapping_join
  target_card_id: relationship.target_plus.settlement_mapping.tcin
  source_type: rule
  target_type: relationship
  inverse_edge_type: null
  materialize_inverse: false
  legacy_edge_aliases: []
  edge_class: canonical
  canonical_cognee_edge: true
```
```yaml
candidate_edge:
  edge_id: edge.target_plus.00572.applies_to_card
  canonical_edge_type: APPLIES_TO_CARD
  source_card_id: rule.target_plus.tcin_mapping_join
  target_card_id: relationship.target_plus.returns_mapping.tcin
  source_type: rule
  target_type: relationship
  inverse_edge_type: null
  materialize_inverse: false
  legacy_edge_aliases: []
  edge_class: canonical
  canonical_cognee_edge: true
```
```yaml
candidate_edge:
  edge_id: edge.target_plus.00573.applies_to_card
  canonical_edge_type: APPLIES_TO_CARD
  source_card_id: rule.target_plus.reverse_charge_not_return
  target_card_id: table.zs_observe.target_settlement
  source_type: rule
  target_type: table
  inverse_edge_type: null
  materialize_inverse: false
  legacy_edge_aliases: []
  edge_class: canonical
  canonical_cognee_edge: true
```
```yaml
candidate_edge:
  edge_id: edge.target_plus.00574.applies_to_card
  canonical_edge_type: APPLIES_TO_CARD
  source_card_id: rule.target_plus.reverse_charge_not_return
  target_card_id: business_process.target_plus.reverse_charge_flow
  source_type: rule
  target_type: business_process
  inverse_edge_type: null
  materialize_inverse: false
  legacy_edge_aliases: []
  edge_class: canonical
  canonical_cognee_edge: true
```
```yaml
candidate_edge:
  edge_id: edge.target_plus.00575.applies_to_card
  canonical_edge_type: APPLIES_TO_CARD
  source_card_id: rule.target_plus.total_tax_zero
  target_card_id: column.zs_observe.target_settlement.total_tax
  source_type: rule
  target_type: column
  inverse_edge_type: null
  materialize_inverse: false
  legacy_edge_aliases: []
  edge_class: canonical
  canonical_cognee_edge: true
```
```yaml
candidate_edge:
  edge_id: edge.target_plus.00576.applies_to_card
  canonical_edge_type: APPLIES_TO_CARD
  source_card_id: rule.target_plus.total_tax_zero
  target_card_id: value_profile.target_plus.settlement.total_tax_zero
  source_type: rule
  target_type: value_profile
  inverse_edge_type: null
  materialize_inverse: false
  legacy_edge_aliases: []
  edge_class: canonical
  canonical_cognee_edge: true
```
```yaml
candidate_edge:
  edge_id: edge.target_plus.00577.applies_to_card
  canonical_edge_type: APPLIES_TO_CARD
  source_card_id: rule.target_plus.no_indian_tcs_tds
  target_card_id: domain.target_plus.tax
  source_type: rule
  target_type: domain
  inverse_edge_type: null
  materialize_inverse: false
  legacy_edge_aliases: []
  edge_class: canonical
  canonical_cognee_edge: true
```
```yaml
candidate_edge:
  edge_id: edge.target_plus.00578.applies_to_card
  canonical_edge_type: APPLIES_TO_CARD
  source_card_id: rule.target_plus.no_indian_tcs_tds
  target_card_id: platform_context.target_plus.us
  source_type: rule
  target_type: platform_context
  inverse_edge_type: null
  materialize_inverse: false
  legacy_edge_aliases: []
  edge_class: canonical
  canonical_cognee_edge: true
```
```yaml
candidate_edge:
  edge_id: edge.target_plus.00579.applies_to_card
  canonical_edge_type: APPLIES_TO_CARD
  source_card_id: rule.target_plus.barcode_formatting
  target_card_id: column.zs_observe.target_tcin_mapping.barcode
  source_type: rule
  target_type: column
  inverse_edge_type: null
  materialize_inverse: false
  legacy_edge_aliases: []
  edge_class: canonical
  canonical_cognee_edge: true
```
```yaml
candidate_edge:
  edge_id: edge.target_plus.00580.applies_to_card
  canonical_edge_type: APPLIES_TO_CARD
  source_card_id: rule.target_plus.barcode_formatting
  target_card_id: value_profile.target_plus.mapping.barcode_coverage
  source_type: rule
  target_type: value_profile
  inverse_edge_type: null
  materialize_inverse: false
  legacy_edge_aliases: []
  edge_class: canonical
  canonical_cognee_edge: true
```
```yaml
candidate_edge:
  edge_id: edge.target_plus.00581.applies_to_card
  canonical_edge_type: APPLIES_TO_CARD
  source_card_id: rule.target_plus.settlement_description_ignore
  target_card_id: column.zs_observe.target_settlement.description
  source_type: rule
  target_type: column
  inverse_edge_type: null
  materialize_inverse: false
  legacy_edge_aliases: []
  edge_class: canonical
  canonical_cognee_edge: true
```
```yaml
candidate_edge:
  edge_id: edge.target_plus.00582.applies_to_card
  canonical_edge_type: APPLIES_TO_CARD
  source_card_id: rule.target_plus.settlement_description_ignore
  target_card_id: column.zs_observe.target_settlement.transaction_type
  source_type: rule
  target_type: column
  inverse_edge_type: null
  materialize_inverse: false
  legacy_edge_aliases: []
  edge_class: canonical
  canonical_cognee_edge: true
```
```yaml
candidate_edge:
  edge_id: edge.target_plus.00583.applies_to_card
  canonical_edge_type: APPLIES_TO_CARD
  source_card_id: rule.target_plus.stripe_identifiers_columns_only
  target_card_id: value_profile.target_plus.settlement.stripe_id_formats
  source_type: rule
  target_type: value_profile
  inverse_edge_type: null
  materialize_inverse: false
  legacy_edge_aliases: []
  edge_class: canonical
  canonical_cognee_edge: true
```
```yaml
candidate_edge:
  edge_id: edge.target_plus.00584.applies_to_card
  canonical_edge_type: APPLIES_TO_CARD
  source_card_id: rule.target_plus.stripe_identifiers_columns_only
  target_card_id: domain.target_plus.payment
  source_type: rule
  target_type: domain
  inverse_edge_type: null
  materialize_inverse: false
  legacy_edge_aliases: []
  edge_class: canonical
  canonical_cognee_edge: true
```
```yaml
candidate_edge:
  edge_id: edge.target_plus.00585.applies_to_card
  canonical_edge_type: APPLIES_TO_CARD
  source_card_id: rule.target_plus.external_logistics_boundary
  target_card_id: domain.target_plus.fulfillment
  source_type: rule
  target_type: domain
  inverse_edge_type: null
  materialize_inverse: false
  legacy_edge_aliases: []
  edge_class: canonical
  canonical_cognee_edge: true
```
```yaml
candidate_edge:
  edge_id: edge.target_plus.00586.applies_to_card
  canonical_edge_type: APPLIES_TO_CARD
  source_card_id: rule.target_plus.external_logistics_boundary
  target_card_id: business_process.target_plus.return_flow
  source_type: rule
  target_type: business_process
  inverse_edge_type: null
  materialize_inverse: false
  legacy_edge_aliases: []
  edge_class: canonical
  canonical_cognee_edge: true
```
```yaml
candidate_edge:
  edge_id: edge.target_plus.00587.applies_to_card
  canonical_edge_type: APPLIES_TO_CARD
  source_card_id: rule.target_plus.one_row_per_event
  target_card_id: table.zs_observe.target_settlement
  source_type: rule
  target_type: table
  inverse_edge_type: null
  materialize_inverse: false
  legacy_edge_aliases: []
  edge_class: canonical
  canonical_cognee_edge: true
```
```yaml
candidate_edge:
  edge_id: edge.target_plus.00588.validates_card
  canonical_edge_type: VALIDATES_CARD
  source_card_id: validation_test.target_plus.active_filter
  target_card_id: table.zs_observe.target_sales
  source_type: validation_test
  target_type: table
  inverse_edge_type: null
  materialize_inverse: false
  legacy_edge_aliases: []
  edge_class: canonical
  canonical_cognee_edge: true
```
```yaml
candidate_edge:
  edge_id: edge.target_plus.00589.validates_card
  canonical_edge_type: VALIDATES_CARD
  source_card_id: validation_test.target_plus.active_filter
  target_card_id: table.zs_observe.target_returns
  source_type: validation_test
  target_type: table
  inverse_edge_type: null
  materialize_inverse: false
  legacy_edge_aliases: []
  edge_class: canonical
  canonical_cognee_edge: true
```
```yaml
candidate_edge:
  edge_id: edge.target_plus.00590.validates_card
  canonical_edge_type: VALIDATES_CARD
  source_card_id: validation_test.target_plus.active_filter
  target_card_id: table.zs_observe.target_settlement
  source_type: validation_test
  target_type: table
  inverse_edge_type: null
  materialize_inverse: false
  legacy_edge_aliases: []
  edge_class: canonical
  canonical_cognee_edge: true
```
```yaml
candidate_edge:
  edge_id: edge.target_plus.00591.validates_card
  canonical_edge_type: VALIDATES_CARD
  source_card_id: validation_test.target_plus.active_filter
  target_card_id: table.zs_observe.target_tcin_mapping
  source_type: validation_test
  target_type: table
  inverse_edge_type: null
  materialize_inverse: false
  legacy_edge_aliases: []
  edge_class: canonical
  canonical_cognee_edge: true
```
```yaml
candidate_edge:
  edge_id: edge.target_plus.00592.validates_card
  canonical_edge_type: VALIDATES_CARD
  source_card_id: validation_test.target_plus.scope_group_123
  target_card_id: table.zs_observe.target_sales
  source_type: validation_test
  target_type: table
  inverse_edge_type: null
  materialize_inverse: false
  legacy_edge_aliases: []
  edge_class: canonical
  canonical_cognee_edge: true
```
```yaml
candidate_edge:
  edge_id: edge.target_plus.00593.validates_card
  canonical_edge_type: VALIDATES_CARD
  source_card_id: validation_test.target_plus.scope_group_123
  target_card_id: table.zs_observe.target_returns
  source_type: validation_test
  target_type: table
  inverse_edge_type: null
  materialize_inverse: false
  legacy_edge_aliases: []
  edge_class: canonical
  canonical_cognee_edge: true
```
```yaml
candidate_edge:
  edge_id: edge.target_plus.00594.validates_card
  canonical_edge_type: VALIDATES_CARD
  source_card_id: validation_test.target_plus.scope_group_123
  target_card_id: table.zs_observe.target_settlement
  source_type: validation_test
  target_type: table
  inverse_edge_type: null
  materialize_inverse: false
  legacy_edge_aliases: []
  edge_class: canonical
  canonical_cognee_edge: true
```
```yaml
candidate_edge:
  edge_id: edge.target_plus.00595.validates_card
  canonical_edge_type: VALIDATES_CARD
  source_card_id: validation_test.target_plus.scope_group_123
  target_card_id: table.zs_observe.target_tcin_mapping
  source_type: validation_test
  target_type: table
  inverse_edge_type: null
  materialize_inverse: false
  legacy_edge_aliases: []
  edge_class: canonical
  canonical_cognee_edge: true
```
```yaml
candidate_edge:
  edge_id: edge.target_plus.00596.validates_card
  canonical_edge_type: VALIDATES_CARD
  source_card_id: validation_test.target_plus.no_forbidden_cards
  target_card_id: platform.target_plus
  source_type: validation_test
  target_type: platform
  inverse_edge_type: null
  materialize_inverse: false
  legacy_edge_aliases: []
  edge_class: canonical
  canonical_cognee_edge: true
```
```yaml
candidate_edge:
  edge_id: edge.target_plus.00597.validates_card
  canonical_edge_type: VALIDATES_CARD
  source_card_id: validation_test.target_plus.no_reverse_charge_return_mix
  target_card_id: table.zs_observe.target_settlement
  source_type: validation_test
  target_type: table
  inverse_edge_type: null
  materialize_inverse: false
  legacy_edge_aliases: []
  edge_class: canonical
  canonical_cognee_edge: true
```
```yaml
candidate_edge:
  edge_id: edge.target_plus.00598.validates_card
  canonical_edge_type: VALIDATES_CARD
  source_card_id: validation_test.target_plus.no_reverse_charge_return_mix
  target_card_id: rule.target_plus.reverse_charge_not_return
  source_type: validation_test
  target_type: rule
  inverse_edge_type: null
  materialize_inverse: false
  legacy_edge_aliases: []
  edge_class: canonical
  canonical_cognee_edge: true
```
```yaml
candidate_edge:
  edge_id: edge.target_plus.00599.validates_card
  canonical_edge_type: VALIDATES_CARD
  source_card_id: validation_test.target_plus.currency_usd_label
  target_card_id: table.zs_observe.target_sales
  source_type: validation_test
  target_type: table
  inverse_edge_type: null
  materialize_inverse: false
  legacy_edge_aliases: []
  edge_class: canonical
  canonical_cognee_edge: true
```
```yaml
candidate_edge:
  edge_id: edge.target_plus.00600.validates_card
  canonical_edge_type: VALIDATES_CARD
  source_card_id: validation_test.target_plus.currency_usd_label
  target_card_id: table.zs_observe.target_returns
  source_type: validation_test
  target_type: table
  inverse_edge_type: null
  materialize_inverse: false
  legacy_edge_aliases: []
  edge_class: canonical
  canonical_cognee_edge: true
```
```yaml
candidate_edge:
  edge_id: edge.target_plus.00601.validates_card
  canonical_edge_type: VALIDATES_CARD
  source_card_id: validation_test.target_plus.currency_usd_label
  target_card_id: table.zs_observe.target_settlement
  source_type: validation_test
  target_type: table
  inverse_edge_type: null
  materialize_inverse: false
  legacy_edge_aliases: []
  edge_class: canonical
  canonical_cognee_edge: true
```
```yaml
candidate_edge:
  edge_id: edge.target_plus.00602.validates_card
  canonical_edge_type: VALIDATES_CARD
  source_card_id: validation_test.target_plus.currency_usd_label
  target_card_id: table.zs_observe.target_tcin_mapping
  source_type: validation_test
  target_type: table
  inverse_edge_type: null
  materialize_inverse: false
  legacy_edge_aliases: []
  edge_class: canonical
  canonical_cognee_edge: true
```
```yaml
candidate_edge:
  edge_id: edge.target_plus.00603.validates_card
  canonical_edge_type: VALIDATES_CARD
  source_card_id: validation_test.target_plus.mapping_join_tcin
  target_card_id: relationship.target_plus.sales_mapping.tcin
  source_type: validation_test
  target_type: relationship
  inverse_edge_type: null
  materialize_inverse: false
  legacy_edge_aliases: []
  edge_class: canonical
  canonical_cognee_edge: true
```
```yaml
candidate_edge:
  edge_id: edge.target_plus.00604.validates_card
  canonical_edge_type: VALIDATES_CARD
  source_card_id: validation_test.target_plus.mapping_join_tcin
  target_card_id: rule.target_plus.tcin_mapping_join
  source_type: validation_test
  target_type: rule
  inverse_edge_type: null
  materialize_inverse: false
  legacy_edge_aliases: []
  edge_class: canonical
  canonical_cognee_edge: true
```
```yaml
candidate_edge:
  edge_id: edge.target_plus.00605.validates_card
  canonical_edge_type: VALIDATES_CARD
  source_card_id: validation_test.target_plus.date_aligned_recon
  target_card_id: reconciliation_profile.target_plus.sales_settlement
  source_type: validation_test
  target_type: reconciliation_profile
  inverse_edge_type: null
  materialize_inverse: false
  legacy_edge_aliases: []
  edge_class: canonical
  canonical_cognee_edge: true
```
```yaml
candidate_edge:
  edge_id: edge.target_plus.00606.validates_card
  canonical_edge_type: VALIDATES_CARD
  source_card_id: validation_test.target_plus.date_aligned_recon
  target_card_id: rule.target_plus.settlement_recency_gap
  source_type: validation_test
  target_type: rule
  inverse_edge_type: null
  materialize_inverse: false
  legacy_edge_aliases: []
  edge_class: canonical
  canonical_cognee_edge: true
```
```yaml
candidate_edge:
  edge_id: edge.target_plus.00607.validates_card
  canonical_edge_type: VALIDATES_CARD
  source_card_id: validation_test.target_plus.commission_15pct
  target_card_id: metric_impl.target_plus.commission_validation
  source_type: validation_test
  target_type: metric_implementation
  inverse_edge_type: null
  materialize_inverse: false
  legacy_edge_aliases: []
  edge_class: canonical
  canonical_cognee_edge: true
```
```yaml
candidate_edge:
  edge_id: edge.target_plus.00608.validates_card
  canonical_edge_type: VALIDATES_CARD
  source_card_id: validation_test.target_plus.commission_15pct
  target_card_id: matching_logic.target_plus.commission_15pct
  source_type: validation_test
  target_type: matching_logic
  inverse_edge_type: null
  materialize_inverse: false
  legacy_edge_aliases: []
  edge_class: canonical
  canonical_cognee_edge: true
```
```yaml
candidate_edge:
  edge_id: edge.target_plus.00609.validates_card
  canonical_edge_type: VALIDATES_CARD
  source_card_id: validation_test.target_plus.no_indian_tax_impl
  target_card_id: domain.target_plus.tax
  source_type: validation_test
  target_type: domain
  inverse_edge_type: null
  materialize_inverse: false
  legacy_edge_aliases: []
  edge_class: canonical
  canonical_cognee_edge: true
```
```yaml
candidate_edge:
  edge_id: edge.target_plus.00610.validates_card
  canonical_edge_type: VALIDATES_CARD
  source_card_id: validation_test.target_plus.no_indian_tax_impl
  target_card_id: rule.target_plus.no_indian_tcs_tds
  source_type: validation_test
  target_type: rule
  inverse_edge_type: null
  materialize_inverse: false
  legacy_edge_aliases: []
  edge_class: canonical
  canonical_cognee_edge: true
```
```yaml
candidate_edge:
  edge_id: edge.target_plus.00611.validates_card
  canonical_edge_type: VALIDATES_CARD
  source_card_id: validation_test.target_plus.barcode_cast
  target_card_id: column.zs_observe.target_tcin_mapping.barcode
  source_type: validation_test
  target_type: column
  inverse_edge_type: null
  materialize_inverse: false
  legacy_edge_aliases: []
  edge_class: canonical
  canonical_cognee_edge: true
```
```yaml
candidate_edge:
  edge_id: edge.target_plus.00612.validates_card
  canonical_edge_type: VALIDATES_CARD
  source_card_id: validation_test.target_plus.barcode_cast
  target_card_id: rule.target_plus.barcode_formatting
  source_type: validation_test
  target_type: rule
  inverse_edge_type: null
  materialize_inverse: false
  legacy_edge_aliases: []
  edge_class: canonical
  canonical_cognee_edge: true
```
```yaml
candidate_edge:
  edge_id: edge.target_plus.00613.uses_table
  canonical_edge_type: USES_TABLE
  source_card_id: query_pattern.target_plus.marketplace.5_1_total_gmv
  target_card_id: table.zs_observe.target_sales
  source_type: query_pattern
  target_type: table
  inverse_edge_type: null
  materialize_inverse: false
  legacy_edge_aliases:
  - query_requires_table
  edge_class: canonical
  canonical_cognee_edge: true
```
```yaml
candidate_edge:
  edge_id: edge.target_plus.00614.requires_rule
  canonical_edge_type: REQUIRES_RULE
  source_card_id: query_pattern.target_plus.marketplace.5_1_total_gmv
  target_card_id: rule.target_plus.active_filter
  source_type: query_pattern
  target_type: rule
  inverse_edge_type: null
  materialize_inverse: false
  legacy_edge_aliases: []
  edge_class: canonical
  canonical_cognee_edge: true
```
```yaml
candidate_edge:
  edge_id: edge.target_plus.00615.produces_metric
  canonical_edge_type: PRODUCES_METRIC
  source_card_id: query_pattern.target_plus.marketplace.5_1_total_gmv
  target_card_id: metric.target_plus.total_gmv
  source_type: query_pattern
  target_type: metric
  inverse_edge_type: null
  materialize_inverse: false
  legacy_edge_aliases: []
  edge_class: canonical
  canonical_cognee_edge: true
```
```yaml
candidate_edge:
  edge_id: edge.target_plus.00616.uses_output_contract
  canonical_edge_type: USES_OUTPUT_CONTRACT
  source_card_id: query_pattern.target_plus.marketplace.5_1_total_gmv
  target_card_id: output_contract.target_plus.metric_timeseries
  source_type: query_pattern
  target_type: output_contract
  inverse_edge_type: null
  materialize_inverse: false
  legacy_edge_aliases: []
  edge_class: canonical
  canonical_cognee_edge: true
```
```yaml
candidate_edge:
  edge_id: edge.target_plus.00617.has_execution_constraint_set
  canonical_edge_type: HAS_EXECUTION_CONSTRAINT_SET
  source_card_id: query_pattern.target_plus.marketplace.5_1_total_gmv
  target_card_id: execution_constraint_set.target_plus.marketplace_parser_constraints
  source_type: query_pattern
  target_type: execution_constraint_set
  inverse_edge_type: null
  materialize_inverse: false
  legacy_edge_aliases: []
  edge_class: canonical
  canonical_cognee_edge: true
```
```yaml
candidate_edge:
  edge_id: edge.target_plus.00618.uses_table
  canonical_edge_type: USES_TABLE
  source_card_id: query_pattern.target_plus.marketplace.5_2_net_revenue_settlement_view
  target_card_id: table.zs_observe.target_settlement
  source_type: query_pattern
  target_type: table
  inverse_edge_type: null
  materialize_inverse: false
  legacy_edge_aliases:
  - query_requires_table
  edge_class: canonical
  canonical_cognee_edge: true
```
```yaml
candidate_edge:
  edge_id: edge.target_plus.00619.requires_rule
  canonical_edge_type: REQUIRES_RULE
  source_card_id: query_pattern.target_plus.marketplace.5_2_net_revenue_settlement_view
  target_card_id: rule.target_plus.active_filter
  source_type: query_pattern
  target_type: rule
  inverse_edge_type: null
  materialize_inverse: false
  legacy_edge_aliases: []
  edge_class: canonical
  canonical_cognee_edge: true
```
```yaml
candidate_edge:
  edge_id: edge.target_plus.00620.requires_rule
  canonical_edge_type: REQUIRES_RULE
  source_card_id: query_pattern.target_plus.marketplace.5_2_net_revenue_settlement_view
  target_card_id: rule.target_plus.currency_label_usd_values
  source_type: query_pattern
  target_type: rule
  inverse_edge_type: null
  materialize_inverse: false
  legacy_edge_aliases: []
  edge_class: canonical
  canonical_cognee_edge: true
```
```yaml
candidate_edge:
  edge_id: edge.target_plus.00621.requires_rule
  canonical_edge_type: REQUIRES_RULE
  source_card_id: query_pattern.target_plus.marketplace.5_2_net_revenue_settlement_view
  target_card_id: rule.target_plus.settlement_recency_gap
  source_type: query_pattern
  target_type: rule
  inverse_edge_type: null
  materialize_inverse: false
  legacy_edge_aliases: []
  edge_class: canonical
  canonical_cognee_edge: true
```
```yaml
candidate_edge:
  edge_id: edge.target_plus.00622.requires_rule
  canonical_edge_type: REQUIRES_RULE
  source_card_id: query_pattern.target_plus.marketplace.5_2_net_revenue_settlement_view
  target_card_id: rule.target_plus.reverse_charge_not_return
  source_type: query_pattern
  target_type: rule
  inverse_edge_type: null
  materialize_inverse: false
  legacy_edge_aliases: []
  edge_class: canonical
  canonical_cognee_edge: true
```
```yaml
candidate_edge:
  edge_id: edge.target_plus.00623.produces_metric
  canonical_edge_type: PRODUCES_METRIC
  source_card_id: query_pattern.target_plus.marketplace.5_2_net_revenue_settlement_view
  target_card_id: metric.target_plus.net_settlement_revenue
  source_type: query_pattern
  target_type: metric
  inverse_edge_type: null
  materialize_inverse: false
  legacy_edge_aliases: []
  edge_class: canonical
  canonical_cognee_edge: true
```
```yaml
candidate_edge:
  edge_id: edge.target_plus.00624.uses_output_contract
  canonical_edge_type: USES_OUTPUT_CONTRACT
  source_card_id: query_pattern.target_plus.marketplace.5_2_net_revenue_settlement_view
  target_card_id: output_contract.target_plus.metric_timeseries
  source_type: query_pattern
  target_type: output_contract
  inverse_edge_type: null
  materialize_inverse: false
  legacy_edge_aliases: []
  edge_class: canonical
  canonical_cognee_edge: true
```
```yaml
candidate_edge:
  edge_id: edge.target_plus.00625.has_execution_constraint_set
  canonical_edge_type: HAS_EXECUTION_CONSTRAINT_SET
  source_card_id: query_pattern.target_plus.marketplace.5_2_net_revenue_settlement_view
  target_card_id: execution_constraint_set.target_plus.marketplace_parser_constraints
  source_type: query_pattern
  target_type: execution_constraint_set
  inverse_edge_type: null
  materialize_inverse: false
  legacy_edge_aliases: []
  edge_class: canonical
  canonical_cognee_edge: true
```
```yaml
candidate_edge:
  edge_id: edge.target_plus.00626.uses_table
  canonical_edge_type: USES_TABLE
  source_card_id: query_pattern.target_plus.marketplace.5_3_return_rate
  target_card_id: table.zs_observe.target_returns
  source_type: query_pattern
  target_type: table
  inverse_edge_type: null
  materialize_inverse: false
  legacy_edge_aliases:
  - query_requires_table
  edge_class: canonical
  canonical_cognee_edge: true
```
```yaml
candidate_edge:
  edge_id: edge.target_plus.00627.uses_table
  canonical_edge_type: USES_TABLE
  source_card_id: query_pattern.target_plus.marketplace.5_3_return_rate
  target_card_id: table.zs_observe.target_sales
  source_type: query_pattern
  target_type: table
  inverse_edge_type: null
  materialize_inverse: false
  legacy_edge_aliases:
  - query_requires_table
  edge_class: canonical
  canonical_cognee_edge: true
```
```yaml
candidate_edge:
  edge_id: edge.target_plus.00628.requires_rule
  canonical_edge_type: REQUIRES_RULE
  source_card_id: query_pattern.target_plus.marketplace.5_3_return_rate
  target_card_id: rule.target_plus.active_filter
  source_type: query_pattern
  target_type: rule
  inverse_edge_type: null
  materialize_inverse: false
  legacy_edge_aliases: []
  edge_class: canonical
  canonical_cognee_edge: true
```
```yaml
candidate_edge:
  edge_id: edge.target_plus.00629.produces_metric
  canonical_edge_type: PRODUCES_METRIC
  source_card_id: query_pattern.target_plus.marketplace.5_3_return_rate
  target_card_id: metric.target_plus.return_rate
  source_type: query_pattern
  target_type: metric
  inverse_edge_type: null
  materialize_inverse: false
  legacy_edge_aliases: []
  edge_class: canonical
  canonical_cognee_edge: true
```
```yaml
candidate_edge:
  edge_id: edge.target_plus.00630.uses_output_contract
  canonical_edge_type: USES_OUTPUT_CONTRACT
  source_card_id: query_pattern.target_plus.marketplace.5_3_return_rate
  target_card_id: output_contract.target_plus.metric_timeseries
  source_type: query_pattern
  target_type: output_contract
  inverse_edge_type: null
  materialize_inverse: false
  legacy_edge_aliases: []
  edge_class: canonical
  canonical_cognee_edge: true
```
```yaml
candidate_edge:
  edge_id: edge.target_plus.00631.has_execution_constraint_set
  canonical_edge_type: HAS_EXECUTION_CONSTRAINT_SET
  source_card_id: query_pattern.target_plus.marketplace.5_3_return_rate
  target_card_id: execution_constraint_set.target_plus.marketplace_parser_constraints
  source_type: query_pattern
  target_type: execution_constraint_set
  inverse_edge_type: null
  materialize_inverse: false
  legacy_edge_aliases: []
  edge_class: canonical
  canonical_cognee_edge: true
```
```yaml
candidate_edge:
  edge_id: edge.target_plus.00632.uses_table
  canonical_edge_type: USES_TABLE
  source_card_id: query_pattern.target_plus.marketplace.5_4_average_order_value_aov
  target_card_id: table.zs_observe.target_sales
  source_type: query_pattern
  target_type: table
  inverse_edge_type: null
  materialize_inverse: false
  legacy_edge_aliases:
  - query_requires_table
  edge_class: canonical
  canonical_cognee_edge: true
```
```yaml
candidate_edge:
  edge_id: edge.target_plus.00633.requires_rule
  canonical_edge_type: REQUIRES_RULE
  source_card_id: query_pattern.target_plus.marketplace.5_4_average_order_value_aov
  target_card_id: rule.target_plus.active_filter
  source_type: query_pattern
  target_type: rule
  inverse_edge_type: null
  materialize_inverse: false
  legacy_edge_aliases: []
  edge_class: canonical
  canonical_cognee_edge: true
```
```yaml
candidate_edge:
  edge_id: edge.target_plus.00634.produces_metric
  canonical_edge_type: PRODUCES_METRIC
  source_card_id: query_pattern.target_plus.marketplace.5_4_average_order_value_aov
  target_card_id: metric.target_plus.aov
  source_type: query_pattern
  target_type: metric
  inverse_edge_type: null
  materialize_inverse: false
  legacy_edge_aliases: []
  edge_class: canonical
  canonical_cognee_edge: true
```
```yaml
candidate_edge:
  edge_id: edge.target_plus.00635.uses_output_contract
  canonical_edge_type: USES_OUTPUT_CONTRACT
  source_card_id: query_pattern.target_plus.marketplace.5_4_average_order_value_aov
  target_card_id: output_contract.target_plus.metric_timeseries
  source_type: query_pattern
  target_type: output_contract
  inverse_edge_type: null
  materialize_inverse: false
  legacy_edge_aliases: []
  edge_class: canonical
  canonical_cognee_edge: true
```
```yaml
candidate_edge:
  edge_id: edge.target_plus.00636.has_execution_constraint_set
  canonical_edge_type: HAS_EXECUTION_CONSTRAINT_SET
  source_card_id: query_pattern.target_plus.marketplace.5_4_average_order_value_aov
  target_card_id: execution_constraint_set.target_plus.marketplace_parser_constraints
  source_type: query_pattern
  target_type: execution_constraint_set
  inverse_edge_type: null
  materialize_inverse: false
  legacy_edge_aliases: []
  edge_class: canonical
  canonical_cognee_edge: true
```
```yaml
candidate_edge:
  edge_id: edge.target_plus.00637.uses_table
  canonical_edge_type: USES_TABLE
  source_card_id: query_pattern.target_plus.marketplace.5_5_effective_payout_rate
  target_card_id: table.zs_observe.target_settlement
  source_type: query_pattern
  target_type: table
  inverse_edge_type: null
  materialize_inverse: false
  legacy_edge_aliases:
  - query_requires_table
  edge_class: canonical
  canonical_cognee_edge: true
```
```yaml
candidate_edge:
  edge_id: edge.target_plus.00638.requires_rule
  canonical_edge_type: REQUIRES_RULE
  source_card_id: query_pattern.target_plus.marketplace.5_5_effective_payout_rate
  target_card_id: rule.target_plus.active_filter
  source_type: query_pattern
  target_type: rule
  inverse_edge_type: null
  materialize_inverse: false
  legacy_edge_aliases: []
  edge_class: canonical
  canonical_cognee_edge: true
```
```yaml
candidate_edge:
  edge_id: edge.target_plus.00639.requires_rule
  canonical_edge_type: REQUIRES_RULE
  source_card_id: query_pattern.target_plus.marketplace.5_5_effective_payout_rate
  target_card_id: rule.target_plus.currency_label_usd_values
  source_type: query_pattern
  target_type: rule
  inverse_edge_type: null
  materialize_inverse: false
  legacy_edge_aliases: []
  edge_class: canonical
  canonical_cognee_edge: true
```
```yaml
candidate_edge:
  edge_id: edge.target_plus.00640.produces_metric
  canonical_edge_type: PRODUCES_METRIC
  source_card_id: query_pattern.target_plus.marketplace.5_5_effective_payout_rate
  target_card_id: metric.target_plus.effective_payout_rate
  source_type: query_pattern
  target_type: metric
  inverse_edge_type: null
  materialize_inverse: false
  legacy_edge_aliases: []
  edge_class: canonical
  canonical_cognee_edge: true
```
```yaml
candidate_edge:
  edge_id: edge.target_plus.00641.uses_output_contract
  canonical_edge_type: USES_OUTPUT_CONTRACT
  source_card_id: query_pattern.target_plus.marketplace.5_5_effective_payout_rate
  target_card_id: output_contract.target_plus.metric_timeseries
  source_type: query_pattern
  target_type: output_contract
  inverse_edge_type: null
  materialize_inverse: false
  legacy_edge_aliases: []
  edge_class: canonical
  canonical_cognee_edge: true
```
```yaml
candidate_edge:
  edge_id: edge.target_plus.00642.has_execution_constraint_set
  canonical_edge_type: HAS_EXECUTION_CONSTRAINT_SET
  source_card_id: query_pattern.target_plus.marketplace.5_5_effective_payout_rate
  target_card_id: execution_constraint_set.target_plus.marketplace_parser_constraints
  source_type: query_pattern
  target_type: execution_constraint_set
  inverse_edge_type: null
  materialize_inverse: false
  legacy_edge_aliases: []
  edge_class: canonical
  canonical_cognee_edge: true
```
```yaml
candidate_edge:
  edge_id: edge.target_plus.00643.uses_table
  canonical_edge_type: USES_TABLE
  source_card_id: query_pattern.target_plus.marketplace.5_6_top_selling_skus
  target_card_id: table.zs_observe.target_sales
  source_type: query_pattern
  target_type: table
  inverse_edge_type: null
  materialize_inverse: false
  legacy_edge_aliases:
  - query_requires_table
  edge_class: canonical
  canonical_cognee_edge: true
```
```yaml
candidate_edge:
  edge_id: edge.target_plus.00644.uses_table
  canonical_edge_type: USES_TABLE
  source_card_id: query_pattern.target_plus.marketplace.5_6_top_selling_skus
  target_card_id: table.zs_observe.target_tcin_mapping
  source_type: query_pattern
  target_type: table
  inverse_edge_type: null
  materialize_inverse: false
  legacy_edge_aliases:
  - query_requires_table
  edge_class: canonical
  canonical_cognee_edge: true
```
```yaml
candidate_edge:
  edge_id: edge.target_plus.00645.requires_rule
  canonical_edge_type: REQUIRES_RULE
  source_card_id: query_pattern.target_plus.marketplace.5_6_top_selling_skus
  target_card_id: rule.target_plus.active_filter
  source_type: query_pattern
  target_type: rule
  inverse_edge_type: null
  materialize_inverse: false
  legacy_edge_aliases: []
  edge_class: canonical
  canonical_cognee_edge: true
```
```yaml
candidate_edge:
  edge_id: edge.target_plus.00646.produces_metric
  canonical_edge_type: PRODUCES_METRIC
  source_card_id: query_pattern.target_plus.marketplace.5_6_top_selling_skus
  target_card_id: metric.target_plus.top_selling_skus
  source_type: query_pattern
  target_type: metric
  inverse_edge_type: null
  materialize_inverse: false
  legacy_edge_aliases: []
  edge_class: canonical
  canonical_cognee_edge: true
```
```yaml
candidate_edge:
  edge_id: edge.target_plus.00647.uses_output_contract
  canonical_edge_type: USES_OUTPUT_CONTRACT
  source_card_id: query_pattern.target_plus.marketplace.5_6_top_selling_skus
  target_card_id: output_contract.target_plus.metric_timeseries
  source_type: query_pattern
  target_type: output_contract
  inverse_edge_type: null
  materialize_inverse: false
  legacy_edge_aliases: []
  edge_class: canonical
  canonical_cognee_edge: true
```
```yaml
candidate_edge:
  edge_id: edge.target_plus.00648.has_execution_constraint_set
  canonical_edge_type: HAS_EXECUTION_CONSTRAINT_SET
  source_card_id: query_pattern.target_plus.marketplace.5_6_top_selling_skus
  target_card_id: execution_constraint_set.target_plus.marketplace_parser_constraints
  source_type: query_pattern
  target_type: execution_constraint_set
  inverse_edge_type: null
  materialize_inverse: false
  legacy_edge_aliases: []
  edge_class: canonical
  canonical_cognee_edge: true
```
```yaml
candidate_edge:
  edge_id: edge.target_plus.00649.uses_table
  canonical_edge_type: USES_TABLE
  source_card_id: query_pattern.target_plus.marketplace.5_7_cancellation_rate
  target_card_id: table.zs_observe.target_sales
  source_type: query_pattern
  target_type: table
  inverse_edge_type: null
  materialize_inverse: false
  legacy_edge_aliases:
  - query_requires_table
  edge_class: canonical
  canonical_cognee_edge: true
```
```yaml
candidate_edge:
  edge_id: edge.target_plus.00650.requires_rule
  canonical_edge_type: REQUIRES_RULE
  source_card_id: query_pattern.target_plus.marketplace.5_7_cancellation_rate
  target_card_id: rule.target_plus.active_filter
  source_type: query_pattern
  target_type: rule
  inverse_edge_type: null
  materialize_inverse: false
  legacy_edge_aliases: []
  edge_class: canonical
  canonical_cognee_edge: true
```
```yaml
candidate_edge:
  edge_id: edge.target_plus.00651.produces_metric
  canonical_edge_type: PRODUCES_METRIC
  source_card_id: query_pattern.target_plus.marketplace.5_7_cancellation_rate
  target_card_id: metric.target_plus.cancellation_rate
  source_type: query_pattern
  target_type: metric
  inverse_edge_type: null
  materialize_inverse: false
  legacy_edge_aliases: []
  edge_class: canonical
  canonical_cognee_edge: true
```
```yaml
candidate_edge:
  edge_id: edge.target_plus.00652.uses_output_contract
  canonical_edge_type: USES_OUTPUT_CONTRACT
  source_card_id: query_pattern.target_plus.marketplace.5_7_cancellation_rate
  target_card_id: output_contract.target_plus.metric_timeseries
  source_type: query_pattern
  target_type: output_contract
  inverse_edge_type: null
  materialize_inverse: false
  legacy_edge_aliases: []
  edge_class: canonical
  canonical_cognee_edge: true
```
```yaml
candidate_edge:
  edge_id: edge.target_plus.00653.has_execution_constraint_set
  canonical_edge_type: HAS_EXECUTION_CONSTRAINT_SET
  source_card_id: query_pattern.target_plus.marketplace.5_7_cancellation_rate
  target_card_id: execution_constraint_set.target_plus.marketplace_parser_constraints
  source_type: query_pattern
  target_type: execution_constraint_set
  inverse_edge_type: null
  materialize_inverse: false
  legacy_edge_aliases: []
  edge_class: canonical
  canonical_cognee_edge: true
```
```yaml
candidate_edge:
  edge_id: edge.target_plus.00654.uses_table
  canonical_edge_type: USES_TABLE
  source_card_id: query_pattern.target_plus.marketplace.6_1_sales_settlement_reconciliation
  target_card_id: table.zs_observe.target_sales
  source_type: query_pattern
  target_type: table
  inverse_edge_type: null
  materialize_inverse: false
  legacy_edge_aliases:
  - query_requires_table
  edge_class: canonical
  canonical_cognee_edge: true
```
```yaml
candidate_edge:
  edge_id: edge.target_plus.00655.uses_table
  canonical_edge_type: USES_TABLE
  source_card_id: query_pattern.target_plus.marketplace.6_1_sales_settlement_reconciliation
  target_card_id: table.zs_observe.target_settlement
  source_type: query_pattern
  target_type: table
  inverse_edge_type: null
  materialize_inverse: false
  legacy_edge_aliases:
  - query_requires_table
  edge_class: canonical
  canonical_cognee_edge: true
```
```yaml
candidate_edge:
  edge_id: edge.target_plus.00656.requires_rule
  canonical_edge_type: REQUIRES_RULE
  source_card_id: query_pattern.target_plus.marketplace.6_1_sales_settlement_reconciliation
  target_card_id: rule.target_plus.active_filter
  source_type: query_pattern
  target_type: rule
  inverse_edge_type: null
  materialize_inverse: false
  legacy_edge_aliases: []
  edge_class: canonical
  canonical_cognee_edge: true
```
```yaml
candidate_edge:
  edge_id: edge.target_plus.00657.requires_rule
  canonical_edge_type: REQUIRES_RULE
  source_card_id: query_pattern.target_plus.marketplace.6_1_sales_settlement_reconciliation
  target_card_id: rule.target_plus.currency_label_usd_values
  source_type: query_pattern
  target_type: rule
  inverse_edge_type: null
  materialize_inverse: false
  legacy_edge_aliases: []
  edge_class: canonical
  canonical_cognee_edge: true
```
```yaml
candidate_edge:
  edge_id: edge.target_plus.00658.requires_rule
  canonical_edge_type: REQUIRES_RULE
  source_card_id: query_pattern.target_plus.marketplace.6_1_sales_settlement_reconciliation
  target_card_id: rule.target_plus.settlement_recency_gap
  source_type: query_pattern
  target_type: rule
  inverse_edge_type: null
  materialize_inverse: false
  legacy_edge_aliases: []
  edge_class: canonical
  canonical_cognee_edge: true
```
```yaml
candidate_edge:
  edge_id: edge.target_plus.00659.uses_reconciliation_profile
  canonical_edge_type: USES_RECONCILIATION_PROFILE
  source_card_id: query_pattern.target_plus.marketplace.6_1_sales_settlement_reconciliation
  target_card_id: reconciliation_profile.target_plus.sales_settlement
  source_type: query_pattern
  target_type: reconciliation_profile
  inverse_edge_type: null
  materialize_inverse: false
  legacy_edge_aliases: []
  edge_class: canonical
  canonical_cognee_edge: true
```
```yaml
candidate_edge:
  edge_id: edge.target_plus.00660.uses_output_contract
  canonical_edge_type: USES_OUTPUT_CONTRACT
  source_card_id: query_pattern.target_plus.marketplace.6_1_sales_settlement_reconciliation
  target_card_id: output_contract.target_plus.reconciliation_status
  source_type: query_pattern
  target_type: output_contract
  inverse_edge_type: null
  materialize_inverse: false
  legacy_edge_aliases: []
  edge_class: canonical
  canonical_cognee_edge: true
```
```yaml
candidate_edge:
  edge_id: edge.target_plus.00661.has_execution_constraint_set
  canonical_edge_type: HAS_EXECUTION_CONSTRAINT_SET
  source_card_id: query_pattern.target_plus.marketplace.6_1_sales_settlement_reconciliation
  target_card_id: execution_constraint_set.target_plus.marketplace_parser_constraints
  source_type: query_pattern
  target_type: execution_constraint_set
  inverse_edge_type: null
  materialize_inverse: false
  legacy_edge_aliases: []
  edge_class: canonical
  canonical_cognee_edge: true
```
```yaml
candidate_edge:
  edge_id: edge.target_plus.00662.uses_table
  canonical_edge_type: USES_TABLE
  source_card_id: query_pattern.target_plus.marketplace.6_2_returns_settlement_refund_match
  target_card_id: table.zs_observe.target_returns
  source_type: query_pattern
  target_type: table
  inverse_edge_type: null
  materialize_inverse: false
  legacy_edge_aliases:
  - query_requires_table
  edge_class: canonical
  canonical_cognee_edge: true
```
```yaml
candidate_edge:
  edge_id: edge.target_plus.00663.uses_table
  canonical_edge_type: USES_TABLE
  source_card_id: query_pattern.target_plus.marketplace.6_2_returns_settlement_refund_match
  target_card_id: table.zs_observe.target_settlement
  source_type: query_pattern
  target_type: table
  inverse_edge_type: null
  materialize_inverse: false
  legacy_edge_aliases:
  - query_requires_table
  edge_class: canonical
  canonical_cognee_edge: true
```
```yaml
candidate_edge:
  edge_id: edge.target_plus.00664.requires_rule
  canonical_edge_type: REQUIRES_RULE
  source_card_id: query_pattern.target_plus.marketplace.6_2_returns_settlement_refund_match
  target_card_id: rule.target_plus.active_filter
  source_type: query_pattern
  target_type: rule
  inverse_edge_type: null
  materialize_inverse: false
  legacy_edge_aliases: []
  edge_class: canonical
  canonical_cognee_edge: true
```
```yaml
candidate_edge:
  edge_id: edge.target_plus.00665.requires_rule
  canonical_edge_type: REQUIRES_RULE
  source_card_id: query_pattern.target_plus.marketplace.6_2_returns_settlement_refund_match
  target_card_id: rule.target_plus.currency_label_usd_values
  source_type: query_pattern
  target_type: rule
  inverse_edge_type: null
  materialize_inverse: false
  legacy_edge_aliases: []
  edge_class: canonical
  canonical_cognee_edge: true
```
```yaml
candidate_edge:
  edge_id: edge.target_plus.00666.requires_rule
  canonical_edge_type: REQUIRES_RULE
  source_card_id: query_pattern.target_plus.marketplace.6_2_returns_settlement_refund_match
  target_card_id: rule.target_plus.settlement_recency_gap
  source_type: query_pattern
  target_type: rule
  inverse_edge_type: null
  materialize_inverse: false
  legacy_edge_aliases: []
  edge_class: canonical
  canonical_cognee_edge: true
```
```yaml
candidate_edge:
  edge_id: edge.target_plus.00667.uses_reconciliation_profile
  canonical_edge_type: USES_RECONCILIATION_PROFILE
  source_card_id: query_pattern.target_plus.marketplace.6_2_returns_settlement_refund_match
  target_card_id: reconciliation_profile.target_plus.returns_settlement
  source_type: query_pattern
  target_type: reconciliation_profile
  inverse_edge_type: null
  materialize_inverse: false
  legacy_edge_aliases: []
  edge_class: canonical
  canonical_cognee_edge: true
```
```yaml
candidate_edge:
  edge_id: edge.target_plus.00668.uses_output_contract
  canonical_edge_type: USES_OUTPUT_CONTRACT
  source_card_id: query_pattern.target_plus.marketplace.6_2_returns_settlement_refund_match
  target_card_id: output_contract.target_plus.reconciliation_status
  source_type: query_pattern
  target_type: output_contract
  inverse_edge_type: null
  materialize_inverse: false
  legacy_edge_aliases: []
  edge_class: canonical
  canonical_cognee_edge: true
```
```yaml
candidate_edge:
  edge_id: edge.target_plus.00669.has_execution_constraint_set
  canonical_edge_type: HAS_EXECUTION_CONSTRAINT_SET
  source_card_id: query_pattern.target_plus.marketplace.6_2_returns_settlement_refund_match
  target_card_id: execution_constraint_set.target_plus.marketplace_parser_constraints
  source_type: query_pattern
  target_type: execution_constraint_set
  inverse_edge_type: null
  materialize_inverse: false
  legacy_edge_aliases: []
  edge_class: canonical
  canonical_cognee_edge: true
```
```yaml
candidate_edge:
  edge_id: edge.target_plus.00670.uses_table
  canonical_edge_type: USES_TABLE
  source_card_id: query_pattern.target_plus.marketplace.6_3_commission_validation
  target_card_id: table.zs_observe.target_settlement
  source_type: query_pattern
  target_type: table
  inverse_edge_type: null
  materialize_inverse: false
  legacy_edge_aliases:
  - query_requires_table
  edge_class: canonical
  canonical_cognee_edge: true
```
```yaml
candidate_edge:
  edge_id: edge.target_plus.00671.requires_rule
  canonical_edge_type: REQUIRES_RULE
  source_card_id: query_pattern.target_plus.marketplace.6_3_commission_validation
  target_card_id: rule.target_plus.active_filter
  source_type: query_pattern
  target_type: rule
  inverse_edge_type: null
  materialize_inverse: false
  legacy_edge_aliases: []
  edge_class: canonical
  canonical_cognee_edge: true
```
```yaml
candidate_edge:
  edge_id: edge.target_plus.00672.requires_rule
  canonical_edge_type: REQUIRES_RULE
  source_card_id: query_pattern.target_plus.marketplace.6_3_commission_validation
  target_card_id: rule.target_plus.currency_label_usd_values
  source_type: query_pattern
  target_type: rule
  inverse_edge_type: null
  materialize_inverse: false
  legacy_edge_aliases: []
  edge_class: canonical
  canonical_cognee_edge: true
```
```yaml
candidate_edge:
  edge_id: edge.target_plus.00673.produces_metric
  canonical_edge_type: PRODUCES_METRIC
  source_card_id: query_pattern.target_plus.marketplace.6_3_commission_validation
  target_card_id: metric.target_plus.commission_validation_variance
  source_type: query_pattern
  target_type: metric
  inverse_edge_type: null
  materialize_inverse: false
  legacy_edge_aliases: []
  edge_class: canonical
  canonical_cognee_edge: true
```
```yaml
candidate_edge:
  edge_id: edge.target_plus.00674.uses_reconciliation_profile
  canonical_edge_type: USES_RECONCILIATION_PROFILE
  source_card_id: query_pattern.target_plus.marketplace.6_3_commission_validation
  target_card_id: reconciliation_profile.target_plus.commission_validation
  source_type: query_pattern
  target_type: reconciliation_profile
  inverse_edge_type: null
  materialize_inverse: false
  legacy_edge_aliases: []
  edge_class: canonical
  canonical_cognee_edge: true
```
```yaml
candidate_edge:
  edge_id: edge.target_plus.00675.uses_output_contract
  canonical_edge_type: USES_OUTPUT_CONTRACT
  source_card_id: query_pattern.target_plus.marketplace.6_3_commission_validation
  target_card_id: output_contract.target_plus.reconciliation_status
  source_type: query_pattern
  target_type: output_contract
  inverse_edge_type: null
  materialize_inverse: false
  legacy_edge_aliases: []
  edge_class: canonical
  canonical_cognee_edge: true
```
```yaml
candidate_edge:
  edge_id: edge.target_plus.00676.has_execution_constraint_set
  canonical_edge_type: HAS_EXECUTION_CONSTRAINT_SET
  source_card_id: query_pattern.target_plus.marketplace.6_3_commission_validation
  target_card_id: execution_constraint_set.target_plus.marketplace_parser_constraints
  source_type: query_pattern
  target_type: execution_constraint_set
  inverse_edge_type: null
  materialize_inverse: false
  legacy_edge_aliases: []
  edge_class: canonical
  canonical_cognee_edge: true
```
```yaml
candidate_edge:
  edge_id: edge.target_plus.00677.uses_table
  canonical_edge_type: USES_TABLE
  source_card_id: query_pattern.target_plus.marketplace.6_4_payout_reconciliation
  target_card_id: table.zs_observe.target_settlement
  source_type: query_pattern
  target_type: table
  inverse_edge_type: null
  materialize_inverse: false
  legacy_edge_aliases:
  - query_requires_table
  edge_class: canonical
  canonical_cognee_edge: true
```
```yaml
candidate_edge:
  edge_id: edge.target_plus.00678.requires_rule
  canonical_edge_type: REQUIRES_RULE
  source_card_id: query_pattern.target_plus.marketplace.6_4_payout_reconciliation
  target_card_id: rule.target_plus.active_filter
  source_type: query_pattern
  target_type: rule
  inverse_edge_type: null
  materialize_inverse: false
  legacy_edge_aliases: []
  edge_class: canonical
  canonical_cognee_edge: true
```
```yaml
candidate_edge:
  edge_id: edge.target_plus.00679.requires_rule
  canonical_edge_type: REQUIRES_RULE
  source_card_id: query_pattern.target_plus.marketplace.6_4_payout_reconciliation
  target_card_id: rule.target_plus.currency_label_usd_values
  source_type: query_pattern
  target_type: rule
  inverse_edge_type: null
  materialize_inverse: false
  legacy_edge_aliases: []
  edge_class: canonical
  canonical_cognee_edge: true
```
```yaml
candidate_edge:
  edge_id: edge.target_plus.00680.requires_rule
  canonical_edge_type: REQUIRES_RULE
  source_card_id: query_pattern.target_plus.marketplace.6_4_payout_reconciliation
  target_card_id: rule.target_plus.settlement_recency_gap
  source_type: query_pattern
  target_type: rule
  inverse_edge_type: null
  materialize_inverse: false
  legacy_edge_aliases: []
  edge_class: canonical
  canonical_cognee_edge: true
```
```yaml
candidate_edge:
  edge_id: edge.target_plus.00681.requires_rule
  canonical_edge_type: REQUIRES_RULE
  source_card_id: query_pattern.target_plus.marketplace.6_4_payout_reconciliation
  target_card_id: rule.target_plus.reverse_charge_not_return
  source_type: query_pattern
  target_type: rule
  inverse_edge_type: null
  materialize_inverse: false
  legacy_edge_aliases: []
  edge_class: canonical
  canonical_cognee_edge: true
```
```yaml
candidate_edge:
  edge_id: edge.target_plus.00682.produces_metric
  canonical_edge_type: PRODUCES_METRIC
  source_card_id: query_pattern.target_plus.marketplace.6_4_payout_reconciliation
  target_card_id: metric.target_plus.payout_batch_total
  source_type: query_pattern
  target_type: metric
  inverse_edge_type: null
  materialize_inverse: false
  legacy_edge_aliases: []
  edge_class: canonical
  canonical_cognee_edge: true
```
```yaml
candidate_edge:
  edge_id: edge.target_plus.00683.uses_reconciliation_profile
  canonical_edge_type: USES_RECONCILIATION_PROFILE
  source_card_id: query_pattern.target_plus.marketplace.6_4_payout_reconciliation
  target_card_id: reconciliation_profile.target_plus.payout_batch
  source_type: query_pattern
  target_type: reconciliation_profile
  inverse_edge_type: null
  materialize_inverse: false
  legacy_edge_aliases: []
  edge_class: canonical
  canonical_cognee_edge: true
```
```yaml
candidate_edge:
  edge_id: edge.target_plus.00684.uses_output_contract
  canonical_edge_type: USES_OUTPUT_CONTRACT
  source_card_id: query_pattern.target_plus.marketplace.6_4_payout_reconciliation
  target_card_id: output_contract.target_plus.reconciliation_status
  source_type: query_pattern
  target_type: output_contract
  inverse_edge_type: null
  materialize_inverse: false
  legacy_edge_aliases: []
  edge_class: canonical
  canonical_cognee_edge: true
```
```yaml
candidate_edge:
  edge_id: edge.target_plus.00685.has_execution_constraint_set
  canonical_edge_type: HAS_EXECUTION_CONSTRAINT_SET
  source_card_id: query_pattern.target_plus.marketplace.6_4_payout_reconciliation
  target_card_id: execution_constraint_set.target_plus.marketplace_parser_constraints
  source_type: query_pattern
  target_type: execution_constraint_set
  inverse_edge_type: null
  materialize_inverse: false
  legacy_edge_aliases: []
  edge_class: canonical
  canonical_cognee_edge: true
```
```yaml
candidate_edge:
  edge_id: edge.target_plus.00686.uses_output_contract
  canonical_edge_type: USES_OUTPUT_CONTRACT
  source_card_id: query_pattern.target_plus.marketplace.8_mandatory_query_filters
  target_card_id: output_contract.target_plus.metric_timeseries
  source_type: query_pattern
  target_type: output_contract
  inverse_edge_type: null
  materialize_inverse: false
  legacy_edge_aliases: []
  edge_class: canonical
  canonical_cognee_edge: true
```
```yaml
candidate_edge:
  edge_id: edge.target_plus.00687.has_execution_constraint_set
  canonical_edge_type: HAS_EXECUTION_CONSTRAINT_SET
  source_card_id: query_pattern.target_plus.marketplace.8_mandatory_query_filters
  target_card_id: execution_constraint_set.target_plus.marketplace_parser_constraints
  source_type: query_pattern
  target_type: execution_constraint_set
  inverse_edge_type: null
  materialize_inverse: false
  legacy_edge_aliases: []
  edge_class: canonical
  canonical_cognee_edge: true
```
```yaml
candidate_edge:
  edge_id: edge.target_plus.00688.uses_table
  canonical_edge_type: USES_TABLE
  source_card_id: query_pattern.target_plus.settlement.8_1_payout_batch_summary
  target_card_id: table.zs_observe.target_settlement
  source_type: query_pattern
  target_type: table
  inverse_edge_type: null
  materialize_inverse: false
  legacy_edge_aliases:
  - query_requires_table
  edge_class: canonical
  canonical_cognee_edge: true
```
```yaml
candidate_edge:
  edge_id: edge.target_plus.00689.requires_rule
  canonical_edge_type: REQUIRES_RULE
  source_card_id: query_pattern.target_plus.settlement.8_1_payout_batch_summary
  target_card_id: rule.target_plus.active_filter
  source_type: query_pattern
  target_type: rule
  inverse_edge_type: null
  materialize_inverse: false
  legacy_edge_aliases: []
  edge_class: canonical
  canonical_cognee_edge: true
```
```yaml
candidate_edge:
  edge_id: edge.target_plus.00690.requires_rule
  canonical_edge_type: REQUIRES_RULE
  source_card_id: query_pattern.target_plus.settlement.8_1_payout_batch_summary
  target_card_id: rule.target_plus.currency_label_usd_values
  source_type: query_pattern
  target_type: rule
  inverse_edge_type: null
  materialize_inverse: false
  legacy_edge_aliases: []
  edge_class: canonical
  canonical_cognee_edge: true
```
```yaml
candidate_edge:
  edge_id: edge.target_plus.00691.requires_rule
  canonical_edge_type: REQUIRES_RULE
  source_card_id: query_pattern.target_plus.settlement.8_1_payout_batch_summary
  target_card_id: rule.target_plus.reverse_charge_not_return
  source_type: query_pattern
  target_type: rule
  inverse_edge_type: null
  materialize_inverse: false
  legacy_edge_aliases: []
  edge_class: canonical
  canonical_cognee_edge: true
```
```yaml
candidate_edge:
  edge_id: edge.target_plus.00692.uses_reconciliation_profile
  canonical_edge_type: USES_RECONCILIATION_PROFILE
  source_card_id: query_pattern.target_plus.settlement.8_1_payout_batch_summary
  target_card_id: reconciliation_profile.target_plus.payout_batch
  source_type: query_pattern
  target_type: reconciliation_profile
  inverse_edge_type: null
  materialize_inverse: false
  legacy_edge_aliases: []
  edge_class: canonical
  canonical_cognee_edge: true
```
```yaml
candidate_edge:
  edge_id: edge.target_plus.00693.uses_output_contract
  canonical_edge_type: USES_OUTPUT_CONTRACT
  source_card_id: query_pattern.target_plus.settlement.8_1_payout_batch_summary
  target_card_id: output_contract.target_plus.reconciliation_status
  source_type: query_pattern
  target_type: output_contract
  inverse_edge_type: null
  materialize_inverse: false
  legacy_edge_aliases: []
  edge_class: canonical
  canonical_cognee_edge: true
```
```yaml
candidate_edge:
  edge_id: edge.target_plus.00694.has_execution_constraint_set
  canonical_edge_type: HAS_EXECUTION_CONSTRAINT_SET
  source_card_id: query_pattern.target_plus.settlement.8_1_payout_batch_summary
  target_card_id: execution_constraint_set.target_plus.marketplace_parser_constraints
  source_type: query_pattern
  target_type: execution_constraint_set
  inverse_edge_type: null
  materialize_inverse: false
  legacy_edge_aliases: []
  edge_class: canonical
  canonical_cognee_edge: true
```
```yaml
candidate_edge:
  edge_id: edge.target_plus.00695.uses_table
  canonical_edge_type: USES_TABLE
  source_card_id: query_pattern.target_plus.settlement.8_2_monthly_settlement_waterfall
  target_card_id: table.zs_observe.target_settlement
  source_type: query_pattern
  target_type: table
  inverse_edge_type: null
  materialize_inverse: false
  legacy_edge_aliases:
  - query_requires_table
  edge_class: canonical
  canonical_cognee_edge: true
```
```yaml
candidate_edge:
  edge_id: edge.target_plus.00696.requires_rule
  canonical_edge_type: REQUIRES_RULE
  source_card_id: query_pattern.target_plus.settlement.8_2_monthly_settlement_waterfall
  target_card_id: rule.target_plus.active_filter
  source_type: query_pattern
  target_type: rule
  inverse_edge_type: null
  materialize_inverse: false
  legacy_edge_aliases: []
  edge_class: canonical
  canonical_cognee_edge: true
```
```yaml
candidate_edge:
  edge_id: edge.target_plus.00697.requires_rule
  canonical_edge_type: REQUIRES_RULE
  source_card_id: query_pattern.target_plus.settlement.8_2_monthly_settlement_waterfall
  target_card_id: rule.target_plus.currency_label_usd_values
  source_type: query_pattern
  target_type: rule
  inverse_edge_type: null
  materialize_inverse: false
  legacy_edge_aliases: []
  edge_class: canonical
  canonical_cognee_edge: true
```
```yaml
candidate_edge:
  edge_id: edge.target_plus.00698.requires_rule
  canonical_edge_type: REQUIRES_RULE
  source_card_id: query_pattern.target_plus.settlement.8_2_monthly_settlement_waterfall
  target_card_id: rule.target_plus.settlement_recency_gap
  source_type: query_pattern
  target_type: rule
  inverse_edge_type: null
  materialize_inverse: false
  legacy_edge_aliases: []
  edge_class: canonical
  canonical_cognee_edge: true
```
```yaml
candidate_edge:
  edge_id: edge.target_plus.00699.requires_rule
  canonical_edge_type: REQUIRES_RULE
  source_card_id: query_pattern.target_plus.settlement.8_2_monthly_settlement_waterfall
  target_card_id: rule.target_plus.reverse_charge_not_return
  source_type: query_pattern
  target_type: rule
  inverse_edge_type: null
  materialize_inverse: false
  legacy_edge_aliases: []
  edge_class: canonical
  canonical_cognee_edge: true
```
```yaml
candidate_edge:
  edge_id: edge.target_plus.00700.uses_output_contract
  canonical_edge_type: USES_OUTPUT_CONTRACT
  source_card_id: query_pattern.target_plus.settlement.8_2_monthly_settlement_waterfall
  target_card_id: output_contract.target_plus.metric_timeseries
  source_type: query_pattern
  target_type: output_contract
  inverse_edge_type: null
  materialize_inverse: false
  legacy_edge_aliases: []
  edge_class: canonical
  canonical_cognee_edge: true
```
```yaml
candidate_edge:
  edge_id: edge.target_plus.00701.has_execution_constraint_set
  canonical_edge_type: HAS_EXECUTION_CONSTRAINT_SET
  source_card_id: query_pattern.target_plus.settlement.8_2_monthly_settlement_waterfall
  target_card_id: execution_constraint_set.target_plus.marketplace_parser_constraints
  source_type: query_pattern
  target_type: execution_constraint_set
  inverse_edge_type: null
  materialize_inverse: false
  legacy_edge_aliases: []
  edge_class: canonical
  canonical_cognee_edge: true
```
```yaml
candidate_edge:
  edge_id: edge.target_plus.00702.uses_table
  canonical_edge_type: USES_TABLE
  source_card_id: query_pattern.target_plus.settlement.8_3_commission_validation
  target_card_id: table.zs_observe.target_settlement
  source_type: query_pattern
  target_type: table
  inverse_edge_type: null
  materialize_inverse: false
  legacy_edge_aliases:
  - query_requires_table
  edge_class: canonical
  canonical_cognee_edge: true
```
```yaml
candidate_edge:
  edge_id: edge.target_plus.00703.requires_rule
  canonical_edge_type: REQUIRES_RULE
  source_card_id: query_pattern.target_plus.settlement.8_3_commission_validation
  target_card_id: rule.target_plus.active_filter
  source_type: query_pattern
  target_type: rule
  inverse_edge_type: null
  materialize_inverse: false
  legacy_edge_aliases: []
  edge_class: canonical
  canonical_cognee_edge: true
```
```yaml
candidate_edge:
  edge_id: edge.target_plus.00704.requires_rule
  canonical_edge_type: REQUIRES_RULE
  source_card_id: query_pattern.target_plus.settlement.8_3_commission_validation
  target_card_id: rule.target_plus.currency_label_usd_values
  source_type: query_pattern
  target_type: rule
  inverse_edge_type: null
  materialize_inverse: false
  legacy_edge_aliases: []
  edge_class: canonical
  canonical_cognee_edge: true
```
```yaml
candidate_edge:
  edge_id: edge.target_plus.00705.uses_reconciliation_profile
  canonical_edge_type: USES_RECONCILIATION_PROFILE
  source_card_id: query_pattern.target_plus.settlement.8_3_commission_validation
  target_card_id: reconciliation_profile.target_plus.commission_validation
  source_type: query_pattern
  target_type: reconciliation_profile
  inverse_edge_type: null
  materialize_inverse: false
  legacy_edge_aliases: []
  edge_class: canonical
  canonical_cognee_edge: true
```
```yaml
candidate_edge:
  edge_id: edge.target_plus.00706.uses_output_contract
  canonical_edge_type: USES_OUTPUT_CONTRACT
  source_card_id: query_pattern.target_plus.settlement.8_3_commission_validation
  target_card_id: output_contract.target_plus.reconciliation_status
  source_type: query_pattern
  target_type: output_contract
  inverse_edge_type: null
  materialize_inverse: false
  legacy_edge_aliases: []
  edge_class: canonical
  canonical_cognee_edge: true
```
```yaml
candidate_edge:
  edge_id: edge.target_plus.00707.has_execution_constraint_set
  canonical_edge_type: HAS_EXECUTION_CONSTRAINT_SET
  source_card_id: query_pattern.target_plus.settlement.8_3_commission_validation
  target_card_id: execution_constraint_set.target_plus.marketplace_parser_constraints
  source_type: query_pattern
  target_type: execution_constraint_set
  inverse_edge_type: null
  materialize_inverse: false
  legacy_edge_aliases: []
  edge_class: canonical
  canonical_cognee_edge: true
```
```yaml
candidate_edge:
  edge_id: edge.target_plus.00708.uses_table
  canonical_edge_type: USES_TABLE
  source_card_id: query_pattern.target_plus.settlement.8_4_sales_settlement_reconciliation
  target_card_id: table.zs_observe.target_sales
  source_type: query_pattern
  target_type: table
  inverse_edge_type: null
  materialize_inverse: false
  legacy_edge_aliases:
  - query_requires_table
  edge_class: canonical
  canonical_cognee_edge: true
```
```yaml
candidate_edge:
  edge_id: edge.target_plus.00709.uses_table
  canonical_edge_type: USES_TABLE
  source_card_id: query_pattern.target_plus.settlement.8_4_sales_settlement_reconciliation
  target_card_id: table.zs_observe.target_settlement
  source_type: query_pattern
  target_type: table
  inverse_edge_type: null
  materialize_inverse: false
  legacy_edge_aliases:
  - query_requires_table
  edge_class: canonical
  canonical_cognee_edge: true
```
```yaml
candidate_edge:
  edge_id: edge.target_plus.00710.requires_rule
  canonical_edge_type: REQUIRES_RULE
  source_card_id: query_pattern.target_plus.settlement.8_4_sales_settlement_reconciliation
  target_card_id: rule.target_plus.active_filter
  source_type: query_pattern
  target_type: rule
  inverse_edge_type: null
  materialize_inverse: false
  legacy_edge_aliases: []
  edge_class: canonical
  canonical_cognee_edge: true
```
```yaml
candidate_edge:
  edge_id: edge.target_plus.00711.requires_rule
  canonical_edge_type: REQUIRES_RULE
  source_card_id: query_pattern.target_plus.settlement.8_4_sales_settlement_reconciliation
  target_card_id: rule.target_plus.currency_label_usd_values
  source_type: query_pattern
  target_type: rule
  inverse_edge_type: null
  materialize_inverse: false
  legacy_edge_aliases: []
  edge_class: canonical
  canonical_cognee_edge: true
```
```yaml
candidate_edge:
  edge_id: edge.target_plus.00712.requires_rule
  canonical_edge_type: REQUIRES_RULE
  source_card_id: query_pattern.target_plus.settlement.8_4_sales_settlement_reconciliation
  target_card_id: rule.target_plus.settlement_recency_gap
  source_type: query_pattern
  target_type: rule
  inverse_edge_type: null
  materialize_inverse: false
  legacy_edge_aliases: []
  edge_class: canonical
  canonical_cognee_edge: true
```
```yaml
candidate_edge:
  edge_id: edge.target_plus.00713.uses_reconciliation_profile
  canonical_edge_type: USES_RECONCILIATION_PROFILE
  source_card_id: query_pattern.target_plus.settlement.8_4_sales_settlement_reconciliation
  target_card_id: reconciliation_profile.target_plus.sales_settlement
  source_type: query_pattern
  target_type: reconciliation_profile
  inverse_edge_type: null
  materialize_inverse: false
  legacy_edge_aliases: []
  edge_class: canonical
  canonical_cognee_edge: true
```
```yaml
candidate_edge:
  edge_id: edge.target_plus.00714.uses_output_contract
  canonical_edge_type: USES_OUTPUT_CONTRACT
  source_card_id: query_pattern.target_plus.settlement.8_4_sales_settlement_reconciliation
  target_card_id: output_contract.target_plus.reconciliation_status
  source_type: query_pattern
  target_type: output_contract
  inverse_edge_type: null
  materialize_inverse: false
  legacy_edge_aliases: []
  edge_class: canonical
  canonical_cognee_edge: true
```
```yaml
candidate_edge:
  edge_id: edge.target_plus.00715.has_execution_constraint_set
  canonical_edge_type: HAS_EXECUTION_CONSTRAINT_SET
  source_card_id: query_pattern.target_plus.settlement.8_4_sales_settlement_reconciliation
  target_card_id: execution_constraint_set.target_plus.marketplace_parser_constraints
  source_type: query_pattern
  target_type: execution_constraint_set
  inverse_edge_type: null
  materialize_inverse: false
  legacy_edge_aliases: []
  edge_class: canonical
  canonical_cognee_edge: true
```
```yaml
candidate_edge:
  edge_id: edge.target_plus.00716.uses_table
  canonical_edge_type: USES_TABLE
  source_card_id: query_pattern.target_plus.settlement.8_5_effective_payout_rate
  target_card_id: table.zs_observe.target_settlement
  source_type: query_pattern
  target_type: table
  inverse_edge_type: null
  materialize_inverse: false
  legacy_edge_aliases:
  - query_requires_table
  edge_class: canonical
  canonical_cognee_edge: true
```
```yaml
candidate_edge:
  edge_id: edge.target_plus.00717.requires_rule
  canonical_edge_type: REQUIRES_RULE
  source_card_id: query_pattern.target_plus.settlement.8_5_effective_payout_rate
  target_card_id: rule.target_plus.active_filter
  source_type: query_pattern
  target_type: rule
  inverse_edge_type: null
  materialize_inverse: false
  legacy_edge_aliases: []
  edge_class: canonical
  canonical_cognee_edge: true
```
```yaml
candidate_edge:
  edge_id: edge.target_plus.00718.requires_rule
  canonical_edge_type: REQUIRES_RULE
  source_card_id: query_pattern.target_plus.settlement.8_5_effective_payout_rate
  target_card_id: rule.target_plus.currency_label_usd_values
  source_type: query_pattern
  target_type: rule
  inverse_edge_type: null
  materialize_inverse: false
  legacy_edge_aliases: []
  edge_class: canonical
  canonical_cognee_edge: true
```
```yaml
candidate_edge:
  edge_id: edge.target_plus.00719.uses_output_contract
  canonical_edge_type: USES_OUTPUT_CONTRACT
  source_card_id: query_pattern.target_plus.settlement.8_5_effective_payout_rate
  target_card_id: output_contract.target_plus.metric_timeseries
  source_type: query_pattern
  target_type: output_contract
  inverse_edge_type: null
  materialize_inverse: false
  legacy_edge_aliases: []
  edge_class: canonical
  canonical_cognee_edge: true
```
```yaml
candidate_edge:
  edge_id: edge.target_plus.00720.has_execution_constraint_set
  canonical_edge_type: HAS_EXECUTION_CONSTRAINT_SET
  source_card_id: query_pattern.target_plus.settlement.8_5_effective_payout_rate
  target_card_id: execution_constraint_set.target_plus.marketplace_parser_constraints
  source_type: query_pattern
  target_type: execution_constraint_set
  inverse_edge_type: null
  materialize_inverse: false
  legacy_edge_aliases: []
  edge_class: canonical
  canonical_cognee_edge: true
```
```yaml
candidate_edge:
  edge_id: edge.target_plus.00721.uses_table
  canonical_edge_type: USES_TABLE
  source_card_id: query_pattern.target_plus.mapping.7_1_full_catalogue_with_sales_coverage
  target_card_id: table.zs_observe.target_sales
  source_type: query_pattern
  target_type: table
  inverse_edge_type: null
  materialize_inverse: false
  legacy_edge_aliases:
  - query_requires_table
  edge_class: canonical
  canonical_cognee_edge: true
```
```yaml
candidate_edge:
  edge_id: edge.target_plus.00722.uses_table
  canonical_edge_type: USES_TABLE
  source_card_id: query_pattern.target_plus.mapping.7_1_full_catalogue_with_sales_coverage
  target_card_id: table.zs_observe.target_tcin_mapping
  source_type: query_pattern
  target_type: table
  inverse_edge_type: null
  materialize_inverse: false
  legacy_edge_aliases:
  - query_requires_table
  edge_class: canonical
  canonical_cognee_edge: true
```
```yaml
candidate_edge:
  edge_id: edge.target_plus.00723.requires_rule
  canonical_edge_type: REQUIRES_RULE
  source_card_id: query_pattern.target_plus.mapping.7_1_full_catalogue_with_sales_coverage
  target_card_id: rule.target_plus.active_filter
  source_type: query_pattern
  target_type: rule
  inverse_edge_type: null
  materialize_inverse: false
  legacy_edge_aliases: []
  edge_class: canonical
  canonical_cognee_edge: true
```
```yaml
candidate_edge:
  edge_id: edge.target_plus.00724.requires_rule
  canonical_edge_type: REQUIRES_RULE
  source_card_id: query_pattern.target_plus.mapping.7_1_full_catalogue_with_sales_coverage
  target_card_id: rule.target_plus.tcin_mapping_join
  source_type: query_pattern
  target_type: rule
  inverse_edge_type: null
  materialize_inverse: false
  legacy_edge_aliases: []
  edge_class: canonical
  canonical_cognee_edge: true
```
```yaml
candidate_edge:
  edge_id: edge.target_plus.00725.produces_metric
  canonical_edge_type: PRODUCES_METRIC
  source_card_id: query_pattern.target_plus.mapping.7_1_full_catalogue_with_sales_coverage
  target_card_id: metric.target_plus.mapping_sales_coverage
  source_type: query_pattern
  target_type: metric
  inverse_edge_type: null
  materialize_inverse: false
  legacy_edge_aliases: []
  edge_class: canonical
  canonical_cognee_edge: true
```
```yaml
candidate_edge:
  edge_id: edge.target_plus.00726.uses_reconciliation_profile
  canonical_edge_type: USES_RECONCILIATION_PROFILE
  source_card_id: query_pattern.target_plus.mapping.7_1_full_catalogue_with_sales_coverage
  target_card_id: reconciliation_profile.target_plus.tcin_mapping
  source_type: query_pattern
  target_type: reconciliation_profile
  inverse_edge_type: null
  materialize_inverse: false
  legacy_edge_aliases: []
  edge_class: canonical
  canonical_cognee_edge: true
```
```yaml
candidate_edge:
  edge_id: edge.target_plus.00727.uses_output_contract
  canonical_edge_type: USES_OUTPUT_CONTRACT
  source_card_id: query_pattern.target_plus.mapping.7_1_full_catalogue_with_sales_coverage
  target_card_id: output_contract.target_plus.reconciliation_status
  source_type: query_pattern
  target_type: output_contract
  inverse_edge_type: null
  materialize_inverse: false
  legacy_edge_aliases: []
  edge_class: canonical
  canonical_cognee_edge: true
```
```yaml
candidate_edge:
  edge_id: edge.target_plus.00728.has_execution_constraint_set
  canonical_edge_type: HAS_EXECUTION_CONSTRAINT_SET
  source_card_id: query_pattern.target_plus.mapping.7_1_full_catalogue_with_sales_coverage
  target_card_id: execution_constraint_set.target_plus.marketplace_parser_constraints
  source_type: query_pattern
  target_type: execution_constraint_set
  inverse_edge_type: null
  materialize_inverse: false
  legacy_edge_aliases: []
  edge_class: canonical
  canonical_cognee_edge: true
```
```yaml
candidate_edge:
  edge_id: edge.target_plus.00729.uses_table
  canonical_edge_type: USES_TABLE
  source_card_id: query_pattern.target_plus.mapping.7_2_brand_level_sku_count
  target_card_id: table.zs_observe.target_tcin_mapping
  source_type: query_pattern
  target_type: table
  inverse_edge_type: null
  materialize_inverse: false
  legacy_edge_aliases:
  - query_requires_table
  edge_class: canonical
  canonical_cognee_edge: true
```
```yaml
candidate_edge:
  edge_id: edge.target_plus.00730.requires_rule
  canonical_edge_type: REQUIRES_RULE
  source_card_id: query_pattern.target_plus.mapping.7_2_brand_level_sku_count
  target_card_id: rule.target_plus.active_filter
  source_type: query_pattern
  target_type: rule
  inverse_edge_type: null
  materialize_inverse: false
  legacy_edge_aliases: []
  edge_class: canonical
  canonical_cognee_edge: true
```
```yaml
candidate_edge:
  edge_id: edge.target_plus.00731.uses_output_contract
  canonical_edge_type: USES_OUTPUT_CONTRACT
  source_card_id: query_pattern.target_plus.mapping.7_2_brand_level_sku_count
  target_card_id: output_contract.target_plus.product_mapping
  source_type: query_pattern
  target_type: output_contract
  inverse_edge_type: null
  materialize_inverse: false
  legacy_edge_aliases: []
  edge_class: canonical
  canonical_cognee_edge: true
```
```yaml
candidate_edge:
  edge_id: edge.target_plus.00732.has_execution_constraint_set
  canonical_edge_type: HAS_EXECUTION_CONSTRAINT_SET
  source_card_id: query_pattern.target_plus.mapping.7_2_brand_level_sku_count
  target_card_id: execution_constraint_set.target_plus.marketplace_parser_constraints
  source_type: query_pattern
  target_type: execution_constraint_set
  inverse_edge_type: null
  materialize_inverse: false
  legacy_edge_aliases: []
  edge_class: canonical
  canonical_cognee_edge: true
```
```yaml
candidate_edge:
  edge_id: edge.target_plus.00733.uses_table
  canonical_edge_type: USES_TABLE
  source_card_id: query_pattern.target_plus.mapping.7_3_enrich_sales_with_mapping_data
  target_card_id: table.zs_observe.target_sales
  source_type: query_pattern
  target_type: table
  inverse_edge_type: null
  materialize_inverse: false
  legacy_edge_aliases:
  - query_requires_table
  edge_class: canonical
  canonical_cognee_edge: true
```
```yaml
candidate_edge:
  edge_id: edge.target_plus.00734.uses_table
  canonical_edge_type: USES_TABLE
  source_card_id: query_pattern.target_plus.mapping.7_3_enrich_sales_with_mapping_data
  target_card_id: table.zs_observe.target_tcin_mapping
  source_type: query_pattern
  target_type: table
  inverse_edge_type: null
  materialize_inverse: false
  legacy_edge_aliases:
  - query_requires_table
  edge_class: canonical
  canonical_cognee_edge: true
```
```yaml
candidate_edge:
  edge_id: edge.target_plus.00735.requires_rule
  canonical_edge_type: REQUIRES_RULE
  source_card_id: query_pattern.target_plus.mapping.7_3_enrich_sales_with_mapping_data
  target_card_id: rule.target_plus.active_filter
  source_type: query_pattern
  target_type: rule
  inverse_edge_type: null
  materialize_inverse: false
  legacy_edge_aliases: []
  edge_class: canonical
  canonical_cognee_edge: true
```
```yaml
candidate_edge:
  edge_id: edge.target_plus.00736.requires_rule
  canonical_edge_type: REQUIRES_RULE
  source_card_id: query_pattern.target_plus.mapping.7_3_enrich_sales_with_mapping_data
  target_card_id: rule.target_plus.tcin_mapping_join
  source_type: query_pattern
  target_type: rule
  inverse_edge_type: null
  materialize_inverse: false
  legacy_edge_aliases: []
  edge_class: canonical
  canonical_cognee_edge: true
```
```yaml
candidate_edge:
  edge_id: edge.target_plus.00737.uses_reconciliation_profile
  canonical_edge_type: USES_RECONCILIATION_PROFILE
  source_card_id: query_pattern.target_plus.mapping.7_3_enrich_sales_with_mapping_data
  target_card_id: reconciliation_profile.target_plus.tcin_mapping
  source_type: query_pattern
  target_type: reconciliation_profile
  inverse_edge_type: null
  materialize_inverse: false
  legacy_edge_aliases: []
  edge_class: canonical
  canonical_cognee_edge: true
```
```yaml
candidate_edge:
  edge_id: edge.target_plus.00738.uses_output_contract
  canonical_edge_type: USES_OUTPUT_CONTRACT
  source_card_id: query_pattern.target_plus.mapping.7_3_enrich_sales_with_mapping_data
  target_card_id: output_contract.target_plus.reconciliation_status
  source_type: query_pattern
  target_type: output_contract
  inverse_edge_type: null
  materialize_inverse: false
  legacy_edge_aliases: []
  edge_class: canonical
  canonical_cognee_edge: true
```
```yaml
candidate_edge:
  edge_id: edge.target_plus.00739.has_execution_constraint_set
  canonical_edge_type: HAS_EXECUTION_CONSTRAINT_SET
  source_card_id: query_pattern.target_plus.mapping.7_3_enrich_sales_with_mapping_data
  target_card_id: execution_constraint_set.target_plus.marketplace_parser_constraints
  source_type: query_pattern
  target_type: execution_constraint_set
  inverse_edge_type: null
  materialize_inverse: false
  legacy_edge_aliases: []
  edge_class: canonical
  canonical_cognee_edge: true
```
```yaml
candidate_edge:
  edge_id: edge.target_plus.00740.uses_table
  canonical_edge_type: USES_TABLE
  source_card_id: query_pattern.target_plus.returns.7_1_return_volume_and_value_by_reason
  target_card_id: table.zs_observe.target_returns
  source_type: query_pattern
  target_type: table
  inverse_edge_type: null
  materialize_inverse: false
  legacy_edge_aliases:
  - query_requires_table
  edge_class: canonical
  canonical_cognee_edge: true
```
```yaml
candidate_edge:
  edge_id: edge.target_plus.00741.requires_rule
  canonical_edge_type: REQUIRES_RULE
  source_card_id: query_pattern.target_plus.returns.7_1_return_volume_and_value_by_reason
  target_card_id: rule.target_plus.active_filter
  source_type: query_pattern
  target_type: rule
  inverse_edge_type: null
  materialize_inverse: false
  legacy_edge_aliases: []
  edge_class: canonical
  canonical_cognee_edge: true
```
```yaml
candidate_edge:
  edge_id: edge.target_plus.00742.produces_metric
  canonical_edge_type: PRODUCES_METRIC
  source_card_id: query_pattern.target_plus.returns.7_1_return_volume_and_value_by_reason
  target_card_id: metric.target_plus.return_reason_value
  source_type: query_pattern
  target_type: metric
  inverse_edge_type: null
  materialize_inverse: false
  legacy_edge_aliases: []
  edge_class: canonical
  canonical_cognee_edge: true
```
```yaml
candidate_edge:
  edge_id: edge.target_plus.00743.uses_output_contract
  canonical_edge_type: USES_OUTPUT_CONTRACT
  source_card_id: query_pattern.target_plus.returns.7_1_return_volume_and_value_by_reason
  target_card_id: output_contract.target_plus.metric_timeseries
  source_type: query_pattern
  target_type: output_contract
  inverse_edge_type: null
  materialize_inverse: false
  legacy_edge_aliases: []
  edge_class: canonical
  canonical_cognee_edge: true
```
```yaml
candidate_edge:
  edge_id: edge.target_plus.00744.has_execution_constraint_set
  canonical_edge_type: HAS_EXECUTION_CONSTRAINT_SET
  source_card_id: query_pattern.target_plus.returns.7_1_return_volume_and_value_by_reason
  target_card_id: execution_constraint_set.target_plus.marketplace_parser_constraints
  source_type: query_pattern
  target_type: execution_constraint_set
  inverse_edge_type: null
  materialize_inverse: false
  legacy_edge_aliases: []
  edge_class: canonical
  canonical_cognee_edge: true
```
```yaml
candidate_edge:
  edge_id: edge.target_plus.00745.uses_table
  canonical_edge_type: USES_TABLE
  source_card_id: query_pattern.target_plus.returns.7_2_return_rate_by_brand
  target_card_id: table.zs_observe.target_returns
  source_type: query_pattern
  target_type: table
  inverse_edge_type: null
  materialize_inverse: false
  legacy_edge_aliases:
  - query_requires_table
  edge_class: canonical
  canonical_cognee_edge: true
```
```yaml
candidate_edge:
  edge_id: edge.target_plus.00746.requires_rule
  canonical_edge_type: REQUIRES_RULE
  source_card_id: query_pattern.target_plus.returns.7_2_return_rate_by_brand
  target_card_id: rule.target_plus.active_filter
  source_type: query_pattern
  target_type: rule
  inverse_edge_type: null
  materialize_inverse: false
  legacy_edge_aliases: []
  edge_class: canonical
  canonical_cognee_edge: true
```
```yaml
candidate_edge:
  edge_id: edge.target_plus.00747.produces_metric
  canonical_edge_type: PRODUCES_METRIC
  source_card_id: query_pattern.target_plus.returns.7_2_return_rate_by_brand
  target_card_id: metric.target_plus.brand_return_rate
  source_type: query_pattern
  target_type: metric
  inverse_edge_type: null
  materialize_inverse: false
  legacy_edge_aliases: []
  edge_class: canonical
  canonical_cognee_edge: true
```
```yaml
candidate_edge:
  edge_id: edge.target_plus.00748.uses_output_contract
  canonical_edge_type: USES_OUTPUT_CONTRACT
  source_card_id: query_pattern.target_plus.returns.7_2_return_rate_by_brand
  target_card_id: output_contract.target_plus.metric_timeseries
  source_type: query_pattern
  target_type: output_contract
  inverse_edge_type: null
  materialize_inverse: false
  legacy_edge_aliases: []
  edge_class: canonical
  canonical_cognee_edge: true
```
```yaml
candidate_edge:
  edge_id: edge.target_plus.00749.has_execution_constraint_set
  canonical_edge_type: HAS_EXECUTION_CONSTRAINT_SET
  source_card_id: query_pattern.target_plus.returns.7_2_return_rate_by_brand
  target_card_id: execution_constraint_set.target_plus.marketplace_parser_constraints
  source_type: query_pattern
  target_type: execution_constraint_set
  inverse_edge_type: null
  materialize_inverse: false
  legacy_edge_aliases: []
  edge_class: canonical
  canonical_cognee_edge: true
```
```yaml
candidate_edge:
  edge_id: edge.target_plus.00750.uses_table
  canonical_edge_type: USES_TABLE
  source_card_id: query_pattern.target_plus.returns.7_3_monthly_return_trend
  target_card_id: table.zs_observe.target_returns
  source_type: query_pattern
  target_type: table
  inverse_edge_type: null
  materialize_inverse: false
  legacy_edge_aliases:
  - query_requires_table
  edge_class: canonical
  canonical_cognee_edge: true
```
```yaml
candidate_edge:
  edge_id: edge.target_plus.00751.requires_rule
  canonical_edge_type: REQUIRES_RULE
  source_card_id: query_pattern.target_plus.returns.7_3_monthly_return_trend
  target_card_id: rule.target_plus.active_filter
  source_type: query_pattern
  target_type: rule
  inverse_edge_type: null
  materialize_inverse: false
  legacy_edge_aliases: []
  edge_class: canonical
  canonical_cognee_edge: true
```
```yaml
candidate_edge:
  edge_id: edge.target_plus.00752.uses_output_contract
  canonical_edge_type: USES_OUTPUT_CONTRACT
  source_card_id: query_pattern.target_plus.returns.7_3_monthly_return_trend
  target_card_id: output_contract.target_plus.metric_timeseries
  source_type: query_pattern
  target_type: output_contract
  inverse_edge_type: null
  materialize_inverse: false
  legacy_edge_aliases: []
  edge_class: canonical
  canonical_cognee_edge: true
```
```yaml
candidate_edge:
  edge_id: edge.target_plus.00753.has_execution_constraint_set
  canonical_edge_type: HAS_EXECUTION_CONSTRAINT_SET
  source_card_id: query_pattern.target_plus.returns.7_3_monthly_return_trend
  target_card_id: execution_constraint_set.target_plus.marketplace_parser_constraints
  source_type: query_pattern
  target_type: execution_constraint_set
  inverse_edge_type: null
  materialize_inverse: false
  legacy_edge_aliases: []
  edge_class: canonical
  canonical_cognee_edge: true
```
```yaml
candidate_edge:
  edge_id: edge.target_plus.00754.uses_table
  canonical_edge_type: USES_TABLE
  source_card_id: query_pattern.target_plus.returns.7_4_returns_sales_reconciliation
  target_card_id: table.zs_observe.target_returns
  source_type: query_pattern
  target_type: table
  inverse_edge_type: null
  materialize_inverse: false
  legacy_edge_aliases:
  - query_requires_table
  edge_class: canonical
  canonical_cognee_edge: true
```
```yaml
candidate_edge:
  edge_id: edge.target_plus.00755.uses_table
  canonical_edge_type: USES_TABLE
  source_card_id: query_pattern.target_plus.returns.7_4_returns_sales_reconciliation
  target_card_id: table.zs_observe.target_sales
  source_type: query_pattern
  target_type: table
  inverse_edge_type: null
  materialize_inverse: false
  legacy_edge_aliases:
  - query_requires_table
  edge_class: canonical
  canonical_cognee_edge: true
```
```yaml
candidate_edge:
  edge_id: edge.target_plus.00756.requires_rule
  canonical_edge_type: REQUIRES_RULE
  source_card_id: query_pattern.target_plus.returns.7_4_returns_sales_reconciliation
  target_card_id: rule.target_plus.active_filter
  source_type: query_pattern
  target_type: rule
  inverse_edge_type: null
  materialize_inverse: false
  legacy_edge_aliases: []
  edge_class: canonical
  canonical_cognee_edge: true
```
```yaml
candidate_edge:
  edge_id: edge.target_plus.00757.requires_rule
  canonical_edge_type: REQUIRES_RULE
  source_card_id: query_pattern.target_plus.returns.7_4_returns_sales_reconciliation
  target_card_id: rule.target_plus.settlement_recency_gap
  source_type: query_pattern
  target_type: rule
  inverse_edge_type: null
  materialize_inverse: false
  legacy_edge_aliases: []
  edge_class: canonical
  canonical_cognee_edge: true
```
```yaml
candidate_edge:
  edge_id: edge.target_plus.00758.uses_reconciliation_profile
  canonical_edge_type: USES_RECONCILIATION_PROFILE
  source_card_id: query_pattern.target_plus.returns.7_4_returns_sales_reconciliation
  target_card_id: reconciliation_profile.target_plus.sales_settlement
  source_type: query_pattern
  target_type: reconciliation_profile
  inverse_edge_type: null
  materialize_inverse: false
  legacy_edge_aliases: []
  edge_class: canonical
  canonical_cognee_edge: true
```
```yaml
candidate_edge:
  edge_id: edge.target_plus.00759.uses_output_contract
  canonical_edge_type: USES_OUTPUT_CONTRACT
  source_card_id: query_pattern.target_plus.returns.7_4_returns_sales_reconciliation
  target_card_id: output_contract.target_plus.reconciliation_status
  source_type: query_pattern
  target_type: output_contract
  inverse_edge_type: null
  materialize_inverse: false
  legacy_edge_aliases: []
  edge_class: canonical
  canonical_cognee_edge: true
```
```yaml
candidate_edge:
  edge_id: edge.target_plus.00760.has_execution_constraint_set
  canonical_edge_type: HAS_EXECUTION_CONSTRAINT_SET
  source_card_id: query_pattern.target_plus.returns.7_4_returns_sales_reconciliation
  target_card_id: execution_constraint_set.target_plus.marketplace_parser_constraints
  source_type: query_pattern
  target_type: execution_constraint_set
  inverse_edge_type: null
  materialize_inverse: false
  legacy_edge_aliases: []
  edge_class: canonical
  canonical_cognee_edge: true
```
```yaml
candidate_edge:
  edge_id: edge.target_plus.00761.uses_table
  canonical_edge_type: USES_TABLE
  source_card_id: query_pattern.target_plus.returns.7_5_sku_level_return_rate
  target_card_id: table.zs_observe.target_returns
  source_type: query_pattern
  target_type: table
  inverse_edge_type: null
  materialize_inverse: false
  legacy_edge_aliases:
  - query_requires_table
  edge_class: canonical
  canonical_cognee_edge: true
```
```yaml
candidate_edge:
  edge_id: edge.target_plus.00762.uses_table
  canonical_edge_type: USES_TABLE
  source_card_id: query_pattern.target_plus.returns.7_5_sku_level_return_rate
  target_card_id: table.zs_observe.target_sales
  source_type: query_pattern
  target_type: table
  inverse_edge_type: null
  materialize_inverse: false
  legacy_edge_aliases:
  - query_requires_table
  edge_class: canonical
  canonical_cognee_edge: true
```
```yaml
candidate_edge:
  edge_id: edge.target_plus.00763.uses_table
  canonical_edge_type: USES_TABLE
  source_card_id: query_pattern.target_plus.returns.7_5_sku_level_return_rate
  target_card_id: table.zs_observe.target_tcin_mapping
  source_type: query_pattern
  target_type: table
  inverse_edge_type: null
  materialize_inverse: false
  legacy_edge_aliases:
  - query_requires_table
  edge_class: canonical
  canonical_cognee_edge: true
```
```yaml
candidate_edge:
  edge_id: edge.target_plus.00764.requires_rule
  canonical_edge_type: REQUIRES_RULE
  source_card_id: query_pattern.target_plus.returns.7_5_sku_level_return_rate
  target_card_id: rule.target_plus.active_filter
  source_type: query_pattern
  target_type: rule
  inverse_edge_type: null
  materialize_inverse: false
  legacy_edge_aliases: []
  edge_class: canonical
  canonical_cognee_edge: true
```
```yaml
candidate_edge:
  edge_id: edge.target_plus.00765.uses_output_contract
  canonical_edge_type: USES_OUTPUT_CONTRACT
  source_card_id: query_pattern.target_plus.returns.7_5_sku_level_return_rate
  target_card_id: output_contract.target_plus.metric_timeseries
  source_type: query_pattern
  target_type: output_contract
  inverse_edge_type: null
  materialize_inverse: false
  legacy_edge_aliases: []
  edge_class: canonical
  canonical_cognee_edge: true
```
```yaml
candidate_edge:
  edge_id: edge.target_plus.00766.has_execution_constraint_set
  canonical_edge_type: HAS_EXECUTION_CONSTRAINT_SET
  source_card_id: query_pattern.target_plus.returns.7_5_sku_level_return_rate
  target_card_id: execution_constraint_set.target_plus.marketplace_parser_constraints
  source_type: query_pattern
  target_type: execution_constraint_set
  inverse_edge_type: null
  materialize_inverse: false
  legacy_edge_aliases: []
  edge_class: canonical
  canonical_cognee_edge: true
```
```yaml
candidate_edge:
  edge_id: edge.target_plus.00767.uses_table
  canonical_edge_type: USES_TABLE
  source_card_id: query_pattern.target_plus.sales.7_1_monthly_sales_gmv_by_brand
  target_card_id: table.zs_observe.target_sales
  source_type: query_pattern
  target_type: table
  inverse_edge_type: null
  materialize_inverse: false
  legacy_edge_aliases:
  - query_requires_table
  edge_class: canonical
  canonical_cognee_edge: true
```
```yaml
candidate_edge:
  edge_id: edge.target_plus.00768.requires_rule
  canonical_edge_type: REQUIRES_RULE
  source_card_id: query_pattern.target_plus.sales.7_1_monthly_sales_gmv_by_brand
  target_card_id: rule.target_plus.active_filter
  source_type: query_pattern
  target_type: rule
  inverse_edge_type: null
  materialize_inverse: false
  legacy_edge_aliases: []
  edge_class: canonical
  canonical_cognee_edge: true
```
```yaml
candidate_edge:
  edge_id: edge.target_plus.00769.produces_metric
  canonical_edge_type: PRODUCES_METRIC
  source_card_id: query_pattern.target_plus.sales.7_1_monthly_sales_gmv_by_brand
  target_card_id: metric.target_plus.monthly_sales_gmv
  source_type: query_pattern
  target_type: metric
  inverse_edge_type: null
  materialize_inverse: false
  legacy_edge_aliases: []
  edge_class: canonical
  canonical_cognee_edge: true
```
```yaml
candidate_edge:
  edge_id: edge.target_plus.00770.uses_output_contract
  canonical_edge_type: USES_OUTPUT_CONTRACT
  source_card_id: query_pattern.target_plus.sales.7_1_monthly_sales_gmv_by_brand
  target_card_id: output_contract.target_plus.metric_timeseries
  source_type: query_pattern
  target_type: output_contract
  inverse_edge_type: null
  materialize_inverse: false
  legacy_edge_aliases: []
  edge_class: canonical
  canonical_cognee_edge: true
```
```yaml
candidate_edge:
  edge_id: edge.target_plus.00771.has_execution_constraint_set
  canonical_edge_type: HAS_EXECUTION_CONSTRAINT_SET
  source_card_id: query_pattern.target_plus.sales.7_1_monthly_sales_gmv_by_brand
  target_card_id: execution_constraint_set.target_plus.marketplace_parser_constraints
  source_type: query_pattern
  target_type: execution_constraint_set
  inverse_edge_type: null
  materialize_inverse: false
  legacy_edge_aliases: []
  edge_class: canonical
  canonical_cognee_edge: true
```
```yaml
candidate_edge:
  edge_id: edge.target_plus.00772.uses_table
  canonical_edge_type: USES_TABLE
  source_card_id: query_pattern.target_plus.sales.7_2_sku_level_sales_performance
  target_card_id: table.zs_observe.target_sales
  source_type: query_pattern
  target_type: table
  inverse_edge_type: null
  materialize_inverse: false
  legacy_edge_aliases:
  - query_requires_table
  edge_class: canonical
  canonical_cognee_edge: true
```
```yaml
candidate_edge:
  edge_id: edge.target_plus.00773.uses_table
  canonical_edge_type: USES_TABLE
  source_card_id: query_pattern.target_plus.sales.7_2_sku_level_sales_performance
  target_card_id: table.zs_observe.target_tcin_mapping
  source_type: query_pattern
  target_type: table
  inverse_edge_type: null
  materialize_inverse: false
  legacy_edge_aliases:
  - query_requires_table
  edge_class: canonical
  canonical_cognee_edge: true
```
```yaml
candidate_edge:
  edge_id: edge.target_plus.00774.requires_rule
  canonical_edge_type: REQUIRES_RULE
  source_card_id: query_pattern.target_plus.sales.7_2_sku_level_sales_performance
  target_card_id: rule.target_plus.active_filter
  source_type: query_pattern
  target_type: rule
  inverse_edge_type: null
  materialize_inverse: false
  legacy_edge_aliases: []
  edge_class: canonical
  canonical_cognee_edge: true
```
```yaml
candidate_edge:
  edge_id: edge.target_plus.00775.uses_output_contract
  canonical_edge_type: USES_OUTPUT_CONTRACT
  source_card_id: query_pattern.target_plus.sales.7_2_sku_level_sales_performance
  target_card_id: output_contract.target_plus.metric_timeseries
  source_type: query_pattern
  target_type: output_contract
  inverse_edge_type: null
  materialize_inverse: false
  legacy_edge_aliases: []
  edge_class: canonical
  canonical_cognee_edge: true
```
```yaml
candidate_edge:
  edge_id: edge.target_plus.00776.has_execution_constraint_set
  canonical_edge_type: HAS_EXECUTION_CONSTRAINT_SET
  source_card_id: query_pattern.target_plus.sales.7_2_sku_level_sales_performance
  target_card_id: execution_constraint_set.target_plus.marketplace_parser_constraints
  source_type: query_pattern
  target_type: execution_constraint_set
  inverse_edge_type: null
  materialize_inverse: false
  legacy_edge_aliases: []
  edge_class: canonical
  canonical_cognee_edge: true
```
```yaml
candidate_edge:
  edge_id: edge.target_plus.00777.uses_table
  canonical_edge_type: USES_TABLE
  source_card_id: query_pattern.target_plus.sales.7_3_sales_settlement_join
  target_card_id: table.zs_observe.target_sales
  source_type: query_pattern
  target_type: table
  inverse_edge_type: null
  materialize_inverse: false
  legacy_edge_aliases:
  - query_requires_table
  edge_class: canonical
  canonical_cognee_edge: true
```
```yaml
candidate_edge:
  edge_id: edge.target_plus.00778.uses_table
  canonical_edge_type: USES_TABLE
  source_card_id: query_pattern.target_plus.sales.7_3_sales_settlement_join
  target_card_id: table.zs_observe.target_settlement
  source_type: query_pattern
  target_type: table
  inverse_edge_type: null
  materialize_inverse: false
  legacy_edge_aliases:
  - query_requires_table
  edge_class: canonical
  canonical_cognee_edge: true
```
```yaml
candidate_edge:
  edge_id: edge.target_plus.00779.requires_rule
  canonical_edge_type: REQUIRES_RULE
  source_card_id: query_pattern.target_plus.sales.7_3_sales_settlement_join
  target_card_id: rule.target_plus.active_filter
  source_type: query_pattern
  target_type: rule
  inverse_edge_type: null
  materialize_inverse: false
  legacy_edge_aliases: []
  edge_class: canonical
  canonical_cognee_edge: true
```
```yaml
candidate_edge:
  edge_id: edge.target_plus.00780.requires_rule
  canonical_edge_type: REQUIRES_RULE
  source_card_id: query_pattern.target_plus.sales.7_3_sales_settlement_join
  target_card_id: rule.target_plus.currency_label_usd_values
  source_type: query_pattern
  target_type: rule
  inverse_edge_type: null
  materialize_inverse: false
  legacy_edge_aliases: []
  edge_class: canonical
  canonical_cognee_edge: true
```
```yaml
candidate_edge:
  edge_id: edge.target_plus.00781.requires_rule
  canonical_edge_type: REQUIRES_RULE
  source_card_id: query_pattern.target_plus.sales.7_3_sales_settlement_join
  target_card_id: rule.target_plus.settlement_recency_gap
  source_type: query_pattern
  target_type: rule
  inverse_edge_type: null
  materialize_inverse: false
  legacy_edge_aliases: []
  edge_class: canonical
  canonical_cognee_edge: true
```
```yaml
candidate_edge:
  edge_id: edge.target_plus.00782.uses_reconciliation_profile
  canonical_edge_type: USES_RECONCILIATION_PROFILE
  source_card_id: query_pattern.target_plus.sales.7_3_sales_settlement_join
  target_card_id: reconciliation_profile.target_plus.sales_settlement
  source_type: query_pattern
  target_type: reconciliation_profile
  inverse_edge_type: null
  materialize_inverse: false
  legacy_edge_aliases: []
  edge_class: canonical
  canonical_cognee_edge: true
```
```yaml
candidate_edge:
  edge_id: edge.target_plus.00783.uses_output_contract
  canonical_edge_type: USES_OUTPUT_CONTRACT
  source_card_id: query_pattern.target_plus.sales.7_3_sales_settlement_join
  target_card_id: output_contract.target_plus.reconciliation_status
  source_type: query_pattern
  target_type: output_contract
  inverse_edge_type: null
  materialize_inverse: false
  legacy_edge_aliases: []
  edge_class: canonical
  canonical_cognee_edge: true
```
```yaml
candidate_edge:
  edge_id: edge.target_plus.00784.has_execution_constraint_set
  canonical_edge_type: HAS_EXECUTION_CONSTRAINT_SET
  source_card_id: query_pattern.target_plus.sales.7_3_sales_settlement_join
  target_card_id: execution_constraint_set.target_plus.marketplace_parser_constraints
  source_type: query_pattern
  target_type: execution_constraint_set
  inverse_edge_type: null
  materialize_inverse: false
  legacy_edge_aliases: []
  edge_class: canonical
  canonical_cognee_edge: true
```
```yaml
candidate_edge:
  edge_id: edge.target_plus.00785.uses_table
  canonical_edge_type: USES_TABLE
  source_card_id: query_pattern.target_plus.sales.7_4_return_rate_by_brand
  target_card_id: table.zs_observe.target_returns
  source_type: query_pattern
  target_type: table
  inverse_edge_type: null
  materialize_inverse: false
  legacy_edge_aliases:
  - query_requires_table
  edge_class: canonical
  canonical_cognee_edge: true
```
```yaml
candidate_edge:
  edge_id: edge.target_plus.00786.uses_table
  canonical_edge_type: USES_TABLE
  source_card_id: query_pattern.target_plus.sales.7_4_return_rate_by_brand
  target_card_id: table.zs_observe.target_sales
  source_type: query_pattern
  target_type: table
  inverse_edge_type: null
  materialize_inverse: false
  legacy_edge_aliases:
  - query_requires_table
  edge_class: canonical
  canonical_cognee_edge: true
```
```yaml
candidate_edge:
  edge_id: edge.target_plus.00787.requires_rule
  canonical_edge_type: REQUIRES_RULE
  source_card_id: query_pattern.target_plus.sales.7_4_return_rate_by_brand
  target_card_id: rule.target_plus.active_filter
  source_type: query_pattern
  target_type: rule
  inverse_edge_type: null
  materialize_inverse: false
  legacy_edge_aliases: []
  edge_class: canonical
  canonical_cognee_edge: true
```
```yaml
candidate_edge:
  edge_id: edge.target_plus.00788.uses_output_contract
  canonical_edge_type: USES_OUTPUT_CONTRACT
  source_card_id: query_pattern.target_plus.sales.7_4_return_rate_by_brand
  target_card_id: output_contract.target_plus.metric_timeseries
  source_type: query_pattern
  target_type: output_contract
  inverse_edge_type: null
  materialize_inverse: false
  legacy_edge_aliases: []
  edge_class: canonical
  canonical_cognee_edge: true
```
```yaml
candidate_edge:
  edge_id: edge.target_plus.00789.has_execution_constraint_set
  canonical_edge_type: HAS_EXECUTION_CONSTRAINT_SET
  source_card_id: query_pattern.target_plus.sales.7_4_return_rate_by_brand
  target_card_id: execution_constraint_set.target_plus.marketplace_parser_constraints
  source_type: query_pattern
  target_type: execution_constraint_set
  inverse_edge_type: null
  materialize_inverse: false
  legacy_edge_aliases: []
  edge_class: canonical
  canonical_cognee_edge: true
```
```yaml
candidate_edge:
  edge_id: edge.target_plus.00790.includes_rule
  canonical_edge_type: INCLUDES_RULE
  source_card_id: execution_constraint_set.target_plus.marketplace_parser_constraints
  target_card_id: rule.target_plus.active_filter
  source_type: execution_constraint_set
  target_type: rule
  inverse_edge_type: null
  materialize_inverse: false
  legacy_edge_aliases:
  - rule_enforced_by_constraint
  edge_class: canonical
  canonical_cognee_edge: true
```
```yaml
candidate_edge:
  edge_id: edge.target_plus.00791.includes_rule
  canonical_edge_type: INCLUDES_RULE
  source_card_id: execution_constraint_set.target_plus.marketplace_parser_constraints
  target_card_id: rule.target_plus.scope_group_123
  source_type: execution_constraint_set
  target_type: rule
  inverse_edge_type: null
  materialize_inverse: false
  legacy_edge_aliases:
  - rule_enforced_by_constraint
  edge_class: canonical
  canonical_cognee_edge: true
```
```yaml
candidate_edge:
  edge_id: edge.target_plus.00792.includes_rule
  canonical_edge_type: INCLUDES_RULE
  source_card_id: execution_constraint_set.target_plus.marketplace_parser_constraints
  target_card_id: rule.target_plus.currency_label_usd_values
  source_type: execution_constraint_set
  target_type: rule
  inverse_edge_type: null
  materialize_inverse: false
  legacy_edge_aliases:
  - rule_enforced_by_constraint
  edge_class: canonical
  canonical_cognee_edge: true
```
```yaml
candidate_edge:
  edge_id: edge.target_plus.00793.includes_rule
  canonical_edge_type: INCLUDES_RULE
  source_card_id: execution_constraint_set.target_plus.marketplace_parser_constraints
  target_card_id: rule.target_plus.tcin_mapping_join
  source_type: execution_constraint_set
  target_type: rule
  inverse_edge_type: null
  materialize_inverse: false
  legacy_edge_aliases:
  - rule_enforced_by_constraint
  edge_class: canonical
  canonical_cognee_edge: true
```
```yaml
candidate_edge:
  edge_id: edge.target_plus.00794.includes_rule
  canonical_edge_type: INCLUDES_RULE
  source_card_id: execution_constraint_set.target_plus.marketplace_parser_constraints
  target_card_id: rule.target_plus.reverse_charge_not_return
  source_type: execution_constraint_set
  target_type: rule
  inverse_edge_type: null
  materialize_inverse: false
  legacy_edge_aliases:
  - rule_enforced_by_constraint
  edge_class: canonical
  canonical_cognee_edge: true
```
```yaml
candidate_edge:
  edge_id: edge.target_plus.00795.includes_rule
  canonical_edge_type: INCLUDES_RULE
  source_card_id: execution_constraint_set.target_plus.marketplace_parser_constraints
  target_card_id: rule.target_plus.marketplace_boundary
  source_type: execution_constraint_set
  target_type: rule
  inverse_edge_type: null
  materialize_inverse: false
  legacy_edge_aliases:
  - rule_enforced_by_constraint
  edge_class: canonical
  canonical_cognee_edge: true
```
```yaml
candidate_edge:
  edge_id: edge.target_plus.00796.includes_validation_test
  canonical_edge_type: INCLUDES_VALIDATION_TEST
  source_card_id: execution_constraint_set.target_plus.marketplace_parser_constraints
  target_card_id: validation_test.target_plus.active_filter
  source_type: execution_constraint_set
  target_type: validation_test
  inverse_edge_type: null
  materialize_inverse: false
  legacy_edge_aliases:
  - validation_enforces_constraint
  edge_class: canonical
  canonical_cognee_edge: true
```
```yaml
candidate_edge:
  edge_id: edge.target_plus.00797.includes_validation_test
  canonical_edge_type: INCLUDES_VALIDATION_TEST
  source_card_id: execution_constraint_set.target_plus.marketplace_parser_constraints
  target_card_id: validation_test.target_plus.no_forbidden_cards
  source_type: execution_constraint_set
  target_type: validation_test
  inverse_edge_type: null
  materialize_inverse: false
  legacy_edge_aliases:
  - validation_enforces_constraint
  edge_class: canonical
  canonical_cognee_edge: true
```
```yaml
candidate_edge:
  edge_id: edge.target_plus.00798.includes_validation_test
  canonical_edge_type: INCLUDES_VALIDATION_TEST
  source_card_id: execution_constraint_set.target_plus.marketplace_parser_constraints
  target_card_id: validation_test.target_plus.no_reverse_charge_return_mix
  source_type: execution_constraint_set
  target_type: validation_test
  inverse_edge_type: null
  materialize_inverse: false
  legacy_edge_aliases:
  - validation_enforces_constraint
  edge_class: canonical
  canonical_cognee_edge: true
```
```yaml
candidate_edge:
  edge_id: edge.target_plus.00799.includes_validation_test
  canonical_edge_type: INCLUDES_VALIDATION_TEST
  source_card_id: execution_constraint_set.target_plus.marketplace_parser_constraints
  target_card_id: validation_test.target_plus.mapping_join_tcin
  source_type: execution_constraint_set
  target_type: validation_test
  inverse_edge_type: null
  materialize_inverse: false
  legacy_edge_aliases:
  - validation_enforces_constraint
  edge_class: canonical
  canonical_cognee_edge: true
```
```yaml
candidate_edge:
  edge_id: edge.target_plus.00800.uses_output_contract
  canonical_edge_type: USES_OUTPUT_CONTRACT
  source_card_id: execution_constraint_set.target_plus.marketplace_parser_constraints
  target_card_id: output_contract.target_plus.metric_timeseries
  source_type: execution_constraint_set
  target_type: output_contract
  inverse_edge_type: null
  materialize_inverse: false
  legacy_edge_aliases: []
  edge_class: canonical
  canonical_cognee_edge: true
```
```yaml
candidate_edge:
  edge_id: edge.target_plus.00801.uses_output_contract
  canonical_edge_type: USES_OUTPUT_CONTRACT
  source_card_id: execution_constraint_set.target_plus.marketplace_parser_constraints
  target_card_id: output_contract.target_plus.reconciliation_status
  source_type: execution_constraint_set
  target_type: output_contract
  inverse_edge_type: null
  materialize_inverse: false
  legacy_edge_aliases: []
  edge_class: canonical
  canonical_cognee_edge: true
```
```yaml
candidate_edge:
  edge_id: edge.target_plus.00802.uses_output_contract
  canonical_edge_type: USES_OUTPUT_CONTRACT
  source_card_id: execution_constraint_set.target_plus.marketplace_parser_constraints
  target_card_id: output_contract.target_plus.product_mapping
  source_type: execution_constraint_set
  target_type: output_contract
  inverse_edge_type: null
  materialize_inverse: false
  legacy_edge_aliases: []
  edge_class: canonical
  canonical_cognee_edge: true
```
## 6. Review Items

```yaml
review_item:
  id: review.target_plus.runtime_scope_selection
  status: open
  issue_type: external_runtime_scope
  summary: Source documents group_level_id=123, but actual user/account runtime selection is external to this marketplace markdown.
  needed_evidence: Runtime account-scope binding layer outside this source document.
  evidence_refs:
  - ev.target_plus.marketplace.1_3_seller_entities_in_dataset
  - ev.target_plus.marketplace.8_mandatory_query_filters
```
```yaml
review_item:
  id: review.target_plus.shipping_fee_basis
  status: open
  issue_type: missing_formula_components
  summary: Shipping_amount is visible and totalled, but weight/zone shipping-fee basis is not exposed as columns/formula in Target tables.
  needed_evidence: Weight, zone, carrier/service level, or Target shipping-fee computation source if shipping charge audit is required.
  evidence_refs:
  - ev.target_plus.marketplace.4_1_commission_structure_confirmed_by_data
  - ev.target_plus.settlement.3_schema_details_37_columns_2
```
```yaml
review_item:
  id: review.target_plus.reverse_charge_tax_basis
  status: open
  issue_type: ambiguous_tax_adjustment_basis
  summary: Reverse charge rows are documented as MPF tax adjustments while total_tax remains 0; detailed remittance/basis reconstruction
    is not fully exposed.
  needed_evidence: External Target tax remittance detail or reverse charge basis mapping if exact tax remittance reconciliation is required.
  evidence_refs:
  - ev.target_plus.marketplace.2_3_reverse_charge_flow
  - ev.target_plus.marketplace.4_3_us_sales_tax_marketplace_facilitator_model
```
```yaml
review_item:
  id: review.target_plus.sku_id_direct_join
  status: open
  issue_type: ambiguous_identifier_mapping
  summary: Transaction sku_id is Shopify-format while mapping sku_id is clean seller SKU; direct sku_id joins are not supported by the
    source.
  needed_evidence: Explicit Shopify-variant-to-clean-SKU bridge if direct SKU joins are needed instead of TCIN joins.
  evidence_refs:
  - ev.target_plus.mapping.1_table_overview
  - ev.target_plus.sales.sku_id_format
```
```yaml
review_item:
  id: review.target_plus.future_return_settlement_window
  status: open
  issue_type: timing_window_external
  summary: Returns returned_date extends into 2026 while settlement source ends Nov 2025; future refund settlement coverage cannot be
    finalized from current source.
  needed_evidence: Later settlement extracts or runtime date cutoffs for post-Nov 2025 return settlements.
  evidence_refs:
  - ev.target_plus.returns.2_key_statistics
  - ev.target_plus.settlement.2_key_statistics_2
```
## 7. Parser QA Summary

```yaml
parser_quality_manifest:
  candidate_cards: 286
  candidate_edges: 802
  source_evidence_count: 144
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
  raw_source_sha256: 2fb29194e31f683d26544cdfedd1e744ac4903c74e6fe89015618d6d8b6050e8
  raw_source_line_count: 1718
  qa_notes:
    missing_edge_reference_ids: []
    dangling_sql_refs: []
    missing_evidence_refs: []
    lazy_workflow_step_ids: []
    unsupported_metric_implementation_ids: []
    forbidden_cards: []
    isolated_cards: []
```
## 8. Source Capture Appendix — Full DOCX Text

The following appendix preserves the Target Plus DOCX source text as extracted. It is included to ensure marketplace-relevant information remains auditable even where it is represented as evidence, caveats, or raw source rather than as canonical cards.

````text
Tab 1
# Target Plus — Business Knowledge Base

## 1. Target Plus Marketplace Overview

### 1.1 Background

Target Plus is an invite-only program that enables third-party retailers to sell on [Target.com](http://Target.com). Target does not charge a setup fee or monthly seller fee, but does charge a referral rate for every sale — a commission fee calculated as a percentage of an item's sale price, typically ranging from 5% to 15%.

Target Plus was launched in **February 2019** by Target Corporation, the US-based retail giant headquartered in Minneapolis, Minnesota. It operates as a **curated, invite-only marketplace** — significantly different from open platforms like Amazon or Walmart Marketplace.

**Key characteristics:**

* **Invite-only:** Target handpicks brands and sellers; no open application accepted by default
* **US-only:** Target Plus does not support dropshipping. All sellers must maintain their own inventory and fulfill orders directly.
* **No fulfillment service:** Target does not offer warehouse/FBA-style fulfillment — sellers ship directly
* Target handles any customer returns, with no hidden charges or fulfillment fees — sellers pay only the referral fee.
* **Payment via Stripe:** Sellers must set up a free account with Target's third-party money transmitter (Stripe). All shipping fees collected are transferred to the seller after applicable referral fees.
* **Marketplace facilitator taxes:** Target collects and remits US sales tax in all applicable states on behalf of sellers — confirmed by `total_tax = $0` in the settlement table

### 1.2 Seller Eligibility

Requirements include a U.S. business and banking presence, the ability to maintain price parity across channels, compliance with shipping standards (24-hour fulfillment, 5-day transit). Sellers must use approved carriers (UPS, USPS, FedEx) and cannot use competitor fulfillment services (Amazon or Walmart) to ship Target Plus orders.

### 1.3 Seller Entities in Dataset

| group_level_id | Entity | Brands | Categories | Products |
|----------------|--------|--------|------------|----------|
| 123            | Mensa brand group | Folkculture, Katchon | Party supplies, craft kits, seasonal décor | Decorative items, party accessories |

### 1.4 Brand Profiles

**Folkculture:**

* 187 SKUs on Target, 170 active in sales
* Average selling price: \~$25.56
* Core products: Party supplies, festive decorations, craft kits
* Also listed on Amazon (all SKUs have ASINs — B07... / B08... format)

**Katchon:**

* 144 SKUs on Target, 119 active in sales
* Average selling price: \~$12.99 (lower price point than Folkculture)
* Core products: Craft accessories, party items, smaller-format products


---

## 2. Transaction Lifecycle

### 2.1 Forward Order Flow

```
Customer places order on Target.com / Target app
  (authenticated buyer — may apply RedCard 5% discount)
        ↓
Order created → appears in target_sales
(transaction_type='forward', order_status='SHIPPED')
(item_id = order_id + '-' + line_item_number)
        ↓
Seller receives order notification
(must ship within 24 hours via UPS/USPS/FedEx
 in unbranded packaging — no Amazon/Walmart markings)
        ↓
Seller ships; order fulfilled
(order_status = 'SHIPPED' in target_sales)
        ↓
Buyer receives within 5 business days
        ↓
Stripe transfer created → target_settlement
(transfer_id generated, transaction_type='forward')
        ↓
Settlement batch aggregated into payout
(payout_id groups multiple transfers)
        ↓
Net payout deposited to seller's Stripe → bank account
(settled_amount = charged_amount_excl_tax − 15% commission)
```

### 2.2 Return Flow

```
Buyer initiates return
  (via Target.com, Target app, or any Target physical store)
        ↓
Target handles return logistics on seller's behalf
  ← This is a key Target Plus differentiator ←
        ↓
Return appears in target_returns
(transaction_type='reverse', internal_txn_type='reverse')
(description = return reason, e.g., 'Changed Mind')
        ↓
Return processed; refund issued to buyer
(internal_txn_type='refunds' row also appears)
        ↓
Settlement reversed → target_settlement
(transaction_type='reverse', internal_txn_type='refunds')
(settled_amount = negative → deducted from seller's next payout)
(commission reversed = +15% credit back to seller)
```

### 2.3 Reverse Charge Flow

```
Target facilitates sales tax on seller's behalf (MPF model)
        ↓
target_settlement: transaction_type='reverse charge', internal_txn_type='others'
(charged_amount = tax base; settled_amount = negative adjustment)
(gross_commission = 0; gross_commission_percentage = 0)
        ↓
Tax remittance deducted from seller's payout
Note: total_tax = 0 in all rows — Target handles tax transparency
```


---

## 3. Entity Relationships Across Tables

### 3.1 Join Map

```
target_tcin_mapping
  tcin  ←──────────────────→  tcin   target_sales
  sku_id (clean)              sku_id (Shopify format)
  brand, asin, barcode         ↕
                             item_id  ←────────────→  item_id   target_settlement
                             order_id ←────────────→  order_id  target_returns
                             tcin     ←────────────→  tcin      target_settlement
                                                       tcin      target_returns
```

### 3.2 Primary Join Keys

| Join | Left Table | Right Table | Key | Coverage |
|------|------------|-------------|-----|----------|
| Sales → Settlement | target_sales | target_settlement | `item_id` = `item_id` | 5,363 / 8,538 = **63%** |
| Sales → Returns | target_sales | target_returns | `order_id` = `order_id` | \~1,050 of sales orders |
| Returns → Settlement | target_returns | target_settlement | `item_id` = `item_id` | 385 / 1,050 = **37%** |
| All → TCIN Mapping | All        | target_tcin_mapping | `tcin` = `tcin` | Sales: 291/293 = **99%** |

> **Coverage gaps explained:** Settlement data runs Apr–Nov 2025; sales run Apr–Dec 2025. Dec 2025 sales (and return settlements) are not yet in the settlement table. This is expected and not a data quality issue.


---

## 4. Fee Structure & Financial Waterfall

### 4.1 Commission Structure (Confirmed by Data)

Target Plus charges a **flat 15% referral fee** for all products in the current dataset.

| Component | Rate | Basis | Observed in Data |
|-----------|------|-------|------------------|
| Referral fee (commission) | **15%** | `charged_amount_excluding_tax` | `gross_commission_percentage = 0.1500` — 100% of rows |
| Shipping fee | Varies | Weight + zone | `shipping_amount` — ₹1,934 total |
| Payment processing | 0%   | Stripe handled by Target | Not separately visible |
| Fixed/closing fee | 0%   | Not charged | Absent from settlement |
| Monthly/listing fee | 0%   | Not charged | Not charged by Target Plus |
| Fulfillment fee | 0%   | Seller self-fulfils | Not charged by Target Plus |

> **Note:** Target referral fees range from 5% to 15% depending on the product category. The dataset shows a flat 15% for both Folkculture and Katchon — consistent with the party supplies / general merchandise category tier.

### 4.2 Full Payout Waterfall (Forward Sales — Observed)

```
Gross Charged Amount (per-unit price)          ₹1,32,081
× Quantity
= charged_amount_excluding_tax                 ₹1,40,429
+ Shipping Amount                               +₹1,983
                                              ──────────
  Total Settlement Base                        ₹1,42,412
  − Gross Commission (15%)                    −₹21,069
                                              ──────────
  Net Forward Settled                          ₹1,21,342  (85.2% payout ratio)
  − Return Refunds (net of commission reversal) −₹9,185
  − Reverse Charge (tax adjustments)           −₹1,721
                                              ──────────
  Total Net Payout (all events)               ₹1,10,436
```

### 4.3 US Sales Tax — Marketplace Facilitator Model

Target acts as a **Marketplace Facilitator (MPF)** across all 50 US states. This means:

* Target collects US sales tax from buyers at point of purchase
* Target remits the tax directly to each state
* Seller sees `total_tax = $0.00` in settlement — tax is invisible
* `reverse charge` rows represent internal tax accounting adjustments

**Implication for GST/TDS:** As a US marketplace, Target Plus has **no Indian TCS or TDS obligations**. There are no `total_tcs_amount` or `tds_194o_rate` fields in any Target table — confirming pure USD transactions with US tax handling.

### 4.4 Return Handling

Target handles any customer returns — buyers return items to Target stores or via mail. Sellers must accept palletized in-store returns and individual mail-in returns, and provide free return shipping. Return costs are not directly visible as deductions in the settlement; instead, the full refund amount is reversed and the commission is credited back.


---

## 5. Key Business Metrics (with SQL)

### 5.1 Total GMV

```sql
SELECT
  SUM(charged_amount) AS gross_gmv,
  SUM(discount_amount) AS total_discounts,
  SUM(charged_amount) + SUM(discount_amount) AS net_gmv
FROM zs_observe.target_sales
WHERE is_active = true AND order_status = 'SHIPPED';
-- Observed: $169,909 gross GMV; −$2,834 discounts
```

### 5.2 Net Revenue (Settlement View)

```sql
SELECT
  SUM(CASE WHEN transaction_type='forward' THEN settled_amount ELSE 0 END) AS forward_settled,
  SUM(CASE WHEN transaction_type='reverse' THEN settled_amount ELSE 0 END) AS return_adjustments,
  SUM(CASE WHEN transaction_type='reverse charge' THEN settled_amount ELSE 0 END) AS tax_adjustments,
  SUM(settled_amount) AS net_revenue
FROM zs_observe.target_settlement
WHERE is_active = true;
-- Observed: $121,342 forward − $9,185 returns − $1,721 tax adj = $110,436 net
```

### 5.3 Return Rate

```sql
SELECT
  ROUND(100.0 * COUNT(DISTINCT r.order_id)
    / NULLIF(COUNT(DISTINCT s.order_id), 0), 2) AS return_rate_pct
FROM zs_observe.target_sales s
LEFT JOIN zs_observe.target_returns r
  ON s.order_id = r.order_id AND r.is_active = true
WHERE s.is_active = true AND s.order_status = 'SHIPPED';
-- Observed: ~12.3% (1050 returns / 8538 orders)
```

### 5.4 Average Order Value (AOV)

```sql
SELECT AVG(charged_amount) AS aov
FROM zs_observe.target_sales
WHERE is_active = true AND order_status = 'SHIPPED';
-- Observed: $23.37 (blended); Folkculture $25.56; Katchon $12.99
```

### 5.5 Effective Payout Rate

```sql
SELECT
  ROUND(100.0 * SUM(settled_amount)
    / NULLIF(SUM(charged_amount_excluding_tax), 0), 2) AS payout_rate_pct
FROM zs_observe.target_settlement
WHERE is_active = true AND transaction_type = 'forward';
-- Observed: 85.2%
```

### 5.6 Top Selling SKUs

```sql
SELECT
  s.tcin, m.sku_id, m.brand, m.asin,
  COUNT(s.order_id) AS units_sold,
  SUM(s.charged_amount) AS revenue
FROM zs_observe.target_sales s
JOIN zs_observe.target_tcin_mapping m ON s.tcin = m.tcin AND m.is_active = true
WHERE s.is_active = true AND s.order_status = 'SHIPPED'
GROUP BY s.tcin, m.sku_id, m.brand, m.asin
ORDER BY units_sold DESC
LIMIT 20;
```

### 5.7 Cancellation Rate

```sql
SELECT
  ROUND(100.0 * COUNT_IF(order_status = 'CANCELED')
    / NULLIF(COUNT(*), 0), 2) AS cancel_rate_pct
FROM zs_observe.target_sales
WHERE is_active = true;
-- Observed: 22/7291 = 0.30% (very low)
```


---

## 6. Reconciliation Use Cases

### 6.1 Sales ↔ Settlement Reconciliation

```sql
SELECT
  s.order_id, s.item_id, s.brand,
  s.charged_amount AS sales_price,
  st.charged_amount_excluding_tax AS settlement_revenue,
  st.gross_commission,
  st.settled_amount,
  CASE
    WHEN st.item_id IS NULL THEN 'Not Yet Settled'
    WHEN ABS(s.charged_amount - st.charged_amount) < 0.01 THEN 'Matched'
    ELSE 'Price Variance'
  END AS recon_status
FROM zs_observe.target_sales s
LEFT JOIN zs_observe.target_settlement st
  ON s.item_id = st.item_id
  AND st.is_active = true
  AND st.transaction_type = 'forward'
WHERE s.is_active = true AND s.order_status = 'SHIPPED';
```

### 6.2 Returns ↔ Settlement Refund Match

```sql
SELECT
  r.order_id, r.tcin, r.description AS return_reason,
  r.charged_amount AS return_value,
  st.settled_amount AS refund_settled,
  CASE WHEN st.item_id IS NULL THEN 'Refund Pending' ELSE 'Refund Settled' END AS status
FROM zs_observe.target_returns r
LEFT JOIN zs_observe.target_settlement st
  ON r.item_id = st.item_id
  AND st.is_active = true
  AND st.transaction_type = 'reverse'
WHERE r.is_active = true AND r.internal_txn_type = 'reverse';
```

### 6.3 Commission Validation

```sql
SELECT
  st.brand, st.tcin,
  st.charged_amount_excluding_tax AS taxable_base,
  st.gross_commission AS commission_charged,
  ROUND(st.charged_amount_excluding_tax * 0.15, 4) AS expected_commission,
  ABS(st.gross_commission - ROUND(st.charged_amount_excluding_tax * 0.15, 4)) AS variance
FROM zs_observe.target_settlement st
WHERE is_active = true
  AND transaction_type = 'forward'
  AND ABS(st.gross_commission - ROUND(st.charged_amount_excluding_tax * 0.15, 4)) > 0.01;
-- Identifies any rows where actual commission deviates from 15%
```

### 6.4 Payout Reconciliation

```sql
SELECT
  payout_id,
  SUM(settled_amount) AS total_payout,
  COUNT(DISTINCT order_id) AS orders_in_payout,
  MIN(created_date) AS earliest_txn,
  MAX(created_date) AS latest_txn,
  COUNT_IF(transaction_type = 'forward') AS sales_rows,
  COUNT_IF(transaction_type = 'reverse') AS return_rows,
  COUNT_IF(transaction_type = 'reverse charge') AS tax_rows
FROM zs_observe.target_settlement
WHERE is_active = true
GROUP BY payout_id
ORDER BY earliest_txn;
```


---

## 7. Data Quality Observations & Known Issues

| Issue | Table(s) | Detail | Mitigation |
|-------|----------|--------|------------|
| `currency_type = INR` but values are USD | All 4 tables | Field label is INR; all amounts are in USD ($) | Treat all financial values as USD |
| Settlement ends Nov 2025 | target_settlement | Dec 2025 sales not yet settled at data cutoff | Expected recency gap; compare sales/settlement over matching date ranges |
| `charged_amount` vs `charged_amount_excluding_tax` | target_settlement | Per-unit vs total: for qty=1 they match; for qty>1 they differ | Use `charged_amount_excluding_tax` for revenue; `charged_amount` for per-unit price |
| `brand` NULL in sales/returns/settlement | All      | Some rows lack brand attribution | Join `target_tcin_mapping` on `tcin` for `LOWER(brand)` |
| Brand case mismatch | target_tcin_mapping | `Folkculture` (title case) vs `folkculture` (lowercase) | Normalize: `LOWER(brand)` in all joins and groupings |
| `description` in settlement = integer | target_settlement | Column type is integer; always NULL | Ignore this column; use `internal_txn_type` for classification |
| `barcode` in scientific notation | target_tcin_mapping | `8.90441E+12` instead of full UPC | Cast or reformat when used in product matching |
| Sales ↔ Settlement coverage 63% | sales + settlement | Dec 2025 sales gap + settlement timing lag | Add date filter to match periods |
| Returns ↔ Settlement coverage 37% | returns + settlement | Same recency gap; returns may settle in future payouts | Accept as timing difference |
| `reverse charge` vs customer return | target_settlement | `transaction_type='reverse charge'` is a tax adjustment, not a product return | Filter `transaction_type = 'reverse'` for return financial impact |


---

## 8. Mandatory Query Filters

```sql
-- All Target tables
WHERE is_active = true
  AND group_level_id = 123

-- Sales: active shipped orders only
WHERE is_active = true AND order_status = 'SHIPPED'

-- Settlement: forward sales only
WHERE is_active = true AND transaction_type = 'forward'

-- Returns: confirmed returns only
WHERE is_active = true AND internal_txn_type = 'reverse'
```


---

## 9. Table Summary Reference

| Table | Purpose | Active Rows | Date Range | Primary Key | Join Key | group_level_id |
|-------|---------|-------------|------------|-------------|----------|----------------|
| `target_sales` | Forward OMS | 7,291       | Apr–Dec 2025 | `item_id`   | `item_id`, `tcin`, `order_id` | 123            |
| `target_returns` | Returns tracking | 1,179       | May–Dec 2025 | `item_id`   | `order_id`, `tcin`, `item_id` | 123            |
| `target_settlement` | Payout ledger | 6,517       | Apr–Nov 2025 | `transfer_id` | `item_id`, `payout_id` | 123            |
| `target_tcin_mapping` | Product catalogue | 331         | —          | `tcin`      | `tcin`, `sku_id`, `asin` | 123            |
Tab 2
# Table: Target Settlement — Table Knowledge Base

**Schema:** `zs_observe`  **Table:** `target_settlement`  **Last Updated:** April 2025  **Maintained By:** ZenStatement Data Team


---

## 1. Table Overview

`target_settlement` is the **financial settlement and payout ledger** for the Target Plus marketplace. It records every financial event in the seller's Target account — sales proceeds, return refunds, reverse charges (chargebacks/taxes), commission deductions, shipping amounts, and the final settled amount per transaction.

Each row corresponds to one `transfer_id` — a Stripe-level fund transfer. Rows are grouped into **payout batches** (`payout_id`), each representing a bank deposit to the seller. The settlement currency is INR by label, but all values are in USD (consistent with the other Target tables).

**Key structural insight:** Unlike multi-row settlement models (e.g., JioMart's 3-row-per-order structure), Target settlement is **one row per order line per event** — the `settled_amount` is already the net payout after commission deduction.

**Payment processor:** Stripe — confirmed by `transfer_id` (`tr_...`), `payout_id` (`po_...`), and `payment_id` (`py_...`) formats.


---

## 2. Key Statistics

| Metric | Value |
|--------|-------|
| Total rows | 6,517 |
| Active rows (`is_active = true`) | 6,517 (100%) |
| group_level_id | 123   |
| Date range (`created_date`) | 2025-04-22 → 2025-11-27 |
| Returned date range | 2025-05-19 → 2025-11-30 |
| Distinct orders | 5,748 |
| Distinct SKUs | 268   |
| Distinct TCINs | 268   |
| Distinct transfer IDs | 6,517 (one per row) |
| Distinct payout batches | 31    |
| Total charged (gross GMV) | ₹1,52,999.33 (USD \~$153K) |
| Total taxable (excl. tax) | ₹1,29,679.26 |
| Total tax | ₹0.00 |
| Total shipping | ₹1,934.34 |
| Total gross commission | ₹19,456.55 |
| Total settled (net payout) | ₹1,10,436.43 |
| Avg commission rate | 15% (flat) |
| Commission as % of charged | \~12.7% effective |
| Currency field | INR (actual values are USD) |


---

## 3. Schema Details (37 Columns)

### 3.1 Identity Columns

| Column | Type | Description |
|--------|------|-------------|
| `unique_id` | varchar | Row identifier |
| `txn_uuid` | varchar | Pipeline UUID |
| `unique_value` | varchar | Dedup hash  |
| `transfer_id` | varchar | **Stripe transfer ID** (format: `tr_1SZX8wGxFTvW7WRNvTtE2N46`) — unique per row |
| `payout_id` | varchar | **Stripe payout ID** (format: `po_1SZh3kGgYJvT8MDtnFnpYLpX`) — groups rows into payment batches |
| `payment_id` | varchar | **Stripe payment charge ID** (format: `py_1SZX8wGgYJvT8MDtfSfVtQYV`) |
| `order_id` | varchar | Target order number — **join key to sales and returns** |
| `item_id` | varchar | Order line item ID — **join key to sales and returns** |
| `sku_id` | varchar | Seller SKU (Shopify format) |
| `tcin` | varchar | Target TCIN — **join key to tcin_mapping** |

### 3.2 Date Columns

| Column | Type | Description |
|--------|------|-------------|
| `created_date` | date | Settlement transaction date |
| `returned_date` | date | Return date (populated for reverse transactions) |

### 3.3 Financial Columns

| Column | Type | Description |
|--------|------|-------------|
| `charged_amount` | decimal | **Per-unit sale price** (USD) |
| `charged_amount_excluding_tax` | decimal | **Total order value net of tax** — for multi-qty orders: `charged_amount × quantity`; also used for refund totals |
| `total_tax` | decimal | Tax amount — **₹0.00 for all rows** (Target collects and remits sales tax on behalf of sellers) |
| `shipping_amount` | decimal | Shipping fee charged to buyer (if any) |
| `gross_commission` | decimal | **Commission charged by Target** (15% of `charged_amount_excluding_tax`) |
| `settled_amount` | decimal | **Net payout to seller** = `charged_amount_excluding_tax` + `shipping_amount` − `gross_commission` |
| `gross_commission_percentage` | decimal | Commission rate — **0.1500** (15%) for all forward/reverse rows; 0 for reverse charge rows |

### 3.4 Classification Columns

| Column | Type | Description |
|--------|------|-------------|
| `transaction_type` | varchar | `forward`, `reverse`, or `reverse charge` |
| `internal_txn_type` | varchar | `sales`, `refunds`, or `others` |
| `description` | integer | Description code (stored as integer — typically NULL) |
| `brand` | varchar | `folkculture`, `katchon`, or NULL |
| `quantity` | integer | Quantity settled |

### 3.5 System / Metadata Columns

| Column | Type | Description |
|--------|------|-------------|
| `group_level_id` | integer | `123`       |
| `currency_type` | varchar | `INR` (label; values are USD) |
| `is_active` | boolean | Always `true` |
| `zen_sheet_name` | varchar | Source sheet |
| `created_at` / `updated_at` | timestamp | Timestamps  |
| `deleted_at` | varchar | Soft delete |


---

## 4. Distinct Value Analysis

### `transaction_type` / `internal_txn_type` Full Breakdown

| Transaction Type | Internal Txn Type | Count | Gross Charged | Commission | Settled | Commission % |
|------------------|-------------------|-------|---------------|------------|---------|--------------|
| `forward`        | `sales`           | 5,659 | ₹1,32,081     | ₹21,069    | ₹1,21,342 | 15%          |
| `reverse`        | `refunds`         | 450   | ₹10,937       | −₹1,613    | −₹9,185 | 15% (reversed) |
| `reverse charge` | `others`          | 408   | ₹9,981        | ₹0         | −₹1,721 | 0%           |

### `reverse charge` — What Is It?

`reverse charge` rows with `internal_txn_type = 'others'` represent **marketplace facilitator tax remittances**. In the US, Target (as a marketplace facilitator) collects and remits sales tax on behalf of sellers. These `reverse charge` entries represent Target's tax obligations being offset against the seller's payout — the `charged_amount` shows the tax base but `settled_amount` is negative (deduction). No `gross_commission` is applied.

### `total_tax = 0.0` (Always)

Target acts as a **Marketplace Facilitator (MPF)** for US sales tax in all 50 states. This means Target collects and remits sales tax directly — the seller never sees gross tax amounts in their settlement; all tax handling is transparent. The `total_tax = 0` confirms this model.

### Payout Batch Structure

31 distinct `payout_id` values across 6,517 rows. Each payout batch spans multiple days of orders:

| Payout ID (sample) | Net Payout | Rows | Date Range |
|--------------------|------------|------|------------|
| `po_1SZh3kGgYJvT8MDtnFnpYLpX` | ₹\~27K (largest) | \~1,200 | Nov 2025   |
| `po_1S0AZzGgYJvT8MDtuRcRANLj` | ₹7,328.72  | 354  | May–Aug 2025 |
| `po_1RsYdyGgYJvT8MDtjcpLMCyB` | ₹4,262.30  | 266  | May–Jul 2025 |
| `po_1RLZ0yGgYJvT8MDt10K8Q4Ew` | ₹19.53     | 1    | Apr 2025 (first payout) |

### Commission Rate

**Flat 15% (**`**gross_commission_percentage = 0.1500**`**)** on `charged_amount_excluding_tax` for all `forward` and `reverse` rows. `reverse charge` rows have 0% commission (these are tax adjustments, not product transactions).

### Stripe ID Formats

| Field | Format | Example |
|-------|--------|---------|
| `transfer_id` | `tr_1{...}GxFTvW7WRN{...}` | `tr_1SZX8wGxFTvW7WRNvTtE2N46` |
| `payout_id` | `po_1{...}GgYJvT8MDt{...}` | `po_1SZh3kGgYJvT8MDtnFnpYLpX` |
| `payment_id` | `py_1{...}GgYJvT8MDt{...}` | `py_1SZX8wGgYJvT8MDtfSfVtQYV` |


---

## 5. Financial Waterfall (Forward Sales)

```
Charged Amount (per unit price, e.g. $29.99)   ₹1,32,081
× Quantity
= charged_amount_excluding_tax                 ₹1,40,429  ← includes multi-qty orders
+ Shipping Amount                               +₹1,983
                                              ──────────
  Gross Settlement Base                        ₹1,42,412
  − Gross Commission (15%)                    −₹21,069
                                              ──────────
  Net Settled (forward)                        ₹1,21,342  (85.2% payout ratio)

Return Refunds (reverse)                       −₹10,937
  + Commission Reversed                        +₹1,613
                                              ──────────
  Net Return Settlement                        −₹9,185

Reverse Charge (tax adjustments)              −₹1,721

Total Net Payout (all rows)                   ₹1,10,436
```


---

## 6. Sample Records

**Forward Sale:**

```
transfer_id              : tr_1SZX8wGxFTvW7WRNvTtE2N46
payout_id                : po_1SZh3kGgYJvT8MDtnFnpYLpX
payment_id               : py_1SZX8wGgYJvT8MDtfSfVtQYV
created_date             : 2025-11-27
transaction_type         : forward
internal_txn_type        : sales
order_id                 : 912003066801210
item_id                  : 912003066801210-8385623039
quantity                 : 2
charged_amount           : 15.9900   ← per-unit price
charged_amount_excl_tax  : 31.9800   ← 2 × 15.99
total_tax                : 0.0000    ← Target remits tax
shipping_amount          : 0.0000
gross_commission         : 4.8000    ← 15% × 31.98
settled_amount           : 27.1800   ← 31.98 − 4.80
tcin                     : 1007112387
gross_commission_pct     : 0.1500
brand                    : folkculture
group_level_id           : 123
```

**Return Refund:**

```
transaction_type         : reverse
internal_txn_type        : refunds
charged_amount           : 29.9900   ← original sale price
charged_amount_excl_tax  : -29.9900  ← negative = reversal
gross_commission         : -4.4985   ← commission reversed
settled_amount           : -25.4915  ← net refund to buyer
returned_date            : 2025-06-15
```


---

## 7. Data Quality Observations

| Issue | Detail | Mitigation |
|-------|--------|------------|
| `description` stored as integer | Always NULL in practice; no useful content | Ignore this column |
| `charged_amount` vs `charged_amount_excluding_tax` | For qty=1: identical. For qty>1: `charged_amount` = unit price, `charged_amount_excluding_tax` = total. Use `charged_amount_excluding_tax` for revenue calculations | Use `charged_amount_excluding_tax` as primary revenue field |
| `total_tax = 0` always | Target handles all US sales tax as marketplace facilitator | Expected; do not flag as data issue |
| `currency_type = INR` | All values are USD amounts | Treat as USD |
| Settlement ends Nov 2025 | Sales data extends to Dec 2025 — Dec sales not yet settled | Recency gap; Dec revenue visible in sales but not settlement |
| `reverse charge` is not product return | `transaction_type = 'reverse charge'` is tax-related, not a customer return | Filter `transaction_type != 'reverse charge'` for product-level analysis |
| Brand NULL for 224 rows | Join `target_tcin_mapping` on `tcin` for brand |            |


---

## 8. Common Query Patterns

### 8.1 Payout Batch Summary

```sql
SELECT
  payout_id,
  MIN(created_date) AS payout_start,
  MAX(created_date) AS payout_end,
  COUNT(*) AS line_items,
  SUM(CASE WHEN transaction_type = 'forward' THEN settled_amount ELSE 0 END) AS sales_settled,
  SUM(CASE WHEN transaction_type = 'reverse' THEN settled_amount ELSE 0 END) AS returns_settled,
  SUM(CASE WHEN transaction_type = 'reverse charge' THEN settled_amount ELSE 0 END) AS tax_adjustments,
  SUM(settled_amount) AS net_payout
FROM zs_observe.target_settlement
WHERE is_active = true
GROUP BY payout_id
ORDER BY payout_start;
```

### 8.2 Monthly Settlement Waterfall

```sql
SELECT
  DATE_TRUNC('month', created_date) AS month,
  SUM(CASE WHEN transaction_type='forward' THEN charged_amount_excluding_tax ELSE 0 END) AS gross_gmv,
  SUM(CASE WHEN transaction_type='forward' THEN gross_commission ELSE 0 END) AS commission,
  SUM(CASE WHEN transaction_type='forward' THEN shipping_amount ELSE 0 END) AS shipping,
  SUM(CASE WHEN transaction_type='forward' THEN settled_amount ELSE 0 END) AS forward_settled,
  SUM(CASE WHEN transaction_type='reverse' THEN settled_amount ELSE 0 END) AS returns_settled,
  SUM(CASE WHEN transaction_type='reverse charge' THEN settled_amount ELSE 0 END) AS tax_adj,
  SUM(settled_amount) AS net_payout
FROM zs_observe.target_settlement
WHERE is_active = true
GROUP BY 1 ORDER BY 1;
```

### 8.3 Commission Validation

```sql
SELECT
  brand,
  SUM(charged_amount_excluding_tax) AS taxable_base,
  SUM(gross_commission) AS commission_charged,
  AVG(gross_commission_percentage) AS avg_commission_rate,
  ROUND(100.0 * SUM(gross_commission)
    / NULLIF(SUM(charged_amount_excluding_tax), 0), 4) AS effective_commission_pct
FROM zs_observe.target_settlement
WHERE is_active = true AND transaction_type = 'forward'
GROUP BY brand;
```

### 8.4 Sales ↔ Settlement Reconciliation

```sql
SELECT
  s.order_id, s.item_id,
  s.charged_amount AS sales_unit_price,
  st.charged_amount_excluding_tax AS settlement_revenue,
  st.gross_commission,
  st.settled_amount,
  CASE WHEN st.item_id IS NULL THEN 'Not in Settlement' ELSE 'Matched' END AS status
FROM zs_observe.target_sales s
LEFT JOIN zs_observe.target_settlement st
  ON s.item_id = st.item_id AND st.is_active = true
WHERE s.is_active = true AND s.order_status = 'SHIPPED';
```

### 8.5 Effective Payout Rate

```sql
SELECT
  ROUND(100.0 * SUM(settled_amount)
    / NULLIF(SUM(charged_amount_excluding_tax), 0), 2) AS payout_rate_pct
FROM zs_observe.target_settlement
WHERE is_active = true AND transaction_type = 'forward';
-- Observed: ~85.2% payout ratio (after 15% commission)
```

**Schema:** `zs_observe`  **Table:** `target_settlement`  **Last Updated:** April 2025  **Maintained By:** ZenStatement Data Team


---

## 1. Table Overview

`target_settlement` is the **financial settlement and payout ledger** for the Target Plus marketplace. It records every financial event in the seller's Target account — sales proceeds, return refunds, reverse charges (chargebacks/taxes), commission deductions, shipping amounts, and the final settled amount per transaction.

Each row corresponds to one `transfer_id` — a Stripe-level fund transfer. Rows are grouped into **payout batches** (`payout_id`), each representing a bank deposit to the seller. The settlement currency is INR by label, but all values are in USD (consistent with the other Target tables).

**Key structural insight:** Unlike multi-row settlement models (e.g., JioMart's 3-row-per-order structure), Target settlement is **one row per order line per event** — the `settled_amount` is already the net payout after commission deduction.

**Payment processor:** Stripe — confirmed by `transfer_id` (`tr_...`), `payout_id` (`po_...`), and `payment_id` (`py_...`) formats.


---

## 2. Key Statistics

| Metric | Value |
|--------|-------|
| Total rows | 6,517 |
| Active rows (`is_active = true`) | 6,517 (100%) |
| group_level_id | 123   |
| Date range (`created_date`) | 2025-04-22 → 2025-11-27 |
| Returned date range | 2025-05-19 → 2025-11-30 |
| Distinct orders | 5,748 |
| Distinct SKUs | 268   |
| Distinct TCINs | 268   |
| Distinct transfer IDs | 6,517 (one per row) |
| Distinct payout batches | 31    |
| Total charged (gross GMV) | ₹1,52,999.33 (USD \~$153K) |
| Total taxable (excl. tax) | ₹1,29,679.26 |
| Total tax | ₹0.00 |
| Total shipping | ₹1,934.34 |
| Total gross commission | ₹19,456.55 |
| Total settled (net payout) | ₹1,10,436.43 |
| Avg commission rate | 15% (flat) |
| Commission as % of charged | \~12.7% effective |
| Currency field | INR (actual values are USD) |


---

## 3. Schema Details (37 Columns)

### 3.1 Identity Columns

| Column | Type | Description |
|--------|------|-------------|
| `unique_id` | varchar | Row identifier |
| `txn_uuid` | varchar | Pipeline UUID |
| `unique_value` | varchar | Dedup hash  |
| `transfer_id` | varchar | **Stripe transfer ID** (format: `tr_1SZX8wGxFTvW7WRNvTtE2N46`) — unique per row |
| `payout_id` | varchar | **Stripe payout ID** (format: `po_1SZh3kGgYJvT8MDtnFnpYLpX`) — groups rows into payment batches |
| `payment_id` | varchar | **Stripe payment charge ID** (format: `py_1SZX8wGgYJvT8MDtfSfVtQYV`) |
| `order_id` | varchar | Target order number — **join key to sales and returns** |
| `item_id` | varchar | Order line item ID — **join key to sales and returns** |
| `sku_id` | varchar | Seller SKU (Shopify format) |
| `tcin` | varchar | Target TCIN — **join key to tcin_mapping** |

### 3.2 Date Columns

| Column | Type | Description |
|--------|------|-------------|
| `created_date` | date | Settlement transaction date |
| `returned_date` | date | Return date (populated for reverse transactions) |

### 3.3 Financial Columns

| Column | Type | Description |
|--------|------|-------------|
| `charged_amount` | decimal | **Per-unit sale price** (USD) |
| `charged_amount_excluding_tax` | decimal | **Total order value net of tax** — for multi-qty orders: `charged_amount × quantity`; also used for refund totals |
| `total_tax` | decimal | Tax amount — **₹0.00 for all rows** (Target collects and remits sales tax on behalf of sellers) |
| `shipping_amount` | decimal | Shipping fee charged to buyer (if any) |
| `gross_commission` | decimal | **Commission charged by Target** (15% of `charged_amount_excluding_tax`) |
| `settled_amount` | decimal | **Net payout to seller** = `charged_amount_excluding_tax` + `shipping_amount` − `gross_commission` |
| `gross_commission_percentage` | decimal | Commission rate — **0.1500** (15%) for all forward/reverse rows; 0 for reverse charge rows |

### 3.4 Classification Columns

| Column | Type | Description |
|--------|------|-------------|
| `transaction_type` | varchar | `forward`, `reverse`, or `reverse charge` |
| `internal_txn_type` | varchar | `sales`, `refunds`, or `others` |
| `description` | integer | Description code (stored as integer — typically NULL) |
| `brand` | varchar | `folkculture`, `katchon`, or NULL |
| `quantity` | integer | Quantity settled |

### 3.5 System / Metadata Columns

| Column | Type | Description |
|--------|------|-------------|
| `group_level_id` | integer | `123`       |
| `currency_type` | varchar | `INR` (label; values are USD) |
| `is_active` | boolean | Always `true` |
| `zen_sheet_name` | varchar | Source sheet |
| `created_at` / `updated_at` | timestamp | Timestamps  |
| `deleted_at` | varchar | Soft delete |


---

## 4. Distinct Value Analysis

### `transaction_type` / `internal_txn_type` Full Breakdown

| Transaction Type | Internal Txn Type | Count | Gross Charged | Commission | Settled | Commission % |
|------------------|-------------------|-------|---------------|------------|---------|--------------|
| `forward`        | `sales`           | 5,659 | ₹1,32,081     | ₹21,069    | ₹1,21,342 | 15%          |
| `reverse`        | `refunds`         | 450   | ₹10,937       | −₹1,613    | −₹9,185 | 15% (reversed) |
| `reverse charge` | `others`          | 408   | ₹9,981        | ₹0         | −₹1,721 | 0%           |

### `reverse charge` — What Is It?

`reverse charge` rows with `internal_txn_type = 'others'` represent **marketplace facilitator tax remittances**. In the US, Target (as a marketplace facilitator) collects and remits sales tax on behalf of sellers. These `reverse charge` entries represent Target's tax obligations being offset against the seller's payout — the `charged_amount` shows the tax base but `settled_amount` is negative (deduction). No `gross_commission` is applied.

### `total_tax = 0.0` (Always)

Target acts as a **Marketplace Facilitator (MPF)** for US sales tax in all 50 states. This means Target collects and remits sales tax directly — the seller never sees gross tax amounts in their settlement; all tax handling is transparent. The `total_tax = 0` confirms this model.

### Payout Batch Structure

31 distinct `payout_id` values across 6,517 rows. Each payout batch spans multiple days of orders:

| Payout ID (sample) | Net Payout | Rows | Date Range |
|--------------------|------------|------|------------|
| `po_1SZh3kGgYJvT8MDtnFnpYLpX` | ₹\~27K (largest) | \~1,200 | Nov 2025   |
| `po_1S0AZzGgYJvT8MDtuRcRANLj` | ₹7,328.72  | 354  | May–Aug 2025 |
| `po_1RsYdyGgYJvT8MDtjcpLMCyB` | ₹4,262.30  | 266  | May–Jul 2025 |
| `po_1RLZ0yGgYJvT8MDt10K8Q4Ew` | ₹19.53     | 1    | Apr 2025 (first payout) |

### Commission Rate

**Flat 15% (**`**gross_commission_percentage = 0.1500**`**)** on `charged_amount_excluding_tax` for all `forward` and `reverse` rows. `reverse charge` rows have 0% commission (these are tax adjustments, not product transactions).

### Stripe ID Formats

| Field | Format | Example |
|-------|--------|---------|
| `transfer_id` | `tr_1{...}GxFTvW7WRN{...}` | `tr_1SZX8wGxFTvW7WRNvTtE2N46` |
| `payout_id` | `po_1{...}GgYJvT8MDt{...}` | `po_1SZh3kGgYJvT8MDtnFnpYLpX` |
| `payment_id` | `py_1{...}GgYJvT8MDt{...}` | `py_1SZX8wGgYJvT8MDtfSfVtQYV` |


---

## 5. Financial Waterfall (Forward Sales)

```
Charged Amount (per unit price, e.g. $29.99)   ₹1,32,081
× Quantity
= charged_amount_excluding_tax                 ₹1,40,429  ← includes multi-qty orders
+ Shipping Amount                               +₹1,983
                                              ──────────
  Gross Settlement Base                        ₹1,42,412
  − Gross Commission (15%)                    −₹21,069
                                              ──────────
  Net Settled (forward)                        ₹1,21,342  (85.2% payout ratio)

Return Refunds (reverse)                       −₹10,937
  + Commission Reversed                        +₹1,613
                                              ──────────
  Net Return Settlement                        −₹9,185

Reverse Charge (tax adjustments)              −₹1,721

Total Net Payout (all rows)                   ₹1,10,436
```


---

## 6. Sample Records

**Forward Sale:**

```
transfer_id              : tr_1SZX8wGxFTvW7WRNvTtE2N46
payout_id                : po_1SZh3kGgYJvT8MDtnFnpYLpX
payment_id               : py_1SZX8wGgYJvT8MDtfSfVtQYV
created_date             : 2025-11-27
transaction_type         : forward
internal_txn_type        : sales
order_id                 : 912003066801210
item_id                  : 912003066801210-8385623039
quantity                 : 2
charged_amount           : 15.9900   ← per-unit price
charged_amount_excl_tax  : 31.9800   ← 2 × 15.99
total_tax                : 0.0000    ← Target remits tax
shipping_amount          : 0.0000
gross_commission         : 4.8000    ← 15% × 31.98
settled_amount           : 27.1800   ← 31.98 − 4.80
tcin                     : 1007112387
gross_commission_pct     : 0.1500
brand                    : folkculture
group_level_id           : 123
```

**Return Refund:**

```
transaction_type         : reverse
internal_txn_type        : refunds
charged_amount           : 29.9900   ← original sale price
charged_amount_excl_tax  : -29.9900  ← negative = reversal
gross_commission         : -4.4985   ← commission reversed
settled_amount           : -25.4915  ← net refund to buyer
returned_date            : 2025-06-15
```


---

## 7. Data Quality Observations

| Issue | Detail | Mitigation |
|-------|--------|------------|
| `description` stored as integer | Always NULL in practice; no useful content | Ignore this column |
| `charged_amount` vs `charged_amount_excluding_tax` | For qty=1: identical. For qty>1: `charged_amount` = unit price, `charged_amount_excluding_tax` = total. Use `charged_amount_excluding_tax` for revenue calculations | Use `charged_amount_excluding_tax` as primary revenue field |
| `total_tax = 0` always | Target handles all US sales tax as marketplace facilitator | Expected; do not flag as data issue |
| `currency_type = INR` | All values are USD amounts | Treat as USD |
| Settlement ends Nov 2025 | Sales data extends to Dec 2025 — Dec sales not yet settled | Recency gap; Dec revenue visible in sales but not settlement |
| `reverse charge` is not product return | `transaction_type = 'reverse charge'` is tax-related, not a customer return | Filter `transaction_type != 'reverse charge'` for product-level analysis |
| Brand NULL for 224 rows | Join `target_tcin_mapping` on `tcin` for brand |            |


---

## 8. Common Query Patterns

### 8.1 Payout Batch Summary

```sql
SELECT
  payout_id,
  MIN(created_date) AS payout_start,
  MAX(created_date) AS payout_end,
  COUNT(*) AS line_items,
  SUM(CASE WHEN transaction_type = 'forward' THEN settled_amount ELSE 0 END) AS sales_settled,
  SUM(CASE WHEN transaction_type = 'reverse' THEN settled_amount ELSE 0 END) AS returns_settled,
  SUM(CASE WHEN transaction_type = 'reverse charge' THEN settled_amount ELSE 0 END) AS tax_adjustments,
  SUM(settled_amount) AS net_payout
FROM zs_observe.target_settlement
WHERE is_active = true
GROUP BY payout_id
ORDER BY payout_start;
```

### 8.2 Monthly Settlement Waterfall

```sql
SELECT
  DATE_TRUNC('month', created_date) AS month,
  SUM(CASE WHEN transaction_type='forward' THEN charged_amount_excluding_tax ELSE 0 END) AS gross_gmv,
  SUM(CASE WHEN transaction_type='forward' THEN gross_commission ELSE 0 END) AS commission,
  SUM(CASE WHEN transaction_type='forward' THEN shipping_amount ELSE 0 END) AS shipping,
  SUM(CASE WHEN transaction_type='forward' THEN settled_amount ELSE 0 END) AS forward_settled,
  SUM(CASE WHEN transaction_type='reverse' THEN settled_amount ELSE 0 END) AS returns_settled,
  SUM(CASE WHEN transaction_type='reverse charge' THEN settled_amount ELSE 0 END) AS tax_adj,
  SUM(settled_amount) AS net_payout
FROM zs_observe.target_settlement
WHERE is_active = true
GROUP BY 1 ORDER BY 1;
```

### 8.3 Commission Validation

```sql
SELECT
  brand,
  SUM(charged_amount_excluding_tax) AS taxable_base,
  SUM(gross_commission) AS commission_charged,
  AVG(gross_commission_percentage) AS avg_commission_rate,
  ROUND(100.0 * SUM(gross_commission)
    / NULLIF(SUM(charged_amount_excluding_tax), 0), 4) AS effective_commission_pct
FROM zs_observe.target_settlement
WHERE is_active = true AND transaction_type = 'forward'
GROUP BY brand;
```

### 8.4 Sales ↔ Settlement Reconciliation

```sql
SELECT
  s.order_id, s.item_id,
  s.charged_amount AS sales_unit_price,
  st.charged_amount_excluding_tax AS settlement_revenue,
  st.gross_commission,
  st.settled_amount,
  CASE WHEN st.item_id IS NULL THEN 'Not in Settlement' ELSE 'Matched' END AS status
FROM zs_observe.target_sales s
LEFT JOIN zs_observe.target_settlement st
  ON s.item_id = st.item_id AND st.is_active = true
WHERE s.is_active = true AND s.order_status = 'SHIPPED';
```

### 8.5 Effective Payout Rate

```sql
SELECT
  ROUND(100.0 * SUM(settled_amount)
    / NULLIF(SUM(charged_amount_excluding_tax), 0), 2) AS payout_rate_pct
FROM zs_observe.target_settlement
WHERE is_active = true AND transaction_type = 'forward';
-- Observed: ~85.2% payout ratio (after 15% commission)
```
Tab 3
# Table: Target TCIN Mapping — Table Knowledge Base

**Schema:** `zs_observe`  **Table:** `target_tcin_mapping`  **Last Updated:** April 2025  **Maintained By:** ZenStatement Data Team


---

## 1. Table Overview

`target_tcin_mapping` Is the **product catalogue cross-reference table** for Target Plus? It maps the seller's internal SKU codes to Target's product identifiers (TCIN), as well as Amazon's product identifier (ASIN) and product barcodes (UPC/EAN). This is the master product dimension table for the Target pipeline.

**TCIN (Target Catalogue Item Number)** is Target's proprietary product ID system — every unique product on [Target.com](http://Target.com) has a TCIN. It is the primary join key across all Target tables. Since the seller's internal SKUs have Shopify prefixes (`#shop-...`) in the OMS tables, `target_tcin_mapping` provides the clean seller SKU format (`1907AAA`, `KA-1-NB-BK-SNGL`) alongside the TCIN mapping.

The `asin` field reveals that both Folkculture and Katchon are also active Amazon sellers — their products are cross-listed with matching ASINs, confirming a multi-channel selling strategy.


---

## 2. Key Statistics

| Metric | Value |
|--------|-------|
| Total rows | 331   |
| Active rows (`is_active = true`) | 331 (100%) |
| group_level_id | 123   |
| Distinct SKUs | 331   |
| Distinct TCINs | 331   |
| Distinct barcodes | 69 (many SKUs share barcodes) |
| All rows have ASIN | 331 (100%) |
| Brands | `Folkculture` (187 SKUs), `Katchon` (144 SKUs) |
| Currency | INR   |


---

## 3. Schema Details (21 Columns)

| Column | Type | Description |
|--------|------|-------------|
| `unique_id` | varchar | Row identifier |
| `txn_uuid` | varchar | Pipeline UUID |
| `unique_value` | varchar | Dedup hash  |
| `sku_id` | varchar | **Seller's clean SKU code** (e.g., `1907AAA`, `KA-1-NB-BK-SNGL`) |
| `tcin` | varchar | **Target Catalogue Item Number** (e.g., `1002553169`) — primary join key |
| `barcode` | varchar | UPC/EAN barcode (69 distinct values — multiple SKUs share barcodes) |
| `brand` | varchar | Brand name (`Folkculture`, `Katchon`) — note title case differs from sales table |
| `asin` | varchar | Amazon Standard Identification Number — confirms cross-channel listing |
| `currency_type` | varchar | `INR`       |
| `group_level_id` | integer | `123`       |
| `group_id` | integer | Internal reference |
| `file_uuid` | varchar | Source file UUID |
| `is_active` | boolean | Always `true` |
| `is_duplicated` | boolean | Dedup flag  |
| `zen_status` | boolean | Pipeline flag |
| `zen_sheet_name` | varchar | Source sheet |
| `created_at` / `updated_at` | timestamp | Timestamps  |
| `deleted_at` | varchar | Soft delete |


---

## 4. Distinct Value Analysis

### Brand Distribution

| Brand | SKU Count | Notes |
|-------|-----------|-------|
| `Folkculture` | 187       | Party supplies, craft kits, seasonal décor |
| `Katchon` | 144       | Craft and party accessories, smaller items |

> Note: `brand` in this table is `Folkculture` (title case) vs `folkculture` (lowercase) in sales/returns/settlement. Always use case-insensitive comparison or `LOWER(brand)`.

### SKU Naming Conventions

| Format | Brand | Example |
|--------|-------|---------|
| `YYYYXXX` (year + variant) | Folkculture | `1907AAA`, `2010III` |
| `KA-{size}-{type}-{color}-{qty}` | Katchon | `KA-1-NB-BK-SNGL`, `KA-18-NB-HP-DOBL` |

### Barcode Coverage

* 331 SKUs but only 69 distinct barcodes
* Multiple SKU variants share the same UPC/EAN barcode (e.g., different sizes/colors of the same base product)
* Barcode stored as scientific notation in some rows (e.g., `8.90441E+12` = `8904412XXXXXX`) — data formatting issue from CSV export

### ASIN Cross-Reference

All 331 TCINs have corresponding Amazon ASINs, confirming the seller maintains the same catalogue on both Target Plus and Amazon. The ASIN can be used to cross-reference pricing, reviews, and rankings on Amazon against Target performance.


---

## 5. Sample Records

```
sku_id    : 1907AAA
barcode   : 8904412XXXXXXX (Folkculture UPC)
tcin      : 1002553169
brand     : Folkculture
asin      : B07VMYDZDG
group_level_id: 123

sku_id    : KA-1-NB-BK-SNGL
barcode   : (Katchon UPC)
tcin      : (Katchon TCIN)
brand     : Katchon
asin      : (Amazon ASIN)
group_level_id: 123
```


---

## 6. Data Quality Observations

| Issue | Detail | Mitigation |
|-------|--------|------------|
| Barcode scientific notation | Some barcodes stored as `8.90441E+12` instead of `8904412XXXXXX` | `CAST(barcode AS DECIMAL)` or treat as string after removing scientific format |
| Brand case mismatch | `Folkculture` here vs `folkculture` in other tables | Use `LOWER(brand)` in joins |
| 331 TCINs vs 322 in sales | 9 TCINs in mapping not seen in sales data (may be unlisted or out-of-stock SKUs) | TCIN mapping is the full catalogue; sales are actual orders |
| `description` / product name absent | No product title stored in mapping | Use [Target.com](http://Target.com) TCIN URL: `https://www.target.com/p/-/A-{tcin}` |
| Shared barcodes | Multiple product variants share one UPC | Cannot use barcode alone as primary key — use `tcin` |


---

## 7. Common Query Patterns

### 7.1 Full Catalogue with Sales Coverage

```sql
SELECT
  m.tcin, m.sku_id, m.brand, m.asin, m.barcode,
  COUNT(s.order_id) AS total_sold,
  SUM(s.charged_amount) AS revenue
FROM zs_observe.target_tcin_mapping m
LEFT JOIN zs_observe.target_sales s
  ON m.tcin = s.tcin AND s.is_active = true AND s.order_status = 'SHIPPED'
WHERE m.is_active = true
GROUP BY m.tcin, m.sku_id, m.brand, m.asin, m.barcode
ORDER BY total_sold DESC;
```

### 7.2 Brand-Level SKU Count

```sql
SELECT
  LOWER(brand) AS brand,
  COUNT(*) AS total_skus,
  COUNT_IF(barcode IS NOT NULL) AS skus_with_barcode,
  COUNT_IF(asin IS NOT NULL) AS skus_on_amazon
FROM zs_observe.target_tcin_mapping
WHERE is_active = true
GROUP BY LOWER(brand);
```

### 7.3 Enrich Sales with Mapping Data

```sql
SELECT
  s.order_id, s.created_date, s.order_status,
  s.charged_amount, s.discount_amount,
  m.sku_id AS clean_sku, m.brand, m.asin, m.barcode
FROM zs_observe.target_sales s
JOIN zs_observe.target_tcin_mapping m
  ON s.tcin = m.tcin AND m.is_active = true
WHERE s.is_active = true
  AND s.order_status = 'SHIPPED';
```
Tab 4
# Table: Target Returns — Table Knowledge Base

**Schema:** `zs_observe`  **Table:** `target_returns`  **Last Updated:** April 2025  **Maintained By:** ZenStatement Data Team


---

## 1. Table Overview

`target_returns` captures every **return transaction** on the Target Plus marketplace — buyer-initiated returns, refund events, and reverse transactions. A key feature of Target Plus is that **Target handles the return logistics on the seller's behalf**: buyers can return items to any Target store or via mail, and Target manages the reverse shipping. The seller is responsible for accepting returned inventory, but does not need to arrange return pickup or courier coordination.

The table records each returned item's original order, return reason, returned date, and the amount refunded. It contains two `internal_txn_type` values — `reverse` (standard return reversal) and `refunds` (processed refund events) — reflecting the two-stage return processing on the platform.


---

## 2. Key Statistics

| Metric | Value |
|--------|-------|
| Total rows | 1,247 |
| Active rows (`is_active = true`) | 1,179 |
| group_level_id | 123   |
| Date range (`created_date`) | 2025-05-05 → 2025-12-31 |
| Date range (`returned_date`) | 2025-05-15 → 2026-02-16 |
| Distinct orders | 1,050 |
| Distinct SKUs | 240   |
| Distinct TCINs | 240   |
| Total charged (returned value) | ₹23,952.51 |
| Avg charged amount | ₹20.32 |
| Brands | `folkculture`, `katchon` |
| Transaction type | `reverse` (100%) |
| Internal txn types | `reverse`, `refunds` |
| Currency | INR (field label; actual USD values) |


---

## 3. Schema Details (30 Columns)

### 3.1 Identity Columns

| Column | Type | Description |
|--------|------|-------------|
| `unique_id` | varchar | Row identifier |
| `txn_uuid` | varchar | Pipeline UUID |
| `unique_value` | varchar | Dedup hash  |
| `order_id` | varchar | Original Target order number |
| `item_id` | varchar | Order line item ID — **join key to sales and settlement** |
| `other_id` | varchar | Carrier tracking number (format varies: `1ZE3656H0317269433` = UPS) |
| `sku_id` | varchar | Seller SKU (Shopify format: `#shop-XXXXXXXXX`) |
| `tcin` | varchar | Target product identifier — **join key to tcin_mapping** |

### 3.2 Date Columns

| Column | Type | Description |
|--------|------|-------------|
| `created_date` | date | Date return was created/registered in the system |
| `returned_date` | date | Date the item was physically returned / refund was processed |

### 3.3 Financial Columns

| Column | Type | Description |
|--------|------|-------------|
| `charged_amount` | decimal | Original sale price / refund amount |
| `quantity` | integer | Quantity returned |

### 3.4 Classification Columns

| Column | Type | Description |
|--------|------|-------------|
| `transaction_type` | varchar | `reverse` — 100% |
| `internal_txn_type` | varchar | `reverse` (return event) or `refunds` (refund processing event) |
| `order_status` | varchar | `DELIVERED`, `IN_TRANSIT`, `OUT_FOR_DELIVERY`, `RETURNED`, or NULL |
| `description` | varchar | **Return reason** — valuable qualitative field (see values below) |
| `brand` | varchar | `folkculture`, `katchon`, or NULL |

### 3.5 System / Metadata Columns

| Column | Type | Description |
|--------|------|-------------|
| `group_level_id` | integer | `123`       |
| `currency_type` | varchar | `INR` (label only; values are USD) |
| `is_active` | boolean | Filter `is_active = true` |
| `zen_sheet_name` | varchar | Source sheet |
| `created_at` / `updated_at` | timestamp | Timestamps  |
| `deleted_at` | varchar | Soft delete |


---

## 4. Distinct Value Analysis

### `internal_txn_type` Distribution

| Internal Txn Type | Count | Total Charged | Meaning |
|-------------------|-------|---------------|---------|
| `reverse`         | 1,039 | ₹22,424.61    | Return event — item being sent back to seller |
| `refunds`         | 140   | ₹1,527.90     | Refund event — financial refund issued to buyer |

### `order_status` (when populated)

| Status | Count | Meaning |
|--------|-------|---------|
| NULL   | \~1,100 | Return processed, status not captured |
| `DELIVERED` | 19    | Return for an item marked as delivered |
| `IN_TRANSIT` | \~few | Return initiated while in transit |
| `OUT_FOR_DELIVERY` | \~few | Return for item about to be delivered |
| `RETURNED` | \~few | Confirms return loop complete |

### Return Reasons (`description` field) — Top 17 Values

| Return Reason | Count | Total Refunded | Avg Refund |
|---------------|-------|----------------|------------|
| Changed Mind  | 765   | ₹15,428        | ₹20.17     |
| Doesnt Fit    | 132   | ₹2,694         | ₹20.41     |
| Poor Quality  | 75    | ₹1,496         | ₹19.94     |
| Arrived Late  | 44    | ₹719           | ₹16.34     |
| Missing Package | 28    | ₹568           | ₹20.29     |
| Sent Wrong Item | \~17  | —              | —          |
| Missing Item or Shipment | \~12  | —              | —          |
| Defective     | \~few | —              | —          |
| Damaged During Shipping | \~few | —              | —          |
| Not as Described | \~few | —              | —          |
| Duplicate Order | \~few | —              | —          |

> **"Changed Mind" accounts for \~65% of all returns** — this is typical for party supplies where impulse purchases are common and items are sometimes ordered in excess.

### `other_id` — Carrier Tracking Numbers

When populated, `other_id` contains the return shipment tracking number:

* `1ZE3656H0317269433` — UPS format (`1Z...`)
* `1Z19R3A49025382586` — UPS format

This is populated for `internal_txn_type = 'reverse'` cases where a physical return shipment occurs.


---

## 5. Sample Records

```
brand              : folkculture
created_date       : 2025-12-31
transaction_type   : reverse
internal_txn_type  : reverse
order_id           : 24410010530101983
item_id            : 912003183800968-8476824854
order_status       : NULL
quantity           : 1
charged_amount     : 29.9900
description        : Changed Mind
sku_id             : #shop-45805085229314
tcin               : 1002584245
returned_date      : 2026-01-24
other_id           : NULL
group_level_id     : 123

brand              : folkculture
description        : Sent Wrong Item
order_status       : DELIVERED
other_id           : 1Z19R3A49025382586   ← UPS tracking
returned_date      : 2026-01-05
```


---

## 6. Data Quality Observations

| Issue | Detail | Mitigation |
|-------|--------|------------|
| 68 inactive rows | Apply `is_active = true` always |            |
| `order_status` NULL for \~93% | Most return rows have no order status | Use `returned_date` for timing; `description` for reason analysis |
| `other_id` NULL for many rows | Tracking not always captured — Target handles logistics so seller may not receive tracking detail | Informational only; use for return cycle time only when populated |
| Duplicate rows for same return | `internal_txn_type = 'reverse'` (event) and `'refunds'` (financial) can both appear for the same order | De-duplicate on `order_id` + `tcin` when counting distinct returns |
| `returned_date` extends to 2026 | Returns created in Dec 2025 may complete physically in Jan–Feb 2026 | Expected lag — filter by `returned_date` for financial period assignment |
| `currency_type = INR` | Same as sales — values are USD prices | Treat as USD |


---

## 7. Common Query Patterns

### 7.1 Return Volume and Value by Reason

```sql
SELECT
  description AS return_reason,
  COUNT(*) AS returns,
  SUM(charged_amount) AS total_refunded,
  AVG(charged_amount) AS avg_refund,
  ROUND(100.0 * COUNT(*) / SUM(COUNT(*)) OVER (), 2) AS pct_of_returns
FROM zs_observe.target_returns
WHERE is_active = true
  AND internal_txn_type = 'reverse'
  AND description IS NOT NULL
GROUP BY description
ORDER BY returns DESC;
```

### 7.2 Return Rate by Brand

```sql
SELECT
  brand,
  COUNT(DISTINCT order_id) AS returned_orders,
  SUM(charged_amount) AS total_refunded
FROM zs_observe.target_returns
WHERE is_active = true
GROUP BY brand
ORDER BY returned_orders DESC;
```

### 7.3 Monthly Return Trend

```sql
SELECT
  DATE_TRUNC('month', created_date) AS month,
  COUNT(*) AS returns,
  SUM(charged_amount) AS refund_value
FROM zs_observe.target_returns
WHERE is_active = true AND internal_txn_type = 'reverse'
GROUP BY 1 ORDER BY 1;
```

### 7.4 Returns ↔ Sales Reconciliation

```sql
SELECT
  r.order_id,
  r.tcin,
  r.description AS return_reason,
  r.charged_amount AS refund_amount,
  r.returned_date,
  s.charged_amount AS original_sale_price,
  s.created_date AS sale_date
FROM zs_observe.target_returns r
LEFT JOIN zs_observe.target_sales s
  ON r.order_id = s.order_id
  AND r.tcin = s.tcin
  AND s.is_active = true
WHERE r.is_active = true
  AND r.internal_txn_type = 'reverse';
```

### 7.5 SKU-Level Return Rate

```sql
SELECT
  r.tcin,
  m.brand,
  COUNT(DISTINCT r.order_id) AS returns,
  COUNT(DISTINCT s.order_id) AS sales,
  ROUND(100.0 * COUNT(DISTINCT r.order_id)
    / NULLIF(COUNT(DISTINCT s.order_id), 0), 2) AS return_rate_pct
FROM zs_observe.target_returns r
LEFT JOIN zs_observe.target_sales s
  ON r.tcin = s.tcin AND s.is_active = true AND s.order_status = 'SHIPPED'
LEFT JOIN zs_observe.target_tcin_mapping m
  ON r.tcin = m.tcin AND m.is_active = true
WHERE r.is_active = true AND r.internal_txn_type = 'reverse'
GROUP BY r.tcin, m.brand
HAVING COUNT(DISTINCT s.order_id) > 5
ORDER BY return_rate_pct DESC;
```


---
Tab 5
# Table: Target Sales — Table Knowledge Base

**Schema:** `zs_observe`  **Table:** `target_sales`  **Last Updated:** April 2025  **Maintained By:** ZenStatement Data Team


---

## 1. Table Overview

`target_sales` is the **forward-order OMS table** for the Target Plus marketplace. It records every item sold on [Target.com](http://Target.com) by the seller — capturing the order ID, SKU, TCIN (Target's product identifier), charged amount, discount applied, and order status. It is the primary source for GMV measurement, sales velocity analysis, and joining to settlement and returns.

**Marketplace:** Target Plus (Target+) — invite-only US marketplace\n**Seller entity:** Mensa brand group (group_level_id = 123)\n**Brands:** folkculture and katchon — party supplies, craft kits, décor accessories\n**Important:** All transactions are in **INR** currency field, but product prices reflect USD values ($9.99–$34.99 range). The `charged_amount` field contains per-unit USD price.


---

## 2. Key Statistics

| Metric | Value |
|--------|-------|
| Total rows | 9,063 |
| Active rows (`is_active = true`) | 7,291 |
| group_level_id | 123   |
| Date range (`created_date`) | 2025-04-22 → 2025-12-31 |
| Distinct orders | 8,538 |
| Distinct SKUs (`sku_id`) | 322   |
| Distinct TCINs | 322   |
| Brands | `folkculture`, `katchon`, NULL |
| Total GMV (`charged_amount`) | ₹1,70,387.59 (≈ USD 170K at ₹1/unit pricing) |
| Total discount | −₹2,837.81 |
| Avg charged amount | ₹23.37 (≈ $23.37 USD per unit) |
| Transaction type | `forward` (100%) |
| Internal txn type | `sales` (100%) |
| Currency field | INR   |


---

## 3. Schema Details (29 Columns)

### 3.1 Identity Columns

| Column | Type | Description |
|--------|------|-------------|
| `unique_id` | varchar | System row identifier |
| `txn_uuid` | varchar | Pipeline UUID |
| `unique_value` | varchar | Deduplication hash |
| `order_id` | varchar | Target order number (format: `912003184143022`) |
| `item_id` | varchar | Order line item ID (format: `order_id-lineitem_no`, e.g., `912003184143022-8483691919`) — **join key to settlement** |
| `other_id` | varchar | Internal store reference code (e.g., `ZVBH`) |
| `sku_id` | varchar | Seller SKU (Shopify format: `#shop-44218603077890`) |
| `tcin` | varchar | **Target Catalogue Item Number** — Target's product identifier (e.g., `1002637927`) — **join key to tcin_mapping** |

### 3.2 Date Columns

| Column | Type | Description |
|--------|------|-------------|
| `created_date` | date | Order creation date |

### 3.3 Financial Columns

| Column | Type | Description |
|--------|------|-------------|
| `charged_amount` | decimal | **Per-unit price charged to buyer** (USD amount, e.g., 29.99) |
| `discount_amount` | decimal | Discount applied (negative value = reduction off charged_amount) |
| `quantity` | integer | Units ordered (almost always 1) |

### 3.4 Classification Columns

| Column | Type | Description |
|--------|------|-------------|
| `transaction_type` | varchar | `forward` — 100% |
| `internal_txn_type` | varchar | `sales` — 100% |
| `order_status` | varchar | `SHIPPED` or `CANCELED` |
| `brand` | varchar | `folkculture`, `katchon`, or NULL |
| `description` | varchar | Product description |

### 3.5 System / Metadata Columns

| Column | Type | Description |
|--------|------|-------------|
| `group_level_id` | integer | `123` — Target seller account |
| `group_id` | integer | Internal group reference |
| `file_uuid` | varchar | Source file UUID |
| `currency_type` | varchar | `INR` (field label only — actual values are USD prices) |
| `is_active` | boolean | Filter `is_active = true` |
| `is_duplicated` | boolean | Dedup flag  |
| `zen_status` | boolean | Pipeline status flag |
| `zen_sheet_name` | varchar | Source sheet name |
| `created_at` / `updated_at` | timestamp | Timestamps  |
| `deleted_at` | varchar | Soft delete timestamp |


---

## 4. Distinct Value Analysis

### `order_status` Distribution

| Status | Count | GMV | Meaning |
|--------|-------|-----|---------|
| `SHIPPED` | 7,269 | ₹1,69,909.31 | Order fulfilled and dispatched to buyer |
| `CANCELED` | 22    | ₹478.28 | Order cancelled before/after shipment |

### `brand` Distribution

| Brand | Count | Distinct SKUs | Orders | GMV | Avg Price |
|-------|-------|---------------|--------|-----|-----------|
| `folkculture` | 5,658 | 170           | 5,363  | ₹1,44,628 | ₹25.56    |
| `katchon` | 1,177 | 119           | 1,109  | ₹15,290 | ₹12.99    |
| NULL  | 456   | 35            | 442    | ₹10,469 | ₹22.96    |

### Order ID Format

`912003184143022` — 15-digit Target order number. The prefix digit indicates order origin:

* `9` prefix — Standard [Target.com](http://Target.com) order
* `1` prefix — Some orders observed with `1` prefix (different fulfilment channel)
* `2` prefix — Also observed

### Item ID Format

`{order_id}-{lineitem_number}` — e.g., `912003184143022-8483691919`

### SKU ID Format

`#shop-{shopify_variant_id}` — e.g., `#shop-44218603077890`\nThese are Shopify variant IDs assigned by the seller's Shopify store, mapped to TCINs via `target_tcin_mapping`.

### TCIN Format

`10XXXXXXXX` — 10-digit Target product ID (e.g., `1002637927`). Unique per product variant on [Target.com](http://Target.com).

### `other_id`

`ZVBH` — observed for all folkculture orders. This appears to be an internal store/warehouse location code.


---

## 5. Sample Records

```
currency_type  : INR
brand          : folkculture
created_date   : 2025-12-31
transaction_type: forward
internal_txn_type: sales
order_id       : 902003184143022
item_id        : 902003184143022-8483691919
order_status   : SHIPPED
quantity       : 1
sku_id         : #shop-44218603077890
charged_amount : 29.9900   ← USD price
other_id       : ZVBH
tcin           : 1002637927
discount_amount: 0.0000
group_level_id : 123

brand          : katchon
order_id       : 912003039684748
sku_id         : #shop-XXXXXXX
charged_amount : 9.9900   ← Katchon avg ~$12.99
discount_amount: 0.0000
```


---

## 6. Data Quality Observations

| Issue | Detail | Mitigation |
|-------|--------|------------|
| `currency_type = INR` but values are USD | Field label is INR; actual `charged_amount` values are in USD (e.g., 29.99) | Treat as USD amounts; do not convert |
| 1,772 inactive rows (9,063 − 7,291) | Superseded/duplicate records | Always `WHERE is_active = true` |
| `brand` NULL for 456 rows | Some orders lack brand attribution | Join `target_tcin_mapping` on `tcin` to derive brand |
| `description` not present in sales table | No product description column | Join `target_tcin_mapping` for product details |
| `quantity` always 1 in observed data | Target Plus orders are predominantly single-unit | `charged_amount` = total for these rows; confirm via settlement `charged_amount_excluding_tax` |
| `other_id = ZVBH` for all folkculture | Internal code, not a meaningful ID for joins | Informational only |
| Settlement coverage 63% | Only 5,363 of 8,538 distinct orders appear in settlement | Settlement data runs Apr–Nov 2025; sales run Apr–Dec 2025 — recency gap |


---

## 7. Common Query Patterns

### 7.1 Monthly Sales GMV by Brand

```sql
SELECT
  DATE_TRUNC('month', created_date) AS month,
  brand,
  COUNT(*) AS orders,
  SUM(charged_amount) AS gmv,
  SUM(discount_amount) AS discounts,
  AVG(charged_amount) AS aov
FROM zs_observe.target_sales
WHERE is_active = true AND order_status = 'SHIPPED'
GROUP BY 1, 2
ORDER BY 1, 2;
```

### 7.2 SKU-Level Sales Performance

```sql
SELECT
  s.tcin, s.sku_id, m.brand,
  COUNT(*) AS units_sold,
  SUM(s.charged_amount) AS revenue,
  SUM(s.discount_amount) AS discounts
FROM zs_observe.target_sales s
LEFT JOIN zs_observe.target_tcin_mapping m ON s.tcin = m.tcin AND m.is_active = true
WHERE s.is_active = true AND s.order_status = 'SHIPPED'
GROUP BY s.tcin, s.sku_id, m.brand
ORDER BY units_sold DESC;
```

### 7.3 Sales → Settlement Join

```sql
SELECT
  s.order_id, s.item_id, s.charged_amount AS sales_price,
  st.settled_amount, st.gross_commission, st.gross_commission_percentage
FROM zs_observe.target_sales s
LEFT JOIN zs_observe.target_settlement st
  ON s.item_id = st.item_id AND st.is_active = true
WHERE s.is_active = true AND s.order_status = 'SHIPPED';
```

### 7.4 Return Rate by Brand

```sql
SELECT
  s.brand,
  COUNT(DISTINCT s.order_id) AS sold_orders,
  COUNT(DISTINCT r.order_id) AS returned_orders,
  ROUND(100.0 * COUNT(DISTINCT r.order_id)
    / NULLIF(COUNT(DISTINCT s.order_id), 0), 2) AS return_rate_pct
FROM zs_observe.target_sales s
LEFT JOIN zs_observe.target_returns r
  ON s.order_id = r.order_id AND r.is_active = true
WHERE s.is_active = true AND s.order_status = 'SHIPPED'
GROUP BY s.brand;
```
````
