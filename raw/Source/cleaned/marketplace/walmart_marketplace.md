# Walmart Marketplace Clean Markdown — V3 Gold-Standard Card-Ready Reference, Unified Edges

```yaml
document_metadata:
  document_id: walmart_marketplace_clean_md_v3_gold_standard_formatted
  vendor: Walmart
  source_docx: /mnt/data/Walmart Recon KB.docx
  source_markdown: null
  manifest: /mnt/data/marketplace_cleanup_manifest_consolidated_v2.md
  generated_on: '2026-05-24'
  frame_of_reference: marketplace_gold_standard_docx_to_clean_md_reference_v3 + marketplace_cleanup_manifest_consolidated_v2
  scope: marketplace_specific_clean_markdown_for_deterministic_parser_with_unified_edges
  marketplace_only: true
  creation_mode: created_from_docx_source_material_then_reformatted_to_flipkart_gold_standard_structure
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
  - warehouse_management
  - external_logistics_lifecycle
  allowed_card_types:
  - platform
  - platform_context
  - domain
  - table
  - column
  - relationship
  - value_profile
  - metric
  - metric_implementation
  - formula_template
  - metric_dependency
  - business_process
  - workflow_step
  - state_transition
  - process_variant
  - reconciliation_profile
  - reconciliation_side
  - reconciliation_unit
  - matching_logic
  - mismatch_category
  - reconciliation_variant
  - query_pattern
  - rule
  - validation_test
  - output_contract
  - execution_constraint_set
```

## 0.1 Redraft Notes — V3 Gold-Standard Format Correction

This V3 corrects the Walmart file shape against the Flipkart gold-standard markdown. V2 was semantically useful but structurally off: cards were flattened, edge blocks used `source_id`/`target_id`, card families were not separated into the canonical 5.x sections, and zero-count sections such as process variants and reconciliation variants were not explicitly represented. V3 preserves the Walmart source-backed semantics while restoring the gold-standard layout, explicit business-process section, value-profile/value-pattern section, metric-dependency section, execution-constraint section, unified edge registry, SQL registry, review registry, quality gates, and coverage summary.

## 0. Parser Instructions

This document is intended to be parsed deterministically. It is not a prose-only summary. It uses a unified marketplace edge taxonomy and gold-standard card-family sectioning. Every `candidate_card`, `candidate_edge`, `review_item`, and SQL reference block is designed to be machine-readable while preserving the marketplace-only boundary.

Critical parser rules:

- Create only Walmart marketplace semantic cards from this document.
- Do not create tenant, group, platform account, account binding, business scope, business flow, bank, payment gateway, external logistics, WMS/warehouse, ERP/accounting, or statutory filing cards.
- Treat `group_level_id = 22` only as documented Walmart/Folkulture scope metadata and a filter value; runtime account binding is outside this marketplace canonical.
- Treat WFS as marketplace fulfilment context/value semantics, not as a warehouse-management or process-variant topology.
- Treat Walmart Marketplace Facilitator tax as withheld/remitted by Walmart and not as seller revenue, Indian GST/TCS/TDS, or statutory tax filing.
- Never use `walmart_settlement.settled_amount` as transaction-level seller payout; use the documented computed payout formula.
- Normalize all edge blocks to `source`, `target`, and `fields`; do not ingest legacy `source_id`/`target_id` edge shape.
- Materialize inverse edges only when `materialize_inverse: true`; otherwise use reverse graph indexes.

## 1. Source Intake and Evidence Registry

```yaml
source_evidence:
  id: ev.walmart.overview.001
  source_document: Walmart Recon KB.docx
  source_section: Tab 1 > 1. Walmart Marketplace Overview
  evidence_type: prose
  summary: Walmart.com US marketplace context for Folkulture, group_level_id 22, USD currency, curated seller model, MPF tax
    model, and 100% WFS fulfilment in the dataset.
  supported_semantics:
  - platform context
  - documented scope values
  - currency context
  - WFS fulfilment context
  - marketplace facilitator tax context
  unsupported_semantics:
  - tenant/group/account-binding cards
  - bank account cards
  - statutory tax filing cards
  confidence: high
```

```yaml
source_evidence:
  id: ev.walmart.business_model.001
  source_document: Walmart Recon KB.docx
  source_section: Tab 1 > 2. Walmart Business Model
  evidence_type: business_rule
  summary: Defines referral-fee based Walmart business model, WFS handling, MPF sales-tax withholding, no Indian GST/TCS/TDS,
    and effective payout formula.
  supported_semantics:
  - referral fee model
  - WFS marketplace fulfilment model
  - MPF tax withholding
  - net payout formula
  - no Indian tax deductions
  unsupported_semantics:
  - external WFS warehouse operations
  - Indian tax filing obligations
  confidence: high
```

```yaml
source_evidence:
  id: ev.walmart.lifecycle.001
  source_document: Walmart Recon KB.docx
  source_section: Tab 1 > 3. Transaction Lifecycle
  evidence_type: workflow
  summary: Defines forward sale, return/refund, and cancellation flows using walmart_oms order_status/internal_txn_type and
    walmart_settlement transaction_type/other_type.
  supported_semantics:
  - forward sale lifecycle
  - refund lifecycle
  - cancellation without settlement
  - state transitions
  unsupported_semantics:
  - process_variant cards for WFS/COD/category labels
  confidence: high
```

```yaml
source_evidence:
  id: ev.walmart.relationships.001
  source_document: Walmart Recon KB.docx
  source_section: Tab 1 > 4. Entity Relationships
  evidence_type: reconciliation_playbook
  summary: 'Defines joins and coverage: OMS to settlement by order_id at 89.6%, OMS to lookup by sku_id=sku at 98.1%, settlement
    to lookup by sku_id=sku at 98.1%; partner_gtin corresponds to OMS item_id.'
  supported_semantics:
  - join map
  - relationship cards
  - coverage guidance
  - reconciliation units
  unsupported_semantics:
  - guaranteed one-to-one match across all date ranges
  confidence: high
```

```yaml
source_evidence:
  id: ev.walmart.metrics.001
  source_document: Walmart Recon KB.docx
  source_section: Tab 1 > 5. Key Business Metrics (with SQL)
  evidence_type: metric_definition
  summary: Defines SQL for forward GMV, product revenue, tax withheld, commission, Walmart-funded savings, net seller revenue,
    commission rate, return rate, AOV, monthly trend, SKU revenue, state distribution, and payout cycle summary.
  supported_semantics:
  - metric cards
  - metric implementations
  - SQL patterns
  - output contracts
  unsupported_semantics:
  - hard universal benchmarks
  confidence: high
```

```yaml
source_evidence:
  id: ev.walmart.reconciliation.001
  source_document: Walmart Recon KB.docx
  source_section: Tab 1 > 6. Reconciliation Use Cases
  evidence_type: query_example
  summary: Provides OMS-settlement reconciliation with 0.10 price-variance threshold, commission validation with 13.46% baseline
    and 0.50 variance threshold, refund-sale match, and three-table enriched view.
  supported_semantics:
  - reconciliation profiles
  - matching logic
  - mismatch categories
  - validation tests
  - query patterns
  unsupported_semantics:
  - universal tolerance outside Walmart context
  confidence: high
```

```yaml
source_evidence:
  id: ev.walmart.quality.001
  source_document: Walmart Recon KB.docx
  source_section: Tab 1 > 7. Data Quality Observations & Known Issues
  evidence_type: caveat
  summary: Documents OMS column shifting, settled_amount always zero, inactive settlement rows, NULL internal_txn_type fallback,
    NULL commission-rate columns, hsn barcode caveat, absent WFS fee rows, lookup sku-null caveat, and expected OMS-settlement
    coverage gap.
  supported_semantics:
  - rules
  - caveats
  - validation tests
  - review items
  unsupported_semantics:
  - blind use of settled_amount as payout
  - HSN tax analysis from OMS hsn
  confidence: high
```

```yaml
source_evidence:
  id: ev.walmart.filters.001
  source_document: Walmart Recon KB.docx
  source_section: Tab 1 > 8. Mandatory Query Filters
  evidence_type: rule_list
  summary: All Walmart tables require is_active=true and group_level_id=22; OMS delivered sales require order_status=DELIVERED
    and internal_txn_type=sales; clean geography uses LENGTH(destination_state)=2; settlement forward/reverse use transaction_type
    filters; lookup joins require sku IS NOT NULL.
  supported_semantics:
  - mandatory filters
  - scope identifier metadata
  - query guardrails
  unsupported_semantics:
  - tenant/account-binding cards
  confidence: high
```

```yaml
source_evidence:
  id: ev.walmart.table_summary.001
  source_document: Walmart Recon KB.docx
  source_section: Tab 1 > 9. Table Summary Reference
  evidence_type: schema_reference
  summary: Defines core tables walmart_oms, walmart_settlement, and walmart_lookup with active rows, date ranges, primary
    keys, join keys, and group_level_id 22.
  supported_semantics:
  - table cards
  - table grain
  - primary keys
  - join keys
  - scope values
  unsupported_semantics:
  - additional tables without full schema
  confidence: high
```

```yaml
source_evidence:
  id: ev.walmart_lookup.schema.001
  source_document: Walmart Recon KB.docx
  source_section: Tab 2 > Walmart Lookup Table KB
  evidence_type: schema_reference
  summary: walmart_lookup is product catalogue reference with 673 usable SKU rows, 3,093 sku-null content rows, columns sku_id,
    sku, item_name, currency_type, group_level_id, is_active, and source lineage fields.
  supported_semantics:
  - lookup table card
  - lookup columns
  - sku-null caveat
  - catalogue enrichment
  unsupported_semantics:
  - using sku-null rows for joins
  confidence: high
```

```yaml
source_evidence:
  id: ev.walmart_settlement.schema.001
  source_document: Walmart Recon KB.docx
  source_section: Tab 3 > Walmart Settlement Table KB
  evidence_type: schema_reference
  summary: walmart_settlement is financial transaction and payout report with 99 columns; settled_amount is always zero, metadata_2
    is period end, metadata_3 is payout date, financial fields include charged_amount, charged_amount_excluding_tax, total_tax,
    gross_commission, marketplace_withheld_tax, and Walmart-funded savings.
  supported_semantics:
  - settlement table card
  - settlement financial columns
  - payout formula
  - transaction type profiles
  - MPF tax semantics
  unsupported_semantics:
  - transaction-level payout from settled_amount
  confidence: high
```

```yaml
source_evidence:
  id: ev.walmart_settlement.values.001
  source_document: Walmart Recon KB.docx
  source_section: Tab 3 > Distinct Value Analysis
  evidence_type: table
  summary: Settlement distinct values include transaction_type forward/reverse, internal_txn_type sales/refunds with NULL
    fallback, product categories/types, product tax codes 2038710 and 2039973, and 17 payout dates.
  supported_semantics:
  - value_profile cards
  - payout cycle logic
  - category segmentation
  unsupported_semantics:
  - process variants from product categories or WFS labels
  confidence: high
```

```yaml
source_evidence:
  id: ev.walmart_oms.schema.001
  source_document: Walmart Recon KB.docx
  source_section: Tab 4 > Walmart OMS Table KB
  evidence_type: schema_reference
  summary: walmart_oms is line-item order tracking table with 972 active rows, 917 orders, 54 SKUs, created/shipped dates,
    order_status values, charged_amount, quantity, destination state/city, item_id/GTIN, sku_id, and group_level_id 22.
  supported_semantics:
  - OMS table card
  - OMS columns
  - order_status profile
  - AOV and cancellation metrics
  - state distribution
  unsupported_semantics:
  - Indian HSN tax semantics from hsn
  confidence: high
```

```yaml
source_evidence:
  id: ev.walmart_oms.quality.001
  source_document: Walmart Recon KB.docx
  source_section: Tab 4 > Data Quality Observations
  evidence_type: caveat
  summary: OMS has column shifting in some rows; clean financial analysis should use order_status and internal_txn_type filters
    plus currency_type=USD or LENGTH(destination_state)=2 when needed; mp_sin is NULL; hsn is barcode/GTIN not Indian HSN.
  supported_semantics:
  - clean row rules
  - quality validation tests
  - HSN caveat
  unsupported_semantics:
  - GST or HSN tax analysis from OMS
  confidence: high
```

## 2. Out-of-Scope Registry

```yaml
out_of_scope_item:
  id: oos.walmart.bank_account.001
  topic: bank_transfer
  source_section: Tab 1 > 2.4 Settlement Payout Mechanics
  mention: Net payout is deposited to seller US bank account and metadata_3 is payout date.
  instruction: Allowed as payout-date/settlement metadata only; do not create bank_account or bank reconciliation cards.
  allowed_as: payout date and computed payout caveat
  forbidden_card_population:
  - bank_account
  - bank_reconciliation
  - payment_gateway_account
  evidence_refs:
  - ev.walmart.business_model.001
```

```yaml
out_of_scope_item:
  id: oos.walmart.wfs_operations.001
  topic: external_wfs_operations
  source_section: Tab 1 > 2.2 WFS Model
  mention: Walmart picks, packs, ships, and handles returns from FC.
  instruction: Allowed as WFS fulfilment context/value profile; do not create warehouse management or external logistics lifecycle
    cards.
  allowed_as: fulfilment model context
  forbidden_card_population:
  - warehouse_management
  - external_logistics_lifecycle
  - inventory_fc_operations
  evidence_refs:
  - ev.walmart.business_model.001
```

```yaml
out_of_scope_item:
  id: oos.walmart.tax_filing.001
  topic: statutory_tax_filing
  source_section: Tab 1 > 2.3 Marketplace Facilitator Tax Model
  mention: Walmart remits US sales tax to tax authorities.
  instruction: Allowed as marketplace facilitator tax semantics; do not create statutory filing obligations for seller.
  allowed_as: tax withholding semantics
  forbidden_card_population:
  - statutory_tax_filing
  - tax_return_filing
  - GST_TCS_TDS_cards
  evidence_refs:
  - ev.walmart.business_model.001
```

```yaml
out_of_scope_item:
  id: oos.walmart.account_binding.001
  topic: tenant_account_scope
  source_section: Tab 1 > 1.2 Seller Entity in Dataset
  mention: group_level_id 22, brand Folkulture, USD, WFS.
  instruction: Allowed as documented_scope_values and filter metadata only.
  allowed_as: scope filter metadata
  forbidden_card_population:
  - tenant
  - group
  - platform_account
  - account_data_binding
  evidence_refs:
  - ev.walmart.overview.001
  - ev.walmart.filters.001
```

## 3. Optional Semantic Field Contract by Canonical Card Type

| card_type | recommended optional semantic fields |
|---|---|
| `platform` | `aliases`, `regions`, `marketplace_model`, `supported_contexts`, `source_platform_codes`, `evidence_refs`, `confidence`, `review_status`, `notes` |
| `platform_context` | `country`, `currency`, `timezone`, `legal_market`, `fulfilment_models`, `sub_platforms`, `evidence_refs`, `confidence`, `review_status`, `notes` |
| `domain` | `parent_domain`, `marketplace_module`, `included_tables`, `included_metrics`, `excluded_topics`, `evidence_refs`, `confidence`, `review_status`, `notes` |
| `table` | `schema_name`, `table_name`, `grain`, `primary_keys`, `business_keys`, `date_columns`, `amount_columns`, `status_columns`, `scope_columns_as_columns_only`, `known_filters`, `source_caveats`, `evidence_refs`, `confidence`, `review_status`, `notes` |
| `column` | `table_id`, `column_name`, `data_type`, `semantic_type`, `business_meaning`, `grain_role`, `metric_role`, `join_role`, `filter_role`, `sign_semantics`, `known_values`, `normalization_rule`, `null_semantics`, `source_caveats`, `evidence_refs`, `confidence`, `review_status`, `notes` |
| `relationship` | `left_table`, `right_table`, `relationship_type`, `join_keys`, `join_grain`, `normalization`, `many_side`, `pre_aggregation_required`, `safe_join_conditions`, `unsafe_join_conditions`, `evidence_refs`, `confidence`, `review_status`, `notes` |
| `value_profile` | `table_id`, `column_name`, `known_values`, `canonical_values`, `value_meanings`, `null_semantics`, `normalization`, `evidence_refs`, `confidence`, `review_status`, `notes` |
| `metric` | `canonical_name`, `colloquial_names`, `metric_family`, `business_question`, `default_grain`, `default_time_basis`, `positive_direction`, `included_components`, `excluded_components`, `benchmarks`, `evidence_refs`, `confidence`, `review_status`, `notes` |
| `metric_implementation` | `metric_id`, `platform_context`, `source_table`, `source_columns`, `formula`, `filters`, `grain`, `time_basis`, `sign_handling`, `aggregation_rule`, `join_dependencies`, `metric_pattern`, `implementation_caveats`, `sql_pattern_ref`, `evidence_refs`, `confidence`, `review_status`, `notes` |
| `formula_template` | `formula_name`, `inputs`, `formula`, `semantic_constraints`, `sign_handling`, `applicable_metrics`, `evidence_refs`, `confidence`, `review_status`, `notes` |
| `metric_dependency` | `metric_id`, `depends_on`, `dependency_type`, `aggregation_order`, `required_before_computation`, `evidence_refs`, `confidence`, `review_status`, `notes` |
| `business_process` | `process_name`, `marketplace_module`, `trigger_event`, `start_state`, `end_state`, `participating_tables`, `important_columns`, `out_of_scope_external_steps`, `evidence_refs`, `confidence`, `review_status`, `notes` |
| `workflow_step` | `process_id`, `step_order`, `step_name`, `trigger`, `input_tables`, `output_semantics`, `required_keys`, `important_columns`, `evidence_refs`, `confidence`, `review_status`, `notes` |
| `state_transition` | `process_id`, `from_state`, `to_state`, `trigger`, `evidence_column`, `value_mapping`, `business_effect`, `evidence_refs`, `confidence`, `review_status`, `notes` |
| `process_variant` | `base_process`, `variant_name`, `variant_condition`, `variant_effect`, `affected_metrics`, `affected_reconciliation`, `evidence_refs`, `confidence`, `review_status`, `notes` |
| `reconciliation_profile` | `profile_name`, `expected_side`, `actual_side`, `unit`, `matching_logic`, `mismatch_categories`, `tolerance`, `date_window`, `grain`, `out_of_scope_cross_domain`, `evidence_refs`, `confidence`, `review_status`, `notes` |
| `reconciliation_side` | `profile_id`, `side_name`, `side_role`, `source_table`, `grain`, `key_columns`, `amount_columns`, `date_columns`, `filters`, `sign_handling`, `evidence_refs`, `confidence`, `review_status`, `notes` |
| `reconciliation_unit` | `unit_name`, `unit_grain`, `keys`, `normalization`, `aggregation_required`, `applicable_profiles`, `evidence_refs`, `confidence`, `review_status`, `notes` |
| `matching_logic` | `profile_id`, `logic_name`, `join_keys`, `normalization`, `pre_aggregation`, `comparison_formula`, `tolerance`, `date_window`, `failure_modes`, `evidence_refs`, `confidence`, `review_status`, `notes` |
| `mismatch_category` | `profile_id`, `category_name`, `definition`, `detection_rule`, `likely_causes`, `severity`, `recommended_output_fields`, `evidence_refs`, `confidence`, `review_status`, `notes` |
| `reconciliation_variant` | `base_profile`, `variant_name`, `variant_condition`, `variant_matching_change`, `variant_tolerance`, `evidence_refs`, `confidence`, `review_status`, `notes` |
| `query_pattern` | `query_intent`, `colloquial_phrases`, `canonical_metric_or_object`, `required_tables`, `required_filters`, `group_by_options`, `time_basis`, `join_requirements`, `sql_pattern_ref`, `evidence_refs`, `confidence`, `review_status`, `notes` |
| `rule` | `rule_name`, `rule_type`, `rule_statement`, `applies_to`, `severity`, `deterministic_action`, `exceptions`, `evidence_refs`, `confidence`, `review_status`, `notes` |
| `validation_test` | `test_name`, `test_type`, `applies_to`, `test_logic`, `expected_result`, `failure_meaning`, `severity`, `evidence_refs`, `confidence`, `review_status`, `notes` |
| `output_contract` | `contract_name`, `use_case`, `required_fields`, `recommended_fields`, `grain`, `sort_order`, `metric_columns`, `diagnostic_columns`, `evidence_refs`, `confidence`, `review_status`, `notes` |
| `execution_constraint_set` | `constraint_name`, `applies_to`, `semantic_constraints`, `aggregation_order`, `date_window_rules`, `filter_rules`, `join_rules`, `sign_rules`, `out_of_scope_runtime_constraints`, `evidence_refs`, `confidence`, `review_status`, `notes` |

## 4. Source Tables and Marketplace Modules

Primary marketplace-owned source tables in scope are `zs_observe.walmart_oms`, `zs_observe.walmart_settlement`, and `zs_observe.walmart_lookup`. Walmart OMS supplies order, SKU, status, buyer-facing amount, state, and clean-row semantics; Walmart settlement supplies transaction type, payout-period, commission, tax, refund, WFS fulfilment context, and computed payout semantics; Walmart lookup supplies SKU-to-item enrichment only when `sku IS NOT NULL`. WFS, US bank transfer, account binding, and statutory tax filing remain outside this canonical except as marketplace caveats/rules.

## 5. Candidate Cards

```yaml
candidate_card_type_counts:
  business_process: 4
  column: 125
  domain: 7
  execution_constraint_set: 2
  formula_template: 4
  matching_logic: 5
  metric: 12
  metric_dependency: 4
  metric_implementation: 12
  mismatch_category: 7
  output_contract: 7
  platform: 1
  platform_context: 1
  query_pattern: 15
  reconciliation_profile: 5
  reconciliation_side: 10
  reconciliation_unit: 5
  relationship: 4
  rule: 14
  state_transition: 4
  table: 3
  validation_test: 9
  value_profile: 11
  workflow_step: 11
```

### 5.1 Platform Cards

```yaml
candidate_card:
  card_type: platform
  card_id: platform.walmart
  name: Walmart Marketplace
  fields:
    platform_key: walmart
    display_name: Walmart Marketplace
    platform_type: marketplace
    allowed_scope: Walmart.com US marketplace semantics, OMS, settlement, catalogue lookup, marketplace facilitator tax, WFS
      marketplace fulfilment context
    excluded_scope: tenant/account binding, bank transfer reconciliation, WFS warehouse operations, statutory tax filing,
      ERP/accounting posting
    evidence_refs:
    - ev.walmart.overview.001
    confidence: high
    review_status: accepted
    notes: Walmart Marketplace
    aliases:
    - Walmart Marketplace
    - Walmart.com
    - Walmart US Marketplace
    regions:
    - US
    marketplace_model: US third-party marketplace with Walmart Fulfillment Services context and Marketplace Facilitator tax
      withholding
    supported_contexts:
    - platform_context.walmart.us
    source_platform_codes:
    - walmart
    excluded_topics: tenant/account binding, bank transfer reconciliation, WFS warehouse operations, statutory tax filing,
      ERP/accounting posting
```

### 5.2 Platform Context Cards

```yaml
candidate_card:
  card_type: platform_context
  card_id: platform_context.walmart.us
  name: Walmart US / Folkulture WFS context
  fields:
    platform: platform.walmart
    country_or_region: US
    marketplace_ids_or_labels:
    - Walmart.com
    - Walmart US Marketplace
    currency_context: USD
    seller_brand_context: Folkulture
    fulfilment_models:
    - Walmart-fulfilledWFS
    documented_scope_values:
      group_level_id:
      - 22
    scope_filter_columns:
    - group_level_id
    business_segments:
    - Home & Garden
    - Grocery
    - Office Products
    - Apparel & Accessories
    data_availability: walmart_oms, walmart_settlement, walmart_lookup in zs_observe
    evidence_refs:
    - ev.walmart.overview.001
    - ev.walmart.table_summary.001
    confidence: high
    review_status: accepted
    notes: Walmart US / Folkulture WFS context
    platform_id: platform.walmart
    country: US
    currency: USD
    legal_market: US Marketplace Facilitator tax model
```

### 5.3 Domain Cards

```yaml
candidate_card:
  card_type: domain
  card_id: domain.marketplace.walmart.orders
  name: Walmart orders domain
  fields:
    domain_key: orders
    platform_context: platform_context.walmart.us
    domain_scope: OMS order and line item lifecycle semantics
    out_of_scope_guardrail: marketplace_semantic_domain_only
    evidence_refs:
    - ev.walmart_oms.schema.001
    confidence: high
    review_status: accepted
    notes: Walmart orders domain
    parent_domain: marketplace
    marketplace_module: orders
    description: OMS order and line item lifecycle semantics
    excluded_topics: marketplace_semantic_domain_only
```

```yaml
candidate_card:
  card_type: domain
  card_id: domain.marketplace.walmart.settlement
  name: Walmart settlement domain
  fields:
    domain_key: settlement
    platform_context: platform_context.walmart.us
    domain_scope: Financial transaction report, payout-period and commission semantics
    out_of_scope_guardrail: marketplace_semantic_domain_only
    evidence_refs:
    - ev.walmart_settlement.schema.001
    confidence: high
    review_status: accepted
    notes: Walmart settlement domain
    parent_domain: marketplace
    marketplace_module: settlement
    description: Financial transaction report, payout-period and commission semantics
    excluded_topics: marketplace_semantic_domain_only
```

```yaml
candidate_card:
  card_type: domain
  card_id: domain.marketplace.walmart.catalogue
  name: Walmart catalogue lookup domain
  fields:
    domain_key: catalogue
    platform_context: platform_context.walmart.us
    domain_scope: SKU-to-product-name enrichment and catalogue reference semantics
    out_of_scope_guardrail: marketplace_semantic_domain_only
    evidence_refs:
    - ev.walmart_lookup.schema.001
    confidence: high
    review_status: accepted
    notes: Walmart catalogue lookup domain
    parent_domain: marketplace
    marketplace_module: catalogue
    description: SKU-to-product-name enrichment and catalogue reference semantics
    excluded_topics: marketplace_semantic_domain_only
```

```yaml
candidate_card:
  card_type: domain
  card_id: domain.marketplace.walmart.fees
  name: Walmart referral fee domain
  fields:
    domain_key: fees
    platform_context: platform_context.walmart.us
    domain_scope: Referral fee / gross_commission deductions and rate validation
    out_of_scope_guardrail: marketplace_semantic_domain_only
    evidence_refs:
    - ev.walmart.business_model.001
    confidence: high
    review_status: accepted
    notes: Walmart referral fee domain
    parent_domain: marketplace
    marketplace_module: fees
    description: Referral fee / gross_commission deductions and rate validation
    excluded_topics: marketplace_semantic_domain_only
```

```yaml
candidate_card:
  card_type: domain
  card_id: domain.marketplace.walmart.tax
  name: Walmart MPF tax domain
  fields:
    domain_key: tax
    platform_context: platform_context.walmart.us
    domain_scope: US marketplace facilitator tax withholding and no Indian TCS/TDS/GST semantics
    out_of_scope_guardrail: marketplace_semantic_domain_only
    evidence_refs:
    - ev.walmart.business_model.001
    confidence: high
    review_status: accepted
    notes: Walmart MPF tax domain
    parent_domain: marketplace
    marketplace_module: tax
    description: US marketplace facilitator tax withholding and no Indian TCS/TDS/GST semantics
    excluded_topics: marketplace_semantic_domain_only
```

```yaml
candidate_card:
  card_type: domain
  card_id: domain.marketplace.walmart.returns
  name: Walmart returns and refunds domain
  fields:
    domain_key: returns
    platform_context: platform_context.walmart.us
    domain_scope: Reverse settlement rows and commission/tax reversal semantics
    out_of_scope_guardrail: marketplace_semantic_domain_only
    evidence_refs:
    - ev.walmart.lifecycle.001
    confidence: high
    review_status: accepted
    notes: Walmart returns and refunds domain
    parent_domain: marketplace
    marketplace_module: returns
    description: Reverse settlement rows and commission/tax reversal semantics
    excluded_topics: marketplace_semantic_domain_only
```

```yaml
candidate_card:
  card_type: domain
  card_id: domain.marketplace.walmart.reconciliation
  name: Walmart reconciliation domain
  fields:
    domain_key: reconciliation
    platform_context: platform_context.walmart.us
    domain_scope: OMS-settlement, refund-sale, commission, tax, and lookup reconciliation semantics
    out_of_scope_guardrail: marketplace_semantic_domain_only
    evidence_refs:
    - ev.walmart.reconciliation.001
    confidence: high
    review_status: accepted
    notes: Walmart reconciliation domain
    parent_domain: marketplace
    marketplace_module: reconciliation
    description: OMS-settlement, refund-sale, commission, tax, and lookup reconciliation semantics
    excluded_topics: marketplace_semantic_domain_only
```

### 5.4 Table Cards

```yaml
candidate_card:
  card_type: table
  card_id: table.zs_observe.walmart_oms
  name: zs_observe.walmart_oms
  fields:
    schema: zs_observe
    table_name: walmart_oms
    full: zs_observe.walmart_oms
    platform_context: platform_context.walmart.us
    domain: domain.marketplace.walmart.orders
    grain: one order line item / SKU purchase row
    date_column: created_date
    mandatory_filters: is_active = true; group_level_id = 22; for delivered sales use order_status = 'DELIVERED' AND internal_txn_type
      = 'sales'
    optional_filters: currency_type = 'USD' for clean financial rows; LENGTH(destination_state)=2 for geography
    scope: marketplace source table
    documented_scope_values:
      group_level_id:
      - 22
    quality_notes: currency_type = 'USD' for clean financial rows; LENGTH(destination_state)=2 for geography
    evidence_refs:
    - ev.walmart_oms.schema.001
    - ev.walmart.filters.001
    confidence: high
    review_status: accepted
    notes: zs_observe.walmart_oms
```

```yaml
candidate_card:
  card_type: table
  card_id: table.zs_observe.walmart_settlement
  name: zs_observe.walmart_settlement
  fields:
    schema: zs_observe
    table_name: walmart_settlement
    full: zs_observe.walmart_settlement
    platform_context: platform_context.walmart.us
    domain: domain.marketplace.walmart.settlement
    grain: financial transaction row within Walmart settlement/payout cycle
    date_column: metadata_2
    mandatory_filters: is_active = true; group_level_id = 22; transaction_type filter required for forward/reverse questions
    optional_filters: metadata_3 for payout date; do not use settled_amount as payout
    scope: marketplace source table
    documented_scope_values:
      group_level_id:
      - 22
    quality_notes: metadata_3 for payout date; do not use settled_amount as payout
    evidence_refs:
    - ev.walmart_settlement.schema.001
    - ev.walmart.filters.001
    confidence: high
    review_status: accepted
    notes: zs_observe.walmart_settlement
```

```yaml
candidate_card:
  card_type: table
  card_id: table.zs_observe.walmart_lookup
  name: zs_observe.walmart_lookup
  fields:
    schema: zs_observe
    table_name: walmart_lookup
    full: zs_observe.walmart_lookup
    platform_context: platform_context.walmart.us
    domain: domain.marketplace.walmart.catalogue
    grain: catalogue/reference row; only sku-populated rows are joinable SKU records
    date_column: created_at
    mandatory_filters: is_active = true; group_level_id = 22; sku IS NOT NULL for joins
    optional_filters: sku-null rows are content/attribute rows and not safe for SKU joins
    scope: marketplace source table
    documented_scope_values:
      group_level_id:
      - 22
    quality_notes: sku-null rows are content/attribute rows and not safe for SKU joins
    evidence_refs:
    - ev.walmart_lookup.schema.001
    - ev.walmart.filters.001
    confidence: high
    review_status: accepted
    notes: zs_observe.walmart_lookup
```

### 5.5 Column Cards

```yaml
candidate_card:
  card_type: column
  card_id: column.zs_observe.walmart_oms.unique_id
  name: walmart_oms.unique_id
  fields:
    table: table.zs_observe.walmart_oms
    column_name: unique_id
    data_type: varchar
    business_meaning: System row identifier
    semantic_category: identifier
    scope_guardrail: marketplace_semantic_column
    evidence_refs:
    - ev.walmart_oms.schema.001
    confidence: high
    review_status: accepted
    notes: System row identifier
```

```yaml
candidate_card:
  card_type: column
  card_id: column.zs_observe.walmart_oms.txn_uuid
  name: walmart_oms.txn_uuid
  fields:
    table: table.zs_observe.walmart_oms
    column_name: txn_uuid
    data_type: varchar
    business_meaning: Pipeline UUID
    semantic_category: identifier
    scope_guardrail: marketplace_semantic_column
    evidence_refs:
    - ev.walmart_oms.schema.001
    confidence: high
    review_status: accepted
    notes: Pipeline UUID
```

```yaml
candidate_card:
  card_type: column
  card_id: column.zs_observe.walmart_oms.unique_value
  name: walmart_oms.unique_value
  fields:
    table: table.zs_observe.walmart_oms
    column_name: unique_value
    data_type: varchar
    business_meaning: Deduplication hash
    semantic_category: identifier
    scope_guardrail: marketplace_semantic_column
    evidence_refs:
    - ev.walmart_oms.schema.001
    confidence: high
    review_status: accepted
    notes: Deduplication hash
```

```yaml
candidate_card:
  card_type: column
  card_id: column.zs_observe.walmart_oms.order_id
  name: walmart_oms.order_id
  fields:
    table: table.zs_observe.walmart_oms
    column_name: order_id
    data_type: varchar
    business_meaning: Walmart order number and primary join key to settlement
    semantic_category: identifier
    scope_guardrail: marketplace_semantic_column
    evidence_refs:
    - ev.walmart_oms.schema.001
    confidence: high
    review_status: accepted
    notes: Walmart order number and primary join key to settlement
```

```yaml
candidate_card:
  card_type: column
  card_id: column.zs_observe.walmart_oms.parent_id
  name: walmart_oms.parent_id
  fields:
    table: table.zs_observe.walmart_oms
    column_name: parent_id
    data_type: varchar
    business_meaning: Parent order reference / Walmart internal purchase order number
    semantic_category: identifier
    scope_guardrail: marketplace_semantic_column
    evidence_refs:
    - ev.walmart_oms.schema.001
    confidence: high
    review_status: accepted
    notes: Parent order reference / Walmart internal purchase order number
```

```yaml
candidate_card:
  card_type: column
  card_id: column.zs_observe.walmart_oms.item_id
  name: walmart_oms.item_id
  fields:
    table: table.zs_observe.walmart_oms
    column_name: item_id
    data_type: varchar
    business_meaning: Walmart item ID / GTIN barcode; corresponds to settlement partner_gtin
    semantic_category: identifier
    scope_guardrail: marketplace_semantic_column
    evidence_refs:
    - ev.walmart_oms.schema.001
    confidence: high
    review_status: accepted
    notes: Walmart item ID / GTIN barcode; corresponds to settlement partner_gtin
```

```yaml
candidate_card:
  card_type: column
  card_id: column.zs_observe.walmart_oms.mp_sin
  name: walmart_oms.mp_sin
  fields:
    table: table.zs_observe.walmart_oms
    column_name: mp_sin
    data_type: varchar
    business_meaning: Marketplace SIN; NULL for all current rows and not usable
    semantic_category: identifier
    scope_guardrail: marketplace_semantic_column
    evidence_refs:
    - ev.walmart_oms.schema.001
    confidence: high
    review_status: accepted
    notes: Marketplace SIN; NULL for all current rows and not usable
```

```yaml
candidate_card:
  card_type: column
  card_id: column.zs_observe.walmart_oms.sku_id
  name: walmart_oms.sku_id
  fields:
    table: table.zs_observe.walmart_oms
    column_name: sku_id
    data_type: varchar
    business_meaning: Seller SKU code and join key to walmart_lookup.sku
    semantic_category: identifier
    scope_guardrail: marketplace_semantic_column
    evidence_refs:
    - ev.walmart_oms.schema.001
    confidence: high
    review_status: accepted
    notes: Seller SKU code and join key to walmart_lookup.sku
```

```yaml
candidate_card:
  card_type: column
  card_id: column.zs_observe.walmart_oms.created_date
  name: walmart_oms.created_date
  fields:
    table: table.zs_observe.walmart_oms
    column_name: created_date
    data_type: date
    business_meaning: Order creation date
    semantic_category: date
    scope_guardrail: marketplace_semantic_column
    evidence_refs:
    - ev.walmart_oms.schema.001
    confidence: high
    review_status: accepted
    notes: Order creation date
```

```yaml
candidate_card:
  card_type: column
  card_id: column.zs_observe.walmart_oms.shipped_date
  name: walmart_oms.shipped_date
  fields:
    table: table.zs_observe.walmart_oms
    column_name: shipped_date
    data_type: date
    business_meaning: Shipment date, with possible column shifting in dirty rows
    semantic_category: date
    scope_guardrail: marketplace_semantic_column
    evidence_refs:
    - ev.walmart_oms.schema.001
    confidence: high
    review_status: accepted
    notes: Shipment date, with possible column shifting in dirty rows
```

```yaml
candidate_card:
  card_type: column
  card_id: column.zs_observe.walmart_oms.metadata_2
  name: walmart_oms.metadata_2
  fields:
    table: table.zs_observe.walmart_oms
    column_name: metadata_2
    data_type: varchar
    business_meaning: Transaction direction value forward when populated correctly
    semantic_category: classification
    scope_guardrail: marketplace_semantic_column
    evidence_refs:
    - ev.walmart_oms.schema.001
    confidence: high
    review_status: accepted
    notes: Transaction direction value forward when populated correctly
```

```yaml
candidate_card:
  card_type: column
  card_id: column.zs_observe.walmart_oms.charged_amount
  name: walmart_oms.charged_amount
  fields:
    table: table.zs_observe.walmart_oms
    column_name: charged_amount
    data_type: decimal
    business_meaning: Buyer-facing order price in USD for OMS sales analysis
    semantic_category: amount
    scope_guardrail: marketplace_semantic_column
    evidence_refs:
    - ev.walmart_oms.schema.001
    confidence: high
    review_status: accepted
    notes: Buyer-facing order price in USD for OMS sales analysis
```

```yaml
candidate_card:
  card_type: column
  card_id: column.zs_observe.walmart_oms.quantity
  name: walmart_oms.quantity
  fields:
    table: table.zs_observe.walmart_oms
    column_name: quantity
    data_type: integer
    business_meaning: Quantity ordered; verify on clean rows due to shifting caveat
    semantic_category: quantity
    scope_guardrail: marketplace_semantic_column
    evidence_refs:
    - ev.walmart_oms.schema.001
    confidence: high
    review_status: accepted
    notes: Quantity ordered; verify on clean rows due to shifting caveat
```

```yaml
candidate_card:
  card_type: column
  card_id: column.zs_observe.walmart_oms.internal_txn_type
  name: walmart_oms.internal_txn_type
  fields:
    table: table.zs_observe.walmart_oms
    column_name: internal_txn_type
    data_type: varchar
    business_meaning: sales for delivered order rows; NULL for some non-delivered rows
    semantic_category: classification
    scope_guardrail: marketplace_semantic_column
    evidence_refs:
    - ev.walmart_oms.schema.001
    confidence: high
    review_status: accepted
    notes: sales for delivered order rows; NULL for some non-delivered rows
```

```yaml
candidate_card:
  card_type: column
  card_id: column.zs_observe.walmart_oms.order_status
  name: walmart_oms.order_status
  fields:
    table: table.zs_observe.walmart_oms
    column_name: order_status
    data_type: varchar
    business_meaning: 'Order lifecycle status: DELIVERED, SHIPPED, CANCELLED, ACKNOWLEDGED'
    semantic_category: status
    scope_guardrail: marketplace_semantic_column
    evidence_refs:
    - ev.walmart_oms.schema.001
    confidence: high
    review_status: accepted
    notes: 'Order lifecycle status: DELIVERED, SHIPPED, CANCELLED, ACKNOWLEDGED'
```

```yaml
candidate_card:
  card_type: column
  card_id: column.zs_observe.walmart_oms.destination_state
  name: walmart_oms.destination_state
  fields:
    table: table.zs_observe.walmart_oms
    column_name: destination_state
    data_type: varchar
    business_meaning: Two-letter US state code for clean geography analysis
    semantic_category: geography
    scope_guardrail: marketplace_semantic_column
    evidence_refs:
    - ev.walmart_oms.schema.001
    confidence: high
    review_status: accepted
    notes: Two-letter US state code for clean geography analysis
```

```yaml
candidate_card:
  card_type: column
  card_id: column.zs_observe.walmart_oms.destination_city
  name: walmart_oms.destination_city
  fields:
    table: table.zs_observe.walmart_oms
    column_name: destination_city
    data_type: varchar
    business_meaning: Buyer city for clean rows
    semantic_category: geography
    scope_guardrail: marketplace_semantic_column
    evidence_refs:
    - ev.walmart_oms.schema.001
    confidence: high
    review_status: accepted
    notes: Buyer city for clean rows
```

```yaml
candidate_card:
  card_type: column
  card_id: column.zs_observe.walmart_oms.source_zipcode
  name: walmart_oms.source_zipcode
  fields:
    table: table.zs_observe.walmart_oms
    column_name: source_zipcode
    data_type: varchar
    business_meaning: Source/origin zipcode; may contain shifted product text
    semantic_category: geography
    scope_guardrail: marketplace_semantic_column
    evidence_refs:
    - ev.walmart_oms.schema.001
    confidence: high
    review_status: accepted
    notes: Source/origin zipcode; may contain shifted product text
```

```yaml
candidate_card:
  card_type: column
  card_id: column.zs_observe.walmart_oms.item_name
  name: walmart_oms.item_name
  fields:
    table: table.zs_observe.walmart_oms
    column_name: item_name
    data_type: varchar
    business_meaning: Product name; may have shifting issues, use lookup for robust product names
    semantic_category: descriptor
    scope_guardrail: marketplace_semantic_column
    evidence_refs:
    - ev.walmart_oms.schema.001
    confidence: high
    review_status: accepted
    notes: Product name; may have shifting issues, use lookup for robust product names
```

```yaml
candidate_card:
  card_type: column
  card_id: column.zs_observe.walmart_oms.hsn
  name: walmart_oms.hsn
  fields:
    table: table.zs_observe.walmart_oms
    column_name: hsn
    data_type: varchar
    business_meaning: Barcode/GTIN-like field; not Indian HSN and not suitable for tax analysis
    semantic_category: identifier
    scope_guardrail: marketplace_semantic_column
    evidence_refs:
    - ev.walmart_oms.schema.001
    confidence: high
    review_status: accepted
    notes: Barcode/GTIN-like field; not Indian HSN and not suitable for tax analysis
```

```yaml
candidate_card:
  card_type: column
  card_id: column.zs_observe.walmart_oms.group_level_id
  name: walmart_oms.group_level_id
  fields:
    table: table.zs_observe.walmart_oms
    column_name: group_level_id
    data_type: integer
    business_meaning: Documented Walmart/Folkulture account scope value 22
    semantic_category: scope_identifier
    scope_guardrail: marketplace_semantic_column
    documented_scope_values:
    - 22
    scope_usage: query filter and documented account scope value only; not an account-binding card
    evidence_refs:
    - ev.walmart_oms.schema.001
    confidence: high
    review_status: accepted
    notes: Documented Walmart/Folkulture account scope value 22
```

```yaml
candidate_card:
  card_type: column
  card_id: column.zs_observe.walmart_oms.currency_type
  name: walmart_oms.currency_type
  fields:
    table: table.zs_observe.walmart_oms
    column_name: currency_type
    data_type: varchar
    business_meaning: USD for clean rows
    semantic_category: currency
    scope_guardrail: marketplace_semantic_column
    evidence_refs:
    - ev.walmart_oms.schema.001
    confidence: high
    review_status: accepted
    notes: USD for clean rows
```

```yaml
candidate_card:
  card_type: column
  card_id: column.zs_observe.walmart_oms.is_active
  name: walmart_oms.is_active
  fields:
    table: table.zs_observe.walmart_oms
    column_name: is_active
    data_type: boolean
    business_meaning: Active flag; all rows active in source stats
    semantic_category: quality_flag
    scope_guardrail: marketplace_semantic_column
    evidence_refs:
    - ev.walmart_oms.schema.001
    confidence: high
    review_status: accepted
    notes: Active flag; all rows active in source stats
```

```yaml
candidate_card:
  card_type: column
  card_id: column.zs_observe.walmart_oms.zen_sheet_name
  name: walmart_oms.zen_sheet_name
  fields:
    table: table.zs_observe.walmart_oms
    column_name: zen_sheet_name
    data_type: varchar
    business_meaning: Source sheet label
    semantic_category: lineage
    scope_guardrail: marketplace_semantic_column
    evidence_refs:
    - ev.walmart_oms.schema.001
    confidence: high
    review_status: accepted
    notes: Source sheet label
```

```yaml
candidate_card:
  card_type: column
  card_id: column.zs_observe.walmart_oms.created_at
  name: walmart_oms.created_at
  fields:
    table: table.zs_observe.walmart_oms
    column_name: created_at
    data_type: timestamp
    business_meaning: Pipeline created timestamp
    semantic_category: lineage
    scope_guardrail: marketplace_semantic_column
    evidence_refs:
    - ev.walmart_oms.schema.001
    confidence: high
    review_status: accepted
    notes: Pipeline created timestamp
```

```yaml
candidate_card:
  card_type: column
  card_id: column.zs_observe.walmart_oms.updated_at
  name: walmart_oms.updated_at
  fields:
    table: table.zs_observe.walmart_oms
    column_name: updated_at
    data_type: timestamp
    business_meaning: Pipeline updated timestamp
    semantic_category: lineage
    scope_guardrail: marketplace_semantic_column
    evidence_refs:
    - ev.walmart_oms.schema.001
    confidence: high
    review_status: accepted
    notes: Pipeline updated timestamp
```

```yaml
candidate_card:
  card_type: column
  card_id: column.zs_observe.walmart_oms.deleted_at
  name: walmart_oms.deleted_at
  fields:
    table: table.zs_observe.walmart_oms
    column_name: deleted_at
    data_type: varchar
    business_meaning: Soft-delete metadata
    semantic_category: quality_flag
    scope_guardrail: marketplace_semantic_column
    evidence_refs:
    - ev.walmart_oms.schema.001
    confidence: high
    review_status: accepted
    notes: Soft-delete metadata
```

```yaml
candidate_card:
  card_type: column
  card_id: column.zs_observe.walmart_settlement.unique_id
  name: walmart_settlement.unique_id
  fields:
    table: table.zs_observe.walmart_settlement
    column_name: unique_id
    data_type: varchar
    business_meaning: Row identifier
    semantic_category: identifier
    scope_guardrail: marketplace_semantic_column
    evidence_refs:
    - ev.walmart_settlement.schema.001
    confidence: high
    review_status: accepted
    notes: Row identifier
```

```yaml
candidate_card:
  card_type: column
  card_id: column.zs_observe.walmart_settlement.txn_uuid
  name: walmart_settlement.txn_uuid
  fields:
    table: table.zs_observe.walmart_settlement
    column_name: txn_uuid
    data_type: varchar
    business_meaning: Pipeline UUID
    semantic_category: identifier
    scope_guardrail: marketplace_semantic_column
    evidence_refs:
    - ev.walmart_settlement.schema.001
    confidence: high
    review_status: accepted
    notes: Pipeline UUID
```

```yaml
candidate_card:
  card_type: column
  card_id: column.zs_observe.walmart_settlement.unique_value
  name: walmart_settlement.unique_value
  fields:
    table: table.zs_observe.walmart_settlement
    column_name: unique_value
    data_type: varchar
    business_meaning: Deduplication hash
    semantic_category: identifier
    scope_guardrail: marketplace_semantic_column
    evidence_refs:
    - ev.walmart_settlement.schema.001
    confidence: high
    review_status: accepted
    notes: Deduplication hash
```

```yaml
candidate_card:
  card_type: column
  card_id: column.zs_observe.walmart_settlement.order_id
  name: walmart_settlement.order_id
  fields:
    table: table.zs_observe.walmart_settlement
    column_name: order_id
    data_type: varchar
    business_meaning: Walmart order number and primary join key to walmart_oms
    semantic_category: identifier
    scope_guardrail: marketplace_semantic_column
    evidence_refs:
    - ev.walmart_settlement.schema.001
    confidence: high
    review_status: accepted
    notes: Walmart order number and primary join key to walmart_oms
```

```yaml
candidate_card:
  card_type: column
  card_id: column.zs_observe.walmart_settlement.parent_id
  name: walmart_settlement.parent_id
  fields:
    table: table.zs_observe.walmart_settlement
    column_name: parent_id
    data_type: varchar
    business_meaning: Parent purchase order number
    semantic_category: identifier
    scope_guardrail: marketplace_semantic_column
    evidence_refs:
    - ev.walmart_settlement.schema.001
    confidence: high
    review_status: accepted
    notes: Parent purchase order number
```

```yaml
candidate_card:
  card_type: column
  card_id: column.zs_observe.walmart_settlement.sku_id
  name: walmart_settlement.sku_id
  fields:
    table: table.zs_observe.walmart_settlement
    column_name: sku_id
    data_type: varchar
    business_meaning: Seller SKU and join key to walmart_lookup.sku
    semantic_category: identifier
    scope_guardrail: marketplace_semantic_column
    evidence_refs:
    - ev.walmart_settlement.schema.001
    confidence: high
    review_status: accepted
    notes: Seller SKU and join key to walmart_lookup.sku
```

```yaml
candidate_card:
  card_type: column
  card_id: column.zs_observe.walmart_settlement.partner_gtin
  name: walmart_settlement.partner_gtin
  fields:
    table: table.zs_observe.walmart_settlement
    column_name: partner_gtin
    data_type: varchar
    business_meaning: Product GTIN/barcode; corresponds to walmart_oms.item_id
    semantic_category: identifier
    scope_guardrail: marketplace_semantic_column
    evidence_refs:
    - ev.walmart_settlement.schema.001
    confidence: high
    review_status: accepted
    notes: Product GTIN/barcode; corresponds to walmart_oms.item_id
```

```yaml
candidate_card:
  card_type: column
  card_id: column.zs_observe.walmart_settlement.partner_item_id
  name: walmart_settlement.partner_item_id
  fields:
    table: table.zs_observe.walmart_settlement
    column_name: partner_item_id
    data_type: varchar
    business_meaning: Walmart internal item ID
    semantic_category: identifier
    scope_guardrail: marketplace_semantic_column
    evidence_refs:
    - ev.walmart_settlement.schema.001
    confidence: high
    review_status: accepted
    notes: Walmart internal item ID
```

```yaml
candidate_card:
  card_type: column
  card_id: column.zs_observe.walmart_settlement.partner_item_name
  name: walmart_settlement.partner_item_name
  fields:
    table: table.zs_observe.walmart_settlement
    column_name: partner_item_name
    data_type: varchar
    business_meaning: Partner item name
    semantic_category: descriptor
    scope_guardrail: marketplace_semantic_column
    evidence_refs:
    - ev.walmart_settlement.schema.001
    confidence: high
    review_status: accepted
    notes: Partner item name
```

```yaml
candidate_card:
  card_type: column
  card_id: column.zs_observe.walmart_settlement.created_date
  name: walmart_settlement.created_date
  fields:
    table: table.zs_observe.walmart_settlement
    column_name: created_date
    data_type: timestamp
    business_meaning: Record creation timestamp
    semantic_category: date
    scope_guardrail: marketplace_semantic_column
    evidence_refs:
    - ev.walmart_settlement.schema.001
    confidence: high
    review_status: accepted
    notes: Record creation timestamp
```

```yaml
candidate_card:
  card_type: column
  card_id: column.zs_observe.walmart_settlement.metadata_2
  name: walmart_settlement.metadata_2
  fields:
    table: table.zs_observe.walmart_settlement
    column_name: metadata_2
    data_type: date
    business_meaning: Settlement period end date; primary financial date
    semantic_category: date
    scope_guardrail: marketplace_semantic_column
    evidence_refs:
    - ev.walmart_settlement.schema.001
    confidence: high
    review_status: accepted
    notes: Settlement period end date; primary financial date
```

```yaml
candidate_card:
  card_type: column
  card_id: column.zs_observe.walmart_settlement.metadata_3
  name: walmart_settlement.metadata_3
  fields:
    table: table.zs_observe.walmart_settlement
    column_name: metadata_3
    data_type: date
    business_meaning: Payout/payment date; date funds hit seller bank according to report metadata
    semantic_category: date
    scope_guardrail: marketplace_semantic_column
    evidence_refs:
    - ev.walmart_settlement.schema.001
    confidence: high
    review_status: accepted
    notes: Payout/payment date; date funds hit seller bank according to report metadata
```

```yaml
candidate_card:
  card_type: column
  card_id: column.zs_observe.walmart_settlement.period_start_date
  name: walmart_settlement.period_start_date
  fields:
    table: table.zs_observe.walmart_settlement
    column_name: period_start_date
    data_type: varchar
    business_meaning: Raw period start date
    semantic_category: date_raw
    scope_guardrail: marketplace_semantic_column
    evidence_refs:
    - ev.walmart_settlement.schema.001
    confidence: high
    review_status: accepted
    notes: Raw period start date
```

```yaml
candidate_card:
  card_type: column
  card_id: column.zs_observe.walmart_settlement.period_end_date
  name: walmart_settlement.period_end_date
  fields:
    table: table.zs_observe.walmart_settlement
    column_name: period_end_date
    data_type: varchar
    business_meaning: Raw period end date
    semantic_category: date_raw
    scope_guardrail: marketplace_semantic_column
    evidence_refs:
    - ev.walmart_settlement.schema.001
    confidence: high
    review_status: accepted
    notes: Raw period end date
```

```yaml
candidate_card:
  card_type: column
  card_id: column.zs_observe.walmart_settlement.transaction_posted_timestamp
  name: walmart_settlement.transaction_posted_timestamp
  fields:
    table: table.zs_observe.walmart_settlement
    column_name: transaction_posted_timestamp
    data_type: varchar
    business_meaning: Raw transaction posting timestamp
    semantic_category: date_raw
    scope_guardrail: marketplace_semantic_column
    evidence_refs:
    - ev.walmart_settlement.schema.001
    confidence: high
    review_status: accepted
    notes: Raw transaction posting timestamp
```

```yaml
candidate_card:
  card_type: column
  card_id: column.zs_observe.walmart_settlement.charged_amount
  name: walmart_settlement.charged_amount
  fields:
    table: table.zs_observe.walmart_settlement
    column_name: charged_amount
    data_type: decimal
    business_meaning: Total buyer-facing price including tax; negative for refunds
    semantic_category: amount
    scope_guardrail: marketplace_semantic_column
    evidence_refs:
    - ev.walmart_settlement.schema.001
    confidence: high
    review_status: accepted
    notes: Total buyer-facing price including tax; negative for refunds
```

```yaml
candidate_card:
  card_type: column
  card_id: column.zs_observe.walmart_settlement.charged_amount_excluding_tax
  name: walmart_settlement.charged_amount_excluding_tax
  fields:
    table: table.zs_observe.walmart_settlement
    column_name: charged_amount_excluding_tax
    data_type: decimal
    business_meaning: Product price excluding tax; base for commission and seller payout
    semantic_category: amount
    scope_guardrail: marketplace_semantic_column
    evidence_refs:
    - ev.walmart_settlement.schema.001
    confidence: high
    review_status: accepted
    notes: Product price excluding tax; base for commission and seller payout
```

```yaml
candidate_card:
  card_type: column
  card_id: column.zs_observe.walmart_settlement.total_tax
  name: walmart_settlement.total_tax
  fields:
    table: table.zs_observe.walmart_settlement
    column_name: total_tax
    data_type: decimal
    business_meaning: US sales tax collected and withheld by Walmart
    semantic_category: amount
    scope_guardrail: marketplace_semantic_column
    evidence_refs:
    - ev.walmart_settlement.schema.001
    confidence: high
    review_status: accepted
    notes: US sales tax collected and withheld by Walmart
```

```yaml
candidate_card:
  card_type: column
  card_id: column.zs_observe.walmart_settlement.gross_commission
  name: walmart_settlement.gross_commission
  fields:
    table: table.zs_observe.walmart_settlement
    column_name: gross_commission
    data_type: decimal
    business_meaning: Walmart referral fee; negative on forward sales and positive on refunds
    semantic_category: fee_amount
    scope_guardrail: marketplace_semantic_column
    evidence_refs:
    - ev.walmart_settlement.schema.001
    confidence: high
    review_status: accepted
    notes: Walmart referral fee; negative on forward sales and positive on refunds
```

```yaml
candidate_card:
  card_type: column
  card_id: column.zs_observe.walmart_settlement.marketplace_withheld_tax
  name: walmart_settlement.marketplace_withheld_tax
  fields:
    table: table.zs_observe.walmart_settlement
    column_name: marketplace_withheld_tax
    data_type: decimal
    business_meaning: Sales tax withheld by Walmart; seller never receives it
    semantic_category: tax_amount
    scope_guardrail: marketplace_semantic_column
    evidence_refs:
    - ev.walmart_settlement.schema.001
    confidence: high
    review_status: accepted
    notes: Sales tax withheld by Walmart; seller never receives it
```

```yaml
candidate_card:
  card_type: column
  card_id: column.zs_observe.walmart_settlement.settled_amount
  name: walmart_settlement.settled_amount
  fields:
    table: table.zs_observe.walmart_settlement
    column_name: settled_amount
    data_type: decimal
    business_meaning: Always zero in this report; not net payout
    semantic_category: amount_caveat
    scope_guardrail: marketplace_semantic_column
    evidence_refs:
    - ev.walmart_settlement.schema.001
    confidence: high
    review_status: accepted
    notes: Always zero in this report; not net payout
```

```yaml
candidate_card:
  card_type: column
  card_id: column.zs_observe.walmart_settlement.total_walmart_funded_savings
  name: walmart_settlement.total_walmart_funded_savings
  fields:
    table: table.zs_observe.walmart_settlement
    column_name: total_walmart_funded_savings
    data_type: decimal
    business_meaning: Discounts funded by Walmart; occasional positive seller credit
    semantic_category: amount
    scope_guardrail: marketplace_semantic_column
    evidence_refs:
    - ev.walmart_settlement.schema.001
    confidence: high
    review_status: accepted
    notes: Discounts funded by Walmart; occasional positive seller credit
```

```yaml
candidate_card:
  card_type: column
  card_id: column.zs_observe.walmart_settlement.charge_savings
  name: walmart_settlement.charge_savings
  fields:
    table: table.zs_observe.walmart_settlement
    column_name: charge_savings
    data_type: decimal
    business_meaning: Charge-level savings, mostly zero
    semantic_category: amount
    scope_guardrail: marketplace_semantic_column
    evidence_refs:
    - ev.walmart_settlement.schema.001
    confidence: high
    review_status: accepted
    notes: Charge-level savings, mostly zero
```

```yaml
candidate_card:
  card_type: column
  card_id: column.zs_observe.walmart_settlement.original_charge
  name: walmart_settlement.original_charge
  fields:
    table: table.zs_observe.walmart_settlement
    column_name: original_charge
    data_type: decimal
    business_meaning: Original charge before savings, mostly zero
    semantic_category: amount
    scope_guardrail: marketplace_semantic_column
    evidence_refs:
    - ev.walmart_settlement.schema.001
    confidence: high
    review_status: accepted
    notes: Original charge before savings, mostly zero
```

```yaml
candidate_card:
  card_type: column
  card_id: column.zs_observe.walmart_settlement.other_tax_fees
  name: walmart_settlement.other_tax_fees
  fields:
    table: table.zs_observe.walmart_settlement
    column_name: other_tax_fees
    data_type: decimal
    business_meaning: Other tax fees
    semantic_category: amount
    scope_guardrail: marketplace_semantic_column
    evidence_refs:
    - ev.walmart_settlement.schema.001
    confidence: high
    review_status: accepted
    notes: Other tax fees
```

```yaml
candidate_card:
  card_type: column
  card_id: column.zs_observe.walmart_settlement.total_amount_computed
  name: walmart_settlement.total_amount_computed
  fields:
    table: table.zs_observe.walmart_settlement
    column_name: total_amount_computed
    data_type: decimal
    business_meaning: ZenStatement-computed total amount
    semantic_category: amount
    scope_guardrail: marketplace_semantic_column
    evidence_refs:
    - ev.walmart_settlement.schema.001
    confidence: high
    review_status: accepted
    notes: ZenStatement-computed total amount
```

```yaml
candidate_card:
  card_type: column
  card_id: column.zs_observe.walmart_settlement.promo_code
  name: walmart_settlement.promo_code
  fields:
    table: table.zs_observe.walmart_settlement
    column_name: promo_code
    data_type: decimal
    business_meaning: Promotional code discount
    semantic_category: amount
    scope_guardrail: marketplace_semantic_column
    evidence_refs:
    - ev.walmart_settlement.schema.001
    confidence: high
    review_status: accepted
    notes: Promotional code discount
```

```yaml
candidate_card:
  card_type: column
  card_id: column.zs_observe.walmart_settlement.product_price
  name: walmart_settlement.product_price
  fields:
    table: table.zs_observe.walmart_settlement
    column_name: product_price
    data_type: varchar
    business_meaning: Raw product price string
    semantic_category: raw_amount
    scope_guardrail: marketplace_semantic_column
    evidence_refs:
    - ev.walmart_settlement.schema.001
    confidence: high
    review_status: accepted
    notes: Raw product price string
```

```yaml
candidate_card:
  card_type: column
  card_id: column.zs_observe.walmart_settlement.product_tax
  name: walmart_settlement.product_tax
  fields:
    table: table.zs_observe.walmart_settlement
    column_name: product_tax
    data_type: varchar
    business_meaning: Raw product tax string
    semantic_category: raw_amount
    scope_guardrail: marketplace_semantic_column
    evidence_refs:
    - ev.walmart_settlement.schema.001
    confidence: high
    review_status: accepted
    notes: Raw product tax string
```

```yaml
candidate_card:
  card_type: column
  card_id: column.zs_observe.walmart_settlement.product_tax_withheld
  name: walmart_settlement.product_tax_withheld
  fields:
    table: table.zs_observe.walmart_settlement
    column_name: product_tax_withheld
    data_type: varchar
    business_meaning: Raw tax withheld string
    semantic_category: raw_amount
    scope_guardrail: marketplace_semantic_column
    evidence_refs:
    - ev.walmart_settlement.schema.001
    confidence: high
    review_status: accepted
    notes: Raw tax withheld string
```

```yaml
candidate_card:
  card_type: column
  card_id: column.zs_observe.walmart_settlement.total_payable
  name: walmart_settlement.total_payable
  fields:
    table: table.zs_observe.walmart_settlement
    column_name: total_payable
    data_type: varchar
    business_meaning: Raw total payable string
    semantic_category: raw_amount
    scope_guardrail: marketplace_semantic_column
    evidence_refs:
    - ev.walmart_settlement.schema.001
    confidence: high
    review_status: accepted
    notes: Raw total payable string
```

```yaml
candidate_card:
  card_type: column
  card_id: column.zs_observe.walmart_settlement.wfs_inventory_fee_reimbursement
  name: walmart_settlement.wfs_inventory_fee_reimbursement
  fields:
    table: table.zs_observe.walmart_settlement
    column_name: wfs_inventory_fee_reimbursement
    data_type: decimal
    business_meaning: WFS inventory fee reimbursement; zero in current dataset
    semantic_category: fee_amount
    scope_guardrail: marketplace_semantic_column
    evidence_refs:
    - ev.walmart_settlement.schema.001
    confidence: high
    review_status: accepted
    notes: WFS inventory fee reimbursement; zero in current dataset
```

```yaml
candidate_card:
  card_type: column
  card_id: column.zs_observe.walmart_settlement.fee_reimbursement
  name: walmart_settlement.fee_reimbursement
  fields:
    table: table.zs_observe.walmart_settlement
    column_name: fee_reimbursement
    data_type: decimal
    business_meaning: General fee reimbursement; zero in current dataset
    semantic_category: fee_amount
    scope_guardrail: marketplace_semantic_column
    evidence_refs:
    - ev.walmart_settlement.schema.001
    confidence: high
    review_status: accepted
    notes: General fee reimbursement; zero in current dataset
```

```yaml
candidate_card:
  card_type: column
  card_id: column.zs_observe.walmart_settlement.wfs_fee_reimbursement
  name: walmart_settlement.wfs_fee_reimbursement
  fields:
    table: table.zs_observe.walmart_settlement
    column_name: wfs_fee_reimbursement
    data_type: decimal
    business_meaning: WFS fee reimbursement; zero in current dataset
    semantic_category: fee_amount
    scope_guardrail: marketplace_semantic_column
    evidence_refs:
    - ev.walmart_settlement.schema.001
    confidence: high
    review_status: accepted
    notes: WFS fee reimbursement; zero in current dataset
```

```yaml
candidate_card:
  card_type: column
  card_id: column.zs_observe.walmart_settlement.wfs_inbound_fee
  name: walmart_settlement.wfs_inbound_fee
  fields:
    table: table.zs_observe.walmart_settlement
    column_name: wfs_inbound_fee
    data_type: decimal
    business_meaning: WFS inbound shipping fee; zero in current dataset
    semantic_category: fee_amount
    scope_guardrail: marketplace_semantic_column
    evidence_refs:
    - ev.walmart_settlement.schema.001
    confidence: high
    review_status: accepted
    notes: WFS inbound shipping fee; zero in current dataset
```

```yaml
candidate_card:
  card_type: column
  card_id: column.zs_observe.walmart_settlement.sem_marketing_fee
  name: walmart_settlement.sem_marketing_fee
  fields:
    table: table.zs_observe.walmart_settlement
    column_name: sem_marketing_fee
    data_type: decimal
    business_meaning: Search/marketing fee; zero in current dataset
    semantic_category: fee_amount
    scope_guardrail: marketplace_semantic_column
    evidence_refs:
    - ev.walmart_settlement.schema.001
    confidence: high
    review_status: accepted
    notes: Search/marketing fee; zero in current dataset
```

```yaml
candidate_card:
  card_type: column
  card_id: column.zs_observe.walmart_settlement.transaction_type
  name: walmart_settlement.transaction_type
  fields:
    table: table.zs_observe.walmart_settlement
    column_name: transaction_type
    data_type: varchar
    business_meaning: forward for sale and reverse for refund
    semantic_category: classification
    scope_guardrail: marketplace_semantic_column
    evidence_refs:
    - ev.walmart_settlement.schema.001
    confidence: high
    review_status: accepted
    notes: forward for sale and reverse for refund
```

```yaml
candidate_card:
  card_type: column
  card_id: column.zs_observe.walmart_settlement.internal_txn_type
  name: walmart_settlement.internal_txn_type
  fields:
    table: table.zs_observe.walmart_settlement
    column_name: internal_txn_type
    data_type: varchar
    business_meaning: sales or refunds; NULL for some rows
    semantic_category: classification
    scope_guardrail: marketplace_semantic_column
    evidence_refs:
    - ev.walmart_settlement.schema.001
    confidence: high
    review_status: accepted
    notes: sales or refunds; NULL for some rows
```

```yaml
candidate_card:
  card_type: column
  card_id: column.zs_observe.walmart_settlement.other_type
  name: walmart_settlement.other_type
  fields:
    table: table.zs_observe.walmart_settlement
    column_name: other_type
    data_type: varchar
    business_meaning: Sale or Refund fallback transaction label
    semantic_category: classification
    scope_guardrail: marketplace_semantic_column
    evidence_refs:
    - ev.walmart_settlement.schema.001
    confidence: high
    review_status: accepted
    notes: Sale or Refund fallback transaction label
```

```yaml
candidate_card:
  card_type: column
  card_id: column.zs_observe.walmart_settlement.transaction_description
  name: walmart_settlement.transaction_description
  fields:
    table: table.zs_observe.walmart_settlement
    column_name: transaction_description
    data_type: varchar
    business_meaning: Purchase for forward or Refund for reverse
    semantic_category: classification
    scope_guardrail: marketplace_semantic_column
    evidence_refs:
    - ev.walmart_settlement.schema.001
    confidence: high
    review_status: accepted
    notes: Purchase for forward or Refund for reverse
```

```yaml
candidate_card:
  card_type: column
  card_id: column.zs_observe.walmart_settlement.description
  name: walmart_settlement.description
  fields:
    table: table.zs_observe.walmart_settlement
    column_name: description
    data_type: varchar
    business_meaning: Product description
    semantic_category: descriptor
    scope_guardrail: marketplace_semantic_column
    evidence_refs:
    - ev.walmart_settlement.schema.001
    confidence: high
    review_status: accepted
    notes: Product description
```

```yaml
candidate_card:
  card_type: column
  card_id: column.zs_observe.walmart_settlement.fulfilment_channel
  name: walmart_settlement.fulfilment_channel
  fields:
    table: table.zs_observe.walmart_settlement
    column_name: fulfilment_channel
    data_type: varchar
    business_meaning: Walmart-fulfilledWFS for all rows
    semantic_category: fulfilment
    scope_guardrail: marketplace_semantic_column
    evidence_refs:
    - ev.walmart_settlement.schema.001
    confidence: high
    review_status: accepted
    notes: Walmart-fulfilledWFS for all rows
```

```yaml
candidate_card:
  card_type: column
  card_id: column.zs_observe.walmart_settlement.fulfillment_type
  name: walmart_settlement.fulfillment_type
  fields:
    table: table.zs_observe.walmart_settlement
    column_name: fulfillment_type
    data_type: varchar
    business_meaning: WFS alternate fulfilment field
    semantic_category: fulfilment
    scope_guardrail: marketplace_semantic_column
    evidence_refs:
    - ev.walmart_settlement.schema.001
    confidence: high
    review_status: accepted
    notes: WFS alternate fulfilment field
```

```yaml
candidate_card:
  card_type: column
  card_id: column.zs_observe.walmart_settlement.brand
  name: walmart_settlement.brand
  fields:
    table: table.zs_observe.walmart_settlement
    column_name: brand
    data_type: varchar
    business_meaning: Folkulture brand label
    semantic_category: descriptor
    scope_guardrail: marketplace_semantic_column
    evidence_refs:
    - ev.walmart_settlement.schema.001
    confidence: high
    review_status: accepted
    notes: Folkulture brand label
```

```yaml
candidate_card:
  card_type: column
  card_id: column.zs_observe.walmart_settlement.brand_ref_1
  name: walmart_settlement.brand_ref_1
  fields:
    table: table.zs_observe.walmart_settlement
    column_name: brand_ref_1
    data_type: varchar
    business_meaning: Product-level brand reference
    semantic_category: descriptor
    scope_guardrail: marketplace_semantic_column
    evidence_refs:
    - ev.walmart_settlement.schema.001
    confidence: high
    review_status: accepted
    notes: Product-level brand reference
```

```yaml
candidate_card:
  card_type: column
  card_id: column.zs_observe.walmart_settlement.brand_ref_2
  name: walmart_settlement.brand_ref_2
  fields:
    table: table.zs_observe.walmart_settlement
    column_name: brand_ref_2
    data_type: varchar
    business_meaning: Secondary brand reference
    semantic_category: descriptor
    scope_guardrail: marketplace_semantic_column
    evidence_refs:
    - ev.walmart_settlement.schema.001
    confidence: high
    review_status: accepted
    notes: Secondary brand reference
```

```yaml
candidate_card:
  card_type: column
  card_id: column.zs_observe.walmart_settlement.product_category
  name: walmart_settlement.product_category
  fields:
    table: table.zs_observe.walmart_settlement
    column_name: product_category
    data_type: varchar
    business_meaning: Walmart category such as Home & Garden or Grocery
    semantic_category: segment
    scope_guardrail: marketplace_semantic_column
    evidence_refs:
    - ev.walmart_settlement.schema.001
    confidence: high
    review_status: accepted
    notes: Walmart category such as Home & Garden or Grocery
```

```yaml
candidate_card:
  card_type: column
  card_id: column.zs_observe.walmart_settlement.product_type
  name: walmart_settlement.product_type
  fields:
    table: table.zs_observe.walmart_settlement
    column_name: product_type
    data_type: varchar
    business_meaning: Product type within category
    semantic_category: segment
    scope_guardrail: marketplace_semantic_column
    evidence_refs:
    - ev.walmart_settlement.schema.001
    confidence: high
    review_status: accepted
    notes: Product type within category
```

```yaml
candidate_card:
  card_type: column
  card_id: column.zs_observe.walmart_settlement.product_tax_code
  name: walmart_settlement.product_tax_code
  fields:
    table: table.zs_observe.walmart_settlement
    column_name: product_tax_code
    data_type: varchar
    business_meaning: Walmart product tax code such as 2038710 or 2039973
    semantic_category: tax_classification
    scope_guardrail: marketplace_semantic_column
    evidence_refs:
    - ev.walmart_settlement.schema.001
    confidence: high
    review_status: accepted
    notes: Walmart product tax code such as 2038710 or 2039973
```

```yaml
candidate_card:
  card_type: column
  card_id: column.zs_observe.walmart_settlement.shipping_method
  name: walmart_settlement.shipping_method
  fields:
    table: table.zs_observe.walmart_settlement
    column_name: shipping_method
    data_type: varchar
    business_meaning: Shipping method
    semantic_category: fulfilment
    scope_guardrail: marketplace_semantic_column
    evidence_refs:
    - ev.walmart_settlement.schema.001
    confidence: high
    review_status: accepted
    notes: Shipping method
```

```yaml
candidate_card:
  card_type: column
  card_id: column.zs_observe.walmart_settlement.item_condition
  name: walmart_settlement.item_condition
  fields:
    table: table.zs_observe.walmart_settlement
    column_name: item_condition
    data_type: varchar
    business_meaning: Item condition
    semantic_category: descriptor
    scope_guardrail: marketplace_semantic_column
    evidence_refs:
    - ev.walmart_settlement.schema.001
    confidence: high
    review_status: accepted
    notes: Item condition
```

```yaml
candidate_card:
  card_type: column
  card_id: column.zs_observe.walmart_settlement.base_commission_rate
  name: walmart_settlement.base_commission_rate
  fields:
    table: table.zs_observe.walmart_settlement
    column_name: base_commission_rate
    data_type: varchar
    business_meaning: Commission rate source column, NULL/not published in current data
    semantic_category: raw_rate
    scope_guardrail: marketplace_semantic_column
    evidence_refs:
    - ev.walmart_settlement.schema.001
    confidence: high
    review_status: accepted
    notes: Commission rate source column, NULL/not published in current data
```

```yaml
candidate_card:
  card_type: column
  card_id: column.zs_observe.walmart_settlement.commission_rate
  name: walmart_settlement.commission_rate
  fields:
    table: table.zs_observe.walmart_settlement
    column_name: commission_rate
    data_type: varchar
    business_meaning: Effective commission rate source column, NULL/not published
    semantic_category: raw_rate
    scope_guardrail: marketplace_semantic_column
    evidence_refs:
    - ev.walmart_settlement.schema.001
    confidence: high
    review_status: accepted
    notes: Effective commission rate source column, NULL/not published
```

```yaml
candidate_card:
  card_type: column
  card_id: column.zs_observe.walmart_settlement.commission_rule
  name: walmart_settlement.commission_rule
  fields:
    table: table.zs_observe.walmart_settlement
    column_name: commission_rule
    data_type: varchar
    business_meaning: Commission rule source column, NULL/not populated
    semantic_category: raw_rate
    scope_guardrail: marketplace_semantic_column
    evidence_refs:
    - ev.walmart_settlement.schema.001
    confidence: high
    review_status: accepted
    notes: Commission rule source column, NULL/not populated
```

```yaml
candidate_card:
  card_type: column
  card_id: column.zs_observe.walmart_settlement.commission_on_product
  name: walmart_settlement.commission_on_product
  fields:
    table: table.zs_observe.walmart_settlement
    column_name: commission_on_product
    data_type: varchar
    business_meaning: Commission on product raw field
    semantic_category: raw_rate
    scope_guardrail: marketplace_semantic_column
    evidence_refs:
    - ev.walmart_settlement.schema.001
    confidence: high
    review_status: accepted
    notes: Commission on product raw field
```

```yaml
candidate_card:
  card_type: column
  card_id: column.zs_observe.walmart_settlement.commission_incentive_program
  name: walmart_settlement.commission_incentive_program
  fields:
    table: table.zs_observe.walmart_settlement
    column_name: commission_incentive_program
    data_type: varchar
    business_meaning: Commission incentive program name
    semantic_category: classification
    scope_guardrail: marketplace_semantic_column
    evidence_refs:
    - ev.walmart_settlement.schema.001
    confidence: high
    review_status: accepted
    notes: Commission incentive program name
```

```yaml
candidate_card:
  card_type: column
  card_id: column.zs_observe.walmart_settlement.incentive_program_name
  name: walmart_settlement.incentive_program_name
  fields:
    table: table.zs_observe.walmart_settlement
    column_name: incentive_program_name
    data_type: varchar
    business_meaning: Incentive program name
    semantic_category: classification
    scope_guardrail: marketplace_semantic_column
    evidence_refs:
    - ev.walmart_settlement.schema.001
    confidence: high
    review_status: accepted
    notes: Incentive program name
```

```yaml
candidate_card:
  card_type: column
  card_id: column.zs_observe.walmart_settlement.commission_saving
  name: walmart_settlement.commission_saving
  fields:
    table: table.zs_observe.walmart_settlement
    column_name: commission_saving
    data_type: varchar
    business_meaning: Commission saving raw value
    semantic_category: raw_amount
    scope_guardrail: marketplace_semantic_column
    evidence_refs:
    - ev.walmart_settlement.schema.001
    confidence: high
    review_status: accepted
    notes: Commission saving raw value
```

```yaml
candidate_card:
  card_type: column
  card_id: column.zs_observe.walmart_settlement.original_commission
  name: walmart_settlement.original_commission
  fields:
    table: table.zs_observe.walmart_settlement
    column_name: original_commission
    data_type: varchar
    business_meaning: Pre-incentive commission raw value
    semantic_category: raw_amount
    scope_guardrail: marketplace_semantic_column
    evidence_refs:
    - ev.walmart_settlement.schema.001
    confidence: high
    review_status: accepted
    notes: Pre-incentive commission raw value
```

```yaml
candidate_card:
  card_type: column
  card_id: column.zs_observe.walmart_settlement.contract_category
  name: walmart_settlement.contract_category
  fields:
    table: table.zs_observe.walmart_settlement
    column_name: contract_category
    data_type: varchar
    business_meaning: Contract category
    semantic_category: classification
    scope_guardrail: marketplace_semantic_column
    evidence_refs:
    - ev.walmart_settlement.schema.001
    confidence: high
    review_status: accepted
    notes: Contract category
```

```yaml
candidate_card:
  card_type: column
  card_id: column.zs_observe.walmart_settlement.destination_state
  name: walmart_settlement.destination_state
  fields:
    table: table.zs_observe.walmart_settlement
    column_name: destination_state
    data_type: varchar
    business_meaning: Two-letter destination state code
    semantic_category: geography
    scope_guardrail: marketplace_semantic_column
    evidence_refs:
    - ev.walmart_settlement.schema.001
    confidence: high
    review_status: accepted
    notes: Two-letter destination state code
```

```yaml
candidate_card:
  card_type: column
  card_id: column.zs_observe.walmart_settlement.destination_city
  name: walmart_settlement.destination_city
  fields:
    table: table.zs_observe.walmart_settlement
    column_name: destination_city
    data_type: varchar
    business_meaning: Buyer city
    semantic_category: geography
    scope_guardrail: marketplace_semantic_column
    evidence_refs:
    - ev.walmart_settlement.schema.001
    confidence: high
    review_status: accepted
    notes: Buyer city
```

```yaml
candidate_card:
  card_type: column
  card_id: column.zs_observe.walmart_settlement.source_zipcode
  name: walmart_settlement.source_zipcode
  fields:
    table: table.zs_observe.walmart_settlement
    column_name: source_zipcode
    data_type: varchar
    business_meaning: Source zipcode
    semantic_category: geography
    scope_guardrail: marketplace_semantic_column
    evidence_refs:
    - ev.walmart_settlement.schema.001
    confidence: high
    review_status: accepted
    notes: Source zipcode
```

```yaml
candidate_card:
  card_type: column
  card_id: column.zs_observe.walmart_settlement.ship_to_state
  name: walmart_settlement.ship_to_state
  fields:
    table: table.zs_observe.walmart_settlement
    column_name: ship_to_state
    data_type: varchar
    business_meaning: Raw ship-to state
    semantic_category: geography
    scope_guardrail: marketplace_semantic_column
    evidence_refs:
    - ev.walmart_settlement.schema.001
    confidence: high
    review_status: accepted
    notes: Raw ship-to state
```

```yaml
candidate_card:
  card_type: column
  card_id: column.zs_observe.walmart_settlement.ship_to_city
  name: walmart_settlement.ship_to_city
  fields:
    table: table.zs_observe.walmart_settlement
    column_name: ship_to_city
    data_type: varchar
    business_meaning: Raw ship-to city
    semantic_category: geography
    scope_guardrail: marketplace_semantic_column
    evidence_refs:
    - ev.walmart_settlement.schema.001
    confidence: high
    review_status: accepted
    notes: Raw ship-to city
```

```yaml
candidate_card:
  card_type: column
  card_id: column.zs_observe.walmart_settlement.ship_to_zipcode
  name: walmart_settlement.ship_to_zipcode
  fields:
    table: table.zs_observe.walmart_settlement
    column_name: ship_to_zipcode
    data_type: varchar
    business_meaning: Raw ship-to zipcode
    semantic_category: geography
    scope_guardrail: marketplace_semantic_column
    evidence_refs:
    - ev.walmart_settlement.schema.001
    confidence: high
    review_status: accepted
    notes: Raw ship-to zipcode
```

```yaml
candidate_card:
  card_type: column
  card_id: column.zs_observe.walmart_settlement.purchase_order__
  name: walmart_settlement.purchase_order__
  fields:
    table: table.zs_observe.walmart_settlement
    column_name: purchase_order__
    data_type: varchar
    business_meaning: Walmart PO number
    semantic_category: identifier
    scope_guardrail: marketplace_semantic_column
    evidence_refs:
    - ev.walmart_settlement.schema.001
    confidence: high
    review_status: accepted
    notes: Walmart PO number
```

```yaml
candidate_card:
  card_type: column
  card_id: column.zs_observe.walmart_settlement.purchase_order_line__
  name: walmart_settlement.purchase_order_line__
  fields:
    table: table.zs_observe.walmart_settlement
    column_name: purchase_order_line__
    data_type: varchar
    business_meaning: Walmart PO line number
    semantic_category: identifier
    scope_guardrail: marketplace_semantic_column
    evidence_refs:
    - ev.walmart_settlement.schema.001
    confidence: high
    review_status: accepted
    notes: Walmart PO line number
```

```yaml
candidate_card:
  card_type: column
  card_id: column.zs_observe.walmart_settlement.customer_order__
  name: walmart_settlement.customer_order__
  fields:
    table: table.zs_observe.walmart_settlement
    column_name: customer_order__
    data_type: varchar
    business_meaning: Customer order number
    semantic_category: identifier
    scope_guardrail: marketplace_semantic_column
    evidence_refs:
    - ev.walmart_settlement.schema.001
    confidence: high
    review_status: accepted
    notes: Customer order number
```

```yaml
candidate_card:
  card_type: column
  card_id: column.zs_observe.walmart_settlement.customer_order_line__
  name: walmart_settlement.customer_order_line__
  fields:
    table: table.zs_observe.walmart_settlement
    column_name: customer_order_line__
    data_type: varchar
    business_meaning: Customer order line
    semantic_category: identifier
    scope_guardrail: marketplace_semantic_column
    evidence_refs:
    - ev.walmart_settlement.schema.001
    confidence: high
    review_status: accepted
    notes: Customer order line
```

```yaml
candidate_card:
  card_type: column
  card_id: column.zs_observe.walmart_settlement.transaction_key
  name: walmart_settlement.transaction_key
  fields:
    table: table.zs_observe.walmart_settlement
    column_name: transaction_key
    data_type: varchar
    business_meaning: Transaction key
    semantic_category: identifier
    scope_guardrail: marketplace_semantic_column
    evidence_refs:
    - ev.walmart_settlement.schema.001
    confidence: high
    review_status: accepted
    notes: Transaction key
```

```yaml
candidate_card:
  card_type: column
  card_id: column.zs_observe.walmart_settlement.campaign_id
  name: walmart_settlement.campaign_id
  fields:
    table: table.zs_observe.walmart_settlement
    column_name: campaign_id
    data_type: varchar
    business_meaning: Campaign identifier
    semantic_category: identifier
    scope_guardrail: marketplace_semantic_column
    evidence_refs:
    - ev.walmart_settlement.schema.001
    confidence: high
    review_status: accepted
    notes: Campaign identifier
```

```yaml
candidate_card:
  card_type: column
  card_id: column.zs_observe.walmart_settlement.group_level_id
  name: walmart_settlement.group_level_id
  fields:
    table: table.zs_observe.walmart_settlement
    column_name: group_level_id
    data_type: integer
    business_meaning: Documented Walmart/Folkulture account scope value 22
    semantic_category: scope_identifier
    scope_guardrail: marketplace_semantic_column
    documented_scope_values:
    - 22
    scope_usage: query filter and documented account scope value only; not an account-binding card
    evidence_refs:
    - ev.walmart_settlement.schema.001
    confidence: high
    review_status: accepted
    notes: Documented Walmart/Folkulture account scope value 22
```

```yaml
candidate_card:
  card_type: column
  card_id: column.zs_observe.walmart_settlement.currency_type
  name: walmart_settlement.currency_type
  fields:
    table: table.zs_observe.walmart_settlement
    column_name: currency_type
    data_type: varchar
    business_meaning: Primary USD currency field
    semantic_category: currency
    scope_guardrail: marketplace_semantic_column
    evidence_refs:
    - ev.walmart_settlement.schema.001
    confidence: high
    review_status: accepted
    notes: Primary USD currency field
```

```yaml
candidate_card:
  card_type: column
  card_id: column.zs_observe.walmart_settlement.is_active
  name: walmart_settlement.is_active
  fields:
    table: table.zs_observe.walmart_settlement
    column_name: is_active
    data_type: boolean
    business_meaning: Active flag; 1,031 of 2,122 active
    semantic_category: quality_flag
    scope_guardrail: marketplace_semantic_column
    evidence_refs:
    - ev.walmart_settlement.schema.001
    confidence: high
    review_status: accepted
    notes: Active flag; 1,031 of 2,122 active
```

```yaml
candidate_card:
  card_type: column
  card_id: column.zs_observe.walmart_settlement.currency
  name: walmart_settlement.currency
  fields:
    table: table.zs_observe.walmart_settlement
    column_name: currency
    data_type: varchar
    business_meaning: Alternate USD currency field
    semantic_category: currency
    scope_guardrail: marketplace_semantic_column
    evidence_refs:
    - ev.walmart_settlement.schema.001
    confidence: high
    review_status: accepted
    notes: Alternate USD currency field
```

```yaml
candidate_card:
  card_type: column
  card_id: column.zs_observe.walmart_settlement.type_description_mapping
  name: walmart_settlement.type_description_mapping
  fields:
    table: table.zs_observe.walmart_settlement
    column_name: type_description_mapping
    data_type: varchar
    business_meaning: Type-description mapping
    semantic_category: classification
    scope_guardrail: marketplace_semantic_column
    evidence_refs:
    - ev.walmart_settlement.schema.001
    confidence: high
    review_status: accepted
    notes: Type-description mapping
```

```yaml
candidate_card:
  card_type: column
  card_id: column.zs_observe.walmart_settlement.debug_is_active_inputs
  name: walmart_settlement.debug_is_active_inputs
  fields:
    table: table.zs_observe.walmart_settlement
    column_name: debug_is_active_inputs
    data_type: varchar
    business_meaning: Debug field
    semantic_category: lineage
    scope_guardrail: marketplace_semantic_column
    evidence_refs:
    - ev.walmart_settlement.schema.001
    confidence: high
    review_status: accepted
    notes: Debug field
```

```yaml
candidate_card:
  card_type: column
  card_id: column.zs_observe.walmart_settlement.none
  name: walmart_settlement.none
  fields:
    table: table.zs_observe.walmart_settlement
    column_name: none
    data_type: varchar
    business_meaning: Unnamed source column
    semantic_category: raw
    scope_guardrail: marketplace_semantic_column
    evidence_refs:
    - ev.walmart_settlement.schema.001
    confidence: high
    review_status: accepted
    notes: Unnamed source column
```

```yaml
candidate_card:
  card_type: column
  card_id: column.zs_observe.walmart_settlement.excessrefundadjustment
  name: walmart_settlement.excessrefundadjustment
  fields:
    table: table.zs_observe.walmart_settlement
    column_name: excessrefundadjustment
    data_type: varchar
    business_meaning: Excess refund adjustment raw field
    semantic_category: amount
    scope_guardrail: marketplace_semantic_column
    evidence_refs:
    - ev.walmart_settlement.schema.001
    confidence: high
    review_status: accepted
    notes: Excess refund adjustment raw field
```

```yaml
candidate_card:
  card_type: column
  card_id: column.zs_observe.walmart_settlement.fulfillment_details
  name: walmart_settlement.fulfillment_details
  fields:
    table: table.zs_observe.walmart_settlement
    column_name: fulfillment_details
    data_type: varchar
    business_meaning: Fulfilment details JSON
    semantic_category: fulfilment
    scope_guardrail: marketplace_semantic_column
    evidence_refs:
    - ev.walmart_settlement.schema.001
    confidence: high
    review_status: accepted
    notes: Fulfilment details JSON
```

```yaml
candidate_card:
  card_type: column
  card_id: column.zs_observe.walmart_settlement.customer_promo_type
  name: walmart_settlement.customer_promo_type
  fields:
    table: table.zs_observe.walmart_settlement
    column_name: customer_promo_type
    data_type: varchar
    business_meaning: Customer promotion type
    semantic_category: classification
    scope_guardrail: marketplace_semantic_column
    evidence_refs:
    - ev.walmart_settlement.schema.001
    confidence: high
    review_status: accepted
    notes: Customer promotion type
```

```yaml
candidate_card:
  card_type: column
  card_id: column.zs_observe.walmart_lookup.unique_id
  name: walmart_lookup.unique_id
  fields:
    table: table.zs_observe.walmart_lookup
    column_name: unique_id
    data_type: bigint
    business_meaning: Row identifier
    semantic_category: identifier
    scope_guardrail: marketplace_semantic_column
    evidence_refs:
    - ev.walmart_lookup.schema.001
    confidence: high
    review_status: accepted
    notes: Row identifier
```

```yaml
candidate_card:
  card_type: column
  card_id: column.zs_observe.walmart_lookup.txn_uuid
  name: walmart_lookup.txn_uuid
  fields:
    table: table.zs_observe.walmart_lookup
    column_name: txn_uuid
    data_type: varchar
    business_meaning: Pipeline UUID
    semantic_category: identifier
    scope_guardrail: marketplace_semantic_column
    evidence_refs:
    - ev.walmart_lookup.schema.001
    confidence: high
    review_status: accepted
    notes: Pipeline UUID
```

```yaml
candidate_card:
  card_type: column
  card_id: column.zs_observe.walmart_lookup.unique_value
  name: walmart_lookup.unique_value
  fields:
    table: table.zs_observe.walmart_lookup
    column_name: unique_value
    data_type: varchar
    business_meaning: Deduplication hash
    semantic_category: identifier
    scope_guardrail: marketplace_semantic_column
    evidence_refs:
    - ev.walmart_lookup.schema.001
    confidence: high
    review_status: accepted
    notes: Deduplication hash
```

```yaml
candidate_card:
  card_type: column
  card_id: column.zs_observe.walmart_lookup.sku_id
  name: walmart_lookup.sku_id
  fields:
    table: table.zs_observe.walmart_lookup
    column_name: sku_id
    data_type: varchar
    business_meaning: Seller SKU code, always populated
    semantic_category: identifier
    scope_guardrail: marketplace_semantic_column
    evidence_refs:
    - ev.walmart_lookup.schema.001
    confidence: high
    review_status: accepted
    notes: Seller SKU code, always populated
```

```yaml
candidate_card:
  card_type: column
  card_id: column.zs_observe.walmart_lookup.sku
  name: walmart_lookup.sku
  fields:
    table: table.zs_observe.walmart_lookup
    column_name: sku
    data_type: varchar
    business_meaning: Seller SKU code duplicate of sku_id; NULL for content rows; use for joins only when populated
    semantic_category: identifier
    scope_guardrail: marketplace_semantic_column
    evidence_refs:
    - ev.walmart_lookup.schema.001
    confidence: high
    review_status: accepted
    notes: Seller SKU code duplicate of sku_id; NULL for content rows; use for joins only when populated
```

```yaml
candidate_card:
  card_type: column
  card_id: column.zs_observe.walmart_lookup.item_name
  name: walmart_lookup.item_name
  fields:
    table: table.zs_observe.walmart_lookup
    column_name: item_name
    data_type: varchar
    business_meaning: Product name / item description; primary enrichment field for usable SKU rows
    semantic_category: descriptor
    scope_guardrail: marketplace_semantic_column
    evidence_refs:
    - ev.walmart_lookup.schema.001
    confidence: high
    review_status: accepted
    notes: Product name / item description; primary enrichment field for usable SKU rows
```

```yaml
candidate_card:
  card_type: column
  card_id: column.zs_observe.walmart_lookup.currency_type
  name: walmart_lookup.currency_type
  fields:
    table: table.zs_observe.walmart_lookup
    column_name: currency_type
    data_type: varchar
    business_meaning: USD
    semantic_category: currency
    scope_guardrail: marketplace_semantic_column
    evidence_refs:
    - ev.walmart_lookup.schema.001
    confidence: high
    review_status: accepted
    notes: USD
```

```yaml
candidate_card:
  card_type: column
  card_id: column.zs_observe.walmart_lookup.group_level_id
  name: walmart_lookup.group_level_id
  fields:
    table: table.zs_observe.walmart_lookup
    column_name: group_level_id
    data_type: integer
    business_meaning: Documented Walmart/Folkulture account scope value 22
    semantic_category: scope_identifier
    scope_guardrail: marketplace_semantic_column
    documented_scope_values:
    - 22
    scope_usage: query filter and documented account scope value only; not an account-binding card
    evidence_refs:
    - ev.walmart_lookup.schema.001
    confidence: high
    review_status: accepted
    notes: Documented Walmart/Folkulture account scope value 22
```

```yaml
candidate_card:
  card_type: column
  card_id: column.zs_observe.walmart_lookup.is_active
  name: walmart_lookup.is_active
  fields:
    table: table.zs_observe.walmart_lookup
    column_name: is_active
    data_type: boolean
    business_meaning: Active flag, always true in source stats
    semantic_category: quality_flag
    scope_guardrail: marketplace_semantic_column
    evidence_refs:
    - ev.walmart_lookup.schema.001
    confidence: high
    review_status: accepted
    notes: Active flag, always true in source stats
```

```yaml
candidate_card:
  card_type: column
  card_id: column.zs_observe.walmart_lookup.ancestry
  name: walmart_lookup.ancestry
  fields:
    table: table.zs_observe.walmart_lookup
    column_name: ancestry
    data_type: varchar
    business_meaning: Lineage field
    semantic_category: lineage
    scope_guardrail: marketplace_semantic_column
    evidence_refs:
    - ev.walmart_lookup.schema.001
    confidence: high
    review_status: accepted
    notes: Lineage field
```

```yaml
candidate_card:
  card_type: column
  card_id: column.zs_observe.walmart_lookup.file_uuid
  name: walmart_lookup.file_uuid
  fields:
    table: table.zs_observe.walmart_lookup
    column_name: file_uuid
    data_type: varchar
    business_meaning: Source file UUID for lineage
    semantic_category: lineage
    scope_guardrail: marketplace_semantic_column
    evidence_refs:
    - ev.walmart_lookup.schema.001
    confidence: high
    review_status: accepted
    notes: Source file UUID for lineage
```

```yaml
candidate_card:
  card_type: column
  card_id: column.zs_observe.walmart_lookup.zen_sheet_name
  name: walmart_lookup.zen_sheet_name
  fields:
    table: table.zs_observe.walmart_lookup
    column_name: zen_sheet_name
    data_type: varchar
    business_meaning: Source sheet, NULL in current data
    semantic_category: lineage
    scope_guardrail: marketplace_semantic_column
    evidence_refs:
    - ev.walmart_lookup.schema.001
    confidence: high
    review_status: accepted
    notes: Source sheet, NULL in current data
```

```yaml
candidate_card:
  card_type: column
  card_id: column.zs_observe.walmart_lookup.created_at
  name: walmart_lookup.created_at
  fields:
    table: table.zs_observe.walmart_lookup
    column_name: created_at
    data_type: timestamp
    business_meaning: Pipeline created timestamp
    semantic_category: lineage
    scope_guardrail: marketplace_semantic_column
    evidence_refs:
    - ev.walmart_lookup.schema.001
    confidence: high
    review_status: accepted
    notes: Pipeline created timestamp
```

```yaml
candidate_card:
  card_type: column
  card_id: column.zs_observe.walmart_lookup.updated_at
  name: walmart_lookup.updated_at
  fields:
    table: table.zs_observe.walmart_lookup
    column_name: updated_at
    data_type: timestamp
    business_meaning: Pipeline updated timestamp
    semantic_category: lineage
    scope_guardrail: marketplace_semantic_column
    evidence_refs:
    - ev.walmart_lookup.schema.001
    confidence: high
    review_status: accepted
    notes: Pipeline updated timestamp
```

```yaml
candidate_card:
  card_type: column
  card_id: column.zs_observe.walmart_lookup.is_duplicated
  name: walmart_lookup.is_duplicated
  fields:
    table: table.zs_observe.walmart_lookup
    column_name: is_duplicated
    data_type: boolean
    business_meaning: Deduplication flag
    semantic_category: quality_flag
    scope_guardrail: marketplace_semantic_column
    evidence_refs:
    - ev.walmart_lookup.schema.001
    confidence: high
    review_status: accepted
    notes: Deduplication flag
```

```yaml
candidate_card:
  card_type: column
  card_id: column.zs_observe.walmart_lookup.zen_status
  name: walmart_lookup.zen_status
  fields:
    table: table.zs_observe.walmart_lookup
    column_name: zen_status
    data_type: boolean
    business_meaning: Pipeline status flag
    semantic_category: quality_flag
    scope_guardrail: marketplace_semantic_column
    evidence_refs:
    - ev.walmart_lookup.schema.001
    confidence: high
    review_status: accepted
    notes: Pipeline status flag
```

### 5.6 Relationship Cards

```yaml
candidate_card:
  card_type: relationship
  card_id: relationship.walmart.oms_to_settlement_order_id
  name: Walmart OMS to settlement order join
  fields:
    from_table: table.zs_observe.walmart_oms
    to_table: table.zs_observe.walmart_settlement
    join_keys:
      left_key: order_id
      right_key: order_id
    relationship_grain: order/SKU line item where keys are populated
    business_semantics: order-level reconciliation / settlement coverage
    join_safety_rule: 89.6% coverage (822/917); gaps expected due settlement timing/cancellations/historical settlement rows
    evidence_refs:
    - ev.walmart.relationships.001
    confidence: high
    review_status: accepted
    notes: Walmart OMS to settlement order join
```

```yaml
candidate_card:
  card_type: relationship
  card_id: relationship.walmart.oms_to_lookup_sku
  name: Walmart OMS to lookup SKU enrichment
  fields:
    from_table: table.zs_observe.walmart_oms
    to_table: table.zs_observe.walmart_lookup
    join_keys:
      left_key: sku_id
      right_key: sku
    relationship_grain: order/SKU line item where keys are populated
    business_semantics: product name enrichment for OMS
    join_safety_rule: 98.1% SKU coverage; require lookup.sku IS NOT NULL
    evidence_refs:
    - ev.walmart.relationships.001
    confidence: high
    review_status: accepted
    notes: Walmart OMS to lookup SKU enrichment
```

```yaml
candidate_card:
  card_type: relationship
  card_id: relationship.walmart.settlement_to_lookup_sku
  name: Walmart settlement to lookup SKU enrichment
  fields:
    from_table: table.zs_observe.walmart_settlement
    to_table: table.zs_observe.walmart_lookup
    join_keys:
      left_key: sku_id
      right_key: sku
    relationship_grain: order/SKU line item where keys are populated
    business_semantics: product name enrichment for settlement
    join_safety_rule: 98.1% SKU coverage; require lookup.sku IS NOT NULL
    evidence_refs:
    - ev.walmart.relationships.001
    confidence: high
    review_status: accepted
    notes: Walmart settlement to lookup SKU enrichment
```

```yaml
candidate_card:
  card_type: relationship
  card_id: relationship.walmart.oms_item_to_settlement_gtin
  name: Walmart OMS item_id to settlement partner_gtin reference
  fields:
    from_table: table.zs_observe.walmart_oms
    to_table: table.zs_observe.walmart_settlement
    join_keys:
      left_key: item_id
      right_key: partner_gtin
    relationship_grain: order/SKU line item where keys are populated
    business_semantics: GTIN/barcode cross-reference only
    join_safety_rule: Use as secondary product identifier, not primary financial join
    evidence_refs:
    - ev.walmart.relationships.001
    confidence: high
    review_status: accepted
    notes: Walmart OMS item_id to settlement partner_gtin reference
```

### 5.7 Value Profile Cards

```yaml
candidate_card:
  card_type: value_profile
  card_id: value_profile.walmart.oms.order_status
  name: Walmart OMS order_status values
  fields:
    column: column.zs_observe.walmart_oms.order_status
    known_values:
      DELIVERED: 917 rows; successfully delivered; use for completed sales
      CANCELLED: 37 rows; cancelled before delivery; no settlement entry expected
      SHIPPED: 17 rows; in transit at data cutoff
      ACKNOWLEDGED: 1 row; order accepted not yet shipped
    value_semantics: Use order_status as primary lifecycle filter; internal_txn_type may be NULL for non-delivered rows
    unknown_or_null_handling: Use order_status as primary lifecycle filter; internal_txn_type may be NULL for non-delivered
      rows
    evidence_refs:
    - ev.walmart_oms.schema.001
    confidence: high
    review_status: accepted
    notes: Walmart OMS order_status values
```

```yaml
candidate_card:
  card_type: value_profile
  card_id: value_profile.walmart.settlement.transaction_type
  name: Walmart settlement transaction_type values
  fields:
    column: column.zs_observe.walmart_settlement.transaction_type
    known_values:
      forward: Sale / purchase rows
      reverse: Refund rows
    value_semantics: Use transaction_type as primary settlement revenue/refund filter
    unknown_or_null_handling: Use transaction_type as primary settlement revenue/refund filter
    evidence_refs:
    - ev.walmart_settlement.values.001
    confidence: high
    review_status: accepted
    notes: Walmart settlement transaction_type values
```

```yaml
candidate_card:
  card_type: value_profile
  card_id: value_profile.walmart.settlement.internal_txn_type
  name: Walmart settlement internal_txn_type values
  fields:
    column: column.zs_observe.walmart_settlement.internal_txn_type
    known_values:
      sales: classified forward sale rows
      refunds: classified reverse refund rows
      'NULL': 161 rows not classified; fallback to other_type or transaction_type
    value_semantics: NULL values require fallback logic
    unknown_or_null_handling: NULL values require fallback logic
    evidence_refs:
    - ev.walmart.quality.001
    confidence: high
    review_status: accepted
    notes: Walmart settlement internal_txn_type values
```

```yaml
candidate_card:
  card_type: value_profile
  card_id: value_profile.walmart.settlement.other_type
  name: Walmart settlement other_type values
  fields:
    column: column.zs_observe.walmart_settlement.other_type
    known_values:
      Sale: forward sale fallback label
      Refund: reverse refund fallback label
      'NULL': some rows may be unclassified
    value_semantics: Use as fallback when internal_txn_type is NULL
    unknown_or_null_handling: Use as fallback when internal_txn_type is NULL
    evidence_refs:
    - ev.walmart.quality.001
    confidence: high
    review_status: accepted
    notes: Walmart settlement other_type values
```

```yaml
candidate_card:
  card_type: value_profile
  card_id: value_profile.walmart.settlement.fulfilment_channel
  name: Walmart WFS fulfilment channel
  fields:
    column: column.zs_observe.walmart_settlement.fulfilment_channel
    known_values:
      Walmart-fulfilledWFS: 100% of settlement rows; Walmart fulfilled services
    value_semantics: Fulfilment label only; do not create process_variant card
    unknown_or_null_handling: Fulfilment label only; do not create process_variant card
    evidence_refs:
    - ev.walmart.business_model.001
    confidence: high
    review_status: accepted
    notes: Walmart WFS fulfilment channel
```

```yaml
candidate_card:
  card_type: value_profile
  card_id: value_profile.walmart.settlement.product_category
  name: Walmart product_category values
  fields:
    column: column.zs_observe.walmart_settlement.product_category
    known_values:
      Home & Garden: Incense, pot holders, tablecloths, incense burners, wooden spoons, plant hangers, table runners
      Grocery: Kitchen towels, cooking utensil sets
      Office Products: Whiteboards
      Apparel & Accessories: Handbags, wallets, messenger bags
    value_semantics: Use for category segmentation, not process variants
    unknown_or_null_handling: Use for category segmentation, not process variants
    evidence_refs:
    - ev.walmart_settlement.values.001
    confidence: high
    review_status: accepted
    notes: Walmart product_category values
```

```yaml
candidate_card:
  card_type: value_profile
  card_id: value_profile.walmart.settlement.product_type
  name: Walmart product_type values
  fields:
    column: column.zs_observe.walmart_settlement.product_type
    known_values:
      values:
      - Bath Rugs
      - Coasters
      - Cooking Spoons
      - Decorative Bowls
      - Decorative Pillow Covers
      - Floor Mats & Doormats
      - Handbags
      - Incense
      - Incense Burners & Holders
      - Kitchen & Cooking Utensil Sets
      - Kitchen Towels
      - Messenger & Shoulder Bags
      - Plant Hangers
      - Pot Holders
      - Shower Curtains & Liners
      - Table Runners
      - Tablecloths
      - Wallets
      - Whiteboards
    value_semantics: Use for product type segmentation; no separate process topology
    unknown_or_null_handling: Use for product type segmentation; no separate process topology
    evidence_refs:
    - ev.walmart_settlement.values.001
    confidence: high
    review_status: accepted
    notes: Walmart product_type values
```

```yaml
candidate_card:
  card_type: value_profile
  card_id: value_profile.walmart.settlement.product_tax_code
  name: Walmart product_tax_code values
  fields:
    column: column.zs_observe.walmart_settlement.product_tax_code
    known_values:
      '2038710': Home & Garden / Incense / Decor
      '2039973': Kitchen / Grocery category items
    value_semantics: Walmart product tax code; not Indian HSN/GST semantics
    unknown_or_null_handling: Walmart product tax code; not Indian HSN/GST semantics
    evidence_refs:
    - ev.walmart_settlement.values.001
    confidence: high
    review_status: accepted
    notes: Walmart product_tax_code values
```

```yaml
candidate_card:
  card_type: value_profile
  card_id: value_profile.walmart.lookup.row_type
  name: Walmart lookup row types
  fields:
    column: table.zs_observe.walmart_lookup
    known_values:
      sku_records: 673 rows with sku populated; safe for joins
      content_rows: 3,093 rows with sku NULL; attribute/content rows not safe for SKU joins
    value_semantics: Always filter sku IS NOT NULL for SKU-to-name joins
    unknown_or_null_handling: Always filter sku IS NOT NULL for SKU-to-name joins
    evidence_refs:
    - ev.walmart_lookup.schema.001
    confidence: high
    review_status: accepted
    notes: Walmart lookup row types
```

```yaml
candidate_card:
  card_type: value_profile
  card_id: value_profile.walmart.currency_type
  name: Walmart currency_type values
  fields:
    column: column.zs_observe.walmart_settlement.currency_type
    known_values:
      USD: 100% Walmart dataset currency
    value_semantics: Use currency_type as primary currency field
    unknown_or_null_handling: Use currency_type as primary currency field
    evidence_refs:
    - ev.walmart.overview.001
    confidence: high
    review_status: accepted
    notes: Walmart currency_type values
```

```yaml
candidate_card:
  card_type: value_profile
  card_id: value_profile.walmart.group_level_id
  name: Walmart group_level_id documented scope value
  fields:
    column: column.zs_observe.walmart_settlement.group_level_id
    known_values:
      22: Folkulture Walmart US dataset scope
    value_semantics: Scope identifier only; runtime account selection belongs outside marketplace canonical
    unknown_or_null_handling: Scope identifier only; runtime account selection belongs outside marketplace canonical
    evidence_refs:
    - ev.walmart.filters.001
    confidence: high
    review_status: accepted
    notes: Walmart group_level_id documented scope value
```

### 5.8 Metric Cards with Colloquial Names

```yaml
candidate_card:
  card_type: metric
  card_id: metric.marketplace.gross_revenue
  name: Gross revenue / GMV
  fields:
    metric_key: gross_revenue
    business_definition: Total forward sales value including tax from Walmart settlement or delivered OMS rows.
    colloquial_names:
    - GMV
    - gross sales
    - topline
    - buyer-facing sales
    metric_pattern: sum_charged_amount_forward
    default_grain: month
    domain: domain.marketplace.walmart.orders; domain.marketplace.walmart.settlement
    scope: generic marketplace metric implemented by Walmart-specific metric_implementation cards
    evidence_refs:
    - ev.walmart.metrics.001
    confidence: high
    review_status: accepted
    notes: Total forward sales value including tax from Walmart settlement or delivered OMS rows.
```

```yaml
candidate_card:
  card_type: metric
  card_id: metric.marketplace.product_revenue_excluding_tax
  name: Product revenue excluding tax
  fields:
    metric_key: product_revenue_excluding_tax
    business_definition: Forward product price before US sales tax; this is the base for seller payout and commission analysis.
    colloquial_names:
    - product revenue
    - taxable price
    - revenue excluding tax
    metric_pattern: sum_charged_amount_excluding_tax_forward
    default_grain: month
    domain: domain.marketplace.walmart.settlement
    scope: generic marketplace metric implemented by Walmart-specific metric_implementation cards
    evidence_refs:
    - ev.walmart.metrics.001
    confidence: high
    review_status: accepted
    notes: Forward product price before US sales tax; this is the base for seller payout and commission analysis.
```

```yaml
candidate_card:
  card_type: metric
  card_id: metric.marketplace.net_seller_payout
  name: Net seller payout
  fields:
    metric_key: net_seller_payout
    business_definition: Estimated seller payout from Walmart report calculated as product revenue excluding tax plus gross_commission;
      do not use settled_amount.
    colloquial_names:
    - net payout
    - seller payout
    - estimated payout
    - net seller revenue
    metric_pattern: sum_product_revenue_plus_gross_commission
    default_grain: payout_cycle
    domain: domain.marketplace.walmart.settlement
    scope: generic marketplace metric implemented by Walmart-specific metric_implementation cards
    benchmarks:
      source_context: Net Payout = charged_amount_excluding_tax + gross_commission
    evidence_refs:
    - ev.walmart.business_model.001
    confidence: high
    review_status: accepted
    notes: Estimated seller payout from Walmart report calculated as product revenue excluding tax plus gross_commission;
      do not use settled_amount.
```

```yaml
candidate_card:
  card_type: metric
  card_id: metric.marketplace.seller_realization_rate
  name: Seller realization rate
  fields:
    metric_key: seller_realization_rate
    business_definition: Percentage of excluding-tax product revenue retained after Walmart referral fee deductions.
    colloquial_names:
    - realization rate
    - net realization
    - payout percentage
    metric_pattern: net_payout_over_product_revenue_excluding_tax
    default_grain: payout_cycle
    domain: domain.marketplace.walmart.settlement
    scope: generic marketplace metric implemented by Walmart-specific metric_implementation cards
    benchmarks:
      context: Derived Walmart realization using computed net seller payout, not settled_amount
    evidence_refs:
    - ev.walmart.metrics.001
    confidence: high
    review_status: accepted
    notes: Percentage of excluding-tax product revenue retained after Walmart referral fee deductions.
```

```yaml
candidate_card:
  card_type: metric
  card_id: metric.marketplace.effective_commission_rate
  name: Effective commission rate
  fields:
    metric_key: effective_commission_rate
    business_definition: Absolute Walmart referral fee divided by charged_amount_excluding_tax.
    colloquial_names:
    - commission rate
    - referral fee rate
    - take rate
    metric_pattern: abs_gross_commission_over_excluding_tax_revenue
    default_grain: product_type
    domain: domain.marketplace.walmart.fees
    scope: generic marketplace metric implemented by Walmart-specific metric_implementation cards
    benchmarks:
      observed_context: ~13.46 percent of taxable/product revenue; guidance only, not hard universal threshold
    evidence_refs:
    - ev.walmart.business_model.001
    confidence: high
    review_status: accepted
    notes: Absolute Walmart referral fee divided by charged_amount_excluding_tax.
```

```yaml
candidate_card:
  card_type: metric
  card_id: metric.marketplace.return_rate
  name: Return / refund rate
  fields:
    metric_key: return_rate
    business_definition: Reverse settlement rows divided by forward settlement rows.
    colloquial_names:
    - refund rate
    - return percentage
    - refund percentage
    metric_pattern: reverse_count_over_forward_count
    default_grain: settlement_period
    domain: domain.marketplace.walmart.returns
    scope: generic marketplace metric implemented by Walmart-specific metric_implementation cards
    benchmarks:
      observed_context: 20 refunds / 1,011 forward = 2.0 percent; source guidance only
    evidence_refs:
    - ev.walmart.metrics.001
    confidence: high
    review_status: accepted
    notes: Reverse settlement rows divided by forward settlement rows.
```

```yaml
candidate_card:
  card_type: metric
  card_id: metric.marketplace.average_order_value
  name: Average order value
  fields:
    metric_key: average_order_value
    business_definition: Average charged_amount for delivered Walmart OMS sales rows.
    colloquial_names:
    - AOV
    - avg price
    - average sale value
    metric_pattern: avg_charged_amount_delivered_sales
    default_grain: order
    domain: domain.marketplace.walmart.orders
    scope: generic marketplace metric implemented by Walmart-specific metric_implementation cards
    benchmarks:
      observed_context: ~$17.47 AOV; source guidance only
    evidence_refs:
    - ev.walmart.metrics.001
    confidence: high
    review_status: accepted
    notes: Average charged_amount for delivered Walmart OMS sales rows.
```

```yaml
candidate_card:
  card_type: metric
  card_id: metric.marketplace.cancellation_rate
  name: Cancellation rate
  fields:
    metric_key: cancellation_rate
    business_definition: Cancelled Walmart OMS orders divided by all active OMS rows.
    colloquial_names:
    - cancel rate
    - cancel percentage
    metric_pattern: cancel_count_over_total_active_orders
    default_grain: order
    domain: domain.marketplace.walmart.orders
    scope: generic marketplace metric implemented by Walmart-specific metric_implementation cards
    benchmarks:
      observed_context: 37/972 = 3.8 percent; source guidance only
    evidence_refs:
    - ev.walmart_oms.schema.001
    confidence: high
    review_status: accepted
    notes: Cancelled Walmart OMS orders divided by all active OMS rows.
```

```yaml
candidate_card:
  card_type: metric
  card_id: metric.marketplace.tax_withheld
  name: Marketplace facilitator tax withheld
  fields:
    metric_key: tax_withheld
    business_definition: US sales tax collected from buyers and withheld/remitted by Walmart; not seller revenue.
    colloquial_names:
    - MPF tax
    - sales tax withheld
    - marketplace withheld tax
    metric_pattern: sum_total_tax_or_abs_marketplace_withheld_tax
    default_grain: month
    domain: domain.marketplace.walmart.tax
    scope: generic marketplace metric implemented by Walmart-specific metric_implementation cards
    evidence_refs:
    - ev.walmart.business_model.001
    confidence: high
    review_status: accepted
    notes: US sales tax collected from buyers and withheld/remitted by Walmart; not seller revenue.
```

```yaml
candidate_card:
  card_type: metric
  card_id: metric.marketplace.walmart_funded_savings
  name: Walmart-funded savings credit
  fields:
    metric_key: walmart_funded_savings
    business_definition: Walmart-funded promotional savings credit from settlement rows.
    colloquial_names:
    - Walmart savings
    - Walmart promo credit
    - funded savings
    metric_pattern: sum_total_walmart_funded_savings
    default_grain: month
    domain: domain.marketplace.walmart.settlement
    scope: generic marketplace metric implemented by Walmart-specific metric_implementation cards
    benchmarks:
      observed_context: $9.23 total in current source stats; rare/occasional
    evidence_refs:
    - ev.walmart.metrics.001
    confidence: high
    review_status: accepted
    notes: Walmart-funded promotional savings credit from settlement rows.
```

```yaml
candidate_card:
  card_type: metric
  card_id: metric.marketplace.sku_revenue
  name: SKU revenue
  fields:
    metric_key: sku_revenue
    business_definition: Revenue and net payout by Walmart SKU enriched from lookup.
    colloquial_names:
    - top SKUs
    - SKU sales
    - product revenue by SKU
    metric_pattern: group_forward_revenue_by_sku
    default_grain: sku
    domain: domain.marketplace.walmart.catalogue; domain.marketplace.walmart.settlement
    scope: generic marketplace metric implemented by Walmart-specific metric_implementation cards
    evidence_refs:
    - ev.walmart.metrics.001
    confidence: high
    review_status: accepted
    notes: Revenue and net payout by Walmart SKU enriched from lookup.
```

```yaml
candidate_card:
  card_type: metric
  card_id: metric.marketplace.revenue_by_state
  name: Revenue by US state
  fields:
    metric_key: revenue_by_state
    business_definition: Delivered OMS revenue by two-letter destination_state.
    colloquial_names:
    - state sales
    - US state distribution
    - geographic revenue
    metric_pattern: group_oms_delivered_sales_by_state
    default_grain: state
    domain: domain.marketplace.walmart.orders
    scope: generic marketplace metric implemented by Walmart-specific metric_implementation cards
    evidence_refs:
    - ev.walmart.metrics.001
    confidence: high
    review_status: accepted
    notes: Delivered OMS revenue by two-letter destination_state.
```

### 5.9 Walmart-Specific Metric Implementation Cards

```yaml
candidate_card:
  card_type: metric_implementation
  card_id: metric_implementation.walmart.walmart_settlement.gross_revenue
  name: 'Walmart settlement implementation: gross_revenue'
  fields:
    implements_metric: metric.marketplace.gross_revenue
    platform_context: platform_context.walmart.us
    source_tables: table.zs_observe.walmart_settlement
    formula: SUM(charged_amount) where transaction_type = forward
    required_filters: is_active = true AND group_level_id = 22 AND transaction_type = 'forward'
    grain: settlement_period
    sql_ref: sql.walmart.settlement.forward_gmv_net_payout
    metric_pattern: sum_charged_amount_forward
    notes: Walmart-specific executable implementation; runtime scope can be supplied externally but documented group_level_id=22
      is preserved as source scope metadata.
    evidence_refs:
    - ev.walmart.metrics.001
    confidence: high
    review_status: accepted
```

```yaml
candidate_card:
  card_type: metric_implementation
  card_id: metric_implementation.walmart.walmart_settlement.product_revenue_excluding_tax
  name: 'Walmart settlement implementation: product_revenue_excluding_tax'
  fields:
    implements_metric: metric.marketplace.product_revenue_excluding_tax
    platform_context: platform_context.walmart.us
    source_tables: table.zs_observe.walmart_settlement
    formula: SUM(charged_amount_excluding_tax) where transaction_type = forward
    required_filters: is_active = true AND group_level_id = 22 AND transaction_type = 'forward'
    grain: settlement_period
    sql_ref: sql.walmart.settlement.forward_gmv_net_payout
    metric_pattern: sum_excluding_tax_forward
    notes: Walmart-specific executable implementation; runtime scope can be supplied externally but documented group_level_id=22
      is preserved as source scope metadata.
    evidence_refs:
    - ev.walmart.metrics.001
    confidence: high
    review_status: accepted
```

```yaml
candidate_card:
  card_type: metric_implementation
  card_id: metric_implementation.walmart.walmart_settlement.net_seller_payout
  name: 'Walmart settlement implementation: net_seller_payout'
  fields:
    implements_metric: metric.marketplace.net_seller_payout
    platform_context: platform_context.walmart.us
    source_tables: table.zs_observe.walmart_settlement
    formula: SUM(charged_amount_excluding_tax + gross_commission); settled_amount is ignored because it is always zero
    required_filters: is_active = true AND group_level_id = 22
    grain: payout_cycle
    sql_ref: sql.walmart.settlement.payout_cycle_summary
    metric_pattern: sum_product_revenue_plus_commission
    notes: Walmart-specific executable implementation; runtime scope can be supplied externally but documented group_level_id=22
      is preserved as source scope metadata.
    evidence_refs:
    - ev.walmart.business_model.001
    confidence: high
    review_status: accepted
```

```yaml
candidate_card:
  card_type: metric_implementation
  card_id: metric_implementation.walmart.walmart_settlement.seller_realization_rate
  name: 'Walmart settlement implementation: seller_realization_rate'
  fields:
    implements_metric: metric.marketplace.seller_realization_rate
    platform_context: platform_context.walmart.us
    source_tables: table.zs_observe.walmart_settlement
    formula: SUM(charged_amount_excluding_tax + gross_commission) / NULLIF(SUM(charged_amount_excluding_tax), 0)
    required_filters: is_active = true AND group_level_id = 22 AND transaction_type = 'forward'
    grain: payout_cycle
    sql_ref: sql.walmart.settlement.forward_gmv_net_payout
    metric_pattern: net_payout_over_product_revenue_ex_tax
    notes: Walmart-specific executable implementation; runtime scope can be supplied externally but documented group_level_id=22
      is preserved as source scope metadata.
    evidence_refs:
    - ev.walmart.metrics.001
    confidence: high
    review_status: accepted
```

```yaml
candidate_card:
  card_type: metric_implementation
  card_id: metric_implementation.walmart.walmart_settlement.effective_commission_rate
  name: 'Walmart settlement implementation: effective_commission_rate'
  fields:
    implements_metric: metric.marketplace.effective_commission_rate
    platform_context: platform_context.walmart.us
    source_tables: table.zs_observe.walmart_settlement
    formula: ABS(SUM(gross_commission)) / NULLIF(SUM(charged_amount_excluding_tax), 0)
    required_filters: is_active = true AND group_level_id = 22 AND transaction_type = 'forward'
    grain: product_type
    sql_ref: sql.walmart.reconciliation.commission_validation
    metric_pattern: abs_commission_over_product_revenue
    notes: Walmart-specific executable implementation; runtime scope can be supplied externally but documented group_level_id=22
      is preserved as source scope metadata.
    evidence_refs:
    - ev.walmart.reconciliation.001
    confidence: high
    review_status: accepted
```

```yaml
candidate_card:
  card_type: metric_implementation
  card_id: metric_implementation.walmart.walmart_settlement.return_rate
  name: 'Walmart settlement implementation: return_rate'
  fields:
    implements_metric: metric.marketplace.return_rate
    platform_context: platform_context.walmart.us
    source_tables: table.zs_observe.walmart_settlement
    formula: COUNT_IF(transaction_type = reverse) / NULLIF(COUNT_IF(transaction_type = forward), 0)
    required_filters: is_active = true AND group_level_id = 22
    grain: settlement_period
    sql_ref: sql.walmart.settlement.return_rate
    metric_pattern: reverse_count_over_forward_count
    notes: Walmart-specific executable implementation; runtime scope can be supplied externally but documented group_level_id=22
      is preserved as source scope metadata.
    evidence_refs:
    - ev.walmart.metrics.001
    confidence: high
    review_status: accepted
```

```yaml
candidate_card:
  card_type: metric_implementation
  card_id: metric_implementation.walmart.walmart_oms.average_order_value
  name: 'Walmart OMS implementation: average_order_value'
  fields:
    implements_metric: metric.marketplace.average_order_value
    platform_context: platform_context.walmart.us
    source_tables: table.zs_observe.walmart_oms
    formula: AVG(charged_amount) for delivered sales rows
    required_filters: is_active = true AND group_level_id = 22 AND order_status = 'DELIVERED' AND internal_txn_type = 'sales'
    grain: order
    sql_ref: sql.walmart.oms.aov
    metric_pattern: avg_charged_amount_delivered_sales
    notes: Walmart-specific executable implementation; runtime scope can be supplied externally but documented group_level_id=22
      is preserved as source scope metadata.
    evidence_refs:
    - ev.walmart.metrics.001
    confidence: high
    review_status: accepted
```

```yaml
candidate_card:
  card_type: metric_implementation
  card_id: metric_implementation.walmart.walmart_oms.cancellation_rate
  name: 'Walmart OMS implementation: cancellation_rate'
  fields:
    implements_metric: metric.marketplace.cancellation_rate
    platform_context: platform_context.walmart.us
    source_tables: table.zs_observe.walmart_oms
    formula: COUNT_IF(order_status = CANCELLED) / COUNT(*)
    required_filters: is_active = true AND group_level_id = 22
    grain: order
    sql_ref: sql.walmart.oms.cancellation_rate
    metric_pattern: cancel_count_over_total_active_orders
    notes: Walmart-specific executable implementation; runtime scope can be supplied externally but documented group_level_id=22
      is preserved as source scope metadata.
    evidence_refs:
    - ev.walmart_oms.schema.001
    confidence: high
    review_status: accepted
```

```yaml
candidate_card:
  card_type: metric_implementation
  card_id: metric_implementation.walmart.walmart_settlement.tax_withheld
  name: 'Walmart settlement implementation: tax_withheld'
  fields:
    implements_metric: metric.marketplace.tax_withheld
    platform_context: platform_context.walmart.us
    source_tables: table.zs_observe.walmart_settlement
    formula: SUM(total_tax) for forward rows or ABS(SUM(marketplace_withheld_tax)) where sign context is needed
    required_filters: is_active = true AND group_level_id = 22 AND transaction_type = 'forward'
    grain: settlement_period
    sql_ref: sql.walmart.validation.mpf_tax_identity
    metric_pattern: sum_total_tax_mpf
    notes: Walmart-specific executable implementation; runtime scope can be supplied externally but documented group_level_id=22
      is preserved as source scope metadata.
    evidence_refs:
    - ev.walmart.business_model.001
    confidence: high
    review_status: accepted
```

```yaml
candidate_card:
  card_type: metric_implementation
  card_id: metric_implementation.walmart.walmart_settlement.walmart_funded_savings
  name: 'Walmart settlement implementation: walmart_funded_savings'
  fields:
    implements_metric: metric.marketplace.walmart_funded_savings
    platform_context: platform_context.walmart.us
    source_tables: table.zs_observe.walmart_settlement
    formula: SUM(total_walmart_funded_savings)
    required_filters: is_active = true AND group_level_id = 22
    grain: settlement_period
    sql_ref: sql.walmart.settlement.forward_gmv_net_payout
    metric_pattern: sum_walmart_funded_savings
    notes: Walmart-specific executable implementation; runtime scope can be supplied externally but documented group_level_id=22
      is preserved as source scope metadata.
    evidence_refs:
    - ev.walmart.metrics.001
    confidence: high
    review_status: accepted
```

```yaml
candidate_card:
  card_type: metric_implementation
  card_id: metric_implementation.walmart.walmart_settlement.sku_revenue
  name: 'Walmart settlement implementation: sku_revenue'
  fields:
    implements_metric: metric.marketplace.sku_revenue
    platform_context: platform_context.walmart.us
    source_tables: table.zs_observe.walmart_settlement; table.zs_observe.walmart_lookup
    formula: SUM(charged_amount_excluding_tax) grouped by sku_id and lookup.item_name
    required_filters: settlement.is_active = true AND settlement.transaction_type = 'forward'; lookup.sku IS NOT NULL
    grain: sku
    sql_ref: sql.walmart.settlement.top_skus
    metric_pattern: group_forward_revenue_by_sku
    notes: Walmart-specific executable implementation; runtime scope can be supplied externally but documented group_level_id=22
      is preserved as source scope metadata.
    evidence_refs:
    - ev.walmart.metrics.001
    confidence: high
    review_status: accepted
```

```yaml
candidate_card:
  card_type: metric_implementation
  card_id: metric_implementation.walmart.walmart_oms.revenue_by_state
  name: 'Walmart OMS implementation: revenue_by_state'
  fields:
    implements_metric: metric.marketplace.revenue_by_state
    platform_context: platform_context.walmart.us
    source_tables: table.zs_observe.walmart_oms
    formula: SUM(charged_amount) grouped by destination_state for delivered clean rows
    required_filters: is_active = true AND group_level_id = 22 AND order_status = 'DELIVERED' AND LENGTH(destination_state)=2
    grain: state
    sql_ref: sql.walmart.oms.state_distribution
    metric_pattern: group_oms_delivered_sales_by_state
    notes: Walmart-specific executable implementation; runtime scope can be supplied externally but documented group_level_id=22
      is preserved as source scope metadata.
    evidence_refs:
    - ev.walmart.metrics.001
    confidence: high
    review_status: accepted
```

### 5.10 Formula Template Cards

```yaml
candidate_card:
  card_type: formula_template
  card_id: formula_template.walmart.net_seller_payout
  name: Walmart net seller payout formula
  fields:
    formula_key: net_seller_payout
    formula: Net Seller Payout = charged_amount_excluding_tax + gross_commission
    sign_semantics: gross_commission is negative for forward rows; marketplace_withheld_tax is not seller revenue; settled_amount
      is zero and ignored
    applicable_tables:
    - table.zs_observe.walmart_settlement
    scope: marketplace_semantic_formula
    evidence_refs:
    - ev.walmart.business_model.001
    confidence: high
    review_status: accepted
    notes: Walmart net seller payout formula
```

```yaml
candidate_card:
  card_type: formula_template
  card_id: formula_template.walmart.mpf_tax_identity
  name: Walmart MPF tax identity
  fields:
    formula_key: mpf_tax_identity
    formula: charged_amount = charged_amount_excluding_tax + total_tax; marketplace_withheld_tax mirrors tax withheld with
      sign context
    sign_semantics: Use total_tax for buyer tax collected and marketplace_withheld_tax for withheld settlement sign semantics
    applicable_tables:
    - table.zs_observe.walmart_settlement
    scope: marketplace_semantic_formula
    evidence_refs:
    - ev.walmart.business_model.001
    confidence: high
    review_status: accepted
    notes: Walmart MPF tax identity
```

```yaml
candidate_card:
  card_type: formula_template
  card_id: formula_template.walmart.effective_commission_rate
  name: Walmart effective commission rate formula
  fields:
    formula_key: effective_commission_rate
    formula: ABS(SUM(gross_commission)) / SUM(charged_amount_excluding_tax)
    sign_semantics: Use calculated formula because commission_rate/base_commission_rate columns are NULL/not published
    applicable_tables:
    - table.zs_observe.walmart_settlement
    scope: marketplace_semantic_formula
    evidence_refs:
    - ev.walmart.quality.001
    confidence: high
    review_status: accepted
    notes: Walmart effective commission rate formula
```

```yaml
candidate_card:
  card_type: formula_template
  card_id: formula_template.walmart.refund_reversal
  name: Walmart refund reversal formula
  fields:
    formula_key: refund_reversal
    formula: Refund rows have negative charged_amount, positive gross_commission, and positive marketplace_withheld_tax
    sign_semantics: Match reverse rows to original forward rows by order_id and sku_id when available
    applicable_tables:
    - table.zs_observe.walmart_settlement
    scope: marketplace_semantic_formula
    evidence_refs:
    - ev.walmart.lifecycle.001
    confidence: high
    review_status: accepted
    notes: Walmart refund reversal formula
```

### 5.11 Metric Dependency Cards

```yaml
candidate_card:
  card_type: metric_dependency
  card_id: metric_dependency.walmart.seller_realization.net_seller_payout_numerator
  name: Seller realization rate depends on net seller payout numerator
  fields:
    metric_id: metric.marketplace.seller_realization_rate
    depends_on: metric.marketplace.net_seller_payout
    dependency_type: numerator
    aggregation_order: compute net seller payout before seller realization rate
    required_before_computation: true
    evidence_refs:
    - ev.walmart.metrics.001
    - ev.walmart.business_model.001
    confidence: high
    review_status: accepted
    notes: Seller realization must use computed Walmart payout, not settled_amount.
```

```yaml
candidate_card:
  card_type: metric_dependency
  card_id: metric_dependency.walmart.seller_realization.product_revenue_denominator
  name: Seller realization rate depends on product revenue denominator
  fields:
    metric_id: metric.marketplace.seller_realization_rate
    depends_on: metric.marketplace.product_revenue_excluding_tax
    dependency_type: denominator
    aggregation_order: aggregate product revenue excluding tax at the same grain before dividing
    required_before_computation: true
    evidence_refs:
    - ev.walmart.metrics.001
    confidence: high
    review_status: accepted
    notes: Use charged_amount_excluding_tax, because MPF tax is not seller revenue.
```

```yaml
candidate_card:
  card_type: metric_dependency
  card_id: metric_dependency.walmart.net_seller_payout.product_revenue_component
  name: Net seller payout depends on product revenue excluding tax
  fields:
    metric_id: metric.marketplace.net_seller_payout
    depends_on: metric.marketplace.product_revenue_excluding_tax
    dependency_type: base_component
    aggregation_order: sum product revenue excluding tax before adding signed commission deduction
    required_before_computation: true
    evidence_refs:
    - ev.walmart.business_model.001
    confidence: high
    review_status: accepted
    notes: Net seller payout is charged_amount_excluding_tax + gross_commission.
```

```yaml
candidate_card:
  card_type: metric_dependency
  card_id: metric_dependency.walmart.average_order_value.gross_revenue_component
  name: Average order value depends on gross revenue
  fields:
    metric_id: metric.marketplace.average_order_value
    depends_on: metric.marketplace.gross_revenue
    dependency_type: numerator_context
    aggregation_order: aggregate GMV and distinct orders at the same order grain before averaging
    required_before_computation: true
    evidence_refs:
    - ev.walmart.metrics.001
    confidence: high
    review_status: accepted
    notes: AOV is an order-grain average over forward/delivered sales context.
```

### 5.12 Business Process Cards

```yaml
candidate_card:
  card_type: business_process
  card_id: business_process.walmart.forward_wfs_sale_to_payout
  name: Walmart forward WFS sale to estimated payout
  fields:
    process_key: forward_wfs_sale_to_payout
    process_description: Forward Walmart.com order appears in OMS, moves through WFS delivery, settles as forward sale in
      walmart_settlement, and contributes to computed net seller payout using charged_amount_excluding_tax plus gross_commission.
    platform_context: platform_context.walmart.us
    process_scope: marketplace_semantic_process
    evidence_refs:
    - ev.walmart.lifecycle.001
    confidence: high
    review_status: accepted
    notes: Walmart forward WFS sale to estimated payout
```

```yaml
candidate_card:
  card_type: business_process
  card_id: business_process.walmart.refund_to_payout_deduction
  name: Walmart refund to next payout deduction
  fields:
    process_key: refund_to_payout_deduction
    process_description: Customer return handled by WFS creates reverse/refund settlement row with negative charged_amount,
      positive commission reversal, positive tax reversal, and deduction from seller payout.
    platform_context: platform_context.walmart.us
    process_scope: marketplace_semantic_process
    evidence_refs:
    - ev.walmart.lifecycle.001
    confidence: high
    review_status: accepted
    notes: Walmart refund to next payout deduction
```

```yaml
candidate_card:
  card_type: business_process
  card_id: business_process.walmart.cancellation_without_settlement
  name: Walmart cancellation without settlement
  fields:
    process_key: cancellation_without_settlement
    process_description: Cancelled orders appear in walmart_oms with order_status = CANCELLED and are not expected to create
      settlement rows.
    platform_context: platform_context.walmart.us
    process_scope: marketplace_semantic_process
    evidence_refs:
    - ev.walmart.lifecycle.001
    confidence: high
    review_status: accepted
    notes: Walmart cancellation without settlement
```

```yaml
candidate_card:
  card_type: business_process
  card_id: business_process.walmart.catalogue_enrichment
  name: Walmart product catalogue enrichment
  fields:
    process_key: catalogue_enrichment
    process_description: walmart_lookup supplies clean item_name enrichment for OMS and settlement via sku_id = sku with sku
      IS NOT NULL.
    platform_context: platform_context.walmart.us
    process_scope: marketplace_semantic_process
    evidence_refs:
    - ev.walmart_lookup.schema.001
    confidence: high
    review_status: accepted
    notes: Walmart product catalogue enrichment
```

### 5.13 Workflow Step Cards

```yaml
candidate_card:
  card_type: workflow_step
  card_id: workflow_step.walmart.forward.order_created_in_oms
  name: OMS forward order captured
  fields:
    process: business_process.walmart.forward_wfs_sale_to_payout
    step_description: walmart_oms captures the line-item order with order_id, sku_id, charged_amount, created_date, order_status
      and internal_txn_type = sales for delivered rows.
    related_canonical_id: table.zs_observe.walmart_oms
    step_order: 1
    evidence_refs:
    - ev.walmart.lifecycle.001
    confidence: high
    review_status: accepted
    notes: OMS forward order captured
```

```yaml
candidate_card:
  card_type: workflow_step
  card_id: workflow_step.walmart.forward.wfs_fulfilment
  name: WFS fulfilment context applied
  fields:
    process: business_process.walmart.forward_wfs_sale_to_payout
    step_description: WFS fulfilment_channel = Walmart-fulfilledWFS means Walmart stores, picks, packs, ships, and handles
      returns; this is marketplace context, not an external logistics process card.
    related_canonical_id: column.zs_observe.walmart_settlement.fulfilment_channel
    step_order: 2
    evidence_refs:
    - ev.walmart.business_model.001
    confidence: high
    review_status: accepted
    notes: WFS fulfilment context applied
```

```yaml
candidate_card:
  card_type: workflow_step
  card_id: workflow_step.walmart.forward.delivered_sales_filter
  name: Delivered OMS sale isolated
  fields:
    process: business_process.walmart.forward_wfs_sale_to_payout
    step_description: Completed OMS sales use order_status = DELIVERED and internal_txn_type = sales before comparing against
      settlement.
    related_canonical_id: column.zs_observe.walmart_oms.order_status
    step_order: 3
    evidence_refs:
    - ev.walmart.filters.001
    confidence: high
    review_status: accepted
    notes: Delivered OMS sale isolated
```

```yaml
candidate_card:
  card_type: workflow_step
  card_id: workflow_step.walmart.forward.forward_settlement_row
  name: Forward settlement row recorded
  fields:
    process: business_process.walmart.forward_wfs_sale_to_payout
    step_description: walmart_settlement transaction_type = forward / other_type = Sale stores charged_amount, charged_amount_excluding_tax,
      total_tax, gross_commission, and marketplace_withheld_tax.
    related_canonical_id: table.zs_observe.walmart_settlement
    step_order: 4
    evidence_refs:
    - ev.walmart.lifecycle.001
    confidence: high
    review_status: accepted
    notes: Forward settlement row recorded
```

```yaml
candidate_card:
  card_type: workflow_step
  card_id: workflow_step.walmart.forward.net_payout_computed
  name: Computed payout from settlement fields
  fields:
    process: business_process.walmart.forward_wfs_sale_to_payout
    step_description: Because settled_amount = 0, compute net seller payout as charged_amount_excluding_tax + gross_commission
      and use metadata_3 as payout date.
    related_canonical_id: formula_template.walmart.net_seller_payout
    step_order: 5
    evidence_refs:
    - ev.walmart.business_model.001
    confidence: high
    review_status: accepted
    notes: Computed payout from settlement fields
```

```yaml
candidate_card:
  card_type: workflow_step
  card_id: workflow_step.walmart.refund.wfs_return_triggered
  name: WFS return/refund triggered
  fields:
    process: business_process.walmart.refund_to_payout_deduction
    step_description: Customer return is handled by Walmart WFS; seller does not directly manage return logistics in this
      source.
    related_canonical_id: platform_context.walmart.us
    step_order: 1
    evidence_refs:
    - ev.walmart.lifecycle.001
    confidence: high
    review_status: accepted
    notes: WFS return/refund triggered
```

```yaml
candidate_card:
  card_type: workflow_step
  card_id: workflow_step.walmart.refund.reverse_settlement_row
  name: Reverse settlement refund row recorded
  fields:
    process: business_process.walmart.refund_to_payout_deduction
    step_description: walmart_settlement transaction_type = reverse / other_type = Refund records negative charged_amount,
      positive gross_commission, and positive marketplace_withheld_tax.
    related_canonical_id: column.zs_observe.walmart_settlement.transaction_type
    step_order: 2
    evidence_refs:
    - ev.walmart.lifecycle.001
    confidence: high
    review_status: accepted
    notes: Reverse settlement refund row recorded
```

```yaml
candidate_card:
  card_type: workflow_step
  card_id: workflow_step.walmart.refund.next_payout_deduction
  name: Refund deducts next payout
  fields:
    process: business_process.walmart.refund_to_payout_deduction
    step_description: Refund rows are deducted from the seller next payout cycle; they should be matched to original sale
      by order_id and sku_id where possible.
    related_canonical_id: reconciliation_profile.walmart.refund_to_sale
    step_order: 3
    evidence_refs:
    - ev.walmart.lifecycle.001
    confidence: high
    review_status: accepted
    notes: Refund deducts next payout
```

```yaml
candidate_card:
  card_type: workflow_step
  card_id: workflow_step.walmart.cancel.cancelled_in_oms
  name: Cancellation retained in OMS only
  fields:
    process: business_process.walmart.cancellation_without_settlement
    step_description: walmart_oms order_status = CANCELLED identifies orders cancelled before shipping; these should not be
      forced into settlement matching.
    related_canonical_id: column.zs_observe.walmart_oms.order_status
    step_order: 1
    evidence_refs:
    - ev.walmart.lifecycle.001
    confidence: high
    review_status: accepted
    notes: Cancellation retained in OMS only
```

```yaml
candidate_card:
  card_type: workflow_step
  card_id: workflow_step.walmart.catalogue.filter_usable_sku_rows
  name: Filter lookup to usable SKU rows
  fields:
    process: business_process.walmart.catalogue_enrichment
    step_description: walmart_lookup rows must satisfy sku IS NOT NULL before joining to OMS or settlement for product names.
    related_canonical_id: column.zs_observe.walmart_lookup.sku
    step_order: 1
    evidence_refs:
    - ev.walmart_lookup.schema.001
    confidence: high
    review_status: accepted
    notes: Filter lookup to usable SKU rows
```

```yaml
candidate_card:
  card_type: workflow_step
  card_id: workflow_step.walmart.catalogue.enrich_oms_settlement
  name: Enrich OMS and settlement products
  fields:
    process: business_process.walmart.catalogue_enrichment
    step_description: Join o.sku_id = l.sku or s.sku_id = l.sku to attach lookup.item_name to financial/order analysis.
    related_canonical_id: relationship.walmart.oms_to_lookup_sku
    step_order: 2
    evidence_refs:
    - ev.walmart.relationships.001
    confidence: high
    review_status: accepted
    notes: Enrich OMS and settlement products
```

### 5.14 State Transition Cards

```yaml
candidate_card:
  card_type: state_transition
  card_id: state_transition.walmart.oms_acknowledged_to_shipped
  name: OMS acknowledged to shipped
  fields:
    state_column: column.zs_observe.walmart_oms.order_status
    from_state: ACKNOWLEDGED
    to_state: SHIPPED
    transition_semantics: Order accepted and moved into shipment; operational state exists in OMS order_status.
    process: business_process.walmart.forward_wfs_sale_to_payout
    evidence_refs:
    - ev.walmart.lifecycle.001
    confidence: high
    review_status: accepted
    notes: OMS acknowledged to shipped
```

```yaml
candidate_card:
  card_type: state_transition
  card_id: state_transition.walmart.oms_shipped_to_delivered
  name: OMS shipped to delivered
  fields:
    state_column: column.zs_observe.walmart_oms.order_status
    from_state: SHIPPED
    to_state: DELIVERED
    transition_semantics: Delivered status marks completed OMS sale and eligible reconciliation side.
    process: business_process.walmart.forward_wfs_sale_to_payout
    evidence_refs:
    - ev.walmart.lifecycle.001
    confidence: high
    review_status: accepted
    notes: OMS shipped to delivered
```

```yaml
candidate_card:
  card_type: state_transition
  card_id: state_transition.walmart.oms_to_cancelled
  name: OMS order to cancelled
  fields:
    state_column: column.zs_observe.walmart_oms.order_status
    from_state: ACKNOWLEDGED/SHIPPED
    to_state: CANCELLED
    transition_semantics: Cancelled orders appear in OMS and are not expected in settlement.
    process: business_process.walmart.cancellation_without_settlement
    evidence_refs:
    - ev.walmart.lifecycle.001
    confidence: high
    review_status: accepted
    notes: OMS order to cancelled
```

```yaml
candidate_card:
  card_type: state_transition
  card_id: state_transition.walmart.settlement_sale_to_refund
  name: Settlement sale to refund classification
  fields:
    state_column: column.zs_observe.walmart_settlement.transaction_type
    from_state: forward
    to_state: reverse
    transition_semantics: Refund rows are represented as reverse transaction_type with negative charged_amount and positive
      fee/tax reversals.
    process: business_process.walmart.refund_to_payout_deduction
    evidence_refs:
    - ev.walmart.lifecycle.001
    confidence: high
    review_status: accepted
    notes: Settlement sale to refund classification
```

### 5.15 Process Variant Cards

No `process_variant` candidate cards are emitted in V3. WFS, product category, product type, currency, state, and group-level scope are represented as platform context, value profiles, rules, or execution constraints unless a source documents a materially different process sequence or matching logic.

### 5.16 Marketplace-Internal Reconciliation Profile Cards

```yaml
candidate_card:
  card_type: reconciliation_profile
  card_id: reconciliation_profile.walmart.oms_to_settlement
  name: Walmart OMS to settlement reconciliation
  fields:
    profile_key: oms_to_settlement
    expected_side: walmart_oms delivered sales
    actual_side: walmart_settlement forward sale rows
    unit: order_id + SKU line-item; amount check on charged_amount
    description: OMS delivered sale should have corresponding settlement forward row; known coverage 89.6% due timing/cancellations/historical
      rows
    reconciliation_scope: marketplace_internal
    evidence_refs:
    - ev.walmart.reconciliation.001
    confidence: high
    review_status: accepted
    notes: Walmart OMS to settlement reconciliation
```

```yaml
candidate_card:
  card_type: reconciliation_profile
  card_id: reconciliation_profile.walmart.commission_validation
  name: Walmart commission validation
  fields:
    profile_key: commission_validation
    expected_side: charged_amount_excluding_tax x observed rate baseline
    actual_side: gross_commission charged by Walmart
    unit: settlement order/SKU row
    description: Validate commission rate from amounts because source rate columns are NULL; 13.46% is guidance/observed baseline
    reconciliation_scope: marketplace_internal
    evidence_refs:
    - ev.walmart.reconciliation.001
    confidence: high
    review_status: accepted
    notes: Walmart commission validation
```

```yaml
candidate_card:
  card_type: reconciliation_profile
  card_id: reconciliation_profile.walmart.refund_to_sale
  name: Walmart refund to original sale match
  fields:
    profile_key: refund_to_sale
    expected_side: walmart_settlement forward sale rows
    actual_side: walmart_settlement reverse refund rows
    unit: order_id + sku_id
    description: Match reverse refund amount and commission reversal to original forward sale where possible
    reconciliation_scope: marketplace_internal
    evidence_refs:
    - ev.walmart.reconciliation.001
    confidence: high
    review_status: accepted
    notes: Walmart refund to original sale match
```

```yaml
candidate_card:
  card_type: reconciliation_profile
  card_id: reconciliation_profile.walmart.mpf_tax_identity
  name: Walmart marketplace facilitator tax identity
  fields:
    profile_key: mpf_tax_identity
    expected_side: charged_amount_excluding_tax + total_tax
    actual_side: charged_amount and marketplace_withheld_tax sign context
    unit: settlement row
    description: Validate MPF tax identity; sales tax is withheld/remitted by Walmart and excluded from seller revenue
    reconciliation_scope: marketplace_internal
    evidence_refs:
    - ev.walmart.business_model.001
    confidence: high
    review_status: accepted
    notes: Walmart marketplace facilitator tax identity
```

```yaml
candidate_card:
  card_type: reconciliation_profile
  card_id: reconciliation_profile.walmart.lookup_coverage
  name: Walmart lookup enrichment coverage
  fields:
    profile_key: lookup_coverage
    expected_side: OMS/settlement SKU population
    actual_side: walmart_lookup sku-populated catalogue rows
    unit: sku_id = sku
    description: Validate product-name enrichment coverage and exclude sku-null content rows
    reconciliation_scope: marketplace_internal
    evidence_refs:
    - ev.walmart.relationships.001
    confidence: high
    review_status: accepted
    notes: Walmart lookup enrichment coverage
```

### 5.17 Reconciliation Side Cards

```yaml
candidate_card:
  card_type: reconciliation_side
  card_id: reconciliation_side.walmart.oms_to_settlement.expected
  name: Walmart OMS to settlement reconciliation expected side
  fields:
    profile: reconciliation_profile.walmart.oms_to_settlement
    side_role: expected
    business_role: walmart_oms delivered sales
    source_table: table.zs_observe.walmart_oms
    evidence_refs:
    - ev.walmart.reconciliation.001
    confidence: high
    review_status: accepted
    notes: Walmart OMS to settlement reconciliation expected side
```

```yaml
candidate_card:
  card_type: reconciliation_side
  card_id: reconciliation_side.walmart.oms_to_settlement.actual
  name: Walmart OMS to settlement reconciliation actual side
  fields:
    profile: reconciliation_profile.walmart.oms_to_settlement
    side_role: actual
    business_role: walmart_settlement forward sale rows
    source_table: table.zs_observe.walmart_settlement
    evidence_refs:
    - ev.walmart.reconciliation.001
    confidence: high
    review_status: accepted
    notes: Walmart OMS to settlement reconciliation actual side
```

```yaml
candidate_card:
  card_type: reconciliation_side
  card_id: reconciliation_side.walmart.commission_validation.expected
  name: Walmart commission validation expected side
  fields:
    profile: reconciliation_profile.walmart.commission_validation
    side_role: expected
    business_role: charged_amount_excluding_tax x observed rate baseline
    source_table: table.zs_observe.walmart_settlement
    evidence_refs:
    - ev.walmart.reconciliation.001
    confidence: high
    review_status: accepted
    notes: Walmart commission validation expected side
```

```yaml
candidate_card:
  card_type: reconciliation_side
  card_id: reconciliation_side.walmart.commission_validation.actual
  name: Walmart commission validation actual side
  fields:
    profile: reconciliation_profile.walmart.commission_validation
    side_role: actual
    business_role: gross_commission charged by Walmart
    source_table: table.zs_observe.walmart_settlement
    evidence_refs:
    - ev.walmart.reconciliation.001
    confidence: high
    review_status: accepted
    notes: Walmart commission validation actual side
```

```yaml
candidate_card:
  card_type: reconciliation_side
  card_id: reconciliation_side.walmart.refund_to_sale.expected
  name: Walmart refund to original sale match expected side
  fields:
    profile: reconciliation_profile.walmart.refund_to_sale
    side_role: expected
    business_role: walmart_settlement forward sale rows
    source_table: table.zs_observe.walmart_settlement
    evidence_refs:
    - ev.walmart.reconciliation.001
    confidence: high
    review_status: accepted
    notes: Walmart refund to original sale match expected side
```

```yaml
candidate_card:
  card_type: reconciliation_side
  card_id: reconciliation_side.walmart.refund_to_sale.actual
  name: Walmart refund to original sale match actual side
  fields:
    profile: reconciliation_profile.walmart.refund_to_sale
    side_role: actual
    business_role: walmart_settlement reverse refund rows
    source_table: table.zs_observe.walmart_settlement
    evidence_refs:
    - ev.walmart.reconciliation.001
    confidence: high
    review_status: accepted
    notes: Walmart refund to original sale match actual side
```

```yaml
candidate_card:
  card_type: reconciliation_side
  card_id: reconciliation_side.walmart.mpf_tax_identity.expected
  name: Walmart marketplace facilitator tax identity expected side
  fields:
    profile: reconciliation_profile.walmart.mpf_tax_identity
    side_role: expected
    business_role: charged_amount_excluding_tax + total_tax
    source_table: table.zs_observe.walmart_settlement
    evidence_refs:
    - ev.walmart.business_model.001
    confidence: high
    review_status: accepted
    notes: Walmart marketplace facilitator tax identity expected side
```

```yaml
candidate_card:
  card_type: reconciliation_side
  card_id: reconciliation_side.walmart.mpf_tax_identity.actual
  name: Walmart marketplace facilitator tax identity actual side
  fields:
    profile: reconciliation_profile.walmart.mpf_tax_identity
    side_role: actual
    business_role: charged_amount and marketplace_withheld_tax sign context
    source_table: table.zs_observe.walmart_lookup
    evidence_refs:
    - ev.walmart.business_model.001
    confidence: high
    review_status: accepted
    notes: Walmart marketplace facilitator tax identity actual side
```

```yaml
candidate_card:
  card_type: reconciliation_side
  card_id: reconciliation_side.walmart.lookup_coverage.expected
  name: Walmart lookup enrichment coverage expected side
  fields:
    profile: reconciliation_profile.walmart.lookup_coverage
    side_role: expected
    business_role: OMS/settlement SKU population
    source_table: table.zs_observe.walmart_oms
    evidence_refs:
    - ev.walmart.relationships.001
    confidence: high
    review_status: accepted
    notes: Walmart lookup enrichment coverage expected side
```

```yaml
candidate_card:
  card_type: reconciliation_side
  card_id: reconciliation_side.walmart.lookup_coverage.actual
  name: Walmart lookup enrichment coverage actual side
  fields:
    profile: reconciliation_profile.walmart.lookup_coverage
    side_role: actual
    business_role: walmart_lookup sku-populated catalogue rows
    source_table: table.zs_observe.walmart_lookup
    evidence_refs:
    - ev.walmart.relationships.001
    confidence: high
    review_status: accepted
    notes: Walmart lookup enrichment coverage actual side
```

### 5.18 Reconciliation Unit Cards

```yaml
candidate_card:
  card_type: reconciliation_unit
  card_id: reconciliation_unit.walmart.oms_to_settlement
  name: Walmart OMS to settlement reconciliation unit
  fields:
    profile: reconciliation_profile.walmart.oms_to_settlement
    unit_key: order_id + SKU line-item; amount check on charged_amount
    grain: order_id + SKU line-item; amount check on charged_amount
    join_keys: order_id; sku_id where available; special logic per profile
    evidence_refs:
    - ev.walmart.reconciliation.001
    confidence: high
    review_status: accepted
    notes: Walmart OMS to settlement reconciliation unit
```

```yaml
candidate_card:
  card_type: reconciliation_unit
  card_id: reconciliation_unit.walmart.commission_validation
  name: Walmart commission validation unit
  fields:
    profile: reconciliation_profile.walmart.commission_validation
    unit_key: settlement order/SKU row
    grain: settlement order/SKU row
    join_keys: order_id; sku_id where available; special logic per profile
    evidence_refs:
    - ev.walmart.reconciliation.001
    confidence: high
    review_status: accepted
    notes: Walmart commission validation unit
```

```yaml
candidate_card:
  card_type: reconciliation_unit
  card_id: reconciliation_unit.walmart.refund_to_sale
  name: Walmart refund to original sale match unit
  fields:
    profile: reconciliation_profile.walmart.refund_to_sale
    unit_key: order_id + sku_id
    grain: order_id + sku_id
    join_keys: order_id; sku_id where available; special logic per profile
    evidence_refs:
    - ev.walmart.reconciliation.001
    confidence: high
    review_status: accepted
    notes: Walmart refund to original sale match unit
```

```yaml
candidate_card:
  card_type: reconciliation_unit
  card_id: reconciliation_unit.walmart.mpf_tax_identity
  name: Walmart marketplace facilitator tax identity unit
  fields:
    profile: reconciliation_profile.walmart.mpf_tax_identity
    unit_key: settlement row
    grain: settlement row
    join_keys: order_id; sku_id where available; special logic per profile
    evidence_refs:
    - ev.walmart.business_model.001
    confidence: high
    review_status: accepted
    notes: Walmart marketplace facilitator tax identity unit
```

```yaml
candidate_card:
  card_type: reconciliation_unit
  card_id: reconciliation_unit.walmart.lookup_coverage
  name: Walmart lookup enrichment coverage unit
  fields:
    profile: reconciliation_profile.walmart.lookup_coverage
    unit_key: sku_id = sku
    grain: sku_id = sku
    join_keys: order_id; sku_id where available; special logic per profile
    evidence_refs:
    - ev.walmart.relationships.001
    confidence: high
    review_status: accepted
    notes: Walmart lookup enrichment coverage unit
```

### 5.19 Matching Logic Cards

```yaml
candidate_card:
  card_type: matching_logic
  card_id: matching_logic.walmart.oms_to_settlement.primary
  name: Walmart OMS to settlement reconciliation matching logic
  fields:
    profile: reconciliation_profile.walmart.oms_to_settlement
    join_keys: order_id + SKU line-item; amount check on charged_amount
    matching_rule: OMS delivered sale should have corresponding settlement forward row; known coverage 89.6% due timing/cancellations/historical
      rows
    aggregation_rule: aggregate by documented grain before status classification
    sql_ref: sql.walmart.reconciliation.oms_settlement
    evidence_refs:
    - ev.walmart.reconciliation.001
    confidence: high
    review_status: accepted
    notes: Walmart OMS to settlement reconciliation matching logic
```

```yaml
candidate_card:
  card_type: matching_logic
  card_id: matching_logic.walmart.commission_validation.primary
  name: Walmart commission validation matching logic
  fields:
    profile: reconciliation_profile.walmart.commission_validation
    join_keys: settlement order/SKU row
    matching_rule: Validate commission rate from amounts because source rate columns are NULL; 13.46% is guidance/observed
      baseline
    aggregation_rule: aggregate by documented grain before status classification
    sql_ref: sql.walmart.reconciliation.commission_validation
    evidence_refs:
    - ev.walmart.reconciliation.001
    confidence: high
    review_status: accepted
    notes: Walmart commission validation matching logic
```

```yaml
candidate_card:
  card_type: matching_logic
  card_id: matching_logic.walmart.refund_to_sale.primary
  name: Walmart refund to original sale match matching logic
  fields:
    profile: reconciliation_profile.walmart.refund_to_sale
    join_keys: order_id + sku_id
    matching_rule: Match reverse refund amount and commission reversal to original forward sale where possible
    aggregation_rule: aggregate by documented grain before status classification
    sql_ref: sql.walmart.reconciliation.refund_sale_match
    evidence_refs:
    - ev.walmart.reconciliation.001
    confidence: high
    review_status: accepted
    notes: Walmart refund to original sale match matching logic
```

```yaml
candidate_card:
  card_type: matching_logic
  card_id: matching_logic.walmart.mpf_tax_identity.primary
  name: Walmart marketplace facilitator tax identity matching logic
  fields:
    profile: reconciliation_profile.walmart.mpf_tax_identity
    join_keys: settlement row
    matching_rule: Validate MPF tax identity; sales tax is withheld/remitted by Walmart and excluded from seller revenue
    aggregation_rule: aggregate by documented grain before status classification
    sql_ref: sql.walmart.validation.mpf_tax_identity
    evidence_refs:
    - ev.walmart.business_model.001
    confidence: high
    review_status: accepted
    notes: Walmart marketplace facilitator tax identity matching logic
```

```yaml
candidate_card:
  card_type: matching_logic
  card_id: matching_logic.walmart.lookup_coverage.primary
  name: Walmart lookup enrichment coverage matching logic
  fields:
    profile: reconciliation_profile.walmart.lookup_coverage
    join_keys: sku_id = sku
    matching_rule: Validate product-name enrichment coverage and exclude sku-null content rows
    aggregation_rule: aggregate by documented grain before status classification
    sql_ref: sql.walmart.validation.lookup_sku_null_monitor
    evidence_refs:
    - ev.walmart.relationships.001
    confidence: high
    review_status: accepted
    notes: Walmart lookup enrichment coverage matching logic
```

### 5.20 Mismatch Category Cards

```yaml
candidate_card:
  card_type: mismatch_category
  card_id: mismatch_category.walmart.oms_to_settlement.not_in_settlement
  name: Not in settlement
  fields:
    profile: reconciliation_profile.walmart.oms_to_settlement
    category_key: not_in_settlement
    description: OMS delivered sale has no matching forward settlement row; may be timing gap or cancellation/status issue.
    evidence_refs:
    - ev.walmart.relationships.001
    confidence: high
    review_status: accepted
    notes: Not in settlement
```

```yaml
candidate_card:
  card_type: mismatch_category
  card_id: mismatch_category.walmart.oms_to_settlement.price_variance
  name: Price variance
  fields:
    profile: reconciliation_profile.walmart.oms_to_settlement
    category_key: price_variance
    description: OMS charged_amount and settlement charged_amount differ by more than source query threshold 0.10.
    evidence_refs:
    - ev.walmart.reconciliation.001
    confidence: high
    review_status: accepted
    notes: Price variance
```

```yaml
candidate_card:
  card_type: mismatch_category
  card_id: mismatch_category.walmart.oms_to_settlement.expected_timing_gap
  name: Expected timing gap
  fields:
    profile: reconciliation_profile.walmart.oms_to_settlement
    category_key: expected_timing_gap
    description: December OMS orders may settle in January and settlement may include historical orders outside OMS range.
    evidence_refs:
    - ev.walmart.relationships.001
    confidence: high
    review_status: accepted
    notes: Expected timing gap
```

```yaml
candidate_card:
  card_type: mismatch_category
  card_id: mismatch_category.walmart.commission.rate_variance
  name: Commission rate variance
  fields:
    profile: reconciliation_profile.walmart.commission_validation
    category_key: rate_variance
    description: gross_commission deviates from 13.46% observed baseline by more than source query threshold 0.50.
    evidence_refs:
    - ev.walmart.reconciliation.001
    confidence: high
    review_status: accepted
    notes: Commission rate variance
```

```yaml
candidate_card:
  card_type: mismatch_category
  card_id: mismatch_category.walmart.refund_to_sale.missing_original_sale
  name: Refund missing original sale
  fields:
    profile: reconciliation_profile.walmart.refund_to_sale
    category_key: missing_original_sale
    description: Reverse/refund row lacks matching forward sale row within active settlement scope.
    evidence_refs:
    - ev.walmart.reconciliation.001
    confidence: high
    review_status: accepted
    notes: Refund missing original sale
```

```yaml
candidate_card:
  card_type: mismatch_category
  card_id: mismatch_category.walmart.mpf_tax.identity_break
  name: MPF tax identity break
  fields:
    profile: reconciliation_profile.walmart.mpf_tax_identity
    category_key: identity_break
    description: charged_amount does not reconcile to charged_amount_excluding_tax plus total_tax or withheld-tax sign semantics
      look inconsistent.
    evidence_refs:
    - ev.walmart.business_model.001
    confidence: high
    review_status: accepted
    notes: MPF tax identity break
```

```yaml
candidate_card:
  card_type: mismatch_category
  card_id: mismatch_category.walmart.lookup.sku_missing
  name: Lookup SKU missing
  fields:
    profile: reconciliation_profile.walmart.lookup_coverage
    category_key: sku_missing
    description: OMS/settlement SKU has no sku-populated lookup row; one SKU gap is documented and should be monitored.
    evidence_refs:
    - ev.walmart_lookup.schema.001
    confidence: high
    review_status: accepted
    notes: Lookup SKU missing
```

### 5.21 Reconciliation Variant Cards

No `reconciliation_variant` candidate cards are emitted in V3. Walmart reconciliation differences are captured in matching logic, mismatch categories, rules, and open reviews rather than unsupported variant cards.

### 5.22 Query Pattern Cards

```yaml
candidate_card:
  card_type: query_pattern
  card_id: query_pattern.walmart.forward_gmv_net_payout
  name: What is Walmart gross revenue and net payout?
  fields:
    natural_language_patterns: What is Walmart gross revenue and net payout?; Show product revenue, tax, commission, and seller
      payout.
    primary_metric: metric.marketplace.net_seller_payout
    source_tables:
    - table.zs_observe.walmart_settlement
    query_logic: Use forward settlement rows and compute payout from charged_amount_excluding_tax + gross_commission.
    sql_ref: sql.walmart.settlement.forward_gmv_net_payout
    scope_policy: Use documented group_level_id=22 from source as scope metadata; runtime account selection should be supplied
      externally by account-binding layer.
    evidence_refs:
    - ev.walmart.metrics.001
    confidence: high
    review_status: accepted
    notes: What is Walmart gross revenue and net payout?
```

```yaml
candidate_card:
  card_type: query_pattern
  card_id: query_pattern.walmart.return_rate
  name: What is Walmart refund rate?
  fields:
    natural_language_patterns: What is Walmart return/refund rate?; How many refunds compared to sales?
    primary_metric: metric.marketplace.return_rate
    source_tables:
    - table.zs_observe.walmart_settlement
    query_logic: Count reverse rows over forward rows using transaction_type.
    sql_ref: sql.walmart.settlement.return_rate
    scope_policy: Use documented group_level_id=22 from source as scope metadata; runtime account selection should be supplied
      externally by account-binding layer.
    evidence_refs:
    - ev.walmart.metrics.001
    confidence: high
    review_status: accepted
    notes: What is Walmart refund rate?
```

```yaml
candidate_card:
  card_type: query_pattern
  card_id: query_pattern.walmart.oms_aov
  name: What is Walmart AOV from OMS?
  fields:
    natural_language_patterns: What is Walmart AOV?; Average Walmart order value.
    primary_metric: metric.marketplace.average_order_value
    source_tables:
    - table.zs_observe.walmart_oms
    query_logic: Average charged_amount for delivered sales rows in OMS.
    sql_ref: sql.walmart.oms.aov
    scope_policy: Use documented group_level_id=22 from source as scope metadata; runtime account selection should be supplied
      externally by account-binding layer.
    evidence_refs:
    - ev.walmart.metrics.001
    confidence: high
    review_status: accepted
    notes: What is Walmart AOV from OMS?
```

```yaml
candidate_card:
  card_type: query_pattern
  card_id: query_pattern.walmart.cancellation_rate
  name: What is Walmart cancellation rate?
  fields:
    natural_language_patterns: What is the Walmart cancellation rate?
    primary_metric: metric.marketplace.cancellation_rate
    source_tables:
    - table.zs_observe.walmart_oms
    query_logic: Count cancelled OMS rows over total active OMS rows.
    sql_ref: sql.walmart.oms.cancellation_rate
    scope_policy: Use documented group_level_id=22 from source as scope metadata; runtime account selection should be supplied
      externally by account-binding layer.
    evidence_refs:
    - ev.walmart_oms.schema.001
    confidence: high
    review_status: accepted
    notes: What is Walmart cancellation rate?
```

```yaml
candidate_card:
  card_type: query_pattern
  card_id: query_pattern.walmart.monthly_revenue
  name: Show Walmart monthly revenue trend
  fields:
    natural_language_patterns: Monthly Walmart revenue and payout trend.
    primary_metric: metric.marketplace.net_seller_payout
    source_tables:
    - table.zs_observe.walmart_settlement
    query_logic: Group forward settlement rows by metadata_2 month.
    sql_ref: sql.walmart.settlement.monthly_revenue
    scope_policy: Use documented group_level_id=22 from source as scope metadata; runtime account selection should be supplied
      externally by account-binding layer.
    evidence_refs:
    - ev.walmart.metrics.001
    confidence: high
    review_status: accepted
    notes: Show Walmart monthly revenue trend
```

```yaml
candidate_card:
  card_type: query_pattern
  card_id: query_pattern.walmart.top_skus
  name: Which Walmart SKUs have the highest revenue?
  fields:
    natural_language_patterns: Top Walmart SKUs by revenue; best-selling Walmart products.
    primary_metric: metric.marketplace.sku_revenue
    source_tables:
    - table.zs_observe.walmart_settlement
    - table.zs_observe.walmart_lookup
    query_logic: Group forward settlement rows by sku_id and enrich with lookup.item_name.
    sql_ref: sql.walmart.settlement.top_skus
    scope_policy: Use documented group_level_id=22 from source as scope metadata; runtime account selection should be supplied
      externally by account-binding layer.
    evidence_refs:
    - ev.walmart.metrics.001
    confidence: high
    review_status: accepted
    notes: Which Walmart SKUs have the highest revenue?
```

```yaml
candidate_card:
  card_type: query_pattern
  card_id: query_pattern.walmart.state_distribution
  name: Which US states generate Walmart sales?
  fields:
    natural_language_patterns: Walmart revenue by US state; state-level sales distribution.
    primary_metric: metric.marketplace.revenue_by_state
    source_tables:
    - table.zs_observe.walmart_oms
    query_logic: Use OMS delivered rows and group by two-letter destination_state.
    sql_ref: sql.walmart.oms.state_distribution
    scope_policy: Use documented group_level_id=22 from source as scope metadata; runtime account selection should be supplied
      externally by account-binding layer.
    evidence_refs:
    - ev.walmart.metrics.001
    confidence: high
    review_status: accepted
    notes: Which US states generate Walmart sales?
```

```yaml
candidate_card:
  card_type: query_pattern
  card_id: query_pattern.walmart.payout_cycle
  name: Summarize Walmart payout cycles
  fields:
    natural_language_patterns: Show Walmart payout cycle summary; payout date and period end.
    primary_metric: metric.marketplace.net_seller_payout
    source_tables:
    - table.zs_observe.walmart_settlement
    query_logic: Group settlement rows by metadata_3 payout date and metadata_2 period end.
    sql_ref: sql.walmart.settlement.payout_cycle_summary
    scope_policy: Use documented group_level_id=22 from source as scope metadata; runtime account selection should be supplied
      externally by account-binding layer.
    evidence_refs:
    - ev.walmart.metrics.001
    confidence: high
    review_status: accepted
    notes: Summarize Walmart payout cycles
```

```yaml
candidate_card:
  card_type: query_pattern
  card_id: query_pattern.walmart.oms_settlement_reconciliation
  name: Reconcile Walmart OMS to settlement
  fields:
    natural_language_patterns: OMS to settlement reconciliation for Walmart delivered orders.
    primary_metric: metric.marketplace.gross_revenue
    source_tables:
    - table.zs_observe.walmart_oms
    - table.zs_observe.walmart_settlement
    query_logic: Left join OMS delivered sales to forward settlement rows by order_id and classify matched/not in settlement/price
      variance.
    sql_ref: sql.walmart.reconciliation.oms_settlement
    scope_policy: Use documented group_level_id=22 from source as scope metadata; runtime account selection should be supplied
      externally by account-binding layer.
    evidence_refs:
    - ev.walmart.reconciliation.001
    confidence: high
    review_status: accepted
    notes: Reconcile Walmart OMS to settlement
```

```yaml
candidate_card:
  card_type: query_pattern
  card_id: query_pattern.walmart.commission_validation
  name: Validate Walmart commission
  fields:
    natural_language_patterns: Validate Walmart referral fee; find commission outliers.
    primary_metric: metric.marketplace.effective_commission_rate
    source_tables:
    - table.zs_observe.walmart_settlement
    query_logic: Compare gross_commission to 13.46% observed baseline with 0.50 variance query threshold.
    sql_ref: sql.walmart.reconciliation.commission_validation
    scope_policy: Use documented group_level_id=22 from source as scope metadata; runtime account selection should be supplied
      externally by account-binding layer.
    evidence_refs:
    - ev.walmart.reconciliation.001
    confidence: high
    review_status: accepted
    notes: Validate Walmart commission
```

```yaml
candidate_card:
  card_type: query_pattern
  card_id: query_pattern.walmart.refund_sale_match
  name: Match Walmart refunds to sales
  fields:
    natural_language_patterns: Match Walmart refund rows to original sales.
    primary_metric: metric.marketplace.return_rate
    source_tables:
    - table.zs_observe.walmart_settlement
    query_logic: Join reverse settlement rows to forward sale rows by order_id and compare amount/commission reversal.
    sql_ref: sql.walmart.reconciliation.refund_sale_match
    scope_policy: Use documented group_level_id=22 from source as scope metadata; runtime account selection should be supplied
      externally by account-binding layer.
    evidence_refs:
    - ev.walmart.reconciliation.001
    confidence: high
    review_status: accepted
    notes: Match Walmart refunds to sales
```

```yaml
candidate_card:
  card_type: query_pattern
  card_id: query_pattern.walmart.full_three_table_view
  name: Build Walmart enriched three-table view
  fields:
    natural_language_patterns: Build Walmart OMS + settlement + lookup enriched table.
    primary_metric: metric.marketplace.net_seller_payout
    source_tables:
    - table.zs_observe.walmart_oms
    - table.zs_observe.walmart_settlement
    - table.zs_observe.walmart_lookup
    query_logic: Join OMS to settlement by order_id and lookup by sku_id=sku for order, product, tax, commission, and payout
      fields.
    sql_ref: sql.walmart.reconciliation.full_three_table_view
    scope_policy: Use documented group_level_id=22 from source as scope metadata; runtime account selection should be supplied
      externally by account-binding layer.
    evidence_refs:
    - ev.walmart.reconciliation.001
    confidence: high
    review_status: accepted
    notes: Build Walmart enriched three-table view
```

```yaml
candidate_card:
  card_type: query_pattern
  card_id: query_pattern.walmart.lookup_catalogue
  name: List usable Walmart SKU catalogue
  fields:
    natural_language_patterns: Show Walmart SKU catalogue with product names.
    primary_metric: metric.marketplace.sku_revenue
    source_tables:
    - table.zs_observe.walmart_lookup
    query_logic: Filter lookup to sku IS NOT NULL rows.
    sql_ref: sql.walmart.lookup.catalogue
    scope_policy: Use documented group_level_id=22 from source as scope metadata; runtime account selection should be supplied
      externally by account-binding layer.
    evidence_refs:
    - ev.walmart_lookup.schema.001
    confidence: high
    review_status: accepted
    notes: List usable Walmart SKU catalogue
```

```yaml
candidate_card:
  card_type: query_pattern
  card_id: query_pattern.walmart.mpf_tax_validation
  name: Validate Walmart MPF tax identity
  fields:
    natural_language_patterns: Validate charged_amount equals product revenue plus tax.
    primary_metric: metric.marketplace.tax_withheld
    source_tables:
    - table.zs_observe.walmart_settlement
    query_logic: Check charged_amount = charged_amount_excluding_tax + total_tax and withheld tax sign semantics.
    sql_ref: sql.walmart.validation.mpf_tax_identity
    scope_policy: Use documented group_level_id=22 from source as scope metadata; runtime account selection should be supplied
      externally by account-binding layer.
    evidence_refs:
    - ev.walmart.business_model.001
    confidence: high
    review_status: accepted
    notes: Validate Walmart MPF tax identity
```

```yaml
candidate_card:
  card_type: query_pattern
  card_id: query_pattern.walmart.wfs_fee_visibility
  name: Check WFS fee visibility
  fields:
    natural_language_patterns: Are WFS storage or inbound fees in Walmart settlement?
    primary_metric: metric.marketplace.net_seller_payout
    source_tables:
    - table.zs_observe.walmart_settlement
    query_logic: Monitor current WFS fee columns which are zero in source report; external WFS fee report needed for full
      WFS cost analysis.
    sql_ref: sql.walmart.validation.wfs_fee_visibility
    scope_policy: Use documented group_level_id=22 from source as scope metadata; runtime account selection should be supplied
      externally by account-binding layer.
    evidence_refs:
    - ev.walmart.quality.001
    confidence: high
    review_status: accepted
    notes: Check WFS fee visibility
```

### 5.23 Rule Cards

```yaml
candidate_card:
  card_type: rule
  card_id: rule.walmart.scope_filters
  name: Walmart mandatory scope filters
  fields:
    rule_type: query_filter
    rule_text: All Walmart production queries should apply is_active = true and group_level_id = 22 unless runtime scope overrides
      are supplied by a separate account-binding layer.
    related_canonical_id: table.zs_observe.walmart_oms
    severity: medium
    evidence_refs:
    - ev.walmart.filters.001
    confidence: high
    review_status: accepted
    notes: All Walmart production queries should apply is_active = true and group_level_id = 22 unless runtime scope overrides
      are supplied by a separate account-binding layer.
```

```yaml
candidate_card:
  card_type: rule
  card_id: rule.walmart.no_settled_amount_payout
  name: Do not use settled_amount as Walmart payout
  fields:
    rule_type: metric_semantics
    rule_text: walmart_settlement.settled_amount is always zero in this report; calculate payout as charged_amount_excluding_tax
      + gross_commission.
    related_canonical_id: column.zs_observe.walmart_settlement.settled_amount
    severity: medium
    evidence_refs:
    - ev.walmart.business_model.001
    confidence: high
    review_status: accepted
    notes: walmart_settlement.settled_amount is always zero in this report; calculate payout as charged_amount_excluding_tax
      + gross_commission.
```

```yaml
candidate_card:
  card_type: rule
  card_id: rule.walmart.mpf_tax_not_seller_revenue
  name: MPF tax is not seller revenue
  fields:
    rule_type: tax_semantics
    rule_text: marketplace_withheld_tax and total_tax represent US sales tax Walmart collects/remits; exclude tax from seller
      revenue and payout calculations.
    related_canonical_id: column.zs_observe.walmart_settlement.marketplace_withheld_tax
    severity: medium
    evidence_refs:
    - ev.walmart.business_model.001
    confidence: high
    review_status: accepted
    notes: marketplace_withheld_tax and total_tax represent US sales tax Walmart collects/remits; exclude tax from seller
      revenue and payout calculations.
```

```yaml
candidate_card:
  card_type: rule
  card_id: rule.walmart.forward_revenue_filter
  name: Forward sales filter
  fields:
    rule_type: query_filter
    rule_text: Use walmart_settlement.transaction_type = forward for settlement forward sales and walmart_oms.order_status
      = DELIVERED with internal_txn_type = sales for completed OMS sales.
    related_canonical_id: metric.marketplace.gross_revenue
    severity: medium
    evidence_refs:
    - ev.walmart.filters.001
    confidence: high
    review_status: accepted
    notes: Use walmart_settlement.transaction_type = forward for settlement forward sales and walmart_oms.order_status = DELIVERED
      with internal_txn_type = sales for completed OMS sales.
```

```yaml
candidate_card:
  card_type: rule
  card_id: rule.walmart.reverse_refund_filter
  name: Refund filter
  fields:
    rule_type: query_filter
    rule_text: Use walmart_settlement.transaction_type = reverse for Walmart refunds; internal_txn_type may be NULL, so transaction_type
      or other_type should be fallback.
    related_canonical_id: metric.marketplace.return_rate
    severity: medium
    evidence_refs:
    - ev.walmart.filters.001
    confidence: high
    review_status: accepted
    notes: Use walmart_settlement.transaction_type = reverse for Walmart refunds; internal_txn_type may be NULL, so transaction_type
      or other_type should be fallback.
```

```yaml
candidate_card:
  card_type: rule
  card_id: rule.walmart.lookup_sku_not_null
  name: Lookup SKU join filter
  fields:
    rule_type: join_guardrail
    rule_text: Use walmart_lookup.sku IS NOT NULL for all SKU-to-name joins because sku-null rows are catalogue content/attribute
      rows.
    related_canonical_id: table.zs_observe.walmart_lookup
    severity: medium
    evidence_refs:
    - ev.walmart_lookup.schema.001
    confidence: high
    review_status: accepted
    notes: Use walmart_lookup.sku IS NOT NULL for all SKU-to-name joins because sku-null rows are catalogue content/attribute
      rows.
```

```yaml
candidate_card:
  card_type: rule
  card_id: rule.walmart.oms_clean_rows
  name: OMS clean row filter
  fields:
    rule_type: query_filter
    rule_text: For geographic or financial analysis affected by column shifting, use valid order_status filters and optionally
      currency_type = USD and LENGTH(destination_state) = 2.
    related_canonical_id: table.zs_observe.walmart_oms
    severity: medium
    evidence_refs:
    - ev.walmart_oms.quality.001
    confidence: high
    review_status: accepted
    notes: For geographic or financial analysis affected by column shifting, use valid order_status filters and optionally
      currency_type = USD and LENGTH(destination_state) = 2.
```

```yaml
candidate_card:
  card_type: rule
  card_id: rule.walmart.compute_commission_rate
  name: Compute commission rate from amounts
  fields:
    rule_type: metric_semantics
    rule_text: Do not use base_commission_rate or commission_rate for operational analysis because they are NULL/not published;
      compute ABS(gross_commission)/charged_amount_excluding_tax.
    related_canonical_id: metric.marketplace.effective_commission_rate
    severity: high
    evidence_refs:
    - ev.walmart.quality.001
    confidence: high
    review_status: accepted
    notes: Do not use base_commission_rate or commission_rate for operational analysis because they are NULL/not published;
      compute ABS(gross_commission)/charged_amount_excluding_tax.
```

```yaml
candidate_card:
  card_type: rule
  card_id: rule.walmart.hsn_is_barcode
  name: OMS hsn is barcode not Indian HSN
  fields:
    rule_type: schema_caveat
    rule_text: walmart_oms.hsn is a barcode/GTIN-like value, not an Indian HSN code; use item_id/partner_gtin for barcode
      matching and do not use hsn for tax classification.
    related_canonical_id: column.zs_observe.walmart_oms.hsn
    severity: medium
    evidence_refs:
    - ev.walmart_oms.quality.001
    confidence: high
    review_status: accepted
    notes: walmart_oms.hsn is a barcode/GTIN-like value, not an Indian HSN code; use item_id/partner_gtin for barcode matching
      and do not use hsn for tax classification.
```

```yaml
candidate_card:
  card_type: rule
  card_id: rule.walmart.no_indian_tax_cards
  name: No Indian GST/TCS/TDS cards
  fields:
    rule_type: scope_guardrail
    rule_text: Walmart.com US marketplace has no Indian GST, TCS, or TDS obligations in this source; do not create Indian
      statutory tax cards.
    related_canonical_id: domain.marketplace.walmart.tax
    severity: high
    evidence_refs:
    - ev.walmart.business_model.001
    confidence: high
    review_status: accepted
    notes: Walmart.com US marketplace has no Indian GST, TCS, or TDS obligations in this source; do not create Indian statutory
      tax cards.
```

```yaml
candidate_card:
  card_type: rule
  card_id: rule.walmart.wfs_fees_external
  name: WFS fees not in settlement report
  fields:
    rule_type: source_gap
    rule_text: WFS storage, inbound, and removal fees are not broken out in walmart_settlement; request external WFS fee report
      before analyzing those costs.
    related_canonical_id: table.zs_observe.walmart_settlement
    severity: medium
    evidence_refs:
    - ev.walmart.quality.001
    confidence: high
    review_status: accepted
    notes: WFS storage, inbound, and removal fees are not broken out in walmart_settlement; request external WFS fee report
      before analyzing those costs.
```

```yaml
candidate_card:
  card_type: rule
  card_id: rule.walmart.no_process_variants_from_segments
  name: No segment-only process variants
  fields:
    rule_type: card_type_guardrail
    rule_text: Do not create process_variant cards from WFS, category, product_type, state, or currency labels; use value_profile,
      rule, or platform_context unless source documents a materially different workflow.
    related_canonical_id: platform_context.walmart.us
    severity: high
    evidence_refs:
    - ev.walmart.overview.001
    confidence: high
    review_status: accepted
    notes: Do not create process_variant cards from WFS, category, product_type, state, or currency labels; use value_profile,
      rule, or platform_context unless source documents a materially different workflow.
```

```yaml
candidate_card:
  card_type: rule
  card_id: rule.walmart.group_level_scope_only
  name: group_level_id is scope metadata only
  fields:
    rule_type: scope_guardrail
    rule_text: Documented group_level_id = 22 can be stored as scope metadata/filter guidance, but must not create tenant,
      group, platform_account, or account_data_binding cards.
    related_canonical_id: column.zs_observe.walmart_settlement.group_level_id
    severity: high
    evidence_refs:
    - ev.walmart.filters.001
    confidence: high
    review_status: accepted
    notes: Documented group_level_id = 22 can be stored as scope metadata/filter guidance, but must not create tenant, group,
      platform_account, or account_data_binding cards.
```

```yaml
candidate_card:
  card_type: rule
  card_id: rule.walmart.no_external_bank_or_erp
  name: No bank/ERP/accounting cards
  fields:
    rule_type: scope_guardrail
    rule_text: Payout date metadata and bank-transfer language are allowed as settlement metadata only; do not create bank
      account, ERP/accounting, payment gateway, or statutory filing cards.
    related_canonical_id: table.zs_observe.walmart_settlement
    severity: high
    evidence_refs:
    - ev.walmart.business_model.001
    confidence: high
    review_status: accepted
    notes: Payout date metadata and bank-transfer language are allowed as settlement metadata only; do not create bank account,
      ERP/accounting, payment gateway, or statutory filing cards.
```

### 5.24 Validation Test Cards

```yaml
candidate_card:
  card_type: validation_test
  card_id: validation_test.walmart.no_settled_amount_payout
  name: Validate Walmart payout does not use settled_amount
  fields:
    related_canonical_id: rule.walmart.no_settled_amount_payout
    test_description: Semantic parser/query generator must not use walmart_settlement.settled_amount as net payout because
      it is always zero.
    test_type: semantic_guard
    sql_ref: sql.walmart.settlement.payout_cycle_summary
    evidence_refs:
    - ev.walmart.business_model.001
    confidence: high
    review_status: accepted
    notes: Validate Walmart payout does not use settled_amount
```

```yaml
candidate_card:
  card_type: validation_test
  card_id: validation_test.walmart.mandatory_filters
  name: Validate mandatory Walmart filters
  fields:
    related_canonical_id: rule.walmart.scope_filters
    test_description: Queries should include is_active = true and documented scope group_level_id = 22 unless external runtime
      scope overrides are explicitly supplied.
    test_type: semantic_guard
    sql_ref: sql.walmart.validation.oms_clean_rows_monitor
    evidence_refs:
    - ev.walmart.filters.001
    confidence: high
    review_status: accepted
    notes: Validate mandatory Walmart filters
```

```yaml
candidate_card:
  card_type: validation_test
  card_id: validation_test.walmart.lookup_sku_not_null
  name: Validate lookup joins exclude sku-null rows
  fields:
    related_canonical_id: rule.walmart.lookup_sku_not_null
    test_description: SKU-to-name joins must filter walmart_lookup.sku IS NOT NULL.
    test_type: join_guard
    sql_ref: sql.walmart.validation.lookup_sku_null_monitor
    evidence_refs:
    - ev.walmart_lookup.schema.001
    confidence: high
    review_status: accepted
    notes: Validate lookup joins exclude sku-null rows
```

```yaml
candidate_card:
  card_type: validation_test
  card_id: validation_test.walmart.mpf_tax_identity
  name: Validate MPF tax identity
  fields:
    related_canonical_id: reconciliation_profile.walmart.mpf_tax_identity
    test_description: Forward settlement rows should reconcile charged_amount to charged_amount_excluding_tax plus total_tax;
      withheld tax is not seller revenue.
    test_type: financial_validation
    sql_ref: sql.walmart.validation.mpf_tax_identity
    evidence_refs:
    - ev.walmart.business_model.001
    confidence: high
    review_status: accepted
    notes: Validate MPF tax identity
```

```yaml
candidate_card:
  card_type: validation_test
  card_id: validation_test.walmart.commission_rate_computed
  name: Validate commission rate is computed from amounts
  fields:
    related_canonical_id: rule.walmart.compute_commission_rate
    test_description: Commission rate columns are NULL/not published, so effective commission must be computed from gross_commission
      and charged_amount_excluding_tax.
    test_type: financial_validation
    sql_ref: sql.walmart.reconciliation.commission_validation
    evidence_refs:
    - ev.walmart.quality.001
    confidence: high
    review_status: accepted
    notes: Validate commission rate is computed from amounts
```

```yaml
candidate_card:
  card_type: validation_test
  card_id: validation_test.walmart.no_indian_tax_cards
  name: Validate no Indian tax card creation
  fields:
    related_canonical_id: rule.walmart.no_indian_tax_cards
    test_description: Do not emit GST/TCS/TDS statutory filing cards from Walmart US data.
    test_type: scope_guard
    sql_ref: sql.walmart.validation.mpf_tax_identity
    evidence_refs:
    - ev.walmart.business_model.001
    confidence: high
    review_status: accepted
    notes: Validate no Indian tax card creation
```

```yaml
candidate_card:
  card_type: validation_test
  card_id: validation_test.walmart.oms_clean_rows
  name: Validate OMS clean-row caveats
  fields:
    related_canonical_id: rule.walmart.oms_clean_rows
    test_description: Geographic analysis must account for column shifting using valid status/currency/state filters.
    test_type: data_quality_validation
    sql_ref: sql.walmart.validation.oms_clean_rows_monitor
    evidence_refs:
    - ev.walmart_oms.quality.001
    confidence: high
    review_status: accepted
    notes: Validate OMS clean-row caveats
```

```yaml
candidate_card:
  card_type: validation_test
  card_id: validation_test.walmart.no_process_variants
  name: Validate no process variants from WFS or categories
  fields:
    related_canonical_id: rule.walmart.no_process_variants_from_segments
    test_description: Parser output should contain zero process_variant cards; WFS/category/product_type are value profiles
      or platform context.
    test_type: card_type_guard
    sql_ref: sql.walmart.validation.wfs_fee_visibility
    evidence_refs:
    - ev.walmart.overview.001
    confidence: high
    review_status: accepted
    notes: Validate no process variants from WFS or categories
```

```yaml
candidate_card:
  card_type: validation_test
  card_id: validation_test.walmart.oms_settlement_coverage
  name: Validate OMS-settlement coverage caveat
  fields:
    related_canonical_id: reconciliation_profile.walmart.oms_to_settlement
    test_description: OMS-settlement coverage near 89.6% has documented timing/cancellation/historical explanations and should
      not automatically fail without date-scope alignment.
    test_type: reconciliation_validation
    sql_ref: sql.walmart.reconciliation.oms_settlement
    evidence_refs:
    - ev.walmart.relationships.001
    confidence: high
    review_status: accepted
    notes: Validate OMS-settlement coverage caveat
```

### 5.25 Output Contract Cards

```yaml
candidate_card:
  card_type: output_contract
  card_id: output_contract.walmart.forward_revenue
  name: Walmart forward revenue output
  fields:
    related_canonical_id: metric.marketplace.net_seller_payout
    output_columns:
    - gross_gmv
    - product_revenue
    - tax_withheld_by_walmart
    - total_commission
    - walmart_savings_credit
    - net_seller_revenue
    - commission_rate_pct
    contract_type: marketplace_analysis_output
    evidence_refs:
    - ev.walmart.metrics.001
    confidence: high
    review_status: accepted
    notes: Walmart forward revenue output
```

```yaml
candidate_card:
  card_type: output_contract
  card_id: output_contract.walmart.oms_settlement_recon
  name: Walmart OMS-settlement reconciliation output
  fields:
    related_canonical_id: reconciliation_profile.walmart.oms_to_settlement
    output_columns:
    - order_id
    - sku_id
    - oms_price_usd
    - order_status
    - order_date
    - stl_total
    - stl_excl_tax
    - tax_withheld
    - gross_commission
    - marketplace_withheld_tax
    - net_payout
    - price_variance
    - recon_status
    contract_type: marketplace_analysis_output
    evidence_refs:
    - ev.walmart.reconciliation.001
    confidence: high
    review_status: accepted
    notes: Walmart OMS-settlement reconciliation output
```

```yaml
candidate_card:
  card_type: output_contract
  card_id: output_contract.walmart.payout_cycle
  name: Walmart payout cycle output
  fields:
    related_canonical_id: metric.marketplace.net_seller_payout
    output_columns:
    - payout_date
    - period_end
    - line_items
    - orders
    - product_revenue
    - total_commission
    - wm_savings
    - estimated_net_payout
    contract_type: marketplace_analysis_output
    evidence_refs:
    - ev.walmart.metrics.001
    confidence: high
    review_status: accepted
    notes: Walmart payout cycle output
```

```yaml
candidate_card:
  card_type: output_contract
  card_id: output_contract.walmart.sku_performance
  name: Walmart SKU performance output
  fields:
    related_canonical_id: metric.marketplace.sku_revenue
    output_columns:
    - sku_id
    - item_name
    - product_type
    - orders
    - revenue
    - avg_price
    - net_payout
    contract_type: marketplace_analysis_output
    evidence_refs:
    - ev.walmart.metrics.001
    confidence: high
    review_status: accepted
    notes: Walmart SKU performance output
```

```yaml
candidate_card:
  card_type: output_contract
  card_id: output_contract.walmart.state_distribution
  name: Walmart state distribution output
  fields:
    related_canonical_id: metric.marketplace.revenue_by_state
    output_columns:
    - destination_state
    - orders
    - revenue_usd
    - pct_of_orders
    contract_type: marketplace_analysis_output
    evidence_refs:
    - ev.walmart.metrics.001
    confidence: high
    review_status: accepted
    notes: Walmart state distribution output
```

```yaml
candidate_card:
  card_type: output_contract
  card_id: output_contract.walmart.commission_validation
  name: Walmart commission validation output
  fields:
    related_canonical_id: reconciliation_profile.walmart.commission_validation
    output_columns:
    - order_id
    - sku_id
    - product_price
    - commission_charged
    - expected_commission
    - variance
    contract_type: marketplace_analysis_output
    evidence_refs:
    - ev.walmart.reconciliation.001
    confidence: high
    review_status: accepted
    notes: Walmart commission validation output
```

```yaml
candidate_card:
  card_type: output_contract
  card_id: output_contract.walmart.refund_sale_match
  name: Walmart refund-sale match output
  fields:
    related_canonical_id: reconciliation_profile.walmart.refund_to_sale
    output_columns:
    - order_id
    - sku_id
    - refund_amount
    - commission_reversed
    - original_sale
    - original_commission
    - refund_variance
    contract_type: marketplace_analysis_output
    evidence_refs:
    - ev.walmart.reconciliation.001
    confidence: high
    review_status: accepted
    notes: Walmart refund-sale match output
```

### 5.26 Execution Constraint Set Cards

```yaml
candidate_card:
  card_type: execution_constraint_set
  card_id: execution_constraint_set.walmart.query_scope_and_filters
  name: Walmart query scope and filter constraints
  fields:
    constraint_name: Walmart query scope and filter constraints
    applies_to:
    - query_pattern.walmart.*
    - metric_implementation.walmart.*
    semantic_constraints:
    - Use zs_observe Walmart tables only for this canonical.
    - Apply is_active = true where documented.
    - Use group_level_id = 22 as documented Walmart/Folkulture scope metadata; runtime account binding remains external.
    - Use explicit transaction_type, internal_txn_type, or order_status filters for forward, reverse, and cancellation analysis.
    - For lookup enrichment, filter walmart_lookup.sku IS NOT NULL.
    aggregation_order:
    - pre-filter active/scope rows
    - pre-aggregate settlement rows before SKU or order-level enrichment where grain can multiply
    - compute payout components before derived rates
    filter_rules:
    - rule.walmart.scope_filters
    - rule.walmart.forward_revenue_filter
    - rule.walmart.reverse_refund_filter
    - rule.walmart.lookup_sku_not_null
    - rule.walmart.oms_clean_rows
    out_of_scope_runtime_constraints:
    - runtime tenant/account binding
    - bank deposit reconciliation
    evidence_refs:
    - ev.walmart.filters.001
    - ev.walmart_lookup.schema.001
    confidence: high
    review_status: accepted
    notes: Runtime bundle for deterministic Walmart marketplace query generation.
```

```yaml
candidate_card:
  card_type: execution_constraint_set
  card_id: execution_constraint_set.walmart.semantic_guardrails
  name: Walmart semantic guardrails
  fields:
    constraint_name: Walmart semantic guardrails
    applies_to:
    - query_pattern.walmart.*
    - metric_implementation.walmart.*
    - business_process.walmart.*
    semantic_constraints:
    - Never use walmart_settlement.settled_amount as seller payout.
    - Treat marketplace_withheld_tax and total_tax as US Marketplace Facilitator tax withheld by Walmart, not seller revenue.
    - Do not create Indian GST/TCS/TDS/statutory filing semantics for Walmart.
    - Treat WFS, category, product type, currency, and state as value/profile/context semantics, not process variants.
    - Do not create external bank, ERP, warehouse, or logistics lifecycle cards.
    sign_rules:
    - gross_commission is signed as a deduction/fee component; payout formula adds it to excluding-tax product revenue
    filter_rules:
    - rule.walmart.no_settled_amount_payout
    - rule.walmart.mpf_tax_not_seller_revenue
    - rule.walmart.no_indian_tax_cards
    - rule.walmart.no_process_variants_from_segments
    - rule.walmart.no_external_bank_or_erp
    out_of_scope_runtime_constraints:
    - WFS storage/inbound/removal fee reports
    - bank-transfer reconciliation
    evidence_refs:
    - ev.walmart.business_model.001
    - ev.walmart.quality.001
    confidence: high
    review_status: accepted
    notes: Cross-cutting semantic constraints that materially affect every Walmart financial query.
```

## 6. Candidate Edges — Unified Edge Taxonomy

> This section uses the Flipkart gold-standard edge block shape: every `candidate_edge` has `edge_id`, `edge_type`, `source`, `target`, and a nested `fields` map. Legacy `source_id` and `target_id` are intentionally not used.

### 6.0 Unified Edge Rules

```yaml
unified_edge_rules:
  canonical_edge_format: UPPERCASE_UNDERSCORE
  accepted_legacy_aliases: true
  canonicalize_legacy_aliases_before_ingestion: true
  store_directed_edge_as_source_of_truth: true
  include_inverse_edge_type_on_every_edge: true
  materialize_inverse_when_materialize_inverse_true: true
  parser_helper_policy:
    retain_parser_helper_edges: true
    parser_helper_edges_may_be_collapsed_into_fields: true
    parser_helper_edge_class: parser_helper
  walmart_specific_edge_shape_rule: Use source/target/fields, never source_id/target_id at top level.
```

### 6.1 Unified Edge Taxonomy Registry

```yaml
unified_edge_taxonomy_registry:
- edge_type: ANSWERS_WITH_METRIC
  observed_source_target_types:
  - query_pattern -> metric
  inverse_edge_type: PRODUCED_BY_QUERY_PATTERN
  materialize_inverse_default: false
- edge_type: APPLIES_TO
  observed_source_target_types:
  - rule -> column
  - rule -> domain
  - rule -> metric
  - rule -> platform_context
  - rule -> table
  inverse_edge_type: HAS_APPLIED_RULE
  materialize_inverse_default: false
- edge_type: APPLIES_TO_QUERY_PATTERN
  observed_source_target_types:
  - execution_constraint_set -> query_pattern
  inverse_edge_type: HAS_EXECUTION_CONSTRAINT_SET
  materialize_inverse_default: false
- edge_type: CONSTRAINED_BY_RULE
  observed_source_target_types:
  - metric_implementation -> rule
  inverse_edge_type: CONSTRAINS_CARD
  materialize_inverse_default: false
- edge_type: ENFORCES_FORMULA
  observed_source_target_types:
  - rule -> formula_template
  inverse_edge_type: FORMULA_ENFORCED_BY_RULE
  materialize_inverse_default: false
- edge_type: FROM_TABLE
  observed_source_target_types:
  - relationship -> table
  inverse_edge_type: SOURCE_OF_RELATIONSHIP
  materialize_inverse_default: false
- edge_type: HAS_COLUMN
  observed_source_target_types:
  - table -> column
  inverse_edge_type: BELONGS_TO_TABLE
  materialize_inverse_default: true
- edge_type: HAS_CONTEXT
  observed_source_target_types:
  - business_process -> platform_context
  - domain -> platform_context
  - metric_implementation -> platform_context
  - platform -> platform_context
  - table -> platform_context
  inverse_edge_type: BELONGS_TO_CONTEXT
  materialize_inverse_default: false
- edge_type: HAS_DOMAIN
  observed_source_target_types:
  - metric -> domain
  - platform_context -> domain
  - table -> domain
  inverse_edge_type: BELONGS_TO_CONTEXT_OR_CARD
  materialize_inverse_default: false
- edge_type: HAS_MATCHING_LOGIC
  observed_source_target_types:
  - reconciliation_profile -> matching_logic
  inverse_edge_type: SUPPORTS_RECONCILIATION_PROFILE
  materialize_inverse_default: false
- edge_type: HAS_MISMATCH_CATEGORY
  observed_source_target_types:
  - reconciliation_profile -> mismatch_category
  inverse_edge_type: MISMATCH_OF_PROFILE
  materialize_inverse_default: false
- edge_type: HAS_SIDE
  observed_source_target_types:
  - reconciliation_profile -> reconciliation_side
  inverse_edge_type: BELONGS_TO_RECONCILIATION_PROFILE
  materialize_inverse_default: false
- edge_type: HAS_STATE_TRANSITION
  observed_source_target_types:
  - business_process -> state_transition
  inverse_edge_type: PART_OF_PROCESS
  materialize_inverse_default: true
- edge_type: HAS_TABLE
  observed_source_target_types:
  - domain -> table
  - platform_context -> table
  inverse_edge_type: BELONGS_TO_DOMAIN_OR_CONTEXT
  materialize_inverse_default: false
- edge_type: HAS_UNIT
  observed_source_target_types:
  - reconciliation_profile -> reconciliation_unit
  inverse_edge_type: PRIMARY_UNIT_OF_PROFILE
  materialize_inverse_default: false
- edge_type: HAS_VALUE_PROFILE
  observed_source_target_types:
  - column -> value_profile
  - table -> value_profile
  inverse_edge_type: PROFILES_COLUMN_OR_TABLE
  materialize_inverse_default: true
- edge_type: HAS_WORKFLOW_STEP
  observed_source_target_types:
  - business_process -> workflow_step
  inverse_edge_type: BELONGS_TO_PROCESS
  materialize_inverse_default: true
- edge_type: IMPLEMENTED_BY
  observed_source_target_types:
  - metric -> metric_implementation
  inverse_edge_type: IMPLEMENTS
  materialize_inverse_default: true
- edge_type: IMPLEMENTS
  observed_source_target_types:
  - metric_implementation -> metric
  inverse_edge_type: IMPLEMENTED_BY
  materialize_inverse_default: true
- edge_type: INCLUDES_RULE
  observed_source_target_types:
  - execution_constraint_set -> rule
  inverse_edge_type: INCLUDED_IN_CONSTRAINT_SET
  materialize_inverse_default: false
- edge_type: OUTPUT_FOR
  observed_source_target_types:
  - output_contract -> metric
  - output_contract -> reconciliation_profile
  inverse_edge_type: USES_OUTPUT_CONTRACT
  materialize_inverse_default: false
- edge_type: PARENT_METRIC
  observed_source_target_types:
  - metric_dependency -> metric
  inverse_edge_type: HAS_METRIC_DEPENDENCY
  materialize_inverse_default: false
- edge_type: PART_OF_PROCESS
  observed_source_target_types:
  - state_transition -> business_process
  inverse_edge_type: HAS_STATE_TRANSITION
  materialize_inverse_default: true
- edge_type: PROFILES_COLUMN
  observed_source_target_types:
  - value_profile -> column
  - value_profile -> table
  inverse_edge_type: HAS_VALUE_PROFILE
  materialize_inverse_default: true
- edge_type: RECONCILED_BY
  observed_source_target_types:
  - business_process -> reconciliation_profile
  inverse_edge_type: SUPPORTS_PROCESS
  materialize_inverse_default: false
- edge_type: TO_TABLE
  observed_source_target_types:
  - relationship -> table
  inverse_edge_type: TARGET_OF_RELATIONSHIP
  materialize_inverse_default: false
- edge_type: USES
  observed_source_target_types:
  - workflow_step -> column
  - workflow_step -> formula_template
  - workflow_step -> platform_context
  - workflow_step -> reconciliation_profile
  - workflow_step -> relationship
  - workflow_step -> table
  inverse_edge_type: USED_BY_STEP
  materialize_inverse_default: false
- edge_type: USES_COLUMN
  observed_source_target_types:
  - formula_template -> column
  - matching_logic -> column
  - metric_implementation -> column
  - query_pattern -> column
  - relationship -> column
  - rule -> column
  - state_transition -> column
  - validation_test -> column
  - workflow_step -> column
  inverse_edge_type: USED_BY_CARD
  materialize_inverse_default: false
- edge_type: USES_DEPENDENT_METRIC
  observed_source_target_types:
  - metric_dependency -> metric
  inverse_edge_type: DEPENDENCY_USED_BY
  materialize_inverse_default: false
- edge_type: USES_RELATIONSHIP
  observed_source_target_types:
  - reconciliation_profile -> relationship
  inverse_edge_type: USED_BY_QUERY_PATTERN
  materialize_inverse_default: false
- edge_type: USES_STATE_COLUMN
  observed_source_target_types:
  - state_transition -> column
  inverse_edge_type: STATE_COLUMN_USED_BY
  materialize_inverse_default: false
- edge_type: USES_TABLE
  observed_source_target_types:
  - formula_template -> table
  - metric_implementation -> table
  - query_pattern -> table
  - reconciliation_profile -> table
  - reconciliation_side -> table
  inverse_edge_type: USED_BY_CARD
  materialize_inverse_default: false
- edge_type: VALIDATED_BY
  observed_source_target_types:
  - business_process -> reconciliation_profile
  inverse_edge_type: VALIDATES_PROCESS
  materialize_inverse_default: false
- edge_type: VALIDATES
  observed_source_target_types:
  - validation_test -> reconciliation_profile
  - validation_test -> rule
  inverse_edge_type: VALIDATED_BY_TEST
  materialize_inverse_default: false
```

### 6.2 Legacy Alias Normalization Registry

```yaml
edge_normalization_registry:
- legacy_edge_alias: source_id
  canonical_field: source
  instruction: V3 emits only source; source_id from V1/V2 is not used.
- legacy_edge_alias: target_id
  canonical_field: target
  instruction: V3 emits only target; target_id from V1/V2 is not used.
- legacy_edge_alias: HAS_CONTEXT for platform->platform_context
  canonical_edge_type: HAS_CONTEXT
  gold_shape: source/target/fields
- legacy_edge_alias: CONSTRAINED_BY_RULE
  canonical_edge_type: CONSTRAINED_BY_RULE
  gold_shape: source/target/fields
```

### 6.3 Edge Coverage Summary

```yaml
edge_coverage_summary:
  ANSWERS_WITH_METRIC: 15
  APPLIES_TO: 14
  APPLIES_TO_QUERY_PATTERN: 30
  CONSTRAINED_BY_RULE: 28
  ENFORCES_FORMULA: 4
  FROM_TABLE: 4
  HAS_COLUMN: 125
  HAS_CONTEXT: 27
  HAS_DOMAIN: 24
  HAS_MATCHING_LOGIC: 5
  HAS_MISMATCH_CATEGORY: 7
  HAS_SIDE: 10
  HAS_STATE_TRANSITION: 4
  HAS_TABLE: 6
  HAS_UNIT: 5
  HAS_VALUE_PROFILE: 11
  HAS_WORKFLOW_STEP: 11
  IMPLEMENTED_BY: 12
  IMPLEMENTS: 12
  INCLUDES_RULE: 10
  OUTPUT_FOR: 7
  PARENT_METRIC: 4
  PART_OF_PROCESS: 4
  PROFILES_COLUMN: 11
  RECONCILED_BY: 2
  TO_TABLE: 4
  USES: 11
  USES_COLUMN: 458
  USES_DEPENDENT_METRIC: 4
  USES_RELATIONSHIP: 3
  USES_STATE_COLUMN: 4
  USES_TABLE: 54
  VALIDATED_BY: 2
  VALIDATES: 9
```

### 6.4 Candidate Edge Registry

```yaml
candidate_edge:
  edge_id: edge.walmart.0001
  edge_type: HAS_CONTEXT
  source: platform.walmart
  target: platform_context.walmart.us
  fields:
    edge_family: business_hierarchy_in_scope
    evidence_basis: source-backed card field dependency
    confidence: high
    canonical_cognee_edge: true
    marketplace_only: true
    canonical_edge_type: HAS_CONTEXT
    inverse_edge_type: BELONGS_TO_CONTEXT
    materialize_inverse: false
    edge_class: canonical
    source_type: platform
    target_type: platform_context
    evidence_refs:
    - ev.walmart.overview.001
```

```yaml
candidate_edge:
  edge_id: edge.walmart.0002
  edge_type: HAS_DOMAIN
  source: platform_context.walmart.us
  target: domain.marketplace.walmart.orders
  fields:
    edge_family: business_hierarchy_in_scope
    evidence_basis: source-backed card field dependency
    confidence: high
    canonical_cognee_edge: true
    marketplace_only: true
    canonical_edge_type: HAS_DOMAIN
    inverse_edge_type: BELONGS_TO_CONTEXT_OR_CARD
    materialize_inverse: false
    edge_class: canonical
    source_type: platform_context
    target_type: domain
    evidence_refs:
    - ev.walmart_oms.schema.001
```

```yaml
candidate_edge:
  edge_id: edge.walmart.0003
  edge_type: HAS_DOMAIN
  source: platform_context.walmart.us
  target: domain.marketplace.walmart.settlement
  fields:
    edge_family: business_hierarchy_in_scope
    evidence_basis: source-backed card field dependency
    confidence: high
    canonical_cognee_edge: true
    marketplace_only: true
    canonical_edge_type: HAS_DOMAIN
    inverse_edge_type: BELONGS_TO_CONTEXT_OR_CARD
    materialize_inverse: false
    edge_class: canonical
    source_type: platform_context
    target_type: domain
    evidence_refs:
    - ev.walmart_settlement.schema.001
```

```yaml
candidate_edge:
  edge_id: edge.walmart.0004
  edge_type: HAS_DOMAIN
  source: platform_context.walmart.us
  target: domain.marketplace.walmart.catalogue
  fields:
    edge_family: business_hierarchy_in_scope
    evidence_basis: source-backed card field dependency
    confidence: high
    canonical_cognee_edge: true
    marketplace_only: true
    canonical_edge_type: HAS_DOMAIN
    inverse_edge_type: BELONGS_TO_CONTEXT_OR_CARD
    materialize_inverse: false
    edge_class: canonical
    source_type: platform_context
    target_type: domain
    evidence_refs:
    - ev.walmart_lookup.schema.001
```

```yaml
candidate_edge:
  edge_id: edge.walmart.0005
  edge_type: HAS_DOMAIN
  source: platform_context.walmart.us
  target: domain.marketplace.walmart.fees
  fields:
    edge_family: business_hierarchy_in_scope
    evidence_basis: source-backed card field dependency
    confidence: high
    canonical_cognee_edge: true
    marketplace_only: true
    canonical_edge_type: HAS_DOMAIN
    inverse_edge_type: BELONGS_TO_CONTEXT_OR_CARD
    materialize_inverse: false
    edge_class: canonical
    source_type: platform_context
    target_type: domain
    evidence_refs:
    - ev.walmart.business_model.001
```

```yaml
candidate_edge:
  edge_id: edge.walmart.0006
  edge_type: HAS_DOMAIN
  source: platform_context.walmart.us
  target: domain.marketplace.walmart.tax
  fields:
    edge_family: business_hierarchy_in_scope
    evidence_basis: source-backed card field dependency
    confidence: high
    canonical_cognee_edge: true
    marketplace_only: true
    canonical_edge_type: HAS_DOMAIN
    inverse_edge_type: BELONGS_TO_CONTEXT_OR_CARD
    materialize_inverse: false
    edge_class: canonical
    source_type: platform_context
    target_type: domain
    evidence_refs:
    - ev.walmart.business_model.001
```

```yaml
candidate_edge:
  edge_id: edge.walmart.0007
  edge_type: HAS_DOMAIN
  source: platform_context.walmart.us
  target: domain.marketplace.walmart.returns
  fields:
    edge_family: business_hierarchy_in_scope
    evidence_basis: source-backed card field dependency
    confidence: high
    canonical_cognee_edge: true
    marketplace_only: true
    canonical_edge_type: HAS_DOMAIN
    inverse_edge_type: BELONGS_TO_CONTEXT_OR_CARD
    materialize_inverse: false
    edge_class: canonical
    source_type: platform_context
    target_type: domain
    evidence_refs:
    - ev.walmart.lifecycle.001
```

```yaml
candidate_edge:
  edge_id: edge.walmart.0008
  edge_type: HAS_DOMAIN
  source: platform_context.walmart.us
  target: domain.marketplace.walmart.reconciliation
  fields:
    edge_family: business_hierarchy_in_scope
    evidence_basis: source-backed card field dependency
    confidence: high
    canonical_cognee_edge: true
    marketplace_only: true
    canonical_edge_type: HAS_DOMAIN
    inverse_edge_type: BELONGS_TO_CONTEXT_OR_CARD
    materialize_inverse: false
    edge_class: canonical
    source_type: platform_context
    target_type: domain
    evidence_refs:
    - ev.walmart.reconciliation.001
```

```yaml
candidate_edge:
  edge_id: edge.walmart.0009
  edge_type: HAS_TABLE
  source: platform_context.walmart.us
  target: table.zs_observe.walmart_oms
  fields:
    edge_family: business_hierarchy_in_scope
    evidence_basis: source-backed card field dependency
    confidence: high
    canonical_cognee_edge: true
    marketplace_only: true
    canonical_edge_type: HAS_TABLE
    inverse_edge_type: BELONGS_TO_DOMAIN_OR_CONTEXT
    materialize_inverse: false
    edge_class: canonical
    source_type: platform_context
    target_type: table
    evidence_refs:
    - ev.walmart.table_summary.001
```

```yaml
candidate_edge:
  edge_id: edge.walmart.0010
  edge_type: HAS_TABLE
  source: platform_context.walmart.us
  target: table.zs_observe.walmart_settlement
  fields:
    edge_family: business_hierarchy_in_scope
    evidence_basis: source-backed card field dependency
    confidence: high
    canonical_cognee_edge: true
    marketplace_only: true
    canonical_edge_type: HAS_TABLE
    inverse_edge_type: BELONGS_TO_DOMAIN_OR_CONTEXT
    materialize_inverse: false
    edge_class: canonical
    source_type: platform_context
    target_type: table
    evidence_refs:
    - ev.walmart.table_summary.001
```

```yaml
candidate_edge:
  edge_id: edge.walmart.0011
  edge_type: HAS_TABLE
  source: platform_context.walmart.us
  target: table.zs_observe.walmart_lookup
  fields:
    edge_family: business_hierarchy_in_scope
    evidence_basis: source-backed card field dependency
    confidence: high
    canonical_cognee_edge: true
    marketplace_only: true
    canonical_edge_type: HAS_TABLE
    inverse_edge_type: BELONGS_TO_DOMAIN_OR_CONTEXT
    materialize_inverse: false
    edge_class: canonical
    source_type: platform_context
    target_type: table
    evidence_refs:
    - ev.walmart.table_summary.001
```

```yaml
candidate_edge:
  edge_id: edge.walmart.0012
  edge_type: HAS_TABLE
  source: domain.marketplace.walmart.orders
  target: table.zs_observe.walmart_oms
  fields:
    edge_family: business_hierarchy_in_scope
    evidence_basis: source-backed card field dependency
    confidence: high
    canonical_cognee_edge: true
    marketplace_only: true
    canonical_edge_type: HAS_TABLE
    inverse_edge_type: BELONGS_TO_DOMAIN_OR_CONTEXT
    materialize_inverse: false
    edge_class: canonical
    source_type: domain
    target_type: table
    evidence_refs:
    - ev.walmart_oms.schema.001
```

```yaml
candidate_edge:
  edge_id: edge.walmart.0013
  edge_type: HAS_TABLE
  source: domain.marketplace.walmart.settlement
  target: table.zs_observe.walmart_settlement
  fields:
    edge_family: business_hierarchy_in_scope
    evidence_basis: source-backed card field dependency
    confidence: high
    canonical_cognee_edge: true
    marketplace_only: true
    canonical_edge_type: HAS_TABLE
    inverse_edge_type: BELONGS_TO_DOMAIN_OR_CONTEXT
    materialize_inverse: false
    edge_class: canonical
    source_type: domain
    target_type: table
    evidence_refs:
    - ev.walmart_settlement.schema.001
```

```yaml
candidate_edge:
  edge_id: edge.walmart.0014
  edge_type: HAS_TABLE
  source: domain.marketplace.walmart.catalogue
  target: table.zs_observe.walmart_lookup
  fields:
    edge_family: business_hierarchy_in_scope
    evidence_basis: source-backed card field dependency
    confidence: high
    canonical_cognee_edge: true
    marketplace_only: true
    canonical_edge_type: HAS_TABLE
    inverse_edge_type: BELONGS_TO_DOMAIN_OR_CONTEXT
    materialize_inverse: false
    edge_class: canonical
    source_type: domain
    target_type: table
    evidence_refs:
    - ev.walmart_lookup.schema.001
```

```yaml
candidate_edge:
  edge_id: edge.walmart.0015
  edge_type: HAS_COLUMN
  source: table.zs_observe.walmart_oms
  target: column.zs_observe.walmart_oms.unique_id
  fields:
    edge_family: business_hierarchy_in_scope
    evidence_basis: source-backed card field dependency
    confidence: high
    canonical_cognee_edge: true
    marketplace_only: true
    canonical_edge_type: HAS_COLUMN
    inverse_edge_type: BELONGS_TO_TABLE
    materialize_inverse: false
    edge_class: canonical
    source_type: table
    target_type: column
```

```yaml
candidate_edge:
  edge_id: edge.walmart.0016
  edge_type: HAS_COLUMN
  source: table.zs_observe.walmart_oms
  target: column.zs_observe.walmart_oms.txn_uuid
  fields:
    edge_family: business_hierarchy_in_scope
    evidence_basis: source-backed card field dependency
    confidence: high
    canonical_cognee_edge: true
    marketplace_only: true
    canonical_edge_type: HAS_COLUMN
    inverse_edge_type: BELONGS_TO_TABLE
    materialize_inverse: false
    edge_class: canonical
    source_type: table
    target_type: column
```

```yaml
candidate_edge:
  edge_id: edge.walmart.0017
  edge_type: HAS_COLUMN
  source: table.zs_observe.walmart_oms
  target: column.zs_observe.walmart_oms.unique_value
  fields:
    edge_family: business_hierarchy_in_scope
    evidence_basis: source-backed card field dependency
    confidence: high
    canonical_cognee_edge: true
    marketplace_only: true
    canonical_edge_type: HAS_COLUMN
    inverse_edge_type: BELONGS_TO_TABLE
    materialize_inverse: false
    edge_class: canonical
    source_type: table
    target_type: column
```

```yaml
candidate_edge:
  edge_id: edge.walmart.0018
  edge_type: HAS_COLUMN
  source: table.zs_observe.walmart_oms
  target: column.zs_observe.walmart_oms.order_id
  fields:
    edge_family: business_hierarchy_in_scope
    evidence_basis: source-backed card field dependency
    confidence: high
    canonical_cognee_edge: true
    marketplace_only: true
    canonical_edge_type: HAS_COLUMN
    inverse_edge_type: BELONGS_TO_TABLE
    materialize_inverse: false
    edge_class: canonical
    source_type: table
    target_type: column
```

```yaml
candidate_edge:
  edge_id: edge.walmart.0019
  edge_type: HAS_COLUMN
  source: table.zs_observe.walmart_oms
  target: column.zs_observe.walmart_oms.parent_id
  fields:
    edge_family: business_hierarchy_in_scope
    evidence_basis: source-backed card field dependency
    confidence: high
    canonical_cognee_edge: true
    marketplace_only: true
    canonical_edge_type: HAS_COLUMN
    inverse_edge_type: BELONGS_TO_TABLE
    materialize_inverse: false
    edge_class: canonical
    source_type: table
    target_type: column
```

```yaml
candidate_edge:
  edge_id: edge.walmart.0020
  edge_type: HAS_COLUMN
  source: table.zs_observe.walmart_oms
  target: column.zs_observe.walmart_oms.item_id
  fields:
    edge_family: business_hierarchy_in_scope
    evidence_basis: source-backed card field dependency
    confidence: high
    canonical_cognee_edge: true
    marketplace_only: true
    canonical_edge_type: HAS_COLUMN
    inverse_edge_type: BELONGS_TO_TABLE
    materialize_inverse: false
    edge_class: canonical
    source_type: table
    target_type: column
```

```yaml
candidate_edge:
  edge_id: edge.walmart.0021
  edge_type: HAS_COLUMN
  source: table.zs_observe.walmart_oms
  target: column.zs_observe.walmart_oms.mp_sin
  fields:
    edge_family: business_hierarchy_in_scope
    evidence_basis: source-backed card field dependency
    confidence: high
    canonical_cognee_edge: true
    marketplace_only: true
    canonical_edge_type: HAS_COLUMN
    inverse_edge_type: BELONGS_TO_TABLE
    materialize_inverse: false
    edge_class: canonical
    source_type: table
    target_type: column
```

```yaml
candidate_edge:
  edge_id: edge.walmart.0022
  edge_type: HAS_COLUMN
  source: table.zs_observe.walmart_oms
  target: column.zs_observe.walmart_oms.sku_id
  fields:
    edge_family: business_hierarchy_in_scope
    evidence_basis: source-backed card field dependency
    confidence: high
    canonical_cognee_edge: true
    marketplace_only: true
    canonical_edge_type: HAS_COLUMN
    inverse_edge_type: BELONGS_TO_TABLE
    materialize_inverse: false
    edge_class: canonical
    source_type: table
    target_type: column
```

```yaml
candidate_edge:
  edge_id: edge.walmart.0023
  edge_type: HAS_COLUMN
  source: table.zs_observe.walmart_oms
  target: column.zs_observe.walmart_oms.created_date
  fields:
    edge_family: business_hierarchy_in_scope
    evidence_basis: source-backed card field dependency
    confidence: high
    canonical_cognee_edge: true
    marketplace_only: true
    canonical_edge_type: HAS_COLUMN
    inverse_edge_type: BELONGS_TO_TABLE
    materialize_inverse: false
    edge_class: canonical
    source_type: table
    target_type: column
```

```yaml
candidate_edge:
  edge_id: edge.walmart.0024
  edge_type: HAS_COLUMN
  source: table.zs_observe.walmart_oms
  target: column.zs_observe.walmart_oms.shipped_date
  fields:
    edge_family: business_hierarchy_in_scope
    evidence_basis: source-backed card field dependency
    confidence: high
    canonical_cognee_edge: true
    marketplace_only: true
    canonical_edge_type: HAS_COLUMN
    inverse_edge_type: BELONGS_TO_TABLE
    materialize_inverse: false
    edge_class: canonical
    source_type: table
    target_type: column
```

```yaml
candidate_edge:
  edge_id: edge.walmart.0025
  edge_type: HAS_COLUMN
  source: table.zs_observe.walmart_oms
  target: column.zs_observe.walmart_oms.metadata_2
  fields:
    edge_family: business_hierarchy_in_scope
    evidence_basis: source-backed card field dependency
    confidence: high
    canonical_cognee_edge: true
    marketplace_only: true
    canonical_edge_type: HAS_COLUMN
    inverse_edge_type: BELONGS_TO_TABLE
    materialize_inverse: false
    edge_class: canonical
    source_type: table
    target_type: column
```

```yaml
candidate_edge:
  edge_id: edge.walmart.0026
  edge_type: HAS_COLUMN
  source: table.zs_observe.walmart_oms
  target: column.zs_observe.walmart_oms.charged_amount
  fields:
    edge_family: business_hierarchy_in_scope
    evidence_basis: source-backed card field dependency
    confidence: high
    canonical_cognee_edge: true
    marketplace_only: true
    canonical_edge_type: HAS_COLUMN
    inverse_edge_type: BELONGS_TO_TABLE
    materialize_inverse: false
    edge_class: canonical
    source_type: table
    target_type: column
```

```yaml
candidate_edge:
  edge_id: edge.walmart.0027
  edge_type: HAS_COLUMN
  source: table.zs_observe.walmart_oms
  target: column.zs_observe.walmart_oms.quantity
  fields:
    edge_family: business_hierarchy_in_scope
    evidence_basis: source-backed card field dependency
    confidence: high
    canonical_cognee_edge: true
    marketplace_only: true
    canonical_edge_type: HAS_COLUMN
    inverse_edge_type: BELONGS_TO_TABLE
    materialize_inverse: false
    edge_class: canonical
    source_type: table
    target_type: column
```

```yaml
candidate_edge:
  edge_id: edge.walmart.0028
  edge_type: HAS_COLUMN
  source: table.zs_observe.walmart_oms
  target: column.zs_observe.walmart_oms.internal_txn_type
  fields:
    edge_family: business_hierarchy_in_scope
    evidence_basis: source-backed card field dependency
    confidence: high
    canonical_cognee_edge: true
    marketplace_only: true
    canonical_edge_type: HAS_COLUMN
    inverse_edge_type: BELONGS_TO_TABLE
    materialize_inverse: false
    edge_class: canonical
    source_type: table
    target_type: column
```

```yaml
candidate_edge:
  edge_id: edge.walmart.0029
  edge_type: HAS_COLUMN
  source: table.zs_observe.walmart_oms
  target: column.zs_observe.walmart_oms.order_status
  fields:
    edge_family: business_hierarchy_in_scope
    evidence_basis: source-backed card field dependency
    confidence: high
    canonical_cognee_edge: true
    marketplace_only: true
    canonical_edge_type: HAS_COLUMN
    inverse_edge_type: BELONGS_TO_TABLE
    materialize_inverse: false
    edge_class: canonical
    source_type: table
    target_type: column
```

```yaml
candidate_edge:
  edge_id: edge.walmart.0030
  edge_type: HAS_COLUMN
  source: table.zs_observe.walmart_oms
  target: column.zs_observe.walmart_oms.destination_state
  fields:
    edge_family: business_hierarchy_in_scope
    evidence_basis: source-backed card field dependency
    confidence: high
    canonical_cognee_edge: true
    marketplace_only: true
    canonical_edge_type: HAS_COLUMN
    inverse_edge_type: BELONGS_TO_TABLE
    materialize_inverse: false
    edge_class: canonical
    source_type: table
    target_type: column
```

```yaml
candidate_edge:
  edge_id: edge.walmart.0031
  edge_type: HAS_COLUMN
  source: table.zs_observe.walmart_oms
  target: column.zs_observe.walmart_oms.destination_city
  fields:
    edge_family: business_hierarchy_in_scope
    evidence_basis: source-backed card field dependency
    confidence: high
    canonical_cognee_edge: true
    marketplace_only: true
    canonical_edge_type: HAS_COLUMN
    inverse_edge_type: BELONGS_TO_TABLE
    materialize_inverse: false
    edge_class: canonical
    source_type: table
    target_type: column
```

```yaml
candidate_edge:
  edge_id: edge.walmart.0032
  edge_type: HAS_COLUMN
  source: table.zs_observe.walmart_oms
  target: column.zs_observe.walmart_oms.source_zipcode
  fields:
    edge_family: business_hierarchy_in_scope
    evidence_basis: source-backed card field dependency
    confidence: high
    canonical_cognee_edge: true
    marketplace_only: true
    canonical_edge_type: HAS_COLUMN
    inverse_edge_type: BELONGS_TO_TABLE
    materialize_inverse: false
    edge_class: canonical
    source_type: table
    target_type: column
```

```yaml
candidate_edge:
  edge_id: edge.walmart.0033
  edge_type: HAS_COLUMN
  source: table.zs_observe.walmart_oms
  target: column.zs_observe.walmart_oms.item_name
  fields:
    edge_family: business_hierarchy_in_scope
    evidence_basis: source-backed card field dependency
    confidence: high
    canonical_cognee_edge: true
    marketplace_only: true
    canonical_edge_type: HAS_COLUMN
    inverse_edge_type: BELONGS_TO_TABLE
    materialize_inverse: false
    edge_class: canonical
    source_type: table
    target_type: column
```

```yaml
candidate_edge:
  edge_id: edge.walmart.0034
  edge_type: HAS_COLUMN
  source: table.zs_observe.walmart_oms
  target: column.zs_observe.walmart_oms.hsn
  fields:
    edge_family: business_hierarchy_in_scope
    evidence_basis: source-backed card field dependency
    confidence: high
    canonical_cognee_edge: true
    marketplace_only: true
    canonical_edge_type: HAS_COLUMN
    inverse_edge_type: BELONGS_TO_TABLE
    materialize_inverse: false
    edge_class: canonical
    source_type: table
    target_type: column
```

```yaml
candidate_edge:
  edge_id: edge.walmart.0035
  edge_type: HAS_COLUMN
  source: table.zs_observe.walmart_oms
  target: column.zs_observe.walmart_oms.group_level_id
  fields:
    edge_family: business_hierarchy_in_scope
    evidence_basis: source-backed card field dependency
    confidence: high
    canonical_cognee_edge: true
    marketplace_only: true
    canonical_edge_type: HAS_COLUMN
    inverse_edge_type: BELONGS_TO_TABLE
    materialize_inverse: false
    edge_class: canonical
    source_type: table
    target_type: column
```

```yaml
candidate_edge:
  edge_id: edge.walmart.0036
  edge_type: HAS_COLUMN
  source: table.zs_observe.walmart_oms
  target: column.zs_observe.walmart_oms.currency_type
  fields:
    edge_family: business_hierarchy_in_scope
    evidence_basis: source-backed card field dependency
    confidence: high
    canonical_cognee_edge: true
    marketplace_only: true
    canonical_edge_type: HAS_COLUMN
    inverse_edge_type: BELONGS_TO_TABLE
    materialize_inverse: false
    edge_class: canonical
    source_type: table
    target_type: column
```

```yaml
candidate_edge:
  edge_id: edge.walmart.0037
  edge_type: HAS_COLUMN
  source: table.zs_observe.walmart_oms
  target: column.zs_observe.walmart_oms.is_active
  fields:
    edge_family: business_hierarchy_in_scope
    evidence_basis: source-backed card field dependency
    confidence: high
    canonical_cognee_edge: true
    marketplace_only: true
    canonical_edge_type: HAS_COLUMN
    inverse_edge_type: BELONGS_TO_TABLE
    materialize_inverse: false
    edge_class: canonical
    source_type: table
    target_type: column
```

```yaml
candidate_edge:
  edge_id: edge.walmart.0038
  edge_type: HAS_COLUMN
  source: table.zs_observe.walmart_oms
  target: column.zs_observe.walmart_oms.zen_sheet_name
  fields:
    edge_family: business_hierarchy_in_scope
    evidence_basis: source-backed card field dependency
    confidence: high
    canonical_cognee_edge: true
    marketplace_only: true
    canonical_edge_type: HAS_COLUMN
    inverse_edge_type: BELONGS_TO_TABLE
    materialize_inverse: false
    edge_class: canonical
    source_type: table
    target_type: column
```

```yaml
candidate_edge:
  edge_id: edge.walmart.0039
  edge_type: HAS_COLUMN
  source: table.zs_observe.walmart_oms
  target: column.zs_observe.walmart_oms.created_at
  fields:
    edge_family: business_hierarchy_in_scope
    evidence_basis: source-backed card field dependency
    confidence: high
    canonical_cognee_edge: true
    marketplace_only: true
    canonical_edge_type: HAS_COLUMN
    inverse_edge_type: BELONGS_TO_TABLE
    materialize_inverse: false
    edge_class: canonical
    source_type: table
    target_type: column
```

```yaml
candidate_edge:
  edge_id: edge.walmart.0040
  edge_type: HAS_COLUMN
  source: table.zs_observe.walmart_oms
  target: column.zs_observe.walmart_oms.updated_at
  fields:
    edge_family: business_hierarchy_in_scope
    evidence_basis: source-backed card field dependency
    confidence: high
    canonical_cognee_edge: true
    marketplace_only: true
    canonical_edge_type: HAS_COLUMN
    inverse_edge_type: BELONGS_TO_TABLE
    materialize_inverse: false
    edge_class: canonical
    source_type: table
    target_type: column
```

```yaml
candidate_edge:
  edge_id: edge.walmart.0041
  edge_type: HAS_COLUMN
  source: table.zs_observe.walmart_oms
  target: column.zs_observe.walmart_oms.deleted_at
  fields:
    edge_family: business_hierarchy_in_scope
    evidence_basis: source-backed card field dependency
    confidence: high
    canonical_cognee_edge: true
    marketplace_only: true
    canonical_edge_type: HAS_COLUMN
    inverse_edge_type: BELONGS_TO_TABLE
    materialize_inverse: false
    edge_class: canonical
    source_type: table
    target_type: column
```

```yaml
candidate_edge:
  edge_id: edge.walmart.0042
  edge_type: HAS_COLUMN
  source: table.zs_observe.walmart_settlement
  target: column.zs_observe.walmart_settlement.unique_id
  fields:
    edge_family: business_hierarchy_in_scope
    evidence_basis: source-backed card field dependency
    confidence: high
    canonical_cognee_edge: true
    marketplace_only: true
    canonical_edge_type: HAS_COLUMN
    inverse_edge_type: BELONGS_TO_TABLE
    materialize_inverse: false
    edge_class: canonical
    source_type: table
    target_type: column
```

```yaml
candidate_edge:
  edge_id: edge.walmart.0043
  edge_type: HAS_COLUMN
  source: table.zs_observe.walmart_settlement
  target: column.zs_observe.walmart_settlement.txn_uuid
  fields:
    edge_family: business_hierarchy_in_scope
    evidence_basis: source-backed card field dependency
    confidence: high
    canonical_cognee_edge: true
    marketplace_only: true
    canonical_edge_type: HAS_COLUMN
    inverse_edge_type: BELONGS_TO_TABLE
    materialize_inverse: false
    edge_class: canonical
    source_type: table
    target_type: column
```

```yaml
candidate_edge:
  edge_id: edge.walmart.0044
  edge_type: HAS_COLUMN
  source: table.zs_observe.walmart_settlement
  target: column.zs_observe.walmart_settlement.unique_value
  fields:
    edge_family: business_hierarchy_in_scope
    evidence_basis: source-backed card field dependency
    confidence: high
    canonical_cognee_edge: true
    marketplace_only: true
    canonical_edge_type: HAS_COLUMN
    inverse_edge_type: BELONGS_TO_TABLE
    materialize_inverse: false
    edge_class: canonical
    source_type: table
    target_type: column
```

```yaml
candidate_edge:
  edge_id: edge.walmart.0045
  edge_type: HAS_COLUMN
  source: table.zs_observe.walmart_settlement
  target: column.zs_observe.walmart_settlement.order_id
  fields:
    edge_family: business_hierarchy_in_scope
    evidence_basis: source-backed card field dependency
    confidence: high
    canonical_cognee_edge: true
    marketplace_only: true
    canonical_edge_type: HAS_COLUMN
    inverse_edge_type: BELONGS_TO_TABLE
    materialize_inverse: false
    edge_class: canonical
    source_type: table
    target_type: column
```

```yaml
candidate_edge:
  edge_id: edge.walmart.0046
  edge_type: HAS_COLUMN
  source: table.zs_observe.walmart_settlement
  target: column.zs_observe.walmart_settlement.parent_id
  fields:
    edge_family: business_hierarchy_in_scope
    evidence_basis: source-backed card field dependency
    confidence: high
    canonical_cognee_edge: true
    marketplace_only: true
    canonical_edge_type: HAS_COLUMN
    inverse_edge_type: BELONGS_TO_TABLE
    materialize_inverse: false
    edge_class: canonical
    source_type: table
    target_type: column
```

```yaml
candidate_edge:
  edge_id: edge.walmart.0047
  edge_type: HAS_COLUMN
  source: table.zs_observe.walmart_settlement
  target: column.zs_observe.walmart_settlement.sku_id
  fields:
    edge_family: business_hierarchy_in_scope
    evidence_basis: source-backed card field dependency
    confidence: high
    canonical_cognee_edge: true
    marketplace_only: true
    canonical_edge_type: HAS_COLUMN
    inverse_edge_type: BELONGS_TO_TABLE
    materialize_inverse: false
    edge_class: canonical
    source_type: table
    target_type: column
```

```yaml
candidate_edge:
  edge_id: edge.walmart.0048
  edge_type: HAS_COLUMN
  source: table.zs_observe.walmart_settlement
  target: column.zs_observe.walmart_settlement.partner_gtin
  fields:
    edge_family: business_hierarchy_in_scope
    evidence_basis: source-backed card field dependency
    confidence: high
    canonical_cognee_edge: true
    marketplace_only: true
    canonical_edge_type: HAS_COLUMN
    inverse_edge_type: BELONGS_TO_TABLE
    materialize_inverse: false
    edge_class: canonical
    source_type: table
    target_type: column
```

```yaml
candidate_edge:
  edge_id: edge.walmart.0049
  edge_type: HAS_COLUMN
  source: table.zs_observe.walmart_settlement
  target: column.zs_observe.walmart_settlement.partner_item_id
  fields:
    edge_family: business_hierarchy_in_scope
    evidence_basis: source-backed card field dependency
    confidence: high
    canonical_cognee_edge: true
    marketplace_only: true
    canonical_edge_type: HAS_COLUMN
    inverse_edge_type: BELONGS_TO_TABLE
    materialize_inverse: false
    edge_class: canonical
    source_type: table
    target_type: column
```

```yaml
candidate_edge:
  edge_id: edge.walmart.0050
  edge_type: HAS_COLUMN
  source: table.zs_observe.walmart_settlement
  target: column.zs_observe.walmart_settlement.partner_item_name
  fields:
    edge_family: business_hierarchy_in_scope
    evidence_basis: source-backed card field dependency
    confidence: high
    canonical_cognee_edge: true
    marketplace_only: true
    canonical_edge_type: HAS_COLUMN
    inverse_edge_type: BELONGS_TO_TABLE
    materialize_inverse: false
    edge_class: canonical
    source_type: table
    target_type: column
```

```yaml
candidate_edge:
  edge_id: edge.walmart.0051
  edge_type: HAS_COLUMN
  source: table.zs_observe.walmart_settlement
  target: column.zs_observe.walmart_settlement.created_date
  fields:
    edge_family: business_hierarchy_in_scope
    evidence_basis: source-backed card field dependency
    confidence: high
    canonical_cognee_edge: true
    marketplace_only: true
    canonical_edge_type: HAS_COLUMN
    inverse_edge_type: BELONGS_TO_TABLE
    materialize_inverse: false
    edge_class: canonical
    source_type: table
    target_type: column
```

```yaml
candidate_edge:
  edge_id: edge.walmart.0052
  edge_type: HAS_COLUMN
  source: table.zs_observe.walmart_settlement
  target: column.zs_observe.walmart_settlement.metadata_2
  fields:
    edge_family: business_hierarchy_in_scope
    evidence_basis: source-backed card field dependency
    confidence: high
    canonical_cognee_edge: true
    marketplace_only: true
    canonical_edge_type: HAS_COLUMN
    inverse_edge_type: BELONGS_TO_TABLE
    materialize_inverse: false
    edge_class: canonical
    source_type: table
    target_type: column
```

```yaml
candidate_edge:
  edge_id: edge.walmart.0053
  edge_type: HAS_COLUMN
  source: table.zs_observe.walmart_settlement
  target: column.zs_observe.walmart_settlement.metadata_3
  fields:
    edge_family: business_hierarchy_in_scope
    evidence_basis: source-backed card field dependency
    confidence: high
    canonical_cognee_edge: true
    marketplace_only: true
    canonical_edge_type: HAS_COLUMN
    inverse_edge_type: BELONGS_TO_TABLE
    materialize_inverse: false
    edge_class: canonical
    source_type: table
    target_type: column
```

```yaml
candidate_edge:
  edge_id: edge.walmart.0054
  edge_type: HAS_COLUMN
  source: table.zs_observe.walmart_settlement
  target: column.zs_observe.walmart_settlement.period_start_date
  fields:
    edge_family: business_hierarchy_in_scope
    evidence_basis: source-backed card field dependency
    confidence: high
    canonical_cognee_edge: true
    marketplace_only: true
    canonical_edge_type: HAS_COLUMN
    inverse_edge_type: BELONGS_TO_TABLE
    materialize_inverse: false
    edge_class: canonical
    source_type: table
    target_type: column
```

```yaml
candidate_edge:
  edge_id: edge.walmart.0055
  edge_type: HAS_COLUMN
  source: table.zs_observe.walmart_settlement
  target: column.zs_observe.walmart_settlement.period_end_date
  fields:
    edge_family: business_hierarchy_in_scope
    evidence_basis: source-backed card field dependency
    confidence: high
    canonical_cognee_edge: true
    marketplace_only: true
    canonical_edge_type: HAS_COLUMN
    inverse_edge_type: BELONGS_TO_TABLE
    materialize_inverse: false
    edge_class: canonical
    source_type: table
    target_type: column
```

```yaml
candidate_edge:
  edge_id: edge.walmart.0056
  edge_type: HAS_COLUMN
  source: table.zs_observe.walmart_settlement
  target: column.zs_observe.walmart_settlement.transaction_posted_timestamp
  fields:
    edge_family: business_hierarchy_in_scope
    evidence_basis: source-backed card field dependency
    confidence: high
    canonical_cognee_edge: true
    marketplace_only: true
    canonical_edge_type: HAS_COLUMN
    inverse_edge_type: BELONGS_TO_TABLE
    materialize_inverse: false
    edge_class: canonical
    source_type: table
    target_type: column
```

```yaml
candidate_edge:
  edge_id: edge.walmart.0057
  edge_type: HAS_COLUMN
  source: table.zs_observe.walmart_settlement
  target: column.zs_observe.walmart_settlement.charged_amount
  fields:
    edge_family: business_hierarchy_in_scope
    evidence_basis: source-backed card field dependency
    confidence: high
    canonical_cognee_edge: true
    marketplace_only: true
    canonical_edge_type: HAS_COLUMN
    inverse_edge_type: BELONGS_TO_TABLE
    materialize_inverse: false
    edge_class: canonical
    source_type: table
    target_type: column
```

```yaml
candidate_edge:
  edge_id: edge.walmart.0058
  edge_type: HAS_COLUMN
  source: table.zs_observe.walmart_settlement
  target: column.zs_observe.walmart_settlement.charged_amount_excluding_tax
  fields:
    edge_family: business_hierarchy_in_scope
    evidence_basis: source-backed card field dependency
    confidence: high
    canonical_cognee_edge: true
    marketplace_only: true
    canonical_edge_type: HAS_COLUMN
    inverse_edge_type: BELONGS_TO_TABLE
    materialize_inverse: false
    edge_class: canonical
    source_type: table
    target_type: column
```

```yaml
candidate_edge:
  edge_id: edge.walmart.0059
  edge_type: HAS_COLUMN
  source: table.zs_observe.walmart_settlement
  target: column.zs_observe.walmart_settlement.total_tax
  fields:
    edge_family: business_hierarchy_in_scope
    evidence_basis: source-backed card field dependency
    confidence: high
    canonical_cognee_edge: true
    marketplace_only: true
    canonical_edge_type: HAS_COLUMN
    inverse_edge_type: BELONGS_TO_TABLE
    materialize_inverse: false
    edge_class: canonical
    source_type: table
    target_type: column
```

```yaml
candidate_edge:
  edge_id: edge.walmart.0060
  edge_type: HAS_COLUMN
  source: table.zs_observe.walmart_settlement
  target: column.zs_observe.walmart_settlement.gross_commission
  fields:
    edge_family: business_hierarchy_in_scope
    evidence_basis: source-backed card field dependency
    confidence: high
    canonical_cognee_edge: true
    marketplace_only: true
    canonical_edge_type: HAS_COLUMN
    inverse_edge_type: BELONGS_TO_TABLE
    materialize_inverse: false
    edge_class: canonical
    source_type: table
    target_type: column
```

```yaml
candidate_edge:
  edge_id: edge.walmart.0061
  edge_type: HAS_COLUMN
  source: table.zs_observe.walmart_settlement
  target: column.zs_observe.walmart_settlement.marketplace_withheld_tax
  fields:
    edge_family: business_hierarchy_in_scope
    evidence_basis: source-backed card field dependency
    confidence: high
    canonical_cognee_edge: true
    marketplace_only: true
    canonical_edge_type: HAS_COLUMN
    inverse_edge_type: BELONGS_TO_TABLE
    materialize_inverse: false
    edge_class: canonical
    source_type: table
    target_type: column
```

```yaml
candidate_edge:
  edge_id: edge.walmart.0062
  edge_type: HAS_COLUMN
  source: table.zs_observe.walmart_settlement
  target: column.zs_observe.walmart_settlement.settled_amount
  fields:
    edge_family: business_hierarchy_in_scope
    evidence_basis: source-backed card field dependency
    confidence: high
    canonical_cognee_edge: true
    marketplace_only: true
    canonical_edge_type: HAS_COLUMN
    inverse_edge_type: BELONGS_TO_TABLE
    materialize_inverse: false
    edge_class: canonical
    source_type: table
    target_type: column
```

```yaml
candidate_edge:
  edge_id: edge.walmart.0063
  edge_type: HAS_COLUMN
  source: table.zs_observe.walmart_settlement
  target: column.zs_observe.walmart_settlement.total_walmart_funded_savings
  fields:
    edge_family: business_hierarchy_in_scope
    evidence_basis: source-backed card field dependency
    confidence: high
    canonical_cognee_edge: true
    marketplace_only: true
    canonical_edge_type: HAS_COLUMN
    inverse_edge_type: BELONGS_TO_TABLE
    materialize_inverse: false
    edge_class: canonical
    source_type: table
    target_type: column
```

```yaml
candidate_edge:
  edge_id: edge.walmart.0064
  edge_type: HAS_COLUMN
  source: table.zs_observe.walmart_settlement
  target: column.zs_observe.walmart_settlement.charge_savings
  fields:
    edge_family: business_hierarchy_in_scope
    evidence_basis: source-backed card field dependency
    confidence: high
    canonical_cognee_edge: true
    marketplace_only: true
    canonical_edge_type: HAS_COLUMN
    inverse_edge_type: BELONGS_TO_TABLE
    materialize_inverse: false
    edge_class: canonical
    source_type: table
    target_type: column
```

```yaml
candidate_edge:
  edge_id: edge.walmart.0065
  edge_type: HAS_COLUMN
  source: table.zs_observe.walmart_settlement
  target: column.zs_observe.walmart_settlement.original_charge
  fields:
    edge_family: business_hierarchy_in_scope
    evidence_basis: source-backed card field dependency
    confidence: high
    canonical_cognee_edge: true
    marketplace_only: true
    canonical_edge_type: HAS_COLUMN
    inverse_edge_type: BELONGS_TO_TABLE
    materialize_inverse: false
    edge_class: canonical
    source_type: table
    target_type: column
```

```yaml
candidate_edge:
  edge_id: edge.walmart.0066
  edge_type: HAS_COLUMN
  source: table.zs_observe.walmart_settlement
  target: column.zs_observe.walmart_settlement.other_tax_fees
  fields:
    edge_family: business_hierarchy_in_scope
    evidence_basis: source-backed card field dependency
    confidence: high
    canonical_cognee_edge: true
    marketplace_only: true
    canonical_edge_type: HAS_COLUMN
    inverse_edge_type: BELONGS_TO_TABLE
    materialize_inverse: false
    edge_class: canonical
    source_type: table
    target_type: column
```

```yaml
candidate_edge:
  edge_id: edge.walmart.0067
  edge_type: HAS_COLUMN
  source: table.zs_observe.walmart_settlement
  target: column.zs_observe.walmart_settlement.total_amount_computed
  fields:
    edge_family: business_hierarchy_in_scope
    evidence_basis: source-backed card field dependency
    confidence: high
    canonical_cognee_edge: true
    marketplace_only: true
    canonical_edge_type: HAS_COLUMN
    inverse_edge_type: BELONGS_TO_TABLE
    materialize_inverse: false
    edge_class: canonical
    source_type: table
    target_type: column
```

```yaml
candidate_edge:
  edge_id: edge.walmart.0068
  edge_type: HAS_COLUMN
  source: table.zs_observe.walmart_settlement
  target: column.zs_observe.walmart_settlement.promo_code
  fields:
    edge_family: business_hierarchy_in_scope
    evidence_basis: source-backed card field dependency
    confidence: high
    canonical_cognee_edge: true
    marketplace_only: true
    canonical_edge_type: HAS_COLUMN
    inverse_edge_type: BELONGS_TO_TABLE
    materialize_inverse: false
    edge_class: canonical
    source_type: table
    target_type: column
```

```yaml
candidate_edge:
  edge_id: edge.walmart.0069
  edge_type: HAS_COLUMN
  source: table.zs_observe.walmart_settlement
  target: column.zs_observe.walmart_settlement.product_price
  fields:
    edge_family: business_hierarchy_in_scope
    evidence_basis: source-backed card field dependency
    confidence: high
    canonical_cognee_edge: true
    marketplace_only: true
    canonical_edge_type: HAS_COLUMN
    inverse_edge_type: BELONGS_TO_TABLE
    materialize_inverse: false
    edge_class: canonical
    source_type: table
    target_type: column
```

```yaml
candidate_edge:
  edge_id: edge.walmart.0070
  edge_type: HAS_COLUMN
  source: table.zs_observe.walmart_settlement
  target: column.zs_observe.walmart_settlement.product_tax
  fields:
    edge_family: business_hierarchy_in_scope
    evidence_basis: source-backed card field dependency
    confidence: high
    canonical_cognee_edge: true
    marketplace_only: true
    canonical_edge_type: HAS_COLUMN
    inverse_edge_type: BELONGS_TO_TABLE
    materialize_inverse: false
    edge_class: canonical
    source_type: table
    target_type: column
```

```yaml
candidate_edge:
  edge_id: edge.walmart.0071
  edge_type: HAS_COLUMN
  source: table.zs_observe.walmart_settlement
  target: column.zs_observe.walmart_settlement.product_tax_withheld
  fields:
    edge_family: business_hierarchy_in_scope
    evidence_basis: source-backed card field dependency
    confidence: high
    canonical_cognee_edge: true
    marketplace_only: true
    canonical_edge_type: HAS_COLUMN
    inverse_edge_type: BELONGS_TO_TABLE
    materialize_inverse: false
    edge_class: canonical
    source_type: table
    target_type: column
```

```yaml
candidate_edge:
  edge_id: edge.walmart.0072
  edge_type: HAS_COLUMN
  source: table.zs_observe.walmart_settlement
  target: column.zs_observe.walmart_settlement.total_payable
  fields:
    edge_family: business_hierarchy_in_scope
    evidence_basis: source-backed card field dependency
    confidence: high
    canonical_cognee_edge: true
    marketplace_only: true
    canonical_edge_type: HAS_COLUMN
    inverse_edge_type: BELONGS_TO_TABLE
    materialize_inverse: false
    edge_class: canonical
    source_type: table
    target_type: column
```

```yaml
candidate_edge:
  edge_id: edge.walmart.0073
  edge_type: HAS_COLUMN
  source: table.zs_observe.walmart_settlement
  target: column.zs_observe.walmart_settlement.wfs_inventory_fee_reimbursement
  fields:
    edge_family: business_hierarchy_in_scope
    evidence_basis: source-backed card field dependency
    confidence: high
    canonical_cognee_edge: true
    marketplace_only: true
    canonical_edge_type: HAS_COLUMN
    inverse_edge_type: BELONGS_TO_TABLE
    materialize_inverse: false
    edge_class: canonical
    source_type: table
    target_type: column
```

```yaml
candidate_edge:
  edge_id: edge.walmart.0074
  edge_type: HAS_COLUMN
  source: table.zs_observe.walmart_settlement
  target: column.zs_observe.walmart_settlement.fee_reimbursement
  fields:
    edge_family: business_hierarchy_in_scope
    evidence_basis: source-backed card field dependency
    confidence: high
    canonical_cognee_edge: true
    marketplace_only: true
    canonical_edge_type: HAS_COLUMN
    inverse_edge_type: BELONGS_TO_TABLE
    materialize_inverse: false
    edge_class: canonical
    source_type: table
    target_type: column
```

```yaml
candidate_edge:
  edge_id: edge.walmart.0075
  edge_type: HAS_COLUMN
  source: table.zs_observe.walmart_settlement
  target: column.zs_observe.walmart_settlement.wfs_fee_reimbursement
  fields:
    edge_family: business_hierarchy_in_scope
    evidence_basis: source-backed card field dependency
    confidence: high
    canonical_cognee_edge: true
    marketplace_only: true
    canonical_edge_type: HAS_COLUMN
    inverse_edge_type: BELONGS_TO_TABLE
    materialize_inverse: false
    edge_class: canonical
    source_type: table
    target_type: column
```

```yaml
candidate_edge:
  edge_id: edge.walmart.0076
  edge_type: HAS_COLUMN
  source: table.zs_observe.walmart_settlement
  target: column.zs_observe.walmart_settlement.wfs_inbound_fee
  fields:
    edge_family: business_hierarchy_in_scope
    evidence_basis: source-backed card field dependency
    confidence: high
    canonical_cognee_edge: true
    marketplace_only: true
    canonical_edge_type: HAS_COLUMN
    inverse_edge_type: BELONGS_TO_TABLE
    materialize_inverse: false
    edge_class: canonical
    source_type: table
    target_type: column
```

```yaml
candidate_edge:
  edge_id: edge.walmart.0077
  edge_type: HAS_COLUMN
  source: table.zs_observe.walmart_settlement
  target: column.zs_observe.walmart_settlement.sem_marketing_fee
  fields:
    edge_family: business_hierarchy_in_scope
    evidence_basis: source-backed card field dependency
    confidence: high
    canonical_cognee_edge: true
    marketplace_only: true
    canonical_edge_type: HAS_COLUMN
    inverse_edge_type: BELONGS_TO_TABLE
    materialize_inverse: false
    edge_class: canonical
    source_type: table
    target_type: column
```

```yaml
candidate_edge:
  edge_id: edge.walmart.0078
  edge_type: HAS_COLUMN
  source: table.zs_observe.walmart_settlement
  target: column.zs_observe.walmart_settlement.transaction_type
  fields:
    edge_family: business_hierarchy_in_scope
    evidence_basis: source-backed card field dependency
    confidence: high
    canonical_cognee_edge: true
    marketplace_only: true
    canonical_edge_type: HAS_COLUMN
    inverse_edge_type: BELONGS_TO_TABLE
    materialize_inverse: false
    edge_class: canonical
    source_type: table
    target_type: column
```

```yaml
candidate_edge:
  edge_id: edge.walmart.0079
  edge_type: HAS_COLUMN
  source: table.zs_observe.walmart_settlement
  target: column.zs_observe.walmart_settlement.internal_txn_type
  fields:
    edge_family: business_hierarchy_in_scope
    evidence_basis: source-backed card field dependency
    confidence: high
    canonical_cognee_edge: true
    marketplace_only: true
    canonical_edge_type: HAS_COLUMN
    inverse_edge_type: BELONGS_TO_TABLE
    materialize_inverse: false
    edge_class: canonical
    source_type: table
    target_type: column
```

```yaml
candidate_edge:
  edge_id: edge.walmart.0080
  edge_type: HAS_COLUMN
  source: table.zs_observe.walmart_settlement
  target: column.zs_observe.walmart_settlement.other_type
  fields:
    edge_family: business_hierarchy_in_scope
    evidence_basis: source-backed card field dependency
    confidence: high
    canonical_cognee_edge: true
    marketplace_only: true
    canonical_edge_type: HAS_COLUMN
    inverse_edge_type: BELONGS_TO_TABLE
    materialize_inverse: false
    edge_class: canonical
    source_type: table
    target_type: column
```

```yaml
candidate_edge:
  edge_id: edge.walmart.0081
  edge_type: HAS_COLUMN
  source: table.zs_observe.walmart_settlement
  target: column.zs_observe.walmart_settlement.transaction_description
  fields:
    edge_family: business_hierarchy_in_scope
    evidence_basis: source-backed card field dependency
    confidence: high
    canonical_cognee_edge: true
    marketplace_only: true
    canonical_edge_type: HAS_COLUMN
    inverse_edge_type: BELONGS_TO_TABLE
    materialize_inverse: false
    edge_class: canonical
    source_type: table
    target_type: column
```

```yaml
candidate_edge:
  edge_id: edge.walmart.0082
  edge_type: HAS_COLUMN
  source: table.zs_observe.walmart_settlement
  target: column.zs_observe.walmart_settlement.description
  fields:
    edge_family: business_hierarchy_in_scope
    evidence_basis: source-backed card field dependency
    confidence: high
    canonical_cognee_edge: true
    marketplace_only: true
    canonical_edge_type: HAS_COLUMN
    inverse_edge_type: BELONGS_TO_TABLE
    materialize_inverse: false
    edge_class: canonical
    source_type: table
    target_type: column
```

```yaml
candidate_edge:
  edge_id: edge.walmart.0083
  edge_type: HAS_COLUMN
  source: table.zs_observe.walmart_settlement
  target: column.zs_observe.walmart_settlement.fulfilment_channel
  fields:
    edge_family: business_hierarchy_in_scope
    evidence_basis: source-backed card field dependency
    confidence: high
    canonical_cognee_edge: true
    marketplace_only: true
    canonical_edge_type: HAS_COLUMN
    inverse_edge_type: BELONGS_TO_TABLE
    materialize_inverse: false
    edge_class: canonical
    source_type: table
    target_type: column
```

```yaml
candidate_edge:
  edge_id: edge.walmart.0084
  edge_type: HAS_COLUMN
  source: table.zs_observe.walmart_settlement
  target: column.zs_observe.walmart_settlement.fulfillment_type
  fields:
    edge_family: business_hierarchy_in_scope
    evidence_basis: source-backed card field dependency
    confidence: high
    canonical_cognee_edge: true
    marketplace_only: true
    canonical_edge_type: HAS_COLUMN
    inverse_edge_type: BELONGS_TO_TABLE
    materialize_inverse: false
    edge_class: canonical
    source_type: table
    target_type: column
```

```yaml
candidate_edge:
  edge_id: edge.walmart.0085
  edge_type: HAS_COLUMN
  source: table.zs_observe.walmart_settlement
  target: column.zs_observe.walmart_settlement.brand
  fields:
    edge_family: business_hierarchy_in_scope
    evidence_basis: source-backed card field dependency
    confidence: high
    canonical_cognee_edge: true
    marketplace_only: true
    canonical_edge_type: HAS_COLUMN
    inverse_edge_type: BELONGS_TO_TABLE
    materialize_inverse: false
    edge_class: canonical
    source_type: table
    target_type: column
```

```yaml
candidate_edge:
  edge_id: edge.walmart.0086
  edge_type: HAS_COLUMN
  source: table.zs_observe.walmart_settlement
  target: column.zs_observe.walmart_settlement.brand_ref_1
  fields:
    edge_family: business_hierarchy_in_scope
    evidence_basis: source-backed card field dependency
    confidence: high
    canonical_cognee_edge: true
    marketplace_only: true
    canonical_edge_type: HAS_COLUMN
    inverse_edge_type: BELONGS_TO_TABLE
    materialize_inverse: false
    edge_class: canonical
    source_type: table
    target_type: column
```

```yaml
candidate_edge:
  edge_id: edge.walmart.0087
  edge_type: HAS_COLUMN
  source: table.zs_observe.walmart_settlement
  target: column.zs_observe.walmart_settlement.brand_ref_2
  fields:
    edge_family: business_hierarchy_in_scope
    evidence_basis: source-backed card field dependency
    confidence: high
    canonical_cognee_edge: true
    marketplace_only: true
    canonical_edge_type: HAS_COLUMN
    inverse_edge_type: BELONGS_TO_TABLE
    materialize_inverse: false
    edge_class: canonical
    source_type: table
    target_type: column
```

```yaml
candidate_edge:
  edge_id: edge.walmart.0088
  edge_type: HAS_COLUMN
  source: table.zs_observe.walmart_settlement
  target: column.zs_observe.walmart_settlement.product_category
  fields:
    edge_family: business_hierarchy_in_scope
    evidence_basis: source-backed card field dependency
    confidence: high
    canonical_cognee_edge: true
    marketplace_only: true
    canonical_edge_type: HAS_COLUMN
    inverse_edge_type: BELONGS_TO_TABLE
    materialize_inverse: false
    edge_class: canonical
    source_type: table
    target_type: column
```

```yaml
candidate_edge:
  edge_id: edge.walmart.0089
  edge_type: HAS_COLUMN
  source: table.zs_observe.walmart_settlement
  target: column.zs_observe.walmart_settlement.product_type
  fields:
    edge_family: business_hierarchy_in_scope
    evidence_basis: source-backed card field dependency
    confidence: high
    canonical_cognee_edge: true
    marketplace_only: true
    canonical_edge_type: HAS_COLUMN
    inverse_edge_type: BELONGS_TO_TABLE
    materialize_inverse: false
    edge_class: canonical
    source_type: table
    target_type: column
```

```yaml
candidate_edge:
  edge_id: edge.walmart.0090
  edge_type: HAS_COLUMN
  source: table.zs_observe.walmart_settlement
  target: column.zs_observe.walmart_settlement.product_tax_code
  fields:
    edge_family: business_hierarchy_in_scope
    evidence_basis: source-backed card field dependency
    confidence: high
    canonical_cognee_edge: true
    marketplace_only: true
    canonical_edge_type: HAS_COLUMN
    inverse_edge_type: BELONGS_TO_TABLE
    materialize_inverse: false
    edge_class: canonical
    source_type: table
    target_type: column
```

```yaml
candidate_edge:
  edge_id: edge.walmart.0091
  edge_type: HAS_COLUMN
  source: table.zs_observe.walmart_settlement
  target: column.zs_observe.walmart_settlement.shipping_method
  fields:
    edge_family: business_hierarchy_in_scope
    evidence_basis: source-backed card field dependency
    confidence: high
    canonical_cognee_edge: true
    marketplace_only: true
    canonical_edge_type: HAS_COLUMN
    inverse_edge_type: BELONGS_TO_TABLE
    materialize_inverse: false
    edge_class: canonical
    source_type: table
    target_type: column
```

```yaml
candidate_edge:
  edge_id: edge.walmart.0092
  edge_type: HAS_COLUMN
  source: table.zs_observe.walmart_settlement
  target: column.zs_observe.walmart_settlement.item_condition
  fields:
    edge_family: business_hierarchy_in_scope
    evidence_basis: source-backed card field dependency
    confidence: high
    canonical_cognee_edge: true
    marketplace_only: true
    canonical_edge_type: HAS_COLUMN
    inverse_edge_type: BELONGS_TO_TABLE
    materialize_inverse: false
    edge_class: canonical
    source_type: table
    target_type: column
```

```yaml
candidate_edge:
  edge_id: edge.walmart.0093
  edge_type: HAS_COLUMN
  source: table.zs_observe.walmart_settlement
  target: column.zs_observe.walmart_settlement.base_commission_rate
  fields:
    edge_family: business_hierarchy_in_scope
    evidence_basis: source-backed card field dependency
    confidence: high
    canonical_cognee_edge: true
    marketplace_only: true
    canonical_edge_type: HAS_COLUMN
    inverse_edge_type: BELONGS_TO_TABLE
    materialize_inverse: false
    edge_class: canonical
    source_type: table
    target_type: column
```

```yaml
candidate_edge:
  edge_id: edge.walmart.0094
  edge_type: HAS_COLUMN
  source: table.zs_observe.walmart_settlement
  target: column.zs_observe.walmart_settlement.commission_rate
  fields:
    edge_family: business_hierarchy_in_scope
    evidence_basis: source-backed card field dependency
    confidence: high
    canonical_cognee_edge: true
    marketplace_only: true
    canonical_edge_type: HAS_COLUMN
    inverse_edge_type: BELONGS_TO_TABLE
    materialize_inverse: false
    edge_class: canonical
    source_type: table
    target_type: column
```

```yaml
candidate_edge:
  edge_id: edge.walmart.0095
  edge_type: HAS_COLUMN
  source: table.zs_observe.walmart_settlement
  target: column.zs_observe.walmart_settlement.commission_rule
  fields:
    edge_family: business_hierarchy_in_scope
    evidence_basis: source-backed card field dependency
    confidence: high
    canonical_cognee_edge: true
    marketplace_only: true
    canonical_edge_type: HAS_COLUMN
    inverse_edge_type: BELONGS_TO_TABLE
    materialize_inverse: false
    edge_class: canonical
    source_type: table
    target_type: column
```

```yaml
candidate_edge:
  edge_id: edge.walmart.0096
  edge_type: HAS_COLUMN
  source: table.zs_observe.walmart_settlement
  target: column.zs_observe.walmart_settlement.commission_on_product
  fields:
    edge_family: business_hierarchy_in_scope
    evidence_basis: source-backed card field dependency
    confidence: high
    canonical_cognee_edge: true
    marketplace_only: true
    canonical_edge_type: HAS_COLUMN
    inverse_edge_type: BELONGS_TO_TABLE
    materialize_inverse: false
    edge_class: canonical
    source_type: table
    target_type: column
```

```yaml
candidate_edge:
  edge_id: edge.walmart.0097
  edge_type: HAS_COLUMN
  source: table.zs_observe.walmart_settlement
  target: column.zs_observe.walmart_settlement.commission_incentive_program
  fields:
    edge_family: business_hierarchy_in_scope
    evidence_basis: source-backed card field dependency
    confidence: high
    canonical_cognee_edge: true
    marketplace_only: true
    canonical_edge_type: HAS_COLUMN
    inverse_edge_type: BELONGS_TO_TABLE
    materialize_inverse: false
    edge_class: canonical
    source_type: table
    target_type: column
```

```yaml
candidate_edge:
  edge_id: edge.walmart.0098
  edge_type: HAS_COLUMN
  source: table.zs_observe.walmart_settlement
  target: column.zs_observe.walmart_settlement.incentive_program_name
  fields:
    edge_family: business_hierarchy_in_scope
    evidence_basis: source-backed card field dependency
    confidence: high
    canonical_cognee_edge: true
    marketplace_only: true
    canonical_edge_type: HAS_COLUMN
    inverse_edge_type: BELONGS_TO_TABLE
    materialize_inverse: false
    edge_class: canonical
    source_type: table
    target_type: column
```

```yaml
candidate_edge:
  edge_id: edge.walmart.0099
  edge_type: HAS_COLUMN
  source: table.zs_observe.walmart_settlement
  target: column.zs_observe.walmart_settlement.commission_saving
  fields:
    edge_family: business_hierarchy_in_scope
    evidence_basis: source-backed card field dependency
    confidence: high
    canonical_cognee_edge: true
    marketplace_only: true
    canonical_edge_type: HAS_COLUMN
    inverse_edge_type: BELONGS_TO_TABLE
    materialize_inverse: false
    edge_class: canonical
    source_type: table
    target_type: column
```

```yaml
candidate_edge:
  edge_id: edge.walmart.0100
  edge_type: HAS_COLUMN
  source: table.zs_observe.walmart_settlement
  target: column.zs_observe.walmart_settlement.original_commission
  fields:
    edge_family: business_hierarchy_in_scope
    evidence_basis: source-backed card field dependency
    confidence: high
    canonical_cognee_edge: true
    marketplace_only: true
    canonical_edge_type: HAS_COLUMN
    inverse_edge_type: BELONGS_TO_TABLE
    materialize_inverse: false
    edge_class: canonical
    source_type: table
    target_type: column
```

```yaml
candidate_edge:
  edge_id: edge.walmart.0101
  edge_type: HAS_COLUMN
  source: table.zs_observe.walmart_settlement
  target: column.zs_observe.walmart_settlement.contract_category
  fields:
    edge_family: business_hierarchy_in_scope
    evidence_basis: source-backed card field dependency
    confidence: high
    canonical_cognee_edge: true
    marketplace_only: true
    canonical_edge_type: HAS_COLUMN
    inverse_edge_type: BELONGS_TO_TABLE
    materialize_inverse: false
    edge_class: canonical
    source_type: table
    target_type: column
```

```yaml
candidate_edge:
  edge_id: edge.walmart.0102
  edge_type: HAS_COLUMN
  source: table.zs_observe.walmart_settlement
  target: column.zs_observe.walmart_settlement.destination_state
  fields:
    edge_family: business_hierarchy_in_scope
    evidence_basis: source-backed card field dependency
    confidence: high
    canonical_cognee_edge: true
    marketplace_only: true
    canonical_edge_type: HAS_COLUMN
    inverse_edge_type: BELONGS_TO_TABLE
    materialize_inverse: false
    edge_class: canonical
    source_type: table
    target_type: column
```

```yaml
candidate_edge:
  edge_id: edge.walmart.0103
  edge_type: HAS_COLUMN
  source: table.zs_observe.walmart_settlement
  target: column.zs_observe.walmart_settlement.destination_city
  fields:
    edge_family: business_hierarchy_in_scope
    evidence_basis: source-backed card field dependency
    confidence: high
    canonical_cognee_edge: true
    marketplace_only: true
    canonical_edge_type: HAS_COLUMN
    inverse_edge_type: BELONGS_TO_TABLE
    materialize_inverse: false
    edge_class: canonical
    source_type: table
    target_type: column
```

```yaml
candidate_edge:
  edge_id: edge.walmart.0104
  edge_type: HAS_COLUMN
  source: table.zs_observe.walmart_settlement
  target: column.zs_observe.walmart_settlement.source_zipcode
  fields:
    edge_family: business_hierarchy_in_scope
    evidence_basis: source-backed card field dependency
    confidence: high
    canonical_cognee_edge: true
    marketplace_only: true
    canonical_edge_type: HAS_COLUMN
    inverse_edge_type: BELONGS_TO_TABLE
    materialize_inverse: false
    edge_class: canonical
    source_type: table
    target_type: column
```

```yaml
candidate_edge:
  edge_id: edge.walmart.0105
  edge_type: HAS_COLUMN
  source: table.zs_observe.walmart_settlement
  target: column.zs_observe.walmart_settlement.ship_to_state
  fields:
    edge_family: business_hierarchy_in_scope
    evidence_basis: source-backed card field dependency
    confidence: high
    canonical_cognee_edge: true
    marketplace_only: true
    canonical_edge_type: HAS_COLUMN
    inverse_edge_type: BELONGS_TO_TABLE
    materialize_inverse: false
    edge_class: canonical
    source_type: table
    target_type: column
```

```yaml
candidate_edge:
  edge_id: edge.walmart.0106
  edge_type: HAS_COLUMN
  source: table.zs_observe.walmart_settlement
  target: column.zs_observe.walmart_settlement.ship_to_city
  fields:
    edge_family: business_hierarchy_in_scope
    evidence_basis: source-backed card field dependency
    confidence: high
    canonical_cognee_edge: true
    marketplace_only: true
    canonical_edge_type: HAS_COLUMN
    inverse_edge_type: BELONGS_TO_TABLE
    materialize_inverse: false
    edge_class: canonical
    source_type: table
    target_type: column
```

```yaml
candidate_edge:
  edge_id: edge.walmart.0107
  edge_type: HAS_COLUMN
  source: table.zs_observe.walmart_settlement
  target: column.zs_observe.walmart_settlement.ship_to_zipcode
  fields:
    edge_family: business_hierarchy_in_scope
    evidence_basis: source-backed card field dependency
    confidence: high
    canonical_cognee_edge: true
    marketplace_only: true
    canonical_edge_type: HAS_COLUMN
    inverse_edge_type: BELONGS_TO_TABLE
    materialize_inverse: false
    edge_class: canonical
    source_type: table
    target_type: column
```

```yaml
candidate_edge:
  edge_id: edge.walmart.0108
  edge_type: HAS_COLUMN
  source: table.zs_observe.walmart_settlement
  target: column.zs_observe.walmart_settlement.purchase_order__
  fields:
    edge_family: business_hierarchy_in_scope
    evidence_basis: source-backed card field dependency
    confidence: high
    canonical_cognee_edge: true
    marketplace_only: true
    canonical_edge_type: HAS_COLUMN
    inverse_edge_type: BELONGS_TO_TABLE
    materialize_inverse: false
    edge_class: canonical
    source_type: table
    target_type: column
```

```yaml
candidate_edge:
  edge_id: edge.walmart.0109
  edge_type: HAS_COLUMN
  source: table.zs_observe.walmart_settlement
  target: column.zs_observe.walmart_settlement.purchase_order_line__
  fields:
    edge_family: business_hierarchy_in_scope
    evidence_basis: source-backed card field dependency
    confidence: high
    canonical_cognee_edge: true
    marketplace_only: true
    canonical_edge_type: HAS_COLUMN
    inverse_edge_type: BELONGS_TO_TABLE
    materialize_inverse: false
    edge_class: canonical
    source_type: table
    target_type: column
```

```yaml
candidate_edge:
  edge_id: edge.walmart.0110
  edge_type: HAS_COLUMN
  source: table.zs_observe.walmart_settlement
  target: column.zs_observe.walmart_settlement.customer_order__
  fields:
    edge_family: business_hierarchy_in_scope
    evidence_basis: source-backed card field dependency
    confidence: high
    canonical_cognee_edge: true
    marketplace_only: true
    canonical_edge_type: HAS_COLUMN
    inverse_edge_type: BELONGS_TO_TABLE
    materialize_inverse: false
    edge_class: canonical
    source_type: table
    target_type: column
```

```yaml
candidate_edge:
  edge_id: edge.walmart.0111
  edge_type: HAS_COLUMN
  source: table.zs_observe.walmart_settlement
  target: column.zs_observe.walmart_settlement.customer_order_line__
  fields:
    edge_family: business_hierarchy_in_scope
    evidence_basis: source-backed card field dependency
    confidence: high
    canonical_cognee_edge: true
    marketplace_only: true
    canonical_edge_type: HAS_COLUMN
    inverse_edge_type: BELONGS_TO_TABLE
    materialize_inverse: false
    edge_class: canonical
    source_type: table
    target_type: column
```

```yaml
candidate_edge:
  edge_id: edge.walmart.0112
  edge_type: HAS_COLUMN
  source: table.zs_observe.walmart_settlement
  target: column.zs_observe.walmart_settlement.transaction_key
  fields:
    edge_family: business_hierarchy_in_scope
    evidence_basis: source-backed card field dependency
    confidence: high
    canonical_cognee_edge: true
    marketplace_only: true
    canonical_edge_type: HAS_COLUMN
    inverse_edge_type: BELONGS_TO_TABLE
    materialize_inverse: false
    edge_class: canonical
    source_type: table
    target_type: column
```

```yaml
candidate_edge:
  edge_id: edge.walmart.0113
  edge_type: HAS_COLUMN
  source: table.zs_observe.walmart_settlement
  target: column.zs_observe.walmart_settlement.campaign_id
  fields:
    edge_family: business_hierarchy_in_scope
    evidence_basis: source-backed card field dependency
    confidence: high
    canonical_cognee_edge: true
    marketplace_only: true
    canonical_edge_type: HAS_COLUMN
    inverse_edge_type: BELONGS_TO_TABLE
    materialize_inverse: false
    edge_class: canonical
    source_type: table
    target_type: column
```

```yaml
candidate_edge:
  edge_id: edge.walmart.0114
  edge_type: HAS_COLUMN
  source: table.zs_observe.walmart_settlement
  target: column.zs_observe.walmart_settlement.group_level_id
  fields:
    edge_family: business_hierarchy_in_scope
    evidence_basis: source-backed card field dependency
    confidence: high
    canonical_cognee_edge: true
    marketplace_only: true
    canonical_edge_type: HAS_COLUMN
    inverse_edge_type: BELONGS_TO_TABLE
    materialize_inverse: false
    edge_class: canonical
    source_type: table
    target_type: column
```

```yaml
candidate_edge:
  edge_id: edge.walmart.0115
  edge_type: HAS_COLUMN
  source: table.zs_observe.walmart_settlement
  target: column.zs_observe.walmart_settlement.currency_type
  fields:
    edge_family: business_hierarchy_in_scope
    evidence_basis: source-backed card field dependency
    confidence: high
    canonical_cognee_edge: true
    marketplace_only: true
    canonical_edge_type: HAS_COLUMN
    inverse_edge_type: BELONGS_TO_TABLE
    materialize_inverse: false
    edge_class: canonical
    source_type: table
    target_type: column
```

```yaml
candidate_edge:
  edge_id: edge.walmart.0116
  edge_type: HAS_COLUMN
  source: table.zs_observe.walmart_settlement
  target: column.zs_observe.walmart_settlement.is_active
  fields:
    edge_family: business_hierarchy_in_scope
    evidence_basis: source-backed card field dependency
    confidence: high
    canonical_cognee_edge: true
    marketplace_only: true
    canonical_edge_type: HAS_COLUMN
    inverse_edge_type: BELONGS_TO_TABLE
    materialize_inverse: false
    edge_class: canonical
    source_type: table
    target_type: column
```

```yaml
candidate_edge:
  edge_id: edge.walmart.0117
  edge_type: HAS_COLUMN
  source: table.zs_observe.walmart_settlement
  target: column.zs_observe.walmart_settlement.currency
  fields:
    edge_family: business_hierarchy_in_scope
    evidence_basis: source-backed card field dependency
    confidence: high
    canonical_cognee_edge: true
    marketplace_only: true
    canonical_edge_type: HAS_COLUMN
    inverse_edge_type: BELONGS_TO_TABLE
    materialize_inverse: false
    edge_class: canonical
    source_type: table
    target_type: column
```

```yaml
candidate_edge:
  edge_id: edge.walmart.0118
  edge_type: HAS_COLUMN
  source: table.zs_observe.walmart_settlement
  target: column.zs_observe.walmart_settlement.type_description_mapping
  fields:
    edge_family: business_hierarchy_in_scope
    evidence_basis: source-backed card field dependency
    confidence: high
    canonical_cognee_edge: true
    marketplace_only: true
    canonical_edge_type: HAS_COLUMN
    inverse_edge_type: BELONGS_TO_TABLE
    materialize_inverse: false
    edge_class: canonical
    source_type: table
    target_type: column
```

```yaml
candidate_edge:
  edge_id: edge.walmart.0119
  edge_type: HAS_COLUMN
  source: table.zs_observe.walmart_settlement
  target: column.zs_observe.walmart_settlement.debug_is_active_inputs
  fields:
    edge_family: business_hierarchy_in_scope
    evidence_basis: source-backed card field dependency
    confidence: high
    canonical_cognee_edge: true
    marketplace_only: true
    canonical_edge_type: HAS_COLUMN
    inverse_edge_type: BELONGS_TO_TABLE
    materialize_inverse: false
    edge_class: canonical
    source_type: table
    target_type: column
```

```yaml
candidate_edge:
  edge_id: edge.walmart.0120
  edge_type: HAS_COLUMN
  source: table.zs_observe.walmart_settlement
  target: column.zs_observe.walmart_settlement.none
  fields:
    edge_family: business_hierarchy_in_scope
    evidence_basis: source-backed card field dependency
    confidence: high
    canonical_cognee_edge: true
    marketplace_only: true
    canonical_edge_type: HAS_COLUMN
    inverse_edge_type: BELONGS_TO_TABLE
    materialize_inverse: false
    edge_class: canonical
    source_type: table
    target_type: column
```

```yaml
candidate_edge:
  edge_id: edge.walmart.0121
  edge_type: HAS_COLUMN
  source: table.zs_observe.walmart_settlement
  target: column.zs_observe.walmart_settlement.excessrefundadjustment
  fields:
    edge_family: business_hierarchy_in_scope
    evidence_basis: source-backed card field dependency
    confidence: high
    canonical_cognee_edge: true
    marketplace_only: true
    canonical_edge_type: HAS_COLUMN
    inverse_edge_type: BELONGS_TO_TABLE
    materialize_inverse: false
    edge_class: canonical
    source_type: table
    target_type: column
```

```yaml
candidate_edge:
  edge_id: edge.walmart.0122
  edge_type: HAS_COLUMN
  source: table.zs_observe.walmart_settlement
  target: column.zs_observe.walmart_settlement.fulfillment_details
  fields:
    edge_family: business_hierarchy_in_scope
    evidence_basis: source-backed card field dependency
    confidence: high
    canonical_cognee_edge: true
    marketplace_only: true
    canonical_edge_type: HAS_COLUMN
    inverse_edge_type: BELONGS_TO_TABLE
    materialize_inverse: false
    edge_class: canonical
    source_type: table
    target_type: column
```

```yaml
candidate_edge:
  edge_id: edge.walmart.0123
  edge_type: HAS_COLUMN
  source: table.zs_observe.walmart_settlement
  target: column.zs_observe.walmart_settlement.customer_promo_type
  fields:
    edge_family: business_hierarchy_in_scope
    evidence_basis: source-backed card field dependency
    confidence: high
    canonical_cognee_edge: true
    marketplace_only: true
    canonical_edge_type: HAS_COLUMN
    inverse_edge_type: BELONGS_TO_TABLE
    materialize_inverse: false
    edge_class: canonical
    source_type: table
    target_type: column
```

```yaml
candidate_edge:
  edge_id: edge.walmart.0124
  edge_type: HAS_COLUMN
  source: table.zs_observe.walmart_lookup
  target: column.zs_observe.walmart_lookup.unique_id
  fields:
    edge_family: business_hierarchy_in_scope
    evidence_basis: source-backed card field dependency
    confidence: high
    canonical_cognee_edge: true
    marketplace_only: true
    canonical_edge_type: HAS_COLUMN
    inverse_edge_type: BELONGS_TO_TABLE
    materialize_inverse: false
    edge_class: canonical
    source_type: table
    target_type: column
```

```yaml
candidate_edge:
  edge_id: edge.walmart.0125
  edge_type: HAS_COLUMN
  source: table.zs_observe.walmart_lookup
  target: column.zs_observe.walmart_lookup.txn_uuid
  fields:
    edge_family: business_hierarchy_in_scope
    evidence_basis: source-backed card field dependency
    confidence: high
    canonical_cognee_edge: true
    marketplace_only: true
    canonical_edge_type: HAS_COLUMN
    inverse_edge_type: BELONGS_TO_TABLE
    materialize_inverse: false
    edge_class: canonical
    source_type: table
    target_type: column
```

```yaml
candidate_edge:
  edge_id: edge.walmart.0126
  edge_type: HAS_COLUMN
  source: table.zs_observe.walmart_lookup
  target: column.zs_observe.walmart_lookup.unique_value
  fields:
    edge_family: business_hierarchy_in_scope
    evidence_basis: source-backed card field dependency
    confidence: high
    canonical_cognee_edge: true
    marketplace_only: true
    canonical_edge_type: HAS_COLUMN
    inverse_edge_type: BELONGS_TO_TABLE
    materialize_inverse: false
    edge_class: canonical
    source_type: table
    target_type: column
```

```yaml
candidate_edge:
  edge_id: edge.walmart.0127
  edge_type: HAS_COLUMN
  source: table.zs_observe.walmart_lookup
  target: column.zs_observe.walmart_lookup.sku_id
  fields:
    edge_family: business_hierarchy_in_scope
    evidence_basis: source-backed card field dependency
    confidence: high
    canonical_cognee_edge: true
    marketplace_only: true
    canonical_edge_type: HAS_COLUMN
    inverse_edge_type: BELONGS_TO_TABLE
    materialize_inverse: false
    edge_class: canonical
    source_type: table
    target_type: column
```

```yaml
candidate_edge:
  edge_id: edge.walmart.0128
  edge_type: HAS_COLUMN
  source: table.zs_observe.walmart_lookup
  target: column.zs_observe.walmart_lookup.sku
  fields:
    edge_family: business_hierarchy_in_scope
    evidence_basis: source-backed card field dependency
    confidence: high
    canonical_cognee_edge: true
    marketplace_only: true
    canonical_edge_type: HAS_COLUMN
    inverse_edge_type: BELONGS_TO_TABLE
    materialize_inverse: false
    edge_class: canonical
    source_type: table
    target_type: column
```

```yaml
candidate_edge:
  edge_id: edge.walmart.0129
  edge_type: HAS_COLUMN
  source: table.zs_observe.walmart_lookup
  target: column.zs_observe.walmart_lookup.item_name
  fields:
    edge_family: business_hierarchy_in_scope
    evidence_basis: source-backed card field dependency
    confidence: high
    canonical_cognee_edge: true
    marketplace_only: true
    canonical_edge_type: HAS_COLUMN
    inverse_edge_type: BELONGS_TO_TABLE
    materialize_inverse: false
    edge_class: canonical
    source_type: table
    target_type: column
```

```yaml
candidate_edge:
  edge_id: edge.walmart.0130
  edge_type: HAS_COLUMN
  source: table.zs_observe.walmart_lookup
  target: column.zs_observe.walmart_lookup.currency_type
  fields:
    edge_family: business_hierarchy_in_scope
    evidence_basis: source-backed card field dependency
    confidence: high
    canonical_cognee_edge: true
    marketplace_only: true
    canonical_edge_type: HAS_COLUMN
    inverse_edge_type: BELONGS_TO_TABLE
    materialize_inverse: false
    edge_class: canonical
    source_type: table
    target_type: column
```

```yaml
candidate_edge:
  edge_id: edge.walmart.0131
  edge_type: HAS_COLUMN
  source: table.zs_observe.walmart_lookup
  target: column.zs_observe.walmart_lookup.group_level_id
  fields:
    edge_family: business_hierarchy_in_scope
    evidence_basis: source-backed card field dependency
    confidence: high
    canonical_cognee_edge: true
    marketplace_only: true
    canonical_edge_type: HAS_COLUMN
    inverse_edge_type: BELONGS_TO_TABLE
    materialize_inverse: false
    edge_class: canonical
    source_type: table
    target_type: column
```

```yaml
candidate_edge:
  edge_id: edge.walmart.0132
  edge_type: HAS_COLUMN
  source: table.zs_observe.walmart_lookup
  target: column.zs_observe.walmart_lookup.is_active
  fields:
    edge_family: business_hierarchy_in_scope
    evidence_basis: source-backed card field dependency
    confidence: high
    canonical_cognee_edge: true
    marketplace_only: true
    canonical_edge_type: HAS_COLUMN
    inverse_edge_type: BELONGS_TO_TABLE
    materialize_inverse: false
    edge_class: canonical
    source_type: table
    target_type: column
```

```yaml
candidate_edge:
  edge_id: edge.walmart.0133
  edge_type: HAS_COLUMN
  source: table.zs_observe.walmart_lookup
  target: column.zs_observe.walmart_lookup.ancestry
  fields:
    edge_family: business_hierarchy_in_scope
    evidence_basis: source-backed card field dependency
    confidence: high
    canonical_cognee_edge: true
    marketplace_only: true
    canonical_edge_type: HAS_COLUMN
    inverse_edge_type: BELONGS_TO_TABLE
    materialize_inverse: false
    edge_class: canonical
    source_type: table
    target_type: column
```

```yaml
candidate_edge:
  edge_id: edge.walmart.0134
  edge_type: HAS_COLUMN
  source: table.zs_observe.walmart_lookup
  target: column.zs_observe.walmart_lookup.file_uuid
  fields:
    edge_family: business_hierarchy_in_scope
    evidence_basis: source-backed card field dependency
    confidence: high
    canonical_cognee_edge: true
    marketplace_only: true
    canonical_edge_type: HAS_COLUMN
    inverse_edge_type: BELONGS_TO_TABLE
    materialize_inverse: false
    edge_class: canonical
    source_type: table
    target_type: column
```

```yaml
candidate_edge:
  edge_id: edge.walmart.0135
  edge_type: HAS_COLUMN
  source: table.zs_observe.walmart_lookup
  target: column.zs_observe.walmart_lookup.zen_sheet_name
  fields:
    edge_family: business_hierarchy_in_scope
    evidence_basis: source-backed card field dependency
    confidence: high
    canonical_cognee_edge: true
    marketplace_only: true
    canonical_edge_type: HAS_COLUMN
    inverse_edge_type: BELONGS_TO_TABLE
    materialize_inverse: false
    edge_class: canonical
    source_type: table
    target_type: column
```

```yaml
candidate_edge:
  edge_id: edge.walmart.0136
  edge_type: HAS_COLUMN
  source: table.zs_observe.walmart_lookup
  target: column.zs_observe.walmart_lookup.created_at
  fields:
    edge_family: business_hierarchy_in_scope
    evidence_basis: source-backed card field dependency
    confidence: high
    canonical_cognee_edge: true
    marketplace_only: true
    canonical_edge_type: HAS_COLUMN
    inverse_edge_type: BELONGS_TO_TABLE
    materialize_inverse: false
    edge_class: canonical
    source_type: table
    target_type: column
```

```yaml
candidate_edge:
  edge_id: edge.walmart.0137
  edge_type: HAS_COLUMN
  source: table.zs_observe.walmart_lookup
  target: column.zs_observe.walmart_lookup.updated_at
  fields:
    edge_family: business_hierarchy_in_scope
    evidence_basis: source-backed card field dependency
    confidence: high
    canonical_cognee_edge: true
    marketplace_only: true
    canonical_edge_type: HAS_COLUMN
    inverse_edge_type: BELONGS_TO_TABLE
    materialize_inverse: false
    edge_class: canonical
    source_type: table
    target_type: column
```

```yaml
candidate_edge:
  edge_id: edge.walmart.0138
  edge_type: HAS_COLUMN
  source: table.zs_observe.walmart_lookup
  target: column.zs_observe.walmart_lookup.is_duplicated
  fields:
    edge_family: business_hierarchy_in_scope
    evidence_basis: source-backed card field dependency
    confidence: high
    canonical_cognee_edge: true
    marketplace_only: true
    canonical_edge_type: HAS_COLUMN
    inverse_edge_type: BELONGS_TO_TABLE
    materialize_inverse: false
    edge_class: canonical
    source_type: table
    target_type: column
```

```yaml
candidate_edge:
  edge_id: edge.walmart.0139
  edge_type: HAS_COLUMN
  source: table.zs_observe.walmart_lookup
  target: column.zs_observe.walmart_lookup.zen_status
  fields:
    edge_family: business_hierarchy_in_scope
    evidence_basis: source-backed card field dependency
    confidence: high
    canonical_cognee_edge: true
    marketplace_only: true
    canonical_edge_type: HAS_COLUMN
    inverse_edge_type: BELONGS_TO_TABLE
    materialize_inverse: false
    edge_class: canonical
    source_type: table
    target_type: column
```

```yaml
candidate_edge:
  edge_id: edge.walmart.0140
  edge_type: FROM_TABLE
  source: relationship.walmart.oms_to_settlement_order_id
  target: table.zs_observe.walmart_oms
  fields:
    edge_family: canonical
    evidence_basis: source-backed card field dependency
    confidence: high
    canonical_cognee_edge: true
    marketplace_only: true
    canonical_edge_type: FROM_TABLE
    inverse_edge_type: SOURCE_OF_RELATIONSHIP
    materialize_inverse: false
    edge_class: canonical
    source_type: relationship
    target_type: table
    evidence_refs:
    - ev.walmart.relationships.001
```

```yaml
candidate_edge:
  edge_id: edge.walmart.0141
  edge_type: TO_TABLE
  source: relationship.walmart.oms_to_settlement_order_id
  target: table.zs_observe.walmart_settlement
  fields:
    edge_family: canonical
    evidence_basis: source-backed card field dependency
    confidence: high
    canonical_cognee_edge: true
    marketplace_only: true
    canonical_edge_type: TO_TABLE
    inverse_edge_type: TARGET_OF_RELATIONSHIP
    materialize_inverse: false
    edge_class: canonical
    source_type: relationship
    target_type: table
    evidence_refs:
    - ev.walmart.relationships.001
```

```yaml
candidate_edge:
  edge_id: edge.walmart.0142
  edge_type: FROM_TABLE
  source: relationship.walmart.oms_to_lookup_sku
  target: table.zs_observe.walmart_oms
  fields:
    edge_family: canonical
    evidence_basis: source-backed card field dependency
    confidence: high
    canonical_cognee_edge: true
    marketplace_only: true
    canonical_edge_type: FROM_TABLE
    inverse_edge_type: SOURCE_OF_RELATIONSHIP
    materialize_inverse: false
    edge_class: canonical
    source_type: relationship
    target_type: table
    evidence_refs:
    - ev.walmart.relationships.001
```

```yaml
candidate_edge:
  edge_id: edge.walmart.0143
  edge_type: TO_TABLE
  source: relationship.walmart.oms_to_lookup_sku
  target: table.zs_observe.walmart_lookup
  fields:
    edge_family: canonical
    evidence_basis: source-backed card field dependency
    confidence: high
    canonical_cognee_edge: true
    marketplace_only: true
    canonical_edge_type: TO_TABLE
    inverse_edge_type: TARGET_OF_RELATIONSHIP
    materialize_inverse: false
    edge_class: canonical
    source_type: relationship
    target_type: table
    evidence_refs:
    - ev.walmart.relationships.001
```

```yaml
candidate_edge:
  edge_id: edge.walmart.0144
  edge_type: FROM_TABLE
  source: relationship.walmart.settlement_to_lookup_sku
  target: table.zs_observe.walmart_settlement
  fields:
    edge_family: canonical
    evidence_basis: source-backed card field dependency
    confidence: high
    canonical_cognee_edge: true
    marketplace_only: true
    canonical_edge_type: FROM_TABLE
    inverse_edge_type: SOURCE_OF_RELATIONSHIP
    materialize_inverse: false
    edge_class: canonical
    source_type: relationship
    target_type: table
    evidence_refs:
    - ev.walmart.relationships.001
```

```yaml
candidate_edge:
  edge_id: edge.walmart.0145
  edge_type: TO_TABLE
  source: relationship.walmart.settlement_to_lookup_sku
  target: table.zs_observe.walmart_lookup
  fields:
    edge_family: canonical
    evidence_basis: source-backed card field dependency
    confidence: high
    canonical_cognee_edge: true
    marketplace_only: true
    canonical_edge_type: TO_TABLE
    inverse_edge_type: TARGET_OF_RELATIONSHIP
    materialize_inverse: false
    edge_class: canonical
    source_type: relationship
    target_type: table
    evidence_refs:
    - ev.walmart.relationships.001
```

```yaml
candidate_edge:
  edge_id: edge.walmart.0146
  edge_type: FROM_TABLE
  source: relationship.walmart.oms_item_to_settlement_gtin
  target: table.zs_observe.walmart_oms
  fields:
    edge_family: canonical
    evidence_basis: source-backed card field dependency
    confidence: high
    canonical_cognee_edge: true
    marketplace_only: true
    canonical_edge_type: FROM_TABLE
    inverse_edge_type: SOURCE_OF_RELATIONSHIP
    materialize_inverse: false
    edge_class: canonical
    source_type: relationship
    target_type: table
    evidence_refs:
    - ev.walmart.relationships.001
```

```yaml
candidate_edge:
  edge_id: edge.walmart.0147
  edge_type: TO_TABLE
  source: relationship.walmart.oms_item_to_settlement_gtin
  target: table.zs_observe.walmart_settlement
  fields:
    edge_family: canonical
    evidence_basis: source-backed card field dependency
    confidence: high
    canonical_cognee_edge: true
    marketplace_only: true
    canonical_edge_type: TO_TABLE
    inverse_edge_type: TARGET_OF_RELATIONSHIP
    materialize_inverse: false
    edge_class: canonical
    source_type: relationship
    target_type: table
    evidence_refs:
    - ev.walmart.relationships.001
```

```yaml
candidate_edge:
  edge_id: edge.walmart.0148
  edge_type: PROFILES_COLUMN
  source: value_profile.walmart.oms.order_status
  target: column.zs_observe.walmart_oms.order_status
  fields:
    edge_family: business_hierarchy_in_scope
    evidence_basis: source-backed card field dependency
    confidence: high
    canonical_cognee_edge: true
    marketplace_only: true
    canonical_edge_type: PROFILES_COLUMN
    inverse_edge_type: HAS_VALUE_PROFILE
    materialize_inverse: false
    edge_class: canonical
    source_type: value_profile
    target_type: column
    evidence_refs:
    - ev.walmart_oms.schema.001
```

```yaml
candidate_edge:
  edge_id: edge.walmart.0149
  edge_type: PROFILES_COLUMN
  source: value_profile.walmart.settlement.transaction_type
  target: column.zs_observe.walmart_settlement.transaction_type
  fields:
    edge_family: business_hierarchy_in_scope
    evidence_basis: source-backed card field dependency
    confidence: high
    canonical_cognee_edge: true
    marketplace_only: true
    canonical_edge_type: PROFILES_COLUMN
    inverse_edge_type: HAS_VALUE_PROFILE
    materialize_inverse: false
    edge_class: canonical
    source_type: value_profile
    target_type: column
    evidence_refs:
    - ev.walmart_settlement.values.001
```

```yaml
candidate_edge:
  edge_id: edge.walmart.0150
  edge_type: PROFILES_COLUMN
  source: value_profile.walmart.settlement.internal_txn_type
  target: column.zs_observe.walmart_settlement.internal_txn_type
  fields:
    edge_family: business_hierarchy_in_scope
    evidence_basis: source-backed card field dependency
    confidence: high
    canonical_cognee_edge: true
    marketplace_only: true
    canonical_edge_type: PROFILES_COLUMN
    inverse_edge_type: HAS_VALUE_PROFILE
    materialize_inverse: false
    edge_class: canonical
    source_type: value_profile
    target_type: column
    evidence_refs:
    - ev.walmart.quality.001
```

```yaml
candidate_edge:
  edge_id: edge.walmart.0151
  edge_type: PROFILES_COLUMN
  source: value_profile.walmart.settlement.other_type
  target: column.zs_observe.walmart_settlement.other_type
  fields:
    edge_family: business_hierarchy_in_scope
    evidence_basis: source-backed card field dependency
    confidence: high
    canonical_cognee_edge: true
    marketplace_only: true
    canonical_edge_type: PROFILES_COLUMN
    inverse_edge_type: HAS_VALUE_PROFILE
    materialize_inverse: false
    edge_class: canonical
    source_type: value_profile
    target_type: column
    evidence_refs:
    - ev.walmart.quality.001
```

```yaml
candidate_edge:
  edge_id: edge.walmart.0152
  edge_type: PROFILES_COLUMN
  source: value_profile.walmart.settlement.fulfilment_channel
  target: column.zs_observe.walmart_settlement.fulfilment_channel
  fields:
    edge_family: business_hierarchy_in_scope
    evidence_basis: source-backed card field dependency
    confidence: high
    canonical_cognee_edge: true
    marketplace_only: true
    canonical_edge_type: PROFILES_COLUMN
    inverse_edge_type: HAS_VALUE_PROFILE
    materialize_inverse: false
    edge_class: canonical
    source_type: value_profile
    target_type: column
    evidence_refs:
    - ev.walmart.business_model.001
```

```yaml
candidate_edge:
  edge_id: edge.walmart.0153
  edge_type: PROFILES_COLUMN
  source: value_profile.walmart.settlement.product_category
  target: column.zs_observe.walmart_settlement.product_category
  fields:
    edge_family: business_hierarchy_in_scope
    evidence_basis: source-backed card field dependency
    confidence: high
    canonical_cognee_edge: true
    marketplace_only: true
    canonical_edge_type: PROFILES_COLUMN
    inverse_edge_type: HAS_VALUE_PROFILE
    materialize_inverse: false
    edge_class: canonical
    source_type: value_profile
    target_type: column
    evidence_refs:
    - ev.walmart_settlement.values.001
```

```yaml
candidate_edge:
  edge_id: edge.walmart.0154
  edge_type: PROFILES_COLUMN
  source: value_profile.walmart.settlement.product_type
  target: column.zs_observe.walmart_settlement.product_type
  fields:
    edge_family: business_hierarchy_in_scope
    evidence_basis: source-backed card field dependency
    confidence: high
    canonical_cognee_edge: true
    marketplace_only: true
    canonical_edge_type: PROFILES_COLUMN
    inverse_edge_type: HAS_VALUE_PROFILE
    materialize_inverse: false
    edge_class: canonical
    source_type: value_profile
    target_type: column
    evidence_refs:
    - ev.walmart_settlement.values.001
```

```yaml
candidate_edge:
  edge_id: edge.walmart.0155
  edge_type: PROFILES_COLUMN
  source: value_profile.walmart.settlement.product_tax_code
  target: column.zs_observe.walmart_settlement.product_tax_code
  fields:
    edge_family: business_hierarchy_in_scope
    evidence_basis: source-backed card field dependency
    confidence: high
    canonical_cognee_edge: true
    marketplace_only: true
    canonical_edge_type: PROFILES_COLUMN
    inverse_edge_type: HAS_VALUE_PROFILE
    materialize_inverse: false
    edge_class: canonical
    source_type: value_profile
    target_type: column
    evidence_refs:
    - ev.walmart_settlement.values.001
```

```yaml
candidate_edge:
  edge_id: edge.walmart.0156
  edge_type: PROFILES_COLUMN
  source: value_profile.walmart.lookup.row_type
  target: table.zs_observe.walmart_lookup
  fields:
    edge_family: business_hierarchy_in_scope
    evidence_basis: source-backed card field dependency
    confidence: high
    canonical_cognee_edge: true
    marketplace_only: true
    canonical_edge_type: PROFILES_COLUMN
    inverse_edge_type: HAS_VALUE_PROFILE
    materialize_inverse: false
    edge_class: canonical
    source_type: value_profile
    target_type: table
    evidence_refs:
    - ev.walmart_lookup.schema.001
```

```yaml
candidate_edge:
  edge_id: edge.walmart.0157
  edge_type: PROFILES_COLUMN
  source: value_profile.walmart.currency_type
  target: column.zs_observe.walmart_settlement.currency_type
  fields:
    edge_family: business_hierarchy_in_scope
    evidence_basis: source-backed card field dependency
    confidence: high
    canonical_cognee_edge: true
    marketplace_only: true
    canonical_edge_type: PROFILES_COLUMN
    inverse_edge_type: HAS_VALUE_PROFILE
    materialize_inverse: false
    edge_class: canonical
    source_type: value_profile
    target_type: column
    evidence_refs:
    - ev.walmart.overview.001
```

```yaml
candidate_edge:
  edge_id: edge.walmart.0158
  edge_type: PROFILES_COLUMN
  source: value_profile.walmart.group_level_id
  target: column.zs_observe.walmart_settlement.group_level_id
  fields:
    edge_family: business_hierarchy_in_scope
    evidence_basis: source-backed card field dependency
    confidence: high
    canonical_cognee_edge: true
    marketplace_only: true
    canonical_edge_type: PROFILES_COLUMN
    inverse_edge_type: HAS_VALUE_PROFILE
    materialize_inverse: false
    edge_class: canonical
    source_type: value_profile
    target_type: column
    evidence_refs:
    - ev.walmart.filters.001
```

```yaml
candidate_edge:
  edge_id: edge.walmart.0159
  edge_type: IMPLEMENTED_BY
  source: metric.marketplace.gross_revenue
  target: metric_implementation.walmart.walmart_settlement.gross_revenue
  fields:
    edge_family: metric_semantics
    evidence_basis: source-backed card field dependency
    confidence: high
    canonical_cognee_edge: true
    marketplace_only: true
    canonical_edge_type: IMPLEMENTED_BY
    inverse_edge_type: IMPLEMENTS
    materialize_inverse: false
    edge_class: canonical
    source_type: metric
    target_type: metric_implementation
    evidence_refs:
    - ev.walmart.metrics.001
```

```yaml
candidate_edge:
  edge_id: edge.walmart.0160
  edge_type: USES_TABLE
  source: metric_implementation.walmart.walmart_settlement.gross_revenue
  target: table.zs_observe.walmart_settlement
  fields:
    edge_family: dependency_usage
    evidence_basis: source-backed card field dependency
    confidence: high
    canonical_cognee_edge: true
    marketplace_only: true
    canonical_edge_type: USES_TABLE
    inverse_edge_type: USED_BY_CARD
    materialize_inverse: false
    edge_class: canonical
    source_type: metric_implementation
    target_type: table
    evidence_refs:
    - ev.walmart.metrics.001
```

```yaml
candidate_edge:
  edge_id: edge.walmart.0161
  edge_type: IMPLEMENTED_BY
  source: metric.marketplace.product_revenue_excluding_tax
  target: metric_implementation.walmart.walmart_settlement.product_revenue_excluding_tax
  fields:
    edge_family: metric_semantics
    evidence_basis: source-backed card field dependency
    confidence: high
    canonical_cognee_edge: true
    marketplace_only: true
    canonical_edge_type: IMPLEMENTED_BY
    inverse_edge_type: IMPLEMENTS
    materialize_inverse: false
    edge_class: canonical
    source_type: metric
    target_type: metric_implementation
    evidence_refs:
    - ev.walmart.metrics.001
```

```yaml
candidate_edge:
  edge_id: edge.walmart.0162
  edge_type: USES_TABLE
  source: metric_implementation.walmart.walmart_settlement.product_revenue_excluding_tax
  target: table.zs_observe.walmart_settlement
  fields:
    edge_family: dependency_usage
    evidence_basis: source-backed card field dependency
    confidence: high
    canonical_cognee_edge: true
    marketplace_only: true
    canonical_edge_type: USES_TABLE
    inverse_edge_type: USED_BY_CARD
    materialize_inverse: false
    edge_class: canonical
    source_type: metric_implementation
    target_type: table
    evidence_refs:
    - ev.walmart.metrics.001
```

```yaml
candidate_edge:
  edge_id: edge.walmart.0163
  edge_type: IMPLEMENTED_BY
  source: metric.marketplace.net_seller_payout
  target: metric_implementation.walmart.walmart_settlement.net_seller_payout
  fields:
    edge_family: metric_semantics
    evidence_basis: source-backed card field dependency
    confidence: high
    canonical_cognee_edge: true
    marketplace_only: true
    canonical_edge_type: IMPLEMENTED_BY
    inverse_edge_type: IMPLEMENTS
    materialize_inverse: false
    edge_class: canonical
    source_type: metric
    target_type: metric_implementation
    evidence_refs:
    - ev.walmart.business_model.001
```

```yaml
candidate_edge:
  edge_id: edge.walmart.0164
  edge_type: USES_TABLE
  source: metric_implementation.walmart.walmart_settlement.net_seller_payout
  target: table.zs_observe.walmart_settlement
  fields:
    edge_family: dependency_usage
    evidence_basis: source-backed card field dependency
    confidence: high
    canonical_cognee_edge: true
    marketplace_only: true
    canonical_edge_type: USES_TABLE
    inverse_edge_type: USED_BY_CARD
    materialize_inverse: false
    edge_class: canonical
    source_type: metric_implementation
    target_type: table
    evidence_refs:
    - ev.walmart.business_model.001
```

```yaml
candidate_edge:
  edge_id: edge.walmart.0165
  edge_type: IMPLEMENTED_BY
  source: metric.marketplace.seller_realization_rate
  target: metric_implementation.walmart.walmart_settlement.seller_realization_rate
  fields:
    edge_family: metric_semantics
    evidence_basis: source-backed card field dependency
    confidence: high
    canonical_cognee_edge: true
    marketplace_only: true
    canonical_edge_type: IMPLEMENTED_BY
    inverse_edge_type: IMPLEMENTS
    materialize_inverse: false
    edge_class: canonical
    source_type: metric
    target_type: metric_implementation
    evidence_refs:
    - ev.walmart.metrics.001
```

```yaml
candidate_edge:
  edge_id: edge.walmart.0166
  edge_type: USES_TABLE
  source: metric_implementation.walmart.walmart_settlement.seller_realization_rate
  target: table.zs_observe.walmart_settlement
  fields:
    edge_family: dependency_usage
    evidence_basis: source-backed card field dependency
    confidence: high
    canonical_cognee_edge: true
    marketplace_only: true
    canonical_edge_type: USES_TABLE
    inverse_edge_type: USED_BY_CARD
    materialize_inverse: false
    edge_class: canonical
    source_type: metric_implementation
    target_type: table
    evidence_refs:
    - ev.walmart.metrics.001
```

```yaml
candidate_edge:
  edge_id: edge.walmart.0167
  edge_type: IMPLEMENTED_BY
  source: metric.marketplace.effective_commission_rate
  target: metric_implementation.walmart.walmart_settlement.effective_commission_rate
  fields:
    edge_family: metric_semantics
    evidence_basis: source-backed card field dependency
    confidence: high
    canonical_cognee_edge: true
    marketplace_only: true
    canonical_edge_type: IMPLEMENTED_BY
    inverse_edge_type: IMPLEMENTS
    materialize_inverse: false
    edge_class: canonical
    source_type: metric
    target_type: metric_implementation
    evidence_refs:
    - ev.walmart.reconciliation.001
```

```yaml
candidate_edge:
  edge_id: edge.walmart.0168
  edge_type: USES_TABLE
  source: metric_implementation.walmart.walmart_settlement.effective_commission_rate
  target: table.zs_observe.walmart_settlement
  fields:
    edge_family: dependency_usage
    evidence_basis: source-backed card field dependency
    confidence: high
    canonical_cognee_edge: true
    marketplace_only: true
    canonical_edge_type: USES_TABLE
    inverse_edge_type: USED_BY_CARD
    materialize_inverse: false
    edge_class: canonical
    source_type: metric_implementation
    target_type: table
    evidence_refs:
    - ev.walmart.reconciliation.001
```

```yaml
candidate_edge:
  edge_id: edge.walmart.0169
  edge_type: IMPLEMENTED_BY
  source: metric.marketplace.return_rate
  target: metric_implementation.walmart.walmart_settlement.return_rate
  fields:
    edge_family: metric_semantics
    evidence_basis: source-backed card field dependency
    confidence: high
    canonical_cognee_edge: true
    marketplace_only: true
    canonical_edge_type: IMPLEMENTED_BY
    inverse_edge_type: IMPLEMENTS
    materialize_inverse: false
    edge_class: canonical
    source_type: metric
    target_type: metric_implementation
    evidence_refs:
    - ev.walmart.metrics.001
```

```yaml
candidate_edge:
  edge_id: edge.walmart.0170
  edge_type: USES_TABLE
  source: metric_implementation.walmart.walmart_settlement.return_rate
  target: table.zs_observe.walmart_settlement
  fields:
    edge_family: dependency_usage
    evidence_basis: source-backed card field dependency
    confidence: high
    canonical_cognee_edge: true
    marketplace_only: true
    canonical_edge_type: USES_TABLE
    inverse_edge_type: USED_BY_CARD
    materialize_inverse: false
    edge_class: canonical
    source_type: metric_implementation
    target_type: table
    evidence_refs:
    - ev.walmart.metrics.001
```

```yaml
candidate_edge:
  edge_id: edge.walmart.0171
  edge_type: IMPLEMENTED_BY
  source: metric.marketplace.average_order_value
  target: metric_implementation.walmart.walmart_oms.average_order_value
  fields:
    edge_family: metric_semantics
    evidence_basis: source-backed card field dependency
    confidence: high
    canonical_cognee_edge: true
    marketplace_only: true
    canonical_edge_type: IMPLEMENTED_BY
    inverse_edge_type: IMPLEMENTS
    materialize_inverse: false
    edge_class: canonical
    source_type: metric
    target_type: metric_implementation
    evidence_refs:
    - ev.walmart.metrics.001
```

```yaml
candidate_edge:
  edge_id: edge.walmart.0172
  edge_type: USES_TABLE
  source: metric_implementation.walmart.walmart_oms.average_order_value
  target: table.zs_observe.walmart_oms
  fields:
    edge_family: dependency_usage
    evidence_basis: source-backed card field dependency
    confidence: high
    canonical_cognee_edge: true
    marketplace_only: true
    canonical_edge_type: USES_TABLE
    inverse_edge_type: USED_BY_CARD
    materialize_inverse: false
    edge_class: canonical
    source_type: metric_implementation
    target_type: table
    evidence_refs:
    - ev.walmart.metrics.001
```

```yaml
candidate_edge:
  edge_id: edge.walmart.0173
  edge_type: IMPLEMENTED_BY
  source: metric.marketplace.cancellation_rate
  target: metric_implementation.walmart.walmart_oms.cancellation_rate
  fields:
    edge_family: metric_semantics
    evidence_basis: source-backed card field dependency
    confidence: high
    canonical_cognee_edge: true
    marketplace_only: true
    canonical_edge_type: IMPLEMENTED_BY
    inverse_edge_type: IMPLEMENTS
    materialize_inverse: false
    edge_class: canonical
    source_type: metric
    target_type: metric_implementation
    evidence_refs:
    - ev.walmart_oms.schema.001
```

```yaml
candidate_edge:
  edge_id: edge.walmart.0174
  edge_type: USES_TABLE
  source: metric_implementation.walmart.walmart_oms.cancellation_rate
  target: table.zs_observe.walmart_oms
  fields:
    edge_family: dependency_usage
    evidence_basis: source-backed card field dependency
    confidence: high
    canonical_cognee_edge: true
    marketplace_only: true
    canonical_edge_type: USES_TABLE
    inverse_edge_type: USED_BY_CARD
    materialize_inverse: false
    edge_class: canonical
    source_type: metric_implementation
    target_type: table
    evidence_refs:
    - ev.walmart_oms.schema.001
```

```yaml
candidate_edge:
  edge_id: edge.walmart.0175
  edge_type: IMPLEMENTED_BY
  source: metric.marketplace.tax_withheld
  target: metric_implementation.walmart.walmart_settlement.tax_withheld
  fields:
    edge_family: metric_semantics
    evidence_basis: source-backed card field dependency
    confidence: high
    canonical_cognee_edge: true
    marketplace_only: true
    canonical_edge_type: IMPLEMENTED_BY
    inverse_edge_type: IMPLEMENTS
    materialize_inverse: false
    edge_class: canonical
    source_type: metric
    target_type: metric_implementation
    evidence_refs:
    - ev.walmart.business_model.001
```

```yaml
candidate_edge:
  edge_id: edge.walmart.0176
  edge_type: USES_TABLE
  source: metric_implementation.walmart.walmart_settlement.tax_withheld
  target: table.zs_observe.walmart_settlement
  fields:
    edge_family: dependency_usage
    evidence_basis: source-backed card field dependency
    confidence: high
    canonical_cognee_edge: true
    marketplace_only: true
    canonical_edge_type: USES_TABLE
    inverse_edge_type: USED_BY_CARD
    materialize_inverse: false
    edge_class: canonical
    source_type: metric_implementation
    target_type: table
    evidence_refs:
    - ev.walmart.business_model.001
```

```yaml
candidate_edge:
  edge_id: edge.walmart.0177
  edge_type: IMPLEMENTED_BY
  source: metric.marketplace.walmart_funded_savings
  target: metric_implementation.walmart.walmart_settlement.walmart_funded_savings
  fields:
    edge_family: metric_semantics
    evidence_basis: source-backed card field dependency
    confidence: high
    canonical_cognee_edge: true
    marketplace_only: true
    canonical_edge_type: IMPLEMENTED_BY
    inverse_edge_type: IMPLEMENTS
    materialize_inverse: false
    edge_class: canonical
    source_type: metric
    target_type: metric_implementation
    evidence_refs:
    - ev.walmart.metrics.001
```

```yaml
candidate_edge:
  edge_id: edge.walmart.0178
  edge_type: USES_TABLE
  source: metric_implementation.walmart.walmart_settlement.walmart_funded_savings
  target: table.zs_observe.walmart_settlement
  fields:
    edge_family: dependency_usage
    evidence_basis: source-backed card field dependency
    confidence: high
    canonical_cognee_edge: true
    marketplace_only: true
    canonical_edge_type: USES_TABLE
    inverse_edge_type: USED_BY_CARD
    materialize_inverse: false
    edge_class: canonical
    source_type: metric_implementation
    target_type: table
    evidence_refs:
    - ev.walmart.metrics.001
```

```yaml
candidate_edge:
  edge_id: edge.walmart.0179
  edge_type: IMPLEMENTED_BY
  source: metric.marketplace.sku_revenue
  target: metric_implementation.walmart.walmart_settlement.sku_revenue
  fields:
    edge_family: metric_semantics
    evidence_basis: source-backed card field dependency
    confidence: high
    canonical_cognee_edge: true
    marketplace_only: true
    canonical_edge_type: IMPLEMENTED_BY
    inverse_edge_type: IMPLEMENTS
    materialize_inverse: false
    edge_class: canonical
    source_type: metric
    target_type: metric_implementation
    evidence_refs:
    - ev.walmart.metrics.001
```

```yaml
candidate_edge:
  edge_id: edge.walmart.0180
  edge_type: USES_TABLE
  source: metric_implementation.walmart.walmart_settlement.sku_revenue
  target: table.zs_observe.walmart_settlement
  fields:
    edge_family: dependency_usage
    evidence_basis: source-backed card field dependency
    confidence: high
    canonical_cognee_edge: true
    marketplace_only: true
    canonical_edge_type: USES_TABLE
    inverse_edge_type: USED_BY_CARD
    materialize_inverse: false
    edge_class: canonical
    source_type: metric_implementation
    target_type: table
    evidence_refs:
    - ev.walmart.metrics.001
```

```yaml
candidate_edge:
  edge_id: edge.walmart.0181
  edge_type: USES_TABLE
  source: metric_implementation.walmart.walmart_settlement.sku_revenue
  target: table.zs_observe.walmart_lookup
  fields:
    edge_family: dependency_usage
    evidence_basis: source-backed card field dependency
    confidence: high
    canonical_cognee_edge: true
    marketplace_only: true
    canonical_edge_type: USES_TABLE
    inverse_edge_type: USED_BY_CARD
    materialize_inverse: false
    edge_class: canonical
    source_type: metric_implementation
    target_type: table
    evidence_refs:
    - ev.walmart.metrics.001
```

```yaml
candidate_edge:
  edge_id: edge.walmart.0182
  edge_type: IMPLEMENTED_BY
  source: metric.marketplace.revenue_by_state
  target: metric_implementation.walmart.walmart_oms.revenue_by_state
  fields:
    edge_family: metric_semantics
    evidence_basis: source-backed card field dependency
    confidence: high
    canonical_cognee_edge: true
    marketplace_only: true
    canonical_edge_type: IMPLEMENTED_BY
    inverse_edge_type: IMPLEMENTS
    materialize_inverse: false
    edge_class: canonical
    source_type: metric
    target_type: metric_implementation
    evidence_refs:
    - ev.walmart.metrics.001
```

```yaml
candidate_edge:
  edge_id: edge.walmart.0183
  edge_type: USES_TABLE
  source: metric_implementation.walmart.walmart_oms.revenue_by_state
  target: table.zs_observe.walmart_oms
  fields:
    edge_family: dependency_usage
    evidence_basis: source-backed card field dependency
    confidence: high
    canonical_cognee_edge: true
    marketplace_only: true
    canonical_edge_type: USES_TABLE
    inverse_edge_type: USED_BY_CARD
    materialize_inverse: false
    edge_class: canonical
    source_type: metric_implementation
    target_type: table
    evidence_refs:
    - ev.walmart.metrics.001
```

```yaml
candidate_edge:
  edge_id: edge.walmart.0184
  edge_type: APPLIES_TO
  source: rule.walmart.scope_filters
  target: table.zs_observe.walmart_oms
  fields:
    edge_family: rule_validation_constraint
    evidence_basis: source-backed card field dependency
    confidence: high
    canonical_cognee_edge: true
    marketplace_only: true
    canonical_edge_type: APPLIES_TO
    inverse_edge_type: HAS_APPLIED_RULE
    materialize_inverse: false
    edge_class: canonical
    source_type: rule
    target_type: table
    evidence_refs:
    - ev.walmart.filters.001
```

```yaml
candidate_edge:
  edge_id: edge.walmart.0185
  edge_type: APPLIES_TO
  source: rule.walmart.no_settled_amount_payout
  target: column.zs_observe.walmart_settlement.settled_amount
  fields:
    edge_family: rule_validation_constraint
    evidence_basis: source-backed card field dependency
    confidence: high
    canonical_cognee_edge: true
    marketplace_only: true
    canonical_edge_type: APPLIES_TO
    inverse_edge_type: HAS_APPLIED_RULE
    materialize_inverse: false
    edge_class: canonical
    source_type: rule
    target_type: column
    evidence_refs:
    - ev.walmart.business_model.001
```

```yaml
candidate_edge:
  edge_id: edge.walmart.0186
  edge_type: APPLIES_TO
  source: rule.walmart.mpf_tax_not_seller_revenue
  target: column.zs_observe.walmart_settlement.marketplace_withheld_tax
  fields:
    edge_family: rule_validation_constraint
    evidence_basis: source-backed card field dependency
    confidence: high
    canonical_cognee_edge: true
    marketplace_only: true
    canonical_edge_type: APPLIES_TO
    inverse_edge_type: HAS_APPLIED_RULE
    materialize_inverse: false
    edge_class: canonical
    source_type: rule
    target_type: column
    evidence_refs:
    - ev.walmart.business_model.001
```

```yaml
candidate_edge:
  edge_id: edge.walmart.0187
  edge_type: APPLIES_TO
  source: rule.walmart.forward_revenue_filter
  target: metric.marketplace.gross_revenue
  fields:
    edge_family: rule_validation_constraint
    evidence_basis: source-backed card field dependency
    confidence: high
    canonical_cognee_edge: true
    marketplace_only: true
    canonical_edge_type: APPLIES_TO
    inverse_edge_type: HAS_APPLIED_RULE
    materialize_inverse: false
    edge_class: canonical
    source_type: rule
    target_type: metric
    evidence_refs:
    - ev.walmart.filters.001
```

```yaml
candidate_edge:
  edge_id: edge.walmart.0188
  edge_type: APPLIES_TO
  source: rule.walmart.reverse_refund_filter
  target: metric.marketplace.return_rate
  fields:
    edge_family: rule_validation_constraint
    evidence_basis: source-backed card field dependency
    confidence: high
    canonical_cognee_edge: true
    marketplace_only: true
    canonical_edge_type: APPLIES_TO
    inverse_edge_type: HAS_APPLIED_RULE
    materialize_inverse: false
    edge_class: canonical
    source_type: rule
    target_type: metric
    evidence_refs:
    - ev.walmart.filters.001
```

```yaml
candidate_edge:
  edge_id: edge.walmart.0189
  edge_type: APPLIES_TO
  source: rule.walmart.lookup_sku_not_null
  target: table.zs_observe.walmart_lookup
  fields:
    edge_family: rule_validation_constraint
    evidence_basis: source-backed card field dependency
    confidence: high
    canonical_cognee_edge: true
    marketplace_only: true
    canonical_edge_type: APPLIES_TO
    inverse_edge_type: HAS_APPLIED_RULE
    materialize_inverse: false
    edge_class: canonical
    source_type: rule
    target_type: table
    evidence_refs:
    - ev.walmart_lookup.schema.001
```

```yaml
candidate_edge:
  edge_id: edge.walmart.0190
  edge_type: APPLIES_TO
  source: rule.walmart.oms_clean_rows
  target: table.zs_observe.walmart_oms
  fields:
    edge_family: rule_validation_constraint
    evidence_basis: source-backed card field dependency
    confidence: high
    canonical_cognee_edge: true
    marketplace_only: true
    canonical_edge_type: APPLIES_TO
    inverse_edge_type: HAS_APPLIED_RULE
    materialize_inverse: false
    edge_class: canonical
    source_type: rule
    target_type: table
    evidence_refs:
    - ev.walmart_oms.quality.001
```

```yaml
candidate_edge:
  edge_id: edge.walmart.0191
  edge_type: APPLIES_TO
  source: rule.walmart.compute_commission_rate
  target: metric.marketplace.effective_commission_rate
  fields:
    edge_family: rule_validation_constraint
    evidence_basis: source-backed card field dependency
    confidence: high
    canonical_cognee_edge: true
    marketplace_only: true
    canonical_edge_type: APPLIES_TO
    inverse_edge_type: HAS_APPLIED_RULE
    materialize_inverse: false
    edge_class: canonical
    source_type: rule
    target_type: metric
    evidence_refs:
    - ev.walmart.quality.001
```

```yaml
candidate_edge:
  edge_id: edge.walmart.0192
  edge_type: APPLIES_TO
  source: rule.walmart.hsn_is_barcode
  target: column.zs_observe.walmart_oms.hsn
  fields:
    edge_family: rule_validation_constraint
    evidence_basis: source-backed card field dependency
    confidence: high
    canonical_cognee_edge: true
    marketplace_only: true
    canonical_edge_type: APPLIES_TO
    inverse_edge_type: HAS_APPLIED_RULE
    materialize_inverse: false
    edge_class: canonical
    source_type: rule
    target_type: column
    evidence_refs:
    - ev.walmart_oms.quality.001
```

```yaml
candidate_edge:
  edge_id: edge.walmart.0193
  edge_type: APPLIES_TO
  source: rule.walmart.no_indian_tax_cards
  target: domain.marketplace.walmart.tax
  fields:
    edge_family: rule_validation_constraint
    evidence_basis: source-backed card field dependency
    confidence: high
    canonical_cognee_edge: true
    marketplace_only: true
    canonical_edge_type: APPLIES_TO
    inverse_edge_type: HAS_APPLIED_RULE
    materialize_inverse: false
    edge_class: canonical
    source_type: rule
    target_type: domain
    evidence_refs:
    - ev.walmart.business_model.001
```

```yaml
candidate_edge:
  edge_id: edge.walmart.0194
  edge_type: APPLIES_TO
  source: rule.walmart.wfs_fees_external
  target: table.zs_observe.walmart_settlement
  fields:
    edge_family: rule_validation_constraint
    evidence_basis: source-backed card field dependency
    confidence: high
    canonical_cognee_edge: true
    marketplace_only: true
    canonical_edge_type: APPLIES_TO
    inverse_edge_type: HAS_APPLIED_RULE
    materialize_inverse: false
    edge_class: canonical
    source_type: rule
    target_type: table
    evidence_refs:
    - ev.walmart.quality.001
```

```yaml
candidate_edge:
  edge_id: edge.walmart.0195
  edge_type: APPLIES_TO
  source: rule.walmart.no_process_variants_from_segments
  target: platform_context.walmart.us
  fields:
    edge_family: rule_validation_constraint
    evidence_basis: source-backed card field dependency
    confidence: high
    canonical_cognee_edge: true
    marketplace_only: true
    canonical_edge_type: APPLIES_TO
    inverse_edge_type: HAS_APPLIED_RULE
    materialize_inverse: false
    edge_class: canonical
    source_type: rule
    target_type: platform_context
    evidence_refs:
    - ev.walmart.overview.001
```

```yaml
candidate_edge:
  edge_id: edge.walmart.0196
  edge_type: APPLIES_TO
  source: rule.walmart.group_level_scope_only
  target: column.zs_observe.walmart_settlement.group_level_id
  fields:
    edge_family: rule_validation_constraint
    evidence_basis: source-backed card field dependency
    confidence: high
    canonical_cognee_edge: true
    marketplace_only: true
    canonical_edge_type: APPLIES_TO
    inverse_edge_type: HAS_APPLIED_RULE
    materialize_inverse: false
    edge_class: canonical
    source_type: rule
    target_type: column
    evidence_refs:
    - ev.walmart.filters.001
```

```yaml
candidate_edge:
  edge_id: edge.walmart.0197
  edge_type: APPLIES_TO
  source: rule.walmart.no_external_bank_or_erp
  target: table.zs_observe.walmart_settlement
  fields:
    edge_family: rule_validation_constraint
    evidence_basis: source-backed card field dependency
    confidence: high
    canonical_cognee_edge: true
    marketplace_only: true
    canonical_edge_type: APPLIES_TO
    inverse_edge_type: HAS_APPLIED_RULE
    materialize_inverse: false
    edge_class: canonical
    source_type: rule
    target_type: table
    evidence_refs:
    - ev.walmart.business_model.001
```

```yaml
candidate_edge:
  edge_id: edge.walmart.0198
  edge_type: VALIDATES
  source: validation_test.walmart.no_settled_amount_payout
  target: rule.walmart.no_settled_amount_payout
  fields:
    edge_family: rule_validation_constraint
    evidence_basis: source-backed card field dependency
    confidence: high
    canonical_cognee_edge: true
    marketplace_only: true
    canonical_edge_type: VALIDATES
    inverse_edge_type: VALIDATED_BY_TEST
    materialize_inverse: false
    edge_class: canonical
    source_type: validation_test
    target_type: rule
    evidence_refs:
    - ev.walmart.business_model.001
```

```yaml
candidate_edge:
  edge_id: edge.walmart.0199
  edge_type: VALIDATES
  source: validation_test.walmart.mandatory_filters
  target: rule.walmart.scope_filters
  fields:
    edge_family: rule_validation_constraint
    evidence_basis: source-backed card field dependency
    confidence: high
    canonical_cognee_edge: true
    marketplace_only: true
    canonical_edge_type: VALIDATES
    inverse_edge_type: VALIDATED_BY_TEST
    materialize_inverse: false
    edge_class: canonical
    source_type: validation_test
    target_type: rule
    evidence_refs:
    - ev.walmart.filters.001
```

```yaml
candidate_edge:
  edge_id: edge.walmart.0200
  edge_type: VALIDATES
  source: validation_test.walmart.lookup_sku_not_null
  target: rule.walmart.lookup_sku_not_null
  fields:
    edge_family: rule_validation_constraint
    evidence_basis: source-backed card field dependency
    confidence: high
    canonical_cognee_edge: true
    marketplace_only: true
    canonical_edge_type: VALIDATES
    inverse_edge_type: VALIDATED_BY_TEST
    materialize_inverse: false
    edge_class: canonical
    source_type: validation_test
    target_type: rule
    evidence_refs:
    - ev.walmart_lookup.schema.001
```

```yaml
candidate_edge:
  edge_id: edge.walmart.0201
  edge_type: VALIDATES
  source: validation_test.walmart.mpf_tax_identity
  target: reconciliation_profile.walmart.mpf_tax_identity
  fields:
    edge_family: rule_validation_constraint
    evidence_basis: source-backed card field dependency
    confidence: high
    canonical_cognee_edge: true
    marketplace_only: true
    canonical_edge_type: VALIDATES
    inverse_edge_type: VALIDATED_BY_TEST
    materialize_inverse: false
    edge_class: canonical
    source_type: validation_test
    target_type: reconciliation_profile
    evidence_refs:
    - ev.walmart.business_model.001
```

```yaml
candidate_edge:
  edge_id: edge.walmart.0202
  edge_type: VALIDATES
  source: validation_test.walmart.commission_rate_computed
  target: rule.walmart.compute_commission_rate
  fields:
    edge_family: rule_validation_constraint
    evidence_basis: source-backed card field dependency
    confidence: high
    canonical_cognee_edge: true
    marketplace_only: true
    canonical_edge_type: VALIDATES
    inverse_edge_type: VALIDATED_BY_TEST
    materialize_inverse: false
    edge_class: canonical
    source_type: validation_test
    target_type: rule
    evidence_refs:
    - ev.walmart.quality.001
```

```yaml
candidate_edge:
  edge_id: edge.walmart.0203
  edge_type: VALIDATES
  source: validation_test.walmart.no_indian_tax_cards
  target: rule.walmart.no_indian_tax_cards
  fields:
    edge_family: rule_validation_constraint
    evidence_basis: source-backed card field dependency
    confidence: high
    canonical_cognee_edge: true
    marketplace_only: true
    canonical_edge_type: VALIDATES
    inverse_edge_type: VALIDATED_BY_TEST
    materialize_inverse: false
    edge_class: canonical
    source_type: validation_test
    target_type: rule
    evidence_refs:
    - ev.walmart.business_model.001
```

```yaml
candidate_edge:
  edge_id: edge.walmart.0204
  edge_type: VALIDATES
  source: validation_test.walmart.oms_clean_rows
  target: rule.walmart.oms_clean_rows
  fields:
    edge_family: rule_validation_constraint
    evidence_basis: source-backed card field dependency
    confidence: high
    canonical_cognee_edge: true
    marketplace_only: true
    canonical_edge_type: VALIDATES
    inverse_edge_type: VALIDATED_BY_TEST
    materialize_inverse: false
    edge_class: canonical
    source_type: validation_test
    target_type: rule
    evidence_refs:
    - ev.walmart_oms.quality.001
```

```yaml
candidate_edge:
  edge_id: edge.walmart.0205
  edge_type: VALIDATES
  source: validation_test.walmart.no_process_variants
  target: rule.walmart.no_process_variants_from_segments
  fields:
    edge_family: rule_validation_constraint
    evidence_basis: source-backed card field dependency
    confidence: high
    canonical_cognee_edge: true
    marketplace_only: true
    canonical_edge_type: VALIDATES
    inverse_edge_type: VALIDATED_BY_TEST
    materialize_inverse: false
    edge_class: canonical
    source_type: validation_test
    target_type: rule
    evidence_refs:
    - ev.walmart.overview.001
```

```yaml
candidate_edge:
  edge_id: edge.walmart.0206
  edge_type: VALIDATES
  source: validation_test.walmart.oms_settlement_coverage
  target: reconciliation_profile.walmart.oms_to_settlement
  fields:
    edge_family: rule_validation_constraint
    evidence_basis: source-backed card field dependency
    confidence: high
    canonical_cognee_edge: true
    marketplace_only: true
    canonical_edge_type: VALIDATES
    inverse_edge_type: VALIDATED_BY_TEST
    materialize_inverse: false
    edge_class: canonical
    source_type: validation_test
    target_type: reconciliation_profile
    evidence_refs:
    - ev.walmart.relationships.001
```

```yaml
candidate_edge:
  edge_id: edge.walmart.0207
  edge_type: OUTPUT_FOR
  source: output_contract.walmart.forward_revenue
  target: metric.marketplace.net_seller_payout
  fields:
    edge_family: query_output_semantics
    evidence_basis: source-backed card field dependency
    confidence: high
    canonical_cognee_edge: true
    marketplace_only: true
    canonical_edge_type: OUTPUT_FOR
    inverse_edge_type: USES_OUTPUT_CONTRACT
    materialize_inverse: false
    edge_class: canonical
    source_type: output_contract
    target_type: metric
    evidence_refs:
    - ev.walmart.metrics.001
```

```yaml
candidate_edge:
  edge_id: edge.walmart.0208
  edge_type: OUTPUT_FOR
  source: output_contract.walmart.oms_settlement_recon
  target: reconciliation_profile.walmart.oms_to_settlement
  fields:
    edge_family: query_output_semantics
    evidence_basis: source-backed card field dependency
    confidence: high
    canonical_cognee_edge: true
    marketplace_only: true
    canonical_edge_type: OUTPUT_FOR
    inverse_edge_type: USES_OUTPUT_CONTRACT
    materialize_inverse: false
    edge_class: canonical
    source_type: output_contract
    target_type: reconciliation_profile
    evidence_refs:
    - ev.walmart.reconciliation.001
```

```yaml
candidate_edge:
  edge_id: edge.walmart.0209
  edge_type: OUTPUT_FOR
  source: output_contract.walmart.payout_cycle
  target: metric.marketplace.net_seller_payout
  fields:
    edge_family: query_output_semantics
    evidence_basis: source-backed card field dependency
    confidence: high
    canonical_cognee_edge: true
    marketplace_only: true
    canonical_edge_type: OUTPUT_FOR
    inverse_edge_type: USES_OUTPUT_CONTRACT
    materialize_inverse: false
    edge_class: canonical
    source_type: output_contract
    target_type: metric
    evidence_refs:
    - ev.walmart.metrics.001
```

```yaml
candidate_edge:
  edge_id: edge.walmart.0210
  edge_type: OUTPUT_FOR
  source: output_contract.walmart.sku_performance
  target: metric.marketplace.sku_revenue
  fields:
    edge_family: query_output_semantics
    evidence_basis: source-backed card field dependency
    confidence: high
    canonical_cognee_edge: true
    marketplace_only: true
    canonical_edge_type: OUTPUT_FOR
    inverse_edge_type: USES_OUTPUT_CONTRACT
    materialize_inverse: false
    edge_class: canonical
    source_type: output_contract
    target_type: metric
    evidence_refs:
    - ev.walmart.metrics.001
```

```yaml
candidate_edge:
  edge_id: edge.walmart.0211
  edge_type: OUTPUT_FOR
  source: output_contract.walmart.state_distribution
  target: metric.marketplace.revenue_by_state
  fields:
    edge_family: query_output_semantics
    evidence_basis: source-backed card field dependency
    confidence: high
    canonical_cognee_edge: true
    marketplace_only: true
    canonical_edge_type: OUTPUT_FOR
    inverse_edge_type: USES_OUTPUT_CONTRACT
    materialize_inverse: false
    edge_class: canonical
    source_type: output_contract
    target_type: metric
    evidence_refs:
    - ev.walmart.metrics.001
```

```yaml
candidate_edge:
  edge_id: edge.walmart.0212
  edge_type: OUTPUT_FOR
  source: output_contract.walmart.commission_validation
  target: reconciliation_profile.walmart.commission_validation
  fields:
    edge_family: query_output_semantics
    evidence_basis: source-backed card field dependency
    confidence: high
    canonical_cognee_edge: true
    marketplace_only: true
    canonical_edge_type: OUTPUT_FOR
    inverse_edge_type: USES_OUTPUT_CONTRACT
    materialize_inverse: false
    edge_class: canonical
    source_type: output_contract
    target_type: reconciliation_profile
    evidence_refs:
    - ev.walmart.reconciliation.001
```

```yaml
candidate_edge:
  edge_id: edge.walmart.0213
  edge_type: OUTPUT_FOR
  source: output_contract.walmart.refund_sale_match
  target: reconciliation_profile.walmart.refund_to_sale
  fields:
    edge_family: query_output_semantics
    evidence_basis: source-backed card field dependency
    confidence: high
    canonical_cognee_edge: true
    marketplace_only: true
    canonical_edge_type: OUTPUT_FOR
    inverse_edge_type: USES_OUTPUT_CONTRACT
    materialize_inverse: false
    edge_class: canonical
    source_type: output_contract
    target_type: reconciliation_profile
    evidence_refs:
    - ev.walmart.reconciliation.001
```

```yaml
candidate_edge:
  edge_id: edge.walmart.0214
  edge_type: HAS_WORKFLOW_STEP
  source: business_process.walmart.forward_wfs_sale_to_payout
  target: workflow_step.walmart.forward.order_created_in_oms
  fields:
    edge_family: business_process_flow
    evidence_basis: source-backed card field dependency
    confidence: high
    canonical_cognee_edge: true
    marketplace_only: true
    canonical_edge_type: HAS_WORKFLOW_STEP
    inverse_edge_type: BELONGS_TO_PROCESS
    materialize_inverse: false
    edge_class: canonical
    source_type: business_process
    target_type: workflow_step
    evidence_refs:
    - ev.walmart.lifecycle.001
```

```yaml
candidate_edge:
  edge_id: edge.walmart.0215
  edge_type: USES
  source: workflow_step.walmart.forward.order_created_in_oms
  target: table.zs_observe.walmart_oms
  fields:
    edge_family: dependency_usage
    evidence_basis: source-backed card field dependency
    confidence: high
    canonical_cognee_edge: true
    marketplace_only: true
    canonical_edge_type: USES
    inverse_edge_type: USED_BY_STEP
    materialize_inverse: false
    edge_class: canonical
    source_type: workflow_step
    target_type: table
    evidence_refs:
    - ev.walmart.lifecycle.001
```

```yaml
candidate_edge:
  edge_id: edge.walmart.0216
  edge_type: HAS_WORKFLOW_STEP
  source: business_process.walmart.forward_wfs_sale_to_payout
  target: workflow_step.walmart.forward.wfs_fulfilment
  fields:
    edge_family: business_process_flow
    evidence_basis: source-backed card field dependency
    confidence: high
    canonical_cognee_edge: true
    marketplace_only: true
    canonical_edge_type: HAS_WORKFLOW_STEP
    inverse_edge_type: BELONGS_TO_PROCESS
    materialize_inverse: false
    edge_class: canonical
    source_type: business_process
    target_type: workflow_step
    evidence_refs:
    - ev.walmart.business_model.001
```

```yaml
candidate_edge:
  edge_id: edge.walmart.0217
  edge_type: USES
  source: workflow_step.walmart.forward.wfs_fulfilment
  target: column.zs_observe.walmart_settlement.fulfilment_channel
  fields:
    edge_family: dependency_usage
    evidence_basis: source-backed card field dependency
    confidence: high
    canonical_cognee_edge: true
    marketplace_only: true
    canonical_edge_type: USES
    inverse_edge_type: USED_BY_STEP
    materialize_inverse: false
    edge_class: canonical
    source_type: workflow_step
    target_type: column
    evidence_refs:
    - ev.walmart.business_model.001
```

```yaml
candidate_edge:
  edge_id: edge.walmart.0218
  edge_type: HAS_WORKFLOW_STEP
  source: business_process.walmart.forward_wfs_sale_to_payout
  target: workflow_step.walmart.forward.delivered_sales_filter
  fields:
    edge_family: business_process_flow
    evidence_basis: source-backed card field dependency
    confidence: high
    canonical_cognee_edge: true
    marketplace_only: true
    canonical_edge_type: HAS_WORKFLOW_STEP
    inverse_edge_type: BELONGS_TO_PROCESS
    materialize_inverse: false
    edge_class: canonical
    source_type: business_process
    target_type: workflow_step
    evidence_refs:
    - ev.walmart.filters.001
```

```yaml
candidate_edge:
  edge_id: edge.walmart.0219
  edge_type: USES
  source: workflow_step.walmart.forward.delivered_sales_filter
  target: column.zs_observe.walmart_oms.order_status
  fields:
    edge_family: dependency_usage
    evidence_basis: source-backed card field dependency
    confidence: high
    canonical_cognee_edge: true
    marketplace_only: true
    canonical_edge_type: USES
    inverse_edge_type: USED_BY_STEP
    materialize_inverse: false
    edge_class: canonical
    source_type: workflow_step
    target_type: column
    evidence_refs:
    - ev.walmart.filters.001
```

```yaml
candidate_edge:
  edge_id: edge.walmart.0220
  edge_type: HAS_WORKFLOW_STEP
  source: business_process.walmart.forward_wfs_sale_to_payout
  target: workflow_step.walmart.forward.forward_settlement_row
  fields:
    edge_family: business_process_flow
    evidence_basis: source-backed card field dependency
    confidence: high
    canonical_cognee_edge: true
    marketplace_only: true
    canonical_edge_type: HAS_WORKFLOW_STEP
    inverse_edge_type: BELONGS_TO_PROCESS
    materialize_inverse: false
    edge_class: canonical
    source_type: business_process
    target_type: workflow_step
    evidence_refs:
    - ev.walmart.lifecycle.001
```

```yaml
candidate_edge:
  edge_id: edge.walmart.0221
  edge_type: USES
  source: workflow_step.walmart.forward.forward_settlement_row
  target: table.zs_observe.walmart_settlement
  fields:
    edge_family: dependency_usage
    evidence_basis: source-backed card field dependency
    confidence: high
    canonical_cognee_edge: true
    marketplace_only: true
    canonical_edge_type: USES
    inverse_edge_type: USED_BY_STEP
    materialize_inverse: false
    edge_class: canonical
    source_type: workflow_step
    target_type: table
    evidence_refs:
    - ev.walmart.lifecycle.001
```

```yaml
candidate_edge:
  edge_id: edge.walmart.0222
  edge_type: HAS_WORKFLOW_STEP
  source: business_process.walmart.forward_wfs_sale_to_payout
  target: workflow_step.walmart.forward.net_payout_computed
  fields:
    edge_family: business_process_flow
    evidence_basis: source-backed card field dependency
    confidence: high
    canonical_cognee_edge: true
    marketplace_only: true
    canonical_edge_type: HAS_WORKFLOW_STEP
    inverse_edge_type: BELONGS_TO_PROCESS
    materialize_inverse: false
    edge_class: canonical
    source_type: business_process
    target_type: workflow_step
    evidence_refs:
    - ev.walmart.business_model.001
```

```yaml
candidate_edge:
  edge_id: edge.walmart.0223
  edge_type: USES
  source: workflow_step.walmart.forward.net_payout_computed
  target: formula_template.walmart.net_seller_payout
  fields:
    edge_family: dependency_usage
    evidence_basis: source-backed card field dependency
    confidence: high
    canonical_cognee_edge: true
    marketplace_only: true
    canonical_edge_type: USES
    inverse_edge_type: USED_BY_STEP
    materialize_inverse: false
    edge_class: canonical
    source_type: workflow_step
    target_type: formula_template
    evidence_refs:
    - ev.walmart.business_model.001
```

```yaml
candidate_edge:
  edge_id: edge.walmart.0224
  edge_type: HAS_WORKFLOW_STEP
  source: business_process.walmart.refund_to_payout_deduction
  target: workflow_step.walmart.refund.wfs_return_triggered
  fields:
    edge_family: business_process_flow
    evidence_basis: source-backed card field dependency
    confidence: high
    canonical_cognee_edge: true
    marketplace_only: true
    canonical_edge_type: HAS_WORKFLOW_STEP
    inverse_edge_type: BELONGS_TO_PROCESS
    materialize_inverse: false
    edge_class: canonical
    source_type: business_process
    target_type: workflow_step
    evidence_refs:
    - ev.walmart.lifecycle.001
```

```yaml
candidate_edge:
  edge_id: edge.walmart.0225
  edge_type: USES
  source: workflow_step.walmart.refund.wfs_return_triggered
  target: platform_context.walmart.us
  fields:
    edge_family: dependency_usage
    evidence_basis: source-backed card field dependency
    confidence: high
    canonical_cognee_edge: true
    marketplace_only: true
    canonical_edge_type: USES
    inverse_edge_type: USED_BY_STEP
    materialize_inverse: false
    edge_class: canonical
    source_type: workflow_step
    target_type: platform_context
    evidence_refs:
    - ev.walmart.lifecycle.001
```

```yaml
candidate_edge:
  edge_id: edge.walmart.0226
  edge_type: HAS_WORKFLOW_STEP
  source: business_process.walmart.refund_to_payout_deduction
  target: workflow_step.walmart.refund.reverse_settlement_row
  fields:
    edge_family: business_process_flow
    evidence_basis: source-backed card field dependency
    confidence: high
    canonical_cognee_edge: true
    marketplace_only: true
    canonical_edge_type: HAS_WORKFLOW_STEP
    inverse_edge_type: BELONGS_TO_PROCESS
    materialize_inverse: false
    edge_class: canonical
    source_type: business_process
    target_type: workflow_step
    evidence_refs:
    - ev.walmart.lifecycle.001
```

```yaml
candidate_edge:
  edge_id: edge.walmart.0227
  edge_type: USES
  source: workflow_step.walmart.refund.reverse_settlement_row
  target: column.zs_observe.walmart_settlement.transaction_type
  fields:
    edge_family: dependency_usage
    evidence_basis: source-backed card field dependency
    confidence: high
    canonical_cognee_edge: true
    marketplace_only: true
    canonical_edge_type: USES
    inverse_edge_type: USED_BY_STEP
    materialize_inverse: false
    edge_class: canonical
    source_type: workflow_step
    target_type: column
    evidence_refs:
    - ev.walmart.lifecycle.001
```

```yaml
candidate_edge:
  edge_id: edge.walmart.0228
  edge_type: HAS_WORKFLOW_STEP
  source: business_process.walmart.refund_to_payout_deduction
  target: workflow_step.walmart.refund.next_payout_deduction
  fields:
    edge_family: business_process_flow
    evidence_basis: source-backed card field dependency
    confidence: high
    canonical_cognee_edge: true
    marketplace_only: true
    canonical_edge_type: HAS_WORKFLOW_STEP
    inverse_edge_type: BELONGS_TO_PROCESS
    materialize_inverse: false
    edge_class: canonical
    source_type: business_process
    target_type: workflow_step
    evidence_refs:
    - ev.walmart.lifecycle.001
```

```yaml
candidate_edge:
  edge_id: edge.walmart.0229
  edge_type: USES
  source: workflow_step.walmart.refund.next_payout_deduction
  target: reconciliation_profile.walmart.refund_to_sale
  fields:
    edge_family: dependency_usage
    evidence_basis: source-backed card field dependency
    confidence: high
    canonical_cognee_edge: true
    marketplace_only: true
    canonical_edge_type: USES
    inverse_edge_type: USED_BY_STEP
    materialize_inverse: false
    edge_class: canonical
    source_type: workflow_step
    target_type: reconciliation_profile
    evidence_refs:
    - ev.walmart.lifecycle.001
```

```yaml
candidate_edge:
  edge_id: edge.walmart.0230
  edge_type: HAS_WORKFLOW_STEP
  source: business_process.walmart.cancellation_without_settlement
  target: workflow_step.walmart.cancel.cancelled_in_oms
  fields:
    edge_family: business_process_flow
    evidence_basis: source-backed card field dependency
    confidence: high
    canonical_cognee_edge: true
    marketplace_only: true
    canonical_edge_type: HAS_WORKFLOW_STEP
    inverse_edge_type: BELONGS_TO_PROCESS
    materialize_inverse: false
    edge_class: canonical
    source_type: business_process
    target_type: workflow_step
    evidence_refs:
    - ev.walmart.lifecycle.001
```

```yaml
candidate_edge:
  edge_id: edge.walmart.0231
  edge_type: USES
  source: workflow_step.walmart.cancel.cancelled_in_oms
  target: column.zs_observe.walmart_oms.order_status
  fields:
    edge_family: dependency_usage
    evidence_basis: source-backed card field dependency
    confidence: high
    canonical_cognee_edge: true
    marketplace_only: true
    canonical_edge_type: USES
    inverse_edge_type: USED_BY_STEP
    materialize_inverse: false
    edge_class: canonical
    source_type: workflow_step
    target_type: column
    evidence_refs:
    - ev.walmart.lifecycle.001
```

```yaml
candidate_edge:
  edge_id: edge.walmart.0232
  edge_type: HAS_WORKFLOW_STEP
  source: business_process.walmart.catalogue_enrichment
  target: workflow_step.walmart.catalogue.filter_usable_sku_rows
  fields:
    edge_family: business_process_flow
    evidence_basis: source-backed card field dependency
    confidence: high
    canonical_cognee_edge: true
    marketplace_only: true
    canonical_edge_type: HAS_WORKFLOW_STEP
    inverse_edge_type: BELONGS_TO_PROCESS
    materialize_inverse: false
    edge_class: canonical
    source_type: business_process
    target_type: workflow_step
    evidence_refs:
    - ev.walmart_lookup.schema.001
```

```yaml
candidate_edge:
  edge_id: edge.walmart.0233
  edge_type: USES
  source: workflow_step.walmart.catalogue.filter_usable_sku_rows
  target: column.zs_observe.walmart_lookup.sku
  fields:
    edge_family: dependency_usage
    evidence_basis: source-backed card field dependency
    confidence: high
    canonical_cognee_edge: true
    marketplace_only: true
    canonical_edge_type: USES
    inverse_edge_type: USED_BY_STEP
    materialize_inverse: false
    edge_class: canonical
    source_type: workflow_step
    target_type: column
    evidence_refs:
    - ev.walmart_lookup.schema.001
```

```yaml
candidate_edge:
  edge_id: edge.walmart.0234
  edge_type: HAS_WORKFLOW_STEP
  source: business_process.walmart.catalogue_enrichment
  target: workflow_step.walmart.catalogue.enrich_oms_settlement
  fields:
    edge_family: business_process_flow
    evidence_basis: source-backed card field dependency
    confidence: high
    canonical_cognee_edge: true
    marketplace_only: true
    canonical_edge_type: HAS_WORKFLOW_STEP
    inverse_edge_type: BELONGS_TO_PROCESS
    materialize_inverse: false
    edge_class: canonical
    source_type: business_process
    target_type: workflow_step
    evidence_refs:
    - ev.walmart.relationships.001
```

```yaml
candidate_edge:
  edge_id: edge.walmart.0235
  edge_type: USES
  source: workflow_step.walmart.catalogue.enrich_oms_settlement
  target: relationship.walmart.oms_to_lookup_sku
  fields:
    edge_family: dependency_usage
    evidence_basis: source-backed card field dependency
    confidence: high
    canonical_cognee_edge: true
    marketplace_only: true
    canonical_edge_type: USES
    inverse_edge_type: USED_BY_STEP
    materialize_inverse: false
    edge_class: canonical
    source_type: workflow_step
    target_type: relationship
    evidence_refs:
    - ev.walmart.relationships.001
```

```yaml
candidate_edge:
  edge_id: edge.walmart.0236
  edge_type: HAS_STATE_TRANSITION
  source: business_process.walmart.forward_wfs_sale_to_payout
  target: state_transition.walmart.oms_acknowledged_to_shipped
  fields:
    edge_family: business_process_flow
    evidence_basis: source-backed card field dependency
    confidence: high
    canonical_cognee_edge: true
    marketplace_only: true
    canonical_edge_type: HAS_STATE_TRANSITION
    inverse_edge_type: PART_OF_PROCESS
    materialize_inverse: false
    edge_class: canonical
    source_type: business_process
    target_type: state_transition
    evidence_refs:
    - ev.walmart.lifecycle.001
```

```yaml
candidate_edge:
  edge_id: edge.walmart.0237
  edge_type: USES_STATE_COLUMN
  source: state_transition.walmart.oms_acknowledged_to_shipped
  target: column.zs_observe.walmart_oms.order_status
  fields:
    edge_family: business_process_flow
    evidence_basis: source-backed card field dependency
    confidence: high
    canonical_cognee_edge: true
    marketplace_only: true
    canonical_edge_type: USES_STATE_COLUMN
    inverse_edge_type: STATE_COLUMN_USED_BY
    materialize_inverse: false
    edge_class: canonical
    source_type: state_transition
    target_type: column
    evidence_refs:
    - ev.walmart.lifecycle.001
```

```yaml
candidate_edge:
  edge_id: edge.walmart.0238
  edge_type: HAS_STATE_TRANSITION
  source: business_process.walmart.forward_wfs_sale_to_payout
  target: state_transition.walmart.oms_shipped_to_delivered
  fields:
    edge_family: business_process_flow
    evidence_basis: source-backed card field dependency
    confidence: high
    canonical_cognee_edge: true
    marketplace_only: true
    canonical_edge_type: HAS_STATE_TRANSITION
    inverse_edge_type: PART_OF_PROCESS
    materialize_inverse: false
    edge_class: canonical
    source_type: business_process
    target_type: state_transition
    evidence_refs:
    - ev.walmart.lifecycle.001
```

```yaml
candidate_edge:
  edge_id: edge.walmart.0239
  edge_type: USES_STATE_COLUMN
  source: state_transition.walmart.oms_shipped_to_delivered
  target: column.zs_observe.walmart_oms.order_status
  fields:
    edge_family: business_process_flow
    evidence_basis: source-backed card field dependency
    confidence: high
    canonical_cognee_edge: true
    marketplace_only: true
    canonical_edge_type: USES_STATE_COLUMN
    inverse_edge_type: STATE_COLUMN_USED_BY
    materialize_inverse: false
    edge_class: canonical
    source_type: state_transition
    target_type: column
    evidence_refs:
    - ev.walmart.lifecycle.001
```

```yaml
candidate_edge:
  edge_id: edge.walmart.0240
  edge_type: HAS_STATE_TRANSITION
  source: business_process.walmart.cancellation_without_settlement
  target: state_transition.walmart.oms_to_cancelled
  fields:
    edge_family: business_process_flow
    evidence_basis: source-backed card field dependency
    confidence: high
    canonical_cognee_edge: true
    marketplace_only: true
    canonical_edge_type: HAS_STATE_TRANSITION
    inverse_edge_type: PART_OF_PROCESS
    materialize_inverse: false
    edge_class: canonical
    source_type: business_process
    target_type: state_transition
    evidence_refs:
    - ev.walmart.lifecycle.001
```

```yaml
candidate_edge:
  edge_id: edge.walmart.0241
  edge_type: USES_STATE_COLUMN
  source: state_transition.walmart.oms_to_cancelled
  target: column.zs_observe.walmart_oms.order_status
  fields:
    edge_family: business_process_flow
    evidence_basis: source-backed card field dependency
    confidence: high
    canonical_cognee_edge: true
    marketplace_only: true
    canonical_edge_type: USES_STATE_COLUMN
    inverse_edge_type: STATE_COLUMN_USED_BY
    materialize_inverse: false
    edge_class: canonical
    source_type: state_transition
    target_type: column
    evidence_refs:
    - ev.walmart.lifecycle.001
```

```yaml
candidate_edge:
  edge_id: edge.walmart.0242
  edge_type: HAS_STATE_TRANSITION
  source: business_process.walmart.refund_to_payout_deduction
  target: state_transition.walmart.settlement_sale_to_refund
  fields:
    edge_family: business_process_flow
    evidence_basis: source-backed card field dependency
    confidence: high
    canonical_cognee_edge: true
    marketplace_only: true
    canonical_edge_type: HAS_STATE_TRANSITION
    inverse_edge_type: PART_OF_PROCESS
    materialize_inverse: false
    edge_class: canonical
    source_type: business_process
    target_type: state_transition
    evidence_refs:
    - ev.walmart.lifecycle.001
```

```yaml
candidate_edge:
  edge_id: edge.walmart.0243
  edge_type: USES_STATE_COLUMN
  source: state_transition.walmart.settlement_sale_to_refund
  target: column.zs_observe.walmart_settlement.transaction_type
  fields:
    edge_family: business_process_flow
    evidence_basis: source-backed card field dependency
    confidence: high
    canonical_cognee_edge: true
    marketplace_only: true
    canonical_edge_type: USES_STATE_COLUMN
    inverse_edge_type: STATE_COLUMN_USED_BY
    materialize_inverse: false
    edge_class: canonical
    source_type: state_transition
    target_type: column
    evidence_refs:
    - ev.walmart.lifecycle.001
```

```yaml
candidate_edge:
  edge_id: edge.walmart.0244
  edge_type: HAS_SIDE
  source: reconciliation_profile.walmart.oms_to_settlement
  target: reconciliation_side.walmart.oms_to_settlement.expected
  fields:
    edge_family: reconciliation_semantics
    evidence_basis: source-backed card field dependency
    confidence: high
    canonical_cognee_edge: true
    marketplace_only: true
    canonical_edge_type: HAS_SIDE
    inverse_edge_type: BELONGS_TO_RECONCILIATION_PROFILE
    materialize_inverse: false
    edge_class: canonical
    source_type: reconciliation_profile
    target_type: reconciliation_side
    evidence_refs:
    - ev.walmart.reconciliation.001
```

```yaml
candidate_edge:
  edge_id: edge.walmart.0245
  edge_type: HAS_SIDE
  source: reconciliation_profile.walmart.oms_to_settlement
  target: reconciliation_side.walmart.oms_to_settlement.actual
  fields:
    edge_family: reconciliation_semantics
    evidence_basis: source-backed card field dependency
    confidence: high
    canonical_cognee_edge: true
    marketplace_only: true
    canonical_edge_type: HAS_SIDE
    inverse_edge_type: BELONGS_TO_RECONCILIATION_PROFILE
    materialize_inverse: false
    edge_class: canonical
    source_type: reconciliation_profile
    target_type: reconciliation_side
    evidence_refs:
    - ev.walmart.reconciliation.001
```

```yaml
candidate_edge:
  edge_id: edge.walmart.0246
  edge_type: HAS_UNIT
  source: reconciliation_profile.walmart.oms_to_settlement
  target: reconciliation_unit.walmart.oms_to_settlement
  fields:
    edge_family: reconciliation_semantics
    evidence_basis: source-backed card field dependency
    confidence: high
    canonical_cognee_edge: true
    marketplace_only: true
    canonical_edge_type: HAS_UNIT
    inverse_edge_type: PRIMARY_UNIT_OF_PROFILE
    materialize_inverse: false
    edge_class: canonical
    source_type: reconciliation_profile
    target_type: reconciliation_unit
    evidence_refs:
    - ev.walmart.reconciliation.001
```

```yaml
candidate_edge:
  edge_id: edge.walmart.0247
  edge_type: HAS_MATCHING_LOGIC
  source: reconciliation_profile.walmart.oms_to_settlement
  target: matching_logic.walmart.oms_to_settlement.primary
  fields:
    edge_family: reconciliation_semantics
    evidence_basis: source-backed card field dependency
    confidence: high
    canonical_cognee_edge: true
    marketplace_only: true
    canonical_edge_type: HAS_MATCHING_LOGIC
    inverse_edge_type: SUPPORTS_RECONCILIATION_PROFILE
    materialize_inverse: false
    edge_class: canonical
    source_type: reconciliation_profile
    target_type: matching_logic
    evidence_refs:
    - ev.walmart.reconciliation.001
```

```yaml
candidate_edge:
  edge_id: edge.walmart.0248
  edge_type: HAS_SIDE
  source: reconciliation_profile.walmart.commission_validation
  target: reconciliation_side.walmart.commission_validation.expected
  fields:
    edge_family: reconciliation_semantics
    evidence_basis: source-backed card field dependency
    confidence: high
    canonical_cognee_edge: true
    marketplace_only: true
    canonical_edge_type: HAS_SIDE
    inverse_edge_type: BELONGS_TO_RECONCILIATION_PROFILE
    materialize_inverse: false
    edge_class: canonical
    source_type: reconciliation_profile
    target_type: reconciliation_side
    evidence_refs:
    - ev.walmart.reconciliation.001
```

```yaml
candidate_edge:
  edge_id: edge.walmart.0249
  edge_type: HAS_SIDE
  source: reconciliation_profile.walmart.commission_validation
  target: reconciliation_side.walmart.commission_validation.actual
  fields:
    edge_family: reconciliation_semantics
    evidence_basis: source-backed card field dependency
    confidence: high
    canonical_cognee_edge: true
    marketplace_only: true
    canonical_edge_type: HAS_SIDE
    inverse_edge_type: BELONGS_TO_RECONCILIATION_PROFILE
    materialize_inverse: false
    edge_class: canonical
    source_type: reconciliation_profile
    target_type: reconciliation_side
    evidence_refs:
    - ev.walmart.reconciliation.001
```

```yaml
candidate_edge:
  edge_id: edge.walmart.0250
  edge_type: HAS_UNIT
  source: reconciliation_profile.walmart.commission_validation
  target: reconciliation_unit.walmart.commission_validation
  fields:
    edge_family: reconciliation_semantics
    evidence_basis: source-backed card field dependency
    confidence: high
    canonical_cognee_edge: true
    marketplace_only: true
    canonical_edge_type: HAS_UNIT
    inverse_edge_type: PRIMARY_UNIT_OF_PROFILE
    materialize_inverse: false
    edge_class: canonical
    source_type: reconciliation_profile
    target_type: reconciliation_unit
    evidence_refs:
    - ev.walmart.reconciliation.001
```

```yaml
candidate_edge:
  edge_id: edge.walmart.0251
  edge_type: HAS_MATCHING_LOGIC
  source: reconciliation_profile.walmart.commission_validation
  target: matching_logic.walmart.commission_validation.primary
  fields:
    edge_family: reconciliation_semantics
    evidence_basis: source-backed card field dependency
    confidence: high
    canonical_cognee_edge: true
    marketplace_only: true
    canonical_edge_type: HAS_MATCHING_LOGIC
    inverse_edge_type: SUPPORTS_RECONCILIATION_PROFILE
    materialize_inverse: false
    edge_class: canonical
    source_type: reconciliation_profile
    target_type: matching_logic
    evidence_refs:
    - ev.walmart.reconciliation.001
```

```yaml
candidate_edge:
  edge_id: edge.walmart.0252
  edge_type: HAS_SIDE
  source: reconciliation_profile.walmart.refund_to_sale
  target: reconciliation_side.walmart.refund_to_sale.expected
  fields:
    edge_family: reconciliation_semantics
    evidence_basis: source-backed card field dependency
    confidence: high
    canonical_cognee_edge: true
    marketplace_only: true
    canonical_edge_type: HAS_SIDE
    inverse_edge_type: BELONGS_TO_RECONCILIATION_PROFILE
    materialize_inverse: false
    edge_class: canonical
    source_type: reconciliation_profile
    target_type: reconciliation_side
    evidence_refs:
    - ev.walmart.reconciliation.001
```

```yaml
candidate_edge:
  edge_id: edge.walmart.0253
  edge_type: HAS_SIDE
  source: reconciliation_profile.walmart.refund_to_sale
  target: reconciliation_side.walmart.refund_to_sale.actual
  fields:
    edge_family: reconciliation_semantics
    evidence_basis: source-backed card field dependency
    confidence: high
    canonical_cognee_edge: true
    marketplace_only: true
    canonical_edge_type: HAS_SIDE
    inverse_edge_type: BELONGS_TO_RECONCILIATION_PROFILE
    materialize_inverse: false
    edge_class: canonical
    source_type: reconciliation_profile
    target_type: reconciliation_side
    evidence_refs:
    - ev.walmart.reconciliation.001
```

```yaml
candidate_edge:
  edge_id: edge.walmart.0254
  edge_type: HAS_UNIT
  source: reconciliation_profile.walmart.refund_to_sale
  target: reconciliation_unit.walmart.refund_to_sale
  fields:
    edge_family: reconciliation_semantics
    evidence_basis: source-backed card field dependency
    confidence: high
    canonical_cognee_edge: true
    marketplace_only: true
    canonical_edge_type: HAS_UNIT
    inverse_edge_type: PRIMARY_UNIT_OF_PROFILE
    materialize_inverse: false
    edge_class: canonical
    source_type: reconciliation_profile
    target_type: reconciliation_unit
    evidence_refs:
    - ev.walmart.reconciliation.001
```

```yaml
candidate_edge:
  edge_id: edge.walmart.0255
  edge_type: HAS_MATCHING_LOGIC
  source: reconciliation_profile.walmart.refund_to_sale
  target: matching_logic.walmart.refund_to_sale.primary
  fields:
    edge_family: reconciliation_semantics
    evidence_basis: source-backed card field dependency
    confidence: high
    canonical_cognee_edge: true
    marketplace_only: true
    canonical_edge_type: HAS_MATCHING_LOGIC
    inverse_edge_type: SUPPORTS_RECONCILIATION_PROFILE
    materialize_inverse: false
    edge_class: canonical
    source_type: reconciliation_profile
    target_type: matching_logic
    evidence_refs:
    - ev.walmart.reconciliation.001
```

```yaml
candidate_edge:
  edge_id: edge.walmart.0256
  edge_type: HAS_SIDE
  source: reconciliation_profile.walmart.mpf_tax_identity
  target: reconciliation_side.walmart.mpf_tax_identity.expected
  fields:
    edge_family: reconciliation_semantics
    evidence_basis: source-backed card field dependency
    confidence: high
    canonical_cognee_edge: true
    marketplace_only: true
    canonical_edge_type: HAS_SIDE
    inverse_edge_type: BELONGS_TO_RECONCILIATION_PROFILE
    materialize_inverse: false
    edge_class: canonical
    source_type: reconciliation_profile
    target_type: reconciliation_side
    evidence_refs:
    - ev.walmart.business_model.001
```

```yaml
candidate_edge:
  edge_id: edge.walmart.0257
  edge_type: HAS_SIDE
  source: reconciliation_profile.walmart.mpf_tax_identity
  target: reconciliation_side.walmart.mpf_tax_identity.actual
  fields:
    edge_family: reconciliation_semantics
    evidence_basis: source-backed card field dependency
    confidence: high
    canonical_cognee_edge: true
    marketplace_only: true
    canonical_edge_type: HAS_SIDE
    inverse_edge_type: BELONGS_TO_RECONCILIATION_PROFILE
    materialize_inverse: false
    edge_class: canonical
    source_type: reconciliation_profile
    target_type: reconciliation_side
    evidence_refs:
    - ev.walmart.business_model.001
```

```yaml
candidate_edge:
  edge_id: edge.walmart.0258
  edge_type: HAS_UNIT
  source: reconciliation_profile.walmart.mpf_tax_identity
  target: reconciliation_unit.walmart.mpf_tax_identity
  fields:
    edge_family: reconciliation_semantics
    evidence_basis: source-backed card field dependency
    confidence: high
    canonical_cognee_edge: true
    marketplace_only: true
    canonical_edge_type: HAS_UNIT
    inverse_edge_type: PRIMARY_UNIT_OF_PROFILE
    materialize_inverse: false
    edge_class: canonical
    source_type: reconciliation_profile
    target_type: reconciliation_unit
    evidence_refs:
    - ev.walmart.business_model.001
```

```yaml
candidate_edge:
  edge_id: edge.walmart.0259
  edge_type: HAS_MATCHING_LOGIC
  source: reconciliation_profile.walmart.mpf_tax_identity
  target: matching_logic.walmart.mpf_tax_identity.primary
  fields:
    edge_family: reconciliation_semantics
    evidence_basis: source-backed card field dependency
    confidence: high
    canonical_cognee_edge: true
    marketplace_only: true
    canonical_edge_type: HAS_MATCHING_LOGIC
    inverse_edge_type: SUPPORTS_RECONCILIATION_PROFILE
    materialize_inverse: false
    edge_class: canonical
    source_type: reconciliation_profile
    target_type: matching_logic
    evidence_refs:
    - ev.walmart.business_model.001
```

```yaml
candidate_edge:
  edge_id: edge.walmart.0260
  edge_type: HAS_SIDE
  source: reconciliation_profile.walmart.lookup_coverage
  target: reconciliation_side.walmart.lookup_coverage.expected
  fields:
    edge_family: reconciliation_semantics
    evidence_basis: source-backed card field dependency
    confidence: high
    canonical_cognee_edge: true
    marketplace_only: true
    canonical_edge_type: HAS_SIDE
    inverse_edge_type: BELONGS_TO_RECONCILIATION_PROFILE
    materialize_inverse: false
    edge_class: canonical
    source_type: reconciliation_profile
    target_type: reconciliation_side
    evidence_refs:
    - ev.walmart.relationships.001
```

```yaml
candidate_edge:
  edge_id: edge.walmart.0261
  edge_type: HAS_SIDE
  source: reconciliation_profile.walmart.lookup_coverage
  target: reconciliation_side.walmart.lookup_coverage.actual
  fields:
    edge_family: reconciliation_semantics
    evidence_basis: source-backed card field dependency
    confidence: high
    canonical_cognee_edge: true
    marketplace_only: true
    canonical_edge_type: HAS_SIDE
    inverse_edge_type: BELONGS_TO_RECONCILIATION_PROFILE
    materialize_inverse: false
    edge_class: canonical
    source_type: reconciliation_profile
    target_type: reconciliation_side
    evidence_refs:
    - ev.walmart.relationships.001
```

```yaml
candidate_edge:
  edge_id: edge.walmart.0262
  edge_type: HAS_UNIT
  source: reconciliation_profile.walmart.lookup_coverage
  target: reconciliation_unit.walmart.lookup_coverage
  fields:
    edge_family: reconciliation_semantics
    evidence_basis: source-backed card field dependency
    confidence: high
    canonical_cognee_edge: true
    marketplace_only: true
    canonical_edge_type: HAS_UNIT
    inverse_edge_type: PRIMARY_UNIT_OF_PROFILE
    materialize_inverse: false
    edge_class: canonical
    source_type: reconciliation_profile
    target_type: reconciliation_unit
    evidence_refs:
    - ev.walmart.relationships.001
```

```yaml
candidate_edge:
  edge_id: edge.walmart.0263
  edge_type: HAS_MATCHING_LOGIC
  source: reconciliation_profile.walmart.lookup_coverage
  target: matching_logic.walmart.lookup_coverage.primary
  fields:
    edge_family: reconciliation_semantics
    evidence_basis: source-backed card field dependency
    confidence: high
    canonical_cognee_edge: true
    marketplace_only: true
    canonical_edge_type: HAS_MATCHING_LOGIC
    inverse_edge_type: SUPPORTS_RECONCILIATION_PROFILE
    materialize_inverse: false
    edge_class: canonical
    source_type: reconciliation_profile
    target_type: matching_logic
    evidence_refs:
    - ev.walmart.relationships.001
```

```yaml
candidate_edge:
  edge_id: edge.walmart.0264
  edge_type: HAS_MISMATCH_CATEGORY
  source: reconciliation_profile.walmart.oms_to_settlement
  target: mismatch_category.walmart.oms_to_settlement.not_in_settlement
  fields:
    edge_family: reconciliation_semantics
    evidence_basis: source-backed card field dependency
    confidence: high
    canonical_cognee_edge: true
    marketplace_only: true
    canonical_edge_type: HAS_MISMATCH_CATEGORY
    inverse_edge_type: MISMATCH_OF_PROFILE
    materialize_inverse: false
    edge_class: canonical
    source_type: reconciliation_profile
    target_type: mismatch_category
    evidence_refs:
    - ev.walmart.relationships.001
```

```yaml
candidate_edge:
  edge_id: edge.walmart.0265
  edge_type: HAS_MISMATCH_CATEGORY
  source: reconciliation_profile.walmart.oms_to_settlement
  target: mismatch_category.walmart.oms_to_settlement.price_variance
  fields:
    edge_family: reconciliation_semantics
    evidence_basis: source-backed card field dependency
    confidence: high
    canonical_cognee_edge: true
    marketplace_only: true
    canonical_edge_type: HAS_MISMATCH_CATEGORY
    inverse_edge_type: MISMATCH_OF_PROFILE
    materialize_inverse: false
    edge_class: canonical
    source_type: reconciliation_profile
    target_type: mismatch_category
    evidence_refs:
    - ev.walmart.reconciliation.001
```

```yaml
candidate_edge:
  edge_id: edge.walmart.0266
  edge_type: HAS_MISMATCH_CATEGORY
  source: reconciliation_profile.walmart.oms_to_settlement
  target: mismatch_category.walmart.oms_to_settlement.expected_timing_gap
  fields:
    edge_family: reconciliation_semantics
    evidence_basis: source-backed card field dependency
    confidence: high
    canonical_cognee_edge: true
    marketplace_only: true
    canonical_edge_type: HAS_MISMATCH_CATEGORY
    inverse_edge_type: MISMATCH_OF_PROFILE
    materialize_inverse: false
    edge_class: canonical
    source_type: reconciliation_profile
    target_type: mismatch_category
    evidence_refs:
    - ev.walmart.relationships.001
```

```yaml
candidate_edge:
  edge_id: edge.walmart.0267
  edge_type: HAS_MISMATCH_CATEGORY
  source: reconciliation_profile.walmart.commission_validation
  target: mismatch_category.walmart.commission.rate_variance
  fields:
    edge_family: reconciliation_semantics
    evidence_basis: source-backed card field dependency
    confidence: high
    canonical_cognee_edge: true
    marketplace_only: true
    canonical_edge_type: HAS_MISMATCH_CATEGORY
    inverse_edge_type: MISMATCH_OF_PROFILE
    materialize_inverse: false
    edge_class: canonical
    source_type: reconciliation_profile
    target_type: mismatch_category
    evidence_refs:
    - ev.walmart.reconciliation.001
```

```yaml
candidate_edge:
  edge_id: edge.walmart.0268
  edge_type: HAS_MISMATCH_CATEGORY
  source: reconciliation_profile.walmart.refund_to_sale
  target: mismatch_category.walmart.refund_to_sale.missing_original_sale
  fields:
    edge_family: reconciliation_semantics
    evidence_basis: source-backed card field dependency
    confidence: high
    canonical_cognee_edge: true
    marketplace_only: true
    canonical_edge_type: HAS_MISMATCH_CATEGORY
    inverse_edge_type: MISMATCH_OF_PROFILE
    materialize_inverse: false
    edge_class: canonical
    source_type: reconciliation_profile
    target_type: mismatch_category
    evidence_refs:
    - ev.walmart.reconciliation.001
```

```yaml
candidate_edge:
  edge_id: edge.walmart.0269
  edge_type: HAS_MISMATCH_CATEGORY
  source: reconciliation_profile.walmart.mpf_tax_identity
  target: mismatch_category.walmart.mpf_tax.identity_break
  fields:
    edge_family: reconciliation_semantics
    evidence_basis: source-backed card field dependency
    confidence: high
    canonical_cognee_edge: true
    marketplace_only: true
    canonical_edge_type: HAS_MISMATCH_CATEGORY
    inverse_edge_type: MISMATCH_OF_PROFILE
    materialize_inverse: false
    edge_class: canonical
    source_type: reconciliation_profile
    target_type: mismatch_category
    evidence_refs:
    - ev.walmart.business_model.001
```

```yaml
candidate_edge:
  edge_id: edge.walmart.0270
  edge_type: HAS_MISMATCH_CATEGORY
  source: reconciliation_profile.walmart.lookup_coverage
  target: mismatch_category.walmart.lookup.sku_missing
  fields:
    edge_family: reconciliation_semantics
    evidence_basis: source-backed card field dependency
    confidence: high
    canonical_cognee_edge: true
    marketplace_only: true
    canonical_edge_type: HAS_MISMATCH_CATEGORY
    inverse_edge_type: MISMATCH_OF_PROFILE
    materialize_inverse: false
    edge_class: canonical
    source_type: reconciliation_profile
    target_type: mismatch_category
    evidence_refs:
    - ev.walmart_lookup.schema.001
```

```yaml
candidate_edge:
  edge_id: edge.walmart.0271
  edge_type: ANSWERS_WITH_METRIC
  source: query_pattern.walmart.forward_gmv_net_payout
  target: metric.marketplace.net_seller_payout
  fields:
    edge_family: query_output_semantics
    evidence_basis: source-backed card field dependency
    confidence: high
    canonical_cognee_edge: true
    marketplace_only: true
    canonical_edge_type: ANSWERS_WITH_METRIC
    inverse_edge_type: PRODUCED_BY_QUERY_PATTERN
    materialize_inverse: false
    edge_class: canonical
    source_type: query_pattern
    target_type: metric
    evidence_refs:
    - ev.walmart.metrics.001
```

```yaml
candidate_edge:
  edge_id: edge.walmart.0272
  edge_type: USES_TABLE
  source: query_pattern.walmart.forward_gmv_net_payout
  target: table.zs_observe.walmart_settlement
  fields:
    edge_family: dependency_usage
    evidence_basis: source-backed card field dependency
    confidence: high
    canonical_cognee_edge: true
    marketplace_only: true
    canonical_edge_type: USES_TABLE
    inverse_edge_type: USED_BY_CARD
    materialize_inverse: false
    edge_class: canonical
    source_type: query_pattern
    target_type: table
    evidence_refs:
    - ev.walmart.metrics.001
```

```yaml
candidate_edge:
  edge_id: edge.walmart.0273
  edge_type: ANSWERS_WITH_METRIC
  source: query_pattern.walmart.return_rate
  target: metric.marketplace.return_rate
  fields:
    edge_family: query_output_semantics
    evidence_basis: source-backed card field dependency
    confidence: high
    canonical_cognee_edge: true
    marketplace_only: true
    canonical_edge_type: ANSWERS_WITH_METRIC
    inverse_edge_type: PRODUCED_BY_QUERY_PATTERN
    materialize_inverse: false
    edge_class: canonical
    source_type: query_pattern
    target_type: metric
    evidence_refs:
    - ev.walmart.metrics.001
```

```yaml
candidate_edge:
  edge_id: edge.walmart.0274
  edge_type: USES_TABLE
  source: query_pattern.walmart.return_rate
  target: table.zs_observe.walmart_settlement
  fields:
    edge_family: dependency_usage
    evidence_basis: source-backed card field dependency
    confidence: high
    canonical_cognee_edge: true
    marketplace_only: true
    canonical_edge_type: USES_TABLE
    inverse_edge_type: USED_BY_CARD
    materialize_inverse: false
    edge_class: canonical
    source_type: query_pattern
    target_type: table
    evidence_refs:
    - ev.walmart.metrics.001
```

```yaml
candidate_edge:
  edge_id: edge.walmart.0275
  edge_type: ANSWERS_WITH_METRIC
  source: query_pattern.walmart.oms_aov
  target: metric.marketplace.average_order_value
  fields:
    edge_family: query_output_semantics
    evidence_basis: source-backed card field dependency
    confidence: high
    canonical_cognee_edge: true
    marketplace_only: true
    canonical_edge_type: ANSWERS_WITH_METRIC
    inverse_edge_type: PRODUCED_BY_QUERY_PATTERN
    materialize_inverse: false
    edge_class: canonical
    source_type: query_pattern
    target_type: metric
    evidence_refs:
    - ev.walmart.metrics.001
```

```yaml
candidate_edge:
  edge_id: edge.walmart.0276
  edge_type: USES_TABLE
  source: query_pattern.walmart.oms_aov
  target: table.zs_observe.walmart_oms
  fields:
    edge_family: dependency_usage
    evidence_basis: source-backed card field dependency
    confidence: high
    canonical_cognee_edge: true
    marketplace_only: true
    canonical_edge_type: USES_TABLE
    inverse_edge_type: USED_BY_CARD
    materialize_inverse: false
    edge_class: canonical
    source_type: query_pattern
    target_type: table
    evidence_refs:
    - ev.walmart.metrics.001
```

```yaml
candidate_edge:
  edge_id: edge.walmart.0277
  edge_type: ANSWERS_WITH_METRIC
  source: query_pattern.walmart.cancellation_rate
  target: metric.marketplace.cancellation_rate
  fields:
    edge_family: query_output_semantics
    evidence_basis: source-backed card field dependency
    confidence: high
    canonical_cognee_edge: true
    marketplace_only: true
    canonical_edge_type: ANSWERS_WITH_METRIC
    inverse_edge_type: PRODUCED_BY_QUERY_PATTERN
    materialize_inverse: false
    edge_class: canonical
    source_type: query_pattern
    target_type: metric
    evidence_refs:
    - ev.walmart_oms.schema.001
```

```yaml
candidate_edge:
  edge_id: edge.walmart.0278
  edge_type: USES_TABLE
  source: query_pattern.walmart.cancellation_rate
  target: table.zs_observe.walmart_oms
  fields:
    edge_family: dependency_usage
    evidence_basis: source-backed card field dependency
    confidence: high
    canonical_cognee_edge: true
    marketplace_only: true
    canonical_edge_type: USES_TABLE
    inverse_edge_type: USED_BY_CARD
    materialize_inverse: false
    edge_class: canonical
    source_type: query_pattern
    target_type: table
    evidence_refs:
    - ev.walmart_oms.schema.001
```

```yaml
candidate_edge:
  edge_id: edge.walmart.0279
  edge_type: ANSWERS_WITH_METRIC
  source: query_pattern.walmart.monthly_revenue
  target: metric.marketplace.net_seller_payout
  fields:
    edge_family: query_output_semantics
    evidence_basis: source-backed card field dependency
    confidence: high
    canonical_cognee_edge: true
    marketplace_only: true
    canonical_edge_type: ANSWERS_WITH_METRIC
    inverse_edge_type: PRODUCED_BY_QUERY_PATTERN
    materialize_inverse: false
    edge_class: canonical
    source_type: query_pattern
    target_type: metric
    evidence_refs:
    - ev.walmart.metrics.001
```

```yaml
candidate_edge:
  edge_id: edge.walmart.0280
  edge_type: USES_TABLE
  source: query_pattern.walmart.monthly_revenue
  target: table.zs_observe.walmart_settlement
  fields:
    edge_family: dependency_usage
    evidence_basis: source-backed card field dependency
    confidence: high
    canonical_cognee_edge: true
    marketplace_only: true
    canonical_edge_type: USES_TABLE
    inverse_edge_type: USED_BY_CARD
    materialize_inverse: false
    edge_class: canonical
    source_type: query_pattern
    target_type: table
    evidence_refs:
    - ev.walmart.metrics.001
```

```yaml
candidate_edge:
  edge_id: edge.walmart.0281
  edge_type: ANSWERS_WITH_METRIC
  source: query_pattern.walmart.top_skus
  target: metric.marketplace.sku_revenue
  fields:
    edge_family: query_output_semantics
    evidence_basis: source-backed card field dependency
    confidence: high
    canonical_cognee_edge: true
    marketplace_only: true
    canonical_edge_type: ANSWERS_WITH_METRIC
    inverse_edge_type: PRODUCED_BY_QUERY_PATTERN
    materialize_inverse: false
    edge_class: canonical
    source_type: query_pattern
    target_type: metric
    evidence_refs:
    - ev.walmart.metrics.001
```

```yaml
candidate_edge:
  edge_id: edge.walmart.0282
  edge_type: USES_TABLE
  source: query_pattern.walmart.top_skus
  target: table.zs_observe.walmart_settlement
  fields:
    edge_family: dependency_usage
    evidence_basis: source-backed card field dependency
    confidence: high
    canonical_cognee_edge: true
    marketplace_only: true
    canonical_edge_type: USES_TABLE
    inverse_edge_type: USED_BY_CARD
    materialize_inverse: false
    edge_class: canonical
    source_type: query_pattern
    target_type: table
    evidence_refs:
    - ev.walmart.metrics.001
```

```yaml
candidate_edge:
  edge_id: edge.walmart.0283
  edge_type: USES_TABLE
  source: query_pattern.walmart.top_skus
  target: table.zs_observe.walmart_lookup
  fields:
    edge_family: dependency_usage
    evidence_basis: source-backed card field dependency
    confidence: high
    canonical_cognee_edge: true
    marketplace_only: true
    canonical_edge_type: USES_TABLE
    inverse_edge_type: USED_BY_CARD
    materialize_inverse: false
    edge_class: canonical
    source_type: query_pattern
    target_type: table
    evidence_refs:
    - ev.walmart.metrics.001
```

```yaml
candidate_edge:
  edge_id: edge.walmart.0284
  edge_type: ANSWERS_WITH_METRIC
  source: query_pattern.walmart.state_distribution
  target: metric.marketplace.revenue_by_state
  fields:
    edge_family: query_output_semantics
    evidence_basis: source-backed card field dependency
    confidence: high
    canonical_cognee_edge: true
    marketplace_only: true
    canonical_edge_type: ANSWERS_WITH_METRIC
    inverse_edge_type: PRODUCED_BY_QUERY_PATTERN
    materialize_inverse: false
    edge_class: canonical
    source_type: query_pattern
    target_type: metric
    evidence_refs:
    - ev.walmart.metrics.001
```

```yaml
candidate_edge:
  edge_id: edge.walmart.0285
  edge_type: USES_TABLE
  source: query_pattern.walmart.state_distribution
  target: table.zs_observe.walmart_oms
  fields:
    edge_family: dependency_usage
    evidence_basis: source-backed card field dependency
    confidence: high
    canonical_cognee_edge: true
    marketplace_only: true
    canonical_edge_type: USES_TABLE
    inverse_edge_type: USED_BY_CARD
    materialize_inverse: false
    edge_class: canonical
    source_type: query_pattern
    target_type: table
    evidence_refs:
    - ev.walmart.metrics.001
```

```yaml
candidate_edge:
  edge_id: edge.walmart.0286
  edge_type: ANSWERS_WITH_METRIC
  source: query_pattern.walmart.payout_cycle
  target: metric.marketplace.net_seller_payout
  fields:
    edge_family: query_output_semantics
    evidence_basis: source-backed card field dependency
    confidence: high
    canonical_cognee_edge: true
    marketplace_only: true
    canonical_edge_type: ANSWERS_WITH_METRIC
    inverse_edge_type: PRODUCED_BY_QUERY_PATTERN
    materialize_inverse: false
    edge_class: canonical
    source_type: query_pattern
    target_type: metric
    evidence_refs:
    - ev.walmart.metrics.001
```

```yaml
candidate_edge:
  edge_id: edge.walmart.0287
  edge_type: USES_TABLE
  source: query_pattern.walmart.payout_cycle
  target: table.zs_observe.walmart_settlement
  fields:
    edge_family: dependency_usage
    evidence_basis: source-backed card field dependency
    confidence: high
    canonical_cognee_edge: true
    marketplace_only: true
    canonical_edge_type: USES_TABLE
    inverse_edge_type: USED_BY_CARD
    materialize_inverse: false
    edge_class: canonical
    source_type: query_pattern
    target_type: table
    evidence_refs:
    - ev.walmart.metrics.001
```

```yaml
candidate_edge:
  edge_id: edge.walmart.0288
  edge_type: ANSWERS_WITH_METRIC
  source: query_pattern.walmart.oms_settlement_reconciliation
  target: metric.marketplace.gross_revenue
  fields:
    edge_family: query_output_semantics
    evidence_basis: source-backed card field dependency
    confidence: high
    canonical_cognee_edge: true
    marketplace_only: true
    canonical_edge_type: ANSWERS_WITH_METRIC
    inverse_edge_type: PRODUCED_BY_QUERY_PATTERN
    materialize_inverse: false
    edge_class: canonical
    source_type: query_pattern
    target_type: metric
    evidence_refs:
    - ev.walmart.reconciliation.001
```

```yaml
candidate_edge:
  edge_id: edge.walmart.0289
  edge_type: USES_TABLE
  source: query_pattern.walmart.oms_settlement_reconciliation
  target: table.zs_observe.walmart_oms
  fields:
    edge_family: dependency_usage
    evidence_basis: source-backed card field dependency
    confidence: high
    canonical_cognee_edge: true
    marketplace_only: true
    canonical_edge_type: USES_TABLE
    inverse_edge_type: USED_BY_CARD
    materialize_inverse: false
    edge_class: canonical
    source_type: query_pattern
    target_type: table
    evidence_refs:
    - ev.walmart.reconciliation.001
```

```yaml
candidate_edge:
  edge_id: edge.walmart.0290
  edge_type: USES_TABLE
  source: query_pattern.walmart.oms_settlement_reconciliation
  target: table.zs_observe.walmart_settlement
  fields:
    edge_family: dependency_usage
    evidence_basis: source-backed card field dependency
    confidence: high
    canonical_cognee_edge: true
    marketplace_only: true
    canonical_edge_type: USES_TABLE
    inverse_edge_type: USED_BY_CARD
    materialize_inverse: false
    edge_class: canonical
    source_type: query_pattern
    target_type: table
    evidence_refs:
    - ev.walmart.reconciliation.001
```

```yaml
candidate_edge:
  edge_id: edge.walmart.0291
  edge_type: ANSWERS_WITH_METRIC
  source: query_pattern.walmart.commission_validation
  target: metric.marketplace.effective_commission_rate
  fields:
    edge_family: query_output_semantics
    evidence_basis: source-backed card field dependency
    confidence: high
    canonical_cognee_edge: true
    marketplace_only: true
    canonical_edge_type: ANSWERS_WITH_METRIC
    inverse_edge_type: PRODUCED_BY_QUERY_PATTERN
    materialize_inverse: false
    edge_class: canonical
    source_type: query_pattern
    target_type: metric
    evidence_refs:
    - ev.walmart.reconciliation.001
```

```yaml
candidate_edge:
  edge_id: edge.walmart.0292
  edge_type: USES_TABLE
  source: query_pattern.walmart.commission_validation
  target: table.zs_observe.walmart_settlement
  fields:
    edge_family: dependency_usage
    evidence_basis: source-backed card field dependency
    confidence: high
    canonical_cognee_edge: true
    marketplace_only: true
    canonical_edge_type: USES_TABLE
    inverse_edge_type: USED_BY_CARD
    materialize_inverse: false
    edge_class: canonical
    source_type: query_pattern
    target_type: table
    evidence_refs:
    - ev.walmart.reconciliation.001
```

```yaml
candidate_edge:
  edge_id: edge.walmart.0293
  edge_type: ANSWERS_WITH_METRIC
  source: query_pattern.walmart.refund_sale_match
  target: metric.marketplace.return_rate
  fields:
    edge_family: query_output_semantics
    evidence_basis: source-backed card field dependency
    confidence: high
    canonical_cognee_edge: true
    marketplace_only: true
    canonical_edge_type: ANSWERS_WITH_METRIC
    inverse_edge_type: PRODUCED_BY_QUERY_PATTERN
    materialize_inverse: false
    edge_class: canonical
    source_type: query_pattern
    target_type: metric
    evidence_refs:
    - ev.walmart.reconciliation.001
```

```yaml
candidate_edge:
  edge_id: edge.walmart.0294
  edge_type: USES_TABLE
  source: query_pattern.walmart.refund_sale_match
  target: table.zs_observe.walmart_settlement
  fields:
    edge_family: dependency_usage
    evidence_basis: source-backed card field dependency
    confidence: high
    canonical_cognee_edge: true
    marketplace_only: true
    canonical_edge_type: USES_TABLE
    inverse_edge_type: USED_BY_CARD
    materialize_inverse: false
    edge_class: canonical
    source_type: query_pattern
    target_type: table
    evidence_refs:
    - ev.walmart.reconciliation.001
```

```yaml
candidate_edge:
  edge_id: edge.walmart.0295
  edge_type: ANSWERS_WITH_METRIC
  source: query_pattern.walmart.full_three_table_view
  target: metric.marketplace.net_seller_payout
  fields:
    edge_family: query_output_semantics
    evidence_basis: source-backed card field dependency
    confidence: high
    canonical_cognee_edge: true
    marketplace_only: true
    canonical_edge_type: ANSWERS_WITH_METRIC
    inverse_edge_type: PRODUCED_BY_QUERY_PATTERN
    materialize_inverse: false
    edge_class: canonical
    source_type: query_pattern
    target_type: metric
    evidence_refs:
    - ev.walmart.reconciliation.001
```

```yaml
candidate_edge:
  edge_id: edge.walmart.0296
  edge_type: USES_TABLE
  source: query_pattern.walmart.full_three_table_view
  target: table.zs_observe.walmart_oms
  fields:
    edge_family: dependency_usage
    evidence_basis: source-backed card field dependency
    confidence: high
    canonical_cognee_edge: true
    marketplace_only: true
    canonical_edge_type: USES_TABLE
    inverse_edge_type: USED_BY_CARD
    materialize_inverse: false
    edge_class: canonical
    source_type: query_pattern
    target_type: table
    evidence_refs:
    - ev.walmart.reconciliation.001
```

```yaml
candidate_edge:
  edge_id: edge.walmart.0297
  edge_type: USES_TABLE
  source: query_pattern.walmart.full_three_table_view
  target: table.zs_observe.walmart_settlement
  fields:
    edge_family: dependency_usage
    evidence_basis: source-backed card field dependency
    confidence: high
    canonical_cognee_edge: true
    marketplace_only: true
    canonical_edge_type: USES_TABLE
    inverse_edge_type: USED_BY_CARD
    materialize_inverse: false
    edge_class: canonical
    source_type: query_pattern
    target_type: table
    evidence_refs:
    - ev.walmart.reconciliation.001
```

```yaml
candidate_edge:
  edge_id: edge.walmart.0298
  edge_type: USES_TABLE
  source: query_pattern.walmart.full_three_table_view
  target: table.zs_observe.walmart_lookup
  fields:
    edge_family: dependency_usage
    evidence_basis: source-backed card field dependency
    confidence: high
    canonical_cognee_edge: true
    marketplace_only: true
    canonical_edge_type: USES_TABLE
    inverse_edge_type: USED_BY_CARD
    materialize_inverse: false
    edge_class: canonical
    source_type: query_pattern
    target_type: table
    evidence_refs:
    - ev.walmart.reconciliation.001
```

```yaml
candidate_edge:
  edge_id: edge.walmart.0299
  edge_type: ANSWERS_WITH_METRIC
  source: query_pattern.walmart.lookup_catalogue
  target: metric.marketplace.sku_revenue
  fields:
    edge_family: query_output_semantics
    evidence_basis: source-backed card field dependency
    confidence: high
    canonical_cognee_edge: true
    marketplace_only: true
    canonical_edge_type: ANSWERS_WITH_METRIC
    inverse_edge_type: PRODUCED_BY_QUERY_PATTERN
    materialize_inverse: false
    edge_class: canonical
    source_type: query_pattern
    target_type: metric
    evidence_refs:
    - ev.walmart_lookup.schema.001
```

```yaml
candidate_edge:
  edge_id: edge.walmart.0300
  edge_type: USES_TABLE
  source: query_pattern.walmart.lookup_catalogue
  target: table.zs_observe.walmart_lookup
  fields:
    edge_family: dependency_usage
    evidence_basis: source-backed card field dependency
    confidence: high
    canonical_cognee_edge: true
    marketplace_only: true
    canonical_edge_type: USES_TABLE
    inverse_edge_type: USED_BY_CARD
    materialize_inverse: false
    edge_class: canonical
    source_type: query_pattern
    target_type: table
    evidence_refs:
    - ev.walmart_lookup.schema.001
```

```yaml
candidate_edge:
  edge_id: edge.walmart.0301
  edge_type: ANSWERS_WITH_METRIC
  source: query_pattern.walmart.mpf_tax_validation
  target: metric.marketplace.tax_withheld
  fields:
    edge_family: query_output_semantics
    evidence_basis: source-backed card field dependency
    confidence: high
    canonical_cognee_edge: true
    marketplace_only: true
    canonical_edge_type: ANSWERS_WITH_METRIC
    inverse_edge_type: PRODUCED_BY_QUERY_PATTERN
    materialize_inverse: false
    edge_class: canonical
    source_type: query_pattern
    target_type: metric
    evidence_refs:
    - ev.walmart.business_model.001
```

```yaml
candidate_edge:
  edge_id: edge.walmart.0302
  edge_type: USES_TABLE
  source: query_pattern.walmart.mpf_tax_validation
  target: table.zs_observe.walmart_settlement
  fields:
    edge_family: dependency_usage
    evidence_basis: source-backed card field dependency
    confidence: high
    canonical_cognee_edge: true
    marketplace_only: true
    canonical_edge_type: USES_TABLE
    inverse_edge_type: USED_BY_CARD
    materialize_inverse: false
    edge_class: canonical
    source_type: query_pattern
    target_type: table
    evidence_refs:
    - ev.walmart.business_model.001
```

```yaml
candidate_edge:
  edge_id: edge.walmart.0303
  edge_type: ANSWERS_WITH_METRIC
  source: query_pattern.walmart.wfs_fee_visibility
  target: metric.marketplace.net_seller_payout
  fields:
    edge_family: query_output_semantics
    evidence_basis: source-backed card field dependency
    confidence: high
    canonical_cognee_edge: true
    marketplace_only: true
    canonical_edge_type: ANSWERS_WITH_METRIC
    inverse_edge_type: PRODUCED_BY_QUERY_PATTERN
    materialize_inverse: false
    edge_class: canonical
    source_type: query_pattern
    target_type: metric
    evidence_refs:
    - ev.walmart.quality.001
```

```yaml
candidate_edge:
  edge_id: edge.walmart.0304
  edge_type: USES_TABLE
  source: query_pattern.walmart.wfs_fee_visibility
  target: table.zs_observe.walmart_settlement
  fields:
    edge_family: dependency_usage
    evidence_basis: source-backed card field dependency
    confidence: high
    canonical_cognee_edge: true
    marketplace_only: true
    canonical_edge_type: USES_TABLE
    inverse_edge_type: USED_BY_CARD
    materialize_inverse: false
    edge_class: canonical
    source_type: query_pattern
    target_type: table
    evidence_refs:
    - ev.walmart.quality.001
```

```yaml
candidate_edge:
  edge_id: edge.walmart.0305
  edge_type: USES_RELATIONSHIP
  source: reconciliation_profile.walmart.oms_to_settlement
  target: relationship.walmart.oms_to_settlement_order_id
  fields:
    edge_family: dependency_usage
    evidence_basis: source-backed card field dependency
    confidence: high
    canonical_cognee_edge: true
    marketplace_only: true
    canonical_edge_type: USES_RELATIONSHIP
    inverse_edge_type: USED_BY_QUERY_PATTERN
    materialize_inverse: false
    edge_class: canonical
    source_type: reconciliation_profile
    target_type: relationship
    evidence_refs:
    - ev.walmart.relationships.001
```

```yaml
candidate_edge:
  edge_id: edge.walmart.0306
  edge_type: USES_RELATIONSHIP
  source: reconciliation_profile.walmart.lookup_coverage
  target: relationship.walmart.oms_to_lookup_sku
  fields:
    edge_family: dependency_usage
    evidence_basis: source-backed card field dependency
    confidence: high
    canonical_cognee_edge: true
    marketplace_only: true
    canonical_edge_type: USES_RELATIONSHIP
    inverse_edge_type: USED_BY_QUERY_PATTERN
    materialize_inverse: false
    edge_class: canonical
    source_type: reconciliation_profile
    target_type: relationship
    evidence_refs:
    - ev.walmart.relationships.001
```

```yaml
candidate_edge:
  edge_id: edge.walmart.0307
  edge_type: USES_RELATIONSHIP
  source: reconciliation_profile.walmart.lookup_coverage
  target: relationship.walmart.settlement_to_lookup_sku
  fields:
    edge_family: dependency_usage
    evidence_basis: source-backed card field dependency
    confidence: high
    canonical_cognee_edge: true
    marketplace_only: true
    canonical_edge_type: USES_RELATIONSHIP
    inverse_edge_type: USED_BY_QUERY_PATTERN
    materialize_inverse: false
    edge_class: canonical
    source_type: reconciliation_profile
    target_type: relationship
    evidence_refs:
    - ev.walmart.relationships.001
```

```yaml
candidate_edge:
  edge_id: edge.walmart.0308
  edge_type: USES_TABLE
  source: reconciliation_profile.walmart.refund_to_sale
  target: table.zs_observe.walmart_settlement
  fields:
    edge_family: dependency_usage
    evidence_basis: source-backed card field dependency
    confidence: high
    canonical_cognee_edge: true
    marketplace_only: true
    canonical_edge_type: USES_TABLE
    inverse_edge_type: USED_BY_CARD
    materialize_inverse: false
    edge_class: canonical
    source_type: reconciliation_profile
    target_type: table
    evidence_refs:
    - ev.walmart.reconciliation.001
```

```yaml
candidate_edge:
  edge_id: edge.walmart.0309
  edge_type: USES_TABLE
  source: formula_template.walmart.net_seller_payout
  target: table.zs_observe.walmart_settlement
  fields:
    edge_family: dependency_usage
    evidence_basis: source-backed card field dependency
    confidence: high
    canonical_cognee_edge: true
    marketplace_only: true
    canonical_edge_type: USES_TABLE
    inverse_edge_type: USED_BY_CARD
    materialize_inverse: false
    edge_class: canonical
    source_type: formula_template
    target_type: table
    evidence_refs:
    - ev.walmart.business_model.001
```

```yaml
candidate_edge:
  edge_id: edge.walmart.0310
  edge_type: USES_TABLE
  source: formula_template.walmart.mpf_tax_identity
  target: table.zs_observe.walmart_settlement
  fields:
    edge_family: dependency_usage
    evidence_basis: source-backed card field dependency
    confidence: high
    canonical_cognee_edge: true
    marketplace_only: true
    canonical_edge_type: USES_TABLE
    inverse_edge_type: USED_BY_CARD
    materialize_inverse: false
    edge_class: canonical
    source_type: formula_template
    target_type: table
    evidence_refs:
    - ev.walmart.business_model.001
```

```yaml
candidate_edge:
  edge_id: edge.walmart.0311
  edge_type: USES_TABLE
  source: formula_template.walmart.effective_commission_rate
  target: table.zs_observe.walmart_settlement
  fields:
    edge_family: dependency_usage
    evidence_basis: source-backed card field dependency
    confidence: high
    canonical_cognee_edge: true
    marketplace_only: true
    canonical_edge_type: USES_TABLE
    inverse_edge_type: USED_BY_CARD
    materialize_inverse: false
    edge_class: canonical
    source_type: formula_template
    target_type: table
    evidence_refs:
    - ev.walmart.quality.001
```

```yaml
candidate_edge:
  edge_id: edge.walmart.0312
  edge_type: USES_TABLE
  source: formula_template.walmart.refund_reversal
  target: table.zs_observe.walmart_settlement
  fields:
    edge_family: dependency_usage
    evidence_basis: source-backed card field dependency
    confidence: high
    canonical_cognee_edge: true
    marketplace_only: true
    canonical_edge_type: USES_TABLE
    inverse_edge_type: USED_BY_CARD
    materialize_inverse: false
    edge_class: canonical
    source_type: formula_template
    target_type: table
    evidence_refs:
    - ev.walmart.lifecycle.001
```

```yaml
candidate_edge:
  edge_id: edge.walmart.0313
  edge_type: ENFORCES_FORMULA
  source: rule.walmart.no_settled_amount_payout
  target: formula_template.walmart.net_seller_payout
  fields:
    edge_family: canonical
    evidence_basis: source-backed card field dependency
    confidence: high
    canonical_cognee_edge: true
    marketplace_only: true
    canonical_edge_type: ENFORCES_FORMULA
    inverse_edge_type: FORMULA_ENFORCED_BY_RULE
    materialize_inverse: false
    edge_class: canonical
    source_type: rule
    target_type: formula_template
    evidence_refs:
    - ev.walmart.business_model.001
```

```yaml
candidate_edge:
  edge_id: edge.walmart.0314
  edge_type: ENFORCES_FORMULA
  source: rule.walmart.mpf_tax_not_seller_revenue
  target: formula_template.walmart.mpf_tax_identity
  fields:
    edge_family: canonical
    evidence_basis: source-backed card field dependency
    confidence: high
    canonical_cognee_edge: true
    marketplace_only: true
    canonical_edge_type: ENFORCES_FORMULA
    inverse_edge_type: FORMULA_ENFORCED_BY_RULE
    materialize_inverse: false
    edge_class: canonical
    source_type: rule
    target_type: formula_template
    evidence_refs:
    - ev.walmart.business_model.001
```

```yaml
candidate_edge:
  edge_id: edge.walmart.0315
  edge_type: ENFORCES_FORMULA
  source: rule.walmart.compute_commission_rate
  target: formula_template.walmart.effective_commission_rate
  fields:
    edge_family: canonical
    evidence_basis: source-backed card field dependency
    confidence: high
    canonical_cognee_edge: true
    marketplace_only: true
    canonical_edge_type: ENFORCES_FORMULA
    inverse_edge_type: FORMULA_ENFORCED_BY_RULE
    materialize_inverse: false
    edge_class: canonical
    source_type: rule
    target_type: formula_template
    evidence_refs:
    - ev.walmart.quality.001
```

```yaml
candidate_edge:
  edge_id: edge.walmart.0316
  edge_type: ENFORCES_FORMULA
  source: rule.walmart.reverse_refund_filter
  target: formula_template.walmart.refund_reversal
  fields:
    edge_family: canonical
    evidence_basis: source-backed card field dependency
    confidence: high
    canonical_cognee_edge: true
    marketplace_only: true
    canonical_edge_type: ENFORCES_FORMULA
    inverse_edge_type: FORMULA_ENFORCED_BY_RULE
    materialize_inverse: false
    edge_class: canonical
    source_type: rule
    target_type: formula_template
    evidence_refs:
    - ev.walmart.lifecycle.001
```

```yaml
candidate_edge:
  edge_id: edge.walmart.0317
  edge_type: RECONCILED_BY
  source: business_process.walmart.forward_wfs_sale_to_payout
  target: reconciliation_profile.walmart.oms_to_settlement
  fields:
    edge_family: reconciliation_semantics
    evidence_basis: source-backed card field dependency
    confidence: high
    canonical_cognee_edge: true
    marketplace_only: true
    canonical_edge_type: RECONCILED_BY
    inverse_edge_type: SUPPORTS_PROCESS
    materialize_inverse: false
    edge_class: canonical
    source_type: business_process
    target_type: reconciliation_profile
    evidence_refs:
    - ev.walmart.reconciliation.001
```

```yaml
candidate_edge:
  edge_id: edge.walmart.0318
  edge_type: RECONCILED_BY
  source: business_process.walmart.refund_to_payout_deduction
  target: reconciliation_profile.walmart.refund_to_sale
  fields:
    edge_family: reconciliation_semantics
    evidence_basis: source-backed card field dependency
    confidence: high
    canonical_cognee_edge: true
    marketplace_only: true
    canonical_edge_type: RECONCILED_BY
    inverse_edge_type: SUPPORTS_PROCESS
    materialize_inverse: false
    edge_class: canonical
    source_type: business_process
    target_type: reconciliation_profile
    evidence_refs:
    - ev.walmart.reconciliation.001
```

```yaml
candidate_edge:
  edge_id: edge.walmart.0319
  edge_type: VALIDATED_BY
  source: business_process.walmart.forward_wfs_sale_to_payout
  target: reconciliation_profile.walmart.commission_validation
  fields:
    edge_family: reconciliation_semantics
    evidence_basis: source-backed card field dependency
    confidence: high
    canonical_cognee_edge: true
    marketplace_only: true
    canonical_edge_type: VALIDATED_BY
    inverse_edge_type: VALIDATES_PROCESS
    materialize_inverse: false
    edge_class: canonical
    source_type: business_process
    target_type: reconciliation_profile
    evidence_refs:
    - ev.walmart.reconciliation.001
```

```yaml
candidate_edge:
  edge_id: edge.walmart.0320
  edge_type: VALIDATED_BY
  source: business_process.walmart.catalogue_enrichment
  target: reconciliation_profile.walmart.lookup_coverage
  fields:
    edge_family: reconciliation_semantics
    evidence_basis: source-backed card field dependency
    confidence: high
    canonical_cognee_edge: true
    marketplace_only: true
    canonical_edge_type: VALIDATED_BY
    inverse_edge_type: VALIDATES_PROCESS
    materialize_inverse: false
    edge_class: canonical
    source_type: business_process
    target_type: reconciliation_profile
    evidence_refs:
    - ev.walmart.relationships.001
```

```yaml
candidate_edge:
  edge_id: edge.walmart.0321
  edge_type: HAS_CONTEXT
  source: domain.marketplace.walmart.orders
  target: platform_context.walmart.us
  fields:
    edge_family: business_hierarchy_in_scope
    evidence_basis: Explicit platform_context binding from card field.
    confidence: high
    canonical_cognee_edge: true
    marketplace_only: true
    canonical_edge_type: HAS_CONTEXT
    inverse_edge_type: BELONGS_TO_CONTEXT
    materialize_inverse: false
    edge_class: canonical
    source_type: domain
    target_type: platform_context
    evidence_refs:
    - ev.walmart_oms.schema.001
    notes: Explicit platform_context binding from card field.
```

```yaml
candidate_edge:
  edge_id: edge.walmart.0322
  edge_type: HAS_CONTEXT
  source: domain.marketplace.walmart.settlement
  target: platform_context.walmart.us
  fields:
    edge_family: business_hierarchy_in_scope
    evidence_basis: Explicit platform_context binding from card field.
    confidence: high
    canonical_cognee_edge: true
    marketplace_only: true
    canonical_edge_type: HAS_CONTEXT
    inverse_edge_type: BELONGS_TO_CONTEXT
    materialize_inverse: false
    edge_class: canonical
    source_type: domain
    target_type: platform_context
    evidence_refs:
    - ev.walmart_settlement.schema.001
    notes: Explicit platform_context binding from card field.
```

```yaml
candidate_edge:
  edge_id: edge.walmart.0323
  edge_type: HAS_CONTEXT
  source: domain.marketplace.walmart.catalogue
  target: platform_context.walmart.us
  fields:
    edge_family: business_hierarchy_in_scope
    evidence_basis: Explicit platform_context binding from card field.
    confidence: high
    canonical_cognee_edge: true
    marketplace_only: true
    canonical_edge_type: HAS_CONTEXT
    inverse_edge_type: BELONGS_TO_CONTEXT
    materialize_inverse: false
    edge_class: canonical
    source_type: domain
    target_type: platform_context
    evidence_refs:
    - ev.walmart_lookup.schema.001
    notes: Explicit platform_context binding from card field.
```

```yaml
candidate_edge:
  edge_id: edge.walmart.0324
  edge_type: HAS_CONTEXT
  source: domain.marketplace.walmart.fees
  target: platform_context.walmart.us
  fields:
    edge_family: business_hierarchy_in_scope
    evidence_basis: Explicit platform_context binding from card field.
    confidence: high
    canonical_cognee_edge: true
    marketplace_only: true
    canonical_edge_type: HAS_CONTEXT
    inverse_edge_type: BELONGS_TO_CONTEXT
    materialize_inverse: false
    edge_class: canonical
    source_type: domain
    target_type: platform_context
    evidence_refs:
    - ev.walmart.business_model.001
    notes: Explicit platform_context binding from card field.
```

```yaml
candidate_edge:
  edge_id: edge.walmart.0325
  edge_type: HAS_CONTEXT
  source: domain.marketplace.walmart.tax
  target: platform_context.walmart.us
  fields:
    edge_family: business_hierarchy_in_scope
    evidence_basis: Explicit platform_context binding from card field.
    confidence: high
    canonical_cognee_edge: true
    marketplace_only: true
    canonical_edge_type: HAS_CONTEXT
    inverse_edge_type: BELONGS_TO_CONTEXT
    materialize_inverse: false
    edge_class: canonical
    source_type: domain
    target_type: platform_context
    evidence_refs:
    - ev.walmart.business_model.001
    notes: Explicit platform_context binding from card field.
```

```yaml
candidate_edge:
  edge_id: edge.walmart.0326
  edge_type: HAS_CONTEXT
  source: domain.marketplace.walmart.returns
  target: platform_context.walmart.us
  fields:
    edge_family: business_hierarchy_in_scope
    evidence_basis: Explicit platform_context binding from card field.
    confidence: high
    canonical_cognee_edge: true
    marketplace_only: true
    canonical_edge_type: HAS_CONTEXT
    inverse_edge_type: BELONGS_TO_CONTEXT
    materialize_inverse: false
    edge_class: canonical
    source_type: domain
    target_type: platform_context
    evidence_refs:
    - ev.walmart.lifecycle.001
    notes: Explicit platform_context binding from card field.
```

```yaml
candidate_edge:
  edge_id: edge.walmart.0327
  edge_type: HAS_CONTEXT
  source: domain.marketplace.walmart.reconciliation
  target: platform_context.walmart.us
  fields:
    edge_family: business_hierarchy_in_scope
    evidence_basis: Explicit platform_context binding from card field.
    confidence: high
    canonical_cognee_edge: true
    marketplace_only: true
    canonical_edge_type: HAS_CONTEXT
    inverse_edge_type: BELONGS_TO_CONTEXT
    materialize_inverse: false
    edge_class: canonical
    source_type: domain
    target_type: platform_context
    evidence_refs:
    - ev.walmart.reconciliation.001
    notes: Explicit platform_context binding from card field.
```

```yaml
candidate_edge:
  edge_id: edge.walmart.0328
  edge_type: HAS_DOMAIN
  source: table.zs_observe.walmart_oms
  target: domain.marketplace.walmart.orders
  fields:
    edge_family: business_hierarchy_in_scope
    evidence_basis: Explicit domain binding from card field.
    confidence: high
    canonical_cognee_edge: true
    marketplace_only: true
    canonical_edge_type: HAS_DOMAIN
    inverse_edge_type: BELONGS_TO_CONTEXT_OR_CARD
    materialize_inverse: false
    edge_class: canonical
    source_type: table
    target_type: domain
    evidence_refs:
    - ev.walmart_oms.schema.001
    - ev.walmart.filters.001
    notes: Explicit domain binding from card field.
```

```yaml
candidate_edge:
  edge_id: edge.walmart.0329
  edge_type: HAS_CONTEXT
  source: table.zs_observe.walmart_oms
  target: platform_context.walmart.us
  fields:
    edge_family: business_hierarchy_in_scope
    evidence_basis: Explicit platform_context binding from card field.
    confidence: high
    canonical_cognee_edge: true
    marketplace_only: true
    canonical_edge_type: HAS_CONTEXT
    inverse_edge_type: BELONGS_TO_CONTEXT
    materialize_inverse: false
    edge_class: canonical
    source_type: table
    target_type: platform_context
    evidence_refs:
    - ev.walmart_oms.schema.001
    - ev.walmart.filters.001
    notes: Explicit platform_context binding from card field.
```

```yaml
candidate_edge:
  edge_id: edge.walmart.0330
  edge_type: HAS_DOMAIN
  source: table.zs_observe.walmart_settlement
  target: domain.marketplace.walmart.settlement
  fields:
    edge_family: business_hierarchy_in_scope
    evidence_basis: Explicit domain binding from card field.
    confidence: high
    canonical_cognee_edge: true
    marketplace_only: true
    canonical_edge_type: HAS_DOMAIN
    inverse_edge_type: BELONGS_TO_CONTEXT_OR_CARD
    materialize_inverse: false
    edge_class: canonical
    source_type: table
    target_type: domain
    evidence_refs:
    - ev.walmart_settlement.schema.001
    - ev.walmart.filters.001
    notes: Explicit domain binding from card field.
```

```yaml
candidate_edge:
  edge_id: edge.walmart.0331
  edge_type: HAS_CONTEXT
  source: table.zs_observe.walmart_settlement
  target: platform_context.walmart.us
  fields:
    edge_family: business_hierarchy_in_scope
    evidence_basis: Explicit platform_context binding from card field.
    confidence: high
    canonical_cognee_edge: true
    marketplace_only: true
    canonical_edge_type: HAS_CONTEXT
    inverse_edge_type: BELONGS_TO_CONTEXT
    materialize_inverse: false
    edge_class: canonical
    source_type: table
    target_type: platform_context
    evidence_refs:
    - ev.walmart_settlement.schema.001
    - ev.walmart.filters.001
    notes: Explicit platform_context binding from card field.
```

```yaml
candidate_edge:
  edge_id: edge.walmart.0332
  edge_type: HAS_DOMAIN
  source: table.zs_observe.walmart_lookup
  target: domain.marketplace.walmart.catalogue
  fields:
    edge_family: business_hierarchy_in_scope
    evidence_basis: Explicit domain binding from card field.
    confidence: high
    canonical_cognee_edge: true
    marketplace_only: true
    canonical_edge_type: HAS_DOMAIN
    inverse_edge_type: BELONGS_TO_CONTEXT_OR_CARD
    materialize_inverse: false
    edge_class: canonical
    source_type: table
    target_type: domain
    evidence_refs:
    - ev.walmart_lookup.schema.001
    - ev.walmart.filters.001
    notes: Explicit domain binding from card field.
```

```yaml
candidate_edge:
  edge_id: edge.walmart.0333
  edge_type: HAS_CONTEXT
  source: table.zs_observe.walmart_lookup
  target: platform_context.walmart.us
  fields:
    edge_family: business_hierarchy_in_scope
    evidence_basis: Explicit platform_context binding from card field.
    confidence: high
    canonical_cognee_edge: true
    marketplace_only: true
    canonical_edge_type: HAS_CONTEXT
    inverse_edge_type: BELONGS_TO_CONTEXT
    materialize_inverse: false
    edge_class: canonical
    source_type: table
    target_type: platform_context
    evidence_refs:
    - ev.walmart_lookup.schema.001
    - ev.walmart.filters.001
    notes: Explicit platform_context binding from card field.
```

```yaml
candidate_edge:
  edge_id: edge.walmart.0334
  edge_type: HAS_DOMAIN
  source: metric.marketplace.gross_revenue
  target: domain.marketplace.walmart.orders
  fields:
    edge_family: business_hierarchy_in_scope
    evidence_basis: Explicit domain binding from card field.
    confidence: high
    canonical_cognee_edge: true
    marketplace_only: true
    canonical_edge_type: HAS_DOMAIN
    inverse_edge_type: BELONGS_TO_CONTEXT_OR_CARD
    materialize_inverse: false
    edge_class: canonical
    source_type: metric
    target_type: domain
    evidence_refs:
    - ev.walmart.metrics.001
    notes: Explicit domain binding from card field.
```

```yaml
candidate_edge:
  edge_id: edge.walmart.0335
  edge_type: HAS_DOMAIN
  source: metric.marketplace.gross_revenue
  target: domain.marketplace.walmart.settlement
  fields:
    edge_family: business_hierarchy_in_scope
    evidence_basis: Explicit domain binding from card field.
    confidence: high
    canonical_cognee_edge: true
    marketplace_only: true
    canonical_edge_type: HAS_DOMAIN
    inverse_edge_type: BELONGS_TO_CONTEXT_OR_CARD
    materialize_inverse: false
    edge_class: canonical
    source_type: metric
    target_type: domain
    evidence_refs:
    - ev.walmart.metrics.001
    notes: Explicit domain binding from card field.
```

```yaml
candidate_edge:
  edge_id: edge.walmart.0336
  edge_type: HAS_DOMAIN
  source: metric.marketplace.product_revenue_excluding_tax
  target: domain.marketplace.walmart.settlement
  fields:
    edge_family: business_hierarchy_in_scope
    evidence_basis: Explicit domain binding from card field.
    confidence: high
    canonical_cognee_edge: true
    marketplace_only: true
    canonical_edge_type: HAS_DOMAIN
    inverse_edge_type: BELONGS_TO_CONTEXT_OR_CARD
    materialize_inverse: false
    edge_class: canonical
    source_type: metric
    target_type: domain
    evidence_refs:
    - ev.walmart.metrics.001
    notes: Explicit domain binding from card field.
```

```yaml
candidate_edge:
  edge_id: edge.walmart.0337
  edge_type: HAS_DOMAIN
  source: metric.marketplace.net_seller_payout
  target: domain.marketplace.walmart.settlement
  fields:
    edge_family: business_hierarchy_in_scope
    evidence_basis: Explicit domain binding from card field.
    confidence: high
    canonical_cognee_edge: true
    marketplace_only: true
    canonical_edge_type: HAS_DOMAIN
    inverse_edge_type: BELONGS_TO_CONTEXT_OR_CARD
    materialize_inverse: false
    edge_class: canonical
    source_type: metric
    target_type: domain
    evidence_refs:
    - ev.walmart.business_model.001
    notes: Explicit domain binding from card field.
```

```yaml
candidate_edge:
  edge_id: edge.walmart.0338
  edge_type: HAS_DOMAIN
  source: metric.marketplace.seller_realization_rate
  target: domain.marketplace.walmart.settlement
  fields:
    edge_family: business_hierarchy_in_scope
    evidence_basis: Explicit domain binding from card field.
    confidence: high
    canonical_cognee_edge: true
    marketplace_only: true
    canonical_edge_type: HAS_DOMAIN
    inverse_edge_type: BELONGS_TO_CONTEXT_OR_CARD
    materialize_inverse: false
    edge_class: canonical
    source_type: metric
    target_type: domain
    evidence_refs:
    - ev.walmart.metrics.001
    notes: Explicit domain binding from card field.
```

```yaml
candidate_edge:
  edge_id: edge.walmart.0339
  edge_type: HAS_DOMAIN
  source: metric.marketplace.effective_commission_rate
  target: domain.marketplace.walmart.fees
  fields:
    edge_family: business_hierarchy_in_scope
    evidence_basis: Explicit domain binding from card field.
    confidence: high
    canonical_cognee_edge: true
    marketplace_only: true
    canonical_edge_type: HAS_DOMAIN
    inverse_edge_type: BELONGS_TO_CONTEXT_OR_CARD
    materialize_inverse: false
    edge_class: canonical
    source_type: metric
    target_type: domain
    evidence_refs:
    - ev.walmart.business_model.001
    notes: Explicit domain binding from card field.
```

```yaml
candidate_edge:
  edge_id: edge.walmart.0340
  edge_type: HAS_DOMAIN
  source: metric.marketplace.return_rate
  target: domain.marketplace.walmart.returns
  fields:
    edge_family: business_hierarchy_in_scope
    evidence_basis: Explicit domain binding from card field.
    confidence: high
    canonical_cognee_edge: true
    marketplace_only: true
    canonical_edge_type: HAS_DOMAIN
    inverse_edge_type: BELONGS_TO_CONTEXT_OR_CARD
    materialize_inverse: false
    edge_class: canonical
    source_type: metric
    target_type: domain
    evidence_refs:
    - ev.walmart.metrics.001
    notes: Explicit domain binding from card field.
```

```yaml
candidate_edge:
  edge_id: edge.walmart.0341
  edge_type: HAS_DOMAIN
  source: metric.marketplace.average_order_value
  target: domain.marketplace.walmart.orders
  fields:
    edge_family: business_hierarchy_in_scope
    evidence_basis: Explicit domain binding from card field.
    confidence: high
    canonical_cognee_edge: true
    marketplace_only: true
    canonical_edge_type: HAS_DOMAIN
    inverse_edge_type: BELONGS_TO_CONTEXT_OR_CARD
    materialize_inverse: false
    edge_class: canonical
    source_type: metric
    target_type: domain
    evidence_refs:
    - ev.walmart.metrics.001
    notes: Explicit domain binding from card field.
```

```yaml
candidate_edge:
  edge_id: edge.walmart.0342
  edge_type: HAS_DOMAIN
  source: metric.marketplace.cancellation_rate
  target: domain.marketplace.walmart.orders
  fields:
    edge_family: business_hierarchy_in_scope
    evidence_basis: Explicit domain binding from card field.
    confidence: high
    canonical_cognee_edge: true
    marketplace_only: true
    canonical_edge_type: HAS_DOMAIN
    inverse_edge_type: BELONGS_TO_CONTEXT_OR_CARD
    materialize_inverse: false
    edge_class: canonical
    source_type: metric
    target_type: domain
    evidence_refs:
    - ev.walmart_oms.schema.001
    notes: Explicit domain binding from card field.
```

```yaml
candidate_edge:
  edge_id: edge.walmart.0343
  edge_type: HAS_DOMAIN
  source: metric.marketplace.tax_withheld
  target: domain.marketplace.walmart.tax
  fields:
    edge_family: business_hierarchy_in_scope
    evidence_basis: Explicit domain binding from card field.
    confidence: high
    canonical_cognee_edge: true
    marketplace_only: true
    canonical_edge_type: HAS_DOMAIN
    inverse_edge_type: BELONGS_TO_CONTEXT_OR_CARD
    materialize_inverse: false
    edge_class: canonical
    source_type: metric
    target_type: domain
    evidence_refs:
    - ev.walmart.business_model.001
    notes: Explicit domain binding from card field.
```

```yaml
candidate_edge:
  edge_id: edge.walmart.0344
  edge_type: HAS_DOMAIN
  source: metric.marketplace.walmart_funded_savings
  target: domain.marketplace.walmart.settlement
  fields:
    edge_family: business_hierarchy_in_scope
    evidence_basis: Explicit domain binding from card field.
    confidence: high
    canonical_cognee_edge: true
    marketplace_only: true
    canonical_edge_type: HAS_DOMAIN
    inverse_edge_type: BELONGS_TO_CONTEXT_OR_CARD
    materialize_inverse: false
    edge_class: canonical
    source_type: metric
    target_type: domain
    evidence_refs:
    - ev.walmart.metrics.001
    notes: Explicit domain binding from card field.
```

```yaml
candidate_edge:
  edge_id: edge.walmart.0345
  edge_type: HAS_DOMAIN
  source: metric.marketplace.sku_revenue
  target: domain.marketplace.walmart.catalogue
  fields:
    edge_family: business_hierarchy_in_scope
    evidence_basis: Explicit domain binding from card field.
    confidence: high
    canonical_cognee_edge: true
    marketplace_only: true
    canonical_edge_type: HAS_DOMAIN
    inverse_edge_type: BELONGS_TO_CONTEXT_OR_CARD
    materialize_inverse: false
    edge_class: canonical
    source_type: metric
    target_type: domain
    evidence_refs:
    - ev.walmart.metrics.001
    notes: Explicit domain binding from card field.
```

```yaml
candidate_edge:
  edge_id: edge.walmart.0346
  edge_type: HAS_DOMAIN
  source: metric.marketplace.sku_revenue
  target: domain.marketplace.walmart.settlement
  fields:
    edge_family: business_hierarchy_in_scope
    evidence_basis: Explicit domain binding from card field.
    confidence: high
    canonical_cognee_edge: true
    marketplace_only: true
    canonical_edge_type: HAS_DOMAIN
    inverse_edge_type: BELONGS_TO_CONTEXT_OR_CARD
    materialize_inverse: false
    edge_class: canonical
    source_type: metric
    target_type: domain
    evidence_refs:
    - ev.walmart.metrics.001
    notes: Explicit domain binding from card field.
```

```yaml
candidate_edge:
  edge_id: edge.walmart.0347
  edge_type: HAS_DOMAIN
  source: metric.marketplace.revenue_by_state
  target: domain.marketplace.walmart.orders
  fields:
    edge_family: business_hierarchy_in_scope
    evidence_basis: Explicit domain binding from card field.
    confidence: high
    canonical_cognee_edge: true
    marketplace_only: true
    canonical_edge_type: HAS_DOMAIN
    inverse_edge_type: BELONGS_TO_CONTEXT_OR_CARD
    materialize_inverse: false
    edge_class: canonical
    source_type: metric
    target_type: domain
    evidence_refs:
    - ev.walmart.metrics.001
    notes: Explicit domain binding from card field.
```

```yaml
candidate_edge:
  edge_id: edge.walmart.0348
  edge_type: HAS_CONTEXT
  source: metric_implementation.walmart.walmart_settlement.gross_revenue
  target: platform_context.walmart.us
  fields:
    edge_family: business_hierarchy_in_scope
    evidence_basis: Explicit platform_context binding from card field.
    confidence: high
    canonical_cognee_edge: true
    marketplace_only: true
    canonical_edge_type: HAS_CONTEXT
    inverse_edge_type: BELONGS_TO_CONTEXT
    materialize_inverse: false
    edge_class: canonical
    source_type: metric_implementation
    target_type: platform_context
    evidence_refs:
    - ev.walmart.metrics.001
    notes: Explicit platform_context binding from card field.
```

```yaml
candidate_edge:
  edge_id: edge.walmart.0349
  edge_type: HAS_CONTEXT
  source: metric_implementation.walmart.walmart_settlement.product_revenue_excluding_tax
  target: platform_context.walmart.us
  fields:
    edge_family: business_hierarchy_in_scope
    evidence_basis: Explicit platform_context binding from card field.
    confidence: high
    canonical_cognee_edge: true
    marketplace_only: true
    canonical_edge_type: HAS_CONTEXT
    inverse_edge_type: BELONGS_TO_CONTEXT
    materialize_inverse: false
    edge_class: canonical
    source_type: metric_implementation
    target_type: platform_context
    evidence_refs:
    - ev.walmart.metrics.001
    notes: Explicit platform_context binding from card field.
```

```yaml
candidate_edge:
  edge_id: edge.walmart.0350
  edge_type: HAS_CONTEXT
  source: metric_implementation.walmart.walmart_settlement.net_seller_payout
  target: platform_context.walmart.us
  fields:
    edge_family: business_hierarchy_in_scope
    evidence_basis: Explicit platform_context binding from card field.
    confidence: high
    canonical_cognee_edge: true
    marketplace_only: true
    canonical_edge_type: HAS_CONTEXT
    inverse_edge_type: BELONGS_TO_CONTEXT
    materialize_inverse: false
    edge_class: canonical
    source_type: metric_implementation
    target_type: platform_context
    evidence_refs:
    - ev.walmart.business_model.001
    notes: Explicit platform_context binding from card field.
```

```yaml
candidate_edge:
  edge_id: edge.walmart.0351
  edge_type: HAS_CONTEXT
  source: metric_implementation.walmart.walmart_settlement.seller_realization_rate
  target: platform_context.walmart.us
  fields:
    edge_family: business_hierarchy_in_scope
    evidence_basis: Explicit platform_context binding from card field.
    confidence: high
    canonical_cognee_edge: true
    marketplace_only: true
    canonical_edge_type: HAS_CONTEXT
    inverse_edge_type: BELONGS_TO_CONTEXT
    materialize_inverse: false
    edge_class: canonical
    source_type: metric_implementation
    target_type: platform_context
    evidence_refs:
    - ev.walmart.metrics.001
    notes: Explicit platform_context binding from card field.
```

```yaml
candidate_edge:
  edge_id: edge.walmart.0352
  edge_type: HAS_CONTEXT
  source: metric_implementation.walmart.walmart_settlement.effective_commission_rate
  target: platform_context.walmart.us
  fields:
    edge_family: business_hierarchy_in_scope
    evidence_basis: Explicit platform_context binding from card field.
    confidence: high
    canonical_cognee_edge: true
    marketplace_only: true
    canonical_edge_type: HAS_CONTEXT
    inverse_edge_type: BELONGS_TO_CONTEXT
    materialize_inverse: false
    edge_class: canonical
    source_type: metric_implementation
    target_type: platform_context
    evidence_refs:
    - ev.walmart.reconciliation.001
    notes: Explicit platform_context binding from card field.
```

```yaml
candidate_edge:
  edge_id: edge.walmart.0353
  edge_type: HAS_CONTEXT
  source: metric_implementation.walmart.walmart_settlement.return_rate
  target: platform_context.walmart.us
  fields:
    edge_family: business_hierarchy_in_scope
    evidence_basis: Explicit platform_context binding from card field.
    confidence: high
    canonical_cognee_edge: true
    marketplace_only: true
    canonical_edge_type: HAS_CONTEXT
    inverse_edge_type: BELONGS_TO_CONTEXT
    materialize_inverse: false
    edge_class: canonical
    source_type: metric_implementation
    target_type: platform_context
    evidence_refs:
    - ev.walmart.metrics.001
    notes: Explicit platform_context binding from card field.
```

```yaml
candidate_edge:
  edge_id: edge.walmart.0354
  edge_type: HAS_CONTEXT
  source: metric_implementation.walmart.walmart_oms.average_order_value
  target: platform_context.walmart.us
  fields:
    edge_family: business_hierarchy_in_scope
    evidence_basis: Explicit platform_context binding from card field.
    confidence: high
    canonical_cognee_edge: true
    marketplace_only: true
    canonical_edge_type: HAS_CONTEXT
    inverse_edge_type: BELONGS_TO_CONTEXT
    materialize_inverse: false
    edge_class: canonical
    source_type: metric_implementation
    target_type: platform_context
    evidence_refs:
    - ev.walmart.metrics.001
    notes: Explicit platform_context binding from card field.
```

```yaml
candidate_edge:
  edge_id: edge.walmart.0355
  edge_type: HAS_CONTEXT
  source: metric_implementation.walmart.walmart_oms.cancellation_rate
  target: platform_context.walmart.us
  fields:
    edge_family: business_hierarchy_in_scope
    evidence_basis: Explicit platform_context binding from card field.
    confidence: high
    canonical_cognee_edge: true
    marketplace_only: true
    canonical_edge_type: HAS_CONTEXT
    inverse_edge_type: BELONGS_TO_CONTEXT
    materialize_inverse: false
    edge_class: canonical
    source_type: metric_implementation
    target_type: platform_context
    evidence_refs:
    - ev.walmart_oms.schema.001
    notes: Explicit platform_context binding from card field.
```

```yaml
candidate_edge:
  edge_id: edge.walmart.0356
  edge_type: HAS_CONTEXT
  source: metric_implementation.walmart.walmart_settlement.tax_withheld
  target: platform_context.walmart.us
  fields:
    edge_family: business_hierarchy_in_scope
    evidence_basis: Explicit platform_context binding from card field.
    confidence: high
    canonical_cognee_edge: true
    marketplace_only: true
    canonical_edge_type: HAS_CONTEXT
    inverse_edge_type: BELONGS_TO_CONTEXT
    materialize_inverse: false
    edge_class: canonical
    source_type: metric_implementation
    target_type: platform_context
    evidence_refs:
    - ev.walmart.business_model.001
    notes: Explicit platform_context binding from card field.
```

```yaml
candidate_edge:
  edge_id: edge.walmart.0357
  edge_type: HAS_CONTEXT
  source: metric_implementation.walmart.walmart_settlement.walmart_funded_savings
  target: platform_context.walmart.us
  fields:
    edge_family: business_hierarchy_in_scope
    evidence_basis: Explicit platform_context binding from card field.
    confidence: high
    canonical_cognee_edge: true
    marketplace_only: true
    canonical_edge_type: HAS_CONTEXT
    inverse_edge_type: BELONGS_TO_CONTEXT
    materialize_inverse: false
    edge_class: canonical
    source_type: metric_implementation
    target_type: platform_context
    evidence_refs:
    - ev.walmart.metrics.001
    notes: Explicit platform_context binding from card field.
```

```yaml
candidate_edge:
  edge_id: edge.walmart.0358
  edge_type: HAS_CONTEXT
  source: metric_implementation.walmart.walmart_settlement.sku_revenue
  target: platform_context.walmart.us
  fields:
    edge_family: business_hierarchy_in_scope
    evidence_basis: Explicit platform_context binding from card field.
    confidence: high
    canonical_cognee_edge: true
    marketplace_only: true
    canonical_edge_type: HAS_CONTEXT
    inverse_edge_type: BELONGS_TO_CONTEXT
    materialize_inverse: false
    edge_class: canonical
    source_type: metric_implementation
    target_type: platform_context
    evidence_refs:
    - ev.walmart.metrics.001
    notes: Explicit platform_context binding from card field.
```

```yaml
candidate_edge:
  edge_id: edge.walmart.0359
  edge_type: HAS_CONTEXT
  source: metric_implementation.walmart.walmart_oms.revenue_by_state
  target: platform_context.walmart.us
  fields:
    edge_family: business_hierarchy_in_scope
    evidence_basis: Explicit platform_context binding from card field.
    confidence: high
    canonical_cognee_edge: true
    marketplace_only: true
    canonical_edge_type: HAS_CONTEXT
    inverse_edge_type: BELONGS_TO_CONTEXT
    materialize_inverse: false
    edge_class: canonical
    source_type: metric_implementation
    target_type: platform_context
    evidence_refs:
    - ev.walmart.metrics.001
    notes: Explicit platform_context binding from card field.
```

```yaml
candidate_edge:
  edge_id: edge.walmart.0360
  edge_type: HAS_CONTEXT
  source: business_process.walmart.forward_wfs_sale_to_payout
  target: platform_context.walmart.us
  fields:
    edge_family: business_hierarchy_in_scope
    evidence_basis: Explicit platform_context binding from card field.
    confidence: high
    canonical_cognee_edge: true
    marketplace_only: true
    canonical_edge_type: HAS_CONTEXT
    inverse_edge_type: BELONGS_TO_CONTEXT
    materialize_inverse: false
    edge_class: canonical
    source_type: business_process
    target_type: platform_context
    evidence_refs:
    - ev.walmart.lifecycle.001
    notes: Explicit platform_context binding from card field.
```

```yaml
candidate_edge:
  edge_id: edge.walmart.0361
  edge_type: HAS_CONTEXT
  source: business_process.walmart.refund_to_payout_deduction
  target: platform_context.walmart.us
  fields:
    edge_family: business_hierarchy_in_scope
    evidence_basis: Explicit platform_context binding from card field.
    confidence: high
    canonical_cognee_edge: true
    marketplace_only: true
    canonical_edge_type: HAS_CONTEXT
    inverse_edge_type: BELONGS_TO_CONTEXT
    materialize_inverse: false
    edge_class: canonical
    source_type: business_process
    target_type: platform_context
    evidence_refs:
    - ev.walmart.lifecycle.001
    notes: Explicit platform_context binding from card field.
```

```yaml
candidate_edge:
  edge_id: edge.walmart.0362
  edge_type: HAS_CONTEXT
  source: business_process.walmart.cancellation_without_settlement
  target: platform_context.walmart.us
  fields:
    edge_family: business_hierarchy_in_scope
    evidence_basis: Explicit platform_context binding from card field.
    confidence: high
    canonical_cognee_edge: true
    marketplace_only: true
    canonical_edge_type: HAS_CONTEXT
    inverse_edge_type: BELONGS_TO_CONTEXT
    materialize_inverse: false
    edge_class: canonical
    source_type: business_process
    target_type: platform_context
    evidence_refs:
    - ev.walmart.lifecycle.001
    notes: Explicit platform_context binding from card field.
```

```yaml
candidate_edge:
  edge_id: edge.walmart.0363
  edge_type: HAS_CONTEXT
  source: business_process.walmart.catalogue_enrichment
  target: platform_context.walmart.us
  fields:
    edge_family: business_hierarchy_in_scope
    evidence_basis: Explicit platform_context binding from card field.
    confidence: high
    canonical_cognee_edge: true
    marketplace_only: true
    canonical_edge_type: HAS_CONTEXT
    inverse_edge_type: BELONGS_TO_CONTEXT
    materialize_inverse: false
    edge_class: canonical
    source_type: business_process
    target_type: platform_context
    evidence_refs:
    - ev.walmart_lookup.schema.001
    notes: Explicit platform_context binding from card field.
```

```yaml
candidate_edge:
  edge_id: edge.walmart.0364
  edge_type: IMPLEMENTS
  source: metric_implementation.walmart.walmart_settlement.gross_revenue
  target: metric.marketplace.gross_revenue
  fields:
    edge_family: metric_semantics
    evidence_basis: Inverse implementation-to-metric edge for direct traversal.
    confidence: high
    canonical_cognee_edge: true
    marketplace_only: true
    canonical_edge_type: IMPLEMENTS
    inverse_edge_type: IMPLEMENTED_BY
    materialize_inverse: false
    edge_class: canonical
    source_type: metric_implementation
    target_type: metric
    evidence_refs:
    - ev.walmart.metrics.001
    notes: Inverse implementation-to-metric edge for direct traversal.
```

```yaml
candidate_edge:
  edge_id: edge.walmart.0365
  edge_type: USES_COLUMN
  source: metric_implementation.walmart.walmart_settlement.gross_revenue
  target: column.zs_observe.walmart_settlement.charged_amount
  fields:
    edge_family: dependency_usage
    evidence_basis: Metric implementation formula/filter/SQL uses this documented column.
    confidence: high
    canonical_cognee_edge: true
    marketplace_only: true
    canonical_edge_type: USES_COLUMN
    inverse_edge_type: USED_BY_CARD
    materialize_inverse: false
    edge_class: canonical
    source_type: metric_implementation
    target_type: column
    evidence_refs:
    - ev.walmart.metrics.001
    notes: Metric implementation formula/filter/SQL uses this documented column.
```

```yaml
candidate_edge:
  edge_id: edge.walmart.0366
  edge_type: USES_COLUMN
  source: metric_implementation.walmart.walmart_settlement.gross_revenue
  target: column.zs_observe.walmart_settlement.charged_amount_excluding_tax
  fields:
    edge_family: dependency_usage
    evidence_basis: Metric implementation formula/filter/SQL uses this documented column.
    confidence: high
    canonical_cognee_edge: true
    marketplace_only: true
    canonical_edge_type: USES_COLUMN
    inverse_edge_type: USED_BY_CARD
    materialize_inverse: false
    edge_class: canonical
    source_type: metric_implementation
    target_type: column
    evidence_refs:
    - ev.walmart.metrics.001
    notes: Metric implementation formula/filter/SQL uses this documented column.
```

```yaml
candidate_edge:
  edge_id: edge.walmart.0367
  edge_type: USES_COLUMN
  source: metric_implementation.walmart.walmart_settlement.gross_revenue
  target: column.zs_observe.walmart_settlement.total_tax
  fields:
    edge_family: dependency_usage
    evidence_basis: Metric implementation formula/filter/SQL uses this documented column.
    confidence: high
    canonical_cognee_edge: true
    marketplace_only: true
    canonical_edge_type: USES_COLUMN
    inverse_edge_type: USED_BY_CARD
    materialize_inverse: false
    edge_class: canonical
    source_type: metric_implementation
    target_type: column
    evidence_refs:
    - ev.walmart.metrics.001
    notes: Metric implementation formula/filter/SQL uses this documented column.
```

```yaml
candidate_edge:
  edge_id: edge.walmart.0368
  edge_type: USES_COLUMN
  source: metric_implementation.walmart.walmart_settlement.gross_revenue
  target: column.zs_observe.walmart_settlement.gross_commission
  fields:
    edge_family: dependency_usage
    evidence_basis: Metric implementation formula/filter/SQL uses this documented column.
    confidence: high
    canonical_cognee_edge: true
    marketplace_only: true
    canonical_edge_type: USES_COLUMN
    inverse_edge_type: USED_BY_CARD
    materialize_inverse: false
    edge_class: canonical
    source_type: metric_implementation
    target_type: column
    evidence_refs:
    - ev.walmart.metrics.001
    notes: Metric implementation formula/filter/SQL uses this documented column.
```

```yaml
candidate_edge:
  edge_id: edge.walmart.0369
  edge_type: USES_COLUMN
  source: metric_implementation.walmart.walmart_settlement.gross_revenue
  target: column.zs_observe.walmart_settlement.total_walmart_funded_savings
  fields:
    edge_family: dependency_usage
    evidence_basis: Metric implementation formula/filter/SQL uses this documented column.
    confidence: high
    canonical_cognee_edge: true
    marketplace_only: true
    canonical_edge_type: USES_COLUMN
    inverse_edge_type: USED_BY_CARD
    materialize_inverse: false
    edge_class: canonical
    source_type: metric_implementation
    target_type: column
    evidence_refs:
    - ev.walmart.metrics.001
    notes: Metric implementation formula/filter/SQL uses this documented column.
```

```yaml
candidate_edge:
  edge_id: edge.walmart.0370
  edge_type: USES_COLUMN
  source: metric_implementation.walmart.walmart_settlement.gross_revenue
  target: column.zs_observe.walmart_settlement.transaction_type
  fields:
    edge_family: dependency_usage
    evidence_basis: Metric implementation formula/filter/SQL uses this documented column.
    confidence: high
    canonical_cognee_edge: true
    marketplace_only: true
    canonical_edge_type: USES_COLUMN
    inverse_edge_type: USED_BY_CARD
    materialize_inverse: false
    edge_class: canonical
    source_type: metric_implementation
    target_type: column
    evidence_refs:
    - ev.walmart.metrics.001
    notes: Metric implementation formula/filter/SQL uses this documented column.
```

```yaml
candidate_edge:
  edge_id: edge.walmart.0371
  edge_type: USES_COLUMN
  source: metric_implementation.walmart.walmart_settlement.gross_revenue
  target: column.zs_observe.walmart_settlement.group_level_id
  fields:
    edge_family: dependency_usage
    evidence_basis: Metric implementation formula/filter/SQL uses this documented column.
    confidence: high
    canonical_cognee_edge: true
    marketplace_only: true
    canonical_edge_type: USES_COLUMN
    inverse_edge_type: USED_BY_CARD
    materialize_inverse: false
    edge_class: canonical
    source_type: metric_implementation
    target_type: column
    evidence_refs:
    - ev.walmart.metrics.001
    notes: Metric implementation formula/filter/SQL uses this documented column.
```

```yaml
candidate_edge:
  edge_id: edge.walmart.0372
  edge_type: USES_COLUMN
  source: metric_implementation.walmart.walmart_settlement.gross_revenue
  target: column.zs_observe.walmart_settlement.is_active
  fields:
    edge_family: dependency_usage
    evidence_basis: Metric implementation formula/filter/SQL uses this documented column.
    confidence: high
    canonical_cognee_edge: true
    marketplace_only: true
    canonical_edge_type: USES_COLUMN
    inverse_edge_type: USED_BY_CARD
    materialize_inverse: false
    edge_class: canonical
    source_type: metric_implementation
    target_type: column
    evidence_refs:
    - ev.walmart.metrics.001
    notes: Metric implementation formula/filter/SQL uses this documented column.
```

```yaml
candidate_edge:
  edge_id: edge.walmart.0373
  edge_type: IMPLEMENTS
  source: metric_implementation.walmart.walmart_settlement.product_revenue_excluding_tax
  target: metric.marketplace.product_revenue_excluding_tax
  fields:
    edge_family: metric_semantics
    evidence_basis: Inverse implementation-to-metric edge for direct traversal.
    confidence: high
    canonical_cognee_edge: true
    marketplace_only: true
    canonical_edge_type: IMPLEMENTS
    inverse_edge_type: IMPLEMENTED_BY
    materialize_inverse: false
    edge_class: canonical
    source_type: metric_implementation
    target_type: metric
    evidence_refs:
    - ev.walmart.metrics.001
    notes: Inverse implementation-to-metric edge for direct traversal.
```

```yaml
candidate_edge:
  edge_id: edge.walmart.0374
  edge_type: USES_COLUMN
  source: metric_implementation.walmart.walmart_settlement.product_revenue_excluding_tax
  target: column.zs_observe.walmart_settlement.charged_amount
  fields:
    edge_family: dependency_usage
    evidence_basis: Metric implementation formula/filter/SQL uses this documented column.
    confidence: high
    canonical_cognee_edge: true
    marketplace_only: true
    canonical_edge_type: USES_COLUMN
    inverse_edge_type: USED_BY_CARD
    materialize_inverse: false
    edge_class: canonical
    source_type: metric_implementation
    target_type: column
    evidence_refs:
    - ev.walmart.metrics.001
    notes: Metric implementation formula/filter/SQL uses this documented column.
```

```yaml
candidate_edge:
  edge_id: edge.walmart.0375
  edge_type: USES_COLUMN
  source: metric_implementation.walmart.walmart_settlement.product_revenue_excluding_tax
  target: column.zs_observe.walmart_settlement.charged_amount_excluding_tax
  fields:
    edge_family: dependency_usage
    evidence_basis: Metric implementation formula/filter/SQL uses this documented column.
    confidence: high
    canonical_cognee_edge: true
    marketplace_only: true
    canonical_edge_type: USES_COLUMN
    inverse_edge_type: USED_BY_CARD
    materialize_inverse: false
    edge_class: canonical
    source_type: metric_implementation
    target_type: column
    evidence_refs:
    - ev.walmart.metrics.001
    notes: Metric implementation formula/filter/SQL uses this documented column.
```

```yaml
candidate_edge:
  edge_id: edge.walmart.0376
  edge_type: USES_COLUMN
  source: metric_implementation.walmart.walmart_settlement.product_revenue_excluding_tax
  target: column.zs_observe.walmart_settlement.total_tax
  fields:
    edge_family: dependency_usage
    evidence_basis: Metric implementation formula/filter/SQL uses this documented column.
    confidence: high
    canonical_cognee_edge: true
    marketplace_only: true
    canonical_edge_type: USES_COLUMN
    inverse_edge_type: USED_BY_CARD
    materialize_inverse: false
    edge_class: canonical
    source_type: metric_implementation
    target_type: column
    evidence_refs:
    - ev.walmart.metrics.001
    notes: Metric implementation formula/filter/SQL uses this documented column.
```

```yaml
candidate_edge:
  edge_id: edge.walmart.0377
  edge_type: USES_COLUMN
  source: metric_implementation.walmart.walmart_settlement.product_revenue_excluding_tax
  target: column.zs_observe.walmart_settlement.gross_commission
  fields:
    edge_family: dependency_usage
    evidence_basis: Metric implementation formula/filter/SQL uses this documented column.
    confidence: high
    canonical_cognee_edge: true
    marketplace_only: true
    canonical_edge_type: USES_COLUMN
    inverse_edge_type: USED_BY_CARD
    materialize_inverse: false
    edge_class: canonical
    source_type: metric_implementation
    target_type: column
    evidence_refs:
    - ev.walmart.metrics.001
    notes: Metric implementation formula/filter/SQL uses this documented column.
```

```yaml
candidate_edge:
  edge_id: edge.walmart.0378
  edge_type: USES_COLUMN
  source: metric_implementation.walmart.walmart_settlement.product_revenue_excluding_tax
  target: column.zs_observe.walmart_settlement.total_walmart_funded_savings
  fields:
    edge_family: dependency_usage
    evidence_basis: Metric implementation formula/filter/SQL uses this documented column.
    confidence: high
    canonical_cognee_edge: true
    marketplace_only: true
    canonical_edge_type: USES_COLUMN
    inverse_edge_type: USED_BY_CARD
    materialize_inverse: false
    edge_class: canonical
    source_type: metric_implementation
    target_type: column
    evidence_refs:
    - ev.walmart.metrics.001
    notes: Metric implementation formula/filter/SQL uses this documented column.
```

```yaml
candidate_edge:
  edge_id: edge.walmart.0379
  edge_type: USES_COLUMN
  source: metric_implementation.walmart.walmart_settlement.product_revenue_excluding_tax
  target: column.zs_observe.walmart_settlement.transaction_type
  fields:
    edge_family: dependency_usage
    evidence_basis: Metric implementation formula/filter/SQL uses this documented column.
    confidence: high
    canonical_cognee_edge: true
    marketplace_only: true
    canonical_edge_type: USES_COLUMN
    inverse_edge_type: USED_BY_CARD
    materialize_inverse: false
    edge_class: canonical
    source_type: metric_implementation
    target_type: column
    evidence_refs:
    - ev.walmart.metrics.001
    notes: Metric implementation formula/filter/SQL uses this documented column.
```

```yaml
candidate_edge:
  edge_id: edge.walmart.0380
  edge_type: USES_COLUMN
  source: metric_implementation.walmart.walmart_settlement.product_revenue_excluding_tax
  target: column.zs_observe.walmart_settlement.group_level_id
  fields:
    edge_family: dependency_usage
    evidence_basis: Metric implementation formula/filter/SQL uses this documented column.
    confidence: high
    canonical_cognee_edge: true
    marketplace_only: true
    canonical_edge_type: USES_COLUMN
    inverse_edge_type: USED_BY_CARD
    materialize_inverse: false
    edge_class: canonical
    source_type: metric_implementation
    target_type: column
    evidence_refs:
    - ev.walmart.metrics.001
    notes: Metric implementation formula/filter/SQL uses this documented column.
```

```yaml
candidate_edge:
  edge_id: edge.walmart.0381
  edge_type: USES_COLUMN
  source: metric_implementation.walmart.walmart_settlement.product_revenue_excluding_tax
  target: column.zs_observe.walmart_settlement.is_active
  fields:
    edge_family: dependency_usage
    evidence_basis: Metric implementation formula/filter/SQL uses this documented column.
    confidence: high
    canonical_cognee_edge: true
    marketplace_only: true
    canonical_edge_type: USES_COLUMN
    inverse_edge_type: USED_BY_CARD
    materialize_inverse: false
    edge_class: canonical
    source_type: metric_implementation
    target_type: column
    evidence_refs:
    - ev.walmart.metrics.001
    notes: Metric implementation formula/filter/SQL uses this documented column.
```

```yaml
candidate_edge:
  edge_id: edge.walmart.0382
  edge_type: IMPLEMENTS
  source: metric_implementation.walmart.walmart_settlement.net_seller_payout
  target: metric.marketplace.net_seller_payout
  fields:
    edge_family: metric_semantics
    evidence_basis: Inverse implementation-to-metric edge for direct traversal.
    confidence: high
    canonical_cognee_edge: true
    marketplace_only: true
    canonical_edge_type: IMPLEMENTS
    inverse_edge_type: IMPLEMENTED_BY
    materialize_inverse: false
    edge_class: canonical
    source_type: metric_implementation
    target_type: metric
    evidence_refs:
    - ev.walmart.business_model.001
    notes: Inverse implementation-to-metric edge for direct traversal.
```

```yaml
candidate_edge:
  edge_id: edge.walmart.0383
  edge_type: USES_COLUMN
  source: metric_implementation.walmart.walmart_settlement.net_seller_payout
  target: column.zs_observe.walmart_settlement.order_id
  fields:
    edge_family: dependency_usage
    evidence_basis: Metric implementation formula/filter/SQL uses this documented column.
    confidence: high
    canonical_cognee_edge: true
    marketplace_only: true
    canonical_edge_type: USES_COLUMN
    inverse_edge_type: USED_BY_CARD
    materialize_inverse: false
    edge_class: canonical
    source_type: metric_implementation
    target_type: column
    evidence_refs:
    - ev.walmart.business_model.001
    notes: Metric implementation formula/filter/SQL uses this documented column.
```

```yaml
candidate_edge:
  edge_id: edge.walmart.0384
  edge_type: USES_COLUMN
  source: metric_implementation.walmart.walmart_settlement.net_seller_payout
  target: column.zs_observe.walmart_settlement.metadata_2
  fields:
    edge_family: dependency_usage
    evidence_basis: Metric implementation formula/filter/SQL uses this documented column.
    confidence: high
    canonical_cognee_edge: true
    marketplace_only: true
    canonical_edge_type: USES_COLUMN
    inverse_edge_type: USED_BY_CARD
    materialize_inverse: false
    edge_class: canonical
    source_type: metric_implementation
    target_type: column
    evidence_refs:
    - ev.walmart.business_model.001
    notes: Metric implementation formula/filter/SQL uses this documented column.
```

```yaml
candidate_edge:
  edge_id: edge.walmart.0385
  edge_type: USES_COLUMN
  source: metric_implementation.walmart.walmart_settlement.net_seller_payout
  target: column.zs_observe.walmart_settlement.metadata_3
  fields:
    edge_family: dependency_usage
    evidence_basis: Metric implementation formula/filter/SQL uses this documented column.
    confidence: high
    canonical_cognee_edge: true
    marketplace_only: true
    canonical_edge_type: USES_COLUMN
    inverse_edge_type: USED_BY_CARD
    materialize_inverse: false
    edge_class: canonical
    source_type: metric_implementation
    target_type: column
    evidence_refs:
    - ev.walmart.business_model.001
    notes: Metric implementation formula/filter/SQL uses this documented column.
```

```yaml
candidate_edge:
  edge_id: edge.walmart.0386
  edge_type: USES_COLUMN
  source: metric_implementation.walmart.walmart_settlement.net_seller_payout
  target: column.zs_observe.walmart_settlement.charged_amount_excluding_tax
  fields:
    edge_family: dependency_usage
    evidence_basis: Metric implementation formula/filter/SQL uses this documented column.
    confidence: high
    canonical_cognee_edge: true
    marketplace_only: true
    canonical_edge_type: USES_COLUMN
    inverse_edge_type: USED_BY_CARD
    materialize_inverse: false
    edge_class: canonical
    source_type: metric_implementation
    target_type: column
    evidence_refs:
    - ev.walmart.business_model.001
    notes: Metric implementation formula/filter/SQL uses this documented column.
```

```yaml
candidate_edge:
  edge_id: edge.walmart.0387
  edge_type: USES_COLUMN
  source: metric_implementation.walmart.walmart_settlement.net_seller_payout
  target: column.zs_observe.walmart_settlement.gross_commission
  fields:
    edge_family: dependency_usage
    evidence_basis: Metric implementation formula/filter/SQL uses this documented column.
    confidence: high
    canonical_cognee_edge: true
    marketplace_only: true
    canonical_edge_type: USES_COLUMN
    inverse_edge_type: USED_BY_CARD
    materialize_inverse: false
    edge_class: canonical
    source_type: metric_implementation
    target_type: column
    evidence_refs:
    - ev.walmart.business_model.001
    notes: Metric implementation formula/filter/SQL uses this documented column.
```

```yaml
candidate_edge:
  edge_id: edge.walmart.0388
  edge_type: USES_COLUMN
  source: metric_implementation.walmart.walmart_settlement.net_seller_payout
  target: column.zs_observe.walmart_settlement.settled_amount
  fields:
    edge_family: dependency_usage
    evidence_basis: Metric implementation formula/filter/SQL uses this documented column.
    confidence: high
    canonical_cognee_edge: true
    marketplace_only: true
    canonical_edge_type: USES_COLUMN
    inverse_edge_type: USED_BY_CARD
    materialize_inverse: false
    edge_class: canonical
    source_type: metric_implementation
    target_type: column
    evidence_refs:
    - ev.walmart.business_model.001
    notes: Metric implementation formula/filter/SQL uses this documented column.
```

```yaml
candidate_edge:
  edge_id: edge.walmart.0389
  edge_type: USES_COLUMN
  source: metric_implementation.walmart.walmart_settlement.net_seller_payout
  target: column.zs_observe.walmart_settlement.total_walmart_funded_savings
  fields:
    edge_family: dependency_usage
    evidence_basis: Metric implementation formula/filter/SQL uses this documented column.
    confidence: high
    canonical_cognee_edge: true
    marketplace_only: true
    canonical_edge_type: USES_COLUMN
    inverse_edge_type: USED_BY_CARD
    materialize_inverse: false
    edge_class: canonical
    source_type: metric_implementation
    target_type: column
    evidence_refs:
    - ev.walmart.business_model.001
    notes: Metric implementation formula/filter/SQL uses this documented column.
```

```yaml
candidate_edge:
  edge_id: edge.walmart.0390
  edge_type: USES_COLUMN
  source: metric_implementation.walmart.walmart_settlement.net_seller_payout
  target: column.zs_observe.walmart_settlement.transaction_type
  fields:
    edge_family: dependency_usage
    evidence_basis: Metric implementation formula/filter/SQL uses this documented column.
    confidence: high
    canonical_cognee_edge: true
    marketplace_only: true
    canonical_edge_type: USES_COLUMN
    inverse_edge_type: USED_BY_CARD
    materialize_inverse: false
    edge_class: canonical
    source_type: metric_implementation
    target_type: column
    evidence_refs:
    - ev.walmart.business_model.001
    notes: Metric implementation formula/filter/SQL uses this documented column.
```

```yaml
candidate_edge:
  edge_id: edge.walmart.0391
  edge_type: USES_COLUMN
  source: metric_implementation.walmart.walmart_settlement.net_seller_payout
  target: column.zs_observe.walmart_settlement.group_level_id
  fields:
    edge_family: dependency_usage
    evidence_basis: Metric implementation formula/filter/SQL uses this documented column.
    confidence: high
    canonical_cognee_edge: true
    marketplace_only: true
    canonical_edge_type: USES_COLUMN
    inverse_edge_type: USED_BY_CARD
    materialize_inverse: false
    edge_class: canonical
    source_type: metric_implementation
    target_type: column
    evidence_refs:
    - ev.walmart.business_model.001
    notes: Metric implementation formula/filter/SQL uses this documented column.
```

```yaml
candidate_edge:
  edge_id: edge.walmart.0392
  edge_type: USES_COLUMN
  source: metric_implementation.walmart.walmart_settlement.net_seller_payout
  target: column.zs_observe.walmart_settlement.is_active
  fields:
    edge_family: dependency_usage
    evidence_basis: Metric implementation formula/filter/SQL uses this documented column.
    confidence: high
    canonical_cognee_edge: true
    marketplace_only: true
    canonical_edge_type: USES_COLUMN
    inverse_edge_type: USED_BY_CARD
    materialize_inverse: false
    edge_class: canonical
    source_type: metric_implementation
    target_type: column
    evidence_refs:
    - ev.walmart.business_model.001
    notes: Metric implementation formula/filter/SQL uses this documented column.
```

```yaml
candidate_edge:
  edge_id: edge.walmart.0393
  edge_type: IMPLEMENTS
  source: metric_implementation.walmart.walmart_settlement.seller_realization_rate
  target: metric.marketplace.seller_realization_rate
  fields:
    edge_family: metric_semantics
    evidence_basis: Inverse implementation-to-metric edge for direct traversal.
    confidence: high
    canonical_cognee_edge: true
    marketplace_only: true
    canonical_edge_type: IMPLEMENTS
    inverse_edge_type: IMPLEMENTED_BY
    materialize_inverse: false
    edge_class: canonical
    source_type: metric_implementation
    target_type: metric
    evidence_refs:
    - ev.walmart.metrics.001
    notes: Inverse implementation-to-metric edge for direct traversal.
```

```yaml
candidate_edge:
  edge_id: edge.walmart.0394
  edge_type: USES_COLUMN
  source: metric_implementation.walmart.walmart_settlement.seller_realization_rate
  target: column.zs_observe.walmart_settlement.charged_amount
  fields:
    edge_family: dependency_usage
    evidence_basis: Metric implementation formula/filter/SQL uses this documented column.
    confidence: high
    canonical_cognee_edge: true
    marketplace_only: true
    canonical_edge_type: USES_COLUMN
    inverse_edge_type: USED_BY_CARD
    materialize_inverse: false
    edge_class: canonical
    source_type: metric_implementation
    target_type: column
    evidence_refs:
    - ev.walmart.metrics.001
    notes: Metric implementation formula/filter/SQL uses this documented column.
```

```yaml
candidate_edge:
  edge_id: edge.walmart.0395
  edge_type: USES_COLUMN
  source: metric_implementation.walmart.walmart_settlement.seller_realization_rate
  target: column.zs_observe.walmart_settlement.charged_amount_excluding_tax
  fields:
    edge_family: dependency_usage
    evidence_basis: Metric implementation formula/filter/SQL uses this documented column.
    confidence: high
    canonical_cognee_edge: true
    marketplace_only: true
    canonical_edge_type: USES_COLUMN
    inverse_edge_type: USED_BY_CARD
    materialize_inverse: false
    edge_class: canonical
    source_type: metric_implementation
    target_type: column
    evidence_refs:
    - ev.walmart.metrics.001
    notes: Metric implementation formula/filter/SQL uses this documented column.
```

```yaml
candidate_edge:
  edge_id: edge.walmart.0396
  edge_type: USES_COLUMN
  source: metric_implementation.walmart.walmart_settlement.seller_realization_rate
  target: column.zs_observe.walmart_settlement.total_tax
  fields:
    edge_family: dependency_usage
    evidence_basis: Metric implementation formula/filter/SQL uses this documented column.
    confidence: high
    canonical_cognee_edge: true
    marketplace_only: true
    canonical_edge_type: USES_COLUMN
    inverse_edge_type: USED_BY_CARD
    materialize_inverse: false
    edge_class: canonical
    source_type: metric_implementation
    target_type: column
    evidence_refs:
    - ev.walmart.metrics.001
    notes: Metric implementation formula/filter/SQL uses this documented column.
```

```yaml
candidate_edge:
  edge_id: edge.walmart.0397
  edge_type: USES_COLUMN
  source: metric_implementation.walmart.walmart_settlement.seller_realization_rate
  target: column.zs_observe.walmart_settlement.gross_commission
  fields:
    edge_family: dependency_usage
    evidence_basis: Metric implementation formula/filter/SQL uses this documented column.
    confidence: high
    canonical_cognee_edge: true
    marketplace_only: true
    canonical_edge_type: USES_COLUMN
    inverse_edge_type: USED_BY_CARD
    materialize_inverse: false
    edge_class: canonical
    source_type: metric_implementation
    target_type: column
    evidence_refs:
    - ev.walmart.metrics.001
    notes: Metric implementation formula/filter/SQL uses this documented column.
```

```yaml
candidate_edge:
  edge_id: edge.walmart.0398
  edge_type: USES_COLUMN
  source: metric_implementation.walmart.walmart_settlement.seller_realization_rate
  target: column.zs_observe.walmart_settlement.total_walmart_funded_savings
  fields:
    edge_family: dependency_usage
    evidence_basis: Metric implementation formula/filter/SQL uses this documented column.
    confidence: high
    canonical_cognee_edge: true
    marketplace_only: true
    canonical_edge_type: USES_COLUMN
    inverse_edge_type: USED_BY_CARD
    materialize_inverse: false
    edge_class: canonical
    source_type: metric_implementation
    target_type: column
    evidence_refs:
    - ev.walmart.metrics.001
    notes: Metric implementation formula/filter/SQL uses this documented column.
```

```yaml
candidate_edge:
  edge_id: edge.walmart.0399
  edge_type: USES_COLUMN
  source: metric_implementation.walmart.walmart_settlement.seller_realization_rate
  target: column.zs_observe.walmart_settlement.transaction_type
  fields:
    edge_family: dependency_usage
    evidence_basis: Metric implementation formula/filter/SQL uses this documented column.
    confidence: high
    canonical_cognee_edge: true
    marketplace_only: true
    canonical_edge_type: USES_COLUMN
    inverse_edge_type: USED_BY_CARD
    materialize_inverse: false
    edge_class: canonical
    source_type: metric_implementation
    target_type: column
    evidence_refs:
    - ev.walmart.metrics.001
    notes: Metric implementation formula/filter/SQL uses this documented column.
```

```yaml
candidate_edge:
  edge_id: edge.walmart.0400
  edge_type: USES_COLUMN
  source: metric_implementation.walmart.walmart_settlement.seller_realization_rate
  target: column.zs_observe.walmart_settlement.group_level_id
  fields:
    edge_family: dependency_usage
    evidence_basis: Metric implementation formula/filter/SQL uses this documented column.
    confidence: high
    canonical_cognee_edge: true
    marketplace_only: true
    canonical_edge_type: USES_COLUMN
    inverse_edge_type: USED_BY_CARD
    materialize_inverse: false
    edge_class: canonical
    source_type: metric_implementation
    target_type: column
    evidence_refs:
    - ev.walmart.metrics.001
    notes: Metric implementation formula/filter/SQL uses this documented column.
```

```yaml
candidate_edge:
  edge_id: edge.walmart.0401
  edge_type: USES_COLUMN
  source: metric_implementation.walmart.walmart_settlement.seller_realization_rate
  target: column.zs_observe.walmart_settlement.is_active
  fields:
    edge_family: dependency_usage
    evidence_basis: Metric implementation formula/filter/SQL uses this documented column.
    confidence: high
    canonical_cognee_edge: true
    marketplace_only: true
    canonical_edge_type: USES_COLUMN
    inverse_edge_type: USED_BY_CARD
    materialize_inverse: false
    edge_class: canonical
    source_type: metric_implementation
    target_type: column
    evidence_refs:
    - ev.walmart.metrics.001
    notes: Metric implementation formula/filter/SQL uses this documented column.
```

```yaml
candidate_edge:
  edge_id: edge.walmart.0402
  edge_type: IMPLEMENTS
  source: metric_implementation.walmart.walmart_settlement.effective_commission_rate
  target: metric.marketplace.effective_commission_rate
  fields:
    edge_family: metric_semantics
    evidence_basis: Inverse implementation-to-metric edge for direct traversal.
    confidence: high
    canonical_cognee_edge: true
    marketplace_only: true
    canonical_edge_type: IMPLEMENTS
    inverse_edge_type: IMPLEMENTED_BY
    materialize_inverse: false
    edge_class: canonical
    source_type: metric_implementation
    target_type: metric
    evidence_refs:
    - ev.walmart.reconciliation.001
    notes: Inverse implementation-to-metric edge for direct traversal.
```

```yaml
candidate_edge:
  edge_id: edge.walmart.0403
  edge_type: USES_COLUMN
  source: metric_implementation.walmart.walmart_settlement.effective_commission_rate
  target: column.zs_observe.walmart_settlement.order_id
  fields:
    edge_family: dependency_usage
    evidence_basis: Metric implementation formula/filter/SQL uses this documented column.
    confidence: high
    canonical_cognee_edge: true
    marketplace_only: true
    canonical_edge_type: USES_COLUMN
    inverse_edge_type: USED_BY_CARD
    materialize_inverse: false
    edge_class: canonical
    source_type: metric_implementation
    target_type: column
    evidence_refs:
    - ev.walmart.reconciliation.001
    notes: Metric implementation formula/filter/SQL uses this documented column.
```

```yaml
candidate_edge:
  edge_id: edge.walmart.0404
  edge_type: USES_COLUMN
  source: metric_implementation.walmart.walmart_settlement.effective_commission_rate
  target: column.zs_observe.walmart_settlement.sku_id
  fields:
    edge_family: dependency_usage
    evidence_basis: Metric implementation formula/filter/SQL uses this documented column.
    confidence: high
    canonical_cognee_edge: true
    marketplace_only: true
    canonical_edge_type: USES_COLUMN
    inverse_edge_type: USED_BY_CARD
    materialize_inverse: false
    edge_class: canonical
    source_type: metric_implementation
    target_type: column
    evidence_refs:
    - ev.walmart.reconciliation.001
    notes: Metric implementation formula/filter/SQL uses this documented column.
```

```yaml
candidate_edge:
  edge_id: edge.walmart.0405
  edge_type: USES_COLUMN
  source: metric_implementation.walmart.walmart_settlement.effective_commission_rate
  target: column.zs_observe.walmart_settlement.charged_amount_excluding_tax
  fields:
    edge_family: dependency_usage
    evidence_basis: Metric implementation formula/filter/SQL uses this documented column.
    confidence: high
    canonical_cognee_edge: true
    marketplace_only: true
    canonical_edge_type: USES_COLUMN
    inverse_edge_type: USED_BY_CARD
    materialize_inverse: false
    edge_class: canonical
    source_type: metric_implementation
    target_type: column
    evidence_refs:
    - ev.walmart.reconciliation.001
    notes: Metric implementation formula/filter/SQL uses this documented column.
```

```yaml
candidate_edge:
  edge_id: edge.walmart.0406
  edge_type: USES_COLUMN
  source: metric_implementation.walmart.walmart_settlement.effective_commission_rate
  target: column.zs_observe.walmart_settlement.gross_commission
  fields:
    edge_family: dependency_usage
    evidence_basis: Metric implementation formula/filter/SQL uses this documented column.
    confidence: high
    canonical_cognee_edge: true
    marketplace_only: true
    canonical_edge_type: USES_COLUMN
    inverse_edge_type: USED_BY_CARD
    materialize_inverse: false
    edge_class: canonical
    source_type: metric_implementation
    target_type: column
    evidence_refs:
    - ev.walmart.reconciliation.001
    notes: Metric implementation formula/filter/SQL uses this documented column.
```

```yaml
candidate_edge:
  edge_id: edge.walmart.0407
  edge_type: USES_COLUMN
  source: metric_implementation.walmart.walmart_settlement.effective_commission_rate
  target: column.zs_observe.walmart_settlement.product_price
  fields:
    edge_family: dependency_usage
    evidence_basis: Metric implementation formula/filter/SQL uses this documented column.
    confidence: high
    canonical_cognee_edge: true
    marketplace_only: true
    canonical_edge_type: USES_COLUMN
    inverse_edge_type: USED_BY_CARD
    materialize_inverse: false
    edge_class: canonical
    source_type: metric_implementation
    target_type: column
    evidence_refs:
    - ev.walmart.reconciliation.001
    notes: Metric implementation formula/filter/SQL uses this documented column.
```

```yaml
candidate_edge:
  edge_id: edge.walmart.0408
  edge_type: USES_COLUMN
  source: metric_implementation.walmart.walmart_settlement.effective_commission_rate
  target: column.zs_observe.walmart_settlement.transaction_type
  fields:
    edge_family: dependency_usage
    evidence_basis: Metric implementation formula/filter/SQL uses this documented column.
    confidence: high
    canonical_cognee_edge: true
    marketplace_only: true
    canonical_edge_type: USES_COLUMN
    inverse_edge_type: USED_BY_CARD
    materialize_inverse: false
    edge_class: canonical
    source_type: metric_implementation
    target_type: column
    evidence_refs:
    - ev.walmart.reconciliation.001
    notes: Metric implementation formula/filter/SQL uses this documented column.
```

```yaml
candidate_edge:
  edge_id: edge.walmart.0409
  edge_type: USES_COLUMN
  source: metric_implementation.walmart.walmart_settlement.effective_commission_rate
  target: column.zs_observe.walmart_settlement.group_level_id
  fields:
    edge_family: dependency_usage
    evidence_basis: Metric implementation formula/filter/SQL uses this documented column.
    confidence: high
    canonical_cognee_edge: true
    marketplace_only: true
    canonical_edge_type: USES_COLUMN
    inverse_edge_type: USED_BY_CARD
    materialize_inverse: false
    edge_class: canonical
    source_type: metric_implementation
    target_type: column
    evidence_refs:
    - ev.walmart.reconciliation.001
    notes: Metric implementation formula/filter/SQL uses this documented column.
```

```yaml
candidate_edge:
  edge_id: edge.walmart.0410
  edge_type: USES_COLUMN
  source: metric_implementation.walmart.walmart_settlement.effective_commission_rate
  target: column.zs_observe.walmart_settlement.is_active
  fields:
    edge_family: dependency_usage
    evidence_basis: Metric implementation formula/filter/SQL uses this documented column.
    confidence: high
    canonical_cognee_edge: true
    marketplace_only: true
    canonical_edge_type: USES_COLUMN
    inverse_edge_type: USED_BY_CARD
    materialize_inverse: false
    edge_class: canonical
    source_type: metric_implementation
    target_type: column
    evidence_refs:
    - ev.walmart.reconciliation.001
    notes: Metric implementation formula/filter/SQL uses this documented column.
```

```yaml
candidate_edge:
  edge_id: edge.walmart.0411
  edge_type: IMPLEMENTS
  source: metric_implementation.walmart.walmart_settlement.return_rate
  target: metric.marketplace.return_rate
  fields:
    edge_family: metric_semantics
    evidence_basis: Inverse implementation-to-metric edge for direct traversal.
    confidence: high
    canonical_cognee_edge: true
    marketplace_only: true
    canonical_edge_type: IMPLEMENTS
    inverse_edge_type: IMPLEMENTED_BY
    materialize_inverse: false
    edge_class: canonical
    source_type: metric_implementation
    target_type: metric
    evidence_refs:
    - ev.walmart.metrics.001
    notes: Inverse implementation-to-metric edge for direct traversal.
```

```yaml
candidate_edge:
  edge_id: edge.walmart.0412
  edge_type: USES_COLUMN
  source: metric_implementation.walmart.walmart_settlement.return_rate
  target: column.zs_observe.walmart_settlement.transaction_type
  fields:
    edge_family: dependency_usage
    evidence_basis: Metric implementation formula/filter/SQL uses this documented column.
    confidence: high
    canonical_cognee_edge: true
    marketplace_only: true
    canonical_edge_type: USES_COLUMN
    inverse_edge_type: USED_BY_CARD
    materialize_inverse: false
    edge_class: canonical
    source_type: metric_implementation
    target_type: column
    evidence_refs:
    - ev.walmart.metrics.001
    notes: Metric implementation formula/filter/SQL uses this documented column.
```

```yaml
candidate_edge:
  edge_id: edge.walmart.0413
  edge_type: USES_COLUMN
  source: metric_implementation.walmart.walmart_settlement.return_rate
  target: column.zs_observe.walmart_settlement.group_level_id
  fields:
    edge_family: dependency_usage
    evidence_basis: Metric implementation formula/filter/SQL uses this documented column.
    confidence: high
    canonical_cognee_edge: true
    marketplace_only: true
    canonical_edge_type: USES_COLUMN
    inverse_edge_type: USED_BY_CARD
    materialize_inverse: false
    edge_class: canonical
    source_type: metric_implementation
    target_type: column
    evidence_refs:
    - ev.walmart.metrics.001
    notes: Metric implementation formula/filter/SQL uses this documented column.
```

```yaml
candidate_edge:
  edge_id: edge.walmart.0414
  edge_type: USES_COLUMN
  source: metric_implementation.walmart.walmart_settlement.return_rate
  target: column.zs_observe.walmart_settlement.is_active
  fields:
    edge_family: dependency_usage
    evidence_basis: Metric implementation formula/filter/SQL uses this documented column.
    confidence: high
    canonical_cognee_edge: true
    marketplace_only: true
    canonical_edge_type: USES_COLUMN
    inverse_edge_type: USED_BY_CARD
    materialize_inverse: false
    edge_class: canonical
    source_type: metric_implementation
    target_type: column
    evidence_refs:
    - ev.walmart.metrics.001
    notes: Metric implementation formula/filter/SQL uses this documented column.
```

```yaml
candidate_edge:
  edge_id: edge.walmart.0415
  edge_type: IMPLEMENTS
  source: metric_implementation.walmart.walmart_oms.average_order_value
  target: metric.marketplace.average_order_value
  fields:
    edge_family: metric_semantics
    evidence_basis: Inverse implementation-to-metric edge for direct traversal.
    confidence: high
    canonical_cognee_edge: true
    marketplace_only: true
    canonical_edge_type: IMPLEMENTS
    inverse_edge_type: IMPLEMENTED_BY
    materialize_inverse: false
    edge_class: canonical
    source_type: metric_implementation
    target_type: metric
    evidence_refs:
    - ev.walmart.metrics.001
    notes: Inverse implementation-to-metric edge for direct traversal.
```

```yaml
candidate_edge:
  edge_id: edge.walmart.0416
  edge_type: USES_COLUMN
  source: metric_implementation.walmart.walmart_oms.average_order_value
  target: column.zs_observe.walmart_oms.charged_amount
  fields:
    edge_family: dependency_usage
    evidence_basis: Metric implementation formula/filter/SQL uses this documented column.
    confidence: high
    canonical_cognee_edge: true
    marketplace_only: true
    canonical_edge_type: USES_COLUMN
    inverse_edge_type: USED_BY_CARD
    materialize_inverse: false
    edge_class: canonical
    source_type: metric_implementation
    target_type: column
    evidence_refs:
    - ev.walmart.metrics.001
    notes: Metric implementation formula/filter/SQL uses this documented column.
```

```yaml
candidate_edge:
  edge_id: edge.walmart.0417
  edge_type: USES_COLUMN
  source: metric_implementation.walmart.walmart_oms.average_order_value
  target: column.zs_observe.walmart_oms.internal_txn_type
  fields:
    edge_family: dependency_usage
    evidence_basis: Metric implementation formula/filter/SQL uses this documented column.
    confidence: high
    canonical_cognee_edge: true
    marketplace_only: true
    canonical_edge_type: USES_COLUMN
    inverse_edge_type: USED_BY_CARD
    materialize_inverse: false
    edge_class: canonical
    source_type: metric_implementation
    target_type: column
    evidence_refs:
    - ev.walmart.metrics.001
    notes: Metric implementation formula/filter/SQL uses this documented column.
```

```yaml
candidate_edge:
  edge_id: edge.walmart.0418
  edge_type: USES_COLUMN
  source: metric_implementation.walmart.walmart_oms.average_order_value
  target: column.zs_observe.walmart_oms.order_status
  fields:
    edge_family: dependency_usage
    evidence_basis: Metric implementation formula/filter/SQL uses this documented column.
    confidence: high
    canonical_cognee_edge: true
    marketplace_only: true
    canonical_edge_type: USES_COLUMN
    inverse_edge_type: USED_BY_CARD
    materialize_inverse: false
    edge_class: canonical
    source_type: metric_implementation
    target_type: column
    evidence_refs:
    - ev.walmart.metrics.001
    notes: Metric implementation formula/filter/SQL uses this documented column.
```

```yaml
candidate_edge:
  edge_id: edge.walmart.0419
  edge_type: USES_COLUMN
  source: metric_implementation.walmart.walmart_oms.average_order_value
  target: column.zs_observe.walmart_oms.group_level_id
  fields:
    edge_family: dependency_usage
    evidence_basis: Metric implementation formula/filter/SQL uses this documented column.
    confidence: high
    canonical_cognee_edge: true
    marketplace_only: true
    canonical_edge_type: USES_COLUMN
    inverse_edge_type: USED_BY_CARD
    materialize_inverse: false
    edge_class: canonical
    source_type: metric_implementation
    target_type: column
    evidence_refs:
    - ev.walmart.metrics.001
    notes: Metric implementation formula/filter/SQL uses this documented column.
```

```yaml
candidate_edge:
  edge_id: edge.walmart.0420
  edge_type: USES_COLUMN
  source: metric_implementation.walmart.walmart_oms.average_order_value
  target: column.zs_observe.walmart_oms.is_active
  fields:
    edge_family: dependency_usage
    evidence_basis: Metric implementation formula/filter/SQL uses this documented column.
    confidence: high
    canonical_cognee_edge: true
    marketplace_only: true
    canonical_edge_type: USES_COLUMN
    inverse_edge_type: USED_BY_CARD
    materialize_inverse: false
    edge_class: canonical
    source_type: metric_implementation
    target_type: column
    evidence_refs:
    - ev.walmart.metrics.001
    notes: Metric implementation formula/filter/SQL uses this documented column.
```

```yaml
candidate_edge:
  edge_id: edge.walmart.0421
  edge_type: IMPLEMENTS
  source: metric_implementation.walmart.walmart_oms.cancellation_rate
  target: metric.marketplace.cancellation_rate
  fields:
    edge_family: metric_semantics
    evidence_basis: Inverse implementation-to-metric edge for direct traversal.
    confidence: high
    canonical_cognee_edge: true
    marketplace_only: true
    canonical_edge_type: IMPLEMENTS
    inverse_edge_type: IMPLEMENTED_BY
    materialize_inverse: false
    edge_class: canonical
    source_type: metric_implementation
    target_type: metric
    evidence_refs:
    - ev.walmart_oms.schema.001
    notes: Inverse implementation-to-metric edge for direct traversal.
```

```yaml
candidate_edge:
  edge_id: edge.walmart.0422
  edge_type: USES_COLUMN
  source: metric_implementation.walmart.walmart_oms.cancellation_rate
  target: column.zs_observe.walmart_oms.order_status
  fields:
    edge_family: dependency_usage
    evidence_basis: Metric implementation formula/filter/SQL uses this documented column.
    confidence: high
    canonical_cognee_edge: true
    marketplace_only: true
    canonical_edge_type: USES_COLUMN
    inverse_edge_type: USED_BY_CARD
    materialize_inverse: false
    edge_class: canonical
    source_type: metric_implementation
    target_type: column
    evidence_refs:
    - ev.walmart_oms.schema.001
    notes: Metric implementation formula/filter/SQL uses this documented column.
```

```yaml
candidate_edge:
  edge_id: edge.walmart.0423
  edge_type: USES_COLUMN
  source: metric_implementation.walmart.walmart_oms.cancellation_rate
  target: column.zs_observe.walmart_oms.group_level_id
  fields:
    edge_family: dependency_usage
    evidence_basis: Metric implementation formula/filter/SQL uses this documented column.
    confidence: high
    canonical_cognee_edge: true
    marketplace_only: true
    canonical_edge_type: USES_COLUMN
    inverse_edge_type: USED_BY_CARD
    materialize_inverse: false
    edge_class: canonical
    source_type: metric_implementation
    target_type: column
    evidence_refs:
    - ev.walmart_oms.schema.001
    notes: Metric implementation formula/filter/SQL uses this documented column.
```

```yaml
candidate_edge:
  edge_id: edge.walmart.0424
  edge_type: USES_COLUMN
  source: metric_implementation.walmart.walmart_oms.cancellation_rate
  target: column.zs_observe.walmart_oms.is_active
  fields:
    edge_family: dependency_usage
    evidence_basis: Metric implementation formula/filter/SQL uses this documented column.
    confidence: high
    canonical_cognee_edge: true
    marketplace_only: true
    canonical_edge_type: USES_COLUMN
    inverse_edge_type: USED_BY_CARD
    materialize_inverse: false
    edge_class: canonical
    source_type: metric_implementation
    target_type: column
    evidence_refs:
    - ev.walmart_oms.schema.001
    notes: Metric implementation formula/filter/SQL uses this documented column.
```

```yaml
candidate_edge:
  edge_id: edge.walmart.0425
  edge_type: IMPLEMENTS
  source: metric_implementation.walmart.walmart_settlement.tax_withheld
  target: metric.marketplace.tax_withheld
  fields:
    edge_family: metric_semantics
    evidence_basis: Inverse implementation-to-metric edge for direct traversal.
    confidence: high
    canonical_cognee_edge: true
    marketplace_only: true
    canonical_edge_type: IMPLEMENTS
    inverse_edge_type: IMPLEMENTED_BY
    materialize_inverse: false
    edge_class: canonical
    source_type: metric_implementation
    target_type: metric
    evidence_refs:
    - ev.walmart.business_model.001
    notes: Inverse implementation-to-metric edge for direct traversal.
```

```yaml
candidate_edge:
  edge_id: edge.walmart.0426
  edge_type: USES_COLUMN
  source: metric_implementation.walmart.walmart_settlement.tax_withheld
  target: column.zs_observe.walmart_settlement.charged_amount
  fields:
    edge_family: dependency_usage
    evidence_basis: Metric implementation formula/filter/SQL uses this documented column.
    confidence: high
    canonical_cognee_edge: true
    marketplace_only: true
    canonical_edge_type: USES_COLUMN
    inverse_edge_type: USED_BY_CARD
    materialize_inverse: false
    edge_class: canonical
    source_type: metric_implementation
    target_type: column
    evidence_refs:
    - ev.walmart.business_model.001
    notes: Metric implementation formula/filter/SQL uses this documented column.
```

```yaml
candidate_edge:
  edge_id: edge.walmart.0427
  edge_type: USES_COLUMN
  source: metric_implementation.walmart.walmart_settlement.tax_withheld
  target: column.zs_observe.walmart_settlement.charged_amount_excluding_tax
  fields:
    edge_family: dependency_usage
    evidence_basis: Metric implementation formula/filter/SQL uses this documented column.
    confidence: high
    canonical_cognee_edge: true
    marketplace_only: true
    canonical_edge_type: USES_COLUMN
    inverse_edge_type: USED_BY_CARD
    materialize_inverse: false
    edge_class: canonical
    source_type: metric_implementation
    target_type: column
    evidence_refs:
    - ev.walmart.business_model.001
    notes: Metric implementation formula/filter/SQL uses this documented column.
```

```yaml
candidate_edge:
  edge_id: edge.walmart.0428
  edge_type: USES_COLUMN
  source: metric_implementation.walmart.walmart_settlement.tax_withheld
  target: column.zs_observe.walmart_settlement.total_tax
  fields:
    edge_family: dependency_usage
    evidence_basis: Metric implementation formula/filter/SQL uses this documented column.
    confidence: high
    canonical_cognee_edge: true
    marketplace_only: true
    canonical_edge_type: USES_COLUMN
    inverse_edge_type: USED_BY_CARD
    materialize_inverse: false
    edge_class: canonical
    source_type: metric_implementation
    target_type: column
    evidence_refs:
    - ev.walmart.business_model.001
    notes: Metric implementation formula/filter/SQL uses this documented column.
```

```yaml
candidate_edge:
  edge_id: edge.walmart.0429
  edge_type: USES_COLUMN
  source: metric_implementation.walmart.walmart_settlement.tax_withheld
  target: column.zs_observe.walmart_settlement.marketplace_withheld_tax
  fields:
    edge_family: dependency_usage
    evidence_basis: Metric implementation formula/filter/SQL uses this documented column.
    confidence: high
    canonical_cognee_edge: true
    marketplace_only: true
    canonical_edge_type: USES_COLUMN
    inverse_edge_type: USED_BY_CARD
    materialize_inverse: false
    edge_class: canonical
    source_type: metric_implementation
    target_type: column
    evidence_refs:
    - ev.walmart.business_model.001
    notes: Metric implementation formula/filter/SQL uses this documented column.
```

```yaml
candidate_edge:
  edge_id: edge.walmart.0430
  edge_type: USES_COLUMN
  source: metric_implementation.walmart.walmart_settlement.tax_withheld
  target: column.zs_observe.walmart_settlement.transaction_type
  fields:
    edge_family: dependency_usage
    evidence_basis: Metric implementation formula/filter/SQL uses this documented column.
    confidence: high
    canonical_cognee_edge: true
    marketplace_only: true
    canonical_edge_type: USES_COLUMN
    inverse_edge_type: USED_BY_CARD
    materialize_inverse: false
    edge_class: canonical
    source_type: metric_implementation
    target_type: column
    evidence_refs:
    - ev.walmart.business_model.001
    notes: Metric implementation formula/filter/SQL uses this documented column.
```

```yaml
candidate_edge:
  edge_id: edge.walmart.0431
  edge_type: USES_COLUMN
  source: metric_implementation.walmart.walmart_settlement.tax_withheld
  target: column.zs_observe.walmart_settlement.group_level_id
  fields:
    edge_family: dependency_usage
    evidence_basis: Metric implementation formula/filter/SQL uses this documented column.
    confidence: high
    canonical_cognee_edge: true
    marketplace_only: true
    canonical_edge_type: USES_COLUMN
    inverse_edge_type: USED_BY_CARD
    materialize_inverse: false
    edge_class: canonical
    source_type: metric_implementation
    target_type: column
    evidence_refs:
    - ev.walmart.business_model.001
    notes: Metric implementation formula/filter/SQL uses this documented column.
```

```yaml
candidate_edge:
  edge_id: edge.walmart.0432
  edge_type: USES_COLUMN
  source: metric_implementation.walmart.walmart_settlement.tax_withheld
  target: column.zs_observe.walmart_settlement.is_active
  fields:
    edge_family: dependency_usage
    evidence_basis: Metric implementation formula/filter/SQL uses this documented column.
    confidence: high
    canonical_cognee_edge: true
    marketplace_only: true
    canonical_edge_type: USES_COLUMN
    inverse_edge_type: USED_BY_CARD
    materialize_inverse: false
    edge_class: canonical
    source_type: metric_implementation
    target_type: column
    evidence_refs:
    - ev.walmart.business_model.001
    notes: Metric implementation formula/filter/SQL uses this documented column.
```

```yaml
candidate_edge:
  edge_id: edge.walmart.0433
  edge_type: IMPLEMENTS
  source: metric_implementation.walmart.walmart_settlement.walmart_funded_savings
  target: metric.marketplace.walmart_funded_savings
  fields:
    edge_family: metric_semantics
    evidence_basis: Inverse implementation-to-metric edge for direct traversal.
    confidence: high
    canonical_cognee_edge: true
    marketplace_only: true
    canonical_edge_type: IMPLEMENTS
    inverse_edge_type: IMPLEMENTED_BY
    materialize_inverse: false
    edge_class: canonical
    source_type: metric_implementation
    target_type: metric
    evidence_refs:
    - ev.walmart.metrics.001
    notes: Inverse implementation-to-metric edge for direct traversal.
```

```yaml
candidate_edge:
  edge_id: edge.walmart.0434
  edge_type: USES_COLUMN
  source: metric_implementation.walmart.walmart_settlement.walmart_funded_savings
  target: column.zs_observe.walmart_settlement.charged_amount
  fields:
    edge_family: dependency_usage
    evidence_basis: Metric implementation formula/filter/SQL uses this documented column.
    confidence: high
    canonical_cognee_edge: true
    marketplace_only: true
    canonical_edge_type: USES_COLUMN
    inverse_edge_type: USED_BY_CARD
    materialize_inverse: false
    edge_class: canonical
    source_type: metric_implementation
    target_type: column
    evidence_refs:
    - ev.walmart.metrics.001
    notes: Metric implementation formula/filter/SQL uses this documented column.
```

```yaml
candidate_edge:
  edge_id: edge.walmart.0435
  edge_type: USES_COLUMN
  source: metric_implementation.walmart.walmart_settlement.walmart_funded_savings
  target: column.zs_observe.walmart_settlement.charged_amount_excluding_tax
  fields:
    edge_family: dependency_usage
    evidence_basis: Metric implementation formula/filter/SQL uses this documented column.
    confidence: high
    canonical_cognee_edge: true
    marketplace_only: true
    canonical_edge_type: USES_COLUMN
    inverse_edge_type: USED_BY_CARD
    materialize_inverse: false
    edge_class: canonical
    source_type: metric_implementation
    target_type: column
    evidence_refs:
    - ev.walmart.metrics.001
    notes: Metric implementation formula/filter/SQL uses this documented column.
```

```yaml
candidate_edge:
  edge_id: edge.walmart.0436
  edge_type: USES_COLUMN
  source: metric_implementation.walmart.walmart_settlement.walmart_funded_savings
  target: column.zs_observe.walmart_settlement.total_tax
  fields:
    edge_family: dependency_usage
    evidence_basis: Metric implementation formula/filter/SQL uses this documented column.
    confidence: high
    canonical_cognee_edge: true
    marketplace_only: true
    canonical_edge_type: USES_COLUMN
    inverse_edge_type: USED_BY_CARD
    materialize_inverse: false
    edge_class: canonical
    source_type: metric_implementation
    target_type: column
    evidence_refs:
    - ev.walmart.metrics.001
    notes: Metric implementation formula/filter/SQL uses this documented column.
```

```yaml
candidate_edge:
  edge_id: edge.walmart.0437
  edge_type: USES_COLUMN
  source: metric_implementation.walmart.walmart_settlement.walmart_funded_savings
  target: column.zs_observe.walmart_settlement.gross_commission
  fields:
    edge_family: dependency_usage
    evidence_basis: Metric implementation formula/filter/SQL uses this documented column.
    confidence: high
    canonical_cognee_edge: true
    marketplace_only: true
    canonical_edge_type: USES_COLUMN
    inverse_edge_type: USED_BY_CARD
    materialize_inverse: false
    edge_class: canonical
    source_type: metric_implementation
    target_type: column
    evidence_refs:
    - ev.walmart.metrics.001
    notes: Metric implementation formula/filter/SQL uses this documented column.
```

```yaml
candidate_edge:
  edge_id: edge.walmart.0438
  edge_type: USES_COLUMN
  source: metric_implementation.walmart.walmart_settlement.walmart_funded_savings
  target: column.zs_observe.walmart_settlement.total_walmart_funded_savings
  fields:
    edge_family: dependency_usage
    evidence_basis: Metric implementation formula/filter/SQL uses this documented column.
    confidence: high
    canonical_cognee_edge: true
    marketplace_only: true
    canonical_edge_type: USES_COLUMN
    inverse_edge_type: USED_BY_CARD
    materialize_inverse: false
    edge_class: canonical
    source_type: metric_implementation
    target_type: column
    evidence_refs:
    - ev.walmart.metrics.001
    notes: Metric implementation formula/filter/SQL uses this documented column.
```

```yaml
candidate_edge:
  edge_id: edge.walmart.0439
  edge_type: USES_COLUMN
  source: metric_implementation.walmart.walmart_settlement.walmart_funded_savings
  target: column.zs_observe.walmart_settlement.transaction_type
  fields:
    edge_family: dependency_usage
    evidence_basis: Metric implementation formula/filter/SQL uses this documented column.
    confidence: high
    canonical_cognee_edge: true
    marketplace_only: true
    canonical_edge_type: USES_COLUMN
    inverse_edge_type: USED_BY_CARD
    materialize_inverse: false
    edge_class: canonical
    source_type: metric_implementation
    target_type: column
    evidence_refs:
    - ev.walmart.metrics.001
    notes: Metric implementation formula/filter/SQL uses this documented column.
```

```yaml
candidate_edge:
  edge_id: edge.walmart.0440
  edge_type: USES_COLUMN
  source: metric_implementation.walmart.walmart_settlement.walmart_funded_savings
  target: column.zs_observe.walmart_settlement.group_level_id
  fields:
    edge_family: dependency_usage
    evidence_basis: Metric implementation formula/filter/SQL uses this documented column.
    confidence: high
    canonical_cognee_edge: true
    marketplace_only: true
    canonical_edge_type: USES_COLUMN
    inverse_edge_type: USED_BY_CARD
    materialize_inverse: false
    edge_class: canonical
    source_type: metric_implementation
    target_type: column
    evidence_refs:
    - ev.walmart.metrics.001
    notes: Metric implementation formula/filter/SQL uses this documented column.
```

```yaml
candidate_edge:
  edge_id: edge.walmart.0441
  edge_type: USES_COLUMN
  source: metric_implementation.walmart.walmart_settlement.walmart_funded_savings
  target: column.zs_observe.walmart_settlement.is_active
  fields:
    edge_family: dependency_usage
    evidence_basis: Metric implementation formula/filter/SQL uses this documented column.
    confidence: high
    canonical_cognee_edge: true
    marketplace_only: true
    canonical_edge_type: USES_COLUMN
    inverse_edge_type: USED_BY_CARD
    materialize_inverse: false
    edge_class: canonical
    source_type: metric_implementation
    target_type: column
    evidence_refs:
    - ev.walmart.metrics.001
    notes: Metric implementation formula/filter/SQL uses this documented column.
```

```yaml
candidate_edge:
  edge_id: edge.walmart.0442
  edge_type: IMPLEMENTS
  source: metric_implementation.walmart.walmart_settlement.sku_revenue
  target: metric.marketplace.sku_revenue
  fields:
    edge_family: metric_semantics
    evidence_basis: Inverse implementation-to-metric edge for direct traversal.
    confidence: high
    canonical_cognee_edge: true
    marketplace_only: true
    canonical_edge_type: IMPLEMENTS
    inverse_edge_type: IMPLEMENTED_BY
    materialize_inverse: false
    edge_class: canonical
    source_type: metric_implementation
    target_type: metric
    evidence_refs:
    - ev.walmart.metrics.001
    notes: Inverse implementation-to-metric edge for direct traversal.
```

```yaml
candidate_edge:
  edge_id: edge.walmart.0443
  edge_type: USES_COLUMN
  source: metric_implementation.walmart.walmart_settlement.sku_revenue
  target: column.zs_observe.walmart_settlement.sku_id
  fields:
    edge_family: dependency_usage
    evidence_basis: Metric implementation formula/filter/SQL uses this documented column.
    confidence: high
    canonical_cognee_edge: true
    marketplace_only: true
    canonical_edge_type: USES_COLUMN
    inverse_edge_type: USED_BY_CARD
    materialize_inverse: false
    edge_class: canonical
    source_type: metric_implementation
    target_type: column
    evidence_refs:
    - ev.walmart.metrics.001
    notes: Metric implementation formula/filter/SQL uses this documented column.
```

```yaml
candidate_edge:
  edge_id: edge.walmart.0444
  edge_type: USES_COLUMN
  source: metric_implementation.walmart.walmart_settlement.sku_revenue
  target: column.zs_observe.walmart_settlement.charged_amount
  fields:
    edge_family: dependency_usage
    evidence_basis: Metric implementation formula/filter/SQL uses this documented column.
    confidence: high
    canonical_cognee_edge: true
    marketplace_only: true
    canonical_edge_type: USES_COLUMN
    inverse_edge_type: USED_BY_CARD
    materialize_inverse: false
    edge_class: canonical
    source_type: metric_implementation
    target_type: column
    evidence_refs:
    - ev.walmart.metrics.001
    notes: Metric implementation formula/filter/SQL uses this documented column.
```

```yaml
candidate_edge:
  edge_id: edge.walmart.0445
  edge_type: USES_COLUMN
  source: metric_implementation.walmart.walmart_settlement.sku_revenue
  target: column.zs_observe.walmart_settlement.charged_amount_excluding_tax
  fields:
    edge_family: dependency_usage
    evidence_basis: Metric implementation formula/filter/SQL uses this documented column.
    confidence: high
    canonical_cognee_edge: true
    marketplace_only: true
    canonical_edge_type: USES_COLUMN
    inverse_edge_type: USED_BY_CARD
    materialize_inverse: false
    edge_class: canonical
    source_type: metric_implementation
    target_type: column
    evidence_refs:
    - ev.walmart.metrics.001
    notes: Metric implementation formula/filter/SQL uses this documented column.
```

```yaml
candidate_edge:
  edge_id: edge.walmart.0446
  edge_type: USES_COLUMN
  source: metric_implementation.walmart.walmart_settlement.sku_revenue
  target: column.zs_observe.walmart_settlement.gross_commission
  fields:
    edge_family: dependency_usage
    evidence_basis: Metric implementation formula/filter/SQL uses this documented column.
    confidence: high
    canonical_cognee_edge: true
    marketplace_only: true
    canonical_edge_type: USES_COLUMN
    inverse_edge_type: USED_BY_CARD
    materialize_inverse: false
    edge_class: canonical
    source_type: metric_implementation
    target_type: column
    evidence_refs:
    - ev.walmart.metrics.001
    notes: Metric implementation formula/filter/SQL uses this documented column.
```

```yaml
candidate_edge:
  edge_id: edge.walmart.0447
  edge_type: USES_COLUMN
  source: metric_implementation.walmart.walmart_settlement.sku_revenue
  target: column.zs_observe.walmart_settlement.transaction_type
  fields:
    edge_family: dependency_usage
    evidence_basis: Metric implementation formula/filter/SQL uses this documented column.
    confidence: high
    canonical_cognee_edge: true
    marketplace_only: true
    canonical_edge_type: USES_COLUMN
    inverse_edge_type: USED_BY_CARD
    materialize_inverse: false
    edge_class: canonical
    source_type: metric_implementation
    target_type: column
    evidence_refs:
    - ev.walmart.metrics.001
    notes: Metric implementation formula/filter/SQL uses this documented column.
```

```yaml
candidate_edge:
  edge_id: edge.walmart.0448
  edge_type: USES_COLUMN
  source: metric_implementation.walmart.walmart_settlement.sku_revenue
  target: column.zs_observe.walmart_settlement.product_type
  fields:
    edge_family: dependency_usage
    evidence_basis: Metric implementation formula/filter/SQL uses this documented column.
    confidence: high
    canonical_cognee_edge: true
    marketplace_only: true
    canonical_edge_type: USES_COLUMN
    inverse_edge_type: USED_BY_CARD
    materialize_inverse: false
    edge_class: canonical
    source_type: metric_implementation
    target_type: column
    evidence_refs:
    - ev.walmart.metrics.001
    notes: Metric implementation formula/filter/SQL uses this documented column.
```

```yaml
candidate_edge:
  edge_id: edge.walmart.0449
  edge_type: USES_COLUMN
  source: metric_implementation.walmart.walmart_settlement.sku_revenue
  target: column.zs_observe.walmart_settlement.group_level_id
  fields:
    edge_family: dependency_usage
    evidence_basis: Metric implementation formula/filter/SQL uses this documented column.
    confidence: high
    canonical_cognee_edge: true
    marketplace_only: true
    canonical_edge_type: USES_COLUMN
    inverse_edge_type: USED_BY_CARD
    materialize_inverse: false
    edge_class: canonical
    source_type: metric_implementation
    target_type: column
    evidence_refs:
    - ev.walmart.metrics.001
    notes: Metric implementation formula/filter/SQL uses this documented column.
```

```yaml
candidate_edge:
  edge_id: edge.walmart.0450
  edge_type: USES_COLUMN
  source: metric_implementation.walmart.walmart_settlement.sku_revenue
  target: column.zs_observe.walmart_settlement.is_active
  fields:
    edge_family: dependency_usage
    evidence_basis: Metric implementation formula/filter/SQL uses this documented column.
    confidence: high
    canonical_cognee_edge: true
    marketplace_only: true
    canonical_edge_type: USES_COLUMN
    inverse_edge_type: USED_BY_CARD
    materialize_inverse: false
    edge_class: canonical
    source_type: metric_implementation
    target_type: column
    evidence_refs:
    - ev.walmart.metrics.001
    notes: Metric implementation formula/filter/SQL uses this documented column.
```

```yaml
candidate_edge:
  edge_id: edge.walmart.0451
  edge_type: USES_COLUMN
  source: metric_implementation.walmart.walmart_settlement.sku_revenue
  target: column.zs_observe.walmart_lookup.sku_id
  fields:
    edge_family: dependency_usage
    evidence_basis: Metric implementation formula/filter/SQL uses this documented column.
    confidence: high
    canonical_cognee_edge: true
    marketplace_only: true
    canonical_edge_type: USES_COLUMN
    inverse_edge_type: USED_BY_CARD
    materialize_inverse: false
    edge_class: canonical
    source_type: metric_implementation
    target_type: column
    evidence_refs:
    - ev.walmart.metrics.001
    notes: Metric implementation formula/filter/SQL uses this documented column.
```

```yaml
candidate_edge:
  edge_id: edge.walmart.0452
  edge_type: USES_COLUMN
  source: metric_implementation.walmart.walmart_settlement.sku_revenue
  target: column.zs_observe.walmart_lookup.sku
  fields:
    edge_family: dependency_usage
    evidence_basis: Metric implementation formula/filter/SQL uses this documented column.
    confidence: high
    canonical_cognee_edge: true
    marketplace_only: true
    canonical_edge_type: USES_COLUMN
    inverse_edge_type: USED_BY_CARD
    materialize_inverse: false
    edge_class: canonical
    source_type: metric_implementation
    target_type: column
    evidence_refs:
    - ev.walmart.metrics.001
    notes: Metric implementation formula/filter/SQL uses this documented column.
```

```yaml
candidate_edge:
  edge_id: edge.walmart.0453
  edge_type: USES_COLUMN
  source: metric_implementation.walmart.walmart_settlement.sku_revenue
  target: column.zs_observe.walmart_lookup.item_name
  fields:
    edge_family: dependency_usage
    evidence_basis: Metric implementation formula/filter/SQL uses this documented column.
    confidence: high
    canonical_cognee_edge: true
    marketplace_only: true
    canonical_edge_type: USES_COLUMN
    inverse_edge_type: USED_BY_CARD
    materialize_inverse: false
    edge_class: canonical
    source_type: metric_implementation
    target_type: column
    evidence_refs:
    - ev.walmart.metrics.001
    notes: Metric implementation formula/filter/SQL uses this documented column.
```

```yaml
candidate_edge:
  edge_id: edge.walmart.0454
  edge_type: USES_COLUMN
  source: metric_implementation.walmart.walmart_settlement.sku_revenue
  target: column.zs_observe.walmart_lookup.group_level_id
  fields:
    edge_family: dependency_usage
    evidence_basis: Metric implementation formula/filter/SQL uses this documented column.
    confidence: high
    canonical_cognee_edge: true
    marketplace_only: true
    canonical_edge_type: USES_COLUMN
    inverse_edge_type: USED_BY_CARD
    materialize_inverse: false
    edge_class: canonical
    source_type: metric_implementation
    target_type: column
    evidence_refs:
    - ev.walmart.metrics.001
    notes: Metric implementation formula/filter/SQL uses this documented column.
```

```yaml
candidate_edge:
  edge_id: edge.walmart.0455
  edge_type: USES_COLUMN
  source: metric_implementation.walmart.walmart_settlement.sku_revenue
  target: column.zs_observe.walmart_lookup.is_active
  fields:
    edge_family: dependency_usage
    evidence_basis: Metric implementation formula/filter/SQL uses this documented column.
    confidence: high
    canonical_cognee_edge: true
    marketplace_only: true
    canonical_edge_type: USES_COLUMN
    inverse_edge_type: USED_BY_CARD
    materialize_inverse: false
    edge_class: canonical
    source_type: metric_implementation
    target_type: column
    evidence_refs:
    - ev.walmart.metrics.001
    notes: Metric implementation formula/filter/SQL uses this documented column.
```

```yaml
candidate_edge:
  edge_id: edge.walmart.0456
  edge_type: IMPLEMENTS
  source: metric_implementation.walmart.walmart_oms.revenue_by_state
  target: metric.marketplace.revenue_by_state
  fields:
    edge_family: metric_semantics
    evidence_basis: Inverse implementation-to-metric edge for direct traversal.
    confidence: high
    canonical_cognee_edge: true
    marketplace_only: true
    canonical_edge_type: IMPLEMENTS
    inverse_edge_type: IMPLEMENTED_BY
    materialize_inverse: false
    edge_class: canonical
    source_type: metric_implementation
    target_type: metric
    evidence_refs:
    - ev.walmart.metrics.001
    notes: Inverse implementation-to-metric edge for direct traversal.
```

```yaml
candidate_edge:
  edge_id: edge.walmart.0457
  edge_type: USES_COLUMN
  source: metric_implementation.walmart.walmart_oms.revenue_by_state
  target: column.zs_observe.walmart_oms.charged_amount
  fields:
    edge_family: dependency_usage
    evidence_basis: Metric implementation formula/filter/SQL uses this documented column.
    confidence: high
    canonical_cognee_edge: true
    marketplace_only: true
    canonical_edge_type: USES_COLUMN
    inverse_edge_type: USED_BY_CARD
    materialize_inverse: false
    edge_class: canonical
    source_type: metric_implementation
    target_type: column
    evidence_refs:
    - ev.walmart.metrics.001
    notes: Metric implementation formula/filter/SQL uses this documented column.
```

```yaml
candidate_edge:
  edge_id: edge.walmart.0458
  edge_type: USES_COLUMN
  source: metric_implementation.walmart.walmart_oms.revenue_by_state
  target: column.zs_observe.walmart_oms.order_status
  fields:
    edge_family: dependency_usage
    evidence_basis: Metric implementation formula/filter/SQL uses this documented column.
    confidence: high
    canonical_cognee_edge: true
    marketplace_only: true
    canonical_edge_type: USES_COLUMN
    inverse_edge_type: USED_BY_CARD
    materialize_inverse: false
    edge_class: canonical
    source_type: metric_implementation
    target_type: column
    evidence_refs:
    - ev.walmart.metrics.001
    notes: Metric implementation formula/filter/SQL uses this documented column.
```

```yaml
candidate_edge:
  edge_id: edge.walmart.0459
  edge_type: USES_COLUMN
  source: metric_implementation.walmart.walmart_oms.revenue_by_state
  target: column.zs_observe.walmart_oms.destination_state
  fields:
    edge_family: dependency_usage
    evidence_basis: Metric implementation formula/filter/SQL uses this documented column.
    confidence: high
    canonical_cognee_edge: true
    marketplace_only: true
    canonical_edge_type: USES_COLUMN
    inverse_edge_type: USED_BY_CARD
    materialize_inverse: false
    edge_class: canonical
    source_type: metric_implementation
    target_type: column
    evidence_refs:
    - ev.walmart.metrics.001
    notes: Metric implementation formula/filter/SQL uses this documented column.
```

```yaml
candidate_edge:
  edge_id: edge.walmart.0460
  edge_type: USES_COLUMN
  source: metric_implementation.walmart.walmart_oms.revenue_by_state
  target: column.zs_observe.walmart_oms.group_level_id
  fields:
    edge_family: dependency_usage
    evidence_basis: Metric implementation formula/filter/SQL uses this documented column.
    confidence: high
    canonical_cognee_edge: true
    marketplace_only: true
    canonical_edge_type: USES_COLUMN
    inverse_edge_type: USED_BY_CARD
    materialize_inverse: false
    edge_class: canonical
    source_type: metric_implementation
    target_type: column
    evidence_refs:
    - ev.walmart.metrics.001
    notes: Metric implementation formula/filter/SQL uses this documented column.
```

```yaml
candidate_edge:
  edge_id: edge.walmart.0461
  edge_type: USES_COLUMN
  source: metric_implementation.walmart.walmart_oms.revenue_by_state
  target: column.zs_observe.walmart_oms.is_active
  fields:
    edge_family: dependency_usage
    evidence_basis: Metric implementation formula/filter/SQL uses this documented column.
    confidence: high
    canonical_cognee_edge: true
    marketplace_only: true
    canonical_edge_type: USES_COLUMN
    inverse_edge_type: USED_BY_CARD
    materialize_inverse: false
    edge_class: canonical
    source_type: metric_implementation
    target_type: column
    evidence_refs:
    - ev.walmart.metrics.001
    notes: Metric implementation formula/filter/SQL uses this documented column.
```

```yaml
candidate_edge:
  edge_id: edge.walmart.0462
  edge_type: USES_COLUMN
  source: query_pattern.walmart.forward_gmv_net_payout
  target: column.zs_observe.walmart_settlement.charged_amount
  fields:
    edge_family: dependency_usage
    evidence_basis: Query pattern SQL/template uses this documented column.
    confidence: high
    canonical_cognee_edge: true
    marketplace_only: true
    canonical_edge_type: USES_COLUMN
    inverse_edge_type: USED_BY_CARD
    materialize_inverse: false
    edge_class: canonical
    source_type: query_pattern
    target_type: column
    evidence_refs:
    - ev.walmart.metrics.001
    notes: Query pattern SQL/template uses this documented column.
```

```yaml
candidate_edge:
  edge_id: edge.walmart.0463
  edge_type: USES_COLUMN
  source: query_pattern.walmart.forward_gmv_net_payout
  target: column.zs_observe.walmart_settlement.charged_amount_excluding_tax
  fields:
    edge_family: dependency_usage
    evidence_basis: Query pattern SQL/template uses this documented column.
    confidence: high
    canonical_cognee_edge: true
    marketplace_only: true
    canonical_edge_type: USES_COLUMN
    inverse_edge_type: USED_BY_CARD
    materialize_inverse: false
    edge_class: canonical
    source_type: query_pattern
    target_type: column
    evidence_refs:
    - ev.walmart.metrics.001
    notes: Query pattern SQL/template uses this documented column.
```

```yaml
candidate_edge:
  edge_id: edge.walmart.0464
  edge_type: USES_COLUMN
  source: query_pattern.walmart.forward_gmv_net_payout
  target: column.zs_observe.walmart_settlement.total_tax
  fields:
    edge_family: dependency_usage
    evidence_basis: Query pattern SQL/template uses this documented column.
    confidence: high
    canonical_cognee_edge: true
    marketplace_only: true
    canonical_edge_type: USES_COLUMN
    inverse_edge_type: USED_BY_CARD
    materialize_inverse: false
    edge_class: canonical
    source_type: query_pattern
    target_type: column
    evidence_refs:
    - ev.walmart.metrics.001
    notes: Query pattern SQL/template uses this documented column.
```

```yaml
candidate_edge:
  edge_id: edge.walmart.0465
  edge_type: USES_COLUMN
  source: query_pattern.walmart.forward_gmv_net_payout
  target: column.zs_observe.walmart_settlement.gross_commission
  fields:
    edge_family: dependency_usage
    evidence_basis: Query pattern SQL/template uses this documented column.
    confidence: high
    canonical_cognee_edge: true
    marketplace_only: true
    canonical_edge_type: USES_COLUMN
    inverse_edge_type: USED_BY_CARD
    materialize_inverse: false
    edge_class: canonical
    source_type: query_pattern
    target_type: column
    evidence_refs:
    - ev.walmart.metrics.001
    notes: Query pattern SQL/template uses this documented column.
```

```yaml
candidate_edge:
  edge_id: edge.walmart.0466
  edge_type: USES_COLUMN
  source: query_pattern.walmart.forward_gmv_net_payout
  target: column.zs_observe.walmart_settlement.total_walmart_funded_savings
  fields:
    edge_family: dependency_usage
    evidence_basis: Query pattern SQL/template uses this documented column.
    confidence: high
    canonical_cognee_edge: true
    marketplace_only: true
    canonical_edge_type: USES_COLUMN
    inverse_edge_type: USED_BY_CARD
    materialize_inverse: false
    edge_class: canonical
    source_type: query_pattern
    target_type: column
    evidence_refs:
    - ev.walmart.metrics.001
    notes: Query pattern SQL/template uses this documented column.
```

```yaml
candidate_edge:
  edge_id: edge.walmart.0467
  edge_type: USES_COLUMN
  source: query_pattern.walmart.forward_gmv_net_payout
  target: column.zs_observe.walmart_settlement.transaction_type
  fields:
    edge_family: dependency_usage
    evidence_basis: Query pattern SQL/template uses this documented column.
    confidence: high
    canonical_cognee_edge: true
    marketplace_only: true
    canonical_edge_type: USES_COLUMN
    inverse_edge_type: USED_BY_CARD
    materialize_inverse: false
    edge_class: canonical
    source_type: query_pattern
    target_type: column
    evidence_refs:
    - ev.walmart.metrics.001
    notes: Query pattern SQL/template uses this documented column.
```

```yaml
candidate_edge:
  edge_id: edge.walmart.0468
  edge_type: USES_COLUMN
  source: query_pattern.walmart.forward_gmv_net_payout
  target: column.zs_observe.walmart_settlement.group_level_id
  fields:
    edge_family: dependency_usage
    evidence_basis: Query pattern SQL/template uses this documented column.
    confidence: high
    canonical_cognee_edge: true
    marketplace_only: true
    canonical_edge_type: USES_COLUMN
    inverse_edge_type: USED_BY_CARD
    materialize_inverse: false
    edge_class: canonical
    source_type: query_pattern
    target_type: column
    evidence_refs:
    - ev.walmart.metrics.001
    notes: Query pattern SQL/template uses this documented column.
```

```yaml
candidate_edge:
  edge_id: edge.walmart.0469
  edge_type: USES_COLUMN
  source: query_pattern.walmart.forward_gmv_net_payout
  target: column.zs_observe.walmart_settlement.is_active
  fields:
    edge_family: dependency_usage
    evidence_basis: Query pattern SQL/template uses this documented column.
    confidence: high
    canonical_cognee_edge: true
    marketplace_only: true
    canonical_edge_type: USES_COLUMN
    inverse_edge_type: USED_BY_CARD
    materialize_inverse: false
    edge_class: canonical
    source_type: query_pattern
    target_type: column
    evidence_refs:
    - ev.walmart.metrics.001
    notes: Query pattern SQL/template uses this documented column.
```

```yaml
candidate_edge:
  edge_id: edge.walmart.0470
  edge_type: USES_COLUMN
  source: query_pattern.walmart.return_rate
  target: column.zs_observe.walmart_settlement.transaction_type
  fields:
    edge_family: dependency_usage
    evidence_basis: Query pattern SQL/template uses this documented column.
    confidence: high
    canonical_cognee_edge: true
    marketplace_only: true
    canonical_edge_type: USES_COLUMN
    inverse_edge_type: USED_BY_CARD
    materialize_inverse: false
    edge_class: canonical
    source_type: query_pattern
    target_type: column
    evidence_refs:
    - ev.walmart.metrics.001
    notes: Query pattern SQL/template uses this documented column.
```

```yaml
candidate_edge:
  edge_id: edge.walmart.0471
  edge_type: USES_COLUMN
  source: query_pattern.walmart.return_rate
  target: column.zs_observe.walmart_settlement.group_level_id
  fields:
    edge_family: dependency_usage
    evidence_basis: Query pattern SQL/template uses this documented column.
    confidence: high
    canonical_cognee_edge: true
    marketplace_only: true
    canonical_edge_type: USES_COLUMN
    inverse_edge_type: USED_BY_CARD
    materialize_inverse: false
    edge_class: canonical
    source_type: query_pattern
    target_type: column
    evidence_refs:
    - ev.walmart.metrics.001
    notes: Query pattern SQL/template uses this documented column.
```

```yaml
candidate_edge:
  edge_id: edge.walmart.0472
  edge_type: USES_COLUMN
  source: query_pattern.walmart.return_rate
  target: column.zs_observe.walmart_settlement.is_active
  fields:
    edge_family: dependency_usage
    evidence_basis: Query pattern SQL/template uses this documented column.
    confidence: high
    canonical_cognee_edge: true
    marketplace_only: true
    canonical_edge_type: USES_COLUMN
    inverse_edge_type: USED_BY_CARD
    materialize_inverse: false
    edge_class: canonical
    source_type: query_pattern
    target_type: column
    evidence_refs:
    - ev.walmart.metrics.001
    notes: Query pattern SQL/template uses this documented column.
```

```yaml
candidate_edge:
  edge_id: edge.walmart.0473
  edge_type: USES_COLUMN
  source: query_pattern.walmart.oms_aov
  target: column.zs_observe.walmart_oms.charged_amount
  fields:
    edge_family: dependency_usage
    evidence_basis: Query pattern SQL/template uses this documented column.
    confidence: high
    canonical_cognee_edge: true
    marketplace_only: true
    canonical_edge_type: USES_COLUMN
    inverse_edge_type: USED_BY_CARD
    materialize_inverse: false
    edge_class: canonical
    source_type: query_pattern
    target_type: column
    evidence_refs:
    - ev.walmart.metrics.001
    notes: Query pattern SQL/template uses this documented column.
```

```yaml
candidate_edge:
  edge_id: edge.walmart.0474
  edge_type: USES_COLUMN
  source: query_pattern.walmart.oms_aov
  target: column.zs_observe.walmart_oms.internal_txn_type
  fields:
    edge_family: dependency_usage
    evidence_basis: Query pattern SQL/template uses this documented column.
    confidence: high
    canonical_cognee_edge: true
    marketplace_only: true
    canonical_edge_type: USES_COLUMN
    inverse_edge_type: USED_BY_CARD
    materialize_inverse: false
    edge_class: canonical
    source_type: query_pattern
    target_type: column
    evidence_refs:
    - ev.walmart.metrics.001
    notes: Query pattern SQL/template uses this documented column.
```

```yaml
candidate_edge:
  edge_id: edge.walmart.0475
  edge_type: USES_COLUMN
  source: query_pattern.walmart.oms_aov
  target: column.zs_observe.walmart_oms.order_status
  fields:
    edge_family: dependency_usage
    evidence_basis: Query pattern SQL/template uses this documented column.
    confidence: high
    canonical_cognee_edge: true
    marketplace_only: true
    canonical_edge_type: USES_COLUMN
    inverse_edge_type: USED_BY_CARD
    materialize_inverse: false
    edge_class: canonical
    source_type: query_pattern
    target_type: column
    evidence_refs:
    - ev.walmart.metrics.001
    notes: Query pattern SQL/template uses this documented column.
```

```yaml
candidate_edge:
  edge_id: edge.walmart.0476
  edge_type: USES_COLUMN
  source: query_pattern.walmart.oms_aov
  target: column.zs_observe.walmart_oms.group_level_id
  fields:
    edge_family: dependency_usage
    evidence_basis: Query pattern SQL/template uses this documented column.
    confidence: high
    canonical_cognee_edge: true
    marketplace_only: true
    canonical_edge_type: USES_COLUMN
    inverse_edge_type: USED_BY_CARD
    materialize_inverse: false
    edge_class: canonical
    source_type: query_pattern
    target_type: column
    evidence_refs:
    - ev.walmart.metrics.001
    notes: Query pattern SQL/template uses this documented column.
```

```yaml
candidate_edge:
  edge_id: edge.walmart.0477
  edge_type: USES_COLUMN
  source: query_pattern.walmart.oms_aov
  target: column.zs_observe.walmart_oms.is_active
  fields:
    edge_family: dependency_usage
    evidence_basis: Query pattern SQL/template uses this documented column.
    confidence: high
    canonical_cognee_edge: true
    marketplace_only: true
    canonical_edge_type: USES_COLUMN
    inverse_edge_type: USED_BY_CARD
    materialize_inverse: false
    edge_class: canonical
    source_type: query_pattern
    target_type: column
    evidence_refs:
    - ev.walmart.metrics.001
    notes: Query pattern SQL/template uses this documented column.
```

```yaml
candidate_edge:
  edge_id: edge.walmart.0478
  edge_type: USES_COLUMN
  source: query_pattern.walmart.cancellation_rate
  target: column.zs_observe.walmart_oms.order_status
  fields:
    edge_family: dependency_usage
    evidence_basis: Query pattern SQL/template uses this documented column.
    confidence: high
    canonical_cognee_edge: true
    marketplace_only: true
    canonical_edge_type: USES_COLUMN
    inverse_edge_type: USED_BY_CARD
    materialize_inverse: false
    edge_class: canonical
    source_type: query_pattern
    target_type: column
    evidence_refs:
    - ev.walmart_oms.schema.001
    notes: Query pattern SQL/template uses this documented column.
```

```yaml
candidate_edge:
  edge_id: edge.walmart.0479
  edge_type: USES_COLUMN
  source: query_pattern.walmart.cancellation_rate
  target: column.zs_observe.walmart_oms.group_level_id
  fields:
    edge_family: dependency_usage
    evidence_basis: Query pattern SQL/template uses this documented column.
    confidence: high
    canonical_cognee_edge: true
    marketplace_only: true
    canonical_edge_type: USES_COLUMN
    inverse_edge_type: USED_BY_CARD
    materialize_inverse: false
    edge_class: canonical
    source_type: query_pattern
    target_type: column
    evidence_refs:
    - ev.walmart_oms.schema.001
    notes: Query pattern SQL/template uses this documented column.
```

```yaml
candidate_edge:
  edge_id: edge.walmart.0480
  edge_type: USES_COLUMN
  source: query_pattern.walmart.cancellation_rate
  target: column.zs_observe.walmart_oms.is_active
  fields:
    edge_family: dependency_usage
    evidence_basis: Query pattern SQL/template uses this documented column.
    confidence: high
    canonical_cognee_edge: true
    marketplace_only: true
    canonical_edge_type: USES_COLUMN
    inverse_edge_type: USED_BY_CARD
    materialize_inverse: false
    edge_class: canonical
    source_type: query_pattern
    target_type: column
    evidence_refs:
    - ev.walmart_oms.schema.001
    notes: Query pattern SQL/template uses this documented column.
```

```yaml
candidate_edge:
  edge_id: edge.walmart.0481
  edge_type: USES_COLUMN
  source: query_pattern.walmart.monthly_revenue
  target: column.zs_observe.walmart_settlement.metadata_2
  fields:
    edge_family: dependency_usage
    evidence_basis: Query pattern SQL/template uses this documented column.
    confidence: high
    canonical_cognee_edge: true
    marketplace_only: true
    canonical_edge_type: USES_COLUMN
    inverse_edge_type: USED_BY_CARD
    materialize_inverse: false
    edge_class: canonical
    source_type: query_pattern
    target_type: column
    evidence_refs:
    - ev.walmart.metrics.001
    notes: Query pattern SQL/template uses this documented column.
```

```yaml
candidate_edge:
  edge_id: edge.walmart.0482
  edge_type: USES_COLUMN
  source: query_pattern.walmart.monthly_revenue
  target: column.zs_observe.walmart_settlement.charged_amount_excluding_tax
  fields:
    edge_family: dependency_usage
    evidence_basis: Query pattern SQL/template uses this documented column.
    confidence: high
    canonical_cognee_edge: true
    marketplace_only: true
    canonical_edge_type: USES_COLUMN
    inverse_edge_type: USED_BY_CARD
    materialize_inverse: false
    edge_class: canonical
    source_type: query_pattern
    target_type: column
    evidence_refs:
    - ev.walmart.metrics.001
    notes: Query pattern SQL/template uses this documented column.
```

```yaml
candidate_edge:
  edge_id: edge.walmart.0483
  edge_type: USES_COLUMN
  source: query_pattern.walmart.monthly_revenue
  target: column.zs_observe.walmart_settlement.gross_commission
  fields:
    edge_family: dependency_usage
    evidence_basis: Query pattern SQL/template uses this documented column.
    confidence: high
    canonical_cognee_edge: true
    marketplace_only: true
    canonical_edge_type: USES_COLUMN
    inverse_edge_type: USED_BY_CARD
    materialize_inverse: false
    edge_class: canonical
    source_type: query_pattern
    target_type: column
    evidence_refs:
    - ev.walmart.metrics.001
    notes: Query pattern SQL/template uses this documented column.
```

```yaml
candidate_edge:
  edge_id: edge.walmart.0484
  edge_type: USES_COLUMN
  source: query_pattern.walmart.monthly_revenue
  target: column.zs_observe.walmart_settlement.total_walmart_funded_savings
  fields:
    edge_family: dependency_usage
    evidence_basis: Query pattern SQL/template uses this documented column.
    confidence: high
    canonical_cognee_edge: true
    marketplace_only: true
    canonical_edge_type: USES_COLUMN
    inverse_edge_type: USED_BY_CARD
    materialize_inverse: false
    edge_class: canonical
    source_type: query_pattern
    target_type: column
    evidence_refs:
    - ev.walmart.metrics.001
    notes: Query pattern SQL/template uses this documented column.
```

```yaml
candidate_edge:
  edge_id: edge.walmart.0485
  edge_type: USES_COLUMN
  source: query_pattern.walmart.monthly_revenue
  target: column.zs_observe.walmart_settlement.transaction_type
  fields:
    edge_family: dependency_usage
    evidence_basis: Query pattern SQL/template uses this documented column.
    confidence: high
    canonical_cognee_edge: true
    marketplace_only: true
    canonical_edge_type: USES_COLUMN
    inverse_edge_type: USED_BY_CARD
    materialize_inverse: false
    edge_class: canonical
    source_type: query_pattern
    target_type: column
    evidence_refs:
    - ev.walmart.metrics.001
    notes: Query pattern SQL/template uses this documented column.
```

```yaml
candidate_edge:
  edge_id: edge.walmart.0486
  edge_type: USES_COLUMN
  source: query_pattern.walmart.monthly_revenue
  target: column.zs_observe.walmart_settlement.group_level_id
  fields:
    edge_family: dependency_usage
    evidence_basis: Query pattern SQL/template uses this documented column.
    confidence: high
    canonical_cognee_edge: true
    marketplace_only: true
    canonical_edge_type: USES_COLUMN
    inverse_edge_type: USED_BY_CARD
    materialize_inverse: false
    edge_class: canonical
    source_type: query_pattern
    target_type: column
    evidence_refs:
    - ev.walmart.metrics.001
    notes: Query pattern SQL/template uses this documented column.
```

```yaml
candidate_edge:
  edge_id: edge.walmart.0487
  edge_type: USES_COLUMN
  source: query_pattern.walmart.monthly_revenue
  target: column.zs_observe.walmart_settlement.is_active
  fields:
    edge_family: dependency_usage
    evidence_basis: Query pattern SQL/template uses this documented column.
    confidence: high
    canonical_cognee_edge: true
    marketplace_only: true
    canonical_edge_type: USES_COLUMN
    inverse_edge_type: USED_BY_CARD
    materialize_inverse: false
    edge_class: canonical
    source_type: query_pattern
    target_type: column
    evidence_refs:
    - ev.walmart.metrics.001
    notes: Query pattern SQL/template uses this documented column.
```

```yaml
candidate_edge:
  edge_id: edge.walmart.0488
  edge_type: USES_COLUMN
  source: query_pattern.walmart.top_skus
  target: column.zs_observe.walmart_settlement.sku_id
  fields:
    edge_family: dependency_usage
    evidence_basis: Query pattern SQL/template uses this documented column.
    confidence: high
    canonical_cognee_edge: true
    marketplace_only: true
    canonical_edge_type: USES_COLUMN
    inverse_edge_type: USED_BY_CARD
    materialize_inverse: false
    edge_class: canonical
    source_type: query_pattern
    target_type: column
    evidence_refs:
    - ev.walmart.metrics.001
    notes: Query pattern SQL/template uses this documented column.
```

```yaml
candidate_edge:
  edge_id: edge.walmart.0489
  edge_type: USES_COLUMN
  source: query_pattern.walmart.top_skus
  target: column.zs_observe.walmart_settlement.charged_amount
  fields:
    edge_family: dependency_usage
    evidence_basis: Query pattern SQL/template uses this documented column.
    confidence: high
    canonical_cognee_edge: true
    marketplace_only: true
    canonical_edge_type: USES_COLUMN
    inverse_edge_type: USED_BY_CARD
    materialize_inverse: false
    edge_class: canonical
    source_type: query_pattern
    target_type: column
    evidence_refs:
    - ev.walmart.metrics.001
    notes: Query pattern SQL/template uses this documented column.
```

```yaml
candidate_edge:
  edge_id: edge.walmart.0490
  edge_type: USES_COLUMN
  source: query_pattern.walmart.top_skus
  target: column.zs_observe.walmart_settlement.charged_amount_excluding_tax
  fields:
    edge_family: dependency_usage
    evidence_basis: Query pattern SQL/template uses this documented column.
    confidence: high
    canonical_cognee_edge: true
    marketplace_only: true
    canonical_edge_type: USES_COLUMN
    inverse_edge_type: USED_BY_CARD
    materialize_inverse: false
    edge_class: canonical
    source_type: query_pattern
    target_type: column
    evidence_refs:
    - ev.walmart.metrics.001
    notes: Query pattern SQL/template uses this documented column.
```

```yaml
candidate_edge:
  edge_id: edge.walmart.0491
  edge_type: USES_COLUMN
  source: query_pattern.walmart.top_skus
  target: column.zs_observe.walmart_settlement.gross_commission
  fields:
    edge_family: dependency_usage
    evidence_basis: Query pattern SQL/template uses this documented column.
    confidence: high
    canonical_cognee_edge: true
    marketplace_only: true
    canonical_edge_type: USES_COLUMN
    inverse_edge_type: USED_BY_CARD
    materialize_inverse: false
    edge_class: canonical
    source_type: query_pattern
    target_type: column
    evidence_refs:
    - ev.walmart.metrics.001
    notes: Query pattern SQL/template uses this documented column.
```

```yaml
candidate_edge:
  edge_id: edge.walmart.0492
  edge_type: USES_COLUMN
  source: query_pattern.walmart.top_skus
  target: column.zs_observe.walmart_settlement.transaction_type
  fields:
    edge_family: dependency_usage
    evidence_basis: Query pattern SQL/template uses this documented column.
    confidence: high
    canonical_cognee_edge: true
    marketplace_only: true
    canonical_edge_type: USES_COLUMN
    inverse_edge_type: USED_BY_CARD
    materialize_inverse: false
    edge_class: canonical
    source_type: query_pattern
    target_type: column
    evidence_refs:
    - ev.walmart.metrics.001
    notes: Query pattern SQL/template uses this documented column.
```

```yaml
candidate_edge:
  edge_id: edge.walmart.0493
  edge_type: USES_COLUMN
  source: query_pattern.walmart.top_skus
  target: column.zs_observe.walmart_settlement.product_type
  fields:
    edge_family: dependency_usage
    evidence_basis: Query pattern SQL/template uses this documented column.
    confidence: high
    canonical_cognee_edge: true
    marketplace_only: true
    canonical_edge_type: USES_COLUMN
    inverse_edge_type: USED_BY_CARD
    materialize_inverse: false
    edge_class: canonical
    source_type: query_pattern
    target_type: column
    evidence_refs:
    - ev.walmart.metrics.001
    notes: Query pattern SQL/template uses this documented column.
```

```yaml
candidate_edge:
  edge_id: edge.walmart.0494
  edge_type: USES_COLUMN
  source: query_pattern.walmart.top_skus
  target: column.zs_observe.walmart_settlement.group_level_id
  fields:
    edge_family: dependency_usage
    evidence_basis: Query pattern SQL/template uses this documented column.
    confidence: high
    canonical_cognee_edge: true
    marketplace_only: true
    canonical_edge_type: USES_COLUMN
    inverse_edge_type: USED_BY_CARD
    materialize_inverse: false
    edge_class: canonical
    source_type: query_pattern
    target_type: column
    evidence_refs:
    - ev.walmart.metrics.001
    notes: Query pattern SQL/template uses this documented column.
```

```yaml
candidate_edge:
  edge_id: edge.walmart.0495
  edge_type: USES_COLUMN
  source: query_pattern.walmart.top_skus
  target: column.zs_observe.walmart_settlement.is_active
  fields:
    edge_family: dependency_usage
    evidence_basis: Query pattern SQL/template uses this documented column.
    confidence: high
    canonical_cognee_edge: true
    marketplace_only: true
    canonical_edge_type: USES_COLUMN
    inverse_edge_type: USED_BY_CARD
    materialize_inverse: false
    edge_class: canonical
    source_type: query_pattern
    target_type: column
    evidence_refs:
    - ev.walmart.metrics.001
    notes: Query pattern SQL/template uses this documented column.
```

```yaml
candidate_edge:
  edge_id: edge.walmart.0496
  edge_type: USES_COLUMN
  source: query_pattern.walmart.top_skus
  target: column.zs_observe.walmart_lookup.sku_id
  fields:
    edge_family: dependency_usage
    evidence_basis: Query pattern SQL/template uses this documented column.
    confidence: high
    canonical_cognee_edge: true
    marketplace_only: true
    canonical_edge_type: USES_COLUMN
    inverse_edge_type: USED_BY_CARD
    materialize_inverse: false
    edge_class: canonical
    source_type: query_pattern
    target_type: column
    evidence_refs:
    - ev.walmart.metrics.001
    notes: Query pattern SQL/template uses this documented column.
```

```yaml
candidate_edge:
  edge_id: edge.walmart.0497
  edge_type: USES_COLUMN
  source: query_pattern.walmart.top_skus
  target: column.zs_observe.walmart_lookup.sku
  fields:
    edge_family: dependency_usage
    evidence_basis: Query pattern SQL/template uses this documented column.
    confidence: high
    canonical_cognee_edge: true
    marketplace_only: true
    canonical_edge_type: USES_COLUMN
    inverse_edge_type: USED_BY_CARD
    materialize_inverse: false
    edge_class: canonical
    source_type: query_pattern
    target_type: column
    evidence_refs:
    - ev.walmart.metrics.001
    notes: Query pattern SQL/template uses this documented column.
```

```yaml
candidate_edge:
  edge_id: edge.walmart.0498
  edge_type: USES_COLUMN
  source: query_pattern.walmart.top_skus
  target: column.zs_observe.walmart_lookup.item_name
  fields:
    edge_family: dependency_usage
    evidence_basis: Query pattern SQL/template uses this documented column.
    confidence: high
    canonical_cognee_edge: true
    marketplace_only: true
    canonical_edge_type: USES_COLUMN
    inverse_edge_type: USED_BY_CARD
    materialize_inverse: false
    edge_class: canonical
    source_type: query_pattern
    target_type: column
    evidence_refs:
    - ev.walmart.metrics.001
    notes: Query pattern SQL/template uses this documented column.
```

```yaml
candidate_edge:
  edge_id: edge.walmart.0499
  edge_type: USES_COLUMN
  source: query_pattern.walmart.top_skus
  target: column.zs_observe.walmart_lookup.group_level_id
  fields:
    edge_family: dependency_usage
    evidence_basis: Query pattern SQL/template uses this documented column.
    confidence: high
    canonical_cognee_edge: true
    marketplace_only: true
    canonical_edge_type: USES_COLUMN
    inverse_edge_type: USED_BY_CARD
    materialize_inverse: false
    edge_class: canonical
    source_type: query_pattern
    target_type: column
    evidence_refs:
    - ev.walmart.metrics.001
    notes: Query pattern SQL/template uses this documented column.
```

```yaml
candidate_edge:
  edge_id: edge.walmart.0500
  edge_type: USES_COLUMN
  source: query_pattern.walmart.top_skus
  target: column.zs_observe.walmart_lookup.is_active
  fields:
    edge_family: dependency_usage
    evidence_basis: Query pattern SQL/template uses this documented column.
    confidence: high
    canonical_cognee_edge: true
    marketplace_only: true
    canonical_edge_type: USES_COLUMN
    inverse_edge_type: USED_BY_CARD
    materialize_inverse: false
    edge_class: canonical
    source_type: query_pattern
    target_type: column
    evidence_refs:
    - ev.walmart.metrics.001
    notes: Query pattern SQL/template uses this documented column.
```

```yaml
candidate_edge:
  edge_id: edge.walmart.0501
  edge_type: USES_COLUMN
  source: query_pattern.walmart.state_distribution
  target: column.zs_observe.walmart_oms.charged_amount
  fields:
    edge_family: dependency_usage
    evidence_basis: Query pattern SQL/template uses this documented column.
    confidence: high
    canonical_cognee_edge: true
    marketplace_only: true
    canonical_edge_type: USES_COLUMN
    inverse_edge_type: USED_BY_CARD
    materialize_inverse: false
    edge_class: canonical
    source_type: query_pattern
    target_type: column
    evidence_refs:
    - ev.walmart.metrics.001
    notes: Query pattern SQL/template uses this documented column.
```

```yaml
candidate_edge:
  edge_id: edge.walmart.0502
  edge_type: USES_COLUMN
  source: query_pattern.walmart.state_distribution
  target: column.zs_observe.walmart_oms.order_status
  fields:
    edge_family: dependency_usage
    evidence_basis: Query pattern SQL/template uses this documented column.
    confidence: high
    canonical_cognee_edge: true
    marketplace_only: true
    canonical_edge_type: USES_COLUMN
    inverse_edge_type: USED_BY_CARD
    materialize_inverse: false
    edge_class: canonical
    source_type: query_pattern
    target_type: column
    evidence_refs:
    - ev.walmart.metrics.001
    notes: Query pattern SQL/template uses this documented column.
```

```yaml
candidate_edge:
  edge_id: edge.walmart.0503
  edge_type: USES_COLUMN
  source: query_pattern.walmart.state_distribution
  target: column.zs_observe.walmart_oms.destination_state
  fields:
    edge_family: dependency_usage
    evidence_basis: Query pattern SQL/template uses this documented column.
    confidence: high
    canonical_cognee_edge: true
    marketplace_only: true
    canonical_edge_type: USES_COLUMN
    inverse_edge_type: USED_BY_CARD
    materialize_inverse: false
    edge_class: canonical
    source_type: query_pattern
    target_type: column
    evidence_refs:
    - ev.walmart.metrics.001
    notes: Query pattern SQL/template uses this documented column.
```

```yaml
candidate_edge:
  edge_id: edge.walmart.0504
  edge_type: USES_COLUMN
  source: query_pattern.walmart.state_distribution
  target: column.zs_observe.walmart_oms.group_level_id
  fields:
    edge_family: dependency_usage
    evidence_basis: Query pattern SQL/template uses this documented column.
    confidence: high
    canonical_cognee_edge: true
    marketplace_only: true
    canonical_edge_type: USES_COLUMN
    inverse_edge_type: USED_BY_CARD
    materialize_inverse: false
    edge_class: canonical
    source_type: query_pattern
    target_type: column
    evidence_refs:
    - ev.walmart.metrics.001
    notes: Query pattern SQL/template uses this documented column.
```

```yaml
candidate_edge:
  edge_id: edge.walmart.0505
  edge_type: USES_COLUMN
  source: query_pattern.walmart.state_distribution
  target: column.zs_observe.walmart_oms.is_active
  fields:
    edge_family: dependency_usage
    evidence_basis: Query pattern SQL/template uses this documented column.
    confidence: high
    canonical_cognee_edge: true
    marketplace_only: true
    canonical_edge_type: USES_COLUMN
    inverse_edge_type: USED_BY_CARD
    materialize_inverse: false
    edge_class: canonical
    source_type: query_pattern
    target_type: column
    evidence_refs:
    - ev.walmart.metrics.001
    notes: Query pattern SQL/template uses this documented column.
```

```yaml
candidate_edge:
  edge_id: edge.walmart.0506
  edge_type: USES_COLUMN
  source: query_pattern.walmart.payout_cycle
  target: column.zs_observe.walmart_settlement.order_id
  fields:
    edge_family: dependency_usage
    evidence_basis: Query pattern SQL/template uses this documented column.
    confidence: high
    canonical_cognee_edge: true
    marketplace_only: true
    canonical_edge_type: USES_COLUMN
    inverse_edge_type: USED_BY_CARD
    materialize_inverse: false
    edge_class: canonical
    source_type: query_pattern
    target_type: column
    evidence_refs:
    - ev.walmart.metrics.001
    notes: Query pattern SQL/template uses this documented column.
```

```yaml
candidate_edge:
  edge_id: edge.walmart.0507
  edge_type: USES_COLUMN
  source: query_pattern.walmart.payout_cycle
  target: column.zs_observe.walmart_settlement.metadata_2
  fields:
    edge_family: dependency_usage
    evidence_basis: Query pattern SQL/template uses this documented column.
    confidence: high
    canonical_cognee_edge: true
    marketplace_only: true
    canonical_edge_type: USES_COLUMN
    inverse_edge_type: USED_BY_CARD
    materialize_inverse: false
    edge_class: canonical
    source_type: query_pattern
    target_type: column
    evidence_refs:
    - ev.walmart.metrics.001
    notes: Query pattern SQL/template uses this documented column.
```

```yaml
candidate_edge:
  edge_id: edge.walmart.0508
  edge_type: USES_COLUMN
  source: query_pattern.walmart.payout_cycle
  target: column.zs_observe.walmart_settlement.metadata_3
  fields:
    edge_family: dependency_usage
    evidence_basis: Query pattern SQL/template uses this documented column.
    confidence: high
    canonical_cognee_edge: true
    marketplace_only: true
    canonical_edge_type: USES_COLUMN
    inverse_edge_type: USED_BY_CARD
    materialize_inverse: false
    edge_class: canonical
    source_type: query_pattern
    target_type: column
    evidence_refs:
    - ev.walmart.metrics.001
    notes: Query pattern SQL/template uses this documented column.
```

```yaml
candidate_edge:
  edge_id: edge.walmart.0509
  edge_type: USES_COLUMN
  source: query_pattern.walmart.payout_cycle
  target: column.zs_observe.walmart_settlement.charged_amount_excluding_tax
  fields:
    edge_family: dependency_usage
    evidence_basis: Query pattern SQL/template uses this documented column.
    confidence: high
    canonical_cognee_edge: true
    marketplace_only: true
    canonical_edge_type: USES_COLUMN
    inverse_edge_type: USED_BY_CARD
    materialize_inverse: false
    edge_class: canonical
    source_type: query_pattern
    target_type: column
    evidence_refs:
    - ev.walmart.metrics.001
    notes: Query pattern SQL/template uses this documented column.
```

```yaml
candidate_edge:
  edge_id: edge.walmart.0510
  edge_type: USES_COLUMN
  source: query_pattern.walmart.payout_cycle
  target: column.zs_observe.walmart_settlement.gross_commission
  fields:
    edge_family: dependency_usage
    evidence_basis: Query pattern SQL/template uses this documented column.
    confidence: high
    canonical_cognee_edge: true
    marketplace_only: true
    canonical_edge_type: USES_COLUMN
    inverse_edge_type: USED_BY_CARD
    materialize_inverse: false
    edge_class: canonical
    source_type: query_pattern
    target_type: column
    evidence_refs:
    - ev.walmart.metrics.001
    notes: Query pattern SQL/template uses this documented column.
```

```yaml
candidate_edge:
  edge_id: edge.walmart.0511
  edge_type: USES_COLUMN
  source: query_pattern.walmart.payout_cycle
  target: column.zs_observe.walmart_settlement.total_walmart_funded_savings
  fields:
    edge_family: dependency_usage
    evidence_basis: Query pattern SQL/template uses this documented column.
    confidence: high
    canonical_cognee_edge: true
    marketplace_only: true
    canonical_edge_type: USES_COLUMN
    inverse_edge_type: USED_BY_CARD
    materialize_inverse: false
    edge_class: canonical
    source_type: query_pattern
    target_type: column
    evidence_refs:
    - ev.walmart.metrics.001
    notes: Query pattern SQL/template uses this documented column.
```

```yaml
candidate_edge:
  edge_id: edge.walmart.0512
  edge_type: USES_COLUMN
  source: query_pattern.walmart.payout_cycle
  target: column.zs_observe.walmart_settlement.transaction_type
  fields:
    edge_family: dependency_usage
    evidence_basis: Query pattern SQL/template uses this documented column.
    confidence: high
    canonical_cognee_edge: true
    marketplace_only: true
    canonical_edge_type: USES_COLUMN
    inverse_edge_type: USED_BY_CARD
    materialize_inverse: false
    edge_class: canonical
    source_type: query_pattern
    target_type: column
    evidence_refs:
    - ev.walmart.metrics.001
    notes: Query pattern SQL/template uses this documented column.
```

```yaml
candidate_edge:
  edge_id: edge.walmart.0513
  edge_type: USES_COLUMN
  source: query_pattern.walmart.payout_cycle
  target: column.zs_observe.walmart_settlement.group_level_id
  fields:
    edge_family: dependency_usage
    evidence_basis: Query pattern SQL/template uses this documented column.
    confidence: high
    canonical_cognee_edge: true
    marketplace_only: true
    canonical_edge_type: USES_COLUMN
    inverse_edge_type: USED_BY_CARD
    materialize_inverse: false
    edge_class: canonical
    source_type: query_pattern
    target_type: column
    evidence_refs:
    - ev.walmart.metrics.001
    notes: Query pattern SQL/template uses this documented column.
```

```yaml
candidate_edge:
  edge_id: edge.walmart.0514
  edge_type: USES_COLUMN
  source: query_pattern.walmart.payout_cycle
  target: column.zs_observe.walmart_settlement.is_active
  fields:
    edge_family: dependency_usage
    evidence_basis: Query pattern SQL/template uses this documented column.
    confidence: high
    canonical_cognee_edge: true
    marketplace_only: true
    canonical_edge_type: USES_COLUMN
    inverse_edge_type: USED_BY_CARD
    materialize_inverse: false
    edge_class: canonical
    source_type: query_pattern
    target_type: column
    evidence_refs:
    - ev.walmart.metrics.001
    notes: Query pattern SQL/template uses this documented column.
```

```yaml
candidate_edge:
  edge_id: edge.walmart.0515
  edge_type: USES_COLUMN
  source: query_pattern.walmart.oms_settlement_reconciliation
  target: column.zs_observe.walmart_oms.order_id
  fields:
    edge_family: dependency_usage
    evidence_basis: Query pattern SQL/template uses this documented column.
    confidence: high
    canonical_cognee_edge: true
    marketplace_only: true
    canonical_edge_type: USES_COLUMN
    inverse_edge_type: USED_BY_CARD
    materialize_inverse: false
    edge_class: canonical
    source_type: query_pattern
    target_type: column
    evidence_refs:
    - ev.walmart.reconciliation.001
    notes: Query pattern SQL/template uses this documented column.
```

```yaml
candidate_edge:
  edge_id: edge.walmart.0516
  edge_type: USES_COLUMN
  source: query_pattern.walmart.oms_settlement_reconciliation
  target: column.zs_observe.walmart_oms.sku_id
  fields:
    edge_family: dependency_usage
    evidence_basis: Query pattern SQL/template uses this documented column.
    confidence: high
    canonical_cognee_edge: true
    marketplace_only: true
    canonical_edge_type: USES_COLUMN
    inverse_edge_type: USED_BY_CARD
    materialize_inverse: false
    edge_class: canonical
    source_type: query_pattern
    target_type: column
    evidence_refs:
    - ev.walmart.reconciliation.001
    notes: Query pattern SQL/template uses this documented column.
```

```yaml
candidate_edge:
  edge_id: edge.walmart.0517
  edge_type: USES_COLUMN
  source: query_pattern.walmart.oms_settlement_reconciliation
  target: column.zs_observe.walmart_oms.created_date
  fields:
    edge_family: dependency_usage
    evidence_basis: Query pattern SQL/template uses this documented column.
    confidence: high
    canonical_cognee_edge: true
    marketplace_only: true
    canonical_edge_type: USES_COLUMN
    inverse_edge_type: USED_BY_CARD
    materialize_inverse: false
    edge_class: canonical
    source_type: query_pattern
    target_type: column
    evidence_refs:
    - ev.walmart.reconciliation.001
    notes: Query pattern SQL/template uses this documented column.
```

```yaml
candidate_edge:
  edge_id: edge.walmart.0518
  edge_type: USES_COLUMN
  source: query_pattern.walmart.oms_settlement_reconciliation
  target: column.zs_observe.walmart_oms.charged_amount
  fields:
    edge_family: dependency_usage
    evidence_basis: Query pattern SQL/template uses this documented column.
    confidence: high
    canonical_cognee_edge: true
    marketplace_only: true
    canonical_edge_type: USES_COLUMN
    inverse_edge_type: USED_BY_CARD
    materialize_inverse: false
    edge_class: canonical
    source_type: query_pattern
    target_type: column
    evidence_refs:
    - ev.walmart.reconciliation.001
    notes: Query pattern SQL/template uses this documented column.
```

```yaml
candidate_edge:
  edge_id: edge.walmart.0519
  edge_type: USES_COLUMN
  source: query_pattern.walmart.oms_settlement_reconciliation
  target: column.zs_observe.walmart_oms.internal_txn_type
  fields:
    edge_family: dependency_usage
    evidence_basis: Query pattern SQL/template uses this documented column.
    confidence: high
    canonical_cognee_edge: true
    marketplace_only: true
    canonical_edge_type: USES_COLUMN
    inverse_edge_type: USED_BY_CARD
    materialize_inverse: false
    edge_class: canonical
    source_type: query_pattern
    target_type: column
    evidence_refs:
    - ev.walmart.reconciliation.001
    notes: Query pattern SQL/template uses this documented column.
```

```yaml
candidate_edge:
  edge_id: edge.walmart.0520
  edge_type: USES_COLUMN
  source: query_pattern.walmart.oms_settlement_reconciliation
  target: column.zs_observe.walmart_oms.order_status
  fields:
    edge_family: dependency_usage
    evidence_basis: Query pattern SQL/template uses this documented column.
    confidence: high
    canonical_cognee_edge: true
    marketplace_only: true
    canonical_edge_type: USES_COLUMN
    inverse_edge_type: USED_BY_CARD
    materialize_inverse: false
    edge_class: canonical
    source_type: query_pattern
    target_type: column
    evidence_refs:
    - ev.walmart.reconciliation.001
    notes: Query pattern SQL/template uses this documented column.
```

```yaml
candidate_edge:
  edge_id: edge.walmart.0521
  edge_type: USES_COLUMN
  source: query_pattern.walmart.oms_settlement_reconciliation
  target: column.zs_observe.walmart_oms.group_level_id
  fields:
    edge_family: dependency_usage
    evidence_basis: Query pattern SQL/template uses this documented column.
    confidence: high
    canonical_cognee_edge: true
    marketplace_only: true
    canonical_edge_type: USES_COLUMN
    inverse_edge_type: USED_BY_CARD
    materialize_inverse: false
    edge_class: canonical
    source_type: query_pattern
    target_type: column
    evidence_refs:
    - ev.walmart.reconciliation.001
    notes: Query pattern SQL/template uses this documented column.
```

```yaml
candidate_edge:
  edge_id: edge.walmart.0522
  edge_type: USES_COLUMN
  source: query_pattern.walmart.oms_settlement_reconciliation
  target: column.zs_observe.walmart_oms.is_active
  fields:
    edge_family: dependency_usage
    evidence_basis: Query pattern SQL/template uses this documented column.
    confidence: high
    canonical_cognee_edge: true
    marketplace_only: true
    canonical_edge_type: USES_COLUMN
    inverse_edge_type: USED_BY_CARD
    materialize_inverse: false
    edge_class: canonical
    source_type: query_pattern
    target_type: column
    evidence_refs:
    - ev.walmart.reconciliation.001
    notes: Query pattern SQL/template uses this documented column.
```

```yaml
candidate_edge:
  edge_id: edge.walmart.0523
  edge_type: USES_COLUMN
  source: query_pattern.walmart.oms_settlement_reconciliation
  target: column.zs_observe.walmart_settlement.order_id
  fields:
    edge_family: dependency_usage
    evidence_basis: Query pattern SQL/template uses this documented column.
    confidence: high
    canonical_cognee_edge: true
    marketplace_only: true
    canonical_edge_type: USES_COLUMN
    inverse_edge_type: USED_BY_CARD
    materialize_inverse: false
    edge_class: canonical
    source_type: query_pattern
    target_type: column
    evidence_refs:
    - ev.walmart.reconciliation.001
    notes: Query pattern SQL/template uses this documented column.
```

```yaml
candidate_edge:
  edge_id: edge.walmart.0524
  edge_type: USES_COLUMN
  source: query_pattern.walmart.oms_settlement_reconciliation
  target: column.zs_observe.walmart_settlement.sku_id
  fields:
    edge_family: dependency_usage
    evidence_basis: Query pattern SQL/template uses this documented column.
    confidence: high
    canonical_cognee_edge: true
    marketplace_only: true
    canonical_edge_type: USES_COLUMN
    inverse_edge_type: USED_BY_CARD
    materialize_inverse: false
    edge_class: canonical
    source_type: query_pattern
    target_type: column
    evidence_refs:
    - ev.walmart.reconciliation.001
    notes: Query pattern SQL/template uses this documented column.
```

```yaml
candidate_edge:
  edge_id: edge.walmart.0525
  edge_type: USES_COLUMN
  source: query_pattern.walmart.oms_settlement_reconciliation
  target: column.zs_observe.walmart_settlement.created_date
  fields:
    edge_family: dependency_usage
    evidence_basis: Query pattern SQL/template uses this documented column.
    confidence: high
    canonical_cognee_edge: true
    marketplace_only: true
    canonical_edge_type: USES_COLUMN
    inverse_edge_type: USED_BY_CARD
    materialize_inverse: false
    edge_class: canonical
    source_type: query_pattern
    target_type: column
    evidence_refs:
    - ev.walmart.reconciliation.001
    notes: Query pattern SQL/template uses this documented column.
```

```yaml
candidate_edge:
  edge_id: edge.walmart.0526
  edge_type: USES_COLUMN
  source: query_pattern.walmart.oms_settlement_reconciliation
  target: column.zs_observe.walmart_settlement.charged_amount
  fields:
    edge_family: dependency_usage
    evidence_basis: Query pattern SQL/template uses this documented column.
    confidence: high
    canonical_cognee_edge: true
    marketplace_only: true
    canonical_edge_type: USES_COLUMN
    inverse_edge_type: USED_BY_CARD
    materialize_inverse: false
    edge_class: canonical
    source_type: query_pattern
    target_type: column
    evidence_refs:
    - ev.walmart.reconciliation.001
    notes: Query pattern SQL/template uses this documented column.
```

```yaml
candidate_edge:
  edge_id: edge.walmart.0527
  edge_type: USES_COLUMN
  source: query_pattern.walmart.oms_settlement_reconciliation
  target: column.zs_observe.walmart_settlement.charged_amount_excluding_tax
  fields:
    edge_family: dependency_usage
    evidence_basis: Query pattern SQL/template uses this documented column.
    confidence: high
    canonical_cognee_edge: true
    marketplace_only: true
    canonical_edge_type: USES_COLUMN
    inverse_edge_type: USED_BY_CARD
    materialize_inverse: false
    edge_class: canonical
    source_type: query_pattern
    target_type: column
    evidence_refs:
    - ev.walmart.reconciliation.001
    notes: Query pattern SQL/template uses this documented column.
```

```yaml
candidate_edge:
  edge_id: edge.walmart.0528
  edge_type: USES_COLUMN
  source: query_pattern.walmart.oms_settlement_reconciliation
  target: column.zs_observe.walmart_settlement.total_tax
  fields:
    edge_family: dependency_usage
    evidence_basis: Query pattern SQL/template uses this documented column.
    confidence: high
    canonical_cognee_edge: true
    marketplace_only: true
    canonical_edge_type: USES_COLUMN
    inverse_edge_type: USED_BY_CARD
    materialize_inverse: false
    edge_class: canonical
    source_type: query_pattern
    target_type: column
    evidence_refs:
    - ev.walmart.reconciliation.001
    notes: Query pattern SQL/template uses this documented column.
```

```yaml
candidate_edge:
  edge_id: edge.walmart.0529
  edge_type: USES_COLUMN
  source: query_pattern.walmart.oms_settlement_reconciliation
  target: column.zs_observe.walmart_settlement.gross_commission
  fields:
    edge_family: dependency_usage
    evidence_basis: Query pattern SQL/template uses this documented column.
    confidence: high
    canonical_cognee_edge: true
    marketplace_only: true
    canonical_edge_type: USES_COLUMN
    inverse_edge_type: USED_BY_CARD
    materialize_inverse: false
    edge_class: canonical
    source_type: query_pattern
    target_type: column
    evidence_refs:
    - ev.walmart.reconciliation.001
    notes: Query pattern SQL/template uses this documented column.
```

```yaml
candidate_edge:
  edge_id: edge.walmart.0530
  edge_type: USES_COLUMN
  source: query_pattern.walmart.oms_settlement_reconciliation
  target: column.zs_observe.walmart_settlement.marketplace_withheld_tax
  fields:
    edge_family: dependency_usage
    evidence_basis: Query pattern SQL/template uses this documented column.
    confidence: high
    canonical_cognee_edge: true
    marketplace_only: true
    canonical_edge_type: USES_COLUMN
    inverse_edge_type: USED_BY_CARD
    materialize_inverse: false
    edge_class: canonical
    source_type: query_pattern
    target_type: column
    evidence_refs:
    - ev.walmart.reconciliation.001
    notes: Query pattern SQL/template uses this documented column.
```

```yaml
candidate_edge:
  edge_id: edge.walmart.0531
  edge_type: USES_COLUMN
  source: query_pattern.walmart.oms_settlement_reconciliation
  target: column.zs_observe.walmart_settlement.transaction_type
  fields:
    edge_family: dependency_usage
    evidence_basis: Query pattern SQL/template uses this documented column.
    confidence: high
    canonical_cognee_edge: true
    marketplace_only: true
    canonical_edge_type: USES_COLUMN
    inverse_edge_type: USED_BY_CARD
    materialize_inverse: false
    edge_class: canonical
    source_type: query_pattern
    target_type: column
    evidence_refs:
    - ev.walmart.reconciliation.001
    notes: Query pattern SQL/template uses this documented column.
```

```yaml
candidate_edge:
  edge_id: edge.walmart.0532
  edge_type: USES_COLUMN
  source: query_pattern.walmart.oms_settlement_reconciliation
  target: column.zs_observe.walmart_settlement.internal_txn_type
  fields:
    edge_family: dependency_usage
    evidence_basis: Query pattern SQL/template uses this documented column.
    confidence: high
    canonical_cognee_edge: true
    marketplace_only: true
    canonical_edge_type: USES_COLUMN
    inverse_edge_type: USED_BY_CARD
    materialize_inverse: false
    edge_class: canonical
    source_type: query_pattern
    target_type: column
    evidence_refs:
    - ev.walmart.reconciliation.001
    notes: Query pattern SQL/template uses this documented column.
```

```yaml
candidate_edge:
  edge_id: edge.walmart.0533
  edge_type: USES_COLUMN
  source: query_pattern.walmart.oms_settlement_reconciliation
  target: column.zs_observe.walmart_settlement.group_level_id
  fields:
    edge_family: dependency_usage
    evidence_basis: Query pattern SQL/template uses this documented column.
    confidence: high
    canonical_cognee_edge: true
    marketplace_only: true
    canonical_edge_type: USES_COLUMN
    inverse_edge_type: USED_BY_CARD
    materialize_inverse: false
    edge_class: canonical
    source_type: query_pattern
    target_type: column
    evidence_refs:
    - ev.walmart.reconciliation.001
    notes: Query pattern SQL/template uses this documented column.
```

```yaml
candidate_edge:
  edge_id: edge.walmart.0534
  edge_type: USES_COLUMN
  source: query_pattern.walmart.oms_settlement_reconciliation
  target: column.zs_observe.walmart_settlement.is_active
  fields:
    edge_family: dependency_usage
    evidence_basis: Query pattern SQL/template uses this documented column.
    confidence: high
    canonical_cognee_edge: true
    marketplace_only: true
    canonical_edge_type: USES_COLUMN
    inverse_edge_type: USED_BY_CARD
    materialize_inverse: false
    edge_class: canonical
    source_type: query_pattern
    target_type: column
    evidence_refs:
    - ev.walmart.reconciliation.001
    notes: Query pattern SQL/template uses this documented column.
```

```yaml
candidate_edge:
  edge_id: edge.walmart.0535
  edge_type: USES_COLUMN
  source: query_pattern.walmart.commission_validation
  target: column.zs_observe.walmart_settlement.order_id
  fields:
    edge_family: dependency_usage
    evidence_basis: Query pattern SQL/template uses this documented column.
    confidence: high
    canonical_cognee_edge: true
    marketplace_only: true
    canonical_edge_type: USES_COLUMN
    inverse_edge_type: USED_BY_CARD
    materialize_inverse: false
    edge_class: canonical
    source_type: query_pattern
    target_type: column
    evidence_refs:
    - ev.walmart.reconciliation.001
    notes: Query pattern SQL/template uses this documented column.
```

```yaml
candidate_edge:
  edge_id: edge.walmart.0536
  edge_type: USES_COLUMN
  source: query_pattern.walmart.commission_validation
  target: column.zs_observe.walmart_settlement.sku_id
  fields:
    edge_family: dependency_usage
    evidence_basis: Query pattern SQL/template uses this documented column.
    confidence: high
    canonical_cognee_edge: true
    marketplace_only: true
    canonical_edge_type: USES_COLUMN
    inverse_edge_type: USED_BY_CARD
    materialize_inverse: false
    edge_class: canonical
    source_type: query_pattern
    target_type: column
    evidence_refs:
    - ev.walmart.reconciliation.001
    notes: Query pattern SQL/template uses this documented column.
```

```yaml
candidate_edge:
  edge_id: edge.walmart.0537
  edge_type: USES_COLUMN
  source: query_pattern.walmart.commission_validation
  target: column.zs_observe.walmart_settlement.charged_amount_excluding_tax
  fields:
    edge_family: dependency_usage
    evidence_basis: Query pattern SQL/template uses this documented column.
    confidence: high
    canonical_cognee_edge: true
    marketplace_only: true
    canonical_edge_type: USES_COLUMN
    inverse_edge_type: USED_BY_CARD
    materialize_inverse: false
    edge_class: canonical
    source_type: query_pattern
    target_type: column
    evidence_refs:
    - ev.walmart.reconciliation.001
    notes: Query pattern SQL/template uses this documented column.
```

```yaml
candidate_edge:
  edge_id: edge.walmart.0538
  edge_type: USES_COLUMN
  source: query_pattern.walmart.commission_validation
  target: column.zs_observe.walmart_settlement.gross_commission
  fields:
    edge_family: dependency_usage
    evidence_basis: Query pattern SQL/template uses this documented column.
    confidence: high
    canonical_cognee_edge: true
    marketplace_only: true
    canonical_edge_type: USES_COLUMN
    inverse_edge_type: USED_BY_CARD
    materialize_inverse: false
    edge_class: canonical
    source_type: query_pattern
    target_type: column
    evidence_refs:
    - ev.walmart.reconciliation.001
    notes: Query pattern SQL/template uses this documented column.
```

```yaml
candidate_edge:
  edge_id: edge.walmart.0539
  edge_type: USES_COLUMN
  source: query_pattern.walmart.commission_validation
  target: column.zs_observe.walmart_settlement.product_price
  fields:
    edge_family: dependency_usage
    evidence_basis: Query pattern SQL/template uses this documented column.
    confidence: high
    canonical_cognee_edge: true
    marketplace_only: true
    canonical_edge_type: USES_COLUMN
    inverse_edge_type: USED_BY_CARD
    materialize_inverse: false
    edge_class: canonical
    source_type: query_pattern
    target_type: column
    evidence_refs:
    - ev.walmart.reconciliation.001
    notes: Query pattern SQL/template uses this documented column.
```

```yaml
candidate_edge:
  edge_id: edge.walmart.0540
  edge_type: USES_COLUMN
  source: query_pattern.walmart.commission_validation
  target: column.zs_observe.walmart_settlement.transaction_type
  fields:
    edge_family: dependency_usage
    evidence_basis: Query pattern SQL/template uses this documented column.
    confidence: high
    canonical_cognee_edge: true
    marketplace_only: true
    canonical_edge_type: USES_COLUMN
    inverse_edge_type: USED_BY_CARD
    materialize_inverse: false
    edge_class: canonical
    source_type: query_pattern
    target_type: column
    evidence_refs:
    - ev.walmart.reconciliation.001
    notes: Query pattern SQL/template uses this documented column.
```

```yaml
candidate_edge:
  edge_id: edge.walmart.0541
  edge_type: USES_COLUMN
  source: query_pattern.walmart.commission_validation
  target: column.zs_observe.walmart_settlement.group_level_id
  fields:
    edge_family: dependency_usage
    evidence_basis: Query pattern SQL/template uses this documented column.
    confidence: high
    canonical_cognee_edge: true
    marketplace_only: true
    canonical_edge_type: USES_COLUMN
    inverse_edge_type: USED_BY_CARD
    materialize_inverse: false
    edge_class: canonical
    source_type: query_pattern
    target_type: column
    evidence_refs:
    - ev.walmart.reconciliation.001
    notes: Query pattern SQL/template uses this documented column.
```

```yaml
candidate_edge:
  edge_id: edge.walmart.0542
  edge_type: USES_COLUMN
  source: query_pattern.walmart.commission_validation
  target: column.zs_observe.walmart_settlement.is_active
  fields:
    edge_family: dependency_usage
    evidence_basis: Query pattern SQL/template uses this documented column.
    confidence: high
    canonical_cognee_edge: true
    marketplace_only: true
    canonical_edge_type: USES_COLUMN
    inverse_edge_type: USED_BY_CARD
    materialize_inverse: false
    edge_class: canonical
    source_type: query_pattern
    target_type: column
    evidence_refs:
    - ev.walmart.reconciliation.001
    notes: Query pattern SQL/template uses this documented column.
```

```yaml
candidate_edge:
  edge_id: edge.walmart.0543
  edge_type: USES_COLUMN
  source: query_pattern.walmart.refund_sale_match
  target: column.zs_observe.walmart_settlement.order_id
  fields:
    edge_family: dependency_usage
    evidence_basis: Query pattern SQL/template uses this documented column.
    confidence: high
    canonical_cognee_edge: true
    marketplace_only: true
    canonical_edge_type: USES_COLUMN
    inverse_edge_type: USED_BY_CARD
    materialize_inverse: false
    edge_class: canonical
    source_type: query_pattern
    target_type: column
    evidence_refs:
    - ev.walmart.reconciliation.001
    notes: Query pattern SQL/template uses this documented column.
```

```yaml
candidate_edge:
  edge_id: edge.walmart.0544
  edge_type: USES_COLUMN
  source: query_pattern.walmart.refund_sale_match
  target: column.zs_observe.walmart_settlement.sku_id
  fields:
    edge_family: dependency_usage
    evidence_basis: Query pattern SQL/template uses this documented column.
    confidence: high
    canonical_cognee_edge: true
    marketplace_only: true
    canonical_edge_type: USES_COLUMN
    inverse_edge_type: USED_BY_CARD
    materialize_inverse: false
    edge_class: canonical
    source_type: query_pattern
    target_type: column
    evidence_refs:
    - ev.walmart.reconciliation.001
    notes: Query pattern SQL/template uses this documented column.
```

```yaml
candidate_edge:
  edge_id: edge.walmart.0545
  edge_type: USES_COLUMN
  source: query_pattern.walmart.refund_sale_match
  target: column.zs_observe.walmart_settlement.charged_amount
  fields:
    edge_family: dependency_usage
    evidence_basis: Query pattern SQL/template uses this documented column.
    confidence: high
    canonical_cognee_edge: true
    marketplace_only: true
    canonical_edge_type: USES_COLUMN
    inverse_edge_type: USED_BY_CARD
    materialize_inverse: false
    edge_class: canonical
    source_type: query_pattern
    target_type: column
    evidence_refs:
    - ev.walmart.reconciliation.001
    notes: Query pattern SQL/template uses this documented column.
```

```yaml
candidate_edge:
  edge_id: edge.walmart.0546
  edge_type: USES_COLUMN
  source: query_pattern.walmart.refund_sale_match
  target: column.zs_observe.walmart_settlement.gross_commission
  fields:
    edge_family: dependency_usage
    evidence_basis: Query pattern SQL/template uses this documented column.
    confidence: high
    canonical_cognee_edge: true
    marketplace_only: true
    canonical_edge_type: USES_COLUMN
    inverse_edge_type: USED_BY_CARD
    materialize_inverse: false
    edge_class: canonical
    source_type: query_pattern
    target_type: column
    evidence_refs:
    - ev.walmart.reconciliation.001
    notes: Query pattern SQL/template uses this documented column.
```

```yaml
candidate_edge:
  edge_id: edge.walmart.0547
  edge_type: USES_COLUMN
  source: query_pattern.walmart.refund_sale_match
  target: column.zs_observe.walmart_settlement.transaction_type
  fields:
    edge_family: dependency_usage
    evidence_basis: Query pattern SQL/template uses this documented column.
    confidence: high
    canonical_cognee_edge: true
    marketplace_only: true
    canonical_edge_type: USES_COLUMN
    inverse_edge_type: USED_BY_CARD
    materialize_inverse: false
    edge_class: canonical
    source_type: query_pattern
    target_type: column
    evidence_refs:
    - ev.walmart.reconciliation.001
    notes: Query pattern SQL/template uses this documented column.
```

```yaml
candidate_edge:
  edge_id: edge.walmart.0548
  edge_type: USES_COLUMN
  source: query_pattern.walmart.refund_sale_match
  target: column.zs_observe.walmart_settlement.original_commission
  fields:
    edge_family: dependency_usage
    evidence_basis: Query pattern SQL/template uses this documented column.
    confidence: high
    canonical_cognee_edge: true
    marketplace_only: true
    canonical_edge_type: USES_COLUMN
    inverse_edge_type: USED_BY_CARD
    materialize_inverse: false
    edge_class: canonical
    source_type: query_pattern
    target_type: column
    evidence_refs:
    - ev.walmart.reconciliation.001
    notes: Query pattern SQL/template uses this documented column.
```

```yaml
candidate_edge:
  edge_id: edge.walmart.0549
  edge_type: USES_COLUMN
  source: query_pattern.walmart.refund_sale_match
  target: column.zs_observe.walmart_settlement.group_level_id
  fields:
    edge_family: dependency_usage
    evidence_basis: Query pattern SQL/template uses this documented column.
    confidence: high
    canonical_cognee_edge: true
    marketplace_only: true
    canonical_edge_type: USES_COLUMN
    inverse_edge_type: USED_BY_CARD
    materialize_inverse: false
    edge_class: canonical
    source_type: query_pattern
    target_type: column
    evidence_refs:
    - ev.walmart.reconciliation.001
    notes: Query pattern SQL/template uses this documented column.
```

```yaml
candidate_edge:
  edge_id: edge.walmart.0550
  edge_type: USES_COLUMN
  source: query_pattern.walmart.refund_sale_match
  target: column.zs_observe.walmart_settlement.is_active
  fields:
    edge_family: dependency_usage
    evidence_basis: Query pattern SQL/template uses this documented column.
    confidence: high
    canonical_cognee_edge: true
    marketplace_only: true
    canonical_edge_type: USES_COLUMN
    inverse_edge_type: USED_BY_CARD
    materialize_inverse: false
    edge_class: canonical
    source_type: query_pattern
    target_type: column
    evidence_refs:
    - ev.walmart.reconciliation.001
    notes: Query pattern SQL/template uses this documented column.
```

```yaml
candidate_edge:
  edge_id: edge.walmart.0551
  edge_type: USES_COLUMN
  source: query_pattern.walmart.full_three_table_view
  target: column.zs_observe.walmart_oms.order_id
  fields:
    edge_family: dependency_usage
    evidence_basis: Query pattern SQL/template uses this documented column.
    confidence: high
    canonical_cognee_edge: true
    marketplace_only: true
    canonical_edge_type: USES_COLUMN
    inverse_edge_type: USED_BY_CARD
    materialize_inverse: false
    edge_class: canonical
    source_type: query_pattern
    target_type: column
    evidence_refs:
    - ev.walmart.reconciliation.001
    notes: Query pattern SQL/template uses this documented column.
```

```yaml
candidate_edge:
  edge_id: edge.walmart.0552
  edge_type: USES_COLUMN
  source: query_pattern.walmart.full_three_table_view
  target: column.zs_observe.walmart_oms.sku_id
  fields:
    edge_family: dependency_usage
    evidence_basis: Query pattern SQL/template uses this documented column.
    confidence: high
    canonical_cognee_edge: true
    marketplace_only: true
    canonical_edge_type: USES_COLUMN
    inverse_edge_type: USED_BY_CARD
    materialize_inverse: false
    edge_class: canonical
    source_type: query_pattern
    target_type: column
    evidence_refs:
    - ev.walmart.reconciliation.001
    notes: Query pattern SQL/template uses this documented column.
```

```yaml
candidate_edge:
  edge_id: edge.walmart.0553
  edge_type: USES_COLUMN
  source: query_pattern.walmart.full_three_table_view
  target: column.zs_observe.walmart_oms.created_date
  fields:
    edge_family: dependency_usage
    evidence_basis: Query pattern SQL/template uses this documented column.
    confidence: high
    canonical_cognee_edge: true
    marketplace_only: true
    canonical_edge_type: USES_COLUMN
    inverse_edge_type: USED_BY_CARD
    materialize_inverse: false
    edge_class: canonical
    source_type: query_pattern
    target_type: column
    evidence_refs:
    - ev.walmart.reconciliation.001
    notes: Query pattern SQL/template uses this documented column.
```

```yaml
candidate_edge:
  edge_id: edge.walmart.0554
  edge_type: USES_COLUMN
  source: query_pattern.walmart.full_three_table_view
  target: column.zs_observe.walmart_oms.charged_amount
  fields:
    edge_family: dependency_usage
    evidence_basis: Query pattern SQL/template uses this documented column.
    confidence: high
    canonical_cognee_edge: true
    marketplace_only: true
    canonical_edge_type: USES_COLUMN
    inverse_edge_type: USED_BY_CARD
    materialize_inverse: false
    edge_class: canonical
    source_type: query_pattern
    target_type: column
    evidence_refs:
    - ev.walmart.reconciliation.001
    notes: Query pattern SQL/template uses this documented column.
```

```yaml
candidate_edge:
  edge_id: edge.walmart.0555
  edge_type: USES_COLUMN
  source: query_pattern.walmart.full_three_table_view
  target: column.zs_observe.walmart_oms.internal_txn_type
  fields:
    edge_family: dependency_usage
    evidence_basis: Query pattern SQL/template uses this documented column.
    confidence: high
    canonical_cognee_edge: true
    marketplace_only: true
    canonical_edge_type: USES_COLUMN
    inverse_edge_type: USED_BY_CARD
    materialize_inverse: false
    edge_class: canonical
    source_type: query_pattern
    target_type: column
    evidence_refs:
    - ev.walmart.reconciliation.001
    notes: Query pattern SQL/template uses this documented column.
```

```yaml
candidate_edge:
  edge_id: edge.walmart.0556
  edge_type: USES_COLUMN
  source: query_pattern.walmart.full_three_table_view
  target: column.zs_observe.walmart_oms.order_status
  fields:
    edge_family: dependency_usage
    evidence_basis: Query pattern SQL/template uses this documented column.
    confidence: high
    canonical_cognee_edge: true
    marketplace_only: true
    canonical_edge_type: USES_COLUMN
    inverse_edge_type: USED_BY_CARD
    materialize_inverse: false
    edge_class: canonical
    source_type: query_pattern
    target_type: column
    evidence_refs:
    - ev.walmart.reconciliation.001
    notes: Query pattern SQL/template uses this documented column.
```

```yaml
candidate_edge:
  edge_id: edge.walmart.0557
  edge_type: USES_COLUMN
  source: query_pattern.walmart.full_three_table_view
  target: column.zs_observe.walmart_oms.destination_state
  fields:
    edge_family: dependency_usage
    evidence_basis: Query pattern SQL/template uses this documented column.
    confidence: high
    canonical_cognee_edge: true
    marketplace_only: true
    canonical_edge_type: USES_COLUMN
    inverse_edge_type: USED_BY_CARD
    materialize_inverse: false
    edge_class: canonical
    source_type: query_pattern
    target_type: column
    evidence_refs:
    - ev.walmart.reconciliation.001
    notes: Query pattern SQL/template uses this documented column.
```

```yaml
candidate_edge:
  edge_id: edge.walmart.0558
  edge_type: USES_COLUMN
  source: query_pattern.walmart.full_three_table_view
  target: column.zs_observe.walmart_oms.destination_city
  fields:
    edge_family: dependency_usage
    evidence_basis: Query pattern SQL/template uses this documented column.
    confidence: high
    canonical_cognee_edge: true
    marketplace_only: true
    canonical_edge_type: USES_COLUMN
    inverse_edge_type: USED_BY_CARD
    materialize_inverse: false
    edge_class: canonical
    source_type: query_pattern
    target_type: column
    evidence_refs:
    - ev.walmart.reconciliation.001
    notes: Query pattern SQL/template uses this documented column.
```

```yaml
candidate_edge:
  edge_id: edge.walmart.0559
  edge_type: USES_COLUMN
  source: query_pattern.walmart.full_three_table_view
  target: column.zs_observe.walmart_oms.item_name
  fields:
    edge_family: dependency_usage
    evidence_basis: Query pattern SQL/template uses this documented column.
    confidence: high
    canonical_cognee_edge: true
    marketplace_only: true
    canonical_edge_type: USES_COLUMN
    inverse_edge_type: USED_BY_CARD
    materialize_inverse: false
    edge_class: canonical
    source_type: query_pattern
    target_type: column
    evidence_refs:
    - ev.walmart.reconciliation.001
    notes: Query pattern SQL/template uses this documented column.
```

```yaml
candidate_edge:
  edge_id: edge.walmart.0560
  edge_type: USES_COLUMN
  source: query_pattern.walmart.full_three_table_view
  target: column.zs_observe.walmart_oms.group_level_id
  fields:
    edge_family: dependency_usage
    evidence_basis: Query pattern SQL/template uses this documented column.
    confidence: high
    canonical_cognee_edge: true
    marketplace_only: true
    canonical_edge_type: USES_COLUMN
    inverse_edge_type: USED_BY_CARD
    materialize_inverse: false
    edge_class: canonical
    source_type: query_pattern
    target_type: column
    evidence_refs:
    - ev.walmart.reconciliation.001
    notes: Query pattern SQL/template uses this documented column.
```

```yaml
candidate_edge:
  edge_id: edge.walmart.0561
  edge_type: USES_COLUMN
  source: query_pattern.walmart.full_three_table_view
  target: column.zs_observe.walmart_oms.is_active
  fields:
    edge_family: dependency_usage
    evidence_basis: Query pattern SQL/template uses this documented column.
    confidence: high
    canonical_cognee_edge: true
    marketplace_only: true
    canonical_edge_type: USES_COLUMN
    inverse_edge_type: USED_BY_CARD
    materialize_inverse: false
    edge_class: canonical
    source_type: query_pattern
    target_type: column
    evidence_refs:
    - ev.walmart.reconciliation.001
    notes: Query pattern SQL/template uses this documented column.
```

```yaml
candidate_edge:
  edge_id: edge.walmart.0562
  edge_type: USES_COLUMN
  source: query_pattern.walmart.full_three_table_view
  target: column.zs_observe.walmart_settlement.order_id
  fields:
    edge_family: dependency_usage
    evidence_basis: Query pattern SQL/template uses this documented column.
    confidence: high
    canonical_cognee_edge: true
    marketplace_only: true
    canonical_edge_type: USES_COLUMN
    inverse_edge_type: USED_BY_CARD
    materialize_inverse: false
    edge_class: canonical
    source_type: query_pattern
    target_type: column
    evidence_refs:
    - ev.walmart.reconciliation.001
    notes: Query pattern SQL/template uses this documented column.
```

```yaml
candidate_edge:
  edge_id: edge.walmart.0563
  edge_type: USES_COLUMN
  source: query_pattern.walmart.full_three_table_view
  target: column.zs_observe.walmart_settlement.sku_id
  fields:
    edge_family: dependency_usage
    evidence_basis: Query pattern SQL/template uses this documented column.
    confidence: high
    canonical_cognee_edge: true
    marketplace_only: true
    canonical_edge_type: USES_COLUMN
    inverse_edge_type: USED_BY_CARD
    materialize_inverse: false
    edge_class: canonical
    source_type: query_pattern
    target_type: column
    evidence_refs:
    - ev.walmart.reconciliation.001
    notes: Query pattern SQL/template uses this documented column.
```

```yaml
candidate_edge:
  edge_id: edge.walmart.0564
  edge_type: USES_COLUMN
  source: query_pattern.walmart.full_three_table_view
  target: column.zs_observe.walmart_settlement.created_date
  fields:
    edge_family: dependency_usage
    evidence_basis: Query pattern SQL/template uses this documented column.
    confidence: high
    canonical_cognee_edge: true
    marketplace_only: true
    canonical_edge_type: USES_COLUMN
    inverse_edge_type: USED_BY_CARD
    materialize_inverse: false
    edge_class: canonical
    source_type: query_pattern
    target_type: column
    evidence_refs:
    - ev.walmart.reconciliation.001
    notes: Query pattern SQL/template uses this documented column.
```

```yaml
candidate_edge:
  edge_id: edge.walmart.0565
  edge_type: USES_COLUMN
  source: query_pattern.walmart.full_three_table_view
  target: column.zs_observe.walmart_settlement.metadata_3
  fields:
    edge_family: dependency_usage
    evidence_basis: Query pattern SQL/template uses this documented column.
    confidence: high
    canonical_cognee_edge: true
    marketplace_only: true
    canonical_edge_type: USES_COLUMN
    inverse_edge_type: USED_BY_CARD
    materialize_inverse: false
    edge_class: canonical
    source_type: query_pattern
    target_type: column
    evidence_refs:
    - ev.walmart.reconciliation.001
    notes: Query pattern SQL/template uses this documented column.
```

```yaml
candidate_edge:
  edge_id: edge.walmart.0566
  edge_type: USES_COLUMN
  source: query_pattern.walmart.full_three_table_view
  target: column.zs_observe.walmart_settlement.charged_amount
  fields:
    edge_family: dependency_usage
    evidence_basis: Query pattern SQL/template uses this documented column.
    confidence: high
    canonical_cognee_edge: true
    marketplace_only: true
    canonical_edge_type: USES_COLUMN
    inverse_edge_type: USED_BY_CARD
    materialize_inverse: false
    edge_class: canonical
    source_type: query_pattern
    target_type: column
    evidence_refs:
    - ev.walmart.reconciliation.001
    notes: Query pattern SQL/template uses this documented column.
```

```yaml
candidate_edge:
  edge_id: edge.walmart.0567
  edge_type: USES_COLUMN
  source: query_pattern.walmart.full_three_table_view
  target: column.zs_observe.walmart_settlement.charged_amount_excluding_tax
  fields:
    edge_family: dependency_usage
    evidence_basis: Query pattern SQL/template uses this documented column.
    confidence: high
    canonical_cognee_edge: true
    marketplace_only: true
    canonical_edge_type: USES_COLUMN
    inverse_edge_type: USED_BY_CARD
    materialize_inverse: false
    edge_class: canonical
    source_type: query_pattern
    target_type: column
    evidence_refs:
    - ev.walmart.reconciliation.001
    notes: Query pattern SQL/template uses this documented column.
```

```yaml
candidate_edge:
  edge_id: edge.walmart.0568
  edge_type: USES_COLUMN
  source: query_pattern.walmart.full_three_table_view
  target: column.zs_observe.walmart_settlement.total_tax
  fields:
    edge_family: dependency_usage
    evidence_basis: Query pattern SQL/template uses this documented column.
    confidence: high
    canonical_cognee_edge: true
    marketplace_only: true
    canonical_edge_type: USES_COLUMN
    inverse_edge_type: USED_BY_CARD
    materialize_inverse: false
    edge_class: canonical
    source_type: query_pattern
    target_type: column
    evidence_refs:
    - ev.walmart.reconciliation.001
    notes: Query pattern SQL/template uses this documented column.
```

```yaml
candidate_edge:
  edge_id: edge.walmart.0569
  edge_type: USES_COLUMN
  source: query_pattern.walmart.full_three_table_view
  target: column.zs_observe.walmart_settlement.gross_commission
  fields:
    edge_family: dependency_usage
    evidence_basis: Query pattern SQL/template uses this documented column.
    confidence: high
    canonical_cognee_edge: true
    marketplace_only: true
    canonical_edge_type: USES_COLUMN
    inverse_edge_type: USED_BY_CARD
    materialize_inverse: false
    edge_class: canonical
    source_type: query_pattern
    target_type: column
    evidence_refs:
    - ev.walmart.reconciliation.001
    notes: Query pattern SQL/template uses this documented column.
```

```yaml
candidate_edge:
  edge_id: edge.walmart.0570
  edge_type: USES_COLUMN
  source: query_pattern.walmart.full_three_table_view
  target: column.zs_observe.walmart_settlement.transaction_type
  fields:
    edge_family: dependency_usage
    evidence_basis: Query pattern SQL/template uses this documented column.
    confidence: high
    canonical_cognee_edge: true
    marketplace_only: true
    canonical_edge_type: USES_COLUMN
    inverse_edge_type: USED_BY_CARD
    materialize_inverse: false
    edge_class: canonical
    source_type: query_pattern
    target_type: column
    evidence_refs:
    - ev.walmart.reconciliation.001
    notes: Query pattern SQL/template uses this documented column.
```

```yaml
candidate_edge:
  edge_id: edge.walmart.0571
  edge_type: USES_COLUMN
  source: query_pattern.walmart.full_three_table_view
  target: column.zs_observe.walmart_settlement.internal_txn_type
  fields:
    edge_family: dependency_usage
    evidence_basis: Query pattern SQL/template uses this documented column.
    confidence: high
    canonical_cognee_edge: true
    marketplace_only: true
    canonical_edge_type: USES_COLUMN
    inverse_edge_type: USED_BY_CARD
    materialize_inverse: false
    edge_class: canonical
    source_type: query_pattern
    target_type: column
    evidence_refs:
    - ev.walmart.reconciliation.001
    notes: Query pattern SQL/template uses this documented column.
```

```yaml
candidate_edge:
  edge_id: edge.walmart.0572
  edge_type: USES_COLUMN
  source: query_pattern.walmart.full_three_table_view
  target: column.zs_observe.walmart_settlement.product_category
  fields:
    edge_family: dependency_usage
    evidence_basis: Query pattern SQL/template uses this documented column.
    confidence: high
    canonical_cognee_edge: true
    marketplace_only: true
    canonical_edge_type: USES_COLUMN
    inverse_edge_type: USED_BY_CARD
    materialize_inverse: false
    edge_class: canonical
    source_type: query_pattern
    target_type: column
    evidence_refs:
    - ev.walmart.reconciliation.001
    notes: Query pattern SQL/template uses this documented column.
```

```yaml
candidate_edge:
  edge_id: edge.walmart.0573
  edge_type: USES_COLUMN
  source: query_pattern.walmart.full_three_table_view
  target: column.zs_observe.walmart_settlement.product_type
  fields:
    edge_family: dependency_usage
    evidence_basis: Query pattern SQL/template uses this documented column.
    confidence: high
    canonical_cognee_edge: true
    marketplace_only: true
    canonical_edge_type: USES_COLUMN
    inverse_edge_type: USED_BY_CARD
    materialize_inverse: false
    edge_class: canonical
    source_type: query_pattern
    target_type: column
    evidence_refs:
    - ev.walmart.reconciliation.001
    notes: Query pattern SQL/template uses this documented column.
```

```yaml
candidate_edge:
  edge_id: edge.walmart.0574
  edge_type: USES_COLUMN
  source: query_pattern.walmart.full_three_table_view
  target: column.zs_observe.walmart_settlement.destination_state
  fields:
    edge_family: dependency_usage
    evidence_basis: Query pattern SQL/template uses this documented column.
    confidence: high
    canonical_cognee_edge: true
    marketplace_only: true
    canonical_edge_type: USES_COLUMN
    inverse_edge_type: USED_BY_CARD
    materialize_inverse: false
    edge_class: canonical
    source_type: query_pattern
    target_type: column
    evidence_refs:
    - ev.walmart.reconciliation.001
    notes: Query pattern SQL/template uses this documented column.
```

```yaml
candidate_edge:
  edge_id: edge.walmart.0575
  edge_type: USES_COLUMN
  source: query_pattern.walmart.full_three_table_view
  target: column.zs_observe.walmart_settlement.destination_city
  fields:
    edge_family: dependency_usage
    evidence_basis: Query pattern SQL/template uses this documented column.
    confidence: high
    canonical_cognee_edge: true
    marketplace_only: true
    canonical_edge_type: USES_COLUMN
    inverse_edge_type: USED_BY_CARD
    materialize_inverse: false
    edge_class: canonical
    source_type: query_pattern
    target_type: column
    evidence_refs:
    - ev.walmart.reconciliation.001
    notes: Query pattern SQL/template uses this documented column.
```

```yaml
candidate_edge:
  edge_id: edge.walmart.0576
  edge_type: USES_COLUMN
  source: query_pattern.walmart.full_three_table_view
  target: column.zs_observe.walmart_settlement.group_level_id
  fields:
    edge_family: dependency_usage
    evidence_basis: Query pattern SQL/template uses this documented column.
    confidence: high
    canonical_cognee_edge: true
    marketplace_only: true
    canonical_edge_type: USES_COLUMN
    inverse_edge_type: USED_BY_CARD
    materialize_inverse: false
    edge_class: canonical
    source_type: query_pattern
    target_type: column
    evidence_refs:
    - ev.walmart.reconciliation.001
    notes: Query pattern SQL/template uses this documented column.
```

```yaml
candidate_edge:
  edge_id: edge.walmart.0577
  edge_type: USES_COLUMN
  source: query_pattern.walmart.full_three_table_view
  target: column.zs_observe.walmart_settlement.is_active
  fields:
    edge_family: dependency_usage
    evidence_basis: Query pattern SQL/template uses this documented column.
    confidence: high
    canonical_cognee_edge: true
    marketplace_only: true
    canonical_edge_type: USES_COLUMN
    inverse_edge_type: USED_BY_CARD
    materialize_inverse: false
    edge_class: canonical
    source_type: query_pattern
    target_type: column
    evidence_refs:
    - ev.walmart.reconciliation.001
    notes: Query pattern SQL/template uses this documented column.
```

```yaml
candidate_edge:
  edge_id: edge.walmart.0578
  edge_type: USES_COLUMN
  source: query_pattern.walmart.full_three_table_view
  target: column.zs_observe.walmart_lookup.sku_id
  fields:
    edge_family: dependency_usage
    evidence_basis: Query pattern SQL/template uses this documented column.
    confidence: high
    canonical_cognee_edge: true
    marketplace_only: true
    canonical_edge_type: USES_COLUMN
    inverse_edge_type: USED_BY_CARD
    materialize_inverse: false
    edge_class: canonical
    source_type: query_pattern
    target_type: column
    evidence_refs:
    - ev.walmart.reconciliation.001
    notes: Query pattern SQL/template uses this documented column.
```

```yaml
candidate_edge:
  edge_id: edge.walmart.0579
  edge_type: USES_COLUMN
  source: query_pattern.walmart.full_three_table_view
  target: column.zs_observe.walmart_lookup.sku
  fields:
    edge_family: dependency_usage
    evidence_basis: Query pattern SQL/template uses this documented column.
    confidence: high
    canonical_cognee_edge: true
    marketplace_only: true
    canonical_edge_type: USES_COLUMN
    inverse_edge_type: USED_BY_CARD
    materialize_inverse: false
    edge_class: canonical
    source_type: query_pattern
    target_type: column
    evidence_refs:
    - ev.walmart.reconciliation.001
    notes: Query pattern SQL/template uses this documented column.
```

```yaml
candidate_edge:
  edge_id: edge.walmart.0580
  edge_type: USES_COLUMN
  source: query_pattern.walmart.full_three_table_view
  target: column.zs_observe.walmart_lookup.item_name
  fields:
    edge_family: dependency_usage
    evidence_basis: Query pattern SQL/template uses this documented column.
    confidence: high
    canonical_cognee_edge: true
    marketplace_only: true
    canonical_edge_type: USES_COLUMN
    inverse_edge_type: USED_BY_CARD
    materialize_inverse: false
    edge_class: canonical
    source_type: query_pattern
    target_type: column
    evidence_refs:
    - ev.walmart.reconciliation.001
    notes: Query pattern SQL/template uses this documented column.
```

```yaml
candidate_edge:
  edge_id: edge.walmart.0581
  edge_type: USES_COLUMN
  source: query_pattern.walmart.full_three_table_view
  target: column.zs_observe.walmart_lookup.group_level_id
  fields:
    edge_family: dependency_usage
    evidence_basis: Query pattern SQL/template uses this documented column.
    confidence: high
    canonical_cognee_edge: true
    marketplace_only: true
    canonical_edge_type: USES_COLUMN
    inverse_edge_type: USED_BY_CARD
    materialize_inverse: false
    edge_class: canonical
    source_type: query_pattern
    target_type: column
    evidence_refs:
    - ev.walmart.reconciliation.001
    notes: Query pattern SQL/template uses this documented column.
```

```yaml
candidate_edge:
  edge_id: edge.walmart.0582
  edge_type: USES_COLUMN
  source: query_pattern.walmart.full_three_table_view
  target: column.zs_observe.walmart_lookup.is_active
  fields:
    edge_family: dependency_usage
    evidence_basis: Query pattern SQL/template uses this documented column.
    confidence: high
    canonical_cognee_edge: true
    marketplace_only: true
    canonical_edge_type: USES_COLUMN
    inverse_edge_type: USED_BY_CARD
    materialize_inverse: false
    edge_class: canonical
    source_type: query_pattern
    target_type: column
    evidence_refs:
    - ev.walmart.reconciliation.001
    notes: Query pattern SQL/template uses this documented column.
```

```yaml
candidate_edge:
  edge_id: edge.walmart.0583
  edge_type: USES_COLUMN
  source: query_pattern.walmart.lookup_catalogue
  target: column.zs_observe.walmart_lookup.sku_id
  fields:
    edge_family: dependency_usage
    evidence_basis: Query pattern SQL/template uses this documented column.
    confidence: high
    canonical_cognee_edge: true
    marketplace_only: true
    canonical_edge_type: USES_COLUMN
    inverse_edge_type: USED_BY_CARD
    materialize_inverse: false
    edge_class: canonical
    source_type: query_pattern
    target_type: column
    evidence_refs:
    - ev.walmart_lookup.schema.001
    notes: Query pattern SQL/template uses this documented column.
```

```yaml
candidate_edge:
  edge_id: edge.walmart.0584
  edge_type: USES_COLUMN
  source: query_pattern.walmart.lookup_catalogue
  target: column.zs_observe.walmart_lookup.sku
  fields:
    edge_family: dependency_usage
    evidence_basis: Query pattern SQL/template uses this documented column.
    confidence: high
    canonical_cognee_edge: true
    marketplace_only: true
    canonical_edge_type: USES_COLUMN
    inverse_edge_type: USED_BY_CARD
    materialize_inverse: false
    edge_class: canonical
    source_type: query_pattern
    target_type: column
    evidence_refs:
    - ev.walmart_lookup.schema.001
    notes: Query pattern SQL/template uses this documented column.
```

```yaml
candidate_edge:
  edge_id: edge.walmart.0585
  edge_type: USES_COLUMN
  source: query_pattern.walmart.lookup_catalogue
  target: column.zs_observe.walmart_lookup.item_name
  fields:
    edge_family: dependency_usage
    evidence_basis: Query pattern SQL/template uses this documented column.
    confidence: high
    canonical_cognee_edge: true
    marketplace_only: true
    canonical_edge_type: USES_COLUMN
    inverse_edge_type: USED_BY_CARD
    materialize_inverse: false
    edge_class: canonical
    source_type: query_pattern
    target_type: column
    evidence_refs:
    - ev.walmart_lookup.schema.001
    notes: Query pattern SQL/template uses this documented column.
```

```yaml
candidate_edge:
  edge_id: edge.walmart.0586
  edge_type: USES_COLUMN
  source: query_pattern.walmart.lookup_catalogue
  target: column.zs_observe.walmart_lookup.currency_type
  fields:
    edge_family: dependency_usage
    evidence_basis: Query pattern SQL/template uses this documented column.
    confidence: high
    canonical_cognee_edge: true
    marketplace_only: true
    canonical_edge_type: USES_COLUMN
    inverse_edge_type: USED_BY_CARD
    materialize_inverse: false
    edge_class: canonical
    source_type: query_pattern
    target_type: column
    evidence_refs:
    - ev.walmart_lookup.schema.001
    notes: Query pattern SQL/template uses this documented column.
```

```yaml
candidate_edge:
  edge_id: edge.walmart.0587
  edge_type: USES_COLUMN
  source: query_pattern.walmart.lookup_catalogue
  target: column.zs_observe.walmart_lookup.group_level_id
  fields:
    edge_family: dependency_usage
    evidence_basis: Query pattern SQL/template uses this documented column.
    confidence: high
    canonical_cognee_edge: true
    marketplace_only: true
    canonical_edge_type: USES_COLUMN
    inverse_edge_type: USED_BY_CARD
    materialize_inverse: false
    edge_class: canonical
    source_type: query_pattern
    target_type: column
    evidence_refs:
    - ev.walmart_lookup.schema.001
    notes: Query pattern SQL/template uses this documented column.
```

```yaml
candidate_edge:
  edge_id: edge.walmart.0588
  edge_type: USES_COLUMN
  source: query_pattern.walmart.lookup_catalogue
  target: column.zs_observe.walmart_lookup.is_active
  fields:
    edge_family: dependency_usage
    evidence_basis: Query pattern SQL/template uses this documented column.
    confidence: high
    canonical_cognee_edge: true
    marketplace_only: true
    canonical_edge_type: USES_COLUMN
    inverse_edge_type: USED_BY_CARD
    materialize_inverse: false
    edge_class: canonical
    source_type: query_pattern
    target_type: column
    evidence_refs:
    - ev.walmart_lookup.schema.001
    notes: Query pattern SQL/template uses this documented column.
```

```yaml
candidate_edge:
  edge_id: edge.walmart.0589
  edge_type: USES_COLUMN
  source: query_pattern.walmart.mpf_tax_validation
  target: column.zs_observe.walmart_settlement.charged_amount
  fields:
    edge_family: dependency_usage
    evidence_basis: Query pattern SQL/template uses this documented column.
    confidence: high
    canonical_cognee_edge: true
    marketplace_only: true
    canonical_edge_type: USES_COLUMN
    inverse_edge_type: USED_BY_CARD
    materialize_inverse: false
    edge_class: canonical
    source_type: query_pattern
    target_type: column
    evidence_refs:
    - ev.walmart.business_model.001
    notes: Query pattern SQL/template uses this documented column.
```

```yaml
candidate_edge:
  edge_id: edge.walmart.0590
  edge_type: USES_COLUMN
  source: query_pattern.walmart.mpf_tax_validation
  target: column.zs_observe.walmart_settlement.charged_amount_excluding_tax
  fields:
    edge_family: dependency_usage
    evidence_basis: Query pattern SQL/template uses this documented column.
    confidence: high
    canonical_cognee_edge: true
    marketplace_only: true
    canonical_edge_type: USES_COLUMN
    inverse_edge_type: USED_BY_CARD
    materialize_inverse: false
    edge_class: canonical
    source_type: query_pattern
    target_type: column
    evidence_refs:
    - ev.walmart.business_model.001
    notes: Query pattern SQL/template uses this documented column.
```

```yaml
candidate_edge:
  edge_id: edge.walmart.0591
  edge_type: USES_COLUMN
  source: query_pattern.walmart.mpf_tax_validation
  target: column.zs_observe.walmart_settlement.total_tax
  fields:
    edge_family: dependency_usage
    evidence_basis: Query pattern SQL/template uses this documented column.
    confidence: high
    canonical_cognee_edge: true
    marketplace_only: true
    canonical_edge_type: USES_COLUMN
    inverse_edge_type: USED_BY_CARD
    materialize_inverse: false
    edge_class: canonical
    source_type: query_pattern
    target_type: column
    evidence_refs:
    - ev.walmart.business_model.001
    notes: Query pattern SQL/template uses this documented column.
```

```yaml
candidate_edge:
  edge_id: edge.walmart.0592
  edge_type: USES_COLUMN
  source: query_pattern.walmart.mpf_tax_validation
  target: column.zs_observe.walmart_settlement.marketplace_withheld_tax
  fields:
    edge_family: dependency_usage
    evidence_basis: Query pattern SQL/template uses this documented column.
    confidence: high
    canonical_cognee_edge: true
    marketplace_only: true
    canonical_edge_type: USES_COLUMN
    inverse_edge_type: USED_BY_CARD
    materialize_inverse: false
    edge_class: canonical
    source_type: query_pattern
    target_type: column
    evidence_refs:
    - ev.walmart.business_model.001
    notes: Query pattern SQL/template uses this documented column.
```

```yaml
candidate_edge:
  edge_id: edge.walmart.0593
  edge_type: USES_COLUMN
  source: query_pattern.walmart.mpf_tax_validation
  target: column.zs_observe.walmart_settlement.transaction_type
  fields:
    edge_family: dependency_usage
    evidence_basis: Query pattern SQL/template uses this documented column.
    confidence: high
    canonical_cognee_edge: true
    marketplace_only: true
    canonical_edge_type: USES_COLUMN
    inverse_edge_type: USED_BY_CARD
    materialize_inverse: false
    edge_class: canonical
    source_type: query_pattern
    target_type: column
    evidence_refs:
    - ev.walmart.business_model.001
    notes: Query pattern SQL/template uses this documented column.
```

```yaml
candidate_edge:
  edge_id: edge.walmart.0594
  edge_type: USES_COLUMN
  source: query_pattern.walmart.mpf_tax_validation
  target: column.zs_observe.walmart_settlement.group_level_id
  fields:
    edge_family: dependency_usage
    evidence_basis: Query pattern SQL/template uses this documented column.
    confidence: high
    canonical_cognee_edge: true
    marketplace_only: true
    canonical_edge_type: USES_COLUMN
    inverse_edge_type: USED_BY_CARD
    materialize_inverse: false
    edge_class: canonical
    source_type: query_pattern
    target_type: column
    evidence_refs:
    - ev.walmart.business_model.001
    notes: Query pattern SQL/template uses this documented column.
```

```yaml
candidate_edge:
  edge_id: edge.walmart.0595
  edge_type: USES_COLUMN
  source: query_pattern.walmart.mpf_tax_validation
  target: column.zs_observe.walmart_settlement.is_active
  fields:
    edge_family: dependency_usage
    evidence_basis: Query pattern SQL/template uses this documented column.
    confidence: high
    canonical_cognee_edge: true
    marketplace_only: true
    canonical_edge_type: USES_COLUMN
    inverse_edge_type: USED_BY_CARD
    materialize_inverse: false
    edge_class: canonical
    source_type: query_pattern
    target_type: column
    evidence_refs:
    - ev.walmart.business_model.001
    notes: Query pattern SQL/template uses this documented column.
```

```yaml
candidate_edge:
  edge_id: edge.walmart.0596
  edge_type: USES_COLUMN
  source: query_pattern.walmart.wfs_fee_visibility
  target: column.zs_observe.walmart_settlement.wfs_inventory_fee_reimbursement
  fields:
    edge_family: dependency_usage
    evidence_basis: Query pattern SQL/template uses this documented column.
    confidence: high
    canonical_cognee_edge: true
    marketplace_only: true
    canonical_edge_type: USES_COLUMN
    inverse_edge_type: USED_BY_CARD
    materialize_inverse: false
    edge_class: canonical
    source_type: query_pattern
    target_type: column
    evidence_refs:
    - ev.walmart.quality.001
    notes: Query pattern SQL/template uses this documented column.
```

```yaml
candidate_edge:
  edge_id: edge.walmart.0597
  edge_type: USES_COLUMN
  source: query_pattern.walmart.wfs_fee_visibility
  target: column.zs_observe.walmart_settlement.fee_reimbursement
  fields:
    edge_family: dependency_usage
    evidence_basis: Query pattern SQL/template uses this documented column.
    confidence: high
    canonical_cognee_edge: true
    marketplace_only: true
    canonical_edge_type: USES_COLUMN
    inverse_edge_type: USED_BY_CARD
    materialize_inverse: false
    edge_class: canonical
    source_type: query_pattern
    target_type: column
    evidence_refs:
    - ev.walmart.quality.001
    notes: Query pattern SQL/template uses this documented column.
```

```yaml
candidate_edge:
  edge_id: edge.walmart.0598
  edge_type: USES_COLUMN
  source: query_pattern.walmart.wfs_fee_visibility
  target: column.zs_observe.walmart_settlement.wfs_fee_reimbursement
  fields:
    edge_family: dependency_usage
    evidence_basis: Query pattern SQL/template uses this documented column.
    confidence: high
    canonical_cognee_edge: true
    marketplace_only: true
    canonical_edge_type: USES_COLUMN
    inverse_edge_type: USED_BY_CARD
    materialize_inverse: false
    edge_class: canonical
    source_type: query_pattern
    target_type: column
    evidence_refs:
    - ev.walmart.quality.001
    notes: Query pattern SQL/template uses this documented column.
```

```yaml
candidate_edge:
  edge_id: edge.walmart.0599
  edge_type: USES_COLUMN
  source: query_pattern.walmart.wfs_fee_visibility
  target: column.zs_observe.walmart_settlement.wfs_inbound_fee
  fields:
    edge_family: dependency_usage
    evidence_basis: Query pattern SQL/template uses this documented column.
    confidence: high
    canonical_cognee_edge: true
    marketplace_only: true
    canonical_edge_type: USES_COLUMN
    inverse_edge_type: USED_BY_CARD
    materialize_inverse: false
    edge_class: canonical
    source_type: query_pattern
    target_type: column
    evidence_refs:
    - ev.walmart.quality.001
    notes: Query pattern SQL/template uses this documented column.
```

```yaml
candidate_edge:
  edge_id: edge.walmart.0600
  edge_type: USES_COLUMN
  source: query_pattern.walmart.wfs_fee_visibility
  target: column.zs_observe.walmart_settlement.sem_marketing_fee
  fields:
    edge_family: dependency_usage
    evidence_basis: Query pattern SQL/template uses this documented column.
    confidence: high
    canonical_cognee_edge: true
    marketplace_only: true
    canonical_edge_type: USES_COLUMN
    inverse_edge_type: USED_BY_CARD
    materialize_inverse: false
    edge_class: canonical
    source_type: query_pattern
    target_type: column
    evidence_refs:
    - ev.walmart.quality.001
    notes: Query pattern SQL/template uses this documented column.
```

```yaml
candidate_edge:
  edge_id: edge.walmart.0601
  edge_type: USES_COLUMN
  source: query_pattern.walmart.wfs_fee_visibility
  target: column.zs_observe.walmart_settlement.group_level_id
  fields:
    edge_family: dependency_usage
    evidence_basis: Query pattern SQL/template uses this documented column.
    confidence: high
    canonical_cognee_edge: true
    marketplace_only: true
    canonical_edge_type: USES_COLUMN
    inverse_edge_type: USED_BY_CARD
    materialize_inverse: false
    edge_class: canonical
    source_type: query_pattern
    target_type: column
    evidence_refs:
    - ev.walmart.quality.001
    notes: Query pattern SQL/template uses this documented column.
```

```yaml
candidate_edge:
  edge_id: edge.walmart.0602
  edge_type: USES_COLUMN
  source: query_pattern.walmart.wfs_fee_visibility
  target: column.zs_observe.walmart_settlement.is_active
  fields:
    edge_family: dependency_usage
    evidence_basis: Query pattern SQL/template uses this documented column.
    confidence: high
    canonical_cognee_edge: true
    marketplace_only: true
    canonical_edge_type: USES_COLUMN
    inverse_edge_type: USED_BY_CARD
    materialize_inverse: false
    edge_class: canonical
    source_type: query_pattern
    target_type: column
    evidence_refs:
    - ev.walmart.quality.001
    notes: Query pattern SQL/template uses this documented column.
```

```yaml
candidate_edge:
  edge_id: edge.walmart.0603
  edge_type: USES_COLUMN
  source: matching_logic.walmart.oms_to_settlement.primary
  target: column.zs_observe.walmart_oms.order_id
  fields:
    edge_family: dependency_usage
    evidence_basis: matching_logic SQL/template uses this documented column.
    confidence: high
    canonical_cognee_edge: true
    marketplace_only: true
    canonical_edge_type: USES_COLUMN
    inverse_edge_type: USED_BY_CARD
    materialize_inverse: false
    edge_class: canonical
    source_type: matching_logic
    target_type: column
    evidence_refs:
    - ev.walmart.reconciliation.001
    notes: matching_logic SQL/template uses this documented column.
```

```yaml
candidate_edge:
  edge_id: edge.walmart.0604
  edge_type: USES_COLUMN
  source: matching_logic.walmart.oms_to_settlement.primary
  target: column.zs_observe.walmart_oms.sku_id
  fields:
    edge_family: dependency_usage
    evidence_basis: matching_logic SQL/template uses this documented column.
    confidence: high
    canonical_cognee_edge: true
    marketplace_only: true
    canonical_edge_type: USES_COLUMN
    inverse_edge_type: USED_BY_CARD
    materialize_inverse: false
    edge_class: canonical
    source_type: matching_logic
    target_type: column
    evidence_refs:
    - ev.walmart.reconciliation.001
    notes: matching_logic SQL/template uses this documented column.
```

```yaml
candidate_edge:
  edge_id: edge.walmart.0605
  edge_type: USES_COLUMN
  source: matching_logic.walmart.oms_to_settlement.primary
  target: column.zs_observe.walmart_oms.created_date
  fields:
    edge_family: dependency_usage
    evidence_basis: matching_logic SQL/template uses this documented column.
    confidence: high
    canonical_cognee_edge: true
    marketplace_only: true
    canonical_edge_type: USES_COLUMN
    inverse_edge_type: USED_BY_CARD
    materialize_inverse: false
    edge_class: canonical
    source_type: matching_logic
    target_type: column
    evidence_refs:
    - ev.walmart.reconciliation.001
    notes: matching_logic SQL/template uses this documented column.
```

```yaml
candidate_edge:
  edge_id: edge.walmart.0606
  edge_type: USES_COLUMN
  source: matching_logic.walmart.oms_to_settlement.primary
  target: column.zs_observe.walmart_oms.charged_amount
  fields:
    edge_family: dependency_usage
    evidence_basis: matching_logic SQL/template uses this documented column.
    confidence: high
    canonical_cognee_edge: true
    marketplace_only: true
    canonical_edge_type: USES_COLUMN
    inverse_edge_type: USED_BY_CARD
    materialize_inverse: false
    edge_class: canonical
    source_type: matching_logic
    target_type: column
    evidence_refs:
    - ev.walmart.reconciliation.001
    notes: matching_logic SQL/template uses this documented column.
```

```yaml
candidate_edge:
  edge_id: edge.walmart.0607
  edge_type: USES_COLUMN
  source: matching_logic.walmart.oms_to_settlement.primary
  target: column.zs_observe.walmart_oms.internal_txn_type
  fields:
    edge_family: dependency_usage
    evidence_basis: matching_logic SQL/template uses this documented column.
    confidence: high
    canonical_cognee_edge: true
    marketplace_only: true
    canonical_edge_type: USES_COLUMN
    inverse_edge_type: USED_BY_CARD
    materialize_inverse: false
    edge_class: canonical
    source_type: matching_logic
    target_type: column
    evidence_refs:
    - ev.walmart.reconciliation.001
    notes: matching_logic SQL/template uses this documented column.
```

```yaml
candidate_edge:
  edge_id: edge.walmart.0608
  edge_type: USES_COLUMN
  source: matching_logic.walmart.oms_to_settlement.primary
  target: column.zs_observe.walmart_oms.order_status
  fields:
    edge_family: dependency_usage
    evidence_basis: matching_logic SQL/template uses this documented column.
    confidence: high
    canonical_cognee_edge: true
    marketplace_only: true
    canonical_edge_type: USES_COLUMN
    inverse_edge_type: USED_BY_CARD
    materialize_inverse: false
    edge_class: canonical
    source_type: matching_logic
    target_type: column
    evidence_refs:
    - ev.walmart.reconciliation.001
    notes: matching_logic SQL/template uses this documented column.
```

```yaml
candidate_edge:
  edge_id: edge.walmart.0609
  edge_type: USES_COLUMN
  source: matching_logic.walmart.oms_to_settlement.primary
  target: column.zs_observe.walmart_oms.group_level_id
  fields:
    edge_family: dependency_usage
    evidence_basis: matching_logic SQL/template uses this documented column.
    confidence: high
    canonical_cognee_edge: true
    marketplace_only: true
    canonical_edge_type: USES_COLUMN
    inverse_edge_type: USED_BY_CARD
    materialize_inverse: false
    edge_class: canonical
    source_type: matching_logic
    target_type: column
    evidence_refs:
    - ev.walmart.reconciliation.001
    notes: matching_logic SQL/template uses this documented column.
```

```yaml
candidate_edge:
  edge_id: edge.walmart.0610
  edge_type: USES_COLUMN
  source: matching_logic.walmart.oms_to_settlement.primary
  target: column.zs_observe.walmart_oms.is_active
  fields:
    edge_family: dependency_usage
    evidence_basis: matching_logic SQL/template uses this documented column.
    confidence: high
    canonical_cognee_edge: true
    marketplace_only: true
    canonical_edge_type: USES_COLUMN
    inverse_edge_type: USED_BY_CARD
    materialize_inverse: false
    edge_class: canonical
    source_type: matching_logic
    target_type: column
    evidence_refs:
    - ev.walmart.reconciliation.001
    notes: matching_logic SQL/template uses this documented column.
```

```yaml
candidate_edge:
  edge_id: edge.walmart.0611
  edge_type: USES_COLUMN
  source: matching_logic.walmart.oms_to_settlement.primary
  target: column.zs_observe.walmart_settlement.order_id
  fields:
    edge_family: dependency_usage
    evidence_basis: matching_logic SQL/template uses this documented column.
    confidence: high
    canonical_cognee_edge: true
    marketplace_only: true
    canonical_edge_type: USES_COLUMN
    inverse_edge_type: USED_BY_CARD
    materialize_inverse: false
    edge_class: canonical
    source_type: matching_logic
    target_type: column
    evidence_refs:
    - ev.walmart.reconciliation.001
    notes: matching_logic SQL/template uses this documented column.
```

```yaml
candidate_edge:
  edge_id: edge.walmart.0612
  edge_type: USES_COLUMN
  source: matching_logic.walmart.oms_to_settlement.primary
  target: column.zs_observe.walmart_settlement.sku_id
  fields:
    edge_family: dependency_usage
    evidence_basis: matching_logic SQL/template uses this documented column.
    confidence: high
    canonical_cognee_edge: true
    marketplace_only: true
    canonical_edge_type: USES_COLUMN
    inverse_edge_type: USED_BY_CARD
    materialize_inverse: false
    edge_class: canonical
    source_type: matching_logic
    target_type: column
    evidence_refs:
    - ev.walmart.reconciliation.001
    notes: matching_logic SQL/template uses this documented column.
```

```yaml
candidate_edge:
  edge_id: edge.walmart.0613
  edge_type: USES_COLUMN
  source: matching_logic.walmart.oms_to_settlement.primary
  target: column.zs_observe.walmart_settlement.created_date
  fields:
    edge_family: dependency_usage
    evidence_basis: matching_logic SQL/template uses this documented column.
    confidence: high
    canonical_cognee_edge: true
    marketplace_only: true
    canonical_edge_type: USES_COLUMN
    inverse_edge_type: USED_BY_CARD
    materialize_inverse: false
    edge_class: canonical
    source_type: matching_logic
    target_type: column
    evidence_refs:
    - ev.walmart.reconciliation.001
    notes: matching_logic SQL/template uses this documented column.
```

```yaml
candidate_edge:
  edge_id: edge.walmart.0614
  edge_type: USES_COLUMN
  source: matching_logic.walmart.oms_to_settlement.primary
  target: column.zs_observe.walmart_settlement.charged_amount
  fields:
    edge_family: dependency_usage
    evidence_basis: matching_logic SQL/template uses this documented column.
    confidence: high
    canonical_cognee_edge: true
    marketplace_only: true
    canonical_edge_type: USES_COLUMN
    inverse_edge_type: USED_BY_CARD
    materialize_inverse: false
    edge_class: canonical
    source_type: matching_logic
    target_type: column
    evidence_refs:
    - ev.walmart.reconciliation.001
    notes: matching_logic SQL/template uses this documented column.
```

```yaml
candidate_edge:
  edge_id: edge.walmart.0615
  edge_type: USES_COLUMN
  source: matching_logic.walmart.oms_to_settlement.primary
  target: column.zs_observe.walmart_settlement.charged_amount_excluding_tax
  fields:
    edge_family: dependency_usage
    evidence_basis: matching_logic SQL/template uses this documented column.
    confidence: high
    canonical_cognee_edge: true
    marketplace_only: true
    canonical_edge_type: USES_COLUMN
    inverse_edge_type: USED_BY_CARD
    materialize_inverse: false
    edge_class: canonical
    source_type: matching_logic
    target_type: column
    evidence_refs:
    - ev.walmart.reconciliation.001
    notes: matching_logic SQL/template uses this documented column.
```

```yaml
candidate_edge:
  edge_id: edge.walmart.0616
  edge_type: USES_COLUMN
  source: matching_logic.walmart.oms_to_settlement.primary
  target: column.zs_observe.walmart_settlement.total_tax
  fields:
    edge_family: dependency_usage
    evidence_basis: matching_logic SQL/template uses this documented column.
    confidence: high
    canonical_cognee_edge: true
    marketplace_only: true
    canonical_edge_type: USES_COLUMN
    inverse_edge_type: USED_BY_CARD
    materialize_inverse: false
    edge_class: canonical
    source_type: matching_logic
    target_type: column
    evidence_refs:
    - ev.walmart.reconciliation.001
    notes: matching_logic SQL/template uses this documented column.
```

```yaml
candidate_edge:
  edge_id: edge.walmart.0617
  edge_type: USES_COLUMN
  source: matching_logic.walmart.oms_to_settlement.primary
  target: column.zs_observe.walmart_settlement.gross_commission
  fields:
    edge_family: dependency_usage
    evidence_basis: matching_logic SQL/template uses this documented column.
    confidence: high
    canonical_cognee_edge: true
    marketplace_only: true
    canonical_edge_type: USES_COLUMN
    inverse_edge_type: USED_BY_CARD
    materialize_inverse: false
    edge_class: canonical
    source_type: matching_logic
    target_type: column
    evidence_refs:
    - ev.walmart.reconciliation.001
    notes: matching_logic SQL/template uses this documented column.
```

```yaml
candidate_edge:
  edge_id: edge.walmart.0618
  edge_type: USES_COLUMN
  source: matching_logic.walmart.oms_to_settlement.primary
  target: column.zs_observe.walmart_settlement.marketplace_withheld_tax
  fields:
    edge_family: dependency_usage
    evidence_basis: matching_logic SQL/template uses this documented column.
    confidence: high
    canonical_cognee_edge: true
    marketplace_only: true
    canonical_edge_type: USES_COLUMN
    inverse_edge_type: USED_BY_CARD
    materialize_inverse: false
    edge_class: canonical
    source_type: matching_logic
    target_type: column
    evidence_refs:
    - ev.walmart.reconciliation.001
    notes: matching_logic SQL/template uses this documented column.
```

```yaml
candidate_edge:
  edge_id: edge.walmart.0619
  edge_type: USES_COLUMN
  source: matching_logic.walmart.oms_to_settlement.primary
  target: column.zs_observe.walmart_settlement.transaction_type
  fields:
    edge_family: dependency_usage
    evidence_basis: matching_logic SQL/template uses this documented column.
    confidence: high
    canonical_cognee_edge: true
    marketplace_only: true
    canonical_edge_type: USES_COLUMN
    inverse_edge_type: USED_BY_CARD
    materialize_inverse: false
    edge_class: canonical
    source_type: matching_logic
    target_type: column
    evidence_refs:
    - ev.walmart.reconciliation.001
    notes: matching_logic SQL/template uses this documented column.
```

```yaml
candidate_edge:
  edge_id: edge.walmart.0620
  edge_type: USES_COLUMN
  source: matching_logic.walmart.oms_to_settlement.primary
  target: column.zs_observe.walmart_settlement.internal_txn_type
  fields:
    edge_family: dependency_usage
    evidence_basis: matching_logic SQL/template uses this documented column.
    confidence: high
    canonical_cognee_edge: true
    marketplace_only: true
    canonical_edge_type: USES_COLUMN
    inverse_edge_type: USED_BY_CARD
    materialize_inverse: false
    edge_class: canonical
    source_type: matching_logic
    target_type: column
    evidence_refs:
    - ev.walmart.reconciliation.001
    notes: matching_logic SQL/template uses this documented column.
```

```yaml
candidate_edge:
  edge_id: edge.walmart.0621
  edge_type: USES_COLUMN
  source: matching_logic.walmart.oms_to_settlement.primary
  target: column.zs_observe.walmart_settlement.group_level_id
  fields:
    edge_family: dependency_usage
    evidence_basis: matching_logic SQL/template uses this documented column.
    confidence: high
    canonical_cognee_edge: true
    marketplace_only: true
    canonical_edge_type: USES_COLUMN
    inverse_edge_type: USED_BY_CARD
    materialize_inverse: false
    edge_class: canonical
    source_type: matching_logic
    target_type: column
    evidence_refs:
    - ev.walmart.reconciliation.001
    notes: matching_logic SQL/template uses this documented column.
```

```yaml
candidate_edge:
  edge_id: edge.walmart.0622
  edge_type: USES_COLUMN
  source: matching_logic.walmart.oms_to_settlement.primary
  target: column.zs_observe.walmart_settlement.is_active
  fields:
    edge_family: dependency_usage
    evidence_basis: matching_logic SQL/template uses this documented column.
    confidence: high
    canonical_cognee_edge: true
    marketplace_only: true
    canonical_edge_type: USES_COLUMN
    inverse_edge_type: USED_BY_CARD
    materialize_inverse: false
    edge_class: canonical
    source_type: matching_logic
    target_type: column
    evidence_refs:
    - ev.walmart.reconciliation.001
    notes: matching_logic SQL/template uses this documented column.
```

```yaml
candidate_edge:
  edge_id: edge.walmart.0623
  edge_type: USES_COLUMN
  source: matching_logic.walmart.commission_validation.primary
  target: column.zs_observe.walmart_settlement.order_id
  fields:
    edge_family: dependency_usage
    evidence_basis: matching_logic SQL/template uses this documented column.
    confidence: high
    canonical_cognee_edge: true
    marketplace_only: true
    canonical_edge_type: USES_COLUMN
    inverse_edge_type: USED_BY_CARD
    materialize_inverse: false
    edge_class: canonical
    source_type: matching_logic
    target_type: column
    evidence_refs:
    - ev.walmart.reconciliation.001
    notes: matching_logic SQL/template uses this documented column.
```

```yaml
candidate_edge:
  edge_id: edge.walmart.0624
  edge_type: USES_COLUMN
  source: matching_logic.walmart.commission_validation.primary
  target: column.zs_observe.walmart_settlement.sku_id
  fields:
    edge_family: dependency_usage
    evidence_basis: matching_logic SQL/template uses this documented column.
    confidence: high
    canonical_cognee_edge: true
    marketplace_only: true
    canonical_edge_type: USES_COLUMN
    inverse_edge_type: USED_BY_CARD
    materialize_inverse: false
    edge_class: canonical
    source_type: matching_logic
    target_type: column
    evidence_refs:
    - ev.walmart.reconciliation.001
    notes: matching_logic SQL/template uses this documented column.
```

```yaml
candidate_edge:
  edge_id: edge.walmart.0625
  edge_type: USES_COLUMN
  source: matching_logic.walmart.commission_validation.primary
  target: column.zs_observe.walmart_settlement.charged_amount_excluding_tax
  fields:
    edge_family: dependency_usage
    evidence_basis: matching_logic SQL/template uses this documented column.
    confidence: high
    canonical_cognee_edge: true
    marketplace_only: true
    canonical_edge_type: USES_COLUMN
    inverse_edge_type: USED_BY_CARD
    materialize_inverse: false
    edge_class: canonical
    source_type: matching_logic
    target_type: column
    evidence_refs:
    - ev.walmart.reconciliation.001
    notes: matching_logic SQL/template uses this documented column.
```

```yaml
candidate_edge:
  edge_id: edge.walmart.0626
  edge_type: USES_COLUMN
  source: matching_logic.walmart.commission_validation.primary
  target: column.zs_observe.walmart_settlement.gross_commission
  fields:
    edge_family: dependency_usage
    evidence_basis: matching_logic SQL/template uses this documented column.
    confidence: high
    canonical_cognee_edge: true
    marketplace_only: true
    canonical_edge_type: USES_COLUMN
    inverse_edge_type: USED_BY_CARD
    materialize_inverse: false
    edge_class: canonical
    source_type: matching_logic
    target_type: column
    evidence_refs:
    - ev.walmart.reconciliation.001
    notes: matching_logic SQL/template uses this documented column.
```

```yaml
candidate_edge:
  edge_id: edge.walmart.0627
  edge_type: USES_COLUMN
  source: matching_logic.walmart.commission_validation.primary
  target: column.zs_observe.walmart_settlement.product_price
  fields:
    edge_family: dependency_usage
    evidence_basis: matching_logic SQL/template uses this documented column.
    confidence: high
    canonical_cognee_edge: true
    marketplace_only: true
    canonical_edge_type: USES_COLUMN
    inverse_edge_type: USED_BY_CARD
    materialize_inverse: false
    edge_class: canonical
    source_type: matching_logic
    target_type: column
    evidence_refs:
    - ev.walmart.reconciliation.001
    notes: matching_logic SQL/template uses this documented column.
```

```yaml
candidate_edge:
  edge_id: edge.walmart.0628
  edge_type: USES_COLUMN
  source: matching_logic.walmart.commission_validation.primary
  target: column.zs_observe.walmart_settlement.transaction_type
  fields:
    edge_family: dependency_usage
    evidence_basis: matching_logic SQL/template uses this documented column.
    confidence: high
    canonical_cognee_edge: true
    marketplace_only: true
    canonical_edge_type: USES_COLUMN
    inverse_edge_type: USED_BY_CARD
    materialize_inverse: false
    edge_class: canonical
    source_type: matching_logic
    target_type: column
    evidence_refs:
    - ev.walmart.reconciliation.001
    notes: matching_logic SQL/template uses this documented column.
```

```yaml
candidate_edge:
  edge_id: edge.walmart.0629
  edge_type: USES_COLUMN
  source: matching_logic.walmart.commission_validation.primary
  target: column.zs_observe.walmart_settlement.group_level_id
  fields:
    edge_family: dependency_usage
    evidence_basis: matching_logic SQL/template uses this documented column.
    confidence: high
    canonical_cognee_edge: true
    marketplace_only: true
    canonical_edge_type: USES_COLUMN
    inverse_edge_type: USED_BY_CARD
    materialize_inverse: false
    edge_class: canonical
    source_type: matching_logic
    target_type: column
    evidence_refs:
    - ev.walmart.reconciliation.001
    notes: matching_logic SQL/template uses this documented column.
```

```yaml
candidate_edge:
  edge_id: edge.walmart.0630
  edge_type: USES_COLUMN
  source: matching_logic.walmart.commission_validation.primary
  target: column.zs_observe.walmart_settlement.is_active
  fields:
    edge_family: dependency_usage
    evidence_basis: matching_logic SQL/template uses this documented column.
    confidence: high
    canonical_cognee_edge: true
    marketplace_only: true
    canonical_edge_type: USES_COLUMN
    inverse_edge_type: USED_BY_CARD
    materialize_inverse: false
    edge_class: canonical
    source_type: matching_logic
    target_type: column
    evidence_refs:
    - ev.walmart.reconciliation.001
    notes: matching_logic SQL/template uses this documented column.
```

```yaml
candidate_edge:
  edge_id: edge.walmart.0631
  edge_type: USES_COLUMN
  source: matching_logic.walmart.refund_to_sale.primary
  target: column.zs_observe.walmart_settlement.order_id
  fields:
    edge_family: dependency_usage
    evidence_basis: matching_logic SQL/template uses this documented column.
    confidence: high
    canonical_cognee_edge: true
    marketplace_only: true
    canonical_edge_type: USES_COLUMN
    inverse_edge_type: USED_BY_CARD
    materialize_inverse: false
    edge_class: canonical
    source_type: matching_logic
    target_type: column
    evidence_refs:
    - ev.walmart.reconciliation.001
    notes: matching_logic SQL/template uses this documented column.
```

```yaml
candidate_edge:
  edge_id: edge.walmart.0632
  edge_type: USES_COLUMN
  source: matching_logic.walmart.refund_to_sale.primary
  target: column.zs_observe.walmart_settlement.sku_id
  fields:
    edge_family: dependency_usage
    evidence_basis: matching_logic SQL/template uses this documented column.
    confidence: high
    canonical_cognee_edge: true
    marketplace_only: true
    canonical_edge_type: USES_COLUMN
    inverse_edge_type: USED_BY_CARD
    materialize_inverse: false
    edge_class: canonical
    source_type: matching_logic
    target_type: column
    evidence_refs:
    - ev.walmart.reconciliation.001
    notes: matching_logic SQL/template uses this documented column.
```

```yaml
candidate_edge:
  edge_id: edge.walmart.0633
  edge_type: USES_COLUMN
  source: matching_logic.walmart.refund_to_sale.primary
  target: column.zs_observe.walmart_settlement.charged_amount
  fields:
    edge_family: dependency_usage
    evidence_basis: matching_logic SQL/template uses this documented column.
    confidence: high
    canonical_cognee_edge: true
    marketplace_only: true
    canonical_edge_type: USES_COLUMN
    inverse_edge_type: USED_BY_CARD
    materialize_inverse: false
    edge_class: canonical
    source_type: matching_logic
    target_type: column
    evidence_refs:
    - ev.walmart.reconciliation.001
    notes: matching_logic SQL/template uses this documented column.
```

```yaml
candidate_edge:
  edge_id: edge.walmart.0634
  edge_type: USES_COLUMN
  source: matching_logic.walmart.refund_to_sale.primary
  target: column.zs_observe.walmart_settlement.gross_commission
  fields:
    edge_family: dependency_usage
    evidence_basis: matching_logic SQL/template uses this documented column.
    confidence: high
    canonical_cognee_edge: true
    marketplace_only: true
    canonical_edge_type: USES_COLUMN
    inverse_edge_type: USED_BY_CARD
    materialize_inverse: false
    edge_class: canonical
    source_type: matching_logic
    target_type: column
    evidence_refs:
    - ev.walmart.reconciliation.001
    notes: matching_logic SQL/template uses this documented column.
```

```yaml
candidate_edge:
  edge_id: edge.walmart.0635
  edge_type: USES_COLUMN
  source: matching_logic.walmart.refund_to_sale.primary
  target: column.zs_observe.walmart_settlement.transaction_type
  fields:
    edge_family: dependency_usage
    evidence_basis: matching_logic SQL/template uses this documented column.
    confidence: high
    canonical_cognee_edge: true
    marketplace_only: true
    canonical_edge_type: USES_COLUMN
    inverse_edge_type: USED_BY_CARD
    materialize_inverse: false
    edge_class: canonical
    source_type: matching_logic
    target_type: column
    evidence_refs:
    - ev.walmart.reconciliation.001
    notes: matching_logic SQL/template uses this documented column.
```

```yaml
candidate_edge:
  edge_id: edge.walmart.0636
  edge_type: USES_COLUMN
  source: matching_logic.walmart.refund_to_sale.primary
  target: column.zs_observe.walmart_settlement.original_commission
  fields:
    edge_family: dependency_usage
    evidence_basis: matching_logic SQL/template uses this documented column.
    confidence: high
    canonical_cognee_edge: true
    marketplace_only: true
    canonical_edge_type: USES_COLUMN
    inverse_edge_type: USED_BY_CARD
    materialize_inverse: false
    edge_class: canonical
    source_type: matching_logic
    target_type: column
    evidence_refs:
    - ev.walmart.reconciliation.001
    notes: matching_logic SQL/template uses this documented column.
```

```yaml
candidate_edge:
  edge_id: edge.walmart.0637
  edge_type: USES_COLUMN
  source: matching_logic.walmart.refund_to_sale.primary
  target: column.zs_observe.walmart_settlement.group_level_id
  fields:
    edge_family: dependency_usage
    evidence_basis: matching_logic SQL/template uses this documented column.
    confidence: high
    canonical_cognee_edge: true
    marketplace_only: true
    canonical_edge_type: USES_COLUMN
    inverse_edge_type: USED_BY_CARD
    materialize_inverse: false
    edge_class: canonical
    source_type: matching_logic
    target_type: column
    evidence_refs:
    - ev.walmart.reconciliation.001
    notes: matching_logic SQL/template uses this documented column.
```

```yaml
candidate_edge:
  edge_id: edge.walmart.0638
  edge_type: USES_COLUMN
  source: matching_logic.walmart.refund_to_sale.primary
  target: column.zs_observe.walmart_settlement.is_active
  fields:
    edge_family: dependency_usage
    evidence_basis: matching_logic SQL/template uses this documented column.
    confidence: high
    canonical_cognee_edge: true
    marketplace_only: true
    canonical_edge_type: USES_COLUMN
    inverse_edge_type: USED_BY_CARD
    materialize_inverse: false
    edge_class: canonical
    source_type: matching_logic
    target_type: column
    evidence_refs:
    - ev.walmart.reconciliation.001
    notes: matching_logic SQL/template uses this documented column.
```

```yaml
candidate_edge:
  edge_id: edge.walmart.0639
  edge_type: USES_COLUMN
  source: matching_logic.walmart.mpf_tax_identity.primary
  target: column.zs_observe.walmart_settlement.charged_amount
  fields:
    edge_family: dependency_usage
    evidence_basis: matching_logic SQL/template uses this documented column.
    confidence: high
    canonical_cognee_edge: true
    marketplace_only: true
    canonical_edge_type: USES_COLUMN
    inverse_edge_type: USED_BY_CARD
    materialize_inverse: false
    edge_class: canonical
    source_type: matching_logic
    target_type: column
    evidence_refs:
    - ev.walmart.business_model.001
    notes: matching_logic SQL/template uses this documented column.
```

```yaml
candidate_edge:
  edge_id: edge.walmart.0640
  edge_type: USES_COLUMN
  source: matching_logic.walmart.mpf_tax_identity.primary
  target: column.zs_observe.walmart_settlement.charged_amount_excluding_tax
  fields:
    edge_family: dependency_usage
    evidence_basis: matching_logic SQL/template uses this documented column.
    confidence: high
    canonical_cognee_edge: true
    marketplace_only: true
    canonical_edge_type: USES_COLUMN
    inverse_edge_type: USED_BY_CARD
    materialize_inverse: false
    edge_class: canonical
    source_type: matching_logic
    target_type: column
    evidence_refs:
    - ev.walmart.business_model.001
    notes: matching_logic SQL/template uses this documented column.
```

```yaml
candidate_edge:
  edge_id: edge.walmart.0641
  edge_type: USES_COLUMN
  source: matching_logic.walmart.mpf_tax_identity.primary
  target: column.zs_observe.walmart_settlement.total_tax
  fields:
    edge_family: dependency_usage
    evidence_basis: matching_logic SQL/template uses this documented column.
    confidence: high
    canonical_cognee_edge: true
    marketplace_only: true
    canonical_edge_type: USES_COLUMN
    inverse_edge_type: USED_BY_CARD
    materialize_inverse: false
    edge_class: canonical
    source_type: matching_logic
    target_type: column
    evidence_refs:
    - ev.walmart.business_model.001
    notes: matching_logic SQL/template uses this documented column.
```

```yaml
candidate_edge:
  edge_id: edge.walmart.0642
  edge_type: USES_COLUMN
  source: matching_logic.walmart.mpf_tax_identity.primary
  target: column.zs_observe.walmart_settlement.marketplace_withheld_tax
  fields:
    edge_family: dependency_usage
    evidence_basis: matching_logic SQL/template uses this documented column.
    confidence: high
    canonical_cognee_edge: true
    marketplace_only: true
    canonical_edge_type: USES_COLUMN
    inverse_edge_type: USED_BY_CARD
    materialize_inverse: false
    edge_class: canonical
    source_type: matching_logic
    target_type: column
    evidence_refs:
    - ev.walmart.business_model.001
    notes: matching_logic SQL/template uses this documented column.
```

```yaml
candidate_edge:
  edge_id: edge.walmart.0643
  edge_type: USES_COLUMN
  source: matching_logic.walmart.mpf_tax_identity.primary
  target: column.zs_observe.walmart_settlement.transaction_type
  fields:
    edge_family: dependency_usage
    evidence_basis: matching_logic SQL/template uses this documented column.
    confidence: high
    canonical_cognee_edge: true
    marketplace_only: true
    canonical_edge_type: USES_COLUMN
    inverse_edge_type: USED_BY_CARD
    materialize_inverse: false
    edge_class: canonical
    source_type: matching_logic
    target_type: column
    evidence_refs:
    - ev.walmart.business_model.001
    notes: matching_logic SQL/template uses this documented column.
```

```yaml
candidate_edge:
  edge_id: edge.walmart.0644
  edge_type: USES_COLUMN
  source: matching_logic.walmart.mpf_tax_identity.primary
  target: column.zs_observe.walmart_settlement.group_level_id
  fields:
    edge_family: dependency_usage
    evidence_basis: matching_logic SQL/template uses this documented column.
    confidence: high
    canonical_cognee_edge: true
    marketplace_only: true
    canonical_edge_type: USES_COLUMN
    inverse_edge_type: USED_BY_CARD
    materialize_inverse: false
    edge_class: canonical
    source_type: matching_logic
    target_type: column
    evidence_refs:
    - ev.walmart.business_model.001
    notes: matching_logic SQL/template uses this documented column.
```

```yaml
candidate_edge:
  edge_id: edge.walmart.0645
  edge_type: USES_COLUMN
  source: matching_logic.walmart.mpf_tax_identity.primary
  target: column.zs_observe.walmart_settlement.is_active
  fields:
    edge_family: dependency_usage
    evidence_basis: matching_logic SQL/template uses this documented column.
    confidence: high
    canonical_cognee_edge: true
    marketplace_only: true
    canonical_edge_type: USES_COLUMN
    inverse_edge_type: USED_BY_CARD
    materialize_inverse: false
    edge_class: canonical
    source_type: matching_logic
    target_type: column
    evidence_refs:
    - ev.walmart.business_model.001
    notes: matching_logic SQL/template uses this documented column.
```

```yaml
candidate_edge:
  edge_id: edge.walmart.0646
  edge_type: USES_COLUMN
  source: matching_logic.walmart.lookup_coverage.primary
  target: column.zs_observe.walmart_lookup.sku_id
  fields:
    edge_family: dependency_usage
    evidence_basis: matching_logic SQL/template uses this documented column.
    confidence: high
    canonical_cognee_edge: true
    marketplace_only: true
    canonical_edge_type: USES_COLUMN
    inverse_edge_type: USED_BY_CARD
    materialize_inverse: false
    edge_class: canonical
    source_type: matching_logic
    target_type: column
    evidence_refs:
    - ev.walmart.relationships.001
    notes: matching_logic SQL/template uses this documented column.
```

```yaml
candidate_edge:
  edge_id: edge.walmart.0647
  edge_type: USES_COLUMN
  source: matching_logic.walmart.lookup_coverage.primary
  target: column.zs_observe.walmart_lookup.sku
  fields:
    edge_family: dependency_usage
    evidence_basis: matching_logic SQL/template uses this documented column.
    confidence: high
    canonical_cognee_edge: true
    marketplace_only: true
    canonical_edge_type: USES_COLUMN
    inverse_edge_type: USED_BY_CARD
    materialize_inverse: false
    edge_class: canonical
    source_type: matching_logic
    target_type: column
    evidence_refs:
    - ev.walmart.relationships.001
    notes: matching_logic SQL/template uses this documented column.
```

```yaml
candidate_edge:
  edge_id: edge.walmart.0648
  edge_type: USES_COLUMN
  source: matching_logic.walmart.lookup_coverage.primary
  target: column.zs_observe.walmart_lookup.group_level_id
  fields:
    edge_family: dependency_usage
    evidence_basis: matching_logic SQL/template uses this documented column.
    confidence: high
    canonical_cognee_edge: true
    marketplace_only: true
    canonical_edge_type: USES_COLUMN
    inverse_edge_type: USED_BY_CARD
    materialize_inverse: false
    edge_class: canonical
    source_type: matching_logic
    target_type: column
    evidence_refs:
    - ev.walmart.relationships.001
    notes: matching_logic SQL/template uses this documented column.
```

```yaml
candidate_edge:
  edge_id: edge.walmart.0649
  edge_type: USES_COLUMN
  source: matching_logic.walmart.lookup_coverage.primary
  target: column.zs_observe.walmart_lookup.is_active
  fields:
    edge_family: dependency_usage
    evidence_basis: matching_logic SQL/template uses this documented column.
    confidence: high
    canonical_cognee_edge: true
    marketplace_only: true
    canonical_edge_type: USES_COLUMN
    inverse_edge_type: USED_BY_CARD
    materialize_inverse: false
    edge_class: canonical
    source_type: matching_logic
    target_type: column
    evidence_refs:
    - ev.walmart.relationships.001
    notes: matching_logic SQL/template uses this documented column.
```

```yaml
candidate_edge:
  edge_id: edge.walmart.0650
  edge_type: USES_COLUMN
  source: validation_test.walmart.no_settled_amount_payout
  target: column.zs_observe.walmart_settlement.order_id
  fields:
    edge_family: dependency_usage
    evidence_basis: validation_test SQL/template uses this documented column.
    confidence: high
    canonical_cognee_edge: true
    marketplace_only: true
    canonical_edge_type: USES_COLUMN
    inverse_edge_type: USED_BY_CARD
    materialize_inverse: false
    edge_class: canonical
    source_type: validation_test
    target_type: column
    evidence_refs:
    - ev.walmart.business_model.001
    notes: validation_test SQL/template uses this documented column.
```

```yaml
candidate_edge:
  edge_id: edge.walmart.0651
  edge_type: USES_COLUMN
  source: validation_test.walmart.no_settled_amount_payout
  target: column.zs_observe.walmart_settlement.metadata_2
  fields:
    edge_family: dependency_usage
    evidence_basis: validation_test SQL/template uses this documented column.
    confidence: high
    canonical_cognee_edge: true
    marketplace_only: true
    canonical_edge_type: USES_COLUMN
    inverse_edge_type: USED_BY_CARD
    materialize_inverse: false
    edge_class: canonical
    source_type: validation_test
    target_type: column
    evidence_refs:
    - ev.walmart.business_model.001
    notes: validation_test SQL/template uses this documented column.
```

```yaml
candidate_edge:
  edge_id: edge.walmart.0652
  edge_type: USES_COLUMN
  source: validation_test.walmart.no_settled_amount_payout
  target: column.zs_observe.walmart_settlement.metadata_3
  fields:
    edge_family: dependency_usage
    evidence_basis: validation_test SQL/template uses this documented column.
    confidence: high
    canonical_cognee_edge: true
    marketplace_only: true
    canonical_edge_type: USES_COLUMN
    inverse_edge_type: USED_BY_CARD
    materialize_inverse: false
    edge_class: canonical
    source_type: validation_test
    target_type: column
    evidence_refs:
    - ev.walmart.business_model.001
    notes: validation_test SQL/template uses this documented column.
```

```yaml
candidate_edge:
  edge_id: edge.walmart.0653
  edge_type: USES_COLUMN
  source: validation_test.walmart.no_settled_amount_payout
  target: column.zs_observe.walmart_settlement.charged_amount_excluding_tax
  fields:
    edge_family: dependency_usage
    evidence_basis: validation_test SQL/template uses this documented column.
    confidence: high
    canonical_cognee_edge: true
    marketplace_only: true
    canonical_edge_type: USES_COLUMN
    inverse_edge_type: USED_BY_CARD
    materialize_inverse: false
    edge_class: canonical
    source_type: validation_test
    target_type: column
    evidence_refs:
    - ev.walmart.business_model.001
    notes: validation_test SQL/template uses this documented column.
```

```yaml
candidate_edge:
  edge_id: edge.walmart.0654
  edge_type: USES_COLUMN
  source: validation_test.walmart.no_settled_amount_payout
  target: column.zs_observe.walmart_settlement.gross_commission
  fields:
    edge_family: dependency_usage
    evidence_basis: validation_test SQL/template uses this documented column.
    confidence: high
    canonical_cognee_edge: true
    marketplace_only: true
    canonical_edge_type: USES_COLUMN
    inverse_edge_type: USED_BY_CARD
    materialize_inverse: false
    edge_class: canonical
    source_type: validation_test
    target_type: column
    evidence_refs:
    - ev.walmart.business_model.001
    notes: validation_test SQL/template uses this documented column.
```

```yaml
candidate_edge:
  edge_id: edge.walmart.0655
  edge_type: USES_COLUMN
  source: validation_test.walmart.no_settled_amount_payout
  target: column.zs_observe.walmart_settlement.settled_amount
  fields:
    edge_family: dependency_usage
    evidence_basis: validation_test SQL/template uses this documented column.
    confidence: high
    canonical_cognee_edge: true
    marketplace_only: true
    canonical_edge_type: USES_COLUMN
    inverse_edge_type: USED_BY_CARD
    materialize_inverse: false
    edge_class: canonical
    source_type: validation_test
    target_type: column
    evidence_refs:
    - ev.walmart.business_model.001
    notes: validation_test SQL/template uses this documented column.
```

```yaml
candidate_edge:
  edge_id: edge.walmart.0656
  edge_type: USES_COLUMN
  source: validation_test.walmart.no_settled_amount_payout
  target: column.zs_observe.walmart_settlement.total_walmart_funded_savings
  fields:
    edge_family: dependency_usage
    evidence_basis: validation_test SQL/template uses this documented column.
    confidence: high
    canonical_cognee_edge: true
    marketplace_only: true
    canonical_edge_type: USES_COLUMN
    inverse_edge_type: USED_BY_CARD
    materialize_inverse: false
    edge_class: canonical
    source_type: validation_test
    target_type: column
    evidence_refs:
    - ev.walmart.business_model.001
    notes: validation_test SQL/template uses this documented column.
```

```yaml
candidate_edge:
  edge_id: edge.walmart.0657
  edge_type: USES_COLUMN
  source: validation_test.walmart.no_settled_amount_payout
  target: column.zs_observe.walmart_settlement.transaction_type
  fields:
    edge_family: dependency_usage
    evidence_basis: validation_test SQL/template uses this documented column.
    confidence: high
    canonical_cognee_edge: true
    marketplace_only: true
    canonical_edge_type: USES_COLUMN
    inverse_edge_type: USED_BY_CARD
    materialize_inverse: false
    edge_class: canonical
    source_type: validation_test
    target_type: column
    evidence_refs:
    - ev.walmart.business_model.001
    notes: validation_test SQL/template uses this documented column.
```

```yaml
candidate_edge:
  edge_id: edge.walmart.0658
  edge_type: USES_COLUMN
  source: validation_test.walmart.no_settled_amount_payout
  target: column.zs_observe.walmart_settlement.group_level_id
  fields:
    edge_family: dependency_usage
    evidence_basis: validation_test SQL/template uses this documented column.
    confidence: high
    canonical_cognee_edge: true
    marketplace_only: true
    canonical_edge_type: USES_COLUMN
    inverse_edge_type: USED_BY_CARD
    materialize_inverse: false
    edge_class: canonical
    source_type: validation_test
    target_type: column
    evidence_refs:
    - ev.walmart.business_model.001
    notes: validation_test SQL/template uses this documented column.
```

```yaml
candidate_edge:
  edge_id: edge.walmart.0659
  edge_type: USES_COLUMN
  source: validation_test.walmart.no_settled_amount_payout
  target: column.zs_observe.walmart_settlement.is_active
  fields:
    edge_family: dependency_usage
    evidence_basis: validation_test SQL/template uses this documented column.
    confidence: high
    canonical_cognee_edge: true
    marketplace_only: true
    canonical_edge_type: USES_COLUMN
    inverse_edge_type: USED_BY_CARD
    materialize_inverse: false
    edge_class: canonical
    source_type: validation_test
    target_type: column
    evidence_refs:
    - ev.walmart.business_model.001
    notes: validation_test SQL/template uses this documented column.
```

```yaml
candidate_edge:
  edge_id: edge.walmart.0660
  edge_type: USES_COLUMN
  source: validation_test.walmart.mandatory_filters
  target: column.zs_observe.walmart_oms.order_status
  fields:
    edge_family: dependency_usage
    evidence_basis: validation_test SQL/template uses this documented column.
    confidence: high
    canonical_cognee_edge: true
    marketplace_only: true
    canonical_edge_type: USES_COLUMN
    inverse_edge_type: USED_BY_CARD
    materialize_inverse: false
    edge_class: canonical
    source_type: validation_test
    target_type: column
    evidence_refs:
    - ev.walmart.filters.001
    notes: validation_test SQL/template uses this documented column.
```

```yaml
candidate_edge:
  edge_id: edge.walmart.0661
  edge_type: USES_COLUMN
  source: validation_test.walmart.mandatory_filters
  target: column.zs_observe.walmart_oms.destination_state
  fields:
    edge_family: dependency_usage
    evidence_basis: validation_test SQL/template uses this documented column.
    confidence: high
    canonical_cognee_edge: true
    marketplace_only: true
    canonical_edge_type: USES_COLUMN
    inverse_edge_type: USED_BY_CARD
    materialize_inverse: false
    edge_class: canonical
    source_type: validation_test
    target_type: column
    evidence_refs:
    - ev.walmart.filters.001
    notes: validation_test SQL/template uses this documented column.
```

```yaml
candidate_edge:
  edge_id: edge.walmart.0662
  edge_type: USES_COLUMN
  source: validation_test.walmart.mandatory_filters
  target: column.zs_observe.walmart_oms.group_level_id
  fields:
    edge_family: dependency_usage
    evidence_basis: validation_test SQL/template uses this documented column.
    confidence: high
    canonical_cognee_edge: true
    marketplace_only: true
    canonical_edge_type: USES_COLUMN
    inverse_edge_type: USED_BY_CARD
    materialize_inverse: false
    edge_class: canonical
    source_type: validation_test
    target_type: column
    evidence_refs:
    - ev.walmart.filters.001
    notes: validation_test SQL/template uses this documented column.
```

```yaml
candidate_edge:
  edge_id: edge.walmart.0663
  edge_type: USES_COLUMN
  source: validation_test.walmart.mandatory_filters
  target: column.zs_observe.walmart_oms.currency_type
  fields:
    edge_family: dependency_usage
    evidence_basis: validation_test SQL/template uses this documented column.
    confidence: high
    canonical_cognee_edge: true
    marketplace_only: true
    canonical_edge_type: USES_COLUMN
    inverse_edge_type: USED_BY_CARD
    materialize_inverse: false
    edge_class: canonical
    source_type: validation_test
    target_type: column
    evidence_refs:
    - ev.walmart.filters.001
    notes: validation_test SQL/template uses this documented column.
```

```yaml
candidate_edge:
  edge_id: edge.walmart.0664
  edge_type: USES_COLUMN
  source: validation_test.walmart.mandatory_filters
  target: column.zs_observe.walmart_oms.is_active
  fields:
    edge_family: dependency_usage
    evidence_basis: validation_test SQL/template uses this documented column.
    confidence: high
    canonical_cognee_edge: true
    marketplace_only: true
    canonical_edge_type: USES_COLUMN
    inverse_edge_type: USED_BY_CARD
    materialize_inverse: false
    edge_class: canonical
    source_type: validation_test
    target_type: column
    evidence_refs:
    - ev.walmart.filters.001
    notes: validation_test SQL/template uses this documented column.
```

```yaml
candidate_edge:
  edge_id: edge.walmart.0665
  edge_type: USES_COLUMN
  source: validation_test.walmart.lookup_sku_not_null
  target: column.zs_observe.walmart_lookup.sku
  fields:
    edge_family: dependency_usage
    evidence_basis: validation_test SQL/template uses this documented column.
    confidence: high
    canonical_cognee_edge: true
    marketplace_only: true
    canonical_edge_type: USES_COLUMN
    inverse_edge_type: USED_BY_CARD
    materialize_inverse: false
    edge_class: canonical
    source_type: validation_test
    target_type: column
    evidence_refs:
    - ev.walmart_lookup.schema.001
    notes: validation_test SQL/template uses this documented column.
```

```yaml
candidate_edge:
  edge_id: edge.walmart.0666
  edge_type: USES_COLUMN
  source: validation_test.walmart.lookup_sku_not_null
  target: column.zs_observe.walmart_lookup.group_level_id
  fields:
    edge_family: dependency_usage
    evidence_basis: validation_test SQL/template uses this documented column.
    confidence: high
    canonical_cognee_edge: true
    marketplace_only: true
    canonical_edge_type: USES_COLUMN
    inverse_edge_type: USED_BY_CARD
    materialize_inverse: false
    edge_class: canonical
    source_type: validation_test
    target_type: column
    evidence_refs:
    - ev.walmart_lookup.schema.001
    notes: validation_test SQL/template uses this documented column.
```

```yaml
candidate_edge:
  edge_id: edge.walmart.0667
  edge_type: USES_COLUMN
  source: validation_test.walmart.lookup_sku_not_null
  target: column.zs_observe.walmart_lookup.is_active
  fields:
    edge_family: dependency_usage
    evidence_basis: validation_test SQL/template uses this documented column.
    confidence: high
    canonical_cognee_edge: true
    marketplace_only: true
    canonical_edge_type: USES_COLUMN
    inverse_edge_type: USED_BY_CARD
    materialize_inverse: false
    edge_class: canonical
    source_type: validation_test
    target_type: column
    evidence_refs:
    - ev.walmart_lookup.schema.001
    notes: validation_test SQL/template uses this documented column.
```

```yaml
candidate_edge:
  edge_id: edge.walmart.0668
  edge_type: USES_COLUMN
  source: validation_test.walmart.mpf_tax_identity
  target: column.zs_observe.walmart_settlement.charged_amount
  fields:
    edge_family: dependency_usage
    evidence_basis: validation_test SQL/template uses this documented column.
    confidence: high
    canonical_cognee_edge: true
    marketplace_only: true
    canonical_edge_type: USES_COLUMN
    inverse_edge_type: USED_BY_CARD
    materialize_inverse: false
    edge_class: canonical
    source_type: validation_test
    target_type: column
    evidence_refs:
    - ev.walmart.business_model.001
    notes: validation_test SQL/template uses this documented column.
```

```yaml
candidate_edge:
  edge_id: edge.walmart.0669
  edge_type: USES_COLUMN
  source: validation_test.walmart.mpf_tax_identity
  target: column.zs_observe.walmart_settlement.charged_amount_excluding_tax
  fields:
    edge_family: dependency_usage
    evidence_basis: validation_test SQL/template uses this documented column.
    confidence: high
    canonical_cognee_edge: true
    marketplace_only: true
    canonical_edge_type: USES_COLUMN
    inverse_edge_type: USED_BY_CARD
    materialize_inverse: false
    edge_class: canonical
    source_type: validation_test
    target_type: column
    evidence_refs:
    - ev.walmart.business_model.001
    notes: validation_test SQL/template uses this documented column.
```

```yaml
candidate_edge:
  edge_id: edge.walmart.0670
  edge_type: USES_COLUMN
  source: validation_test.walmart.mpf_tax_identity
  target: column.zs_observe.walmart_settlement.total_tax
  fields:
    edge_family: dependency_usage
    evidence_basis: validation_test SQL/template uses this documented column.
    confidence: high
    canonical_cognee_edge: true
    marketplace_only: true
    canonical_edge_type: USES_COLUMN
    inverse_edge_type: USED_BY_CARD
    materialize_inverse: false
    edge_class: canonical
    source_type: validation_test
    target_type: column
    evidence_refs:
    - ev.walmart.business_model.001
    notes: validation_test SQL/template uses this documented column.
```

```yaml
candidate_edge:
  edge_id: edge.walmart.0671
  edge_type: USES_COLUMN
  source: validation_test.walmart.mpf_tax_identity
  target: column.zs_observe.walmart_settlement.marketplace_withheld_tax
  fields:
    edge_family: dependency_usage
    evidence_basis: validation_test SQL/template uses this documented column.
    confidence: high
    canonical_cognee_edge: true
    marketplace_only: true
    canonical_edge_type: USES_COLUMN
    inverse_edge_type: USED_BY_CARD
    materialize_inverse: false
    edge_class: canonical
    source_type: validation_test
    target_type: column
    evidence_refs:
    - ev.walmart.business_model.001
    notes: validation_test SQL/template uses this documented column.
```

```yaml
candidate_edge:
  edge_id: edge.walmart.0672
  edge_type: USES_COLUMN
  source: validation_test.walmart.mpf_tax_identity
  target: column.zs_observe.walmart_settlement.transaction_type
  fields:
    edge_family: dependency_usage
    evidence_basis: validation_test SQL/template uses this documented column.
    confidence: high
    canonical_cognee_edge: true
    marketplace_only: true
    canonical_edge_type: USES_COLUMN
    inverse_edge_type: USED_BY_CARD
    materialize_inverse: false
    edge_class: canonical
    source_type: validation_test
    target_type: column
    evidence_refs:
    - ev.walmart.business_model.001
    notes: validation_test SQL/template uses this documented column.
```

```yaml
candidate_edge:
  edge_id: edge.walmart.0673
  edge_type: USES_COLUMN
  source: validation_test.walmart.mpf_tax_identity
  target: column.zs_observe.walmart_settlement.group_level_id
  fields:
    edge_family: dependency_usage
    evidence_basis: validation_test SQL/template uses this documented column.
    confidence: high
    canonical_cognee_edge: true
    marketplace_only: true
    canonical_edge_type: USES_COLUMN
    inverse_edge_type: USED_BY_CARD
    materialize_inverse: false
    edge_class: canonical
    source_type: validation_test
    target_type: column
    evidence_refs:
    - ev.walmart.business_model.001
    notes: validation_test SQL/template uses this documented column.
```

```yaml
candidate_edge:
  edge_id: edge.walmart.0674
  edge_type: USES_COLUMN
  source: validation_test.walmart.mpf_tax_identity
  target: column.zs_observe.walmart_settlement.is_active
  fields:
    edge_family: dependency_usage
    evidence_basis: validation_test SQL/template uses this documented column.
    confidence: high
    canonical_cognee_edge: true
    marketplace_only: true
    canonical_edge_type: USES_COLUMN
    inverse_edge_type: USED_BY_CARD
    materialize_inverse: false
    edge_class: canonical
    source_type: validation_test
    target_type: column
    evidence_refs:
    - ev.walmart.business_model.001
    notes: validation_test SQL/template uses this documented column.
```

```yaml
candidate_edge:
  edge_id: edge.walmart.0675
  edge_type: USES_COLUMN
  source: validation_test.walmart.commission_rate_computed
  target: column.zs_observe.walmart_settlement.order_id
  fields:
    edge_family: dependency_usage
    evidence_basis: validation_test SQL/template uses this documented column.
    confidence: high
    canonical_cognee_edge: true
    marketplace_only: true
    canonical_edge_type: USES_COLUMN
    inverse_edge_type: USED_BY_CARD
    materialize_inverse: false
    edge_class: canonical
    source_type: validation_test
    target_type: column
    evidence_refs:
    - ev.walmart.quality.001
    notes: validation_test SQL/template uses this documented column.
```

```yaml
candidate_edge:
  edge_id: edge.walmart.0676
  edge_type: USES_COLUMN
  source: validation_test.walmart.commission_rate_computed
  target: column.zs_observe.walmart_settlement.sku_id
  fields:
    edge_family: dependency_usage
    evidence_basis: validation_test SQL/template uses this documented column.
    confidence: high
    canonical_cognee_edge: true
    marketplace_only: true
    canonical_edge_type: USES_COLUMN
    inverse_edge_type: USED_BY_CARD
    materialize_inverse: false
    edge_class: canonical
    source_type: validation_test
    target_type: column
    evidence_refs:
    - ev.walmart.quality.001
    notes: validation_test SQL/template uses this documented column.
```

```yaml
candidate_edge:
  edge_id: edge.walmart.0677
  edge_type: USES_COLUMN
  source: validation_test.walmart.commission_rate_computed
  target: column.zs_observe.walmart_settlement.charged_amount_excluding_tax
  fields:
    edge_family: dependency_usage
    evidence_basis: validation_test SQL/template uses this documented column.
    confidence: high
    canonical_cognee_edge: true
    marketplace_only: true
    canonical_edge_type: USES_COLUMN
    inverse_edge_type: USED_BY_CARD
    materialize_inverse: false
    edge_class: canonical
    source_type: validation_test
    target_type: column
    evidence_refs:
    - ev.walmart.quality.001
    notes: validation_test SQL/template uses this documented column.
```

```yaml
candidate_edge:
  edge_id: edge.walmart.0678
  edge_type: USES_COLUMN
  source: validation_test.walmart.commission_rate_computed
  target: column.zs_observe.walmart_settlement.gross_commission
  fields:
    edge_family: dependency_usage
    evidence_basis: validation_test SQL/template uses this documented column.
    confidence: high
    canonical_cognee_edge: true
    marketplace_only: true
    canonical_edge_type: USES_COLUMN
    inverse_edge_type: USED_BY_CARD
    materialize_inverse: false
    edge_class: canonical
    source_type: validation_test
    target_type: column
    evidence_refs:
    - ev.walmart.quality.001
    notes: validation_test SQL/template uses this documented column.
```

```yaml
candidate_edge:
  edge_id: edge.walmart.0679
  edge_type: USES_COLUMN
  source: validation_test.walmart.commission_rate_computed
  target: column.zs_observe.walmart_settlement.product_price
  fields:
    edge_family: dependency_usage
    evidence_basis: validation_test SQL/template uses this documented column.
    confidence: high
    canonical_cognee_edge: true
    marketplace_only: true
    canonical_edge_type: USES_COLUMN
    inverse_edge_type: USED_BY_CARD
    materialize_inverse: false
    edge_class: canonical
    source_type: validation_test
    target_type: column
    evidence_refs:
    - ev.walmart.quality.001
    notes: validation_test SQL/template uses this documented column.
```

```yaml
candidate_edge:
  edge_id: edge.walmart.0680
  edge_type: USES_COLUMN
  source: validation_test.walmart.commission_rate_computed
  target: column.zs_observe.walmart_settlement.transaction_type
  fields:
    edge_family: dependency_usage
    evidence_basis: validation_test SQL/template uses this documented column.
    confidence: high
    canonical_cognee_edge: true
    marketplace_only: true
    canonical_edge_type: USES_COLUMN
    inverse_edge_type: USED_BY_CARD
    materialize_inverse: false
    edge_class: canonical
    source_type: validation_test
    target_type: column
    evidence_refs:
    - ev.walmart.quality.001
    notes: validation_test SQL/template uses this documented column.
```

```yaml
candidate_edge:
  edge_id: edge.walmart.0681
  edge_type: USES_COLUMN
  source: validation_test.walmart.commission_rate_computed
  target: column.zs_observe.walmart_settlement.group_level_id
  fields:
    edge_family: dependency_usage
    evidence_basis: validation_test SQL/template uses this documented column.
    confidence: high
    canonical_cognee_edge: true
    marketplace_only: true
    canonical_edge_type: USES_COLUMN
    inverse_edge_type: USED_BY_CARD
    materialize_inverse: false
    edge_class: canonical
    source_type: validation_test
    target_type: column
    evidence_refs:
    - ev.walmart.quality.001
    notes: validation_test SQL/template uses this documented column.
```

```yaml
candidate_edge:
  edge_id: edge.walmart.0682
  edge_type: USES_COLUMN
  source: validation_test.walmart.commission_rate_computed
  target: column.zs_observe.walmart_settlement.is_active
  fields:
    edge_family: dependency_usage
    evidence_basis: validation_test SQL/template uses this documented column.
    confidence: high
    canonical_cognee_edge: true
    marketplace_only: true
    canonical_edge_type: USES_COLUMN
    inverse_edge_type: USED_BY_CARD
    materialize_inverse: false
    edge_class: canonical
    source_type: validation_test
    target_type: column
    evidence_refs:
    - ev.walmart.quality.001
    notes: validation_test SQL/template uses this documented column.
```

```yaml
candidate_edge:
  edge_id: edge.walmart.0683
  edge_type: USES_COLUMN
  source: validation_test.walmart.no_indian_tax_cards
  target: column.zs_observe.walmart_settlement.charged_amount
  fields:
    edge_family: dependency_usage
    evidence_basis: validation_test SQL/template uses this documented column.
    confidence: high
    canonical_cognee_edge: true
    marketplace_only: true
    canonical_edge_type: USES_COLUMN
    inverse_edge_type: USED_BY_CARD
    materialize_inverse: false
    edge_class: canonical
    source_type: validation_test
    target_type: column
    evidence_refs:
    - ev.walmart.business_model.001
    notes: validation_test SQL/template uses this documented column.
```

```yaml
candidate_edge:
  edge_id: edge.walmart.0684
  edge_type: USES_COLUMN
  source: validation_test.walmart.no_indian_tax_cards
  target: column.zs_observe.walmart_settlement.charged_amount_excluding_tax
  fields:
    edge_family: dependency_usage
    evidence_basis: validation_test SQL/template uses this documented column.
    confidence: high
    canonical_cognee_edge: true
    marketplace_only: true
    canonical_edge_type: USES_COLUMN
    inverse_edge_type: USED_BY_CARD
    materialize_inverse: false
    edge_class: canonical
    source_type: validation_test
    target_type: column
    evidence_refs:
    - ev.walmart.business_model.001
    notes: validation_test SQL/template uses this documented column.
```

```yaml
candidate_edge:
  edge_id: edge.walmart.0685
  edge_type: USES_COLUMN
  source: validation_test.walmart.no_indian_tax_cards
  target: column.zs_observe.walmart_settlement.total_tax
  fields:
    edge_family: dependency_usage
    evidence_basis: validation_test SQL/template uses this documented column.
    confidence: high
    canonical_cognee_edge: true
    marketplace_only: true
    canonical_edge_type: USES_COLUMN
    inverse_edge_type: USED_BY_CARD
    materialize_inverse: false
    edge_class: canonical
    source_type: validation_test
    target_type: column
    evidence_refs:
    - ev.walmart.business_model.001
    notes: validation_test SQL/template uses this documented column.
```

```yaml
candidate_edge:
  edge_id: edge.walmart.0686
  edge_type: USES_COLUMN
  source: validation_test.walmart.no_indian_tax_cards
  target: column.zs_observe.walmart_settlement.marketplace_withheld_tax
  fields:
    edge_family: dependency_usage
    evidence_basis: validation_test SQL/template uses this documented column.
    confidence: high
    canonical_cognee_edge: true
    marketplace_only: true
    canonical_edge_type: USES_COLUMN
    inverse_edge_type: USED_BY_CARD
    materialize_inverse: false
    edge_class: canonical
    source_type: validation_test
    target_type: column
    evidence_refs:
    - ev.walmart.business_model.001
    notes: validation_test SQL/template uses this documented column.
```

```yaml
candidate_edge:
  edge_id: edge.walmart.0687
  edge_type: USES_COLUMN
  source: validation_test.walmart.no_indian_tax_cards
  target: column.zs_observe.walmart_settlement.transaction_type
  fields:
    edge_family: dependency_usage
    evidence_basis: validation_test SQL/template uses this documented column.
    confidence: high
    canonical_cognee_edge: true
    marketplace_only: true
    canonical_edge_type: USES_COLUMN
    inverse_edge_type: USED_BY_CARD
    materialize_inverse: false
    edge_class: canonical
    source_type: validation_test
    target_type: column
    evidence_refs:
    - ev.walmart.business_model.001
    notes: validation_test SQL/template uses this documented column.
```

```yaml
candidate_edge:
  edge_id: edge.walmart.0688
  edge_type: USES_COLUMN
  source: validation_test.walmart.no_indian_tax_cards
  target: column.zs_observe.walmart_settlement.group_level_id
  fields:
    edge_family: dependency_usage
    evidence_basis: validation_test SQL/template uses this documented column.
    confidence: high
    canonical_cognee_edge: true
    marketplace_only: true
    canonical_edge_type: USES_COLUMN
    inverse_edge_type: USED_BY_CARD
    materialize_inverse: false
    edge_class: canonical
    source_type: validation_test
    target_type: column
    evidence_refs:
    - ev.walmart.business_model.001
    notes: validation_test SQL/template uses this documented column.
```

```yaml
candidate_edge:
  edge_id: edge.walmart.0689
  edge_type: USES_COLUMN
  source: validation_test.walmart.no_indian_tax_cards
  target: column.zs_observe.walmart_settlement.is_active
  fields:
    edge_family: dependency_usage
    evidence_basis: validation_test SQL/template uses this documented column.
    confidence: high
    canonical_cognee_edge: true
    marketplace_only: true
    canonical_edge_type: USES_COLUMN
    inverse_edge_type: USED_BY_CARD
    materialize_inverse: false
    edge_class: canonical
    source_type: validation_test
    target_type: column
    evidence_refs:
    - ev.walmart.business_model.001
    notes: validation_test SQL/template uses this documented column.
```

```yaml
candidate_edge:
  edge_id: edge.walmart.0690
  edge_type: USES_COLUMN
  source: validation_test.walmart.oms_clean_rows
  target: column.zs_observe.walmart_oms.order_status
  fields:
    edge_family: dependency_usage
    evidence_basis: validation_test SQL/template uses this documented column.
    confidence: high
    canonical_cognee_edge: true
    marketplace_only: true
    canonical_edge_type: USES_COLUMN
    inverse_edge_type: USED_BY_CARD
    materialize_inverse: false
    edge_class: canonical
    source_type: validation_test
    target_type: column
    evidence_refs:
    - ev.walmart_oms.quality.001
    notes: validation_test SQL/template uses this documented column.
```

```yaml
candidate_edge:
  edge_id: edge.walmart.0691
  edge_type: USES_COLUMN
  source: validation_test.walmart.oms_clean_rows
  target: column.zs_observe.walmart_oms.destination_state
  fields:
    edge_family: dependency_usage
    evidence_basis: validation_test SQL/template uses this documented column.
    confidence: high
    canonical_cognee_edge: true
    marketplace_only: true
    canonical_edge_type: USES_COLUMN
    inverse_edge_type: USED_BY_CARD
    materialize_inverse: false
    edge_class: canonical
    source_type: validation_test
    target_type: column
    evidence_refs:
    - ev.walmart_oms.quality.001
    notes: validation_test SQL/template uses this documented column.
```

```yaml
candidate_edge:
  edge_id: edge.walmart.0692
  edge_type: USES_COLUMN
  source: validation_test.walmart.oms_clean_rows
  target: column.zs_observe.walmart_oms.group_level_id
  fields:
    edge_family: dependency_usage
    evidence_basis: validation_test SQL/template uses this documented column.
    confidence: high
    canonical_cognee_edge: true
    marketplace_only: true
    canonical_edge_type: USES_COLUMN
    inverse_edge_type: USED_BY_CARD
    materialize_inverse: false
    edge_class: canonical
    source_type: validation_test
    target_type: column
    evidence_refs:
    - ev.walmart_oms.quality.001
    notes: validation_test SQL/template uses this documented column.
```

```yaml
candidate_edge:
  edge_id: edge.walmart.0693
  edge_type: USES_COLUMN
  source: validation_test.walmart.oms_clean_rows
  target: column.zs_observe.walmart_oms.currency_type
  fields:
    edge_family: dependency_usage
    evidence_basis: validation_test SQL/template uses this documented column.
    confidence: high
    canonical_cognee_edge: true
    marketplace_only: true
    canonical_edge_type: USES_COLUMN
    inverse_edge_type: USED_BY_CARD
    materialize_inverse: false
    edge_class: canonical
    source_type: validation_test
    target_type: column
    evidence_refs:
    - ev.walmart_oms.quality.001
    notes: validation_test SQL/template uses this documented column.
```

```yaml
candidate_edge:
  edge_id: edge.walmart.0694
  edge_type: USES_COLUMN
  source: validation_test.walmart.oms_clean_rows
  target: column.zs_observe.walmart_oms.is_active
  fields:
    edge_family: dependency_usage
    evidence_basis: validation_test SQL/template uses this documented column.
    confidence: high
    canonical_cognee_edge: true
    marketplace_only: true
    canonical_edge_type: USES_COLUMN
    inverse_edge_type: USED_BY_CARD
    materialize_inverse: false
    edge_class: canonical
    source_type: validation_test
    target_type: column
    evidence_refs:
    - ev.walmart_oms.quality.001
    notes: validation_test SQL/template uses this documented column.
```

```yaml
candidate_edge:
  edge_id: edge.walmart.0695
  edge_type: USES_COLUMN
  source: validation_test.walmart.no_process_variants
  target: column.zs_observe.walmart_settlement.wfs_inventory_fee_reimbursement
  fields:
    edge_family: dependency_usage
    evidence_basis: validation_test SQL/template uses this documented column.
    confidence: high
    canonical_cognee_edge: true
    marketplace_only: true
    canonical_edge_type: USES_COLUMN
    inverse_edge_type: USED_BY_CARD
    materialize_inverse: false
    edge_class: canonical
    source_type: validation_test
    target_type: column
    evidence_refs:
    - ev.walmart.overview.001
    notes: validation_test SQL/template uses this documented column.
```

```yaml
candidate_edge:
  edge_id: edge.walmart.0696
  edge_type: USES_COLUMN
  source: validation_test.walmart.no_process_variants
  target: column.zs_observe.walmart_settlement.fee_reimbursement
  fields:
    edge_family: dependency_usage
    evidence_basis: validation_test SQL/template uses this documented column.
    confidence: high
    canonical_cognee_edge: true
    marketplace_only: true
    canonical_edge_type: USES_COLUMN
    inverse_edge_type: USED_BY_CARD
    materialize_inverse: false
    edge_class: canonical
    source_type: validation_test
    target_type: column
    evidence_refs:
    - ev.walmart.overview.001
    notes: validation_test SQL/template uses this documented column.
```

```yaml
candidate_edge:
  edge_id: edge.walmart.0697
  edge_type: USES_COLUMN
  source: validation_test.walmart.no_process_variants
  target: column.zs_observe.walmart_settlement.wfs_fee_reimbursement
  fields:
    edge_family: dependency_usage
    evidence_basis: validation_test SQL/template uses this documented column.
    confidence: high
    canonical_cognee_edge: true
    marketplace_only: true
    canonical_edge_type: USES_COLUMN
    inverse_edge_type: USED_BY_CARD
    materialize_inverse: false
    edge_class: canonical
    source_type: validation_test
    target_type: column
    evidence_refs:
    - ev.walmart.overview.001
    notes: validation_test SQL/template uses this documented column.
```

```yaml
candidate_edge:
  edge_id: edge.walmart.0698
  edge_type: USES_COLUMN
  source: validation_test.walmart.no_process_variants
  target: column.zs_observe.walmart_settlement.wfs_inbound_fee
  fields:
    edge_family: dependency_usage
    evidence_basis: validation_test SQL/template uses this documented column.
    confidence: high
    canonical_cognee_edge: true
    marketplace_only: true
    canonical_edge_type: USES_COLUMN
    inverse_edge_type: USED_BY_CARD
    materialize_inverse: false
    edge_class: canonical
    source_type: validation_test
    target_type: column
    evidence_refs:
    - ev.walmart.overview.001
    notes: validation_test SQL/template uses this documented column.
```

```yaml
candidate_edge:
  edge_id: edge.walmart.0699
  edge_type: USES_COLUMN
  source: validation_test.walmart.no_process_variants
  target: column.zs_observe.walmart_settlement.sem_marketing_fee
  fields:
    edge_family: dependency_usage
    evidence_basis: validation_test SQL/template uses this documented column.
    confidence: high
    canonical_cognee_edge: true
    marketplace_only: true
    canonical_edge_type: USES_COLUMN
    inverse_edge_type: USED_BY_CARD
    materialize_inverse: false
    edge_class: canonical
    source_type: validation_test
    target_type: column
    evidence_refs:
    - ev.walmart.overview.001
    notes: validation_test SQL/template uses this documented column.
```

```yaml
candidate_edge:
  edge_id: edge.walmart.0700
  edge_type: USES_COLUMN
  source: validation_test.walmart.no_process_variants
  target: column.zs_observe.walmart_settlement.product_type
  fields:
    edge_family: dependency_usage
    evidence_basis: validation_test SQL/template uses this documented column.
    confidence: high
    canonical_cognee_edge: true
    marketplace_only: true
    canonical_edge_type: USES_COLUMN
    inverse_edge_type: USED_BY_CARD
    materialize_inverse: false
    edge_class: canonical
    source_type: validation_test
    target_type: column
    evidence_refs:
    - ev.walmart.overview.001
    notes: validation_test SQL/template uses this documented column.
```

```yaml
candidate_edge:
  edge_id: edge.walmart.0701
  edge_type: USES_COLUMN
  source: validation_test.walmart.no_process_variants
  target: column.zs_observe.walmart_settlement.group_level_id
  fields:
    edge_family: dependency_usage
    evidence_basis: validation_test SQL/template uses this documented column.
    confidence: high
    canonical_cognee_edge: true
    marketplace_only: true
    canonical_edge_type: USES_COLUMN
    inverse_edge_type: USED_BY_CARD
    materialize_inverse: false
    edge_class: canonical
    source_type: validation_test
    target_type: column
    evidence_refs:
    - ev.walmart.overview.001
    notes: validation_test SQL/template uses this documented column.
```

```yaml
candidate_edge:
  edge_id: edge.walmart.0702
  edge_type: USES_COLUMN
  source: validation_test.walmart.no_process_variants
  target: column.zs_observe.walmart_settlement.is_active
  fields:
    edge_family: dependency_usage
    evidence_basis: validation_test SQL/template uses this documented column.
    confidence: high
    canonical_cognee_edge: true
    marketplace_only: true
    canonical_edge_type: USES_COLUMN
    inverse_edge_type: USED_BY_CARD
    materialize_inverse: false
    edge_class: canonical
    source_type: validation_test
    target_type: column
    evidence_refs:
    - ev.walmart.overview.001
    notes: validation_test SQL/template uses this documented column.
```

```yaml
candidate_edge:
  edge_id: edge.walmart.0703
  edge_type: USES_COLUMN
  source: validation_test.walmart.oms_settlement_coverage
  target: column.zs_observe.walmart_oms.order_id
  fields:
    edge_family: dependency_usage
    evidence_basis: validation_test SQL/template uses this documented column.
    confidence: high
    canonical_cognee_edge: true
    marketplace_only: true
    canonical_edge_type: USES_COLUMN
    inverse_edge_type: USED_BY_CARD
    materialize_inverse: false
    edge_class: canonical
    source_type: validation_test
    target_type: column
    evidence_refs:
    - ev.walmart.relationships.001
    notes: validation_test SQL/template uses this documented column.
```

```yaml
candidate_edge:
  edge_id: edge.walmart.0704
  edge_type: USES_COLUMN
  source: validation_test.walmart.oms_settlement_coverage
  target: column.zs_observe.walmart_oms.sku_id
  fields:
    edge_family: dependency_usage
    evidence_basis: validation_test SQL/template uses this documented column.
    confidence: high
    canonical_cognee_edge: true
    marketplace_only: true
    canonical_edge_type: USES_COLUMN
    inverse_edge_type: USED_BY_CARD
    materialize_inverse: false
    edge_class: canonical
    source_type: validation_test
    target_type: column
    evidence_refs:
    - ev.walmart.relationships.001
    notes: validation_test SQL/template uses this documented column.
```

```yaml
candidate_edge:
  edge_id: edge.walmart.0705
  edge_type: USES_COLUMN
  source: validation_test.walmart.oms_settlement_coverage
  target: column.zs_observe.walmart_oms.created_date
  fields:
    edge_family: dependency_usage
    evidence_basis: validation_test SQL/template uses this documented column.
    confidence: high
    canonical_cognee_edge: true
    marketplace_only: true
    canonical_edge_type: USES_COLUMN
    inverse_edge_type: USED_BY_CARD
    materialize_inverse: false
    edge_class: canonical
    source_type: validation_test
    target_type: column
    evidence_refs:
    - ev.walmart.relationships.001
    notes: validation_test SQL/template uses this documented column.
```

```yaml
candidate_edge:
  edge_id: edge.walmart.0706
  edge_type: USES_COLUMN
  source: validation_test.walmart.oms_settlement_coverage
  target: column.zs_observe.walmart_oms.charged_amount
  fields:
    edge_family: dependency_usage
    evidence_basis: validation_test SQL/template uses this documented column.
    confidence: high
    canonical_cognee_edge: true
    marketplace_only: true
    canonical_edge_type: USES_COLUMN
    inverse_edge_type: USED_BY_CARD
    materialize_inverse: false
    edge_class: canonical
    source_type: validation_test
    target_type: column
    evidence_refs:
    - ev.walmart.relationships.001
    notes: validation_test SQL/template uses this documented column.
```

```yaml
candidate_edge:
  edge_id: edge.walmart.0707
  edge_type: USES_COLUMN
  source: validation_test.walmart.oms_settlement_coverage
  target: column.zs_observe.walmart_oms.internal_txn_type
  fields:
    edge_family: dependency_usage
    evidence_basis: validation_test SQL/template uses this documented column.
    confidence: high
    canonical_cognee_edge: true
    marketplace_only: true
    canonical_edge_type: USES_COLUMN
    inverse_edge_type: USED_BY_CARD
    materialize_inverse: false
    edge_class: canonical
    source_type: validation_test
    target_type: column
    evidence_refs:
    - ev.walmart.relationships.001
    notes: validation_test SQL/template uses this documented column.
```

```yaml
candidate_edge:
  edge_id: edge.walmart.0708
  edge_type: USES_COLUMN
  source: validation_test.walmart.oms_settlement_coverage
  target: column.zs_observe.walmart_oms.order_status
  fields:
    edge_family: dependency_usage
    evidence_basis: validation_test SQL/template uses this documented column.
    confidence: high
    canonical_cognee_edge: true
    marketplace_only: true
    canonical_edge_type: USES_COLUMN
    inverse_edge_type: USED_BY_CARD
    materialize_inverse: false
    edge_class: canonical
    source_type: validation_test
    target_type: column
    evidence_refs:
    - ev.walmart.relationships.001
    notes: validation_test SQL/template uses this documented column.
```

```yaml
candidate_edge:
  edge_id: edge.walmart.0709
  edge_type: USES_COLUMN
  source: validation_test.walmart.oms_settlement_coverage
  target: column.zs_observe.walmart_oms.group_level_id
  fields:
    edge_family: dependency_usage
    evidence_basis: validation_test SQL/template uses this documented column.
    confidence: high
    canonical_cognee_edge: true
    marketplace_only: true
    canonical_edge_type: USES_COLUMN
    inverse_edge_type: USED_BY_CARD
    materialize_inverse: false
    edge_class: canonical
    source_type: validation_test
    target_type: column
    evidence_refs:
    - ev.walmart.relationships.001
    notes: validation_test SQL/template uses this documented column.
```

```yaml
candidate_edge:
  edge_id: edge.walmart.0710
  edge_type: USES_COLUMN
  source: validation_test.walmart.oms_settlement_coverage
  target: column.zs_observe.walmart_oms.is_active
  fields:
    edge_family: dependency_usage
    evidence_basis: validation_test SQL/template uses this documented column.
    confidence: high
    canonical_cognee_edge: true
    marketplace_only: true
    canonical_edge_type: USES_COLUMN
    inverse_edge_type: USED_BY_CARD
    materialize_inverse: false
    edge_class: canonical
    source_type: validation_test
    target_type: column
    evidence_refs:
    - ev.walmart.relationships.001
    notes: validation_test SQL/template uses this documented column.
```

```yaml
candidate_edge:
  edge_id: edge.walmart.0711
  edge_type: USES_COLUMN
  source: validation_test.walmart.oms_settlement_coverage
  target: column.zs_observe.walmart_settlement.order_id
  fields:
    edge_family: dependency_usage
    evidence_basis: validation_test SQL/template uses this documented column.
    confidence: high
    canonical_cognee_edge: true
    marketplace_only: true
    canonical_edge_type: USES_COLUMN
    inverse_edge_type: USED_BY_CARD
    materialize_inverse: false
    edge_class: canonical
    source_type: validation_test
    target_type: column
    evidence_refs:
    - ev.walmart.relationships.001
    notes: validation_test SQL/template uses this documented column.
```

```yaml
candidate_edge:
  edge_id: edge.walmart.0712
  edge_type: USES_COLUMN
  source: validation_test.walmart.oms_settlement_coverage
  target: column.zs_observe.walmart_settlement.sku_id
  fields:
    edge_family: dependency_usage
    evidence_basis: validation_test SQL/template uses this documented column.
    confidence: high
    canonical_cognee_edge: true
    marketplace_only: true
    canonical_edge_type: USES_COLUMN
    inverse_edge_type: USED_BY_CARD
    materialize_inverse: false
    edge_class: canonical
    source_type: validation_test
    target_type: column
    evidence_refs:
    - ev.walmart.relationships.001
    notes: validation_test SQL/template uses this documented column.
```

```yaml
candidate_edge:
  edge_id: edge.walmart.0713
  edge_type: USES_COLUMN
  source: validation_test.walmart.oms_settlement_coverage
  target: column.zs_observe.walmart_settlement.created_date
  fields:
    edge_family: dependency_usage
    evidence_basis: validation_test SQL/template uses this documented column.
    confidence: high
    canonical_cognee_edge: true
    marketplace_only: true
    canonical_edge_type: USES_COLUMN
    inverse_edge_type: USED_BY_CARD
    materialize_inverse: false
    edge_class: canonical
    source_type: validation_test
    target_type: column
    evidence_refs:
    - ev.walmart.relationships.001
    notes: validation_test SQL/template uses this documented column.
```

```yaml
candidate_edge:
  edge_id: edge.walmart.0714
  edge_type: USES_COLUMN
  source: validation_test.walmart.oms_settlement_coverage
  target: column.zs_observe.walmart_settlement.charged_amount
  fields:
    edge_family: dependency_usage
    evidence_basis: validation_test SQL/template uses this documented column.
    confidence: high
    canonical_cognee_edge: true
    marketplace_only: true
    canonical_edge_type: USES_COLUMN
    inverse_edge_type: USED_BY_CARD
    materialize_inverse: false
    edge_class: canonical
    source_type: validation_test
    target_type: column
    evidence_refs:
    - ev.walmart.relationships.001
    notes: validation_test SQL/template uses this documented column.
```

```yaml
candidate_edge:
  edge_id: edge.walmart.0715
  edge_type: USES_COLUMN
  source: validation_test.walmart.oms_settlement_coverage
  target: column.zs_observe.walmart_settlement.charged_amount_excluding_tax
  fields:
    edge_family: dependency_usage
    evidence_basis: validation_test SQL/template uses this documented column.
    confidence: high
    canonical_cognee_edge: true
    marketplace_only: true
    canonical_edge_type: USES_COLUMN
    inverse_edge_type: USED_BY_CARD
    materialize_inverse: false
    edge_class: canonical
    source_type: validation_test
    target_type: column
    evidence_refs:
    - ev.walmart.relationships.001
    notes: validation_test SQL/template uses this documented column.
```

```yaml
candidate_edge:
  edge_id: edge.walmart.0716
  edge_type: USES_COLUMN
  source: validation_test.walmart.oms_settlement_coverage
  target: column.zs_observe.walmart_settlement.total_tax
  fields:
    edge_family: dependency_usage
    evidence_basis: validation_test SQL/template uses this documented column.
    confidence: high
    canonical_cognee_edge: true
    marketplace_only: true
    canonical_edge_type: USES_COLUMN
    inverse_edge_type: USED_BY_CARD
    materialize_inverse: false
    edge_class: canonical
    source_type: validation_test
    target_type: column
    evidence_refs:
    - ev.walmart.relationships.001
    notes: validation_test SQL/template uses this documented column.
```

```yaml
candidate_edge:
  edge_id: edge.walmart.0717
  edge_type: USES_COLUMN
  source: validation_test.walmart.oms_settlement_coverage
  target: column.zs_observe.walmart_settlement.gross_commission
  fields:
    edge_family: dependency_usage
    evidence_basis: validation_test SQL/template uses this documented column.
    confidence: high
    canonical_cognee_edge: true
    marketplace_only: true
    canonical_edge_type: USES_COLUMN
    inverse_edge_type: USED_BY_CARD
    materialize_inverse: false
    edge_class: canonical
    source_type: validation_test
    target_type: column
    evidence_refs:
    - ev.walmart.relationships.001
    notes: validation_test SQL/template uses this documented column.
```

```yaml
candidate_edge:
  edge_id: edge.walmart.0718
  edge_type: USES_COLUMN
  source: validation_test.walmart.oms_settlement_coverage
  target: column.zs_observe.walmart_settlement.marketplace_withheld_tax
  fields:
    edge_family: dependency_usage
    evidence_basis: validation_test SQL/template uses this documented column.
    confidence: high
    canonical_cognee_edge: true
    marketplace_only: true
    canonical_edge_type: USES_COLUMN
    inverse_edge_type: USED_BY_CARD
    materialize_inverse: false
    edge_class: canonical
    source_type: validation_test
    target_type: column
    evidence_refs:
    - ev.walmart.relationships.001
    notes: validation_test SQL/template uses this documented column.
```

```yaml
candidate_edge:
  edge_id: edge.walmart.0719
  edge_type: USES_COLUMN
  source: validation_test.walmart.oms_settlement_coverage
  target: column.zs_observe.walmart_settlement.transaction_type
  fields:
    edge_family: dependency_usage
    evidence_basis: validation_test SQL/template uses this documented column.
    confidence: high
    canonical_cognee_edge: true
    marketplace_only: true
    canonical_edge_type: USES_COLUMN
    inverse_edge_type: USED_BY_CARD
    materialize_inverse: false
    edge_class: canonical
    source_type: validation_test
    target_type: column
    evidence_refs:
    - ev.walmart.relationships.001
    notes: validation_test SQL/template uses this documented column.
```

```yaml
candidate_edge:
  edge_id: edge.walmart.0720
  edge_type: USES_COLUMN
  source: validation_test.walmart.oms_settlement_coverage
  target: column.zs_observe.walmart_settlement.internal_txn_type
  fields:
    edge_family: dependency_usage
    evidence_basis: validation_test SQL/template uses this documented column.
    confidence: high
    canonical_cognee_edge: true
    marketplace_only: true
    canonical_edge_type: USES_COLUMN
    inverse_edge_type: USED_BY_CARD
    materialize_inverse: false
    edge_class: canonical
    source_type: validation_test
    target_type: column
    evidence_refs:
    - ev.walmart.relationships.001
    notes: validation_test SQL/template uses this documented column.
```

```yaml
candidate_edge:
  edge_id: edge.walmart.0721
  edge_type: USES_COLUMN
  source: validation_test.walmart.oms_settlement_coverage
  target: column.zs_observe.walmart_settlement.group_level_id
  fields:
    edge_family: dependency_usage
    evidence_basis: validation_test SQL/template uses this documented column.
    confidence: high
    canonical_cognee_edge: true
    marketplace_only: true
    canonical_edge_type: USES_COLUMN
    inverse_edge_type: USED_BY_CARD
    materialize_inverse: false
    edge_class: canonical
    source_type: validation_test
    target_type: column
    evidence_refs:
    - ev.walmart.relationships.001
    notes: validation_test SQL/template uses this documented column.
```

```yaml
candidate_edge:
  edge_id: edge.walmart.0722
  edge_type: USES_COLUMN
  source: validation_test.walmart.oms_settlement_coverage
  target: column.zs_observe.walmart_settlement.is_active
  fields:
    edge_family: dependency_usage
    evidence_basis: validation_test SQL/template uses this documented column.
    confidence: high
    canonical_cognee_edge: true
    marketplace_only: true
    canonical_edge_type: USES_COLUMN
    inverse_edge_type: USED_BY_CARD
    materialize_inverse: false
    edge_class: canonical
    source_type: validation_test
    target_type: column
    evidence_refs:
    - ev.walmart.relationships.001
    notes: validation_test SQL/template uses this documented column.
```

```yaml
candidate_edge:
  edge_id: edge.walmart.0723
  edge_type: USES_COLUMN
  source: formula_template.walmart.net_seller_payout
  target: column.zs_observe.walmart_settlement.charged_amount_excluding_tax
  fields:
    edge_family: dependency_usage
    evidence_basis: Formula uses this documented column.
    confidence: high
    canonical_cognee_edge: true
    marketplace_only: true
    canonical_edge_type: USES_COLUMN
    inverse_edge_type: USED_BY_CARD
    materialize_inverse: false
    edge_class: canonical
    source_type: formula_template
    target_type: column
    evidence_refs:
    - ev.walmart.business_model.001
    notes: Formula uses this documented column.
```

```yaml
candidate_edge:
  edge_id: edge.walmart.0724
  edge_type: USES_COLUMN
  source: formula_template.walmart.net_seller_payout
  target: column.zs_observe.walmart_settlement.gross_commission
  fields:
    edge_family: dependency_usage
    evidence_basis: Formula uses this documented column.
    confidence: high
    canonical_cognee_edge: true
    marketplace_only: true
    canonical_edge_type: USES_COLUMN
    inverse_edge_type: USED_BY_CARD
    materialize_inverse: false
    edge_class: canonical
    source_type: formula_template
    target_type: column
    evidence_refs:
    - ev.walmart.business_model.001
    notes: Formula uses this documented column.
```

```yaml
candidate_edge:
  edge_id: edge.walmart.0725
  edge_type: USES_COLUMN
  source: formula_template.walmart.net_seller_payout
  target: column.zs_observe.walmart_settlement.marketplace_withheld_tax
  fields:
    edge_family: dependency_usage
    evidence_basis: Formula uses this documented column.
    confidence: high
    canonical_cognee_edge: true
    marketplace_only: true
    canonical_edge_type: USES_COLUMN
    inverse_edge_type: USED_BY_CARD
    materialize_inverse: false
    edge_class: canonical
    source_type: formula_template
    target_type: column
    evidence_refs:
    - ev.walmart.business_model.001
    notes: Formula uses this documented column.
```

```yaml
candidate_edge:
  edge_id: edge.walmart.0726
  edge_type: USES_COLUMN
  source: formula_template.walmart.net_seller_payout
  target: column.zs_observe.walmart_settlement.settled_amount
  fields:
    edge_family: dependency_usage
    evidence_basis: Formula uses this documented column.
    confidence: high
    canonical_cognee_edge: true
    marketplace_only: true
    canonical_edge_type: USES_COLUMN
    inverse_edge_type: USED_BY_CARD
    materialize_inverse: false
    edge_class: canonical
    source_type: formula_template
    target_type: column
    evidence_refs:
    - ev.walmart.business_model.001
    notes: Formula uses this documented column.
```

```yaml
candidate_edge:
  edge_id: edge.walmart.0727
  edge_type: USES_COLUMN
  source: formula_template.walmart.mpf_tax_identity
  target: column.zs_observe.walmart_settlement.charged_amount
  fields:
    edge_family: dependency_usage
    evidence_basis: Formula uses this documented column.
    confidence: high
    canonical_cognee_edge: true
    marketplace_only: true
    canonical_edge_type: USES_COLUMN
    inverse_edge_type: USED_BY_CARD
    materialize_inverse: false
    edge_class: canonical
    source_type: formula_template
    target_type: column
    evidence_refs:
    - ev.walmart.business_model.001
    notes: Formula uses this documented column.
```

```yaml
candidate_edge:
  edge_id: edge.walmart.0728
  edge_type: USES_COLUMN
  source: formula_template.walmart.mpf_tax_identity
  target: column.zs_observe.walmart_settlement.charged_amount_excluding_tax
  fields:
    edge_family: dependency_usage
    evidence_basis: Formula uses this documented column.
    confidence: high
    canonical_cognee_edge: true
    marketplace_only: true
    canonical_edge_type: USES_COLUMN
    inverse_edge_type: USED_BY_CARD
    materialize_inverse: false
    edge_class: canonical
    source_type: formula_template
    target_type: column
    evidence_refs:
    - ev.walmart.business_model.001
    notes: Formula uses this documented column.
```

```yaml
candidate_edge:
  edge_id: edge.walmart.0729
  edge_type: USES_COLUMN
  source: formula_template.walmart.mpf_tax_identity
  target: column.zs_observe.walmart_settlement.total_tax
  fields:
    edge_family: dependency_usage
    evidence_basis: Formula uses this documented column.
    confidence: high
    canonical_cognee_edge: true
    marketplace_only: true
    canonical_edge_type: USES_COLUMN
    inverse_edge_type: USED_BY_CARD
    materialize_inverse: false
    edge_class: canonical
    source_type: formula_template
    target_type: column
    evidence_refs:
    - ev.walmart.business_model.001
    notes: Formula uses this documented column.
```

```yaml
candidate_edge:
  edge_id: edge.walmart.0730
  edge_type: USES_COLUMN
  source: formula_template.walmart.mpf_tax_identity
  target: column.zs_observe.walmart_settlement.marketplace_withheld_tax
  fields:
    edge_family: dependency_usage
    evidence_basis: Formula uses this documented column.
    confidence: high
    canonical_cognee_edge: true
    marketplace_only: true
    canonical_edge_type: USES_COLUMN
    inverse_edge_type: USED_BY_CARD
    materialize_inverse: false
    edge_class: canonical
    source_type: formula_template
    target_type: column
    evidence_refs:
    - ev.walmart.business_model.001
    notes: Formula uses this documented column.
```

```yaml
candidate_edge:
  edge_id: edge.walmart.0731
  edge_type: USES_COLUMN
  source: formula_template.walmart.effective_commission_rate
  target: column.zs_observe.walmart_settlement.charged_amount_excluding_tax
  fields:
    edge_family: dependency_usage
    evidence_basis: Formula uses this documented column.
    confidence: high
    canonical_cognee_edge: true
    marketplace_only: true
    canonical_edge_type: USES_COLUMN
    inverse_edge_type: USED_BY_CARD
    materialize_inverse: false
    edge_class: canonical
    source_type: formula_template
    target_type: column
    evidence_refs:
    - ev.walmart.quality.001
    notes: Formula uses this documented column.
```

```yaml
candidate_edge:
  edge_id: edge.walmart.0732
  edge_type: USES_COLUMN
  source: formula_template.walmart.effective_commission_rate
  target: column.zs_observe.walmart_settlement.gross_commission
  fields:
    edge_family: dependency_usage
    evidence_basis: Formula uses this documented column.
    confidence: high
    canonical_cognee_edge: true
    marketplace_only: true
    canonical_edge_type: USES_COLUMN
    inverse_edge_type: USED_BY_CARD
    materialize_inverse: false
    edge_class: canonical
    source_type: formula_template
    target_type: column
    evidence_refs:
    - ev.walmart.quality.001
    notes: Formula uses this documented column.
```

```yaml
candidate_edge:
  edge_id: edge.walmart.0733
  edge_type: USES_COLUMN
  source: formula_template.walmart.effective_commission_rate
  target: column.zs_observe.walmart_settlement.base_commission_rate
  fields:
    edge_family: dependency_usage
    evidence_basis: Formula uses this documented column.
    confidence: high
    canonical_cognee_edge: true
    marketplace_only: true
    canonical_edge_type: USES_COLUMN
    inverse_edge_type: USED_BY_CARD
    materialize_inverse: false
    edge_class: canonical
    source_type: formula_template
    target_type: column
    evidence_refs:
    - ev.walmart.quality.001
    notes: Formula uses this documented column.
```

```yaml
candidate_edge:
  edge_id: edge.walmart.0734
  edge_type: USES_COLUMN
  source: formula_template.walmart.effective_commission_rate
  target: column.zs_observe.walmart_settlement.commission_rate
  fields:
    edge_family: dependency_usage
    evidence_basis: Formula uses this documented column.
    confidence: high
    canonical_cognee_edge: true
    marketplace_only: true
    canonical_edge_type: USES_COLUMN
    inverse_edge_type: USED_BY_CARD
    materialize_inverse: false
    edge_class: canonical
    source_type: formula_template
    target_type: column
    evidence_refs:
    - ev.walmart.quality.001
    notes: Formula uses this documented column.
```

```yaml
candidate_edge:
  edge_id: edge.walmart.0735
  edge_type: USES_COLUMN
  source: formula_template.walmart.refund_reversal
  target: column.zs_observe.walmart_settlement.order_id
  fields:
    edge_family: dependency_usage
    evidence_basis: Formula uses this documented column.
    confidence: high
    canonical_cognee_edge: true
    marketplace_only: true
    canonical_edge_type: USES_COLUMN
    inverse_edge_type: USED_BY_CARD
    materialize_inverse: false
    edge_class: canonical
    source_type: formula_template
    target_type: column
    evidence_refs:
    - ev.walmart.lifecycle.001
    notes: Formula uses this documented column.
```

```yaml
candidate_edge:
  edge_id: edge.walmart.0736
  edge_type: USES_COLUMN
  source: formula_template.walmart.refund_reversal
  target: column.zs_observe.walmart_settlement.sku_id
  fields:
    edge_family: dependency_usage
    evidence_basis: Formula uses this documented column.
    confidence: high
    canonical_cognee_edge: true
    marketplace_only: true
    canonical_edge_type: USES_COLUMN
    inverse_edge_type: USED_BY_CARD
    materialize_inverse: false
    edge_class: canonical
    source_type: formula_template
    target_type: column
    evidence_refs:
    - ev.walmart.lifecycle.001
    notes: Formula uses this documented column.
```

```yaml
candidate_edge:
  edge_id: edge.walmart.0737
  edge_type: USES_COLUMN
  source: formula_template.walmart.refund_reversal
  target: column.zs_observe.walmart_settlement.charged_amount
  fields:
    edge_family: dependency_usage
    evidence_basis: Formula uses this documented column.
    confidence: high
    canonical_cognee_edge: true
    marketplace_only: true
    canonical_edge_type: USES_COLUMN
    inverse_edge_type: USED_BY_CARD
    materialize_inverse: false
    edge_class: canonical
    source_type: formula_template
    target_type: column
    evidence_refs:
    - ev.walmart.lifecycle.001
    notes: Formula uses this documented column.
```

```yaml
candidate_edge:
  edge_id: edge.walmart.0738
  edge_type: USES_COLUMN
  source: formula_template.walmart.refund_reversal
  target: column.zs_observe.walmart_settlement.gross_commission
  fields:
    edge_family: dependency_usage
    evidence_basis: Formula uses this documented column.
    confidence: high
    canonical_cognee_edge: true
    marketplace_only: true
    canonical_edge_type: USES_COLUMN
    inverse_edge_type: USED_BY_CARD
    materialize_inverse: false
    edge_class: canonical
    source_type: formula_template
    target_type: column
    evidence_refs:
    - ev.walmart.lifecycle.001
    notes: Formula uses this documented column.
```

```yaml
candidate_edge:
  edge_id: edge.walmart.0739
  edge_type: USES_COLUMN
  source: formula_template.walmart.refund_reversal
  target: column.zs_observe.walmart_settlement.marketplace_withheld_tax
  fields:
    edge_family: dependency_usage
    evidence_basis: Formula uses this documented column.
    confidence: high
    canonical_cognee_edge: true
    marketplace_only: true
    canonical_edge_type: USES_COLUMN
    inverse_edge_type: USED_BY_CARD
    materialize_inverse: false
    edge_class: canonical
    source_type: formula_template
    target_type: column
    evidence_refs:
    - ev.walmart.lifecycle.001
    notes: Formula uses this documented column.
```

```yaml
candidate_edge:
  edge_id: edge.walmart.0740
  edge_type: USES_COLUMN
  source: relationship.walmart.oms_to_settlement_order_id
  target: column.zs_observe.walmart_oms.order_id
  fields:
    edge_family: dependency_usage
    evidence_basis: Relationship left join key column.
    confidence: high
    canonical_cognee_edge: true
    marketplace_only: true
    canonical_edge_type: USES_COLUMN
    inverse_edge_type: USED_BY_CARD
    materialize_inverse: false
    edge_class: canonical
    source_type: relationship
    target_type: column
    evidence_refs:
    - ev.walmart.relationships.001
    notes: Relationship left join key column.
```

```yaml
candidate_edge:
  edge_id: edge.walmart.0741
  edge_type: USES_COLUMN
  source: relationship.walmart.oms_to_settlement_order_id
  target: column.zs_observe.walmart_settlement.order_id
  fields:
    edge_family: dependency_usage
    evidence_basis: Relationship right join key column.
    confidence: high
    canonical_cognee_edge: true
    marketplace_only: true
    canonical_edge_type: USES_COLUMN
    inverse_edge_type: USED_BY_CARD
    materialize_inverse: false
    edge_class: canonical
    source_type: relationship
    target_type: column
    evidence_refs:
    - ev.walmart.relationships.001
    notes: Relationship right join key column.
```

```yaml
candidate_edge:
  edge_id: edge.walmart.0742
  edge_type: USES_COLUMN
  source: relationship.walmart.oms_to_lookup_sku
  target: column.zs_observe.walmart_oms.sku_id
  fields:
    edge_family: dependency_usage
    evidence_basis: Relationship left join key column.
    confidence: high
    canonical_cognee_edge: true
    marketplace_only: true
    canonical_edge_type: USES_COLUMN
    inverse_edge_type: USED_BY_CARD
    materialize_inverse: false
    edge_class: canonical
    source_type: relationship
    target_type: column
    evidence_refs:
    - ev.walmart.relationships.001
    notes: Relationship left join key column.
```

```yaml
candidate_edge:
  edge_id: edge.walmart.0743
  edge_type: USES_COLUMN
  source: relationship.walmart.oms_to_lookup_sku
  target: column.zs_observe.walmart_lookup.sku
  fields:
    edge_family: dependency_usage
    evidence_basis: Relationship right join key column.
    confidence: high
    canonical_cognee_edge: true
    marketplace_only: true
    canonical_edge_type: USES_COLUMN
    inverse_edge_type: USED_BY_CARD
    materialize_inverse: false
    edge_class: canonical
    source_type: relationship
    target_type: column
    evidence_refs:
    - ev.walmart.relationships.001
    notes: Relationship right join key column.
```

```yaml
candidate_edge:
  edge_id: edge.walmart.0744
  edge_type: USES_COLUMN
  source: relationship.walmart.settlement_to_lookup_sku
  target: column.zs_observe.walmart_settlement.sku_id
  fields:
    edge_family: dependency_usage
    evidence_basis: Relationship left join key column.
    confidence: high
    canonical_cognee_edge: true
    marketplace_only: true
    canonical_edge_type: USES_COLUMN
    inverse_edge_type: USED_BY_CARD
    materialize_inverse: false
    edge_class: canonical
    source_type: relationship
    target_type: column
    evidence_refs:
    - ev.walmart.relationships.001
    notes: Relationship left join key column.
```

```yaml
candidate_edge:
  edge_id: edge.walmart.0745
  edge_type: USES_COLUMN
  source: relationship.walmart.settlement_to_lookup_sku
  target: column.zs_observe.walmart_lookup.sku
  fields:
    edge_family: dependency_usage
    evidence_basis: Relationship right join key column.
    confidence: high
    canonical_cognee_edge: true
    marketplace_only: true
    canonical_edge_type: USES_COLUMN
    inverse_edge_type: USED_BY_CARD
    materialize_inverse: false
    edge_class: canonical
    source_type: relationship
    target_type: column
    evidence_refs:
    - ev.walmart.relationships.001
    notes: Relationship right join key column.
```

```yaml
candidate_edge:
  edge_id: edge.walmart.0746
  edge_type: USES_COLUMN
  source: relationship.walmart.oms_item_to_settlement_gtin
  target: column.zs_observe.walmart_oms.item_id
  fields:
    edge_family: dependency_usage
    evidence_basis: Relationship left join key column.
    confidence: high
    canonical_cognee_edge: true
    marketplace_only: true
    canonical_edge_type: USES_COLUMN
    inverse_edge_type: USED_BY_CARD
    materialize_inverse: false
    edge_class: canonical
    source_type: relationship
    target_type: column
    evidence_refs:
    - ev.walmart.relationships.001
    notes: Relationship left join key column.
```

```yaml
candidate_edge:
  edge_id: edge.walmart.0747
  edge_type: USES_COLUMN
  source: relationship.walmart.oms_item_to_settlement_gtin
  target: column.zs_observe.walmart_settlement.partner_gtin
  fields:
    edge_family: dependency_usage
    evidence_basis: Relationship right join key column.
    confidence: high
    canonical_cognee_edge: true
    marketplace_only: true
    canonical_edge_type: USES_COLUMN
    inverse_edge_type: USED_BY_CARD
    materialize_inverse: false
    edge_class: canonical
    source_type: relationship
    target_type: column
    evidence_refs:
    - ev.walmart.relationships.001
    notes: Relationship right join key column.
```

```yaml
candidate_edge:
  edge_id: edge.walmart.0748
  edge_type: USES_TABLE
  source: reconciliation_side.walmart.oms_to_settlement.expected
  target: table.zs_observe.walmart_oms
  fields:
    edge_family: dependency_usage
    evidence_basis: Reconciliation side source table.
    confidence: high
    canonical_cognee_edge: true
    marketplace_only: true
    canonical_edge_type: USES_TABLE
    inverse_edge_type: USED_BY_CARD
    materialize_inverse: false
    edge_class: canonical
    source_type: reconciliation_side
    target_type: table
    evidence_refs:
    - ev.walmart.reconciliation.001
    notes: Reconciliation side source table.
```

```yaml
candidate_edge:
  edge_id: edge.walmart.0749
  edge_type: USES_TABLE
  source: reconciliation_side.walmart.oms_to_settlement.actual
  target: table.zs_observe.walmart_settlement
  fields:
    edge_family: dependency_usage
    evidence_basis: Reconciliation side source table.
    confidence: high
    canonical_cognee_edge: true
    marketplace_only: true
    canonical_edge_type: USES_TABLE
    inverse_edge_type: USED_BY_CARD
    materialize_inverse: false
    edge_class: canonical
    source_type: reconciliation_side
    target_type: table
    evidence_refs:
    - ev.walmart.reconciliation.001
    notes: Reconciliation side source table.
```

```yaml
candidate_edge:
  edge_id: edge.walmart.0750
  edge_type: USES_TABLE
  source: reconciliation_side.walmart.commission_validation.expected
  target: table.zs_observe.walmart_settlement
  fields:
    edge_family: dependency_usage
    evidence_basis: Reconciliation side source table.
    confidence: high
    canonical_cognee_edge: true
    marketplace_only: true
    canonical_edge_type: USES_TABLE
    inverse_edge_type: USED_BY_CARD
    materialize_inverse: false
    edge_class: canonical
    source_type: reconciliation_side
    target_type: table
    evidence_refs:
    - ev.walmart.reconciliation.001
    notes: Reconciliation side source table.
```

```yaml
candidate_edge:
  edge_id: edge.walmart.0751
  edge_type: USES_TABLE
  source: reconciliation_side.walmart.commission_validation.actual
  target: table.zs_observe.walmart_settlement
  fields:
    edge_family: dependency_usage
    evidence_basis: Reconciliation side source table.
    confidence: high
    canonical_cognee_edge: true
    marketplace_only: true
    canonical_edge_type: USES_TABLE
    inverse_edge_type: USED_BY_CARD
    materialize_inverse: false
    edge_class: canonical
    source_type: reconciliation_side
    target_type: table
    evidence_refs:
    - ev.walmart.reconciliation.001
    notes: Reconciliation side source table.
```

```yaml
candidate_edge:
  edge_id: edge.walmart.0752
  edge_type: USES_TABLE
  source: reconciliation_side.walmart.refund_to_sale.expected
  target: table.zs_observe.walmart_settlement
  fields:
    edge_family: dependency_usage
    evidence_basis: Reconciliation side source table.
    confidence: high
    canonical_cognee_edge: true
    marketplace_only: true
    canonical_edge_type: USES_TABLE
    inverse_edge_type: USED_BY_CARD
    materialize_inverse: false
    edge_class: canonical
    source_type: reconciliation_side
    target_type: table
    evidence_refs:
    - ev.walmart.reconciliation.001
    notes: Reconciliation side source table.
```

```yaml
candidate_edge:
  edge_id: edge.walmart.0753
  edge_type: USES_TABLE
  source: reconciliation_side.walmart.refund_to_sale.actual
  target: table.zs_observe.walmart_settlement
  fields:
    edge_family: dependency_usage
    evidence_basis: Reconciliation side source table.
    confidence: high
    canonical_cognee_edge: true
    marketplace_only: true
    canonical_edge_type: USES_TABLE
    inverse_edge_type: USED_BY_CARD
    materialize_inverse: false
    edge_class: canonical
    source_type: reconciliation_side
    target_type: table
    evidence_refs:
    - ev.walmart.reconciliation.001
    notes: Reconciliation side source table.
```

```yaml
candidate_edge:
  edge_id: edge.walmart.0754
  edge_type: USES_TABLE
  source: reconciliation_side.walmart.mpf_tax_identity.expected
  target: table.zs_observe.walmart_settlement
  fields:
    edge_family: dependency_usage
    evidence_basis: Reconciliation side source table.
    confidence: high
    canonical_cognee_edge: true
    marketplace_only: true
    canonical_edge_type: USES_TABLE
    inverse_edge_type: USED_BY_CARD
    materialize_inverse: false
    edge_class: canonical
    source_type: reconciliation_side
    target_type: table
    evidence_refs:
    - ev.walmart.business_model.001
    notes: Reconciliation side source table.
```

```yaml
candidate_edge:
  edge_id: edge.walmart.0755
  edge_type: USES_TABLE
  source: reconciliation_side.walmart.mpf_tax_identity.actual
  target: table.zs_observe.walmart_lookup
  fields:
    edge_family: dependency_usage
    evidence_basis: Reconciliation side source table.
    confidence: high
    canonical_cognee_edge: true
    marketplace_only: true
    canonical_edge_type: USES_TABLE
    inverse_edge_type: USED_BY_CARD
    materialize_inverse: false
    edge_class: canonical
    source_type: reconciliation_side
    target_type: table
    evidence_refs:
    - ev.walmart.business_model.001
    notes: Reconciliation side source table.
```

```yaml
candidate_edge:
  edge_id: edge.walmart.0756
  edge_type: USES_TABLE
  source: reconciliation_side.walmart.lookup_coverage.expected
  target: table.zs_observe.walmart_oms
  fields:
    edge_family: dependency_usage
    evidence_basis: Reconciliation side source table.
    confidence: high
    canonical_cognee_edge: true
    marketplace_only: true
    canonical_edge_type: USES_TABLE
    inverse_edge_type: USED_BY_CARD
    materialize_inverse: false
    edge_class: canonical
    source_type: reconciliation_side
    target_type: table
    evidence_refs:
    - ev.walmart.relationships.001
    notes: Reconciliation side source table.
```

```yaml
candidate_edge:
  edge_id: edge.walmart.0757
  edge_type: USES_TABLE
  source: reconciliation_side.walmart.lookup_coverage.actual
  target: table.zs_observe.walmart_lookup
  fields:
    edge_family: dependency_usage
    evidence_basis: Reconciliation side source table.
    confidence: high
    canonical_cognee_edge: true
    marketplace_only: true
    canonical_edge_type: USES_TABLE
    inverse_edge_type: USED_BY_CARD
    materialize_inverse: false
    edge_class: canonical
    source_type: reconciliation_side
    target_type: table
    evidence_refs:
    - ev.walmart.relationships.001
    notes: Reconciliation side source table.
```

```yaml
candidate_edge:
  edge_id: edge.walmart.0758
  edge_type: USES_TABLE
  source: reconciliation_profile.walmart.oms_to_settlement
  target: table.zs_observe.walmart_oms
  fields:
    edge_family: dependency_usage
    evidence_basis: Reconciliation profile source table through sides.
    confidence: high
    canonical_cognee_edge: true
    marketplace_only: true
    canonical_edge_type: USES_TABLE
    inverse_edge_type: USED_BY_CARD
    materialize_inverse: false
    edge_class: canonical
    source_type: reconciliation_profile
    target_type: table
    evidence_refs:
    - ev.walmart.reconciliation.001
    notes: Reconciliation profile source table through sides.
```

```yaml
candidate_edge:
  edge_id: edge.walmart.0759
  edge_type: USES_TABLE
  source: reconciliation_profile.walmart.oms_to_settlement
  target: table.zs_observe.walmart_settlement
  fields:
    edge_family: dependency_usage
    evidence_basis: Reconciliation profile source table through sides.
    confidence: high
    canonical_cognee_edge: true
    marketplace_only: true
    canonical_edge_type: USES_TABLE
    inverse_edge_type: USED_BY_CARD
    materialize_inverse: false
    edge_class: canonical
    source_type: reconciliation_profile
    target_type: table
    evidence_refs:
    - ev.walmart.reconciliation.001
    notes: Reconciliation profile source table through sides.
```

```yaml
candidate_edge:
  edge_id: edge.walmart.0760
  edge_type: USES_TABLE
  source: reconciliation_profile.walmart.commission_validation
  target: table.zs_observe.walmart_settlement
  fields:
    edge_family: dependency_usage
    evidence_basis: Reconciliation profile source table through sides.
    confidence: high
    canonical_cognee_edge: true
    marketplace_only: true
    canonical_edge_type: USES_TABLE
    inverse_edge_type: USED_BY_CARD
    materialize_inverse: false
    edge_class: canonical
    source_type: reconciliation_profile
    target_type: table
    evidence_refs:
    - ev.walmart.reconciliation.001
    notes: Reconciliation profile source table through sides.
```

```yaml
candidate_edge:
  edge_id: edge.walmart.0761
  edge_type: USES_TABLE
  source: reconciliation_profile.walmart.mpf_tax_identity
  target: table.zs_observe.walmart_lookup
  fields:
    edge_family: dependency_usage
    evidence_basis: Reconciliation profile source table through sides.
    confidence: high
    canonical_cognee_edge: true
    marketplace_only: true
    canonical_edge_type: USES_TABLE
    inverse_edge_type: USED_BY_CARD
    materialize_inverse: false
    edge_class: canonical
    source_type: reconciliation_profile
    target_type: table
    evidence_refs:
    - ev.walmart.business_model.001
    notes: Reconciliation profile source table through sides.
```

```yaml
candidate_edge:
  edge_id: edge.walmart.0762
  edge_type: USES_TABLE
  source: reconciliation_profile.walmart.mpf_tax_identity
  target: table.zs_observe.walmart_settlement
  fields:
    edge_family: dependency_usage
    evidence_basis: Reconciliation profile source table through sides.
    confidence: high
    canonical_cognee_edge: true
    marketplace_only: true
    canonical_edge_type: USES_TABLE
    inverse_edge_type: USED_BY_CARD
    materialize_inverse: false
    edge_class: canonical
    source_type: reconciliation_profile
    target_type: table
    evidence_refs:
    - ev.walmart.business_model.001
    notes: Reconciliation profile source table through sides.
```

```yaml
candidate_edge:
  edge_id: edge.walmart.0763
  edge_type: USES_TABLE
  source: reconciliation_profile.walmart.lookup_coverage
  target: table.zs_observe.walmart_lookup
  fields:
    edge_family: dependency_usage
    evidence_basis: Reconciliation profile source table through sides.
    confidence: high
    canonical_cognee_edge: true
    marketplace_only: true
    canonical_edge_type: USES_TABLE
    inverse_edge_type: USED_BY_CARD
    materialize_inverse: false
    edge_class: canonical
    source_type: reconciliation_profile
    target_type: table
    evidence_refs:
    - ev.walmart.relationships.001
    notes: Reconciliation profile source table through sides.
```

```yaml
candidate_edge:
  edge_id: edge.walmart.0764
  edge_type: USES_TABLE
  source: reconciliation_profile.walmart.lookup_coverage
  target: table.zs_observe.walmart_oms
  fields:
    edge_family: dependency_usage
    evidence_basis: Reconciliation profile source table through sides.
    confidence: high
    canonical_cognee_edge: true
    marketplace_only: true
    canonical_edge_type: USES_TABLE
    inverse_edge_type: USED_BY_CARD
    materialize_inverse: false
    edge_class: canonical
    source_type: reconciliation_profile
    target_type: table
    evidence_refs:
    - ev.walmart.relationships.001
    notes: Reconciliation profile source table through sides.
```

```yaml
candidate_edge:
  edge_id: edge.walmart.0765
  edge_type: USES_COLUMN
  source: rule.walmart.scope_filters
  target: column.zs_observe.walmart_oms.group_level_id
  fields:
    edge_family: dependency_usage
    evidence_basis: Text references this documented column.
    confidence: high
    canonical_cognee_edge: true
    marketplace_only: true
    canonical_edge_type: USES_COLUMN
    inverse_edge_type: USED_BY_CARD
    materialize_inverse: false
    edge_class: canonical
    source_type: rule
    target_type: column
    evidence_refs:
    - ev.walmart.filters.001
    notes: Text references this documented column.
```

```yaml
candidate_edge:
  edge_id: edge.walmart.0766
  edge_type: USES_COLUMN
  source: rule.walmart.scope_filters
  target: column.zs_observe.walmart_oms.is_active
  fields:
    edge_family: dependency_usage
    evidence_basis: Text references this documented column.
    confidence: high
    canonical_cognee_edge: true
    marketplace_only: true
    canonical_edge_type: USES_COLUMN
    inverse_edge_type: USED_BY_CARD
    materialize_inverse: false
    edge_class: canonical
    source_type: rule
    target_type: column
    evidence_refs:
    - ev.walmart.filters.001
    notes: Text references this documented column.
```

```yaml
candidate_edge:
  edge_id: edge.walmart.0767
  edge_type: USES_COLUMN
  source: rule.walmart.no_settled_amount_payout
  target: column.zs_observe.walmart_settlement.settled_amount
  fields:
    edge_family: dependency_usage
    evidence_basis: Explicit related column binding.
    confidence: high
    canonical_cognee_edge: true
    marketplace_only: true
    canonical_edge_type: USES_COLUMN
    inverse_edge_type: USED_BY_CARD
    materialize_inverse: false
    edge_class: canonical
    source_type: rule
    target_type: column
    evidence_refs:
    - ev.walmart.business_model.001
    notes: Explicit related column binding.
```

```yaml
candidate_edge:
  edge_id: edge.walmart.0768
  edge_type: USES_COLUMN
  source: rule.walmart.no_settled_amount_payout
  target: column.zs_observe.walmart_settlement.charged_amount_excluding_tax
  fields:
    edge_family: dependency_usage
    evidence_basis: Text references this documented column.
    confidence: high
    canonical_cognee_edge: true
    marketplace_only: true
    canonical_edge_type: USES_COLUMN
    inverse_edge_type: USED_BY_CARD
    materialize_inverse: false
    edge_class: canonical
    source_type: rule
    target_type: column
    evidence_refs:
    - ev.walmart.business_model.001
    notes: Text references this documented column.
```

```yaml
candidate_edge:
  edge_id: edge.walmart.0769
  edge_type: USES_COLUMN
  source: rule.walmart.no_settled_amount_payout
  target: column.zs_observe.walmart_settlement.gross_commission
  fields:
    edge_family: dependency_usage
    evidence_basis: Text references this documented column.
    confidence: high
    canonical_cognee_edge: true
    marketplace_only: true
    canonical_edge_type: USES_COLUMN
    inverse_edge_type: USED_BY_CARD
    materialize_inverse: false
    edge_class: canonical
    source_type: rule
    target_type: column
    evidence_refs:
    - ev.walmart.business_model.001
    notes: Text references this documented column.
```

```yaml
candidate_edge:
  edge_id: edge.walmart.0770
  edge_type: USES_COLUMN
  source: rule.walmart.mpf_tax_not_seller_revenue
  target: column.zs_observe.walmart_settlement.marketplace_withheld_tax
  fields:
    edge_family: dependency_usage
    evidence_basis: Explicit related column binding.
    confidence: high
    canonical_cognee_edge: true
    marketplace_only: true
    canonical_edge_type: USES_COLUMN
    inverse_edge_type: USED_BY_CARD
    materialize_inverse: false
    edge_class: canonical
    source_type: rule
    target_type: column
    evidence_refs:
    - ev.walmart.business_model.001
    notes: Explicit related column binding.
```

```yaml
candidate_edge:
  edge_id: edge.walmart.0771
  edge_type: USES_COLUMN
  source: rule.walmart.mpf_tax_not_seller_revenue
  target: column.zs_observe.walmart_settlement.total_tax
  fields:
    edge_family: dependency_usage
    evidence_basis: Text references this documented column.
    confidence: high
    canonical_cognee_edge: true
    marketplace_only: true
    canonical_edge_type: USES_COLUMN
    inverse_edge_type: USED_BY_CARD
    materialize_inverse: false
    edge_class: canonical
    source_type: rule
    target_type: column
    evidence_refs:
    - ev.walmart.business_model.001
    notes: Text references this documented column.
```

```yaml
candidate_edge:
  edge_id: edge.walmart.0772
  edge_type: USES_COLUMN
  source: rule.walmart.forward_revenue_filter
  target: column.zs_observe.walmart_oms.internal_txn_type
  fields:
    edge_family: dependency_usage
    evidence_basis: Text references this documented column.
    confidence: high
    canonical_cognee_edge: true
    marketplace_only: true
    canonical_edge_type: USES_COLUMN
    inverse_edge_type: USED_BY_CARD
    materialize_inverse: false
    edge_class: canonical
    source_type: rule
    target_type: column
    evidence_refs:
    - ev.walmart.filters.001
    notes: Text references this documented column.
```

```yaml
candidate_edge:
  edge_id: edge.walmart.0773
  edge_type: USES_COLUMN
  source: rule.walmart.forward_revenue_filter
  target: column.zs_observe.walmart_oms.order_status
  fields:
    edge_family: dependency_usage
    evidence_basis: Text references this documented column.
    confidence: high
    canonical_cognee_edge: true
    marketplace_only: true
    canonical_edge_type: USES_COLUMN
    inverse_edge_type: USED_BY_CARD
    materialize_inverse: false
    edge_class: canonical
    source_type: rule
    target_type: column
    evidence_refs:
    - ev.walmart.filters.001
    notes: Text references this documented column.
```

```yaml
candidate_edge:
  edge_id: edge.walmart.0774
  edge_type: USES_COLUMN
  source: rule.walmart.forward_revenue_filter
  target: column.zs_observe.walmart_settlement.transaction_type
  fields:
    edge_family: dependency_usage
    evidence_basis: Text references this documented column.
    confidence: high
    canonical_cognee_edge: true
    marketplace_only: true
    canonical_edge_type: USES_COLUMN
    inverse_edge_type: USED_BY_CARD
    materialize_inverse: false
    edge_class: canonical
    source_type: rule
    target_type: column
    evidence_refs:
    - ev.walmart.filters.001
    notes: Text references this documented column.
```

```yaml
candidate_edge:
  edge_id: edge.walmart.0775
  edge_type: USES_COLUMN
  source: rule.walmart.forward_revenue_filter
  target: column.zs_observe.walmart_settlement.internal_txn_type
  fields:
    edge_family: dependency_usage
    evidence_basis: Text references this documented column.
    confidence: high
    canonical_cognee_edge: true
    marketplace_only: true
    canonical_edge_type: USES_COLUMN
    inverse_edge_type: USED_BY_CARD
    materialize_inverse: false
    edge_class: canonical
    source_type: rule
    target_type: column
    evidence_refs:
    - ev.walmart.filters.001
    notes: Text references this documented column.
```

```yaml
candidate_edge:
  edge_id: edge.walmart.0776
  edge_type: USES_COLUMN
  source: rule.walmart.reverse_refund_filter
  target: column.zs_observe.walmart_settlement.transaction_type
  fields:
    edge_family: dependency_usage
    evidence_basis: Text references this documented column.
    confidence: high
    canonical_cognee_edge: true
    marketplace_only: true
    canonical_edge_type: USES_COLUMN
    inverse_edge_type: USED_BY_CARD
    materialize_inverse: false
    edge_class: canonical
    source_type: rule
    target_type: column
    evidence_refs:
    - ev.walmart.filters.001
    notes: Text references this documented column.
```

```yaml
candidate_edge:
  edge_id: edge.walmart.0777
  edge_type: USES_COLUMN
  source: rule.walmart.reverse_refund_filter
  target: column.zs_observe.walmart_settlement.internal_txn_type
  fields:
    edge_family: dependency_usage
    evidence_basis: Text references this documented column.
    confidence: high
    canonical_cognee_edge: true
    marketplace_only: true
    canonical_edge_type: USES_COLUMN
    inverse_edge_type: USED_BY_CARD
    materialize_inverse: false
    edge_class: canonical
    source_type: rule
    target_type: column
    evidence_refs:
    - ev.walmart.filters.001
    notes: Text references this documented column.
```

```yaml
candidate_edge:
  edge_id: edge.walmart.0778
  edge_type: USES_COLUMN
  source: rule.walmart.reverse_refund_filter
  target: column.zs_observe.walmart_settlement.other_type
  fields:
    edge_family: dependency_usage
    evidence_basis: Text references this documented column.
    confidence: high
    canonical_cognee_edge: true
    marketplace_only: true
    canonical_edge_type: USES_COLUMN
    inverse_edge_type: USED_BY_CARD
    materialize_inverse: false
    edge_class: canonical
    source_type: rule
    target_type: column
    evidence_refs:
    - ev.walmart.filters.001
    notes: Text references this documented column.
```

```yaml
candidate_edge:
  edge_id: edge.walmart.0779
  edge_type: USES_COLUMN
  source: rule.walmart.lookup_sku_not_null
  target: column.zs_observe.walmart_lookup.sku
  fields:
    edge_family: dependency_usage
    evidence_basis: Text references this documented column.
    confidence: high
    canonical_cognee_edge: true
    marketplace_only: true
    canonical_edge_type: USES_COLUMN
    inverse_edge_type: USED_BY_CARD
    materialize_inverse: false
    edge_class: canonical
    source_type: rule
    target_type: column
    evidence_refs:
    - ev.walmart_lookup.schema.001
    notes: Text references this documented column.
```

```yaml
candidate_edge:
  edge_id: edge.walmart.0780
  edge_type: USES_COLUMN
  source: rule.walmart.oms_clean_rows
  target: column.zs_observe.walmart_oms.order_status
  fields:
    edge_family: dependency_usage
    evidence_basis: Text references this documented column.
    confidence: high
    canonical_cognee_edge: true
    marketplace_only: true
    canonical_edge_type: USES_COLUMN
    inverse_edge_type: USED_BY_CARD
    materialize_inverse: false
    edge_class: canonical
    source_type: rule
    target_type: column
    evidence_refs:
    - ev.walmart_oms.quality.001
    notes: Text references this documented column.
```

```yaml
candidate_edge:
  edge_id: edge.walmart.0781
  edge_type: USES_COLUMN
  source: rule.walmart.oms_clean_rows
  target: column.zs_observe.walmart_oms.destination_state
  fields:
    edge_family: dependency_usage
    evidence_basis: Text references this documented column.
    confidence: high
    canonical_cognee_edge: true
    marketplace_only: true
    canonical_edge_type: USES_COLUMN
    inverse_edge_type: USED_BY_CARD
    materialize_inverse: false
    edge_class: canonical
    source_type: rule
    target_type: column
    evidence_refs:
    - ev.walmart_oms.quality.001
    notes: Text references this documented column.
```

```yaml
candidate_edge:
  edge_id: edge.walmart.0782
  edge_type: USES_COLUMN
  source: rule.walmart.oms_clean_rows
  target: column.zs_observe.walmart_oms.currency_type
  fields:
    edge_family: dependency_usage
    evidence_basis: Text references this documented column.
    confidence: high
    canonical_cognee_edge: true
    marketplace_only: true
    canonical_edge_type: USES_COLUMN
    inverse_edge_type: USED_BY_CARD
    materialize_inverse: false
    edge_class: canonical
    source_type: rule
    target_type: column
    evidence_refs:
    - ev.walmart_oms.quality.001
    notes: Text references this documented column.
```

```yaml
candidate_edge:
  edge_id: edge.walmart.0783
  edge_type: USES_COLUMN
  source: rule.walmart.compute_commission_rate
  target: column.zs_observe.walmart_settlement.charged_amount_excluding_tax
  fields:
    edge_family: dependency_usage
    evidence_basis: Text references this documented column.
    confidence: high
    canonical_cognee_edge: true
    marketplace_only: true
    canonical_edge_type: USES_COLUMN
    inverse_edge_type: USED_BY_CARD
    materialize_inverse: false
    edge_class: canonical
    source_type: rule
    target_type: column
    evidence_refs:
    - ev.walmart.quality.001
    notes: Text references this documented column.
```

```yaml
candidate_edge:
  edge_id: edge.walmart.0784
  edge_type: USES_COLUMN
  source: rule.walmart.compute_commission_rate
  target: column.zs_observe.walmart_settlement.gross_commission
  fields:
    edge_family: dependency_usage
    evidence_basis: Text references this documented column.
    confidence: high
    canonical_cognee_edge: true
    marketplace_only: true
    canonical_edge_type: USES_COLUMN
    inverse_edge_type: USED_BY_CARD
    materialize_inverse: false
    edge_class: canonical
    source_type: rule
    target_type: column
    evidence_refs:
    - ev.walmart.quality.001
    notes: Text references this documented column.
```

```yaml
candidate_edge:
  edge_id: edge.walmart.0785
  edge_type: USES_COLUMN
  source: rule.walmart.compute_commission_rate
  target: column.zs_observe.walmart_settlement.base_commission_rate
  fields:
    edge_family: dependency_usage
    evidence_basis: Text references this documented column.
    confidence: high
    canonical_cognee_edge: true
    marketplace_only: true
    canonical_edge_type: USES_COLUMN
    inverse_edge_type: USED_BY_CARD
    materialize_inverse: false
    edge_class: canonical
    source_type: rule
    target_type: column
    evidence_refs:
    - ev.walmart.quality.001
    notes: Text references this documented column.
```

```yaml
candidate_edge:
  edge_id: edge.walmart.0786
  edge_type: USES_COLUMN
  source: rule.walmart.compute_commission_rate
  target: column.zs_observe.walmart_settlement.commission_rate
  fields:
    edge_family: dependency_usage
    evidence_basis: Text references this documented column.
    confidence: high
    canonical_cognee_edge: true
    marketplace_only: true
    canonical_edge_type: USES_COLUMN
    inverse_edge_type: USED_BY_CARD
    materialize_inverse: false
    edge_class: canonical
    source_type: rule
    target_type: column
    evidence_refs:
    - ev.walmart.quality.001
    notes: Text references this documented column.
```

```yaml
candidate_edge:
  edge_id: edge.walmart.0787
  edge_type: USES_COLUMN
  source: rule.walmart.hsn_is_barcode
  target: column.zs_observe.walmart_oms.hsn
  fields:
    edge_family: dependency_usage
    evidence_basis: Explicit related column binding.
    confidence: high
    canonical_cognee_edge: true
    marketplace_only: true
    canonical_edge_type: USES_COLUMN
    inverse_edge_type: USED_BY_CARD
    materialize_inverse: false
    edge_class: canonical
    source_type: rule
    target_type: column
    evidence_refs:
    - ev.walmart_oms.quality.001
    notes: Explicit related column binding.
```

```yaml
candidate_edge:
  edge_id: edge.walmart.0788
  edge_type: USES_COLUMN
  source: rule.walmart.hsn_is_barcode
  target: column.zs_observe.walmart_oms.item_id
  fields:
    edge_family: dependency_usage
    evidence_basis: Text references this documented column.
    confidence: high
    canonical_cognee_edge: true
    marketplace_only: true
    canonical_edge_type: USES_COLUMN
    inverse_edge_type: USED_BY_CARD
    materialize_inverse: false
    edge_class: canonical
    source_type: rule
    target_type: column
    evidence_refs:
    - ev.walmart_oms.quality.001
    notes: Text references this documented column.
```

```yaml
candidate_edge:
  edge_id: edge.walmart.0789
  edge_type: USES_COLUMN
  source: rule.walmart.no_process_variants_from_segments
  target: column.zs_observe.walmart_settlement.product_type
  fields:
    edge_family: dependency_usage
    evidence_basis: Text references this documented column.
    confidence: high
    canonical_cognee_edge: true
    marketplace_only: true
    canonical_edge_type: USES_COLUMN
    inverse_edge_type: USED_BY_CARD
    materialize_inverse: false
    edge_class: canonical
    source_type: rule
    target_type: column
    evidence_refs:
    - ev.walmart.overview.001
    notes: Text references this documented column.
```

```yaml
candidate_edge:
  edge_id: edge.walmart.0790
  edge_type: USES_COLUMN
  source: rule.walmart.no_process_variants_from_segments
  target: column.zs_observe.walmart_settlement.currency
  fields:
    edge_family: dependency_usage
    evidence_basis: Text references this documented column.
    confidence: high
    canonical_cognee_edge: true
    marketplace_only: true
    canonical_edge_type: USES_COLUMN
    inverse_edge_type: USED_BY_CARD
    materialize_inverse: false
    edge_class: canonical
    source_type: rule
    target_type: column
    evidence_refs:
    - ev.walmart.overview.001
    notes: Text references this documented column.
```

```yaml
candidate_edge:
  edge_id: edge.walmart.0791
  edge_type: USES_COLUMN
  source: rule.walmart.group_level_scope_only
  target: column.zs_observe.walmart_settlement.group_level_id
  fields:
    edge_family: dependency_usage
    evidence_basis: Explicit related column binding.
    confidence: high
    canonical_cognee_edge: true
    marketplace_only: true
    canonical_edge_type: USES_COLUMN
    inverse_edge_type: USED_BY_CARD
    materialize_inverse: false
    edge_class: canonical
    source_type: rule
    target_type: column
    evidence_refs:
    - ev.walmart.filters.001
    notes: Explicit related column binding.
```

```yaml
candidate_edge:
  edge_id: edge.walmart.0792
  edge_type: USES_COLUMN
  source: rule.walmart.group_level_scope_only
  target: column.zs_observe.walmart_oms.group_level_id
  fields:
    edge_family: dependency_usage
    evidence_basis: Text references this documented column.
    confidence: high
    canonical_cognee_edge: true
    marketplace_only: true
    canonical_edge_type: USES_COLUMN
    inverse_edge_type: USED_BY_CARD
    materialize_inverse: false
    edge_class: canonical
    source_type: rule
    target_type: column
    evidence_refs:
    - ev.walmart.filters.001
    notes: Text references this documented column.
```

```yaml
candidate_edge:
  edge_id: edge.walmart.0793
  edge_type: USES_COLUMN
  source: rule.walmart.group_level_scope_only
  target: column.zs_observe.walmart_lookup.group_level_id
  fields:
    edge_family: dependency_usage
    evidence_basis: Text references this documented column.
    confidence: high
    canonical_cognee_edge: true
    marketplace_only: true
    canonical_edge_type: USES_COLUMN
    inverse_edge_type: USED_BY_CARD
    materialize_inverse: false
    edge_class: canonical
    source_type: rule
    target_type: column
    evidence_refs:
    - ev.walmart.filters.001
    notes: Text references this documented column.
```

```yaml
candidate_edge:
  edge_id: edge.walmart.0794
  edge_type: USES_COLUMN
  source: workflow_step.walmart.forward.order_created_in_oms
  target: column.zs_observe.walmart_oms.order_id
  fields:
    edge_family: dependency_usage
    evidence_basis: Text references this documented column.
    confidence: high
    canonical_cognee_edge: true
    marketplace_only: true
    canonical_edge_type: USES_COLUMN
    inverse_edge_type: USED_BY_CARD
    materialize_inverse: false
    edge_class: canonical
    source_type: workflow_step
    target_type: column
    evidence_refs:
    - ev.walmart.lifecycle.001
    notes: Text references this documented column.
```

```yaml
candidate_edge:
  edge_id: edge.walmart.0795
  edge_type: USES_COLUMN
  source: workflow_step.walmart.forward.order_created_in_oms
  target: column.zs_observe.walmart_oms.sku_id
  fields:
    edge_family: dependency_usage
    evidence_basis: Text references this documented column.
    confidence: high
    canonical_cognee_edge: true
    marketplace_only: true
    canonical_edge_type: USES_COLUMN
    inverse_edge_type: USED_BY_CARD
    materialize_inverse: false
    edge_class: canonical
    source_type: workflow_step
    target_type: column
    evidence_refs:
    - ev.walmart.lifecycle.001
    notes: Text references this documented column.
```

```yaml
candidate_edge:
  edge_id: edge.walmart.0796
  edge_type: USES_COLUMN
  source: workflow_step.walmart.forward.order_created_in_oms
  target: column.zs_observe.walmart_oms.created_date
  fields:
    edge_family: dependency_usage
    evidence_basis: Text references this documented column.
    confidence: high
    canonical_cognee_edge: true
    marketplace_only: true
    canonical_edge_type: USES_COLUMN
    inverse_edge_type: USED_BY_CARD
    materialize_inverse: false
    edge_class: canonical
    source_type: workflow_step
    target_type: column
    evidence_refs:
    - ev.walmart.lifecycle.001
    notes: Text references this documented column.
```

```yaml
candidate_edge:
  edge_id: edge.walmart.0797
  edge_type: USES_COLUMN
  source: workflow_step.walmart.forward.order_created_in_oms
  target: column.zs_observe.walmart_oms.charged_amount
  fields:
    edge_family: dependency_usage
    evidence_basis: Text references this documented column.
    confidence: high
    canonical_cognee_edge: true
    marketplace_only: true
    canonical_edge_type: USES_COLUMN
    inverse_edge_type: USED_BY_CARD
    materialize_inverse: false
    edge_class: canonical
    source_type: workflow_step
    target_type: column
    evidence_refs:
    - ev.walmart.lifecycle.001
    notes: Text references this documented column.
```

```yaml
candidate_edge:
  edge_id: edge.walmart.0798
  edge_type: USES_COLUMN
  source: workflow_step.walmart.forward.order_created_in_oms
  target: column.zs_observe.walmart_oms.internal_txn_type
  fields:
    edge_family: dependency_usage
    evidence_basis: Text references this documented column.
    confidence: high
    canonical_cognee_edge: true
    marketplace_only: true
    canonical_edge_type: USES_COLUMN
    inverse_edge_type: USED_BY_CARD
    materialize_inverse: false
    edge_class: canonical
    source_type: workflow_step
    target_type: column
    evidence_refs:
    - ev.walmart.lifecycle.001
    notes: Text references this documented column.
```

```yaml
candidate_edge:
  edge_id: edge.walmart.0799
  edge_type: USES_COLUMN
  source: workflow_step.walmart.forward.order_created_in_oms
  target: column.zs_observe.walmart_oms.order_status
  fields:
    edge_family: dependency_usage
    evidence_basis: Text references this documented column.
    confidence: high
    canonical_cognee_edge: true
    marketplace_only: true
    canonical_edge_type: USES_COLUMN
    inverse_edge_type: USED_BY_CARD
    materialize_inverse: false
    edge_class: canonical
    source_type: workflow_step
    target_type: column
    evidence_refs:
    - ev.walmart.lifecycle.001
    notes: Text references this documented column.
```

```yaml
candidate_edge:
  edge_id: edge.walmart.0800
  edge_type: USES_COLUMN
  source: workflow_step.walmart.forward.wfs_fulfilment
  target: column.zs_observe.walmart_settlement.fulfilment_channel
  fields:
    edge_family: dependency_usage
    evidence_basis: Explicit related column binding.
    confidence: high
    canonical_cognee_edge: true
    marketplace_only: true
    canonical_edge_type: USES_COLUMN
    inverse_edge_type: USED_BY_CARD
    materialize_inverse: false
    edge_class: canonical
    source_type: workflow_step
    target_type: column
    evidence_refs:
    - ev.walmart.business_model.001
    notes: Explicit related column binding.
```

```yaml
candidate_edge:
  edge_id: edge.walmart.0801
  edge_type: USES_COLUMN
  source: workflow_step.walmart.forward.delivered_sales_filter
  target: column.zs_observe.walmart_oms.order_status
  fields:
    edge_family: dependency_usage
    evidence_basis: Explicit related column binding.
    confidence: high
    canonical_cognee_edge: true
    marketplace_only: true
    canonical_edge_type: USES_COLUMN
    inverse_edge_type: USED_BY_CARD
    materialize_inverse: false
    edge_class: canonical
    source_type: workflow_step
    target_type: column
    evidence_refs:
    - ev.walmart.filters.001
    notes: Explicit related column binding.
```

```yaml
candidate_edge:
  edge_id: edge.walmart.0802
  edge_type: USES_COLUMN
  source: workflow_step.walmart.forward.delivered_sales_filter
  target: column.zs_observe.walmart_oms.internal_txn_type
  fields:
    edge_family: dependency_usage
    evidence_basis: Text references this documented column.
    confidence: high
    canonical_cognee_edge: true
    marketplace_only: true
    canonical_edge_type: USES_COLUMN
    inverse_edge_type: USED_BY_CARD
    materialize_inverse: false
    edge_class: canonical
    source_type: workflow_step
    target_type: column
    evidence_refs:
    - ev.walmart.filters.001
    notes: Text references this documented column.
```

```yaml
candidate_edge:
  edge_id: edge.walmart.0803
  edge_type: USES_COLUMN
  source: workflow_step.walmart.forward.delivered_sales_filter
  target: column.zs_observe.walmart_settlement.internal_txn_type
  fields:
    edge_family: dependency_usage
    evidence_basis: Text references this documented column.
    confidence: high
    canonical_cognee_edge: true
    marketplace_only: true
    canonical_edge_type: USES_COLUMN
    inverse_edge_type: USED_BY_CARD
    materialize_inverse: false
    edge_class: canonical
    source_type: workflow_step
    target_type: column
    evidence_refs:
    - ev.walmart.filters.001
    notes: Text references this documented column.
```

```yaml
candidate_edge:
  edge_id: edge.walmart.0804
  edge_type: USES_COLUMN
  source: workflow_step.walmart.forward.forward_settlement_row
  target: column.zs_observe.walmart_settlement.charged_amount
  fields:
    edge_family: dependency_usage
    evidence_basis: Text references this documented column.
    confidence: high
    canonical_cognee_edge: true
    marketplace_only: true
    canonical_edge_type: USES_COLUMN
    inverse_edge_type: USED_BY_CARD
    materialize_inverse: false
    edge_class: canonical
    source_type: workflow_step
    target_type: column
    evidence_refs:
    - ev.walmart.lifecycle.001
    notes: Text references this documented column.
```

```yaml
candidate_edge:
  edge_id: edge.walmart.0805
  edge_type: USES_COLUMN
  source: workflow_step.walmart.forward.forward_settlement_row
  target: column.zs_observe.walmart_settlement.charged_amount_excluding_tax
  fields:
    edge_family: dependency_usage
    evidence_basis: Text references this documented column.
    confidence: high
    canonical_cognee_edge: true
    marketplace_only: true
    canonical_edge_type: USES_COLUMN
    inverse_edge_type: USED_BY_CARD
    materialize_inverse: false
    edge_class: canonical
    source_type: workflow_step
    target_type: column
    evidence_refs:
    - ev.walmart.lifecycle.001
    notes: Text references this documented column.
```

```yaml
candidate_edge:
  edge_id: edge.walmart.0806
  edge_type: USES_COLUMN
  source: workflow_step.walmart.forward.forward_settlement_row
  target: column.zs_observe.walmart_settlement.total_tax
  fields:
    edge_family: dependency_usage
    evidence_basis: Text references this documented column.
    confidence: high
    canonical_cognee_edge: true
    marketplace_only: true
    canonical_edge_type: USES_COLUMN
    inverse_edge_type: USED_BY_CARD
    materialize_inverse: false
    edge_class: canonical
    source_type: workflow_step
    target_type: column
    evidence_refs:
    - ev.walmart.lifecycle.001
    notes: Text references this documented column.
```

```yaml
candidate_edge:
  edge_id: edge.walmart.0807
  edge_type: USES_COLUMN
  source: workflow_step.walmart.forward.forward_settlement_row
  target: column.zs_observe.walmart_settlement.gross_commission
  fields:
    edge_family: dependency_usage
    evidence_basis: Text references this documented column.
    confidence: high
    canonical_cognee_edge: true
    marketplace_only: true
    canonical_edge_type: USES_COLUMN
    inverse_edge_type: USED_BY_CARD
    materialize_inverse: false
    edge_class: canonical
    source_type: workflow_step
    target_type: column
    evidence_refs:
    - ev.walmart.lifecycle.001
    notes: Text references this documented column.
```

```yaml
candidate_edge:
  edge_id: edge.walmart.0808
  edge_type: USES_COLUMN
  source: workflow_step.walmart.forward.forward_settlement_row
  target: column.zs_observe.walmart_settlement.marketplace_withheld_tax
  fields:
    edge_family: dependency_usage
    evidence_basis: Text references this documented column.
    confidence: high
    canonical_cognee_edge: true
    marketplace_only: true
    canonical_edge_type: USES_COLUMN
    inverse_edge_type: USED_BY_CARD
    materialize_inverse: false
    edge_class: canonical
    source_type: workflow_step
    target_type: column
    evidence_refs:
    - ev.walmart.lifecycle.001
    notes: Text references this documented column.
```

```yaml
candidate_edge:
  edge_id: edge.walmart.0809
  edge_type: USES_COLUMN
  source: workflow_step.walmart.forward.forward_settlement_row
  target: column.zs_observe.walmart_settlement.transaction_type
  fields:
    edge_family: dependency_usage
    evidence_basis: Text references this documented column.
    confidence: high
    canonical_cognee_edge: true
    marketplace_only: true
    canonical_edge_type: USES_COLUMN
    inverse_edge_type: USED_BY_CARD
    materialize_inverse: false
    edge_class: canonical
    source_type: workflow_step
    target_type: column
    evidence_refs:
    - ev.walmart.lifecycle.001
    notes: Text references this documented column.
```

```yaml
candidate_edge:
  edge_id: edge.walmart.0810
  edge_type: USES_COLUMN
  source: workflow_step.walmart.forward.forward_settlement_row
  target: column.zs_observe.walmart_settlement.other_type
  fields:
    edge_family: dependency_usage
    evidence_basis: Text references this documented column.
    confidence: high
    canonical_cognee_edge: true
    marketplace_only: true
    canonical_edge_type: USES_COLUMN
    inverse_edge_type: USED_BY_CARD
    materialize_inverse: false
    edge_class: canonical
    source_type: workflow_step
    target_type: column
    evidence_refs:
    - ev.walmart.lifecycle.001
    notes: Text references this documented column.
```

```yaml
candidate_edge:
  edge_id: edge.walmart.0811
  edge_type: USES_COLUMN
  source: workflow_step.walmart.forward.net_payout_computed
  target: column.zs_observe.walmart_settlement.metadata_3
  fields:
    edge_family: dependency_usage
    evidence_basis: Text references this documented column.
    confidence: high
    canonical_cognee_edge: true
    marketplace_only: true
    canonical_edge_type: USES_COLUMN
    inverse_edge_type: USED_BY_CARD
    materialize_inverse: false
    edge_class: canonical
    source_type: workflow_step
    target_type: column
    evidence_refs:
    - ev.walmart.business_model.001
    notes: Text references this documented column.
```

```yaml
candidate_edge:
  edge_id: edge.walmart.0812
  edge_type: USES_COLUMN
  source: workflow_step.walmart.forward.net_payout_computed
  target: column.zs_observe.walmart_settlement.charged_amount_excluding_tax
  fields:
    edge_family: dependency_usage
    evidence_basis: Text references this documented column.
    confidence: high
    canonical_cognee_edge: true
    marketplace_only: true
    canonical_edge_type: USES_COLUMN
    inverse_edge_type: USED_BY_CARD
    materialize_inverse: false
    edge_class: canonical
    source_type: workflow_step
    target_type: column
    evidence_refs:
    - ev.walmart.business_model.001
    notes: Text references this documented column.
```

```yaml
candidate_edge:
  edge_id: edge.walmart.0813
  edge_type: USES_COLUMN
  source: workflow_step.walmart.forward.net_payout_computed
  target: column.zs_observe.walmart_settlement.gross_commission
  fields:
    edge_family: dependency_usage
    evidence_basis: Text references this documented column.
    confidence: high
    canonical_cognee_edge: true
    marketplace_only: true
    canonical_edge_type: USES_COLUMN
    inverse_edge_type: USED_BY_CARD
    materialize_inverse: false
    edge_class: canonical
    source_type: workflow_step
    target_type: column
    evidence_refs:
    - ev.walmart.business_model.001
    notes: Text references this documented column.
```

```yaml
candidate_edge:
  edge_id: edge.walmart.0814
  edge_type: USES_COLUMN
  source: workflow_step.walmart.forward.net_payout_computed
  target: column.zs_observe.walmart_settlement.settled_amount
  fields:
    edge_family: dependency_usage
    evidence_basis: Text references this documented column.
    confidence: high
    canonical_cognee_edge: true
    marketplace_only: true
    canonical_edge_type: USES_COLUMN
    inverse_edge_type: USED_BY_CARD
    materialize_inverse: false
    edge_class: canonical
    source_type: workflow_step
    target_type: column
    evidence_refs:
    - ev.walmart.business_model.001
    notes: Text references this documented column.
```

```yaml
candidate_edge:
  edge_id: edge.walmart.0815
  edge_type: USES_COLUMN
  source: workflow_step.walmart.refund.reverse_settlement_row
  target: column.zs_observe.walmart_settlement.transaction_type
  fields:
    edge_family: dependency_usage
    evidence_basis: Explicit related column binding.
    confidence: high
    canonical_cognee_edge: true
    marketplace_only: true
    canonical_edge_type: USES_COLUMN
    inverse_edge_type: USED_BY_CARD
    materialize_inverse: false
    edge_class: canonical
    source_type: workflow_step
    target_type: column
    evidence_refs:
    - ev.walmart.lifecycle.001
    notes: Explicit related column binding.
```

```yaml
candidate_edge:
  edge_id: edge.walmart.0816
  edge_type: USES_COLUMN
  source: workflow_step.walmart.refund.reverse_settlement_row
  target: column.zs_observe.walmart_settlement.charged_amount
  fields:
    edge_family: dependency_usage
    evidence_basis: Text references this documented column.
    confidence: high
    canonical_cognee_edge: true
    marketplace_only: true
    canonical_edge_type: USES_COLUMN
    inverse_edge_type: USED_BY_CARD
    materialize_inverse: false
    edge_class: canonical
    source_type: workflow_step
    target_type: column
    evidence_refs:
    - ev.walmart.lifecycle.001
    notes: Text references this documented column.
```

```yaml
candidate_edge:
  edge_id: edge.walmart.0817
  edge_type: USES_COLUMN
  source: workflow_step.walmart.refund.reverse_settlement_row
  target: column.zs_observe.walmart_settlement.gross_commission
  fields:
    edge_family: dependency_usage
    evidence_basis: Text references this documented column.
    confidence: high
    canonical_cognee_edge: true
    marketplace_only: true
    canonical_edge_type: USES_COLUMN
    inverse_edge_type: USED_BY_CARD
    materialize_inverse: false
    edge_class: canonical
    source_type: workflow_step
    target_type: column
    evidence_refs:
    - ev.walmart.lifecycle.001
    notes: Text references this documented column.
```

```yaml
candidate_edge:
  edge_id: edge.walmart.0818
  edge_type: USES_COLUMN
  source: workflow_step.walmart.refund.reverse_settlement_row
  target: column.zs_observe.walmart_settlement.marketplace_withheld_tax
  fields:
    edge_family: dependency_usage
    evidence_basis: Text references this documented column.
    confidence: high
    canonical_cognee_edge: true
    marketplace_only: true
    canonical_edge_type: USES_COLUMN
    inverse_edge_type: USED_BY_CARD
    materialize_inverse: false
    edge_class: canonical
    source_type: workflow_step
    target_type: column
    evidence_refs:
    - ev.walmart.lifecycle.001
    notes: Text references this documented column.
```

```yaml
candidate_edge:
  edge_id: edge.walmart.0819
  edge_type: USES_COLUMN
  source: workflow_step.walmart.refund.reverse_settlement_row
  target: column.zs_observe.walmart_settlement.other_type
  fields:
    edge_family: dependency_usage
    evidence_basis: Text references this documented column.
    confidence: high
    canonical_cognee_edge: true
    marketplace_only: true
    canonical_edge_type: USES_COLUMN
    inverse_edge_type: USED_BY_CARD
    materialize_inverse: false
    edge_class: canonical
    source_type: workflow_step
    target_type: column
    evidence_refs:
    - ev.walmart.lifecycle.001
    notes: Text references this documented column.
```

```yaml
candidate_edge:
  edge_id: edge.walmart.0820
  edge_type: USES_COLUMN
  source: workflow_step.walmart.refund.next_payout_deduction
  target: column.zs_observe.walmart_oms.order_id
  fields:
    edge_family: dependency_usage
    evidence_basis: Text references this documented column.
    confidence: high
    canonical_cognee_edge: true
    marketplace_only: true
    canonical_edge_type: USES_COLUMN
    inverse_edge_type: USED_BY_CARD
    materialize_inverse: false
    edge_class: canonical
    source_type: workflow_step
    target_type: column
    evidence_refs:
    - ev.walmart.lifecycle.001
    notes: Text references this documented column.
```

```yaml
candidate_edge:
  edge_id: edge.walmart.0821
  edge_type: USES_COLUMN
  source: workflow_step.walmart.refund.next_payout_deduction
  target: column.zs_observe.walmart_oms.sku_id
  fields:
    edge_family: dependency_usage
    evidence_basis: Text references this documented column.
    confidence: high
    canonical_cognee_edge: true
    marketplace_only: true
    canonical_edge_type: USES_COLUMN
    inverse_edge_type: USED_BY_CARD
    materialize_inverse: false
    edge_class: canonical
    source_type: workflow_step
    target_type: column
    evidence_refs:
    - ev.walmart.lifecycle.001
    notes: Text references this documented column.
```

```yaml
candidate_edge:
  edge_id: edge.walmart.0822
  edge_type: USES_COLUMN
  source: workflow_step.walmart.refund.next_payout_deduction
  target: column.zs_observe.walmart_settlement.order_id
  fields:
    edge_family: dependency_usage
    evidence_basis: Text references this documented column.
    confidence: high
    canonical_cognee_edge: true
    marketplace_only: true
    canonical_edge_type: USES_COLUMN
    inverse_edge_type: USED_BY_CARD
    materialize_inverse: false
    edge_class: canonical
    source_type: workflow_step
    target_type: column
    evidence_refs:
    - ev.walmart.lifecycle.001
    notes: Text references this documented column.
```

```yaml
candidate_edge:
  edge_id: edge.walmart.0823
  edge_type: USES_COLUMN
  source: workflow_step.walmart.refund.next_payout_deduction
  target: column.zs_observe.walmart_settlement.sku_id
  fields:
    edge_family: dependency_usage
    evidence_basis: Text references this documented column.
    confidence: high
    canonical_cognee_edge: true
    marketplace_only: true
    canonical_edge_type: USES_COLUMN
    inverse_edge_type: USED_BY_CARD
    materialize_inverse: false
    edge_class: canonical
    source_type: workflow_step
    target_type: column
    evidence_refs:
    - ev.walmart.lifecycle.001
    notes: Text references this documented column.
```

```yaml
candidate_edge:
  edge_id: edge.walmart.0824
  edge_type: USES_COLUMN
  source: workflow_step.walmart.refund.next_payout_deduction
  target: column.zs_observe.walmart_lookup.sku_id
  fields:
    edge_family: dependency_usage
    evidence_basis: Text references this documented column.
    confidence: high
    canonical_cognee_edge: true
    marketplace_only: true
    canonical_edge_type: USES_COLUMN
    inverse_edge_type: USED_BY_CARD
    materialize_inverse: false
    edge_class: canonical
    source_type: workflow_step
    target_type: column
    evidence_refs:
    - ev.walmart.lifecycle.001
    notes: Text references this documented column.
```

```yaml
candidate_edge:
  edge_id: edge.walmart.0825
  edge_type: USES_COLUMN
  source: workflow_step.walmart.cancel.cancelled_in_oms
  target: column.zs_observe.walmart_oms.order_status
  fields:
    edge_family: dependency_usage
    evidence_basis: Explicit related column binding.
    confidence: high
    canonical_cognee_edge: true
    marketplace_only: true
    canonical_edge_type: USES_COLUMN
    inverse_edge_type: USED_BY_CARD
    materialize_inverse: false
    edge_class: canonical
    source_type: workflow_step
    target_type: column
    evidence_refs:
    - ev.walmart.lifecycle.001
    notes: Explicit related column binding.
```

```yaml
candidate_edge:
  edge_id: edge.walmart.0826
  edge_type: USES_COLUMN
  source: workflow_step.walmart.catalogue.filter_usable_sku_rows
  target: column.zs_observe.walmart_lookup.sku
  fields:
    edge_family: dependency_usage
    evidence_basis: Explicit related column binding.
    confidence: high
    canonical_cognee_edge: true
    marketplace_only: true
    canonical_edge_type: USES_COLUMN
    inverse_edge_type: USED_BY_CARD
    materialize_inverse: false
    edge_class: canonical
    source_type: workflow_step
    target_type: column
    evidence_refs:
    - ev.walmart_lookup.schema.001
    notes: Explicit related column binding.
```

```yaml
candidate_edge:
  edge_id: edge.walmart.0827
  edge_type: USES_COLUMN
  source: workflow_step.walmart.catalogue.enrich_oms_settlement
  target: column.zs_observe.walmart_oms.sku_id
  fields:
    edge_family: dependency_usage
    evidence_basis: Text references this documented column.
    confidence: high
    canonical_cognee_edge: true
    marketplace_only: true
    canonical_edge_type: USES_COLUMN
    inverse_edge_type: USED_BY_CARD
    materialize_inverse: false
    edge_class: canonical
    source_type: workflow_step
    target_type: column
    evidence_refs:
    - ev.walmart.relationships.001
    notes: Text references this documented column.
```

```yaml
candidate_edge:
  edge_id: edge.walmart.0828
  edge_type: USES_COLUMN
  source: workflow_step.walmart.catalogue.enrich_oms_settlement
  target: column.zs_observe.walmart_oms.item_name
  fields:
    edge_family: dependency_usage
    evidence_basis: Text references this documented column.
    confidence: high
    canonical_cognee_edge: true
    marketplace_only: true
    canonical_edge_type: USES_COLUMN
    inverse_edge_type: USED_BY_CARD
    materialize_inverse: false
    edge_class: canonical
    source_type: workflow_step
    target_type: column
    evidence_refs:
    - ev.walmart.relationships.001
    notes: Text references this documented column.
```

```yaml
candidate_edge:
  edge_id: edge.walmart.0829
  edge_type: USES_COLUMN
  source: workflow_step.walmart.catalogue.enrich_oms_settlement
  target: column.zs_observe.walmart_settlement.sku_id
  fields:
    edge_family: dependency_usage
    evidence_basis: Text references this documented column.
    confidence: high
    canonical_cognee_edge: true
    marketplace_only: true
    canonical_edge_type: USES_COLUMN
    inverse_edge_type: USED_BY_CARD
    materialize_inverse: false
    edge_class: canonical
    source_type: workflow_step
    target_type: column
    evidence_refs:
    - ev.walmart.relationships.001
    notes: Text references this documented column.
```

```yaml
candidate_edge:
  edge_id: edge.walmart.0830
  edge_type: USES_COLUMN
  source: workflow_step.walmart.catalogue.enrich_oms_settlement
  target: column.zs_observe.walmart_lookup.sku_id
  fields:
    edge_family: dependency_usage
    evidence_basis: Text references this documented column.
    confidence: high
    canonical_cognee_edge: true
    marketplace_only: true
    canonical_edge_type: USES_COLUMN
    inverse_edge_type: USED_BY_CARD
    materialize_inverse: false
    edge_class: canonical
    source_type: workflow_step
    target_type: column
    evidence_refs:
    - ev.walmart.relationships.001
    notes: Text references this documented column.
```

```yaml
candidate_edge:
  edge_id: edge.walmart.0831
  edge_type: USES_COLUMN
  source: workflow_step.walmart.catalogue.enrich_oms_settlement
  target: column.zs_observe.walmart_lookup.sku
  fields:
    edge_family: dependency_usage
    evidence_basis: Text references this documented column.
    confidence: high
    canonical_cognee_edge: true
    marketplace_only: true
    canonical_edge_type: USES_COLUMN
    inverse_edge_type: USED_BY_CARD
    materialize_inverse: false
    edge_class: canonical
    source_type: workflow_step
    target_type: column
    evidence_refs:
    - ev.walmart.relationships.001
    notes: Text references this documented column.
```

```yaml
candidate_edge:
  edge_id: edge.walmart.0832
  edge_type: USES_COLUMN
  source: workflow_step.walmart.catalogue.enrich_oms_settlement
  target: column.zs_observe.walmart_lookup.item_name
  fields:
    edge_family: dependency_usage
    evidence_basis: Text references this documented column.
    confidence: high
    canonical_cognee_edge: true
    marketplace_only: true
    canonical_edge_type: USES_COLUMN
    inverse_edge_type: USED_BY_CARD
    materialize_inverse: false
    edge_class: canonical
    source_type: workflow_step
    target_type: column
    evidence_refs:
    - ev.walmart.relationships.001
    notes: Text references this documented column.
```

```yaml
candidate_edge:
  edge_id: edge.walmart.0833
  edge_type: USES_COLUMN
  source: query_pattern.walmart.oms_aov
  target: column.zs_observe.walmart_settlement.charged_amount
  fields:
    edge_family: dependency_usage
    evidence_basis: Text references this documented column.
    confidence: high
    canonical_cognee_edge: true
    marketplace_only: true
    canonical_edge_type: USES_COLUMN
    inverse_edge_type: USED_BY_CARD
    materialize_inverse: false
    edge_class: canonical
    source_type: query_pattern
    target_type: column
    evidence_refs:
    - ev.walmart.metrics.001
    notes: Text references this documented column.
```

```yaml
candidate_edge:
  edge_id: edge.walmart.0834
  edge_type: USES_COLUMN
  source: query_pattern.walmart.monthly_revenue
  target: column.zs_observe.walmart_oms.metadata_2
  fields:
    edge_family: dependency_usage
    evidence_basis: Text references this documented column.
    confidence: high
    canonical_cognee_edge: true
    marketplace_only: true
    canonical_edge_type: USES_COLUMN
    inverse_edge_type: USED_BY_CARD
    materialize_inverse: false
    edge_class: canonical
    source_type: query_pattern
    target_type: column
    evidence_refs:
    - ev.walmart.metrics.001
    notes: Text references this documented column.
```

```yaml
candidate_edge:
  edge_id: edge.walmart.0835
  edge_type: USES_COLUMN
  source: query_pattern.walmart.top_skus
  target: column.zs_observe.walmart_oms.sku_id
  fields:
    edge_family: dependency_usage
    evidence_basis: Text references this documented column.
    confidence: high
    canonical_cognee_edge: true
    marketplace_only: true
    canonical_edge_type: USES_COLUMN
    inverse_edge_type: USED_BY_CARD
    materialize_inverse: false
    edge_class: canonical
    source_type: query_pattern
    target_type: column
    evidence_refs:
    - ev.walmart.metrics.001
    notes: Text references this documented column.
```

```yaml
candidate_edge:
  edge_id: edge.walmart.0836
  edge_type: USES_COLUMN
  source: query_pattern.walmart.top_skus
  target: column.zs_observe.walmart_oms.item_name
  fields:
    edge_family: dependency_usage
    evidence_basis: Text references this documented column.
    confidence: high
    canonical_cognee_edge: true
    marketplace_only: true
    canonical_edge_type: USES_COLUMN
    inverse_edge_type: USED_BY_CARD
    materialize_inverse: false
    edge_class: canonical
    source_type: query_pattern
    target_type: column
    evidence_refs:
    - ev.walmart.metrics.001
    notes: Text references this documented column.
```

```yaml
candidate_edge:
  edge_id: edge.walmart.0837
  edge_type: USES_COLUMN
  source: query_pattern.walmart.state_distribution
  target: column.zs_observe.walmart_settlement.destination_state
  fields:
    edge_family: dependency_usage
    evidence_basis: Text references this documented column.
    confidence: high
    canonical_cognee_edge: true
    marketplace_only: true
    canonical_edge_type: USES_COLUMN
    inverse_edge_type: USED_BY_CARD
    materialize_inverse: false
    edge_class: canonical
    source_type: query_pattern
    target_type: column
    evidence_refs:
    - ev.walmart.metrics.001
    notes: Text references this documented column.
```

```yaml
candidate_edge:
  edge_id: edge.walmart.0838
  edge_type: USES_COLUMN
  source: query_pattern.walmart.payout_cycle
  target: column.zs_observe.walmart_oms.metadata_2
  fields:
    edge_family: dependency_usage
    evidence_basis: Text references this documented column.
    confidence: high
    canonical_cognee_edge: true
    marketplace_only: true
    canonical_edge_type: USES_COLUMN
    inverse_edge_type: USED_BY_CARD
    materialize_inverse: false
    edge_class: canonical
    source_type: query_pattern
    target_type: column
    evidence_refs:
    - ev.walmart.metrics.001
    notes: Text references this documented column.
```

```yaml
candidate_edge:
  edge_id: edge.walmart.0839
  edge_type: USES_COLUMN
  source: query_pattern.walmart.refund_sale_match
  target: column.zs_observe.walmart_oms.order_id
  fields:
    edge_family: dependency_usage
    evidence_basis: Text references this documented column.
    confidence: high
    canonical_cognee_edge: true
    marketplace_only: true
    canonical_edge_type: USES_COLUMN
    inverse_edge_type: USED_BY_CARD
    materialize_inverse: false
    edge_class: canonical
    source_type: query_pattern
    target_type: column
    evidence_refs:
    - ev.walmart.reconciliation.001
    notes: Text references this documented column.
```

```yaml
candidate_edge:
  edge_id: edge.walmart.0840
  edge_type: USES_COLUMN
  source: query_pattern.walmart.mpf_tax_validation
  target: column.zs_observe.walmart_oms.charged_amount
  fields:
    edge_family: dependency_usage
    evidence_basis: Text references this documented column.
    confidence: high
    canonical_cognee_edge: true
    marketplace_only: true
    canonical_edge_type: USES_COLUMN
    inverse_edge_type: USED_BY_CARD
    materialize_inverse: false
    edge_class: canonical
    source_type: query_pattern
    target_type: column
    evidence_refs:
    - ev.walmart.business_model.001
    notes: Text references this documented column.
```

```yaml
candidate_edge:
  edge_id: edge.walmart.0841
  edge_type: USES_COLUMN
  source: validation_test.walmart.mandatory_filters
  target: column.zs_observe.walmart_settlement.group_level_id
  fields:
    edge_family: dependency_usage
    evidence_basis: Text references this documented column.
    confidence: high
    canonical_cognee_edge: true
    marketplace_only: true
    canonical_edge_type: USES_COLUMN
    inverse_edge_type: USED_BY_CARD
    materialize_inverse: false
    edge_class: canonical
    source_type: validation_test
    target_type: column
    evidence_refs:
    - ev.walmart.filters.001
    notes: Text references this documented column.
```

```yaml
candidate_edge:
  edge_id: edge.walmart.0842
  edge_type: USES_COLUMN
  source: validation_test.walmart.mandatory_filters
  target: column.zs_observe.walmart_settlement.is_active
  fields:
    edge_family: dependency_usage
    evidence_basis: Text references this documented column.
    confidence: high
    canonical_cognee_edge: true
    marketplace_only: true
    canonical_edge_type: USES_COLUMN
    inverse_edge_type: USED_BY_CARD
    materialize_inverse: false
    edge_class: canonical
    source_type: validation_test
    target_type: column
    evidence_refs:
    - ev.walmart.filters.001
    notes: Text references this documented column.
```

```yaml
candidate_edge:
  edge_id: edge.walmart.0843
  edge_type: USES_COLUMN
  source: validation_test.walmart.mandatory_filters
  target: column.zs_observe.walmart_lookup.group_level_id
  fields:
    edge_family: dependency_usage
    evidence_basis: Text references this documented column.
    confidence: high
    canonical_cognee_edge: true
    marketplace_only: true
    canonical_edge_type: USES_COLUMN
    inverse_edge_type: USED_BY_CARD
    materialize_inverse: false
    edge_class: canonical
    source_type: validation_test
    target_type: column
    evidence_refs:
    - ev.walmart.filters.001
    notes: Text references this documented column.
```

```yaml
candidate_edge:
  edge_id: edge.walmart.0844
  edge_type: USES_COLUMN
  source: validation_test.walmart.mandatory_filters
  target: column.zs_observe.walmart_lookup.is_active
  fields:
    edge_family: dependency_usage
    evidence_basis: Text references this documented column.
    confidence: high
    canonical_cognee_edge: true
    marketplace_only: true
    canonical_edge_type: USES_COLUMN
    inverse_edge_type: USED_BY_CARD
    materialize_inverse: false
    edge_class: canonical
    source_type: validation_test
    target_type: column
    evidence_refs:
    - ev.walmart.filters.001
    notes: Text references this documented column.
```

```yaml
candidate_edge:
  edge_id: edge.walmart.0845
  edge_type: USES_COLUMN
  source: validation_test.walmart.mpf_tax_identity
  target: column.zs_observe.walmart_oms.charged_amount
  fields:
    edge_family: dependency_usage
    evidence_basis: Text references this documented column.
    confidence: high
    canonical_cognee_edge: true
    marketplace_only: true
    canonical_edge_type: USES_COLUMN
    inverse_edge_type: USED_BY_CARD
    materialize_inverse: false
    edge_class: canonical
    source_type: validation_test
    target_type: column
    evidence_refs:
    - ev.walmart.business_model.001
    notes: Text references this documented column.
```

```yaml
candidate_edge:
  edge_id: edge.walmart.0846
  edge_type: USES_COLUMN
  source: validation_test.walmart.oms_clean_rows
  target: column.zs_observe.walmart_settlement.currency
  fields:
    edge_family: dependency_usage
    evidence_basis: Text references this documented column.
    confidence: high
    canonical_cognee_edge: true
    marketplace_only: true
    canonical_edge_type: USES_COLUMN
    inverse_edge_type: USED_BY_CARD
    materialize_inverse: false
    edge_class: canonical
    source_type: validation_test
    target_type: column
    evidence_refs:
    - ev.walmart_oms.quality.001
    notes: Text references this documented column.
```

```yaml
candidate_edge:
  edge_id: edge.walmart.0847
  edge_type: HAS_VALUE_PROFILE
  source: column.zs_observe.walmart_oms.order_status
  target: value_profile.walmart.oms.order_status
  fields:
    edge_family: business_hierarchy_in_scope
    evidence_basis: Column has value profile.
    confidence: high
    canonical_cognee_edge: true
    marketplace_only: true
    canonical_edge_type: HAS_VALUE_PROFILE
    inverse_edge_type: PROFILES_COLUMN_OR_TABLE
    materialize_inverse: false
    edge_class: canonical
    source_type: column
    target_type: value_profile
    evidence_refs:
    - ev.walmart_oms.schema.001
    notes: Column has value profile.
```

```yaml
candidate_edge:
  edge_id: edge.walmart.0848
  edge_type: HAS_VALUE_PROFILE
  source: column.zs_observe.walmart_settlement.transaction_type
  target: value_profile.walmart.settlement.transaction_type
  fields:
    edge_family: business_hierarchy_in_scope
    evidence_basis: Column has value profile.
    confidence: high
    canonical_cognee_edge: true
    marketplace_only: true
    canonical_edge_type: HAS_VALUE_PROFILE
    inverse_edge_type: PROFILES_COLUMN_OR_TABLE
    materialize_inverse: false
    edge_class: canonical
    source_type: column
    target_type: value_profile
    evidence_refs:
    - ev.walmart_settlement.values.001
    notes: Column has value profile.
```

```yaml
candidate_edge:
  edge_id: edge.walmart.0849
  edge_type: HAS_VALUE_PROFILE
  source: column.zs_observe.walmart_settlement.internal_txn_type
  target: value_profile.walmart.settlement.internal_txn_type
  fields:
    edge_family: business_hierarchy_in_scope
    evidence_basis: Column has value profile.
    confidence: high
    canonical_cognee_edge: true
    marketplace_only: true
    canonical_edge_type: HAS_VALUE_PROFILE
    inverse_edge_type: PROFILES_COLUMN_OR_TABLE
    materialize_inverse: false
    edge_class: canonical
    source_type: column
    target_type: value_profile
    evidence_refs:
    - ev.walmart.quality.001
    notes: Column has value profile.
```

```yaml
candidate_edge:
  edge_id: edge.walmart.0850
  edge_type: HAS_VALUE_PROFILE
  source: column.zs_observe.walmart_settlement.other_type
  target: value_profile.walmart.settlement.other_type
  fields:
    edge_family: business_hierarchy_in_scope
    evidence_basis: Column has value profile.
    confidence: high
    canonical_cognee_edge: true
    marketplace_only: true
    canonical_edge_type: HAS_VALUE_PROFILE
    inverse_edge_type: PROFILES_COLUMN_OR_TABLE
    materialize_inverse: false
    edge_class: canonical
    source_type: column
    target_type: value_profile
    evidence_refs:
    - ev.walmart.quality.001
    notes: Column has value profile.
```

```yaml
candidate_edge:
  edge_id: edge.walmart.0851
  edge_type: HAS_VALUE_PROFILE
  source: column.zs_observe.walmart_settlement.fulfilment_channel
  target: value_profile.walmart.settlement.fulfilment_channel
  fields:
    edge_family: business_hierarchy_in_scope
    evidence_basis: Column has value profile.
    confidence: high
    canonical_cognee_edge: true
    marketplace_only: true
    canonical_edge_type: HAS_VALUE_PROFILE
    inverse_edge_type: PROFILES_COLUMN_OR_TABLE
    materialize_inverse: false
    edge_class: canonical
    source_type: column
    target_type: value_profile
    evidence_refs:
    - ev.walmart.business_model.001
    notes: Column has value profile.
```

```yaml
candidate_edge:
  edge_id: edge.walmart.0852
  edge_type: HAS_VALUE_PROFILE
  source: column.zs_observe.walmart_settlement.product_category
  target: value_profile.walmart.settlement.product_category
  fields:
    edge_family: business_hierarchy_in_scope
    evidence_basis: Column has value profile.
    confidence: high
    canonical_cognee_edge: true
    marketplace_only: true
    canonical_edge_type: HAS_VALUE_PROFILE
    inverse_edge_type: PROFILES_COLUMN_OR_TABLE
    materialize_inverse: false
    edge_class: canonical
    source_type: column
    target_type: value_profile
    evidence_refs:
    - ev.walmart_settlement.values.001
    notes: Column has value profile.
```

```yaml
candidate_edge:
  edge_id: edge.walmart.0853
  edge_type: HAS_VALUE_PROFILE
  source: column.zs_observe.walmart_settlement.product_type
  target: value_profile.walmart.settlement.product_type
  fields:
    edge_family: business_hierarchy_in_scope
    evidence_basis: Column has value profile.
    confidence: high
    canonical_cognee_edge: true
    marketplace_only: true
    canonical_edge_type: HAS_VALUE_PROFILE
    inverse_edge_type: PROFILES_COLUMN_OR_TABLE
    materialize_inverse: false
    edge_class: canonical
    source_type: column
    target_type: value_profile
    evidence_refs:
    - ev.walmart_settlement.values.001
    notes: Column has value profile.
```

```yaml
candidate_edge:
  edge_id: edge.walmart.0854
  edge_type: HAS_VALUE_PROFILE
  source: column.zs_observe.walmart_settlement.product_tax_code
  target: value_profile.walmart.settlement.product_tax_code
  fields:
    edge_family: business_hierarchy_in_scope
    evidence_basis: Column has value profile.
    confidence: high
    canonical_cognee_edge: true
    marketplace_only: true
    canonical_edge_type: HAS_VALUE_PROFILE
    inverse_edge_type: PROFILES_COLUMN_OR_TABLE
    materialize_inverse: false
    edge_class: canonical
    source_type: column
    target_type: value_profile
    evidence_refs:
    - ev.walmart_settlement.values.001
    notes: Column has value profile.
```

```yaml
candidate_edge:
  edge_id: edge.walmart.0855
  edge_type: HAS_VALUE_PROFILE
  source: table.zs_observe.walmart_lookup
  target: value_profile.walmart.lookup.row_type
  fields:
    edge_family: business_hierarchy_in_scope
    evidence_basis: Column has value profile.
    confidence: high
    canonical_cognee_edge: true
    marketplace_only: true
    canonical_edge_type: HAS_VALUE_PROFILE
    inverse_edge_type: PROFILES_COLUMN_OR_TABLE
    materialize_inverse: false
    edge_class: canonical
    source_type: table
    target_type: value_profile
    evidence_refs:
    - ev.walmart_lookup.schema.001
    notes: Column has value profile.
```

```yaml
candidate_edge:
  edge_id: edge.walmart.0856
  edge_type: HAS_VALUE_PROFILE
  source: column.zs_observe.walmart_settlement.currency_type
  target: value_profile.walmart.currency_type
  fields:
    edge_family: business_hierarchy_in_scope
    evidence_basis: Column has value profile.
    confidence: high
    canonical_cognee_edge: true
    marketplace_only: true
    canonical_edge_type: HAS_VALUE_PROFILE
    inverse_edge_type: PROFILES_COLUMN_OR_TABLE
    materialize_inverse: false
    edge_class: canonical
    source_type: column
    target_type: value_profile
    evidence_refs:
    - ev.walmart.overview.001
    notes: Column has value profile.
```

```yaml
candidate_edge:
  edge_id: edge.walmart.0857
  edge_type: HAS_VALUE_PROFILE
  source: column.zs_observe.walmart_settlement.group_level_id
  target: value_profile.walmart.group_level_id
  fields:
    edge_family: business_hierarchy_in_scope
    evidence_basis: Column has value profile.
    confidence: high
    canonical_cognee_edge: true
    marketplace_only: true
    canonical_edge_type: HAS_VALUE_PROFILE
    inverse_edge_type: PROFILES_COLUMN_OR_TABLE
    materialize_inverse: false
    edge_class: canonical
    source_type: column
    target_type: value_profile
    evidence_refs:
    - ev.walmart.filters.001
    notes: Column has value profile.
```

```yaml
candidate_edge:
  edge_id: edge.walmart.0858
  edge_type: USES_COLUMN
  source: state_transition.walmart.oms_acknowledged_to_shipped
  target: column.zs_observe.walmart_oms.order_status
  fields:
    edge_family: dependency_usage
    evidence_basis: State transition uses this state column.
    confidence: high
    canonical_cognee_edge: true
    marketplace_only: true
    canonical_edge_type: USES_COLUMN
    inverse_edge_type: USED_BY_CARD
    materialize_inverse: false
    edge_class: canonical
    source_type: state_transition
    target_type: column
    evidence_refs:
    - ev.walmart.lifecycle.001
    notes: State transition uses this state column.
```

```yaml
candidate_edge:
  edge_id: edge.walmart.0859
  edge_type: PART_OF_PROCESS
  source: state_transition.walmart.oms_acknowledged_to_shipped
  target: business_process.walmart.forward_wfs_sale_to_payout
  fields:
    edge_family: business_process_flow
    evidence_basis: State transition is bound to this business process.
    confidence: high
    canonical_cognee_edge: true
    marketplace_only: true
    canonical_edge_type: PART_OF_PROCESS
    inverse_edge_type: HAS_STATE_TRANSITION
    materialize_inverse: false
    edge_class: canonical
    source_type: state_transition
    target_type: business_process
    evidence_refs:
    - ev.walmart.lifecycle.001
    notes: State transition is bound to this business process.
```

```yaml
candidate_edge:
  edge_id: edge.walmart.0860
  edge_type: USES_COLUMN
  source: state_transition.walmart.oms_shipped_to_delivered
  target: column.zs_observe.walmart_oms.order_status
  fields:
    edge_family: dependency_usage
    evidence_basis: State transition uses this state column.
    confidence: high
    canonical_cognee_edge: true
    marketplace_only: true
    canonical_edge_type: USES_COLUMN
    inverse_edge_type: USED_BY_CARD
    materialize_inverse: false
    edge_class: canonical
    source_type: state_transition
    target_type: column
    evidence_refs:
    - ev.walmart.lifecycle.001
    notes: State transition uses this state column.
```

```yaml
candidate_edge:
  edge_id: edge.walmart.0861
  edge_type: PART_OF_PROCESS
  source: state_transition.walmart.oms_shipped_to_delivered
  target: business_process.walmart.forward_wfs_sale_to_payout
  fields:
    edge_family: business_process_flow
    evidence_basis: State transition is bound to this business process.
    confidence: high
    canonical_cognee_edge: true
    marketplace_only: true
    canonical_edge_type: PART_OF_PROCESS
    inverse_edge_type: HAS_STATE_TRANSITION
    materialize_inverse: false
    edge_class: canonical
    source_type: state_transition
    target_type: business_process
    evidence_refs:
    - ev.walmart.lifecycle.001
    notes: State transition is bound to this business process.
```

```yaml
candidate_edge:
  edge_id: edge.walmart.0862
  edge_type: USES_COLUMN
  source: state_transition.walmart.oms_to_cancelled
  target: column.zs_observe.walmart_oms.order_status
  fields:
    edge_family: dependency_usage
    evidence_basis: State transition uses this state column.
    confidence: high
    canonical_cognee_edge: true
    marketplace_only: true
    canonical_edge_type: USES_COLUMN
    inverse_edge_type: USED_BY_CARD
    materialize_inverse: false
    edge_class: canonical
    source_type: state_transition
    target_type: column
    evidence_refs:
    - ev.walmart.lifecycle.001
    notes: State transition uses this state column.
```

```yaml
candidate_edge:
  edge_id: edge.walmart.0863
  edge_type: PART_OF_PROCESS
  source: state_transition.walmart.oms_to_cancelled
  target: business_process.walmart.cancellation_without_settlement
  fields:
    edge_family: business_process_flow
    evidence_basis: State transition is bound to this business process.
    confidence: high
    canonical_cognee_edge: true
    marketplace_only: true
    canonical_edge_type: PART_OF_PROCESS
    inverse_edge_type: HAS_STATE_TRANSITION
    materialize_inverse: false
    edge_class: canonical
    source_type: state_transition
    target_type: business_process
    evidence_refs:
    - ev.walmart.lifecycle.001
    notes: State transition is bound to this business process.
```

```yaml
candidate_edge:
  edge_id: edge.walmart.0864
  edge_type: USES_COLUMN
  source: state_transition.walmart.settlement_sale_to_refund
  target: column.zs_observe.walmart_settlement.transaction_type
  fields:
    edge_family: dependency_usage
    evidence_basis: State transition uses this state column.
    confidence: high
    canonical_cognee_edge: true
    marketplace_only: true
    canonical_edge_type: USES_COLUMN
    inverse_edge_type: USED_BY_CARD
    materialize_inverse: false
    edge_class: canonical
    source_type: state_transition
    target_type: column
    evidence_refs:
    - ev.walmart.lifecycle.001
    notes: State transition uses this state column.
```

```yaml
candidate_edge:
  edge_id: edge.walmart.0865
  edge_type: PART_OF_PROCESS
  source: state_transition.walmart.settlement_sale_to_refund
  target: business_process.walmart.refund_to_payout_deduction
  fields:
    edge_family: business_process_flow
    evidence_basis: State transition is bound to this business process.
    confidence: high
    canonical_cognee_edge: true
    marketplace_only: true
    canonical_edge_type: PART_OF_PROCESS
    inverse_edge_type: HAS_STATE_TRANSITION
    materialize_inverse: false
    edge_class: canonical
    source_type: state_transition
    target_type: business_process
    evidence_refs:
    - ev.walmart.lifecycle.001
    notes: State transition is bound to this business process.
```

```yaml
candidate_edge:
  edge_id: edge.walmart.0866
  edge_type: CONSTRAINED_BY_RULE
  source: metric_implementation.walmart.walmart_settlement.gross_revenue
  target: rule.walmart.forward_revenue_filter
  fields:
    edge_family: rule_validation_constraint
    evidence_basis: Metric implementation constrained by source-backed rule.
    confidence: high
    canonical_cognee_edge: true
    marketplace_only: true
    canonical_edge_type: CONSTRAINED_BY_RULE
    inverse_edge_type: CONSTRAINS_CARD
    materialize_inverse: false
    edge_class: canonical
    source_type: metric_implementation
    target_type: rule
    evidence_refs:
    - ev.walmart.filters.001
    notes: Metric implementation constrained by source-backed rule.
```

```yaml
candidate_edge:
  edge_id: edge.walmart.0867
  edge_type: CONSTRAINED_BY_RULE
  source: metric_implementation.walmart.walmart_settlement.gross_revenue
  target: rule.walmart.wfs_fees_external
  fields:
    edge_family: rule_validation_constraint
    evidence_basis: Metric implementation constrained by source-backed rule.
    confidence: high
    canonical_cognee_edge: true
    marketplace_only: true
    canonical_edge_type: CONSTRAINED_BY_RULE
    inverse_edge_type: CONSTRAINS_CARD
    materialize_inverse: false
    edge_class: canonical
    source_type: metric_implementation
    target_type: rule
    evidence_refs:
    - ev.walmart.quality.001
    notes: Metric implementation constrained by source-backed rule.
```

```yaml
candidate_edge:
  edge_id: edge.walmart.0868
  edge_type: CONSTRAINED_BY_RULE
  source: metric_implementation.walmart.walmart_settlement.gross_revenue
  target: rule.walmart.no_external_bank_or_erp
  fields:
    edge_family: rule_validation_constraint
    evidence_basis: Metric implementation constrained by source-backed rule.
    confidence: high
    canonical_cognee_edge: true
    marketplace_only: true
    canonical_edge_type: CONSTRAINED_BY_RULE
    inverse_edge_type: CONSTRAINS_CARD
    materialize_inverse: false
    edge_class: canonical
    source_type: metric_implementation
    target_type: rule
    evidence_refs:
    - ev.walmart.business_model.001
    notes: Metric implementation constrained by source-backed rule.
```

```yaml
candidate_edge:
  edge_id: edge.walmart.0869
  edge_type: CONSTRAINED_BY_RULE
  source: metric_implementation.walmart.walmart_settlement.product_revenue_excluding_tax
  target: rule.walmart.wfs_fees_external
  fields:
    edge_family: rule_validation_constraint
    evidence_basis: Metric implementation constrained by source-backed rule.
    confidence: high
    canonical_cognee_edge: true
    marketplace_only: true
    canonical_edge_type: CONSTRAINED_BY_RULE
    inverse_edge_type: CONSTRAINS_CARD
    materialize_inverse: false
    edge_class: canonical
    source_type: metric_implementation
    target_type: rule
    evidence_refs:
    - ev.walmart.quality.001
    notes: Metric implementation constrained by source-backed rule.
```

```yaml
candidate_edge:
  edge_id: edge.walmart.0870
  edge_type: CONSTRAINED_BY_RULE
  source: metric_implementation.walmart.walmart_settlement.product_revenue_excluding_tax
  target: rule.walmart.no_external_bank_or_erp
  fields:
    edge_family: rule_validation_constraint
    evidence_basis: Metric implementation constrained by source-backed rule.
    confidence: high
    canonical_cognee_edge: true
    marketplace_only: true
    canonical_edge_type: CONSTRAINED_BY_RULE
    inverse_edge_type: CONSTRAINS_CARD
    materialize_inverse: false
    edge_class: canonical
    source_type: metric_implementation
    target_type: rule
    evidence_refs:
    - ev.walmart.business_model.001
    notes: Metric implementation constrained by source-backed rule.
```

```yaml
candidate_edge:
  edge_id: edge.walmart.0871
  edge_type: CONSTRAINED_BY_RULE
  source: metric_implementation.walmart.walmart_settlement.net_seller_payout
  target: rule.walmart.wfs_fees_external
  fields:
    edge_family: rule_validation_constraint
    evidence_basis: Metric implementation constrained by source-backed rule.
    confidence: high
    canonical_cognee_edge: true
    marketplace_only: true
    canonical_edge_type: CONSTRAINED_BY_RULE
    inverse_edge_type: CONSTRAINS_CARD
    materialize_inverse: false
    edge_class: canonical
    source_type: metric_implementation
    target_type: rule
    evidence_refs:
    - ev.walmart.quality.001
    notes: Metric implementation constrained by source-backed rule.
```

```yaml
candidate_edge:
  edge_id: edge.walmart.0872
  edge_type: CONSTRAINED_BY_RULE
  source: metric_implementation.walmart.walmart_settlement.net_seller_payout
  target: rule.walmart.no_external_bank_or_erp
  fields:
    edge_family: rule_validation_constraint
    evidence_basis: Metric implementation constrained by source-backed rule.
    confidence: high
    canonical_cognee_edge: true
    marketplace_only: true
    canonical_edge_type: CONSTRAINED_BY_RULE
    inverse_edge_type: CONSTRAINS_CARD
    materialize_inverse: false
    edge_class: canonical
    source_type: metric_implementation
    target_type: rule
    evidence_refs:
    - ev.walmart.business_model.001
    notes: Metric implementation constrained by source-backed rule.
```

```yaml
candidate_edge:
  edge_id: edge.walmart.0873
  edge_type: CONSTRAINED_BY_RULE
  source: metric_implementation.walmart.walmart_settlement.seller_realization_rate
  target: rule.walmart.wfs_fees_external
  fields:
    edge_family: rule_validation_constraint
    evidence_basis: Metric implementation constrained by source-backed rule.
    confidence: high
    canonical_cognee_edge: true
    marketplace_only: true
    canonical_edge_type: CONSTRAINED_BY_RULE
    inverse_edge_type: CONSTRAINS_CARD
    materialize_inverse: false
    edge_class: canonical
    source_type: metric_implementation
    target_type: rule
    evidence_refs:
    - ev.walmart.quality.001
    notes: Metric implementation constrained by source-backed rule.
```

```yaml
candidate_edge:
  edge_id: edge.walmart.0874
  edge_type: CONSTRAINED_BY_RULE
  source: metric_implementation.walmart.walmart_settlement.seller_realization_rate
  target: rule.walmart.no_external_bank_or_erp
  fields:
    edge_family: rule_validation_constraint
    evidence_basis: Metric implementation constrained by source-backed rule.
    confidence: high
    canonical_cognee_edge: true
    marketplace_only: true
    canonical_edge_type: CONSTRAINED_BY_RULE
    inverse_edge_type: CONSTRAINS_CARD
    materialize_inverse: false
    edge_class: canonical
    source_type: metric_implementation
    target_type: rule
    evidence_refs:
    - ev.walmart.business_model.001
    notes: Metric implementation constrained by source-backed rule.
```

```yaml
candidate_edge:
  edge_id: edge.walmart.0875
  edge_type: CONSTRAINED_BY_RULE
  source: metric_implementation.walmart.walmart_settlement.effective_commission_rate
  target: rule.walmart.compute_commission_rate
  fields:
    edge_family: rule_validation_constraint
    evidence_basis: Metric implementation constrained by source-backed rule.
    confidence: high
    canonical_cognee_edge: true
    marketplace_only: true
    canonical_edge_type: CONSTRAINED_BY_RULE
    inverse_edge_type: CONSTRAINS_CARD
    materialize_inverse: false
    edge_class: canonical
    source_type: metric_implementation
    target_type: rule
    evidence_refs:
    - ev.walmart.quality.001
    notes: Metric implementation constrained by source-backed rule.
```

```yaml
candidate_edge:
  edge_id: edge.walmart.0876
  edge_type: CONSTRAINED_BY_RULE
  source: metric_implementation.walmart.walmart_settlement.effective_commission_rate
  target: rule.walmart.wfs_fees_external
  fields:
    edge_family: rule_validation_constraint
    evidence_basis: Metric implementation constrained by source-backed rule.
    confidence: high
    canonical_cognee_edge: true
    marketplace_only: true
    canonical_edge_type: CONSTRAINED_BY_RULE
    inverse_edge_type: CONSTRAINS_CARD
    materialize_inverse: false
    edge_class: canonical
    source_type: metric_implementation
    target_type: rule
    evidence_refs:
    - ev.walmart.quality.001
    notes: Metric implementation constrained by source-backed rule.
```

```yaml
candidate_edge:
  edge_id: edge.walmart.0877
  edge_type: CONSTRAINED_BY_RULE
  source: metric_implementation.walmart.walmart_settlement.effective_commission_rate
  target: rule.walmart.no_external_bank_or_erp
  fields:
    edge_family: rule_validation_constraint
    evidence_basis: Metric implementation constrained by source-backed rule.
    confidence: high
    canonical_cognee_edge: true
    marketplace_only: true
    canonical_edge_type: CONSTRAINED_BY_RULE
    inverse_edge_type: CONSTRAINS_CARD
    materialize_inverse: false
    edge_class: canonical
    source_type: metric_implementation
    target_type: rule
    evidence_refs:
    - ev.walmart.business_model.001
    notes: Metric implementation constrained by source-backed rule.
```

```yaml
candidate_edge:
  edge_id: edge.walmart.0878
  edge_type: CONSTRAINED_BY_RULE
  source: metric_implementation.walmart.walmart_settlement.return_rate
  target: rule.walmart.reverse_refund_filter
  fields:
    edge_family: rule_validation_constraint
    evidence_basis: Metric implementation constrained by source-backed rule.
    confidence: high
    canonical_cognee_edge: true
    marketplace_only: true
    canonical_edge_type: CONSTRAINED_BY_RULE
    inverse_edge_type: CONSTRAINS_CARD
    materialize_inverse: false
    edge_class: canonical
    source_type: metric_implementation
    target_type: rule
    evidence_refs:
    - ev.walmart.filters.001
    notes: Metric implementation constrained by source-backed rule.
```

```yaml
candidate_edge:
  edge_id: edge.walmart.0879
  edge_type: CONSTRAINED_BY_RULE
  source: metric_implementation.walmart.walmart_settlement.return_rate
  target: rule.walmart.wfs_fees_external
  fields:
    edge_family: rule_validation_constraint
    evidence_basis: Metric implementation constrained by source-backed rule.
    confidence: high
    canonical_cognee_edge: true
    marketplace_only: true
    canonical_edge_type: CONSTRAINED_BY_RULE
    inverse_edge_type: CONSTRAINS_CARD
    materialize_inverse: false
    edge_class: canonical
    source_type: metric_implementation
    target_type: rule
    evidence_refs:
    - ev.walmart.quality.001
    notes: Metric implementation constrained by source-backed rule.
```

```yaml
candidate_edge:
  edge_id: edge.walmart.0880
  edge_type: CONSTRAINED_BY_RULE
  source: metric_implementation.walmart.walmart_settlement.return_rate
  target: rule.walmart.no_external_bank_or_erp
  fields:
    edge_family: rule_validation_constraint
    evidence_basis: Metric implementation constrained by source-backed rule.
    confidence: high
    canonical_cognee_edge: true
    marketplace_only: true
    canonical_edge_type: CONSTRAINED_BY_RULE
    inverse_edge_type: CONSTRAINS_CARD
    materialize_inverse: false
    edge_class: canonical
    source_type: metric_implementation
    target_type: rule
    evidence_refs:
    - ev.walmart.business_model.001
    notes: Metric implementation constrained by source-backed rule.
```

```yaml
candidate_edge:
  edge_id: edge.walmart.0881
  edge_type: CONSTRAINED_BY_RULE
  source: metric_implementation.walmart.walmart_oms.average_order_value
  target: rule.walmart.scope_filters
  fields:
    edge_family: rule_validation_constraint
    evidence_basis: Metric implementation constrained by source-backed rule.
    confidence: high
    canonical_cognee_edge: true
    marketplace_only: true
    canonical_edge_type: CONSTRAINED_BY_RULE
    inverse_edge_type: CONSTRAINS_CARD
    materialize_inverse: false
    edge_class: canonical
    source_type: metric_implementation
    target_type: rule
    evidence_refs:
    - ev.walmart.filters.001
    notes: Metric implementation constrained by source-backed rule.
```

```yaml
candidate_edge:
  edge_id: edge.walmart.0882
  edge_type: CONSTRAINED_BY_RULE
  source: metric_implementation.walmart.walmart_oms.average_order_value
  target: rule.walmart.oms_clean_rows
  fields:
    edge_family: rule_validation_constraint
    evidence_basis: Metric implementation constrained by source-backed rule.
    confidence: high
    canonical_cognee_edge: true
    marketplace_only: true
    canonical_edge_type: CONSTRAINED_BY_RULE
    inverse_edge_type: CONSTRAINS_CARD
    materialize_inverse: false
    edge_class: canonical
    source_type: metric_implementation
    target_type: rule
    evidence_refs:
    - ev.walmart_oms.quality.001
    notes: Metric implementation constrained by source-backed rule.
```

```yaml
candidate_edge:
  edge_id: edge.walmart.0883
  edge_type: CONSTRAINED_BY_RULE
  source: metric_implementation.walmart.walmart_oms.cancellation_rate
  target: rule.walmart.scope_filters
  fields:
    edge_family: rule_validation_constraint
    evidence_basis: Metric implementation constrained by source-backed rule.
    confidence: high
    canonical_cognee_edge: true
    marketplace_only: true
    canonical_edge_type: CONSTRAINED_BY_RULE
    inverse_edge_type: CONSTRAINS_CARD
    materialize_inverse: false
    edge_class: canonical
    source_type: metric_implementation
    target_type: rule
    evidence_refs:
    - ev.walmart.filters.001
    notes: Metric implementation constrained by source-backed rule.
```

```yaml
candidate_edge:
  edge_id: edge.walmart.0884
  edge_type: CONSTRAINED_BY_RULE
  source: metric_implementation.walmart.walmart_oms.cancellation_rate
  target: rule.walmart.oms_clean_rows
  fields:
    edge_family: rule_validation_constraint
    evidence_basis: Metric implementation constrained by source-backed rule.
    confidence: high
    canonical_cognee_edge: true
    marketplace_only: true
    canonical_edge_type: CONSTRAINED_BY_RULE
    inverse_edge_type: CONSTRAINS_CARD
    materialize_inverse: false
    edge_class: canonical
    source_type: metric_implementation
    target_type: rule
    evidence_refs:
    - ev.walmart_oms.quality.001
    notes: Metric implementation constrained by source-backed rule.
```

```yaml
candidate_edge:
  edge_id: edge.walmart.0885
  edge_type: CONSTRAINED_BY_RULE
  source: metric_implementation.walmart.walmart_settlement.tax_withheld
  target: rule.walmart.wfs_fees_external
  fields:
    edge_family: rule_validation_constraint
    evidence_basis: Metric implementation constrained by source-backed rule.
    confidence: high
    canonical_cognee_edge: true
    marketplace_only: true
    canonical_edge_type: CONSTRAINED_BY_RULE
    inverse_edge_type: CONSTRAINS_CARD
    materialize_inverse: false
    edge_class: canonical
    source_type: metric_implementation
    target_type: rule
    evidence_refs:
    - ev.walmart.quality.001
    notes: Metric implementation constrained by source-backed rule.
```

```yaml
candidate_edge:
  edge_id: edge.walmart.0886
  edge_type: CONSTRAINED_BY_RULE
  source: metric_implementation.walmart.walmart_settlement.tax_withheld
  target: rule.walmart.no_external_bank_or_erp
  fields:
    edge_family: rule_validation_constraint
    evidence_basis: Metric implementation constrained by source-backed rule.
    confidence: high
    canonical_cognee_edge: true
    marketplace_only: true
    canonical_edge_type: CONSTRAINED_BY_RULE
    inverse_edge_type: CONSTRAINS_CARD
    materialize_inverse: false
    edge_class: canonical
    source_type: metric_implementation
    target_type: rule
    evidence_refs:
    - ev.walmart.business_model.001
    notes: Metric implementation constrained by source-backed rule.
```

```yaml
candidate_edge:
  edge_id: edge.walmart.0887
  edge_type: CONSTRAINED_BY_RULE
  source: metric_implementation.walmart.walmart_settlement.walmart_funded_savings
  target: rule.walmart.wfs_fees_external
  fields:
    edge_family: rule_validation_constraint
    evidence_basis: Metric implementation constrained by source-backed rule.
    confidence: high
    canonical_cognee_edge: true
    marketplace_only: true
    canonical_edge_type: CONSTRAINED_BY_RULE
    inverse_edge_type: CONSTRAINS_CARD
    materialize_inverse: false
    edge_class: canonical
    source_type: metric_implementation
    target_type: rule
    evidence_refs:
    - ev.walmart.quality.001
    notes: Metric implementation constrained by source-backed rule.
```

```yaml
candidate_edge:
  edge_id: edge.walmart.0888
  edge_type: CONSTRAINED_BY_RULE
  source: metric_implementation.walmart.walmart_settlement.walmart_funded_savings
  target: rule.walmart.no_external_bank_or_erp
  fields:
    edge_family: rule_validation_constraint
    evidence_basis: Metric implementation constrained by source-backed rule.
    confidence: high
    canonical_cognee_edge: true
    marketplace_only: true
    canonical_edge_type: CONSTRAINED_BY_RULE
    inverse_edge_type: CONSTRAINS_CARD
    materialize_inverse: false
    edge_class: canonical
    source_type: metric_implementation
    target_type: rule
    evidence_refs:
    - ev.walmart.business_model.001
    notes: Metric implementation constrained by source-backed rule.
```

```yaml
candidate_edge:
  edge_id: edge.walmart.0889
  edge_type: CONSTRAINED_BY_RULE
  source: metric_implementation.walmart.walmart_settlement.sku_revenue
  target: rule.walmart.lookup_sku_not_null
  fields:
    edge_family: rule_validation_constraint
    evidence_basis: Metric implementation constrained by source-backed rule.
    confidence: high
    canonical_cognee_edge: true
    marketplace_only: true
    canonical_edge_type: CONSTRAINED_BY_RULE
    inverse_edge_type: CONSTRAINS_CARD
    materialize_inverse: false
    edge_class: canonical
    source_type: metric_implementation
    target_type: rule
    evidence_refs:
    - ev.walmart_lookup.schema.001
    notes: Metric implementation constrained by source-backed rule.
```

```yaml
candidate_edge:
  edge_id: edge.walmart.0890
  edge_type: CONSTRAINED_BY_RULE
  source: metric_implementation.walmart.walmart_settlement.sku_revenue
  target: rule.walmart.wfs_fees_external
  fields:
    edge_family: rule_validation_constraint
    evidence_basis: Metric implementation constrained by source-backed rule.
    confidence: high
    canonical_cognee_edge: true
    marketplace_only: true
    canonical_edge_type: CONSTRAINED_BY_RULE
    inverse_edge_type: CONSTRAINS_CARD
    materialize_inverse: false
    edge_class: canonical
    source_type: metric_implementation
    target_type: rule
    evidence_refs:
    - ev.walmart.quality.001
    notes: Metric implementation constrained by source-backed rule.
```

```yaml
candidate_edge:
  edge_id: edge.walmart.0891
  edge_type: CONSTRAINED_BY_RULE
  source: metric_implementation.walmart.walmart_settlement.sku_revenue
  target: rule.walmart.no_external_bank_or_erp
  fields:
    edge_family: rule_validation_constraint
    evidence_basis: Metric implementation constrained by source-backed rule.
    confidence: high
    canonical_cognee_edge: true
    marketplace_only: true
    canonical_edge_type: CONSTRAINED_BY_RULE
    inverse_edge_type: CONSTRAINS_CARD
    materialize_inverse: false
    edge_class: canonical
    source_type: metric_implementation
    target_type: rule
    evidence_refs:
    - ev.walmart.business_model.001
    notes: Metric implementation constrained by source-backed rule.
```

```yaml
candidate_edge:
  edge_id: edge.walmart.0892
  edge_type: CONSTRAINED_BY_RULE
  source: metric_implementation.walmart.walmart_oms.revenue_by_state
  target: rule.walmart.scope_filters
  fields:
    edge_family: rule_validation_constraint
    evidence_basis: Metric implementation constrained by source-backed rule.
    confidence: high
    canonical_cognee_edge: true
    marketplace_only: true
    canonical_edge_type: CONSTRAINED_BY_RULE
    inverse_edge_type: CONSTRAINS_CARD
    materialize_inverse: false
    edge_class: canonical
    source_type: metric_implementation
    target_type: rule
    evidence_refs:
    - ev.walmart.filters.001
    notes: Metric implementation constrained by source-backed rule.
```

```yaml
candidate_edge:
  edge_id: edge.walmart.0893
  edge_type: CONSTRAINED_BY_RULE
  source: metric_implementation.walmart.walmart_oms.revenue_by_state
  target: rule.walmart.oms_clean_rows
  fields:
    edge_family: rule_validation_constraint
    evidence_basis: Metric implementation constrained by source-backed rule.
    confidence: high
    canonical_cognee_edge: true
    marketplace_only: true
    canonical_edge_type: CONSTRAINED_BY_RULE
    inverse_edge_type: CONSTRAINS_CARD
    materialize_inverse: false
    edge_class: canonical
    source_type: metric_implementation
    target_type: rule
    evidence_refs:
    - ev.walmart_oms.quality.001
    notes: Metric implementation constrained by source-backed rule.
```

```yaml
candidate_edge:
  edge_id: edge.metric_dependency.walmart.seller_realization.net_seller_payout_numerator.parent_metric.metric.marketplace.seller_realization_rate
  edge_type: PARENT_METRIC
  source: metric_dependency.walmart.seller_realization.net_seller_payout_numerator
  target: metric.marketplace.seller_realization_rate
  fields:
    edge_family: metric_semantics
    evidence_basis: gold-standard metric dependency / execution constraint section
    confidence: high
    canonical_cognee_edge: true
    marketplace_only: true
    canonical_edge_type: PARENT_METRIC
    inverse_edge_type: HAS_METRIC_DEPENDENCY
    materialize_inverse: false
    edge_class: canonical
    source_type: metric_dependency
    target_type: metric
    evidence_refs:
    - ev.walmart.metrics.001
    - ev.walmart.business_model.001
```

```yaml
candidate_edge:
  edge_id: edge.metric_dependency.walmart.seller_realization.net_seller_payout_numerator.uses_dependent_metric.metric.marketplace.net_seller_payout
  edge_type: USES_DEPENDENT_METRIC
  source: metric_dependency.walmart.seller_realization.net_seller_payout_numerator
  target: metric.marketplace.net_seller_payout
  fields:
    edge_family: metric_semantics
    evidence_basis: gold-standard metric dependency / execution constraint section
    confidence: high
    canonical_cognee_edge: true
    marketplace_only: true
    canonical_edge_type: USES_DEPENDENT_METRIC
    inverse_edge_type: DEPENDENCY_USED_BY
    materialize_inverse: false
    edge_class: canonical
    source_type: metric_dependency
    target_type: metric
    evidence_refs:
    - ev.walmart.metrics.001
    - ev.walmart.business_model.001
```

```yaml
candidate_edge:
  edge_id: edge.metric_dependency.walmart.seller_realization.product_revenue_denominator.parent_metric.metric.marketplace.seller_realization_rate
  edge_type: PARENT_METRIC
  source: metric_dependency.walmart.seller_realization.product_revenue_denominator
  target: metric.marketplace.seller_realization_rate
  fields:
    edge_family: metric_semantics
    evidence_basis: gold-standard metric dependency / execution constraint section
    confidence: high
    canonical_cognee_edge: true
    marketplace_only: true
    canonical_edge_type: PARENT_METRIC
    inverse_edge_type: HAS_METRIC_DEPENDENCY
    materialize_inverse: false
    edge_class: canonical
    source_type: metric_dependency
    target_type: metric
    evidence_refs:
    - ev.walmart.metrics.001
```

```yaml
candidate_edge:
  edge_id: edge.metric_dependency.walmart.seller_realization.product_revenue_denominator.uses_dependent_metric.metric.marketplace.product_revenue_excluding_tax
  edge_type: USES_DEPENDENT_METRIC
  source: metric_dependency.walmart.seller_realization.product_revenue_denominator
  target: metric.marketplace.product_revenue_excluding_tax
  fields:
    edge_family: metric_semantics
    evidence_basis: gold-standard metric dependency / execution constraint section
    confidence: high
    canonical_cognee_edge: true
    marketplace_only: true
    canonical_edge_type: USES_DEPENDENT_METRIC
    inverse_edge_type: DEPENDENCY_USED_BY
    materialize_inverse: false
    edge_class: canonical
    source_type: metric_dependency
    target_type: metric
    evidence_refs:
    - ev.walmart.metrics.001
```

```yaml
candidate_edge:
  edge_id: edge.metric_dependency.walmart.net_seller_payout.product_revenue_component.parent_metric.metric.marketplace.net_seller_payout
  edge_type: PARENT_METRIC
  source: metric_dependency.walmart.net_seller_payout.product_revenue_component
  target: metric.marketplace.net_seller_payout
  fields:
    edge_family: metric_semantics
    evidence_basis: gold-standard metric dependency / execution constraint section
    confidence: high
    canonical_cognee_edge: true
    marketplace_only: true
    canonical_edge_type: PARENT_METRIC
    inverse_edge_type: HAS_METRIC_DEPENDENCY
    materialize_inverse: false
    edge_class: canonical
    source_type: metric_dependency
    target_type: metric
    evidence_refs:
    - ev.walmart.business_model.001
```

```yaml
candidate_edge:
  edge_id: edge.metric_dependency.walmart.net_seller_payout.product_revenue_component.uses_dependent_metric.metric.marketplace.product_revenue_excluding_tax
  edge_type: USES_DEPENDENT_METRIC
  source: metric_dependency.walmart.net_seller_payout.product_revenue_component
  target: metric.marketplace.product_revenue_excluding_tax
  fields:
    edge_family: metric_semantics
    evidence_basis: gold-standard metric dependency / execution constraint section
    confidence: high
    canonical_cognee_edge: true
    marketplace_only: true
    canonical_edge_type: USES_DEPENDENT_METRIC
    inverse_edge_type: DEPENDENCY_USED_BY
    materialize_inverse: false
    edge_class: canonical
    source_type: metric_dependency
    target_type: metric
    evidence_refs:
    - ev.walmart.business_model.001
```

```yaml
candidate_edge:
  edge_id: edge.metric_dependency.walmart.average_order_value.gross_revenue_component.parent_metric.metric.marketplace.average_order_value
  edge_type: PARENT_METRIC
  source: metric_dependency.walmart.average_order_value.gross_revenue_component
  target: metric.marketplace.average_order_value
  fields:
    edge_family: metric_semantics
    evidence_basis: gold-standard metric dependency / execution constraint section
    confidence: high
    canonical_cognee_edge: true
    marketplace_only: true
    canonical_edge_type: PARENT_METRIC
    inverse_edge_type: HAS_METRIC_DEPENDENCY
    materialize_inverse: false
    edge_class: canonical
    source_type: metric_dependency
    target_type: metric
    evidence_refs:
    - ev.walmart.metrics.001
```

```yaml
candidate_edge:
  edge_id: edge.metric_dependency.walmart.average_order_value.gross_revenue_component.uses_dependent_metric.metric.marketplace.gross_revenue
  edge_type: USES_DEPENDENT_METRIC
  source: metric_dependency.walmart.average_order_value.gross_revenue_component
  target: metric.marketplace.gross_revenue
  fields:
    edge_family: metric_semantics
    evidence_basis: gold-standard metric dependency / execution constraint section
    confidence: high
    canonical_cognee_edge: true
    marketplace_only: true
    canonical_edge_type: USES_DEPENDENT_METRIC
    inverse_edge_type: DEPENDENCY_USED_BY
    materialize_inverse: false
    edge_class: canonical
    source_type: metric_dependency
    target_type: metric
    evidence_refs:
    - ev.walmart.metrics.001
```

```yaml
candidate_edge:
  edge_id: edge.execution_constraint_set.walmart.query_scope_and_filters.includes_rule.rule.walmart.scope_filters
  edge_type: INCLUDES_RULE
  source: execution_constraint_set.walmart.query_scope_and_filters
  target: rule.walmart.scope_filters
  fields:
    edge_family: rule_validation_constraint
    evidence_basis: gold-standard metric dependency / execution constraint section
    confidence: high
    canonical_cognee_edge: true
    marketplace_only: true
    canonical_edge_type: INCLUDES_RULE
    inverse_edge_type: INCLUDED_IN_CONSTRAINT_SET
    materialize_inverse: false
    edge_class: canonical
    source_type: execution_constraint_set
    target_type: rule
    evidence_refs:
    - ev.walmart.filters.001
    - ev.walmart_lookup.schema.001
```

```yaml
candidate_edge:
  edge_id: edge.execution_constraint_set.walmart.query_scope_and_filters.includes_rule.rule.walmart.forward_revenue_filter
  edge_type: INCLUDES_RULE
  source: execution_constraint_set.walmart.query_scope_and_filters
  target: rule.walmart.forward_revenue_filter
  fields:
    edge_family: rule_validation_constraint
    evidence_basis: gold-standard metric dependency / execution constraint section
    confidence: high
    canonical_cognee_edge: true
    marketplace_only: true
    canonical_edge_type: INCLUDES_RULE
    inverse_edge_type: INCLUDED_IN_CONSTRAINT_SET
    materialize_inverse: false
    edge_class: canonical
    source_type: execution_constraint_set
    target_type: rule
    evidence_refs:
    - ev.walmart.filters.001
    - ev.walmart_lookup.schema.001
```

```yaml
candidate_edge:
  edge_id: edge.execution_constraint_set.walmart.query_scope_and_filters.includes_rule.rule.walmart.reverse_refund_filter
  edge_type: INCLUDES_RULE
  source: execution_constraint_set.walmart.query_scope_and_filters
  target: rule.walmart.reverse_refund_filter
  fields:
    edge_family: rule_validation_constraint
    evidence_basis: gold-standard metric dependency / execution constraint section
    confidence: high
    canonical_cognee_edge: true
    marketplace_only: true
    canonical_edge_type: INCLUDES_RULE
    inverse_edge_type: INCLUDED_IN_CONSTRAINT_SET
    materialize_inverse: false
    edge_class: canonical
    source_type: execution_constraint_set
    target_type: rule
    evidence_refs:
    - ev.walmart.filters.001
    - ev.walmart_lookup.schema.001
```

```yaml
candidate_edge:
  edge_id: edge.execution_constraint_set.walmart.query_scope_and_filters.includes_rule.rule.walmart.lookup_sku_not_null
  edge_type: INCLUDES_RULE
  source: execution_constraint_set.walmart.query_scope_and_filters
  target: rule.walmart.lookup_sku_not_null
  fields:
    edge_family: rule_validation_constraint
    evidence_basis: gold-standard metric dependency / execution constraint section
    confidence: high
    canonical_cognee_edge: true
    marketplace_only: true
    canonical_edge_type: INCLUDES_RULE
    inverse_edge_type: INCLUDED_IN_CONSTRAINT_SET
    materialize_inverse: false
    edge_class: canonical
    source_type: execution_constraint_set
    target_type: rule
    evidence_refs:
    - ev.walmart.filters.001
    - ev.walmart_lookup.schema.001
```

```yaml
candidate_edge:
  edge_id: edge.execution_constraint_set.walmart.query_scope_and_filters.includes_rule.rule.walmart.oms_clean_rows
  edge_type: INCLUDES_RULE
  source: execution_constraint_set.walmart.query_scope_and_filters
  target: rule.walmart.oms_clean_rows
  fields:
    edge_family: rule_validation_constraint
    evidence_basis: gold-standard metric dependency / execution constraint section
    confidence: high
    canonical_cognee_edge: true
    marketplace_only: true
    canonical_edge_type: INCLUDES_RULE
    inverse_edge_type: INCLUDED_IN_CONSTRAINT_SET
    materialize_inverse: false
    edge_class: canonical
    source_type: execution_constraint_set
    target_type: rule
    evidence_refs:
    - ev.walmart.filters.001
    - ev.walmart_lookup.schema.001
```

```yaml
candidate_edge:
  edge_id: edge.execution_constraint_set.walmart.query_scope_and_filters.applies_to_query_pattern.query_pattern.walmart.forward_gmv_net_payout
  edge_type: APPLIES_TO_QUERY_PATTERN
  source: execution_constraint_set.walmart.query_scope_and_filters
  target: query_pattern.walmart.forward_gmv_net_payout
  fields:
    edge_family: rule_validation_constraint
    evidence_basis: gold-standard metric dependency / execution constraint section
    confidence: high
    canonical_cognee_edge: true
    marketplace_only: true
    canonical_edge_type: APPLIES_TO_QUERY_PATTERN
    inverse_edge_type: HAS_EXECUTION_CONSTRAINT_SET
    materialize_inverse: false
    edge_class: canonical
    source_type: execution_constraint_set
    target_type: query_pattern
    evidence_refs:
    - ev.walmart.filters.001
    - ev.walmart_lookup.schema.001
```

```yaml
candidate_edge:
  edge_id: edge.execution_constraint_set.walmart.query_scope_and_filters.applies_to_query_pattern.query_pattern.walmart.return_rate
  edge_type: APPLIES_TO_QUERY_PATTERN
  source: execution_constraint_set.walmart.query_scope_and_filters
  target: query_pattern.walmart.return_rate
  fields:
    edge_family: rule_validation_constraint
    evidence_basis: gold-standard metric dependency / execution constraint section
    confidence: high
    canonical_cognee_edge: true
    marketplace_only: true
    canonical_edge_type: APPLIES_TO_QUERY_PATTERN
    inverse_edge_type: HAS_EXECUTION_CONSTRAINT_SET
    materialize_inverse: false
    edge_class: canonical
    source_type: execution_constraint_set
    target_type: query_pattern
    evidence_refs:
    - ev.walmart.filters.001
    - ev.walmart_lookup.schema.001
```

```yaml
candidate_edge:
  edge_id: edge.execution_constraint_set.walmart.query_scope_and_filters.applies_to_query_pattern.query_pattern.walmart.oms_aov
  edge_type: APPLIES_TO_QUERY_PATTERN
  source: execution_constraint_set.walmart.query_scope_and_filters
  target: query_pattern.walmart.oms_aov
  fields:
    edge_family: rule_validation_constraint
    evidence_basis: gold-standard metric dependency / execution constraint section
    confidence: high
    canonical_cognee_edge: true
    marketplace_only: true
    canonical_edge_type: APPLIES_TO_QUERY_PATTERN
    inverse_edge_type: HAS_EXECUTION_CONSTRAINT_SET
    materialize_inverse: false
    edge_class: canonical
    source_type: execution_constraint_set
    target_type: query_pattern
    evidence_refs:
    - ev.walmart.filters.001
    - ev.walmart_lookup.schema.001
```

```yaml
candidate_edge:
  edge_id: edge.execution_constraint_set.walmart.query_scope_and_filters.applies_to_query_pattern.query_pattern.walmart.cancellation_rate
  edge_type: APPLIES_TO_QUERY_PATTERN
  source: execution_constraint_set.walmart.query_scope_and_filters
  target: query_pattern.walmart.cancellation_rate
  fields:
    edge_family: rule_validation_constraint
    evidence_basis: gold-standard metric dependency / execution constraint section
    confidence: high
    canonical_cognee_edge: true
    marketplace_only: true
    canonical_edge_type: APPLIES_TO_QUERY_PATTERN
    inverse_edge_type: HAS_EXECUTION_CONSTRAINT_SET
    materialize_inverse: false
    edge_class: canonical
    source_type: execution_constraint_set
    target_type: query_pattern
    evidence_refs:
    - ev.walmart.filters.001
    - ev.walmart_lookup.schema.001
```

```yaml
candidate_edge:
  edge_id: edge.execution_constraint_set.walmart.query_scope_and_filters.applies_to_query_pattern.query_pattern.walmart.monthly_revenue
  edge_type: APPLIES_TO_QUERY_PATTERN
  source: execution_constraint_set.walmart.query_scope_and_filters
  target: query_pattern.walmart.monthly_revenue
  fields:
    edge_family: rule_validation_constraint
    evidence_basis: gold-standard metric dependency / execution constraint section
    confidence: high
    canonical_cognee_edge: true
    marketplace_only: true
    canonical_edge_type: APPLIES_TO_QUERY_PATTERN
    inverse_edge_type: HAS_EXECUTION_CONSTRAINT_SET
    materialize_inverse: false
    edge_class: canonical
    source_type: execution_constraint_set
    target_type: query_pattern
    evidence_refs:
    - ev.walmart.filters.001
    - ev.walmart_lookup.schema.001
```

```yaml
candidate_edge:
  edge_id: edge.execution_constraint_set.walmart.query_scope_and_filters.applies_to_query_pattern.query_pattern.walmart.top_skus
  edge_type: APPLIES_TO_QUERY_PATTERN
  source: execution_constraint_set.walmart.query_scope_and_filters
  target: query_pattern.walmart.top_skus
  fields:
    edge_family: rule_validation_constraint
    evidence_basis: gold-standard metric dependency / execution constraint section
    confidence: high
    canonical_cognee_edge: true
    marketplace_only: true
    canonical_edge_type: APPLIES_TO_QUERY_PATTERN
    inverse_edge_type: HAS_EXECUTION_CONSTRAINT_SET
    materialize_inverse: false
    edge_class: canonical
    source_type: execution_constraint_set
    target_type: query_pattern
    evidence_refs:
    - ev.walmart.filters.001
    - ev.walmart_lookup.schema.001
```

```yaml
candidate_edge:
  edge_id: edge.execution_constraint_set.walmart.query_scope_and_filters.applies_to_query_pattern.query_pattern.walmart.state_distribution
  edge_type: APPLIES_TO_QUERY_PATTERN
  source: execution_constraint_set.walmart.query_scope_and_filters
  target: query_pattern.walmart.state_distribution
  fields:
    edge_family: rule_validation_constraint
    evidence_basis: gold-standard metric dependency / execution constraint section
    confidence: high
    canonical_cognee_edge: true
    marketplace_only: true
    canonical_edge_type: APPLIES_TO_QUERY_PATTERN
    inverse_edge_type: HAS_EXECUTION_CONSTRAINT_SET
    materialize_inverse: false
    edge_class: canonical
    source_type: execution_constraint_set
    target_type: query_pattern
    evidence_refs:
    - ev.walmart.filters.001
    - ev.walmart_lookup.schema.001
```

```yaml
candidate_edge:
  edge_id: edge.execution_constraint_set.walmart.query_scope_and_filters.applies_to_query_pattern.query_pattern.walmart.payout_cycle
  edge_type: APPLIES_TO_QUERY_PATTERN
  source: execution_constraint_set.walmart.query_scope_and_filters
  target: query_pattern.walmart.payout_cycle
  fields:
    edge_family: rule_validation_constraint
    evidence_basis: gold-standard metric dependency / execution constraint section
    confidence: high
    canonical_cognee_edge: true
    marketplace_only: true
    canonical_edge_type: APPLIES_TO_QUERY_PATTERN
    inverse_edge_type: HAS_EXECUTION_CONSTRAINT_SET
    materialize_inverse: false
    edge_class: canonical
    source_type: execution_constraint_set
    target_type: query_pattern
    evidence_refs:
    - ev.walmart.filters.001
    - ev.walmart_lookup.schema.001
```

```yaml
candidate_edge:
  edge_id: edge.execution_constraint_set.walmart.query_scope_and_filters.applies_to_query_pattern.query_pattern.walmart.oms_settlement_reconciliation
  edge_type: APPLIES_TO_QUERY_PATTERN
  source: execution_constraint_set.walmart.query_scope_and_filters
  target: query_pattern.walmart.oms_settlement_reconciliation
  fields:
    edge_family: rule_validation_constraint
    evidence_basis: gold-standard metric dependency / execution constraint section
    confidence: high
    canonical_cognee_edge: true
    marketplace_only: true
    canonical_edge_type: APPLIES_TO_QUERY_PATTERN
    inverse_edge_type: HAS_EXECUTION_CONSTRAINT_SET
    materialize_inverse: false
    edge_class: canonical
    source_type: execution_constraint_set
    target_type: query_pattern
    evidence_refs:
    - ev.walmart.filters.001
    - ev.walmart_lookup.schema.001
```

```yaml
candidate_edge:
  edge_id: edge.execution_constraint_set.walmart.query_scope_and_filters.applies_to_query_pattern.query_pattern.walmart.commission_validation
  edge_type: APPLIES_TO_QUERY_PATTERN
  source: execution_constraint_set.walmart.query_scope_and_filters
  target: query_pattern.walmart.commission_validation
  fields:
    edge_family: rule_validation_constraint
    evidence_basis: gold-standard metric dependency / execution constraint section
    confidence: high
    canonical_cognee_edge: true
    marketplace_only: true
    canonical_edge_type: APPLIES_TO_QUERY_PATTERN
    inverse_edge_type: HAS_EXECUTION_CONSTRAINT_SET
    materialize_inverse: false
    edge_class: canonical
    source_type: execution_constraint_set
    target_type: query_pattern
    evidence_refs:
    - ev.walmart.filters.001
    - ev.walmart_lookup.schema.001
```

```yaml
candidate_edge:
  edge_id: edge.execution_constraint_set.walmart.query_scope_and_filters.applies_to_query_pattern.query_pattern.walmart.refund_sale_match
  edge_type: APPLIES_TO_QUERY_PATTERN
  source: execution_constraint_set.walmart.query_scope_and_filters
  target: query_pattern.walmart.refund_sale_match
  fields:
    edge_family: rule_validation_constraint
    evidence_basis: gold-standard metric dependency / execution constraint section
    confidence: high
    canonical_cognee_edge: true
    marketplace_only: true
    canonical_edge_type: APPLIES_TO_QUERY_PATTERN
    inverse_edge_type: HAS_EXECUTION_CONSTRAINT_SET
    materialize_inverse: false
    edge_class: canonical
    source_type: execution_constraint_set
    target_type: query_pattern
    evidence_refs:
    - ev.walmart.filters.001
    - ev.walmart_lookup.schema.001
```

```yaml
candidate_edge:
  edge_id: edge.execution_constraint_set.walmart.query_scope_and_filters.applies_to_query_pattern.query_pattern.walmart.full_three_table_view
  edge_type: APPLIES_TO_QUERY_PATTERN
  source: execution_constraint_set.walmart.query_scope_and_filters
  target: query_pattern.walmart.full_three_table_view
  fields:
    edge_family: rule_validation_constraint
    evidence_basis: gold-standard metric dependency / execution constraint section
    confidence: high
    canonical_cognee_edge: true
    marketplace_only: true
    canonical_edge_type: APPLIES_TO_QUERY_PATTERN
    inverse_edge_type: HAS_EXECUTION_CONSTRAINT_SET
    materialize_inverse: false
    edge_class: canonical
    source_type: execution_constraint_set
    target_type: query_pattern
    evidence_refs:
    - ev.walmart.filters.001
    - ev.walmart_lookup.schema.001
```

```yaml
candidate_edge:
  edge_id: edge.execution_constraint_set.walmart.query_scope_and_filters.applies_to_query_pattern.query_pattern.walmart.lookup_catalogue
  edge_type: APPLIES_TO_QUERY_PATTERN
  source: execution_constraint_set.walmart.query_scope_and_filters
  target: query_pattern.walmart.lookup_catalogue
  fields:
    edge_family: rule_validation_constraint
    evidence_basis: gold-standard metric dependency / execution constraint section
    confidence: high
    canonical_cognee_edge: true
    marketplace_only: true
    canonical_edge_type: APPLIES_TO_QUERY_PATTERN
    inverse_edge_type: HAS_EXECUTION_CONSTRAINT_SET
    materialize_inverse: false
    edge_class: canonical
    source_type: execution_constraint_set
    target_type: query_pattern
    evidence_refs:
    - ev.walmart.filters.001
    - ev.walmart_lookup.schema.001
```

```yaml
candidate_edge:
  edge_id: edge.execution_constraint_set.walmart.query_scope_and_filters.applies_to_query_pattern.query_pattern.walmart.mpf_tax_validation
  edge_type: APPLIES_TO_QUERY_PATTERN
  source: execution_constraint_set.walmart.query_scope_and_filters
  target: query_pattern.walmart.mpf_tax_validation
  fields:
    edge_family: rule_validation_constraint
    evidence_basis: gold-standard metric dependency / execution constraint section
    confidence: high
    canonical_cognee_edge: true
    marketplace_only: true
    canonical_edge_type: APPLIES_TO_QUERY_PATTERN
    inverse_edge_type: HAS_EXECUTION_CONSTRAINT_SET
    materialize_inverse: false
    edge_class: canonical
    source_type: execution_constraint_set
    target_type: query_pattern
    evidence_refs:
    - ev.walmart.filters.001
    - ev.walmart_lookup.schema.001
```

```yaml
candidate_edge:
  edge_id: edge.execution_constraint_set.walmart.query_scope_and_filters.applies_to_query_pattern.query_pattern.walmart.wfs_fee_visibility
  edge_type: APPLIES_TO_QUERY_PATTERN
  source: execution_constraint_set.walmart.query_scope_and_filters
  target: query_pattern.walmart.wfs_fee_visibility
  fields:
    edge_family: rule_validation_constraint
    evidence_basis: gold-standard metric dependency / execution constraint section
    confidence: high
    canonical_cognee_edge: true
    marketplace_only: true
    canonical_edge_type: APPLIES_TO_QUERY_PATTERN
    inverse_edge_type: HAS_EXECUTION_CONSTRAINT_SET
    materialize_inverse: false
    edge_class: canonical
    source_type: execution_constraint_set
    target_type: query_pattern
    evidence_refs:
    - ev.walmart.filters.001
    - ev.walmart_lookup.schema.001
```

```yaml
candidate_edge:
  edge_id: edge.execution_constraint_set.walmart.semantic_guardrails.includes_rule.rule.walmart.no_settled_amount_payout
  edge_type: INCLUDES_RULE
  source: execution_constraint_set.walmart.semantic_guardrails
  target: rule.walmart.no_settled_amount_payout
  fields:
    edge_family: rule_validation_constraint
    evidence_basis: gold-standard metric dependency / execution constraint section
    confidence: high
    canonical_cognee_edge: true
    marketplace_only: true
    canonical_edge_type: INCLUDES_RULE
    inverse_edge_type: INCLUDED_IN_CONSTRAINT_SET
    materialize_inverse: false
    edge_class: canonical
    source_type: execution_constraint_set
    target_type: rule
    evidence_refs:
    - ev.walmart.business_model.001
    - ev.walmart.quality.001
```

```yaml
candidate_edge:
  edge_id: edge.execution_constraint_set.walmart.semantic_guardrails.includes_rule.rule.walmart.mpf_tax_not_seller_revenue
  edge_type: INCLUDES_RULE
  source: execution_constraint_set.walmart.semantic_guardrails
  target: rule.walmart.mpf_tax_not_seller_revenue
  fields:
    edge_family: rule_validation_constraint
    evidence_basis: gold-standard metric dependency / execution constraint section
    confidence: high
    canonical_cognee_edge: true
    marketplace_only: true
    canonical_edge_type: INCLUDES_RULE
    inverse_edge_type: INCLUDED_IN_CONSTRAINT_SET
    materialize_inverse: false
    edge_class: canonical
    source_type: execution_constraint_set
    target_type: rule
    evidence_refs:
    - ev.walmart.business_model.001
    - ev.walmart.quality.001
```

```yaml
candidate_edge:
  edge_id: edge.execution_constraint_set.walmart.semantic_guardrails.includes_rule.rule.walmart.no_indian_tax_cards
  edge_type: INCLUDES_RULE
  source: execution_constraint_set.walmart.semantic_guardrails
  target: rule.walmart.no_indian_tax_cards
  fields:
    edge_family: rule_validation_constraint
    evidence_basis: gold-standard metric dependency / execution constraint section
    confidence: high
    canonical_cognee_edge: true
    marketplace_only: true
    canonical_edge_type: INCLUDES_RULE
    inverse_edge_type: INCLUDED_IN_CONSTRAINT_SET
    materialize_inverse: false
    edge_class: canonical
    source_type: execution_constraint_set
    target_type: rule
    evidence_refs:
    - ev.walmart.business_model.001
    - ev.walmart.quality.001
```

```yaml
candidate_edge:
  edge_id: edge.execution_constraint_set.walmart.semantic_guardrails.includes_rule.rule.walmart.no_process_variants_from_segments
  edge_type: INCLUDES_RULE
  source: execution_constraint_set.walmart.semantic_guardrails
  target: rule.walmart.no_process_variants_from_segments
  fields:
    edge_family: rule_validation_constraint
    evidence_basis: gold-standard metric dependency / execution constraint section
    confidence: high
    canonical_cognee_edge: true
    marketplace_only: true
    canonical_edge_type: INCLUDES_RULE
    inverse_edge_type: INCLUDED_IN_CONSTRAINT_SET
    materialize_inverse: false
    edge_class: canonical
    source_type: execution_constraint_set
    target_type: rule
    evidence_refs:
    - ev.walmart.business_model.001
    - ev.walmart.quality.001
```

```yaml
candidate_edge:
  edge_id: edge.execution_constraint_set.walmart.semantic_guardrails.includes_rule.rule.walmart.no_external_bank_or_erp
  edge_type: INCLUDES_RULE
  source: execution_constraint_set.walmart.semantic_guardrails
  target: rule.walmart.no_external_bank_or_erp
  fields:
    edge_family: rule_validation_constraint
    evidence_basis: gold-standard metric dependency / execution constraint section
    confidence: high
    canonical_cognee_edge: true
    marketplace_only: true
    canonical_edge_type: INCLUDES_RULE
    inverse_edge_type: INCLUDED_IN_CONSTRAINT_SET
    materialize_inverse: false
    edge_class: canonical
    source_type: execution_constraint_set
    target_type: rule
    evidence_refs:
    - ev.walmart.business_model.001
    - ev.walmart.quality.001
```

```yaml
candidate_edge:
  edge_id: edge.execution_constraint_set.walmart.semantic_guardrails.applies_to_query_pattern.query_pattern.walmart.forward_gmv_net_payout
  edge_type: APPLIES_TO_QUERY_PATTERN
  source: execution_constraint_set.walmart.semantic_guardrails
  target: query_pattern.walmart.forward_gmv_net_payout
  fields:
    edge_family: rule_validation_constraint
    evidence_basis: gold-standard metric dependency / execution constraint section
    confidence: high
    canonical_cognee_edge: true
    marketplace_only: true
    canonical_edge_type: APPLIES_TO_QUERY_PATTERN
    inverse_edge_type: HAS_EXECUTION_CONSTRAINT_SET
    materialize_inverse: false
    edge_class: canonical
    source_type: execution_constraint_set
    target_type: query_pattern
    evidence_refs:
    - ev.walmart.business_model.001
    - ev.walmart.quality.001
```

```yaml
candidate_edge:
  edge_id: edge.execution_constraint_set.walmart.semantic_guardrails.applies_to_query_pattern.query_pattern.walmart.return_rate
  edge_type: APPLIES_TO_QUERY_PATTERN
  source: execution_constraint_set.walmart.semantic_guardrails
  target: query_pattern.walmart.return_rate
  fields:
    edge_family: rule_validation_constraint
    evidence_basis: gold-standard metric dependency / execution constraint section
    confidence: high
    canonical_cognee_edge: true
    marketplace_only: true
    canonical_edge_type: APPLIES_TO_QUERY_PATTERN
    inverse_edge_type: HAS_EXECUTION_CONSTRAINT_SET
    materialize_inverse: false
    edge_class: canonical
    source_type: execution_constraint_set
    target_type: query_pattern
    evidence_refs:
    - ev.walmart.business_model.001
    - ev.walmart.quality.001
```

```yaml
candidate_edge:
  edge_id: edge.execution_constraint_set.walmart.semantic_guardrails.applies_to_query_pattern.query_pattern.walmart.oms_aov
  edge_type: APPLIES_TO_QUERY_PATTERN
  source: execution_constraint_set.walmart.semantic_guardrails
  target: query_pattern.walmart.oms_aov
  fields:
    edge_family: rule_validation_constraint
    evidence_basis: gold-standard metric dependency / execution constraint section
    confidence: high
    canonical_cognee_edge: true
    marketplace_only: true
    canonical_edge_type: APPLIES_TO_QUERY_PATTERN
    inverse_edge_type: HAS_EXECUTION_CONSTRAINT_SET
    materialize_inverse: false
    edge_class: canonical
    source_type: execution_constraint_set
    target_type: query_pattern
    evidence_refs:
    - ev.walmart.business_model.001
    - ev.walmart.quality.001
```

```yaml
candidate_edge:
  edge_id: edge.execution_constraint_set.walmart.semantic_guardrails.applies_to_query_pattern.query_pattern.walmart.cancellation_rate
  edge_type: APPLIES_TO_QUERY_PATTERN
  source: execution_constraint_set.walmart.semantic_guardrails
  target: query_pattern.walmart.cancellation_rate
  fields:
    edge_family: rule_validation_constraint
    evidence_basis: gold-standard metric dependency / execution constraint section
    confidence: high
    canonical_cognee_edge: true
    marketplace_only: true
    canonical_edge_type: APPLIES_TO_QUERY_PATTERN
    inverse_edge_type: HAS_EXECUTION_CONSTRAINT_SET
    materialize_inverse: false
    edge_class: canonical
    source_type: execution_constraint_set
    target_type: query_pattern
    evidence_refs:
    - ev.walmart.business_model.001
    - ev.walmart.quality.001
```

```yaml
candidate_edge:
  edge_id: edge.execution_constraint_set.walmart.semantic_guardrails.applies_to_query_pattern.query_pattern.walmart.monthly_revenue
  edge_type: APPLIES_TO_QUERY_PATTERN
  source: execution_constraint_set.walmart.semantic_guardrails
  target: query_pattern.walmart.monthly_revenue
  fields:
    edge_family: rule_validation_constraint
    evidence_basis: gold-standard metric dependency / execution constraint section
    confidence: high
    canonical_cognee_edge: true
    marketplace_only: true
    canonical_edge_type: APPLIES_TO_QUERY_PATTERN
    inverse_edge_type: HAS_EXECUTION_CONSTRAINT_SET
    materialize_inverse: false
    edge_class: canonical
    source_type: execution_constraint_set
    target_type: query_pattern
    evidence_refs:
    - ev.walmart.business_model.001
    - ev.walmart.quality.001
```

```yaml
candidate_edge:
  edge_id: edge.execution_constraint_set.walmart.semantic_guardrails.applies_to_query_pattern.query_pattern.walmart.top_skus
  edge_type: APPLIES_TO_QUERY_PATTERN
  source: execution_constraint_set.walmart.semantic_guardrails
  target: query_pattern.walmart.top_skus
  fields:
    edge_family: rule_validation_constraint
    evidence_basis: gold-standard metric dependency / execution constraint section
    confidence: high
    canonical_cognee_edge: true
    marketplace_only: true
    canonical_edge_type: APPLIES_TO_QUERY_PATTERN
    inverse_edge_type: HAS_EXECUTION_CONSTRAINT_SET
    materialize_inverse: false
    edge_class: canonical
    source_type: execution_constraint_set
    target_type: query_pattern
    evidence_refs:
    - ev.walmart.business_model.001
    - ev.walmart.quality.001
```

```yaml
candidate_edge:
  edge_id: edge.execution_constraint_set.walmart.semantic_guardrails.applies_to_query_pattern.query_pattern.walmart.state_distribution
  edge_type: APPLIES_TO_QUERY_PATTERN
  source: execution_constraint_set.walmart.semantic_guardrails
  target: query_pattern.walmart.state_distribution
  fields:
    edge_family: rule_validation_constraint
    evidence_basis: gold-standard metric dependency / execution constraint section
    confidence: high
    canonical_cognee_edge: true
    marketplace_only: true
    canonical_edge_type: APPLIES_TO_QUERY_PATTERN
    inverse_edge_type: HAS_EXECUTION_CONSTRAINT_SET
    materialize_inverse: false
    edge_class: canonical
    source_type: execution_constraint_set
    target_type: query_pattern
    evidence_refs:
    - ev.walmart.business_model.001
    - ev.walmart.quality.001
```

```yaml
candidate_edge:
  edge_id: edge.execution_constraint_set.walmart.semantic_guardrails.applies_to_query_pattern.query_pattern.walmart.payout_cycle
  edge_type: APPLIES_TO_QUERY_PATTERN
  source: execution_constraint_set.walmart.semantic_guardrails
  target: query_pattern.walmart.payout_cycle
  fields:
    edge_family: rule_validation_constraint
    evidence_basis: gold-standard metric dependency / execution constraint section
    confidence: high
    canonical_cognee_edge: true
    marketplace_only: true
    canonical_edge_type: APPLIES_TO_QUERY_PATTERN
    inverse_edge_type: HAS_EXECUTION_CONSTRAINT_SET
    materialize_inverse: false
    edge_class: canonical
    source_type: execution_constraint_set
    target_type: query_pattern
    evidence_refs:
    - ev.walmart.business_model.001
    - ev.walmart.quality.001
```

```yaml
candidate_edge:
  edge_id: edge.execution_constraint_set.walmart.semantic_guardrails.applies_to_query_pattern.query_pattern.walmart.oms_settlement_reconciliation
  edge_type: APPLIES_TO_QUERY_PATTERN
  source: execution_constraint_set.walmart.semantic_guardrails
  target: query_pattern.walmart.oms_settlement_reconciliation
  fields:
    edge_family: rule_validation_constraint
    evidence_basis: gold-standard metric dependency / execution constraint section
    confidence: high
    canonical_cognee_edge: true
    marketplace_only: true
    canonical_edge_type: APPLIES_TO_QUERY_PATTERN
    inverse_edge_type: HAS_EXECUTION_CONSTRAINT_SET
    materialize_inverse: false
    edge_class: canonical
    source_type: execution_constraint_set
    target_type: query_pattern
    evidence_refs:
    - ev.walmart.business_model.001
    - ev.walmart.quality.001
```

```yaml
candidate_edge:
  edge_id: edge.execution_constraint_set.walmart.semantic_guardrails.applies_to_query_pattern.query_pattern.walmart.commission_validation
  edge_type: APPLIES_TO_QUERY_PATTERN
  source: execution_constraint_set.walmart.semantic_guardrails
  target: query_pattern.walmart.commission_validation
  fields:
    edge_family: rule_validation_constraint
    evidence_basis: gold-standard metric dependency / execution constraint section
    confidence: high
    canonical_cognee_edge: true
    marketplace_only: true
    canonical_edge_type: APPLIES_TO_QUERY_PATTERN
    inverse_edge_type: HAS_EXECUTION_CONSTRAINT_SET
    materialize_inverse: false
    edge_class: canonical
    source_type: execution_constraint_set
    target_type: query_pattern
    evidence_refs:
    - ev.walmart.business_model.001
    - ev.walmart.quality.001
```

```yaml
candidate_edge:
  edge_id: edge.execution_constraint_set.walmart.semantic_guardrails.applies_to_query_pattern.query_pattern.walmart.refund_sale_match
  edge_type: APPLIES_TO_QUERY_PATTERN
  source: execution_constraint_set.walmart.semantic_guardrails
  target: query_pattern.walmart.refund_sale_match
  fields:
    edge_family: rule_validation_constraint
    evidence_basis: gold-standard metric dependency / execution constraint section
    confidence: high
    canonical_cognee_edge: true
    marketplace_only: true
    canonical_edge_type: APPLIES_TO_QUERY_PATTERN
    inverse_edge_type: HAS_EXECUTION_CONSTRAINT_SET
    materialize_inverse: false
    edge_class: canonical
    source_type: execution_constraint_set
    target_type: query_pattern
    evidence_refs:
    - ev.walmart.business_model.001
    - ev.walmart.quality.001
```

```yaml
candidate_edge:
  edge_id: edge.execution_constraint_set.walmart.semantic_guardrails.applies_to_query_pattern.query_pattern.walmart.full_three_table_view
  edge_type: APPLIES_TO_QUERY_PATTERN
  source: execution_constraint_set.walmart.semantic_guardrails
  target: query_pattern.walmart.full_three_table_view
  fields:
    edge_family: rule_validation_constraint
    evidence_basis: gold-standard metric dependency / execution constraint section
    confidence: high
    canonical_cognee_edge: true
    marketplace_only: true
    canonical_edge_type: APPLIES_TO_QUERY_PATTERN
    inverse_edge_type: HAS_EXECUTION_CONSTRAINT_SET
    materialize_inverse: false
    edge_class: canonical
    source_type: execution_constraint_set
    target_type: query_pattern
    evidence_refs:
    - ev.walmart.business_model.001
    - ev.walmart.quality.001
```

```yaml
candidate_edge:
  edge_id: edge.execution_constraint_set.walmart.semantic_guardrails.applies_to_query_pattern.query_pattern.walmart.lookup_catalogue
  edge_type: APPLIES_TO_QUERY_PATTERN
  source: execution_constraint_set.walmart.semantic_guardrails
  target: query_pattern.walmart.lookup_catalogue
  fields:
    edge_family: rule_validation_constraint
    evidence_basis: gold-standard metric dependency / execution constraint section
    confidence: high
    canonical_cognee_edge: true
    marketplace_only: true
    canonical_edge_type: APPLIES_TO_QUERY_PATTERN
    inverse_edge_type: HAS_EXECUTION_CONSTRAINT_SET
    materialize_inverse: false
    edge_class: canonical
    source_type: execution_constraint_set
    target_type: query_pattern
    evidence_refs:
    - ev.walmart.business_model.001
    - ev.walmart.quality.001
```

```yaml
candidate_edge:
  edge_id: edge.execution_constraint_set.walmart.semantic_guardrails.applies_to_query_pattern.query_pattern.walmart.mpf_tax_validation
  edge_type: APPLIES_TO_QUERY_PATTERN
  source: execution_constraint_set.walmart.semantic_guardrails
  target: query_pattern.walmart.mpf_tax_validation
  fields:
    edge_family: rule_validation_constraint
    evidence_basis: gold-standard metric dependency / execution constraint section
    confidence: high
    canonical_cognee_edge: true
    marketplace_only: true
    canonical_edge_type: APPLIES_TO_QUERY_PATTERN
    inverse_edge_type: HAS_EXECUTION_CONSTRAINT_SET
    materialize_inverse: false
    edge_class: canonical
    source_type: execution_constraint_set
    target_type: query_pattern
    evidence_refs:
    - ev.walmart.business_model.001
    - ev.walmart.quality.001
```

```yaml
candidate_edge:
  edge_id: edge.execution_constraint_set.walmart.semantic_guardrails.applies_to_query_pattern.query_pattern.walmart.wfs_fee_visibility
  edge_type: APPLIES_TO_QUERY_PATTERN
  source: execution_constraint_set.walmart.semantic_guardrails
  target: query_pattern.walmart.wfs_fee_visibility
  fields:
    edge_family: rule_validation_constraint
    evidence_basis: gold-standard metric dependency / execution constraint section
    confidence: high
    canonical_cognee_edge: true
    marketplace_only: true
    canonical_edge_type: APPLIES_TO_QUERY_PATTERN
    inverse_edge_type: HAS_EXECUTION_CONSTRAINT_SET
    materialize_inverse: false
    edge_class: canonical
    source_type: execution_constraint_set
    target_type: query_pattern
    evidence_refs:
    - ev.walmart.business_model.001
    - ev.walmart.quality.001
```

## 7. SQL Pattern Registry

```yaml
sql_pattern:
  sql_ref: sql.walmart.settlement.forward_gmv_net_payout
  description: Forward GMV, product revenue, tax, commission, savings, and net payout
  sql_template: SELECT SUM(charged_amount) AS gross_gmv, SUM(charged_amount_excluding_tax) AS product_revenue, SUM(total_tax)
    AS tax_withheld_by_walmart, SUM(gross_commission) AS total_commission, SUM(total_walmart_funded_savings) AS walmart_savings_credit,
    SUM(charged_amount_excluding_tax + gross_commission) AS net_seller_revenue, ROUND(100.0 * ABS(SUM(gross_commission)) /
    NULLIF(SUM(charged_amount_excluding_tax), 0), 2) AS commission_rate_pct FROM zs_observe.walmart_settlement WHERE is_active
    = true AND group_level_id = 22 AND transaction_type = 'forward';
  evidence_refs:
  - ev.walmart.metrics.001
```

```yaml
sql_pattern:
  sql_ref: sql.walmart.settlement.return_rate
  description: Return/refund rate from settlement transaction types
  sql_template: SELECT COUNT_IF(transaction_type = 'reverse') AS refunds, COUNT_IF(transaction_type = 'forward') AS sales,
    ROUND(100.0 * COUNT_IF(transaction_type = 'reverse') / NULLIF(COUNT_IF(transaction_type = 'forward'), 0), 2) AS refund_rate_pct
    FROM zs_observe.walmart_settlement WHERE is_active = true AND group_level_id = 22;
  evidence_refs:
  - ev.walmart.metrics.001
```

```yaml
sql_pattern:
  sql_ref: sql.walmart.oms.aov
  description: AOV from delivered OMS sales
  sql_template: SELECT AVG(charged_amount) AS aov_usd, MIN(charged_amount) AS min_price, MAX(charged_amount) AS max_price,
    COUNT(*) AS orders, SUM(charged_amount) AS total_gmv FROM zs_observe.walmart_oms WHERE is_active = true AND group_level_id
    = 22 AND order_status = 'DELIVERED' AND internal_txn_type = 'sales';
  evidence_refs:
  - ev.walmart.metrics.001
  - ev.walmart.filters.001
```

```yaml
sql_pattern:
  sql_ref: sql.walmart.oms.cancellation_rate
  description: Cancellation rate from OMS order_status
  sql_template: SELECT ROUND(100.0 * COUNT_IF(order_status = 'CANCELLED') / NULLIF(COUNT(*), 0), 2) AS cancel_rate_pct, COUNT_IF(order_status
    = 'CANCELLED') AS cancelled, COUNT_IF(order_status = 'DELIVERED') AS delivered FROM zs_observe.walmart_oms WHERE is_active
    = true AND group_level_id = 22;
  evidence_refs:
  - ev.walmart_oms.schema.001
```

```yaml
sql_pattern:
  sql_ref: sql.walmart.settlement.monthly_revenue
  description: Monthly revenue trend by settlement period end
  sql_template: SELECT DATE_TRUNC('month', CAST(metadata_2 AS DATE)) AS month, COUNT(*) AS transactions, SUM(charged_amount_excluding_tax)
    AS product_revenue, SUM(gross_commission) AS commission, SUM(charged_amount_excluding_tax + gross_commission) AS net_payout,
    SUM(total_walmart_funded_savings) AS walmart_savings FROM zs_observe.walmart_settlement WHERE is_active = true AND group_level_id
    = 22 AND transaction_type = 'forward' GROUP BY 1 ORDER BY 1;
  evidence_refs:
  - ev.walmart.metrics.001
```

```yaml
sql_pattern:
  sql_ref: sql.walmart.settlement.top_skus
  description: Top SKUs by settlement product revenue
  sql_template: SELECT s.sku_id, l.item_name, s.product_type, COUNT(*) AS orders, SUM(s.charged_amount_excluding_tax) AS revenue,
    AVG(s.charged_amount) AS avg_price, SUM(s.charged_amount_excluding_tax + s.gross_commission) AS net_payout FROM zs_observe.walmart_settlement
    s LEFT JOIN zs_observe.walmart_lookup l ON s.sku_id = l.sku AND l.is_active = true AND l.group_level_id = 22 AND l.sku
    IS NOT NULL WHERE s.is_active = true AND s.group_level_id = 22 AND s.transaction_type = 'forward' GROUP BY s.sku_id, l.item_name,
    s.product_type ORDER BY revenue DESC LIMIT 20;
  evidence_refs:
  - ev.walmart.metrics.001
  - ev.walmart_lookup.schema.001
```

```yaml
sql_pattern:
  sql_ref: sql.walmart.oms.state_distribution
  description: OMS delivered sales by destination state
  sql_template: SELECT destination_state, COUNT(*) AS orders, SUM(charged_amount) AS revenue_usd, ROUND(100.0 * COUNT(*) /
    SUM(COUNT(*)) OVER (), 2) AS pct_of_orders FROM zs_observe.walmart_oms WHERE is_active = true AND group_level_id = 22
    AND order_status = 'DELIVERED' AND LENGTH(destination_state) = 2 GROUP BY destination_state ORDER BY orders DESC LIMIT
    15;
  evidence_refs:
  - ev.walmart.metrics.001
  - ev.walmart.filters.001
```

```yaml
sql_pattern:
  sql_ref: sql.walmart.settlement.payout_cycle_summary
  description: Payout cycle summary using metadata_2 period end and metadata_3 payout date
  sql_template: SELECT CAST(metadata_3 AS DATE) AS payout_date, CAST(metadata_2 AS DATE) AS period_end, COUNT(*) AS line_items,
    COUNT(DISTINCT order_id) AS orders, SUM(CASE WHEN transaction_type='forward' THEN charged_amount_excluding_tax ELSE 0
    END) AS product_revenue, SUM(gross_commission) AS total_commission, SUM(total_walmart_funded_savings) AS wm_savings, SUM(charged_amount_excluding_tax
    + gross_commission) AS estimated_net_payout FROM zs_observe.walmart_settlement WHERE is_active = true AND group_level_id
    = 22 GROUP BY 1, 2 ORDER BY 1;
  evidence_refs:
  - ev.walmart.metrics.001
```

```yaml
sql_pattern:
  sql_ref: sql.walmart.reconciliation.oms_settlement
  description: OMS to settlement reconciliation
  sql_template: SELECT o.order_id, o.sku_id, o.charged_amount AS oms_price_usd, o.order_status, o.created_date AS order_date,
    s.charged_amount AS stl_total, s.charged_amount_excluding_tax AS stl_excl_tax, s.total_tax AS tax_withheld, s.gross_commission,
    s.marketplace_withheld_tax, ROUND(s.charged_amount_excluding_tax + s.gross_commission, 4) AS net_payout, ABS(o.charged_amount
    - s.charged_amount) AS price_variance, CASE WHEN s.order_id IS NULL THEN 'Not in Settlement' WHEN ABS(o.charged_amount
    - s.charged_amount) > 0.10 THEN 'Price Variance' ELSE 'Matched' END AS recon_status FROM zs_observe.walmart_oms o LEFT
    JOIN zs_observe.walmart_settlement s ON o.order_id = s.order_id AND s.is_active = true AND s.group_level_id = 22 AND s.transaction_type
    = 'forward' WHERE o.is_active = true AND o.group_level_id = 22 AND o.order_status = 'DELIVERED' AND o.internal_txn_type
    = 'sales';
  evidence_refs:
  - ev.walmart.reconciliation.001
```

```yaml
sql_pattern:
  sql_ref: sql.walmart.reconciliation.commission_validation
  description: Commission validation against source observed 13.46 percent baseline
  sql_template: SELECT order_id, sku_id, charged_amount_excluding_tax AS product_price, gross_commission AS commission_charged,
    ROUND(charged_amount_excluding_tax * -0.1346, 4) AS expected_commission, ABS(gross_commission - ROUND(charged_amount_excluding_tax
    * -0.1346, 4)) AS variance FROM zs_observe.walmart_settlement WHERE is_active = true AND group_level_id = 22 AND transaction_type
    = 'forward' AND ABS(gross_commission - ROUND(charged_amount_excluding_tax * -0.1346, 4)) > 0.50 ORDER BY variance DESC;
  evidence_refs:
  - ev.walmart.reconciliation.001
```

```yaml
sql_pattern:
  sql_ref: sql.walmart.reconciliation.refund_sale_match
  description: Refund rows matched back to original sale rows
  sql_template: SELECT r.order_id, r.sku_id, r.charged_amount AS refund_amount, r.gross_commission AS commission_reversed,
    s.charged_amount AS original_sale, s.gross_commission AS original_commission, ABS(r.charged_amount) - ABS(s.charged_amount)
    AS refund_variance FROM zs_observe.walmart_settlement r LEFT JOIN zs_observe.walmart_settlement s ON r.order_id = s.order_id
    AND s.transaction_type = 'forward' AND s.is_active = true AND s.group_level_id = 22 WHERE r.is_active = true AND r.group_level_id
    = 22 AND r.transaction_type = 'reverse';
  evidence_refs:
  - ev.walmart.reconciliation.001
```

```yaml
sql_pattern:
  sql_ref: sql.walmart.reconciliation.full_three_table_view
  description: Full three-table enriched OMS/settlement/lookup view
  sql_template: SELECT o.order_id, o.created_date AS order_date, o.order_status, o.destination_state, o.destination_city,
    l.item_name AS product_name, s.product_type, s.product_category, o.charged_amount AS oms_price, s.charged_amount_excluding_tax
    AS taxable_price, s.total_tax AS tax_withheld, s.gross_commission AS commission, ROUND(s.charged_amount_excluding_tax
    + s.gross_commission, 2) AS net_payout, CAST(s.metadata_3 AS DATE) AS payout_date FROM zs_observe.walmart_oms o LEFT JOIN
    zs_observe.walmart_settlement s ON o.order_id = s.order_id AND s.is_active = true AND s.group_level_id = 22 AND s.transaction_type
    = 'forward' LEFT JOIN zs_observe.walmart_lookup l ON o.sku_id = l.sku AND l.is_active = true AND l.group_level_id = 22
    AND l.sku IS NOT NULL WHERE o.is_active = true AND o.group_level_id = 22 AND o.order_status = 'DELIVERED' AND o.internal_txn_type
    = 'sales';
  evidence_refs:
  - ev.walmart.reconciliation.001
```

```yaml
sql_pattern:
  sql_ref: sql.walmart.lookup.catalogue
  description: Usable SKU catalogue rows
  sql_template: SELECT sku, sku_id, item_name, currency_type, group_level_id FROM zs_observe.walmart_lookup WHERE is_active
    = true AND group_level_id = 22 AND sku IS NOT NULL ORDER BY sku;
  evidence_refs:
  - ev.walmart_lookup.schema.001
```

```yaml
sql_pattern:
  sql_ref: sql.walmart.lookup.oms_product_enrichment
  description: OMS rows enriched with lookup product names
  sql_template: SELECT o.order_id, o.created_date, o.order_status, o.sku_id AS order_sku, l.item_name AS product_name, o.charged_amount,
    o.destination_state FROM zs_observe.walmart_oms o LEFT JOIN zs_observe.walmart_lookup l ON o.sku_id = l.sku AND l.is_active
    = true AND l.group_level_id = 22 AND l.sku IS NOT NULL WHERE o.is_active = true AND o.group_level_id = 22 AND o.order_status
    = 'DELIVERED';
  evidence_refs:
  - ev.walmart_lookup.schema.001
```

```yaml
sql_pattern:
  sql_ref: sql.walmart.lookup.settlement_product_enrichment
  description: Settlement rows enriched with lookup product names
  sql_template: SELECT s.sku_id, l.item_name, s.product_category, s.product_type, COUNT(*) AS orders, SUM(s.charged_amount_excluding_tax)
    AS revenue_usd FROM zs_observe.walmart_settlement s LEFT JOIN zs_observe.walmart_lookup l ON s.sku_id = l.sku AND l.is_active
    = true AND l.group_level_id = 22 AND l.sku IS NOT NULL WHERE s.is_active = true AND s.group_level_id = 22 AND s.transaction_type
    = 'forward' GROUP BY s.sku_id, l.item_name, s.product_category, s.product_type ORDER BY revenue_usd DESC;
  evidence_refs:
  - ev.walmart_lookup.schema.001
```

```yaml
sql_pattern:
  sql_ref: sql.walmart.validation.mpf_tax_identity
  description: MPF tax identity validation
  sql_template: SELECT COUNT(*) AS checked_rows, SUM(CASE WHEN ROUND(charged_amount, 2) = ROUND(charged_amount_excluding_tax
    + total_tax, 2) THEN 1 ELSE 0 END) AS matching_total_tax_identity, SUM(total_tax) AS total_tax, SUM(marketplace_withheld_tax)
    AS marketplace_withheld_tax FROM zs_observe.walmart_settlement WHERE is_active = true AND group_level_id = 22 AND transaction_type
    = 'forward';
  evidence_refs:
  - ev.walmart.business_model.001
  - ev.walmart.quality.001
```

```yaml
sql_pattern:
  sql_ref: sql.walmart.validation.wfs_fee_visibility
  description: WFS fee column visibility monitor
  sql_template: SELECT SUM(wfs_inventory_fee_reimbursement) AS wfs_inventory_fee_reimbursement, SUM(fee_reimbursement) AS
    fee_reimbursement, SUM(wfs_fee_reimbursement) AS wfs_fee_reimbursement, SUM(wfs_inbound_fee) AS wfs_inbound_fee, SUM(sem_marketing_fee)
    AS sem_marketing_fee FROM zs_observe.walmart_settlement WHERE is_active = true AND group_level_id = 22;
  evidence_refs:
  - ev.walmart.quality.001
```

```yaml
sql_pattern:
  sql_ref: sql.walmart.validation.lookup_sku_null_monitor
  description: Lookup sku-null content row monitor
  sql_template: SELECT COUNT(*) AS total_rows, COUNT_IF(sku IS NOT NULL) AS usable_sku_rows, COUNT_IF(sku IS NULL) AS content_attribute_rows
    FROM zs_observe.walmart_lookup WHERE is_active = true AND group_level_id = 22;
  evidence_refs:
  - ev.walmart_lookup.schema.001
```

```yaml
sql_pattern:
  sql_ref: sql.walmart.validation.oms_clean_rows_monitor
  description: OMS clean geographic and financial rows monitor
  sql_template: SELECT COUNT(*) AS rows, COUNT_IF(currency_type = 'USD') AS usd_rows, COUNT_IF(LENGTH(destination_state) =
    2) AS clean_state_rows, COUNT_IF(order_status IN ('DELIVERED','SHIPPED','CANCELLED','ACKNOWLEDGED')) AS valid_status_rows
    FROM zs_observe.walmart_oms WHERE is_active = true AND group_level_id = 22;
  evidence_refs:
  - ev.walmart_oms.quality.001
```

## 8. Review Item Registry

```yaml
review_item:
  review_id: review.walmart.group_scope_external
  review_type: scope_layer_required
  related_card_type: column
  related_canonical_id: column.zs_observe.walmart_settlement.group_level_id
  issue: DOCX documents group_level_id = 22, but runtime account/scope binding must not be created in marketplace canonical.
  required_resolution: Provide runtime scope from separate tenant/group/account-binding layer; keep group_level_id only as
    documented column/filter metadata here.
  severity: high
  evidence_refs:
  - ev.walmart.filters.001
  status: open
```

```yaml
review_item:
  review_id: review.walmart.wfs_fee_external_report
  review_type: external_source_required
  related_card_type: rule
  related_canonical_id: rule.walmart.wfs_fees_external
  issue: WFS storage, inbound, and removal fees are not present in walmart_settlement; current WFS columns are zero/not complete
    for full WFS cost analysis.
  required_resolution: Use Walmart seller portal WFS fee report before creating WFS storage/inbound/removal fee metric implementations.
  severity: medium
  evidence_refs:
  - ev.walmart.quality.001
  status: open
```

```yaml
review_item:
  review_id: review.walmart.bank_payout_reconciliation_external
  review_type: external_source_required
  related_card_type: metric
  related_canonical_id: metric.marketplace.net_seller_payout
  issue: DOCX provides payout date metadata but not the actual consolidated bank transfer table/amount.
  required_resolution: Do not reconcile to bank deposit unless a separate bank/payout source is supplied outside marketplace
    canonical.
  severity: medium
  evidence_refs:
  - ev.walmart.business_model.001
  status: open
```

## 9. Quality Gates for Deterministic Parser Output

```yaml
quality_gates:
  candidate_cards: 282
  candidate_edges: 941
  canonical_edges: 941
  source_evidence_count: 14
  source_tables: 3
  sql_patterns: 19
  missing_edge_references: 0
  missing_evidence_refs: 0
  dangling_sql_refs: 0
  open_reviews: 3
  lazy_workflow_steps: 0
  placeholder_metric_formulas: 0
  unsupported_metric_implementations: 0
  process_variant_cards: 0
  process_variants_review_required: 0
  hard_threshold_benchmarks_without_rule: 0
  forbidden_scope_cards_from_scope_ids: 0
  gold_standard_format_sections: pass
  candidate_edge_source_target_fields_format: pass
  business_process_cards_section: 4
  value_profile_cards_section: 11
  metric_dependency_cards_section: 4
  execution_constraint_set_cards_section: 2
  walmart_settled_amount_as_payout: blocked_by_rule.walmart.no_settled_amount_payout
  walmart_us_mpf_tax_boundary: pass
  group_level_scope_boundary: pass
```

## 10. Candidate Coverage Summary

```yaml
candidate_coverage_summary:
  candidate_card_type_counts:
    business_process: 4
    column: 125
    domain: 7
    execution_constraint_set: 2
    formula_template: 4
    matching_logic: 5
    metric: 12
    metric_dependency: 4
    metric_implementation: 12
    mismatch_category: 7
    output_contract: 7
    platform: 1
    platform_context: 1
    query_pattern: 15
    reconciliation_profile: 5
    reconciliation_side: 10
    reconciliation_unit: 5
    relationship: 4
    rule: 14
    state_transition: 4
    table: 3
    validation_test: 9
    value_profile: 11
    workflow_step: 11
  candidate_edge_type_counts:
    ANSWERS_WITH_METRIC: 15
    APPLIES_TO: 14
    APPLIES_TO_QUERY_PATTERN: 30
    CONSTRAINED_BY_RULE: 28
    ENFORCES_FORMULA: 4
    FROM_TABLE: 4
    HAS_COLUMN: 125
    HAS_CONTEXT: 27
    HAS_DOMAIN: 24
    HAS_MATCHING_LOGIC: 5
    HAS_MISMATCH_CATEGORY: 7
    HAS_SIDE: 10
    HAS_STATE_TRANSITION: 4
    HAS_TABLE: 6
    HAS_UNIT: 5
    HAS_VALUE_PROFILE: 11
    HAS_WORKFLOW_STEP: 11
    IMPLEMENTED_BY: 12
    IMPLEMENTS: 12
    INCLUDES_RULE: 10
    OUTPUT_FOR: 7
    PARENT_METRIC: 4
    PART_OF_PROCESS: 4
    PROFILES_COLUMN: 11
    RECONCILED_BY: 2
    TO_TABLE: 4
    USES: 11
    USES_COLUMN: 458
    USES_DEPENDENT_METRIC: 4
    USES_RELATIONSHIP: 3
    USES_STATE_COLUMN: 4
    USES_TABLE: 54
    VALIDATED_BY: 2
    VALIDATES: 9
```

## 11. Manifest Compliance Notes

- Evidence anchoring: every retained card points to explicit Walmart DOCX evidence refs.
- Card-type fit: WFS/category/geography/scope labels are value/profile/context semantics, not process variants.
- Gold-standard format: card families are separated into 5.x sections; business process, workflow, state transition, value profile, metric dependency, and execution constraint sections are explicit.
- Edge shape: all edges use `source`, `target`, and nested `fields`; legacy `source_id`/`target_id` shape has been removed.
- Metric executability: every metric implementation has an executable SQL ref; no `settled_amount` payout implementation is allowed.
- Scope discipline: `group_level_id = 22` is preserved only as documented scope metadata/filter guidance.
- Review discipline: only external runtime/account/bank/WFS-fee gaps remain open.
