# Flipkart Marketplace Clean Markdown — V8 Card-Ready Reference, Unified Edges

```yaml
document_metadata:
  document_id: flipkart_marketplace_clean_md_v9_refactored
  vendor: Flipkart
  source_docx: /mnt/data/Flipkart Recon Doc.docx
  frame_of_reference: marketplace_gold_standard_docx_to_clean_md_reference_v3
  generated_on: 2026-05-22
  scope: marketplace_specific_clean_markdown_for_deterministic_parser_with_unified_edges
  marketplace_only: true
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

## 0.1 Redraft Notes — V9 Manifest Refactor

This V9 refactor applies the consolidated marketplace cleanup manifests to the Flipkart canonical markdown. It removes lazy process variants for value segments, corrects source-backed schema/type issues, adds documented benchmarks and group-level scope values as canonical guidance, expands the DOCX-backed five-step reconciliation workflow, resolves placeholder SQL references, and preserves unresolved source gaps as review items rather than inventing semantics.

## 0. Parser Instructions

This document is intended to be parsed deterministically. It is not a prose-only summary. It uses the unified marketplace edge taxonomy: canonical edge types, legacy edge aliases, inverse edge metadata, and materialization rules are all explicit. Every `candidate_card`, `candidate_edge`, `review_item`, and SQL reference block is designed to be machine-readable while preserving the marketplace-only boundary.

Critical parser rules:

- Create only Flipkart marketplace semantic cards from this document.
- Do not create tenant, group, platform account, account binding, business scope, business flow, external logistics, bank, payment gateway, ERP/accounting, or statutory filing cards.
- Treat scope-like fields such as `group_level_id` and `group_id` only as columns/caveats; documented scope values may be stored on canonical column/value-profile cards but must not create tenant/group/account-binding cards.
- Treat marketplace fulfilment, shipping, TCS/TDS, GST, NEFT, and payout fields as marketplace semantics only.
- Do not maximize card count. Emit cards only where evidence, caveat, or review state is explicit.
- Normalize all legacy edge aliases into canonical uppercase edge types before graph ingestion.
- Materialize inverse edges only when `materialize_inverse: true`; otherwise use reverse graph indexes.

## 1. Source Intake and Evidence Registry

```yaml
source_evidence:
  id: evidence.flipkart.overview
  source_section: Overview / Flipkart MP Tables
  summary: Flipkart marketplace data is modeled around OMS, settlement, commission, and cashback tables; all analytical and reconciliation guidance in this document is limited to marketplace-owned semantics.
  confidence: high
```

```yaml
source_evidence:
  id: evidence.flipkart.settlement
  source_section: flipkart_settlement section
  summary: Settlement represents marketplace payout, fee, tax deduction, offer, reverse, fulfilment, and seller-tier semantics. Key table is zs_observe.flipkart_settlement; source SQL also references zs_refined.flipkart_settlement.
  confidence: high
```

```yaml
source_evidence:
  id: evidence.flipkart.commission
  source_section: flipkart_commission section
  summary: Commission table provides detailed fee invoice lines with order_id lacking OD prefix, fee classification by description/fee_name, charged_amount and total_tax as the core decimal amount fields, and many rows per order item.
  confidence: high
```

```yaml
source_evidence:
  id: evidence.flipkart.cashback
  source_section: flipkart_cashback section
  summary: Cashback table records credit/debit notes, promotional subsidies, document type/subtype, forward/reverse/cancel transaction types, and signed charged_amount semantics.
  confidence: high
```

```yaml
source_evidence:
  id: evidence.flipkart.oms
  source_section: flipkart_oms section and relationship/query references
  summary: OMS is referenced as the marketplace order source, but the source section repeats cashback-like content. Treat OMS schema as partial and review-required.
  confidence: high
```

```yaml
source_evidence:
  id: evidence.flipkart.relationships
  source_section: Key joins / Query examples
  summary: Commission order_id excludes OD prefix and must be normalized before joining to settlement, OMS, or cashback. Many-side fee/cashback tables should be pre-aggregated before joining.
  confidence: high
```

```yaml
source_evidence:
  id: evidence.flipkart.query_patterns
  source_section: Query examples / reconciliation examples
  summary: Source examples cover realization rate, settlement by fulfilment type, settlement cycle, fee breakdown, fee pivot, settlement-vs-commission reconciliation, cashback analysis, and Shopsy comparison.
  confidence: high
```

```yaml
source_evidence:
  id: evidence.flipkart.shopsy
  source_section: Shopsy and cashback notes
  summary: Shopsy is indicated through string column is_shopsy_order_ with values such as true/false; treat it as a value-platform flag, not a separate non-marketplace domain.
  confidence: high
```

```yaml
source_evidence:
  id: evidence.flipkart.fulfilment
  source_section: Fulfilment naming notes
  summary: OMS uses FBF/NON_FBF, while settlement uses flipkart_fulfilment/seller_easy_ship; these are marketplace fulfilment semantics.
  confidence: high
```

```yaml
source_evidence:
  id: evidence.flipkart.scope_caveats
  source_section: Known caveats
  summary: group_level_id values differ by table and must be treated as table columns/caveats only, not as account-binding or business hierarchy cards.
  confidence: high
```

```yaml
source_evidence:
  id: evidence.flipkart.fee_structure
  source_section: Seller Fee Structure (Nov 2025 Revision)
  summary: DOCX documents commission ranges, zero commission below ₹1,000, Shopsy zero commission, fixed fee slabs, shipping fee basis, collection
    fee rates, and fee summary formula.
  confidence: high
```

```yaml
source_evidence:
  id: evidence.flipkart.seller_tier
  source_section: Seller Tier System
  summary: DOCX documents seller tiers, payout cycle, fixed fee level, and qualification metrics; no reliable schema column is provided for seller
    tier binding.
  confidence: high
```

```yaml
source_evidence:
  id: evidence.flipkart.payment_process
  source_section: Settlement / Payment Process
  summary: DOCX states payout cycle begins from dispatch date, lasts 7 to 15 days depending on seller tier, and settlement reports show order-wise
    fee/tax/refund/net details.
  confidence: high
```

```yaml
source_evidence:
  id: evidence.flipkart.metrics_benchmarks
  source_section: Key Metrics for Seller Analytics
  summary: DOCX defines GMV, Net Revenue, AOV, Realization Rate, Effective Fee Rate, Return Rate, Cancellation Rate, Cashback Rate, and benchmark/guidance
    values for realization and category return rates.
  confidence: high
```

```yaml
source_evidence:
  id: evidence.flipkart.reconciliation_framework
  source_section: Reconciliation Framework (ZenStatement Context)
  summary: 'DOCX defines a five-step reconciliation framework: order verification, fee validation, cashback reconciliation, settlement verification,
    and cross-table discrepancy detection.'
  confidence: high
```

```yaml
source_evidence:
  id: evidence.flipkart.pipeline_architecture
  source_section: Data Pipeline Architecture (ZenStatement)
  summary: DOCX shows flipkart_oms in zs_recon_processor, commission/cashback in zs_observe, and settlement in zs_refined/final enriched processing
    stage.
  confidence: high
```

```yaml
source_evidence:
  id: evidence.flipkart.pitfalls
  source_section: Common Pitfalls & Gotchas
  summary: DOCX documents OD-prefix mismatch, group_level_id differences by table, Shopsy string flag, fulfilment naming mismatch, granular settlement
    fee nulls, string-vs-decimal traps, low OMS active rate, and TCS/TDS cash-flow treatment.
  confidence: high
```

```yaml
source_evidence:
  id: evidence.flipkart.settlement_logic
  source_section: 'Table: flipkart_settlement > Purpose, Critical Filters, Core Settlement Logic, Columns, Relationships'
  summary: DOCX defines settlement as cash-flow ground truth, group_level_id 66388, settlement waterfall components, fee/tax deduction signs,
    vendor_payout as string, fulfilment mapping, and settlement-to-commission reconciliation.
  confidence: high
```

```yaml
source_evidence:
  id: evidence.flipkart.commission_schema
  source_section: 'Table: flipkart_commission > Purpose, Order ID Format, Transaction Types & Fee Names, Financial Columns'
  summary: DOCX defines commission as fee invoice detail, order_id without OD prefix, transaction_type Order Item, metadata commission invoice,
    description/fee_name fee classes, charged_amount and total_tax as authoritative decimals, and string legacy fee fields.
  confidence: high
```

```yaml
source_evidence:
  id: evidence.flipkart.cashback_schema
  source_section: 'Table: flipkart_cashback > Purpose, Transaction Types & Document Types, Financial Columns, Date Columns'
  summary: DOCX defines cashback credit/debit notes, signed charged_amount, forward/reverse/forward-cancel semantics, nullable document classifications,
    created_date timestamp as primary date filter, and invoice_date string.
  confidence: high
```


## 2. Out-of-Scope Registry

```yaml
out_of_scope_item:
  id: oos.flipkart.tenant_group
  topic: Tenant, group, platform account, account data binding, business scope, and business flow cards
  instruction: Do not create these card types from this marketplace document. Scope values such as group_level_id remain table columns only.
  allowed_as: column/filter caveat only
```

```yaml
out_of_scope_item:
  id: oos.flipkart.bank
  topic: Banking and settlement-to-bank credit reconciliation
  instruction: Do not create bank account, bank ledger, UTR-to-bank-credit, or marketplace payout-to-bank reconciliation cards.
  allowed_as: settlement_id/neft_type/vendor_payout as marketplace settlement columns only
```

```yaml
out_of_scope_item:
  id: oos.flipkart.logistics
  topic: External logistics or courier lifecycle
  instruction: Do not create courier, AWB lifecycle, carrier NDR, external delivery, or logistics COD remittance cards.
  allowed_as: fulfilment_type, shipping_fee, reverse_shipping_fee, zone, weight as marketplace fee columns only
```

```yaml
out_of_scope_item:
  id: oos.flipkart.payment_gateway
  topic: Payment gateway reconciliation
  instruction: Do not create PG transaction, PG settlement, or PG-to-bank cards.
  allowed_as: collection_fee as marketplace fee column only
```

```yaml
out_of_scope_item:
  id: oos.flipkart.erp_accounting
  topic: ERP/accounting/GL mappings
  instruction: Do not create journal entry, ledger posting, revenue recognition, or accounting-close cards.
  allowed_as: marketplace deductions and taxes as marketplace metrics only
```

```yaml
out_of_scope_item:
  id: oos.flipkart.tax_compliance
  topic: Statutory tax filing and GST/TDS/TCS return compliance
  instruction: Do not create statutory filing cards or tax liability computation cards.
  allowed_as: TCS/TDS/GST columns and marketplace deduction metrics only
```

```yaml
out_of_scope_item:
  id: oos.flipkart.connector_pipeline
  topic: Connector/pipeline runtime operations
  instruction: Do not create ingestion schedule, retry, SLA, dbt/Airflow, or infrastructure validation cards.
  allowed_as: semantic data-quality validation only
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
| `metric` | `canonical_name`, `colloquial_names`, `metric_family`, `business_question`, `default_grain`, `default_time_basis`, `positive_direction`, `included_components`, `excluded_components`, `evidence_refs`, `confidence`, `review_status`, `notes` |
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

Primary marketplace-owned source tables in scope are `zs_recon_processor.flipkart_oms`, `zs_observe.flipkart_settlement`, `zs_observe.flipkart_commission`, and `zs_observe.flipkart_cashback`. The settlement source also appears in example SQL as `zs_refined.flipkart_settlement`; treat that as an alias/review caveat unless the deployment explicitly uses it.

## 5. Candidate Cards

### 5.1 Platform Cards

```yaml
candidate_card:
  card_type: platform
  card_id: platform.flipkart
  name: Flipkart
  fields:
    aliases: 
      - Flipkart Marketplace
      - Flipkart India
      - FK
    regions: 
      - IN
    marketplace_model: Indian e-commerce marketplace
    supported_contexts: 
      - platform_context.flipkart.in
    source_platform_codes: 
      - flipkart
    excluded_topics: 
      - tenant/group/account binding
      - external logistics
      - bank reconciliation
    evidence_refs: 
      - evidence.flipkart.overview
    confidence: high
    review_status: accepted
```

### 5.2 Platform Context Cards

```yaml
candidate_card:
  card_type: platform_context
  card_id: platform_context.flipkart.in
  name: Flipkart India marketplace context
  fields:
    platform_id: platform.flipkart
    country: India
    currency: INR
    timezone: Asia/Kolkata
    fulfilment_models: 
      - FBF
      - NON_FBF
      - flipkart_fulfilment
      - seller_easy_ship
    sub_platforms: 
      - Shopsy flag via is_shopsy_order_
    source_caveats: 
      - FBF/NON_FBF naming differs from settlement naming; normalize semantically.
      - Shopsy flag is string-valued in source examples.
    evidence_refs: 
      - evidence.flipkart.fulfilment
      - evidence.flipkart.shopsy
    confidence: high
    review_status: accepted
```

### 5.3 Domain Cards

```yaml
candidate_card:
  card_type: domain
  card_id: domain.marketplace.flipkart.orders
  name: Flipkart marketplace orders
  fields:
    parent_domain: marketplace
    marketplace_module: orders
    description: Order/OMS semantics, order item identifiers, order value, forward/reverse/cancel signals.
    included_tables: 
      - table.flipkart.oms
      - table.flipkart.settlement
      - table.flipkart.commission
      - table.flipkart.cashback
    excluded_topics: 
      - tenant/account scoping
      - bank reconciliation
      - external logistics
      - ERP/accounting
    evidence_refs: 
      - evidence.flipkart.overview
    confidence: high
    review_status: accepted
```

```yaml
candidate_card:
  card_type: domain
  card_id: domain.marketplace.flipkart.settlement
  name: Flipkart marketplace settlement
  fields:
    parent_domain: marketplace
    marketplace_module: settlement
    description: Marketplace payout, settlement amount, sale/refund/offer components, settlement cycle, fulfilment and NEFT fields.
    included_tables: 
      - table.flipkart.oms
      - table.flipkart.settlement
      - table.flipkart.commission
      - table.flipkart.cashback
    excluded_topics: 
      - tenant/account scoping
      - bank reconciliation
      - external logistics
      - ERP/accounting
    evidence_refs: 
      - evidence.flipkart.overview
    confidence: high
    review_status: accepted
```

```yaml
candidate_card:
  card_type: domain
  card_id: domain.marketplace.flipkart.fees
  name: Flipkart marketplace fees and commission
  fields:
    parent_domain: marketplace
    marketplace_module: fees and commission
    description: Commission, fixed, shipping, reverse shipping, collection, franchise, pick-and-pack, GST on fees, rebates.
    included_tables: 
      - table.flipkart.oms
      - table.flipkart.settlement
      - table.flipkart.commission
      - table.flipkart.cashback
    excluded_topics: 
      - tenant/account scoping
      - bank reconciliation
      - external logistics
      - ERP/accounting
    evidence_refs: 
      - evidence.flipkart.overview
    confidence: high
    review_status: accepted
```

```yaml
candidate_card:
  card_type: domain
  card_id: domain.marketplace.flipkart.cashback
  name: Flipkart cashback, promotions, and credit/debit notes
  fields:
    parent_domain: marketplace
    marketplace_module: flipkart cashback, promotions, and credit/debit notes
    description: Promotional subsidy, cashback amount, credit/debit document handling, Shopsy cashback analysis.
    included_tables: 
      - table.flipkart.oms
      - table.flipkart.settlement
      - table.flipkart.commission
      - table.flipkart.cashback
    excluded_topics: 
      - tenant/account scoping
      - bank reconciliation
      - external logistics
      - ERP/accounting
    evidence_refs: 
      - evidence.flipkart.overview
    confidence: high
    review_status: accepted
```

```yaml
candidate_card:
  card_type: domain
  card_id: domain.marketplace.flipkart.returns
  name: Flipkart returns and cancellations
  fields:
    parent_domain: marketplace
    marketplace_module: flipkart returns and cancellations
    description: Reverse and cancel marketplace semantics, return_type, negative/reversal treatment.
    included_tables: 
      - table.flipkart.oms
      - table.flipkart.settlement
      - table.flipkart.commission
      - table.flipkart.cashback
    excluded_topics: 
      - tenant/account scoping
      - bank reconciliation
      - external logistics
      - ERP/accounting
    evidence_refs: 
      - evidence.flipkart.overview
    confidence: high
    review_status: accepted
```

```yaml
candidate_card:
  card_type: domain
  card_id: domain.marketplace.flipkart.fulfilment
  name: Flipkart marketplace fulfilment fee semantics
  fields:
    parent_domain: marketplace
    marketplace_module: fulfilment fee semantics
    description: FBF/NON_FBF and settlement fulfilment type effects on fee and payout behavior; no external logistics cards.
    included_tables: 
      - table.flipkart.oms
      - table.flipkart.settlement
      - table.flipkart.commission
      - table.flipkart.cashback
    excluded_topics: 
      - tenant/account scoping
      - bank reconciliation
      - external logistics
      - ERP/accounting
    evidence_refs: 
      - evidence.flipkart.overview
    confidence: high
    review_status: accepted
```

```yaml
candidate_card:
  card_type: domain
  card_id: domain.marketplace.flipkart.reconciliation
  name: Flipkart marketplace-internal reconciliation
  fields:
    parent_domain: marketplace
    marketplace_module: flipkart marketplace-internal reconciliation
    description: OMS↔settlement, settlement↔commission, settlement↔cashback/offer, settlement waterfall checks.
    included_tables: 
      - table.flipkart.oms
      - table.flipkart.settlement
      - table.flipkart.commission
      - table.flipkart.cashback
    excluded_topics: 
      - tenant/account scoping
      - bank reconciliation
      - external logistics
      - ERP/accounting
    evidence_refs: 
      - evidence.flipkart.overview
    confidence: high
    review_status: accepted
```

```yaml
candidate_card:
  card_type: domain
  card_id: domain.marketplace.flipkart.tax_deductions
  name: Flipkart marketplace tax deduction fields
  fields:
    parent_domain: marketplace
    marketplace_module: tax deduction fields
    description: TCS/TDS/GST-on-fees as marketplace settlement/fee deductions, not statutory filing.
    included_tables: 
      - table.flipkart.oms
      - table.flipkart.settlement
      - table.flipkart.commission
      - table.flipkart.cashback
    excluded_topics: 
      - tenant/account scoping
      - bank reconciliation
      - external logistics
      - ERP/accounting
    evidence_refs: 
      - evidence.flipkart.overview
    confidence: high
    review_status: accepted
```

### 5.4 Table Cards

```yaml
candidate_card:
  card_type: table
  card_id: table.flipkart.oms
  name: zs_recon_processor.flipkart_oms
  fields:
    schema_name: zs_recon_processor
    table_name: flipkart_oms
    marketplace_module: orders
    grain: order item / transaction row; schema review required because DOCX table body repeats cashback semantics
    primary_keys:
    - order_id
    - item_id
    business_keys:
    - order_id
    - item_id
    date_columns:
    - created_date
    amount_columns:
    - charged_amount
    status_columns:
    - transaction_type
    - fulfilment_type
    - is_shopsy_order_
    - is_active
    scope_columns_as_columns_only:
    - group_level_id
    known_filters:
    - is_active = true
    - group_level_id values vary by OMS deployment; do not cross-table match group_level_id
    source_caveats:
    - DOCX reconciliation framework uses flipkart_oms for order verification, but the detailed table section labelled flipkart_oms repeats cashback-like
      descriptions.
    - Use OMS cards only where query examples or reconciliation framework explicitly support order semantics.
    evidence_refs:
    - evidence.flipkart.oms
    - evidence.flipkart.reconciliation_framework
    - evidence.flipkart.pipeline_architecture
    confidence: medium
    review_status: review_required
    source_aliases:
    - DOCX table header also says zs_observe; pipeline section says flipkart_oms lives in zs_recon_processor
```

```yaml
candidate_card:
  card_type: table
  card_id: table.flipkart.settlement
  name: zs_observe.flipkart_settlement
  fields:
    schema_name: zs_observe
    table_name: flipkart_settlement
    source_aliases:
    - zs_refined.flipkart_settlement in sample SQL
    - zs_observe.flipkart_settlement in table header and most source examples
    marketplace_module: settlement
    grain: settlement line / order item settlement row
    primary_keys:
    - settlement_id
    - order_id
    - item_id
    business_keys:
    - order_id
    - item_id
    - invoice_number
    - sku_id
    date_columns:
    - settlement_date
    - created_date
    amount_columns:
    - settled_amount
    - sale_settled_amount
    - refund_settled_amount
    - offer_settled_amount
    - my_share_settled_amount
    - addon_settled_amount
    - taxes_settled_amount
    - offer_adjustment_settled_amount
    - protection_fund_settled_amount
    - mp_fee
    - gst_on_mp_fees
    - total_tcs_amount
    - total_tds_amount
    - total_tax
    status_columns:
    - neft_type
    - fulfilment_type
    - return_type
    - is_active
    - is_duplicated
    - zen_status
    scope_columns_as_columns_only:
    - group_level_id
    - group_id
    known_filters:
    - is_active = true
    - 'documented scope value: group_level_id = 66388'
    source_caveats:
    - Granular fee columns can be null; mp_fee is the reliable aggregate for fee impact.
    - Core waterfall includes my_share_settled_amount, addon_settled_amount, and taxes_settled_amount in addition to sale/refund/offer/protection/fee/tax
      components.
    - group_level_id value 66388 appears in settlement examples; do not treat as account binding.
    evidence_refs:
    - evidence.flipkart.settlement
    - evidence.flipkart.settlement_logic
    - evidence.flipkart.scope_caveats
    confidence: high
    review_status: accepted
    documented_scope_values:
      group_level_id:
      - 66388
```

```yaml
candidate_card:
  card_type: table
  card_id: table.flipkart.commission
  name: zs_observe.flipkart_commission
  fields:
    schema_name: zs_observe
    table_name: flipkart_commission
    marketplace_module: fees
    grain: fee invoice line; many rows per order item
    primary_keys:
    - id / source row identifier if present
    business_keys:
    - order_id
    - item_id
    - invoice_number
    date_columns:
    - created_date
    - date
    amount_columns:
    - charged_amount
    - total_tax
    - fee_amount
    - fee_waiver_amount
    - total_fee_amount
    - total_tax_amount
    status_columns:
    - metadata
    - transaction_type
    - service_type
    - description
    - fee_name
    - is_active
    scope_columns_as_columns_only:
    - group_level_id
    - group_id
    known_filters:
    - is_active = true
    - 'documented scope value: group_level_id = 22'
    source_caveats:
    - order_id is stored without OD prefix; normalize when joining to settlement/OMS/cashback.
    - Pre-aggregate by order_id,item_id before joining to settlement or OMS.
    - Use charged_amount and total_tax as authoritative decimal fields; secondary fee amount columns are string legacy fields and must be cast.
    - Active rows are documented as transaction_type = 'Order Item' and metadata = 'commission invoice'.
    evidence_refs:
    - evidence.flipkart.commission
    - evidence.flipkart.commission_schema
    - evidence.flipkart.relationships
    confidence: high
    review_status: accepted
    documented_scope_values:
      group_level_id:
      - 22
```

```yaml
candidate_card:
  card_type: table
  card_id: table.flipkart.cashback
  name: zs_observe.flipkart_cashback
  fields:
    schema_name: zs_observe
    table_name: flipkart_cashback
    marketplace_module: cashback/promotions
    grain: credit/debit note line / promotional subsidy line
    primary_keys:
    - credit_debit_note_no
    - order_id
    - item_id
    business_keys:
    - order_id
    - item_id
    - credit_debit_note_no
    - invoice_number
    date_columns:
    - created_date
    - invoice_date
    amount_columns:
    - charged_amount
    - charged_amount_excluding_tax
    - taxable_value
    - tds_amount
    - manual_charge_amount_excluding_tax
    status_columns:
    - transaction_type
    - internal_transaction_type
    - document_type
    - document_sub_type
    - is_shopsy_order_
    - is_active
    scope_columns_as_columns_only:
    - group_level_id
    - group_id
    known_filters:
    - is_active = true
    - 'documented scope value: group_level_id = 22'
    source_caveats:
    - charged_amount is signed; positive forward credit notes and negative reverse/cancel debit notes must not be flattened.
    - document_type and document_sub_type can be null and must be preserved.
    - created_date is the documented primary date filter; invoice_date is a string and should not be used as a native date without parsing.
    evidence_refs:
    - evidence.flipkart.cashback
    - evidence.flipkart.cashback_schema
    - evidence.flipkart.shopsy
    confidence: high
    review_status: accepted
    documented_scope_values:
      group_level_id:
      - 22
```

### 5.5 Column Cards

```yaml
candidate_card:
  card_type: column
  card_id: column.oms.order_id
  name: table.flipkart.oms.order_id
  fields:
    table_id: table.flipkart.oms
    column_name: order_id
    data_type: string
    semantic_type: marketplace_order_identifier
    business_meaning: Primary marketplace order identifier; may contain OD prefix.
    metric_role: ''
    join_role: join_key
    filter_role: ''
    source_caveats: []
    evidence_refs: 
      - evidence.flipkart.oms
    confidence: medium
    review_status: review_required
```

```yaml
candidate_card:
  card_type: column
  card_id: column.oms.item_id
  name: table.flipkart.oms.item_id
  fields:
    table_id: table.flipkart.oms
    column_name: item_id
    data_type: string
    semantic_type: marketplace_order_item_identifier
    business_meaning: Order item / line identifier.
    metric_role: ''
    join_role: join_key
    filter_role: ''
    source_caveats: []
    evidence_refs: 
      - evidence.flipkart.oms
    confidence: medium
    review_status: review_required
```

```yaml
candidate_card:
  card_type: column
  card_id: column.oms.charged_amount
  name: table.flipkart.oms.charged_amount
  fields:
    table_id: table.flipkart.oms
    column_name: charged_amount
    data_type: decimal
    semantic_type: order_amount
    business_meaning: Order/transaction amount used for GMV-like calculations when OMS schema is verified.
    metric_role: metric_amount
    join_role: ''
    filter_role: ''
    source_caveats: []
    evidence_refs: 
      - evidence.flipkart.oms
    confidence: medium
    review_status: review_required
```

```yaml
candidate_card:
  card_type: column
  card_id: column.oms.transaction_type
  name: table.flipkart.oms.transaction_type
  fields:
    table_id: table.flipkart.oms
    column_name: transaction_type
    data_type: string
    semantic_type: transaction_direction
    business_meaning: Forward, reverse, or cancellation transaction indicator.
    metric_role: ''
    join_role: ''
    filter_role: filter/status
    source_caveats: []
    evidence_refs: 
      - evidence.flipkart.oms
    confidence: medium
    review_status: review_required
```

```yaml
candidate_card:
  card_type: column
  card_id: column.oms.fulfilment_type
  name: table.flipkart.oms.fulfilment_type
  fields:
    table_id: table.flipkart.oms
    column_name: fulfilment_type
    data_type: string
    semantic_type: fulfilment_model
    business_meaning: OMS fulfilment naming such as FBF or NON_FBF.
    metric_role: ''
    join_role: ''
    filter_role: filter
    source_caveats: []
    evidence_refs: 
      - evidence.flipkart.oms
    confidence: medium
    review_status: review_required
```

```yaml
candidate_card:
  card_type: column
  card_id: column.oms.is_shopsy_order_
  name: table.flipkart.oms.is_shopsy_order_
  fields:
    table_id: table.flipkart.oms
    column_name: is_shopsy_order_
    data_type: string
    semantic_type: sub_platform_flag
    business_meaning: String Shopsy flag; treat true/false as strings unless typed otherwise in warehouse.
    metric_role: ''
    join_role: ''
    filter_role: filter
    source_caveats: []
    evidence_refs: 
      - evidence.flipkart.oms
    confidence: medium
    review_status: review_required
```

```yaml
candidate_card:
  card_type: column
  card_id: column.oms.quantity
  name: table.flipkart.oms.quantity
  fields:
    table_id: table.flipkart.oms
    column_name: quantity
    data_type: decimal
    semantic_type: item_quantity
    business_meaning: Quantity for item-level order calculations.
    metric_role: metric_amount
    join_role: ''
    filter_role: ''
    source_caveats: []
    evidence_refs: 
      - evidence.flipkart.oms
    confidence: medium
    review_status: review_required
```

```yaml
candidate_card:
  card_type: column
  card_id: column.oms.currency_type
  name: table.flipkart.oms.currency_type
  fields:
    table_id: table.flipkart.oms
    column_name: currency_type
    data_type: string
    semantic_type: currency
    business_meaning: Currency, expected INR for Flipkart India.
    metric_role: ''
    join_role: ''
    filter_role: ''
    source_caveats: []
    evidence_refs: 
      - evidence.flipkart.oms
    confidence: medium
    review_status: review_required
```

```yaml
candidate_card:
  card_type: column
  card_id: column.oms.created_date
  name: table.flipkart.oms.created_date
  fields:
    table_id: table.flipkart.oms
    column_name: created_date
    data_type: timestamp_review_required
    semantic_type: event_date
    business_meaning: Order/row created timestamp or date; source table body is inconsistent, so date usage remains review-required.
    metric_role: ''
    join_role: ''
    filter_role: ''
    source_caveats:
    - DOCX table body repeats cashback schema; verify actual zs_recon_processor.flipkart_oms type before strict date filtering.
    evidence_refs:
    - evidence.flipkart.oms
    - evidence.flipkart.pipeline_architecture
    confidence: medium
    review_status: review_required
```

```yaml
candidate_card:
  card_type: column
  card_id: column.oms.is_active
  name: table.flipkart.oms.is_active
  fields:
    table_id: table.flipkart.oms
    column_name: is_active
    data_type: boolean
    semantic_type: active_row_flag
    business_meaning: Mandatory active-row filter.
    metric_role: ''
    join_role: ''
    filter_role: filter
    source_caveats: []
    evidence_refs: 
      - evidence.flipkart.oms
    confidence: medium
    review_status: review_required
```

```yaml
candidate_card:
  card_type: column
  card_id: column.oms.group_level_id
  name: table.flipkart.oms.group_level_id
  fields:
    table_id: table.flipkart.oms
    column_name: group_level_id
    data_type: integer
    semantic_type: scope_column_only
    business_meaning: Table-level scope column; not a marketplace account card.
    metric_role: ''
    join_role: ''
    filter_role: filter_caveat
    source_caveats:
    - Scope column only; never emit tenant/group/account-binding cards from this field.
    - Documented scope value only; do not create tenant/group/account-binding cards.
    evidence_refs:
    - evidence.flipkart.scope_caveats
    - evidence.flipkart.pitfalls
    confidence: medium
    review_status: review_required
    documented_scope_values:
    - 22
    - 26
    - 65787
    - 65853
```

```yaml
candidate_card:
  card_type: column
  card_id: column.settlement.settlement_id
  name: table.flipkart.settlement.settlement_id
  fields:
    table_id: table.flipkart.settlement
    column_name: settlement_id
    data_type: string
    semantic_type: marketplace_settlement_identifier
    business_meaning: Flipkart settlement / NEFT batch identifier.
    metric_role: ''
    join_role: join/report_key
    filter_role: ''
    source_caveats: []
    evidence_refs: 
      - evidence.flipkart.settlement
    confidence: high
    review_status: accepted
```

```yaml
candidate_card:
  card_type: column
  card_id: column.settlement.order_id
  name: table.flipkart.settlement.order_id
  fields:
    table_id: table.flipkart.settlement
    column_name: order_id
    data_type: string
    semantic_type: marketplace_order_identifier
    business_meaning: Order identifier, commonly with OD prefix.
    metric_role: ''
    join_role: join_key
    filter_role: ''
    source_caveats: []
    evidence_refs: 
      - evidence.flipkart.settlement
    confidence: high
    review_status: accepted
```

```yaml
candidate_card:
  card_type: column
  card_id: column.settlement.item_id
  name: table.flipkart.settlement.item_id
  fields:
    table_id: table.flipkart.settlement
    column_name: item_id
    data_type: string
    semantic_type: marketplace_order_item_identifier
    business_meaning: Item-level join key.
    metric_role: ''
    join_role: join_key
    filter_role: ''
    source_caveats: []
    evidence_refs: 
      - evidence.flipkart.settlement
    confidence: high
    review_status: accepted
```

```yaml
candidate_card:
  card_type: column
  card_id: column.settlement.invoice_number
  name: table.flipkart.settlement.invoice_number
  fields:
    table_id: table.flipkart.settlement
    column_name: invoice_number
    data_type: string
    semantic_type: invoice_identifier
    business_meaning: Invoice identifier used for reporting and join context.
    metric_role: ''
    join_role: join_key
    filter_role: ''
    source_caveats: []
    evidence_refs: 
      - evidence.flipkart.settlement
    confidence: high
    review_status: accepted
```

```yaml
candidate_card:
  card_type: column
  card_id: column.settlement.sku_id
  name: table.flipkart.settlement.sku_id
  fields:
    table_id: table.flipkart.settlement
    column_name: sku_id
    data_type: string
    semantic_type: sku_identifier
    business_meaning: Seller SKU or product identifier.
    metric_role: ''
    join_role: ''
    filter_role: ''
    source_caveats: []
    evidence_refs: 
      - evidence.flipkart.settlement
    confidence: high
    review_status: accepted
```

```yaml
candidate_card:
  card_type: column
  card_id: column.settlement.product_sub_category
  name: table.flipkart.settlement.product_sub_category
  fields:
    table_id: table.flipkart.settlement
    column_name: product_sub_category
    data_type: string
    semantic_type: product_category
    business_meaning: Product category/sub-category used for analysis.
    metric_role: ''
    join_role: ''
    filter_role: ''
    source_caveats: []
    evidence_refs: 
      - evidence.flipkart.settlement
    confidence: high
    review_status: accepted
```

```yaml
candidate_card:
  card_type: column
  card_id: column.settlement.quantity
  name: table.flipkart.settlement.quantity
  fields:
    table_id: table.flipkart.settlement
    column_name: quantity
    data_type: decimal
    semantic_type: settled_quantity
    business_meaning: Quantity at settlement line.
    metric_role: metric_amount
    join_role: ''
    filter_role: ''
    source_caveats: []
    evidence_refs: 
      - evidence.flipkart.settlement
    confidence: high
    review_status: accepted
```

```yaml
candidate_card:
  card_type: column
  card_id: column.settlement.settled_amount
  name: table.flipkart.settlement.settled_amount
  fields:
    table_id: table.flipkart.settlement
    column_name: settled_amount
    data_type: decimal
    semantic_type: net_marketplace_settlement
    business_meaning: Actual net amount settled by Flipkart for the line.
    metric_role: metric_amount
    join_role: ''
    filter_role: ''
    source_caveats: []
    evidence_refs: 
      - evidence.flipkart.settlement
    confidence: high
    review_status: accepted
```

```yaml
candidate_card:
  card_type: column
  card_id: column.settlement.sale_settled_amount
  name: table.flipkart.settlement.sale_settled_amount
  fields:
    table_id: table.flipkart.settlement
    column_name: sale_settled_amount
    data_type: decimal
    semantic_type: sale_component
    business_meaning: Sale settlement component used as denominator for realization and fee rates.
    metric_role: metric_amount
    join_role: ''
    filter_role: ''
    source_caveats: []
    evidence_refs: 
      - evidence.flipkart.settlement
    confidence: high
    review_status: accepted
```

```yaml
candidate_card:
  card_type: column
  card_id: column.settlement.refund_settled_amount
  name: table.flipkart.settlement.refund_settled_amount
  fields:
    table_id: table.flipkart.settlement
    column_name: refund_settled_amount
    data_type: decimal
    semantic_type: refund_component
    business_meaning: Refund / reverse settlement component.
    metric_role: metric_amount
    join_role: ''
    filter_role: ''
    source_caveats: []
    evidence_refs: 
      - evidence.flipkart.settlement
    confidence: high
    review_status: accepted
```

```yaml
candidate_card:
  card_type: column
  card_id: column.settlement.offer_settled_amount
  name: table.flipkart.settlement.offer_settled_amount
  fields:
    table_id: table.flipkart.settlement
    column_name: offer_settled_amount
    data_type: decimal
    semantic_type: offer_component
    business_meaning: Offer/cashback settlement component.
    metric_role: metric_amount
    join_role: ''
    filter_role: ''
    source_caveats: []
    evidence_refs: 
      - evidence.flipkart.settlement
    confidence: high
    review_status: accepted
```

```yaml
candidate_card:
  card_type: column
  card_id: column.settlement.offer_adjustment_settled_amount
  name: table.flipkart.settlement.offer_adjustment_settled_amount
  fields:
    table_id: table.flipkart.settlement
    column_name: offer_adjustment_settled_amount
    data_type: decimal
    semantic_type: offer_adjustment_component
    business_meaning: Offer adjustment component used in cashback reconciliation.
    metric_role: metric_amount
    join_role: ''
    filter_role: ''
    source_caveats: []
    evidence_refs: 
      - evidence.flipkart.settlement
    confidence: high
    review_status: accepted
```

```yaml
candidate_card:
  card_type: column
  card_id: column.settlement.protection_fund_settled_amount
  name: table.flipkart.settlement.protection_fund_settled_amount
  fields:
    table_id: table.flipkart.settlement
    column_name: protection_fund_settled_amount
    data_type: decimal
    semantic_type: protection_fund_component
    business_meaning: Protection fund settlement component.
    metric_role: metric_amount
    join_role: ''
    filter_role: ''
    source_caveats: []
    evidence_refs: 
      - evidence.flipkart.settlement
    confidence: high
    review_status: accepted
```

```yaml
candidate_card:
  card_type: column
  card_id: column.settlement.mp_fee
  name: table.flipkart.settlement.mp_fee
  fields:
    table_id: table.flipkart.settlement
    column_name: mp_fee
    data_type: decimal
    semantic_type: marketplace_fee_total
    business_meaning: Aggregate marketplace fee impact; often more reliable than granular fee columns.
    metric_role: metric_amount
    join_role: ''
    filter_role: ''
    source_caveats: []
    evidence_refs: 
      - evidence.flipkart.settlement
    confidence: high
    review_status: accepted
```

```yaml
candidate_card:
  card_type: column
  card_id: column.settlement.gst_on_mp_fees
  name: table.flipkart.settlement.gst_on_mp_fees
  fields:
    table_id: table.flipkart.settlement
    column_name: gst_on_mp_fees
    data_type: decimal
    semantic_type: gst_on_marketplace_fees
    business_meaning: GST charged on marketplace fees.
    metric_role: metric_amount
    join_role: ''
    filter_role: ''
    source_caveats: []
    evidence_refs: 
      - evidence.flipkart.settlement
    confidence: high
    review_status: accepted
```

```yaml
candidate_card:
  card_type: column
  card_id: column.settlement.total_tcs_amount
  name: table.flipkart.settlement.total_tcs_amount
  fields:
    table_id: table.flipkart.settlement
    column_name: total_tcs_amount
    data_type: decimal
    semantic_type: tcs_deduction
    business_meaning: Marketplace TCS deduction cash-flow field.
    metric_role: metric_amount
    join_role: ''
    filter_role: ''
    source_caveats: []
    evidence_refs: 
      - evidence.flipkart.settlement
    confidence: high
    review_status: accepted
```

```yaml
candidate_card:
  card_type: column
  card_id: column.settlement.total_tds_amount
  name: table.flipkart.settlement.total_tds_amount
  fields:
    table_id: table.flipkart.settlement
    column_name: total_tds_amount
    data_type: decimal
    semantic_type: tds_deduction
    business_meaning: Marketplace TDS deduction cash-flow field.
    metric_role: metric_amount
    join_role: ''
    filter_role: ''
    source_caveats: []
    evidence_refs: 
      - evidence.flipkart.settlement
    confidence: high
    review_status: accepted
```

```yaml
candidate_card:
  card_type: column
  card_id: column.settlement.commission_fee
  name: table.flipkart.settlement.commission_fee
  fields:
    table_id: table.flipkart.settlement
    column_name: commission_fee
    data_type: decimal
    semantic_type: commission_fee_component
    business_meaning: Settlement-level commission fee component, may be null.
    metric_role: metric_amount
    join_role: ''
    filter_role: ''
    source_caveats: []
    evidence_refs: 
      - evidence.flipkart.settlement
    confidence: high
    review_status: accepted
```

```yaml
candidate_card:
  card_type: column
  card_id: column.settlement.shipping_fee
  name: table.flipkart.settlement.shipping_fee
  fields:
    table_id: table.flipkart.settlement
    column_name: shipping_fee
    data_type: decimal
    semantic_type: shipping_fee_component
    business_meaning: Marketplace shipping fee component, not external logistics card.
    metric_role: metric_amount
    join_role: ''
    filter_role: ''
    source_caveats: []
    evidence_refs: 
      - evidence.flipkart.settlement
    confidence: high
    review_status: accepted
```

```yaml
candidate_card:
  card_type: column
  card_id: column.settlement.fixed_fee
  name: table.flipkart.settlement.fixed_fee
  fields:
    table_id: table.flipkart.settlement
    column_name: fixed_fee
    data_type: decimal
    semantic_type: fixed_fee_component
    business_meaning: Fixed/closing fee component.
    metric_role: metric_amount
    join_role: ''
    filter_role: ''
    source_caveats: []
    evidence_refs: 
      - evidence.flipkart.settlement
    confidence: high
    review_status: accepted
```

```yaml
candidate_card:
  card_type: column
  card_id: column.settlement.reverse_shipping_fee
  name: table.flipkart.settlement.reverse_shipping_fee
  fields:
    table_id: table.flipkart.settlement
    column_name: reverse_shipping_fee
    data_type: decimal
    semantic_type: reverse_shipping_fee_component
    business_meaning: Reverse shipping fee charged by marketplace.
    metric_role: metric_amount
    join_role: ''
    filter_role: ''
    source_caveats: []
    evidence_refs: 
      - evidence.flipkart.settlement
    confidence: high
    review_status: accepted
```

```yaml
candidate_card:
  card_type: column
  card_id: column.settlement.collection_fee
  name: table.flipkart.settlement.collection_fee
  fields:
    table_id: table.flipkart.settlement
    column_name: collection_fee
    data_type: decimal
    semantic_type: collection_fee_component
    business_meaning: Collection/COD/payment-related marketplace fee.
    metric_role: metric_amount
    join_role: ''
    filter_role: ''
    source_caveats: []
    evidence_refs: 
      - evidence.flipkart.settlement
    confidence: high
    review_status: accepted
```

```yaml
candidate_card:
  card_type: column
  card_id: column.settlement.franchise_fee
  name: table.flipkart.settlement.franchise_fee
  fields:
    table_id: table.flipkart.settlement
    column_name: franchise_fee
    data_type: decimal
    semantic_type: franchise_fee_component
    business_meaning: Marketplace franchise fee component if populated.
    metric_role: metric_amount
    join_role: ''
    filter_role: ''
    source_caveats: []
    evidence_refs: 
      - evidence.flipkart.settlement
    confidence: high
    review_status: accepted
```

```yaml
candidate_card:
  card_type: column
  card_id: column.settlement.pick_and_pack_fee
  name: table.flipkart.settlement.pick_and_pack_fee
  fields:
    table_id: table.flipkart.settlement
    column_name: pick_and_pack_fee
    data_type: decimal
    semantic_type: pick_pack_fee_component
    business_meaning: Marketplace fulfilment pick and pack fee component.
    metric_role: metric_amount
    join_role: ''
    filter_role: ''
    source_caveats: []
    evidence_refs: 
      - evidence.flipkart.settlement
    confidence: high
    review_status: accepted
```

```yaml
candidate_card:
  card_type: column
  card_id: column.settlement.neft_type
  name: table.flipkart.settlement.neft_type
  fields:
    table_id: table.flipkart.settlement
    column_name: neft_type
    data_type: string
    semantic_type: settlement_payment_type
    business_meaning: Settlement mode/cycle classification such as prepaid/postpaid semantics.
    metric_role: ''
    join_role: ''
    filter_role: filter
    source_caveats: []
    evidence_refs: 
      - evidence.flipkart.settlement
    confidence: high
    review_status: accepted
```

```yaml
candidate_card:
  card_type: column
  card_id: column.settlement.vendor_payout
  name: table.flipkart.settlement.vendor_payout
  fields:
    table_id: table.flipkart.settlement
    column_name: vendor_payout
    data_type: string
    semantic_type: vendor_payout_identifier
    business_meaning: Vendor/payout identifier field; not a numeric bank-payout amount and not a bank card.
    metric_role: metric_amount
    join_role: ''
    filter_role: ''
    source_caveats:
    - DOCX settlement identifiers table declares vendor_payout as string.
    evidence_refs:
    - evidence.flipkart.settlement_logic
    confidence: high
    review_status: accepted
```

```yaml
candidate_card:
  card_type: column
  card_id: column.settlement.settlement_date
  name: table.flipkart.settlement.settlement_date
  fields:
    table_id: table.flipkart.settlement
    column_name: settlement_date
    data_type: date
    semantic_type: settlement_date
    business_meaning: Date of marketplace settlement.
    metric_role: ''
    join_role: ''
    filter_role: ''
    source_caveats: []
    evidence_refs: 
      - evidence.flipkart.settlement
    confidence: high
    review_status: accepted
```

```yaml
candidate_card:
  card_type: column
  card_id: column.settlement.created_date
  name: table.flipkart.settlement.created_date
  fields:
    table_id: table.flipkart.settlement
    column_name: created_date
    data_type: date
    semantic_type: row_created_date
    business_meaning: Row created date; settlement-cycle fallback.
    metric_role: ''
    join_role: ''
    filter_role: ''
    source_caveats: []
    evidence_refs: 
      - evidence.flipkart.settlement
    confidence: high
    review_status: accepted
```


```yaml
candidate_card:
  card_type: column
  card_id: column.settlement.fulfilment_type
  name: table.flipkart.settlement.fulfilment_type
  fields:
    table_id: table.flipkart.settlement
    column_name: fulfilment_type
    data_type: string
    semantic_type: settlement_fulfilment_model
    business_meaning: Settlement naming such as flipkart_fulfilment or seller_easy_ship.
    metric_role: ''
    join_role: ''
    filter_role: filter
    source_caveats: []
    evidence_refs: 
      - evidence.flipkart.settlement
    confidence: high
    review_status: accepted
```

```yaml
candidate_card:
  card_type: column
  card_id: column.settlement.return_type
  name: table.flipkart.settlement.return_type
  fields:
    table_id: table.flipkart.settlement
    column_name: return_type
    data_type: string
    semantic_type: return_classification
    business_meaning: Return/reverse classification.
    metric_role: ''
    join_role: ''
    filter_role: filter
    source_caveats: []
    evidence_refs: 
      - evidence.flipkart.settlement
    confidence: high
    review_status: accepted
```

```yaml
candidate_card:
  card_type: column
  card_id: column.settlement.zone
  name: table.flipkart.settlement.zone
  fields:
    table_id: table.flipkart.settlement
    column_name: zone
    data_type: string
    semantic_type: marketplace_zone
    business_meaning: Marketplace shipping zone for fee analysis.
    metric_role: ''
    join_role: ''
    filter_role: filter
    source_caveats: []
    evidence_refs: 
      - evidence.flipkart.settlement
    confidence: high
    review_status: accepted
```

```yaml
candidate_card:
  card_type: column
  card_id: column.settlement.tier
  name: table.flipkart.settlement.tier
  fields:
    table_id: table.flipkart.settlement
    column_name: tier
    data_type: string
    semantic_type: marketplace_city_tier
    business_meaning: City tier / marketplace settlement tier field if populated; do not treat as seller performance tier without a documented
      seller-tier column.
    metric_role: ''
    join_role: ''
    filter_role: filter
    source_caveats:
    - DOCX fulfilment/logistics section lists tier as City tier; seller-tier system is described conceptually but no seller-tier schema column
      is identified.
    evidence_refs:
    - evidence.flipkart.settlement_logic
    - evidence.flipkart.seller_tier
    confidence: high
    review_status: accepted
```

```yaml
candidate_card:
  card_type: column
  card_id: column.settlement.gross_weight
  name: table.flipkart.settlement.gross_weight
  fields:
    table_id: table.flipkart.settlement
    column_name: gross_weight
    data_type: decimal
    semantic_type: gross_weight
    business_meaning: Weight used in marketplace shipping/fee analysis.
    metric_role: metric_attribute
    join_role: ''
    filter_role: ''
    source_caveats: []
    evidence_refs: 
      - evidence.flipkart.settlement
    confidence: high
    review_status: accepted
```

```yaml
candidate_card:
  card_type: column
  card_id: column.settlement.vol_weight
  name: table.flipkart.settlement.vol_weight
  fields:
    table_id: table.flipkart.settlement
    column_name: vol_weight
    data_type: decimal
    semantic_type: volumetric_weight
    business_meaning: Volumetric weight used in shipping fee calculations.
    metric_role: metric_attribute
    join_role: ''
    filter_role: ''
    source_caveats: []
    evidence_refs: 
      - evidence.flipkart.settlement
    confidence: high
    review_status: accepted
```

```yaml
candidate_card:
  card_type: column
  card_id: column.settlement.is_active
  name: table.flipkart.settlement.is_active
  fields:
    table_id: table.flipkart.settlement
    column_name: is_active
    data_type: boolean
    semantic_type: active_row_flag
    business_meaning: Mandatory active-row filter.
    metric_role: ''
    join_role: ''
    filter_role: filter
    source_caveats: []
    evidence_refs: 
      - evidence.flipkart.settlement
    confidence: high
    review_status: accepted
```

```yaml
candidate_card:
  card_type: column
  card_id: column.settlement.is_duplicated
  name: table.flipkart.settlement.is_duplicated
  fields:
    table_id: table.flipkart.settlement
    column_name: is_duplicated
    data_type: boolean
    semantic_type: duplicate_flag
    business_meaning: Duplicate row marker for data-quality checks.
    metric_role: ''
    join_role: ''
    filter_role: filter
    source_caveats: []
    evidence_refs: 
      - evidence.flipkart.settlement
    confidence: high
    review_status: accepted
```

```yaml
candidate_card:
  card_type: column
  card_id: column.settlement.zen_status
  name: table.flipkart.settlement.zen_status
  fields:
    table_id: table.flipkart.settlement
    column_name: zen_status
    data_type: string
    semantic_type: zen_status
    business_meaning: Internal status field; use only if documented in source.
    metric_role: ''
    join_role: ''
    filter_role: ''
    source_caveats: []
    evidence_refs: 
      - evidence.flipkart.settlement
    confidence: high
    review_status: accepted
```

```yaml
candidate_card:
  card_type: column
  card_id: column.settlement.group_level_id
  name: table.flipkart.settlement.group_level_id
  fields:
    table_id: table.flipkart.settlement
    column_name: group_level_id
    data_type: integer
    semantic_type: scope_column_only
    business_meaning: Table-level scope column; not an account-binding card.
    metric_role: ''
    join_role: ''
    filter_role: filter_caveat
    source_caveats:
    - Scope column only; never emit tenant/group/account-binding cards from this field.
    - Documented scope value only; do not create tenant/group/account-binding cards.
    evidence_refs:
    - evidence.flipkart.settlement_logic
    - evidence.flipkart.scope_caveats
    confidence: high
    review_status: accepted
    documented_scope_values:
    - 66388
```

```yaml
candidate_card:
  card_type: column
  card_id: column.settlement.group_id
  name: table.flipkart.settlement.group_id
  fields:
    table_id: table.flipkart.settlement
    column_name: group_id
    data_type: integer
    semantic_type: scope_column_only
    business_meaning: Table-level scope column; not a group card.
    metric_role: ''
    join_role: ''
    filter_role: filter_caveat
    source_caveats: 
      - Scope column only; never emit tenant/group/account-binding cards from this field.
    evidence_refs: 
      - evidence.flipkart.settlement
    confidence: high
    review_status: accepted
```

```yaml
candidate_card:
  card_type: column
  card_id: column.commission.order_id
  name: table.flipkart.commission.order_id
  fields:
    table_id: table.flipkart.commission
    column_name: order_id
    data_type: string
    semantic_type: marketplace_order_identifier_without_od
    business_meaning: Order id stored without OD prefix; normalize before cross-table joins.
    metric_role: ''
    join_role: join_key
    filter_role: ''
    source_caveats: 
      - Commission order_id lacks OD prefix; apply REPLACE on other tables before joining.
    evidence_refs: 
      - evidence.flipkart.commission
    confidence: high
    review_status: accepted
```

```yaml
candidate_card:
  card_type: column
  card_id: column.commission.item_id
  name: table.flipkart.commission.item_id
  fields:
    table_id: table.flipkart.commission
    column_name: item_id
    data_type: string
    semantic_type: marketplace_order_item_identifier
    business_meaning: Item-level key.
    metric_role: ''
    join_role: join_key
    filter_role: ''
    source_caveats: []
    evidence_refs: 
      - evidence.flipkart.commission
    confidence: high
    review_status: accepted
```

```yaml
candidate_card:
  card_type: column
  card_id: column.commission.invoice_number
  name: table.flipkart.commission.invoice_number
  fields:
    table_id: table.flipkart.commission
    column_name: invoice_number
    data_type: string
    semantic_type: invoice_identifier
    business_meaning: Invoice identifier for fee lines.
    metric_role: ''
    join_role: join_key
    filter_role: ''
    source_caveats: []
    evidence_refs: 
      - evidence.flipkart.commission
    confidence: high
    review_status: accepted
```

```yaml
candidate_card:
  card_type: column
  card_id: column.commission.description
  name: table.flipkart.commission.description
  fields:
    table_id: table.flipkart.commission
    column_name: description
    data_type: string
    semantic_type: fee_description
    business_meaning: Fee class such as Commission, Fixed Fee, Shipping Fee, Reverse Shipping Fee, Collection Fee.
    metric_role: ''
    join_role: ''
    filter_role: filter
    source_caveats: []
    evidence_refs: 
      - evidence.flipkart.commission
    confidence: high
    review_status: accepted
```

```yaml
candidate_card:
  card_type: column
  card_id: column.commission.fee_name
  name: table.flipkart.commission.fee_name
  fields:
    table_id: table.flipkart.commission
    column_name: fee_name
    data_type: string
    semantic_type: fee_name
    business_meaning: Fee display name / subcategory.
    metric_role: ''
    join_role: ''
    filter_role: filter
    source_caveats: []
    evidence_refs: 
      - evidence.flipkart.commission
    confidence: high
    review_status: accepted
```

```yaml
candidate_card:
  card_type: column
  card_id: column.commission.charged_amount
  name: table.flipkart.commission.charged_amount
  fields:
    table_id: table.flipkart.commission
    column_name: charged_amount
    data_type: decimal
    semantic_type: fee_charged_amount
    business_meaning: Core fee amount for detailed fee calculations.
    metric_role: metric_amount
    join_role: ''
    filter_role: ''
    source_caveats: []
    evidence_refs: 
      - evidence.flipkart.commission
    confidence: high
    review_status: accepted
```

```yaml
candidate_card:
  card_type: column
  card_id: column.commission.total_tax
  name: table.flipkart.commission.total_tax
  fields:
    table_id: table.flipkart.commission
    column_name: total_tax
    data_type: decimal
    semantic_type: fee_tax_amount
    business_meaning: Tax on fee line.
    metric_role: metric_amount
    join_role: ''
    filter_role: ''
    source_caveats: []
    evidence_refs: 
      - evidence.flipkart.commission
    confidence: high
    review_status: accepted
```

```yaml
candidate_card:
  card_type: column
  card_id: column.commission.fee_amount
  name: table.flipkart.commission.fee_amount
  fields:
    table_id: table.flipkart.commission
    column_name: fee_amount
    data_type: string
    semantic_type: legacy_fee_amount
    business_meaning: Legacy/string fee amount; cast before numeric use.
    metric_role: metric_amount_caveat
    join_role: ''
    filter_role: ''
    source_caveats: 
      - Cast from string before numeric use.
    evidence_refs: 
      - evidence.flipkart.commission
    confidence: high
    review_status: accepted
```

```yaml
candidate_card:
  card_type: column
  card_id: column.commission.fee_waiver_amount
  name: table.flipkart.commission.fee_waiver_amount
  fields:
    table_id: table.flipkart.commission
    column_name: fee_waiver_amount
    data_type: string
    semantic_type: legacy_fee_waiver_amount
    business_meaning: Legacy/string waiver amount; cast before numeric use.
    metric_role: metric_amount_caveat
    join_role: ''
    filter_role: ''
    source_caveats: 
      - Cast from string before numeric use.
    evidence_refs: 
      - evidence.flipkart.commission
    confidence: high
    review_status: accepted
```




```yaml
candidate_card:
  card_type: column
  card_id: column.commission.created_date
  name: table.flipkart.commission.created_date
  fields:
    table_id: table.flipkart.commission
    column_name: created_date
    data_type: date
    semantic_type: row_created_date
    business_meaning: Row created date.
    metric_role: ''
    join_role: ''
    filter_role: ''
    source_caveats: []
    evidence_refs: 
      - evidence.flipkart.commission
    confidence: high
    review_status: accepted
```



```yaml
candidate_card:
  card_type: column
  card_id: column.commission.is_active
  name: table.flipkart.commission.is_active
  fields:
    table_id: table.flipkart.commission
    column_name: is_active
    data_type: boolean
    semantic_type: active_row_flag
    business_meaning: Mandatory active-row filter.
    metric_role: ''
    join_role: ''
    filter_role: filter
    source_caveats: []
    evidence_refs: 
      - evidence.flipkart.commission
    confidence: high
    review_status: accepted
```

```yaml
candidate_card:
  card_type: column
  card_id: column.commission.group_level_id
  name: table.flipkart.commission.group_level_id
  fields:
    table_id: table.flipkart.commission
    column_name: group_level_id
    data_type: integer
    semantic_type: scope_column_only
    business_meaning: Table-level scope column, not account binding.
    metric_role: ''
    join_role: ''
    filter_role: filter_caveat
    source_caveats:
    - Scope column only; never emit tenant/group/account-binding cards from this field.
    - Documented scope value only; do not create tenant/group/account-binding cards.
    evidence_refs:
    - evidence.flipkart.commission_schema
    - evidence.flipkart.scope_caveats
    confidence: high
    review_status: accepted
    documented_scope_values:
    - 22
```

```yaml
candidate_card:
  card_type: column
  card_id: column.commission.group_id
  name: table.flipkart.commission.group_id
  fields:
    table_id: table.flipkart.commission
    column_name: group_id
    data_type: integer
    semantic_type: scope_column_only
    business_meaning: Table-level scope column, not group card.
    metric_role: ''
    join_role: ''
    filter_role: filter_caveat
    source_caveats: 
      - Scope column only; never emit tenant/group/account-binding cards from this field.
    evidence_refs: 
      - evidence.flipkart.commission
    confidence: high
    review_status: accepted
```

```yaml
candidate_card:
  card_type: column
  card_id: column.cashback.order_id
  name: table.flipkart.cashback.order_id
  fields:
    table_id: table.flipkart.cashback
    column_name: order_id
    data_type: string
    semantic_type: marketplace_order_identifier
    business_meaning: Order id used for cashback/order reconciliation.
    metric_role: ''
    join_role: join_key
    filter_role: ''
    source_caveats: []
    evidence_refs: 
      - evidence.flipkart.cashback
    confidence: high
    review_status: accepted
```

```yaml
candidate_card:
  card_type: column
  card_id: column.cashback.item_id
  name: table.flipkart.cashback.item_id
  fields:
    table_id: table.flipkart.cashback
    column_name: item_id
    data_type: string
    semantic_type: marketplace_order_item_identifier
    business_meaning: Order item key.
    metric_role: ''
    join_role: join_key
    filter_role: ''
    source_caveats: []
    evidence_refs: 
      - evidence.flipkart.cashback
    confidence: high
    review_status: accepted
```

```yaml
candidate_card:
  card_type: column
  card_id: column.cashback.credit_debit_note_no
  name: table.flipkart.cashback.credit_debit_note_no
  fields:
    table_id: table.flipkart.cashback
    column_name: credit_debit_note_no
    data_type: string
    semantic_type: credit_debit_note_identifier
    business_meaning: Credit/debit note identifier.
    metric_role: ''
    join_role: join/report_key
    filter_role: ''
    source_caveats: []
    evidence_refs: 
      - evidence.flipkart.cashback
    confidence: high
    review_status: accepted
```

```yaml
candidate_card:
  card_type: column
  card_id: column.cashback.invoice_number
  name: table.flipkart.cashback.invoice_number
  fields:
    table_id: table.flipkart.cashback
    column_name: invoice_number
    data_type: string
    semantic_type: invoice_identifier
    business_meaning: Invoice number.
    metric_role: ''
    join_role: join_key
    filter_role: ''
    source_caveats: []
    evidence_refs: 
      - evidence.flipkart.cashback
    confidence: high
    review_status: accepted
```

```yaml
candidate_card:
  card_type: column
  card_id: column.cashback.irn
  name: table.flipkart.cashback.irn
  fields:
    table_id: table.flipkart.cashback
    column_name: irn
    data_type: string
    semantic_type: invoice_reference_number
    business_meaning: IRN/tax invoice reference if populated.
    metric_role: ''
    join_role: ''
    filter_role: ''
    source_caveats: []
    evidence_refs: 
      - evidence.flipkart.cashback
    confidence: high
    review_status: accepted
```

```yaml
candidate_card:
  card_type: column
  card_id: column.cashback.transaction_type
  name: table.flipkart.cashback.transaction_type
  fields:
    table_id: table.flipkart.cashback
    column_name: transaction_type
    data_type: string
    semantic_type: cashback_transaction_type
    business_meaning: forward, reverse, forward cancel.
    metric_role: ''
    join_role: ''
    filter_role: filter/status
    source_caveats: []
    evidence_refs: 
      - evidence.flipkart.cashback
    confidence: high
    review_status: accepted
```

```yaml
candidate_card:
  card_type: column
  card_id: column.cashback.internal_transaction_type
  name: table.flipkart.cashback.internal_transaction_type
  fields:
    table_id: table.flipkart.cashback
    column_name: internal_transaction_type
    data_type: string
    semantic_type: internal_transaction_type
    business_meaning: Internal transaction classifier.
    metric_role: ''
    join_role: ''
    filter_role: filter/status
    source_caveats: []
    evidence_refs: 
      - evidence.flipkart.cashback
    confidence: high
    review_status: accepted
```

```yaml
candidate_card:
  card_type: column
  card_id: column.cashback.document_type
  name: table.flipkart.cashback.document_type
  fields:
    table_id: table.flipkart.cashback
    column_name: document_type
    data_type: string
    semantic_type: document_type
    business_meaning: Credit Note, Debit Note, or null.
    metric_role: ''
    join_role: ''
    filter_role: filter/status
    source_caveats: []
    evidence_refs: 
      - evidence.flipkart.cashback
    confidence: high
    review_status: accepted
```

```yaml
candidate_card:
  card_type: column
  card_id: column.cashback.document_sub_type
  name: table.flipkart.cashback.document_sub_type
  fields:
    table_id: table.flipkart.cashback
    column_name: document_sub_type
    data_type: string
    semantic_type: document_sub_type
    business_meaning: Sale, Return, Cancellation, or null.
    metric_role: ''
    join_role: ''
    filter_role: filter/status
    source_caveats: []
    evidence_refs: 
      - evidence.flipkart.cashback
    confidence: high
    review_status: accepted
```

```yaml
candidate_card:
  card_type: column
  card_id: column.cashback.charged_amount
  name: table.flipkart.cashback.charged_amount
  fields:
    table_id: table.flipkart.cashback
    column_name: charged_amount
    data_type: decimal
    semantic_type: cashback_or_promo_amount
    business_meaning: Signed cashback/promo amount.
    metric_role: metric_amount
    join_role: ''
    filter_role: ''
    source_caveats: 
      - Signed amount; preserve negative reverse/cancel semantics.
    evidence_refs: 
      - evidence.flipkart.cashback
    confidence: high
    review_status: accepted
```

```yaml
candidate_card:
  card_type: column
  card_id: column.cashback.total_tax
  name: table.flipkart.cashback.total_tax
  fields:
    table_id: table.flipkart.cashback
    column_name: total_tax
    data_type: decimal
    semantic_type: tax_amount
    business_meaning: Tax amount on cashback/credit-debit note line.
    metric_role: metric_amount
    join_role: ''
    filter_role: ''
    source_caveats: []
    evidence_refs: 
      - evidence.flipkart.cashback
    confidence: high
    review_status: accepted
```

```yaml
candidate_card:
  card_type: column
  card_id: column.cashback.fee_amount
  name: table.flipkart.cashback.fee_amount
  fields:
    table_id: table.flipkart.cashback
    column_name: fee_amount
    data_type: string
    semantic_type: legacy_fee_amount
    business_meaning: Legacy/string fee amount; cast before numeric use.
    metric_role: metric_amount_caveat
    join_role: ''
    filter_role: ''
    source_caveats: 
      - Cast from string before numeric use.
    evidence_refs: 
      - evidence.flipkart.cashback
    confidence: high
    review_status: accepted
```

```yaml
candidate_card:
  card_type: column
  card_id: column.cashback.fee_waiver_amount
  name: table.flipkart.cashback.fee_waiver_amount
  fields:
    table_id: table.flipkart.cashback
    column_name: fee_waiver_amount
    data_type: string
    semantic_type: legacy_fee_waiver_amount
    business_meaning: Legacy/string waiver amount; cast before numeric use.
    metric_role: metric_amount_caveat
    join_role: ''
    filter_role: ''
    source_caveats: 
      - Cast from string before numeric use.
    evidence_refs: 
      - evidence.flipkart.cashback
    confidence: high
    review_status: accepted
```


```yaml
candidate_card:
  card_type: column
  card_id: column.cashback.invoice_date
  name: table.flipkart.cashback.invoice_date
  fields:
    table_id: table.flipkart.cashback
    column_name: invoice_date
    data_type: string
    semantic_type: invoice_date_string
    business_meaning: Invoice date stored as string format; parse before native date operations.
    metric_role: ''
    join_role: ''
    filter_role: ''
    source_caveats:
    - DOCX Date Columns declares invoice_date as string.
    evidence_refs:
    - evidence.flipkart.cashback_schema
    confidence: high
    review_status: accepted
```


```yaml
candidate_card:
  card_type: column
  card_id: column.cashback.created_date
  name: table.flipkart.cashback.created_date
  fields:
    table_id: table.flipkart.cashback
    column_name: created_date
    data_type: timestamp
    semantic_type: cashback_event_timestamp
    business_meaning: Cashback event timestamp and documented primary date filter.
    metric_role: ''
    join_role: ''
    filter_role: ''
    source_caveats: []
    evidence_refs:
    - evidence.flipkart.cashback_schema
    confidence: high
    review_status: accepted
```

```yaml
candidate_card:
  card_type: column
  card_id: column.cashback.is_shopsy_order_
  name: table.flipkart.cashback.is_shopsy_order_
  fields:
    table_id: table.flipkart.cashback
    column_name: is_shopsy_order_
    data_type: string
    semantic_type: shopsy_flag
    business_meaning: String sub-platform flag.
    metric_role: ''
    join_role: ''
    filter_role: filter
    source_caveats: []
    evidence_refs: 
      - evidence.flipkart.cashback
    confidence: high
    review_status: accepted
```


```yaml
candidate_card:
  card_type: column
  card_id: column.cashback.seller_gstin
  name: table.flipkart.cashback.seller_gstin
  fields:
    table_id: table.flipkart.cashback
    column_name: seller_gstin
    data_type: string
    semantic_type: seller_gstin
    business_meaning: Seller GSTIN field; marketplace column only, not account binding.
    metric_role: ''
    join_role: ''
    filter_role: ''
    source_caveats: []
    evidence_refs: 
      - evidence.flipkart.cashback
    confidence: high
    review_status: accepted
```

```yaml
candidate_card:
  card_type: column
  card_id: column.cashback.is_active
  name: table.flipkart.cashback.is_active
  fields:
    table_id: table.flipkart.cashback
    column_name: is_active
    data_type: boolean
    semantic_type: active_row_flag
    business_meaning: Mandatory active-row filter.
    metric_role: ''
    join_role: ''
    filter_role: filter
    source_caveats: []
    evidence_refs: 
      - evidence.flipkart.cashback
    confidence: high
    review_status: accepted
```

```yaml
candidate_card:
  card_type: column
  card_id: column.cashback.group_level_id
  name: table.flipkart.cashback.group_level_id
  fields:
    table_id: table.flipkart.cashback
    column_name: group_level_id
    data_type: integer
    semantic_type: scope_column_only
    business_meaning: Table-level scope column, not account binding.
    metric_role: ''
    join_role: ''
    filter_role: filter_caveat
    source_caveats:
    - Scope column only; never emit tenant/group/account-binding cards from this field.
    - Documented scope value only; do not create tenant/group/account-binding cards.
    evidence_refs:
    - evidence.flipkart.cashback_schema
    - evidence.flipkart.scope_caveats
    confidence: high
    review_status: accepted
    documented_scope_values:
    - 22
```

```yaml
candidate_card:
  card_type: column
  card_id: column.cashback.group_id
  name: table.flipkart.cashback.group_id
  fields:
    table_id: table.flipkart.cashback
    column_name: group_id
    data_type: integer
    semantic_type: scope_column_only
    business_meaning: Table-level scope column, not group card.
    metric_role: ''
    join_role: ''
    filter_role: filter_caveat
    source_caveats: 
      - Scope column only; never emit tenant/group/account-binding cards from this field.
    evidence_refs: 
      - evidence.flipkart.cashback
    confidence: high
    review_status: accepted
```

```yaml
candidate_card:
  card_type: column
  card_id: column.settlement.my_share_settled_amount
  name: table.flipkart.settlement.my_share_settled_amount
  fields:
    table_id: table.flipkart.settlement
    column_name: my_share_settled_amount
    data_type: decimal
    semantic_type: seller_share_adjustment_component
    business_meaning: Seller's share adjustment component included in settlement waterfall.
    metric_role: metric_amount
    join_role: ''
    filter_role: ''
    source_caveats: []
    evidence_refs:
    - evidence.flipkart.settlement_logic
    confidence: high
    review_status: accepted
```

```yaml
candidate_card:
  card_type: column
  card_id: column.settlement.addon_settled_amount
  name: table.flipkart.settlement.addon_settled_amount
  fields:
    table_id: table.flipkart.settlement
    column_name: addon_settled_amount
    data_type: decimal
    semantic_type: addon_settlement_component
    business_meaning: Add-on service settlement component included in settlement waterfall.
    metric_role: metric_amount
    join_role: ''
    filter_role: ''
    source_caveats: []
    evidence_refs:
    - evidence.flipkart.settlement_logic
    confidence: high
    review_status: accepted
```

```yaml
candidate_card:
  card_type: column
  card_id: column.settlement.taxes_settled_amount
  name: table.flipkart.settlement.taxes_settled_amount
  fields:
    table_id: table.flipkart.settlement
    column_name: taxes_settled_amount
    data_type: decimal
    semantic_type: tax_adjustment_settlement_component
    business_meaning: Tax adjustment component included in settlement waterfall.
    metric_role: metric_amount
    join_role: ''
    filter_role: ''
    source_caveats: []
    evidence_refs:
    - evidence.flipkart.settlement_logic
    confidence: high
    review_status: accepted
```

```yaml
candidate_card:
  card_type: column
  card_id: column.settlement.total_tax
  name: table.flipkart.settlement.total_tax
  fields:
    table_id: table.flipkart.settlement
    column_name: total_tax
    data_type: decimal
    semantic_type: settlement_tax_component
    business_meaning: Total tax component on the settlement row.
    metric_role: metric_amount
    join_role: ''
    filter_role: ''
    source_caveats: []
    evidence_refs:
    - evidence.flipkart.settlement_logic
    confidence: high
    review_status: accepted
```

```yaml
candidate_card:
  card_type: column
  card_id: column.commission.metadata
  name: table.flipkart.commission.metadata
  fields:
    table_id: table.flipkart.commission
    column_name: metadata
    data_type: string
    semantic_type: commission_invoice_metadata
    business_meaning: Metadata value documented as 'commission invoice' for active fee invoice rows.
    metric_role: ''
    join_role: ''
    filter_role: filter/status
    source_caveats: []
    evidence_refs:
    - evidence.flipkart.commission_schema
    confidence: high
    review_status: accepted
```

```yaml
candidate_card:
  card_type: column
  card_id: column.commission.transaction_type
  name: table.flipkart.commission.transaction_type
  fields:
    table_id: table.flipkart.commission
    column_name: transaction_type
    data_type: string
    semantic_type: commission_transaction_type
    business_meaning: Transaction type documented as 'Order Item' for active commission invoice rows.
    metric_role: ''
    join_role: ''
    filter_role: filter/status
    source_caveats: []
    evidence_refs:
    - evidence.flipkart.commission_schema
    confidence: high
    review_status: accepted
```


### 5.6 Relationship Cards

```yaml
candidate_card:
  card_type: relationship
  card_id: relationship.flipkart.oms_settlement
  name: Flipkart oms_settlement
  fields:
    left_table: table.flipkart.oms
    right_table: table.flipkart.settlement
    relationship_type: one_to_many_or_many_to_many_review
    join_keys: 
      - order_id + item_id
    join_grain: order_id + item_id
    normalization: source keys preserved
    many_side: review required
    pre_aggregation_required: false
    safe_join_conditions: 
      - filter is_active = true on both sides
      - pre-aggregate many-side detail tables before amount comparison
    unsafe_join_conditions: 
      - joining raw commission/cashback rows directly to settlement and summing settlement amounts
      - using group_level_id as a cross-table join key
    notes: Use exact order_id/item_id when OMS is verified; review OMS schema.
    evidence_refs: 
      - evidence.flipkart.relationships
    confidence: medium
    review_status: review_required
```

```yaml
candidate_card:
  card_type: relationship
  card_id: relationship.flipkart.commission_settlement
  name: Flipkart commission_settlement
  fields:
    left_table: table.flipkart.commission
    right_table: table.flipkart.settlement
    relationship_type: many_to_one_after_aggregation
    join_keys: 
      - commission.order_id = REPLACE(settlement.order_id, 'OD', '') AND item_id
    join_grain: order_id + item_id
    normalization: OD prefix removal is required when joining commission order_id to other tables.
    many_side: commission/cashback detail side
    pre_aggregation_required: true
    safe_join_conditions: 
      - filter is_active = true on both sides
      - pre-aggregate many-side detail tables before amount comparison
    unsafe_join_conditions: 
      - joining raw commission/cashback rows directly to settlement and summing settlement amounts
      - using group_level_id as a cross-table join key
    notes: Aggregate commission by order_id,item_id before joining.
    evidence_refs: 
      - evidence.flipkart.relationships
    confidence: high
    review_status: accepted
```

```yaml
candidate_card:
  card_type: relationship
  card_id: relationship.flipkart.commission_oms
  name: Flipkart commission_oms
  fields:
    left_table: table.flipkart.commission
    right_table: table.flipkart.oms
    relationship_type: many_to_one_after_aggregation
    join_keys: 
      - commission.order_id = REPLACE(oms.order_id, 'OD', '') AND item_id
    join_grain: order_id + item_id
    normalization: OD prefix removal is required when joining commission order_id to other tables.
    many_side: commission/cashback detail side
    pre_aggregation_required: true
    safe_join_conditions: 
      - filter is_active = true on both sides
      - pre-aggregate many-side detail tables before amount comparison
    unsafe_join_conditions: 
      - joining raw commission/cashback rows directly to settlement and summing settlement amounts
      - using group_level_id as a cross-table join key
    notes: Aggregate commission first; OMS schema is review-required.
    evidence_refs: 
      - evidence.flipkart.relationships
    confidence: medium
    review_status: review_required
```

```yaml
candidate_card:
  card_type: relationship
  card_id: relationship.flipkart.cashback_settlement
  name: Flipkart cashback_settlement
  fields:
    left_table: table.flipkart.cashback
    right_table: table.flipkart.settlement
    relationship_type: many_to_one_after_aggregation
    join_keys: 
      - cashback.order_id = settlement.order_id AND item_id
    join_grain: order_id + item_id
    normalization: source keys preserved
    many_side: commission/cashback detail side
    pre_aggregation_required: true
    safe_join_conditions: 
      - filter is_active = true on both sides
      - pre-aggregate many-side detail tables before amount comparison
    unsafe_join_conditions: 
      - joining raw commission/cashback rows directly to settlement and summing settlement amounts
      - using group_level_id as a cross-table join key
    notes: Aggregate cashback by order_id,item_id before comparing to settlement offer fields.
    evidence_refs: 
      - evidence.flipkart.relationships
    confidence: high
    review_status: accepted
```

```yaml
candidate_card:
  card_type: relationship
  card_id: relationship.flipkart.cashback_commission
  name: Flipkart cashback_commission
  fields:
    left_table: table.flipkart.cashback
    right_table: table.flipkart.commission
    relationship_type: many_to_many_review
    join_keys: 
      - REPLACE(cashback.order_id, 'OD', '') = commission.order_id AND item_id
    join_grain: order_id + item_id
    normalization: OD prefix removal is required when joining commission order_id to other tables.
    many_side: commission/cashback detail side
    pre_aggregation_required: true
    safe_join_conditions: 
      - filter is_active = true on both sides
      - pre-aggregate many-side detail tables before amount comparison
    unsafe_join_conditions: 
      - joining raw commission/cashback rows directly to settlement and summing settlement amounts
      - using group_level_id as a cross-table join key
    notes: Use only for diagnostic analysis; aggregate both sides if comparing amounts.
    evidence_refs: 
      - evidence.flipkart.relationships
    confidence: high
    review_status: accepted
```

```yaml
candidate_card:
  card_type: relationship
  card_id: relationship.flipkart.cashback_oms
  name: Flipkart cashback_oms
  fields:
    left_table: table.flipkart.cashback
    right_table: table.flipkart.oms
    relationship_type: many_to_one_after_aggregation
    join_keys: 
      - cashback.order_id = oms.order_id AND item_id
    join_grain: order_id + item_id
    normalization: source keys preserved
    many_side: commission/cashback detail side
    pre_aggregation_required: true
    safe_join_conditions: 
      - filter is_active = true on both sides
      - pre-aggregate many-side detail tables before amount comparison
    unsafe_join_conditions: 
      - joining raw commission/cashback rows directly to settlement and summing settlement amounts
      - using group_level_id as a cross-table join key
    notes: Aggregate cashback before joining; OMS schema is review-required.
    evidence_refs: 
      - evidence.flipkart.relationships
    confidence: medium
    review_status: review_required
```

### 5.7 Value Profile Cards

```yaml
candidate_card:
  card_type: value_profile
  card_id: value_profile.flipkart.commission.description
  name: Flipkart commission.description
  fields:
    table_id: table.flipkart.commission
    column_name: description
    known_values:
    - Fixed Fee
    - Commission
    - Shipping Fee
    - Reverse Shipping Fee
    - Collection Fee
    value_meanings: description/fee_name identifies the specific Flipkart fee invoice line; active rows usually generate 2-5 fee rows per order
      item.
    null_semantics: preserve nulls where observed
    normalization: case/source-value preserving unless query pattern says otherwise
    evidence_refs:
    - evidence.flipkart.commission_schema
    - evidence.flipkart.fee_structure
    confidence: high
    review_status: accepted
```

```yaml
candidate_card:
  card_type: value_profile
  card_id: value_profile.flipkart.cashback.transaction_type
  name: Flipkart cashback.transaction_type
  fields:
    table_id: table.flipkart.cashback
    column_name: transaction_type
    known_values:
    - forward
    - reverse
    - forward cancel
    value_meanings: Forward credit notes are positive; reverse and forward-cancel debit notes reverse cashback/promotional credits.
    null_semantics: preserve nulls where observed
    normalization: case/source-value preserving unless query pattern says otherwise
    evidence_refs:
    - evidence.flipkart.cashback_schema
    confidence: high
    review_status: accepted
```

```yaml
candidate_card:
  card_type: value_profile
  card_id: value_profile.flipkart.cashback.document_type
  name: Flipkart cashback.document_type
  fields:
    table_id: table.flipkart.cashback
    column_name: document_type
    known_values:
    - Credit Note
    - Debit Note
    - 'null'
    value_meanings: Credit Note generally represents sale cashback credit; Debit Note reverses cashback on return/cancellation; null is explicitly
      observed.
    null_semantics: preserve nulls where observed
    normalization: case/source-value preserving unless query pattern says otherwise
    evidence_refs:
    - evidence.flipkart.cashback_schema
    confidence: high
    review_status: accepted
```

```yaml
candidate_card:
  card_type: value_profile
  card_id: value_profile.flipkart.cashback.document_sub_type
  name: Flipkart cashback.document_sub_type
  fields:
    table_id: table.flipkart.cashback
    column_name: document_sub_type
    known_values:
    - Sale
    - Return
    - Cancellation
    - 'null'
    value_meanings: Sale, Return, and Cancellation classify credit/debit note business effect; null is explicitly observed.
    null_semantics: preserve nulls where observed
    normalization: case/source-value preserving unless query pattern says otherwise
    evidence_refs:
    - evidence.flipkart.cashback_schema
    confidence: high
    review_status: accepted
```

```yaml
candidate_card:
  card_type: value_profile
  card_id: value_profile.flipkart.cashback.is_shopsy_order
  name: Flipkart cashback.is_shopsy_order
  fields:
    table_id: table.flipkart.cashback
    column_name: is_shopsy_order_
    known_values:
    - 'true'
    - 'false'
    value_meanings: String-valued Shopsy flag; filter with is_shopsy_order_ = 'true', not boolean true.
    null_semantics: preserve nulls where observed
    normalization: case/source-value preserving unless query pattern says otherwise
    evidence_refs:
    - evidence.flipkart.shopsy
    - evidence.flipkart.pitfalls
    confidence: high
    review_status: accepted
```

```yaml
candidate_card:
  card_type: value_profile
  card_id: value_profile.flipkart.oms.fulfilment_type
  name: Flipkart oms.fulfilment_type
  fields:
    table_id: table.flipkart.oms
    column_name: fulfilment_type
    known_values:
    - FBF
    - NON_FBF
    value_meanings: OMS fulfilment naming; FBF maps to flipkart_fulfilment, NON_FBF maps to seller_easy_ship in settlement.
    null_semantics: preserve nulls where observed
    normalization: case/source-value preserving unless query pattern says otherwise
    evidence_refs:
    - evidence.flipkart.fulfilment
    - evidence.flipkart.pitfalls
    confidence: high
    review_status: accepted
```

```yaml
candidate_card:
  card_type: value_profile
  card_id: value_profile.flipkart.settlement.fulfilment_type
  name: Flipkart settlement.fulfilment_type
  fields:
    table_id: table.flipkart.settlement
    column_name: fulfilment_type
    known_values:
    - flipkart_fulfilment
    - seller_easy_ship
    value_meanings: Settlement fulfilment naming; map semantically to FBF/NON_FBF where needed.
    null_semantics: preserve nulls where observed
    normalization: case/source-value preserving unless query pattern says otherwise
    evidence_refs:
    - evidence.flipkart.fulfilment
    - evidence.flipkart.settlement_logic
    confidence: high
    review_status: accepted
```

```yaml
candidate_card:
  card_type: value_profile
  card_id: value_profile.flipkart.settlement.neft_type
  name: Flipkart settlement.neft_type
  fields:
    table_id: table.flipkart.settlement
    column_name: neft_type
    known_values:
    - Prepaid
    - Postpaid
    value_meanings: Payment method / settlement cycle classification; source SQL groups settlement by fulfilment_type and neft_type.
    null_semantics: preserve nulls where observed
    normalization: case/source-value preserving unless query pattern says otherwise
    evidence_refs:
    - evidence.flipkart.settlement_logic
    - evidence.flipkart.payment_process
    confidence: high
    review_status: accepted
```

```yaml
candidate_card:
  card_type: value_profile
  card_id: value_profile.flipkart.settlement.return_type
  name: Flipkart settlement.return_type
  fields:
    table_id: table.flipkart.settlement
    column_name: return_type
    known_values:
    - return
    - rto
    - cancel
    - source-specific
    value_meanings: Return/reverse type classification; preserve source values and verify taxonomy before hard return-rate implementation.
    null_semantics: preserve nulls where observed
    normalization: case/source-value preserving unless query pattern says otherwise
    evidence_refs:
    - evidence.flipkart.settlement_logic
    confidence: high
    review_status: accepted
```

```yaml
candidate_card:
  card_type: value_profile
  card_id: value_profile.flipkart.settlement.is_active
  name: Flipkart settlement.is_active
  fields:
    table_id: table.flipkart.settlement
    column_name: is_active
    known_values: 
      - true
      - false
    value_meanings: Active row flag; deterministic extraction should include active=true filters for analytics.
    null_semantics: preserve nulls where observed
    normalization: case/source-value preserving unless query pattern says otherwise
    evidence_refs: 
      - evidence.flipkart.cashback
      - evidence.flipkart.fulfilment
      - evidence.flipkart.scope_caveats
    confidence: high
    review_status: accepted
```

```yaml
candidate_card:
  card_type: value_profile
  card_id: value_profile.flipkart.group_level_id
  name: Flipkart group_level_id
  fields:
    table_id: multiple
    column_name: group_level_id
    known_values:
    - 'OMS: 22/26/65787/65853'
    - 'Settlement: 66388'
    - 'Commission/Cashback: 22'
    value_meanings: Documented scope identifiers vary by table; use as table-specific scope/filter metadata, never as cross-table join keys or
      account-binding cards.
    null_semantics: preserve nulls where observed
    normalization: case/source-value preserving unless query pattern says otherwise
    evidence_refs:
    - evidence.flipkart.scope_caveats
    - evidence.flipkart.pitfalls
    confidence: high
    review_status: accepted
```

### 5.8 Metric Cards with Colloquial Names

```yaml
candidate_card:
  card_type: metric
  card_id: metric.gross_merchandise_value
  name: Gross Merchandise Value
  fields:
    canonical_name: gross_merchandise_value
    colloquial_names: 
      - GMV
      - gross sales
      - gross revenue
      - topline
      - order value
    metric_family: sales
    business_question: SUM forward order amount or sale-settled amount fallback
    default_grain: order item or settlement line depending implementation
    default_time_basis: settlement_date for settlement metrics; created/order date for order metrics
    positive_direction: higher_is_better except fees/taxes/returns/cancellations
    included_components: 
      - marketplace-owned Flipkart fields only
    excluded_components: 
      - COGS
      - bank deposits
      - external logistics charges
      - ERP/accounting adjustments
    evidence_refs: 
      - evidence.flipkart.query_patterns
    confidence: high
    review_status: accepted
```

```yaml
candidate_card:
  card_type: metric
  card_id: metric.net_revenue
  name: Net Revenue
  fields:
    canonical_name: net_revenue
    colloquial_names: 
      - net sales
      - net revenue
      - net order value
    metric_family: sales
    business_question: Order value after reverse/cancel adjustments where source permits
    default_grain: order item or settlement line depending implementation
    default_time_basis: settlement_date for settlement metrics; created/order date for order metrics
    positive_direction: higher_is_better except fees/taxes/returns/cancellations
    included_components: 
      - marketplace-owned Flipkart fields only
    excluded_components: 
      - COGS
      - bank deposits
      - external logistics charges
      - ERP/accounting adjustments
    evidence_refs: 
      - evidence.flipkart.query_patterns
    confidence: high
    review_status: accepted
```

```yaml
candidate_card:
  card_type: metric
  card_id: metric.order_count
  name: Order Count
  fields:
    canonical_name: order_count
    colloquial_names: 
      - orders
      - number of orders
      - order volume
    metric_family: volume
    business_question: COUNT DISTINCT order_id or order_id/item_id depending grain
    default_grain: order item or settlement line depending implementation
    default_time_basis: settlement_date for settlement metrics; created/order date for order metrics
    positive_direction: higher_is_better except fees/taxes/returns/cancellations
    included_components: 
      - marketplace-owned Flipkart fields only
    excluded_components: 
      - COGS
      - bank deposits
      - external logistics charges
      - ERP/accounting adjustments
    evidence_refs: 
      - evidence.flipkart.query_patterns
    confidence: high
    review_status: accepted
```

```yaml
candidate_card:
  card_type: metric
  card_id: metric.average_order_value
  name: Average Order Value
  fields:
    canonical_name: average_order_value
    colloquial_names: 
      - AOV
      - average basket value
    metric_family: sales
    business_question: GMV divided by order count
    default_grain: order item or settlement line depending implementation
    default_time_basis: settlement_date for settlement metrics; created/order date for order metrics
    positive_direction: higher_is_better except fees/taxes/returns/cancellations
    included_components: 
      - marketplace-owned Flipkart fields only
    excluded_components: 
      - COGS
      - bank deposits
      - external logistics charges
      - ERP/accounting adjustments
    evidence_refs: 
      - evidence.flipkart.query_patterns
    confidence: high
    review_status: accepted
```

```yaml
candidate_card:
  card_type: metric
  card_id: metric.net_settlement
  name: Net Settlement
  fields:
    canonical_name: net_settlement
    colloquial_names: 
      - settlement amount
      - payout
      - net payout
      - amount received from Flipkart
    metric_family: settlement
    business_question: SUM settled_amount
    default_grain: order item or settlement line depending implementation
    default_time_basis: settlement_date for settlement metrics; created/order date for order metrics
    positive_direction: higher_is_better except fees/taxes/returns/cancellations
    included_components: 
      - marketplace-owned Flipkart fields only
    excluded_components: 
      - COGS
      - bank deposits
      - external logistics charges
      - ERP/accounting adjustments
    evidence_refs: 
      - evidence.flipkart.query_patterns
    confidence: high
    review_status: accepted
```

```yaml
candidate_card:
  card_type: metric
  card_id: metric.realization_rate
  name: Realization Rate
  fields:
    canonical_name: realization_rate
    colloquial_names:
    - seller realization
    - realization
    - payout percent
    - settlement percentage
    metric_family: ratio
    business_question: net settlement divided by sale settled amount
    default_grain: order item or settlement line depending implementation
    default_time_basis: settlement_date for settlement metrics; created/order date for order metrics
    positive_direction: higher_is_better except fees/taxes/returns/cancellations
    included_components:
    - marketplace-owned Flipkart fields only
    excluded_components:
    - COGS
    - bank deposits
    - external logistics charges
    - ERP/accounting adjustments
    evidence_refs:
    - evidence.flipkart.query_patterns
    - evidence.flipkart.metrics_benchmarks
    confidence: high
    review_status: accepted
    benchmarks:
      flipkart_india_healthy: 70-80 percent
      interpretation: Outside range warrants investigation into return volume, fee burden, ad/promotion spend, or settlement component anomalies;
        guidance only, not a hard validation threshold.
      source: docx Key Metrics for Seller Analytics > Profitability Metrics
```

```yaml
candidate_card:
  card_type: metric
  card_id: metric.effective_fee_rate
  name: Effective Fee Rate
  fields:
    canonical_name: effective_fee_rate
    colloquial_names: 
      - fee burden
      - take rate
      - platform fee rate
    metric_family: ratio
    business_question: ABS marketplace fee divided by sale amount
    default_grain: order item or settlement line depending implementation
    default_time_basis: settlement_date for settlement metrics; created/order date for order metrics
    positive_direction: higher_is_better except fees/taxes/returns/cancellations
    included_components: 
      - marketplace-owned Flipkart fields only
    excluded_components: 
      - COGS
      - bank deposits
      - external logistics charges
      - ERP/accounting adjustments
    evidence_refs: 
      - evidence.flipkart.query_patterns
    confidence: high
    review_status: accepted
```

```yaml
candidate_card:
  card_type: metric
  card_id: metric.marketplace_fee_total
  name: Marketplace Fee Total
  fields:
    canonical_name: marketplace_fee_total
    colloquial_names: 
      - MP fee
      - platform fee
      - Flipkart deductions
      - marketplace deductions
    metric_family: fee
    business_question: SUM mp_fee or detail fee sums
    default_grain: order item or settlement line depending implementation
    default_time_basis: settlement_date for settlement metrics; created/order date for order metrics
    positive_direction: higher_is_better except fees/taxes/returns/cancellations
    included_components: 
      - marketplace-owned Flipkart fields only
    excluded_components: 
      - COGS
      - bank deposits
      - external logistics charges
      - ERP/accounting adjustments
    evidence_refs: 
      - evidence.flipkart.query_patterns
    confidence: high
    review_status: accepted
```

```yaml
candidate_card:
  card_type: metric
  card_id: metric.commission_fee
  name: Commission Fee
  fields:
    canonical_name: commission_fee
    colloquial_names: 
      - commission
      - commission charged
    metric_family: fee
    business_question: Commission fee lines
    default_grain: order item or settlement line depending implementation
    default_time_basis: settlement_date for settlement metrics; created/order date for order metrics
    positive_direction: higher_is_better except fees/taxes/returns/cancellations
    included_components: 
      - marketplace-owned Flipkart fields only
    excluded_components: 
      - COGS
      - bank deposits
      - external logistics charges
      - ERP/accounting adjustments
    evidence_refs: 
      - evidence.flipkart.query_patterns
    confidence: high
    review_status: accepted
```

```yaml
candidate_card:
  card_type: metric
  card_id: metric.fixed_fee
  name: Fixed Fee
  fields:
    canonical_name: fixed_fee
    colloquial_names: 
      - fixed fee
      - closing fee
    metric_family: fee
    business_question: Fixed Fee lines
    default_grain: order item or settlement line depending implementation
    default_time_basis: settlement_date for settlement metrics; created/order date for order metrics
    positive_direction: higher_is_better except fees/taxes/returns/cancellations
    included_components: 
      - marketplace-owned Flipkart fields only
    excluded_components: 
      - COGS
      - bank deposits
      - external logistics charges
      - ERP/accounting adjustments
    evidence_refs: 
      - evidence.flipkart.query_patterns
    confidence: high
    review_status: accepted
```

```yaml
candidate_card:
  card_type: metric
  card_id: metric.shipping_fee
  name: Shipping Fee
  fields:
    canonical_name: shipping_fee
    colloquial_names: 
      - shipping fee
      - freight fee
      - delivery fee charged by Flipkart
    metric_family: fee
    business_question: Shipping Fee lines or settlement shipping_fee
    default_grain: order item or settlement line depending implementation
    default_time_basis: settlement_date for settlement metrics; created/order date for order metrics
    positive_direction: higher_is_better except fees/taxes/returns/cancellations
    included_components: 
      - marketplace-owned Flipkart fields only
    excluded_components: 
      - COGS
      - bank deposits
      - external logistics charges
      - ERP/accounting adjustments
    evidence_refs: 
      - evidence.flipkart.query_patterns
    confidence: high
    review_status: accepted
```

```yaml
candidate_card:
  card_type: metric
  card_id: metric.reverse_shipping_fee
  name: Reverse Shipping Fee
  fields:
    canonical_name: reverse_shipping_fee
    colloquial_names: 
      - reverse shipping fee
      - return shipping fee
    metric_family: fee
    business_question: Reverse Shipping Fee lines or settlement component
    default_grain: order item or settlement line depending implementation
    default_time_basis: settlement_date for settlement metrics; created/order date for order metrics
    positive_direction: higher_is_better except fees/taxes/returns/cancellations
    included_components: 
      - marketplace-owned Flipkart fields only
    excluded_components: 
      - COGS
      - bank deposits
      - external logistics charges
      - ERP/accounting adjustments
    evidence_refs: 
      - evidence.flipkart.query_patterns
    confidence: high
    review_status: accepted
```

```yaml
candidate_card:
  card_type: metric
  card_id: metric.collection_fee
  name: Collection Fee
  fields:
    canonical_name: collection_fee
    colloquial_names: 
      - collection fee
      - COD fee
      - payment collection fee
    metric_family: fee
    business_question: Collection Fee lines
    default_grain: order item or settlement line depending implementation
    default_time_basis: settlement_date for settlement metrics; created/order date for order metrics
    positive_direction: higher_is_better except fees/taxes/returns/cancellations
    included_components: 
      - marketplace-owned Flipkart fields only
    excluded_components: 
      - COGS
      - bank deposits
      - external logistics charges
      - ERP/accounting adjustments
    evidence_refs: 
      - evidence.flipkart.query_patterns
    confidence: high
    review_status: accepted
```

```yaml
candidate_card:
  card_type: metric
  card_id: metric.net_cashback
  name: Net Cashback
  fields:
    canonical_name: net_cashback
    colloquial_names: 
      - cashback
      - promotion subsidy
      - offer credit
      - promo amount
    metric_family: promotion
    business_question: Signed SUM cashback.charged_amount
    default_grain: order item or settlement line depending implementation
    default_time_basis: settlement_date for settlement metrics; created/order date for order metrics
    positive_direction: higher_is_better except fees/taxes/returns/cancellations
    included_components: 
      - marketplace-owned Flipkart fields only
    excluded_components: 
      - COGS
      - bank deposits
      - external logistics charges
      - ERP/accounting adjustments
    evidence_refs: 
      - evidence.flipkart.query_patterns
    confidence: high
    review_status: accepted
```

```yaml
candidate_card:
  card_type: metric
  card_id: metric.cashback_rate
  name: Cashback Rate
  fields:
    canonical_name: cashback_rate
    colloquial_names: 
      - cashback percentage
      - offer rate
      - promo rate
    metric_family: ratio
    business_question: cashback amount divided by order value
    default_grain: order item or settlement line depending implementation
    default_time_basis: settlement_date for settlement metrics; created/order date for order metrics
    positive_direction: higher_is_better except fees/taxes/returns/cancellations
    included_components: 
      - marketplace-owned Flipkart fields only
    excluded_components: 
      - COGS
      - bank deposits
      - external logistics charges
      - ERP/accounting adjustments
    evidence_refs: 
      - evidence.flipkart.query_patterns
    confidence: high
    review_status: accepted
```

```yaml
candidate_card:
  card_type: metric
  card_id: metric.return_rate
  name: Return Rate
  fields:
    canonical_name: return_rate
    colloquial_names:
    - return rate
    - reverse rate
    metric_family: ratio
    business_question: reverse/return orders divided by forward orders
    default_grain: order item or settlement line depending implementation
    default_time_basis: settlement_date for settlement metrics; created/order date for order metrics
    positive_direction: higher_is_better except fees/taxes/returns/cancellations
    included_components:
    - marketplace-owned Flipkart fields only
    excluded_components:
    - COGS
    - bank deposits
    - external logistics charges
    - ERP/accounting adjustments
    evidence_refs:
    - evidence.flipkart.query_patterns
    - evidence.flipkart.metrics_benchmarks
    confidence: high
    review_status: accepted
    benchmarks:
      fashion_typical: 20-30 percent
      electronics_typical: 5-10 percent
      interpretation: Category-context guidance only; do not hard-fail without category/account/period context.
      source: docx Key Metrics for Seller Analytics > Operational Metrics
```

```yaml
candidate_card:
  card_type: metric
  card_id: metric.cancellation_rate
  name: Cancellation Rate
  fields:
    canonical_name: cancellation_rate
    colloquial_names: 
      - cancel rate
      - cancellation rate
    metric_family: ratio
    business_question: cancelled orders divided by forward orders
    default_grain: order item or settlement line depending implementation
    default_time_basis: settlement_date for settlement metrics; created/order date for order metrics
    positive_direction: higher_is_better except fees/taxes/returns/cancellations
    included_components: 
      - marketplace-owned Flipkart fields only
    excluded_components: 
      - COGS
      - bank deposits
      - external logistics charges
      - ERP/accounting adjustments
    evidence_refs: 
      - evidence.flipkart.query_patterns
    confidence: high
    review_status: accepted
```

```yaml
candidate_card:
  card_type: metric
  card_id: metric.settlement_cycle_days
  name: Settlement Cycle Days
  fields:
    canonical_name: settlement_cycle_days
    colloquial_names: 
      - payout lag
      - settlement lag
      - cash cycle
    metric_family: cycle_time
    business_question: Date difference between order/created/dispatch and settlement date
    default_grain: order item or settlement line depending implementation
    default_time_basis: settlement_date for settlement metrics; created/order date for order metrics
    positive_direction: higher_is_better except fees/taxes/returns/cancellations
    included_components: 
      - marketplace-owned Flipkart fields only
    excluded_components: 
      - COGS
      - bank deposits
      - external logistics charges
      - ERP/accounting adjustments
    evidence_refs: 
      - evidence.flipkart.query_patterns
    confidence: high
    review_status: accepted
```

```yaml
candidate_card:
  card_type: metric
  card_id: metric.tcs_deducted
  name: Tcs Deducted
  fields:
    canonical_name: tcs_deducted
    colloquial_names: 
      - TCS
      - tax collected at source
    metric_family: tax_deduction
    business_question: SUM total_tcs_amount
    default_grain: order item or settlement line depending implementation
    default_time_basis: settlement_date for settlement metrics; created/order date for order metrics
    positive_direction: higher_is_better except fees/taxes/returns/cancellations
    included_components: 
      - marketplace-owned Flipkart fields only
    excluded_components: 
      - COGS
      - bank deposits
      - external logistics charges
      - ERP/accounting adjustments
    evidence_refs: 
      - evidence.flipkart.query_patterns
    confidence: high
    review_status: accepted
```

```yaml
candidate_card:
  card_type: metric
  card_id: metric.tds_deducted
  name: Tds Deducted
  fields:
    canonical_name: tds_deducted
    colloquial_names: 
      - TDS
      - tax deducted at source
    metric_family: tax_deduction
    business_question: SUM total_tds_amount
    default_grain: order item or settlement line depending implementation
    default_time_basis: settlement_date for settlement metrics; created/order date for order metrics
    positive_direction: higher_is_better except fees/taxes/returns/cancellations
    included_components: 
      - marketplace-owned Flipkart fields only
    excluded_components: 
      - COGS
      - bank deposits
      - external logistics charges
      - ERP/accounting adjustments
    evidence_refs: 
      - evidence.flipkart.query_patterns
    confidence: high
    review_status: accepted
```

```yaml
candidate_card:
  card_type: metric
  card_id: metric.gst_on_marketplace_fees
  name: Gst On Marketplace Fees
  fields:
    canonical_name: gst_on_marketplace_fees
    colloquial_names: 
      - GST on fees
      - GST charged by Flipkart
    metric_family: tax_on_fee
    business_question: SUM gst_on_mp_fees or fee total_tax
    default_grain: order item or settlement line depending implementation
    default_time_basis: settlement_date for settlement metrics; created/order date for order metrics
    positive_direction: higher_is_better except fees/taxes/returns/cancellations
    included_components: 
      - marketplace-owned Flipkart fields only
    excluded_components: 
      - COGS
      - bank deposits
      - external logistics charges
      - ERP/accounting adjustments
    evidence_refs: 
      - evidence.flipkart.query_patterns
    confidence: high
    review_status: accepted
```

```yaml
candidate_card:
  card_type: metric
  card_id: metric.protection_fund_settlement
  name: Protection Fund Settlement
  fields:
    canonical_name: protection_fund_settlement
    colloquial_names: 
      - protection fund
      - protection fund settled amount
    metric_family: adjustment
    business_question: SUM protection_fund_settled_amount
    default_grain: order item or settlement line depending implementation
    default_time_basis: settlement_date for settlement metrics; created/order date for order metrics
    positive_direction: higher_is_better except fees/taxes/returns/cancellations
    included_components: 
      - marketplace-owned Flipkart fields only
    excluded_components: 
      - COGS
      - bank deposits
      - external logistics charges
      - ERP/accounting adjustments
    evidence_refs: 
      - evidence.flipkart.query_patterns
    confidence: high
    review_status: accepted
```

### 5.9 Flipkart-Specific Metric Implementation Cards

```yaml
candidate_card:
  card_type: metric_implementation
  card_id: metric_implementation.flipkart.gmv.oms
  name: Flipkart gmv.oms
  fields:
    metric_id: metric.gross_merchandise_value
    platform_context: platform_context.flipkart.in
    source_table: table.flipkart.oms
    source_columns:
    - charged_amount
    formula: SUM(charged_amount)
    filters:
    - is_active = true AND transaction_type = 'forward'
    grain: order_id/item_id
    time_basis: created_date
    sign_handling: preserve source sign unless formula explicitly uses ABS for reporting ratio
    aggregation_rule: aggregate at declared grain before joins
    join_dependencies:
    - see relationship cards when cross-table
    metric_pattern: platform-specific implementation of generic colloquial metric
    implementation_caveats:
    - OMS schema partial/inconsistent in DOCX; implementation is review-required until actual OMS schema is verified.
    sql_pattern_ref: sql.flipkart.oms_gmv_review
    evidence_refs:
    - evidence.flipkart.metrics_benchmarks
    - evidence.flipkart.oms
    - evidence.flipkart.reconciliation_framework
    confidence: medium
    review_status: review_required
```

```yaml
candidate_card:
  card_type: metric_implementation
  card_id: metric_implementation.flipkart.gmv.settlement_fallback
  name: Flipkart gmv.settlement_fallback
  fields:
    metric_id: metric.gross_merchandise_value
    platform_context: platform_context.flipkart.in
    source_table: table.flipkart.settlement
    source_columns:
    - sale_settled_amount
    formula: SUM(sale_settled_amount)
    filters:
    - is_active = true
    grain: settlement line
    time_basis: settlement_date
    sign_handling: preserve source sign unless formula explicitly uses ABS for reporting ratio
    aggregation_rule: aggregate at declared grain before joins
    join_dependencies:
    - see relationship cards when cross-table
    metric_pattern: platform-specific implementation of generic colloquial metric
    implementation_caveats:
    - Fallback sales proxy when OMS value is unavailable.
    sql_pattern_ref: sql.flipkart.settlement_gmv_fallback
    evidence_refs:
    - evidence.flipkart.query_patterns
    - evidence.flipkart.settlement_logic
    confidence: high
    review_status: accepted
```

```yaml
candidate_card:
  card_type: metric_implementation
  card_id: metric_implementation.flipkart.net_settlement
  name: Flipkart net_settlement
  fields:
    metric_id: metric.net_settlement
    platform_context: platform_context.flipkart.in
    source_table: table.flipkart.settlement
    source_columns:
    - settled_amount
    formula: SUM(settled_amount)
    filters:
    - is_active = true
    grain: settlement line
    time_basis: settlement_date
    sign_handling: preserve source sign unless formula explicitly uses ABS for reporting ratio
    aggregation_rule: aggregate at declared grain before joins
    join_dependencies:
    - see relationship cards when cross-table
    metric_pattern: platform-specific implementation of generic colloquial metric
    implementation_caveats:
    - Net Flipkart settlement amount.
    sql_pattern_ref: sql.flipkart.net_settlement
    evidence_refs:
    - evidence.flipkart.query_patterns
    - evidence.flipkart.settlement_logic
    confidence: high
    review_status: accepted
```

```yaml
candidate_card:
  card_type: metric_implementation
  card_id: metric_implementation.flipkart.realization_rate
  name: Flipkart realization_rate
  fields:
    metric_id: metric.realization_rate
    platform_context: platform_context.flipkart.in
    source_table: table.flipkart.settlement
    source_columns:
    - settled_amount
    - sale_settled_amount
    formula: SUM(settled_amount) / NULLIF(SUM(sale_settled_amount), 0)
    filters:
    - is_active = true
    grain: settlement line
    time_basis: settlement_date
    sign_handling: preserve source sign unless formula explicitly uses ABS for reporting ratio
    aggregation_rule: aggregate at declared grain before joins
    join_dependencies:
    - see relationship cards when cross-table
    metric_pattern: platform-specific implementation of generic colloquial metric
    implementation_caveats:
    - Use sale_settled_amount denominator.
    sql_pattern_ref: sql.flipkart.realization_rate
    evidence_refs:
    - evidence.flipkart.query_patterns
    - evidence.flipkart.settlement_logic
    confidence: high
    review_status: accepted
```

```yaml
candidate_card:
  card_type: metric_implementation
  card_id: metric_implementation.flipkart.effective_fee_rate
  name: Flipkart effective_fee_rate
  fields:
    metric_id: metric.effective_fee_rate
    platform_context: platform_context.flipkart.in
    source_table: table.flipkart.settlement
    source_columns:
    - mp_fee
    - sale_settled_amount
    formula: ABS(SUM(mp_fee)) / NULLIF(SUM(sale_settled_amount), 0)
    filters:
    - is_active = true
    grain: settlement line
    time_basis: settlement_date
    sign_handling: preserve source sign unless formula explicitly uses ABS for reporting ratio
    aggregation_rule: aggregate at declared grain before joins
    join_dependencies:
    - see relationship cards when cross-table
    metric_pattern: platform-specific implementation of generic colloquial metric
    implementation_caveats:
    - Use ABS for presenting fee burden; do not change stored sign semantics.
    sql_pattern_ref: sql.flipkart.effective_fee_rate
    evidence_refs:
    - evidence.flipkart.query_patterns
    - evidence.flipkart.settlement_logic
    confidence: high
    review_status: accepted
```

```yaml
candidate_card:
  card_type: metric_implementation
  card_id: metric_implementation.flipkart.mp_fee_total
  name: Flipkart mp_fee_total
  fields:
    metric_id: metric.marketplace_fee_total
    platform_context: platform_context.flipkart.in
    source_table: table.flipkart.settlement
    source_columns:
    - mp_fee
    formula: SUM(mp_fee)
    filters:
    - is_active = true
    grain: settlement line
    time_basis: settlement_date
    sign_handling: preserve source sign unless formula explicitly uses ABS for reporting ratio
    aggregation_rule: aggregate at declared grain before joins
    join_dependencies:
    - see relationship cards when cross-table
    metric_pattern: platform-specific implementation of generic colloquial metric
    implementation_caveats:
    - Aggregate marketplace fee from settlement.
    sql_pattern_ref: sql.flipkart.marketplace_fee_total
    evidence_refs:
    - evidence.flipkart.query_patterns
    - evidence.flipkart.settlement_logic
    confidence: high
    review_status: accepted
```

```yaml
candidate_card:
  card_type: metric_implementation
  card_id: metric_implementation.flipkart.commission_fee_detail
  name: Flipkart commission_fee_detail
  fields:
    metric_id: metric.commission_fee
    platform_context: platform_context.flipkart.in
    source_table: table.flipkart.commission
    source_columns:
    - charged_amount
    - description
    formula: SUM(charged_amount)
    filters:
    - is_active = true AND description = 'Commission'
    grain: fee line pre-aggregated by order/item for joins
    time_basis: created_date
    sign_handling: preserve source sign unless formula explicitly uses ABS for reporting ratio
    aggregation_rule: aggregate at declared grain before joins
    join_dependencies:
    - see relationship cards when cross-table
    metric_pattern: platform-specific implementation of generic colloquial metric
    implementation_caveats:
    - Use description filter.
    sql_pattern_ref: sql.flipkart.commission_fee_detail
    evidence_refs:
    - evidence.flipkart.query_patterns
    - evidence.flipkart.commission_schema
    confidence: high
    review_status: accepted
```

```yaml
candidate_card:
  card_type: metric_implementation
  card_id: metric_implementation.flipkart.fixed_fee_detail
  name: Flipkart fixed_fee_detail
  fields:
    metric_id: metric.fixed_fee
    platform_context: platform_context.flipkart.in
    source_table: table.flipkart.commission
    source_columns:
    - charged_amount
    - description
    formula: SUM(charged_amount)
    filters:
    - is_active = true AND description = 'Fixed Fee'
    grain: fee line
    time_basis: created_date
    sign_handling: preserve source sign unless formula explicitly uses ABS for reporting ratio
    aggregation_rule: aggregate at declared grain before joins
    join_dependencies:
    - see relationship cards when cross-table
    metric_pattern: platform-specific implementation of generic colloquial metric
    implementation_caveats:
    - Use description filter.
    sql_pattern_ref: sql.flipkart.fixed_fee_detail
    evidence_refs:
    - evidence.flipkart.query_patterns
    - evidence.flipkart.commission_schema
    confidence: high
    review_status: accepted
```

```yaml
candidate_card:
  card_type: metric_implementation
  card_id: metric_implementation.flipkart.shipping_fee_detail
  name: Flipkart shipping_fee_detail
  fields:
    metric_id: metric.shipping_fee
    platform_context: platform_context.flipkart.in
    source_table: table.flipkart.commission
    source_columns:
    - charged_amount
    - description
    formula: SUM(charged_amount)
    filters:
    - is_active = true AND description = 'Shipping Fee'
    grain: fee line
    time_basis: created_date
    sign_handling: preserve source sign unless formula explicitly uses ABS for reporting ratio
    aggregation_rule: aggregate at declared grain before joins
    join_dependencies:
    - see relationship cards when cross-table
    metric_pattern: platform-specific implementation of generic colloquial metric
    implementation_caveats:
    - Marketplace shipping fee only.
    sql_pattern_ref: sql.flipkart.shipping_fee_detail
    evidence_refs:
    - evidence.flipkart.query_patterns
    - evidence.flipkart.commission_schema
    confidence: high
    review_status: accepted
```

```yaml
candidate_card:
  card_type: metric_implementation
  card_id: metric_implementation.flipkart.reverse_shipping_fee_detail
  name: Flipkart reverse_shipping_fee_detail
  fields:
    metric_id: metric.reverse_shipping_fee
    platform_context: platform_context.flipkart.in
    source_table: table.flipkart.commission
    source_columns:
    - charged_amount
    - description
    formula: SUM(charged_amount)
    filters:
    - is_active = true AND description = 'Reverse Shipping Fee'
    grain: fee line
    time_basis: created_date
    sign_handling: preserve source sign unless formula explicitly uses ABS for reporting ratio
    aggregation_rule: aggregate at declared grain before joins
    join_dependencies:
    - see relationship cards when cross-table
    metric_pattern: platform-specific implementation of generic colloquial metric
    implementation_caveats:
    - Marketplace reverse shipping fee only.
    sql_pattern_ref: sql.flipkart.reverse_shipping_fee_detail
    evidence_refs:
    - evidence.flipkart.query_patterns
    - evidence.flipkart.commission_schema
    confidence: high
    review_status: accepted
```

```yaml
candidate_card:
  card_type: metric_implementation
  card_id: metric_implementation.flipkart.collection_fee_detail
  name: Flipkart collection_fee_detail
  fields:
    metric_id: metric.collection_fee
    platform_context: platform_context.flipkart.in
    source_table: table.flipkart.commission
    source_columns:
    - charged_amount
    - description
    formula: SUM(charged_amount)
    filters:
    - is_active = true AND description = 'Collection Fee'
    grain: fee line
    time_basis: created_date
    sign_handling: preserve source sign unless formula explicitly uses ABS for reporting ratio
    aggregation_rule: aggregate at declared grain before joins
    join_dependencies:
    - see relationship cards when cross-table
    metric_pattern: platform-specific implementation of generic colloquial metric
    implementation_caveats:
    - Marketplace collection/COD/payment fee only.
    sql_pattern_ref: sql.flipkart.collection_fee_detail
    evidence_refs:
    - evidence.flipkart.query_patterns
    - evidence.flipkart.commission_schema
    confidence: high
    review_status: accepted
```

```yaml
candidate_card:
  card_type: metric_implementation
  card_id: metric_implementation.flipkart.net_cashback
  name: Flipkart net_cashback
  fields:
    metric_id: metric.net_cashback
    platform_context: platform_context.flipkart.in
    source_table: table.flipkart.cashback
    source_columns:
    - charged_amount
    - transaction_type
    - document_type
    - document_sub_type
    - created_date
    formula: SUM(charged_amount)
    filters:
    - is_active = true
    grain: cashback line
    time_basis: created_date
    sign_handling: preserve source sign unless formula explicitly uses ABS for reporting ratio
    aggregation_rule: aggregate at declared grain before joins
    join_dependencies:
    - see relationship cards when cross-table
    metric_pattern: platform-specific implementation of generic colloquial metric
    implementation_caveats:
    - Preserve signed credit/debit note semantics; created_date is the documented primary date filter.
    sql_pattern_ref: sql.flipkart.cashback_net
    evidence_refs:
    - evidence.flipkart.query_patterns
    - evidence.flipkart.cashback_schema
    confidence: high
    review_status: accepted
```

```yaml
candidate_card:
  card_type: metric_implementation
  card_id: metric_implementation.flipkart.cashback_rate
  name: Flipkart cashback_rate
  fields:
    metric_id: metric.cashback_rate
    platform_context: platform_context.flipkart.in
    source_table: table.flipkart.cashback + table.flipkart.oms
    source_columns:
    - cashback.charged_amount
    - oms.charged_amount
    formula: SUM(CASE WHEN cb.transaction_type = 'forward' THEN cb.charged_amount ELSE 0 END) / NULLIF(SUM(CASE WHEN o.transaction_type = 'forward'
      THEN o.charged_amount ELSE 0 END), 0)
    filters:
    - is_active = true on both tables
    grain: order/item after cashback aggregation
    time_basis: created_date
    sign_handling: preserve source sign unless formula explicitly uses ABS for reporting ratio
    aggregation_rule: aggregate at declared grain before joins
    join_dependencies:
    - see relationship cards when cross-table
    metric_pattern: platform-specific implementation of generic colloquial metric
    implementation_caveats:
    - OMS schema partial; aggregate cashback by order_id,item_id before joining; review before production.
    sql_pattern_ref: sql.flipkart.cashback_rate
    evidence_refs:
    - evidence.flipkart.query_patterns
    - evidence.flipkart.cashback_schema
    confidence: medium
    review_status: review_required
```

```yaml
candidate_card:
  card_type: metric_implementation
  card_id: metric_implementation.flipkart.settlement_cycle_days
  name: Flipkart settlement_cycle_days
  fields:
    metric_id: metric.settlement_cycle_days
    platform_context: platform_context.flipkart.in
    source_table: table.flipkart.settlement
    source_columns:
    - created_date
    - settlement_date
    formula: AVG(DATE_DIFF('day', created_date, settlement_date))
    filters:
    - is_active = true AND settlement_date IS NOT NULL
    grain: settlement line
    time_basis: settlement_date
    sign_handling: preserve source sign unless formula explicitly uses ABS for reporting ratio
    aggregation_rule: aggregate at declared grain before joins
    join_dependencies:
    - see relationship cards when cross-table
    metric_pattern: platform-specific implementation of generic colloquial metric
    implementation_caveats:
    - Dispatch date is preferable but not present in source excerpts.
    sql_pattern_ref: sql.flipkart.settlement_cycle
    evidence_refs:
    - evidence.flipkart.query_patterns
    - evidence.flipkart.settlement_logic
    confidence: medium
    review_status: review_required
```

```yaml
candidate_card:
  card_type: metric_implementation
  card_id: metric_implementation.flipkart.tcs_deducted
  name: Flipkart tcs_deducted
  fields:
    metric_id: metric.tcs_deducted
    platform_context: platform_context.flipkart.in
    source_table: table.flipkart.settlement
    source_columns:
    - total_tcs_amount
    formula: SUM(total_tcs_amount)
    filters:
    - is_active = true
    grain: settlement line
    time_basis: settlement_date
    sign_handling: preserve source sign unless formula explicitly uses ABS for reporting ratio
    aggregation_rule: aggregate at declared grain before joins
    join_dependencies:
    - see relationship cards when cross-table
    metric_pattern: platform-specific implementation of generic colloquial metric
    implementation_caveats:
    - Cash-flow tax deduction, not statutory filing.
    sql_pattern_ref: sql.flipkart.tcs_deducted
    evidence_refs:
    - evidence.flipkart.query_patterns
    - evidence.flipkart.settlement_logic
    confidence: high
    review_status: accepted
```

```yaml
candidate_card:
  card_type: metric_implementation
  card_id: metric_implementation.flipkart.tds_deducted
  name: Flipkart tds_deducted
  fields:
    metric_id: metric.tds_deducted
    platform_context: platform_context.flipkart.in
    source_table: table.flipkart.settlement
    source_columns:
    - total_tds_amount
    formula: SUM(total_tds_amount)
    filters:
    - is_active = true
    grain: settlement line
    time_basis: settlement_date
    sign_handling: preserve source sign unless formula explicitly uses ABS for reporting ratio
    aggregation_rule: aggregate at declared grain before joins
    join_dependencies:
    - see relationship cards when cross-table
    metric_pattern: platform-specific implementation of generic colloquial metric
    implementation_caveats:
    - Cash-flow tax deduction, not statutory filing.
    sql_pattern_ref: sql.flipkart.tds_deducted
    evidence_refs:
    - evidence.flipkart.query_patterns
    - evidence.flipkart.settlement_logic
    confidence: high
    review_status: accepted
```

```yaml
candidate_card:
  card_type: metric_implementation
  card_id: metric_implementation.flipkart.gst_on_mp_fees
  name: Flipkart gst_on_mp_fees
  fields:
    metric_id: metric.gst_on_marketplace_fees
    platform_context: platform_context.flipkart.in
    source_table: table.flipkart.settlement
    source_columns:
    - gst_on_mp_fees
    formula: SUM(gst_on_mp_fees)
    filters:
    - is_active = true
    grain: settlement line
    time_basis: settlement_date
    sign_handling: preserve source sign unless formula explicitly uses ABS for reporting ratio
    aggregation_rule: aggregate at declared grain before joins
    join_dependencies:
    - see relationship cards when cross-table
    metric_pattern: platform-specific implementation of generic colloquial metric
    implementation_caveats:
    - Settlement-level GST on marketplace fees.
    sql_pattern_ref: sql.flipkart.gst_on_mp_fees
    evidence_refs:
    - evidence.flipkart.query_patterns
    - evidence.flipkart.settlement_logic
    confidence: high
    review_status: accepted
```

```yaml
candidate_card:
  card_type: metric_implementation
  card_id: metric_implementation.flipkart.fee_tax_detail
  name: Flipkart fee_tax_detail
  fields:
    metric_id: metric.gst_on_marketplace_fees
    platform_context: platform_context.flipkart.in
    source_table: table.flipkart.commission
    source_columns:
    - total_tax
    formula: SUM(total_tax)
    filters:
    - is_active = true
    grain: fee line
    time_basis: created_date
    sign_handling: preserve source sign unless formula explicitly uses ABS for reporting ratio
    aggregation_rule: aggregate at declared grain before joins
    join_dependencies:
    - see relationship cards when cross-table
    metric_pattern: platform-specific implementation of generic colloquial metric
    implementation_caveats:
    - Detailed fee tax from commission table.
    sql_pattern_ref: sql.flipkart.fee_tax_detail
    evidence_refs:
    - evidence.flipkart.query_patterns
    - evidence.flipkart.commission_schema
    confidence: high
    review_status: accepted
```

```yaml
candidate_card:
  card_type: metric_implementation
  card_id: metric_implementation.flipkart.return_rate
  name: Flipkart return_rate
  fields:
    metric_id: metric.return_rate
    platform_context: platform_context.flipkart.in
    source_table: table.flipkart.settlement
    source_columns:
    - return_type
    - refund_settled_amount
    - sale_settled_amount
    - order_id
    formula: COUNT(DISTINCT CASE WHEN return_type IS NOT NULL OR refund_settled_amount < 0 THEN order_id END) / NULLIF(COUNT(DISTINCT CASE WHEN
      sale_settled_amount > 0 THEN order_id END), 0)
    filters:
    - is_active = true
    grain: order
    time_basis: settlement_date
    sign_handling: preserve source sign unless formula explicitly uses ABS for reporting ratio
    aggregation_rule: aggregate at declared grain before joins
    join_dependencies:
    - see relationship cards when cross-table
    metric_pattern: platform-specific implementation of generic colloquial metric
    implementation_caveats:
    - Settlement-based proxy; full OMS reverse/forward implementation is preferred when verified.
    sql_pattern_ref: sql.flipkart.return_rate
    evidence_refs:
    - evidence.flipkart.query_patterns
    - evidence.flipkart.settlement_logic
    confidence: medium
    review_status: review_required
```

```yaml
candidate_card:
  card_type: metric_implementation
  card_id: metric_implementation.flipkart.cancellation_rate
  name: Flipkart cancellation_rate
  fields:
    metric_id: metric.cancellation_rate
    platform_context: platform_context.flipkart.in
    source_table: table.flipkart.cashback
    source_columns:
    - transaction_type
    - document_sub_type
    - order_id
    formula: COUNT(DISTINCT CASE WHEN transaction_type = 'forward cancel' OR document_sub_type = 'Cancellation' THEN order_id END) / NULLIF(COUNT(DISTINCT
      CASE WHEN transaction_type = 'forward' THEN order_id END), 0)
    filters:
    - is_active = true
    grain: order
    time_basis: created_date
    sign_handling: preserve source sign unless formula explicitly uses ABS for reporting ratio
    aggregation_rule: aggregate at declared grain before joins
    join_dependencies:
    - see relationship cards when cross-table
    metric_pattern: platform-specific implementation of generic colloquial metric
    implementation_caveats:
    - Cashback document_sub_type/transaction_type is a cancellation signal, not full OMS cancellation truth.
    sql_pattern_ref: sql.flipkart.cancellation_rate
    evidence_refs:
    - evidence.flipkart.query_patterns
    - evidence.flipkart.cashback_schema
    confidence: medium
    review_status: review_required
```

```yaml
candidate_card:
  card_type: metric_implementation
  card_id: metric_implementation.flipkart.protection_fund
  name: Flipkart protection_fund
  fields:
    metric_id: metric.protection_fund_settlement
    platform_context: platform_context.flipkart.in
    source_table: table.flipkart.settlement
    source_columns:
    - protection_fund_settled_amount
    formula: SUM(protection_fund_settled_amount)
    filters:
    - is_active = true
    grain: settlement line
    time_basis: settlement_date
    sign_handling: preserve source sign unless formula explicitly uses ABS for reporting ratio
    aggregation_rule: aggregate at declared grain before joins
    join_dependencies:
    - see relationship cards when cross-table
    metric_pattern: platform-specific implementation of generic colloquial metric
    implementation_caveats:
    - Protection fund component from settlement.
    sql_pattern_ref: sql.flipkart.protection_fund_settlement
    evidence_refs:
    - evidence.flipkart.query_patterns
    - evidence.flipkart.settlement_logic
    confidence: high
    review_status: accepted
```

### 5.10 Formula Template Cards

```yaml
candidate_card:
  card_type: formula_template
  card_id: formula.flipkart.realization_rate
  name: realization_rate
  fields:
    formula_name: realization_rate
    inputs: 
      - settled_amount
      - sale_settled_amount
    formula: SUM(settled_amount) / NULLIF(SUM(sale_settled_amount), 0)
    semantic_constraints: 
      - Use settlement_date basis and active settlement rows.
    sign_handling: source-sign preserving unless stated otherwise
    evidence_refs: 
      - evidence.flipkart.query_patterns
    confidence: high
    review_status: accepted
```

```yaml
candidate_card:
  card_type: formula_template
  card_id: formula.flipkart.effective_fee_rate
  name: effective_fee_rate
  fields:
    formula_name: effective_fee_rate
    inputs: 
      - mp_fee
      - sale_settled_amount
    formula: ABS(SUM(mp_fee)) / NULLIF(SUM(sale_settled_amount), 0)
    semantic_constraints: 
      - ABS is presentational for fee burden only.
    sign_handling: source-sign preserving unless stated otherwise
    evidence_refs: 
      - evidence.flipkart.query_patterns
    confidence: high
    review_status: accepted
```

```yaml
candidate_card:
  card_type: formula_template
  card_id: formula.flipkart.total_fee_detail
  name: total_fee_detail
  fields:
    formula_name: total_fee_detail
    inputs: 
      - commission_fee
      - fixed_fee
      - shipping_fee
      - reverse_shipping_fee
      - collection_fee
      - total_tax
    formula: SUM(charged_amount + total_tax) after fee-line classification
    semantic_constraints: 
      - Pre-aggregate commission table by order_id,item_id and description.
    sign_handling: source-sign preserving unless stated otherwise
    evidence_refs: 
      - evidence.flipkart.query_patterns
    confidence: high
    review_status: accepted
```

```yaml
candidate_card:
  card_type: formula_template
  card_id: formula.flipkart.net_cashback
  name: net_cashback
  fields:
    formula_name: net_cashback
    inputs: 
      - charged_amount
    formula: SUM(charged_amount)
    semantic_constraints: 
      - Preserve forward/reverse/cancel signs.
    sign_handling: source-sign preserving unless stated otherwise
    evidence_refs: 
      - evidence.flipkart.query_patterns
    confidence: high
    review_status: accepted
```

```yaml
candidate_card:
  card_type: formula_template
  card_id: formula.flipkart.order_id_normalization
  name: commission_order_id_normalization
  fields:
    formula_name: commission_order_id_normalization
    inputs: 
      - order_id
    formula: REPLACE(other_table.order_id, 'OD', '') = commission.order_id
    semantic_constraints: 
      - Required when joining commission to OD-prefixed order ids.
    sign_handling: source-sign preserving unless stated otherwise
    evidence_refs: 
      - evidence.flipkart.query_patterns
    confidence: high
    review_status: accepted
```

```yaml
candidate_card:
  card_type: formula_template
  card_id: formula.flipkart.settlement_cycle_days
  name: settlement_cycle_days
  fields:
    formula_name: settlement_cycle_days
    inputs: 
      - created_date
      - settlement_date
    formula: DATE_DIFF('day', created_date, settlement_date)
    semantic_constraints: 
      - Dispatch date preferred but absent; created_date is fallback.
    sign_handling: source-sign preserving unless stated otherwise
    evidence_refs: 
      - evidence.flipkart.query_patterns
    confidence: high
    review_status: accepted
```

```yaml
candidate_card:
  card_type: formula_template
  card_id: formula.flipkart.volumetric_weight
  name: volumetric_weight
  fields:
    formula_name: volumetric_weight
    inputs: 
      - length
      - breadth
      - height
    formula: length * breadth * height / 5000
    semantic_constraints: 
      - Use only when dimensions are present; settlement has vol_weight already.
    sign_handling: source-sign preserving unless stated otherwise
    evidence_refs: 
      - evidence.flipkart.query_patterns
    confidence: high
    review_status: accepted
```

```yaml
candidate_card:
  card_type: formula_template
  card_id: formula.flipkart.settlement_waterfall
  name: settlement_waterfall
  fields:
    formula_name: settlement_waterfall
    inputs:
    - sale_settled_amount
    - refund_settled_amount
    - offer_settled_amount
    - my_share_settled_amount
    - addon_settled_amount
    - taxes_settled_amount
    - offer_adjustment_settled_amount
    - protection_fund_settled_amount
    - mp_fee
    - gst_on_mp_fees
    - total_tcs_amount
    - total_tds_amount
    formula: credits(sale + refund + offer + my_share + addon + taxes + offer_adjustment + protection_fund) - ABS(mp_fee) - ABS(gst_on_mp_fees)
      - ABS(total_tcs_amount) - ABS(total_tds_amount) ≈ settled_amount
    semantic_constraints:
    - Use the DOCX settlement waterfall; numeric tolerance remains review-required unless the SQL pattern explicitly uses 0.01.
    sign_handling: source-sign preserving unless stated otherwise
    evidence_refs:
    - evidence.flipkart.settlement_logic
    confidence: high
    review_status: accepted
```

### 5.11 Metric Dependency Cards

```yaml
candidate_card:
  card_type: metric_dependency
  card_id: metric_dependency.flipkart.realization.depends_on.settlement
  name: Flipkart realization.depends_on.settlement
  fields:
    metric_id: metric.realization_rate
    depends_on: 
      - metric.net_settlement
      - metric.gross_merchandise_value
    dependency_type: ratio_denominator
    aggregation_order: dependencies must be computed/normalized before parent metric
    required_before_computation: true
    evidence_refs: 
      - evidence.flipkart.relationships
    confidence: high
    review_status: accepted
```

```yaml
candidate_card:
  card_type: metric_dependency
  card_id: metric_dependency.flipkart.fee_rate.depends_on.fees_sales
  name: Flipkart fee_rate.depends_on.fees_sales
  fields:
    metric_id: metric.effective_fee_rate
    depends_on: 
      - metric.marketplace_fee_total
      - metric.gross_merchandise_value
    dependency_type: ratio_denominator
    aggregation_order: dependencies must be computed/normalized before parent metric
    required_before_computation: true
    evidence_refs: 
      - evidence.flipkart.relationships
    confidence: high
    review_status: accepted
```

```yaml
candidate_card:
  card_type: metric_dependency
  card_id: metric_dependency.flipkart.cashback_rate.depends_on.cashback_sales
  name: Flipkart cashback_rate.depends_on.cashback_sales
  fields:
    metric_id: metric.cashback_rate
    depends_on: 
      - metric.net_cashback
      - metric.gross_merchandise_value
    dependency_type: ratio_denominator
    aggregation_order: dependencies must be computed/normalized before parent metric
    required_before_computation: true
    evidence_refs: 
      - evidence.flipkart.relationships
    confidence: high
    review_status: accepted
```

```yaml
candidate_card:
  card_type: metric_dependency
  card_id: metric_dependency.flipkart.aov.depends_on.gmv_count
  name: Flipkart aov.depends_on.gmv_count
  fields:
    metric_id: metric.average_order_value
    depends_on: 
      - metric.gross_merchandise_value
      - metric.order_count
    dependency_type: ratio_denominator
    aggregation_order: dependencies must be computed/normalized before parent metric
    required_before_computation: true
    evidence_refs: 
      - evidence.flipkart.relationships
    confidence: high
    review_status: accepted
```

```yaml
candidate_card:
  card_type: metric_dependency
  card_id: metric_dependency.flipkart.settlement_recon.depends_on.normalization
  name: Flipkart settlement_recon.depends_on.normalization
  fields:
    metric_id: metric.marketplace_fee_total
    depends_on: 
      - formula.flipkart.order_id_normalization
    dependency_type: join_normalization
    aggregation_order: dependencies must be computed/normalized before parent metric
    required_before_computation: true
    evidence_refs: 
      - evidence.flipkart.relationships
    confidence: high
    review_status: accepted
```

### 5.12 Business Process Cards

```yaml
candidate_card:
  card_type: business_process
  card_id: business_process.flipkart.forward_order_to_settlement
  name: Forward order to settlement
  fields:
    process_name: Flipkart settlement/payment verification
    marketplace_module: Flipkart marketplace
    trigger_event: settled order item appears in flipkart_settlement
    start_state: settlement sale/refund/offer components available
    end_state: settled_amount computed from marketplace components and settlement timing measured
    participating_tables:
    - table.flipkart.settlement
    - table.flipkart.oms
    important_columns:
    - order_id
    - item_id
    - sale_settled_amount
    - refund_settled_amount
    - settled_amount
    - settlement_date
    - created_date
    - neft_type
    out_of_scope_external_steps:
    - external logistics lifecycle
    - bank deposit matching
    - account binding
    evidence_refs:
    - evidence.flipkart.payment_process
    - evidence.flipkart.settlement_logic
    confidence: high
    review_status: accepted
```

```yaml
candidate_card:
  card_type: business_process
  card_id: business_process.flipkart.return_cancel_reversal
  name: Return/cancel reversal
  fields:
    process_name: Return/cancel reversal through settlement and cashback
    marketplace_module: Flipkart marketplace
    trigger_event: return or forward cancel transaction appears
    start_state: forward sale / credit note exists
    end_state: refund settlement component or debit-note cashback reversal recorded
    participating_tables:
    - table.flipkart.settlement
    - table.flipkart.cashback
    - table.flipkart.oms
    important_columns:
    - return_type
    - refund_settled_amount
    - transaction_type
    - document_type
    - document_sub_type
    - charged_amount
    out_of_scope_external_steps:
    - external logistics lifecycle
    - bank deposit matching
    - account binding
    evidence_refs:
    - evidence.flipkart.cashback_schema
    - evidence.flipkart.settlement_logic
    - evidence.flipkart.metrics_benchmarks
    confidence: high
    review_status: accepted
```

```yaml
candidate_card:
  card_type: business_process
  card_id: business_process.flipkart.commission_fee_invoice
  name: Commission fee invoice
  fields:
    process_name: Commission fee invoice validation
    marketplace_module: Flipkart marketplace
    trigger_event: active flipkart_commission fee invoice rows with metadata = 'commission invoice'
    start_state: fee invoice line by order_id,item_id,description
    end_state: fee detail aggregated and reconciled to settlement mp_fee
    participating_tables:
    - table.flipkart.commission
    - table.flipkart.settlement
    important_columns:
    - order_id
    - item_id
    - description
    - fee_name
    - charged_amount
    - total_tax
    - mp_fee
    out_of_scope_external_steps:
    - external logistics lifecycle
    - bank deposit matching
    - account binding
    evidence_refs:
    - evidence.flipkart.commission_schema
    - evidence.flipkart.relationships
    - evidence.flipkart.reconciliation_framework
    confidence: high
    review_status: accepted
```

```yaml
candidate_card:
  card_type: business_process
  card_id: business_process.flipkart.cashback_credit_debit_note
  name: Cashback credit/debit note
  fields:
    process_name: Cashback credit/debit note reconciliation
    marketplace_module: Flipkart marketplace
    trigger_event: cashback credit note, debit note, return, or cancellation row appears
    start_state: cashback credit/debit note line
    end_state: signed net cashback compared to settlement offer fields
    participating_tables:
    - table.flipkart.cashback
    - table.flipkart.settlement
    important_columns:
    - order_id
    - item_id
    - transaction_type
    - document_type
    - document_sub_type
    - charged_amount
    - offer_settled_amount
    - offer_adjustment_settled_amount
    out_of_scope_external_steps:
    - external logistics lifecycle
    - bank deposit matching
    - account binding
    evidence_refs:
    - evidence.flipkart.cashback_schema
    - evidence.flipkart.reconciliation_framework
    confidence: high
    review_status: accepted
```



```yaml
candidate_card:
  card_type: business_process
  card_id: business_process.flipkart.marketplace_reconciliation_pipeline
  name: Marketplace reconciliation pipeline
  fields:
    process_name: Flipkart five-step marketplace reconciliation framework
    marketplace_module: Flipkart marketplace
    trigger_event: OMS, settlement, commission, and cashback tables available for a reconciliation period
    start_state: marketplace source rows filtered to active records
    end_state: order, fee, cashback, settlement, and cross-table discrepancy outputs produced
    participating_tables:
    - table.flipkart.oms
    - table.flipkart.settlement
    - table.flipkart.commission
    - table.flipkart.cashback
    important_columns:
    - order_id
    - item_id
    - charged_amount
    - settled_amount
    - mp_fee
    - total_tax
    - transaction_type
    - description
    out_of_scope_external_steps:
    - external logistics lifecycle
    - bank deposit matching
    - account binding
    evidence_refs:
    - evidence.flipkart.reconciliation_framework
    confidence: high
    review_status: accepted
```

### 5.13 Workflow Step Cards

```yaml
candidate_card:
  card_type: workflow_step
  card_id: workflow_step.flipkart.order_capture
  name: Capture order item
  fields:
    process_id: business_process.flipkart.forward_order_to_settlement
    step_order: 1
    step_name: Settlement sale component capture
    trigger: active settlement line available for order_id,item_id
    input_tables:
    - table.flipkart.settlement
    output_semantics: sale_settled_amount, refund_settled_amount, and offer/protection components become the settlement-side facts for the order
      item
    required_keys:
    - order_id
    - item_id
    - settlement_id
    important_columns:
    - sale_settled_amount
    - refund_settled_amount
    - offer_settled_amount
    - settled_amount
    evidence_refs:
    - evidence.flipkart.settlement_logic
    confidence: high
    review_status: accepted
```

```yaml
candidate_card:
  card_type: workflow_step
  card_id: workflow_step.flipkart.settlement_capture
  name: Capture settlement line
  fields:
    process_id: business_process.flipkart.forward_order_to_settlement
    step_order: 2
    step_name: Apply marketplace deductions and compute net settlement
    trigger: settlement components and fee/tax deductions available on the same settlement line
    input_tables:
    - table.flipkart.settlement
    output_semantics: settled_amount is verified against documented settlement waterfall using mp_fee, GST on fees, TCS, and TDS deductions
    required_keys:
    - order_id
    - item_id
    - settlement_id
    important_columns:
    - settled_amount
    - mp_fee
    - gst_on_mp_fees
    - total_tcs_amount
    - total_tds_amount
    evidence_refs:
    - evidence.flipkart.settlement_logic
    confidence: high
    review_status: accepted
```

```yaml
candidate_card:
  card_type: workflow_step
  card_id: workflow_step.flipkart.fee_invoice_capture
  name: Capture fee invoice lines
  fields:
    process_id: business_process.flipkart.commission_fee_invoice
    step_order: 1
    step_name: Capture fee invoice lines
    trigger: source row available
    input_tables:
    - table.flipkart.commission
    output_semantics: fee invoice line is captured with description/fee_name, charged_amount, total_tax, transaction_type, and metadata
    required_keys:
    - order_id
    - item_id
    important_columns:
    - description
    - fee_name
    - charged_amount
    - total_tax
    - metadata
    - transaction_type
    evidence_refs:
    - evidence.flipkart.commission_schema
    confidence: high
    review_status: accepted
```

```yaml
candidate_card:
  card_type: workflow_step
  card_id: workflow_step.flipkart.fee_aggregation
  name: Aggregate fee detail
  fields:
    process_id: business_process.flipkart.commission_fee_invoice
    step_order: 2
    step_name: Aggregate fee detail
    trigger: source row available
    input_tables:
    - table.flipkart.commission
    output_semantics: commission fee lines are pre-aggregated by normalized order_id,item_id before comparison to settlement mp_fee
    required_keys:
    - order_id_without_od_prefix
    - item_id
    important_columns:
    - description
    - charged_amount
    - total_tax
    evidence_refs:
    - evidence.flipkart.relationships
    - evidence.flipkart.commission_schema
    confidence: high
    review_status: accepted
```

```yaml
candidate_card:
  card_type: workflow_step
  card_id: workflow_step.flipkart.cashback_note_capture
  name: Capture credit/debit note
  fields:
    process_id: business_process.flipkart.cashback_credit_debit_note
    step_order: 1
    step_name: Capture credit/debit note
    trigger: source row available
    input_tables:
    - table.flipkart.cashback
    output_semantics: credit/debit note row captures signed promotional subsidy and document classification
    required_keys:
    - order_id
    - item_id
    - credit_debit_note_no
    important_columns:
    - transaction_type
    - document_type
    - document_sub_type
    - charged_amount
    - created_date
    evidence_refs:
    - evidence.flipkart.cashback_schema
    confidence: high
    review_status: accepted
```

```yaml
candidate_card:
  card_type: workflow_step
  card_id: workflow_step.flipkart.cashback_aggregation
  name: Aggregate cashback
  fields:
    process_id: business_process.flipkart.cashback_credit_debit_note
    step_order: 2
    step_name: Aggregate cashback
    trigger: source row available
    input_tables:
    - table.flipkart.cashback
    output_semantics: signed cashback rows are aggregated by order_id,item_id before comparison to settlement offer and offer adjustment fields
    required_keys:
    - order_id
    - item_id
    important_columns:
    - charged_amount
    - offer_settled_amount
    - offer_adjustment_settled_amount
    evidence_refs:
    - evidence.flipkart.cashback_schema
    - evidence.flipkart.relationships
    confidence: high
    review_status: accepted
```

```yaml
candidate_card:
  card_type: workflow_step
  card_id: workflow_step.flipkart.settlement_reconcile
  name: Reconcile settlement to source concepts
  fields:
    process_id: business_process.flipkart.marketplace_reconciliation_pipeline
    step_order: 1
    step_name: Step 1 order verification
    trigger: active OMS/order rows are available for the period
    input_tables:
    - table.flipkart.oms
    output_semantics: confirm orders exist, transaction types are correct, quantities/amounts/tax are present, and missing/duplicate orders are
      identified
    required_keys:
    - order_id
    - item_id
    important_columns:
    - transaction_type
    - charged_amount
    - quantity
    - is_active
    evidence_refs:
    - evidence.flipkart.reconciliation_framework
    confidence: high
    review_status: accepted
```

```yaml
candidate_card:
  card_type: workflow_step
  card_id: workflow_step.flipkart.exception_output
  name: Output exceptions
  fields:
    process_id: business_process.flipkart.marketplace_reconciliation_pipeline
    step_order: 5
    step_name: Step 5 cross-table discrepancy detection
    trigger: order, fee, cashback, and settlement sides have been filtered, normalized, and aggregated
    input_tables:
    - table.flipkart.oms
    - table.flipkart.settlement
    - table.flipkart.commission
    - table.flipkart.cashback
    output_semantics: compare OMS charged_amount minus commission fees, fee GST, TCS, and TDS against settlement.settled_amount and surface discrepancies
    required_keys:
    - order_id
    - item_id
    important_columns:
    - charged_amount
    - charged_amount + total_tax
    - total_tcs_amount
    - total_tds_amount
    - settled_amount
    evidence_refs:
    - evidence.flipkart.reconciliation_framework
    confidence: high
    review_status: accepted
```

```yaml
candidate_card:
  card_type: workflow_step
  card_id: workflow_step.flipkart.recon_fee_validation
  name: Step 2 fee validation
  fields:
    process_id: business_process.flipkart.marketplace_reconciliation_pipeline
    step_order: 2
    step_name: Step 2 fee validation
    trigger: five-step reconciliation framework execution
    input_tables:
    - table.flipkart.oms
    - table.flipkart.settlement
    - table.flipkart.commission
    - table.flipkart.cashback
    output_semantics: verify Fixed Fee, Commission, Shipping Fee, Reverse Shipping Fee, Collection Fee, waivers, and rebates against fee invoice
      detail before settlement comparison
    required_keys:
    - order_id
    - item_id
    important_columns:
    - description
    - fee_name
    - charged_amount
    - total_tax
    evidence_refs:
    - evidence.flipkart.reconciliation_framework
    confidence: high
    review_status: accepted
```

```yaml
candidate_card:
  card_type: workflow_step
  card_id: workflow_step.flipkart.recon_cashback_reconciliation
  name: Step 3 cashback reconciliation
  fields:
    process_id: business_process.flipkart.marketplace_reconciliation_pipeline
    step_order: 3
    step_name: Step 3 cashback reconciliation
    trigger: five-step reconciliation framework execution
    input_tables:
    - table.flipkart.oms
    - table.flipkart.settlement
    - table.flipkart.commission
    - table.flipkart.cashback
    output_semantics: ensure cashback credit notes balance promotional orders and debit notes reverse cashback on returns/cancellations
    required_keys:
    - order_id
    - item_id
    important_columns:
    - transaction_type
    - document_type
    - document_sub_type
    - charged_amount
    evidence_refs:
    - evidence.flipkart.reconciliation_framework
    confidence: high
    review_status: accepted
```

```yaml
candidate_card:
  card_type: workflow_step
  card_id: workflow_step.flipkart.recon_settlement_verification
  name: Step 4 settlement verification
  fields:
    process_id: business_process.flipkart.marketplace_reconciliation_pipeline
    step_order: 4
    step_name: Step 4 settlement verification
    trigger: five-step reconciliation framework execution
    input_tables:
    - table.flipkart.oms
    - table.flipkart.settlement
    - table.flipkart.commission
    - table.flipkart.cashback
    output_semantics: confirm net payout matches expected order value minus fees and taxes, mp_fee matches commission detail, TCS/TDS are correct,
      and settlement timing is checked against SLA
    required_keys:
    - order_id
    - item_id
    important_columns:
    - settled_amount
    - sale_settled_amount
    - mp_fee
    - total_tcs_amount
    - total_tds_amount
    evidence_refs:
    - evidence.flipkart.reconciliation_framework
    confidence: high
    review_status: accepted
```

```yaml
candidate_card:
  card_type: workflow_step
  card_id: workflow_step.flipkart.return_cashback_reversal
  name: Cashback debit-note reversal
  fields:
    process_id: business_process.flipkart.return_cancel_reversal
    step_order: 1
    step_name: Cashback debit-note reversal
    trigger: return or cancellation signal appears in cashback or settlement
    input_tables:
    - table.flipkart.cashback
    - table.flipkart.settlement
    output_semantics: reverse or forward-cancel cashback debit notes claw back prior promotional credits using negative charged_amount.
    required_keys:
    - order_id
    - item_id
    important_columns:
    - transaction_type
    - document_type
    - document_sub_type
    - charged_amount
    evidence_refs:
    - evidence.flipkart.cashback_schema
    - evidence.flipkart.settlement_logic
    confidence: high
    review_status: accepted
```

```yaml
candidate_card:
  card_type: workflow_step
  card_id: workflow_step.flipkart.return_refund_settlement_component
  name: Settlement refund component capture
  fields:
    process_id: business_process.flipkart.return_cancel_reversal
    step_order: 2
    step_name: Settlement refund component capture
    trigger: return or cancellation signal appears in cashback or settlement
    input_tables:
    - table.flipkart.cashback
    - table.flipkart.settlement
    output_semantics: refund_settled_amount and return_type capture return/refund settlement impact for order item reconciliation.
    required_keys:
    - order_id
    - item_id
    important_columns:
    - return_type
    - refund_settled_amount
    - settled_amount
    evidence_refs:
    - evidence.flipkart.cashback_schema
    - evidence.flipkart.settlement_logic
    confidence: high
    review_status: accepted
```


### 5.14 State Transition Cards



```yaml
candidate_card:
  card_type: state_transition
  card_id: state_transition.flipkart.cashback.sale_to_return
  name: Flipkart cashback.sale_to_return
  fields:
    process_id: business_process.flipkart.cashback_credit_debit_note
    from_state: forward + Credit Note + Sale
    to_state: reverse + Debit Note + Return
    trigger: customer return reverses a prior cashback credit
    evidence_column: cashback.transaction_type + cashback.document_type + cashback.document_sub_type
    business_effect: cashback credit is clawed back with negative charged_amount on return
    evidence_refs:
    - evidence.flipkart.cashback_schema
    confidence: high
    review_status: accepted
    value_mapping:
      from:
        transaction_type: forward
        document_type: Credit Note
        document_sub_type: Sale
      to:
        transaction_type: reverse
        document_type: Debit Note
        document_sub_type: Return
```

```yaml
candidate_card:
  card_type: state_transition
  card_id: state_transition.flipkart.cashback.forward_to_cancel
  name: Flipkart cashback.forward_to_cancel
  fields:
    process_id: business_process.flipkart.cashback_credit_debit_note
    from_state: forward cashback credit
    to_state: forward cancel + Debit Note + Cancellation
    trigger: order cancelled before delivery reverses cashback/offer credit
    evidence_column: cashback.transaction_type + cashback.document_type + cashback.document_sub_type
    business_effect: cancelled cashback/offer impact is recorded as a negative debit-note amount
    evidence_refs:
    - evidence.flipkart.cashback_schema
    confidence: high
    review_status: accepted
    value_mapping:
      to:
        transaction_type: forward cancel
        document_type: Debit Note
        document_sub_type: Cancellation
```


### 5.15 Process Variant Cards

No `process_variant` candidate cards are emitted in V9. Fulfilment, Shopsy, prepaid/postpaid, and seller-tier concepts are represented as value profiles, rules, benchmarks, or review items unless a source documents a materially different process sequence or matching logic.

### 5.16 Marketplace-Internal Reconciliation Profile Cards

```yaml
candidate_card:
  card_type: reconciliation_profile
  card_id: reconciliation_profile.flipkart.oms_settlement
  name: Flipkart OMS/order to settlement
  fields:
    profile_name: Flipkart OMS/order to settlement
    expected_side: reconciliation_side.flipkart.oms_expected
    actual_side: reconciliation_side.flipkart.settlement_actual
    unit: reconciliation_unit.flipkart.order_item
    matching_logic: matching_logic.flipkart.oms_settlement
    mismatch_categories: 
      - missing_settlement
      - amount_variance
      - fee_variance
      - cashback_variance
      - normalization_failure
    tolerance: review_required
    date_window: review required unless query pattern defines one
    grain: order_id + item_id or settlement line
    out_of_scope_cross_domain: 
      - bank deposits
      - external logistics
      - ERP/accounting
    evidence_refs: 
      - evidence.flipkart.query_patterns
      - evidence.flipkart.relationships
    confidence: medium
    review_status: review_required
```

```yaml
candidate_card:
  card_type: reconciliation_profile
  card_id: reconciliation_profile.flipkart.settlement_commission
  name: Flipkart settlement mp_fee to commission detail
  fields:
    profile_name: Flipkart settlement mp_fee to commission detail
    expected_side: reconciliation_side.flipkart.settlement_fee_actual
    actual_side: reconciliation_side.flipkart.commission_detail_expected
    unit: reconciliation_unit.flipkart.normalized_order_item
    matching_logic: matching_logic.flipkart.settlement_commission_od_normalized
    mismatch_categories: 
      - missing_settlement
      - amount_variance
      - fee_variance
      - cashback_variance
      - normalization_failure
    tolerance: 0.01
    date_window: review required unless query pattern defines one
    grain: order_id + item_id or settlement line
    out_of_scope_cross_domain: 
      - bank deposits
      - external logistics
      - ERP/accounting
    evidence_refs: 
      - evidence.flipkart.query_patterns
      - evidence.flipkart.relationships
    confidence: high
    review_status: accepted
```

```yaml
candidate_card:
  card_type: reconciliation_profile
  card_id: reconciliation_profile.flipkart.cashback_settlement_offer
  name: Flipkart cashback to settlement offer fields
  fields:
    profile_name: Flipkart cashback to settlement offer fields
    expected_side: reconciliation_side.flipkart.cashback_expected
    actual_side: reconciliation_side.flipkart.settlement_offer_actual
    unit: reconciliation_unit.flipkart.order_item
    matching_logic: matching_logic.flipkart.cashback_settlement_offer
    mismatch_categories: 
      - missing_settlement
      - amount_variance
      - fee_variance
      - cashback_variance
      - normalization_failure
    tolerance: 0.01
    date_window: review required unless query pattern defines one
    grain: order_id + item_id or settlement line
    out_of_scope_cross_domain: 
      - bank deposits
      - external logistics
      - ERP/accounting
    evidence_refs: 
      - evidence.flipkart.query_patterns
      - evidence.flipkart.relationships
    confidence: high
    review_status: accepted
```

```yaml
candidate_card:
  card_type: reconciliation_profile
  card_id: reconciliation_profile.flipkart.settlement_waterfall
  name: Flipkart settlement component waterfall
  fields:
    profile_name: Flipkart settlement component waterfall
    expected_side: reconciliation_side.flipkart.settlement_components
    actual_side: reconciliation_side.flipkart.settlement_net
    unit: reconciliation_unit.flipkart.settlement_line
    matching_logic: matching_logic.flipkart.settlement_waterfall
    mismatch_categories: 
      - missing_settlement
      - amount_variance
      - fee_variance
      - cashback_variance
      - normalization_failure
    tolerance: review_required
    date_window: review required unless query pattern defines one
    grain: order_id + item_id or settlement line
    out_of_scope_cross_domain: 
      - bank deposits
      - external logistics
      - ERP/accounting
    evidence_refs: 
      - evidence.flipkart.query_patterns
      - evidence.flipkart.relationships
    confidence: medium
    review_status: review_required
```

```yaml
candidate_card:
  card_type: reconciliation_profile
  card_id: reconciliation_profile.flipkart.cross_table_pipeline
  name: Flipkart marketplace financial pipeline
  fields:
    profile_name: Flipkart marketplace financial pipeline
    expected_side: reconciliation_side.flipkart.order_fee_cashback_expected
    actual_side: reconciliation_side.flipkart.settlement_actual
    unit: reconciliation_unit.flipkart.order_item
    matching_logic: matching_logic.flipkart.cross_table_pipeline
    mismatch_categories: 
      - missing_settlement
      - amount_variance
      - fee_variance
      - cashback_variance
      - normalization_failure
    tolerance: review_required
    date_window: review required unless query pattern defines one
    grain: order_id + item_id or settlement line
    out_of_scope_cross_domain: 
      - bank deposits
      - external logistics
      - ERP/accounting
    evidence_refs: 
      - evidence.flipkart.query_patterns
      - evidence.flipkart.relationships
    confidence: medium
    review_status: review_required
```

### 5.17 Reconciliation Side Cards

```yaml
candidate_card:
  card_type: reconciliation_side
  card_id: reconciliation_side.flipkart.oms_expected
  name: Flipkart oms_expected
  fields:
    profile_id: reconciliation_profile.flipkart.oms_settlement
    side_role: expected
    source_table: table.flipkart.oms
    grain: order/item or settlement line
    key_columns: 
      - order_id
      - item_id
    amount_columns: 
      - charged_amount
    filters: 
      - is_active = true where applicable
    sign_handling: preserve source sign; compare after documented aggregation
    evidence_refs: 
      - evidence.flipkart.query_patterns
    confidence: high
    review_status: accepted
```

```yaml
candidate_card:
  card_type: reconciliation_side
  card_id: reconciliation_side.flipkart.settlement_actual
  name: Flipkart settlement_actual
  fields:
    profile_id: reconciliation_profile.flipkart.oms_settlement
    side_role: actual
    source_table: table.flipkart.settlement
    grain: order/item or settlement line
    key_columns: 
      - order_id
      - item_id
    amount_columns: 
      - settled_amount
      - sale_settled_amount
    filters: 
      - is_active = true where applicable
    sign_handling: preserve source sign; compare after documented aggregation
    evidence_refs: 
      - evidence.flipkart.query_patterns
    confidence: high
    review_status: accepted
```

```yaml
candidate_card:
  card_type: reconciliation_side
  card_id: reconciliation_side.flipkart.settlement_fee_actual
  name: Flipkart settlement_fee_actual
  fields:
    profile_id: reconciliation_profile.flipkart.settlement_commission
    side_role: actual
    source_table: table.flipkart.settlement
    grain: order/item or settlement line
    key_columns: 
      - order_id
      - item_id
    amount_columns: 
      - mp_fee
    filters: 
      - is_active = true where applicable
    sign_handling: preserve source sign; compare after documented aggregation
    evidence_refs: 
      - evidence.flipkart.query_patterns
    confidence: high
    review_status: accepted
```

```yaml
candidate_card:
  card_type: reconciliation_side
  card_id: reconciliation_side.flipkart.commission_detail_expected
  name: Flipkart commission_detail_expected
  fields:
    profile_id: reconciliation_profile.flipkart.settlement_commission
    side_role: expected
    source_table: table.flipkart.commission
    grain: order/item or settlement line
    key_columns: 
      - order_id
      - item_id
    amount_columns: 
      - charged_amount
      - total_tax
    filters: 
      - is_active = true where applicable
    sign_handling: preserve source sign; compare after documented aggregation
    evidence_refs: 
      - evidence.flipkart.query_patterns
    confidence: high
    review_status: accepted
```

```yaml
candidate_card:
  card_type: reconciliation_side
  card_id: reconciliation_side.flipkart.cashback_expected
  name: Flipkart cashback_expected
  fields:
    profile_id: reconciliation_profile.flipkart.cashback_settlement_offer
    side_role: expected
    source_table: table.flipkart.cashback
    grain: order/item or settlement line
    key_columns: 
      - order_id
      - item_id
    amount_columns: 
      - charged_amount
    filters: 
      - is_active = true where applicable
    sign_handling: preserve source sign; compare after documented aggregation
    evidence_refs: 
      - evidence.flipkart.query_patterns
    confidence: high
    review_status: accepted
```

```yaml
candidate_card:
  card_type: reconciliation_side
  card_id: reconciliation_side.flipkart.settlement_offer_actual
  name: Flipkart settlement_offer_actual
  fields:
    profile_id: reconciliation_profile.flipkart.cashback_settlement_offer
    side_role: actual
    source_table: table.flipkart.settlement
    grain: order/item or settlement line
    key_columns: 
      - order_id
      - item_id
    amount_columns: 
      - offer_settled_amount
      - offer_adjustment_settled_amount
    filters: 
      - is_active = true where applicable
    sign_handling: preserve source sign; compare after documented aggregation
    evidence_refs: 
      - evidence.flipkart.query_patterns
    confidence: high
    review_status: accepted
```

```yaml
candidate_card:
  card_type: reconciliation_side
  card_id: reconciliation_side.flipkart.settlement_components
  name: Flipkart settlement_components
  fields:
    profile_id: reconciliation_profile.flipkart.settlement_waterfall
    side_role: expected
    source_table: table.flipkart.settlement
    grain: order/item or settlement line
    key_columns:
    - settlement_id
    - order_id
    - item_id
    amount_columns:
    - sale_settled_amount
    - refund_settled_amount
    - offer_settled_amount
    - my_share_settled_amount
    - addon_settled_amount
    - taxes_settled_amount
    - offer_adjustment_settled_amount
    - protection_fund_settled_amount
    - mp_fee
    - gst_on_mp_fees
    - total_tcs_amount
    - total_tds_amount
    filters:
    - is_active = true where applicable
    sign_handling: credits are summed with source sign; fee/tax deductions use ABS where DOCX waterfall expresses them as deductions
    evidence_refs:
    - evidence.flipkart.settlement_logic
    confidence: high
    review_status: accepted
```

```yaml
candidate_card:
  card_type: reconciliation_side
  card_id: reconciliation_side.flipkart.settlement_net
  name: Flipkart settlement_net
  fields:
    profile_id: reconciliation_profile.flipkart.settlement_waterfall
    side_role: actual
    source_table: table.flipkart.settlement
    grain: order/item or settlement line
    key_columns: 
      - settlement_id
      - order_id
      - item_id
    amount_columns: 
      - settled_amount
    filters: 
      - is_active = true where applicable
    sign_handling: preserve source sign; compare after documented aggregation
    evidence_refs: 
      - evidence.flipkart.query_patterns
    confidence: high
    review_status: accepted
```

```yaml
candidate_card:
  card_type: reconciliation_side
  card_id: reconciliation_side.flipkart.order_fee_cashback_expected
  name: Flipkart order_fee_cashback_expected
  fields:
    profile_id: reconciliation_profile.flipkart.cross_table_pipeline
    side_role: expected
    source_table: multiple_marketplace_tables
    grain: order/item or settlement line
    key_columns: 
      - order_id
      - item_id
    amount_columns: 
      - charged_amount
      - mp_fee
      - cashback_amount
    filters: 
      - is_active = true where applicable
    sign_handling: preserve source sign; compare after documented aggregation
    evidence_refs: 
      - evidence.flipkart.query_patterns
    confidence: high
    review_status: accepted
```

```yaml
candidate_card:
  card_type: reconciliation_side
  card_id: reconciliation_side.flipkart.settlement_pipeline_actual
  name: Flipkart settlement_pipeline_actual
  fields:
    profile_id: reconciliation_profile.flipkart.cross_table_pipeline
    side_role: actual
    source_table: table.flipkart.settlement
    grain: order/item or settlement line
    key_columns: 
      - order_id
      - item_id
    amount_columns: 
      - settled_amount
    filters: 
      - is_active = true where applicable
    sign_handling: preserve source sign; compare after documented aggregation
    evidence_refs: 
      - evidence.flipkart.query_patterns
    confidence: high
    review_status: accepted
```

### 5.18 Reconciliation Unit Cards

```yaml
candidate_card:
  card_type: reconciliation_unit
  card_id: reconciliation_unit.flipkart.order_item
  name: Flipkart order_item
  fields:
    unit_name: order item
    unit_grain: order item
    keys: 
      - order_id
      - item_id
    normalization: source order_id + item_id
    aggregation_required: yes for many-side fee/cashback tables
    applicable_profiles: 
      - Flipkart marketplace-internal profiles only
    evidence_refs: 
      - evidence.flipkart.relationships
    confidence: high
    review_status: accepted
```

```yaml
candidate_card:
  card_type: reconciliation_unit
  card_id: reconciliation_unit.flipkart.normalized_order_item
  name: Flipkart normalized_order_item
  fields:
    unit_name: normalized order item
    unit_grain: normalized order item
    keys: 
      - REPLACE(order_id, OD, empty)
      - item_id
    normalization: commission id normalization required
    aggregation_required: yes for many-side fee/cashback tables
    applicable_profiles: 
      - Flipkart marketplace-internal profiles only
    evidence_refs: 
      - evidence.flipkart.relationships
    confidence: high
    review_status: accepted
```

```yaml
candidate_card:
  card_type: reconciliation_unit
  card_id: reconciliation_unit.flipkart.settlement_line
  name: Flipkart settlement_line
  fields:
    unit_name: settlement line
    unit_grain: settlement line
    keys: 
      - settlement_id
      - order_id
      - item_id
    normalization: same-row settlement component check
    aggregation_required: yes for many-side fee/cashback tables
    applicable_profiles: 
      - Flipkart marketplace-internal profiles only
    evidence_refs: 
      - evidence.flipkart.relationships
    confidence: high
    review_status: accepted
```

```yaml
candidate_card:
  card_type: reconciliation_unit
  card_id: reconciliation_unit.flipkart.credit_debit_note_line
  name: Flipkart credit_debit_note_line
  fields:
    unit_name: credit/debit note line
    unit_grain: credit/debit note line
    keys: 
      - credit_debit_note_no
      - order_id
      - item_id
    normalization: cashback document unit
    aggregation_required: yes for many-side fee/cashback tables
    applicable_profiles: 
      - Flipkart marketplace-internal profiles only
    evidence_refs: 
      - evidence.flipkart.relationships
    confidence: high
    review_status: accepted
```

```yaml
candidate_card:
  card_type: reconciliation_unit
  card_id: reconciliation_unit.flipkart.fulfilment_bucket
  name: Flipkart fulfilment_bucket
  fields:
    unit_name: fulfilment bucket
    unit_grain: fulfilment bucket
    keys: 
      - fulfilment_type
      - neft_type
    normalization: aggregate comparison bucket
    aggregation_required: yes for many-side fee/cashback tables
    applicable_profiles: 
      - Flipkart marketplace-internal profiles only
    evidence_refs: 
      - evidence.flipkart.relationships
    confidence: high
    review_status: accepted
```

### 5.19 Matching Logic Cards

```yaml
candidate_card:
  card_type: matching_logic
  card_id: matching_logic.flipkart.oms_settlement
  name: Flipkart oms_settlement
  fields:
    profile_id: reconciliation_profile.flipkart.oms_settlement
    join_keys: 
      - order_id
      - item_id
    normalization: exact after OMS schema review
    pre_aggregation: aggregate commission/cashback details before joining
    comparison_formula: compare OMS amount to sale/settlement amount
    tolerance: review_required
    date_window: review required
    failure_modes: 
      - missing key
      - duplicate many-side rows
      - sign mismatch
      - OD normalization failure
    evidence_refs: 
      - evidence.flipkart.relationships
      - evidence.flipkart.query_patterns
    confidence: medium
    review_status: review_required
```

```yaml
candidate_card:
  card_type: matching_logic
  card_id: matching_logic.flipkart.settlement_commission_od_normalized
  name: Flipkart settlement_commission_od_normalized
  fields:
    profile_id: reconciliation_profile.flipkart.settlement_commission
    join_keys: 
      - commission.order_id = REPLACE(settlement.order_id, OD, empty)
      - item_id
    normalization: OD prefix removal
    pre_aggregation: aggregate commission/cashback details before joining
    comparison_formula: compare ABS/SUM commission fees to settlement mp_fee after sign review
    tolerance: 0.01
    date_window: review required
    failure_modes: 
      - missing key
      - duplicate many-side rows
      - sign mismatch
      - OD normalization failure
    evidence_refs: 
      - evidence.flipkart.relationships
      - evidence.flipkart.query_patterns
    confidence: high
    review_status: accepted
```

```yaml
candidate_card:
  card_type: matching_logic
  card_id: matching_logic.flipkart.cashback_settlement_offer
  name: Flipkart cashback_settlement_offer
  fields:
    profile_id: reconciliation_profile.flipkart.cashback_settlement_offer
    join_keys: 
      - cashback.order_id = settlement.order_id
      - item_id
    normalization: exact order/item; aggregate cashback
    pre_aggregation: aggregate commission/cashback details before joining
    comparison_formula: compare SUM(cashback.charged_amount) to settlement offer fields
    tolerance: 0.01
    date_window: review required
    failure_modes: 
      - missing key
      - duplicate many-side rows
      - sign mismatch
      - OD normalization failure
    evidence_refs: 
      - evidence.flipkart.relationships
      - evidence.flipkart.query_patterns
    confidence: high
    review_status: accepted
```

```yaml
candidate_card:
  card_type: matching_logic
  card_id: matching_logic.flipkart.settlement_waterfall
  name: Flipkart settlement_waterfall
  fields:
    profile_id: reconciliation_profile.flipkart.settlement_waterfall
    join_keys:
    - settlement_id
    - order_id
    - item_id
    normalization: same row
    pre_aggregation: same-row component calculation; aggregate only after row-level component expression is formed
    comparison_formula: component_sum = sale + refund + offer + my_share + addon + taxes + offer_adjustment + protection_fund - ABS(mp_fee) -
      ABS(gst_on_mp_fees) - ABS(total_tcs_amount) - ABS(total_tds_amount); compare component_sum to settled_amount
    tolerance: review_required
    date_window: review required
    failure_modes:
    - missing key
    - duplicate many-side rows
    - sign mismatch
    - OD normalization failure
    evidence_refs:
    - evidence.flipkart.settlement_logic
    confidence: high
    review_status: review_required
```

```yaml
candidate_card:
  card_type: matching_logic
  card_id: matching_logic.flipkart.cross_table_pipeline
  name: Flipkart cross_table_pipeline
  fields:
    profile_id: reconciliation_profile.flipkart.cross_table_pipeline
    join_keys: 
      - normalized order_id
      - item_id
    normalization: OD normalization plus pre-aggregation
    pre_aggregation: aggregate commission/cashback details before joining
    comparison_formula: compare expected marketplace financial stack to settlement actual
    tolerance: review_required
    date_window: review required
    failure_modes: 
      - missing key
      - duplicate many-side rows
      - sign mismatch
      - OD normalization failure
    evidence_refs: 
      - evidence.flipkart.relationships
      - evidence.flipkart.query_patterns
    confidence: medium
    review_status: review_required
```

### 5.20 Mismatch Category Cards

```yaml
candidate_card:
  card_type: mismatch_category
  card_id: mismatch_category.flipkart.missing_settlement
  name: Missing Settlement
  fields:
    category_name: missing_settlement
    definition: Order/cashback/fee line has no matching settlement row
    detection_rule: left join actual side is null
    likely_causes: 
      - source timing
      - sign convention
      - missing row
      - join key mismatch
      - aggregation error
    severity: medium
    recommended_output_fields: 
      - order_id
      - item_id
      - expected_amount
      - actual_amount
      - variance_amount
      - variance_reason
    evidence_refs: 
      - evidence.flipkart.query_patterns
    confidence: high
    review_status: accepted
```

```yaml
candidate_card:
  card_type: mismatch_category
  card_id: mismatch_category.flipkart.sale_amount_variance
  name: Sale Amount Variance
  fields:
    category_name: sale_amount_variance
    definition: OMS/order sales amount does not match settlement sale component
    detection_rule: ABS(expected - actual) > tolerance
    likely_causes: 
      - source timing
      - sign convention
      - missing row
      - join key mismatch
      - aggregation error
    severity: medium
    recommended_output_fields: 
      - order_id
      - item_id
      - expected_amount
      - actual_amount
      - variance_amount
      - variance_reason
    evidence_refs: 
      - evidence.flipkart.query_patterns
    confidence: high
    review_status: accepted
```

```yaml
candidate_card:
  card_type: mismatch_category
  card_id: mismatch_category.flipkart.mp_fee_variance
  name: Mp Fee Variance
  fields:
    category_name: mp_fee_variance
    definition: Commission detail sum does not match settlement mp_fee
    detection_rule: ABS(detail_fee - settlement_mp_fee) > tolerance
    likely_causes: 
      - source timing
      - sign convention
      - missing row
      - join key mismatch
      - aggregation error
    severity: medium
    recommended_output_fields: 
      - order_id
      - item_id
      - expected_amount
      - actual_amount
      - variance_amount
      - variance_reason
    evidence_refs: 
      - evidence.flipkart.query_patterns
    confidence: high
    review_status: accepted
```

```yaml
candidate_card:
  card_type: mismatch_category
  card_id: mismatch_category.flipkart.missing_fee_detail
  name: Missing Fee Detail
  fields:
    category_name: missing_fee_detail
    definition: Settlement mp_fee exists but no matching commission fee detail
    detection_rule: fee side null
    likely_causes: 
      - source timing
      - sign convention
      - missing row
      - join key mismatch
      - aggregation error
    severity: medium
    recommended_output_fields: 
      - order_id
      - item_id
      - expected_amount
      - actual_amount
      - variance_amount
      - variance_reason
    evidence_refs: 
      - evidence.flipkart.query_patterns
    confidence: high
    review_status: accepted
```

```yaml
candidate_card:
  card_type: mismatch_category
  card_id: mismatch_category.flipkart.cashback_offer_variance
  name: Cashback Offer Variance
  fields:
    category_name: cashback_offer_variance
    definition: Cashback/promotional amount does not match settlement offer fields
    detection_rule: ABS(cashback_sum - offer_sum) > tolerance
    likely_causes: 
      - source timing
      - sign convention
      - missing row
      - join key mismatch
      - aggregation error
    severity: medium
    recommended_output_fields: 
      - order_id
      - item_id
      - expected_amount
      - actual_amount
      - variance_amount
      - variance_reason
    evidence_refs: 
      - evidence.flipkart.query_patterns
    confidence: high
    review_status: accepted
```

```yaml
candidate_card:
  card_type: mismatch_category
  card_id: mismatch_category.flipkart.null_cashback_classification
  name: Null Cashback Classification
  fields:
    category_name: null_cashback_classification
    definition: Cashback document type/subtype is null
    detection_rule: document_type IS NULL OR document_sub_type IS NULL
    likely_causes: 
      - source timing
      - sign convention
      - missing row
      - join key mismatch
      - aggregation error
    severity: medium
    recommended_output_fields: 
      - order_id
      - item_id
      - expected_amount
      - actual_amount
      - variance_amount
      - variance_reason
    evidence_refs: 
      - evidence.flipkart.query_patterns
    confidence: high
    review_status: accepted
```

```yaml
candidate_card:
  card_type: mismatch_category
  card_id: mismatch_category.flipkart.settlement_waterfall_imbalance
  name: Settlement Waterfall Imbalance
  fields:
    category_name: settlement_waterfall_imbalance
    definition: Settlement components do not reconcile to settled_amount
    detection_rule: ABS(component_sum - settled_amount) > tolerance
    likely_causes: 
      - source timing
      - sign convention
      - missing row
      - join key mismatch
      - aggregation error
    severity: medium
    recommended_output_fields: 
      - order_id
      - item_id
      - expected_amount
      - actual_amount
      - variance_amount
      - variance_reason
    evidence_refs: 
      - evidence.flipkart.query_patterns
    confidence: high
    review_status: accepted
```

```yaml
candidate_card:
  card_type: mismatch_category
  card_id: mismatch_category.flipkart.tax_deduction_variance
  name: Tax Deduction Variance
  fields:
    category_name: tax_deduction_variance
    definition: TCS/TDS/GST component inconsistent with expected calculation
    detection_rule: tax comparison fails after source rule is known
    likely_causes: 
      - source timing
      - sign convention
      - missing row
      - join key mismatch
      - aggregation error
    severity: medium
    recommended_output_fields: 
      - order_id
      - item_id
      - expected_amount
      - actual_amount
      - variance_amount
      - variance_reason
    evidence_refs: 
      - evidence.flipkart.query_patterns
    confidence: high
    review_status: accepted
```

```yaml
candidate_card:
  card_type: mismatch_category
  card_id: mismatch_category.flipkart.order_id_normalization_failure
  name: Order Id Normalization Failure
  fields:
    category_name: order_id_normalization_failure
    definition: Commission order_id join fails because OD prefix was not normalized
    detection_rule: commission rows unmatched until OD normalization applied
    likely_causes: 
      - source timing
      - sign convention
      - missing row
      - join key mismatch
      - aggregation error
    severity: medium
    recommended_output_fields: 
      - order_id
      - item_id
      - expected_amount
      - actual_amount
      - variance_amount
      - variance_reason
    evidence_refs: 
      - evidence.flipkart.query_patterns
    confidence: high
    review_status: accepted
```

```yaml
candidate_card:
  card_type: mismatch_category
  card_id: mismatch_category.flipkart.active_filter_omitted
  name: Active Filter Omitted
  fields:
    category_name: active_filter_omitted
    definition: Inactive rows included in metric/reconciliation
    detection_rule: query lacks is_active = true
    likely_causes: 
      - source timing
      - sign convention
      - missing row
      - join key mismatch
      - aggregation error
    severity: medium
    recommended_output_fields: 
      - order_id
      - item_id
      - expected_amount
      - actual_amount
      - variance_amount
      - variance_reason
    evidence_refs: 
      - evidence.flipkart.query_patterns
    confidence: high
    review_status: accepted
```

### 5.21 Reconciliation Variant Cards

```yaml
candidate_card:
  card_type: reconciliation_variant
  card_id: reconciliation_variant.flipkart.commission_od_normalized
  name: Flipkart commission_od_normalized
  fields:
    base_profile: reconciliation_profile.flipkart.settlement_commission
    variant_condition: commission order_id lacks OD prefix
    variant_matching_change: requires REPLACE on settlement/OMS/cashback order_id before join
    variant_tolerance: same as base profile unless source says otherwise
    evidence_refs: 
      - evidence.flipkart.shopsy
      - evidence.flipkart.relationships
    confidence: high
    review_status: accepted
```

```yaml
candidate_card:
  card_type: reconciliation_variant
  card_id: reconciliation_variant.flipkart.cashback_offer_adjustment
  name: Flipkart cashback_offer_adjustment
  fields:
    base_profile: reconciliation_profile.flipkart.cashback_settlement_offer
    variant_condition: offer adjustment fields included
    variant_matching_change: compare cashback to offer_settled_amount + offer_adjustment_settled_amount
    variant_tolerance: same as base profile unless source says otherwise
    evidence_refs: 
      - evidence.flipkart.shopsy
      - evidence.flipkart.relationships
    confidence: high
    review_status: accepted
```

```yaml
candidate_card:
  card_type: reconciliation_variant
  card_id: reconciliation_variant.flipkart.settlement_waterfall_same_row
  name: Flipkart settlement_waterfall_same_row
  fields:
    base_profile: reconciliation_profile.flipkart.settlement_waterfall
    variant_condition: same-row settlement component check
    variant_matching_change: no external join; review sign formula
    variant_tolerance: same as base profile unless source says otherwise
    evidence_refs: 
      - evidence.flipkart.shopsy
      - evidence.flipkart.relationships
    confidence: high
    review_status: accepted
```

```yaml
candidate_card:
  card_type: reconciliation_variant
  card_id: reconciliation_variant.flipkart.shopsy_zero_commission
  name: Flipkart shopsy_zero_commission
  fields:
    base_profile: reconciliation_profile.flipkart.settlement_commission
    variant_condition: Shopsy rows may have zero/altered commission behavior
    variant_matching_change: expect commission behavior differences under is_shopsy_order_ = true
    variant_tolerance: same as base profile unless source says otherwise
    evidence_refs: 
      - evidence.flipkart.shopsy
      - evidence.flipkart.relationships
    confidence: medium
    review_status: review_required
```

### 5.22 Query Pattern Cards

```yaml
candidate_card:
  card_type: query_pattern
  card_id: query_pattern.flipkart.gmv
  name: GMV / gross sales / topline
  fields:
    query_intent: GMV / gross sales / topline
    colloquial_phrases: 
      - GMV
      - gross sales
      - gross revenue
      - topline
    canonical_metric_or_object: metric.gross_merchandise_value
    required_tables: 
      - table.flipkart.oms
      - table.flipkart.settlement
    required_filters: 
      - is_active = true where available
    group_by_options: 
      - date/month
      - fulfilment_type
      - neft_type
      - description
      - document_type
      - is_shopsy_order_
    time_basis: settlement_date for settlement, created_date for cashback, created_date fallback for OMS/commission
    join_requirements: 
      - use relationship cards; pre-aggregate many-side tables
    sql_pattern_ref: sql.flipkart.monthly_settlement
    evidence_refs: 
      - evidence.flipkart.query_patterns
    confidence: high
    review_status: accepted
```

```yaml
candidate_card:
  card_type: query_pattern
  card_id: query_pattern.flipkart.net_settlement
  name: Net payout / settlement amount
  fields:
    query_intent: Net payout / settlement amount
    colloquial_phrases: 
      - settlement amount
      - payout
      - net settlement
    canonical_metric_or_object: metric.net_settlement
    required_tables: 
      - table.flipkart.settlement
    required_filters: 
      - is_active = true where available
    group_by_options: 
      - date/month
      - fulfilment_type
      - neft_type
      - description
      - document_type
      - is_shopsy_order_
    time_basis: settlement_date for settlement, created_date for cashback, created_date fallback for OMS/commission
    join_requirements: 
      - use relationship cards; pre-aggregate many-side tables
    sql_pattern_ref: sql.flipkart.monthly_settlement
    evidence_refs: 
      - evidence.flipkart.query_patterns
    confidence: high
    review_status: accepted
```

```yaml
candidate_card:
  card_type: query_pattern
  card_id: query_pattern.flipkart.realization
  name: Realization rate
  fields:
    query_intent: Realization rate
    colloquial_phrases: 
      - realization
      - seller realization
      - payout percent
    canonical_metric_or_object: metric.realization_rate
    required_tables: 
      - table.flipkart.settlement
    required_filters: 
      - is_active = true where available
    group_by_options: 
      - date/month
      - fulfilment_type
      - neft_type
      - description
      - document_type
      - is_shopsy_order_
    time_basis: settlement_date for settlement, created_date for cashback, created_date fallback for OMS/commission
    join_requirements: 
      - use relationship cards; pre-aggregate many-side tables
    sql_pattern_ref: sql.flipkart.realization_rate
    evidence_refs: 
      - evidence.flipkart.query_patterns
    confidence: high
    review_status: accepted
```

```yaml
candidate_card:
  card_type: query_pattern
  card_id: query_pattern.flipkart.settlement_by_fulfilment
  name: Settlement by fulfilment
  fields:
    query_intent: Settlement by fulfilment
    colloquial_phrases: 
      - FBF vs NFBF
      - fulfilment settlement
      - seller easy ship
    canonical_metric_or_object: metric.net_settlement
    required_tables: 
      - table.flipkart.settlement
    required_filters: 
      - is_active = true where available
    group_by_options: 
      - date/month
      - fulfilment_type
      - neft_type
      - description
      - document_type
      - is_shopsy_order_
    time_basis: settlement_date for settlement, created_date for cashback, created_date fallback for OMS/commission
    join_requirements: 
      - use relationship cards; pre-aggregate many-side tables
    sql_pattern_ref: sql.flipkart.settlement_by_fulfilment
    evidence_refs: 
      - evidence.flipkart.query_patterns
    confidence: high
    review_status: accepted
```

```yaml
candidate_card:
  card_type: query_pattern
  card_id: query_pattern.flipkart.settlement_cycle
  name: Settlement cycle / payout lag
  fields:
    query_intent: Settlement cycle / payout lag
    colloquial_phrases: 
      - settlement lag
      - payout lag
      - cash cycle
    canonical_metric_or_object: metric.settlement_cycle_days
    required_tables: 
      - table.flipkart.settlement
    required_filters: 
      - is_active = true where available
    group_by_options: 
      - date/month
      - fulfilment_type
      - neft_type
      - description
      - document_type
      - is_shopsy_order_
    time_basis: settlement_date for settlement, created_date for cashback, created_date fallback for OMS/commission
    join_requirements: 
      - use relationship cards; pre-aggregate many-side tables
    sql_pattern_ref: sql.flipkart.settlement_cycle
    evidence_refs: 
      - evidence.flipkart.query_patterns
    confidence: high
    review_status: accepted
```

```yaml
candidate_card:
  card_type: query_pattern
  card_id: query_pattern.flipkart.fee_breakdown
  name: Fee breakdown
  fields:
    query_intent: Fee breakdown
    colloquial_phrases: 
      - commission breakup
      - fee breakup
      - deduction breakup
    canonical_metric_or_object: metric.marketplace_fee_total
    required_tables: 
      - table.flipkart.commission
    required_filters: 
      - is_active = true where available
    group_by_options: 
      - date/month
      - fulfilment_type
      - neft_type
      - description
      - document_type
      - is_shopsy_order_
    time_basis: settlement_date for settlement, created_date for cashback, created_date fallback for OMS/commission
    join_requirements: 
      - use relationship cards; pre-aggregate many-side tables
    sql_pattern_ref: sql.flipkart.fee_by_description
    evidence_refs: 
      - evidence.flipkart.query_patterns
    confidence: high
    review_status: accepted
```

```yaml
candidate_card:
  card_type: query_pattern
  card_id: query_pattern.flipkart.fee_pivot
  name: Fee pivot by order/item
  fields:
    query_intent: Fee pivot by order/item
    colloquial_phrases: 
      - commission fee
      - fixed fee
      - shipping fee
      - collection fee
    canonical_metric_or_object: metric.marketplace_fee_total
    required_tables: 
      - table.flipkart.commission
    required_filters: 
      - is_active = true where available
    group_by_options: 
      - date/month
      - fulfilment_type
      - neft_type
      - description
      - document_type
      - is_shopsy_order_
    time_basis: settlement_date for settlement, created_date for cashback, created_date fallback for OMS/commission
    join_requirements: 
      - use relationship cards; pre-aggregate many-side tables
    sql_pattern_ref: sql.flipkart.fee_pivot
    evidence_refs: 
      - evidence.flipkart.query_patterns
    confidence: high
    review_status: accepted
```

```yaml
candidate_card:
  card_type: query_pattern
  card_id: query_pattern.flipkart.commission_recon
  name: Settlement vs commission reconciliation
  fields:
    query_intent: Settlement vs commission reconciliation
    colloquial_phrases: 
      - mp_fee mismatch
      - fee reconciliation
      - commission variance
    canonical_metric_or_object: reconciliation_profile.flipkart.settlement_commission
    required_tables: 
      - table.flipkart.settlement
      - table.flipkart.commission
    required_filters: 
      - is_active = true where available
    group_by_options: 
      - date/month
      - fulfilment_type
      - neft_type
      - description
      - document_type
      - is_shopsy_order_
    time_basis: settlement_date for settlement, created_date for cashback, created_date fallback for OMS/commission
    join_requirements: 
      - use relationship cards; pre-aggregate many-side tables
    sql_pattern_ref: sql.flipkart.settlement_commission_recon
    evidence_refs: 
      - evidence.flipkart.query_patterns
    confidence: high
    review_status: accepted
```

```yaml
candidate_card:
  card_type: query_pattern
  card_id: query_pattern.flipkart.cashback
  name: Cashback / promotion amount
  fields:
    query_intent: Cashback / promotion amount
    colloquial_phrases: 
      - cashback
      - offer amount
      - promo subsidy
    canonical_metric_or_object: metric.net_cashback
    required_tables: 
      - table.flipkart.cashback
    required_filters: 
      - is_active = true where available
    group_by_options: 
      - date/month
      - fulfilment_type
      - neft_type
      - description
      - document_type
      - is_shopsy_order_
    time_basis: settlement_date for settlement, created_date for cashback, created_date fallback for OMS/commission
    join_requirements: 
      - use relationship cards; pre-aggregate many-side tables
    sql_pattern_ref: sql.flipkart.cashback_net
    evidence_refs: 
      - evidence.flipkart.query_patterns
    confidence: high
    review_status: accepted
```

```yaml
candidate_card:
  card_type: query_pattern
  card_id: query_pattern.flipkart.cashback_doc_type
  name: Cashback by document type
  fields:
    query_intent: Cashback by document type
    colloquial_phrases: 
      - credit note
      - debit note
      - cashback return
    canonical_metric_or_object: metric.net_cashback
    required_tables: 
      - table.flipkart.cashback
    required_filters: 
      - is_active = true where available
    group_by_options: 
      - date/month
      - fulfilment_type
      - neft_type
      - description
      - document_type
      - is_shopsy_order_
    time_basis: settlement_date for settlement, created_date for cashback, created_date fallback for OMS/commission
    join_requirements: 
      - use relationship cards; pre-aggregate many-side tables
    sql_pattern_ref: sql.flipkart.cashback_doc_type
    evidence_refs: 
      - evidence.flipkart.query_patterns
    confidence: high
    review_status: accepted
```

```yaml
candidate_card:
  card_type: query_pattern
  card_id: query_pattern.flipkart.cashback_rate
  name: Cashback percentage
  fields:
    query_intent: Cashback percentage
    colloquial_phrases: 
      - cashback rate
      - offer rate
      - promo percent
    canonical_metric_or_object: metric.cashback_rate
    required_tables: 
      - table.flipkart.cashback
      - table.flipkart.oms
    required_filters: 
      - is_active = true where available
    group_by_options: 
      - date/month
      - fulfilment_type
      - neft_type
      - description
      - document_type
      - is_shopsy_order_
    time_basis: settlement_date for settlement, created_date for cashback, created_date fallback for OMS/commission
    join_requirements: 
      - use relationship cards; pre-aggregate many-side tables
    sql_pattern_ref: sql.flipkart.cashback_rate
    evidence_refs: 
      - evidence.flipkart.query_patterns
    confidence: high
    review_status: accepted
```

```yaml
candidate_card:
  card_type: query_pattern
  card_id: query_pattern.flipkart.shopsy_cashback
  name: Shopsy cashback
  fields:
    query_intent: Shopsy cashback
    colloquial_phrases: 
      - Shopsy cashback
      - Shopsy offers
    canonical_metric_or_object: metric.net_cashback
    required_tables: 
      - table.flipkart.cashback
    required_filters: 
      - is_active = true where available
    group_by_options: 
      - date/month
      - fulfilment_type
      - neft_type
      - description
      - document_type
      - is_shopsy_order_
    time_basis: settlement_date for settlement, created_date for cashback, created_date fallback for OMS/commission
    join_requirements: 
      - use relationship cards; pre-aggregate many-side tables
    sql_pattern_ref: sql.flipkart.shopsy_cashback
    evidence_refs: 
      - evidence.flipkart.query_patterns
    confidence: high
    review_status: accepted
```

```yaml
candidate_card:
  card_type: query_pattern
  card_id: query_pattern.flipkart.cashback_offer_recon
  name: Cashback vs settlement offer reconciliation
  fields:
    query_intent: Cashback vs settlement offer reconciliation
    colloquial_phrases: 
      - offer mismatch
      - cashback settlement variance
    canonical_metric_or_object: reconciliation_profile.flipkart.cashback_settlement_offer
    required_tables: 
      - table.flipkart.cashback
      - table.flipkart.settlement
    required_filters: 
      - is_active = true where available
    group_by_options: 
      - date/month
      - fulfilment_type
      - neft_type
      - description
      - document_type
      - is_shopsy_order_
    time_basis: settlement_date for settlement, created_date for cashback, created_date fallback for OMS/commission
    join_requirements: 
      - use relationship cards; pre-aggregate many-side tables
    sql_pattern_ref: sql.flipkart.cashback_settlement_offer_recon
    evidence_refs: 
      - evidence.flipkart.query_patterns
    confidence: high
    review_status: accepted
```

```yaml
candidate_card:
  card_type: query_pattern
  card_id: query_pattern.flipkart.tcs_tds
  name: TCS/TDS deductions
  fields:
    query_intent: TCS/TDS deductions
    colloquial_phrases: 
      - TCS
      - TDS
      - tax deduction
    canonical_metric_or_object: metric.tcs_deducted
    required_tables: 
      - table.flipkart.settlement
    required_filters: 
      - is_active = true where available
    group_by_options: 
      - date/month
      - fulfilment_type
      - neft_type
      - description
      - document_type
      - is_shopsy_order_
    time_basis: settlement_date for settlement, created_date for cashback, created_date fallback for OMS/commission
    join_requirements: 
      - use relationship cards; pre-aggregate many-side tables
    sql_pattern_ref: sql.flipkart.monthly_settlement
    evidence_refs: 
      - evidence.flipkart.query_patterns
    confidence: high
    review_status: accepted
```

```yaml
candidate_card:
  card_type: query_pattern
  card_id: query_pattern.flipkart.gst_fees
  name: GST on marketplace fees
  fields:
    query_intent: GST on marketplace fees
    colloquial_phrases: 
      - GST on fees
      - fee tax
    canonical_metric_or_object: metric.gst_on_marketplace_fees
    required_tables: 
      - table.flipkart.settlement
      - table.flipkart.commission
    required_filters: 
      - is_active = true where available
    group_by_options: 
      - date/month
      - fulfilment_type
      - neft_type
      - description
      - document_type
      - is_shopsy_order_
    time_basis: settlement_date for settlement, created_date for cashback, created_date fallback for OMS/commission
    join_requirements: 
      - use relationship cards; pre-aggregate many-side tables
    sql_pattern_ref: sql.flipkart.fee_by_description
    evidence_refs: 
      - evidence.flipkart.query_patterns
    confidence: high
    review_status: accepted
```

### 5.23 Rule Cards

```yaml
candidate_card:
  card_type: rule
  card_id: rule.flipkart.active_filter
  name: Flipkart active_filter
  fields:
    rule_name: active_filter
    rule_type: active_row_filter
    rule_statement: Always apply is_active = true on Flipkart source tables when computing metrics or reconciliation.
    applies_to: 
      - Flipkart marketplace clean markdown and downstream parser
    severity: high
    deterministic_action: enforce or emit review item
    exceptions: 
      - only if source DOCX explicitly overrides with stronger evidence
    evidence_refs: 
      - evidence.flipkart.query_patterns
      - evidence.flipkart.relationships
    confidence: high
    review_status: accepted
```

```yaml
candidate_card:
  card_type: rule
  card_id: rule.flipkart.group_scope_as_column
  name: Flipkart group_scope_as_column
  fields:
    rule_name: group_scope_as_column
    rule_type: scope_column_only
    rule_statement: group_level_id/group_id are columns/caveats only; do not create account or hierarchy cards.
    applies_to: 
      - Flipkart marketplace clean markdown and downstream parser
    severity: high
    deterministic_action: enforce or emit review item
    exceptions: 
      - only if source DOCX explicitly overrides with stronger evidence
    evidence_refs: 
      - evidence.flipkart.query_patterns
      - evidence.flipkart.relationships
    confidence: high
    review_status: accepted
```

```yaml
candidate_card:
  card_type: rule
  card_id: rule.flipkart.commission_od_normalization
  name: Flipkart commission_od_normalization
  fields:
    rule_name: commission_od_normalization
    rule_type: join_normalization
    rule_statement: Commission order_id lacks OD prefix; normalize OD-prefixed order ids before joining.
    applies_to: 
      - Flipkart marketplace clean markdown and downstream parser
    severity: high
    deterministic_action: enforce or emit review item
    exceptions: 
      - only if source DOCX explicitly overrides with stronger evidence
    evidence_refs: 
      - evidence.flipkart.query_patterns
      - evidence.flipkart.relationships
    confidence: high
    review_status: accepted
```

```yaml
candidate_card:
  card_type: rule
  card_id: rule.flipkart.preaggregate_many_side
  name: Flipkart preaggregate_many_side
  fields:
    rule_name: preaggregate_many_side
    rule_type: aggregation
    rule_statement: Pre-aggregate commission/cashback by order_id,item_id before joining to settlement/OMS.
    applies_to: 
      - Flipkart marketplace clean markdown and downstream parser
    severity: medium
    deterministic_action: enforce or emit review item
    exceptions: 
      - only if source DOCX explicitly overrides with stronger evidence
    evidence_refs: 
      - evidence.flipkart.query_patterns
      - evidence.flipkart.relationships
    confidence: high
    review_status: accepted
```

```yaml
candidate_card:
  card_type: rule
  card_id: rule.flipkart.cashback_signed
  name: Flipkart cashback_signed
  fields:
    rule_name: cashback_signed
    rule_type: sign_semantics
    rule_statement: Cashback charged_amount is signed; preserve reverse/cancel signs.
    applies_to: 
      - Flipkart marketplace clean markdown and downstream parser
    severity: medium
    deterministic_action: enforce or emit review item
    exceptions: 
      - only if source DOCX explicitly overrides with stronger evidence
    evidence_refs: 
      - evidence.flipkart.query_patterns
      - evidence.flipkart.relationships
    confidence: high
    review_status: accepted
```

```yaml
candidate_card:
  card_type: rule
  card_id: rule.flipkart.mp_fee_preferred
  name: Flipkart mp_fee_preferred
  fields:
    rule_name: mp_fee_preferred
    rule_type: metric_source_preference
    rule_statement: Use settlement mp_fee for aggregate fee impact; use commission table for detailed fee class breakdown.
    applies_to: 
      - Flipkart marketplace clean markdown and downstream parser
    severity: medium
    deterministic_action: enforce or emit review item
    exceptions: 
      - only if source DOCX explicitly overrides with stronger evidence
    evidence_refs: 
      - evidence.flipkart.query_patterns
      - evidence.flipkart.relationships
    confidence: high
    review_status: accepted
```

```yaml
candidate_card:
  card_type: rule
  card_id: rule.flipkart.string_fee_columns
  name: Flipkart string_fee_columns
  fields:
    rule_name: string_fee_columns
    rule_type: type_cast
    rule_statement: Legacy fee_amount/fee_waiver_amount/base_price/commission_rate fields require casting before numeric use.
    applies_to: 
      - Flipkart marketplace clean markdown and downstream parser
    severity: medium
    deterministic_action: enforce or emit review item
    exceptions: 
      - only if source DOCX explicitly overrides with stronger evidence
    evidence_refs: 
      - evidence.flipkart.query_patterns
      - evidence.flipkart.relationships
    confidence: high
    review_status: accepted
```

```yaml
candidate_card:
  card_type: rule
  card_id: rule.flipkart.tcs_tds_not_cost
  name: Flipkart tcs_tds_not_cost
  fields:
    rule_name: tcs_tds_not_cost
    rule_type: tax_semantics
    rule_statement: TCS/TDS are marketplace cash-flow deductions, not permanent cost metrics by default.
    applies_to: 
      - Flipkart marketplace clean markdown and downstream parser
    severity: medium
    deterministic_action: enforce or emit review item
    exceptions: 
      - only if source DOCX explicitly overrides with stronger evidence
    evidence_refs: 
      - evidence.flipkart.query_patterns
      - evidence.flipkart.relationships
    confidence: high
    review_status: accepted
```

```yaml
candidate_card:
  card_type: rule
  card_id: rule.flipkart.fulfilment_marketplace_only
  name: Flipkart fulfilment_marketplace_only
  fields:
    rule_name: fulfilment_marketplace_only
    rule_type: domain_boundary
    rule_statement: Fulfilment and shipping columns are marketplace fee semantics only, not logistics-domain cards.
    applies_to: 
      - Flipkart marketplace clean markdown and downstream parser
    severity: medium
    deterministic_action: enforce or emit review item
    exceptions: 
      - only if source DOCX explicitly overrides with stronger evidence
    evidence_refs: 
      - evidence.flipkart.query_patterns
      - evidence.flipkart.relationships
    confidence: high
    review_status: accepted
```

```yaml
candidate_card:
  card_type: rule
  card_id: rule.flipkart.shopsy_string_flag
  name: Flipkart shopsy_string_flag
  fields:
    rule_name: shopsy_string_flag
    rule_type: value_semantics
    rule_statement: is_shopsy_order_ should be treated as source string values true/false unless warehouse metadata proves boolean.
    applies_to: 
      - Flipkart marketplace clean markdown and downstream parser
    severity: medium
    deterministic_action: enforce or emit review item
    exceptions: 
      - only if source DOCX explicitly overrides with stronger evidence
    evidence_refs: 
      - evidence.flipkart.query_patterns
      - evidence.flipkart.relationships
    confidence: high
    review_status: accepted
```

```yaml
candidate_card:
  card_type: rule
  card_id: rule.flipkart.no_bank_cards
  name: Flipkart no_bank_cards
  fields:
    rule_name: no_bank_cards
    rule_type: domain_boundary
    rule_statement: Settlement_id, NEFT type, and vendor_payout are marketplace settlement fields, not bank reconciliation cards.
    applies_to: 
      - Flipkart marketplace clean markdown and downstream parser
    severity: medium
    deterministic_action: enforce or emit review item
    exceptions: 
      - only if source DOCX explicitly overrides with stronger evidence
    evidence_refs: 
      - evidence.flipkart.query_patterns
      - evidence.flipkart.relationships
    confidence: high
    review_status: accepted
```

```yaml
candidate_card:
  card_type: rule
  card_id: rule.flipkart.oms_review
  name: Flipkart oms_review
  fields:
    rule_name: oms_review
    rule_type: evidence_quality
    rule_statement: Do not rely on full OMS schema until source inconsistency is resolved.
    applies_to: 
      - Flipkart marketplace clean markdown and downstream parser
    severity: medium
    deterministic_action: enforce or emit review item
    exceptions: 
      - only if source DOCX explicitly overrides with stronger evidence
    evidence_refs: 
      - evidence.flipkart.query_patterns
      - evidence.flipkart.relationships
    confidence: high
    review_status: accepted
```

```yaml
candidate_card:
  card_type: rule
  card_id: rule.flipkart.fulfilment_fee_segmentation
  name: Flipkart fulfilment fee segmentation
  fields:
    rule_name: fulfilment_fee_segmentation
    rule_type: segment_interpretation
    rule_statement: FBF/NON_FBF and flipkart_fulfilment/seller_easy_ship are fulfilment-value segments affecting fixed fee, shipping, visibility,
      and settlement analysis; do not create a process_variant unless source documents different reconciliation matching logic.
    applies_to:
    - value_profile.flipkart.oms.fulfilment_type
    - value_profile.flipkart.settlement.fulfilment_type
    - metric.effective_fee_rate
    - metric.settlement_cycle_days
    severity: medium
    deterministic_action: treat as value_profile/rule-driven segmentation, not a process_variant card
    exceptions:
    - create a process_variant only if a later source documents a distinct process sequence or matching rule
    evidence_refs:
    - evidence.flipkart.fulfilment
    - evidence.flipkart.fee_structure
    confidence: high
    review_status: accepted
```

```yaml
candidate_card:
  card_type: rule
  card_id: rule.flipkart.shopsy_zero_commission
  name: Flipkart Shopsy zero commission rule
  fields:
    rule_name: shopsy_zero_commission
    rule_type: fee_segment_guidance
    rule_statement: Shopsy is identified by is_shopsy_order_ = 'true' and has zero commission on all products; other fees still apply.
    applies_to:
    - value_profile.flipkart.cashback.is_shopsy_order
    - metric.commission_fee
    - metric.effective_fee_rate
    severity: medium
    deterministic_action: use as benchmark/fee interpretation guidance; do not create a Shopsy process_variant or separate non-marketplace domain
    exceptions:
    - hard validation requires account/category/period-specific rate-card evidence
    evidence_refs:
    - evidence.flipkart.shopsy
    - evidence.flipkart.fee_structure
    confidence: high
    review_status: accepted
```

```yaml
candidate_card:
  card_type: rule
  card_id: rule.flipkart.prepaid_postpaid_collection_fee
  name: Flipkart prepaid/postpaid collection fee guidance
  fields:
    rule_name: prepaid_postpaid_collection_fee
    rule_type: fee_segment_guidance
    rule_statement: Collection fee is documented as 2% for Prepaid and 2.5% for Postpaid/COD; neft_type/payment method may segment analysis but
      is not itself a process variant.
    applies_to:
    - value_profile.flipkart.settlement.neft_type
    - metric.collection_fee
    - metric.effective_fee_rate
    severity: medium
    deterministic_action: encode as rule/value-profile guidance; do not create prepaid_vs_postpaid process_variant
    exceptions:
    - hard validation requires current account/category rate-card evidence
    evidence_refs:
    - evidence.flipkart.fee_structure
    - evidence.flipkart.settlement_logic
    confidence: high
    review_status: accepted
```

```yaml
candidate_card:
  card_type: rule
  card_id: rule.flipkart.seller_tier_guidance_only
  name: Flipkart seller-tier guidance only
  fields:
    rule_name: seller_tier_guidance_only
    rule_type: benchmark_scope_guidance
    rule_statement: Seller tier affects fixed-fee level and payout speed conceptually, but the DOCX does not identify a reliable seller-tier schema
      column; do not build seller-tier process cards or tier-specific metric implementations from this markdown alone.
    applies_to:
    - metric.settlement_cycle_days
    - metric.fixed_fee
    - column.settlement.tier
    severity: medium
    deterministic_action: keep seller-tier as contextual guidance/review item unless an explicit seller-tier source column is supplied
    exceptions:
    - external runtime account scope or a later schema source can bind seller tier
    evidence_refs:
    - evidence.flipkart.seller_tier
    confidence: high
    review_status: accepted
```

```yaml
candidate_card:
  card_type: rule
  card_id: rule.flipkart.benchmark_guidance_only
  name: Flipkart benchmark guidance only
  fields:
    rule_name: benchmark_guidance_only
    rule_type: benchmark_policy
    rule_statement: Documented benchmark ranges belong on metric cards as guidance and must not be encoded as hard validation thresholds unless
      a separate account/category/period-specific rule exists.
    applies_to:
    - metric.realization_rate
    - metric.return_rate
    severity: medium
    deterministic_action: include benchmarks on metric cards and block hard-failure validation without additional context
    exceptions:
    - explicit validation_test with account/category/period threshold evidence
    evidence_refs:
    - evidence.flipkart.metrics_benchmarks
    confidence: high
    review_status: accepted
```


### 5.24 Validation Test Cards

```yaml
candidate_card:
  card_type: validation_test
  card_id: validation_test.flipkart.active_filter_present
  name: Flipkart active_filter_present
  fields:
    test_name: active_filter_present
    test_type: semantic_query_validation
    applies_to: metric/query/reconciliation
    test_logic: query must contain is_active = true for source tables that have is_active
    expected_result: Pass when active filter present
    failure_meaning: parser output is not deterministic or violates marketplace-only boundary
    severity: medium
    evidence_refs: 
      - evidence.flipkart.query_patterns
    confidence: high
    review_status: accepted
```

```yaml
candidate_card:
  card_type: validation_test
  card_id: validation_test.flipkart.commission_order_id_normalized
  name: Flipkart commission_order_id_normalized
  fields:
    test_name: commission_order_id_normalized
    test_type: join_validation
    applies_to: commission joins
    test_logic: join must normalize OD prefix when joining commission to settlement/OMS/cashback
    expected_result: Pass when REPLACE/normalization appears
    failure_meaning: parser output is not deterministic or violates marketplace-only boundary
    severity: medium
    evidence_refs: 
      - evidence.flipkart.query_patterns
    confidence: high
    review_status: accepted
```

```yaml
candidate_card:
  card_type: validation_test
  card_id: validation_test.flipkart.commission_preaggregated
  name: Flipkart commission_preaggregated
  fields:
    test_name: commission_preaggregated
    test_type: aggregation_validation
    applies_to: commission joins
    test_logic: commission table must be aggregated to order_id,item_id before amount comparison
    expected_result: Pass when CTE/grouping exists
    failure_meaning: parser output is not deterministic or violates marketplace-only boundary
    severity: medium
    evidence_refs: 
      - evidence.flipkart.query_patterns
    confidence: high
    review_status: accepted
```

```yaml
candidate_card:
  card_type: validation_test
  card_id: validation_test.flipkart.cashback_preaggregated
  name: Flipkart cashback_preaggregated
  fields:
    test_name: cashback_preaggregated
    test_type: aggregation_validation
    applies_to: cashback joins
    test_logic: cashback table must be aggregated to order_id,item_id before amount comparison
    expected_result: Pass when CTE/grouping exists
    failure_meaning: parser output is not deterministic or violates marketplace-only boundary
    severity: medium
    evidence_refs: 
      - evidence.flipkart.query_patterns
    confidence: high
    review_status: accepted
```

```yaml
candidate_card:
  card_type: validation_test
  card_id: validation_test.flipkart.group_not_binding
  name: Flipkart group_not_binding
  fields:
    test_name: group_not_binding
    test_type: scope_validation
    applies_to: all cards
    test_logic: no tenant/group/platform_account/account_data_binding cards created
    expected_result: Pass when forbidden card types absent
    failure_meaning: parser output is not deterministic or violates marketplace-only boundary
    severity: high
    evidence_refs: 
      - evidence.flipkart.query_patterns
    confidence: high
    review_status: accepted
```

```yaml
candidate_card:
  card_type: validation_test
  card_id: validation_test.flipkart.cashback_null_preserved
  name: Flipkart cashback_null_preserved
  fields:
    test_name: cashback_null_preserved
    test_type: value_validation
    applies_to: cashback value profile
    test_logic: document_type and document_sub_type nulls are preserved
    expected_result: Pass when null is listed or source-null policy documented
    failure_meaning: parser output is not deterministic or violates marketplace-only boundary
    severity: medium
    evidence_refs: 
      - evidence.flipkart.query_patterns
    confidence: high
    review_status: accepted
```

```yaml
candidate_card:
  card_type: validation_test
  card_id: validation_test.flipkart.mp_fee_recon
  name: Flipkart mp_fee_recon
  fields:
    test_name: mp_fee_recon
    test_type: reconciliation_validation
    applies_to: settlement_commission profile
    test_logic: settlement mp_fee compared to commission detail after OD normalization
    expected_result: Pass when variance output includes order_id,item_id,mp_fee,detail_fee
    failure_meaning: parser output is not deterministic or violates marketplace-only boundary
    severity: medium
    evidence_refs: 
      - evidence.flipkart.query_patterns
    confidence: high
    review_status: accepted
```

```yaml
candidate_card:
  card_type: validation_test
  card_id: validation_test.flipkart.cashback_offer_recon
  name: Flipkart cashback_offer_recon
  fields:
    test_name: cashback_offer_recon
    test_type: reconciliation_validation
    applies_to: cashback_settlement_offer profile
    test_logic: cashback signed sum compared to offer settlement fields
    expected_result: Pass when variance output includes cashback and settlement offer amounts
    failure_meaning: parser output is not deterministic or violates marketplace-only boundary
    severity: medium
    evidence_refs: 
      - evidence.flipkart.query_patterns
    confidence: high
    review_status: accepted
```

```yaml
candidate_card:
  card_type: validation_test
  card_id: validation_test.flipkart.no_external_logistics
  name: Flipkart no_external_logistics
  fields:
    test_name: no_external_logistics
    test_type: domain_boundary_validation
    applies_to: all cards
    test_logic: no courier/AWB lifecycle or logistics COD cards created
    expected_result: Pass when logistics domain cards absent
    failure_meaning: parser output is not deterministic or violates marketplace-only boundary
    severity: high
    evidence_refs: 
      - evidence.flipkart.query_patterns
    confidence: high
    review_status: accepted
```

```yaml
candidate_card:
  card_type: validation_test
  card_id: validation_test.flipkart.no_bank_recon
  name: Flipkart no_bank_recon
  fields:
    test_name: no_bank_recon
    test_type: domain_boundary_validation
    applies_to: all cards
    test_logic: no bank-credit or UTR-to-bank reconciliation cards created
    expected_result: Pass when bank cards absent
    failure_meaning: parser output is not deterministic or violates marketplace-only boundary
    severity: high
    evidence_refs: 
      - evidence.flipkart.query_patterns
    confidence: high
    review_status: accepted
```

### 5.25 Output Contract Cards

```yaml
candidate_card:
  card_type: output_contract
  card_id: output_contract.flipkart.settlement_summary
  name: Flipkart settlement_summary
  fields:
    contract_name: Settlement summary
    use_case: Settlement summary
    required_fields: 
      - settlement_date/month
      - settled_amount
      - sale_settled_amount
      - mp_fee
      - realization_rate
    recommended_fields: 
      - fulfilment_type
      - neft_type
      - total_tcs_amount
      - total_tds_amount
    grain: as required by use case
    sort_order: 
      - largest variance first for exception outputs
      - date ascending for time series
    metric_columns: 
      - settled_amount
      - sale_settled_amount
      - mp_fee
      - realization_rate
    diagnostic_columns: 
      - order_id
      - item_id
      - variance_reason
      - source_table
    evidence_refs: 
      - evidence.flipkart.query_patterns
    confidence: high
    review_status: accepted
```

```yaml
candidate_card:
  card_type: output_contract
  card_id: output_contract.flipkart.fee_breakdown
  name: Flipkart fee_breakdown
  fields:
    contract_name: Fee breakdown report
    use_case: Fee breakdown report
    required_fields: 
      - description
      - fee_amount
      - fee_tax
    recommended_fields: 
      - order_id
      - item_id
      - fulfilment_type
    grain: as required by use case
    sort_order: 
      - largest variance first for exception outputs
      - date ascending for time series
    metric_columns: 
      - fee_amount
      - fee_tax
    diagnostic_columns: 
      - order_id
      - item_id
      - variance_reason
      - source_table
    evidence_refs: 
      - evidence.flipkart.query_patterns
    confidence: high
    review_status: accepted
```

```yaml
candidate_card:
  card_type: output_contract
  card_id: output_contract.flipkart.commission_recon
  name: Flipkart commission_recon
  fields:
    contract_name: Commission reconciliation exceptions
    use_case: Commission reconciliation exceptions
    required_fields: 
      - order_id
      - item_id
      - settlement_mp_fee
      - commission_fee_total
      - variance
    recommended_fields: 
      - variance_reason
      - description_breakdown
    grain: as required by use case
    sort_order: 
      - largest variance first for exception outputs
      - date ascending for time series
    metric_columns: 
      - settlement_mp_fee
      - commission_fee_total
      - variance
    diagnostic_columns: 
      - order_id
      - item_id
      - variance_reason
      - source_table
    evidence_refs: 
      - evidence.flipkart.query_patterns
    confidence: high
    review_status: accepted
```

```yaml
candidate_card:
  card_type: output_contract
  card_id: output_contract.flipkart.cashback_recon
  name: Flipkart cashback_recon
  fields:
    contract_name: Cashback reconciliation exceptions
    use_case: Cashback reconciliation exceptions
    required_fields: 
      - order_id
      - item_id
      - cashback_amount
      - settlement_offer_amount
      - variance
    recommended_fields: 
      - document_type
      - document_sub_type
      - transaction_type
    grain: as required by use case
    sort_order: 
      - largest variance first for exception outputs
      - date ascending for time series
    metric_columns: 
      - cashback_amount
      - settlement_offer_amount
      - variance
    diagnostic_columns: 
      - order_id
      - item_id
      - variance_reason
      - source_table
    evidence_refs: 
      - evidence.flipkart.query_patterns
    confidence: high
    review_status: accepted
```

```yaml
candidate_card:
  card_type: output_contract
  card_id: output_contract.flipkart.settlement_cycle
  name: Flipkart settlement_cycle
  fields:
    contract_name: Settlement cycle report
    use_case: Settlement cycle report
    required_fields: 
      - settlement_date
      - avg_settlement_cycle_days
    recommended_fields: 
      - fulfilment_type
      - neft_type
    grain: as required by use case
    sort_order: 
      - largest variance first for exception outputs
      - date ascending for time series
    metric_columns: []
    diagnostic_columns: 
      - order_id
      - item_id
      - variance_reason
      - source_table
    evidence_refs: 
      - evidence.flipkart.query_patterns
    confidence: high
    review_status: accepted
```

```yaml
candidate_card:
  card_type: output_contract
  card_id: output_contract.flipkart.shopsy_comparison
  name: Flipkart shopsy_comparison
  fields:
    contract_name: Shopsy comparison
    use_case: Shopsy comparison
    required_fields: 
      - is_shopsy_order_
      - cashback_amount
      - rows
    recommended_fields: 
      - commission_fee
      - settlement_amount
      - realization_rate
    grain: as required by use case
    sort_order: 
      - largest variance first for exception outputs
      - date ascending for time series
    metric_columns: 
      - cashback_amount
    diagnostic_columns: 
      - order_id
      - item_id
      - variance_reason
      - source_table
    evidence_refs: 
      - evidence.flipkart.query_patterns
    confidence: high
    review_status: accepted
```

### 5.26 Execution Constraint Set Cards

```yaml
candidate_card:
  card_type: execution_constraint_set
  card_id: execution_constraint_set.flipkart.marketplace_only
  name: Marketplace-only extraction boundary
  fields:
    constraint_name: Marketplace-only extraction boundary
    applies_to: 
      - Flipkart marketplace parser-ready markdown
    semantic_constraints: 
      - emit only allowed marketplace card types
      - do not emit forbidden card types
    aggregation_order: 
      - filter active rows
      - normalize keys
      - pre-aggregate many-side tables
      - join/compare
      - compute metrics
    date_window_rules: 
      - only use source-provided date windows; otherwise mark review
    filter_rules: 
      - do not add tenant/account filters from marketplace doc
    join_rules: 
      - use relationship cards
    sign_rules: 
      - source sign preserving
    out_of_scope_runtime_constraints: 
      - no runtime/infra constraints
    evidence_refs: 
      - evidence.flipkart.query_patterns
    confidence: high
    review_status: accepted
```

```yaml
candidate_card:
  card_type: execution_constraint_set
  card_id: execution_constraint_set.flipkart.active_filters
  name: Active row filters
  fields:
    constraint_name: Active row filters
    applies_to: 
      - Flipkart marketplace parser-ready markdown
    semantic_constraints: 
      - apply is_active = true when available
    aggregation_order: 
      - filter active rows
      - normalize keys
      - pre-aggregate many-side tables
      - join/compare
      - compute metrics
    date_window_rules: 
      - only use source-provided date windows; otherwise mark review
    filter_rules: 
      - do not add tenant/account filters from marketplace doc
    join_rules: 
      - use relationship cards
    sign_rules: 
      - source sign preserving
    out_of_scope_runtime_constraints: 
      - no account filters in marketplace doc
    evidence_refs: 
      - evidence.flipkart.query_patterns
    confidence: high
    review_status: accepted
```

```yaml
candidate_card:
  card_type: execution_constraint_set
  card_id: execution_constraint_set.flipkart.preaggregation
  name: Pre-aggregation before joins
  fields:
    constraint_name: Pre-aggregation before joins
    applies_to: 
      - Flipkart marketplace parser-ready markdown
    semantic_constraints: 
      - aggregate commission and cashback by order_id,item_id before joins
    aggregation_order: 
      - filter active rows
      - normalize keys
      - pre-aggregate many-side tables
      - join/compare
      - compute metrics
    date_window_rules: 
      - only use source-provided date windows; otherwise mark review
    filter_rules: 
      - do not add tenant/account filters from marketplace doc
    join_rules: 
      - use relationship cards
    sign_rules: 
      - source sign preserving
    out_of_scope_runtime_constraints: 
      - avoid double counting
    evidence_refs: 
      - evidence.flipkart.query_patterns
    confidence: high
    review_status: accepted
```

```yaml
candidate_card:
  card_type: execution_constraint_set
  card_id: execution_constraint_set.flipkart.order_id_normalization
  name: Order id normalization
  fields:
    constraint_name: Order id normalization
    applies_to: 
      - Flipkart marketplace parser-ready markdown
    semantic_constraints: 
      - normalize OD prefix for commission joins
    aggregation_order: 
      - filter active rows
      - normalize keys
      - pre-aggregate many-side tables
      - join/compare
      - compute metrics
    date_window_rules: 
      - only use source-provided date windows; otherwise mark review
    filter_rules: 
      - do not add tenant/account filters from marketplace doc
    join_rules: 
      - use relationship cards
    sign_rules: 
      - source sign preserving
    out_of_scope_runtime_constraints: 
      - do not normalize away meaningful non-OD characters
    evidence_refs: 
      - evidence.flipkart.query_patterns
    confidence: high
    review_status: accepted
```

```yaml
candidate_card:
  card_type: execution_constraint_set
  card_id: execution_constraint_set.flipkart.sign_handling
  name: Sign handling
  fields:
    constraint_name: Sign handling
    applies_to: 
      - Flipkart marketplace parser-ready markdown
    semantic_constraints: 
      - preserve cashback/reverse/refund signs
      - use ABS only for presentational fee burden
    aggregation_order: 
      - filter active rows
      - normalize keys
      - pre-aggregate many-side tables
      - join/compare
      - compute metrics
    date_window_rules: 
      - only use source-provided date windows; otherwise mark review
    filter_rules: 
      - do not add tenant/account filters from marketplace doc
    join_rules: 
      - use relationship cards
    sign_rules: 
      - source sign preserving
    out_of_scope_runtime_constraints: 
      - do not flatten signed data
    evidence_refs: 
      - evidence.flipkart.query_patterns
    confidence: high
    review_status: accepted
```

```yaml
candidate_card:
  card_type: execution_constraint_set
  card_id: execution_constraint_set.flipkart.date_basis
  name: Date basis
  fields:
    constraint_name: Date basis
    applies_to: 
      - Flipkart marketplace parser-ready markdown
    semantic_constraints: 
      - settlement_date for settlement metrics
      - created_date for cashback
      - created_date fallback for cycle metric
    aggregation_order: 
      - filter active rows
      - normalize keys
      - pre-aggregate many-side tables
      - join/compare
      - compute metrics
    date_window_rules: 
      - only use source-provided date windows; otherwise mark review
    filter_rules: 
      - do not add tenant/account filters from marketplace doc
    join_rules: 
      - use relationship cards
    sign_rules: 
      - source sign preserving
    out_of_scope_runtime_constraints: 
      - dispatch date requires source review
    evidence_refs: 
      - evidence.flipkart.query_patterns
    confidence: high
    review_status: accepted
```

```yaml
candidate_card:
  card_type: execution_constraint_set
  card_id: execution_constraint_set.flipkart.tax_boundary
  name: Tax boundary
  fields:
    constraint_name: Tax boundary
    applies_to: 
      - Flipkart marketplace parser-ready markdown
    semantic_constraints: 
      - TCS/TDS/GST are marketplace deduction fields only
    aggregation_order: 
      - filter active rows
      - normalize keys
      - pre-aggregate many-side tables
      - join/compare
      - compute metrics
    date_window_rules: 
      - only use source-provided date windows; otherwise mark review
    filter_rules: 
      - do not add tenant/account filters from marketplace doc
    join_rules: 
      - use relationship cards
    sign_rules: 
      - source sign preserving
    out_of_scope_runtime_constraints: 
      - no statutory filing cards
    evidence_refs: 
      - evidence.flipkart.query_patterns
    confidence: high
    review_status: accepted
```

```yaml
candidate_card:
  card_type: execution_constraint_set
  card_id: execution_constraint_set.flipkart.fulfilment_boundary
  name: Fulfilment boundary
  fields:
    constraint_name: Fulfilment boundary
    applies_to: 
      - Flipkart marketplace parser-ready markdown
    semantic_constraints: 
      - fulfilment/shipping fields remain marketplace fee semantics
    aggregation_order: 
      - filter active rows
      - normalize keys
      - pre-aggregate many-side tables
      - join/compare
      - compute metrics
    date_window_rules: 
      - only use source-provided date windows; otherwise mark review
    filter_rules: 
      - do not add tenant/account filters from marketplace doc
    join_rules: 
      - use relationship cards
    sign_rules: 
      - source sign preserving
    out_of_scope_runtime_constraints: 
      - no external logistics cards
    evidence_refs: 
      - evidence.flipkart.query_patterns
    confidence: high
    review_status: accepted
```

## 6. Candidate Edges — Unified Edge Taxonomy

> This section replaces the mixed old/new edge registry with a single umbrella taxonomy. Each `candidate_edge` uses a canonical uppercase `edge_type`, keeps any older parser-helper label in `legacy_edge_aliases`, and declares `inverse_edge_type` plus whether the inverse should be physically materialized.
>
> Dual-side rule: core containment and membership edges are materialized in both directions. Usage/provenance edges remain single directed edges with reverse lookup through graph indexes unless `materialize_inverse: true` is set.
>
> Marketplace-only exclusions remain active: this file does not create tenant, group, platform account, account data binding, business scope, business flow, bank, logistics, payment-gateway, ERP/accounting, or statutory-filing edges.

### 6.0 Unified Edge Rules

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
      - HAS_VALUE_PROFILE <-> PROFILES_COLUMN_OR_PROFILES_TABLE
      - HAS_IMPLEMENTATION <-> IMPLEMENTS_METRIC
      - HAS_BUSINESS_PROCESS <-> BELONGS_TO_DOMAIN_FOR_PROCESS
      - HAS_WORKFLOW_STEP <-> BELONGS_TO_PROCESS
      - HAS_STATE_TRANSITION <-> BELONGS_TO_PROCESS
      - HAS_PROCESS_VARIANT <-> EXTENDS_PROCESS
      - HAS_RECONCILIATION_PROFILE <-> SUPPORTS_PROCESS
      - HAS_RECONCILIATION_SIDE <-> BELONGS_TO_RECONCILIATION_PROFILE
      - USES_MATCHING_LOGIC <-> SUPPORTS_RECONCILIATION_PROFILE
      - RULE_HAS_VALIDATION_TEST <-> VALIDATION_TEST_ENFORCES_RULE
    index_reverse_lookup_only:
      - SOURCED_FROM_PLATFORM
      - SOURCED_FROM_PLATFORM_CONTEXT
      - APPLIES_TO_PLATFORM
      - APPLIES_TO_PLATFORM_CONTEXT
      - USES_TABLE
      - USES_COLUMN
      - USES_FORMULA_TEMPLATE
      - DEPENDS_ON_METRIC
      - PRODUCES_METRIC
      - USES_RECONCILIATION_PROFILE
      - REQUIRES_RULE
      - USES_OUTPUT_CONTRACT
      - INCLUDES_RULE
      - INCLUDES_VALIDATION_TEST
      - APPLIES_TO_QUERY_PATTERN
  parser_helper_policy:
    retain_parser_helper_edges: true
    parser_helper_edges_may_be_collapsed_into_fields: true
    parser_helper_edge_class: parser_helper
```

### 6.1 Unified Edge Taxonomy Registry

```yaml
unified_edge_taxonomy_registry:
- edge_type: HAS_PLATFORM_CONTEXT
  source_type: platform
  target_type: platform_context
  inverse_edge_type: BELONGS_TO_PLATFORM
  materialize_inverse_default: true
- edge_type: BELONGS_TO_PLATFORM
  source_type: platform_context
  target_type: platform
  inverse_edge_type: HAS_PLATFORM_CONTEXT
  materialize_inverse_default: true
- edge_type: SOURCED_FROM_PLATFORM
  source_type: table
  target_type: platform
  inverse_edge_type: HAS_SOURCE_TABLE
  materialize_inverse_default: false
- edge_type: SOURCED_FROM_PLATFORM_CONTEXT
  source_type: table
  target_type: platform_context
  inverse_edge_type: HAS_SOURCE_TABLE
  materialize_inverse_default: false
- edge_type: APPLIES_TO_PLATFORM
  source_type: any_marketplace_card
  target_type: platform
  inverse_edge_type: HAS_APPLICABLE_CARD
  materialize_inverse_default: false
- edge_type: APPLIES_TO_PLATFORM_CONTEXT
  source_type: any_marketplace_card
  target_type: platform_context
  inverse_edge_type: HAS_APPLICABLE_CARD
  materialize_inverse_default: false
- edge_type: HAS_COLUMN
  source_type: table
  target_type: column
  inverse_edge_type: BELONGS_TO_TABLE
  materialize_inverse_default: true
- edge_type: BELONGS_TO_TABLE
  source_type: column
  target_type: table
  inverse_edge_type: HAS_COLUMN
  materialize_inverse_default: true
  legacy_aliases:
  - column_belongs_to_table
- edge_type: HAS_VALUE_PROFILE
  source_type: table_or_column
  target_type: value_profile
  inverse_edge_type: PROFILES_COLUMN_or_PROFILES_TABLE
  materialize_inverse_default: true
- edge_type: PROFILES_COLUMN
  source_type: value_profile
  target_type: column
  inverse_edge_type: HAS_VALUE_PROFILE
  materialize_inverse_default: true
  legacy_aliases:
  - value_profile_describes_column
- edge_type: PROFILES_TABLE
  source_type: value_profile
  target_type: table
  inverse_edge_type: HAS_VALUE_PROFILE
  materialize_inverse_default: true
- edge_type: HAS_RELATIONSHIP
  source_type: table
  target_type: relationship
  inverse_edge_type: RELATIONSHIP_OF_TABLE
  materialize_inverse_default: false
- edge_type: SOURCE_TABLE
  source_type: relationship
  target_type: table
  inverse_edge_type: SOURCE_OF_RELATIONSHIP
  materialize_inverse_default: false
- edge_type: TARGET_TABLE
  source_type: relationship
  target_type: table
  inverse_edge_type: TARGET_OF_RELATIONSHIP
  materialize_inverse_default: false
- edge_type: USES_SOURCE_COLUMN
  source_type: relationship
  target_type: column
  inverse_edge_type: SOURCE_COLUMN_OF_RELATIONSHIP
  materialize_inverse_default: false
- edge_type: USES_TARGET_COLUMN
  source_type: relationship
  target_type: column
  inverse_edge_type: TARGET_COLUMN_OF_RELATIONSHIP
  materialize_inverse_default: false
- edge_type: HAS_IMPLEMENTATION
  source_type: metric
  target_type: metric_implementation
  inverse_edge_type: IMPLEMENTS_METRIC
  materialize_inverse_default: true
- edge_type: IMPLEMENTS_METRIC
  source_type: metric_implementation
  target_type: metric
  inverse_edge_type: HAS_IMPLEMENTATION
  materialize_inverse_default: true
  legacy_aliases:
  - implements_metric
- edge_type: USES_TABLE
  source_type: metric_implementation_or_query_pattern_or_business_process_or_reconciliation_side
  target_type: table
  inverse_edge_type: USED_BY_*
  materialize_inverse_default: false
  legacy_aliases:
  - implementation_uses_table
  - query_requires_table
  - process_uses_table
  - side_uses_table
- edge_type: USES_COLUMN
  source_type: metric_implementation_or_reconciliation_side
  target_type: column
  inverse_edge_type: USED_BY_*
  materialize_inverse_default: false
  legacy_aliases:
  - implementation_uses_column
  - side_uses_key_column
  - side_uses_amount_column
- edge_type: USES_FORMULA_TEMPLATE
  source_type: metric_implementation
  target_type: formula_template
  inverse_edge_type: USED_BY_IMPLEMENTATION
  materialize_inverse_default: false
- edge_type: DEPENDS_ON_METRIC
  source_type: metric
  target_type: metric
  inverse_edge_type: DEPENDENCY_OF_METRIC
  materialize_inverse_default: false
  legacy_aliases:
  - metric_depends_on_metric
- edge_type: PARENT_METRIC
  source_type: metric_dependency
  target_type: metric
  inverse_edge_type: HAS_METRIC_DEPENDENCY
  materialize_inverse_default: false
- edge_type: USES_DEPENDENT_METRIC
  source_type: metric_dependency
  target_type: metric
  inverse_edge_type: DEPENDENCY_USED_BY
  materialize_inverse_default: false
- edge_type: BELONGS_TO_DOMAIN
  source_type: metric_or_business_process
  target_type: domain
  inverse_edge_type: HAS_METRIC_or_HAS_BUSINESS_PROCESS
  materialize_inverse_default: true_for_business_process_false_for_metric
- edge_type: HAS_BUSINESS_PROCESS
  source_type: domain
  target_type: business_process
  inverse_edge_type: BELONGS_TO_DOMAIN
  materialize_inverse_default: true
- edge_type: HAS_WORKFLOW_STEP
  source_type: business_process
  target_type: workflow_step
  inverse_edge_type: BELONGS_TO_PROCESS
  materialize_inverse_default: true
- edge_type: BELONGS_TO_PROCESS
  source_type: workflow_step_or_state_transition
  target_type: business_process
  inverse_edge_type: HAS_WORKFLOW_STEP_or_HAS_STATE_TRANSITION
  materialize_inverse_default: true
  legacy_aliases:
  - step_in_process
  - transition_in_process
- edge_type: HAS_STATE_TRANSITION
  source_type: business_process
  target_type: state_transition
  inverse_edge_type: BELONGS_TO_PROCESS
  materialize_inverse_default: true
- edge_type: TRIGGERED_BY_STEP
  source_type: state_transition
  target_type: workflow_step
  inverse_edge_type: TRIGGERS_TRANSITION
  materialize_inverse_default: false
- edge_type: HAS_PROCESS_VARIANT
  source_type: business_process
  target_type: process_variant
  inverse_edge_type: EXTENDS_PROCESS
  materialize_inverse_default: true
- edge_type: EXTENDS_PROCESS
  source_type: process_variant
  target_type: business_process
  inverse_edge_type: HAS_PROCESS_VARIANT
  materialize_inverse_default: true
- edge_type: HAS_RECONCILIATION_PROFILE
  source_type: business_process
  target_type: reconciliation_profile
  inverse_edge_type: SUPPORTS_PROCESS
  materialize_inverse_default: true
- edge_type: SUPPORTS_PROCESS
  source_type: reconciliation_profile
  target_type: business_process
  inverse_edge_type: HAS_RECONCILIATION_PROFILE
  materialize_inverse_default: true
- edge_type: HAS_RECONCILIATION_SIDE
  source_type: reconciliation_profile
  target_type: reconciliation_side
  inverse_edge_type: BELONGS_TO_RECONCILIATION_PROFILE
  materialize_inverse_default: true
  legacy_aliases:
  - profile_expected_side
  - profile_actual_side
  edge_properties:
    side_role: expected_or_actual
- edge_type: BELONGS_TO_RECONCILIATION_PROFILE
  source_type: reconciliation_side
  target_type: reconciliation_profile
  inverse_edge_type: HAS_RECONCILIATION_SIDE
  materialize_inverse_default: true
- edge_type: HAS_PRIMARY_UNIT
  source_type: reconciliation_profile
  target_type: reconciliation_unit
  inverse_edge_type: PRIMARY_UNIT_OF_PROFILE
  materialize_inverse_default: false
  legacy_aliases:
  - profile_uses_unit
- edge_type: HAS_SECONDARY_UNIT
  source_type: reconciliation_profile
  target_type: reconciliation_unit
  inverse_edge_type: SECONDARY_UNIT_OF_PROFILE
  materialize_inverse_default: false
- edge_type: USES_MATCHING_LOGIC
  source_type: reconciliation_profile
  target_type: matching_logic
  inverse_edge_type: SUPPORTS_RECONCILIATION_PROFILE
  materialize_inverse_default: true
  legacy_aliases:
  - profile_uses_matching_logic
- edge_type: SUPPORTS_RECONCILIATION_PROFILE
  source_type: matching_logic
  target_type: reconciliation_profile
  inverse_edge_type: USES_MATCHING_LOGIC
  materialize_inverse_default: true
- edge_type: HAS_MISMATCH_CATEGORY
  source_type: reconciliation_profile
  target_type: mismatch_category
  inverse_edge_type: MISMATCH_OF_PROFILE
  materialize_inverse_default: false
  legacy_aliases:
  - profile_has_mismatch_category
- edge_type: EXTENDS_RECONCILIATION_PROFILE
  source_type: reconciliation_variant
  target_type: reconciliation_profile
  inverse_edge_type: HAS_RECONCILIATION_VARIANT
  materialize_inverse_default: false
- edge_type: OVERRIDES_MATCHING_LOGIC
  source_type: reconciliation_variant
  target_type: matching_logic
  inverse_edge_type: OVERRIDDEN_BY_VARIANT
  materialize_inverse_default: false
- edge_type: PRODUCES_METRIC
  source_type: query_pattern
  target_type: metric
  inverse_edge_type: PRODUCED_BY_QUERY_PATTERN
  materialize_inverse_default: false
  legacy_aliases:
  - query_targets_card
- edge_type: USES_RECONCILIATION_PROFILE
  source_type: query_pattern
  target_type: reconciliation_profile
  inverse_edge_type: USED_BY_QUERY_PATTERN
  materialize_inverse_default: false
  legacy_aliases:
  - query_targets_card
- edge_type: USES_RELATIONSHIP
  source_type: query_pattern
  target_type: relationship
  inverse_edge_type: USED_BY_QUERY_PATTERN
  materialize_inverse_default: false
- edge_type: REQUIRES_RULE
  source_type: query_pattern
  target_type: rule
  inverse_edge_type: REQUIRED_BY_QUERY_PATTERN
  materialize_inverse_default: false
  legacy_aliases:
  - query_targets_card
- edge_type: HAS_VALIDATION_TEST
  source_type: query_pattern_or_rule
  target_type: validation_test
  inverse_edge_type: VALIDATES_QUERY_PATTERN_or_ENFORCES_RULE
  materialize_inverse_default: true_only_for_rule_to_validation
- edge_type: ENFORCES_RULE
  source_type: validation_test
  target_type: rule
  inverse_edge_type: HAS_VALIDATION_TEST
  materialize_inverse_default: true
- edge_type: USES_OUTPUT_CONTRACT
  source_type: query_pattern_or_execution_constraint_set
  target_type: output_contract
  inverse_edge_type: USED_BY_QUERY_PATTERN_or_USED_BY_CONSTRAINT_SET
  materialize_inverse_default: false
- edge_type: INCLUDES_RULE
  source_type: execution_constraint_set
  target_type: rule
  inverse_edge_type: INCLUDED_IN_CONSTRAINT_SET
  materialize_inverse_default: false
  legacy_aliases:
  - rule_enforced_by_constraint
- edge_type: INCLUDES_VALIDATION_TEST
  source_type: execution_constraint_set
  target_type: validation_test
  inverse_edge_type: INCLUDED_IN_CONSTRAINT_SET
  materialize_inverse_default: false
  legacy_aliases:
  - validation_enforces_constraint
- edge_type: APPLIES_TO_QUERY_PATTERN
  source_type: execution_constraint_set
  target_type: query_pattern
  inverse_edge_type: HAS_EXECUTION_CONSTRAINT_SET
  materialize_inverse_default: false
- edge_type: TARGETS_CARD
  source_type: query_pattern
  target_type: any_canonical_card
  inverse_edge_type: TARGETED_BY_QUERY_PATTERN
  materialize_inverse_default: false
  legacy_aliases:
  - query_targets_card
  edge_class: parser_helper
```

### 6.2 Legacy Alias Normalization Registry

```yaml
edge_normalization_registry:
- legacy_edge_alias: column_belongs_to_table
  canonical_edge_type: BELONGS_TO_TABLE
  source_type: column
  target_type: table
  inverse_edge_type: HAS_COLUMN
  materialize_inverse_default: true
  canonical_cognee_edge: true
- legacy_edge_alias: value_profile_describes_column
  canonical_edge_type: PROFILES_COLUMN
  source_type: value_profile
  target_type: column
  inverse_edge_type: HAS_VALUE_PROFILE
  materialize_inverse_default: true
  canonical_cognee_edge: true
- legacy_edge_alias: implementation_uses_table
  canonical_edge_type: USES_TABLE
  source_type: metric_implementation
  target_type: table
  inverse_edge_type: USED_BY_IMPLEMENTATION
  materialize_inverse_default: false
  canonical_cognee_edge: true
- legacy_edge_alias: implementation_uses_column
  canonical_edge_type: USES_COLUMN
  source_type: metric_implementation
  target_type: column
  inverse_edge_type: USED_BY_IMPLEMENTATION
  materialize_inverse_default: false
  canonical_cognee_edge: true
- legacy_edge_alias: implements_metric
  canonical_edge_type: IMPLEMENTS_METRIC
  source_type: metric_implementation
  target_type: metric
  inverse_edge_type: HAS_IMPLEMENTATION
  materialize_inverse_default: true
  canonical_cognee_edge: true
- legacy_edge_alias: metric_depends_on_metric
  canonical_edge_type: DEPENDS_ON_METRIC
  source_type: metric
  target_type: metric
  inverse_edge_type: DEPENDENCY_OF_METRIC
  materialize_inverse_default: false
  canonical_cognee_edge: true
- legacy_edge_alias: query_targets_card
  canonical_edge_type: TARGETS_CARD
  source_type: query_pattern
  target_type: any_canonical_card
  inverse_edge_type: TARGETED_BY_QUERY_PATTERN
  materialize_inverse_default: false
  canonical_cognee_edge: false
  parser_note: Fallback only; specialize to PRODUCES_METRIC, USES_RECONCILIATION_PROFILE, USES_OUTPUT_CONTRACT, REQUIRES_RULE, or HAS_VALIDATION_TEST when target
    type is known.
- legacy_edge_alias: query_requires_table
  canonical_edge_type: USES_TABLE
  source_type: query_pattern
  target_type: table
  inverse_edge_type: USED_BY_QUERY_PATTERN
  materialize_inverse_default: false
  canonical_cognee_edge: true
- legacy_edge_alias: process_uses_table
  canonical_edge_type: USES_TABLE
  source_type: business_process
  target_type: table
  inverse_edge_type: USED_BY_PROCESS
  materialize_inverse_default: false
  canonical_cognee_edge: false
- legacy_edge_alias: step_in_process
  canonical_edge_type: BELONGS_TO_PROCESS
  source_type: workflow_step
  target_type: business_process
  inverse_edge_type: HAS_WORKFLOW_STEP
  materialize_inverse_default: true
  canonical_cognee_edge: true
- legacy_edge_alias: transition_in_process
  canonical_edge_type: BELONGS_TO_PROCESS
  source_type: state_transition
  target_type: business_process
  inverse_edge_type: HAS_STATE_TRANSITION
  materialize_inverse_default: true
  canonical_cognee_edge: true
- legacy_edge_alias: profile_expected_side
  canonical_edge_type: HAS_RECONCILIATION_SIDE
  source_type: reconciliation_profile
  target_type: reconciliation_side
  inverse_edge_type: BELONGS_TO_RECONCILIATION_PROFILE
  materialize_inverse_default: true
  canonical_cognee_edge: true
  edge_properties:
    side_role: expected
- legacy_edge_alias: profile_actual_side
  canonical_edge_type: HAS_RECONCILIATION_SIDE
  source_type: reconciliation_profile
  target_type: reconciliation_side
  inverse_edge_type: BELONGS_TO_RECONCILIATION_PROFILE
  materialize_inverse_default: true
  canonical_cognee_edge: true
  edge_properties:
    side_role: actual
- legacy_edge_alias: profile_uses_unit
  canonical_edge_type: HAS_PRIMARY_UNIT
  source_type: reconciliation_profile
  target_type: reconciliation_unit
  inverse_edge_type: PRIMARY_UNIT_OF_PROFILE
  materialize_inverse_default: false
  canonical_cognee_edge: true
- legacy_edge_alias: profile_uses_matching_logic
  canonical_edge_type: USES_MATCHING_LOGIC
  source_type: reconciliation_profile
  target_type: matching_logic
  inverse_edge_type: SUPPORTS_RECONCILIATION_PROFILE
  materialize_inverse_default: true
  canonical_cognee_edge: true
- legacy_edge_alias: profile_has_mismatch_category
  canonical_edge_type: HAS_MISMATCH_CATEGORY
  source_type: reconciliation_profile
  target_type: mismatch_category
  inverse_edge_type: MISMATCH_OF_PROFILE
  materialize_inverse_default: false
  canonical_cognee_edge: true
- legacy_edge_alias: side_uses_table
  canonical_edge_type: USES_TABLE
  source_type: reconciliation_side
  target_type: table
  inverse_edge_type: USED_BY_RECONCILIATION_SIDE
  materialize_inverse_default: false
  canonical_cognee_edge: false
- legacy_edge_alias: side_uses_key_column
  canonical_edge_type: USES_COLUMN
  source_type: reconciliation_side
  target_type: column
  inverse_edge_type: USED_BY_RECONCILIATION_SIDE
  materialize_inverse_default: false
  canonical_cognee_edge: false
  edge_properties:
    column_role: key
- legacy_edge_alias: side_uses_amount_column
  canonical_edge_type: USES_COLUMN
  source_type: reconciliation_side
  target_type: column
  inverse_edge_type: USED_BY_RECONCILIATION_SIDE
  materialize_inverse_default: false
  canonical_cognee_edge: false
  edge_properties:
    column_role: amount
- legacy_edge_alias: validation_enforces_constraint
  canonical_edge_type: INCLUDES_VALIDATION_TEST
  source_type: execution_constraint_set
  target_type: validation_test
  inverse_edge_type: INCLUDED_IN_CONSTRAINT_SET
  materialize_inverse_default: false
  canonical_cognee_edge: true
  parser_note: Legacy direction is reversed during canonicalization; canonical source is execution_constraint_set.
- legacy_edge_alias: rule_enforced_by_constraint
  canonical_edge_type: INCLUDES_RULE
  source_type: execution_constraint_set
  target_type: rule
  inverse_edge_type: INCLUDED_IN_CONSTRAINT_SET
  materialize_inverse_default: false
  canonical_cognee_edge: true
  parser_note: Legacy direction is reversed during canonicalization; canonical source is execution_constraint_set.
```

### 6.3 Edge Coverage Summary

```yaml
edge_coverage_summary:
  source_design: Unified marketplace edge taxonomy derived from Cognee KB Design v4 §8 plus legacy parser-helper aliases
  cards: 293
  edges: 889
  canonical_cognee_edges: 814
  parser_helper_edges: 75
  edges_with_legacy_aliases: 409
  materialized_inverse_edges_added: 21
  edges_marked_for_inverse_materialization: 387
  isolated_cards_after_edge_build: 0
  missing_edge_references: 0
  edge_families:
    applicability: 59
    business_hierarchy_in_scope: 2
    data_understanding: 280
    execution_guidance: 187
    execution_guidance_derived: 5
    metric_understanding: 161
    metric_understanding_derived: 1
    process_understanding: 63
    process_understanding_derived: 28
    reconciliation_understanding: 56
    reconciliation_understanding_derived: 47
  edge_types:
    APPLIES_TO_PLATFORM: 21
    APPLIES_TO_PLATFORM_CONTEXT: 38
    APPLIES_TO_QUERY_PATTERN: 46
    BELONGS_TO_DOMAIN: 29
    BELONGS_TO_PLATFORM: 1
    BELONGS_TO_PROCESS: 13
    BELONGS_TO_RECONCILIATION_PROFILE: 11
    BELONGS_TO_TABLE: 92
    DEPENDS_ON_METRIC: 8
    ENFORCES_RULE: 10
    EXTENDS_PROCESS: 4
    EXTENDS_RECONCILIATION_PROFILE: 4
    HAS_BUSINESS_PROCESS: 7
    HAS_COLUMN: 92
    HAS_IMPLEMENTATION: 21
    HAS_MISMATCH_CATEGORY: 5
    HAS_PLATFORM_CONTEXT: 1
    HAS_PRIMARY_UNIT: 5
    HAS_PROCESS_VARIANT: 4
    HAS_RECONCILIATION_PROFILE: 5
    HAS_RECONCILIATION_SIDE: 11
    HAS_RELATIONSHIP: 12
    HAS_STATE_TRANSITION: 5
    HAS_VALIDATION_TEST: 27
    HAS_VALUE_PROFILE: 20
    HAS_WORKFLOW_STEP: 8
    IMPLEMENTS_METRIC: 21
    INCLUDES_RULE: 9
    INCLUDES_VALIDATION_TEST: 9
    PARENT_METRIC: 5
    PRODUCES_METRIC: 13
    PROFILES_COLUMN: 10
    PROFILES_TABLE: 10
    REQUIRES_RULE: 28
    SOURCED_FROM_PLATFORM: 4
    SOURCED_FROM_PLATFORM_CONTEXT: 4
    SOURCE_TABLE: 6
    SUPPORTS_PROCESS: 5
    SUPPORTS_RECONCILIATION_PROFILE: 5
    TARGET_TABLE: 6
    USED_IN_PROCESS: 15
    USES_COLUMN: 68
    USES_DEPENDENT_METRIC: 8
    USES_FORMULA_TEMPLATE: 10
    USES_MATCHING_LOGIC: 5
    USES_METRIC: 15
    USES_OUTPUT_CONTRACT: 23
    USES_RECONCILIATION_PROFILE: 2
    USES_RELATIONSHIP: 5
    USES_SOURCE_COLUMN: 12
    USES_TABLE: 79
    USES_TARGET_COLUMN: 12
  isolated_card_ids: []
  missing_reference_ids: []
```

### 6.4 Candidate Edge Registry

```yaml
candidate_edge:
  edge_id: edge.platform.flipkart.has_platform_context.platform_context.flipkart.in
  edge_type: HAS_PLATFORM_CONTEXT
  source: platform.flipkart
  target: platform_context.flipkart.in
  fields:
    edge_family: business_hierarchy_in_scope
    evidence_basis: platform.fields.supported_contexts
    confidence: high
    canonical_cognee_edge: true
    marketplace_only: true
    canonical_edge_type: HAS_PLATFORM_CONTEXT
    inverse_edge_type: BELONGS_TO_PLATFORM
    materialize_inverse: true
    edge_class: canonical
    source_type: platform
    target_type: platform_context
```

```yaml
candidate_edge:
  edge_id: edge.platform_context.flipkart.in.belongs_to_platform.platform.flipkart
  edge_type: BELONGS_TO_PLATFORM
  source: platform_context.flipkart.in
  target: platform.flipkart
  fields:
    edge_family: business_hierarchy_in_scope
    evidence_basis: platform_context.fields.platform_id
    confidence: high
    canonical_cognee_edge: true
    marketplace_only: true
    canonical_edge_type: BELONGS_TO_PLATFORM
    inverse_edge_type: HAS_PLATFORM_CONTEXT
    materialize_inverse: true
    edge_class: canonical
    source_type: platform_context
    target_type: platform
```

```yaml
candidate_edge:
  edge_id: edge.metric_implementation.flipkart.gmv.oms.applies_to_platform_context.platform_context.flipkart.in
  edge_type: APPLIES_TO_PLATFORM_CONTEXT
  source: metric_implementation.flipkart.gmv.oms
  target: platform_context.flipkart.in
  fields:
    edge_family: applicability
    evidence_basis: metric_implementation.fields.platform_context
    confidence: high
    canonical_cognee_edge: true
    marketplace_only: true
    canonical_edge_type: APPLIES_TO_PLATFORM_CONTEXT
    inverse_edge_type: HAS_APPLICABLE_CARD
    materialize_inverse: false
    edge_class: canonical
    source_type: metric_implementation
    target_type: platform_context
```

```yaml
candidate_edge:
  edge_id: edge.metric_implementation.flipkart.gmv.oms.applies_to_platform.platform.flipkart
  edge_type: APPLIES_TO_PLATFORM
  source: metric_implementation.flipkart.gmv.oms
  target: platform.flipkart
  fields:
    edge_family: applicability
    evidence_basis: derived from platform_context.flipkart.in
    confidence: high
    canonical_cognee_edge: true
    marketplace_only: true
    canonical_edge_type: APPLIES_TO_PLATFORM
    inverse_edge_type: HAS_APPLICABLE_CARD
    materialize_inverse: false
    edge_class: canonical
    source_type: metric_implementation
    target_type: platform
```

```yaml
candidate_edge:
  edge_id: edge.metric_implementation.flipkart.gmv.settlement_fallback.applies_to_platform_context.platform_context.flipkart.in
  edge_type: APPLIES_TO_PLATFORM_CONTEXT
  source: metric_implementation.flipkart.gmv.settlement_fallback
  target: platform_context.flipkart.in
  fields:
    edge_family: applicability
    evidence_basis: metric_implementation.fields.platform_context
    confidence: high
    canonical_cognee_edge: true
    marketplace_only: true
    canonical_edge_type: APPLIES_TO_PLATFORM_CONTEXT
    inverse_edge_type: HAS_APPLICABLE_CARD
    materialize_inverse: false
    edge_class: canonical
    source_type: metric_implementation
    target_type: platform_context
```

```yaml
candidate_edge:
  edge_id: edge.metric_implementation.flipkart.gmv.settlement_fallback.applies_to_platform.platform.flipkart
  edge_type: APPLIES_TO_PLATFORM
  source: metric_implementation.flipkart.gmv.settlement_fallback
  target: platform.flipkart
  fields:
    edge_family: applicability
    evidence_basis: derived from platform_context.flipkart.in
    confidence: high
    canonical_cognee_edge: true
    marketplace_only: true
    canonical_edge_type: APPLIES_TO_PLATFORM
    inverse_edge_type: HAS_APPLICABLE_CARD
    materialize_inverse: false
    edge_class: canonical
    source_type: metric_implementation
    target_type: platform
```

```yaml
candidate_edge:
  edge_id: edge.metric_implementation.flipkart.net_settlement.applies_to_platform_context.platform_context.flipkart.in
  edge_type: APPLIES_TO_PLATFORM_CONTEXT
  source: metric_implementation.flipkart.net_settlement
  target: platform_context.flipkart.in
  fields:
    edge_family: applicability
    evidence_basis: metric_implementation.fields.platform_context
    confidence: high
    canonical_cognee_edge: true
    marketplace_only: true
    canonical_edge_type: APPLIES_TO_PLATFORM_CONTEXT
    inverse_edge_type: HAS_APPLICABLE_CARD
    materialize_inverse: false
    edge_class: canonical
    source_type: metric_implementation
    target_type: platform_context
```

```yaml
candidate_edge:
  edge_id: edge.metric_implementation.flipkart.net_settlement.applies_to_platform.platform.flipkart
  edge_type: APPLIES_TO_PLATFORM
  source: metric_implementation.flipkart.net_settlement
  target: platform.flipkart
  fields:
    edge_family: applicability
    evidence_basis: derived from platform_context.flipkart.in
    confidence: high
    canonical_cognee_edge: true
    marketplace_only: true
    canonical_edge_type: APPLIES_TO_PLATFORM
    inverse_edge_type: HAS_APPLICABLE_CARD
    materialize_inverse: false
    edge_class: canonical
    source_type: metric_implementation
    target_type: platform
```

```yaml
candidate_edge:
  edge_id: edge.metric_implementation.flipkart.realization_rate.applies_to_platform_context.platform_context.flipkart.in
  edge_type: APPLIES_TO_PLATFORM_CONTEXT
  source: metric_implementation.flipkart.realization_rate
  target: platform_context.flipkart.in
  fields:
    edge_family: applicability
    evidence_basis: metric_implementation.fields.platform_context
    confidence: high
    canonical_cognee_edge: true
    marketplace_only: true
    canonical_edge_type: APPLIES_TO_PLATFORM_CONTEXT
    inverse_edge_type: HAS_APPLICABLE_CARD
    materialize_inverse: false
    edge_class: canonical
    source_type: metric_implementation
    target_type: platform_context
```

```yaml
candidate_edge:
  edge_id: edge.metric_implementation.flipkart.realization_rate.applies_to_platform.platform.flipkart
  edge_type: APPLIES_TO_PLATFORM
  source: metric_implementation.flipkart.realization_rate
  target: platform.flipkart
  fields:
    edge_family: applicability
    evidence_basis: derived from platform_context.flipkart.in
    confidence: high
    canonical_cognee_edge: true
    marketplace_only: true
    canonical_edge_type: APPLIES_TO_PLATFORM
    inverse_edge_type: HAS_APPLICABLE_CARD
    materialize_inverse: false
    edge_class: canonical
    source_type: metric_implementation
    target_type: platform
```

```yaml
candidate_edge:
  edge_id: edge.metric_implementation.flipkart.effective_fee_rate.applies_to_platform_context.platform_context.flipkart.in
  edge_type: APPLIES_TO_PLATFORM_CONTEXT
  source: metric_implementation.flipkart.effective_fee_rate
  target: platform_context.flipkart.in
  fields:
    edge_family: applicability
    evidence_basis: metric_implementation.fields.platform_context
    confidence: high
    canonical_cognee_edge: true
    marketplace_only: true
    canonical_edge_type: APPLIES_TO_PLATFORM_CONTEXT
    inverse_edge_type: HAS_APPLICABLE_CARD
    materialize_inverse: false
    edge_class: canonical
    source_type: metric_implementation
    target_type: platform_context
```

```yaml
candidate_edge:
  edge_id: edge.metric_implementation.flipkart.effective_fee_rate.applies_to_platform.platform.flipkart
  edge_type: APPLIES_TO_PLATFORM
  source: metric_implementation.flipkart.effective_fee_rate
  target: platform.flipkart
  fields:
    edge_family: applicability
    evidence_basis: derived from platform_context.flipkart.in
    confidence: high
    canonical_cognee_edge: true
    marketplace_only: true
    canonical_edge_type: APPLIES_TO_PLATFORM
    inverse_edge_type: HAS_APPLICABLE_CARD
    materialize_inverse: false
    edge_class: canonical
    source_type: metric_implementation
    target_type: platform
```

```yaml
candidate_edge:
  edge_id: edge.metric_implementation.flipkart.mp_fee_total.applies_to_platform_context.platform_context.flipkart.in
  edge_type: APPLIES_TO_PLATFORM_CONTEXT
  source: metric_implementation.flipkart.mp_fee_total
  target: platform_context.flipkart.in
  fields:
    edge_family: applicability
    evidence_basis: metric_implementation.fields.platform_context
    confidence: high
    canonical_cognee_edge: true
    marketplace_only: true
    canonical_edge_type: APPLIES_TO_PLATFORM_CONTEXT
    inverse_edge_type: HAS_APPLICABLE_CARD
    materialize_inverse: false
    edge_class: canonical
    source_type: metric_implementation
    target_type: platform_context
```

```yaml
candidate_edge:
  edge_id: edge.metric_implementation.flipkart.mp_fee_total.applies_to_platform.platform.flipkart
  edge_type: APPLIES_TO_PLATFORM
  source: metric_implementation.flipkart.mp_fee_total
  target: platform.flipkart
  fields:
    edge_family: applicability
    evidence_basis: derived from platform_context.flipkart.in
    confidence: high
    canonical_cognee_edge: true
    marketplace_only: true
    canonical_edge_type: APPLIES_TO_PLATFORM
    inverse_edge_type: HAS_APPLICABLE_CARD
    materialize_inverse: false
    edge_class: canonical
    source_type: metric_implementation
    target_type: platform
```

```yaml
candidate_edge:
  edge_id: edge.metric_implementation.flipkart.commission_fee_detail.applies_to_platform_context.platform_context.flipkart.in
  edge_type: APPLIES_TO_PLATFORM_CONTEXT
  source: metric_implementation.flipkart.commission_fee_detail
  target: platform_context.flipkart.in
  fields:
    edge_family: applicability
    evidence_basis: metric_implementation.fields.platform_context
    confidence: high
    canonical_cognee_edge: true
    marketplace_only: true
    canonical_edge_type: APPLIES_TO_PLATFORM_CONTEXT
    inverse_edge_type: HAS_APPLICABLE_CARD
    materialize_inverse: false
    edge_class: canonical
    source_type: metric_implementation
    target_type: platform_context
```

```yaml
candidate_edge:
  edge_id: edge.metric_implementation.flipkart.commission_fee_detail.applies_to_platform.platform.flipkart
  edge_type: APPLIES_TO_PLATFORM
  source: metric_implementation.flipkart.commission_fee_detail
  target: platform.flipkart
  fields:
    edge_family: applicability
    evidence_basis: derived from platform_context.flipkart.in
    confidence: high
    canonical_cognee_edge: true
    marketplace_only: true
    canonical_edge_type: APPLIES_TO_PLATFORM
    inverse_edge_type: HAS_APPLICABLE_CARD
    materialize_inverse: false
    edge_class: canonical
    source_type: metric_implementation
    target_type: platform
```

```yaml
candidate_edge:
  edge_id: edge.metric_implementation.flipkart.fixed_fee_detail.applies_to_platform_context.platform_context.flipkart.in
  edge_type: APPLIES_TO_PLATFORM_CONTEXT
  source: metric_implementation.flipkart.fixed_fee_detail
  target: platform_context.flipkart.in
  fields:
    edge_family: applicability
    evidence_basis: metric_implementation.fields.platform_context
    confidence: high
    canonical_cognee_edge: true
    marketplace_only: true
    canonical_edge_type: APPLIES_TO_PLATFORM_CONTEXT
    inverse_edge_type: HAS_APPLICABLE_CARD
    materialize_inverse: false
    edge_class: canonical
    source_type: metric_implementation
    target_type: platform_context
```

```yaml
candidate_edge:
  edge_id: edge.metric_implementation.flipkart.fixed_fee_detail.applies_to_platform.platform.flipkart
  edge_type: APPLIES_TO_PLATFORM
  source: metric_implementation.flipkart.fixed_fee_detail
  target: platform.flipkart
  fields:
    edge_family: applicability
    evidence_basis: derived from platform_context.flipkart.in
    confidence: high
    canonical_cognee_edge: true
    marketplace_only: true
    canonical_edge_type: APPLIES_TO_PLATFORM
    inverse_edge_type: HAS_APPLICABLE_CARD
    materialize_inverse: false
    edge_class: canonical
    source_type: metric_implementation
    target_type: platform
```

```yaml
candidate_edge:
  edge_id: edge.metric_implementation.flipkart.shipping_fee_detail.applies_to_platform_context.platform_context.flipkart.in
  edge_type: APPLIES_TO_PLATFORM_CONTEXT
  source: metric_implementation.flipkart.shipping_fee_detail
  target: platform_context.flipkart.in
  fields:
    edge_family: applicability
    evidence_basis: metric_implementation.fields.platform_context
    confidence: high
    canonical_cognee_edge: true
    marketplace_only: true
    canonical_edge_type: APPLIES_TO_PLATFORM_CONTEXT
    inverse_edge_type: HAS_APPLICABLE_CARD
    materialize_inverse: false
    edge_class: canonical
    source_type: metric_implementation
    target_type: platform_context
```

```yaml
candidate_edge:
  edge_id: edge.metric_implementation.flipkart.shipping_fee_detail.applies_to_platform.platform.flipkart
  edge_type: APPLIES_TO_PLATFORM
  source: metric_implementation.flipkart.shipping_fee_detail
  target: platform.flipkart
  fields:
    edge_family: applicability
    evidence_basis: derived from platform_context.flipkart.in
    confidence: high
    canonical_cognee_edge: true
    marketplace_only: true
    canonical_edge_type: APPLIES_TO_PLATFORM
    inverse_edge_type: HAS_APPLICABLE_CARD
    materialize_inverse: false
    edge_class: canonical
    source_type: metric_implementation
    target_type: platform
```

```yaml
candidate_edge:
  edge_id: edge.metric_implementation.flipkart.reverse_shipping_fee_detail.applies_to_platform_context.platform_context.flipkart.in
  edge_type: APPLIES_TO_PLATFORM_CONTEXT
  source: metric_implementation.flipkart.reverse_shipping_fee_detail
  target: platform_context.flipkart.in
  fields:
    edge_family: applicability
    evidence_basis: metric_implementation.fields.platform_context
    confidence: high
    canonical_cognee_edge: true
    marketplace_only: true
    canonical_edge_type: APPLIES_TO_PLATFORM_CONTEXT
    inverse_edge_type: HAS_APPLICABLE_CARD
    materialize_inverse: false
    edge_class: canonical
    source_type: metric_implementation
    target_type: platform_context
```

```yaml
candidate_edge:
  edge_id: edge.metric_implementation.flipkart.reverse_shipping_fee_detail.applies_to_platform.platform.flipkart
  edge_type: APPLIES_TO_PLATFORM
  source: metric_implementation.flipkart.reverse_shipping_fee_detail
  target: platform.flipkart
  fields:
    edge_family: applicability
    evidence_basis: derived from platform_context.flipkart.in
    confidence: high
    canonical_cognee_edge: true
    marketplace_only: true
    canonical_edge_type: APPLIES_TO_PLATFORM
    inverse_edge_type: HAS_APPLICABLE_CARD
    materialize_inverse: false
    edge_class: canonical
    source_type: metric_implementation
    target_type: platform
```

```yaml
candidate_edge:
  edge_id: edge.metric_implementation.flipkart.collection_fee_detail.applies_to_platform_context.platform_context.flipkart.in
  edge_type: APPLIES_TO_PLATFORM_CONTEXT
  source: metric_implementation.flipkart.collection_fee_detail
  target: platform_context.flipkart.in
  fields:
    edge_family: applicability
    evidence_basis: metric_implementation.fields.platform_context
    confidence: high
    canonical_cognee_edge: true
    marketplace_only: true
    canonical_edge_type: APPLIES_TO_PLATFORM_CONTEXT
    inverse_edge_type: HAS_APPLICABLE_CARD
    materialize_inverse: false
    edge_class: canonical
    source_type: metric_implementation
    target_type: platform_context
```

```yaml
candidate_edge:
  edge_id: edge.metric_implementation.flipkart.collection_fee_detail.applies_to_platform.platform.flipkart
  edge_type: APPLIES_TO_PLATFORM
  source: metric_implementation.flipkart.collection_fee_detail
  target: platform.flipkart
  fields:
    edge_family: applicability
    evidence_basis: derived from platform_context.flipkart.in
    confidence: high
    canonical_cognee_edge: true
    marketplace_only: true
    canonical_edge_type: APPLIES_TO_PLATFORM
    inverse_edge_type: HAS_APPLICABLE_CARD
    materialize_inverse: false
    edge_class: canonical
    source_type: metric_implementation
    target_type: platform
```

```yaml
candidate_edge:
  edge_id: edge.metric_implementation.flipkart.net_cashback.applies_to_platform_context.platform_context.flipkart.in
  edge_type: APPLIES_TO_PLATFORM_CONTEXT
  source: metric_implementation.flipkart.net_cashback
  target: platform_context.flipkart.in
  fields:
    edge_family: applicability
    evidence_basis: metric_implementation.fields.platform_context
    confidence: high
    canonical_cognee_edge: true
    marketplace_only: true
    canonical_edge_type: APPLIES_TO_PLATFORM_CONTEXT
    inverse_edge_type: HAS_APPLICABLE_CARD
    materialize_inverse: false
    edge_class: canonical
    source_type: metric_implementation
    target_type: platform_context
```

```yaml
candidate_edge:
  edge_id: edge.metric_implementation.flipkart.net_cashback.applies_to_platform.platform.flipkart
  edge_type: APPLIES_TO_PLATFORM
  source: metric_implementation.flipkart.net_cashback
  target: platform.flipkart
  fields:
    edge_family: applicability
    evidence_basis: derived from platform_context.flipkart.in
    confidence: high
    canonical_cognee_edge: true
    marketplace_only: true
    canonical_edge_type: APPLIES_TO_PLATFORM
    inverse_edge_type: HAS_APPLICABLE_CARD
    materialize_inverse: false
    edge_class: canonical
    source_type: metric_implementation
    target_type: platform
```

```yaml
candidate_edge:
  edge_id: edge.metric_implementation.flipkart.cashback_rate.applies_to_platform_context.platform_context.flipkart.in
  edge_type: APPLIES_TO_PLATFORM_CONTEXT
  source: metric_implementation.flipkart.cashback_rate
  target: platform_context.flipkart.in
  fields:
    edge_family: applicability
    evidence_basis: metric_implementation.fields.platform_context
    confidence: high
    canonical_cognee_edge: true
    marketplace_only: true
    canonical_edge_type: APPLIES_TO_PLATFORM_CONTEXT
    inverse_edge_type: HAS_APPLICABLE_CARD
    materialize_inverse: false
    edge_class: canonical
    source_type: metric_implementation
    target_type: platform_context
```

```yaml
candidate_edge:
  edge_id: edge.metric_implementation.flipkart.cashback_rate.applies_to_platform.platform.flipkart
  edge_type: APPLIES_TO_PLATFORM
  source: metric_implementation.flipkart.cashback_rate
  target: platform.flipkart
  fields:
    edge_family: applicability
    evidence_basis: derived from platform_context.flipkart.in
    confidence: high
    canonical_cognee_edge: true
    marketplace_only: true
    canonical_edge_type: APPLIES_TO_PLATFORM
    inverse_edge_type: HAS_APPLICABLE_CARD
    materialize_inverse: false
    edge_class: canonical
    source_type: metric_implementation
    target_type: platform
```

```yaml
candidate_edge:
  edge_id: edge.metric_implementation.flipkart.settlement_cycle_days.applies_to_platform_context.platform_context.flipkart.in
  edge_type: APPLIES_TO_PLATFORM_CONTEXT
  source: metric_implementation.flipkart.settlement_cycle_days
  target: platform_context.flipkart.in
  fields:
    edge_family: applicability
    evidence_basis: metric_implementation.fields.platform_context
    confidence: high
    canonical_cognee_edge: true
    marketplace_only: true
    canonical_edge_type: APPLIES_TO_PLATFORM_CONTEXT
    inverse_edge_type: HAS_APPLICABLE_CARD
    materialize_inverse: false
    edge_class: canonical
    source_type: metric_implementation
    target_type: platform_context
```

```yaml
candidate_edge:
  edge_id: edge.metric_implementation.flipkart.settlement_cycle_days.applies_to_platform.platform.flipkart
  edge_type: APPLIES_TO_PLATFORM
  source: metric_implementation.flipkart.settlement_cycle_days
  target: platform.flipkart
  fields:
    edge_family: applicability
    evidence_basis: derived from platform_context.flipkart.in
    confidence: high
    canonical_cognee_edge: true
    marketplace_only: true
    canonical_edge_type: APPLIES_TO_PLATFORM
    inverse_edge_type: HAS_APPLICABLE_CARD
    materialize_inverse: false
    edge_class: canonical
    source_type: metric_implementation
    target_type: platform
```

```yaml
candidate_edge:
  edge_id: edge.metric_implementation.flipkart.tcs_deducted.applies_to_platform_context.platform_context.flipkart.in
  edge_type: APPLIES_TO_PLATFORM_CONTEXT
  source: metric_implementation.flipkart.tcs_deducted
  target: platform_context.flipkart.in
  fields:
    edge_family: applicability
    evidence_basis: metric_implementation.fields.platform_context
    confidence: high
    canonical_cognee_edge: true
    marketplace_only: true
    canonical_edge_type: APPLIES_TO_PLATFORM_CONTEXT
    inverse_edge_type: HAS_APPLICABLE_CARD
    materialize_inverse: false
    edge_class: canonical
    source_type: metric_implementation
    target_type: platform_context
```

```yaml
candidate_edge:
  edge_id: edge.metric_implementation.flipkart.tcs_deducted.applies_to_platform.platform.flipkart
  edge_type: APPLIES_TO_PLATFORM
  source: metric_implementation.flipkart.tcs_deducted
  target: platform.flipkart
  fields:
    edge_family: applicability
    evidence_basis: derived from platform_context.flipkart.in
    confidence: high
    canonical_cognee_edge: true
    marketplace_only: true
    canonical_edge_type: APPLIES_TO_PLATFORM
    inverse_edge_type: HAS_APPLICABLE_CARD
    materialize_inverse: false
    edge_class: canonical
    source_type: metric_implementation
    target_type: platform
```

```yaml
candidate_edge:
  edge_id: edge.metric_implementation.flipkart.tds_deducted.applies_to_platform_context.platform_context.flipkart.in
  edge_type: APPLIES_TO_PLATFORM_CONTEXT
  source: metric_implementation.flipkart.tds_deducted
  target: platform_context.flipkart.in
  fields:
    edge_family: applicability
    evidence_basis: metric_implementation.fields.platform_context
    confidence: high
    canonical_cognee_edge: true
    marketplace_only: true
    canonical_edge_type: APPLIES_TO_PLATFORM_CONTEXT
    inverse_edge_type: HAS_APPLICABLE_CARD
    materialize_inverse: false
    edge_class: canonical
    source_type: metric_implementation
    target_type: platform_context
```

```yaml
candidate_edge:
  edge_id: edge.metric_implementation.flipkart.tds_deducted.applies_to_platform.platform.flipkart
  edge_type: APPLIES_TO_PLATFORM
  source: metric_implementation.flipkart.tds_deducted
  target: platform.flipkart
  fields:
    edge_family: applicability
    evidence_basis: derived from platform_context.flipkart.in
    confidence: high
    canonical_cognee_edge: true
    marketplace_only: true
    canonical_edge_type: APPLIES_TO_PLATFORM
    inverse_edge_type: HAS_APPLICABLE_CARD
    materialize_inverse: false
    edge_class: canonical
    source_type: metric_implementation
    target_type: platform
```

```yaml
candidate_edge:
  edge_id: edge.metric_implementation.flipkart.gst_on_mp_fees.applies_to_platform_context.platform_context.flipkart.in
  edge_type: APPLIES_TO_PLATFORM_CONTEXT
  source: metric_implementation.flipkart.gst_on_mp_fees
  target: platform_context.flipkart.in
  fields:
    edge_family: applicability
    evidence_basis: metric_implementation.fields.platform_context
    confidence: high
    canonical_cognee_edge: true
    marketplace_only: true
    canonical_edge_type: APPLIES_TO_PLATFORM_CONTEXT
    inverse_edge_type: HAS_APPLICABLE_CARD
    materialize_inverse: false
    edge_class: canonical
    source_type: metric_implementation
    target_type: platform_context
```

```yaml
candidate_edge:
  edge_id: edge.metric_implementation.flipkart.gst_on_mp_fees.applies_to_platform.platform.flipkart
  edge_type: APPLIES_TO_PLATFORM
  source: metric_implementation.flipkart.gst_on_mp_fees
  target: platform.flipkart
  fields:
    edge_family: applicability
    evidence_basis: derived from platform_context.flipkart.in
    confidence: high
    canonical_cognee_edge: true
    marketplace_only: true
    canonical_edge_type: APPLIES_TO_PLATFORM
    inverse_edge_type: HAS_APPLICABLE_CARD
    materialize_inverse: false
    edge_class: canonical
    source_type: metric_implementation
    target_type: platform
```

```yaml
candidate_edge:
  edge_id: edge.metric_implementation.flipkart.fee_tax_detail.applies_to_platform_context.platform_context.flipkart.in
  edge_type: APPLIES_TO_PLATFORM_CONTEXT
  source: metric_implementation.flipkart.fee_tax_detail
  target: platform_context.flipkart.in
  fields:
    edge_family: applicability
    evidence_basis: metric_implementation.fields.platform_context
    confidence: high
    canonical_cognee_edge: true
    marketplace_only: true
    canonical_edge_type: APPLIES_TO_PLATFORM_CONTEXT
    inverse_edge_type: HAS_APPLICABLE_CARD
    materialize_inverse: false
    edge_class: canonical
    source_type: metric_implementation
    target_type: platform_context
```

```yaml
candidate_edge:
  edge_id: edge.metric_implementation.flipkart.fee_tax_detail.applies_to_platform.platform.flipkart
  edge_type: APPLIES_TO_PLATFORM
  source: metric_implementation.flipkart.fee_tax_detail
  target: platform.flipkart
  fields:
    edge_family: applicability
    evidence_basis: derived from platform_context.flipkart.in
    confidence: high
    canonical_cognee_edge: true
    marketplace_only: true
    canonical_edge_type: APPLIES_TO_PLATFORM
    inverse_edge_type: HAS_APPLICABLE_CARD
    materialize_inverse: false
    edge_class: canonical
    source_type: metric_implementation
    target_type: platform
```

```yaml
candidate_edge:
  edge_id: edge.metric_implementation.flipkart.return_rate.applies_to_platform_context.platform_context.flipkart.in
  edge_type: APPLIES_TO_PLATFORM_CONTEXT
  source: metric_implementation.flipkart.return_rate
  target: platform_context.flipkart.in
  fields:
    edge_family: applicability
    evidence_basis: metric_implementation.fields.platform_context
    confidence: high
    canonical_cognee_edge: true
    marketplace_only: true
    canonical_edge_type: APPLIES_TO_PLATFORM_CONTEXT
    inverse_edge_type: HAS_APPLICABLE_CARD
    materialize_inverse: false
    edge_class: canonical
    source_type: metric_implementation
    target_type: platform_context
```

```yaml
candidate_edge:
  edge_id: edge.metric_implementation.flipkart.return_rate.applies_to_platform.platform.flipkart
  edge_type: APPLIES_TO_PLATFORM
  source: metric_implementation.flipkart.return_rate
  target: platform.flipkart
  fields:
    edge_family: applicability
    evidence_basis: derived from platform_context.flipkart.in
    confidence: high
    canonical_cognee_edge: true
    marketplace_only: true
    canonical_edge_type: APPLIES_TO_PLATFORM
    inverse_edge_type: HAS_APPLICABLE_CARD
    materialize_inverse: false
    edge_class: canonical
    source_type: metric_implementation
    target_type: platform
```

```yaml
candidate_edge:
  edge_id: edge.metric_implementation.flipkart.cancellation_rate.applies_to_platform_context.platform_context.flipkart.in
  edge_type: APPLIES_TO_PLATFORM_CONTEXT
  source: metric_implementation.flipkart.cancellation_rate
  target: platform_context.flipkart.in
  fields:
    edge_family: applicability
    evidence_basis: metric_implementation.fields.platform_context
    confidence: high
    canonical_cognee_edge: true
    marketplace_only: true
    canonical_edge_type: APPLIES_TO_PLATFORM_CONTEXT
    inverse_edge_type: HAS_APPLICABLE_CARD
    materialize_inverse: false
    edge_class: canonical
    source_type: metric_implementation
    target_type: platform_context
```

```yaml
candidate_edge:
  edge_id: edge.metric_implementation.flipkart.cancellation_rate.applies_to_platform.platform.flipkart
  edge_type: APPLIES_TO_PLATFORM
  source: metric_implementation.flipkart.cancellation_rate
  target: platform.flipkart
  fields:
    edge_family: applicability
    evidence_basis: derived from platform_context.flipkart.in
    confidence: high
    canonical_cognee_edge: true
    marketplace_only: true
    canonical_edge_type: APPLIES_TO_PLATFORM
    inverse_edge_type: HAS_APPLICABLE_CARD
    materialize_inverse: false
    edge_class: canonical
    source_type: metric_implementation
    target_type: platform
```

```yaml
candidate_edge:
  edge_id: edge.metric_implementation.flipkart.protection_fund.applies_to_platform_context.platform_context.flipkart.in
  edge_type: APPLIES_TO_PLATFORM_CONTEXT
  source: metric_implementation.flipkart.protection_fund
  target: platform_context.flipkart.in
  fields:
    edge_family: applicability
    evidence_basis: metric_implementation.fields.platform_context
    confidence: high
    canonical_cognee_edge: true
    marketplace_only: true
    canonical_edge_type: APPLIES_TO_PLATFORM_CONTEXT
    inverse_edge_type: HAS_APPLICABLE_CARD
    materialize_inverse: false
    edge_class: canonical
    source_type: metric_implementation
    target_type: platform_context
```

```yaml
candidate_edge:
  edge_id: edge.metric_implementation.flipkart.protection_fund.applies_to_platform.platform.flipkart
  edge_type: APPLIES_TO_PLATFORM
  source: metric_implementation.flipkart.protection_fund
  target: platform.flipkart
  fields:
    edge_family: applicability
    evidence_basis: derived from platform_context.flipkart.in
    confidence: high
    canonical_cognee_edge: true
    marketplace_only: true
    canonical_edge_type: APPLIES_TO_PLATFORM
    inverse_edge_type: HAS_APPLICABLE_CARD
    materialize_inverse: false
    edge_class: canonical
    source_type: metric_implementation
    target_type: platform
```

```yaml
candidate_edge:
  edge_id: edge.table.flipkart.oms.sourced_from_platform.platform.flipkart
  edge_type: SOURCED_FROM_PLATFORM
  source: table.flipkart.oms
  target: platform.flipkart
  fields:
    edge_family: data_understanding
    evidence_basis: marketplace document vendor/platform scope
    confidence: high
    canonical_cognee_edge: true
    marketplace_only: true
    canonical_edge_type: SOURCED_FROM_PLATFORM
    inverse_edge_type: HAS_SOURCE_TABLE
    materialize_inverse: false
    edge_class: canonical
    source_type: table
    target_type: platform
```

```yaml
candidate_edge:
  edge_id: edge.table.flipkart.oms.sourced_from_platform_context.platform_context.flipkart.in
  edge_type: SOURCED_FROM_PLATFORM_CONTEXT
  source: table.flipkart.oms
  target: platform_context.flipkart.in
  fields:
    edge_family: data_understanding
    evidence_basis: marketplace document vendor/platform context
    confidence: high
    canonical_cognee_edge: true
    marketplace_only: true
    canonical_edge_type: SOURCED_FROM_PLATFORM_CONTEXT
    inverse_edge_type: HAS_SOURCE_TABLE
    materialize_inverse: false
    edge_class: canonical
    source_type: table
    target_type: platform_context
```

```yaml
candidate_edge:
  edge_id: edge.table.flipkart.settlement.sourced_from_platform.platform.flipkart
  edge_type: SOURCED_FROM_PLATFORM
  source: table.flipkart.settlement
  target: platform.flipkart
  fields:
    edge_family: data_understanding
    evidence_basis: marketplace document vendor/platform scope
    confidence: high
    canonical_cognee_edge: true
    marketplace_only: true
    canonical_edge_type: SOURCED_FROM_PLATFORM
    inverse_edge_type: HAS_SOURCE_TABLE
    materialize_inverse: false
    edge_class: canonical
    source_type: table
    target_type: platform
```

```yaml
candidate_edge:
  edge_id: edge.table.flipkart.settlement.sourced_from_platform_context.platform_context.flipkart.in
  edge_type: SOURCED_FROM_PLATFORM_CONTEXT
  source: table.flipkart.settlement
  target: platform_context.flipkart.in
  fields:
    edge_family: data_understanding
    evidence_basis: marketplace document vendor/platform context
    confidence: high
    canonical_cognee_edge: true
    marketplace_only: true
    canonical_edge_type: SOURCED_FROM_PLATFORM_CONTEXT
    inverse_edge_type: HAS_SOURCE_TABLE
    materialize_inverse: false
    edge_class: canonical
    source_type: table
    target_type: platform_context
```

```yaml
candidate_edge:
  edge_id: edge.table.flipkart.commission.sourced_from_platform.platform.flipkart
  edge_type: SOURCED_FROM_PLATFORM
  source: table.flipkart.commission
  target: platform.flipkart
  fields:
    edge_family: data_understanding
    evidence_basis: marketplace document vendor/platform scope
    confidence: high
    canonical_cognee_edge: true
    marketplace_only: true
    canonical_edge_type: SOURCED_FROM_PLATFORM
    inverse_edge_type: HAS_SOURCE_TABLE
    materialize_inverse: false
    edge_class: canonical
    source_type: table
    target_type: platform
```

```yaml
candidate_edge:
  edge_id: edge.table.flipkart.commission.sourced_from_platform_context.platform_context.flipkart.in
  edge_type: SOURCED_FROM_PLATFORM_CONTEXT
  source: table.flipkart.commission
  target: platform_context.flipkart.in
  fields:
    edge_family: data_understanding
    evidence_basis: marketplace document vendor/platform context
    confidence: high
    canonical_cognee_edge: true
    marketplace_only: true
    canonical_edge_type: SOURCED_FROM_PLATFORM_CONTEXT
    inverse_edge_type: HAS_SOURCE_TABLE
    materialize_inverse: false
    edge_class: canonical
    source_type: table
    target_type: platform_context
```

```yaml
candidate_edge:
  edge_id: edge.table.flipkart.cashback.sourced_from_platform.platform.flipkart
  edge_type: SOURCED_FROM_PLATFORM
  source: table.flipkart.cashback
  target: platform.flipkart
  fields:
    edge_family: data_understanding
    evidence_basis: marketplace document vendor/platform scope
    confidence: high
    canonical_cognee_edge: true
    marketplace_only: true
    canonical_edge_type: SOURCED_FROM_PLATFORM
    inverse_edge_type: HAS_SOURCE_TABLE
    materialize_inverse: false
    edge_class: canonical
    source_type: table
    target_type: platform
```

```yaml
candidate_edge:
  edge_id: edge.table.flipkart.cashback.sourced_from_platform_context.platform_context.flipkart.in
  edge_type: SOURCED_FROM_PLATFORM_CONTEXT
  source: table.flipkart.cashback
  target: platform_context.flipkart.in
  fields:
    edge_family: data_understanding
    evidence_basis: marketplace document vendor/platform context
    confidence: high
    canonical_cognee_edge: true
    marketplace_only: true
    canonical_edge_type: SOURCED_FROM_PLATFORM_CONTEXT
    inverse_edge_type: HAS_SOURCE_TABLE
    materialize_inverse: false
    edge_class: canonical
    source_type: table
    target_type: platform_context
```

```yaml
candidate_edge:
  edge_id: edge.table.flipkart.oms.has_column.column.oms.order_id
  edge_type: HAS_COLUMN
  source: table.flipkart.oms
  target: column.oms.order_id
  fields:
    edge_family: data_understanding
    evidence_basis: column.fields.table_id
    confidence: high
    canonical_cognee_edge: true
    marketplace_only: true
    canonical_edge_type: HAS_COLUMN
    inverse_edge_type: BELONGS_TO_TABLE
    materialize_inverse: true
    edge_class: canonical
    source_type: table
    target_type: column
```

```yaml
candidate_edge:
  edge_id: edge.column.oms.order_id.belongs_to_table.table.flipkart.oms
  edge_type: BELONGS_TO_TABLE
  source: column.oms.order_id
  target: table.flipkart.oms
  fields:
    edge_family: data_understanding
    evidence_basis: column.fields.table_id
    confidence: high
    canonical_cognee_edge: true
    marketplace_only: true
    canonical_edge_type: BELONGS_TO_TABLE
    legacy_edge_aliases:
    - column_belongs_to_table
    inverse_edge_type: HAS_COLUMN
    materialize_inverse: true
    edge_class: canonical
    source_type: column
    target_type: table
```

```yaml
candidate_edge:
  edge_id: edge.table.flipkart.oms.has_column.column.oms.item_id
  edge_type: HAS_COLUMN
  source: table.flipkart.oms
  target: column.oms.item_id
  fields:
    edge_family: data_understanding
    evidence_basis: column.fields.table_id
    confidence: high
    canonical_cognee_edge: true
    marketplace_only: true
    canonical_edge_type: HAS_COLUMN
    inverse_edge_type: BELONGS_TO_TABLE
    materialize_inverse: true
    edge_class: canonical
    source_type: table
    target_type: column
```

```yaml
candidate_edge:
  edge_id: edge.column.oms.item_id.belongs_to_table.table.flipkart.oms
  edge_type: BELONGS_TO_TABLE
  source: column.oms.item_id
  target: table.flipkart.oms
  fields:
    edge_family: data_understanding
    evidence_basis: column.fields.table_id
    confidence: high
    canonical_cognee_edge: true
    marketplace_only: true
    canonical_edge_type: BELONGS_TO_TABLE
    legacy_edge_aliases:
    - column_belongs_to_table
    inverse_edge_type: HAS_COLUMN
    materialize_inverse: true
    edge_class: canonical
    source_type: column
    target_type: table
```

```yaml
candidate_edge:
  edge_id: edge.table.flipkart.oms.has_column.column.oms.charged_amount
  edge_type: HAS_COLUMN
  source: table.flipkart.oms
  target: column.oms.charged_amount
  fields:
    edge_family: data_understanding
    evidence_basis: column.fields.table_id
    confidence: high
    canonical_cognee_edge: true
    marketplace_only: true
    canonical_edge_type: HAS_COLUMN
    inverse_edge_type: BELONGS_TO_TABLE
    materialize_inverse: true
    edge_class: canonical
    source_type: table
    target_type: column
```

```yaml
candidate_edge:
  edge_id: edge.column.oms.charged_amount.belongs_to_table.table.flipkart.oms
  edge_type: BELONGS_TO_TABLE
  source: column.oms.charged_amount
  target: table.flipkart.oms
  fields:
    edge_family: data_understanding
    evidence_basis: column.fields.table_id
    confidence: high
    canonical_cognee_edge: true
    marketplace_only: true
    canonical_edge_type: BELONGS_TO_TABLE
    legacy_edge_aliases:
    - column_belongs_to_table
    inverse_edge_type: HAS_COLUMN
    materialize_inverse: true
    edge_class: canonical
    source_type: column
    target_type: table
```

```yaml
candidate_edge:
  edge_id: edge.table.flipkart.oms.has_column.column.oms.transaction_type
  edge_type: HAS_COLUMN
  source: table.flipkart.oms
  target: column.oms.transaction_type
  fields:
    edge_family: data_understanding
    evidence_basis: column.fields.table_id
    confidence: high
    canonical_cognee_edge: true
    marketplace_only: true
    canonical_edge_type: HAS_COLUMN
    inverse_edge_type: BELONGS_TO_TABLE
    materialize_inverse: true
    edge_class: canonical
    source_type: table
    target_type: column
```

```yaml
candidate_edge:
  edge_id: edge.column.oms.transaction_type.belongs_to_table.table.flipkart.oms
  edge_type: BELONGS_TO_TABLE
  source: column.oms.transaction_type
  target: table.flipkart.oms
  fields:
    edge_family: data_understanding
    evidence_basis: column.fields.table_id
    confidence: high
    canonical_cognee_edge: true
    marketplace_only: true
    canonical_edge_type: BELONGS_TO_TABLE
    legacy_edge_aliases:
    - column_belongs_to_table
    inverse_edge_type: HAS_COLUMN
    materialize_inverse: true
    edge_class: canonical
    source_type: column
    target_type: table
```

```yaml
candidate_edge:
  edge_id: edge.table.flipkart.oms.has_column.column.oms.fulfilment_type
  edge_type: HAS_COLUMN
  source: table.flipkart.oms
  target: column.oms.fulfilment_type
  fields:
    edge_family: data_understanding
    evidence_basis: column.fields.table_id
    confidence: high
    canonical_cognee_edge: true
    marketplace_only: true
    canonical_edge_type: HAS_COLUMN
    inverse_edge_type: BELONGS_TO_TABLE
    materialize_inverse: true
    edge_class: canonical
    source_type: table
    target_type: column
```

```yaml
candidate_edge:
  edge_id: edge.column.oms.fulfilment_type.belongs_to_table.table.flipkart.oms
  edge_type: BELONGS_TO_TABLE
  source: column.oms.fulfilment_type
  target: table.flipkart.oms
  fields:
    edge_family: data_understanding
    evidence_basis: column.fields.table_id
    confidence: high
    canonical_cognee_edge: true
    marketplace_only: true
    canonical_edge_type: BELONGS_TO_TABLE
    legacy_edge_aliases:
    - column_belongs_to_table
    inverse_edge_type: HAS_COLUMN
    materialize_inverse: true
    edge_class: canonical
    source_type: column
    target_type: table
```

```yaml
candidate_edge:
  edge_id: edge.table.flipkart.oms.has_column.column.oms.is_shopsy_order
  edge_type: HAS_COLUMN
  source: table.flipkart.oms
  target: column.oms.is_shopsy_order_
  fields:
    edge_family: data_understanding
    evidence_basis: column.fields.table_id
    confidence: high
    canonical_cognee_edge: true
    marketplace_only: true
    canonical_edge_type: HAS_COLUMN
    inverse_edge_type: BELONGS_TO_TABLE
    materialize_inverse: true
    edge_class: canonical
    source_type: table
    target_type: column
```

```yaml
candidate_edge:
  edge_id: edge.column.oms.is_shopsy_order.belongs_to_table.table.flipkart.oms
  edge_type: BELONGS_TO_TABLE
  source: column.oms.is_shopsy_order_
  target: table.flipkart.oms
  fields:
    edge_family: data_understanding
    evidence_basis: column.fields.table_id
    confidence: high
    canonical_cognee_edge: true
    marketplace_only: true
    canonical_edge_type: BELONGS_TO_TABLE
    legacy_edge_aliases:
    - column_belongs_to_table
    inverse_edge_type: HAS_COLUMN
    materialize_inverse: true
    edge_class: canonical
    source_type: column
    target_type: table
```

```yaml
candidate_edge:
  edge_id: edge.table.flipkart.oms.has_column.column.oms.quantity
  edge_type: HAS_COLUMN
  source: table.flipkart.oms
  target: column.oms.quantity
  fields:
    edge_family: data_understanding
    evidence_basis: column.fields.table_id
    confidence: high
    canonical_cognee_edge: true
    marketplace_only: true
    canonical_edge_type: HAS_COLUMN
    inverse_edge_type: BELONGS_TO_TABLE
    materialize_inverse: true
    edge_class: canonical
    source_type: table
    target_type: column
```

```yaml
candidate_edge:
  edge_id: edge.column.oms.quantity.belongs_to_table.table.flipkart.oms
  edge_type: BELONGS_TO_TABLE
  source: column.oms.quantity
  target: table.flipkart.oms
  fields:
    edge_family: data_understanding
    evidence_basis: column.fields.table_id
    confidence: high
    canonical_cognee_edge: true
    marketplace_only: true
    canonical_edge_type: BELONGS_TO_TABLE
    legacy_edge_aliases:
    - column_belongs_to_table
    inverse_edge_type: HAS_COLUMN
    materialize_inverse: true
    edge_class: canonical
    source_type: column
    target_type: table
```

```yaml
candidate_edge:
  edge_id: edge.table.flipkart.oms.has_column.column.oms.currency_type
  edge_type: HAS_COLUMN
  source: table.flipkart.oms
  target: column.oms.currency_type
  fields:
    edge_family: data_understanding
    evidence_basis: column.fields.table_id
    confidence: high
    canonical_cognee_edge: true
    marketplace_only: true
    canonical_edge_type: HAS_COLUMN
    inverse_edge_type: BELONGS_TO_TABLE
    materialize_inverse: true
    edge_class: canonical
    source_type: table
    target_type: column
```

```yaml
candidate_edge:
  edge_id: edge.column.oms.currency_type.belongs_to_table.table.flipkart.oms
  edge_type: BELONGS_TO_TABLE
  source: column.oms.currency_type
  target: table.flipkart.oms
  fields:
    edge_family: data_understanding
    evidence_basis: column.fields.table_id
    confidence: high
    canonical_cognee_edge: true
    marketplace_only: true
    canonical_edge_type: BELONGS_TO_TABLE
    legacy_edge_aliases:
    - column_belongs_to_table
    inverse_edge_type: HAS_COLUMN
    materialize_inverse: true
    edge_class: canonical
    source_type: column
    target_type: table
```

```yaml
candidate_edge:
  edge_id: edge.table.flipkart.oms.has_column.column.oms.created_date
  edge_type: HAS_COLUMN
  source: table.flipkart.oms
  target: column.oms.created_date
  fields:
    edge_family: data_understanding
    evidence_basis: column.fields.table_id
    confidence: high
    canonical_cognee_edge: true
    marketplace_only: true
    canonical_edge_type: HAS_COLUMN
    inverse_edge_type: BELONGS_TO_TABLE
    materialize_inverse: true
    edge_class: canonical
    source_type: table
    target_type: column
```

```yaml
candidate_edge:
  edge_id: edge.column.oms.created_date.belongs_to_table.table.flipkart.oms
  edge_type: BELONGS_TO_TABLE
  source: column.oms.created_date
  target: table.flipkart.oms
  fields:
    edge_family: data_understanding
    evidence_basis: column.fields.table_id
    confidence: high
    canonical_cognee_edge: true
    marketplace_only: true
    canonical_edge_type: BELONGS_TO_TABLE
    legacy_edge_aliases:
    - column_belongs_to_table
    inverse_edge_type: HAS_COLUMN
    materialize_inverse: true
    edge_class: canonical
    source_type: column
    target_type: table
```

```yaml
candidate_edge:
  edge_id: edge.table.flipkart.oms.has_column.column.oms.is_active
  edge_type: HAS_COLUMN
  source: table.flipkart.oms
  target: column.oms.is_active
  fields:
    edge_family: data_understanding
    evidence_basis: column.fields.table_id
    confidence: high
    canonical_cognee_edge: true
    marketplace_only: true
    canonical_edge_type: HAS_COLUMN
    inverse_edge_type: BELONGS_TO_TABLE
    materialize_inverse: true
    edge_class: canonical
    source_type: table
    target_type: column
```

```yaml
candidate_edge:
  edge_id: edge.column.oms.is_active.belongs_to_table.table.flipkart.oms
  edge_type: BELONGS_TO_TABLE
  source: column.oms.is_active
  target: table.flipkart.oms
  fields:
    edge_family: data_understanding
    evidence_basis: column.fields.table_id
    confidence: high
    canonical_cognee_edge: true
    marketplace_only: true
    canonical_edge_type: BELONGS_TO_TABLE
    legacy_edge_aliases:
    - column_belongs_to_table
    inverse_edge_type: HAS_COLUMN
    materialize_inverse: true
    edge_class: canonical
    source_type: column
    target_type: table
```

```yaml
candidate_edge:
  edge_id: edge.table.flipkart.oms.has_column.column.oms.group_level_id
  edge_type: HAS_COLUMN
  source: table.flipkart.oms
  target: column.oms.group_level_id
  fields:
    edge_family: data_understanding
    evidence_basis: column.fields.table_id
    confidence: high
    canonical_cognee_edge: true
    marketplace_only: true
    canonical_edge_type: HAS_COLUMN
    inverse_edge_type: BELONGS_TO_TABLE
    materialize_inverse: true
    edge_class: canonical
    source_type: table
    target_type: column
```

```yaml
candidate_edge:
  edge_id: edge.column.oms.group_level_id.belongs_to_table.table.flipkart.oms
  edge_type: BELONGS_TO_TABLE
  source: column.oms.group_level_id
  target: table.flipkart.oms
  fields:
    edge_family: data_understanding
    evidence_basis: column.fields.table_id
    confidence: high
    canonical_cognee_edge: true
    marketplace_only: true
    canonical_edge_type: BELONGS_TO_TABLE
    legacy_edge_aliases:
    - column_belongs_to_table
    inverse_edge_type: HAS_COLUMN
    materialize_inverse: true
    edge_class: canonical
    source_type: column
    target_type: table
```

```yaml
candidate_edge:
  edge_id: edge.table.flipkart.settlement.has_column.column.settlement.settlement_id
  edge_type: HAS_COLUMN
  source: table.flipkart.settlement
  target: column.settlement.settlement_id
  fields:
    edge_family: data_understanding
    evidence_basis: column.fields.table_id
    confidence: high
    canonical_cognee_edge: true
    marketplace_only: true
    canonical_edge_type: HAS_COLUMN
    inverse_edge_type: BELONGS_TO_TABLE
    materialize_inverse: true
    edge_class: canonical
    source_type: table
    target_type: column
```

```yaml
candidate_edge:
  edge_id: edge.column.settlement.settlement_id.belongs_to_table.table.flipkart.settlement
  edge_type: BELONGS_TO_TABLE
  source: column.settlement.settlement_id
  target: table.flipkart.settlement
  fields:
    edge_family: data_understanding
    evidence_basis: column.fields.table_id
    confidence: high
    canonical_cognee_edge: true
    marketplace_only: true
    canonical_edge_type: BELONGS_TO_TABLE
    legacy_edge_aliases:
    - column_belongs_to_table
    inverse_edge_type: HAS_COLUMN
    materialize_inverse: true
    edge_class: canonical
    source_type: column
    target_type: table
```

```yaml
candidate_edge:
  edge_id: edge.table.flipkart.settlement.has_column.column.settlement.order_id
  edge_type: HAS_COLUMN
  source: table.flipkart.settlement
  target: column.settlement.order_id
  fields:
    edge_family: data_understanding
    evidence_basis: column.fields.table_id
    confidence: high
    canonical_cognee_edge: true
    marketplace_only: true
    canonical_edge_type: HAS_COLUMN
    inverse_edge_type: BELONGS_TO_TABLE
    materialize_inverse: true
    edge_class: canonical
    source_type: table
    target_type: column
```

```yaml
candidate_edge:
  edge_id: edge.column.settlement.order_id.belongs_to_table.table.flipkart.settlement
  edge_type: BELONGS_TO_TABLE
  source: column.settlement.order_id
  target: table.flipkart.settlement
  fields:
    edge_family: data_understanding
    evidence_basis: column.fields.table_id
    confidence: high
    canonical_cognee_edge: true
    marketplace_only: true
    canonical_edge_type: BELONGS_TO_TABLE
    legacy_edge_aliases:
    - column_belongs_to_table
    inverse_edge_type: HAS_COLUMN
    materialize_inverse: true
    edge_class: canonical
    source_type: column
    target_type: table
```

```yaml
candidate_edge:
  edge_id: edge.table.flipkart.settlement.has_column.column.settlement.item_id
  edge_type: HAS_COLUMN
  source: table.flipkart.settlement
  target: column.settlement.item_id
  fields:
    edge_family: data_understanding
    evidence_basis: column.fields.table_id
    confidence: high
    canonical_cognee_edge: true
    marketplace_only: true
    canonical_edge_type: HAS_COLUMN
    inverse_edge_type: BELONGS_TO_TABLE
    materialize_inverse: true
    edge_class: canonical
    source_type: table
    target_type: column
```

```yaml
candidate_edge:
  edge_id: edge.column.settlement.item_id.belongs_to_table.table.flipkart.settlement
  edge_type: BELONGS_TO_TABLE
  source: column.settlement.item_id
  target: table.flipkart.settlement
  fields:
    edge_family: data_understanding
    evidence_basis: column.fields.table_id
    confidence: high
    canonical_cognee_edge: true
    marketplace_only: true
    canonical_edge_type: BELONGS_TO_TABLE
    legacy_edge_aliases:
    - column_belongs_to_table
    inverse_edge_type: HAS_COLUMN
    materialize_inverse: true
    edge_class: canonical
    source_type: column
    target_type: table
```

```yaml
candidate_edge:
  edge_id: edge.table.flipkart.settlement.has_column.column.settlement.invoice_number
  edge_type: HAS_COLUMN
  source: table.flipkart.settlement
  target: column.settlement.invoice_number
  fields:
    edge_family: data_understanding
    evidence_basis: column.fields.table_id
    confidence: high
    canonical_cognee_edge: true
    marketplace_only: true
    canonical_edge_type: HAS_COLUMN
    inverse_edge_type: BELONGS_TO_TABLE
    materialize_inverse: true
    edge_class: canonical
    source_type: table
    target_type: column
```

```yaml
candidate_edge:
  edge_id: edge.column.settlement.invoice_number.belongs_to_table.table.flipkart.settlement
  edge_type: BELONGS_TO_TABLE
  source: column.settlement.invoice_number
  target: table.flipkart.settlement
  fields:
    edge_family: data_understanding
    evidence_basis: column.fields.table_id
    confidence: high
    canonical_cognee_edge: true
    marketplace_only: true
    canonical_edge_type: BELONGS_TO_TABLE
    legacy_edge_aliases:
    - column_belongs_to_table
    inverse_edge_type: HAS_COLUMN
    materialize_inverse: true
    edge_class: canonical
    source_type: column
    target_type: table
```

```yaml
candidate_edge:
  edge_id: edge.table.flipkart.settlement.has_column.column.settlement.sku_id
  edge_type: HAS_COLUMN
  source: table.flipkart.settlement
  target: column.settlement.sku_id
  fields:
    edge_family: data_understanding
    evidence_basis: column.fields.table_id
    confidence: high
    canonical_cognee_edge: true
    marketplace_only: true
    canonical_edge_type: HAS_COLUMN
    inverse_edge_type: BELONGS_TO_TABLE
    materialize_inverse: true
    edge_class: canonical
    source_type: table
    target_type: column
```

```yaml
candidate_edge:
  edge_id: edge.column.settlement.sku_id.belongs_to_table.table.flipkart.settlement
  edge_type: BELONGS_TO_TABLE
  source: column.settlement.sku_id
  target: table.flipkart.settlement
  fields:
    edge_family: data_understanding
    evidence_basis: column.fields.table_id
    confidence: high
    canonical_cognee_edge: true
    marketplace_only: true
    canonical_edge_type: BELONGS_TO_TABLE
    legacy_edge_aliases:
    - column_belongs_to_table
    inverse_edge_type: HAS_COLUMN
    materialize_inverse: true
    edge_class: canonical
    source_type: column
    target_type: table
```

```yaml
candidate_edge:
  edge_id: edge.table.flipkart.settlement.has_column.column.settlement.product_sub_category
  edge_type: HAS_COLUMN
  source: table.flipkart.settlement
  target: column.settlement.product_sub_category
  fields:
    edge_family: data_understanding
    evidence_basis: column.fields.table_id
    confidence: high
    canonical_cognee_edge: true
    marketplace_only: true
    canonical_edge_type: HAS_COLUMN
    inverse_edge_type: BELONGS_TO_TABLE
    materialize_inverse: true
    edge_class: canonical
    source_type: table
    target_type: column
```

```yaml
candidate_edge:
  edge_id: edge.column.settlement.product_sub_category.belongs_to_table.table.flipkart.settlement
  edge_type: BELONGS_TO_TABLE
  source: column.settlement.product_sub_category
  target: table.flipkart.settlement
  fields:
    edge_family: data_understanding
    evidence_basis: column.fields.table_id
    confidence: high
    canonical_cognee_edge: true
    marketplace_only: true
    canonical_edge_type: BELONGS_TO_TABLE
    legacy_edge_aliases:
    - column_belongs_to_table
    inverse_edge_type: HAS_COLUMN
    materialize_inverse: true
    edge_class: canonical
    source_type: column
    target_type: table
```

```yaml
candidate_edge:
  edge_id: edge.table.flipkart.settlement.has_column.column.settlement.quantity
  edge_type: HAS_COLUMN
  source: table.flipkart.settlement
  target: column.settlement.quantity
  fields:
    edge_family: data_understanding
    evidence_basis: column.fields.table_id
    confidence: high
    canonical_cognee_edge: true
    marketplace_only: true
    canonical_edge_type: HAS_COLUMN
    inverse_edge_type: BELONGS_TO_TABLE
    materialize_inverse: true
    edge_class: canonical
    source_type: table
    target_type: column
```

```yaml
candidate_edge:
  edge_id: edge.column.settlement.quantity.belongs_to_table.table.flipkart.settlement
  edge_type: BELONGS_TO_TABLE
  source: column.settlement.quantity
  target: table.flipkart.settlement
  fields:
    edge_family: data_understanding
    evidence_basis: column.fields.table_id
    confidence: high
    canonical_cognee_edge: true
    marketplace_only: true
    canonical_edge_type: BELONGS_TO_TABLE
    legacy_edge_aliases:
    - column_belongs_to_table
    inverse_edge_type: HAS_COLUMN
    materialize_inverse: true
    edge_class: canonical
    source_type: column
    target_type: table
```

```yaml
candidate_edge:
  edge_id: edge.table.flipkart.settlement.has_column.column.settlement.settled_amount
  edge_type: HAS_COLUMN
  source: table.flipkart.settlement
  target: column.settlement.settled_amount
  fields:
    edge_family: data_understanding
    evidence_basis: column.fields.table_id
    confidence: high
    canonical_cognee_edge: true
    marketplace_only: true
    canonical_edge_type: HAS_COLUMN
    inverse_edge_type: BELONGS_TO_TABLE
    materialize_inverse: true
    edge_class: canonical
    source_type: table
    target_type: column
```

```yaml
candidate_edge:
  edge_id: edge.column.settlement.settled_amount.belongs_to_table.table.flipkart.settlement
  edge_type: BELONGS_TO_TABLE
  source: column.settlement.settled_amount
  target: table.flipkart.settlement
  fields:
    edge_family: data_understanding
    evidence_basis: column.fields.table_id
    confidence: high
    canonical_cognee_edge: true
    marketplace_only: true
    canonical_edge_type: BELONGS_TO_TABLE
    legacy_edge_aliases:
    - column_belongs_to_table
    inverse_edge_type: HAS_COLUMN
    materialize_inverse: true
    edge_class: canonical
    source_type: column
    target_type: table
```

```yaml
candidate_edge:
  edge_id: edge.table.flipkart.settlement.has_column.column.settlement.sale_settled_amount
  edge_type: HAS_COLUMN
  source: table.flipkart.settlement
  target: column.settlement.sale_settled_amount
  fields:
    edge_family: data_understanding
    evidence_basis: column.fields.table_id
    confidence: high
    canonical_cognee_edge: true
    marketplace_only: true
    canonical_edge_type: HAS_COLUMN
    inverse_edge_type: BELONGS_TO_TABLE
    materialize_inverse: true
    edge_class: canonical
    source_type: table
    target_type: column
```

```yaml
candidate_edge:
  edge_id: edge.column.settlement.sale_settled_amount.belongs_to_table.table.flipkart.settlement
  edge_type: BELONGS_TO_TABLE
  source: column.settlement.sale_settled_amount
  target: table.flipkart.settlement
  fields:
    edge_family: data_understanding
    evidence_basis: column.fields.table_id
    confidence: high
    canonical_cognee_edge: true
    marketplace_only: true
    canonical_edge_type: BELONGS_TO_TABLE
    legacy_edge_aliases:
    - column_belongs_to_table
    inverse_edge_type: HAS_COLUMN
    materialize_inverse: true
    edge_class: canonical
    source_type: column
    target_type: table
```

```yaml
candidate_edge:
  edge_id: edge.table.flipkart.settlement.has_column.column.settlement.refund_settled_amount
  edge_type: HAS_COLUMN
  source: table.flipkart.settlement
  target: column.settlement.refund_settled_amount
  fields:
    edge_family: data_understanding
    evidence_basis: column.fields.table_id
    confidence: high
    canonical_cognee_edge: true
    marketplace_only: true
    canonical_edge_type: HAS_COLUMN
    inverse_edge_type: BELONGS_TO_TABLE
    materialize_inverse: true
    edge_class: canonical
    source_type: table
    target_type: column
```

```yaml
candidate_edge:
  edge_id: edge.column.settlement.refund_settled_amount.belongs_to_table.table.flipkart.settlement
  edge_type: BELONGS_TO_TABLE
  source: column.settlement.refund_settled_amount
  target: table.flipkart.settlement
  fields:
    edge_family: data_understanding
    evidence_basis: column.fields.table_id
    confidence: high
    canonical_cognee_edge: true
    marketplace_only: true
    canonical_edge_type: BELONGS_TO_TABLE
    legacy_edge_aliases:
    - column_belongs_to_table
    inverse_edge_type: HAS_COLUMN
    materialize_inverse: true
    edge_class: canonical
    source_type: column
    target_type: table
```

```yaml
candidate_edge:
  edge_id: edge.table.flipkart.settlement.has_column.column.settlement.offer_settled_amount
  edge_type: HAS_COLUMN
  source: table.flipkart.settlement
  target: column.settlement.offer_settled_amount
  fields:
    edge_family: data_understanding
    evidence_basis: column.fields.table_id
    confidence: high
    canonical_cognee_edge: true
    marketplace_only: true
    canonical_edge_type: HAS_COLUMN
    inverse_edge_type: BELONGS_TO_TABLE
    materialize_inverse: true
    edge_class: canonical
    source_type: table
    target_type: column
```

```yaml
candidate_edge:
  edge_id: edge.column.settlement.offer_settled_amount.belongs_to_table.table.flipkart.settlement
  edge_type: BELONGS_TO_TABLE
  source: column.settlement.offer_settled_amount
  target: table.flipkart.settlement
  fields:
    edge_family: data_understanding
    evidence_basis: column.fields.table_id
    confidence: high
    canonical_cognee_edge: true
    marketplace_only: true
    canonical_edge_type: BELONGS_TO_TABLE
    legacy_edge_aliases:
    - column_belongs_to_table
    inverse_edge_type: HAS_COLUMN
    materialize_inverse: true
    edge_class: canonical
    source_type: column
    target_type: table
```

```yaml
candidate_edge:
  edge_id: edge.table.flipkart.settlement.has_column.column.settlement.offer_adjustment_settled_amount
  edge_type: HAS_COLUMN
  source: table.flipkart.settlement
  target: column.settlement.offer_adjustment_settled_amount
  fields:
    edge_family: data_understanding
    evidence_basis: column.fields.table_id
    confidence: high
    canonical_cognee_edge: true
    marketplace_only: true
    canonical_edge_type: HAS_COLUMN
    inverse_edge_type: BELONGS_TO_TABLE
    materialize_inverse: true
    edge_class: canonical
    source_type: table
    target_type: column
```

```yaml
candidate_edge:
  edge_id: edge.column.settlement.offer_adjustment_settled_amount.belongs_to_table.table.flipkart.settlement
  edge_type: BELONGS_TO_TABLE
  source: column.settlement.offer_adjustment_settled_amount
  target: table.flipkart.settlement
  fields:
    edge_family: data_understanding
    evidence_basis: column.fields.table_id
    confidence: high
    canonical_cognee_edge: true
    marketplace_only: true
    canonical_edge_type: BELONGS_TO_TABLE
    legacy_edge_aliases:
    - column_belongs_to_table
    inverse_edge_type: HAS_COLUMN
    materialize_inverse: true
    edge_class: canonical
    source_type: column
    target_type: table
```

```yaml
candidate_edge:
  edge_id: edge.table.flipkart.settlement.has_column.column.settlement.protection_fund_settled_amount
  edge_type: HAS_COLUMN
  source: table.flipkart.settlement
  target: column.settlement.protection_fund_settled_amount
  fields:
    edge_family: data_understanding
    evidence_basis: column.fields.table_id
    confidence: high
    canonical_cognee_edge: true
    marketplace_only: true
    canonical_edge_type: HAS_COLUMN
    inverse_edge_type: BELONGS_TO_TABLE
    materialize_inverse: true
    edge_class: canonical
    source_type: table
    target_type: column
```

```yaml
candidate_edge:
  edge_id: edge.column.settlement.protection_fund_settled_amount.belongs_to_table.table.flipkart.settlement
  edge_type: BELONGS_TO_TABLE
  source: column.settlement.protection_fund_settled_amount
  target: table.flipkart.settlement
  fields:
    edge_family: data_understanding
    evidence_basis: column.fields.table_id
    confidence: high
    canonical_cognee_edge: true
    marketplace_only: true
    canonical_edge_type: BELONGS_TO_TABLE
    legacy_edge_aliases:
    - column_belongs_to_table
    inverse_edge_type: HAS_COLUMN
    materialize_inverse: true
    edge_class: canonical
    source_type: column
    target_type: table
```

```yaml
candidate_edge:
  edge_id: edge.table.flipkart.settlement.has_column.column.settlement.mp_fee
  edge_type: HAS_COLUMN
  source: table.flipkart.settlement
  target: column.settlement.mp_fee
  fields:
    edge_family: data_understanding
    evidence_basis: column.fields.table_id
    confidence: high
    canonical_cognee_edge: true
    marketplace_only: true
    canonical_edge_type: HAS_COLUMN
    inverse_edge_type: BELONGS_TO_TABLE
    materialize_inverse: true
    edge_class: canonical
    source_type: table
    target_type: column
```

```yaml
candidate_edge:
  edge_id: edge.column.settlement.mp_fee.belongs_to_table.table.flipkart.settlement
  edge_type: BELONGS_TO_TABLE
  source: column.settlement.mp_fee
  target: table.flipkart.settlement
  fields:
    edge_family: data_understanding
    evidence_basis: column.fields.table_id
    confidence: high
    canonical_cognee_edge: true
    marketplace_only: true
    canonical_edge_type: BELONGS_TO_TABLE
    legacy_edge_aliases:
    - column_belongs_to_table
    inverse_edge_type: HAS_COLUMN
    materialize_inverse: true
    edge_class: canonical
    source_type: column
    target_type: table
```

```yaml
candidate_edge:
  edge_id: edge.table.flipkart.settlement.has_column.column.settlement.gst_on_mp_fees
  edge_type: HAS_COLUMN
  source: table.flipkart.settlement
  target: column.settlement.gst_on_mp_fees
  fields:
    edge_family: data_understanding
    evidence_basis: column.fields.table_id
    confidence: high
    canonical_cognee_edge: true
    marketplace_only: true
    canonical_edge_type: HAS_COLUMN
    inverse_edge_type: BELONGS_TO_TABLE
    materialize_inverse: true
    edge_class: canonical
    source_type: table
    target_type: column
```

```yaml
candidate_edge:
  edge_id: edge.column.settlement.gst_on_mp_fees.belongs_to_table.table.flipkart.settlement
  edge_type: BELONGS_TO_TABLE
  source: column.settlement.gst_on_mp_fees
  target: table.flipkart.settlement
  fields:
    edge_family: data_understanding
    evidence_basis: column.fields.table_id
    confidence: high
    canonical_cognee_edge: true
    marketplace_only: true
    canonical_edge_type: BELONGS_TO_TABLE
    legacy_edge_aliases:
    - column_belongs_to_table
    inverse_edge_type: HAS_COLUMN
    materialize_inverse: true
    edge_class: canonical
    source_type: column
    target_type: table
```

```yaml
candidate_edge:
  edge_id: edge.table.flipkart.settlement.has_column.column.settlement.total_tcs_amount
  edge_type: HAS_COLUMN
  source: table.flipkart.settlement
  target: column.settlement.total_tcs_amount
  fields:
    edge_family: data_understanding
    evidence_basis: column.fields.table_id
    confidence: high
    canonical_cognee_edge: true
    marketplace_only: true
    canonical_edge_type: HAS_COLUMN
    inverse_edge_type: BELONGS_TO_TABLE
    materialize_inverse: true
    edge_class: canonical
    source_type: table
    target_type: column
```

```yaml
candidate_edge:
  edge_id: edge.column.settlement.total_tcs_amount.belongs_to_table.table.flipkart.settlement
  edge_type: BELONGS_TO_TABLE
  source: column.settlement.total_tcs_amount
  target: table.flipkart.settlement
  fields:
    edge_family: data_understanding
    evidence_basis: column.fields.table_id
    confidence: high
    canonical_cognee_edge: true
    marketplace_only: true
    canonical_edge_type: BELONGS_TO_TABLE
    legacy_edge_aliases:
    - column_belongs_to_table
    inverse_edge_type: HAS_COLUMN
    materialize_inverse: true
    edge_class: canonical
    source_type: column
    target_type: table
```

```yaml
candidate_edge:
  edge_id: edge.table.flipkart.settlement.has_column.column.settlement.total_tds_amount
  edge_type: HAS_COLUMN
  source: table.flipkart.settlement
  target: column.settlement.total_tds_amount
  fields:
    edge_family: data_understanding
    evidence_basis: column.fields.table_id
    confidence: high
    canonical_cognee_edge: true
    marketplace_only: true
    canonical_edge_type: HAS_COLUMN
    inverse_edge_type: BELONGS_TO_TABLE
    materialize_inverse: true
    edge_class: canonical
    source_type: table
    target_type: column
```

```yaml
candidate_edge:
  edge_id: edge.column.settlement.total_tds_amount.belongs_to_table.table.flipkart.settlement
  edge_type: BELONGS_TO_TABLE
  source: column.settlement.total_tds_amount
  target: table.flipkart.settlement
  fields:
    edge_family: data_understanding
    evidence_basis: column.fields.table_id
    confidence: high
    canonical_cognee_edge: true
    marketplace_only: true
    canonical_edge_type: BELONGS_TO_TABLE
    legacy_edge_aliases:
    - column_belongs_to_table
    inverse_edge_type: HAS_COLUMN
    materialize_inverse: true
    edge_class: canonical
    source_type: column
    target_type: table
```

```yaml
candidate_edge:
  edge_id: edge.table.flipkart.settlement.has_column.column.settlement.commission_fee
  edge_type: HAS_COLUMN
  source: table.flipkart.settlement
  target: column.settlement.commission_fee
  fields:
    edge_family: data_understanding
    evidence_basis: column.fields.table_id
    confidence: high
    canonical_cognee_edge: true
    marketplace_only: true
    canonical_edge_type: HAS_COLUMN
    inverse_edge_type: BELONGS_TO_TABLE
    materialize_inverse: true
    edge_class: canonical
    source_type: table
    target_type: column
```

```yaml
candidate_edge:
  edge_id: edge.column.settlement.commission_fee.belongs_to_table.table.flipkart.settlement
  edge_type: BELONGS_TO_TABLE
  source: column.settlement.commission_fee
  target: table.flipkart.settlement
  fields:
    edge_family: data_understanding
    evidence_basis: column.fields.table_id
    confidence: high
    canonical_cognee_edge: true
    marketplace_only: true
    canonical_edge_type: BELONGS_TO_TABLE
    legacy_edge_aliases:
    - column_belongs_to_table
    inverse_edge_type: HAS_COLUMN
    materialize_inverse: true
    edge_class: canonical
    source_type: column
    target_type: table
```

```yaml
candidate_edge:
  edge_id: edge.table.flipkart.settlement.has_column.column.settlement.shipping_fee
  edge_type: HAS_COLUMN
  source: table.flipkart.settlement
  target: column.settlement.shipping_fee
  fields:
    edge_family: data_understanding
    evidence_basis: column.fields.table_id
    confidence: high
    canonical_cognee_edge: true
    marketplace_only: true
    canonical_edge_type: HAS_COLUMN
    inverse_edge_type: BELONGS_TO_TABLE
    materialize_inverse: true
    edge_class: canonical
    source_type: table
    target_type: column
```

```yaml
candidate_edge:
  edge_id: edge.column.settlement.shipping_fee.belongs_to_table.table.flipkart.settlement
  edge_type: BELONGS_TO_TABLE
  source: column.settlement.shipping_fee
  target: table.flipkart.settlement
  fields:
    edge_family: data_understanding
    evidence_basis: column.fields.table_id
    confidence: high
    canonical_cognee_edge: true
    marketplace_only: true
    canonical_edge_type: BELONGS_TO_TABLE
    legacy_edge_aliases:
    - column_belongs_to_table
    inverse_edge_type: HAS_COLUMN
    materialize_inverse: true
    edge_class: canonical
    source_type: column
    target_type: table
```

```yaml
candidate_edge:
  edge_id: edge.table.flipkart.settlement.has_column.column.settlement.fixed_fee
  edge_type: HAS_COLUMN
  source: table.flipkart.settlement
  target: column.settlement.fixed_fee
  fields:
    edge_family: data_understanding
    evidence_basis: column.fields.table_id
    confidence: high
    canonical_cognee_edge: true
    marketplace_only: true
    canonical_edge_type: HAS_COLUMN
    inverse_edge_type: BELONGS_TO_TABLE
    materialize_inverse: true
    edge_class: canonical
    source_type: table
    target_type: column
```

```yaml
candidate_edge:
  edge_id: edge.column.settlement.fixed_fee.belongs_to_table.table.flipkart.settlement
  edge_type: BELONGS_TO_TABLE
  source: column.settlement.fixed_fee
  target: table.flipkart.settlement
  fields:
    edge_family: data_understanding
    evidence_basis: column.fields.table_id
    confidence: high
    canonical_cognee_edge: true
    marketplace_only: true
    canonical_edge_type: BELONGS_TO_TABLE
    legacy_edge_aliases:
    - column_belongs_to_table
    inverse_edge_type: HAS_COLUMN
    materialize_inverse: true
    edge_class: canonical
    source_type: column
    target_type: table
```

```yaml
candidate_edge:
  edge_id: edge.table.flipkart.settlement.has_column.column.settlement.reverse_shipping_fee
  edge_type: HAS_COLUMN
  source: table.flipkart.settlement
  target: column.settlement.reverse_shipping_fee
  fields:
    edge_family: data_understanding
    evidence_basis: column.fields.table_id
    confidence: high
    canonical_cognee_edge: true
    marketplace_only: true
    canonical_edge_type: HAS_COLUMN
    inverse_edge_type: BELONGS_TO_TABLE
    materialize_inverse: true
    edge_class: canonical
    source_type: table
    target_type: column
```

```yaml
candidate_edge:
  edge_id: edge.column.settlement.reverse_shipping_fee.belongs_to_table.table.flipkart.settlement
  edge_type: BELONGS_TO_TABLE
  source: column.settlement.reverse_shipping_fee
  target: table.flipkart.settlement
  fields:
    edge_family: data_understanding
    evidence_basis: column.fields.table_id
    confidence: high
    canonical_cognee_edge: true
    marketplace_only: true
    canonical_edge_type: BELONGS_TO_TABLE
    legacy_edge_aliases:
    - column_belongs_to_table
    inverse_edge_type: HAS_COLUMN
    materialize_inverse: true
    edge_class: canonical
    source_type: column
    target_type: table
```

```yaml
candidate_edge:
  edge_id: edge.table.flipkart.settlement.has_column.column.settlement.collection_fee
  edge_type: HAS_COLUMN
  source: table.flipkart.settlement
  target: column.settlement.collection_fee
  fields:
    edge_family: data_understanding
    evidence_basis: column.fields.table_id
    confidence: high
    canonical_cognee_edge: true
    marketplace_only: true
    canonical_edge_type: HAS_COLUMN
    inverse_edge_type: BELONGS_TO_TABLE
    materialize_inverse: true
    edge_class: canonical
    source_type: table
    target_type: column
```

```yaml
candidate_edge:
  edge_id: edge.column.settlement.collection_fee.belongs_to_table.table.flipkart.settlement
  edge_type: BELONGS_TO_TABLE
  source: column.settlement.collection_fee
  target: table.flipkart.settlement
  fields:
    edge_family: data_understanding
    evidence_basis: column.fields.table_id
    confidence: high
    canonical_cognee_edge: true
    marketplace_only: true
    canonical_edge_type: BELONGS_TO_TABLE
    legacy_edge_aliases:
    - column_belongs_to_table
    inverse_edge_type: HAS_COLUMN
    materialize_inverse: true
    edge_class: canonical
    source_type: column
    target_type: table
```

```yaml
candidate_edge:
  edge_id: edge.table.flipkart.settlement.has_column.column.settlement.franchise_fee
  edge_type: HAS_COLUMN
  source: table.flipkart.settlement
  target: column.settlement.franchise_fee
  fields:
    edge_family: data_understanding
    evidence_basis: column.fields.table_id
    confidence: high
    canonical_cognee_edge: true
    marketplace_only: true
    canonical_edge_type: HAS_COLUMN
    inverse_edge_type: BELONGS_TO_TABLE
    materialize_inverse: true
    edge_class: canonical
    source_type: table
    target_type: column
```

```yaml
candidate_edge:
  edge_id: edge.column.settlement.franchise_fee.belongs_to_table.table.flipkart.settlement
  edge_type: BELONGS_TO_TABLE
  source: column.settlement.franchise_fee
  target: table.flipkart.settlement
  fields:
    edge_family: data_understanding
    evidence_basis: column.fields.table_id
    confidence: high
    canonical_cognee_edge: true
    marketplace_only: true
    canonical_edge_type: BELONGS_TO_TABLE
    legacy_edge_aliases:
    - column_belongs_to_table
    inverse_edge_type: HAS_COLUMN
    materialize_inverse: true
    edge_class: canonical
    source_type: column
    target_type: table
```

```yaml
candidate_edge:
  edge_id: edge.table.flipkart.settlement.has_column.column.settlement.pick_and_pack_fee
  edge_type: HAS_COLUMN
  source: table.flipkart.settlement
  target: column.settlement.pick_and_pack_fee
  fields:
    edge_family: data_understanding
    evidence_basis: column.fields.table_id
    confidence: high
    canonical_cognee_edge: true
    marketplace_only: true
    canonical_edge_type: HAS_COLUMN
    inverse_edge_type: BELONGS_TO_TABLE
    materialize_inverse: true
    edge_class: canonical
    source_type: table
    target_type: column
```

```yaml
candidate_edge:
  edge_id: edge.column.settlement.pick_and_pack_fee.belongs_to_table.table.flipkart.settlement
  edge_type: BELONGS_TO_TABLE
  source: column.settlement.pick_and_pack_fee
  target: table.flipkart.settlement
  fields:
    edge_family: data_understanding
    evidence_basis: column.fields.table_id
    confidence: high
    canonical_cognee_edge: true
    marketplace_only: true
    canonical_edge_type: BELONGS_TO_TABLE
    legacy_edge_aliases:
    - column_belongs_to_table
    inverse_edge_type: HAS_COLUMN
    materialize_inverse: true
    edge_class: canonical
    source_type: column
    target_type: table
```

```yaml
candidate_edge:
  edge_id: edge.table.flipkart.settlement.has_column.column.settlement.neft_type
  edge_type: HAS_COLUMN
  source: table.flipkart.settlement
  target: column.settlement.neft_type
  fields:
    edge_family: data_understanding
    evidence_basis: column.fields.table_id
    confidence: high
    canonical_cognee_edge: true
    marketplace_only: true
    canonical_edge_type: HAS_COLUMN
    inverse_edge_type: BELONGS_TO_TABLE
    materialize_inverse: true
    edge_class: canonical
    source_type: table
    target_type: column
```

```yaml
candidate_edge:
  edge_id: edge.column.settlement.neft_type.belongs_to_table.table.flipkart.settlement
  edge_type: BELONGS_TO_TABLE
  source: column.settlement.neft_type
  target: table.flipkart.settlement
  fields:
    edge_family: data_understanding
    evidence_basis: column.fields.table_id
    confidence: high
    canonical_cognee_edge: true
    marketplace_only: true
    canonical_edge_type: BELONGS_TO_TABLE
    legacy_edge_aliases:
    - column_belongs_to_table
    inverse_edge_type: HAS_COLUMN
    materialize_inverse: true
    edge_class: canonical
    source_type: column
    target_type: table
```

```yaml
candidate_edge:
  edge_id: edge.table.flipkart.settlement.has_column.column.settlement.vendor_payout
  edge_type: HAS_COLUMN
  source: table.flipkart.settlement
  target: column.settlement.vendor_payout
  fields:
    edge_family: data_understanding
    evidence_basis: column.fields.table_id
    confidence: high
    canonical_cognee_edge: true
    marketplace_only: true
    canonical_edge_type: HAS_COLUMN
    inverse_edge_type: BELONGS_TO_TABLE
    materialize_inverse: true
    edge_class: canonical
    source_type: table
    target_type: column
```

```yaml
candidate_edge:
  edge_id: edge.column.settlement.vendor_payout.belongs_to_table.table.flipkart.settlement
  edge_type: BELONGS_TO_TABLE
  source: column.settlement.vendor_payout
  target: table.flipkart.settlement
  fields:
    edge_family: data_understanding
    evidence_basis: column.fields.table_id
    confidence: high
    canonical_cognee_edge: true
    marketplace_only: true
    canonical_edge_type: BELONGS_TO_TABLE
    legacy_edge_aliases:
    - column_belongs_to_table
    inverse_edge_type: HAS_COLUMN
    materialize_inverse: true
    edge_class: canonical
    source_type: column
    target_type: table
```

```yaml
candidate_edge:
  edge_id: edge.table.flipkart.settlement.has_column.column.settlement.settlement_date
  edge_type: HAS_COLUMN
  source: table.flipkart.settlement
  target: column.settlement.settlement_date
  fields:
    edge_family: data_understanding
    evidence_basis: column.fields.table_id
    confidence: high
    canonical_cognee_edge: true
    marketplace_only: true
    canonical_edge_type: HAS_COLUMN
    inverse_edge_type: BELONGS_TO_TABLE
    materialize_inverse: true
    edge_class: canonical
    source_type: table
    target_type: column
```

```yaml
candidate_edge:
  edge_id: edge.column.settlement.settlement_date.belongs_to_table.table.flipkart.settlement
  edge_type: BELONGS_TO_TABLE
  source: column.settlement.settlement_date
  target: table.flipkart.settlement
  fields:
    edge_family: data_understanding
    evidence_basis: column.fields.table_id
    confidence: high
    canonical_cognee_edge: true
    marketplace_only: true
    canonical_edge_type: BELONGS_TO_TABLE
    legacy_edge_aliases:
    - column_belongs_to_table
    inverse_edge_type: HAS_COLUMN
    materialize_inverse: true
    edge_class: canonical
    source_type: column
    target_type: table
```

```yaml
candidate_edge:
  edge_id: edge.table.flipkart.settlement.has_column.column.settlement.created_date
  edge_type: HAS_COLUMN
  source: table.flipkart.settlement
  target: column.settlement.created_date
  fields:
    edge_family: data_understanding
    evidence_basis: column.fields.table_id
    confidence: high
    canonical_cognee_edge: true
    marketplace_only: true
    canonical_edge_type: HAS_COLUMN
    inverse_edge_type: BELONGS_TO_TABLE
    materialize_inverse: true
    edge_class: canonical
    source_type: table
    target_type: column
```

```yaml
candidate_edge:
  edge_id: edge.column.settlement.created_date.belongs_to_table.table.flipkart.settlement
  edge_type: BELONGS_TO_TABLE
  source: column.settlement.created_date
  target: table.flipkart.settlement
  fields:
    edge_family: data_understanding
    evidence_basis: column.fields.table_id
    confidence: high
    canonical_cognee_edge: true
    marketplace_only: true
    canonical_edge_type: BELONGS_TO_TABLE
    legacy_edge_aliases:
    - column_belongs_to_table
    inverse_edge_type: HAS_COLUMN
    materialize_inverse: true
    edge_class: canonical
    source_type: column
    target_type: table
```



```yaml
candidate_edge:
  edge_id: edge.table.flipkart.settlement.has_column.column.settlement.fulfilment_type
  edge_type: HAS_COLUMN
  source: table.flipkart.settlement
  target: column.settlement.fulfilment_type
  fields:
    edge_family: data_understanding
    evidence_basis: column.fields.table_id
    confidence: high
    canonical_cognee_edge: true
    marketplace_only: true
    canonical_edge_type: HAS_COLUMN
    inverse_edge_type: BELONGS_TO_TABLE
    materialize_inverse: true
    edge_class: canonical
    source_type: table
    target_type: column
```

```yaml
candidate_edge:
  edge_id: edge.column.settlement.fulfilment_type.belongs_to_table.table.flipkart.settlement
  edge_type: BELONGS_TO_TABLE
  source: column.settlement.fulfilment_type
  target: table.flipkart.settlement
  fields:
    edge_family: data_understanding
    evidence_basis: column.fields.table_id
    confidence: high
    canonical_cognee_edge: true
    marketplace_only: true
    canonical_edge_type: BELONGS_TO_TABLE
    legacy_edge_aliases:
    - column_belongs_to_table
    inverse_edge_type: HAS_COLUMN
    materialize_inverse: true
    edge_class: canonical
    source_type: column
    target_type: table
```

```yaml
candidate_edge:
  edge_id: edge.table.flipkart.settlement.has_column.column.settlement.return_type
  edge_type: HAS_COLUMN
  source: table.flipkart.settlement
  target: column.settlement.return_type
  fields:
    edge_family: data_understanding
    evidence_basis: column.fields.table_id
    confidence: high
    canonical_cognee_edge: true
    marketplace_only: true
    canonical_edge_type: HAS_COLUMN
    inverse_edge_type: BELONGS_TO_TABLE
    materialize_inverse: true
    edge_class: canonical
    source_type: table
    target_type: column
```

```yaml
candidate_edge:
  edge_id: edge.column.settlement.return_type.belongs_to_table.table.flipkart.settlement
  edge_type: BELONGS_TO_TABLE
  source: column.settlement.return_type
  target: table.flipkart.settlement
  fields:
    edge_family: data_understanding
    evidence_basis: column.fields.table_id
    confidence: high
    canonical_cognee_edge: true
    marketplace_only: true
    canonical_edge_type: BELONGS_TO_TABLE
    legacy_edge_aliases:
    - column_belongs_to_table
    inverse_edge_type: HAS_COLUMN
    materialize_inverse: true
    edge_class: canonical
    source_type: column
    target_type: table
```

```yaml
candidate_edge:
  edge_id: edge.table.flipkart.settlement.has_column.column.settlement.zone
  edge_type: HAS_COLUMN
  source: table.flipkart.settlement
  target: column.settlement.zone
  fields:
    edge_family: data_understanding
    evidence_basis: column.fields.table_id
    confidence: high
    canonical_cognee_edge: true
    marketplace_only: true
    canonical_edge_type: HAS_COLUMN
    inverse_edge_type: BELONGS_TO_TABLE
    materialize_inverse: true
    edge_class: canonical
    source_type: table
    target_type: column
```

```yaml
candidate_edge:
  edge_id: edge.column.settlement.zone.belongs_to_table.table.flipkart.settlement
  edge_type: BELONGS_TO_TABLE
  source: column.settlement.zone
  target: table.flipkart.settlement
  fields:
    edge_family: data_understanding
    evidence_basis: column.fields.table_id
    confidence: high
    canonical_cognee_edge: true
    marketplace_only: true
    canonical_edge_type: BELONGS_TO_TABLE
    legacy_edge_aliases:
    - column_belongs_to_table
    inverse_edge_type: HAS_COLUMN
    materialize_inverse: true
    edge_class: canonical
    source_type: column
    target_type: table
```

```yaml
candidate_edge:
  edge_id: edge.table.flipkart.settlement.has_column.column.settlement.tier
  edge_type: HAS_COLUMN
  source: table.flipkart.settlement
  target: column.settlement.tier
  fields:
    edge_family: data_understanding
    evidence_basis: column.fields.table_id
    confidence: high
    canonical_cognee_edge: true
    marketplace_only: true
    canonical_edge_type: HAS_COLUMN
    inverse_edge_type: BELONGS_TO_TABLE
    materialize_inverse: true
    edge_class: canonical
    source_type: table
    target_type: column
```

```yaml
candidate_edge:
  edge_id: edge.column.settlement.tier.belongs_to_table.table.flipkart.settlement
  edge_type: BELONGS_TO_TABLE
  source: column.settlement.tier
  target: table.flipkart.settlement
  fields:
    edge_family: data_understanding
    evidence_basis: column.fields.table_id
    confidence: high
    canonical_cognee_edge: true
    marketplace_only: true
    canonical_edge_type: BELONGS_TO_TABLE
    legacy_edge_aliases:
    - column_belongs_to_table
    inverse_edge_type: HAS_COLUMN
    materialize_inverse: true
    edge_class: canonical
    source_type: column
    target_type: table
```

```yaml
candidate_edge:
  edge_id: edge.table.flipkart.settlement.has_column.column.settlement.gross_weight
  edge_type: HAS_COLUMN
  source: table.flipkart.settlement
  target: column.settlement.gross_weight
  fields:
    edge_family: data_understanding
    evidence_basis: column.fields.table_id
    confidence: high
    canonical_cognee_edge: true
    marketplace_only: true
    canonical_edge_type: HAS_COLUMN
    inverse_edge_type: BELONGS_TO_TABLE
    materialize_inverse: true
    edge_class: canonical
    source_type: table
    target_type: column
```

```yaml
candidate_edge:
  edge_id: edge.column.settlement.gross_weight.belongs_to_table.table.flipkart.settlement
  edge_type: BELONGS_TO_TABLE
  source: column.settlement.gross_weight
  target: table.flipkart.settlement
  fields:
    edge_family: data_understanding
    evidence_basis: column.fields.table_id
    confidence: high
    canonical_cognee_edge: true
    marketplace_only: true
    canonical_edge_type: BELONGS_TO_TABLE
    legacy_edge_aliases:
    - column_belongs_to_table
    inverse_edge_type: HAS_COLUMN
    materialize_inverse: true
    edge_class: canonical
    source_type: column
    target_type: table
```

```yaml
candidate_edge:
  edge_id: edge.table.flipkart.settlement.has_column.column.settlement.vol_weight
  edge_type: HAS_COLUMN
  source: table.flipkart.settlement
  target: column.settlement.vol_weight
  fields:
    edge_family: data_understanding
    evidence_basis: column.fields.table_id
    confidence: high
    canonical_cognee_edge: true
    marketplace_only: true
    canonical_edge_type: HAS_COLUMN
    inverse_edge_type: BELONGS_TO_TABLE
    materialize_inverse: true
    edge_class: canonical
    source_type: table
    target_type: column
```

```yaml
candidate_edge:
  edge_id: edge.column.settlement.vol_weight.belongs_to_table.table.flipkart.settlement
  edge_type: BELONGS_TO_TABLE
  source: column.settlement.vol_weight
  target: table.flipkart.settlement
  fields:
    edge_family: data_understanding
    evidence_basis: column.fields.table_id
    confidence: high
    canonical_cognee_edge: true
    marketplace_only: true
    canonical_edge_type: BELONGS_TO_TABLE
    legacy_edge_aliases:
    - column_belongs_to_table
    inverse_edge_type: HAS_COLUMN
    materialize_inverse: true
    edge_class: canonical
    source_type: column
    target_type: table
```

```yaml
candidate_edge:
  edge_id: edge.table.flipkart.settlement.has_column.column.settlement.is_active
  edge_type: HAS_COLUMN
  source: table.flipkart.settlement
  target: column.settlement.is_active
  fields:
    edge_family: data_understanding
    evidence_basis: column.fields.table_id
    confidence: high
    canonical_cognee_edge: true
    marketplace_only: true
    canonical_edge_type: HAS_COLUMN
    inverse_edge_type: BELONGS_TO_TABLE
    materialize_inverse: true
    edge_class: canonical
    source_type: table
    target_type: column
```

```yaml
candidate_edge:
  edge_id: edge.column.settlement.is_active.belongs_to_table.table.flipkart.settlement
  edge_type: BELONGS_TO_TABLE
  source: column.settlement.is_active
  target: table.flipkart.settlement
  fields:
    edge_family: data_understanding
    evidence_basis: column.fields.table_id
    confidence: high
    canonical_cognee_edge: true
    marketplace_only: true
    canonical_edge_type: BELONGS_TO_TABLE
    legacy_edge_aliases:
    - column_belongs_to_table
    inverse_edge_type: HAS_COLUMN
    materialize_inverse: true
    edge_class: canonical
    source_type: column
    target_type: table
```

```yaml
candidate_edge:
  edge_id: edge.table.flipkart.settlement.has_column.column.settlement.is_duplicated
  edge_type: HAS_COLUMN
  source: table.flipkart.settlement
  target: column.settlement.is_duplicated
  fields:
    edge_family: data_understanding
    evidence_basis: column.fields.table_id
    confidence: high
    canonical_cognee_edge: true
    marketplace_only: true
    canonical_edge_type: HAS_COLUMN
    inverse_edge_type: BELONGS_TO_TABLE
    materialize_inverse: true
    edge_class: canonical
    source_type: table
    target_type: column
```

```yaml
candidate_edge:
  edge_id: edge.column.settlement.is_duplicated.belongs_to_table.table.flipkart.settlement
  edge_type: BELONGS_TO_TABLE
  source: column.settlement.is_duplicated
  target: table.flipkart.settlement
  fields:
    edge_family: data_understanding
    evidence_basis: column.fields.table_id
    confidence: high
    canonical_cognee_edge: true
    marketplace_only: true
    canonical_edge_type: BELONGS_TO_TABLE
    legacy_edge_aliases:
    - column_belongs_to_table
    inverse_edge_type: HAS_COLUMN
    materialize_inverse: true
    edge_class: canonical
    source_type: column
    target_type: table
```

```yaml
candidate_edge:
  edge_id: edge.table.flipkart.settlement.has_column.column.settlement.zen_status
  edge_type: HAS_COLUMN
  source: table.flipkart.settlement
  target: column.settlement.zen_status
  fields:
    edge_family: data_understanding
    evidence_basis: column.fields.table_id
    confidence: high
    canonical_cognee_edge: true
    marketplace_only: true
    canonical_edge_type: HAS_COLUMN
    inverse_edge_type: BELONGS_TO_TABLE
    materialize_inverse: true
    edge_class: canonical
    source_type: table
    target_type: column
```

```yaml
candidate_edge:
  edge_id: edge.column.settlement.zen_status.belongs_to_table.table.flipkart.settlement
  edge_type: BELONGS_TO_TABLE
  source: column.settlement.zen_status
  target: table.flipkart.settlement
  fields:
    edge_family: data_understanding
    evidence_basis: column.fields.table_id
    confidence: high
    canonical_cognee_edge: true
    marketplace_only: true
    canonical_edge_type: BELONGS_TO_TABLE
    legacy_edge_aliases:
    - column_belongs_to_table
    inverse_edge_type: HAS_COLUMN
    materialize_inverse: true
    edge_class: canonical
    source_type: column
    target_type: table
```

```yaml
candidate_edge:
  edge_id: edge.table.flipkart.settlement.has_column.column.settlement.group_level_id
  edge_type: HAS_COLUMN
  source: table.flipkart.settlement
  target: column.settlement.group_level_id
  fields:
    edge_family: data_understanding
    evidence_basis: column.fields.table_id
    confidence: high
    canonical_cognee_edge: true
    marketplace_only: true
    canonical_edge_type: HAS_COLUMN
    inverse_edge_type: BELONGS_TO_TABLE
    materialize_inverse: true
    edge_class: canonical
    source_type: table
    target_type: column
```

```yaml
candidate_edge:
  edge_id: edge.column.settlement.group_level_id.belongs_to_table.table.flipkart.settlement
  edge_type: BELONGS_TO_TABLE
  source: column.settlement.group_level_id
  target: table.flipkart.settlement
  fields:
    edge_family: data_understanding
    evidence_basis: column.fields.table_id
    confidence: high
    canonical_cognee_edge: true
    marketplace_only: true
    canonical_edge_type: BELONGS_TO_TABLE
    legacy_edge_aliases:
    - column_belongs_to_table
    inverse_edge_type: HAS_COLUMN
    materialize_inverse: true
    edge_class: canonical
    source_type: column
    target_type: table
```

```yaml
candidate_edge:
  edge_id: edge.table.flipkart.settlement.has_column.column.settlement.group_id
  edge_type: HAS_COLUMN
  source: table.flipkart.settlement
  target: column.settlement.group_id
  fields:
    edge_family: data_understanding
    evidence_basis: column.fields.table_id
    confidence: high
    canonical_cognee_edge: true
    marketplace_only: true
    canonical_edge_type: HAS_COLUMN
    inverse_edge_type: BELONGS_TO_TABLE
    materialize_inverse: true
    edge_class: canonical
    source_type: table
    target_type: column
```

```yaml
candidate_edge:
  edge_id: edge.column.settlement.group_id.belongs_to_table.table.flipkart.settlement
  edge_type: BELONGS_TO_TABLE
  source: column.settlement.group_id
  target: table.flipkart.settlement
  fields:
    edge_family: data_understanding
    evidence_basis: column.fields.table_id
    confidence: high
    canonical_cognee_edge: true
    marketplace_only: true
    canonical_edge_type: BELONGS_TO_TABLE
    legacy_edge_aliases:
    - column_belongs_to_table
    inverse_edge_type: HAS_COLUMN
    materialize_inverse: true
    edge_class: canonical
    source_type: column
    target_type: table
```

```yaml
candidate_edge:
  edge_id: edge.table.flipkart.commission.has_column.column.commission.order_id
  edge_type: HAS_COLUMN
  source: table.flipkart.commission
  target: column.commission.order_id
  fields:
    edge_family: data_understanding
    evidence_basis: column.fields.table_id
    confidence: high
    canonical_cognee_edge: true
    marketplace_only: true
    canonical_edge_type: HAS_COLUMN
    inverse_edge_type: BELONGS_TO_TABLE
    materialize_inverse: true
    edge_class: canonical
    source_type: table
    target_type: column
```

```yaml
candidate_edge:
  edge_id: edge.column.commission.order_id.belongs_to_table.table.flipkart.commission
  edge_type: BELONGS_TO_TABLE
  source: column.commission.order_id
  target: table.flipkart.commission
  fields:
    edge_family: data_understanding
    evidence_basis: column.fields.table_id
    confidence: high
    canonical_cognee_edge: true
    marketplace_only: true
    canonical_edge_type: BELONGS_TO_TABLE
    legacy_edge_aliases:
    - column_belongs_to_table
    inverse_edge_type: HAS_COLUMN
    materialize_inverse: true
    edge_class: canonical
    source_type: column
    target_type: table
```

```yaml
candidate_edge:
  edge_id: edge.table.flipkart.commission.has_column.column.commission.item_id
  edge_type: HAS_COLUMN
  source: table.flipkart.commission
  target: column.commission.item_id
  fields:
    edge_family: data_understanding
    evidence_basis: column.fields.table_id
    confidence: high
    canonical_cognee_edge: true
    marketplace_only: true
    canonical_edge_type: HAS_COLUMN
    inverse_edge_type: BELONGS_TO_TABLE
    materialize_inverse: true
    edge_class: canonical
    source_type: table
    target_type: column
```

```yaml
candidate_edge:
  edge_id: edge.column.commission.item_id.belongs_to_table.table.flipkart.commission
  edge_type: BELONGS_TO_TABLE
  source: column.commission.item_id
  target: table.flipkart.commission
  fields:
    edge_family: data_understanding
    evidence_basis: column.fields.table_id
    confidence: high
    canonical_cognee_edge: true
    marketplace_only: true
    canonical_edge_type: BELONGS_TO_TABLE
    legacy_edge_aliases:
    - column_belongs_to_table
    inverse_edge_type: HAS_COLUMN
    materialize_inverse: true
    edge_class: canonical
    source_type: column
    target_type: table
```

```yaml
candidate_edge:
  edge_id: edge.table.flipkart.commission.has_column.column.commission.invoice_number
  edge_type: HAS_COLUMN
  source: table.flipkart.commission
  target: column.commission.invoice_number
  fields:
    edge_family: data_understanding
    evidence_basis: column.fields.table_id
    confidence: high
    canonical_cognee_edge: true
    marketplace_only: true
    canonical_edge_type: HAS_COLUMN
    inverse_edge_type: BELONGS_TO_TABLE
    materialize_inverse: true
    edge_class: canonical
    source_type: table
    target_type: column
```

```yaml
candidate_edge:
  edge_id: edge.column.commission.invoice_number.belongs_to_table.table.flipkart.commission
  edge_type: BELONGS_TO_TABLE
  source: column.commission.invoice_number
  target: table.flipkart.commission
  fields:
    edge_family: data_understanding
    evidence_basis: column.fields.table_id
    confidence: high
    canonical_cognee_edge: true
    marketplace_only: true
    canonical_edge_type: BELONGS_TO_TABLE
    legacy_edge_aliases:
    - column_belongs_to_table
    inverse_edge_type: HAS_COLUMN
    materialize_inverse: true
    edge_class: canonical
    source_type: column
    target_type: table
```

```yaml
candidate_edge:
  edge_id: edge.table.flipkart.commission.has_column.column.commission.description
  edge_type: HAS_COLUMN
  source: table.flipkart.commission
  target: column.commission.description
  fields:
    edge_family: data_understanding
    evidence_basis: column.fields.table_id
    confidence: high
    canonical_cognee_edge: true
    marketplace_only: true
    canonical_edge_type: HAS_COLUMN
    inverse_edge_type: BELONGS_TO_TABLE
    materialize_inverse: true
    edge_class: canonical
    source_type: table
    target_type: column
```

```yaml
candidate_edge:
  edge_id: edge.column.commission.description.belongs_to_table.table.flipkart.commission
  edge_type: BELONGS_TO_TABLE
  source: column.commission.description
  target: table.flipkart.commission
  fields:
    edge_family: data_understanding
    evidence_basis: column.fields.table_id
    confidence: high
    canonical_cognee_edge: true
    marketplace_only: true
    canonical_edge_type: BELONGS_TO_TABLE
    legacy_edge_aliases:
    - column_belongs_to_table
    inverse_edge_type: HAS_COLUMN
    materialize_inverse: true
    edge_class: canonical
    source_type: column
    target_type: table
```

```yaml
candidate_edge:
  edge_id: edge.table.flipkart.commission.has_column.column.commission.fee_name
  edge_type: HAS_COLUMN
  source: table.flipkart.commission
  target: column.commission.fee_name
  fields:
    edge_family: data_understanding
    evidence_basis: column.fields.table_id
    confidence: high
    canonical_cognee_edge: true
    marketplace_only: true
    canonical_edge_type: HAS_COLUMN
    inverse_edge_type: BELONGS_TO_TABLE
    materialize_inverse: true
    edge_class: canonical
    source_type: table
    target_type: column
```

```yaml
candidate_edge:
  edge_id: edge.column.commission.fee_name.belongs_to_table.table.flipkart.commission
  edge_type: BELONGS_TO_TABLE
  source: column.commission.fee_name
  target: table.flipkart.commission
  fields:
    edge_family: data_understanding
    evidence_basis: column.fields.table_id
    confidence: high
    canonical_cognee_edge: true
    marketplace_only: true
    canonical_edge_type: BELONGS_TO_TABLE
    legacy_edge_aliases:
    - column_belongs_to_table
    inverse_edge_type: HAS_COLUMN
    materialize_inverse: true
    edge_class: canonical
    source_type: column
    target_type: table
```

```yaml
candidate_edge:
  edge_id: edge.table.flipkart.commission.has_column.column.commission.charged_amount
  edge_type: HAS_COLUMN
  source: table.flipkart.commission
  target: column.commission.charged_amount
  fields:
    edge_family: data_understanding
    evidence_basis: column.fields.table_id
    confidence: high
    canonical_cognee_edge: true
    marketplace_only: true
    canonical_edge_type: HAS_COLUMN
    inverse_edge_type: BELONGS_TO_TABLE
    materialize_inverse: true
    edge_class: canonical
    source_type: table
    target_type: column
```

```yaml
candidate_edge:
  edge_id: edge.column.commission.charged_amount.belongs_to_table.table.flipkart.commission
  edge_type: BELONGS_TO_TABLE
  source: column.commission.charged_amount
  target: table.flipkart.commission
  fields:
    edge_family: data_understanding
    evidence_basis: column.fields.table_id
    confidence: high
    canonical_cognee_edge: true
    marketplace_only: true
    canonical_edge_type: BELONGS_TO_TABLE
    legacy_edge_aliases:
    - column_belongs_to_table
    inverse_edge_type: HAS_COLUMN
    materialize_inverse: true
    edge_class: canonical
    source_type: column
    target_type: table
```

```yaml
candidate_edge:
  edge_id: edge.table.flipkart.commission.has_column.column.commission.total_tax
  edge_type: HAS_COLUMN
  source: table.flipkart.commission
  target: column.commission.total_tax
  fields:
    edge_family: data_understanding
    evidence_basis: column.fields.table_id
    confidence: high
    canonical_cognee_edge: true
    marketplace_only: true
    canonical_edge_type: HAS_COLUMN
    inverse_edge_type: BELONGS_TO_TABLE
    materialize_inverse: true
    edge_class: canonical
    source_type: table
    target_type: column
```

```yaml
candidate_edge:
  edge_id: edge.column.commission.total_tax.belongs_to_table.table.flipkart.commission
  edge_type: BELONGS_TO_TABLE
  source: column.commission.total_tax
  target: table.flipkart.commission
  fields:
    edge_family: data_understanding
    evidence_basis: column.fields.table_id
    confidence: high
    canonical_cognee_edge: true
    marketplace_only: true
    canonical_edge_type: BELONGS_TO_TABLE
    legacy_edge_aliases:
    - column_belongs_to_table
    inverse_edge_type: HAS_COLUMN
    materialize_inverse: true
    edge_class: canonical
    source_type: column
    target_type: table
```

```yaml
candidate_edge:
  edge_id: edge.table.flipkart.commission.has_column.column.commission.fee_amount
  edge_type: HAS_COLUMN
  source: table.flipkart.commission
  target: column.commission.fee_amount
  fields:
    edge_family: data_understanding
    evidence_basis: column.fields.table_id
    confidence: high
    canonical_cognee_edge: true
    marketplace_only: true
    canonical_edge_type: HAS_COLUMN
    inverse_edge_type: BELONGS_TO_TABLE
    materialize_inverse: true
    edge_class: canonical
    source_type: table
    target_type: column
```

```yaml
candidate_edge:
  edge_id: edge.column.commission.fee_amount.belongs_to_table.table.flipkart.commission
  edge_type: BELONGS_TO_TABLE
  source: column.commission.fee_amount
  target: table.flipkart.commission
  fields:
    edge_family: data_understanding
    evidence_basis: column.fields.table_id
    confidence: high
    canonical_cognee_edge: true
    marketplace_only: true
    canonical_edge_type: BELONGS_TO_TABLE
    legacy_edge_aliases:
    - column_belongs_to_table
    inverse_edge_type: HAS_COLUMN
    materialize_inverse: true
    edge_class: canonical
    source_type: column
    target_type: table
```

```yaml
candidate_edge:
  edge_id: edge.table.flipkart.commission.has_column.column.commission.fee_waiver_amount
  edge_type: HAS_COLUMN
  source: table.flipkart.commission
  target: column.commission.fee_waiver_amount
  fields:
    edge_family: data_understanding
    evidence_basis: column.fields.table_id
    confidence: high
    canonical_cognee_edge: true
    marketplace_only: true
    canonical_edge_type: HAS_COLUMN
    inverse_edge_type: BELONGS_TO_TABLE
    materialize_inverse: true
    edge_class: canonical
    source_type: table
    target_type: column
```

```yaml
candidate_edge:
  edge_id: edge.column.commission.fee_waiver_amount.belongs_to_table.table.flipkart.commission
  edge_type: BELONGS_TO_TABLE
  source: column.commission.fee_waiver_amount
  target: table.flipkart.commission
  fields:
    edge_family: data_understanding
    evidence_basis: column.fields.table_id
    confidence: high
    canonical_cognee_edge: true
    marketplace_only: true
    canonical_edge_type: BELONGS_TO_TABLE
    legacy_edge_aliases:
    - column_belongs_to_table
    inverse_edge_type: HAS_COLUMN
    materialize_inverse: true
    edge_class: canonical
    source_type: column
    target_type: table
```







```yaml
candidate_edge:
  edge_id: edge.table.flipkart.commission.has_column.column.commission.created_date
  edge_type: HAS_COLUMN
  source: table.flipkart.commission
  target: column.commission.created_date
  fields:
    edge_family: data_understanding
    evidence_basis: column.fields.table_id
    confidence: high
    canonical_cognee_edge: true
    marketplace_only: true
    canonical_edge_type: HAS_COLUMN
    inverse_edge_type: BELONGS_TO_TABLE
    materialize_inverse: true
    edge_class: canonical
    source_type: table
    target_type: column
```

```yaml
candidate_edge:
  edge_id: edge.column.commission.created_date.belongs_to_table.table.flipkart.commission
  edge_type: BELONGS_TO_TABLE
  source: column.commission.created_date
  target: table.flipkart.commission
  fields:
    edge_family: data_understanding
    evidence_basis: column.fields.table_id
    confidence: high
    canonical_cognee_edge: true
    marketplace_only: true
    canonical_edge_type: BELONGS_TO_TABLE
    legacy_edge_aliases:
    - column_belongs_to_table
    inverse_edge_type: HAS_COLUMN
    materialize_inverse: true
    edge_class: canonical
    source_type: column
    target_type: table
```





```yaml
candidate_edge:
  edge_id: edge.table.flipkart.commission.has_column.column.commission.is_active
  edge_type: HAS_COLUMN
  source: table.flipkart.commission
  target: column.commission.is_active
  fields:
    edge_family: data_understanding
    evidence_basis: column.fields.table_id
    confidence: high
    canonical_cognee_edge: true
    marketplace_only: true
    canonical_edge_type: HAS_COLUMN
    inverse_edge_type: BELONGS_TO_TABLE
    materialize_inverse: true
    edge_class: canonical
    source_type: table
    target_type: column
```

```yaml
candidate_edge:
  edge_id: edge.column.commission.is_active.belongs_to_table.table.flipkart.commission
  edge_type: BELONGS_TO_TABLE
  source: column.commission.is_active
  target: table.flipkart.commission
  fields:
    edge_family: data_understanding
    evidence_basis: column.fields.table_id
    confidence: high
    canonical_cognee_edge: true
    marketplace_only: true
    canonical_edge_type: BELONGS_TO_TABLE
    legacy_edge_aliases:
    - column_belongs_to_table
    inverse_edge_type: HAS_COLUMN
    materialize_inverse: true
    edge_class: canonical
    source_type: column
    target_type: table
```

```yaml
candidate_edge:
  edge_id: edge.table.flipkart.commission.has_column.column.commission.group_level_id
  edge_type: HAS_COLUMN
  source: table.flipkart.commission
  target: column.commission.group_level_id
  fields:
    edge_family: data_understanding
    evidence_basis: column.fields.table_id
    confidence: high
    canonical_cognee_edge: true
    marketplace_only: true
    canonical_edge_type: HAS_COLUMN
    inverse_edge_type: BELONGS_TO_TABLE
    materialize_inverse: true
    edge_class: canonical
    source_type: table
    target_type: column
```

```yaml
candidate_edge:
  edge_id: edge.column.commission.group_level_id.belongs_to_table.table.flipkart.commission
  edge_type: BELONGS_TO_TABLE
  source: column.commission.group_level_id
  target: table.flipkart.commission
  fields:
    edge_family: data_understanding
    evidence_basis: column.fields.table_id
    confidence: high
    canonical_cognee_edge: true
    marketplace_only: true
    canonical_edge_type: BELONGS_TO_TABLE
    legacy_edge_aliases:
    - column_belongs_to_table
    inverse_edge_type: HAS_COLUMN
    materialize_inverse: true
    edge_class: canonical
    source_type: column
    target_type: table
```

```yaml
candidate_edge:
  edge_id: edge.table.flipkart.commission.has_column.column.commission.group_id
  edge_type: HAS_COLUMN
  source: table.flipkart.commission
  target: column.commission.group_id
  fields:
    edge_family: data_understanding
    evidence_basis: column.fields.table_id
    confidence: high
    canonical_cognee_edge: true
    marketplace_only: true
    canonical_edge_type: HAS_COLUMN
    inverse_edge_type: BELONGS_TO_TABLE
    materialize_inverse: true
    edge_class: canonical
    source_type: table
    target_type: column
```

```yaml
candidate_edge:
  edge_id: edge.column.commission.group_id.belongs_to_table.table.flipkart.commission
  edge_type: BELONGS_TO_TABLE
  source: column.commission.group_id
  target: table.flipkart.commission
  fields:
    edge_family: data_understanding
    evidence_basis: column.fields.table_id
    confidence: high
    canonical_cognee_edge: true
    marketplace_only: true
    canonical_edge_type: BELONGS_TO_TABLE
    legacy_edge_aliases:
    - column_belongs_to_table
    inverse_edge_type: HAS_COLUMN
    materialize_inverse: true
    edge_class: canonical
    source_type: column
    target_type: table
```

```yaml
candidate_edge:
  edge_id: edge.table.flipkart.cashback.has_column.column.cashback.order_id
  edge_type: HAS_COLUMN
  source: table.flipkart.cashback
  target: column.cashback.order_id
  fields:
    edge_family: data_understanding
    evidence_basis: column.fields.table_id
    confidence: high
    canonical_cognee_edge: true
    marketplace_only: true
    canonical_edge_type: HAS_COLUMN
    inverse_edge_type: BELONGS_TO_TABLE
    materialize_inverse: true
    edge_class: canonical
    source_type: table
    target_type: column
```

```yaml
candidate_edge:
  edge_id: edge.column.cashback.order_id.belongs_to_table.table.flipkart.cashback
  edge_type: BELONGS_TO_TABLE
  source: column.cashback.order_id
  target: table.flipkart.cashback
  fields:
    edge_family: data_understanding
    evidence_basis: column.fields.table_id
    confidence: high
    canonical_cognee_edge: true
    marketplace_only: true
    canonical_edge_type: BELONGS_TO_TABLE
    legacy_edge_aliases:
    - column_belongs_to_table
    inverse_edge_type: HAS_COLUMN
    materialize_inverse: true
    edge_class: canonical
    source_type: column
    target_type: table
```

```yaml
candidate_edge:
  edge_id: edge.table.flipkart.cashback.has_column.column.cashback.item_id
  edge_type: HAS_COLUMN
  source: table.flipkart.cashback
  target: column.cashback.item_id
  fields:
    edge_family: data_understanding
    evidence_basis: column.fields.table_id
    confidence: high
    canonical_cognee_edge: true
    marketplace_only: true
    canonical_edge_type: HAS_COLUMN
    inverse_edge_type: BELONGS_TO_TABLE
    materialize_inverse: true
    edge_class: canonical
    source_type: table
    target_type: column
```

```yaml
candidate_edge:
  edge_id: edge.column.cashback.item_id.belongs_to_table.table.flipkart.cashback
  edge_type: BELONGS_TO_TABLE
  source: column.cashback.item_id
  target: table.flipkart.cashback
  fields:
    edge_family: data_understanding
    evidence_basis: column.fields.table_id
    confidence: high
    canonical_cognee_edge: true
    marketplace_only: true
    canonical_edge_type: BELONGS_TO_TABLE
    legacy_edge_aliases:
    - column_belongs_to_table
    inverse_edge_type: HAS_COLUMN
    materialize_inverse: true
    edge_class: canonical
    source_type: column
    target_type: table
```

```yaml
candidate_edge:
  edge_id: edge.table.flipkart.cashback.has_column.column.cashback.credit_debit_note_no
  edge_type: HAS_COLUMN
  source: table.flipkart.cashback
  target: column.cashback.credit_debit_note_no
  fields:
    edge_family: data_understanding
    evidence_basis: column.fields.table_id
    confidence: high
    canonical_cognee_edge: true
    marketplace_only: true
    canonical_edge_type: HAS_COLUMN
    inverse_edge_type: BELONGS_TO_TABLE
    materialize_inverse: true
    edge_class: canonical
    source_type: table
    target_type: column
```

```yaml
candidate_edge:
  edge_id: edge.column.cashback.credit_debit_note_no.belongs_to_table.table.flipkart.cashback
  edge_type: BELONGS_TO_TABLE
  source: column.cashback.credit_debit_note_no
  target: table.flipkart.cashback
  fields:
    edge_family: data_understanding
    evidence_basis: column.fields.table_id
    confidence: high
    canonical_cognee_edge: true
    marketplace_only: true
    canonical_edge_type: BELONGS_TO_TABLE
    legacy_edge_aliases:
    - column_belongs_to_table
    inverse_edge_type: HAS_COLUMN
    materialize_inverse: true
    edge_class: canonical
    source_type: column
    target_type: table
```

```yaml
candidate_edge:
  edge_id: edge.table.flipkart.cashback.has_column.column.cashback.invoice_number
  edge_type: HAS_COLUMN
  source: table.flipkart.cashback
  target: column.cashback.invoice_number
  fields:
    edge_family: data_understanding
    evidence_basis: column.fields.table_id
    confidence: high
    canonical_cognee_edge: true
    marketplace_only: true
    canonical_edge_type: HAS_COLUMN
    inverse_edge_type: BELONGS_TO_TABLE
    materialize_inverse: true
    edge_class: canonical
    source_type: table
    target_type: column
```

```yaml
candidate_edge:
  edge_id: edge.column.cashback.invoice_number.belongs_to_table.table.flipkart.cashback
  edge_type: BELONGS_TO_TABLE
  source: column.cashback.invoice_number
  target: table.flipkart.cashback
  fields:
    edge_family: data_understanding
    evidence_basis: column.fields.table_id
    confidence: high
    canonical_cognee_edge: true
    marketplace_only: true
    canonical_edge_type: BELONGS_TO_TABLE
    legacy_edge_aliases:
    - column_belongs_to_table
    inverse_edge_type: HAS_COLUMN
    materialize_inverse: true
    edge_class: canonical
    source_type: column
    target_type: table
```

```yaml
candidate_edge:
  edge_id: edge.table.flipkart.cashback.has_column.column.cashback.irn
  edge_type: HAS_COLUMN
  source: table.flipkart.cashback
  target: column.cashback.irn
  fields:
    edge_family: data_understanding
    evidence_basis: column.fields.table_id
    confidence: high
    canonical_cognee_edge: true
    marketplace_only: true
    canonical_edge_type: HAS_COLUMN
    inverse_edge_type: BELONGS_TO_TABLE
    materialize_inverse: true
    edge_class: canonical
    source_type: table
    target_type: column
```

```yaml
candidate_edge:
  edge_id: edge.column.cashback.irn.belongs_to_table.table.flipkart.cashback
  edge_type: BELONGS_TO_TABLE
  source: column.cashback.irn
  target: table.flipkart.cashback
  fields:
    edge_family: data_understanding
    evidence_basis: column.fields.table_id
    confidence: high
    canonical_cognee_edge: true
    marketplace_only: true
    canonical_edge_type: BELONGS_TO_TABLE
    legacy_edge_aliases:
    - column_belongs_to_table
    inverse_edge_type: HAS_COLUMN
    materialize_inverse: true
    edge_class: canonical
    source_type: column
    target_type: table
```

```yaml
candidate_edge:
  edge_id: edge.table.flipkart.cashback.has_column.column.cashback.transaction_type
  edge_type: HAS_COLUMN
  source: table.flipkart.cashback
  target: column.cashback.transaction_type
  fields:
    edge_family: data_understanding
    evidence_basis: column.fields.table_id
    confidence: high
    canonical_cognee_edge: true
    marketplace_only: true
    canonical_edge_type: HAS_COLUMN
    inverse_edge_type: BELONGS_TO_TABLE
    materialize_inverse: true
    edge_class: canonical
    source_type: table
    target_type: column
```

```yaml
candidate_edge:
  edge_id: edge.column.cashback.transaction_type.belongs_to_table.table.flipkart.cashback
  edge_type: BELONGS_TO_TABLE
  source: column.cashback.transaction_type
  target: table.flipkart.cashback
  fields:
    edge_family: data_understanding
    evidence_basis: column.fields.table_id
    confidence: high
    canonical_cognee_edge: true
    marketplace_only: true
    canonical_edge_type: BELONGS_TO_TABLE
    legacy_edge_aliases:
    - column_belongs_to_table
    inverse_edge_type: HAS_COLUMN
    materialize_inverse: true
    edge_class: canonical
    source_type: column
    target_type: table
```

```yaml
candidate_edge:
  edge_id: edge.table.flipkart.cashback.has_column.column.cashback.internal_transaction_type
  edge_type: HAS_COLUMN
  source: table.flipkart.cashback
  target: column.cashback.internal_transaction_type
  fields:
    edge_family: data_understanding
    evidence_basis: column.fields.table_id
    confidence: high
    canonical_cognee_edge: true
    marketplace_only: true
    canonical_edge_type: HAS_COLUMN
    inverse_edge_type: BELONGS_TO_TABLE
    materialize_inverse: true
    edge_class: canonical
    source_type: table
    target_type: column
```

```yaml
candidate_edge:
  edge_id: edge.column.cashback.internal_transaction_type.belongs_to_table.table.flipkart.cashback
  edge_type: BELONGS_TO_TABLE
  source: column.cashback.internal_transaction_type
  target: table.flipkart.cashback
  fields:
    edge_family: data_understanding
    evidence_basis: column.fields.table_id
    confidence: high
    canonical_cognee_edge: true
    marketplace_only: true
    canonical_edge_type: BELONGS_TO_TABLE
    legacy_edge_aliases:
    - column_belongs_to_table
    inverse_edge_type: HAS_COLUMN
    materialize_inverse: true
    edge_class: canonical
    source_type: column
    target_type: table
```

```yaml
candidate_edge:
  edge_id: edge.table.flipkart.cashback.has_column.column.cashback.document_type
  edge_type: HAS_COLUMN
  source: table.flipkart.cashback
  target: column.cashback.document_type
  fields:
    edge_family: data_understanding
    evidence_basis: column.fields.table_id
    confidence: high
    canonical_cognee_edge: true
    marketplace_only: true
    canonical_edge_type: HAS_COLUMN
    inverse_edge_type: BELONGS_TO_TABLE
    materialize_inverse: true
    edge_class: canonical
    source_type: table
    target_type: column
```

```yaml
candidate_edge:
  edge_id: edge.column.cashback.document_type.belongs_to_table.table.flipkart.cashback
  edge_type: BELONGS_TO_TABLE
  source: column.cashback.document_type
  target: table.flipkart.cashback
  fields:
    edge_family: data_understanding
    evidence_basis: column.fields.table_id
    confidence: high
    canonical_cognee_edge: true
    marketplace_only: true
    canonical_edge_type: BELONGS_TO_TABLE
    legacy_edge_aliases:
    - column_belongs_to_table
    inverse_edge_type: HAS_COLUMN
    materialize_inverse: true
    edge_class: canonical
    source_type: column
    target_type: table
```

```yaml
candidate_edge:
  edge_id: edge.table.flipkart.cashback.has_column.column.cashback.document_sub_type
  edge_type: HAS_COLUMN
  source: table.flipkart.cashback
  target: column.cashback.document_sub_type
  fields:
    edge_family: data_understanding
    evidence_basis: column.fields.table_id
    confidence: high
    canonical_cognee_edge: true
    marketplace_only: true
    canonical_edge_type: HAS_COLUMN
    inverse_edge_type: BELONGS_TO_TABLE
    materialize_inverse: true
    edge_class: canonical
    source_type: table
    target_type: column
```

```yaml
candidate_edge:
  edge_id: edge.column.cashback.document_sub_type.belongs_to_table.table.flipkart.cashback
  edge_type: BELONGS_TO_TABLE
  source: column.cashback.document_sub_type
  target: table.flipkart.cashback
  fields:
    edge_family: data_understanding
    evidence_basis: column.fields.table_id
    confidence: high
    canonical_cognee_edge: true
    marketplace_only: true
    canonical_edge_type: BELONGS_TO_TABLE
    legacy_edge_aliases:
    - column_belongs_to_table
    inverse_edge_type: HAS_COLUMN
    materialize_inverse: true
    edge_class: canonical
    source_type: column
    target_type: table
```

```yaml
candidate_edge:
  edge_id: edge.table.flipkart.cashback.has_column.column.cashback.charged_amount
  edge_type: HAS_COLUMN
  source: table.flipkart.cashback
  target: column.cashback.charged_amount
  fields:
    edge_family: data_understanding
    evidence_basis: column.fields.table_id
    confidence: high
    canonical_cognee_edge: true
    marketplace_only: true
    canonical_edge_type: HAS_COLUMN
    inverse_edge_type: BELONGS_TO_TABLE
    materialize_inverse: true
    edge_class: canonical
    source_type: table
    target_type: column
```

```yaml
candidate_edge:
  edge_id: edge.column.cashback.charged_amount.belongs_to_table.table.flipkart.cashback
  edge_type: BELONGS_TO_TABLE
  source: column.cashback.charged_amount
  target: table.flipkart.cashback
  fields:
    edge_family: data_understanding
    evidence_basis: column.fields.table_id
    confidence: high
    canonical_cognee_edge: true
    marketplace_only: true
    canonical_edge_type: BELONGS_TO_TABLE
    legacy_edge_aliases:
    - column_belongs_to_table
    inverse_edge_type: HAS_COLUMN
    materialize_inverse: true
    edge_class: canonical
    source_type: column
    target_type: table
```

```yaml
candidate_edge:
  edge_id: edge.table.flipkart.cashback.has_column.column.cashback.total_tax
  edge_type: HAS_COLUMN
  source: table.flipkart.cashback
  target: column.cashback.total_tax
  fields:
    edge_family: data_understanding
    evidence_basis: column.fields.table_id
    confidence: high
    canonical_cognee_edge: true
    marketplace_only: true
    canonical_edge_type: HAS_COLUMN
    inverse_edge_type: BELONGS_TO_TABLE
    materialize_inverse: true
    edge_class: canonical
    source_type: table
    target_type: column
```

```yaml
candidate_edge:
  edge_id: edge.column.cashback.total_tax.belongs_to_table.table.flipkart.cashback
  edge_type: BELONGS_TO_TABLE
  source: column.cashback.total_tax
  target: table.flipkart.cashback
  fields:
    edge_family: data_understanding
    evidence_basis: column.fields.table_id
    confidence: high
    canonical_cognee_edge: true
    marketplace_only: true
    canonical_edge_type: BELONGS_TO_TABLE
    legacy_edge_aliases:
    - column_belongs_to_table
    inverse_edge_type: HAS_COLUMN
    materialize_inverse: true
    edge_class: canonical
    source_type: column
    target_type: table
```

```yaml
candidate_edge:
  edge_id: edge.table.flipkart.cashback.has_column.column.cashback.fee_amount
  edge_type: HAS_COLUMN
  source: table.flipkart.cashback
  target: column.cashback.fee_amount
  fields:
    edge_family: data_understanding
    evidence_basis: column.fields.table_id
    confidence: high
    canonical_cognee_edge: true
    marketplace_only: true
    canonical_edge_type: HAS_COLUMN
    inverse_edge_type: BELONGS_TO_TABLE
    materialize_inverse: true
    edge_class: canonical
    source_type: table
    target_type: column
```

```yaml
candidate_edge:
  edge_id: edge.column.cashback.fee_amount.belongs_to_table.table.flipkart.cashback
  edge_type: BELONGS_TO_TABLE
  source: column.cashback.fee_amount
  target: table.flipkart.cashback
  fields:
    edge_family: data_understanding
    evidence_basis: column.fields.table_id
    confidence: high
    canonical_cognee_edge: true
    marketplace_only: true
    canonical_edge_type: BELONGS_TO_TABLE
    legacy_edge_aliases:
    - column_belongs_to_table
    inverse_edge_type: HAS_COLUMN
    materialize_inverse: true
    edge_class: canonical
    source_type: column
    target_type: table
```

```yaml
candidate_edge:
  edge_id: edge.table.flipkart.cashback.has_column.column.cashback.fee_waiver_amount
  edge_type: HAS_COLUMN
  source: table.flipkart.cashback
  target: column.cashback.fee_waiver_amount
  fields:
    edge_family: data_understanding
    evidence_basis: column.fields.table_id
    confidence: high
    canonical_cognee_edge: true
    marketplace_only: true
    canonical_edge_type: HAS_COLUMN
    inverse_edge_type: BELONGS_TO_TABLE
    materialize_inverse: true
    edge_class: canonical
    source_type: table
    target_type: column
```

```yaml
candidate_edge:
  edge_id: edge.column.cashback.fee_waiver_amount.belongs_to_table.table.flipkart.cashback
  edge_type: BELONGS_TO_TABLE
  source: column.cashback.fee_waiver_amount
  target: table.flipkart.cashback
  fields:
    edge_family: data_understanding
    evidence_basis: column.fields.table_id
    confidence: high
    canonical_cognee_edge: true
    marketplace_only: true
    canonical_edge_type: BELONGS_TO_TABLE
    legacy_edge_aliases:
    - column_belongs_to_table
    inverse_edge_type: HAS_COLUMN
    materialize_inverse: true
    edge_class: canonical
    source_type: column
    target_type: table
```



```yaml
candidate_edge:
  edge_id: edge.table.flipkart.cashback.has_column.column.cashback.invoice_date
  edge_type: HAS_COLUMN
  source: table.flipkart.cashback
  target: column.cashback.invoice_date
  fields:
    edge_family: data_understanding
    evidence_basis: column.fields.table_id
    confidence: high
    canonical_cognee_edge: true
    marketplace_only: true
    canonical_edge_type: HAS_COLUMN
    inverse_edge_type: BELONGS_TO_TABLE
    materialize_inverse: true
    edge_class: canonical
    source_type: table
    target_type: column
```

```yaml
candidate_edge:
  edge_id: edge.column.cashback.invoice_date.belongs_to_table.table.flipkart.cashback
  edge_type: BELONGS_TO_TABLE
  source: column.cashback.invoice_date
  target: table.flipkart.cashback
  fields:
    edge_family: data_understanding
    evidence_basis: column.fields.table_id
    confidence: high
    canonical_cognee_edge: true
    marketplace_only: true
    canonical_edge_type: BELONGS_TO_TABLE
    legacy_edge_aliases:
    - column_belongs_to_table
    inverse_edge_type: HAS_COLUMN
    materialize_inverse: true
    edge_class: canonical
    source_type: column
    target_type: table
```



```yaml
candidate_edge:
  edge_id: edge.table.flipkart.cashback.has_column.column.cashback.created_date
  edge_type: HAS_COLUMN
  source: table.flipkart.cashback
  target: column.cashback.created_date
  fields:
    edge_family: data_understanding
    evidence_basis: column.fields.table_id
    confidence: high
    canonical_cognee_edge: true
    marketplace_only: true
    canonical_edge_type: HAS_COLUMN
    inverse_edge_type: BELONGS_TO_TABLE
    materialize_inverse: true
    edge_class: canonical
    source_type: table
    target_type: column
```

```yaml
candidate_edge:
  edge_id: edge.column.cashback.created_date.belongs_to_table.table.flipkart.cashback
  edge_type: BELONGS_TO_TABLE
  source: column.cashback.created_date
  target: table.flipkart.cashback
  fields:
    edge_family: data_understanding
    evidence_basis: column.fields.table_id
    confidence: high
    canonical_cognee_edge: true
    marketplace_only: true
    canonical_edge_type: BELONGS_TO_TABLE
    legacy_edge_aliases:
    - column_belongs_to_table
    inverse_edge_type: HAS_COLUMN
    materialize_inverse: true
    edge_class: canonical
    source_type: column
    target_type: table
```

```yaml
candidate_edge:
  edge_id: edge.table.flipkart.cashback.has_column.column.cashback.is_shopsy_order
  edge_type: HAS_COLUMN
  source: table.flipkart.cashback
  target: column.cashback.is_shopsy_order_
  fields:
    edge_family: data_understanding
    evidence_basis: column.fields.table_id
    confidence: high
    canonical_cognee_edge: true
    marketplace_only: true
    canonical_edge_type: HAS_COLUMN
    inverse_edge_type: BELONGS_TO_TABLE
    materialize_inverse: true
    edge_class: canonical
    source_type: table
    target_type: column
```

```yaml
candidate_edge:
  edge_id: edge.column.cashback.is_shopsy_order.belongs_to_table.table.flipkart.cashback
  edge_type: BELONGS_TO_TABLE
  source: column.cashback.is_shopsy_order_
  target: table.flipkart.cashback
  fields:
    edge_family: data_understanding
    evidence_basis: column.fields.table_id
    confidence: high
    canonical_cognee_edge: true
    marketplace_only: true
    canonical_edge_type: BELONGS_TO_TABLE
    legacy_edge_aliases:
    - column_belongs_to_table
    inverse_edge_type: HAS_COLUMN
    materialize_inverse: true
    edge_class: canonical
    source_type: column
    target_type: table
```



```yaml
candidate_edge:
  edge_id: edge.table.flipkart.cashback.has_column.column.cashback.seller_gstin
  edge_type: HAS_COLUMN
  source: table.flipkart.cashback
  target: column.cashback.seller_gstin
  fields:
    edge_family: data_understanding
    evidence_basis: column.fields.table_id
    confidence: high
    canonical_cognee_edge: true
    marketplace_only: true
    canonical_edge_type: HAS_COLUMN
    inverse_edge_type: BELONGS_TO_TABLE
    materialize_inverse: true
    edge_class: canonical
    source_type: table
    target_type: column
```

```yaml
candidate_edge:
  edge_id: edge.column.cashback.seller_gstin.belongs_to_table.table.flipkart.cashback
  edge_type: BELONGS_TO_TABLE
  source: column.cashback.seller_gstin
  target: table.flipkart.cashback
  fields:
    edge_family: data_understanding
    evidence_basis: column.fields.table_id
    confidence: high
    canonical_cognee_edge: true
    marketplace_only: true
    canonical_edge_type: BELONGS_TO_TABLE
    legacy_edge_aliases:
    - column_belongs_to_table
    inverse_edge_type: HAS_COLUMN
    materialize_inverse: true
    edge_class: canonical
    source_type: column
    target_type: table
```

```yaml
candidate_edge:
  edge_id: edge.table.flipkart.cashback.has_column.column.cashback.is_active
  edge_type: HAS_COLUMN
  source: table.flipkart.cashback
  target: column.cashback.is_active
  fields:
    edge_family: data_understanding
    evidence_basis: column.fields.table_id
    confidence: high
    canonical_cognee_edge: true
    marketplace_only: true
    canonical_edge_type: HAS_COLUMN
    inverse_edge_type: BELONGS_TO_TABLE
    materialize_inverse: true
    edge_class: canonical
    source_type: table
    target_type: column
```

```yaml
candidate_edge:
  edge_id: edge.column.cashback.is_active.belongs_to_table.table.flipkart.cashback
  edge_type: BELONGS_TO_TABLE
  source: column.cashback.is_active
  target: table.flipkart.cashback
  fields:
    edge_family: data_understanding
    evidence_basis: column.fields.table_id
    confidence: high
    canonical_cognee_edge: true
    marketplace_only: true
    canonical_edge_type: BELONGS_TO_TABLE
    legacy_edge_aliases:
    - column_belongs_to_table
    inverse_edge_type: HAS_COLUMN
    materialize_inverse: true
    edge_class: canonical
    source_type: column
    target_type: table
```

```yaml
candidate_edge:
  edge_id: edge.table.flipkart.cashback.has_column.column.cashback.group_level_id
  edge_type: HAS_COLUMN
  source: table.flipkart.cashback
  target: column.cashback.group_level_id
  fields:
    edge_family: data_understanding
    evidence_basis: column.fields.table_id
    confidence: high
    canonical_cognee_edge: true
    marketplace_only: true
    canonical_edge_type: HAS_COLUMN
    inverse_edge_type: BELONGS_TO_TABLE
    materialize_inverse: true
    edge_class: canonical
    source_type: table
    target_type: column
```

```yaml
candidate_edge:
  edge_id: edge.column.cashback.group_level_id.belongs_to_table.table.flipkart.cashback
  edge_type: BELONGS_TO_TABLE
  source: column.cashback.group_level_id
  target: table.flipkart.cashback
  fields:
    edge_family: data_understanding
    evidence_basis: column.fields.table_id
    confidence: high
    canonical_cognee_edge: true
    marketplace_only: true
    canonical_edge_type: BELONGS_TO_TABLE
    legacy_edge_aliases:
    - column_belongs_to_table
    inverse_edge_type: HAS_COLUMN
    materialize_inverse: true
    edge_class: canonical
    source_type: column
    target_type: table
```

```yaml
candidate_edge:
  edge_id: edge.table.flipkart.cashback.has_column.column.cashback.group_id
  edge_type: HAS_COLUMN
  source: table.flipkart.cashback
  target: column.cashback.group_id
  fields:
    edge_family: data_understanding
    evidence_basis: column.fields.table_id
    confidence: high
    canonical_cognee_edge: true
    marketplace_only: true
    canonical_edge_type: HAS_COLUMN
    inverse_edge_type: BELONGS_TO_TABLE
    materialize_inverse: true
    edge_class: canonical
    source_type: table
    target_type: column
```

```yaml
candidate_edge:
  edge_id: edge.column.cashback.group_id.belongs_to_table.table.flipkart.cashback
  edge_type: BELONGS_TO_TABLE
  source: column.cashback.group_id
  target: table.flipkart.cashback
  fields:
    edge_family: data_understanding
    evidence_basis: column.fields.table_id
    confidence: high
    canonical_cognee_edge: true
    marketplace_only: true
    canonical_edge_type: BELONGS_TO_TABLE
    legacy_edge_aliases:
    - column_belongs_to_table
    inverse_edge_type: HAS_COLUMN
    materialize_inverse: true
    edge_class: canonical
    source_type: column
    target_type: table
```

```yaml
candidate_edge:
  edge_id: edge.table.flipkart.commission.has_value_profile.value_profile.flipkart.commission.description
  edge_type: HAS_VALUE_PROFILE
  source: table.flipkart.commission
  target: value_profile.flipkart.commission.description
  fields:
    edge_family: data_understanding
    evidence_basis: value_profile.fields.table_id
    confidence: high
    canonical_cognee_edge: true
    marketplace_only: true
    canonical_edge_type: HAS_VALUE_PROFILE
    inverse_edge_type: PROFILES_TABLE
    materialize_inverse: true
    edge_class: canonical
    source_type: table
    target_type: value_profile
```

```yaml
candidate_edge:
  edge_id: edge.column.commission.description.has_value_profile.value_profile.flipkart.commission.description
  edge_type: HAS_VALUE_PROFILE
  source: column.commission.description
  target: value_profile.flipkart.commission.description
  fields:
    edge_family: data_understanding
    evidence_basis: value_profile.fields.column_name + table_id
    confidence: high
    canonical_cognee_edge: true
    marketplace_only: true
    canonical_edge_type: HAS_VALUE_PROFILE
    inverse_edge_type: PROFILES_COLUMN
    materialize_inverse: true
    edge_class: canonical
    source_type: column
    target_type: value_profile
```

```yaml
candidate_edge:
  edge_id: edge.value_profile.flipkart.commission.description.profiles_column.column.commission.description
  edge_type: PROFILES_COLUMN
  source: value_profile.flipkart.commission.description
  target: column.commission.description
  fields:
    edge_family: data_understanding
    evidence_basis: value_profile.fields.column_name + table_id
    confidence: high
    canonical_cognee_edge: true
    marketplace_only: true
    canonical_edge_type: PROFILES_COLUMN
    legacy_edge_aliases:
    - value_profile_describes_column
    inverse_edge_type: HAS_VALUE_PROFILE
    materialize_inverse: true
    edge_class: canonical
    source_type: value_profile
    target_type: column
```

```yaml
candidate_edge:
  edge_id: edge.table.flipkart.cashback.has_value_profile.value_profile.flipkart.cashback.transaction_type
  edge_type: HAS_VALUE_PROFILE
  source: table.flipkart.cashback
  target: value_profile.flipkart.cashback.transaction_type
  fields:
    edge_family: data_understanding
    evidence_basis: value_profile.fields.table_id
    confidence: high
    canonical_cognee_edge: true
    marketplace_only: true
    canonical_edge_type: HAS_VALUE_PROFILE
    inverse_edge_type: PROFILES_TABLE
    materialize_inverse: true
    edge_class: canonical
    source_type: table
    target_type: value_profile
```

```yaml
candidate_edge:
  edge_id: edge.column.cashback.transaction_type.has_value_profile.value_profile.flipkart.cashback.transaction_type
  edge_type: HAS_VALUE_PROFILE
  source: column.cashback.transaction_type
  target: value_profile.flipkart.cashback.transaction_type
  fields:
    edge_family: data_understanding
    evidence_basis: value_profile.fields.column_name + table_id
    confidence: high
    canonical_cognee_edge: true
    marketplace_only: true
    canonical_edge_type: HAS_VALUE_PROFILE
    inverse_edge_type: PROFILES_COLUMN
    materialize_inverse: true
    edge_class: canonical
    source_type: column
    target_type: value_profile
```

```yaml
candidate_edge:
  edge_id: edge.value_profile.flipkart.cashback.transaction_type.profiles_column.column.cashback.transaction_type
  edge_type: PROFILES_COLUMN
  source: value_profile.flipkart.cashback.transaction_type
  target: column.cashback.transaction_type
  fields:
    edge_family: data_understanding
    evidence_basis: value_profile.fields.column_name + table_id
    confidence: high
    canonical_cognee_edge: true
    marketplace_only: true
    canonical_edge_type: PROFILES_COLUMN
    legacy_edge_aliases:
    - value_profile_describes_column
    inverse_edge_type: HAS_VALUE_PROFILE
    materialize_inverse: true
    edge_class: canonical
    source_type: value_profile
    target_type: column
```

```yaml
candidate_edge:
  edge_id: edge.table.flipkart.cashback.has_value_profile.value_profile.flipkart.cashback.document_type
  edge_type: HAS_VALUE_PROFILE
  source: table.flipkart.cashback
  target: value_profile.flipkart.cashback.document_type
  fields:
    edge_family: data_understanding
    evidence_basis: value_profile.fields.table_id
    confidence: high
    canonical_cognee_edge: true
    marketplace_only: true
    canonical_edge_type: HAS_VALUE_PROFILE
    inverse_edge_type: PROFILES_TABLE
    materialize_inverse: true
    edge_class: canonical
    source_type: table
    target_type: value_profile
```

```yaml
candidate_edge:
  edge_id: edge.column.cashback.document_type.has_value_profile.value_profile.flipkart.cashback.document_type
  edge_type: HAS_VALUE_PROFILE
  source: column.cashback.document_type
  target: value_profile.flipkart.cashback.document_type
  fields:
    edge_family: data_understanding
    evidence_basis: value_profile.fields.column_name + table_id
    confidence: high
    canonical_cognee_edge: true
    marketplace_only: true
    canonical_edge_type: HAS_VALUE_PROFILE
    inverse_edge_type: PROFILES_COLUMN
    materialize_inverse: true
    edge_class: canonical
    source_type: column
    target_type: value_profile
```

```yaml
candidate_edge:
  edge_id: edge.value_profile.flipkart.cashback.document_type.profiles_column.column.cashback.document_type
  edge_type: PROFILES_COLUMN
  source: value_profile.flipkart.cashback.document_type
  target: column.cashback.document_type
  fields:
    edge_family: data_understanding
    evidence_basis: value_profile.fields.column_name + table_id
    confidence: high
    canonical_cognee_edge: true
    marketplace_only: true
    canonical_edge_type: PROFILES_COLUMN
    legacy_edge_aliases:
    - value_profile_describes_column
    inverse_edge_type: HAS_VALUE_PROFILE
    materialize_inverse: true
    edge_class: canonical
    source_type: value_profile
    target_type: column
```

```yaml
candidate_edge:
  edge_id: edge.table.flipkart.cashback.has_value_profile.value_profile.flipkart.cashback.document_sub_type
  edge_type: HAS_VALUE_PROFILE
  source: table.flipkart.cashback
  target: value_profile.flipkart.cashback.document_sub_type
  fields:
    edge_family: data_understanding
    evidence_basis: value_profile.fields.table_id
    confidence: high
    canonical_cognee_edge: true
    marketplace_only: true
    canonical_edge_type: HAS_VALUE_PROFILE
    inverse_edge_type: PROFILES_TABLE
    materialize_inverse: true
    edge_class: canonical
    source_type: table
    target_type: value_profile
```

```yaml
candidate_edge:
  edge_id: edge.column.cashback.document_sub_type.has_value_profile.value_profile.flipkart.cashback.document_sub_type
  edge_type: HAS_VALUE_PROFILE
  source: column.cashback.document_sub_type
  target: value_profile.flipkart.cashback.document_sub_type
  fields:
    edge_family: data_understanding
    evidence_basis: value_profile.fields.column_name + table_id
    confidence: high
    canonical_cognee_edge: true
    marketplace_only: true
    canonical_edge_type: HAS_VALUE_PROFILE
    inverse_edge_type: PROFILES_COLUMN
    materialize_inverse: true
    edge_class: canonical
    source_type: column
    target_type: value_profile
```

```yaml
candidate_edge:
  edge_id: edge.value_profile.flipkart.cashback.document_sub_type.profiles_column.column.cashback.document_sub_type
  edge_type: PROFILES_COLUMN
  source: value_profile.flipkart.cashback.document_sub_type
  target: column.cashback.document_sub_type
  fields:
    edge_family: data_understanding
    evidence_basis: value_profile.fields.column_name + table_id
    confidence: high
    canonical_cognee_edge: true
    marketplace_only: true
    canonical_edge_type: PROFILES_COLUMN
    legacy_edge_aliases:
    - value_profile_describes_column
    inverse_edge_type: HAS_VALUE_PROFILE
    materialize_inverse: true
    edge_class: canonical
    source_type: value_profile
    target_type: column
```

```yaml
candidate_edge:
  edge_id: edge.table.flipkart.cashback.has_value_profile.value_profile.flipkart.cashback.is_shopsy_order
  edge_type: HAS_VALUE_PROFILE
  source: table.flipkart.cashback
  target: value_profile.flipkart.cashback.is_shopsy_order
  fields:
    edge_family: data_understanding
    evidence_basis: value_profile.fields.table_id
    confidence: high
    canonical_cognee_edge: true
    marketplace_only: true
    canonical_edge_type: HAS_VALUE_PROFILE
    inverse_edge_type: PROFILES_TABLE
    materialize_inverse: true
    edge_class: canonical
    source_type: table
    target_type: value_profile
```

```yaml
candidate_edge:
  edge_id: edge.column.cashback.is_shopsy_order.has_value_profile.value_profile.flipkart.cashback.is_shopsy_order
  edge_type: HAS_VALUE_PROFILE
  source: column.cashback.is_shopsy_order_
  target: value_profile.flipkart.cashback.is_shopsy_order
  fields:
    edge_family: data_understanding
    evidence_basis: value_profile.fields.column_name + table_id
    confidence: high
    canonical_cognee_edge: true
    marketplace_only: true
    canonical_edge_type: HAS_VALUE_PROFILE
    inverse_edge_type: PROFILES_COLUMN
    materialize_inverse: true
    edge_class: canonical
    source_type: column
    target_type: value_profile
```

```yaml
candidate_edge:
  edge_id: edge.value_profile.flipkart.cashback.is_shopsy_order.profiles_column.column.cashback.is_shopsy_order
  edge_type: PROFILES_COLUMN
  source: value_profile.flipkart.cashback.is_shopsy_order
  target: column.cashback.is_shopsy_order_
  fields:
    edge_family: data_understanding
    evidence_basis: value_profile.fields.column_name + table_id
    confidence: high
    canonical_cognee_edge: true
    marketplace_only: true
    canonical_edge_type: PROFILES_COLUMN
    legacy_edge_aliases:
    - value_profile_describes_column
    inverse_edge_type: HAS_VALUE_PROFILE
    materialize_inverse: true
    edge_class: canonical
    source_type: value_profile
    target_type: column
```

```yaml
candidate_edge:
  edge_id: edge.table.flipkart.oms.has_value_profile.value_profile.flipkart.oms.fulfilment_type
  edge_type: HAS_VALUE_PROFILE
  source: table.flipkart.oms
  target: value_profile.flipkart.oms.fulfilment_type
  fields:
    edge_family: data_understanding
    evidence_basis: value_profile.fields.table_id
    confidence: high
    canonical_cognee_edge: true
    marketplace_only: true
    canonical_edge_type: HAS_VALUE_PROFILE
    inverse_edge_type: PROFILES_TABLE
    materialize_inverse: true
    edge_class: canonical
    source_type: table
    target_type: value_profile
```

```yaml
candidate_edge:
  edge_id: edge.column.oms.fulfilment_type.has_value_profile.value_profile.flipkart.oms.fulfilment_type
  edge_type: HAS_VALUE_PROFILE
  source: column.oms.fulfilment_type
  target: value_profile.flipkart.oms.fulfilment_type
  fields:
    edge_family: data_understanding
    evidence_basis: value_profile.fields.column_name + table_id
    confidence: high
    canonical_cognee_edge: true
    marketplace_only: true
    canonical_edge_type: HAS_VALUE_PROFILE
    inverse_edge_type: PROFILES_COLUMN
    materialize_inverse: true
    edge_class: canonical
    source_type: column
    target_type: value_profile
```

```yaml
candidate_edge:
  edge_id: edge.value_profile.flipkart.oms.fulfilment_type.profiles_column.column.oms.fulfilment_type
  edge_type: PROFILES_COLUMN
  source: value_profile.flipkart.oms.fulfilment_type
  target: column.oms.fulfilment_type
  fields:
    edge_family: data_understanding
    evidence_basis: value_profile.fields.column_name + table_id
    confidence: high
    canonical_cognee_edge: true
    marketplace_only: true
    canonical_edge_type: PROFILES_COLUMN
    legacy_edge_aliases:
    - value_profile_describes_column
    inverse_edge_type: HAS_VALUE_PROFILE
    materialize_inverse: true
    edge_class: canonical
    source_type: value_profile
    target_type: column
```

```yaml
candidate_edge:
  edge_id: edge.table.flipkart.settlement.has_value_profile.value_profile.flipkart.settlement.fulfilment_type
  edge_type: HAS_VALUE_PROFILE
  source: table.flipkart.settlement
  target: value_profile.flipkart.settlement.fulfilment_type
  fields:
    edge_family: data_understanding
    evidence_basis: value_profile.fields.table_id
    confidence: high
    canonical_cognee_edge: true
    marketplace_only: true
    canonical_edge_type: HAS_VALUE_PROFILE
    inverse_edge_type: PROFILES_TABLE
    materialize_inverse: true
    edge_class: canonical
    source_type: table
    target_type: value_profile
```

```yaml
candidate_edge:
  edge_id: edge.column.settlement.fulfilment_type.has_value_profile.value_profile.flipkart.settlement.fulfilment_type
  edge_type: HAS_VALUE_PROFILE
  source: column.settlement.fulfilment_type
  target: value_profile.flipkart.settlement.fulfilment_type
  fields:
    edge_family: data_understanding
    evidence_basis: value_profile.fields.column_name + table_id
    confidence: high
    canonical_cognee_edge: true
    marketplace_only: true
    canonical_edge_type: HAS_VALUE_PROFILE
    inverse_edge_type: PROFILES_COLUMN
    materialize_inverse: true
    edge_class: canonical
    source_type: column
    target_type: value_profile
```

```yaml
candidate_edge:
  edge_id: edge.value_profile.flipkart.settlement.fulfilment_type.profiles_column.column.settlement.fulfilment_type
  edge_type: PROFILES_COLUMN
  source: value_profile.flipkart.settlement.fulfilment_type
  target: column.settlement.fulfilment_type
  fields:
    edge_family: data_understanding
    evidence_basis: value_profile.fields.column_name + table_id
    confidence: high
    canonical_cognee_edge: true
    marketplace_only: true
    canonical_edge_type: PROFILES_COLUMN
    legacy_edge_aliases:
    - value_profile_describes_column
    inverse_edge_type: HAS_VALUE_PROFILE
    materialize_inverse: true
    edge_class: canonical
    source_type: value_profile
    target_type: column
```

```yaml
candidate_edge:
  edge_id: edge.table.flipkart.settlement.has_value_profile.value_profile.flipkart.settlement.neft_type
  edge_type: HAS_VALUE_PROFILE
  source: table.flipkart.settlement
  target: value_profile.flipkart.settlement.neft_type
  fields:
    edge_family: data_understanding
    evidence_basis: value_profile.fields.table_id
    confidence: high
    canonical_cognee_edge: true
    marketplace_only: true
    canonical_edge_type: HAS_VALUE_PROFILE
    inverse_edge_type: PROFILES_TABLE
    materialize_inverse: true
    edge_class: canonical
    source_type: table
    target_type: value_profile
```

```yaml
candidate_edge:
  edge_id: edge.column.settlement.neft_type.has_value_profile.value_profile.flipkart.settlement.neft_type
  edge_type: HAS_VALUE_PROFILE
  source: column.settlement.neft_type
  target: value_profile.flipkart.settlement.neft_type
  fields:
    edge_family: data_understanding
    evidence_basis: value_profile.fields.column_name + table_id
    confidence: high
    canonical_cognee_edge: true
    marketplace_only: true
    canonical_edge_type: HAS_VALUE_PROFILE
    inverse_edge_type: PROFILES_COLUMN
    materialize_inverse: true
    edge_class: canonical
    source_type: column
    target_type: value_profile
```

```yaml
candidate_edge:
  edge_id: edge.value_profile.flipkart.settlement.neft_type.profiles_column.column.settlement.neft_type
  edge_type: PROFILES_COLUMN
  source: value_profile.flipkart.settlement.neft_type
  target: column.settlement.neft_type
  fields:
    edge_family: data_understanding
    evidence_basis: value_profile.fields.column_name + table_id
    confidence: high
    canonical_cognee_edge: true
    marketplace_only: true
    canonical_edge_type: PROFILES_COLUMN
    legacy_edge_aliases:
    - value_profile_describes_column
    inverse_edge_type: HAS_VALUE_PROFILE
    materialize_inverse: true
    edge_class: canonical
    source_type: value_profile
    target_type: column
```

```yaml
candidate_edge:
  edge_id: edge.table.flipkart.settlement.has_value_profile.value_profile.flipkart.settlement.return_type
  edge_type: HAS_VALUE_PROFILE
  source: table.flipkart.settlement
  target: value_profile.flipkart.settlement.return_type
  fields:
    edge_family: data_understanding
    evidence_basis: value_profile.fields.table_id
    confidence: high
    canonical_cognee_edge: true
    marketplace_only: true
    canonical_edge_type: HAS_VALUE_PROFILE
    inverse_edge_type: PROFILES_TABLE
    materialize_inverse: true
    edge_class: canonical
    source_type: table
    target_type: value_profile
```

```yaml
candidate_edge:
  edge_id: edge.column.settlement.return_type.has_value_profile.value_profile.flipkart.settlement.return_type
  edge_type: HAS_VALUE_PROFILE
  source: column.settlement.return_type
  target: value_profile.flipkart.settlement.return_type
  fields:
    edge_family: data_understanding
    evidence_basis: value_profile.fields.column_name + table_id
    confidence: high
    canonical_cognee_edge: true
    marketplace_only: true
    canonical_edge_type: HAS_VALUE_PROFILE
    inverse_edge_type: PROFILES_COLUMN
    materialize_inverse: true
    edge_class: canonical
    source_type: column
    target_type: value_profile
```

```yaml
candidate_edge:
  edge_id: edge.value_profile.flipkart.settlement.return_type.profiles_column.column.settlement.return_type
  edge_type: PROFILES_COLUMN
  source: value_profile.flipkart.settlement.return_type
  target: column.settlement.return_type
  fields:
    edge_family: data_understanding
    evidence_basis: value_profile.fields.column_name + table_id
    confidence: high
    canonical_cognee_edge: true
    marketplace_only: true
    canonical_edge_type: PROFILES_COLUMN
    legacy_edge_aliases:
    - value_profile_describes_column
    inverse_edge_type: HAS_VALUE_PROFILE
    materialize_inverse: true
    edge_class: canonical
    source_type: value_profile
    target_type: column
```

```yaml
candidate_edge:
  edge_id: edge.table.flipkart.settlement.has_value_profile.value_profile.flipkart.settlement.is_active
  edge_type: HAS_VALUE_PROFILE
  source: table.flipkart.settlement
  target: value_profile.flipkart.settlement.is_active
  fields:
    edge_family: data_understanding
    evidence_basis: value_profile.fields.table_id
    confidence: high
    canonical_cognee_edge: true
    marketplace_only: true
    canonical_edge_type: HAS_VALUE_PROFILE
    inverse_edge_type: PROFILES_TABLE
    materialize_inverse: true
    edge_class: canonical
    source_type: table
    target_type: value_profile
```

```yaml
candidate_edge:
  edge_id: edge.column.settlement.is_active.has_value_profile.value_profile.flipkart.settlement.is_active
  edge_type: HAS_VALUE_PROFILE
  source: column.settlement.is_active
  target: value_profile.flipkart.settlement.is_active
  fields:
    edge_family: data_understanding
    evidence_basis: value_profile.fields.column_name + table_id
    confidence: high
    canonical_cognee_edge: true
    marketplace_only: true
    canonical_edge_type: HAS_VALUE_PROFILE
    inverse_edge_type: PROFILES_COLUMN
    materialize_inverse: true
    edge_class: canonical
    source_type: column
    target_type: value_profile
```

```yaml
candidate_edge:
  edge_id: edge.value_profile.flipkart.settlement.is_active.profiles_column.column.settlement.is_active
  edge_type: PROFILES_COLUMN
  source: value_profile.flipkart.settlement.is_active
  target: column.settlement.is_active
  fields:
    edge_family: data_understanding
    evidence_basis: value_profile.fields.column_name + table_id
    confidence: high
    canonical_cognee_edge: true
    marketplace_only: true
    canonical_edge_type: PROFILES_COLUMN
    legacy_edge_aliases:
    - value_profile_describes_column
    inverse_edge_type: HAS_VALUE_PROFILE
    materialize_inverse: true
    edge_class: canonical
    source_type: value_profile
    target_type: column
```

```yaml
candidate_edge:
  edge_id: edge.table.flipkart.oms.has_relationship.relationship.flipkart.oms_settlement
  edge_type: HAS_RELATIONSHIP
  source: table.flipkart.oms
  target: relationship.flipkart.oms_settlement
  fields:
    edge_family: data_understanding
    evidence_basis: relationship.fields.left_table
    confidence: high
    canonical_cognee_edge: true
    marketplace_only: true
    canonical_edge_type: HAS_RELATIONSHIP
    inverse_edge_type: RELATIONSHIP_OF_TABLE
    materialize_inverse: false
    edge_class: canonical
    source_type: table
    target_type: relationship
```

```yaml
candidate_edge:
  edge_id: edge.table.flipkart.settlement.has_relationship.relationship.flipkart.oms_settlement
  edge_type: HAS_RELATIONSHIP
  source: table.flipkart.settlement
  target: relationship.flipkart.oms_settlement
  fields:
    edge_family: data_understanding
    evidence_basis: relationship.fields.right_table
    confidence: high
    canonical_cognee_edge: true
    marketplace_only: true
    canonical_edge_type: HAS_RELATIONSHIP
    inverse_edge_type: RELATIONSHIP_OF_TABLE
    materialize_inverse: false
    edge_class: canonical
    source_type: table
    target_type: relationship
```

```yaml
candidate_edge:
  edge_id: edge.relationship.flipkart.oms_settlement.source_table.table.flipkart.oms
  edge_type: SOURCE_TABLE
  source: relationship.flipkart.oms_settlement
  target: table.flipkart.oms
  fields:
    edge_family: data_understanding
    evidence_basis: relationship.fields.left_table
    confidence: high
    canonical_cognee_edge: true
    marketplace_only: true
    canonical_edge_type: SOURCE_TABLE
    inverse_edge_type: SOURCE_OF_RELATIONSHIP
    materialize_inverse: false
    edge_class: canonical
    source_type: relationship
    target_type: table
```

```yaml
candidate_edge:
  edge_id: edge.relationship.flipkart.oms_settlement.target_table.table.flipkart.settlement
  edge_type: TARGET_TABLE
  source: relationship.flipkart.oms_settlement
  target: table.flipkart.settlement
  fields:
    edge_family: data_understanding
    evidence_basis: relationship.fields.right_table
    confidence: high
    canonical_cognee_edge: true
    marketplace_only: true
    canonical_edge_type: TARGET_TABLE
    inverse_edge_type: TARGET_OF_RELATIONSHIP
    materialize_inverse: false
    edge_class: canonical
    source_type: relationship
    target_type: table
```

```yaml
candidate_edge:
  edge_id: edge.relationship.flipkart.oms_settlement.uses_source_column.column.oms.order_id
  edge_type: USES_SOURCE_COLUMN
  source: relationship.flipkart.oms_settlement
  target: column.oms.order_id
  fields:
    edge_family: data_understanding
    evidence_basis: relationship.fields.join_keys
    confidence: high
    canonical_cognee_edge: true
    marketplace_only: true
    join_key_text: order_id + item_id
    canonical_edge_type: USES_SOURCE_COLUMN
    inverse_edge_type: SOURCE_COLUMN_OF_RELATIONSHIP
    materialize_inverse: false
    edge_class: canonical
    source_type: relationship
    target_type: column
```

```yaml
candidate_edge:
  edge_id: edge.relationship.flipkart.oms_settlement.uses_source_column.column.oms.item_id
  edge_type: USES_SOURCE_COLUMN
  source: relationship.flipkart.oms_settlement
  target: column.oms.item_id
  fields:
    edge_family: data_understanding
    evidence_basis: relationship.fields.join_keys
    confidence: high
    canonical_cognee_edge: true
    marketplace_only: true
    join_key_text: order_id + item_id
    canonical_edge_type: USES_SOURCE_COLUMN
    inverse_edge_type: SOURCE_COLUMN_OF_RELATIONSHIP
    materialize_inverse: false
    edge_class: canonical
    source_type: relationship
    target_type: column
```

```yaml
candidate_edge:
  edge_id: edge.relationship.flipkart.oms_settlement.uses_target_column.column.settlement.order_id
  edge_type: USES_TARGET_COLUMN
  source: relationship.flipkart.oms_settlement
  target: column.settlement.order_id
  fields:
    edge_family: data_understanding
    evidence_basis: relationship.fields.join_keys
    confidence: high
    canonical_cognee_edge: true
    marketplace_only: true
    join_key_text: order_id + item_id
    canonical_edge_type: USES_TARGET_COLUMN
    inverse_edge_type: TARGET_COLUMN_OF_RELATIONSHIP
    materialize_inverse: false
    edge_class: canonical
    source_type: relationship
    target_type: column
```

```yaml
candidate_edge:
  edge_id: edge.relationship.flipkart.oms_settlement.uses_target_column.column.settlement.item_id
  edge_type: USES_TARGET_COLUMN
  source: relationship.flipkart.oms_settlement
  target: column.settlement.item_id
  fields:
    edge_family: data_understanding
    evidence_basis: relationship.fields.join_keys
    confidence: high
    canonical_cognee_edge: true
    marketplace_only: true
    join_key_text: order_id + item_id
    canonical_edge_type: USES_TARGET_COLUMN
    inverse_edge_type: TARGET_COLUMN_OF_RELATIONSHIP
    materialize_inverse: false
    edge_class: canonical
    source_type: relationship
    target_type: column
```

```yaml
candidate_edge:
  edge_id: edge.table.flipkart.commission.has_relationship.relationship.flipkart.commission_settlement
  edge_type: HAS_RELATIONSHIP
  source: table.flipkart.commission
  target: relationship.flipkart.commission_settlement
  fields:
    edge_family: data_understanding
    evidence_basis: relationship.fields.left_table
    confidence: high
    canonical_cognee_edge: true
    marketplace_only: true
    canonical_edge_type: HAS_RELATIONSHIP
    inverse_edge_type: RELATIONSHIP_OF_TABLE
    materialize_inverse: false
    edge_class: canonical
    source_type: table
    target_type: relationship
```

```yaml
candidate_edge:
  edge_id: edge.table.flipkart.settlement.has_relationship.relationship.flipkart.commission_settlement
  edge_type: HAS_RELATIONSHIP
  source: table.flipkart.settlement
  target: relationship.flipkart.commission_settlement
  fields:
    edge_family: data_understanding
    evidence_basis: relationship.fields.right_table
    confidence: high
    canonical_cognee_edge: true
    marketplace_only: true
    canonical_edge_type: HAS_RELATIONSHIP
    inverse_edge_type: RELATIONSHIP_OF_TABLE
    materialize_inverse: false
    edge_class: canonical
    source_type: table
    target_type: relationship
```

```yaml
candidate_edge:
  edge_id: edge.relationship.flipkart.commission_settlement.source_table.table.flipkart.commission
  edge_type: SOURCE_TABLE
  source: relationship.flipkart.commission_settlement
  target: table.flipkart.commission
  fields:
    edge_family: data_understanding
    evidence_basis: relationship.fields.left_table
    confidence: high
    canonical_cognee_edge: true
    marketplace_only: true
    canonical_edge_type: SOURCE_TABLE
    inverse_edge_type: SOURCE_OF_RELATIONSHIP
    materialize_inverse: false
    edge_class: canonical
    source_type: relationship
    target_type: table
```

```yaml
candidate_edge:
  edge_id: edge.relationship.flipkart.commission_settlement.target_table.table.flipkart.settlement
  edge_type: TARGET_TABLE
  source: relationship.flipkart.commission_settlement
  target: table.flipkart.settlement
  fields:
    edge_family: data_understanding
    evidence_basis: relationship.fields.right_table
    confidence: high
    canonical_cognee_edge: true
    marketplace_only: true
    canonical_edge_type: TARGET_TABLE
    inverse_edge_type: TARGET_OF_RELATIONSHIP
    materialize_inverse: false
    edge_class: canonical
    source_type: relationship
    target_type: table
```

```yaml
candidate_edge:
  edge_id: edge.relationship.flipkart.commission_settlement.uses_source_column.column.commission.order_id
  edge_type: USES_SOURCE_COLUMN
  source: relationship.flipkart.commission_settlement
  target: column.commission.order_id
  fields:
    edge_family: data_understanding
    evidence_basis: relationship.fields.join_keys
    confidence: high
    canonical_cognee_edge: true
    marketplace_only: true
    join_key_text: commission.order_id = REPLACE(settlement.order_id, 'OD', '') AND item_id
    canonical_edge_type: USES_SOURCE_COLUMN
    inverse_edge_type: SOURCE_COLUMN_OF_RELATIONSHIP
    materialize_inverse: false
    edge_class: canonical
    source_type: relationship
    target_type: column
```

```yaml
candidate_edge:
  edge_id: edge.relationship.flipkart.commission_settlement.uses_source_column.column.commission.item_id
  edge_type: USES_SOURCE_COLUMN
  source: relationship.flipkart.commission_settlement
  target: column.commission.item_id
  fields:
    edge_family: data_understanding
    evidence_basis: relationship.fields.join_keys
    confidence: high
    canonical_cognee_edge: true
    marketplace_only: true
    join_key_text: commission.order_id = REPLACE(settlement.order_id, 'OD', '') AND item_id
    canonical_edge_type: USES_SOURCE_COLUMN
    inverse_edge_type: SOURCE_COLUMN_OF_RELATIONSHIP
    materialize_inverse: false
    edge_class: canonical
    source_type: relationship
    target_type: column
```

```yaml
candidate_edge:
  edge_id: edge.relationship.flipkart.commission_settlement.uses_target_column.column.settlement.order_id
  edge_type: USES_TARGET_COLUMN
  source: relationship.flipkart.commission_settlement
  target: column.settlement.order_id
  fields:
    edge_family: data_understanding
    evidence_basis: relationship.fields.join_keys
    confidence: high
    canonical_cognee_edge: true
    marketplace_only: true
    join_key_text: commission.order_id = REPLACE(settlement.order_id, 'OD', '') AND item_id
    canonical_edge_type: USES_TARGET_COLUMN
    inverse_edge_type: TARGET_COLUMN_OF_RELATIONSHIP
    materialize_inverse: false
    edge_class: canonical
    source_type: relationship
    target_type: column
```

```yaml
candidate_edge:
  edge_id: edge.relationship.flipkart.commission_settlement.uses_target_column.column.settlement.item_id
  edge_type: USES_TARGET_COLUMN
  source: relationship.flipkart.commission_settlement
  target: column.settlement.item_id
  fields:
    edge_family: data_understanding
    evidence_basis: relationship.fields.join_keys
    confidence: high
    canonical_cognee_edge: true
    marketplace_only: true
    join_key_text: commission.order_id = REPLACE(settlement.order_id, 'OD', '') AND item_id
    canonical_edge_type: USES_TARGET_COLUMN
    inverse_edge_type: TARGET_COLUMN_OF_RELATIONSHIP
    materialize_inverse: false
    edge_class: canonical
    source_type: relationship
    target_type: column
```

```yaml
candidate_edge:
  edge_id: edge.table.flipkart.commission.has_relationship.relationship.flipkart.commission_oms
  edge_type: HAS_RELATIONSHIP
  source: table.flipkart.commission
  target: relationship.flipkart.commission_oms
  fields:
    edge_family: data_understanding
    evidence_basis: relationship.fields.left_table
    confidence: high
    canonical_cognee_edge: true
    marketplace_only: true
    canonical_edge_type: HAS_RELATIONSHIP
    inverse_edge_type: RELATIONSHIP_OF_TABLE
    materialize_inverse: false
    edge_class: canonical
    source_type: table
    target_type: relationship
```

```yaml
candidate_edge:
  edge_id: edge.table.flipkart.oms.has_relationship.relationship.flipkart.commission_oms
  edge_type: HAS_RELATIONSHIP
  source: table.flipkart.oms
  target: relationship.flipkart.commission_oms
  fields:
    edge_family: data_understanding
    evidence_basis: relationship.fields.right_table
    confidence: high
    canonical_cognee_edge: true
    marketplace_only: true
    canonical_edge_type: HAS_RELATIONSHIP
    inverse_edge_type: RELATIONSHIP_OF_TABLE
    materialize_inverse: false
    edge_class: canonical
    source_type: table
    target_type: relationship
```

```yaml
candidate_edge:
  edge_id: edge.relationship.flipkart.commission_oms.source_table.table.flipkart.commission
  edge_type: SOURCE_TABLE
  source: relationship.flipkart.commission_oms
  target: table.flipkart.commission
  fields:
    edge_family: data_understanding
    evidence_basis: relationship.fields.left_table
    confidence: high
    canonical_cognee_edge: true
    marketplace_only: true
    canonical_edge_type: SOURCE_TABLE
    inverse_edge_type: SOURCE_OF_RELATIONSHIP
    materialize_inverse: false
    edge_class: canonical
    source_type: relationship
    target_type: table
```

```yaml
candidate_edge:
  edge_id: edge.relationship.flipkart.commission_oms.target_table.table.flipkart.oms
  edge_type: TARGET_TABLE
  source: relationship.flipkart.commission_oms
  target: table.flipkart.oms
  fields:
    edge_family: data_understanding
    evidence_basis: relationship.fields.right_table
    confidence: high
    canonical_cognee_edge: true
    marketplace_only: true
    canonical_edge_type: TARGET_TABLE
    inverse_edge_type: TARGET_OF_RELATIONSHIP
    materialize_inverse: false
    edge_class: canonical
    source_type: relationship
    target_type: table
```

```yaml
candidate_edge:
  edge_id: edge.relationship.flipkart.commission_oms.uses_source_column.column.commission.order_id
  edge_type: USES_SOURCE_COLUMN
  source: relationship.flipkart.commission_oms
  target: column.commission.order_id
  fields:
    edge_family: data_understanding
    evidence_basis: relationship.fields.join_keys
    confidence: high
    canonical_cognee_edge: true
    marketplace_only: true
    join_key_text: commission.order_id = REPLACE(oms.order_id, 'OD', '') AND item_id
    canonical_edge_type: USES_SOURCE_COLUMN
    inverse_edge_type: SOURCE_COLUMN_OF_RELATIONSHIP
    materialize_inverse: false
    edge_class: canonical
    source_type: relationship
    target_type: column
```

```yaml
candidate_edge:
  edge_id: edge.relationship.flipkart.commission_oms.uses_source_column.column.commission.item_id
  edge_type: USES_SOURCE_COLUMN
  source: relationship.flipkart.commission_oms
  target: column.commission.item_id
  fields:
    edge_family: data_understanding
    evidence_basis: relationship.fields.join_keys
    confidence: high
    canonical_cognee_edge: true
    marketplace_only: true
    join_key_text: commission.order_id = REPLACE(oms.order_id, 'OD', '') AND item_id
    canonical_edge_type: USES_SOURCE_COLUMN
    inverse_edge_type: SOURCE_COLUMN_OF_RELATIONSHIP
    materialize_inverse: false
    edge_class: canonical
    source_type: relationship
    target_type: column
```

```yaml
candidate_edge:
  edge_id: edge.relationship.flipkart.commission_oms.uses_target_column.column.oms.order_id
  edge_type: USES_TARGET_COLUMN
  source: relationship.flipkart.commission_oms
  target: column.oms.order_id
  fields:
    edge_family: data_understanding
    evidence_basis: relationship.fields.join_keys
    confidence: high
    canonical_cognee_edge: true
    marketplace_only: true
    join_key_text: commission.order_id = REPLACE(oms.order_id, 'OD', '') AND item_id
    canonical_edge_type: USES_TARGET_COLUMN
    inverse_edge_type: TARGET_COLUMN_OF_RELATIONSHIP
    materialize_inverse: false
    edge_class: canonical
    source_type: relationship
    target_type: column
```

```yaml
candidate_edge:
  edge_id: edge.relationship.flipkart.commission_oms.uses_target_column.column.oms.item_id
  edge_type: USES_TARGET_COLUMN
  source: relationship.flipkart.commission_oms
  target: column.oms.item_id
  fields:
    edge_family: data_understanding
    evidence_basis: relationship.fields.join_keys
    confidence: high
    canonical_cognee_edge: true
    marketplace_only: true
    join_key_text: commission.order_id = REPLACE(oms.order_id, 'OD', '') AND item_id
    canonical_edge_type: USES_TARGET_COLUMN
    inverse_edge_type: TARGET_COLUMN_OF_RELATIONSHIP
    materialize_inverse: false
    edge_class: canonical
    source_type: relationship
    target_type: column
```

```yaml
candidate_edge:
  edge_id: edge.table.flipkart.cashback.has_relationship.relationship.flipkart.cashback_settlement
  edge_type: HAS_RELATIONSHIP
  source: table.flipkart.cashback
  target: relationship.flipkart.cashback_settlement
  fields:
    edge_family: data_understanding
    evidence_basis: relationship.fields.left_table
    confidence: high
    canonical_cognee_edge: true
    marketplace_only: true
    canonical_edge_type: HAS_RELATIONSHIP
    inverse_edge_type: RELATIONSHIP_OF_TABLE
    materialize_inverse: false
    edge_class: canonical
    source_type: table
    target_type: relationship
```

```yaml
candidate_edge:
  edge_id: edge.table.flipkart.settlement.has_relationship.relationship.flipkart.cashback_settlement
  edge_type: HAS_RELATIONSHIP
  source: table.flipkart.settlement
  target: relationship.flipkart.cashback_settlement
  fields:
    edge_family: data_understanding
    evidence_basis: relationship.fields.right_table
    confidence: high
    canonical_cognee_edge: true
    marketplace_only: true
    canonical_edge_type: HAS_RELATIONSHIP
    inverse_edge_type: RELATIONSHIP_OF_TABLE
    materialize_inverse: false
    edge_class: canonical
    source_type: table
    target_type: relationship
```

```yaml
candidate_edge:
  edge_id: edge.relationship.flipkart.cashback_settlement.source_table.table.flipkart.cashback
  edge_type: SOURCE_TABLE
  source: relationship.flipkart.cashback_settlement
  target: table.flipkart.cashback
  fields:
    edge_family: data_understanding
    evidence_basis: relationship.fields.left_table
    confidence: high
    canonical_cognee_edge: true
    marketplace_only: true
    canonical_edge_type: SOURCE_TABLE
    inverse_edge_type: SOURCE_OF_RELATIONSHIP
    materialize_inverse: false
    edge_class: canonical
    source_type: relationship
    target_type: table
```

```yaml
candidate_edge:
  edge_id: edge.relationship.flipkart.cashback_settlement.target_table.table.flipkart.settlement
  edge_type: TARGET_TABLE
  source: relationship.flipkart.cashback_settlement
  target: table.flipkart.settlement
  fields:
    edge_family: data_understanding
    evidence_basis: relationship.fields.right_table
    confidence: high
    canonical_cognee_edge: true
    marketplace_only: true
    canonical_edge_type: TARGET_TABLE
    inverse_edge_type: TARGET_OF_RELATIONSHIP
    materialize_inverse: false
    edge_class: canonical
    source_type: relationship
    target_type: table
```

```yaml
candidate_edge:
  edge_id: edge.relationship.flipkart.cashback_settlement.uses_source_column.column.cashback.order_id
  edge_type: USES_SOURCE_COLUMN
  source: relationship.flipkart.cashback_settlement
  target: column.cashback.order_id
  fields:
    edge_family: data_understanding
    evidence_basis: relationship.fields.join_keys
    confidence: high
    canonical_cognee_edge: true
    marketplace_only: true
    join_key_text: cashback.order_id = settlement.order_id AND item_id
    canonical_edge_type: USES_SOURCE_COLUMN
    inverse_edge_type: SOURCE_COLUMN_OF_RELATIONSHIP
    materialize_inverse: false
    edge_class: canonical
    source_type: relationship
    target_type: column
```

```yaml
candidate_edge:
  edge_id: edge.relationship.flipkart.cashback_settlement.uses_source_column.column.cashback.item_id
  edge_type: USES_SOURCE_COLUMN
  source: relationship.flipkart.cashback_settlement
  target: column.cashback.item_id
  fields:
    edge_family: data_understanding
    evidence_basis: relationship.fields.join_keys
    confidence: high
    canonical_cognee_edge: true
    marketplace_only: true
    join_key_text: cashback.order_id = settlement.order_id AND item_id
    canonical_edge_type: USES_SOURCE_COLUMN
    inverse_edge_type: SOURCE_COLUMN_OF_RELATIONSHIP
    materialize_inverse: false
    edge_class: canonical
    source_type: relationship
    target_type: column
```

```yaml
candidate_edge:
  edge_id: edge.relationship.flipkart.cashback_settlement.uses_target_column.column.settlement.order_id
  edge_type: USES_TARGET_COLUMN
  source: relationship.flipkart.cashback_settlement
  target: column.settlement.order_id
  fields:
    edge_family: data_understanding
    evidence_basis: relationship.fields.join_keys
    confidence: high
    canonical_cognee_edge: true
    marketplace_only: true
    join_key_text: cashback.order_id = settlement.order_id AND item_id
    canonical_edge_type: USES_TARGET_COLUMN
    inverse_edge_type: TARGET_COLUMN_OF_RELATIONSHIP
    materialize_inverse: false
    edge_class: canonical
    source_type: relationship
    target_type: column
```

```yaml
candidate_edge:
  edge_id: edge.relationship.flipkart.cashback_settlement.uses_target_column.column.settlement.item_id
  edge_type: USES_TARGET_COLUMN
  source: relationship.flipkart.cashback_settlement
  target: column.settlement.item_id
  fields:
    edge_family: data_understanding
    evidence_basis: relationship.fields.join_keys
    confidence: high
    canonical_cognee_edge: true
    marketplace_only: true
    join_key_text: cashback.order_id = settlement.order_id AND item_id
    canonical_edge_type: USES_TARGET_COLUMN
    inverse_edge_type: TARGET_COLUMN_OF_RELATIONSHIP
    materialize_inverse: false
    edge_class: canonical
    source_type: relationship
    target_type: column
```

```yaml
candidate_edge:
  edge_id: edge.table.flipkart.cashback.has_relationship.relationship.flipkart.cashback_commission
  edge_type: HAS_RELATIONSHIP
  source: table.flipkart.cashback
  target: relationship.flipkart.cashback_commission
  fields:
    edge_family: data_understanding
    evidence_basis: relationship.fields.left_table
    confidence: high
    canonical_cognee_edge: true
    marketplace_only: true
    canonical_edge_type: HAS_RELATIONSHIP
    inverse_edge_type: RELATIONSHIP_OF_TABLE
    materialize_inverse: false
    edge_class: canonical
    source_type: table
    target_type: relationship
```

```yaml
candidate_edge:
  edge_id: edge.table.flipkart.commission.has_relationship.relationship.flipkart.cashback_commission
  edge_type: HAS_RELATIONSHIP
  source: table.flipkart.commission
  target: relationship.flipkart.cashback_commission
  fields:
    edge_family: data_understanding
    evidence_basis: relationship.fields.right_table
    confidence: high
    canonical_cognee_edge: true
    marketplace_only: true
    canonical_edge_type: HAS_RELATIONSHIP
    inverse_edge_type: RELATIONSHIP_OF_TABLE
    materialize_inverse: false
    edge_class: canonical
    source_type: table
    target_type: relationship
```

```yaml
candidate_edge:
  edge_id: edge.relationship.flipkart.cashback_commission.source_table.table.flipkart.cashback
  edge_type: SOURCE_TABLE
  source: relationship.flipkart.cashback_commission
  target: table.flipkart.cashback
  fields:
    edge_family: data_understanding
    evidence_basis: relationship.fields.left_table
    confidence: high
    canonical_cognee_edge: true
    marketplace_only: true
    canonical_edge_type: SOURCE_TABLE
    inverse_edge_type: SOURCE_OF_RELATIONSHIP
    materialize_inverse: false
    edge_class: canonical
    source_type: relationship
    target_type: table
```

```yaml
candidate_edge:
  edge_id: edge.relationship.flipkart.cashback_commission.target_table.table.flipkart.commission
  edge_type: TARGET_TABLE
  source: relationship.flipkart.cashback_commission
  target: table.flipkart.commission
  fields:
    edge_family: data_understanding
    evidence_basis: relationship.fields.right_table
    confidence: high
    canonical_cognee_edge: true
    marketplace_only: true
    canonical_edge_type: TARGET_TABLE
    inverse_edge_type: TARGET_OF_RELATIONSHIP
    materialize_inverse: false
    edge_class: canonical
    source_type: relationship
    target_type: table
```

```yaml
candidate_edge:
  edge_id: edge.relationship.flipkart.cashback_commission.uses_source_column.column.cashback.order_id
  edge_type: USES_SOURCE_COLUMN
  source: relationship.flipkart.cashback_commission
  target: column.cashback.order_id
  fields:
    edge_family: data_understanding
    evidence_basis: relationship.fields.join_keys
    confidence: high
    canonical_cognee_edge: true
    marketplace_only: true
    join_key_text: REPLACE(cashback.order_id, 'OD', '') = commission.order_id AND item_id
    canonical_edge_type: USES_SOURCE_COLUMN
    inverse_edge_type: SOURCE_COLUMN_OF_RELATIONSHIP
    materialize_inverse: false
    edge_class: canonical
    source_type: relationship
    target_type: column
```

```yaml
candidate_edge:
  edge_id: edge.relationship.flipkart.cashback_commission.uses_source_column.column.cashback.item_id
  edge_type: USES_SOURCE_COLUMN
  source: relationship.flipkart.cashback_commission
  target: column.cashback.item_id
  fields:
    edge_family: data_understanding
    evidence_basis: relationship.fields.join_keys
    confidence: high
    canonical_cognee_edge: true
    marketplace_only: true
    join_key_text: REPLACE(cashback.order_id, 'OD', '') = commission.order_id AND item_id
    canonical_edge_type: USES_SOURCE_COLUMN
    inverse_edge_type: SOURCE_COLUMN_OF_RELATIONSHIP
    materialize_inverse: false
    edge_class: canonical
    source_type: relationship
    target_type: column
```

```yaml
candidate_edge:
  edge_id: edge.relationship.flipkart.cashback_commission.uses_target_column.column.commission.order_id
  edge_type: USES_TARGET_COLUMN
  source: relationship.flipkart.cashback_commission
  target: column.commission.order_id
  fields:
    edge_family: data_understanding
    evidence_basis: relationship.fields.join_keys
    confidence: high
    canonical_cognee_edge: true
    marketplace_only: true
    join_key_text: REPLACE(cashback.order_id, 'OD', '') = commission.order_id AND item_id
    canonical_edge_type: USES_TARGET_COLUMN
    inverse_edge_type: TARGET_COLUMN_OF_RELATIONSHIP
    materialize_inverse: false
    edge_class: canonical
    source_type: relationship
    target_type: column
```

```yaml
candidate_edge:
  edge_id: edge.relationship.flipkart.cashback_commission.uses_target_column.column.commission.item_id
  edge_type: USES_TARGET_COLUMN
  source: relationship.flipkart.cashback_commission
  target: column.commission.item_id
  fields:
    edge_family: data_understanding
    evidence_basis: relationship.fields.join_keys
    confidence: high
    canonical_cognee_edge: true
    marketplace_only: true
    join_key_text: REPLACE(cashback.order_id, 'OD', '') = commission.order_id AND item_id
    canonical_edge_type: USES_TARGET_COLUMN
    inverse_edge_type: TARGET_COLUMN_OF_RELATIONSHIP
    materialize_inverse: false
    edge_class: canonical
    source_type: relationship
    target_type: column
```

```yaml
candidate_edge:
  edge_id: edge.table.flipkart.cashback.has_relationship.relationship.flipkart.cashback_oms
  edge_type: HAS_RELATIONSHIP
  source: table.flipkart.cashback
  target: relationship.flipkart.cashback_oms
  fields:
    edge_family: data_understanding
    evidence_basis: relationship.fields.left_table
    confidence: high
    canonical_cognee_edge: true
    marketplace_only: true
    canonical_edge_type: HAS_RELATIONSHIP
    inverse_edge_type: RELATIONSHIP_OF_TABLE
    materialize_inverse: false
    edge_class: canonical
    source_type: table
    target_type: relationship
```

```yaml
candidate_edge:
  edge_id: edge.table.flipkart.oms.has_relationship.relationship.flipkart.cashback_oms
  edge_type: HAS_RELATIONSHIP
  source: table.flipkart.oms
  target: relationship.flipkart.cashback_oms
  fields:
    edge_family: data_understanding
    evidence_basis: relationship.fields.right_table
    confidence: high
    canonical_cognee_edge: true
    marketplace_only: true
    canonical_edge_type: HAS_RELATIONSHIP
    inverse_edge_type: RELATIONSHIP_OF_TABLE
    materialize_inverse: false
    edge_class: canonical
    source_type: table
    target_type: relationship
```

```yaml
candidate_edge:
  edge_id: edge.relationship.flipkart.cashback_oms.source_table.table.flipkart.cashback
  edge_type: SOURCE_TABLE
  source: relationship.flipkart.cashback_oms
  target: table.flipkart.cashback
  fields:
    edge_family: data_understanding
    evidence_basis: relationship.fields.left_table
    confidence: high
    canonical_cognee_edge: true
    marketplace_only: true
    canonical_edge_type: SOURCE_TABLE
    inverse_edge_type: SOURCE_OF_RELATIONSHIP
    materialize_inverse: false
    edge_class: canonical
    source_type: relationship
    target_type: table
```

```yaml
candidate_edge:
  edge_id: edge.relationship.flipkart.cashback_oms.target_table.table.flipkart.oms
  edge_type: TARGET_TABLE
  source: relationship.flipkart.cashback_oms
  target: table.flipkart.oms
  fields:
    edge_family: data_understanding
    evidence_basis: relationship.fields.right_table
    confidence: high
    canonical_cognee_edge: true
    marketplace_only: true
    canonical_edge_type: TARGET_TABLE
    inverse_edge_type: TARGET_OF_RELATIONSHIP
    materialize_inverse: false
    edge_class: canonical
    source_type: relationship
    target_type: table
```

```yaml
candidate_edge:
  edge_id: edge.relationship.flipkart.cashback_oms.uses_source_column.column.cashback.order_id
  edge_type: USES_SOURCE_COLUMN
  source: relationship.flipkart.cashback_oms
  target: column.cashback.order_id
  fields:
    edge_family: data_understanding
    evidence_basis: relationship.fields.join_keys
    confidence: high
    canonical_cognee_edge: true
    marketplace_only: true
    join_key_text: cashback.order_id = oms.order_id AND item_id
    canonical_edge_type: USES_SOURCE_COLUMN
    inverse_edge_type: SOURCE_COLUMN_OF_RELATIONSHIP
    materialize_inverse: false
    edge_class: canonical
    source_type: relationship
    target_type: column
```

```yaml
candidate_edge:
  edge_id: edge.relationship.flipkart.cashback_oms.uses_source_column.column.cashback.item_id
  edge_type: USES_SOURCE_COLUMN
  source: relationship.flipkart.cashback_oms
  target: column.cashback.item_id
  fields:
    edge_family: data_understanding
    evidence_basis: relationship.fields.join_keys
    confidence: high
    canonical_cognee_edge: true
    marketplace_only: true
    join_key_text: cashback.order_id = oms.order_id AND item_id
    canonical_edge_type: USES_SOURCE_COLUMN
    inverse_edge_type: SOURCE_COLUMN_OF_RELATIONSHIP
    materialize_inverse: false
    edge_class: canonical
    source_type: relationship
    target_type: column
```

```yaml
candidate_edge:
  edge_id: edge.relationship.flipkart.cashback_oms.uses_target_column.column.oms.order_id
  edge_type: USES_TARGET_COLUMN
  source: relationship.flipkart.cashback_oms
  target: column.oms.order_id
  fields:
    edge_family: data_understanding
    evidence_basis: relationship.fields.join_keys
    confidence: high
    canonical_cognee_edge: true
    marketplace_only: true
    join_key_text: cashback.order_id = oms.order_id AND item_id
    canonical_edge_type: USES_TARGET_COLUMN
    inverse_edge_type: TARGET_COLUMN_OF_RELATIONSHIP
    materialize_inverse: false
    edge_class: canonical
    source_type: relationship
    target_type: column
```

```yaml
candidate_edge:
  edge_id: edge.relationship.flipkart.cashback_oms.uses_target_column.column.oms.item_id
  edge_type: USES_TARGET_COLUMN
  source: relationship.flipkart.cashback_oms
  target: column.oms.item_id
  fields:
    edge_family: data_understanding
    evidence_basis: relationship.fields.join_keys
    confidence: high
    canonical_cognee_edge: true
    marketplace_only: true
    join_key_text: cashback.order_id = oms.order_id AND item_id
    canonical_edge_type: USES_TARGET_COLUMN
    inverse_edge_type: TARGET_COLUMN_OF_RELATIONSHIP
    materialize_inverse: false
    edge_class: canonical
    source_type: relationship
    target_type: column
```

```yaml
candidate_edge:
  edge_id: edge.metric.gross_merchandise_value.has_implementation.metric_implementation.flipkart.gmv.oms
  edge_type: HAS_IMPLEMENTATION
  source: metric.gross_merchandise_value
  target: metric_implementation.flipkart.gmv.oms
  fields:
    edge_family: metric_understanding
    evidence_basis: metric_implementation.fields.metric_id
    confidence: high
    canonical_cognee_edge: true
    marketplace_only: true
    canonical_edge_type: HAS_IMPLEMENTATION
    inverse_edge_type: IMPLEMENTS_METRIC
    materialize_inverse: true
    edge_class: canonical
    source_type: metric
    target_type: metric_implementation
```

```yaml
candidate_edge:
  edge_id: edge.metric_implementation.flipkart.gmv.oms.implements_metric.metric.gross_merchandise_value
  edge_type: IMPLEMENTS_METRIC
  source: metric_implementation.flipkart.gmv.oms
  target: metric.gross_merchandise_value
  fields:
    edge_family: metric_understanding
    evidence_basis: metric_implementation.fields.metric_id
    confidence: high
    canonical_cognee_edge: true
    marketplace_only: true
    canonical_edge_type: IMPLEMENTS_METRIC
    legacy_edge_aliases:
    - implements_metric
    inverse_edge_type: HAS_IMPLEMENTATION
    materialize_inverse: true
    edge_class: canonical
    source_type: metric_implementation
    target_type: metric
```

```yaml
candidate_edge:
  edge_id: edge.metric_implementation.flipkart.gmv.oms.uses_table.table.flipkart.oms
  edge_type: USES_TABLE
  source: metric_implementation.flipkart.gmv.oms
  target: table.flipkart.oms
  fields:
    edge_family: metric_understanding
    evidence_basis: metric_implementation.fields.source_table
    confidence: high
    canonical_cognee_edge: true
    marketplace_only: true
    canonical_edge_type: USES_TABLE
    legacy_edge_aliases:
    - implementation_uses_table
    inverse_edge_type: USED_BY_IMPLEMENTATION
    materialize_inverse: false
    edge_class: canonical
    source_type: metric_implementation
    target_type: table
```

```yaml
candidate_edge:
  edge_id: edge.metric_implementation.flipkart.gmv.oms.uses_column.column.oms.charged_amount
  edge_type: USES_COLUMN
  source: metric_implementation.flipkart.gmv.oms
  target: column.oms.charged_amount
  fields:
    edge_family: metric_understanding
    evidence_basis: metric_implementation.fields.source_columns
    confidence: high
    canonical_cognee_edge: true
    marketplace_only: true
    canonical_edge_type: USES_COLUMN
    legacy_edge_aliases:
    - implementation_uses_column
    inverse_edge_type: USED_BY_IMPLEMENTATION
    materialize_inverse: false
    edge_class: canonical
    source_type: metric_implementation
    target_type: column
```

```yaml
candidate_edge:
  edge_id: edge.metric.gross_merchandise_value.has_implementation.metric_implementation.flipkart.gmv.settlement_fallback
  edge_type: HAS_IMPLEMENTATION
  source: metric.gross_merchandise_value
  target: metric_implementation.flipkart.gmv.settlement_fallback
  fields:
    edge_family: metric_understanding
    evidence_basis: metric_implementation.fields.metric_id
    confidence: high
    canonical_cognee_edge: true
    marketplace_only: true
    canonical_edge_type: HAS_IMPLEMENTATION
    inverse_edge_type: IMPLEMENTS_METRIC
    materialize_inverse: true
    edge_class: canonical
    source_type: metric
    target_type: metric_implementation
```

```yaml
candidate_edge:
  edge_id: edge.metric_implementation.flipkart.gmv.settlement_fallback.implements_metric.metric.gross_merchandise_value
  edge_type: IMPLEMENTS_METRIC
  source: metric_implementation.flipkart.gmv.settlement_fallback
  target: metric.gross_merchandise_value
  fields:
    edge_family: metric_understanding
    evidence_basis: metric_implementation.fields.metric_id
    confidence: high
    canonical_cognee_edge: true
    marketplace_only: true
    canonical_edge_type: IMPLEMENTS_METRIC
    legacy_edge_aliases:
    - implements_metric
    inverse_edge_type: HAS_IMPLEMENTATION
    materialize_inverse: true
    edge_class: canonical
    source_type: metric_implementation
    target_type: metric
```

```yaml
candidate_edge:
  edge_id: edge.metric_implementation.flipkart.gmv.settlement_fallback.uses_table.table.flipkart.settlement
  edge_type: USES_TABLE
  source: metric_implementation.flipkart.gmv.settlement_fallback
  target: table.flipkart.settlement
  fields:
    edge_family: metric_understanding
    evidence_basis: metric_implementation.fields.source_table
    confidence: high
    canonical_cognee_edge: true
    marketplace_only: true
    canonical_edge_type: USES_TABLE
    legacy_edge_aliases:
    - implementation_uses_table
    inverse_edge_type: USED_BY_IMPLEMENTATION
    materialize_inverse: false
    edge_class: canonical
    source_type: metric_implementation
    target_type: table
```

```yaml
candidate_edge:
  edge_id: edge.metric_implementation.flipkart.gmv.settlement_fallback.uses_column.column.settlement.sale_settled_amount
  edge_type: USES_COLUMN
  source: metric_implementation.flipkart.gmv.settlement_fallback
  target: column.settlement.sale_settled_amount
  fields:
    edge_family: metric_understanding
    evidence_basis: metric_implementation.fields.source_columns
    confidence: high
    canonical_cognee_edge: true
    marketplace_only: true
    canonical_edge_type: USES_COLUMN
    legacy_edge_aliases:
    - implementation_uses_column
    inverse_edge_type: USED_BY_IMPLEMENTATION
    materialize_inverse: false
    edge_class: canonical
    source_type: metric_implementation
    target_type: column
```

```yaml
candidate_edge:
  edge_id: edge.metric.net_settlement.has_implementation.metric_implementation.flipkart.net_settlement
  edge_type: HAS_IMPLEMENTATION
  source: metric.net_settlement
  target: metric_implementation.flipkart.net_settlement
  fields:
    edge_family: metric_understanding
    evidence_basis: metric_implementation.fields.metric_id
    confidence: high
    canonical_cognee_edge: true
    marketplace_only: true
    canonical_edge_type: HAS_IMPLEMENTATION
    inverse_edge_type: IMPLEMENTS_METRIC
    materialize_inverse: true
    edge_class: canonical
    source_type: metric
    target_type: metric_implementation
```

```yaml
candidate_edge:
  edge_id: edge.metric_implementation.flipkart.net_settlement.implements_metric.metric.net_settlement
  edge_type: IMPLEMENTS_METRIC
  source: metric_implementation.flipkart.net_settlement
  target: metric.net_settlement
  fields:
    edge_family: metric_understanding
    evidence_basis: metric_implementation.fields.metric_id
    confidence: high
    canonical_cognee_edge: true
    marketplace_only: true
    canonical_edge_type: IMPLEMENTS_METRIC
    legacy_edge_aliases:
    - implements_metric
    inverse_edge_type: HAS_IMPLEMENTATION
    materialize_inverse: true
    edge_class: canonical
    source_type: metric_implementation
    target_type: metric
```

```yaml
candidate_edge:
  edge_id: edge.metric_implementation.flipkart.net_settlement.uses_table.table.flipkart.settlement
  edge_type: USES_TABLE
  source: metric_implementation.flipkart.net_settlement
  target: table.flipkart.settlement
  fields:
    edge_family: metric_understanding
    evidence_basis: metric_implementation.fields.source_table
    confidence: high
    canonical_cognee_edge: true
    marketplace_only: true
    canonical_edge_type: USES_TABLE
    legacy_edge_aliases:
    - implementation_uses_table
    inverse_edge_type: USED_BY_IMPLEMENTATION
    materialize_inverse: false
    edge_class: canonical
    source_type: metric_implementation
    target_type: table
```

```yaml
candidate_edge:
  edge_id: edge.metric_implementation.flipkart.net_settlement.uses_column.column.settlement.settled_amount
  edge_type: USES_COLUMN
  source: metric_implementation.flipkart.net_settlement
  target: column.settlement.settled_amount
  fields:
    edge_family: metric_understanding
    evidence_basis: metric_implementation.fields.source_columns
    confidence: high
    canonical_cognee_edge: true
    marketplace_only: true
    canonical_edge_type: USES_COLUMN
    legacy_edge_aliases:
    - implementation_uses_column
    inverse_edge_type: USED_BY_IMPLEMENTATION
    materialize_inverse: false
    edge_class: canonical
    source_type: metric_implementation
    target_type: column
```

```yaml
candidate_edge:
  edge_id: edge.metric.realization_rate.has_implementation.metric_implementation.flipkart.realization_rate
  edge_type: HAS_IMPLEMENTATION
  source: metric.realization_rate
  target: metric_implementation.flipkart.realization_rate
  fields:
    edge_family: metric_understanding
    evidence_basis: metric_implementation.fields.metric_id
    confidence: high
    canonical_cognee_edge: true
    marketplace_only: true
    canonical_edge_type: HAS_IMPLEMENTATION
    inverse_edge_type: IMPLEMENTS_METRIC
    materialize_inverse: true
    edge_class: canonical
    source_type: metric
    target_type: metric_implementation
```

```yaml
candidate_edge:
  edge_id: edge.metric_implementation.flipkart.realization_rate.implements_metric.metric.realization_rate
  edge_type: IMPLEMENTS_METRIC
  source: metric_implementation.flipkart.realization_rate
  target: metric.realization_rate
  fields:
    edge_family: metric_understanding
    evidence_basis: metric_implementation.fields.metric_id
    confidence: high
    canonical_cognee_edge: true
    marketplace_only: true
    canonical_edge_type: IMPLEMENTS_METRIC
    legacy_edge_aliases:
    - implements_metric
    inverse_edge_type: HAS_IMPLEMENTATION
    materialize_inverse: true
    edge_class: canonical
    source_type: metric_implementation
    target_type: metric
```

```yaml
candidate_edge:
  edge_id: edge.metric_implementation.flipkart.realization_rate.uses_table.table.flipkart.settlement
  edge_type: USES_TABLE
  source: metric_implementation.flipkart.realization_rate
  target: table.flipkart.settlement
  fields:
    edge_family: metric_understanding
    evidence_basis: metric_implementation.fields.source_table
    confidence: high
    canonical_cognee_edge: true
    marketplace_only: true
    canonical_edge_type: USES_TABLE
    legacy_edge_aliases:
    - implementation_uses_table
    inverse_edge_type: USED_BY_IMPLEMENTATION
    materialize_inverse: false
    edge_class: canonical
    source_type: metric_implementation
    target_type: table
```

```yaml
candidate_edge:
  edge_id: edge.metric_implementation.flipkart.realization_rate.uses_column.column.settlement.settled_amount
  edge_type: USES_COLUMN
  source: metric_implementation.flipkart.realization_rate
  target: column.settlement.settled_amount
  fields:
    edge_family: metric_understanding
    evidence_basis: metric_implementation.fields.source_columns
    confidence: high
    canonical_cognee_edge: true
    marketplace_only: true
    canonical_edge_type: USES_COLUMN
    legacy_edge_aliases:
    - implementation_uses_column
    inverse_edge_type: USED_BY_IMPLEMENTATION
    materialize_inverse: false
    edge_class: canonical
    source_type: metric_implementation
    target_type: column
```

```yaml
candidate_edge:
  edge_id: edge.metric_implementation.flipkart.realization_rate.uses_column.column.settlement.sale_settled_amount
  edge_type: USES_COLUMN
  source: metric_implementation.flipkart.realization_rate
  target: column.settlement.sale_settled_amount
  fields:
    edge_family: metric_understanding
    evidence_basis: metric_implementation.fields.source_columns
    confidence: high
    canonical_cognee_edge: true
    marketplace_only: true
    canonical_edge_type: USES_COLUMN
    legacy_edge_aliases:
    - implementation_uses_column
    inverse_edge_type: USED_BY_IMPLEMENTATION
    materialize_inverse: false
    edge_class: canonical
    source_type: metric_implementation
    target_type: column
```

```yaml
candidate_edge:
  edge_id: edge.metric_implementation.flipkart.realization_rate.uses_formula_template.formula.flipkart.realization_rate
  edge_type: USES_FORMULA_TEMPLATE
  source: metric_implementation.flipkart.realization_rate
  target: formula.flipkart.realization_rate
  fields:
    edge_family: metric_understanding
    evidence_basis: deterministic formula/name mapping
    confidence: high
    canonical_cognee_edge: true
    marketplace_only: true
    canonical_edge_type: USES_FORMULA_TEMPLATE
    inverse_edge_type: USED_BY_IMPLEMENTATION
    materialize_inverse: false
    edge_class: canonical
    source_type: metric_implementation
    target_type: formula_template
```

```yaml
candidate_edge:
  edge_id: edge.metric.effective_fee_rate.has_implementation.metric_implementation.flipkart.effective_fee_rate
  edge_type: HAS_IMPLEMENTATION
  source: metric.effective_fee_rate
  target: metric_implementation.flipkart.effective_fee_rate
  fields:
    edge_family: metric_understanding
    evidence_basis: metric_implementation.fields.metric_id
    confidence: high
    canonical_cognee_edge: true
    marketplace_only: true
    canonical_edge_type: HAS_IMPLEMENTATION
    inverse_edge_type: IMPLEMENTS_METRIC
    materialize_inverse: true
    edge_class: canonical
    source_type: metric
    target_type: metric_implementation
```

```yaml
candidate_edge:
  edge_id: edge.metric_implementation.flipkart.effective_fee_rate.implements_metric.metric.effective_fee_rate
  edge_type: IMPLEMENTS_METRIC
  source: metric_implementation.flipkart.effective_fee_rate
  target: metric.effective_fee_rate
  fields:
    edge_family: metric_understanding
    evidence_basis: metric_implementation.fields.metric_id
    confidence: high
    canonical_cognee_edge: true
    marketplace_only: true
    canonical_edge_type: IMPLEMENTS_METRIC
    legacy_edge_aliases:
    - implements_metric
    inverse_edge_type: HAS_IMPLEMENTATION
    materialize_inverse: true
    edge_class: canonical
    source_type: metric_implementation
    target_type: metric
```

```yaml
candidate_edge:
  edge_id: edge.metric_implementation.flipkart.effective_fee_rate.uses_table.table.flipkart.settlement
  edge_type: USES_TABLE
  source: metric_implementation.flipkart.effective_fee_rate
  target: table.flipkart.settlement
  fields:
    edge_family: metric_understanding
    evidence_basis: metric_implementation.fields.source_table
    confidence: high
    canonical_cognee_edge: true
    marketplace_only: true
    canonical_edge_type: USES_TABLE
    legacy_edge_aliases:
    - implementation_uses_table
    inverse_edge_type: USED_BY_IMPLEMENTATION
    materialize_inverse: false
    edge_class: canonical
    source_type: metric_implementation
    target_type: table
```

```yaml
candidate_edge:
  edge_id: edge.metric_implementation.flipkart.effective_fee_rate.uses_column.column.settlement.mp_fee
  edge_type: USES_COLUMN
  source: metric_implementation.flipkart.effective_fee_rate
  target: column.settlement.mp_fee
  fields:
    edge_family: metric_understanding
    evidence_basis: metric_implementation.fields.source_columns
    confidence: high
    canonical_cognee_edge: true
    marketplace_only: true
    canonical_edge_type: USES_COLUMN
    legacy_edge_aliases:
    - implementation_uses_column
    inverse_edge_type: USED_BY_IMPLEMENTATION
    materialize_inverse: false
    edge_class: canonical
    source_type: metric_implementation
    target_type: column
```

```yaml
candidate_edge:
  edge_id: edge.metric_implementation.flipkart.effective_fee_rate.uses_column.column.settlement.sale_settled_amount
  edge_type: USES_COLUMN
  source: metric_implementation.flipkart.effective_fee_rate
  target: column.settlement.sale_settled_amount
  fields:
    edge_family: metric_understanding
    evidence_basis: metric_implementation.fields.source_columns
    confidence: high
    canonical_cognee_edge: true
    marketplace_only: true
    canonical_edge_type: USES_COLUMN
    legacy_edge_aliases:
    - implementation_uses_column
    inverse_edge_type: USED_BY_IMPLEMENTATION
    materialize_inverse: false
    edge_class: canonical
    source_type: metric_implementation
    target_type: column
```

```yaml
candidate_edge:
  edge_id: edge.metric_implementation.flipkart.effective_fee_rate.uses_formula_template.formula.flipkart.effective_fee_rate
  edge_type: USES_FORMULA_TEMPLATE
  source: metric_implementation.flipkart.effective_fee_rate
  target: formula.flipkart.effective_fee_rate
  fields:
    edge_family: metric_understanding
    evidence_basis: deterministic formula/name mapping
    confidence: high
    canonical_cognee_edge: true
    marketplace_only: true
    canonical_edge_type: USES_FORMULA_TEMPLATE
    inverse_edge_type: USED_BY_IMPLEMENTATION
    materialize_inverse: false
    edge_class: canonical
    source_type: metric_implementation
    target_type: formula_template
```

```yaml
candidate_edge:
  edge_id: edge.metric.marketplace_fee_total.has_implementation.metric_implementation.flipkart.mp_fee_total
  edge_type: HAS_IMPLEMENTATION
  source: metric.marketplace_fee_total
  target: metric_implementation.flipkart.mp_fee_total
  fields:
    edge_family: metric_understanding
    evidence_basis: metric_implementation.fields.metric_id
    confidence: high
    canonical_cognee_edge: true
    marketplace_only: true
    canonical_edge_type: HAS_IMPLEMENTATION
    inverse_edge_type: IMPLEMENTS_METRIC
    materialize_inverse: true
    edge_class: canonical
    source_type: metric
    target_type: metric_implementation
```

```yaml
candidate_edge:
  edge_id: edge.metric_implementation.flipkart.mp_fee_total.implements_metric.metric.marketplace_fee_total
  edge_type: IMPLEMENTS_METRIC
  source: metric_implementation.flipkart.mp_fee_total
  target: metric.marketplace_fee_total
  fields:
    edge_family: metric_understanding
    evidence_basis: metric_implementation.fields.metric_id
    confidence: high
    canonical_cognee_edge: true
    marketplace_only: true
    canonical_edge_type: IMPLEMENTS_METRIC
    legacy_edge_aliases:
    - implements_metric
    inverse_edge_type: HAS_IMPLEMENTATION
    materialize_inverse: true
    edge_class: canonical
    source_type: metric_implementation
    target_type: metric
```

```yaml
candidate_edge:
  edge_id: edge.metric_implementation.flipkart.mp_fee_total.uses_table.table.flipkart.settlement
  edge_type: USES_TABLE
  source: metric_implementation.flipkart.mp_fee_total
  target: table.flipkart.settlement
  fields:
    edge_family: metric_understanding
    evidence_basis: metric_implementation.fields.source_table
    confidence: high
    canonical_cognee_edge: true
    marketplace_only: true
    canonical_edge_type: USES_TABLE
    legacy_edge_aliases:
    - implementation_uses_table
    inverse_edge_type: USED_BY_IMPLEMENTATION
    materialize_inverse: false
    edge_class: canonical
    source_type: metric_implementation
    target_type: table
```

```yaml
candidate_edge:
  edge_id: edge.metric_implementation.flipkart.mp_fee_total.uses_column.column.settlement.mp_fee
  edge_type: USES_COLUMN
  source: metric_implementation.flipkart.mp_fee_total
  target: column.settlement.mp_fee
  fields:
    edge_family: metric_understanding
    evidence_basis: metric_implementation.fields.source_columns
    confidence: high
    canonical_cognee_edge: true
    marketplace_only: true
    canonical_edge_type: USES_COLUMN
    legacy_edge_aliases:
    - implementation_uses_column
    inverse_edge_type: USED_BY_IMPLEMENTATION
    materialize_inverse: false
    edge_class: canonical
    source_type: metric_implementation
    target_type: column
```

```yaml
candidate_edge:
  edge_id: edge.metric.commission_fee.has_implementation.metric_implementation.flipkart.commission_fee_detail
  edge_type: HAS_IMPLEMENTATION
  source: metric.commission_fee
  target: metric_implementation.flipkart.commission_fee_detail
  fields:
    edge_family: metric_understanding
    evidence_basis: metric_implementation.fields.metric_id
    confidence: high
    canonical_cognee_edge: true
    marketplace_only: true
    canonical_edge_type: HAS_IMPLEMENTATION
    inverse_edge_type: IMPLEMENTS_METRIC
    materialize_inverse: true
    edge_class: canonical
    source_type: metric
    target_type: metric_implementation
```

```yaml
candidate_edge:
  edge_id: edge.metric_implementation.flipkart.commission_fee_detail.implements_metric.metric.commission_fee
  edge_type: IMPLEMENTS_METRIC
  source: metric_implementation.flipkart.commission_fee_detail
  target: metric.commission_fee
  fields:
    edge_family: metric_understanding
    evidence_basis: metric_implementation.fields.metric_id
    confidence: high
    canonical_cognee_edge: true
    marketplace_only: true
    canonical_edge_type: IMPLEMENTS_METRIC
    legacy_edge_aliases:
    - implements_metric
    inverse_edge_type: HAS_IMPLEMENTATION
    materialize_inverse: true
    edge_class: canonical
    source_type: metric_implementation
    target_type: metric
```

```yaml
candidate_edge:
  edge_id: edge.metric_implementation.flipkart.commission_fee_detail.uses_table.table.flipkart.commission
  edge_type: USES_TABLE
  source: metric_implementation.flipkart.commission_fee_detail
  target: table.flipkart.commission
  fields:
    edge_family: metric_understanding
    evidence_basis: metric_implementation.fields.source_table
    confidence: high
    canonical_cognee_edge: true
    marketplace_only: true
    canonical_edge_type: USES_TABLE
    legacy_edge_aliases:
    - implementation_uses_table
    inverse_edge_type: USED_BY_IMPLEMENTATION
    materialize_inverse: false
    edge_class: canonical
    source_type: metric_implementation
    target_type: table
```

```yaml
candidate_edge:
  edge_id: edge.metric_implementation.flipkart.commission_fee_detail.uses_column.column.commission.charged_amount
  edge_type: USES_COLUMN
  source: metric_implementation.flipkart.commission_fee_detail
  target: column.commission.charged_amount
  fields:
    edge_family: metric_understanding
    evidence_basis: metric_implementation.fields.source_columns
    confidence: high
    canonical_cognee_edge: true
    marketplace_only: true
    canonical_edge_type: USES_COLUMN
    legacy_edge_aliases:
    - implementation_uses_column
    inverse_edge_type: USED_BY_IMPLEMENTATION
    materialize_inverse: false
    edge_class: canonical
    source_type: metric_implementation
    target_type: column
```

```yaml
candidate_edge:
  edge_id: edge.metric_implementation.flipkart.commission_fee_detail.uses_column.column.commission.description
  edge_type: USES_COLUMN
  source: metric_implementation.flipkart.commission_fee_detail
  target: column.commission.description
  fields:
    edge_family: metric_understanding
    evidence_basis: metric_implementation.fields.source_columns
    confidence: high
    canonical_cognee_edge: true
    marketplace_only: true
    canonical_edge_type: USES_COLUMN
    legacy_edge_aliases:
    - implementation_uses_column
    inverse_edge_type: USED_BY_IMPLEMENTATION
    materialize_inverse: false
    edge_class: canonical
    source_type: metric_implementation
    target_type: column
```

```yaml
candidate_edge:
  edge_id: edge.metric_implementation.flipkart.commission_fee_detail.uses_formula_template.formula.flipkart.total_fee_detail
  edge_type: USES_FORMULA_TEMPLATE
  source: metric_implementation.flipkart.commission_fee_detail
  target: formula.flipkart.total_fee_detail
  fields:
    edge_family: metric_understanding
    evidence_basis: deterministic formula/name mapping
    confidence: high
    canonical_cognee_edge: true
    marketplace_only: true
    canonical_edge_type: USES_FORMULA_TEMPLATE
    inverse_edge_type: USED_BY_IMPLEMENTATION
    materialize_inverse: false
    edge_class: canonical
    source_type: metric_implementation
    target_type: formula_template
```

```yaml
candidate_edge:
  edge_id: edge.metric.fixed_fee.has_implementation.metric_implementation.flipkart.fixed_fee_detail
  edge_type: HAS_IMPLEMENTATION
  source: metric.fixed_fee
  target: metric_implementation.flipkart.fixed_fee_detail
  fields:
    edge_family: metric_understanding
    evidence_basis: metric_implementation.fields.metric_id
    confidence: high
    canonical_cognee_edge: true
    marketplace_only: true
    canonical_edge_type: HAS_IMPLEMENTATION
    inverse_edge_type: IMPLEMENTS_METRIC
    materialize_inverse: true
    edge_class: canonical
    source_type: metric
    target_type: metric_implementation
```

```yaml
candidate_edge:
  edge_id: edge.metric_implementation.flipkart.fixed_fee_detail.implements_metric.metric.fixed_fee
  edge_type: IMPLEMENTS_METRIC
  source: metric_implementation.flipkart.fixed_fee_detail
  target: metric.fixed_fee
  fields:
    edge_family: metric_understanding
    evidence_basis: metric_implementation.fields.metric_id
    confidence: high
    canonical_cognee_edge: true
    marketplace_only: true
    canonical_edge_type: IMPLEMENTS_METRIC
    legacy_edge_aliases:
    - implements_metric
    inverse_edge_type: HAS_IMPLEMENTATION
    materialize_inverse: true
    edge_class: canonical
    source_type: metric_implementation
    target_type: metric
```

```yaml
candidate_edge:
  edge_id: edge.metric_implementation.flipkart.fixed_fee_detail.uses_table.table.flipkart.commission
  edge_type: USES_TABLE
  source: metric_implementation.flipkart.fixed_fee_detail
  target: table.flipkart.commission
  fields:
    edge_family: metric_understanding
    evidence_basis: metric_implementation.fields.source_table
    confidence: high
    canonical_cognee_edge: true
    marketplace_only: true
    canonical_edge_type: USES_TABLE
    legacy_edge_aliases:
    - implementation_uses_table
    inverse_edge_type: USED_BY_IMPLEMENTATION
    materialize_inverse: false
    edge_class: canonical
    source_type: metric_implementation
    target_type: table
```

```yaml
candidate_edge:
  edge_id: edge.metric_implementation.flipkart.fixed_fee_detail.uses_column.column.commission.charged_amount
  edge_type: USES_COLUMN
  source: metric_implementation.flipkart.fixed_fee_detail
  target: column.commission.charged_amount
  fields:
    edge_family: metric_understanding
    evidence_basis: metric_implementation.fields.source_columns
    confidence: high
    canonical_cognee_edge: true
    marketplace_only: true
    canonical_edge_type: USES_COLUMN
    legacy_edge_aliases:
    - implementation_uses_column
    inverse_edge_type: USED_BY_IMPLEMENTATION
    materialize_inverse: false
    edge_class: canonical
    source_type: metric_implementation
    target_type: column
```

```yaml
candidate_edge:
  edge_id: edge.metric_implementation.flipkart.fixed_fee_detail.uses_column.column.commission.description
  edge_type: USES_COLUMN
  source: metric_implementation.flipkart.fixed_fee_detail
  target: column.commission.description
  fields:
    edge_family: metric_understanding
    evidence_basis: metric_implementation.fields.source_columns
    confidence: high
    canonical_cognee_edge: true
    marketplace_only: true
    canonical_edge_type: USES_COLUMN
    legacy_edge_aliases:
    - implementation_uses_column
    inverse_edge_type: USED_BY_IMPLEMENTATION
    materialize_inverse: false
    edge_class: canonical
    source_type: metric_implementation
    target_type: column
```

```yaml
candidate_edge:
  edge_id: edge.metric_implementation.flipkart.fixed_fee_detail.uses_formula_template.formula.flipkart.total_fee_detail
  edge_type: USES_FORMULA_TEMPLATE
  source: metric_implementation.flipkart.fixed_fee_detail
  target: formula.flipkart.total_fee_detail
  fields:
    edge_family: metric_understanding
    evidence_basis: deterministic formula/name mapping
    confidence: high
    canonical_cognee_edge: true
    marketplace_only: true
    canonical_edge_type: USES_FORMULA_TEMPLATE
    inverse_edge_type: USED_BY_IMPLEMENTATION
    materialize_inverse: false
    edge_class: canonical
    source_type: metric_implementation
    target_type: formula_template
```

```yaml
candidate_edge:
  edge_id: edge.metric.shipping_fee.has_implementation.metric_implementation.flipkart.shipping_fee_detail
  edge_type: HAS_IMPLEMENTATION
  source: metric.shipping_fee
  target: metric_implementation.flipkart.shipping_fee_detail
  fields:
    edge_family: metric_understanding
    evidence_basis: metric_implementation.fields.metric_id
    confidence: high
    canonical_cognee_edge: true
    marketplace_only: true
    canonical_edge_type: HAS_IMPLEMENTATION
    inverse_edge_type: IMPLEMENTS_METRIC
    materialize_inverse: true
    edge_class: canonical
    source_type: metric
    target_type: metric_implementation
```

```yaml
candidate_edge:
  edge_id: edge.metric_implementation.flipkart.shipping_fee_detail.implements_metric.metric.shipping_fee
  edge_type: IMPLEMENTS_METRIC
  source: metric_implementation.flipkart.shipping_fee_detail
  target: metric.shipping_fee
  fields:
    edge_family: metric_understanding
    evidence_basis: metric_implementation.fields.metric_id
    confidence: high
    canonical_cognee_edge: true
    marketplace_only: true
    canonical_edge_type: IMPLEMENTS_METRIC
    legacy_edge_aliases:
    - implements_metric
    inverse_edge_type: HAS_IMPLEMENTATION
    materialize_inverse: true
    edge_class: canonical
    source_type: metric_implementation
    target_type: metric
```

```yaml
candidate_edge:
  edge_id: edge.metric_implementation.flipkart.shipping_fee_detail.uses_table.table.flipkart.commission
  edge_type: USES_TABLE
  source: metric_implementation.flipkart.shipping_fee_detail
  target: table.flipkart.commission
  fields:
    edge_family: metric_understanding
    evidence_basis: metric_implementation.fields.source_table
    confidence: high
    canonical_cognee_edge: true
    marketplace_only: true
    canonical_edge_type: USES_TABLE
    legacy_edge_aliases:
    - implementation_uses_table
    inverse_edge_type: USED_BY_IMPLEMENTATION
    materialize_inverse: false
    edge_class: canonical
    source_type: metric_implementation
    target_type: table
```

```yaml
candidate_edge:
  edge_id: edge.metric_implementation.flipkart.shipping_fee_detail.uses_column.column.commission.charged_amount
  edge_type: USES_COLUMN
  source: metric_implementation.flipkart.shipping_fee_detail
  target: column.commission.charged_amount
  fields:
    edge_family: metric_understanding
    evidence_basis: metric_implementation.fields.source_columns
    confidence: high
    canonical_cognee_edge: true
    marketplace_only: true
    canonical_edge_type: USES_COLUMN
    legacy_edge_aliases:
    - implementation_uses_column
    inverse_edge_type: USED_BY_IMPLEMENTATION
    materialize_inverse: false
    edge_class: canonical
    source_type: metric_implementation
    target_type: column
```

```yaml
candidate_edge:
  edge_id: edge.metric_implementation.flipkart.shipping_fee_detail.uses_column.column.commission.description
  edge_type: USES_COLUMN
  source: metric_implementation.flipkart.shipping_fee_detail
  target: column.commission.description
  fields:
    edge_family: metric_understanding
    evidence_basis: metric_implementation.fields.source_columns
    confidence: high
    canonical_cognee_edge: true
    marketplace_only: true
    canonical_edge_type: USES_COLUMN
    legacy_edge_aliases:
    - implementation_uses_column
    inverse_edge_type: USED_BY_IMPLEMENTATION
    materialize_inverse: false
    edge_class: canonical
    source_type: metric_implementation
    target_type: column
```

```yaml
candidate_edge:
  edge_id: edge.metric_implementation.flipkart.shipping_fee_detail.uses_formula_template.formula.flipkart.total_fee_detail
  edge_type: USES_FORMULA_TEMPLATE
  source: metric_implementation.flipkart.shipping_fee_detail
  target: formula.flipkart.total_fee_detail
  fields:
    edge_family: metric_understanding
    evidence_basis: deterministic formula/name mapping
    confidence: high
    canonical_cognee_edge: true
    marketplace_only: true
    canonical_edge_type: USES_FORMULA_TEMPLATE
    inverse_edge_type: USED_BY_IMPLEMENTATION
    materialize_inverse: false
    edge_class: canonical
    source_type: metric_implementation
    target_type: formula_template
```

```yaml
candidate_edge:
  edge_id: edge.metric.reverse_shipping_fee.has_implementation.metric_implementation.flipkart.reverse_shipping_fee_detail
  edge_type: HAS_IMPLEMENTATION
  source: metric.reverse_shipping_fee
  target: metric_implementation.flipkart.reverse_shipping_fee_detail
  fields:
    edge_family: metric_understanding
    evidence_basis: metric_implementation.fields.metric_id
    confidence: high
    canonical_cognee_edge: true
    marketplace_only: true
    canonical_edge_type: HAS_IMPLEMENTATION
    inverse_edge_type: IMPLEMENTS_METRIC
    materialize_inverse: true
    edge_class: canonical
    source_type: metric
    target_type: metric_implementation
```

```yaml
candidate_edge:
  edge_id: edge.metric_implementation.flipkart.reverse_shipping_fee_detail.implements_metric.metric.reverse_shipping_fee
  edge_type: IMPLEMENTS_METRIC
  source: metric_implementation.flipkart.reverse_shipping_fee_detail
  target: metric.reverse_shipping_fee
  fields:
    edge_family: metric_understanding
    evidence_basis: metric_implementation.fields.metric_id
    confidence: high
    canonical_cognee_edge: true
    marketplace_only: true
    canonical_edge_type: IMPLEMENTS_METRIC
    legacy_edge_aliases:
    - implements_metric
    inverse_edge_type: HAS_IMPLEMENTATION
    materialize_inverse: true
    edge_class: canonical
    source_type: metric_implementation
    target_type: metric
```

```yaml
candidate_edge:
  edge_id: edge.metric_implementation.flipkart.reverse_shipping_fee_detail.uses_table.table.flipkart.commission
  edge_type: USES_TABLE
  source: metric_implementation.flipkart.reverse_shipping_fee_detail
  target: table.flipkart.commission
  fields:
    edge_family: metric_understanding
    evidence_basis: metric_implementation.fields.source_table
    confidence: high
    canonical_cognee_edge: true
    marketplace_only: true
    canonical_edge_type: USES_TABLE
    legacy_edge_aliases:
    - implementation_uses_table
    inverse_edge_type: USED_BY_IMPLEMENTATION
    materialize_inverse: false
    edge_class: canonical
    source_type: metric_implementation
    target_type: table
```

```yaml
candidate_edge:
  edge_id: edge.metric_implementation.flipkart.reverse_shipping_fee_detail.uses_column.column.commission.charged_amount
  edge_type: USES_COLUMN
  source: metric_implementation.flipkart.reverse_shipping_fee_detail
  target: column.commission.charged_amount
  fields:
    edge_family: metric_understanding
    evidence_basis: metric_implementation.fields.source_columns
    confidence: high
    canonical_cognee_edge: true
    marketplace_only: true
    canonical_edge_type: USES_COLUMN
    legacy_edge_aliases:
    - implementation_uses_column
    inverse_edge_type: USED_BY_IMPLEMENTATION
    materialize_inverse: false
    edge_class: canonical
    source_type: metric_implementation
    target_type: column
```

```yaml
candidate_edge:
  edge_id: edge.metric_implementation.flipkart.reverse_shipping_fee_detail.uses_column.column.commission.description
  edge_type: USES_COLUMN
  source: metric_implementation.flipkart.reverse_shipping_fee_detail
  target: column.commission.description
  fields:
    edge_family: metric_understanding
    evidence_basis: metric_implementation.fields.source_columns
    confidence: high
    canonical_cognee_edge: true
    marketplace_only: true
    canonical_edge_type: USES_COLUMN
    legacy_edge_aliases:
    - implementation_uses_column
    inverse_edge_type: USED_BY_IMPLEMENTATION
    materialize_inverse: false
    edge_class: canonical
    source_type: metric_implementation
    target_type: column
```

```yaml
candidate_edge:
  edge_id: edge.metric_implementation.flipkart.reverse_shipping_fee_detail.uses_formula_template.formula.flipkart.total_fee_detail
  edge_type: USES_FORMULA_TEMPLATE
  source: metric_implementation.flipkart.reverse_shipping_fee_detail
  target: formula.flipkart.total_fee_detail
  fields:
    edge_family: metric_understanding
    evidence_basis: deterministic formula/name mapping
    confidence: high
    canonical_cognee_edge: true
    marketplace_only: true
    canonical_edge_type: USES_FORMULA_TEMPLATE
    inverse_edge_type: USED_BY_IMPLEMENTATION
    materialize_inverse: false
    edge_class: canonical
    source_type: metric_implementation
    target_type: formula_template
```

```yaml
candidate_edge:
  edge_id: edge.metric.collection_fee.has_implementation.metric_implementation.flipkart.collection_fee_detail
  edge_type: HAS_IMPLEMENTATION
  source: metric.collection_fee
  target: metric_implementation.flipkart.collection_fee_detail
  fields:
    edge_family: metric_understanding
    evidence_basis: metric_implementation.fields.metric_id
    confidence: high
    canonical_cognee_edge: true
    marketplace_only: true
    canonical_edge_type: HAS_IMPLEMENTATION
    inverse_edge_type: IMPLEMENTS_METRIC
    materialize_inverse: true
    edge_class: canonical
    source_type: metric
    target_type: metric_implementation
```

```yaml
candidate_edge:
  edge_id: edge.metric_implementation.flipkart.collection_fee_detail.implements_metric.metric.collection_fee
  edge_type: IMPLEMENTS_METRIC
  source: metric_implementation.flipkart.collection_fee_detail
  target: metric.collection_fee
  fields:
    edge_family: metric_understanding
    evidence_basis: metric_implementation.fields.metric_id
    confidence: high
    canonical_cognee_edge: true
    marketplace_only: true
    canonical_edge_type: IMPLEMENTS_METRIC
    legacy_edge_aliases:
    - implements_metric
    inverse_edge_type: HAS_IMPLEMENTATION
    materialize_inverse: true
    edge_class: canonical
    source_type: metric_implementation
    target_type: metric
```

```yaml
candidate_edge:
  edge_id: edge.metric_implementation.flipkart.collection_fee_detail.uses_table.table.flipkart.commission
  edge_type: USES_TABLE
  source: metric_implementation.flipkart.collection_fee_detail
  target: table.flipkart.commission
  fields:
    edge_family: metric_understanding
    evidence_basis: metric_implementation.fields.source_table
    confidence: high
    canonical_cognee_edge: true
    marketplace_only: true
    canonical_edge_type: USES_TABLE
    legacy_edge_aliases:
    - implementation_uses_table
    inverse_edge_type: USED_BY_IMPLEMENTATION
    materialize_inverse: false
    edge_class: canonical
    source_type: metric_implementation
    target_type: table
```

```yaml
candidate_edge:
  edge_id: edge.metric_implementation.flipkart.collection_fee_detail.uses_column.column.commission.charged_amount
  edge_type: USES_COLUMN
  source: metric_implementation.flipkart.collection_fee_detail
  target: column.commission.charged_amount
  fields:
    edge_family: metric_understanding
    evidence_basis: metric_implementation.fields.source_columns
    confidence: high
    canonical_cognee_edge: true
    marketplace_only: true
    canonical_edge_type: USES_COLUMN
    legacy_edge_aliases:
    - implementation_uses_column
    inverse_edge_type: USED_BY_IMPLEMENTATION
    materialize_inverse: false
    edge_class: canonical
    source_type: metric_implementation
    target_type: column
```

```yaml
candidate_edge:
  edge_id: edge.metric_implementation.flipkart.collection_fee_detail.uses_column.column.commission.description
  edge_type: USES_COLUMN
  source: metric_implementation.flipkart.collection_fee_detail
  target: column.commission.description
  fields:
    edge_family: metric_understanding
    evidence_basis: metric_implementation.fields.source_columns
    confidence: high
    canonical_cognee_edge: true
    marketplace_only: true
    canonical_edge_type: USES_COLUMN
    legacy_edge_aliases:
    - implementation_uses_column
    inverse_edge_type: USED_BY_IMPLEMENTATION
    materialize_inverse: false
    edge_class: canonical
    source_type: metric_implementation
    target_type: column
```

```yaml
candidate_edge:
  edge_id: edge.metric_implementation.flipkart.collection_fee_detail.uses_formula_template.formula.flipkart.total_fee_detail
  edge_type: USES_FORMULA_TEMPLATE
  source: metric_implementation.flipkart.collection_fee_detail
  target: formula.flipkart.total_fee_detail
  fields:
    edge_family: metric_understanding
    evidence_basis: deterministic formula/name mapping
    confidence: high
    canonical_cognee_edge: true
    marketplace_only: true
    canonical_edge_type: USES_FORMULA_TEMPLATE
    inverse_edge_type: USED_BY_IMPLEMENTATION
    materialize_inverse: false
    edge_class: canonical
    source_type: metric_implementation
    target_type: formula_template
```

```yaml
candidate_edge:
  edge_id: edge.metric.net_cashback.has_implementation.metric_implementation.flipkart.net_cashback
  edge_type: HAS_IMPLEMENTATION
  source: metric.net_cashback
  target: metric_implementation.flipkart.net_cashback
  fields:
    edge_family: metric_understanding
    evidence_basis: metric_implementation.fields.metric_id
    confidence: high
    canonical_cognee_edge: true
    marketplace_only: true
    canonical_edge_type: HAS_IMPLEMENTATION
    inverse_edge_type: IMPLEMENTS_METRIC
    materialize_inverse: true
    edge_class: canonical
    source_type: metric
    target_type: metric_implementation
```

```yaml
candidate_edge:
  edge_id: edge.metric_implementation.flipkart.net_cashback.implements_metric.metric.net_cashback
  edge_type: IMPLEMENTS_METRIC
  source: metric_implementation.flipkart.net_cashback
  target: metric.net_cashback
  fields:
    edge_family: metric_understanding
    evidence_basis: metric_implementation.fields.metric_id
    confidence: high
    canonical_cognee_edge: true
    marketplace_only: true
    canonical_edge_type: IMPLEMENTS_METRIC
    legacy_edge_aliases:
    - implements_metric
    inverse_edge_type: HAS_IMPLEMENTATION
    materialize_inverse: true
    edge_class: canonical
    source_type: metric_implementation
    target_type: metric
```

```yaml
candidate_edge:
  edge_id: edge.metric_implementation.flipkart.net_cashback.uses_table.table.flipkart.cashback
  edge_type: USES_TABLE
  source: metric_implementation.flipkart.net_cashback
  target: table.flipkart.cashback
  fields:
    edge_family: metric_understanding
    evidence_basis: metric_implementation.fields.source_table
    confidence: high
    canonical_cognee_edge: true
    marketplace_only: true
    canonical_edge_type: USES_TABLE
    legacy_edge_aliases:
    - implementation_uses_table
    inverse_edge_type: USED_BY_IMPLEMENTATION
    materialize_inverse: false
    edge_class: canonical
    source_type: metric_implementation
    target_type: table
```

```yaml
candidate_edge:
  edge_id: edge.metric_implementation.flipkart.net_cashback.uses_column.column.cashback.charged_amount
  edge_type: USES_COLUMN
  source: metric_implementation.flipkart.net_cashback
  target: column.cashback.charged_amount
  fields:
    edge_family: metric_understanding
    evidence_basis: metric_implementation.fields.source_columns
    confidence: high
    canonical_cognee_edge: true
    marketplace_only: true
    canonical_edge_type: USES_COLUMN
    legacy_edge_aliases:
    - implementation_uses_column
    inverse_edge_type: USED_BY_IMPLEMENTATION
    materialize_inverse: false
    edge_class: canonical
    source_type: metric_implementation
    target_type: column
```

```yaml
candidate_edge:
  edge_id: edge.metric_implementation.flipkart.net_cashback.uses_formula_template.formula.flipkart.net_cashback
  edge_type: USES_FORMULA_TEMPLATE
  source: metric_implementation.flipkart.net_cashback
  target: formula.flipkart.net_cashback
  fields:
    edge_family: metric_understanding
    evidence_basis: deterministic formula/name mapping
    confidence: high
    canonical_cognee_edge: true
    marketplace_only: true
    canonical_edge_type: USES_FORMULA_TEMPLATE
    inverse_edge_type: USED_BY_IMPLEMENTATION
    materialize_inverse: false
    edge_class: canonical
    source_type: metric_implementation
    target_type: formula_template
```

```yaml
candidate_edge:
  edge_id: edge.metric.cashback_rate.has_implementation.metric_implementation.flipkart.cashback_rate
  edge_type: HAS_IMPLEMENTATION
  source: metric.cashback_rate
  target: metric_implementation.flipkart.cashback_rate
  fields:
    edge_family: metric_understanding
    evidence_basis: metric_implementation.fields.metric_id
    confidence: high
    canonical_cognee_edge: true
    marketplace_only: true
    canonical_edge_type: HAS_IMPLEMENTATION
    inverse_edge_type: IMPLEMENTS_METRIC
    materialize_inverse: true
    edge_class: canonical
    source_type: metric
    target_type: metric_implementation
```

```yaml
candidate_edge:
  edge_id: edge.metric_implementation.flipkart.cashback_rate.implements_metric.metric.cashback_rate
  edge_type: IMPLEMENTS_METRIC
  source: metric_implementation.flipkart.cashback_rate
  target: metric.cashback_rate
  fields:
    edge_family: metric_understanding
    evidence_basis: metric_implementation.fields.metric_id
    confidence: high
    canonical_cognee_edge: true
    marketplace_only: true
    canonical_edge_type: IMPLEMENTS_METRIC
    legacy_edge_aliases:
    - implements_metric
    inverse_edge_type: HAS_IMPLEMENTATION
    materialize_inverse: true
    edge_class: canonical
    source_type: metric_implementation
    target_type: metric
```

```yaml
candidate_edge:
  edge_id: edge.metric_implementation.flipkart.cashback_rate.uses_table.table.flipkart.cashback
  edge_type: USES_TABLE
  source: metric_implementation.flipkart.cashback_rate
  target: table.flipkart.cashback
  fields:
    edge_family: metric_understanding
    evidence_basis: metric_implementation.fields.source_table
    confidence: high
    canonical_cognee_edge: true
    marketplace_only: true
    canonical_edge_type: USES_TABLE
    legacy_edge_aliases:
    - implementation_uses_table
    inverse_edge_type: USED_BY_IMPLEMENTATION
    materialize_inverse: false
    edge_class: canonical
    source_type: metric_implementation
    target_type: table
```

```yaml
candidate_edge:
  edge_id: edge.metric_implementation.flipkart.cashback_rate.uses_table.table.flipkart.oms
  edge_type: USES_TABLE
  source: metric_implementation.flipkart.cashback_rate
  target: table.flipkart.oms
  fields:
    edge_family: metric_understanding
    evidence_basis: metric_implementation.fields.source_table
    confidence: high
    canonical_cognee_edge: true
    marketplace_only: true
    canonical_edge_type: USES_TABLE
    legacy_edge_aliases:
    - implementation_uses_table
    inverse_edge_type: USED_BY_IMPLEMENTATION
    materialize_inverse: false
    edge_class: canonical
    source_type: metric_implementation
    target_type: table
```

```yaml
candidate_edge:
  edge_id: edge.metric.settlement_cycle_days.has_implementation.metric_implementation.flipkart.settlement_cycle_days
  edge_type: HAS_IMPLEMENTATION
  source: metric.settlement_cycle_days
  target: metric_implementation.flipkart.settlement_cycle_days
  fields:
    edge_family: metric_understanding
    evidence_basis: metric_implementation.fields.metric_id
    confidence: high
    canonical_cognee_edge: true
    marketplace_only: true
    canonical_edge_type: HAS_IMPLEMENTATION
    inverse_edge_type: IMPLEMENTS_METRIC
    materialize_inverse: true
    edge_class: canonical
    source_type: metric
    target_type: metric_implementation
```

```yaml
candidate_edge:
  edge_id: edge.metric_implementation.flipkart.settlement_cycle_days.implements_metric.metric.settlement_cycle_days
  edge_type: IMPLEMENTS_METRIC
  source: metric_implementation.flipkart.settlement_cycle_days
  target: metric.settlement_cycle_days
  fields:
    edge_family: metric_understanding
    evidence_basis: metric_implementation.fields.metric_id
    confidence: high
    canonical_cognee_edge: true
    marketplace_only: true
    canonical_edge_type: IMPLEMENTS_METRIC
    legacy_edge_aliases:
    - implements_metric
    inverse_edge_type: HAS_IMPLEMENTATION
    materialize_inverse: true
    edge_class: canonical
    source_type: metric_implementation
    target_type: metric
```

```yaml
candidate_edge:
  edge_id: edge.metric_implementation.flipkart.settlement_cycle_days.uses_table.table.flipkart.settlement
  edge_type: USES_TABLE
  source: metric_implementation.flipkart.settlement_cycle_days
  target: table.flipkart.settlement
  fields:
    edge_family: metric_understanding
    evidence_basis: metric_implementation.fields.source_table
    confidence: high
    canonical_cognee_edge: true
    marketplace_only: true
    canonical_edge_type: USES_TABLE
    legacy_edge_aliases:
    - implementation_uses_table
    inverse_edge_type: USED_BY_IMPLEMENTATION
    materialize_inverse: false
    edge_class: canonical
    source_type: metric_implementation
    target_type: table
```

```yaml
candidate_edge:
  edge_id: edge.metric_implementation.flipkart.settlement_cycle_days.uses_column.column.settlement.created_date
  edge_type: USES_COLUMN
  source: metric_implementation.flipkart.settlement_cycle_days
  target: column.settlement.created_date
  fields:
    edge_family: metric_understanding
    evidence_basis: metric_implementation.fields.source_columns
    confidence: high
    canonical_cognee_edge: true
    marketplace_only: true
    canonical_edge_type: USES_COLUMN
    legacy_edge_aliases:
    - implementation_uses_column
    inverse_edge_type: USED_BY_IMPLEMENTATION
    materialize_inverse: false
    edge_class: canonical
    source_type: metric_implementation
    target_type: column
```

```yaml
candidate_edge:
  edge_id: edge.metric_implementation.flipkart.settlement_cycle_days.uses_column.column.settlement.settlement_date
  edge_type: USES_COLUMN
  source: metric_implementation.flipkart.settlement_cycle_days
  target: column.settlement.settlement_date
  fields:
    edge_family: metric_understanding
    evidence_basis: metric_implementation.fields.source_columns
    confidence: high
    canonical_cognee_edge: true
    marketplace_only: true
    canonical_edge_type: USES_COLUMN
    legacy_edge_aliases:
    - implementation_uses_column
    inverse_edge_type: USED_BY_IMPLEMENTATION
    materialize_inverse: false
    edge_class: canonical
    source_type: metric_implementation
    target_type: column
```

```yaml
candidate_edge:
  edge_id: edge.metric_implementation.flipkart.settlement_cycle_days.uses_formula_template.formula.flipkart.settlement_cycle_days
  edge_type: USES_FORMULA_TEMPLATE
  source: metric_implementation.flipkart.settlement_cycle_days
  target: formula.flipkart.settlement_cycle_days
  fields:
    edge_family: metric_understanding
    evidence_basis: deterministic formula/name mapping
    confidence: high
    canonical_cognee_edge: true
    marketplace_only: true
    canonical_edge_type: USES_FORMULA_TEMPLATE
    inverse_edge_type: USED_BY_IMPLEMENTATION
    materialize_inverse: false
    edge_class: canonical
    source_type: metric_implementation
    target_type: formula_template
```

```yaml
candidate_edge:
  edge_id: edge.metric.tcs_deducted.has_implementation.metric_implementation.flipkart.tcs_deducted
  edge_type: HAS_IMPLEMENTATION
  source: metric.tcs_deducted
  target: metric_implementation.flipkart.tcs_deducted
  fields:
    edge_family: metric_understanding
    evidence_basis: metric_implementation.fields.metric_id
    confidence: high
    canonical_cognee_edge: true
    marketplace_only: true
    canonical_edge_type: HAS_IMPLEMENTATION
    inverse_edge_type: IMPLEMENTS_METRIC
    materialize_inverse: true
    edge_class: canonical
    source_type: metric
    target_type: metric_implementation
```

```yaml
candidate_edge:
  edge_id: edge.metric_implementation.flipkart.tcs_deducted.implements_metric.metric.tcs_deducted
  edge_type: IMPLEMENTS_METRIC
  source: metric_implementation.flipkart.tcs_deducted
  target: metric.tcs_deducted
  fields:
    edge_family: metric_understanding
    evidence_basis: metric_implementation.fields.metric_id
    confidence: high
    canonical_cognee_edge: true
    marketplace_only: true
    canonical_edge_type: IMPLEMENTS_METRIC
    legacy_edge_aliases:
    - implements_metric
    inverse_edge_type: HAS_IMPLEMENTATION
    materialize_inverse: true
    edge_class: canonical
    source_type: metric_implementation
    target_type: metric
```

```yaml
candidate_edge:
  edge_id: edge.metric_implementation.flipkart.tcs_deducted.uses_table.table.flipkart.settlement
  edge_type: USES_TABLE
  source: metric_implementation.flipkart.tcs_deducted
  target: table.flipkart.settlement
  fields:
    edge_family: metric_understanding
    evidence_basis: metric_implementation.fields.source_table
    confidence: high
    canonical_cognee_edge: true
    marketplace_only: true
    canonical_edge_type: USES_TABLE
    legacy_edge_aliases:
    - implementation_uses_table
    inverse_edge_type: USED_BY_IMPLEMENTATION
    materialize_inverse: false
    edge_class: canonical
    source_type: metric_implementation
    target_type: table
```

```yaml
candidate_edge:
  edge_id: edge.metric_implementation.flipkart.tcs_deducted.uses_column.column.settlement.total_tcs_amount
  edge_type: USES_COLUMN
  source: metric_implementation.flipkart.tcs_deducted
  target: column.settlement.total_tcs_amount
  fields:
    edge_family: metric_understanding
    evidence_basis: metric_implementation.fields.source_columns
    confidence: high
    canonical_cognee_edge: true
    marketplace_only: true
    canonical_edge_type: USES_COLUMN
    legacy_edge_aliases:
    - implementation_uses_column
    inverse_edge_type: USED_BY_IMPLEMENTATION
    materialize_inverse: false
    edge_class: canonical
    source_type: metric_implementation
    target_type: column
```

```yaml
candidate_edge:
  edge_id: edge.metric.tds_deducted.has_implementation.metric_implementation.flipkart.tds_deducted
  edge_type: HAS_IMPLEMENTATION
  source: metric.tds_deducted
  target: metric_implementation.flipkart.tds_deducted
  fields:
    edge_family: metric_understanding
    evidence_basis: metric_implementation.fields.metric_id
    confidence: high
    canonical_cognee_edge: true
    marketplace_only: true
    canonical_edge_type: HAS_IMPLEMENTATION
    inverse_edge_type: IMPLEMENTS_METRIC
    materialize_inverse: true
    edge_class: canonical
    source_type: metric
    target_type: metric_implementation
```

```yaml
candidate_edge:
  edge_id: edge.metric_implementation.flipkart.tds_deducted.implements_metric.metric.tds_deducted
  edge_type: IMPLEMENTS_METRIC
  source: metric_implementation.flipkart.tds_deducted
  target: metric.tds_deducted
  fields:
    edge_family: metric_understanding
    evidence_basis: metric_implementation.fields.metric_id
    confidence: high
    canonical_cognee_edge: true
    marketplace_only: true
    canonical_edge_type: IMPLEMENTS_METRIC
    legacy_edge_aliases:
    - implements_metric
    inverse_edge_type: HAS_IMPLEMENTATION
    materialize_inverse: true
    edge_class: canonical
    source_type: metric_implementation
    target_type: metric
```

```yaml
candidate_edge:
  edge_id: edge.metric_implementation.flipkart.tds_deducted.uses_table.table.flipkart.settlement
  edge_type: USES_TABLE
  source: metric_implementation.flipkart.tds_deducted
  target: table.flipkart.settlement
  fields:
    edge_family: metric_understanding
    evidence_basis: metric_implementation.fields.source_table
    confidence: high
    canonical_cognee_edge: true
    marketplace_only: true
    canonical_edge_type: USES_TABLE
    legacy_edge_aliases:
    - implementation_uses_table
    inverse_edge_type: USED_BY_IMPLEMENTATION
    materialize_inverse: false
    edge_class: canonical
    source_type: metric_implementation
    target_type: table
```

```yaml
candidate_edge:
  edge_id: edge.metric_implementation.flipkart.tds_deducted.uses_column.column.settlement.total_tds_amount
  edge_type: USES_COLUMN
  source: metric_implementation.flipkart.tds_deducted
  target: column.settlement.total_tds_amount
  fields:
    edge_family: metric_understanding
    evidence_basis: metric_implementation.fields.source_columns
    confidence: high
    canonical_cognee_edge: true
    marketplace_only: true
    canonical_edge_type: USES_COLUMN
    legacy_edge_aliases:
    - implementation_uses_column
    inverse_edge_type: USED_BY_IMPLEMENTATION
    materialize_inverse: false
    edge_class: canonical
    source_type: metric_implementation
    target_type: column
```

```yaml
candidate_edge:
  edge_id: edge.metric.gst_on_marketplace_fees.has_implementation.metric_implementation.flipkart.gst_on_mp_fees
  edge_type: HAS_IMPLEMENTATION
  source: metric.gst_on_marketplace_fees
  target: metric_implementation.flipkart.gst_on_mp_fees
  fields:
    edge_family: metric_understanding
    evidence_basis: metric_implementation.fields.metric_id
    confidence: high
    canonical_cognee_edge: true
    marketplace_only: true
    canonical_edge_type: HAS_IMPLEMENTATION
    inverse_edge_type: IMPLEMENTS_METRIC
    materialize_inverse: true
    edge_class: canonical
    source_type: metric
    target_type: metric_implementation
```

```yaml
candidate_edge:
  edge_id: edge.metric_implementation.flipkart.gst_on_mp_fees.implements_metric.metric.gst_on_marketplace_fees
  edge_type: IMPLEMENTS_METRIC
  source: metric_implementation.flipkart.gst_on_mp_fees
  target: metric.gst_on_marketplace_fees
  fields:
    edge_family: metric_understanding
    evidence_basis: metric_implementation.fields.metric_id
    confidence: high
    canonical_cognee_edge: true
    marketplace_only: true
    canonical_edge_type: IMPLEMENTS_METRIC
    legacy_edge_aliases:
    - implements_metric
    inverse_edge_type: HAS_IMPLEMENTATION
    materialize_inverse: true
    edge_class: canonical
    source_type: metric_implementation
    target_type: metric
```

```yaml
candidate_edge:
  edge_id: edge.metric_implementation.flipkart.gst_on_mp_fees.uses_table.table.flipkart.settlement
  edge_type: USES_TABLE
  source: metric_implementation.flipkart.gst_on_mp_fees
  target: table.flipkart.settlement
  fields:
    edge_family: metric_understanding
    evidence_basis: metric_implementation.fields.source_table
    confidence: high
    canonical_cognee_edge: true
    marketplace_only: true
    canonical_edge_type: USES_TABLE
    legacy_edge_aliases:
    - implementation_uses_table
    inverse_edge_type: USED_BY_IMPLEMENTATION
    materialize_inverse: false
    edge_class: canonical
    source_type: metric_implementation
    target_type: table
```

```yaml
candidate_edge:
  edge_id: edge.metric_implementation.flipkart.gst_on_mp_fees.uses_column.column.settlement.gst_on_mp_fees
  edge_type: USES_COLUMN
  source: metric_implementation.flipkart.gst_on_mp_fees
  target: column.settlement.gst_on_mp_fees
  fields:
    edge_family: metric_understanding
    evidence_basis: metric_implementation.fields.source_columns
    confidence: high
    canonical_cognee_edge: true
    marketplace_only: true
    canonical_edge_type: USES_COLUMN
    legacy_edge_aliases:
    - implementation_uses_column
    inverse_edge_type: USED_BY_IMPLEMENTATION
    materialize_inverse: false
    edge_class: canonical
    source_type: metric_implementation
    target_type: column
```

```yaml
candidate_edge:
  edge_id: edge.metric.gst_on_marketplace_fees.has_implementation.metric_implementation.flipkart.fee_tax_detail
  edge_type: HAS_IMPLEMENTATION
  source: metric.gst_on_marketplace_fees
  target: metric_implementation.flipkart.fee_tax_detail
  fields:
    edge_family: metric_understanding
    evidence_basis: metric_implementation.fields.metric_id
    confidence: high
    canonical_cognee_edge: true
    marketplace_only: true
    canonical_edge_type: HAS_IMPLEMENTATION
    inverse_edge_type: IMPLEMENTS_METRIC
    materialize_inverse: true
    edge_class: canonical
    source_type: metric
    target_type: metric_implementation
```

```yaml
candidate_edge:
  edge_id: edge.metric_implementation.flipkart.fee_tax_detail.implements_metric.metric.gst_on_marketplace_fees
  edge_type: IMPLEMENTS_METRIC
  source: metric_implementation.flipkart.fee_tax_detail
  target: metric.gst_on_marketplace_fees
  fields:
    edge_family: metric_understanding
    evidence_basis: metric_implementation.fields.metric_id
    confidence: high
    canonical_cognee_edge: true
    marketplace_only: true
    canonical_edge_type: IMPLEMENTS_METRIC
    legacy_edge_aliases:
    - implements_metric
    inverse_edge_type: HAS_IMPLEMENTATION
    materialize_inverse: true
    edge_class: canonical
    source_type: metric_implementation
    target_type: metric
```

```yaml
candidate_edge:
  edge_id: edge.metric_implementation.flipkart.fee_tax_detail.uses_table.table.flipkart.commission
  edge_type: USES_TABLE
  source: metric_implementation.flipkart.fee_tax_detail
  target: table.flipkart.commission
  fields:
    edge_family: metric_understanding
    evidence_basis: metric_implementation.fields.source_table
    confidence: high
    canonical_cognee_edge: true
    marketplace_only: true
    canonical_edge_type: USES_TABLE
    legacy_edge_aliases:
    - implementation_uses_table
    inverse_edge_type: USED_BY_IMPLEMENTATION
    materialize_inverse: false
    edge_class: canonical
    source_type: metric_implementation
    target_type: table
```

```yaml
candidate_edge:
  edge_id: edge.metric_implementation.flipkart.fee_tax_detail.uses_column.column.commission.total_tax
  edge_type: USES_COLUMN
  source: metric_implementation.flipkart.fee_tax_detail
  target: column.commission.total_tax
  fields:
    edge_family: metric_understanding
    evidence_basis: metric_implementation.fields.source_columns
    confidence: high
    canonical_cognee_edge: true
    marketplace_only: true
    canonical_edge_type: USES_COLUMN
    legacy_edge_aliases:
    - implementation_uses_column
    inverse_edge_type: USED_BY_IMPLEMENTATION
    materialize_inverse: false
    edge_class: canonical
    source_type: metric_implementation
    target_type: column
```

```yaml
candidate_edge:
  edge_id: edge.metric.return_rate.has_implementation.metric_implementation.flipkart.return_rate
  edge_type: HAS_IMPLEMENTATION
  source: metric.return_rate
  target: metric_implementation.flipkart.return_rate
  fields:
    edge_family: metric_understanding
    evidence_basis: metric_implementation.fields.metric_id
    confidence: high
    canonical_cognee_edge: true
    marketplace_only: true
    canonical_edge_type: HAS_IMPLEMENTATION
    inverse_edge_type: IMPLEMENTS_METRIC
    materialize_inverse: true
    edge_class: canonical
    source_type: metric
    target_type: metric_implementation
```

```yaml
candidate_edge:
  edge_id: edge.metric_implementation.flipkart.return_rate.implements_metric.metric.return_rate
  edge_type: IMPLEMENTS_METRIC
  source: metric_implementation.flipkart.return_rate
  target: metric.return_rate
  fields:
    edge_family: metric_understanding
    evidence_basis: metric_implementation.fields.metric_id
    confidence: high
    canonical_cognee_edge: true
    marketplace_only: true
    canonical_edge_type: IMPLEMENTS_METRIC
    legacy_edge_aliases:
    - implements_metric
    inverse_edge_type: HAS_IMPLEMENTATION
    materialize_inverse: true
    edge_class: canonical
    source_type: metric_implementation
    target_type: metric
```

```yaml
candidate_edge:
  edge_id: edge.metric_implementation.flipkart.return_rate.uses_table.table.flipkart.settlement
  edge_type: USES_TABLE
  source: metric_implementation.flipkart.return_rate
  target: table.flipkart.settlement
  fields:
    edge_family: metric_understanding
    evidence_basis: metric_implementation.fields.source_table
    confidence: high
    canonical_cognee_edge: true
    marketplace_only: true
    canonical_edge_type: USES_TABLE
    legacy_edge_aliases:
    - implementation_uses_table
    inverse_edge_type: USED_BY_IMPLEMENTATION
    materialize_inverse: false
    edge_class: canonical
    source_type: metric_implementation
    target_type: table
```

```yaml
candidate_edge:
  edge_id: edge.metric_implementation.flipkart.return_rate.uses_column.column.settlement.return_type
  edge_type: USES_COLUMN
  source: metric_implementation.flipkart.return_rate
  target: column.settlement.return_type
  fields:
    edge_family: metric_understanding
    evidence_basis: metric_implementation.fields.source_columns
    confidence: high
    canonical_cognee_edge: true
    marketplace_only: true
    canonical_edge_type: USES_COLUMN
    legacy_edge_aliases:
    - implementation_uses_column
    inverse_edge_type: USED_BY_IMPLEMENTATION
    materialize_inverse: false
    edge_class: canonical
    source_type: metric_implementation
    target_type: column
```

```yaml
candidate_edge:
  edge_id: edge.metric_implementation.flipkart.return_rate.uses_column.column.settlement.order_id
  edge_type: USES_COLUMN
  source: metric_implementation.flipkart.return_rate
  target: column.settlement.order_id
  fields:
    edge_family: metric_understanding
    evidence_basis: metric_implementation.fields.source_columns
    confidence: high
    canonical_cognee_edge: true
    marketplace_only: true
    canonical_edge_type: USES_COLUMN
    legacy_edge_aliases:
    - implementation_uses_column
    inverse_edge_type: USED_BY_IMPLEMENTATION
    materialize_inverse: false
    edge_class: canonical
    source_type: metric_implementation
    target_type: column
```

```yaml
candidate_edge:
  edge_id: edge.metric.cancellation_rate.has_implementation.metric_implementation.flipkart.cancellation_rate
  edge_type: HAS_IMPLEMENTATION
  source: metric.cancellation_rate
  target: metric_implementation.flipkart.cancellation_rate
  fields:
    edge_family: metric_understanding
    evidence_basis: metric_implementation.fields.metric_id
    confidence: high
    canonical_cognee_edge: true
    marketplace_only: true
    canonical_edge_type: HAS_IMPLEMENTATION
    inverse_edge_type: IMPLEMENTS_METRIC
    materialize_inverse: true
    edge_class: canonical
    source_type: metric
    target_type: metric_implementation
```

```yaml
candidate_edge:
  edge_id: edge.metric_implementation.flipkart.cancellation_rate.implements_metric.metric.cancellation_rate
  edge_type: IMPLEMENTS_METRIC
  source: metric_implementation.flipkart.cancellation_rate
  target: metric.cancellation_rate
  fields:
    edge_family: metric_understanding
    evidence_basis: metric_implementation.fields.metric_id
    confidence: high
    canonical_cognee_edge: true
    marketplace_only: true
    canonical_edge_type: IMPLEMENTS_METRIC
    legacy_edge_aliases:
    - implements_metric
    inverse_edge_type: HAS_IMPLEMENTATION
    materialize_inverse: true
    edge_class: canonical
    source_type: metric_implementation
    target_type: metric
```

```yaml
candidate_edge:
  edge_id: edge.metric_implementation.flipkart.cancellation_rate.uses_table.table.flipkart.cashback
  edge_type: USES_TABLE
  source: metric_implementation.flipkart.cancellation_rate
  target: table.flipkart.cashback
  fields:
    edge_family: metric_understanding
    evidence_basis: metric_implementation.fields.source_table
    confidence: high
    canonical_cognee_edge: true
    marketplace_only: true
    canonical_edge_type: USES_TABLE
    legacy_edge_aliases:
    - implementation_uses_table
    inverse_edge_type: USED_BY_IMPLEMENTATION
    materialize_inverse: false
    edge_class: canonical
    source_type: metric_implementation
    target_type: table
```

```yaml
candidate_edge:
  edge_id: edge.metric_implementation.flipkart.cancellation_rate.uses_column.column.cashback.document_sub_type
  edge_type: USES_COLUMN
  source: metric_implementation.flipkart.cancellation_rate
  target: column.cashback.document_sub_type
  fields:
    edge_family: metric_understanding
    evidence_basis: metric_implementation.fields.source_columns
    confidence: high
    canonical_cognee_edge: true
    marketplace_only: true
    canonical_edge_type: USES_COLUMN
    legacy_edge_aliases:
    - implementation_uses_column
    inverse_edge_type: USED_BY_IMPLEMENTATION
    materialize_inverse: false
    edge_class: canonical
    source_type: metric_implementation
    target_type: column
```

```yaml
candidate_edge:
  edge_id: edge.metric_implementation.flipkart.cancellation_rate.uses_column.column.cashback.order_id
  edge_type: USES_COLUMN
  source: metric_implementation.flipkart.cancellation_rate
  target: column.cashback.order_id
  fields:
    edge_family: metric_understanding
    evidence_basis: metric_implementation.fields.source_columns
    confidence: high
    canonical_cognee_edge: true
    marketplace_only: true
    canonical_edge_type: USES_COLUMN
    legacy_edge_aliases:
    - implementation_uses_column
    inverse_edge_type: USED_BY_IMPLEMENTATION
    materialize_inverse: false
    edge_class: canonical
    source_type: metric_implementation
    target_type: column
```

```yaml
candidate_edge:
  edge_id: edge.metric.protection_fund_settlement.has_implementation.metric_implementation.flipkart.protection_fund
  edge_type: HAS_IMPLEMENTATION
  source: metric.protection_fund_settlement
  target: metric_implementation.flipkart.protection_fund
  fields:
    edge_family: metric_understanding
    evidence_basis: metric_implementation.fields.metric_id
    confidence: high
    canonical_cognee_edge: true
    marketplace_only: true
    canonical_edge_type: HAS_IMPLEMENTATION
    inverse_edge_type: IMPLEMENTS_METRIC
    materialize_inverse: true
    edge_class: canonical
    source_type: metric
    target_type: metric_implementation
```

```yaml
candidate_edge:
  edge_id: edge.metric_implementation.flipkart.protection_fund.implements_metric.metric.protection_fund_settlement
  edge_type: IMPLEMENTS_METRIC
  source: metric_implementation.flipkart.protection_fund
  target: metric.protection_fund_settlement
  fields:
    edge_family: metric_understanding
    evidence_basis: metric_implementation.fields.metric_id
    confidence: high
    canonical_cognee_edge: true
    marketplace_only: true
    canonical_edge_type: IMPLEMENTS_METRIC
    legacy_edge_aliases:
    - implements_metric
    inverse_edge_type: HAS_IMPLEMENTATION
    materialize_inverse: true
    edge_class: canonical
    source_type: metric_implementation
    target_type: metric
```

```yaml
candidate_edge:
  edge_id: edge.metric_implementation.flipkart.protection_fund.uses_table.table.flipkart.settlement
  edge_type: USES_TABLE
  source: metric_implementation.flipkart.protection_fund
  target: table.flipkart.settlement
  fields:
    edge_family: metric_understanding
    evidence_basis: metric_implementation.fields.source_table
    confidence: high
    canonical_cognee_edge: true
    marketplace_only: true
    canonical_edge_type: USES_TABLE
    legacy_edge_aliases:
    - implementation_uses_table
    inverse_edge_type: USED_BY_IMPLEMENTATION
    materialize_inverse: false
    edge_class: canonical
    source_type: metric_implementation
    target_type: table
```

```yaml
candidate_edge:
  edge_id: edge.metric_implementation.flipkart.protection_fund.uses_column.column.settlement.protection_fund_settled_amount
  edge_type: USES_COLUMN
  source: metric_implementation.flipkart.protection_fund
  target: column.settlement.protection_fund_settled_amount
  fields:
    edge_family: metric_understanding
    evidence_basis: metric_implementation.fields.source_columns
    confidence: high
    canonical_cognee_edge: true
    marketplace_only: true
    canonical_edge_type: USES_COLUMN
    legacy_edge_aliases:
    - implementation_uses_column
    inverse_edge_type: USED_BY_IMPLEMENTATION
    materialize_inverse: false
    edge_class: canonical
    source_type: metric_implementation
    target_type: column
```

```yaml
candidate_edge:
  edge_id: edge.metric_dependency.flipkart.realization.depends_on.settlement.parent_metric.metric.realization_rate
  edge_type: PARENT_METRIC
  source: metric_dependency.flipkart.realization.depends_on.settlement
  target: metric.realization_rate
  fields:
    edge_family: metric_understanding
    evidence_basis: metric_dependency.fields.metric_id
    confidence: high
    canonical_cognee_edge: true
    marketplace_only: true
    canonical_edge_type: PARENT_METRIC
    inverse_edge_type: HAS_METRIC_DEPENDENCY
    materialize_inverse: false
    edge_class: canonical
    source_type: metric_dependency
    target_type: metric
```

```yaml
candidate_edge:
  edge_id: edge.metric.realization_rate.depends_on_metric.metric.net_settlement
  edge_type: DEPENDS_ON_METRIC
  source: metric.realization_rate
  target: metric.net_settlement
  fields:
    edge_family: metric_understanding
    evidence_basis: metric_dependency.fields.depends_on
    confidence: high
    canonical_cognee_edge: true
    marketplace_only: true
    canonical_edge_type: DEPENDS_ON_METRIC
    legacy_edge_aliases:
    - metric_depends_on_metric
    inverse_edge_type: DEPENDENCY_OF_METRIC
    materialize_inverse: false
    edge_class: canonical
    source_type: metric
    target_type: metric
```

```yaml
candidate_edge:
  edge_id: edge.metric_dependency.flipkart.realization.depends_on.settlement.uses_dependent_metric.metric.net_settlement
  edge_type: USES_DEPENDENT_METRIC
  source: metric_dependency.flipkart.realization.depends_on.settlement
  target: metric.net_settlement
  fields:
    edge_family: metric_understanding
    evidence_basis: metric_dependency.fields.depends_on
    confidence: high
    canonical_cognee_edge: true
    marketplace_only: true
    canonical_edge_type: USES_DEPENDENT_METRIC
    inverse_edge_type: DEPENDENCY_USED_BY
    materialize_inverse: false
    edge_class: canonical
    source_type: metric_dependency
    target_type: metric
```

```yaml
candidate_edge:
  edge_id: edge.metric.realization_rate.depends_on_metric.metric.gross_merchandise_value
  edge_type: DEPENDS_ON_METRIC
  source: metric.realization_rate
  target: metric.gross_merchandise_value
  fields:
    edge_family: metric_understanding
    evidence_basis: metric_dependency.fields.depends_on
    confidence: high
    canonical_cognee_edge: true
    marketplace_only: true
    canonical_edge_type: DEPENDS_ON_METRIC
    legacy_edge_aliases:
    - metric_depends_on_metric
    inverse_edge_type: DEPENDENCY_OF_METRIC
    materialize_inverse: false
    edge_class: canonical
    source_type: metric
    target_type: metric
```

```yaml
candidate_edge:
  edge_id: edge.metric_dependency.flipkart.realization.depends_on.settlement.uses_dependent_metric.metric.gross_merchandise_value
  edge_type: USES_DEPENDENT_METRIC
  source: metric_dependency.flipkart.realization.depends_on.settlement
  target: metric.gross_merchandise_value
  fields:
    edge_family: metric_understanding
    evidence_basis: metric_dependency.fields.depends_on
    confidence: high
    canonical_cognee_edge: true
    marketplace_only: true
    canonical_edge_type: USES_DEPENDENT_METRIC
    inverse_edge_type: DEPENDENCY_USED_BY
    materialize_inverse: false
    edge_class: canonical
    source_type: metric_dependency
    target_type: metric
```

```yaml
candidate_edge:
  edge_id: edge.metric_dependency.flipkart.fee_rate.depends_on.fees_sales.parent_metric.metric.effective_fee_rate
  edge_type: PARENT_METRIC
  source: metric_dependency.flipkart.fee_rate.depends_on.fees_sales
  target: metric.effective_fee_rate
  fields:
    edge_family: metric_understanding
    evidence_basis: metric_dependency.fields.metric_id
    confidence: high
    canonical_cognee_edge: true
    marketplace_only: true
    canonical_edge_type: PARENT_METRIC
    inverse_edge_type: HAS_METRIC_DEPENDENCY
    materialize_inverse: false
    edge_class: canonical
    source_type: metric_dependency
    target_type: metric
```

```yaml
candidate_edge:
  edge_id: edge.metric.effective_fee_rate.depends_on_metric.metric.marketplace_fee_total
  edge_type: DEPENDS_ON_METRIC
  source: metric.effective_fee_rate
  target: metric.marketplace_fee_total
  fields:
    edge_family: metric_understanding
    evidence_basis: metric_dependency.fields.depends_on
    confidence: high
    canonical_cognee_edge: true
    marketplace_only: true
    canonical_edge_type: DEPENDS_ON_METRIC
    legacy_edge_aliases:
    - metric_depends_on_metric
    inverse_edge_type: DEPENDENCY_OF_METRIC
    materialize_inverse: false
    edge_class: canonical
    source_type: metric
    target_type: metric
```

```yaml
candidate_edge:
  edge_id: edge.metric_dependency.flipkart.fee_rate.depends_on.fees_sales.uses_dependent_metric.metric.marketplace_fee_total
  edge_type: USES_DEPENDENT_METRIC
  source: metric_dependency.flipkart.fee_rate.depends_on.fees_sales
  target: metric.marketplace_fee_total
  fields:
    edge_family: metric_understanding
    evidence_basis: metric_dependency.fields.depends_on
    confidence: high
    canonical_cognee_edge: true
    marketplace_only: true
    canonical_edge_type: USES_DEPENDENT_METRIC
    inverse_edge_type: DEPENDENCY_USED_BY
    materialize_inverse: false
    edge_class: canonical
    source_type: metric_dependency
    target_type: metric
```

```yaml
candidate_edge:
  edge_id: edge.metric.effective_fee_rate.depends_on_metric.metric.gross_merchandise_value
  edge_type: DEPENDS_ON_METRIC
  source: metric.effective_fee_rate
  target: metric.gross_merchandise_value
  fields:
    edge_family: metric_understanding
    evidence_basis: metric_dependency.fields.depends_on
    confidence: high
    canonical_cognee_edge: true
    marketplace_only: true
    canonical_edge_type: DEPENDS_ON_METRIC
    legacy_edge_aliases:
    - metric_depends_on_metric
    inverse_edge_type: DEPENDENCY_OF_METRIC
    materialize_inverse: false
    edge_class: canonical
    source_type: metric
    target_type: metric
```

```yaml
candidate_edge:
  edge_id: edge.metric_dependency.flipkart.fee_rate.depends_on.fees_sales.uses_dependent_metric.metric.gross_merchandise_value
  edge_type: USES_DEPENDENT_METRIC
  source: metric_dependency.flipkart.fee_rate.depends_on.fees_sales
  target: metric.gross_merchandise_value
  fields:
    edge_family: metric_understanding
    evidence_basis: metric_dependency.fields.depends_on
    confidence: high
    canonical_cognee_edge: true
    marketplace_only: true
    canonical_edge_type: USES_DEPENDENT_METRIC
    inverse_edge_type: DEPENDENCY_USED_BY
    materialize_inverse: false
    edge_class: canonical
    source_type: metric_dependency
    target_type: metric
```

```yaml
candidate_edge:
  edge_id: edge.metric_dependency.flipkart.cashback_rate.depends_on.cashback_sales.parent_metric.metric.cashback_rate
  edge_type: PARENT_METRIC
  source: metric_dependency.flipkart.cashback_rate.depends_on.cashback_sales
  target: metric.cashback_rate
  fields:
    edge_family: metric_understanding
    evidence_basis: metric_dependency.fields.metric_id
    confidence: high
    canonical_cognee_edge: true
    marketplace_only: true
    canonical_edge_type: PARENT_METRIC
    inverse_edge_type: HAS_METRIC_DEPENDENCY
    materialize_inverse: false
    edge_class: canonical
    source_type: metric_dependency
    target_type: metric
```

```yaml
candidate_edge:
  edge_id: edge.metric.cashback_rate.depends_on_metric.metric.net_cashback
  edge_type: DEPENDS_ON_METRIC
  source: metric.cashback_rate
  target: metric.net_cashback
  fields:
    edge_family: metric_understanding
    evidence_basis: metric_dependency.fields.depends_on
    confidence: high
    canonical_cognee_edge: true
    marketplace_only: true
    canonical_edge_type: DEPENDS_ON_METRIC
    legacy_edge_aliases:
    - metric_depends_on_metric
    inverse_edge_type: DEPENDENCY_OF_METRIC
    materialize_inverse: false
    edge_class: canonical
    source_type: metric
    target_type: metric
```

```yaml
candidate_edge:
  edge_id: edge.metric_dependency.flipkart.cashback_rate.depends_on.cashback_sales.uses_dependent_metric.metric.net_cashback
  edge_type: USES_DEPENDENT_METRIC
  source: metric_dependency.flipkart.cashback_rate.depends_on.cashback_sales
  target: metric.net_cashback
  fields:
    edge_family: metric_understanding
    evidence_basis: metric_dependency.fields.depends_on
    confidence: high
    canonical_cognee_edge: true
    marketplace_only: true
    canonical_edge_type: USES_DEPENDENT_METRIC
    inverse_edge_type: DEPENDENCY_USED_BY
    materialize_inverse: false
    edge_class: canonical
    source_type: metric_dependency
    target_type: metric
```

```yaml
candidate_edge:
  edge_id: edge.metric.cashback_rate.depends_on_metric.metric.gross_merchandise_value
  edge_type: DEPENDS_ON_METRIC
  source: metric.cashback_rate
  target: metric.gross_merchandise_value
  fields:
    edge_family: metric_understanding
    evidence_basis: metric_dependency.fields.depends_on
    confidence: high
    canonical_cognee_edge: true
    marketplace_only: true
    canonical_edge_type: DEPENDS_ON_METRIC
    legacy_edge_aliases:
    - metric_depends_on_metric
    inverse_edge_type: DEPENDENCY_OF_METRIC
    materialize_inverse: false
    edge_class: canonical
    source_type: metric
    target_type: metric
```

```yaml
candidate_edge:
  edge_id: edge.metric_dependency.flipkart.cashback_rate.depends_on.cashback_sales.uses_dependent_metric.metric.gross_merchandise_value
  edge_type: USES_DEPENDENT_METRIC
  source: metric_dependency.flipkart.cashback_rate.depends_on.cashback_sales
  target: metric.gross_merchandise_value
  fields:
    edge_family: metric_understanding
    evidence_basis: metric_dependency.fields.depends_on
    confidence: high
    canonical_cognee_edge: true
    marketplace_only: true
    canonical_edge_type: USES_DEPENDENT_METRIC
    inverse_edge_type: DEPENDENCY_USED_BY
    materialize_inverse: false
    edge_class: canonical
    source_type: metric_dependency
    target_type: metric
```

```yaml
candidate_edge:
  edge_id: edge.metric_dependency.flipkart.aov.depends_on.gmv_count.parent_metric.metric.average_order_value
  edge_type: PARENT_METRIC
  source: metric_dependency.flipkart.aov.depends_on.gmv_count
  target: metric.average_order_value
  fields:
    edge_family: metric_understanding
    evidence_basis: metric_dependency.fields.metric_id
    confidence: high
    canonical_cognee_edge: true
    marketplace_only: true
    canonical_edge_type: PARENT_METRIC
    inverse_edge_type: HAS_METRIC_DEPENDENCY
    materialize_inverse: false
    edge_class: canonical
    source_type: metric_dependency
    target_type: metric
```

```yaml
candidate_edge:
  edge_id: edge.metric.average_order_value.depends_on_metric.metric.gross_merchandise_value
  edge_type: DEPENDS_ON_METRIC
  source: metric.average_order_value
  target: metric.gross_merchandise_value
  fields:
    edge_family: metric_understanding
    evidence_basis: metric_dependency.fields.depends_on
    confidence: high
    canonical_cognee_edge: true
    marketplace_only: true
    canonical_edge_type: DEPENDS_ON_METRIC
    legacy_edge_aliases:
    - metric_depends_on_metric
    inverse_edge_type: DEPENDENCY_OF_METRIC
    materialize_inverse: false
    edge_class: canonical
    source_type: metric
    target_type: metric
```

```yaml
candidate_edge:
  edge_id: edge.metric_dependency.flipkart.aov.depends_on.gmv_count.uses_dependent_metric.metric.gross_merchandise_value
  edge_type: USES_DEPENDENT_METRIC
  source: metric_dependency.flipkart.aov.depends_on.gmv_count
  target: metric.gross_merchandise_value
  fields:
    edge_family: metric_understanding
    evidence_basis: metric_dependency.fields.depends_on
    confidence: high
    canonical_cognee_edge: true
    marketplace_only: true
    canonical_edge_type: USES_DEPENDENT_METRIC
    inverse_edge_type: DEPENDENCY_USED_BY
    materialize_inverse: false
    edge_class: canonical
    source_type: metric_dependency
    target_type: metric
```

```yaml
candidate_edge:
  edge_id: edge.metric.average_order_value.depends_on_metric.metric.order_count
  edge_type: DEPENDS_ON_METRIC
  source: metric.average_order_value
  target: metric.order_count
  fields:
    edge_family: metric_understanding
    evidence_basis: metric_dependency.fields.depends_on
    confidence: high
    canonical_cognee_edge: true
    marketplace_only: true
    canonical_edge_type: DEPENDS_ON_METRIC
    legacy_edge_aliases:
    - metric_depends_on_metric
    inverse_edge_type: DEPENDENCY_OF_METRIC
    materialize_inverse: false
    edge_class: canonical
    source_type: metric
    target_type: metric
```

```yaml
candidate_edge:
  edge_id: edge.metric_dependency.flipkart.aov.depends_on.gmv_count.uses_dependent_metric.metric.order_count
  edge_type: USES_DEPENDENT_METRIC
  source: metric_dependency.flipkart.aov.depends_on.gmv_count
  target: metric.order_count
  fields:
    edge_family: metric_understanding
    evidence_basis: metric_dependency.fields.depends_on
    confidence: high
    canonical_cognee_edge: true
    marketplace_only: true
    canonical_edge_type: USES_DEPENDENT_METRIC
    inverse_edge_type: DEPENDENCY_USED_BY
    materialize_inverse: false
    edge_class: canonical
    source_type: metric_dependency
    target_type: metric
```

```yaml
candidate_edge:
  edge_id: edge.metric_dependency.flipkart.settlement_recon.depends_on.normalization.parent_metric.metric.marketplace_fee_total
  edge_type: PARENT_METRIC
  source: metric_dependency.flipkart.settlement_recon.depends_on.normalization
  target: metric.marketplace_fee_total
  fields:
    edge_family: metric_understanding
    evidence_basis: metric_dependency.fields.metric_id
    confidence: high
    canonical_cognee_edge: true
    marketplace_only: true
    canonical_edge_type: PARENT_METRIC
    inverse_edge_type: HAS_METRIC_DEPENDENCY
    materialize_inverse: false
    edge_class: canonical
    source_type: metric_dependency
    target_type: metric
```

```yaml
candidate_edge:
  edge_id: edge.metric_dependency.flipkart.settlement_recon.depends_on.normalization.uses_formula_template.formula.flipkart.order_id_normalization
  edge_type: USES_FORMULA_TEMPLATE
  source: metric_dependency.flipkart.settlement_recon.depends_on.normalization
  target: formula.flipkart.order_id_normalization
  fields:
    edge_family: metric_understanding_derived
    evidence_basis: metric_dependency.fields.depends_on references formula template
    confidence: high
    canonical_cognee_edge: true
    marketplace_only: true
    note: Derived helper edge because MetricDependency.depends_on points at a Formula Template, while Cognee v4 canonical dependency edges target Metric cards.
    canonical_edge_type: USES_FORMULA_TEMPLATE
    inverse_edge_type: USED_BY_IMPLEMENTATION
    materialize_inverse: false
    edge_class: canonical
    source_type: metric_dependency
    target_type: formula_template
```

```yaml
candidate_edge:
  edge_id: edge.metric.gross_merchandise_value.belongs_to_domain.domain.marketplace.flipkart.orders
  edge_type: BELONGS_TO_DOMAIN
  source: metric.gross_merchandise_value
  target: domain.marketplace.flipkart.orders
  fields:
    edge_family: metric_understanding
    evidence_basis: metric.fields.metric_family
    confidence: high
    canonical_cognee_edge: true
    marketplace_only: true
    canonical_edge_type: BELONGS_TO_DOMAIN
    inverse_edge_type: HAS_METRIC
    materialize_inverse: false
    edge_class: canonical
    source_type: metric
    target_type: domain
```

```yaml
candidate_edge:
  edge_id: edge.metric.net_revenue.belongs_to_domain.domain.marketplace.flipkart.orders
  edge_type: BELONGS_TO_DOMAIN
  source: metric.net_revenue
  target: domain.marketplace.flipkart.orders
  fields:
    edge_family: metric_understanding
    evidence_basis: metric.fields.metric_family
    confidence: high
    canonical_cognee_edge: true
    marketplace_only: true
    canonical_edge_type: BELONGS_TO_DOMAIN
    inverse_edge_type: HAS_METRIC
    materialize_inverse: false
    edge_class: canonical
    source_type: metric
    target_type: domain
```

```yaml
candidate_edge:
  edge_id: edge.metric.order_count.belongs_to_domain.domain.marketplace.flipkart.orders
  edge_type: BELONGS_TO_DOMAIN
  source: metric.order_count
  target: domain.marketplace.flipkart.orders
  fields:
    edge_family: metric_understanding
    evidence_basis: metric.fields.metric_family
    confidence: high
    canonical_cognee_edge: true
    marketplace_only: true
    canonical_edge_type: BELONGS_TO_DOMAIN
    inverse_edge_type: HAS_METRIC
    materialize_inverse: false
    edge_class: canonical
    source_type: metric
    target_type: domain
```

```yaml
candidate_edge:
  edge_id: edge.metric.average_order_value.belongs_to_domain.domain.marketplace.flipkart.orders
  edge_type: BELONGS_TO_DOMAIN
  source: metric.average_order_value
  target: domain.marketplace.flipkart.orders
  fields:
    edge_family: metric_understanding
    evidence_basis: metric.fields.metric_family
    confidence: high
    canonical_cognee_edge: true
    marketplace_only: true
    canonical_edge_type: BELONGS_TO_DOMAIN
    inverse_edge_type: HAS_METRIC
    materialize_inverse: false
    edge_class: canonical
    source_type: metric
    target_type: domain
```

```yaml
candidate_edge:
  edge_id: edge.metric.net_settlement.belongs_to_domain.domain.marketplace.flipkart.settlement
  edge_type: BELONGS_TO_DOMAIN
  source: metric.net_settlement
  target: domain.marketplace.flipkart.settlement
  fields:
    edge_family: metric_understanding
    evidence_basis: metric.fields.metric_family
    confidence: high
    canonical_cognee_edge: true
    marketplace_only: true
    canonical_edge_type: BELONGS_TO_DOMAIN
    inverse_edge_type: HAS_METRIC
    materialize_inverse: false
    edge_class: canonical
    source_type: metric
    target_type: domain
```

```yaml
candidate_edge:
  edge_id: edge.metric.realization_rate.belongs_to_domain.domain.marketplace.flipkart.settlement
  edge_type: BELONGS_TO_DOMAIN
  source: metric.realization_rate
  target: domain.marketplace.flipkart.settlement
  fields:
    edge_family: metric_understanding
    evidence_basis: metric.fields.metric_family
    confidence: high
    canonical_cognee_edge: true
    marketplace_only: true
    canonical_edge_type: BELONGS_TO_DOMAIN
    inverse_edge_type: HAS_METRIC
    materialize_inverse: false
    edge_class: canonical
    source_type: metric
    target_type: domain
```

```yaml
candidate_edge:
  edge_id: edge.metric.effective_fee_rate.belongs_to_domain.domain.marketplace.flipkart.fees
  edge_type: BELONGS_TO_DOMAIN
  source: metric.effective_fee_rate
  target: domain.marketplace.flipkart.fees
  fields:
    edge_family: metric_understanding
    evidence_basis: metric.fields.metric_family
    confidence: high
    canonical_cognee_edge: true
    marketplace_only: true
    canonical_edge_type: BELONGS_TO_DOMAIN
    inverse_edge_type: HAS_METRIC
    materialize_inverse: false
    edge_class: canonical
    source_type: metric
    target_type: domain
```

```yaml
candidate_edge:
  edge_id: edge.metric.marketplace_fee_total.belongs_to_domain.domain.marketplace.flipkart.fees
  edge_type: BELONGS_TO_DOMAIN
  source: metric.marketplace_fee_total
  target: domain.marketplace.flipkart.fees
  fields:
    edge_family: metric_understanding
    evidence_basis: metric.fields.metric_family
    confidence: high
    canonical_cognee_edge: true
    marketplace_only: true
    canonical_edge_type: BELONGS_TO_DOMAIN
    inverse_edge_type: HAS_METRIC
    materialize_inverse: false
    edge_class: canonical
    source_type: metric
    target_type: domain
```

```yaml
candidate_edge:
  edge_id: edge.metric.commission_fee.belongs_to_domain.domain.marketplace.flipkart.fees
  edge_type: BELONGS_TO_DOMAIN
  source: metric.commission_fee
  target: domain.marketplace.flipkart.fees
  fields:
    edge_family: metric_understanding
    evidence_basis: metric.fields.metric_family
    confidence: high
    canonical_cognee_edge: true
    marketplace_only: true
    canonical_edge_type: BELONGS_TO_DOMAIN
    inverse_edge_type: HAS_METRIC
    materialize_inverse: false
    edge_class: canonical
    source_type: metric
    target_type: domain
```

```yaml
candidate_edge:
  edge_id: edge.metric.fixed_fee.belongs_to_domain.domain.marketplace.flipkart.fees
  edge_type: BELONGS_TO_DOMAIN
  source: metric.fixed_fee
  target: domain.marketplace.flipkart.fees
  fields:
    edge_family: metric_understanding
    evidence_basis: metric.fields.metric_family
    confidence: high
    canonical_cognee_edge: true
    marketplace_only: true
    canonical_edge_type: BELONGS_TO_DOMAIN
    inverse_edge_type: HAS_METRIC
    materialize_inverse: false
    edge_class: canonical
    source_type: metric
    target_type: domain
```

```yaml
candidate_edge:
  edge_id: edge.metric.shipping_fee.belongs_to_domain.domain.marketplace.flipkart.fees
  edge_type: BELONGS_TO_DOMAIN
  source: metric.shipping_fee
  target: domain.marketplace.flipkart.fees
  fields:
    edge_family: metric_understanding
    evidence_basis: metric.fields.metric_family
    confidence: high
    canonical_cognee_edge: true
    marketplace_only: true
    canonical_edge_type: BELONGS_TO_DOMAIN
    inverse_edge_type: HAS_METRIC
    materialize_inverse: false
    edge_class: canonical
    source_type: metric
    target_type: domain
```

```yaml
candidate_edge:
  edge_id: edge.metric.reverse_shipping_fee.belongs_to_domain.domain.marketplace.flipkart.fees
  edge_type: BELONGS_TO_DOMAIN
  source: metric.reverse_shipping_fee
  target: domain.marketplace.flipkart.fees
  fields:
    edge_family: metric_understanding
    evidence_basis: metric.fields.metric_family
    confidence: high
    canonical_cognee_edge: true
    marketplace_only: true
    canonical_edge_type: BELONGS_TO_DOMAIN
    inverse_edge_type: HAS_METRIC
    materialize_inverse: false
    edge_class: canonical
    source_type: metric
    target_type: domain
```

```yaml
candidate_edge:
  edge_id: edge.metric.collection_fee.belongs_to_domain.domain.marketplace.flipkart.fees
  edge_type: BELONGS_TO_DOMAIN
  source: metric.collection_fee
  target: domain.marketplace.flipkart.fees
  fields:
    edge_family: metric_understanding
    evidence_basis: metric.fields.metric_family
    confidence: high
    canonical_cognee_edge: true
    marketplace_only: true
    canonical_edge_type: BELONGS_TO_DOMAIN
    inverse_edge_type: HAS_METRIC
    materialize_inverse: false
    edge_class: canonical
    source_type: metric
    target_type: domain
```

```yaml
candidate_edge:
  edge_id: edge.metric.net_cashback.belongs_to_domain.domain.marketplace.flipkart.cashback
  edge_type: BELONGS_TO_DOMAIN
  source: metric.net_cashback
  target: domain.marketplace.flipkart.cashback
  fields:
    edge_family: metric_understanding
    evidence_basis: metric.fields.metric_family
    confidence: high
    canonical_cognee_edge: true
    marketplace_only: true
    canonical_edge_type: BELONGS_TO_DOMAIN
    inverse_edge_type: HAS_METRIC
    materialize_inverse: false
    edge_class: canonical
    source_type: metric
    target_type: domain
```

```yaml
candidate_edge:
  edge_id: edge.metric.cashback_rate.belongs_to_domain.domain.marketplace.flipkart.cashback
  edge_type: BELONGS_TO_DOMAIN
  source: metric.cashback_rate
  target: domain.marketplace.flipkart.cashback
  fields:
    edge_family: metric_understanding
    evidence_basis: metric.fields.metric_family
    confidence: high
    canonical_cognee_edge: true
    marketplace_only: true
    canonical_edge_type: BELONGS_TO_DOMAIN
    inverse_edge_type: HAS_METRIC
    materialize_inverse: false
    edge_class: canonical
    source_type: metric
    target_type: domain
```

```yaml
candidate_edge:
  edge_id: edge.metric.return_rate.belongs_to_domain.domain.marketplace.flipkart.returns
  edge_type: BELONGS_TO_DOMAIN
  source: metric.return_rate
  target: domain.marketplace.flipkart.returns
  fields:
    edge_family: metric_understanding
    evidence_basis: metric.fields.metric_family
    confidence: high
    canonical_cognee_edge: true
    marketplace_only: true
    canonical_edge_type: BELONGS_TO_DOMAIN
    inverse_edge_type: HAS_METRIC
    materialize_inverse: false
    edge_class: canonical
    source_type: metric
    target_type: domain
```

```yaml
candidate_edge:
  edge_id: edge.metric.cancellation_rate.belongs_to_domain.domain.marketplace.flipkart.returns
  edge_type: BELONGS_TO_DOMAIN
  source: metric.cancellation_rate
  target: domain.marketplace.flipkart.returns
  fields:
    edge_family: metric_understanding
    evidence_basis: metric.fields.metric_family
    confidence: high
    canonical_cognee_edge: true
    marketplace_only: true
    canonical_edge_type: BELONGS_TO_DOMAIN
    inverse_edge_type: HAS_METRIC
    materialize_inverse: false
    edge_class: canonical
    source_type: metric
    target_type: domain
```

```yaml
candidate_edge:
  edge_id: edge.metric.settlement_cycle_days.belongs_to_domain.domain.marketplace.flipkart.settlement
  edge_type: BELONGS_TO_DOMAIN
  source: metric.settlement_cycle_days
  target: domain.marketplace.flipkart.settlement
  fields:
    edge_family: metric_understanding
    evidence_basis: metric.fields.metric_family
    confidence: high
    canonical_cognee_edge: true
    marketplace_only: true
    canonical_edge_type: BELONGS_TO_DOMAIN
    inverse_edge_type: HAS_METRIC
    materialize_inverse: false
    edge_class: canonical
    source_type: metric
    target_type: domain
```

```yaml
candidate_edge:
  edge_id: edge.metric.tcs_deducted.belongs_to_domain.domain.marketplace.flipkart.tax_deductions
  edge_type: BELONGS_TO_DOMAIN
  source: metric.tcs_deducted
  target: domain.marketplace.flipkart.tax_deductions
  fields:
    edge_family: metric_understanding
    evidence_basis: metric.fields.metric_family
    confidence: high
    canonical_cognee_edge: true
    marketplace_only: true
    canonical_edge_type: BELONGS_TO_DOMAIN
    inverse_edge_type: HAS_METRIC
    materialize_inverse: false
    edge_class: canonical
    source_type: metric
    target_type: domain
```

```yaml
candidate_edge:
  edge_id: edge.metric.tds_deducted.belongs_to_domain.domain.marketplace.flipkart.tax_deductions
  edge_type: BELONGS_TO_DOMAIN
  source: metric.tds_deducted
  target: domain.marketplace.flipkart.tax_deductions
  fields:
    edge_family: metric_understanding
    evidence_basis: metric.fields.metric_family
    confidence: high
    canonical_cognee_edge: true
    marketplace_only: true
    canonical_edge_type: BELONGS_TO_DOMAIN
    inverse_edge_type: HAS_METRIC
    materialize_inverse: false
    edge_class: canonical
    source_type: metric
    target_type: domain
```

```yaml
candidate_edge:
  edge_id: edge.metric.gst_on_marketplace_fees.belongs_to_domain.domain.marketplace.flipkart.tax_deductions
  edge_type: BELONGS_TO_DOMAIN
  source: metric.gst_on_marketplace_fees
  target: domain.marketplace.flipkart.tax_deductions
  fields:
    edge_family: metric_understanding
    evidence_basis: metric.fields.metric_family
    confidence: high
    canonical_cognee_edge: true
    marketplace_only: true
    canonical_edge_type: BELONGS_TO_DOMAIN
    inverse_edge_type: HAS_METRIC
    materialize_inverse: false
    edge_class: canonical
    source_type: metric
    target_type: domain
```

```yaml
candidate_edge:
  edge_id: edge.metric.protection_fund_settlement.belongs_to_domain.domain.marketplace.flipkart.cashback
  edge_type: BELONGS_TO_DOMAIN
  source: metric.protection_fund_settlement
  target: domain.marketplace.flipkart.cashback
  fields:
    edge_family: metric_understanding
    evidence_basis: metric.fields.metric_family
    confidence: high
    canonical_cognee_edge: true
    marketplace_only: true
    canonical_edge_type: BELONGS_TO_DOMAIN
    inverse_edge_type: HAS_METRIC
    materialize_inverse: false
    edge_class: canonical
    source_type: metric
    target_type: domain
```

```yaml
candidate_edge:
  edge_id: edge.domain.marketplace.flipkart.orders.has_business_process.business_process.flipkart.forward_order_to_settlement
  edge_type: HAS_BUSINESS_PROCESS
  source: domain.marketplace.flipkart.orders
  target: business_process.flipkart.forward_order_to_settlement
  fields:
    edge_family: process_understanding
    evidence_basis: deterministic process/domain semantic mapping
    confidence: high
    canonical_cognee_edge: true
    marketplace_only: true
    canonical_edge_type: HAS_BUSINESS_PROCESS
    inverse_edge_type: BELONGS_TO_DOMAIN
    materialize_inverse: true
    edge_class: canonical
    source_type: domain
    target_type: business_process
```

```yaml
candidate_edge:
  edge_id: edge.business_process.flipkart.forward_order_to_settlement.belongs_to_domain.domain.marketplace.flipkart.orders
  edge_type: BELONGS_TO_DOMAIN
  source: business_process.flipkart.forward_order_to_settlement
  target: domain.marketplace.flipkart.orders
  fields:
    edge_family: process_understanding
    evidence_basis: deterministic process/domain semantic mapping
    confidence: high
    canonical_cognee_edge: true
    marketplace_only: true
    canonical_edge_type: BELONGS_TO_DOMAIN
    inverse_edge_type: HAS_BUSINESS_PROCESS
    materialize_inverse: true
    edge_class: canonical
    source_type: business_process
    target_type: domain
```

```yaml
candidate_edge:
  edge_id: edge.domain.marketplace.flipkart.returns.has_business_process.business_process.flipkart.return_cancel_reversal
  edge_type: HAS_BUSINESS_PROCESS
  source: domain.marketplace.flipkart.returns
  target: business_process.flipkart.return_cancel_reversal
  fields:
    edge_family: process_understanding
    evidence_basis: deterministic process/domain semantic mapping
    confidence: high
    canonical_cognee_edge: true
    marketplace_only: true
    canonical_edge_type: HAS_BUSINESS_PROCESS
    inverse_edge_type: BELONGS_TO_DOMAIN
    materialize_inverse: true
    edge_class: canonical
    source_type: domain
    target_type: business_process
```

```yaml
candidate_edge:
  edge_id: edge.business_process.flipkart.return_cancel_reversal.belongs_to_domain.domain.marketplace.flipkart.returns
  edge_type: BELONGS_TO_DOMAIN
  source: business_process.flipkart.return_cancel_reversal
  target: domain.marketplace.flipkart.returns
  fields:
    edge_family: process_understanding
    evidence_basis: deterministic process/domain semantic mapping
    confidence: high
    canonical_cognee_edge: true
    marketplace_only: true
    canonical_edge_type: BELONGS_TO_DOMAIN
    inverse_edge_type: HAS_BUSINESS_PROCESS
    materialize_inverse: true
    edge_class: canonical
    source_type: business_process
    target_type: domain
```

```yaml
candidate_edge:
  edge_id: edge.domain.marketplace.flipkart.fees.has_business_process.business_process.flipkart.commission_fee_invoice
  edge_type: HAS_BUSINESS_PROCESS
  source: domain.marketplace.flipkart.fees
  target: business_process.flipkart.commission_fee_invoice
  fields:
    edge_family: process_understanding
    evidence_basis: deterministic process/domain semantic mapping
    confidence: high
    canonical_cognee_edge: true
    marketplace_only: true
    canonical_edge_type: HAS_BUSINESS_PROCESS
    inverse_edge_type: BELONGS_TO_DOMAIN
    materialize_inverse: true
    edge_class: canonical
    source_type: domain
    target_type: business_process
```

```yaml
candidate_edge:
  edge_id: edge.business_process.flipkart.commission_fee_invoice.belongs_to_domain.domain.marketplace.flipkart.fees
  edge_type: BELONGS_TO_DOMAIN
  source: business_process.flipkart.commission_fee_invoice
  target: domain.marketplace.flipkart.fees
  fields:
    edge_family: process_understanding
    evidence_basis: deterministic process/domain semantic mapping
    confidence: high
    canonical_cognee_edge: true
    marketplace_only: true
    canonical_edge_type: BELONGS_TO_DOMAIN
    inverse_edge_type: HAS_BUSINESS_PROCESS
    materialize_inverse: true
    edge_class: canonical
    source_type: business_process
    target_type: domain
```

```yaml
candidate_edge:
  edge_id: edge.domain.marketplace.flipkart.cashback.has_business_process.business_process.flipkart.cashback_credit_debit_note
  edge_type: HAS_BUSINESS_PROCESS
  source: domain.marketplace.flipkart.cashback
  target: business_process.flipkart.cashback_credit_debit_note
  fields:
    edge_family: process_understanding
    evidence_basis: deterministic process/domain semantic mapping
    confidence: high
    canonical_cognee_edge: true
    marketplace_only: true
    canonical_edge_type: HAS_BUSINESS_PROCESS
    inverse_edge_type: BELONGS_TO_DOMAIN
    materialize_inverse: true
    edge_class: canonical
    source_type: domain
    target_type: business_process
```

```yaml
candidate_edge:
  edge_id: edge.business_process.flipkart.cashback_credit_debit_note.belongs_to_domain.domain.marketplace.flipkart.cashback
  edge_type: BELONGS_TO_DOMAIN
  source: business_process.flipkart.cashback_credit_debit_note
  target: domain.marketplace.flipkart.cashback
  fields:
    edge_family: process_understanding
    evidence_basis: deterministic process/domain semantic mapping
    confidence: high
    canonical_cognee_edge: true
    marketplace_only: true
    canonical_edge_type: BELONGS_TO_DOMAIN
    inverse_edge_type: HAS_BUSINESS_PROCESS
    materialize_inverse: true
    edge_class: canonical
    source_type: business_process
    target_type: domain
```





```yaml
candidate_edge:
  edge_id: edge.domain.marketplace.flipkart.reconciliation.has_business_process.business_process.flipkart.marketplace_reconciliation_pipeline
  edge_type: HAS_BUSINESS_PROCESS
  source: domain.marketplace.flipkart.reconciliation
  target: business_process.flipkart.marketplace_reconciliation_pipeline
  fields:
    edge_family: process_understanding
    evidence_basis: deterministic process/domain semantic mapping
    confidence: high
    canonical_cognee_edge: true
    marketplace_only: true
    canonical_edge_type: HAS_BUSINESS_PROCESS
    inverse_edge_type: BELONGS_TO_DOMAIN
    materialize_inverse: true
    edge_class: canonical
    source_type: domain
    target_type: business_process
```

```yaml
candidate_edge:
  edge_id: edge.business_process.flipkart.marketplace_reconciliation_pipeline.belongs_to_domain.domain.marketplace.flipkart.reconciliation
  edge_type: BELONGS_TO_DOMAIN
  source: business_process.flipkart.marketplace_reconciliation_pipeline
  target: domain.marketplace.flipkart.reconciliation
  fields:
    edge_family: process_understanding
    evidence_basis: deterministic process/domain semantic mapping
    confidence: high
    canonical_cognee_edge: true
    marketplace_only: true
    canonical_edge_type: BELONGS_TO_DOMAIN
    inverse_edge_type: HAS_BUSINESS_PROCESS
    materialize_inverse: true
    edge_class: canonical
    source_type: business_process
    target_type: domain
```

```yaml
candidate_edge:
  edge_id: edge.business_process.flipkart.forward_order_to_settlement.uses_table.table.flipkart.oms
  edge_type: USES_TABLE
  source: business_process.flipkart.forward_order_to_settlement
  target: table.flipkart.oms
  fields:
    edge_family: process_understanding_derived
    evidence_basis: business_process.fields.participating_tables
    confidence: high
    canonical_cognee_edge: false
    marketplace_only: true
    note: Derived parser helper edge from explicit participating_tables field; not listed in Cognee v4 §8.5 but useful for deterministic retrieval.
    canonical_edge_type: USES_TABLE
    legacy_edge_aliases:
    - process_uses_table
    inverse_edge_type: USED_BY_PROCESS
    materialize_inverse: false
    edge_class: parser_helper
    source_type: business_process
    target_type: table
```

```yaml
candidate_edge:
  edge_id: edge.business_process.flipkart.forward_order_to_settlement.uses_table.table.flipkart.settlement
  edge_type: USES_TABLE
  source: business_process.flipkart.forward_order_to_settlement
  target: table.flipkart.settlement
  fields:
    edge_family: process_understanding_derived
    evidence_basis: business_process.fields.participating_tables
    confidence: high
    canonical_cognee_edge: false
    marketplace_only: true
    note: Derived parser helper edge from explicit participating_tables field; not listed in Cognee v4 §8.5 but useful for deterministic retrieval.
    canonical_edge_type: USES_TABLE
    legacy_edge_aliases:
    - process_uses_table
    inverse_edge_type: USED_BY_PROCESS
    materialize_inverse: false
    edge_class: parser_helper
    source_type: business_process
    target_type: table
```

```yaml
candidate_edge:
  edge_id: edge.business_process.flipkart.forward_order_to_settlement.uses_table.table.flipkart.commission
  edge_type: USES_TABLE
  source: business_process.flipkart.forward_order_to_settlement
  target: table.flipkart.commission
  fields:
    edge_family: process_understanding_derived
    evidence_basis: business_process.fields.participating_tables
    confidence: high
    canonical_cognee_edge: false
    marketplace_only: true
    note: Derived parser helper edge from explicit participating_tables field; not listed in Cognee v4 §8.5 but useful for deterministic retrieval.
    canonical_edge_type: USES_TABLE
    legacy_edge_aliases:
    - process_uses_table
    inverse_edge_type: USED_BY_PROCESS
    materialize_inverse: false
    edge_class: parser_helper
    source_type: business_process
    target_type: table
```

```yaml
candidate_edge:
  edge_id: edge.business_process.flipkart.forward_order_to_settlement.uses_table.table.flipkart.cashback
  edge_type: USES_TABLE
  source: business_process.flipkart.forward_order_to_settlement
  target: table.flipkart.cashback
  fields:
    edge_family: process_understanding_derived
    evidence_basis: business_process.fields.participating_tables
    confidence: high
    canonical_cognee_edge: false
    marketplace_only: true
    note: Derived parser helper edge from explicit participating_tables field; not listed in Cognee v4 §8.5 but useful for deterministic retrieval.
    canonical_edge_type: USES_TABLE
    legacy_edge_aliases:
    - process_uses_table
    inverse_edge_type: USED_BY_PROCESS
    materialize_inverse: false
    edge_class: parser_helper
    source_type: business_process
    target_type: table
```

```yaml
candidate_edge:
  edge_id: edge.business_process.flipkart.return_cancel_reversal.uses_table.table.flipkart.oms
  edge_type: USES_TABLE
  source: business_process.flipkart.return_cancel_reversal
  target: table.flipkart.oms
  fields:
    edge_family: process_understanding_derived
    evidence_basis: business_process.fields.participating_tables
    confidence: high
    canonical_cognee_edge: false
    marketplace_only: true
    note: Derived parser helper edge from explicit participating_tables field; not listed in Cognee v4 §8.5 but useful for deterministic retrieval.
    canonical_edge_type: USES_TABLE
    legacy_edge_aliases:
    - process_uses_table
    inverse_edge_type: USED_BY_PROCESS
    materialize_inverse: false
    edge_class: parser_helper
    source_type: business_process
    target_type: table
```

```yaml
candidate_edge:
  edge_id: edge.business_process.flipkart.return_cancel_reversal.uses_table.table.flipkart.settlement
  edge_type: USES_TABLE
  source: business_process.flipkart.return_cancel_reversal
  target: table.flipkart.settlement
  fields:
    edge_family: process_understanding_derived
    evidence_basis: business_process.fields.participating_tables
    confidence: high
    canonical_cognee_edge: false
    marketplace_only: true
    note: Derived parser helper edge from explicit participating_tables field; not listed in Cognee v4 §8.5 but useful for deterministic retrieval.
    canonical_edge_type: USES_TABLE
    legacy_edge_aliases:
    - process_uses_table
    inverse_edge_type: USED_BY_PROCESS
    materialize_inverse: false
    edge_class: parser_helper
    source_type: business_process
    target_type: table
```

```yaml
candidate_edge:
  edge_id: edge.business_process.flipkart.return_cancel_reversal.uses_table.table.flipkart.commission
  edge_type: USES_TABLE
  source: business_process.flipkart.return_cancel_reversal
  target: table.flipkart.commission
  fields:
    edge_family: process_understanding_derived
    evidence_basis: business_process.fields.participating_tables
    confidence: high
    canonical_cognee_edge: false
    marketplace_only: true
    note: Derived parser helper edge from explicit participating_tables field; not listed in Cognee v4 §8.5 but useful for deterministic retrieval.
    canonical_edge_type: USES_TABLE
    legacy_edge_aliases:
    - process_uses_table
    inverse_edge_type: USED_BY_PROCESS
    materialize_inverse: false
    edge_class: parser_helper
    source_type: business_process
    target_type: table
```

```yaml
candidate_edge:
  edge_id: edge.business_process.flipkart.return_cancel_reversal.uses_table.table.flipkart.cashback
  edge_type: USES_TABLE
  source: business_process.flipkart.return_cancel_reversal
  target: table.flipkart.cashback
  fields:
    edge_family: process_understanding_derived
    evidence_basis: business_process.fields.participating_tables
    confidence: high
    canonical_cognee_edge: false
    marketplace_only: true
    note: Derived parser helper edge from explicit participating_tables field; not listed in Cognee v4 §8.5 but useful for deterministic retrieval.
    canonical_edge_type: USES_TABLE
    legacy_edge_aliases:
    - process_uses_table
    inverse_edge_type: USED_BY_PROCESS
    materialize_inverse: false
    edge_class: parser_helper
    source_type: business_process
    target_type: table
```

```yaml
candidate_edge:
  edge_id: edge.business_process.flipkart.commission_fee_invoice.uses_table.table.flipkart.oms
  edge_type: USES_TABLE
  source: business_process.flipkart.commission_fee_invoice
  target: table.flipkart.oms
  fields:
    edge_family: process_understanding_derived
    evidence_basis: business_process.fields.participating_tables
    confidence: high
    canonical_cognee_edge: false
    marketplace_only: true
    note: Derived parser helper edge from explicit participating_tables field; not listed in Cognee v4 §8.5 but useful for deterministic retrieval.
    canonical_edge_type: USES_TABLE
    legacy_edge_aliases:
    - process_uses_table
    inverse_edge_type: USED_BY_PROCESS
    materialize_inverse: false
    edge_class: parser_helper
    source_type: business_process
    target_type: table
```

```yaml
candidate_edge:
  edge_id: edge.business_process.flipkart.commission_fee_invoice.uses_table.table.flipkart.settlement
  edge_type: USES_TABLE
  source: business_process.flipkart.commission_fee_invoice
  target: table.flipkart.settlement
  fields:
    edge_family: process_understanding_derived
    evidence_basis: business_process.fields.participating_tables
    confidence: high
    canonical_cognee_edge: false
    marketplace_only: true
    note: Derived parser helper edge from explicit participating_tables field; not listed in Cognee v4 §8.5 but useful for deterministic retrieval.
    canonical_edge_type: USES_TABLE
    legacy_edge_aliases:
    - process_uses_table
    inverse_edge_type: USED_BY_PROCESS
    materialize_inverse: false
    edge_class: parser_helper
    source_type: business_process
    target_type: table
```

```yaml
candidate_edge:
  edge_id: edge.business_process.flipkart.commission_fee_invoice.uses_table.table.flipkart.commission
  edge_type: USES_TABLE
  source: business_process.flipkart.commission_fee_invoice
  target: table.flipkart.commission
  fields:
    edge_family: process_understanding_derived
    evidence_basis: business_process.fields.participating_tables
    confidence: high
    canonical_cognee_edge: false
    marketplace_only: true
    note: Derived parser helper edge from explicit participating_tables field; not listed in Cognee v4 §8.5 but useful for deterministic retrieval.
    canonical_edge_type: USES_TABLE
    legacy_edge_aliases:
    - process_uses_table
    inverse_edge_type: USED_BY_PROCESS
    materialize_inverse: false
    edge_class: parser_helper
    source_type: business_process
    target_type: table
```

```yaml
candidate_edge:
  edge_id: edge.business_process.flipkart.commission_fee_invoice.uses_table.table.flipkart.cashback
  edge_type: USES_TABLE
  source: business_process.flipkart.commission_fee_invoice
  target: table.flipkart.cashback
  fields:
    edge_family: process_understanding_derived
    evidence_basis: business_process.fields.participating_tables
    confidence: high
    canonical_cognee_edge: false
    marketplace_only: true
    note: Derived parser helper edge from explicit participating_tables field; not listed in Cognee v4 §8.5 but useful for deterministic retrieval.
    canonical_edge_type: USES_TABLE
    legacy_edge_aliases:
    - process_uses_table
    inverse_edge_type: USED_BY_PROCESS
    materialize_inverse: false
    edge_class: parser_helper
    source_type: business_process
    target_type: table
```

```yaml
candidate_edge:
  edge_id: edge.business_process.flipkart.cashback_credit_debit_note.uses_table.table.flipkart.oms
  edge_type: USES_TABLE
  source: business_process.flipkart.cashback_credit_debit_note
  target: table.flipkart.oms
  fields:
    edge_family: process_understanding_derived
    evidence_basis: business_process.fields.participating_tables
    confidence: high
    canonical_cognee_edge: false
    marketplace_only: true
    note: Derived parser helper edge from explicit participating_tables field; not listed in Cognee v4 §8.5 but useful for deterministic retrieval.
    canonical_edge_type: USES_TABLE
    legacy_edge_aliases:
    - process_uses_table
    inverse_edge_type: USED_BY_PROCESS
    materialize_inverse: false
    edge_class: parser_helper
    source_type: business_process
    target_type: table
```

```yaml
candidate_edge:
  edge_id: edge.business_process.flipkart.cashback_credit_debit_note.uses_table.table.flipkart.settlement
  edge_type: USES_TABLE
  source: business_process.flipkart.cashback_credit_debit_note
  target: table.flipkart.settlement
  fields:
    edge_family: process_understanding_derived
    evidence_basis: business_process.fields.participating_tables
    confidence: high
    canonical_cognee_edge: false
    marketplace_only: true
    note: Derived parser helper edge from explicit participating_tables field; not listed in Cognee v4 §8.5 but useful for deterministic retrieval.
    canonical_edge_type: USES_TABLE
    legacy_edge_aliases:
    - process_uses_table
    inverse_edge_type: USED_BY_PROCESS
    materialize_inverse: false
    edge_class: parser_helper
    source_type: business_process
    target_type: table
```

```yaml
candidate_edge:
  edge_id: edge.business_process.flipkart.cashback_credit_debit_note.uses_table.table.flipkart.commission
  edge_type: USES_TABLE
  source: business_process.flipkart.cashback_credit_debit_note
  target: table.flipkart.commission
  fields:
    edge_family: process_understanding_derived
    evidence_basis: business_process.fields.participating_tables
    confidence: high
    canonical_cognee_edge: false
    marketplace_only: true
    note: Derived parser helper edge from explicit participating_tables field; not listed in Cognee v4 §8.5 but useful for deterministic retrieval.
    canonical_edge_type: USES_TABLE
    legacy_edge_aliases:
    - process_uses_table
    inverse_edge_type: USED_BY_PROCESS
    materialize_inverse: false
    edge_class: parser_helper
    source_type: business_process
    target_type: table
```

```yaml
candidate_edge:
  edge_id: edge.business_process.flipkart.cashback_credit_debit_note.uses_table.table.flipkart.cashback
  edge_type: USES_TABLE
  source: business_process.flipkart.cashback_credit_debit_note
  target: table.flipkart.cashback
  fields:
    edge_family: process_understanding_derived
    evidence_basis: business_process.fields.participating_tables
    confidence: high
    canonical_cognee_edge: false
    marketplace_only: true
    note: Derived parser helper edge from explicit participating_tables field; not listed in Cognee v4 §8.5 but useful for deterministic retrieval.
    canonical_edge_type: USES_TABLE
    legacy_edge_aliases:
    - process_uses_table
    inverse_edge_type: USED_BY_PROCESS
    materialize_inverse: false
    edge_class: parser_helper
    source_type: business_process
    target_type: table
```









```yaml
candidate_edge:
  edge_id: edge.business_process.flipkart.marketplace_reconciliation_pipeline.uses_table.table.flipkart.oms
  edge_type: USES_TABLE
  source: business_process.flipkart.marketplace_reconciliation_pipeline
  target: table.flipkart.oms
  fields:
    edge_family: process_understanding_derived
    evidence_basis: business_process.fields.participating_tables
    confidence: high
    canonical_cognee_edge: false
    marketplace_only: true
    note: Derived parser helper edge from explicit participating_tables field; not listed in Cognee v4 §8.5 but useful for deterministic retrieval.
    canonical_edge_type: USES_TABLE
    legacy_edge_aliases:
    - process_uses_table
    inverse_edge_type: USED_BY_PROCESS
    materialize_inverse: false
    edge_class: parser_helper
    source_type: business_process
    target_type: table
```

```yaml
candidate_edge:
  edge_id: edge.business_process.flipkart.marketplace_reconciliation_pipeline.uses_table.table.flipkart.settlement
  edge_type: USES_TABLE
  source: business_process.flipkart.marketplace_reconciliation_pipeline
  target: table.flipkart.settlement
  fields:
    edge_family: process_understanding_derived
    evidence_basis: business_process.fields.participating_tables
    confidence: high
    canonical_cognee_edge: false
    marketplace_only: true
    note: Derived parser helper edge from explicit participating_tables field; not listed in Cognee v4 §8.5 but useful for deterministic retrieval.
    canonical_edge_type: USES_TABLE
    legacy_edge_aliases:
    - process_uses_table
    inverse_edge_type: USED_BY_PROCESS
    materialize_inverse: false
    edge_class: parser_helper
    source_type: business_process
    target_type: table
```

```yaml
candidate_edge:
  edge_id: edge.business_process.flipkart.marketplace_reconciliation_pipeline.uses_table.table.flipkart.commission
  edge_type: USES_TABLE
  source: business_process.flipkart.marketplace_reconciliation_pipeline
  target: table.flipkart.commission
  fields:
    edge_family: process_understanding_derived
    evidence_basis: business_process.fields.participating_tables
    confidence: high
    canonical_cognee_edge: false
    marketplace_only: true
    note: Derived parser helper edge from explicit participating_tables field; not listed in Cognee v4 §8.5 but useful for deterministic retrieval.
    canonical_edge_type: USES_TABLE
    legacy_edge_aliases:
    - process_uses_table
    inverse_edge_type: USED_BY_PROCESS
    materialize_inverse: false
    edge_class: parser_helper
    source_type: business_process
    target_type: table
```

```yaml
candidate_edge:
  edge_id: edge.business_process.flipkart.marketplace_reconciliation_pipeline.uses_table.table.flipkart.cashback
  edge_type: USES_TABLE
  source: business_process.flipkart.marketplace_reconciliation_pipeline
  target: table.flipkart.cashback
  fields:
    edge_family: process_understanding_derived
    evidence_basis: business_process.fields.participating_tables
    confidence: high
    canonical_cognee_edge: false
    marketplace_only: true
    note: Derived parser helper edge from explicit participating_tables field; not listed in Cognee v4 §8.5 but useful for deterministic retrieval.
    canonical_edge_type: USES_TABLE
    legacy_edge_aliases:
    - process_uses_table
    inverse_edge_type: USED_BY_PROCESS
    materialize_inverse: false
    edge_class: parser_helper
    source_type: business_process
    target_type: table
```

```yaml
candidate_edge:
  edge_id: edge.business_process.flipkart.forward_order_to_settlement.has_workflow_step.workflow_step.flipkart.order_capture
  edge_type: HAS_WORKFLOW_STEP
  source: business_process.flipkart.forward_order_to_settlement
  target: workflow_step.flipkart.order_capture
  fields:
    edge_family: process_understanding
    evidence_basis: workflow_step.fields.process_id
    confidence: high
    canonical_cognee_edge: true
    marketplace_only: true
    canonical_edge_type: HAS_WORKFLOW_STEP
    inverse_edge_type: BELONGS_TO_PROCESS
    materialize_inverse: true
    edge_class: canonical
    source_type: business_process
    target_type: workflow_step
```

```yaml
candidate_edge:
  edge_id: edge.workflow_step.flipkart.order_capture.belongs_to_process.business_process.flipkart.forward_order_to_settlement
  edge_type: BELONGS_TO_PROCESS
  source: workflow_step.flipkart.order_capture
  target: business_process.flipkart.forward_order_to_settlement
  fields:
    edge_family: process_understanding
    evidence_basis: workflow_step.fields.process_id
    confidence: high
    canonical_cognee_edge: true
    marketplace_only: true
    canonical_edge_type: BELONGS_TO_PROCESS
    legacy_edge_aliases:
    - step_in_process
    inverse_edge_type: HAS_WORKFLOW_STEP
    materialize_inverse: true
    edge_class: canonical
    source_type: workflow_step
    target_type: business_process
```

```yaml
candidate_edge:
  edge_id: edge.business_process.flipkart.forward_order_to_settlement.has_workflow_step.workflow_step.flipkart.settlement_capture
  edge_type: HAS_WORKFLOW_STEP
  source: business_process.flipkart.forward_order_to_settlement
  target: workflow_step.flipkart.settlement_capture
  fields:
    edge_family: process_understanding
    evidence_basis: workflow_step.fields.process_id
    confidence: high
    canonical_cognee_edge: true
    marketplace_only: true
    canonical_edge_type: HAS_WORKFLOW_STEP
    inverse_edge_type: BELONGS_TO_PROCESS
    materialize_inverse: true
    edge_class: canonical
    source_type: business_process
    target_type: workflow_step
```

```yaml
candidate_edge:
  edge_id: edge.workflow_step.flipkart.settlement_capture.belongs_to_process.business_process.flipkart.forward_order_to_settlement
  edge_type: BELONGS_TO_PROCESS
  source: workflow_step.flipkart.settlement_capture
  target: business_process.flipkart.forward_order_to_settlement
  fields:
    edge_family: process_understanding
    evidence_basis: workflow_step.fields.process_id
    confidence: high
    canonical_cognee_edge: true
    marketplace_only: true
    canonical_edge_type: BELONGS_TO_PROCESS
    legacy_edge_aliases:
    - step_in_process
    inverse_edge_type: HAS_WORKFLOW_STEP
    materialize_inverse: true
    edge_class: canonical
    source_type: workflow_step
    target_type: business_process
```

```yaml
candidate_edge:
  edge_id: edge.business_process.flipkart.commission_fee_invoice.has_workflow_step.workflow_step.flipkart.fee_invoice_capture
  edge_type: HAS_WORKFLOW_STEP
  source: business_process.flipkart.commission_fee_invoice
  target: workflow_step.flipkart.fee_invoice_capture
  fields:
    edge_family: process_understanding
    evidence_basis: workflow_step.fields.process_id
    confidence: high
    canonical_cognee_edge: true
    marketplace_only: true
    canonical_edge_type: HAS_WORKFLOW_STEP
    inverse_edge_type: BELONGS_TO_PROCESS
    materialize_inverse: true
    edge_class: canonical
    source_type: business_process
    target_type: workflow_step
```

```yaml
candidate_edge:
  edge_id: edge.workflow_step.flipkart.fee_invoice_capture.belongs_to_process.business_process.flipkart.commission_fee_invoice
  edge_type: BELONGS_TO_PROCESS
  source: workflow_step.flipkart.fee_invoice_capture
  target: business_process.flipkart.commission_fee_invoice
  fields:
    edge_family: process_understanding
    evidence_basis: workflow_step.fields.process_id
    confidence: high
    canonical_cognee_edge: true
    marketplace_only: true
    canonical_edge_type: BELONGS_TO_PROCESS
    legacy_edge_aliases:
    - step_in_process
    inverse_edge_type: HAS_WORKFLOW_STEP
    materialize_inverse: true
    edge_class: canonical
    source_type: workflow_step
    target_type: business_process
```

```yaml
candidate_edge:
  edge_id: edge.business_process.flipkart.commission_fee_invoice.has_workflow_step.workflow_step.flipkart.fee_aggregation
  edge_type: HAS_WORKFLOW_STEP
  source: business_process.flipkart.commission_fee_invoice
  target: workflow_step.flipkart.fee_aggregation
  fields:
    edge_family: process_understanding
    evidence_basis: workflow_step.fields.process_id
    confidence: high
    canonical_cognee_edge: true
    marketplace_only: true
    canonical_edge_type: HAS_WORKFLOW_STEP
    inverse_edge_type: BELONGS_TO_PROCESS
    materialize_inverse: true
    edge_class: canonical
    source_type: business_process
    target_type: workflow_step
```

```yaml
candidate_edge:
  edge_id: edge.workflow_step.flipkart.fee_aggregation.belongs_to_process.business_process.flipkart.commission_fee_invoice
  edge_type: BELONGS_TO_PROCESS
  source: workflow_step.flipkart.fee_aggregation
  target: business_process.flipkart.commission_fee_invoice
  fields:
    edge_family: process_understanding
    evidence_basis: workflow_step.fields.process_id
    confidence: high
    canonical_cognee_edge: true
    marketplace_only: true
    canonical_edge_type: BELONGS_TO_PROCESS
    legacy_edge_aliases:
    - step_in_process
    inverse_edge_type: HAS_WORKFLOW_STEP
    materialize_inverse: true
    edge_class: canonical
    source_type: workflow_step
    target_type: business_process
```

```yaml
candidate_edge:
  edge_id: edge.business_process.flipkart.cashback_credit_debit_note.has_workflow_step.workflow_step.flipkart.cashback_note_capture
  edge_type: HAS_WORKFLOW_STEP
  source: business_process.flipkart.cashback_credit_debit_note
  target: workflow_step.flipkart.cashback_note_capture
  fields:
    edge_family: process_understanding
    evidence_basis: workflow_step.fields.process_id
    confidence: high
    canonical_cognee_edge: true
    marketplace_only: true
    canonical_edge_type: HAS_WORKFLOW_STEP
    inverse_edge_type: BELONGS_TO_PROCESS
    materialize_inverse: true
    edge_class: canonical
    source_type: business_process
    target_type: workflow_step
```

```yaml
candidate_edge:
  edge_id: edge.workflow_step.flipkart.cashback_note_capture.belongs_to_process.business_process.flipkart.cashback_credit_debit_note
  edge_type: BELONGS_TO_PROCESS
  source: workflow_step.flipkart.cashback_note_capture
  target: business_process.flipkart.cashback_credit_debit_note
  fields:
    edge_family: process_understanding
    evidence_basis: workflow_step.fields.process_id
    confidence: high
    canonical_cognee_edge: true
    marketplace_only: true
    canonical_edge_type: BELONGS_TO_PROCESS
    legacy_edge_aliases:
    - step_in_process
    inverse_edge_type: HAS_WORKFLOW_STEP
    materialize_inverse: true
    edge_class: canonical
    source_type: workflow_step
    target_type: business_process
```

```yaml
candidate_edge:
  edge_id: edge.business_process.flipkart.cashback_credit_debit_note.has_workflow_step.workflow_step.flipkart.cashback_aggregation
  edge_type: HAS_WORKFLOW_STEP
  source: business_process.flipkart.cashback_credit_debit_note
  target: workflow_step.flipkart.cashback_aggregation
  fields:
    edge_family: process_understanding
    evidence_basis: workflow_step.fields.process_id
    confidence: high
    canonical_cognee_edge: true
    marketplace_only: true
    canonical_edge_type: HAS_WORKFLOW_STEP
    inverse_edge_type: BELONGS_TO_PROCESS
    materialize_inverse: true
    edge_class: canonical
    source_type: business_process
    target_type: workflow_step
```

```yaml
candidate_edge:
  edge_id: edge.workflow_step.flipkart.cashback_aggregation.belongs_to_process.business_process.flipkart.cashback_credit_debit_note
  edge_type: BELONGS_TO_PROCESS
  source: workflow_step.flipkart.cashback_aggregation
  target: business_process.flipkart.cashback_credit_debit_note
  fields:
    edge_family: process_understanding
    evidence_basis: workflow_step.fields.process_id
    confidence: high
    canonical_cognee_edge: true
    marketplace_only: true
    canonical_edge_type: BELONGS_TO_PROCESS
    legacy_edge_aliases:
    - step_in_process
    inverse_edge_type: HAS_WORKFLOW_STEP
    materialize_inverse: true
    edge_class: canonical
    source_type: workflow_step
    target_type: business_process
```

```yaml
candidate_edge:
  edge_id: edge.business_process.flipkart.marketplace_reconciliation_pipeline.has_workflow_step.workflow_step.flipkart.settlement_reconcile
  edge_type: HAS_WORKFLOW_STEP
  source: business_process.flipkart.marketplace_reconciliation_pipeline
  target: workflow_step.flipkart.settlement_reconcile
  fields:
    edge_family: process_understanding
    evidence_basis: workflow_step.fields.process_id
    confidence: high
    canonical_cognee_edge: true
    marketplace_only: true
    canonical_edge_type: HAS_WORKFLOW_STEP
    inverse_edge_type: BELONGS_TO_PROCESS
    materialize_inverse: true
    edge_class: canonical
    source_type: business_process
    target_type: workflow_step
```

```yaml
candidate_edge:
  edge_id: edge.workflow_step.flipkart.settlement_reconcile.belongs_to_process.business_process.flipkart.marketplace_reconciliation_pipeline
  edge_type: BELONGS_TO_PROCESS
  source: workflow_step.flipkart.settlement_reconcile
  target: business_process.flipkart.marketplace_reconciliation_pipeline
  fields:
    edge_family: process_understanding
    evidence_basis: workflow_step.fields.process_id
    confidence: high
    canonical_cognee_edge: true
    marketplace_only: true
    canonical_edge_type: BELONGS_TO_PROCESS
    legacy_edge_aliases:
    - step_in_process
    inverse_edge_type: HAS_WORKFLOW_STEP
    materialize_inverse: true
    edge_class: canonical
    source_type: workflow_step
    target_type: business_process
```

```yaml
candidate_edge:
  edge_id: edge.business_process.flipkart.marketplace_reconciliation_pipeline.has_workflow_step.workflow_step.flipkart.exception_output
  edge_type: HAS_WORKFLOW_STEP
  source: business_process.flipkart.marketplace_reconciliation_pipeline
  target: workflow_step.flipkart.exception_output
  fields:
    edge_family: process_understanding
    evidence_basis: workflow_step.fields.process_id
    confidence: high
    canonical_cognee_edge: true
    marketplace_only: true
    canonical_edge_type: HAS_WORKFLOW_STEP
    inverse_edge_type: BELONGS_TO_PROCESS
    materialize_inverse: true
    edge_class: canonical
    source_type: business_process
    target_type: workflow_step
```

```yaml
candidate_edge:
  edge_id: edge.workflow_step.flipkart.exception_output.belongs_to_process.business_process.flipkart.marketplace_reconciliation_pipeline
  edge_type: BELONGS_TO_PROCESS
  source: workflow_step.flipkart.exception_output
  target: business_process.flipkart.marketplace_reconciliation_pipeline
  fields:
    edge_family: process_understanding
    evidence_basis: workflow_step.fields.process_id
    confidence: high
    canonical_cognee_edge: true
    marketplace_only: true
    canonical_edge_type: BELONGS_TO_PROCESS
    legacy_edge_aliases:
    - step_in_process
    inverse_edge_type: HAS_WORKFLOW_STEP
    materialize_inverse: true
    edge_class: canonical
    source_type: workflow_step
    target_type: business_process
```





```yaml
candidate_edge:
  edge_id: edge.business_process.flipkart.cashback_credit_debit_note.has_state_transition.state_transition.flipkart.cashback.sale_to_return
  edge_type: HAS_STATE_TRANSITION
  source: business_process.flipkart.cashback_credit_debit_note
  target: state_transition.flipkart.cashback.sale_to_return
  fields:
    edge_family: process_understanding
    evidence_basis: state_transition.fields.process_id
    confidence: high
    canonical_cognee_edge: true
    marketplace_only: true
    canonical_edge_type: HAS_STATE_TRANSITION
    inverse_edge_type: BELONGS_TO_PROCESS
    materialize_inverse: true
    edge_class: canonical
    source_type: business_process
    target_type: state_transition
```

```yaml
candidate_edge:
  edge_id: edge.state_transition.flipkart.cashback.sale_to_return.belongs_to_process.business_process.flipkart.cashback_credit_debit_note
  edge_type: BELONGS_TO_PROCESS
  source: state_transition.flipkart.cashback.sale_to_return
  target: business_process.flipkart.cashback_credit_debit_note
  fields:
    edge_family: process_understanding
    evidence_basis: state_transition.fields.process_id
    confidence: high
    canonical_cognee_edge: true
    marketplace_only: true
    canonical_edge_type: BELONGS_TO_PROCESS
    legacy_edge_aliases:
    - transition_in_process
    inverse_edge_type: HAS_STATE_TRANSITION
    materialize_inverse: true
    edge_class: canonical
    source_type: state_transition
    target_type: business_process
```

```yaml
candidate_edge:
  edge_id: edge.business_process.flipkart.cashback_credit_debit_note.has_state_transition.state_transition.flipkart.cashback.forward_to_cancel
  edge_type: HAS_STATE_TRANSITION
  source: business_process.flipkart.cashback_credit_debit_note
  target: state_transition.flipkart.cashback.forward_to_cancel
  fields:
    edge_family: process_understanding
    evidence_basis: state_transition.fields.process_id
    confidence: high
    canonical_cognee_edge: true
    marketplace_only: true
    canonical_edge_type: HAS_STATE_TRANSITION
    inverse_edge_type: BELONGS_TO_PROCESS
    materialize_inverse: true
    edge_class: canonical
    source_type: business_process
    target_type: state_transition
```

```yaml
candidate_edge:
  edge_id: edge.state_transition.flipkart.cashback.forward_to_cancel.belongs_to_process.business_process.flipkart.cashback_credit_debit_note
  edge_type: BELONGS_TO_PROCESS
  source: state_transition.flipkart.cashback.forward_to_cancel
  target: business_process.flipkart.cashback_credit_debit_note
  fields:
    edge_family: process_understanding
    evidence_basis: state_transition.fields.process_id
    confidence: high
    canonical_cognee_edge: true
    marketplace_only: true
    canonical_edge_type: BELONGS_TO_PROCESS
    legacy_edge_aliases:
    - transition_in_process
    inverse_edge_type: HAS_STATE_TRANSITION
    materialize_inverse: true
    edge_class: canonical
    source_type: state_transition
    target_type: business_process
```











```yaml
candidate_edge:
  edge_id: edge.reconciliation_profile.flipkart.oms_settlement.has_reconciliation_side.reconciliation_side.flipkart.oms_expected
  edge_type: HAS_RECONCILIATION_SIDE
  source: reconciliation_profile.flipkart.oms_settlement
  target: reconciliation_side.flipkart.oms_expected
  fields:
    edge_family: reconciliation_understanding
    evidence_basis: reconciliation_profile.fields.expected_side
    confidence: high
    canonical_cognee_edge: true
    marketplace_only: true
    side_role: expected
    edge_properties:
      side_role: expected
    canonical_edge_type: HAS_RECONCILIATION_SIDE
    legacy_edge_aliases:
    - profile_expected_side
    inverse_edge_type: BELONGS_TO_RECONCILIATION_PROFILE
    materialize_inverse: true
    edge_class: canonical
    source_type: reconciliation_profile
    target_type: reconciliation_side
```

```yaml
candidate_edge:
  edge_id: edge.reconciliation_profile.flipkart.oms_settlement.has_reconciliation_side.reconciliation_side.flipkart.settlement_actual
  edge_type: HAS_RECONCILIATION_SIDE
  source: reconciliation_profile.flipkart.oms_settlement
  target: reconciliation_side.flipkart.settlement_actual
  fields:
    edge_family: reconciliation_understanding
    evidence_basis: reconciliation_profile.fields.actual_side
    confidence: high
    canonical_cognee_edge: true
    marketplace_only: true
    side_role: actual
    edge_properties:
      side_role: actual
    canonical_edge_type: HAS_RECONCILIATION_SIDE
    legacy_edge_aliases:
    - profile_actual_side
    inverse_edge_type: BELONGS_TO_RECONCILIATION_PROFILE
    materialize_inverse: true
    edge_class: canonical
    source_type: reconciliation_profile
    target_type: reconciliation_side
```

```yaml
candidate_edge:
  edge_id: edge.reconciliation_profile.flipkart.oms_settlement.has_primary_unit.reconciliation_unit.flipkart.order_item
  edge_type: HAS_PRIMARY_UNIT
  source: reconciliation_profile.flipkart.oms_settlement
  target: reconciliation_unit.flipkart.order_item
  fields:
    edge_family: reconciliation_understanding
    evidence_basis: reconciliation_profile.fields.unit
    confidence: high
    canonical_cognee_edge: true
    marketplace_only: true
    canonical_edge_type: HAS_PRIMARY_UNIT
    legacy_edge_aliases:
    - profile_uses_unit
    inverse_edge_type: PRIMARY_UNIT_OF_PROFILE
    materialize_inverse: false
    edge_class: canonical
    source_type: reconciliation_profile
    target_type: reconciliation_unit
```

```yaml
candidate_edge:
  edge_id: edge.reconciliation_profile.flipkart.oms_settlement.uses_matching_logic.matching_logic.flipkart.oms_settlement
  edge_type: USES_MATCHING_LOGIC
  source: reconciliation_profile.flipkart.oms_settlement
  target: matching_logic.flipkart.oms_settlement
  fields:
    edge_family: reconciliation_understanding
    evidence_basis: reconciliation_profile.fields.matching_logic
    confidence: high
    canonical_cognee_edge: true
    marketplace_only: true
    canonical_edge_type: USES_MATCHING_LOGIC
    legacy_edge_aliases:
    - profile_uses_matching_logic
    inverse_edge_type: SUPPORTS_RECONCILIATION_PROFILE
    materialize_inverse: true
    edge_class: canonical
    source_type: reconciliation_profile
    target_type: matching_logic
```

```yaml
candidate_edge:
  edge_id: edge.reconciliation_profile.flipkart.oms_settlement.has_mismatch_category.mismatch_category.flipkart.missing_settlement
  edge_type: HAS_MISMATCH_CATEGORY
  source: reconciliation_profile.flipkart.oms_settlement
  target: mismatch_category.flipkart.missing_settlement
  fields:
    edge_family: reconciliation_understanding
    evidence_basis: reconciliation_profile.fields.mismatch_categories
    confidence: high
    canonical_cognee_edge: true
    marketplace_only: true
    canonical_edge_type: HAS_MISMATCH_CATEGORY
    legacy_edge_aliases:
    - profile_has_mismatch_category
    inverse_edge_type: MISMATCH_OF_PROFILE
    materialize_inverse: false
    edge_class: canonical
    source_type: reconciliation_profile
    target_type: mismatch_category
```

```yaml
candidate_edge:
  edge_id: edge.reconciliation_profile.flipkart.settlement_commission.has_reconciliation_side.reconciliation_side.flipkart.settlement_fee_actual
  edge_type: HAS_RECONCILIATION_SIDE
  source: reconciliation_profile.flipkart.settlement_commission
  target: reconciliation_side.flipkart.settlement_fee_actual
  fields:
    edge_family: reconciliation_understanding
    evidence_basis: reconciliation_profile.fields.expected_side
    confidence: high
    canonical_cognee_edge: true
    marketplace_only: true
    side_role: expected
    edge_properties:
      side_role: expected
    canonical_edge_type: HAS_RECONCILIATION_SIDE
    legacy_edge_aliases:
    - profile_expected_side
    inverse_edge_type: BELONGS_TO_RECONCILIATION_PROFILE
    materialize_inverse: true
    edge_class: canonical
    source_type: reconciliation_profile
    target_type: reconciliation_side
```

```yaml
candidate_edge:
  edge_id: edge.reconciliation_profile.flipkart.settlement_commission.has_reconciliation_side.reconciliation_side.flipkart.commission_detail_expected
  edge_type: HAS_RECONCILIATION_SIDE
  source: reconciliation_profile.flipkart.settlement_commission
  target: reconciliation_side.flipkart.commission_detail_expected
  fields:
    edge_family: reconciliation_understanding
    evidence_basis: reconciliation_profile.fields.actual_side
    confidence: high
    canonical_cognee_edge: true
    marketplace_only: true
    side_role: actual
    edge_properties:
      side_role: actual
    canonical_edge_type: HAS_RECONCILIATION_SIDE
    legacy_edge_aliases:
    - profile_actual_side
    inverse_edge_type: BELONGS_TO_RECONCILIATION_PROFILE
    materialize_inverse: true
    edge_class: canonical
    source_type: reconciliation_profile
    target_type: reconciliation_side
```

```yaml
candidate_edge:
  edge_id: edge.reconciliation_profile.flipkart.settlement_commission.has_primary_unit.reconciliation_unit.flipkart.normalized_order_item
  edge_type: HAS_PRIMARY_UNIT
  source: reconciliation_profile.flipkart.settlement_commission
  target: reconciliation_unit.flipkart.normalized_order_item
  fields:
    edge_family: reconciliation_understanding
    evidence_basis: reconciliation_profile.fields.unit
    confidence: high
    canonical_cognee_edge: true
    marketplace_only: true
    canonical_edge_type: HAS_PRIMARY_UNIT
    legacy_edge_aliases:
    - profile_uses_unit
    inverse_edge_type: PRIMARY_UNIT_OF_PROFILE
    materialize_inverse: false
    edge_class: canonical
    source_type: reconciliation_profile
    target_type: reconciliation_unit
```

```yaml
candidate_edge:
  edge_id: edge.reconciliation_profile.flipkart.settlement_commission.uses_matching_logic.matching_logic.flipkart.settlement_commission_od_normalized
  edge_type: USES_MATCHING_LOGIC
  source: reconciliation_profile.flipkart.settlement_commission
  target: matching_logic.flipkart.settlement_commission_od_normalized
  fields:
    edge_family: reconciliation_understanding
    evidence_basis: reconciliation_profile.fields.matching_logic
    confidence: high
    canonical_cognee_edge: true
    marketplace_only: true
    canonical_edge_type: USES_MATCHING_LOGIC
    legacy_edge_aliases:
    - profile_uses_matching_logic
    inverse_edge_type: SUPPORTS_RECONCILIATION_PROFILE
    materialize_inverse: true
    edge_class: canonical
    source_type: reconciliation_profile
    target_type: matching_logic
```

```yaml
candidate_edge:
  edge_id: edge.reconciliation_profile.flipkart.settlement_commission.has_mismatch_category.mismatch_category.flipkart.missing_settlement
  edge_type: HAS_MISMATCH_CATEGORY
  source: reconciliation_profile.flipkart.settlement_commission
  target: mismatch_category.flipkart.missing_settlement
  fields:
    edge_family: reconciliation_understanding
    evidence_basis: reconciliation_profile.fields.mismatch_categories
    confidence: high
    canonical_cognee_edge: true
    marketplace_only: true
    canonical_edge_type: HAS_MISMATCH_CATEGORY
    legacy_edge_aliases:
    - profile_has_mismatch_category
    inverse_edge_type: MISMATCH_OF_PROFILE
    materialize_inverse: false
    edge_class: canonical
    source_type: reconciliation_profile
    target_type: mismatch_category
```

```yaml
candidate_edge:
  edge_id: edge.reconciliation_profile.flipkart.cashback_settlement_offer.has_reconciliation_side.reconciliation_side.flipkart.cashback_expected
  edge_type: HAS_RECONCILIATION_SIDE
  source: reconciliation_profile.flipkart.cashback_settlement_offer
  target: reconciliation_side.flipkart.cashback_expected
  fields:
    edge_family: reconciliation_understanding
    evidence_basis: reconciliation_profile.fields.expected_side
    confidence: high
    canonical_cognee_edge: true
    marketplace_only: true
    side_role: expected
    edge_properties:
      side_role: expected
    canonical_edge_type: HAS_RECONCILIATION_SIDE
    legacy_edge_aliases:
    - profile_expected_side
    inverse_edge_type: BELONGS_TO_RECONCILIATION_PROFILE
    materialize_inverse: true
    edge_class: canonical
    source_type: reconciliation_profile
    target_type: reconciliation_side
```

```yaml
candidate_edge:
  edge_id: edge.reconciliation_profile.flipkart.cashback_settlement_offer.has_reconciliation_side.reconciliation_side.flipkart.settlement_offer_actual
  edge_type: HAS_RECONCILIATION_SIDE
  source: reconciliation_profile.flipkart.cashback_settlement_offer
  target: reconciliation_side.flipkart.settlement_offer_actual
  fields:
    edge_family: reconciliation_understanding
    evidence_basis: reconciliation_profile.fields.actual_side
    confidence: high
    canonical_cognee_edge: true
    marketplace_only: true
    side_role: actual
    edge_properties:
      side_role: actual
    canonical_edge_type: HAS_RECONCILIATION_SIDE
    legacy_edge_aliases:
    - profile_actual_side
    inverse_edge_type: BELONGS_TO_RECONCILIATION_PROFILE
    materialize_inverse: true
    edge_class: canonical
    source_type: reconciliation_profile
    target_type: reconciliation_side
```

```yaml
candidate_edge:
  edge_id: edge.reconciliation_profile.flipkart.cashback_settlement_offer.has_primary_unit.reconciliation_unit.flipkart.order_item
  edge_type: HAS_PRIMARY_UNIT
  source: reconciliation_profile.flipkart.cashback_settlement_offer
  target: reconciliation_unit.flipkart.order_item
  fields:
    edge_family: reconciliation_understanding
    evidence_basis: reconciliation_profile.fields.unit
    confidence: high
    canonical_cognee_edge: true
    marketplace_only: true
    canonical_edge_type: HAS_PRIMARY_UNIT
    legacy_edge_aliases:
    - profile_uses_unit
    inverse_edge_type: PRIMARY_UNIT_OF_PROFILE
    materialize_inverse: false
    edge_class: canonical
    source_type: reconciliation_profile
    target_type: reconciliation_unit
```

```yaml
candidate_edge:
  edge_id: edge.reconciliation_profile.flipkart.cashback_settlement_offer.uses_matching_logic.matching_logic.flipkart.cashback_settlement_offer
  edge_type: USES_MATCHING_LOGIC
  source: reconciliation_profile.flipkart.cashback_settlement_offer
  target: matching_logic.flipkart.cashback_settlement_offer
  fields:
    edge_family: reconciliation_understanding
    evidence_basis: reconciliation_profile.fields.matching_logic
    confidence: high
    canonical_cognee_edge: true
    marketplace_only: true
    canonical_edge_type: USES_MATCHING_LOGIC
    legacy_edge_aliases:
    - profile_uses_matching_logic
    inverse_edge_type: SUPPORTS_RECONCILIATION_PROFILE
    materialize_inverse: true
    edge_class: canonical
    source_type: reconciliation_profile
    target_type: matching_logic
```

```yaml
candidate_edge:
  edge_id: edge.reconciliation_profile.flipkart.cashback_settlement_offer.has_mismatch_category.mismatch_category.flipkart.missing_settlement
  edge_type: HAS_MISMATCH_CATEGORY
  source: reconciliation_profile.flipkart.cashback_settlement_offer
  target: mismatch_category.flipkart.missing_settlement
  fields:
    edge_family: reconciliation_understanding
    evidence_basis: reconciliation_profile.fields.mismatch_categories
    confidence: high
    canonical_cognee_edge: true
    marketplace_only: true
    canonical_edge_type: HAS_MISMATCH_CATEGORY
    legacy_edge_aliases:
    - profile_has_mismatch_category
    inverse_edge_type: MISMATCH_OF_PROFILE
    materialize_inverse: false
    edge_class: canonical
    source_type: reconciliation_profile
    target_type: mismatch_category
```

```yaml
candidate_edge:
  edge_id: edge.reconciliation_profile.flipkart.settlement_waterfall.has_reconciliation_side.reconciliation_side.flipkart.settlement_components
  edge_type: HAS_RECONCILIATION_SIDE
  source: reconciliation_profile.flipkart.settlement_waterfall
  target: reconciliation_side.flipkart.settlement_components
  fields:
    edge_family: reconciliation_understanding
    evidence_basis: reconciliation_profile.fields.expected_side
    confidence: high
    canonical_cognee_edge: true
    marketplace_only: true
    side_role: expected
    edge_properties:
      side_role: expected
    canonical_edge_type: HAS_RECONCILIATION_SIDE
    legacy_edge_aliases:
    - profile_expected_side
    inverse_edge_type: BELONGS_TO_RECONCILIATION_PROFILE
    materialize_inverse: true
    edge_class: canonical
    source_type: reconciliation_profile
    target_type: reconciliation_side
```

```yaml
candidate_edge:
  edge_id: edge.reconciliation_profile.flipkart.settlement_waterfall.has_reconciliation_side.reconciliation_side.flipkart.settlement_net
  edge_type: HAS_RECONCILIATION_SIDE
  source: reconciliation_profile.flipkart.settlement_waterfall
  target: reconciliation_side.flipkart.settlement_net
  fields:
    edge_family: reconciliation_understanding
    evidence_basis: reconciliation_profile.fields.actual_side
    confidence: high
    canonical_cognee_edge: true
    marketplace_only: true
    side_role: actual
    edge_properties:
      side_role: actual
    canonical_edge_type: HAS_RECONCILIATION_SIDE
    legacy_edge_aliases:
    - profile_actual_side
    inverse_edge_type: BELONGS_TO_RECONCILIATION_PROFILE
    materialize_inverse: true
    edge_class: canonical
    source_type: reconciliation_profile
    target_type: reconciliation_side
```

```yaml
candidate_edge:
  edge_id: edge.reconciliation_profile.flipkart.settlement_waterfall.has_primary_unit.reconciliation_unit.flipkart.settlement_line
  edge_type: HAS_PRIMARY_UNIT
  source: reconciliation_profile.flipkart.settlement_waterfall
  target: reconciliation_unit.flipkart.settlement_line
  fields:
    edge_family: reconciliation_understanding
    evidence_basis: reconciliation_profile.fields.unit
    confidence: high
    canonical_cognee_edge: true
    marketplace_only: true
    canonical_edge_type: HAS_PRIMARY_UNIT
    legacy_edge_aliases:
    - profile_uses_unit
    inverse_edge_type: PRIMARY_UNIT_OF_PROFILE
    materialize_inverse: false
    edge_class: canonical
    source_type: reconciliation_profile
    target_type: reconciliation_unit
```

```yaml
candidate_edge:
  edge_id: edge.reconciliation_profile.flipkart.settlement_waterfall.uses_matching_logic.matching_logic.flipkart.settlement_waterfall
  edge_type: USES_MATCHING_LOGIC
  source: reconciliation_profile.flipkart.settlement_waterfall
  target: matching_logic.flipkart.settlement_waterfall
  fields:
    edge_family: reconciliation_understanding
    evidence_basis: reconciliation_profile.fields.matching_logic
    confidence: high
    canonical_cognee_edge: true
    marketplace_only: true
    canonical_edge_type: USES_MATCHING_LOGIC
    legacy_edge_aliases:
    - profile_uses_matching_logic
    inverse_edge_type: SUPPORTS_RECONCILIATION_PROFILE
    materialize_inverse: true
    edge_class: canonical
    source_type: reconciliation_profile
    target_type: matching_logic
```

```yaml
candidate_edge:
  edge_id: edge.reconciliation_profile.flipkart.settlement_waterfall.has_mismatch_category.mismatch_category.flipkart.missing_settlement
  edge_type: HAS_MISMATCH_CATEGORY
  source: reconciliation_profile.flipkart.settlement_waterfall
  target: mismatch_category.flipkart.missing_settlement
  fields:
    edge_family: reconciliation_understanding
    evidence_basis: reconciliation_profile.fields.mismatch_categories
    confidence: high
    canonical_cognee_edge: true
    marketplace_only: true
    canonical_edge_type: HAS_MISMATCH_CATEGORY
    legacy_edge_aliases:
    - profile_has_mismatch_category
    inverse_edge_type: MISMATCH_OF_PROFILE
    materialize_inverse: false
    edge_class: canonical
    source_type: reconciliation_profile
    target_type: mismatch_category
```

```yaml
candidate_edge:
  edge_id: edge.reconciliation_profile.flipkart.cross_table_pipeline.has_reconciliation_side.reconciliation_side.flipkart.order_fee_cashback_expected
  edge_type: HAS_RECONCILIATION_SIDE
  source: reconciliation_profile.flipkart.cross_table_pipeline
  target: reconciliation_side.flipkart.order_fee_cashback_expected
  fields:
    edge_family: reconciliation_understanding
    evidence_basis: reconciliation_profile.fields.expected_side
    confidence: high
    canonical_cognee_edge: true
    marketplace_only: true
    side_role: expected
    edge_properties:
      side_role: expected
    canonical_edge_type: HAS_RECONCILIATION_SIDE
    legacy_edge_aliases:
    - profile_expected_side
    inverse_edge_type: BELONGS_TO_RECONCILIATION_PROFILE
    materialize_inverse: true
    edge_class: canonical
    source_type: reconciliation_profile
    target_type: reconciliation_side
```

```yaml
candidate_edge:
  edge_id: edge.reconciliation_profile.flipkart.cross_table_pipeline.has_reconciliation_side.reconciliation_side.flipkart.settlement_actual
  edge_type: HAS_RECONCILIATION_SIDE
  source: reconciliation_profile.flipkart.cross_table_pipeline
  target: reconciliation_side.flipkart.settlement_actual
  fields:
    edge_family: reconciliation_understanding
    evidence_basis: reconciliation_profile.fields.actual_side
    confidence: high
    canonical_cognee_edge: true
    marketplace_only: true
    side_role: actual
    edge_properties:
      side_role: actual
    canonical_edge_type: HAS_RECONCILIATION_SIDE
    legacy_edge_aliases:
    - profile_actual_side
    inverse_edge_type: BELONGS_TO_RECONCILIATION_PROFILE
    materialize_inverse: true
    edge_class: canonical
    source_type: reconciliation_profile
    target_type: reconciliation_side
```

```yaml
candidate_edge:
  edge_id: edge.reconciliation_profile.flipkart.cross_table_pipeline.has_primary_unit.reconciliation_unit.flipkart.order_item
  edge_type: HAS_PRIMARY_UNIT
  source: reconciliation_profile.flipkart.cross_table_pipeline
  target: reconciliation_unit.flipkart.order_item
  fields:
    edge_family: reconciliation_understanding
    evidence_basis: reconciliation_profile.fields.unit
    confidence: high
    canonical_cognee_edge: true
    marketplace_only: true
    canonical_edge_type: HAS_PRIMARY_UNIT
    legacy_edge_aliases:
    - profile_uses_unit
    inverse_edge_type: PRIMARY_UNIT_OF_PROFILE
    materialize_inverse: false
    edge_class: canonical
    source_type: reconciliation_profile
    target_type: reconciliation_unit
```

```yaml
candidate_edge:
  edge_id: edge.reconciliation_profile.flipkart.cross_table_pipeline.uses_matching_logic.matching_logic.flipkart.cross_table_pipeline
  edge_type: USES_MATCHING_LOGIC
  source: reconciliation_profile.flipkart.cross_table_pipeline
  target: matching_logic.flipkart.cross_table_pipeline
  fields:
    edge_family: reconciliation_understanding
    evidence_basis: reconciliation_profile.fields.matching_logic
    confidence: high
    canonical_cognee_edge: true
    marketplace_only: true
    canonical_edge_type: USES_MATCHING_LOGIC
    legacy_edge_aliases:
    - profile_uses_matching_logic
    inverse_edge_type: SUPPORTS_RECONCILIATION_PROFILE
    materialize_inverse: true
    edge_class: canonical
    source_type: reconciliation_profile
    target_type: matching_logic
```

```yaml
candidate_edge:
  edge_id: edge.reconciliation_profile.flipkart.cross_table_pipeline.has_mismatch_category.mismatch_category.flipkart.missing_settlement
  edge_type: HAS_MISMATCH_CATEGORY
  source: reconciliation_profile.flipkart.cross_table_pipeline
  target: mismatch_category.flipkart.missing_settlement
  fields:
    edge_family: reconciliation_understanding
    evidence_basis: reconciliation_profile.fields.mismatch_categories
    confidence: high
    canonical_cognee_edge: true
    marketplace_only: true
    canonical_edge_type: HAS_MISMATCH_CATEGORY
    legacy_edge_aliases:
    - profile_has_mismatch_category
    inverse_edge_type: MISMATCH_OF_PROFILE
    materialize_inverse: false
    edge_class: canonical
    source_type: reconciliation_profile
    target_type: mismatch_category
```

```yaml
candidate_edge:
  edge_id: edge.reconciliation_side.flipkart.oms_expected.uses_table.table.flipkart.oms
  edge_type: USES_TABLE
  source: reconciliation_side.flipkart.oms_expected
  target: table.flipkart.oms
  fields:
    edge_family: reconciliation_understanding_derived
    evidence_basis: reconciliation_side.fields.source_table
    confidence: high
    canonical_cognee_edge: false
    marketplace_only: true
    note: Derived parser helper edge from explicit ReconciliationSide.source_table field.
    canonical_edge_type: USES_TABLE
    legacy_edge_aliases:
    - side_uses_table
    inverse_edge_type: USED_BY_RECONCILIATION_SIDE
    materialize_inverse: false
    edge_class: parser_helper
    source_type: reconciliation_side
    target_type: table
```

```yaml
candidate_edge:
  edge_id: edge.reconciliation_side.flipkart.oms_expected.uses_column.column.oms.order_id.role_key
  edge_type: USES_COLUMN
  source: reconciliation_side.flipkart.oms_expected
  target: column.oms.order_id
  fields:
    edge_family: reconciliation_understanding_derived
    evidence_basis: reconciliation_side.fields.key_columns
    confidence: high
    canonical_cognee_edge: false
    marketplace_only: true
    note: Derived parser helper edge from explicit ReconciliationSide.key_columns field.
    original_edge_type: USES_KEY_COLUMN
    column_role: key
    edge_properties:
      column_role: key
    canonical_edge_type: USES_COLUMN
    legacy_edge_aliases:
    - side_uses_key_column
    inverse_edge_type: USED_BY_RECONCILIATION_SIDE
    materialize_inverse: false
    edge_class: parser_helper
    source_type: reconciliation_side
    target_type: column
```

```yaml
candidate_edge:
  edge_id: edge.reconciliation_side.flipkart.oms_expected.uses_column.column.oms.item_id.role_key
  edge_type: USES_COLUMN
  source: reconciliation_side.flipkart.oms_expected
  target: column.oms.item_id
  fields:
    edge_family: reconciliation_understanding_derived
    evidence_basis: reconciliation_side.fields.key_columns
    confidence: high
    canonical_cognee_edge: false
    marketplace_only: true
    note: Derived parser helper edge from explicit ReconciliationSide.key_columns field.
    original_edge_type: USES_KEY_COLUMN
    column_role: key
    edge_properties:
      column_role: key
    canonical_edge_type: USES_COLUMN
    legacy_edge_aliases:
    - side_uses_key_column
    inverse_edge_type: USED_BY_RECONCILIATION_SIDE
    materialize_inverse: false
    edge_class: parser_helper
    source_type: reconciliation_side
    target_type: column
```

```yaml
candidate_edge:
  edge_id: edge.reconciliation_side.flipkart.oms_expected.uses_column.column.oms.charged_amount.role_amount
  edge_type: USES_COLUMN
  source: reconciliation_side.flipkart.oms_expected
  target: column.oms.charged_amount
  fields:
    edge_family: reconciliation_understanding_derived
    evidence_basis: reconciliation_side.fields.amount_columns
    confidence: high
    canonical_cognee_edge: false
    marketplace_only: true
    note: Derived parser helper edge from explicit ReconciliationSide.amount_columns field.
    original_edge_type: USES_AMOUNT_COLUMN
    column_role: amount
    edge_properties:
      column_role: amount
    canonical_edge_type: USES_COLUMN
    legacy_edge_aliases:
    - side_uses_amount_column
    inverse_edge_type: USED_BY_RECONCILIATION_SIDE
    materialize_inverse: false
    edge_class: parser_helper
    source_type: reconciliation_side
    target_type: column
```

```yaml
candidate_edge:
  edge_id: edge.reconciliation_side.flipkart.settlement_actual.uses_table.table.flipkart.settlement
  edge_type: USES_TABLE
  source: reconciliation_side.flipkart.settlement_actual
  target: table.flipkart.settlement
  fields:
    edge_family: reconciliation_understanding_derived
    evidence_basis: reconciliation_side.fields.source_table
    confidence: high
    canonical_cognee_edge: false
    marketplace_only: true
    note: Derived parser helper edge from explicit ReconciliationSide.source_table field.
    canonical_edge_type: USES_TABLE
    legacy_edge_aliases:
    - side_uses_table
    inverse_edge_type: USED_BY_RECONCILIATION_SIDE
    materialize_inverse: false
    edge_class: parser_helper
    source_type: reconciliation_side
    target_type: table
```

```yaml
candidate_edge:
  edge_id: edge.reconciliation_side.flipkart.settlement_actual.uses_column.column.settlement.order_id.role_key
  edge_type: USES_COLUMN
  source: reconciliation_side.flipkart.settlement_actual
  target: column.settlement.order_id
  fields:
    edge_family: reconciliation_understanding_derived
    evidence_basis: reconciliation_side.fields.key_columns
    confidence: high
    canonical_cognee_edge: false
    marketplace_only: true
    note: Derived parser helper edge from explicit ReconciliationSide.key_columns field.
    original_edge_type: USES_KEY_COLUMN
    column_role: key
    edge_properties:
      column_role: key
    canonical_edge_type: USES_COLUMN
    legacy_edge_aliases:
    - side_uses_key_column
    inverse_edge_type: USED_BY_RECONCILIATION_SIDE
    materialize_inverse: false
    edge_class: parser_helper
    source_type: reconciliation_side
    target_type: column
```

```yaml
candidate_edge:
  edge_id: edge.reconciliation_side.flipkart.settlement_actual.uses_column.column.settlement.item_id.role_key
  edge_type: USES_COLUMN
  source: reconciliation_side.flipkart.settlement_actual
  target: column.settlement.item_id
  fields:
    edge_family: reconciliation_understanding_derived
    evidence_basis: reconciliation_side.fields.key_columns
    confidence: high
    canonical_cognee_edge: false
    marketplace_only: true
    note: Derived parser helper edge from explicit ReconciliationSide.key_columns field.
    original_edge_type: USES_KEY_COLUMN
    column_role: key
    edge_properties:
      column_role: key
    canonical_edge_type: USES_COLUMN
    legacy_edge_aliases:
    - side_uses_key_column
    inverse_edge_type: USED_BY_RECONCILIATION_SIDE
    materialize_inverse: false
    edge_class: parser_helper
    source_type: reconciliation_side
    target_type: column
```

```yaml
candidate_edge:
  edge_id: edge.reconciliation_side.flipkart.settlement_actual.uses_column.column.settlement.settled_amount.role_amount
  edge_type: USES_COLUMN
  source: reconciliation_side.flipkart.settlement_actual
  target: column.settlement.settled_amount
  fields:
    edge_family: reconciliation_understanding_derived
    evidence_basis: reconciliation_side.fields.amount_columns
    confidence: high
    canonical_cognee_edge: false
    marketplace_only: true
    note: Derived parser helper edge from explicit ReconciliationSide.amount_columns field.
    original_edge_type: USES_AMOUNT_COLUMN
    column_role: amount
    edge_properties:
      column_role: amount
    canonical_edge_type: USES_COLUMN
    legacy_edge_aliases:
    - side_uses_amount_column
    inverse_edge_type: USED_BY_RECONCILIATION_SIDE
    materialize_inverse: false
    edge_class: parser_helper
    source_type: reconciliation_side
    target_type: column
```

```yaml
candidate_edge:
  edge_id: edge.reconciliation_side.flipkart.settlement_actual.uses_column.column.settlement.sale_settled_amount.role_amount
  edge_type: USES_COLUMN
  source: reconciliation_side.flipkart.settlement_actual
  target: column.settlement.sale_settled_amount
  fields:
    edge_family: reconciliation_understanding_derived
    evidence_basis: reconciliation_side.fields.amount_columns
    confidence: high
    canonical_cognee_edge: false
    marketplace_only: true
    note: Derived parser helper edge from explicit ReconciliationSide.amount_columns field.
    original_edge_type: USES_AMOUNT_COLUMN
    column_role: amount
    edge_properties:
      column_role: amount
    canonical_edge_type: USES_COLUMN
    legacy_edge_aliases:
    - side_uses_amount_column
    inverse_edge_type: USED_BY_RECONCILIATION_SIDE
    materialize_inverse: false
    edge_class: parser_helper
    source_type: reconciliation_side
    target_type: column
```

```yaml
candidate_edge:
  edge_id: edge.reconciliation_side.flipkart.settlement_fee_actual.uses_table.table.flipkart.settlement
  edge_type: USES_TABLE
  source: reconciliation_side.flipkart.settlement_fee_actual
  target: table.flipkart.settlement
  fields:
    edge_family: reconciliation_understanding_derived
    evidence_basis: reconciliation_side.fields.source_table
    confidence: high
    canonical_cognee_edge: false
    marketplace_only: true
    note: Derived parser helper edge from explicit ReconciliationSide.source_table field.
    canonical_edge_type: USES_TABLE
    legacy_edge_aliases:
    - side_uses_table
    inverse_edge_type: USED_BY_RECONCILIATION_SIDE
    materialize_inverse: false
    edge_class: parser_helper
    source_type: reconciliation_side
    target_type: table
```

```yaml
candidate_edge:
  edge_id: edge.reconciliation_side.flipkart.settlement_fee_actual.uses_column.column.settlement.order_id.role_key
  edge_type: USES_COLUMN
  source: reconciliation_side.flipkart.settlement_fee_actual
  target: column.settlement.order_id
  fields:
    edge_family: reconciliation_understanding_derived
    evidence_basis: reconciliation_side.fields.key_columns
    confidence: high
    canonical_cognee_edge: false
    marketplace_only: true
    note: Derived parser helper edge from explicit ReconciliationSide.key_columns field.
    original_edge_type: USES_KEY_COLUMN
    column_role: key
    edge_properties:
      column_role: key
    canonical_edge_type: USES_COLUMN
    legacy_edge_aliases:
    - side_uses_key_column
    inverse_edge_type: USED_BY_RECONCILIATION_SIDE
    materialize_inverse: false
    edge_class: parser_helper
    source_type: reconciliation_side
    target_type: column
```

```yaml
candidate_edge:
  edge_id: edge.reconciliation_side.flipkart.settlement_fee_actual.uses_column.column.settlement.item_id.role_key
  edge_type: USES_COLUMN
  source: reconciliation_side.flipkart.settlement_fee_actual
  target: column.settlement.item_id
  fields:
    edge_family: reconciliation_understanding_derived
    evidence_basis: reconciliation_side.fields.key_columns
    confidence: high
    canonical_cognee_edge: false
    marketplace_only: true
    note: Derived parser helper edge from explicit ReconciliationSide.key_columns field.
    original_edge_type: USES_KEY_COLUMN
    column_role: key
    edge_properties:
      column_role: key
    canonical_edge_type: USES_COLUMN
    legacy_edge_aliases:
    - side_uses_key_column
    inverse_edge_type: USED_BY_RECONCILIATION_SIDE
    materialize_inverse: false
    edge_class: parser_helper
    source_type: reconciliation_side
    target_type: column
```

```yaml
candidate_edge:
  edge_id: edge.reconciliation_side.flipkart.settlement_fee_actual.uses_column.column.settlement.mp_fee.role_amount
  edge_type: USES_COLUMN
  source: reconciliation_side.flipkart.settlement_fee_actual
  target: column.settlement.mp_fee
  fields:
    edge_family: reconciliation_understanding_derived
    evidence_basis: reconciliation_side.fields.amount_columns
    confidence: high
    canonical_cognee_edge: false
    marketplace_only: true
    note: Derived parser helper edge from explicit ReconciliationSide.amount_columns field.
    original_edge_type: USES_AMOUNT_COLUMN
    column_role: amount
    edge_properties:
      column_role: amount
    canonical_edge_type: USES_COLUMN
    legacy_edge_aliases:
    - side_uses_amount_column
    inverse_edge_type: USED_BY_RECONCILIATION_SIDE
    materialize_inverse: false
    edge_class: parser_helper
    source_type: reconciliation_side
    target_type: column
```

```yaml
candidate_edge:
  edge_id: edge.reconciliation_side.flipkart.commission_detail_expected.uses_table.table.flipkart.commission
  edge_type: USES_TABLE
  source: reconciliation_side.flipkart.commission_detail_expected
  target: table.flipkart.commission
  fields:
    edge_family: reconciliation_understanding_derived
    evidence_basis: reconciliation_side.fields.source_table
    confidence: high
    canonical_cognee_edge: false
    marketplace_only: true
    note: Derived parser helper edge from explicit ReconciliationSide.source_table field.
    canonical_edge_type: USES_TABLE
    legacy_edge_aliases:
    - side_uses_table
    inverse_edge_type: USED_BY_RECONCILIATION_SIDE
    materialize_inverse: false
    edge_class: parser_helper
    source_type: reconciliation_side
    target_type: table
```

```yaml
candidate_edge:
  edge_id: edge.reconciliation_side.flipkart.commission_detail_expected.uses_column.column.commission.order_id.role_key
  edge_type: USES_COLUMN
  source: reconciliation_side.flipkart.commission_detail_expected
  target: column.commission.order_id
  fields:
    edge_family: reconciliation_understanding_derived
    evidence_basis: reconciliation_side.fields.key_columns
    confidence: high
    canonical_cognee_edge: false
    marketplace_only: true
    note: Derived parser helper edge from explicit ReconciliationSide.key_columns field.
    original_edge_type: USES_KEY_COLUMN
    column_role: key
    edge_properties:
      column_role: key
    canonical_edge_type: USES_COLUMN
    legacy_edge_aliases:
    - side_uses_key_column
    inverse_edge_type: USED_BY_RECONCILIATION_SIDE
    materialize_inverse: false
    edge_class: parser_helper
    source_type: reconciliation_side
    target_type: column
```

```yaml
candidate_edge:
  edge_id: edge.reconciliation_side.flipkart.commission_detail_expected.uses_column.column.commission.item_id.role_key
  edge_type: USES_COLUMN
  source: reconciliation_side.flipkart.commission_detail_expected
  target: column.commission.item_id
  fields:
    edge_family: reconciliation_understanding_derived
    evidence_basis: reconciliation_side.fields.key_columns
    confidence: high
    canonical_cognee_edge: false
    marketplace_only: true
    note: Derived parser helper edge from explicit ReconciliationSide.key_columns field.
    original_edge_type: USES_KEY_COLUMN
    column_role: key
    edge_properties:
      column_role: key
    canonical_edge_type: USES_COLUMN
    legacy_edge_aliases:
    - side_uses_key_column
    inverse_edge_type: USED_BY_RECONCILIATION_SIDE
    materialize_inverse: false
    edge_class: parser_helper
    source_type: reconciliation_side
    target_type: column
```

```yaml
candidate_edge:
  edge_id: edge.reconciliation_side.flipkart.commission_detail_expected.uses_column.column.commission.charged_amount.role_amount
  edge_type: USES_COLUMN
  source: reconciliation_side.flipkart.commission_detail_expected
  target: column.commission.charged_amount
  fields:
    edge_family: reconciliation_understanding_derived
    evidence_basis: reconciliation_side.fields.amount_columns
    confidence: high
    canonical_cognee_edge: false
    marketplace_only: true
    note: Derived parser helper edge from explicit ReconciliationSide.amount_columns field.
    original_edge_type: USES_AMOUNT_COLUMN
    column_role: amount
    edge_properties:
      column_role: amount
    canonical_edge_type: USES_COLUMN
    legacy_edge_aliases:
    - side_uses_amount_column
    inverse_edge_type: USED_BY_RECONCILIATION_SIDE
    materialize_inverse: false
    edge_class: parser_helper
    source_type: reconciliation_side
    target_type: column
```

```yaml
candidate_edge:
  edge_id: edge.reconciliation_side.flipkart.commission_detail_expected.uses_column.column.commission.total_tax.role_amount
  edge_type: USES_COLUMN
  source: reconciliation_side.flipkart.commission_detail_expected
  target: column.commission.total_tax
  fields:
    edge_family: reconciliation_understanding_derived
    evidence_basis: reconciliation_side.fields.amount_columns
    confidence: high
    canonical_cognee_edge: false
    marketplace_only: true
    note: Derived parser helper edge from explicit ReconciliationSide.amount_columns field.
    original_edge_type: USES_AMOUNT_COLUMN
    column_role: amount
    edge_properties:
      column_role: amount
    canonical_edge_type: USES_COLUMN
    legacy_edge_aliases:
    - side_uses_amount_column
    inverse_edge_type: USED_BY_RECONCILIATION_SIDE
    materialize_inverse: false
    edge_class: parser_helper
    source_type: reconciliation_side
    target_type: column
```

```yaml
candidate_edge:
  edge_id: edge.reconciliation_side.flipkart.cashback_expected.uses_table.table.flipkart.cashback
  edge_type: USES_TABLE
  source: reconciliation_side.flipkart.cashback_expected
  target: table.flipkart.cashback
  fields:
    edge_family: reconciliation_understanding_derived
    evidence_basis: reconciliation_side.fields.source_table
    confidence: high
    canonical_cognee_edge: false
    marketplace_only: true
    note: Derived parser helper edge from explicit ReconciliationSide.source_table field.
    canonical_edge_type: USES_TABLE
    legacy_edge_aliases:
    - side_uses_table
    inverse_edge_type: USED_BY_RECONCILIATION_SIDE
    materialize_inverse: false
    edge_class: parser_helper
    source_type: reconciliation_side
    target_type: table
```

```yaml
candidate_edge:
  edge_id: edge.reconciliation_side.flipkart.cashback_expected.uses_column.column.cashback.order_id.role_key
  edge_type: USES_COLUMN
  source: reconciliation_side.flipkart.cashback_expected
  target: column.cashback.order_id
  fields:
    edge_family: reconciliation_understanding_derived
    evidence_basis: reconciliation_side.fields.key_columns
    confidence: high
    canonical_cognee_edge: false
    marketplace_only: true
    note: Derived parser helper edge from explicit ReconciliationSide.key_columns field.
    original_edge_type: USES_KEY_COLUMN
    column_role: key
    edge_properties:
      column_role: key
    canonical_edge_type: USES_COLUMN
    legacy_edge_aliases:
    - side_uses_key_column
    inverse_edge_type: USED_BY_RECONCILIATION_SIDE
    materialize_inverse: false
    edge_class: parser_helper
    source_type: reconciliation_side
    target_type: column
```

```yaml
candidate_edge:
  edge_id: edge.reconciliation_side.flipkart.cashback_expected.uses_column.column.cashback.item_id.role_key
  edge_type: USES_COLUMN
  source: reconciliation_side.flipkart.cashback_expected
  target: column.cashback.item_id
  fields:
    edge_family: reconciliation_understanding_derived
    evidence_basis: reconciliation_side.fields.key_columns
    confidence: high
    canonical_cognee_edge: false
    marketplace_only: true
    note: Derived parser helper edge from explicit ReconciliationSide.key_columns field.
    original_edge_type: USES_KEY_COLUMN
    column_role: key
    edge_properties:
      column_role: key
    canonical_edge_type: USES_COLUMN
    legacy_edge_aliases:
    - side_uses_key_column
    inverse_edge_type: USED_BY_RECONCILIATION_SIDE
    materialize_inverse: false
    edge_class: parser_helper
    source_type: reconciliation_side
    target_type: column
```

```yaml
candidate_edge:
  edge_id: edge.reconciliation_side.flipkart.cashback_expected.uses_column.column.cashback.charged_amount.role_amount
  edge_type: USES_COLUMN
  source: reconciliation_side.flipkart.cashback_expected
  target: column.cashback.charged_amount
  fields:
    edge_family: reconciliation_understanding_derived
    evidence_basis: reconciliation_side.fields.amount_columns
    confidence: high
    canonical_cognee_edge: false
    marketplace_only: true
    note: Derived parser helper edge from explicit ReconciliationSide.amount_columns field.
    original_edge_type: USES_AMOUNT_COLUMN
    column_role: amount
    edge_properties:
      column_role: amount
    canonical_edge_type: USES_COLUMN
    legacy_edge_aliases:
    - side_uses_amount_column
    inverse_edge_type: USED_BY_RECONCILIATION_SIDE
    materialize_inverse: false
    edge_class: parser_helper
    source_type: reconciliation_side
    target_type: column
```

```yaml
candidate_edge:
  edge_id: edge.reconciliation_side.flipkart.settlement_offer_actual.uses_table.table.flipkart.settlement
  edge_type: USES_TABLE
  source: reconciliation_side.flipkart.settlement_offer_actual
  target: table.flipkart.settlement
  fields:
    edge_family: reconciliation_understanding_derived
    evidence_basis: reconciliation_side.fields.source_table
    confidence: high
    canonical_cognee_edge: false
    marketplace_only: true
    note: Derived parser helper edge from explicit ReconciliationSide.source_table field.
    canonical_edge_type: USES_TABLE
    legacy_edge_aliases:
    - side_uses_table
    inverse_edge_type: USED_BY_RECONCILIATION_SIDE
    materialize_inverse: false
    edge_class: parser_helper
    source_type: reconciliation_side
    target_type: table
```

```yaml
candidate_edge:
  edge_id: edge.reconciliation_side.flipkart.settlement_offer_actual.uses_column.column.settlement.order_id.role_key
  edge_type: USES_COLUMN
  source: reconciliation_side.flipkart.settlement_offer_actual
  target: column.settlement.order_id
  fields:
    edge_family: reconciliation_understanding_derived
    evidence_basis: reconciliation_side.fields.key_columns
    confidence: high
    canonical_cognee_edge: false
    marketplace_only: true
    note: Derived parser helper edge from explicit ReconciliationSide.key_columns field.
    original_edge_type: USES_KEY_COLUMN
    column_role: key
    edge_properties:
      column_role: key
    canonical_edge_type: USES_COLUMN
    legacy_edge_aliases:
    - side_uses_key_column
    inverse_edge_type: USED_BY_RECONCILIATION_SIDE
    materialize_inverse: false
    edge_class: parser_helper
    source_type: reconciliation_side
    target_type: column
```

```yaml
candidate_edge:
  edge_id: edge.reconciliation_side.flipkart.settlement_offer_actual.uses_column.column.settlement.item_id.role_key
  edge_type: USES_COLUMN
  source: reconciliation_side.flipkart.settlement_offer_actual
  target: column.settlement.item_id
  fields:
    edge_family: reconciliation_understanding_derived
    evidence_basis: reconciliation_side.fields.key_columns
    confidence: high
    canonical_cognee_edge: false
    marketplace_only: true
    note: Derived parser helper edge from explicit ReconciliationSide.key_columns field.
    original_edge_type: USES_KEY_COLUMN
    column_role: key
    edge_properties:
      column_role: key
    canonical_edge_type: USES_COLUMN
    legacy_edge_aliases:
    - side_uses_key_column
    inverse_edge_type: USED_BY_RECONCILIATION_SIDE
    materialize_inverse: false
    edge_class: parser_helper
    source_type: reconciliation_side
    target_type: column
```

```yaml
candidate_edge:
  edge_id: edge.reconciliation_side.flipkart.settlement_offer_actual.uses_column.column.settlement.offer_settled_amount.role_amount
  edge_type: USES_COLUMN
  source: reconciliation_side.flipkart.settlement_offer_actual
  target: column.settlement.offer_settled_amount
  fields:
    edge_family: reconciliation_understanding_derived
    evidence_basis: reconciliation_side.fields.amount_columns
    confidence: high
    canonical_cognee_edge: false
    marketplace_only: true
    note: Derived parser helper edge from explicit ReconciliationSide.amount_columns field.
    original_edge_type: USES_AMOUNT_COLUMN
    column_role: amount
    edge_properties:
      column_role: amount
    canonical_edge_type: USES_COLUMN
    legacy_edge_aliases:
    - side_uses_amount_column
    inverse_edge_type: USED_BY_RECONCILIATION_SIDE
    materialize_inverse: false
    edge_class: parser_helper
    source_type: reconciliation_side
    target_type: column
```

```yaml
candidate_edge:
  edge_id: edge.reconciliation_side.flipkart.settlement_offer_actual.uses_column.column.settlement.offer_adjustment_settled_amount.role_amount
  edge_type: USES_COLUMN
  source: reconciliation_side.flipkart.settlement_offer_actual
  target: column.settlement.offer_adjustment_settled_amount
  fields:
    edge_family: reconciliation_understanding_derived
    evidence_basis: reconciliation_side.fields.amount_columns
    confidence: high
    canonical_cognee_edge: false
    marketplace_only: true
    note: Derived parser helper edge from explicit ReconciliationSide.amount_columns field.
    original_edge_type: USES_AMOUNT_COLUMN
    column_role: amount
    edge_properties:
      column_role: amount
    canonical_edge_type: USES_COLUMN
    legacy_edge_aliases:
    - side_uses_amount_column
    inverse_edge_type: USED_BY_RECONCILIATION_SIDE
    materialize_inverse: false
    edge_class: parser_helper
    source_type: reconciliation_side
    target_type: column
```

```yaml
candidate_edge:
  edge_id: edge.reconciliation_side.flipkart.settlement_components.uses_table.table.flipkart.settlement
  edge_type: USES_TABLE
  source: reconciliation_side.flipkart.settlement_components
  target: table.flipkart.settlement
  fields:
    edge_family: reconciliation_understanding_derived
    evidence_basis: reconciliation_side.fields.source_table
    confidence: high
    canonical_cognee_edge: false
    marketplace_only: true
    note: Derived parser helper edge from explicit ReconciliationSide.source_table field.
    canonical_edge_type: USES_TABLE
    legacy_edge_aliases:
    - side_uses_table
    inverse_edge_type: USED_BY_RECONCILIATION_SIDE
    materialize_inverse: false
    edge_class: parser_helper
    source_type: reconciliation_side
    target_type: table
```

```yaml
candidate_edge:
  edge_id: edge.reconciliation_side.flipkart.settlement_components.uses_column.column.settlement.settlement_id.role_key
  edge_type: USES_COLUMN
  source: reconciliation_side.flipkart.settlement_components
  target: column.settlement.settlement_id
  fields:
    edge_family: reconciliation_understanding_derived
    evidence_basis: reconciliation_side.fields.key_columns
    confidence: high
    canonical_cognee_edge: false
    marketplace_only: true
    note: Derived parser helper edge from explicit ReconciliationSide.key_columns field.
    original_edge_type: USES_KEY_COLUMN
    column_role: key
    edge_properties:
      column_role: key
    canonical_edge_type: USES_COLUMN
    legacy_edge_aliases:
    - side_uses_key_column
    inverse_edge_type: USED_BY_RECONCILIATION_SIDE
    materialize_inverse: false
    edge_class: parser_helper
    source_type: reconciliation_side
    target_type: column
```

```yaml
candidate_edge:
  edge_id: edge.reconciliation_side.flipkart.settlement_components.uses_column.column.settlement.order_id.role_key
  edge_type: USES_COLUMN
  source: reconciliation_side.flipkart.settlement_components
  target: column.settlement.order_id
  fields:
    edge_family: reconciliation_understanding_derived
    evidence_basis: reconciliation_side.fields.key_columns
    confidence: high
    canonical_cognee_edge: false
    marketplace_only: true
    note: Derived parser helper edge from explicit ReconciliationSide.key_columns field.
    original_edge_type: USES_KEY_COLUMN
    column_role: key
    edge_properties:
      column_role: key
    canonical_edge_type: USES_COLUMN
    legacy_edge_aliases:
    - side_uses_key_column
    inverse_edge_type: USED_BY_RECONCILIATION_SIDE
    materialize_inverse: false
    edge_class: parser_helper
    source_type: reconciliation_side
    target_type: column
```

```yaml
candidate_edge:
  edge_id: edge.reconciliation_side.flipkart.settlement_components.uses_column.column.settlement.item_id.role_key
  edge_type: USES_COLUMN
  source: reconciliation_side.flipkart.settlement_components
  target: column.settlement.item_id
  fields:
    edge_family: reconciliation_understanding_derived
    evidence_basis: reconciliation_side.fields.key_columns
    confidence: high
    canonical_cognee_edge: false
    marketplace_only: true
    note: Derived parser helper edge from explicit ReconciliationSide.key_columns field.
    original_edge_type: USES_KEY_COLUMN
    column_role: key
    edge_properties:
      column_role: key
    canonical_edge_type: USES_COLUMN
    legacy_edge_aliases:
    - side_uses_key_column
    inverse_edge_type: USED_BY_RECONCILIATION_SIDE
    materialize_inverse: false
    edge_class: parser_helper
    source_type: reconciliation_side
    target_type: column
```

```yaml
candidate_edge:
  edge_id: edge.reconciliation_side.flipkart.settlement_components.uses_column.column.settlement.sale_settled_amount.role_amount
  edge_type: USES_COLUMN
  source: reconciliation_side.flipkart.settlement_components
  target: column.settlement.sale_settled_amount
  fields:
    edge_family: reconciliation_understanding_derived
    evidence_basis: reconciliation_side.fields.amount_columns
    confidence: high
    canonical_cognee_edge: false
    marketplace_only: true
    note: Derived parser helper edge from explicit ReconciliationSide.amount_columns field.
    original_edge_type: USES_AMOUNT_COLUMN
    column_role: amount
    edge_properties:
      column_role: amount
    canonical_edge_type: USES_COLUMN
    legacy_edge_aliases:
    - side_uses_amount_column
    inverse_edge_type: USED_BY_RECONCILIATION_SIDE
    materialize_inverse: false
    edge_class: parser_helper
    source_type: reconciliation_side
    target_type: column
```

```yaml
candidate_edge:
  edge_id: edge.reconciliation_side.flipkart.settlement_components.uses_column.column.settlement.refund_settled_amount.role_amount
  edge_type: USES_COLUMN
  source: reconciliation_side.flipkart.settlement_components
  target: column.settlement.refund_settled_amount
  fields:
    edge_family: reconciliation_understanding_derived
    evidence_basis: reconciliation_side.fields.amount_columns
    confidence: high
    canonical_cognee_edge: false
    marketplace_only: true
    note: Derived parser helper edge from explicit ReconciliationSide.amount_columns field.
    original_edge_type: USES_AMOUNT_COLUMN
    column_role: amount
    edge_properties:
      column_role: amount
    canonical_edge_type: USES_COLUMN
    legacy_edge_aliases:
    - side_uses_amount_column
    inverse_edge_type: USED_BY_RECONCILIATION_SIDE
    materialize_inverse: false
    edge_class: parser_helper
    source_type: reconciliation_side
    target_type: column
```

```yaml
candidate_edge:
  edge_id: edge.reconciliation_side.flipkart.settlement_components.uses_column.column.settlement.offer_settled_amount.role_amount
  edge_type: USES_COLUMN
  source: reconciliation_side.flipkart.settlement_components
  target: column.settlement.offer_settled_amount
  fields:
    edge_family: reconciliation_understanding_derived
    evidence_basis: reconciliation_side.fields.amount_columns
    confidence: high
    canonical_cognee_edge: false
    marketplace_only: true
    note: Derived parser helper edge from explicit ReconciliationSide.amount_columns field.
    original_edge_type: USES_AMOUNT_COLUMN
    column_role: amount
    edge_properties:
      column_role: amount
    canonical_edge_type: USES_COLUMN
    legacy_edge_aliases:
    - side_uses_amount_column
    inverse_edge_type: USED_BY_RECONCILIATION_SIDE
    materialize_inverse: false
    edge_class: parser_helper
    source_type: reconciliation_side
    target_type: column
```

```yaml
candidate_edge:
  edge_id: edge.reconciliation_side.flipkart.settlement_components.uses_column.column.settlement.mp_fee.role_amount
  edge_type: USES_COLUMN
  source: reconciliation_side.flipkart.settlement_components
  target: column.settlement.mp_fee
  fields:
    edge_family: reconciliation_understanding_derived
    evidence_basis: reconciliation_side.fields.amount_columns
    confidence: high
    canonical_cognee_edge: false
    marketplace_only: true
    note: Derived parser helper edge from explicit ReconciliationSide.amount_columns field.
    original_edge_type: USES_AMOUNT_COLUMN
    column_role: amount
    edge_properties:
      column_role: amount
    canonical_edge_type: USES_COLUMN
    legacy_edge_aliases:
    - side_uses_amount_column
    inverse_edge_type: USED_BY_RECONCILIATION_SIDE
    materialize_inverse: false
    edge_class: parser_helper
    source_type: reconciliation_side
    target_type: column
```

```yaml
candidate_edge:
  edge_id: edge.reconciliation_side.flipkart.settlement_components.uses_column.column.settlement.gst_on_mp_fees.role_amount
  edge_type: USES_COLUMN
  source: reconciliation_side.flipkart.settlement_components
  target: column.settlement.gst_on_mp_fees
  fields:
    edge_family: reconciliation_understanding_derived
    evidence_basis: reconciliation_side.fields.amount_columns
    confidence: high
    canonical_cognee_edge: false
    marketplace_only: true
    note: Derived parser helper edge from explicit ReconciliationSide.amount_columns field.
    original_edge_type: USES_AMOUNT_COLUMN
    column_role: amount
    edge_properties:
      column_role: amount
    canonical_edge_type: USES_COLUMN
    legacy_edge_aliases:
    - side_uses_amount_column
    inverse_edge_type: USED_BY_RECONCILIATION_SIDE
    materialize_inverse: false
    edge_class: parser_helper
    source_type: reconciliation_side
    target_type: column
```

```yaml
candidate_edge:
  edge_id: edge.reconciliation_side.flipkart.settlement_components.uses_column.column.settlement.total_tcs_amount.role_amount
  edge_type: USES_COLUMN
  source: reconciliation_side.flipkart.settlement_components
  target: column.settlement.total_tcs_amount
  fields:
    edge_family: reconciliation_understanding_derived
    evidence_basis: reconciliation_side.fields.amount_columns
    confidence: high
    canonical_cognee_edge: false
    marketplace_only: true
    note: Derived parser helper edge from explicit ReconciliationSide.amount_columns field.
    original_edge_type: USES_AMOUNT_COLUMN
    column_role: amount
    edge_properties:
      column_role: amount
    canonical_edge_type: USES_COLUMN
    legacy_edge_aliases:
    - side_uses_amount_column
    inverse_edge_type: USED_BY_RECONCILIATION_SIDE
    materialize_inverse: false
    edge_class: parser_helper
    source_type: reconciliation_side
    target_type: column
```

```yaml
candidate_edge:
  edge_id: edge.reconciliation_side.flipkart.settlement_components.uses_column.column.settlement.total_tds_amount.role_amount
  edge_type: USES_COLUMN
  source: reconciliation_side.flipkart.settlement_components
  target: column.settlement.total_tds_amount
  fields:
    edge_family: reconciliation_understanding_derived
    evidence_basis: reconciliation_side.fields.amount_columns
    confidence: high
    canonical_cognee_edge: false
    marketplace_only: true
    note: Derived parser helper edge from explicit ReconciliationSide.amount_columns field.
    original_edge_type: USES_AMOUNT_COLUMN
    column_role: amount
    edge_properties:
      column_role: amount
    canonical_edge_type: USES_COLUMN
    legacy_edge_aliases:
    - side_uses_amount_column
    inverse_edge_type: USED_BY_RECONCILIATION_SIDE
    materialize_inverse: false
    edge_class: parser_helper
    source_type: reconciliation_side
    target_type: column
```

```yaml
candidate_edge:
  edge_id: edge.reconciliation_side.flipkart.settlement_net.uses_table.table.flipkart.settlement
  edge_type: USES_TABLE
  source: reconciliation_side.flipkart.settlement_net
  target: table.flipkart.settlement
  fields:
    edge_family: reconciliation_understanding_derived
    evidence_basis: reconciliation_side.fields.source_table
    confidence: high
    canonical_cognee_edge: false
    marketplace_only: true
    note: Derived parser helper edge from explicit ReconciliationSide.source_table field.
    canonical_edge_type: USES_TABLE
    legacy_edge_aliases:
    - side_uses_table
    inverse_edge_type: USED_BY_RECONCILIATION_SIDE
    materialize_inverse: false
    edge_class: parser_helper
    source_type: reconciliation_side
    target_type: table
```

```yaml
candidate_edge:
  edge_id: edge.reconciliation_side.flipkart.settlement_net.uses_column.column.settlement.settlement_id.role_key
  edge_type: USES_COLUMN
  source: reconciliation_side.flipkart.settlement_net
  target: column.settlement.settlement_id
  fields:
    edge_family: reconciliation_understanding_derived
    evidence_basis: reconciliation_side.fields.key_columns
    confidence: high
    canonical_cognee_edge: false
    marketplace_only: true
    note: Derived parser helper edge from explicit ReconciliationSide.key_columns field.
    original_edge_type: USES_KEY_COLUMN
    column_role: key
    edge_properties:
      column_role: key
    canonical_edge_type: USES_COLUMN
    legacy_edge_aliases:
    - side_uses_key_column
    inverse_edge_type: USED_BY_RECONCILIATION_SIDE
    materialize_inverse: false
    edge_class: parser_helper
    source_type: reconciliation_side
    target_type: column
```

```yaml
candidate_edge:
  edge_id: edge.reconciliation_side.flipkart.settlement_net.uses_column.column.settlement.order_id.role_key
  edge_type: USES_COLUMN
  source: reconciliation_side.flipkart.settlement_net
  target: column.settlement.order_id
  fields:
    edge_family: reconciliation_understanding_derived
    evidence_basis: reconciliation_side.fields.key_columns
    confidence: high
    canonical_cognee_edge: false
    marketplace_only: true
    note: Derived parser helper edge from explicit ReconciliationSide.key_columns field.
    original_edge_type: USES_KEY_COLUMN
    column_role: key
    edge_properties:
      column_role: key
    canonical_edge_type: USES_COLUMN
    legacy_edge_aliases:
    - side_uses_key_column
    inverse_edge_type: USED_BY_RECONCILIATION_SIDE
    materialize_inverse: false
    edge_class: parser_helper
    source_type: reconciliation_side
    target_type: column
```

```yaml
candidate_edge:
  edge_id: edge.reconciliation_side.flipkart.settlement_net.uses_column.column.settlement.item_id.role_key
  edge_type: USES_COLUMN
  source: reconciliation_side.flipkart.settlement_net
  target: column.settlement.item_id
  fields:
    edge_family: reconciliation_understanding_derived
    evidence_basis: reconciliation_side.fields.key_columns
    confidence: high
    canonical_cognee_edge: false
    marketplace_only: true
    note: Derived parser helper edge from explicit ReconciliationSide.key_columns field.
    original_edge_type: USES_KEY_COLUMN
    column_role: key
    edge_properties:
      column_role: key
    canonical_edge_type: USES_COLUMN
    legacy_edge_aliases:
    - side_uses_key_column
    inverse_edge_type: USED_BY_RECONCILIATION_SIDE
    materialize_inverse: false
    edge_class: parser_helper
    source_type: reconciliation_side
    target_type: column
```

```yaml
candidate_edge:
  edge_id: edge.reconciliation_side.flipkart.settlement_net.uses_column.column.settlement.settled_amount.role_amount
  edge_type: USES_COLUMN
  source: reconciliation_side.flipkart.settlement_net
  target: column.settlement.settled_amount
  fields:
    edge_family: reconciliation_understanding_derived
    evidence_basis: reconciliation_side.fields.amount_columns
    confidence: high
    canonical_cognee_edge: false
    marketplace_only: true
    note: Derived parser helper edge from explicit ReconciliationSide.amount_columns field.
    original_edge_type: USES_AMOUNT_COLUMN
    column_role: amount
    edge_properties:
      column_role: amount
    canonical_edge_type: USES_COLUMN
    legacy_edge_aliases:
    - side_uses_amount_column
    inverse_edge_type: USED_BY_RECONCILIATION_SIDE
    materialize_inverse: false
    edge_class: parser_helper
    source_type: reconciliation_side
    target_type: column
```

```yaml
candidate_edge:
  edge_id: edge.reconciliation_profile.flipkart.cross_table_pipeline.has_reconciliation_side.reconciliation_side.flipkart.settlement_pipeline_actual
  edge_type: HAS_RECONCILIATION_SIDE
  source: reconciliation_profile.flipkart.cross_table_pipeline
  target: reconciliation_side.flipkart.settlement_pipeline_actual
  fields:
    edge_family: reconciliation_understanding
    evidence_basis: reconciliation_side.fields.profile_id
    confidence: high
    canonical_cognee_edge: true
    marketplace_only: true
    canonical_edge_type: HAS_RECONCILIATION_SIDE
    inverse_edge_type: BELONGS_TO_RECONCILIATION_PROFILE
    materialize_inverse: true
    edge_class: canonical
    source_type: reconciliation_profile
    target_type: reconciliation_side
```

```yaml
candidate_edge:
  edge_id: edge.reconciliation_side.flipkart.settlement_pipeline_actual.uses_table.table.flipkart.settlement
  edge_type: USES_TABLE
  source: reconciliation_side.flipkart.settlement_pipeline_actual
  target: table.flipkart.settlement
  fields:
    edge_family: reconciliation_understanding_derived
    evidence_basis: reconciliation_side.fields.source_table
    confidence: high
    canonical_cognee_edge: false
    marketplace_only: true
    note: Derived parser helper edge from explicit ReconciliationSide.source_table field.
    canonical_edge_type: USES_TABLE
    legacy_edge_aliases:
    - side_uses_table
    inverse_edge_type: USED_BY_RECONCILIATION_SIDE
    materialize_inverse: false
    edge_class: parser_helper
    source_type: reconciliation_side
    target_type: table
```

```yaml
candidate_edge:
  edge_id: edge.reconciliation_side.flipkart.settlement_pipeline_actual.uses_column.column.settlement.order_id.role_key
  edge_type: USES_COLUMN
  source: reconciliation_side.flipkart.settlement_pipeline_actual
  target: column.settlement.order_id
  fields:
    edge_family: reconciliation_understanding_derived
    evidence_basis: reconciliation_side.fields.key_columns
    confidence: high
    canonical_cognee_edge: false
    marketplace_only: true
    note: Derived parser helper edge from explicit ReconciliationSide.key_columns field.
    original_edge_type: USES_KEY_COLUMN
    column_role: key
    edge_properties:
      column_role: key
    canonical_edge_type: USES_COLUMN
    legacy_edge_aliases:
    - side_uses_key_column
    inverse_edge_type: USED_BY_RECONCILIATION_SIDE
    materialize_inverse: false
    edge_class: parser_helper
    source_type: reconciliation_side
    target_type: column
```

```yaml
candidate_edge:
  edge_id: edge.reconciliation_side.flipkart.settlement_pipeline_actual.uses_column.column.settlement.item_id.role_key
  edge_type: USES_COLUMN
  source: reconciliation_side.flipkart.settlement_pipeline_actual
  target: column.settlement.item_id
  fields:
    edge_family: reconciliation_understanding_derived
    evidence_basis: reconciliation_side.fields.key_columns
    confidence: high
    canonical_cognee_edge: false
    marketplace_only: true
    note: Derived parser helper edge from explicit ReconciliationSide.key_columns field.
    original_edge_type: USES_KEY_COLUMN
    column_role: key
    edge_properties:
      column_role: key
    canonical_edge_type: USES_COLUMN
    legacy_edge_aliases:
    - side_uses_key_column
    inverse_edge_type: USED_BY_RECONCILIATION_SIDE
    materialize_inverse: false
    edge_class: parser_helper
    source_type: reconciliation_side
    target_type: column
```

```yaml
candidate_edge:
  edge_id: edge.reconciliation_side.flipkart.settlement_pipeline_actual.uses_column.column.settlement.settled_amount.role_amount
  edge_type: USES_COLUMN
  source: reconciliation_side.flipkart.settlement_pipeline_actual
  target: column.settlement.settled_amount
  fields:
    edge_family: reconciliation_understanding_derived
    evidence_basis: reconciliation_side.fields.amount_columns
    confidence: high
    canonical_cognee_edge: false
    marketplace_only: true
    note: Derived parser helper edge from explicit ReconciliationSide.amount_columns field.
    original_edge_type: USES_AMOUNT_COLUMN
    column_role: amount
    edge_properties:
      column_role: amount
    canonical_edge_type: USES_COLUMN
    legacy_edge_aliases:
    - side_uses_amount_column
    inverse_edge_type: USED_BY_RECONCILIATION_SIDE
    materialize_inverse: false
    edge_class: parser_helper
    source_type: reconciliation_side
    target_type: column
```

```yaml
candidate_edge:
  edge_id: edge.matching_logic.flipkart.oms_settlement.supports_reconciliation_profile.reconciliation_profile.flipkart.oms_settlement
  edge_type: SUPPORTS_RECONCILIATION_PROFILE
  source: matching_logic.flipkart.oms_settlement
  target: reconciliation_profile.flipkart.oms_settlement
  fields:
    edge_family: reconciliation_understanding
    evidence_basis: matching_logic.fields.profile_id
    confidence: high
    canonical_cognee_edge: true
    marketplace_only: true
    canonical_edge_type: SUPPORTS_RECONCILIATION_PROFILE
    inverse_edge_type: USES_MATCHING_LOGIC
    materialize_inverse: true
    edge_class: canonical
    source_type: matching_logic
    target_type: reconciliation_profile
```

```yaml
candidate_edge:
  edge_id: edge.matching_logic.flipkart.settlement_commission_od_normalized.supports_reconciliation_profile.reconciliation_profile.flipkart.settlement_commission
  edge_type: SUPPORTS_RECONCILIATION_PROFILE
  source: matching_logic.flipkart.settlement_commission_od_normalized
  target: reconciliation_profile.flipkart.settlement_commission
  fields:
    edge_family: reconciliation_understanding
    evidence_basis: matching_logic.fields.profile_id
    confidence: high
    canonical_cognee_edge: true
    marketplace_only: true
    canonical_edge_type: SUPPORTS_RECONCILIATION_PROFILE
    inverse_edge_type: USES_MATCHING_LOGIC
    materialize_inverse: true
    edge_class: canonical
    source_type: matching_logic
    target_type: reconciliation_profile
```

```yaml
candidate_edge:
  edge_id: edge.matching_logic.flipkart.cashback_settlement_offer.supports_reconciliation_profile.reconciliation_profile.flipkart.cashback_settlement_offer
  edge_type: SUPPORTS_RECONCILIATION_PROFILE
  source: matching_logic.flipkart.cashback_settlement_offer
  target: reconciliation_profile.flipkart.cashback_settlement_offer
  fields:
    edge_family: reconciliation_understanding
    evidence_basis: matching_logic.fields.profile_id
    confidence: high
    canonical_cognee_edge: true
    marketplace_only: true
    canonical_edge_type: SUPPORTS_RECONCILIATION_PROFILE
    inverse_edge_type: USES_MATCHING_LOGIC
    materialize_inverse: true
    edge_class: canonical
    source_type: matching_logic
    target_type: reconciliation_profile
```

```yaml
candidate_edge:
  edge_id: edge.matching_logic.flipkart.settlement_waterfall.supports_reconciliation_profile.reconciliation_profile.flipkart.settlement_waterfall
  edge_type: SUPPORTS_RECONCILIATION_PROFILE
  source: matching_logic.flipkart.settlement_waterfall
  target: reconciliation_profile.flipkart.settlement_waterfall
  fields:
    edge_family: reconciliation_understanding
    evidence_basis: matching_logic.fields.profile_id
    confidence: high
    canonical_cognee_edge: true
    marketplace_only: true
    canonical_edge_type: SUPPORTS_RECONCILIATION_PROFILE
    inverse_edge_type: USES_MATCHING_LOGIC
    materialize_inverse: true
    edge_class: canonical
    source_type: matching_logic
    target_type: reconciliation_profile
```

```yaml
candidate_edge:
  edge_id: edge.matching_logic.flipkart.cross_table_pipeline.supports_reconciliation_profile.reconciliation_profile.flipkart.cross_table_pipeline
  edge_type: SUPPORTS_RECONCILIATION_PROFILE
  source: matching_logic.flipkart.cross_table_pipeline
  target: reconciliation_profile.flipkart.cross_table_pipeline
  fields:
    edge_family: reconciliation_understanding
    evidence_basis: matching_logic.fields.profile_id
    confidence: high
    canonical_cognee_edge: true
    marketplace_only: true
    canonical_edge_type: SUPPORTS_RECONCILIATION_PROFILE
    inverse_edge_type: USES_MATCHING_LOGIC
    materialize_inverse: true
    edge_class: canonical
    source_type: matching_logic
    target_type: reconciliation_profile
```

```yaml
candidate_edge:
  edge_id: edge.reconciliation_variant.flipkart.commission_od_normalized.extends_reconciliation_profile.reconciliation_profile.flipkart.settlement_commission
  edge_type: EXTENDS_RECONCILIATION_PROFILE
  source: reconciliation_variant.flipkart.commission_od_normalized
  target: reconciliation_profile.flipkart.settlement_commission
  fields:
    edge_family: reconciliation_understanding
    evidence_basis: reconciliation_variant.fields.base_profile
    confidence: high
    canonical_cognee_edge: true
    marketplace_only: true
    canonical_edge_type: EXTENDS_RECONCILIATION_PROFILE
    inverse_edge_type: HAS_RECONCILIATION_VARIANT
    materialize_inverse: false
    edge_class: canonical
    source_type: reconciliation_variant
    target_type: reconciliation_profile
```

```yaml
candidate_edge:
  edge_id: edge.reconciliation_variant.flipkart.cashback_offer_adjustment.extends_reconciliation_profile.reconciliation_profile.flipkart.cashback_settlement_offer
  edge_type: EXTENDS_RECONCILIATION_PROFILE
  source: reconciliation_variant.flipkart.cashback_offer_adjustment
  target: reconciliation_profile.flipkart.cashback_settlement_offer
  fields:
    edge_family: reconciliation_understanding
    evidence_basis: reconciliation_variant.fields.base_profile
    confidence: high
    canonical_cognee_edge: true
    marketplace_only: true
    canonical_edge_type: EXTENDS_RECONCILIATION_PROFILE
    inverse_edge_type: HAS_RECONCILIATION_VARIANT
    materialize_inverse: false
    edge_class: canonical
    source_type: reconciliation_variant
    target_type: reconciliation_profile
```

```yaml
candidate_edge:
  edge_id: edge.reconciliation_variant.flipkart.settlement_waterfall_same_row.extends_reconciliation_profile.reconciliation_profile.flipkart.settlement_waterfall
  edge_type: EXTENDS_RECONCILIATION_PROFILE
  source: reconciliation_variant.flipkart.settlement_waterfall_same_row
  target: reconciliation_profile.flipkart.settlement_waterfall
  fields:
    edge_family: reconciliation_understanding
    evidence_basis: reconciliation_variant.fields.base_profile
    confidence: high
    canonical_cognee_edge: true
    marketplace_only: true
    canonical_edge_type: EXTENDS_RECONCILIATION_PROFILE
    inverse_edge_type: HAS_RECONCILIATION_VARIANT
    materialize_inverse: false
    edge_class: canonical
    source_type: reconciliation_variant
    target_type: reconciliation_profile
```

```yaml
candidate_edge:
  edge_id: edge.reconciliation_variant.flipkart.shopsy_zero_commission.extends_reconciliation_profile.reconciliation_profile.flipkart.settlement_commission
  edge_type: EXTENDS_RECONCILIATION_PROFILE
  source: reconciliation_variant.flipkart.shopsy_zero_commission
  target: reconciliation_profile.flipkart.settlement_commission
  fields:
    edge_family: reconciliation_understanding
    evidence_basis: reconciliation_variant.fields.base_profile
    confidence: high
    canonical_cognee_edge: true
    marketplace_only: true
    canonical_edge_type: EXTENDS_RECONCILIATION_PROFILE
    inverse_edge_type: HAS_RECONCILIATION_VARIANT
    materialize_inverse: false
    edge_class: canonical
    source_type: reconciliation_variant
    target_type: reconciliation_profile
```

```yaml
candidate_edge:
  edge_id: edge.business_process.flipkart.forward_order_to_settlement.has_reconciliation_profile.reconciliation_profile.flipkart.oms_settlement
  edge_type: HAS_RECONCILIATION_PROFILE
  source: business_process.flipkart.forward_order_to_settlement
  target: reconciliation_profile.flipkart.oms_settlement
  fields:
    edge_family: reconciliation_understanding
    evidence_basis: deterministic process/profile semantic mapping
    confidence: high
    canonical_cognee_edge: true
    marketplace_only: true
    canonical_edge_type: HAS_RECONCILIATION_PROFILE
    inverse_edge_type: SUPPORTS_PROCESS
    materialize_inverse: true
    edge_class: canonical
    source_type: business_process
    target_type: reconciliation_profile
```

```yaml
candidate_edge:
  edge_id: edge.reconciliation_profile.flipkart.oms_settlement.supports_process.business_process.flipkart.forward_order_to_settlement
  edge_type: SUPPORTS_PROCESS
  source: reconciliation_profile.flipkart.oms_settlement
  target: business_process.flipkart.forward_order_to_settlement
  fields:
    edge_family: reconciliation_understanding
    evidence_basis: deterministic process/profile semantic mapping
    confidence: high
    canonical_cognee_edge: true
    marketplace_only: true
    canonical_edge_type: SUPPORTS_PROCESS
    inverse_edge_type: HAS_RECONCILIATION_PROFILE
    materialize_inverse: true
    edge_class: canonical
    source_type: reconciliation_profile
    target_type: business_process
```

```yaml
candidate_edge:
  edge_id: edge.business_process.flipkart.commission_fee_invoice.has_reconciliation_profile.reconciliation_profile.flipkart.settlement_commission
  edge_type: HAS_RECONCILIATION_PROFILE
  source: business_process.flipkart.commission_fee_invoice
  target: reconciliation_profile.flipkart.settlement_commission
  fields:
    edge_family: reconciliation_understanding
    evidence_basis: deterministic process/profile semantic mapping
    confidence: high
    canonical_cognee_edge: true
    marketplace_only: true
    canonical_edge_type: HAS_RECONCILIATION_PROFILE
    inverse_edge_type: SUPPORTS_PROCESS
    materialize_inverse: true
    edge_class: canonical
    source_type: business_process
    target_type: reconciliation_profile
```

```yaml
candidate_edge:
  edge_id: edge.reconciliation_profile.flipkart.settlement_commission.supports_process.business_process.flipkart.commission_fee_invoice
  edge_type: SUPPORTS_PROCESS
  source: reconciliation_profile.flipkart.settlement_commission
  target: business_process.flipkart.commission_fee_invoice
  fields:
    edge_family: reconciliation_understanding
    evidence_basis: deterministic process/profile semantic mapping
    confidence: high
    canonical_cognee_edge: true
    marketplace_only: true
    canonical_edge_type: SUPPORTS_PROCESS
    inverse_edge_type: HAS_RECONCILIATION_PROFILE
    materialize_inverse: true
    edge_class: canonical
    source_type: reconciliation_profile
    target_type: business_process
```

```yaml
candidate_edge:
  edge_id: edge.business_process.flipkart.cashback_credit_debit_note.has_reconciliation_profile.reconciliation_profile.flipkart.cashback_settlement_offer
  edge_type: HAS_RECONCILIATION_PROFILE
  source: business_process.flipkart.cashback_credit_debit_note
  target: reconciliation_profile.flipkart.cashback_settlement_offer
  fields:
    edge_family: reconciliation_understanding
    evidence_basis: deterministic process/profile semantic mapping
    confidence: high
    canonical_cognee_edge: true
    marketplace_only: true
    canonical_edge_type: HAS_RECONCILIATION_PROFILE
    inverse_edge_type: SUPPORTS_PROCESS
    materialize_inverse: true
    edge_class: canonical
    source_type: business_process
    target_type: reconciliation_profile
```

```yaml
candidate_edge:
  edge_id: edge.reconciliation_profile.flipkart.cashback_settlement_offer.supports_process.business_process.flipkart.cashback_credit_debit_note
  edge_type: SUPPORTS_PROCESS
  source: reconciliation_profile.flipkart.cashback_settlement_offer
  target: business_process.flipkart.cashback_credit_debit_note
  fields:
    edge_family: reconciliation_understanding
    evidence_basis: deterministic process/profile semantic mapping
    confidence: high
    canonical_cognee_edge: true
    marketplace_only: true
    canonical_edge_type: SUPPORTS_PROCESS
    inverse_edge_type: HAS_RECONCILIATION_PROFILE
    materialize_inverse: true
    edge_class: canonical
    source_type: reconciliation_profile
    target_type: business_process
```

```yaml
candidate_edge:
  edge_id: edge.business_process.flipkart.marketplace_reconciliation_pipeline.has_reconciliation_profile.reconciliation_profile.flipkart.settlement_waterfall
  edge_type: HAS_RECONCILIATION_PROFILE
  source: business_process.flipkart.marketplace_reconciliation_pipeline
  target: reconciliation_profile.flipkart.settlement_waterfall
  fields:
    edge_family: reconciliation_understanding
    evidence_basis: deterministic process/profile semantic mapping
    confidence: high
    canonical_cognee_edge: true
    marketplace_only: true
    canonical_edge_type: HAS_RECONCILIATION_PROFILE
    inverse_edge_type: SUPPORTS_PROCESS
    materialize_inverse: true
    edge_class: canonical
    source_type: business_process
    target_type: reconciliation_profile
```

```yaml
candidate_edge:
  edge_id: edge.reconciliation_profile.flipkart.settlement_waterfall.supports_process.business_process.flipkart.marketplace_reconciliation_pipeline
  edge_type: SUPPORTS_PROCESS
  source: reconciliation_profile.flipkart.settlement_waterfall
  target: business_process.flipkart.marketplace_reconciliation_pipeline
  fields:
    edge_family: reconciliation_understanding
    evidence_basis: deterministic process/profile semantic mapping
    confidence: high
    canonical_cognee_edge: true
    marketplace_only: true
    canonical_edge_type: SUPPORTS_PROCESS
    inverse_edge_type: HAS_RECONCILIATION_PROFILE
    materialize_inverse: true
    edge_class: canonical
    source_type: reconciliation_profile
    target_type: business_process
```

```yaml
candidate_edge:
  edge_id: edge.business_process.flipkart.marketplace_reconciliation_pipeline.has_reconciliation_profile.reconciliation_profile.flipkart.cross_table_pipeline
  edge_type: HAS_RECONCILIATION_PROFILE
  source: business_process.flipkart.marketplace_reconciliation_pipeline
  target: reconciliation_profile.flipkart.cross_table_pipeline
  fields:
    edge_family: reconciliation_understanding
    evidence_basis: deterministic process/profile semantic mapping
    confidence: high
    canonical_cognee_edge: true
    marketplace_only: true
    canonical_edge_type: HAS_RECONCILIATION_PROFILE
    inverse_edge_type: SUPPORTS_PROCESS
    materialize_inverse: true
    edge_class: canonical
    source_type: business_process
    target_type: reconciliation_profile
```

```yaml
candidate_edge:
  edge_id: edge.reconciliation_profile.flipkart.cross_table_pipeline.supports_process.business_process.flipkart.marketplace_reconciliation_pipeline
  edge_type: SUPPORTS_PROCESS
  source: reconciliation_profile.flipkart.cross_table_pipeline
  target: business_process.flipkart.marketplace_reconciliation_pipeline
  fields:
    edge_family: reconciliation_understanding
    evidence_basis: deterministic process/profile semantic mapping
    confidence: high
    canonical_cognee_edge: true
    marketplace_only: true
    canonical_edge_type: SUPPORTS_PROCESS
    inverse_edge_type: HAS_RECONCILIATION_PROFILE
    materialize_inverse: true
    edge_class: canonical
    source_type: reconciliation_profile
    target_type: business_process
```

```yaml
candidate_edge:
  edge_id: edge.query_pattern.flipkart.gmv.uses_table.table.flipkart.oms
  edge_type: USES_TABLE
  source: query_pattern.flipkart.gmv
  target: table.flipkart.oms
  fields:
    edge_family: execution_guidance
    evidence_basis: query_pattern.fields.required_tables
    confidence: high
    canonical_cognee_edge: true
    marketplace_only: true
    canonical_edge_type: USES_TABLE
    legacy_edge_aliases:
    - query_requires_table
    inverse_edge_type: USED_BY_QUERY_PATTERN
    materialize_inverse: false
    edge_class: canonical
    source_type: query_pattern
    target_type: table
```

```yaml
candidate_edge:
  edge_id: edge.query_pattern.flipkart.gmv.uses_table.table.flipkart.settlement
  edge_type: USES_TABLE
  source: query_pattern.flipkart.gmv
  target: table.flipkart.settlement
  fields:
    edge_family: execution_guidance
    evidence_basis: query_pattern.fields.required_tables
    confidence: high
    canonical_cognee_edge: true
    marketplace_only: true
    canonical_edge_type: USES_TABLE
    legacy_edge_aliases:
    - query_requires_table
    inverse_edge_type: USED_BY_QUERY_PATTERN
    materialize_inverse: false
    edge_class: canonical
    source_type: query_pattern
    target_type: table
```

```yaml
candidate_edge:
  edge_id: edge.query_pattern.flipkart.gmv.produces_metric.metric.gross_merchandise_value
  edge_type: PRODUCES_METRIC
  source: query_pattern.flipkart.gmv
  target: metric.gross_merchandise_value
  fields:
    edge_family: execution_guidance
    evidence_basis: query_pattern.fields.canonical_metric_or_object
    confidence: high
    canonical_cognee_edge: true
    marketplace_only: true
    canonical_edge_type: PRODUCES_METRIC
    legacy_edge_aliases:
    - query_targets_card
    inverse_edge_type: PRODUCED_BY_QUERY_PATTERN
    materialize_inverse: false
    edge_class: canonical
    source_type: query_pattern
    target_type: metric
```

```yaml
candidate_edge:
  edge_id: edge.query_pattern.flipkart.gmv.uses_relationship.relationship.flipkart.oms_settlement
  edge_type: USES_RELATIONSHIP
  source: query_pattern.flipkart.gmv
  target: relationship.flipkart.oms_settlement
  fields:
    edge_family: execution_guidance_derived
    evidence_basis: query_pattern.fields.required_tables + relationship table pair
    confidence: high
    canonical_cognee_edge: true
    marketplace_only: true
    note: Derived parser helper edge. Cognee v4 §8.7 lists QueryPattern->Table/Metric/Reconciliation; this links the explicit join path when both tables are required.
    canonical_edge_type: USES_RELATIONSHIP
    inverse_edge_type: USED_BY_QUERY_PATTERN
    materialize_inverse: false
    edge_class: canonical
    source_type: query_pattern
    target_type: relationship
```

```yaml
candidate_edge:
  edge_id: edge.query_pattern.flipkart.gmv.requires_rule.rule.flipkart.active_filter
  edge_type: REQUIRES_RULE
  source: query_pattern.flipkart.gmv
  target: rule.flipkart.active_filter
  fields:
    edge_family: execution_guidance
    evidence_basis: query_pattern.fields.required_filters
    confidence: high
    canonical_cognee_edge: true
    marketplace_only: true
    canonical_edge_type: REQUIRES_RULE
    legacy_edge_aliases:
    - query_targets_card
    inverse_edge_type: REQUIRED_BY_QUERY_PATTERN
    materialize_inverse: false
    edge_class: canonical
    source_type: query_pattern
    target_type: rule
```

```yaml
candidate_edge:
  edge_id: edge.query_pattern.flipkart.gmv.has_validation_test.validation_test.flipkart.active_filter_present
  edge_type: HAS_VALIDATION_TEST
  source: query_pattern.flipkart.gmv
  target: validation_test.flipkart.active_filter_present
  fields:
    edge_family: execution_guidance
    evidence_basis: query_pattern.fields.required_filters
    confidence: high
    canonical_cognee_edge: true
    marketplace_only: true
    canonical_edge_type: HAS_VALIDATION_TEST
    legacy_edge_aliases:
    - query_targets_card
    inverse_edge_type: VALIDATES_QUERY_PATTERN
    materialize_inverse: false
    edge_class: canonical
    source_type: query_pattern
    target_type: validation_test
```

```yaml
candidate_edge:
  edge_id: edge.query_pattern.flipkart.net_settlement.uses_table.table.flipkart.settlement
  edge_type: USES_TABLE
  source: query_pattern.flipkart.net_settlement
  target: table.flipkart.settlement
  fields:
    edge_family: execution_guidance
    evidence_basis: query_pattern.fields.required_tables
    confidence: high
    canonical_cognee_edge: true
    marketplace_only: true
    canonical_edge_type: USES_TABLE
    legacy_edge_aliases:
    - query_requires_table
    inverse_edge_type: USED_BY_QUERY_PATTERN
    materialize_inverse: false
    edge_class: canonical
    source_type: query_pattern
    target_type: table
```

```yaml
candidate_edge:
  edge_id: edge.query_pattern.flipkart.net_settlement.produces_metric.metric.net_settlement
  edge_type: PRODUCES_METRIC
  source: query_pattern.flipkart.net_settlement
  target: metric.net_settlement
  fields:
    edge_family: execution_guidance
    evidence_basis: query_pattern.fields.canonical_metric_or_object
    confidence: high
    canonical_cognee_edge: true
    marketplace_only: true
    canonical_edge_type: PRODUCES_METRIC
    legacy_edge_aliases:
    - query_targets_card
    inverse_edge_type: PRODUCED_BY_QUERY_PATTERN
    materialize_inverse: false
    edge_class: canonical
    source_type: query_pattern
    target_type: metric
```

```yaml
candidate_edge:
  edge_id: edge.query_pattern.flipkart.net_settlement.requires_rule.rule.flipkart.active_filter
  edge_type: REQUIRES_RULE
  source: query_pattern.flipkart.net_settlement
  target: rule.flipkart.active_filter
  fields:
    edge_family: execution_guidance
    evidence_basis: query_pattern.fields.required_filters
    confidence: high
    canonical_cognee_edge: true
    marketplace_only: true
    canonical_edge_type: REQUIRES_RULE
    legacy_edge_aliases:
    - query_targets_card
    inverse_edge_type: REQUIRED_BY_QUERY_PATTERN
    materialize_inverse: false
    edge_class: canonical
    source_type: query_pattern
    target_type: rule
```

```yaml
candidate_edge:
  edge_id: edge.query_pattern.flipkart.net_settlement.has_validation_test.validation_test.flipkart.active_filter_present
  edge_type: HAS_VALIDATION_TEST
  source: query_pattern.flipkart.net_settlement
  target: validation_test.flipkart.active_filter_present
  fields:
    edge_family: execution_guidance
    evidence_basis: query_pattern.fields.required_filters
    confidence: high
    canonical_cognee_edge: true
    marketplace_only: true
    canonical_edge_type: HAS_VALIDATION_TEST
    legacy_edge_aliases:
    - query_targets_card
    inverse_edge_type: VALIDATES_QUERY_PATTERN
    materialize_inverse: false
    edge_class: canonical
    source_type: query_pattern
    target_type: validation_test
```

```yaml
candidate_edge:
  edge_id: edge.query_pattern.flipkart.realization.uses_table.table.flipkart.settlement
  edge_type: USES_TABLE
  source: query_pattern.flipkart.realization
  target: table.flipkart.settlement
  fields:
    edge_family: execution_guidance
    evidence_basis: query_pattern.fields.required_tables
    confidence: high
    canonical_cognee_edge: true
    marketplace_only: true
    canonical_edge_type: USES_TABLE
    legacy_edge_aliases:
    - query_requires_table
    inverse_edge_type: USED_BY_QUERY_PATTERN
    materialize_inverse: false
    edge_class: canonical
    source_type: query_pattern
    target_type: table
```

```yaml
candidate_edge:
  edge_id: edge.query_pattern.flipkart.realization.produces_metric.metric.realization_rate
  edge_type: PRODUCES_METRIC
  source: query_pattern.flipkart.realization
  target: metric.realization_rate
  fields:
    edge_family: execution_guidance
    evidence_basis: query_pattern.fields.canonical_metric_or_object
    confidence: high
    canonical_cognee_edge: true
    marketplace_only: true
    canonical_edge_type: PRODUCES_METRIC
    legacy_edge_aliases:
    - query_targets_card
    inverse_edge_type: PRODUCED_BY_QUERY_PATTERN
    materialize_inverse: false
    edge_class: canonical
    source_type: query_pattern
    target_type: metric
```

```yaml
candidate_edge:
  edge_id: edge.query_pattern.flipkart.realization.requires_rule.rule.flipkart.active_filter
  edge_type: REQUIRES_RULE
  source: query_pattern.flipkart.realization
  target: rule.flipkart.active_filter
  fields:
    edge_family: execution_guidance
    evidence_basis: query_pattern.fields.required_filters
    confidence: high
    canonical_cognee_edge: true
    marketplace_only: true
    canonical_edge_type: REQUIRES_RULE
    legacy_edge_aliases:
    - query_targets_card
    inverse_edge_type: REQUIRED_BY_QUERY_PATTERN
    materialize_inverse: false
    edge_class: canonical
    source_type: query_pattern
    target_type: rule
```

```yaml
candidate_edge:
  edge_id: edge.query_pattern.flipkart.realization.has_validation_test.validation_test.flipkart.active_filter_present
  edge_type: HAS_VALIDATION_TEST
  source: query_pattern.flipkart.realization
  target: validation_test.flipkart.active_filter_present
  fields:
    edge_family: execution_guidance
    evidence_basis: query_pattern.fields.required_filters
    confidence: high
    canonical_cognee_edge: true
    marketplace_only: true
    canonical_edge_type: HAS_VALIDATION_TEST
    legacy_edge_aliases:
    - query_targets_card
    inverse_edge_type: VALIDATES_QUERY_PATTERN
    materialize_inverse: false
    edge_class: canonical
    source_type: query_pattern
    target_type: validation_test
```

```yaml
candidate_edge:
  edge_id: edge.query_pattern.flipkart.settlement_by_fulfilment.uses_table.table.flipkart.settlement
  edge_type: USES_TABLE
  source: query_pattern.flipkart.settlement_by_fulfilment
  target: table.flipkart.settlement
  fields:
    edge_family: execution_guidance
    evidence_basis: query_pattern.fields.required_tables
    confidence: high
    canonical_cognee_edge: true
    marketplace_only: true
    canonical_edge_type: USES_TABLE
    legacy_edge_aliases:
    - query_requires_table
    inverse_edge_type: USED_BY_QUERY_PATTERN
    materialize_inverse: false
    edge_class: canonical
    source_type: query_pattern
    target_type: table
```

```yaml
candidate_edge:
  edge_id: edge.query_pattern.flipkart.settlement_by_fulfilment.produces_metric.metric.net_settlement
  edge_type: PRODUCES_METRIC
  source: query_pattern.flipkart.settlement_by_fulfilment
  target: metric.net_settlement
  fields:
    edge_family: execution_guidance
    evidence_basis: query_pattern.fields.canonical_metric_or_object
    confidence: high
    canonical_cognee_edge: true
    marketplace_only: true
    canonical_edge_type: PRODUCES_METRIC
    legacy_edge_aliases:
    - query_targets_card
    inverse_edge_type: PRODUCED_BY_QUERY_PATTERN
    materialize_inverse: false
    edge_class: canonical
    source_type: query_pattern
    target_type: metric
```

```yaml
candidate_edge:
  edge_id: edge.query_pattern.flipkart.settlement_by_fulfilment.requires_rule.rule.flipkart.active_filter
  edge_type: REQUIRES_RULE
  source: query_pattern.flipkart.settlement_by_fulfilment
  target: rule.flipkart.active_filter
  fields:
    edge_family: execution_guidance
    evidence_basis: query_pattern.fields.required_filters
    confidence: high
    canonical_cognee_edge: true
    marketplace_only: true
    canonical_edge_type: REQUIRES_RULE
    legacy_edge_aliases:
    - query_targets_card
    inverse_edge_type: REQUIRED_BY_QUERY_PATTERN
    materialize_inverse: false
    edge_class: canonical
    source_type: query_pattern
    target_type: rule
```

```yaml
candidate_edge:
  edge_id: edge.query_pattern.flipkart.settlement_by_fulfilment.has_validation_test.validation_test.flipkart.active_filter_present
  edge_type: HAS_VALIDATION_TEST
  source: query_pattern.flipkart.settlement_by_fulfilment
  target: validation_test.flipkart.active_filter_present
  fields:
    edge_family: execution_guidance
    evidence_basis: query_pattern.fields.required_filters
    confidence: high
    canonical_cognee_edge: true
    marketplace_only: true
    canonical_edge_type: HAS_VALIDATION_TEST
    legacy_edge_aliases:
    - query_targets_card
    inverse_edge_type: VALIDATES_QUERY_PATTERN
    materialize_inverse: false
    edge_class: canonical
    source_type: query_pattern
    target_type: validation_test
```

```yaml
candidate_edge:
  edge_id: edge.query_pattern.flipkart.settlement_cycle.uses_table.table.flipkart.settlement
  edge_type: USES_TABLE
  source: query_pattern.flipkart.settlement_cycle
  target: table.flipkart.settlement
  fields:
    edge_family: execution_guidance
    evidence_basis: query_pattern.fields.required_tables
    confidence: high
    canonical_cognee_edge: true
    marketplace_only: true
    canonical_edge_type: USES_TABLE
    legacy_edge_aliases:
    - query_requires_table
    inverse_edge_type: USED_BY_QUERY_PATTERN
    materialize_inverse: false
    edge_class: canonical
    source_type: query_pattern
    target_type: table
```

```yaml
candidate_edge:
  edge_id: edge.query_pattern.flipkart.settlement_cycle.produces_metric.metric.settlement_cycle_days
  edge_type: PRODUCES_METRIC
  source: query_pattern.flipkart.settlement_cycle
  target: metric.settlement_cycle_days
  fields:
    edge_family: execution_guidance
    evidence_basis: query_pattern.fields.canonical_metric_or_object
    confidence: high
    canonical_cognee_edge: true
    marketplace_only: true
    canonical_edge_type: PRODUCES_METRIC
    legacy_edge_aliases:
    - query_targets_card
    inverse_edge_type: PRODUCED_BY_QUERY_PATTERN
    materialize_inverse: false
    edge_class: canonical
    source_type: query_pattern
    target_type: metric
```

```yaml
candidate_edge:
  edge_id: edge.query_pattern.flipkart.settlement_cycle.requires_rule.rule.flipkart.active_filter
  edge_type: REQUIRES_RULE
  source: query_pattern.flipkart.settlement_cycle
  target: rule.flipkart.active_filter
  fields:
    edge_family: execution_guidance
    evidence_basis: query_pattern.fields.required_filters
    confidence: high
    canonical_cognee_edge: true
    marketplace_only: true
    canonical_edge_type: REQUIRES_RULE
    legacy_edge_aliases:
    - query_targets_card
    inverse_edge_type: REQUIRED_BY_QUERY_PATTERN
    materialize_inverse: false
    edge_class: canonical
    source_type: query_pattern
    target_type: rule
```

```yaml
candidate_edge:
  edge_id: edge.query_pattern.flipkart.settlement_cycle.has_validation_test.validation_test.flipkart.active_filter_present
  edge_type: HAS_VALIDATION_TEST
  source: query_pattern.flipkart.settlement_cycle
  target: validation_test.flipkart.active_filter_present
  fields:
    edge_family: execution_guidance
    evidence_basis: query_pattern.fields.required_filters
    confidence: high
    canonical_cognee_edge: true
    marketplace_only: true
    canonical_edge_type: HAS_VALIDATION_TEST
    legacy_edge_aliases:
    - query_targets_card
    inverse_edge_type: VALIDATES_QUERY_PATTERN
    materialize_inverse: false
    edge_class: canonical
    source_type: query_pattern
    target_type: validation_test
```

```yaml
candidate_edge:
  edge_id: edge.query_pattern.flipkart.fee_breakdown.uses_table.table.flipkart.commission
  edge_type: USES_TABLE
  source: query_pattern.flipkart.fee_breakdown
  target: table.flipkart.commission
  fields:
    edge_family: execution_guidance
    evidence_basis: query_pattern.fields.required_tables
    confidence: high
    canonical_cognee_edge: true
    marketplace_only: true
    canonical_edge_type: USES_TABLE
    legacy_edge_aliases:
    - query_requires_table
    inverse_edge_type: USED_BY_QUERY_PATTERN
    materialize_inverse: false
    edge_class: canonical
    source_type: query_pattern
    target_type: table
```

```yaml
candidate_edge:
  edge_id: edge.query_pattern.flipkart.fee_breakdown.produces_metric.metric.marketplace_fee_total
  edge_type: PRODUCES_METRIC
  source: query_pattern.flipkart.fee_breakdown
  target: metric.marketplace_fee_total
  fields:
    edge_family: execution_guidance
    evidence_basis: query_pattern.fields.canonical_metric_or_object
    confidence: high
    canonical_cognee_edge: true
    marketplace_only: true
    canonical_edge_type: PRODUCES_METRIC
    legacy_edge_aliases:
    - query_targets_card
    inverse_edge_type: PRODUCED_BY_QUERY_PATTERN
    materialize_inverse: false
    edge_class: canonical
    source_type: query_pattern
    target_type: metric
```

```yaml
candidate_edge:
  edge_id: edge.query_pattern.flipkart.fee_breakdown.requires_rule.rule.flipkart.active_filter
  edge_type: REQUIRES_RULE
  source: query_pattern.flipkart.fee_breakdown
  target: rule.flipkart.active_filter
  fields:
    edge_family: execution_guidance
    evidence_basis: query_pattern.fields.required_filters
    confidence: high
    canonical_cognee_edge: true
    marketplace_only: true
    canonical_edge_type: REQUIRES_RULE
    legacy_edge_aliases:
    - query_targets_card
    inverse_edge_type: REQUIRED_BY_QUERY_PATTERN
    materialize_inverse: false
    edge_class: canonical
    source_type: query_pattern
    target_type: rule
```

```yaml
candidate_edge:
  edge_id: edge.query_pattern.flipkart.fee_breakdown.has_validation_test.validation_test.flipkart.active_filter_present
  edge_type: HAS_VALIDATION_TEST
  source: query_pattern.flipkart.fee_breakdown
  target: validation_test.flipkart.active_filter_present
  fields:
    edge_family: execution_guidance
    evidence_basis: query_pattern.fields.required_filters
    confidence: high
    canonical_cognee_edge: true
    marketplace_only: true
    canonical_edge_type: HAS_VALIDATION_TEST
    legacy_edge_aliases:
    - query_targets_card
    inverse_edge_type: VALIDATES_QUERY_PATTERN
    materialize_inverse: false
    edge_class: canonical
    source_type: query_pattern
    target_type: validation_test
```

```yaml
candidate_edge:
  edge_id: edge.query_pattern.flipkart.fee_pivot.uses_table.table.flipkart.commission
  edge_type: USES_TABLE
  source: query_pattern.flipkart.fee_pivot
  target: table.flipkart.commission
  fields:
    edge_family: execution_guidance
    evidence_basis: query_pattern.fields.required_tables
    confidence: high
    canonical_cognee_edge: true
    marketplace_only: true
    canonical_edge_type: USES_TABLE
    legacy_edge_aliases:
    - query_requires_table
    inverse_edge_type: USED_BY_QUERY_PATTERN
    materialize_inverse: false
    edge_class: canonical
    source_type: query_pattern
    target_type: table
```

```yaml
candidate_edge:
  edge_id: edge.query_pattern.flipkart.fee_pivot.produces_metric.metric.marketplace_fee_total
  edge_type: PRODUCES_METRIC
  source: query_pattern.flipkart.fee_pivot
  target: metric.marketplace_fee_total
  fields:
    edge_family: execution_guidance
    evidence_basis: query_pattern.fields.canonical_metric_or_object
    confidence: high
    canonical_cognee_edge: true
    marketplace_only: true
    canonical_edge_type: PRODUCES_METRIC
    legacy_edge_aliases:
    - query_targets_card
    inverse_edge_type: PRODUCED_BY_QUERY_PATTERN
    materialize_inverse: false
    edge_class: canonical
    source_type: query_pattern
    target_type: metric
```

```yaml
candidate_edge:
  edge_id: edge.query_pattern.flipkart.fee_pivot.requires_rule.rule.flipkart.active_filter
  edge_type: REQUIRES_RULE
  source: query_pattern.flipkart.fee_pivot
  target: rule.flipkart.active_filter
  fields:
    edge_family: execution_guidance
    evidence_basis: query_pattern.fields.required_filters
    confidence: high
    canonical_cognee_edge: true
    marketplace_only: true
    canonical_edge_type: REQUIRES_RULE
    legacy_edge_aliases:
    - query_targets_card
    inverse_edge_type: REQUIRED_BY_QUERY_PATTERN
    materialize_inverse: false
    edge_class: canonical
    source_type: query_pattern
    target_type: rule
```

```yaml
candidate_edge:
  edge_id: edge.query_pattern.flipkart.fee_pivot.has_validation_test.validation_test.flipkart.active_filter_present
  edge_type: HAS_VALIDATION_TEST
  source: query_pattern.flipkart.fee_pivot
  target: validation_test.flipkart.active_filter_present
  fields:
    edge_family: execution_guidance
    evidence_basis: query_pattern.fields.required_filters
    confidence: high
    canonical_cognee_edge: true
    marketplace_only: true
    canonical_edge_type: HAS_VALIDATION_TEST
    legacy_edge_aliases:
    - query_targets_card
    inverse_edge_type: VALIDATES_QUERY_PATTERN
    materialize_inverse: false
    edge_class: canonical
    source_type: query_pattern
    target_type: validation_test
```

```yaml
candidate_edge:
  edge_id: edge.query_pattern.flipkart.commission_recon.uses_table.table.flipkart.settlement
  edge_type: USES_TABLE
  source: query_pattern.flipkart.commission_recon
  target: table.flipkart.settlement
  fields:
    edge_family: execution_guidance
    evidence_basis: query_pattern.fields.required_tables
    confidence: high
    canonical_cognee_edge: true
    marketplace_only: true
    canonical_edge_type: USES_TABLE
    legacy_edge_aliases:
    - query_requires_table
    inverse_edge_type: USED_BY_QUERY_PATTERN
    materialize_inverse: false
    edge_class: canonical
    source_type: query_pattern
    target_type: table
```

```yaml
candidate_edge:
  edge_id: edge.query_pattern.flipkart.commission_recon.uses_table.table.flipkart.commission
  edge_type: USES_TABLE
  source: query_pattern.flipkart.commission_recon
  target: table.flipkart.commission
  fields:
    edge_family: execution_guidance
    evidence_basis: query_pattern.fields.required_tables
    confidence: high
    canonical_cognee_edge: true
    marketplace_only: true
    canonical_edge_type: USES_TABLE
    legacy_edge_aliases:
    - query_requires_table
    inverse_edge_type: USED_BY_QUERY_PATTERN
    materialize_inverse: false
    edge_class: canonical
    source_type: query_pattern
    target_type: table
```

```yaml
candidate_edge:
  edge_id: edge.query_pattern.flipkart.commission_recon.uses_reconciliation_profile.reconciliation_profile.flipkart.settlement_commission
  edge_type: USES_RECONCILIATION_PROFILE
  source: query_pattern.flipkart.commission_recon
  target: reconciliation_profile.flipkart.settlement_commission
  fields:
    edge_family: execution_guidance
    evidence_basis: query_pattern.fields.canonical_metric_or_object
    confidence: high
    canonical_cognee_edge: true
    marketplace_only: true
    canonical_edge_type: USES_RECONCILIATION_PROFILE
    legacy_edge_aliases:
    - query_targets_card
    inverse_edge_type: USED_BY_QUERY_PATTERN
    materialize_inverse: false
    edge_class: canonical
    source_type: query_pattern
    target_type: reconciliation_profile
```

```yaml
candidate_edge:
  edge_id: edge.query_pattern.flipkart.commission_recon.uses_relationship.relationship.flipkart.commission_settlement
  edge_type: USES_RELATIONSHIP
  source: query_pattern.flipkart.commission_recon
  target: relationship.flipkart.commission_settlement
  fields:
    edge_family: execution_guidance_derived
    evidence_basis: query_pattern.fields.required_tables + relationship table pair
    confidence: high
    canonical_cognee_edge: true
    marketplace_only: true
    note: Derived parser helper edge. Cognee v4 §8.7 lists QueryPattern->Table/Metric/Reconciliation; this links the explicit join path when both tables are required.
    canonical_edge_type: USES_RELATIONSHIP
    inverse_edge_type: USED_BY_QUERY_PATTERN
    materialize_inverse: false
    edge_class: canonical
    source_type: query_pattern
    target_type: relationship
```

```yaml
candidate_edge:
  edge_id: edge.query_pattern.flipkart.commission_recon.requires_rule.rule.flipkart.active_filter
  edge_type: REQUIRES_RULE
  source: query_pattern.flipkart.commission_recon
  target: rule.flipkart.active_filter
  fields:
    edge_family: execution_guidance
    evidence_basis: query_pattern.fields.required_filters
    confidence: high
    canonical_cognee_edge: true
    marketplace_only: true
    canonical_edge_type: REQUIRES_RULE
    legacy_edge_aliases:
    - query_targets_card
    inverse_edge_type: REQUIRED_BY_QUERY_PATTERN
    materialize_inverse: false
    edge_class: canonical
    source_type: query_pattern
    target_type: rule
```

```yaml
candidate_edge:
  edge_id: edge.query_pattern.flipkart.commission_recon.has_validation_test.validation_test.flipkart.active_filter_present
  edge_type: HAS_VALIDATION_TEST
  source: query_pattern.flipkart.commission_recon
  target: validation_test.flipkart.active_filter_present
  fields:
    edge_family: execution_guidance
    evidence_basis: query_pattern.fields.required_filters
    confidence: high
    canonical_cognee_edge: true
    marketplace_only: true
    canonical_edge_type: HAS_VALIDATION_TEST
    legacy_edge_aliases:
    - query_targets_card
    inverse_edge_type: VALIDATES_QUERY_PATTERN
    materialize_inverse: false
    edge_class: canonical
    source_type: query_pattern
    target_type: validation_test
```

```yaml
candidate_edge:
  edge_id: edge.query_pattern.flipkart.commission_recon.requires_rule.rule.flipkart.preaggregate_many_side
  edge_type: REQUIRES_RULE
  source: query_pattern.flipkart.commission_recon
  target: rule.flipkart.preaggregate_many_side
  fields:
    edge_family: execution_guidance
    evidence_basis: query_pattern.fields.join_requirements
    confidence: high
    canonical_cognee_edge: true
    marketplace_only: true
    canonical_edge_type: REQUIRES_RULE
    legacy_edge_aliases:
    - query_targets_card
    inverse_edge_type: REQUIRED_BY_QUERY_PATTERN
    materialize_inverse: false
    edge_class: canonical
    source_type: query_pattern
    target_type: rule
```

```yaml
candidate_edge:
  edge_id: edge.query_pattern.flipkart.commission_recon.requires_rule.rule.flipkart.commission_od_normalization
  edge_type: REQUIRES_RULE
  source: query_pattern.flipkart.commission_recon
  target: rule.flipkart.commission_od_normalization
  fields:
    edge_family: execution_guidance
    evidence_basis: query_pattern.fields.join_requirements
    confidence: high
    canonical_cognee_edge: true
    marketplace_only: true
    canonical_edge_type: REQUIRES_RULE
    legacy_edge_aliases:
    - query_targets_card
    inverse_edge_type: REQUIRED_BY_QUERY_PATTERN
    materialize_inverse: false
    edge_class: canonical
    source_type: query_pattern
    target_type: rule
```

```yaml
candidate_edge:
  edge_id: edge.query_pattern.flipkart.commission_recon.has_validation_test.validation_test.flipkart.commission_order_id_normalized
  edge_type: HAS_VALIDATION_TEST
  source: query_pattern.flipkart.commission_recon
  target: validation_test.flipkart.commission_order_id_normalized
  fields:
    edge_family: execution_guidance
    evidence_basis: query_pattern.fields.join_requirements
    confidence: high
    canonical_cognee_edge: true
    marketplace_only: true
    canonical_edge_type: HAS_VALIDATION_TEST
    legacy_edge_aliases:
    - query_targets_card
    inverse_edge_type: VALIDATES_QUERY_PATTERN
    materialize_inverse: false
    edge_class: canonical
    source_type: query_pattern
    target_type: validation_test
```

```yaml
candidate_edge:
  edge_id: edge.query_pattern.flipkart.cashback.uses_table.table.flipkart.cashback
  edge_type: USES_TABLE
  source: query_pattern.flipkart.cashback
  target: table.flipkart.cashback
  fields:
    edge_family: execution_guidance
    evidence_basis: query_pattern.fields.required_tables
    confidence: high
    canonical_cognee_edge: true
    marketplace_only: true
    canonical_edge_type: USES_TABLE
    legacy_edge_aliases:
    - query_requires_table
    inverse_edge_type: USED_BY_QUERY_PATTERN
    materialize_inverse: false
    edge_class: canonical
    source_type: query_pattern
    target_type: table
```

```yaml
candidate_edge:
  edge_id: edge.query_pattern.flipkart.cashback.produces_metric.metric.net_cashback
  edge_type: PRODUCES_METRIC
  source: query_pattern.flipkart.cashback
  target: metric.net_cashback
  fields:
    edge_family: execution_guidance
    evidence_basis: query_pattern.fields.canonical_metric_or_object
    confidence: high
    canonical_cognee_edge: true
    marketplace_only: true
    canonical_edge_type: PRODUCES_METRIC
    legacy_edge_aliases:
    - query_targets_card
    inverse_edge_type: PRODUCED_BY_QUERY_PATTERN
    materialize_inverse: false
    edge_class: canonical
    source_type: query_pattern
    target_type: metric
```

```yaml
candidate_edge:
  edge_id: edge.query_pattern.flipkart.cashback.requires_rule.rule.flipkart.active_filter
  edge_type: REQUIRES_RULE
  source: query_pattern.flipkart.cashback
  target: rule.flipkart.active_filter
  fields:
    edge_family: execution_guidance
    evidence_basis: query_pattern.fields.required_filters
    confidence: high
    canonical_cognee_edge: true
    marketplace_only: true
    canonical_edge_type: REQUIRES_RULE
    legacy_edge_aliases:
    - query_targets_card
    inverse_edge_type: REQUIRED_BY_QUERY_PATTERN
    materialize_inverse: false
    edge_class: canonical
    source_type: query_pattern
    target_type: rule
```

```yaml
candidate_edge:
  edge_id: edge.query_pattern.flipkart.cashback.has_validation_test.validation_test.flipkart.active_filter_present
  edge_type: HAS_VALIDATION_TEST
  source: query_pattern.flipkart.cashback
  target: validation_test.flipkart.active_filter_present
  fields:
    edge_family: execution_guidance
    evidence_basis: query_pattern.fields.required_filters
    confidence: high
    canonical_cognee_edge: true
    marketplace_only: true
    canonical_edge_type: HAS_VALIDATION_TEST
    legacy_edge_aliases:
    - query_targets_card
    inverse_edge_type: VALIDATES_QUERY_PATTERN
    materialize_inverse: false
    edge_class: canonical
    source_type: query_pattern
    target_type: validation_test
```

```yaml
candidate_edge:
  edge_id: edge.query_pattern.flipkart.cashback.requires_rule.rule.flipkart.cashback_signed
  edge_type: REQUIRES_RULE
  source: query_pattern.flipkart.cashback
  target: rule.flipkart.cashback_signed
  fields:
    edge_family: execution_guidance
    evidence_basis: cashback query semantics
    confidence: high
    canonical_cognee_edge: true
    marketplace_only: true
    canonical_edge_type: REQUIRES_RULE
    legacy_edge_aliases:
    - query_targets_card
    inverse_edge_type: REQUIRED_BY_QUERY_PATTERN
    materialize_inverse: false
    edge_class: canonical
    source_type: query_pattern
    target_type: rule
```

```yaml
candidate_edge:
  edge_id: edge.query_pattern.flipkart.cashback_doc_type.uses_table.table.flipkart.cashback
  edge_type: USES_TABLE
  source: query_pattern.flipkart.cashback_doc_type
  target: table.flipkart.cashback
  fields:
    edge_family: execution_guidance
    evidence_basis: query_pattern.fields.required_tables
    confidence: high
    canonical_cognee_edge: true
    marketplace_only: true
    canonical_edge_type: USES_TABLE
    legacy_edge_aliases:
    - query_requires_table
    inverse_edge_type: USED_BY_QUERY_PATTERN
    materialize_inverse: false
    edge_class: canonical
    source_type: query_pattern
    target_type: table
```

```yaml
candidate_edge:
  edge_id: edge.query_pattern.flipkart.cashback_doc_type.produces_metric.metric.net_cashback
  edge_type: PRODUCES_METRIC
  source: query_pattern.flipkart.cashback_doc_type
  target: metric.net_cashback
  fields:
    edge_family: execution_guidance
    evidence_basis: query_pattern.fields.canonical_metric_or_object
    confidence: high
    canonical_cognee_edge: true
    marketplace_only: true
    canonical_edge_type: PRODUCES_METRIC
    legacy_edge_aliases:
    - query_targets_card
    inverse_edge_type: PRODUCED_BY_QUERY_PATTERN
    materialize_inverse: false
    edge_class: canonical
    source_type: query_pattern
    target_type: metric
```

```yaml
candidate_edge:
  edge_id: edge.query_pattern.flipkart.cashback_doc_type.requires_rule.rule.flipkart.active_filter
  edge_type: REQUIRES_RULE
  source: query_pattern.flipkart.cashback_doc_type
  target: rule.flipkart.active_filter
  fields:
    edge_family: execution_guidance
    evidence_basis: query_pattern.fields.required_filters
    confidence: high
    canonical_cognee_edge: true
    marketplace_only: true
    canonical_edge_type: REQUIRES_RULE
    legacy_edge_aliases:
    - query_targets_card
    inverse_edge_type: REQUIRED_BY_QUERY_PATTERN
    materialize_inverse: false
    edge_class: canonical
    source_type: query_pattern
    target_type: rule
```

```yaml
candidate_edge:
  edge_id: edge.query_pattern.flipkart.cashback_doc_type.has_validation_test.validation_test.flipkart.active_filter_present
  edge_type: HAS_VALIDATION_TEST
  source: query_pattern.flipkart.cashback_doc_type
  target: validation_test.flipkart.active_filter_present
  fields:
    edge_family: execution_guidance
    evidence_basis: query_pattern.fields.required_filters
    confidence: high
    canonical_cognee_edge: true
    marketplace_only: true
    canonical_edge_type: HAS_VALIDATION_TEST
    legacy_edge_aliases:
    - query_targets_card
    inverse_edge_type: VALIDATES_QUERY_PATTERN
    materialize_inverse: false
    edge_class: canonical
    source_type: query_pattern
    target_type: validation_test
```

```yaml
candidate_edge:
  edge_id: edge.query_pattern.flipkart.cashback_doc_type.requires_rule.rule.flipkart.cashback_signed
  edge_type: REQUIRES_RULE
  source: query_pattern.flipkart.cashback_doc_type
  target: rule.flipkart.cashback_signed
  fields:
    edge_family: execution_guidance
    evidence_basis: cashback query semantics
    confidence: high
    canonical_cognee_edge: true
    marketplace_only: true
    canonical_edge_type: REQUIRES_RULE
    legacy_edge_aliases:
    - query_targets_card
    inverse_edge_type: REQUIRED_BY_QUERY_PATTERN
    materialize_inverse: false
    edge_class: canonical
    source_type: query_pattern
    target_type: rule
```

```yaml
candidate_edge:
  edge_id: edge.query_pattern.flipkart.cashback_rate.uses_table.table.flipkart.cashback
  edge_type: USES_TABLE
  source: query_pattern.flipkart.cashback_rate
  target: table.flipkart.cashback
  fields:
    edge_family: execution_guidance
    evidence_basis: query_pattern.fields.required_tables
    confidence: high
    canonical_cognee_edge: true
    marketplace_only: true
    canonical_edge_type: USES_TABLE
    legacy_edge_aliases:
    - query_requires_table
    inverse_edge_type: USED_BY_QUERY_PATTERN
    materialize_inverse: false
    edge_class: canonical
    source_type: query_pattern
    target_type: table
```

```yaml
candidate_edge:
  edge_id: edge.query_pattern.flipkart.cashback_rate.uses_table.table.flipkart.oms
  edge_type: USES_TABLE
  source: query_pattern.flipkart.cashback_rate
  target: table.flipkart.oms
  fields:
    edge_family: execution_guidance
    evidence_basis: query_pattern.fields.required_tables
    confidence: high
    canonical_cognee_edge: true
    marketplace_only: true
    canonical_edge_type: USES_TABLE
    legacy_edge_aliases:
    - query_requires_table
    inverse_edge_type: USED_BY_QUERY_PATTERN
    materialize_inverse: false
    edge_class: canonical
    source_type: query_pattern
    target_type: table
```

```yaml
candidate_edge:
  edge_id: edge.query_pattern.flipkart.cashback_rate.produces_metric.metric.cashback_rate
  edge_type: PRODUCES_METRIC
  source: query_pattern.flipkart.cashback_rate
  target: metric.cashback_rate
  fields:
    edge_family: execution_guidance
    evidence_basis: query_pattern.fields.canonical_metric_or_object
    confidence: high
    canonical_cognee_edge: true
    marketplace_only: true
    canonical_edge_type: PRODUCES_METRIC
    legacy_edge_aliases:
    - query_targets_card
    inverse_edge_type: PRODUCED_BY_QUERY_PATTERN
    materialize_inverse: false
    edge_class: canonical
    source_type: query_pattern
    target_type: metric
```

```yaml
candidate_edge:
  edge_id: edge.query_pattern.flipkart.cashback_rate.uses_relationship.relationship.flipkart.cashback_oms
  edge_type: USES_RELATIONSHIP
  source: query_pattern.flipkart.cashback_rate
  target: relationship.flipkart.cashback_oms
  fields:
    edge_family: execution_guidance_derived
    evidence_basis: query_pattern.fields.required_tables + relationship table pair
    confidence: high
    canonical_cognee_edge: true
    marketplace_only: true
    note: Derived parser helper edge. Cognee v4 §8.7 lists QueryPattern->Table/Metric/Reconciliation; this links the explicit join path when both tables are required.
    canonical_edge_type: USES_RELATIONSHIP
    inverse_edge_type: USED_BY_QUERY_PATTERN
    materialize_inverse: false
    edge_class: canonical
    source_type: query_pattern
    target_type: relationship
```

```yaml
candidate_edge:
  edge_id: edge.query_pattern.flipkart.cashback_rate.requires_rule.rule.flipkart.active_filter
  edge_type: REQUIRES_RULE
  source: query_pattern.flipkart.cashback_rate
  target: rule.flipkart.active_filter
  fields:
    edge_family: execution_guidance
    evidence_basis: query_pattern.fields.required_filters
    confidence: high
    canonical_cognee_edge: true
    marketplace_only: true
    canonical_edge_type: REQUIRES_RULE
    legacy_edge_aliases:
    - query_targets_card
    inverse_edge_type: REQUIRED_BY_QUERY_PATTERN
    materialize_inverse: false
    edge_class: canonical
    source_type: query_pattern
    target_type: rule
```

```yaml
candidate_edge:
  edge_id: edge.query_pattern.flipkart.cashback_rate.has_validation_test.validation_test.flipkart.active_filter_present
  edge_type: HAS_VALIDATION_TEST
  source: query_pattern.flipkart.cashback_rate
  target: validation_test.flipkart.active_filter_present
  fields:
    edge_family: execution_guidance
    evidence_basis: query_pattern.fields.required_filters
    confidence: high
    canonical_cognee_edge: true
    marketplace_only: true
    canonical_edge_type: HAS_VALIDATION_TEST
    legacy_edge_aliases:
    - query_targets_card
    inverse_edge_type: VALIDATES_QUERY_PATTERN
    materialize_inverse: false
    edge_class: canonical
    source_type: query_pattern
    target_type: validation_test
```

```yaml
candidate_edge:
  edge_id: edge.query_pattern.flipkart.cashback_rate.requires_rule.rule.flipkart.preaggregate_many_side
  edge_type: REQUIRES_RULE
  source: query_pattern.flipkart.cashback_rate
  target: rule.flipkart.preaggregate_many_side
  fields:
    edge_family: execution_guidance
    evidence_basis: query_pattern.fields.join_requirements
    confidence: high
    canonical_cognee_edge: true
    marketplace_only: true
    canonical_edge_type: REQUIRES_RULE
    legacy_edge_aliases:
    - query_targets_card
    inverse_edge_type: REQUIRED_BY_QUERY_PATTERN
    materialize_inverse: false
    edge_class: canonical
    source_type: query_pattern
    target_type: rule
```

```yaml
candidate_edge:
  edge_id: edge.query_pattern.flipkart.cashback_rate.requires_rule.rule.flipkart.cashback_signed
  edge_type: REQUIRES_RULE
  source: query_pattern.flipkart.cashback_rate
  target: rule.flipkart.cashback_signed
  fields:
    edge_family: execution_guidance
    evidence_basis: cashback query semantics
    confidence: high
    canonical_cognee_edge: true
    marketplace_only: true
    canonical_edge_type: REQUIRES_RULE
    legacy_edge_aliases:
    - query_targets_card
    inverse_edge_type: REQUIRED_BY_QUERY_PATTERN
    materialize_inverse: false
    edge_class: canonical
    source_type: query_pattern
    target_type: rule
```

```yaml
candidate_edge:
  edge_id: edge.query_pattern.flipkart.shopsy_cashback.uses_table.table.flipkart.cashback
  edge_type: USES_TABLE
  source: query_pattern.flipkart.shopsy_cashback
  target: table.flipkart.cashback
  fields:
    edge_family: execution_guidance
    evidence_basis: query_pattern.fields.required_tables
    confidence: high
    canonical_cognee_edge: true
    marketplace_only: true
    canonical_edge_type: USES_TABLE
    legacy_edge_aliases:
    - query_requires_table
    inverse_edge_type: USED_BY_QUERY_PATTERN
    materialize_inverse: false
    edge_class: canonical
    source_type: query_pattern
    target_type: table
```

```yaml
candidate_edge:
  edge_id: edge.query_pattern.flipkart.shopsy_cashback.produces_metric.metric.net_cashback
  edge_type: PRODUCES_METRIC
  source: query_pattern.flipkart.shopsy_cashback
  target: metric.net_cashback
  fields:
    edge_family: execution_guidance
    evidence_basis: query_pattern.fields.canonical_metric_or_object
    confidence: high
    canonical_cognee_edge: true
    marketplace_only: true
    canonical_edge_type: PRODUCES_METRIC
    legacy_edge_aliases:
    - query_targets_card
    inverse_edge_type: PRODUCED_BY_QUERY_PATTERN
    materialize_inverse: false
    edge_class: canonical
    source_type: query_pattern
    target_type: metric
```

```yaml
candidate_edge:
  edge_id: edge.query_pattern.flipkart.shopsy_cashback.requires_rule.rule.flipkart.active_filter
  edge_type: REQUIRES_RULE
  source: query_pattern.flipkart.shopsy_cashback
  target: rule.flipkart.active_filter
  fields:
    edge_family: execution_guidance
    evidence_basis: query_pattern.fields.required_filters
    confidence: high
    canonical_cognee_edge: true
    marketplace_only: true
    canonical_edge_type: REQUIRES_RULE
    legacy_edge_aliases:
    - query_targets_card
    inverse_edge_type: REQUIRED_BY_QUERY_PATTERN
    materialize_inverse: false
    edge_class: canonical
    source_type: query_pattern
    target_type: rule
```

```yaml
candidate_edge:
  edge_id: edge.query_pattern.flipkart.shopsy_cashback.has_validation_test.validation_test.flipkart.active_filter_present
  edge_type: HAS_VALIDATION_TEST
  source: query_pattern.flipkart.shopsy_cashback
  target: validation_test.flipkart.active_filter_present
  fields:
    edge_family: execution_guidance
    evidence_basis: query_pattern.fields.required_filters
    confidence: high
    canonical_cognee_edge: true
    marketplace_only: true
    canonical_edge_type: HAS_VALIDATION_TEST
    legacy_edge_aliases:
    - query_targets_card
    inverse_edge_type: VALIDATES_QUERY_PATTERN
    materialize_inverse: false
    edge_class: canonical
    source_type: query_pattern
    target_type: validation_test
```

```yaml
candidate_edge:
  edge_id: edge.query_pattern.flipkart.shopsy_cashback.requires_rule.rule.flipkart.cashback_signed
  edge_type: REQUIRES_RULE
  source: query_pattern.flipkart.shopsy_cashback
  target: rule.flipkart.cashback_signed
  fields:
    edge_family: execution_guidance
    evidence_basis: cashback query semantics
    confidence: high
    canonical_cognee_edge: true
    marketplace_only: true
    canonical_edge_type: REQUIRES_RULE
    legacy_edge_aliases:
    - query_targets_card
    inverse_edge_type: REQUIRED_BY_QUERY_PATTERN
    materialize_inverse: false
    edge_class: canonical
    source_type: query_pattern
    target_type: rule
```

```yaml
candidate_edge:
  edge_id: edge.query_pattern.flipkart.cashback_offer_recon.uses_table.table.flipkart.cashback
  edge_type: USES_TABLE
  source: query_pattern.flipkart.cashback_offer_recon
  target: table.flipkart.cashback
  fields:
    edge_family: execution_guidance
    evidence_basis: query_pattern.fields.required_tables
    confidence: high
    canonical_cognee_edge: true
    marketplace_only: true
    canonical_edge_type: USES_TABLE
    legacy_edge_aliases:
    - query_requires_table
    inverse_edge_type: USED_BY_QUERY_PATTERN
    materialize_inverse: false
    edge_class: canonical
    source_type: query_pattern
    target_type: table
```

```yaml
candidate_edge:
  edge_id: edge.query_pattern.flipkart.cashback_offer_recon.uses_table.table.flipkart.settlement
  edge_type: USES_TABLE
  source: query_pattern.flipkart.cashback_offer_recon
  target: table.flipkart.settlement
  fields:
    edge_family: execution_guidance
    evidence_basis: query_pattern.fields.required_tables
    confidence: high
    canonical_cognee_edge: true
    marketplace_only: true
    canonical_edge_type: USES_TABLE
    legacy_edge_aliases:
    - query_requires_table
    inverse_edge_type: USED_BY_QUERY_PATTERN
    materialize_inverse: false
    edge_class: canonical
    source_type: query_pattern
    target_type: table
```

```yaml
candidate_edge:
  edge_id: edge.query_pattern.flipkart.cashback_offer_recon.uses_reconciliation_profile.reconciliation_profile.flipkart.cashback_settlement_offer
  edge_type: USES_RECONCILIATION_PROFILE
  source: query_pattern.flipkart.cashback_offer_recon
  target: reconciliation_profile.flipkart.cashback_settlement_offer
  fields:
    edge_family: execution_guidance
    evidence_basis: query_pattern.fields.canonical_metric_or_object
    confidence: high
    canonical_cognee_edge: true
    marketplace_only: true
    canonical_edge_type: USES_RECONCILIATION_PROFILE
    legacy_edge_aliases:
    - query_targets_card
    inverse_edge_type: USED_BY_QUERY_PATTERN
    materialize_inverse: false
    edge_class: canonical
    source_type: query_pattern
    target_type: reconciliation_profile
```

```yaml
candidate_edge:
  edge_id: edge.query_pattern.flipkart.cashback_offer_recon.uses_relationship.relationship.flipkart.cashback_settlement
  edge_type: USES_RELATIONSHIP
  source: query_pattern.flipkart.cashback_offer_recon
  target: relationship.flipkart.cashback_settlement
  fields:
    edge_family: execution_guidance_derived
    evidence_basis: query_pattern.fields.required_tables + relationship table pair
    confidence: high
    canonical_cognee_edge: true
    marketplace_only: true
    note: Derived parser helper edge. Cognee v4 §8.7 lists QueryPattern->Table/Metric/Reconciliation; this links the explicit join path when both tables are required.
    canonical_edge_type: USES_RELATIONSHIP
    inverse_edge_type: USED_BY_QUERY_PATTERN
    materialize_inverse: false
    edge_class: canonical
    source_type: query_pattern
    target_type: relationship
```

```yaml
candidate_edge:
  edge_id: edge.query_pattern.flipkart.cashback_offer_recon.requires_rule.rule.flipkart.active_filter
  edge_type: REQUIRES_RULE
  source: query_pattern.flipkart.cashback_offer_recon
  target: rule.flipkart.active_filter
  fields:
    edge_family: execution_guidance
    evidence_basis: query_pattern.fields.required_filters
    confidence: high
    canonical_cognee_edge: true
    marketplace_only: true
    canonical_edge_type: REQUIRES_RULE
    legacy_edge_aliases:
    - query_targets_card
    inverse_edge_type: REQUIRED_BY_QUERY_PATTERN
    materialize_inverse: false
    edge_class: canonical
    source_type: query_pattern
    target_type: rule
```

```yaml
candidate_edge:
  edge_id: edge.query_pattern.flipkart.cashback_offer_recon.has_validation_test.validation_test.flipkart.active_filter_present
  edge_type: HAS_VALIDATION_TEST
  source: query_pattern.flipkart.cashback_offer_recon
  target: validation_test.flipkart.active_filter_present
  fields:
    edge_family: execution_guidance
    evidence_basis: query_pattern.fields.required_filters
    confidence: high
    canonical_cognee_edge: true
    marketplace_only: true
    canonical_edge_type: HAS_VALIDATION_TEST
    legacy_edge_aliases:
    - query_targets_card
    inverse_edge_type: VALIDATES_QUERY_PATTERN
    materialize_inverse: false
    edge_class: canonical
    source_type: query_pattern
    target_type: validation_test
```

```yaml
candidate_edge:
  edge_id: edge.query_pattern.flipkart.cashback_offer_recon.requires_rule.rule.flipkart.preaggregate_many_side
  edge_type: REQUIRES_RULE
  source: query_pattern.flipkart.cashback_offer_recon
  target: rule.flipkart.preaggregate_many_side
  fields:
    edge_family: execution_guidance
    evidence_basis: query_pattern.fields.join_requirements
    confidence: high
    canonical_cognee_edge: true
    marketplace_only: true
    canonical_edge_type: REQUIRES_RULE
    legacy_edge_aliases:
    - query_targets_card
    inverse_edge_type: REQUIRED_BY_QUERY_PATTERN
    materialize_inverse: false
    edge_class: canonical
    source_type: query_pattern
    target_type: rule
```

```yaml
candidate_edge:
  edge_id: edge.query_pattern.flipkart.cashback_offer_recon.requires_rule.rule.flipkart.cashback_signed
  edge_type: REQUIRES_RULE
  source: query_pattern.flipkart.cashback_offer_recon
  target: rule.flipkart.cashback_signed
  fields:
    edge_family: execution_guidance
    evidence_basis: cashback query semantics
    confidence: high
    canonical_cognee_edge: true
    marketplace_only: true
    canonical_edge_type: REQUIRES_RULE
    legacy_edge_aliases:
    - query_targets_card
    inverse_edge_type: REQUIRED_BY_QUERY_PATTERN
    materialize_inverse: false
    edge_class: canonical
    source_type: query_pattern
    target_type: rule
```

```yaml
candidate_edge:
  edge_id: edge.query_pattern.flipkart.tcs_tds.uses_table.table.flipkart.settlement
  edge_type: USES_TABLE
  source: query_pattern.flipkart.tcs_tds
  target: table.flipkart.settlement
  fields:
    edge_family: execution_guidance
    evidence_basis: query_pattern.fields.required_tables
    confidence: high
    canonical_cognee_edge: true
    marketplace_only: true
    canonical_edge_type: USES_TABLE
    legacy_edge_aliases:
    - query_requires_table
    inverse_edge_type: USED_BY_QUERY_PATTERN
    materialize_inverse: false
    edge_class: canonical
    source_type: query_pattern
    target_type: table
```

```yaml
candidate_edge:
  edge_id: edge.query_pattern.flipkart.tcs_tds.produces_metric.metric.tcs_deducted
  edge_type: PRODUCES_METRIC
  source: query_pattern.flipkart.tcs_tds
  target: metric.tcs_deducted
  fields:
    edge_family: execution_guidance
    evidence_basis: query_pattern.fields.canonical_metric_or_object
    confidence: high
    canonical_cognee_edge: true
    marketplace_only: true
    canonical_edge_type: PRODUCES_METRIC
    legacy_edge_aliases:
    - query_targets_card
    inverse_edge_type: PRODUCED_BY_QUERY_PATTERN
    materialize_inverse: false
    edge_class: canonical
    source_type: query_pattern
    target_type: metric
```

```yaml
candidate_edge:
  edge_id: edge.query_pattern.flipkart.tcs_tds.requires_rule.rule.flipkart.active_filter
  edge_type: REQUIRES_RULE
  source: query_pattern.flipkart.tcs_tds
  target: rule.flipkart.active_filter
  fields:
    edge_family: execution_guidance
    evidence_basis: query_pattern.fields.required_filters
    confidence: high
    canonical_cognee_edge: true
    marketplace_only: true
    canonical_edge_type: REQUIRES_RULE
    legacy_edge_aliases:
    - query_targets_card
    inverse_edge_type: REQUIRED_BY_QUERY_PATTERN
    materialize_inverse: false
    edge_class: canonical
    source_type: query_pattern
    target_type: rule
```

```yaml
candidate_edge:
  edge_id: edge.query_pattern.flipkart.tcs_tds.has_validation_test.validation_test.flipkart.active_filter_present
  edge_type: HAS_VALIDATION_TEST
  source: query_pattern.flipkart.tcs_tds
  target: validation_test.flipkart.active_filter_present
  fields:
    edge_family: execution_guidance
    evidence_basis: query_pattern.fields.required_filters
    confidence: high
    canonical_cognee_edge: true
    marketplace_only: true
    canonical_edge_type: HAS_VALIDATION_TEST
    legacy_edge_aliases:
    - query_targets_card
    inverse_edge_type: VALIDATES_QUERY_PATTERN
    materialize_inverse: false
    edge_class: canonical
    source_type: query_pattern
    target_type: validation_test
```

```yaml
candidate_edge:
  edge_id: edge.query_pattern.flipkart.tcs_tds.requires_rule.rule.flipkart.tcs_tds_not_cost
  edge_type: REQUIRES_RULE
  source: query_pattern.flipkart.tcs_tds
  target: rule.flipkart.tcs_tds_not_cost
  fields:
    edge_family: execution_guidance
    evidence_basis: tax query semantics
    confidence: high
    canonical_cognee_edge: true
    marketplace_only: true
    canonical_edge_type: REQUIRES_RULE
    legacy_edge_aliases:
    - query_targets_card
    inverse_edge_type: REQUIRED_BY_QUERY_PATTERN
    materialize_inverse: false
    edge_class: canonical
    source_type: query_pattern
    target_type: rule
```

```yaml
candidate_edge:
  edge_id: edge.query_pattern.flipkart.gst_fees.uses_table.table.flipkart.settlement
  edge_type: USES_TABLE
  source: query_pattern.flipkart.gst_fees
  target: table.flipkart.settlement
  fields:
    edge_family: execution_guidance
    evidence_basis: query_pattern.fields.required_tables
    confidence: high
    canonical_cognee_edge: true
    marketplace_only: true
    canonical_edge_type: USES_TABLE
    legacy_edge_aliases:
    - query_requires_table
    inverse_edge_type: USED_BY_QUERY_PATTERN
    materialize_inverse: false
    edge_class: canonical
    source_type: query_pattern
    target_type: table
```

```yaml
candidate_edge:
  edge_id: edge.query_pattern.flipkart.gst_fees.uses_table.table.flipkart.commission
  edge_type: USES_TABLE
  source: query_pattern.flipkart.gst_fees
  target: table.flipkart.commission
  fields:
    edge_family: execution_guidance
    evidence_basis: query_pattern.fields.required_tables
    confidence: high
    canonical_cognee_edge: true
    marketplace_only: true
    canonical_edge_type: USES_TABLE
    legacy_edge_aliases:
    - query_requires_table
    inverse_edge_type: USED_BY_QUERY_PATTERN
    materialize_inverse: false
    edge_class: canonical
    source_type: query_pattern
    target_type: table
```

```yaml
candidate_edge:
  edge_id: edge.query_pattern.flipkart.gst_fees.produces_metric.metric.gst_on_marketplace_fees
  edge_type: PRODUCES_METRIC
  source: query_pattern.flipkart.gst_fees
  target: metric.gst_on_marketplace_fees
  fields:
    edge_family: execution_guidance
    evidence_basis: query_pattern.fields.canonical_metric_or_object
    confidence: high
    canonical_cognee_edge: true
    marketplace_only: true
    canonical_edge_type: PRODUCES_METRIC
    legacy_edge_aliases:
    - query_targets_card
    inverse_edge_type: PRODUCED_BY_QUERY_PATTERN
    materialize_inverse: false
    edge_class: canonical
    source_type: query_pattern
    target_type: metric
```

```yaml
candidate_edge:
  edge_id: edge.query_pattern.flipkart.gst_fees.uses_relationship.relationship.flipkart.commission_settlement
  edge_type: USES_RELATIONSHIP
  source: query_pattern.flipkart.gst_fees
  target: relationship.flipkart.commission_settlement
  fields:
    edge_family: execution_guidance_derived
    evidence_basis: query_pattern.fields.required_tables + relationship table pair
    confidence: high
    canonical_cognee_edge: true
    marketplace_only: true
    note: Derived parser helper edge. Cognee v4 §8.7 lists QueryPattern->Table/Metric/Reconciliation; this links the explicit join path when both tables are required.
    canonical_edge_type: USES_RELATIONSHIP
    inverse_edge_type: USED_BY_QUERY_PATTERN
    materialize_inverse: false
    edge_class: canonical
    source_type: query_pattern
    target_type: relationship
```

```yaml
candidate_edge:
  edge_id: edge.query_pattern.flipkart.gst_fees.requires_rule.rule.flipkart.active_filter
  edge_type: REQUIRES_RULE
  source: query_pattern.flipkart.gst_fees
  target: rule.flipkart.active_filter
  fields:
    edge_family: execution_guidance
    evidence_basis: query_pattern.fields.required_filters
    confidence: high
    canonical_cognee_edge: true
    marketplace_only: true
    canonical_edge_type: REQUIRES_RULE
    legacy_edge_aliases:
    - query_targets_card
    inverse_edge_type: REQUIRED_BY_QUERY_PATTERN
    materialize_inverse: false
    edge_class: canonical
    source_type: query_pattern
    target_type: rule
```

```yaml
candidate_edge:
  edge_id: edge.query_pattern.flipkart.gst_fees.has_validation_test.validation_test.flipkart.active_filter_present
  edge_type: HAS_VALIDATION_TEST
  source: query_pattern.flipkart.gst_fees
  target: validation_test.flipkart.active_filter_present
  fields:
    edge_family: execution_guidance
    evidence_basis: query_pattern.fields.required_filters
    confidence: high
    canonical_cognee_edge: true
    marketplace_only: true
    canonical_edge_type: HAS_VALIDATION_TEST
    legacy_edge_aliases:
    - query_targets_card
    inverse_edge_type: VALIDATES_QUERY_PATTERN
    materialize_inverse: false
    edge_class: canonical
    source_type: query_pattern
    target_type: validation_test
```

```yaml
candidate_edge:
  edge_id: edge.query_pattern.flipkart.gst_fees.requires_rule.rule.flipkart.preaggregate_many_side
  edge_type: REQUIRES_RULE
  source: query_pattern.flipkart.gst_fees
  target: rule.flipkart.preaggregate_many_side
  fields:
    edge_family: execution_guidance
    evidence_basis: query_pattern.fields.join_requirements
    confidence: high
    canonical_cognee_edge: true
    marketplace_only: true
    canonical_edge_type: REQUIRES_RULE
    legacy_edge_aliases:
    - query_targets_card
    inverse_edge_type: REQUIRED_BY_QUERY_PATTERN
    materialize_inverse: false
    edge_class: canonical
    source_type: query_pattern
    target_type: rule
```

```yaml
candidate_edge:
  edge_id: edge.query_pattern.flipkart.gst_fees.requires_rule.rule.flipkart.commission_od_normalization
  edge_type: REQUIRES_RULE
  source: query_pattern.flipkart.gst_fees
  target: rule.flipkart.commission_od_normalization
  fields:
    edge_family: execution_guidance
    evidence_basis: query_pattern.fields.join_requirements
    confidence: high
    canonical_cognee_edge: true
    marketplace_only: true
    canonical_edge_type: REQUIRES_RULE
    legacy_edge_aliases:
    - query_targets_card
    inverse_edge_type: REQUIRED_BY_QUERY_PATTERN
    materialize_inverse: false
    edge_class: canonical
    source_type: query_pattern
    target_type: rule
```

```yaml
candidate_edge:
  edge_id: edge.query_pattern.flipkart.gst_fees.has_validation_test.validation_test.flipkart.commission_order_id_normalized
  edge_type: HAS_VALIDATION_TEST
  source: query_pattern.flipkart.gst_fees
  target: validation_test.flipkart.commission_order_id_normalized
  fields:
    edge_family: execution_guidance
    evidence_basis: query_pattern.fields.join_requirements
    confidence: high
    canonical_cognee_edge: true
    marketplace_only: true
    canonical_edge_type: HAS_VALIDATION_TEST
    legacy_edge_aliases:
    - query_targets_card
    inverse_edge_type: VALIDATES_QUERY_PATTERN
    materialize_inverse: false
    edge_class: canonical
    source_type: query_pattern
    target_type: validation_test
```

```yaml
candidate_edge:
  edge_id: edge.query_pattern.flipkart.gst_fees.requires_rule.rule.flipkart.tcs_tds_not_cost
  edge_type: REQUIRES_RULE
  source: query_pattern.flipkart.gst_fees
  target: rule.flipkart.tcs_tds_not_cost
  fields:
    edge_family: execution_guidance
    evidence_basis: tax query semantics
    confidence: high
    canonical_cognee_edge: true
    marketplace_only: true
    canonical_edge_type: REQUIRES_RULE
    legacy_edge_aliases:
    - query_targets_card
    inverse_edge_type: REQUIRED_BY_QUERY_PATTERN
    materialize_inverse: false
    edge_class: canonical
    source_type: query_pattern
    target_type: rule
```

```yaml
candidate_edge:
  edge_id: edge.query_pattern.flipkart.gmv.uses_output_contract.output_contract.flipkart.settlement_summary
  edge_type: USES_OUTPUT_CONTRACT
  source: query_pattern.flipkart.gmv
  target: output_contract.flipkart.settlement_summary
  fields:
    edge_family: execution_guidance
    evidence_basis: deterministic query/output use-case mapping
    confidence: high
    canonical_cognee_edge: true
    marketplace_only: true
    canonical_edge_type: USES_OUTPUT_CONTRACT
    legacy_edge_aliases:
    - query_targets_card
    inverse_edge_type: USED_BY_QUERY_PATTERN
    materialize_inverse: false
    edge_class: canonical
    source_type: query_pattern
    target_type: output_contract
```

```yaml
candidate_edge:
  edge_id: edge.query_pattern.flipkart.net_settlement.uses_output_contract.output_contract.flipkart.settlement_summary
  edge_type: USES_OUTPUT_CONTRACT
  source: query_pattern.flipkart.net_settlement
  target: output_contract.flipkart.settlement_summary
  fields:
    edge_family: execution_guidance
    evidence_basis: deterministic query/output use-case mapping
    confidence: high
    canonical_cognee_edge: true
    marketplace_only: true
    canonical_edge_type: USES_OUTPUT_CONTRACT
    legacy_edge_aliases:
    - query_targets_card
    inverse_edge_type: USED_BY_QUERY_PATTERN
    materialize_inverse: false
    edge_class: canonical
    source_type: query_pattern
    target_type: output_contract
```

```yaml
candidate_edge:
  edge_id: edge.query_pattern.flipkart.realization.uses_output_contract.output_contract.flipkart.settlement_summary
  edge_type: USES_OUTPUT_CONTRACT
  source: query_pattern.flipkart.realization
  target: output_contract.flipkart.settlement_summary
  fields:
    edge_family: execution_guidance
    evidence_basis: deterministic query/output use-case mapping
    confidence: high
    canonical_cognee_edge: true
    marketplace_only: true
    canonical_edge_type: USES_OUTPUT_CONTRACT
    legacy_edge_aliases:
    - query_targets_card
    inverse_edge_type: USED_BY_QUERY_PATTERN
    materialize_inverse: false
    edge_class: canonical
    source_type: query_pattern
    target_type: output_contract
```

```yaml
candidate_edge:
  edge_id: edge.query_pattern.flipkart.settlement_by_fulfilment.uses_output_contract.output_contract.flipkart.settlement_summary
  edge_type: USES_OUTPUT_CONTRACT
  source: query_pattern.flipkart.settlement_by_fulfilment
  target: output_contract.flipkart.settlement_summary
  fields:
    edge_family: execution_guidance
    evidence_basis: deterministic query/output use-case mapping
    confidence: high
    canonical_cognee_edge: true
    marketplace_only: true
    canonical_edge_type: USES_OUTPUT_CONTRACT
    legacy_edge_aliases:
    - query_targets_card
    inverse_edge_type: USED_BY_QUERY_PATTERN
    materialize_inverse: false
    edge_class: canonical
    source_type: query_pattern
    target_type: output_contract
```

```yaml
candidate_edge:
  edge_id: edge.query_pattern.flipkart.settlement_cycle.uses_output_contract.output_contract.flipkart.settlement_cycle
  edge_type: USES_OUTPUT_CONTRACT
  source: query_pattern.flipkart.settlement_cycle
  target: output_contract.flipkart.settlement_cycle
  fields:
    edge_family: execution_guidance
    evidence_basis: deterministic query/output use-case mapping
    confidence: high
    canonical_cognee_edge: true
    marketplace_only: true
    canonical_edge_type: USES_OUTPUT_CONTRACT
    legacy_edge_aliases:
    - query_targets_card
    inverse_edge_type: USED_BY_QUERY_PATTERN
    materialize_inverse: false
    edge_class: canonical
    source_type: query_pattern
    target_type: output_contract
```

```yaml
candidate_edge:
  edge_id: edge.query_pattern.flipkart.fee_breakdown.uses_output_contract.output_contract.flipkart.fee_breakdown
  edge_type: USES_OUTPUT_CONTRACT
  source: query_pattern.flipkart.fee_breakdown
  target: output_contract.flipkart.fee_breakdown
  fields:
    edge_family: execution_guidance
    evidence_basis: deterministic query/output use-case mapping
    confidence: high
    canonical_cognee_edge: true
    marketplace_only: true
    canonical_edge_type: USES_OUTPUT_CONTRACT
    legacy_edge_aliases:
    - query_targets_card
    inverse_edge_type: USED_BY_QUERY_PATTERN
    materialize_inverse: false
    edge_class: canonical
    source_type: query_pattern
    target_type: output_contract
```

```yaml
candidate_edge:
  edge_id: edge.query_pattern.flipkart.fee_pivot.uses_output_contract.output_contract.flipkart.fee_breakdown
  edge_type: USES_OUTPUT_CONTRACT
  source: query_pattern.flipkart.fee_pivot
  target: output_contract.flipkart.fee_breakdown
  fields:
    edge_family: execution_guidance
    evidence_basis: deterministic query/output use-case mapping
    confidence: high
    canonical_cognee_edge: true
    marketplace_only: true
    canonical_edge_type: USES_OUTPUT_CONTRACT
    legacy_edge_aliases:
    - query_targets_card
    inverse_edge_type: USED_BY_QUERY_PATTERN
    materialize_inverse: false
    edge_class: canonical
    source_type: query_pattern
    target_type: output_contract
```

```yaml
candidate_edge:
  edge_id: edge.query_pattern.flipkart.commission_recon.uses_output_contract.output_contract.flipkart.commission_recon
  edge_type: USES_OUTPUT_CONTRACT
  source: query_pattern.flipkart.commission_recon
  target: output_contract.flipkart.commission_recon
  fields:
    edge_family: execution_guidance
    evidence_basis: deterministic query/output use-case mapping
    confidence: high
    canonical_cognee_edge: true
    marketplace_only: true
    canonical_edge_type: USES_OUTPUT_CONTRACT
    legacy_edge_aliases:
    - query_targets_card
    inverse_edge_type: USED_BY_QUERY_PATTERN
    materialize_inverse: false
    edge_class: canonical
    source_type: query_pattern
    target_type: output_contract
```

```yaml
candidate_edge:
  edge_id: edge.query_pattern.flipkart.cashback.uses_output_contract.output_contract.flipkart.cashback_recon
  edge_type: USES_OUTPUT_CONTRACT
  source: query_pattern.flipkart.cashback
  target: output_contract.flipkart.cashback_recon
  fields:
    edge_family: execution_guidance
    evidence_basis: deterministic query/output use-case mapping
    confidence: high
    canonical_cognee_edge: true
    marketplace_only: true
    canonical_edge_type: USES_OUTPUT_CONTRACT
    legacy_edge_aliases:
    - query_targets_card
    inverse_edge_type: USED_BY_QUERY_PATTERN
    materialize_inverse: false
    edge_class: canonical
    source_type: query_pattern
    target_type: output_contract
```

```yaml
candidate_edge:
  edge_id: edge.query_pattern.flipkart.cashback_doc_type.uses_output_contract.output_contract.flipkart.cashback_recon
  edge_type: USES_OUTPUT_CONTRACT
  source: query_pattern.flipkart.cashback_doc_type
  target: output_contract.flipkart.cashback_recon
  fields:
    edge_family: execution_guidance
    evidence_basis: deterministic query/output use-case mapping
    confidence: high
    canonical_cognee_edge: true
    marketplace_only: true
    canonical_edge_type: USES_OUTPUT_CONTRACT
    legacy_edge_aliases:
    - query_targets_card
    inverse_edge_type: USED_BY_QUERY_PATTERN
    materialize_inverse: false
    edge_class: canonical
    source_type: query_pattern
    target_type: output_contract
```

```yaml
candidate_edge:
  edge_id: edge.query_pattern.flipkart.cashback_rate.uses_output_contract.output_contract.flipkart.cashback_recon
  edge_type: USES_OUTPUT_CONTRACT
  source: query_pattern.flipkart.cashback_rate
  target: output_contract.flipkart.cashback_recon
  fields:
    edge_family: execution_guidance
    evidence_basis: deterministic query/output use-case mapping
    confidence: high
    canonical_cognee_edge: true
    marketplace_only: true
    canonical_edge_type: USES_OUTPUT_CONTRACT
    legacy_edge_aliases:
    - query_targets_card
    inverse_edge_type: USED_BY_QUERY_PATTERN
    materialize_inverse: false
    edge_class: canonical
    source_type: query_pattern
    target_type: output_contract
```

```yaml
candidate_edge:
  edge_id: edge.query_pattern.flipkart.shopsy_cashback.uses_output_contract.output_contract.flipkart.shopsy_comparison
  edge_type: USES_OUTPUT_CONTRACT
  source: query_pattern.flipkart.shopsy_cashback
  target: output_contract.flipkart.shopsy_comparison
  fields:
    edge_family: execution_guidance
    evidence_basis: deterministic query/output use-case mapping
    confidence: high
    canonical_cognee_edge: true
    marketplace_only: true
    canonical_edge_type: USES_OUTPUT_CONTRACT
    legacy_edge_aliases:
    - query_targets_card
    inverse_edge_type: USED_BY_QUERY_PATTERN
    materialize_inverse: false
    edge_class: canonical
    source_type: query_pattern
    target_type: output_contract
```

```yaml
candidate_edge:
  edge_id: edge.query_pattern.flipkart.cashback_offer_recon.uses_output_contract.output_contract.flipkart.cashback_recon
  edge_type: USES_OUTPUT_CONTRACT
  source: query_pattern.flipkart.cashback_offer_recon
  target: output_contract.flipkart.cashback_recon
  fields:
    edge_family: execution_guidance
    evidence_basis: deterministic query/output use-case mapping
    confidence: high
    canonical_cognee_edge: true
    marketplace_only: true
    canonical_edge_type: USES_OUTPUT_CONTRACT
    legacy_edge_aliases:
    - query_targets_card
    inverse_edge_type: USED_BY_QUERY_PATTERN
    materialize_inverse: false
    edge_class: canonical
    source_type: query_pattern
    target_type: output_contract
```

```yaml
candidate_edge:
  edge_id: edge.query_pattern.flipkart.tcs_tds.uses_output_contract.output_contract.flipkart.settlement_summary
  edge_type: USES_OUTPUT_CONTRACT
  source: query_pattern.flipkart.tcs_tds
  target: output_contract.flipkart.settlement_summary
  fields:
    edge_family: execution_guidance
    evidence_basis: deterministic query/output use-case mapping
    confidence: high
    canonical_cognee_edge: true
    marketplace_only: true
    canonical_edge_type: USES_OUTPUT_CONTRACT
    legacy_edge_aliases:
    - query_targets_card
    inverse_edge_type: USED_BY_QUERY_PATTERN
    materialize_inverse: false
    edge_class: canonical
    source_type: query_pattern
    target_type: output_contract
```

```yaml
candidate_edge:
  edge_id: edge.query_pattern.flipkart.gst_fees.uses_output_contract.output_contract.flipkart.fee_breakdown
  edge_type: USES_OUTPUT_CONTRACT
  source: query_pattern.flipkart.gst_fees
  target: output_contract.flipkart.fee_breakdown
  fields:
    edge_family: execution_guidance
    evidence_basis: deterministic query/output use-case mapping
    confidence: high
    canonical_cognee_edge: true
    marketplace_only: true
    canonical_edge_type: USES_OUTPUT_CONTRACT
    legacy_edge_aliases:
    - query_targets_card
    inverse_edge_type: USED_BY_QUERY_PATTERN
    materialize_inverse: false
    edge_class: canonical
    source_type: query_pattern
    target_type: output_contract
```

```yaml
candidate_edge:
  edge_id: edge.rule.flipkart.active_filter.has_validation_test.validation_test.flipkart.active_filter_present
  edge_type: HAS_VALIDATION_TEST
  source: rule.flipkart.active_filter
  target: validation_test.flipkart.active_filter_present
  fields:
    edge_family: execution_guidance
    evidence_basis: deterministic rule/test semantic mapping
    confidence: high
    canonical_cognee_edge: true
    marketplace_only: true
    canonical_edge_type: HAS_VALIDATION_TEST
    inverse_edge_type: ENFORCES_RULE
    materialize_inverse: true
    edge_class: canonical
    source_type: rule
    target_type: validation_test
```

```yaml
candidate_edge:
  edge_id: edge.validation_test.flipkart.active_filter_present.enforces_rule.rule.flipkart.active_filter
  edge_type: ENFORCES_RULE
  source: validation_test.flipkart.active_filter_present
  target: rule.flipkart.active_filter
  fields:
    edge_family: execution_guidance
    evidence_basis: deterministic rule/test semantic mapping
    confidence: high
    canonical_cognee_edge: true
    marketplace_only: true
    canonical_edge_type: ENFORCES_RULE
    inverse_edge_type: HAS_VALIDATION_TEST
    materialize_inverse: true
    edge_class: canonical
    source_type: validation_test
    target_type: rule
```

```yaml
candidate_edge:
  edge_id: edge.rule.flipkart.group_scope_as_column.has_validation_test.validation_test.flipkart.group_not_binding
  edge_type: HAS_VALIDATION_TEST
  source: rule.flipkart.group_scope_as_column
  target: validation_test.flipkart.group_not_binding
  fields:
    edge_family: execution_guidance
    evidence_basis: deterministic rule/test semantic mapping
    confidence: high
    canonical_cognee_edge: true
    marketplace_only: true
    canonical_edge_type: HAS_VALIDATION_TEST
    inverse_edge_type: ENFORCES_RULE
    materialize_inverse: true
    edge_class: canonical
    source_type: rule
    target_type: validation_test
```

```yaml
candidate_edge:
  edge_id: edge.validation_test.flipkart.group_not_binding.enforces_rule.rule.flipkart.group_scope_as_column
  edge_type: ENFORCES_RULE
  source: validation_test.flipkart.group_not_binding
  target: rule.flipkart.group_scope_as_column
  fields:
    edge_family: execution_guidance
    evidence_basis: deterministic rule/test semantic mapping
    confidence: high
    canonical_cognee_edge: true
    marketplace_only: true
    canonical_edge_type: ENFORCES_RULE
    inverse_edge_type: HAS_VALIDATION_TEST
    materialize_inverse: true
    edge_class: canonical
    source_type: validation_test
    target_type: rule
```

```yaml
candidate_edge:
  edge_id: edge.rule.flipkart.commission_od_normalization.has_validation_test.validation_test.flipkart.commission_order_id_normalized
  edge_type: HAS_VALIDATION_TEST
  source: rule.flipkart.commission_od_normalization
  target: validation_test.flipkart.commission_order_id_normalized
  fields:
    edge_family: execution_guidance
    evidence_basis: deterministic rule/test semantic mapping
    confidence: high
    canonical_cognee_edge: true
    marketplace_only: true
    canonical_edge_type: HAS_VALIDATION_TEST
    inverse_edge_type: ENFORCES_RULE
    materialize_inverse: true
    edge_class: canonical
    source_type: rule
    target_type: validation_test
```

```yaml
candidate_edge:
  edge_id: edge.validation_test.flipkart.commission_order_id_normalized.enforces_rule.rule.flipkart.commission_od_normalization
  edge_type: ENFORCES_RULE
  source: validation_test.flipkart.commission_order_id_normalized
  target: rule.flipkart.commission_od_normalization
  fields:
    edge_family: execution_guidance
    evidence_basis: deterministic rule/test semantic mapping
    confidence: high
    canonical_cognee_edge: true
    marketplace_only: true
    canonical_edge_type: ENFORCES_RULE
    inverse_edge_type: HAS_VALIDATION_TEST
    materialize_inverse: true
    edge_class: canonical
    source_type: validation_test
    target_type: rule
```

```yaml
candidate_edge:
  edge_id: edge.rule.flipkart.preaggregate_many_side.has_validation_test.validation_test.flipkart.commission_preaggregated
  edge_type: HAS_VALIDATION_TEST
  source: rule.flipkart.preaggregate_many_side
  target: validation_test.flipkart.commission_preaggregated
  fields:
    edge_family: execution_guidance
    evidence_basis: deterministic rule/test semantic mapping
    confidence: high
    canonical_cognee_edge: true
    marketplace_only: true
    canonical_edge_type: HAS_VALIDATION_TEST
    inverse_edge_type: ENFORCES_RULE
    materialize_inverse: true
    edge_class: canonical
    source_type: rule
    target_type: validation_test
```

```yaml
candidate_edge:
  edge_id: edge.validation_test.flipkart.commission_preaggregated.enforces_rule.rule.flipkart.preaggregate_many_side
  edge_type: ENFORCES_RULE
  source: validation_test.flipkart.commission_preaggregated
  target: rule.flipkart.preaggregate_many_side
  fields:
    edge_family: execution_guidance
    evidence_basis: deterministic rule/test semantic mapping
    confidence: high
    canonical_cognee_edge: true
    marketplace_only: true
    canonical_edge_type: ENFORCES_RULE
    inverse_edge_type: HAS_VALIDATION_TEST
    materialize_inverse: true
    edge_class: canonical
    source_type: validation_test
    target_type: rule
```

```yaml
candidate_edge:
  edge_id: edge.rule.flipkart.preaggregate_many_side.has_validation_test.validation_test.flipkart.cashback_preaggregated
  edge_type: HAS_VALIDATION_TEST
  source: rule.flipkart.preaggregate_many_side
  target: validation_test.flipkart.cashback_preaggregated
  fields:
    edge_family: execution_guidance
    evidence_basis: deterministic rule/test semantic mapping
    confidence: high
    canonical_cognee_edge: true
    marketplace_only: true
    canonical_edge_type: HAS_VALIDATION_TEST
    inverse_edge_type: ENFORCES_RULE
    materialize_inverse: true
    edge_class: canonical
    source_type: rule
    target_type: validation_test
```

```yaml
candidate_edge:
  edge_id: edge.validation_test.flipkart.cashback_preaggregated.enforces_rule.rule.flipkart.preaggregate_many_side
  edge_type: ENFORCES_RULE
  source: validation_test.flipkart.cashback_preaggregated
  target: rule.flipkart.preaggregate_many_side
  fields:
    edge_family: execution_guidance
    evidence_basis: deterministic rule/test semantic mapping
    confidence: high
    canonical_cognee_edge: true
    marketplace_only: true
    canonical_edge_type: ENFORCES_RULE
    inverse_edge_type: HAS_VALIDATION_TEST
    materialize_inverse: true
    edge_class: canonical
    source_type: validation_test
    target_type: rule
```

```yaml
candidate_edge:
  edge_id: edge.rule.flipkart.cashback_signed.has_validation_test.validation_test.flipkart.cashback_null_preserved
  edge_type: HAS_VALIDATION_TEST
  source: rule.flipkart.cashback_signed
  target: validation_test.flipkart.cashback_null_preserved
  fields:
    edge_family: execution_guidance
    evidence_basis: deterministic rule/test semantic mapping
    confidence: high
    canonical_cognee_edge: true
    marketplace_only: true
    canonical_edge_type: HAS_VALIDATION_TEST
    inverse_edge_type: ENFORCES_RULE
    materialize_inverse: true
    edge_class: canonical
    source_type: rule
    target_type: validation_test
```

```yaml
candidate_edge:
  edge_id: edge.validation_test.flipkart.cashback_null_preserved.enforces_rule.rule.flipkart.cashback_signed
  edge_type: ENFORCES_RULE
  source: validation_test.flipkart.cashback_null_preserved
  target: rule.flipkart.cashback_signed
  fields:
    edge_family: execution_guidance
    evidence_basis: deterministic rule/test semantic mapping
    confidence: high
    canonical_cognee_edge: true
    marketplace_only: true
    canonical_edge_type: ENFORCES_RULE
    inverse_edge_type: HAS_VALIDATION_TEST
    materialize_inverse: true
    edge_class: canonical
    source_type: validation_test
    target_type: rule
```

```yaml
candidate_edge:
  edge_id: edge.rule.flipkart.cashback_signed.has_validation_test.validation_test.flipkart.cashback_offer_recon
  edge_type: HAS_VALIDATION_TEST
  source: rule.flipkart.cashback_signed
  target: validation_test.flipkart.cashback_offer_recon
  fields:
    edge_family: execution_guidance
    evidence_basis: deterministic rule/test semantic mapping
    confidence: high
    canonical_cognee_edge: true
    marketplace_only: true
    canonical_edge_type: HAS_VALIDATION_TEST
    inverse_edge_type: ENFORCES_RULE
    materialize_inverse: true
    edge_class: canonical
    source_type: rule
    target_type: validation_test
```

```yaml
candidate_edge:
  edge_id: edge.validation_test.flipkart.cashback_offer_recon.enforces_rule.rule.flipkart.cashback_signed
  edge_type: ENFORCES_RULE
  source: validation_test.flipkart.cashback_offer_recon
  target: rule.flipkart.cashback_signed
  fields:
    edge_family: execution_guidance
    evidence_basis: deterministic rule/test semantic mapping
    confidence: high
    canonical_cognee_edge: true
    marketplace_only: true
    canonical_edge_type: ENFORCES_RULE
    inverse_edge_type: HAS_VALIDATION_TEST
    materialize_inverse: true
    edge_class: canonical
    source_type: validation_test
    target_type: rule
```

```yaml
candidate_edge:
  edge_id: edge.rule.flipkart.mp_fee_preferred.has_validation_test.validation_test.flipkart.mp_fee_recon
  edge_type: HAS_VALIDATION_TEST
  source: rule.flipkart.mp_fee_preferred
  target: validation_test.flipkart.mp_fee_recon
  fields:
    edge_family: execution_guidance
    evidence_basis: deterministic rule/test semantic mapping
    confidence: high
    canonical_cognee_edge: true
    marketplace_only: true
    canonical_edge_type: HAS_VALIDATION_TEST
    inverse_edge_type: ENFORCES_RULE
    materialize_inverse: true
    edge_class: canonical
    source_type: rule
    target_type: validation_test
```

```yaml
candidate_edge:
  edge_id: edge.validation_test.flipkart.mp_fee_recon.enforces_rule.rule.flipkart.mp_fee_preferred
  edge_type: ENFORCES_RULE
  source: validation_test.flipkart.mp_fee_recon
  target: rule.flipkart.mp_fee_preferred
  fields:
    edge_family: execution_guidance
    evidence_basis: deterministic rule/test semantic mapping
    confidence: high
    canonical_cognee_edge: true
    marketplace_only: true
    canonical_edge_type: ENFORCES_RULE
    inverse_edge_type: HAS_VALIDATION_TEST
    materialize_inverse: true
    edge_class: canonical
    source_type: validation_test
    target_type: rule
```

```yaml
candidate_edge:
  edge_id: edge.rule.flipkart.no_bank_cards.has_validation_test.validation_test.flipkart.no_bank_recon
  edge_type: HAS_VALIDATION_TEST
  source: rule.flipkart.no_bank_cards
  target: validation_test.flipkart.no_bank_recon
  fields:
    edge_family: execution_guidance
    evidence_basis: deterministic rule/test semantic mapping
    confidence: high
    canonical_cognee_edge: true
    marketplace_only: true
    canonical_edge_type: HAS_VALIDATION_TEST
    inverse_edge_type: ENFORCES_RULE
    materialize_inverse: true
    edge_class: canonical
    source_type: rule
    target_type: validation_test
```

```yaml
candidate_edge:
  edge_id: edge.validation_test.flipkart.no_bank_recon.enforces_rule.rule.flipkart.no_bank_cards
  edge_type: ENFORCES_RULE
  source: validation_test.flipkart.no_bank_recon
  target: rule.flipkart.no_bank_cards
  fields:
    edge_family: execution_guidance
    evidence_basis: deterministic rule/test semantic mapping
    confidence: high
    canonical_cognee_edge: true
    marketplace_only: true
    canonical_edge_type: ENFORCES_RULE
    inverse_edge_type: HAS_VALIDATION_TEST
    materialize_inverse: true
    edge_class: canonical
    source_type: validation_test
    target_type: rule
```

```yaml
candidate_edge:
  edge_id: edge.rule.flipkart.fulfilment_marketplace_only.has_validation_test.validation_test.flipkart.no_external_logistics
  edge_type: HAS_VALIDATION_TEST
  source: rule.flipkart.fulfilment_marketplace_only
  target: validation_test.flipkart.no_external_logistics
  fields:
    edge_family: execution_guidance
    evidence_basis: deterministic rule/test semantic mapping
    confidence: high
    canonical_cognee_edge: true
    marketplace_only: true
    canonical_edge_type: HAS_VALIDATION_TEST
    inverse_edge_type: ENFORCES_RULE
    materialize_inverse: true
    edge_class: canonical
    source_type: rule
    target_type: validation_test
```

```yaml
candidate_edge:
  edge_id: edge.validation_test.flipkart.no_external_logistics.enforces_rule.rule.flipkart.fulfilment_marketplace_only
  edge_type: ENFORCES_RULE
  source: validation_test.flipkart.no_external_logistics
  target: rule.flipkart.fulfilment_marketplace_only
  fields:
    edge_family: execution_guidance
    evidence_basis: deterministic rule/test semantic mapping
    confidence: high
    canonical_cognee_edge: true
    marketplace_only: true
    canonical_edge_type: ENFORCES_RULE
    inverse_edge_type: HAS_VALIDATION_TEST
    materialize_inverse: true
    edge_class: canonical
    source_type: validation_test
    target_type: rule
```

```yaml
candidate_edge:
  edge_id: edge.execution_constraint_set.flipkart.marketplace_only.includes_rule.rule.flipkart.group_scope_as_column
  edge_type: INCLUDES_RULE
  source: execution_constraint_set.flipkart.marketplace_only
  target: rule.flipkart.group_scope_as_column
  fields:
    edge_family: execution_guidance
    evidence_basis: deterministic constraint/rule semantic mapping
    confidence: high
    canonical_cognee_edge: true
    marketplace_only: true
    canonical_edge_type: INCLUDES_RULE
    legacy_edge_aliases:
    - rule_enforced_by_constraint
    inverse_edge_type: INCLUDED_IN_CONSTRAINT_SET
    materialize_inverse: false
    edge_class: canonical
    source_type: execution_constraint_set
    target_type: rule
```

```yaml
candidate_edge:
  edge_id: edge.execution_constraint_set.flipkart.marketplace_only.includes_rule.rule.flipkart.no_bank_cards
  edge_type: INCLUDES_RULE
  source: execution_constraint_set.flipkart.marketplace_only
  target: rule.flipkart.no_bank_cards
  fields:
    edge_family: execution_guidance
    evidence_basis: deterministic constraint/rule semantic mapping
    confidence: high
    canonical_cognee_edge: true
    marketplace_only: true
    canonical_edge_type: INCLUDES_RULE
    legacy_edge_aliases:
    - rule_enforced_by_constraint
    inverse_edge_type: INCLUDED_IN_CONSTRAINT_SET
    materialize_inverse: false
    edge_class: canonical
    source_type: execution_constraint_set
    target_type: rule
```

```yaml
candidate_edge:
  edge_id: edge.execution_constraint_set.flipkart.marketplace_only.includes_rule.rule.flipkart.fulfilment_marketplace_only
  edge_type: INCLUDES_RULE
  source: execution_constraint_set.flipkart.marketplace_only
  target: rule.flipkart.fulfilment_marketplace_only
  fields:
    edge_family: execution_guidance
    evidence_basis: deterministic constraint/rule semantic mapping
    confidence: high
    canonical_cognee_edge: true
    marketplace_only: true
    canonical_edge_type: INCLUDES_RULE
    legacy_edge_aliases:
    - rule_enforced_by_constraint
    inverse_edge_type: INCLUDED_IN_CONSTRAINT_SET
    materialize_inverse: false
    edge_class: canonical
    source_type: execution_constraint_set
    target_type: rule
```

```yaml
candidate_edge:
  edge_id: edge.execution_constraint_set.flipkart.active_filters.includes_rule.rule.flipkart.active_filter
  edge_type: INCLUDES_RULE
  source: execution_constraint_set.flipkart.active_filters
  target: rule.flipkart.active_filter
  fields:
    edge_family: execution_guidance
    evidence_basis: deterministic constraint/rule semantic mapping
    confidence: high
    canonical_cognee_edge: true
    marketplace_only: true
    canonical_edge_type: INCLUDES_RULE
    legacy_edge_aliases:
    - rule_enforced_by_constraint
    inverse_edge_type: INCLUDED_IN_CONSTRAINT_SET
    materialize_inverse: false
    edge_class: canonical
    source_type: execution_constraint_set
    target_type: rule
```

```yaml
candidate_edge:
  edge_id: edge.execution_constraint_set.flipkart.preaggregation.includes_rule.rule.flipkart.preaggregate_many_side
  edge_type: INCLUDES_RULE
  source: execution_constraint_set.flipkart.preaggregation
  target: rule.flipkart.preaggregate_many_side
  fields:
    edge_family: execution_guidance
    evidence_basis: deterministic constraint/rule semantic mapping
    confidence: high
    canonical_cognee_edge: true
    marketplace_only: true
    canonical_edge_type: INCLUDES_RULE
    legacy_edge_aliases:
    - rule_enforced_by_constraint
    inverse_edge_type: INCLUDED_IN_CONSTRAINT_SET
    materialize_inverse: false
    edge_class: canonical
    source_type: execution_constraint_set
    target_type: rule
```

```yaml
candidate_edge:
  edge_id: edge.execution_constraint_set.flipkart.order_id_normalization.includes_rule.rule.flipkart.commission_od_normalization
  edge_type: INCLUDES_RULE
  source: execution_constraint_set.flipkart.order_id_normalization
  target: rule.flipkart.commission_od_normalization
  fields:
    edge_family: execution_guidance
    evidence_basis: deterministic constraint/rule semantic mapping
    confidence: high
    canonical_cognee_edge: true
    marketplace_only: true
    canonical_edge_type: INCLUDES_RULE
    legacy_edge_aliases:
    - rule_enforced_by_constraint
    inverse_edge_type: INCLUDED_IN_CONSTRAINT_SET
    materialize_inverse: false
    edge_class: canonical
    source_type: execution_constraint_set
    target_type: rule
```

```yaml
candidate_edge:
  edge_id: edge.execution_constraint_set.flipkart.sign_handling.includes_rule.rule.flipkart.cashback_signed
  edge_type: INCLUDES_RULE
  source: execution_constraint_set.flipkart.sign_handling
  target: rule.flipkart.cashback_signed
  fields:
    edge_family: execution_guidance
    evidence_basis: deterministic constraint/rule semantic mapping
    confidence: high
    canonical_cognee_edge: true
    marketplace_only: true
    canonical_edge_type: INCLUDES_RULE
    legacy_edge_aliases:
    - rule_enforced_by_constraint
    inverse_edge_type: INCLUDED_IN_CONSTRAINT_SET
    materialize_inverse: false
    edge_class: canonical
    source_type: execution_constraint_set
    target_type: rule
```

```yaml
candidate_edge:
  edge_id: edge.execution_constraint_set.flipkart.tax_boundary.includes_rule.rule.flipkart.tcs_tds_not_cost
  edge_type: INCLUDES_RULE
  source: execution_constraint_set.flipkart.tax_boundary
  target: rule.flipkart.tcs_tds_not_cost
  fields:
    edge_family: execution_guidance
    evidence_basis: deterministic constraint/rule semantic mapping
    confidence: high
    canonical_cognee_edge: true
    marketplace_only: true
    canonical_edge_type: INCLUDES_RULE
    legacy_edge_aliases:
    - rule_enforced_by_constraint
    inverse_edge_type: INCLUDED_IN_CONSTRAINT_SET
    materialize_inverse: false
    edge_class: canonical
    source_type: execution_constraint_set
    target_type: rule
```

```yaml
candidate_edge:
  edge_id: edge.execution_constraint_set.flipkart.fulfilment_boundary.includes_rule.rule.flipkart.fulfilment_marketplace_only
  edge_type: INCLUDES_RULE
  source: execution_constraint_set.flipkart.fulfilment_boundary
  target: rule.flipkart.fulfilment_marketplace_only
  fields:
    edge_family: execution_guidance
    evidence_basis: deterministic constraint/rule semantic mapping
    confidence: high
    canonical_cognee_edge: true
    marketplace_only: true
    canonical_edge_type: INCLUDES_RULE
    legacy_edge_aliases:
    - rule_enforced_by_constraint
    inverse_edge_type: INCLUDED_IN_CONSTRAINT_SET
    materialize_inverse: false
    edge_class: canonical
    source_type: execution_constraint_set
    target_type: rule
```

```yaml
candidate_edge:
  edge_id: edge.execution_constraint_set.flipkart.marketplace_only.includes_validation_test.validation_test.flipkart.group_not_binding
  edge_type: INCLUDES_VALIDATION_TEST
  source: execution_constraint_set.flipkart.marketplace_only
  target: validation_test.flipkart.group_not_binding
  fields:
    edge_family: execution_guidance
    evidence_basis: deterministic constraint/test semantic mapping
    confidence: high
    canonical_cognee_edge: true
    marketplace_only: true
    canonical_edge_type: INCLUDES_VALIDATION_TEST
    legacy_edge_aliases:
    - validation_enforces_constraint
    inverse_edge_type: INCLUDED_IN_CONSTRAINT_SET
    materialize_inverse: false
    edge_class: canonical
    source_type: execution_constraint_set
    target_type: validation_test
```

```yaml
candidate_edge:
  edge_id: edge.execution_constraint_set.flipkart.marketplace_only.includes_validation_test.validation_test.flipkart.no_bank_recon
  edge_type: INCLUDES_VALIDATION_TEST
  source: execution_constraint_set.flipkart.marketplace_only
  target: validation_test.flipkart.no_bank_recon
  fields:
    edge_family: execution_guidance
    evidence_basis: deterministic constraint/test semantic mapping
    confidence: high
    canonical_cognee_edge: true
    marketplace_only: true
    canonical_edge_type: INCLUDES_VALIDATION_TEST
    legacy_edge_aliases:
    - validation_enforces_constraint
    inverse_edge_type: INCLUDED_IN_CONSTRAINT_SET
    materialize_inverse: false
    edge_class: canonical
    source_type: execution_constraint_set
    target_type: validation_test
```

```yaml
candidate_edge:
  edge_id: edge.execution_constraint_set.flipkart.marketplace_only.includes_validation_test.validation_test.flipkart.no_external_logistics
  edge_type: INCLUDES_VALIDATION_TEST
  source: execution_constraint_set.flipkart.marketplace_only
  target: validation_test.flipkart.no_external_logistics
  fields:
    edge_family: execution_guidance
    evidence_basis: deterministic constraint/test semantic mapping
    confidence: high
    canonical_cognee_edge: true
    marketplace_only: true
    canonical_edge_type: INCLUDES_VALIDATION_TEST
    legacy_edge_aliases:
    - validation_enforces_constraint
    inverse_edge_type: INCLUDED_IN_CONSTRAINT_SET
    materialize_inverse: false
    edge_class: canonical
    source_type: execution_constraint_set
    target_type: validation_test
```

```yaml
candidate_edge:
  edge_id: edge.execution_constraint_set.flipkart.active_filters.includes_validation_test.validation_test.flipkart.active_filter_present
  edge_type: INCLUDES_VALIDATION_TEST
  source: execution_constraint_set.flipkart.active_filters
  target: validation_test.flipkart.active_filter_present
  fields:
    edge_family: execution_guidance
    evidence_basis: deterministic constraint/test semantic mapping
    confidence: high
    canonical_cognee_edge: true
    marketplace_only: true
    canonical_edge_type: INCLUDES_VALIDATION_TEST
    legacy_edge_aliases:
    - validation_enforces_constraint
    inverse_edge_type: INCLUDED_IN_CONSTRAINT_SET
    materialize_inverse: false
    edge_class: canonical
    source_type: execution_constraint_set
    target_type: validation_test
```

```yaml
candidate_edge:
  edge_id: edge.execution_constraint_set.flipkart.preaggregation.includes_validation_test.validation_test.flipkart.commission_preaggregated
  edge_type: INCLUDES_VALIDATION_TEST
  source: execution_constraint_set.flipkart.preaggregation
  target: validation_test.flipkart.commission_preaggregated
  fields:
    edge_family: execution_guidance
    evidence_basis: deterministic constraint/test semantic mapping
    confidence: high
    canonical_cognee_edge: true
    marketplace_only: true
    canonical_edge_type: INCLUDES_VALIDATION_TEST
    legacy_edge_aliases:
    - validation_enforces_constraint
    inverse_edge_type: INCLUDED_IN_CONSTRAINT_SET
    materialize_inverse: false
    edge_class: canonical
    source_type: execution_constraint_set
    target_type: validation_test
```

```yaml
candidate_edge:
  edge_id: edge.execution_constraint_set.flipkart.preaggregation.includes_validation_test.validation_test.flipkart.cashback_preaggregated
  edge_type: INCLUDES_VALIDATION_TEST
  source: execution_constraint_set.flipkart.preaggregation
  target: validation_test.flipkart.cashback_preaggregated
  fields:
    edge_family: execution_guidance
    evidence_basis: deterministic constraint/test semantic mapping
    confidence: high
    canonical_cognee_edge: true
    marketplace_only: true
    canonical_edge_type: INCLUDES_VALIDATION_TEST
    legacy_edge_aliases:
    - validation_enforces_constraint
    inverse_edge_type: INCLUDED_IN_CONSTRAINT_SET
    materialize_inverse: false
    edge_class: canonical
    source_type: execution_constraint_set
    target_type: validation_test
```

```yaml
candidate_edge:
  edge_id: edge.execution_constraint_set.flipkart.order_id_normalization.includes_validation_test.validation_test.flipkart.commission_order_id_normalized
  edge_type: INCLUDES_VALIDATION_TEST
  source: execution_constraint_set.flipkart.order_id_normalization
  target: validation_test.flipkart.commission_order_id_normalized
  fields:
    edge_family: execution_guidance
    evidence_basis: deterministic constraint/test semantic mapping
    confidence: high
    canonical_cognee_edge: true
    marketplace_only: true
    canonical_edge_type: INCLUDES_VALIDATION_TEST
    legacy_edge_aliases:
    - validation_enforces_constraint
    inverse_edge_type: INCLUDED_IN_CONSTRAINT_SET
    materialize_inverse: false
    edge_class: canonical
    source_type: execution_constraint_set
    target_type: validation_test
```

```yaml
candidate_edge:
  edge_id: edge.execution_constraint_set.flipkart.sign_handling.includes_validation_test.validation_test.flipkart.cashback_null_preserved
  edge_type: INCLUDES_VALIDATION_TEST
  source: execution_constraint_set.flipkart.sign_handling
  target: validation_test.flipkart.cashback_null_preserved
  fields:
    edge_family: execution_guidance
    evidence_basis: deterministic constraint/test semantic mapping
    confidence: high
    canonical_cognee_edge: true
    marketplace_only: true
    canonical_edge_type: INCLUDES_VALIDATION_TEST
    legacy_edge_aliases:
    - validation_enforces_constraint
    inverse_edge_type: INCLUDED_IN_CONSTRAINT_SET
    materialize_inverse: false
    edge_class: canonical
    source_type: execution_constraint_set
    target_type: validation_test
```

```yaml
candidate_edge:
  edge_id: edge.execution_constraint_set.flipkart.fulfilment_boundary.includes_validation_test.validation_test.flipkart.no_external_logistics
  edge_type: INCLUDES_VALIDATION_TEST
  source: execution_constraint_set.flipkart.fulfilment_boundary
  target: validation_test.flipkart.no_external_logistics
  fields:
    edge_family: execution_guidance
    evidence_basis: deterministic constraint/test semantic mapping
    confidence: high
    canonical_cognee_edge: true
    marketplace_only: true
    canonical_edge_type: INCLUDES_VALIDATION_TEST
    legacy_edge_aliases:
    - validation_enforces_constraint
    inverse_edge_type: INCLUDED_IN_CONSTRAINT_SET
    materialize_inverse: false
    edge_class: canonical
    source_type: execution_constraint_set
    target_type: validation_test
```

```yaml
candidate_edge:
  edge_id: edge.execution_constraint_set.flipkart.marketplace_only.applies_to_query_pattern.query_pattern.flipkart.gmv
  edge_type: APPLIES_TO_QUERY_PATTERN
  source: execution_constraint_set.flipkart.marketplace_only
  target: query_pattern.flipkart.gmv
  fields:
    edge_family: execution_guidance
    evidence_basis: deterministic constraint/query semantic mapping
    confidence: high
    canonical_cognee_edge: true
    marketplace_only: true
    canonical_edge_type: APPLIES_TO_QUERY_PATTERN
    inverse_edge_type: HAS_EXECUTION_CONSTRAINT_SET
    materialize_inverse: false
    edge_class: canonical
    source_type: execution_constraint_set
    target_type: query_pattern
```

```yaml
candidate_edge:
  edge_id: edge.execution_constraint_set.flipkart.marketplace_only.applies_to_query_pattern.query_pattern.flipkart.net_settlement
  edge_type: APPLIES_TO_QUERY_PATTERN
  source: execution_constraint_set.flipkart.marketplace_only
  target: query_pattern.flipkart.net_settlement
  fields:
    edge_family: execution_guidance
    evidence_basis: deterministic constraint/query semantic mapping
    confidence: high
    canonical_cognee_edge: true
    marketplace_only: true
    canonical_edge_type: APPLIES_TO_QUERY_PATTERN
    inverse_edge_type: HAS_EXECUTION_CONSTRAINT_SET
    materialize_inverse: false
    edge_class: canonical
    source_type: execution_constraint_set
    target_type: query_pattern
```

```yaml
candidate_edge:
  edge_id: edge.execution_constraint_set.flipkart.marketplace_only.applies_to_query_pattern.query_pattern.flipkart.realization
  edge_type: APPLIES_TO_QUERY_PATTERN
  source: execution_constraint_set.flipkart.marketplace_only
  target: query_pattern.flipkart.realization
  fields:
    edge_family: execution_guidance
    evidence_basis: deterministic constraint/query semantic mapping
    confidence: high
    canonical_cognee_edge: true
    marketplace_only: true
    canonical_edge_type: APPLIES_TO_QUERY_PATTERN
    inverse_edge_type: HAS_EXECUTION_CONSTRAINT_SET
    materialize_inverse: false
    edge_class: canonical
    source_type: execution_constraint_set
    target_type: query_pattern
```

```yaml
candidate_edge:
  edge_id: edge.execution_constraint_set.flipkart.marketplace_only.applies_to_query_pattern.query_pattern.flipkart.settlement_by_fulfilment
  edge_type: APPLIES_TO_QUERY_PATTERN
  source: execution_constraint_set.flipkart.marketplace_only
  target: query_pattern.flipkart.settlement_by_fulfilment
  fields:
    edge_family: execution_guidance
    evidence_basis: deterministic constraint/query semantic mapping
    confidence: high
    canonical_cognee_edge: true
    marketplace_only: true
    canonical_edge_type: APPLIES_TO_QUERY_PATTERN
    inverse_edge_type: HAS_EXECUTION_CONSTRAINT_SET
    materialize_inverse: false
    edge_class: canonical
    source_type: execution_constraint_set
    target_type: query_pattern
```

```yaml
candidate_edge:
  edge_id: edge.execution_constraint_set.flipkart.marketplace_only.applies_to_query_pattern.query_pattern.flipkart.settlement_cycle
  edge_type: APPLIES_TO_QUERY_PATTERN
  source: execution_constraint_set.flipkart.marketplace_only
  target: query_pattern.flipkart.settlement_cycle
  fields:
    edge_family: execution_guidance
    evidence_basis: deterministic constraint/query semantic mapping
    confidence: high
    canonical_cognee_edge: true
    marketplace_only: true
    canonical_edge_type: APPLIES_TO_QUERY_PATTERN
    inverse_edge_type: HAS_EXECUTION_CONSTRAINT_SET
    materialize_inverse: false
    edge_class: canonical
    source_type: execution_constraint_set
    target_type: query_pattern
```

```yaml
candidate_edge:
  edge_id: edge.execution_constraint_set.flipkart.marketplace_only.applies_to_query_pattern.query_pattern.flipkart.fee_breakdown
  edge_type: APPLIES_TO_QUERY_PATTERN
  source: execution_constraint_set.flipkart.marketplace_only
  target: query_pattern.flipkart.fee_breakdown
  fields:
    edge_family: execution_guidance
    evidence_basis: deterministic constraint/query semantic mapping
    confidence: high
    canonical_cognee_edge: true
    marketplace_only: true
    canonical_edge_type: APPLIES_TO_QUERY_PATTERN
    inverse_edge_type: HAS_EXECUTION_CONSTRAINT_SET
    materialize_inverse: false
    edge_class: canonical
    source_type: execution_constraint_set
    target_type: query_pattern
```

```yaml
candidate_edge:
  edge_id: edge.execution_constraint_set.flipkart.marketplace_only.applies_to_query_pattern.query_pattern.flipkart.fee_pivot
  edge_type: APPLIES_TO_QUERY_PATTERN
  source: execution_constraint_set.flipkart.marketplace_only
  target: query_pattern.flipkart.fee_pivot
  fields:
    edge_family: execution_guidance
    evidence_basis: deterministic constraint/query semantic mapping
    confidence: high
    canonical_cognee_edge: true
    marketplace_only: true
    canonical_edge_type: APPLIES_TO_QUERY_PATTERN
    inverse_edge_type: HAS_EXECUTION_CONSTRAINT_SET
    materialize_inverse: false
    edge_class: canonical
    source_type: execution_constraint_set
    target_type: query_pattern
```

```yaml
candidate_edge:
  edge_id: edge.execution_constraint_set.flipkart.marketplace_only.applies_to_query_pattern.query_pattern.flipkart.commission_recon
  edge_type: APPLIES_TO_QUERY_PATTERN
  source: execution_constraint_set.flipkart.marketplace_only
  target: query_pattern.flipkart.commission_recon
  fields:
    edge_family: execution_guidance
    evidence_basis: deterministic constraint/query semantic mapping
    confidence: high
    canonical_cognee_edge: true
    marketplace_only: true
    canonical_edge_type: APPLIES_TO_QUERY_PATTERN
    inverse_edge_type: HAS_EXECUTION_CONSTRAINT_SET
    materialize_inverse: false
    edge_class: canonical
    source_type: execution_constraint_set
    target_type: query_pattern
```

```yaml
candidate_edge:
  edge_id: edge.execution_constraint_set.flipkart.marketplace_only.applies_to_query_pattern.query_pattern.flipkart.cashback
  edge_type: APPLIES_TO_QUERY_PATTERN
  source: execution_constraint_set.flipkart.marketplace_only
  target: query_pattern.flipkart.cashback
  fields:
    edge_family: execution_guidance
    evidence_basis: deterministic constraint/query semantic mapping
    confidence: high
    canonical_cognee_edge: true
    marketplace_only: true
    canonical_edge_type: APPLIES_TO_QUERY_PATTERN
    inverse_edge_type: HAS_EXECUTION_CONSTRAINT_SET
    materialize_inverse: false
    edge_class: canonical
    source_type: execution_constraint_set
    target_type: query_pattern
```

```yaml
candidate_edge:
  edge_id: edge.execution_constraint_set.flipkart.marketplace_only.applies_to_query_pattern.query_pattern.flipkart.cashback_doc_type
  edge_type: APPLIES_TO_QUERY_PATTERN
  source: execution_constraint_set.flipkart.marketplace_only
  target: query_pattern.flipkart.cashback_doc_type
  fields:
    edge_family: execution_guidance
    evidence_basis: deterministic constraint/query semantic mapping
    confidence: high
    canonical_cognee_edge: true
    marketplace_only: true
    canonical_edge_type: APPLIES_TO_QUERY_PATTERN
    inverse_edge_type: HAS_EXECUTION_CONSTRAINT_SET
    materialize_inverse: false
    edge_class: canonical
    source_type: execution_constraint_set
    target_type: query_pattern
```

```yaml
candidate_edge:
  edge_id: edge.execution_constraint_set.flipkart.marketplace_only.applies_to_query_pattern.query_pattern.flipkart.cashback_rate
  edge_type: APPLIES_TO_QUERY_PATTERN
  source: execution_constraint_set.flipkart.marketplace_only
  target: query_pattern.flipkart.cashback_rate
  fields:
    edge_family: execution_guidance
    evidence_basis: deterministic constraint/query semantic mapping
    confidence: high
    canonical_cognee_edge: true
    marketplace_only: true
    canonical_edge_type: APPLIES_TO_QUERY_PATTERN
    inverse_edge_type: HAS_EXECUTION_CONSTRAINT_SET
    materialize_inverse: false
    edge_class: canonical
    source_type: execution_constraint_set
    target_type: query_pattern
```

```yaml
candidate_edge:
  edge_id: edge.execution_constraint_set.flipkart.marketplace_only.applies_to_query_pattern.query_pattern.flipkart.shopsy_cashback
  edge_type: APPLIES_TO_QUERY_PATTERN
  source: execution_constraint_set.flipkart.marketplace_only
  target: query_pattern.flipkart.shopsy_cashback
  fields:
    edge_family: execution_guidance
    evidence_basis: deterministic constraint/query semantic mapping
    confidence: high
    canonical_cognee_edge: true
    marketplace_only: true
    canonical_edge_type: APPLIES_TO_QUERY_PATTERN
    inverse_edge_type: HAS_EXECUTION_CONSTRAINT_SET
    materialize_inverse: false
    edge_class: canonical
    source_type: execution_constraint_set
    target_type: query_pattern
```

```yaml
candidate_edge:
  edge_id: edge.execution_constraint_set.flipkart.marketplace_only.applies_to_query_pattern.query_pattern.flipkart.cashback_offer_recon
  edge_type: APPLIES_TO_QUERY_PATTERN
  source: execution_constraint_set.flipkart.marketplace_only
  target: query_pattern.flipkart.cashback_offer_recon
  fields:
    edge_family: execution_guidance
    evidence_basis: deterministic constraint/query semantic mapping
    confidence: high
    canonical_cognee_edge: true
    marketplace_only: true
    canonical_edge_type: APPLIES_TO_QUERY_PATTERN
    inverse_edge_type: HAS_EXECUTION_CONSTRAINT_SET
    materialize_inverse: false
    edge_class: canonical
    source_type: execution_constraint_set
    target_type: query_pattern
```

```yaml
candidate_edge:
  edge_id: edge.execution_constraint_set.flipkart.marketplace_only.applies_to_query_pattern.query_pattern.flipkart.tcs_tds
  edge_type: APPLIES_TO_QUERY_PATTERN
  source: execution_constraint_set.flipkart.marketplace_only
  target: query_pattern.flipkart.tcs_tds
  fields:
    edge_family: execution_guidance
    evidence_basis: deterministic constraint/query semantic mapping
    confidence: high
    canonical_cognee_edge: true
    marketplace_only: true
    canonical_edge_type: APPLIES_TO_QUERY_PATTERN
    inverse_edge_type: HAS_EXECUTION_CONSTRAINT_SET
    materialize_inverse: false
    edge_class: canonical
    source_type: execution_constraint_set
    target_type: query_pattern
```

```yaml
candidate_edge:
  edge_id: edge.execution_constraint_set.flipkart.marketplace_only.applies_to_query_pattern.query_pattern.flipkart.gst_fees
  edge_type: APPLIES_TO_QUERY_PATTERN
  source: execution_constraint_set.flipkart.marketplace_only
  target: query_pattern.flipkart.gst_fees
  fields:
    edge_family: execution_guidance
    evidence_basis: deterministic constraint/query semantic mapping
    confidence: high
    canonical_cognee_edge: true
    marketplace_only: true
    canonical_edge_type: APPLIES_TO_QUERY_PATTERN
    inverse_edge_type: HAS_EXECUTION_CONSTRAINT_SET
    materialize_inverse: false
    edge_class: canonical
    source_type: execution_constraint_set
    target_type: query_pattern
```

```yaml
candidate_edge:
  edge_id: edge.execution_constraint_set.flipkart.active_filters.applies_to_query_pattern.query_pattern.flipkart.gmv
  edge_type: APPLIES_TO_QUERY_PATTERN
  source: execution_constraint_set.flipkart.active_filters
  target: query_pattern.flipkart.gmv
  fields:
    edge_family: execution_guidance
    evidence_basis: deterministic constraint/query semantic mapping
    confidence: high
    canonical_cognee_edge: true
    marketplace_only: true
    canonical_edge_type: APPLIES_TO_QUERY_PATTERN
    inverse_edge_type: HAS_EXECUTION_CONSTRAINT_SET
    materialize_inverse: false
    edge_class: canonical
    source_type: execution_constraint_set
    target_type: query_pattern
```

```yaml
candidate_edge:
  edge_id: edge.execution_constraint_set.flipkart.active_filters.applies_to_query_pattern.query_pattern.flipkart.net_settlement
  edge_type: APPLIES_TO_QUERY_PATTERN
  source: execution_constraint_set.flipkart.active_filters
  target: query_pattern.flipkart.net_settlement
  fields:
    edge_family: execution_guidance
    evidence_basis: deterministic constraint/query semantic mapping
    confidence: high
    canonical_cognee_edge: true
    marketplace_only: true
    canonical_edge_type: APPLIES_TO_QUERY_PATTERN
    inverse_edge_type: HAS_EXECUTION_CONSTRAINT_SET
    materialize_inverse: false
    edge_class: canonical
    source_type: execution_constraint_set
    target_type: query_pattern
```

```yaml
candidate_edge:
  edge_id: edge.execution_constraint_set.flipkart.active_filters.applies_to_query_pattern.query_pattern.flipkart.realization
  edge_type: APPLIES_TO_QUERY_PATTERN
  source: execution_constraint_set.flipkart.active_filters
  target: query_pattern.flipkart.realization
  fields:
    edge_family: execution_guidance
    evidence_basis: deterministic constraint/query semantic mapping
    confidence: high
    canonical_cognee_edge: true
    marketplace_only: true
    canonical_edge_type: APPLIES_TO_QUERY_PATTERN
    inverse_edge_type: HAS_EXECUTION_CONSTRAINT_SET
    materialize_inverse: false
    edge_class: canonical
    source_type: execution_constraint_set
    target_type: query_pattern
```

```yaml
candidate_edge:
  edge_id: edge.execution_constraint_set.flipkart.active_filters.applies_to_query_pattern.query_pattern.flipkart.settlement_by_fulfilment
  edge_type: APPLIES_TO_QUERY_PATTERN
  source: execution_constraint_set.flipkart.active_filters
  target: query_pattern.flipkart.settlement_by_fulfilment
  fields:
    edge_family: execution_guidance
    evidence_basis: deterministic constraint/query semantic mapping
    confidence: high
    canonical_cognee_edge: true
    marketplace_only: true
    canonical_edge_type: APPLIES_TO_QUERY_PATTERN
    inverse_edge_type: HAS_EXECUTION_CONSTRAINT_SET
    materialize_inverse: false
    edge_class: canonical
    source_type: execution_constraint_set
    target_type: query_pattern
```

```yaml
candidate_edge:
  edge_id: edge.execution_constraint_set.flipkart.active_filters.applies_to_query_pattern.query_pattern.flipkart.settlement_cycle
  edge_type: APPLIES_TO_QUERY_PATTERN
  source: execution_constraint_set.flipkart.active_filters
  target: query_pattern.flipkart.settlement_cycle
  fields:
    edge_family: execution_guidance
    evidence_basis: deterministic constraint/query semantic mapping
    confidence: high
    canonical_cognee_edge: true
    marketplace_only: true
    canonical_edge_type: APPLIES_TO_QUERY_PATTERN
    inverse_edge_type: HAS_EXECUTION_CONSTRAINT_SET
    materialize_inverse: false
    edge_class: canonical
    source_type: execution_constraint_set
    target_type: query_pattern
```

```yaml
candidate_edge:
  edge_id: edge.execution_constraint_set.flipkart.active_filters.applies_to_query_pattern.query_pattern.flipkart.fee_breakdown
  edge_type: APPLIES_TO_QUERY_PATTERN
  source: execution_constraint_set.flipkart.active_filters
  target: query_pattern.flipkart.fee_breakdown
  fields:
    edge_family: execution_guidance
    evidence_basis: deterministic constraint/query semantic mapping
    confidence: high
    canonical_cognee_edge: true
    marketplace_only: true
    canonical_edge_type: APPLIES_TO_QUERY_PATTERN
    inverse_edge_type: HAS_EXECUTION_CONSTRAINT_SET
    materialize_inverse: false
    edge_class: canonical
    source_type: execution_constraint_set
    target_type: query_pattern
```

```yaml
candidate_edge:
  edge_id: edge.execution_constraint_set.flipkart.active_filters.applies_to_query_pattern.query_pattern.flipkart.fee_pivot
  edge_type: APPLIES_TO_QUERY_PATTERN
  source: execution_constraint_set.flipkart.active_filters
  target: query_pattern.flipkart.fee_pivot
  fields:
    edge_family: execution_guidance
    evidence_basis: deterministic constraint/query semantic mapping
    confidence: high
    canonical_cognee_edge: true
    marketplace_only: true
    canonical_edge_type: APPLIES_TO_QUERY_PATTERN
    inverse_edge_type: HAS_EXECUTION_CONSTRAINT_SET
    materialize_inverse: false
    edge_class: canonical
    source_type: execution_constraint_set
    target_type: query_pattern
```

```yaml
candidate_edge:
  edge_id: edge.execution_constraint_set.flipkart.active_filters.applies_to_query_pattern.query_pattern.flipkart.commission_recon
  edge_type: APPLIES_TO_QUERY_PATTERN
  source: execution_constraint_set.flipkart.active_filters
  target: query_pattern.flipkart.commission_recon
  fields:
    edge_family: execution_guidance
    evidence_basis: deterministic constraint/query semantic mapping
    confidence: high
    canonical_cognee_edge: true
    marketplace_only: true
    canonical_edge_type: APPLIES_TO_QUERY_PATTERN
    inverse_edge_type: HAS_EXECUTION_CONSTRAINT_SET
    materialize_inverse: false
    edge_class: canonical
    source_type: execution_constraint_set
    target_type: query_pattern
```

```yaml
candidate_edge:
  edge_id: edge.execution_constraint_set.flipkart.active_filters.applies_to_query_pattern.query_pattern.flipkart.cashback
  edge_type: APPLIES_TO_QUERY_PATTERN
  source: execution_constraint_set.flipkart.active_filters
  target: query_pattern.flipkart.cashback
  fields:
    edge_family: execution_guidance
    evidence_basis: deterministic constraint/query semantic mapping
    confidence: high
    canonical_cognee_edge: true
    marketplace_only: true
    canonical_edge_type: APPLIES_TO_QUERY_PATTERN
    inverse_edge_type: HAS_EXECUTION_CONSTRAINT_SET
    materialize_inverse: false
    edge_class: canonical
    source_type: execution_constraint_set
    target_type: query_pattern
```

```yaml
candidate_edge:
  edge_id: edge.execution_constraint_set.flipkart.active_filters.applies_to_query_pattern.query_pattern.flipkart.cashback_doc_type
  edge_type: APPLIES_TO_QUERY_PATTERN
  source: execution_constraint_set.flipkart.active_filters
  target: query_pattern.flipkart.cashback_doc_type
  fields:
    edge_family: execution_guidance
    evidence_basis: deterministic constraint/query semantic mapping
    confidence: high
    canonical_cognee_edge: true
    marketplace_only: true
    canonical_edge_type: APPLIES_TO_QUERY_PATTERN
    inverse_edge_type: HAS_EXECUTION_CONSTRAINT_SET
    materialize_inverse: false
    edge_class: canonical
    source_type: execution_constraint_set
    target_type: query_pattern
```

```yaml
candidate_edge:
  edge_id: edge.execution_constraint_set.flipkart.active_filters.applies_to_query_pattern.query_pattern.flipkart.cashback_rate
  edge_type: APPLIES_TO_QUERY_PATTERN
  source: execution_constraint_set.flipkart.active_filters
  target: query_pattern.flipkart.cashback_rate
  fields:
    edge_family: execution_guidance
    evidence_basis: deterministic constraint/query semantic mapping
    confidence: high
    canonical_cognee_edge: true
    marketplace_only: true
    canonical_edge_type: APPLIES_TO_QUERY_PATTERN
    inverse_edge_type: HAS_EXECUTION_CONSTRAINT_SET
    materialize_inverse: false
    edge_class: canonical
    source_type: execution_constraint_set
    target_type: query_pattern
```

```yaml
candidate_edge:
  edge_id: edge.execution_constraint_set.flipkart.active_filters.applies_to_query_pattern.query_pattern.flipkart.shopsy_cashback
  edge_type: APPLIES_TO_QUERY_PATTERN
  source: execution_constraint_set.flipkart.active_filters
  target: query_pattern.flipkart.shopsy_cashback
  fields:
    edge_family: execution_guidance
    evidence_basis: deterministic constraint/query semantic mapping
    confidence: high
    canonical_cognee_edge: true
    marketplace_only: true
    canonical_edge_type: APPLIES_TO_QUERY_PATTERN
    inverse_edge_type: HAS_EXECUTION_CONSTRAINT_SET
    materialize_inverse: false
    edge_class: canonical
    source_type: execution_constraint_set
    target_type: query_pattern
```

```yaml
candidate_edge:
  edge_id: edge.execution_constraint_set.flipkart.active_filters.applies_to_query_pattern.query_pattern.flipkart.cashback_offer_recon
  edge_type: APPLIES_TO_QUERY_PATTERN
  source: execution_constraint_set.flipkart.active_filters
  target: query_pattern.flipkart.cashback_offer_recon
  fields:
    edge_family: execution_guidance
    evidence_basis: deterministic constraint/query semantic mapping
    confidence: high
    canonical_cognee_edge: true
    marketplace_only: true
    canonical_edge_type: APPLIES_TO_QUERY_PATTERN
    inverse_edge_type: HAS_EXECUTION_CONSTRAINT_SET
    materialize_inverse: false
    edge_class: canonical
    source_type: execution_constraint_set
    target_type: query_pattern
```

```yaml
candidate_edge:
  edge_id: edge.execution_constraint_set.flipkart.active_filters.applies_to_query_pattern.query_pattern.flipkart.tcs_tds
  edge_type: APPLIES_TO_QUERY_PATTERN
  source: execution_constraint_set.flipkart.active_filters
  target: query_pattern.flipkart.tcs_tds
  fields:
    edge_family: execution_guidance
    evidence_basis: deterministic constraint/query semantic mapping
    confidence: high
    canonical_cognee_edge: true
    marketplace_only: true
    canonical_edge_type: APPLIES_TO_QUERY_PATTERN
    inverse_edge_type: HAS_EXECUTION_CONSTRAINT_SET
    materialize_inverse: false
    edge_class: canonical
    source_type: execution_constraint_set
    target_type: query_pattern
```

```yaml
candidate_edge:
  edge_id: edge.execution_constraint_set.flipkart.active_filters.applies_to_query_pattern.query_pattern.flipkart.gst_fees
  edge_type: APPLIES_TO_QUERY_PATTERN
  source: execution_constraint_set.flipkart.active_filters
  target: query_pattern.flipkart.gst_fees
  fields:
    edge_family: execution_guidance
    evidence_basis: deterministic constraint/query semantic mapping
    confidence: high
    canonical_cognee_edge: true
    marketplace_only: true
    canonical_edge_type: APPLIES_TO_QUERY_PATTERN
    inverse_edge_type: HAS_EXECUTION_CONSTRAINT_SET
    materialize_inverse: false
    edge_class: canonical
    source_type: execution_constraint_set
    target_type: query_pattern
```

```yaml
candidate_edge:
  edge_id: edge.execution_constraint_set.flipkart.preaggregation.applies_to_query_pattern.query_pattern.flipkart.commission_recon
  edge_type: APPLIES_TO_QUERY_PATTERN
  source: execution_constraint_set.flipkart.preaggregation
  target: query_pattern.flipkart.commission_recon
  fields:
    edge_family: execution_guidance
    evidence_basis: deterministic constraint/query semantic mapping
    confidence: high
    canonical_cognee_edge: true
    marketplace_only: true
    canonical_edge_type: APPLIES_TO_QUERY_PATTERN
    inverse_edge_type: HAS_EXECUTION_CONSTRAINT_SET
    materialize_inverse: false
    edge_class: canonical
    source_type: execution_constraint_set
    target_type: query_pattern
```

```yaml
candidate_edge:
  edge_id: edge.execution_constraint_set.flipkart.preaggregation.applies_to_query_pattern.query_pattern.flipkart.cashback_offer_recon
  edge_type: APPLIES_TO_QUERY_PATTERN
  source: execution_constraint_set.flipkart.preaggregation
  target: query_pattern.flipkart.cashback_offer_recon
  fields:
    edge_family: execution_guidance
    evidence_basis: deterministic constraint/query semantic mapping
    confidence: high
    canonical_cognee_edge: true
    marketplace_only: true
    canonical_edge_type: APPLIES_TO_QUERY_PATTERN
    inverse_edge_type: HAS_EXECUTION_CONSTRAINT_SET
    materialize_inverse: false
    edge_class: canonical
    source_type: execution_constraint_set
    target_type: query_pattern
```

```yaml
candidate_edge:
  edge_id: edge.execution_constraint_set.flipkart.preaggregation.applies_to_query_pattern.query_pattern.flipkart.gst_fees
  edge_type: APPLIES_TO_QUERY_PATTERN
  source: execution_constraint_set.flipkart.preaggregation
  target: query_pattern.flipkart.gst_fees
  fields:
    edge_family: execution_guidance
    evidence_basis: deterministic constraint/query semantic mapping
    confidence: high
    canonical_cognee_edge: true
    marketplace_only: true
    canonical_edge_type: APPLIES_TO_QUERY_PATTERN
    inverse_edge_type: HAS_EXECUTION_CONSTRAINT_SET
    materialize_inverse: false
    edge_class: canonical
    source_type: execution_constraint_set
    target_type: query_pattern
```

```yaml
candidate_edge:
  edge_id: edge.execution_constraint_set.flipkart.order_id_normalization.applies_to_query_pattern.query_pattern.flipkart.commission_recon
  edge_type: APPLIES_TO_QUERY_PATTERN
  source: execution_constraint_set.flipkart.order_id_normalization
  target: query_pattern.flipkart.commission_recon
  fields:
    edge_family: execution_guidance
    evidence_basis: deterministic constraint/query semantic mapping
    confidence: high
    canonical_cognee_edge: true
    marketplace_only: true
    canonical_edge_type: APPLIES_TO_QUERY_PATTERN
    inverse_edge_type: HAS_EXECUTION_CONSTRAINT_SET
    materialize_inverse: false
    edge_class: canonical
    source_type: execution_constraint_set
    target_type: query_pattern
```

```yaml
candidate_edge:
  edge_id: edge.execution_constraint_set.flipkart.order_id_normalization.applies_to_query_pattern.query_pattern.flipkart.gst_fees
  edge_type: APPLIES_TO_QUERY_PATTERN
  source: execution_constraint_set.flipkart.order_id_normalization
  target: query_pattern.flipkart.gst_fees
  fields:
    edge_family: execution_guidance
    evidence_basis: deterministic constraint/query semantic mapping
    confidence: high
    canonical_cognee_edge: true
    marketplace_only: true
    canonical_edge_type: APPLIES_TO_QUERY_PATTERN
    inverse_edge_type: HAS_EXECUTION_CONSTRAINT_SET
    materialize_inverse: false
    edge_class: canonical
    source_type: execution_constraint_set
    target_type: query_pattern
```

```yaml
candidate_edge:
  edge_id: edge.execution_constraint_set.flipkart.sign_handling.applies_to_query_pattern.query_pattern.flipkart.cashback
  edge_type: APPLIES_TO_QUERY_PATTERN
  source: execution_constraint_set.flipkart.sign_handling
  target: query_pattern.flipkart.cashback
  fields:
    edge_family: execution_guidance
    evidence_basis: deterministic constraint/query semantic mapping
    confidence: high
    canonical_cognee_edge: true
    marketplace_only: true
    canonical_edge_type: APPLIES_TO_QUERY_PATTERN
    inverse_edge_type: HAS_EXECUTION_CONSTRAINT_SET
    materialize_inverse: false
    edge_class: canonical
    source_type: execution_constraint_set
    target_type: query_pattern
```

```yaml
candidate_edge:
  edge_id: edge.execution_constraint_set.flipkart.sign_handling.applies_to_query_pattern.query_pattern.flipkart.cashback_doc_type
  edge_type: APPLIES_TO_QUERY_PATTERN
  source: execution_constraint_set.flipkart.sign_handling
  target: query_pattern.flipkart.cashback_doc_type
  fields:
    edge_family: execution_guidance
    evidence_basis: deterministic constraint/query semantic mapping
    confidence: high
    canonical_cognee_edge: true
    marketplace_only: true
    canonical_edge_type: APPLIES_TO_QUERY_PATTERN
    inverse_edge_type: HAS_EXECUTION_CONSTRAINT_SET
    materialize_inverse: false
    edge_class: canonical
    source_type: execution_constraint_set
    target_type: query_pattern
```

```yaml
candidate_edge:
  edge_id: edge.execution_constraint_set.flipkart.sign_handling.applies_to_query_pattern.query_pattern.flipkart.cashback_rate
  edge_type: APPLIES_TO_QUERY_PATTERN
  source: execution_constraint_set.flipkart.sign_handling
  target: query_pattern.flipkart.cashback_rate
  fields:
    edge_family: execution_guidance
    evidence_basis: deterministic constraint/query semantic mapping
    confidence: high
    canonical_cognee_edge: true
    marketplace_only: true
    canonical_edge_type: APPLIES_TO_QUERY_PATTERN
    inverse_edge_type: HAS_EXECUTION_CONSTRAINT_SET
    materialize_inverse: false
    edge_class: canonical
    source_type: execution_constraint_set
    target_type: query_pattern
```

```yaml
candidate_edge:
  edge_id: edge.execution_constraint_set.flipkart.sign_handling.applies_to_query_pattern.query_pattern.flipkart.shopsy_cashback
  edge_type: APPLIES_TO_QUERY_PATTERN
  source: execution_constraint_set.flipkart.sign_handling
  target: query_pattern.flipkart.shopsy_cashback
  fields:
    edge_family: execution_guidance
    evidence_basis: deterministic constraint/query semantic mapping
    confidence: high
    canonical_cognee_edge: true
    marketplace_only: true
    canonical_edge_type: APPLIES_TO_QUERY_PATTERN
    inverse_edge_type: HAS_EXECUTION_CONSTRAINT_SET
    materialize_inverse: false
    edge_class: canonical
    source_type: execution_constraint_set
    target_type: query_pattern
```

```yaml
candidate_edge:
  edge_id: edge.execution_constraint_set.flipkart.sign_handling.applies_to_query_pattern.query_pattern.flipkart.cashback_offer_recon
  edge_type: APPLIES_TO_QUERY_PATTERN
  source: execution_constraint_set.flipkart.sign_handling
  target: query_pattern.flipkart.cashback_offer_recon
  fields:
    edge_family: execution_guidance
    evidence_basis: deterministic constraint/query semantic mapping
    confidence: high
    canonical_cognee_edge: true
    marketplace_only: true
    canonical_edge_type: APPLIES_TO_QUERY_PATTERN
    inverse_edge_type: HAS_EXECUTION_CONSTRAINT_SET
    materialize_inverse: false
    edge_class: canonical
    source_type: execution_constraint_set
    target_type: query_pattern
```

```yaml
candidate_edge:
  edge_id: edge.execution_constraint_set.flipkart.date_basis.applies_to_query_pattern.query_pattern.flipkart.settlement_cycle
  edge_type: APPLIES_TO_QUERY_PATTERN
  source: execution_constraint_set.flipkart.date_basis
  target: query_pattern.flipkart.settlement_cycle
  fields:
    edge_family: execution_guidance
    evidence_basis: deterministic constraint/query semantic mapping
    confidence: high
    canonical_cognee_edge: true
    marketplace_only: true
    canonical_edge_type: APPLIES_TO_QUERY_PATTERN
    inverse_edge_type: HAS_EXECUTION_CONSTRAINT_SET
    materialize_inverse: false
    edge_class: canonical
    source_type: execution_constraint_set
    target_type: query_pattern
```

```yaml
candidate_edge:
  edge_id: edge.execution_constraint_set.flipkart.date_basis.applies_to_query_pattern.query_pattern.flipkart.net_settlement
  edge_type: APPLIES_TO_QUERY_PATTERN
  source: execution_constraint_set.flipkart.date_basis
  target: query_pattern.flipkart.net_settlement
  fields:
    edge_family: execution_guidance
    evidence_basis: deterministic constraint/query semantic mapping
    confidence: high
    canonical_cognee_edge: true
    marketplace_only: true
    canonical_edge_type: APPLIES_TO_QUERY_PATTERN
    inverse_edge_type: HAS_EXECUTION_CONSTRAINT_SET
    materialize_inverse: false
    edge_class: canonical
    source_type: execution_constraint_set
    target_type: query_pattern
```

```yaml
candidate_edge:
  edge_id: edge.execution_constraint_set.flipkart.date_basis.applies_to_query_pattern.query_pattern.flipkart.realization
  edge_type: APPLIES_TO_QUERY_PATTERN
  source: execution_constraint_set.flipkart.date_basis
  target: query_pattern.flipkart.realization
  fields:
    edge_family: execution_guidance
    evidence_basis: deterministic constraint/query semantic mapping
    confidence: high
    canonical_cognee_edge: true
    marketplace_only: true
    canonical_edge_type: APPLIES_TO_QUERY_PATTERN
    inverse_edge_type: HAS_EXECUTION_CONSTRAINT_SET
    materialize_inverse: false
    edge_class: canonical
    source_type: execution_constraint_set
    target_type: query_pattern
```

```yaml
candidate_edge:
  edge_id: edge.execution_constraint_set.flipkart.tax_boundary.applies_to_query_pattern.query_pattern.flipkart.tcs_tds
  edge_type: APPLIES_TO_QUERY_PATTERN
  source: execution_constraint_set.flipkart.tax_boundary
  target: query_pattern.flipkart.tcs_tds
  fields:
    edge_family: execution_guidance
    evidence_basis: deterministic constraint/query semantic mapping
    confidence: high
    canonical_cognee_edge: true
    marketplace_only: true
    canonical_edge_type: APPLIES_TO_QUERY_PATTERN
    inverse_edge_type: HAS_EXECUTION_CONSTRAINT_SET
    materialize_inverse: false
    edge_class: canonical
    source_type: execution_constraint_set
    target_type: query_pattern
```

```yaml
candidate_edge:
  edge_id: edge.execution_constraint_set.flipkart.tax_boundary.applies_to_query_pattern.query_pattern.flipkart.gst_fees
  edge_type: APPLIES_TO_QUERY_PATTERN
  source: execution_constraint_set.flipkart.tax_boundary
  target: query_pattern.flipkart.gst_fees
  fields:
    edge_family: execution_guidance
    evidence_basis: deterministic constraint/query semantic mapping
    confidence: high
    canonical_cognee_edge: true
    marketplace_only: true
    canonical_edge_type: APPLIES_TO_QUERY_PATTERN
    inverse_edge_type: HAS_EXECUTION_CONSTRAINT_SET
    materialize_inverse: false
    edge_class: canonical
    source_type: execution_constraint_set
    target_type: query_pattern
```

```yaml
candidate_edge:
  edge_id: edge.execution_constraint_set.flipkart.fulfilment_boundary.applies_to_query_pattern.query_pattern.flipkart.settlement_by_fulfilment
  edge_type: APPLIES_TO_QUERY_PATTERN
  source: execution_constraint_set.flipkart.fulfilment_boundary
  target: query_pattern.flipkart.settlement_by_fulfilment
  fields:
    edge_family: execution_guidance
    evidence_basis: deterministic constraint/query semantic mapping
    confidence: high
    canonical_cognee_edge: true
    marketplace_only: true
    canonical_edge_type: APPLIES_TO_QUERY_PATTERN
    inverse_edge_type: HAS_EXECUTION_CONSTRAINT_SET
    materialize_inverse: false
    edge_class: canonical
    source_type: execution_constraint_set
    target_type: query_pattern
```

```yaml
candidate_edge:
  edge_id: edge.execution_constraint_set.flipkart.marketplace_only.uses_output_contract.output_contract.flipkart.settlement_summary
  edge_type: USES_OUTPUT_CONTRACT
  source: execution_constraint_set.flipkart.marketplace_only
  target: output_contract.flipkart.settlement_summary
  fields:
    edge_family: execution_guidance
    evidence_basis: deterministic constraint/output semantic mapping
    confidence: high
    canonical_cognee_edge: true
    marketplace_only: true
    canonical_edge_type: USES_OUTPUT_CONTRACT
    inverse_edge_type: USED_BY_CONSTRAINT_SET
    materialize_inverse: false
    edge_class: canonical
    source_type: execution_constraint_set
    target_type: output_contract
```

```yaml
candidate_edge:
  edge_id: edge.execution_constraint_set.flipkart.active_filters.uses_output_contract.output_contract.flipkart.settlement_summary
  edge_type: USES_OUTPUT_CONTRACT
  source: execution_constraint_set.flipkart.active_filters
  target: output_contract.flipkart.settlement_summary
  fields:
    edge_family: execution_guidance
    evidence_basis: deterministic constraint/output semantic mapping
    confidence: high
    canonical_cognee_edge: true
    marketplace_only: true
    canonical_edge_type: USES_OUTPUT_CONTRACT
    inverse_edge_type: USED_BY_CONSTRAINT_SET
    materialize_inverse: false
    edge_class: canonical
    source_type: execution_constraint_set
    target_type: output_contract
```

```yaml
candidate_edge:
  edge_id: edge.execution_constraint_set.flipkart.preaggregation.uses_output_contract.output_contract.flipkart.commission_recon
  edge_type: USES_OUTPUT_CONTRACT
  source: execution_constraint_set.flipkart.preaggregation
  target: output_contract.flipkart.commission_recon
  fields:
    edge_family: execution_guidance
    evidence_basis: deterministic constraint/output semantic mapping
    confidence: high
    canonical_cognee_edge: true
    marketplace_only: true
    canonical_edge_type: USES_OUTPUT_CONTRACT
    inverse_edge_type: USED_BY_CONSTRAINT_SET
    materialize_inverse: false
    edge_class: canonical
    source_type: execution_constraint_set
    target_type: output_contract
```

```yaml
candidate_edge:
  edge_id: edge.execution_constraint_set.flipkart.order_id_normalization.uses_output_contract.output_contract.flipkart.commission_recon
  edge_type: USES_OUTPUT_CONTRACT
  source: execution_constraint_set.flipkart.order_id_normalization
  target: output_contract.flipkart.commission_recon
  fields:
    edge_family: execution_guidance
    evidence_basis: deterministic constraint/output semantic mapping
    confidence: high
    canonical_cognee_edge: true
    marketplace_only: true
    canonical_edge_type: USES_OUTPUT_CONTRACT
    inverse_edge_type: USED_BY_CONSTRAINT_SET
    materialize_inverse: false
    edge_class: canonical
    source_type: execution_constraint_set
    target_type: output_contract
```

```yaml
candidate_edge:
  edge_id: edge.execution_constraint_set.flipkart.sign_handling.uses_output_contract.output_contract.flipkart.cashback_recon
  edge_type: USES_OUTPUT_CONTRACT
  source: execution_constraint_set.flipkart.sign_handling
  target: output_contract.flipkart.cashback_recon
  fields:
    edge_family: execution_guidance
    evidence_basis: deterministic constraint/output semantic mapping
    confidence: high
    canonical_cognee_edge: true
    marketplace_only: true
    canonical_edge_type: USES_OUTPUT_CONTRACT
    inverse_edge_type: USED_BY_CONSTRAINT_SET
    materialize_inverse: false
    edge_class: canonical
    source_type: execution_constraint_set
    target_type: output_contract
```

```yaml
candidate_edge:
  edge_id: edge.execution_constraint_set.flipkart.date_basis.uses_output_contract.output_contract.flipkart.settlement_cycle
  edge_type: USES_OUTPUT_CONTRACT
  source: execution_constraint_set.flipkart.date_basis
  target: output_contract.flipkart.settlement_cycle
  fields:
    edge_family: execution_guidance
    evidence_basis: deterministic constraint/output semantic mapping
    confidence: high
    canonical_cognee_edge: true
    marketplace_only: true
    canonical_edge_type: USES_OUTPUT_CONTRACT
    inverse_edge_type: USED_BY_CONSTRAINT_SET
    materialize_inverse: false
    edge_class: canonical
    source_type: execution_constraint_set
    target_type: output_contract
```

```yaml
candidate_edge:
  edge_id: edge.execution_constraint_set.flipkart.tax_boundary.uses_output_contract.output_contract.flipkart.settlement_summary
  edge_type: USES_OUTPUT_CONTRACT
  source: execution_constraint_set.flipkart.tax_boundary
  target: output_contract.flipkart.settlement_summary
  fields:
    edge_family: execution_guidance
    evidence_basis: deterministic constraint/output semantic mapping
    confidence: high
    canonical_cognee_edge: true
    marketplace_only: true
    canonical_edge_type: USES_OUTPUT_CONTRACT
    inverse_edge_type: USED_BY_CONSTRAINT_SET
    materialize_inverse: false
    edge_class: canonical
    source_type: execution_constraint_set
    target_type: output_contract
```

```yaml
candidate_edge:
  edge_id: edge.execution_constraint_set.flipkart.fulfilment_boundary.uses_output_contract.output_contract.flipkart.settlement_summary
  edge_type: USES_OUTPUT_CONTRACT
  source: execution_constraint_set.flipkart.fulfilment_boundary
  target: output_contract.flipkart.settlement_summary
  fields:
    edge_family: execution_guidance
    evidence_basis: deterministic constraint/output semantic mapping
    confidence: high
    canonical_cognee_edge: true
    marketplace_only: true
    canonical_edge_type: USES_OUTPUT_CONTRACT
    inverse_edge_type: USED_BY_CONSTRAINT_SET
    materialize_inverse: false
    edge_class: canonical
    source_type: execution_constraint_set
    target_type: output_contract
```

```yaml
candidate_edge:
  edge_id: edge.business_process.flipkart.forward_order_to_settlement.uses_metric.metric.gross_merchandise_value
  edge_type: USES_METRIC
  source: business_process.flipkart.forward_order_to_settlement
  target: metric.gross_merchandise_value
  fields:
    edge_family: process_understanding
    evidence_basis: deterministic process/metric semantic mapping
    confidence: high
    canonical_cognee_edge: true
    marketplace_only: true
    canonical_edge_type: USES_METRIC
    inverse_edge_type: USED_IN_PROCESS
    materialize_inverse: true
    edge_class: canonical
    source_type: business_process
    target_type: metric
```

```yaml
candidate_edge:
  edge_id: edge.metric.gross_merchandise_value.used_in_process.business_process.flipkart.forward_order_to_settlement
  edge_type: USED_IN_PROCESS
  source: metric.gross_merchandise_value
  target: business_process.flipkart.forward_order_to_settlement
  fields:
    edge_family: metric_understanding
    evidence_basis: deterministic process/metric semantic mapping
    confidence: high
    canonical_cognee_edge: true
    marketplace_only: true
    canonical_edge_type: USED_IN_PROCESS
    inverse_edge_type: USES_METRIC
    materialize_inverse: true
    edge_class: canonical
    source_type: metric
    target_type: business_process
```

```yaml
candidate_edge:
  edge_id: edge.business_process.flipkart.forward_order_to_settlement.uses_metric.metric.net_settlement
  edge_type: USES_METRIC
  source: business_process.flipkart.forward_order_to_settlement
  target: metric.net_settlement
  fields:
    edge_family: process_understanding
    evidence_basis: deterministic process/metric semantic mapping
    confidence: high
    canonical_cognee_edge: true
    marketplace_only: true
    canonical_edge_type: USES_METRIC
    inverse_edge_type: USED_IN_PROCESS
    materialize_inverse: true
    edge_class: canonical
    source_type: business_process
    target_type: metric
```

```yaml
candidate_edge:
  edge_id: edge.metric.net_settlement.used_in_process.business_process.flipkart.forward_order_to_settlement
  edge_type: USED_IN_PROCESS
  source: metric.net_settlement
  target: business_process.flipkart.forward_order_to_settlement
  fields:
    edge_family: metric_understanding
    evidence_basis: deterministic process/metric semantic mapping
    confidence: high
    canonical_cognee_edge: true
    marketplace_only: true
    canonical_edge_type: USED_IN_PROCESS
    inverse_edge_type: USES_METRIC
    materialize_inverse: true
    edge_class: canonical
    source_type: metric
    target_type: business_process
```

```yaml
candidate_edge:
  edge_id: edge.business_process.flipkart.forward_order_to_settlement.uses_metric.metric.realization_rate
  edge_type: USES_METRIC
  source: business_process.flipkart.forward_order_to_settlement
  target: metric.realization_rate
  fields:
    edge_family: process_understanding
    evidence_basis: deterministic process/metric semantic mapping
    confidence: high
    canonical_cognee_edge: true
    marketplace_only: true
    canonical_edge_type: USES_METRIC
    inverse_edge_type: USED_IN_PROCESS
    materialize_inverse: true
    edge_class: canonical
    source_type: business_process
    target_type: metric
```

```yaml
candidate_edge:
  edge_id: edge.metric.realization_rate.used_in_process.business_process.flipkart.forward_order_to_settlement
  edge_type: USED_IN_PROCESS
  source: metric.realization_rate
  target: business_process.flipkart.forward_order_to_settlement
  fields:
    edge_family: metric_understanding
    evidence_basis: deterministic process/metric semantic mapping
    confidence: high
    canonical_cognee_edge: true
    marketplace_only: true
    canonical_edge_type: USED_IN_PROCESS
    inverse_edge_type: USES_METRIC
    materialize_inverse: true
    edge_class: canonical
    source_type: metric
    target_type: business_process
```

```yaml
candidate_edge:
  edge_id: edge.business_process.flipkart.return_cancel_reversal.uses_metric.metric.return_rate
  edge_type: USES_METRIC
  source: business_process.flipkart.return_cancel_reversal
  target: metric.return_rate
  fields:
    edge_family: process_understanding
    evidence_basis: deterministic process/metric semantic mapping
    confidence: high
    canonical_cognee_edge: true
    marketplace_only: true
    canonical_edge_type: USES_METRIC
    inverse_edge_type: USED_IN_PROCESS
    materialize_inverse: true
    edge_class: canonical
    source_type: business_process
    target_type: metric
```

```yaml
candidate_edge:
  edge_id: edge.metric.return_rate.used_in_process.business_process.flipkart.return_cancel_reversal
  edge_type: USED_IN_PROCESS
  source: metric.return_rate
  target: business_process.flipkart.return_cancel_reversal
  fields:
    edge_family: metric_understanding
    evidence_basis: deterministic process/metric semantic mapping
    confidence: high
    canonical_cognee_edge: true
    marketplace_only: true
    canonical_edge_type: USED_IN_PROCESS
    inverse_edge_type: USES_METRIC
    materialize_inverse: true
    edge_class: canonical
    source_type: metric
    target_type: business_process
```

```yaml
candidate_edge:
  edge_id: edge.business_process.flipkart.return_cancel_reversal.uses_metric.metric.cancellation_rate
  edge_type: USES_METRIC
  source: business_process.flipkart.return_cancel_reversal
  target: metric.cancellation_rate
  fields:
    edge_family: process_understanding
    evidence_basis: deterministic process/metric semantic mapping
    confidence: high
    canonical_cognee_edge: true
    marketplace_only: true
    canonical_edge_type: USES_METRIC
    inverse_edge_type: USED_IN_PROCESS
    materialize_inverse: true
    edge_class: canonical
    source_type: business_process
    target_type: metric
```

```yaml
candidate_edge:
  edge_id: edge.metric.cancellation_rate.used_in_process.business_process.flipkart.return_cancel_reversal
  edge_type: USED_IN_PROCESS
  source: metric.cancellation_rate
  target: business_process.flipkart.return_cancel_reversal
  fields:
    edge_family: metric_understanding
    evidence_basis: deterministic process/metric semantic mapping
    confidence: high
    canonical_cognee_edge: true
    marketplace_only: true
    canonical_edge_type: USED_IN_PROCESS
    inverse_edge_type: USES_METRIC
    materialize_inverse: true
    edge_class: canonical
    source_type: metric
    target_type: business_process
```

```yaml
candidate_edge:
  edge_id: edge.business_process.flipkart.commission_fee_invoice.uses_metric.metric.marketplace_fee_total
  edge_type: USES_METRIC
  source: business_process.flipkart.commission_fee_invoice
  target: metric.marketplace_fee_total
  fields:
    edge_family: process_understanding
    evidence_basis: deterministic process/metric semantic mapping
    confidence: high
    canonical_cognee_edge: true
    marketplace_only: true
    canonical_edge_type: USES_METRIC
    inverse_edge_type: USED_IN_PROCESS
    materialize_inverse: true
    edge_class: canonical
    source_type: business_process
    target_type: metric
```

```yaml
candidate_edge:
  edge_id: edge.metric.marketplace_fee_total.used_in_process.business_process.flipkart.commission_fee_invoice
  edge_type: USED_IN_PROCESS
  source: metric.marketplace_fee_total
  target: business_process.flipkart.commission_fee_invoice
  fields:
    edge_family: metric_understanding
    evidence_basis: deterministic process/metric semantic mapping
    confidence: high
    canonical_cognee_edge: true
    marketplace_only: true
    canonical_edge_type: USED_IN_PROCESS
    inverse_edge_type: USES_METRIC
    materialize_inverse: true
    edge_class: canonical
    source_type: metric
    target_type: business_process
```

```yaml
candidate_edge:
  edge_id: edge.business_process.flipkart.commission_fee_invoice.uses_metric.metric.commission_fee
  edge_type: USES_METRIC
  source: business_process.flipkart.commission_fee_invoice
  target: metric.commission_fee
  fields:
    edge_family: process_understanding
    evidence_basis: deterministic process/metric semantic mapping
    confidence: high
    canonical_cognee_edge: true
    marketplace_only: true
    canonical_edge_type: USES_METRIC
    inverse_edge_type: USED_IN_PROCESS
    materialize_inverse: true
    edge_class: canonical
    source_type: business_process
    target_type: metric
```

```yaml
candidate_edge:
  edge_id: edge.metric.commission_fee.used_in_process.business_process.flipkart.commission_fee_invoice
  edge_type: USED_IN_PROCESS
  source: metric.commission_fee
  target: business_process.flipkart.commission_fee_invoice
  fields:
    edge_family: metric_understanding
    evidence_basis: deterministic process/metric semantic mapping
    confidence: high
    canonical_cognee_edge: true
    marketplace_only: true
    canonical_edge_type: USED_IN_PROCESS
    inverse_edge_type: USES_METRIC
    materialize_inverse: true
    edge_class: canonical
    source_type: metric
    target_type: business_process
```

```yaml
candidate_edge:
  edge_id: edge.business_process.flipkart.commission_fee_invoice.uses_metric.metric.effective_fee_rate
  edge_type: USES_METRIC
  source: business_process.flipkart.commission_fee_invoice
  target: metric.effective_fee_rate
  fields:
    edge_family: process_understanding
    evidence_basis: deterministic process/metric semantic mapping
    confidence: high
    canonical_cognee_edge: true
    marketplace_only: true
    canonical_edge_type: USES_METRIC
    inverse_edge_type: USED_IN_PROCESS
    materialize_inverse: true
    edge_class: canonical
    source_type: business_process
    target_type: metric
```

```yaml
candidate_edge:
  edge_id: edge.metric.effective_fee_rate.used_in_process.business_process.flipkart.commission_fee_invoice
  edge_type: USED_IN_PROCESS
  source: metric.effective_fee_rate
  target: business_process.flipkart.commission_fee_invoice
  fields:
    edge_family: metric_understanding
    evidence_basis: deterministic process/metric semantic mapping
    confidence: high
    canonical_cognee_edge: true
    marketplace_only: true
    canonical_edge_type: USED_IN_PROCESS
    inverse_edge_type: USES_METRIC
    materialize_inverse: true
    edge_class: canonical
    source_type: metric
    target_type: business_process
```

```yaml
candidate_edge:
  edge_id: edge.business_process.flipkart.cashback_credit_debit_note.uses_metric.metric.net_cashback
  edge_type: USES_METRIC
  source: business_process.flipkart.cashback_credit_debit_note
  target: metric.net_cashback
  fields:
    edge_family: process_understanding
    evidence_basis: deterministic process/metric semantic mapping
    confidence: high
    canonical_cognee_edge: true
    marketplace_only: true
    canonical_edge_type: USES_METRIC
    inverse_edge_type: USED_IN_PROCESS
    materialize_inverse: true
    edge_class: canonical
    source_type: business_process
    target_type: metric
```

```yaml
candidate_edge:
  edge_id: edge.metric.net_cashback.used_in_process.business_process.flipkart.cashback_credit_debit_note
  edge_type: USED_IN_PROCESS
  source: metric.net_cashback
  target: business_process.flipkart.cashback_credit_debit_note
  fields:
    edge_family: metric_understanding
    evidence_basis: deterministic process/metric semantic mapping
    confidence: high
    canonical_cognee_edge: true
    marketplace_only: true
    canonical_edge_type: USED_IN_PROCESS
    inverse_edge_type: USES_METRIC
    materialize_inverse: true
    edge_class: canonical
    source_type: metric
    target_type: business_process
```

```yaml
candidate_edge:
  edge_id: edge.business_process.flipkart.cashback_credit_debit_note.uses_metric.metric.cashback_rate
  edge_type: USES_METRIC
  source: business_process.flipkart.cashback_credit_debit_note
  target: metric.cashback_rate
  fields:
    edge_family: process_understanding
    evidence_basis: deterministic process/metric semantic mapping
    confidence: high
    canonical_cognee_edge: true
    marketplace_only: true
    canonical_edge_type: USES_METRIC
    inverse_edge_type: USED_IN_PROCESS
    materialize_inverse: true
    edge_class: canonical
    source_type: business_process
    target_type: metric
```

```yaml
candidate_edge:
  edge_id: edge.metric.cashback_rate.used_in_process.business_process.flipkart.cashback_credit_debit_note
  edge_type: USED_IN_PROCESS
  source: metric.cashback_rate
  target: business_process.flipkart.cashback_credit_debit_note
  fields:
    edge_family: metric_understanding
    evidence_basis: deterministic process/metric semantic mapping
    confidence: high
    canonical_cognee_edge: true
    marketplace_only: true
    canonical_edge_type: USED_IN_PROCESS
    inverse_edge_type: USES_METRIC
    materialize_inverse: true
    edge_class: canonical
    source_type: metric
    target_type: business_process
```





```yaml
candidate_edge:
  edge_id: edge.business_process.flipkart.marketplace_reconciliation_pipeline.uses_metric.metric.net_settlement
  edge_type: USES_METRIC
  source: business_process.flipkart.marketplace_reconciliation_pipeline
  target: metric.net_settlement
  fields:
    edge_family: process_understanding
    evidence_basis: deterministic process/metric semantic mapping
    confidence: high
    canonical_cognee_edge: true
    marketplace_only: true
    canonical_edge_type: USES_METRIC
    inverse_edge_type: USED_IN_PROCESS
    materialize_inverse: true
    edge_class: canonical
    source_type: business_process
    target_type: metric
```

```yaml
candidate_edge:
  edge_id: edge.metric.net_settlement.used_in_process.business_process.flipkart.marketplace_reconciliation_pipeline
  edge_type: USED_IN_PROCESS
  source: metric.net_settlement
  target: business_process.flipkart.marketplace_reconciliation_pipeline
  fields:
    edge_family: metric_understanding
    evidence_basis: deterministic process/metric semantic mapping
    confidence: high
    canonical_cognee_edge: true
    marketplace_only: true
    canonical_edge_type: USED_IN_PROCESS
    inverse_edge_type: USES_METRIC
    materialize_inverse: true
    edge_class: canonical
    source_type: metric
    target_type: business_process
```

```yaml
candidate_edge:
  edge_id: edge.business_process.flipkart.marketplace_reconciliation_pipeline.uses_metric.metric.marketplace_fee_total
  edge_type: USES_METRIC
  source: business_process.flipkart.marketplace_reconciliation_pipeline
  target: metric.marketplace_fee_total
  fields:
    edge_family: process_understanding
    evidence_basis: deterministic process/metric semantic mapping
    confidence: high
    canonical_cognee_edge: true
    marketplace_only: true
    canonical_edge_type: USES_METRIC
    inverse_edge_type: USED_IN_PROCESS
    materialize_inverse: true
    edge_class: canonical
    source_type: business_process
    target_type: metric
```

```yaml
candidate_edge:
  edge_id: edge.metric.marketplace_fee_total.used_in_process.business_process.flipkart.marketplace_reconciliation_pipeline
  edge_type: USED_IN_PROCESS
  source: metric.marketplace_fee_total
  target: business_process.flipkart.marketplace_reconciliation_pipeline
  fields:
    edge_family: metric_understanding
    evidence_basis: deterministic process/metric semantic mapping
    confidence: high
    canonical_cognee_edge: true
    marketplace_only: true
    canonical_edge_type: USED_IN_PROCESS
    inverse_edge_type: USES_METRIC
    materialize_inverse: true
    edge_class: canonical
    source_type: metric
    target_type: business_process
```

```yaml
candidate_edge:
  edge_id: edge.business_process.flipkart.marketplace_reconciliation_pipeline.uses_metric.metric.net_cashback
  edge_type: USES_METRIC
  source: business_process.flipkart.marketplace_reconciliation_pipeline
  target: metric.net_cashback
  fields:
    edge_family: process_understanding
    evidence_basis: deterministic process/metric semantic mapping
    confidence: high
    canonical_cognee_edge: true
    marketplace_only: true
    canonical_edge_type: USES_METRIC
    inverse_edge_type: USED_IN_PROCESS
    materialize_inverse: true
    edge_class: canonical
    source_type: business_process
    target_type: metric
```

```yaml
candidate_edge:
  edge_id: edge.metric.net_cashback.used_in_process.business_process.flipkart.marketplace_reconciliation_pipeline
  edge_type: USED_IN_PROCESS
  source: metric.net_cashback
  target: business_process.flipkart.marketplace_reconciliation_pipeline
  fields:
    edge_family: metric_understanding
    evidence_basis: deterministic process/metric semantic mapping
    confidence: high
    canonical_cognee_edge: true
    marketplace_only: true
    canonical_edge_type: USED_IN_PROCESS
    inverse_edge_type: USES_METRIC
    materialize_inverse: true
    edge_class: canonical
    source_type: metric
    target_type: business_process
```

```yaml
candidate_edge:
  edge_id: edge.value_profile.flipkart.group_level_id.applies_to_platform_context.platform_context.flipkart.in
  edge_type: APPLIES_TO_PLATFORM_CONTEXT
  source: value_profile.flipkart.group_level_id
  target: platform_context.flipkart.in
  fields:
    edge_family: applicability
    evidence_basis: fallback isolated-card context anchor
    confidence: medium
    canonical_cognee_edge: true
    marketplace_only: true
    note: Added only because no stronger explicit edge was available; preserves marketplace-only scope.
    canonical_edge_type: APPLIES_TO_PLATFORM_CONTEXT
    inverse_edge_type: HAS_APPLICABLE_CARD
    materialize_inverse: false
    edge_class: canonical
    source_type: value_profile
    target_type: platform_context
```

```yaml
candidate_edge:
  edge_id: edge.formula.flipkart.volumetric_weight.applies_to_platform_context.platform_context.flipkart.in
  edge_type: APPLIES_TO_PLATFORM_CONTEXT
  source: formula.flipkart.volumetric_weight
  target: platform_context.flipkart.in
  fields:
    edge_family: applicability
    evidence_basis: fallback isolated-card context anchor
    confidence: medium
    canonical_cognee_edge: true
    marketplace_only: true
    note: Added only because no stronger explicit edge was available; preserves marketplace-only scope.
    canonical_edge_type: APPLIES_TO_PLATFORM_CONTEXT
    inverse_edge_type: HAS_APPLICABLE_CARD
    materialize_inverse: false
    edge_class: canonical
    source_type: formula_template
    target_type: platform_context
```

```yaml
candidate_edge:
  edge_id: edge.formula.flipkart.settlement_waterfall.applies_to_platform_context.platform_context.flipkart.in
  edge_type: APPLIES_TO_PLATFORM_CONTEXT
  source: formula.flipkart.settlement_waterfall
  target: platform_context.flipkart.in
  fields:
    edge_family: applicability
    evidence_basis: fallback isolated-card context anchor
    confidence: medium
    canonical_cognee_edge: true
    marketplace_only: true
    note: Added only because no stronger explicit edge was available; preserves marketplace-only scope.
    canonical_edge_type: APPLIES_TO_PLATFORM_CONTEXT
    inverse_edge_type: HAS_APPLICABLE_CARD
    materialize_inverse: false
    edge_class: canonical
    source_type: formula_template
    target_type: platform_context
```

```yaml
candidate_edge:
  edge_id: edge.reconciliation_unit.flipkart.credit_debit_note_line.applies_to_platform_context.platform_context.flipkart.in
  edge_type: APPLIES_TO_PLATFORM_CONTEXT
  source: reconciliation_unit.flipkart.credit_debit_note_line
  target: platform_context.flipkart.in
  fields:
    edge_family: applicability
    evidence_basis: fallback isolated-card context anchor
    confidence: medium
    canonical_cognee_edge: true
    marketplace_only: true
    note: Added only because no stronger explicit edge was available; preserves marketplace-only scope.
    canonical_edge_type: APPLIES_TO_PLATFORM_CONTEXT
    inverse_edge_type: HAS_APPLICABLE_CARD
    materialize_inverse: false
    edge_class: canonical
    source_type: reconciliation_unit
    target_type: platform_context
```

```yaml
candidate_edge:
  edge_id: edge.reconciliation_unit.flipkart.fulfilment_bucket.applies_to_platform_context.platform_context.flipkart.in
  edge_type: APPLIES_TO_PLATFORM_CONTEXT
  source: reconciliation_unit.flipkart.fulfilment_bucket
  target: platform_context.flipkart.in
  fields:
    edge_family: applicability
    evidence_basis: fallback isolated-card context anchor
    confidence: medium
    canonical_cognee_edge: true
    marketplace_only: true
    note: Added only because no stronger explicit edge was available; preserves marketplace-only scope.
    canonical_edge_type: APPLIES_TO_PLATFORM_CONTEXT
    inverse_edge_type: HAS_APPLICABLE_CARD
    materialize_inverse: false
    edge_class: canonical
    source_type: reconciliation_unit
    target_type: platform_context
```

```yaml
candidate_edge:
  edge_id: edge.mismatch_category.flipkart.sale_amount_variance.applies_to_platform_context.platform_context.flipkart.in
  edge_type: APPLIES_TO_PLATFORM_CONTEXT
  source: mismatch_category.flipkart.sale_amount_variance
  target: platform_context.flipkart.in
  fields:
    edge_family: applicability
    evidence_basis: fallback isolated-card context anchor
    confidence: medium
    canonical_cognee_edge: true
    marketplace_only: true
    note: Added only because no stronger explicit edge was available; preserves marketplace-only scope.
    canonical_edge_type: APPLIES_TO_PLATFORM_CONTEXT
    inverse_edge_type: HAS_APPLICABLE_CARD
    materialize_inverse: false
    edge_class: canonical
    source_type: mismatch_category
    target_type: platform_context
```

```yaml
candidate_edge:
  edge_id: edge.mismatch_category.flipkart.mp_fee_variance.applies_to_platform_context.platform_context.flipkart.in
  edge_type: APPLIES_TO_PLATFORM_CONTEXT
  source: mismatch_category.flipkart.mp_fee_variance
  target: platform_context.flipkart.in
  fields:
    edge_family: applicability
    evidence_basis: fallback isolated-card context anchor
    confidence: medium
    canonical_cognee_edge: true
    marketplace_only: true
    note: Added only because no stronger explicit edge was available; preserves marketplace-only scope.
    canonical_edge_type: APPLIES_TO_PLATFORM_CONTEXT
    inverse_edge_type: HAS_APPLICABLE_CARD
    materialize_inverse: false
    edge_class: canonical
    source_type: mismatch_category
    target_type: platform_context
```

```yaml
candidate_edge:
  edge_id: edge.mismatch_category.flipkart.missing_fee_detail.applies_to_platform_context.platform_context.flipkart.in
  edge_type: APPLIES_TO_PLATFORM_CONTEXT
  source: mismatch_category.flipkart.missing_fee_detail
  target: platform_context.flipkart.in
  fields:
    edge_family: applicability
    evidence_basis: fallback isolated-card context anchor
    confidence: medium
    canonical_cognee_edge: true
    marketplace_only: true
    note: Added only because no stronger explicit edge was available; preserves marketplace-only scope.
    canonical_edge_type: APPLIES_TO_PLATFORM_CONTEXT
    inverse_edge_type: HAS_APPLICABLE_CARD
    materialize_inverse: false
    edge_class: canonical
    source_type: mismatch_category
    target_type: platform_context
```

```yaml
candidate_edge:
  edge_id: edge.mismatch_category.flipkart.cashback_offer_variance.applies_to_platform_context.platform_context.flipkart.in
  edge_type: APPLIES_TO_PLATFORM_CONTEXT
  source: mismatch_category.flipkart.cashback_offer_variance
  target: platform_context.flipkart.in
  fields:
    edge_family: applicability
    evidence_basis: fallback isolated-card context anchor
    confidence: medium
    canonical_cognee_edge: true
    marketplace_only: true
    note: Added only because no stronger explicit edge was available; preserves marketplace-only scope.
    canonical_edge_type: APPLIES_TO_PLATFORM_CONTEXT
    inverse_edge_type: HAS_APPLICABLE_CARD
    materialize_inverse: false
    edge_class: canonical
    source_type: mismatch_category
    target_type: platform_context
```

```yaml
candidate_edge:
  edge_id: edge.mismatch_category.flipkart.null_cashback_classification.applies_to_platform_context.platform_context.flipkart.in
  edge_type: APPLIES_TO_PLATFORM_CONTEXT
  source: mismatch_category.flipkart.null_cashback_classification
  target: platform_context.flipkart.in
  fields:
    edge_family: applicability
    evidence_basis: fallback isolated-card context anchor
    confidence: medium
    canonical_cognee_edge: true
    marketplace_only: true
    note: Added only because no stronger explicit edge was available; preserves marketplace-only scope.
    canonical_edge_type: APPLIES_TO_PLATFORM_CONTEXT
    inverse_edge_type: HAS_APPLICABLE_CARD
    materialize_inverse: false
    edge_class: canonical
    source_type: mismatch_category
    target_type: platform_context
```

```yaml
candidate_edge:
  edge_id: edge.mismatch_category.flipkart.settlement_waterfall_imbalance.applies_to_platform_context.platform_context.flipkart.in
  edge_type: APPLIES_TO_PLATFORM_CONTEXT
  source: mismatch_category.flipkart.settlement_waterfall_imbalance
  target: platform_context.flipkart.in
  fields:
    edge_family: applicability
    evidence_basis: fallback isolated-card context anchor
    confidence: medium
    canonical_cognee_edge: true
    marketplace_only: true
    note: Added only because no stronger explicit edge was available; preserves marketplace-only scope.
    canonical_edge_type: APPLIES_TO_PLATFORM_CONTEXT
    inverse_edge_type: HAS_APPLICABLE_CARD
    materialize_inverse: false
    edge_class: canonical
    source_type: mismatch_category
    target_type: platform_context
```

```yaml
candidate_edge:
  edge_id: edge.mismatch_category.flipkart.tax_deduction_variance.applies_to_platform_context.platform_context.flipkart.in
  edge_type: APPLIES_TO_PLATFORM_CONTEXT
  source: mismatch_category.flipkart.tax_deduction_variance
  target: platform_context.flipkart.in
  fields:
    edge_family: applicability
    evidence_basis: fallback isolated-card context anchor
    confidence: medium
    canonical_cognee_edge: true
    marketplace_only: true
    note: Added only because no stronger explicit edge was available; preserves marketplace-only scope.
    canonical_edge_type: APPLIES_TO_PLATFORM_CONTEXT
    inverse_edge_type: HAS_APPLICABLE_CARD
    materialize_inverse: false
    edge_class: canonical
    source_type: mismatch_category
    target_type: platform_context
```

```yaml
candidate_edge:
  edge_id: edge.mismatch_category.flipkart.order_id_normalization_failure.applies_to_platform_context.platform_context.flipkart.in
  edge_type: APPLIES_TO_PLATFORM_CONTEXT
  source: mismatch_category.flipkart.order_id_normalization_failure
  target: platform_context.flipkart.in
  fields:
    edge_family: applicability
    evidence_basis: fallback isolated-card context anchor
    confidence: medium
    canonical_cognee_edge: true
    marketplace_only: true
    note: Added only because no stronger explicit edge was available; preserves marketplace-only scope.
    canonical_edge_type: APPLIES_TO_PLATFORM_CONTEXT
    inverse_edge_type: HAS_APPLICABLE_CARD
    materialize_inverse: false
    edge_class: canonical
    source_type: mismatch_category
    target_type: platform_context
```

```yaml
candidate_edge:
  edge_id: edge.mismatch_category.flipkart.active_filter_omitted.applies_to_platform_context.platform_context.flipkart.in
  edge_type: APPLIES_TO_PLATFORM_CONTEXT
  source: mismatch_category.flipkart.active_filter_omitted
  target: platform_context.flipkart.in
  fields:
    edge_family: applicability
    evidence_basis: fallback isolated-card context anchor
    confidence: medium
    canonical_cognee_edge: true
    marketplace_only: true
    note: Added only because no stronger explicit edge was available; preserves marketplace-only scope.
    canonical_edge_type: APPLIES_TO_PLATFORM_CONTEXT
    inverse_edge_type: HAS_APPLICABLE_CARD
    materialize_inverse: false
    edge_class: canonical
    source_type: mismatch_category
    target_type: platform_context
```

```yaml
candidate_edge:
  edge_id: edge.rule.flipkart.string_fee_columns.applies_to_platform_context.platform_context.flipkart.in
  edge_type: APPLIES_TO_PLATFORM_CONTEXT
  source: rule.flipkart.string_fee_columns
  target: platform_context.flipkart.in
  fields:
    edge_family: applicability
    evidence_basis: fallback isolated-card context anchor
    confidence: medium
    canonical_cognee_edge: true
    marketplace_only: true
    note: Added only because no stronger explicit edge was available; preserves marketplace-only scope.
    canonical_edge_type: APPLIES_TO_PLATFORM_CONTEXT
    inverse_edge_type: HAS_APPLICABLE_CARD
    materialize_inverse: false
    edge_class: canonical
    source_type: rule
    target_type: platform_context
```

```yaml
candidate_edge:
  edge_id: edge.rule.flipkart.shopsy_string_flag.applies_to_platform_context.platform_context.flipkart.in
  edge_type: APPLIES_TO_PLATFORM_CONTEXT
  source: rule.flipkart.shopsy_string_flag
  target: platform_context.flipkart.in
  fields:
    edge_family: applicability
    evidence_basis: fallback isolated-card context anchor
    confidence: medium
    canonical_cognee_edge: true
    marketplace_only: true
    note: Added only because no stronger explicit edge was available; preserves marketplace-only scope.
    canonical_edge_type: APPLIES_TO_PLATFORM_CONTEXT
    inverse_edge_type: HAS_APPLICABLE_CARD
    materialize_inverse: false
    edge_class: canonical
    source_type: rule
    target_type: platform_context
```

```yaml
candidate_edge:
  edge_id: edge.rule.flipkart.oms_review.applies_to_platform_context.platform_context.flipkart.in
  edge_type: APPLIES_TO_PLATFORM_CONTEXT
  source: rule.flipkart.oms_review
  target: platform_context.flipkart.in
  fields:
    edge_family: applicability
    evidence_basis: fallback isolated-card context anchor
    confidence: medium
    canonical_cognee_edge: true
    marketplace_only: true
    note: Added only because no stronger explicit edge was available; preserves marketplace-only scope.
    canonical_edge_type: APPLIES_TO_PLATFORM_CONTEXT
    inverse_edge_type: HAS_APPLICABLE_CARD
    materialize_inverse: false
    edge_class: canonical
    source_type: rule
    target_type: platform_context
```

```yaml
candidate_edge:
  edge_id: edge.value_profile.flipkart.commission.description.profiles_table.table.flipkart.commission
  edge_type: PROFILES_TABLE
  source: value_profile.flipkart.commission.description
  target: table.flipkart.commission
  fields:
    edge_family: data_understanding
    evidence_basis: materialized inverse of edge.table.flipkart.commission.has_value_profile.value_profile.flipkart.commission.description
    confidence: high
    canonical_cognee_edge: true
    marketplace_only: true
    canonical_edge_type: PROFILES_TABLE
    inverse_edge_type: HAS_VALUE_PROFILE
    materialize_inverse: false
    materialized_inverse: true
    inverse_of_edge_id: edge.table.flipkart.commission.has_value_profile.value_profile.flipkart.commission.description
    edge_class: canonical
    source_type: value_profile
    target_type: table
```

```yaml
candidate_edge:
  edge_id: edge.value_profile.flipkart.cashback.transaction_type.profiles_table.table.flipkart.cashback
  edge_type: PROFILES_TABLE
  source: value_profile.flipkart.cashback.transaction_type
  target: table.flipkart.cashback
  fields:
    edge_family: data_understanding
    evidence_basis: materialized inverse of edge.table.flipkart.cashback.has_value_profile.value_profile.flipkart.cashback.transaction_type
    confidence: high
    canonical_cognee_edge: true
    marketplace_only: true
    canonical_edge_type: PROFILES_TABLE
    inverse_edge_type: HAS_VALUE_PROFILE
    materialize_inverse: false
    materialized_inverse: true
    inverse_of_edge_id: edge.table.flipkart.cashback.has_value_profile.value_profile.flipkart.cashback.transaction_type
    edge_class: canonical
    source_type: value_profile
    target_type: table
```

```yaml
candidate_edge:
  edge_id: edge.value_profile.flipkart.cashback.document_type.profiles_table.table.flipkart.cashback
  edge_type: PROFILES_TABLE
  source: value_profile.flipkart.cashback.document_type
  target: table.flipkart.cashback
  fields:
    edge_family: data_understanding
    evidence_basis: materialized inverse of edge.table.flipkart.cashback.has_value_profile.value_profile.flipkart.cashback.document_type
    confidence: high
    canonical_cognee_edge: true
    marketplace_only: true
    canonical_edge_type: PROFILES_TABLE
    inverse_edge_type: HAS_VALUE_PROFILE
    materialize_inverse: false
    materialized_inverse: true
    inverse_of_edge_id: edge.table.flipkart.cashback.has_value_profile.value_profile.flipkart.cashback.document_type
    edge_class: canonical
    source_type: value_profile
    target_type: table
```

```yaml
candidate_edge:
  edge_id: edge.value_profile.flipkart.cashback.document_sub_type.profiles_table.table.flipkart.cashback
  edge_type: PROFILES_TABLE
  source: value_profile.flipkart.cashback.document_sub_type
  target: table.flipkart.cashback
  fields:
    edge_family: data_understanding
    evidence_basis: materialized inverse of edge.table.flipkart.cashback.has_value_profile.value_profile.flipkart.cashback.document_sub_type
    confidence: high
    canonical_cognee_edge: true
    marketplace_only: true
    canonical_edge_type: PROFILES_TABLE
    inverse_edge_type: HAS_VALUE_PROFILE
    materialize_inverse: false
    materialized_inverse: true
    inverse_of_edge_id: edge.table.flipkart.cashback.has_value_profile.value_profile.flipkart.cashback.document_sub_type
    edge_class: canonical
    source_type: value_profile
    target_type: table
```

```yaml
candidate_edge:
  edge_id: edge.value_profile.flipkart.cashback.is_shopsy_order.profiles_table.table.flipkart.cashback
  edge_type: PROFILES_TABLE
  source: value_profile.flipkart.cashback.is_shopsy_order
  target: table.flipkart.cashback
  fields:
    edge_family: data_understanding
    evidence_basis: materialized inverse of edge.table.flipkart.cashback.has_value_profile.value_profile.flipkart.cashback.is_shopsy_order
    confidence: high
    canonical_cognee_edge: true
    marketplace_only: true
    canonical_edge_type: PROFILES_TABLE
    inverse_edge_type: HAS_VALUE_PROFILE
    materialize_inverse: false
    materialized_inverse: true
    inverse_of_edge_id: edge.table.flipkart.cashback.has_value_profile.value_profile.flipkart.cashback.is_shopsy_order
    edge_class: canonical
    source_type: value_profile
    target_type: table
```

```yaml
candidate_edge:
  edge_id: edge.value_profile.flipkart.oms.fulfilment_type.profiles_table.table.flipkart.oms
  edge_type: PROFILES_TABLE
  source: value_profile.flipkart.oms.fulfilment_type
  target: table.flipkart.oms
  fields:
    edge_family: data_understanding
    evidence_basis: materialized inverse of edge.table.flipkart.oms.has_value_profile.value_profile.flipkart.oms.fulfilment_type
    confidence: high
    canonical_cognee_edge: true
    marketplace_only: true
    canonical_edge_type: PROFILES_TABLE
    inverse_edge_type: HAS_VALUE_PROFILE
    materialize_inverse: false
    materialized_inverse: true
    inverse_of_edge_id: edge.table.flipkart.oms.has_value_profile.value_profile.flipkart.oms.fulfilment_type
    edge_class: canonical
    source_type: value_profile
    target_type: table
```

```yaml
candidate_edge:
  edge_id: edge.value_profile.flipkart.settlement.fulfilment_type.profiles_table.table.flipkart.settlement
  edge_type: PROFILES_TABLE
  source: value_profile.flipkart.settlement.fulfilment_type
  target: table.flipkart.settlement
  fields:
    edge_family: data_understanding
    evidence_basis: materialized inverse of edge.table.flipkart.settlement.has_value_profile.value_profile.flipkart.settlement.fulfilment_type
    confidence: high
    canonical_cognee_edge: true
    marketplace_only: true
    canonical_edge_type: PROFILES_TABLE
    inverse_edge_type: HAS_VALUE_PROFILE
    materialize_inverse: false
    materialized_inverse: true
    inverse_of_edge_id: edge.table.flipkart.settlement.has_value_profile.value_profile.flipkart.settlement.fulfilment_type
    edge_class: canonical
    source_type: value_profile
    target_type: table
```

```yaml
candidate_edge:
  edge_id: edge.value_profile.flipkart.settlement.neft_type.profiles_table.table.flipkart.settlement
  edge_type: PROFILES_TABLE
  source: value_profile.flipkart.settlement.neft_type
  target: table.flipkart.settlement
  fields:
    edge_family: data_understanding
    evidence_basis: materialized inverse of edge.table.flipkart.settlement.has_value_profile.value_profile.flipkart.settlement.neft_type
    confidence: high
    canonical_cognee_edge: true
    marketplace_only: true
    canonical_edge_type: PROFILES_TABLE
    inverse_edge_type: HAS_VALUE_PROFILE
    materialize_inverse: false
    materialized_inverse: true
    inverse_of_edge_id: edge.table.flipkart.settlement.has_value_profile.value_profile.flipkart.settlement.neft_type
    edge_class: canonical
    source_type: value_profile
    target_type: table
```

```yaml
candidate_edge:
  edge_id: edge.value_profile.flipkart.settlement.return_type.profiles_table.table.flipkart.settlement
  edge_type: PROFILES_TABLE
  source: value_profile.flipkart.settlement.return_type
  target: table.flipkart.settlement
  fields:
    edge_family: data_understanding
    evidence_basis: materialized inverse of edge.table.flipkart.settlement.has_value_profile.value_profile.flipkart.settlement.return_type
    confidence: high
    canonical_cognee_edge: true
    marketplace_only: true
    canonical_edge_type: PROFILES_TABLE
    inverse_edge_type: HAS_VALUE_PROFILE
    materialize_inverse: false
    materialized_inverse: true
    inverse_of_edge_id: edge.table.flipkart.settlement.has_value_profile.value_profile.flipkart.settlement.return_type
    edge_class: canonical
    source_type: value_profile
    target_type: table
```

```yaml
candidate_edge:
  edge_id: edge.value_profile.flipkart.settlement.is_active.profiles_table.table.flipkart.settlement
  edge_type: PROFILES_TABLE
  source: value_profile.flipkart.settlement.is_active
  target: table.flipkart.settlement
  fields:
    edge_family: data_understanding
    evidence_basis: materialized inverse of edge.table.flipkart.settlement.has_value_profile.value_profile.flipkart.settlement.is_active
    confidence: high
    canonical_cognee_edge: true
    marketplace_only: true
    canonical_edge_type: PROFILES_TABLE
    inverse_edge_type: HAS_VALUE_PROFILE
    materialize_inverse: false
    materialized_inverse: true
    inverse_of_edge_id: edge.table.flipkart.settlement.has_value_profile.value_profile.flipkart.settlement.is_active
    edge_class: canonical
    source_type: value_profile
    target_type: table
```

```yaml
candidate_edge:
  edge_id: edge.reconciliation_side.flipkart.oms_expected.belongs_to_reconciliation_profile.reconciliation_profile.flipkart.oms_settlement
  edge_type: BELONGS_TO_RECONCILIATION_PROFILE
  source: reconciliation_side.flipkart.oms_expected
  target: reconciliation_profile.flipkart.oms_settlement
  fields:
    edge_family: reconciliation_understanding
    evidence_basis: materialized inverse of edge.reconciliation_profile.flipkart.oms_settlement.has_reconciliation_side.reconciliation_side.flipkart.oms_expected
    confidence: high
    canonical_cognee_edge: true
    marketplace_only: true
    canonical_edge_type: BELONGS_TO_RECONCILIATION_PROFILE
    inverse_edge_type: HAS_RECONCILIATION_SIDE
    materialize_inverse: false
    materialized_inverse: true
    inverse_of_edge_id: edge.reconciliation_profile.flipkart.oms_settlement.has_reconciliation_side.reconciliation_side.flipkart.oms_expected
    edge_class: canonical
    source_type: reconciliation_side
    target_type: reconciliation_profile
    edge_properties:
      side_role: expected
    side_role: expected
```

```yaml
candidate_edge:
  edge_id: edge.reconciliation_side.flipkart.settlement_actual.belongs_to_reconciliation_profile.reconciliation_profile.flipkart.oms_settlement
  edge_type: BELONGS_TO_RECONCILIATION_PROFILE
  source: reconciliation_side.flipkart.settlement_actual
  target: reconciliation_profile.flipkart.oms_settlement
  fields:
    edge_family: reconciliation_understanding
    evidence_basis: materialized inverse of edge.reconciliation_profile.flipkart.oms_settlement.has_reconciliation_side.reconciliation_side.flipkart.settlement_actual
    confidence: high
    canonical_cognee_edge: true
    marketplace_only: true
    canonical_edge_type: BELONGS_TO_RECONCILIATION_PROFILE
    inverse_edge_type: HAS_RECONCILIATION_SIDE
    materialize_inverse: false
    materialized_inverse: true
    inverse_of_edge_id: edge.reconciliation_profile.flipkart.oms_settlement.has_reconciliation_side.reconciliation_side.flipkart.settlement_actual
    edge_class: canonical
    source_type: reconciliation_side
    target_type: reconciliation_profile
    edge_properties:
      side_role: actual
    side_role: actual
```

```yaml
candidate_edge:
  edge_id: edge.reconciliation_side.flipkart.settlement_fee_actual.belongs_to_reconciliation_profile.reconciliation_profile.flipkart.settlement_commission
  edge_type: BELONGS_TO_RECONCILIATION_PROFILE
  source: reconciliation_side.flipkart.settlement_fee_actual
  target: reconciliation_profile.flipkart.settlement_commission
  fields:
    edge_family: reconciliation_understanding
    evidence_basis: materialized inverse of edge.reconciliation_profile.flipkart.settlement_commission.has_reconciliation_side.reconciliation_side.flipkart.settlement_fee_actual
    confidence: high
    canonical_cognee_edge: true
    marketplace_only: true
    canonical_edge_type: BELONGS_TO_RECONCILIATION_PROFILE
    inverse_edge_type: HAS_RECONCILIATION_SIDE
    materialize_inverse: false
    materialized_inverse: true
    inverse_of_edge_id: edge.reconciliation_profile.flipkart.settlement_commission.has_reconciliation_side.reconciliation_side.flipkart.settlement_fee_actual
    edge_class: canonical
    source_type: reconciliation_side
    target_type: reconciliation_profile
    edge_properties:
      side_role: expected
    side_role: expected
```

```yaml
candidate_edge:
  edge_id: edge.reconciliation_side.flipkart.commission_detail_expected.belongs_to_reconciliation_profile.reconciliation_profile.flipkart.settlement_commission
  edge_type: BELONGS_TO_RECONCILIATION_PROFILE
  source: reconciliation_side.flipkart.commission_detail_expected
  target: reconciliation_profile.flipkart.settlement_commission
  fields:
    edge_family: reconciliation_understanding
    evidence_basis: materialized inverse of edge.reconciliation_profile.flipkart.settlement_commission.has_reconciliation_side.reconciliation_side.flipkart.commission_detail_expected
    confidence: high
    canonical_cognee_edge: true
    marketplace_only: true
    canonical_edge_type: BELONGS_TO_RECONCILIATION_PROFILE
    inverse_edge_type: HAS_RECONCILIATION_SIDE
    materialize_inverse: false
    materialized_inverse: true
    inverse_of_edge_id: edge.reconciliation_profile.flipkart.settlement_commission.has_reconciliation_side.reconciliation_side.flipkart.commission_detail_expected
    edge_class: canonical
    source_type: reconciliation_side
    target_type: reconciliation_profile
    edge_properties:
      side_role: actual
    side_role: actual
```

```yaml
candidate_edge:
  edge_id: edge.reconciliation_side.flipkart.cashback_expected.belongs_to_reconciliation_profile.reconciliation_profile.flipkart.cashback_settlement_offer
  edge_type: BELONGS_TO_RECONCILIATION_PROFILE
  source: reconciliation_side.flipkart.cashback_expected
  target: reconciliation_profile.flipkart.cashback_settlement_offer
  fields:
    edge_family: reconciliation_understanding
    evidence_basis: materialized inverse of edge.reconciliation_profile.flipkart.cashback_settlement_offer.has_reconciliation_side.reconciliation_side.flipkart.cashback_expected
    confidence: high
    canonical_cognee_edge: true
    marketplace_only: true
    canonical_edge_type: BELONGS_TO_RECONCILIATION_PROFILE
    inverse_edge_type: HAS_RECONCILIATION_SIDE
    materialize_inverse: false
    materialized_inverse: true
    inverse_of_edge_id: edge.reconciliation_profile.flipkart.cashback_settlement_offer.has_reconciliation_side.reconciliation_side.flipkart.cashback_expected
    edge_class: canonical
    source_type: reconciliation_side
    target_type: reconciliation_profile
    edge_properties:
      side_role: expected
    side_role: expected
```

```yaml
candidate_edge:
  edge_id: edge.reconciliation_side.flipkart.settlement_offer_actual.belongs_to_reconciliation_profile.reconciliation_profile.flipkart.cashback_settlement_offer
  edge_type: BELONGS_TO_RECONCILIATION_PROFILE
  source: reconciliation_side.flipkart.settlement_offer_actual
  target: reconciliation_profile.flipkart.cashback_settlement_offer
  fields:
    edge_family: reconciliation_understanding
    evidence_basis: materialized inverse of edge.reconciliation_profile.flipkart.cashback_settlement_offer.has_reconciliation_side.reconciliation_side.flipkart.settlement_offer_actual
    confidence: high
    canonical_cognee_edge: true
    marketplace_only: true
    canonical_edge_type: BELONGS_TO_RECONCILIATION_PROFILE
    inverse_edge_type: HAS_RECONCILIATION_SIDE
    materialize_inverse: false
    materialized_inverse: true
    inverse_of_edge_id: edge.reconciliation_profile.flipkart.cashback_settlement_offer.has_reconciliation_side.reconciliation_side.flipkart.settlement_offer_actual
    edge_class: canonical
    source_type: reconciliation_side
    target_type: reconciliation_profile
    edge_properties:
      side_role: actual
    side_role: actual
```

```yaml
candidate_edge:
  edge_id: edge.reconciliation_side.flipkart.settlement_components.belongs_to_reconciliation_profile.reconciliation_profile.flipkart.settlement_waterfall
  edge_type: BELONGS_TO_RECONCILIATION_PROFILE
  source: reconciliation_side.flipkart.settlement_components
  target: reconciliation_profile.flipkart.settlement_waterfall
  fields:
    edge_family: reconciliation_understanding
    evidence_basis: materialized inverse of edge.reconciliation_profile.flipkart.settlement_waterfall.has_reconciliation_side.reconciliation_side.flipkart.settlement_components
    confidence: high
    canonical_cognee_edge: true
    marketplace_only: true
    canonical_edge_type: BELONGS_TO_RECONCILIATION_PROFILE
    inverse_edge_type: HAS_RECONCILIATION_SIDE
    materialize_inverse: false
    materialized_inverse: true
    inverse_of_edge_id: edge.reconciliation_profile.flipkart.settlement_waterfall.has_reconciliation_side.reconciliation_side.flipkart.settlement_components
    edge_class: canonical
    source_type: reconciliation_side
    target_type: reconciliation_profile
    edge_properties:
      side_role: expected
    side_role: expected
```

```yaml
candidate_edge:
  edge_id: edge.reconciliation_side.flipkart.settlement_net.belongs_to_reconciliation_profile.reconciliation_profile.flipkart.settlement_waterfall
  edge_type: BELONGS_TO_RECONCILIATION_PROFILE
  source: reconciliation_side.flipkart.settlement_net
  target: reconciliation_profile.flipkart.settlement_waterfall
  fields:
    edge_family: reconciliation_understanding
    evidence_basis: materialized inverse of edge.reconciliation_profile.flipkart.settlement_waterfall.has_reconciliation_side.reconciliation_side.flipkart.settlement_net
    confidence: high
    canonical_cognee_edge: true
    marketplace_only: true
    canonical_edge_type: BELONGS_TO_RECONCILIATION_PROFILE
    inverse_edge_type: HAS_RECONCILIATION_SIDE
    materialize_inverse: false
    materialized_inverse: true
    inverse_of_edge_id: edge.reconciliation_profile.flipkart.settlement_waterfall.has_reconciliation_side.reconciliation_side.flipkart.settlement_net
    edge_class: canonical
    source_type: reconciliation_side
    target_type: reconciliation_profile
    edge_properties:
      side_role: actual
    side_role: actual
```

```yaml
candidate_edge:
  edge_id: edge.reconciliation_side.flipkart.order_fee_cashback_expected.belongs_to_reconciliation_profile.reconciliation_profile.flipkart.cross_table_pipeline
  edge_type: BELONGS_TO_RECONCILIATION_PROFILE
  source: reconciliation_side.flipkart.order_fee_cashback_expected
  target: reconciliation_profile.flipkart.cross_table_pipeline
  fields:
    edge_family: reconciliation_understanding
    evidence_basis: materialized inverse of edge.reconciliation_profile.flipkart.cross_table_pipeline.has_reconciliation_side.reconciliation_side.flipkart.order_fee_cashback_expected
    confidence: high
    canonical_cognee_edge: true
    marketplace_only: true
    canonical_edge_type: BELONGS_TO_RECONCILIATION_PROFILE
    inverse_edge_type: HAS_RECONCILIATION_SIDE
    materialize_inverse: false
    materialized_inverse: true
    inverse_of_edge_id: edge.reconciliation_profile.flipkart.cross_table_pipeline.has_reconciliation_side.reconciliation_side.flipkart.order_fee_cashback_expected
    edge_class: canonical
    source_type: reconciliation_side
    target_type: reconciliation_profile
    edge_properties:
      side_role: expected
    side_role: expected
```

```yaml
candidate_edge:
  edge_id: edge.reconciliation_side.flipkart.settlement_actual.belongs_to_reconciliation_profile.reconciliation_profile.flipkart.cross_table_pipeline
  edge_type: BELONGS_TO_RECONCILIATION_PROFILE
  source: reconciliation_side.flipkart.settlement_actual
  target: reconciliation_profile.flipkart.cross_table_pipeline
  fields:
    edge_family: reconciliation_understanding
    evidence_basis: materialized inverse of edge.reconciliation_profile.flipkart.cross_table_pipeline.has_reconciliation_side.reconciliation_side.flipkart.settlement_actual
    confidence: high
    canonical_cognee_edge: true
    marketplace_only: true
    canonical_edge_type: BELONGS_TO_RECONCILIATION_PROFILE
    inverse_edge_type: HAS_RECONCILIATION_SIDE
    materialize_inverse: false
    materialized_inverse: true
    inverse_of_edge_id: edge.reconciliation_profile.flipkart.cross_table_pipeline.has_reconciliation_side.reconciliation_side.flipkart.settlement_actual
    edge_class: canonical
    source_type: reconciliation_side
    target_type: reconciliation_profile
    edge_properties:
      side_role: actual
    side_role: actual
```

```yaml
candidate_edge:
  edge_id: edge.reconciliation_side.flipkart.settlement_pipeline_actual.belongs_to_reconciliation_profile.reconciliation_profile.flipkart.cross_table_pipeline
  edge_type: BELONGS_TO_RECONCILIATION_PROFILE
  source: reconciliation_side.flipkart.settlement_pipeline_actual
  target: reconciliation_profile.flipkart.cross_table_pipeline
  fields:
    edge_family: reconciliation_understanding
    evidence_basis: materialized inverse of edge.reconciliation_profile.flipkart.cross_table_pipeline.has_reconciliation_side.reconciliation_side.flipkart.settlement_pipeline_actual
    confidence: high
    canonical_cognee_edge: true
    marketplace_only: true
    canonical_edge_type: BELONGS_TO_RECONCILIATION_PROFILE
    inverse_edge_type: HAS_RECONCILIATION_SIDE
    materialize_inverse: false
    materialized_inverse: true
    inverse_of_edge_id: edge.reconciliation_profile.flipkart.cross_table_pipeline.has_reconciliation_side.reconciliation_side.flipkart.settlement_pipeline_actual
    edge_class: canonical
    source_type: reconciliation_side
    target_type: reconciliation_profile
```

```yaml
candidate_edge:
  edge_id: edge.table.flipkart.settlement.has_column.column.settlement.my_share_settled_amount
  edge_type: HAS_COLUMN
  source: table.flipkart.settlement
  target: column.settlement.my_share_settled_amount
  fields:
    edge_family: data_understanding
    evidence_basis: column.fields.table_id
    confidence: high
    canonical_cognee_edge: true
    marketplace_only: true
    canonical_edge_type: HAS_COLUMN
    inverse_edge_type: BELONGS_TO_TABLE
    materialize_inverse: true
    edge_class: canonical
    source_type: table
    target_type: column
```

```yaml
candidate_edge:
  edge_id: edge.column.settlement.my_share_settled_amount.belongs_to_table.table.flipkart.settlement
  edge_type: BELONGS_TO_TABLE
  source: column.settlement.my_share_settled_amount
  target: table.flipkart.settlement
  fields:
    edge_family: data_understanding
    evidence_basis: column.fields.table_id
    confidence: high
    canonical_cognee_edge: true
    marketplace_only: true
    canonical_edge_type: BELONGS_TO_TABLE
    inverse_edge_type: HAS_COLUMN
    materialize_inverse: true
    edge_class: canonical
    source_type: column
    target_type: table
    legacy_edge_aliases:
    - column_belongs_to_table
```

```yaml
candidate_edge:
  edge_id: edge.table.flipkart.settlement.has_column.column.settlement.addon_settled_amount
  edge_type: HAS_COLUMN
  source: table.flipkart.settlement
  target: column.settlement.addon_settled_amount
  fields:
    edge_family: data_understanding
    evidence_basis: column.fields.table_id
    confidence: high
    canonical_cognee_edge: true
    marketplace_only: true
    canonical_edge_type: HAS_COLUMN
    inverse_edge_type: BELONGS_TO_TABLE
    materialize_inverse: true
    edge_class: canonical
    source_type: table
    target_type: column
```

```yaml
candidate_edge:
  edge_id: edge.column.settlement.addon_settled_amount.belongs_to_table.table.flipkart.settlement
  edge_type: BELONGS_TO_TABLE
  source: column.settlement.addon_settled_amount
  target: table.flipkart.settlement
  fields:
    edge_family: data_understanding
    evidence_basis: column.fields.table_id
    confidence: high
    canonical_cognee_edge: true
    marketplace_only: true
    canonical_edge_type: BELONGS_TO_TABLE
    inverse_edge_type: HAS_COLUMN
    materialize_inverse: true
    edge_class: canonical
    source_type: column
    target_type: table
    legacy_edge_aliases:
    - column_belongs_to_table
```

```yaml
candidate_edge:
  edge_id: edge.table.flipkart.settlement.has_column.column.settlement.taxes_settled_amount
  edge_type: HAS_COLUMN
  source: table.flipkart.settlement
  target: column.settlement.taxes_settled_amount
  fields:
    edge_family: data_understanding
    evidence_basis: column.fields.table_id
    confidence: high
    canonical_cognee_edge: true
    marketplace_only: true
    canonical_edge_type: HAS_COLUMN
    inverse_edge_type: BELONGS_TO_TABLE
    materialize_inverse: true
    edge_class: canonical
    source_type: table
    target_type: column
```

```yaml
candidate_edge:
  edge_id: edge.column.settlement.taxes_settled_amount.belongs_to_table.table.flipkart.settlement
  edge_type: BELONGS_TO_TABLE
  source: column.settlement.taxes_settled_amount
  target: table.flipkart.settlement
  fields:
    edge_family: data_understanding
    evidence_basis: column.fields.table_id
    confidence: high
    canonical_cognee_edge: true
    marketplace_only: true
    canonical_edge_type: BELONGS_TO_TABLE
    inverse_edge_type: HAS_COLUMN
    materialize_inverse: true
    edge_class: canonical
    source_type: column
    target_type: table
    legacy_edge_aliases:
    - column_belongs_to_table
```

```yaml
candidate_edge:
  edge_id: edge.table.flipkart.settlement.has_column.column.settlement.total_tax
  edge_type: HAS_COLUMN
  source: table.flipkart.settlement
  target: column.settlement.total_tax
  fields:
    edge_family: data_understanding
    evidence_basis: column.fields.table_id
    confidence: high
    canonical_cognee_edge: true
    marketplace_only: true
    canonical_edge_type: HAS_COLUMN
    inverse_edge_type: BELONGS_TO_TABLE
    materialize_inverse: true
    edge_class: canonical
    source_type: table
    target_type: column
```

```yaml
candidate_edge:
  edge_id: edge.column.settlement.total_tax.belongs_to_table.table.flipkart.settlement
  edge_type: BELONGS_TO_TABLE
  source: column.settlement.total_tax
  target: table.flipkart.settlement
  fields:
    edge_family: data_understanding
    evidence_basis: column.fields.table_id
    confidence: high
    canonical_cognee_edge: true
    marketplace_only: true
    canonical_edge_type: BELONGS_TO_TABLE
    inverse_edge_type: HAS_COLUMN
    materialize_inverse: true
    edge_class: canonical
    source_type: column
    target_type: table
    legacy_edge_aliases:
    - column_belongs_to_table
```

```yaml
candidate_edge:
  edge_id: edge.table.flipkart.commission.has_column.column.commission.metadata
  edge_type: HAS_COLUMN
  source: table.flipkart.commission
  target: column.commission.metadata
  fields:
    edge_family: data_understanding
    evidence_basis: column.fields.table_id
    confidence: high
    canonical_cognee_edge: true
    marketplace_only: true
    canonical_edge_type: HAS_COLUMN
    inverse_edge_type: BELONGS_TO_TABLE
    materialize_inverse: true
    edge_class: canonical
    source_type: table
    target_type: column
```

```yaml
candidate_edge:
  edge_id: edge.column.commission.metadata.belongs_to_table.table.flipkart.commission
  edge_type: BELONGS_TO_TABLE
  source: column.commission.metadata
  target: table.flipkart.commission
  fields:
    edge_family: data_understanding
    evidence_basis: column.fields.table_id
    confidence: high
    canonical_cognee_edge: true
    marketplace_only: true
    canonical_edge_type: BELONGS_TO_TABLE
    inverse_edge_type: HAS_COLUMN
    materialize_inverse: true
    edge_class: canonical
    source_type: column
    target_type: table
    legacy_edge_aliases:
    - column_belongs_to_table
```

```yaml
candidate_edge:
  edge_id: edge.table.flipkart.commission.has_column.column.commission.transaction_type
  edge_type: HAS_COLUMN
  source: table.flipkart.commission
  target: column.commission.transaction_type
  fields:
    edge_family: data_understanding
    evidence_basis: column.fields.table_id
    confidence: high
    canonical_cognee_edge: true
    marketplace_only: true
    canonical_edge_type: HAS_COLUMN
    inverse_edge_type: BELONGS_TO_TABLE
    materialize_inverse: true
    edge_class: canonical
    source_type: table
    target_type: column
```

```yaml
candidate_edge:
  edge_id: edge.column.commission.transaction_type.belongs_to_table.table.flipkart.commission
  edge_type: BELONGS_TO_TABLE
  source: column.commission.transaction_type
  target: table.flipkart.commission
  fields:
    edge_family: data_understanding
    evidence_basis: column.fields.table_id
    confidence: high
    canonical_cognee_edge: true
    marketplace_only: true
    canonical_edge_type: BELONGS_TO_TABLE
    inverse_edge_type: HAS_COLUMN
    materialize_inverse: true
    edge_class: canonical
    source_type: column
    target_type: table
    legacy_edge_aliases:
    - column_belongs_to_table
```

```yaml
candidate_edge:
  edge_id: edge.business_process.flipkart.marketplace_reconciliation_pipeline.has_workflow_step.workflow_step.flipkart.recon_fee_validation
  edge_type: HAS_WORKFLOW_STEP
  source: business_process.flipkart.marketplace_reconciliation_pipeline
  target: workflow_step.flipkart.recon_fee_validation
  fields:
    edge_family: process_understanding
    evidence_basis: workflow_step.fields.process_id
    confidence: high
    canonical_cognee_edge: true
    marketplace_only: true
    canonical_edge_type: HAS_WORKFLOW_STEP
    inverse_edge_type: BELONGS_TO_PROCESS
    materialize_inverse: true
    edge_class: canonical
    source_type: business_process
    target_type: workflow_step
```

```yaml
candidate_edge:
  edge_id: edge.workflow_step.flipkart.recon_fee_validation.belongs_to_process.business_process.flipkart.marketplace_reconciliation_pipeline
  edge_type: BELONGS_TO_PROCESS
  source: workflow_step.flipkart.recon_fee_validation
  target: business_process.flipkart.marketplace_reconciliation_pipeline
  fields:
    edge_family: process_understanding
    evidence_basis: workflow_step.fields.process_id
    confidence: high
    canonical_cognee_edge: true
    marketplace_only: true
    canonical_edge_type: BELONGS_TO_PROCESS
    inverse_edge_type: HAS_WORKFLOW_STEP
    materialize_inverse: true
    edge_class: canonical
    source_type: workflow_step
    target_type: business_process
    legacy_edge_aliases:
    - step_in_process
```

```yaml
candidate_edge:
  edge_id: edge.business_process.flipkart.marketplace_reconciliation_pipeline.has_workflow_step.workflow_step.flipkart.recon_cashback_reconciliation
  edge_type: HAS_WORKFLOW_STEP
  source: business_process.flipkart.marketplace_reconciliation_pipeline
  target: workflow_step.flipkart.recon_cashback_reconciliation
  fields:
    edge_family: process_understanding
    evidence_basis: workflow_step.fields.process_id
    confidence: high
    canonical_cognee_edge: true
    marketplace_only: true
    canonical_edge_type: HAS_WORKFLOW_STEP
    inverse_edge_type: BELONGS_TO_PROCESS
    materialize_inverse: true
    edge_class: canonical
    source_type: business_process
    target_type: workflow_step
```

```yaml
candidate_edge:
  edge_id: edge.workflow_step.flipkart.recon_cashback_reconciliation.belongs_to_process.business_process.flipkart.marketplace_reconciliation_pipeline
  edge_type: BELONGS_TO_PROCESS
  source: workflow_step.flipkart.recon_cashback_reconciliation
  target: business_process.flipkart.marketplace_reconciliation_pipeline
  fields:
    edge_family: process_understanding
    evidence_basis: workflow_step.fields.process_id
    confidence: high
    canonical_cognee_edge: true
    marketplace_only: true
    canonical_edge_type: BELONGS_TO_PROCESS
    inverse_edge_type: HAS_WORKFLOW_STEP
    materialize_inverse: true
    edge_class: canonical
    source_type: workflow_step
    target_type: business_process
    legacy_edge_aliases:
    - step_in_process
```

```yaml
candidate_edge:
  edge_id: edge.business_process.flipkart.marketplace_reconciliation_pipeline.has_workflow_step.workflow_step.flipkart.recon_settlement_verification
  edge_type: HAS_WORKFLOW_STEP
  source: business_process.flipkart.marketplace_reconciliation_pipeline
  target: workflow_step.flipkart.recon_settlement_verification
  fields:
    edge_family: process_understanding
    evidence_basis: workflow_step.fields.process_id
    confidence: high
    canonical_cognee_edge: true
    marketplace_only: true
    canonical_edge_type: HAS_WORKFLOW_STEP
    inverse_edge_type: BELONGS_TO_PROCESS
    materialize_inverse: true
    edge_class: canonical
    source_type: business_process
    target_type: workflow_step
```

```yaml
candidate_edge:
  edge_id: edge.workflow_step.flipkart.recon_settlement_verification.belongs_to_process.business_process.flipkart.marketplace_reconciliation_pipeline
  edge_type: BELONGS_TO_PROCESS
  source: workflow_step.flipkart.recon_settlement_verification
  target: business_process.flipkart.marketplace_reconciliation_pipeline
  fields:
    edge_family: process_understanding
    evidence_basis: workflow_step.fields.process_id
    confidence: high
    canonical_cognee_edge: true
    marketplace_only: true
    canonical_edge_type: BELONGS_TO_PROCESS
    inverse_edge_type: HAS_WORKFLOW_STEP
    materialize_inverse: true
    edge_class: canonical
    source_type: workflow_step
    target_type: business_process
    legacy_edge_aliases:
    - step_in_process
```

```yaml
candidate_edge:
  edge_id: edge.business_process.flipkart.return_cancel_reversal.has_workflow_step.workflow_step.flipkart.return_cashback_reversal
  edge_type: HAS_WORKFLOW_STEP
  source: business_process.flipkart.return_cancel_reversal
  target: workflow_step.flipkart.return_cashback_reversal
  fields:
    edge_family: process_understanding
    evidence_basis: workflow_step.fields.process_id
    confidence: high
    canonical_cognee_edge: true
    marketplace_only: true
    canonical_edge_type: HAS_WORKFLOW_STEP
    inverse_edge_type: BELONGS_TO_PROCESS
    materialize_inverse: true
    edge_class: canonical
    source_type: business_process
    target_type: workflow_step
```

```yaml
candidate_edge:
  edge_id: edge.workflow_step.flipkart.return_cashback_reversal.belongs_to_process.business_process.flipkart.return_cancel_reversal
  edge_type: BELONGS_TO_PROCESS
  source: workflow_step.flipkart.return_cashback_reversal
  target: business_process.flipkart.return_cancel_reversal
  fields:
    edge_family: process_understanding
    evidence_basis: workflow_step.fields.process_id
    confidence: high
    canonical_cognee_edge: true
    marketplace_only: true
    canonical_edge_type: BELONGS_TO_PROCESS
    inverse_edge_type: HAS_WORKFLOW_STEP
    materialize_inverse: true
    edge_class: canonical
    source_type: workflow_step
    target_type: business_process
    legacy_edge_aliases:
    - step_in_process
```

```yaml
candidate_edge:
  edge_id: edge.business_process.flipkart.return_cancel_reversal.has_workflow_step.workflow_step.flipkart.return_refund_settlement_component
  edge_type: HAS_WORKFLOW_STEP
  source: business_process.flipkart.return_cancel_reversal
  target: workflow_step.flipkart.return_refund_settlement_component
  fields:
    edge_family: process_understanding
    evidence_basis: workflow_step.fields.process_id
    confidence: high
    canonical_cognee_edge: true
    marketplace_only: true
    canonical_edge_type: HAS_WORKFLOW_STEP
    inverse_edge_type: BELONGS_TO_PROCESS
    materialize_inverse: true
    edge_class: canonical
    source_type: business_process
    target_type: workflow_step
```

```yaml
candidate_edge:
  edge_id: edge.workflow_step.flipkart.return_refund_settlement_component.belongs_to_process.business_process.flipkart.return_cancel_reversal
  edge_type: BELONGS_TO_PROCESS
  source: workflow_step.flipkart.return_refund_settlement_component
  target: business_process.flipkart.return_cancel_reversal
  fields:
    edge_family: process_understanding
    evidence_basis: workflow_step.fields.process_id
    confidence: high
    canonical_cognee_edge: true
    marketplace_only: true
    canonical_edge_type: BELONGS_TO_PROCESS
    inverse_edge_type: HAS_WORKFLOW_STEP
    materialize_inverse: true
    edge_class: canonical
    source_type: workflow_step
    target_type: business_process
    legacy_edge_aliases:
    - step_in_process
```

```yaml
candidate_edge:
  edge_id: edge.rule.flipkart.fulfilment_fee_segmentation.applies_to_platform_context.platform_context.flipkart.in
  edge_type: APPLIES_TO_PLATFORM_CONTEXT
  source: rule.flipkart.fulfilment_fee_segmentation
  target: platform_context.flipkart.in
  fields:
    edge_family: rule_understanding
    evidence_basis: rule.fields.applies_to / v9 refactor
    confidence: high
    canonical_cognee_edge: true
    marketplace_only: true
    canonical_edge_type: APPLIES_TO_PLATFORM_CONTEXT
    inverse_edge_type: HAS_APPLICABLE_RULE
    materialize_inverse: false
    edge_class: canonical
    source_type: rule
    target_type: platform_context
```

```yaml
candidate_edge:
  edge_id: edge.rule.flipkart.shopsy_zero_commission.applies_to_platform_context.platform_context.flipkart.in
  edge_type: APPLIES_TO_PLATFORM_CONTEXT
  source: rule.flipkart.shopsy_zero_commission
  target: platform_context.flipkart.in
  fields:
    edge_family: rule_understanding
    evidence_basis: rule.fields.applies_to / v9 refactor
    confidence: high
    canonical_cognee_edge: true
    marketplace_only: true
    canonical_edge_type: APPLIES_TO_PLATFORM_CONTEXT
    inverse_edge_type: HAS_APPLICABLE_RULE
    materialize_inverse: false
    edge_class: canonical
    source_type: rule
    target_type: platform_context
```

```yaml
candidate_edge:
  edge_id: edge.rule.flipkart.prepaid_postpaid_collection_fee.applies_to_platform_context.platform_context.flipkart.in
  edge_type: APPLIES_TO_PLATFORM_CONTEXT
  source: rule.flipkart.prepaid_postpaid_collection_fee
  target: platform_context.flipkart.in
  fields:
    edge_family: rule_understanding
    evidence_basis: rule.fields.applies_to / v9 refactor
    confidence: high
    canonical_cognee_edge: true
    marketplace_only: true
    canonical_edge_type: APPLIES_TO_PLATFORM_CONTEXT
    inverse_edge_type: HAS_APPLICABLE_RULE
    materialize_inverse: false
    edge_class: canonical
    source_type: rule
    target_type: platform_context
```

```yaml
candidate_edge:
  edge_id: edge.rule.flipkart.seller_tier_guidance_only.applies_to_platform_context.platform_context.flipkart.in
  edge_type: APPLIES_TO_PLATFORM_CONTEXT
  source: rule.flipkart.seller_tier_guidance_only
  target: platform_context.flipkart.in
  fields:
    edge_family: rule_understanding
    evidence_basis: rule.fields.applies_to / v9 refactor
    confidence: high
    canonical_cognee_edge: true
    marketplace_only: true
    canonical_edge_type: APPLIES_TO_PLATFORM_CONTEXT
    inverse_edge_type: HAS_APPLICABLE_RULE
    materialize_inverse: false
    edge_class: canonical
    source_type: rule
    target_type: platform_context
```

```yaml
candidate_edge:
  edge_id: edge.rule.flipkart.benchmark_guidance_only.applies_to_platform_context.platform_context.flipkart.in
  edge_type: APPLIES_TO_PLATFORM_CONTEXT
  source: rule.flipkart.benchmark_guidance_only
  target: platform_context.flipkart.in
  fields:
    edge_family: rule_understanding
    evidence_basis: rule.fields.applies_to / v9 refactor
    confidence: high
    canonical_cognee_edge: true
    marketplace_only: true
    canonical_edge_type: APPLIES_TO_PLATFORM_CONTEXT
    inverse_edge_type: HAS_APPLICABLE_RULE
    materialize_inverse: false
    edge_class: canonical
    source_type: rule
    target_type: platform_context
```

```yaml
candidate_edge:
  edge_id: edge.rule.flipkart.benchmark_guidance_only.applies_to_metric.metric.realization_rate
  edge_type: APPLIES_TO_METRIC
  source: rule.flipkart.benchmark_guidance_only
  target: metric.realization_rate
  fields:
    edge_family: metric_understanding
    evidence_basis: benchmark_card_manifest
    confidence: high
    canonical_cognee_edge: true
    marketplace_only: true
    canonical_edge_type: APPLIES_TO_METRIC
    inverse_edge_type: RELATED_TO
    materialize_inverse: false
    edge_class: canonical
    source_type: rule
    target_type: metric
```

```yaml
candidate_edge:
  edge_id: edge.rule.flipkart.benchmark_guidance_only.applies_to_metric.metric.return_rate
  edge_type: APPLIES_TO_METRIC
  source: rule.flipkart.benchmark_guidance_only
  target: metric.return_rate
  fields:
    edge_family: metric_understanding
    evidence_basis: benchmark_card_manifest
    confidence: high
    canonical_cognee_edge: true
    marketplace_only: true
    canonical_edge_type: APPLIES_TO_METRIC
    inverse_edge_type: RELATED_TO
    materialize_inverse: false
    edge_class: canonical
    source_type: rule
    target_type: metric
```


## 7. SQL Pattern Registry

```yaml
sql_pattern:
  ref: sql.flipkart.realization_rate
  name: Flipkart realization rate
  intent: Net settlement divided by sale settled amount
  sql: |
    SELECT
      SUM(settled_amount) / NULLIF(SUM(sale_settled_amount), 0) AS realization_rate
    FROM zs_observe.flipkart_settlement
    WHERE is_active = true;
```

```yaml
sql_pattern:
  ref: sql.flipkart.settlement_by_fulfilment
  name: Flipkart settlement by fulfilment
  intent: Settlement and fee by fulfilment and NEFT type
  sql: |
    SELECT
      fulfilment_type,
      neft_type,
      COUNT(*) AS rows,
      SUM(settled_amount) AS total_settled,
      SUM(sale_settled_amount) AS total_sale,
      SUM(mp_fee) AS total_marketplace_fee,
      SUM(settled_amount) / NULLIF(SUM(sale_settled_amount), 0) AS realization_rate
    FROM zs_observe.flipkart_settlement
    WHERE is_active = true
    GROUP BY fulfilment_type, neft_type;
```

```yaml
sql_pattern:
  ref: sql.flipkart.settlement_cycle
  name: Flipkart settlement cycle
  intent: Average settlement lag using created_date fallback
  caveats: Dispatch date is preferable if available; created_date is deterministic fallback.
  sql: |
    SELECT
      AVG(DATE_DIFF('day', created_date, settlement_date)) AS avg_settlement_cycle_days
    FROM zs_observe.flipkart_settlement
    WHERE is_active = true
      AND settlement_date IS NOT NULL;
```

```yaml
sql_pattern:
  ref: sql.flipkart.fee_by_description
  name: Flipkart fee by description
  intent: Detailed fee breakdown from commission table
  sql: |
    SELECT
      description,
      SUM(charged_amount) AS fee_amount,
      SUM(total_tax) AS fee_tax
    FROM zs_observe.flipkart_commission
    WHERE is_active = true
    GROUP BY description;
```

```yaml
sql_pattern:
  ref: sql.flipkart.fee_pivot
  name: Flipkart fee pivot
  intent: Fee type pivot from commission table
  sql: |
    SELECT
      order_id,
      item_id,
      SUM(CASE WHEN description = 'Commission' THEN charged_amount ELSE 0 END) AS commission_fee,
      SUM(CASE WHEN description = 'Fixed Fee' THEN charged_amount ELSE 0 END) AS fixed_fee,
      SUM(CASE WHEN description = 'Shipping Fee' THEN charged_amount ELSE 0 END) AS shipping_fee,
      SUM(CASE WHEN description = 'Reverse Shipping Fee' THEN charged_amount ELSE 0 END) AS reverse_shipping_fee,
      SUM(CASE WHEN description = 'Collection Fee' THEN charged_amount ELSE 0 END) AS collection_fee,
      SUM(total_tax) AS fee_tax
    FROM zs_observe.flipkart_commission
    WHERE is_active = true
    GROUP BY order_id, item_id;
```

```yaml
sql_pattern:
  ref: sql.flipkart.settlement_commission_recon
  name: Flipkart settlement to commission fee reconciliation
  intent: Compare settlement mp_fee to commission detail using OD normalization
  sql: |
    WITH commission_detail AS (
      SELECT
        order_id,
        item_id,
        SUM(charged_amount + COALESCE(total_tax, 0)) AS commission_fee_total
      FROM zs_observe.flipkart_commission
      WHERE is_active = true
      GROUP BY order_id, item_id
    )
    SELECT
      s.order_id,
      s.item_id,
      s.mp_fee,
      c.commission_fee_total,
      s.mp_fee - c.commission_fee_total AS variance
    FROM zs_observe.flipkart_settlement s
    LEFT JOIN commission_detail c
      ON c.order_id = REPLACE(s.order_id, 'OD', '')
     AND c.item_id = s.item_id
    WHERE s.is_active = true
      AND ABS(COALESCE(s.mp_fee, 0) - COALESCE(c.commission_fee_total, 0)) > 0.01;
```

```yaml
sql_pattern:
  ref: sql.flipkart.cashback_net
  name: Flipkart net cashback
  intent: Signed cashback / promo impact
  sql: |
    SELECT
      SUM(charged_amount) AS net_cashback
    FROM zs_observe.flipkart_cashback
    WHERE is_active = true;
```

```yaml
sql_pattern:
  ref: sql.flipkart.cashback_doc_type
  name: Flipkart cashback by document type
  intent: Credit/debit note analysis
  sql: |
    SELECT
      transaction_type,
      document_type,
      document_sub_type,
      SUM(charged_amount) AS amount,
      COUNT(*) AS rows
    FROM zs_observe.flipkart_cashback
    WHERE is_active = true
    GROUP BY transaction_type, document_type, document_sub_type;
```

```yaml
sql_pattern:
  ref: sql.flipkart.cashback_rate
  name: Flipkart cashback rate
  intent: Cashback as percentage of OMS order value
  caveats: OMS schema is review-required.
  sql: |
    WITH cashback AS (
      SELECT order_id, item_id, SUM(charged_amount) AS cashback_amount
      FROM zs_observe.flipkart_cashback
      WHERE is_active = true
      GROUP BY order_id, item_id
    )
    SELECT
      SUM(c.cashback_amount) / NULLIF(SUM(o.charged_amount), 0) AS cashback_rate
    FROM zs_recon_processor.flipkart_oms o
    LEFT JOIN cashback c
      ON c.order_id = o.order_id
     AND c.item_id = o.item_id
    WHERE o.is_active = true;
```

```yaml
sql_pattern:
  ref: sql.flipkart.shopsy_cashback
  name: Flipkart Shopsy cashback comparison
  intent: Compare Shopsy and non-Shopsy cashback
  sql: |
    SELECT
      is_shopsy_order_,
      SUM(charged_amount) AS cashback_amount,
      COUNT(*) AS rows
    FROM zs_observe.flipkart_cashback
    WHERE is_active = true
    GROUP BY is_shopsy_order_;
```

```yaml
sql_pattern:
  ref: sql.flipkart.cashback_settlement_offer_recon
  name: Flipkart cashback to settlement offer reconciliation
  intent: Compare cashback to settlement offer fields
  caveats: Source also references zs_refined.flipkart_settlement; use primary table unless deployment says otherwise.
  sql: |
    WITH cashback AS (
      SELECT order_id, item_id, SUM(charged_amount) AS cashback_amount
      FROM zs_observe.flipkart_cashback
      WHERE is_active = true
      GROUP BY order_id, item_id
    )
    SELECT
      s.order_id,
      s.item_id,
      c.cashback_amount,
      COALESCE(s.offer_settled_amount, 0) + COALESCE(s.offer_adjustment_settled_amount, 0) AS settlement_offer_amount,
      c.cashback_amount - (COALESCE(s.offer_settled_amount, 0) + COALESCE(s.offer_adjustment_settled_amount, 0)) AS variance
    FROM zs_observe.flipkart_settlement s
    LEFT JOIN cashback c
      ON c.order_id = s.order_id
     AND c.item_id = s.item_id
    WHERE s.is_active = true;
```

```yaml
sql_pattern:
  ref: sql.flipkart.monthly_settlement
  name: Flipkart monthly settlement summary
  intent: Monthly settled and sale amount
  sql: |
    SELECT
      DATE_TRUNC('month', settlement_date) AS settlement_month,
      SUM(settled_amount) AS total_settled,
      SUM(sale_settled_amount) AS total_sale,
      SUM(mp_fee) AS total_marketplace_fee,
      SUM(total_tcs_amount) AS total_tcs,
      SUM(total_tds_amount) AS total_tds
    FROM zs_observe.flipkart_settlement
    WHERE is_active = true
    GROUP BY 1
    ORDER BY 1;
```

```yaml
sql_pattern:
  ref: sql.flipkart.oms_gmv_review
  name: Flipkart OMS GMV review-required implementation
  intent: GMV from verified OMS forward rows
  sql: "SELECT SUM(charged_amount) AS gmv\nFROM zs_recon_processor.flipkart_oms\nWHERE is_active = true\n  AND transaction_type = 'forward';"
```

```yaml
sql_pattern:
  ref: sql.flipkart.settlement_gmv_fallback
  name: Flipkart settlement GMV fallback
  intent: Gross sale proxy from settlement sale component
  sql: 'SELECT SUM(sale_settled_amount) AS gross_sale_proxy

    FROM zs_observe.flipkart_settlement

    WHERE is_active = true;'
```

```yaml
sql_pattern:
  ref: sql.flipkart.net_settlement
  name: Flipkart net settlement
  intent: Net settlement from settled_amount
  sql: 'SELECT SUM(settled_amount) AS net_settlement

    FROM zs_observe.flipkart_settlement

    WHERE is_active = true;'
```

```yaml
sql_pattern:
  ref: sql.flipkart.effective_fee_rate
  name: Flipkart effective fee rate
  intent: Marketplace fee burden from settlement mp_fee
  sql: 'SELECT ABS(SUM(mp_fee)) / NULLIF(SUM(sale_settled_amount), 0) AS effective_fee_rate

    FROM zs_observe.flipkart_settlement

    WHERE is_active = true;'
```

```yaml
sql_pattern:
  ref: sql.flipkart.marketplace_fee_total
  name: Flipkart marketplace fee total
  intent: Aggregate mp_fee from settlement
  sql: 'SELECT SUM(mp_fee) AS marketplace_fee_total

    FROM zs_observe.flipkart_settlement

    WHERE is_active = true;'
```

```yaml
sql_pattern:
  ref: sql.flipkart.commission_fee_detail
  name: Flipkart commission_fee_detail
  intent: Commission fee detail from commission invoices
  sql: "SELECT SUM(charged_amount) AS fee_amount\nFROM zs_observe.flipkart_commission\nWHERE is_active = true\n  AND description = 'Commission';"
```

```yaml
sql_pattern:
  ref: sql.flipkart.fixed_fee_detail
  name: Flipkart fixed_fee_detail
  intent: Fixed Fee fee detail from commission invoices
  sql: "SELECT SUM(charged_amount) AS fee_amount\nFROM zs_observe.flipkart_commission\nWHERE is_active = true\n  AND description = 'Fixed Fee';"
```

```yaml
sql_pattern:
  ref: sql.flipkart.shipping_fee_detail
  name: Flipkart shipping_fee_detail
  intent: Shipping Fee fee detail from commission invoices
  sql: "SELECT SUM(charged_amount) AS fee_amount\nFROM zs_observe.flipkart_commission\nWHERE is_active = true\n  AND description = 'Shipping Fee';"
```

```yaml
sql_pattern:
  ref: sql.flipkart.reverse_shipping_fee_detail
  name: Flipkart reverse_shipping_fee_detail
  intent: Reverse Shipping Fee fee detail from commission invoices
  sql: "SELECT SUM(charged_amount) AS fee_amount\nFROM zs_observe.flipkart_commission\nWHERE is_active = true\n  AND description = 'Reverse Shipping\
    \ Fee';"
```

```yaml
sql_pattern:
  ref: sql.flipkart.collection_fee_detail
  name: Flipkart collection_fee_detail
  intent: Collection Fee fee detail from commission invoices
  sql: "SELECT SUM(charged_amount) AS fee_amount\nFROM zs_observe.flipkart_commission\nWHERE is_active = true\n  AND description = 'Collection\
    \ Fee';"
```

```yaml
sql_pattern:
  ref: sql.flipkart.tcs_deducted
  name: Flipkart TCS deducted
  intent: TCS deduction from settlement
  sql: 'SELECT SUM(total_tcs_amount) AS tcs_deducted

    FROM zs_observe.flipkart_settlement

    WHERE is_active = true;'
```

```yaml
sql_pattern:
  ref: sql.flipkart.tds_deducted
  name: Flipkart TDS deducted
  intent: TDS deduction from settlement
  sql: 'SELECT SUM(total_tds_amount) AS tds_deducted

    FROM zs_observe.flipkart_settlement

    WHERE is_active = true;'
```

```yaml
sql_pattern:
  ref: sql.flipkart.gst_on_mp_fees
  name: Flipkart GST on marketplace fees
  intent: GST on marketplace fees from settlement
  sql: 'SELECT SUM(gst_on_mp_fees) AS gst_on_marketplace_fees

    FROM zs_observe.flipkart_settlement

    WHERE is_active = true;'
```

```yaml
sql_pattern:
  ref: sql.flipkart.fee_tax_detail
  name: Flipkart commission fee tax detail
  intent: GST/tax on commission fee invoice detail
  sql: 'SELECT SUM(total_tax) AS total_tax_on_fee

    FROM zs_observe.flipkart_commission

    WHERE is_active = true;'
```

```yaml
sql_pattern:
  ref: sql.flipkart.return_rate
  name: Flipkart settlement return-rate proxy
  intent: Settlement-based return rate proxy
  sql: "SELECT\n  COUNT(DISTINCT CASE WHEN return_type IS NOT NULL OR refund_settled_amount < 0 THEN order_id END)\n    / NULLIF(COUNT(DISTINCT\
    \ CASE WHEN sale_settled_amount > 0 THEN order_id END), 0) AS return_rate\nFROM zs_observe.flipkart_settlement\nWHERE is_active = true;"
```

```yaml
sql_pattern:
  ref: sql.flipkart.cancellation_rate
  name: Flipkart cashback cancellation signal rate
  intent: Cancellation signal from cashback debit notes
  sql: "SELECT\n  COUNT(DISTINCT CASE WHEN transaction_type = 'forward cancel' OR document_sub_type = 'Cancellation' THEN order_id END)\n    /\
    \ NULLIF(COUNT(DISTINCT CASE WHEN transaction_type = 'forward' THEN order_id END), 0) AS cancellation_rate_signal\nFROM zs_observe.flipkart_cashback\n\
    WHERE is_active = true;"
```

```yaml
sql_pattern:
  ref: sql.flipkart.protection_fund_settlement
  name: Flipkart protection fund settlement
  intent: Protection fund settlement component
  sql: 'SELECT SUM(protection_fund_settled_amount) AS protection_fund_settlement

    FROM zs_observe.flipkart_settlement

    WHERE is_active = true;'
```

```yaml
sql_pattern:
  ref: sql.flipkart.settlement_waterfall_v9
  name: Flipkart settlement waterfall v9
  intent: Documented settlement component waterfall including all credits and debits
  sql: "SELECT\n  order_id,\n  item_id,\n  settled_amount,\n  COALESCE(sale_settled_amount, 0)\n    + COALESCE(refund_settled_amount, 0)\n   \
    \ + COALESCE(offer_settled_amount, 0)\n    + COALESCE(my_share_settled_amount, 0)\n    + COALESCE(addon_settled_amount, 0)\n    + COALESCE(taxes_settled_amount,\
    \ 0)\n    + COALESCE(offer_adjustment_settled_amount, 0)\n    + COALESCE(protection_fund_settled_amount, 0)\n    - ABS(COALESCE(mp_fee, 0))\n\
    \    - ABS(COALESCE(gst_on_mp_fees, 0))\n    - ABS(COALESCE(total_tcs_amount, 0))\n    - ABS(COALESCE(total_tds_amount, 0)) AS component_sum,\n\
    \  settled_amount - (\n    COALESCE(sale_settled_amount, 0)\n    + COALESCE(refund_settled_amount, 0)\n    + COALESCE(offer_settled_amount,\
    \ 0)\n    + COALESCE(my_share_settled_amount, 0)\n    + COALESCE(addon_settled_amount, 0)\n    + COALESCE(taxes_settled_amount, 0)\n    +\
    \ COALESCE(offer_adjustment_settled_amount, 0)\n    + COALESCE(protection_fund_settled_amount, 0)\n    - ABS(COALESCE(mp_fee, 0))\n    - ABS(COALESCE(gst_on_mp_fees,\
    \ 0))\n    - ABS(COALESCE(total_tcs_amount, 0))\n    - ABS(COALESCE(total_tds_amount, 0))\n  ) AS variance\nFROM zs_observe.flipkart_settlement\n\
    WHERE is_active = true;"
```


## 8. Review Item Registry

```yaml
review_item:
  id: review.flipkart.oms_schema_inconsistency
  severity: high
  issue: The DOCX section labelled flipkart_oms contains cashback-like column descriptions and not a complete OMS schema.
  deterministic_action: Keep OMS schema partial/review-required; use OMS only where source query examples or reconciliation framework explicitly
    support order semantics. Do not invent complete OMS schema from cashback-like table body.
  affected_cards: table.flipkart.oms, metric_implementation.flipkart.gmv.oms
  status: open
```

```yaml
review_item:
  id: review.flipkart.settlement_schema_alias
  severity: medium
  issue: Source text and SQL references use both zs_observe.flipkart_settlement and zs_refined.flipkart_settlement.
  deterministic_action: Use zs_observe.flipkart_settlement as canonical primary table; preserve zs_refined.flipkart_settlement as source alias/caveat
    in table and SQL notes.
  affected_cards: table.flipkart.settlement, query patterns
  status: resolved
```

```yaml
review_item:
  id: review.flipkart.dispatch_date_missing
  severity: medium
  issue: Settlement cycle should ideally start from dispatch date, but source examples use created_date to settlement_date.
  deterministic_action: Use created_date as deterministic fallback for settlement cycle metric and keep dispatch-date dependency open because
    payout cycle starts from dispatch date in business prose.
  affected_cards: metric_implementation.flipkart.settlement_cycle_days
  status: open
```

```yaml
review_item:
  id: review.flipkart.seller_tier_column_missing
  severity: medium
  issue: Seller-tier payout cycle is described conceptually but no reliable seller tier column is specified in the schema excerpts.
  deterministic_action: Do not create seller-tier business_process/process_variant or accepted tier-specific implementation; retain seller tier
    as guidance-only rule until a reliable seller-tier source column exists.
  affected_cards: rule.flipkart.seller_tier_guidance_only, metric_implementation.flipkart.settlement_cycle_days, column.settlement.tier
  status: open
```

```yaml
review_item:
  id: review.flipkart.net_margin_external_dependency
  severity: medium
  issue: Net margin requires product cost/COGS, which is not marketplace-owned in the DOCX.
  deterministic_action: Do not create net margin implementation from marketplace DOCX alone because COGS is external to marketplace semantics.
  affected_cards: metric.net_margin excluded
  status: resolved
```

```yaml
review_item:
  id: review.flipkart.reconciliation_tolerance
  severity: medium
  issue: Several reconciliation examples imply a numeric tolerance; 0.01 appears in SQL examples but is not universally declared.
  deterministic_action: Use 0.01 only for SQL examples that explicitly contain it; otherwise keep tolerance review-required.
  affected_cards: reconciliation profiles and matching logic
  status: open
```

```yaml
review_item:
  id: review.flipkart.cashback_null_document_policy
  severity: low
  issue: Cashback document_type and document_sub_type can be null.
  deterministic_action: Keep null as a known documented cashback document_type/document_sub_type value and do not coerce to Unknown.
  affected_cards: value_profile.flipkart.cashback.document_type, value_profile.flipkart.cashback.document_sub_type
  status: resolved
```

```yaml
review_item:
  id: review.flipkart.group_scope_external
  severity: medium
  issue: group_level_id/group_id are present, but marketplace document should not create account binding.
  deterministic_action: Document group_level_id values on column/value-profile cards as scope identifiers; runtime account/scope selection remains
    outside marketplace markdown.
  affected_cards: columns with group scope
  status: open
```

## 9. Quality Gates for Deterministic Parser Output

1. All candidate_card blocks use only allowed marketplace card types.
2. No tenant, group, platform_account, account_data_binding, business_scope_set, or business_flow_binding card is emitted.
3. All table, column, metric, process, reconciliation, rule, validation, and query cards remain marketplace-specific.
4. External identifiers such as group_level_id, group_id, NEFT fields, GSTIN, and fulfilment/shipping values remain columns/caveats only.
5. Every metric has colloquial names and every platform-specific metric implementation references source tables, formulas, filters, grain, sign handling, and caveats.
6. Reconciliation cards are marketplace-internal only and include sides, unit, matching logic, mismatch categories, tolerance/date-window handling, and out-of-scope cross-domain notes.
7. The OMS source inconsistency is preserved as a review item, not silently repaired.
8. Commission order_id OD-prefix normalization and many-side pre-aggregation are explicit rules, constraints, and validation tests.
9. Candidate edges are not optional: every table column, value profile, metric implementation, query pattern, process step, reconciliation side, and reconciliation profile must be attached through unified typed edges.
10. Every edge must declare `canonical_edge_type`, `inverse_edge_type`, `materialize_inverse`, `source_type`, `target_type`, and `edge_class`.
11. Legacy parser-helper edge names may appear only as `legacy_edge_aliases`; they must not replace canonical `edge_type`.
12. Embedded parent/child references are expanded into explicit candidate_edge blocks for deterministic graph ingestion.

## 10. Candidate Coverage Summary

| card_type | count |
|---|---:|
| `platform` | 1 |
| `platform_context` | 1 |
| `domain` | 8 |
| `table` | 4 |
| `column` | 89 |
| `relationship` | 6 |
| `value_profile` | 11 |
| `metric` | 22 |
| `metric_implementation` | 21 |
| `formula_template` | 8 |
| `metric_dependency` | 5 |
| `business_process` | 5 |
| `workflow_step` | 13 |
| `state_transition` | 2 |
| `process_variant` | 0 |
| `reconciliation_profile` | 5 |
| `reconciliation_side` | 10 |
| `reconciliation_unit` | 5 |
| `matching_logic` | 5 |
| `mismatch_category` | 10 |
| `reconciliation_variant` | 4 |
| `query_pattern` | 15 |
| `rule` | 17 |
| `validation_test` | 10 |
| `output_contract` | 6 |
| `execution_constraint_set` | 8 |

Total candidate cards: **291**  
Total candidate edges: **870**  
Evidence items: **0**  
Review items: **8**  
Open review items: **5**  
SQL patterns: **30**

```yaml
parser_quality_manifest:
  candidate_cards: 291
  candidate_edges: 870
  source_evidence_count: 0
  sql_patterns: 30
  missing_edge_references: 0
  dangling_sql_refs: 0
  deleted_card_references: 0
  open_reviews: 5
  lazy_workflow_steps: 0
  placeholder_metric_formulas: 0
  unsupported_metric_implementations: 0
  process_variant_cards: 0
  process_variants_review_required: 0
  hard_threshold_benchmarks_without_rule: 0
  forbidden_scope_cards_from_scope_ids: 0
  unsupported_docx_columns_removed:
    - column.settlement.report_end_date
    - column.commission.commission_rate
    - column.commission.base_price
    - column.commission.rebate_amount
    - column.commission.insertion_date
    - column.commission.report_end_date
    - column.cashback.posted_date
    - column.cashback.order_date
    - column.cashback.buyer_gstin
```
